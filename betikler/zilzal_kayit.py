# -*- coding: utf-8 -*-
"""zilzal_kayit.py — sûre 99 (Zilzal) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 99

CIPA = {
 # blok 1-8
 1: dict(kademe='L1', olgu=True, cipa=False, not_="'izâ zulzileti'l-ardu zilzâlehâ' — yer + sarsılma, mastarla pekiştirilmiş; büyüklük / süre / mekanizma yok — L1 (56:4 kaydı emsali; aynı iskeletli 89:21 kaydı olgu=False — ayrışma ARIZA'da); tarayıcı vermedi"),
 2: dict(kademe='L1', olgu=True, cipa=False, not_="'ve exraceti'l-ardu esqâlehâ' — yerin içindekini çıkarması, âhirette kozmik olay — L1 (84:4 kaydı emsali); tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'ve qâle'l-insânu mâ lehâ' — söz, soru (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'yevme'izin tuhaddisu axbârehâ' — yerin anlatması, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'bi-enne rabbeke evhâ lehâ' — vahiy (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'yevme'izin yasduru'n-nâsu eştâtâ' — âhirette insanların çıkışı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe='L1', olgu=False, cipa=False, not_="'misqâle zerratin xayran' — zerre ağırlığı ölçü birimi, iddia amele dair (34:3 kaydı emsali); tarayıcı vermedi"),
 8: dict(kademe='L1', olgu=False, cipa=False, not_="'misqâle zerratin şerran' — zerre ağırlığı ölçü birimi, iddia amele dair (34:3 kaydı emsali); tarayıcı vermedi"),
}

ARIZA = {
 (1, 8): [
  "esmâ: e_oto 0 token; KARAR değişmedi (726); lafız yok, Rab 1 (99:5) — sûrenin tek Rab geçişi; mühür yok",
  "kök tablosu: blokta yeni kök yok (1532); retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı",
  "gloss (1021): kök صدر gloss'u 'göğüs' — 99:6 'yasduru' (çıkmak, dönmek) anlamını vermiyor; lemma korpusta 1",
  "yıldız: ★★★ 99:1 pas z=5,38 (kısa tek fiilli edilgen); ★★★ 99:5 rab z=5,01 (lafızsız kısa ayette tek Rab); ★★ 99:6 pas z=2,52 — formül davranışı",
  "fâsıla (924): metin ا 5 (99:1-5, hepsi -hâ), م 1 (99:6), ه 2 (99:7-8); ölçüm A 5, N 1, H 2 — ا → م ve م → ه geçişleri kafiye kırığı işaretlenmedi",
  "biçim (924): ayet 1 harf 39 → harf3 20 (besmele ailesi); 99:1 fiil + aynı kökten mastar — kök ikilemesi var, mm2 yok (sûre 89 dikkati); 'izâ' şart dizisi (99:1-3) ve cevabı (99:4), 99:5 'bi' gerekçesi, 99:6 'li' ta'lîli biçim alanında görünmüyor",
  "iltifât: ölçüm 0; 99:5 2MS'nin girişi {3} → {2, 3} kısmi örtüşme",
  "adsız gönderge (1017): sarsan (99:1, edilgen), hitap 2MS (99:5), gösteren (99:6, edilgen), 'men' (99:7-8) — adlandırılmadı; 99:4 'tuhaddisu' öznesi 3FS, ad yazılmamış — 'el-ard' okuma",
  "çıpa: L1 4 (99:1 — 56:4 kaydı emsali; 99:2 — 84:4 kaydı emsali; 99:7, 99:8 ölçü birimi, olgu=False — 34:3 kaydı emsali); olgu=False 6; tarayıcı v4 blokta aday vermedi",
  "çıpa sınıflama ayrışması (kayıt): aynı iskelet ('izâ' + edilgen PERF 3FS + 'el-ard' + aynı kökten mastar) 56:4'te L1 olgu=True, 89:21'de olgu=False kaydedilmiş; 99:1 için 56:4 emsali alındı — iki eski kayıt değiştirilmedi",
  "aday 1040 (kayıt): 98:8 / 99:1 sûre sınırı — Rabbinden korkana işaretle kapanış / 'izâ' şartıyla açılış; fâsıla ه → ا; sûre 98 lafız 3 Rab 2, sûre 99 lafızsız Rab 1; ardışık sûre okuma bağı 98:6-7 / 99:7-8 'şerr' / 'xayr' — sıra ters",
  "aday 1039: ayet içi 0; blok içi 1 (99:7 / 99:8 'xayran' / 'şerran')",
  "aday 1041: sûre içi kayıt yok — lafız yok, Rab 1; 'evhâ'nın öznesi Rab, alıcı yer",
  "korpusun iki geçişi, ikisi de basıldı: lemma 'zilzâl' (33:11, 99:1); lemma 'eştât' (24:61, 99:6); korpusta 1: lemma 'yasduru' (99:6)",
  "bağ: kalıp / lemma eşleri okumayla (98:8, 33:11, 22:1, 56:4, 89:21, 84:3, 84:4, 16:7, 93:11, 47:31, 16:68, 41:12, 24:61, 34:3, 21:47, 10:61, 98:6, 98:7); 98:6-8 bu oturumda sûre 98'de basılmıştı, yeniden basılmadı; diğerleri AR + meal ile basıldı",
  "◈K / ◈B: ◈K dolu 99:1, 99:2 (أرض), 99:4, 99:6 (يوم); ◈B dolu 99:3, 99:6 (أنس); tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 8 ayet; oturum_xy 33 sayım, 0 uyuşmaz",
  "süreç: sûre 99 dosyaları beyyine_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_99.py, oturum dışı; ad 'zilzal'; set değişkeni ASCII 'ZILZAL'); sûre 8 ayet — tek blok, ara zip yok",
 ],
}

DUZELTME = {}
