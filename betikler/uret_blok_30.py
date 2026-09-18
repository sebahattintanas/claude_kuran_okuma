# -*- coding: utf-8 -*-
"""uret_blok_30.py — sûre 30'un altı blok betiğini üretir.

Blok betikleri ölçüm satırını ELLE taşımaz: olcum_bicim.olcum() ile defterden
üretir. Meal ve matematikçi merceği rum_metin_1/2'den gelir.
"""
BLOKLAR = [(1, 10), (11, 20), (21, 30), (31, 40), (41, 50), (51, 60)]

BASLIK = {
 (1, 10): "sûre 30 (Rûm) birinci blok — Rum yenilgisi, ölçülü öngörü ve tarihe bakış.",
 (11, 20): "sûre 30 ikinci blok — yaratma döngüsü, vakitler ve 'âyetlerinden biri de' dizisinin açılışı.",
 (21, 30): "sûre 30 üçüncü blok — âyetler dizisinin gövdesi: eşler, çeşitlilik, uyku, şimşek, fıtrat.",
 (31, 40): "sûre 30 dördüncü blok — dinde bölünme, davranış düzenliliği, ribâ ve dört aşamalı döngü.",
 (41, 50): "sûre 30 beşinci blok — karada ve denizde bozulma, rüzgârlar ve yağmurun mekanizması.",
 (51, 60): "sûre 30 altıncı ve SON blok — sararan ekin, sağırlık, ömür döngüsü ve sûre kapanışı.",
}

SABLON = '''# -*- coding: utf-8 -*-
"""blok_30_%(a)d_%(b)d.py — %(baslik)s

Ölçüm satırı (›) defterden üretilir (olcum_bicim.py); kök anmaları
kok_turkce.json'dan otomatik gloss geçişinden geçer. Yorum (◇) elle yazılır.
"""
import json
import olcum_bicim
import gloss_gecis
from rum_metin_1 import MEAL as MEAL1, M as M1
from rum_metin_2 import MEAL as MEAL2, M as M2
MEAL = dict(MEAL1); MEAL.update(MEAL2)
M = dict(M1); M.update(M2)

DIK = json.load(open('blok_dikey_30_%(a)d_%(b)d.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']
# 28:1 — kuran_veri.json metninde besmele GÖMÜLÜ (112 ayetlik bilinen kirlilik);
# defter temiz (n=1). Ham metin burada kırpılır, ölçüm zaten defterden geliyor.
_t = AR[(30, 1)].split()
if len(_t) == 5:            # besmele (4 kelime) + الم
    AR[(30, 1)] = _t[-1]

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
OM.setdefault('30', {})
for n in range(%(a)d, %(b)d + 1):
    OM['30']["30:%%d" %% n] = {"ar": AR[(30, n)], "meal": MEAL[n],
                             "olcum": olcum_bicim.olcum(30, n),
                             "mercek": M[n],
                             # 28:1'de kök yok → dikey satır da yok (26:1 ile aynı durum)
                             "dikey": DIK.get("30:%%d" %% n, "  · (ayette kök bulunmuyor — dikey satır yok)")}
    # blok kapanış protokolü: kök anmaları otomatik gloss geçişinden geçer
    gloss_gecis.gecir_kayit(OM['30']["30:%%d" %% n])
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 30 →', len([k for k in OM['30'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK.setdefault('30', {})
for n in range(%(a)d, %(b)d + 1):
    MK['30']["30:%%d" %% n] = gloss_gecis.gecir(M[n])
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 30 →', len(MK['30']))
'''

for a, b in BLOKLAR:
    src = SABLON % {'a': a, 'b': b, 'baslik': BASLIK[(a, b)]}
    open('blok_30_%d_%d.py' % (a, b), 'w', encoding='utf-8').write(src)
    print('yazıldı: blok_30_%d_%d.py' % (a, b))
