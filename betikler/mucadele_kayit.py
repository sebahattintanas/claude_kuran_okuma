# -*- coding: utf-8 -*-
"""mucadele_kayit.py — sûre 58 (Mücâdele) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 58

CIPA = {
 # blok 5-7
 6: dict(kademe=None, olgu=False, cipa=False, not_="'yevme yeb'asuhumu'llâhu cemî'an' — diriliş günü, âhiret; doğal olgu değil; tarayıcı vermedi"),
 7: dict(kademe='L0', olgu=True, cipa=False, not_="'ya'lemu mâ fi's-semâvâti ve mâ fi'l-ard' — gökler ve yer yalnız bilginin alanı olarak adlanıyor; süreç / ölçü yok — L0 (57:5 emsali); sayı dizisi kişi sayısı, ölçü değil; tarayıcı v4 adayı, çıpa değil"),
 # blok 8-10
 8: dict(kademe=None, olgu=False, cipa=False, not_="'hasbuhum cehennem, yaslevnehâ' — cehennem, âhiret; doğal olgu değil; tarayıcı vermedi"),
 # blok 14-18
 17: dict(kademe=None, olgu=False, cipa=False, not_="'ashâbu'n-nâri hum fîhâ hâlidûn' — ateş, âhiret; doğal olgu değil; tarayıcı vermedi"),
 18: dict(kademe=None, olgu=False, cipa=False, not_="'yevme yeb'asuhumu'llâhu cemî'an' — diriliş günü, âhiret; doğal olgu değil; tarayıcı vermedi"),
 # blok 19-22
 22: dict(kademe=None, olgu=False, cipa=False, not_="'cennâtin tecrî min tahtihe'l-enhâr' — cennet, âhiret; doğal olgu değil (57:12 emsali); tarayıcı v4 adayı, çıpa değil"),
}

ARIZA = {
 (1, 4): [
  "esmâ: e_oto 5 token (58:1×2, 58:2×2, 58:3), okuyucu kararı 5'inde İLÂHÎ (lafzın haberi); KARAR 518 → 523; bilanço geçerli mühür 58:1, 2, 3",
  "esmâ ayrışması: ölçüm satırı 58:3 'habîr' için 'MÜHÜRSÜZ', bilanço geçerli mühür (57:2 emsali) — mühür iddiası yalnız bilançodan (aday 1022 ailesi)",
  "harf alanı: ayet 1 ölçümünde harf → harf3 farkı 'isaret' alanıyla açıklanmıyor — 58:1 93 → 72 (isaret 0), 57:1 57 → 37, 56:1 33 → 14 (isaret 0); 58:2-4'te fark = isaret (6, 6, 7). Sûre başı besmele harfleri 'harf' alanına giriyor olabilir — araç alanı, metin hakkında kanıt değil (aday 924); araç donuk, KAPATILAMAZ",
  "gloss (1021 ailesi): kök ظهر tablosu 'sırt; zuhur, açığa çıkma' — 'zâhara' III. bab iki kullanımı (33:26 arka çıkma / 33:4, 58:2-3 eşi anneye benzetme) ayrı yazılmıyor",
  "adsız (aday 1017): 58:1 konuşan kadın ('elletî'), kocası ('zevcihâ'), muhatap 2MS — ad verilmedi",
  "aday 1040 alanı (kayıt, test yok): 57:29 → 58:1 — lafızla kapanış / lafız 3. kelimede açılış; 'ya'lem' / 'semi'a'; fâsıla م → ر",
  "aday 1041 alanı (kayıt, test yok): lemma 'semî'' ve 'basîr' 11:24 insan benzetmesinde / 58:1 lafzın haberi",
  "karşıt çift (aday 1039, okuma): 58:2 sözle 'anne' denen eşler / doğuran anneler; 58:4 inanma / inkâr — kayıt, test yok",
  "yıldız: 58:1 ★★★ allah z=3,92 (4 lafız / 18 kelime) — bloğun tek yıldızı; 58:2-4 yıldızsız",
  "çıpa: 58:1-4 değerlendirilmedi (doğal olgu yok); L4 yok",
  "okuma: 3:181†, 12:86, 24:35, 22:75, 31:28, 11:24, 57:29 → 58:1; 33:4, 33:26, 33:6, 22:30, 25:4, 22:60 → 58:2; 57:10 → 58:3; 48:9 → 58:4 — KAPATILAMAZ",
  "tetik: ön kuru koşu 1 tetik satırı (58:1 B) — kayıtta 0 uyuşmaz; [x/y] 0 (47 sayım)",
 ],
 (5, 7): [
  "esmâ: e_oto 2 token (58:6 'şehîd', 58:7 'alîm'), ikisi İLÂHÎ (lafzın haberi); KARAR 523 → 525; bilanço geçerli mühür 58:6, 7",
  "esmâ ayrışması: ölçüm satırı 58:6 'şehîd' ve 58:7 'alîm' için 'MÜHÜRSÜZ', bilanço geçerli mühür (57:2, 58:3 emsali) — mühür iddiası yalnız bilançodan (aday 1022 ailesi)",
  "biçim (517 ailesi): 58:5 lafızlı 3. şahıs cümleden 1P 'enzelnâ'ya geçiş — sahset ['1', '3'], iltifât 0",
  "kök tablosu: كبت bu blokta eklendi (kok_ekle_58; 1414 → 1415); retroaktif yama 0",
  "aday 1041 alanı (kayıt, test yok): lemma 'râbi'' / 'sâdis' 18:22 köpek / 58:7 'huve' (lafız); 'nesiye' 9:67 insan ve Allah / 58:6 yalnız insan; 'şehîd' 24:6 insan tanıklar / 58:6 lafzın haberi; 'alîm' 51:28 insan / 58:7 lafzın haberi",
  "karşıt çift (aday 1039, okuma): 58:6 ahsâ / nesû; 58:7 ednâ / ekser, gökler / yer — kayıt, test yok",
  "yıldız: 58:5 ★★ pas z=2,52 (iki edilgen 'kubitû / kubite'); 58:6 ★★★ allah z=3,47 + kafiye kırığı (د); 58:7 ★★★ n z=3,67 (47 kelime)",
  "sûre içi kalıp eşleri henüz okunmadı: 58:5 → 58:20 ('inne'llezîne yuhâddûna'llâhe ve rasûleh'), 58:6 → 58:18 ('yevme yeb'asuhumu'llâhu cemî'â') — nakarat3 GEÇER, okuma eşin bloğunda",
  "çıpa: 58:7 L0 (tarayıcı v4 adayı); 58:6 âhiret, olgu değil; 58:5 değerlendirilmedi; L4 yok",
  "okuma: 58:4, 57:25 → 58:5; 24:64, 18:49, 36:12, 9:67, 22:17, 24:6 → 58:6; 49:16, 9:78, 43:80, 18:22, 57:4, 22:17, 9:115, 29:62, 51:28 → 58:7 — KAPATILAMAZ",
  "tetik: ön kuru koşu 2 tetik satırı (58:6 K, 58:7 K) — kayıtta 0 uyuşmaz; [x/y] 0 (41 sayım)",
 ],
 (8, 10): [
  "esmâ: e_oto 1 token (58:10 'el-mu'minûn'), okuyucu kararı DEĞİL (çoğul inananlar); KARAR 525 → 526; bilanço geçerli mühür yok (ölçüm 'mühür EVET' esma_kayit alanında, karar sonrası geçersiz)",
  "esmâ listesi (aday 1022 ailesi): 'mu'min' esmâ setinde, çoğul 'el-mu'minûn' tekil Allah adıyla aynı lemmaya düşüyor — e_oto sayıyor; karar el ile",
  "gloss (1021 ailesi): kök حيي tablosu dirim / utanma / selamlama anlamlarını ayırıyor; ◈B tetiği kök düzeyinde — 58:8 'hayyevke' selamlama tetik verdi, satır dolu yazıldı (anlam dirim değil)",
  "alıntı (aday 1017 alanı): 58:8 iç söz 'levlâ yu'azzibuna'llâhu bimâ neqûl' — 1P alıntı içinde, sahset 1/2/3, iltifât 0; konuşanlar adsız fısıldaşanlar, 2MS muhatap adsız",
  "aday 1041 alanı (kayıt, test yok): lemma 'mu'min' esmâ listesinde / 58:10 inananlar",
  "karşıt çift (aday 1039, okuma): 58:8 nuhû / ya'ûdûn; 58:9 ism-udvân-ma'siyet / birr-taqvâ; 58:10 şeytan (üzme) / Allah'a tevekkül — kayıt, test yok",
  "kapanan sûre içi eş: 58:3 'summe ye'ûdûne limâ' → 58:8 'summe ya'ûdûne limâ nuhû anh' (nakarat3 GEÇMEZ; okumada bağ)",
  "yıldız: 58:8 ★★ n z=2,72 + kafiye kırığı (ر); 58:10 ★ allah z=1,82; 58:9 yıldızsız",
  "çıpa: 58:8 cehennem, âhiret, olgu değil; 58:9-10 değerlendirilmedi; L4 yok",
  "okuma: 14:28, 40:69, 58:7, 58:3, 24:61, 57:15, 22:72 → 58:8; 58:8, 58:6 → 58:9; 14:11, 9:51 → 58:10 — KAPATILAMAZ",
  "tetik: ön kuru koşu 1 tetik satırı (58:8 B) — kayıtta 0 uyuşmaz; [x/y] 0 (39 sayım)",
 ],
 (11, 13): [
  "esmâ: e_oto 4 token (58:11 'habîr', 58:12 'ğafûr', 'rahîm', 58:13 'habîr'), dördü İLÂHÎ (lafzın haberi); KARAR 526 → 530; bilanço geçerli mühür 58:11, 12, 13",
  "esmâ son konum (aday 1022 ailesi): 58:13 'habîr' 22. kelime, ayet 'bimâ ta'melûn' ile bitiyor — ölçüm 'SON konum' diyor, esma_kayit son3 'bimâ ta'melûn'u atlıyor; mühür iddiası yalnız bilançodan, ölçüt metnin son kelimesi değil",
  "esmâ ayrışması: ölçüm satırı 58:11 ve 58:13 'habîr' için 'MÜHÜRSÜZ', bilanço geçerli mühür (58:3 emsali); 58:12 ölçüm ÇİFT mühür",
  "kök tablosu: فسح, جلس, نشز bu blokta eklendi (1415 → 1418); retroaktif genel geçişte 1 yama",
  "hapaks: 58:11 فسح ve جلس korpusta tek ayet (ölçüm HAPAKS, z=6,79) — ★★★ kaynağı",
  "dikey (aday 924): 58:11 فسح sonra 'kalkma' ×5800,2, نشز önce فسح ×1675,6 — n=3 / n=5 köklerde beklenen değer çok küçük, kat oranı şişiyor (⚠ n<15); araç alanı, kanıt değil",
  "B tetik (1021 ailesi): يدي kökü 58:12-13 'beyne yedey' (önünde) deyiminde — satır dolu yazıldı, organ işlevi yok",
  "aday 1041 alanı (kayıt, test yok): فسح 58:11 insanlara emir / Allah'ın cevabı aynı ayette; 'tâbe' 24:5 insanlar / 58:13 Allah",
  "karşıt çift (aday 1039, okuma): 49:1 'lâ tuqaddimû' / 58:12 'fe-qaddimû'; 58:12 emir / 58:13 'lem tef'alû' — kayıt, test yok",
  "kapanan sûre içi eş: 58:3 → 58:11 've'llâhu bimâ ta'melûne habîr' (nakarat3 GEÇER); 58:9 → 58:11 → 58:12 'yâ eyyuhe'llezîne âmenû izâ' (3 ayet, nakarat3 GEÇER)",
  "yıldız: 58:11 ★★★ hapaks z=6,79 + kafiye kırığı (ر); 58:13 ★ allah z=1,97; 58:12 yıldızsız",
  "çıpa: 58:11-13 değerlendirilmedi (doğal olgu yok); L4 yok",
  "okuma: 9:38, 24:28, 12:76, 43:32, 17:107, 57:10, 58:3 → 58:11; 49:1, 11:78, 33:53, 24:28, 58:4, 16:115, 24:5 → 58:12; 33:72, 49:1, 24:5, 22:78, 9:16, 58:11 → 58:13 — KAPATILAMAZ",
  "tetik: ön kuru koşu 2 tetik satırı (58:12 B, 58:13 B) — kayıtta 0 uyuşmaz; [x/y] 0 (45 sayım)",
 ],
 (14, 18): [
  "esmâ: e_oto 0 token; KARAR 530 (değişmedi); bilanço geçerli mühür yok — beş ayetin hiçbiri esmâ ile bitmiyor",
  "sayı işareti (aday 924): 58:15 'e'adde' (hazırladı) kök عدد nedeniyle sayı işareti aldı — anlam sayı değil; araç alanı",
  "biçim (517 ailesi): 58:14 'QASEM' etiketi — yemin fiil olarak anlatılıyor ('yahlifûne'), ayet yemin cümlesi değil; 58:18 'DIKKAT + QASEM' 'elâ inne' tekidi için",
  "lemma (1021 ailesi): 'yemîn' lemması sağ yan (56:27 'ashâbu'l-yemîn') ve yemin ('eymân', 58:16) anlamlarını ayırmıyor (65 token / 58 ayet); kök جنن 'cunne' (kalkan) 'örtme' altında",
  "adsız (aday 1017): 58:14 gazap edilen topluluk ve dost edinenler adsız — ad verilmedi",
  "aday 1039 alanı (kayıt, test yok): 'e'adda'llâhu lehum' 9:89, 33:35 ödül / 58:15 azap; 58:14 minkum / minhum; 58:18 lehû / lekum",
  "kapanan sûre içi eş: 58:5 'azâbun muhîn' → 58:16; 58:6 'yevme yeb'asuhumu'llâhu cemî'an' → 58:18 (nakarat3 GEÇER); 58:8 'e lem tera ile'llezîne' → 58:14 (nakarat3 GEÇER)",
  "yıldız: 58:14-18 beşi de yıldızsız; kafiye kırığı yok, fâsıla beşinde ن",
  "çıpa: 58:17 ateş ve 58:18 diriliş günü âhiret, olgu değil; 58:14-16 değerlendirilmedi; L4 yok",
  "okuma: 58:8, 48:6, 9:56, 43:86 → 58:14; 9:89, 33:35, 9:9 → 58:15; 9:9, 56:27, 58:5, 58:14 → 58:16; 10:27, 58:2 → 58:17; 58:6, 9:62, 18:104, 43:37, 58:14 → 58:18 — KAPATILAMAZ",
  "tetik: ön kuru koşu 1 tetik satırı (58:18 K) — kayıtta 0 uyuşmaz; [x/y] 0 (41 sayım)",
 ],
 (19, 22): [
  "esmâ: e_oto 3 token (58:21 'qavî', 'azîz', 58:22 'âhir'); 'qavî', 'azîz' İLÂHÎ, 'âhir' DEĞİL ('el-yevmi'l-âhir', günün sıfatı; 57:3 'el-âhir' İLÂHÎ kararının karşıtı); KARAR 530 → 533; bilanço geçerli mühür 58:21",
  "sayı işareti (aday 924): 58:22 'aşîre' (akraba) kök عشر ('on') nedeniyle sayı işareti aldı — anlam sayı değil",
  "alıntı (1017 alanı / 517 ailesi): 58:21 'keteba'llâhu le-ağlibenne ene ve rusulî' — lafızlı 3. şahıstan 1S alıntıya geçiş; sahset 1/3, iltifât 0",
  "kök tablosu: حوذ bu blokta eklendi (1418 → 1419); retroaktif yama 0",
  "aday 1041 alanı (kayıt, test yok): 'âhir' 57:3 Allah / 58:22 gün; رضو 58:22 aynı ayette Allah ve insanlar ('radiya'llâhu anhum ve radû anh')",
  "karşıt çift (aday 1039, okuma): 58:19 hizbu'ş-şeytân / hâsirûn ↔ 58:22 hizbu'llâh / mufluhûn; 58:20 ezellîn / 58:21 le-ağlibenne; 58:22 yuvâddûn / hâdde — kayıt, test yok",
  "kapanan sûre içi eş: 58:5 → 58:20 'inne'llezîne yuhâddûna'llâhe ve rasûleh' (nakarat3 GEÇER); 58:6 'nesûh' → 58:19 'fe-ensâhum'; 58:10 şeytan → 58:19",
  "ardışık sûre (aday 1040 alanı, kayıt): 'inne'llâhe qaviyyun azîz' yalnız 57:25 ve 58:21",
  "yıldız: 58:21 ★★★ allah z=3,92 + kafiye kırığı (ز); 58:22 ★★★ n z=4,10 (51 kelime); 58:20 ★ allah z=1,97; 58:19 yıldızsız",
  "çıpa: 58:22 cennet, âhiret, olgu değil (tarayıcı v4 adayı); 58:19-21 değerlendirilmedi; L4 yok",
  "okuma: 18:63, 58:6, 58:10, 58:22 → 58:19; 58:5 → 58:20; 57:25, 22:40, 58:22 → 58:21; 9:44, 9:63, 9:24, 9:89, 57:12, 9:100, 57:3, 58:19 → 58:22 — KAPATILAMAZ",
  "tetik: ön kuru koşu 2 tetik satırı (58:22 K, 58:22 B) — kayıtta 0 uyuşmaz; [x/y] 0 (46 sayım)",
 ],
}

DUZELTME = {
}
