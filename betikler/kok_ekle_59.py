# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 59 (Haşr) blokları için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    # sûre 59 (Haşr) — blok blok eklenir (2026-10-22); korpus geçişleri kok_envanteri ayet_sayisi ile
    # blok 1-5
    ('خرب', "yıkma, harap etme; yıkıntı (yuhribûn / harâb; 2 ayet)"),
    ('جلو', "yurttan sürülme (celâ'); açığa çıkma, tecelli (tecellâ / cellâ; 5 ayet)"),
    # blok 6-10
    ('وجف', "at / binek koşturma (evcefe); çarpıntı, titreme (vâcife; 2 ayet)"),
    ('دول', "elden ele dolaşma (dûle; nudâvilu, sırayla döndürme; 2 ayet)"),
    ('خصص', "yoksulluk, darlık (hasâsa); seçip ayırma, has kılma (yahtessu / hâssaten; 4 ayet)"),
    # blok 11-17
    ('وبل', "işin kötü sonucu, ağır vebal (vebâl); sağanak (vâbil); ağır (vebîl; 7 ayet)"),
    # blok 18-24
    ('همن', "gözetip koruyan, hâkim (muheymin; 2 ayet)"),
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
