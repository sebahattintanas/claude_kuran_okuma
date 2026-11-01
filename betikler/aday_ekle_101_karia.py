# -*- coding: utf-8 -*-
"""aday_ekle_101_karia.py — sûre 101 (Karia) adayları (AX_karia) ve okuma bağları (AS_karia).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

KARIA = [
]

BAGLAR = {"AS_karia": [
 # blok 1-11
 {'bag': '100:11 → 101:1', 'kural': "okuma — ardışık sûre sınırı: Rab + tekitli haberle kapanış / tek kelimeyle açılış; fâsıla ر → ة (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '69:1 → 101:1', 'kural': "okuma — tek kelimelik açılış: 'el-hâqqa' / 'el-qâri'a'; 69:1-3 ve 101:1-3 aynı üç ayetlik kuruluş", 'not': 'kuruluş eşi.'},
 {'bag': '69:4 → 101:1', 'kural': "okuma — lemma 'qâri'a': 'bi'l-qâri'a' yalanlanan / tek başına ad", 'not': 'lemma eşi.'},
 {'bag': '13:31 → 101:1', 'kural': "okuma — lemma 'qâri'a': nekre, inkâr edenlere dokunan / belirli, tek başına", 'not': 'lemma eşi.'},
 {'bag': '69:2 → 101:2', 'kural': "okuma — 'mâ' + aynı belirli ad: 'me'l-hâqqa' / 'me'l-qâri'a'", 'not': 'kuruluş eşi.'},
 {'bag': '101:1 → 101:3', 'kural': "sûre içi — 'el-qâri'a' üç ayet sonunda: tek kelime / 'mâ' ile / 've mâ edrâke mâ' ile", 'not': 'sûre içi eş.'},
 {'bag': '97:2 → 101:3', 'kural': "okuma — harekesiz 've mâ edrâke mâ': iki kelimelik tamlama / tek kelime", 'not': 'kalıp eşi.'},
 {'bag': '70:8 → 101:4', 'kural': "okuma — 'yevme' + IMPF 'kâne' + belirli ad + 'ke' + ad: gök / insanlar", 'not': 'kuruluş eşi.'},
 {'bag': '70:9 → 101:5', 'kural': "okuma — harekesiz 've tekûnu'l-cibâlu ke'l-'ihn' korpusun iki geçişi: sıfatsız / 'el-menfûş' ile; ilk ayetin öznesi gök / insanlar", 'not': 'kalıp eşi.'},
 {'bag': '23:102 → 101:6', 'kural': "okuma — harekesiz 'saqulet mevâzînuh': 'fe-men' + 'ulâ'ike humu'l-muflihûn' / 'fe-emmâ men' + 101:7", 'not': 'kalıp eşi.'},
 {'bag': '69:21 → 101:7', 'kural': "okuma — esit2 TAM: 'fe-huve fî 'îşetin râdiyeh'; 69:19 kitabı sağdan verilen / 101:6 tartısı ağır gelen şartına cevap", 'not': 'TAM tekrar.'},
 {'bag': '23:103 → 101:8', 'kural': "okuma — lemma 'xaffet' + 'mevâzînuh': 23:102-103 ardışık / 101:6 ve 101:8 arasında 101:7", 'not': 'kalıp eşi.'},
 {'bag': '101:6 → 101:8', 'kural': "sûre içi — aynı iskelet 'emmâ men' + PERF + 'mevâzînuh': 'saqulet' / 'xaffet' (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '101:3 → 101:10', 'kural': "sûre içi — 've mâ edrâke mâ' iki geçiş: 'el-qâri'a' / 'hiyeh' (ölçüm nakarat3)", 'not': 'sûre içi eş.'},
 {'bag': '69:19 → 101:10', 'kural': "okuma — ayet sonu 'h': 'kitâbiyeh' / 'hiyeh'", 'not': 'yazım eşi.'},
 {'bag': '88:4 → 101:11', 'kural': "okuma — lemma 'hâmiye' korpusun iki geçişi: 'nâran hâmiyeh' ACC, girilen ateş / 'nârun hâmiyeh' NOM, sorunun cevabı", 'not': 'lemma eşi.'},
 {'bag': '101:9 → 101:11', 'kural': "sûre içi — 'hâviye' (101:9) → soru (101:10) → 'nârun hâmiyeh' (101:11): metin kendi sorusunu cevaplıyor", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_karia', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in KARIA]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_karia'] = KARIA
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_karia', len(KARIA), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_karia', len(BAGLAR['AS_karia']))
