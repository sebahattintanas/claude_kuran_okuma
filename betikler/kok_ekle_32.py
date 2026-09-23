# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 32 blok 1-10, 11-20 ve 21-30 için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    ('جدد',  'yenilik, yeni olma'),
    ('مهن',  'hor görülme, değersizlik'),
    # blok 11-20
    ('جفو',  'uzaklaşma, ayrılma (yataktan)'),
    ('ضجع',  'yatak, uzanma yeri'),
    # blok 21-30
    ('جرز',  'kurak, bitkisiz (yer)'),
]

def nfc(s): return unicodedata.normalize('NFC', s)
korpus = {nfc(k): k for k in env}

eklendi, bulunamadi = [], []
for ara, tr in ISTEK:
    k = korpus.get(nfc(ara))
    if k is None:
        bulunamadi.append(ara); continue
    if k in kt: continue
    kt[k] = tr
    eklendi.append((k, tr))

json.dump(kt, open('kok_turkce.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1, sort_keys=True)
print("eklenen:", len(eklendi))
for k, v in eklendi: print("  ", k, "->", v)
print("bulunamayan:", bulunamadi)
print("toplam kök:", len(kt))
