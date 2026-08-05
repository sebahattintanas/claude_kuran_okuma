#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sesli_sinav2.py — SESLİ KATMANI, İKİNCİ DENEME (LPC'siz)
=========================================================
BİRİNCİ DENEME NEDEN ÇÖKTÜ (sesli_sinav.py):
  LPC formant kestirimi gerçek seste İMKÂNSIZ değerler üretti (F1=1524 Hz;
  insan seslisinde F1 tavanı ~900 Hz). Muhtemel sebep: LPC, formant yerine
  F0 harmoniğine kilitleniyor (110 Hz × 14 ≈ 1540).
  Ve aletim yalnızca KENDİ sentezimde doğrulanmıştı — döngüsel doğrulama:
  sentezleyicim 3 temiz rezonatör koyuyor, çıkarıcım 3 temiz rezonatör buluyor.
  Gerçek konuşma öyle değil. O null bir MODEL null'ı değil, ALET arızasıydı.

BU DENEME:
  Formant KESTİRMİYOR. Sadece enerjinin nerede olduğuna bakıyor.
  Fizik: â'nın F1'i yüksek (~750 Hz), î ve û'nunki düşük (~280-320).
  → â ağırlıklı ayette, ötümlü çerçevelerin spektral ağırlık merkezi YUKARIDA.
  (Not: merkez F2'yi değil F1'i izliyor — ilk tahminim tersiydi, ölçüm düzeltti.)

  SINIRI, baştan: â'yı (î,û)'dan ayırır; î ile û'yu AYIRAMAZ (F1'leri neredeyse aynı).
  Yani 3'lü değil, 2'li bir test: "â mı, değil mi".

TAVAN (kendi sentezimde, gerçeği bilerek ölçüldü):
  tüm çerçeveler      r=+0.53
  sadece ötümlü       r=+0.84   ← bu yöntemin ULAŞABİLECEĞİ EN İYİ
  Gerçek seste bundan İYİ olamaz. Belirgin biçimde düşükse, ölçemedik demektir.

BEKLENTİ (önceden yazıldı, sonuç ne olursa değişmeyecek):
  - İşaret POZİTİF olmalı (â çok → merkez yukarı).
  - Gerçek seste r ~0.3-0.6 beklerim; tavan 0.84 ve gerçek ses gürültülü.
  - NULL ÇIKABİLİR. Çıkarsa "ölçemedik" deriz, "model yanlış" demeyiz.
  - EN BÜYÜK TEHDİT: makam. Kārî perdeyi gezdirir; F0 değişimi merkezi kaydırır.
    Bunu ölçeceğiz (F0 ile merkez korele mi) ve gerekirse F0'ı kontrol edeceğiz.

