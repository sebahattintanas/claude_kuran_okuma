# -*- coding: utf-8 -*-
"""alak_metin_1.py — sûre 96 (Alak) meal ve mercekler (◇ + ◈K ◈B ◈D ◈A).
Arapça sabit YOK: kökler yalnız korpus kök biçimiyle anılır, kelime biçimleri Latin harfle.
Yeni bloklar MEALn/Mn sözlükleri olarak eklenir ve sonda MEAL/M'ye katılır.
Sûre 40'tan itibaren ◇ satırında her ayet 'Karşıt çift (aday 1039, okuma): …' notu taşır — yoksa 'yok'
(okuma kolunun kontrol verisi; seçerek raporlama önlenir)."""
MEAL = {}
M = {}

# ── blok 96:1-8 (2026-10-31) ──
MEAL1 = {
 1: "Yaratan Rabbinin adıyla oku;",
 2: "insanı bir alakadan yarattı.",
 3: "Oku; Rabbin en cömert olandır,",
 4: "o ki kalemle öğretti,",
 5: "insana bilmediğini öğretti.",
 6: "Hayır! İnsan gerçekten azar,",
 7: "kendini yeterli gördüğü için.",
 8: "Şüphesiz dönüş Rabbinedir.",
}
M1 = {
 1: "◇ 'iqra' bi'smi rabbike'llezî xalaq' — IMPV 2MS + 'bi' + ad (GEN) + Rab (GEN) + 2MS + ilgi 'ellezî' + PERF 3MS (ölçüm edim emir, kip IMPV). Hitap 2MS adsız (1017). 'iqra'' ve 'xalaqa' nesnesiz (okuma). Sûre sınırı: 95:8 ('e-leyse'llâhu bi-ahkemi'l-hâkimîn') (okumada görüldü) sûre sonu → 96:1 emir ile açılış; fâsıla ن → ق (aday 1040, kayıt). Harekesiz 'bi'smi rabbike' 4 ayet: 69:52 ('fe-sebbih bi'smi rabbike'l-'azîm') (okumada görüldü), okunmuş 2 ayet daha, 96:1; 69:52'de 'sebbih' + sıfat / burada 'iqra'' + 'ellezî xalaqa' (okuma). Harekesiz 'ellezî xalaqa' 21 ayet: 87:2 ('ellezî xalaqa fe-sevvâ') (okumada görüldü), okunmuş 15 ayet daha, 96:1, henüz okunmamış 4; 87:1-2 (okumada görüldü) 'rabbike' + 'ellezî xalaqa' ardışık iki ayette / burada aynı ayette (okuma). Lemma 'qara'e' 15 ayet: okunmuş 12, sûre içi 96:1 ve 96:3, henüz okunmamış 1. Kök سمو ◈K tetiğinde S1 kısıtı — 'ism' izinli lemma değil, '—'. Ölçüm harf 37 → harf3 18 — besmele ailesi (924). Ölçüm ★★★ rab z=3,94 (formül davranışı). Çıpa: yaratma, nesnesiz; aşama / madde yok — L1 (87:2 kaydı emsali); tarayıcı vermedi. Lafız yok; esmâ yok. 5 kelime. قرأ [1/2], سمو [1/1], ربب [1/3], خلق [1/2]. Fâsıla ق. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — B2 'xalaqa' (tetik خلق) — yaratma, nesnesiz; madde / aşama yok; B1, B3, B4 —.\n"
    "◈D — D1 IMPV + 'bi' + ad + Rab + 2MS + 'ellezî' + PERF; D2 emir (ölçüm IMPV); D3 'bi'smi rabbike' (69:52); 'ellezî xalaqa' (87:2); D4 2MS + 3MS, sahset ['2', '3'].\n"
    "◈A — A1 Rab (2MS iyelik); hitap 2MS (adsız); A2 —; A3 konuşan adsız; A4 sûre emirle açılıyor.",
 2: "◇ 'xalaqa'l-insâne min 'alaq' — PERF 3MS + belirli ad (ACC) + 'min' + nekre ad (GEN). 96:1'in nesnesiz 'xalaqa'sı burada nesne ve madde ile tekrarlanıyor (okuma). Harekesiz 'xalaqa'l-insâne min' 5 ayet: 55:14 ('… min salsâlin ke'l-fexxâr') (okumada görüldü), okunmuş 3 ayet daha, 96:2; 55:14'te kuru balçık / burada ''alaq' (okuma). Lemma ''alaq' korpusta 1; kök علق 6 ayet: 75:38 ('thumme kâne 'alaqaten fe-xalaqa fe-sevvâ') (okumada görüldü), okunmuş 3 ayet daha, 96:2, henüz okunmamış 1; 75:38'de tekil ''alaqa' aşama dizisinde / burada ''alaq' tek madde adı (okuma). Lemma 'insân' 69 ayet: 55:14, 90:4 ve 95:4 (okumada görüldü), okunmuş 56 ayet daha, sûre içi 96:2, 96:5 ve 96:6, henüz okunmamış 7. Çıpa: yaratma + madde adı; aşama dizisi / mekanizma yok — L1 (75:38 kaydı emsali); tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 4 kelime, yıldızsız. خلق [2/2], أنس [1/3], علق [1/1]. Fâsıla ق. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — B1 insan ('el-insân' — ölçüm kök alanı أنس); B2 'xalaqa' (tetik خلق) — yaratma, 'min 'alaq' maddesiyle; B3 ''alaq' (tetik علق) — madde adı, aşama dizisi yok; B4 —.\n"
    "◈D — D1 PERF + belirli ad + 'min' + nekre ad; D2 —; D3 'xalaqa'l-insâne min' (55:14); kök علق (75:38); D4 3MS, sahset ['3'].\n"
    "◈A — A1 yaratan (3MS); insan; A2 —; A3 konuşan adsız; A4 yaratılış.",
 3: "◇ 'iqra' ve rabbuke'l-ekram' — IMPV 2MS + 've' + Rab (NOM) + 2MS + belirli üstünlük adı (NOM) (ölçüm kip IMPV). 96:1 emrinin tekrarı; 've' sonrası ad cümlesi (okuma). Ölçüm iltifât 1 — {3} → {2}. Lemma 'qara'e' sûre içi iki geçişin ikisi de basıldı. Lemma 'ekram' 2 ayet: 49:13 ('inne ekramekum 'inda'llâhi etqâkum') (okumada görüldü), 96:3 — korpusun iki geçişi: 49:13'te insanların en değerlisi / burada Rabbin sıfatı (okuma; aday 1041 sûreler arası okuma notu). 'ekram' esmâ listesinde değil — e_oto vermedi. Ölçüm ★★★ rab z=6,78 (formül davranışı). Fâsıla ق → م (ölçüm N sınıfı, kırık işaretlenmedi, 924). Çıpa: emir / sıfat (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız yok; esmâ yok. 3 kelime. قرأ [2/2], ربب [2/3], كرم [1/1]. Fâsıla م. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 IMPV + 've' + Rab + 2MS + üstünlük adı; D2 emir (ölçüm IMPV); D3 96:1 emrinin tekrarı; 'ekram' (49:13); D4 2MS, sahset ['2'], iltifât 1.\n"
    "◈A — A1 Rab (2MS iyelik); hitap 2MS; A2 —; A3 konuşan adsız; A4 emrin tekrarı.",
 4: "◇ 'ellezî 'alleme bi'l-qalem' — ilgi 'ellezî' + II. bab PERF 3MS + 'bi' + belirli ad (GEN); 96:3 'rabbuke'l-ekram'ın sıfat cümlesi (okuma). 'alleme' nesnesiz (okuma). Ölçüm iltifât 1 — {2} → {3}: 'ellezî' sıfat cümlesi, hitap değişmedi (924, sûre 87 dikkati). Lemma ''alleme' 35 ayet: 55:4 (''allemehu'l-beyân') (okumada görüldü), okunmuş 17 ayet daha, sûre içi 96:4 ve 96:5, henüz okunmamış 15. Lemma 'qalem' 4 ayet: 68:1 ('nûn ve'l-qalemi …') (okumada görüldü), okunmuş 1 ayet daha, 96:4, henüz okunmamış 1; 68:1'de yemin edilen / burada öğretme aracı (okuma). Kök علم sûre içi dört geçiş: 96:4, 96:5 (iki), 96:14 (henüz okunmadı). Çıpa: öğretme (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 3 kelime, yıldızsız. علم [1/4], قلم [1/1]. Fâsıla م. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'ellezî' + PERF + 'bi' + belirli ad; D2 —; D3 'alleme' (55:4); 'qalem' (68:1); D4 3MS, sahset ['3'], iltifât 1 (924).\n"
    "◈A — A1 öğreten ('ellezî', Rab'ın sıfatı); A2 —; A3 konuşan adsız; A4 Rabbin nitelemesi.",
 5: "◇ ''alleme'l-insâne mâ lem ya'lem' — II. bab PERF 3MS + belirli ad (ACC) + ilgi 'mâ' + 'lem' + IMPF (cezm) 3MS (ölçüm kip NEG). 96:4 'alleme'sinin nesneli tekrarı (okuma). Kök علم ikilemesi [2,3/4]: öğretti / bilmiyordu (okuma). Lemma ''alleme' sûre içi iki geçişin ikisi de basıldı. Lemma ''alime' 340 ayet: okunmuş 225, sûre içi 96:5 ve 96:14 (henüz okunmadı), henüz okunmamış 113. Çıpa: öğretme / bilgi (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 5 kelime, yıldızsız. علم ikilemesi [2,3/4], أنس [2/3]. Fâsıla م. Karşıt çift (aday 1039, okuma): ''alleme' / 'lem ya'lem' — öğretti / bilmiyordu (ayet içi).\n"
    "◈K — —\n"
    "◈B — B1 insan ('el-insân' — ölçüm kök alanı أنس); B2 —; B3 —; B4 —.\n"
    "◈D — D1 PERF + belirli ad + 'mâ' + 'lem' + IMPF; D2 olumsuzluk (ölçüm NEG); D3 kök ikilemesi علم; 96:4 ile 'alleme'; D4 3MS, sahset ['3'].\n"
    "◈A — A1 öğreten (3MS); insan; A2 —; A3 konuşan adsız; A4 öğretilen bilgi.",
 6: "◇ 'kellâ inne'l-insâne le-yatğâ' — 'kellâ' + 'inne' + belirli ad (ACC) + 'le' + IMPF 3MS (ölçüm kip EMPH, biçim KELLA). Lemma 'tağâ' 12 ayet: 79:17 ('… innehû tağâ') ve 79:37 ('fe-emmâ men tağâ') (okumada görüldü), okunmuş 9 ayet daha, 96:6; 79:17'de PERF, adı ayette geçen bir kişi için / burada IMPF, 'el-insân' için (okuma). Lemma 'insân' sûre içi üç geçişin üçü bu blokta (96:2, 5, 6). Ölçüm fâsıla sınıfı 'ٓ' — son harfte medde işareti; metinde ى (924); 96:6-8 üçü aynı artefakt sınıfında olduğundan kırık işaretlenmedi. Çıpa: tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 4 kelime, yıldızsız. أنس [3/3], طغي [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — B1 insan ('el-insân' — ölçüm kök alanı أنس); B2 —; B3 —; B4 —.\n"
    "◈D — D1 'kellâ' + 'inne' + belirli ad + 'le' + IMPF; D2 tekit + reddiye (ölçüm EMPH, KELLA); D3 'tağâ' (79:17, 79:37); D4 3MS, sahset ['3'].\n"
    "◈A — A1 insan; A2 —; A3 konuşan adsız; A4 azma.",
 7: "◇ 'en ra'âhu'steğnâ' — 'en' + PERF 3MS + 3MS + X. bab PERF 3MS. 'ra'â'nın öznesi ve nesnesi aynı kişi — kendini gördü (okuma); 96:6'nın gerekçesi (okuma). Lemma 'istağnâ' 4 ayet: 80:5 ve 92:8 (okumada görüldü), okunmuş 1 ayet daha, 96:7 — korpusun dört geçişi okundu. Lemma 'ra'â' 253 ayet: okunmuş 194, sûre içi 96:7, 96:9, 96:11, 96:13 ve 96:14 (son dördü henüz okunmadı), henüz okunmamış 54. Ölçüm fâsıla sınıfı 'ٓ' (924). Çıpa: tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 3 kelime, yıldızsız. رأي [1/5], غني [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'en' + PERF + 3MS + PERF; D2 —; D3 'istağnâ' (80:5, 92:8); D4 3MS, sahset ['3'].\n"
    "◈A — A1 insan (3MS); A2 —; A3 konuşan adsız; A4 azmanın gerekçesi.",
 8: "◇ 'inne ilâ rabbike'r-ruc'â' — 'inne' + 'ilâ' + Rab (GEN) + 2MS + belirli ad (ACC). Ölçüm iltifât 1 — {3} → {2}. 53:42 ('ve enne ilâ rabbike'l-muntehâ') (okumada görüldü) — aynı kuruluş: 'inne / enne' + 'ilâ rabbike' + belirli fu'lâ ad; 79:44 ('ilâ rabbike muntehâhâ') (okumada görüldü) (okuma). Harekesiz 'ilâ rabbike' 12 ayet: 53:42 ve 79:44 (okumada görüldü), okunmuş 9 ayet daha, 96:8. Lemma 'ruc'â' korpusta 1. Kök رجع 103 ayet: okunmuş 80, 96:8, henüz okunmamış 22. Rab sûre içi üç geçişin üçü bu blokta (96:1, 3, 8). Ölçüm ★★★ rab z=5,01 (formül davranışı). Ölçüm fâsıla sınıfı 'ٓ' (924). Çıpa: âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız yok; esmâ yok. 4 kelime. ربب [3/3], رجع [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'inne' + 'ilâ' + Rab + 2MS + belirli ad; D2 tekit ('inne'); D3 'ilâ rabbike' + fu'lâ ad (53:42); 79:44; D4 2MS, sahset ['2'], iltifât 1.\n"
    "◈A — A1 Rab (2MS iyelik); hitap 2MS; A2 —; A3 konuşan adsız; A4 dönüş.",
}
MEAL.update(MEAL1); M.update(M1)

