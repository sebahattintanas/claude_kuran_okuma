# -*- coding: utf-8 -*-
"""aday_ekle_108_kevser.py — sûre 108 (Kevser) adayları (AX_kevser) ve okuma bağları (AS_kevser).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

KEVSER = [
]

BAGLAR = {"AS_kevser": [
 # blok 1-3
 {'bag': '107:7 → 108:1', 'kural': "okuma — ardışık sûre sınırı: esirgemeyle ('yemne'ûn') kapanış / vermeyle ('a'taynâ') açılış; fâsıla ن → ر; 107 lafızsız ve Rabsız, 108 Rab 1 (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '107:4 → 108:2', 'kural': "okuma — kök صلو ardışık iki sûrede: namaz kılanlara 'veyl' / 2MS'ye namaz emri", 'not': 'sınır ötesi eş.'},
 {'bag': '93:5 → 108:1', 'kural': "okuma — lemma 'a'tâ' + 2MS: Rab öznesi, gelecek / 1P öznesi, geçmiş", 'not': 'lemma eşi.'},
 {'bag': '87:15 → 108:2', 'kural': "okuma — lemma 'sallâ' + Rab: Rabbinin adını anıp namaz kılan / Rabbin için namaz kıl", 'not': 'lemma eşi.'},
 {'bag': '108:1 → 108:2', 'kural': "sûre içi — 1P konuşan / Rab 3. şahıs isimle (sahset kısmi örtüşme, iltifât 0); aynılık KAPATILAMAZ", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_kevser', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in KEVSER]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_kevser'] = KEVSER
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_kevser', len(KEVSER), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_kevser', len(BAGLAR['AS_kevser']))
