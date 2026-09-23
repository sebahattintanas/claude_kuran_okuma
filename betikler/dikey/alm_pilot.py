# -*- coding: utf-8 -*-
"""ALM dikey mercek pilotu — ön-kayıt: notlar/ON_KAYIT_dikey_ALM.md"""
import re, random, collections, json, sys
MORPH = sys.argv[1] if len(sys.argv) > 1 else 'veri/morph.txt'
SIL = re.compile('[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u0640]')
ELIF = str.maketrans({'ٱ':'ا','أ':'ا','إ':'ا','آ':'ا'})
def rasm(s): return SIL.sub('', s).translate(ELIF)

W = collections.OrderedDict(); ETK = collections.defaultdict(list)
for sat in open(MORPH, encoding='utf-8'):
    p = sat.rstrip('\n').split('\t')
    if len(p) < 4: continue
    s, a, w, _ = map(int, p[0].split(':'))
    W.setdefault((s, a, w), []).append(p[1]); ETK[(s, a, w)].append(p[3])
AY = collections.OrderedDict()
MUK = []
for (s, a, w), segs in W.items():
    r = rasm(''.join(segs))
    if any(t.startswith('INL') for t in ETK[(s, a, w)]):
        MUK.append(((s, a, w), r)); r = None
    AY.setdefault((s, a), []).append(((s, a, w), r, segs, ETK[(s, a, w)]))

# Ö1 kelime içi
# ALM hedefi ELLE YAZILMAZ: mukattaa kelimesinin (2:1) rasmından türetilir
HEDEF = rasm(''.join(W[(2, 1, 1)]))
o1 = []; tur = collections.Counter()
for k, kel in AY.items():
    for key, r, segs, et in kel:
        if r and HEDEF in r:
            if r == HEDEF: t = 'tam kelime (mukattaa rasmı)'
            elif any(x.startswith('DET') for x in et) and rasm(segs[[x.startswith('DET') for x in et].index(True)+1] if len(segs)>1 else '').startswith('م') : t = 'ال + م-başlı kelime'
            else: t = 'kök/kalıp içi'
            o1.append((key, r, t)); tur[t] += 1
# Ö2 sınır atlayan
o2 = []
for k, kel in AY.items():
    parts = [r for _, r, _, _ in kel if r]
    if not parts: continue
    sinir = set(); pos = 0
    for r in parts: pos += len(r); sinir.add(pos)
    dz = ''.join(parts)
    for m in re.finditer('(?=الم)', dz):
        i = m.start()
        if (i+1) in sinir or (i+2) in sinir: o2.append((k, dz[max(0,i-4):i+7]))
# Ö3 kelime başları
def o3say(ay):
    c = 0; vak = []
    for k, kel in ay.items():
        ilk = [r[0] for _, r, _, _ in kel if r]
        for i in range(len(ilk)-2):
            if ilk[i:i+3] == ['ا','ل','م']: c += 1; vak.append((k, i))
    return c, vak
g3, v3 = o3say(AY)
# Ö4 ayet başları (mukattaa ayeti dahil, ilk harfiyle)
ILK = collections.OrderedDict()
for (s,a,w),segs in W.items():
    if (s,a) not in ILK: ILK[(s,a)] = rasm(''.join(segs))[0]
SUR = collections.defaultdict(list)
for (s,a),h in ILK.items(): SUR[s].append(((s,a),h))
def o4say(sur):
    c=0; vak=[]
    for s,L in sur.items():
        hs=[h for _,h in L]
        for i in range(len(hs)-2):
            if hs[i:i+3]==['ا','ل','م']: c+=1; vak.append(L[i][0])
    return c,vak
g4, v4 = o4say(SUR)
rnd = random.Random(0); N=1000; b3=b4=0; d3=[]; d4=[]
for _ in range(N):
    P={}
    for k,kel in AY.items():
        kk=kel[:]; rnd.shuffle(kk); P[k]=kk
    x,_=o3say(P); d3.append(x); b3+= x>=g3
    Q={}
    for s,L in SUR.items():
        LL=L[:]; rnd.shuffle(LL); Q[s]=LL
    y,_=o4say(Q); d4.append(y); b4+= y>=g4
import statistics as st
out = {
 'mukattaa_hariç_tutulan': len(MUK),
 'O1_kelime_ici': {'toplam': len(o1), 'tur': dict(tur)},
 'O1_tam_kelime_ornek': [f'{k[0]}:{k[1]}' for k,r,t in o1 if t=='tam kelime الم'],
 'O1_kok_ici_ornek': [(f'{k[0]}:{k[1]}:{k[2]}', r) for k,r,t in o1 if t=='kök/kalıp içi'][:40],
 'O2_sinir_atlayan': len(o2), 'O2_ornek': [(f'{k[0]}:{k[1]}',x) for k,x in o2[:12]],
 'O3': {'gozlenen': g3, 'perm_ort': round(st.mean(d3),1), 'perm_sd': round(st.pstdev(d3),1), 'p': round((b3+1)/(N+1),4)},
 'O4': {'gozlenen': g4, 'perm_ort': round(st.mean(d4),2), 'perm_sd': round(st.pstdev(d4),2), 'p': round((b4+1)/(N+1),4), 'vakalar': [f'{s}:{a}' for s,a in v4]},
}
json.dump(out, open('ciktilar/dikey_alm_pilot.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))
