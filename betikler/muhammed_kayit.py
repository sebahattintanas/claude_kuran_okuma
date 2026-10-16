# -*- coding: utf-8 -*-
"""muhammed_kayit.py — sûre 47 (Muhammed) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 47

CIPA = {
 # blok 1-10
 10: dict(kademe='L0', olgu=True, cipa=False, not_="yeryüzü yalnız gezilen yer olarak adlanıyor ('fi'l-ard'); süreç/ölçü yok — L0 (40:21, 40:82 emsali); tarayıcı vermedi"),
 # blok 11-20
 22: dict(kademe='L0', olgu=True, cipa=False, not_="yeryüzü yalnız bozgunculuğun yeri olarak adlanıyor ('fi'l-ard'); süreç/ölçü yok — L0 (40:21 emsali); tarayıcı v4 adayı, çıpa değil"),
 23: dict(kademe='L1', olgu=True, cipa=False, not_="gözler ('ebsâr', tetik بصر) ve sağırlık fiili — işlev alınan olarak; mekanizma yok — L1 (46:26 emsali: aynı organlar verilen); 22:46 'kalpler kör olur' okumada görüldü; tarayıcı vermedi"),
 36: dict(kademe=None, olgu=False, cipa=False, not_="'el-hayâtu'd-dunyâ la'ibun ve lehv' — dünya hayatının nitelenmesi, doğal olgu yok; tarayıcı v4 adayı (hasr 'innemâ'), çıpa değil"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="cennet ırmakları (su, süt, şarap, bal) ve kaynar su — âhiret sahnesi, doğal olgu iddiası değil (37:46, 44:46 emsali); 'em'â'' organ anılıyor, mekanizma yok; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: blokta esmâ tokeni yok (e_oto 0); mühür yok; e_el=? 0",
  "aday 1040 alanı: 46:34-35 ('ellezîne keferû', helâk) → 47:1 ('ellezîne keferû … adalle'); 46:25 'tudammiru' → 47:10 'dammera'llâhu' (aynı lemma); 47:1 hurûf-ı mukattaa yok — 'Hâ Mîm' dizisinin dışında — kayıt, test yok",
  "aday 1041 alanı: نصر 47:7 'in tensurû'llâha yensurkum' — aynı lemma insan → Allah ve Allah → insan, aynı ayette; 'intesara' 47:4 Allah / 26:93, 26:227, 42:39, 42:41 insan ya da ilâhlar; sınırda: كفر 47:1 'keferû' / 47:2 'keffera' (kök ortak, farklı kalıp), 'haqq' 22:62, 31:30 Allah / 47:2 indirilen — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 47:1, 47:8, 47:9 'adalle' / 'ahbata' öznesi 3MS adsız (47:1, 47:8'de ayette lafız fiilin öznesi değil); 47:5-6 'hum' göndergesi 47:4 'ellezîne qutilû'; 47:4-7 muhatap 2MP adsız — KAPATILAMAZ",
  "biçim (517 ailesi): 47:2 ara cümle ('ve huve'l-haqqu min rabbihim'); 47:4 'lev' şartı ve cevap lâmı, 'lâkin', 'immâ … ve immâ'; 47:8 masdarla beddua ('fe-ta'sen') ölçümde işaretsiz; 47:4'te 3MP → 2MP geçişi ayetler arası (ölçüm iltifât alanı ayet içi, 0)",
  "kafiye / yıldız (aday 1001): 47:10 fâsıla ا KAFİYE KIRILMASI; bilanço ★ kaynağı 'allah' (z=0,72) yazıyor — ★'ı veren kafiye kırığı",
  "hapaks: تعس 47:8 'ta's' (kok_ekle_47; korpusta 1) — ★★★ kaynak hapaks",
  "gloss (1021 ailesi, araç): 'menn' lemması 20:80 (yiyecek) / 47:4 (karşılıksız bırakma) aynı lemma etiketi",
  "okuma: 16:88, 22:25 → 47:1; 29:7 → 47:2; 22:62, 31:30, 14:25 → 47:3; 26:93, 26:227, 42:39, 42:41 → 47:4 ('intesara'); 40:8 → 47:6; 33:19 → 47:9; 12:109, 30:9, 35:44, 40:21, 40:82 → 47:10 — KAPATILAMAZ",
  "tetik: ilk koşuda 0 uyuşmaz (47:3 أنس; 47:4 وضع; 47:10 أرض)",
 ],
 (11, 20): [
  "esmâ (1022 ailesi): 47:11 'mevlâ' ×2 ölçüm MÜHÜRSÜZ / esma_kayit mühür EVET (ÇİFT) — 47:11:4 ilâhî, 47:11:10 değil ('lâ mevlâ lehum'); 47:19 'mu'min' (insan) değil; karar sonrası bilanço geçerli mühür [11]",
  "aday 1041 alanı: ولي 47:11 'mevlâ' Allah için / olumsuzlanmış başkası için aynı ayette (44:41 insanlar arası); علم 47:19 'fa'lem' (2MS) / 've'llâhu ya'lemu' aynı ayette — kayıt, test yok",
  "hapaks: أسن, عسل, معي 47:15 (★★★ hapaks z=10,30); شرط 47:18 (★★★ z=3,28) — kok_ekle_47",
  "◈B tetik dışı organ: 47:15 'em'â'' (معي) ve 'şârib' (شرب) listede yok — satır '—', gözlem ◇'de (ön-kayıt §4 sınırı; metin hakkında kanıt değil)",
  "konuşan / gönderge (1017 ailesi): 47:13 'ahraceteke' muhatap 2MS ve kasaba adsız; 47:13 1P konuşan (47:12 3MS lafızdan geçiş, ayetler arası); 47:14 'zuyyine' süsleyen adsız; 47:16 alıntıdaki 'qâle' öznesi; 47:17 'zâde' öznesi 3MS; 47:20 muhatap 2MS — KAPATILAMAZ",
  "biçim (517 ailesi): 47:12 tekit 'inne', teşbih 'kemâ'; 47:14-15 'e-fe-men … ke-men' / 'mesel … ke-men' teşbihli inkârî soru; 47:20 'lev lâ' tahzîzi ve teşbihli mef'ûl-i mutlak ölçümde işaretsiz",
  "okuma: 22:14, 22:23 → 47:12; 41:24 → 47:12; 22:45, 30:9 → 47:13; 11:17 + 35:8 → 47:14 (iki açılış yan yana); 13:35, 16:66, 37:46, 44:46 → 47:15; 10:42, 16:108 → 47:16; 9:124 → 47:17; 43:66 → 47:18; 12:29, 40:55 → 47:19; 9:124, 24:1, 33:12, 33:19 → 47:20 — KAPATILAMAZ",
  "tetik: ikinci koşuda 0 uyuşmaz — ilk koşuda 47:15 ◈B tetiksiz satır dolu yazılmıştı, '—' yapıldı (organ gözlemi ◇'ye taşındı)",
 ],
 (21, 30): [
  "esmâ: blokta esmâ tokeni yok (e_oto 0); mühür yok; e_el=? 0",
  "aday 1041 alanı: خرج 'ahraca' 47:13 (kasaba muhatabı çıkardı) / 47:29 (Allah kinleri çıkarır) aynı lemma; sınırda: عرف 47:6 ''arrafe' (Allah) / 47:30 ''arafa' (2MS) farklı lemma; 'emlâ' 47:25 öznesi şeytân/Allah belirsiz, 13:32 ve 22:44'te Allah göndergeli 1S — kayıt, test yok",
  "kafiye: 47:24 fâsıla ٓ — KAFİYE KIRILMASI (sûrede ikinci, 47:10'dan sonra); ★★★ kaynağı hapaks (قفل)",
  "hapaks: قفل 47:24 'aqfâl', لحن 47:30 'lahn' (★★★, z=3,28) — kok_ekle_47",
  "gloss (1021 ailesi): دبر 'arka' — 47:24 'yetedebberûn' (düşünme, sonunu tartma) anlamını kapsamıyor; ولي tek gloss 47:11 'mevlâ', 47:20 'evlâ', 47:22 'teveleytum' üçünü kapsıyor",
  "konuşan / gönderge (1017 ailesi): 47:21 3MP göndergesi; 47:25 've emlâ lehum' öznesi; 47:26 söyleyen ve muhatap gruplar adsız; 47:30 muhatap 2MS — KAPATILAMAZ",
  "iltifât: ölçüm 47:22 ve 47:23'te iltifât 1 (3MP → 2MP → 3MP); 47:30 ayet içinde 1P → 2MS → 3MS → 2MP, ölçüm iltifât 0 (sahset 1-2-3)",
  "biçim (517 ailesi): 47:21 yüklemsiz isim cümlesi; 47:24 'em' munkatı'a; 47:25 tekit 'inne'; 47:27 'keyfe' cevabının hazfi ölçümde işaretsiz",
  "çıpa: 47:22 L0 (tarayıcı v4 adayı, çıpa değil; kesinlik 0/1); 47:23 L1 (organ işlevi alınıyor; 46:26 emsali)",
  "okuma: 24:53 → 47:21; 13:8, 22:5, 31:34, 33:6 → 47:22 ('erhâm'); 22:46 → 47:23; 23:68, 38:29 → 47:24; 18:64, 12:18, 20:96, 13:32, 22:44 → 47:25; 47:9 → 47:26 (II/IV), 47:28; 16:28, 16:32, 32:11 → 47:27; 9:72 → 47:28; 47:20 → 47:29; 47:4 → 47:30 — KAPATILAMAZ",
  "tetik: ilk koşuda 0 uyuşmaz (47:22 أرض; 47:23 بصر; 47:24 قلب; 47:29 قلب)",
 ],
 (31, 38): [
  "esmâ: 47:38 'ğaniyy' — lafzın haberi, ilâhî (KARAR 385); ölçüm MÜHÜRSÜZ, esma_kayit mühür hayır — ayrışma yok; e_el=? 0",
  "aday 1041 alanı: 'ebtale' 10:81 Allah (büyüyü boşa çıkarır) / 47:33 inananlar ('lâ tubtılû a'mâlekum'); sûre içi 'ahbata' (Allah, 47:9, 28, 32) / 'ebtale' (2MP, 47:33) farklı lemma — kayıt, test yok",
  "aday 1040 alanı: 47:38 → 48:1 sûre sınırı henüz okunmadı (kayıt yok)",
  "çıpa: 47:36 tarayıcı v4 adayı, olgu yok (çıpa değil); blokta L-kademe yok",
  "konuşan / gönderge (1017 ailesi): 47:32 'yuhbitu', 47:36 'yu'tikum' / 'yes'elkum', 47:37 'yuhric' (isteyen mi istek mi) öznesi 3MS adsız; 47:32-33 'er-rasûl' adsız; 47:38 yerine getirilecek topluluk adsız — KAPATILAMAZ",
  "biçim (517 ailesi): 47:32, 47:34 tekit 'inne'; 47:36 hasr 'innemâ'; 47:38 tenbîh 'hâ' ve hasr 'fe-innemâ' ölçümde işaretsiz",
  "okuma: 21:35 → 47:31 ('nebluvkum'); 9:94 → 47:31 ('ahbârikum'); 22:25 → 47:32, 47:34; 16:27, 9:39 → 47:32; 24:54, 33:66, 10:81 → 47:33; 9:80 → 47:34; 19:4 → 47:35; 29:64 → 47:36 (sıra ters); 9:76 → 47:37-38; 29:6, 31:12, 35:15, 9:39 → 47:38 — KAPATILAMAZ",
  "sûre içi kapanışlar (ölçüm): عمل 12/12 (47:1 → 47:35), حبط 3/3, هدي 5/5, طوع 4/4, بطل 2/2, غفر 3/3, كفر 11/11, أمن 11/11, وقي 3/3, خرج 4/4, ضغن 2/2, مثل 4/4, ولي 5/5, سبل 5/5, أله 28/28",
  'tetik: ilk koşuda 0 uyuşmaz (47:34 موت; 47:36 حيي)',
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_47.py uygular)
DUZELTME = {
}
