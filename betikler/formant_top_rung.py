#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
formant_top_rung.py  —  MERDİVENİN EN ÜSTÜ: sesli-kimliği değişmezliği
======================================================================
SORU: Metnin öngördüğü UZUN-SESLİ dizisi (â/û/î), iki karîde de akustik olarak
      geri-üretilebiliyor mu, birbirine ve metne hizalanıyor mu?

Yöntem (hepsi sentetikte doğrulandı):
  - metin-ayağı : med_vowels(ar) -> öngörülen â/û/î dizisi
  - ses-ayağı   : dip-segment -> her uzun çekirdekte (F1, HFR) -> karî-İÇİ k-means(3)
                  -> fizikle etiketle (yüksek F1=â; kalanlar HFR yüksek=î, düşük=û)
  - LPC formant : 11 kHz'e indir, order 14, dar-bantlı en düşük kutup=F1
  - HFR         : >1800 Hz enerji oranı (ön/î parlak, arka/û karanlık)

DÜRÜSTLÜK — asıl kapı azınlıkta:
  â ~ %78 olduğu için "hep â" bile ~%78 tutturur (SIKICI TABAN). Bu yüzden
  gerçek ölçüt: î/û'yu karîler tutarlı ve metinle uyumlu geri-üretiyor mu?
  Betik hem genel hem AZINLIK (î/û) uyumunu ayrı verir; taban ile kıyaslar.

  Ayrıca: değişmezlik geçse bile "Kuran'a özgü" DEĞİL — sesli kimliği Arapça'nın.
  Bu katman KÖPRÜYÜ doğrular ve süre-ölçümüne HİZALAMA verir; ikinci kapı (kontrol)
  yine şarttır.

ÇALIŞTIRMA:
  pip install librosa soundfile scipy numpy scikit-learn      # + ffmpeg
  python formant_top_rung.py
