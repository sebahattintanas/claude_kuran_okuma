#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sesli_sinav.py — SESLİ KATMANININ DIŞ SINAVI
=============================================
SORU: Model "bu med â", "bu med î" diyor. Gerçek kārînin ağzında da öyle mi?

NEDEN BU SEFER FARKLI:
  Önceki formant testi (formant_top_rung.py) HİZALAMA yüzünden çöktü —
  sesi parçalayıp her parçayı bir mede eşlemeye çalışmıştı, tutmadı.
  Bu test hizalamayı TAMAMEN ATLIYOR:
    model  → "bu ayetin sesli-zamanının %X'i â"      (ayet düzeyi oran)
    ses    → "bu kaydın sesli çerçevelerinin %Y'si â-benzeri"  (ayet düzeyi oran)
    test   → 45 ayet boyunca X ile Y korele mi?
  Hangi ânın hangi mede denk geldiğini BİLMEMİZ GEREKMİYOR.

TARAFSIZLIK:
  Sesli şablonlarımı dayatmıyorum. Sesliler, kārînin KENDİ sesinden
  denetimsiz kümelemeyle çıkarılıyor (KMeans, k=3). Kümeler sonra
  formant geometrisiyle â/î/û'ya bağlanıyor (â: en yüksek F1,
  î: en yüksek F2, û: en düşük F2) — bu geometri fizik, tercih değil.

BEKLENTİ (önceden yazıyorum, sonuç ne olursa değişmeyecek):
  - Mutlak oranlar TUTMAYACAK (önceki test bunu gösterdi: metin â%78,
    kārî â%38-54). Formant ölçümü gürültülü, mp3 yüksek frekansı bozuyor.
  - KRİTİK OLAN: ayetler arası KORELASYON. Model â-ağırlıklı dediği ayette
    ses de â-ağırlıklı mı? Bu r>0 ve p<0.05 çıkarsa sesli katmanı doğrulanır.
  - NULL ÇIKABİLİR. Çıkarsa: "süre metnin, ama sesli kimliğini ölçemedik" deriz.
    Bu, iskeletin anlaşılır olmasını YALANLAMAZ — sadece ölçemediğimizi söyler.

KURULUM:  audio/1/050001.mp3 …   audio/2/050001.mp3 …   kuran_veri.json
          pip install librosa scikit-learn numpy scipy
