# -*- coding: utf-8 -*-
"""abese_kayit.py — sûre 80 ('Abese) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 80

CIPA = {
 # blok 1-10
 1: dict(kademe=None, olgu=False, cipa=False, not_="''abese ve tevellâ' — kişinin tavrı (olgu=False); özne adsız; merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'en câ'ehu'l-a'mâ' — kişi nitelemesi (kör), doğa olgusu iddiası değil (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ yudrîke le'allehû yezzekkâ' — hitap (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'ev yezzekkeru fe-tenfe'ahu'z-zikrâ' — hitap (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'emmâ meni'stağnâ' — tafsîl (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'fe-ente lehû tesaddâ' — hitap (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ 'aleyke ellâ yezzekkâ' — hitap (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'ve emmâ men câ'eke yes'â' — tafsîl (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 9: dict(kademe=None, olgu=False, cipa=False, not_="'ve huve yaxşâ' — hâl (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'fe-ente 'anhu telehhâ' — hitap (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 11-20
 11: dict(kademe=None, olgu=False, cipa=False, not_="'kellâ innehâ tezkira' — söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 12: dict(kademe=None, olgu=False, cipa=False, not_="'fe-men şâ'e zekerah' — söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'fî suhufin mukarrama' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe=None, olgu=False, cipa=False, not_="'merfû'atin mutahhara' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="'bi-eydî sefera' — gaybî, yazıcılar adsız (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 16: dict(kademe=None, olgu=False, cipa=False, not_="'kirâmin berara' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 17: dict(kademe=None, olgu=False, cipa=False, not_="'qutile'l-insânu mâ ekferah' — beddua / taaccüb (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 18: dict(kademe=None, olgu=False, cipa=False, not_="'min eyyi şey'in xalaqah' — soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 19: dict(kademe='L1', olgu=True, cipa=False, not_="'min nutfetin xalaqahû fe-qaddarah' — madde (nutfe) + yaratma + ölçme, aşama ardışıklığı ve nedensellik yok — L1 (76:2 emsali); tarayıcı vermedi"),
 20: dict(kademe=None, olgu=False, cipa=False, not_="'thumme's-sebîle yessarah' — yol göndergesi KAPATILAMAZ (doğum / hayat yolu) (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 21-30
 21: dict(kademe='L1', olgu=True, cipa=False, not_="'thumme emâtehû fe-eqberah' — ölüm + defin, süreç adlı, nedensellik / mekanizma yok — L1; tarayıcı vermedi"),
 22: dict(kademe=None, olgu=False, cipa=False, not_="'thumme izâ şâ'e enşerah' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 23: dict(kademe=None, olgu=False, cipa=False, not_="'kellâ lemmâ yeqdi mâ emerah' — yargı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 24: dict(kademe='L0', olgu=True, cipa=False, not_="'fe'l-yenzuri'l-insânu ilâ ta'âmih' — yiyecek adlanıyor, süreç yok — L0; tarayıcı vermedi"),
 25: dict(kademe='L1', olgu=True, cipa=False, not_="'ennâ sabebne'l-mâ'e sabbâ' — su + dökme süreci, mekanizma yok — L1; tarayıcı vermedi"),
 26: dict(kademe='L1', olgu=True, cipa=False, not_="'thumme şeqaqne'l-arda şaqqâ' — yer + yarma süreci, mekanizma yok — L1; tarayıcı vermedi"),
 27: dict(kademe='L1', olgu=True, cipa=False, not_="'fe-enbetnâ fîhâ habbâ' — su → yer yarılması → tane, 'thumme' / 'fe' ile sıralı, 'bihî' / ta'lîl yok — L1 (L2 sınır vakası: 50:9 'bihî', 78:15 ta'lîl ile L2); tarayıcı vermedi"),
 28: dict(kademe='L1', olgu=True, cipa=False, not_="''ineben ve qadbâ' — bitki adları, 80:25-27 zincirinin halkası — L1 (78:16 kaydı emsali); tarayıcı vermedi"),
 29: dict(kademe='L1', olgu=True, cipa=False, not_="'zeytûnen ve naxlâ' — bitki adları, zincir halkası — L1; tarayıcı vermedi"),
 30: dict(kademe='L1', olgu=True, cipa=False, not_="'hadâ'iqa ğulbâ' — bahçe + nitelik, zincir halkası — L1 (78:16 kaydı emsali); tarayıcı vermedi"),
 # blok 31-42
 31: dict(kademe='L1', olgu=True, cipa=False, not_="'fâkiheten ve ebbâ' — bitki adları, zincirin son halkası — L1 (78:16 kaydı emsali); tarayıcı vermedi"),
 32: dict(kademe='L1', olgu=True, cipa=False, not_="'metâ'an lekum ve li-en'âmikum' — işlev adı (yararlanma), nedensellik bağı yok — L1 (79:33 kaydı emsali); tarayıcı vermedi"),
 33: dict(kademe=None, olgu=False, cipa=False, not_="'fe-izâ câ'eti's-sâxxa' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 34: dict(kademe=None, olgu=False, cipa=False, not_="'yevme yefirru'l-mer'u min axîh' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 35: dict(kademe=None, olgu=False, cipa=False, not_="'ve ummihî ve ebîh' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 36: dict(kademe=None, olgu=False, cipa=False, not_="'ve sâhibetihî ve benîh' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 37: dict(kademe=None, olgu=False, cipa=False, not_="'li-kulli'mri'in minhum yevme'izin şe'nun yuğnîh' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 38: dict(kademe=None, olgu=False, cipa=False, not_="'vucûhun yevme'izin musfira' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 39: dict(kademe=None, olgu=False, cipa=False, not_="'dâhiketun mustebşira' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 40: dict(kademe=None, olgu=False, cipa=False, not_="'ve vucûhun yevme'izin 'aleyhâ ğabera' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 41: dict(kademe=None, olgu=False, cipa=False, not_="'tarhaquhâ qatara' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 42: dict(kademe=None, olgu=False, cipa=False, not_="'ulâ'ike humu'l-kefaratu'l-fecera' — yargı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: e_oto 0 token; KARAR değişmedi (692); bilanço esma_muhur_43 [], geçerli []",
  "kök tablosu: kok_ekle_80 1 kök (صدي 80:6; ölçüm kök alanında '???' → eklendi); 1492 → 1493; retroaktif yama 'daha önce okunmuş 1 ayet' — kök صدي'nin sûre 8 ayeti, okuma_metni'nde kayıt yok, atlandı; hedefli 0, genel 0 (ikinci koşu da 0); 2 ayetlik kök — hapaks yıldızı yok",
  "harf alanı: ayet 1 ölçümünde harf 27 → harf3 8, isaret 0 (ayet 1 ailesi; besmele); araç alanı (924)",
  "fâsıla (924): 80:1, 3, 4 ölçüm 'ٓ' (medde) sınıfı — metinde ى; 80:2 KAFİYE KIRILMASI sahte (80:1 medde artefaktından), bilanço ★ kaynağı 'n', kafiye_kirik True (aday 1001); metinde 80:1-10 hepsi ى; gerçek geçiş ا → ى sûre sınırında (79:46 → 80:1)",
  "ölçüm iltifât (tanım, 924): 80:2 → 3 {3} → {2, 3} kısmi örtüşme — 3MS anlatıdan 2MS hitaba geçiş iltifât sayılmıyor",
  "adsız gönderge (1017): 80:1 yüzünü ekşiten 3MS; 80:2 'el-a'mâ'; 80:3-10 muhatap 2MS; 80:5 yeterli gören; 80:8 koşarak gelen — 80:1 3MS ile 80:3 2MS'nin ve 80:2 kör ile 80:8 gelenin aynılığı metinde işaretli değil, KAPATILAMAZ (okuma: içerik koşutluğu)",
  "alıntı (1017): blokta söz işareti yok — tırnak yok",
  "okuma ikiliği: 80:7 've mâ 'aleyke' — 'mâ' olumsuz / soru KAPATILAMAZ (ölçüm NEG)",
  "aday 1040 (kayıt): 79:46 / 80:1 sûre sınırı — 3MP + saat ile kapanış / 3MS iki fiille açılış; fâsıla ا → ى",
  "aday 1040 ailesi (okuma): ardışık sûrede 79:18 'tezekkâ' / 80:3, 7; 79:37, 40 'emmâ men' tafsîli / 80:5, 8; 79:22 'yes'â' (sırt dönüp) / 80:8 (gelip); 79:43 'zikrâ' / 80:4; 79:45 'men yaxşâhâ' / 80:9 've huve yaxşâ'; 79:42-45 ve 80:3-10 2MS muhatap adsız",
  "aday 1039 (okuma): ayetler arası 80:3 / 80:7 ('le'allehû yezzekkâ' / 'ellâ yezzekkâ'), 80:5 / 80:8 (yeterli gören / koşarak gelen), 80:6 / 80:10 ('lehû tesaddâ' / ''anhu telehhâ')",
  "bağ: kalıp eşleri okumayla (33:63, 42:17, 74:22; ardışık 79:18, 22, 37, 40, 43, 45, 46); 87:9 henüz okunmadı — bağ yazılmadı",
  "◈K / ◈B: tetik yok — on ayette iki satır da '—'; 80:2 عمي (kör) tetik listesinde değil",
  "çıpa: blokun on ayeti olgu=False — kişi tavrı / hitap; 80:2 'kör' kişi nitelemesi, doğa olgusu iddiası olarak değerlendirilmedi; tarayıcı aday vermedi",
  "süreç: sûre 80 dosyaları naziat_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_80.py); tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 15 sayım 0 uyuşmaz",
  "morph (924, kayıttan sonra eklendi): 80:10 'telehhâ' morph'ta PERF I. bab 3MS etiketli — biçim IMPF V. bab 2MS (◈D bu biçimi yazıyor); ölçüm zaman PERF, şahıs 3MS 2 bu etiketten; ayet kayıtları değişmedi",
 ],
 (11, 20): [
  "esmâ: e_oto 2 token (80:16:1 'kerîm', 80:16:2 'berr' — 'kirâmin berara', yazıcıların sıfatı); ikisi DEĞİL; KARAR 692 → 694; esma_kayit 'mühür EVET (ÇİFT)', bilanço esma_muhur_43 [16], geçerli [] (1022)",
  "kök tablosu: yeni kök yok ('???' yok); retroaktif yama 0",
  "yıldız (924): 80:17 ★★ pas z=2,52 — formül davranışı; öbür 9 ayet yıldızsız",
  "fâsıla (924): ölçüm H sınıfı ة (80:11, 13-16) ile ه'yi (80:12, 17-20) birleştiriyor; gerçek geçişler ى → ة (80:10 → 11), ة → ه → ة (80:11 → 12 → 13), ة → ه (80:16 → 17) işaretsiz",
  "edilgen (924): 80:14 'merfû'a', 'mutahhara' edilgen ortaç — ölçüm EDİLGEN fiil saymıyor; 80:17 'qutile' sayılıyor",
  "adsız gönderge (1017): 80:11 'innehâ' (3FS) ve 80:12 'zekerahû' (3MS) göndergesi — 74:54-55'te ikisi 3MS — KAPATILAMAZ; 80:12 dileyen; 80:14 yükselten / arındıran; 80:15-16 'sefera' kim oldukları; 80:17 öldüren; 80:18-20 yaratan / ölçen / kolaylaştıran 3MS zamirle",
  "alıntı (1017): blokta söz işareti yok — tırnak yok",
  "okuma ikiliği: 80:17 'mâ ekferah' (taaccüb / soru), 80:20 'es-sebîl' (doğum yolu / hayat ve hidayet yolu) KAPATILAMAZ",
  "gloss (1021): سفر (yolculuk / kitaplar / yazıcılar) — kök iki anlamı birleştiriyor; برر 'iyilik; kara' — 'berara' için lemma sayısı verilmedi (eşsesli olabilir), kök sayısı verildi",
  "esit2: 80:12 → 74:55 TAM (basıldı)",
  "korpusun son geçişi: lemma 'tezkira' (9 ayetin 8'i okunmuştu) ve 'nutfe' (12 ayetin 11'i) 80:11 / 80:19 ile tamam",
  "aday 1040 ailesi (okuma): ardışık sûrede 79:35 'el-insân' + 'mâ' / 80:17",
  "bağ: kalıp eşleri okumayla (53:36, 74:54, 74:55, 76:2, 76:3); 76:2-3 nutfe / sebîl / küfür ögeleri 80:17-20'de yeniden (okuma)",
  "◈K / ◈B: ◈K tetik yok; ◈B dolu — 80:15 يدي, 80:17 أنس, 80:18 خلق, 80:19 نطف خلق",
  "çıpa: 80:19 L1 olgu=True (nutfe + yaratma + ölçme); 80:13-16 gaybî, 80:11-12, 17-18, 20 olgu=False; tarayıcı aday vermedi",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 22 sayım 0 uyuşmaz",
 ],
 (21, 30): [
  "esmâ: e_oto 0 token; KARAR değişmedi (694); bilanço esma_muhur_43 [], geçerli []",
  "kök tablosu: kok_ekle_80 1 kök (قضب 80:28; ölçüm kök alanında '???' → eklendi); 1493 → 1494; retroaktif yama 'daha önce okunmuş 1 ayet' — صدي'nin sûre 8 ayeti (kayıt yok, atlandı); hedefli 0, genel 0 (ikinci koşu da 0)",
  "hapaks (yeni kök dersi): 80:28 قضب ★★★ hapaks z=3,28 — içerik iddiası değil; öbür 9 ayet yıldızsız",
  "fâsıla (924): 80:24 ölçüm 'ٓ' (medde) — metinde ه; gerçek geçiş ه → ا (80:24 → 25) işaretsiz; 80:25-30 ا",
  "iltifât: 80:25 {3} → {1} ölçüm 1 — anlatıcı 3MS'den 1P konuşana geçiş",
  "adsız gönderge (1017): 80:21-22 öldüren / dirilten 3MS; 80:23 'yeqdi' öznesi ve 'emerahû'daki emreden — dağılım KAPATILAMAZ; 80:25-27 konuşan 1P adsız",
  "aday 1041 (kayıt): شيأ / 'şâ'e' — 80:12 'men şâ'e' (insan) / 80:22 'izâ şâ'e' (dirilten 3MS)",
  "aday 1039 (okuma): ayetler arası 80:21 / 80:22 ('emâtehû' / 'enşerahû')",
  "aday 1040 ailesi (okuma): ardışık sûrede 79:31 su (3MS, yerden çıkarma) / 80:25 (1P, dökme)",
  "gloss (1021): حبب 'sevgi' — 80:27 'habb' (tane); غلب 'üstün gelme' — 80:30 'ğulb' (sık, kalın)",
  "çıpa: 80:25-27 su → yer → tane dizisi 'thumme' / 'fe' ile sıralı ama 'bihî' / ta'lîl yok — L1, L2 sınır vakası (50:9, 78:15 L2 'bihî' / ta'lîl ile); 80:21 ölüm L1; 80:24 yiyecek L0; 80:28-30 bitki adları L1 (78:16 kaydı emsali); 80:22-23 olgu=False; tarayıcı aday vermedi",
  "bağ: kalıp eşleri okumayla (16:11, 31:10, 50:9, 78:15, 78:32; ardışık 79:31); 86:5 henüz okunmadı — bağ yazılmadı",
  "◈K / ◈B: ◈K dolu — 80:25 موه, 80:26 أرض; ◈B dolu — 80:21 موت, 80:24 أنس, 80:27 نبت; 80:28-30 bitki adları (عنب زيت نخل حدق) tetik listesinde değil",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 21 sayım 0 uyuşmaz",
 ],
 (31, 42): [
  "blok sınırı: sûrenin son 12 ayeti tek blok (31-40 + 41-42 iki ayetlik blok yerine)",
  "esmâ: e_oto 0 token; KARAR değişmedi (694); bilanço esma_muhur_43 [], geçerli []",
  "kök tablosu: kok_ekle_80 2 kök (أبب 80:31, صخخ 80:33; ölçüm kök alanında '???' → eklendi); 1494 → 1496; retroaktif yama 'daha önce okunmuş 1 ayet' — صدي'nin sûre 8 ayeti (kayıt yok, atlandı); hedefli 0, genel 0 (ikinci koşu da 0)",
  "hapaks (yeni kök dersi): 80:31 أبب, 80:33 صخخ ★★★ hapaks z=3,28 — içerik iddiası değil; öbür 10 ayet yıldızsız",
  "fâsıla (924): metinde 80:31 ا, 80:32 م, 80:33 ة, 80:34-37 ه, 80:38-42 ة; ölçüm 80:32'de N sınıfı ama KAFİYE KIRILMASI işaretlemiyor (79:33'te aynı ayette işaretlemişti — bağlama bağlı z eşiği); ة / ه ölçümde aynı H sınıfı",
  "biçim (924): 80:42 zamir fasl ile hasr ('ulâ'ike humu') biçim alanında yok",
  "iltifât: 80:32 {} → {2} ve 80:33 {2} → {3} ölçüm 1",
  "adsız gönderge (1017): 80:32 muhatap 2MP; 80:33 'es-sâxxa'; 80:34-37 'el-mer'' cins ve yakınları; 80:38-41 yüzlerin sahipleri; 80:42 'ulâ'ike' göndergesi (80:40-41, okuma); 80:33 'izâ' cevap sınırı KAPATILAMAZ",
  "aday 1040 (kayıt): ardışık sûrede TAM tekrar — 79:33 / 80:32 'metâ'an lekum ve li-en'âmikum' (esit2), ikisinin ardından aynı açılış 'fe-izâ câ'eti' + korpusta tek ad (79:34 'et-tâmmetu'l-kubrâ' / 80:33 'es-sâxxa'); harekesiz 'fe-izâ câ'eti' korpusun iki ayeti bunlar",
  "aday 1040 ailesi (okuma): 78:40 'yevme' + 'el-mer'' / 80:34",
  "aday 1039 (okuma): ayet içi 80:35 ('umm' / 'eb'); ayetler arası 80:38-39 / 80:40-41 (parlak, gülen, sevinen / tozlu, karartılı)",
  "korpusun son geçişi: lemma 'fâkiha' (80:31), 'farra' (80:34), 'şe'n' (80:37), 'rahiqa' (80:41)",
  "sûre içi tam sayım (hepsi bu oturumda basıldı): جيأ [3/3], غني [2/2], مرأ [2/2], وجه [2/2], يوم [4/4], سفر [2/2], كفر [2/2]",
  "gloss (1021): سفر iki anlam (80:15 yazıcılar / 80:38 parlayan); فجر 'fışkırtma; fecir' — 80:42 'fecera' için uymuyor",
  "bağ: kalıp eşleri okumayla (10:26, 70:11, 70:12, 75:22, 75:24, 78:40; ardışık 79:33, 79:34); 88:2, 88:8 henüz okunmadı — bağ yazılmadı",
  "◈K / ◈B: ◈K dolu — 80:34, 37, 38, 40 يوم; ◈B dolu — 80:32 نعم; 80:38-41 'vucûh' (وجه) tetik listesinde değil",
  "çıpa: 80:31-32 L1 olgu=True (bitki zincirinin sonu, yararlanma işlevi); 80:33-42 olgu=False (âhiret); tarayıcı aday vermedi",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 31 sayım 0 uyuşmaz; kayıttan önce 80:42 harekesiz 'ulâ'ike hum' okunmuş / okunmamış sayısı düzeltildi (12 / 7 yazılmıştı, liste 10 / 9)",
 ],
}

DUZELTME = {
}
