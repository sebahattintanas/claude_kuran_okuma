# -*- coding: utf-8 -*-
import json,re,random
d=json.load(open('../repo/veri/kuran_veri.json'))
A=d['sureler'][68]['ayetler']
def sonharf(a):
    w=[x for x in a['ar_saf'].split() if re.search(r'[\u0621-\u064A]',x)][-1]
    w=re.sub(r'[\u064B-\u0652\u0670\u06DD\u06D6-\u06ED]','',w)
    return w[-1]
son=[sonharf(a) for a in A]
def sinif(c):
    if c in 'ةه': return 'H'      # tâ-marbûta / hâ
    if c in 'نم': return 'N'      # nûn / mîm
    return 'X'
# 30-32 وه: son harf ه ama önceki و → ayrı sınıf
def sinif2(a):
    w=[x for x in a['ar_saf'].split() if re.search(r'[\u0621-\u064A]',x)][-1]
    w=re.sub(r'[\u064B-\u0652\u0670\u06DD\u06D6-\u06ED]','',w)
    if w.endswith('وه'): return 'W'
    return sinif(w[-1])
et=[sinif2(a) for a in A]
print('sınıf dizisi:'); print(''.join(et))
def saflik(seq):
    """en iyi 2-kesimli üç-blok saflığı"""
    n=len(seq); best=0; bi=None
    for i in range(1,n-1):
        for j in range(i+1,n):
            s=0
            for blk in (seq[:i],seq[i:j],seq[j:]):
                if blk: s+=max(blk.count(c) for c in set(blk))
            if s>best: best,bi=s,(i,j)
    return best,bi
obs,kes=saflik(et)
print('gözlem saflık: %d/%d = %.3f  kesimler: ayet %d ve %d sonrası'%(obs,len(et),obs/len(et),kes[0],kes[1]))
rnd=[]
random.seed(69)
for _ in range(2000):
    x=et[:]; random.shuffle(x); rnd.append(saflik(x)[0])
pv=sum(1 for r in rnd if r>=obs)/len(rnd)
print('permütasyon (2000, sûre içi sıra karıştırma): ortalama %.1f, maks %d, p=%.4f'%(sum(rnd)/len(rnd),max(rnd),pv))
