# -*- coding: utf-8 -*-
"""aday_ekle_111_mesed.py — sûre 111 (Mesed) adayları (AX_mesed) ve okuma bağları (AS_mesed).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

MESED = [
]

BAGLAR = {"AS_mesed": [
 # blok 1-5
 {'bag': '110:3 → 111:1', 'kural': "okuma — ardışık sûre sınırı: Rabbin 'tevvâb' sıfatıyla kapanış / PERF 3FS 'tebbet' ile açılış; fâsıla ا → ب; 110 lafız 2 Rab 1, 111 lafızsız ve Rabsız (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '11:101 → 111:1', 'kural': "okuma — kök تبب: 'tetbîb' ilâhların katmadığı yıkım / 'tebbet', 'tebb'; korpusun üç ayetinin ikisi", 'not': 'kök eşi.'},
 {'bag': '77:31 → 111:1', 'kural': "okuma — lemma 'leheb' (korpusun üç geçişi okundu): alevden korumama / künye", 'not': 'lemma eşi.'},
 {'bag': '69:28 → 111:2', 'kural': "okuma — kalıp 'mâ ağnâ' + 'an' + mal: 1S 'mâliyeh' / 3MS 'mâluhû'", 'not': 'kalıp eşi.'},
 {'bag': '92:11 → 111:2', 'kural': "okuma — harekesiz ''anhu mâluhû' (korpusun iki geçişi): IMPF 'yuğnî' + 'izâ teraddâ' / PERF 'ağnâ' + 've mâ keseb'", 'not': 'kalıp eşi.'},
 {'bag': '15:84 → 111:2', 'kural': "okuma — 'ağnâ' + 'kesebe' tek ayette: kazanılan tek özne, 3MP / mal ve kazanılan iki özne, 3MS", 'not': 'kuruluş eşi.'},
 {'bag': '88:4 → 111:3', 'kural': "okuma — lemma 'yaslâ' + nekre 'nâran' + nitelik: 3FS 'hâmiye' / 3MS 'se-' + 'zâte leheb'", 'not': 'kuruluş eşi.'},
 {'bag': '85:5 → 111:3', 'kural': "okuma — 'nâr' + 'zât' + ad: belirli GEN 'zâti'l-veqûd' / nekre ACC 'zâte leheb'", 'not': 'kuruluş eşi.'},
 {'bag': '111:1 → 111:3', 'kural': "sûre içi — lemma 'leheb' iki geçiş: künye / ateşin niteliği", 'not': 'sûre içi eş.'},
 {'bag': '77:31 → 111:3', 'kural': "okuma — kök غني + 'leheb': tek ayette / ardışık iki ayette (111:2-3)", 'not': 'kuruluş eşi.'},
 {'bag': '72:15 → 111:4', 'kural': "okuma — lemma 'hatab' (korpusun iki geçişi okundu): sapanlar cehenneme odun / odun taşıyıcısı", 'not': 'lemma eşi.'},
 {'bag': '66:10 → 111:4', 'kural': "okuma — lemma 'imra'at' + kocaya izâfet, ateş bağlamı: 'imra'ete nûhin ve'mra'ete lût' / 'imra'atuhû'", 'not': 'lemma eşi.'},
 {'bag': '50:16 → 111:5', 'kural': "okuma — lemma 'habl': 'habli'l-verîd' damar / 'hablun min mesed' ip", 'not': 'lemma eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_mesed', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in MESED]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_mesed'] = MESED
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_mesed', len(MESED), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_mesed', len(BAGLAR['AS_mesed']))
