# -*- coding: utf-8 -*-
"""mulk_kayit.py — sûre 67 (Mülk) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 67

CIPA = {
 # blok 1-10
 2: dict(kademe='L0', olgu=True, cipa=False, not_="'halaqa'l-mevte ve'l-hayâh' — ölüm ve hayat yaratılan olarak adlanıyor; amaç (sınama) doğal olgu değil, süreç / ölçü yok — L0; tarayıcı v4 adayı, çıpa değil"),
 3: dict(kademe='L1', olgu=True, cipa=False, not_="'seb'a semâvâtin tibâqâ … mâ terâ … min tefâvut … hel terâ min futûr' — yedi gök (sayı) kat kat (düzen), uyumsuzluk ve çatlak yokluğu; gözlemcinin bakışı çağrılıyor ama görünüş-durum ayrımı ve karşılaştırma yok; ölçü birimi / mekanizma yok — L1 (41:12, 65:12 emsali); L4 sınıf / ölçü koluna sınırda, KAPATILAMAZ; tarayıcı v4 adayı, çıpa değil"),
 4: dict(kademe='L1', olgu=True, cipa=False, not_="'yenqalib ileyke'l-basaru hâsi'en ve huve hasîr' — görme (bakış) ve yorgunluğu: organ işlevine nitelik; mekanizma / ölçü yok — L1; tarayıcı vermedi"),
 5: dict(kademe='L1', olgu=True, cipa=False, not_="'zeyyenne's-semâ'e'd-dunyâ bi-mesâbîha ve ce'alnâhâ rucûmen li'ş-şeyâtîn' — en yakın gök kandillerle süslü, kandillere işlev (atış); şeytanlar olgu değil, azap âhiret; mekanizma yok — L1 (41:12 emsali); tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'azâbu cehennem' — âhiret; doğal olgu değil; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'semi'û lehâ şehîqan ve hiye tefûr' — cehennemin sesi ve kaynaması, âhiret; 11:40 tennûr dünya nesnesi ama burada âhiret — doğal olgu değil, merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'tekâdu temeyyezu mine'l-ğayz' — cehennem, âhiret; doğal olgu değil; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'lev kunnâ nesme'u ev na'qilu' — işitme ve akletme yeti olarak, gerçekleşmemiş şartta; olgu tarifi yok, âhiret konuşması; merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 11-20
 15: dict(kademe='L1', olgu=True, cipa=False, not_="'ce'ale lekumu'l-arda zelûlâ fe'mşû fî menâkibihâ ve kulû min rizqih' — yer + nitelik (boyun eğik) + işlev (yürüme, yeme); mekanizma / ölçü yok — L1; tarayıcı vermedi"),
 16: dict(kademe='L1', olgu=True, cipa=False, not_="'en yahsife bikumu'l-arda fe-izâ hiye temûr' — yerin batırılması ve çalkalanması, tehdit kipinde; batırma → çalkalanma ardışıklığı ('fe-izâ') L2 koluna sınırda, sebep ilâhî fail — L1, KAPATILAMAZ; tarayıcı vermedi"),
 17: dict(kademe='L0', olgu=True, cipa=False, not_="'en yursile aleykum hâsibâ' — taş yağdıran rüzgâr adlanıyor, tehdit kipinde; süreç / ölçü yok — L0; tarayıcı vermedi"),
 19: dict(kademe='L1', olgu=True, cipa=False, not_="'ile't-tayri fevqahum sâffâtin ve yaqbidn mâ yumsikuhunne ille'r-rahmân' — kuşlar + uçuş davranışı (kanat açma / kapama); havada tutulmanın nedeni ilâhî fail, doğal olgu arası sebep-sonuç değil — L2 koluna sınırda, KAPATILAMAZ; L1; tarayıcı v4 adayı, çıpa değil"),
 # blok 21-30
 22: dict(kademe=None, olgu=False, cipa=False, not_="'yemşî mukibben alâ vechihî … seviyyen alâ sırâtin mustaqîm' — iki yürüyüş meseli, karşılaştırma aracı; olgu değil (teşbih aracı), merdiven uygulanmadı; tarayıcı vermedi"),
 23: dict(kademe='L1', olgu=True, cipa=False, not_="'enşe'ekum ve ce'ale lekumu's-sem'a ve'l-ebsâra ve'l-ef'ide' — insan + verilen organ / yetiler (işitme, görme, gönül); aşama ve mekanizma yok — L1 (23:78, 32:9 emsali); tarayıcı vermedi"),
 24: dict(kademe='L0', olgu=True, cipa=False, not_="'zere'ekum fi'l-ard' — insanın yeryüzüne yayılması adlanıyor; toplanma âhiret; süreç / ölçü yok — L0; tarayıcı vermedi"),
 27: dict(kademe=None, olgu=False, cipa=False, not_="'sî'et vucûhu'llezîne keferû' — âhiret sahnesi; doğal olgu değil; tarayıcı vermedi"),
 30: dict(kademe='L2', olgu=True, cipa=False, not_="'in asbaha mâ'ukum ğavran fe-men ye'tîkum bi-mâ'in ma'în' — suyun yerin dibine çekilmesi ve akan suyu kimin getireceği: yeti sınırı kolu, soru biçiminde (18:41 'fe-len testetî'a' açık, 27:60 ve 35:41 emsali) — L2; mekanizma / ölçü yok; tarayıcı v4 adayı, çıpa değil"),
}

ARIZA = {
 (1, 10): [
  "esmâ: e_oto 5 token (67:1 'qadîr'; 67:2 'azîz', 'ğafûr'; 67:3 'rahmân'; 67:9 'kebîr'); 'kebîr' DEĞİL (sapıklığın sıfatı), öbür dördü İLÂHÎ; KARAR 635 → 640; bilanço geçerli mühür 67:1, 67:2; 67:9 esma_kayit mühür EVET, karar sonrası geçersiz (1022); 67:1 ölçüm satırı 'MÜHÜRSÜZ' yazıyor, bilanço geçerli mühür (ölçüm etiketi ayrışması); 67:3 'rahmân' orta konum, mühür yok",
  "harf alanı: ayet 1 ölçümünde harf 52 → harf3 32, isaret 0 (önceki sûrelerin ayet 1 ailesi); araç alanı (aday 924); KAPATILAMAZ",
  "kök tablosu: kok_ekle_67 2 kök (طبق 67:3, gloss korpus 3 ayet; وسق dikey komşuluğunda karşılıksız çıktı — طبق komşusu, gloss korpus 2 ayet; sûre 33 emsali); 1433 → 1435; retroaktif yama hedef 0, yama 0, genel geçiş 0",
  "gloss (1021 ailesi): أيي 'âyet, işaret' — 67:2 'eyyukum' (hangisi); صبح 'sabah; olmak' — 67:5 'mesâbîh' (kandiller); بأس 'şiddet, azap; savaş gücü' — 67:6 'bi'se' (ne kötü); قلب 'çevirme; kalp' — 67:4 'yenqalib' (dönme), ◈B tetiği kök düzeyinde",
  "ölçüm kip (517 ailesi): 67:2 'eyyukum' INTG sayılıyor, cümle haber + amaç; 67:4 emir + meczum cevap şart anlamı COND olarak çıkmıyor; 67:7 'izâ' şart-zaman kip yok; 67:1 'biyedihi'l-mulk' ve 67:6 haberin öne alınması biçim alanında yok",
  "biçim / iltifât (1017 ailesi): 67:1 3MS → 67:2 2MP → 67:3-4 2MS → 67:5 1P ('zeyyennâ') → 67:6-10 3MP; 67:8-9 alıntı içinde 2MP; ölçüm iltifât 0 (blok içi)",
  "yıldız (924): 67:6 ★★ rab z=2,72 (7 kelimede 1 Rab), 67:7 ★ pas z=1,57 — içerik iddiası değil",
  "sayı işareti: 67:3 'seb'' gerçek sayı (yedi); 67:4 'kerrateyn' ikil, ölçüm sayı işareti vermiyor",
  "aktör (1038 ailesi): 67:5 'şeytan' adlı (tür adı, rol mecrur), 67:6 'cehennem' adlı yer; 67:8 bekçiler ve bölük, 67:9-10 konuşan cehennemlikler ölçümde 'aktör yok'",
  "adsız (aday 1017): 67:1-3 mevsûl 'ellezî' göndergesi (67:3 'er-rahmân' adla), 2MP / 2MS muhatap, 1P konuşan (67:5), 'nezîr', bekçiler, bölük, cehennemlikler — ad verilmedi; 67:9 'in entum illâ fî dalâlin kebîr' cümlesinin konuşanı metinde işaretli değil, KAPATILAMAZ",
  "çıpa: 67:2 L0, 67:3 L1, 67:4 L1, 67:5 L1 (olgu); 67:6-8, 67:10 olgu değil (âhiret); tarayıcı v4 adayları 67:2, 67:3 — ikisi de çıpa değil; L4 yok",
  "dikey (924): n küçük köklerde ×kat şişmesi (67:3 طبق komşusu وسق ×2692,9 tek ayet) — tablo değeri bulgu değil",
  "fâsıla: blok içi on ayet ر (ölçüm R sınıfı); kafiye kırığı 0 (blok içi)",
  "aday 1040 (kayıt): 66:12 → 67:1 sûre sınırı — örnek anlatısıyla kapanış ('mine'l-qânitîn') / övgüyle açılış ('tebâreke'); fâsıla ن → ر; iki ayetin ölçüm kökleri ortak değil; 66:9 / 67:6 'cehennem … bi'se'l-masîr' ardışık sûre; 64:1 / 67:1 'mulk' + 'alâ kulli şey'in qadîr' ve 65:12 / 67:3 'ellezî haleqa seb'a semâvât' (ardışık değil, okuma bağı); test yok",
  "aday 1041 (kayıt): blokta vaka yok ('kebîr' 67:9'da yalnız sapıklık için)",
  "karşıt çift (aday 1039, okuma): 67:2 ölüm / hayat; 67:9 onay / yalanlama; öbür sekiz ayette yok",
  "tetik: ön kuru koşu 0 uyuşmaz; kayıtta 0; [x/y] 0 (86 sayım)",
 ],
 (11, 20): [
  "esmâ: e_oto 7 token (67:12 'kebîr'; 67:13 'alîm'; 67:14 'latîf', 'habîr'; 67:19 'rahmân', 'basîr'; 67:20 'rahmân'); 'kebîr' DEĞİL (ecrin sıfatı), öbür altısı İLÂHÎ; KARAR 640 → 647; bilanço geçerli mühür 67:13, 14, 19, 20; 67:12 esma_kayit mühür EVET, karar sonrası geçersiz (1022)",
  "esmâ mühür / ölçüm ayrışması: 67:13 ve 67:19 ölçüm satırı 'MÜHÜRSÜZ', bilanço geçerli; 67:20 'rahmân' ölçümde ORTA konum (ayet 'ğurûr' ile bitiyor) ama bilanço geçerli mühür — mühür ölçütü 'son konum' etiketiyle ayrışıyor; 67:13 'alîm'i 'bi-zâti's-sudûr' izliyor (konum metinden; 1022)",
  "ölçüm kip (517 ailesi): 67:17 'em emintum' soru INTG olarak çıkmıyor (yalnız FUT); 67:12 ve 67:13 tekit 'inne' kip alanında yok; 67:11 'fe-suhqan' beddua kip yok; 67:15 'ileyhi'n-nuşûr' haber öne alınması biçim alanında yok",
  "biçim / iltifât (1017 ailesi): 67:10 1P → 67:11 3MP; 67:12 3MP → 67:13 2MP → 67:14 3MS → 67:15-17 2MP → 67:17-18 1S ('nezîr', 'nekîr' düşmüş zamir) → 67:18-19 3MP → 67:20 2MP; ölçüm iltifât 0 (blok içi)",
  "gloss (1021 ailesi): نكب 'sapma, yoldan çıkma; omuz' — 67:15 'menâkib' (sırtlar); نذر 67:17 'nezîr' 1S 'uyarım' anlamında (67:8-9 'uyarıcı')",
  "nakarat3 (1003): 67:16 / 67:17 'emine + men + fî + semâ'' GEÇER (ikisi blok içi); 67:20 'em-men + zâ + ellezî' GEÇMEZ, eşi 67:21 henüz okunmadı (defterden)",
  "yıldız (924): 67:12 ★★ rab z=2,05 (9 kelimede 1 Rab) — içerik iddiası değil",
  "adsız (aday 1017): 'men fi's-semâ'' (67:16, 17), 1S konuşan (67:17-18), 'men haleqa' (67:14; fail / meful belirsiz, KAPATILAMAZ), öncekiler (67:18), 'cund' (67:20), 67:11 'fe-suhqan' konuşanı — ad verilmedi",
  "çıpa: 67:15 L1, 67:16 L1 (L2 koluna sınırda), 67:17 L0, 67:19 L1 (L2 koluna sınırda); tarayıcı v4 adayı 67:19 — çıpa değil; L4 yok",
  "fâsıla: blok içi on ayet ر (ölçüm R sınıfı); kafiye kırığı 0 (blok içi)",
  "aday 1040 (kayıt): blokta ardışık sûre bağı yok; 35:25-26 / 67:18 ve 35:7 / 67:12 ardışık değil, okuma bağı",
  "aday 1041 (kayıt): kök بصر 67:3-4 'el-basar' (insan bakışı) / 67:19 'basîr' (ilâhî sıfat) — kelime değil kök düzeyinde, sınır vakası; كبر 67:9 'dalâlin kebîr' / 67:12 'ecrun kebîr' — ikisi de Allah için değil",
  "karşıt çift (aday 1039, okuma): 67:13 gizleme / açığa vurma; 67:16 gök / yer; 67:19 kanat açma / kapama; 67:12 ayet içinde yok, 67:11 / 67:12 ardışık ayetlerde; öbür altı ayette yok",
  "tetik: ön kuru koşu 0 uyuşmaz; kayıtta 0; [x/y] 0 (80 sayım)",
 ],
 (21, 30): [
  "esmâ: e_oto 3 token (67:26 'mubîn'; 67:29 'rahmân', 'mubîn'); iki 'mubîn' DEĞİL (uyarıcının ve sapıklığın sıfatı), 'rahmân' İLÂHÎ; KARAR 647 → 650; bilanço geçerli mühür 67:29 — ayetin son esmâ tokeni 'mubîn' DEĞİL kararlı, 'rahmân' 3. kelimede: mühür ölçütü karar sonrası konumla ayrışıyor; 67:26 esma_kayit mühür EVET, karar sonrası geçersiz (1022)",
  "fâsıla (924): 67:1-21 ر, 67:22 م, 67:23-27 ن, 67:28 م, 67:29-30 ن — R → N sınıf geçişi 67:22'de; bilanço kafiye kırığı 0 (sûre 64 dersi: fâsıla iddiası ayet ayet harften)",
  "ölçüm biçim (517 ailesi): 67:26 'innemâ' ×2 hasrı HASR olarak çıkmıyor; 67:22 mesel / karşılaştırma biçim alanında yok; 67:24, 67:29 haber / câr öne alınması yok",
  "esit2 / sıralı eşleşme: 67:23 ↔ 23:78 BENZER 0,9263, 67:24 ↔ 23:79 BENZER 0,9492 — iki ayet aynı sırayla; ardışık sûre değil, okuma bağı (1040 alanına değil); 67:25 YAKIN ×5, BENZER ×1",
  "nakarat3 (1003): 67:20 / 67:21, 67:23 / 67:24, 67:28 / 67:30 — üç çift, hepsi GEÇMEZ, hepsi sûre içi ve okundu",
  "harekesiz kalıp gürültüsü (sûre 41 dersi): 67:27 'teddeûn' — sayı lemmadan",
  "kök tetik (◈B): 67:30 عين 'ma'în' (akan su) organ anlamı değil, tetik kök düzeyinde (67:4 قلب emsali)",
  "gloss (1021 ailesi): صبح 'sabah; olmak' — 67:30 'asbaha' (oluverme); بين 'arası; açıklama' — 67:26, 67:29 'mubîn' (apaçık)",
  "yıldız (924): 67:24 ★ pas z=1,57, 67:26 ★ allah z=1,69, 67:27 ★ pas z=1,57 — içerik iddiası değil",
  "sayı işareti (924): 67:23 'qalîl' — sayı değil",
  "biçim / konuşan (1017 ailesi): 67:23-30 'qul' altı ayette; 'qul' muhatabı 2MS 67:26 1S 'ene', 67:28 1S / 1P, 67:29 1P olarak konuşuyor — adlanmıyor; 67:25 3MP konuşanlar ve 67:27 'qîle' konuşanı adsız; ölçüm iltifât 0",
  "çıpa: 67:23 L1, 67:24 L0, 67:30 L2 (yeti sınırı kolu); 67:22 mesel, 67:27 âhiret olgu değil; tarayıcı v4 adayı 67:30 — çıpa değil; L4 yok",
  "aday 1040 (kayıt): blokta ardışık sûre bağı yok; sûre sonu 67:30 → 68:1 sınırı sûre 68 okunurken yazılacak (henüz okunmadı)",
  "aday 1041 (kayıt): kök رحم 67:28 'rahimenâ' (Allah'ın fiili) / 'er-rahmân' — aynı gönderge, vaka değil; بين 'mubîn' 67:26 uyarıcı, 67:29 sapıklık — ikisi de Allah için değil; vaka yok",
  "karşıt çift (aday 1039, okuma): 67:22 yüzüstü / dimdik; 67:24 yayma / toplanma; 67:26 bilgi Allah katında / ben uyarıcıyım; 67:28 helâk / merhamet; 67:30 çekilmiş su / akan su; öbür beş ayette yok",
  "tetik: ön kuru koşu 0 uyuşmaz; kayıtta 0; [x/y] ilk koşuda 1 uyuşmaz (67:22 başka ayetin sayısı [x/y] biçiminde) — kayıttan önce düzeltildi, son koşu 0 (87 sayım)",
 ],
}

DUZELTME = {
}
