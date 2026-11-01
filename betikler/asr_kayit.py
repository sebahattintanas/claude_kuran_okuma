# -*- coding: utf-8 -*-
"""asr_kayit.py — sûre 103 (Asr) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 103

CIPA = {
 # blok 1-3
 1: dict(kademe='L0', olgu=True, cipa=False, not_="'ve'l-'asr' — yemin edilen vakit / zaman adı (anlamı KAPATILAMAZ); iki okumada da süreç yok — L0 (93:1 kaydı emsali); tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'inne'l-insâne le-fî xusr' — ziyan, durum (olgu=False; 100:6 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'illa'llezîne âmenû …' — iman, amel, tavsiye — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 3): [
  "esmâ: e_oto 0 token; KARAR değişmedi (728); lafız yok, Rab yok — lafızsız ve Rabsız sûre (sûre 101 ve 102 gibi); mühür yok",
  "kök tablosu: blokta yeni kök yok (1537); retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı",
  "yıldız: blokta yıldız yok (üç ayet yıldızsız)",
  "biçim (924): ayet 1 harf 25 → harf3 6 (besmele ailesi); QASEM 103:1, EMPH 103:2, ISTISNA 103:3 ölçümde var",
  "fâsıla: ölçüm R 3 (103:1-3 ر) — geçiş yok",
  "iltifât: ölçüm 0; sahset 103:1 ve 103:2 — (şahıs işareti yok), 103:3 ['3']",
  "adsız gönderge (1017): yemin eden ve konuşan adsız; 103:3 'ellezîne' adsız — adlandırılmadı",
  "çıpa: L0 1 (103:1 — yemin edilen vakit / zaman adı, anlamı KAPATILAMAZ); L1 / L2 / L4 yok; olgu=False 2; tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 102:8 / 103:1 sûre sınırı — sorguyla kapanış / yeminle açılış; fâsıla م → ر; iki sûre de lafızsız ve Rabsız",
  "aday 1039: ayet içi 0; blok içi 0 (103:2 'xusr' karşısında metinde ikinci uç yok; 'haqq' / 'sabr' karşıt değil)",
  "aday 1041: kayıt yok — lafız / Rab yok",
  "korpusta 1 (kayıt): lemma ''asr'; kalıp 've'l-'asr', 'inne'l-insâne le-fî', 've tevâsav bi'l-haqq'; korpusun iki geçişi, ikisi de basıldı: lemma 'xusr' (65:9, 103:2), kalıp 've tevâsav bi's-sabr' (90:17, 103:3)",
  "bağ: kalıp / lemma eşleri okumayla (102:8, 93:1, 95:4, 95:5, 95:6, 84:25, 96:6, 100:6, 70:19, 70:20, 70:21, 70:22, 65:9, 90:17, 51:53, 78:14); hepsi AR + meal ile emsal listesinde basıldı",
  "◈K / ◈B: ◈K boş (kök عصر tetik listesinde değil — gözlem ◇'de); ◈B dolu 103:2 (أنس); tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 3 ayet; oturum_xy 9 sayım, 0 uyuşmaz",
  "süreç: sûre 103 dosyaları tekasur_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_103.py, oturum dışı; ad 'asr'; ilerleme yüzdesi sabiti maskelendi; sûre 96 şablonuyla normalleştirilmiş aile karşılaştırması temiz); sûre 3 ayet — tek blok, ara zip yok",
 ],
}

DUZELTME = {}
