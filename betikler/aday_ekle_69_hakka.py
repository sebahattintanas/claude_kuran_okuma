# -*- coding: utf-8 -*-
"""aday_ekle_69_hakka.py — sûre 69 (Hâkka) adayları (AX_hakka) ve okuma bağları (AS_hakka).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

HAKKA = [
]

BAGLAR = {"AS_hakka": [
 # blok 1-10
 {'bag': '68:52 → 69:1', 'kural': "okuma — ardışık sûre sınırı; 'zikrun li'l-âlemîn' ile kapanış / 'el-hâqqa' ile açılış; fâsıla ن → ة (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '69:1 → 69:3', 'kural': "sûre içi — lemma 'hâqqa' (3 ayet): ad / soru / 'mâ edrâke' sorusu", 'not': 'sûre içi eş.'},
 {'bag': '26:141 → 69:4', 'kural': "lemma dizisi 'kezzebe + Semûd' (4 ayet) — 'kezzebet Semûdu'", 'not': 'kalıp eşi.'},
 {'bag': '54:23 → 69:4', 'kural': "lemma dizisi 'kezzebe + Semûd' (4 ayet) — 'bi'n-nuzur' / 'bi'l-qâri'a'", 'not': 'kalıp eşi.'},
 {'bag': '69:5 → 69:6', 'kural': "sûre içi — 'fe-emmâ … fe-uhlikû' / 've emmâ … fe-uhlikû' (biçim AMMA)", 'not': 'sûre içi eş.'},
 {'bag': '68:31 → 69:5', 'kural': "okuma — kök طغي: 'innâ kunnâ tâğîn' / 'bi't-tâğiya' (ardışık sûre)", 'not': 'ardışık sûre bağı.'},
 {'bag': '54:19 → 69:6', 'kural': "lemma dizisi 'rîh + sarsar' (3 ayet) — 1P 'erselnâ' / edilgen 'uhlikû'", 'not': 'kalıp eşi.'},
 {'bag': '41:16 → 69:6', 'kural': "lemma dizisi 'rîh + sarsar' (3 ayet) — 'rîhan sarsaran'", 'not': 'kalıp eşi.'},
 {'bag': '54:20 → 69:7', 'kural': "lemma dizisi 'a'câz + nahl' (2 ayet) — 'munqa'ir' / 'hâviya'; 54:19-20 ile 69:6-7 aynı sıra", 'not': 'kalıp eşi.'},
 {'bag': '27:52 → 69:7', 'kural': "okuma — lemma 'hâviya': 'buyûtuhum hâviyeten' / 'a'câzu nahlin hâviya'", 'not': 'lemma eşi.'},
 {'bag': '67:3 → 69:8', 'kural': "lemma dizisi 'hel + ra'â' (3 ayet) — 'hel terâ min futûr' / 'hel terâ lehum min bâqiya'", 'not': 'kalıp eşi.'},
 {'bag': '69:7 → 69:8', 'kural': "sûre içi — kök رأي: 'fe-terâ' / 'fe-hel terâ'", 'not': 'sûre içi eş.'},
 {'bag': '53:53 → 69:9', 'kural': "okuma — lemma 'mu'tefika' (3 ayet)", 'not': 'lemma eşi.'},
 {'bag': '54:42 → 69:10', 'kural': "lemma dizisi 'ehaze + ahz' (3 ayet) — 1P 'ehaznâhum' / 3MS 'ehazehum'", 'not': 'kalıp eşi.'},
 {'bag': '11:102 → 69:10', 'kural': "okuma — lemma 'ahz': 'ahzu rabbike' / 'ahzeten râbiya'", 'not': 'lemma eşi.'},
 # blok 11-20
 {'bag': '69:5 → 69:11', 'kural': "sûre içi — kök طغي: 'et-tâğiya' (helâk) / 'tağe'l-mâ'' (suyun taşması)", 'not': 'sûre içi eş.'},
 {'bag': '36:41 → 69:11', 'kural': "okuma — 1P 'hamalnâ' + taşıyan gemi", 'not': 'kurgu eşi.'},
 {'bag': '51:3 → 69:11', 'kural': "okuma — lemma 'câriya' (3 ayet)", 'not': 'lemma eşi.'},
 {'bag': '56:73 → 69:12', 'kural': "okuma — 1P 'ce'ale' + 'tezkira': 'ce'alnâhâ tezkiraten' / 'li-nec'alehâ … tezkiraten'", 'not': 'kurgu eşi.'},
 {'bag': '39:68 → 69:13', 'kural': "lemma dizisi 'nefeha + fî + sûr' (10 ayet) — iki üfürüş / 'nefhatun vâhida'", 'not': 'kalıp eşi.'},
 {'bag': '69:13 → 69:14', 'kural': "sûre içi — 'nefhatun vâhida' / 'dekketen vâhida'", 'not': 'sûre içi eş.'},
 {'bag': '56:1 → 69:15', 'kural': "lemma dizisi 'veqa'a + vâqi'a' (2 ayet) — 'izâ' şartı / 'fe-yevme'izin' cevabı", 'not': 'kalıp eşi.'},
 {'bag': '55:37 → 69:16', 'kural': "lemma dizisi 'inşaqqa + semâ'' (2 ayet) — 'verdeten ke'd-dihân' / 'vâhiya'", 'not': 'kalıp eşi.'},
 {'bag': '40:7 → 69:17', 'kural': "lemma dizisi 'hamale + arş' (2 ayet) — mevsûl taşıyanlar / 'semâniya'", 'not': 'kalıp eşi.'},
 {'bag': '69:7 → 69:17', 'kural': "sûre içi — kök ثمن: 'semâniyete eyyâm' / 'semâniya'", 'not': 'sûre içi eş.'},
 {'bag': '69:11 → 69:17', 'kural': "sûre içi — lemma 'hamale' üç geçiş (69:11, 14, 17)", 'not': 'sûre içi eş.'},
 {'bag': '18:48 → 69:18', 'kural': "okuma — lemma 'arada' edilgen: 3MP 'urıdû' / 2MP 'tu'radûne'", 'not': 'lemma eşi.'},
 {'bag': '17:71 → 69:19', 'kural': "lemma dizisi 'men + âtâ + kitâb + yemîn' (3 ayet) / xref — 'yaqra'ûne kitâbehum' / 'iqra'û kitâbiyeh'", 'not': 'kalıp eşi.'},
 {'bag': '69:19 → 69:20', 'kural': "sûre içi — 'kitâbiyeh' / 'hisâbiyeh' (fâsıla ه)", 'not': 'sûre içi eş.'},
 # blok 21-30
 {'bag': '52:19 → 69:24', 'kural': "lemma dizisi 'ekele + şeribe + henî'' (3 ayet) / xref — 'bi-mâ kuntum ta'melûn' / 'bi-mâ esleftum'", 'not': 'kalıp eşi.'},
 {'bag': '10:30 → 69:24', 'kural': "lemma dizisi 'mâ + eslefe' (2 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '69:19 → 69:25', 'kural': "sûre içi — 'emmâ men ûtiye kitâbehû': 'bi-yemînihî' / 'bi-şimâlihî' (nakarat3, karşıt çift aday 1039)", 'not': 'sûre içi eş.'},
 {'bag': '56:41 → 69:25', 'kural': "okuma — lemma 'şimâl': 'ashâbu'ş-şimâl' / 'bi-şimâlihî'", 'not': 'lemma eşi.'},
 {'bag': '18:42 → 69:25', 'kural': "lemma dizisi 'leyt + lem' (3 ayet) — 'yâ leytenî lem'", 'not': 'kalıp eşi.'},
 {'bag': '25:28 → 69:25', 'kural': "lemma dizisi 'leyt + lem' (3 ayet) — 'leytenî lem'", 'not': 'kalıp eşi.'},
 {'bag': '69:20 → 69:26', 'kural': "sûre içi — kök حسب: 'mulâqin hisâbiyeh' / 'lem edri mâ hisâbiyeh' (karşıt çift aday 1039)", 'not': 'sûre içi eş.'},
 {'bag': '69:3 → 69:26', 'kural': "sûre içi — kök دري: 'mâ edrâke' / 'lem edri'", 'not': 'sûre içi eş.'},
 {'bag': '26:207 → 69:28', 'kural': "okuma — lemma 'ağnâ': 'mâ ağnâ anhum' / 'mâ ağnâ annî'", 'not': 'lemma eşi.'},
 {'bag': '69:6 → 69:29', 'kural': "sûre içi — kök هلك: 'fe-uhlikû' (kavimler) / 'heleke' (güç)", 'not': 'sûre içi eş.'},
 {'bag': '44:47 → 69:30', 'kural': "harekesiz kalıp 'huzûhu' (2 ayet) — 'fa'tilûhu' / 'fe-ğullûh'", 'not': 'kalıp eşi.'},
 # blok 31-41
 {'bag': '40:71 → 69:32', 'kural': "okuma — lemma 'silsile': 've's-selâsilu' / 'fî silsiletin … seb'ûne zirâ'â'", 'not': 'lemma eşi.'},
 {'bag': '18:18 → 69:32', 'kural': "okuma — lemma 'zirâ'': kol (organ) / arşın (birim)", 'not': 'lemma eşi.'},
 {'bag': '69:7 → 69:32', 'kural': "sûre içi — kök سبع: 'seb'a leyâl' / 'seb'ûne zirâ'â'", 'not': 'sûre içi eş.'},
 {'bag': '24:15 → 69:33', 'kural': "lemma dizisi 'Allâh + azîm' (3 ayet) — haber / lafzın sıfatı", 'not': 'kalıp eşi.'},
 {'bag': '68:24 → 69:34', 'kural': "okuma — 'miskîn' ardışık sûrede: bahçeye girmesin denen / doyurulmayan (1040 değil)", 'not': 'ardışık sûre bağı.'},
 {'bag': '26:101 → 69:35', 'kural': "okuma — 'hamîm' (candan yakın): 've lâ sadîqin hamîm' / 'leyse lehu … hamîm'", 'not': 'lemma eşi.'},
 {'bag': '69:34 → 69:36', 'kural': "sûre içi — kök طعم: yoksula yedirmeyen / yiyeceği yok", 'not': 'sûre içi eş.'},
 {'bag': '69:9 → 69:37', 'kural': "sûre içi — kök خطأ: 'bi'l-hâti'a' / 'el-hâti'ûn'", 'not': 'sûre içi eş.'},
 {'bag': '69:24 → 69:37', 'kural': "sûre içi — kök أكل: 'kulû' / 'lâ ye'kuluhû' (karşıt çift aday 1039)", 'not': 'sûre içi eş.'},
 {'bag': '56:75 → 69:38', 'kural': "harekesiz kalıp 'fe-lâ uqsimu' (5 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '69:38 → 69:39', 'kural': "sûre içi — 'bi-mâ tubsirûn' / 've mâ lâ tubsirûn' (karşıt çift aday 1039)", 'not': 'sûre içi eş.'},
 {'bag': '69:40 → 69:41', 'kural': "sûre içi — 'qavlu rasûlin kerîm' / 'qavli şâ'ir' (karşıt çift aday 1039)", 'not': 'sûre içi eş.'},
 {'bag': '52:30 → 69:41', 'kural': "okuma — lemma 'şâ'ir': 'em yeqûlûne şâ'irun' / 've mâ huve bi-qavli şâ'ir'", 'not': 'lemma eşi.'},
 {'bag': '37:36 → 69:41', 'kural': "okuma — lemma 'şâ'ir': 'li-şâ'irin mecnûn' / 'qavli şâ'ir'", 'not': 'lemma eşi.'},
 # blok 42-52
 {'bag': '52:29 → 69:42', 'kural': "okuma — lemma 'kâhin' (2 ayet): 'bi-kâhinin ve lâ mecnûn' / 'qavli kâhin'", 'not': 'lemma eşi.'},
 {'bag': '69:41 → 69:42', 'kural': "sûre içi — 'qalîlen mâ tu'minûn' / 'qalîlen mâ tezekkerûn'; şâ'ir / kâhin", 'not': 'sûre içi eş.'},
 {'bag': '27:62 → 69:42', 'kural': "lemma dizisi 'qalîl + mâ + tezekkera' (4 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '56:80 → 69:43', 'kural': "esit2 (TAM) — 'tenzîlun min rabbi'l-âlemîn'", 'not': 'tekrar ayet.'},
 {'bag': '52:33 → 69:44', 'kural': "okuma — lemma 'teqavvele' (2 ayet): iddia / şart", 'not': 'lemma eşi.'},
 {'bag': '69:19 → 69:45', 'kural': "sûre içi — lemma 'yemîn': 'bi-yemînihî' / 'bi'l-yemîn'", 'not': 'sûre içi eş.'},
 {'bag': '69:10 → 69:45', 'kural': "sûre içi — kök أخذ: 3MS 'ehazehum' / 1P 'le-ehaznâ'", 'not': 'sûre içi eş.'},
 {'bag': '27:61 → 69:47', 'kural': "okuma — lemma 'hâciz' (2 ayet): iki deniz arası engel / engel olacak kimse", 'not': 'lemma eşi.'},
 {'bag': '69:12 → 69:48', 'kural': "sûre içi — lemma 'tezkira': 'li-nec'alehâ lekum tezkiraten' / 'le-tezkiratun li'l-muttaqîn'", 'not': 'sûre içi eş.'},
 {'bag': '68:8 → 69:49', 'kural': "okuma — lemma 'mukezzib' ardışık sûrede (1040 değil)", 'not': 'ardışık sûre bağı.'},
 {'bag': '69:48 → 69:50', 'kural': "sûre içi — 'innehû le-tezkiratun li'l-muttaqîn' / 'innehû le-hasratun ale'l-kâfirîn' (karşıt çift aday 1039)", 'not': 'sûre içi eş.'},
 {'bag': '56:95 → 69:51', 'kural': "lemma dizisi 'haqq + yaqîn' (2 ayet) — 'haqqu'l-yaqîn'", 'not': 'kalıp eşi.'},
 {'bag': '69:1 → 69:51', 'kural': "sûre içi — kök حقق: 'el-hâqqa' (açılış) / 'haqqu'l-yaqîn' (kapanışa bir ayet)", 'not': 'sûre içi eş.'},
 {'bag': '56:96 → 69:52', 'kural': "esit2 (TAM) — 'fe-sebbih bi'smi rabbike'l-azîm'; 56:95-96 ile 69:51-52 aynı sıra", 'not': 'tekrar ayet.'},
 {'bag': '69:33 → 69:52', 'kural': "sûre içi — 'el-azîm': lafzın sıfatı / Rabbin sıfatı", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_hakka', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in HAKKA]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_hakka'] = HAKKA
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_hakka', len(HAKKA), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_hakka', len(BAGLAR['AS_hakka']))
