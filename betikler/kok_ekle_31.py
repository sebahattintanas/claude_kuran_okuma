# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 31 blok 1-10, 11-20, 21-30 ve 31-34 için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    ('بثث',  'yayma, saçıp dağıtma; dert'),
    ('عمد',  'direk, sütun; kasıt'),
    ('وقر',  'ağırlık (kulakta), yük; vakar'),
    # blok 11-20
    ('حمر',  'eşek; kızıllık'),
    ('خدد',  'yanak; yarık'),
    ('سبغ',  'bolca verme, tamamlama'),
    ('صخر',  'kaya'),
    ('صعر',  'yüz çevirme (kibirle), yanak eğme'),
    ('فخر',  'övünme, böbürlenme'),
    ('قصد',  'orta yol, itidal; kasıt'),
    # blok 21-30
    ('عرو',  'kulp, tutamak'),
    ('غلظ',  'kalınlık, sertlik'),
    ('قلم',  'kalem'),
    ('وثق',  'sağlam bağ, güven; ahit'),
    # blok 31-34
    ('ختر',  'gaddarlık, ahde vefasızlık'),
    ('غيث',  'yağmur, imdat yağmuru'),
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
print("toplam kök:", len(kt))
