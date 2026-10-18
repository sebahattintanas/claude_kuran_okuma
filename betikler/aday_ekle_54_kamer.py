# -*- coding: utf-8 -*-
"""aday_ekle_54_kamer.py — sûre 54 (Kamer) adayları (AX_kamer) ve okuma bağları (AS_kamer).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

KAMER = [
]

BAGLAR = {"AS_kamer": [
 {'bag': '53:62 → 54:1', 'kural': 'okuma — ardışık sûre sınırı; fâsıla ا → ر; aday 1040 alanında kayıt, test yok', 'not': 'sûre sınırı.'},
 {'bag': '53:57 → 54:1', 'kural': "okuma — 'ezifeti'l-âzife' / 'iqterabeti's-sâ'a': iki kökle 'yaklaştı', sûre sınırının iki yanında (aday 1040, kayıt)", 'not': 'yaklaşma.'},
 {'bag': '21:1 → 54:1 · 54:2', 'kural': "okuma — 'iqterabe … mu'ridûn' bir ayette / 'iqterabet' + 'yu'ridû' iki ayette", 'not': 'yaklaştı, yüz çevirme.'},
 {'bag': '52:44 → 54:2', 'kural': "tam kalıp 've in yerev' 4 ayet; okundu — şart + nesne + 'yeqûlû' + adlandırma", 'not': 'görseler derler.'},
 {'bag': '47:14 → 54:3', 'kural': "tam kalıp 've'ttebe'û ehvâ'ehum' 3 ayet; okundu", 'not': 'hevesler.'},
 {'bag': '53:23 → 54:3 · 54:4', 'kural': "okuma — تبع + هوي ve 've leqad câ'ehum' sûre sınırının iki yanında (aday 1040, kayıt)", 'not': 'uyma, gelen.'},
 {'bag': '10:101 → 54:5', 'kural': "okuma — 'mâ tuğni'l-âyâtu ve'n-nuzur' / 'fe-mâ tuğni'n-nuzur'", 'not': 'uyarılar.'},
 {'bag': '53:56 → 54:5', 'kural': "okuma — 'nezîrun mine'n-nuzur' / 'fe-mâ tuğni'n-nuzur' (aday 1040, kayıt)", 'not': 'uyarıcı.'},
 {'bag': '51:54 · 53:29 → 54:6', 'kural': "tam kalıp 'fe-tevelle anhum' 3 ayet; okundu — 53:29 'fe-a'rid' ile yüz çevirme emri", 'not': 'yüz çevir.'},
 {'bag': '50:41 → 54:6', 'kural': "okuma — 'yevme yunâdi'l-munâdi' / 'yevme yed'u'd-dâ'': zarf + aynı kökten fiil ve fâil", 'not': 'çağıran.'},
 {'bag': '36:51 → 54:7', 'kural': "lemma 'ecdâs' 3 ayet; okundu — kabirlerden çıkış", 'not': 'kabirler.'},
 {'bag': '14:43 → 54:8', 'kural': "lemma 'muhti'' 3 ayet; okundu", 'not': 'boyun uzatan.'},
 {'bag': '50:12 → 54:9', 'kural': "tam kalıp 'kezzebet qablehum qavmu nûh' 5 ayet; okundu", 'not': 'Nûh kavmi.'},
 {'bag': '53:52 → 54:9', 'kural': 'okuma — Nûh kavmi sûre sınırının iki yanında (aday 1040, kayıt)', 'not': 'Nûh kavmi.'},
 {'bag': '52:29 → 54:9', 'kural': "okuma — 'mecnûn' 2MS için olumsuzlanıyor / 'abdenâ' için söyleniyor", 'not': 'deli.'},
 {'bag': '54:4 → 54:9', 'kural': "okuma — زجر sûre içi: 'muzdecer' / 'uzdücir'", 'not': 'caydırma.'},
 {'bag': '44:22 → 54:10', 'kural': "tam kalıp 'fe-de'â rabbeh' 2 ayet; okundu — 'enne' 3MP / 'ennî' 1S", 'not': 'Rabbine seslendi.'},
 {'bag': '15:14 → 54:11', 'kural': "okuma — 'fetahnâ' + gökten kapı: varsayım / olmuş (xref ölçümde)", 'not': 'gök kapısı.'},
 {'bag': '36:34 → 54:12', 'kural': "okuma — 'feccernâ … uyûn': bahçelerde pınar / yer pınar", 'not': 'pınar.'},
 {'bag': '11:44 → 54:11 · 54:12', 'kural': "okuma — yer ve gök suyu + 'emr': çekilme / buluşma", 'not': 'tufan suları.'},
 {'bag': '11:37 · 23:27 · 52:48 → 54:14', 'kural': "tam kelime 'bi-a'yuninâ' 4 ayet; okundu — yapım emri / muhatap / akış", 'not': 'gözlerimiz.'},
 {'bag': '54:12 → 54:14', 'kural': "okuma — عين sûre içi: 'uyûn' pınar / 'a'yuninâ' göz", 'not': 'aynı kök.'},
 {'bag': '29:15 · 29:35 → 54:15', 'kural': "okuma — 'âyeten' + 'hâ' (ce'alnâhâ / tereknâ minhâ / teraknâhâ)", 'not': 'işaret.'},
 {'bag': '54:15 · 54:17', 'kural': "tam kalıp 'fe-hel min muddekir' 6 ayet; 'muddekir' lemma — korpusta yalnız sûre 54", 'not': 'nakarat.'},
 {'bag': '54:16 · 54:18', 'kural': "tam kalıp 'fe-keyfe kâne azâbî ve nuzur' 4 ayet — korpusta yalnız sûre 54; 1P → 1S", 'not': 'nakarat.'},
 {'bag': '26:123 → 54:18', 'kural': "tam kalıp 'kezzebet âd' 2 ayet; okundu", 'not': 'Âd.'},
 {'bag': '53:50 → 54:18', 'kural': 'okuma — helâk sırası sûre sınırında: Âd, Semûd, Nûh kavmi / Nûh kavmi, Âd (aday 1040, kayıt)', 'not': 'helâk listesi.'},
 {'bag': '41:16 → 54:19', 'kural': "tam kalıp 'rîhan sarsaran' 2 ayet; okundu — 'eyyâm nahisât' / 'yevm nahs'", 'not': 'rüzgâr.'},
 {'bag': '51:41 → 54:19', 'kural': "okuma — Âd + 'erselnâ aleyhim' + rüzgâr: 'el-akîm' / 'sarsar'", 'not': 'Âd rüzgârı.'},
 {'bag': '54:2 → 54:19', 'kural': "okuma — 'mustemirr' lemma 2 ayet, ikisi bu sûrede: sihr / nahs", 'not': 'süregelen.'},
 {'bag': '50:10 → 54:20', 'kural': "okuma — 'nahl': yükselen hurmalar / sökülmüş hurma kütükleri", 'not': 'hurma.'},
 {'bag': '54:16 · 54:18 · 54:21 · 54:30', 'kural': "tam kalıp 'fe-keyfe kâne azâbî ve nuzur' 4 ayet — korpusta yalnız sûre 54; dördü de okundu", 'not': 'nakarat tamam.'},
 {'bag': '54:17 → 54:22', 'kural': "tam kalıp 've leqad yessernâ'l-qur'âne li'z-zikri fe-hel min muddekir' — Nûh / Âd kıssası sonrası", 'not': 'nakarat.'},
 {'bag': '26:141 → 54:23', 'kural': "tam kalıp 'kezzebet semûd' 4 ayet; okundu — 'el-murselîn' / 'bi'n-nuzur'", 'not': 'Semûd.'},
 {'bag': '53:51 → 54:23', 'kural': 'okuma — Semûd sûre sınırının iki yanında (aday 1040, kayıt)', 'not': 'Semûd.'},
 {'bag': '26:154 → 54:24', 'kural': "okuma — 'beşerun mislunâ' / 'beşeren minnâ'", 'not': 'beşer.'},
 {'bag': '38:8 → 54:25', 'kural': "okuma — 'e-unzile aleyhi'z-zikru min beyninâ' / 'e-ulqiye'z-zikru aleyhi min beyninâ'", 'not': 'zikir aramızdan.'},
 {'bag': '54:25 → 54:26', 'kural': "okuma — 'kezzâbun eşir' / 'meni'l-kezzâbu'l-eşir'; 'eşir' lemma yalnız bu iki ayette", 'not': 'yalancı, şımarık.'},
 {'bag': '17:59 · 11:64 · 26:155 → 54:27', 'kural': "lemma 'nâqa' 7 ayet; okundu — 'mubsıra' / 'âyeten' / 'fitneten'", 'not': 'dişi deve.'},
 {'bag': '44:59 → 54:27', 'kural': "lemma 'irtaqib' 4 ayet; okundu — emir 2MS", 'not': 'gözetle.'},
 {'bag': '53:22 → 54:28', 'kural': "lemma 'qisme' 3 ayet; okundu — ardışık iki sûrede: erkek-dişi / su paylaştırması (aday 1040, kayıt)", 'not': 'paylaştırma.'},
 {'bag': '26:155 → 54:28', 'kural': "lemma 'şirb' 2 ayet; okundu — 'lehâ şirb ve lekum şirb' / 'kullu şirbin muhtadar'", 'not': 'içme payı.'},
 {'bag': '26:157 → 54:29', 'kural': "okuma — 'fe-aqarûhâ' çoğul / 'fe-aqar' tekil + 'sâhibehum'", 'not': 'kesme.'},
 {'bag': '36:29 → 54:31', 'kural': "tam kalıp 'sayhaten vâhideten' 5 ayet; okundu", 'not': 'tek çığlık.'},
 {'bag': '29:40 → 54:31 · 54:34', 'kural': "okuma — 'hâsib' ve 'sayha' bir ayette / Semûd'a 'sayha', Lût kavmine 'hâsib' iki ayette", 'not': 'helâk türleri.'},
 {'bag': '18:45 → 54:31', 'kural': "lemma 'heşîm' 2 ayet; okundu — dünya hayatı benzetmesi / helâk edilenler", 'not': 'kuru ot.'},
 {'bag': '54:19 · 54:31 · 54:34', 'kural': "tam kalıp 'innâ erselnâ aleyhim' 3 ayet — korpusta yalnız sûre 54", 'not': 'nakarat.'},
 {'bag': '54:17 · 54:22 · 54:32 · 54:40', 'kural': "tam kalıp 've leqad yessernâ'l-qur'âne li'z-zikri fe-hel min muddekir' 4 ayet — korpusta yalnız sûre 54; dördü de okundu", 'not': 'nakarat tamam.'},
 {'bag': '26:160 → 54:33', 'kural': "tam kalıp 'kezzebet qavmu lût' 2 ayet; okundu", 'not': 'Lût kavmi.'},
 {'bag': '51:18 → 54:34', 'kural': "lemma 'sehar' 3 ayet; okundu — 'bi'l-eshâr' / 'bi-sehar'", 'not': 'seher.'},
 {'bag': '54:2 → 54:34', 'kural': "okuma — سحر sûre içi: 'sihr' / 'sehar' (gloss 1021)", 'not': 'aynı kök.'},
 {'bag': '27:40 → 54:35 · 54:38', 'kural': "okuma — 'men şekera' ve 'mustaqirr' 27:40'ta bir ayette", 'not': 'şükür, yerleşik.'},
 {'bag': '54:14 → 54:35', 'kural': "okuma — جزي: 'li-men kâne kufir' / 'men şeker'; ayetler arası karşıt çift (aday 1039)", 'not': 'karşılık.'},
 {'bag': '44:16 → 54:36', 'kural': "lemma 'batşe' 2 ayet; okundu", 'not': 'yakalayış.'},
 {'bag': '53:55 → 54:36', 'kural': "lemma 'temârâ' 4 ayet, dördü okundu — sûre sınırının iki yanında (aday 1040, kayıt)", 'not': 'kuşku.'},
 {'bag': '36:66 → 54:37', 'kural': "okuma — 'le-tamesnâ alâ a'yunihim' varsayım / 'fe-tamesnâ a'yunehum' olmuş", 'not': 'gözleri silmek.'},
 {'bag': '15:68 → 54:37', 'kural': "okuma — 'dayf' konuklar", 'not': 'konuklar.'},
 {'bag': '54:12 · 54:14 · 54:37', 'kural': 'okuma — عين sûre içi üç geçiş: pınar / gözetim / silinen gözler', 'not': 'aynı kök.'},
 {'bag': '14:6 · 40:46 → 54:41', 'kural': "tam kalıp 'âle fir'avn' 12 ayet (2'si basıldı)", 'not': 'Firavun ailesi.'},
 {'bag': '54:34 · 54:41', 'kural': "okuma — 'âl' sûre içi: Lût ailesi / Firavun ailesi", 'not': 'aile.'},
 {'bag': '20:56 → 54:42', 'kural': "okuma — 'âyâtinâ kullehâ' + 'kezzebe' (kalıp sayımı imlâ farkıyla ayırıyor)", 'not': 'bütün âyetler.'},
 {'bag': '11:102 → 54:42', 'kural': "lemma 'ahz' 5 ayet — fiil + masdar ikilemesi", 'not': 'yakalayış.'},
 {'bag': '18:45 · 43:42 → 54:42', 'kural': "lemma 'muqtedir' 4 ayet (54:55 henüz okunmadı)", 'not': 'güç yetiren.'},
 {'bag': '18:45 → 54:31 · 54:42', 'kural': "okuma — 'heşîm' ve 'muqtedir' 18:45'te bir ayette, burada iki ayette", 'not': 'bir ayetten iki ayete.'},
 {'bag': '9:1 → 54:43', 'kural': "lemma 'berâ'e' 2 ayet", 'not': 'aklanma / ilişki kesme.'},
 {'bag': '37:156 → 54:43', 'kural': "tam kalıp 'em lekum' 4 ayet (68:37, 68:39 henüz okunmadı)", 'not': 'soru kalıbı.'},
 {'bag': '26:196 → 54:43', 'kural': "lemma 'zubur' 7 ayet", 'not': 'kitaplar.'},
 {'bag': '51:45 · 28:81 → 54:44', 'kural': "lemma 'muntasir' 4 ayet — üçü olumsuz, burada olumlu iddia", 'not': 'üstün gelme.'},
 {'bag': '26:56 → 54:44', 'kural': "okuma — 'cemî'' kendi topluluğunu niteleyen alıntı", 'not': 'hep birlikte.'},
 {'bag': '54:10 · 54:44', 'kural': "okuma — نصر sûre içi: 'fe'ntasir' / 'muntasir'", 'not': 'yardım.'},
 {'bag': '54:44 → 54:45', 'kural': "okuma — 'cemî'un muntasir' / 'yuhzemu'l-cem'' (aday 1039, kayıt)", 'not': 'iddia / bozgun.'},
 {'bag': '48:22 · 33:15 → 54:45', 'kural': "okuma — 'vellâ' + 'dubur'", 'not': 'arka dönme.'},
 {'bag': '15:43 · 11:17 → 54:46', 'kural': "lemma 'mev'id' 12 ayet — yer / vakit", 'not': 'vaat edilen.'},
 {'bag': '54:24 · 54:47', 'kural': "kalıp 'fî dalâlin ve su'ur' 2 ayet, ikisi bu sûrede", 'not': 'sapıklık ve çılgınlık.'},
 {'bag': '43:74 → 54:47', 'kural': "tam kalıp 'inne'l-mucrimîn' 2 ayet", 'not': 'suçlular.'},
 {'bag': '40:71 → 54:48', 'kural': "lemma 'yushab' 2 ayet", 'not': 'sürüklenme.'},
 {'bag': '17:97 · 25:34 → 54:48', 'kural': "tam kalıp 'alâ vucûhihim' 3 ayet — haşr / sahb", 'not': 'yüzüstü.'},
 {'bag': '15:21 → 54:49', 'kural': "lemma 'qader' 10 ayet — indirilenin / yaratılanın ölçüsü", 'not': 'ölçü.'},
 {'bag': '16:77 → 54:50', 'kural': "lemma 'lemh' 2 ayet — 've mâ emru … illâ ke-lemhi'l-basar' kuruluşu", 'not': 'göz kırpışı.'},
 {'bag': '54:49 → 54:50', 'kural': "okuma — 'kulle şey'' / 'vâhide' (aday 1039, kayıt)", 'not': 'her şey / tek.'},
 {'bag': '54:15 · 54:17 · 54:22 · 54:32 · 54:40 · 54:51', 'kural': "tam kalıp 'fe-hel min muddekir' 6 ayet, altısı bu sûrede", 'not': 'öğüt alan var mı.'},
 {'bag': '34:54 · 15:10 · 19:69 → 54:51', 'kural': "lemma 'şî'a' 10 ayet", 'not': 'benzerler / bölükler.'},
 {'bag': '54:43 · 54:52', 'kural': "tam kalıp 'fi'z-zubur' 2 ayet, ikisi bu sûrede", 'not': 'kitaplarda.'},
 {'bag': '54:49 · 54:52', 'kural': "okuma — 'kullu şey'' yaratılan / yapılan", 'not': 'her şey.'},
 {'bag': '18:49 · 10:61 · 34:3 → 54:53', 'kural': 'okuma — küçük / büyük + kitap', 'not': 'küçük büyük.'},
 {'bag': '17:58 · 33:6 → 54:53', 'kural': "okuma — سطر 'mestûr' / 'mustetar'", 'not': 'yazılmış.'},
 {'bag': '15:45 · 51:15 · 52:17 · 44:51 → 54:54', 'kural': "tam kalıp 'inne'l-muttaqîne fî' 6 ayet (77:41 henüz okunmadı); esit2 BENZER", 'not': 'sakınanlar.'},
 {'bag': '54:47 → 54:54', 'kural': "okuma — 'inne'l-X fî A ve B' iskeleti: suçlular / sakınanlar (aday 1039, kayıt)", 'not': 'iki yurt.'},
 {'bag': '9:81 → 54:55', 'kural': "lemma 'maq'ad' 4 ayet", 'not': 'oturak.'},
 {'bag': '54:42 · 54:55', 'kural': "okuma — 'muqtedir' sûrenin iki geçerli mührü", 'not': 'güç yetiren.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_kamer', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in KAMER]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_kamer'] = KAMER
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_kamer', len(KAMER), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_kamer', len(BAGLAR['AS_kamer']))
