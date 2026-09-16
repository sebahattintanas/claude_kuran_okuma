# -*- coding: utf-8 -*-
"""uret_blok_betikleri.py — sûre 28'in dokuz blok betiğini üretir.

Blok betikleri ölçüm satırını ELLE taşımaz: olcum_bicim.olcum() ile defterden
üretir. Meal ve matematikçi merceği kasas_metin_1/2'den gelir.
"""
BLOKLAR = [(1, 10), (11, 20), (21, 30), (31, 40), (41, 50),
           (51, 60), (61, 70), (71, 80), (81, 88)]

BASLIK = {
 (1, 10): "sûre 28 (Kasas) birinci blok — mukattaa, açılış formülü ve Mûsâ'nın doğum anlatısı.",
 (11, 20): "sûre 28 ikinci blok — kız kardeş, anneye dönüş, şehirdeki vuruş ve kaçış kararı.",
 (21, 30): "sûre 28 üçüncü blok — Medyen'e çıkış, Şuayb sahnesi, sözleşme ve ateş.",
 (31, 40): "sûre 28 dördüncü blok — asâ ve el, Hârûn talebi, Firavun'un kulesi ve sonu.",
 (41, 50): "sûre 28 beşinci blok — öncüler ve lânet, Kitab'ın verilişi, üç 'değildin' ayeti.",
 (51, 60): "sûre 28 altıncı blok — iki kat ecir, harem, şehirlerin helâki ve dünya süsü.",
 (61, 70): "sûre 28 yedinci blok — vaat karşılaştırması, ortakların sorgusu ve tevhid kapanışı.",
 (71, 80): "sûre 28 sekizinci blok — sermed nakaratı, gece/gündüz çıpası ve Kārûn'un girişi.",
 (81, 88): "sûre 28 dokuzuncu ve SON blok — Kārûn'un sonu, âhiret yurdu ve sûre kapanışı.",
}

SABLON = '''# -*- coding: utf-8 -*-
"""blok_28_%(a)d_%(b)d.py — %(baslik)s

Ölçüm satırı (›) defterden üretilir (olcum_bicim.py); kök anmaları
kok_turkce.json'dan otomatik gloss geçişinden geçer. Yorum (◇) elle yazılır.
"""
import json
import olcum_bicim
import gloss_gecis
from kasas_metin_1 import MEAL as MEAL1, M as M1
from kasas_metin_2 import MEAL as MEAL2, M as M2
MEAL = dict(MEAL1); MEAL.update(MEAL2)
M = dict(M1); M.update(M2)

DIK = json.load(open('blok_dikey_28_%(a)d_%(b)d.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']
# 28:1 — kuran_veri.json metninde besmele GÖMÜLÜ (112 ayetlik bilinen kirlilik);
# defter temiz (n=1). Ham metin burada kırpılır, ölçüm zaten defterden geliyor.
_t = AR[(28, 1)].split()
if len(_t) == 5:            # besmele (4 kelime) + طسم
    AR[(28, 1)] = _t[-1]

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
OM.setdefault('28', {})
for n in range(%(a)d, %(b)d + 1):
    OM['28']["28:%%d" %% n] = {"ar": AR[(28, n)], "meal": MEAL[n],
                             "olcum": olcum_bicim.olcum(28, n),
                             "mercek": M[n],
                             # 28:1'de kök yok → dikey satır da yok (26:1 ile aynı durum)
                             "dikey": DIK.get("28:%%d" %% n, "  · (ayette kök bulunmuyor — dikey satır yok)")}
    # blok kapanış protokolü: kök anmaları otomatik gloss geçişinden geçer
    gloss_gecis.gecir_kayit(OM['28']["28:%%d" %% n])
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 28 →', len([k for k in OM['28'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK.setdefault('28', {})
for n in range(%(a)d, %(b)d + 1):
    MK['28']["28:%%d" %% n] = gloss_gecis.gecir(M[n])
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 28 →', len(MK['28']))
'''

for a, b in BLOKLAR:
    src = SABLON % {'a': a, 'b': b, 'baslik': BASLIK[(a, b)]}
    open('blok_28_%d_%d.py' % (a, b), 'w', encoding='utf-8').write(src)
    print('yazıldı: blok_28_%d_%d.py' % (a, b))
