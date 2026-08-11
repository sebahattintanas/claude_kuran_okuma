# -*- coding: utf-8 -*-
"""TAM-AYET ÖZDEŞLİĞİ: normalize edilmiş ayet metni birebir aynı olan ayetler.
Sonra: hangi sûre çiftleri kaç tam-ayet paylaşıyor?"""
import json, re, unicodedata
from collections import defaultdict
d=json.load(open('../repo/veri/kuran_veri.json'))
def sad(s):
    s=unicodedata.normalize('NFC',s)
    s=re.sub(r'[\u064B-\u0652\u0670\u06DD\u06D6-\u06ED\u0640]','',s)
    s=s.replace('ٱ','ا').replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ى','ي').replace('ة','ه')
    s=re.sub(r'[^\u0621-\u064A ]',' ',s)
    return re.sub(r'\s+',' ',s).strip()
m=defaultdict(list); ns=defaultdict(int)
for s in d['sureler']:
    for a in s['ayetler']:
        t=sad(a['ar_saf'])
        if len(t.split())<3: continue          # 3 kelimeden kısa ayetler dışarıda
        m[t].append((s['no'],a['no'])); 
    ns[s['no']]=len(s['ayetler'])
cift=defaultdict(list)
for t,ks in m.items():
    sur=sorted({k[0] for k in ks})
    if len(sur)<2: continue
    for i in range(len(sur)):
        for j in range(i+1,len(sur)):
            cift[(sur[i],sur[j])].append(t)
rows=sorted(cift.items(), key=lambda kv:-len(kv[1]))
print('tam-ayet paylaşan sûre çifti sayısı: %d'%len(rows))
print()
print('--- en çok tam-ayet paylaşan 12 çift ---')
for (A,B),ts in rows[:12]:
    print(' %3d-%-4d  %2d ayet  (nA=%d nB=%d)'%(A,B,len(ts),ns[A],ns[B]))
print()
r=[(k,v) for k,v in rows if k==(56,69)]
sira=[i for i,(k,v) in enumerate(rows,1) if k==(56,69)]
print('56-69: %d tam-ayet | sıra %s / %d'%(len(r[0][1]) if r else 0, sira, len(rows)))
for t in (r[0][1] if r else []): print('   »',t)
# 69'un tüm tam-ayet ortakları
print()
print('--- 69 hangi sûrelerle tam-ayet paylaşıyor ---')
for (A,B),ts in rows:
    if 69 in (A,B): print('  %d-%d : %d  %s'%(A,B,len(ts),ts))
