# -*- coding: utf-8 -*-
"""aday_ekle_102_tekasur.py — sûre 102 (Tekasur) adayları (AX_tekasur) ve okuma bağları (AS_tekasur).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

TEKASUR = [
]

BAGLAR = {"AS_tekasur": [
 # blok 1-8
 {'bag': '101:11 → 102:1', 'kural': "okuma — ardışık sûre sınırı: ateş adıyla kapanış / 2MP hitapla açılış; fâsıla ة → ر (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '57:20 → 102:1', 'kural': "okuma — lemma 'tekâsur' korpusun iki geçişi: mallarda ve evlatlarda / neyin çoğaltıldığı yazılmamış", 'not': 'lemma eşi.'},
 {'bag': '82:4 → 102:2', 'kural': "okuma — kök قبر: 'qubûr' altüst edilen / 'maqâbir' varılan", 'not': 'kök eşi.'},
 {'bag': '100:9 → 102:2', 'kural': "okuma — kök قبر: kabirlerdekiler çıkarılan / kabirlere varılan", 'not': 'kök eşi.'},
 {'bag': '11:93 → 102:3', 'kural': "okuma — kalıp 'sevfe ta'lemûn': nesneli / nesnesiz", 'not': 'kalıp eşi.'},
 {'bag': '102:3 → 102:4', 'kural': "sûre içi — 'kellâ sevfe ta'lemûn' iki geçiş, ikincisi 'summe' ile (ölçüm esit2 BENZER 0,9231)", 'not': 'sûre içi eş.'},
 {'bag': '78:4 → 102:3', 'kural': "okuma — 'kellâ' + gelecek + 'alime': 3MP 'se-' / 2MP 'sevfe'", 'not': 'kuruluş eşi.'},
 {'bag': '78:5 → 102:4', 'kural': "okuma — kalıp 'summe kellâ' korpusun iki geçişi; 78:4-5 ve 102:3-4 aynı ikili kuruluş", 'not': 'kalıp eşi.'},
 {'bag': '56:76 → 102:5', 'kural': "okuma — kalıp 'lev ta'lemûn' korpusun iki geçişi: ara söz / cevapsız şart", 'not': 'kalıp eşi.'},
 {'bag': '69:51 → 102:5', 'kural': "okuma — lemma 'yaqîn' tamlamada: 'haqqu'l-yaqîn' / ''ilme'l-yaqîn'", 'not': 'lemma eşi.'},
 {'bag': '56:95 → 102:7', 'kural': "okuma — lemma 'yaqîn' tamlamada: 'haqqu'l-yaqîn' / ''ayne'l-yaqîn'", 'not': 'lemma eşi.'},
 {'bag': '102:5 → 102:7', 'kural': "sûre içi — ''ilme'l-yaqîn' / ''ayne'l-yaqîn': aynı 'yaqîn', ilk ad bilgi / göz", 'not': 'sûre içi eş.'},
 {'bag': '79:36 → 102:6', 'kural': "okuma — lemma 'cahîm' + kök رأي: görecek olana gösterilen / 2MP görecek", 'not': 'lemma eşi.'},
 {'bag': '101:11 → 102:6', 'kural': "okuma — ardışık iki sûrede ateş adı: 'nâr' / 'cahîm'", 'not': 'sınır ötesi eş.'},
 {'bag': '102:6 → 102:7', 'kural': "sûre içi — 'le-terawunne' iki geçiş, ikincisi 'summe' ve 3FS zamirle", 'not': 'sûre içi eş.'},
 {'bag': '16:56 → 102:8', 'kural': "okuma — kalıp 'le-tus'elunne' korpusun iki geçişi: yeminle, uydurduklarından / 'yevme'izin', nimetten", 'not': 'kalıp eşi.'},
 {'bag': '100:11 → 102:8', 'kural': "okuma — 'yevme'izin': Rab haberdar / 2MP sorguya çekilen", 'not': 'kalıp eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_tekasur', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in TEKASUR]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_tekasur'] = TEKASUR
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_tekasur', len(TEKASUR), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_tekasur', len(BAGLAR['AS_tekasur']))
