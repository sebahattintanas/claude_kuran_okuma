# -*- coding: utf-8 -*-
"""insirah_metin_1.py — sûre 94 (İnşirâh) meal ve mercekler (◇ + ◈K ◈B ◈D ◈A).
Arapça sabit YOK: kökler yalnız korpus kök biçimiyle anılır, kelime biçimleri Latin harfle.
Yeni bloklar MEALn/Mn sözlükleri olarak eklenir ve sonda MEAL/M'ye katılır.
Sûre 40'tan itibaren ◇ satırında her ayet 'Karşıt çift (aday 1039, okuma): …' notu taşır — yoksa 'yok'
(okuma kolunun kontrol verisi; seçerek raporlama önlenir)."""
MEAL = {}
M = {}

# ── blok 94:1-8 (2026-10-31) ──
MEAL1 = {
 1: "Senin için göğsünü açmadık mı?",
 2: "Yükünü üzerinden indirdik,",
 3: "o yük ki belini bükmüştü;",
 4: "ve senin için anılmanı yükselttik.",
 5: "Şüphesiz zorlukla birlikte bir kolaylık vardır;",
 6: "şüphesiz zorlukla birlikte bir kolaylık vardır.",
 7: "Öyleyse bitirdiğinde yorulup çalış,",
 8: "ve yalnız Rabbine yönel.",
}
M1 = {
 1: "◇ 'e-lem neşrah leke sadrek' — soru 'e' + 'lem' + IMPF (cezm) 1P + 'li' + 2MS + ad (ACC) + 2MS (ölçüm edim soru, kip INTG, NEG). Konuşan 1P, hitap 2MS — ikisi adsız (1017). Ardışık sûrede 'e-lem' + cezm IMPF + 2MS: 93:6 ('e-lem yecidke yetîmen fe-âvâ') (okumada görüldü) 3MS bulan / burada 1P açan (okuma; aday 1040 okuma bağı). Sûre sınırı: 93:11 ('ve emmâ bi-ni'meti rabbike fe-haddith') (okumada görüldü) sûre sonu → 94:1 soru ile açılış; fâsıla ث → ك (aday 1040, kayıt). Lemma 'şeraha' 5 ayet: 20:25 ('rabbi'şrah lî sadrî') ve 39:22 ('e-fe-men şeraha'llâhu sadrahû …') (okumada görüldü), okunmuş 1 ayet daha, 94:1, henüz okunmamış 1; 20:25'te 1S dua (emir) / 39:22'de lafız özne / burada 1P soru, üçünde de nesne 'sadr' (okuma). Lemma 'sadr' 41 ayet: 20:25 ve 39:22 (okumada görüldü), okunmuş 26 ayet daha, 94:1, henüz okunmamış 12. Organ adı 'sadr' (göğüs) ◈B tetik listesinde değil — '—', gözlem burada. Ölçüm harf 32 → harf3 13 — besmele ailesi (924). Çıpa: organ adı var, açma mecazî; süreç / mekanizma yok — olgu=False; merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 4 kelime, yıldızsız. شرح [1/1], صدر [1/1]. Fâsıla ك. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'e' + 'lem' + IMPF + 'li' + 2MS + ad + 2MS; D2 soru (ölçüm INTG) + olumsuzluk; D3 'şeraha … sadr' (20:25, 39:22); 'e-lem' + 2MS (93:6); D4 1P + 2MS, sahset ['1', '2'].\n"
    "◈A — A1 konuşan 1P (adsız); hitap 2MS; A2 —; A3 konuşan 1P adsız; A4 sûre soruyla açılıyor.",
 2: "◇ 've veda'nâ 'anke vizrek' — 've' + PERF 1P + ''an' + 2MS + ad (ACC) + 2MS. 94:1 sorusuna atıflı haber (okuma). Lemma 'veda'a' 19 ayet: okunmuş 14, 94:2, henüz okunmamış 4. Kök وضع ◈B tetik listesinde (doğurma): 'veda'nâ' (indirdik) da satırı doldurur — doğurma anlamı değil (sûre 88 dikkati). Lemma 'vizr' 11 ayet: 53:38 ('ellâ teziru vâziratun vizra uxrâ') (okumada görüldü), okunmuş 7 ayet daha, 94:2, henüz okunmamış 2; 53:38'de yük başkasına taşıtılmaz / burada 2MS'nin yükü 1P tarafından indirildi (okuma). Çıpa: tutum / söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 3 kelime, yıldızsız. وضع [1/1], وزر [1/1]. Fâsıla ك. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — B2 'veda'nâ' (tetik وضع) — indirme, yükü kaldırma; doğurma anlamı değil; B1, B3, B4 —.\n"
    "◈D — D1 've' + PERF 1P + ''an' + 2MS + ad + 2MS; D2 —; D3 'vizr' (53:38); D4 1P + 2MS, sahset ['1', '2'].\n"
    "◈A — A1 konuşan 1P (adsız); hitap 2MS; yük; A2 —; A3 konuşan 1P adsız; A4 verilen nimet.",
 3: "◇ 'ellezî enqada zahrek' — ilgi 'ellezî' + IV. bab PERF 3MS + ad (ACC) + 2MS; 94:2 'vizr'in sıfat cümlesi (okuma). Ölçüm iltifât 0 — {1, 2} → {2, 3} kısmi örtüşme. Lemma 'enqada' korpusta 1; kök نقض 9 ayet: okunmuş 4, 94:3, henüz okunmamış 4. Lemma 'zahr' 15 ayet: 84:10 ('… verâ'e zahrih') (okumada görüldü), okunmuş 5 ayet daha, 94:3, henüz okunmamış 8; 84:10'da kitabın verildiği yön / burada yükün büktüğü bel (okuma). Organ adı 'zahr' (sırt) ◈B tetik listesinde değil — '—', gözlem burada. Çıpa: organ adı mecazî kullanımda (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 3 kelime, yıldızsız. نقض [1/1], ظهر [1/1]. Fâsıla ك. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'ellezî' + PERF + ad + 2MS; D2 —; D3 —; D4 2MS + 3MS, sahset ['2', '3'].\n"
    "◈A — A1 yük ('ellezî'); hitap 2MS; A2 —; A3 konuşan adsız; A4 yükün niteliği.",
 4: "◇ 've rafa'nâ leke zikrek' — 've' + PERF 1P + 'li' + 2MS + ad (ACC) + 2MS. 94:1 ve 94:4'te 'leke', 94:2'de ''anke' — üç ayette 1P + 2MS'ye yönelik edat + 2MS iyelikli nesne (okuma). Lemma 'rafa'a' 22 ayet: okunmuş 12, 94:4, henüz okunmamış 9. Lemma 'zikr' 71 ayet: 39:22 (okumada görüldü), okunmuş 64 ayet daha, 94:4, henüz okunmamış 5; 39:22'de 'zikri'llâh' (Allah'ın anılması) / burada 2MS'nin anılması (okuma). Fâsıla 94:1-4 ك (2MS iyelik eki). Çıpa: tutum / söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 3 kelime, yıldızsız. رفع [1/1], ذكر [1/1]. Fâsıla ك. Karşıt çift (aday 1039, okuma): 94:2 'veda'nâ' / 94:4 'rafa'nâ' — indirdik / yükselttik (ayetler arası).\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 've' + PERF 1P + 'li' + 2MS + ad + 2MS; D2 —; D3 94:1-2 ile aynı yönelim ('leke', ''anke'); D4 1P + 2MS, sahset ['1', '2'].\n"
    "◈A — A1 konuşan 1P (adsız); hitap 2MS; A2 —; A3 konuşan 1P adsız; A4 verilen nimet dizisi kapanıyor.",
 5: "◇ 'fe-inne ma'a'l-'usri yusrâ' — 'fe' + 'inne' + 'ma'a' + belirli ad (GEN) + nekre ad (ACC); şahıs işareti yok (ölçüm sahset —). 'el-'usr' belirli / 'yusr' nekre (okuma). Ölçüm esit2 TAM → 94:6 ve nakarat3 — sûre içi tekrar, fark yalnız baştaki 'fe' (okuma). 65:7 ('… seyec'alu'llâhu ba'de 'usrin yusrâ') (okumada görüldü) — iki lemma birlikte: 65:7'de 'ba'de' (ardından) ve ikisi nekre / burada 'ma'a' (birlikte) ve ''usr' belirli (okuma). Ardışık sûre: 92:7 ve 92:10 'li'l-yusrâ' / 'li'l-'usrâ' (okumada görüldü) fu'lâ biçimi / burada fu'l biçimi (okuma; aday 1040 okuma bağı). Lemma ''usr' 5 ayet: 65:7 (okumada görüldü), okunmuş 1 ayet daha, sûre içi 94:5 ve 94:6, henüz okunmamış 1. Lemma 'yusr' 7 ayet: 65:7 (okumada görüldü), okunmuş 3 ayet daha, sûre içi 94:5 ve 94:6, henüz okunmamış 1. Kök عسر 12 ayet: 92:10, 74:9 ve 65:7 (okumada görüldü), okunmuş 5 ayet daha, sûre içi 94:5 ve 94:6, henüz okunmamış 2. Kök يسر 40 ayet: 92:7, 92:10, 87:8 ve 65:7 (okumada görüldü), okunmuş 26 ayet daha, sûre içi 94:5 ve 94:6, henüz okunmamış 8. Fâsıla ك → ا (ölçüm kırık işaretlemedi, 924). Çıpa: tutum / söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 4 kelime, yıldızsız. عسر [1/2], يسر [1/2]. Fâsıla ا. Karşıt çift (aday 1039, okuma): ''usr' / 'yusr' — zorluk / kolaylık (ayet içi).\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'fe' + 'inne' + 'ma'a' + belirli ad + nekre ad; D2 tekit ('inne'); D3 esit2 TAM → 94:6; 'usr … yusr' (65:7); D4 şahıs işareti yok.\n"
    "◈A — A1 zorluk, kolaylık; A2 —; A3 konuşan adsız; A4 genel önerme.",
 6: "◇ 'inne ma'a'l-'usri yusrâ' — 'inne' + 'ma'a' + belirli ad (GEN) + nekre ad (ACC); 94:5'in 'fe'siz tekrarı (ölçüm esit2 TAM → 94:5, nakarat3). Ölçüm harf 14 → harf3 13, isaret 1; 94:5 harf3 14 — fark 'fe' (okuma). Lemma ''usr' ve 'yusr' sûre içi iki geçişin ikisi de basıldı. Çıpa: tutum / söz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 4 kelime, yıldızsız. عسر [2/2], يسر [2/2]. Fâsıla ا. Karşıt çift (aday 1039, okuma): ''usr' / 'yusr' — zorluk / kolaylık (ayet içi); 94:5 ile aynı çift, tekrar.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'inne' + 'ma'a' + belirli ad + nekre ad; D2 tekit ('inne'); D3 esit2 TAM → 94:5; D4 şahıs işareti yok.\n"
    "◈A — A1 zorluk, kolaylık; A2 —; A3 konuşan adsız; A4 önermenin tekrarı.",
 7: "◇ 'fe-izâ feraġte fe'nsab' — 'fe' + 'izâ' + PERF 2MS + 'fe' + IMPV 2MS (ölçüm edim emir, kip IMPV). Neyi bitirdiği yazılmamış (okuma). Lemma 'feraġa' 2 ayet: 55:31 ('se-nefruğu lekum eyyuhe's-saqalân') (okumada görüldü), 94:7 — 55:31'de 1P konuşan / burada 2MS (okuma). Morph lemma etiketi ('nusibet') 2 ayet: 88:19 ('… keyfe nusibet') (okumada görüldü), 94:7 — 88:19'da dağların dikilmesi (edilgen) / burada 2MS'ye emir; aynı etiket iki anlamda (924). Kök نصب gloss'u ('pay, nasip; dikili taş; yorgunluk') iki anlamı da taşıyor. Fâsıla ا → ب (ölçüm kırık işaretlemedi, 924). Çıpa: buyruk (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Lafız ve Rab yok; esmâ yok. 3 kelime, yıldızsız. فرغ [1/1], نصب [1/1]. Fâsıla ب. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 'fe' + 'izâ' + PERF + 'fe' + IMPV; D2 emir (ölçüm IMPV); D3 'feraġa' (55:31); D4 2MS, sahset ['2'].\n"
    "◈A — A1 hitap 2MS; A2 —; A3 konuşan adsız; A4 buyruk.",
 8: "◇ 've ilâ rabbike fe'rġab' — 've' + 'ilâ' + Rab (GEN) + 2MS + 'fe' + IMPV 2MS (ölçüm kip IMPV); 'ilâ rabbike' fiilden önce (okuma). Sûrenin tek Rab'ı, lafız yok — bütün ayetler basıldı. Kök رغب 8 ayet: 68:32 ('… innâ ilâ rabbinâ râğibûn') ve 9:59 ('… innâ ile'llâhi râğibûn') (okumada görüldü), okunmuş 3 ayet daha, 94:8, henüz okunmamış 2; 68:32'de 1P söz 'ilâ rabbinâ' + ad / 9:59'da 'ile'llâh' + ad / burada 'ilâ rabbike' + emir (okuma). Lemma 'raġıbe' 4 ayet: okunmuş 1, 94:8, henüz okunmamış 2. Lemma 'rabb' 866 ayet: okunmuş 648, 94:8, henüz okunmamış 217. Ölçüm ★★★ rab z=6,78 — lafızsız kısa ayette tek Rab (formül davranışı). Çıpa: buyruk (olgu=False); merdiven uygulanmadı; tarayıcı vermedi. Esmâ yok. 3 kelime. ربب [1/1], رغب [1/1]. Fâsıla ب. Karşıt çift (aday 1039, okuma): yok.\n"
    "◈K — —\n"
    "◈B — —\n"
    "◈D — D1 've' + 'ilâ' + Rab + 2MS + 'fe' + IMPV; D2 emir (ölçüm IMPV); D3 'ilâ rabb' + kök رغب (68:32); D4 2MS, sahset ['2'].\n"
    "◈A — A1 hitap 2MS; Rab; A2 —; A3 konuşan adsız; A4 sûre emirle kapanıyor.",
}
MEAL.update(MEAL1); M.update(M1)
