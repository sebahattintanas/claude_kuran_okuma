# -*- coding: utf-8 -*-
"""aday_ekle_104_humeze.py — sûre 104 (Humeze) adayları (AX_humeze) ve okuma bağları (AS_humeze).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

HUMEZE = [
]

BAGLAR = {"AS_humeze": [
 # blok 1-9
 {'bag': '103:3 → 104:1', 'kural': "okuma — ardışık sûre sınırı: istisna (iman edenler) ile kapanış / 'veyl' ile açılış; fâsıla ر → ة; 103 lafızsız ve Rabsız, 104 lafız 1 (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '45:7 → 104:1', 'kural': "okuma — kalıp 'veylun li-kulli' korpusun iki geçişi: 'kull' + iki nekre nitelik ('effâkin esîm' / 'humezetin lumeze')", 'not': 'kalıp eşi.'},
 {'bag': '68:11 → 104:1', 'kural': "okuma — kök همز: 'hemmâz' / 'humeze'", 'not': 'kök eşi.'},
 {'bag': '23:97 → 104:1', 'kural': "okuma — kök همز: şeytanların kışkırtmaları ('hemezât') / 'humeze'", 'not': 'kök eşi.'},
 {'bag': '90:5 → 104:3', 'kural': "okuma — kalıp 'yahsebu en(ne)': 'e-' sorusu + olumsuz 'ehad' / haber, mal öznesi", 'not': 'kalıp eşi.'},
 {'bag': '90:7 → 104:3', 'kural': "okuma — kalıp 'yahsebu en(ne)': 'e-' sorusu + olumsuz 'ehad' / haber, mal öznesi", 'not': 'kalıp eşi.'},
 {'bag': '104:3 → 104:4', 'kural': "sûre içi — sanı / 'kellâ' reddiyesi (ölçüm KELLA)", 'not': 'sûre içi eş.'},
 {'bag': '68:49 → 104:4', 'kural': "okuma — lemma 'nebeze' edilgen + 'le': şart cevabında gerçekleşmeyen atılma / tekitli gelecek", 'not': 'lemma eşi.'},
 {'bag': '104:4 → 104:5', 'kural': "sûre içi — lemma 'hutame' korpusun tamamı (iki geçiş, ardışık iki ayet)", 'not': 'sûre içi eş.'},
 {'bag': '69:3 → 104:5', 'kural': "okuma — kalıp 've mâ edrâke mâ' (ölçüm esit2 BENZER 0,8667)", 'not': 'kalıp eşi.'},
 {'bag': '101:10 → 104:5', 'kural': "okuma — kalıp 've mâ edrâke mâ'; ardından gelen ayet iki yerde de 'nâr' + sıfat (101:11 / 104:6)", 'not': 'kuruluş eşi.'},
 {'bag': '101:11 → 104:6', 'kural': "okuma — soruya cevap 'nâr' + sıfat: nekre 'hâmiye' / lafza izâfet + 'mûqade'", 'not': 'kuruluş eşi.'},
 {'bag': '85:5 → 104:6', 'kural': "okuma — kök وقد: 'en-nâri zâti'l-veqûd' / 'nâru'llâhi'l-mûqade'", 'not': 'kök eşi.'},
 {'bag': '104:6 → 104:7', 'kural': "sûre içi — dişil ilgi zamiri 'elletî' 'nâr'ı niteliyor", 'not': 'sûre içi eş.'},
 {'bag': '90:20 → 104:8', 'kural': "okuma — lemma 'mu'sade' korpusun iki geçişi, ikisinde de ''aleyhim' + 'mu'sade'", 'not': 'lemma eşi.'},
 {'bag': '31:10 → 104:9', 'kural': "okuma — lemma ''amed': göklerin direksiz yaratılması / uzatılmış direkler içinde", 'not': 'lemma eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_humeze', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in HUMEZE]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_humeze'] = HUMEZE
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_humeze', len(HUMEZE), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_humeze', len(BAGLAR['AS_humeze']))
