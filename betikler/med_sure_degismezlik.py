#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
med_sure_degismezlik.py  (v2)
=============================
SORU:  "Bir ayetin, OKUYUCUDAN BAĞIMSIZ, tutarlı bir SÜRE (med/mora) imzası var mı?"
       Varsa -> yapı metne/tecvîde aittir (sezgi desteklenir).
       Sadece tek karîye özgüyse -> performanstır (o ayet için sezgi düşer).

Katmanlar:
  (A) METİN-ÖNGÖRÜSÜ : ar'dan med olayları -> beklenen mora profili.
        * v2: kuran_veri.json'da 'med_yuku'/'mora_profil' HAZIR varsa onu kullanır
          (zenginleştirilmiş sürüm); yoksa predict_madd ile hesaplar.
  (B) SES-ÖLÇÜMÜ      : her karînin sesinden hece-süre profili (librosa).
        * v2: enerji-TEPESİ yerine DİP'ler-arası SEGMENT süresi -> uzun-düz med
          sesini artık doğru yakalar (eski sürümün zayıf noktası giderildi).
  (C) DENEY           : karîler-arası değişmezlik + metin<->ses uyumu + boş-model.
  (D) KONTROL kancası : aynı ölçütü Kuran-DIŞI makamlı Arapçaya uygula.

ÇALIŞTIRMA:
  pip install librosa soundfile numpy scipy      # + ffmpeg (mp3 için)
  # RECITERS yollarını düzenle; kuran_veri.json'u betiğin yanına koy; sonra:
  python med_sure_degismezlik.py

