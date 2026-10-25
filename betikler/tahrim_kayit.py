# -*- coding: utf-8 -*-
"""tahrim_kayit.py — sûre 66 (Tahrîm) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 66

CIPA = {
 # blok 5-8
 5: dict(kademe=None, olgu=False, cipa=False, not_="'seyyibâtin ve ebkârâ' — evlilik geçmişine göre iki sınıf (medenî durum), sıfat dizisinin sonu; doğal olgu değil, merdiven uygulanmadı; tarayıcı v4 adayı (hapaks ثيب), çıpa değil"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'nâran vaqûduhe'n-nâsu ve'l-hicâra … melâ'iketun ğılâzun şidâd' — âhiret ateşi ve melekler; doğal olgu değil; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'cennâtin tecrî min tahtihe'l-enhâr … nûruhum yes'â' — âhiret; doğal olgu değil; tarayıcı vermedi"),
 # blok 9-12
 12: dict(kademe=None, olgu=False, cipa=False, not_="'ahsanet fercehâ fe-nefahnâ fîhi min rûhinâ' — iffet ve ruhtan üfleme; biyolojik süreç anlatılmıyor, doğal olgu değil, merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 4): [
  "esmâ: e_oto 9 token (66:1 'ğafûr', 'rahîm'; 66:2 'mevlâ', 'alîm', 'hakîm'; 66:3 'alîm', 'habîr'; 66:4 'mevlâ', 'mu'minîn'); 'mu'minîn' DEĞİL, öbür sekizi İLÂHÎ; KARAR 623 → 632; bilanço geçerli mühür 66:1, 2, 3; 66:4 esma_kayit mühür EVET, karar sonrası geçersiz (ayet 'zahîr' — melekler — ile kapanıyor; 1022)",
  "esmâ: 66:3 'el-alîmu'l-habîr' lafız olmadan, Peygamberin sözünde fail — İLÂHÎ; 66:4 'mevlâ' haberine Cibrîl ve 'sâlihu'l-mu'minîn' atıfla ortak",
  "harf alanı: ayet 1 ölçümünde harf 78 → harf3 55, isaret 0 (önceki sûrelerin ayet 1 ailesi); araç alanı (aday 924); KAPATILAMAZ",
  "kök tablosu: kok_ekle_66 1 kök (صغو, 66:4; 1431 → 1432; gloss korpus 2 ayet); retroaktif yama hedef 1 (6:113 — sûre 6 kaydında ayet düzeyi kayıt yok, henüz okunmadı), yama 0, genel geçiş 0; blok 5-8 için ثيب eksik — orada eklenecek",
  "yıldız (924): 66:2 ★★★ allah z=3,11 (11 kelimede 2 lafız), 66:1 ★★ allah z=2,33, 66:3 ★ n z=1,76 — içerik iddiası değil",
  "sayı işareti (924): 66:1, 66:3 'zevc' — 'ezvâc' (eşler), sayı değil",
  "biçim: 66:1 2MS → 66:2 2MP; 66:3 alıntı içinde 1S / 2MS; 66:4 ikil 2D — ölçüm iltifât 0",
  "kafiye (924): 66:2 م → 66:3 ر geçişi kafiye kırığı olarak işaretlenmedi",
  "nakarat3 (1003): 66:4 'tâbe ilâ lafız' eşi 66:8 henüz okunmadı (defterden)",
  "aday 1040 (kayıt): 65:12 → 66:1 sûre sınırı — bilgiyle kapanış / soru ve nidâyla açılış; fâsıla ا → م; ayrıca 65:1 / 66:1 ardışık iki sûre aynı nidâ 'yâ eyyuhe'n-nebiyy' ile açılıyor; 64:14 / 65:1 / 66:1 üç ardışık sûrede eşler; 64:4 / 66:3 'esarra' (ardışık değil, okuma bağı); test yok",
  "aday 1041 (kayıt): 66:3 fiil 'nebbe'e' eş, Peygamber ve Allah için aynı ayette; 66:2 / 66:4 'mevlâ' Allah için, haberine Cibrîl ve 'sâlihu'l-mu'minîn' ortak",
  "kök iki anlam (okuma, D3): ظهر 66:3 'azharahu' (açığa çıkardı) / 66:4 'tezâherâ', 'zahîr' (destek); حلل 66:1 'ehalle' (helâl kılma) / 66:2 'tahille' (yeminin çözülmesi)",
  "adsız (aday 1017): Peygamber ('en-nebiyy', 2MS / 3MS), eşleri, eşlerinden biri (66:3 konuşan 3FS), iki muhatap (66:4, 2D) — ad verilmedi; Cibrîl metinde adlı",
  "çıpa: blokta doğal olgu yok; melekler olgu değil; tarayıcı adayı yok",
  "karşıt çift (aday 1039, okuma): 66:1 yasak etme / helâl kılma; 66:3 gizledi / açığa çıkardı, bildirdi / vazgeçti; 66:4 tövbe / karşı birleşme; 66:2 yok — kayıt, test yok",
  "okuma: 33:28, 65:1, 65:12, 9:29, 64:14 → 66:1; 33:38, 47:11, 33:1 → 66:2; 64:4, 64:7, 31:34 → 66:3; 28:86 → 66:4 — KAPATILAMAZ",
  "kendi kaydı (kayıttan önce): 66:4'te 66:3'e ait ظهر [1/3] sayısı 66:4 [x/y] biçiminde yazılmıştı — oturum_xy yakaladı, düzeltildi",
  "tetik: ön kuru koşu 3 uyuşmaz (66:1 ◈B زوج, 66:3 ◈B زوج, 66:4 ◈B قلب) → satırlar dolduruldu; kayıtta 0 uyuşmaz; [x/y] 0 (42 sayım)",
 ],
 (5, 8): [
  "esmâ: 3 token (66:8 'nûr' ×2, 'qadîr'); 'nûr' ×2 DEĞİL (inananların nuru), 'qadîr' İLÂHÎ ('rabbenâ' hitabının haberi); KARAR 632 → 635; bilanço geçerli mühür 66:8; 66:5, 66:6, 66:7 esmâsız",
  "esmâ alanı (924): 66:8 ölçüm satırı 'qadîr' için 'SON konum, MÜHÜRSÜZ' gösteriyor, esma_kayit ve bilanço mühür EVET / geçerli — iki alan farklı; KAPATILAMAZ",
  "kök tablosu: kok_ekle_66 ثيب eklendi (66:5; 1432 → 1433; gloss korpus 1 ayet); retroaktif yama hedefi yok (kök yalnız 66:5'te)",
  "yıldız (924): 66:5 ★★★ hapaks z=3,28 (ثيب), 66:8 ★★★ n z=3,46 (45 kelime) — içerik iddiası değil; 66:6, 66:7 yıldızsız",
  "sayı işareti (924): 66:5 'zevc' — 'ezvâcen' (eşler), sayı değil",
  "edilgen: 66:6 'yu'merûn', 66:7 'tuczevne' — fail adlanmıyor (1017)",
  "nakarat3 (1003): 66:5 / 66:8 'asâ rabb en', 66:6 / 66:8 'yâ eyyuhe'llezîne âmenû', 66:4 / 66:8 'tâbe ilâ lafız' — üçü GEÇMEZ; eşler sûre içinde okundu, iplikler kapandı",
  "xref: 66:6 → 2:24 henüz okunmadı",
  "aday 1040 (kayıt): 65:1 / 66:5 fiil 'tallaqa'; 65:5 'yukeffir anhu seyyi'âtihî' ve 65:11 'yudhilhu cennâtin tecrî min tahtihe'l-enhâr' / 66:8; test yok",
  "aday 1041: blokta yeni kayıt yok",
  "kök / lemma iki anlam (okuma, D3): 'yemîn' 66:2 'eymânikum' (yeminler) / 66:8 'bi-eymânihim' (sağ yanlar); نور 66:6 'nâr' (ateş) / 66:8 'nûr' — gloss iki anlamı taşıyor",
  "adsız (aday 1017): muhatap eşler (66:5, 2FP), olası eşler (sıfatlarla), Peygamber ('en-nebiyy'), karşılık veren (66:7 edilgen), konuşan inananlar (66:8, 1P) — ad verilmedi",
  "çıpa: 66:5 medenî durum (tarayıcı v4 adayı, çıpa değil); 66:6 ateş ve melekler, 66:7 'el-yevm', 66:8 cennet ve nur — âhiret; blokta doğal olgu yok",
  "karşıt çift (aday 1039, okuma): 66:5 dul / bakire; 66:7 inananlar / inkâr edenler (66:6 ile); 66:8 ateş / nur (66:6 ile, aynı kök); 66:6 yok — kayıt, test yok",
  "okuma: 65:1, 33:49, 33:35, 56:36 → 66:5; 64:16, 16:50 → 66:6; 9:66, 52:16, 45:28 → 66:7; 66:4, 64:9, 47:2, 65:5, 65:11, 57:12 → 66:8 — KAPATILAMAZ",
  "tetik: ön kuru koşu 5 uyuşmaz (66:5 ◈B زوج, 66:6 ◈B أنس, 66:7 ◈K يوم, 66:8 ◈K نهر يوم ve ◈B يدي) → satırlar dolduruldu; kayıtta 0 uyuşmaz; [x/y] 0 (71 sayım)",
 ],
 (9, 12): [
  "esmâ: blokta esmâ tokeni yok (e_oto 0); KARAR 635 değişmedi; geçerli mühür yok",
  "esit2 alanı (924): 66:9 metni 9:73 ile karakter karşılaştırmasında EŞİT, ölçüm esit2 oranı 0,9821 (kademe YAKIN) — araç tam eşitliği 1 vermiyor; KAPATILAMAZ",
  "kök tablosu: blok 9-12 için karşılık eksiği yok; retroaktif yama 0",
  "kök iki anlam (1021): بني 66:11 'ibni' (yap) / 66:12 'ibnete' (kız) — gloss 'bina, yapma' 'kız / oğul' anlamını taşımıyor (korpus kökü iki anlamı birleştiriyor)",
  "yıldız (924): 66:10 ★ n z=1,55 (27 kelime) — içerik iddiası değil; 66:9, 66:11, 66:12 yıldızsız",
  "edilgen: 66:10 'qîle' — söyleyen adlanmıyor (1017)",
  "biçim: 66:10 lafız 3MS → 1P 'ibâdinâ', 66:12 1P 'nefahnâ' → 3FS — ölçüm iltifât 0",
  "nakarat3 (1003): 66:10 / 66:11 'daraba'llâhu meselen li'llezîne' GEÇER (4 kelime / 2 ayet) — iki mesel, iki grup",
  "adlı (metinde): Nûh, Lût, Firavun, Meryem, İmrân, cehennem, cennet; adsız (aday 1017): Nûh ve Lût'un eşleri, Firavun'un eşi, 66:10 'qîle' söyleyen — ad verilmedi",
  "aday 1040: blokta yeni kayıt yok (66:12 → 67:1 sûre sınırı 67 henüz okunmadı, yazılmadı)",
  "aday 1041: blokta yeni kayıt yok",
  "çıpa: 66:12 iffet / ruhtan üfleme olgu değil; 66:9 cehennem, 66:10 ateş, 66:11 cennet — âhiret; blokta doğal olgu yok; tarayıcı adayı yok",
  "karşıt çift (aday 1039, okuma): 66:10 / 66:11 inkâr edenler / inananlar, ateşe girin / cennette ev; 66:9, 66:12 yok — kayıt, test yok",
  "okuma: 9:73, 66:1, 65:1, 33:28, 33:1 → 66:9; 28:9, 45:19, 12:67, 12:68, 14:21 → 66:10; 28:9, 23:28, 28:21 → 66:11; 28:27, 21:91, 33:35 → 66:12 — KAPATILAMAZ",
  "tetik: ön kuru koşu 0 uyuşmaz (blokta tetik yok); kayıtta 0; [x/y] 0 (59 sayım)",
 ],
}

DUZELTME = {
}
