# -*- coding: utf-8 -*-
"""ONARIM 4 — `nakarat` alanı: AYET düzeyi -> N-GRAM düzeyi.
(aday 844/845/870: sûre 27'de üç ayet-içi nakarat var, alan üçünü de görmüyor;
 sûre 26'da 34 ayet dolu çünkü orada nakarat TAM AYET.)

Yeni tanım: aynı sûrede EN AZ İKİ AYRI AYETTE geçen, en az üç kelimelik
azami (maximal) kelime n-gramı. Her kalıp için tür:
  'tam'    — kalıp ayetin tamamını kaplıyor (eski alanın gördüğü tür)
  'ic'     — ayet içinde, sabit kalıp
Yeni alan: 'nakarat2' — eski dugum.nakarat korunur.
"""
import json
from collections import defaultdict, Counter

ISK = json.load(open('ayet_iskelet.json', encoding='utf-8'))
sure = defaultdict(list)
for k, ws in ISK.items():
    s, a = k.split(':')
    sure[int(s)].append((int(a), ws))

nak = defaultdict(list)
kaliplar = defaultdict(list)
for s, ayetler in sure.items():
    idx = defaultdict(set)
    for a, ws in ayetler:
        for n in range(3, min(len(ws), 25) + 1):
            for i in range(len(ws) - n + 1):
                idx[' '.join(ws[i:i+n])].add(a)
    tekrar = {g: v for g, v in idx.items() if len(v) > 1}
    # azami kalıplar: daha uzun bir kalıp aynı ayet kümesini veriyorsa kısayı at
    azami = {}
    for g, v in sorted(tekrar.items(), key=lambda x: -len(x[0].split())):
        if any(g in h and tekrar[h] >= v for h in azami): continue
        azami[g] = v
    for g, v in azami.items():
        kaliplar[s].append((g, sorted(v)))
        for a in v:
            ws = dict(ayetler)[a]
            tur = 'tam' if g == ' '.join(ws) else 'ic'
            nak['%d:%d' % (s, a)].append([g, len(v), tur])

D = json.load(open('defter.json'))
for r in D:
    k = '%d:%d' % (r['k'][0], r['k'][1])
    r['nakarat2'] = sorted(nak.get(k, []), key=lambda x: (-len(x[0].split()), -x[1]))
json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)

eski = {tuple(r['k']) for r in D if r['dugum']['nakarat']}
yeni = {tuple(r['k']) for r in D if r['nakarat2']}
print('=== NAKARAT ONARIMI ===')
print('ESKİ: %d ayet dolu' % len(eski))
print('YENİ: %d ayet dolu' % len(yeni))
print('kazanılan: %d | KAYBEDİLEN: %d' % (len(yeni - eski), len(eski - yeni)))
if eski - yeni:
    print('KAYIP:', sorted(eski - yeni)[:10])
print('tür dağılımı:', dict(Counter(x[2] for r in D for x in r['nakarat2'])))
print()
for s in (26, 27):
    e = len([r for r in D if r['k'][0] == s and r['dugum']['nakarat']])
    y = len([r for r in D if r['k'][0] == s and r['nakarat2']])
    print('sûre %d: eski %d ayet -> yeni %d ayet | kalıp sayısı %d' % (s, e, y, len(kaliplar[s])))
print()
print('=== SÛRE 27\'NİN KALIPLARI (>=2 ayet, uzunluğa göre) ===')
for g, v in sorted(kaliplar[27], key=lambda x: (-len(x[0].split()), -len(x[1])))[:12]:
    print('  %d ayet  n=%-2d  %-46s %s' % (len(v), len(g.split()), g, v))
json.dump({str(s): kaliplar[s] for s in kaliplar}, open('nakarat_kaliplari.json', 'w', encoding='utf-8'), ensure_ascii=False)
