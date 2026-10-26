# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 68 (Kalem) blokları için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    # sûre 68 (Kalem) — blok blok eklenir (2026-10-25); korpus geçişleri kok_envanteri ayet_sayisi ile
    # blok 1-10: eksik kök yok
    # blok 11-20
    ('نمم', "söz taşıma, koğuculuk (nemîm; 1 ayet)"),
    ('زنم', "soysuz, sonradan katılmış (zenîm; 1 ayet)"),
    ('خرطم', "hortum, burun (hurtûm; 1 ayet)"),
    ('صرم', "kesip devşirme (sarama); kesilmiş, kararmış (sarîm) (3 ayet)"),
    # blok 21-30
    ('حرد', "kasıt, kararlılık; engelleme (hard; 1 ayet)"),
    ('وسط', "orta, aradaki; en makul (evsat, vasat; 5 ayet)"),
    # blok 31-41: eksik kök yok
    # blok 42-52: eksik kök yok
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
