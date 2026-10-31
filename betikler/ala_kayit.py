# -*- coding: utf-8 -*-
"""ala_kayit.py — sûre 87 (A'lâ) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 87

CIPA = {
 # blok 1-8
 1: dict(kademe=None, olgu=False, cipa=False, not_="'sebbihi'sme rabbike'l-a'lâ' — emir, tesbih (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe='L1', olgu=True, cipa=False, not_="'ellezî xalaqa fe-sevvâ' — yaratma + düzenleme, 'fe' ile sıralı; nesne, madde, aşama adı ve nedensellik yok — L1 (82:7, 75:38 kayıtları emsali); tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'ve'llezî qaddara fe-hedâ' — ölçü verme + yol gösterme, nesne ve madde adsız, doğal olgu adlanmıyor (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe='L1', olgu=True, cipa=False, not_="'ve'llezî axraca'l-mer'â' — otlak çıkarma süreci; mekanizma / nedensellik yok — L1 (79:31 kaydı emsali); tarayıcı vermedi"),
 5: dict(kademe='L1', olgu=True, cipa=False, not_="'fe-ce'alehû ğuthâ'en ahvâ' — otlak → kararmış çerçöp, 'fe' ile sıralı iki hâl; nedensellik / ölçü yok — L1; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'se-nuqri'uke fe-lâ tensâ' — hitap, vaat (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'illâ mâ şâ'a'llâh, innehû ya'lemu'l-cehra ve mâ yaxfâ' — gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'ve nuyessiruke li'l-yusrâ' — hitap, vaat (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 9-19
 9: dict(kademe=None, olgu=False, cipa=False, not_="'fe-zekkir in nefe'ati'z-zikrâ' — emir (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'se-yezzekkeru men yaxşâ' — insan tutumu (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 11: dict(kademe=None, olgu=False, cipa=False, not_="'ve yetecennebuhe'l-eşqâ' — insan tutumu (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 12: dict(kademe=None, olgu=False, cipa=False, not_="'ellezî yaslâ'n-nâra'l-kubrâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'thumme lâ yemûtu fîhâ ve lâ yahyâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe=None, olgu=False, cipa=False, not_="'qad eflaha men tezekkâ' — insan tutumu (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="'ve zekera'sme rabbihî fe-sallâ' — insan tutumu (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 16: dict(kademe=None, olgu=False, cipa=False, not_="'bel tu'thirûne'l-hayâte'd-dunyâ' — insan tutumu (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 17: dict(kademe=None, olgu=False, cipa=False, not_="'ve'l-âxiratu xayrun ve ebqâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 18: dict(kademe=None, olgu=False, cipa=False, not_="'inne hâzâ le-fi's-suhufi'l-ûlâ' — söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 19: dict(kademe=None, olgu=False, cipa=False, not_="'suhufi ibrâhîme ve mûsâ' — söz / kaynak (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 8): [
  "esmâ: e_oto 0 token; KARAR değişmedi (714); Rab 87:1, lafız 87:7; 'el-a'lâ' esmâ listesinde yok — e_oto vermedi; i'râbı metinde görünmüyor (son harf ى), morph etiketi GEN ('rabb'e bağlı)",
  "kök tablosu: kok_ekle_87 1 kök (حوي 87:5; korpus 2 ayet, iki lemma); 1512 → 1513; retroaktif yama 'daha önce okunmuş 1 ayet' saydı — okunmamış sûrede, kayıt yok, atlandı; hedefli 0, genel 0 (ikinci koşu da 0)",
  "harf alanı: ayet 1 ölçümünde harf 34 → harf3 15, isaret 0 (ayet 1 ailesi; besmele); araç alanı (924)",
  "yıldız: ★★★ 87:1 rab z=5,01 (kısa ayette tek Rab); ★ 87:7 allah z=1,69; ★ 87:6 kaynak 'n' etiketli ama kafiye_kirik True — sahte kırıktan (1001) — formül davranışı",
  "fâsıla (924): 87:6 'tensâ' son harfte medde işareti 'ٓ' sınıfı ve KAFİYE KIRILMASI veriyor — metindeki harf ى; blokta sekiz ayetin sekizi ى",
  "iltifât: 87:2 {2} → {3} ölçümde 1 — 'ellezî' 87:1 Rabbinin sıfatı, hitap eden ve muhatap değişmedi (924); 87:6 {3} → {1, 2}, 87:7 {1, 2} → {3}, 87:8 {3} → {1, 2} gerçek",
  "biçim (924): 87:6 'lâ tensâ' kip NEG (haber; son harf yazılı, morph IND) doğru; 87:7 ISTISNA doğru, 'inne' kip alanında yok",
  "KAPATILAMAZ: 87:7 konuşan 1P ile lafzın aynılığı (metinde işaretli değil); 87:1 'el-a'lâ'nın bağlandığı ad metin harfinden",
  "adsız gönderge (1017): 87:1, 6, 8 muhatap 2MS; 87:6, 8 konuşan 1P",
  "◈B (tetik dışı bitki / renk): 87:4 'el-mer'â', 87:5 'ğuthâ'' ve 'ahvâ' tetik listesinde değil — '—', gözlem ◇'ye",
  "çıpa: 87:2, 4, 5 L1 (yaratma + düzenleme; otlak çıkarma; otlak → çerçöp); 87:3 olgu=False (ölçü + yol, nesne adsız); tarayıcı v4 blokta aday vermedi",
  "esit2 / nakarat3: blokta boş; xref 87:1 → 56:74, 56:96, 69:52 (basıldı)",
  "aday 1040 (kayıt): 86:17 / 87:1 sûre sınırı — 2MS'ye emir ile kapanış / 2MS'ye emir ile açılış; 86 lafızsız ve Rabsız, 87:1 Rab; fâsıla ا → ى",
  "aday 1041 ailesi (okuma, sûreler arası): 'rabb' + 'a'lâ' 79:24 bir kişinin kendisi için iddiası ('qâle' ile işaretli) / 87:1 2MS'nin Rabbi — sûre içi kayıt değil, okuma bağı",
  "bağ: kalıp / lemma eşleri okumayla (56:74, 56:96, 69:52, 55:78, 73:8, 76:25, 79:24, 53:7, 75:38, 82:7, 80:19, 20:50, 79:31, 23:41, 75:17, 75:18, 21:110, 80:20); bütün emsaller sohbette AR + meal ile basıldı",
  "◈K / ◈B: ◈K blokta tetik yok (سمو 'ism' S1 izinli lemma değil); ◈B dolu 87:2 خلق; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 21 sayım, 0 uyuşmaz",
  "süreç: sûre 87 dosyaları tarik_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_87.py, oturum dışı); kapanış / paket blok listesi BLOK_LISTESI_ELLE ile bırakıldı, sûre sonunda üç yerde birlikte doldurulacak",
 ],
 (9, 19): [
  "esmâ: e_oto 2 token — 87:17 'el-âxira' (âhiret) ve 87:18 'el-ûlâ' (sayfaların sıfatı) DEĞİL; KARAR 714 → 716; ölçüm satırı 87:17 'SON konum, MÜHÜRSÜZ', esma_kayit 87:17-18 mühür EVET, karar sonrası geçerli mühür 0 (1022)",
  "kök tablosu: yeni kök yok (1513); retroaktif yama hedefli 0, genel 0",
  "yıldız: ★★★ 87:15 rab z=5,01 (kısa ayette tek Rab); ★ 87:17 kaynak 'n' etiketli ama kafiye_kirik True — sahte kırıktan (1001) — formül davranışı",
  "fâsıla (924): 87:17 'ebqâ' son harfte medde işareti 'ٓ' sınıfı ve KAFİYE KIRILMASI veriyor — metindeki harf ى; 87:16 ا (ى → ا → ى) ölçümde aynı A sınıfı, işaretlenmedi",
  "iltifât: 87:16 {3} → {2} gerçek (2MP); 87:9 {1, 2} → {2, 3} kısmi örtüşme, ölçüm 0 (924) — 1P'den 2MS'ye emre geçiş",
  "biçim (924): 87:9 COND + IMPV, 87:10 FUT, 87:13 NEG 2, 87:14 CERT, 87:16 IDRAB, 87:18 EMPH + DIKKAT doğru; 87:11 'se' yok, kip alanı boş — doğru",
  "KAPATILAMAZ: 87:18 'hâzâ' göndergesi; 87:9 şartın cevabı ayrı fiil olarak yazılmamış",
  "adsız gönderge (1017): 87:9 muhatap 2MS ve emreden; 87:10 'men yaxşâ', 87:11 'el-eşqâ', 87:14 'men tezekkâ' genel; 87:16 muhatap 2MP; 87:19 adlı İbrâhîm, Mûsâ",
  "aday 1041 (kayıt): ilgi zamiri 'ellezî' sûre içi 87:2-4 Rab / 87:12 en bedbaht",
  "esit2: 87:14 BENZER → 91:9 (henüz okunmadı); xref 87:15 → 73:8, 76:25 ve 87:16 → 79:38 (basıldı)",
  "sûre içi tam sayım (bütün geçişler bu oturumda basıldı): ذكر [4/4] (87:9 ×2, 10, 15); سمو, ربب, حيي, صحف, يسر ikişer [2/2]; lafız 1 (87:7), Rab 2 (87:1, 15)",
  "çıpa: blokta merdiven uygulanan ayet yok (11 ayetin 11'i olgu=False); tarayıcı v4 blokta aday vermedi",
  "bağ: kalıp / lemma eşleri okumayla (51:55, 80:4, 84:12, 20:74, 79:18, 73:8, 76:25, 79:38, 42:36, 20:133, 53:36, 53:37); bütün emsaller sohbette AR + meal ile basıldı",
  "◈K / ◈B: ◈K blokta tetik yok (نور 'nâr' tetik listesinde değil); ◈B dolu 87:13 موت حيي, 87:16 حيي; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, sûre geneli 19 / 0; oturum_xy blok 26, sûre geneli 47 sayım, 0 uyuşmaz",
 ],
}

DUZELTME = {
}
