# -*- coding: utf-8 -*-
"""felak_kayit.py — sûre 113 (Felak) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 113

CIPA = {
 # blok 1-5
 1: dict(kademe=None, olgu=False, cipa=False, not_="'qul e'ûzu bi-rabbi'l-feleq' — sığınma (olgu=False); 'el-feleq' KAPATILAMAZ; merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'min şerri mâ xalaq' — yaratılanların şerri, genel (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'ğâsiqin izâ vaqab' — gönderge adsız, merdiven uygulanmaz (olgu=False); tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'en-neffâsâti fi'l-'uqad' — gönderge adsız, merdiven uygulanmaz (olgu=False); tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'hâsidin izâ hased' — gönderge adsız, merdiven uygulanmaz (olgu=False); tarayıcı vermedi"),
}

ARIZA = {
 (1, 5): [
  "esmâ: e_oto 0 token; KARAR değişmedi (732); lafız yok, Rab 1 (113:1 'rabbi'l-feleq'); mühür yok",
  "kök tablosu: iki yeni kök (نفث, وقب) ölçümde '???' ile göründü — kok_ekle_113 ile eklendi (1548 → 1550; ikisi de korpusta tek ayet); retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı; dikey yeniden koşuldu, karşılık eksiği yok",
  "yıldız: 113:1 ★★★ rab (z=5,01), 113:3 ★★★ hapaks (وقب), 113:4 ★★★ hapaks (نفث) — tek Rab ve yeni kökler, formül davranışı; 113:2, 113:5 yıldızsız; kafiye kırığı yok, 1001 vakası yok",
  "fâsıla: metinde ق ق ب د د; 113:3 ق → ب ve 113:4 ب → د geçişleri ölçümde işaretsiz (924)",
  "biçim (924): ayet 1 harf 33 → harf3 14 (besmele ailesi); 113:4 şahıs işareti yok (sahset —)",
  "iltifât (924): ölçüm 113:2'de 1 — sahset ['1', '2'] → ['3']; 'mâ xalaq' ilgi cümlesinin fiili, hitap ve konuşan değişmiyor (sûre 87 dikkatinin eşi)",
  "söz / gönderge (1017): 'qul' sözü 113:1'de açıyor; 113:2-5 'min şerri' öbekleri 'e'ûzu'ya bağlı — söz sınırı sözdizimiyle belli, meal tırnağı 113:1 / 113:5; hitap, 'qul' diyen ve söz içi 1S adsız; 'el-feleq', 'ğâsiq', 'en-neffâsât', 'hâsid' adsız — KAPATILAMAZ",
  "xref: 113:1 → 40:27 (basıldı) ve sûre 114'ün ilk ayeti (henüz okunmadı); esit2 / nakarat3 yok",
  "çıpa: L0 / L1 / L2 / L4 yok; olgu=False 5; 113:3-5 gönderge adsız (merdiven uygulanmaz); tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 112:4 / 113:1 sûre sınırı — olumsuz isim cümlesiyle kapanış / 'qul' emriyle açılış; fâsıla د → ق; 112 lafız 2 Rab yok, 113 lafızsız Rab 1; okuma bağı: ardışık iki sûre 'qul' ile açılıyor (112:1 / 113:1)",
  "aday 1039: ayet içi 0; blok içi 0",
  "aday 1041: kayıt yok — Rab tek geçiş, lafız yok",
  "korpusta 1 (kayıt): lemma 'feleq', 'ğâsiq', 'vaqabe', 'neffâse', 'hâsid'; harekesiz 'şerri mâ xalaq', 'ğâsiqin izâ', 'fi'l-'uqad', 'izâ hased'; sûre içi tam sayım: kök شرر [4/4], ربب [1/1], حسد ikilemesi [1,2/2]",
  "bağ: emsaller 40:27, 23:97, 72:6, 26:63, 17:78, 20:27, 48:15, 70:20 — hepsi AR + meal ile emsal listesinde basıldı (NFC fark 0), her biri ilgili oturum_lem / oturum_say listesinde doğrulandı; 112:1, 112:4, 25:2, 50:16 bu oturumda daha önce basılmıştı, yeniden basılmadı",
  "◈K / ◈B: ◈K beş ayette '—' (kök غسق tetik listesinde değil — gözlem ◇'de); ◈B 113:2 dolu (tetik خلق) — tetik ön kuru koşusu kayıttan önce '—' yazılmış satırı yakaladı, satır dolduruldu; diğer dört ayette '—'; ikinci ön kuru koşu 0 uyuşmaz, 5 ayet (geçici modül, silindi); oturum_xy 15 sayım, 0 uyuşmaz",
  "süreç: sûre 113 dosyaları ihlas_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_113.py, oturum dışı; ad 'felak', harf sınırlı; dosya eşlemesi ayrı, kaynak ≠ hedef assert'li; ISTEK boş kuruldu, kökler ayrı yamayla; kayıt dosyası boş — assert'li; yüzde sabiti maskeli; I['not'] satırı genel değişimden sonra; sûre 96 şablonuyla aile karşılaştırması temiz); sûre 5 ayet — tek blok, ara zip yok",
 ],
}

DUZELTME = {}
