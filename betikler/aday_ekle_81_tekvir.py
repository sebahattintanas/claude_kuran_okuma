# -*- coding: utf-8 -*-
"""aday_ekle_81_tekvir.py — sûre 81 (Tekvîr) adayları (AX_tekvir) ve okuma bağları (AS_tekvir).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

TEKVIR = [
]

BAGLAR = {"AS_tekvir": [
 # blok 1-10
 {'bag': '80:42 → 81:1', 'kural': "okuma — ardışık sûre sınırı: işaret zamiri + hasr ile yargı (sûre sonu) / şart zarfı ile kozmik olay dizisi açılışı; fâsıla ة → ت; ikisi de lafızsız, Rabsız (aday 1040, kayıt)", 'not': 'sınır.'},
 {'bag': '80:33 → 81:1', 'kural': "okuma — ardışık sûrede 'izâ' ile âhiret açılışı: 'fe-izâ câ'eti's-sâxxa' / 'ize'ş-şemsu kuvviret' dizisi (aday 1040 ailesi, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '39:5 → 81:1', 'kural': "okuma — kök كور korpusun iki ayeti: gece ile gündüz dürülür, etken 3MS, dünya / güneş dürülür, edilgen, âhiret", 'not': 'kök eşi.'},
 {'bag': '75:9 → 81:1', 'kural': "okuma — şart dizisinde güneşe edilgen fiil: 'cumi'a' / 'kuvviret'", 'not': 'kurgu eşi.'},
 {'bag': '77:8 → 81:2', 'kural': "okuma — 'izâ' + 'en-nucûm' + 3FS fiil: 'tumiset' (edilgen) / 'inkederet' (VII. bab)", 'not': 'kalıp eşi.'},
 {'bag': '77:10 → 81:3', 'kural': "okuma — harekesiz 've ize'l-cibâl' korpusun iki ayeti: 'nusifet' / 'suyyiret'", 'not': 'kalıp eşi.'},
 {'bag': '78:20 → 81:3', 'kural': "okuma — lemma 'suyyiret' + 'el-cibâl': fiil önde / ad önde (iki sûre önce)", 'not': 'lemma eşi.'},
 {'bag': '22:45 → 81:4', 'kural': "okuma — kök عطل korpusun iki ayeti: atıl kuyu / salıverilen gebe develer", 'not': 'kök eşi.'},
 {'bag': '52:6 → 81:6', 'kural': "okuma — deniz + kök سجر: yemin içinde 'el-mescûr' / şart dizisinde 'succiret'; anlam ikiliği iki ayette de KAPATILAMAZ", 'not': 'kök eşi.'},
 {'bag': '81:8 → 81:9', 'kural': "sûre içi — soru fiili 'su'ilet' / sorunun içeriği 'bi-eyyi zenbin qutilet' (dolaylı aktarım)", 'not': 'sûre içi eş.'},
 {'bag': '80:17 → 81:9', 'kural': "okuma — ardışık sûrede edilgen PERF 'qutile' (beddua) / 'qutilet' (soru) (aday 1040 ailesi, kayıt)", 'not': 'lemma eşi.'},
 {'bag': '80:13 → 81:10', 'kural': "okuma — ardışık sûrede lemma 'suhuf': değerli sayfalar / açılan sayfalar (aday 1040 ailesi, kayıt)", 'not': 'lemma eşi.'},
 {'bag': '80:22 → 81:10', 'kural': "okuma — ardışık sûrede kök نشر: 'enşerah' (diriltme) / 'nuşiret' (sayfaların açılması) (aday 1040 ailesi, kayıt; 1021)", 'not': 'kök eşi.'},
 {'bag': '74:52 → 81:10', 'kural': "okuma — 'suhuf' + kök نشر: istenen açık sayfalar / açılan sayfalar", 'not': 'kurgu eşi.'},
 # blok 11-20
 {'bag': '77:9 → 81:11', 'kural': "okuma — harekesiz 've ize's-semâ'' korpusun iki ayeti: 'furicet' / 'kuşitat'", 'not': 'kalıp eşi.'},
 {'bag': '79:36 → 81:12', 'kural': "okuma — edilgen fiil + 'el-cahîm' (iki sûre önce): 'burrizet' / 'su''iret'", 'not': 'kurgu eşi.'},
 {'bag': '26:90 → 81:13', 'kural': "okuma — lemma 'uzlifet' + 'el-cenne': fiil önde, 'li'l-muttaqîn' / ad önde, kime olduğu yok", 'not': 'lemma eşi.'},
 {'bag': '50:31 → 81:13', 'kural': "okuma — lemma 'uzlifet' + 'el-cenne': 'li'l-muttaqîne ğayra ba'îd' / yalın", 'not': 'lemma eşi.'},
 {'bag': '81:12 → 81:13', 'kural': "sûre içi — cehennem alevlendirildi / cennet yaklaştırıldı (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '81:1 → 81:14', 'kural': "sûre içi — 'izâ' şart dizisi (81:1-13, on iki 'izâ' ayeti) / tek cevap ''alimet nefsun mâ ahdarat'", 'not': 'sûre içi eş.'},
 {'bag': '81:7 → 81:18', 'kural': "sûre içi — kök نفس [3/3]: canlar / can / nefes alma (1021)", 'not': 'sûre içi eş.'},
 {'bag': '56:75 → 81:15', 'kural': "okuma — harekesiz 'fe-lâ uqsimu' (5 ayet): yıldızların düştüğü yerler / adsız 'el-xunnes'", 'not': 'kalıp eşi.'},
 {'bag': '69:38 → 81:15', 'kural': "okuma — 'fe-lâ uqsimu' yemini ve aynı cevap (69:40 / 81:19)", 'not': 'kalıp eşi.'},
 {'bag': '55:24 → 81:16', 'kural': "okuma — lemma 'cevâr' (3 ayet): denizdeki yükseltilmiş, gemi olarak nitelenen / gönderge adsız", 'not': 'lemma eşi.'},
 {'bag': '74:33 → 81:17', 'kural': "okuma — gece yemini + zaman edatı + fiil: 'iz edber' / 'izâ 'as'as'", 'not': 'kalıp eşi.'},
 {'bag': '74:34 → 81:18', 'kural': "okuma — sabah yemini + 'izâ' + PERF 3MS: 'esfer' / 'teneffes'; 74:33-34 / 81:17-18 sıralı iki ayet (ardışık olmayan sûre)", 'not': 'kalıp eşi.'},
 {'bag': '81:17 → 81:18', 'kural': "sûre içi — gece / sabah (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '69:40 → 81:19', 'kural': "ölçüm esit2 TAM — 'innehû le-qavlu rasûlin kerîm', ikisi de 'fe-lâ uqsimu' yemininin cevabı", 'not': 'kalıp eşi.'},
 {'bag': '17:42 → 81:20', 'kural': "okuma — harekesiz 'zi'l-'arş' korpusun iki ayeti: ilâhların yol arayacağı / elçinin katında itibarlı olduğu arş sahibi", 'not': 'kalıp eşi.'},
 {'bag': '40:15 → 81:20', 'kural': "okuma — 'zû'l-'arş' aynı tamlama, imlâ / i'râb farkıyla harekesiz kalıba girmiyor", 'not': 'kalıp eşi.'},
 {'bag': '53:5 → 81:20', 'kural': "okuma — kök قوي ile nitelenen: 'şedîdu'l-quvâ' öğreten / 'zî quvva' elçi", 'not': 'kök eşi.'},
 {'bag': '77:21 → 81:20', 'kural': "okuma — lemma 'mekîn': sağlam yerleşim yeri / itibarlı elçi (korpusun son geçişi)", 'not': 'lemma eşi.'},
 # blok 21-29
 {'bag': '26:107 → 81:21', 'kural': "okuma — 'rasûl' + 'emîn': elçinin kendi sözü (1S) / anlatıcının nitelemesi", 'not': 'lemma eşi.'},
 {'bag': '53:2 → 81:22', 'kural': "okuma — 'sâhibukum' + olumsuzlama: sapmadı, azmadı / deli değil", 'not': 'kalıp eşi.'},
 {'bag': '34:46 → 81:22', 'kural': "okuma — 'sâhibukum' + kök جنن olumsuzlamayla: 'min cinne' / 'bi-mecnûn'", 'not': 'kök eşi.'},
 {'bag': '68:2 → 81:22', 'kural': "okuma — 'mâ … bi-mecnûn': 2MS hitap / 'sâhibukum' 3MS; 81:22 'mecnûn'un korpustaki son geçişi", 'not': 'kalıp eşi.'},
 {'bag': '81:13 → 81:22', 'kural': "sûre içi — kök جنن [2/2]: cennet / deli (1021)", 'not': 'sûre içi eş.'},
 {'bag': '53:13 → 81:23', 'kural': "okuma — harekesiz 've le-qad re'âhu' korpusun iki ayeti: 3MS görür, 3MS görülür — 'nezleten uxrâ' / 'bi'l-ufuqi'l-mubîn'", 'not': 'kalıp eşi.'},
 {'bag': '53:7 → 81:23', 'kural': "okuma — lemma 'ufuq': 'el-ufuqu'l-a'lâ' / 'el-ufuqu'l-mubîn' (korpusun son geçişi)", 'not': 'lemma eşi.'},
 {'bag': '69:41 → 81:25', 'kural': "okuma — harekesiz 've mâ huve bi-qavl' korpusun iki ayeti, ikisi de 69:40 / 81:19 eş cevabın ardından: şair sözü / kovulmuş şeytan sözü", 'not': 'kalıp eşi.'},
 {'bag': '81:19 → 81:25', 'kural': "sûre içi — kök قول [2/2]: değerli elçinin sözü / kovulmuş şeytanın sözü (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '38:87 → 81:27', 'kural': "ölçüm esit2 TAM — 'in huve illâ zikrun li'l-'âlemîn'", 'not': 'kalıp eşi.'},
 {'bag': '68:52 → 81:27', 'kural': "ölçüm esit2 BENZER — 've mâ huve illâ' / 'in huve illâ' + 'zikrun li'l-'âlemîn'", 'not': 'kalıp eşi.'},
 {'bag': '80:11 → 81:27', 'kural': "okuma — ardışık sûrede sıralı eşleşme: öğüt ('tezkira' / 'zikr') + 'men şâ'e' (80:11-12 / 81:27-28) (aday 1040, kayıt)", 'not': 'kurgu eşi.'},
 {'bag': '80:12 → 81:28', 'kural': "okuma — ardışık sûrede 'men şâ'e': 'fe-men şâ'e zekerah' / 'li-men şâ'e minkum en yesteqîm' (aday 1040, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '74:37 → 81:28', 'kural': "okuma — harekesiz 'li-men şâ'e minkum' korpusun iki ayeti: öne geçmek ya da geri kalmak / doğru gitmek", 'not': 'kalıp eşi.'},
 {'bag': '76:29 → 81:27', 'kural': "okuma — öğüt + 'men şâ'e' + 'mâ teşâ'ûne illâ' sırası iki sûrede: 76:29-30 / 81:27-29 (ardışık olmayan sûre)", 'not': 'kurgu eşi.'},
 {'bag': '76:30 → 81:29', 'kural': "ölçüm xref + harekesiz 've mâ teşâ'ûne illâ en yeşâ'a' korpusun iki ayeti: devamı ''alîmen hakîmâ' / 'rabbu'l-'âlemîn'", 'not': 'kalıp eşi.'},
 {'bag': '81:28 → 81:29', 'kural': "sûre içi — 'şâ'e' [3/3]: muhatabın dilemesi / Allah'ın dilemesi (aday 1041, kayıt; aday 1039 ayet içi)", 'not': 'sûre içi eş.'},
 {'bag': '81:14 → 81:29', 'kural': "sûre içi — kök علم [3/3]: 'alimet' (bilme) / ''âlemîn' (81:27, 29) (1021)", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_tekvir', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in TEKVIR]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_tekvir'] = TEKVIR
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_tekvir', len(TEKVIR), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_tekvir', len(BAGLAR['AS_tekvir']))
