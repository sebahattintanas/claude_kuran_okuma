#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tilavet_sentez.py — KÂRÎSİZ TİLÂVET İSKELETİ
=============================================
Metnin buyurduğundan ses üretir. Hiçbir insan kaydından öğrenilmedi.

  SÜRE      ← tecvîd (med 2 / ârız 4 / lâzım 6 hareke) — METNE ait
  SESLİ     ← formant fiziği (â/î/û ağız rezonansları) — METNE ait
  PERDE     ← DÜZ 110 Hz — METİN PERDE BUYURMAZ. Bu sayı KEYFÎ.
              Makam (Bayâtî/Hicaz/Rast...) kārînin tercihidir, metnin değil.

Yani: robotik duyulacak. O robotiklik dürüstlüğün kendisi —
metnin verdiği bu kadar; ezgi insanın katkısı.

ÇIKTI: her ayet için .wav  ·  ÇALIŞTIRMA: python tilavet_sentez.py
"""
import json, os, sys
import numpy as np
from scipy.signal import lfilter
from scipy.io import wavfile

SR=22050
F0=110.0          # KEYFÎ — metin perde buyurmuyor
HAREKE=0.20       # 1 hareke = 200 ms (murattal). Tempo seçimi; oranlar korunur.
UNS=0.070         # ünsüz eklemleme süresi

# ---------- kaynak & süzgeç ----------
def rez(x,f,bw):
    r=np.exp(-np.pi*bw/SR); th=2*np.pi*f/SR
    return lfilter([(1-2*r*np.cos(th)+r*r)],[1,-2*r*np.cos(th),r*r],x)
def glottal(n,f0=F0):
    t=np.arange(n)/SR; ph=(f0*t)%1.0
    y=np.where(ph<0.4,0.5*(1-np.cos(np.pi*ph/0.4)),np.where(ph<0.6,np.cos(np.pi*(ph-0.4)/0.4),0))
    return y-y.mean()
def kaskad(src,F,BW):
    y=src
    for f,bw in zip(F,BW): y=rez(y,f,bw)
    return y
def zarf(y,ar=0.012,de=0.012):
    n=len(y); a=int(ar*SR); d=int(de*SR)
    e=np.ones(n)
    if a>0 and a<n: e[:a]=np.linspace(0,1,a)
    if d>0 and d<n: e[-d:]=np.linspace(1,0,d)
    return y*e

# ---------- sesliler (Arapça, erkek yaklaşık) ----------
SESLI={
 'a':([700,1200,2500],[90,100,140]), 'i':([300,2300,3000],[70,110,150]), 'u':([350,800,2400],[70,100,140]),
 'A':([750,1150,2500],[90,100,140]), 'I':([280,2400,3050],[70,110,150]), 'U':([320,750,2400],[70,100,140]),
}
def sesli(v,sure,emfatik=False):
    F,BW=SESLI[v]; F=list(F)
    if emfatik: F[1]=max(700,F[1]-350); F[0]=F[0]+60      # tefhîm: F2 düşer (gerçek fizik)
    n=max(1,int(sure*SR))
    return zarf(kaskad(glottal(n),F,BW))

# ---------- ünsüzler ----------
def gurultu(n,merkez,bw,kaz=1.0):
    x=np.random.randn(n)
    return zarf(rez(x,merkez,bw)*kaz,0.005,0.005)
def patlama(kapanma,merkez,sesli_mi=False):
    nk=int(kapanma*SR); y=np.zeros(nk)
    if sesli_mi: y+=0.05*kaskad(glottal(nk),[250],[120])   # ötümlü kapanma mırıltısı
    nb=int(0.012*SR); y=np.concatenate([y,gurultu(nb,merkez,900,0.9)])
    return y
def nazal(sure,F2=1700):
    n=int(sure*SR)
    return zarf(kaskad(glottal(n),[250,F2,2600],[80,150,200])*0.6)
def yanal(sure):        # ل
    n=int(sure*SR)
    return zarf(kaskad(glottal(n),[350,1200,2600],[70,110,150])*0.8)
def carpma(sure):       # ر — titrek
    n=int(sure*SR); y=kaskad(glottal(n),[500,1400,2500],[80,120,160])
    t=np.arange(n)/SR; return zarf(y*(0.5+0.5*np.sin(2*np.pi*26*t))*0.85)
def bogaz(sure,otumlu): # ح / ع — farengeal
    n=int(sure*SR)
    if otumlu: return zarf(kaskad(glottal(n),[700,1100,2400],[110,130,180])*0.75)  # ع
    return gurultu(n,1200,700,0.35)                                                 # ح

EMFATIK=set('صضطظ')
UNSUZ={
 'ء':('patlama',(0.035,700,False)), 'ب':('patlama',(0.045,600,True)),  'ت':('patlama',(0.045,3200,False)),
 'ث':('gurultu',(5500,2200,0.22)),  'ج':('patlama',(0.040,2200,True)), 'ح':('bogaz',(False,)),
 'خ':('gurultu',(1600,900,0.30)),   'د':('patlama',(0.040,2600,True)), 'ذ':('gurultu',(4800,2000,0.20)),
 'ر':('carpma',()),                 'ز':('gurultu',(5200,1800,0.28)),  'س':('gurultu',(6200,1800,0.35)),
 'ش':('gurultu',(3300,1400,0.35)),  'ص':('gurultu',(5000,1600,0.35)),  'ض':('patlama',(0.045,1800,True)),
 'ط':('patlama',(0.045,1900,False)),'ظ':('gurultu',(4200,1600,0.22)),  'ع':('bogaz',(True,)),
 'غ':('gurultu',(1400,800,0.26)),   'ف':('gurultu',(7000,2500,0.22)),  'ق':('patlama',(0.050,1100,False)),
 'ك':('patlama',(0.045,2100,False)),'ل':('yanal',()),                  'م':('nazal',(1000,)),
 'ن':('nazal',(1700,)),             'ه':('gurultu',(1000,1600,0.14)),  'و':('kayma',('U',)),
 'ي':('kayma',('I',)),              'ٱ':('yok',()), 'ا':('yok',()),
}
def unsuz_ses(c,emf=False):
    if c not in UNSUZ: return np.zeros(int(UNS*SR))
    tip,p=UNSUZ[c]
    if tip=='patlama': return patlama(p[0],p[1],p[2])
    if tip=='gurultu': return gurultu(int(UNS*SR),p[0],p[1],p[2])
    if tip=='nazal':   return nazal(UNS,p[0])
    if tip=='yanal':   return yanal(UNS)
    if tip=='carpma':  return carpma(UNS)
    if tip=='bogaz':   return bogaz(UNS,p[0])
    if tip=='kayma':   return sesli(p[0],UNS)*0.7
    return np.zeros(int(UNS*SR))

# ---------- metin çözümleme ----------
FATHA,DAMMA,KASRA,SUKUN,SHADDA=0x64E,0x64F,0x650,0x652,0x651
FATHATAN,DAMMATAN,KASRATAN=0x64B,0x64C,0x64D
TANWIN={FATHATAN:'a',DAMMATAN:'u',KASRATAN:'i'}
DAGGER,MADDA,WASLA,MAKSURA=0x670,0x653,0x671,0x649
HRK={FATHA:'a',DAMMA:'u',KASRA:'i'}
SESSIZ_M={0x6DF,0x6E0}; ISARET=set(range(0x6D6,0x6EE))|{0x640,0xFEFF}
HARAKAT={FATHA,DAMMA,KASRA,SUKUN,SHADDA,FATHATAN,DAMMATAN,KASRATAN}
def _isL(cp): return (0x621<=cp<=0x64A and cp not in HARAKAT) or cp==WASLA or (0x66E<=cp<=0x6D3)
def coz(ar):
    L=[];cur=None;sp=False
    for ch in ar:
        cp=ord(ch)
        if cp==0x20: sp=True; continue
        if cp in SESSIZ_M:
            if cur: cur[1].append(cp)
            continue
        if cp in ISARET or (0x610<=cp<=0x61A): continue
        if cp in HARAKAT or cp in (DAGGER,MADDA):
            if cur: cur[1].append(cp)
            continue
        if _isL(cp): cur=[ch,[],sp]; L.append(cur); sp=False
    return [c for c in L if not any(x in SESSIZ_M for x in c[1])]

# mukattaa harf isimleri: (ünsüz, sesli, uzunluk_hareke, kapanış_ünsüzü)
MUK_ISIM={'ا':[('ء','a',1,'ل'),('ي',None,0,None),('ف',None,0,None)],  # elif = e-li-f (medsiz)
 'ل':[('ل','A',6,'م')], 'م':[('م','I',6,'م')], 'ص':[('ص','A',6,'د')], 'ر':[('ر','A',2,None)],
 'ك':[('ك','A',6,'ف')], 'ه':[('ه','A',2,None)], 'ي':[('ي','A',2,None)], 'ع':[('ع','a',6,'ن')],
 'ط':[('ط','A',2,None)], 'س':[('س','I',6,'ن')], 'ح':[('ح','A',2,None)], 'ق':[('ق','A',6,'ف')],
 'ن':[('ن','U',6,'ن')]}

def _uzunluk(L,k,muk):
    """med kaç hareke? sonraki harfe bakılır (muttasıl/munfasıl 4, lâzım 6, yoksa 2)"""
    if k+1<len(L):
        nc,nh=L[k+1][0],L[k+1][1]
        if nc in ('ء','أ','إ','ؤ','ئ'): return 4
        if SHADDA in nh or SUKUN in nh: return 6
    return 2

def _saf_med(L,k):
    """bu harf SADECE önceki sesliyi uzatan bir taşıyıcı mı? ('A'/'I'/'U' ya da None)
       ÖNEMLİ: üst-elif (ٰ) BURAYA girmez — o, ünsüzün ÜSTÜNDE durur, ünsüzü yutmaz."""
    ch,har=L[k][0],L[k][1]
    if ch=='آ': return 'A'
    if ch in ('ا','ى') or ord(ch)==MAKSURA:
        if MADDA in har: return 'A'
        if not any(h in har for h in HRK):
            if k>0 and (FATHA in L[k-1][1] or FATHATAN in L[k-1][1]): return 'A'
        return None
    if ch=='و' and not har and k>0 and DAMMA in L[k-1][1]: return 'U'
    if ch=='ي' and not har and k>0 and KASRA in L[k-1][1]: return 'I'
    return None

def _arid_indeksi(L,muk):
    """vakıfla uzayacak med-i ârız'ın harf indeksi (model kuralının aynısı)"""
    if not L: return None
    last=len(L)-1
    if last<muk: return None
    if FATHATAN in L[last][1]: return None            # ıvaz
    if _saf_med(L,last) or DAGGER in L[last][1]: return None   # açık
    for j in (last-1,last-2):
        if j>=muk and j>=0 and (_saf_med(L,j) or DAGGER in L[j][1]): return j
    return None

