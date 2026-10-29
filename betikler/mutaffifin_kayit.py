# -*- coding: utf-8 -*-
"""mutaffifin_kayit.py — sûre 83 ('Mutaffifîn) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 83

CIPA = {
 # blok 1-10
 1: dict(kademe=None, olgu=False, cipa=False, not_="'veylun li'l-mutaffifîn' — insan davranışı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'ellezîne izâ iktâlû …' — insan davranışı, ölçme (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'ve izâ kâlûhum ev vezenûhum yuxsirûn' — insan davranışı, ölçme / tartma (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'e-lâ yezunnu ulâ'ike ennehum meb'ûthûn' — âhiret, soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'li-yevmin 'azîm' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'yevme yeqûmu'n-nâsu li-rabbi'l-'âlemîn' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'kellâ inne kitâbe'l-fuccâri le-fî siccîn' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ edrâke mâ siccîn' — soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 9: dict(kademe=None, olgu=False, cipa=False, not_="'kitâbun merqûm' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'veylun yevme'izin li'l-mukezzibîn' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 11-20
 11: dict(kademe=None, olgu=False, cipa=False, not_="'ellezîne yukezzibûne bi-yevmi'd-dîn' — âhiret, tarif (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 12: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ yukezzibu bihî illâ kullu mu'tedin esîm' — yargı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'izâ tutlâ 'aleyhi âyâtunâ qâle esâtîru'l-evvelîn' — söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe=None, olgu=False, cipa=False, not_="'kellâ bel râne 'alâ qulûbihim …' — kalp organ adı, manevi bağlam (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="'kellâ innehum 'an rabbihim yevme'izin le-mahcûbûn' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 16: dict(kademe=None, olgu=False, cipa=False, not_="'thumme innehum le-sâlu'l-cahîm' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 17: dict(kademe=None, olgu=False, cipa=False, not_="'thumme yuqâlu hâze'llezî kuntum bihî tukezzibûn' — âhiret, söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 18: dict(kademe=None, olgu=False, cipa=False, not_="'kellâ inne kitâbe'l-ebrâri le-fî 'illiyyîn' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 19: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ edrâke mâ 'illiyyûn' — soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 20: dict(kademe=None, olgu=False, cipa=False, not_="'kitâbun merqûm' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 21-28
 21: dict(kademe=None, olgu=False, cipa=False, not_="'yeşheduhu'l-muqarrabûn' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 22: dict(kademe=None, olgu=False, cipa=False, not_="'inne'l-ebrâra le-fî na'îm' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 23: dict(kademe=None, olgu=False, cipa=False, not_="''ale'l-erâ'iki yenzurûn' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 24: dict(kademe=None, olgu=False, cipa=False, not_="'ta'rifu fî vucûhihim nadrate'n-na'îm' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 25: dict(kademe=None, olgu=False, cipa=False, not_="'yusqavne min rahîqin maxtûm' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 26: dict(kademe=None, olgu=False, cipa=False, not_="'xitâmuhû misk …' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 27: dict(kademe=None, olgu=False, cipa=False, not_="'ve mizâcuhû min tesnîm' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 28: dict(kademe=None, olgu=False, cipa=False, not_="''aynen yeşrabu bihe'l-muqarrabûn' — âhiret, pınar (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 29-36
 29: dict(kademe=None, olgu=False, cipa=False, not_="'inne'llezîne ecramû … yadhakûn' — insan davranışı, dünya (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 30: dict(kademe=None, olgu=False, cipa=False, not_="'ve izâ merrû bihim yeteğâmezûn' — insan davranışı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 31: dict(kademe=None, olgu=False, cipa=False, not_="'ve izâ'nqalebû ilâ ehlihimu'nqalebû fekihîn' — insan davranışı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 32: dict(kademe=None, olgu=False, cipa=False, not_="'ve izâ ra'evhum qâlû …' — söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 33: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ ursilû 'aleyhim hâfizîn' — insan davranışı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 34: dict(kademe=None, olgu=False, cipa=False, not_="'fe'l-yevme'llezîne âmenû … yadhakûn' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 35: dict(kademe=None, olgu=False, cipa=False, not_="''ale'l-erâ'iki yenzurûn' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 36: dict(kademe=None, olgu=False, cipa=False, not_="'hel thuvvibe'l-kuffâru …' — âhiret, soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: e_oto 0 token; KARAR değişmedi (699); 83:6 sûrenin ilk Rab'ı ('li-rabbi'l-'âlemîn'), lafız yok",
  "kök tablosu: kok_ekle_83 1 kök (طفف 83:1; korpusta tek ayet); 1505 → 1506; retroaktif yama hedefli 0, genel 0 (ikinci koşu da 0)",
  "harf alanı: ayet 1 ölçümünde harf 31 → harf3 11, isaret 0 (ayet 1 ailesi; besmele); araç alanı (924)",
  "yıldız: ★★★ 2 — 83:1 hapaks (yeni kök), 83:6 rab z=3,94 (lafızsız kısa ayette Rab) — formül davranışı, içerik iddiası değil",
  "biçim / kip (924): 83:2-3 'izâ' şart yapısı kip alanında yok; 83:7 KELLA + EMPH, 83:4 INTG + NEG doğru",
  "nakarat3: 83:7 'kellâ inne kitâb' ve 83:8 've mâ edrâke mâ' süzgeç GEÇMEZ (3 kelime / 2 ayet); eşleri henüz okunmadı",
  "esit2: 83:10 → 77:15, 19, 24, 28, 34, 37, 40, 45, 47, 49 (TAM, sûre 77 nakaratı — 77:15 basıldı, kalanı sayı olarak); 83:9 → 83:20 (TAM, henüz okunmadı)",
  "okuma ikiliği: 83:9 'kitâbun merqûm' — 'siccîn'in açıklaması / 83:7 'kitâb'ın nitelemesi KAPATILAMAZ",
  "gloss (1021): kök سجن 'hapis, zindan' — 'siccîn' adına metnin vermediği anlam taşıyor",
  "adsız gönderge (1017): 83:1-3 eksik ölçenler ve karşı taraf; 83:8 muhatap 2MS; konuşan adsız",
  "fâsıla: 83:1-4 ن, 83:5 م, 83:6-8 ن, 83:9 م, 83:10 ن — ölçüm hepsi N sınıfı",
  "aday 1040 (kayıt): 82:19 / 83:1 sûre sınırı — 'li' + lafız ile kapanış / 'veyl' + 'li' + ortaç ile açılış; fâsıla ه → ن; ardışık sûrede iskelet: 82:14 / 83:7 'inne' + 'el-fuccâr' + 'le-fî' + nekre (cehennem / siccîn)",
  "aday 1040 ailesi (okuma): 82:17 / 83:8 've mâ edrâke mâ' + âhiret adı",
  "bağ: kalıp / lemma eşleri okumayla (12:63, 17:35, 26:181, 26:182, 55:9, 56:47, 78:38, 40:51, 40:66, 81:29, 38:28, 80:42, 69:3, 77:14, 77:15, 52:11); 83:18, 83:19, 83:20 henüz okunmadı — bağ yazılmadı",
  "◈K / ◈B: ◈K dolu 83:5, 6, 10 يوم; ◈B dolu 83:2, 6 أنس; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 25 sayım 0 uyuşmaz",
  "süreç: sûre 83 dosyaları infitar_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_83.py, oturum dışı)",
 ],
 (11, 20): [
  "esmâ: e_oto 2 token (83:13 'evvel' — 'el-evvelîn', öncekiler; 83:18 'berr' — 'el-ebrâr') — ikisi de DEĞİL; KARAR 699 → 701; mühür iddiası bilançodan (1022); Rab 83:15 (sûre bütünü Rab 2: 83:6, 15)",
  "kök tablosu: kok_ekle_83 1 kök (رين 83:14; korpusta tek ayet); 1506 → 1507; retroaktif yama hedefli 0, GENEL GEÇİŞ 5 — gloss_gecis harekesiz iskelet ↔ kök çakışması: 28:81, 29:38, 39:72, 40:76, 43:56 ölçüm satırında fâsıla kelimesinin ('…rîn' ile biten çoğul ortaç) iskelet parçası kök sanıldı ve 'râne' glossu yapıştı; yama_rin_83.py ile açıklama notuna çevrildi (sûre 59 Hâmân yamasının eşi, 924); araç değişmedi; yama ikinci koşu 0, retroaktif ikinci koşu 0",
  "alıntı (1017): 83:13 'qâle' işaretli söz, 83:17 'yuqâlu' işaretli söz — meal tek tırnaklı; ikisi de ayet içinde kapanıyor (sonraki ayet 'kellâ' ile anlatıcı sesi); 83:17'de söyleyen adsız",
  "yıldız: ★★★ 2 (83:14 hapaks — yeni kök; 83:15 rab z=3,23); ★★ 83:13 pas z=2,52; ★ 83:17 pas z=1,57 — formül davranışı",
  "nakarat3: 83:7 / 83:18 'kellâ inne kitâb' ve 83:8 / 83:19 've mâ edrâke mâ' — süzgeç GEÇMEZ (3 kelime); 83:9 / 83:20 esit2 TAM — 83:7-9 / 83:18-20 üç ayetlik dizi aynı sırayla (okuma)",
  "okuma ikiliği: 83:20 'kitâbun merqûm' — ''illiyyûn'un açıklaması / 83:18 'kitâb'ın nitelemesi KAPATILAMAZ (83:9 ile aynı)",
  "◈B: 83:14 قلب tetikliyor — kalp organ adı ama işlev mecaz ('üstünü kaplama'), satır dolu, not düşüldü (67:4 türü)",
  "fâsıla: 83:11 ن, 83:12 م, 83:13-15 ن, 83:16 م, 83:17-19 ن, 83:20 م — ölçüm hepsi N",
  "aday 1040 (kayıt): 82:13-14 / 83:7, 18 iyiler / günahkârlar ikilisi 'inne' + 'le-fî' iskeletiyle (ardışık sûrede sıra ters)",
  "aday 1040 ailesi (okuma): 82:9 / 83:11 'kezzebe bi'd-dîn'; 82:14-15 / 83:16 cahîm + kök صلي",
  "bağ: kalıp / lemma eşleri okumayla (74:46, 68:12, 68:15, 31:7, 74:53, 82:9, 38:59, 37:21, 77:29, 83:7, 83:8, 83:9, 82:13); 89:17 henüz okunmadı",
  "◈K / ◈B: ◈K dolu 83:11, 15 يوم; ◈B dolu 83:14 قلب; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 31 sayım 0 uyuşmaz",
  "süreç: kayıttan önce düzelttiğim — 83:14 ◇'de çakışma yamasının hedef ayet numaraları (okunmuş, basılmamış) adla yazılmıştı; 'okunmuş 5 ayet' diye sayıya çevrildi (ARIZA'da kayıt numaraları korunuyor — yama hedefi)",
 ],
 (21, 28): [
  "esmâ: e_oto 1 token (83:22 'berr' — 'el-ebrâr') — DEĞİL; KARAR 701 → 702; mühür iddiası bilançodan (1022)",
  "kök tablosu: kok_ekle_83 2 kök (رحق 83:25; سنم 83:27; ikisi de korpusta tek ayet); 1507 → 1509; retroaktif yama hedefli 0, genel 0 (ikinci koşu da 0)",
  "yıldız: ★★★ 2 — 83:25 pas z=5,38 + hapaks; 83:27 hapaks (yeni kök) — formül davranışı",
  "gloss (1021): kök نفس 'nefis, can' 83:26 'yetenâfes / mutenâfisûn'da (yarışma) uymuyor; kök مسك 'tutma' 'misk'te uymuyor; kök برر eşsesli lemma (sayı verilmedi)",
  "esit2: 83:22 → 82:13 TAM (ardışık sûrede bir ayetin TAM tekrarı); 83:23 → 83:35 TAM (henüz okunmadı)",
  "adsız gönderge (1017): 83:21 'el-muqarrabûn' kime yakın kılındıkları adlanmıyor — meal parantezi kayıttan önce çıkarıldı; 83:24 muhatap 2MS; 83:25 içiren adsız (edilgen); 83:26 yarışanlar",
  "fâsıla: 83:21 ن, 83:22 م, 83:23 ن, 83:24-25 م, 83:26 ن, 83:27 م, 83:28 ن — ölçüm hepsi N",
  "aday 1040 (kayıt): 82:13 / 83:22 'inne'l-ebrâra le-fî na'îm' ardışık sûrede TAM (esit2)",
  "bağ: kalıp / lemma eşleri okumayla (56:11, 76:13, 75:22, 76:11, 76:17, 76:5, 76:6); 76:5-6 / 83:27-28 'mizâc' + ''aynen yeşrabu bihâ' sırası (ardışık olmayan sûre); 83:35 henüz okunmadı",
  "◈K / ◈B: ◈K tetik yok; ◈B dolu 83:28 عين (pınar, organ anlamı değil — not düşüldü); 83:24 'vech' (yüz) tetik listesinde değil — '—'; 83:22, 24 نعم 'na'îm' S1 izinli lemma değil",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 21 sayım 0 uyuşmaz; kayıttan önce düzelttiğim — 83:21 meal parantezi '(Allah'a)' metinde olmayan göndergeyi adlıyordu, çıkarıldı (1017)",
 ],
 (29, 36): [
  "esmâ: e_oto 0 token; KARAR değişmedi (702); lafız ve Rab yok — sûre bütünü lafız 0, Rab 2 (83:6, 15)",
  "kök tablosu: kok_ekle_83 1 kök (غمز 83:30; korpusta tek ayet); 1509 → 1510; retroaktif yama hedefli 0, genel 0 (ikinci koşu da 0)",
  "yıldız: ★★★ 2 — 83:30 hapaks (yeni kök), 83:33 pas z=5,38; ★ 83:36 pas z=1,57 — formül davranışı",
  "biçim (924): 83:29 'inne' tekidi kip alanında yok; 83:30-32 'izâ' şart yapısı kip alanında yok",
  "alıntı (1017): 83:32 'qâlû' işaretli söz — meal tek tırnaklı, ayet içinde kapanıyor (83:33 anlatıcı sesi)",
  "okuma ikiliği: 83:33 zamir dağılımı (gönderilmeyenler suçlular / 'aleyhim' müminler) okumayla — metin zamirle bırakıyor, KAPATILAMAZ; 83:34 'el-yevm' âhiret 'bugün'ü (okuma)",
  "gloss (1021): kök قلب 83:14 'qulûb' (kalpler) / 83:31 'inqalebû' (dönme); kök ثوب 'elbise; karşılık' — burada karşılık",
  "◈B: 83:31 قلب tetikliyor — dönme anlamı, organ değil; satır dolu, not düşüldü (67:4 türü)",
  "fâsıla: 83:29-36 hepsi ن — ölçüm N",
  "aday 1040 ailesi (okuma): 82:10 / 83:33 'alâ' + zamir + 'hâfizîn' — üzerinizde gözetleyiciler var / gözetleyici olarak gönderilmediler; 83:36 → 84:1 sınırı 84:1 okunurken",
  "bağ: kalıp / lemma eşleri okumayla (23:110, 44:27, 52:18, 36:55, 68:26, 82:10, 83:23); 84:9 henüz okunmadı — bağ yazılmadı",
  "◈K / ◈B: ◈K dolu 83:34 يوم; ◈B dolu 83:31 قلب; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, sûre geneli 36 / 0; oturum_xy 24 sayım 0 (sûre geneli 101 / 0)",
 ],
}

DUZELTME = {
}