"""
import os, json, math
import numpy as np

VERI_YOLU="kuran_veri.json"
RECITERS={"kari1":"audio/1","kari2":"audio/2"}
SURE=50; AYETLER=range(1,46)          # Kaf

# ---------- metin-ayağı ----------
ALEF={0x627,0x671,0x622,0x625,0x623}; DAGGER=0x670; MAKSURA=0x649; MADDA=0x653
WAW=0x648; YE=0x64A; HAMZA={0x621,0x623,0x624,0x625,0x626}
FATHA=0x64E; DAMMA=0x64F; KASRA=0x650; SUKUN=0x652; SHADDA=0x651
TANWIN={0x64B,0x64C,0x64D}; HARAKAT={FATHA,DAMMA,KASRA,SUKUN,SHADDA}|TANWIN
MARKS=set(range(0x6D6,0x6EE))|{0x640,0xFEFF}
def _isL(cp): return (0x621<=cp<=0x64A and cp not in HARAKAT) or cp==0x671 or (0x66E<=cp<=0x6D3)
def med_vowels(ar):
    L=[]; cur=None; sp=False
    for ch in ar:
        cp=ord(ch)
        if cp==0x20: sp=True; continue
        if cp in MARKS or (0x610<=cp<=0x61A): continue
        if cp in HARAKAT or cp==DAGGER or cp==MADDA:
            if cur is not None: cur[1].append(cp)
            continue
        if _isL(cp): cur=[cp,[],sp]; L.append(cur); sp=False
    out=[]
    for k,(cp,har,sp) in enumerate(L):
        cls=None
        if DAGGER in har or MADDA in har: cls='â'
        elif cp in ALEF or cp==MAKSURA:
            if KASRA not in har and DAMMA not in har: cls='â'
        elif cp==WAW and har==[] and k>0 and DAMMA in L[k-1][1]: cls='û'
        elif cp==YE and har==[] and k>0 and KASRA in L[k-1][1]: cls='î'
        if cls: out.append(cls)
    return out

# ---------- ses-ayağı ----------
def _load(path):
    import librosa
    y,sr=librosa.load(path,sr=22050,mono=True); return y,22050
def segments(y,sr=22050):
    import librosa
    from scipy.ndimage import uniform_filter1d
    from scipy.signal import find_peaks
    hop=256; rms=librosa.feature.rms(y=y,frame_length=1024,hop_length=hop)[0]
    t=librosa.frames_to_time(np.arange(len(rms)),sr=sr,hop_length=hop)
    db=20*np.log10(rms+1e-9); db-=db.max(); sm=uniform_filter1d(db,7); voiced=sm>-35
    idx=np.where(voiced)[0]; out=[]
    for bl in np.split(idx,np.where(np.diff(idx)>1)[0]+1):
        if len(bl)<2: continue
        seg=sm[bl]; dips,_=find_peaks(-seg,prominence=4); bd=[0]+list(dips)+[len(bl)-1]
        for a,b in zip(bd[:-1],bd[1:]):
            dur=t[bl[b]]-t[bl[a]]
            if b>a and dur>0.05: out.append((int(bl[a]*hop),int(bl[b]*hop),dur))
    return out
def feats(y,s,e,sr=22050):
    import librosa
    from scipy.signal import lfilter, resample_poly
    seg=y[s:e]
    if len(seg)<220: return None
    mid=seg[len(seg)//4:3*len(seg)//4] if len(seg)>440 else seg
    ts=11025; z=resample_poly(mid,ts,sr); zp=lfilter([1,-0.97],1,z)*np.hamming(len(z))
    try: a=librosa.lpc(zp.astype(float),order=14)
    except Exception: return None
    r=np.roots(a); r=r[np.imag(r)>=0.01]
    fr=np.angle(r)*ts/(2*np.pi); bw=-0.5*(ts/(2*np.pi))*np.log(np.abs(r)+1e-12)
    cand=sorted([f for f,b in zip(fr,bw) if 150<f<1100 and b<600]); F1=cand[0] if cand else 400.0
    S=np.abs(np.fft.rfft(z*np.hamming(len(z)))); f=np.fft.rfftfreq(len(z),1/ts); S/=S.sum()+1e-12
    hfr=float(S[f>1800].sum())
    return (F1,hfr)

def reciter_sequences(folder, verses_meds):
    """Karînin tüm Kaf med-adaylarını topla, karî-içi kümele, ayet-ayet sesli dizisi döndür."""
    pool=[]; index=[]      # (F1,hfr) ve (ayet, poz)
    per_verse_counts={}
    for (s,a,n_med) in verses_meds:
        p=os.path.join(folder,f"{s:03d}{a:03d}.mp3")
        if not os.path.exists(p): per_verse_counts[a]=None; continue
        y,sr=_load(p); segs=segments(y)
        if not segs: per_verse_counts[a]=[]; continue
        segs_sorted=sorted(segs,key=lambda x:-x[2])[:max(1,n_med)]   # en uzun n_med çekirdek
        segs_time=sorted(segs_sorted,key=lambda x:x[0])              # zaman sırası
        seq_feats=[]
        for (st,en,du) in segs_time:
            fe=feats(y,st,en)
            if fe: seq_feats.append(fe)
        per_verse_counts[a]=len(seq_feats)
        for fe in seq_feats:
            pool.append(fe); index.append(a)
    if len(pool)<6: return None,None
    from sklearn.cluster import KMeans
    X=np.array(pool,float); Xz=(X-X.mean(0))/(X.std(0)+1e-9)
    km=KMeans(n_clusters=3,n_init=10,random_state=0).fit(Xz)
    cen=km.cluster_centers_; order=np.argsort(cen[:,0])
    lab={order[2]:'â'}
    r0,r1=order[0],order[1]
    if cen[r0,1]>cen[r1,1]: lab[r0]='î'; lab[r1]='û'
    else: lab[r1]='î'; lab[r0]='û'
    labels=[lab[c] for c in km.labels_]
    # ayetlere geri dağıt
    seqs={}; i=0
    for (s,a,n_med) in verses_meds:
        c=per_verse_counts.get(a)
        if c is None: seqs[a]=None; continue
        seqs[a]=labels[i:i+c]; i+=c
    return seqs, (X, labels)

# ---------- metrikler ----------
def align_acc(x,y):
    if not x or not y: return None,0
    n=min(len(x),len(y)); 
    if n==0: return None,0
    eq=sum(1 for i in range(n) if x[i]==y[i]); return eq/n, n
def minority_acc(pred,ref):
    # sadece ref'te î/û olan konumlar
    n=min(len(pred),len(ref)); hit=tot=0
    for i in range(n):
        if ref[i] in ('î','û'):
            tot+=1; hit+= (pred[i]==ref[i])
    return (hit/tot if tot else None), tot

def run():
    veri=json.load(open(VERI_YOLU,encoding='utf-8'))
    kaf=next(s for s in veri['sureler'] if s['no']==SURE)
    text={a['no']:med_vowels(a['ar']) for a in kaf['ayetler'] if a['no'] in AYETLER}
    verses_meds=[(SURE,a,len(text[a])) for a in sorted(text)]

    print("="*66); print("MERDİVENİN EN ÜSTÜ — sesli-kimliği değişmezliği (Kaf)"); print("="*66)
    R={}
    for name,folder in RECITERS.items():
        if not os.path.isdir(folder): print(f"[!] klasör yok: {folder}"); continue
        seqs,_=reciter_sequences(folder,verses_meds)
        if seqs is None: print(f"[!] {name}: yeterli ses/çekirdek yok"); continue
        R[name]=seqs
    if len(R)<1: print("[!] Ses bulunamadı — RECITERS yollarını kontrol et."); return

    # metin dağılımı (taban)
    allt=[v for a in text for v in text[a]]
    from collections import Counter
    ct=Counter(allt); tt=sum(ct.values())
    print("\nMETİN uzun-sesli dağılımı:  â %.0f%% · î %.0f%% · û %.0f%%  (n=%d)  [taban: 'hep â' = %.0f%%]"
          %(100*ct['â']/tt,100*ct['î']/tt,100*ct['û']/tt,tt,100*ct['â']/tt))

    # her karî: metinle uyum (genel + azınlık) ve geri-üretilen dağılım
    print("\n1) KARÎ ↔ METİN uyumu")
    for name,seqs in R.items():
        pred=[]; ref=[]
        for a in text:
            if seqs.get(a): 
                n=min(len(seqs[a]),len(text[a])); pred+=seqs[a][:n]; ref+=text[a][:n]
        g,_=align_acc(pred,ref); m,mt=minority_acc(pred,ref)
        cp=Counter(pred); sp=max(1,sum(cp.values()))
        gtxt = f"{100*g:.0f}" if g is not None else "—"
        mtxt = f"{100*m:.0f}" if m is not None else "—"
        da,di,du = 100*cp['â']/sp, 100*cp['î']/sp, 100*cp['û']/sp
        print(f"   {name}: genel={gtxt}%  AZINLIK(î/û)={mtxt}% (n={mt})   "
              f"geri-uretilen: a{da:.0f}/i{di:.0f}/u{du:.0f}")

    # karîler arası değişmezlik
    if len(R)>=2:
        names=list(R.keys()); A,B=R[names[0]],R[names[1]]
        pa=[]; pb=[]
        for a in text:
            if A.get(a) and B.get(a):
                n=min(len(A[a]),len(B[a])); pa+=A[a][:n]; pb+=B[a][:n]
        g,n=align_acc(pa,pb)
        # azınlık: her ikisinin de î/û dediği ya da birinin
        mtot=mhit=0
        for x,ymm in zip(pa,pb):
            if 'î' in (x,ymm) or 'û' in (x,ymm):
                mtot+=1; mhit+=(x==ymm)
        print(f"\n2) KARÎLER-ARASI DEĞİŞMEZLİK ({names[0]} - {names[1]})")
        gtxt = f"{100*g:.0f}" if g is not None else "—"
        mtxt = f"{100*mhit/mtot:.0f}" if mtot>0 else "—"
        print(f"   genel uyum={gtxt}% (n={n})   azinlik-iceren konumlarda uyum={mtxt}% (n={mtot})")
        print("   NOT: genel uyumu 'hep â' tabanıyla kıyasla; asıl sinyal azınlıkta.")

    print("\n3) OKUMA")
    print("   Azınlık(î/û) hem karîler-arası tutarlı hem metinle uyumlu (tabanın belirgin üstünde)")
    print("   => köprü GERÇEK: metin sesli-kimliğini öngörüyor, ses geri-üretiyor, hizalama mümkün.")
    print("   => sonraki: bu hizalamayla SÜRE'yi isimli medlerde ölç; sonra KONTROL (Kuran-dışı).")
    print("   Azınlık tabana yakınsa: ya ölçüm (mp3 HF kaybı HFR'yi bozar) ya hizalama zayıf.")

if __name__=="__main__":
    if not os.path.exists(VERI_YOLU): print("[!] kuran_veri.json yok"); raise SystemExit
    run()
