# -*- coding: utf-8 -*-
"""cin_kayit.py — sûre 72 (Cin) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 72

CIPA = {
 # blok 1-10
 8: dict(kademe='L1', olgu=True, cipa=False, not_="'lemesne's-semâ'e fe-vecednâhâ muli'et harasen şedîden ve şuhubâ' — gök + alevler ('şuhub') + doldurulmuşluk; mekanizma / ölçü yok — L1 (37:10 emsali); 'haras' bekçiler gaybî (olgu=False); cinler olgu değil; tarayıcı vermedi"),
 9: dict(kademe='L1', olgu=True, cipa=False, not_="'yecid lehû şihâben rasadâ' — alev + gözetleme işlevi; mekanizma yok — L1 (37:10 emsali); tarayıcı vermedi"),
 # blok 11-20
 15: dict(kademe=None, olgu=False, cipa=False, not_="'li-cehenneme hatabâ' — cehennem, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 16: dict(kademe='L1', olgu=True, cipa=False, not_="'le-esqaynâhum mâ'en ğadeqâ' — su + içirme, şarta bağlı ('lev'); kaynak / mekanizma yok — L1 (56:68 emsali); tarayıcı v4 adayı (A_şart), çıpa değil"),
 # blok 21-28
 23: dict(kademe=None, olgu=False, cipa=False, not_="'nâra cehenneme hâlidîne fîhâ ebedâ' — cehennem, ebedîlik; âhiret (olgu=False); merdiven uygulanmadı; tarayıcı v4 adayı, çıpa değil"),
 24: dict(kademe=None, olgu=False, cipa=False, not_="'raev mâ yû'adûn … eqallu 'adedâ' — vaat edilen (âhiret / azap); sayı karşılaştırması nicelik, doğal olgu yok (olgu=False); tarayıcı v4 adayı, çıpa değil"),
 25: dict(kademe=None, olgu=False, cipa=False, not_="'em yec'alu lehû rabbî emedâ' — süre adı, birim yok; ölçülen vaat edilen (gaybî, olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 28: dict(kademe=None, olgu=False, cipa=False, not_="'ahsâ kulle şey'in 'adedâ' — her şeyin sayılması; doğal olgu adı yok, olgu=False; merdiven uygulanmadı (36:12 aynı kurgu); tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: e_oto 2 token (72:2, 72:7 'ehad' — nefy içinde 'hiç kimse'); ikisi DEĞİL; KARAR 662 → 664; esma_kayit mühür EVET ×2, karar sonrası geçersiz (1022); blokta geçerli mühür yok",
  "kök tablosu: kok_ekle_72 1 kök (حرس 72:8, gloss korpus 1 ayet; blok_dikey 'KARŞILIK YOK' → eklendi); 1452 → 1453; retroaktif yama hedef 0, yama 0, genel geçiş 0",
  "hapaks (yeni kök dersi): 72:8 ★★★ hapaks z=3,28 (pas 1,57 de eşik üstü) — yeni kökün tek tokeni; içerik iddiası değil",
  "yıldız (924): 72:2 ★★ rab z=2,05, 72:3 ★★ rab z=2,05, 72:4 ★★ allah z=2,33, 72:7 ★ allah z=1,69, 72:10 ★ pas z=1,57 — içerik iddiası değil; öbür dört ayet yıldızsız",
  "harf alanı: ayet 1 ölçümünde harf 72 → harf3 49, isaret 0 (ayet 1 ailesi; besmele); araç alanı (924); KAPATILAMAZ",
  "sayı işareti: 72:2, 72:7 'ehad' — sayı değil, nefy içinde 'hiç kimse' (kök kaynaklı yanlış alarm, sûre 58 dersi ailesi)",
  "gloss (1021): جدد 72:3 'cedd' (şan, ululuk) — gloss 'yenilik, yeni olma'",
  "◈K tetik dışı: 72:8 'şuhub', 72:9 'şihâb' (شهب) — gök cismi / alev, tetik listesinde değil; 72:8 satırı سمو ile dolu, 72:9 '—', gözlem ◇'de",
  "◈B: 72:1, 72:9 tetik سمع işitme işlevi; 72:5, 72:6 tetik أنس — cin canlı sınıfı değil notuyla; satırlar dolu",
  "ölçüm kip (517 ailesi): 'inne' / 'enne' tekidi kip alanında yok; 72:7 teşbih 'kemâ', 72:10 'em' muâdelesi biçim alanında yok",
  "ölçüm iltifât: 72:7 2MP muhatap girişi ('zanentum') iltifât sayılmıyor (araç alanı, 924); muhatap adsız",
  "nakarat3: 72:5 'ennâ zanennâ en len' ve 'zanne en len' (72:5, 72:7 + henüz okunmamış 1 ayet) — GEÇER, sûre içi",
  "esit2 / xref: blokta esit2 yok; 72:2 xref 18:38 (basıldı) ve okunmuş 1 ayet; öbür dokuz ayette xref yok; lemma eşleri 6:101, 80:36 (sâhibe), 4:43, 5:6, 6:7 (lemese) henüz okunmadı",
  "adsız (aday 1017): 72:1 'qul' muhatabı ve 1S 'ileyye', 'ûhiye' faili; 'nefer'; 72:4 'sefîhunâ'; 72:6 adamlar; 72:7 2MP muhatap; 72:8 'muli'et' faili; 72:10 'urîde' faili — ad verilmedi; metnin adladıkları (cin, insan, Kur'an, Allah, Rab) adıyla anıldı",
  "çıpa: 72:8 L1 (gök + alevler), 72:9 L1 (alev, gözetleme) — 37:10 emsali; 'haras' gaybî olgu=False; 72:10 'fi'l-ard' mekân — merdiven yok; tarayıcı adayı yok; L4 yok",
  "fâsıla: 72:1-10 hepsi ا (71:5'ten bu yana); ölçüm kafiye kırığı 0",
  "aday 1040 (kayıt): 71:28 'rabbi'ğfir lî … illâ tebârâ' / 72:1 'qul ûhiye ileyye …' — sûre sınırı; fâsıla ا → ا; test yok",
  "aday 1041 (kayıt): 72:10 'urîde' (edilgen, fail adsız) / 'erâde rabbuhum' — fail adsız, vaka sayılmadı; 'ehad' 72:2, 72:7 insan / kimse — sûrede Allah için 'ehad' yok (şimdiye dek); vaka yok",
  "karşıt çift (aday 1039, okuma): 72:5 ins / cinn; 72:6 ins adamları / cin adamları; 72:9 geçmiş / şimdi; 72:10 şer / reşad, edilgen / etken; öbür altı ayette yok",
  "tetik: ön kuru koşu 6 uyuşmaz (72:1 ◈B سمع; 72:5 ◈B أنس; 72:6 ◈B أنس; 72:8 ◈K سمو; 72:9 ◈B سمع; 72:10 ◈K أرض — satırlar dolduruldu); kayıtta 0; [x/y] 0 (71 sayım)",
  "süreç (kendi hatam, sunumdan önce): kayıt yaması betiği ilk denemede bir assert'te durdu, sonraki komutlar ayrı satırda olduğu için blok betiği boş CIPA / ARIZA ve yer tutucu başlıkla bir kez koştu; yama tamamlanıp aynı blok betiği sunumdan önce yeniden koşuldu (okuma_metni kaydı bütünüyle yeniden yazıldı); mercek metni yalnız bir yazım hatası ('5. 4 / 72:4') düzeltilerek aynı",
 ],
 (11, 20): [
  "esmâ: e_oto 2 token (72:18, 72:20 'ehad' — nehy / nefy içinde 'hiç kimse'); ikisi DEĞİL; KARAR 664 → 666; esma_kayit mühür EVET ×2, karar sonrası geçersiz (1022); blokta geçerli mühür yok",
  "kök tablosu: kok_ekle_72 5 kök (هرب 72:12, حري 72:14, حطب 72:15, غدق 72:16, لبد 72:19; blok_dikey 'KARŞILIK YOK' → eklendi; حطب ve لبد korpusta 2'şer ayet, öbürleri henüz okunmadı — gloss'ta ayet numarası yok); 1453 → 1458; retroaktif yama hedef 0, yama 0, genel geçiş 0",
  "hapaks (yeni kök dersi): 72:12 هرب, 72:14 حري, 72:16 غدق ★★★ hapaks z=3,28 — yeni köklerin tek tokeni; içerik iddiası değil",
  "yıldız (924): 72:18 ★★★ allah z=4,47 (8 kelimede 2 lafız), 72:20 ★★ rab z=2,34, 72:17 ★ rab z=1,81 — içerik iddiası değil; öbür dört ayet yıldızsız",
  "sayı işareti: 72:18, 72:20 'ehad' — sayı değil (kök kaynaklı yanlış alarm)",
  "ölçüm kip (517 ailesi): 72:20 'innemâ' hasrı biçim HASR olarak yok ('innemâ' hasrı dersi); 72:17 ta'lîl 'li' kip alanında yok",
  "ölçüm iltifât: 72:18 ve 72:19 iltifât 1 sayılıyor; 72:16 cinlerin 1P'sinden su içiren 1P'ye geçiş sayılmıyor (iki 1P aynı kişi biçimi; araç alanı, 924)",
  "konuşan katmanı (aday 1017, okuma): 72:1'de açılan cinlerin 1P sözü 72:15'e dek 've ennâ / ennehû' ile sürüyor; 72:16 'en lev' 72:1 bildiriminin devamı olabilir; 72:16-17 1P içiren / sınayan, 72:18-19 've enne' — sınır metinde işaretli değil, adlandırılmadı; KAPATILAMAZ",
  "nakarat3: 72:12 'ennâ zanennâ en len' (72:5 ile) ve 'zanne en len' (72:5, 72:7, 72:12) — GEÇER, sûre içi",
  "esit2 / xref: blokta esit2 yok; 72:13 xref okunmuş 1 ayet; 72:20 xref henüz okunmamış 4 ayet (2:68-70, 7:134); öbür sekiz ayette xref yok",
  "adsız (aday 1017): 72:11 ve 72:14 gruplar; 72:13 inanan 'men'; 72:16-17 1P içiren / sınayan; 72:17 yüz çeviren 'men'; 72:18 2MP muhatap; 72:19 'abdu'llâh' (izâfet, ad değil) ve 3MP; 72:20 'qul' muhatabı — ad verilmedi; metnin adladıkları (Allah, Rab, cehennem, müslimler / qâsitler cins adı) adıyla anıldı",
  "çıpa: 72:16 L1 (su + içirme, şarta bağlı; 56:68 emsali) — tarayıcı v4 adayı (A_şart), çıpa değil; 72:15 cehennem odun olgu=False; 72:12 'fi'l-ard' mekân — merdiven yok; L4 yok",
  "fâsıla: 72:11-20 hepsi ا; ölçüm kafiye kırığı 0",
  "aday 1040 (kayıt): blokta sûre sınırı yok; vaka yok",
  "aday 1041 (kayıt): lemma 'de'â' 72:18 (2MP yasak), 72:19 (kul), 72:20 (1S) — hepsi insan / kul fiili, Allah'ın fiili değil; vaka yok. Kökün iki kullanımı (Allah değil): 'tarîqa' 72:11 gruplar / 72:16 yol; قوم 72:16 'istaqâmû' / 72:19 'qâme'",
  "karşıt çift (aday 1039, okuma): 72:11 iyiler / diğerleri; 72:12 yerde / kaçarak; 72:14 müslimler / qâsitler; ayetler arası 72:14 / 72:15 (reşad / cehennem odunu) ve 72:16 / 72:17 (istikamet / yüz çevirme); öbür beş ayette yok",
  "tetik: ön kuru koşu 3 uyuşmaz (72:12 ◈K أرض; 72:13 ◈B سمع; 72:16 ◈K موه — satırlar dolduruldu); kayıtta 0; [x/y] 0 (61 sayım)",
 ],
 (21, 28): [
  "esmâ: e_oto 4 token (72:22 'ehad' DEĞİL; 72:25 'qarîb' DEĞİL — vaat edilenin yakınlığı, 70:7 kararıyla aynı; 72:26 ''âlim' İLÂHÎ — 'âlimu'l-ğayb', göndergesi 72:25 Rab, sınıf E; 72:26 'ehad' DEĞİL); KARAR 666 → 670; esma_kayit mühür EVET ×3 (72:22, 25, 26), karar sonrası geçerli 0 — 72:26'da İLÂHÎ token ORTA, son token DEĞİL (1022)",
  "kök tablosu: kok_ekle_72 bu blokta 0 kök (blok_dikey 'karşılık eksiği yok'); 1458 değişmedi; retroaktif yama hedef 0, yama 0, genel geçiş 0",
  "yıldız (924): 72:23 ★ allah z=1,97, 72:24 ★ pas z=1,57, 72:25 ★ rab z=1,62 — içerik iddiası değil; öbür beş ayet yıldızsız",
  "sayı işareti: 72:22, 72:26 'ehad' — sayı değil; 72:24 'eqall', ''aded' ve 72:28 ''aded' — nicelik / sayma kavramı, sayı kelimesi değil",
  "◈B: 72:27 tetik يدي 'beyne yedeyhi' deyimsel (önünden), organ anlamı değil — satır dolu, not düşüldü (kök düzeyi tetik kuralı)",
  "◈K: 72:23 tetik أبد 'ebedâ' — âhiret ebedîliği; satır dolu",
  "ölçüm kip (517 ailesi): 'inne' tekidi kip alanında yok; 72:28 ta'lîl 'li' kip alanında yok; 72:23 ve 72:27 ISTISNA, 72:24 FUT var",
  "konuşan katmanı (aday 1017, okuma): 'qul' 72:20, 21, 22, 25 — 1S konuşan adsız; 72:23 'illâ belâğan' 72:22'nin istisnası; 72:26-28 3MS anlatım 'qul' çerçevesi içinde mi, metin belirtmiyor — adlandırılmadı",
  "esit2 / xref: blokta esit2 yok; 72:22 xref 18:27 (basıldı); 72:23 xref 4:14 (henüz okunmadı), 33:36, 9:63 (basıldı); 72:28 xref 7:79, 7:93 (henüz okunmadı); öbür beş ayette xref yok",
  "adsız (aday 1017): 'qul' muhatabı ve 1S konuşan; 2MP muhatap (72:21, 25); elçi 'rasûl' (72:23, 27, adsız); isyan eden 'men'; 72:24 3MP ve vaat eden (edilgen); gözetleyiciler (72:27); elçiler 3MP (72:28); 72:28 'li-ya'leme' öznesi — ad verilmedi; metnin adladıkları (Allah, Rab, cehennem) adıyla anıldı",
  "çıpa: blokta doğal olgu yok; 72:23 (cehennem, ebedîlik) ve 72:24 (vaat edilen) olgu=False — ikisi de tarayıcı v4 adayı, çıpa değil; 72:25 'emed' ve 72:28 'ahsâ … 'adedâ' olgu=False; L4 yok",
  "fâsıla: 72:21-28 hepsi ا; sûrenin 28 ayeti de ا (71:5'ten bu yana kesintisiz); ölçüm kafiye kırığı 0",
  "aday 1040 (kayıt): 72:28 → 73:1 yazılmadı (73 henüz okunmadı)",
  "aday 1041 (kayıt): vaka yok — 'seleke' 72:17, 72:27 iki geçişte de Rab (3MS); 71:20 'li-teslukû' insan fiili (ardışık sûre, aynı sûre değil); 'rasad' 72:9 alev / 72:27 gözetleyiciler — Allah için değil",
  "karşıt çift (aday 1039, okuma): 72:21 zarar / reşad; 72:25 yakın / süre; 72:26 gayb / açığa çıkarma; 72:27 önünden / arkasından; öbür dört ayette yok",
  "tetik: ön kuru koşu 2 uyuşmaz (72:23 ◈K أبد; 72:27 ◈B يدي — satırlar dolduruldu); kayıtta 0; [x/y] 0 (69 sayım)",
 ],
}

DUZELTME = {
}
