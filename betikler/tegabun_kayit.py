# -*- coding: utf-8 -*-
"""tegabun_kayit.py — sûre 64 (Teğâbun) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 64

CIPA = {
 # blok 1-6
 1: dict(kademe='L0', olgu=True, cipa=False, not_="'yusebbihu li'llâhi mâ fi's-semâvâti ve mâ fi'l-ard' — gökler ve yer tesbih edenlerin yeri olarak adlanıyor; süreç / ölçü yok — L0 (62:1 emsali); tarayıcı vermedi"),
 3: dict(kademe='L0', olgu=True, cipa=False, not_="'halaqa's-semâvâti ve'l-arda bi'l-haqq' — gökler ve yer yaratılan olarak adlanıyor; süreç / ölçü yok — L0; biçim verme 2MP'ye, aşama yok; tarayıcı vermedi"),
 4: dict(kademe='L0', olgu=True, cipa=False, not_="'ya'lemu mâ fi's-semâvâti ve'l-ard' — gökler ve yer bilginin nesnesi; süreç / ölçü yok — L0; tarayıcı vermedi"),
 # blok 7-12
 9: dict(kademe=None, olgu=False, cipa=False, not_="'cennâtin tecrî min tahtihe'l-enhâr … ebedâ' — cennet ırmakları, âhiret; doğal olgu değil, merdiven uygulanmadı; tarayıcı v4 adayı, çıpa değil"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'ashâbu'n-nâr' — âhiret ateşi; doğal olgu değil; tarayıcı vermedi"),
 # blok 13-18
 14: dict(kademe=None, olgu=False, cipa=False, not_="'inne min ezvâcikum ve evlâdikum aduvven lekum' — eşler ve çocuklar insan ilişkisi; doğal süreç yok, merdiven uygulanmadı; tarayıcı v4 adayı, çıpa değil"),
 17: dict(kademe=None, olgu=False, cipa=False, not_="'in tuqridu'llâhe qardan hasenen' — borç insan yapımı ilişki, mecaz; doğal olgu değil; tarayıcı vermedi"),
}

ARIZA = {
 (1, 6): [
  "esmâ: e_oto 6 token (64:1 'qadîr'; 64:2 'mu'min', 'basîr'; 64:4 'alîm'; 64:6 'ğaniyy', 'hamîd'); 'mu'min' DEĞİL (insan), öbür beşi İLÂHÎ; KARAR 602 → 608; bilanço geçerli mühür 64:1, 2, 4, 6",
  "esmâ ölçüm (1022): 64:1, 64:2, 64:4 ölçüm satırı 'MÜHÜRSÜZ' yazıyor, karar sonrası bilanço geçerli mühür veriyor; 64:4 'alîm' ölçümde 'SON' konum, ardından 'bi-zâti's-sudûr' geliyor — mühür iddiası bilançodan",
  "harf alanı: ayet 1 ölçümünde harf 79 → harf3 57, isaret 0 (önceki sûrelerin ayet 1 ailesi); 64:2-6'da fark = isaret — besmele harfleri olabilir; araç alanı, metin hakkında kanıt değil (aday 924); KAPATILAMAZ",
  "kök tablosu: kok_ekle_64 blok 1-6 için boş (karşılık eksiği yok); 1430 kök; retroaktif yama hedef 0",
  "fâsıla: 64:1-4 ر (R sınıfı), 64:5 م (N sınıfı), 64:6 د; bilanço kafiye kırığı 0 — sınıf geçişi işaretlenmedi (924)",
  "yıldız (924): 64:6 ★ allah z=1,97 (16 kelimede 2 lafız) — içerik iddiası değil",
  "tetik listesi dışı organ (ön-kayıt §4): 64:4 'sudûr' (göğüsler) — ◈B satırı doldurulmadı, gözlem ◇'de",
  "nakarat3 (1003): 64:1 / 64:4 'mâ fî semâ' sûre içi blokta; 64:2 'lafız bimâ amel' eşi 64:8 henüz okunmadı (defterden koşuldu)",
  "aday 1040 (kayıt): 63:11 → 64:1 sûre sınırı — ecelin ertelenmemesi ve 'habîrun bimâ ta'melûn' ile kapanış / göklerin ve yerin tesbihiyle açılış; fâsıla ن → ر; test yok",
  "okuma bağı (1040 dışı): 62:1 / 64:1 aynı tesbih açılışı — harekesiz 'yusebbihu li'llâh' 2 ayet; arada sûre 63, ardışık değil",
  "aday 1041: blokta vaka yok (64:6 kök غني 'istağnâ' / 'ğaniyy' ikisi de Allah için)",
  "adsız (aday 1017): 64:2-5 muhatap 2MP; 64:5 önceki inkâr edenler (adsız); 64:6 elçiler ve topluluk — ad verilmedi",
  "çıpa: L0 64:1, 64:3, 64:4 (gökler ve yer); L4 yok; tarayıcı adayı yok",
  "karşıt çift (aday 1039, okuma): 64:1 ve 64:3 gökler / yer; 64:2 kâfir / mu'min; 64:4 gizli / açık; 64:5, 64:6 yok — kayıt, test yok",
  "okuma: 63:11, 62:1 → 64:1; 57:4 → 64:2; 39:5, 40:64 → 64:3; 16:19, 31:23 → 64:4; 9:70, 59:15 → 64:5; 40:22, 9:70, 54:24, 14:8 → 64:6 — KAPATILAMAZ",
  "kendi kaydı (kayıttan önce): 64:1 lemma 'sebbaha' okunmuş / okunmamış sayısı yanlış yazılmıştı (33 / 6 → 31 / 8); 64:2 ◈B tetik listesi eksik yazılmıştı (خلق → خلق بصر) — düzeltildi",
  "tetik: ön kuru koşu 5 uyuşmaz (64:1, 64:3, 64:4 ◈K سمو أرض; 64:2 ◈B خلق بصر; 64:3 ◈B خلق) → satırlar dolduruldu; kayıtta 0 uyuşmaz; [x/y] 0 (58 sayım)",
 ],
 (7, 12): [
  "esmâ: e_oto 4 token (64:8 'nûr', 'habîr'; 64:11 'alîm'; 64:12 'mubîn'); 'habîr' ve 'alîm' İLÂHÎ, 'nûr' (indirilen nur) ve 'mubîn' (tebliğin sıfatı) DEĞİL; KARAR 608 → 612; bilanço geçerli mühür 64:8, 64:11; 64:12 esma_kayit mühür EVET, karar sonrası geçersiz (1022)",
  "esmâ ölçüm (1022): 64:8 'habîr', 64:11 'alîm' ölçümde 'MÜHÜRSÜZ', bilanço geçerli mühür veriyor — mühür iddiası bilançodan",
  "kafiye (924): bilanço kafiye kırığı 64:9 (ر → م) ve 64:10 (م → ر); blok 1-6'da 64:5 (ر → م) ve 64:6 (م → د) geçişleri işaretlenmemişti — işaretleme tutarsız; araç alanı",
  "yıldız (1001 / 924): 64:10 ★ kaynak 'allah' z=-0,53 — ayette lafız yok, ★ kafiye kırığından geliyor olabilir, kaynak etiketi yanlış; 64:9 ★★★ hapaks z=3,28 (غبن, kafiye kırığıyla); 64:8 ★★★ ve 64:11 ★★★ allah (10 kelimede 2, 16 kelimede 3 lafız); 64:7 ★★ pas z=2,12 — içerik iddiası değil",
  "hapaks: 64:9 kök غبن korpusta 1 token ('teğâbun'), sûre adı; eklenmiş kök değil (kok_turkce'de var)",
  "kök tablosu: kok_ekle_64 blok 7-12 için boş (karşılık eksiği yok); 1430 kök; retroaktif yama hedef 0",
  "biçim (924): 64:12 hasr 'fe-innemâ' ölçümde HASR olarak yazılmıyor (64:11 'mâ … illâ' HASR yazılıyor)",
  "kök iki anlam (okuma, D3): نور 64:8 'en-nûr' / 64:10 'en-nâr'; كفر 64:9 'yukeffir' (örtme) / sûre içi öbür geçişler (inkâr) — gloss iki anlamı taşımıyor (كفر 'inkâr, nankörlük'; 1021 ailesi)",
  "aday 1041 (kayıt): kök هدي 64:6 'e-beşerun yehdûnenâ' (topluluğun sözünde beşer öznesi) / 64:11 'yehdi qalbeh' (Allah öznesi) — aynı sûrede",
  "nakarat3 (1003): 64:2 → 64:8 'lafız bimâ amel' kapandı; 64:9 / 64:11 've men yu'min bi'llâh' blokta",
  "esit2: 64:12 → 5:92 BENZER — henüz okunmadı",
  "adsız (aday 1017): 64:7 'qul' muhatabı ve 1S konuşan; 64:8 ve 64:12 elçi; edilgen dirilten / haber veren (64:7) — ad verilmedi",
  "çıpa: 64:9 cennet ırmakları (âhiret, tarayıcı v4 adayı — çıpa değil, olgu değil), 64:10 ateş (âhiret); L0-L4 yok",
  "karşıt çift (aday 1039, okuma): 64:7 diriltilmeyecekler / diriltileceksiniz; 64:9 iyi iş / kötülükler; 64:9 / 64:10 cennet-kurtuluş / ateş-kötü varış; 64:12 itaat / yüz çevirme; 64:8, 64:11 yok — kayıt, test yok",
  "okuma: 62:6, 58:7, 24:64, 31:23, 57:22 → 64:7; 61:11, 57:10 → 64:8; 9:100 → 64:9; 57:19, 58:8 → 64:10; 57:22, 63:3, 58:7, 24:64 → 64:11; 24:54 → 64:12 — KAPATILAMAZ",
  "kendi kaydı (kayıttan önce): 64:7'de Rab için 'sûre içi tek' yazılmıştı — 64:13-18 henüz okunmadığı için 'şimdiye dek tek' olarak düzeltildi",
  "tetik: ön kuru koşu 2 uyuşmaz (64:9 ◈K يوم نهر أبد, 64:11 ◈B قلب) → satırlar dolduruldu; kayıtta 0 uyuşmaz; [x/y] 0 (73 sayım)",
 ],
 (13, 18): [
  "esmâ: e_oto 8 token (64:13 'mu'minûn'; 64:14 'ğafûr', 'rahîm'; 64:17 'şekûr', 'halîm'; 64:18 'âlim', 'azîz', 'hakîm'); 'mu'minûn' DEĞİL (inananlar, çoğul), öbür yedisi İLÂHÎ; KARAR 612 → 620; bilanço geçerli mühür 64:14, 17, 18; 64:13 esma_kayit mühür EVET, karar sonrası geçersiz (1022)",
  "esmâ sınıf E: 64:18 'âlim' lafız olmadan İLÂHÎ (62:8 emsali; ad dizisi 64:17 lafzının devamı)",
  "kök / lafız (sûre 59 dersi): kök أله sûre içi 21 token, lafız 20 (bilanço 5 + 8 + 7) — fark 64:13 'ilâh' tokeni",
  "biçim (924): 64:13 ölçüm iltifât 1, şahıs alanı yalnız 3MS 2 — iltifât değeri açıklanmıyor; 64:15 hasr 'innemâ' ölçümde HASR olarak yazılmıyor (64:12 ile aynı açık)",
  "sayı işareti (924): 64:14 'zevc' — 'ezvâcikum' (eşleriniz), sayı değil",
  "yıldız (924): 64:13 ★★★ allah z=3,92 (9 kelimede 2 lafız), 64:17 ★★ allah z=2,80, 64:15 ★ allah z=1,97 — içerik iddiası değil",
  "kök tablosu: kok_ekle_64 blok 13-18 için boş (karşılık eksiği yok); 1430 kök; retroaktif yama hedef 0",
  "kafiye: blok içi kafiye kırığı 0 (64:13 ن, 64:14 م, 64:15 م, 64:16 ن, 64:17 م, 64:18 م; geçişler işaretlenmedi — 924)",
  "aday 1040 (kayıt): 63:4 'humu'l-aduvvu fe'hzerhum' / 64:14 'aduvven lekum fe'hzerûhum'; 63:9 / 64:15 'emvâlukum ve evlâdukum' — ardışık sûreler; test yok; 64:18 → 65:1 sûre sınırı 65:1 henüz okunmadığı için yazılmadı",
  "aday 1041 (kayıt): 64:14 kök غفر 'tağfirû' (2MP, insan) / 'ğafûr' (Allah) aynı ayette",
  "esit2: 64:15 → 8:28 BENZER (henüz okunmadı); 64:18 → 32:6 BENZER (okumada görüldü)",
  "okuma bağı (ardışık değil): 9:129 'tevellev → lâ ilâhe illâ huve → tevekkül' tek ayette / 64:12-13 iki ayette; 62:1 açılışındaki 'el-azîzi'l-hakîm' / 64:18 kapanışta",
  "adsız (aday 1017): 64:14-17 muhatap 2MP; 64:16 edilgen 'yûqa' koruyan adlanmıyor; 64:18 özne adsız (sıfatla) — ad verilmedi",
  "çıpa: 64:14 tarayıcı v4 adayı — eşler / çocuklar, olgu değil; 64:17 borç mecaz; L0-L4 yok",
  "karşıt çift (aday 1039, okuma): 64:14 düşman-sakının / affetme; 64:15 sınav / ödül; 64:16 harcama / nefsin hırsı; 64:18 gayb / şehâdet; 64:13, 64:17 yok — kayıt, test yok",
  "okuma: 9:129, 58:10 → 64:13; 63:4 → 64:14; 63:9, 9:22 → 64:15; 59:9 → 64:16; 57:11, 57:18 → 64:17; 62:8, 32:6, 62:1 → 64:18 — KAPATILAMAZ",
  "tetik: ön kuru koşu 2 uyuşmaz (64:14 ◈B زوج, 64:16 ◈B سمع) → satırlar dolduruldu; kayıtta 0 uyuşmaz; [x/y] 0 (49 sayım)",
 ],
}

DUZELTME = {
}
