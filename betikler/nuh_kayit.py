# -*- coding: utf-8 -*-
"""nuh_kayit.py — sûre 71 (Nûh) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 71

CIPA = {
 # blok 1-10
 4: dict(kademe='L0', olgu=True, cipa=False, not_="'yu'ahhirkum ilâ ecelin musemmâ … inne ecela'llâhi izâ câ'e lâ yu'ahhar' — ömrün sonu (ecel) adlanıyor, süreç / ölçü yok — L0 (63:11 emsali, aynı kurgu); tarayıcı v4 adayı, çıpa değil"),
 5: dict(kademe='L0', olgu=True, cipa=False, not_="'de'avtu qavmî leylen ve nehârâ' — gece / gündüz yalnız zaman zarfı olarak adlanıyor; süreç / ölçü yok — L0 (40:46 emsali); tarayıcı vermedi"),
 7: dict(kademe='L1', olgu=True, cipa=False, not_="'ce'alû esâbi'ahum fî âzânihim' — organ adları (parmak, kulak) + eylem; işlev / mekanizma yok — L1 (organ + eylem emsali); 2:19 aynı jest benzetme içinde; tarayıcı vermedi"),
 # blok 11-20
 11: dict(kademe='L1', olgu=True, cipa=False, not_="'yursili's-semâ'e aleykum midrârâ' — gök + bol yağış fiili; mekanizma / ölçü yok — L1; tarayıcı vermedi"),
 12: dict(kademe='L0', olgu=True, cipa=False, not_="'cennât' (bahçeler), 'enhâr' (ırmaklar) adlanıyor; süreç / ölçü yok — L0; mal ve oğullar doğal olgu değil; tarayıcı vermedi"),
 14: dict(kademe='L1', olgu=True, cipa=False, not_="'halaqakum atvârâ' — insanın evre evre yaratılışı; evreler çoğul, adsız, sırasız; mekanizma yok — L1 (39:6 emsali; 23:14 adlı aşamalardan ayrı); tarayıcı vermedi"),
 15: dict(kademe='L1', olgu=True, cipa=False, not_="'seb'a semâvâtin tibâqâ' — yedi gök (sayı) kat kat (düzen), gözlem çağrısı 'e-lem teraw'; birim / mekanizma yok — L1 (67:3 emsali); L4 sınıf / ölçü koluna sınırda, KAPATILAMAZ; tarayıcı v4 adayı, çıpa değil"),
 16: dict(kademe='L1', olgu=True, cipa=False, not_="'ce'ale'l-qamera fîhinne nûran ve ce'ale'ş-şemse sirâcâ' — ay ve güneş işlev adıyla (ışık, kandil), göklerde; mekanizma / ölçü yok — L1 (10:5'te ölçü kolu 'menâzil … adede's-sinîn' var, burada yok); tarayıcı vermedi"),
 17: dict(kademe='L1', olgu=True, cipa=False, not_="'enbetekum mine'l-ardi nebâtâ' — insanın yerden oluşu süreç fiiliyle; aşama / mekanizma yok; 'nebâtâ' mef'ûl mutlak, benzetme sınırı — L1; tarayıcı vermedi"),
 18: dict(kademe=None, olgu=False, cipa=False, not_="'yu'îdukum fîhâ ve yuhricukum ihrâcâ' — yere dönüş ve çıkarılış; çıkarılış diriliş (gaybî, olgu=False); yere dönüş kolu doğal — sınır vakası, merdiven uygulanmadı (20:55 aynı üçlü); tarayıcı vermedi"),
 19: dict(kademe='L1', olgu=True, cipa=False, not_="'ce'ale lekumu'l-arda bisâtâ' — yer + işlev adı; mekanizma / ölçü yok — L1 (43:10 emsali); tarayıcı vermedi"),
 20: dict(kademe='L1', olgu=True, cipa=False, not_="'li-teslukû minhâ subulen ficâcâ' — yer üzerindeki geniş yollar, işlev ta'lîli; mekanizma yok — L1 (43:10 emsali); tarayıcı vermedi"),
 # blok 21-28
 25: dict(kademe=None, olgu=False, cipa=False, not_="'uğriqû fe-udhilû nârâ' — boğulma cezası (tarihî olay, gerekçesi 'hatî'ât') ve ateş (âhiret, olgu=False); merdiven uygulanmadı (37:82 emsali); tarayıcı vermedi"),
 27: dict(kademe='L0', olgu=True, cipa=False, not_="'ve lâ yelidû illâ fâciran keffârâ' — doğurma (insan üremesi) adlanıyor, şarta bağlı öngörü; süreç / ölçü yok — L0; ◈B tetik listesinde ولد yok; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: e_oto 2 token (71:2 'mubîn' — Nûh'un kendini nitelemesi, DEĞİL; 71:10 'ğaffâr' — Rab, İLÂHÎ); KARAR 656 → 658; esma_kayit mühür EVET ×2, karar sonrası geçerli 1 (71:10); ölçüm satırı 71:10'da 'SON konum, MÜHÜRSÜZ' yazıyor — bilanço geçerli sayıyor (1022)",
  "kök tablosu: kok_ekle_71 0 kök (blok_dikey 'karşılık eksiği yok'); 1451 değişmedi; retroaktif yama hedef 0, yama 0, genel geçiş 0",
  "yıldız (924): 71:3 ★★★ allah z=3,47 (5 kelimede 1 lafız), 71:5 ★★ rab z=2,72, 71:10 ★★★ rab z=3,23 — içerik iddiası değil; öbür yedi ayet yıldızsız",
  "harf alanı: ayet 1 ölçümünde harf 72 → harf3 51, isaret 0 (ayet 1 ailesi; besmele sayılıyor olabilir); araç alanı (924); KAPATILAMAZ",
  "fâsıla / kafiye (924): fâsıla م (71:1), ن (71:2-4), ا (71:5-10); ölçüm kafiye kırığı 0 — 71:1 → 71:2 (م → ن) ve 71:4 → 71:5 (ن → ا) geçişleri işaretsiz (sûre 64 dersi); fâsıla iddiası ayet ayet harften",
  "ölçüm kip (517 ailesi): 71:1, 71:2, 71:4, 71:5, 71:7, 71:8, 71:9, 71:10 tekit 'inne' kip alanında yok; 71:5 harfsiz nidâ 'rabbi' VOC olarak yok (71:2 'yâ qavmi' VOC var); 71:6 HASR var",
  "ölçüm iltifât: 71:5'te muhatap kavimden Rabbe, 71:10'da alıntı içi 1S → 2MP — iltifât sayılmıyor (konuşma katmanı değişimi, araç alanı, 924)",
  "esit2 / xref: blokta esit2 yok; 71:1 xref 8:32 (henüz okunmadı) ve okunmuş 3 ayet; 71:2 xref 11:25, 71:3 xref 29:16, 71:4 xref 14:10, 71:7 xref 2:19 (okundu, basıldı); 71:5 xref okunmuş 1 ayet; 71:10 xref okunmuş 2 ayet; 71:6, 71:8, 71:9 bağ yok; lemma dizisi eşi 7:59 henüz okunmadı",
  "adsız (aday 1017): 71:1 1P gönderen 'innâ' — ad verilmedi; 71:2 ve 71:5 'qâle' 3MS en yakın ad 71:1 Nûh (okuma); 71:7 2MS muhatap Rab (71:5 nidâsından, okuma); kavim adlanmıyor, yalnız 'qavmihî / qavmî'",
  "çıpa: 71:4 L0 (ecel, ömrün sonu; 63:11 emsali) — tarayıcı v4 adayı, çıpa değil; 71:5 L0 (gece / gündüz zaman zarfı; 40:46 emsali); 71:7 L1 (organ + eylem); L4 yok",
  "◈B tetik listesi dışı organ (ön-kayıt §4): 71:7 parmak (صبع), kulak (أذن) — satır '—', gözlem ◇'de",
  "aday 1040 (kayıt): 70:44 'zâlike'l-yevmu'llezî kânû yû'adûn' / 71:1 'innâ erselnâ nûhan … azâbun elîm' — sûre sınırı; fâsıla ن → م; test yok",
  "aday 1041 (kayıt): blokta vaka yok — 71:2 'mubîn' insan nitelemesi (esmâ DEĞİL), sûre içinde şimdiye dek Allah için 'mubîn' yok; kök غفر Allah'ın fiili (71:4, 71:7) ve sıfatı (71:10) ile kavmin dileği (71:10 'isteğfirû') — aynı kelime değil",
  "karşıt çift (aday 1039, okuma): 71:4 'yu'ahhirkum' / 'lâ yu'ahhar'; 71:5 gece / gündüz; 71:9 'a'lentu' / 'esrartu' ve 71:8 'cihârâ' / 71:9 'isrârâ'; öbür altı ayette yok",
  "tetik: ön kuru koşu 2 uyuşmaz (71:4 ◈K أجل; 71:5 ◈K ليل نهر — satırlar dolduruldu); kayıtta 0; [x/y] 0 (60 sayım)",
 ],
 (11, 20): [
  "esmâ: e_oto 1 token (71:16 'nûr' — ayın nitelemesi, DEĞİL); KARAR 658 → 659; esma_kayit mühür EVET, karar sonrası geçersiz (1022); blokta geçerli mühür yok",
  "kök tablosu: kok_ekle_71 0 kök (blok_dikey 'karşılık eksiği yok'); 1451 değişmedi; retroaktif yama hedef 0, yama 0, genel geçiş 0",
  "yıldız (924): 71:13 ★★ allah z=2,80, 71:15 ★ allah z=1,97, 71:17 ★★★ allah z=3,47, 71:19 ★★★ allah z=3,47 — kısa ayette tek lafız; içerik iddiası değil; öbür altı ayet yıldızsız",
  "gloss (1021 ailesi): طور 71:14 'atvâr' (evreler) — gloss 'Tûr dağı'; بني 71:12 'benîn' (oğullar) — gloss 'bina, yapma'; نهر 71:5 'nehâr' (gündüz) — gloss 'ırmak' (71:12 'enhâr' ile doğru); وقر 71:13 'veqâr' — gloss kulak ağırlığı ile birlikte; sayı verilmedi",
  "sayı işareti: 71:15 'seb'' — gerçek sayı (gök sayısı)",
  "◈K tetik dışı ışık sınıfı (S1 'uygulanmayanlar'): 71:16 'nûr', 'sirâc' — gözlem ◇'de; satır ay / güneş tetiğiyle dolu",
  "◈B: 71:15 tetik خلق göklerin yaratılması (canlı yok) — satır dolu, 'canlı yok' notu (◈B kök düzeyi tetik kuralı); 71:18 dönüş / çıkarılış tetik dışı — satır '—'",
  "ölçüm kip (517 ailesi): 71:11, 71:12 meczûm cevaplar (71:10 emrinin) kip alanında yok (71:4'te COND vardı); 71:20 ta'lîl 'li' kip alanında yok",
  "fâsıla: 71:11-20 hepsi ا (71:5'ten bu yana on altı ayet); ölçüm kafiye kırığı 0",
  "esit2 / xref: blokta esit2 yok; 71:11 xref 6:6 (henüz okunmadı), 11:52 (okundu, basıldı); 71:12 xref 17:6 (basıldı) ve okunmuş 1 ayet; 71:15 xref 67:3 (basıldı); 71:19 xref okunmuş 1 ayet; 71:13, 71:14, 71:16, 71:17, 71:18, 71:20 bağ yok; lemma eşleri 2:29, 84:19, 88:17, 78:13 henüz okunmadı",
  "adsız (aday 1017): 71:11-20 özne 3MS — 71:10 'rabbekum' göndergesi (okuma), 71:13'ten lafız; kavim adlanmıyor; 71:16 'fîhinne' → 71:15 gökler, 71:18 'fîhâ' ve 71:20 'minhâ' → yer (okuma)",
  "çıpa: L1 71:11 (gök + yağış), 71:14 (evreler), 71:15 (yedi gök; 67:3 emsali, L4 sınırda, KAPATILAMAZ — tarayıcı v4 adayı, çıpa değil), 71:16 (ay / güneş), 71:17 (yerden bitirilme), 71:19 (yer 'bisât'), 71:20 (yollar); L0 71:12 (bahçe, ırmak); 71:18 olgu=False (diriliş; yere dönüş kolu sınır vakası); L4 yok",
  "aday 1040 (kayıt): blokta sûre sınırı yok; vaka yok",
  "aday 1041 (kayıt): kök / lemma 'ce'ale' — 71:7 kavmin fiili ('ce'alû esâbi'ahum') / 71:12, 71:16, 71:19 Allah'ın fiili; aynı sûrede aynı kelime iki öznede; kayıt, test yok",
  "karşıt çift (aday 1039, okuma): 71:16 ay / güneş; 71:18 'yu'îdukum fîhâ' / 'yuhricukum'; öbür sekiz ayette yok",
  "tetik: ön kuru koşu 9 uyuşmaz (71:11 ◈K سمو; 71:12 ◈K نهر; 71:14 ◈B خلق; 71:15 ◈K سمو ◈B خلق; 71:16 ◈K قمر شمس; 71:17 ◈K أرض ◈B نبت; 71:19 ◈K أرض — satırlar dolduruldu); kayıtta 0; [x/y] 0 (50 sayım)",
 ],
 (21, 28): [
  "esmâ: e_oto 3 token (71:25 'nasîr' — 'ensâr' insan / yardımcı çoğulu; 71:28 'mu'min' ×2 — insanlar); üçü DEĞİL; KARAR 659 → 662; esma_kayit mühür EVET 1 (71:25), karar sonrası geçersiz (1022); blokta geçerli mühür yok",
  "kök tablosu: kok_ekle_71 1 kök (نسر 71:23, put adı, gloss korpus 1 ayet; blok_dikey 'KARŞILIK YOK' → eklendi); 1451 → 1452; retroaktif yama hedef 0, yama 0, genel geçiş 0",
  "hapaks (yeni kök dersi): 71:23 ★★★ hapaks z=3,28 — yeni kökün tek tokeni; içerik iddiası değil",
  "yıldız (924): 71:25 ★★★ pas z=3,48 (3 fiilde 2 edilgen), 71:26 ★ rab z=1,81 — içerik iddiası değil; 71:21 ve 71:28'de Rab var, yıldız yok (uzun ayet); öbür dört ayet yıldızsız",
  "kök / lafız: أله [7/8] 71:23 'âlihetekum' kök sayımı — lafız değil; sûrede lafız 7 token (bilanço: 2 + 4 + 1), kök أله 8",
  "gloss (1021 / özel ad iskeleti): ودد 71:23 'vedd' — gloss 'sevgi'; سوع 71:23 'suvâ'' — gloss 'saat'; put adları kök glossuyla çakışıyor (gloss_gecis özel ad iskeleti bekleyen kararına ek vaka; araç değişmedi)",
  "gloss (1021): نور 71:25 'nâr' (ateş) — gloss 'nûr, ışık; nâr, ateş' iki anlam birlikte; 71:16 'nûr' ile aynı kök",
  "lemma eşsesli (sûre 69 / 60 dersi): 71:21 lemma 'asâ' değnek ve isyan geçişlerini birleştiriyor — kök عصي sayısı verildi (32 ayet)",
  "sayı işareti: 71:24 'kesîr' — sayı değil, nicelik sıfatı (sûre 58 dersi ailesi; kök kaynaklı yanlış alarm)",
  "ölçüm kip (517 ailesi): 71:23 nehy 'lâ tezerunne' biçim NEHY olarak yok (71:24, 71:26, 71:28'de var); 71:21, 71:26, 71:28 harfsiz nidâ 'rabbi' VOC yok",
  "ölçüm iltifât: 71:25 Nûh'un sözünden anlatıcı sesine geçiş (3MP edilgen) ve 71:26'da dönüş iltifât sayılmıyor (araç alanı, 924)",
  "nakarat3: 71:21 / 71:26 'qâle nûhun rabbi' GEÇMEZ (3 kelime); 71:24 / 71:28 'lâ tezidi'z-zâlimîne illâ' GEÇER — sûre içi",
  "esit2 / xref: blokta esit2 yok; 71:25 xref 4:123, 4:173 (henüz okunmadı) ve okunmuş 1 ayet; 71:28 xref 14:41 (okundu, basıldı); öbür altı ayette xref yok",
  "adsız (aday 1017): 71:21 'men', 71:22-23 3MP (kurnazlık eden / konuşan), 71:23 2MP muhatap, 71:24 'edallû' öznesi (adlar mı konuşanlar mı belirsiz), 71:25 edilgen fail — ad verilmedi; metnin adladıkları (Nûh, beş put adı) adıyla anıldı",
  "çıpa: 71:27 L0 (doğurma, şarta bağlı); 71:25 olgu=False (boğulma cezası, ateş; 37:82 emsali); 71:26 'ale'l-ard' mekân — merdiven yok; tarayıcı adayı yok; L4 yok",
  "◈B tetik dışı: 71:27 ولد (doğurma), 71:25 boğulma — satır '—' (ön-kayıt §4)",
  "fâsıla: 71:21-28 hepsi ا; sûre: م (71:1), ن (71:2-4), ا (71:5-28); ölçüm kafiye kırığı sûrede 0 (iki geçiş işaretsiz, blok 1-10 ARIZA)",
  "aday 1040 (kayıt): 71:28 → 72:1 yazılmadı (72 henüz okunmadı)",
  "aday 1041 (kayıt): lemma 'zâde' — 71:6 öznesi çağrı, 71:21 mal ve çocuk, 71:24 ve 71:28 Rab (2MS); lemma 'vezera' — 71:23 kavmin yasağı 'lâ tezerunne', 71:26-27 Rabbe 'lâ tezer', 'in tezerhum'; iki vaka, kayıt, test yok",
  "karşıt çift (aday 1039, okuma): 71:21 isyan / uyma; 71:27 'ibâdeke' / 'fâciran keffârâ'; 71:28 mü'minler / zalimler, 'iğfir' / 'tebârâ'; öbür beş ayette yok",
  "tetik: ön kuru koşu 1 uyuşmaz (71:26 ◈K أرض — satır dolduruldu); kayıtta 0; [x/y] 0 (66 sayım)",
 ],
}

DUZELTME = {
 10: dict(alan='meal', eski="çünkü O çok bağışlayıcıdır.'",
          dogru="Meal sonundaki kapanış tırnağı yanlış: 71:10 'fe-qultu' alıntısı 71:11-12 meczûm cevaplarıyla sürüyor (okuma); doğrusu 'Dedim ki: Rabbinizden bağışlanma dileyin; çünkü O çok bağışlayıcıdır;' — tırnak kapanmaz. Özgün alan korunur.",
          aday=1017, blok='1-10'),
 20: dict(alan='meal', eski="geniş yollarda yürüyesiniz.'",
          dogru="Meal sonundaki kapanış tırnakları okunmamış ayete dayalı alıntı sınırı varsayımı: alıntının sonu henüz okunmadı (71:20 ◈A ile çelişiyor); doğrusu 'ki orada geniş yollarda yürüyesiniz.' — tırnaksız. Özgün alan korunur.",
          aday=1017, blok='11-20'),
}
