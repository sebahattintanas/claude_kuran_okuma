# -*- coding: utf-8 -*-
"""aday_ekle_48_fetih.py — sûre 48 (Fetih) adayları (AX_fetih) ve okuma bağları (AS_fetih).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

FETIH = [
]

BAGLAR = {"AS_fetih": [
 {'bag': '47:38 → 48:1', 'kural': "okuma — ardışık sûre sınırı; hitap 2MP → 2MS, fâsıla م → ا; aday 1040 alanında kayıt, test yok", 'not': 'sûre sınırı.'},
 {'bag': '32:28 · 32:29 · 26:118 → 48:1', 'kural': "'feth' lemma 12 ayet; okunanlarda hüküm / ayırma; sûre içi 48:1, 18, 27", 'not': 'fetih.'},
 {'bag': '47:19 → 48:2', 'kural': "okuma — 'istağfir li-zenbike' / 'li-yağfira leke … min zenbike'; aday 1040 alanına sınırda", 'not': 'günah ve bağışlanma.'},
 {'bag': '12:6 · 16:81 → 48:2', 'kural': "lemma dizisi 'yutimmu ni'metehû aleyk' 5 ayet; okundu", 'not': 'nimetin tamamlanması.'},
 {'bag': '1:6 · 37:118 → 48:2', 'kural': "lemma dizisi 'hedâ + sırât + mustaqîm' 5 ayet; sûre içi 48:2, 48:20 (henüz okunmadı)", 'not': 'dosdoğru yol.'},
 {'bag': '47:7 → 48:3', 'kural': "okuma — نصر 'yensurkum' / 'yensurake'; aday 1040 alanına sınırda", 'not': 'yardım.'},
 {'bag': '48:3 → 48:7', 'kural': "okuma — 'azîz' yardımın sıfatı / Allah; aday 1041 alanında kayıt", 'not': 'azîz.'},
 {'bag': '9:26 · 9:40 → 48:4', 'kural': "'sekîne' lemma 6 ayet; okundu — 'alâ' / 'fî qulûb'; 9:26 görülmeyen ordular / 48:4 göklerin ve yerin orduları", 'not': 'sekîne ve ordular.'},
 {'bag': '48:4 → 48:7', 'kural': "nakarat3 've li'llâhi cunûdu's-semâvâti ve'l-ard … ve kâna'llâhu' (ölçüm, GEÇER); esmâ çifti değişiyor ('alîmen hakîmâ' / 'azîzen hakîmâ')", 'not': 'göklerin ve yerin orduları.'},
 {'bag': '9:72 → 48:5', 'kural': "xref (ölçüm); okundu — 'va'ada' / 'li-yudhile', aynı çift ve cennet terkibi", 'not': 'inanan erkek ve kadınlar.'},
 {'bag': '47:19 → 48:5', 'kural': "okuma — 'li'l-mu'minîne ve'l-mu'minât' ardışık sûrelerde; aday 1040 alanına sınırda", 'not': 'mu\'minîn / mu\'minât.'},
 {'bag': '47:2 · 29:7 → 48:5', 'kural': "lemma dizisi 'keffera + an + seyyie' 12 ayet; okundu", 'not': 'kötülüklerin örtülmesi.'},
 {'bag': '33:73 → 48:6', 'kural': "lemma dizisi 'munâfiq + munâfiqa + muşrik + muşrika' 2 ayet; xref (ölçüm); okundu — 33:73 azap → tevbe (tek ayet), 48:5-6 cennet → azap (iki ayet)", 'not': 'münafık ve müşrikler.'},
 {'bag': '9:98 → 48:6', 'kural': "lemma dizisi 'aleyhim dâ'iratu's-sev'' 2 ayet; okundu", 'not': 'kötülük çemberi.'},
 {'bag': '48:5 → 48:6', 'kural': "okuma — aynı ta'lîl lâmına atıf; cennet / azap; karşıt çift (aday 1039, okuma)", 'not': 'iki çift.'},
 {'bag': '33:45 → 48:8', 'kural': "lemma dizisi 'erselnâke şâhiden ve mubeşşiran ve nezîrâ' 2 ayet; xref (ölçüm); okundu — 33:45 nidâlı", 'not': 'şahit, müjdeci, uyarıcı.'},
 {'bag': '48:1 → 48:8', 'kural': "okuma — 'innâ fetahnâ leke' / 'innâ erselnâke' (aynı açılış)", 'not': 'innâ + 1P + 2MS.'},
 {'bag': '33:42 → 48:9', 'kural': "lemma dizisi 'sebbeha + bukra + asîl' 2 ayet; xref (ölçüm); okundu", 'not': 'sabah akşam tesbih.'},
 {'bag': '9:111 → 48:10', 'kural': "okuma — 'evfâ', ''ahd', 'bâya'a' 9:111'de bir arada (KAPATILAMAZ); 'bâya'a' lemma 4 ayet", 'not': 'biat ve ahit.'},
 {'bag': '47:38 · 29:6 · 31:12 → 48:10', 'kural': "okuma — 'men … fe-innemâ … nefsih' kalıbı (cimrilik / cihad / şükür / ahit bozma); aday 1040 alanına sınırda", 'not': 'kendi aleyhine.'},
 {'bag': '9:12 · 43:50 → 48:10', 'kural': "'nekese' lemma 5 ayet; okundu", 'not': 'ahdi bozma.'},
 {'bag': '48:10 (yed)', 'kural': "okuma — 'yedu'llâhi fevqa eydîhim': يدي aynı lemma Allah ve insan; aday 1041 alanında kayıt", 'not': 'el.'},
 {'bag': '9:81 → 48:11 · 48:15 · 48:16', 'kural': "'muhallef' lemma 4 ayet; 9:81 okundu; sûre içi üç ayet", 'not': 'geri bırakılanlar.'},
 {'bag': '9:80 · 12:97 · 24:62 → 48:11', 'kural': "lemma dizisi 'istağfir lenâ / lehum' 12 ayet; okundu", 'not': 'bağışlanma dileme.'},
 {'bag': '47:19 → 48:11', 'kural': "okuma — 'istağfir li-zenbik' (emir) / 'fe'stağfir lenâ' (bedevî isteği)", 'not': 'istiğfar.'},
 {'bag': '48:11 → 48:18', 'kural': "okuma — 'mâ leyse fî qulûbihim' / 'alime mâ fî qulûbihim'; karşıt çift (aday 1039, okuma)", 'not': 'kalplerdeki.'},
 {'bag': '48:11 → 48:14', 'kural': "okuma — ملك 'yemliku' / 'mulk'; غفر 'istağfir' / 'yağfiru'; aday 1041 alanında kayıt", 'not': 'mülk ve bağış.'},
 {'bag': '48:6 → 48:12', 'kural': "okuma — 'zanne's-sev'' sûre içi iki kez; 3MP / 2MP", 'not': 'kötü zan.'},
 {'bag': '25:18 → 48:12', 'kural': "lemma dizisi 'kâne qavmen bûrâ' 2 ayet; xref (ölçüm); okundu", 'not': 'helâk olan topluluk.'},
 {'bag': '48:6 → 48:13', 'kural': "okuma — 'e'adde lehum cehennem' (عدد) / 'a'tednâ … se'îrâ' (عتد); KAPATILAMAZ", 'not': 'hazırlanan ateş.'},
 {'bag': '24:42 · 42:49 · 45:27 → 48:14', 'kural': "lemma dizisi 've li'llâhi mulku's-semâvâti ve'l-ard' 8 ayet; okundu", 'not': 'göklerin ve yerin mülkü.'},
 {'bag': '48:4 · 48:7 → 48:14', 'kural': "okuma — 'cunûdu's-semâvâti ve'l-ard' / 'mulku's-semâvâti ve'l-ard'", 'not': 'ordular / mülk.'},
 {'bag': '9:83 → 48:15', 'kural': "okuma — geri kalanlara 'len' ile ret, aynı yapı; KAPATILAMAZ", 'not': 'uymayacaksınız.'},
 {'bag': '47:38 → 48:16', 'kural': "okuma — 've in tetevellev' ardışık sûrelerde, cevap farklı; aday 1040 alanına sınırda", 'not': 'yüz çevirme.'},
 {'bag': '9:39 → 47:38 · 48:16', 'kural': "lemma dizisi 'yu'azzibkum azâben elîmâ' 4 ayet; xref (ölçüm); 9:39'un iki parçası ardışık sûrelerde — KAPATILAMAZ", 'not': 'acı azap ve değiştirme.'},
 {'bag': '17:5 · 27:33 → 48:16', 'kural': "'ulû be's şedîd' okundu", 'not': 'çetin savaş gücü.'},
 {'bag': '24:61 → 48:17', 'kural': "lemma dizisi 'leyse ale'l-a'mâ harac…' 2 ayet; xref (ölçüm); okundu — bağlam farklı", 'not': 'kör, topal, hasta.'},
 {'bag': '48:16 → 48:17', 'kural': "okuma — itaat / yüz çevirme 2MP şart → 3MS genel şart", 'not': 'iki seçenek.'},
 {'bag': '48:10 → 48:18', 'kural': "okuma — 'yubâyi'ûneke' sûre içi; 48:18 yer ve zaman ile", 'not': 'biat.'},
 {'bag': '48:4 → 48:18', 'kural': "okuma — sekîne sûre içi ikinci; 'fî qulûb' / 'aleyhim'", 'not': 'sekîne.'},
 {'bag': '48:1 → 48:18', 'kural': "okuma — 'fethan mubînâ' / 'fethan qarîbâ'", 'not': 'fetih.'},
 {'bag': '48:7 → 48:19', 'kural': "nakarat3 've kâna'llâhu azîzen hakîmâ' (ölçüm, GEÇER)", 'not': 'azîz hakîm.'},
 {'bag': '48:19 → 48:20', 'kural': "okuma — 'meğânime kesîraten ye'huzûnehâ / te'huzûnehâ' 3MP → 2MP", 'not': 'ganimetler.'},
 {'bag': '48:2 → 48:20', 'kural': "okuma — 'yehdiyeke / yehdiyekum sırâtan mustaqîmâ' 2MS → 2MP", 'not': 'dosdoğru yol.'},
 {'bag': '48:10 → 48:20 (yed)', 'kural': "okuma — 'yedu'llâh' / 'eydiye'n-nâs'; aday 1041 alanında kayıt", 'not': 'el.'},
 {'bag': '48:20 → 48:21', 'kural': "okuma — 've uhrâ' 48:20 'meğânime kesîra'ya atıf", 'not': 'başka ganimetler.'},
 {'bag': '33:27 → 48:21', 'kural': "lemma dizisi 've kâna'llâhu alâ kulli şey'in qadîrâ' 2 ayet; okundu — henüz ayak basılmamış yer + aynı kapanış", 'not': 'her şeye güç yetiren.'},
 {'bag': '48:21 (qadr)', 'kural': "okuma — قدر 'lem taqdirû' / 'qadîr' aynı ayette; aday 1041 alanında kayıt (kök)", 'not': 'güç.'},
 {'bag': '33:15 → 48:22', 'kural': "lemma dizisi 'vellâ + dubur' 6 ayet; okundu", 'not': 'arka dönme.'},
 {'bag': '33:65 → 48:22', 'kural': "lemma dizisi 'lâ yecidûne veliyyen ve lâ nasîrâ' 2 ayet; xref (ölçüm); okundu — ateşte / savaşta; KAPATILAMAZ", 'not': 'dost ve yardımcı yok.'},
 {'bag': '48:3 → 48:22', 'kural': "okuma — نصر 'nasran' (Allah'ın yardımı) / 'lâ nasîrâ'", 'not': 'yardım.'},
 {'bag': '33:62 · 35:43 · 33:38 → 48:23', 'kural': "lemma dizisi 'len tecide li-sunneti'llâhi tebdîlâ' 3 ayet; esit2 BENZER 33:62 (ölçüm); okundu", 'not': 'Allah\'ın yasası.'},
 {'bag': '48:15 → 48:23', 'kural': "okuma — بدل 'yubeddilû kelâma'llâh' / 'len tecide … tebdîlâ'", 'not': 'değiştirme.'},
 {'bag': '48:20 → 48:24', 'kural': "okuma — 'keffe eydiye … ankum' tek yön → iki yön (ayna)", 'not': 'ellerin çekilmesi.'},
 {'bag': '33:9 · 48:11 → 48:24', 'kural': "lemma dizisi 'kâna'llâhu bimâ ta'melûne basîrâ' 3 ayet; nakarat3 GEÇER (ölçüm); 48:11 'habîrâ' aynı çerçeve", 'not': 'gören.'},
 {'bag': '33:27 · 9:120 → 48:25', 'kural': "'vati'e' lemma 3 ayet; okundu", 'not': 'ayak basma.'},
 {'bag': '48:5 → 48:25', 'kural': "okuma — erkek / kadın çiftleri sûre içi", 'not': 'inanan erkek ve kadınlar.'},
 {'bag': '48:16 · 48:17 → 48:25', 'kural': "okuma — 'azâben elîmâ' sûre içi üç ayet", 'not': 'acı azap.'},
 {'bag': '9:26 → 48:26', 'kural': "lemma dizisi 'enzela'llâhu sekînetehû alâ rasûlihî ve ale'l-mu'minîn' 2 ayet; xref (ölçüm); okundu", 'not': 'sekîne.'},
 {'bag': '48:4 · 48:18 → 48:26', 'kural': "okuma — sekîne sûre içi üç ayet; 48:4 inananların kalbine sekîne / 48:26 inkâr edenlerin kalbinde hamiyye", 'not': 'kalp ve sekîne.'},
 {'bag': '33:33 → 48:26', 'kural': "'câhiliyye' lemma 4 ayet; okundu", 'not': 'cahiliye.'},
 {'bag': '33:40 → 48:26', 'kural': "lemma dizisi 've kâna'llâhu bi-kulli şey'in alîmâ' 2 ayet; okundu", 'not': 'her şeyi bilen.'},
 {'bag': '37:105 · 12:100 → 48:27', 'kural': "'ru'yâ' lemma 6 ayet; okundu — 'saddaqte'r-ru'yâ' / 'sadaqa'llâhu … er-ru'yâ'; ru'yâ + haqq; KAPATILAMAZ", 'not': 'rüya.'},
 {'bag': '12:99 → 48:27', 'kural': "lemma dizisi 'in şâ'a'llâhu âminîn' 2 ayet; xref (ölçüm); okundu — iki ayette girme + in şâ'a'llâh + âminîn", 'not': 'güven içinde girme.'},
 {'bag': '48:18 → 48:27', 'kural': "lemma dizisi 'fethan qarîbâ' 3 ayet (61:13 henüz okunmadı); 'fe-alime mâ' sûre içi iki ayet", 'not': 'yakın fetih.'},
 {'bag': '9:33 → 48:28', 'kural': "lemma dizisi 'huwe'llezî ersele rasûlehû … kullih' 3 ayet; xref (ölçüm); okundu — aynı cümle, farklı kapanış", 'not': 'hak din.'},
 {'bag': '10:29 · 13:43 · 17:96 → 48:28', 'kural': "lemma dizisi 'kefâ bi'llâhi şehîdâ' 6 ayet; okundu — üçünde 'beynî ve beynekum', 48:28'de yok", 'not': 'tanık olarak Allah.'},
 {'bag': '48:8 → 48:28', 'kural': "okuma — شهد 'şâhiden' (elçi) / 'şehîdâ' (Allah); aday 1041 alanında kayıt (kök)", 'not': 'tanık.'},
 {'bag': '33:40 · 47:2 → 48:29', 'kural': "'Muhammed' lemma 4 ayet; okundu; 47:2 → 48:29 ardışık sûre (aday 1040 alanına sınırda)", 'not': 'Muhammed.'},
 {'bag': '47:30 → 48:29', 'kural': "'sîmâ' lemma 6 ayet; okundu — ardışık sûrelerde; aday 1040 alanına sınırda; KAPATILAMAZ", 'not': 'nişan.'},
 {'bag': '48:14 → 48:29', 'kural': "okuma — 'rahîm' Allah / 'ruhamâ'' insanlar; aday 1041 alanında kayıt", 'not': 'merhamet.'},
 {'bag': '48:16 → 48:29', 'kural': "okuma — شدد 'be'sin şedîd' (düşman) / 'eşiddâ'' (elçinin yanındakiler)", 'not': 'çetinlik.'},
 {'bag': '9:112 → 48:29', 'kural': "lemma dizisi 'râki' + sâcid' 2 ayet; okundu", 'not': 'rükû ve secde.'},
 {'bag': '48:18 → 48:29', 'kural': "okuma — رضو 'radiya'llâhu' / 'yebteğûne … ridvânâ'", 'not': 'hoşnutluk.'},
 {'bag': '9:111 → 48:29', 'kural': "okuma — Tevrât ve İncîl 9:111'de vaat, 48:29'da vasıf", 'not': 'iki kitap.'},
 {'bag': '39:21 → 48:29', 'kural': "'zer'' lemma 10 ayet; okundu — 39:21 büyüme → çöküş (L4) / 48:29 yalnız büyüme, teşbih içinde (L4 adayı, TARTIŞMALI); KAPATILAMAZ", 'not': 'ekin.'},
 {'bag': '9:120 → 48:29', 'kural': "'ğâza' lemma 3 ayet; okundu — 'yeğîzu'l-kuffâr' / 'li-yeğîza bihimu'l-kuffâr'", 'not': 'öfkelendirme.'},
 {'bag': '48:1 → 48:29', 'kural': "okuma — sûre açılışı 'fethan mubînâ' / kapanışı 'ecran azîmâ'; fâsıla ا sûre boyunca", 'not': 'sûre çerçevesi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_fetih', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in FETIH]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_fetih'] = FETIH
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_fetih', len(FETIH), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_fetih', len(BAGLAR['AS_fetih']))
