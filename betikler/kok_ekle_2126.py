# -*- coding: utf-8 -*-
"""kok_turkce.json'a yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json (korpustan türetilmiş)
içinden NFC eşlemesiyle bulunup KOPYALANIR.
"""
import json, unicodedata, io

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

# arama dizgisi -> Türkçe karşılık.  Arama dizgisi anahtar DEĞİL; yalnız arama.
ISTEK = [
    ('برهن', 'burhan, kesin delil'),
    ('رتق',  'bitişik olma, ratk'),
    ('شفق',  'şafak; işfak, içi titreyerek korkma'),
    ('فتق',  'ayırma, yarma (fatk)'),
    ('ملق',  'yoksulluk korkusu, imlâk'),
    ('نشر',  'yayma, açma; diriltme'),
    ('نيل',  'erişme, nail olma'),
    ('هات',  'getirin (getirme emri)'),
    ('أثم',  'günah, ism'),
    ('بهت',  'şaşkına çevirme; bühtan'),
    ('سقف',  'tavan, çatı'),
    ('شحن',  'yükleme, doldurma'),
    ('ظهر',  'sırt; zuhur, açığa çıkma'),
    ('فجج',  'geniş yol, dağ geçidi (fecc)'),
    ('كفف',  'alıkoyma; avuç'),
    ('ميد',  'sarsılma, yalpalama'),
]

def nfc(s): return unicodedata.normalize('NFC', s)
korpus = {nfc(k): k for k in env}        # korpus formu

eklendi, bulunamadi = [], []
for ara, tr in ISTEK:
    k = korpus.get(nfc(ara))
    if k is None:
        bulunamadi.append(ara); continue
    if k in kt:
        continue
    kt[k] = tr                            # ANAHTAR korpustan kopyalandı
    eklendi.append((k, tr))

json.dump(kt, open('kok_turkce.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1, sort_keys=True)
print("eklenen:", len(eklendi))
for k, v in eklendi: print("  ", k, "->", v)
print("bulunamayan:", bulunamadi)
print("toplam kök:", len(kt))
