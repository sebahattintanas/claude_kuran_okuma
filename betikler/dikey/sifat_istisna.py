# -*- coding: utf-8 -*-
"""Sıfat ayetlerinin istisnaları. Ön-kayıt: notlar/ON_KAYIT_sifat_istisna.md"""
import collections, json, unicodedata
NF=lambda x: unicodedata.normalize('NFC',x)
W=collections.OrderedDict()
for l in open('veri/morph.txt',encoding='utf-8'):
    p=l.rstrip('\n').split('\t'); s,a,w,_=map(int,p[0].split(':'))
    W.setdefault((s,a),collections.OrderedDict()).setdefault(w,[]).append((p[1],p[3].split('|')))
LEMS={x[4:] for v in W.values() for ws in v.values() for _,t in ws for x in t if x.startswith('LEM:')}
cz={NF(x):x for x in LEMS}; ILLA=cz[NF('إِلّا')]; INS=cz[NF('إِنسان')]
metin=lambda k:' '.join(''.join(f for f,_ in ws) for ws in W[k].values())
SIFAT=['4:28','14:34','16:4','17:11','17:67','17:100','22:66','33:72','42:48','43:15','70:19','76:2','100:6','11:9','17:83','18:54','41:49']
def pencere(s,a): return [(s,a+d) for d in range(0,4) if (s,a+d) in W]
def adaylar(keys):
    out=[]
    for s,a in keys:
        for k in pencere(s,a):
            for w,ws in W[k].items():
                for f,t in ws:
                    if f'LEM:{ILLA}' in t:
                        etk='EXP' if 'EXP' in t else ('RES' if 'RES' in t else '?')
                        kel=list(W[k].values()); i=list(W[k]).index(w)
                        out.append(dict(kaynak=f'{s}:{a}',ayet=f'{k[0]}:{k[1]}',etiket=etk,
                            baglam=' '.join(''.join(x for x,_ in v) for v in kel[max(0,i-4):i+7])))
    return out
A1=adaylar([tuple(map(int,x.split(':'))) for x in SIFAT])
insk=[k for k,v in W.items() if any(f'LEM:{INS}' in t for ws in v.values() for _,t in ws)]
A2=adaylar(insk)
json.dump({'sifat':A1,'insan_tum':A2},open('ciktilar/sifat_istisna_aday.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('SIFAT kümesi aday:',len(A1))
for i,x in enumerate(A1,1): print(i,x['kaynak'],'→',x['ayet'],x['etiket'],'|',x['baglam'])
print('\nTÜM insân ayetleri aday:',len(A2),' (tekil ayet:',len({x['ayet'] for x in A2}),')')
