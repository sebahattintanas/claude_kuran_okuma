# -*- coding: utf-8 -*-
"""talak_kayit.py — sûre 65 (Talâk) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 65

CIPA = {
 # blok 1-3
 1: dict(kademe=None, olgu=False, cipa=False, not_="'li-iddetihinne ve ahsu'l-idde' — iddet sayımı insan uygulaması (hukuk); doğal olgu değil, merdiven uygulanmadı; tarayıcı v4 adayı ('F_ölçü'), çıpa değil"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'fe-izâ beleğne ecelehunne' — ecel iddet süresi, insan uygulaması; 'el-yevmi'l-âhir' âhiret; doğal olgu değil; tarayıcı v4 adayı, çıpa değil"),
 3: dict(kademe='L1', olgu=True, cipa=False, not_="'qad ce'ale'llâhu li-kulli şey'in qadrâ' — ölçü kelimesi ('qadr'), birim / miktar / mekanizma yok — L1; L4 ölçü kolu yalnız kelime düzeyinde (54:49 emsali); tarayıcı v4 adayı, çıpa değil"),
 # blok 4-7
 4: dict(kademe='L1', olgu=True, cipa=False, not_="'ye'isne mine'l-mahîd … lem yahidne … ulâtu'l-ahmâl … en yeda'ne hamlehunne' — aybaşı kesilmesi, henüz görmeme, gebelik ve doğum adlanıyor; iddet için üç sınıf, süre (üç ay, doğum) olguyu değil iddeti ölçüyor (799 ilkesi) — L1; L4 sınıf kolu için sınır vakası (sınıflama hukukî), kayıt; tarayıcı v4 adayı ('F_ölçü'), çıpa değil"),
 6: dict(kademe='L0', olgu=True, cipa=False, not_="'hattâ yeda'ne hamlehunne … fe-in erda'ne' — gebelik, doğum, emzirme adlanıyor; süreç / ölçü yok — L0; tarayıcı vermedi"),
 # blok 8-12
 8: dict(kademe=None, olgu=False, cipa=False, not_="'ke-eyyin min qaryetin' — kasaba insan yerleşimi; hesap ve azap anlatı; doğal olgu değil; tarayıcı vermedi"),
 11: dict(kademe=None, olgu=False, cipa=False, not_="'mine'z-zulumâti ile'n-nûr' mecaz; 'cennâtin tecrî min tahtihe'l-enhâr … ebedâ' âhiret; doğal olgu değil, merdiven uygulanmadı; tarayıcı v4 adayı, çıpa değil"),
 12: dict(kademe='L1', olgu=True, cipa=False, not_="'halaqa seb'a semâvâtin ve mine'l-ardi mislehunne yetenezzelu'l-emru beynehunne' — yedi gök (sayı), yerden benzeri, arada emrin inişi; ölçü birimi / mekanizma yok — L1 (41:12 emsali); L4 sınıf / ölçü koluna sınırda, KAPATILAMAZ; tarayıcı v4 adayı, çıpa değil"),
}

ARIZA = {
 (1, 3): [
  "esmâ: e_oto 1 token (65:2 'âhir' — 'el-yevmi'l-âhir'), DEĞİL; KARAR 620 → 621; 65:2 esma_kayit mühür EVET, karar sonrası geçersiz (1022); blokta geçerli mühür yok",
  "harf alanı: ayet 1 ölçümünde harf 202 → harf3 169, isaret 0 (önceki sûrelerin ayet 1 ailesi); araç alanı, metin hakkında kanıt değil (aday 924); KAPATILAMAZ",
  "kök tablosu: blok 1-3 için karşılık eksiği yok; 65:4 için حيض eksik — blok 4-7'de kok_ekle_65 ile eklenecek",
  "yıldız (924): 65:1 ★★★ n z=3,04 (41 kelime), 65:2 ★ n z=1,87 (30 kelime) — uzun ayet; 65:3 ★★ allah z=2,33 — içerik iddiası değil",
  "sayı işareti (924): 65:1 'idde' ×2 — sayma / bekleme süresi, rakam yok; 65:2 ikil 'zevey' sayı işareti almıyor",
  "biçim: 65:1 tekil nidâ 'yâ eyyuhe'n-nebiyy' ardından 2MP 'tallaqtum' ve sonda 2MS 'lâ tedrî' — ölçüm iltifât 0 (şahıs alanı 2MS 1 · 2MP 11)",
  "nakarat3 (1003): 65:2 've men yetteqi'llâh(e yec'al lehû)' GEÇER — sûre içi eşleri henüz okunmadı (defterden)",
  "aday 1040 (kayıt): 64:18 → 65:1 sûre sınırı — sıfat dizisiyle kapanış / nidâ ve hükümle açılış; fâsıla م → ا; ardışık sûrelerde: 64:16 / 65:1 sakınma emri, 64:13 / 65:3 tevekkül, 64:14 / 65:1 eşler; test yok",
  "aday 1041 (kayıt): 65:2 / 65:3 kök بلغ 'beleğne ecelehunne' (kadınlar) / 'bâliğu emrih' (Allah)",
  "adsız (aday 1017): 65:1 nidâ 'en-nebiyy', kadınlar (sınıf); 65:2 iki adil şahit, edilgen 'yû'azu' öğüt veren — ad verilmedi",
  "çıpa: 65:1 iddet, 65:2 ecel (insan uygulaması, olgu değil); 65:3 L1 'li-kulli şey'in qadrâ'; tarayıcı v4 adayı 3 (65:1, 2, 3), hiçbiri çıpa değil",
  "karşıt çift (aday 1039, okuma): 65:1 çıkarmayın / çıkmasınlar; 65:2 tutun / ayrılın; 65:3 hesaba katmadığı / ona yeter — kayıt, test yok",
  "okuma: 64:18, 33:1, 33:49, 9:36, 64:16, 33:30, 58:4, 31:34 → 65:1; 58:3 → 65:2; 39:47, 59:2, 64:13, 9:129, 54:49 → 65:3 — KAPATILAMAZ",
  "tetik: ön kuru koşu 1 uyuşmaz (65:2 ◈K أجل يوم) → satır dolduruldu; kayıtta 0 uyuşmaz; [x/y] 0 (54 sayım)",
 ],
 (4, 7): [
  "esmâ: blokta e_oto token yok; KARAR 621 (değişmedi); geçerli mühür yok",
  "kök tablosu: kok_ekle_65 1 kök (حيض, 65:4; 1430 → 1431; gloss 'mahîd / yahid', korpus 2 ayet); retroaktif yama hedef 1 (2:222 — sûre 2 kısmi okunduğu için hedefe giriyor, kaydı yok, henüz okunmadı), yama 0, genel geçiş 0",
  "yıldız (924): 65:4 ★ n z=1,65, 65:6 ★★ n z=2,08 (uzun ayet); 65:5 ★★ allah z=2,33, 65:7 ★ allah z=1,87 — içerik iddiası değil",
  "sayı işareti (924): 65:4 'idde' (sayma) ve 'selâse' (üç ay) — 'selâse' gerçek sayı, iddet süresi",
  "biçim (924): 65:7 ölçüm şahıs alanında 1S 1 — metinde 1S yok (etiket hatası olabilir); araç alanı",
  "gloss (1021 ailesi): 65:5 كفر 'yukeffir' (örtme) — gloss 'inkâr, nankörlük' (64:9 ile aynı açık); 65:7 قدر 'qudira aleyhi rizquh' (daraltma) — gloss 'ölçü, güç yetirme'",
  "nakarat3 (1003): 65:2 / 65:4 've men yetteqi'llâhe yec'al lehû' GEÇER; 65:2 / 65:4 / 65:5 've men yetteqi'llâh' GEÇER — sûre içi blok 1 ile kapandı",
  "çıpa sınır vakası (kayıt, karar istemiyor): 65:4 biyolojik durumlara göre üç sınıf + süre — L4 sınıf kolu kelimesel olarak uyar, ama sınıflama ve ölçü hukukî (iddet); L1 yazıldı, 799 ilkesine göre",
  "aday 1040 (kayıt): 64:9 / 65:5 'yukeffir anhu seyyi'âtihî' — ardışık sûreler; test yok",
  "aday 1041 (kayıt): 65:5 / 65:6 kök أجر 'ecrâ' (Allah'ın ödülü) / 'ucûrahunne' (emzirenin ücreti)",
  "adsız (aday 1017): 65:4 kadınlar (üç sınıf); 65:6 çocuk ('lehû'), emziren başka kadın ('uhrâ'); 65:7 'zû se'a', 'men qudira aleyhi', edilgen 'qudira' daraltan — ad verilmedi",
  "çıpa: L1 65:4 (biyolojik durumlar, iddet sınıfları), L0 65:6 (gebelik, doğum, emzirme); tarayıcı v4 adayı 65:4, çıpa değil",
  "karşıt çift (aday 1039, okuma): 65:4 aybaşından umut kesenler / henüz görmeyenler; 65:5 kötülükler / ödül; 65:6 oturtun / sıkıştırmayın, danışın / anlaşamazsanız; 65:7 geniş / daraltılmış, zorluk / kolaylık — kayıt, test yok",
  "okuma: 60:13, 22:2, 18:88 → 65:4; 64:9, 29:7 → 65:5; 22:2, 28:7, 28:20 → 65:6; 24:22, 23:62 → 65:7 — KAPATILAMAZ",
  "kendi kaydı (kayıttan önce): 65:4'te 'selâse' için 'sûrede ilk gerçek sayı' yazılmıştı — 65:2 'zevey' (iki) sayılmadan; 'süre sayıyla veriliyor' olarak düzeltildi",
  "tetik: ön kuru koşu 3 uyuşmaz (65:4 ◈K أجل, ◈B حمل وضع; 65:6 ◈B حمل وضع) → satırlar dolduruldu; kayıtta 0 uyuşmaz; [x/y] 0 (71 sayım)",
 ],
 (8, 12): [
  "esmâ: e_oto 2 token (65:11 'nûr' — 'ile'n-nûr', mecaz, DEĞİL; 65:12 'qadîr' — İLÂHÎ); KARAR 621 → 623; 65:12 'qadîr' orta konum, ardından 've enna'llâhe qad ehâta …' — bilanço geçerli mühür yok",
  "kök tablosu: blok 8-12 için karşılık eksiği yok; 1431 kök; retroaktif yama hedef yeni kök yok",
  "yıldız (924): 65:10 ★★★ allah z=3,22 (16 kelimede 3 lafız), 65:11 ★★ n z=2,29 (34 kelime), 65:12 ★ allah z=1,87 — içerik iddiası değil",
  "sayı işareti (924): 65:10 'e'adde' — kök عدد, 'hazırladı', sayı değil (sûre 58 dersi); 65:12 'seb'' gerçek sayı (yedi gök)",
  "biçim (924): 65:8 3MS 'rabbihâ' → 1P 'hâsebnâhâ', 'azzebnâhâ' — ölçüm iltifât 0; mm2 65:8 (meful mutlak ×2) ölçümle uyumlu",
  "gloss (1021 ailesi): 65:11 ظلم 'ez-zulumât' (karanlık) — gloss 'zulüm'; 65:10 عدد 'e'adde' (hazırlama) — gloss 'sayma, sayı'",
  "aday 1040 (kayıt): 64:5 / 65:9 'zâqû / zâqat vebâle emri-'; 64:9 / 65:11 've men yu'min bi'llâhi ve ya'mel sâlihan … yudhilhu cennâtin … ebedâ' — ardışık sûreler; 65:12 → 66:1 sûre sınırı 66:1 henüz okunmadığı için yazılmadı; test yok",
  "aday 1041 (kayıt): 65:8 'emri rabbihâ' (Rabbin emri) / 65:9 'emrihâ' (kasabanın işi) — aynı kelime Rab ve kasaba için, ardışık ayetlerde",
  "kök iki anlam (okuma, D3): عدد 65:1, 65:4 'idde' (sayma) / 65:10 'e'adde' (hazırlama); ظلم 65:1 'zaleme' (zulüm) / 65:11 'ez-zulumât' (karanlık); قدر 65:3 / 65:7 / 65:12",
  "adsız (aday 1017): 65:8 kasaba ('qarye'), elçiler; 65:10 halk ('lehum'); 65:11 elçi ('rasûlen'); 18:87 emsalinde konuşan — ad verilmedi",
  "çıpa: L1 65:12 (yedi gök ve yer; 41:12 emsali, L4 sınırda, KAPATILAMAZ); 65:8 kasaba, 65:11 mecaz / âhiret — olgu değil; tarayıcı v4 adayı 65:11, 65:12 — çıpa değil",
  "karşıt çift (aday 1039, okuma): 65:11 karanlıklar / aydınlık; 65:12 gökler / yer; 65:8, 9, 10 yok — kayıt, test yok",
  "okuma: 47:13, 51:44, 18:87 → 65:8; 59:15, 64:5 → 65:9; 58:15 → 65:10; 57:9, 64:9 → 65:11; 41:12, 17:44, 64:18 → 65:12 — KAPATILAMAZ",
  "kendi kaydı (kayıttan önce): 65:11'de ölçüm xref 3:101, 3:113 (henüz okunmadı) yazılmamıştı — eklendi",
  "tetik: ön kuru koşu 3 uyuşmaz (65:11 ◈K نهر أبد; 65:12 ◈K سمو أرض, ◈B خلق) → satırlar dolduruldu; kayıtta 0 uyuşmaz; [x/y] 0 (73 sayım)",
 ],
}

DUZELTME = {
}
