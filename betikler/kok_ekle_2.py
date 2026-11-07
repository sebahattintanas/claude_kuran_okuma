# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 2 (Bakara) blokları için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    # sûre 2 (Bakara, 21. ayetten) — blok blok eklenir (2026-11-01); korpus geçişleri kok_envanteri ayet_sayisi ile
    # blok 30-33
    ('سفك', "kan dökme, akıtma (sefk; 2 ayet)"),
    # blok 54-59
    ('حطط', "indirme, bırakma; 'hitta' (bağışla, yükümüzü indir; 2 ayet)"),
    # blok 60-61
    ('بقل', 'sebze, yeşillik (baql; 1 ayet)'),
    ('قثأ', "acur, hıyar (qiththâ'; 1 ayet)"),
    ('فوم', 'sarımsak ya da buğday (fûm; 1 ayet)'),
    ('عدس', "mercimek ('adas; 1 ayet)"),
    ('بصل', 'soğan (basal; 1 ayet)'),
    # blok 62-66
    ('قرد', 'maymun (qırade, çoğul; 3 ayet)'),
    # blok 67-70
    ('فقع', "parlak, koyu (renk için 'fâqi''; 1 ayet)"),
    # blok 71-74
    ('وشي', "alaca, leke (renk için 'şiye'; 1 ayet)"),
    # blok 87-90
    ('غلف', "örtülü, perdeli (ğulf; 'qulûbunâ ğulf'; 2 ayet)"),
    # blok 96-101
    ('زحزح', "uzaklaştırma, kurtarma (zahzaha; 'bi-muzahzihihî'; 2 ayet)"),
    # blok 153-159
    ('مرو', "Merve (tepe adı, 'el-merwe'; Safâ ile birlikte; 1 ayet)"),
    # blok 168-172
    ('نعق', "(çobanın sürüye) bağırması, haykırma ('yen’iqu'; 1 ayet)"),
    # blok 183-185
    ('طوق', "güç yetirme, takat ('yutîqûneh', 'tâqa'); boyna dolama ('yutavvaqûn'; 4 ayet)"),
    ('رمض', "Ramazan (ay adı, 'şehru ramadân'; 1 ayet)"),
    # blok 186-188
    ('رفث', "kadına yaklaşma, cinsel ilişki / söz ('er-refes'; 2 ayet)"),
    ('خيط', "iplik ('el-xayt'); iğne ('el-xiyât'; 2 ayet)"),
    # blok 232-233
    ('عضل', "engel olma, (evlenmeden) alıkoyma ('ta’dulû'; 2 ayet)"),
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
