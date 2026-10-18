# -*- coding: utf-8 -*-
"""rahman_kayit.py — sûre 55 (Rahmân) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 55

CIPA = {
 # blok 1-10
 3: dict(kademe='L0', olgu=True, cipa=False, not_="'halaqa'l-insân' — insan adlanıyor, madde / evre yok (16:4, 32:7'de 'min nutfe', 'min tîn' var) — L0; tarayıcı vermedi"),
 5: dict(kademe='L1', olgu=True, cipa=False, not_="'eş-şemsu ve'l-qameru bi-husbân' — iki gök cismi + ölçü kelimesi ('husbân'); birim / süre / yörünge yok — L1; L4 ölçü kolu yalnız kelime düzeyinde, KAPATILAMAZ (54:49 emsali); tarayıcı vermedi"),
 6: dict(kademe='L1', olgu=True, cipa=False, not_="'ve'n-necmu ve'ş-şeceru yescudân' — gök cismi / bitki + davranış (secde); 'necm' iki okumalı — L1 (22:18 emsali); tarayıcı vermedi"),
 7: dict(kademe='L1', olgu=True, cipa=False, not_="'ve's-semâ'e rafe'ahâ' — gök + yükseltme; 'mîzân' ölçü aracı adı, birim yok — L1 (13:2 emsali); tarayıcı vermedi"),
 10: dict(kademe='L1', olgu=True, cipa=False, not_="'ve'l-arda veda'ahâ li'l-enâm' — yer + yararlanan; 'li-' işlev mi ta'lîl mi KAPATILAMAZ (L2 sınırı) — L1; tarayıcı vermedi"),
 # blok 11-20
 11: dict(kademe='L1', olgu=True, cipa=False, not_="'fâkihetun ve'n-nahlu zâtu'l-ekmâm' — bitki + nitelik (tomurcuk kabuğu); süreç yok — L1; tarayıcı vermedi"),
 12: dict(kademe='L1', olgu=True, cipa=False, not_="'el-habbu zu'l-asfi ve'r-reyhân' — bitki sınıfları + nitelik; sınıflama ölçütü / üye eşlemesi yok — L1; tarayıcı vermedi"),
 14: dict(kademe='L1', olgu=True, cipa=False, not_="'halaqa'l-insâne min salsâlin ke'l-fahhâr' — insan + madde + teşbihle nitelik; evre / mekanizma yok — L1 (15:26 emsali); tarayıcı vermedi"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="'halaqa'l-cânne min mâricin min nâr' — cânn gözlem dışı varlık; doğal olgu değil; tarayıcı vermedi"),
 17: dict(kademe='L1', olgu=True, cipa=False, not_="'rabbu'l-meşriqayni ve rabbu'l-mağribeyn' — doğu / batı noktaları ikil sayıyla; ne olduğu adlanmıyor — L1; ikilin göndergesi KAPATILAMAZ; tarayıcı vermedi"),
 19: dict(kademe='L1', olgu=True, cipa=False, not_="'meraca'l-bahrayni yeltaqiyân' — iki su kütlesi + buluşma; nitelik / mekanizma yok (25:53'te nitelik var) — L1 (27:61 emsali); tarayıcı vermedi"),
 20: dict(kademe='L1', olgu=True, cipa=False, not_="'beynehumâ berzahun lâ yebğiyân' — engel + taşmama ardışık, nedensellik edatı yok — L1; L2 sınırı KAPATILAMAZ; tarayıcı vermedi"),
 # blok 21-30
 22: dict(kademe='L1', olgu=True, cipa=False, not_="'yahrucu minhumâ'l-lu'lu'u ve'l-mercân' — deniz ürünleri adı + çıkış (süreç adı); oluşum / mekanizma yok — L1 (35:12 emsali); tarayıcı vermedi"),
 24: dict(kademe=None, olgu=False, cipa=False, not_="'el-cevâri'l-munşe'ât … ke'l-a'lâm' — gemi insan yapımı; doğal olgu değil (54:13 emsali); tarayıcı vermedi"),
 # blok 31-40
 33: dict(kademe='L2', olgu=True, cipa=False, not_="'in isteta'tum en tenfuzû min aqtâri's-semâvâti ve'l-ard … lâ tenfuzûne illâ bi-sultân' — YETİ SINIRI; göklerin ve yerin çevresi adlı, ölçü / mekanizma yok — L2 (27:60, 17:88 emsali); tarayıcı v4 adayı, çıpa değil"),
 37: dict(kademe='L1', olgu=True, cipa=False, not_="'inşaqqati's-semâ'u fe-kânet verdeten ke'd-dihân' — gök + hâl (yarılma) + renk teşbihi; gelecek sahne, süreç / ölçü yok — L1 (54:1 emsali); tarayıcı vermedi"),
 # blok 41-50
 48: dict(kademe=None, olgu=False, cipa=False, not_="'zevâtâ efnân' — cennet ağaçlarının dalları, âhiret; doğal olgu değil; tarayıcı vermedi"),
 50: dict(kademe=None, olgu=False, cipa=False, not_="'fîhimâ aynâni tecriyân' — cennet pınarları, âhiret; doğal olgu değil (54:54 emsali); tarayıcı vermedi"),
 # blok 51-60
 52: dict(kademe=None, olgu=False, cipa=False, not_="'min kulli fâkihetin zevcân' — cennet meyveleri, âhiret; doğal olgu değil (13:3 yeryüzü emsali ayrı); tarayıcı vermedi"),
 # blok 61-70
 66: dict(kademe=None, olgu=False, cipa=False, not_="'aynâni naddâhatân' — cennet pınarları, âhiret; doğal olgu değil; tarayıcı vermedi"),
 68: dict(kademe=None, olgu=False, cipa=False, not_="'fâkihetun ve nahlun ve rummân' — cennet ağaçları, âhiret; doğal olgu değil (55:11 yeryüzü L1 ayrı); tarayıcı vermedi"),
 # blok 71-78
 72: dict(kademe=None, olgu=False, cipa=False, not_="'hûrun maqsûrâtun fi'l-hiyâm' — cennet, âhiret; doğal olgu değil; tarayıcı vermedi"),
 74: dict(kademe=None, olgu=False, cipa=False, not_="'lem yatmishunne insun qablehum ve lâ cânn' — cennet, âhiret (55:56 ile aynı); doğal olgu değil; tarayıcı vermedi"),
 76: dict(kademe=None, olgu=False, cipa=False, not_="'refref', 'abqariyy' — cennet döşeği, âhiret; doğal olgu değil; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: 55:1 'rahmân' ölçüm satırında SON konum 'MÜHÜRSÜZ', bilanço esma_muhur_43_gecerli [1] — ayrışma (tek kelimelik ayette 'son konum' ile mühür ölçütü çakışıyor); el kararı ilâhî; mühür iddiası yazılmadı; lafız 0, Rab 0",
  "yıldız: 55:10 ★★★ hapaks 'enâm' (z=3,28); 9 ayet yıldızsız",
  'fâsıla: 55:1-9 ن, 55:10 م — N sınıfı, kafiye kırığı yok',
  'ham veri: kuran_veri 55:1 metninde sûre başı besmelesi ekli; blok_goster ve ölçüm ayıklıyor (n=1) — doğru; ilk ham basımda görüldü',
  "biçim (517 ailesi): 55:7 ve 55:10 meful takdimi ('ve's-semâ'e rafe'ahâ', 've'l-arda veda'ahâ') ölçümde işaretsiz; 55:8 'ellâ' ta'lîl / tefsîr iki okumalı",
  "iki okumalı (KAPATILAMAZ): 55:6 'en-necm' yıldız / gövdesiz bitki; meal 'yıldız'ı seçti",
  "lemma (1021 ailesi): 'husbân' 18:40 gökten yıkım / 55:5 hesap — aynı lemma iki anlam",
  "konuşan / gönderge (1017 ailesi): 55:8-9 muhatap 2MP adsız; 55:2 öğrenen yok, 55:4 'hu' insan",
  "aday 1040 alanı (sûre sınırı; kayıt, test yok): fâsıla 54:55 ر → 55:1 ن; 54:55 'melîk' + 'muqtedir' / 55:1 'er-rahmân'; 54:17, 22, 32, 40 'yessernâ'l-qur'ân' / 55:2 ''allema'l-qur'ân'; 54:1 'el-qamer' / 55:5 'el-qamer'; 54:49 'bi-qader' / 55:5 'bi-husbân', 55:7 'el-mîzân'; 53:1 've'n-necm' / 55:6 've'n-necm'",
  "okuma: 55:2-4 öğretti / yarattı / öğretti; 55:7 / 55:10 gök yükseltildi / yer konuldu (simetrik kuruluş); 55:7-9 'vezn / mîzân' üç ayette dört kez",
  "karşıt çift (aday 1039, okuma): ayet içi 55:5 şems / qamer, 55:6 necm / şecer, 55:7 rafe'a / vada'a, 55:9 eqîmû / lâ tuhsirû; ayetler arası 55:7 / 55:10 gök / yer — kayıt, test yok",
  'çıpa: 55:3 L0; 55:5, 6, 7, 10 L1 (55:5 ölçü yalnız kelime, 55:10 L2 sınırı KAPATILAMAZ); tarayıcı adayı yok',
  'okuma: 20:5, 54:55 → 55:1; 53:5, 54:17 → 55:2; 16:4, 21:37, 32:7, 54:49 → 55:3; 13:2, 39:5, 18:40, 54:1 → 55:5; 22:18, 16:49, 53:1 → 55:6; 13:2, 42:17, 21:47 → 55:7; 20:81, 53:17 → 55:8; 18:105, 11:85, 17:35, 26:182 → 55:9 — KAPATILAMAZ',
  "tetik: ön kuru koşu 8 tetik satırı (55:3 خلق أنس ◈B; 55:5 شمس قمر ◈K; 55:6 نجم ◈K, شجر ◈B; 55:7 سمو ◈K, وضع ◈B; 55:10 أرض ◈K, وضع ◈B) — kayıtta 0 uyuşmaz; [x/y] 0 (26 sayım); kayıttan önce 'allema' lemma sayısı 37 → 35 düzeltildi",
 ],
 (11, 20): [
  "esmâ: blokta e_oto tokeni yok; mühür ölçümü [] — karar gerekmedi; lafız 0, Rab 5 token / 4 ayet (55:13, 16, 17 ×2, 18) — sûrenin ilk Rab'bi 55:13",
  'yıldız: dört ★★★ rab (55:13, 16, 18 z=5,01; 55:17 z=10,34) — kısa nakarat ayetinde Rab formülü, bilinen davranış; hapaks, edilgen yok',
  'fâsıla: 55:11 م, 55:14-15 ر (R sınıfı), diğerleri ن; kafiye kırığı ölçümde yok',
  "gloss (1021 ailesi): 55:12 'habb' حبب 'sevgi', 'asf' عصف 'fırtına', 'reyhân' روح 'ruh; rüzgâr'; 55:14 'fahhâr' فخر 'övünme' — bu ayetlerdeki anlamı kapsamıyor; 55:15 'nâr' نور sayacında",
  "biçim (517 ailesi): 55:11 ve 55:20 takdim, 55:14 teşbih 'ke-' ölçümde işaretsiz; 55:17 mübteda hazfi",
  "konuşan / gönderge (1017 ailesi): nakarat muhatabı 2D adsız — meal 'ikiniz' dedi, adlandırmadı; 55:14-15 insan / cânn metinde adlı",
  "nakarat (sayım): 'fe-bi-eyyi âlâ'i rabbikumâ tukezzibân' tam kalıp 31 ayet, otuz biri de bu sûrede (55:13 … 55:77); blokta 3 geçiş (55:13, 16, 18); 'âlâ'' lemma 34 ayet — 53:55 tekil muhatapla",
  "aday 1040 alanı (kayıt): 54:20 'nahl' / 55:11 'nahl'; 54:12 'fe'ltaqa'l-mâ'' / 55:19 'yeltaqiyân'; 53:55 / 55:13 (ardışık değil)",
  "okuma: 15:26-27 insan / cânn sırası → 55:14-15 aynı sıra; 25:53 'meraca'l-bahrayn' + 'beynehumâ berzah' iki ayete (55:19-20) dağılıyor, su nitelikleri yok; 'meşriq' tekil (26:28) / çoğul (37:5) / ikil (43:38, 55:17)",
  "okuma: 55:17-20'de ikil yoğunluğu (meşriqayn, mağribeyn, bahrayn, yeltaqiyân, beynehumâ, yebğiyân); nakarat da 2D",
  'karşıt çift (aday 1039, okuma): ayet içi 55:17 meşriqayn / mağribeyn; ayetler arası 55:14 / 55:15 salsâl / nâr, 55:19 / 55:20 buluşma / taşmama — kayıt, test yok',
  'çıpa: 55:11, 12, 14, 17, 19, 20 L1 (55:20 L2 sınırı KAPATILAMAZ); 55:15 olgu değil (cânn); tarayıcı adayı yok',
  'okuma: 41:47, 36:57, 38:51, 43:73, 44:55, 52:22, 54:20 → 55:11; 53:55 → 55:13; 15:26, 55:3 → 55:14; 15:27 → 55:15; 26:28, 37:5, 43:38 → 55:17; 25:53, 27:61, 54:12 → 55:19; 25:53, 23:100 → 55:20 — KAPATILAMAZ',
  "tetik: ön kuru koşu 3 tetik satırı (55:14 خلق أنس ◈B; 55:15 خلق ◈B; 55:19 بحر ◈K) — kayıtta 0 uyuşmaz; [x/y] 0 (35 sayım); kayıttan önce okunmuş ama basılmamış ayet anmaları (42:42, 49:9; 36:33, 50:9) çıkarıldı, 'beğâ' lemma 25 → 24 düzeltildi; 'fâkihe' ayetleri basılıp adla anıldı",
 ],
 (21, 30): [
  "esmâ: blokta e_oto tokeni yok; 55:27 'zu'l-celâli ve'l-ikrâm' sıfat ifadesi esmâ ölçümünde yok — karar gerekmedi; lafız 0, Rab 6 (nakarat 5 + 55:27)",
  "yıldız: 7 ★★★ — rab 6 (nakarat 55:21, 23, 25, 28, 30 z=5,01; 55:27 z=3,23), hapaks 1 (55:26 'fân' z=3,28); hapaks 'fân' kok_ekle_55 ile eklenen kökten",
  'fâsıla: 55:24 ve 55:27 م, diğerleri ن — N sınıfı, kafiye kırığı yok',
  "gloss (1021 ailesi): 55:22 'mercân' مرج 'salıverme'; 55:24 'a'lâm' علم 'bilme' — bu anlamları kapsamıyor",
  "biçim (517 ailesi): 55:24 takdim 'lehû' ve teşbih 'ke-'; 55:29 ayırma zamiri 'huve'; 55:27 2D → 2MS sayı değişimi ölçümde iltifât sayılmıyor (iltifât 0)",
  "kalıp (924): 55:29 'men fi's-semâvâti ve'l-ard' harekesiz kalıpta 2 ayet — imlâ / 've men' biçim farkı ayırıyor; sayı iddiası yalnız kalıp düzeyinde",
  "konuşan / gönderge (1017 ailesi): nakarat 2D muhatap adsız; 55:27 2MS muhatap adsız; 55:26 'men', 55:29 'men' isteyenler adsız",
  'nakarat (sayım): blokta 5 geçiş (55:21, 23, 25, 28, 30); 55:13-30 arası toplam 8',
  "okuma: 28:88 'kullu şey'in hâlikun illâ vechehû' bir ayette → 55:26-27 iki ayette ('fân' / 'yebqâ vechu rabbik'); 53:51 'fe-mâ ebqâ' / 55:27 'yebqâ'; 42:32 'min âyâtihi'l-cevâr' / 55:24 'lehu'l-cevâr'; 30:26 'lehû men fi's-semâvât' / 55:29 'yes'eluhû men fi's-semâvât'",
  'okuma: 55:19-22 deniz dizisi (salıverme, buluşma, engel, inci ve mercan) + 55:24 gemiler',
  "karşıt çift (aday 1039, okuma): ayet içi 55:22 lu'lu' / mercân, 55:27 celâl / ikrâm, 55:29 semâvât / ard; ayetler arası 55:26 / 55:27 fân / yebqâ — kayıt, test yok",
  'çıpa: 55:22 L1; 55:24 olgu değil (gemi); tarayıcı adayı yok',
  'okuma: 35:12, 52:24 → 55:22; 42:32 → 55:24; 28:88 → 55:26; 53:51, 28:88 → 55:27; 30:26, 10:61 → 55:29 — KAPATILAMAZ',
  "tetik: ön kuru koşu 2 tetik satırı (55:24 بحر ◈K; 55:29 سمو أرض يوم ◈K) — kayıtta 0 uyuşmaz; [x/y] 0 (43 sayım); kayıttan önce 55:29 kalıp ifadesi ('yes'eluhû ile' — yanlış) düzeltildi",
 ],
 (31, 40): [
  'esmâ: blokta e_oto tokeni yok; mühür ölçümü [] — karar gerekmedi; lafız 0, Rab 5 (nakarat)',
  "yıldız: 8 ★★★ — rab 5 (nakarat 55:32, 34, 36, 38, 40), hapaks 2 (55:33 'nefeze' ×3, 55:35 'şuvâz'), pas 1 (55:39 z=5,38); 55:35'te pas z=2,52 de eşikte, kaynak hapaks seçildi",
  "edilgen: 55:35 'yursalu' (gönderen adsız), 55:39 'yus'elu' (soran adsız) — gerçek edilgen",
  'fâsıla: on ayetin hepsi ن; kafiye kırığı yok',
  "gloss / etiket (1021, 924): 55:31 'eyyuhâ' nidâ edatı أيي sayacında; 55:33 'ma'şer' عشر 'on' sayacında ve 'sayı işareti' etiketli — sayı değil; 55:37 'verde' ورد 'varma'; 55:35 'nâr' نور sayacında",
  "iki okumalı (KAPATILAMAZ): 55:35 'nuhâs' bakır / duman — meal 'bakır'",
  "konuşan / gönderge (1017): nakaratın 2D muhatabı 55:31 'es-seqalân' ve 55:33 'ma'şera'l-cinni ve'l-ins' ile metinde adlanıyor — meal adı metinden aldı; nakarat mealinde ad eklenmedi; 55:31 1P konuşan adsız",
  "biçim (517): 55:37 teşbih; 55:37 'izâ' şartının cevabı 55:39 — arada nakarat (55:38); şart-cevap bağı ölçümde işaretsiz",
  'tarayıcı v4: 55:33 aday (yeti sınırı) — okuma L2, çıpa değil',
  "okuma: 17:88 insan + cin yeti sınırı (Kur'ân'ın benzeri) → 55:33 cin + insan yeti sınırı (gök ve yerin çevresi); 33:14 'aqtâr' şehir / gök-yer; 21:23, 28:78 'lâ yus'elu' → 55:39; 55:29 'yes'eluhû' / 55:39 'lâ yus'elu'; 54:10 'fe'ntasir' / 55:35 'fe-lâ tentasirân'; 54:1 ay / 19:90 yer / 55:37 gök yarılıyor",
  "aday 1040 alanı (kayıt): 54:10 / 55:35 'intasara'; 54:1 / 55:37 'inşaqqa'",
  "karşıt çift (aday 1039, okuma): ayet içi 55:33 cinn / ins, semâvât / ard, fe'nfuzû / lâ tenfuzûne; 55:35 şuvâz / nuhâs; 55:39 ins / cânn — kayıt, test yok",
  'çıpa: 55:33 L2 (yeti sınırı), 55:37 L1; tarayıcı adayı 55:33 — kesinlik okuma kararında 0/1 (L4 değil)',
  'okuma: 55:33 (55:31); 17:88, 33:14 → 55:33; 54:10 → 55:35; 54:1, 19:90, 25:25 → 55:37; 21:23, 28:78, 55:29 → 55:39 — KAPATILAMAZ',
  "tetik: ön kuru koşu 5 tetik satırı (55:33 سمو أرض ◈K, أنس ◈B; 55:37 سمو ◈K; 55:39 يوم ◈K, أنس ◈B) — kayıtta 0 uyuşmaz; [x/y] 0 (46 sayım); kayıttan önce 'istetâ'a' lemma 42 → 41 düzeltildi",
 ],
 (41, 50): [
  'esmâ: blokta e_oto tokeni yok; mühür ölçümü [] — karar gerekmedi; lafız 0, Rab 5 (nakarat 4 + 55:46)',
  "yıldız: 7 ★★★ — rab 5 (nakarat 55:42, 45, 47, 49; 55:46 z=3,94), pas 1 (55:41 EDİLGEN 2/2 z=5,38), hapaks 1 (55:48 'efnân')",
  'fâsıla: 55:41 م, diğerleri ن — kafiye kırığı yok',
  "gloss (1021): 55:44 'ân' (kızgın) أني 'vakit, ân' sayacında; lemma 'el-âne' (şimdi) ile karışıyor",
  "etiket (924): 55:43 'cehennem' aktör 'rol fail' — metinde mübteda-haber; 55:50 'tecriyân' ölçümde 2D / 3FD ikircikli",
  'biçim (517): 55:43 alıntı mı anlatı mı işaretsiz (söyleyen adsız); 55:46 ve 55:50 takdim',
  "konuşan / gönderge (1017): 55:41 tanıyan ve yakalayan adsız (edilgen); 55:43 söyleyen adsız; 55:46 korkan 'men' adsız",
  'sahne (okuma): 55:41-44 suçlular ve cehennem → 55:46-50 iki cennet; ikil yoğunluğu (cennetân, zevâtâ, aynâni, tecriyân)',
  "okuma: 47:30 'bi-sîmâhum' 2MS tanır / 55:41 edilgen 'yu'rafu'; 36:63, 52:14 'hâzihî … elletî' → 55:43; 52:24 'yetûfu' cennette / 55:44 cehennemde; 14:14 'li-men hâfe maqâmî' → 55:46; 34:15-16 ve 18:32 dünya bahçeleri ikil → 55:46, 48; 54:12 'uyûn' → 55:50",
  "aday 1040 alanı (kayıt): 54:12 'uyûnen' / 55:50 'aynâni'",
  'karşıt çift (aday 1039, okuma): ayet içi 55:41 nevâsî / aqdâm; ayetler arası 55:43-44 cehennem / 55:46 cennetân — kayıt, test yok',
  'çıpa: 55:48, 55:50 olgu değil (cennet); blokta kademe yok; tarayıcı adayı yok',
  'okuma: 47:30, 11:56 → 55:41; 36:63, 52:14 → 55:43; 52:24 → 55:44; 14:14, 34:15, 18:32 → 55:46; 34:16 → 55:48; 54:12 → 55:50 — KAPATILAMAZ',
  "tetik: ön kuru koşu 1 tetik satırı (55:50 عين ◈B) — kayıtta 0 uyuşmaz; [x/y] 0 (35 sayım); kayıttan önce 'hamîm' lemma 20 → 19 düzeltildi ve basılmamış 40:72'yi kapsayan '40:71-72' aralığı çıkarıldı",
 ],
 (51, 60): [
  'esmâ: blokta e_oto tokeni yok; mühür ölçümü [] — karar gerekmedi; lafız 0, Rab 5 (nakarat)',
  'yıldız: 5 ★★★ rab (nakarat 55:51, 53, 55, 57, 59); hapaks, edilgen yok',
  'fâsıla: on ayetin hepsi ن; kafiye kırığı yok',
  "gloss / etiket (1021, 924): مرج [4/4] sayacı 'mârij', 'meraca', 'mercân' üç anlamı topluyor; 55:52 'zevcân' 'sayı işareti' etiketli — ikil isim",
  "biçim (517): 55:58 teşbih 'ke-enne'; 55:52, 56 takdim",
  "gönderge (okuma, KAPATILAMAZ): 55:56 'fîhinne' çoğul — 55:46-54 ikil 'fîhimâ / el-cenneteyn' sonrası; iki cennet mi döşekler mi",
  "konuşan / gönderge (1017): 55:54 yaslananlar, 55:56 'qâsirâtu't-tarf' ve 'qablehum' adsız; meal 'kadınlar' dedi (dilbilgisel cinsiyet), ad eklemedi",
  "kalıp (sayım): 'qâsirâtu't-tarf' 3 ayet (37:48, 38:52, 55:56); 'ke-ennehunne' 2 ayet (37:49, 55:58) — 37:48-49 dizisi burada 55:56, 58'de, arada nakarat; 'lem yatmishunne' 2 ayet (55:56, 74)",
  "okuma: 13:3, 51:49 'min kull … zevceyn' → 55:52; 18:31, 44:53 'istebraq' giysi / 55:54 döşek astarı; 34:33 'hel yuczevne illâ' → 55:60 'hel cezâ'u'l-ihsâni ille'l-ihsân'; 54:35 'neczî men şeker' / 55:60",
  'karşıt çift (aday 1039, okuma): ayet içi 55:56 ins / cânn, 55:58 yâqût / mercân — kayıt, test yok',
  'çıpa: 55:52 olgu değil (cennet); blokta kademe yok; tarayıcı adayı yok',
  'okuma: 13:3, 51:49 → 55:52; 18:31, 38:51, 44:53, 19:25 → 55:54; 37:48, 38:52 → 55:56; 37:49, 55:22 → 55:58; 34:33, 54:35 → 55:60 — KAPATILAMAZ',
  'tetik: ön kuru koşu 2 tetik satırı (55:52 زوج ◈B; 55:56 أنس ◈B) — kayıtta 0 uyuşmaz; [x/y] 0 (38 sayım)',
 ],
 (61, 70): [
  'esmâ: blokta e_oto tokeni yok; mühür ölçümü [] — karar gerekmedi; lafız 0, Rab 5 (nakarat)',
  "yıldız: 7 ★★★ — rab 5 (nakarat 55:61, 63, 65, 67, 69), hapaks 2 (55:64 'mudhâmmetân', 55:66 'naddâhatân'); ikisi de kok_ekle_55 kökü",
  'fâsıla: on ayetin hepsi ن; kafiye kırığı yok',
  "gloss / lemma (1021): 55:70 'hayrât' lemması 'el-hayrât' (iyilikler) ile aynı sayaçta",
  'biçim (517): 55:62, 66, 68, 70 takdim; 55:64 mübteda hazfi',
  "iki okumalı (KAPATILAMAZ): 55:62 'min dûnihimâ' derece / mekân",
  "konuşan / gönderge (1017): nakarat 2D muhatap adsız; 55:70 kadınlar adsız — meal dilbilgisel cinsiyetle 'kadınlar' dedi",
  "okuma (paralel dizi): 55:46 / 62 cennetân; 48 / 64 dal / renk; 50 / 66 akan / fışkıran pınar; 52 / 68 meyve çiftleri / adlı meyveler; 56 / 70 'fîhinne' — ikinci dizinin kalanı 55:72-76 henüz okunmadı",
  "okuma: 55:11 'fîhâ fâkihetun ve'n-nahl' yeryüzü / 55:68 'fîhimâ fâkihetun ve nahl' cennet; 55:1 ve 55:64 sûrenin iki tek kelimelik ayeti",
  'karşıt çift (aday 1039, okuma): ayetler arası 55:46 / 62 iki çift cennet, 55:50 / 66 akan / fışkıran, 55:11 / 68 yer / cennet — kayıt, test yok',
  'çıpa: 55:66, 68 olgu değil (cennet); blokta kademe yok; tarayıcı adayı yok',
  'okuma: 55:46 → 55:62; 55:48 → 55:64; 55:50 → 55:66; 55:11, 55:52 → 55:68; 55:56, 55:60 → 55:70 — KAPATILAMAZ',
  'tetik: ön kuru koşu 1 tetik satırı (55:66 عين ◈B) — kayıtta 0 uyuşmaz; [x/y] 0 (30 sayım); kayıttan önce hayrât okunmuş sayısı 5 → 6 düzeltildi',
 ],
 (71, 78): [
  'esmâ: blokta e_oto tokeni yok; mühür ölçümü [] — karar gerekmedi; lafız 0, Rab 5 (nakarat 4 + 55:78)',
  "yıldız: 7 ★★★ — rab 5 (55:71, 73, 75, 77, 78), hapaks 2 (55:72 'hiyâm'; 55:76 'refref' + 'abqariyy', z=6,79); üç kök de kok_ekle_55 kökü; 55:74 yıldız yok",
  'fâsıla: 55:72 ve 55:78 م, diğerleri ن; ölçüm N sınıfı, kafiye kırığı yok',
  "biçim (517): 55:78 2MS 'rabbike' — 2D'den sayı değişimi, ölçüm iltifât 0 (55:27 ile aynı)",
  "iki okumalı (KAPATILAMAZ): 55:72 mübteda hazfi / 'fîhinne'ye haber; 55:74 'qablehum' göndergesi",
  "lemma (1021): 55:78 سمو kök sayacı 'ism' ile 'semâ'yı topluyor; 55:72 'maqsûrât' edilgen ortaç, ölçüm edilgen fiil saymıyor",
  'çıpa: 55:72, 74, 76 olgu=False (cennet); 55:78 çıpasız',
  'tetik: ön kuru koşu 1 tetik satırı (55:74 أنس ◈B) — kayıtta 0 uyuşmaz; [x/y] 0 (33 sayım)',
 ],
}

DUZELTME = {
}
