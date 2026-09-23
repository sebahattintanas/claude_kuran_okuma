# -*- coding: utf-8 -*-
"""(2) insân dikey yığını — betimsel. Ön-kayıt: notlar/ON_KAYIT_insan_ayet_birimi.md"""
import collections, json
exec(open('betikler/dikey/insan_uclu.py',encoding='utf-8').read().split('# ---- A')[0])
FORM=collections.defaultdict(str)
for l in open('veri/morph.txt',encoding='utf-8'):
    p=l.rstrip('\n').split('\t'); s,a,w,_=map(int,p[0].split(':')); FORM[(s,a,w)]+=p[1]
NZ=json.load(open('tablolar/nuzul.json'))['sira']; NZR={s:i+1 for i,s in enumerate(NZ)}
KT=json.load(open('tablolar/kok_turkce.json'))
rows=[]; fiil_kok=collections.Counter(); hal_mss=collections.Counter()
for (s,a),L_ in AY.items():
    idx=[i for i,d in enumerate(L_) if d['h']=='INS']
    if not idx: continue
    n=len(L_)
    fiiller=[]
    for i,d in enumerate(L_):
        for t in d['segs']:
            if 'V' in [x for x in t] or any(x in t for x in ('PERF','IMPF','IMPV')):
                lm=[x[4:] for x in t if x.startswith('LEM:')]; rk=[x[5:] for x in t if x.startswith('ROOT:')]
                if lm and rk: fiiller.append((i,lm[0],rk[0],'PASS' in t))
    for i in idx:
        hal=next((c for c in ('NOM','ACC','GEN') if c in L_[i]['ht']),'?')
        yakin=min(fiiller,key=lambda f:abs(f[0]-i)) if fiiller else None
        kok=set().union(*[d['kok'] for d in L_])
        r=dict(ayet=f'{s}:{a}',tip=TIP[(s,a)],nuzul=NZR.get(s),hal=hal,konum=round(i/(n-1),2) if n>1 else 0,
               fiil=[f"{lm}{' (edilgen)' if ps else ''}" for _,lm,_,ps in fiiller],
               yakin=(f"{yakin[1]} — {KT.get(yakin[2],'?').split(';')[0]}" if yakin else '-'),
               khalk='خلق' in kok, mess='مسس' in kok, serr='شرر' in kok,
               metin=' '.join(FORM[(s,a,w)] for w in range(1,n+1)))
        rows.append(r)
        if yakin: fiil_kok[yakin[2]]+=1
        if r['mess']: hal_mss[hal]+=1
json.dump(rows,open('ciktilar/insan_yigin.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
# markdown
md=['# insân dikey yığını — mushaf sırası','',
    '*Betimsel. Örüntüler KAPATILAMAZ (aday 899). İniş sırası `nuzul.json`\'dan — DOĞRULANMAMIŞ liste.*','',
    '| ayet | M/D | iniş | hâl | konum | en yakın fiil | خلق | مسس | شرر | metin |','|---|---|---|---|---|---|---|---|---|---|']
for r in rows:
    md.append(f"| {r['ayet']} | {r['tip']} | {r['nuzul']} | {r['hal']} | {r['konum']} | {r['yakin']} | {'●' if r['khalk'] else ''} | {'●' if r['mess'] else ''} | {'●' if r['serr'] else ''} | {r['metin']} |")
open('ciktilar/insan_yigin.md','w',encoding='utf-8').write('\n'.join(md))
H=collections.Counter(r['hal'] for r in rows)
print('token',len(rows),'hâl',dict(H))
print('en yakın fiil kökleri:',[(k,KT.get(k,'?').split(';')[0][:18],v) for k,v in fiil_kok.most_common(15)])
print('مسس ayetlerinde insân hâli:',dict(hal_mss))
print('خلق ayetlerinde hâl:',dict(collections.Counter(r['hal'] for r in rows if r['khalk'])))
print('konum ilk üçte bir:',sum(r['konum']<=1/3 for r in rows),'/',len(rows))
for r in rows:
    if r['mess'] or r['serr']: print(r['ayet'],r['hal'],r['yakin'],'|',r['metin'][:90])
