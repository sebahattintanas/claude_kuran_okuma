# -*- coding: utf-8 -*-
"""blok_32_1_10.py — sûre 32 (Secde) birinci blok — yaratılış, ölçü ve insanın çamurdan başlayan sırası.

Ölçüm satırı (›) defterden üretilir (olcum_bicim.py); kök anmaları
kok_turkce.json'dan otomatik gloss geçişinden geçer. Yorum (◇) elle yazılır.
"""
import json
import olcum_bicim
import gloss_gecis
from secde_metin_1 import MEAL as MEAL1, M as M1
from secde_metin_2 import MEAL as MEAL2, M as M2
MEAL = dict(MEAL1); M = dict(M1)
MEAL.update(MEAL2); M.update(M2)

DIK = json.load(open('blok_dikey_32_1_10.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']
# 28:1 — kuran_veri.json metninde besmele GÖMÜLÜ (112 ayetlik bilinen kirlilik);
# defter temiz (n=1). Ham metin burada kırpılır, ölçüm zaten defterden geliyor.
_t = AR[(32, 1)].split()
if len(_t) == 5:            # besmele (4 kelime) + الم
    AR[(32, 1)] = _t[-1]

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
OM.setdefault('32', {})
for n in range(1, 10 + 1):
    OM['32']["32:%d" % n] = {"ar": AR[(32, n)], "meal": MEAL[n],
                             "olcum": olcum_bicim.olcum(32, n),
                             "mercek": M[n],
                             # 28:1'de kök yok → dikey satır da yok (26:1 ile aynı durum)
                             "dikey": DIK.get("32:%d" % n, "  · (ayette kök bulunmuyor — dikey satır yok)")}
    # blok kapanış protokolü: kök anmaları otomatik gloss geçişinden geçer
    gloss_gecis.gecir_kayit(OM['32']["32:%d" % n])
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 32 →', len([k for k in OM['32'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK.setdefault('32', {})
for n in range(1, 10 + 1):
    MK['32']["32:%d" % n] = gloss_gecis.gecir(M[n])
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 32 →', len(MK['32']))
