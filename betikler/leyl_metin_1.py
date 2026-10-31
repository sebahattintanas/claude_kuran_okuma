# -*- coding: utf-8 -*-
"""leyl_metin_1.py — sûre 92 (Leyl) meal ve mercekler (◇ + ◈K ◈B ◈D ◈A).
Arapça sabit YOK: kökler yalnız korpus kök biçimiyle anılır, kelime biçimleri Latin harfle.
Yeni bloklar MEALn/Mn sözlükleri olarak eklenir ve sonda MEAL/M'ye katılır.
Sûre 40'tan itibaren ◇ satırında her ayet 'Karşıt çift (aday 1039, okuma): …' notu taşır — yoksa 'yok'
(okuma kolunun kontrol verisi; seçerek raporlama önlenir)."""
MEAL = {}
M = {}

# ── blok 92:1-11 (2026-10-31) ──
MEAL1 = {
 1: "Bürüdüğünde geceye yemin olsun,",
 2: "açığa çıktığında gündüze,",
 3: "erkeği ve dişiyi yaratana —",
 4: "şüphesiz çabanız türlü türlüdür.",
 5: "Kim verir ve sakınırsa",
 6: "ve en güzeli doğrularsa,",
 7: "onu en kolay olana kolaylaştıracağız.",
 8: "Kim de cimrilik eder ve kendini yeterli görürse",
 9: "ve en güzeli yalanlarsa,",
 10: "onu en zor olana kolaylaştıracağız.",
 11: "Yıkıma düştüğünde malı ona yarar sağlamaz.",
}
M1 = {
 1: "◇ 've'l-leyli izâ yağşâ' — yemin 've' + belirli ad (GEN) + 'izâ' + IMPF 3MS (ölçüm biçim QASEM); nesne yazılmamış — neyi bürüdüğü metinde yok (okuma). Yemin eden adsız (1017). Lemma dizisi 'leyl' + 'izâ' + 'ğaşiye' 2 ayet: 91:4 ('ve'l-leyli izâ yağşâhâ') (okumada görüldü), 92:1 — ardışık sûrede aynı lemma dizisi; 91:4'te 3FS nesne 'hâ' / burada nesnesiz (okuma); harekesiz 've'l-leyli izâ yağşâ' korpusta 1 (92:1). Sûre sınırı: 91:15 ('ve lâ yaxâfu 'uqbâhâ') (okumada görüldü) sûre sonu → 92:1 yemin ile açılış; fâsıla ا → ى (aday 1040, kayıt). Lemma 'leyl' 75 ayet: 91:4 ve 10:6 (okumada görüldü), okunmuş 60 ayet daha, 92:1, henüz okunmamış 12. Lemma 'ğaşiye' 11 ayet: 91:4 (okumada görüldü), okunmuş 8 ayet daha, 92:1, henüz okunmamış 1. Ölçüm harf 31 → harf3 12 — besmele ailesi (924). Çıpa: yemin edilen vakit + süreç; mekanizma yok — L0 (91:4 kaydı emsali); tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 3 kelime, yıldızsız. ليل [1/1], غشو [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — K1 gece (ليل — ölçüm kök alanı); K2 —; K3 —; K4 'yağşâ' — bürüme, özne gece; nesne yazılmamış.\n"
    "◈B — —\n"
    "◈D — D1 've' + belirli ad + 'izâ' + IMPF; D2 yemin (ölçüm QASEM); D3 91:4 ile aynı lemma dizisi (nesne farkı); D4 3MS, sahset ['3'].\n"
    "◈A — A1 gece; A2 —; A3 yemin eden adsız; A4 sûre yeminle açılıyor.",
 2: "◇ 've'n-nehâri izâ tecellâ' — 've' + belirli ad (GEN) + 'izâ' + PERF 3MS; atıflı yemin (ölçüm biçim alanında QASEM yok, 924). 92:1 IMPF / burada PERF (okuma). Fiil V. bab 'tecellâ' — ölçüm bab alanı 'I. bab' yazıyor (morph VF:1 etiketi, 924). Harekesiz 've'n-nehâri izâ' 2 ayet: 91:3 ('ve'n-nehâri izâ cellâhâ') (okumada görüldü), 92:2 — 91:3'te II. bab + 3FS nesne (gündüz bir şeyi açığa çıkarır) / burada V. bab nesnesiz (gündüz açığa çıkar) (okuma). Kök جلو 5 ayet: 91:3 (okumada görüldü), okunmuş 1 ayet daha, 92:2, henüz okunmamış 2. Lemma 'tecellâ' 2 ayet: 92:2 ve henüz okunmamış 1. Lemma 'nehâr' 50 ayet: 91:3 ve 10:6 (okumada görüldü), okunmuş 39 ayet daha, 92:2, henüz okunmamış 8. Çıpa: yemin edilen vakit + süreç — L0 (91:3 kaydı emsali); tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 3 kelime, yıldızsız. نهر [1/1], جلو [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): 92:1 'el-leyl' / 92:2 'en-nehâr' — gece / gündüz; 'yağşâ' / 'tecellâ' — bürüme / açığa çıkma (ayetler arası).\n"
    "◈K — K1 gündüz (نهر — ölçüm kök alanı); K2 —; K3 —; K4 'tecellâ' — açığa çıkma, özne gündüz.\n"
    "◈B — —\n"
    "◈D — D1 've' + belirli ad + 'izâ' + PERF; D2 atıflı yemin (924); D3 've'n-nehâri izâ' (91:3); 92:1 ile aynı kalıp; D4 3MS, sahset ['3'].\n"
    "◈A — A1 gündüz; A2 —; A3 yemin eden adsız; A4 yemin dizisi.",
 3: "◇ 've mâ xalaqa'z-zekera ve'l-unthâ' — 've' + 'mâ' + PERF 3MS + iki belirli ad (ACC); atıflı yemin (924). Morph 'mâ' ilgi zamiri (REL) — meal 'yaratana' (ilgi okuması); 'mâ' mastar okuması da metinde dışlanmıyor — KAPATILAMAZ (okuma). Yaratan adsız (1017). Ölçüm xref → 49:13 (okumada görüldü): 49:13'te 1P + 2MP nesne 'xalaqnâkum min zekerin ve unthâ' (nekre) / burada 3MS + belirli 'ez-zeker', 'el-unthâ' nesne (okuma). Harekesiz 've mâ xalaqa' 3 ayet: 10:6 (okumada görüldü), 92:3, henüz okunmamış 1; 10:6'da özne lafız ve yer 'fi's-semâvâti ve'l-ard' / burada özne yazılmamış (okuma). Lemma 'xalaqa' 168 ayet: 10:6 ve 49:13 (okumada görüldü), okunmuş 136 ayet daha, 92:3, henüz okunmamış 29. Lemma 'zeker' 18 ayet: 49:13 (okumada görüldü), okunmuş 8 ayet daha, 92:3, henüz okunmamış 8. Lemma 'unthâ' 22 ayet: 49:13 (okumada görüldü), okunmuş 15 ayet daha, 92:3, henüz okunmamış 5. Kök ذكر gloss'u ('anma, zikir') 'zeker' (erkek) anlamına uymuyor (1021). Ölçüm fâsıla 'KAFİYE KIRILMASI' ve ★ — son harfte medde işareti harf sayıldı; metinde ى, 92:1-2 ile aynı — yanlış pozitif (924). Çıpa: yaratma + iki cins adı; aşama / madde / mekanizma yok — L1 (49:13 kaydı emsali); tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 4 kelime. خلق [1/1], ذكر [1/1], أنث [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): 'ez-zeker' / 'el-unthâ' — erkek / dişi (ayet içi).\n"
    "◈K — —\n"
    "◈B — B1 erkek / dişi ('ez-zeker', 'el-unthâ' — tetik أنث; kök ذكر tetik listesinde değil); B2 'xalaqa' (tetik خلق) — yaratma; madde / aşama yok; B3 —; B4 —.\n"
    "◈D — D1 've' + 'mâ' + PERF + iki belirli ad; D2 atıflı yemin (924); D3 'xalaqa … zeker … unthâ' (49:13, xref); 've mâ xalaqa' (10:6); D4 3MS, sahset ['3'].\n"
    "◈A — A1 yaratan (adsız 'mâ'); erkek, dişi; A2 —; A3 yemin eden adsız; A4 yemin dizisi kapanıyor.",
 4: "◇ 'inne sa'yekum le-şettâ' — 'inne' + ad (ACC) + 2MP + 'le' + ad (ölçüm kip EMPH). Yemin dizisinin (92:1-3) cevabı olarak okunabilir (okuma). Hitap 2MP adsız (1017); ölçüm iltifât 1, {3} → {2} — 2MP hitabın girişi. Lemma 'sa'y' 9 ayet: 76:22 ('… ve kâne sa'yukum meşkûrâ') ve 53:40 ('ve enne sa'yehû sevfe yurâ') (okumada görüldü), okunmuş 5 ayet daha, 92:4, henüz okunmamış 1; 76:22'de 2MP çaba şükranla karşılanmış / burada 2MP çaba türlü türlü (okuma). Lemma 'şettâ' 3 ayet: 20:53 (okumada görüldü), okunmuş 1 ayet daha, 92:4 — 20:53'te bitkiler türlü türlü / burada çaba (okuma). Çıpa: tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 3 kelime, yıldızsız. سعي [1/1], شتت [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'inne' + ad + 2MP + 'le' + ad; D2 tekit (ölçüm EMPH); D3 'sa'yukum' (76:22, lemma); D4 2MP, sahset ['2'], iltifât 1.\n"
    "◈A — A1 hitap 2MP (adsız); A2 —; A3 konuşan adsız; A4 yeminin cevabı (okuma).",
 5: "◇ 'fe-emmâ men a'tâ ve'ttaqâ' — 'fe' + 'emmâ' + 'men' + IV. bab PERF 3MS + 've' + VIII. bab PERF 3MS (ölçüm edim şart, kip COND, biçim AMMA). 'a'tâ' nesnesiz — ne verdiği yazılmamış (okuma). Ölçüm iltifât 1, {2} → {3}: 2MP hitaptan 'men' ile üçüncü şahıs anlatımına geçiş (okuma). Harekesiz 'fe-emmâ men' 6 ayet: 79:37 ('fe-emmâ men tağâ') (okumada görüldü), okunmuş 3 ayet daha, 92:5, henüz okunmamış 1. Lemma 'a'tâ' 7 ayet: 53:34 ('ve a'tâ qalîlen ve ekdâ') (okumada görüldü), okunmuş 3 ayet daha, 92:5, henüz okunmamış 2; 53:34'te az verip kesen / burada nesnesiz verip sakınan (okuma). Lemma 'ittaqâ' 158 ayet: 10:6 ('yetteqûn') (okumada görüldü), okunmuş 76 ayet daha, 92:5, henüz okunmamış 80. Kök وقي [1/2] — sûre içi ikinci geçiş 92:17 (henüz okunmadı). Çıpa: tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 4 kelime, yıldızsız. عطو [1/1], وقي [1/2]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'fe' + 'emmâ' + 'men' + PERF + 've' + PERF; D2 şart / ayırma (ölçüm COND, AMMA); D3 'fe-emmâ men' (79:37); D4 3MS, sahset ['3'], iltifât 1.\n"
    "◈A — A1 veren ve sakınan (adsız 'men'); A2 —; A3 konuşan adsız; A4 iki yolun birincisi açılıyor.",
 6: "◇ 've saddaqa bi'l-husnâ' — 've' + II. bab PERF 3MS + 'bi' + belirli ad (GEN); özne 92:5 'men' (okuma). 'el-husnâ' (en güzel olan) — neyin en güzeli olduğu metinde yazılmamış — KAPATILAMAZ; meal 'en güzeli' ile açık bıraktı. Lemma 'saddaqa' 10 ayet: okunmuş 9, 92:6. Lemma 'husnâ' 17 ayet: okunmuş 12, sûre içi 92:6 ve 92:9, henüz okunmamış 3. Çıpa: tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 2 kelime, yıldızsız. صدق [1/1], حسن [1/2]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 've' + PERF + 'bi' + belirli ad; D2 —; D3 92:9 ile aynı iskelet ('bi'l-husnâ'); D4 3MS, sahset ['3'].\n"
    "◈A — A1 aynı 'men' (adsız); A2 —; A3 konuşan adsız; A4 birinci yol.",
 7: "◇ 'fe-se-nuyessiruhû li'l-yusrâ' — 'fe' + 'se' + II. bab IMPF 1P + 3MS + 'li' + belirli ad (GEN) (ölçüm kip FUT). Konuşan 1P adsız (1017) — sûrede 1P'nin ilk geçişi. 3MS 'hû' 92:5 'men' (okuma). Ölçüm iltifât 0 — {3} → {1, 3} kısmi örtüşme (924). Lemma dizisi 'yessara' + 'yusrâ' 2 ayet: 87:8 ('ve nuyessiruke li'l-yusrâ') (okumada görüldü), 92:7; 87:8'de 2MS nesne / burada 3MS nesne ve 'se' gelecek eki (okuma). Harekesiz 'fe-se-nuyessiruhû' 2 ayet: sûre içi 92:7 ve 92:10. Lemma 'yessara' 11 ayet: 87:8 (okumada görüldü), okunmuş 8 ayet daha, sûre içi 92:7 ve 92:10. Lemma 'yusrâ' 2 ayet: 87:8 (okumada görüldü), 92:7. Çıpa: âhiret / sonuç (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 2 kelime, yıldızsız. يسر ikilemesi [1,2/3]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'fe' + 'se' + IMPF 1P + 3MS + 'li' + belirli ad; D2 gelecek (ölçüm FUT); D3 kök ikilemesi يسر; 'nuyessiru … li'l-yusrâ' (87:8); 92:10 ile aynı iskelet; D4 1P + 3MS, sahset ['1', '3'], iltifât 0 (924).\n"
    "◈A — A1 konuşan 1P (adsız); veren-sakınan ('hû'); A2 —; A3 konuşan 1P adsız; A4 birinci yolun sonucu.",
 8: "◇ 've emmâ men bexile ve'steğnâ' — 've' + 'emmâ' + 'men' + PERF 3MS + 've' + X. bab PERF 3MS (ölçüm edim şart, kip COND, biçim AMMA). 92:5 ile aynı iskelet: 'emmâ' + 'men' + iki PERF (okuma). Harekesiz 've emmâ men' 7 ayet: 79:40 ve 80:8 ('ve emmâ men câ'eke yes'â') (okumada görüldü), okunmuş 3 ayet daha, 92:8, henüz okunmamış 1. Lemma 'istağnâ' 4 ayet: 80:5 ('emmâ meni'steğnâ') (okumada görüldü), okunmuş 1 ayet daha, 92:8, henüz okunmamış 1; 80:5'te 'emmâ' + 'men' + 'istağnâ' tek başına / burada 'bexile'ye atıflı ikinci fiil (okuma). Lemma 'bexile' 7 ayet: 47:38 ve 57:24 (okumada görüldü), okunmuş 2 ayet daha, 92:8, henüz okunmamış 2. 47:38 ve 57:24'te kök بخل insan için, kök غني lafız için ('el-ğaniyy') / burada ikisi de 'men' için ('bexile ve'steğnâ') (okuma; aday 1041 sûreler arası okuma notu). Kök غني [1/2]. Çıpa: tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 4 kelime, yıldızsız. بخل [1/1], غني [1/2]. Fâsıla ى. Karşıt çift (aday 1039, okuma): 92:5 'a'tâ' / 92:8 'bexile' — verdi / cimrilik etti (ayetler arası).\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 've' + 'emmâ' + 'men' + PERF + 've' + PERF; D2 şart / ayırma (ölçüm COND, AMMA); D3 've emmâ men' (79:40, 80:8); 'emmâ men istağnâ' (80:5); 92:5 ile aynı iskelet; D4 3MS, sahset ['3'].\n"
    "◈A — A1 cimri ve kendini yeterli gören (adsız 'men'); A2 —; A3 konuşan adsız; A4 ikinci yol açılıyor.",
 9: "◇ 've kezzebe bi'l-husnâ' — 've' + II. bab PERF 3MS + 'bi' + belirli ad (GEN); özne 92:8 'men' (okuma). 92:6 ile aynı iskelet, yalnız fiil farklı (okuma). Lemma 'kezzebe' 163 ayet: okunmuş 122, sûre içi 92:9 ve 92:16 (henüz okunmadı), henüz okunmamış 39. Lemma 'husnâ' sûre içi 92:6 ve 92:9. Çıpa: tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 2 kelime, yıldızsız. كذب [1/2], حسن [2/2]. Fâsıla ى. Karşıt çift (aday 1039, okuma): 92:6 'saddaqa' / 92:9 'kezzebe' — doğruladı / yalanladı (ayetler arası).\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 've' + PERF + 'bi' + belirli ad; D2 —; D3 92:6 ile aynı iskelet; D4 3MS, sahset ['3'].\n"
    "◈A — A1 aynı 'men' (adsız); A2 —; A3 konuşan adsız; A4 ikinci yol.",
 10: "◇ 'fe-se-nuyessiruhû li'l-'usrâ' — 'fe' + 'se' + II. bab IMPF 1P + 3MS + 'li' + belirli ad (GEN) (ölçüm kip FUT). 92:7 ile aynı iskelet, yalnız son ad farklı (okuma); 'kolaylaştırma' fiili 'en zor olan'a yönelik (okuma). 3MS 'hû' 92:8 'men' (okuma). Lemma ''usrâ' korpusta 1. Kök عسر 12 ayet: 74:9 ('… yevmun 'asîr') (okumada görüldü), okunmuş 6 ayet daha, 92:10, henüz okunmamış 4. Kök يسر sûre içi üç geçişin üçü bu blokta (92:7 iki, 92:10 bir) — [3/3]. Çıpa: âhiret / sonuç (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 2 kelime, yıldızsız. يسر [3/3], عسر [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): 92:7 'li'l-yusrâ' / 92:10 'li'l-'usrâ' — en kolay / en zor (ayetler arası).\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'fe' + 'se' + IMPF 1P + 3MS + 'li' + belirli ad; D2 gelecek (ölçüm FUT); D3 92:7 ile aynı iskelet; D4 1P + 3MS, sahset ['1', '3'].\n"
    "◈A — A1 konuşan 1P (adsız); cimri ('hû'); A2 —; A3 konuşan 1P adsız; A4 ikinci yolun sonucu.",
 11: "◇ 've mâ yuğnî 'anhu mâluhû izâ teraddâ' — 've' + 'mâ' (olumsuzluk) + IV. bab IMPF 3MS + ''an' + 3MS + ad (NOM) + 3MS + 'izâ' + V. bab PERF 3MS (ölçüm kip NEG). 92:3 'mâ' ilgi / burada olumsuzluk (morph NEG) (okuma). 3MS zamirler 92:8 'men' (okuma). Lemma 'ağnâ' 28 ayet: 69:28 ('mâ ağnâ 'annî mâliyeh') (okumada görüldü), okunmuş 22 ayet daha, 92:11, henüz okunmamış 4; 69:28'de PERF 1S, malı kendisine yarar sağlamadı (kendi sözü) / burada IMPF 3MS (okuma). Lemma 'mâl' 80 ayet: 69:28 (okumada görüldü), okunmuş 47 ayet daha, sûre içi 92:11 ve 92:18 (henüz okunmadı), henüz okunmamış 30. Kök غني [2/2]: 92:8 'istağnâ' (kendini yeterli gördü) / 92:11 'yuğnî' (malı yetmez) (okuma). Lemma 'teraddâ' korpusta 1; kök ردي 6 ayet: okunmuş 3, 92:11, henüz okunmamış 2. Ölçüm fâsıla 'KAFİYE KIRILMASI' ve ★ — son harfte medde işareti harf sayıldı; metinde ى — yanlış pozitif (924). Çıpa: tutum / âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 6 kelime. غني [2/2], مول [1/2], ردي [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 've' + 'mâ' + IMPF + ''an' + 3MS + ad + 3MS + 'izâ' + PERF; D2 olumsuzlama (ölçüm NEG); D3 'mâ ağnâ 'an … mâl' (69:28, lemma); D4 3MS ×4, sahset ['3'].\n"
    "◈A — A1 cimri (3MS); malı; A2 —; A3 konuşan adsız; A4 ikinci yolun sonu.",
}
MEAL.update(MEAL1); M.update(M1)

