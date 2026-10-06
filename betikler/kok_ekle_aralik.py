# -*- coding: utf-8 -*-
"""kok_turkce.json'a aralık okuması (2026-10-05, ayrı oturum) sırasında açığa çıkan karşılıksız kökü ekler.
16:10 ağır okumasında ölçüm satırı '???', dikey 'KARŞILIK YOK' verdi (okumayı bloke eden arıza istisnası).
ANAHTAR KURALI: anahtar ELLE YAZILMAZ — kok_envanteri.json içinden NFC eşlemesiyle KOPYALANIR.
Lemma sayımı (morph): sîmâ 6 · yesûmu 4 · musavvema/musavvim 4 · tusîmu 1.
سمد: hapaks (53:61 sâmidûn), tek lemma."""
import json, unicodedata
env = json.load(open('kok_envanteri.json', encoding='utf-8'))
kt = json.load(open('kok_turkce.json', encoding='utf-8'))
ISTEK = [
    ('سوم', 'nişan, alamet (sîmâ); azap reva görme (yesûmu); işaretli (musavvem); otlatma (tusîmu)'),
    # 53:61 ağır okuması (aralık 53:58→62) — hapaks; ölçüm satırı ??? verdi
    ('سمد', 'kayıtsızca oyalanma, gaflet; başı dik, umursamaz durma (sâmidûn)'),
]
nfc = lambda s: unicodedata.normalize('NFC', s)
korpus = {nfc(k): k for k in env}
eklendi, bulunamadi = [], []
for ara, tr in ISTEK:
    k = korpus.get(nfc(ara))
    if k is None: bulunamadi.append(ara); continue
    if k in kt: continue
    kt[k] = tr; eklendi.append((k, tr))
json.dump(kt, open('kok_turkce.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)
print('eklenen:', len(eklendi)); [print('  ', k, '->', v) for k, v in eklendi]
print('bulunamayan:', bulunamadi); assert not bulunamadi, 'NFC eşleşmesi yok — koşu DURDU'
print('toplam kök:', len(kt))
