# -*- coding: utf-8 -*-
"""ahkaf_kayit.py — sûre 46 (Ahkâf) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 46

CIPA = {
 # blok 1-10
 3: dict(kademe='L1', olgu=True, cipa=False, not_="gökler, yer ve 'mâ beynehumâ' 'bi'l-haqq' + 'ecelin musemmâ' (adı konmuş süre, birimsiz): öğe + süre niteliği, süreç/mekanizma yok — L1 (30:8 aynı terkip); tarayıcı vermedi"),
 4: dict(kademe='L0', olgu=True, cipa=False, not_="yer ve gökler adlanıyor (yalvarılanların yaratması sorgulanıyor; 35:40 aynı terkip, L0); tarayıcı v4 adayı, çıpa değil"),
 # blok 11-20
 15: dict(kademe='L4', olgu=True, cipa=True, not_="ÖLÇÜ kolu: taşıma + sütten kesme 'selâsûne şehrâ' (birim şehr) ve 'erba'îne sene' (birim sene); taşıma/doğurma 'kurhen', olgunluk eşiği 'belağa eşuddeh' adlı; mekanizma yok — ölçü kolu tek başına L4 adayı, TARTIŞMALI (31:14 emsali: sûre 31 kapanışı 'L4 adayı, TARTIŞMALI', KAPATILAMAZ); 31:14 'iki yıl' ile 46:15 'otuz ay' arasındaki hesap metinde kurulmuyor; tarayıcı v4 adayı — isabet"),
 # blok 21-30
 24: dict(kademe='L1', olgu=True, cipa=False, not_="bulut ('âriz', 'mumtır') ve rüzgâr ('rîh') adlanıyor; algı ('hâzâ âridun mumtırunâ') ile durum ('bel huve … rîhun') açıkça ayrılıyor ama karşılaştırma yok — L3 koluna sınırda (27:88 L3'te karşılaştırma vardı), KAPATILAMAZ; süreç/ölçü yok — L1 (41:16 emsali); tarayıcı vermedi"),
 26: dict(kademe='L1', olgu=True, cipa=False, not_="kulak, göz, gönül verilen olarak (16:78, 23:78, 32:9 aynı üçlü); işlev/mekanizma yok — L1; tarayıcı vermedi"),
 # blok 31-35
 33: dict(kademe='L1', olgu=True, cipa=False, not_="gökler ve yer yaratılan olarak + 'lem ya'ya' yorulmama niteliği; ölüleri diriltme gücü a fortiori delil (36:81 L0, 17:99 aynı açılış); süreç/ölçü yok — L1; tarayıcı v4 adayı, çıpa değil"),
 35: dict(kademe='L1', olgu=False, cipa=False, not_="'sâ'aten min nehâr' süre ölçüsü, 'ke-enne' ile algılanan kalış; durum ayrıca söylenmiyor — L3 koluna sınırda, KAPATILAMAZ; gün sonrası algı, doğal olgu iddiası değil — L1 (10:45 emsali); tarayıcı v4 adayı, çıpa değil"),
}

ARIZA = {
 (1, 10): [
  "esmâ (1022 ailesi): 46:7 'mubîn' (büyü), 46:9 'mubîn' (uyarıcı) ölçüm MÜHÜRSÜZ / esma_kayit mühür EVET — değil (mühür yanlış); 46:2 'azîz' + 'hakîm', 46:8 'şehîd', 'ğafûr' + 'rahîm' ilâhî — karar sonrası bilanço geçerli mühür [2, 8]",
  "aday 1040 alanı: 45:37 → 46:1-2 ('el-azîz el-hakîm' önceki sûrenin son ayetinde ve bu sûrenin ikinci ayetinde; 46:1-2 = 45:1-2 esit2 TAM) — kayıt, test yok",
  "aday 1041 alanına sınırda: شهد 46:8 'şehîd' (Allah) / 46:10 'şâhid' (İsrâiloğullarından biri) — aynı kök, farklı kalıp; kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 46:4, 8, 9 'qul' muhatabı / alıntı içi 1S adsız; 46:5-6 yalvaran ve yalvarılan 3MP göndergeleri ayrılmıyor; 46:10 şahit adsız — KAPATILAMAZ",
  "biçim (517 ailesi): 46:5 'men' sorusu, 46:6 'izâ', 46:8 'em', 46:10 şart cevabının hazfi ve tekit ölçümde işaretsiz",
  "gloss (1021 ailesi): أثر 46:4 'esâre' (kalıntı) — gloss 'tercih etme, üstün tutma'",
  "okuma: 15:85 + 30:8 → 46:3; 35:40 → 46:4; 34:43 → 46:7; 11:35 → 46:8; 13:43, 29:52 → 46:8 ('kefâ bihî şehîden'); 10:15 → 46:9; 41:52 → 46:5 + 46:10 — KAPATILAMAZ",
  "oturum notu: esmâ bilanço iddiası okuyucu kararı eklendikten SONRA koşulan bilançodan yazıldı (sûre 45 dersi)",
  'tetik: ilk koşuda 0 uyuşmaz (46:3 سمو/أرض/أجل + خلق; 46:4 أرض/سمو + خلق; 46:5 يوم; 46:6 أنس)',
 ],
 (11, 20): [
  "esmâ (1022 ailesi): 46:17 'evvel' ('esâtîru'l-evvelîn', öncekiler) esma_kayit SON konum mühür EVET / ölçüm esmâ yok — değil (mühür yanlış); karar sonrası bilanço geçerli mühür yok (bilanço karar eklendikten SONRA koşuldu)",
  "çıpa: 46:15 L4 adayı (ölçü kolu: 'selâsûne şehrâ', 'erba'îne sene'; mekanizma yok) — TARTIŞMALI, 31:14 emsali; tarayıcı v4 isabet; KAPATILAMAZ",
  "aday 1041 alanına sınırda: وعد 46:17 anne babanın vaadi ('ete'idâninî') ve 'va'da'llâh' aynı ayette; 46:16 'va'de's-sıdq … yû'adûn' — aynı kök, farklı kalıp; kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 46:11 'bihî' göndergesi; 46:12 'li-yunzira' öznesi 3MS; 46:17 söyleyen 'ellezî'; 46:19 'li-yuvaffiyehum' fâili; 46:20 alıntının söyleyeni — metinde adsız, KAPATILAMAZ; 46:17 tekil 'ellezî' → 46:18 çoğul 'ulâ'ike'",
  "biçim (517 ailesi): 46:13, 46:15, 46:17, 46:18 tekit 'inne', 46:15 nidâ, 46:20 alıntı ölçümde işaretsiz",
  "okuma: 11:17 → 46:12 (şahit + Mûsâ'nın kitabı sırası 46:10 → 46:12); 41:30 → 46:13; 29:8, 31:14, 27:19, 41:33 → 46:15; 24:38 → 46:16; 17:23, 21:67, 23:35 → 46:17; 41:25 → 46:18; 41:15, 40:75, 41:17 → 46:20 — KAPATILAMAZ",
  "ölçü iki sûrede: 31:14 sütten kesme 'iki yıl' / 46:15 taşıma + sütten kesme 'otuz ay' — aradaki hesap metinde yok (okuma; KAPATILAMAZ)",
  'tetik: ilk koşuda 0 uyuşmaz (46:15 سنو + أنس/حمل/وضع; 46:18 أنس; 46:20 يوم/أرض + حيي)',
 ],
 (21, 30): [
  "esmâ: blokta esmâ tokeni yok (e_oto 0); mühür yok",
  "çıpa: 46:24 L3 koluna sınırda (algı/durum ayrımı var, karşılaştırma yok) — L1 kaydedildi, KAPATILAMAZ; tarayıcı v4 aday vermedi",
  "konuşan / gönderge (1017 ailesi): 46:21 'ehâ âd' adsız (11:50, 26:124'te adlı); 46:21 'vezkur', 46:29 'ileyke' muhatap 2MS adsız; 46:23 söyleyen 1S; 46:24 'bel huve …' cümlesinin söyleyeni — metinde adsız, KAPATILAMAZ",
  "biçim (517 ailesi): 46:23 'innemâ' hasrı ve 'lâkinne'; 46:28 'lev lâ' tahzîzi; 46:30 tekit 'innâ' ölçümde işaretsiz; 46:24 3MP → 2MP geçişi ölçümde iltifât 0",
  "hapaks: حقف 46:21 'ahqâf' (kok_ekle_46; korpusta 1) — ★★★ kaynak hapaks",
  "okuma: 41:14 → 46:21 ('min beyni … ve min half' + 'allâ ta'budû illa'llâh', çoğuldan tekile); 26:135, 11:26 → 46:21; 11:32 → 46:22; 33:63, 11:57, 11:29 → 46:23; 41:16, 13:17 → 46:24; 10:13, 29:38 → 46:25; 16:78, 23:78, 32:9, 45:33 → 46:26; 29:41 → 46:28; 46:12 → 46:30 (önce / sonra, Mûsâ'nın kitabı) — KAPATILAMAZ",
  "Âd anlatısında 11:26 ve 11:29, 11:32 (Nûh anlatısı) cümleleri 46:21-23'te Âd'ın kardeşine/kavmine (okumada görüldü; kayıt)",
  'tetik: ilk koşuda 0 uyuşmaz (46:21 يوم + يدي; 46:24 روح; 46:26 سمع/بصر; 46:29 سمع; 46:30 سمع/يدي)',
 ],
 (31, 35): [
  "esmâ (1022 ailesi): 46:32 'velî' ('evliyâ'', Allah'tan başkası) ve 'mubîn' (sapıklık) ölçüm MÜHÜRSÜZ / esma_kayit mühür EVET (ÇİFT) — değil (mühür yanlış); 46:33 'qadîr' ölçüm MÜHÜRSÜZ / esma_kayit mühür EVET — ilâhî; karar sonrası bilanço geçerli mühür [33]",
  "aday 1041 alanı: 'velî' lemması 42:9 'fe'llâhu huve'l-veliyy' (Allah) / 46:32 'min dûnihî evliyâ'' (Allah'tan başkası) — aynı lemma; kayıt, test yok",
  "kafiye: 46:33 fâsıla ر — KAFİYE KIRILMASI (ölçüm); sûrenin öbür 34 ayeti ن 26 / م 8",
  "çıpa: 46:33 L1 (36:81 emsali), 46:35 L1 (L3 koluna sınırda, 'ke-enne' algısı; 10:45 emsali) — tarayıcı v4 iki aday, çıpa değil",
  "konuşan / gönderge (1017 ailesi): 46:31 'dâ'iya'llâh' adsız, 'bihî' göndergesi; 46:34 soran ve 'qâle' öznesi; 46:35 muhatap 2MS — metinde adsız, KAPATILAMAZ",
  "biçim (517 ailesi): 46:31 emrin cevabı cezmi; 46:32 'men' şartı; 46:33 'belâ' ve tekit; 46:34 yemin; 46:35 'ke-enne' teşbihi ölçümde işaretsiz",
  "okuma: 33:46, 14:10 → 46:31; 39:22, 42:9 → 46:32; 17:99, 42:9, 41:39 → 46:33; 46:3 → 46:33 (gökler-yer yaratması sûre başı ve sonu); 46:20 → 46:34 (aynı açılış, iki alıntı); 34:3 → 46:34; 10:45 → 46:35 — KAPATILAMAZ",
  "aday 1040 alanı: 46:35 → 47:1 sûre sınırı henüz okunmadı (kayıt yok)",
  'tetik: ilk koşuda 0 uyuşmaz (46:32 أرض; 46:33 سمو/أرض + خلق/حيي/موت; 46:34 يوم; 46:35 يوم/سوع/نهر)',
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_46.py uygular)
DUZELTME = {
}
