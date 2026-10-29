# -*- coding: utf-8 -*-
"""tekvir_kayit.py — sûre 81 ('Tekvîr) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 81

CIPA = {
 # blok 1-10
 1: dict(kademe='L1', olgu=True, cipa=False, not_="'ize'ş-şemsu kuvviret' — âhirette kozmik olay (güneş), süreç adlı, nedensellik / mekanizma yok — L1; tarayıcı vermedi"),
 2: dict(kademe='L1', olgu=True, cipa=False, not_="'ize'n-nucûmu'nkederet' — âhirette kozmik olay (yıldızlar) — L1; tarayıcı vermedi"),
 3: dict(kademe='L1', olgu=True, cipa=False, not_="'ize'l-cibâlu suyyiret' — âhirette kozmik olay (dağlar) — L1 (78:20 kaydı emsali); tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'ize'l-'işâru 'uttilet' — âhiret, hayvan sınıfı, kozmik olay değil (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'ize'l-vuhûşu huşiret' — âhiret, hayvan sınıfı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe='L1', olgu=True, cipa=False, not_="'ize'l-bihâru succiret' — âhirette kozmik olay (denizler); fiil anlamı KAPATILAMAZ (tutuşturma / doldurma) — L1; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'ize'n-nufûsu zuvvicet' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'ize'l-mev'ûdetu su'ilet' — âhiret, insan yapımı fiil (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 9: dict(kademe=None, olgu=False, cipa=False, not_="'bi-eyyi zenbin qutilet' — âhiret, soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'ize's-suhufu nuşiret' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 11-20
 11: dict(kademe='L1', olgu=True, cipa=False, not_="'ize's-semâ'u kuşitat' — âhirette kozmik olay (gök) — L1; tarayıcı vermedi"),
 12: dict(kademe=None, olgu=False, cipa=False, not_="'ize'l-cahîmu su''iret' — âhiret, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'ize'l-cennetu uzlifet' — âhiret, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe=None, olgu=False, cipa=False, not_="''alimet nefsun mâ ahdarat' — âhiret, şart cevabı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="'fe-lâ uqsimu bi'l-xunnes' — yemin edilen adsız, gönderge yok; merdiven uygulanmadı; tarayıcı vermedi"),
 16: dict(kademe=None, olgu=False, cipa=False, not_="'el-cevâri'l-kunnes' — yemin edilenin sıfatları, gönderge adsız; merdiven uygulanmadı; tarayıcı vermedi"),
 17: dict(kademe='L0', olgu=True, cipa=False, not_="'ve'l-leyli izâ 'as'as' — zaman zarfı olarak gece — L0; fiil anlamı KAPATILAMAZ; tarayıcı vermedi"),
 18: dict(kademe='L0', olgu=True, cipa=False, not_="'ve's-subhi izâ teneffes' — zaman zarfı olarak sabah — L0; tarayıcı vermedi"),
 19: dict(kademe=None, olgu=False, cipa=False, not_="'innehû le-qavlu rasûlin kerîm' — söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 20: dict(kademe=None, olgu=False, cipa=False, not_="'zî quvvetin 'inde zi'l-'arşi mekîn' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 21-29
 21: dict(kademe=None, olgu=False, cipa=False, not_="'mutâ'in themme emîn' — gaybî, elçinin nitelenmesi (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 22: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ sâhibukum bi-mecnûn' — söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 23: dict(kademe='L0', olgu=True, cipa=False, not_="'ve le-qad re'âhu bi'l-ufuqi'l-mubîn' — ufuk yer adı olarak adlanıyor, süreç yok — L0; görme olayı gaybî; tarayıcı vermedi"),
 24: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ huve 'ale'l-ğaybi bi-danîn' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 25: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ huve bi-qavli şeytânin racîm' — söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 26: dict(kademe=None, olgu=False, cipa=False, not_="'fe-eyne tezhebûn' — soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 27: dict(kademe=None, olgu=False, cipa=False, not_="'in huve illâ zikrun li'l-'âlemîn' — söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 28: dict(kademe=None, olgu=False, cipa=False, not_="'li-men şâ'e minkum en yesteqîm' — söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 29: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ teşâ'ûne illâ en yeşâ'a'llâhu rabbu'l-'âlemîn' — söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: e_oto 0 token; KARAR değişmedi (694); lafız 0, Rab 0",
  "kök tablosu: kok_ekle_81 3 kök (كدر 81:2; وحش 81:5; وأد 81:8 — ölçüm kök alanında '???' → eklendi; üçü de korpusta tek ayet); 1496 → 1499; retroaktif yama hedefli 0, genel 0 (ikinci koşu da 0)",
  "harf alanı: ayet 1 ölçümünde harf 31 → harf3 12, isaret 0 (ayet 1 ailesi; besmele); araç alanı (924)",
  "yıldız: on ayetin onu ★★★ — dokuzunda pas z=5,38 (kısa tek fiilli edilgen; 81:2 VII. bab, edilgen değil), 81:2, 5, 8 hapaks z=3,28 (yeni kök) — formül davranışı, içerik iddiası değil",
  "sayı işareti (yanlış pozitif): 81:4 ''işâr' (kök عشر 'on'), 81:7 'zuvvicet' (kök زوج) — metinde sayı yok; kök عشر gloss'u ''işâr'da uymuyor (1021)",
  "biçim / kip (924): 'izâ' şart zarfı dokuz ayette kip alanında çıkmıyor (edim haber, kip yok); şart cevabı bu blokta yok — henüz okunmadı, KAPATILAMAZ",
  "adsız gönderge (1017): dokuz edilgen fiilin faili adsız; 81:8 soran ve gömen, 81:9 öldüren adsız; 81:7 eşleştirilenler KAPATILAMAZ",
  "alıntı (1017): 81:8-9 'su'ilet' söz fiili ama 'qâle / qîle' değil; soru 3FS 'qutilet' — dolaylı aktarım, meal tırnaksız",
  "okuma ikiliği: 81:6 'succiret' tutuşturma / doldurup taşırma KAPATILAMAZ (kök سجر gloss'u iki anlamı birlikte veriyor)",
  "fâsıla: 81:1-10 hepsi ت (ölçüm ve metin uyumlu); sûre sınırı 80:42 ة → 81:1 ت",
  "aday 1040 (kayıt): 80:42 / 81:1 sûre sınırı — işaret zamiri + hasr ile yargı, sûre sonu / şart zarfı ile kozmik olay dizisi açılışı; fâsıla ة → ت; ikisi de lafızsız, Rabsız",
  "aday 1040 ailesi (okuma): ardışık sûrede 80:13 'suhuf' / 81:10; 80:22 kök نشر 'enşerah' (diriltme) / 81:10 'nuşiret' (sayfalar); 80:17 edilgen 'qutile' / 81:9 'qutilet'; 80:33 'fe-izâ' ile âhiret açılışı / 81:1-10 'izâ' dizisi",
  "bağ: kalıp / lemma eşleri okumayla (39:5, 75:9, 77:8, 77:10, 78:20, 22:45, 52:6, 74:52); 82:3 henüz okunmadı — bağ yazılmadı",
  "◈K / ◈B: ◈K dolu 81:1 شمس, 81:2 نجم, 81:3 جبل, 81:6 بحر; ◈B dolu 81:7 زوج (eşleştirme, üreme aşaması değil); 81:4-5 hayvan adları tetik listesinde değil — '—', gözlem ◇'de",
  "süreç: sûre 81 dosyaları abese_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_81.py, oturum dışı); tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 21 sayım 0 uyuşmaz",
 ],
 (11, 20): [
  "esmâ: e_oto 1 token (81:19 'kerîm') — karar DEĞİL (elçinin sıfatı); KARAR 694 → 695; ölçüm satırı 'SON konum, MÜHÜRSÜZ' — mühür iddiası bilançodan (1022)",
  "kök tablosu: kok_ekle_81 4 kök (كشط 81:11; خنس 81:15; كنس 81:16; عسعس 81:17); 1499 → 1503; retroaktif yama hedefli 0, genel 0 (ikinci koşu da 0); خنس 2 ayetlik (öbürü henüz okunmadı) — hapaks yıldızı yok",
  "yıldız: ★★★ 7 (81:11, 12, 13 pas z=5,38; 81:11, 16, 17 hapaks — yeni kök); yıldızsız 81:14, 15, 18, 19, 20 — formül davranışı, içerik iddiası değil",
  "biçim (924): atıflı yeminler (81:17, 18) biçim alanında QASEM yok, yalnız 81:15; 'fe-lâ uqsimu' kip NEG (yemin girişi); 81:14 şart cevabı kip alanında yok",
  "ölçüm iltifât (924): 81:17 {1} → {3} iltifât 1 — 1S yeminden 3MS fiile; konuşan değişmiyor",
  "adsız gönderge (1017): 81:11-13 failler; 81:15 konuşan 1S; 81:15-16 yemin edilen 'xunnes / cevâr / kunnes' (ne olduğu KAPATILAMAZ, çıpa merdiveni uygulanmadı); 81:19 'hu' ve elçi adsız",
  "okuma ikiliği: 81:14 'nefsun' (her can / bir can); 81:17 ''as'as' (kararıp gelme / çekilip gitme) KAPATILAMAZ",
  "gloss (1021): kök نفس 'nefis, can' 81:18 'teneffese'de (sabahın nefes alması) uymuyor; kök جري 'akma' 81:16 'cevâr'da gönderge adsız",
  "fâsıla: 81:1-14 ت, 81:15-18 س, 81:19 م, 81:20 ن (ölçüm N sınıfı); geçişler 81:14 → 15, 81:18 → 19 — ölçüm KAFİYE KIRILMASI işaretlemedi (924)",
  "aday 1041 (kayıt): 81:20 'zû' — 'zî quvva' (elçi) / 'zi'l-'arş' (arşın sahibi, lafızsız) aynı ayette",
  "aday 1040: bu blokta ardışık sûre bağı yok; 79:36 (iki sûre önce) okuma bağı",
  "bağ: kalıp / lemma eşleri okumayla (77:9, 79:36, 26:90, 50:31, 56:75, 69:38, 55:24, 74:33, 74:34, 69:40, 17:42, 40:15, 53:5, 77:21); 82:5, 84:16, 86:13 henüz okunmadı — bağ yazılmadı",
  "◈K / ◈B: ◈K dolu 81:11 سمو ('semâ'', S1 izinli), 81:17 ليل; 81:18 صبح tetik listesinde değil — '—'; ◈B tetik yok",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 24 sayım 0 uyuşmaz; kayıttan önce düzelttiklerim: esma_el yorumunda basılmamış ayet numarası (emsal adı) — çıkarıldı; 17:42 harf çevirisi; 81:13 'son ve izâ' sırası (dizinin on ikinci 'izâ'sı, 've izâ'nın on birincisi)",
 ],
 (21, 29): [
  "esmâ: e_oto 1 token (81:23 'mubîn') — karar DEĞİL (ufkun sıfatı); KARAR 695 → 696; ölçüm satırı 'SON konum, MÜHÜRSÜZ' — mühür iddiası bilançodan (1022); 81:29 'rabbu'l-'âlemîn' Rab ekseninde, esmâ e_oto yok",
  "lafız / Rab: sûrenin tek lafzı ve tek Rab'ı 81:29 (ölçüm 6. ve 7. sıra, 8 kelime); ★★ lafız z=1,97, rab z=2,34 — formül davranışı",
  "kök tablosu: kok_ekle_81 1 kök (ضنن 81:24); 1503 → 1504; retroaktif yama hedefli 0, genel 0 (ikinci koşu da 0); ★★★ hapaks 81:24 (yeni kök)",
  "ölçüm iltifât (924): 81:22 {3} → {2}, 81:23 {2} → {3}, 81:26 {3} → {2}, 81:27 {2} → {3} — konuşan değişmiyor, gönderge / muhatap değişimi",
  "adsız gönderge (1017): 81:21 elçi; 81:22 'sâhibukum' ve 2MP muhatap — elçi ile aynılığı metinde işaretli değil, KAPATILAMAZ; 81:23 gören / görülen KAPATILAMAZ; 81:24, 25, 27 'huve' göndergesi KAPATILAMAZ",
  "gloss (1021): kök جنن 81:13 'cenne' / 81:22 'mecnûn'; kök علم 81:14 'alimet' / 81:27, 29 ''âlemîn' — gloss ('bilme') ''âlemîn'de uymuyor",
  "fâsıla: 81:21-24 ن, 81:25 م, 81:26-27 ن, 81:28 م, 81:29 ن — ölçüm hepsi N sınıfı",
  "aday 1041 (kayıt): 'şâ'e' — 81:28 dileyen (muhatap), 81:29 'teşâ'ûne' (muhataplar) / 'yeşâ'a'llâh'",
  "aday 1040 (kayıt): ardışık sûrede sıralı eşleşme — 80:11-12 öğüt + 'fe-men şâ'e' / 81:27-28 'zikr' + 'li-men şâ'e'; 81:29 → 82:1 sûre sınırı 82:1 okunurken",
  "bağ: kalıp / lemma eşleri okumayla (26:107, 53:2, 34:46, 68:2, 53:7, 53:13, 69:41, 38:87, 68:52, 74:37, 76:29, 76:30, 80:11, 80:12); 6:128, 7:89 (ölçüm xref) henüz okunmadı — bağ yazılmadı",
  "◈K / ◈B: tetik yok — dokuz ayette iki satır da '—'; 81:23 أفق tetik listesinde değil",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) ilk taslakta 1 uyuşmaz yakaladı (81:23 ◈K dolu yazılmıştı — tetik yok) → '—', gözlem ◇'ye; ikinci koşu 0; sûre geneli 29 ayet / 0. oturum_xy 21 sayım 0 (sûre geneli 66 / 0); kayıttan önce düzelttiğim: 81:29 lafız / Rab konumu ifadesi ('sondan üçüncü ve ikinci kelime')",
 ],
}

DUZELTME = {
}
