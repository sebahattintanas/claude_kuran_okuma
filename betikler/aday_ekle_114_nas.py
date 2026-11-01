# -*- coding: utf-8 -*-
"""aday_ekle_114_nas.py — sûre 114 (Nas) adayları (AX_nas) ve okuma bağları (AS_nas).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

NAS = [
]

BAGLAR = {"AS_nas": [
 # blok 1-6
 {'bag': '113:5 → 114:1', 'kural': "okuma — ardışık sûre sınırı: haset öbeğiyle kapanış / 'qul e'ûzu bi-rabbi'n-nâs' ile açılış; fâsıla د → س; iki sûre de lafızsız, Rab 1 (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '113:1 → 114:1', 'kural': "okuma — harekesiz 'qul e'ûzu bi-rabb' (korpusun iki geçişi), iki ardışık sûrenin ilk ayeti: 'el-feleq' / 'en-nâs' (aday 1040, okuma bağı)", 'not': 'açılış eşi.'},
 {'bag': '113:2 → 114:4', 'kural': "okuma — ardışık sûrede 'min şerri' + tamlayan: dört öbek / tek öbek, iki sıfatlı belirli ad (aday 1040, okuma bağı)", 'not': 'kuruluş eşi.'},
 {'bag': '20:114 → 114:2', 'kural': "okuma — lemma 'melik': lafzın sıfatı, belirli / 'en-nâs' tamlaması", 'not': 'lemma eşi.'},
 {'bag': '12:43 → 114:2', 'kural': "okuma — lemma 'melik' insan için (kral) / Allah için (aday 1041 ailesi, sûreler arası okuma notu)", 'not': 'lemma eşi.'},
 {'bag': '11:101 → 114:3', 'kural': "okuma — lemma 'ilâh': yakarılan ilâhlar ('âlihetuhum') / 'ilâhi'n-nâs' (sûreler arası okuma notu)", 'not': 'lemma eşi.'},
 {'bag': '81:15 → 114:4', 'kural': "okuma — kök خنس (korpusun iki geçişi okundu): yemin edilen sinenler / 'el-xannâs' sıfat", 'not': 'kök eşi.'},
 {'bag': '20:120 → 114:5', 'kural': "okuma — lemma 'vesvese': özne adlı, 'ileyhi' / özne ilgi zamiri, 'fî sudûri'n-nâs'", 'not': 'lemma eşi.'},
 {'bag': '50:16 → 114:5', 'kural': "okuma — lemma 'vesvese': özne nefs, 'bihî' / göğüslerde", 'not': 'lemma eşi.'},
 {'bag': '11:119 → 114:6', 'kural': "okuma — harekesiz 'mine'l-cinneti ve'n-nâs' (korpusun üç geçişi okundu): cehennemi dolduracaklar, 'ecma'în' ile / vesvesecinin ya da insanların açıklaması", 'not': 'kalıp eşi.'},
 {'bag': '114:1 → 114:3', 'kural': "sûre içi — üç atıfsız tamlama, aynı iskelet ad + 'en-nâs': Rab, Melik, İlâh", 'not': 'sûre içi eş.'},
 {'bag': '114:4 → 114:5', 'kural': "sûre içi — kök وسوس [2/2]: ad 'el-vesvâs' / fiil 'yuvesvisu'", 'not': 'sûre içi eş.'},
 {'bag': '114:1 → 114:6', 'kural': "sûre içi — lemma 'nâs' beş geçiş [5/5]: tamlayan (114:1-3), göğüslerine vesvese verilenler (114:5), cinlerle birlikte (114:6)", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_nas', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in NAS]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_nas'] = NAS
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_nas', len(NAS), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_nas', len(BAGLAR['AS_nas']))
