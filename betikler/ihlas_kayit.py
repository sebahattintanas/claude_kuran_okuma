# -*- coding: utf-8 -*-
"""ihlas_kayit.py — sûre 112 (Ihlas) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 112

CIPA = {
 # blok 1-4
 1: dict(kademe=None, olgu=False, cipa=False, not_="'qul huve'llâhu ehad' — ilâhî sıfat (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'allâhu's-samed' — ilâhî sıfat (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'lem yelid ve lem yûled' — tenzih, olumsuz hüküm (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'ve lem yekun lehû kufuwen ehad' — tenzih, olumsuz hüküm (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 4): [
  "esmâ: e_oto 3 token — okuyucu kararları: 112:1 'ehad' ilahi, 112:2 'es-samed' ilahi, 112:4 'ehad' degil (olumsuz cümlede nekre, 'hiç kimse'; sûre 89 dersi) — KARAR 729 → 732; ölçüm mührü 3 (112:1, 112:2, 112:4), bilanço geçerli 2 (112:1, 112:2); ölçüm satırı üçünde de 'SON konum, MÜHÜRSÜZ' (1022); lafız 2 (112:1, 112:2), Rab yok",
  "kök tablosu: iki yeni kök (صمد, كفأ) ölçümde '???' ile göründü — kok_ekle_112 ile eklendi (1546 → 1548; ikisi de korpusta tek ayet); retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı; dikey yeniden koşuldu, karşılık eksiği yok",
  "yıldız: 112:1 ★★★ allah (z=4,47), 112:2 ★★★ allah (z=9,47; hapaks z=3,28 de eşikte), 112:3 ★★ pas (z=2,52), 112:4 ★★★ hapaks (z=3,28) — kısa ayetler, tek lafız, edilgen ve yeni köklerden; formül davranışı; kafiye kırığı yok, 1001 vakası yok",
  "fâsıla: metinde د د د د — tek sınıf; geçiş yok",
  "biçim (924): ayet 1 harf 30 → harf3 11 (besmele ailesi); sayı işareti 'ehad' iki ayette (112:1, 112:4) kök kaynaklı — 112:4'te 'hiç kimse', yanlış pozitif; 112:2 şahıs işareti yok (sahset —)",
  "söz / gönderge (1017): 'qul' sözü 112:1'de açıyor; söz sınırı metinde işaretsiz — meal tırnağı 112:1 / 112:4, 112:2-4'ün söz içi mi anlatıcı sesi mi olduğu KAPATILAMAZ; 2MS hitap ve 'qul' diyen adsız",
  "iltifât: ölçüm 0; sahset 112:1 ['2', '3'] → 112:2 — → 112:3-4 ['3']",
  "◈B: kök ولد (doğurma, 112:3) tetik listesinde değil — satır '—', gözlem ◇'de",
  "esit2 / nakarat3 / xref: blokta dördü de bağ YOK",
  "çıpa: L0 / L1 / L2 / L4 yok; olgu=False 4; tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 111:5 / 112:1 sûre sınırı — fiilsiz isim cümlesiyle kapanış / 'qul' emriyle açılış; fâsıla د → د; 111 lafızsız ve Rabsız, 112 lafız 2 Rab yok",
  "aday 1039: ayet içi 1 (112:3 'yelid' / 'yûled', etken / edilgen); blok içi 0",
  "aday 1041 (kayıt): lemma 'ehad' 112:1 Allah (olumlu haber, ilahi) / 112:4 'hiç kimse' (olumsuz cümlede nekre, degil)",
  "korpusta 1 (kayıt): lemma 'samed', 'kufuv'; harekesiz 'qul huve'llâh', 'allâhu's-samed', 'lem yelid ve lem yûled'; sûre içi tam sayım: kök أله [2/2], أحد [2/2], ولد ikilemesi [1,2/2]",
  "bağ: emsaller 67:29, 59:22, 72:22, 89:25, 17:111, 25:2, 37:152, 19:33 — hepsi AR + meal ile emsal listesinde basıldı (NFC fark 0), her biri ilgili oturum_lem / oturum_say listesinde doğrulandı; 111:5 bu oturumda daha önce basılmıştı, yeniden basılmadı",
  "◈K / ◈B: dört ayette de '—'; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 4 ayet; oturum_xy 10 sayım, 0 uyuşmaz",
  "süreç: sûre 112 dosyaları mesed_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_112.py, oturum dışı; ad 'ihlas', harf sınırlı; dosya eşlemesi ayrı yazıldı, kaynak ≠ hedef assert'li — sûre 111 dersi; ISTEK boş kuruldu, kökler ayrı yamayla; kayıt dosyası boş — assert'li; yüzde sabiti maskeli; I['not'] satırı genel değişimden sonra; sûre 96 şablonuyla aile karşılaştırması temiz); sûre 4 ayet — tek blok, ara zip yok",
 ],
}

DUZELTME = {}
