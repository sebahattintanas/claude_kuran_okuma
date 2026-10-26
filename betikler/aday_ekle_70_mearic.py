# -*- coding: utf-8 -*-
"""aday_ekle_70_mearic.py — sûre 70 (Meâric) adayları (AX_mearic) ve okuma bağları (AS_mearic).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

MEARIC = [
]

BAGLAR = {"AS_mearic": [
 # blok 1-10
 {'bag': '69:52 → 70:1', 'kural': "okuma — ardışık sûre sınırı; 'fe-sebbih bi'smi rabbike'l-azîm' ile kapanış / 'se'ele sâ'ilun' ile açılış; fâsıla م → ع (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '52:7 → 70:1', 'kural': "okuma — lemma 'azâb' + 'vâqi'': 'inne azâbe rabbike le-vâqi'' / 'bi-azâbin vâqi''", 'not': 'lemma eşi.'},
 {'bag': '52:8 → 70:2', 'kural': "lemma 'dâfi'' (2 ayet) — 52:7-8 ile 70:1-2 aynı sıra", 'not': 'lemma eşi.'},
 {'bag': '43:33 → 70:3', 'kural': "lemma 'me'âric' (2 ayet) — evlere basamaklar / 'zi'l-me'âric'", 'not': 'lemma eşi.'},
 {'bag': '70:3 → 70:4', 'kural': "sûre içi — kök عرج: 'me'âric' / 'ta'ruc'", 'not': 'sûre içi eş.'},
 {'bag': '32:5 → 70:4', 'kural': "lemma dizisi 'yevm + kâne + miqdâr' (2 ayet) / xref — 'elfe sene' / 'hamsîne elfe sene'", 'not': 'kalıp eşi.'},
 {'bag': '22:47 → 70:4', 'kural': "okuma — 'elf sene' ölçüsü: 'ke-elfi senetin' / 'hamsîne elfe sene'", 'not': 'kurgu eşi.'},
 {'bag': '29:14 → 70:4', 'kural': "lemma 'hamsîn' (2 ayet) — 'elfe senetin illâ hamsîne' / 'hamsîne elfe sene'", 'not': 'lemma eşi.'},
 {'bag': '16:2 → 70:4', 'kural': "lemma dizisi 'melek + rûh' (3 ayet) — iniş / yükseliş", 'not': 'kalıp eşi.'},
 {'bag': '12:18 → 70:5', 'kural': "lemma dizisi 'sabr + cemîl' (3 ayet) — 'fe-sabrun cemîl' / 'sabran cemîlâ'", 'not': 'kalıp eşi.'},
 {'bag': '12:83 → 70:5', 'kural': "lemma dizisi 'sabr + cemîl' (3 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '68:48 → 70:5', 'kural': "okuma — 2MS emir 'fe'sbir'", 'not': 'kurgu eşi.'},
 {'bag': '21:109 → 70:6', 'kural': "okuma — lemma 'qarîb' + 'ba'îd' aynı ayette / 70:6-7'de iki ayete bölünmüş", 'not': 'lemma eşi.'},
 {'bag': '70:6 → 70:7', 'kural': "sûre içi — 'yeravnehû ba'îdâ' / 'nerâhu qarîbâ' (karşıt çift aday 1039)", 'not': 'sûre içi eş.'},
 {'bag': '18:29 → 70:8', 'kural': "lemma 'muhl' (3 ayet) — suyun teşbihi / göğün teşbihi", 'not': 'lemma eşi.'},
 {'bag': '44:45 → 70:8', 'kural': "lemma 'muhl' (3 ayet) — karınlarda kaynayanın teşbihi / göğün teşbihi", 'not': 'lemma eşi.'},
 {'bag': '69:16 → 70:8', 'kural': "okuma — ardışık sûre; gök: 'inşaqqati's-semâ'' / 'tekûnu's-semâ'u ke'l-muhl'", 'not': 'ardışık sûre bağı.'},
 {'bag': '69:14 → 70:9', 'kural': "okuma — ardışık sûre; dağlar: 'humileti'l-ardu ve'l-cibâl' / 'tekûnu'l-cibâlu ke'l-'ihn'", 'not': 'ardışık sûre bağı.'},
 {'bag': '70:8 → 70:9', 'kural': "sûre içi — 'tekûnu' + ad + 'ke-' teşbih, iki ayet koşut", 'not': 'sûre içi eş.'},
 {'bag': '69:35 → 70:10', 'kural': "okuma — ardışık sûre; 'hamîm' yakın dost anlamında", 'not': 'ardışık sûre bağı.'},
 {'bag': '70:1 → 70:10', 'kural': "sûre içi — lemma 'se'ele': soran / sormayan", 'not': 'sûre içi eş.'},
 # blok 11-20
 {'bag': '39:47 → 70:11', 'kural': "okuma — lemma 'iftedâ' + 'mâ fi'l-ardi cemî'an' + azap tek ayette / 70:11-14'e yayılmış", 'not': 'kurgu eşi.'},
 {'bag': '10:54 → 70:11', 'kural': "okuma — lemma 'iftedâ': 'le'ftedet bih' / 'lev yeftedî'", 'not': 'lemma eşi.'},
 {'bag': '15:2 → 70:11', 'kural': "okuma — 'vedde … lev' dileği", 'not': 'kurgu eşi.'},
 {'bag': '68:9 → 70:11', 'kural': "okuma — 'vedde … lev' dileği (ardışık olmayan sûre)", 'not': 'kurgu eşi.'},
 {'bag': '14:8 → 70:14', 'kural': "lemma dizisi 'men + fî + ard + cemî'' (3 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '18:29 → 70:16', 'kural': "okuma — kök شوي: 'yeşvi'l-vucûh' / 'li'ş-şevâ'", 'not': 'kök eşi.'},
 {'bag': '53:33 → 70:17', 'kural': "okuma — lemma 'tevellâ'", 'not': 'lemma eşi.'},
 {'bag': '69:12 → 70:18', 'kural': "okuma — ardışık sûre; kök وعي: 'ta'iyehâ … vâ'iya' / 'fe-ev'â'", 'not': 'ardışık sûre bağı.'},
 {'bag': '70:14 → 70:18', 'kural': "sûre içi — kök جمع: 'cemî'an' / 'ceme'a'", 'not': 'sûre içi eş.'},
 {'bag': '21:37 → 70:19', 'kural': "okuma — edilgen 'hulika' + 'insân': malzeme / nitelik", 'not': 'kurgu eşi.'},
 {'bag': '17:83 → 70:20', 'kural': "lemma dizisi 'messe + şerr' (4 ayet) — 'ye'ûsâ' / 'cezû'â'", 'not': 'kalıp eşi.'},
 {'bag': '41:49 → 70:20', 'kural': "lemma dizisi 'messe + şerr' (4 ayet) — 'ye'ûsun qanût'", 'not': 'kalıp eşi.'},
 {'bag': '41:51 → 70:20', 'kural': "lemma dizisi 'messe + şerr' (4 ayet) — 'zû du'â'in 'arîd'", 'not': 'kalıp eşi.'},
 {'bag': '70:19 → 70:20', 'kural': "sûre içi — 'helû'â' / 'cezû'â' (fe'ûl vezni, fâsıla ا)", 'not': 'sûre içi eş.'},
 {'bag': '70:11 → 70:14', 'kural': "sûre içi — fidye listesi 'bi-benîh … ve men fi'l-ardi cemî'an'", 'not': 'sûre içi eş.'},
 {'bag': '70:15 → 70:17', 'kural': "sûre içi — 'lazâ' → 'ted'û' (3FS fail)", 'not': 'sûre içi eş.'},
 # blok 21-30
 {'bag': '70:20 → 70:21', 'kural': "sûre içi — 'izâ messehu'ş-şerru cezû'â' / 'izâ messehu'l-hayru menû'â' (karşıt çift aday 1039)", 'not': 'sûre içi eş.'},
 {'bag': '23:9 → 70:23', 'kural': "lemma dizisi 'ellezî + hum + alâ + salât' (3 ayet) — 'yuhâfizûn' / 'dâ'imûn'", 'not': 'kalıp eşi.'},
 {'bag': '13:35 → 70:23', 'kural': "okuma — lemma 'dâ'im' (2 ayet)", 'not': 'lemma eşi.'},
 {'bag': '51:19 → 70:24', 'kural': "lemma dizisi 'fî + mâl + haqq' (2 ayet) ve 'sâ'il + mahrûm' (2 ayet) — tek ayet / 70:24-25 iki ayet", 'not': 'kalıp eşi.'},
 {'bag': '68:27 → 70:25', 'kural': "okuma — lemma 'mahrûm'", 'not': 'lemma eşi.'},
 {'bag': '70:1 → 70:25', 'kural': "sûre içi — lemma 'sâ'il': azabı soran / isteyen", 'not': 'sûre içi eş.'},
 {'bag': '1:4 → 70:26', 'kural': "lemma dizisi 'yevm + dîn' (13 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '23:57 → 70:27', 'kural': "okuma — 'hum min … rabbihim muşfiqûn': 'haşye' / 'azâb'", 'not': 'kurgu eşi.'},
 {'bag': '52:26 → 70:27', 'kural': "okuma — lemma 'muşfiq'", 'not': 'lemma eşi.'},
 {'bag': '17:57 → 70:28', 'kural': "lemma dizisi 'inne + azâb + rabb' (3 ayet) — 'kâne mahzûrâ' / 'ğayru me'mûn'", 'not': 'kalıp eşi.'},
 {'bag': '52:7 → 70:28', 'kural': "lemma dizisi 'inne + azâb + rabb' (3 ayet) — 'le-vâqi'' / 'ğayru me'mûn'", 'not': 'kalıp eşi.'},
 {'bag': '70:28 → 70:30', 'kural': "sûre içi — 'ğayru me'mûn' / 'ğayru melûmîn'", 'not': 'sûre içi eş.'},
 {'bag': '23:5 → 70:29', 'kural': "esit2 TAM (ölçüm) — metin aynı", 'not': 'tekrar ayet.'},
 {'bag': '23:6 → 70:30', 'kural': "esit2 TAM (ölçüm) / xref — metin aynı; 23:5-6 / 70:29-30 aynı sıra", 'not': 'tekrar ayet.'},
 # blok 31-37
 {'bag': '23:7 → 70:31', 'kural': "esit2 TAM (ölçüm) / xref — metin aynı", 'not': 'tekrar ayet.'},
 {'bag': '23:8 → 70:32', 'kural': "esit2 TAM (ölçüm) / xref — metin aynı", 'not': 'tekrar ayet.'},
 {'bag': '23:9 → 70:34', 'kural': "esit2 YAKIN 0,9565 (ölçüm) — 'salavâtihim' / 'salâtihim'", 'not': 'tekrar ayet.'},
 {'bag': '70:23 → 70:34', 'kural': "nakarat3 sûre içi (ölçüm GEÇER) — 'dâ'imûn' / 'yuhâfizûn'; dizi namazla açılıp kapanıyor", 'not': 'sûre içi eş.'},
 {'bag': '70:29 → 70:34', 'kural': "sûre içi — kök حفظ: 'hâfizûn' / 'yuhâfizûn'", 'not': 'sûre içi eş.'},
 {'bag': '70:28 → 70:32', 'kural': "sûre içi — kök أمن: 'me'mûn' / 'emânâtihim'", 'not': 'sûre içi eş.'},
 {'bag': '23:10 → 70:35', 'kural': "okuma — dizinin 'ulâ'ike' kapanışı: 'humu'l-vârisûn' / 'fî cennâtin mukramûn'", 'not': 'kurgu eşi.'},
 {'bag': '37:42 → 70:35', 'kural': "okuma — lemma 'mukram'", 'not': 'lemma eşi.'},
 {'bag': '70:31 → 70:35', 'kural': "sûre içi — 'ulâ'ike humu'l-'âdûn' / 'ulâ'ike fî cennâtin mukramûn' (karşıt çift aday 1039)", 'not': 'sûre içi eş.'},
 {'bag': '70:22 → 70:35', 'kural': "sûre içi — 'ille'l-musallîn' istisnasının hükmü", 'not': 'sûre içi eş.'},
 {'bag': '14:43 → 70:36', 'kural': "okuma — lemma 'muhti'' (3 ayet)", 'not': 'lemma eşi.'},
 {'bag': '54:8 → 70:36', 'kural': "okuma — lemma 'muhti'' (3 ayet)", 'not': 'lemma eşi.'},
 {'bag': '70:2 → 70:36', 'kural': "sûre içi — kök كفر: 'li'l-kâfirîn' / 'keferû'", 'not': 'sûre içi eş.'},
 {'bag': '50:17 → 70:37', 'kural': "lemma dizisi 'an + yemîn + an + şimâl' (2 ayet) — 'qa'îd' / ''izîn'", 'not': 'kalıp eşi.'},
 {'bag': '69:25 → 70:37', 'kural': "okuma — ardışık sûre; 'yemîn' / 'şimâl' iki ayette (69:19, 69:25) / tek ayette", 'not': 'ardışık sûre bağı.'},
 # blok 38-44
 {'bag': '26:85 → 70:38', 'kural': "lemma dizisi 'cenne + na'îm' (11 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '70:35 → 70:38', 'kural': "sûre içi — kök جنن: 'fî cennâtin mukramûn' / 'cennete na'îm' umudu", 'not': 'sûre içi eş.'},
 {'bag': '70:15 → 70:39', 'kural': "sûre içi — iki 'kellâ': fidye dileğine / cennet umuduna", 'not': 'sûre içi eş.'},
 {'bag': '70:19 → 70:39', 'kural': "sûre içi — kök خلق: edilgen 'hulika' / 1P 'halaqnâhum'", 'not': 'sûre içi eş.'},
 {'bag': '69:38 → 70:40', 'kural': "okuma — ardışık sûre; 'fe-lâ uqsimu'", 'not': 'ardışık sûre bağı.'},
 {'bag': '56:75 → 70:40', 'kural': "okuma — 'fe-lâ uqsimu'", 'not': 'kurgu eşi.'},
 {'bag': '26:28 → 70:40', 'kural': "lemma dizisi 'rabb + meşriq + mağrib' (3 ayet) / xref — tekil / çoğul", 'not': 'kalıp eşi.'},
 {'bag': '37:5 → 70:40', 'kural': "okuma — lemma 'meşriq' çoğul 'meşâriq'", 'not': 'lemma eşi.'},
 {'bag': '55:17 → 70:40', 'kural': "okuma — lemma 'meşriq' / 'mağrib' ikil / çoğul", 'not': 'lemma eşi.'},
 {'bag': '56:60 → 70:41', 'kural': "lemma dizisi 'mâ + nahnu + mesbûq' (2 ayet) — 56:60-61 iki parça / 70:41 ters sıra tek ayet", 'not': 'kalıp eşi.'},
 {'bag': '70:21 → 70:41', 'kural': "sûre içi — kök خير: 'el-hayr' / 'hayran minhum'", 'not': 'sûre içi eş.'},
 {'bag': '43:83 → 70:42', 'kural': "esit2 TAM (ölçüm) — metin aynı", 'not': 'tekrar ayet.'},
 {'bag': '70:5 → 70:42', 'kural': "sûre içi — sûrenin iki 2MS emri: 'fe'sbir' / 'fe-zerhum'", 'not': 'sûre içi eş.'},
 {'bag': '54:7 → 70:43', 'kural': "lemma dizisi 'harace + min + ecdâs' (2 ayet) — 'ke-ennehum cerâd' / 'ke-ennehum ilâ nusub'; 54:7 iki parçası 70:43-44'te ters sıra", 'not': 'kalıp eşi.'},
 {'bag': '50:44 → 70:43', 'kural': "okuma — lemma 'sirâ'' (2 ayet)", 'not': 'lemma eşi.'},
 {'bag': '68:43 → 70:44', 'kural': "lemma dizisi 'hâşi' + basar + rahiqa + zille' (2 ayet) / xref — ilk yarı aynı", 'not': 'kalıp eşi.'},
 {'bag': '21:103 → 70:44', 'kural': "lemma dizisi 'yevm + ellezî + kâne + va'ade' (2 ayet) / xref — 2MP / 3MP", 'not': 'kalıp eşi.'},
 {'bag': '70:42 → 70:44', 'kural': "sûre içi — 'yevmehumu'llezî yû'adûn' / 'zâlike'l-yevmu'llezî kânû yû'adûn'", 'not': 'sûre içi eş.'},
 {'bag': '70:4 → 70:44', 'kural': "sûre içi — kök يوم ilk / son geçiş: 'fî yevmin kâne miqdâruhû' / 'zâlike'l-yevmu'llezî kânû yû'adûn'", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_mearic', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in MEARIC]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_mearic'] = MEARIC
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_mearic', len(MEARIC), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_mearic', len(BAGLAR['AS_mearic']))
