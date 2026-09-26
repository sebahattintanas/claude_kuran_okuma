# -*- coding: utf-8 -*-
"""Genel kişi merceği. Kullanım: python3 kisi_mercek.py LEM1 LEM2
Ön-kayıt: notlar/ON_KAYIT_dikey_suleyman_davud.md"""
import re, sys, json, collections, math, random, statistics as st
SIL = re.compile('[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u0640]')
ELIF = str.maketrans({'ٱ':'ا','أ':'ا','إ':'ا','آ':'ا'})
rasm = lambda s: SIL.sub('', s).translate(ELIF)
LEMS = sys.argv[1:]
W = collections.OrderedDict()
for l in open('veri/morph.txt', encoding='utf-8'):
    p = l.rstrip('\n').split('\t'); s,a,w,_ = map(int, p[0].split(':'))
    W.setdefault((s,a,w), []).append((p[1], p[3]))
AY = collections.OrderedDict()
for (s,a,w), segs in W.items():
    tags = [t.split('|') for _,t in segs]
    ana = [t for t in tags if 'PN' in t]
    lem = [x[4:] for t in tags for x in t if x.startswith('LEM:')]
    kok = [x[5:] for t in tags for x in t if x.startswith('ROOT:')]
    pnlem = [x[4:] for t in ana for x in t if x.startswith('LEM:')]
    allah = any('ROOT:أله' in t for t in ana)
    AY.setdefault((s,a), []).append(dict(w=w, r=rasm(''.join(x for x,_ in segs)), kok=kok,
        pn=pnlem, allah=allah, inl=segs[0][1].startswith('INL')))
def binom2(k, n, p):
    pk = lambda i: math.comb(n,i)*p**i*(1-p)**(n-i)
    o = pk(k); return min(1.0, sum(pk(i) for i in range(n+1) if pk(i) <= o*(1+1e-9)))
# PN konum tabanı (Allah hariç, etiketle)
taban = [0,0]
for L in AY.values():
    n=len(L)
    if n<2: continue
    for x in L:
        if x['pn'] and not x['allah']:
            taban[1]+=1; taban[0]+= (x['w']-1)/(n-1) <= 1/3
p0 = taban[0]/taban[1]
OUT={'pn_taban':{'ilk_ucte_bir':taban[0],'toplam':taban[1],'oran':round(p0,4)}}
anma={}; pen={}
for L_ in LEMS:
    t=[(k,x['w']) for k,L in AY.items() for x in L if L_ in x['pn']]
    anma[L_]=t
    pen[L_]={(k[0],k[1]+d) for k,_ in t for d in (-1,0,1) if (k[0],k[1]+d) in AY}
    ilk=sum(1 for k,w in t if len(AY[k])>1 and (w-1)/(len(AY[k])-1)<=1/3)
    nn=sum(1 for k,w in t if len(AY[k])>1)
    OUT[L_]={'token':len(t),'ayet':len({k for k,_ in t}),'sure':dict(collections.Counter(k[0] for k,_ in t)),
             'ayetler':sorted({f'{k[0]}:{k[1]}' for k,_ in t}),'pencere':len(pen[L_]),
             'konum':{'ilk_ucte_bir':ilk,'n':nn,'p_binom':round(binom2(ilk,nn,p0),4)}}
A,B=LEMS
birlikte=sorted({k for k,_ in anma[A]}&{k for k,_ in anma[B]})
OUT['birlikte_ayet']=[f'{s}:{a}' for s,a in birlikte]
bolge={'ORTAK':pen[A]&pen[B],'YALNIZ_'+A:pen[A]-pen[B],'YALNIZ_'+B:pen[B]-pen[A]}
kor=collections.Counter(r for L in AY.values() for x in L for r in set(x['kok']))
TOP=sum(len(L) for L in AY.values())
def sahneler(ks):
    ks=sorted(ks); sc=[]
    for k in ks:
        if sc and sc[-1][-1][0]==k[0] and sc[-1][-1][1]+1>=k[1]: sc[-1].append(k)
        else: sc.append([k])
    return sc
for ad,ks in bolge.items():
    sc=sahneler(ks); sid={k:i for i,c in enumerate(sc) for k in c}
    pw=sum(len(AY[k]) for k in ks); gz=collections.Counter(); ss=collections.defaultdict(set)
    for k in ks:
        for x in AY[k]:
            for r in set(x['kok']): gz[r]+=1; ss[r].add(sid[k])
    rows=sorted([(r,o,round(o/(kor[r]*pw/TOP),1),len(ss[r])) for r,o in gz.items()],key=lambda x:-x[2])
    OUT[ad]={'ayet':len(ks),'sahne':[f'{c[0][0]}:{c[0][1]}-{c[-1][1]}' for c in sc],
             'guclu':[x for x in rows if x[2]>=3 and x[3]>=2],'tum_sayim':{r:o for r,o,_,_ in rows}}
# gizli dizi: isim dışında rasm
for L_ in LEMS:
    hed=sorted({x['r'] for k,L in AY.items() for x in L if L_ in x['pn']},key=len)[0]
    hed=re.sub('^[وفلب]+','',hed) if len(hed)>4 else hed
    g1=[(f'{k[0]}:{k[1]}',x['r']) for k,L in AY.items() for x in L if hed in x['r'] and L_ not in x['pn']]
    g2=[]
    for k,L in AY.items():
        dz='';sin=[]
        for x in L:
            if x['inl']: continue
            sin.append((len(dz),len(dz)+len(x['r']),L_ in x['pn'])); dz+=x['r']
        for m in re.finditer('(?=%s)'%hed,dz):
            i,j=m.start(),m.start()+len(hed)
            if any(b[0]<=i and j<=b[1] for b in sin): continue
            if any(b[2] and b[0]<j and i<b[1] for b in sin): continue
            g2.append((f'{k[0]}:{k[1]}',dz[max(0,i-4):j+4]))
    OUT[L_]['gizli']={'dizi':hed,'G1':g1,'G2':g2}
# dosya adı ASCII (Buckwalter rasm): Arapça dosya adı Windows yüklemesinde bozuluyordu
BW = dict(zip(map(chr, range(0x621, 0x64B)), "'|>&<}AbptvjHxd*rzs$SDTZEg______fqklmnhwYy"))
asc = lambda s: ''.join(BW.get(c, '') for c in rasm(s)).replace('_', '')
json.dump(OUT,open('ciktilar/dikey_kisi_%s.json'%'_'.join(asc(x) for x in LEMS),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(json.dumps({k:v for k,v in OUT.items() if not k.startswith(('ORTAK','YALNIZ'))},ensure_ascii=False,indent=1))
for ad in bolge: print(ad,OUT[ad]['ayet'],OUT[ad]['sahne']); print('  güçlü:',OUT[ad]['guclu'])
for ad in bolge: print(ad,{r:OUT[ad]['tum_sayim'].get(r,0) for r in ['نمل','طير','جند','حدد','جبل']})
