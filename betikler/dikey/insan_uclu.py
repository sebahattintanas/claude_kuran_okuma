# -*- coding: utf-8 -*-
"""İnsanın üç adı. Ön-kayıt: notlar/ON_KAYIT_insan_uclu.md"""
import collections, json, unicodedata, numpy as np
from scipy.stats import hypergeom, chi2_contingency
NF=lambda x: unicodedata.normalize('NFC',x)
KEL=collections.OrderedDict()
for l in open('veri/morph.txt',encoding='utf-8'):
    p=l.rstrip('\n').split('\t'); s,a,w,_=map(int,p[0].split(':')); t=p[3].split('|')
    d=KEL.setdefault((s,a,w),{'segs':[],'kok':set()})
    d['segs'].append(t); d['kok'].update(x[5:] for x in t if x.startswith('ROOT:'))
LEMS={x[4:] for d in KEL.values() for t in d['segs'] for x in t if x.startswith('LEM:')}
cz={NF(x):x for x in LEMS}
def L(x): assert NF(x) in cz,x; return cz[NF(x)]
HED={'INS':L('إِنسان'),'NAS':L('ناس'),'BES':L('بَشَر')}
def hedef(d):
    for t in d['segs']:
        lm=[x[4:] for x in t if x.startswith('LEM:')]
        for k,v in HED.items():
            if v in lm: return k,t
    return None,None
AY=collections.OrderedDict()
for (s,a,w),d in KEL.items():
    d['h'],d['ht']=hedef(d); AY.setdefault((s,a),[]).append(d)
TIP={tuple(x['k']):x['tip'] for x in json.load(open('ciktilar/defter.json'))}
OUT={'sayim':{k:sum(1 for d in KEL.values() if d['h']==k) for k in HED}}
# ---- A
anma={k:{a for a,L_ in AY.items() if any(d['h']==k for d in L_)} for k in HED}
pen={k:{(s,a+dd) for s,a in v for dd in (-1,0,1) if (s,a+dd) in AY} for k,v in anma.items()}
U=set().union(*pen.values())
ozel={k:pen[k]-set().union(*[pen[j] for j in pen if j!=k]) for k in pen}
def sayim(ks):
    c=collections.Counter(); srs=collections.defaultdict(set); n=0
    for k in ks:
        for d in AY[k]:
            if d['h']: continue
            n+=1
            for r in d['kok']: c[r]+=1; srs[r].add(k[0])
    return c,srs,n
UC,_,M=sayim(U); testler=[]
for k in HED:
    c,srs,n=sayim(ozel[k])
    for r,x in c.items():
        if x<3: continue
        K=UC[r]; p=hypergeom.sf(x-1,M,K,n); kat=(x/n)/((K-x)/(M-n)) if K>x else float('inf')
        testler.append((k,r,x,K,kat,p,len(srs[r])))
m=len(testler); es=0.05/m
OUT['A']={'m':m,'esik':es,'bolge':{k:{'anma_ayet':len(anma[k]),'pencere':len(pen[k]),'ozel':len(ozel[k])} for k in HED}}
for k in HED:
    OUT['A'][k]=[(r,x,K,round(kat,1) if kat!=float('inf') else 'inf','%.1e'%p,s) for kk,r,x,K,kat,p,s in sorted(testler,key=lambda z:z[5]) if kk==k and p<es and kat>=2 and s>=3]
# ---- B
rng=np.random.default_rng(0)
def test(tab):
    tab=np.array(tab)
    tab=tab[:,tab.sum(0)>0]
    chi,p,dof,exp=chi2_contingency(tab,correction=False)
    if (exp<5).any():
        # Monte Carlo: satır toplamları sabit, etiketleri karıştır
        rows=np.repeat(np.arange(tab.shape[0]),tab.sum(1)); cols=np.concatenate([np.repeat(np.arange(tab.shape[1]),tab[i]) for i in range(tab.shape[0])])
        # doğru eşleme için hücre bazlı liste
        lab=[];cat=[]
        for i in range(tab.shape[0]):
            for j in range(tab.shape[1]): lab+= [i]*tab[i,j]; cat+=[j]*tab[i,j]
        lab=np.array(lab);cat=np.array(cat); ge=0
        for _ in range(20000):
            pc=rng.permutation(cat); t2=np.zeros_like(tab)
            np.add.at(t2,(lab,pc),1)
            c2=chi2_contingency(t2,correction=False)[0] if (t2.sum(0)>0).all() else 0
            ge+= c2>=chi-1e-9
        return round(chi,2),(ge+1)/20001,'MC'
    return round(chi,2),p,'asimptotik'
prof={k:collections.Counter() for k in HED}
for (s,a),L_ in AY.items():
    for i,d in enumerate(L_):
        if not d['h']: continue
        k=d['h']; t=d['ht']; allseg=[x for tt in d['segs'] for x in tt]
        voc='VOC' in allseg or (i>0 and any('VOC' in tt for tt in L_[i-1]['segs']))
        prof[k]['hitap' if voc else 'hitap_yok']+=1
        prof[k]['DET' if 'DET' in allseg else 'DET_yok']+=1
        prof[k][next((c for c in ('NOM','ACC','GEN') if c in t),'hal?')]+=1
        prof[k]['tip_'+TIP[(s,a)]]+=1
        prof[k]['son' if i==len(L_)-1 else 'son_degil']+=1
OUT['profil']={k:dict(v) for k,v in prof.items()}
olc={'B1_hitap':['hitap','hitap_yok'],'B2_DET':['DET','DET_yok'],'B3_hal':['NOM','ACC','GEN'],'B4_nuzul':['tip_M','tip_D'],'B5_son':['son','son_degil']}
OUT['B']={}
for ad,cs in olc.items():
    tab=[[prof[k][c] for c in cs] for k in HED]
    chi,p,yon=test(tab)
    OUT['B'][ad]={'tablo':{k:dict(zip(cs,r)) for k,r in zip(HED,tab)},'oran':{k:round(r[0]/sum(r),3) for k,r in zip(HED,tab)},'chi2':chi,'p':'%.2e'%p,'yontem':yon}
json.dump(OUT,open('ciktilar/insan_uclu.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
KT=json.load(open('tablolar/kok_turkce.json'))
print('sayım',OUT['sayim']); print('A',OUT['A']['m'],'%.1e'%es,OUT['A']['bolge'])
for k in HED:
    print(k,len(OUT['A'][k]))
    for r,x,K,kat,p,s in OUT['A'][k]: print(f'   {r} ({KT.get(r,"?")[:28]}) k={x}/K={K} ×{kat} p={p} sûre={s}')
for ad,v in OUT['B'].items(): print(ad,v['tablo'],'oran(ilk sütun)',v['oran'],'χ²',v['chi2'],'p',v['p'],v['yontem'])
