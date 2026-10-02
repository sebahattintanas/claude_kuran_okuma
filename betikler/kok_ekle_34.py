# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 34 (Sebe') blokları için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    # blok 1-10
    ('عزب',  "uzak kalma, gizli kalma (ya'zubu)"),
    ('سرد',  'örme, halka halka dizme (zırh örgüsü)'),
    # blok 11-20
    ('حرب',  'savaş (harb); mihrap, yüksek oda, mabet (mihrâb); savaşma (hâreb)'),
    ('جفن',  'büyük çanak, havuz gibi kap (cifân)'),
    ('نسأ',  "değnek, asa (minse'e); erteleme (nesî')"),
    ('شمل',  'sol, sol yan (şimâl); kapsama, içine alma (iştemele)'),
    ('عرم',  'şiddetli sel, bent seli (arim)'),
    ('خمط',  'acı, buruk meyve (hamt)'),
    ('أثل',  'ılgın ağacı (esl)'),
    ('سدر',  'sedir, arak ağacı (sidr, sidre)'),
    ('سفر',  'yolculuk (sefer); kitaplar (esfâr); aydınlanma (esfera); yazıcılar (sefere)'),
    # blok 31-40
    ('غلل',  'kin (gıll); boyunduruk, zincir (ağlâl); hıyanet, emanete el uzatma (galle)'),
    # blok 51-54
    ('فوت',  'elden kaçma, kaçıp kurtulma (fâte, fevt); uyumsuzluk (tefâvüt)'),
    ('نوش',  'uzanıp alma, erişme (tenâvüş)'),
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
