# -*- coding: utf-8 -*-
"""aday_ekle_57_hadid.py — sûre 57 (Hadîd) adayları (AX_hadid) ve okuma bağları (AS_hadid).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

HADID = [
]

BAGLAR = {"AS_hadid": [
 {'bag': '56:96 → 57:1', 'kural': "okuma — ardışık sûre sınırı; 2MS tesbih emri + Rab / PERF tesbih + lafız; fâsıla م → م (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '17:44 · 24:41 → 57:1', 'kural': "lemma سبح 40 ayet — IMPF + 'lehû' / PERF + 'li-' + lafız (59:1, 61:1 'sebbaha lillâh' henüz okunmadı)", 'not': 'tesbih.'},
 {'bag': '9:116 → 57:2', 'kural': "kalıp 'lehû mulku's-semâvâti ve'l-ardi yuhyî' 2 ayet; xref ölçümde", 'not': 'mülk ve dirim.'},
 {'bag': '10:56 → 57:2', 'kural': "kalıp 'yuhyî ve yumît' 9 ayet", 'not': 'diriltir, öldürür.'},
 {'bag': '30:50 → 57:2', 'kural': "kalıp 've huve alâ kulli şey'in qadîr' 7 ayet", 'not': 'kudret.'},
 {'bag': '56:13 · 56:14 → 57:3', 'kural': "okuma — 'evvel', 'âhir' lemmaları insanlar için / Allah için (aday 1041 ve 1040, kayıt)", 'not': 'ilk / son.'},
 {'bag': '30:7 → 57:3', 'kural': "lemma 'zâhir' 8 ayet — dünyanın zâhiri / Allah'ın sıfatı ('bâtın' okunanlarda yok)", 'not': 'zâhir.'},
 {'bag': '31:20 → 57:3', 'kural': "okuma — dişil 'zâhire / bâtına' nimet sıfatı / eril sıfat Allah için (lemma ayrı)", 'not': 'zâhir / bâtın.'},
 {'bag': '10:3 · 25:59 · 32:4 · 13:2 → 57:4', 'kural': "kalıp 'istevâ ale'l-arş' 6 ayet (7:54 henüz okunmadı)", 'not': 'istivâ.'},
 {'bag': '20:5 → 57:4', 'kural': "okuma — 'ale'l-arşi'stevâ' ters sıra", 'not': 'istivâ.'},
 {'bag': '10:3 · 11:7 · 25:59 · 32:4 · 50:38 → 57:4', 'kural': "lemma 'sitte' 7 ayet — 've mâ beynehumâ' üçünde var, 57:4'te yok; 11:7 'arşuhû ale'l-mâ''", 'not': 'altı gün.'},
 {'bag': '34:2 → 57:4', 'kural': "kalıp 'ya'lemu mâ yelicu … ya'rucu fîhâ' 2 ayet; xref ölçümde — devamı rahîm ğafûr / ma'akum", 'not': 'bilgi.'},
 {'bag': '25:2 · 39:44 · 9:116 → 57:5', 'kural': "kalıp 'lehû mulku's-semâvâti ve'l-ard' 10 ayet", 'not': 'mülk.'},
 {'bag': '57:2 · 57:5', 'kural': 'nakarat3 GEÇER — aynı ilk yarı, devamı farklı', 'not': 'sûre içi tekrar.'},
 {'bag': '22:76 · 35:4 → 57:5', 'kural': "kalıp 've ile'llâhi turja'u'l-umûr' 6 ayet (2:210, 3:109, 8:44 henüz okunmadı)", 'not': 'dönüş.'},
 {'bag': '24:42 → 57:5', 'kural': "esit2 BENZER — 'ile'llâhi'l-masîr' / 'ile'llâhi turja'u'l-umûr'", 'not': 'dönüş.'},
 {'bag': '39:44 → 57:5', 'kural': "okuma — aynı ilk yarı; 'summe ileyhi turja'ûn' 2MP / 'turja'u'l-umûr'", 'not': 'dönüş.'},
 {'bag': '22:61 · 31:29 · 35:13 → 57:6', 'kural': "tam kalıp 'yûlicu'l-leyle fi'n-nehâr …' 4 ayet (3:27 2MS henüz okunmadı)", 'not': 'gece / gündüz.'},
 {'bag': '31:23 → 57:6', 'kural': "kalıp 'alîmun bi-zâti's-sudûr' 12 ayet", 'not': 'göğüslerin özü.'},
 {'bag': '57:4 · 57:6', 'kural': 'kök ولج sûre içi — I. bab girer / IV. bab girdirir', 'not': 'giriş.'},
 {'bag': '57:3 · 57:4 · 57:6', 'kural': "kök علم sûre içi — 'alîm' / 'ya'lemu' / 'alîm'", 'not': 'bilgi.'},
 {'bag': '24:62 · 49:15 → 57:7', 'kural': "tam kalıp 'âmenû bi'llâhi ve rasûlihî' 4 ayet — PERF tanım / IMPV emir (4:136 henüz okunmadı)", 'not': 'iman.'},
 {'bag': '35:7 → 57:7', 'kural': "önek toleranslı kalıp 'ecr + kebîr' 4 ayet; esmâ kararı DEĞİL emsali", 'not': 'büyük ecir.'},
 {'bag': '57:7 · 57:8', 'kural': "nakarat3 'âmene + Allah + rasûl' GEÇER (sûre içi diğer ikisi henüz okunmadı)", 'not': 'iman ve elçi.'},
 {'bag': '9:116 · 29:22 · 42:47 · 45:34 → 57:8 · 57:10', 'kural': "kalıp 've mâ lekum' 12 ayet — 'min …' yardımcı yokluğu / NEG + IMPF kınama sorusu", 'not': 'size ne oluyor.'},
 {'bag': '13:20 · 33:7 → 57:8', 'kural': "lemma 'mîsâq' 23 ayet — 1P 'ehaznâ' / 3MS 'ehaze' (fâil KAPATILAMAZ)", 'not': 'kesin söz.'},
 {'bag': '25:1 · 18:1 → 57:9', 'kural': "okuma — 'ellezî + indirme + alâ abdihî': nezzele / enzele / yunezzilu", 'not': 'kuluna indirme.'},
 {'bag': '33:43 → 57:9', 'kural': "kalıp 'li-yuhricakum mine'z-zulumâti ile'n-nûr' 2 ayet; ikisi de 'huve'llezî' ile", 'not': 'karanlıktan ışığa.'},
 {'bag': '14:1 · 14:5 → 57:9', 'kural': "kalıp 'mine'z-zulumâti ile'n-nûr' 7 ayet — çıkaran 2MS / emir alan / 3MS", 'not': 'çıkarma.'},
 {'bag': '16:7 · 16:47 · 22:65 → 57:9', 'kural': "kalıp 'le-ra'ûfun rahîm' 5 ayet — Rab / lafız; xref 24:20", 'not': 'şefkat.'},
 {'bag': '57:4 · 57:9', 'kural': 'kök نزل ve خرج sûre içi — I. bab / II. ve IV. bab (okuma)', 'not': 'bab geçişi.'},
 {'bag': '57:2 · 57:5 · 57:10', 'kural': "okuma — 'lehû mulku's-semâvâti ve'l-ard' / 'lillâhi mîrâsu's-semâvâti ve'l-ard' (lemma 'mîrâs' okunanlarda yok; 3:180 henüz okunmadı)", 'not': 'mülk / miras.'},
 {'bag': '57:4 · 57:10', 'kural': "kök سوي sûre içi 'istevâ' / 'lâ yestevî'; 've'llâhu bimâ ta'melûne basîr / habîr' (nakarat3 GEÇMEZ)", 'not': 'denklik.'},
 {'bag': '9:20 → 57:10', 'kural': "lemma 'a'zam' 3 ayet — 'a'zamu deraceten' iki ayette (73:20 henüz okunmadı)", 'not': 'derece.'},
 {'bag': '32:28 · 48:1 → 57:10', 'kural': "lemma 'feth' 12 ayet — 57:10'da olay adlanmıyor (1017)", 'not': 'fetih.'},
 {'bag': '10:26 → 57:10', 'kural': "lemma 'husnâ' 17 ayet (4:95 've kullen va'ade'llâhu'l-husnâ' henüz okunmadı)", 'not': 'en güzel.'},
 {'bag': '57:7 · 57:10', 'kural': 'kök نفق sûre içi — emir / PERF / soru', 'not': 'harcama.'},
 {'bag': '25:69 · 33:30 → 57:11', 'kural': "lemma 'yudâ'ifu' 9 ayet — azabın katlanması (edilgen) / borcun katlanması (etken); 'aqrada' okunanlarda yok", 'not': 'katlama.'},
 {'bag': '57:7 · 57:11', 'kural': "okuma — 'lehum ecrun kebîr' / 've lehû ecrun kerîm'", 'not': 'ecir.'},
 {'bag': '9:72 · 33:73 → 57:12', 'kural': "kalıp 'el-mu'minîne ve'l-mu'minât' 7 ayet", 'not': 'inanan erkek / kadın.'},
 {'bag': '9:72 · 9:89 → 57:12', 'kural': "kalıp 'cennâtun tecrî min tahtihe'l-enhâr' 27 ayet; 'zâlike (huve) 'l-fevzu'l-azîm' (xref 9:89; 4:13 henüz okunmadı)", 'not': 'cennet.'},
 {'bag': '10:64 → 57:12', 'kural': "lemma 'buşrâ' 15 ayet; 'zâlike huve'l-fevzu'l-azîm' 6 ayet", 'not': 'müjde.'},
 {'bag': '57:9 · 57:12 · 57:13', 'kural': "lemma 'nûr' sûre içi — çıkarılan yer / taşınan ışık / istenen ışık", 'not': 'ışık.'},
 {'bag': '57:12 · 57:13', 'kural': "okuma — ardışık iki ayette eril + dişil çift: mu'minîn / munâfiqûn (aday 1039 kaydı)", 'not': 'iki sınıf.'},
 {'bag': '9:67 · 9:68 · 9:73 · 33:73 · 48:6 → 57:13', 'kural': "lemma 'munâfiq' 25 ayet; merfû çift 'el-munâfiqûne ve'l-munâfiqât' 9:67 / 57:13", 'not': 'münafıklar.'},
 {'bag': '20:10 · 27:7 → 57:13', 'kural': 'kök قبس 3 ayet — ateşten kor / ışıktan pay', 'not': 'kor.'},
 {'bag': '57:3 · 57:13', 'kural': "okuma — 'zâhir / bâtın' Allah için / surun yüzleri için; sıra ters (aday 1041, kayıt)", 'not': 'iç / dış.'},
 {'bag': '9:52 → 57:14', 'kural': "lemma 'terabbes' 11 ayet — 'ma'akum' + bekleme", 'not': 'bekleme.'},
 {'bag': '22:52 → 57:14', 'kural': "lemma 'umniyye' 5 ayet — tekil / çoğul", 'not': 'kuruntu.'},
 {'bag': '40:78 → 57:14', 'kural': "önek toleranslı kalıp 'câ'e emru'llâh' 2 ayet; xref ölçümde", 'not': 'emir geldi.'},
 {'bag': '31:33 · 35:5 → 57:14', 'kural': "kalıp 'bi'llâhi'l-ğarûr' 3 ayet — nehiy (uyarı) / PERF (gerçekleşmiş); xref ölçümde", 'not': 'aldatıcı.'},
 {'bag': '29:25 · 45:34 → 57:15', 'kural': "önek toleranslı kalıp 'me'vâkumu'n-nâr' 3 ayet", 'not': 'barınak.'},
 {'bag': '47:11 → 57:15', 'kural': "okuma — 'mevlâ' Allah için / ateş için (aday 1041, kayıt)", 'not': 'mevlâ.'},
 {'bag': '9:73 · 22:72 → 57:15', 'kural': "kalıp 've bi'se'l-masîr' 9 ayet", 'not': 'kötü varış.'},
 {'bag': '57:12 · 57:15', 'kural': "okuma — 'buşrâkumu'l-yevm' / 'fe'l-yevme lâ yu'hazu minkum fidye' (aday 1039 kaydı)", 'not': 'bugün.'},
 {'bag': '13:28 · 39:22 · 39:23 → 57:16', 'kural': "xref ölçümde — kalp + Allah'ı anma: itmi'nân / katılık / yumuşama / huşû", 'not': 'kalpler.'},
 {'bag': '22:53 · 39:22 → 57:16', 'kural': "kök قسو 6 ayet — katılık 'qulûb' ile", 'not': 'katılaşma.'},
 {'bag': '20:108 → 57:16', 'kural': "lemma 'haşa'a' 2 ayet — sesler / kalpler", 'not': 'huşû.'},
 {'bag': '18:12 → 57:16', 'kural': "lemma 'emed' 4 ayet", 'not': 'süre.'},
 {'bag': '57:4 · 57:16', 'kural': "okuma — 'mâ yenzilu mine's-semâ'' / 'mâ nezele mine'l-haqq' (nakarat3 GEÇMEZ)", 'not': 'inen.'},
 {'bag': '57:16 · 57:17 · 41:39', 'kural': "okuma — kalplerin huşûu ve katılaşması → ölü yerin diriltilmesi; kök خشع 41:39'da yer için (aday 1039 kaydı)", 'not': 'kalp / yer.'},
 {'bag': '30:19 · 30:50 → 57:17', 'kural': "önek toleranslı kalıp 'yuhyi'l-arda ba'de mevtihâ' 2 ayet (30:50 elif-medde imlâsıyla düşüyor)", 'not': 'yerin diriltilmesi.'},
 {'bag': '35:9 · 45:5 · 41:39 → 57:17', 'kural': "okuma — 'fe-ahyâ bihi'l-ard …' sebepli (L2) / sebepsiz (L1)", 'not': 'çıpa kademesi.'},
 {'bag': '57:2 · 57:17', 'kural': 'kök حيي / موت sûre içi — nesne adsız / yer', 'not': 'dirim.'},
 {'bag': '33:35 · 12:88 → 57:18', 'kural': "okuma — 'mutesaddiq' (idgamsız) / 'mussaddiq' (idgamlı; lemma ayrı)", 'not': 'sadaka.'},
 {'bag': '57:11 · 57:18', 'kural': 'nakarat3 GEÇER; xref — etken 3MS / edilgen 3MP', 'not': 'güzel borç.'},
 {'bag': '57:12 · 57:13 · 57:18', 'kural': 'okuma — eril + dişil çift üç ayette', 'not': 'çiftler.'},
 {'bag': '57:7 · 57:19', 'kural': "nakarat3 GEÇER — 'rasûlihî' / 'rusulihî'", 'not': 'elçi / elçiler.'},
 {'bag': '19:41 · 19:56 → 57:19', 'kural': "lemma 'sıddîq' 5 ayet — tekil peygamber sıfatı / çoğul sınıf", 'not': 'sıddîk.'},
 {'bag': '22:51 → 57:19', 'kural': "kalıp 'ulâ'ike ashâbu'l-cahîm' 4 ayet — 'âyâtinâ' 1P ile", 'not': 'cehennemlik.'},
 {'bag': '47:36 · 29:64 → 57:20', 'kural': "önek toleranslı kalıp 'el-hayâtu'd-dunyâ la'ibun ve lehv' 2 ayet; xref 47:36 (6:32 henüz okunmadı); 29:64 sıra ters", 'not': 'oyun ve eğlence.'},
 {'bag': '39:21 → 57:20', 'kural': "kalıp 'yehîcu fe-terâhu musfarrâ' 2 ayet; xref ölçümde — doğrudan anlatım (L4) / teşbih içinde (L4 adayı, TARTIŞMALI)", 'not': 'bitki süreci.'},
 {'bag': '30:51 · 56:65 → 57:20', 'kural': "lemma 'musfarr' 3, 'hutâm' 3 ayet", 'not': 'sararma, kırıntı.'},
 {'bag': '18:45 · 10:24 → 57:20', 'kural': 'okuma — dünya hayatı meseli: su + bitki + yok oluş / yağmur + bitki + çer çöp', 'not': 'mesel.'},
 {'bag': '42:28 → 57:20', 'kural': "lemma 'ğays' 3 ayet", 'not': 'yağmur.'},
 {'bag': '48:29 → 57:20', 'kural': "okuma — ekin meseli 'yu'cibu'z-zurrâ'' / 'a'cebe'l-kuffâr'; ikisi de teşbih içi L4 adayı (karar açık)", 'not': 'beğenme.'},
 {'bag': '40:39 → 57:20', 'kural': "xref ölçümde — 'hâzihi'l-hayâtu'd-dunyâ metâ'' (3:185 'metâ'u'l-ğurûr' henüz okunmadı)", 'not': 'geçimlik.'},
 {'bag': '57:14 · 57:20', 'kural': 'kök غرر sûre içi — aldatan / aldanış', 'not': 'aldanış.'},
 {'bag': '57:3 · 57:20', 'kural': "okuma — 'âhir' Allah için / âhiret için (aday 1041, kayıt)", 'not': 'âhir.'},
 {'bag': '57:19 · 57:21', 'kural': "nakarat3 'âmene + Allah + rasûl' GEÇER — 'rusulih' iki ayette", 'not': 'iman.'},
 {'bag': '57:20 · 57:21', 'kural': "okuma — 'mağfiratun mine'llâh' / 'mağfiratin min rabbikum'; aldatıcı geçimlik / cennet (aday 1039 kaydı)", 'not': 'bağışlanma.'},
 {'bag': '56:10 → 57:21', 'kural': "okuma — 'es-sâbiqûn' / 'sâbiqû' emri (okuma bağı; 1040 alanı değil)", 'not': 'öne geçme.'},
 {'bag': '42:30 → 57:22', 'kural': "okuma — 'mâ esâbekum min musîbe' ellerin kazancı / kitapta önceden (64:11 henüz okunmadı)", 'not': 'musibet.'},
 {'bag': '35:11 · 22:70 · 29:19 → 57:22', 'kural': "kalıp 'inne zâlike ale'llâhi yesîr' 4 ayet; 35:11 ve 22:70'te 'fî kitâb' da aynı ayette", 'not': 'kitap ve kolaylık.'},
 {'bag': '57:22 → 57:23', 'kural': "okuma — 'fî kitâb' → 'li-keylâ te'sev' amacı", 'not': 'amaç.'},
 {'bag': '31:18 → 57:23', 'kural': "kalıp 'kulle muhtâlin fehûr' 2 ayet; xref ölçümde", 'not': 'böbürlenen.'},
 {'bag': '11:10 → 57:23', 'kural': "lemma 'fehûr' 4 ayet — 'ferih' + 'fehûr' / 'tefrahû' + 'fehûr' aynı ayette", 'not': 'sevinç ve övünme.'},
 {'bag': '57:20 · 57:23', 'kural': 'kök فخر sûre içi — tefâhur / fehûr', 'not': 'övünme.'},
 {'bag': '47:38 → 57:24', 'kural': "okuma — cimrilik + 'el-ğaniyy' + 'tevellî' aynı ayette (4:37 kalıbı henüz okunmadı)", 'not': 'cimrilik.'},
 {'bag': '48:17 → 57:24', 'kural': "kalıp 've men yetevelle' 4 ayet", 'not': 'yüz çevirme.'},
 {'bag': '31:26 · 35:15 → 57:24', 'kural': "kalıp 'Allah huve'l-ğaniyyu'l-hamîd' 4 ayet (60:6 henüz okunmadı)", 'not': 'zengin, övülen.'},
 {'bag': '57:18 · 57:24', 'kural': 'okuma — sadaka verenler / cimriler (aday 1039 kaydı)', 'not': 'karşıt.'},
 {'bag': '42:17 · 55:7 → 57:25', 'kural': "lemma 'mîzân' 16 ayet — kitap + mîzân indirme (42:17 3MS / 57:25 1P)", 'not': 'ölçü.'},
 {'bag': '17:50 · 18:96 · 22:21 · 34:10 · 50:22 → 57:25', 'kural': "lemma 'hadîd' 6 ayet — madde / keskin (50:22; 1021); sûre içinde yalnız 57:25", 'not': 'demir.'},
 {'bag': '57:1 · 57:25', 'kural': "kök عزز sûre içi — 'el-azîzu'l-hakîm' / 'qaviyyun azîz' (ikisi de geçerli mühür)", 'not': 'izzet.'},
 {'bag': '57:25 · 57:26', 'kural': "okuma — 'le-qad erselnâ' iki ardışık ayette: 'rusulenâ' / 'Nûhan ve İbrâhîm'", 'not': 'elçiler.'},
 {'bag': '29:27 → 57:26', 'kural': "xref ölçümde — 'ce'alnâ fî zurriyyetih(imâ)'n-nubuvvete ve'l-kitâb' tekil / ikil", 'not': 'soy.'},
 {'bag': '45:16 → 57:26', 'kural': "lemma 'nubuvve' 5 ayet", 'not': 'peygamberlik.'},
 {'bag': '57:16 · 57:26', 'kural': "nakarat3 've kesîrun minhum fâsiqûn' GEÇER (sûre içi üçüncüsü 57:27 henüz okunmadı)", 'not': 'yoldan çıkanlar.'},
 {'bag': '57:26 → 57:27', 'kural': "okuma — 'erselnâ Nûhan ve İbrâhîm' → 'qaffeynâ alâ âsârihim' ('qaffâ' okunanlarda yok; 2:87, 5:46 henüz okunmadı)", 'not': 'art arda.'},
 {'bag': '19:34 · 33:7 → 57:27', 'kural': "lemma 'Îsâ' 25 ayet — 'Îse'bnu Meryem'", 'not': 'Îsâ.'},
 {'bag': '9:111 · 48:29 → 57:27', 'kural': "lemma 'İncîl' 12 ayet", 'not': 'İncîl.'},
 {'bag': '24:2 → 57:27', 'kural': "lemma 'ra'fe' 2 ayet — nehiy altında / kalplere konulan", 'not': 'şefkat.'},
 {'bag': '57:9 · 57:27', 'kural': "okuma — kökler رأف ve رحم Allah için / insanların kalbinde, aynı sıra (aday 1041, kayıt)", 'not': 'şefkat ve merhamet.'},
 {'bag': '57:16 · 57:27', 'kural': "okuma — 'qaset qulûbuhum' / 'ce'alnâ fî qulûbihim ra'feten ve rahme'", 'not': 'kalpler.'},
 {'bag': '57:16 · 57:26 · 57:27', 'kural': "nakarat3 've kesîrun minhum fâsiqûn' sûre içi 3 ayet GEÇER", 'not': 'yoldan çıkanlar.'},
 {'bag': '57:20 · 57:27', 'kural': "kök رضو sûre içi — ridvân (âhirette) / ibtiğâ'e ridvân", 'not': 'hoşnutluk.'},
 {'bag': '33:70 → 57:28', 'kural': "kalıp 'yâ eyyuhe'llezîne âmenu'ttequ'llâh' 7 ayet; sûrede tek nidâ", 'not': 'nidâ.'},
 {'bag': '57:7 · 57:28', 'kural': "okuma — 'âminû bi'llâhi ve rasûlih' / 'âminû bi-rasûlih'", 'not': 'iman emri.'},
 {'bag': '21:85 · 38:48 → 57:28', 'kural': "lemma 'kifl' 4 ayet — özel ad parçası / 'kifleyn' (1021 ailesi)", 'not': 'pay.'},
 {'bag': '57:12 · 57:28', 'kural': "okuma — 'yes'â nûruhum' / 'nûran temşûne bih'; 'nûr' sûre içi 7 token", 'not': 'ışık.'},
 {'bag': '29:46 → 57:29', 'kural': "kalıp 'ehlu'l-kitâb' 31 ayet; sûrede tek", 'not': 'kitap ehli.'},
 {'bag': '57:12 · 57:29', 'kural': "okuma — lemma 'yed' insan elleri / 'bi-yedi'llâh' (aday 1041, kayıt)", 'not': 'el.'},
 {'bag': '57:21 · 57:29', 'kural': "nakarat3 GEÇER — 'yu'tîhi men yeşâ'u va'llâhu zu'l-fadli'l-azîm' iki ayette; sûre bu cümleyle bitiyor", 'not': 'lütuf.'},
 {'bag': '57:1 · 57:29', 'kural': "okuma — sûre açılışı 'el-azîzu'l-hakîm' / kapanışı 'zu'l-fadli'l-azîm'", 'not': 'çerçeve.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_hadid', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in HADID]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_hadid'] = HADID
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_hadid', len(HADID), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_hadid', len(BAGLAR['AS_hadid']))
