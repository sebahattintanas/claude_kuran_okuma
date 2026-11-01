# -*- coding: utf-8 -*-
"""nas_kayit.py — sûre 114 (Nas) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 114

CIPA = {
 # blok 1-6
 1: dict(kademe=None, olgu=False, cipa=False, not_="'qul e'ûzu bi-rabbi'n-nâs' — sığınma (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'meliki'n-nâs' — ilâhî sıfat (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'ilâhi'n-nâs' — ilâhî sıfat (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'min şerri'l-vesvâsi'l-xannâs' — gönderge adsız, merdiven uygulanmaz (olgu=False); tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'ellezî yuvesvisu fî sudûri'n-nâs' — vesvese (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'mine'l-cinneti ve'n-nâs' — sınıf adları (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 6): [
  "esmâ: e_oto 1 token (114:2 'melik', 1. token) — okuyucu kararı 'ilahi' (KARAR 732 → 733); ölçüm satırı '1. sırada, SON konum, MÜHÜRSÜZ' — konum etiketi iki kelimelik ayette metinle uyuşmuyor (son kelime 'en-nâs'); bilanço geçerli mühür 114:2 (1022); 'ilâh' (114:3) esmâ listesinde değil; lafız yok, Rab 1 (114:1)",
  "kök tablosu: blokta yeni kök yok (1550); retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı",
  "yıldız: yalnız 114:1 ★★★ rab (z=5,01) — kısa ayette tek Rab, formül davranışı; diğer 5 ayet yıldızsız; kafiye kırığı yok, 1001 vakası yok",
  "fâsıla: metinde س س س س س س — 114:1-3, 5, 6 aynı kelime 'en-nâs', 114:4 'el-xannâs'; geçiş yok",
  "biçim (924): ayet 1 harf 33 → harf3 14 (besmele ailesi); 114:2-4 ve 114:6 şahıs işareti yok (sahset —); harekesiz kalıp 'mine'l-cinne' imlâda 'cinne' / 'cenne' ayırmıyor — kalıp sayısı verilmedi (sûre 41 dersi)",
  "iltifât (924): ölçüm 114:5'te 1 — 'ellezî yuvesvisu' ilgi cümlesinin fiili; hitap ve konuşan değişmiyor (sûre 87, 113 eşi)",
  "söz / gönderge (1017): 'qul' sözü 114:1'de açıyor; 114:2-3 atıfsız tamlamalar, 114:4-6 'min şerri' öbeği 'e'ûzu'ya bağlı — söz sınırı sözdizimiyle belli, meal tırnağı 114:1 / 114:6; hitap, 'qul' diyen ve söz içi 1S adsız; 'el-vesvâs' adsız; 114:6 'min' öbeğinin bağlandığı yer ('el-vesvâs' / 'en-nâs') KAPATILAMAZ",
  "xref: 114:1 → 40:27 ve 113:1 (ikisi de bu oturumda basıldı); esit2 / nakarat3 yok",
  "çıpa: L0 / L1 / L2 / L4 yok; olgu=False 6; 114:4 gönderge adsız; tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 113:5 / 114:1 sûre sınırı — haset öbeğiyle kapanış / 'qul e'ûzu bi-rabbi'n-nâs' ile açılış; fâsıla د → س; iki sûre de lafızsız, Rab 1; okuma bağı: 113:1 / 114:1 aynı açılış (harekesiz 'qul e'ûzu bi-rabb' korpusun iki geçişi), 113:2-5 / 114:4 'min şerri'. KORPUS SONU: 114:6 okuma sırasının son ayeti — 1040 için 'korpus sonu' olarak not edildi; sûre 1'e geri bağ kurulmadı",
  "aday 1039: ayet içi 1 (114:6 'el-cinne' / 'en-nâs'); blok içi 0",
  "aday 1041: sûre içi kayıt yok — Rab, 'melik', 'ilâh' yalnız ilâhî göndergeyle; sûreler arası okuma notu: lemma 'melik' 20:114 Allah / 12:43, 12:76 kral; lemma 'ilâh' 59:22 / 11:101 'âlihetuhum'",
  "korpusta 1 (kayıt): lemma 'vesvâs', 'xannâs'; harekesiz 'rabbi'n-nâs', 'meliki'n-nâs', 'ilâhi'n-nâs', 'fî sudûri'n-nâs'; sûre içi tam sayım: kök أنس [5/5], وسوس [2/2], ربب [1/1]",
  "bağ: emsaller 20:114, 12:43, 81:15, 20:120, 11:119 — hepsi AR + meal ile emsal listesinde basıldı (NFC fark 0), her biri ilgili oturum_lem / oturum_say listesinde doğrulandı; 113:1, 113:5, 40:27, 23:97, 72:6, 50:16, 29:10, 110:2, 12:76, 59:22, 11:101 bu oturumda daha önce basılmıştı, yeniden basılmadı",
  "◈K / ◈B: ◈K altı ayette '—'; ◈B 114:1, 2, 3, 5, 6 dolu (tetik أنس, 'en-nâs'), 114:4 '—'; 'sudûr' (kök صدر) tetik dışı organ adı — gözlem ◇'de; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 6 ayet; oturum_xy 18 sayım, 0 uyuşmaz",
  "süreç: sûre 114 dosyaları felak_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_114.py, oturum dışı; ad 'nas', harf sınırlı, yalnız felak → nas yönünde — sûre 110 'nasr' dosyalarına dokunulmadı; dosya eşlemesi ayrı, kaynak ≠ hedef assert'li; ISTEK boş; kayıt dosyası boş — assert'li; yüzde sabiti maskeli; I['not'] 'korpus sonu' satırı genel değişimden sonra; sûre 96 şablonuyla aile karşılaştırması temiz); sûre 6 ayet — tek blok, ara zip yok",
 ],
}

DUZELTME = {}
