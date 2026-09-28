# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 33 (Ahzâb) blokları için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    # blok 1-10
    ('جوف',  'iç, oyuk (göğüs boşluğu)'),
    ('سفل',  'alt, aşağı'),
    ('حنجر', 'gırtlak, boğaz'),
    # blok 11-20
    ('قطر',  'yan, çevre (aktâr); erimiş bakır (kıtr)'),
    ('عوق',  'engelleme, alıkoyma'),
    ('هلم',  'haydi, gel'),
    ('شحح',  'cimrilik, hırs'),
    ('سلق',  'dille saldırma, iğneleme'),
    # blok 21-30
    ('أسو',  'örnek (üsve); kederlenme (te\'se)'),
    ('نحب',  'adak, ahit (nahb); ömrün sonu'),
    ('صيص',  'kale, sığınak (sayâsî)'),
    ('أسر',  'esir alma, bağlama; yaratılış bağı (esr)'),
    # blok 31-40
    ('صوم',  'oruç (savm, sıyâm)'),
    ('ختم',  'mühürleme; son (hâtem, hitâm)'),
    ('حمأ',  'kara balçık (hame\')'),        # dikey komşuluğunda karşılıksız çıktı
    # blok 41-50
    ('ودع',  'bırakma, terk (da\'); emanet bırakılan yer (müstevda\')'),
    ('فيأ',  'geri dönme; savaşsız elde edilen (fey\'); gölge'),
    # blok 51-60
    ('عجب',  'hoşa gitme, beğenme; şaşma (aceb)'),
    ('جلب',  'toplayıp sürme (ecleb); dış örtü (cilbâb)'),
    ('غرو',  'kışkırtma, üzerine salma (iğrâ)'),
    # blok 61-70
    ('ثقف',  'ele geçirme, yakalama (sekife)'),
    ('سود',  'efendi, ulu (seyyid); siyahlık (esved)'),
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
