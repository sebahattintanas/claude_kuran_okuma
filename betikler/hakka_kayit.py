# -*- coding: utf-8 -*-
"""hakka_kayit.py — sûre 69 (Hâkka) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 69

CIPA = {
 # blok 1-10
 5: dict(kademe=None, olgu=False, cipa=False, not_="'fe-uhlikû bi't-tâğiya' — helâk aracı adlanmıyor ('et-tâğiya', aşırı olan); olgu tarifi yok; merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe='L1', olgu=True, cipa=False, not_="'bi-rîhin sarsarin âtiya' — rüzgâr + iki nitelik; süre / ölçü bu ayette yok — L1 (41:16, 54:19 emsali); tarayıcı vermedi"),
 7: dict(kademe='L1', olgu=True, cipa=False, not_="'seb'a leyâlin ve semâniyete eyyâmin husûmen' — rüzgârın süresi sayıyla (gece / gün birimi); olayın süresi, olgunun mekanizması değil — L1; L4 'birim' koluna sınırda, KAPATILAMAZ; 'a'câzu nahlin hâviya' teşbih aracı (olgu=False); tarayıcı v4 adayı (F_ölçü), çıpa değil"),
 # blok 11-20
 11: dict(kademe='L1', olgu=True, cipa=False, not_="'tağe'l-mâ'' — su + taşma fiili; ölçü / mekanizma yok — L1 (54:11 emsali); 'el-câriya' (gemi) araç, olgu=False (36:41 emsali); tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'nufiha fi's-sûr' — sûr araç, gelecek sahnenin olayı; doğal olgu değil; merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe='L1', olgu=True, cipa=False, not_="'humileti'l-ardu ve'l-cibâlu fe-dukketâ dekketen vâhida' — yer + dağ + hâl (kaldırılma, dağıtılma); 'vâhida' tek darbe, ölçü / mekanizma değil — L1 (56:4-5 emsali); tarayıcı vermedi"),
 16: dict(kademe='L1', olgu=True, cipa=False, not_="'inşaqqati's-semâ'u fe-hiye yevme'izin vâhiya' — gök + hâl (yarılma, gevşeklik); süreç / ölçü yok — L1 (55:37 emsali); tarayıcı vermedi"),
 17: dict(kademe=None, olgu=False, cipa=False, not_="'el-melek', 'arş', 'semâniya' — âhiret sahnesi (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 21-30
 22: dict(kademe=None, olgu=False, cipa=False, not_="'fî cennetin âliya' — âhiret cenneti (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 23: dict(kademe=None, olgu=False, cipa=False, not_="'qutûfuhâ dâniya' — cennet salkımları, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 31-41
 32: dict(kademe=None, olgu=False, cipa=False, not_="'silsiletin zer'uhâ seb'ûne zirâ'â' — âhiret sahnesinde insan yapımı araç (zincir), uzunluk birimiyle; doğal olgu değil (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: blokta e_oto token yok; KARAR 653 değişmedi; geçerli mühür yok",
  "kök tablosu: kok_ekle_69 2 kök (حسم 69:7, gloss korpus 1 ayet; صرع 69:7, gloss korpus 1 ayet — ikisi de blok_dikey 'KARŞILIK YOK'); 1441 → 1443; retroaktif yama hedef 0, yama 0, genel geçiş 0",
  "hapaks (49:11 dersi): 69:7 ★★★ hapaks z=6,79 — iki yeni kökün korpustaki tek tokeni; içerik iddiası değil",
  "yıldız (924): 69:5, 69:6 ★★★ pas z=5,38 (tek fiil edilgen), 69:10 ★★★ rab z=3,23 (6 kelimede 1 Rab) — içerik iddiası değil",
  "harf alanı: ayet 1 ölçümünde harf 25 → harf3 6, isaret 0 (ayet 1 ailesi, tek kelimelik ayet); araç alanı (924); KAPATILAMAZ",
  "gloss (1021 ailesi): عود 69:4, 69:6 'Âd (kavim adı) — gloss 'geri dönme'; lemma 'Âd korpus listesi 'âd (2:173, 6:145 — haddi aşan) ile birleşik — sayı verilmedi; lemma 'asâ (عصي) listesi değnek 'asâ ile birleşik görünüyor — sayı verilmedi",
  "sayı işareti: 69:7 'seb'' ve 'semâniye' — gerçek sayı (gece / gün)",
  "esit2 / xref: 69:3 ↔ 86:2, 90:12, 104:5 BENZER (henüz okunmadı); blokta başka bağ yok",
  "adsız (aday 1017): 2MS muhatap (69:3, 7, 8), helâk eden (edilgen 69:5-6), 'sehharahâ' faili, 'men qablehû', 'el-mu'tefikât', 'rasûl', 'ehazehum' faili — ad verilmedi; metnin adladıkları (Semûd, 'Âd, Fir'avn) adıyla anıldı",
  "çıpa: 69:6 L1, 69:7 L1 (sayılı süre, L4 'birim' koluna sınırda — KAPATILAMAZ); 69:5 olgu=False; tarayıcı v4 adayı 69:7 (F_ölçü), çıpa değil; L4 yok",
  "fâsıla: blok içi on ayet ة (H sınıfı); kafiye kırığı 0 (blok içi); 68:52 ن → 69:1 ة sûre sınırında sınıf değişimi",
  "aday 1040 (kayıt): 68:52 'zikrun li'l-âlemîn' / 69:1 'el-hâqqa' — sûre sınırı, cevapla kapanış → tek kelimelik adla açılış; test yok",
  "aday 1041 (kayıt): blokta vaka yok",
  "karşıt çift (aday 1039, okuma): 69:7 geceler / günler; öbür dokuz ayette yok",
  "tetik: ön kuru koşu 2 uyuşmaz (69:6 ◈K روح, 69:7 ◈K ليل يوم — satırlar dolduruldu); kayıtta 0; [x/y] 0 (39 sayım)",
 ], (11, 20): [
  "esmâ: blokta e_oto token yok; KARAR 653 değişmedi; geçerli mühür yok",
  "kök tablosu: kok_ekle_69 3 kök (وهي 69:16 ve هاء 69:19 — ikisi korpus 1 ayet; جمم — 69:14 دكك dikey komşuluğunda 'KARŞILIK YOK', 89:20 henüz okunmadı, sûre 67 وسق emsali); 1443 → 1446; retroaktif yama hedef 0, yama 0, genel geçiş 0",
  "hapaks (49:11 dersi): 69:16 ve 69:19 ★★★ hapaks z=3,28 — yeni köklerin tek tokeni; içerik iddiası değil",
  "yıldız (924): 69:13, 69:14 ★★★ pas z=5,38; 69:18 ★★ pas z=2,52; 69:17 ★★ rab z=2,05; 69:19 hapaks ve pas (z=1,57) birlikte — içerik iddiası değil",
  "sayı işareti: 69:13, 69:14 'vâhida' (bir), 69:17 'semâniya' (sekiz) — gerçek sayı; 69:17'de sayılanın ne olduğu adlanmıyor",
  "ölçüm kip (517 ailesi): 69:11, 69:20 tekit 'inne' kip alanında yok; 69:13 şart 'izâ' kip alanında yok (69:19 'men' COND yazılıyor)",
  "ölçüm iltifât: 69:10 3MP → 69:11 1P / 2MP ölçümde iltifât değil (araç alanı, 924)",
  "◈B tetik kök düzeyinde: حمل 69:11 'hamalnâkum', 69:14 'humilet', 69:17 'yahmilu' — taşıma / kaldırma, gebelik değil; satırlar dolu, B4'te not (ön-kayıt §4)",
  "esit2 / xref: blokta esit2 yok; 69:19 xref 17:71 (okundu), 84:7 (henüz okunmadı); nakarat3 69:19 / 69:25 süzgeç GEÇMEZ (69:25 henüz okunmadı)",
  "adsız (aday 1017): 1P konuşan ve 2MP muhatap (69:11-12, 18), gemi ve taşınanlar, üfüren ve kaldıran (edilgen 69:13-14), 'el-melek', 'semâniya', kitabı sağından verilen, 2MP dinleyenler — ad verilmedi",
  "çıpa: L1 3 (69:11 su, 69:14 yer ve dağlar, 69:16 gök); olgu=False 69:13 (sûr), 69:17 (arş sahnesi), 69:11 gemi; tarayıcı adayı yok; L4 yok",
  "fâsıla: blok içi ة (69:11-18) ve ه (69:19-20), hepsi H sınıfı; kafiye kırığı 0 (blok içi)",
  "aday 1040 (kayıt): blokta sûre sınırı yok; vaka yok",
  "aday 1041 (kayıt): blokta vaka yok",
  "karşıt çift (aday 1039, okuma): on ayette yok",
  "tetik: ön kuru koşu 9 uyuşmaz (69:11 ◈K موه ◈B حمل; 69:14 ◈K أرض جبل ◈B حمل; 69:15-18 ◈K يوم / سمو; 69:17 ◈B حمل — satırlar dolduruldu); kayıtta 0; [x/y] 0 (51 sayım)",
 ], (21, 30): [
  "esmâ: blokta e_oto token yok; KARAR 653 değişmedi; geçerli mühür yok",
  "kök tablosu: kok_ekle_69 1 kök (قطف 69:23, gloss korpus 2 ayet; blok_dikey 'KARŞILIK YOK'); 1446 → 1447; retroaktif yama hedef 0, yama 0; genel geçiş ilk koşuda 2 ek gloss yaması verdi (okuma_metni içi; ikinci koşu 0)",
  "yıldız (924): 69:25 ★★★ pas z=3,48 — içerik iddiası değil; öbür dokuz ayet yıldızsız",
  "ölçüm iltifât (1017 ailesi): 69:21 (69:20 1S alıntı → 3MS anlatı), 69:24 (anlatı → 2MP alıntı), 69:25 (anlatı → 1S alıntı), 69:27 (1S → 3FS) — alıntı sınırı ve alıntı içi zamir iltifât sayılıyor",
  "esit2 / xref: 69:21 ↔ 101:7 TAM (henüz okunmadı; ölçüm aynı eşi iki kez yazıyor), 69:22 ↔ 88:10 TAM (henüz okunmadı); 69:24 xref 52:19 (okundu), 77:43 (henüz okunmadı); 69:25 xref 3:20 (henüz okunmadı); nakarat3 69:19 / 69:25 GEÇMEZ",
  "ölçüm kip (517 ailesi): 'leyt' temennisi (69:25, 69:27) kip alanında yok (VOC yazılıyor)",
  "gloss (1021 ailesi): غلل 69:30 'ğullûh' (bağlayın) — gloss kin / boyunduruk / hıyanet çok anlamlı; lemma 'ğalle' listesi 3:161 'ğalle' (hıyanet) ile birleşik",
  "adsız (aday 1017): kitabı sağından / solundan verilen, 69:24 ve 69:30'da konuşan, 2MP muhataplar, 69:27 'hâ' göndergesi — ad verilmedi",
  "çıpa: blokta doğal olgu yok (69:22-23 cennet, âhiret, olgu=False); tarayıcı adayı yok",
  "fâsıla: blok içi ة (69:21-24, 27) ve ه (69:25-26, 28-30), hepsi H sınıfı; kafiye kırığı 0 (blok içi)",
  "aday 1040 (kayıt): blokta sûre sınırı yok; vaka yok",
  "aday 1041 (kayıt): blokta vaka yok",
  "karşıt çift (aday 1039, okuma): 69:19 / 69:25 sağ / sol; 69:20 / 69:26 hesabına kavuşacağını bilen / hesabını bilmemeyi dileyen; öbür sekiz ayette yok",
  "tetik: ön kuru koşu 1 uyuşmaz (69:24 ◈K يوم — satır dolduruldu); kayıtta 0; [x/y] 0 (33 sayım)",
 ], (31, 41): [
  "esmâ: e_oto 1 token (69:40 'kerîm' — 'rasûlin kerîm'); DEĞİL; KARAR 653 → 654; esma_kayit mühür EVET, karar sonrası geçersiz (1022); blokta geçerli mühür yok",
  "esmâ (924): 69:33 'el-azîm' (lafzın sıfatı) esma_kayit token vermedi (e_oto 0); 42:4 'el-aliyyu'l-azîm'de vermişti — araç alanı, inceleme yapılmadı",
  "kök tablosu: blokta eksik kök yok; 1447 değişmedi; retroaktif yama 0, genel geçiş 0",
  "lafız: 69:33 sûrenin ilk ve tek lafız tokeni (أله [1/1]); ★★ allah z=2,80 — içerik iddiası değil; öbür on ayet yıldızsız",
  "sayı işareti: 69:32 'seb'ûn' — gerçek sayı (yetmiş arşın); 69:41 'qalîl' — sayı değil ('ne az')",
  "gloss / lemma (1021 ailesi): حمم 69:35 'hamîm' (candan yakın) — gloss 'kaynar su'; lemma 'hamîm' listesi iki anlamı birleştiriyor, sayı verilmedi; ذرع 'zer'' okunmuş iki ayette 'dâqa bihim zer'an' (göğüs darlığı), burada arşın",
  "esit2 / xref: 69:34 ↔ 107:3 TAM (ölçüm iki kez yazıyor), 89:18 BENZER; 69:40 ↔ 81:19 TAM — hepsi henüz okunmadı",
  "ölçüm iltifât: 69:38 (3MS sahne → 1S / 2MP yemin), 69:40 (2MP → 3MS); 69:31 / 69:33 emir-alıntı → anlatı geçişi ölçümde iltifât değil",
  "biçim / kip (517 ailesi): 69:35 biçim DIKKAT dayanaksız görünüyor; 69:33 tekit 'inne' ve 69:35 'leyse' kip alanında yok",
  "adsız (aday 1017): emreden ve 2MP muhataplar (69:30-32), kitabı solundan verilen (3MS), yoksul, 'el-hâti'ûn', 1S yemin eden, 'rasûl kerîm', 69:40-41 'huve' göndergesi — ad verilmedi",
  "çıpa: blokta doğal olgu yok (69:32 zincir, insan yapımı, âhiret); tarayıcı adayı yok",
  "fâsıla: blok içi ه (69:31-32), م (69:33, 35, 40) ve ن (69:34, 36-39, 41); H → N sınıf geçişi 69:32 / 69:33 — kafiye kırığı işaretlenmedi (924)",
  "aday 1040 (kayıt): blokta sûre sınırı yok; ardışık sûre okuma bağı 68:24 / 69:34 'miskîn' (1040 değil)",
  "aday 1041 (kayıt): 'kerîm' 69:40 elçinin sıfatı — esmâ listesi lemması, Allah için kullanımı bu blokta yok; vaka yok",
  "karşıt çift (aday 1039, okuma): 69:24 / 69:37 ikram yemeği / yalnız hata işleyenlerin yediği; 69:38 / 69:39 görülen / görülmeyen; 69:40 / 69:41 elçi sözü / şair sözü; öbür sekiz ayette yok",
  "tetik: ön kuru koşu 3 uyuşmaz (69:35 ◈K يوم, 69:38 ve 69:39 ◈B بصر — satırlar dolduruldu); kayıtta 0; [x/y] 0 (40 sayım)",
 ], (42, 52): [
  "esmâ: e_oto 1 token (69:47 'ehad' — 'min ehadin', hiç kimse); DEĞİL; KARAR 654 → 655; esma_kayit mühür EVET, karar sonrası geçersiz (1022); blokta geçerli mühür yok",
  "esmâ (924): 69:52 'el-azîm' (Rabbin sıfatı) esma_kayit token vermedi — 69:33 ile aynı; araç alanı, inceleme yapılmadı",
  "kök tablosu: kok_ekle_69 1 kök (وتن 69:46, gloss korpus 1 ayet; blok_dikey 'KARŞILIK YOK'); 1447 → 1448; retroaktif yama 0, genel geçiş 0",
  "hapaks (49:11 dersi): 69:46 ★★★ hapaks z=3,28 — yeni kökün tek tokeni; içerik iddiası değil",
  "yıldız (924): 69:43, 69:52 ★★★ rab z=5,01 (4 kelimede 1 Rab) — içerik iddiası değil",
  "kafiye (aday 1001 ailesi): 69:44 fâsıla ل — ölçüm KAFİYE KIRILMASI (sûrede tek ل); ★ kafiye kırığından, bilanço kaynak etiketi 'n' (z=-0,79) yanlış",
  "sayı işareti: 69:42 'qalîl', 69:47 'ehad' — ikisi de sayı değil (nefy / 'ne az')",
  "ölçüm iltifât: 69:44, 69:49, 69:50, 69:52 — şahıssız / 1P / 3MS / 2MS geçişleri iltifât sayılıyor",
  "esit2 / xref: 69:43 ↔ 56:80 TAM, 69:52 ↔ 56:74, 56:96 TAM (okundu); xref 26:192 (okundu), 87:1 (henüz okunmadı)",
  "adsız (aday 1017): 69:44 'teqavvele' faili (3MS), 1P konuşan (69:44-47, 49), 2MP muhatap, muttakîler, yalanlayanlar, kâfirler, 2MS muhatap (69:52), 'innehû' göndergesi — ad verilmedi",
  "çıpa: blokta doğal olgu yok (69:46 'vetîn' organ, varsayım içinde; olgu tarifi değil); tarayıcı adayı yok",
  "fâsıla: blok içi ن (69:42-43, 45-51), ل (69:44), م (69:52); kafiye kırığı 1 (69:44)",
  "aday 1040 (kayıt): 69:52 → 70:1 yazılmadı (70 henüz okunmadı); ardışık olmayan eşleşme (okuma bağı): 56:80 / 69:43, 56:95-96 / 69:51-52",
  "aday 1041 (kayıt): 'el-azîm' 69:33 lafzın sıfatı / 69:52 Rabbin sıfatı — iki kullanım da ilâhî, vaka yok",
  "karşıt çift (aday 1039, okuma): 69:48 / 69:49 muttakîler / yalanlayanlar; 69:48 / 69:50 öğüt / hasret; öbür dokuz ayette yok",
  "tetik: ön kuru koşu 0 uyuşmaz (blokta tetik yok); kayıtta 0; [x/y] 0 (37 sayım)",
 ],
}

DUZELTME = {
}
