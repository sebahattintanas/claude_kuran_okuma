# -*- coding: utf-8 -*-
"""aday_ekle_65_talak.py — sûre 65 (Talâk) adayları (AX_talak) ve okuma bağları (AS_talak).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

TALAK = [
]

BAGLAR = {"AS_talak": [
 # blok 1-3
 {'bag': '64:18 → 65:1', 'kural': "okuma — ardışık sûre sınırı; sıfat dizisiyle kapanış / nidâ ve hükümle açılış; fâsıla م → ا (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '64:16 → 65:1', 'kural': "okuma — sakınma emri 'fe'ttequ'llâh' / 've'ttequ'llâhe rabbekum'; ardışık sûreler (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '64:14 → 65:1', 'kural': "okuma — 'ezvâcikum' / 'en-nisâ'': eşlerden düşman olanlar / boşama hükmü; ardışık sûreler (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '33:1 → 65:1', 'kural': "lemma dizisi — 'yâ eyyuhe'n-nebiyy' (13 ayet)", 'not': 'açılış eşi.'},
 {'bag': '33:49 → 65:1', 'kural': "okuma — lemma 'tallaqa', 'idde': dokunmadan boşananlara iddet yok / iddet gözetilerek boşama", 'not': 'lemma eşi.'},
 {'bag': '9:36 → 65:1', 'kural': "okuma — lemma 'idde': ayların sayısı / boşananın iddeti", 'not': 'lemma eşi.'},
 {'bag': '33:30 → 65:1', 'kural': "ölçüm xref — 'ye'ti- bi-fâhişetin mubeyyineh'", 'not': 'xref.'},
 {'bag': '58:4 → 65:1', 'kural': "lemma dizisi — 've tilke hudûdu'llâh' (6 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '31:34 → 65:1', 'kural': "okuma — lemma 'tedrî': 've mâ tedrî nefsun' / 'lâ tedrî le'alla'llâh'", 'not': 'lemma eşi.'},
 {'bag': '58:3 → 65:2', 'kural': "lemma dizisi — 'zâlikum tû'azûne bihî' / 'zâlikum yû'azu bihî' (3 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '65:1 → 65:2', 'kural': "sûre içi — kök خرج: evden çıkarma / çıkma yasağı / 'mahracâ' (خرج [3/4])", 'not': 'sûre içi eş.'},
 {'bag': '59:2 → 65:3', 'kural': "okuma — 'min haysu lem yahtesibû' / 'min haysu lâ yahtesib': baskın / rızık", 'not': 'kalıp eşi.'},
 {'bag': '39:47 → 65:3', 'kural': "okuma — lemma 'ihtesebe' (3 ayet)", 'not': 'lemma eşi.'},
 {'bag': '64:13 → 65:3', 'kural': "okuma — tevekkül 'ale'llâhi fe'l-yetevekkel' / 'men yetevekkel ale'llâh'; ardışık sûreler (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '9:129 → 65:3', 'kural': "okuma — lemma 'hasb': 'hasbiya'llâh' / 'fe-huve hasbuh'", 'not': 'lemma eşi.'},
 {'bag': '54:49 → 65:3', 'kural': "okuma — 'kulle şey'in … bi-qader' / 'li-kulli şey'in qadrâ'; yaratma / koyma", 'not': 'konu eşi.'},
 {'bag': '65:2 → 65:3', 'kural': "sûre içi — şart cevabı sürüyor; kök بلغ insan / Allah (بلغ [2/2]; aday 1041, kayıt), جعل", 'not': 'sûre içi süreklilik.'},
 # blok 4-7
 {'bag': '60:13 → 65:4', 'kural': "okuma — lemma 'ye'ise': âhiretten / aybaşından umut kesme", 'not': 'lemma eşi.'},
 {'bag': '22:2 → 65:4', 'kural': "okuma — 'teda'u kullu zâti hamlin hamlehâ' / 'en yeda'ne hamlehunne': sarsıntı günü / iddet sonu", 'not': 'ifade eşi.'},
 {'bag': '18:88 → 65:4', 'kural': "lemma dizisi — 'min emr- yusrâ' (2 ayet): 1P / 3MS", 'not': 'kalıp eşi.'},
 {'bag': '65:2 → 65:4', 'kural': "nakarat3 GEÇER — 've men yetteqi'llâhe yec'al lehû': 'mahracâ' / 'min emrihî yusrâ'; kök أجل 'ecelehunne' ×2 (أجل [2/2])", 'not': 'sûre içi nakarat.'},
 {'bag': '65:1 → 65:4', 'kural': "sûre içi — lemma 'idde' 65:1 ×2 / 65:4", 'not': 'sûre içi eş.'},
 {'bag': '64:9 → 65:5', 'kural': "lemma dizisi — 'yukeffir anhu seyyi'âtihî' (12 ayet): bahçelere sokma / ödülü büyütme; ardışık sûreler (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '29:7 → 65:5', 'kural': "lemma dizisi — 'keffera + an + seyyi'e' (12 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '65:4 → 65:5', 'kural': "nakarat3 GEÇER — 've men yetteqi'llâh' (65:2, 4, 5): üç karşılık", 'not': 'sûre içi nakarat.'},
 {'bag': '22:2 → 65:6', 'kural': "okuma — lemma 'erda'a': emzirdiğini unutma / ücretli emzirme", 'not': 'lemma eşi.'},
 {'bag': '28:7 → 65:6', 'kural': "okuma — lemma 'erda'a': emzirme vahyi / ücretli emzirme", 'not': 'lemma eşi.'},
 {'bag': '28:20 → 65:6', 'kural': "okuma — lemma 'i'temere' (2 ayet): öldürmek için danışma / iyilikle danışma", 'not': 'lemma karşıtı.'},
 {'bag': '65:1 → 65:6', 'kural': "sûre içi — evden çıkarma yasağı / 'eskinûhunne' (oturtun)", 'not': 'sûre içi karşılık.'},
 {'bag': '65:4 → 65:6', 'kural': "sûre içi — 'en yeda'ne hamlehunne' / 'hattâ yeda'ne hamlehunne' (حمل [4/4], وضع [2/2])", 'not': 'sûre içi eş.'},
 {'bag': '65:5 → 65:6', 'kural': "sûre içi — kök أجر: Allah'ın ödülü / emzirenin ücreti (أجر [2/2]; aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '24:22 → 65:7', 'kural': "okuma — lemma 'se'a': 'ulu'l-fadli ve's-se'a' / 'zû se'a'", 'not': 'lemma eşi.'},
 {'bag': '23:62 → 65:7', 'kural': "okuma — lemma 'kellefe': 'lâ nukellifu nefsen illâ vus'ahâ' / 'lâ yukellifu'llâhu nefsen illâ mâ âtâhâ'", 'not': 'kalıp eşi.'},
 {'bag': '65:4 → 65:7', 'kural': "sûre içi — kök يسر: 'min emrihî yusrâ' / 'ba'de usrin yusrâ' (يسر [2/2])", 'not': 'sûre içi eş.'},
 {'bag': '65:6 → 65:7', 'kural': "sûre içi — kök عسر 'teâsertum' / 'usr'; نفق 'fe-enfiqû' / 'li-yunfiq' (نفق [3/3])", 'not': 'sûre içi eş.'},
 {'bag': '65:3 → 65:7', 'kural': "sûre içi — kök قدر: 'qadrâ' (ölçü) / 'qudira aleyhi' (daraltma); رزق 'yerzuqhu' / 'rizquh'", 'not': 'kök iki anlam.'},

 # blok 8-12
 {'bag': '47:13 → 65:8', 'kural': "lemma dizisi — 've ke-eyyin min qaryetin' (4 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '51:44 → 65:8', 'kural': "lemma dizisi + ölçüm xref — 'atev an emri rabbi-' (3 ayet): 3MP topluluk / 3FS kasaba", 'not': 'kalıp eşi.'},
 {'bag': '18:87 → 65:8', 'kural': "lemma dizisi + ölçüm xref — 'azzebe- azâben nukrâ' (2 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '65:3 → 65:8', 'kural': "sûre içi — kök حسب: 'yahtesib', 'hasbuh' / 'hâsebnâhâ hisâben' (حسب [4/4])", 'not': 'sûre içi eş.'},
 {'bag': '65:1 → 65:8', 'kural': "sûre içi — Rab: 'rabbekum' / 'rabbihâ' (ربب [2/2])", 'not': 'sûre içi eş.'},
 {'bag': '64:5 → 65:9', 'kural': "lemma dizisi — 'zâqa + vebâle emr-' (4 ayet): 3MP / 3FS; ardışık sûreler (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '59:15 → 65:9', 'kural': "lemma dizisi — 'zâqû vebâle emrihim' (4 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '65:8 → 65:9', 'kural': "sûre içi — 'emri rabbihâ' / 'emrihâ': Rab ve kasaba için aynı kelime (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '58:15 → 65:10', 'kural': "lemma dizisi + ölçüm xref — 'e'adda'llâhu lehum azâben şedîdâ' (2 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '65:1 → 65:10', 'kural': "sûre içi — kök وقي: 'ittequ' ile açılış / 'fe'ttequ'llâh' ile son bölüm (وقي [5/5]); عدد 'idde' / 'e'adde' (iki anlam)", 'not': 'sûre içi eş.'},
 {'bag': '65:8 → 65:10', 'kural': "sûre içi — kök عذب, شدد: 'hisâben şedîdâ', 'azâben nukrâ' / 'azâben şedîdâ' (عذب [3/3], شدد [2/2])", 'not': 'sûre içi eş.'},
 {'bag': '65:5 → 65:10', 'kural': "sûre içi — kök نزل: 'enzelehû ileykum' / 'enzela'llâhu ileykum'", 'not': 'sûre içi eş.'},
 {'bag': '57:9 → 65:11', 'kural': "lemma dizisi — 'li-yuhric- mine'z-zulumâti ile'n-nûr' (7 ayet): 2MP / 3MP", 'not': 'kalıp eşi.'},
 {'bag': '64:9 → 65:11', 'kural': "lemma dizisi + ölçüm xref — 've men yu'min bi'llâhi ve ya'mel sâlihan … yudhilhu cennâtin … ebedâ' (2 ayet): 'el-fevzu'l-azîm' / 'ahsena'llâhu lehû rizqâ'; ardışık sûreler (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '65:10 → 65:11', 'kural': "sûre içi — bedel: 'zikrâ' → 'rasûlen'", 'not': 'sûre içi süreklilik.'},
 {'bag': '65:1 → 65:11', 'kural': "sûre içi — kök خرج 'lâ tuhricûhunne' / 'li-yuhric' (خرج [4/4]); ظلم 'zaleme' / 'ez-zulumât' (iki anlam)", 'not': 'sûre içi eş.'},
 {'bag': '65:3 → 65:11', 'kural': "sûre içi — kök رزق: 'yerzuqhu' / 'rizqâ' (رزق [3/3])", 'not': 'sûre içi eş.'},
 {'bag': '41:12 → 65:12', 'kural': "lemma dizisi — 'seb'a semâvât' (5 ayet); 'evhâ fî kulli semâ'in emrahâ' / 'yetenezzelu'l-emru beynehunne'", 'not': 'kalıp eşi.'},
 {'bag': '17:44 → 65:12', 'kural': "okuma — lemma 'seb'': 'es-semâvâtu's-seb'u ve'l-ard'", 'not': 'lemma eşi.'},
 {'bag': '65:3 → 65:12', 'kural': "sûre içi — 'li-kulli şey'in qadrâ' / 'alâ kulli şey'in qadîr', 'bi-kulli şey'in ilmâ' (قدر [3/3], كلل [3/3], شيأ [3/3])", 'not': 'sûre içi eş.'},
 {'bag': '65:1 → 65:12', 'kural': "okuma — 'emr' ile açılış ('yuhdisu … emrâ') ve kapanış ('yetenezzelu'l-emr'); lemma 'emr' sûre içi 8 token; halka iddiası yok", 'not': 'sûre sınırları.'},

]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_talak', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in TALAK]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_talak'] = TALAK
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_talak', len(TALAK), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_talak', len(BAGLAR['AS_talak']))
