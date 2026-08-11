# -*- coding: utf-8 -*-
"""2. DÜĞÜM AĞI — ayet grafı ve merkezîlik.
Düğüm: ayet. Kenar: ortak SEYREK lemma-3gram (2-3 sûrede geçen).
Merkezîlik: derece (kaç ayete bağlı) ve ağırlıklı derece (kaç ortak dizi).
Ayrıca tam-ayet ikizleri ayrı kenar sınıfı.
"""
import json
from collections import defaultdict, Counter

D = json.load(open('defter.json'))
kom = defaultdict(set); agir = Counter()
for r in D:
    k = tuple(r['k'])
    for g, hedefler in r['xref']:
        for h in hedefler:
            kom[k].add(tuple(h)); agir[k] += 1
    for h in r['esit']:
        kom[k].add(tuple(h)); agir[k] += 5      # tam-ayet ikizi ağır kenar

for r in D:
    k = tuple(r['k'])
    r['dugum'] = {'derece': len(kom[k]), 'agirlik': agir[k]}

json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)
json.dump({'%d:%d' % k: sorted('%d:%d' % h for h in v) for k, v in kom.items() if v},
          open('ayet_grafi.json', 'w', encoding='utf-8'), ensure_ascii=False)

n = sum(1 for r in D if r['dugum']['derece'])
e = sum(r['dugum']['derece'] for r in D) // 2
print('graf: %d bağlı ayet, ~%d kenar' % (n, e))
top = sorted(D, key=lambda r: -r['dugum']['derece'])[:15]
print()
print('%-9s %-7s %-8s %s' % ('ayet', 'derece', 'ağırlık', 'n'))
for r in top:
    print('%-9s %-7d %-8d %d' % ('%d:%d' % tuple(r['k']), r['dugum']['derece'], r['dugum']['agirlik'], r['n']))
print()
# sûre bazlı ortalama derece
sd = defaultdict(list)
for r in D: sd[r['k'][0]].append(r['dugum']['derece'])
ort = sorted(((sum(v)/len(v), s, len(v)) for s, v in sd.items() if len(v) >= 20), reverse=True)
print('sûre başına ortalama derece (n>=20 ayet) — en bağlı 8:')
for o, s, n_ in ort[:8]: print('   sûre %3d: %.2f (%d ayet)' % (s, o, n_))
print('en az bağlı 5:')
for o, s, n_ in ort[-5:]: print('   sûre %3d: %.2f (%d ayet)' % (s, o, n_))