# ── blok 92:12-21 (2026-10-31) ──
MEAL2 = {
 12: "Şüphesiz yol göstermek bize düşer.",
 13: "Şüphesiz âhiret de ilki de bizimdir.",
 14: "Sizi alev saçan bir ateşle uyardım;",
 15: "ona en bedbahttan başkası girmez,",
 16: "o ki yalanladı ve yüz çevirdi.",
 17: "En sakınan ise ondan uzak tutulacak,",
 18: "o ki malını verir, arınır.",
 19: "Onun katında hiç kimsenin karşılığı verilecek bir nimeti yoktur,",
 20: "yalnız en yüce Rabbinin yüzünü aramak vardır.",
 21: "Ve o elbette hoşnut olacaktır.",
}
M2 = {
 12: "◇ 'inne 'aleynâ le'l-hudâ' — 'inne' + ''alâ' + 1P + 'le' + belirli ad (ACC) (ölçüm kip EMPH). Konuşan 1P adsız (1017) — 92:7 ve 92:10'daki 1P (okuma). Ölçüm iltifât 1, {3} → {1}. Harekesiz 'inne 'aleynâ' 4 ayet: 75:17, 75:19 ve 88:26 (okumada görüldü), 92:12 — üçünde ''aleynâ' + zamirli ad (toplamak ve okutmak, açıklamak, hesap) / burada belirli 'el-hudâ' (okuma). Lemma dizisi (bütün ayet) 2 ayet: 22:67 ('… innake le-'alâ huden mustaqîm') (okumada görüldü), 92:12 — 22:67'de 2MS + nekre 'huden' / burada 1P + belirli 'el-hudâ' (okuma). Lemma 'hudâ' 77 ayet: 22:67 (okumada görüldü), okunmuş 48 ayet daha, 92:12, henüz okunmamış 27. Çıpa: söz / tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 3 kelime, yıldızsız. هدي [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'inne' + ''alâ' + 1P + 'le' + belirli ad; D2 tekit (ölçüm EMPH); D3 'inne 'aleynâ' (75:17, 75:19, 88:26); lemma dizisi 22:67; D4 1P, sahset ['1'], iltifât 1.\n"
    "◈A — A1 konuşan 1P (adsız); A2 —; A3 konuşan 1P adsız; A4 yol göstermenin sahibi.",
 13: "◇ 've inne lenâ le'l-âxirate ve'l-ûlâ' — 've' + 'inne' + 'li' + 1P + 'le' + iki belirli ad (ACC) (ölçüm kip EMPH). 92:12 ile aynı kuruluş, ''alâ' yerine 'li' (okuma). Lemma dizisi 'âxira' + 'ûlâ' 3 ayet: 53:25 ('fe-li'llâhi'l-âxiratu ve'l-ûlâ') ve 79:25 (okumada görüldü), 92:13; 53:25'te 'li' + lafız / burada 'li' + 1P (okuma); 79:25'te iki âlem cezanın niteliği (okuma). Lemma 'âxir' 153 ayet: 53:25 ve 79:25 (okumada görüldü), okunmuş 101 ayet daha, 92:13, henüz okunmamış 49. Lemma 'evvel' 82 ayet: 53:25 ve 79:25 (okumada görüldü), okunmuş 65 ayet daha, 92:13, henüz okunmamış 14. Esmâ: e_oto 'âxir' ve 'evvel' — âhiret ve ilk (dünya), ilâhî ad değil: karar 'degil'; ölçüm 'SON konum, MÜHÜRSÜZ', esma_kayit mühür EVET (ÇİFT), bilanço geçerli mühür 0 (1022). Çıpa: âhiret / söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok. 4 kelime, yıldızsız. أخر [1/1], أول [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): 'el-âxira' / 'el-ûlâ' — son / ilk (âhiret / dünya) (ayet içi).\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 've' + 'inne' + 'li' + 1P + 'le' + iki belirli ad; D2 tekit (ölçüm EMPH); D3 'âxira … ûlâ' (53:25, 79:25); 92:12 ile aynı kuruluş; D4 1P, sahset ['1'].\n"
    "◈A — A1 konuşan 1P (adsız); âhiret, ilk; A2 —; A3 konuşan 1P adsız; A4 iki âlemin sahibi.",
 14: "◇ 'fe-enzertukum nâran telezzâ' — 'fe' + IV. bab PERF 1S + 2MP + nekre ad (ACC) + IMPF 3FS. Konuşan 1S — 92:12-13'te 1P; adsız (1017); ölçüm iltifât 0 — {1} → {1, 2, 3} kısmi örtüşme, 1P → 1S geçişi sahset'te aynı '1' (924). Hitap 2MP — 92:4'teki 2MP (okuma). 'telezzâ' V. bab — ölçüm bab alanı 'I. bab' (morph VF:1 etiketi, 924). Kök لظي yeni eklendi (1527 → 1528); korpusta tek ayet — ölçüm ★★★ hapaks z=3,28 (formül davranışı). 70:15 ('kellâ innehâ lezâ') (okumada görüldü) aynı harfler morph'ta özel ad, kök etiketi yok — kök sayısına girmiyor (924); 70:15'te ateşin adı / burada ateşin fiili (okuma). Lemma 'enzere' 40 ayet: okunmuş 32, 92:14, henüz okunmamış 7. Lemma 'nâr' 138 ayet: 87:12 (okumada görüldü), okunmuş 89 ayet daha, 92:14, henüz okunmamış 47. Çıpa: âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 3 kelime. نذر [1/1], نور [1/1], لظي [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'fe' + PERF 1S + 2MP + nekre ad + IMPF 3FS; D2 —; D3 70:15 (aynı harfler, özel ad); D4 1S + 2MP + 3FS, sahset ['1', '2', '3'], iltifât 0 (924).\n"
    "◈A — A1 uyaran 1S (adsız); hitap 2MP; ateş; A2 —; A3 konuşan 1S adsız; A4 uyarı.",
 15: "◇ 'lâ yaslâhâ ille'l-eşqâ' — 'lâ' + IMPF 3MS + 3FS + 'illâ' + belirli üstünlük adı (NOM) (ölçüm kip NEG, RES, biçim HASR). 3FS 'hâ' 92:14 'nâr' (okuma). Lemma 'eşqâ' 3 ayet: 87:11 ve 91:12 (okumada görüldü), 92:15 — korpusun üç geçişi de okundu; 87:11'de belirli, 91:12'de iyelikli, burada belirli (okuma). 87:11-12'de 'el-eşqâ' + 'ellezî yaslâ'n-nâr' / burada 'yaslâhâ' + 'el-eşqâ' + 92:16 'ellezî' — aynı üç öğe, sıra farklı (okuma). Lemma 'yaslâ' 13 ayet: 87:12 (okumada görüldü), okunmuş 9 ayet daha, 92:15, henüz okunmamış 2. Kök شقو 12 ayet: okunmuş 11, 92:15. Çıpa: âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 4 kelime, yıldızsız. صلي [1/1], شقو [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'lâ' + IMPF + 3FS + 'illâ' + belirli ad; D2 hasr (ölçüm NEG, RES, HASR); D3 'eşqâ' (87:11, 91:12); 'yaslâ' (87:12); D4 3MS + 3FS, sahset ['3'].\n"
    "◈A — A1 en bedbaht (adsız); ateş; A2 —; A3 konuşan adsız; A4 ateşe girecek olan.",
 16: "◇ 'ellezî kezzebe ve tevellâ' — ilgi 'ellezî' + II. bab PERF 3MS + 've' + V. bab PERF 3MS; 92:15 'el-eşqâ'nın sıfat cümlesi (okuma). Ölçüm iltifât 0. Harekesiz 'kezzebe ve tevellâ' 4 ayet: 20:48 ve 75:32 (okumada görüldü), 92:16, henüz okunmamış 1; 20:48'de 'men' ile, 75:32'de 'lâkin' ile / burada 'ellezî' ile (okuma). Lemma 'kezzebe' sûre içi 92:9 ve 92:16 — iki geçiş de basıldı. Lemma 'tevellâ' 76 ayet: 20:48 ve 75:32 (okumada görüldü), okunmuş 45 ayet daha, 92:16, henüz okunmamış 28. Çıpa: tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 3 kelime, yıldızsız. كذب [2/2], ولي [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'ellezî' + PERF + 've' + PERF; D2 —; D3 'kezzebe ve tevellâ' (20:48, 75:32); D4 3MS, sahset ['3'].\n"
    "◈A — A1 en bedbaht ('ellezî', adsız); A2 —; A3 konuşan adsız; A4 ateşe girecek olanın nitelemesi.",
 17: "◇ 've se-yujennebuhe'l-etqâ' — 've' + 'se' + II. bab IMPF edilgen 3MS + 3FS + belirli üstünlük adı (NOM) (ölçüm kip FUT; EDİLGEN 1/1, ★★★ pas z=5,38 — formül davranışı). Uzak tutan yazılmamış (edilgen, 1017). 3FS 'hâ' 92:14 'nâr' (okuma). Kök جنب: 87:11 ('ve yetecennebuhe'l-eşqâ') (okumada görüldü) — aynı kök + 3FS + belirli üstünlük adı; 87:11'de V. bab etken, özne 'el-eşqâ' / burada II. bab edilgen, özne 'el-etqâ' (okuma). Lemma 'yujennebu' korpusta 1. Kök جنب 31 ayet: 87:11 (okumada görüldü), okunmuş 22 ayet daha, 92:17, henüz okunmamış 7. Lemma 'etqâ' 2 ayet: 49:13 ('etqâkum') (okumada görüldü), 92:17. Kök وقي sûre içi iki geçiş (92:5 'ittaqâ', 92:17 'el-etqâ') — ikisi de basıldı. Çıpa: âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 2 kelime. جنب [1/1], وقي [2/2]. Fâsıla ى. Karşıt çift (aday 1039, okuma): 92:15 'el-eşqâ' / 92:17 'el-etqâ' — en bedbaht / en sakınan; 'yaslâhâ' / 'yujennebuhâ' — ona girer / ondan uzak tutulur (ayetler arası).\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 've' + 'se' + IMPF edilgen + 3FS + belirli ad; D2 gelecek (ölçüm FUT), edilgen; D3 kök جنب + 'hâ' + üstünlük adı (87:11); D4 3MS + 3FS, sahset ['3'].\n"
    "◈A — A1 en sakınan (adsız); ateş; uzak tutan yazılmamış; A2 —; A3 konuşan adsız; A4 ateşten uzak tutulacak olan.",
 18: "◇ 'ellezî yu'tî mâlehû yetezekkâ' — 'ellezî' + IV. bab IMPF 3MS + ad (ACC) + 3MS + V. bab IMPF 3MS; 92:17 'el-etqâ'nın sıfat cümlesi (okuma). 'yetezekkâ' bağlaçsız ikinci fiil — hâl ya da amaç okuması metinde ayrılmıyor (okuma); meal virgülle yan yana bıraktı. Lemma 'tezekkâ' 7 ayet: 87:14 ('qad efleha men tezekkâ') ve 79:18 (okumada görüldü), okunmuş 4 ayet daha, 92:18; 87:14'te 'men tezekkâ' kurtuluşa erer / burada 'ellezî … yetezekkâ' (okuma). Lemma 'mâl' sûre içi 92:11 ve 92:18 — 92:11'de malı ona yarar sağlamaz / burada malını verir (okuma). 92:5 'a'tâ' (kök عطو) / burada 'yu'tî' (kök أتي) — verme iki ayrı kökle (okuma). Lemma 'âtâ' 240 ayet: okunmuş 141, 92:18, henüz okunmamış 98. Çıpa: tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 4 kelime, yıldızsız. أتي [1/1], مول [2/2], زكو [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'ellezî' + IMPF + ad + 3MS + IMPF; D2 —; D3 'tezekkâ' (87:14, 79:18); D4 3MS ×3, sahset ['3'].\n"
    "◈A — A1 en sakınan ('ellezî', adsız); malı; A2 —; A3 konuşan adsız; A4 en sakınanın nitelemesi.",
 19: "◇ 've mâ li-ehadin 'indehû min ni'metin tujzâ' — 've' + 'mâ' (olumsuzluk) + 'li' + nekre ad + ''inde' + 3MS + 'min' + nekre ad + IMPF edilgen 3FS (ölçüm kip NEG; EDİLGEN 1/1, ★★★ pas z=5,38 — formül davranışı). 'ehad' olumsuz cümlede 'hiç kimse' — esmâ e_oto verdi, karar 'degil'; ölçüm 'ORTA, MÜHÜRSÜZ', esma_kayit mühür EVET, bilanço geçerli 0 (1022); ölçüm sayı işareti 'ehad' yanlış pozitif (924). 3MS 'hû' 92:17-18 en sakınan (okuma). Karşılığı veren yazılmamış (edilgen). Ölçüm fâsıla 'KAFİYE KIRILMASI' — son harfte medde işareti harf sayıldı; metinde ى — yanlış pozitif (924); ★★★ kaynağı 'pas', kırık bayrağı da açık (1001). Lemma 'ehad' 72 ayet: okunmuş 49, 92:19, henüz okunmamış 22. Lemma 'ni'meh' 49 ayet: okunmuş 31, 92:19, henüz okunmamış 17. Lemma 'cezâ' (fiil) 71 ayet: okunmuş 52, 92:19, henüz okunmamış 18. Kök نعم ◈B S1 kısıtında izinli lemma değil ('ni'meh') — '—'. Çıpa: tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok. 6 kelime. أحد [1/1], عند [1/1], نعم [1/1], جزي [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 've' + 'mâ' + 'li' + nekre ad + ''inde' + 3MS + 'min' + nekre ad + IMPF edilgen; D2 olumsuzlama (ölçüm NEG), edilgen; D3 —; D4 3MS + 3FS, sahset ['3'].\n"
    "◈A — A1 hiç kimse (nekre); en sakınan ('hû'); A2 —; A3 konuşan adsız; A4 verişin karşılık için olmadığı.",
 20: "◇ 'ille'btiğâ'e vechi rabbihi'l-a'lâ' — 'illâ' + VIII. bab mastar (ACC) + ad (GEN) + Rab (GEN) + 3MS + belirli üstünlük adı (GEN) (ölçüm biçim ISTISNA); 92:19 olumsuzluğunun istisnası (okuma). 3MS 'hi' en sakınan (okuma). 'el-a'lâ' GEN — 'vech' de 'rabb' de GEN, bağlandığı ad i'râbdan okunmuyor — KAPATILAMAZ; meal 'en yüce Rabbinin' ile Rab'a bağladı; esmâ listesinde değil, e_oto vermedi. Ölçüm xref → 13:22 (okumada görüldü): 13:22'de 3MP 'rabbihim', sabreden çoğul / burada 3MS 'rabbihi' + 'el-a'lâ' (okuma). Harekesiz 'ille'btiğâ'e vech' 2 ayet: 92:20 ve henüz okunmamış 1. Lemma 'ibtiğâ'' 13 ayet: 13:22 (okumada görüldü), okunmuş 5 ayet daha, 92:20, henüz okunmamış 6. Lemma 'vech' 66 ayet: 13:22 (okumada görüldü), okunmuş 44 ayet daha, 92:20, henüz okunmamış 20. Lemma 'a'lâ' 9 ayet: 87:1 ('sebbihi'sme rabbike'l-a'lâ') ve 79:24 ('ene rabbukumu'l-a'lâ') (okumada görüldü), okunmuş 6 ayet daha, 92:20; 87:1 ve burada Rab tamlaması, 79:24'te konuşanın kendisi için iddiası (okuma; aday 1041 sûreler arası okuma notu). Lemma 'rabb' 866 ayet: okunmuş 644, 92:20, henüz okunmamış 221. Sûrede Rab tek geçiş (92:20), lafız yok — bütün ayetler basıldı. Ölçüm ★★★ rab z=3,94 — lafızsız kısa ayette tek Rab (formül davranışı). Kök بغي gloss'u ('iffetsizlik; azgınlık; yakışma') 'ibtiğâ'' (arama) anlamına uymuyor (1021). Sûrede üç belirli üstünlük adı: 92:15 'el-eşqâ', 92:17 'el-etqâ', 92:20 'el-a'lâ' (okuma). Çıpa: tutum / Rab (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. 5 kelime. بغي [1/1], وجه [1/1], ربب [1/1], علو [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'illâ' + mastar + ad + Rab + 3MS + belirli ad; D2 istisna (ölçüm ISTISNA); D3 'ibtiğâ'e vechi rabb' (13:22, xref); 'rabb … el-a'lâ' (87:1, 79:24); D4 3MS, sahset ['3'].\n"
    "◈A — A1 Rab (3MS iyelik); en sakınan; A2 —; A3 konuşan adsız; A4 verişin yöneldiği.",
 21: "◇ 've le-sevfe yerdâ' — 've' + 'le' + 'sevfe' + IMPF 3MS (ölçüm kip EMPH, FUT). 'yerdâ' öznesi yazılmamış — en yakın 3MS 92:20 'rabbihi'nin 'hi'si (en sakınan) ya da Rab — KAPATILAMAZ (okuma); meal 'o' ile açık bıraktı. Lemma 'radiye' 31 ayet: okunmuş 21, 92:21, henüz okunmamış 9. Sûre ى ile kapanıyor; sûre boyunca fâsıla tek tip ى (92:3, 11, 19 ölçüm kırıkları medde artefaktı). Çıpa: âhiret / tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 2 kelime, yıldızsız. رضو [1/1]. Fâsıla ى. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 've' + 'le' + 'sevfe' + IMPF; D2 tekit + gelecek (ölçüm EMPH, FUT); D3 —; D4 3MS, sahset ['3'].\n"
    "◈A — A1 hoşnut olacak (özne yazılmamış); A2 —; A3 konuşan adsız; A4 sûre gelecek kipiyle kapanıyor.",
}
MEAL.update(MEAL2); M.update(M2)
