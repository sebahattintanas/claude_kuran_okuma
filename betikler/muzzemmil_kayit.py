# -*- coding: utf-8 -*-
"""muzzemmil_kayit.py — sûre 73 (Müzzemmil) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 73

CIPA = {
 # blok 1-10
 2: dict(kademe='L0', olgu=True, cipa=False, not_="'qumi'l-leyle illâ qalîlâ' — gece yalnız zaman olarak adlanıyor; süreç / ölçü yok — L0; tarayıcı vermedi"),
 3: dict(kademe='L1', olgu=True, cipa=False, not_="'nisfehû evi'nqus minhu qalîlâ' — gecenin süresi kesirle (yarı, biraz eksik); birim yok — L1, KAPATILAMAZ; tarayıcı v4 adayı (F_ölçü), çıpa değil"),
 6: dict(kademe='L0', olgu=True, cipa=False, not_="'nâşi'ete'l-leyl' — gece kalkışı; gece zaman adı, süreç / ölçü yok — L0; tarayıcı vermedi"),
 7: dict(kademe='L0', olgu=True, cipa=False, not_="'fi'n-nehâri sebhan tavîlâ' — gündüz zaman adı; L0; tarayıcı vermedi"),
 9: dict(kademe='L0', olgu=True, cipa=False, not_="'rabbu'l-meşriqi ve'l-mağrib' — doğu / batı tekil, rubûbiyet tamlaması; sayı / ölçü yok — L0 (70:40 çoğul L0, 55:17 ikil L1 emsali); tarayıcı vermedi"),
 # blok 11-19
 12: dict(kademe=None, olgu=False, cipa=False, not_="'enkâlen ve cahîmâ' — cehennem, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'ta'âmen zâ ğussa ve 'azâben elîmâ' — cehennem yiyeceği ve azap, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe='L1', olgu=True, cipa=False, not_="'tercufu'l-ardu ve'l-cibâl … kesîben mehîlâ' — âhirette kozmik olay (yer, dağlar); süreç adı, mekanizma / ölçü yok — L1 (69:14 ailesi); tarayıcı vermedi"),
 17: dict(kademe=None, olgu=False, cipa=False, not_="'yevmen yec'alu'l-vildâne şîbâ' — âhiret / gaybî olay (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 18: dict(kademe='L1', olgu=True, cipa=False, not_="'es-semâ'u munfatirun bihî' — âhirette kozmik olay (gök yarılması); mekanizma / ölçü yok — L1; tarayıcı vermedi"),
 # blok 20-20
 20: dict(kademe='L1', olgu=True, cipa=False, not_="'Allâhu yuqaddiru'l-leyle ve'n-nehâr' — ölçü fiili (taqdîr) + gece / gündüz, birim yok; kesirler (üçte iki, yarı, üçte bir) insanın kalkış süresini ölçüyor, doğal olgunun ölçüsü değil; 'len tuhsûhu' insan sayımının sınırı — L1, KAPATILAMAZ (36:39 L1 emsali); tarayıcı v4 adayı, çıpa değil"),
}

ARIZA = {
 (1, 10): [
  "esmâ: e_oto 1 token (73:9 'vekîl' — zamir Rab'a döner, 39:62 kuralı); İLÂHÎ; KARAR 670 → 671; esma_kayit geçerli mühür [9] — ölçüm satırı 'SON konum, MÜHÜRSÜZ' yazıyor, bilanço geçerli mühür veriyor (ayrışma, 1022 ailesi; araç alanı)",
  "kök tablosu: kok_ekle_73 3 kök (زمل 73:1, نصف 73:3, بتل 73:8; blok_dikey 'KARŞILIK YOK' → eklendi); 1458 → 1461; retroaktif yama: hedef sûre listesi 5 ayet (sûre 2, 4 — ayet kaydı yok), hedefli yama 0; genel geçiş 1 (30:4 mercek alanında daha önce karşılıksız anılan نصف kesir listesinde — gloss eklendi; ikinci koşu 0)",
  "hapaks (yeni kök dersi): 73:1 زمل ve 73:8 بتل ★★★ hapaks z=3,28 — yeni kökün tek ayeti; içerik iddiası değil",
  "yıldız (924): 73:8 rab z=3,23 eşik üstü, 73:9 ★★ rab z=2,05 — içerik iddiası değil; 73:2-7, 10 yıldızsız",
  "harf alanı: ayet 1 ölçümünde harf 30 → harf3 11, isaret 0 (ayet 1 ailesi; besmele); araç alanı (924); KAPATILAMAZ",
  "fâsıla: 73:1 ل → 73:2-10 ا; ölçüm kafiye kırığı 0 — işaretsiz geçiş (araç alanı, 924); 72 sûresinin ا dizisi 73:1'de kesiliyor",
  "sayı işareti: 73:2, 73:3 'qalîl' nicelik; 73:3 'nisf' kesir — sayı değil (okuma)",
  "gloss (1021): نهر 73:7 'nehâr' (gündüz) — gloss 'ırmak' (sûre 71 ailesi)",
  "◈K: 73:2, 73:6 ليل ve 73:7 نهر tetik — satırlar dolu; 73:9 شرق / غرب tetik listesinde değil, satır '—', gözlem ◇'de",
  "tarayıcı v4: 73:3 aday (F_ölçü) — çıpa değil, L1",
  "ölçüm iltifât: 73:6 (2MS → 3FS) ve 73:7 (3FS → 2MS) iltifât sayılıyor — haber cümlesine geçiş; okuma notu ◇'de",
  "ölçüm kip (517 ailesi): 73:5, 6, 7 'inne' tekidi kip alanında yok",
  "xref: 73:8 → 76:25, 87:15 (henüz okunmadı); 73:9 → 26:28, 70:40 (basıldı)",
  "kök ikilemesi: 73:4 رتل, 73:8 بتل, 73:10 هجر (mm2) — üçü de mef'ûl mutlak",
  "süreç: ön kuru koşuda 3 tetik uyuşmazı (73:2 ◈K ليل, 73:6 ◈K ليل, 73:7 ◈K نهر) dolduruldu; kayıt öncesi 73:9 ◈K satırı tetiksiz olduğu hâlde dolu yazılmıştı → '—' (oturum_tetik 1 → 0)",
 ],
 (11, 19): [
  "esmâ: e_oto 0 token (73:15 'şâhid' e_oto değil); KARAR 671 değişmedi; blokta mühür yok",
  "kök tablosu: kok_ekle_73 4 kök (نكل 73:12, غصص 73:13, كثب 73:14, هيل 73:14; blok_dikey 'KARŞILIK YOK' → eklendi); 1461 → 1465; retroaktif yama: hedef sûre listesi 8 ayet (ayet kaydı yok), hedefli yama 0, genel geçiş 0",
  "hapaks (yeni kök dersi): 73:13 غصص ★★★ hapaks z=3,28; 73:14 كثب + هيل ★★★ hapaks z=6,79 — içerik iddiası değil",
  "yıldız (924): 73:19 ★★ rab z=2,05 — içerik iddiası değil; 73:11, 12, 15, 16, 17, 18 yıldızsız",
  "ölçüm iltifât: 73:11 1S girişi ('zernî', 73:5 1P'den sonra) ve 73:12 1S → 1P geçişi iltifât sayılmıyor (araç alanı, 924); 73:14, 73:15 iltifât 1",
  "gloss (1021 ailesi): مهل 73:11 'mehhil' (mühlet ver) — kökte 'muhl' (erimiş maden) ile eşsesli lemma birleşmesi; kök sayımı verilmedi",
  "gloss: وبل 73:16 'vebîl' — gloss '(vebîl; 7 ayet)' kökün ayet sayısını lemmaya yazıyor; lemma 'vebîl' korpusta 1, kök 7 ayet",
  "eşsesli kök: سمو 73:8 'ism' / 73:18 'semâ'' — [x/2] kök sayımı iki ayrı lemmayı birleştiriyor; içerik iddiası değil",
  "◈K: 73:14 يوم / أرض / جبل, 73:17 يوم, 73:18 سمو tetik — satırlar dolu",
  "ölçüm biçim: 73:15 teşbih 'kemâ' biçim alanında yok (924)",
  "esit2 / xref: 73:19 esit2 → 76:29 TAM (henüz okunmadı); xref 73:18 → 17:5 (basıldı), 73:19 → 25:57 (basıldı), 76:29 (henüz okunmadı)",
  "kök ikilemesi: 73:14 جبل ×2, 73:15 رسل ×4 (simetri [4, 1, 7, 1]), 73:16 أخذ ×2 (mm2, mef'ûl mutlak)",
  "konuşan katmanı: 73:11 1S → 73:12-16 1P → 73:18-19 3MS; 73:17 2MP soru — sınırlar metinde işaretli değil, KAPATILAMAZ (1017)",
  "süreç: ön kuru koşuda 3 tetik uyuşmazı (73:14 ◈K يوم أرض جبل, 73:17 ◈K يوم, 73:18 ◈K سمو) dolduruldu; kayıtta 0",
 ],
 (20, 20): [
  "esmâ: e_oto 2 token (73:20 'ğafûr', 'rahîm' — inne'nin haberi, göndergesi lafız); İLÂHÎ ×2; KARAR 671 → 673; esma_kayit mühür EVET (ÇİFT), ton cemâl; geçerli mühür [20]",
  "kök tablosu: blok_dikey 'KARŞILIK YOK' yok — kök eklenmedi (1465); retroaktif yama hedefli 0, genel 0",
  "yıldız (924): 73:20 ★★★ kaynak n (78 kelime, n z=6,96) — içerik iddiası değil",
  "ölçüm iltifât: 73:20 içinde 2MS ('rabbeke', 'enneke', 'me'ake') → 2MP ('aleykum', 'fe'qra'û' …) geçişi iltifât sayılmıyor (iltifât 0; araç alanı, 924)",
  "fâsıla: 73:19 ا → 73:20 م ('rahîm'); ölçüm kafiye kırığı 0 — işaretsiz geçiş (924)",
  "ayet başı hizb işareti (۞) metinde var, ölçüm kelime sayımına girmiyor (araç notu)",
  "sayı işareti: 'sulus' ×2, 'nisf' — kesir, doğru alarm (okuma)",
  "◈K: tetik ليل / نهر / أرض — satır dolu",
  "tarayıcı v4: 73:20 aday — çıpa değil, L1",
  "xref: 73:20 → 2:110 (henüz okunmadı; dört kalıp), 4:74 (henüz okunmadı), 62:10 (basıldı)",
  "kök ikilemesi: 11 kök (أخر, أله ×7, ثلث, خير, علم ×3, غفر, قرأ ×3, قرض, قوم, ليل, يسر); simetri [6, 26, 49, 2]",
  "nakarat3: ayet içi 'fe'qra'û mâ teyessera' ×2, ''alime en' ×2, 've âharûne' ×2 — nakarat3 alanında görünmüyor (tek ayet içi; araç alanı)",
  "süreç: ön kuru koşuda 1 tetik uyuşmazı (73:20 ◈K ليل نهر أرض) dolduruldu; kayıtta 0",
 ],
}

DUZELTME = {
}
