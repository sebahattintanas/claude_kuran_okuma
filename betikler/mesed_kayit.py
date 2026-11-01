# -*- coding: utf-8 -*-
"""mesed_kayit.py — sûre 111 (Mesed) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 111

CIPA = {
 # blok 1-5
 1: dict(kademe=None, olgu=False, cipa=False, not_="'tebbet yedâ ebî lehebin ve tebb' — kişiye yönelik hüküm (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'mâ ağnâ 'anhu mâluhû ve mâ keseb' — mal ve kazancın yararsızlığı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'se-yaslâ nâran zâte leheb' — âhirette ateşe girme (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'ve'mra'etuhû hammâlete'l-hatab' — kişi nitelemesi (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'fî cîdihâ hablun min mesed' — ceza tasviri, organ adı + nesne (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 5): [
  "esmâ: e_oto 0 token; KARAR değişmedi (729); lafız yok, Rab yok — lafızsız ve Rabsız sûre; mühür yok",
  "kök tablosu: iki yeni kök (جيد, مسد) ölçümde '???' ile göründü — kok_ekle_111 ile eklendi (1544 → 1546; ikisi de korpusta tek ayet); retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı; dikey yeniden koşuldu, karşılık eksiği yok",
  "yıldız: yalnız 111:5 ★★★ kaynak hapaks (z=6,79) — yeni eklenen iki kökten, formül davranışı; diğer 4 ayet yıldızsız; kafiye kırığı yok, 1001 vakası yok",
  "fâsıla: metinde ب ب ب ب د; 111:5 ب → د geçişi ölçümde işaretsiz (924)",
  "biçim (924): ayet 1 harf 35 → harf3 15 (besmele ailesi); 111:1 iki PERF ölçümde ikisi de haber (dilek / haber ayrımı yok); morph 'ağnâ' (111:2) VF:1 — ölçüm 'I. bab', fiil IV. bab (sûre 92 dikkatinin eşi); 111:2 iki özneli 3MS fiil özne sayısı görünmüyor",
  "aktör (924): 111:1 künyeyle anılan kişi ('ebî leheb') ölçüm aktör alanında yok; 111:4 'imrae' adsız aktör",
  "iltifât: ölçüm 0; sahset bütün ayetlerde ['3'] — 3FS / 3MS dönüşleri (111:1 'yedâ' / 3MS, 111:4-5 kadın 3FS) ölçümde aynı '3' (924)",
  "gönderge (1017): konuşan adsız, hitap yok; kişi metinde yalnız künyeyle; kadın 'imra'atuhû' iyelikle, adsız; 111:4 'imra'atuhû'nun 111:3 fiiline atıflı mı 111:5'in başı mı olduğu KAPATILAMAZ",
  "esit2 / nakarat3 / xref: blokta beşi de bağ YOK",
  "çıpa: L0 / L1 / L2 / L4 yok; olgu=False 5; tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 110:3 / 111:1 sûre sınırı — Rabbin 'tevvâb' sıfatıyla kapanış / PERF 3FS 'tebbet' ile açılış; fâsıla ا → ب; 110 lafız 2 Rab 1, 111 lafızsız ve Rabsız",
  "aday 1039: ayet içi 0; blok içi 0",
  "aday 1041: kayıt yok — lafız / Rab yok; okuma notu: lemma 'leheb' sûre içinde künyede (111:1) ve ateş niteliğinde (111:3)",
  "korpusta 1 (kayıt): lemma 'tebbe' (iki token, tek ayet), 'hammâle', 'cîd', 'mesed'; harekesiz 'ebî leheb', 'hablun min mesed'; sûre içi tam sayım: kök لهب [2/2], تبب ikilemesi [1,2/2]",
  "bağ: emsaller 77:31, 11:101, 69:28, 92:11, 15:84, 88:4, 85:5, 72:15, 66:10, 50:16 — hepsi AR + meal ile emsal listesinde basıldı (NFC fark 0), her biri ilgili oturum_lem / oturum_say listesinde doğrulandı; 110:3 bu oturumda daha önce basılmıştı, yeniden basılmadı; 11:101 'ağnet' ayrı lemma etiketinde — 'ağnâ' sayımına katılmadı",
  "◈K / ◈B: ◈K beş ayette '—'; ◈B 111:1 dolu (tetik يدي), 111:4 dolu (tetik حمل, gebelik anlamı değil), diğer üç ayette '—'; 'cîd' (boyun) tetik listesinde değil — gözlem ◇'de; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 5 ayet; oturum_xy 17 sayım, 0 uyuşmaz",
  "süreç: sûre 111 dosyaları nasr_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_111.py, oturum dışı; ad 'mesed', harf sınırlı; ISTEK boş kuruldu, kökler ayrı yamayla eklendi; kayıt dosyası boş — assert'li; yüzde sabiti maskeli; I['not'] satırı genel değişimden sonra; sûre 96 şablonuyla aile karşılaştırması temiz); iskele türetilirken dosya eşlemesinin kaynak adları da değişti — koşudan önce yakalandı, düzeltildi; sûre 5 ayet — tek blok, ara zip yok",
 ],
}

DUZELTME = {}
