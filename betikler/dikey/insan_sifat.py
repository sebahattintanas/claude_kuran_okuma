# -*- coding: utf-8 -*-
"""(A) İnsâna yüklenen sıfat adayları. Ön-kayıt: notlar/ON_KAYIT_insan_sifat_ve_sira.md"""
import collections, json, unicodedata
NF=lambda x: unicodedata.normalize('NFC',x)
KEL=collections.OrderedDict()
for l in open('veri/morph.txt',encoding='utf-8'):
    p=l.rstrip('\n').split('\t'); s,a,w,_=map(int,p[0].split(':'))
    KEL.setdefault((s,a,w),[]).append(dict(f=p[1],pos=p[2],t=p[3].split('|')))
LEMS={x[4:] for v in KEL.values() for sg in v for x in sg['t'] if x.startswith('LEM:')}
cz={NF(x):x for x in LEMS}; INS=cz[NF('إِنسان')]
AY=collections.OrderedDict()
for (s,a,w),v in KEL.items(): AY.setdefault((s,a),[]).append(v)
lem=lambda sg:next((x[4:] for x in sg['t'] if x.startswith('LEM:')),'?')
aday=[]
for (s,a),L_ in AY.items():
    for i,segs in enumerate(L_):
        if not any(lem(sg)==INS for sg in segs): continue
        for j in range(i+1,min(i+7,len(L_))):
            ss=L_[j]
            if any(sg['pos']=='P' and 'P' in sg['t'] and 'PREF' in sg['t'] for sg in ss): continue   # bitişik harf-i cer
            if j>0 and any(sg['pos']=='P' and 'P' in sg['t'] and 'PREF' not in sg['t'] for sg in L_[j-1]): continue  # ayrık harf-i cer
            if any('PRON' in sg['t'] for sg in ss): continue
            n=[sg for sg in ss if sg['pos']=='N' and 'MS' in sg['t'] and 'INDEF' in sg['t'] and ('NOM' in sg['t'] or 'ACC' in sg['t'])]
            if n:
                aday.append(dict(ayet=f'{s}:{a}',lem=lem(n[0]),form=''.join(x['f'] for x in ss),hal=next(c for c in ('NOM','ACC') if c in n[0]['t']),
                    uzaklik=j-i,baglam=' '.join(''.join(x['f'] for x in w) for w in L_[max(0,i-2):j+2])))
json.dump(aday,open('ciktilar/insan_sifat_aday.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(aday))
for i,x in enumerate(aday,1): print(i,x['ayet'],x['lem'],x['hal'],x['uzaklik'],'|',x['baglam'])
