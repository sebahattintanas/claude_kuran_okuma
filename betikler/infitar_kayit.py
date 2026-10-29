# -*- coding: utf-8 -*-
"""infitar_kayit.py — sûre 82 ('İnfitâr) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 82

CIPA = {
 # blok 1-10
 1: dict(kademe='L1', olgu=True, cipa=False, not_="'ize's-semâ'u'nfatarat' — âhirette kozmik olay (gök) — L1; tarayıcı vermedi"),
 2: dict(kademe='L1', olgu=True, cipa=False, not_="'ize'l-kevâkibu'ntetharat' — âhirette kozmik olay (yıldızlar) — L1; tarayıcı vermedi"),
 3: dict(kademe='L1', olgu=True, cipa=False, not_="'ize'l-bihâru fuccirat' — âhirette kozmik olay (denizler) — L1; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'ize'l-qubûru bu'thirat' — âhiret, insan yapımı yer (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="''alimet nefsun mâ qaddemet ve axxarat' — âhiret, şart cevabı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'yâ eyyuhe'l-insânu mâ ğarraka bi-rabbike'l-kerîm' — hitap (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe='L1', olgu=True, cipa=False, not_="'ellezî xalaqaka fe-sevvâke fe-'adelek' — yaratma + düzenleme + dengeleme, 'fe' ile sıralı, aşama adı ve nedensellik yok — L1 (75:38 kaydı emsali); tarayıcı vermedi"),
 8: dict(kademe='L1', olgu=True, cipa=False, not_="'fî eyyi sûratin mâ şâ'e rakkebek' — biçim + oluşturma, nedensellik yok — L1; tarayıcı vermedi"),
 9: dict(kademe=None, olgu=False, cipa=False, not_="'kellâ bel tukezzibûne bi'd-dîn' — yargı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'ve inne 'aleykum le-hâfizîn' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 11-19
 11: dict(kademe=None, olgu=False, cipa=False, not_="'kirâmen kâtibîn' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 12: dict(kademe=None, olgu=False, cipa=False, not_="'ya'lemûne mâ tef'alûn' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'inne'l-ebrâra le-fî na'îm' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe=None, olgu=False, cipa=False, not_="'ve inne'l-fuccâra le-fî cahîm' — âhiret, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="'yaslevnehâ yevme'd-dîn' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 16: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ hum 'anhâ bi-ğâ'ibîn' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 17: dict(kademe=None, olgu=False, cipa=False, not_="'ve mâ edrâke mâ yevmu'd-dîn' — soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 18: dict(kademe=None, olgu=False, cipa=False, not_="'thumme mâ edrâke mâ yevmu'd-dîn' — soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 19: dict(kademe=None, olgu=False, cipa=False, not_="'yevme lâ temliku nefsun li-nefsin şey'â …' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: e_oto 1 token (82:6 'kerîm') — karar İLÂHÎ ('rabbike'l-kerîm'); KARAR 696 → 697; ölçüm satırı 'SON konum, MÜHÜRSÜZ' — mühür iddiası bilançodan (1022); 82:6 sûrenin ilk Rab'ı",
  "kök tablosu: kok_ekle_82 1 kök (بعثر 82:4; 2 ayet, öbürü henüz okunmadı); 1504 → 1505; retroaktif yama hedefli 0, genel 0 (ikinci koşu da 0); hapaks yıldızı yok",
  "harf alanı: ayet 1 ölçümünde harf 34 → harf3 15, isaret 0 (ayet 1 ailesi; besmele); araç alanı (924)",
  "yıldız: ★★★ 3 — 82:3, 4 pas z=5,38 (kısa tek fiilli edilgen); 82:6 rab z=3,23 (lafızsız kısa ayette Rab) — formül davranışı; 82:1, 2 VII. / VIII. bab, edilgen değil",
  "biçim / kip (924): 'izâ' şart zarfı ve şart cevabı (82:5) kip alanında yok; 82:6 'mâ' sorusu kip alanında yok (yalnız VOC); 82:8 'mâ şâ'e' ölçümde COND — şart / mevsûl KAPATILAMAZ",
  "ölçüm iltifât (924): 82:8 → 9 2MS → 2MP, sahset ikisinde de ['2'] — tekil / çoğul ayrılmıyor, iltifât 0",
  "fâsıla: 82:1-5 ت, 82:6 م, 82:7-8 ك, 82:9-10 ن — ölçüm sınıf geçişlerini kırık olarak işaretlemedi (924)",
  "adsız gönderge (1017): edilgen failler (82:3, 4); 82:6 'el-insân' (cins) ve konuşan; 82:7-8 yaratan 3MS (82:6 Rab'a bağlı sıfat cümlesi); 82:9 muhataplar 2MP; 82:10 'hâfizîn'",
  "okuma ikiliği: 82:5 'nefsun' (her can / bir can); 82:8 'mâ' (şart / mevsûl) KAPATILAMAZ",
  "lemma eşsesli: ''adele' listesi dengeleme / adalet / sapma anlamlarını birleştiriyor — lemma sayısı verilmedi",
  "aday 1040 (kayıt): 81:29 / 82:1 sûre sınırı — lafız + Rab + hasr ile kapanış / lafızsız şart zarfı ile açılış; fâsıla ن → ت; ardışık sûrede yapı eşleşmesi: 've izâ' + ad + fiil şart dizisi ve ''alimet nefsun mâ …' cevabı (81:1-14 / 82:1-5); harekesiz 've ize'l-bihâr' korpusun iki ayeti 81:6 / 82:3",
  "aday 1040 ailesi (okuma): 81:11 / 82:1 'ize's-semâ''; 81:2 / 82:2 yıldız adı + dönüşlü fiil; 81:19 / 82:6 'kerîm' elçi / Rab",
  "bağ: kalıp / lemma eşleri okumayla (73:18, 37:6, 54:12, 75:13, 31:33, 75:38, 18:37, 40:64, 64:3, 74:53); 84:1, 84:6 henüz okunmadı — bağ yazılmadı",
  "◈K / ◈B: ◈K dolu 82:1 سمو ('semâ'', S1 izinli), 82:2 كوكب, 82:3 بحر; ◈B dolu 82:6 أنس, 82:7 خلق; tetik ön kuru koşu 0 uyuşmaz",
  "süreç: sûre 82 dosyaları tekvir_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_82.py, oturum dışı); oturum_xy 28 sayım 0 uyuşmaz; kayıttan önce düzelttiğim: 82:7 ''adele' eşsesli lemma sayısı çıkarıldı",
 ],
 (11, 19): [
  "esmâ: e_oto 2 token (82:11 'kirâm' — yazıcıların sıfatı; 82:13 'berr' — insan çoğulu 'el-ebrâr') — ikisi de DEĞİL; KARAR 697 → 699; ölçüm satırı 'SON konum, MÜHÜRSÜZ' — mühür iddiası bilançodan (1022)",
  "lafız / Rab: sûrenin tek lafzı 82:19 son kelime (★ lafız z=1,69 — formül davranışı); sûre bütünü Rab 1 (82:6), lafız 1 (82:19)",
  "kök tablosu: yeni kök yok (1505); retroaktif yama hedefli 0, genel 0",
  "nakarat: 82:17-18 've / thumme mâ edrâke mâ yevmu'd-dîn' — ölçüm nakarat3 (5 kelime / 2 ayet) ve esit2 BENZER ikisinde görünüyor",
  "biçim (924): 82:19 'li'llâh' takdimiyle hasr anlamı biçim alanında yok (okuma); 82:15-16 3FS zamirin göndergesi (cahîm) ölçümde yok, okumayla",
  "gloss (1021): kök برر 'iyilik; kara' — 'ebrâr' lemma listesi eşsesli birleşme içeriyor (lemma sayısı verilmedi); kök فجر 82:3 'fuccirat' / 82:14 'fuccâr'; kök شيأ 82:8 'şâ'e' / 82:19 'şey''",
  "adsız gönderge (1017): 82:11-12 yazıcılar; 82:17-18 muhatap 2MS (82:6 'el-insân' ile aynılığı metinde işaretli değil); konuşan sûre boyu adsız",
  "fâsıla: 82:11-12 ن, 82:13-14 م, 82:15-18 ن, 82:19 ه — ölçüm N ve H sınıfı; geçişler kırık işaretlenmedi (924)",
  "aday 1041 (kayıt): kök كرم — 82:6 'rabbike'l-kerîm' (İLÂHÎ) / 82:11 'kirâmen kâtibîn' (yazıcılar)",
  "aday 1040 ailesi (okuma): ardışık iki sûre de lafızla biten ayetle kapanıyor (81:29 / 82:19); 82:19 → 83:1 sınırı 83:1 okunurken",
  "bağ: kalıp / lemma eşleri okumayla (80:16, 76:5, 38:28, 80:42, 1:4, 69:3, 77:14, 81:29); 83:22 (esit2 TAM), 83:7, 83:11, 2:48, 2:123 (xref) henüz okunmadı — bağ yazılmadı",
  "◈K / ◈B: ◈K dolu 82:15, 17, 18, 19 يوم; ◈B tetik yok (82:13 نعم 'na'îm' S1 izinli lemma değil)",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, sûre geneli 19 / 0; oturum_xy 24 sayım 0 (sûre geneli 52 / 0); kayıttan önce düzelttiğim yok",
 ],
}

DUZELTME = {
}
