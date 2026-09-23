# -*- coding: utf-8 -*-
"""(B) Yaratılışta sıra grafiği. Ön-kayıt: notlar/ON_KAYIT_insan_sifat_ve_sira.md"""
import collections, json, unicodedata, itertools
NF=lambda x: unicodedata.normalize('NFC',x)
SEG=[]
for l in open('veri/morph.txt',encoding='utf-8'):
    p=l.rstrip('\n').split('\t'); s,a,w,g=map(int,p[0].split(':')); SEG.append(((s,a),w,p[1],p[2],p[3].split('|')))
LEMS={x[4:] for *_,t in SEG for x in t if x.startswith('LEM:')}
cz={NF(x):x for x in LEMS}
def R(x):
    assert NF(x) in cz,('YOK',x); return cz[NF(x)]
INSAN={R(x):x for x in ['تُراب','طِين','صَلْصال','حَمَإ','سُلالَة','نُطْفَة','عَلَقَة','مُضْغَة','عِظام','لَحْم','سَوَّى','نَفَخَ']}
KOZ={R(x):x for x in ['سَماء','أَرْض','دُخان','رَواسِي','جَبَل','اسْتَوَى','دَحَى']}
BAG={'خلق','جعل','سوي','فطر','نشأ','بدأ','دحو','نفخ','بني','سمك'}
AY=collections.OrderedDict()
for k,w,f,pos,t in SEG: AY.setdefault(k,[]).append((w,f,pos,t))
lem=lambda t:next((x[4:] for x in t if x.startswith('LEM:')),None)
def dizi(k):
    out=[]; seen_ba=False
    segs=AY[k]
    for idx,(w,f,pos,t) in enumerate(segs):
        l=lem(t)
        if l==R('ثُمّ') or (l=='ف' and ('REM' in t or 'CONJ' in t)): out.append(('|',k,w)); continue
        if l==R('بَعْد') and idx+1<len(segs) and lem(segs[idx+1][3])==R('ذا'): out.append(('|',k,w)); continue
        if l in INSAN: out.append((('İ',INSAN[l]),k,w))
        elif l in KOZ: out.append((('K',KOZ[l]),k,w))
    return out
def bag(k): return any(x[5:] in BAG for *_,t in AY[k] for x in t if x.startswith('ROOT:'))
kenar=collections.defaultdict(list); keys=list(AY)
for i,k in enumerate(keys):
    if not bag(k): continue
    d=dizi(k)
    # sonraki ayet sıra işaretiyle başlıyorsa devam
    if i+1<len(keys) and keys[i+1][0]==k[0]:
        d2=dizi(keys[i+1])
        if d2 and d2[0][0]=='|' and d2[0][2]==1: d=d+d2
    bol=[[]]
    for x in d:
        if x[0]=='|': bol.append([])
        else: bol[-1].append(x)
    bol=[b for b in bol if b]  # boş bölütler birleşir
    for b1,b2 in zip(bol,bol[1:]):
        for (A,ka,_),(B,kb,_) in itertools.product(b1,b2):
            if A[0]==B[0] and A[1]!=B[1]:
                kenar[(A[0],A[1],B[1])].append(f'{k[0]}:{k[1]}')
E={k:sorted(set(v)) for k,v in kenar.items()}
cel=[(g,a,b,E[(g,a,b)],E[(g,b,a)]) for (g,a,b) in E if (g,b,a) in E and a<b]
def zincir(g):
    G=collections.defaultdict(set)
    for (gg,a,b) in E:
        if gg==g and (gg,b,a) not in E: G[a].add(b)
    best=[]
    def dfs(n,yol):
        nonlocal best
        if len(yol)>len(best): best=yol[:]
        for m in G[n]:
            if m not in yol: dfs(m,yol+[m])
    for n in list(G): dfs(n,[n])
    return best
OUT={'kenarlar':{f'{g} {a} → {b}':v for (g,a,b),v in sorted(E.items())},'celisen':cel,'zincir_insan':zincir('İ'),'zincir_kozmos':zincir('K')}
json.dump(OUT,open('ciktilar/yaratilis_sira.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for k,v in OUT['kenarlar'].items(): print(k,v)
print('\nÇELİŞEN:'); [print(' ',x) for x in cel]
print('\nen uzun zincir İNSAN:',' → '.join(OUT['zincir_insan'])); print('en uzun zincir KOZMOS:',' → '.join(OUT['zincir_kozmos']))
