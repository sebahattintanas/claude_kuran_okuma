# -*- coding: utf-8 -*-
"""necm_kayit.py — sûre 53 (Necm) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 53

CIPA = {
 # blok 1-10
 1: dict(kademe='L1', olgu=True, cipa=False, not_="'ve'n-necmi izâ hevâ' — yıldız + hâl (düşme / batma), yemin nesnesi; süreç / ölçü / mekanizma yok — L1 (52:9 emsali); tarayıcı vermedi"),
 7: dict(kademe='L1', olgu=True, cipa=False, not_="'bi'l-ufuqi'l-a'lâ' — ufuk + nitelik, anlatıda konum olarak; süreç yok — L1; tarayıcı vermedi"),
 9: dict(kademe=None, olgu=False, cipa=False, not_="'qâbe qavseyni ev ednâ' — mesafe birimi adlanıyor (anlatı içi yakınlık), doğal olgu değil; üst sınır 'ev ednâ' ile açık — çıpa değil; tarayıcı vermedi"),
 # blok 11-20
 14: dict(kademe=None, olgu=False, cipa=False, not_="'sidrati'l-muntehâ' — ağaç adı (sidr) yer izâfetinde; doğal olgu iddiası değil, KAPATILAMAZ; tarayıcı vermedi"),
 # blok 21-30
 26: dict(kademe='L0', olgu=True, cipa=False, not_="'fi's-semâvât' — meleklerin bulunduğu yer olarak gökler adlanıyor; nitelik / süreç / ölçü yok — L0 (51:22 emsali); tarayıcı vermedi"),
 # blok 31-40
 31: dict(kademe='L0', olgu=True, cipa=False, not_="'mâ fi's-semâvâti ve mâ fi'l-ard' — gökler ve yer mülkiyet ifadesinde adlanıyor; ta'lîl 'li-yecziye' karşılığa bağlı, doğal nedensellik değil — L0; tarayıcı v4 adayı, çıpa değil"),
 32: dict(kademe='L1', olgu=True, cipa=False, not_="'enşe'ekum mine'l-ard … ecinnetun fî butûni ummehâtikum' — kaynak (yer) ve hâl (karında cenin) adlanıyor, ara aşama / süreç yok (39:6 'halqan min ba'di halq' ardışıklığı burada yok) — L1; tarayıcı vermedi"),
 # blok 41-50
 44: dict(kademe='L0', olgu=True, cipa=False, not_="'emâte ve ahyâ' — ölüm ve dirilik fiil olarak adlanıyor, fâil 'huwa'; süreç / aşama yok — L0; tarayıcı vermedi"),
 45: dict(kademe='L1', olgu=True, cipa=False, not_="'halaqa'z-zevceyni'z-zekera ve'l-unsâ' + 53:46 'min nutfetin' — çift ve madde adlanıyor, ara aşama yok (35:11 emsali L1); tarayıcı vermedi"),
 46: dict(kademe='L1', olgu=True, cipa=False, not_="'min nutfetin izâ tumnâ' — madde (nutfe) + hâl (dökülme), aşama ardışıklığı yok — L1; tarayıcı vermedi"),
 49: dict(kademe='L0', olgu=True, cipa=False, not_="'rabbu'ş-şi'râ' — bir yıldız adla anılıyor, nitelik / süreç yok — L0; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  'esmâ: blokta e_oto tokeni yok; mühür ölçümü [] — karar gerekmedi; lafız 0, Rab 0',
  "aday 1040 alanı: 52:49 → 53:1 (fâsıla م → ى); 52:49 'idbâra'n-nucûm' / 53:1 've'n-necm'; 51:1, 52:1, 53:1 ardışık üç sûre 've' yeminiyle açılıyor; 52:29 'mâ ente … bi-kâhinin ve lâ mecnûn' / 53:2 'mâ dalle sâhibukum ve mâ ğavâ' — kayıt, test yok",
  "aday 1041 alanı (lemma 'istevâ'): 20:5 Rahmân / 28:14 insan / 48:29 ekin; 53:6'da özne adsız — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): yemin eden adsız; 53:2 'sâhibukum' adlanmıyor, muhatap 2MP adsız; 53:4 'huve' göndergesi, 53:5 öğreten 'şedîdu'l-quvâ' ve 'allemehû' zamiri, 53:6-9 özne 3MS, 53:10 vahyeden ve 'abdihî' göndergesi adlanmıyor; 53:4 vahyeden (edilgen) adsız — meal hiçbirini adlandırmadı, KAPATILAMAZ",
  "biçim (517 ailesi): 53:1 QASEM işaretli, 52:1 ve 51:1'de işaretsizdi (tutarsızlık araçta); 53:4 HASR işaretli",
  "ölçüm (924): 53:1 harf 31 → harf3 12 — besmele bitişik; 53:3 fâsıla medd işareti 'ٓ' olarak okunmuş, KAFİYE KIRILMASI işaretli — araç artefaktı",
  'yıldız formülü: 53:4 ★★★ pas z=5,38 (edilgen gerçek); 53:9 ★★★ hapaks قوب قوس z=6,79 (kok_ekle_53, ikisi de 1 token) — bilinen davranış, içerik iddiası değil',
  "yıldız etiketi (1001): 53:3 ★ kafiye kırığından (araç artefaktı), bilanço etiketi 'n' z=-0,89",
  "kök çok-anlam (sûre içi): هوي 53:1 'hevâ' (düştü) / 53:3 'el-hevâ' (arzu) — gloss ikisini kapsıyor",
  'gloss (1021 ailesi): kok_ekle_53 altı kök — قوب قوس ضيز لمم كدي قني; dördü 1 token, anlamlar korpus içinden doğrulanamaz',
  'çıpa: 53:9 mesafe birimi (qâb qavseyn) — ölçü kolu, ama doğal olgu değil, çıpa merdivenine girmiyor',
  'okuma: 52:49, 51:1, 52:1, 14:37, 20:81, 22:31 → 53:1; 34:46, 20:121, 28:63, 52:29 → 53:2; 34:46, 36:69, 12:104, 38:87, 23:25, 11:37, 23:27 → 53:4; 51:58 → 53:5; 20:5, 41:11, 28:14, 48:29 → 53:6; 41:53 → 53:7; 20:38 → 53:10 — KAPATILAMAZ',
  'tetik: ön kuru koşu 1 tetik satırı (53:1 نجم) — ilk koşuda 0 uyuşmaz; [x/y] ilk koşuda 0 (23 sayım)',
 ],
 (11, 20): [
  'esmâ: blokta e_oto tokeni yok; mühür ölçümü [] — karar gerekmedi; lafız 0, Rab 1 (53:18, sûre içi [1/7])',
  "aday 1041 alanı (kök düzeyi): عزز 38:9 'el-azîz' (Rab) / 53:19 'el-Uzzâ' (put adı) — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 53:11-18 gören, görülen ('ra'âhu'), örten ('mâ yağşâ'), gözün sahibi adlanmıyor; 53:12 muhatap 2MP adsız; meal adlandırmadı — KAPATILAMAZ",
  "ölçüm (924): 53:12 morph 'tumârûnehû'yu PASS etiketliyor; fiil III. bab etken, ön ek ötresi edilgenle aynı görünüyor — EDİLGEN 1/2 ve ★★ pas z=2,52 araç arızası",
  "fâsıla (924): 53:11, 15, 18, 20 fâsıla medd işareti 'ٓ' olarak okunmuş (harf ى), KAFİYE KIRILMASI işaretli; 53:19 ى iken önceki artefakta bağlı kırık — beş ayetin hepsi araç davranışı",
  "yıldız etiketi (1001): 53:11, 15, 19, 20 ★ bu kırık işaretinden, bilanço etiketi 'n'",
  'yıldız formülü: 53:18 ★★★ rab z=3,23 (6 kelimede 1 Rab) — bilinen davranış, içerik iddiası değil',
  "biçim (517 ailesi): 53:15 takdim 'indehâ' ölçümde işaretsiz; 53:13, 18 CERT / EMPH, 53:12, 19 INTG işaretli",
  "kuruluş (okuma): 'fiil + mâ + aynı fiil' 53:10 'evhâ … mâ evhâ' ve 53:16 'yağşâ … mâ yağşâ'; 20:78 'ğaşiyehum … mâ ğaşiyehum' aynı fiille; 'mâ … ve mâ' olumsuzlaması 53:2 ve 53:17",
  "görme zinciri (okuma): رأي sûre içi 53:11, 12, 13, 18 gören 3MS → 53:19 'e-fe-ra'eytum' muhatap 2MP; ölçüm iltifât 53:19",
  "lemma: 'sidre' korpusta yalnız 53:14 ve 53:16; 'el-Lât', 'el-Uzzâ', 'Menât' korpusta 1'er",
  "gloss (1021 ailesi): مني 'temenni, kuruntu; meni' — 'Menât' özel adını kapsamıyor; فأد 'fuâd' ◈B tetik listesinde değil (gözlem ◇'de)",
  'okuma: 17:36, 28:10 → 53:11; 42:18 → 53:12; 32:19 → 53:15; 20:78, 53:10 → 53:16; 33:10, 53:2 → 53:17; 20:23 → 53:18; 26:75, 39:38, 38:9 → 53:19 — KAPATILAMAZ',
  "tetik: ön kuru koşu 1 tetik satırı (53:17 بصر ◈B) — ilk koşuda 0 uyuşmaz; [x/y] ilk koşuda 0 (28 sayım); kayıttan önce 53:12 ve 53:14'te başka sûre ayetine 'sûre içi' etiketi düzeltildi",
 ],
 (21, 30): [
  "esmâ: e_oto 3 token (53:25 'âhir', 'evvel'; 53:27 'âhir') — el kararı üçü de 'degil' (âhiret / ilk; esma_el KARAR 460); esma_muhur_43 [25] → geçerli [] — mühür yok; lafız 3 (53:23, 25, 26), Rab 2 (53:23, 30)",
  "ölçüm (924): 53:22 'biçim QASEM' — قسم kökü yemin okunmuş; 'qisme' paylaştırma, yemin yok — araç arızası",
  "fâsıla (924): 53:26 fâsıla medd işareti 'ٓ' olarak okunmuş, KAFİYE KIRILMASI; 53:21 ى iken önceki ayetin 'ٓ' artefaktına bağlı kırık; 53:22, 23 'ٓ' sınıfı kırıksız (önceki de 'ٓ') — araç davranışı",
  "yıldız etiketi (1001): 53:21, 26 ★ kafiye kırık işaretinden, bilanço etiketi 'n'",
  'yıldız formülü: 53:22 ★★★ hapaks z=3,28 (ضيز, kök ve lemma korpusta 1); 53:25 ★★★ allah z=6,14 (3 kelimede 1. sırada lafız) — bilinen davranış, içerik iddiası değil',
  "biçim (517 ailesi): 53:25 takdim 'li'llâhi' ölçümde işaretsiz; 53:24 soru 'em' kip işaretsiz; 53:23 ayet içi 2MP → 3MP geçişi, ölçüm iltifât 0",
  "konuşan / gönderge (1017 ailesi): 53:21 'lehu' göndergesi, 53:29 1P konuşan ('zikrinâ') ve 2MS muhatap, 53:30 'rabbeke' muhatabı adlanmıyor; meal adlandırmadı — KAPATILAMAZ",
  "gloss (1021 ailesi): مني [2/3] 53:24 'temennâ' — 53:20 'Menât' aynı sayaçta, gloss özel adı kapsamıyor; ذكر 53:21 'zeker' / 53:29 'zikr' aynı sayaçta (gloss 'anma, zikir' cinsi kapsamıyor)",
  "ad koyma ipliği (okuma): سمو 53:23 'esmâ'un semmeytumûhâ' [1,2/6], 53:27 'yusemmûne … tesmiye' [4,5/6]; 'tesmiye' lemma korpusta 1",
  "kalıplar (sayım): 'in yettebi'ûne ille'z-zann' 4 ayet (sûre içi 53:23, 28); 'ez-zanne lâ yuğnî mine'l-haqqi şey'â' 2 ayet (10:36, 53:28); 'inne rabbeke huwa a'lemu bi-men dalle an sebîlihî' 3 ayet (16:125, 53:30, 68:7 henüz okunmadı)",
  'karşıt çift (aday 1039, okuma): ayet içi 53:21 zeker / unsâ, 53:23 zann-hevâ / hudâ, 53:25 âhira / ûlâ, 53:28 zann / haqq, 53:30 dalle / ihtedâ — kayıt, test yok',
  "çıpa: 53:26 L0 ('fi's-semâvât', meleklerin yeri); tarayıcı adayı yok",
  'okuma: 52:39 → 53:21; 12:40, 10:66, 53:1, 53:3 → 53:23; 28:70 → 53:25; 36:23, 20:109, 34:23 → 53:26; 37:150, 43:19 → 53:27; 10:36 → 53:28; 53:8, 53:9 → 53:29; 16:125, 53:2 → 53:30 — KAPATILAMAZ',
  'tetik: ön kuru koşu 5 tetik satırı (53:21, 27 أنث ◈B; 53:24 أنس ◈B; 53:26 سمو ◈K; 53:29 حيي ◈B) — kayıtta 0 uyuşmaz; [x/y] ilk koşuda 0 (23 sayım); oturum_say aralıkları duraklama işaretleri (ۚ ۖ ۞) dışlanarak yeniden sayıldı',
 ],
 (31, 40): [
  "esmâ: e_oto 1 token (53:32 'vâsi'') — el kararı 'ilahi' (Rab'bin yüklemi; esma_el KARAR 461); esma_muhur_43 [] — mühür yok; lafız 1 (53:31), Rab 1 (53:32)",
  "edilgen: 53:36 'yunebbe'' ve 53:40 'yurâ' gerçek edilgen — ölçüm doğru; ★★★ pas z=5,38 ikisinde de (tek fiilli kısa ayet) — formül davranışı",
  'yıldız formülü: 53:34 ★★★ hapaks z=3,28 (كدي, kök ve lemma korpusta 1)',
  "fâsıla (924): 53:32, 37 fâsıla 'ٓ' okunmuş, KAFİYE KIRILMASI; 53:33, 36 ى iken önceki 'ٓ' artefaktına bağlı kırık; 53:34, 35 'ٓ' sınıfı kırıksız (önceki de 'ٓ') — araç davranışı",
  "yıldız etiketi (1001): 53:32, 33, 37 ★ kafiye kırık işaretinden, bilanço etiketi 'n'",
  "biçim (517 ailesi): 53:31 takdim 've li'llâhi' ölçümde işaretsiz; 53:32 ayet içi 3MP → 2MS → 2MP geçişi, ölçüm iltifât 0",
  'konuşan / gönderge (1017 ailesi): 53:31 kötülük / iyilik edenler, 53:33-35 arka çeviren, 53:36 haber veren ve 53:40 gören (edilgen) adlanmıyor; 53:36 Mûsâ ve 53:37 İbrâhîm metindeki adlar — meal metin dışı ad eklemedi',
  "◈B tetik listesi (ön-kayıt §4): 53:32 'ecinne fî butûni ummehâtikum' — جنن, بطن tetik listesinde değil; satır '—', gözlem ◇'de",
  "aday 1041 alanı (kök düzeyi): غفر 42:37 'hum yağfirûn' (insan) / 53:32 'vâsi'u'l-mağfira' (Rab) — aynı 'kebâ'ira'l-ismi ve'l-fevâhiş' dizisinin ardından; kayıt, test yok",
  "lemma (sayım): 'lemem', 'ecinne', 'ekdâ' korpusta 1'er; 'vâzire' 5 ayet — hepsi 'lâ teziru vâziratun vizra uhrâ' kalıbında; 'butûni ummehâtikum' 3 ayet (16:78, 39:6, 53:32)",
  "görme zinciri kapandı (okuma): رأي [8/8] — 53:11, 12, 13, 18 (3MS) → 53:19 (2MP) → 53:33 (2MS) → 53:35 'yerâ' → 53:40 edilgen 'yurâ'",
  "karşıt çift (aday 1039, okuma): ayet içi 53:31 esâ'û / ahsenû, 53:32 kebâ'ir / lemem, 53:34 a'tâ / ekdâ; ayetler arası 53:24 temennâ / 53:39 se'â — kayıt, test yok",
  'okuma: 42:37, 16:78, 39:6, 35:18 → 53:32; 19:77, 45:23 → 53:33; 52:41 → 53:35; 17:15, 35:18, 39:7 → 53:38; 20:15, 53:24 → 53:39 — KAPATILAMAZ',
  'tetik: ön kuru koşu 3 tetik satırı (53:31 سمو أرض ◈K; 53:32 أرض ◈K; 53:39 أنس ◈B) — kayıtta 0 uyuşmaz; [x/y] 0 (23 sayım); kayıttan önce basılmamış iki ayet anması (53:33, 53:36 notlarında) ve ölçülmemiş bir 1041 notu (53:37) çıkarıldı',
 ],
 (41, 50): [
  "esmâ: e_oto 1 token (53:50 'evvel') — el kararı 'degil' (Âd'ın sıfatı; esma_el KARAR 462); esma_muhur_43 [50] → geçerli [] — mühür yok; lafız 0, Rab 2 (53:42, 49)",
  "edilgen: 53:41 'yuczâ' ve 53:46 'tumnâ' gerçek edilgen — ölçüm doğru; ★★★ pas z=5,38 (tek fiilli kısa ayet) — formül davranışı",
  'yıldız formülü: 53:42 ve 53:49 ★★★ rab z=5,01 (4 kelimede 3. sırada Rab); 53:48 ★★★ hapaks z=3,28 (قني) — bilinen davranış',
  "fâsıla: blokta kafiye kırığı yok — on fâsılanın hepsi ى / ا (A sınıfı); 'ٓ' artefaktı bu blokta görünmüyor",
  "aktör (924 / 1021): 53:49 'Şi'râ' ölçümde 'sahte-ilah, rol fail' — metinde ad izâfetle (GEN), tapınma söylenmiyor; sınıf ve rol araç kategorisi, KAPATILAMAZ; gloss شعر 'şair; farkında olma' yıldız adını kapsamıyor",
  "gloss (1021 ailesi): مني [3/3] sayacı 53:20 'Menât', 53:24 'temennâ', 53:46 'tumnâ' üç anlamı topluyor; عود 53:50 'Âd' kavim adını kapsamıyor; lemma 'Âd' 2:173, 6:145'teki 'âd' (aşan) kelimesini de sayıyor",
  "biçim (517 ailesi): 53:42 'ilâ rabbike', 53:47 'aleyhi' takdimi ve 53:43, 44, 48, 49 'huwa' ayırma zamiri ölçümde işaretsiz",
  "konuşan / gönderge (1017 ailesi): 53:41 karşılığı veren (edilgen), 53:42 muhatap 2MS adsız; 'huwa' göndergesi 53:42 'rabbike' (okuma) — meal 'O' ile verdi, ad eklemedi",
  "kalıp (sayım): 've ennehû huwa' tam kalıp 4 ayet — 53:43, 44, 48, 49; korpusta yalnız bu sûrede",
  "sûre içi iplikler (okuma): ذكر/أنث 53:21 soru → 53:45 yaratma; نهي 53:14 'sidrati'l-muntehâ' → 53:42 'ilâ rabbike'l-muntehâ'; وفي 53:37 'vaffâ' → 53:41 'el-evfâ'; جزي 53:31 ×2 → 53:41 ×2; نشأ 53:32 → 53:47; غني 53:26, 28 olumsuz → 53:48 olumlu",
  'karşıt çift (aday 1039, okuma): ayet içi 53:43 adheke / ebkâ, 53:44 emâte / ahyâ, 53:45 zeker / unsâ; ayetler arası 53:32 / 53:47 — kayıt, test yok',
  'çıpa: 53:44 L0, 53:45 L1, 53:46 L1, 53:49 L0; tarayıcı adayı yok',
  'okuma: 20:15, 53:31, 53:37 → 53:41; 53:14 → 53:42; 9:82 → 53:43; 50:43 → 53:44; 51:49, 53:21 → 53:45; 35:11 → 53:46; 29:20, 53:32 → 53:47; 53:1 → 53:49; 51:41, 53:25 → 53:50 — KAPATILAMAZ',
  "tetik: ön kuru koşu 3 tetik satırı (53:44 موت حيي; 53:45 خلق زوج أنث; 53:46 نطف; hepsi ◈B) — kayıtta 0 uyuşmaz; [x/y] 0 (15 sayım); kayıttan önce 53:50 notunda okunmamış iki ayete 'henüz okunmadı' eklendi",
 ],
 (51, 62): [
  "esmâ: e_oto 1 token (53:56 'evvel') — el kararı 'degil' (uyarıcıların sıfatı; esma_el KARAR 463); esma_muhur_43 [56] → geçerli [] — mühür yok; lafız 2 (53:58, 62), Rab 1 (53:55)",
  'yıldız formülü: 53:55 ★★★ rab z=5,01; 53:62 ★★★ allah z=6,14; 53:58 ★★ allah z=2,80; 53:61 ★★★ hapaks z=3,28 (سمد) — bilinen davranış',
  "fâsıla (okuma): 53:57-58 ة (H), 53:59-61 ن (N), 53:62 ا — sûrenin ى fâsılasından ayrılan son bölüm; ölçüm bu blokta KAFİYE KIRILMASI işaretlemedi (sınıf geçişi 53:57'de işaretsiz) — araç davranışı, KAPATILAMAZ",
  "biçim (517 ailesi): 53:52 'inne … kânû hum' tekit ve ayırma zamiri, 53:53 meful takdimi, 53:58 'leyse' olumsuzluğu ölçümde işaretsiz",
  "konuşan / gönderge (1017 ailesi): 53:53 'el-mu'tefike' metinde adlanmıyor — meal ad eklemedi; 53:54 büren, 53:56 'hâzâ', 53:57 'el-âzife' adsız; 53:55 muhatap 2MS, 53:59-62 muhatap 2MP adsız",
  'gloss: سمد iki okuma veriyor (oyalanma / başı dik durma) — meal birini seçti, KAPATILAMAZ',
  "kuruluş (okuma): 'fiil + mâ + aynı fiil' sûre içi üç kez — 53:10 'evhâ … mâ evhâ', 53:16 'yağşâ … mâ yağşâ', 53:54 'ğaşşâ … mâ ğaşşâ'; 53:16 ve 53:54 aynı kök (غشو)",
  "sûre içi iplikler kapandı (okuma): هوي 53:1 → 53:53 'ehvâ'; مري 53:12 → 53:55; طغي 53:17 → 53:52; ضحك/بكي 53:43 → 53:60; أول 53:25, 50 → 53:56; ليس 53:39 → 53:58; عبد 53:10 → 53:62; Rab [7/7] 53:55; lafız [6/6] 53:62",
  "liste (okuma): 53:50-53 Âd, Semûd, Nûh kavmi, 'el-mu'tefike' — 9:70 aynı dördü 'mu'tefikât' çoğuluyla bir ayette veriyor",
  "karşıt çift (aday 1039, okuma): ayet içi 53:60 tadhakûne / lâ tebkûn; ayetler arası 53:17 'mâ tağâ' / 53:52 'atğâ', 53:43 / 53:60 — kayıt, test yok",
  'aday 1040 (sûre sınırı): 53:62 → 54:1 henüz okunmadı — kayıt yok',
  'çıpa: blokta olgu adlanan ayet yok; tarayıcı adayı yok',
  'okuma: 51:43 → 53:51; 51:46, 9:70, 53:17 → 53:52; 9:70, 53:1 → 53:53; 53:10, 53:16 → 53:54; 53:12 → 53:55; 51:50 → 53:56; 40:18 → 53:57; 39:38 → 53:58; 52:34, 50:2 → 53:59; 53:43, 9:82 → 53:60; 41:37, 53:10 → 53:62 — KAPATILAMAZ',
  'tetik: ön kuru koşu 0 tetik satırı — kayıtta 0 uyuşmaz; [x/y] 0 (12 sayım)',
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_53.py uygular)
DUZELTME = {
}
