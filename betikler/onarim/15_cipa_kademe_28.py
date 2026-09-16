# -*- coding: utf-8 -*-
"""15_cipa_kademe_28.py — P0 #6, ikinci sûre verisi.

Sûre 28'in olgu içeren ayetleri, 14_cipa_tanimi.py'deki L0-L4 tanımına ve
sûre 27'nin EMSALLERİNE göre yerleştirilir. Emsal bağı açıkça yazılır:
her satır, sûre 27'de hangi ayetle aynı kademeye konduğunu taşır.
"""
import json
D = json.load(open('defter.json')); DD = {tuple(r['k']): r for r in D}
T27 = {x['ayet']: x for x in json.load(open('cipa_kademe_27.json', encoding='utf-8'))}

# ayet, kademe, olgu_mu, emsal (sûre 27'den), gerekçe
TABLO = [
 (4,  'L1', False, '27:17', 'halk bölüklere ayrılıyor — sınıflama var ama olgu değil, anlatı'),
 (7,  'L0', True,  '27:24', 'ٱلْيَمّ — su kütlesi adlandırılıyor, başka bir şey söylenmiyor'),
 (10, 'L2', False, '27:62', 'kalbe bağ vurulmasaydı açığa vuracaktı — karşı-olgusal nedensellik, ama olgu değil'),
 (14, 'L1', True,  '27:40', 'أَشُدّ + ٱسْتَوَىٰ — gelişim eşiği iki terimle adlandırılıyor, ölçü yok'),
 (23, 'L0', True,  '27:20', 'Medyen suyu, sulanan sürüler — adlandırma'),
 (29, 'L0', True,  '27:82', 'Tûr yanında ateş — adlandırma'),
 (30, 'L0', True,  '27:24', 'vadi, sağ kıyı, ağaç — üç konum adlandırılıyor'),
 (31, 'L1', True,  '27:39', 'asâ yılan gibi kıvranıyor — benzetme var, görünüş/durum ayrımı YOK'),
 (32, 'L1', True,  '27:25', 'el kusursuz bembeyaz çıkıyor — süreç + nitelik, mekanizma yok'),
 (57, 'L1', True,  '27:61', 'her şeyin ürünleri güvenli hareme toplanıyor — yapı var, ilişki yok'),
 (71, 'L2', True,  '27:60', 'gece sürekli kılınsa kim ışık getirir — karşı-olgusal nedensellik + YETİ SINIRI'),
 (72, 'L2', True,  '27:60', 'gündüz sürekli kılınsa kim gece getirir — karşı-olgusal nedensellik + YETİ SINIRI'),
 (73, 'L2', True,  '27:86', 'gece dinlenme, gündüz lütuf arama İÇİN — işlevsel nedensellik'),
 (76, 'L1', True,  '27:40', 'anahtarlar güçlü topluluğa ağır geliyor — insan-topluluğu ölçüsü, birim değil'),
 (81, 'L0', True,  '27:87', 'yer yarılıp yutuyor — adlandırma'),
]

KAD = {'L0': 0, 'L1': 1, 'L2': 2, 'L3': 3, 'L4': 4}

print('=== SÛRE 28 — ÇIPA KADEME TABLOSU (emsal bağlı) ===')
print('%-7s %-4s %-6s %-7s %-7s %s' % ('ayet', 'kad', 'olgu', 'yıldız', 'emsal', 'gerekçe'))
for a, k, olgu, ems, g in TABLO:
    y = DD[(28, a)].get('yildiz', 0)
    print('28:%-4d %-4s %-6s %-7s %-7s %s'
          % (a, k, 'evet' if olgu else 'HAYIR', '★' * y if y else '—', ems, g))

import collections
print()
print('kademe dağılımı :', dict(collections.Counter(k for _, k, _, _, _ in TABLO)))
print('olgu olan       :', sum(1 for _, _, o, _, _ in TABLO if o), '/', len(TABLO))

# --- iki sûrenin birleşik tablosu
BIRLESIK = []
for ay, x in T27.items():
    n = int(ay.split(':')[1])
    # sûre 27'de 'olgu değil' notu gerekçede açıkça yazılı olanlar
    olgu = 'olgu değil' not in x['gerekce']
    BIRLESIK.append((ay, x['kademe'], olgu, x['yildiz'], x['gerekce']))
for a, k, olgu, ems, g in TABLO:
    BIRLESIK.append(('28:%d' % a, k, olgu, DD[(28, a)].get('yildiz', 0), g))

print()
print('=== İKİ SÛRENİN BİRLEŞİK TABLOSU (%d ayet) ===' % len(BIRLESIK))
for esik in ('L2', 'L3', 'L4'):
    e = KAD[esik]
    ic = [x for x in BIRLESIK if KAD[x[1]] >= e]
    olgu = [x for x in ic if x[2]]
    print('  eşik %s+ : %2d ayet · bunlardan olgu olan %2d · olgu OLMAYAN %d'
          % (esik, len(ic), len(olgu), len(ic) - len(olgu)))
    if ic:
        print('            %s' % ', '.join('%s(%s%s)' % (x[0], x[1], '' if x[2] else ',olgu değil') for x in ic))

print()
print('=== SEÇİLEN ÖLÇÜT: çıpa = (L2+) VE (olgu = evet) ===')
CIPA = [x for x in BIRLESIK if KAD[x[1]] >= 2 and x[2]]
for x in CIPA:
    print('  %-7s %-4s %-6s %s' % (x[0], x[1], '★' * x[3] if x[3] else '—', x[4]))
yc = sum(1 for x in CIPA if x[3] > 0)
print('  çıpa: %d ayet · yıldızlı %d (%%%.1f)' % (len(CIPA), yc, 100 * yc / len(CIPA)))

t27 = sum(1 for a in range(1, 94) if DD[(27, a)].get('yildiz', 0) > 0)
t28 = sum(1 for a in range(1, 89) if DD[(28, a)].get('yildiz', 0) > 0)
print('  karşılaştırma tabanı: sûre 27 %%%.1f · sûre 28 %%%.1f · ikisi birlikte %%%.1f'
      % (100 * t27 / 93, 100 * t28 / 88, 100 * (t27 + t28) / 181))

json.dump([{'ayet': x[0], 'kademe': x[1], 'olgu': x[2], 'yildiz': x[3], 'gerekce': x[4]}
           for x in BIRLESIK],
          open('cipa_kademe_27_28.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('\ncipa_kademe_27_28.json yazıldı (%d kayıt)' % len(BIRLESIK))
