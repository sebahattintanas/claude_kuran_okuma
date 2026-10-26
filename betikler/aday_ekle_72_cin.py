# -*- coding: utf-8 -*-
"""aday_ekle_72_cin.py — sûre 72 (Cin) adayları (AX_cin) ve okuma bağları (AS_cin).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

CIN = [
]

BAGLAR = {"AS_cin": [
 # blok 1-10
 {'bag': '71:28 → 72:1', 'kural': "okuma — ardışık sûre sınırı; Nûh'un duası ile kapanış / 'qul ûhiye ileyye' ile açılış; fâsıla ا → ا (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '46:29 → 72:1', 'kural': "okuma — 'nefer + min + cinn' + Kur'an dinleme: 1P anlatı / vahiy bildirimi", 'not': 'kurgu eşi.'},
 {'bag': '18:38 → 72:2', 'kural': "xref (ölçüm) 'eşreke + rabb + ehad' — 1S / 1P 'len'", 'not': 'kalıp eşi.'},
 {'bag': '72:1 → 72:2', 'kural': "sûre içi — 'qur'ân' → 'yehdî' öznesi", 'not': 'sûre içi eş.'},
 {'bag': '70:12 → 72:3', 'kural': "okuma — lemma 'sâhibe' (4 ayet): suçlunun eşi / Rab için nefy", 'not': 'lemma eşi.'},
 {'bag': '18:14 → 72:4', 'kural': "okuma — lemma 'şetat' (2 ayet)", 'not': 'lemma eşi.'},
 {'bag': '17:88 → 72:5', 'kural': "lemma dizisi 'ins + cinn + alâ' (2 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '72:4 → 72:5', 'kural': "sûre içi — 'ale'llâhi şetatâ' / 'ale'llâhi kezibâ'", 'not': 'sûre içi eş.'},
 {'bag': '72:5 → 72:7', 'kural': "nakarat3 sûre içi (ölçüm GEÇER) — 'zanne en len'", 'not': 'sûre içi eş.'},
 {'bag': '72:5 → 72:6', 'kural': "sûre içi — 'ins' / 'cinn' çifti ardışık iki ayette", 'not': 'sûre içi eş.'},
 {'bag': '15:17 → 72:8', 'kural': "okuma — göğün korunması: 1P 'hafiznâhâ' / cinlerin tanıklığı 'muli'et harasen'", 'not': 'kurgu eşi.'},
 {'bag': '37:10 → 72:8', 'kural': "okuma — alev (şihâb / şuhub) — gök korunması", 'not': 'kurgu eşi.'},
 {'bag': '67:5 → 72:8', 'kural': "okuma — gök + şeytanlara atış / alevler", 'not': 'kurgu eşi.'},
 {'bag': '15:18 → 72:9', 'kural': "okuma — lemma 'şihâb' (4 ayet) + 'sem'': 'istereqa's-sem'' / 'meqâ'ide li's-sem''", 'not': 'lemma eşi.'},
 {'bag': '37:10 → 72:9', 'kural': "okuma — lemma 'şihâb' (4 ayet): 'sâqib' / 'rasad'", 'not': 'lemma eşi.'},
 {'bag': '72:8 → 72:9', 'kural': "sûre içi — kök شهب: 'şuhub' / 'şihâb'", 'not': 'sûre içi eş.'},
 {'bag': '72:2 → 72:10', 'kural': "sûre içi — kök رشد: 'ruşd' / 'raşad'", 'not': 'sûre içi eş.'},
 # blok 11-20
 {'bag': '23:17 → 72:11', 'kural': "okuma — lemma 'tarîqa' (5 ayet): gökler / gruplar", 'not': 'lemma eşi.'},
 {'bag': '20:63 → 72:11', 'kural': "okuma — lemma 'tarîqa': yol, gelenek / gruplar", 'not': 'lemma eşi.'},
 {'bag': '72:11 → 72:14', 'kural': "sûre içi — 'ennâ minne … ve minnâ …' kalıbı: iyiler / müslimler", 'not': 'sûre içi eş.'},
 {'bag': '72:5 → 72:12', 'kural': "nakarat3 sûre içi (ölçüm GEÇER) — 'ennâ zanennâ en len': yanlış kanı / doğru kanı", 'not': 'sûre içi eş.'},
 {'bag': '72:2 → 72:13', 'kural': "sûre içi — 'âmennâ bihî' ×2; 'yehdî' / 'el-hudâ'", 'not': 'sûre içi eş.'},
 {'bag': '72:6 → 72:13', 'kural': "sûre içi — lemma 'rehaq' (2 ayet, korpusun tamamı): artırılan / korkulmayan", 'not': 'sûre içi eş.'},
 {'bag': '12:20 → 72:13', 'kural': "okuma — lemma 'bahs' (2 ayet)", 'not': 'lemma eşi.'},
 {'bag': '72:14 → 72:15', 'kural': "sûre içi — lemma 'qâsit' (2 ayet, korpusun tamamı); 'fe-men esleme' / 'emme'l-qâsitûn' tafsîli", 'not': 'sûre içi eş.'},
 {'bag': '72:10 → 72:14', 'kural': "sûre içi — kök رشد: 'raşedâ' ×2", 'not': 'sûre içi eş.'},
 {'bag': '72:11 → 72:16', 'kural': "sûre içi — lemma 'tarîqa': gruplar / yol", 'not': 'sûre içi eş.'},
 {'bag': '41:30 → 72:16', 'kural': "okuma — lemma 'istaqâma'", 'not': 'lemma eşi.'},
 {'bag': '15:22 → 72:16', 'kural': "okuma — lemma 'esqâ' + 'mâ'': 1P geçmiş / şarta bağlı", 'not': 'lemma eşi.'},
 {'bag': '20:124 → 72:17', 'kural': "lemma dizisi 'a'rade + an + zikr' (2 ayet) — 'zikrî' / 'zikri rabbihî'", 'not': 'kalıp eşi.'},
 {'bag': '71:20 → 72:17', 'kural': "okuma — ardışık sûre; kök سلك: yolda yürüme / azaba sokma", 'not': 'ardışık sûre bağı.'},
 {'bag': '26:213 → 72:18', 'kural': "lemma dizisi 'de'â + ma'a + allah' (5 ayet) — 2MS 'ilâhen âhar' / 2MP 'ehadâ'", 'not': 'kalıp eşi.'},
 {'bag': '28:88 → 72:18', 'kural': "lemma dizisi 'de'â + ma'a + allah' (5 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '72:18 → 72:20', 'kural': "sûre içi — kök دعو: 'lâ ted'û' / 'yed'ûhu' / 'ed'û rabbî'", 'not': 'sûre içi eş.'},
 {'bag': '72:1 → 72:20', 'kural': "sûre içi — iki 'qul': vahiy bildirimi / 1S ikrar", 'not': 'sûre içi eş.'},
 {'bag': '72:2 → 72:20', 'kural': "sûre içi — 'len nuşrike bi-rabbinâ ehadâ' (1P) / 'lâ uşriku bihî ehadâ' (1S)", 'not': 'sûre içi eş.'},
 {'bag': '13:36 → 72:20', 'kural': "okuma — 'qul innemâ … ve lâ uşrike bih'", 'not': 'kurgu eşi.'},
 # blok 21-28
 {'bag': '10:49 → 72:21', 'kural': "okuma — 'qul + lâ emliku + darr': kendisi için / sizin için", 'not': 'kurgu eşi.'},
 {'bag': '72:10 → 72:21', 'kural': "sûre içi — 'şerr … raşad' / 'darr … raşad'", 'not': 'sûre içi eş.'},
 {'bag': '72:20 → 72:21', 'kural': "sûre içi — ardışık 'qul' (72:20, 21, 22, 25)", 'not': 'sûre içi eş.'},
 {'bag': '18:27 → 72:22', 'kural': "lemma dizisi 'vecede + min + dûn + multehad' (2 ayet) / xref — 2MS / 1S", 'not': 'kalıp eşi.'},
 {'bag': '33:36 → 72:23', 'kural': "lemma dizisi ''asâ + allah + rasûl' (3 ayet) / xref", 'not': 'kalıp eşi.'},
 {'bag': '9:63 → 72:23', 'kural': "xref (ölçüm) 'rasûl + nâr + hâlid' — 'hâliden' / 'hâlidîne … ebedâ'", 'not': 'kalıp eşi.'},
 {'bag': '72:15 → 72:23', 'kural': "sûre içi — lemma 'cehennem': 'hatab' / 'nâr'", 'not': 'sûre içi eş.'},
 {'bag': '19:75 → 72:24', 'kural': "lemma dizisi 'hattâ + izâ + ra'â + mâ' (2 ayet) / lemma 'ed'af' (2 ayet) — 'ed'afu cundâ' / 'ed'afu nâsiran'", 'not': 'kalıp eşi.'},
 {'bag': '18:39 → 72:24', 'kural': "okuma — lemma 'eqall' (2 ayet)", 'not': 'lemma eşi.'},
 {'bag': '72:24 → 72:28', 'kural': "sûre içi — lemma ''aded': 'eqallu 'adedâ' / 'kulle şey'in 'adedâ'", 'not': 'sûre içi eş.'},
 {'bag': '21:109 → 72:25', 'kural': "okuma — 'in edrî e-qarîbun … mâ tû'adûn': 'em ba'îd' / 'em yec'alu lehû rabbî emedâ'", 'not': 'kurgu eşi.'},
 {'bag': '72:10 → 72:25', 'kural': "sûre içi — lemma 'tedrî': cinlerin 'lâ nedrî' / 1S 'in edrî'", 'not': 'sûre içi eş.'},
 {'bag': '72:24 → 72:25', 'kural': "sûre içi — 'mâ yû'adûn' (3MP) / 'mâ tû'adûn' (2MP)", 'not': 'sûre içi eş.'},
 {'bag': '70:7 → 72:25', 'kural': "okuma — 'qarîb' vaat edilen için (esmâ DEĞİL, aynı karar)", 'not': 'lemma eşi.'},
 {'bag': '62:8 → 72:26', 'kural': "lemma dizisi ''âlim + ğayb' (13 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '72:2 → 72:26', 'kural': "sûre içi — kök أحد altı geçişin altısı nefy / nehy içinde 'ehad' (72:2, 7, 18, 20, 22, 26)", 'not': 'sûre içi eş.'},
 {'bag': '21:28 → 72:27', 'kural': "okuma — lemma 'irtedâ' (3 ayet) + 'beyne eydîhim … halfehum'", 'not': 'lemma eşi.'},
 {'bag': '72:9 → 72:27', 'kural': "sûre içi — lemma 'rasad' (2 ayet, korpusun tamamı): alev / gözetleyiciler", 'not': 'sûre içi eş.'},
 {'bag': '72:17 → 72:27', 'kural': "sûre içi — kök سلك: azaba sokma / gözetleyici yürütme", 'not': 'sûre içi eş.'},
 {'bag': '36:12 → 72:28', 'kural': "okuma — lemma 'ahsâ' + 'kulle şey'': 1P / 3MS", 'not': 'lemma eşi.'},
 {'bag': '72:23 → 72:28', 'kural': "sûre içi — lemma 'risâle': 'belâğan … ve risâlâtih' / 'ebleğû risâlâti rabbihim'", 'not': 'sûre içi eş.'},
 {'bag': '72:1 → 72:28', 'kural': "sûre içi — vahiy bildirimi ile açılış / tebliğin bilinmesi ile kapanış (okuma)", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_cin', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in CIN]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_cin'] = CIN
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_cin', len(CIN), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_cin', len(BAGLAR['AS_cin']))