KURULUM:  audio/1/*.mp3  audio/2/*.mp3  kuran_veri.json  tilavet_sentez.py
          pip install librosa numpy scipy
ÇALIŞTIRMA:  python sesli_sinav2.py
"""
import os, sys, json, warnings
warnings.filterwarnings('ignore')
import numpy as np
try:
    import librosa
    from scipy import stats
except ImportError as e:
    sys.exit("[!] eksik: %s\n    pip install librosa numpy scipy"%e)

SURE=50; SR=22050; TAVAN=0.84

def model_oranlari():
    import importlib.util
    if not os.path.exists('tilavet_sentez.py'):
        sys.exit("[!] tilavet_sentez.py bu klasörde olmalı")
    spec=importlib.util.spec_from_file_location('ts','tilavet_sentez.py')
    ts=importlib.util.module_from_spec(spec); spec.loader.exec_module(ts)
    veri=json.load(open('kuran_veri.json',encoding='utf-8'))
    s=next(x for x in veri['sureler'] if x['no']==SURE)
    out={}
    for a in s['ayetler']:
        _,seg=ts.sentezle_iz(a['ar_saf'], a.get('mukattaa',0))
        t={'a':0.,'i':0.,'u':0.}
        for b,e,et,tip,li in seg:
            if tip in ('sesli','med'):
                k=et[0].lower()
                if k in t: t[k]+=(e-b)
        tot=sum(t.values())
        if tot>0: out[a['no']]=t['a']/tot        # â oranı
    return out

def olc(yol):
    """(ötümlü çerçevelerin ağırlık merkezi, ortalama F0) — LPC YOK"""
    y,sr=librosa.load(yol,sr=SR,mono=True)
    y,_=librosa.effects.trim(y,top_db=35)
    if len(y)<sr*0.4: return None
    f0,vflag,_=librosa.pyin(y,fmin=60,fmax=350,sr=sr,frame_length=1024,hop_length=256)
    S=np.abs(librosa.stft(y,n_fft=1024,hop_length=256))
    fr=librosa.fft_frequencies(sr=sr,n_fft=1024)
    m=fr<3500                                    # mp3 üstünü bozuyor — girmiyoruz
    cm=(S[m].T*fr[m]).sum(1)/(S[m].sum(0)+1e-9)
    n=min(len(cm),len(vflag))
    ot=np.array([bool(v) for v in vflag[:n]])
    rms=librosa.feature.rms(y=y,frame_length=1024,hop_length=256)[0][:n]
    guc = rms>np.percentile(rms,50)
    sec = ot & guc
    if sec.sum()<10: return None
    f0v=f0[:n][sec]; f0v=f0v[~np.isnan(f0v)]
    return float(cm[:n][sec].mean()), float(np.mean(f0v)) if len(f0v) else np.nan

def main():
    print("="*70)
    print("  SESLİ KATMANI — 2. DENEME (LPC'siz, ağırlık merkezi)")
    print("  yöntemin tavanı: r=%.2f (kendi sentezimde ölçüldü)"%TAVAN)
    print("="*70)
    M=model_oranlari()
    print("\n  model: %d ayet · â oranı ort %.2f · sd %.3f · aralık %.2f-%.2f"%(
        len(M), np.mean(list(M.values())), np.std(list(M.values())),
        min(M.values()), max(M.values())))

    tum={}
    for kari in ('1','2'):
        d=os.path.join('audio',kari)
        if not os.path.isdir(d): print("\n[!] %s yok"%d); continue
        print("\n"+"="*70); print("  KÂRÎ %s"%kari); print("="*70)
        print("  ölçülüyor (pyin — yavaş)...")
        C={}; F={}
        for n in sorted(M):
            f=os.path.join(d,"%03d%03d.mp3"%(SURE,n))
            if not os.path.exists(f): continue
            r=olc(f)
            if r is None: continue
            C[n],F[n]=r
        if len(C)<15: print("  [!] yeterli veri yok"); continue
        ortak=sorted(set(M)&set(C))
        x=np.array([M[n] for n in ortak])          # model: â oranı
        y=np.array([C[n] for n in ortak])          # ses: ağırlık merkezi
        f0=np.array([F[n] for n in ortak])
        print("  %d ayet ölçüldü · merkez ort %.0f Hz (sd %.0f) · F0 ort %.0f Hz"%(
            len(ortak),y.mean(),y.std(),np.nanmean(f0)))

        print("\n  1) ASIL TEST — â oranı ↔ ağırlık merkezi")
        r,p=stats.pearsonr(x,y)
        yz=" ***" if p<0.001 else (" **" if p<0.01 else (" *" if p<0.05 else ""))
        print("     r=%+.3f  p=%.4f%s      (tavan %.2f · işaret POZİTİF olmalı)"%(r,p,yz,TAVAN))

        print("\n  2) BOŞ MODEL (ayet eşleşmeleri karıştırıldı)")
        rng=np.random.default_rng(0)
        null=[stats.pearsonr(x,rng.permutation(y))[0] for _ in range(5000)]
        pp=(np.sum(np.array(null)>=r)+1)/5001
        print("     gözlenen r=%+.3f · boş model ort %+.3f · p=%.4f"%(r,np.mean(null),pp))

        print("\n  3) TEHDİT KONTROLÜ — makam merkezi kaydırıyor mu?")
        ok=~np.isnan(f0)
        if ok.sum()>10:
            rf,pf=stats.pearsonr(f0[ok],y[ok])
            print("     r(F0, merkez) = %+.3f (p=%.3f)  ← perde, merkezi ne kadar sürüklüyor"%(rf,pf))
            # F0 etkisini çıkarıp tekrar bak
            yy=y[ok]-np.poly1d(np.polyfit(f0[ok],y[ok],1))(f0[ok])
            rc,pc=stats.pearsonr(x[ok],yy)
            print("     F0 SABİTKEN: r(â oranı, merkez | F0) = %+.3f (p=%.4f)"%(rc,pc))
        else:
            print("     F0 ölçülemedi")

        print("\n  4) YORUM")
        if p<0.05 and r>0:
            print("     → SESLİ KATMANI ÖLÇÜLDÜ. Model'in â öngörüsü gerçek seste karşılık")
            print("       buluyor (tavanın %%%.0f'i)."%(100*r/TAVAN))
        elif p<0.05 and r<0:
            print("     → TERS İŞARET. Beklenen pozitifti. Bir şey yanlış — yorumlamıyorum.")
        else:
            print("     → NULL: ölçemedik. Model YANLIŞ demek DEĞİL — ölçemedik demek.")
            print("       (mp3 kaybı, makam gezinmesi, 45 ayet, ya da yöntem yetersiz)")
        tum[kari]=(x,y)

    if len(tum)==2:
        print("\n"+"="*70); print("  KÂRÎLER ARASI"); print("="*70)
        y1=tum['1'][1]; y2=tum['2'][1]
        n=min(len(y1),len(y2))
        r,p=stats.pearsonr(y1[:n],y2[:n])
        print("\n  r(kārî1 merkez, kārî2 merkez) = %+.3f (p=%.4f)"%(r,p))
        print("  → yüksekse: ikisi aynı sesli yapısını üretiyor (metne bağlı)")
        print("    düşükse: merkez kārîye özgü şeyleri ölçüyor, metne değil")

    print("\n"+"="*70)
    print("  Çıktının tamamını yapıştır.")
    print("="*70)

if __name__=='__main__':
    main()
