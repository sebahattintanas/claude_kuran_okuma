# -*- coding: utf-8 -*-
"""aday_ekle_110_nasr.py — sûre 110 (Nasr) adayları (AX_nasr) ve okuma bağları (AS_nasr).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

NASR = [
]

BAGLAR = {"AS_nasr": [
 # blok 1-3
 {'bag': '109:6 → 110:1', 'kural': "okuma — ardışık sûre sınırı: fiilsiz paralel isim cümlesiyle kapanış / 'izâ' şartıyla açılış; fâsıla ن → ح; 109 lafızsız ve Rabsız, 110 lafız 2 Rab 1 (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '109:6 → 110:2', 'kural': "okuma — ardışık sûre, kök دين: 'dînukum' / 'dîn' (2MP / 1S iyelik) → 'dîni'llâh' (aday 1040, okuma bağı)", 'not': 'kök eşi.'},
 {'bag': '61:13 → 110:1', 'kural': "okuma — xref 'nasr' + lafız + 'feth': nekre, 'mina'llâh', 'qarîb' / izâfet, belirli, 'izâ' şartı", 'not': 'kuruluş eşi.'},
 {'bag': '29:10 → 110:1', 'kural': "okuma — kalıp 'câ'e nasr' (korpusun iki geçişi): 'in' şartı, nekre, 'min rabbik' / 'izâ' şartı, lafza izâfet", 'not': 'kalıp eşi.'},
 {'bag': '12:76 → 110:2', 'kural': "okuma — kalıp 'fî dîn' (korpusun üç geçişi): 'dîni'l-melik' / 'dîni'llâh'", 'not': 'kalıp eşi.'},
 {'bag': '24:2 → 110:2', 'kural': "okuma — harekesiz 'fî dîni'llâh': ceza hükmünde acımama / insanların girişi", 'not': 'kalıp eşi.'},
 {'bag': '78:18 → 110:2', 'kural': "okuma — lemma 'fevc', hâl 'efwâcâ': sûra üfürüldüğü gün geliş (2MP) / dine giriş (3MP)", 'not': 'lemma eşi.'},
 {'bag': '15:98 → 110:3', 'kural': "okuma — kalıp 'fe-sebbih bi-hamdi rabbike' (korpusun iki geçişi): ardından secde emri / istiğfar emri", 'not': 'kalıp eşi.'},
 {'bag': '40:55 → 110:3', 'kural': "okuma — tesbih + istiğfar emirleri ters sırada: 'li-zenbike' ve vakitle / nesne Rab, vakitsiz", 'not': 'kuruluş eşi.'},
 {'bag': '42:5 → 110:3', 'kural': "okuma — xref 'sebbeha' + 'bi-hamdi rabb' + 'istaxfere' aynı sırada: IMPF 3MP melekler / IMPV 2MS", 'not': 'kuruluş eşi.'},
 {'bag': '9:118 → 110:3', 'kural': "okuma — lemma 'tevvâb': lafız + ayırma zamiri + belirli, 'er-rahîm' ile / nekre, 'kâne' haberi, tek başına", 'not': 'lemma eşi.'},
 {'bag': '110:1 → 110:3', 'kural': "sûre içi — 'izâ' şartı (110:1-2) → 'fe' ile cevap (okuma; ölçüm şart işaretlemiyor)", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_nasr', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in NASR]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_nasr'] = NASR
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_nasr', len(NASR), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_nasr', len(BAGLAR['AS_nasr']))