ÇALIŞTIRMA:  python sesli_sinav.py
"""
import os, sys, json, warnings
warnings.filterwarnings('ignore')
import numpy as np

try:
    import librosa
    from sklearn.cluster import KMeans
    from scipy import stats
    from scipy.signal import lfilter
except ImportError as e:
    sys.exit("[!] eksik paket: %s\n    pip install librosa scikit-learn numpy scipy"%e)

SURE=50; SR=22050
MEDS={'A':2,'B':4,'C':6}
def birim(c): return MEDS[c] if c in MEDS else int(c)

# ---------- MODELİN ÖNGÖRÜSÜ ----------
# ritim_kod harf başına: rakam=vuruş, A/B/C=med. Ama sesli KİMLİĞİ kodda yok —
# metinden yeniden çıkarmalıyız. tilavet_sentez'in çözümleyicisini kullanıyoruz.
def model_sesli_oranlari():
    import importlib.util
    if not os.path.exists('tilavet_sentez.py'):
        sys.exit("[!] tilavet_sentez.py bu klasörde olmalı (sesli kimliği ondan çıkıyor)")
    spec=importlib.util.spec_from_file_location('ts','tilavet_sentez.py')
    ts=importlib.util.module_from_spec(spec); spec.loader.exec_module(ts)
    veri=json.load(open('kuran_veri.json',encoding='utf-8'))
    s=next(x for x in veri['sureler'] if x['no']==SURE)
    out={}
    for a in s['ayetler']:
        _,seg=ts.sentezle_iz(a['ar_saf'], a.get('mukattaa',0))
        # her sesli/med segmentinin süresi, kimliğine göre toplanır
        t={'a':0.0,'i':0.0,'u':0.0}
        for b,e,et,tip,li in seg:
            if tip not in ('sesli','med'): continue
            k=et[0]                       # 'a','i','u','A','I','U'
            kk=k.lower()
            if kk in t: t[kk]+=(e-b)
        tot=sum(t.values())
        if tot<=0: continue
        out[a['no']]=dict(a=t['a']/tot, i=t['i']/tot, u=t['u']/tot, sesli_sn=tot,
                          mora=sum(birim(c) for c in a['ritim_kod']))
    return out

# ---------- SESTEN SESLİ ÇIKARMA ----------
def formant_cerceveleri(yol):
    """ötümlü, kararlı çerçevelerden (F1,F2) çıkar"""
    y,sr=librosa.load(yol,sr=SR,mono=True)
    y,_=librosa.effects.trim(y,top_db=35)
    if len(y)<sr*0.3: return np.zeros((0,2))
    f0,vflag,_=librosa.pyin(y,fmin=60,fmax=350,sr=sr,frame_length=1024,hop_length=256)
    W=int(0.030*sr); H=256
    rms=librosa.feature.rms(y=y,frame_length=W,hop_length=H)[0]
    esik=np.percentile(rms,55)
    F=[]
    for i in range(len(rms)):
        if i>=len(vflag) or not vflag[i]: continue     # ötümlü değilse atla
        if rms[i]<esik: continue                        # zayıfsa atla
        b=i*H; seg=y[b:b+W]
        if len(seg)<W: continue
        s2=lfilter([1,-0.97],1,seg*np.hamming(len(seg)))
        try: A=librosa.lpc(s2,order=14)
        except Exception: continue
        r=np.roots(A); r=r[(np.imag(r)>0.01)&(np.abs(r)<1.0)]
        if len(r)<2: continue
        f=np.sort(np.angle(r)*sr/(2*np.pi))
        f=[x for x in f if 180<x<3200]
        if len(f)<2: continue
        F.append([f[0],f[1]])
    return np.array(F)

def kumele_ve_etiketle(F):
    """denetimsiz 3 küme → formant geometrisiyle â/î/û'ya bağla"""
    if len(F)<30: return None,None
    X=np.log(F)                                   # log uzayında daha düzgün
    X=(X-X.mean(0))/(X.std(0)+1e-9)               # kārîye göre normalize
    km=KMeans(n_clusters=3,n_init=10,random_state=0).fit(X)
    mer=np.array([F[km.labels_==k].mean(0) for k in range(3)])   # gerçek Hz
    # geometri (fizik, tercih değil): â=en yüksek F1 · î=en yüksek F2 · û=en düşük F2
    etiket={}
    a_k=int(np.argmax(mer[:,0]))
    kalan=[k for k in range(3) if k!=a_k]
    i_k=max(kalan,key=lambda k:mer[k,1])
    u_k=[k for k in kalan if k!=i_k][0]
    etiket[a_k]='a'; etiket[i_k]='i'; etiket[u_k]='u'
    return km,(etiket,mer)

