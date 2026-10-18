# -*- coding: utf-8 -*-
"""tur_kayit.py — sûre 52 (Tûr) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 52

CIPA = {
 # blok 1-10
 1: dict(kademe=None, olgu=False, cipa=False, not_="'ve't-Tûr' — metindeki yer adı, yemin nesnesi; nitelik / süreç yok, doğal olgu iddiası değil; tarayıcı vermedi"),
 5: dict(kademe='L1', olgu=True, cipa=False, not_="'es-saqfi'l-merfû'' — tavan + nitelik (yükseltilmiş); tavanın gök olduğu 52:5 metninde yok (21:32 'saqfen mahfûzâ' okundu; bağ KAPATILAMAZ); süreç / ölçü yok — L1; tarayıcı vermedi"),
 6: dict(kademe='L1', olgu=True, cipa=False, not_="'el-bahri'l-mescûr' — deniz + nitelik; 'mescûr' iki okumalı (dolu / tutuşturulmuş; 40:72 'yuscerûn' okundu) — seçim KAPATILAMAZ; süreç / ölçü / mekanizma yok — L1; tarayıcı vermedi"),
 9: dict(kademe='L1', olgu=True, cipa=False, not_="'yevme temûru's-semâ'u mevrâ' — gök + hâl (çalkalanma), gelecekteki gün sahnesi; mekanizma / ölçü yok (39:69 kıyamet sahnesi emsali L1); doğal süreç iddiası KAPATILAMAZ; tarayıcı vermedi"),
 10: dict(kademe='L1', olgu=True, cipa=False, not_="'ve tesîru'l-cibâlu seyrâ' — dağlar + hâl (yürüme), aynı gün sahnesi; 18:47 'nusayyiru'l-cibâl' okundu; mekanizma / ölçü yok — L1; tarayıcı vermedi"),
 # blok 31-40
 35: dict(kademe=None, olgu=False, cipa=False, not_="'em hulîqû min ğayri şey'' — yaratılış kaynağı sorusu, olgu iddiası değil (soru); tarayıcı vermedi"),
 36: dict(kademe='L0', olgu=True, cipa=False, not_="'em halaqu's-semâvâti ve'l-ard' — gökler ve yer yaratmanın nesnesi olarak adlanıyor, soru içinde; nitelik / süreç yok — L0; tarayıcı vermedi"),
 # blok 41-49
 44: dict(kademe='L1', olgu=True, cipa=False, not_="'kisfen mine's-semâ'i sâqıtan … sehâbun merkûm' — görülen (gökten düşen parça) ile söylenen (yığılmış bulut) ayrılıyor, karşılaştırma yok — L3 koluna sınırda, KAPATILAMAZ (46:24 emsali L1); şart içinde; tarayıcı v4 adayı — aday, çıpa değil"),
 49: dict(kademe='L0', olgu=True, cipa=False, not_="gece ve yıldızların çekilişi tesbih vakti olarak adlanıyor; süreç / ölçü yok — L0 (51:17 emsali); tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: blokta e_oto tokeni yok; mühür ölçümü [] — karar gerekmedi; Rab 1 (52:7 'rabbike', sûre içi [1/7])",
  "aday 1040 alanı: 51:60 → 52:1 (fâsıla ن → ر); 51:1 've'z-zâriyât' / 52:1 've't-Tûr' — ardışık iki sûre 've' yeminiyle açılıyor; 51:6 've inne'd-dîne le-vâqi'' → 52:7 'inne azâbe rabbike le-vâqi'' — iki sûrenin yemin cevabında 'inne + ism + le-vâqi'' — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): yemin eden adlanmıyor; 52:7 muhatap 2MS adsız; 52:9 çalkalandıran, 52:10 yürüten adlanmıyor (18:47'de 1P 'nusayyiru') — KAPATILAMAZ",
  "ölçüm (924): 52:1 harf 25 → harf3 6, n=1 — korpus metninde besmele bitişik, harf sayımı besmeleyi katıyor olabilir (51:1 kaydıyla aynı tür); 52:8 iltifât 1 — 3MS zamir azaba dönüyor, konuşan / muhatap değişmiyor",
  "fâsıla (924): 52:6 fâsıla ر, R sınıfı iken KAFİYE KIRILMASI işaretli; 52:9 ر / ع → ا geçişinde işaret yok — araç davranışı, KAPATILAMAZ",
  "yıldız formülü: 52:3 ★★★ hapaks رقق (kok_ekle_52, 1 token); 52:7 ★★★ rab z=5,01 (4 kelimede 1 Rab) — bilinen davranış, içerik iddiası değil",
  "yıldız etiketi (1001): 52:5 ve 52:6 ★ kafiye kırığından, bilanço kaynağı 'n' z=-1,11",
  "biçim (517 ailesi): 52:1-6 yemin 've' ölçümde işaretsiz (kip yok; 51:4'te QASEM işaretliydi); 52:9-10 mef'ûl-i mutlak paralelliği ölçümde yok; 52:7 EMPH, 52:8 NEG işaretli",
  "gloss (1021 ailesi): رقق 'ince deri, parşömen' (kok_ekle_52) — tek geçiş, korpus içinden doğrulanamaz; سجر 'tutuşturma / dolup taşma' — 52:6 'mescûr' için seçim KAPATILAMAZ; عمر 'ömür; imar etme' — 52:4 'ma'mûr' imar anlamında, ◈K / ◈B tetikliyor (satır dolu, zaman / canlı yok)",
  "okuma: 19:52, 20:80, 23:20, 28:29, 28:46 → 52:1; 17:58, 33:6 → 52:2; 17:13 → 52:3; 21:32, 16:26, 43:33 → 52:5; 40:72 → 52:6; 17:57, 21:46, 42:22, 51:6 → 52:7; 34:18, 13:31, 18:47 → 52:10 — KAPATILAMAZ",
  "tetik: ön kuru koşu 5 tetik satırı (52:4 عمر ◈K ve ◈B; 52:6 بحر; 52:9 يوم سمو; 52:10 جبل) — ilk koşuda 0 uyuşmaz; [x/y] ilk koşuda 0 (20 sayım)",
 ],
 (11, 20): [
  "esmâ: blokta e_oto tokeni yok; mühür ölçümü [] — karar gerekmedi; Rab 2 (52:18 'rabbuhum' ×2, sûre içi [2,3/7])",
  "çıpa: blokta doğal olgu yok (ateş / bahçe sahnesi) — CIPA kaydı açılmadı; tarayıcı vermedi",
  "aday 1040 alanı: 51:60 'fe-veylun' → 52:11 'fe-veylun'; 51:13 → 52:13 ('yevme' + edilgen + ateş); 51:14 → 52:14 ('hâzâ / hâzihi … ellezî / elletî kuntum bihî / bihâ'); 51:15 → 52:17 (esit2 BENZER); 51:16 → 52:18 — 'mâ âtâhum rabbuhum' lemma dizisi korpusta yalnız bu iki ayette — kayıt, test yok",
  "aday 1041 alanı (kök düzeyi): وقي 52:17 'muttaqîn' sakınanlar / 52:18 'veqâhum' Rab korur — aynı kelime değil, kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 52:13 iten, 52:16 karşılık veren (edilgen) adsız; 52:14-16 ve 52:19 alıntılarını söyleyen adsız, alıntı sınırları ölçümde işaretsiz; 52:20 1P 'zevvecnâhum' adsız — KAPATILAMAZ",
  "yıldız formülü: 52:13 ★★★ pas z=5,38 (edilgen gerçek); 52:18 ★★★ rab z=5,01 (8 kelimede 2 Rab) — bilinen davranış, içerik iddiası değil",
  "biçim (517 ailesi): 52:11 beddua 'veyl', 52:16 hasr 'innemâ', 52:17 tekit 'inne' ölçümde işaretsiz; 52:14-15 DIKKAT, 52:15 INTG, 52:16 NEHY işaretli",
  "gloss (1021 ailesi): فكه 'meyve; şakalaşma' — 52:18 'fâkihîn' (keyif süren) kapsanmıyor olabilir; سرر 'sır, gizleme' — 52:20 'surur' (tahtlar) kapsanmıyor; araç dondurulmuş, boşluk kanıt değil (924)",
  "esit2: 52:17 → 15:45, 51:15 BENZER 0,8889 (okundu), 54:54 BENZER (henüz okunmadı); 52:19 → 77:43 TAM (henüz okunmadı)",
  "okuma: 51:60, 16:36, 43:25 → 52:11; 9:65, 43:83 → 52:12; 51:13 → 52:13; 32:20, 34:42, 37:21, 51:14 → 52:14; 15:15, 21:3, 27:13, 36:9 → 52:15; 14:29, 17:18, 38:56, 36:64, 14:21, 45:28 → 52:16; 15:45, 51:15 → 52:17; 51:16, 36:55, 44:27, 40:7, 44:56 → 52:18; 44:54, 15:47, 37:44, 43:34, 51:15 → 52:20 — KAPATILAMAZ",
  "tetik: ön kuru koşu 4 tetik satırı (52:11 يوم; 52:13 يوم; 52:15 بصر ◈B; 52:20 زوج عين ◈B) — ilk koşuda 0 uyuşmaz; [x/y] ilk koşuda 0 (39 sayım); kayıttan önce 52:15 karşıt çift notu sadeleştirildi",
 ],
 (21, 30): [
  "esmâ: 52:28 'el-berr', 'er-rahîm' — 'ned'ûhu' ile çağrılanın sıfatları (52:27 lafız), ölçüm MÜHÜR / esma_kayit EVET → karar 'ilâhî' ×2 (KARAR 455) — karar sonrası bilanço geçerli mühür [28]; lafız 1 (52:27, sûre içi [1/4], sûrenin ilk lafzı), Rab 1 (52:29)",
  'çıpa: blokta doğal olgu yok (52:24 inci teşbihi nesne, süreç değil) — CIPA kaydı açılmadı; tarayıcı vermedi',
  "aday 1040 alanı: 51:28 'ğulâm' → 52:24 'ğilmân'; 51:55 've zekkir' → 52:29 'fe-zekkir'; 51:52 'sâhirun ev mecnûn' → 52:29 'kâhinin ve lâ mecnûn' — kayıt, test yok",
  "aday 1041 alanı: 'berr' lemma — 19:14, 19:32 insan için / 52:28 Allah'ın sıfatı (lemma ayrıca 'kara' anlamında) — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 52:21-22 1P 'elhaqnâ', 'eletnâhum', 'emdednâhum' adsız; 52:26-28 alıntının sonu ölçümde işaretsiz; 52:29 muhatap 2MS adsız; 52:30 söyleyenler 3MP adsız, alıntı içi 1P — KAPATILAMAZ",
  'yıldız formülü: 52:21 ★★★ hapaks ألت (kok_ekle_52, 1 token); 52:27 ★★ allah z=2,80; 52:29 ★★ rab z=2,34 — bilinen davranış, içerik iddiası değil',
  "biçim (517 ailesi): 52:24 teşbih 'ke-enne', 52:26 ve 52:28 tekit 'innâ' / 'innehû' + fasl zamiri 'huve', 52:30 'em' ölçümde işaretsiz; 52:21, 23, 29 NEG işaretli",
  "gloss (1021 ailesi): منن 'lütuf' — 52:30 'reybu'l-menûn' (zamanın felaketi) kapsanmıyor; فكه 52:18 'fâkihîn' / 52:22 'fâkihe' iki anlam; 52:23 'yetenâze'ûn' — 18:21, 20:62 çekişme / burada kadeh paylaşımı (KAPATILAMAZ)",
  "kök çok-anlam (sûre içi): قبل 52:25 'aqbele' (yönelme) / 52:26, 28 'qabl' (önce); جنن 52:17 'cennât' / 52:29 'mecnûn'; منن 52:27 / 52:30",
  'esit2: 52:25 → 37:27, 37:50 TAM (okundu; bağlam 37:22, 23, 24, 43 okundu), 68:30 BENZER (henüz okunmadı)',
  'okuma: 29:12, 47:3, 13:23, 40:8 → 52:21; 36:57, 44:55 → 52:22; 18:21, 20:62, 37:45 → 52:23; 37:49, 51:28, 37:45 → 52:24; 37:27, 37:50 → 52:25; 18:49, 42:22, 21:28, 23:57 → 52:26; 12:90, 28:82, 15:27 → 52:27; 28:53, 19:14, 19:32, 17:67 → 52:28; 15:6, 26:27, 37:36, 44:14, 51:39, 51:52, 51:55 → 52:29; 21:5, 37:36, 26:224, 9:52, 20:135, 23:25 → 52:30 — KAPATILAMAZ',
  "tetik: ön kuru koşu 0 tetik (blokta ◈K / ◈B tetik kökü yok) — ilk koşuda 0 uyuşmaz; [x/y] ilk koşuda 0 (54 sayım); kayıttan önce 52:25'te 37:27 / 37:50 bağlam nitelemesi basılan 37:22, 23, 24, 43'e dayandırıldı",
  "kayıt dosyası (araç değil): 11-20 ARIZA eki virgülün ardına aynı satıra düşmüştü (' ], (11, 20): ['), ekleme çapası kayboldu; 21-30 ekinde yakalandı, satır düzeni onarıldı, içerik eşitliği assert ile doğrulandı",
 ],
 (31, 40): [
  "esmâ: 52:35 'el-hâliqûn' — özne 'hum' (soru), 52:38 'mubîn' — delilin sıfatı; ölçüm MÜHÜRSÜZ / esma_kayit EVET → karar 'değil' ×2 (KARAR 457) — karar sonrası bilanço mühür [35, 38], geçerli []; lafız 0, Rab 1 (52:37)",
  "aday 1040 alanı: 51:53 'bel hum qavmun tâğûn' → 52:32 'em hum qavmun tâğûn' — 'qavm tâğî' lemma dizisi korpusta yalnız bu iki ayette; 51:38 → 52:38 'bi-sultânin mubîn' (lemma dizisi 12 ayet, sûre çiftine özgü değil) — kayıt, test yok",
  "aday 1041 alanı: 'hâliq' lemma — 13:16, 15:28, 23:14, 37:125 Allah için / 52:35 3MP insanlar için soru içinde — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 52:31 'qul' muhatabı 2MS adsız, alıntı içi 1S; 52:33 'teqavvelehû', 52:34 'mislihî' zamirlerinin göndergesi adlanmıyor; 52:35 yaratan (edilgen) adsız; 52:39 'lehu' göndergesi adsız (37:149'da 'li-rabbike') — KAPATILAMAZ",
  "soru dizisi: 'em' 52:30-40'ta 9 ayette 12 token (lemma sayımı; 52:41, 42, 43 henüz okunmadı) — ölçüm 'em'i ayrı biçim olarak işaretlemiyor; 52:32 DIKKAT, 52:33 ve 52:36 IDRAB işaretli (517)",
  'ölçüm (924): 52:39 3MP → 2MP hitap geçişi, 52:40 2MP → 2MS ölçümde iltifât 0',
  'yıldız formülü: 52:35 ★★★ pas z=5,38 (edilgen gerçek); 52:37 ★★ rab z=2,72 — bilinen davranış, içerik iddiası değil',
  "gloss (1021 ailesi): سطر 'satır, yazma; esâtîr' — 52:37 'musaytirûn' (hükmedenler) kapsanmıyor (52:2 'mestûr' ile aynı kök); بني 'bina, yapma' — 52:39 'benât / benûn' kapsanmıyor; حلم 52:32 'ahlâm' akıl / 12:44, 21:5 rüya — seçim KAPATILAMAZ",
  'kök çok-anlam (sûre içi): سطر 52:2 / 52:37; سأل 52:25 / 52:40; ربص 52:30 / 52:31 (karşılıklı bekleme)',
  'esit2: 52:40 → 68:46 TAM (henüz okunmadı)',
  'okuma: 9:52, 20:135 → 52:31; 51:53, 37:30, 12:44, 21:5 → 52:32; 10:38, 11:13 → 52:33; 10:38, 11:13, 37:157, 17:88 → 52:34; 13:16, 15:28, 23:14, 37:125 → 52:35; 13:16 → 52:36; 38:9, 17:100 → 52:37; 51:38, 37:156 → 52:38; 37:149, 37:153, 16:57, 43:16 → 52:39; 36:21, 9:98 → 52:40 — KAPATILAMAZ',
  "tetik: ön kuru koşu 4 tetik satırı (52:35 خلق ◈B; 52:36 سمو أرض ◈K, خلق ◈B; 52:38 سمع ◈B) — ilk koşuda 0 uyuşmaz; [x/y] ilk koşuda 0 (34 sayım); kayıttan önce 52:36'da bu oturumda basılmamış üç ayet anması çıkarıldı",
 ],
 (41, 49): [
  'esmâ: blokta e_oto tokeni yok; mühür ölçümü [] — karar gerekmedi; lafız 2 token 1 ayet (52:43), Rab 2 (52:48 ×2, sûre içi [6,7/7])',
  'çıpa: 52:44 L1 (L3 koluna sınırda, algı / durum ayrımı var, karşılaştırma yok; 46:24 emsali) — tarayıcı v4 adayı, çıpa değil; 52:49 L0',
  "aday 1040 alanı: 51:44 'es-sâ'iqa' → 52:45 'yus'aqûn' (صعق) — kayıt, test yok; 52:49 → 53:1 sınırı sûre 53 okunurken yazılacak (53:1 henüz okunmadı)",
  "aday 1040 alanı DIŞI (ardışık değil, okuma): 50:39-40 → 52:48-49 — 'sabır + sebbih bi-hamdi rabbik + vakit', 'mine'l-leyli fe-sebbihhu ve edbâra / idbâra' iki ayet sırasıyla; esit2 52:49 → 50:40 BENZER 0,9048",
  "aday 1041 alanı (kök düzeyi): كيد 12:76 'kidnâ' (1P) / 52:42 'keyd' insanlar için, 'mekîdûn' edilgen — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 52:42 tuzağa düşüren, 52:45 çarpan, 52:46 yardım eden adsız (edilgen); 52:48 1P 'a'yuninâ' adsız; 52:45, 48, 49 muhatap 2MS adsız; 52:47 'zâlik' göndergesi KAPATILAMAZ",
  "soru dizisi: 'em' 52:30-43'te 12 ayette (52:30, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43; lemma sayımı), 52:43 tenzihle kapanıyor; ölçüm 'em'i işaretlemiyor (517)",
  'yıldız formülü: 52:43 ★★★ allah z=3,92 (9 kelimede 2 lafız); 52:48 ★★★ rab z=3,94; 52:45 ★ pas z=1,57, 52:46 ★★ pas z=2,52 (edilgenler gerçek) — bilinen davranış, içerik iddiası değil',
  "biçim (517 ailesi): 52:42 fasl zamiri 'hum', 52:43 tenzih 'subhâna', 52:47 tekit 'inne' + istidrâk 'lâkinne', 52:48 tekit 'inneke', 52:49 takdim 'mine'l-leyl' ölçümde işaretsiz; 52:44 COND, 52:46 NEG 2 işaretli",
  "kök sûre içi kapanışları: يوم [5/5] 52:46, عذب [4/4] 52:47, ربب [7/7] 52:48, صبر [3/3] 52:48, سبح [3/3] 52:49, كيد [3/3] 52:46, قول [6/6] 52:44, عين [2/2] 52:48 (52:20 'în' / 52:48 'a'yun'), كتب [2/2] 52:41 (52:2 'kitâb' / 'yektubûn')",
  'esit2: 52:41 → 68:47 TAM (henüz okunmadı); 52:49 → 50:40 BENZER (okundu)',
  'okuma: 52:37 → 52:41; 21:70, 37:98, 12:76 → 52:42; 28:68, 28:71 → 52:43; 17:92, 26:187, 34:9, 30:48, 24:43 → 52:44; 43:83, 39:68, 51:44 → 52:45; 44:41, 21:39 → 52:46; 10:55, 44:39, 32:21 → 52:47; 11:37, 23:27, 50:39 → 52:48; 50:40 → 52:49 — KAPATILAMAZ',
  "tetik: ön kuru koşu 6 tetik satırı (52:44 سمو سحب; 52:45 يوم; 52:46 يوم; 52:48 حين ◈K, عين ◈B; 52:49 ليل نجم) — ilk koşuda 0 uyuşmaz; [x/y] ilk koşuda 1 uyuşmaz (52:41 عند — başka ayete ait sayı [x/y] biçimiyle yazılmıştı), düzeltme sonrası 0 (44 sayım); kayıttan önce 52:45'te 51:44 metninde olmayan kavim adı çıkarıldı, 52:41 'onuncu ayet' sayımı 52:30 dizisine sınırlandı",
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_52.py uygular)
DUZELTME = {
 11: dict(alan='mercek', eski="'mukezzib' lemma 21 ayet; okunan 16:36, 43:25 (lemma sayımı)",
          dogru="16:36 ve 43:25 kayıt sırasında bu oturumda AR metni basılmadan 'okunan' diye anıldı (bağ AS_tur '16:36 · 43:25 → 52:11' de 'okundu' diye yazıldı). Metinler sûre sonunda basıldı: ikisinde de 'fe'nzurû / fe'nzur keyfe kâne âqibetu'l-mukezzibîn' — lemma anması doğru, ama kayıt anında görülmemişti. Özgün alan korunur.",
          aday=1017, blok='11-20'),
}
