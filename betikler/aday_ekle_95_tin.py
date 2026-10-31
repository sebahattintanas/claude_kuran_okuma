# -*- coding: utf-8 -*-
"""aday_ekle_95_tin.py — sûre 95 (Tîn) adayları (AX_tin) ve okuma bağları (AS_tin).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

TIN = [
]

BAGLAR = {"AS_tin": [
 # blok 1-8
 {'bag': '94:8 → 95:1', 'kural': 'okuma — ardışık sûre sınırı: Rabbe yönelme emri ile kapanış / incir ve zeytine yemin ile açılış; fâsıla ب → ن (aday 1040, kayıt)', 'not': 'sınır eşi.'},
 {'bag': '80:29 → 95:1', 'kural': "okuma — lemma 'zeytûn': yerden bitenler dizisinde / yemin edilen", 'not': 'lemma eşi.'},
 {'bag': '52:1 → 95:2', 'kural': "okuma — lemma 'tûr' yeminde: tek başına / 'tûri sînîn' tamlaması", 'not': 'lemma eşi.'},
 {'bag': '23:20 → 95:2', 'kural': "okuma — 'tûr' + yer adı tamlaması: 'tûri seynâ'' / 'tûri sînîn' (ikinci ad farklı biçimde)", 'not': 'kalıp eşi.'},
 {'bag': '90:1 → 95:3', 'kural': "okuma — 'hâze'l-beled' yeminde: 'lâ uqsimu bi-' / 've' + sıfat 'el-emîn'", 'not': 'kalıp eşi.'},
 {'bag': '90:4 → 95:4', 'kural': "okuma — harekesiz 'le-qad xalaqne'l-insân' korpusun iki geçişi, ikisi de yeminin ardından: 'fî kebed' / 'fî ahseni taqvîm'", 'not': 'kalıp eşi.'},
 {'bag': '95:4 → 95:5', 'kural': 'sûre içi — en güzel biçim / aşağıların en aşağısı (aday 1039, okuma)', 'not': 'sûre içi eş.'},
 {'bag': '11:82 → 95:5', 'kural': "okuma — lemma 'sâfil' (korpusun üç geçişi okundu): yerin üstü altına / insan aşağıların aşağısına", 'not': 'lemma eşi.'},
 {'bag': '84:25 → 95:6', 'kural': "ölçüm esit2 YAKIN + lemma dizisi (bütün ayet): 'lehum' / 'fe-lehum'", 'not': 'esit2 eşi.'},
 {'bag': '41:8 → 95:6', 'kural': "ölçüm esit2 BENZER + xref: 'inne' ile / 'illâ' ile istisna", 'not': 'esit2 eşi.'},
 {'bag': '95:3 → 95:6', 'kural': "sûre içi — kök أمن iki geçiş: 'el-emîn' / 'âmenû'", 'not': 'sûre içi eş.'},
 {'bag': '82:9 → 95:7', 'kural': "okuma — 'kezzebe' + 'bi'd-dîn': 2MP yalanlar / 3MS soru öznesi + 2MS nesne", 'not': 'lemma eşi.'},
 {'bag': '39:36 → 95:8', 'kural': "okuma — harekesiz 'e-leyse'llâhu' + 'bi' + ad: 'bi-kâfin' / 'bi-ahkemi'l-hâkimîn'", 'not': 'kalıp eşi.'},
 {'bag': '11:45 → 95:8', 'kural': "okuma — lemma 'ahkem' korpusun iki geçişi, ikisinde de 'ahkemu'l-hâkimîn': 2MS hitapla dua / lafızla soru", 'not': 'lemma eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_tin', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in TIN]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_tin'] = TIN
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_tin', len(TIN), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_tin', len(BAGLAR['AS_tin']))
