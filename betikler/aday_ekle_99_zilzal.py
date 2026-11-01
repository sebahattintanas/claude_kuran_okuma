# -*- coding: utf-8 -*-
"""aday_ekle_99_zilzal.py — sûre 99 (Zilzal) adayları (AX_zilzal) ve okuma bağları (AS_zilzal).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

ZILZAL = [
]

BAGLAR = {"AS_zilzal": [
 # blok 1-8
 {'bag': '98:8 → 99:1', 'kural': "okuma — ardışık sûre sınırı: Rabbinden korkana işaretle kapanış / 'izâ' şartıyla açılış; fâsıla ه → ا (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '33:11 → 99:1', 'kural': "okuma — lemma 'zilzâl' korpusun iki geçişi, ikisi de fiil + aynı kökten mastar: özne mü'minler, nekre + sıfat / özne yer, 3FS iyelikli", 'not': 'lemma eşi.'},
 {'bag': '22:1 → 99:1', 'kural': "okuma — kök زلزل: 'zelzelete's-sâ'a' ad / 'zulzilet … zilzâlehâ' fiil + mastar", 'not': 'kök eşi.'},
 {'bag': '56:4 → 99:1', 'kural': "okuma — iskelet 'izâ' + edilgen PERF 3FS + 'el-ard' + aynı kökten mastar: kök رجج / kök زلزل", 'not': 'kuruluş eşi.'},
 {'bag': '89:21 → 99:1', 'kural': "okuma — iskelet 'izâ' + edilgen PERF 3FS + 'el-ard' + mastar: kök دكك, mastar iki kez / kök زلزل, mastar iyelikli", 'not': 'kuruluş eşi.'},
 {'bag': '84:4 → 99:2', 'kural': "okuma — 'izâ' dizisinde yer içindekini veriyor: 've elqat mâ fîhâ' / 've exracet … esqâlehâ'", 'not': 'kuruluş eşi.'},
 {'bag': '16:7 → 99:2', 'kural': "okuma — lemma 'esqâl': hayvanların taşıdığı yükler / yerin ağırlıkları", 'not': 'lemma eşi.'},
 {'bag': '99:2 → 99:7', 'kural': "sûre içi — kök ثقل üç geçiş: 'esqâl' ağırlıklar / 'misqâl' ağırlık ölçüsü (99:7, 99:8)", 'not': 'sûre içi eş.'},
 {'bag': '99:3 → 99:4', 'kural': "sûre içi — insanın sorusu ('mâ lehâ') / yerin anlatması ('tuhaddisu axbârehâ')", 'not': 'sûre içi eş.'},
 {'bag': '93:11 → 99:4', 'kural': "okuma — lemma 'haddese': 2MS'ye emir, Rabbin nimeti / özne yer, kendi haberleri", 'not': 'lemma eşi.'},
 {'bag': '47:31 → 99:4', 'kural': "okuma — lemma 'axbâr': 2MP'nin haberleri sınanıyor / yer haberlerini anlatıyor", 'not': 'lemma eşi.'},
 {'bag': '16:68 → 99:5', 'kural': "okuma — Rab + lemma 'evhâ' + insan olmayan alıcı: bal arısı / yer", 'not': 'kuruluş eşi.'},
 {'bag': '41:12 → 99:5', 'kural': "okuma — lemma 'evhâ' + insan olmayan alıcı: her gök / yer", 'not': 'lemma eşi.'},
 {'bag': '99:4 → 99:6', 'kural': "sûre içi — 'yevme'izin' iki geçiş: yer anlatır / insanlar çıkar", 'not': 'sûre içi eş.'},
 {'bag': '24:61 → 99:6', 'kural': "okuma — lemma 'eştât' korpusun iki geçişi: toplu ya da ayrı yemek / insanların dağınık çıkışı", 'not': 'lemma eşi.'},
 {'bag': '99:6 → 99:7', 'kural': "sûre içi — kök رأي üç geçiş: 'li-yurav' edilgen gösterilme / 'yerahu' görme (99:7, 99:8); kök عمل üç geçiş", 'not': 'sûre içi eş.'},
 {'bag': '34:3 → 99:7', 'kural': "okuma — harekesiz 'misqâle zerra': O'ndan gizli kalmaz (bilgi) / amelin ölçüsü ve görülmesi", 'not': 'kalıp eşi.'},
 {'bag': '10:61 → 99:7', 'kural': "okuma — harekesiz 'misqâle zerra': Rabbinden gizli kalmaz / işleyen görür", 'not': 'kalıp eşi.'},
 {'bag': '21:47 → 99:7', 'kural': "okuma — lemma 'misqâl': 'misqâle habbetin min xardal' tartıda / 'misqâle zerra' amel ölçüsü", 'not': 'lemma eşi.'},
 {'bag': '99:7 → 99:8', 'kural': "sûre içi — aynı şart iskeleti (esit2 BENZER): 'xayran' / 'şerran' (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '98:7 → 99:7', 'kural': "okuma — ardışık sûre: 'xayru'l-beriyye' / 'xayran'; 98:6-7'de önce şerr sonra hayır, 99:7-8'de önce hayır sonra şerr (aday 1040, okuma)", 'not': 'ardışık sûre eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_zilzal', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in ZILZAL]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_zilzal'] = ZILZAL
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_zilzal', len(ZILZAL), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_zilzal', len(BAGLAR['AS_zilzal']))
