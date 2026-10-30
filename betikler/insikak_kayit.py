# -*- coding: utf-8 -*-
"""insikak_kayit.py — sûre 84 (İnşikâk) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 84

CIPA = {
 # blok 1-9
 1: dict(kademe='L1', olgu=True, cipa=False, not_="'ize's-semâ'u'nşaqqat' — âhirette kozmik olay (gök) — L1; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'ve ezinet li-rabbihâ ve huqqat' — göğün Rabbine kulak vermesi, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe='L1', olgu=True, cipa=False, not_="'ve ize'l-ardu muddet' — âhirette kozmik olay (yer) — L1; tarayıcı vermedi"),
 4: dict(kademe='L1', olgu=True, cipa=False, not_="'ve elqat mâ fîhâ ve texallet' — âhirette kozmik olay (yer) — L1; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'ve ezinet li-rabbihâ ve huqqat' — yerin Rabbine kulak vermesi, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'yâ eyyuhe'l-insânu inneke kâdihun …' — hitap (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'fe-emmâ men ûtiye kitâbehû bi-yemînih' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'fe-sevfe yuhâsebu hisâben yesîrâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 9: dict(kademe=None, olgu=False, cipa=False, not_="'ve yenqalibu ilâ ehlihî mesrûrâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 10-15
 10: dict(kademe=None, olgu=False, cipa=False, not_="'ve emmâ men ûtiye kitâbehû verâ'e zahrih' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 11: dict(kademe=None, olgu=False, cipa=False, not_="'fe-sevfe yed'û thubûrâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 12: dict(kademe=None, olgu=False, cipa=False, not_="'ve yaslâ se'îrâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'innehû kâne fî ehlihî mesrûrâ' — dünya, insan hâli (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe=None, olgu=False, cipa=False, not_="'innehû zanne en len yehûr' — âhiret inkârı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="'belâ inne rabbehû kâne bihî basîrâ' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 16-25
 16: dict(kademe='L0', olgu=True, cipa=False, not_="'fe-lâ uqsimu bi'ş-şafaq' — zaman (akşam kızıllığı), yemin edilen — L0 (81:17-18 kaydı emsali); tarayıcı vermedi"),
 17: dict(kademe='L0', olgu=True, cipa=False, not_="'ve'l-leyli ve mâ vesaq' — zaman (gece), yemin edilen — L0; 'mâ vesaq' adsız; tarayıcı vermedi"),
 18: dict(kademe='L0', olgu=True, cipa=False, not_="'ve'l-qameri ize'ttesaq' — gökcismi + süreç (dolunay), yemin edilen — L0 (81:18 sabah + süreç emsali); tarayıcı vermedi"),
 19: dict(kademe=None, olgu=False, cipa=False, not_="'le-terkebunne tabaqan 'an tabaq' — insan hâli, katlar adsız (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 20: dict(kademe=None, olgu=False, cipa=False, not_="'fe-mâ lehum lâ yu'minûn' — insan davranışı, soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 21: dict(kademe=None, olgu=False, cipa=False, not_="'ve izâ quri'e 'aleyhimu'l-qur'ânu lâ yescudûn' — insan davranışı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 22: dict(kademe=None, olgu=False, cipa=False, not_="'beli'llezîne keferû yukezzibûn' — insan davranışı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 23: dict(kademe=None, olgu=False, cipa=False, not_="'ve'llâhu a'lemu bimâ yû'ûn' — gaybî, bilme (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 24: dict(kademe=None, olgu=False, cipa=False, not_="'fe-beşşirhum bi-'azâbin elîm' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 25: dict(kademe=None, olgu=False, cipa=False, not_="'illa'llezîne âmenû … lehum ecrun ğayru memnûn' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 9): [
  "esmâ: e_oto 0 token; KARAR değişmedi (702); lafız yok; Rab 84:2, 5, 6 (sûre içi dört geçişin üçü)",
  "kök tablosu: kok_ekle_84 1 kök (كدح 84:6; korpusta tek ayet); 1510 → 1511; retroaktif yama hedefli 0, genel 0 (ikinci koşu da 0)",
  "harf alanı: ayet 1 ölçümünde harf 33 → harf3 14, isaret 0 (ayet 1 ailesi; besmele); araç alanı (924)",
  "yıldız: ★★★ 6 — 84:2, 5 rab z=6,78 (+ pas 2,52); 84:3, 7, 8 pas z=5,38; 84:6 hapaks z=3,28 (yeni kök; rab 2,34) — formül davranışı, içerik iddiası değil",
  "biçim / kip (924): 84:1, 3 'izâ' şart zarfı kip alanında yok; 84:6 'inne' tekidi kip alanında yok; 84:6 VOC + DIKKAT, 84:7 AMMA + COND, 84:8 FUT + MM doğru",
  "şart dizisi: 84:1-5 cevabı metinde açık değil (84:6 nidâ / 84:7 'fe-emmâ') — KAPATILAMAZ",
  "okuma ikiliği: 84:6 'mulâqîhi' zamiri (Rab / 'kedh') KAPATILAMAZ, meal 'onunla' açık bırakır; 84:2 ve 84:5 öznesi 3FS — gök / yer en yakın dişil adla (okuma)",
  "iltifât (924): 84:5 {3} → 84:6 {2, 3} ve 84:6 → 84:7 {3} kısmi örtüşme — iltifât 0",
  "gloss (1021): kök لقي iki anlamda (84:4 atma / 84:6 karşılaşma) — kök sayısı iki anlamı birleştiriyor; lemma 'ezine' izin verme / kulak verme kullanımlarını birleştiriyor — lemma sayısı verilmedi",
  "esit2: 84:2 / 84:5 TAM (sûre içi; ikisi de bu blokta basıldı); nakarat3 84:2 / 5 ve 84:7 süzgeç GEÇMEZ (84:7 eşi henüz okunmadı)",
  "adsız gönderge (1017): 84:2, 5 lâyık kılan; 84:3 uzatan; 84:4 'mâ fîhâ'; 84:6 muhatap 'el-insân' (cins), konuşan adsız; 84:7 veren; 84:8 hesaba çeken; 84:9 'ehl'",
  "fâsıla: 84:1-5 ت, 84:6-7 ه, 84:8-9 ا — ölçüm ت / H / A sınıfı; ت → ه (84:5 → 6) ve ه → ا (84:7 → 8) geçişleri bilançoda kafiye kırığı işaretlenmedi (924)",
  "◈B: 84:7 'yemîn' (sağ el) tetik listesinde değil — '—', gözlem ◇'ye; 84:9 قلب tetikliyor — dönme anlamı, organ değil; satır dolu, not düşüldü",
  "aday 1040 (kayıt): 83:36 / 84:1 sûre sınırı — soru + 3MP / şart zarfı + 3FS; ikisi de lafızsız, Rabsız; fâsıla ن → ت",
  "aday 1040 ailesi (okuma): 83:31 / 84:9 'inqalebe' + 'ilâ ehl' + hâl — dünyada keyifli dönüş / âhirette sevinçli dönüş",
  "bağ: kalıp / lemma eşleri okumayla (82:1, 19:90, 54:1, 55:37, 69:16, 15:19, 50:7, 82:6, 62:8, 69:19, 17:71, 65:8, 83:31); 84:10, 84:13 henüz okunmadı — bağ yazılmadı",
  "◈K / ◈B: ◈K dolu 84:1 سمو, 84:3 أرض; ◈B dolu 84:6 أنس, 84:9 قلب; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 25 sayım 0 uyuşmaz",
  "süreç: sûre 84 dosyaları mutaffifin_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_84.py, oturum dışı); kapanış / paket blok listesi BLOK_LISTESI_ELLE",
 ],
 (10, 15): [
  "esmâ: e_oto 1 token (84:15 'basîr' — 'inne rabbehû kâne bihî basîrâ') — İLÂHÎ; KARAR 702 → 703; ölçüm 'SON konum, MÜHÜRSÜZ' / bilanço geçerli mühür 84:15 — mühür iddiası bilançodan (1022)",
  "Rab: sûre içi dört geçişin dördü basıldı (84:2, 5, 6, 15) — ربب [4/4] 84:15; lafız yok",
  "kök tablosu: yeni kök yok (1511); retroaktif yama hedefli 0, genel 0",
  "fâsıla / kafiye (924, 1001): 84:10 ا → ه ve 84:14 ا → ر bilançoda kafiye kırığı — ikisi de metinde gerçek geçiş; 84:11 ه → ا ve 84:15 ر → ا işaretlenmedi; 84:14 ★ kaynağı 'n' etiketli, kafiye_kirik True (1001)",
  "yıldız: ★★★ 2 — 84:10 pas z=5,38, 84:15 rab z=3,23; ★ 84:14 (n, kafiye kırığı) — formül davranışı, içerik iddiası değil",
  "biçim / kip (924): 84:13, 14, 15 'inne' tekidi kip alanında yok; 84:15 'belâ' kip alanında yok; 84:10 AMMA + COND, 84:11 FUT, 84:14 NEG doğru",
  "gloss (1021): kök سرر 'sır, gizleme' 'mesrûr'da (sevinç) uymuyor — 84:9 ve 84:13 (84:9 için kayıttan sonra görüldü, burada yazıldı); kök حور dört anlamı birlikte veriyor, burada dönme",
  "◈B: 84:10 'zahr' (sırt) tetik listesinde değil — '—', gözlem ◇'ye; 84:15 بصر tetikliyor — 'basîr' Rab'ın sıfatı, organ adı yok; satır dolu",
  "adsız gönderge (1017): 84:10 veren; 84:13 'ehl'; konuşan adsız; 84:13-14 'innehû' zamiri 84:10 'men'e (okuma)",
  "okuma ikiliği: 84:13 'inne' gerekçe (okuma) — metin işaretlemiyor; 84:9 / 84:13 iki ayrı kişi (84:7 'men' / 84:10 'men') okumayla",
  "aday 1040 ailesi (okuma): 83:4 / 84:14 'zanne' + diriliş (soru / sanmıştı); 83:16 / 84:12 kök صلي; 83:31 / 84:13 dünyada aile yanında keyif / sevinç",
  "bağ: kalıp / lemma eşleri okumayla (69:25, 25:13, 25:14, 82:15, 83:16, 83:4, 64:7, 72:7, 17:96, 83:31; sûre içi 84:7, 84:8, 84:9); 4:10 henüz okunmadı — bağ yazılmadı",
  "◈K / ◈B: ◈K tetik yok; ◈B dolu 84:15 بصر; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 16 sayım 0 uyuşmaz",
 ],
 (16, 25): [
  "esmâ: e_oto 0 token; KARAR değişmedi (703); 84:23 sûrenin tek lafzı ('ve'llâhu a'lem' — 'a'lem' esmâ listesinde değil); sûre bütünü lafız 1, Rab 4 (84:2, 5, 6, 15); geçerli mühür sûrede 1 (84:15)",
  "kök tablosu: yeni kök yok (1511); retroaktif yama hedefli 0, genel 0",
  "yıldız: ★★★ 84:23 allah z=4,47 (lafızlı kısa ayet); ★★ 84:21 pas z=2,52 — formül davranışı, içerik iddiası değil",
  "iltifât: ölçüm 84:16, 17, 19, 20 — 84:16 {3} → {1} (1S yemin), 84:19 {3} → {2} (2MP hitap), 84:20 {2} → {3} gerçek; 84:17 {1} → {3} 'vesaqa' 3MS fiilinden, konuşan değişmedi (924); 84:24 {3} → {2, 3} kısmi örtüşme, 0",
  "biçim (924): 84:17-18 atıflı yeminlerde QASEM yok; 84:16 'lâ' yemin girişi kip NEG; 84:21 'izâ' şart kip alanında yok; 84:16 QASEM, 84:19 EMPH 2, 84:20 INTG + NEG, 84:22 IDRAB, 84:24 IMPV, 84:25 ISTISNA doğru",
  "fâsıla (924): 84:16-19 ق, 84:20-23 ن, 84:24 م, 84:25 ن; ا → ق (84:15 → 16) ve ق → ن (84:19 → 20) gerçek geçiş, bilanço kafiye kırığı işaretlemedi; ن / م N sınıfında",
  "gloss (1021): kök شفق şafak / işfâq; kök وسق toplama / tamamlanma (korpusun iki ayeti bu blokta); kök وعي üç anlam, burada biriktirme",
  "KAPATILAMAZ: 84:17 'mâ vesaq'; 84:19 'tabaqan 'an tabaq' katları; 84:22 yalanlananın ne olduğu; 84:23 biriktirilen; 84:24 2MS muhatabın 84:6 'insân' ile aynılığı; 84:25 istisnanın neyden olduğu ve türü",
  "adsız gönderge (1017): 84:16 konuşan 1S; 84:19 muhatap 2MP; 84:20-22 3MP; 84:21 okuyan; 84:24 muhatap 2MS",
  "aktör (1038 ailesi): 84:21 'qur'ân' rol fail — edilgen fiilin nâib-i faili (okuma)",
  "secde işareti 84:21 metinde; oturum_lemdizi / oturum_say durak işaretlerini atlıyor — sayımı etkilemedi",
  "esit2: 84:25 YAKIN → 41:8 (basıldı), 95:6 (henüz okunmadı) — 'inne' / 'illâ' farkı",
  "çıpa: L0 3 (84:16 şafak, 84:17 gece, 84:18 ay — yemin edilen zaman / gökcismi; 81:17-18 emsali); diğerleri olgu=False",
  "aday 1041: sûre 84'te kayıt yok — 'kâne' 84:13 (insan) / 84:15 (Rab) bağlayıcı fiil, bölünme sayılmadı",
  "aday 1040: 84:25 → 85:1 sınırı 85:1 okunurken",
  "bağ: kalıp / lemma eşleri okumayla (56:75, 69:38, 70:40, 81:15, 75:1, 81:17, 81:18, 67:3, 71:15, 57:8, 31:7, 45:8, 70:18, 41:8, 68:3); 5:84, 7:204, 85:19, 95:6 henüz okunmadı — bağ yazılmadı",
  "süreç: kayıttan önce düzelttiğim — 84:24 ◇'de basılmamış okunmuş ayet (sûre 9) numarayla yazılmıştı; 'okunmuş 1' diye sayıya çevrildi",
  "◈K / ◈B: ◈K dolu 84:17 ليل, 84:18 قمر; 84:16 'şafaq' tetik listesinde değil — '—'; ◈B tetik yok; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 25 sayım 0 uyuşmaz",
 ],
}

DUZELTME = {
 21: dict(alan='mercek', eski="okunma + yüz çevirme + 84:24 ile aynı 'fe-beşşirhu bi-'azâbin elîm'",
          dogru="'aynı' yanlış: 31:7 ve 45:8'de 3MS 'fe-beşşirhu bi-'azâbin elîm', 84:24'te 3MP 'fe-beşşirhum bi-'azâbin elîm' — zamir farklı, geri kalan aynı (84:24 ◇ bunu doğru yazıyor). Basılan metinler değişmedi; yalnız karşılaştırma cümlesi. Kayıttan sonra sunum sırasında yakalandı.",
          aday=None, blok='16-25'),
}
