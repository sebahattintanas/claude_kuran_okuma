# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 35 (Fâtır) blokları için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    # blok 1-10
    ('صعد',  "toprak yüzeyi, yer (sa'îd); yükselme, çıkma (sa'ide, yas'adu); zorlu yokuş, sarp çıkış (sa'ûd); dik tırmanma (yassa''adu)"),
    # blok 11-20
    ('سوغ',  "boğazdan kolay geçen, içimi rahat (sâiğ); yutabilme (esâğa)"),
    ('طرو',  'taze, yumuşak (tarî)'),
    ('مخر',  'suyu yararak giden (gemiler) (mevâhir)'),
    ('قطمر', 'hurma çekirdeği zarı, en ince şey (kıtmîr)'),
    # blok 41-45
    ('زول',  "yerinden kayma, ayrılma, son bulma (zâle); yok olma, sona erme (zevâl)"),
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
