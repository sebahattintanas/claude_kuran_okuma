# -*- coding: utf-8 -*-
"""aday_ekle_5_maide.py — sûre 5 (Mâide) adayları (AX_maide) ve okuma bağları (AS_maide).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1043'ten); betik sıranın kopmadığını doğrular.
"""
import json

MAIDE = [
]

BAGLAR = {"AS_maide": [
 # blok 1-2
 {'bag': '22:28 → 5:1', 'kural': "okuma — harekesiz 'behîmetu'l-en'âm'", 'not': 'kalıp eşi; lemma behîme eşi.'},
 {'bag': '22:34 → 5:1', 'kural': "okuma — harekesiz 'behîmetu'l-en'âm'", 'not': 'kalıp eşi; lemma behîme eşi.'},
 {'bag': '22:30 → 5:1', 'kural': "okuma — harekesiz 'illâ mâ yutlâ 'aleykum'", 'not': 'kalıp eşi; lemma ehalle eşi.'},
 {'bag': '4:127 → 5:1', 'kural': "okuma — harekesiz 'yutlâ 'aleykum'", 'not': 'kalıp eşi.'},
 {'bag': '5:1 → 5:2', 'kural': "sûre içi — harekesiz 'yâ eyyuhe'llezîne âmenû'", 'not': 'blok içi kalıp eşi (ölçüm nakarat3); lemma ehalle eşi (izin / yasak).'},
 {'bag': '2:158 → 5:2', 'kural': "okuma — lemma 'şe'â'ir'", 'not': 'lemma eşi.'},
 {'bag': '22:32 → 5:2', 'kural': "okuma — lemma 'şe'â'ir'", 'not': 'lemma eşi.'},
 {'bag': '22:36 → 5:2', 'kural': "okuma — lemma 'şe'â'ir'", 'not': 'lemma eşi.'},
 {'bag': '2:194 → 5:2', 'kural': "okuma — harekesiz 'eş-şehra'l-harâm'", 'not': 'kalıp eşi.'},
 {'bag': '2:217 → 5:2', 'kural': "okuma — harekesiz 'eş-şehra'l-harâm'", 'not': 'kalıp eşi.'},
 {'bag': '2:196 → 5:2', 'kural': "okuma — lemma 'hedy'; harekesiz 'şedîdu'l-'iqâb'", 'not': 'lemma ve kalıp eşi.'},
 {'bag': '48:25 → 5:2', 'kural': "okuma — lemma 'hedy'; harekesiz ''ani'l-mescidi'l-harâm'", 'not': 'lemma ve kalıp eşi (ölçüm xref).'},
 {'bag': '2:198 → 5:2', 'kural': "okuma — lemma dizisi 'ibteğâ fadl min rabb'", 'not': 'lemma dizisi eşi (ölçüm xref).'},
 {'bag': '59:7 → 5:2', 'kural': "okuma — harekesiz 'inna'llâhe şedîdu'l-'iqâb'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '49:1 → 5:2', 'kural': "okuma — önek kesilmiş 've'ttequ'llâhe inna'llâh'", 'not': 'kalıp eşi.'},
 # blok 3-4
 {'bag': '2:173 → 5:3', 'kural': "okuma — harekesiz 'el-meytetu ve'd-demu ve lahmu'l-xinzîr'", 'not': "kalıp eşi (ölçüm xref); önek kesilmiş 'fe-meni'dturr' eşi."},
 {'bag': '16:115 → 5:3', 'kural': "okuma — harekesiz 'el-meytetu ve'd-demu ve lahmu'l-xinzîr'", 'not': "kalıp eşi (ölçüm xref); harekesiz 'uhille li-ğayri'llâhi bih' eşi."},
 {'bag': '2:150 → 5:3', 'kural': "okuma — lemma dizisi 'xaşiye xaşiye'", 'not': 'lemma dizisi eşi (korkmama / korkma emri).'},
 {'bag': '2:185 → 5:3', 'kural': "okuma — lemma 'ekmel'", 'not': 'lemma eşi.'},
 {'bag': '3:85 → 5:3', 'kural': "okuma — lemma 'islâm'", 'not': 'lemma eşi.'},
 {'bag': '3:19 → 5:3', 'kural': "okuma — lemma 'islâm'", 'not': 'lemma eşi.'},
 {'bag': '9:120 → 5:3', 'kural': "okuma — lemma 'maxmasa'", 'not': 'lemma eşi.'},
 {'bag': '70:43 → 5:3', 'kural': "okuma — lemma 'nusub'", 'not': 'lemma eşi.'},
 {'bag': '3:19 → 5:4', 'kural': "okuma — harekesiz 'serî'u'l-hisâb'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '3:199 → 5:4', 'kural': "okuma — harekesiz 'inna'llâhe serî'u'l-hisâb'", 'not': 'kalıp eşi.'},
 {'bag': '14:51 → 5:4', 'kural': "okuma — harekesiz 'inna'llâhe serî'u'l-hisâb'", 'not': 'kalıp eşi.'},
 {'bag': '40:17 → 5:4', 'kural': "okuma — harekesiz 'inna'llâhe serî'u'l-hisâb'", 'not': 'kalıp eşi.'},
 {'bag': '22:28 → 5:4', 'kural': "okuma — lemma dizisi 'zekera ism allâh'", 'not': 'lemma dizisi eşi (ölçüm xref).'},
 {'bag': '22:34 → 5:4', 'kural': "okuma — lemma dizisi 'zekera ism allâh'", 'not': 'lemma dizisi eşi (ölçüm xref).'},
 {'bag': '22:36 → 5:4', 'kural': "okuma — lemma dizisi 'zekera ism allâh'", 'not': 'lemma dizisi eşi (ölçüm xref).'},
 {'bag': '5:1 → 5:4', 'kural': "sûre içi — lemma 'ehalle'", 'not': 'sûre içi lemma eşi (helâl kılma).'},
 {'bag': '5:2 → 5:4', 'kural': "sûre içi — önek kesilmiş 've'ttequ'llâhe inna'llâh'", 'not': 'sûre içi kalıp eşi (ölçüm nakarat3); lemma ehalle eşi.'},
 # blok 5-6
 {'bag': '3:186 → 5:5', 'kural': "okuma — harekesiz 'mine'llezîne ûtu'l-kitâbe min qablikum'", 'not': 'kalıp eşi.'},
 {'bag': '3:93 → 5:5', 'kural': "okuma — lemma 'hill'", 'not': 'lemma eşi; lemma taâm eşi.'},
 {'bag': '60:10 → 5:5', 'kural': "okuma — harekesiz 'âteytumûhunne ucûrahunne'", 'not': 'kalıp eşi; lemma hill eşi.'},
 {'bag': '4:24 → 5:5', 'kural': "okuma — harekesiz 'muhsinîne ğayra musâfihîn'", 'not': 'kalıp eşi (ölçüm xref); lemma muhsane eşi.'},
 {'bag': '4:25 → 5:5', 'kural': "okuma — lemma 'axdân'", 'not': 'lemma eşi; lemma muhsane eşi.'},
 {'bag': '39:65 → 5:5', 'kural': "okuma — lemma 'habita'", 'not': 'lemma eşi; harekesiz mine-l-xâsirîn eşi.'},
 {'bag': '2:217 → 5:5', 'kural': "okuma — lemma 'habita'", 'not': 'lemma eşi.'},
 {'bag': '3:85 → 5:5', 'kural': "okuma — önek kesilmiş 've huve fi'l-âxirati mine'l-xâsirîn'", 'not': 'kalıp eşi.'},
 {'bag': '4:43 → 5:6', 'kural': "okuma — harekesiz 'kuntum merdâ ev 'alâ sefer'", 'not': 'kalıp eşi (ölçüm xref); teyemmüm dizisinin kalıp eşleri.'},
 {'bag': '2:184 → 5:6', 'kural': "okuma — lemma dizisi 'merîd ev 'alâ sefer'", 'not': 'lemma dizisi eşi (ölçüm xref).'},
 {'bag': '2:185 → 5:6', 'kural': "okuma — lemma dizisi 'merîd ev 'alâ sefer'", 'not': 'lemma dizisi eşi (ölçüm xref).'},
 {'bag': '22:78 → 5:6', 'kural': "okuma — lemma 'harac'", 'not': 'lemma eşi.'},
 {'bag': '12:6 → 5:6', 'kural': "okuma — lemma dizisi 'etemme ni'me'", 'not': 'lemma dizisi eşi.'},
 {'bag': '16:81 → 5:6', 'kural': "okuma — lemma dizisi 'etemme ni'me'", 'not': 'lemma dizisi eşi.'},
 {'bag': '48:2 → 5:6', 'kural': "okuma — lemma dizisi 'etemme ni'me'", 'not': 'lemma dizisi eşi.'},
 {'bag': '2:150 → 5:6', 'kural': "okuma — lemma dizisi 'etemme ni'me'", 'not': 'lemma dizisi eşi.'},
 {'bag': '5:1 → 5:6', 'kural': "sûre içi — harekesiz 'yâ eyyuhe'llezîne âmenû'", 'not': 'sûre içi kalıp eşi (ölçüm nakarat3).'},
 # blok 7-11
 {'bag': '2:285 → 5:7', 'kural': "okuma — harekesiz 'semi'nâ ve eta'nâ'", 'not': 'kalıp eşi.'},
 {'bag': '24:51 → 5:7', 'kural': "okuma — harekesiz 'semi'nâ ve eta'nâ'", 'not': 'kalıp eşi.'},
 {'bag': '3:119 → 5:7', 'kural': "okuma — harekesiz 'inna'llâhe 'alîmun bi-zâti's-sudûr'", 'not': 'kalıp eşi.'},
 {'bag': '5:4 → 5:7', 'kural': "sûre içi — önek kesilmiş 've'ttequ'llâhe inna'llâh'", 'not': 'sûre içi kalıp eşi (ölçüm nakarat3).'},
 {'bag': '5:7 → 5:8', 'kural': "sûre içi — önek kesilmiş 've'ttequ'llâhe inna'llâh'", 'not': 'blok içi kalıp eşi (ölçüm nakarat3).'},
 {'bag': '5:7 → 5:11', 'kural': "sûre içi — lemma dizisi 'zekera ni'me allâh 'alâ'", 'not': 'blok içi lemma dizisi eşi (ölçüm nakarat3); harekesiz yazım farkı.'},
 {'bag': '4:135 → 5:8', 'kural': "okuma — harekesiz 'yâ eyyuhe'llezîne âmenû kûnû'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '5:2 → 5:8', 'kural': "sûre içi — önek kesilmiş 've lâ yecrimennekum şene'ânu qavm'", 'not': 'sûre içi kalıp eşi (ölçüm nakarat3).'},
 {'bag': '2:237 → 5:8', 'kural': "okuma — harekesiz 'aqrabu li't-taqvâ'", 'not': 'kalıp eşi.'},
 {'bag': '59:18 → 5:8', 'kural': "okuma — harekesiz 'inna'llâhe xabîrun bimâ ta'melûn'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '5:8 → 5:11', 'kural': "sûre içi — harekesiz 'yâ eyyuhe'llezîne âmenû'", 'not': 'blok içi kalıp eşi (ölçüm nakarat3).'},
 {'bag': '48:29 → 5:9', 'kural': "okuma — harekesiz 've'ade'llâhu'llezîne âmenû ve 'amilu's-sâlihât'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '49:3 → 5:9', 'kural': "okuma — harekesiz 'mağfiratun ve ecrun 'azîm'", 'not': 'kalıp eşi.'},
 {'bag': '57:19 → 5:10', 'kural': "okuma — önek kesilmiş 've'llezîne keferû ve kezzebû bi-âyâtinâ ulâ'ike ashâbu'l-cahîm'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '2:39 → 5:10', 'kural': "okuma — önek kesilmiş 've'llezîne keferû ve kezzebû bi-âyâtinâ'", 'not': 'kalıp eşi.'},
 {'bag': '33:9 → 5:11', 'kural': "okuma — lemma dizisi 'eyy ellezî âmene zekera ni'me allâh 'alâ'", 'not': 'lemma dizisi eşi (ölçüm xref).'},
 {'bag': '35:3 → 5:11', 'kural': "okuma — harekesiz 'zkurû ni'meta'llâhi 'aleykum'", 'not': 'kalıp eşi.'},
 {'bag': '3:122 → 5:11', 'kural': "okuma — önek kesilmiş 've 'ale'llâhi fe'l-yetevekkeli'l-mu'minûn'", 'not': 'kalıp eşi; lemma hemme eşi.'},
 {'bag': '64:13 → 5:11', 'kural': "okuma — önek kesilmiş 've 'ale'llâhi fe'l-yetevekkeli'l-mu'minûn'", 'not': 'kalıp eşi.'},
 # blok 12-14
 {'bag': '3:81 → 5:12', 'kural': "okuma — harekesiz 'axaza'llâhu mîsâq'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '3:187 → 5:12', 'kural': "okuma — harekesiz 'axaza'llâhu mîsâq'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '48:9 → 5:12', 'kural': "okuma — lemma ''azzar'", 'not': "lemma eşi; LEM ''azzar' (morph LEM ham biçim)."},
 {'bag': '2:245 → 5:12', 'kural': "okuma — harekesiz 'llâhe qardan hasenen'", 'not': 'kalıp eşi.'},
 {'bag': '57:11 → 5:12', 'kural': "okuma — harekesiz 'llâhe qardan hasenen'", 'not': 'kalıp eşi.'},
 {'bag': '47:12 → 5:12', 'kural': "okuma — harekesiz 'cennâtin tecrî min tahtihe'l-enhâr'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '2:108 → 5:12', 'kural': "okuma — önek kesilmiş 'fe-qad dalle sevâ'e's-sebîl'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '60:1 → 5:12', 'kural': "okuma — önek kesilmiş 'fe-qad dalle sevâ'e's-sebîl'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '4:155 → 5:13', 'kural': "okuma — önek kesilmiş 'fe-bimâ naqdihim mîsâqahum'", 'not': 'kalıp eşi.'},
 {'bag': '22:53 → 5:13', 'kural': "okuma — lemma 'qâsiye'", 'not': 'lemma eşi.'},
 {'bag': '4:46 → 5:13', 'kural': "okuma — harekesiz 'yuharrifûne'l-kelime 'an mevâdi'ih'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '2:75 → 5:13', 'kural': "okuma — lemma 'yuharrif'", 'not': "lemma eşi; LEM 'yuharrif' (morph LEM ham biçim)."},
 {'bag': '40:19 → 5:13', 'kural': "okuma — lemma 'xâ'ine'", 'not': 'lemma eşi.'},
 {'bag': '2:249 → 5:13', 'kural': "okuma — harekesiz 'illâ qalîlen minhum'", 'not': 'kalıp eşi.'},
 {'bag': '2:195 → 5:13', 'kural': "okuma — harekesiz 'inna'llâhe yuhibbu'l-muhsinîn'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '3:134 → 5:13', 'kural': "okuma — lemma dizisi 'allâh ahbeb muhsin'", 'not': "lemma dizisi eşi (ölçüm xref); LEM 'ahbeb' (morph LEM ham biçim)."},
 {'bag': '5:13 → 5:14', 'kural': "sûre içi — harekesiz 'hazzan mimmâ zukkirû bih'", 'not': "blok içi kalıp eşi (ölçüm nakarat3); lemma dizisi 'nesiye hazz min mâ zukkir bi' eşi — önek farkı ('ve' / 'fe')."},
 {'bag': '60:4 → 5:14', 'kural': "okuma — lemma dizisi 'beyn 'adâve bağdâ''", 'not': 'lemma dizisi eşi (ölçüm xref).'},
 {'bag': '16:112 → 5:14', 'kural': "okuma — harekesiz 'bimâ kânû yasna'ûn'", 'not': 'kalıp eşi.'},
 # blok 15-17
 {'bag': '42:30 → 5:15', 'kural': "okuma — önek kesilmiş 've ya'fû 'an kesîr'", 'not': 'kalıp eşi.'},
 {'bag': '2:257 → 5:16', 'kural': "okuma — harekesiz 'mine'z-zulumâti ile'n-nûr'", 'not': 'kalıp eşi.'},
 {'bag': '14:1 → 5:16', 'kural': "okuma — lemma dizisi 'zuleme ilâ nûr izn'", 'not': 'lemma dizisi eşi (ölçüm xref).'},
 {'bag': '2:142 → 5:16', 'kural': "okuma — harekesiz 'ilâ sırâtin mustaqîm'", 'not': "kalıp eşi; 'yehdî' ile dosdoğru yola iletme."},
 {'bag': '9:31 → 5:17', 'kural': "okuma — lemma dizisi 'mesîh ibn meryem'", 'not': 'lemma dizisi eşi (ölçüm xref).'},
 {'bag': '48:11 → 5:17', 'kural': "okuma — harekesiz 'mina'llâhi şey'en'", 'not': "kalıp eşi (ölçüm xref); 'fe-men yemliku' sorusu ve 'in erâde' şartı."},
 {'bag': '14:8 → 5:17', 'kural': "okuma — önek kesilmiş 've men fi'l-ardi cemî'an'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '3:47 → 5:17', 'kural': "okuma — harekesiz 'yaxluqu mâ yeşâ''", 'not': 'kalıp eşi.'},
 {'bag': '2:284 → 5:17', 'kural': "okuma — harekesiz 'yeşâ' ve'llâhu 'alâ kulli şey'in qadîr'", 'not': 'kalıp eşi.'},
 # blok 18-19
 {'bag': '3:129 → 5:18', 'kural': "okuma — harekesiz 'yağfiru li-men yeşâ'u ve yu'azzibu men yeşâ''", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '48:14 → 5:18', 'kural': "okuma — harekesiz 'yağfiru li-men yeşâ'u ve yu'azzibu men yeşâ''", 'not': "kalıp eşi; 'mulku's-semâvâti ve'l-ard' ile."},
 {'bag': '2:284 → 5:18', 'kural': "okuma — harekesiz 've yu'azzibu men yeşâ''", 'not': "kalıp eşi (ölçüm xref); 2:284'te 'fe' önekli."},
 {'bag': '30:20 → 5:18', 'kural': "okuma — harekesiz 'entum beşerun'", 'not': 'kalıp eşi.'},
 {'bag': '64:3 → 5:18', 'kural': "okuma — önek kesilmiş 've ileyhi'l-masîr'", 'not': 'kalıp eşi.'},
 {'bag': '5:17 → 5:18', 'kural': "sûre içi — harekesiz 've li'llâhi mulku's-semâvâti ve'l-ardi ve mâ beynehumâ'", 'not': 'bölüm içi kalıp eşi (ölçüm nakarat3).'},
 {'bag': '5:15 → 5:19', 'kural': "sûre içi — harekesiz 'yâ ehle'l-kitâbi qad câ'akum rasûlunâ yubeyyinu lekum'", 'not': "bölüm içi kalıp eşi (ölçüm nakarat3, xref); yedi kelimelik kalıp — genel hitap 'yâ ehle'l-kitâb' değil."},
 {'bag': '5:17 → 5:19', 'kural': "sûre içi — harekesiz 've'llâhu 'alâ kulli şey'in qadîr'", 'not': 'bölüm içi kalıp eşi (ölçüm nakarat3).'},
 # blok 20-23
 {'bag': '2:54 → 5:20', 'kural': "okuma — harekesiz 'qâle mûsâ li-qavmihî yâ qavmi'", 'not': 'kalıp eşi.'},
 {'bag': '61:5 → 5:20', 'kural': "okuma — harekesiz 'qâle mûsâ li-qavmihî yâ qavmi'", 'not': 'kalıp eşi.'},
 {'bag': '14:6 → 5:20', 'kural': "okuma — harekesiz 'zkurû ni'meta'llâhi 'aleykum iz'", 'not': "kalıp eşi (ölçüm xref); önek kesilmiş 've iz qâle mûsâ li-qavmih' sayımında ayrıca."},
 {'bag': '33:9 → 5:20', 'kural': "okuma — harekesiz 'zkurû ni'meta'llâhi 'aleykum iz'", 'not': 'kalıp eşi.'},
 {'bag': '5:11 → 5:20', 'kural': "sûre içi — lemma dizisi 'zekera ni'me allâh 'alâ iz'", 'not': "sûre içi lemma dizisi eşi (ölçüm nakarat3); harekesiz yazım farkı ('ni'me' ة / ت)."},
 {'bag': '3:149 → 5:21', 'kural': "okuma — önek kesilmiş 'fe-tenqalibû xâsirîn'", 'not': 'kalıp eşi.'},
 {'bag': '26:130 → 5:22', 'kural': "okuma — lemma 'cebbâr'", 'not': 'lemma eşi.'},
 # blok 24-26
 {'bag': '5:22 → 5:24', 'kural': "sûre içi — lemma dizisi 'inne len dexale'", 'not': "bölüm içi kalıp eşi (ölçüm nakarat3); harekesiz 'qâlû yâ mûsâ' açılışı da eş; önek farkı ('ve')."},
 {'bag': '9:86 → 5:24', 'kural': "okuma — lemma 'qâ'id'", 'not': 'lemma eşi.'},
 {'bag': '10:49 → 5:25', 'kural': "okuma — harekesiz 'lâ emliku'", 'not': 'kalıp eşi.'},
 {'bag': '28:34 → 5:25', 'kural': "okuma — önek kesilmiş 've exî'", 'not': 'kalıp eşi.'},
 {'bag': '61:5 → 5:25', 'kural': "okuma — harekesiz 'l-qavmi'l-fâsiqîn'", 'not': 'kalıp eşi.'},
 {'bag': '5:25 → 5:26', 'kural': "sûre içi — harekesiz 'l-qavmi'l-fâsiqîn'", 'not': 'blok içi kalıp eşi.'},
 {'bag': '46:15 → 5:26', 'kural': "okuma — harekesiz 'erba'îne sene'", 'not': 'kalıp eşi.'},
 # blok 27-30
 {'bag': '10:71 → 5:27', 'kural': "okuma — önek kesilmiş 've'tlu 'aleyhim nebe''", 'not': 'kalıp eşi.'},
 {'bag': '3:183 → 5:27', 'kural': "okuma — lemma 'qurbân'", 'not': 'lemma eşi.'},
 {'bag': '59:16 → 5:28', 'kural': "okuma — harekesiz 'innî exâfu'llâhe rabbe'l-'âlemîn'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '28:27 → 5:29', 'kural': "okuma — harekesiz 'innî urîd'", 'not': 'kalıp eşi.'},
 {'bag': '59:17 → 5:29', 'kural': "okuma — önek kesilmiş 've zâlike cezâ'u'z-zâlimîn'", 'not': 'kalıp eşi.'},
 # blok 31-32
 {'bag': '27:76 → 5:32', 'kural': "okuma — harekesiz ''alâ benî isrâ'îl'", 'not': 'kalıp eşi.'},
 {'bag': '18:74 → 5:32', 'kural': "okuma — harekesiz 'bi-ğayri nefs'", 'not': 'kalıp eşi.'},
 {'bag': '13:31 → 5:32', 'kural': "okuma — harekesiz 'n-nâse cemî'an'", 'not': 'kalıp eşi.'},
 {'bag': '57:25 → 5:32', 'kural': "okuma — harekesiz 'rusulunâ bi'l-beyyinât'", 'not': 'kalıp eşi.'},
 # blok 33-36
 {'bag': '9:107 → 5:33', 'kural': "okuma — lemma dizisi 'hârebe allâh rasûl'", 'not': 'lemma dizisi eşi (ölçüm xref).'},
 {'bag': '59:3 → 5:33', 'kural': "okuma — lemma dizisi 'fî dunyâ fî âxir 'azâb'", 'not': 'lemma dizisi eşi (ölçüm xref).'},
 {'bag': '13:18 → 5:36', 'kural': "okuma — harekesiz 'lev enne lehum mâ fi'l-ardi cemî'an ve mislehû me'ah'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '70:11 → 5:36', 'kural': "okuma — lemma 'iftedâ'", 'not': 'lemma eşi (ölçüm xref).'},
 # blok 37-40
 {'bag': '9:68 → 5:37', 'kural': "okuma — harekesiz 've lehum 'azâbun muqîm'", 'not': 'kalıp eşi.'},
 {'bag': '2:66 → 5:38', 'kural': "okuma — lemma 'nekâl'", 'not': 'lemma eşi.'},
 {'bag': '9:102 → 5:39', 'kural': "okuma — lemma dizisi 'tâbe 'alâ'", 'not': 'lemma dizisi eşi (ölçüm xref).'},
 {'bag': '2:107 → 5:40', 'kural': "okuma — harekesiz 'llâhe lehû mulku's-semâvâti ve'l-ard'", 'not': 'kalıp eşi (ölçüm xref).'},
 # blok 41-41
 {'bag': '3:176 → 5:41', 'kural': "okuma — önek kesilmiş 'lâ yahzunke'llezîne yusâri'ûne'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '2:114 → 5:41', 'kural': "okuma — harekesiz 'lehum fi'd-dunyâ xizyun'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '9:47 → 5:41', 'kural': "okuma — lemma 'semmâ''", 'not': 'lemma eşi.'},
 {'bag': '4:28 → 5:41', 'kural': "okuma — lemma dizisi 'erâde allâh en'", 'not': 'lemma dizisi eşi.'},
 # blok 42-44
 {'bag': '49:9 → 5:42', 'kural': "okuma — harekesiz 'llâhe yuhibbu'l-muqsitîn'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '24:47 → 5:43', 'kural': "okuma — önek kesilmiş 've mâ ulâ'ike bi'l-mu'minîn'", 'not': 'kalıp eşi.'},
 {'bag': '2:41 → 5:44', 'kural': "okuma — önek kesilmiş 've lâ teşterû bi-âyâtî semenen qalîlâ'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '3:79 → 5:44', 'kural': "okuma — lemma 'rabbâniyyîn'", 'not': 'lemma eşi.'},
 # blok 45-47
 {'bag': '2:178 → 5:45', 'kural': "okuma — lemma 'qısâs'", 'not': 'lemma eşi.'},
 {'bag': '57:27 → 5:46', 'kural': "okuma — önek kesilmiş 've âteynâhu'l-incîl'", 'not': 'kalıp eşi.'},
 {'bag': '3:138 → 5:46', 'kural': "okuma — önek kesilmiş 've hudan ve mev'izatan li'l-muttaqîn'", 'not': 'kalıp eşi (ölçüm xref).'},
 {'bag': '3:82 → 5:47', 'kural': "okuma — harekesiz 'fe-ulâ'ike humu'l-fâsiqûn'", 'not': 'kalıp eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_maide', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in MAIDE]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_maide'] = MAIDE
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_maide', len(MAIDE), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_maide', len(BAGLAR['AS_maide']))
