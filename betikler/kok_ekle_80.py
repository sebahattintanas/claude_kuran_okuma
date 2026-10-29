# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 80 ('Abese) blokları için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    # sûre 80 ('Abese) — blok blok eklenir (2026-10-29); korpus geçişleri kok_envanteri ayet_sayisi ile
    # blok 1-10
    ('صدي', "yönelme, ilgilenme (tesaddâ); el çırpma, ıslık (tasdiye) (2 ayet)"),
    # blok 21-30
    ('قضب', "yaş yem, yonca, biçilip yeniden biten ot (qadb; 1 ayet)"),
    # blok 31-42
    ('أبب', "çayır, otlak, hayvan otu (ebb; 1 ayet)"),
    ('صخخ', "kulakları sağır eden çığlık, büyük ses (sâxxa; 1 ayet)"),
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
