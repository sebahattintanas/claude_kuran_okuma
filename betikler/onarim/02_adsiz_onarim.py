# -*- coding: utf-8 -*-
"""ONARIM 1b — adsız aktör alanı: kök eşleşmesi → LEMMA eşleşmesi,
ve BELİRLİLİK KOŞULU KALDIRILDI.

Eski kural (aktor2.py):
    elif 'INDEF' in p and s['pos'] == 'N':
        if ROOT in ADSIZ_KOK: adsiz.append(...)

İki arıza (aday 802 / 833):
  (a) KÖK düzeyinde eşleşme  -> yanlış pozitif: مَرِيئ, نُفُور, رِجْل, طُوفان ...
  (b) INDEF koşulu           -> yanlış negatif: izâfetli/belirli bütün aktörler
      (Lût'un karısı, Firavun'un karısı, İmrân'ın karısı ...)
  (c) ek olarak: ADSIZ_KOK'un 'karye' anahtarı YANLIŞ YAZILMIŞ (ى/ي) ve
      korpusta hiç eşleşmiyordu -> 57 token ölü.

Yeni kural: lemma, adsiz_lemma_listesi.json'daki SEÇİLİ İNDEKSLERDE mi?
Hiçbir Arapça dizge elle yazılmadı; seçim indeks üzerinden.

Alan ESKİSİNİN YERİNE GEÇMEZ: yeni alan adı 'adsiz2'. Eski 'adsiz' korunur ki
sûre 27 okumasının ölçümleri yeniden üretilebilir kalsın.
"""
import re, json
from collections import defaultdict, Counter

L = json.load(open('adsiz_lemma_listesi.json', encoding='utf-8'))
SEC = {
    'imrae': [14],            # امْرَأَت  — dişil kişi
    'mer':   [15, 16, 17, 18],# امْرِئ / مَرْء / امْرَأ / امْرُؤٌا — eril kişi (YENİ etiket)
    'racül': [26, 27, 29],
    'ferîk': [0, 11],
    'nefer': [23, 25],
    'tâife': [30],
    'karye': [20],
}
DISLANAN = sorted(set(r['i'] for r in L if r['pos'] == 'N') -
                  set(i for v in SEC.values() for i in v))
LEMMA_ET = {}
for et, idx in SEC.items():
    for i in idx:
        assert L[i]['pos'] == 'N', 'fiil seçilemez: %d' % i
        LEMMA_ET[L[i]['lemma']] = et

tok = defaultdict(list)
for ln in open('morph.txt', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 4: continue
    loc = p[0].split(':')
    if len(loc) == 5: loc = loc[1:]
    if len(loc) != 4: continue
    tok[(int(loc[0]), int(loc[1]))].append({'w': int(loc[2]), 'pos': p[2], 'f': p[3]})

def lem(f):
    m = re.search(r'LEM:([^|]+)', f); return m.group(1) if m else ''

D = json.load(open('defter.json'))
for r in D:
    S = tok.get((r['k'][0], r['k'][1]), [])
    yeni = []
    for s in S:
        if s['pos'] != 'N': continue
        et = LEMMA_ET.get(lem(s['f']))
        if et: yeni.append([s['w'], et])
    r['adsiz2'] = yeni
json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)

eski_ayet = {tuple(r['k']) for r in D if r['adsiz']}
yeni_ayet = {tuple(r['k']) for r in D if r['adsiz2']}
eski_tok = sum(len(r['adsiz']) for r in D)
yeni_tok = sum(len(r['adsiz2']) for r in D)

print('=== ADSIZ AKTÖR ONARIMI ===')
print('ESKİ: %4d token / %4d ayet' % (eski_tok, len(eski_ayet)))
print('YENİ: %4d token / %4d ayet' % (yeni_tok, len(yeni_ayet)))
print()
print('yalnız eskide (düşen, yani yanlış pozitif adayı): %d ayet' % len(eski_ayet - yeni_ayet))
print('yalnız yenide (kazanılan, yani yanlış negatif idi): %d ayet' % len(yeni_ayet - eski_ayet))
print('ortak: %d ayet' % len(eski_ayet & yeni_ayet))
print()
print('DIŞLANAN isim lemmaları (yanlış pozitif kaynağı), indeks ve token:')
for i in DISLANAN:
    print('   %3d %-8s n=%-4d' % (i, L[i]['capa_etiket'], L[i]['n']))
print('   dışlanan toplam token: %d' % sum(L[i]['n'] for i in DISLANAN))
print()
print('yeni etiket dağılımı:', dict(Counter(x[1] for r in D for x in r['adsiz2']).most_common()))
print('eski etiket dağılımı:', dict(Counter(x[1] for r in D for x in r['adsiz']).most_common()))
