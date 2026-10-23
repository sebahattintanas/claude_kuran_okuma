# -*- coding: utf-8 -*-
"""mumtehine_kayit.py — sûre 60 (Mümtehine) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 60

CIPA = {
 # blok 1-3
 3: dict(kademe=None, olgu=False, cipa=False, not_="'yevme'l-qiyâmeti yefsilu beynekum' — kıyamet günü, âhiret; doğal olgu değil; tarayıcı vermedi"),
 # blok 4-7
 6: dict(kademe=None, olgu=False, cipa=False, not_="'yercu'llâhe ve'l-yevme'l-âhir' — âhiret günü; doğal olgu değil; tarayıcı vermedi"),
 # blok 11-13
 11: dict(kademe=None, olgu=False, cipa=False, not_="'ezvâc' insan eşleri; tarayıcı adayı (زوج, şart + ölçü işareti) — doğal olgu değil, çıpa yok"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'el-âhire' âhiret; 'ashâbu'l-qubûr' kabirdekiler — doğal olgu değil; tarayıcı vermedi"),
}

ARIZA = {
 (1, 3): [
  "esmâ: e_oto 2 token (60:1 'evliyâ'', 60:3 'basîr'); 'evliyâ'' DEĞİL (çoğul dostlar), 'basîr' İLÂHÎ (lafzın haberi); KARAR 561 → 563; bilanço geçerli mühür 60:3 (ölçüm satırı 'SON, MÜHÜRSÜZ' — 1022 ailesi)",
  "harf alanı: ayet 1 ölçümünde harf 247 → harf3 214, isaret 0 (56:1-59:1 ailesi); 60:2-3'te fark = isaret (4, 3) — besmele harfleri olabilir; araç alanı, metin hakkında kanıt değil (aday 924); KAPATILAMAZ",
  "morph etiketi (924): 60:3:2 'tenfe'a' 2MS etiketli (ölçüm 2MS 1); okumada fail 'erhâmukum' — sahset alanı etkileniyor",
  "gloss (1021 ailesi): kök رحم tablosu 'rahmet, merhamet' — 60:3 'erhâm' (akrabalar) anlamı yazılmıyor",
  "biçim (517 ailesi): 60:1 1S konuşan ('aduvvî', 'sebîlî', 'merdâtî', 'ene a'lemu') ile 3. şahıs 'bi'llâhi rabbikum' aynı ayette — iltifât 0",
  "kök tablosu: sûre 60 blok 1-3'te eksik kök yok (kok_ekle_60 boş); retroaktif yama 0",
  "adsız (aday 1017): 60:1 inananlar (muhatap), düşmanlar, elçi ('er-rasûl') adsız; konuşan 1S; 60:2 düşmanlar adsız — ad verilmedi",
  "aday 1040 alanı (kayıt, test yok): 59:24 → 60:1 — ad dizisi ve tesbihle kapanış / nidâ ve yasakla açılış; 59:18 aynı nidâ; fâsıla م → ل",
  "aday 1041 alanı (kayıt, test yok): lemma 'veliyy' esmâ listesinde / 60:1 'evliyâ'' (dostlar)",
  "karşıt çift (aday 1039, okuma): 60:1 düşman / dost, gizli / açık, sevgi / inkâr; 60:1 'meveddet' / 60:2 'veddû lev tekfurûn'; 60:2 eller / diller; 60:3 dünya bağları / kıyamette ayırma — kayıt, test yok",
  "yıldız: 60:1 ★★★ n z=3,78 (48 kelime); 60:2-3 yıldızsız",
  "sûre içi kalıp eşleri henüz okunmadı: 60:1 → 60:13 ('yâ eyyuhe'llezîne âmenû lâ', nakarat3 GEÇER); 60:1 → 60:7 (meveddet); 60:1 → 60:8, 9 (ahrace)",
  "çıpa: 60:3 kıyamet, olgu değil; doğal olgu yok; tarayıcı adayı yok; L4 yok",
  "okuma: 9:23, 59:8, 59:18, 59:24 → 60:1; 60:1 → 60:2; 47:22, 26:88, 22:17, 57:4, 58:22 → 60:3 — KAPATILAMAZ",
  "tetik: ön kuru koşu 3 tetik satırı (60:2 B, 60:3 K, B) — kayıtta 0 uyuşmaz; [x/y] 0 (47 sayım)",
  "kendi kaydı (kayıttan önce): 60:3'te basılmamış okunan eşler hakkında anlam iddiası ('rahimler') silindi",
 ],
 (4, 7): [
  "esmâ: e_oto 8 token (60:5 'azîz', 'hakîm'; 60:6 'âhir', 'ğanî', 'hamîd'; 60:7 'qadîr', 'ğafûr', 'rahîm'); 7'si İLÂHÎ, 60:6 'âhir' DEĞİL (günün sıfatı, 58:22 emsali); KARAR 563 → 571; bilanço geçerli mühür 60:5, 6, 7",
  "sayı işareti (aday 924): 60:4 'vahdeh' ('tek başına') sayı işareti aldı — anlam sayma değil",
  "kafiye: 60:6 fâsıla د — KAFİYE KIRILMASI (ölçüm); ★ kaynağı allah z=1,58, kırık tek başına ★ vermiyor (1001 ölçütü, bilanço ile uyumlu)",
  "adlı aktör: İbrâhîm (60:4 ×2) — sûrenin ilk adlı kişisi (bu oturumda okunan 60:1-7 içinde; ölçüm aktör alanı)",
  "adsız (aday 1017): 60:4 İbrâhîm'in beraberindekileri, kavimleri, babası; 60:5 dua eden 1P; 60:7 düşmanlık edilenler — ad verilmedi",
  "alıntı (1017 alanı / 517 ailesi): 60:4 üç iç söz (1P kavme ilan, 1S babaya vaat, 1P Rab'be dua), dua 60:5'te sürüyor; iltifât 0",
  "aday 1041 alanı (kayıt, test yok): lemma 'âhir' 57:3 Allah / 60:6 gün; lemma 'ğanî' 59:7 zenginler / 60:6 Allah (ardışık sûreler); lemma 'berî'' 59:16 şeytan / 60:4 İbrâhîm ve beraberindekiler (aynı 'innî / innâ berî'' yapısı)",
  "karşıt çift (aday 1039, okuma): 60:4 küfür ilanı / tek Allah'a iman şartı, istiğfar vaadi / gücüm yetmez, düşmanlık-öfke / 60:7 sevgi; 60:5 sınama aracı kılma / bağışla; 60:6 umma / yüz çevirme; 60:7 düşmanlık edilenler / sevgi, 60:1 yasak sevgi / 60:7 umulan sevgi — kayıt, test yok",
  "yıldız: 60:4 ★★★ n z=4,20 (52 kelime); 60:7 ★★★ allah z=3,47 (3 lafız / 15 kelime); 60:5 ★★ rab z=2,96; 60:6 ★ allah",
  "kapanan sûre içi eşler: 60:4 ↔ 60:6 ('uswetun hasenah'); 60:1 → 60:7 ('meveddet'; ودد [4/4]); عدو [5/5] ve ربب [4/4] sûre içi son geçişler; henüz okunmayan: 60:7 nakarat3 'allâh ğafûr rahîm' (GEÇMEZ, eş sonraki blokta)",
  "çıpa: 60:6 âhiret günü, olgu değil; doğal olgu yok; tarayıcı adayı yok; L4 yok",
  "okuma: 33:21, 59:16, 40:84, 19:47, 9:114, 42:10 → 60:4; 10:85, 29:26, 60:4 → 60:5; 33:21, 57:24, 57:3, 59:7, 60:4 → 60:6; 60:1, 60:4, 57:28 → 60:7 — KAPATILAMAZ",
  "tetik: ön kuru koşu 2 tetik satırı (60:4 K, 60:6 K) — kayıtta 0 uyuşmaz; [x/y] 0 (54 sayım)",
 ],
 (8, 10): [
  "esmâ: e_oto 2 token (60:10 'alîm', 'hakîm'), ikisi İLÂHÎ (lafzın haberi); KARAR 571 → 573; bilanço geçerli mühür 60:10",
  "gloss (1021 ailesi): kök ظهر tablosu 'sırt; zuhur' — 60:9 'zâherû' (destek verme) ile 33:4 / 58:2-3 zıhâr anlamı ayrı yazılmıyor (58:1-4 kaydının sürmesi)",
  "adsız (aday 1017): 60:8-9 savaşan / savaşmayan, çıkaran / çıkarmayan, destek veren gruplar; 60:10 göç eden inanan kadınlar (3FP), inkârcı kocalar ve inkârcı kadınlar — sınıf, ad verilmedi",
  "aday 1041 alanı (kayıt, test yok): lemma 'ehabbe' 59:9 insanlar / 60:8 Allah; lemma 'imtehane' 49:3 Allah sınar / 60:10 inananlar sınar; kök علم aynı ayette (60:10) Allah'ın bilmesi ('a'lem', 'alîm') ve inananların bilmesi ('alimtumûhunne')",
  "karşıt çift (aday 1039, okuma): 60:8 / 60:9 savaşmayan-çıkarmayan / savaşan-çıkaran, iyilik-adalet / dost edinme, 'el-muqsitîn' / 'ez-zâlimûn'; 60:10 inanan kadınlar / inkârcılar, çapraz helal olmama, iki tarafın 'harcadığını isteme' hakkı, geri göndermeme / tutmama — kayıt, test yok",
  "yıldız: 60:10 ★★★ n z=4,52 (55 kelime; sûre içinde en uzun ayet); 60:8-9 yıldızsız",
  "kapanan sûre içi eşler: 60:8 ↔ 60:9 ('nehâ + lafız + an + ellezî', 'qâtele fi'd-dîn', 'ahrace min diyâr'); 60:1 → 60:8, 9 ('ahrace'; خرج [5/5] sûre içi son); henüz okunmayan: 60:10 → 60:12 ('izâ câ'e + mu'mine', nakarat3 GEÇMEZ), 60:10 → 60:13 (nidâ)",
  "çıpa: doğal olgu yok; tarayıcı adayı yok; L4 yok",
  "okuma: 60:1, 49:9, 59:9 → 60:8; 60:8, 33:26, 33:4, 9:13, 9:23 → 60:9; 60:1, 59:8, 49:3, 59:11, 49:8 → 60:10 — KAPATILAMAZ",
  "tetik: ön kuru koşu 0 tetik satırı (üç ayette ◈K / ◈B tetiği yok) — kayıtta 0 uyuşmaz; [x/y] 0 (40 sayım)",
 ],
 (11, 13): [
  "esmâ: e_oto 4 token — 60:11 'mu'min' DEĞİL (inananların sıfatı), 60:12 'ğafûr', 'rahîm' İLÂHÎ, 60:13 'âhir' DEĞİL ('el-âhire'); KARAR 573 → 577; bilanço geçerli mühür 60:12 (60:11 mühür adayı geçersiz)",
  "lemma çakışması (aday 924, araç boşluğu kanıt değil): lemma 'asâ' 37 ayet listesi değnek ('asâ) geçişlerini de içeriyor; 60:12 'ya'sîneke' için kök عصي sayısı (32 ayet) kullanıldı",
  "tarayıcı adayı 60:11 (زوج, şart + ölçü) — insan eşleri, doğal olgu değil; çıpa yok (CIPA 11 olgu False)",
  "adsız (aday 1017): 60:11 giden eşler ve kocaları; 60:12 biat eden kadınlar (3FP); 60:13 gazaba uğramış topluluk, 'el-kuffâr', 'ashâbu'l-qubûr' — sınıf, ad verilmedi; Nebî 'en-nebiyy' sıfatıyla",
  "okuma ikiliği: 60:13 'kemâ ye'ise'l-kuffâru min ashâbi'l-qubûr' iki yöne açık (inkârcılar kabirdekilerden / kabirdeki inkârcılar umut kesti); meal birincisini aldı, karar verilmedi",
  "karşıt çift (aday 1039, okuma): 60:10 gelen kadınlar / 60:11 giden eşler (aynı ödeme, ters yön); 60:12 'yubâyi'neke' / 'lâ ya'sîneke'; 60:12 'istağfir' / 60:13 'ye'isû' — kayıt, test yok",
  "yıldız: 60:12 ★★ n z=2,72; 60:11, 60:13 yıldızsız",
  "kapanan sûre içi eşler: 60:10 → 60:11 (نفق [4/4] son); 60:10 → 60:12 ('izâ câ'e + mu'mine', GEÇMEZ); 60:7 → 60:12 ('lafız + ğafûr + rahîm', GEÇMEZ); 60:1 → 60:13 ('yâ eyyuhe'llezîne âmenû lâ', GEÇER — sûre başı / sonu dost edinme yasağı); 60:9 → 60:13 (ولي [5/5] son); sûre içinde açık eş kalmadı",
  "fâsıla: sûre içi ر 3 ayet (60:3, 60:4, 60:13); bu blokta kafiye kırığı 0 (sûre içi kırık 60:6, blok 4-7)",
  "okuma: 57:23, 16:126 → 60:11; 60:10, 48:10, 17:31, 24:62, 60:7 → 60:12; 60:1, 58:14, 60:9, 12:87 → 60:13 — KAPATILAMAZ",
  "tetik: ön kuru koşu 2 uyuşmaz (60:11 ◈B زوج, 60:12 ◈B يدي) → satırlar dolduruldu; kayıtta 0 uyuşmaz; [x/y] 0 (53 sayım)",
 ],
}

DUZELTME = {
}
