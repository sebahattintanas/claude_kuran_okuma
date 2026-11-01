# -*- coding: utf-8 -*-
"""aday_ekle_106_kureys.py — sûre 106 (Kureys) adayları (AX_kureys) ve okuma bağları (AS_kureys).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

KUREYS = [
]

BAGLAR = {"AS_kureys": [
 # blok 1-4
 {'bag': '105:5 → 106:1', 'kural': "okuma — ardışık sûre sınırı: teşbihle kapanış / fiilsiz 'li-' öbeğiyle açılış; fâsıla ل → ش; iki sûre de lafız 0, Rab 1; öbeğin bağlanması KAPATILAMAZ (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '106:1 → 106:2', 'kural': "sûre içi — lemma 'îlâf' korpusun tamamı (iki geçiş, ardışık iki ayet), ikincisi 3MP zamirle", 'not': 'sûre içi eş.'},
 {'bag': '93:1 → 106:2', 'kural': "okuma — adlı zaman: yemin edilen vakit / yolculuğun mevsimleri (çıpa L0 emsali)", 'not': 'kuruluş eşi.'},
 {'bag': '106:1 → 106:3', 'kural': "sûre içi — fiilsiz 'li-' öbeği / 'fe' + emir; bağlanma KAPATILAMAZ", 'not': 'sûre içi eş.'},
 {'bag': '27:91 → 106:3', 'kural': "okuma — kulluk + Rab + işaret + yer + 'ellezî': 'rabbe hâzihi'l-belde' / 'rabbe hâze'l-beyt' (106:4 'ellezî')", 'not': 'kuruluş eşi.'},
 {'bag': '106:3 → 106:4', 'kural': "sûre içi — 'ellezî' 'rabb'ı niteliyor", 'not': 'sûre içi eş.'},
 {'bag': '88:7 → 106:4', 'kural': "okuma — kalıp 'min cû'' korpusun iki geçişi: açlıktan korumayan / açlıktan doyuran", 'not': 'kalıp eşi.'},
 {'bag': '16:112 → 106:4', 'kural': "okuma — 'cû'' ve 'xavf' birlikte: tattırılan / kurtarılan", 'not': 'lemma eşi.'},
 {'bag': '103:3 → 106:4', 'kural': "okuma — lemma 'âmene' (eşsesli): insanlar iman etti / Rab güvene kavuşturdu (aday 1041, sûreler arası okuma notu)", 'not': 'lemma eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_kureys', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in KUREYS]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_kureys'] = KUREYS
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_kureys', len(KUREYS), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_kureys', len(BAGLAR['AS_kureys']))
