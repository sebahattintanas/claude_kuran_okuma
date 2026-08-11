# -*- coding: utf-8 -*-
"""
ÖN-KAYIT (hesaplamadan önce sabitlendi):
H: Sûre 69 ile sûre 56, korpustaki diğer sûre çiftlerinden daha güçlü bir
   SIRALI lafız örtüşmesi gösterir.
Ölçüm:
 1) Her ayet NFC + hareke/işaret temizliği ile normalize edilir, kelimelere bölünür.
 2) n=3 kelimelik ardışık dizgiler (3-gram) çıkarılır.
 3) SEYREK 3-gram: tam olarak 2 farklı sûrede geçen 3-gram. (Formülvari
    yaygın kalıplar -- 'قل هو الله', 'ان الله' vb. -- böylece elenir.)
 4) Bir sûre çifti (A,B) için eşleşme kümesi: seyrek 3-gram'ın A'da i., B'de
    j. ayette geçtiği (i,j) çiftleri.
 5) m = eşleşen ayet-çifti sayısı (tekilleştirilmiş).
 6) L = (i,j) çiftleri arasında her iki koordinatta ARTAN en uzun zincir (LIS).
    L, sıranın korunma derecesidir.
Null (yalnızca sıra bileşeni için): A ve B'nin ayet etiketleri rastgele
    permüte edilir, aynı eşleşme kümesiyle L yeniden hesaplanır. 1000 tur.
    p = P(L_null >= L_göz).
Bonferroni: eşleşmesi olan sûre çifti sayısı üzerinden.
Not: 69 ile 56 karşılaştırması bu testi DOĞURAN gözlemdir; bu yüzden
    test tüm çiftlere körlemesine uygulanır ve 69-56'nın SIRALAMASI raporlanır.
"""
import json, re, unicodedata, random
from collections import defaultdict

d = json.load(open('../repo/veri/kuran_veri.json'))
def sad(s):
    s = unicodedata.normalize('NFC', s)
    s = re.sub(r'[\u064B-\u0652\u0670\u06DD\u06D6-\u06ED\u0640\u06E0-\u06ED]', '', s)
    s = s.replace('ٱ','ا').replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ى','ي').replace('ة','ه')
    s = re.sub(r'[^\u0621-\u064A ]', ' ', s)
    return re.sub(r'\s+',' ', s).strip()

ayet = {}   # (sure, ayet_no) -> kelimeler
sira = defaultdict(list)
for s in d['sureler']:
    for a in s['ayetler']:
        w = sad(a['ar_saf']).split()
        ayet[(s['no'], a['no'])] = w
        sira[s['no']].append(a['no'])

N = 3
gram = defaultdict(set)   # 3gram -> {(sure,ayet)}
for k, w in ayet.items():
    for i in range(len(w)-N+1):
        gram[' '.join(w[i:i+N])].add(k)

seyrek = {g: ks for g, ks in gram.items() if len({k[0] for k in ks}) == 2}
print('toplam 3-gram: %d | tam 2 sûrede geçen (seyrek): %d' % (len(gram), len(seyrek)))

cift = defaultdict(set)
for g, ks in seyrek.items():
    sur = sorted({k[0] for k in ks})
    A, B = sur
    for ka in [k for k in ks if k[0]==A]:
        for kb in [k for k in ks if k[0]==B]:
            cift[(A,B)].add((ka[1], kb[1]))

def LIS(pairs):
    ps = sorted(pairs)
    import bisect
    tails = []
    for _, j in ps:
        p = bisect.bisect_left(tails, j)
        if p == len(tails): tails.append(j)
        else: tails[p] = j
    return len(tails)

sonuc = []
for (A,B), P in cift.items():
    if len(P) < 4: continue
    sonuc.append((A, B, len(P), LIS(P)))
sonuc.sort(key=lambda r: (-r[3], -r[2]))
print('eşleşmesi >=4 olan sûre çifti: %d' % len(sonuc))
print()
print('--- SIRALI ÖRTÜŞME (L) en yüksek 15 çift ---')
print('%-9s %-4s %-4s' % ('çift','m','L'))
for A,B,m,L in sonuc[:15]:
    print('%3d-%-5d %-4d %-4d' % (A,B,m,L))
r = [x for x in sonuc if {x[0],x[1]}=={56,69}]
print()
print('56-69:', r, '| L sıralaması:', [i for i,x in enumerate(sonuc,1) if {x[0],x[1]}=={56,69}])
json.dump([{'A':a,'B':b,'m':m,'L':l} for a,b,m,l in sonuc], open('ortusme_ham.json','w'))
