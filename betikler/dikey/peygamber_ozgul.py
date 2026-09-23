# -*- coding: utf-8 -*-
"""Her peygamber adının kendine ait kökleri. Ön-kayıt: notlar/ON_KAYIT_dikey_peygamber_ozgul.md"""
import re, json, collections
from scipy.stats import hypergeom
AD = {'Âdem':['آدَم'],'İdrîs':['إِدْرِيس'],'Nûh':['نُوح'],'Hûd':['هُود'],'Sâlih':['صالِح'],'İbrâhim':['إِبْراهِيم'],
 'Lût':['لُوط'],'İsmâil':['إِسْماعِيل'],'İshak':['إِسْحاق'],'Yakub':['يَعْقُوب'],'Yûsuf':['يُوسُف'],'Eyyûb':['أَيُّوب'],
 'Şuayb':['شُعَيْب'],'Mûsâ':['مُوسَى'],'Hârûn':['هارُون'],'Dâvûd':['داوُد'],'Süleyman':['سُلَيْمان'],'İlyâs':['إِلْياس'],
 'Elyesa':['الْيَسَع'],'Yûnus':['يُونُس'],'Zekeriyyâ':['زَكَرِيّا'],'Yahyâ':['يَحْيَى'],'Îsâ':['عِيسَى','مَسِيح'],'Muhammed':['مُحَمَّد']}
# dizgeleri korpustan doğrula (elle yazılan kaçmasın)
KORPUS_PN=collections.Counter()
AY=collections.OrderedDict()
for l in open('veri/morph.txt',encoding='utf-8'):
    p=l.rstrip('\n').split('\t'); s,a,w,_=map(int,p[0].split(':')); t=p[3].split('|')
    d=AY.setdefault((s,a),collections.OrderedDict()).setdefault(w,{'kok':set(),'pn':set()})
    for x in t:
        if x.startswith('ROOT:'): d['kok'].add(x[5:])
        if x.startswith('LEM:') and 'PN' in t: d['pn'].add(x[4:]); KORPUS_PN[x[4:]]+=1
import unicodedata
NF=lambda x: unicodedata.normalize('NFC',x)
cozum={NF(k):k for k in KORPUS_PN}
duzeltilen=[l for v in AD.values() for l in v if l not in KORPUS_PN and NF(l) in cozum]
AD={n:[l if l in KORPUS_PN else cozum.get(NF(l),l) for l in v] for n,v in AD.items()}
print('korpustan çözülen (elle yazım farklıydı):',duzeltilen)
eksik=[l for v in AD.values() for l in v if l not in KORPUS_PN]
assert not eksik, ('KORPUSTA YOK', eksik)
anma={n:sorted({k for k,W in AY.items() for d in W.values() if d['pn']&set(L)}) for n,L in AD.items()}
pen={n:{(s,a+dd) for s,a in v for dd in (-1,0,1) if (s,a+dd) in AY} for n,v in anma.items()}
U=set().union(*pen.values())
ozel={n:pen[n]-set().union(*[pen[m] for m in pen if m!=n]) for n in pen}
import sys
SAPMA='--isim-haric' in sys.argv
TUM=set(l for v in AD.values() for l in v)
temiz=lambda d: not (SAPMA and d['pn']&TUM)
kel=lambda ks:[d for k in sorted(ks) for d in AY[k].values() if temiz(d)]
UW=kel(U); M=len(UW); UK=collections.Counter(r for d in UW for r in d['kok'])
testler=[]
for n in AD:
    ks=sorted(ozel[n]); W_=[(k,d) for k in ks for d in AY[k].values() if temiz(d)]; nn=len(W_)
    kc=collections.Counter(r for _,d in W_ for r in d['kok'])
    sure=collections.defaultdict(set)
    for k,d in W_:
        for r in d['kok']: sure[r].add(k[0])
    for r,k in kc.items():
        if k<3: continue
        K=UK[r]; p=hypergeom.sf(k-1,M,K,nn)
        dis=(K-k)/(M-nn) if M>nn else 0
        x=(k/nn)/dis if dis>0 else float('inf')
        testler.append(dict(ad=n,kok=r,k=k,K=K,n=nn,p=p,kat=round(x,1) if x!=float('inf') else 'inf',sure=sorted(sure[r])))
m=len(testler); esik=0.05/m
ait=collections.defaultdict(list); tek=collections.defaultdict(list)
for t in testler:
    buyuk= t['kat']=='inf' or t['kat']>=3
    if t['p']<esik and buyuk:
        (ait if len(t['sure'])>=2 else tek)[t['ad']].append(t)
OUT={'m_test':m,'esik':esik,'M_havuz_kelime':M,'havuz_ayet':len(U),
 'ad':{n:{'anma_ayet':len(anma[n]),'pencere':len(pen[n]),'ozel_ayet':len(ozel[n]),'ozel_kelime':sum(len(AY[k]) for k in ozel[n]),
         'ait':[(t['kok'],t['k'],t['K'],t['kat'],'%.1e'%t['p'],t['sure']) for t in sorted(ait[n],key=lambda t:t['p'])],
         'tek_sure':[(t['kok'],t['k'],t['K'],t['kat'],'%.1e'%t['p'],t['sure']) for t in sorted(tek[n],key=lambda t:t['p'])]} for n in AD}}
json.dump(OUT,open('ciktilar/dikey_peygamber_ozgul%s.json'%('_isimharic' if SAPMA else ''),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('m =',m,' eşik =%.2e'%esik,' havuz',len(U),'ayet',M,'kelime')
print(f"{'ad':10s} anma pen özel | ait | tek")
for n,v in OUT['ad'].items(): print(f"{n:10s} {v['anma_ayet']:4d} {v['pencere']:4d} {v['ozel_ayet']:4d} | {len(v['ait']):3d} | {len(v['tek_sure']):3d}")
print('toplam ait',sum(len(v) for v in ait.values()),'toplam tek-sûre',sum(len(v) for v in tek.values()))
