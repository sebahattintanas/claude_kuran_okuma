# -*- coding: utf-8 -*-
"""qaf_kayit.py — sûre 50 (Qâf) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 50

CIPA = {
 # blok 1-10
 3: dict(kademe=None, olgu=False, cipa=False, not_="'mitnâ ve kunnâ turâben' — inkârcıların alıntılanan sorusu; ölüm → toprak sırası alıntıda, doğal olgu iddiası değil; tarayıcı vermedi"),
 4: dict(kademe='L1', olgu=True, cipa=False, not_="'mâ tenqusu'l-ardu minhum' — yerin (ölüleri) eksiltmesi süreç olarak adlanıyor; aşama, ölçü, mekanizma yok — L1; tarayıcı vermedi"),
 6: dict(kademe='L1', olgu=True, cipa=False, not_="gök: bina edilmiş, süslenmiş, yarıksız ('mâ lehâ min furûc') — nitelik sayımı; süreç / ölçü yok — L1; tarayıcı v4 adayı, çıpa değil"),
 7: dict(kademe='L1', olgu=True, cipa=False, not_="yerin uzatılması, sabit dağlar, her çiftten bitki — adlandırma + nitelik (15:19 emsali); mekanizma yok — L1; tarayıcı vermedi"),
 9: dict(kademe='L2', olgu=True, cipa=False, not_="gökten su → onunla ('bihî') bahçeler ve taneler — nedensel bağ adlanıyor (27:60 emsali) — L2; ölçü / mekanizma yok; tarayıcı vermedi"),
 10: dict(kademe='L1', olgu=True, cipa=False, not_="boylu hurma, dizili tomurcuk — görünüş niteliği; süreç yok — L1; tarayıcı vermedi"),
 # blok 11-20
 11: dict(kademe='L2', olgu=True, cipa=False, not_="su ile ('bihî') ölü beldeyi diriltme — nedensel bağ adlanıyor (43:11, 25:49 emsali) — L2; ardından 'kezâlike'l-hurûc' kıyası (doğal olgudan diriliş çıkarımı, okuma); ölçü / mekanizma yok; tarayıcı vermedi"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="ilk / yeni yaratma — doğal olgu iddiası değil, soru ve idrâb; tarayıcı vermedi"),
 16: dict(kademe='L0', olgu=True, cipa=False, not_="insanın yaratılması adlanıyor (malzeme yok); 'habli'l-verîd' organ adı yakınlık ölçütü olarak — L0; işlev / mekanizma yok; tarayıcı vermedi"),
 19: dict(kademe='L0', olgu=True, cipa=False, not_="'sekratu'l-mevt' ölümün bir hâli adlanıyor — L0; süreç / ölçü yok; tarayıcı vermedi"),
 20: dict(kademe=None, olgu=False, cipa=False, not_="sûra üfleme, tehdit günü — eskatolojik, doğal olgu iddiası değil; tarayıcı vermedi"),
 # blok 21-30
 22: dict(kademe=None, olgu=False, cipa=False, not_="'basaruke'l-yevme hadîd' — perdenin kaldırılması, eskatolojik hitap; doğal olgu iddiası değil; tarayıcı vermedi"),
 # blok 31-40
 38: dict(kademe='L1', olgu=True, cipa=False, not_="gökler, yer ve aradakilerin 'fî sitteti eyyâm' yaratılması — sayı + birim (gün) var, süreç / sıra / mekanizma yok; 'gün'ün ölçü birimi mi dönem mi KAPATILAMAZ — L4 ölçü koluna sınırda, L1 (41:10 emsali); 'mâ messenâ min luğûb' yaratıcı hakkında, doğal olgu değil; tarayıcı vermedi"),
 39: dict(kademe='L0', olgu=True, cipa=False, not_="güneşin doğuşu ve batışı yalnız tesbih vakti olarak adlanıyor; süreç / ölçü yok — L0; tarayıcı vermedi"),
 40: dict(kademe='L0', olgu=True, cipa=False, not_="gece vakit belirteci olarak adlanıyor — L0; tarayıcı vermedi"),
 # blok 41-45
 44: dict(kademe=None, olgu=False, cipa=False, not_="'teşeqqaqu'l-ardu anhum' — diriliş sahnesi, eskatolojik; doğal olgu iddiası değil; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: 50:1 'mecîd' (Kur'ân'ın sıfatı), 50:4 'hafîz' (kitabın sıfatı) — ilâhî değil; ölçüm MÜHÜRSÜZ (sırada ad, SON konum), esma_kayit kararı 'değil' (1022) — karar sonrası bilanço geçerli mühür []",
  "aday 1040 alanı: sûre sınırı 49:18 → 50:1 (fâsıla ن → د; 49:18 'basîrun bimâ ta'melûn' → 50:1 harf + yemin QASEM); 38:1 'Sâd ve'l-Qur'âni zi'z-zikr' / 50:1 'Qâf ve'l-Qur'âni'l-mecîd' ve 38:4 / 50:2 eş açılış (ardışık değil) — kayıt, test yok",
  "aday 1041 alanı: مجد 11:73 'hamîdun mecîd' (Allah) / 50:1 'el-Qur'âni'l-mecîd'; حفظ 42:6, 34:21 'hafîz' (Allah / Rab) / 50:4 'kitâbun hafîz' — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 1P 'alimnâ' (50:4), 'beneynâhâ', 'zeyyennâhâ' (50:6), 'medednâhâ', 'elqaynâ', 'enbetnâ' (50:7), 'nezzelnâ', 'enbetnâ' (50:9) — konuşan adlanmıyor; 50:2 'munzirun minhum' adsız — KAPATILAMAZ",
  "ölçüm (924): 50:3 'mitnâ' EDİLGEN 1/2 (pas z=2,52) ve iltifât 1 — okumada etken 'öldüğümüz', iltifât 3MP → 1P alıntı geçişi; ★★ bu işaretlerden — araç davranışı, metin hakkında kanıt değil",
  "yıldız etiketi (1001): 50:2 ★ — KAFİYE KIRILMASI ب'den; etiket 'allah' z=-0,53 basıyor (lafız yok) — etiket / kaynak uyuşmazlığı, bilinen tür",
  "yıldız formülü: 50:10 ★★★ hapaks بسق (kok_ekle_50 ile eklenen kök, 1 token; z=3,28) — bilinen davranış, içerik iddiası değil",
  "gloss (1021 ailesi): طلع 'doğma (güneş)' — 50:10 'tal'' (hurma tomurcuğu) anlamını kapsamıyor; حبب 'sevgi, sevme' — 50:9 'habb' (tane) anlamını kapsamıyor",
  "biçim (517 ailesi): 50:2 'bel' cevabı söylenmemiş yeminin ardında; 50:3 dönüş inkârı; 50:8 meful leh — ölçümde işaretsiz; 50:4 'qad' CERT ile işaretli",
  "okuma: 38:1, 11:73 → 50:1; 38:4, 11:72 → 50:2; 23:35, 23:82, 37:16, 37:53 → 50:3; 13:41, 21:44, 35:11, 42:6, 34:21 → 50:4; 29:68 → 50:5; 37:6, 41:12, 15:16 → 50:6; 15:19, 22:5, 13:3, 16:15, 21:31, 27:61, 31:10, 41:10 → 50:7; 34:9 → 50:8; 27:60, 23:18, 43:11, 15:22, 39:21, 21:50, 23:29, 38:29, 36:33, 10:24, 11:100, 21:15 → 50:9; 26:148, 37:65 → 50:10 — KAPATILAMAZ",
  "tetik: ilk koşuda 0 uyuşmaz (50:3 موت; 50:4 أرض; 50:6 سمو; 50:7 أرض + نبت زوج; 50:8 بصر; 50:9 سمو موه + نبت); [x/y] ilk koşuda 0 (56 sayım); kayıttan önce 50:3 emsal notu düzeltildi (23:35 2MP 'muhracûn', 'izâmen' farkı)",
 ], (11, 20): [
  "esmâ: 50:15 'evvel' (yaratmanın sıfatı), 50:18 'raqîb' (adsız gözetleyici) — ilâhî değil; 50:18 ölçüm MÜHÜRSÜZ / esma_kayit mühür EVET → karar 'değil' (1022) — karar sonrası bilanço geçerli mühür []",
  "aday 1041 alanı: رقب 4:1, 5:117, 33:52 'raqîb' (Allah) / 11:93 'innî ma'akum raqîb' (Şuayb) / 50:18 adsız gözetleyici; عيي 46:33 'lem ya'ye' (Allah, olumsuz) / 50:15 'e-fe-ayînâ' (1P, soru) — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 1P 'ahyeynâ' (50:11), 'ayînâ' (50:15), 'halaqnâ', 'na'lemu', 'nahnu' (50:16) adsız; 50:14 'vaîdi' gizli 1S adsız; 50:17 iki alıcı ve 'qa'îd', 50:18 'raqîb' adsız; 50:19 muhatap 2MS adsız; 50:20 üfleyen adsız (edilgen) — KAPATILAMAZ",
  "yıldız etiketi (1001): 50:11 ★ kafiye kırığı ج'den, etiket 'allah' z=-0,53 (lafız yok); 50:13 ★ kafiye kırığı ط'den, etiket 'n' z=-0,89 — etiket / kaynak uyuşmazlığı, bilinen tür",
  "yıldız formülü: 50:18 لفظ, 50:19 حيد ★★★ hapaks (kok_ekle_50 kökleri, 1 token; z=3,28); 50:20 ★★★ pas z=5,38 (tek fiilli kısa ayet, edilgen gerçek) — bilinen davranış, içerik iddiası değil",
  "biçim (517 ailesi): 50:11 teşbih 'kezâlike', 50:14 'kullun' + gizli 1S iyelik 'vaîdi', 50:19 3MS → 2MS hitap geçişi (ölçüm iltifât 0) ölçümde işaretsiz",
  "◈B tetik listesi: 50:16 'verîd' (damar) ve 50:17 'yemîn' / 'şimâl' organ / yan tetik listesinde yok — 50:16 satırı B1/B2 ile dolu, verîd tetik dışı not edildi; ön-kayıt §4 sınırı",
  "okuma: 42:27, 25:49, 43:11, 40:11, 50:42 (sûre içi metin) → 50:11; 22:42, 38:12, 25:38 → 50:12; 22:43, 38:13 → 50:13; 15:78, 26:176, 38:13, 44:37, 38:14, 14:14, 20:113 → 50:14; 46:33, 13:5 → 50:15; 15:26, 23:12 → 50:16; 24:15, 21:103 → 50:17; 4:1, 5:117, 33:52, 11:93 → 50:18; 15:72 → 50:19; 18:99, 20:102, 23:101, 27:87, 36:51, 39:68 → 50:20 — KAPATILAMAZ",
  "tetik: ön kuru koşu 5 tetik (50:11 حيي موت; 50:15 خلق; 50:16 خلق أنس; 50:19 موت; 50:20 يوم) — ilk koşuda 0 uyuşmaz; [x/y] ilk koşuda 0 (50 sayım); kayıttan önce iki geniş ifade daraltıldı (50:13 'ihvânu Lût', 50:20 sûr emsallerinin devamı)",
 ],
 (21, 30): [
  "esmâ: 50:21 'şehîd' — nefisle gelen adsız tanık, ilâhî değil; ölçüm MÜHÜRSÜZ / esma_kayit mühür EVET → karar 'değil' (1022) — karar sonrası bilanço geçerli mühür []",
  "konuşan / gönderge (1017 ailesi): 50:21 sürücü ve tanık; 50:22 konuşan 1P 'keşefnâ' ve 2MS muhatap; 50:23, 50:27 'qarîn' (43:36'da şeytan — burada adlanmıyor); 50:24, 50:26 ikil emrin emredeni ve emredilenleri; 50:28-29 1S 'ledeyye' / 'ene' — 22:10 ve 41:46'da aynı 'zallâm li'l-abîd' 3. şahısla Allah / Rab için; 50:30 1P 'neqûlu' — hepsi adsız, KAPATILAMAZ",
  "aday 1041 alanı: ظلم 'bi-zallâmin li'l-abîd' 22:10 (Allah, 3. şahıs), 41:46 (Rab, 3. şahıs) / 50:29 (1S, adsız) — kayıt, test yok",
  "gloss (1021 ailesi): حدد 'demir; sınır koyma' — 50:22 'hadîd' (keskin, göz için) anlamını kapsamıyor",
  "yıldız etiketi (1001): 50:25 ★ kafiye kırığı ب'den, etiket 'n' z=-0,89 — bilinen tür",
  "yıldız formülü: 50:27 ★ rab z=1,81 (10 kelimede 1 Rab — kısa ayet); 50:29 ★★★ pas z=5,38 (tek fiilli kısa ayet, edilgen gerçek); 50:26 lafız 1 (z=1,47) yıldızsız — bilinen davranış, içerik iddiası değil",
  "biçim (517 ailesi): 50:23 → 50:27 aynı 'qâle qarînuhû' ile teslim / savunma; 50:28 1S → 50:30 1P geçişi ölçümde iltifât 0; ikil emir 50:24, 50:26 iltifât yalnız 50:24'te 1",
  "okuma: 21:97, 18:101, 17:50, 18:96, 34:10 → 50:22; 43:36, 43:38, 37:51, 41:25 → 50:23; 17:39, 14:34, 39:3, 11:59, 14:15 → 50:24; 11:62, 14:9, 34:54 → 50:25; 15:96, 17:22, 17:39 → 50:26; 43:38 → 50:27; 26:96, 39:31 → 50:28; 22:10, 41:46 → 50:29 — KAPATILAMAZ",
  "tetik: ön kuru koşu 3 tetik (50:22 يوم + بصر; 50:30 يوم) — ilk koşuda 0 uyuşmaz; [x/y] ilk koşuda 0 (48 sayım)",
 ],
 (31, 40): [
  "esmâ: 50:32 'hafîz' (kulun sıfatı), 50:34 'selâm' (esenlik), 50:37 'şehîd' (kulak verenin hâli) — ilâhî değil, ölçüm MÜHÜRSÜZ / esma_kayit mühür EVET → karar 'değil' (1022); 50:33 'er-Rahmân' ilâhî (meful, ORTA konum, mühür yok) — karar sonrası bilanço geçerli mühür []",
  "aday 1041 alanı: حفظ 50:4 kitap / 50:32 kul / 42:6, 34:21 Allah; لغب 35:35 cennet ehli 'lâ yemessunâ … luğûb' / 50:38 1P yaratıcı 'mâ messenâ min luğûb' — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 50:31 yaklaştıran, 50:32 vaat eden ve hitap eden, 50:34 emreden adsız; 50:35 'ledeynâ', 50:36 'ehleknâ', 50:38 'halaqnâ' 1P adsız; 50:39-40 muhatap 2MS adsız — KAPATILAMAZ",
  "yıldız formülü: 50:31, 50:32 ★★★ pas z=5,38 (tek fiilli kısa ayet; edilgen gerçek) — bilinen davranış",
  "yıldız etiketi (1001): 50:36 ★ kafiye kırığı ص'den, etiket 'allah' z=-0,53 (lafız yok); 50:40 ★ kafiye kırığı, etiket 'n' z=-0,79",
  "çıpa: 50:38 'fî sitteti eyyâm' — sayı + birim, mekanizma yok; L1, L4 ölçü koluna sınırda (41:10 kaydıyla tutarlı); 25:59 ve 32:4 kayıtlarında çıpa kademesi bu oturumda görülmedi — KAPATILAMAZ",
  "biçim (517 ailesi): 50:31 3FS → 50:32 2MP hitap (iltifât 1), 50:32 2MP → 50:33 3MS 'men' (iltifât 1); 50:28-29 1S 'ledeyye' → 50:35 1P 'ledeynâ' geçişi ölçümde işaretsiz",
  "okuma: 26:90, 27:22 → 50:31; 17:25, 38:17, 38:30, 38:44 → 50:32; 36:11 → 50:33; 15:46 → 50:34; 19:74, 19:98, 20:128, 36:31, 43:8, 28:78, 14:21, 41:48, 42:35 → 50:36; 39:21 → 50:37; 25:59, 32:4, 35:35 → 50:38; 20:130, 38:17, 15:98 → 50:39; 20:130 → 50:40 — KAPATILAMAZ",
  "tetik: ön kuru koşu 7 tetik (50:33 قلب; 50:34 يوم; 50:37 قلب سمع; 50:38 سمو أرض يوم + خلق; 50:39 شمس; 50:40 ليل) — ilk koşuda 0 uyuşmaz; [x/y] ilk koşuda 0 (56 sayım); kayıttan önce iki ifade düzeltildi (50:32 sayım kapsamı, 50:33 'ilk ilâhî karar' kaynağı)",
 ],
 (41, 45): [
  "esmâ: 50:41 'qarîb' (yerin sıfatı), 50:45 'cebbâr' (2MS için olumsuzlanan) — ilâhî değil; ölçüm MÜHÜRSÜZ / esma_kayit mühür EVET → karar 'değil' (1022) — karar sonrası bilanço geçerli mühür []",
  "aday 1041 alanı: جبر 'cebbâr' okunan 11:59, 14:15, 19:32, 26:130, 40:35 insan için / 50:45 muhatap için olumsuz; 59:23 henüz okunmadı — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 50:41 çağıran ve 2MS muhatap; 50:43, 44, 45 1P 'nahnu' / 'aleynâ'; 50:45 gizli 1S 'vaîdi' — adsız, KAPATILAMAZ",
  "biçim (517 ailesi): 50:43 tekit 'innâ nahnu' ölçümde işaretsiz; fâsıla ر 50:43-44 (sûrede yalnız iki ر; KAFİYE KIRILMASI işaretlenmedi) — ölçüm sınıf tanımı, metin hakkında kanıt değil (924)",
  "okuma: 34:51 → 50:41; 36:49, 36:53 → 50:42; 15:23, 22:48 → 50:43; 25:25 → 50:44; 20:104, 11:59, 14:15, 19:32, 26:130, 40:35 → 50:45 — KAPATILAMAZ",
  "tetik: ön kuru koşu 6 tetik (50:41 يوم + سمع; 50:42 يوم + سمع; 50:43 حيي موت; 50:44 يوم أرض) — ilk koşuda 0 uyuşmaz; [x/y] ilk koşuda 0 (26 sayım)",
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_50.py uygular)
DUZELTME = {
}
