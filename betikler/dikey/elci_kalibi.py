# -*- coding: utf-8 -*-
"""Elçi kıssası kalıbı. Ön-kayıt: notlar/ON_KAYIT_elci_kaliibi.md"""
import sys, math, json, itertools, collections
src=open('betikler/dikey/peygamber_ozgul.py',encoding='utf-8').read().split('anma={n:')[0]
sys.argv=['x','--isim-haric']; ns={}; exec(src,ns)
AY,AD=ns['AY'],ns['AD']
# veri düzeltmesi: 2:111, 2:135, 2:140 هُودًا = Yahudi
HUD=[l for l in AD['Hûd']][0]; duz=0
for k in [(2,111),(2,135),(2,140)]:
    for d in AY[k].values():
        if HUD in d['pn']: d['pn'].discard(HUD); duz+=1
assert duz==3, duz
anma={n:sorted({k for k,W in AY.items() for d in W.values() if d['pn']&set(L)}) for n,L in AD.items()}
pen={n:{(s,a+dd) for s,a in v for dd in (-1,0,1) if (s,a+dd) in AY} for n,v in anma.items()}
ozel={n:pen[n]-set().union(*[pen[m] for m in pen if m!=n]) for n in pen}
TUM=set(l for v in AD.values() for l in v)
def sayim(ks):
    c=collections.Counter()
    for k in ks:
        for d in AY[k].values():
            if d['pn']&TUM: continue
            for r in d['kok']: c[r]+=1
    return c
EVREN=[n for n in AD if len(ozel[n])>=10]
E=['Nûh','Hûd','Sâlih','Şuayb','Lût']
V={n:sayim(ozel[n]) for n in EVREN}
df=collections.Counter(r for n in EVREN for r in V[n])
idf={r:math.log(len(EVREN)/df[r]) for r in df}
def vek(c): return {r:v*idf.get(r,0) for r,v in c.items() if idf.get(r,0)>0}
def cos(a,b):
    ort=set(a)&set(b); s=sum(a[r]*b[r] for r in ort)
    na=math.sqrt(sum(x*x for x in a.values())); nb=math.sqrt(sum(x*x for x in b.values()))
    return s/(na*nb) if na and nb else None
VW={n:vek(V[n]) for n in EVREN}
S1={}
for a,b in itertools.combinations(EVREN,2): S1[frozenset((a,b))]=cos(VW[a],VW[b])
# M2
sureler={n:{s for s,_ in ozel[n]} for n in EVREN}
S2={}
for a,b in itertools.combinations(EVREN,2):
    ka={k for k in ozel[a] if k[0] not in sureler[b]}; kb={k for k in ozel[b] if k[0] not in sureler[a]}
    ca,cb=sayim(ka),sayim(kb)
    if sum(ca.values())<30 or sum(cb.values())<30: S2[frozenset((a,b))]=None; continue
    S2[frozenset((a,b))]=cos(vek(ca),vek(cb))
def ort(S,g):
    v=[S[frozenset(p)] for p in itertools.combinations(g,2) if S[frozenset(p)] is not None]
    return (sum(v)/len(v), len(v)) if v else (None,0)
def test(S):
    g0,nc=ort(S,E); dag=[]
    for g in itertools.combinations(EVREN,5):
        m,_=ort(S,g)
        if m is not None: dag.append(m)
    p=sum(x>=g0-1e-12 for x in dag)/len(dag)
    sira=sorted(dag,reverse=True).index(min(dag,key=lambda x:abs(x-g0)))+1
    return dict(E_ort=round(g0,4),cift=nc,kume_sayisi=len(dag),p=round(p,4),sira=sira,
                dag_medyan=round(sorted(dag)[len(dag)//2],4),dag_max=round(max(dag),4))
OUT={'hud_duzeltme':duz,'evren':EVREN,'ozel_ayet':{n:len(ozel[n]) for n in EVREN},
     'M1':test(S1),'M2':test(S2),
     'M2_dusen_ciftler':[sorted(p) for p,v in S2.items() if v is None and set(p)<=set(E)],
     'E_ic_M1':{n:round(sum(S1[frozenset((n,m))] for m in E if m!=n)/4,4) for n in E},
     'E_ciftler_M1':{'-'.join(sorted(p)):round(S1[frozenset(p)],3) for p in itertools.combinations(E,2)},
     'E_ciftler_M2':{'-'.join(sorted(p)):(round(S2[frozenset(p)],3) if S2[frozenset(p)] is not None else None) for p in itertools.combinations(E,2)}}
# M3
Eb=collections.Counter(); kac=collections.Counter()
for n in E:
    for r in V[n]: kac[r]+=1
    Eb.update(V[n])
Rest=collections.Counter()
for n in EVREN:
    if n not in E: Rest.update(V[n])
tE=sum(Eb.values()); tR=sum(Rest.values())
m3=[(r,Eb[r],kac[r],round((Eb[r]/tE)/(Rest[r]/tR),1) if Rest[r] else 'inf') for r in Eb if kac[r]>=4]
m3.sort(key=lambda x:-(x[3] if x[3]!='inf' else 1e9))
OUT['M3']=m3
# en yakın komşu: her E üyesi için M1'de en benzer 3 ad
OUT['komsu_M1']={n:sorted([(m,round(S1[frozenset((n,m))],3)) for m in EVREN if m!=n],key=lambda x:-x[1])[:3] for n in E}
json.dump(OUT,open('ciktilar/elci_kalibi.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(json.dumps({k:v for k,v in OUT.items() if k!='M3'},ensure_ascii=False,indent=1))
KT=json.load(open('tablolar/kok_turkce.json'))
print('M3:'); [print(' ',r,KT.get(r,'?')[:30],'n=',c,'ad=',k,'×',x) for r,c,k,x in m3]
