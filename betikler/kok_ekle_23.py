# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 23 blok 1-20 için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    ('سلل',  'süzülüp çıkan öz, sülâle'),
    ('كسو',  'giydirme, örtü giydirme'),
    ('فكه',  'meyve; şakalaşma'),
    ('دهن',  'yağ; yağ gibi yumuşama, müdâhene'),
    ('صبغ',  'boya; katık'),
    ('بقر',  'sığır, inek'),
    ('سنبل', 'başak'),
    ('عجف',  'cılız, zayıf'),
    ('لوم',  'kınama, levm'),
    ('وري',  'arka, öte; gizleme'),
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
