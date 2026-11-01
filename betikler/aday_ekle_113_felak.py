# -*- coding: utf-8 -*-
"""aday_ekle_113_felak.py — sûre 113 (Felak) adayları (AX_felak) ve okuma bağları (AS_felak).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

FELAK = [
]

BAGLAR = {"AS_felak": [
 # blok 1-5
 {'bag': '112:4 → 113:1', 'kural': "okuma — ardışık sûre sınırı: olumsuz isim cümlesiyle kapanış / 'qul' emriyle açılış; fâsıla د → ق; 112 lafız 2 Rab yok, 113 lafızsız Rab 1 (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '112:1 → 113:1', 'kural': "okuma — ardışık iki sûre 'qul' ile açılıyor: 'qul huve'llâhu ehad' / 'qul e'ûzu' (aday 1040, okuma bağı)", 'not': 'açılış eşi.'},
 {'bag': '40:27 → 113:1', 'kural': "okuma — xref 'e'ûzu' + 'bi-rabb': PERF 1S Mûsâ, 'rabbî ve rabbikum' / IMPF 1S söz içi, 'rabbi'l-feleq'", 'not': 'kuruluş eşi.'},
 {'bag': '23:97 → 113:1', 'kural': "okuma — 'qul' + 'e'ûzu': nidâ ile 2MS 'bike' + 'min hemezâti'ş-şeyâtîn' / 3. şahıs Rab tamlaması + 'min şerri' dizisi", 'not': 'kalıp eşi.'},
 {'bag': '72:6 → 113:1', 'kural': "okuma — lemma 'e'ûzu': sığınılan 'ricâl mine'l-cinn' / 'rabbi'l-feleq'", 'not': 'lemma eşi.'},
 {'bag': '26:63 → 113:1', 'kural': "okuma — kök فلق: denizin yarılması (fiil) / 'el-feleq' (ad, tarif edilmiyor)", 'not': 'kök eşi.'},
 {'bag': '70:20 → 113:2', 'kural': "okuma — lemma 'şerr': belirli, insana dokunan / 'min şerri' + tamlayan, sığınılan", 'not': 'lemma eşi.'},
 {'bag': '17:78 → 113:3', 'kural': "okuma — kök غسق: 'ğaseqi'l-leyl' (leyl ile tamlama) / nekre ortaç 'ğâsiq', adsız", 'not': 'kök eşi.'},
 {'bag': '20:27 → 113:4', 'kural': "okuma — lemma ''uqde': dildeki tekil düğüm, çözülmesi dilenen / belirli çoğul, üflenen", 'not': 'lemma eşi.'},
 {'bag': '48:15 → 113:5', 'kural': "okuma — lemma 'hasede': IMPF 2MP 'tahsudûnenâ' / PERF 3MS, ortaçla aynı kök", 'not': 'lemma eşi.'},
 {'bag': '113:3 → 113:5', 'kural': "sûre içi — aynı dizi: 'min şerri' + nekre ortaç + 'izâ' + PERF 3MS", 'not': 'sûre içi eş.'},
 {'bag': '113:2 → 113:5', 'kural': "sûre içi — 'min şerri' dört kez (kök شرر [4/4]): genel ilgi / üç adsız nitelik", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_felak', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in FELAK]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_felak'] = FELAK
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_felak', len(FELAK), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_felak', len(BAGLAR['AS_felak']))
