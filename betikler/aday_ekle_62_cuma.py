# -*- coding: utf-8 -*-
"""aday_ekle_62_cuma.py — sûre 62 (Cuma) adayları (AX_cuma) ve okuma bağları (AS_cuma).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

CUMA = [
]

BAGLAR = {"AS_cuma": [
 # blok 1-5
 {'bag': '61:14 → 62:1', 'kural': "okuma — ardışık sûre sınırı; inananların üstün gelmesiyle kapanış / tesbihle açılış; fâsıla ن → م (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '61:1 → 62:1', 'kural': "lemma dizisi + esit2 BENZER — 'sebbaha / yusebbihu li'llâhi mâ fi's-semâvâti ve mâ fi'l-ard'; ardışık sûre başları, PERF → IMPF (aday 1040, kayıt)", 'not': 'ardışık açılış.'},
 {'bag': '59:1 → 62:1', 'kural': "lemma dizisi + esit2 BENZER — aynı tesbih açılışı (4 ayet)", 'not': 'açılış eşi.'},
 {'bag': '59:23 → 62:1', 'kural': "lemma dizisi — 'el-melik + el-quddûs' (2 ayet): haber dizisi / lafza sıfat", 'not': 'ad dizisi eşi.'},
 {'bag': '61:9 → 62:2', 'kural': "okuma — 'huve'llezî ersele / be'ase' + elçi, ardışık sûreler (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '26:97 → 62:2', 'kural': "kalıp — 'lefî dalâlin mubîn' (5 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '12:8 → 62:2', 'kural': "kalıp — 'lefî dalâlin mubîn' (5 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '62:1 → 62:3', 'kural': "sûre içi — 'el-azîzi'l-hakîm' sıfat / 'huve'l-azîzu'l-hakîm' haber", 'not': 'sûre içi eş.'},
 {'bag': '62:2 → 62:3', 'kural': "okuma — 'âharîne minhum' 'fi'l-ummiyyîn'e atıf", 'not': 'sûre içi akış.'},
 {'bag': '62:1 → 62:2', 'kural': "sûre içi — kök حكم: 'el-hakîm' (Allah) / 'el-hikmeh' (öğretilen) (aday 1041, kayıt)", 'not': 'aynı kök iki gönderge.'},
 {'bag': '57:21 → 62:4', 'kural': "kalıp — 'zâlike fadlu'llâhi yu'tîhi men yeşâ' ve'llâhu zu'l-fadli'l-azîm' (2 ayet; 62:4'ün tamamı)", 'not': 'tam kalıp eşi.'},
 {'bag': '57:29 → 62:4', 'kural': "kalıp — 've'llâhu zu'l-fadli'l-azîm' (6 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '24:54 → 62:5', 'kural': "okuma — lemma 'hummile': yüklenen görev / yüklenen kitap", 'not': 'lemma eşi.'},
 {'bag': '16:8 → 62:5', 'kural': "okuma — lemma 'himâr': binek / yük taşıyan (teşbih)", 'not': 'lemma eşi.'},
 {'bag': '31:19 → 62:5', 'kural': "okuma — lemma 'himâr': ses benzetmesi / yük benzetmesi", 'not': 'lemma eşi.'},
 {'bag': '34:19 → 62:5', 'kural': "okuma — lemma 'esfâr' eşsesli: yolculuklar / kitaplar (924)", 'not': 'eşsesli.'},
 {'bag': '61:6 → 62:5', 'kural': "okuma — Tevrât, ardışık sûreler (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '61:7 → 62:5', 'kural': "kalıp — 've'llâhu lâ yehdi'l-qavme'z-zâlimîn' (6 ayet), ardışık sûrelerde aynı kapanış (aday 1040, kayıt)", 'not': 'ortak kapanış.'},
 # blok 6-11
 {'bag': '22:17 → 62:6', 'kural': "okuma — lemma 'hâde': sayılan gruplardan biri / nidâ ile muhatap", 'not': 'lemma eşi.'},
 {'bag': '62:5 → 62:6', 'kural': "okuma — Tevrât yüklenenler / 'ellezîne hâdû' (gönderge eşlenmedi)", 'not': 'sûre içi akış.'},
 {'bag': '62:6 → 62:7', 'kural': "sûre içi — kök مني: 'fe-temennev' / 'lâ yetemennevnehû ebeden' (aday 1039, kayıt)", 'not': 'sûre içi karşıt.'},
 {'bag': '9:47 → 62:7', 'kural': "kalıp — 've'llâhu alîmun bi'z-zâlimîn' (4 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '62:6 → 62:8', 'kural': "sûre içi — kök موت: dilenmeyen ölüm / kaçılan ölüm", 'not': 'sûre içi eş.'},
 {'bag': '33:16 → 62:8', 'kural': "okuma — lemma 'ferra' + 'el-mevt': ölümden kaçış fayda vermez", 'not': 'konu eşi.'},
 {'bag': '9:94 → 62:8', 'kural': "lemma dizisi + ölçüm xref — 'turaddûne ilâ âlimi'l-ğaybi ve'ş-şehâdeti fe-yunebbi'ukum bimâ kuntum ta'melûn' (3 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '9:105 → 62:8', 'kural': "lemma dizisi + ölçüm xref — aynı kalıp (3 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '59:22 → 62:8', 'kural': "lemma dizisi — 'âlim + ğayb + şehâde' (10 ayet)", 'not': 'ad eşi.'},
 {'bag': '24:37 → 62:9', 'kural': "okuma — 'ticâret' ve 'bey'' Allah'ı anmaktan oyalamaz / alışverişi bırakın", 'not': 'konu eşi.'},
 {'bag': '61:11 → 62:9', 'kural': "lemma dizisi — 'zâlikum hayrun lekum in kuntum ta'lemûn' (4 ayet), ardışık sûreler (aday 1040, kayıt)", 'not': 'ortak kapanış.'},
 {'bag': '62:7 → 62:9', 'kural': "sûre içi — kök علم: 'alîm' / 'âlim' (Allah) / 'ta'lemûn' (inananlar) (aday 1041, kayıt)", 'not': 'aynı kök iki özne.'},
 {'bag': '62:9 → 62:10', 'kural': "sûre içi — 'salât', 'zikr'; alışverişi bırakın / lütuf arayın (aday 1039, kayıt)", 'not': 'sûre içi akış.'},
 {'bag': '62:4 → 62:10', 'kural': "sûre içi — kök فضل (فضل [3/3] son)", 'not': 'sûre içi eş.'},
 {'bag': '30:20 → 62:10', 'kural': "okuma — lemma 'inteşere': yaratılıştan sonra yayılma / namazdan sonra dağılma", 'not': 'lemma eşi.'},
 {'bag': '61:10 → 62:11', 'kural': "okuma — lemma 'ticâret': azaptan kurtaran / koşulup gidilen; ardışık sûreler (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '57:20 → 62:11', 'kural': "okuma — lemma 'lehv'", 'not': 'lemma eşi.'},
 {'bag': '24:37 → 62:11', 'kural': "okuma — ticaretin oyalamadığı adamlar / ticarete dağılanlar", 'not': 'konu karşıtı.'},
 {'bag': '22:58 → 62:11', 'kural': "ölçüm xref — 'hayru'r-râziqîn' ('inne … le-huve' / 've'llâhu')", 'not': 'ortak kapanış.'},
 {'bag': '62:9 → 62:11', 'kural': "sûre içi — kök خير: 'hayrun lekum' / 'hayrun mine'l-lehv' / 'hayru'r-râziqîn'", 'not': 'sûre içi eş.'},
 {'bag': '62:1 → 62:11', 'kural': "okuma — sûre başı tesbih / sûre sonu 'hayru'r-râziqîn'; halka iddiası yok", 'not': 'sûre sınırları.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_cuma', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in CUMA]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_cuma'] = CUMA
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_cuma', len(CUMA), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_cuma', len(BAGLAR['AS_cuma']))
