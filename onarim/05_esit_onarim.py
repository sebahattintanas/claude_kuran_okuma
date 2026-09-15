# -*- coding: utf-8 -*-
"""ONARIM 3 — `esit` alanı: TAM DİZGE eşleşmesi -> YAKIN eşleşme.
(aday 854: 27:80 ↔ 30:52 tek bağlaç harfi farkla kaçıyordu;
 aday 869: 27:81 ↔ 30:53 kelime İÇİNDE tek harf farkla kaçıyordu.)

Yöntem: n-gram bloklama ile aday çiftler, sonra iskelet üzerinde
karakter benzerliği (difflib). Eşik taranarak seçildi.
Yeni alan: 'esit2' — eski 'esit' korunur.
"""
import json, difflib
from collections import defaultdict

ISK = json.load(open('ayet_iskelet.json', encoding='utf-8'))
NG = json.load(open('ngram_indeks.json', encoding='utf-8'))
DUZ = {k: ''.join(v) for k, v in ISK.items()}

# --- bloklama: en az bir 4-gram paylaşan ayet çiftleri
aday = set()
for g, v in NG.items():
    if len(g.split()) < 4: continue
    if len(v) > 60: continue          # besmele gibi çok yayılan kalıplar atlanır
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            aday.add((v[i], v[j]))
print('aday çift (4-gram bloklama): %d' % len(aday))

def benzer(a, b):
    x, y = DUZ[a], DUZ[b]
    if not x or not y: return 0.0
    if abs(len(x) - len(y)) / max(len(x), len(y)) > 0.25: return 0.0
    return difflib.SequenceMatcher(None, x, y).ratio()

skor = {}
for a, b in aday:
    s = benzer(a, b)
    if s >= 0.80: skor[(a, b)] = s
print('benzerlik >= 0,80 olan çift: %d' % len(skor))

print()
print('=== EŞİK TARAMASI ===')
for esik in (0.80, 0.85, 0.90, 0.92, 0.95, 0.98, 1.00):
    n = sum(1 for s in skor.values() if s >= esik)
    ay = len({x for (a, b), s in skor.items() if s >= esik for x in (a, b)})
    print('  eşik %.2f -> %5d çift / %4d ayet' % (esik, n, ay))

# sınama vakaları eşik seçimi için
SIN = [('27:80', '30:52'), ('27:81', '30:53'), ('1:2', '37:182'), ('94:5', '94:6'),
       ('27:71', '10:48'), ('27:58', '26:173')]
print()
print('=== SINAMA ÇİFTLERİNİN BENZERLİĞİ ===')
for a, b in SIN:
    print('  %-7s ↔ %-7s  benzerlik=%.4f' % (a, b, benzer(a, b)))

print()
print('=== EŞİK 0,95 ile TAM EŞLEŞME ARASINDAKİ 34 ÇİFT (kazanılanlar) ===')
yeni = sorted([(s, a, b) for (a, b), s in skor.items() if 0.95 <= s < 1.0], reverse=True)
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s_ in veri['sureler']:
    for a_ in s_['ayetler']: AR['%d:%d' % (s_['no'], a_['no'])] = a_['ar']
for s, a, b in yeni:
    print('  %.4f  %-7s ↔ %-7s' % (s, a, b))
    print('        %s' % AR[a][:70])
    print('        %s' % AR[b][:70])
