# -*- coding: utf-8 -*-
import json
from collections import Counter, defaultdict
D=json.load(open('defter.json',encoding='utf-8'))
S=27
rows=sorted([r for r in D if r['k'][0]==S], key=lambda r:r['k'][1])
tot=len(rows); kel=sum(r['n'] for r in rows)
KEL=sum(r['n'] for r in D); AA=sum(len(r['A']) for r in D); RR=sum(len(r['R']) for r in D)
A=sum(len(r['A']) for r in rows); R=sum(len(r['R']) for r in rows)
print('ayet',tot,'kelime',kel,'ort',round(kel/tot,2),'tip',rows[0]['tip'],'nuz',rows[0]['nuz'])
print('A',A,'kat',round((A/kel)/(AA/KEL),2),'R',R,'kat',round((R/kel)/(RR/KEL),2),'A/R',round(A/R,3))
print('lafizli ayet',[(r['k'][1],len(r['A'])) for r in rows if r['A']])
print('ilk R ayet', [r['k'][1] for r in rows if r['R']][:6])
fsc=Counter(r['fs'][2] for r in rows); son=Counter(r['fs'][1] for r in rows)
print('fasila sinif',fsc.most_common()); print('son harf',son.most_common(6))
print('kirik',[r['k'][1] for r in rows if r['z'].get('kafiye_kirik')])
es=Counter(); ay=0; muhur=0
for r in rows:
    if r['esma']:
        ay+=1
        for p,e in r['esma']: es[e]+=1
    if r.get('esma_k') and r['esma_k'].get('muhur'): muhur+=1
print('esma token',sum(es.values()),'ayet',ay,'muhur',muhur); print(es.most_common())
ed=Counter(); fg=Counter(); ir=Counter(); zm=Counter(); vf=Counter(); pas=0; pasay=0; ilt=[]
for r in rows:
    for e in r['edim']: ed[e]+=1
    for f in r['fig']: fg[f]+=1
    for k,v in r['irab'].items(): ir[k]+=v
    for k,v in r['zmn'].items(): zm[k]+=v
    for k,v in r['vf'].items(): vf[k]+=v
    pas+=r['pas']; pasay+=1 if r['pas'] else 0
    if r['ilt']: ilt.append((r['k'][1],r['ilt_yon']))
t=sum(ir.values())
print('edim',ed.most_common()); print('fig',fg.most_common())
print('irab',ir.most_common(),'ACC payı',round(ir['ACC']/t,3))
print('zmn',zm.most_common(),'vf',sorted(vf.items(),key=lambda x:-x[1]))
print('pas',pas,'/ayet',pasay,'iltifat',len(ilt),ilt)
yd=Counter(r['yildiz'] for r in rows); print('yildiz',sorted(yd.items()))
print('yildiz3',[r['k'][1] for r in rows if r['yildiz']==3])
print('hapaks',[(r['k'][1],r['hapaks']) for r in rows if r['hapaks']])
print('esit',[(r['k'][1],r['esit']) for r in rows if r['esit']][:30])
print('esit ayet sayisi',sum(1 for r in rows if r['esit']))
adli=Counter(); adsiz=Counter()
for r in rows:
    for x in r['adli']: adli[(x[1],x[2])]+=1
    for x in r['adsiz']: adsiz[x[1]]+=1
print('adli',adli.most_common()); print('adsiz',adsiz.most_common())
print('nakarat',[r['k'][1] for r in rows if r['dugum'].get('nakarat')][:40])
print('nakarat sayisi',sum(1 for r in rows if r['dugum'].get('nakarat')))
ns=sorted(((r['n'],r['k'][1]) for r in rows),reverse=True)
print('en uzun',ns[:5],'en kisa',ns[-5:])
