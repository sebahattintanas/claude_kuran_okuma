# -*- coding: utf-8 -*-
"""ONARIM 3b (v2) — esit2. Eşik 0,95.

v1 ARIZASI: yalnız 4-gram bloklama kullanılıyordu; üç kelimelik ayetlerin
4-gram'ı olmadığı için 46 ayet KAYBOLDU (sûre 26'nın nakarat ayetleri dahil).
Onarımın kendi yanlış negatifi — aday 867'nin dersi burada tekrarladı.

v2: (a) tam eşleşmeler iskelet karması ile DOĞRUDAN bulunur (kayıp imkânsız),
    (b) yakın eşleşmeler 3-gram bloklama ile aranır,
    ikisinin birleşimi yazılır.
"""
import json, difflib
from collections import defaultdict

ISK = json.load(open('ayet_iskelet.json', encoding='utf-8'))
NG = json.load(open('ngram_indeks.json', encoding='utf-8'))
DUZ = {k: ''.join(v) for k, v in ISK.items()}
ESIK = 0.85   # üçüncü kademe (aday 890): 0,95 'yakin', 0,85-0,95 'benzer'

# (a) TAM eşleşme — karma ile, bloklamadan bağımsız
grup = defaultdict(list)
for k, v in DUZ.items():
    if v: grup[v].append(k)
cift = {}
for v, ks in grup.items():
    if len(ks) < 2: continue
    for i in range(len(ks)):
        for j in range(i + 1, len(ks)):
            cift[(ks[i], ks[j])] = 1.0

# (b) YAKIN eşleşme — 3-gram bloklama
aday = set()
for g, v in NG.items():
    if len(v) > 60: continue
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            p = (v[i], v[j])
            if p not in cift: aday.add(p)
for a, b in aday:
    x, y = DUZ[a], DUZ[b]
    if not x or not y: continue
    if abs(len(x) - len(y)) / max(len(x), len(y)) > 0.25: continue
    s = difflib.SequenceMatcher(None, x, y).ratio()
    if s >= ESIK: cift[(a, b)] = s

esl = defaultdict(list)
for (a, b), s in cift.items():
    t = 'tam' if s == 1.0 else ('yakin' if s >= 0.95 else 'benzer')
    for p, q in ((a, b), (b, a)):
        ss, aa = q.split(':')
        esl[p].append([int(ss), int(aa), round(s, 4), t])

D = json.load(open('defter.json'))
for r in D:
    k = '%d:%d' % (r['k'][0], r['k'][1])
    r['esit2'] = sorted(esl.get(k, []), key=lambda x: (-x[2], x[0], x[1]))
json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)

eski = {tuple(r['k']) for r in D if r.get('esit')}
yeni = {tuple(r['k']) for r in D if r['esit2']}
tam = sum(1 for r in D for e in r['esit2'] if e[3] == 'tam')
ben = sum(1 for r in D for e in r['esit2'] if e[3] == 'benzer')
yak = sum(1 for r in D for e in r['esit2'] if e[3] == 'yakin')
print('=== ESİT ONARIMI v2 (eşik %.2f) ===' % ESIK)
print('ESKİ: %d ayet dolu' % len(eski))
print('YENİ: %d ayet dolu  (tam %d · yakın %d · benzer %d bağ)' % (len(yeni), tam, yak, ben))
print('kazanılan ayet: %d | KAYBEDİLEN ayet: %d' % (len(yeni - eski), len(eski - yeni)))
assert not (eski - yeni), 'KAYIP VAR: %s' % sorted(eski - yeni)[:10]
print('*** yanlış negatif denetimi: KAYIP YOK ***')
print()
SIN = [('27:80','30:52'),('27:81','30:53'),('1:2','37:182'),('94:5','94:6'),
       ('27:71','10:48'),('27:58','26:173'),('26:108','26:110')]
print('=== SINAMA KÜMESİ ===')
g = 0
for a, b in SIN:
    s_, a_ = b.split(':')
    var = any(e[0] == int(s_) and e[1] == int(a_) for e in next(r for r in D if '%d:%d'%(r['k'][0],r['k'][1]) == a)['esit2'])
    g += var
    print('  %-7s ↔ %-7s  %s' % (a, b, 'GEÇTİ' if var else '**DÜŞTÜ**'))
print('  sınama: %d/%d' % (g, len(SIN)))
