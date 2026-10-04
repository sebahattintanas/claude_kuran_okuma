# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 36 (Yâsîn) blokları için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    # blok 1-10
    ('ذقن',  'çeneler (ezkân)'),
    ('قمح',  'başı yukarı kalkık, kıpırdayamaz hâlde (muqmah)'),
    # blok 31-40
    ('سلخ',  'sıyrılma, soyulup çıkma (inselaha); sıyırıp çıkarma (neslahu)'),
    ('عرجن', 'kurumuş hurma salkımı sapı (urcûn)'),
    # blok 51-60
    ('جدث',  'kabirler (ecdâs)'),
    ('رقد',  'uyku, uykudakiler (rukûd); uyku yeri (merqad)'),
    ('شغل',  'meşguliyet, iş (şuğul); meşgul etme (şeğalet)'),
    ('أرك',  'süslü koltuklar, tahtlar (erâik)'),
    # blok 61-70
    ('طمس',  'silme, silinip yok edilme (tumiset)'),
    ('مسخ',  'şeklini bozup başka hâle çevirme (mesh)'),
    ('مضي',  'geçip gitme, sürüp gitme (mezâ); ileri gidiş (muziyy)'),
    # blok 71-83
    ('رمم',  'çürümüş, ufalanmış kemik (ramîm)'),
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
