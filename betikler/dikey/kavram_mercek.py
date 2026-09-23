# -*- coding: utf-8 -*-
"""Kavram merceği. Ön-kayıt: notlar/ON_KAYIT_kavram_mercek.md"""
import collections, json, unicodedata, itertools, math
from scipy.stats import hypergeom, binomtest
NF=lambda x: unicodedata.normalize('NFC',x)
SEG=[]  # (s,a,w,pos,tags)
for l in open('veri/morph.txt',encoding='utf-8'):
    p=l.rstrip('\n').split('\t'); s,a,w,_=map(int,p[0].split(':'))
    SEG.append((s,a,w,p[2],p[3].split('|')))
LEMS={x[4:] for *_,t in SEG for x in t if x.startswith('LEM:')}
coz={NF(x):x for x in LEMS}
def L(x):
    assert NF(x) in coz, ('KORPUSTA YOK',x); return coz[NF(x)]
lem=lambda t:[x[4:] for x in t if x.startswith('LEM:')]
KAV={
 'C_dar':  lambda pos,t: L('جَنَّة') in lem(t) and 'PN' in t,
 'C_genis':lambda pos,t: L('جَنَّة') in lem(t),
 'S_kul':  lambda pos,t: L('صالِح') in lem(t) and 'PN' not in t and ('MP' in t or 'MD' in t),
 'S_amel': lambda pos,t: L('صالِحَة') in lem(t) and 'FP' in t,
 'I':      lambda pos,t: L('إِنسان') in lem(t)}
KEL=collections.OrderedDict()   # (s,a,w) -> dict
for s,a,w,pos,t in SEG:
    d=KEL.setdefault((s,a,w),{'kok':set(),'kav':set(),'N':False})
    d['kok'].update(x[5:] for x in t if x.startswith('ROOT:'))
    if pos=='N': d['N']=True
    for k,f in KAV.items():
        if f(pos,t): d['kav'].add(k)
AY=collections.OrderedDict()
for (s,a,w),d in KEL.items(): AY.setdefault((s,a),[]).append(d)
son={id(L_[-1]) for L_ in AY.values()}
OUT={'tanim_sayim':{k:sum(1 for d in KEL.values() if k in d['kav']) for k in KAV}}
# Ölçüm 1
def sayim(ks,kav):
    c=collections.Counter(); srs=collections.defaultdict(set); n=0
    for k in ks:
        for d in AY[k]:
            if kav in d['kav']: continue
            n+=1
            for r in d['kok']: c[r]+=1; srs[r].add(k[0])
    return c,srs,n
TOPK=collections.Counter(r for d in KEL.values() for r in d['kok']); TOPN=len(KEL)
ham={}
for kav in KAV:
    ayt={k for k,L_ in AY.items() if any(kav in d['kav'] for d in L_)}
    pen={(s,a+dd) for s,a in ayt for dd in (-1,0,1) if (s,a+dd) in AY}
    c,srs,n=sayim(pen,kav)
    # evren: kavram kelimeleri hariç korpus
    kavN=sum(1 for d in KEL.values() if kav in d['kav'])
    for r,k in c.items():
        if k<3: continue
        K=TOPK[r]; p=hypergeom.sf(k-1,TOPN-kavN,K,n)
        x=(k/n)/((K-k)/(TOPN-kavN-n)) if K>k else float('inf')
        ham.setdefault(kav,[]).append((r,k,K,x,p,len(srs[r])))
    OUT.setdefault('pencere',{})[kav]={'ayet':len(ayt),'pencere':len(pen),'kelime':n}
m=sum(len(v) for v in ham.values()); esik=0.05/m
OUT['m']=m; OUT['esik']=esik
for kav,v in ham.items():
    ait=[(r,k,K,round(x,1) if x!=float('inf') else 'inf','%.1e'%p,s) for r,k,K,x,p,s in sorted(v,key=lambda z:z[4]) if p<esik and x>=2 and s>=3]
    OUT.setdefault('ait',{})[kav]=ait
sag=[r for r,*_ in OUT['ait']['C_dar'] if r in {x[0] for x in OUT['ait']['C_genis']}]
OUT['cennet_saglam']=sag
# Ölçüm 2
tabN=[0,0]
for L_ in AY.values():
    for i,d in enumerate(L_):
        if d['N'] and not d['kav']: tabN[1]+=1; tabN[0]+= i==len(L_)-1
p0=tabN[0]/tabN[1]; OUT['taban_son']=round(p0,4)
for kav in ['C_genis','S_kul','S_amel','I']:
    t=[i==len(L_)-1 for L_ in AY.values() for i,d in enumerate(L_) if kav in d['kav']]
    b=binomtest(sum(t),len(t),p0)
    OUT.setdefault('son_konum',{})[kav]={'son':sum(t),'n':len(t),'oran':round(sum(t)/len(t),3),'p':round(b.pvalue,5)}
# Ölçüm 3
AK={kav:{k for k,L_ in AY.items() if any(kav in d['kav'] for d in L_)} for kav in KAV}
N=len(AY)
for a,b in itertools.combinations(['C_genis','S_kul','S_amel','I'],2):
    na,nb=len(AK[a]),len(AK[b]); o=len(AK[a]&AK[b]); e=na*nb/N
    hg=hypergeom(N,na,nb)
    p=min(1.0,2*min(hg.sf(o-1),hg.cdf(o)))
    OUT.setdefault('birlikte',{})[f'{a}–{b}']={'gozlenen':o,'beklenen':round(e,2),'yon':'üst' if o>e else 'alt','p':'%.2e'%p,
        'ayetler':[f'{s}:{x}' for s,x in sorted(AK[a]&AK[b])][:12]}
json.dump(OUT,open('ciktilar/kavram_mercek.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
KT=json.load(open('tablolar/kok_turkce.json'))
print('tanım:',OUT['tanim_sayim'],'\npencere:',OUT['pencere'],'\nm=',m,'eşik=%.2e'%esik)
for kav,v in OUT['ait'].items():
    print(f'\n{kav}: {len(v)} kök')
    for r,k,K,x,p,s in v: print(f'   {r} ({KT.get(r,"?")[:28]}) k={k}/K={K} ×{x} p={p} sûre={s}')
print('\ncennet sağlam:',sag)
print('\nson konum taban',OUT['taban_son'],OUT['son_konum'])
print('\nbirlikte:'); [print(' ',k,v) for k,v in OUT['birlikte'].items()]
