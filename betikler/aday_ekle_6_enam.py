# -*- coding: utf-8 -*-
"""aday_ekle_6_enam.py — sûre 6 (En'âm) adayları (AX_enam) ve okuma bağları (AS_enam).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1043'ten); betik sıranın kopmadığını doğrular.
"""
import json

ENAM = [
]

BAGLAR = {"AS_enam": [
 # blok 1-5
 {'bag': '36:46 → 6:4', 'kural': "okuma — harekesiz 'âyetin min âyâti rabbihim'", 'not': 'kalıp eşi (sayım); esit2 YAKIN.'},
 {'bag': '50:5 → 6:5', 'kural': "okuma — harekesiz 'kezzebû bi'l-haqq'", 'not': 'kalıp eşi (sayım); ölçüm xref.'},
 {'bag': '26:6 → 6:5', 'kural': "okuma — harekesiz 'mâ kânû bihî yestehzi'ûn'", 'not': 'kalıp eşi (sayım); ölçüm xref.'},
 # blok 6-11
 {'bag': '36:31 → 6:6', 'kural': "okuma — harekesiz 'e-lem yerav kem ehleknâ'", 'not': 'kalıp eşi (sayım); ölçüm xref.'},
 {'bag': '5:110 → 6:7', 'kural': "okuma — harekesiz 'in hâzâ illâ sihrun mubîn'", 'not': 'kalıp eşi (sayım); ölçüm xref; sûre 5 okumasında basılmış.'},
 {'bag': '21:41 → 6:10', 'kural': "okuma — harekesiz 'bi-rusulin min qablik'", 'not': 'kalıp eşi (sayım); esit2 YAKIN.'},
 {'bag': '27:69 → 6:11', 'kural': "okuma — harekesiz 'qul sîrû fi'l-ard'", 'not': 'kalıp eşi (sayım); esit2 BENZER.'},
 # blok 12-15
 {'bag': '4:87 → 6:12', 'kural': "okuma — harekesiz 'le-yecma'annekum ilâ yevmi'l-qiyâmeti lâ raybe fîh'", 'not': 'kalıp eşi (sayım); ölçüm xref.'},
 {'bag': '39:13 → 6:15', 'kural': "okuma — harekesiz 'qul innî exâfu in 'aseytu rabbî 'azâbe yevmin 'azîm'", 'not': 'kalıp eşi (sayım); esit2 TAM.'},
 # blok 16-19
 {'bag': '40:9 → 6:16', 'kural': "okuma — ölçüm xref (يوم رحم فوز); lemma dizisi eşi 'dizi 6 16 4 7'", 'not': 'zamir eki farkı; harekesiz eş yok.'},
 {'bag': '10:107 → 6:17', 'kural': "okuma — harekesiz 've in yemseske'llâhu bi-durr'", 'not': 'kalıp eşi (sayım); ölçüm xref.'},
 {'bag': '3:18 → 6:19', 'kural': "okuma — ölçüm xref (شهد اللّه إله); kök شهد ve lafız", 'not': 'ölçüm xref (شهد اللّه إله).'},
 # blok 20-24
 {'bag': '2:146 → 6:20', 'kural': "okuma — harekesiz 'ya'rifûnehû kemâ ya'rifûne ebnâ'ehum'", 'not': 'kalıp eşi (sayım); ölçüm xref.'},
 {'bag': '11:21 → 6:20', 'kural': "okuma — harekesiz 'xasirû enfusehum'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '10:17 → 6:21', 'kural': "okuma — harekesiz 'ev kezzebe bi-âyâtih'", 'not': 'kalıp eşi (sayım); ölçüm xref ve esit2 BENZER.'},
 {'bag': '10:28 → 6:22', 'kural': "okuma — harekesiz 've yevme nahşuruhum cemî'an'", 'not': 'kalıp eşi (sayım); ölçüm xref.'},
 {'bag': '11:21 → 6:24', 'kural': "okuma — harekesiz 'mâ kânû yefterûn'", 'not': 'kalıp eşi (sayım); ölçüm xref.'},
 # blok 25-28
 {'bag': '17:46 → 6:25', 'kural': "okuma — harekesiz 've fî âzânihim vaqrâ'", 'not': 'kalıp eşi (sayım); ölçüm xref.'},
 # blok 29-32
 {'bag': '46:34 → 6:30', 'kural': "okuma — harekesiz 'eleyse hâzâ bi'l-haqq'", 'not': 'kalıp eşi (sayım); ölçüm xref.'},
 {'bag': '10:45 → 6:31', 'kural': "okuma — harekesiz 'kezzebû bi-liqâ'i'llâh'", 'not': 'kalıp eşi (sayım); ölçüm xref.'},
 {'bag': '47:36 → 6:32', 'kural': "okuma — harekesiz 'la'ibun ve lahv'", 'not': 'kalıp eşi (sayım); ölçüm xref.'},
 # blok 33-36
 {'bag': '40:63 → 6:33', 'kural': "okuma — harekesiz 'bi-âyâti'llâhi yechadûn'", 'not': 'kalıp eşi (sayım); ölçüm xref.'},
 {'bag': '35:4 → 6:34', 'kural': "okuma — harekesiz 'kuzzibet rusulun min qablik'", 'not': 'kalıp eşi (sayım); ölçüm xref.'},
 # blok 37-41
 {'bag': '13:7 → 6:37', 'kural': "okuma — harekesiz 'âyetun min rabbih'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '11:6 → 6:38', 'kural': "okuma — harekesiz 'dâbbetin fi'l-ard'", 'not': 'kalıp eşi (sayım).'},
 # blok 42-45
 {'bag': '16:63 → 6:42', 'kural': "okuma — harekesiz 'ilâ umemin min qablik'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '37:182 → 6:45', 'kural': "okuma — harekesiz 've'l-hamdu li'llâhi rabbi'l-'âlemîn'", 'not': 'kalıp eşi (sayım).'},
 # blok 46-49
 {'bag': '28:71 → 6:46', 'kural': "okuma — harekesiz 'men ilâhun ğayru'llâhi ye'tîkum'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '18:56 → 6:48', 'kural': "okuma — harekesiz 've mâ nursilu'l-murselîne illâ mubeşşirîne ve munzirîn'", 'not': 'kalıp eşi (sayım).'},
 # blok 50-53
 {'bag': '11:31 → 6:50', 'kural': "okuma — harekesiz ''indî xazâ'inu'llâh'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '18:28 → 6:52', 'kural': "okuma — harekesiz 'llezîne yed'ûne rabbehum bi'l-ğadâti ve'l-'aşiyyi yurîdûne vechehû'", 'not': 'kalıp eşi (sayım).'},
 # blok 54-58
 {'bag': '16:119 → 6:54', 'kural': "okuma — ölçüm xref (سوء جهالة تاب); lemma dizisi eşi 'dizi 6 54 18 23'", 'not': "fiil çekimi farkı; önek kesilmiş eş 'ğafûrun rahîm' (sayım: 'say 6:54 26-27 --on')."},
 {'bag': '40:66 → 6:56', 'kural': "okuma — harekesiz 'qul innî nuhîtu en a'bude'llezîne ted'ûne min dûni'llâh'", 'not': 'kalıp eşi (sayım); ölçüm xref.'},
 # blok 59-61
 {'bag': '10:61 → 6:59', 'kural': "okuma — harekesiz 'illâ fî kitâbin mubîn'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '23:99 → 6:61', 'kural': "okuma — harekesiz 'hattâ izâ câ'e'; ölçüm xref (جاء أحد موت); lemma dizisi eşi 'dizi 6 61 8 12'", 'not': 'zamir eki farkı.'},
 # blok 62-67
 {'bag': '10:30 → 6:62', 'kural': "okuma — harekesiz 'ile'llâhi mevlâhumu'l-haqq'; ölçüm xref (ردّ اللّه مولى حقّ); lemma dizisi eşi 'dizi 6 62 2 6'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '10:22 → 6:63', 'kural': "okuma — harekesiz 'le-nekûnenne mine'ş-şâkirîn'; ölçüm xref (أنجى كان شاكر); lemma dizisi eşi 'dizi 6 63 11 17'", 'not': 'zamir eki farkı.'},
 # blok 68-70
 {'bag': '4:140 → 6:68', 'kural': "okuma — harekesiz 'hattâ yaxûdû fî hadîsin ğayrih'; ölçüm xref (خاض حديث غير)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '10:4 → 6:70', 'kural': "okuma — harekesiz 'şarâbun min hamîmin ve 'azâbun alîm'; ölçüm xref (شراب حميم عذاب); lemma dizisi eşi 'dizi 6 70 38 42'", 'not': 'kalıp eşi (sayım).'},
 # blok 71-73
 {'bag': '2:120 → 6:71', 'kural': "okuma — harekesiz 'inne hude'llâhi huve'l-hudâ'; ölçüm xref (قال هدى اللّه)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '10:106 → 6:71', 'kural': "okuma — ölçüm xref (اللّه نفع يضرّ); lemma dizisi eşi 'dizi 6 71 6 10'", 'not': 'lemma dizisi eşi (sayım).'},
 # blok 74-78
 {'bag': '43:26 → 6:74', 'kural': "okuma — harekesiz 've iz qâle ibrâhîmu li-ebîh'; sayım 'say 6:74 1-4'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '11:54 → 6:78', 'kural': "okuma — harekesiz 'berî'un mimmâ tuşrikûn'; sayım 'say 6:78 15-17'", 'not': 'kalıp eşi (sayım).'},
 # blok 79-83
 {'bag': '3:151 → 6:81', 'kural': "okuma — harekesiz 'bi'llâhi mâ lem yunezzil'; sayım 'say 6:81 9-12'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '12:76 → 6:83', 'kural': "okuma — harekesiz 'nerfe'u deracâtin men neşâ'u'; sayım 'say 6:83 7-10'", 'not': 'kalıp eşi (sayım).'},
 # blok 84-90
 {'bag': '21:72 → 6:84', 'kural': "okuma — harekesiz 've vehebnâ lehû ishâqa ve ya'qûbe'; sayım 'say 6:84 1-4'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '39:23 → 6:88', 'kural': "okuma — harekesiz 'zâlike hude'llâhi yehdî bihî men yeşâ'u'; sayım 'say 6:88 1-7'", 'not': 'kalıp eşi (sayım).'},
 # blok 91-92
 {'bag': '22:74 → 6:91', 'kural': "okuma — harekesiz 'qaderu'llâhe haqqa qadrihî'; sayım 'say 6:91 2-5'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '42:7 → 6:92', 'kural': "okuma — harekesiz 'umme'l-qurâ ve men havlehâ'; sayım 'say 6:92 10-13'", 'not': 'kalıp eşi (sayım).'},
 # blok 93-94
 {'bag': '46:20 → 6:93', 'kural': "okuma — harekesiz 'tuczevne 'azâbe'l-hûni'; sayım 'say 6:93 36-38'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '18:48 → 6:94', 'kural': "okuma — harekesiz 'kemâ xalaqnâkum'; sayım 'say 6:94 4-5'", 'not': 'kalıp eşi (sayım).'},
 # blok 95-99
 {'bag': '36:38 → 6:96', 'kural': "okuma — harekesiz 'zâlike taqdîru'l-'azîzi'l-'alîm'; sayım 'say 6:96 9-12'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '27:63 → 6:97', 'kural': "okuma — harekesiz 'zulumâti'l-berri ve'l-bahr'; sayım 'say 6:97 9-11'", 'not': 'kalıp eşi (sayım).'},
 # blok 100-103
 {'bag': '2:117 → 6:101', 'kural': "okuma — harekesiz 'bedî'u's-semâvâti ve'l-ard'; sayım 'say 6:101 1-3'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '39:62 → 6:102', 'kural': "okuma — harekesiz 'xâliqu kulli şey'in'; sayım 'say 6:102 8-10'", 'not': 'kalıp eşi (sayım).'},
 # blok 104-108
 {'bag': '33:2 → 6:106', 'kural': "okuma — ölçüm xref (اتّبع أوحى ربّ); lemma dizisi eşi 'dizi 6 106 1 6'", 'not': 'kalıp eşi (sayım); fiil çekimi farkı.'},
 {'bag': '39:7 → 6:108', 'kural': "okuma — ölçüm xref (ربّ مرجع نبّأ); lemma dizisi eşi 'dizi 6 108 18 25'", 'not': 'kalıp eşi (sayım); zamir eki farkı.'},
 # blok 109-113
 {'bag': '35:42 → 6:109', 'kural': "okuma — harekesiz 've aqsemû bi'llâhi cehde eymânihim'; sayım 'say 6:109 1-4'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '25:31 → 6:112', 'kural': "okuma — harekesiz 've kezâlike ce'alnâ li-kulli nebiyyin 'aduvven'; sayım 'say 6:112 1-5'", 'not': 'kalıp eşi (sayım).'},
 # blok 114-117
 {'bag': '10:66 → 6:116', 'kural': "okuma — harekesiz 'in yettebi'ûne illa'z-zanne ve in hum illâ yaxrusûn'; sayım 'say 6:116 11-18'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '16:125 → 6:117', 'kural': "okuma — ölçüm xref (سبيل أعلم مهتدي); lemma dizisi eşi 'dizi 6 117 1 11'", 'not': 'kalıp eşi (sayım); önek farkı.'},
 {'bag': '68:7 → 6:117', 'kural': "okuma — ölçüm xref (سبيل أعلم مهتدي); lemma dizisi eşi 'dizi 6 117 1 11'", 'not': 'kalıp eşi (sayım); önek farkı.'},
 # blok 118-121
 {'bag': '53:30 → 6:119', 'kural': "okuma — harekesiz 'inne rabbeke huve a'lemu'; sayım 'say 6:119 26-29'", 'not': 'kalıp eşi (sayım).'},
 # blok 122-125
 {'bag': '28:48 → 6:124', 'kural': "okuma — harekesiz 'misle mâ ûtiye'; sayım 'say 6:124 9-11'", 'not': 'kalıp eşi (sayım).'},
 # blok 126-130
 {'bag': '16:13 → 6:126', 'kural': "okuma — harekesiz 'li-qavmin yezzekkerûn'; sayım 'say 6:126 8-9'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '34:40 → 6:128', 'kural': "okuma — harekesiz 've yevme yahşuruhum cemî'an'; sayım 'say 6:128 1-3'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '55:33 → 6:130', 'kural': "okuma — harekesiz 'yâ ma'şera'l-cinni ve'l-ins'; sayım 'say 6:130 1-3'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '39:71 → 6:130', 'kural': "okuma — harekesiz 've yunzirûnekum liqâ'e yevmikum'; sayım 'say 6:130 11-13'", 'not': 'kalıp eşi (sayım).'},
 # blok 131-135
 {'bag': '28:59 → 6:131', 'kural': "okuma — harekesiz 'rabbuke muhlike'; sayım 'say 6:131 5-6'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '11:117 → 6:131', 'kural': "okuma — harekesiz 'l-qurâ bi-zulm'; sayım 'say 6:131 7-8'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '46:19 → 6:132', 'kural': "okuma — harekesiz 've li-kullin derecât'; sayım 'say 6:132 1-2'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '11:123 → 6:132', 'kural': "okuma — harekesiz 'rabbuke bi-ğâfil'; sayım 'say 6:132 6-7'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '27:93 → 6:132', 'kural': "okuma — harekesiz 'rabbuke bi-ğâfil'; sayım 'say 6:132 6-7'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '11:93 → 6:135', 'kural': "okuma — harekesiz ''alâ mekânetikum'; sayım 'say 6:135 4-5'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '11:121 → 6:135', 'kural': "okuma — harekesiz ''alâ mekânetikum'; sayım 'say 6:135 4-5'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '39:39 → 6:135', 'kural': "okuma — harekesiz ''alâ mekânetikum'; sayım 'say 6:135 4-5'", 'not': 'kalıp eşi (sayım).'},
 {'bag': '28:37 → 6:135', 'kural': "okuma — harekesiz ''âqibetu'd-dâr'; sayım 'say 6:135 13-14'", 'not': 'kalıp eşi (sayım).'},
 # blok 136-138
 {'bag': '22:36 → 6:138', 'kural': "okuma — harekesiz 'isma'llâhi 'aleyhâ'; sayım 'say 6:138 18-20'; en uzun ortak lemma dizisi 'zekere ism allâh 'alâ' (dizi 6 138 17 20)", 'not': 'kalıp eşi (sayım).'},
 # blok 139-141
 # blok 142-144
 {'bag': '2:168 → 6:142', 'kural': "okuma — harekesiz 've lâ tettebi'û xutuvâti'ş-şeytân, innehû lekum 'aduvvun mubîn'; sayım 'say 6:142 9-16'; en uzun ortak lemma dizisi 'lâ ittebe xutuve şeytân inne _ 'aduvv mubîn' (dizi 6 142 9 16)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '2:208 → 6:142', 'kural': "okuma — harekesiz 've lâ tettebi'û xutuvâti'ş-şeytân, innehû lekum 'aduvvun mubîn'; sayım 'say 6:142 9-16'; en uzun ortak lemma dizisi 'lâ ittebe xutuve şeytân inne _ 'aduvv mubîn' (dizi 6 142 9 16)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '24:21 → 6:142', 'kural': "okuma — harekesiz 'tettebi'û xutuvâti'ş-şeytân'; sayım 'say 6:142 10-12'; en uzun ortak lemma dizisi 'lâ ittebe xutuve şeytân' (dizi 6 142 9 12)", 'not': 'kalıp eşi (sayım).'},
 # blok 145-147
 {'bag': '2:173 → 6:145', 'kural': "okuma — harekesiz 'fe-meni'dturra ğayra bâğin ve lâ 'âdin'; sayım 'say 6:145 30-35'; en uzun ortak lemma dizisi 'men idturra ğayr bâğ lâ 'âd' (dizi 6 145 30 35)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '16:115 → 6:145', 'kural': "okuma — harekesiz 'uhille li-ğayri'llâhi bih, fe-meni'dturra ğayra bâğin ve lâ 'âdin'; sayım 'say 6:145 26-35'; lemma dizisi 'uhille ğayr allâh _ men idturra ğayr bâğ lâ 'âd' (dizi 6 145 26 35); en uzun ortak lemma dizisi 'men idturra ğayr bâğ lâ 'âd inne' (dizi 6 145 30 36)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '12:110 → 6:147', 'kural': "okuma — harekesiz ''ani'l-qavmi'l-mucrimîn'; sayım 'say 6:147 11-13'; en uzun ortak lemma dizisi 'lâ radde be's 'an qavm mucrim' (dizi 6 147 8 13)", 'not': 'kalıp eşi (sayım).'},
 # blok 148-150
 {'bag': '16:35 → 6:148', 'kural': "okuma — harekesiz 've lâ harramnâ'; sayım 'say 6:148 11-12'; lemma dizisi 'lâ âbâ' lâ harrame min' (dizi 6 148 9 13); en uzun ortak lemma dizisi 'qâle ellezî eşrake lev şâ'e allâh mâ' (dizi 6 148 1 7)", 'not': 'kalıp eşi (sayım).'},
 {'bag': '16:9 → 6:149', 'kural': "okuma — harekesiz 'şâ'e le-hedâkum ecma'în'; sayım 'say 6:149 6-8'; en uzun ortak lemma dizisi 'lev şâ'e hedâ ecma'' (dizi 6 149 5 8)", 'not': 'kalıp eşi (sayım).'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_enam', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in ENAM]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_enam'] = ENAM
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_enam', len(ENAM), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_enam', len(BAGLAR['AS_enam']))
