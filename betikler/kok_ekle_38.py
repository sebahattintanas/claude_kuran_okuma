# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 38 (Sâd) blokları için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    # sûre 38 (Sâd) tümü baştan (2026-10-10); baskın lemma sayıldı (morph.txt)
    ('حنث',  'yemini bozma, günah (tahnes, hins)'),
    ('رخو',  'yumuşak, kolay esen (rukhâ\'; rüzgâr)'),
    ('صفن',  'üç ayak üstünde duran asil at (sâfinât)'),
    ('غسل',  'yıkanma, yıkama (iğtisâl, ğasl); yıkanma suyu (muğtesel); irin (ğislîn)'),
    ('قحم',  'dalma, saldırarak girme (iqtihâm, muqtahim)'),
    ('قطط',  'pay, nasip; hesap belgesi (qıtt)'),
    ('كرس',  'taht, kürsü (kursî)'),
    ('لوت',  'değil, artık yok (lâte — olumsuzluk edatı)'),
    ('نوص',  'kaçış, kurtuluş yeri (menâs)'),
    ('هزم',  'bozguna uğratma (hezeme, mehzûm)'),
    ('وتد',  'kazık, direk (evtâd)'),
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
