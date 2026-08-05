#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
imza_nedir.py — "İki karînin paylaştığı imza NEYİN imzası?"
============================================================
Bulgu (önceki test): iki karî aynı ayetin bir yapısını paylaşıyor (değişmez),
ama bu benim med-süre öngörümle açıklanmıyor. Peki paylaşılan şey NE?

Bu betik dört özelliği aynı ayetlerde ölçer ve her biri için sorar:
  "aynı-ayet benzerliği, FARKLI-ayet benzerliğinden (boş-model) belirgin yüksek mi?"
Yüksekse: o özellik ayete-özgü ve karîden bağımsız = imzanın taşıyıcısı.
(Boş-model şart: 'aynı kelimeler zaten benzer' tuzağını eler.)

Özellikler:
  1) enerji konturu    (RMS zarfı — nerede yüksek/alçak)
  2) süre-ritmi        (dip-segment göreli süreleri — tempo/uzatma yapısı)
  3) F0 / EZGİ         (perde konturu — makam/melodi)   [librosa.yin]
  4) tını (spektral merkez)  (parlak/karanlık gidişi)

ÇALIŞTIRMA:  python imza_nedir.py     (pip install librosa scipy numpy + ffmpeg)
"""
import os, math, random
import numpy as np, librosa
from scipy.ndimage import uniform_filter1d
from scipy.signal import find_peaks

RECITERS={"kari1":"audio/1","kari2":"audio/2"}
SURE=50; AYETLER=range(1,46)
SR=22050; HOP=256; NRES=64

def load(p):
    y,_=librosa.load(p,sr=SR,mono=True); return y
def resample_contour(x,n=NRES):
    x=np.asarray(x,float); x=x[np.isfinite(x)]
    if len(x)<2: return None
    return np.interp(np.linspace(0,len(x)-1,n),np.arange(len(x)),x)
def energy_contour(y):
    rms=librosa.feature.rms(y=y,frame_length=1024,hop_length=HOP)[0]
    db=20*np.log10(rms+1e-9); db-=db.max(); return resample_contour(db)
def f0_contour(y):
    f0=librosa.yin(y,fmin=70,fmax=400,sr=SR,frame_length=1024,hop_length=HOP)
    return resample_contour(uniform_filter1d(np.log(np.clip(f0,50,500)),5))
def centroid_contour(y):
    c=librosa.feature.spectral_centroid(y=y,sr=SR,hop_length=HOP)[0]
    return resample_contour(np.log(c+1e-6))
def duration_profile(y):
    rms=librosa.feature.rms(y=y,frame_length=1024,hop_length=HOP)[0]
    t=librosa.frames_to_time(np.arange(len(rms)),sr=SR,hop_length=HOP)
    db=20*np.log10(rms+1e-9); db-=db.max(); sm=uniform_filter1d(db,7); voiced=sm>-35
    idx=np.where(voiced)[0]; segs=[]
    if len(idx)<2: return None
    for bl in np.split(idx,np.where(np.diff(idx)>1)[0]+1):
        if len(bl)<2: continue
        seg=sm[bl]; dips,_=find_peaks(-seg,prominence=4); bd=[0]+list(dips)+[len(bl)-1]
        for a,b in zip(bd[:-1],bd[1:]):
            d=t[bl[b]]-t[bl[a]]
            if b>a and d>0.05: segs.append(d)
    if len(segs)<2: return None
    s=np.array(segs,float); return s/s.sum()
def dtw_corr(a,b):
    if a is None or b is None: return float('nan')
    a=np.asarray(a,float); b=np.asarray(b,float); n,m=len(a),len(b)
    if n<2 or m<2: return float('nan')
    D=np.full((n+1,m+1),np.inf); D[0,0]=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            c=abs(a[i-1]-b[j-1]); D[i,j]=c+min(D[i-1,j],D[i,j-1],D[i-1,j-1])
    i,j=n,m; pa=[]; pb=[]
    while i>0 and j>0:
        pa.append(a[i-1]); pb.append(b[j-1])
        s=int(np.argmin([D[i-1,j-1],D[i-1,j],D[i,j-1]]))
        i,j=(i-1,j-1) if s==0 else ((i-1,j) if s==1 else (i,j-1))
    pa=np.array(pa[::-1]); pb=np.array(pb[::-1])
    if pa.std()<1e-9 or pb.std()<1e-9: return float('nan')
    return float(np.corrcoef(pa,pb)[0,1])

FEATS=[("enerji",energy_contour),("süre-ritmi",duration_profile),
       ("F0/ezgi",f0_contour),("tını",centroid_contour)]

def fpath(folder,a): return os.path.join(folder,f"{SURE:03d}{a:03d}.mp3")

def run():
    names=list(RECITERS)
    if len(names)<2: print("[!] en az 2 karî gerek"); return
    fa,fb=RECITERS[names[0]],RECITERS[names[1]]
    data={}   # ayet -> {feat: (contourA, contourB)}
    print("özellikler çıkarılıyor (F0 biraz yavaş olabilir)...")
    for a in AYETLER:
        pa,pb=fpath(fa,a),fpath(fb,a)
        if not(os.path.exists(pa) and os.path.exists(pb)): continue
        ya,yb=load(pa),load(pb)
        d={}
        for nm,fn in FEATS:
            d[nm]=(fn(ya),fn(yb))
        data[a]=d
    verses=list(data)
    if len(verses)<5: print("[!] yeterli ayet yok:",len(verses)); return
    print(f"{len(verses)} ayet işlendi\n")
    print("=== İMZA ÇÖZÜMLEMESİ: her özellik ayete-özgü mü? ===")
    print("%-12s %8s %8s %8s %10s"%("özellik","aynı","farklı","fark","aynı>farklı"))
    rng=random.Random(0)
    results=[]
    for nm,_ in FEATS:
        same=[]; null=[]
        for a in verses:
            ca,cb=data[a][nm]
            s=dtw_corr(ca,cb)
            if not math.isnan(s): same.append(s)
            # boş-model: aynı karî A'nın a'sı, karî B'nin BAŞKA ayeti
            others=[x for x in verses if x!=a]
            for b in rng.sample(others,min(3,len(others))):
                s2=dtw_corr(ca,data[b][nm][1])
                if not math.isnan(s2): null.append(s2)
        ms=np.mean(same) if same else float('nan')
        mn=np.mean(null) if null else float('nan')
        # ayet-başına aynı>farklı oranı
        wins=[]
        for a in verses:
            ca,cb=data[a][nm]; s=dtw_corr(ca,cb)
            others=[x for x in verses if x!=a]
            ns=[dtw_corr(ca,data[b][nm][1]) for b in others]
            ns=[x for x in ns if not math.isnan(x)]
            if not math.isnan(s) and ns: wins.append(s>np.mean(ns))
        wr=100*np.mean(wins) if wins else float('nan')
        results.append((nm,ms,mn,ms-mn,wr))
        print("%-12s %+8.2f %+8.2f %+8.2f %9.0f%%"%(nm,ms,mn,ms-mn,wr))
    print("\nOKUMA:")
    print("  'fark' (aynı−farklı) en büyük olan özellik = imzanın asıl taşıyıcısı.")
    print("  fark ~0 ise o özellik ayete-özgü değil (ya herkeste benzer ya rastgele).")
    best=max(results,key=lambda r:(r[3] if not math.isnan(r[3]) else -9))
    print(f"  => en ayete-özgü/değişmez: **{best[0]}** (fark {best[3]:+.2f})")
    print("  NOT: yüksek 'aynı' + yüksek 'farklı' (ikisi de) = 'aynı kelimeler' etkisi, imza değil.")

if __name__=="__main__":
    run()
