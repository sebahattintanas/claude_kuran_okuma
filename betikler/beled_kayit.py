# -*- coding: utf-8 -*-
"""beled_kayit.py — sûre 90 (Beled) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 90

CIPA = {
 # blok 1-10
 1: dict(kademe=None, olgu=False, cipa=False, not_="'lâ uqsimu bi-hâze'l-beled' — yemin edilen yer, gönderge yalnız işaretle (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'ve ente hillun bi-hâze'l-beled' — hitap, belde adsız (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'ve vâlidin ve mâ veled' — gönderge adsız (doğuran / doğurulan); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe='L1', olgu=True, cipa=False, not_="'leqad xalaqne'l-insâne fî kebed' — yaratma + durum; aşama / madde / mekanizma yok — L1 (76:2 kaydı emsali); tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'e-yahsebu en len yaqdira 'aleyhi ehad' — insan tutumu (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'yeqûlu ehlektu mâlen lubedâ' — insan tutumu, söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'e-yahsebu en lem yerahû ehad' — insan tutumu (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe='L1', olgu=True, cipa=False, not_="'e-lem nec'al lehû 'ayneyn' — organ verilmiş olarak adlanıyor; işlev / mekanizma yok — L1 (78:6 kaydı emsali); tarayıcı vermedi"),
 9: dict(kademe='L1', olgu=True, cipa=False, not_="'ve lisânen ve şefeteyn' — organ, 90:8'e atıf; işlev / mekanizma yok — L1; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'ve hedeynâhu'n-necdeyn' — yol gösterme (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 11-20
 11: dict(kademe=None, olgu=False, cipa=False, not_="'fe-le'qtehame'l-'aqabe' — insan tutumu (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 12: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ edrâke me'l-'aqabe' — soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'fekku raqabe' — eylem (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe=None, olgu=False, cipa=False, not_="'ev it'âmun fî yevmin zî mesğabe' — eylem (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="'yetîmen zâ maqrabe' — eylem (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 16: dict(kademe=None, olgu=False, cipa=False, not_="'ev miskînen zâ metrabe' — eylem (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 17: dict(kademe=None, olgu=False, cipa=False, not_="'thumme kâne mine'llezîne âmenû …' — inanç / tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 18: dict(kademe=None, olgu=False, cipa=False, not_="'ulâ'ike ashâbu'l-meymene' — âhiret, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 19: dict(kademe=None, olgu=False, cipa=False, not_="'ve'llezîne keferû bi-âyâtinâ hum ashâbu'l-meş'eme' — âhiret, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 20: dict(kademe=None, olgu=False, cipa=False, not_="''aleyhim nârun mu'sade' — âhiret, azap (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: e_oto 2 token (90:5:6, 90:7:5 'ehad' — olumsuz cümlede 'hiç kimse'); esma_el_ekle ile 'degil' (yamalar/esma_el_90_1_10.txt; KARAR 718 → 720); bilançoda esma_muhur_43 [5, 7], geçerli mühür []; lafız ve Rab yok",
  "kök tablosu: kok_ekle_90 3 kök (كبد 90:4, شفه 90:9, نجد 90:10; üçü korpusta tek ayet); 1518 → 1521; retroaktif yama hedefli 0, genel 0 (ikinci koşu da 0)",
  "süreç (89:21-30'dan devreden not): o bloğun kaydından sonraki genel retroaktif gloss geçişi 89:21 kaydının dikey alanını yamaladı — kök جمم gloss'u kök biçimi دكك'i taşıyor, gloss geçişi bu anmayı yeniden sardı; taban kayıtları değişmedi (git HEAD okuma_metni ile karşılaştırıldı), ikinci koşu 0; 89:21 kaydına dokunulmadı, protokol gereği bu bloğun ARIZA'sına yazıldı (1021)",
  "yıldız: ★★★ 90:4, 9, 10 hapaks z=3,28 (bu blokta eklenen kökler); ★ 90:6 kaynak n, kafiye kırığıyla — formül davranışı",
  "fâsıla: 90:1-5 د, 90:6 ا (ölçüm KAFİYE KIRILMASI, gerçek), 90:7 د, 90:8-10 ن; د → ن geçişi işaretlenmedi (924)",
  "iltifât: 90:2 {1} → {2} (1S yeminden 2MS hitaba) gerçek; 90:3 {2} → {3} ilgi cümlesi fiili 'veled' — konuşan / hitap değişmiyor (924); 90:4 {3} → {1} 1P konuşan gerçek; 90:5 {1} → {3} insan anlatımı gerçek",
  "biçim (924): 90:1 yemin fiilinin önündeki 'lâ' NEG sayılıyor; 90:3 atıflı yeminde QASEM yok; 90:5, 7 'ehad' sayı işareti yanlış pozitif; ayet 1 harf 34 → harf3 15 (besmele ailesi)",
  "alıntı: 90:6 'yeqûlu' ('qâle' lemması) ile işaretli söz, ayet sonunda kapanıyor — meal tırnaklı",
  "adsız gönderge (1017): 90:1 konuşan 1S; 90:2 muhatap 2MS; 90:3 doğuran / doğurulan; 90:4, 8, 10 konuşan 1P; 90:5-7 öznesi yazılmamış (90:4 insan, okuma)",
  "KAPATILAMAZ: 90:1-2 beldenin adı (yalnız işaret 'hâzâ'); 90:3 doğuran / doğurulanın kim olduğu; 90:2 'hill' (konaklayan / helâl) — meal konaklama okumasını seçti; 90:10 'necdeyn'in hangi iki yol olduğu",
  "çıpa: L1 3 (90:4 yaratma + durum, 76:2 emsali; 90:8 göz, 78:6 emsali; 90:9 dil + dudak, atıf); olgu=False 7; tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 89:30 / 90:1 sûre sınırı — 1S konuşanın 2FS'ye giriş emri ile kapanış / 1S yemin ile açılış; fâsıla ى → د; 89 Rab ile sürdü (8), 90:1-10'da lafız ve Rab yok; ardışık sûre okuma bağları 89:11 / 90:1 'beled', 89:25 / 90:5 'ehad', 89:20 / 90:6 'mâl'",
  "aday 1041: blokta kayıt yok — lafız ve Rab yok; 1S / 1P konuşan adsız",
  "bağ: kalıp / lemma eşleri okumayla (75:1, 75:3, 75:36, 77:25, 78:6, 76:3, 89:8, 89:20); bütün emsaller sohbette AR + meal ile basıldı",
  "◈K / ◈B: ◈K tetik yok; ◈B dolu 90:4 خلق أنس, 90:8 عين; ولد (90:3), لسن ve شفه (90:9) tetik listesinde değil — '—', gözlem ◇'de; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 10 / 0; oturum_xy 25 sayım, 0 uyuşmaz",
  "süreç: sûre 90 dosyaları fecr_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_90.py, oturum dışı); blok sınırı sûrenin bölümlerine göre (1-10 yemin + insan + verilenler; 11-20 sarp yokuş + iki grup); taban 75699c1 değişmedi — sûre 90 zip'i 87-89'u da taşıyacak",
 ],
 (11, 20): [
  "esmâ: e_oto 0 token; KARAR değişmedi (720); lafız ve Rab yok — sûre 90 lafızsız ve Rabsız",
  "kök tablosu: kok_ekle_90 2 kök (فكك 90:13, korpusta 2 ayet; سغب 90:14, tek ayet); 1521 → 1523; retroaktif yama hedefli 0, genel 0 (ikinci koşu da 0)",
  "yıldız: ★★★ 90:14 hapaks z=3,28 (سغب) — formül davranışı; blokta başka yıldız yok",
  "fâsıla (924): 90:11-20 ة (on ayet); 90:10 ن → 90:11 ة geçişi kafiye kırığı işaretlenmedi",
  "iltifât: blokta ölçüm 0; 90:12 2MS hitap (sahset ['2', '3']) ve 90:19 1P ('âyâtinâ') kısmi örtüşmeyle iltifât vermiyor (924)",
  "biçim (924): 90:11 'fe-lâ' + PERF NEG doğru; 90:13-16 fiilsiz cevap dizisi (mastar + nesneler) biçim alanında görünmüyor",
  "adsız gönderge (1017): 90:11 ve 90:17 öznesi yazılmamış (90:10'un 3MS'si, okuma); 90:12 muhatap 2MS; 90:19 konuşan 1P",
  "esit2: 90:12 BENZER → 69:3 (basıldı)",
  "çıpa: blokta merdiven uygulanan ayet yok (10 ayetin 10'u olgu=False: tutum, soru, eylem, âhiret); tarayıcı v4 blokta aday vermedi",
  "aday 1039: ayetler arası 2 (90:17 / 19 iman / inkâr; 90:18 / 19 sağ / sol)",
  "aday 1041: blokta kayıt yok — lafız ve Rab yok",
  "bağ: kalıp / lemma eşleri okumayla (69:3, 74:27, 56:8, 56:9, 76:8, 69:34, 83:29, 47:4, 89:17, 89:18); bütün emsaller sohbette AR + meal ile basıldı; 56:8-9 / 90:18-19 iki sûrede aynı sırayla iki ardışık ayet",
  "◈K / ◈B: ◈K dolu 90:14 يوم; ◈B tetik yok; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 1-20 toplam 20 / 0; oturum_xy blok 27, 1-20 toplam 52 sayım, 0 uyuşmaz",
 ],
}

DUZELTME = {
}
