# -*- coding: utf-8 -*-
"""mearic_kayit.py — sûre 70 (Meâric) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 70

CIPA = {
 # blok 1-10
 4: dict(kademe=None, olgu=False, cipa=False, not_="'ta'ruju'l-melâ'iketu ve'r-rûhu ileyhi fî yevmin kâne miqdâruhû hamsîne elfe sene' — melekler ve rûhun yükselişi gaybî (olgu=False); süre sayıyla ölçülüyor ama ölçülen olgu doğal değil; merdiven uygulanmadı; tarayıcı v4 adayı (F_ölçü), çıpa değil; emsal 32:5 eski kaydı 'L4 (ölçü) · olgu EVET' — tutarsızlık bekleyen kararlara (yalnız kayıt)"),
 8: dict(kademe='L1', olgu=True, cipa=False, not_="'yevme tekûnu's-semâ'u ke'l-muhl' — gök + hâl; mekanizma / ölçü yok — L1 (69:16, 55:37 emsali); 'ke'l-muhl' teşbih aracı (olgu=False); tarayıcı vermedi"),
 9: dict(kademe='L1', olgu=True, cipa=False, not_="'ve tekûnu'l-cibâlu ke'l-'ihn' — dağlar + hâl; mekanizma / ölçü yok — L1 (69:14 emsali); 'ke'l-'ihn' teşbih aracı (olgu=False); tarayıcı vermedi"),
 # blok 11-20
 15: dict(kademe=None, olgu=False, cipa=False, not_="'innehâ lazâ' — âhiret ateşi, adlı yer (olgu=False); 70:16-18 nitelikleri de aynı sahne; merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 31-37
 35: dict(kademe=None, olgu=False, cipa=False, not_="'fî cennâtin mukramûn' — âhiret cenneti (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 38-44
 38: dict(kademe=None, olgu=False, cipa=False, not_="'cennete na'îm' — âhiret cenneti (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 40: dict(kademe='L0', olgu=True, cipa=False, not_="'bi-rabbi'l-meşâriqi ve'l-meğârib' — doğular / batılar çoğul, yemin içinde rubûbiyet tamlaması; sayı / ölçü / mekanizma yok — L0 (37:5 emsali; 55:17 ikil L1); tarayıcı vermedi"),
 43: dict(kademe=None, olgu=False, cipa=False, not_="'yahrucûne mine'l-ecdâsi sirâ'an' — âhiret, kabirlerden çıkış (olgu=False); 'ilâ nusubin' teşbih aracı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: e_oto 1 token (70:7 'qarîb' — 've nerâhu qarîbâ'); DEĞİL; KARAR 655 → 656; esma_kayit mühür EVET, karar sonrası geçersiz (1022); blokta geçerli mühür yok",
  "kök tablosu: kok_ekle_70 0 kök (blok_dikey 'karşılık eksiği yok'); 1448 değişmedi; retroaktif yama hedef 0, yama 0, genel geçiş 0",
  "yıldız (924): 70:3 ★★★ allah z=4,47 (4 kelimede 1 lafız) — içerik iddiası değil; öbür dokuz ayet yıldızsız",
  "harf alanı: ayet 1 ölçümünde harf 38 → harf3 16, isaret 0 (ayet 1 ailesi; 69:1 emsali); araç alanı (924); KAPATILAMAZ",
  "gloss (1021 ailesi): حمم 70:10 'hamîm' (yakın dost; 69:35 aynı anlam) — gloss 'kaynar su, hamîm'; lemma 'hamîm' listesi kaynar su anlamıyla birleşik — sayı verilmedi",
  "sayı işareti: 70:4 'hamsîn', 'elf' — gerçek sayı (yıl birimiyle)",
  "ölçüm iltifât: 70:5 (3MS → 2MS), 70:6 (2MS → 3MP) sayılıyor; 70:7 1P girişi iltifât sayılmıyor (araç alanı, 924)",
  "esit2 / xref: blokta esit2 yok; 70:4 xref 32:5 (okundu); 70:9 xref 101:5 (henüz okunmadı); lemma dizisi 'melek + rûh' eşi 97:4 henüz okunmadı",
  "adsız (aday 1017): 70:1 'sâ'il', kâfirler, 2MS muhatap (70:5), 3MP 'innehum', 1P konuşan (70:7), 70:6-7 'hû' göndergesi, 70:10 'hamîm' — ad verilmedi; metnin adladıkları (Allah, melekler, rûh) adıyla anıldı",
  "çıpa: 70:8 L1 (gök), 70:9 L1 (dağlar); teşbih araçları 'ke'l-muhl', 'ke'l-'ihn' olgu=False; 70:4 olgu=False (gaybî yükseliş) — tarayıcı v4 adayı (F_ölçü), çıpa değil; emsal 32:5 eski kaydı 'L4 (ölçü) · olgu EVET' ile tutarsız — bekleyen kararlara (yalnız kayıt); L4 yok",
  "fâsıla: ع (70:1-2), ج (70:3), ة (70:4), ا (70:5-7, 70:10), ل (70:8), ن (70:9); ölçüm kafiye kırığı 0",
  "aday 1040 (kayıt): 69:52 'fe-sebbih bi'smi rabbike'l-azîm' / 70:1 'se'ele sâ'ilun bi-azâbin vâqi'' — sûre sınırı; fâsıla م → ع; test yok",
  "aday 1041 (kayıt): 70:6 'yeravnehû' (3MP) / 70:7 'nerâhu' (1P) — aynı fiil iki öznede; 1P konuşan adsız (1017), vaka sayılmadı",
  "karşıt çift (aday 1039, okuma): 70:6 / 70:7 uzak / yakın; öbür sekiz ayette yok",
  "tetik: ön kuru koşu 3 uyuşmaz (70:4 ◈K يوم سنو; 70:8 ◈K يوم سمو; 70:9 ◈K جبل — satırlar dolduruldu); kayıtta 0; [x/y] 0 (39 sayım)",
 ], (11, 20): [
  "esmâ: blokta e_oto token yok; KARAR 656 değişmedi; geçerli mühür yok",
  "kök tablosu: kok_ekle_70 1 kök (هلع 70:19, gloss korpus 1 ayet; blok_dikey 'KARŞILIK YOK'); 1448 → 1449; retroaktif yama hedef 0, yama 0, genel geçiş 0",
  "hapaks (49:11 dersi): 70:19 ★★★ (pas z=5,38; hapaks z=3,28) — yeni kökün tek tokeni ve tek fiil edilgen; içerik iddiası değil",
  "yıldız (924): 70:11 ★ pas z=1,57 (3 fiilde 1 edilgen) — içerik iddiası değil",
  "fâsıla / kafiye (aday 1001 ailesi): 70:18 ölçüm fâsıla 'ٓ' (medde işareti son harf sayılıyor; metinde ى) — KAFİYE KIRILMASI araç kaynaklı; ★ bu kırıktan, bilanço kaynak etiketi 'n' (z=-1,11) yanlış; KAPATILAMAZ",
  "gloss (1021 ailesi): بني 70:11 'benîh' (oğulları) — gloss 'bina, yapma'; lemma listesi 77 ayet, sayı verilmedi",
  "kök yok: 70:15 'lazâ' — ölçüm 'kökler —'; dikey satır yok; aktör adlı (yer)",
  "ölçüm kip (517 ailesi): 70:11 temenni 'lev', 70:19 tekit 'inne', 70:20 şart 'izâ' kip alanında yok; 70:15 'kellâ' biçim KELLA olarak var",
  "esit2 / xref: blokta esit2 yok; 70:11 xref 5:36 (henüz okunmadı); lemma dizisi eşi 5:17 (henüz okunmadı)",
  "adsız (aday 1017): 70:11 gösteren (edilgen) ve 'mucrim', eş, kardeş, akraba, 70:17 'men', 70:19 yaratan (edilgen) — ad verilmedi; metnin adladığı 'lazâ' adıyla anıldı",
  "çıpa: blokta doğal olgu yok; 70:15 'lazâ' âhiret (olgu=False); tarayıcı adayı yok; L4 yok",
  "fâsıla: ه (70:11-14), ى (70:15-18; 70:18 ölçümde ٓ), ا (70:19-20); gerçek kafiye kırığı yok (okuma)",
  "aday 1040 (kayıt): blokta sûre sınırı yok; vaka yok",
  "aday 1041 (kayıt): blokta vaka yok",
  "karşıt çift (aday 1039, okuma): on ayette yok",
  "tetik: ön kuru koşu 4 uyuşmaz (70:11 ◈K يوم ◈B بصر; 70:14 ◈K أرض; 70:19 ◈B أنس خلق — satırlar dolduruldu); kayıtta 0; [x/y] 0 (28 sayım)",
 ], (21, 30): [
  "esmâ: blokta e_oto token yok (Rab 2 token sınıf R); KARAR 656 değişmedi; geçerli mühür yok",
  "kök tablosu: kok_ekle_70 0 kök (blok_dikey 'karşılık eksiği yok'); 1449 değişmedi; retroaktif yama hedef 0, yama 0, genel geçiş 0",
  "yıldız (924): 70:27 ★★★ rab z=3,23 (6 kelimede 1 Rab), 70:28 ★★★ rab z=3,94 (5 kelimede 1 Rab) — içerik iddiası değil; öbür sekiz ayet yıldızsız",
  "sayı işareti: 70:30 'zevc' — sayı değil (eş)",
  "ölçüm kip (517 ailesi): 70:21 şart 'izâ', 70:28 tekit 'inne' kip alanında yok; 70:22, 70:30 istisna biçim ISTISNA olarak var",
  "esit2 / xref: 70:29 ↔ 23:5 TAM, 70:30 ↔ 23:6 TAM (okundu); 70:30 xref 33:50 (okundu); nakarat3 70:23 sûre içi eşi 70:34 (henüz okunmadı); lemma dizisi eşi 6:17 (henüz okunmadı)",
  "adsız (aday 1017): namaz kılanlar ve sıfat dizisinin özneleri, isteyen, yoksun, 'mâ meleket eymânuhum' — ad verilmedi",
  "çıpa: blokta doğal olgu yok; tarayıcı adayı yok; L4 yok",
  "fâsıla: ا (70:21), ن (70:22-23, 26-30), م (70:24-25); ölçüm kafiye kırığı 0",
  "aday 1040 (kayıt): blokta sûre sınırı yok; ardışık olmayan eşleşme (okuma bağı): 23:5-6 / 70:29-30 aynı sıra TAM; 51:19 / 70:24-25 tek ayet → iki ayet",
  "aday 1041 (kayıt): blokta vaka yok",
  "karşıt çift (aday 1039, okuma): 70:20 / 70:21 şer / hayır, cezû' / menû'; öbür dokuz ayette yok",
  "tetik: ön kuru koşu 2 uyuşmaz (70:26 ◈K يوم; 70:30 ◈B زوج — satırlar dolduruldu); kayıtta 0; [x/y] 0 (36 sayım)",
 ], (31, 37): [
  "esmâ: blokta e_oto token yok; KARAR 656 değişmedi; geçerli mühür yok",
  "kök tablosu: kok_ekle_70 1 kök (عزو 70:37, gloss korpus 1 ayet; blok_dikey 'KARŞILIK YOK'); 1449 → 1450; retroaktif yama hedef 0, yama 0, genel geçiş 0",
  "hapaks (49:11 dersi): 70:37 ★★★ hapaks z=3,28 — yeni kökün tek tokeni; içerik iddiası değil",
  "blok sınırı: sûrenin kalan 14 ayeti 70:31-37 ve 70:38-44 olarak iki yedili bloğa bölündü",
  "ölçüm iltifât: 70:36 'qibeleke' (2MS) girişi iltifât sayılmıyor (3MP → 2MS; araç alanı, 924)",
  "esit2 / xref: 70:31 ↔ 23:7 TAM, 70:32 ↔ 23:8 TAM, 70:34 ↔ 23:9 YAKIN 0,9565 (okundu); nakarat3 70:34 ↔ 70:23 sûre içi GEÇER",
  "adsız (aday 1017): sınırı aşanlar, sıfat dizisinin özneleri, inkâr edenler, 2MS muhatap (70:36) — ad verilmedi",
  "çıpa: blokta doğal olgu yok; 70:35 cennet (olgu=False); tarayıcı adayı yok; L4 yok",
  "fâsıla: blok içi yedi ayet ن (N sınıfı); kafiye kırığı 0",
  "aday 1040 (kayıt): blokta sûre sınırı yok; ardışık olmayan eşleşme (okuma bağı): 23:5-9 / 70:29-34 — beş ayet aynı sırayla (dördü TAM, biri YAKIN), araya 70:33 giriyor; 23:10 / 70:35 'ulâ'ike' kapanışı",
  "aday 1041 (kayıt): blokta vaka yok",
  "karşıt çift (aday 1039, okuma): 70:31 / 70:35 'ulâ'ike humu'l-'âdûn' / 'ulâ'ike fî cennâtin mukramûn'; 70:37 sağ / sol; öbür dört ayette yok",
  "tetik: ön kuru koşu 0 uyuşmaz (blokta tetik yok); kayıtta 0; [x/y] 0 (23 sayım)",
 ], (38, 44): [
  "esmâ: blokta e_oto token yok (Rab 1 token sınıf R); KARAR 656 değişmedi; geçerli mühür yok",
  "kök tablosu: kok_ekle_70 1 kök (وفض 70:43, gloss korpus 1 ayet; blok_dikey 'KARŞILIK YOK'); 1450 → 1451; retroaktif yama hedef 0, yama 0, genel geçiş 0",
  "hapaks (49:11 dersi): 70:43 ★★★ hapaks z=3,28 — yeni kökün tek tokeni; içerik iddiası değil",
  "yıldız (924): 70:38 ★★ pas z=2,52, 70:40 ★★ rab z=2,72, 70:44 ★ pas z=1,57 — içerik iddiası değil",
  "ölçüm iltifât: 70:40 1S 'uqsimu' / 1P 'innâ' aynı ayette, 70:42 2MS 'fe-zerhum' girişi — iltifât sayılmıyor (araç alanı, 924)",
  "esit2 / xref: 70:42 ↔ 43:83 TAM (okundu); 70:44 xref 68:43, 21:103 (okundu); 70:40 xref 26:28 (okundu), 73:9 (henüz okunmadı); 70:38 xref 5:65 (henüz okunmadı)",
  "adsız (aday 1017): 70:38 sokan (edilgen), 1S / 1P konuşan (70:39-41), 2MS muhatap (70:42), vaat eden (edilgen 70:42, 70:44), 3MP inkâr edenler — ad verilmedi",
  "çıpa: 70:40 L0 (doğular / batılar çoğul, rubûbiyet tamlaması; 37:5 emsali); 70:38 cennet, 70:43 kabirlerden çıkış ve 'nusub' teşbihi olgu=False; tarayıcı adayı yok; L4 yok",
  "fâsıla: م (70:38), ن (70:39-44); ölçüm kafiye kırığı 0",
  "aday 1040 (kayıt): 70:44 → 71:1 yazılmadı (71 henüz okunmadı); ardışık olmayan eşleşme (okuma bağı): 43:83 / 70:42 TAM; 56:60-61 / 70:41 ters sıra; 54:7 / 70:43-44 ters sıra iki ayete; 68:43 / 70:44 ilk yarı",
  "aday 1041 (kayıt): 70:19 'hulika' (edilgen) / 70:39 'halaqnâhum' (1P) — fail adsız (1017), vaka sayılmadı",
  "karşıt çift (aday 1039, okuma): 70:40 ayet içi doğular / batılar; öbür altı ayette yok",
  "tetik: ön kuru koşu 5 uyuşmaz (70:39 ◈B خلق; 70:42, 70:43, 70:44 ◈K يوم; 70:44 ◈B بصر — satırlar dolduruldu); kayıtta 0; [x/y] 0 (42 sayım)",
 ],
}

DUZELTME = {
 20: dict(alan='mercek', eski="karşılık 've'ûs', 'ye'ûs qanût'",
          dogru="17:83'ün karşılığı 'kâne ye'ûsâ' — 've'ûs' yazım hatası, doğrusu 'ye'ûs'. Dört karşılık: 'ye'ûs' (17:83), 'ye'ûs qanût' (41:49), 'zû du'â'' (41:51), 'cezû'' (70:20). Özgün alan korunur.",
          aday=1003, blok='11-20'),
}