def _sentez_govde(ar, muk=0, iz=False):
    L=coz(ar); parca=[]; seg=[]; t=[0.0]; li=[0]
    arid=_arid_indeksi(L,muk)
    def ekle(y,et,tip):
        if y is None or len(y)==0: return
        if iz: seg.append((t[0],t[0]+len(y)/SR,et,tip,li[0]))
        parca.append(y); t[0]+=len(y)/SR
    for k in range(len(L)):
        li[0]=k
        ch,har,_ = L[k][0],L[k][1],L[k][2]
        # ---- mukattaa: harf ADIYLA okunur ----
        if k<muk:
            if ch=='ا':
                for c,v,u in [('ء','a',1),('ل','i',1),('ف',None,0)]:
                    ekle(unsuz_ses(c),c,'unsuz')
                    if v: ekle(sesli(v,u*HAREKE),v,'sesli')
            else:
                ad=MUK_ISIM.get(ch)
                if ad:
                    c,v,u,kap=ad[0]
                    e0=c in EMFATIK
                    ekle(unsuz_ses(c,e0),c,'unsuz')
                    if v: ekle(sesli(v,u*HAREKE,e0),'%s(%d)'%(v,u),'med')
                    if kap: ekle(unsuz_ses(kap),kap,'unsuz')
            ekle(np.zeros(int(0.05*SR)),'','bosluk')
            continue
        emf = ch in EMFATIK or (k>0 and L[k-1][0] in EMFATIK)
        # ---- 1) saf med taşıyıcısı: önceki KISA sesliyi uzatır ----
        sm=_saf_med(L,k)
        if sm:
            u=_uzunluk(L,k,muk)
            if arid==k and u<ARID_MORA: u=ARID_MORA
            if parca:
                parca.pop()
                if iz and seg:
                    son=seg.pop(); t[0]=son[0]
            ekle(sesli(sm,u*HAREKE,emf),'%s(%d)'%(sm,u),'med')
            continue
        # ---- sessiz taşıyıcı (harekesiz elif/vasla) ----
        if ch in ('ا','ٱ','آ') and not har:
            if k==0: ekle(sesli('i',HAREKE),'i','sesli')   # vasla, söz başında
            continue
        # ---- 2) ÜNSÜZ ----
        ekle(unsuz_ses(ch,emf),ch,'unsuz')
        if SHADDA in har: ekle(unsuz_ses(ch,emf),ch,'unsuz')   # ikizlenme
        # ---- 3) ünsüzün seslisi ----
        if DAGGER in har:                    # üst-elif: ünsüz + UZUN â  (ünsüz KORUNUR)
            u=_uzunluk(L,k,muk)
            if arid==k and u<ARID_MORA: u=ARID_MORA
            ekle(sesli('A',u*HAREKE,emf),'A(%d)'%u,'med')
        elif MADDA in har:
            ekle(sesli('A',2*HAREKE,emf),'A(2)','med')
        else:
            v=next((HRK[h] for h in har if h in HRK),None)
            if v: ekle(sesli(v,HAREKE,emf),v,'sesli')
            tw=next((TANWIN[h] for h in har if h in TANWIN),None)
            if tw:
                ekle(sesli(tw,HAREKE,emf),tw,'sesli'); ekle(nazal(UNS),'n','unsuz')
    if not parca: return (np.zeros(100),[]) if iz else np.zeros(100)
    y=np.concatenate(parca); mx=np.max(np.abs(y))
    y = y/mx*0.85 if mx>0 else y
    return (y,seg) if iz else y

