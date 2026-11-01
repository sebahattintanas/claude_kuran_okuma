# -*- coding: utf-8 -*-
"""aday_ekle_103_asr.py — sûre 103 (Asr) adayları (AX_asr) ve okuma bağları (AS_asr).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

ASR = [
]

BAGLAR = {"AS_asr": [
 # blok 1-3
 {'bag': '102:8 → 103:1', 'kural': "okuma — ardışık sûre sınırı: sorguyla kapanış / yeminle açılış; fâsıla م → ر; iki sûre de lafızsız ve Rabsız (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '93:1 → 103:1', 'kural': "okuma — 've' + belirli ad, yemin edilen vakit adı: kuşluk / 'asr' (anlamı KAPATILAMAZ)", 'not': 'kuruluş eşi.'},
 {'bag': '78:14 → 103:1', 'kural': "okuma — kök عصر: 'el-mu'sırât' / 'el-'asr'", 'not': 'kök eşi.'},
 {'bag': '70:19 → 103:2', 'kural': "okuma — kalıp 'inne'l-insân': edilgen fiil + hâl / 'le' + 'fî' + ad", 'not': 'kalıp eşi.'},
 {'bag': '96:6 → 103:2', 'kural': "okuma — kalıp 'inne'l-insân': 'le' + IMPF / 'le' + 'fî' + ad", 'not': 'kalıp eşi.'},
 {'bag': '100:6 → 103:2', 'kural': "okuma — kalıp 'inne'l-insân': 'li-rabbihî' + 'le' + sıfat / 'le' + 'fî' + ad", 'not': 'kalıp eşi.'},
 {'bag': '65:9 → 103:2', 'kural': "okuma — lemma 'xusr' korpusun iki geçişi: işin sonu / insanın içinde bulunduğu", 'not': 'lemma eşi.'},
 {'bag': '95:5 → 103:2', 'kural': "okuma — insan hakkında tekil hüküm (3MS zamir / belirli ad), ardından 'ellezîne' istisnası (95:6 / 103:3)", 'not': 'kuruluş eşi.'},
 {'bag': '70:22 → 103:3', 'kural': "okuma — 'el-insân' (70:19) hakkında hükümden sonra çoğul istisna: 'el-musallîn' / 'ellezîne'", 'not': 'kuruluş eşi.'},
 {'bag': '84:25 → 103:3', 'kural': "okuma — kalıp 'illa'llezîne âmenû ve 'amilu's-sâlihât': devamı karşılık / iki 'tevâsav'", 'not': 'kalıp eşi.'},
 {'bag': '95:6 → 103:3', 'kural': "okuma — kalıp 'illa'llezîne âmenû ve 'amilu's-sâlihât': devamı karşılık / iki 'tevâsav'", 'not': 'kalıp eşi.'},
 {'bag': '90:17 → 103:3', 'kural': "okuma — kalıp 've tevâsav bi's-sabr' korpusun iki geçişi: sabır ilk (merhametle) / sabır ikinci (hakla)", 'not': 'kalıp eşi.'},
 {'bag': '51:53 → 103:3', 'kural': "okuma — lemma 'tevâsav': azgın topluluk hakkında soru / iman edenlerin hakkı ve sabrı tavsiyesi", 'not': 'lemma eşi.'},
 {'bag': '103:2 → 103:3', 'kural': "sûre içi — 'el-insân' hakkında hüküm / 'illâ' istisnası (ölçüm ISTISNA)", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_asr', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in ASR]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_asr'] = ASR
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_asr', len(ASR), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_asr', len(BAGLAR['AS_asr']))
