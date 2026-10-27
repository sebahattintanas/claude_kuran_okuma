# -*- coding: utf-8 -*-
"""aday_ekle_74_muddessir.py — sûre 74 (Müddessir) adayları (AX_muddessir) ve okuma bağları (AS_muddessir).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

MUDDESSIR = [
]

BAGLAR = {"AS_muddessir": [
 # blok 1-10
 {'bag': '73:20 → 74:1', 'kural': "okuma — ardışık sûre sınırı; lafız + 2MP emir + tekitli haberle kapanış / 2MS nidâ ile açılış; fâsıla م → ر (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '73:1 → 74:1', 'kural': "okuma — ardışık sûre açılışı aynı kalıp: nidâ + 'örtünen' anlamlı tek sıfat (muzzemmil / muddessir) (aday 1040, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '73:2 → 74:2', 'kural': "okuma — ardışık sûrenin ikinci ayetinde 'qum' emri: gece ile / uyarı ile; 73:1-2 ↔ 74:1-2 iki ayetlik sıralı eşleşme (aday 1040, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '26:214 → 74:2', 'kural': "okuma — 'enzir' emri: nesneyle (yakın akraba) / nesnesiz", 'not': 'lemma eşi.'},
 {'bag': '17:111 → 74:3', 'kural': "okuma — 'kebbir' emri: zamir + mef'ûl mutlak / Rab öne alınmış meful", 'not': 'lemma eşi.'},
 {'bag': '22:37 → 74:3', 'kural': "okuma — 'kebbere': lafız / Rab", 'not': 'lemma eşi.'},
 {'bag': '71:7 → 74:4', 'kural': "okuma — 'siyâb': çağrıya karşı elbiseye bürünme / elbiseyi temizleme emri", 'not': 'lemma eşi.'},
 {'bag': '22:26 → 74:4', 'kural': "okuma — 2MS emir 'tahhir': ev / elbise", 'not': 'lemma eşi.'},
 {'bag': '73:10 → 74:5', 'kural': "okuma — 'uhcur' emri: kişiler / pislik; ardışık sûre, okuma bağı (sûre sınırı değil)", 'not': 'lemma eşi.'},
 {'bag': '19:46 → 74:5', 'kural': "okuma — 'uhcur' emri: babadan oğula / 2MS'ye", 'not': 'lemma eşi.'},
 {'bag': '74:3 → 74:5', 'kural': "sûre içi — 've' + meful + 'fe' + emir dizilimi: 74:3, 4, 5 ve 74:7 (câr ile)", 'not': 'sûre içi eş.'},
 {'bag': '73:10 → 74:7', 'kural': "okuma — 'isbir' emri; 73:10'daki 'isbir' + 'uhcur' çifti 74:5 / 74:7'ye ayrılmış (ardışık sûre, okuma bağı)", 'not': 'kurgu eşi.'},
 {'bag': '52:48 → 74:7', 'kural': "okuma — 'isbir' + 'li-' + Rab: hüküm aracılı / doğrudan", 'not': 'kalıp eşi.'},
 {'bag': '74:3 → 74:7', 'kural': "sûre içi — ربب 'rabbeke' meful / 'li-rabbike' câr; ikisi de emirden önce", 'not': 'sûre içi eş.'},
 {'bag': '69:13 → 74:8', 'kural': "okuma — 'fe-izâ' + edilgen fiil + 'fî' + alet adı (nufiha / sûr ↔ nuqira / nâqûr); kök ortak değil", 'not': 'kurgu eşi.'},
 {'bag': '25:26 → 74:9', 'kural': "okuma — lemma 'asîr' iki ayet: gün + 'ale'l-kâfirîn' + 'asîr' tek ayette / 74:9-10'a bölünmüş", 'not': 'lemma eşi.'},
 {'bag': '54:8 → 74:9', 'kural': "okuma — kök عسر 'yevmun 'asir' (kâfirlerin sözü) / 'yevmun 'asîr' (anlatıcı hükmü); lemma farklı", 'not': 'kurgu eşi.'},
 {'bag': '74:9 → 74:10', 'kural': "sûre içi — ''asîr' / 'ğayru yesîr' karşıt çift (aday 1039)", 'not': 'sûre içi eş.'},
 # blok 11-20
 {'bag': '68:44 → 74:11', 'kural': "okuma — lemma dizisi 'yezeru + men' korpusun iki ayeti: 'zernî ve men yukezzibu' / 'zernî ve men halaqtu'", 'not': 'kalıp eşi.'},
 {'bag': '73:11 → 74:11', 'kural': "okuma — 'zernî' + 've' + nesne: yalanlayanlar / yarattığım (ardışık sûre, okuma bağı; sûre sınırı değil)", 'not': 'kalıp eşi.'},
 {'bag': '56:30 → 74:12', 'kural': "okuma — lemma 'memdûd' iki ayet: gölge / mal", 'not': 'lemma eşi.'},
 {'bag': '71:12 → 74:12', 'kural': "okuma — مدد + مول + بني tek ayette (vaat) / 74:12-13'e dağılmış (verilen nimet)", 'not': 'kurgu eşi.'},
 {'bag': '68:14 → 74:13', 'kural': "okuma — 'mâl ve benîn' tek ayette / 74:12-13'e bölünmüş", 'not': 'kurgu eşi.'},
 {'bag': '73:15 → 74:13', 'kural': "okuma — lemma 'şâhid': tanık elçi / hazır bulunan oğullar (ardışık sûre, okuma bağı)", 'not': 'lemma eşi.'},
 {'bag': '74:12 → 74:14', 'kural': "sûre içi — 1S nimet sayımı: mal, oğullar, döşenen yol", 'not': 'sûre içi eş.'},
 {'bag': '70:38 → 74:15', 'kural': "okuma — 'yatma'u + en' + fiil: cennete girme umudu / artırma umudu", 'not': 'kalıp eşi.'},
 {'bag': '50:24 → 74:16', 'kural': "okuma — lemma ''anîd'", 'not': 'lemma eşi.'},
 {'bag': '74:1 → 74:16', 'kural': "sûre içi — kök أيي sayımı 'eyyuhâ' / 'âyât' iki ayrı lemmayı birleştiriyor (ARIZA)", 'not': 'sûre içi eş.'},
 {'bag': '18:73 → 74:17', 'kural': "okuma — lemma 'erheqa': ''usr' ile / 'sa'ûd' ile", 'not': 'lemma eşi.'},
 {'bag': '72:13 → 74:17', 'kural': "okuma — kök رهق: ad 'rahaq' / fiil 'urhiqu' (ardışık olmayan sûre)", 'not': 'kök eşi.'},
 {'bag': '73:20 → 74:18', 'kural': "okuma — lemma 'qaddara': Allah gece ve gündüzü / adsız 3MS insan (aday 1041, kayıt; ardışık sûre)", 'not': 'lemma eşi.'},
 {'bag': '36:39 → 74:18', 'kural': "okuma — lemma 'qaddara': 1P ay menzillerini / 3MS insan (aday 1041 ailesi)", 'not': 'lemma eşi.'},
 {'bag': '51:10 → 74:19', 'kural': "okuma — edilgen beddua 'qutile': ardından özne / ardından 'keyfe' sorusu", 'not': 'kalıp eşi.'},
 {'bag': '74:19 → 74:20', 'kural': "sûre içi — 'qutile keyfe qaddar' tekrarı: 'fe' / 'summe' (ölçüm nakarat3)", 'not': 'sûre içi eş.'},
 {'bag': '74:18 → 74:20', 'kural': "sûre içi — قدر 'qaddara' üç ayette art arda", 'not': 'sûre içi eş.'},
 # blok 21-30
 {'bag': '74:20 → 74:23', 'kural': "sûre içi — dört ardışık ayet 'summe' ile başlıyor (74:20-23)", 'not': 'sûre içi eş.'},
 {'bag': '70:17 → 74:23', 'kural': "okuma — lemma 'edbere': 'edbere ve tevellâ' / 'edbere ve'stekbera'", 'not': 'lemma eşi.'},
 {'bag': '71:7 → 74:23', 'kural': "okuma — lemma 'istekbera'", 'not': 'lemma eşi.'},
 {'bag': '74:3 → 74:23', 'kural': "sûre içi — كبر 'fe-kebbir' (Rabbi büyüt) / 'istekbera' (büyüklendi)", 'not': 'sûre içi eş.'},
 {'bag': '37:15 → 74:24', 'kural': "okuma — 'in hâzâ illâ sihr': 'mubîn' / 'yu'ser'", 'not': 'kalıp eşi.'},
 {'bag': '34:43 → 74:24', 'kural': "okuma — 'in hâzâ illâ sihr': 'mubîn' / 'yu'ser'", 'not': 'kalıp eşi.'},
 {'bag': '54:2 → 74:24', 'kural': "okuma — kök سحر: 'sihr' + sıfat / 'sihr' + edilgen fiil", 'not': 'kök eşi.'},
 {'bag': '74:24 → 74:25', 'kural': "sûre içi — 'in hâzâ illâ' tekrarı, aynı alıntı içinde (ölçüm nakarat3)", 'not': 'sûre içi eş.'},
 {'bag': '23:24 → 74:25', 'kural': "okuma — 'mâ … illâ beşer' elçi için / 'qavlu'l-beşer' söz için", 'not': 'kurgu eşi.'},
 {'bag': '36:15 → 74:25', 'kural': "okuma — 'mâ … illâ beşer' elçiler için / söz için", 'not': 'kurgu eşi.'},
 {'bag': '74:17 → 74:26', 'kural': "sûre içi — 'se' + IV. bab 1S + 3MS + ikinci meful: 'sa'ûd' / 'seqar'", 'not': 'sûre içi eş.'},
 {'bag': '69:31 → 74:26', 'kural': "okuma — kök صلي: 2MP emir 'sallûh' / 1S gelecek 'uslîhi'", 'not': 'kök eşi.'},
 {'bag': '54:48 → 74:26', 'kural': "okuma — lemma 'seqar': öbür sûrelerdeki tek geçiş", 'not': 'lemma eşi.'},
 {'bag': '69:3 → 74:27', 'kural': "okuma — 'mâ edrâke mâ': 'el-hâqqa' / 'seqar'", 'not': 'kalıp eşi.'},
 {'bag': '71:26 → 74:28', 'kural': "okuma — 'lâ tezer': nehiy (Rabbe dua) / nefy (Sekar)", 'not': 'lemma eşi.'},
 {'bag': '74:11 → 74:28', 'kural': "sûre içi — وذر 'zernî' / 'lâ tezer'", 'not': 'sûre içi eş.'},
 {'bag': '74:25 → 74:29', 'kural': "sûre içi — lemma 'beşer': 'qavlu'l-beşer' / 'li'l-beşer'", 'not': 'sûre içi eş.'},
 {'bag': '27:48 → 74:30', 'kural': "okuma — lemma 'tis'a' korpusun iki ayeti", 'not': 'lemma eşi.'},
 {'bag': '9:36 → 74:30', 'kural': "okuma — ''aşer' bileşik sayının ikinci ögesi: on iki / on dokuz", 'not': 'lemma eşi.'},
 {'bag': '12:4 → 74:30', 'kural': "okuma — ''aşer' bileşik sayının ikinci ögesi: on bir / on dokuz", 'not': 'lemma eşi.'},
 # blok 31-31
 {'bag': '74:30 → 74:31', 'kural': "sûre içi — ''iddetehum' 74:30'daki sayıya döner; sayının gerekçesi", 'not': 'sûre içi eş.'},
 {'bag': '9:37 → 74:31', 'kural': "okuma — lemma ''idde'", 'not': 'lemma eşi.'},
 {'bag': '17:60 → 74:31', 'kural': "okuma — 'mâ ce'alnâ … illâ fitneten li-' iskeleti", 'not': 'kalıp eşi.'},
 {'bag': '37:63 → 74:31', 'kural': "okuma — 1P 'ce'alnâ' + 'fitne' + 'li-'", 'not': 'kalıp eşi.'},
 {'bag': '22:53 → 74:31', 'kural': "okuma — 'fitne' ile 'ellezîne fî qulûbihim marad' aynı ayette", 'not': 'kurgu eşi.'},
 {'bag': '27:14 → 74:31', 'kural': "okuma — lemma 'isteyqane' korpusun iki ayeti: inkârla / kitap verilenlerin bilgisi", 'not': 'lemma eşi.'},
 {'bag': '48:4 → 74:31', 'kural': "okuma — 'izdâde + îmân' ve 'cunûd' aynı ayette", 'not': 'kurgu eşi.'},
 {'bag': '48:7 → 74:31', 'kural': "okuma — 'cunûd': lafza izâfet / Rabbe izâfet", 'not': 'lemma eşi.'},
 {'bag': '33:12 → 74:31', 'kural': "okuma — 'ellezîne fî qulûbihim marad' + söz", 'not': 'kalıp eşi.'},
 {'bag': '14:4 → 74:31', 'kural': "xref (ölçüm) 'yudillu'llâhu men yeşâ'u ve yehdî men yeşâ'' — ardından ''azîz hakîm' / 'cunûde rabbik'", 'not': 'kalıp eşi.'},
 {'bag': '74:3 → 74:31', 'kural': "sûre içi — ربب üç geçişin üçü 2MS izâfetli (74:3, 74:7, 74:31)", 'not': 'sûre içi eş.'},
 {'bag': '74:12 → 74:31', 'kural': "sûre içi — جعل 'ce'altu' 1S / 'ce'alnâ' 1P ×2", 'not': 'sûre içi eş.'},
 {'bag': '74:29 → 74:31', 'kural': "sûre içi — lemma 'beşer': 'li'l-beşer' (Sekar) / 'zikrâ li'l-beşer'", 'not': 'sûre içi eş.'},
 # blok 32-40
 {'bag': '36:39 → 74:32', 'kural': "okuma — lemma 'qamer': ölçülen (menziller) / kasem nesnesi", 'not': 'lemma eşi.'},
 {'bag': '74:16 → 74:32', 'kural': "sûre içi — 'kellâ' (şimdiye dek ikinci)", 'not': 'sûre içi eş.'},
 {'bag': '74:23 → 74:33', 'kural': "sûre içi — lemma 'edbere': adsız insan / gece", 'not': 'sûre içi eş.'},
 {'bag': '74:33 → 74:34', 'kural': "sûre içi — gece 'iz edbera' / sabah 'izâ esfera' karşıt çift (aday 1039)", 'not': 'sûre içi eş.'},
 {'bag': '11:81 → 74:34', 'kural': "okuma — lemma 'subh': vade / kasem nesnesi", 'not': 'lemma eşi.'},
 {'bag': '53:18 → 74:35', 'kural': "okuma — 'kubrâ': âyetlerin sıfatı / 'ihde'l-kuber'", 'not': 'lemma eşi.'},
 {'bag': '74:23 → 74:35', 'kural': "sûre içi — كبر üç geçiş: 'kebbir' / 'istekbera' / 'kuber' (74:3, 74:23, 74:35)", 'not': 'sûre içi eş.'},
 {'bag': '74:2 → 74:36', 'kural': "sûre içi — نذر 'enzir' emri / 'nezîr'", 'not': 'sûre içi eş.'},
 {'bag': '74:31 → 74:36', 'kural': "sûre içi — lemma 'beşer' dört geçiş (74:25, 29, 31, 36), dördü de fâsıla kelimesi", 'not': 'sûre içi eş.'},
 {'bag': '48:2 → 74:37', 'kural': "okuma — 'teqaddeme / te'ahhara' çifti: günah / insanın seçimi", 'not': 'kalıp eşi.'},
 {'bag': '74:31 → 74:37', 'kural': "sûre içi — 'şâ'e': Allah'ın dilemesi / insanın dilemesi (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '52:21 → 74:38', 'kural': "okuma — 'kull + … + kesebe + rehîn(e)': eril / dişil, farklı lemmalar", 'not': 'kurgu eşi.'},
 {'bag': '40:17 → 74:38', 'kural': "okuma — 'kullu nefsin bimâ kesebet' + ceza fiili / + 'rehîne'", 'not': 'kalıp eşi.'},
 {'bag': '14:51 → 74:38', 'kural': "okuma — 'kulle nefsin mâ kesebet' + ceza fiili / + 'rehîne'", 'not': 'kalıp eşi.'},
 {'bag': '56:27 → 74:39', 'kural': "okuma — 'ashâbu'l-yemîn'; korpustaki beş geçişin dördü sûre 56'da", 'not': 'kalıp eşi.'},
 {'bag': '56:38 → 74:39', 'kural': "okuma — 'ashâbu'l-yemîn'", 'not': 'kalıp eşi.'},
 {'bag': '74:31 → 74:39', 'kural': "sûre içi — صحب 'ashâbe'n-nâr' / 'ashâbe'l-yemîn'", 'not': 'sûre içi eş.'},
 {'bag': '52:25 → 74:40', 'kural': "okuma — cennet ehli 'yetesâ'elûn'", 'not': 'lemma eşi.'},
 {'bag': '37:50 → 74:40', 'kural': "okuma — cennet ehli 'yetesâ'elûn'", 'not': 'lemma eşi.'},
 # blok 41-48
 {'bag': '15:12 → 74:42', 'kural': "okuma — 'seleke + fî' + 'mucrimîn' tek ayette / 74:41-42'ye bölünmüş", 'not': 'kurgu eşi.'},
 {'bag': '26:200 → 74:42', 'kural': "okuma — 'seleke + fî' + 'mucrimîn' tek ayette / 74:41-42'ye bölünmüş", 'not': 'kurgu eşi.'},
 {'bag': '69:32 → 74:42', 'kural': "okuma — lemma 'seleke': cehennemde zincire sokma emri / Sekar'a sokma sorusu", 'not': 'lemma eşi.'},
 {'bag': '74:27 → 74:42', 'kural': "sûre içi — lemma 'seqar' üçüncü geçiş (74:26, 74:27, 74:42)", 'not': 'sûre içi eş.'},
 {'bag': '70:22 → 74:43', 'kural': "okuma — 'musallîn': istisna edilenler / suçluların olmadıkları", 'not': 'lemma eşi.'},
 {'bag': '74:43 → 74:46', 'kural': "sûre içi — dört 1P cümle: 'lem neku' ×2, 've kunnâ' ×2", 'not': 'sûre içi eş.'},
 {'bag': '69:34 → 74:44', 'kural': "okuma — kök طعم + 'miskîn': ta'âm teşviki yok / doyurmak yok", 'not': 'kurgu eşi.'},
 {'bag': '70:42 → 74:45', 'kural': "okuma — 'hâda': 2MS'ye emirle anlatılan / suçluların kendi ağzından", 'not': 'lemma eşi.'},
 {'bag': '43:83 → 74:45', 'kural': "okuma — 'hâda': 2MS'ye emirle anlatılan / suçluların kendi ağzından", 'not': 'lemma eşi.'},
 {'bag': '74:9 → 74:46', 'kural': "sûre içi — يوم üç geçiş: 'yevme'izin yevmun 'asîr' / 'yevmi'd-dîn'", 'not': 'sûre içi eş.'},
 {'bag': '15:99 → 74:47', 'kural': "okuma — 'hattâ + etâ + yaqîn' korpusun iki ayeti: 2MS emir + gelecek / 1P geçmiş", 'not': 'kalıp eşi.'},
 {'bag': '74:31 → 74:47', 'kural': "sûre içi — يقن 'li-yesteyqine' / 'el-yaqîn'", 'not': 'sûre içi eş.'},
 {'bag': '20:109 → 74:48', 'kural': "okuma — 'nefe'a + şefâ'a': istisnalı / istisnasız", 'not': 'kalıp eşi.'},
 {'bag': '26:100 → 74:48', 'kural': "okuma — lemma 'şâfi'' korpusun iki ayeti: 1P ağzından / 3MP anlatım", 'not': 'lemma eşi.'},
 # blok 49-56
 {'bag': '73:19 → 74:49', 'kural': "okuma — 'tezkira' + 'fe-men şâ'e': 73:19 tek ayette / 74:54-55 (ardışık sûre, okuma bağı)", 'not': 'kurgu eşi.'},
 {'bag': '69:48 → 74:54', 'kural': "okuma — 'inne + tezkira': 'le-tezkiratun li'l-muttaqîn' / yalın", 'not': 'kalıp eşi.'},
 {'bag': '62:5 → 74:50', 'kural': "okuma — 'himâr' teşbihi: kitaba karşı tutum / öğütten yüz çevirme", 'not': 'kurgu eşi.'},
 {'bag': '16:8 → 74:50', 'kural': "okuma — lemma 'himâr': binek / teşbih aracı", 'not': 'lemma eşi.'},
 {'bag': '51:50 → 74:51', 'kural': "okuma — lemma 'ferra': Allah'a kaçış emri / eşeklerin kaçışı", 'not': 'lemma eşi.'},
 {'bag': '70:38 → 74:52', 'kural': "okuma — 'kullu'mri'in minhum en' + edilgen fiil: cennete sokulma umudu / sayfalar verilme isteği", 'not': 'kalıp eşi.'},
 {'bag': '53:36 → 74:52', 'kural': "okuma — lemma 'suhuf'", 'not': 'lemma eşi.'},
 {'bag': '74:31 → 74:52', 'kural': "sûre içi — 'erâde': Allah / insan (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '74:16 → 74:53', 'kural': "sûre içi — 'kellâ' dört geçiş (74:16, 32, 53, 54)", 'not': 'sûre içi eş.'},
 {'bag': '74:49 → 74:54', 'kural': "sûre içi — lemma 'tezkira' iki geçiş", 'not': 'sûre içi eş.'},
 {'bag': '74:37 → 74:55', 'kural': "sûre içi — insanın dilemesi 'li-men şâ'e minkum' / 'fe-men şâ'e'", 'not': 'sûre içi eş.'},
 {'bag': '74:55 → 74:56', 'kural': "sûre içi — 'men şâ'e zekerah' (insan) / 'mâ yezkurûne illâ en yeşâ'a'llâh' (Allah) (aday 1041 ailesi)", 'not': 'sûre içi eş.'},
 {'bag': '11:81 → 74:56', 'kural': "okuma — lemma 'ehl': insan (aile) / Allah ('ehlu't-teqvâ'; aday 1041, kayıt)", 'not': 'lemma eşi.'},
 {'bag': '73:20 → 74:56', 'kural': "okuma — ardışık iki sûrenin son ayeti lafız + غفر ile kapanıyor ('ğafûrun rahîm' / 'ehlu'l-mağfira'); 1040 sûre sınırı değil (74:56 → 75:1 henüz okunmadı)", 'not': 'kurgu eşi.'},
 {'bag': '74:31 → 74:56', 'kural': "sûre içi — lafız üç geçiş (74:31 ×2, 74:56); 'şâ'e' Allah için", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_muddessir', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in MUDDESSIR]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_muddessir'] = MUDDESSIR
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_muddessir', len(MUDDESSIR), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_muddessir', len(BAGLAR['AS_muddessir']))
