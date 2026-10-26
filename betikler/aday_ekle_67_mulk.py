# -*- coding: utf-8 -*-
"""aday_ekle_67_mulk.py — sûre 67 (Mülk) adayları (AX_mulk) ve okuma bağları (AS_mulk).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

MULK = [
]

BAGLAR = {"AS_mulk": [
 # blok 1-10
 {'bag': '66:12 → 67:1', 'kural': "okuma — ardışık sûre sınırı; örnek anlatısıyla kapanış / övgüyle açılış; fâsıla ن → ر; ortak kök yok (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '25:1 → 67:1', 'kural': "okuma — lemma 'tebâreke' + mevsûl: sıla indirme / mülkün elde oluşu", 'not': 'lemma eşi.'},
 {'bag': '64:1 → 67:1', 'kural': "okuma — 'mulk' + 'alâ kulli şey'in qadîr' aynı ayette (ardışık değil, okuma bağı)", 'not': 'kalıp eşi.'},
 {'bag': '65:12 → 67:1', 'kural': "kalıp — 'alâ kulli şey'in qadîr' (33 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '11:7 → 67:2', 'kural': "xref (ölçüm) — 'li-yebluvekum eyyukum ahsenu amelâ': göklerin ve yerin yaratılışı / ölümün ve hayatın yaratılışı", 'not': 'xref eşi.'},
 {'bag': '18:7 → 67:2', 'kural': "xref (ölçüm) — 'li-nebluvehum eyyuhum ahsenu amelâ' (1P, 3MP) / 3MS, 2MP", 'not': 'xref eşi.'},
 {'bag': '35:28 → 67:2', 'kural': "lemma dizisi — 'azîz + ğafûr' (2 ayet): lafızla nekre / zamirle marife", 'not': 'ortak kapanış.'},
 {'bag': '67:1 → 67:2', 'kural': "sûre içi — mevsûl 'ellezî' ile süren övgü", 'not': 'sûre içi eş.'},
 {'bag': '65:12 → 67:3', 'kural': "xref (ölçüm) — 'ellezî haleqa seb'a semâvât': lafızla ve yerle / mevsûlle, yersiz (ardışık değil, okuma bağı)", 'not': 'xref eşi.'},
 {'bag': '67:2 → 67:3', 'kural': "sûre içi — kök خلق: 'haleqa'l-mevt' / 'haleqa seb'a semâvât', 'halqi'r-rahmân'", 'not': 'sûre içi eş.'},
 {'bag': '67:3 → 67:4', 'kural': "lemma dizisi — 'race'a + basar' (2 ayet, ikisi sûre içi): 'fe'rci'' / 'summe'rci' … kerrateyn'", 'not': 'sûre içi pekiştirme.'},
 {'bag': '41:12 → 67:5', 'kural': "xref (ölçüm) — 'zeyyenne's-semâ'e'd-dunyâ bi-mesâbîh': 've hifzâ' / 've ce'alnâhâ rucûmâ'", 'not': 'xref eşi.'},
 {'bag': '37:6 → 67:5', 'kural': "xref (ölçüm) — 'zeyyenne's-semâ'e'd-dunyâ': 'bi-zîneti'l-kevâkib' / 'bi-mesâbîh'", 'not': 'xref eşi.'},
 {'bag': '18:7 → 67:5', 'kural': "okuma — kök زين: yeryüzünün süsü / dünya göğünün süsü", 'not': 'kök eşi.'},
 {'bag': '67:3 → 67:5', 'kural': "sûre içi — lemma 'semâ'': yedi gök / dünya göğü", 'not': 'sûre içi eş.'},
 {'bag': '66:9 → 67:6', 'kural': "lemma dizisi — 'bi'se + masîr' (11 ayet), ikisinde de cehennem (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '67:5 → 67:6', 'kural': "sûre içi — kök عذب: 'azâbe's-sa'îr' (şeytanlar) / 'azâbu cehennem' (inkâr edenler)", 'not': 'sûre içi eş.'},
 {'bag': '11:106 → 67:7', 'kural': "okuma — lemma 'şehîq' (2 ayet): ateştekilerin sesi / ateşin sesi", 'not': 'lemma eşi.'},
 {'bag': '11:40 → 67:7', 'kural': "okuma — lemma 'fâra': tennûr / cehennem", 'not': 'lemma eşi.'},
 {'bag': '67:7 → 67:8', 'kural': "sûre içi — lemma 'elqâ' edilgen: 'ulqû' / 'ulqiye' (لقي [2/2])", 'not': 'sûre içi eş.'},
 {'bag': '39:71 → 67:8', 'kural': "okuma — 'hazanetuhâ e-lem ye'tikum': 'rusulun minkum' / 'nezîr'", 'not': 'kalıp eşi.'},
 {'bag': '39:71 → 67:9', 'kural': "lemma dizisi — 'qâle + belâ' (10 ayet): onay + azap sözünün hak oluşu / onay + yalanlamanın itirafı", 'not': 'kalıp eşi.'},
 {'bag': '67:8 → 67:9', 'kural': "sûre içi — soru-cevap: 'e-lem ye'tikum nezîr' / 'belâ qad câ'enâ nezîr' (نذر)", 'not': 'sûre içi eş.'},
 {'bag': '25:44 → 67:10', 'kural': "lemma dizisi — 'semi'a + ev + aqale' (2 ayet): 2MS'ye sorulan 3MP durum / 1P itiraf", 'not': 'kalıp eşi.'},
 {'bag': '35:6 → 67:10', 'kural': "xref (ölçüm) — 'ashâbi's-sa'îr': şeytanın taraftarlarını çağırdığı yer / kendi itirafları", 'not': 'xref eşi.'},
 {'bag': '67:5 → 67:10', 'kural': "sûre içi — kök سعر: 'azâbe's-sa'îr' / 'ashâbi's-sa'îr'", 'not': 'sûre içi eş.'},
 {'bag': '67:7 → 67:10', 'kural': "sûre içi — kök سمع: cehennemin sesini işitme / dünyada dinleme", 'not': 'sûre içi eş.'},
 # blok 11-20
 {'bag': '40:11 → 67:11', 'kural': "lemma dizisi — 'i'terafe + zenb' (3 ayet): 1P itiraf 'zunûbinâ' / 3MP anlatı 'zenbihim'", 'not': 'kalıp eşi.'},
 {'bag': '9:102 → 67:11', 'kural': "lemma dizisi — 'i'terafe + zenb' (3 ayet): dünyada itiraf / cehennemde itiraf", 'not': 'kalıp eşi.'},
 {'bag': '67:10 → 67:11', 'kural': "sûre içi — 'ashâbi's-sa'îr' ×2 (lemma dizisi 3 ayet: 35:6, 67:10, 67:11)", 'not': 'sûre içi eş.'},
 {'bag': '21:49 → 67:12', 'kural': "xref (ölçüm) — 'ellezîne yahşevne rabbehum bi'l-ğayb'", 'not': 'xref eşi.'},
 {'bag': '35:18 → 67:12', 'kural': "xref (ölçüm) — 'yahşevne rabbehum bi'l-ğayb': uyarının yararlandığı kişiler / karşılık", 'not': 'xref eşi.'},
 {'bag': '35:7 → 67:12', 'kural': "xref (ölçüm) — 'lehum mağfiretun ve ecrun kebîr': aynı ayette azap / mağfiret karşıtı; burada ardışık ayetlerde", 'not': 'xref eşi.'},
 {'bag': '11:11 → 67:12', 'kural': "xref (ölçüm) — 'lehum mağfiretun ve ecrun kebîr'", 'not': 'xref eşi.'},
 {'bag': '67:11 → 67:12', 'kural': "sûre içi — 'fe-suhqan li-ashâbi's-sa'îr' / 'lehum mağfiretun ve ecrun kebîr' (karşıt çift, okuma)", 'not': 'sûre içi karşıt.'},
 {'bag': '67:6 → 67:12', 'kural': "sûre içi — Rab ×2 (ربب [2/2]): 'keferû bi-rabbihim' / 'yahşevne rabbehum'", 'not': 'sûre içi karşıt.'},
 {'bag': '67:9 → 67:12', 'kural': "sûre içi — 'kebîr' ×2 (كبر [2/2]): 'dalâlin kebîr' / 'ecrun kebîr'", 'not': 'sûre içi eş.'},
 {'bag': '13:10 → 67:13', 'kural': "xref (ölçüm) — 'esarra'l-qavle … cehera bih': eşitlik cümlesi / muhayyer emir", 'not': 'xref eşi.'},
 {'bag': '22:63 → 67:14', 'kural': "lemma dizisi — 'latîf + habîr' (5 ayet): lafızla nekre / zamirle marife", 'not': 'ortak kapanış.'},
 {'bag': '67:13 → 67:14', 'kural': "sûre içi — kök علم: 'alîm' / 'ya'lemu'", 'not': 'sûre içi eş.'},
 {'bag': '67:2 → 67:14', 'kural': "sûre içi — kök خلق dört geçiş (67:2, 67:3 ×2, 67:14)", 'not': 'sûre içi eş.'},
 {'bag': '34:15 → 67:15', 'kural': "lemma dizisi — 'ekele + min + rizq' (2 ayet): Sebe' bahçeleri / yeryüzü", 'not': 'kalıp eşi.'},
 {'bag': '35:9 → 67:15', 'kural': "okuma — lemma 'nuşûr': ölü yerin diriltilmesi benzetmesi / yerde yürüyüşten dönüş", 'not': 'lemma eşi.'},
 {'bag': '67:5 → 67:15', 'kural': "sûre içi — kök جعل: 1P 'ce'alnâhâ' / 3MS 'ce'ale'", 'not': 'sûre içi eş.'},
 {'bag': '67:16 → 67:17', 'kural': "nakarat3 (GEÇER) — 'e-emintum men fi's-semâ'i en': batırma / taş yağdırma", 'not': 'sûre içi tekrar.'},
 {'bag': '17:68 → 67:16', 'kural': "okuma — 'emine' + 'hasefe' aynı soruda; 'yursile aleykum hâsibâ' 67:17'de (tek ayet / iki ayet)", 'not': 'kalıp eşi.'},
 {'bag': '29:40 → 67:16', 'kural': "lemma dizisi — 'hasefe + ard' (3 ayet): geçmişte yapılan / tehdit", 'not': 'kalıp eşi.'},
 {'bag': '52:9 → 67:16', 'kural': "okuma — lemma 'temûr' (2 ayet): gök / yer", 'not': 'lemma eşi.'},
 {'bag': '67:15 → 67:16', 'kural': "sûre içi — 'el-ard': 'zelûl' / 'temûr' (okuma)", 'not': 'sûre içi karşıt.'},
 {'bag': '17:68 → 67:17', 'kural': "okuma — lemma 'hâsib': 'yursile aleykum hâsibâ' aynı kalıp", 'not': 'lemma eşi.'},
 {'bag': '29:40 → 67:17', 'kural': "okuma — lemma 'hâsib': 'erselnâ aleyhi hâsibâ' (geçmiş) / tehdit", 'not': 'lemma eşi.'},
 {'bag': '67:8 → 67:17', 'kural': "sûre içi — 'nezîr': uyarıcı / 1S uyarım (iki anlam)", 'not': 'sûre içi eş.'},
 {'bag': '35:25 → 67:18', 'kural': "lemma dizisi — 'qad kezzebe'llezîne min qablihim' (2 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '35:26 → 67:18', 'kural': "lemma dizisi — 'keyfe kâne nekîr' (4 ayet): iki ayete yayılan / tek ayette", 'not': 'kalıp eşi.'},
 {'bag': '67:9 → 67:18', 'kural': "sûre içi — kök كذب: 'kezzebnâ' (itiraf) / 'kezzebe' (öncekiler)", 'not': 'sûre içi eş.'},
 {'bag': '67:17 → 67:18', 'kural': "sûre içi — 1S düşmüş zamir 'nezîr' / 'nekîr'; 'keyfe' ×2", 'not': 'sûre içi eş.'},
 {'bag': '16:79 → 67:19', 'kural': "lemma dizisi — 'lem yerav ile't-tayr … mâ yumsikuhunne illâ' (2 ayet): 'ille'llâh' / 'ille'r-rahmân'", 'not': 'kalıp eşi.'},
 {'bag': '24:41 → 67:19', 'kural': "okuma — lemma 'sâffa' (3 ayet): kuşlar 'sâffât'", 'not': 'lemma eşi.'},
 {'bag': '67:3 → 67:19', 'kural': "sûre içi — kök بصر: 'el-basar' (insan bakışı) / 'basîr' (ilâhî) (aday 1041 alanına sınırda, kayıt); gözlem çağrısı eşi", 'not': 'sûre içi eş.'},
 {'bag': '67:1 → 67:19', 'kural': "sûre içi — 'kulli şey'': 'qadîr' / 'basîr'", 'not': 'sûre içi eş.'},
 {'bag': '67:9 → 67:20', 'kural': "okuma — HASR 'in … illâ fî': 'dalâlin kebîr' (inkârcıların sözü) / 'ğurûr' (inkârcılar hakkında)", 'not': 'kurgu eşi.'},
 {'bag': '67:6 → 67:20', 'kural': "sûre içi — kök كفر: 'keferû' / 'el-kâfirûn'", 'not': 'sûre içi eş.'},
 # blok 21-30
 {'bag': '67:20 → 67:21', 'kural': "nakarat3 (GEÇMEZ) — 'em-men hâzâ'llezî': yardım edecek ordu / rızıklandıran", 'not': 'sûre içi tekrar.'},
 {'bag': '67:19 → 67:21', 'kural': "sûre içi — kök مسك: kuşları havada tutma / rızkı alıkoyma (iki anlam)", 'not': 'sûre içi eş.'},
 {'bag': '67:15 → 67:21', 'kural': "sûre içi — kök رزق: 'kulû min rizqihî' / 'yerzuqukum … rizqahû'", 'not': 'sûre içi eş.'},
 {'bag': '23:75 → 67:21', 'kural': "okuma — lemma 'lecce' (2 ayet): 'fî tuğyânihim' / 'fî utuvvin ve nufûr'", 'not': 'lemma eşi.'},
 {'bag': '25:21 → 67:21', 'kural': "okuma — lemma 'utuvv' (2 ayet)", 'not': 'lemma eşi.'},
 {'bag': '19:43 → 67:22', 'kural': "okuma — lemma 'sevî': yolun sıfatı / yürüyenin hâli; 'sırât' ikisinde de", 'not': 'lemma eşi.'},
 {'bag': '1:6 → 67:22', 'kural': "lemma dizisi — 'sırât + mustaqîm' (31 ayet): 'ihdinâ' / 'ehdâ'", 'not': 'kalıp eşi.'},
 {'bag': '67:15 → 67:22', 'kural': "sûre içi — kök مشي: 'imşû fî menâkibihâ' / 'yemşî' ×2", 'not': 'sûre içi eş.'},
 {'bag': '23:78 → 67:23', 'kural': "esit2 (BENZER 0,9263) — 'enşe'e lekumu's-sem'a ve'l-ebsâra ve'l-ef'ide qalîlen mâ teşkurûn'", 'not': 'benzer ayet.'},
 {'bag': '32:9 → 67:23', 'kural': "xref (ölçüm) — 've ce'ale lekumu's-sem'a ve'l-ebsâra ve'l-ef'ide qalîlen mâ teşkurûn'", 'not': 'xref eşi.'},
 {'bag': '23:79 → 67:24', 'kural': "esit2 (BENZER 0,9492) — 'ellezî zere'ekum fi'l-ardi ve ileyhi tuhşerûn'; 23:78-79 ↔ 67:23-24 sıralı eşleşme (ardışık değil, okuma bağı)", 'not': 'benzer ayet.'},
 {'bag': '67:23 → 67:24', 'kural': "nakarat3 (GEÇMEZ) — 'qul huve'llezî': var etme / yayma", 'not': 'sûre içi tekrar.'},
 {'bag': '67:15 → 67:24', 'kural': "sûre içi — 'ileyhi'n-nuşûr' / 'ileyhi tuhşerûn'", 'not': 'sûre içi eş.'},
 {'bag': '36:48 → 67:25', 'kural': "esit2 (YAKIN 0,9825) — 've yeqûlûne metâ hâze'l-va'du in kuntum sâdiqîn' (6 ayet)", 'not': 'tekrar ayet.'},
 {'bag': '46:23 → 67:26', 'kural': "lemma dizisi — 'innema'l-ilmu inda'llâh' (4 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '29:50 → 67:26', 'kural': "xref (ölçüm) — 'innemâ … inda'llâhi ve innemâ ene nezîrun mubîn': 'el-âyât' / 'el-ilm'", 'not': 'xref eşi.'},
 {'bag': '67:25 → 67:26', 'kural': "sûre içi — soru-cevap: 'metâ hâze'l-va'd' / 'innema'l-ilmu inda'llâh'", 'not': 'sûre içi eş.'},
 {'bag': '17:7 → 67:27', 'kural': "lemma dizisi — 'sâ'e + vech' (2 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '36:57 → 67:27', 'kural': "okuma — lemma 'iddeâ': cennettekilerin istedikleri / inkârcıların çağırdığı", 'not': 'lemma karşıtı.'},
 {'bag': '67:25 → 67:27', 'kural': "sûre içi — 'el-va'd' → 'ra'evhu' (zamir göndergesi, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '67:28 → 67:30', 'kural': "nakarat3 (GEÇMEZ) — 'qul e-ra'eytum in': helâk / suyun çekilmesi", 'not': 'sûre içi tekrar.'},
 {'bag': '67:3 → 67:28', 'kural': "sûre içi — kök رحم: 'er-rahmân' / 'rahimenâ'", 'not': 'sûre içi eş.'},
 {'bag': '67:9 → 67:29', 'kural': "sûre içi — kök ضلل: 'dalâlin kebîr' / 'dalâlin mubîn'", 'not': 'sûre içi eş.'},
 {'bag': '67:26 → 67:29', 'kural': "sûre içi — 'mubîn': 'nezîrun mubîn' / 'dalâlin mubîn' (iki karşı gönderge)", 'not': 'sûre içi eş.'},
 {'bag': '67:17 → 67:29', 'kural': "sûre içi — 'fe-se-ta'lemûn' ×2: 'keyfe nezîr' / 'men huve fî dalâlin mubîn'", 'not': 'sûre içi eş.'},
 {'bag': '18:41 → 67:30', 'kural': "xref (ölçüm) — 'asbaha mâ'u- ğavran': 'fe-len testetî'a lehû talebâ' / 'fe-men ye'tîkum bi-mâ'in ma'în'", 'not': 'xref eşi.'},
 {'bag': '23:50 → 67:30', 'kural': "okuma — lemma 'ma'în': 'zâti qarârin ve ma'în' / 'bi-mâ'in ma'în'", 'not': 'lemma eşi.'},
 {'bag': '67:1 → 67:30', 'kural': "sûre içi — açılış övgü ve mülkle, kapanış cevapsız soruyla (okuma)", 'not': 'sûre çerçevesi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_mulk', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in MULK]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_mulk'] = MULK
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_mulk', len(MULK), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_mulk', len(BAGLAR['AS_mulk']))
