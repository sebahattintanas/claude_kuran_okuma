# -*- coding: utf-8 -*-
"""kalem_kayit.py — sûre 68 (Kalem) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 68

CIPA = {
 # blok 1-10: doğal olgu yok, merdiven uygulanmadı (kalem ve yazı insan yapımı; 68:5 görme işlevi olgu tarifi değil)
 # blok 11-20
 17: dict(kademe=None, olgu=False, cipa=False, not_="'le-yasrimunnehâ musbihîn' — bahçenin devşirilmesi insan eylemi (tarım), yemin anlatısı; doğal olgu değil, merdiven uygulanmadı; tarayıcı vermedi"),
 19: dict(kademe=None, olgu=False, cipa=False, not_="'tâfe aleyhâ tâ'ifun min rabbike' — 'tâ'if' ne olduğu adlanmıyor, olgu tarifi yok; merdiven uygulanmadı; tarayıcı vermedi"),
 20: dict(kademe=None, olgu=False, cipa=False, not_="'fe-asbahat ke's-sarîm' — bahçenin hâli teşbihle (teşbih aracı olgu=False); tarayıcı vermedi"),
 # blok 21-30
 22: dict(kademe=None, olgu=False, cipa=False, not_="'eni'ğdû alâ harsikum in kuntum sârimîn' — ekinin devşirilmesi insan eylemi (tarım), alıntı içi emir; doğal olgu değil, merdiven uygulanmadı; tarayıcı v4 adayı, çıpa değil"),
 # blok 31-41
 34: dict(kademe=None, olgu=False, cipa=False, not_="'cennâti'n-na'îm' — âhiret cenneti (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 39: dict(kademe=None, olgu=False, cipa=False, not_="'ilâ yevmi'l-qiyâme' — âhiret zamanı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 42-52
 42: dict(kademe=None, olgu=False, cipa=False, not_="'yevme yukşefu an sâq' — adı verilmeyen gün, âhiret sahnesi (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 49: dict(kademe=None, olgu=False, cipa=False, not_="'le-nubize bi'l-arâ'' — anlatı içi gerçekleşmeyen olay, olgu tarifi değil; merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: blokta e_oto token yok; KARAR 650 değişmedi; 'a'lem' (68:7 ×2) esmâ listesinde değil; geçerli mühür yok",
  "harf alanı: ayet 1 ölçümünde harf 36 → harf3 16, isaret 0 (ayet 1 ailesi; hurûf-ı mukattaa 'Nûn'); araç alanı (aday 924); KAPATILAMAZ",
  "biçim (517 ailesi): 68:10 'NEHY + QASEM' — QASEM 'hallâf' (حلف, yemin eden) kökünden yanlış alarm, ayette yemin yok (924)",
  "ölçüm iltifât: 68:2 iltifât 1 (68:1 3MP → 68:2 2MS) — bilanço iltifat_ayet [2]; 68:5 2MS / 3MP → 68:6 2MP ölçümde iltifât değil",
  "ölçüm kip (517 ailesi): 68:6 'eyyikum' INTG — dolaylı soru, 68:5'in nesnesi; 68:9 'lev' istek kip alanında yok; 68:7 tekit 'inne' kip alanında yok",
  "gloss (1021 ailesi): أيي 68:6 'eyyikum' (hangisi); خلق 68:4 'huluq' (ahlâk) — gloss 'yaratma', ◈B tetiği kök düzeyinde; جنن 68:2 'mecnûn' (deli)",
  "yıldız (924): 68:2 ★★★ rab z=3,94 (5 kelimede 1 Rab), 68:7 ★ rab z=1,62 — içerik iddiası değil",
  "esit2 / xref: 68:7 ↔ 6:117 YAKIN (henüz okunmadı), xref 16:125 (okundu)",
  "adsız (aday 1017): 68:1 'yesturûn' 3MP, 2MS muhatap (68:2-10), 68:5 3MP, yalanlayanlar, 'hallâf' — ad verilmedi",
  "çıpa: blokta doğal olgu yok; tarayıcı adayı yok",
  "fâsıla: blok içi ن (68:4 م), on ayet N sınıfı; kafiye kırığı 0 (blok içi)",
  "aday 1040 (kayıt): 67:30 → 68:1 sûre sınırı — cevapsız soruyla kapanış / harf ve yeminle açılış; 67:30 fâsılası ن, 68:1 'Nûn' harfiyle açılıyor; test yok",
  "aday 1041 (kayıt): blokta vaka yok ('huluq' 26:137 öncekilerin âdeti / 68:4 2MS'nin ahlâkı — ikisi de Allah için değil)",
  "karşıt çift (aday 1039, okuma): 68:7 yolundan sapan / doğru yolu bulanlar; öbür dokuz ayette yok",
  "tetik: ön kuru koşu 0 uyuşmaz; kayıtta 0; [x/y] ilk koşuda 1 uyuşmaz (68:10 başka geçişin sayısı [x/y] biçiminde) — kayıttan önce düzeltildi, son koşu 0 (31 sayım)",
 ],
 (11, 20): [
  "esmâ: e_oto 1 token (68:15 'evvel' — 'esâtîru'l-evvelîn'); DEĞİL; KARAR 650 → 651; esma_kayit mühür EVET, karar sonrası geçersiz (1022); blokta geçerli mühür yok",
  "kök tablosu: kok_ekle_68 4 kök (نمم 68:11, زنم 68:13, خرطم 68:16, صرم 68:17, 20; gloss korpus ayet sayısıyla); 1435 → 1439; retroaktif yama hedef 0, yama 0, genel geçiş 0",
  "hapaks (49:11 dersi): 68:11, 68:13, 68:16 ★★★ hapaks z=3,28 — üçü de yeni eklenen kökün korpustaki tek tokeni; içerik iddiası değil",
  "yıldız (924): 68:15 ★★ pas z=2,52, 68:19 ★★ rab z=2,72 — içerik iddiası değil",
  "sayı işareti (924; sûre 58 dersi): 68:18 'yestesnûn' — kök ثني (iki) kaynaklı yanlış alarm",
  "ölçüm iltifât: 68:14 iltifât 1 (68:11-13 şahıssız sıfat dizisi → 68:14 3MS) — bilanço iltifat_ayet [14]; 68:19 kıssa içinde 2MS 'rabbike' ölçümde iltifât değil",
  "biçim (517 ailesi): 68:17 QASEM gerçek yemin fiili ('aqsamû'), 68:10'daki yanlış QASEM'den ayrı; 68:20 teşbih 'ke-' biçim alanında yok",
  "gloss (1021 ailesi): بني 68:14 'benîn' (oğullar) — gloss 'bina, yapma'; جنن 68:17 'el-cenne' (dünya bahçesi) / 68:2 'mecnûn'",
  "esit2 / xref: 68:15 ↔ 83:13 TAM (henüz okunmadı); 68:12 xref 50:25 (okundu)",
  "adsız (aday 1017): 68:10-16 nitelenen (3MS), 1P konuşan (68:15-17), bahçe sahipleri, 'tâ'if' — ad verilmedi; 68:14 'en' gerekçesinin bağlandığı fiil KAPATILAMAZ",
  "organ: 68:16 'hurtûm' ◈B organ listesinde değil — satır '—', gözlem ◇'de (ön-kayıt §4; yeni tetik sınıfı ayrı karar ister)",
  "çıpa: blokta doğal olgu yok (68:17 tarım insan eylemi, 68:19 'tâ'if' adsız, 68:20 teşbih); tarayıcı adayı yok",
  "fâsıla: blok içi م (68:11-13, 16, 20) ve ن (68:14, 15, 17-19), hepsi N sınıfı; kafiye kırığı 0 (blok içi)",
  "aday 1040 (kayıt): 67:2 'li-yebluvekum' / 68:17 'belevnâhum' — ardışık sûrede 'belâ'; test yok",
  "aday 1041 (kayıt): blokta vaka yok",
  "karşıt çift (aday 1039, okuma): on ayette yok",
  "tetik: ön kuru koşu 0 uyuşmaz (blokta tetik yok); kayıtta 0; [x/y] 0 (40 sayım)",
 ],
 (21, 30): [
  "esmâ: blokta e_oto token yok; KARAR 651 değişmedi; geçerli mühür yok",
  "kök tablosu: kok_ekle_68 2 kök (حرد 68:25, gloss korpus 1 ayet; وسط 68:28, gloss korpus 5 ayet); 1439 → 1441; retroaktif yama hedef 3 (2:143, 2:238, 5:89 — okunmamış, kaydı yok), yama 0, genel geçiş 0",
  "hapaks (49:11 dersi): 68:25 ★★★ hapaks z=3,28 — yeni kök حرد'ın tek tokeni; içerik iddiası değil",
  "yıldız (924): 68:29 ★★★ rab z=3,23 (6 kelimede 1 Rab) — içerik iddiası değil",
  "ölçüm iltifât (1017 ailesi): 68:22 iltifât 1 (68:21 anlatı → 68:22 alıntı içi 2MP), 68:23 iltifât 1 (alıntı → anlatı) — alıntı sınırı iltifât sayılıyor; 68:24, 68:26-29 alıntılar iltifât değil",
  "ölçüm kip (517 ailesi): 68:29 tekit 'inne' kip alanında yok; 68:28 'levlâ' teşvik kip alanında yok",
  "esit2 / xref: 68:27 ↔ 56:67 TAM (okundu); 68:30 ↔ 37:27, 37:50, 52:25 BENZER; 68:29 xref 17:93, 17:108; 68:26 xref 83:32 (henüz okunmadı)",
  "adsız (aday 1017): bahçe sahipleri, 'evsatuhum' (68:28), yoksul (68:24) — ad verilmedi",
  "çıpa: blokta doğal olgu yok (68:22 tarım insan eylemi); tarayıcı v4 adayı 68:22 — çıpa değil",
  "fâsıla: blok içi on ayet ن (N sınıfı); kafiye kırığı 0 (blok içi)",
  "aday 1040 (kayıt): 67:27 'fe-lemmâ ra'evhu' / 68:26 'fe-lemmâ ra'evhâ' — ardışık sûrede açılış eşi; test yok",
  "aday 1041 (kayıt): kök قدر 67:1 'qadîr' (İLÂHÎ) / 68:25 'qâdirîn' (bahçe sahipleri) — kök düzeyinde sınır vakası, lemmalar ayrı",
  "karşıt çift (aday 1039, okuma): on ayette yok",
  "tetik: ön kuru koşu 0 uyuşmaz (68:24 ◈K يوم); kayıtta 0; [x/y] 0 (36 sayım)",
 ], (31, 41): [
  "esmâ: e_oto 1 token (68:33 'el-âhira' — 've le-azâbu'l-âhira'); DEĞİL; KARAR 651 → 652; esma_kayit mühür EVET, karar sonrası geçersiz (1022); blokta geçerli mühür yok",
  "kök tablosu: blokta eksik kök yok; 1441 değişmedi; retroaktif yama hedef 3 (önceki bloktan, okunmamış), yama 0, genel geçiş 0",
  "yıldız (924): 68:32 ★★★ rab z=3,94 (10 kelimede 2 Rab), 68:34 ★★★ rab z=3,23 (6 kelimede 1 Rab) — içerik iddiası değil",
  "ölçüm iltifât: 68:35 iltifât 1 (68:34 3MP → 68:35 1P), 68:36 iltifât 1 (1P → 2MP); 68:40 2MP → 2MS / 3MP ölçümde iltifât değil (araç alanı, 924)",
  "ölçüm kip (517 ailesi): 68:37, 68:39, 68:41 'em' sorusu kip alanında yok (68:39, 68:41 başka kip var); 68:31, 68:34 tekit 'inne' kip alanında yok; 68:32 'asâ' ümit kip alanında yok",
  "gloss (1021 ailesi): أيي 68:40 'eyyuhum' (hangisi) — gloss 'âyet, işaret'; أخر 68:33 'el-âhira' (âhiret) — gloss 'geciktirme, sonraya bırakma'; جنن 68:34 'cennât'",
  "esit2 / xref: 68:31 ↔ 21:14 BENZER (okundu); 68:36 ↔ 37:154 TAM (okundu); 68:33 xref 16:41, 39:26 (okundu); 68:34 xref 3:15, 98:8 (henüz okunmadı)",
  "adsız (aday 1017): bahçe sahipleri (68:31-32), 3MP (68:33), 1P konuşan (68:35, 68:39), 2MP muhatap (68:36-39), 2MS muhatap ve 3MP (68:40-41), 'şurakâ' — ad verilmedi",
  "çıpa: blokta doğal olgu yok (68:34 cennet, 68:39 kıyamet günü âhiret, olgu=False); tarayıcı adayı yok",
  "fâsıla: blok içi ن (68:31-33, 35-39, 41) ve م (68:34, 68:40), hepsi N sınıfı; kafiye kırığı 0 (blok içi)",
  "aday 1040 (kayıt): blokta ardışık sûre eşi aranmadı; vaka yok",
  "aday 1041 (kayıt): blokta vaka yok",
  "karşıt çift (aday 1039, okuma): 68:35 müslimler / mücrimler; 68:33-34 âhiret azabı / nimet cennetleri; öbür dokuz ayette yok",
  "tetik: ön kuru koşu 0 uyuşmaz (68:39 ◈K يوم); kayıtta 0; [x/y] 0 (45 sayım)",
 ], (42, 52): [
  "esmâ: e_oto 1 token (68:45 'metîn' — 'inne keydî metîn'); DEĞİL; KARAR 652 → 653; esma_kayit mühür EVET, karar sonrası geçersiz (1022); blokta geçerli mühür yok",
  "kök tablosu: blokta eksik kök yok; 1441 değişmedi; retroaktif yama hedef 3 (önceki bloktan, okunmamış), yama 0, genel geçiş 0",
  "yıldız (924): 68:42 ★★★ pas z=3,48, 68:43 ★ pas z=1,57, 68:49 ★★ pas z=2,52, 68:48 ★ rab z=1,62, 68:50 ★★★ rab z=3,94 — içerik iddiası değil",
  "ölçüm iltifât: blokta iltifât 0; 68:44 1S → 1P (konuşan) ve 68:46 3MP → 2MS ölçümde iltifât değil (araç alanı, 924)",
  "ölçüm kip (517 ailesi): 68:46, 68:47 'em' sorusu kip alanında yok; 68:45 tekit 'inne' kip alanında yok; 68:44 biçim DIKKAT etiketi — dayanağı ölçümde görünmüyor (924)",
  "esit2 / xref: 68:45 ↔ 7:183 TAM (henüz okunmadı) — ölçüm aynı eşi iki kez yazıyor (araç alanı); 68:46 ↔ 52:40 TAM, 68:47 ↔ 52:41 TAM (okundu); 68:52 ↔ 38:87 (okundu), 81:27 (henüz okunmadı) BENZER; xref 68:43 → 70:44, 68:44 → 7:182, 68:48 → 52:48, 76:24",
  "nakarat3: 68:42 / 68:43 'da'â + ilâ + sucûd' — süzgeç GEÇMEZ (sûre içi iki ayet)",
  "adsız (aday 1017): 68:42 açan ve çağıran (edilgen), 3MP, 1S / 1P konuşan (68:44-45), 2MS muhatap, 'sâhibu'l-hût' (68:48-50), 'ellezîne keferû' (68:51), 68:52 'huve' göndergesi — ad verilmedi",
  "çıpa: blokta doğal olgu yok (68:42 âhiret sahnesi, 68:49 anlatı içi olay); tarayıcı adayı yok",
  "fâsıla: blok içi ن (68:42-47, 50-52) ve م (68:48, 68:49), hepsi N sınıfı; kafiye kırığı 0 (blok içi)",
  "aday 1040 (kayıt): blokta ardışık sûre eşi yok; 52:40-41 / 68:46-47 iki ardışık TAM eş — sûreler ardışık değil, kayıt",
  "aday 1041 (kayıt): lemma 'metîn' 51:58 (İLÂHÎ sıfat, lafzın haberi) / 68:45 ('keydî' sıfatı, 1S konuşanın düzeni) — sınır vakası, kayıt",
  "karşıt çift (aday 1039, okuma): 68:42-43 güç yetirememe / sağlamken; 68:49-50 kınanmış / salihlerden; 68:51-52 deli / âlemlere zikir; öbür sekiz ayette yok",
  "tetik: ön kuru koşu 3 uyuşmaz (68:42 ◈K يوم, 68:43 ◈B بصر, 68:51 ◈B بصر سمع — satırlar dolduruldu); kayıtta 0; [x/y] 0 (76 sayım)",
 ],
}

DUZELTME = {
}
