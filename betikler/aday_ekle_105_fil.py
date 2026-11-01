# -*- coding: utf-8 -*-
"""aday_ekle_105_fil.py — sûre 105 (Fil) adayları (AX_fil) ve okuma bağları (AS_fil).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

FIL = [
]

BAGLAR = {"AS_fil": [
 # blok 1-5
 {'bag': '104:9 → 105:1', 'kural': "okuma — ardışık sûre sınırı: fiilsiz öbekle kapanış / 'e-lem tera' sorusuyla açılış; fâsıla ة → ل; 104 lafız 1 Rab 0, 105 lafız 0 Rab 1 (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '89:6 → 105:1', 'kural': "okuma — kalıp 'e-lem tera keyfe fe'ale rabbuke' korpusun iki geçişi: 'bi-'âd' / 'bi-ashâbi'l-fîl' (ölçüm xref)", 'not': 'kalıp eşi.'},
 {'bag': '105:1 → 105:2', 'kural': "sûre içi — iki 'e-lem' sorusu (IMPF cezm); 3MS özne sürüyor", 'not': 'sûre içi eş.'},
 {'bag': '77:32 → 105:4', 'kural': "okuma — lemma 'ramâ' aynı biçim 'termî' (3FS) + 'bi': kıvılcım / taş", 'not': 'lemma eşi.'},
 {'bag': '15:74 → 105:4', 'kural': "okuma — lemma 'siccîl' (korpusun tamamı 3 ayet): yağdırılan / kuşların attığı", 'not': 'lemma eşi.'},
 {'bag': '55:12 → 105:5', 'kural': "okuma — lemma ''asf': saman yapraklı tane / yenmiş ekin yaprağı teşbihi", 'not': 'lemma eşi.'},
 {'bag': '21:58 → 105:5', 'kural': "okuma — kalıp 'fe-ce'alehum' + sonuç: paramparça / yenmiş ekin yaprağı gibi", 'not': 'kalıp eşi.'},
 {'bag': '105:3 → 105:4', 'kural': "sûre içi — 3FS fiil 'termî' 'tayr'a uyuyor", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_fil', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in FIL]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_fil'] = FIL
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_fil', len(FIL), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_fil', len(BAGLAR['AS_fil']))
