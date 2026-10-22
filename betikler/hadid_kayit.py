# -*- coding: utf-8 -*-
"""hadid_kayit.py — sûre 57 (Hadîd) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 57

CIPA = {
 # blok 1-6
 1: dict(kademe='L0', olgu=True, cipa=False, not_="'sebbaha lillâhi mâ fi's-semâvâti ve'l-ard' — gökler ve yer tesbih edenlerin yeri olarak adlanıyor; süreç / ölçü yok — L0; tarayıcı vermedi"),
 2: dict(kademe='L0', olgu=True, cipa=False, not_="'lehû mulku's-semâvâti ve'l-ard, yuhyî ve yumît' — gökler ve yer mülk, dirim / ölüm adlanıyor; süreç / mekanizma yok — L0 (39:44 emsali); tarayıcı vermedi"),
 4: dict(kademe='L1', olgu=True, cipa=False, not_="'fî sitteti eyyâmin summe'stevâ' — sayı + birim (gün) ve sıra; süreç / mekanizma yok, 'gün' ölçü birimi mi dönem mi KAPATILAMAZ — L4 ölçü koluna sınırda, L1 (50:38 emsali); yere giren / çıkan, gökten inen / yükselen dört süreç + yön (34:2 emsali L1); tarayıcı vermedi"),
 5: dict(kademe='L0', olgu=True, cipa=False, not_="'lehû mulku's-semâvâti ve'l-ard' — gökler ve yer yalnız mülk olarak; süreç / ölçü yok — L0 (39:44 emsali); tarayıcı vermedi"),
 6: dict(kademe='L1', olgu=True, cipa=False, not_="'yûlicu'l-leyle fi'n-nehâr …' — gece-gündüz karşılıklı geçiş, süreç adlı, mekanizma / ölçü yok — L1 (35:13 emsali); tarayıcı vermedi"),
 # blok 7-10
 9: dict(kademe=None, olgu=False, cipa=False, not_="'mine'z-zulumâti ile'n-nûr' — karanlıktan ışığa çıkarma mecaz (hidayet), doğal olgu değil; merdiven uygulanmadı (33:43 emsali); tarayıcı v4 adayı, çıpa değil"),
 10: dict(kademe='L0', olgu=True, cipa=False, not_="'lillâhi mîrâsu's-semâvâti ve'l-ard' — gökler ve yer yalnız miras olarak adlanıyor; süreç / ölçü yok — L0 (57:5 emsali); tarayıcı vermedi"),
 # blok 11-15
 12: dict(kademe=None, olgu=False, cipa=False, not_="'cennâtun tecrî min tahtihe'l-enhâr' — cennet, âhiret; doğal olgu değil; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'bi-sûrin lehû bâb, bâtınuhû … zâhiruhû' — âhiret sahnesi, sur ve kapı; doğal olgu değil; tarayıcı v4 adayı (iç / dış), çıpa değil"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="'me'vâkumu'n-nâr' — cehennem, âhiret; doğal olgu değil; tarayıcı vermedi"),
 # blok 16-19
 17: dict(kademe='L1', olgu=True, cipa=False, not_="'yuhyi'l-arda ba'de mevtihâ' — ölü yerin diriltilmesi süreç olarak adlı; sebep (su / rızık), ara durum, mekanizma bu ayette yok — L1 (35:9, 45:5, 41:39 L2 nedenselliği yok); tarayıcı v4 adayı, çıpa değil"),
 19: dict(kademe=None, olgu=False, cipa=False, not_="'ashâbu'l-cahîm' — cehennem, âhiret; doğal olgu değil; tarayıcı vermedi"),
 # blok 20-22
 20: dict(kademe='L4', olgu=True, cipa=False, not_="MEKANİZMA kolu adayı: yağmur → beğenilen bitki → kabarıp kuruma ('yehîcu') → sararma ('musfarr') → çer çöp ('hutâm'); dört aşama 'summe / fe / summe' ile ardışık, ara durumlar adlı — 39:21 emsali (L4; aynı 'yehîcu fe-terâhu musfarran summe … hutâmâ' dizisi), suyun yolu ve renk ayrımı burada yok; ANCAK teşbih içinde ('ke-meseli ğays', dünya hayatı meseli): olgu benzetme aracı, iddia değil — L4 adayı, TARTIŞMALI (48:29 ile aynı statü; cipa kararı açık, okuyucu onayı bekler); tarayıcı v4 adayı — kısmi isabet"),
 21: dict(kademe=None, olgu=False, cipa=False, not_="'cennetin arduhâ ke-ardi's-semâ'i ve'l-ard' — cennet, âhiret; gök ve yer ölçü benzetmesi (birim yok); doğal olgu değil; tarayıcı vermedi"),
 # blok 23-26
 25: dict(kademe='L1', olgu=True, cipa=False, not_="'enzelne'l-hadîde fîhi be'sun şedîdun ve menâfi'u li'n-nâs' — demir (madde) + iki nitelik (çetin güç, yararlar); süreç / mekanizma / ölçü yok — L1 (34:10 emsali); 'enzelnâ' köken iddiası kelime düzeyinde, KAPATILAMAZ; tarayıcı vermedi"),
}

ARIZA = {
 (1, 6): [
  "esmâ: e_oto 10 token (57:1×2, 57:2, 57:3×5, 57:4, 57:6), okuyucu kararı 10'unda İLÂHÎ — 57:3 'evvel / âhir' 56:13:3 / 56:14:3 DEĞİL kararlarının karşıtı (gönderge 57:1 lafız); KARAR 483 → 493; bilanço geçerli mühür 57:1, 2, 3, 4, 6",
  "esmâ ayrışması: ölçüm satırı 57:2 'qadîr', 57:4 'basîr', 57:6 'alîm' için 'MÜHÜRSÜZ', bilanço geçerli mühür (51:58 emsali) — mühür iddiası yalnız bilançodan; 57:3 ölçüm esmâ alanında 'evvel' yok, esma_kayit e_oto sayıyor (aday 1022; 46:17 emsali)",
  "yıldız: 57:2 ve 57:3 ★ kaynağı kafiye kırığı, bilanço 'allah' etiketli z=-0,53 (aday 1001); 57:1 ★ allah z=1,69; 57:4 ★★ n z=2,50 (uzun ayet, 48:29 emsali); 57:5 ★★★ pas z=5,38 (kısa tek fiilli edilgen, 53:36 emsali; allah z=1,97 de eşikte)",
  "fâsıla: 57:1 م, 57:2 ر, 57:3 م, 57:4-6 ر — ölçüm 57:2 ve 57:3'ü kafiye kırığı işaretliyor, 57:4'ü (م → ر) işaretlemiyor; aracın kuralı KAPATILAMAZ (924)",
  "gloss (1021 ailesi): أخر 'geciktirme' — 57:3 'âhir' (son) anlamını kapsamıyor; نهر 'ırmak' — 57:6 'nehâr' (gündüz) anlamını kapsamıyor",
  "biçim (517 ailesi): 57:2 ve 57:5 takdim ('lehû', 'ile'llâhi') ölçüm biçim alanında yok; 57:4 ayet içi 3MS → 2MP geçişi iltifât 0 (alan ayetler arası geçişi sayıyor)",
  "konuşan / gönderge (1017 ailesi): 57:1-6 'huve' / 'lehû' göndergesi 57:1, 4, 5 lafız; 57:4 muhatap 2MP adsız; 57:1 tesbih eden 'mâ' adsız; 57:5 döndüren adsız (edilgen)",
  "aday 1040 alanı (sûre sınırı; kayıt, test yok): 56:96 'fe-sebbih bi'smi rabbike'l-azîm' 2MS emir + Rab / 57:1 'sebbaha lillâh' PERF + lafız — fâsıla م → م; 56:13-14 'el-evvelîn / el-âhirîn' / 57:3 'el-evvel / el-âhir'",
  "aday 1041 alanı (kayıt, test yok): 'evvel', 'âhir' lemmaları 56:13, 56:14 insanlar için / 57:3 Allah için",
  "okuma (sûre içi): 57:2 / 57:5 aynı ilk yarı (nakarat3 GEÇER); ولج 57:4 I. bab / 57:6 IV. bab; علم 57:3 'alîm', 57:4 'ya'lemu', 57:6 'alîm'",
  "karşıt çift (aday 1039, okuma): 57:2 yuhyî / yumît; 57:3 evvel / âhir, zâhir / bâtın; 57:4 yelicu / yahrucu, yenzilu / ya'rucu; 57:6 leyl / nehâr; 57:1, 2, 4, 5 gökler / yer — kayıt, test yok",
  "çıpa: 57:1, 2, 5 L0; 57:4, 6 L1 (50:38, 34:2, 35:13 emsali); 57:3 değerlendirilmedi; L4 yok; tarayıcı adayı yok",
  "okuma: 56:96, 17:44, 24:41 → 57:1; 9:116, 10:56, 30:50 → 57:2; 30:7, 31:20, 56:13, 56:14 → 57:3; 10:3, 13:2, 20:5, 25:59, 32:4, 11:7, 50:38, 34:2 → 57:4; 25:2, 39:44, 24:42, 22:76, 35:4 → 57:5; 22:61, 31:29, 35:13, 31:23 → 57:6 — KAPATILAMAZ",
  "tetik: ön kuru koşu 7 tetik satırı (57:1 K, 57:2 K+B, 57:4 K+B, 57:5 K, 57:6 K) — kayıtta 0 uyuşmaz; [x/y] 0 (48 sayım); kayıttan önce 57:6 'alîm' konumu ölçüm satırına göre düzeltildi ('son konum'), 57:6 emsal lafız sırası yeniden yazıldı",
 ],
 (7, 10): [
  "esmâ: e_oto 6 token (57:7, 57:8, 57:9×3, 57:10); okuyucu kararı DEĞİL 3 (57:7 'kebîr' ecrin sıfatı — 35:7:13; 57:8 'mu'minîn' insanlar — 37:29:5; 57:9 'nûr' ışık — 35:20:4), İLÂHÎ 3 (57:9 'ra'ûf', 'rahîm'; 57:10 'habîr'); KARAR 493 → 499; mühür ölçümü 57:7-10, geçerli mühür 57:9, 10",
  "tarayıcı v4 adayı 57:9 (karanlık / ışık) — mecaz, doğal olgu değil; isabet 0/1 (aday 1014 kesinlik)",
  "yıldız: 57:10 ★★ kaynağı n z=2,61 (uzun ayet; allah z=1,63 de eşikte) — formül; öteki üç ayet yıldızsız",
  "fâsıla: 57:7 ر, 57:8 ن, 57:9 م, 57:10 ر — ölçüm yalnız 57:10'u kafiye kırığı işaretliyor; 57:4'te aynı م → ر geçişi işaretlenmemişti, 57:8 ر → ن de işaretlenmedi — aracın kuralı KAPATILAMAZ (924)",
  "biçim (517 ailesi): 57:6 → 57:7 3MS anlatıdan 2MP emre geçiş iltifât 0 (bilanço iltifât boş); 57:10 ölçüm satırı 'biçim' alanını boş basıyor; 57:10 'kullen' takdimi ölçümde yok",
  "harekesiz kalıp (924): 57:7 IMPV 'âminû' ile 24:62, 49:15 PERF 'âmenû' aynı kalıba düşüyor — kip ayrımı okumayla; 'ecr + kebîr' tam kalıpta 1, önek toleranslı 4",
  "konuşan / gönderge (1017 ailesi): 57:8 'ehaze mîsâqakum' fâili (er-rasûl / Allah) KAPATILAMAZ, meal 'O' dedi; 57:9 'abdihî' adsız; 57:10 'el-feth' hangi olay — metinde adlanmıyor, meal adlandırmadı; harcayıp savaşanlar adsız",
  "okuma (sûre içi): 57:4 'yenzilu / yahrucu' (I. bab) → 57:9 'yunezzilu / yuhricakum' (II. / IV. bab); 57:4 'istevâ' / 57:10 'lâ yestevî'; 57:2, 5 'mulk' / 57:10 'mîrâs'; 57:4 'basîr' / 57:10 'habîr' aynı kuruluş; 57:8 / 57:10 've mâ lekum' + NEG",
  "karşıt çift (aday 1039, okuma): 57:8 lâ tu'minûn / li-tu'minû; 57:9 zulumât / nûr; 57:10 qabl / ba'd, gökler / yer — kayıt, test yok",
  "çıpa: 57:10 L0; 57:9 olgu değil (mecaz); 57:7, 8 değerlendirilmedi; L4 yok",
  "okuma: 24:62, 49:15, 35:7 → 57:7; 9:116, 29:22, 45:34, 42:47, 13:20, 33:7 → 57:8; 25:1, 18:1, 33:43, 14:1, 14:5, 16:7, 16:47, 22:65, 24:20 → 57:9; 32:28, 48:1, 9:20, 10:26 → 57:10 — KAPATILAMAZ",
  "tetik: ön kuru koşu 1 tetik satırı (57:10 K) — kayıtta 0 uyuşmaz; [x/y] 0 (45 sayım); kayıttan önce basılmamış okunmuş ayet adları sayıya çevrildi (11:11, 13:25), 've mâ lekum' okunmuş sayısı 2 → 3 düzeltildi, 57:10 fâsıla geçişi ölçüme göre yeniden yazıldı ('ر → ر' yanlıştı)",
 ],
 (11, 15): [
  "esmâ: e_oto 8 token (57:11, 57:12×2, 57:13×4, 57:15); okuyucu kararı 8'inde DEĞİL ('kerîm' ecir; 'mu'minîn' insanlar; 'nûr' ×3 ışık; 'bâtın', 'zâhir' surun yüzleri; 'mevlâ' ateş); KARAR 499 → 507; mühür ölçümü 57:11, 13, 15, geçerli mühür 0",
  "aday 1041 alanı (kayıt, test yok): 'zâhir', 'bâtın' 57:3 Allah için (İLÂHÎ) / 57:13 surun dış ve iç yüzü (DEĞİL) — aynı sûrede, sıra ters; 'mevlâ' 47:11 Allah için / 57:15 ateş için",
  "tarayıcı v4 adayı 57:13 (sur, kapı, iç / dış) — âhiret sahnesi, olgu değil; isabet 0/1 (aday 1014 kesinlik)",
  "yıldız: 57:13 ★ n z=1,55; 57:15 ★ pas z=1,57 (EDİLGEN 1/3); öteki üç ayet yıldızsız",
  "fâsıla: 57:11-12 م, 57:13 ب, 57:14-15 ر — ölçüm hiçbirini kafiye kırığı işaretlemiyor (57:12 م → 57:13 ب ve ب → ر sınıf geçişi; 57:10 م → ر işaretlenmişti) — aracın kuralı KAPATILAMAZ (924)",
  "biçim (517 ailesi): 57:12 ayet içi 2MS → 3MP → 2MP iltifât 0; 57:12 'buşrâkum' öncesi söyleme fiili yok, alıntı sınırı ölçümde yok; 57:15 zemm 'bi'se' ölçüm kip alanında yok",
  "harekesiz kalıp (924): 'el-munâfiqûne ve'l-munâfiqât' merfû 2 ayet, mansub / mecrur biçim (9:68, 33:73, 48:6) kalıptan düşüyor — sayım lemmadan",
  "konuşan / gönderge (1017 ailesi): 57:12 'terâ' 2MS ve 'buşrâkum'u söyleyen adsız; 57:13 'qîle' söyleyen ve 'duribe' çeken adsız (edilgen); 57:14 'qâlû' fâili adsız; 'el-ğarûr' adsız, meal 'o aldatıcı'; 57:15 konuşan (57:14 devamı mı) KAPATILAMAZ; 57:13 'bâtınuhû / zâhiruhû' göndergesi (sur / kapı) KAPATILAMAZ; 'verâ'akum' mekân mı KAPATILAMAZ",
  "okuma (sûre içi): 57:12 / 57:13 eril + dişil çift (mu'minîn / munâfiqûn); نور 57:9 → 57:12 → 57:13 ×2; يوم 57:12 ×2, 57:13, 57:15 — müjde / fidye yok; 57:7 'ecrun kebîr' / 57:11 'ecrun kerîm'",
  "karşıt çift (aday 1039, okuma): 57:12 mu'minîn / mu'minât; 57:12 / 57:13 inananlar / münafıklar; 57:13 bâtın / zâhir, rahme / azâb; 57:14 e-lem nekun ma'akum / belâ ve lâkin; 57:12 / 57:15 bugün müjde / bugün fidye yok — kayıt, test yok",
  "çıpa: 57:12, 13, 15 olgu değil (cennet, âhiret sahnesi, cehennem); 57:11, 14 değerlendirilmedi; L4 yok",
  "okuma: 25:69, 33:30, 57:7 → 57:11; 9:72, 9:89, 10:64, 33:73 → 57:12; 9:67, 9:68, 9:73, 33:73, 48:6, 20:10, 27:7, 57:3 → 57:13; 9:52, 22:52, 40:78, 31:33, 35:5 → 57:14; 29:25, 45:34, 47:11, 9:73, 22:72 → 57:15 — KAPATILAMAZ",
  "tetik: ön kuru koşu 4 tetik satırı (57:12 K+B, 57:13 K, 57:15 K) — kayıtta 0 uyuşmaz; [x/y] 0 (62 sayım); kayıttan önce 'munâfiq' ve 'yudâ'ifu' okunmuş sayıları liste ile yeniden sayıldı, kök قبس sayımı koşuldu (3 ayet)",
 ],
 (16, 19): [
  "esmâ: e_oto 3 token (57:18, 57:19×2); okuyucu kararı 3'ünde DEĞİL ('kerîm' ecir; 'şuhedâ'' insanlar; 'nûr' ışık); KARAR 507 → 510; mühür ölçümü 57:18, geçerli mühür 0",
  "tarayıcı v4 adayı 57:17 (yer, ölüm, diriltme) — L1, çıpa değil; isabet 0/1 (aday 1014 kesinlik)",
  "yıldız: 57:16 ★ n z=1,65; 57:18 ★★ pas z=2,52 (EDİLGEN 1/2, kısa ayet) — formül; 57:17, 19 yıldızsız",
  "harekesiz kalıp (924): 30:50 'ba'de mevtihâ' elif-medde imlâsıyla 'yuhyi'l-arda ba'de mevtihâ' kalıbından düşüyor (kalıp 2 ayet, okumayla 3); 'mussaddiq' (idgamlı) ve 'mutesaddiq' morph'ta ayrı lemma",
  "biçim (517 ailesi): 57:17 lafız 3MS → 'beyyennâ' 1P ve 57:19 'rabbihim' → 'âyâtinâ' 1P ayet içi geçişleri iltifât 0; 57:18 'inne', 57:19 hasr ('humu's-sıddîqûn') ölçüm kip alanında yok",
  "iki okumalı (KAPATILAMAZ): 57:19 've'ş-şuhedâ'' atıf ('es-sıddîqûn ve'ş-şuhedâ'') / yeni mübteda — meal ikincisini seçti",
  "konuşan / gönderge (1017 ailesi): 57:16 'ellezîne ûtû'l-kitâbe min qabl' adsız (meal adlandırmadı), veren adsız (edilgen); 57:18 katlayan adsız (edilgen)",
  "okuma (sûre içi): eril + dişil çift 57:12, 13, 18; 57:11 / 57:18 karz kalıbı etken → edilgen; 57:7 'rasûlihî' / 57:19 'rusulihî'; 57:2 / 57:17 ihyâ — nesne adsız / yer; 57:4 'mâ yenzilu mine's-semâ'' / 57:16 'mâ nezele mine'l-haqq'; 57:16 kalplerin katılaşması → 57:17 ölü yerin diriltilmesi (41:39 'hâşi'a' yer)",
  "karşıt çift (aday 1039, okuma): 57:16 tahşa'a / qaset; 57:17 yuhyî / mevt; 57:16 / 57:17 katı kalp / diriltilen yer; 57:18 eril / dişil; 57:19 âmenû / keferû, ecr ve nûr / ashâbu'l-cahîm — kayıt, test yok",
  "çıpa: 57:17 L1; 57:19 olgu değil (cehennem); 57:16, 18 değerlendirilmedi; L4 yok",
  "okuma: 13:28, 39:22, 39:23, 22:53, 20:108, 41:39, 18:12, 57:4 → 57:16; 9:123, 30:19, 30:50, 35:9, 45:5, 41:39, 57:2 → 57:17; 33:35, 12:88, 57:11 → 57:18; 57:7, 19:41, 19:56, 22:51 → 57:19 — KAPATILAMAZ",
  "tetik: ön kuru koşu 3 tetik satırı (57:16 B, 57:17 K+B) — kayıtta 0 uyuşmaz; [x/y] 0 (47 sayım); kayıttan önce 30:50'nin kalıptan düşüşü morph metniyle doğrulandı, kök قسو sayımı koşuldu (6 ayet)",
 ],
 (20, 22): [
  "ÇIPA KARARI AÇIK (kullanıcı): 57:20 mesel içi bitki süreci — 39:21 L4 dizisinin ('yehîcu fe-terâhu musfarran summe … hutâmâ') teşbih içindeki tekrarı; 48:29 ile birlikte teşbih içi L4 adayı ikinci vaka; cipa=False kaydedildi, karar kullanıcıda",
  "esmâ: e_oto 1 token (57:20 'âhir' — âhiret), okuyucu kararı DEĞİL; KARAR 510 → 511; mühür ölçümü yok, geçerli mühür 0; 57:21, 22 esmâ yok",
  "aday 1041 alanı (kayıt, test yok): 'âhir' lemması 57:3 Allah için (İLÂHÎ) / 57:20 âhiret için (DEĞİL), aynı sûrede",
  "tarayıcı v4 adayı 57:20 — L4 adayı teşbih içinde, kısmi isabet (48:29 emsali; aday 1014)",
  "yıldız: 57:20 ★★ n z=2,82 (uzun ayet; kafiye kırığı da işaretli); 57:21 ★ allah z=1,87 (kafiye kırığı da işaretli); 57:22 yıldızsız",
  "fâsıla: 57:19 م → 57:20 ر → 57:21 م → 57:22 ر — ölçüm 57:20 ve 57:21'i kafiye kırığı işaretliyor, 57:22'yi işaretlemiyor (57:21 م → 57:22 ر aynı tür geçiş) — aracın kuralı KAPATILAMAZ (924)",
  "iki okumalı (KAPATILAMAZ): 57:20 'el-kuffâr' inkârcılar / (tohumu örten) ekinciler — meal kelimeyi korudu; gloss كفر 'örtme' anlamını kapsamıyor (1021); 57:22 'nebre'ehâ' göndergesi (musîbe / yer / nefisler)",
  "biçim (517 ailesi): 57:22 2MP → 1P → lafız 3MS geçişi iltifât 0; 57:21 teşbih 'ke-' ölçümde yok",
  "konuşan / gönderge (1017 ailesi): 57:20 'terâhu' gören 2MS adsız; 57:21 'u'iddet' hazırlayan adsız (edilgen)",
  "okuma (sûre içi): غرر 57:14 aldatan / 57:20 aldanış; 57:19 / 57:21 'âmenû bi'llâhi ve rusulih'; 57:20 'mağfiratun mine'llâh' / 57:21 'mağfiratin min rabbikum'; 57:16 kalp katılığı → 57:17 yerin diriltilmesi → 57:20 bitkinin kuruyuşu (dirim / çöküş dizisi; okuma)",
  "karşıt çift (aday 1039, okuma): 57:20 dunyâ / âhira, azâb / mağfira ve ridvân, beğenilen bitki / hutâm; 57:20 metâ'u'l-ğurûr / 57:21 gök ve yer genişliğinde cennet; 57:22 yer / canlar — kayıt, test yok",
  "çıpa: 57:20 L4 adayı (teşbih, TARTIŞMALI); 57:21 olgu değil (cennet); 57:22 değerlendirilmedi; L4 kesin yok",
  "okuma: 47:36, 29:64, 39:21, 30:51, 56:65, 18:45, 10:24, 42:28, 48:29, 40:39 → 57:20; 57:19, 57:20, 56:10 → 57:21; 42:30, 35:11, 22:70, 29:19 → 57:22 — KAPATILAMAZ",
  "tetik: ön kuru koşu 3 tetik satırı (57:20 B, 57:21 K, 57:22 K) — kayıtta 0 uyuşmaz; [x/y] 0 (52 sayım); kayıttan önce okunmuş ama basılmamış xref ayetinin (sûre 9) adı sayıya çevrildi, 56:10 metni basıldı, 57:20 âhiret cümlesinin kalıp sayımı iki parça olarak yeniden yazıldı",
 ],
 (23, 26): [
  "esmâ: e_oto 4 token (57:24 'ğaniyy', 'hamîd'; 57:25 'qaviyy', 'azîz'), okuyucu kararı 4'ünde İLÂHÎ (lafzın haberi); KARAR 511 → 515; geçerli mühür 57:24, 25 (ölçüm ÇİFT ikisinde de)",
  "aktör: sûrede ilk adlı kişiler 57:26 Nûh, İbrâhîm (ölçüm aktör alanı 57:1-25'te boş)",
  "yıldız: 57:25 ★ n z=1,65 (formül); 57:23, 24, 26 yıldızsız",
  "fâsıla: 57:23 ر, 57:24 د, 57:25 ز, 57:26 ن — dört ayette dört ayrı harf; ölçüm hiçbirini kafiye kırığı işaretlemiyor (57:20-21 sınıf geçişleri işaretlenmişti) — aracın kuralı KAPATILAMAZ (924)",
  "gloss (1021 ailesi): حدد 'demir; sınır koyma' 50:22 'hadîd' (keskin görüş) anlamını kapsamıyor — aynı lemma iki anlam",
  "biçim (517 ailesi): 57:24 'inne' + hasr 'huve', 57:25 1P → lafız 3MS geçişi ölçüm kip / iltifât alanlarında yok",
  "iki okumalı (KAPATILAMAZ): 57:24 'ellezîne yebhalûn' — 57:23 'kulle muhtâlin fehûr'dan bedel / yeni mübteda (haber hazf)",
  "konuşan / gönderge (1017 ailesi): 57:25 elçiler ve yardım edenler adsız; 57:26 'minhum' göndergesi soy; 31:18 bağlamındaki kişi adı basılan ayette yok — kayıttan önce mercekten çıkarıldı",
  "okuma (sûre içi): فخر 57:20 tefâhur / 57:23 fehûr; ولي 57:15 mevlâ / 57:24 yetevelle; عزز 57:1 / 57:25; نزل 57:25 kitap-mîzân ve demir için aynı fiil; 'le-qad erselnâ' 57:25 / 57:26; 've kesîrun minhum fâsiqûn' 57:16 / 57:26",
  "karşıt çift (aday 1039, okuma): 57:23 fâtekum / âtâkum (kayıp / verilen); 57:24 yebhalûn / el-ğaniyy; 57:18 / 57:24 sadaka / cimrilik; 57:25 be'sun şedîd / menâfi'; 57:26 muhted / fâsiqûn — kayıt, test yok",
  "çıpa: 57:25 L1 (demir); 57:23, 24, 26 değerlendirilmedi; L4 yok",
  "okuma: 57:22, 31:18, 11:10 → 57:23; 47:38, 48:17, 31:26, 35:15 → 57:24; 42:17, 55:7, 17:50, 18:96, 22:21, 34:10, 50:22 → 57:25; 29:27, 45:16, 57:16, 57:25 → 57:26 — KAPATILAMAZ",
  "tetik: ön kuru koşu 2 tetik satırı (57:24 B, 57:25 B) — kayıtta 0 uyuşmaz; [x/y] 0 (44 sayım); kayıttan önce 57:26 'ilk adlı kişi' iddiası ölçüm satırlarıyla doğrulandı",
 ],
 (27, 29): [
  "esmâ: e_oto 3 token (57:28 'nûr', 'ğafûr', 'rahîm'); 'nûr' DEĞİL (ışık), 'ğafûr', 'rahîm' İLÂHÎ; KARAR 515 → 518; geçerli mühür 57:28 (ölçüm ÇİFT); 57:29 son kelime 'el-azîm' esmâ listesinde yok (56:96 emsali)",
  "aday 1041 alanı (kayıt, test yok): kökler رأف ve رحم 57:9 Allah için ('ra'ûfun rahîm') / 57:27 insanların kalbinde ('ra'feten ve rahmeten'); lemma 'yed' 57:12 insan elleri / 57:29 'bi-yedi'llâh'",
  "aktör: 57:27 adlı Îsâ, Meryem, kitap İncîl (ölçüm) — sûrenin ikinci ve son adlı ayeti (57:26 Nûh, İbrâhîm)",
  "yıldız: 57:27 ★★ n z=2,82 (uzun ayet); 57:29 ★★ allah z=2,20 (3 lafız, 22 kelime) — formül; 57:28 yıldızsız",
  "iki okumalı (KAPATILAMAZ): 57:27 'ruhbâniyye' atıf (ce'alnâ'ya) / ayrı cümle (ibteda'ûhâ) — meal ikincisini seçti; 'illa'btiğâ'e ridvâni'llâh' istisna munqatı' / muttasıl; 57:29 'li-ellâ' 'lâ' zâide mi — meal olumlu okudu",
  "gloss / lemma (1021 ailesi): 'kifl' lemması 21:85, 38:48'de özel ad parçası ('zâ'l-kifl'), 57:28'de 'kifleyn' (iki pay) — lemma sayacı ayırmıyor",
  "biçim (517 ailesi): 57:27 1P anlatı içinde lafız ('ridvâni'llâh') ayet içi geçişi iltifât 0; 57:28 emre cevap meczûm üç fiil ölçümde ayrı kip değil",
  "sûre kapanışı (okuma): 57:21 ve 57:29 aynı cümleyle bitiyor ('yu'tîhi men yeşâ'u va'llâhu zu'l-fadli'l-azîm'; nakarat3 GEÇER); 've kesîrun minhum fâsiqûn' üç ayette (57:16, 26, 27); 'nûr' 57:9-28 boyunca 7 token; aday 1040 alanı 57:29 → 58:1 yazılmadı (58 henüz okunmadı)",
  "karşıt çift (aday 1039, okuma): 57:27 ce'alnâ ra'fe ve rahme / ibteda'û ruhbâniyye, âmenû minhum / fâsiqûn; 57:29 lâ yaqdirûn / bi-yedi'llâh — kayıt, test yok",
  "çıpa: 57:27-29 değerlendirilmedi (doğal olgu yok); L4 yok",
  "okuma: 57:26, 19:34, 33:7, 9:111, 48:29, 24:2, 57:9, 57:16 → 57:27; 33:70, 57:7, 21:85, 38:48, 57:12 → 57:28; 29:46, 57:21, 57:12, 57:1 → 57:29 — KAPATILAMAZ",
  "tetik: ön kuru koşu 2 tetik satırı (57:27 B, 57:29 B) — kayıtta 0 uyuşmaz; [x/y] 0 (45 sayım); kayıttan önce 'yâ eyyuhâ' sûre içi tekliği lemma sayımıyla doğrulandı (kök أيي sûre içi 57:9, 17, 19 âyet; nidâ yalnız 57:28)",
 ],
}

DUZELTME = {
}
