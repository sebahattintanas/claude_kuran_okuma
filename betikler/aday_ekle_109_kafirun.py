# -*- coding: utf-8 -*-
"""aday_ekle_109_kafirun.py — sûre 109 (Kafirun) adayları (AX_kafirun) ve okuma bağları (AS_kafirun).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

KAFIRUN = [
]

BAGLAR = {"AS_kafirun": [
 # blok 1-6
 {'bag': '108:3 → 109:1', 'kural': "okuma — ardışık sûre sınırı: 2MS'ye hitapla kapanış / 2MS'ye 'qul' emriyle açılış; fâsıla ر → ن; 108 Rab 1, 109 lafızsız ve Rabsız (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '10:104 → 109:1', 'kural': "okuma — kalıp 'qul yâ eyyuhâ' + 'lâ a'budu' + 'ta'budûn' + kök دين: 'en-nâs' / 'el-kâfirûn'", 'not': 'kuruluş eşi.'},
 {'bag': '10:104 → 109:2', 'kural': "okuma — 'lâ a'budu' + ilgi + 'ta'budûn': 'ellezîne … min dûni'llâh' / 'mâ', tapılan adsız", 'not': 'kalıp eşi.'},
 {'bag': '43:81 → 109:4', 'kural': "okuma — 'qul' + 1S + lemma ''âbid': 'ene evvelu'l-'âbidîn' / 'ene 'âbidun'", 'not': 'lemma eşi.'},
 {'bag': '109:3 → 109:5', 'kural': "sûre içi — TAM tekrar (ölçüm esit2 1,0000; nakarat3 süzgeç GEÇER)", 'not': 'sûre içi eş.'},
 {'bag': '109:2 → 109:4', 'kural': "sûre içi — 1S → 2MP sırası: IMPF + IMPF / ortaç + PERF", 'not': 'sûre içi eş.'},
 {'bag': '107:1 → 109:6', 'kural': "okuma — kök دين iki sûre arayla: 'bi'd-dîn' yalanlanan / 'dînukum' — 'dîn'", 'not': 'kök eşi.'},
 {'bag': '10:104 → 109:6', 'kural': "okuma — 1S iyelikli 'dînî': şüphe edilen / sizin dininize karşı", 'not': 'kök eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_kafirun', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in KAFIRUN]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_kafirun'] = KAFIRUN
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_kafirun', len(KAFIRUN), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_kafirun', len(BAGLAR['AS_kafirun']))
