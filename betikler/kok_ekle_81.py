# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 81 (Tekvîr) blokları için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    # sûre 81 (Tekvîr) — blok blok eklenir (2026-10-29); korpus geçişleri kok_envanteri ayet_sayisi ile
    # blok 1-10
    ('كدر', "bulanma, dökülüp kararma (inkederet; 1 ayet)"),
    ('وحش', "vahşi hayvan (vuhûş; 1 ayet)"),
    ('وأد', "diri diri gömme (mev'ûde; 1 ayet)"),
    # blok 11-20
    ('كشط', "sıyırıp kaldırma, açma (kuşitat; 1 ayet)"),
    ('خنس', "sinip geri çekilme, gizlenme (xunnes, xannâs; 2 ayet)"),
    ('كنس', "yuvaya çekilip gizlenme (kunnes; 1 ayet)"),
    ('عسعس', "kararıp gelme ya da çekilip gitme (gece için, 'as'as; 1 ayet)"),
    # blok 21-29
    ('ضنن', "esirgeme, kıskanıp saklama (danîn; 1 ayet)"),
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
