# -*- coding: utf-8 -*-
"""aday_ekle_7_araf.py — sûre 7 (A'râf) adayları (AX_araf) ve okuma bağları (AS_araf).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1043'ten); betik sıranın kopmadığını doğrular.
"""
import json

ARAF = [
]

BAGLAR = {"AS_araf": [
 # blok 1-5
 {'bag': '21:14 → 7:5', 'kural': "okuma — harekesiz 'innâ kunnâ zâlimîn'; sayım 'say 7:5 10-12'; en uzun ortak lemma dizisi 'inne kâne zâlim' (dizi 7 5 10 12)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '21:46 → 7:5', 'kural': "okuma — harekesiz 'innâ kunnâ zâlimîn'; sayım 'say 7:5 10-12'; en uzun ortak lemma dizisi 'inne kâne zâlim' (dizi 7 5 10 12)", 'not': 'kalıp eşi (sayım).'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_araf', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in ARAF]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_araf'] = ARAF
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_araf', len(ARAF), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_araf', len(BAGLAR['AS_araf']))
