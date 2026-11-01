# -*- coding: utf-8 -*-
"""aday_ekle_112_ihlas.py — sûre 112 (Ihlas) adayları (AX_ihlas) ve okuma bağları (AS_ihlas).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

IHLAS = [
]

BAGLAR = {"AS_ihlas": [
 # blok 1-4
 {'bag': '111:5 → 112:1', 'kural': "okuma — ardışık sûre sınırı: fiilsiz isim cümlesiyle kapanış / 'qul' emriyle açılış; fâsıla د → د; 111 lafızsız ve Rabsız, 112 lafız 2 Rab yok (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '67:29 → 112:1', 'kural': "okuma — kalıp 'qul huve': 'er-rahmân' + 1P inanma / lafız + 'ehad'", 'not': 'kalıp eşi.'},
 {'bag': '59:22 → 112:1', 'kural': "okuma — harekesiz 'huve'llâh': ilgi zamiri + nefy-istisna / nekre haber 'ehad'", 'not': 'kalıp eşi.'},
 {'bag': '72:22 → 112:1', 'kural': "okuma — harekesiz 'allâhu ehad' (korpusun iki geçişi): 'mina'llâhi ehad' olumsuz özne 'hiç kimse' / lafzın haberi", 'not': 'kalıp eşi.'},
 {'bag': '112:1 → 112:4', 'kural': "sûre içi — lemma 'ehad': Allah, olumlu haber / 'hiç kimse', olumsuz cümlede nekre (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '89:25 → 112:4', 'kural': "okuma — olumsuz cümlede nekre 'ehad' ('hiç kimse'): esmâ 'degil' emsali", 'not': 'kuruluş eşi.'},
 {'bag': '37:152 → 112:3', 'kural': "okuma — lemma 'velede', özne Allah: iddia, PERF olumlu ('ve innehum le-kâzibûn') / 'lem' ile olumsuz + edilgen", 'not': 'lemma eşi.'},
 {'bag': '19:33 → 112:3', 'kural': "okuma — lemma 'velede' edilgen: PERF 1S 'vulidtu' / 'lem yûled' 3MS", 'not': 'lemma eşi.'},
 {'bag': '17:111 → 112:4', 'kural': "okuma — kalıp 've lem yekun lehû' (korpusun üç geçişi okundu): 'şerîk' + 'veliyy', önce 'lem yettexiz veleden' / 'kufuwen ehad', önce 'lem yelid'", 'not': 'kalıp eşi.'},
 {'bag': '25:2 → 112:4', 'kural': "okuma — kalıp 've lem yekun lehû': 'şerîkun fi'l-mulk', önce 'lem yettexiz veleden' / 'kufuwen ehad'", 'not': 'kalıp eşi.'},
 {'bag': '112:3 → 112:4', 'kural': "sûre içi — 'lem' + cezm üç kez: 'yelid', 'yûled', 'yekun'", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_ihlas', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in IHLAS]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_ihlas'] = IHLAS
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_ihlas', len(IHLAS), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_ihlas', len(BAGLAR['AS_ihlas']))
