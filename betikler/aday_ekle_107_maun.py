# -*- coding: utf-8 -*-
"""aday_ekle_107_maun.py — sûre 107 (Maun) adayları (AX_maun) ve okuma bağları (AS_maun).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

MAUN = [
]

BAGLAR = {"AS_maun": [
 # blok 1-7
 {'bag': '106:4 → 107:1', 'kural': "okuma — ardışık sûre sınırı: Rab'ın doyurmasıyla kapanış / 'e-ra'eyte' sorusuyla açılış; fâsıla ف → ن; 106 Rab 1, 107 lafızsız ve Rabsız (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '106:4 → 107:3', 'kural': "okuma — kök طعم ardışık iki sûrede: Rab doyurdu / yoksulun yemeğine özendirmeyen", 'not': 'sınır ötesi eş.'},
 {'bag': '96:9 → 107:1', 'kural': "okuma — kalıp 'e-ra'eyte'llezî' korpusun iki geçişi: engelleyen / dîni yalanlayan", 'not': 'kalıp eşi.'},
 {'bag': '89:17 → 107:2', 'kural': "okuma — lemma 'yetîm': ikram edilmeyen / itip kakılan; ardından ikisinde de yoksulun yemeği (89:18 / 107:3)", 'not': 'kuruluş eşi.'},
 {'bag': '69:34 → 107:3', 'kural': "okuma — kalıp 've lâ yahuddu 'alâ ta'âmi'l-miskîn' korpusun iki geçişi (ölçüm esit2 TAM, xref)", 'not': 'kalıp eşi.'},
 {'bag': '89:18 → 107:3', 'kural': "okuma — 2MP VI. bab 'tehâddûne' / 3MS 'yahuddu' (ölçüm esit2 BENZER 0,9000)", 'not': 'kalıp eşi.'},
 {'bag': '70:22 → 107:4', 'kural': "okuma — lemma 'musallî': istisna edilenler / 'veyl' ile anılanlar", 'not': 'lemma eşi.'},
 {'bag': '70:23 → 107:5', 'kural': "okuma — 'musallîn' + 'ellezîne hum … salâtihim': ''alâ … dâ'imûn' / ''an … sâhûn'", 'not': 'kuruluş eşi.'},
 {'bag': '51:11 → 107:5', 'kural': "okuma — lemma 'sâhî' korpusun iki geçişi, ikisinde de 'ellezîne hum' + 'sâhûn'", 'not': 'lemma eşi.'},
 {'bag': '107:5 → 107:6', 'kural': "sûre içi — 'ellezîne hum' iki geçiş", 'not': 'sûre içi eş.'},
 {'bag': '107:1 → 107:6', 'kural': "sûre içi — kök رأي: 'e-ra'eyte' (2MS) / 'yurâ'ûn' (3MP, gösteriş)", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_maun', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in MAUN]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_maun'] = MAUN
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_maun', len(MAUN), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_maun', len(BAGLAR['AS_maun']))