def main():
    print("="*70)
    print("  SESLİ KATMANININ DIŞ SINAVI — Kāf, %d ayet"%45)
    print("="*70)
    M=model_sesli_oranlari()
    print("\n  model hazır: %d ayet için sesli oranları çıkarıldı"%len(M))
    ilk=sorted(M)[:3]
    for n in ilk:
        d=M[n]; print("    50:%-3d  â %.0f%% · î %.0f%% · û %.0f%%  (sesli süresi %.1f sn)"%(
            n,100*d['a'],100*d['i'],100*d['u'],d['sesli_sn']))

    for kari in ('1','2'):
        d=os.path.join('audio',kari)
        if not os.path.isdir(d): print("\n[!] %s yok"%d); continue
        print("\n"+"="*70); print("  KÂRÎ %s"%kari); print("="*70)
        print("\n  formant çıkarılıyor (yavaş — pyin)...")
        HEP=[]; AYET={}
        for n in sorted(M):
            f=os.path.join(d,"%03d%03d.mp3"%(SURE,n))
            if not os.path.exists(f): continue
            F=formant_cerceveleri(f)
            if len(F)<20: continue
            AYET[n]=F; HEP.append(F)
        if len(AYET)<15: print("  [!] yeterli veri yok"); continue
        HEPSI=np.vstack(HEP)
        print("  %d ayet · %d sesli çerçeve"%(len(AYET),len(HEPSI)))
        km,bilgi=kumele_ve_etiketle(HEPSI)
        if km is None: print("  [!] kümeleme başarısız"); continue
        etiket,mer=bilgi
        print("\n  DENETİMSİZ KÜMELER (kārînin kendi sesinden):")
        for k in range(3):
            print("    küme %d → '%s'   F1=%4.0f Hz  F2=%4.0f Hz"%(k,etiket[k],mer[k,0],mer[k,1]))
        print("    (etiketleme geometriyle: â=en yüksek F1, î=en yüksek F2, û=en düşük F2)")

        # ayet başına ses oranları
        mu=np.log(HEPSI).mean(0); sd=np.log(HEPSI).std(0)+1e-9
        SES={}
        for n,F in AYET.items():
            lab=km.predict((np.log(F)-mu)/sd)
            c={'a':0,'i':0,'u':0}
            for l in lab: c[etiket[int(l)]]+=1
            t=sum(c.values())
            SES[n]=dict(a=c['a']/t,i=c['i']/t,u=c['u']/t,n=t)

        ortak=sorted(set(M)&set(SES))
        print("\n  1) MUTLAK ORANLAR (tutmaması BEKLENİYOR)")
        for v in ('a','i','u'):
            mm=np.mean([M[n][v] for n in ortak]); ss=np.mean([SES[n][v] for n in ortak])
            print("     %s : model %%%-4.0f  ses %%%-4.0f  fark %+.0f puan"%(v,100*mm,100*ss,100*(ss-mm)))

        print("\n  2) ASIL TEST — AYETLER ARASI KORELASYON")
        print("     (model â-ağırlıklı dediği ayette ses de â-ağırlıklı mı?)")
        sonuc={}
        for v in ('a','i','u'):
            x=np.array([M[n][v] for n in ortak]); y=np.array([SES[n][v] for n in ortak])
            if np.std(x)<1e-6 or np.std(y)<1e-6:
                print("     %s : varyans yok, atlandı"%v); continue
            r,p=stats.pearsonr(x,y); sonuc[v]=(r,p)
            yz=" ***" if p<0.001 else (" **" if p<0.01 else (" *" if p<0.05 else ""))
            print("     %s : r=%+.3f  p=%.4f%s"%(v,r,p,yz))

        # boş model: ayet etiketlerini karıştır
        print("\n  3) BOŞ MODEL (ayet eşleşmeleri karıştırıldı)")
        rng=np.random.default_rng(0)
        for v in ('a','i','u'):
            if v not in sonuc: continue
            x=np.array([M[n][v] for n in ortak]); y=np.array([SES[n][v] for n in ortak])
            null=[]
            for _ in range(3000):
                yy=rng.permutation(y)
                null.append(stats.pearsonr(x,yy)[0])
            obs=sonuc[v][0]
            p=(np.sum(np.array(null)>=obs)+1)/3001
            print("     %s : gözlenen r=%+.3f · boş model ort r=%+.3f · p=%.4f"%(v,obs,np.mean(null),p))

        print("\n  4) YORUM")
        iyi=[v for v,(r,p) in sonuc.items() if p<0.05 and r>0]
        if iyi:
            print("     → SESLİ KATMANI DOĞRULANDI (%s). Model'in sesli kimliği öngörüsü,"%", ".join(iyi))
            print("       gerçek kārînin ağzında ölçülebilir karşılık buluyor.")
        else:
            print("     → NULL: sesli kimliğini bu yöntemle ÖLÇEMEDİK.")
            print("       Bu, iskeletin anlaşılır olmasını yalanlamaz — ölçemediğimizi söyler.")
            print("       (mp3 yüksek frekans kaybı, LPC gürültüsü, 45 ayet az olabilir)")

    print("\n"+"="*70)
    print("  Çıktının tamamını yapıştır. Null çıkarsa null yazacağız.")
    print("="*70)

if __name__=='__main__':
    main()
