# -*- coding: utf-8 -*-
"""Süleyman merceği — ön-kayıt: notlar/ON_KAYIT_dikey_suleyman.md"""
import re, random, collections, json, statistics as st
SIL = re.compile('[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u0640]')
ELIF = str.maketrans({'ٱ':'ا','أ':'ا','إ':'ا','آ':'ا'})
rasm = lambda s: SIL.sub('', s).translate(ELIF)
W = collections.OrderedDict()
for l in open('veri/morph.txt', encoding='utf-8'):
    p = l.rstrip('\n').split('\t'); s,a,w,_ = map(int, p[0].split(':'))
    W.setdefault((s,a,w), []).append((p[1], p[3]))
AY = collections.OrderedDict()
for (s,a,w), segs in W.items():
    et = '|'.join(t for _,t in segs)
    kok = [m for m in re.findall(r'ROOT:([^|]+)', et)]
    lem = re.findall(r'LEM:([^|]+)', et)
    AY.setdefault((s,a), []).append(dict(w=w, r=rasm(''.join(x for x,_ in segs)), kok=kok, lem=lem,
        pn='PN' in et.split('|'), sul='سُلَيْمان' in lem, inl=et.startswith('INL')))
OUT = {}
# açık anma
tok = [(k, x['w']) for k,L in AY.items() for x in L if x['sul']]
ayet = sorted({k for k,_ in tok})
OUT['acik'] = {'token': len(tok), 'ayet': len(ayet), 'sure': dict(collections.Counter(k[0] for k,_ in tok)),
               'ayetler': [f'{s}:{a}' for s,a in ayet], 'isim_rasm': sorted({x['r'] for L in AY.values() for x in L if x['sul']})}
# gizli dizi
def g2say(ay, hedef):
    c=0; vak=[]
    for k,L in ay.items():
        parts=[x for x in L if not x['inl']]
        dz=''; sin=[]
        for x in parts: sin.append((len(dz), len(dz)+len(x['r']), x['sul'])); dz+=x['r']
        for m in re.finditer('(?=%s)'%hedef, dz):
            i,j=m.start(), m.start()+len(hedef)
            icinde=[b for b in sin if b[0]<=i and j<=b[1]]
            if icinde: continue            # tek kelime içinde (G1 ya da isim)
            if any(b[2] and b[0]<j and i<b[1] for b in sin): continue  # ismin kendisine değiyor
            c+=1; vak.append((f'{k[0]}:{k[1]}', dz[max(0,i-5):j+5]))
    return c, vak
rnd=random.Random(0)
# hedef dizgeler ELLE YAZILMAZ: ismin korpustaki rasm biçimlerinden türetilir
ISIM = sorted({x['r'] for L in AY.values() for x in L if x['sul']}, key=len)
HEDEFLER = [re.sub('^[وفلب]+', '', ISIM[0])]
for hedef in HEDEFLER:
    g1=[(f'{k[0]}:{k[1]}:{x["w"]}', x['r']) for k,L in AY.items() for x in L if hedef in x['r'] and not x['sul']]
    g2,v2=g2say(AY,hedef)
    ilk=lambda ay: sum(1 for L in ay.values() for i in range(len(L)-len(hedef)+1)
                       if ''.join(x['r'][0] for x in L[i:i+len(hedef)] if x['r'])==hedef)
    g3=ilk(AY)
    d2=[];d3=[]
    for _ in range(1000):
        P={k:rnd.sample(L,len(L)) for k,L in AY.items()}
        d2.append(g2say(P,hedef)[0]); d3.append(ilk(P))
    OUT['gizli_'+hedef]={'G1_kelime_ici':g1,'G2_sinir_atlayan':{'gozlenen':g2,'vakalar':v2,
        'perm_ort':round(st.mean(d2),2),'perm_sd':round(st.pstdev(d2),2),'p':round((sum(x>=g2 for x in d2)+1)/1001,4)},
        'G3_bas_harf':{'gozlenen':g3,'perm_ort':round(st.mean(d3),3),'p':round((sum(x>=g3 for x in d3)+1)/1001,4)}}
# iskelet س-ل-م
isk=collections.Counter(); diger=[]
for k,L in AY.items():
    for x in L:
        if x['sul'] or x['inl'] or 'سلم' not in x['r']: continue
        t='kök سلم' if 'سلم' in x['kok'] else 'başka'
        isk[t]+=1
        if t=='başka': diger.append((f'{k[0]}:{k[1]}', x['r'], x['kok']))
OUT['iskelet_slm']={'dagilim':dict(isk),'baska_ornek':diger[:30]}
# dikey yığın
yig=[]
for (s,a) in ayet:
    L=AY[(s,a)]; n=len(L)
    poz=[x['w'] for x in L if x['sul']]
    ust=AY.get((s,a-1)); alt=AY.get((s,a+1))
    yig.append({'ayet':f'{s}:{a}','n':n,'ilk':L[0]['r'],'son':L[-1]['r'],'fasila':L[-1]['r'][-1],
        'isim_konum':poz,'goreli':[round((p-1)/(n-1),2) if n>1 else 0 for p in poz],
        'ust_son':ust[-1]['r'] if ust else None,'alt_ilk':alt[0]['r'] if alt else None})
OUT['dikey_yigin']=yig
# komşuluk (±1 ayet)
pencere=sorted({(s,a+d) for s,a in ayet for d in (-1,0,1) if (s,a+d) in AY})
sahne=[]; 
for k in pencere:
    if sahne and sahne[-1][-1][0]==k[0] and sahne[-1][-1][1]+1>=k[1]: sahne[-1].append(k)
    else: sahne.append([k])
sahne_id={k:i for i,sc in enumerate(sahne) for k in sc}
kor=collections.Counter(r for L in AY.values() for x in L for r in set(x['kok']))
TOP=sum(len(L) for L in AY.values()); pw=sum(len(AY[k]) for k in pencere)
gz=collections.Counter(); sc=collections.defaultdict(set)
for k in pencere:
    for x in AY[k]:
        for r in set(x['kok']): gz[r]+=1; sc[r].add(sahne_id[k])
rows=[]
for r,o in gz.items():
    e=kor[r]*pw/TOP
    if o>=3: rows.append((r,o,round(e,2),round(o/e,1),len(sc[r])))
rows.sort(key=lambda x:-x[3])
pn=collections.Counter(l for k in pencere for x in AY[k] if x['pn'] and not x['sul'] for l in x['lem'] if l not in ('اللَّه',))
OUT['komsuluk']={'pencere_ayet':len(pencere),'sahne':len(sahne),'sahneler':[f'{sc_[0][0]}:{sc_[0][1]}-{sc_[-1][1]}' for sc_ in sahne],
    'zengin':rows[:30],'zengin_3sahne_ve_x3':[x for x in rows if x[4]>=3 and x[3]>=3],'pn':pn.most_common(12)}
json.dump(OUT,open('ciktilar/dikey_suleyman.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
