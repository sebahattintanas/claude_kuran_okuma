# -*- coding: utf-8 -*-
"""fecr_kayit.py — sûre 89 (Fecr) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 89

CIPA = {
 # blok 1-14
 1: dict(kademe='L0', olgu=True, cipa=False, not_="'ve'l-fecr' — yemin edilen adlı zaman; süreç / ölçü yok — L0; tarayıcı vermedi"),
 2: dict(kademe='L0', olgu=True, cipa=False, not_="'ve leyâlin 'aşr' — yemin edilen zaman (gece) + sayı; hangi geceler adsız; süreç / ölçü yok — L0; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'ve'ş-şef'i ve'l-vetr' — gönderge adsız (çift / tek); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe='L0', olgu=True, cipa=False, not_="'ve'l-leyli izâ yesr' — yemin edilen adlı zaman + hareket fiili; mekanizma yok — L0 (81:17 kaydı emsali); tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'hel fî zâlike qasemun li-zî hicr' — soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'e-lem tera keyfe fe'ale rabbuke bi-'âd' — tarihsel olay, kavim (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'irame zâti'l-'imâd' — insan yapımı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'elletî lem yuxlaq mithluhâ fi'l-bilâd' — insan yapımı / kavim (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 9: dict(kademe=None, olgu=False, cipa=False, not_="'ve themûde'llezîne câbu's-saxra bi'l-vâd' — insan yapımı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'ve fir'avne zi'l-evtâd' — kişi (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 11: dict(kademe=None, olgu=False, cipa=False, not_="'ellezîne tağav fi'l-bilâd' — insan tutumu (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 12: dict(kademe=None, olgu=False, cipa=False, not_="'fe-ekthrû fîhe'l-fesâd' — insan tutumu (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'fe-sabbe 'aleyhim rabbuke sevta 'azâb' — azap, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe=None, olgu=False, cipa=False, not_="'inne rabbeke le-bi'l-mirsâd' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 15-20
 15: dict(kademe=None, olgu=False, cipa=False, not_="'fe-emme'l-insânu izâ me'btelâhu rabbuhû …' — insan tutumu, sınama (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 16: dict(kademe=None, olgu=False, cipa=False, not_="'ve emmâ izâ me'btelâhu fe-qadera 'aleyhi rizqahû …' — insan tutumu, sınama (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 17: dict(kademe=None, olgu=False, cipa=False, not_="'kellâ bel lâ tukrimûne'l-yetîm' — insan tutumu (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 18: dict(kademe=None, olgu=False, cipa=False, not_="'ve lâ tehâddûne 'alâ ta'âmi'l-miskîn' — insan tutumu (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 19: dict(kademe=None, olgu=False, cipa=False, not_="'ve te'kulûne't-turâthe eklen lemmâ' — insan tutumu (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 20: dict(kademe=None, olgu=False, cipa=False, not_="'ve tuhibbûne'l-mâle hubben cemmâ' — insan tutumu (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 21-30
 21: dict(kademe=None, olgu=False, cipa=False, not_="'kellâ izâ dukketi'l-ardu dakkan dakkâ' — âhiret sahnesi, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 22: dict(kademe=None, olgu=False, cipa=False, not_="'ve câ'e rabbuke ve'l-meleku saffen saffâ' — âhiret sahnesi, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 23: dict(kademe=None, olgu=False, cipa=False, not_="'ve cî'e yevme'izin bi-cehennem …' — âhiret sahnesi, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 24: dict(kademe=None, olgu=False, cipa=False, not_="'yeqûlu yâ leytenî qaddemtu li-hayâtî' — âhiret sahnesi, söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 25: dict(kademe=None, olgu=False, cipa=False, not_="'fe-yevme'izin lâ yu'azzibu 'azâbehû ehad' — âhiret, azap (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 26: dict(kademe=None, olgu=False, cipa=False, not_="'ve lâ yûthiqu vethâqahû ehad' — âhiret, azap (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 27: dict(kademe=None, olgu=False, cipa=False, not_="'yâ eyyetuhe'n-nefsu'l-mutma'inne' — hitap, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 28: dict(kademe=None, olgu=False, cipa=False, not_="'irci'î ilâ rabbiki râdıyeten merdıyye' — hitap, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 29: dict(kademe=None, olgu=False, cipa=False, not_="'fe'dxulî fî 'ibâdî' — hitap, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 30: dict(kademe=None, olgu=False, cipa=False, not_="'ve'dxulî cennetî' — hitap, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 14): [
  "esmâ: e_oto 0 token; KARAR değişmedi (716); Rab 3 (89:6, 13, 14), lafız yok",
  "kök tablosu: kok_ekle_89 1 kök (سوط 89:13; korpusta tek ayet); 1517 → 1518; retroaktif yama hedefli 0, genel 0 (ikinci koşu da 0)",
  "harf alanı: ayet 1 ölçümünde harf 25 → harf3 6, isaret 0 (ayet 1 ailesi; besmele); araç alanı (924)",
  "yıldız: ★★★ 89:6 rab z=3,23, 89:13 rab z=3,94 (hapaks 3,28 ve kafiye_kirik da var), 89:14 rab z=6,78, 89:8 pas z=5,38 — formül davranışı",
  "fâsıla: 89:1-5 ر, 89:6-12 د, 89:13 ب, 89:14 د; ölçüm 89:13 KAFİYE KIRILMASI doğru (gerçek); ر → د geçişi (89:5 → 6) işaretlenmedi (924)",
  "biçim (924): 89:2-4 atıflı yeminlerde QASEM yok; 89:5 QASEM 'qasem' adından — yanlış pozitif (yemin değil, soru); 89:12 sayı işareti 'ekthere' yanlış pozitif; 89:2 ''aşr' gerçek sayı",
  "KAPATILAMAZ: 89:1-4 yemin dizisinin cevabı (89:14 okunabilir, işaret yok); 89:2 on gecenin hangileri olduğu; 89:3 çift / tekin göndergesi",
  "adsız gönderge (1017): 89:1-4 yemin eden; 89:6, 13, 14 muhatap 2MS; 89:8 yaratan (edilgen); 89:5 akıl sahibi (nekre)",
  "gloss (1021): kök عود 'geri dönme' — özel ad ''Âd' (özel ad iskeleti çakışması, bekleyen karar ailesi); kök جوب 'cevap verme' — 'câbû' (oydular) uymuyor; kök حجر — 'hicr' (akıl) uymuyor",
  "lemma (eşsesli): 'hicr' morph'ta akıl / engel / yer adı geçişlerini birleştiriyor — lemma sayısı verilmedi",
  "◈K (tetik dışı zaman): 89:1 'el-fecr' (kök فجر) tetik listesinde değil — '—', gözlem ◇'ye; ◈K dolu 89:2, 4 ليل; ◈B dolu 89:8 خلق (canlı oluşumu değil)",
  "çıpa: L0 3 (89:1 fecir, 89:2 on gece, 89:4 gece — yemin edilen zaman); 89:3 gönderge adsız; 89:6-14 olgu=False (kavim, insan yapımı, azap); tarayıcı v4 blokta aday vermedi",
  "esit2 / nakarat3: blokta boş; xref 89:6 → 105:1 (henüz okunmadı)",
  "aday 1040 (kayıt): 88:26 / 89:1 sûre sınırı — 1P konuşanın hesap sözü ile kapanış / yemin ile açılış; fâsıla م → ر; 88'de Rab yok, 89 Rab ile devam ediyor (89:6)",
  "bağ: kalıp / lemma eşleri okumayla (81:17, 56:76, 38:12, 78:7, 80:25, 44:48, 78:21); bütün emsaller sohbette AR + meal ile basıldı",
  "◈K / ◈B: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 32 sayım, 0 uyuşmaz",
  "süreç: sûre 89 dosyaları gasiye_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_89.py, oturum dışı); blok sınırı sûrenin bölümlerine göre (1-14 yeminler + kavimler + Rab gözetlemede; 14 kısa ayet tek blok); taban 75699c1 değişmedi — sûre 89 zip'i 87-88'i de taşıyacak",
 ],
 (15, 20): [
  "esmâ: e_oto 0 token; KARAR değişmedi (716); Rab 3 (89:15 iki — anlatıcı sesinde ve insanın sözünde; 89:16 insanın sözünde)",
  "kök tablosu: yeni kök yok (1518); retroaktif yama hedefli 0, genel 0",
  "yıldız: ★★★ 89:15 rab z=3,55; ★ 89:16 rab z=1,81; ★★★ 89:20 hapaks z=3,28 (جمم korpusta tek ayet) — formül davranışı",
  "fâsıla (924): 89:15-16 ن, 89:17 م, 89:18 ن (ölçüm N sınıfı), 89:19-20 ا; د → ن ve ن → ا geçişleri kafiye kırığı işaretlenmedi",
  "iltifât: 89:15 {2} → {1, 3} (2MS hitaptan insan anlatımına; 1S yalnız alıntı içinde), 89:17 {1, 3} → {2} (2MP hitap) gerçek",
  "biçim (924): 89:15-16 AMMA, 89:17 KELLA + IDRAB + NEG, 89:18 NEG doğru; 89:19-20 fiil + aynı kökten mastar (mef'ûl mutlak) — mm2 boş, kök ikilemesi veriyor; nakarat3 89:15-16 sûre içi, süzgeç GEÇMEZ",
  "alıntı: 89:15-16 'fe-yeqûlu' ('qâle' lemması) ile işaretli söz, ayet sonunda metin kapatıyor — meal tırnaklı",
  "adsız gönderge (1017): 89:15-16 insan (genel); 89:16 sınayan yazılmamış (89:15 Rab, okuma); 89:17-20 muhatap 2MP",
  "aday 1041 (kayıt): kök كرم 89:15 Rab ikram eder (iki geçiş) / 89:17 2MP yetime ikram etmez",
  "gloss (1021): kök جمم gloss'u bir dikey komşuluk araç notunu taşıyor ('— دكك dikey komşuluğunda karşılıksız çıktı') — gloss dizgesinde araç notu; değiştirilmedi",
  "esit2: 89:18 BENZER → 69:34 (basıldı), 107:3 (henüz okunmadı)",
  "çıpa: blokta merdiven uygulanan ayet yok (6 ayetin 6'sı insan tutumu, olgu=False); tarayıcı v4 blokta aday vermedi",
  "bağ: kalıp / lemma eşleri okumayla (76:2, 12:21, 22:18, 74:53, 69:34, 76:8); bütün emsaller sohbette AR + meal ile basıldı",
  "◈K / ◈B: ◈K tetik yok; ◈B dolu 89:15 أنس; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 1-20 toplam 20 / 0; oturum_xy blok 23, 1-20 toplam 55 sayım, 0 uyuşmaz",
 ],
 (21, 30): [
  "esmâ: e_oto 2 token (89:25:5, 89:26:4 'ehad' — olumsuz cümlede 'hiç kimse'); esma_el_ekle ile 'degil' (yamalar/esma_el_89_21_30.txt; KARAR 716 → 718); bilançoda esma_muhur_43 [25, 26], geçerli mühür []; Rab 2 (89:22, 28); sûre Rab toplamı 8 (89:6, 13, 14, 15 iki, 16, 22, 28); lafız sûrede yok",
  "kök tablosu: yeni kök yok (1518); retroaktif yama hedefli 0, genel 0",
  "süreç (89:15-20'den devreden not): o bloğun kaydından sonraki genel retroaktif gloss geçişi 89:20 kaydının kendi iki alanını (olcum, mercek) yamaladı — kök جمم gloss'u kök biçimi دكك'i içerdiği için ikinci gloss geçişi gloss'u iç içe yazdı; taban kayıtları değişmedi (git HEAD okuma_metni ile karşılaştırıldı), ikinci koşu 0; 89:20 kaydına dokunulmadı, protokol gereği bu bloğun ARIZA'sına yazıldı (1021)",
  "yıldız: ★★★ 89:21 pas z=5,38; ★★★ 89:22 rab z=3,94; ★★ 89:23 pas z=2,52; ★★★ 89:28 rab z=3,94 — formül davranışı",
  "fâsıla (924): 89:21-22 ا, 89:23-24 ى, 89:25-26 د, 89:27-28 ة, 89:29-30 ى; ikişerli geçişlerin hiçbiri kafiye kırığı olarak işaretlenmedi",
  "iltifât: 89:21 {2} → {3} (2MP hitaptan anlatıma) gerçek; 89:28 2FS hitap gerçek; 89:29-30 konuşan 1S — ölçüm iltifât 0 (89:28'de Rab 2FS zamirle, okuma)",
  "biçim (924): 89:21 fiil + aynı mastar iki kez — mm2 boş, kök ikilemesi veriyor; 89:25-26 mm2 doğru; 89:25-26 sayı işareti 'ehad' yanlış pozitif ('hiç kimse'); 89:27 DIKKAT + VOC doğru",
  "alıntı: 89:24 'yeqûlu' ('qâle' lemması) ile işaretli söz, ayet sonunda kapanıyor — meal tırnaklı; 89:27-30 söz işareti yok — tırnaksız",
  "adsız gönderge (1017): 89:21 fail (edilgen); 89:22 muhatap 2MS; 89:23 getiren (edilgen); 89:24 'yeqûlu' öznesi yazılmamış (89:23 insan, okuma); 89:27-30 konuşan adsız (89:29-30 1S)",
  "KAPATILAMAZ: 89:25-26 'azâbehû' / 'vethâqahû' 3MS zamir göndergesi (en yakın 3MS ad 89:23 insan, öncesinde 89:22 Rab) — meal 'onun' ile açık bıraktı",
  "esit2 / nakarat3: blokta boş; xref 89:23 → 79:35 (basıldı)",
  "çıpa: blokta merdiven uygulanan ayet yok (10 ayetin 10'u olgu=False: âhiret sahnesi, söz, azap, hitap); tarayıcı v4 blokta aday vermedi",
  "aday 1041: blokta yeni kayıt yok — lemma 'câ'e' 89:22 Rab (etken) / 89:23 cehennem (edilgen), insan değil",
  "bağ: kalıp / lemma eşleri okumayla (69:14, 75:26, 78:38, 79:35, 69:25, 78:40, 47:4, 16:112, 69:21, 88:9, 75:30); bütün emsaller sohbette AR + meal ile basıldı",
  "◈K / ◈B: ◈K dolu 89:21 أرض, 89:23 ve 89:25 يوم; ◈B dolu 89:23 أنس, 89:24 حيي; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 1-30 toplam 30 / 0; oturum_xy blok 32, 1-30 toplam 87 sayım, 0 uyuşmaz",
 ],
}

DUZELTME = {
}
