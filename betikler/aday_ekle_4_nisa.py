# -*- coding: utf-8 -*-
"""aday_ekle_4_nisa.py — sûre 4 (Nisâ) adayları (AX_nisa) ve okuma bağları (AS_nisa).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1043'ten); betik sıranın kopmadığını doğrular.
"""
import json

NISA = [
]

BAGLAR = {"AS_nisa": [
 # blok 1-5
 {'bag': '22:1 → 4:1', 'kural': "okuma — harekesiz 'yâ eyyuhe'n-nâsu'tteqû rabbekum'", 'not': 'kalıp eşi.'},
 {'bag': '31:33 → 4:1', 'kural': "okuma — harekesiz 'yâ eyyuhe'n-nâsu'tteqû rabbekum'", 'not': 'kalıp eşi.'},
 {'bag': '39:6 → 4:1', 'kural': "okuma — lemma dizisi 'xalaqa min nefs vâhide' ve harekesiz 'minhâ zevcehâ'", 'not': 'lemma dizisi ve kalıp eşi.'},
 {'bag': '33:52 → 4:1', 'kural': "okuma — lemma 'raqîb'", 'not': 'lemma eşi.'},
 {'bag': '4:1 → 4:2', 'kural': "sûre içi — 'itteqû rabbekum' hitabından yetimlere malları verme emrine (sayım dışı — anlatı bağı)", 'not': 'sûre içi ardışık.'},
 {'bag': '2:108 → 4:2', 'kural': "okuma — lemma 'yetebeddelu'", 'not': 'lemma eşi.'},
 {'bag': '33:52 → 4:2', 'kural': "okuma — lemma 'yetebeddelu'", 'not': 'lemma eşi.'},
 {'bag': '4:2 → 4:3', 'kural': "sûre içi — lemma 'yetîm' ('el-yetâmâ' / 'fi'l-yetâmâ')", 'not': 'sûre içi ardışık.'},
 {'bag': '35:1 → 4:3', 'kural': "okuma — harekesiz 'mesnâ ve sulâse ve rubâ''", 'not': 'kalıp eşi.'},
 {'bag': '30:28 → 4:3', 'kural': "okuma — harekesiz 'mâ meleket eymânukum'", 'not': 'kalıp eşi.'},
 {'bag': '33:52 → 4:3', 'kural': "okuma — lemma dizisi 'mâ meleket yemîn'", 'not': 'lemma dizisi eşi.'},
 {'bag': '4:3 → 4:4', 'kural': "sûre içi — lemma 'nisâ'' ('mine'n-nisâ'' / 'en-nisâ'')", 'not': 'sûre içi ardışık.'},
 {'bag': '4:4 → 4:5', 'kural': "sûre içi — lemma 'âtâ' ('âtû' / 'lâ tu'tû')", 'not': 'sûre içi ardışık.'},
 {'bag': '4:2 → 4:5', 'kural': "sûre içi — lemma 'mâl' ('emvâlehum' / 'emvâlekum')", 'not': 'sûre içi lemma eşi (blok içi).'},
 {'bag': '2:235 → 4:5', 'kural': "okuma — harekesiz 'qavlen ma'rûfâ'", 'not': 'kalıp eşi.'},
 {'bag': '33:32 → 4:5', 'kural': "okuma — harekesiz 'qavlen ma'rûfâ'", 'not': 'kalıp eşi.'},
 # blok 6-10
 {'bag': '4:5 → 4:6', 'kural': "sûre içi — lemma 'mâl' ('emvâlekum' / 'emvâlehum'; beyinsize verilmeyen maldan ergin yetime verilen mala)", 'not': 'sûre içi ardışık.'},
 {'bag': '4:2 → 4:6', 'kural': "sûre içi — lemma 'yetîm' ve lemma 'mâl' ('âtu'l-yetâmâ emvâlehum' / 'fe'dfe'û ileyhim emvâlehum')", 'not': 'sûre içi lemma eşi.'},
 {'bag': '33:39 → 4:6', 'kural': "okuma — önek kesilmiş 've kefâ bi'llâhi hasîbâ'", 'not': 'kalıp eşi.'},
 {'bag': '17:14 → 4:6', 'kural': "okuma — lemma 'hasîb'", 'not': 'lemma eşi.'},
 {'bag': '24:33 → 4:6', 'kural': "okuma — lemma 'yesta'fifu'", 'not': 'lemma eşi.'},
 {'bag': '24:60 → 4:6', 'kural': "okuma — lemma 'yesta'fifu'", 'not': 'lemma eşi.'},
 {'bag': '3:147 → 4:6', 'kural': "okuma — lemma 'isrâf'", 'not': 'lemma eşi.'},
 {'bag': '20:10 → 4:6', 'kural': "okuma — lemma 'âneste'", 'not': 'lemma eşi.'},
 {'bag': '4:6 → 4:7', 'kural': "sûre içi — yetimlerin mallarının teslimden miras paylarına (sayım dışı — anlatı bağı)", 'not': 'sûre içi ardışık.'},
 {'bag': '4:7 → 4:8', 'kural': "sûre içi — kök قرب ('el-aqrabûn' / 'ulu'l-qurbâ')", 'not': 'sûre içi ardışık.'},
 {'bag': '4:5 → 4:8', 'kural': "sûre içi — önek kesilmiş 've qûlû lehum qavlen ma'rûfâ'", 'not': 'sûre içi kalıp eşi.'},
 {'bag': '2:235 → 4:8', 'kural': "okuma — harekesiz 'qavlen ma'rûfâ'", 'not': 'kalıp eşi.'},
 {'bag': '33:32 → 4:8', 'kural': "okuma — harekesiz 'qavlen ma'rûfâ'", 'not': 'kalıp eşi.'},
 {'bag': '4:8 → 4:9', 'kural': "sûre içi — lemma 'qavl' ('qavlen ma'rûfâ' / 'qavlen sedîdâ')", 'not': 'sûre içi ardışık.'},
 {'bag': '4:7 → 4:9', 'kural': "sûre içi — lemma 'terake' ('terake'l-vâlidân' / 'lev terakû')", 'not': 'sûre içi lemma eşi (blok içi).'},
 {'bag': '33:70 → 4:9', 'kural': "okuma — harekesiz 'qavlen sedîdâ'", 'not': 'kalıp eşi.'},
 {'bag': '4:9 → 4:10', 'kural': "sûre içi — zayıf soy için korkudan yetim malını yiyenlerin tehdidine (sayım dışı — anlatı bağı)", 'not': 'sûre içi ardışık.'},
 {'bag': '4:6 → 4:10', 'kural': "sûre içi — lemma 'ekele' ('lâ te'kulûhâ' / 'ye'kulûne')", 'not': 'sûre içi lemma eşi (blok içi).'},
 {'bag': '4:2 → 4:10', 'kural': "sûre içi — lemma 'ekele' ('lâ te'kulû emvâlehum' / 'ye'kulûne emvâle'l-yetâmâ')", 'not': 'sûre içi lemma eşi.'},
 {'bag': '2:174 → 4:10', 'kural': "okuma — harekesiz 'fî butûnihim'", 'not': 'kalıp eşi.'},
 {'bag': '22:20 → 4:10', 'kural': "okuma — harekesiz 'fî butûnihim'", 'not': 'kalıp eşi.'},
 {'bag': '84:12 → 4:10', 'kural': "okuma — lemma 'yeslâ' ve lemma 'se'îr'", 'not': 'lemma eşi.'},
 # blok 11-11
 {'bag': '4:7 → 4:11', 'kural': "sûre içi — lemma 'terake' ('mimmâ terake'l-vâlidân' / 'mimmâ terake'; genel pay hükmünden paylara)", 'not': 'sûre içi lemma eşi.'},
 {'bag': '2:180 → 4:11', 'kural': "okuma — lemma 'vasiyye' ve lemma 'terake'", 'not': 'lemma eşi.'},
 {'bag': '19:31 → 4:11', 'kural': "okuma — lemma 'evsâ'", 'not': 'lemma eşi.'},
 {'bag': '2:237 → 4:11', 'kural': "okuma — lemma 'nisf'", 'not': 'lemma eşi.'},
 {'bag': '9:24 → 4:11', 'kural': "okuma — harekesiz 'âbâ'ukum ve ebnâ'ukum'", 'not': 'kalıp eşi.'},
 {'bag': '9:60 → 4:11', 'kural': "okuma — harekesiz 'ferîdaten mina'llâh'", 'not': 'kalıp eşi.'},
 {'bag': '33:1 → 4:11', 'kural': "okuma — harekesiz 'inna'llâhe kâne 'alîmen hakîmâ'", 'not': 'kalıp eşi.'},
 {'bag': '76:30 → 4:11', 'kural': "okuma — harekesiz 'inna'llâhe kâne 'alîmen hakîmâ'", 'not': 'kalıp eşi.'},
 {'bag': '31:33 → 4:11', 'kural': "okuma — lemma 'veled'", 'not': 'lemma eşi.'},
 # blok 12-12
 {'bag': '4:11 → 4:12', 'kural': "sûre içi — harekesiz 'min ba'di vasiyyetin yûsâ bihâ ev deyn' (çocukların ve ana babanın paylarından eşlerin ve kelâlenin paylarına)", 'not': 'sûre içi ardışık.'},
 {'bag': '2:237 → 4:12', 'kural': "okuma — lemma 'nisf'", 'not': 'lemma eşi.'},
 {'bag': '73:20 → 4:12', 'kural': "okuma — lemma 'nisf' ve lemma 'sulus'", 'not': 'lemma eşi.'},
 {'bag': '2:240 → 4:12', 'kural': "okuma — lemma 'vasiyye' ve lemma 'zevc'", 'not': 'lemma eşi.'},
 {'bag': '2:282 → 4:12', 'kural': "okuma — lemma 'deyn'", 'not': 'lemma eşi.'},
 {'bag': '19:6 → 4:12', 'kural': "okuma — lemma 'verise'", 'not': 'lemma eşi.'},
 {'bag': '22:59 → 4:12', 'kural': "okuma — lemma 'halîm'", 'not': 'lemma eşi.'},
 {'bag': '2:225 → 4:12', 'kural': "okuma — lemma 'halîm'", 'not': 'lemma eşi.'},
 {'bag': '33:51 → 4:12', 'kural': "okuma — lemma 'halîm'", 'not': 'lemma eşi.'},
 # blok 13-14
 {'bag': '4:12 → 4:13', 'kural': "sûre içi — 'tilke hudûdu'llâh' işareti önceki miras paylarına (sayım dışı — anlatı bağı)", 'not': 'sûre içi ardışık.'},
 {'bag': '2:229 → 4:13', 'kural': "okuma — harekesiz 'tilke hudûdu'llâh'", 'not': 'kalıp eşi.'},
 {'bag': '48:17 → 4:13', 'kural': "okuma — önek kesilmiş 've men yuti'i'llâhe ve rasûlehû' ve harekesiz 'yudxilhu'", 'not': 'kalıp eşi.'},
 {'bag': '9:89 → 4:13', 'kural': "okuma — harekesiz 'el-fevzu'l-'azîm'", 'not': 'kalıp eşi.'},
 {'bag': '57:12 → 4:13', 'kural': "okuma — harekesiz 'el-fevzu'l-'azîm'", 'not': 'kalıp eşi.'},
 {'bag': '4:13 → 4:14', 'kural': "sûre içi — lemma 'hudûd' ve harekesiz 'yudxilhu' (itaatten isyana, cennetten ateşe)", 'not': 'sûre içi ardışık.'},
 {'bag': '33:36 → 4:14', 'kural': "okuma — önek kesilmiş 've men ya'si'llâhe ve rasûlehû'", 'not': 'kalıp eşi.'},
 {'bag': '72:23 → 4:14', 'kural': "okuma — önek kesilmiş 've men ya'si'llâhe ve rasûlehû'", 'not': 'kalıp eşi.'},
 {'bag': '2:229 → 4:14', 'kural': "okuma — lemma 'yete'adde' ve lemma 'hudûd'", 'not': 'lemma eşi.'},
 {'bag': '65:1 → 4:14', 'kural': "okuma — lemma 'yete'adde' ve lemma 'hudûd'", 'not': 'lemma eşi.'},
 {'bag': '3:178 → 4:14', 'kural': "okuma — harekesiz ''azâbun muhîn'", 'not': 'kalıp eşi.'},
 # blok 15-18
 {'bag': '2:282 → 4:15', 'kural': "okuma — lemma 'isteşhidu'", 'not': 'lemma eşi.'},
 {'bag': '3:135 → 4:15', 'kural': "okuma — lemma 'fâhişe'", 'not': 'lemma eşi.'},
 {'bag': '65:1 → 4:15', 'kural': "okuma — lemma 'fâhişe'", 'not': 'lemma eşi.'},
 {'bag': '4:15 → 4:16', 'kural': "sûre içi — lemma 'etâ' ('ye'tîne' / 'ye'tiyânihâ'; kadınların hayâsızlığından iki kişinin işlediğine)", 'not': 'sûre içi ardışık.'},
 {'bag': '4:16 → 4:17', 'kural': "sûre içi — lemma 'tâbe' ('tâbâ' / 'yetûbûne', 'yetûbu')", 'not': 'sûre içi ardışık.'},
 {'bag': '3:90 → 4:17', 'kural': "okuma — lemma 'tevbe'", 'not': 'lemma eşi.'},
 {'bag': '16:119 → 4:17', 'kural': "okuma — lemma 'cehâle'", 'not': 'lemma eşi.'},
 {'bag': '33:24 → 4:17', 'kural': "okuma — lemma 'tâbe'", 'not': 'lemma eşi.'},
 {'bag': '48:4 → 4:17', 'kural': "okuma — önek kesilmiş 've kâna'llâhu 'alîmen hakîmâ'", 'not': 'kalıp eşi.'},
 {'bag': '4:17 → 4:18', 'kural': "sûre içi — harekesiz 'li'llezîne ya'melûn' ve lemma 'tevbe'", 'not': 'sûre içi ardışık.'},
 {'bag': '10:91 → 4:18', 'kural': "okuma — lemma 'ân'", 'not': 'lemma eşi.'},
 {'bag': '17:10 → 4:18', 'kural': "okuma — harekesiz 'a'tednâ lehum 'azâben elîmâ'", 'not': 'kalıp eşi.'},
 # blok 19-22
 {'bag': '4:18 → 4:19', 'kural': "sûre içi — tövbe hükümlerinden kadınlara davranışa (sayım dışı — anlatı bağı)", 'not': 'sûre içi ardışık.'},
 {'bag': '4:15 → 4:19', 'kural': "sûre içi — harekesiz 'ye'tîne' ve lemma 'fâhişe'", 'not': 'sûre içi kalıp ve lemma eşi.'},
 {'bag': '65:1 → 4:19', 'kural': "okuma — harekesiz 'illâ en ye'tîne bi-fâhişetin mubeyyine'", 'not': 'kalıp eşi.'},
 {'bag': '33:30 → 4:19', 'kural': "okuma — harekesiz 'bi-fâhişetin mubeyyine'", 'not': 'kalıp eşi.'},
 {'bag': '2:216 → 4:19', 'kural': "okuma — harekesiz 'en tekrehû şey'â'", 'not': 'kalıp eşi.'},
 {'bag': '2:232 → 4:19', 'kural': "okuma — lemma 'ta'dulu'", 'not': 'lemma eşi.'},
 {'bag': '2:269 → 4:19', 'kural': "okuma — harekesiz 'xayran kesîrâ'", 'not': 'kalıp eşi.'},
 {'bag': '4:19 → 4:20', 'kural': "sûre içi — lemma 'âtâ' ('âteytumûhunne' / 'âteytum')", 'not': 'sûre içi ardışık.'},
 {'bag': '3:14 → 4:20', 'kural': "okuma — lemma 'qıntâr'", 'not': 'lemma eşi.'},
 {'bag': '33:58 → 4:20', 'kural': "okuma — harekesiz 'buhtânen ve ismen mubînâ'", 'not': 'kalıp eşi.'},
 {'bag': '4:20 → 4:21', 'kural': "sûre içi — lemma 'exaze' ('e-te'xuzûnehû' / 'te'xuzûnehû')", 'not': 'sûre içi ardışık.'},
 {'bag': '33:7 → 4:21', 'kural': "okuma — harekesiz 'mîsâqan ğalîzâ'", 'not': 'kalıp eşi.'},
 {'bag': '4:21 → 4:22', 'kural': "sûre içi — eşlerle ilişkiden evlenme yasaklarına (sayım dışı — anlatı bağı)", 'not': 'sûre içi ardışık.'},
 {'bag': '4:19 → 4:22', 'kural': "sûre içi — lemma 'fâhişe'", 'not': 'sûre içi lemma eşi (blok içi).'},
 {'bag': '4:3 → 4:22', 'kural': "sûre içi — lemma 'nekaha'", 'not': 'sûre içi lemma eşi.'},
 {'bag': '17:32 → 4:22', 'kural': "okuma — harekesiz 've sâ'e sebîlâ' ve lemma 'fâhişe'", 'not': 'kalıp ve lemma eşi.'},
 {'bag': '35:39 → 4:22', 'kural': "okuma — lemma 'maqt'", 'not': 'lemma eşi.'},
 # blok 23-24
 {'bag': '2:233 → 4:23', 'kural': "okuma — lemma 'radâ'a' ve önek kesilmiş 'fe-lâ cunâha 'aleykum'", 'not': 'lemma ve kalıp eşi.'},
 {'bag': '22:2 → 4:23', 'kural': "okuma — lemma 'erda'at'", 'not': 'lemma eşi.'},
 {'bag': '86:7 → 4:23', 'kural': "okuma — lemma 'sulb'", 'not': 'lemma eşi.'},
 {'bag': '25:6 → 4:23', 'kural': "okuma — harekesiz 'ğafûran rahîmâ'", 'not': 'kalıp eşi.'},
 {'bag': '33:24 → 4:23', 'kural': "okuma — harekesiz 'inna'llâhe kâne ğafûran rahîmâ'", 'not': 'kalıp eşi.'},
 {'bag': '4:12 → 4:23', 'kural': "sûre içi — lemma 'uxt'", 'not': 'sûre içi lemma eşi.'},
 {'bag': '4:23 → 4:24', 'kural': "sûre içi — lemma 'cunâh'", 'not': 'sûre içi ardışık.'},
 {'bag': '4:3 → 4:24', 'kural': "sûre içi — harekesiz 'mâ meleket eymânukum'", 'not': 'sûre içi kalıp eşi.'},
 {'bag': '4:11 → 4:24', 'kural': "sûre içi — harekesiz 'inna'llâhe kâne 'alîmen hakîmâ' ve lemma 'ferîde'", 'not': 'sûre içi kalıp ve lemma eşi.'},
 {'bag': '2:236 → 4:24', 'kural': "okuma — lemma 'ferîde'", 'not': 'lemma eşi.'},
 {'bag': '2:232 → 4:24', 'kural': "okuma — lemma 'terâda'", 'not': 'lemma eşi.'},
 {'bag': '2:235 → 4:24', 'kural': "okuma — önek kesilmiş 've lâ cunâha 'aleykum'", 'not': 'kalıp eşi.'},
 {'bag': '60:10 → 4:24', 'kural': "okuma — önek kesilmiş 've lâ cunâha 'aleykum'", 'not': 'kalıp eşi.'},
 {'bag': '9:69 → 4:24', 'kural': "okuma — lemma 'istemta'a'", 'not': 'lemma eşi.'},
 {'bag': '24:23 → 4:24', 'kural': "okuma — lemma 'muhsane'", 'not': 'lemma eşi.'},
 # blok 25-28
 {'bag': '4:24 → 4:25', 'kural': "sûre içi — harekesiz 'mâ meleket eymânukum' ve lemma 'muhsane'", 'not': 'sûre içi ardışık.'},
 {'bag': '4:3 → 4:25', 'kural': "sûre içi — harekesiz 'mâ meleket eymânukum'", 'not': 'sûre içi kalıp eşi.'},
 {'bag': '4:12 → 4:25', 'kural': "sûre içi — lemma 'nisf'", 'not': 'sûre içi lemma eşi.'},
 {'bag': '4:19 → 4:25', 'kural': "sûre içi — lemma 'fâhişe'", 'not': 'sûre içi lemma eşi.'},
 {'bag': '9:86 → 4:25', 'kural': "okuma — lemma 'tavl'", 'not': 'lemma eşi.'},
 {'bag': '24:33 → 4:25', 'kural': "okuma — lemma 'fetât'", 'not': 'lemma eşi.'},
 {'bag': '3:195 → 4:25', 'kural': "okuma — harekesiz 'ba'dukum min ba'd'", 'not': 'kalıp eşi.'},
 {'bag': '24:23 → 4:25', 'kural': "okuma — lemma 'muhsane'", 'not': 'lemma eşi.'},
 {'bag': '24:19 → 4:25', 'kural': "okuma — lemma 'fâhişe'", 'not': 'lemma eşi.'},
 {'bag': '2:184 → 4:25', 'kural': "okuma — harekesiz 'xayrun lekum'", 'not': 'kalıp eşi.'},
 {'bag': '49:5 → 4:25', 'kural': "okuma — önek kesilmiş 've'llâhu ğafûrun rahîm'", 'not': 'kalıp eşi.'},
 {'bag': '9:91 → 4:25', 'kural': "okuma — önek kesilmiş 've'llâhu ğafûrun rahîm'", 'not': 'kalıp eşi.'},
 {'bag': '3:137 → 4:26', 'kural': "okuma — lemma 'sunne'", 'not': 'lemma eşi.'},
 {'bag': '9:106 → 4:26', 'kural': "okuma — önek kesilmiş 've'llâhu 'alîmun hakîm'", 'not': 'kalıp eşi.'},
 {'bag': '9:60 → 4:26', 'kural': "okuma — önek kesilmiş 've'llâhu 'alîmun hakîm'", 'not': 'kalıp eşi.'},
 {'bag': '60:10 → 4:26', 'kural': "okuma — önek kesilmiş 've'llâhu 'alîmun hakîm'", 'not': 'kalıp eşi.'},
 {'bag': '4:26 → 4:27', 'kural': "sûre içi — lemma 'erâde'", 'not': 'sûre içi ardışık.'},
 {'bag': '4:26 → 4:28', 'kural': "sûre içi — harekesiz 'yurîdu'llâh'", 'not': 'sûre içi kalıp eşi, blok içi.'},
 {'bag': '3:14 → 4:27', 'kural': "okuma — lemma 'şeheve'", 'not': 'lemma eşi.'},
 {'bag': '19:59 → 4:27', 'kural': "okuma — lemma 'şeheve'", 'not': 'lemma eşi.'},
 {'bag': '4:27 → 4:28', 'kural': "sûre içi — lemma 'erâde'", 'not': 'sûre içi ardışık.'},
 {'bag': '2:86 → 4:28', 'kural': "okuma — lemma 'xaffefe'", 'not': 'lemma eşi.'},
 {'bag': '2:282 → 4:28', 'kural': "okuma — lemma 'da'îf'", 'not': 'lemma eşi.'},
 {'bag': '9:91 → 4:28', 'kural': "okuma — lemma 'da'îf'", 'not': 'lemma eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_nisa', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in NISA]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_nisa'] = NISA
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_nisa', len(NISA), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_nisa', len(BAGLAR['AS_nisa']))
