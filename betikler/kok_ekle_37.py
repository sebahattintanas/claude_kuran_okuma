# -*- coding: utf-8 -*-
"""kok_turkce.json'a sûre 37 (Sâffât) blokları için yeni kök karşılıkları ekler.
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC
eşlemesiyle bulunup KOPYALANIR."""
import json, unicodedata

env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))

ISTEK = [
    # sûrenin tümü baştan (oturum 2026-10-04 sonu); baskın lemma sayıldı
    ('دحر',  'kovulmuş, itilmiş (medhûr); kovma (duhûr)'),
    ('وصب',  'sürekli, kesintisiz (vâsib)'),
    ('ثقب',  'delip geçen, parlayan (sâqıb)'),
    ('لزب',  'yapışkan (lâzib)'),
    ('كأس',  'kadeh (ke\'s)'),
    ('لذذ',  'lezzet (lezze); hoşa gitme (telezzu)'),
    ('غول',  'baş döndürme, sarhoşluk, zarar (gavl)'),
    ('نزف',  'aklı gitme, sarhoş olma (yunzefu)'),
    ('شوب',  'karışım (şevb)'),
    ('هرع',  'koşturulma, ardından seğirtme (yuhra\'u)'),
    ('سقم',  'hasta, hastalıklı (sakîm)'),
    ('روغ',  'gizlice yönelme, yanaşma (râğa)'),
    ('زفف',  'koşarak gelme (yeziffu)'),
    ('تلل',  'yüzüstü yatırma, yere yıkma (telle)'),
    ('جبن',  'alın, şakak (cebîn)'),
    ('أبق',  'kaçma — kölenin kaçışı (ebeqa)'),
    ('سهم',  'kura çekme, ok atışmak (sâheme)'),
    ('دحض',  'kaybeden, yenilen (mudhad); çürütme, geçersiz kılma (yudhidu, dâhida)'),
    ('لقم',  'yutma (iltekame)'),
    ('حوت',  'balık (hût)'),
    ('سوح',  'avlu, meydan (sâha)'),
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
