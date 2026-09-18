# -*- coding: utf-8 -*-
"""blok_30_31_40.py — sûre 30 dördüncü blok — dinde bölünme, davranış düzenliliği, ribâ ve dört aşamalı döngü.

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

DIK = json.load(open('blok_dikey_30_31_40.json', encoding='utf-8'))
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
for n in range(31, 40 + 1):
    OM['30']["30:%d" % n] = {"ar": AR[(30, n)], "meal": MEAL[n],
                             "olcum": olcum_bicim.olcum(30, n),
                             "mercek": M[n],
                             # 28:1'de kök yok → dikey satır da yok (26:1 ile aynı durum)
                             "dikey": DIK.get("30:%d" % n, "  · (ayette kök bulunmuyor — dikey satır yok)")}
    # blok kapanış protokolü: kök anmaları otomatik gloss geçişinden geçer
    gloss_gecis.gecir_kayit(OM['30']["30:%d" % n])
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 30 →', len([k for k in OM['30'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK.setdefault('30', {})
for n in range(31, 40 + 1):
    MK['30']["30:%d" % n] = gloss_gecis.gecir(M[n])
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 30 →', len(MK['30']))
