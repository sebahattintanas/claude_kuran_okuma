# -*- coding: utf-8 -*-
import json, re, unicodedata, random, bisect
from collections import defaultdict
d = json.load(open('../repo/veri/kuran_veri.json'))
def sad(s):
    s = unicodedata.normalize('NFC', s)
    s = re.sub(r'[\u064B-\u0652\u0670\u06DD\u06D6-\u06ED\u0640]', '', s)
    s = s.replace('ٱ','ا').replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ى','ي').replace('ة','ه')
    s = re.sub(r'[^\u0621-\u064A ]', ' ', s)
    return re.sub(r'\s+',' ', s).strip()
ayet={}; ns=defaultdict(int)
for s in d['sureler']:
    for a in s['ayetler']:
        ayet[(s['no'],a['no'])]=sad(a['ar_saf']).split(); ns[s['no']]+=1
def calc(N, maxsur=2):
    gram=defaultdict(set)
    for k,w in ayet.items():
        for i in range(len(w)-N+1): gram[' '.join(w[i:i+N])].add(k)
    seyrek={g:ks for g,ks in gram.items() if len({k[0] for k in ks})==maxsur}
    cift=defaultdict(set); gramlist=defaultdict(list)
    for g,ks in seyrek.items():
        sur=sorted({k[0] for k in ks})
        for ii in range(len(sur)):
            for jj in range(ii+1,len(sur)):
                A,B=sur[ii],sur[jj]
                for ka in [k for k in ks if k[0]==A]:
                    for kb in [k for k in ks if k[0]==B]:
                        cift[(A,B)].add((ka[1],kb[1])); gramlist[(A,B)].append(g)
    return cift,gramlist,seyrek
for N in (2,3):
    cift,gl,sy=calc(N)
    P=cift.get((56,69),set())
    print('N=%d | seyrek %d-gram: %d | 56-69 eşleşen ayet çifti: %d'%(N,N,len(sy),len(P)))
    print('   çiftler:',sorted(P))
    print('   ortak %d-gramlar:'%N, sorted(set(gl.get((56,69),[]))))
    # yoğunluk sıralaması: m / sqrt(nA*nB)
    rows=[]
    for (A,B),Q in cift.items():
        yog=len(Q)/ (ns[A]*ns[B])**0.5
        rows.append((A,B,len(Q),yog))
    rows.sort(key=lambda r:-r[3])
    sr=[i for i,r in enumerate(rows,1) if (r[0],r[1])==(56,69)]
    print('   yoğunluk sıralaması (m/sqrt(nA*nB)): %s / %d çift'%(sr, len(rows)))
    print('   ilk 8 yoğun çift:', [(a,b,m,round(y,3)) for a,b,m,y in rows[:8]])
    print()
