# -*- coding: utf-8 -*-
"""hucurat_kayit.py — sûre 49 (Hucurât) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 49

CIPA = {
 # blok 11-18
 12: dict(kademe=None, olgu=False, cipa=False, not_="'lahme ehîhi meyten' — soru içinde temsil (gıybet benzetmesi), doğal olgu iddiası değil; tarayıcı v4 adayı, çıpa değil"),
 13: dict(kademe='L1', olgu=True, cipa=False, not_="insanın iki kaynaktan (erkek / dişi) yaratılması + halk / kabile sınıflaması + işlev ('li-te'ârafû'); aşama, ölçü, mekanizma yok — L1 (42:49-50 emsali); ta'lîl lâmı işlev bildiriyor, L2'ye sınırda (27:86 emsali), sınıflama toplumsal; tarayıcı v4 adayı, çıpa değil"),
 16: dict(kademe='L0', olgu=True, cipa=False, not_="gökler ve yer yalnız bilginin nesnesi olarak adlanıyor; süreç/ölçü yok — L0; tarayıcı vermedi"),
 18: dict(kademe='L0', olgu=True, cipa=False, not_="'ğaybe's-semâvâti ve'l-ard' — bilinen gayb; süreç/ölçü yok — L0; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: 49:1 'semî'' + 'alîm', 49:5 'ğafûr' + 'rahîm', 49:8 'alîm' + 'hakîm' — ilâhî, ölçüm MÜHÜR ile esma_kayit EVET uyumlu; 49:9, 49:10 'mu'min' değil — karar sonrası bilanço geçerli mühür [1, 5, 8]",
  "aday 1040 alanı: 48:29 → 49:1 (hitap 3MP / 2MS → 2MP nidâ; fâsıla ا → م; 'Muhammedun rasûlu'llâh' → 'yedeyi'llâhi ve rasûlih'); 48:29 'mağfiraten ve ecran azîmâ' → 49:3; 48:12 'zuyyine … fî qulûbikum' → 49:7 'zeyyenehû fî qulûbikum'; 47:9/28/32 'ahbata' → 49:2 'habita' — kayıt, test yok",
  "aday 1041 alanı: يدي 49:1 'yedeyi'llâh' (48:10 'yedu'llâh' kaydına ek) — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): nidâ 'yâ eyyuhe'llezîne âmenû' ayetlerinde (49:1, 2, 6) konuşan adlanmıyor; 49:4, 49:5 muhatap 2MS adsız; 49:6 fâsık ve topluluk adsız — KAPATILAMAZ",
  "biçim (517 ailesi): tekit 'inne' (49:1, 3, 4, 9), teşbih 'ke-cehri' (49:2), 'lâkinne' ve takdim 'fîkum' (49:7), hasr 'innemâ' (49:10) ölçümde işaretsiz",
  "yıldız formülü: 49:1 (15 kelime, 3 lafız) ★★★ allah z=3,47; 49:8 (7 kelime, 2 lafız) ★★★ allah z=5,18 — kısa ayette lafız oranı (bilinen davranış; içerik iddiası değil)",
  "◈B tetik listesi: 49:2-3 'savt' (ses) tetik listesinde yok — satır '—' / tetik dışı; araç açığı değil, ön-kayıt §4 sınırı",
  "okuma: 9:23, 24:21, 24:27, 33:53, 33:69, 18:57, 22:10, 9:103, 24:60 → 49:1; 31:19, 20:108, 17:64, 9:17, 9:69, 12:15, 39:55 → 49:2; 31:19, 24:30, 24:31, 33:35 → 49:3; 33:53, 29:63 → 49:4; 47:21, 9:74, 9:91, 9:99, 24:62 → 49:5; 46:35, 47:25, 47:32, 9:113, 16:119, 23:40, 26:157 → 49:6; 9:128, 9:23 → 49:7; 9:15, 24:58 → 49:8; 24:2, 28:15, 38:22, 38:24, 42:42 → 49:9; 24:62, 12:5, 12:100, 24:56, 27:46, 36:45 → 49:10 — KAPATILAMAZ",
  "ölçüm (924): 49:1 harf 90 → harf3 61, isaret 0 — korpus metninde 49:1 besmele ile başlıyor (sûre başı); harf sayımı besmeleyi katıyor olabilir, kelime sayısı (n=15) katmıyor — araç açığı, metin hakkında kanıt değil",
  "tetik: ilk koşuda 0 uyuşmaz (49:1 يدي + سمع; 49:3 قلب; 49:7 قلب); [x/y] ilk koşuda 0",
 ], (11, 18): [
  "esmâ: 49:12 'tevvâb' + 'rahîm', 49:13 'alîm' + 'habîr', 49:14 'ğafûr' + 'rahîm' ilâhî (ölçüm MÜHÜR); 49:16 'alîm', 49:18 'basîr' ilâhî, ölçüm MÜHÜRSÜZ / esma_kayit EVET (1022); 49:12 'ehad' ('ehadukum') ve 49:15 'mu'min' değil — karar sonrası bilanço geçerli mühür [12, 13, 14, 16, 18]",
  "aday 1040 alanı: 48:6, 48:12 'zanne's-sev'' → 49:12 'zann'; 48:11 'se-yeqûlu … mine'l-a'râb' → 49:14 'qâleti'l-a'râb'; 48:24 'bimâ ta'melûne basîrâ' → 49:18; sûre sınırı 49:18 → 50:1 henüz okunmadı — kayıt, test yok",
  "aday 1041 alanı: سخر 9:79 'sehira'llâhu minhum' / 49:11 insanlar arası yasak; منن 49:17 'lâ temunnû' (insan) / 'bel Allâhu yemunnu' (Allah) aynı ayette; علم 49:16 'tu'allimûna'llâh' (fâil insan, meful Allah) / 12:37 'allemenî rabbî' — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 49:13 1P 'innâ halaqnâkum' → 3MS 'inda'llâh' ayet içinde, ölçüm iltifât 0; 49:14, 49:16, 49:17 muhatap 2MS adsız ('qul'); 49:17 1S 'aleyye' alıntıda, konuşan adlanmıyor — KAPATILAMAZ",
  "biçim (517 ailesi): zemm 'bi'se' (49:11), tekit 'inne' / 'innâ' (49:12, 13, 14, 18), 'lâkin', 'lemmâ' (49:14), hasr 'innemâ' (49:15) ölçümde işaretsiz",
  "gloss (1021 ailesi): قبل 'ön, önce; kabul' — 49:13 'qabâ'il' (kabile) anlamını kapsamıyor; سخر 'boyun eğdirme' — 49:11 'sehira' (alay etme) anlamını kapsamıyor",
  "yıldız formülü: 49:11 (z=6,79), 49:12 ve 49:14 (z=3,28) ★★★ kaynak hapaks — kok_ekle_49 ile eklenen köklerden (نبز, لقب, جسس, ليت; korpusta 1 token); 49:16 (z=3,22), 49:18 (z=3,47) ★★★ kaynak allah — kısa ayette lafız oranı; bilinen davranış, içerik iddiası değil",
  "◈B tetik listesi: 49:12 'lahm' (et) organ tetik listesinde yok — satır B4 ('meyt') ile dolu, et gözlemi ◇'de",
  "okuma: 9:79, 9:58, 11:38, 21:41, 37:12, 9:23, 24:50 → 49:11; 22:30, 42:37, 39:17, 33:10, 35:12, 25:49, 43:11, 47:9, 47:26, 47:28, 9:104, 9:118 → 49:12; 22:1, 27:16, 35:15, 42:50, 10:45, 31:34 → 49:13; 9:90, 9:97, 9:98, 9:99, 9:101, 9:120, 48:11, 48:16, 24:62 → 49:14; 24:62, 9:45, 24:50, 9:41, 9:81 → 49:15; 12:37, 33:40, 48:26 → 49:16; 14:11, 20:37, 26:22, 28:5, 37:114, 9:74, 12:17 → 49:17; 11:31, 2:3, 9:94, 9:105, 48:24 → 49:18 — KAPATILAMAZ",
  "tetik: ilk koşuda 0 uyuşmaz (ön kuru koşu: 49:12 موت; 49:13 أنس خلق أنث; 49:14 قلب; 49:16 سمو/أرض; 49:18 سمو/أرض + بصر); [x/y] ilk koşuda 0; kayıttan önce yedi emsal anması (görülmeden 'okumada görüldü' yazılmış ayetler) çıkarıldı",
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_49.py uygular)
DUZELTME = {
}
