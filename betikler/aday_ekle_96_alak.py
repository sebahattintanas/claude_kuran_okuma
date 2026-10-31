# -*- coding: utf-8 -*-
"""aday_ekle_96_alak.py — sûre 96 (Alak) adayları (AX_alak) ve okuma bağları (AS_alak).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

ALAK = [
]

BAGLAR = {"AS_alak": [
 # blok 1-8
 {'bag': '95:8 → 96:1', 'kural': 'okuma — ardışık sûre sınırı: lafızla soru ile kapanış / Rab adıyla okuma emri ile açılış; fâsıla ن → ق (aday 1040, kayıt)', 'not': 'sınır eşi.'},
 {'bag': '69:52 → 96:1', 'kural': "okuma — harekesiz 'bi'smi rabbike': 'sebbih' + sıfat / 'iqra'' + 'ellezî xalaqa'", 'not': 'kalıp eşi.'},
 {'bag': '87:2 → 96:1', 'kural': "okuma — harekesiz 'ellezî xalaqa' Rab'dan sonra: 87:1-2 iki ayette / 96:1 tek ayette", 'not': 'kalıp eşi.'},
 {'bag': '96:1 → 96:2', 'kural': "sûre içi — lemma 'xalaqa' iki geçiş: nesnesiz / 'el-insân' + 'min 'alaq'", 'not': 'sûre içi eş.'},
 {'bag': '55:14 → 96:2', 'kural': "okuma — harekesiz 'xalaqa'l-insâne min': kuru balçık / ''alaq'", 'not': 'kalıp eşi.'},
 {'bag': '75:38 → 96:2', 'kural': "okuma — kök علق: tekil ''alaqa' aşama dizisinde / ''alaq' tek madde adı", 'not': 'kök eşi.'},
 {'bag': '96:1 → 96:3', 'kural': "sûre içi — 'iqra'' emri iki kez: Rab adıyla / Rab en cömert", 'not': 'sûre içi eş.'},
 {'bag': '49:13 → 96:3', 'kural': "okuma — lemma 'ekram' korpusun iki geçişi: insanların en değerlisi / Rabbin sıfatı (aday 1041, sûreler arası okuma notu)", 'not': 'lemma eşi.'},
 {'bag': '55:4 → 96:4', 'kural': "okuma — lemma ''alleme': 'el-beyân' nesnesiyle / 'bi'l-qalem' araçla", 'not': 'lemma eşi.'},
 {'bag': '68:1 → 96:4', 'kural': "okuma — lemma 'qalem': yemin edilen / öğretme aracı", 'not': 'lemma eşi.'},
 {'bag': '96:4 → 96:5', 'kural': "sûre içi — lemma ''alleme' iki geçiş: nesnesiz / 'el-insân' + 'mâ lem ya'lem'", 'not': 'sûre içi eş.'},
 {'bag': '79:17 → 96:6', 'kural': "okuma — lemma 'tağâ': PERF, ayette adı geçen kişi / IMPF, 'el-insân'", 'not': 'lemma eşi.'},
 {'bag': '80:5 → 96:7', 'kural': "okuma — lemma 'istağnâ' (korpusun dört geçişi okundu): 'emmâ meni'steğnâ' / 'en ra'âhu'steğnâ'", 'not': 'lemma eşi.'},
 {'bag': '92:8 → 96:7', 'kural': "okuma — lemma 'istağnâ': cimrilikle birlikte / azmanın gerekçesi", 'not': 'lemma eşi.'},
 {'bag': '53:42 → 96:8', 'kural': "okuma — 'enne / inne' + 'ilâ rabbike' + belirli fu'lâ ad: 'el-muntehâ' / 'er-ruc'â'", 'not': 'kalıp eşi.'},
 {'bag': '79:44 → 96:8', 'kural': "okuma — 'ilâ rabbike' + varış adı: 'muntehâhâ' / 'er-ruc'â'", 'not': 'kalıp eşi.'},
 # blok 9-19
 {'bag': '25:43 → 96:9', 'kural': "okuma — harekesiz 'e-ra'eyte': 'men' + PERF / 'ellezî' + IMPF", 'not': 'kalıp eşi.'},
 {'bag': '79:40 → 96:9', 'kural': "okuma — lemma 'nehâ': kendi nefsini engelleyen / başkasını engelleyen", 'not': 'lemma eşi.'},
 {'bag': '75:31 → 96:10', 'kural': "okuma — lemma 'sallâ': kılmayan / kılan ve engellenen", 'not': 'lemma eşi.'},
 {'bag': '96:9 → 96:13', 'kural': "sûre içi — harekesiz 'e-ra'eyte' üç geçiş: 96:9, 96:11, 96:13", 'not': 'sûre içi eş.'},
 {'bag': '20:48 → 96:13', 'kural': "okuma — harekesiz 'kezzebe ve tevellâ': korpusun dört geçişi okundu", 'not': 'kalıp eşi.'},
 {'bag': '75:32 → 96:13', 'kural': "okuma — harekesiz 'kezzebe ve tevellâ'; 75:31-32 'sallâ' + 'kezzebe ve tevellâ' ardışık / 96:10 ve 96:13", 'not': 'kalıp eşi.'},
 {'bag': '92:16 → 96:13', 'kural': "okuma — harekesiz 'kezzebe ve tevellâ': 'ellezî' ile / 'e-ra'eyte in' ile", 'not': 'kalıp eşi.'},
 {'bag': '96:11 → 96:13', 'kural': "sûre içi — iki 'e-ra'eyte in' şartı: doğru yol, sakınma / yalanlama, yüz çevirme (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '9:78 → 96:14', 'kural': "okuma — harekesiz 'e-lem ya'lem' + 'enne'llâhe': Allah bilir / Allah görür", 'not': 'kalıp eşi.'},
 {'bag': '96:5 → 96:14', 'kural': "sûre içi — 'lem ya'lem' dizisi iki ayette: insanın bilmediği / bilmedi mi", 'not': 'sûre içi eş.'},
 {'bag': '96:7 → 96:14', 'kural': "sûre içi — lemma 'ra'â': öznesi insan / öznesi Allah (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '96:9 → 96:15', 'kural': "sûre içi — kök نهي iki geçiş: 'yenhâ' / 'yentehi'", 'not': 'sûre içi eş.'},
 {'bag': '11:56 → 96:15', 'kural': "okuma — lemma 'nâsiye': her canlının perçemi O'nun elinde / tehdit; korpusun üç geçişi okundu", 'not': 'lemma eşi.'},
 {'bag': '55:41 → 96:15', 'kural': 'okuma — kök نصي: edilgen yakalama / 1P etken; korpusun dört geçişi okundu', 'not': 'kök eşi.'},
 {'bag': '68:16 → 96:15', 'kural': 'okuma — 1P gelecek / tekit + yüzdeki uzuv: burun / perçem', 'not': 'kuruluş eşi.'},
 {'bag': '96:13 → 96:16', 'kural': "sûre içi — kök كذب iki geçiş: 'kezzebe' / 'kâdhibe'", 'not': 'sûre içi eş.'},
 {'bag': '69:9 → 96:16', 'kural': "okuma — lemma 'xâti'e' korpusun iki geçişi: belirli ad / nekre sıfat", 'not': 'lemma eşi.'},
 {'bag': '29:29 → 96:17', 'kural': "okuma — lemma 'nâdî' korpusun iki geçişi: toplantı yeri / çağrılacak meclis", 'not': 'lemma eşi.'},
 {'bag': '96:17 → 96:18', 'kural': "sûre içi — lemma 'de'â' iki geçiş: 3MS emir / 1P gelecek (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '96:15 → 96:18', 'kural': "sûre içi — konuşan 1P iki geçiş: 'le-nesfa'an' / 'se-ned'u'", 'not': 'sûre içi eş.'},
 {'bag': '68:8 → 96:19', 'kural': "okuma — 'lâ tuti'': yalanlayanlar / 3MS (96:13 'kezzebe' sonrası)", 'not': 'kalıp eşi.'},
 {'bag': '84:21 → 96:19', 'kural': "okuma — lemma 'secede', ikisi de secde işaretli: olumsuz 3MP / emir 2MS", 'not': 'lemma eşi.'},
 {'bag': '96:6 → 96:19', 'kural': "sûre içi — 'kellâ' üç geçiş: 96:6, 96:15, 96:19", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_alak', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in ALAK]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_alak'] = ALAK
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_alak', len(ALAK), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_alak', len(BAGLAR['AS_alak']))
