# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 55 (Rahmân) blokları için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    # sûre 55 (Rahmân) tümü baştan (2026-10-18); korpus geçişleri kok_envanteri ayet_sayisi ile
    ('أنم', "yaratıklar, enâm (1 token)"),
    ('فني', "fânî olma, yok olup gitme (fân; 1 token)"),
    ('نفذ', "geçip çıkma, delip geçme (nefeze)"),
    ('شوظ', "dumansız alev (şuvâz; 1 token)"),
    ('فنن', "dal, dallar (efnân; 1 token)"),
    ('طمث', "dokunma (lem yatmis)"),
    ('دهم', "koyu yeşil, siyaha çalan (mudhâmmetân; 1 token)"),
    ('نضخ', "fışkırma (naddâhatân; 1 token)"),
    ('خيم', "çadır (hiyâm; 1 token)"),
    ('رفرف', "yastık, döşek (refref; 1 token)"),
    ('عبقر', "işlemeli halı, nadide (abqariyy; 1 token)"),
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
