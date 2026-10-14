# -*- coding: utf-8 -*-
"""casiye_kayit.py — sûre 45 (Câsiye) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 45

CIPA = {
 # blok 1-10
 3: dict(kademe='L0', olgu=True, cipa=False, not_="gökler ve yer âyetlerin yeri olarak adlı; süreç/ölçü yok — L0; tarayıcı vermedi"),
 4: dict(kademe='L1', olgu=True, cipa=False, not_="insanın yaratılışı + yayılan canlılar ('mâ yebussu min dâbbe'): canlı sınıfı + eylem, aşama/mekanizma yok — L1 (42:29 emsali); tarayıcı vermedi"),
 5: dict(kademe='L2', olgu=True, cipa=False, not_="gökten indirilen rızık → onunla ('bihî') ölü yerin diriltilmesi: nedensel bağ adlı (16:65, 30:24, 35:9 emsali); gece-gündüz 'ihtilâf'ı ve rüzgârların 'tasrîf'i adlandırma; mekanizma/ölçü yok — L2; tarayıcı vermedi"),
 # blok 11-20
 12: dict(kademe='L1', olgu=True, cipa=False, not_="deniz boyun eğdirme + gemilerin 'bi-emrihî' akışı; ta'lîl ('li-') insan ihtiyacına (lütuf arama, şükür) — işlev, doğal olgu içi nedensellik yok — L1 (40:80, 43:13 emsali); 'fulk' gemi, kozmik öğe değil (S2 açık); tarayıcı v4 adayı, çıpa değil"),
 13: dict(kademe='L1', olgu=True, cipa=False, not_="göklerde ve yerde olanların hepsinin boyun eğdirilmesi: öğe + işlev, süreç/ölçü yok — L1 (31:20 emsali); tarayıcı vermedi"),
 # blok 21-30
 22: dict(kademe='L0', olgu=True, cipa=False, not_="gökler ve yer 'bi'l-haqq' yaratılan olarak; ta'lîl ('li-tuczâ') karşılığa, doğal süreç/ölçü yok — L0 (44:38-39 emsali); tarayıcı v4 adayı, çıpa değil"),
 24: dict(kademe='L0', olgu=False, cipa=False, not_="'dehr' helâk edici olarak söyleyenlerin sözü içinde (alıntı); olgu iddiası anlatıcının değil; birim/süreç yok — L0; tarayıcı vermedi"),
 # blok 31-37
 36: dict(kademe='L0', olgu=True, cipa=False, not_="gökler ve yer Rab tamlamasında (44:7, 26:24 emsali); süreç yok — L0; tarayıcı vermedi"),
 37: dict(kademe='L0', olgu=True, cipa=False, not_="gökler ve yer büyüklüğün yeri olarak; süreç/ölçü yok — L0; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ (1022 ailesi): 45:3 'mu'min' (inananlar), 45:10 'evliyâ'' (edinilen dostlar) ölçüm MÜHÜRSÜZ / esma_kayit mühür EVET — değil; 45:2 'azîz' + 'hakîm' lafzın sıfatı, ilâhî — bilanço geçerli mühür listesi boş (esma_muhur_43 [2, 3, 10], geçerli [])",
  "aday 1040 alanı: 44:59 → 45:1 sûre sınırı; 44:44 'ta'âmu'l-esîm' → 45:7 'effâkin esîm' — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 45:4 'yebussu' öznesi 3MS adsız; 45:4 2MP → 3MP, 45:6 1P/2MS → 3MP, 45:9 3MS → 3MP 'ulâike' ölçüm iltifât 0; 45:8 okuyan (edilgen 'tutlâ') ve muhatap 2MS adsız",
  "biçim (517 ailesi): 45:8 'ke-en' benzetmesi, 45:9 'izâ' şart ölçümde işaretsiz",
  "gloss (1021 ailesi): روح 45:5 rüzgâr",
  "okuma: 31:6-7 → 45:8-9 aynı iki unsur ters sırada; 2:164 (henüz okunmadı) 45:4-5'in dört lemma dizisinde de var — KAPATILAMAZ",
  'tetik: ilk koşuda 0 uyuşmaz (45:3 سمو/أرض; 45:4 خلق/دبب; 45:5 ليل/نهر/سمو/أرض/روح + حيي/موت; 45:8 سمع)',
 ],
 (11, 20): [
  "esmâ (1022 ailesi): 45:19 'evliyâ'' (zâlimler) değil / 'veliyy' (lafzın haberi) ilâhî — ölçüm ikisi de MÜHÜRSÜZ, esma_kayit mühür EVET; bilanço geçerli mühür []",
  "aday 1041 alanı: 'veliyy' 45:19 aynı ayette zâlimlerin birbirine ('evliyâ'') ve Allah'ın takvâ sahiplerine; 45:10 'evliyâ'' edinilen dostlar; 9:71 mü'minler birbirinin 'evliyâ''ı — kayıt, test yok",
  "aday 1040 alanı: 44:32 Benî İsrâîl 'ale'l-âlemîn' → 45:16 'faddalnâhum ale'l-âlemîn'; 44:4-5 'emr' → 45:17-18 'mine'l-emr' — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 45:11, 45:20 'hâzâ' göndergesi adsız; 45:14 'li-yecziye' öznesi 3MS adsız; 45:14, 18, 19 muhatap 2MS adsız; 45:12 3MS → 2MP, 45:15 3MS → 2MP, 45:17 1P → 3MP → 2MS ölçüm iltifât 0",
  "biçim (517 ailesi): 45:12 ta'lîl 'li-', 45:15 şart 'men', 45:19 tekit ölçümde işaretsiz",
  "gloss (1021 ailesi): بغي 45:12 arama / 45:17 azgınlık; شرع 45:18 'şerî'a'",
  "okuma: 10:93 → 45:16-17 (Benî İsrâîl, 'razaqnâhum mine't-tayyibât', ilim geldikten sonra ayrılık, aynı kapanış cümlesi); 42:14 → 45:17 ('illâ min ba'di mâ câehumu'l-ilmu bağyen beynehum') — KAPATILAMAZ",
  "oturum notu: kayıttan önce 45:14'teki 'eyyâm + Allah' sayım ifadesi düzeltildi (lemma dizisi 'yevm + Allah'; 40:16 terkip değil)",
  'tetik: ilk koşuda 0 uyuşmaz (45:12 بحر/فلك; 45:13 سمو/أرض; 45:14, 17 يوم; 45:20 بصر/أنس)',
 ],
 (21, 30): [
  "esmâ (1022 ailesi): 45:30 'mubîn' (kurtuluşun sıfatı) ölçüm MÜHÜRSÜZ / esma_kayit mühür EVET — değil",
  "aday 1040 alanı: 44:35-36 → 45:24-25 ('in/mâ hiye illâ …' + ''tû bi-âbâinâ in kuntum sâdiqîn', xref ölçüm); 44:57 'el-fevzu'l-azîm' → 45:30 'el-fevzu'l-mubîn' — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 45:24-25 söyleyenler 3MP adsız; 45:28 'el-yevme tuczevne' ve 45:29 1P konuşan adsız, alıntı sınırı işaretsiz; 45:23 2MS → 2MP, 45:28 2MS → 3FS → 2MP ölçüm iltifât 0",
  "biçim (517 ailesi): 45:21 'em' sorusu ve 'sâe' zem fiili, 45:22 ta'lîl, 45:29 tekit ölçümde işaretsiz",
  "okuma: 2:7 → 45:23 (mühür, üç organ, 'ğışâve'; sıra ve sayı farklı); 23:37 + 43:20 → 45:24; 23:62 → 45:22 + 45:29 — KAPATILAMAZ",
  "sûre adı: 'câsiye' lemma korpusta 1, yalnız 45:28",
  "oturum notu: kayıttan önce 45:27 lemma dizisi ifadesi açık yazıldı",
  'tetik: ilk koşuda 0 uyuşmaz (45:21 حيي/موت; 45:22 سمو/أرض + خلق; 45:23 سمع/قلب/بصر; 45:24 دهر + حيي/موت; 45:26 يوم + حيي/موت/أنس; 45:27 سمو/أرض/يوم/سوع; 45:28 يوم)',
 ],
 (31, 37): [
  "esmâ (1022 ailesi): 45:37 'azîz' + 'hakîm' (zamir 'huve', 45:36 lafız) ilâhî — ölçüm SON MÜHÜR, esma_kayit ÇİFT; bilanço geçerli mühür listesi boş (esma_muhur_43 [37], geçerli [])",
  "aday 1041 alanı: 'kibriyâ'' 10:78 (Firavun'un ileri gelenlerinin Mûsâ ve Hârûn'a isnadı) / 45:37 (O'nun) — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 45:31 1S konuşan ('âyâtî') adsız (23:105 aynı); 45:32, 34 'qîle' söyleyen adsız; 45:34 1P 'nensâkum' adsız; 45:35 2MP → 3MP alıntı sınırı işaretsiz; ölçüm iltifât 0",
  "biçim (517 ailesi): 45:32 tekit 'inne', 45:34 'kemâ' ölçümde işaretsiz",
  "gloss (1021 ailesi): نور 45:34 ateş ('en-nâr')",
  "okuma: 45:2 → 45:37 'el-azîz el-hakîm' sûrenin ikinci ve son ayeti; 45:30-31 'emmâ' taksimi; 32:14 → 45:34 (karşılıklı unutma, sıra ters); 39:48 + 16:34 → 45:33 — KAPATILAMAZ",
  'tetik: ilk koşuda 0 uyuşmaz (45:32 سوع; 45:34, 35 يوم; 45:35 حيي; 45:36, 37 سمو/أرض)',
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_45.py uygular)
DUZELTME = {
 37: dict(alan='mercek', eski="okuyucu kararı ilâhî; bilanço geçerli mühür listesi boş (1022).",
          dogru="Bilanço iddiası okuyucu kararı eklenmeden ÖNCE koşulan bilançodan yazılmıştı. Kayıtlı bilanço (karar sonrası) 45:37'yi geçerli mühür sayıyor (31-37: esma_muhur_43 [37], geçerli [37]). Aynı yanlış iddia blok ARIZA kayıtlarında 45:2 (1-10: geçerli [2]) ve 45:19 (11-20: geçerli [19]) için de var; sûre profili: mühür 6, geçerli 3 (2, 19, 37), yanlış 3 (3, 10, 30). Özgün alan korunur.",
          aday=1022, blok='31-37'),
}
