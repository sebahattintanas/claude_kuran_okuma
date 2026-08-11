# -*- coding: utf-8 -*-
"""2. DÜĞÜM AĞI v2 — nakarat düzeltmesi.

SORUN (v1): sûre içinde tekrarlanan nakaratlar birbirine bağlanıp yapay
klik üretiyordu. 55. sûrenin 31 kez geçen فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ
nakaratı tüm en-yüksek-dereceli ayetleri işgal ediyordu (derece 31).

DÜZELTME:
 (a) NAKARAT = aynı sûre içinde normalize metni birebir aynı olan ayet kümesi.
     Her küme tek düğüme indirgenir; küme-içi kenarlar SİLİNİR.
 (b) Kenarlar iki sınıfa ayrılır: iç-bağ (aynı sûre) / dış-bağ (sûreler arası).
     Merkezîlik DIŞ-BAĞ üzerinden ölçülür — iç-bağ ayrıca raporlanır.
 (c) Nakaratlar kendi başına bir ÖLÇÜM olarak ayrı dosyaya yazılır.
"""
import json, re, unicodedata
from collections import defaultdict, Counter

D = json.load(open('defter.json'))
d = json.load(open('../repo/veri/kuran_veri.json'))
def sad(x):
    x = unicodedata.normalize('NFC', x)
    x = re.sub(r'[\u064B-\u0652\u0670\u06DD\u06D6-\u06ED\u0640]', '', x)
    x = x.replace('ٱ','ا').replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ى','ي').replace('ة','ه')
    return re.sub(r'\s+', ' ', re.sub(r'[^\u0621-\u064A ]', ' ', x)).strip()

# --- (c) nakarat tespiti: aynı sûre içinde birebir tekrar ---
grup = defaultdict(list)
for s in d['sureler']:
    for a in s['ayetler']:
        t = sad(a['ar_saf'])
        if len(t.split()) >= 3:
            grup[(s['no'], t)].append(a['no'])
nakarat = {k: v for k, v in grup.items() if len(v) > 1}
temsil = {}          # (sure,ayet) -> temsilci ayet
nak_uye = {}
for (s, t), ays in nakarat.items():
    for a in ays:
        temsil[(s, a)] = (s, ays[0]); nak_uye[(s, a)] = len(ays)

print('NAKARAT: %d küme, %d ayet' % (len(nakarat), sum(len(v) for v in nakarat.values())))
top = sorted(((len(v), s, v[0]) for (s, t), v in nakarat.items()), reverse=True)[:10]
for n, s, a in top:
    print('   sûre %3d: %2d kez (ilk %d:%d)' % (s, n, s, a))
sn = Counter(s for (s, t) in nakarat for _ in [0])
sc = Counter()
for (s, t), v in nakarat.items(): sc[s] += len(v)
print('   nakaratı en çok olan sûreler:', sc.most_common(8))

# --- (a)(b) graf yeniden ---
ic = defaultdict(set); dis = defaultdict(set)
for r in D:
    k = tuple(r['k'])
    kk = temsil.get(k, k)
    hedefler = []
    for g, hs in r['xref']: hedefler += [tuple(h) for h in hs]
    hedefler += [tuple(h) for h in r['esit']]
    for h in hedefler:
        hh = temsil.get(h, h)
        if hh == kk: continue                 # nakarat-içi kenar SİLİNDİ
        (ic if hh[0] == kk[0] else dis)[kk].add(hh)

for r in D:
    k = tuple(r['k']); kk = temsil.get(k, k)
    r['dugum'] = {'dis': len(dis[kk]), 'ic': len(ic[kk]),
                  'nakarat': nak_uye.get(k, 0), 'temsil': list(kk) if kk != k else None}

json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)
json.dump({'%d:%d' % k: {'dis': sorted('%d:%d' % h for h in dis[k]), 'ic': sorted('%d:%d' % h for h in ic[k])}
           for k in set(list(dis) + list(ic))}, open('ayet_grafi.json', 'w', encoding='utf-8'), ensure_ascii=False)
json.dump({'%d' % s: {'kume': len([1 for (ss, t) in nakarat if ss == s]), 'ayet': sc[s]} for s in sc},
          open('nakarat.json', 'w', encoding='utf-8'), ensure_ascii=False)

print()
print('graf v2: dış-bağı olan ayet %d | iç-bağı olan %d' % (
    sum(1 for r in D if r['dugum']['dis']), sum(1 for r in D if r['dugum']['ic'])))
print()
print('--- DIŞ-BAĞ derecesi en yüksek 15 ayet ---')
print('%-9s %-6s %-5s %-4s' % ('ayet', 'dış', 'iç', 'n'))
for r in sorted(D, key=lambda r: -r['dugum']['dis'])[:15]:
    print('%-9s %-6d %-5d %-4d' % ('%d:%d' % tuple(r['k']), r['dugum']['dis'], r['dugum']['ic'], r['n']))
print()
sd = defaultdict(list)
for r in D: sd[r['k'][0]].append(r['dugum']['dis'])
ort = sorted(((sum(v)/len(v), s, len(v)) for s, v in sd.items() if len(v) >= 20), reverse=True)
print('sûre başına ortalama DIŞ-BAĞ (n>=20) — en bağlı 10:')
for o, s, n_ in ort[:10]: print('   sûre %3d: %.2f' % (s, o))
print('en az bağlı 6:')
for o, s, n_ in ort[-6:]: print('   sûre %3d: %.2f' % (s, o))
