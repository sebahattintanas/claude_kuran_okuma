# -*- coding: utf-8 -*-
"""aday_ekle_100_adiyat.py — sûre 100 (Adiyat) adayları (AX_adiyat) ve okuma bağları (AS_adiyat).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

ADIYAT = [
]

BAGLAR = {"AS_adiyat": [
 # blok 1-11
 {'bag': '99:8 → 100:1', 'kural': "okuma — ardışık sûre sınırı: şartla kapanış / yeminle açılış; fâsıla ه → ا (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '79:1 → 100:1', 'kural': "okuma — 've' + adsız dişil çoğul ortaç + ACC mastar ile açılan yemin dizisi", 'not': 'kuruluş eşi.'},
 {'bag': '77:1 → 100:1', 'kural': "okuma — 've' + adsız dişil çoğul ortaç + ACC ile açılan yemin dizisi", 'not': 'kuruluş eşi.'},
 {'bag': '79:3 → 100:2', 'kural': "okuma — dişil çoğul ortaç + aynı / yakın anlamlı ACC; atıflı yeminde QASEM yok (924)", 'not': 'kuruluş eşi.'},
 {'bag': '81:18 → 100:3', 'kural': "okuma — lemma 'subh': yemin edilen sabah / baskının zamanı (ACC zarf)", 'not': 'lemma eşi.'},
 {'bag': '30:48 → 100:4', 'kural': "okuma — lemma 'esâra': rüzgârlar bulutu kaldırır / adsız özne tozu kaldırır", 'not': 'lemma eşi.'},
 {'bag': '100:4 → 100:5', 'kural': "sûre içi — aynı iskelet 'fe' + PERF 3FP + 'bihî' + nekre ACC", 'not': 'sûre içi eş.'},
 {'bag': '70:19 → 100:6', 'kural': "okuma — harekesiz 'inne'l-insân': 'xuliqa helû'â' / 'li-rabbihî le-kenûd'", 'not': 'kalıp eşi.'},
 {'bag': '96:6 → 100:6', 'kural': "okuma — harekesiz 'inne'l-insân' + 'le-': IMPF 'le-yatğâ' / nekre sıfat 'le-kenûd'", 'not': 'kalıp eşi.'},
 {'bag': '100:6 → 100:8', 'kural': "sûre içi — 'inne' + 'le-' tekitli haber üç ayette art arda; 've innehû' iki geçiş (100:7, 100:8)", 'not': 'sûre içi eş.'},
 {'bag': '89:20 → 100:8', 'kural': "okuma — lemma 'hubb': nesnesi açıkça mal, 'hubben cemmâ' / 'hubbu'l-xayr'", 'not': 'lemma eşi.'},
 {'bag': '85:12 → 100:8', 'kural': "okuma — harekesiz 'le-şedîd': Rabbin yakalayışı / insan (aday 1041, sûreler arası okuma notu)", 'not': 'kalıp eşi.'},
 {'bag': '82:4 → 100:9', 'kural': "okuma — lemma 'bu'thira' korpusun iki geçişi: özne kabirler 3FS / 'mâ fi'l-qubûr' 3MS", 'not': 'lemma eşi.'},
 {'bag': '99:2 → 100:9', 'kural': "okuma — ardışık sûre: yer ağırlıklarını çıkarır / kabirlerdekiler altüst edilir (aday 1040, okuma)", 'not': 'ardışık sûre eşi.'},
 {'bag': '100:9 → 100:10', 'kural': "sûre içi — aynı kuruluş: edilgen PERF + 'mâ fî' + belirli çoğul — 'el-qubûr' / 'es-sudûr'", 'not': 'sûre içi eş.'},
 {'bag': '10:57 → 100:10', 'kural': "okuma — harekesiz 'mâ fi's-sudûr' korpusun iki geçişi: göğüslerdekine şifa / göğüslerdekinin açığa çıkarılması", 'not': 'kalıp eşi.'},
 {'bag': '99:6 → 100:10', 'kural': "okuma — ardışık sûre: kök صدر 'yasduru' (gloss uymuyor) / 'es-sudûr' (gloss uyuyor) (aday 1040, okuma)", 'not': 'ardışık sûre eşi.'},
 {'bag': '17:30 → 100:11', 'kural': "okuma — Rab + 'bi' + zamir / ad + lemma 'xabîr': 'bi-'ibâdihî xabîran basîrâ' / 'bihim yevme'izin le-xabîr'", 'not': 'kuruluş eşi.'},
 {'bag': '99:4 → 100:11', 'kural': "okuma — ardışık sûre: 'yevme'izin' (99:4, 99:6 / 100:11) ve kök خبر 'axbârehâ' / 'xabîr' (aday 1040, okuma)", 'not': 'ardışık sûre eşi.'},
 {'bag': '100:6 → 100:11', 'kural': "sûre içi — Rab iki geçiş: 'li-rabbihî' 3MS / 'rabbehum' 3MP (tekilden çoğula)", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_adiyat', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in ADIYAT]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_adiyat'] = ADIYAT
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_adiyat', len(ADIYAT), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_adiyat', len(BAGLAR['AS_adiyat']))
