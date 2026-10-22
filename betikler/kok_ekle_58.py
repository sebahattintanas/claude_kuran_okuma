# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 58 (Mücâdele) blokları için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    # sûre 58 (Mücâdele) — blok blok eklenir (2026-10-21); korpus geçişleri kok_envanteri ayet_sayisi ile
    # blok 5-7
    ('كبت', "kahredip alçaltma, yüzüstü çökertme (kubitû / yekbit; 2 ayet)"),
    # blok 11-13
    ('فسح', "yer açma, genişletme (tefessahû / fefsehû / yefsah; 1 ayet)"),
    ('جلس', "oturma; meclis, oturulan yer (mecâlis; 1 ayet)"),
    ('نشز', "kalkma, yükseğe kaldırma; geçimsizlik (unşuzû / nunşiz / nuşûz; 4 ayet)"),
    # blok 19-22
    ('حوذ', "ele geçirip kuşatma, hâkim olma (istahveze; 2 ayet)"),
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
