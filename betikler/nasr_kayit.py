# -*- coding: utf-8 -*-
"""nasr_kayit.py — sûre 110 (Nasr) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 110

CIPA = {
 # blok 1-3
 1: dict(kademe=None, olgu=False, cipa=False, not_="'izâ câ'e nasru'llâhi ve'l-feth' — yardım ve fethin gelişi, olay (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'ve ra'eyte'n-nâse yedxulûne fî dîni'llâhi efwâcâ' — insanların dine girişi, olay (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'fe-sebbih bi-hamdi rabbike ve'staxfirhu' — emir, tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 3): [
  "esmâ: e_oto 1 token (110:3 'tevvâb', 7. token) — okuyucu kararı 'ilahi' eklendi (KARAR 728 → 729); ölçüm satırı 'SON konum, MÜHÜRSÜZ' / bilanço geçerli mühür 110:3 (1022); lafız 2 (110:1, 110:2), Rab 1 (110:3)",
  "kök tablosu: blokta yeni kök yok (1544); retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı",
  "yıldız: 110:1 ★★★ kaynak allah (z=3,47), 110:2 ★★ allah (z=2,33), 110:3 ★★ rab (z=2,72) — kısa ayette tek lafız / tek Rab, formül davranışı; kafiye kırığı yok, 1001 vakası yok",
  "fâsıla: metinde ح ا ا; 110:2 ح → ا geçişi ölçümde işaretsiz (924)",
  "biçim (924): ayet 1 harf 38 → harf3 19 (besmele ailesi); 'izâ' şartı ve 'fe' cevabı ölçümde yok (110:1-2 edim haber); iki özneli 3MS fiil (110:1 'nasr' + 'el-feth') özne sayısı ölçümde görünmüyor (sûre 97 dikkatinin eşi)",
  "iltifât: ölçüm 0; sahset 110:1 ['3'] → 110:2-3 ['2', '3'] — 2MS'nin girişi kısmi örtüşme (924, sûre 75 dersi)",
  "söz / gönderge (1017): söz fiili yok, meal tırnaksız; 2MS hitap ve konuşan adsız; yardımın kime olduğu ve 'el-feth'in neyin açılışı olduğu KAPATILAMAZ; 110:3 bağış dilemenin kimin için olduğu yazılmamış",
  "esit2 / nakarat3: blokta yok; xref 110:1 → 61:13, 110:3 → 42:5 (ikisi de AR + meal ile emsal listesinde basıldı); 110:2 bağ YOK",
  "çıpa: L0 / L1 / L2 / L4 yok; olgu=False 3 (olay, olay, emir); tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 109:6 / 110:1 sûre sınırı — fiilsiz paralel isim cümlesiyle kapanış / 'izâ' şartıyla açılış; fâsıla ن → ح; 109 lafızsız ve Rabsız, 110 lafız 2 Rab 1; ardışık sûre okuma bağı kök دين 109:6 / 110:2",
  "aday 1039: ayet içi 0; blok içi 0",
  "aday 1041: kayıt yok — 'tevvâb', lafız ve Rab yalnız ilâhî göndergeyle",
  "korpusta 1 (kayıt): harekesiz kalıp 'nasru'llâhi ve'l-feth', 've ra'eyte'n-nâs', 'yedxulûne fî', 'fe-sebbih bi-hamdi rabbike ve'staxfirhu', 'innehû kâne tevvâbâ'; sûre içi tam sayım: kök أله [2/2], ربب [1/1]",
  "bağ: emsaller 109:6, 61:13, 29:10, 12:76, 24:2, 78:18, 15:98, 40:55, 42:5, 9:118 — hepsi AR + meal ile emsal listesinde basıldı (NFC fark 0); her biri ilgili oturum_lem / oturum_say listesinde doğrulandı",
  "◈K / ◈B: ◈K üç ayette '—'; ◈B 110:2 dolu (tetik أنس), 110:1 ve 110:3 '—'; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 3 ayet; oturum_xy 18 sayım, 0 uyuşmaz",
  "süreç: sûre 110 dosyaları kafirun_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_110.py, oturum dışı; ad 'nasr', harf sınırlı; ISTEK boş; kayıt dosyası CIPA / ARIZA / DUZELTME boş — assert'li; yüzde sabiti maskeli; I['not'] satırı genel değişimden sonra; sûre 96 şablonuyla normalleştirilmiş aile karşılaştırması temiz); sûre 3 ayet — tek blok, ara zip yok",
 ],
}

DUZELTME = {}