ARID_MORA=4
def sentezle(ar, muk=0):     return _sentez_govde(ar,muk,iz=False)
def sentezle_iz(ar, muk=0):  return _sentez_govde(ar,muk,iz=True)

if __name__=='__main__':
    veri=json.load(open('kuran_veri.json',encoding='utf-8'))
    S={s['no']:s for s in veri['sureler']}
    hedef=[(50,1),(50,2),(1,1),(1,2),(108,1),(108,2),(108,3),(2,1),(112,1)]
    os.makedirs('sentez',exist_ok=True)
    print("KÂRÎSİZ TİLÂVET İSKELETİ")
    print("perde: DÜZ %g Hz (KEYFÎ — metin perde buyurmaz)"%F0)
    print("süre: tecvîd · sesli: formant fiziği\n")
    for sn,an in hedef:
        a=next(x for x in S[sn]['ayetler'] if x['no']==an)
        y=sentezle(a['ar_saf'], a.get('mukattaa',0))
        fn='sentez/%03d%03d.wav'%(sn,an)
        wavfile.write(fn,SR,(y*32767).astype(np.int16))
        print("  %d:%-3d %-42s %5.2f sn  →  %s"%(sn,an,a['ar_saf'][:42],len(y)/SR,fn))
    print("\nDinle. Yanlış geliyorsa MODEL yanlıştır — söyle, düzeltiriz.")
