# -*- coding: utf-8 -*-
"""Sâlihât köprüsü. Ön-kayıt: notlar/ON_KAYIT_salihat_kopru.md"""
import collections, json, unicodedata, numpy as np
NF=lambda x: unicodedata.normalize('NFC',x)
AY=collections.OrderedDict()
for l in open('veri/morph.txt',encoding='utf-8'):
    p=l.rstrip('\n').split('\t'); s,a,w,_=map(int,p[0].split(':')); t=p[3].split('|')
    d=AY.setdefault((s,a),{'kok':set(),'lem':set(),'sal':False,'w':set()})
    d['w'].add(w)
    d['kok'].update(x[5:] for x in t if x.startswith('ROOT:')); d['lem'].update(x[4:] for x in t if x.startswith('LEM:'))
KOKLER={r for d in AY.values() for r in d['kok']}; LEMS={x for d in AY.values() for x in d['lem']}
cz={NF(x):x for x in LEMS}
NEG={'كفر','ظلم','خسر','كذب','فسق','ضلل','جرم','عذب'}; OD_K={'أجر','فوز','غفر'}
for r in NEG|OD_K|{'أمن'}: assert r in KOKLER,('KÖK YOK',r)
SAL=cz[NF('صالِحَة')]; JN=cz[NF('جَنَّة')]
for l in open('veri/morph.txt',encoding='utf-8'):
    p=l.rstrip('\n').split('\t'); t=p[3].split('|')
    if f'LEM:{SAL}' in t and 'FP' in t: s,a=map(int,p[0].split(':')[:2]); AY[(s,a)]['sal']=True
win=lambda s,a,r:[(s,x) for x in r if (s,x) in AY]
def ozellik(k):
    s,a=k
    on=win(s,a,range(a-2,a+1)); ar=win(s,a,range(a,a+3)); tum=win(s,a,range(a-2,a+3))
    neg=any(AY[x]['kok']&NEG for x in on)
    od=any((AY[x]['kok']&OD_K) or (JN in AY[x]['lem']) for x in ar)
    return neg, od, sum(len(AY[x]['w']) for x in tum)
F={k:ozellik(k) for k in AY}
uz=np.array([F[k][2] for k in AY]); sinir=np.quantile(uz,np.linspace(0,1,11)[1:-1])
dec=lambda n:int(np.searchsorted(sinir,n,side='right'))
SALK=[k for k in AY if AY[k]['sal']]
TABAN=[k for k in AY if not AY[k]['sal']]
IMAN=[k for k in AY if not AY[k]['sal'] and 'أمن' in AY[k]['kok']]
rng=np.random.default_rng(0)
def test(ix, grup):
    oran=collections.defaultdict(lambda:[0,0])
    for k in grup:
        v=F[k]; x=(v[0] and v[1]) if ix=='kopru' else v[0]
        o=oran[dec(v[2])]; o[0]+=x; o[1]+=1
    ps=[]; gz=0
    for k in SALK:
        v=F[k]; gz+=(v[0] and v[1]) if ix=='kopru' else v[0]
        o=oran[dec(v[2])]; ps.append(o[0]/o[1] if o[1] else 0)
    ps=np.array(ps); sim=(rng.random((20000,len(ps)))<ps).sum(1)
    return dict(gozlenen=int(gz),n=len(SALK),beklenen=round(float(ps.sum()),2),p=round(float(((sim>=gz).sum()+1)/20001),5))
OUT={'n':{'sal':len(SALK),'taban':len(TABAN),'iman':len(IMAN)},
     'M1a':test('kopru',TABAN),'M1b':test('kopru',IMAN),'M2a':test('neg',TABAN),'M2b':test('neg',IMAN)}
OUT['oranlar']={g:{'kopru':round(sum(F[k][0] and F[k][1] for k in G)/len(G),3),'neg':round(sum(F[k][0] for k in G)/len(G),3),'odul':round(sum(F[k][1] for k in G)/len(G),3)} for g,G in (('sal',SALK),('taban',TABAN),('iman',IMAN))}
OUT['sal_ayetler']=[(f'{s}:{a}','K' if F[(s,a)][0] and F[(s,a)][1] else ('N' if F[(s,a)][0] else ('Ö' if F[(s,a)][1] else '-'))) for s,a in SALK]
json.dump(OUT,open('ciktilar/salihat_kopru.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(json.dumps({k:v for k,v in OUT.items() if k!='sal_ayetler'},ensure_ascii=False,indent=1))
print(' '.join(f'{a}{t}' for a,t in OUT['sal_ayetler']))
