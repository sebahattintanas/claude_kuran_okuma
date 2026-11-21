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
