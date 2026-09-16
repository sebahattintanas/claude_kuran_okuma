# -*- coding: utf-8 -*-
"""23_fig_kella_onarim.py — ONARIM 15 (P0 #11, aday 927).

ARIZA: `fig` alanının KELLA etiketi `كَلَّا` edatını yüzey biçimiyle arıyor ve
`كُلّ` (her) ile karıştırıyor. 29:40'ın ilk kelimesi فَكُلًّا ve morfolojisi net:
ROOT:كلل | LEM:كُلّ — yani 'her biri'. Alan yine de KELLA yazıyor.

ONARIM: yeni alan `fig2` — `fig`in tamamı, KELLA ölçütü morfolojiye bağlanmış
hâliyle: ayet `LEM:كَلّا` taşıyorsa KELLA, taşımıyorsa etiket düşer.
Eski `fig` alanı KORUNUR.

kaybedilen == 0 SAVI: KELLA dışındaki bütün etiketler aynen taşınır ve gerçek
KELLA'ların hiçbiri düşmez (yanlış negatif sıfır).
"""
import json, collections

KELLA_LEM = 'LEM:\u0643\u064e\u0644\u0651\u0627'      # LEM:كَلّا — korpus lemma biçimi

D = json.load(open('defter.json', encoding='utf-8'))

gercek = set()
for ln in open('morph.txt', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 4:
        continue
    loc = p[0].split(':')
    if len(loc) == 5:
        loc = loc[1:]
    if len(loc) != 4:
        continue
    if KELLA_LEM in p[3]:
        gercek.add((int(loc[0]), int(loc[1])))

eski_kella = {tuple(r['k']) for r in D if 'KELLA' in r['fig']}

print('=== ONARIM 15 — fig KELLA etiketi ===')
print('eski ölçüt (yüzey)   : %d ayet' % len(eski_kella))
print('morfolojide LEM:كَلّا : %d ayet' % len(gercek))
print('YANLIŞ POZİTİF       : %d ayet (%%%.0f)'
      % (len(eski_kella - gercek), 100 * len(eski_kella - gercek) / len(eski_kella)))
print('YANLIŞ NEGATİF       : %d  <- sıfır olmalı' % len(gercek - eski_kella))
assert not (gercek - eski_kella), 'yanlış negatif != 0 — teşhis yanlış'

print('\ndüşen etiketler:')
for k in sorted(eski_kella - gercek):
    print('   %d:%d' % k)

# --- fig2 yaz
dus = 0
for r in D:
    k = tuple(r['k'])
    f2 = [x for x in r['fig'] if x != 'KELLA']
    if 'KELLA' in r['fig'] and k in gercek:
        f2.append('KELLA')
    elif 'KELLA' in r['fig']:
        dus += 1
    r['fig2'] = sorted(f2)

# kaybedilen denetimi: KELLA dışı etiketler birebir korundu mu
kayip = [tuple(r['k']) for r in D
         if sorted(x for x in r['fig'] if x != 'KELLA') != sorted(x for x in r['fig2'] if x != 'KELLA')]
print('\nKELLA dışı etiketlerde KAYBEDİLEN: %d  <- sıfır olmalı' % len(kayip))
assert not kayip

e = collections.Counter(x for r in D for x in r['fig'])
y = collections.Counter(x for r in D for x in r['fig2'])
print('\netiket dağılımı  eski → yeni')
for t in sorted(set(e) | set(y)):
    ok = '  ← düzeltildi' if e[t] != y[t] else ''
    print('   %-8s %4d → %4d%s' % (t, e[t], y[t], ok))

json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('\ndefter.json: fig2 yazıldı (%d ayette KELLA düştü, %d alan)' % (dus, len(D[0])))
