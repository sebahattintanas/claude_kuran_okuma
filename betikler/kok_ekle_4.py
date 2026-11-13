# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 4 (Nisâ) blokları için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    # sûre 4 (Nisâ) — blok blok eklenir (2026-11-09); korpus geçişleri kok_envanteri ayet_sayisi ile
    # blok 1-5
    ('حوب', "günah, vebal ('hûb'); 1 ayet"),
    ('عول', "haktan sapma, ağma; geçindirme yükü ('te’ûlu'); 1 ayet"),
    # blok 6-10
    ('بدر', "acele etme, davranma ('bidâr'); 1 ayet"),
    # blok 19-22
    ('فضو', "varma, ulaşma; birbirine geçip kaynaşma ('efdâ'); 1 ayet"),
    # blok 23-24
    ('سفح', "dökme, akıtma ('mesfûh'); iffetsizce ilişki kuran ('musâfih'); 4 ayet"),
    # blok 25-28
    ('خدن', "gizli dost, metres ('ahdân'); 2 ayet"),
    ('ميل', "meyletme, sapma, bir yana kayma ('meyl'); 3 ayet"),
    # blok 40-43
    ('غوط', "çukur, alçak yer ('ğâ'it'); def-i hacetin kinayesi; 2 ayet"),
    # blok 48-52
    ('جبت', "cibt ('el-cibt'); tâğût ile birlikte anılan batıl tapınç nesnesi, anlamı tartışmalı; 1 ayet"),
    # blok 53-57
    ('نضج', "pişme, olgunlaşma ('nadicet'); 1 ayet"),
    # blok 71-75
    ('ثبي', "bölük, ayrı küme ('subât'); 1 ayet"),
    ('بطأ', "ağırdan alma, geri kalma ('le-yubatti'enne'); 1 ayet"),
    # blok 79-83
    ('ذيع', "yayma, duyurma ('ezâ'û'); 1 ayet"),
    ('نبط', "çıkarma, içinden çıkarıp anlama ('yestenbitûnehû'); 1 ayet"),
    # blok 88-90
    ('ركس', "tersine çevirme, eski hâline geri döndürme ('erkesehum'); 2 ayet"),
    # blok 97-101
    ('رغم', "burun sürtme (rağm); gidilecek yer, sığınak ('murâğamen'); 1 ayet"),
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
