# -*- coding: utf-8 -*-
"""24_onarim_sinama.py — ONARIM 14 ve 15'in sınama kümeleri.

Protokol maddesi 2: her onarım, OKUMADA BELGELENMİŞ vakalardan kurulu bir kümeyle
sınanır ve sonuç n/n olarak yazılır. Sınama kümeleri okuma kayıtlarından alınır,
onarım yazılırken kurulmaz.
"""
import json

D = json.load(open('defter.json', encoding='utf-8'))
IX = {tuple(r['k']): r for r in D}

# ---------------------------------------------------------------- ONARIM 14
# okuma kayıtlarından: hapaks olarak BELGELENMİŞ ayetler (sûre 28-29) korunmalı,
# ve okumada 'korpusta tek ayette ama hapaks sayılmıyor' diye kaydedilen vakalar
# artık hapaks2 olmalı.
S14 = [
 # (ayet, hapaks2 bekleniyor mu, okuma kaydı)
 ((28, 15), True,  'وكز — sûre 28 ilk hapaksı, blok 2 kaydı'),
 ((28, 23), True,  'ذود — blok 3'),
 ((28, 29), True,  'جذو — blok 3'),
 ((28, 30), True,  'بقع — blok 3'),
 ((28, 34), True,  'ردأ + فصح — çift hapaks, blok 4'),
 ((28, 42), True,  'قبح — blok 5'),
 ((28, 76), True,  'نوأ — blok 8'),
 ((29, 48), True,  'خطط — sûre 29 tek hapaksı'),
 ((29, 41), True,  'عنكب — OKUMADA KAYDEDİLDİ: korpusta tek ayette ama iki token '
                   'olduğu için hapaks SAYILMIYORDU; onarım bunu düzeltmeli'),
 ((29, 40), False, 'dört dar kök var ama hiçbiri tek ayetlik değil — hapaks2 BOŞ kalmalı'),
 ((28, 12), False, 'دلل/كفل/نصح dar ama tek ayetlik değil — okuma "nadirlik yığılması '
                   'ile hapaks ayrı şeyler" diye kaydetmişti'),
 ((28, 15), True,  'tekrar: hapaks korunuyor mu'),
]
print('=== ONARIM 14 SINAMA KÜMESİ ===')
gecen = 0
for k, bekl, not_ in S14:
    var = bool(IX[k]['hapaks2'])
    ok = (var == bekl)
    gecen += ok
    print('  %-8s %-4s beklenen %-5s → %-5s  %s' %
          ('%d:%d' % k, 'OK' if ok else 'HATA', bekl, var, not_))
print('  SONUÇ: %d/%d' % (gecen, len(S14)))

# eski hapaks'ın tamamı korunuyor mu (kaybedilen == 0, ayet düzeyinde)
kayip = [tuple(r['k']) for r in D if r['hapaks'] and not r['hapaks2']]
print('  eski hapaks dolu ama hapaks2 boş: %d  <- sıfır olmalı' % len(kayip))

# ---------------------------------------------------------------- ONARIM 15
S15 = [
 ((29, 40), False, 'فَكُلًّا = "her biri" (ROOT:كلل|LEM:كُلّ) — OKUMADA KAYDEDİLDİ, '
                   'KELLA DÜŞMELİ'),
 ((74, 16), True,  'gerçek كَلَّا — korunmalı'),
 ((74, 32), True,  'gerçek كَلَّا — korunmalı'),
 ((80, 11), True,  'gerçek كَلَّا — korunmalı'),
 ((96, 6),  True,  'gerçek كَلَّا — korunmalı'),
 ((102, 3), True,  'gerçek كَلَّا — korunmalı'),
 ((4, 95),  False, 'كلل kökü var, كَلَّا yok — düşmeli'),
 ((21, 79), False, 'كلل kökü var, كَلَّا yok — düşmeli'),
]
print('\n=== ONARIM 15 SINAMA KÜMESİ ===')
gecen15 = 0
for k, bekl, not_ in S15:
    if k not in IX:
        print('  %-8s ATLANDI (ayet yok)' % ('%d:%d' % k)); continue
    var = 'KELLA' in IX[k]['fig2']
    ok = (var == bekl)
    gecen15 += ok
    print('  %-8s %-4s beklenen %-5s → %-5s  %s' %
          ('%d:%d' % k, 'OK' if ok else 'HATA', bekl, var, not_))
print('  SONUÇ: %d/%d' % (gecen15, len(S15)))

# ---------------------------------------------------------------- düşen alt-kayıtlar
print('\n=== ADAY 926\'NIN İKİ ALT-KAYDI DÜŞTÜ ===')
h1 = sum(1 for r in D if r['hapaks'])
h2 = sum(1 for r in D if r['hapaks2'])
deg = [(tuple(r['k']), r['yildiz'], r['yildiz2']) for r in D if r['yildiz'] != r['yildiz2']]
y0 = [x for x in deg if x[1] == 0]
print('  ÖNGÖRÜ 1: "hapaks ayeti 358 → 379"  ·  GERÇEK: %d → %d' % (h1, h2))
print('     sebep: eklenen 21 kökün dördü, zaten hapaks taşıyan ayetlere düşüyor')
print('  ÖNGÖRÜ 2: "beş yeni ★★★"            ·  GERÇEK: %d ayet yıldız değiştirdi, '
      '%d\'i yıldızsızdan ★★★\'a' % (len(deg), len(y0)))
print('     sebep: 21 ayetin 11\'i zaten başka ölçütten ★★★ idi; kalan 10\'u değişti, '
      'beşi ★ ya da ★★ iken ★★★ oldu')
