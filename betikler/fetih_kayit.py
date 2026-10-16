# -*- coding: utf-8 -*-
"""fetih_kayit.py — sûre 48 (Fetih) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 48

CIPA = {
 # blok 1-10
 4: dict(kademe='L0', olgu=True, cipa=False, not_="gökler ve yer yalnız 'cunûd' tamlamasında (mülk) adlanıyor; kalp sekînenin yeri; süreç/ölçü yok — L0; tarayıcı v4 adayı, çıpa değil"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="cennet ırmakları — âhiret sahnesi, doğal olgu iddiası değil (47:15 emsali); tarayıcı v4 adayı, çıpa değil"),
 7: dict(kademe='L0', olgu=True, cipa=False, not_="48:4 ile aynı terkip ('cunûdu's-semâvâti ve'l-ard'); süreç/ölçü yok — L0; tarayıcı vermedi"),
 # blok 11-20
 14: dict(kademe='L0', olgu=True, cipa=False, not_="gökler ve yer yalnız 'mulk' tamlamasında adlanıyor; süreç/ölçü yok — L0; tarayıcı vermedi"),
 17: dict(kademe=None, olgu=False, cipa=False, not_="cennet ırmakları — âhiret sahnesi, doğal olgu iddiası değil (48:5 emsali); tarayıcı vermedi"),
 18: dict(kademe='L0', olgu=True, cipa=False, not_="ağaç yalnız biatin yeri olarak adlanıyor; tür / süreç yok — L0; tarayıcı vermedi"),
 # blok 21-29
 29: dict(kademe='L4', olgu=True, cipa=False, not_="MEKANİZMA kolu adayı: ekin → filiz çıkarma → güçlendirme → kalınlaşma → gövde üzerinde doğrulma; dört aşama 'fe' ile ardışık, ara parçalar adlı (şat', sûq) — 39:21 emsali (L4, büyüme → çöküş); ANCAK teşbih içinde ('ke-zer'in', İncil'deki mesel): olgu benzetme aracı, iddia değil — L4 adayı, TARTIŞMALI (KAPATILAMAZ; cipa kararı açık, okuyucu onayı bekler); tarayıcı v4 adayı (B_ta'lîl) — kısmi isabet"),
}

ARIZA = {
 (1, 10): [
  "esmâ (1022 ailesi): 48:1 'mubîn' (fethin sıfatı) ve 48:3 'azîz' (yardımın sıfatı) ölçüm MÜHÜRSÜZ / esma_kayit mühür EVET — değil (mühür yanlış); 48:4 'alîm' + 'hakîm', 48:7 'azîz' + 'hakîm' ilâhî; 48:4, 48:5 'mu'min' insan — karar sonrası bilanço geçerli mühür [4, 7]",
  "aday 1040 alanı: 47:38 → 48:1 (hitap 2MP → 2MS; fâsıla م → ا); 47:19 'istağfir li-zenbike' → 48:2 'li-yağfira leke … min zenbike'; 47:7 'yensurkum' → 48:3 'yensurake'; 47:19 'li'l-mu'minîne ve'l-mu'minât' → 48:5; 47:38 → 48:10 'fe-innemâ … nefsih' kalıbı — kayıt, test yok",
  "aday 1041 alanı: يدي 48:10 'yedu'llâhi fevqa eydîhim' (aynı lemma Allah ve insan, aynı ayette); 'azîz' 48:3 yardımın sıfatı / 48:7 Allah — kayıt, test yok",
  "yıldız formülü: 48:3 (4 kelime) ve 48:7 (8 kelime) ★★★ kaynak allah z=4,47 — kısa ayette lafız oranı (bilinen davranış; içerik iddiası değil)",
  "konuşan / gönderge (1017 ailesi): 48:1-3, 48:8, 48:10 muhatap 2MS adsız; 48:9 'tu'azzirûhu ve tuvaqqirûhu' zamir göndergesi (Allah / elçi) ayrılmıyor; 48:8 → 48:9 2MS → 2MP — KAPATILAMAZ",
  "biçim (517 ailesi): tekit 'innâ' (48:1, 8), takdim 'li'llâhi cunûdu' (48:4, 7), zemm 'sâ'et' (48:6), hasr 'innemâ' ×2 ve 'fe-innemâ' (48:10) ölçümde işaretsiz",
  "okuma: 32:28-29, 26:118 → 48:1; 12:6, 16:81, 1:6, 37:118, 14:10, 46:31 → 48:2; 9:26, 9:40 → 48:4; 9:72, 29:7, 47:2, 10:64 → 48:5; 33:73, 9:98 → 48:6; 33:45 → 48:8; 33:42, 24:47, 24:62 → 48:9; 9:111, 9:12, 9:13, 43:50, 29:6, 31:12 → 48:10 — KAPATILAMAZ",
  "tetik: ilk koşuda 0 uyuşmaz (48:4 سمو/أرض + قلب; 48:5 نهر; 48:7 سمو/أرض; 48:10 يدي)",
 ],
 (11, 20): [
  "esmâ (1022 ailesi): 48:11 'habîr' ölçüm MÜHÜRSÜZ / esma_kayit EVET — ilâhî; 48:18 'mu'min' + 'qarîb' ve 48:20 'mu'min' esma_kayit EVET — değil (mühür yanlış); 48:14 'ğafûr' + 'rahîm', 48:19 'azîz' + 'hakîm' ilâhî — karar sonrası bilanço geçerli mühür [11, 14, 19]",
  "aday 1040 alanı: 47:38 've in tetevellev' → 48:16 've in tetevellev'; 9:39 'yu'azzibkum … yestebdil qavmen ğayrakum' parçaları 47:38 / 48:16'da; 47:28 'ridvân' → 48:18 'radiya' — kayıt, test yok",
  "aday 1041 alanı: ملك 48:11 'yemliku' (insana soru) / 48:14 'mulk' (Allah); يدي 48:10 'yedu'llâh' / 48:20 'eydiye'n-nâs'; غفر 48:11 'istağfir' (insan isteği) / 48:14 'yağfiru', 'ğafûr' (Allah) — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 48:11, 48:15 muhatap 2MS adsız; 48:12 'zuyyine' süsleyen adsız (edilgen); 48:16 'qavmin ulî be'sin şedîd' topluluk adsız; 48:15 iki ayrı 1P (bedevîler / muhatap tarafı) — KAPATILAMAZ",
  "biçim (517 ailesi): 48:11 soru 'fe-men yemliku', 48:13 tekit 'fe-innâ', 48:14 takdim 'li'llâhi mulku', 48:16 teşbih 'kemâ', 48:17 üçlü tekrar ölçümde işaretsiz",
  "◈B tetik listesi: 48:17 'a'mâ', 'a'rec', 'merîd' (beden durumları) tetik listesinde yok — satır '—'; araç açığı (aday 924: metin hakkında kanıt değil)",
  "okuma: 9:80, 12:97, 12:98, 19:47, 24:62, 9:81 → 48:11; 25:18 → 48:12; 24:42, 42:49, 45:27, 25:70, 33:5, 33:50, 33:59, 33:73 → 48:14; 9:6, 9:83, 9:87 → 48:15; 9:39, 17:5, 27:33 → 48:16; 24:61 → 48:17; 33:51, 28:30 → 48:18; 10:11, 17:18, 18:58, 38:16 → 48:20 — KAPATILAMAZ",
  "tetik: ilk koşuda 0 uyuşmaz (48:11 قلب; 48:12 أبد + قلب; 48:14 سمو/أرض; 48:17 نهر; 48:18 شجر + قلب; 48:20 يدي + أنس)",
 ],
 (21, 29): [
  "esmâ (1022 ailesi): 48:21 'qadîr', 48:24 'basîr', 48:26 'alîm', 48:28 'şehîd' ölçüm MÜHÜRSÜZ / esma_kayit EVET — ilâhî; 48:22 'veliyy' + 'nasîr' (olumsuzlanan başkası, 33:65 formülü) ve 48:27 'qarîb' (fethin sıfatı) esma_kayit EVET — değil (mühür yanlış); 48:25, 48:26 'mu'min', 48:29 'ruhamâ'' değil — karar sonrası bilanço geçerli mühür [21, 24, 26, 28]",
  "aday 1040 alanı: 47:2 'Muhammed' → 48:29 'Muhammed'; 47:30 'sîmâ' → 48:29 'sîmâ'; 47:28 'ridvân' → 48:18 'radiya' → 48:29 'ridvân' — kayıt, test yok; sûre sınırı 48:29 → 49:1 henüz okunmadı",
  "aday 1041 alanı: قدر 48:21 'lem taqdirû' (insan) / 'qadîr' (Allah) aynı ayette (kök); شهد 48:8 'şâhid' (elçi) / 48:28 'şehîd' (Allah) (kök); رحم 48:14 'rahîm' (Allah) / 48:29 'ruhamâ'' (insanlar) (lemma) — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 48:23 muhatap 2MS adsız ('len tecide'); 48:25 1P 'le-azzebnâ' ayetin 3MS lafız bölümüyle aynı ayette, ölçüm iltifât 0; 48:25 birinci 'lev lâ' şartının cevabı metinde yok (meal parantezi); 48:29 'terâhum' 2MS adsız — KAPATILAMAZ",
  "biçim (517 ailesi): 48:29 teşbih 'ke-' ölçümde işaretsiz; 48:25 ölçüm IMPV 1 — metinde emir yok (araç açığı; aday 924: metin hakkında kanıt değil)",
  "◈B tetik listesi: 48:27 'ru'ûs' (baş), 48:29 'vucûh' (yüz), 'zer'' / 'şat'' / 'sûq' (bitki ve gövde) tetik listesinde yok — satırlar '—'; araç açığı (aday 924)",
  "yıldız formülü: 48:29 ★★★ kaynak n z=4,42 (54 kelime, sûrenin en uzun ayeti); sûrede ★★★ 48:3, 48:7 (kaynak allah, kısa) ve 48:29 (kaynak n, uzun) — bilinen davranış, içerik iddiası değil",
  "okuma: 17:60 → 48:21; 33:27 → 48:21, 48:25; 33:15, 33:65 → 48:22; 33:38, 33:62, 35:43 → 48:23; 33:9 → 48:24; 9:120 → 48:25, 48:29; 33:33, 9:26, 33:40 → 48:26; 12:5, 12:43, 12:99, 12:100, 17:60, 37:105 → 48:27; 9:33, 10:29, 13:43, 17:96 → 48:28; 33:40, 47:2, 9:112, 47:30, 9:111, 39:21 → 48:29 — KAPATILAMAZ",
  "tetik: ilk koşuda 0 uyuşmaz (48:24 يدي + بصر; 48:26 قلب); [x/y] ilk koşuda 1 uyuşmaz (48:28 شهد [1/2] → [2/2]) — düzeltildi",
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_48.py uygular)
DUZELTME = {
}
