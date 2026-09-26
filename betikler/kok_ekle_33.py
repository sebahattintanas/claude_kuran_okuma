# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 33 (Ahzâb) blokları için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    # blok 1-10
    ('جوف',  'iç, oyuk (göğüs boşluğu)'),
    ('سفل',  'alt, aşağı'),
    ('حنجر', 'gırtlak, boğaz'),
    # blok 11-20
    ('قطر',  'yan, çevre (aktâr); erimiş bakır (kıtr)'),
    ('عوق',  'engelleme, alıkoyma'),
    ('هلم',  'haydi, gel'),
    ('شحح',  'cimrilik, hırs'),
    ('سلق',  'dille saldırma, iğneleme'),
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
assert not bulunamadi, "NFC eşleşmesi yok — koşu DURDU"
print("toplam kök:", len(kt))
