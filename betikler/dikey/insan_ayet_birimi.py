# -*- coding: utf-8 -*-
"""(1) ayet birimli ayırt eden kökler. Ön-kayıt: notlar/ON_KAYIT_insan_ayet_birimi.md"""
import collections, json
from scipy.stats import hypergeom
exec(open('betikler/dikey/insan_uclu.py',encoding='utf-8').read().split('# ---- A')[0])
def ayet_kok(k):  # kavram kelimeleri hariç, ayet başına küme
    return {r for d in AY[k] if not d['h'] for r in d['kok']}
AK={k:ayet_kok(k) for k in AY}
def kosu(evren, bolgeler, etiket):
    E=list(evren); M=len(E); UK=collections.Counter(r for k in E for r in AK[k]); tl=[]
    for ad,bol in bolgeler.items():
        n=len(bol); c=collections.Counter(r for k in bol for r in AK[k])
        srs=collections.defaultdict(set)
        for k in bol:
            for r in AK[k]: srs[r].add(k[0])
        for r,x in c.items():
            if x<3: continue
            K=UK[r]; p=hypergeom.sf(x-1,M,K,n); kat=(x/n)/((K-x)/(M-n)) if K>x else float('inf')
            tl.append((ad,r,x,K,kat,p,len(srs[r])))
    m=len(tl); es=0.05/m; out={'m':m,'esik':es}
    for ad in bolgeler:
        out[ad]=[(r,x,K,round(kat,1) if kat!=float('inf') else 'inf','%.1e'%p,s) for a,r,x,K,kat,p,s in sorted(tl,key=lambda z:z[5]) if a==ad and p<es and kat>=2 and s>=3]
    return out
anma={k:{a for a,L_ in AY.items() if any(d['h']==k for d in L_)} for k in HED}
pen={k:{(s,a+dd) for s,a in v for dd in (-1,0,1) if (s,a+dd) in AY} for k,v in anma.items()}
U=set().union(*pen.values())
ozel={k:pen[k]-set().union(*[pen[j] for j in pen if j!=k]) for k in pen}
R1a=kosu(U,ozel,'1a')
R1b=kosu(set(AY),{'INS':pen['INS']},'1b')
OUT={'1a':R1a,'1b':R1b}
json.dump(OUT,open('ciktilar/insan_ayet_birimi.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
KT=json.load(open('tablolar/kok_turkce.json'))
for kk,R in OUT.items():
    print(f'== {kk}  m={R["m"]} eşik={R["esik"]:.1e}')
    for ad in [a for a in R if a not in ('m','esik')]:
        print(' ',ad,len(R[ad]))
        for r,x,K,kat,p,s in R[ad]: print(f'     {r} ({KT.get(r,"?")[:26]}) ayet={x}/K={K} ×{kat} p={p} sûre={s}')
