# -*- coding: utf-8 -*-
"""aday_ekle_97_kadr.py — sûre 97 (Kadr) adayları (AX_kadr) ve okuma bağları (AS_kadr).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

KADR = [
]

BAGLAR = {"AS_kadr": [
 # blok 1-5
 {'bag': '96:19 → 97:1', 'kural': "okuma — ardışık sûre sınırı: 2MS'ye yasak ve secde emri ile kapanış / 1P haber ile açılış; fâsıla ب → ر (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '12:2 → 97:1', 'kural': "okuma — harekesiz 'innâ enzelnâhu': ACC 'qur'ânen 'arabiyyen' / 'fî leyleti'l-qadr'", 'not': 'kalıp eşi.'},
 {'bag': '44:3 → 97:1', 'kural': "okuma — harekesiz 'innâ enzelnâhu' + 'fî' + lemma 'leyle': nekre, 'mubârake' sıfatlı / belirli, 'el-qadr' tamlamalı", 'not': 'kalıp eşi.'},
 {'bag': '97:1 → 97:3', 'kural': "sûre içi — harekesiz 'leyletu'l-qadr' ardışık üç ayette: 97:1, 97:2, 97:3 (korpusun tamamı)", 'not': 'sûre içi eş.'},
 {'bag': '69:3 → 97:2', 'kural': "okuma — harekesiz 've mâ edrâke mâ': 'el-hâqqa' / 'leyletu'l-qadr'", 'not': 'kalıp eşi.'},
 {'bag': '86:2 → 97:2', 'kural': "okuma — harekesiz 've mâ edrâke mâ': 'et-târıq' / 'leyletu'l-qadr'", 'not': 'kalıp eşi.'},
 {'bag': '70:4 → 97:3', 'kural': "okuma — lemma 'elf' süre ölçüsünde: 'xamsîne elfe sene' / 'elfi şehr'", 'not': 'lemma eşi.'},
 {'bag': '70:4 → 97:4', 'kural': "okuma — harekesiz 'el-melâ'iketu ve'r-rûh' korpusun iki geçişi: 'ta'ruju' yükselir / 'tenezzelu' iner", 'not': 'kalıp eşi.'},
 {'bag': '78:38 → 97:4', 'kural': "okuma — aynı iki ad ters sırayla ('er-rûhu ve'l-melâ'iketu'); fiil öndeki ada uyuyor: 'yeqûmu' 3MS / 'tenezzelu' 3FS", 'not': 'kuruluş eşi.'},
 {'bag': '16:2 → 97:4', 'kural': "okuma — kök نزل + melekler + rûh + 'emr' aynı ayette: melekler nesne, rûh 'bi' ile / ikisi özne", 'not': 'kuruluş eşi.'},
 {'bag': '41:30 → 97:4', 'kural': "okuma — lemma 'tenezzele' + 'el-melâ'iketu': iki te ile 'tetenezzelu' / tek te ile 'tenezzelu'", 'not': 'lemma eşi.'},
 {'bag': '14:1 → 97:4', 'kural': "okuma — harekesiz 'bi-izni rabbihim': çıkarma fiiline bağlı / inişe bağlı", 'not': 'kalıp eşi.'},
 {'bag': '44:4 → 97:4', 'kural': "okuma — harekesiz 'kullu emr' + geceye dönen 'fîhâ'; 44:3-4 ardışık / 97:1 ve 97:4 arasında iki ayet", 'not': 'kalıp eşi.'},
 {'bag': '97:1 → 97:4', 'kural': "sûre içi — kök نزل iki geçiş: 'enzelnâ' PERF 1P / 'tenezzelu' IMPF 3FS", 'not': 'sûre içi eş.'},
 {'bag': '89:1 → 97:5', 'kural': "okuma — lemma 'fecr': yemin edilen / gecenin sınırı", 'not': 'lemma eşi.'},
 {'bag': '97:3 → 97:5', 'kural': "sûre içi — 'leyle' (97:1-3) / 'fecr' (97:5): gece fecrin doğuşuyla sınırlanıyor (aday 1039, okuma)", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_kadr', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in KADR]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_kadr'] = KADR
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_kadr', len(KADR), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_kadr', len(BAGLAR['AS_kadr']))
