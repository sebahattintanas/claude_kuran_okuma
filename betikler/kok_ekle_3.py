# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 3 (Âl-i İmrân) blokları için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    # sûre 3 (Âl-i İmrân) — blok blok eklenir (2026-11-08); korpus geçişleri kok_envanteri ayet_sayisi ile
    # blok 10-14
    ('قنطر', "yığın, büyük miktar mal ('qintâr'); yığılmış ('muqantara'); 3 ayet"),
    # blok 38-41
    ('رمز', "işaret etme, ima ('remz'); 1 ayet"),
    # blok 42-47
    ('كهل', "olgunluk çağı, orta yaş ('kehl'); 2 ayet"),
    # blok 48-51
    ('ذخر', "biriktirme, saklama ('iddixâr'); 1 ayet"),
    # blok 57-63
    ('بهل', "lanetleşme, içtenlikle yakarma ('ibtihâl'); 1 ayet"),
    # blok 74-77
    ('دنر', "dinar, altın para ('dînâr'); 1 ayet"),
    # blok 121-125
    ('فشل', "yılgınlık, gevşeyip cesaretini yitirme ('feşile'); 4 ayet"),
    # blok 137-143
    ('محص', "sınayarak arındırma, ayıklama ('yumahhisa'); 2 ayet"),
    # blok 154-155
    ('نعس', "uyuklama, hafif uyku ('nu'âs'); 2 ayet"),
    # blok 156-159
    ('غزو', "gazâ, savaşa çıkma ('ğuzzâ'); 1 ayet"),
    ('فظظ', "kaba, katı ('fazz'); 1 ayet"),
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
