# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 73 (Müzzemmil) blokları için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    # sûre 73 (Müzzemmil) — blok blok eklenir (2026-10-26); korpus geçişleri kok_envanteri ayet_sayisi ile
    # blok 1-10
    ('زمل', "örtünüp bürünen (muzzemmil; 1 ayet)"),
    ('نصف', "yarı (nısf; 7 ayet)"),
    ('بتل', "bütünüyle yönelme, kendini adama (tebettel / tebtîl; 1 ayet)"),
    # blok 11-19
    ('نكل', "ibret olacak ceza, ağır bağ / pranga (nekâl / enkâl / tenkîl; 5 ayet)"),
    ('غصص', "boğazda takılma (ğussa; 1 ayet)"),
    ('كثب', "kum yığını (kesîb; 1 ayet)"),
    ('هيل', "akıp dağılan, savrulan (mehîl; 1 ayet)"),
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
