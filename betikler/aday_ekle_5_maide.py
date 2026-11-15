# -*- coding: utf-8 -*-
"""aday_ekle_5_maide.py — sûre 5 (Mâide) adayları (AX_maide) ve okuma bağları (AS_maide).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1043'ten); betik sıranın kopmadığını doğrular.
"""
import json

MAIDE = [
]

BAGLAR = {"AS_maide": [
 # blok 1-2
 {'bag': '22:28 → 5:1', 'kural': "okuma — harekesiz 'behîmetu'l-en'âm'", 'not': 'kalıp eşi; lemma behîme eşi.'},
 {'bag': '22:34 → 5:1', 'kural': "okuma — harekesiz 'behîmetu'l-en'âm'", 'not': 'kalıp eşi; lemma behîme eşi.'},
 {'bag': '22:30 → 5:1', 'kural': "okuma — harekesiz 'illâ mâ yutlâ 'aleykum'", 'not': 'kalıp eşi; lemma ehalle eşi.'},
 {'bag': '4:127 → 5:1', 'kural': "okuma — harekesiz 'yutlâ 'aleykum'", 'not': 'kalıp eşi.'},
 {'bag': '5:1 → 5:2', 'kural': "sûre içi — harekesiz 'yâ eyyuhe'llezîne âmenû'", 'not': 'blok içi kalıp eşi (ölçüm nakarat3); lemma ehalle eşi (izin / yasak).'},
 {'bag': '2:158 → 5:2', 'kural': "okuma — lemma 'şe'â'ir'", 'not': 'lemma eşi.'},
 {'bag': '22:32 → 5:2', 'kural': "okuma — lemma 'şe'â'ir'", 'not': 'lemma eşi.'},
 {'bag': '22:36 → 5:2', 'kural': "okuma — lemma 'şe'â'ir'", 'not': 'lemma eşi.'},
 {'bag': '2:194 → 5:2', 'kural': "okuma — harekesiz 'eş-şehra'l-harâm'", 'not': 'kalıp eşi.'},
 {'bag': '2:217 → 5:2', 'kural': "okuma — harekesiz 'eş-şehra'l-harâm'", 'not': 'kalıp eşi.'},
 {'bag': '2:196 → 5:2', 'kural': "okuma — lemma 'hedy'; harekesiz 'şedîdu'l-'iqâb'", 'not': 'lemma ve kalıp eşi.'},
 {'bag': '48:25 → 5:2', 'kural': "okuma — lemma 'hedy'; harekesiz ''ani'l-mescidi'l-harâm'", 'not': 'lemma ve kalıp eşi (ölçüm xref).'},
 {'bag': '2:198 → 5:2', 'kural': "okuma — lemma dizisi 'ibteğâ fadl min rabb'", 'not': 'lemma dizisi eşi (ölçüm xref).'},
 {'bag': '59:7 → 5:2', 'kural': "okuma — harekesiz 'inna'llâhe şedîdu'l-'iqâb'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '49:1 → 5:2', 'kural': "okuma — önek kesilmiş 've'ttequ'llâhe inna'llâh'", 'not': 'kalıp eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_maide', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in MAIDE]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_maide'] = MAIDE
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_maide', len(MAIDE), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_maide', len(BAGLAR['AS_maide']))