# ── blok 96:9-19 (2026-10-31) ──
MEAL2 = {
 9: "Gördün mü o engelleyeni,",
 10: "bir kulu, namaz kıldığında?",
 11: "Gördün mü, ya o doğru yol üzerindeyse,",
 12: "ya da sakınmayı emrettiyse?",
 13: "Gördün mü, ya yalanladı ve yüz çevirdiyse?",
 14: "Bilmedi mi ki Allah görüyor?",
 15: "Hayır! Eğer vazgeçmezse, andolsun onu perçeminden tutup sürükleriz;",
 16: "yalancı, günahkâr bir perçemden.",
 17: "O hâlde meclisini çağırsın;",
 18: "Biz de zebânîleri çağıracağız.",
 19: "Hayır! Ona boyun eğme; secde et ve yaklaş.",
}
M2 = {
 9: "◇ 'e-ra'eyte'llezî yenhâ' — soru 'e' + PERF 2MS + ilgi 'ellezî' + IMPF 3MS (ölçüm edim soru, kip INTG). Hitap 2MS adsız; 'ellezî yenhâ' adsız (1017). 'yenhâ'nın nesnesi 96:10'da (okuma). Harekesiz 'e-ra'eyte' 6 ayet: 25:43 ('e-ra'eyte meni't-texadhe ilâhehû hevâh') (okumada görüldü), okunmuş 1 ayet daha, sûre içi 96:9, 96:11 ve 96:13, henüz okunmamış 1; 25:43'te 'men' + PERF / burada 'ellezî' + IMPF (okuma). Lemma 'nehâ' 31 ayet: 79:40 ('ve nehe'n-nefse 'ani'l-hevâ') (okumada görüldü), okunmuş 15 ayet daha, 96:9, henüz okunmamış 14; 79:40'ta kişi kendi nefsini / burada başkasını engelleyen (okuma). Lemma 'ra'â' sûre içi beş geçiş: 96:7 öznesi insan, 96:9, 96:11, 96:13 'e-ra'eyte' (2MS), 96:14 öznesi Allah (okuma; aday 1041). Ölçüm KAFİYE KIRILMASI ★ (n z=-1,00): 96:8 'ٓ' sınıfı → 96:9 A sınıfı — metinde ikisinin de son harfi ى; medde işareti artefaktı, sahte kırık (924). Çıpa: engelleme (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 3 kelime. رأي [2/5], نهي [1/2]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 soru + PERF + 'ellezî' + IMPF; D2 soru (ölçüm INTG); D3 'e-ra'eyte' (25:43); 'nehâ' (79:40); D4 2MS + 3MS, sahset ['2', '3'].\n"
    "◈A — A1 hitap 2MS (adsız); engelleyen (adsız); A2 —; A3 konuşan adsız; A4 engelleme sorusu.",
 10: "◇ ''abden izâ sallâ' — nekre ad (ACC) + 'izâ' + II. bab PERF 3MS. 96:9 'yenhâ'nın nesnesi (okuma); ''abd' nekre, adsız (1017). Lemma 'sallâ' 10 ayet: 75:31 ('fe-lâ saddaqa ve lâ sallâ') (okumada görüldü), okunmuş 5 ayet daha, 96:10, henüz okunmamış 3; 75:31'de kılmayan / burada kılan ve engellenen (okuma). Lemma ''abd' 126 ayet: okunmuş 103, 96:10, henüz okunmamış 22. Ölçüm fâsıla sınıfı 'ٓ' (924). Çıpa: ibadet (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 3 kelime, yıldızsız. عبد [1/1], صلو [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 nekre ad + 'izâ' + PERF; D2 —; D3 'sallâ' (75:31); D4 3MS, sahset ['3'].\n"
    "◈A — A1 kul (adsız, nekre); A2 —; A3 konuşan adsız; A4 namaz kılanın engellenmesi.",
 11: "◇ 'e-ra'eyte in kâne 'ala'l-hudâ' — soru 'e' + PERF 2MS + şart 'in' + PERF 3MS 'kâne' + 'alâ' + belirli ad (GEN) (ölçüm edim soru, şart; kip COND, INTG). 'kâne'nin öznesi adsız (1017): 96:9'daki engelleyen mi 96:10'daki kul mu metinde yazılmamış; şart cevabı da yazılmamış (okuma). Harekesiz 'e-ra'eyte' sûre içi ikinci geçiş. Harekesiz 'kâne 'alâ' 9 ayet: okunmuş 6, 96:11, henüz okunmamış 2. Lemma 'hudâ' 77 ayet: okunmuş 50, 96:11, henüz okunmamış 26. Ölçüm fâsıla sınıfı 'ٓ' (924). Çıpa: yol / tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 5 kelime, yıldızsız. رأي [3/5], كون [1/1], هدي [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): 'kâne 'ala'l-hudâ' / 96:13 'kezzebe ve tevellâ' — iki 'e-ra'eyte in' şartı (blok içi).\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 soru + PERF + 'in' + 'kâne' + 'alâ' + belirli ad; D2 soru + şart (ölçüm INTG, COND); D3 96:9 ve 96:13 ile 'e-ra'eyte'; D4 2MS + 3MS, sahset ['2', '3'].\n"
    "◈A — A1 hitap 2MS; 3MS adsız; A2 —; A3 konuşan adsız; A4 doğru yol şartı.",
 12: "◇ 'ev emere bi't-taqvâ' — 'ev' + PERF 3MS + 'bi' + belirli ad (GEN). 96:11 şartının ikinci şıkkı (okuma); özne adsız (1017). Harekesiz 'emere bi't-taqvâ' korpusta 1. Lemma 'taqvâ' 17 ayet: okunmuş 11, 96:12, henüz okunmamış 5. Lemma 'emere' 71 ayet: okunmuş 40, 96:12, henüz okunmamış 30. Ölçüm fâsıla sınıfı 'ٓ' (924). Çıpa: emir / tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 3 kelime, yıldızsız. أمر [1/1], وقي [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok (96:11 şartının aynı tarafı).\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'ev' + PERF + 'bi' + belirli ad; D2 —; D3 96:11 şartına bağlı; D4 3MS, sahset ['3'].\n"
    "◈A — A1 3MS adsız; A2 —; A3 konuşan adsız; A4 sakınmayı emretme.",
 13: "◇ 'e-ra'eyte in kezzebe ve tevellâ' — soru 'e' + PERF 2MS + şart 'in' + II. bab PERF 3MS + 've' + V. bab PERF 3MS (ölçüm edim soru, şart; kip COND, INTG). Özne adsız (1017); şart cevabı yazılmamış, 96:14 soru ile sürüyor (okuma). Harekesiz 'kezzebe ve tevellâ' 4 ayet: 20:48, 75:32 ve 92:16 (okumada görüldü), 96:13 — korpusun dört geçişi okundu. 75:31-32 ('fe-lâ saddaqa ve lâ sallâ … ve lâkin kezzebe ve tevellâ') (okumada görüldü): 'sallâ' ile 'kezzebe ve tevellâ' orada ardışık iki ayette / burada 96:10 ve 96:13'te, 'sallâ' kulun, 'kezzebe ve tevellâ' şartın (okuma). Harekesiz 'e-ra'eyte' sûre içi üçüncü geçiş. Kök كذب sûre içi 96:13 ve 96:16. Ölçüm fâsıla sınıfı 'ٓ' (924). Çıpa: tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 4 kelime, yıldızsız. رأي [4/5], كذب [1/2], ولي [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): 96:11-12 ''ala'l-hudâ … bi't-taqvâ' / 'kezzebe ve tevellâ' — iki 'e-ra'eyte in' şartı (blok içi).\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 soru + PERF + 'in' + PERF + 've' + PERF; D2 soru + şart (ölçüm INTG, COND); D3 'kezzebe ve tevellâ' (20:48, 75:32, 92:16); 75:31; D4 2MS + 3MS, sahset ['2', '3'].\n"
    "◈A — A1 hitap 2MS; 3MS adsız; A2 —; A3 konuşan adsız; A4 yalanlama şartı.",
 14: "◇ 'e-lem ya'lem bi-enne'llâhe yerâ' — soru 'e' + 'lem' + IMPF (cezm) 3MS + 'bi' + 'enne' + lafız (ACC) + IMPF 3MS (ölçüm edim soru, kip INTG, NEG). Sûrenin tek lafız geçişi; üç 'e-ra'eyte' (2MS) sorusunun ardından 'ra'â'nın öznesi Allah (okuma). Kök رأي [5/5]: 96:7 'ra'âhu' öznesi insan / 96:14 'yerâ' öznesi Allah — aynı lemma insan ve Allah için (aday 1041 sûre içi, kayıt). Kök علم [4/4]: 96:5 'mâ lem ya'lem' (insanın bilmediği) / 96:14 'e-lem ya'lem' — aynı 'lem ya'lem' dizisi iki ayette (okuma). Harekesiz 'e-lem ya'lem' (son eşleşmesi) 4 ayet: 9:78 ('e-lem ya'lemû enne'llâhe ya'lemu sirrahum …') (okumada görüldü), okunmuş 2 ayet daha, 96:14; 9:78'de Allah bilir / burada Allah görür (okuma). Ölçüm ★★★ allah z=3,47 (formül davranışı). Çıpa: bilgi / görme (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Rab yok; esmâ yok. 5 kelime. علم [4/4], أله [1/1], رأي [5/5]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 soru + 'lem' + IMPF + 'bi' + 'enne' + lafız + IMPF; D2 soru + olumsuzluk (ölçüm INTG, NEG); D3 'e-lem ya'lem' (9:78); 96:5 'lem ya'lem'; 96:7 'ra'â'; D4 3MS, sahset ['3'].\n"
    "◈A — A1 Allah (gören); 3MS adsız; A2 —; A3 konuşan adsız; A4 Allah'ın görmesi.",
 15: "◇ 'kellâ le-in lem yentehi le-nesfa'an bi'n-nâsiyeh' — 'kellâ' + 'le' + şart 'in' + 'lem' + VIII. bab IMPF (cezm) 3MS + 'le' + IMPF 1P (tekit) + 'bi' + belirli ad (GEN) (ölçüm kip COND, EMPH, NEG; biçim KELLA). Ölçüm şahıs 1P 1: konuşan birinci çoğul (okuma); 'yentehi'nin öznesi adsız (1017). Kök نهي [2/2]: 96:9 'yenhâ' engelliyor / 96:15 'yentehi' vazgeçmezse — engelleyene aynı kökle vazgeçme şartı (okuma). Lemma 'intehâ' 16 ayet: okunmuş 7, 96:15, henüz okunmamış 8. HAPAKS سفع: lemma ve kök korpusta 1 (ölçüm hapaks z=3,28 ★★★). Lemma 'nâsiye' 3 ayet: 11:56 ('mâ min dâbbetin illâ huve âxidhun bi-nâsiyetihâ') (okumada görüldü), sûre içi 96:15 ve 96:16 — korpusun üç geçişi okundu; 11:56'da her canlının perçemi O'nun elinde / burada tehdit (okuma). Kök نصي 4 ayet: 11:56 ve 55:41 ('fe-yu'xadhu bi'n-nevâsî ve'l-aqdâm') (okumada görüldü), 96:15, 96:16 — korpusun dört geçişi okundu; 55:41 edilgen / burada 1P etken (okuma). 68:16 ('se-nesimuhû 'ala'l-xurtûm') (okumada görüldü): 1P gelecek + yüzdeki uzuv / burada 1P tekit + alın perçemi (okuma). 'nâsiye' uzuv adı; kök ◈B tetik listesinde değil. 'kellâ' sûre içi 96:6, 96:15, 96:19. Çıpa: tehdit (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 6 kelime. نهي [2/2], سفع [1/1], نصي [1/2]. Fâsıla ة. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'kellâ' + 'le' + 'in' + 'lem' + IMPF + 'le' + IMPF + 'bi' + belirli ad; D2 reddiye + şart + tekit (ölçüm KELLA, COND, EMPH); D3 'nâsiye' (11:56); kök نصي (55:41); 68:16; D4 1P + 3MS, sahset ['1', '3'].\n"
    "◈A — A1 konuşan 1P; 3MS adsız; A2 —; A3 konuşan 1P (adsız); A4 perçemden tutma tehdidi.",
 16: "◇ 'nâsiyetin kâdhibetin xâti'eh' — nekre ad (GEN) + iki nekre ism-i fâil sıfat (F, GEN); 96:15 'bi'n-nâsiyeh'in bedeli (okuma). Fiil yok (ölçüm zaman yok, şahıs işaret yok). 'nâsiye' 96:15'te belirli / burada nekre tekrar (okuma). Kök كذب [2/2]: 96:13 'kezzebe' fiil / 96:16 'kâdhibe' perçemin sıfatı (okuma). Lemma 'kâdhib' 32 ayet: okunmuş 28, 96:16, henüz okunmamış 3. Lemma 'xâti'e' 2 ayet: 69:9 ('… bi'l-xâti'eh') (okumada görüldü), 96:16 — korpusun iki geçişi okundu; 69:9'da belirli ad / burada nekre sıfat (okuma). Çıpa: nitelik (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 3 kelime, yıldızsız. نصي [2/2], كذب [2/2], خطأ [1/1]. Fâsıla ة. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 nekre ad + iki nekre sıfat; D2 —; D3 'xâti'e' (69:9); 96:15 'nâsiye' tekrarı; D4 şahıs işareti yok.\n"
    "◈A — A1 —; A2 —; A3 konuşan adsız; A4 perçemin nitelenmesi.",
 17: "◇ 'fe'l-yed'u nâdiyeh' — 'fe' + 'li' (emir) + IMPF (cezm) 3MS + ad (ACC) + 3MS (ölçüm edim emir, kip IMPV). Özne 96:15-16'daki 3MS, adsız (1017). Lemma 'nâdî' 2 ayet: 29:29 ('… ve te'tûne fî nâdîkumu'l-munker') (okumada görüldü), 96:17 — korpusun iki geçişi okundu; 29:29'da toplantı yeri / burada çağrılacak meclis (okuma). Kök ندي 50 ayet: okunmuş 39, 96:17, henüz okunmamış 10. Lemma 'de'â' 155 ayet: okunmuş 118, sûre içi 96:17 ve 96:18, henüz okunmamış 35. Çıpa: çağrı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 2 kelime, yıldızsız. دعو [1/2], ندي [1/1]. Fâsıla ه. Karşıt çift (aday 1039, okuma): 'fe'l-yed'u nâdiyeh' / 96:18 'se-ned'u'z-zebâniyeh' — aynı fiille iki tarafın çağrısı (blok içi).\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'fe' + 'li' + IMPF + ad + 3MS; D2 emir (ölçüm IMPV); D3 'nâdî' (29:29); D4 3MS, sahset ['3'].\n"
    "◈A — A1 3MS adsız; meclisi; A2 —; A3 konuşan adsız; A4 meydan okuma.",
 18: "◇ 'se-ned'u'z-zebâniyeh' — 'se' + IMPF 1P + belirli ad (ACC) (ölçüm kip FUT). Ölçüm iltifât 1 — {3} → {1}: 96:15 'le-nesfa'an' ile aynı 1P konuşan (okuma). HAPAKS زبن: lemma ve kök korpusta 1 (ölçüm hapaks z=3,28 ★★★). Lemma 'de'â' sûre içi iki geçişin ikisi de bu blokta: 96:17 3MS emir / 96:18 1P gelecek (okuma). 'ned'u' yazıda sonundaki vavsız (okuma). Çıpa: tehdit (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 2 kelime. دعو [2/2], زبن [1/1]. Fâsıla ة. Karşıt çift (aday 1039, okuma): 96:17 'fe'l-yed'u nâdiyeh' / 'se-ned'u'z-zebâniyeh' (blok içi).\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'se' + IMPF + belirli ad; D2 gelecek (ölçüm FUT); D3 96:17 ile 'de'â'; 96:15 1P; D4 1P, sahset ['1'], iltifât 1.\n"
    "◈A — A1 konuşan 1P; zebânîler; A2 —; A3 konuşan 1P (adsız); A4 karşı çağrı.",
 19: "◇ 'kellâ lâ tuti'hu ve'scud ve'qterib' — 'kellâ' + 'lâ' (nehy) + IV. bab IMPF (cezm) 2MS + 3MS + 've' + IMPV 2MS + 've' + VIII. bab IMPV 2MS (ölçüm edim emir, yasak; kip IMPV 2, PRO 1; biçim KELLA + NEHY). Ölçüm iltifât 1 — {1} → {2}: hitap yeniden 2MS, adsız (1017); 'tuti'hu'nun 3MS'si adsız (okuma). Lemma 'etâ'a' 64 ayet: okunmuş 43, 96:19, henüz okunmamış 20. 68:8 ('fe-lâ tuti'i'l-mukezzibîn') (okumada görüldü): 'lâ tuti'' + yalanlayanlar / burada 'lâ tuti'hu' 96:13 'kezzebe' şartından sonra (okuma). Lemma 'secede' 27 ayet: okunmuş 19, 96:19, henüz okunmamış 7. 84:21 ('… lâ yescudûn') (okumada görüldü): secde işaretli iki ayet bu oturumda; 84:21'de olumsuz 3MP / burada emir 2MS (okuma). Lemma 'iqterabe' 5 ayet: okunmuş 3, 96:19, henüz okunmamış 1. 'kellâ' sûre içi üç geçişin üçü basıldı. Ölçüm fâsıla ب (96:15-18 ة / ه'den sonra); ölçüm kırık işaretlemedi. Çıpa: emir / ibadet (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 5 kelime, yıldızsız. طوع [1/1], سجد [1/1], قرب [1/1]. Fâsıla ب. Karşıt çift (aday 1039, okuma): 'lâ tuti'hu' / 've'scud ve'qterib' — boyun eğme / secde et ve yaklaş (ayet içi).\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'kellâ' + 'lâ' + IMPF + 3MS + 've' + IMPV + 've' + IMPV; D2 reddiye + yasak + emir (ölçüm KELLA, PRO, IMPV); D3 'lâ tuti'' (68:8); secde (84:21); D4 2MS + 3MS, sahset ['2', '3'], iltifât 1.\n"
    "◈A — A1 hitap 2MS; 3MS adsız; A2 —; A3 konuşan adsız; A4 sûre secde emriyle kapanıyor.",
}
MEAL.update(MEAL2); M.update(M2)