DÜRÜSTLÜK NOTLARI (değişmedi): med sınıflaması kural-tabanlı yaklaşımdır;
ses tarafı fonem-hizalaması yapmaz ('hangi med' değil 'uzun tutulan yer nerede').
Karar eşikleri ÖNCEDEN sabittir. İki kapı: (1) değişmezlik, (2) kontrol.
"""
import os, json, math, random
import numpy as np

# ========================= 0) AYARLAR =========================
VERI_YOLU = "kuran_veri.json"
RECITERS = {
    "kari1": "audio/1",
    "kari2": "audio/2",
}
TEST_AYETLER = [(50,a) for a in range(1,46)]   # Kaf suresi, iki karide de tam
KONTROL_KLASORU = None
ESIK_CV_DEGISMEZ = 0.15
ESIK_DTW_UYUM    = 0.60
ESIK_METIN_KORR  = 0.40

# ========================= (A) METİN =========================
ALEF={0x627,0x671,0x622,0x625,0x623}; DAGGER=0x670; MAKSURA=0x649
WAW=0x648; YE=0x64A; MADDA=0x653
HAMZA={0x621,0x623,0x624,0x625,0x626}
FATHA=0x64E; DAMMA=0x64F; KASRA=0x650; SUKUN=0x652; SHADDA=0x651
TANWIN={0x64B,0x64C,0x64D}; HARAKAT={FATHA,DAMMA,KASRA,SUKUN,SHADDA}|TANWIN
MARKS=set(range(0x6D6,0x6EE))|{0x640,0xFEFF}
def _is_letter(cp):
    return (0x621<=cp<=0x64A and cp not in HARAKAT) or cp==0x671 or (0x66E<=cp<=0x6D3)
def predict_madd(ar):
    letters=[]; space=False; cur=None
    for ch in ar:
        cp=ord(ch)
        if cp==0x20: space=True; continue
        if cp in MARKS or (0x610<=cp<=0x61A): continue
        if cp in HARAKAT or cp==DAGGER or cp==MADDA:
            if cur is not None: cur[1].append(cp)
            continue
        if _is_letter(cp):
            cur=[cp,[],space]; letters.append(cur); space=False
    prof=[]; types={'tabii':0,'muttasil':0,'munfasil':0,'lazim':0}
    for k,(cp,har,sp) in enumerate(letters):
        nxt=letters[k+1] if k+1<len(letters) else None
        is_med=False
        if DAGGER in har or MADDA in har: is_med=True
        elif cp in ALEF or cp==MAKSURA:
            if KASRA not in har and DAMMA not in har: is_med=True
        elif cp==WAW and har==[] and k>0 and DAMMA in letters[k-1][1]: is_med=True
        elif cp==YE   and har==[] and k>0 and KASRA in letters[k-1][1]: is_med=True
        if is_med:
            mora=2; kind='tabii'
            if nxt:
                ncp,nhar,nsp=nxt
                if ncp in HAMZA: kind='munfasil' if nsp else 'muttasil'; mora=4
                elif SHADDA in nhar or SUKUN in nhar: kind='lazim'; mora=6
            types[kind]+=1; prof.append(mora)
        else: prof.append(1)
    load=sum(w for w in prof if w>1)/max(1,sum(prof))
    return prof, load, types

# ========================= (B) SES (v2) =========================
def measure_profile(path, sr=22050):
    """Enerji zarfında DİP'ler-arası segment süreleri -> göreli hece-süre profili.
       Uzun-düz med sesini doğru yakalar (tempoya karşı normalize)."""
    import librosa
    from scipy.ndimage import uniform_filter1d
    from scipy.signal import find_peaks
    y,sr=librosa.load(path,sr=sr,mono=True)
    if y.size < sr*0.2: return None
    hop=256
    rms=librosa.feature.rms(y=y,frame_length=1024,hop_length=hop)[0]
    t=librosa.frames_to_time(np.arange(len(rms)),sr=sr,hop_length=hop)
    db=20*np.log10(rms+1e-9); db-=db.max()
    sm=uniform_filter1d(db,size=7)
    voiced=sm>-35
    if voiced.sum()<3: return None
    idx=np.where(voiced)[0]
    blocks=np.split(idx,np.where(np.diff(idx)>1)[0]+1)
    segs=[]
    for bl in blocks:
        if len(bl)<2: continue
        seg=sm[bl]
        dips,_=find_peaks(-seg,prominence=4)         # blok içi hece sınırları
        bounds=[0]+list(dips)+[len(bl)-1]
        for a,b in zip(bounds[:-1],bounds[1:]):
            if b>a: segs.append(t[bl[b]]-t[bl[a]])
    segs=np.array([s for s in segs if s>0.02],float)
    if len(segs)<2: return None
    prof=segs/segs.sum()
    long_frac=float(np.sort(prof)[-max(1,len(prof)//4):].sum())
    dur_total=float(t[voiced][-1]-t[voiced][0])
    return dict(nuclei=prof.tolist(), long_frac=long_frac,
                dur_total=dur_total, rate=len(segs)/dur_total if dur_total>0 else 0)

# ========================= yardımcı: DTW =========================
def dtw_corr(a,b):
    a=np.asarray(a,float); b=np.asarray(b,float)
    n,m=len(a),len(b)
    if n<2 or m<2: return float('nan')
    D=np.full((n+1,m+1),np.inf); D[0,0]=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            c=abs(a[i-1]-b[j-1])
            D[i,j]=c+min(D[i-1,j],D[i,j-1],D[i-1,j-1])
    i,j=n,m; pa=[]; pb=[]
    while i>0 and j>0:
        pa.append(a[i-1]); pb.append(b[j-1])
        step=int(np.argmin([D[i-1,j-1],D[i-1,j],D[i,j-1]]))
        if step==0: i,j=i-1,j-1
        elif step==1: i-=1
        else: j-=1
    pa=np.array(pa[::-1]); pb=np.array(pb[::-1])
    if pa.std()<1e-9 or pb.std()<1e-9: return float('nan')
    return float(np.corrcoef(pa,pb)[0,1])

# ========================= (C) DENEY =========================
def fpath(folder,s,a): return os.path.join(folder,f"{s:03d}{a:03d}.mp3")

def get_text_load(ay):
    # kadans dahil (waqf) tercih; yoksa gövde; yoksa hesapla
    if 'med_yuku_waqf' in ay: return float(ay['med_yuku_waqf'])
    if 'med_yuku' in ay: return float(ay['med_yuku'])
    return predict_madd(ay.get('ar',''))[1]
def get_text_profile(ay):
    if ay.get('mora_profil_waqf'): return list(ay['mora_profil_waqf'])
    if ay.get('mora_profil'): return list(ay['mora_profil'])
    return predict_madd(ay.get('ar',''))[0]

def run(veri):
    byno={}
    for su in veri['sureler']:
        for ay in su['ayetler']:
            byno[(su['no'],ay['no'])]=ay
    print("="*64); print("MED-SÜRE DEĞİŞMEZLİK DENEYİ (v2)"); print("="*64)
    per_verse=[]
    for (s,a) in TEST_AYETLER:
        ay=byno.get((s,a))
        if not ay: continue
        tload=get_text_load(ay)
        measured=[]; profs=[]
        for rname,folder in RECITERS.items():
            p=fpath(folder,s,a)
            if not os.path.exists(p): continue
            m=measure_profile(p)
            if m: measured.append(m['long_frac']); profs.append(m['nuclei'])
        if len(measured)<2:
            print(f"  {s}:{a}  yeterli ses yok (n={len(measured)})"); continue
        cv=float(np.std(measured)/(np.mean(measured)+1e-9))
        cs=[dtw_corr(profs[i],profs[j]) for i in range(len(profs)) for j in range(i+1,len(profs))]
        cs=[c for c in cs if not math.isnan(c)]
        mdtw=float(np.mean(cs)) if cs else float('nan')
        # KÖPRÜ: metnin öngördüğü mora profili <-> ölçülen süre profili (ayet-içi şekil)
        tprof=get_text_profile(ay)
        sm=[dtw_corr(tprof,pr) for pr in profs]; sm=[c for c in sm if not math.isnan(c)]
        shape=float(np.mean(sm)) if sm else float('nan')
        # boş-model: metin profilini karıştır
        import random as _r; nn=[]
        for _ in range(30):
            ts=tprof[:]; _r.shuffle(ts)
            cc=[dtw_corr(ts,pr) for pr in profs]; cc=[c for c in cc if not math.isnan(c)]
            if cc: nn.append(np.mean(cc))
        shape_null=float(np.mean(nn)) if nn else float('nan')
        per_verse.append((s,a,tload,float(np.mean(measured)),cv,mdtw,shape,shape_null))
        print(f"  {s}:{a}  metin-yük={tload:.2f}  uzun-pay={np.mean(measured):.2f}"
              f"  CV={cv:.2f}  karî-DTW={mdtw:.2f}  şekil={shape:+.2f}(boş {shape_null:+.2f})  (n={len(measured)})")
    if not per_verse:
        print("\n[!] Ses bulunamadı — RECITERS yolları ve dosya adlarını (001001.mp3) kontrol et."); return
    A=np.array([[x[2],x[3],x[4],x[5],x[6],x[7]] for x in per_verse],float)
    tload,meas,cv,dtw,shape,shnull=A[:,0],A[:,1],A[:,2],A[:,3],A[:,4],A[:,5]
    print("\n"+"-"*64); print("SONUÇ"); print("-"*64)
    print("1) Karîler-arası DEĞİŞMEZLİK")
    print(f"   ort CV(med-yükü) = {np.nanmean(cv):.3f}  (eşik <{ESIK_CV_DEGISMEZ}) -> "
          + ("DEĞİŞMEZ ✓" if np.nanmean(cv)<ESIK_CV_DEGISMEZ else "değişken ✗"))
    print(f"   ort profil-DTW   = {np.nanmean(dtw):.3f}  (eşik >{ESIK_DTW_UYUM})  -> "
          + ("TUTARLI ✓" if np.nanmean(dtw)>ESIK_DTW_UYUM else "tutarsız ✗"))
    # KÖPRÜ (asıl test): ayet-içi şekil eşleşmesi, boş-modele karşı
    sh=shape[~np.isnan(shape)]; sn=shnull[~np.isnan(shnull)]
    print("\n2) METİN profili <-> SES profili (ayet-içi şekil, DTW)")
    if len(sh)>=3:
        d=sh-shnull[~np.isnan(shape)]
        # eşleşmeli izin testi: gerçek şekil, karışık şekilden yüksek mi?
        from numpy import mean as _m
        win=np.mean(sh)-np.mean(sn)
        print(f"   gerçek şekil-uyumu = {np.mean(sh):+.3f}   boş-model = {np.mean(sn):+.3f}   fark = {win:+.3f}")
        print(f"   ayet-başına gerçek>boş oranı: {100*np.mean(d>0):.0f}%   ({np.sum(d>0)}/{len(d)})")
        print("   -> "+("METİN ŞEKLİ SESİ ÖNGÖRÜYOR ✓" if (win>0.05 and np.mean(d>0)>0.6) else "zayıf/boş ✗"))
    else:
        print("   yeterli veri yok")
    # skaler (ikincil, tek-sûrede zayıf olabilir)
    if np.std(tload)>1e-9 and np.std(meas)>1e-9:
        r=float(np.corrcoef(tload,meas)[0,1])
        print(f"\n   (ikincil) skaler med-yükü<->uzun-pay korr r={r:+.3f}  [tek-sûrede düşük varyans, zayıf olabilir]")
    print("\n3) OKUMA — sayılara bak, aşağıdaki iki cümle koşulsuz basılır:")
    print("   Değişmez + şekil öngörüyor => süre-imzası METNE ait.")
    print("   Değişmez ama şekil öngörmüyor => karîler ORTAK bir şey paylaşıyor ama metin öngörümüz değil.")
    print("   KONTROL yine şart (Kuran-dışı makamlı Arapça).")

if __name__=="__main__":
    if not os.path.exists(VERI_YOLU):
        print(f"[!] {VERI_YOLU} bulunamadı — VERI_YOLU'nu düzenle."); raise SystemExit
    run(json.load(open(VERI_YOLU,encoding='utf-8')))
