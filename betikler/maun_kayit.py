# -*- coding: utf-8 -*-
"""maun_kayit.py — sûre 107 (Maun) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 107

CIPA = {
 # blok 1-7
 1: dict(kademe=None, olgu=False, cipa=False, not_="'e-ra'eyte'llezî yukezzibu bi'd-dîn' — yalanlama, tutum (olgu=False; 96:9 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'fe-zâlike'llezî yedu''u'l-yetîm' — tutum (olgu=False; 89:17 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'ve lâ yahuddu 'alâ ta'âmi'l-miskîn' — tutum (olgu=False; 89:18 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'fe-veylun li'l-musallîn' — kınama (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'ellezîne hum 'an salâtihim sâhûn' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'ellezîne hum yurâ'ûn' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'ve yemne'ûne'l-mâ'ûn' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 7): [
  "esmâ: e_oto 0 token; KARAR değişmedi (728); lafız yok, Rab yok — lafızsız ve Rabsız sûre; mühür yok",
  "kök tablosu: blokta yeni kök yok (1541); retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı",
  "yıldız: blokta yıldız yok (yedi ayet yıldızsız)",
  "biçim (924): ayet 1 harf 38 → harf3 19 (besmele ailesi); INTG 107:1, NEG 107:3 ölçümde var",
  "fâsıla (924): ölçüm N 7 — metinde 107:2 م, diğerleri ن; ن / م tek N sınıfında, geçiş görünmüyor",
  "iltifât: ölçüm 0; sahset 107:1 ['2', '3'], 107:2-3 ['3'], 107:5-7 ['3'], 107:4 —",
  "gönderge (924): 3MS ('ellezî', 107:1-3) → çoğul ('el-musallîn', 107:4; 3MP 107:5-7) ölçümde '3' / '3', görünmüyor",
  "esit2 (araç tekrarı): 107:3 satırında 69:34 TAM iki kez yazılıyor",
  "adsız gönderge (1017): 2MS hitap adsız; yalanlayan ve namaz kılanlar adsız; konuşan adsız",
  "çıpa: L0 / L1 / L2 / L4 yok; olgu=False 7 (tutum, kınama); tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 106:4 / 107:1 sûre sınırı — Rab'ın doyurmasıyla kapanış / 'e-ra'eyte' sorusuyla açılış; fâsıla ف → ن; 106 Rab 1, 107 lafızsız ve Rabsız; okuma bağı kök طعم 106:4 / 107:3",
  "aday 1039: ayet içi 0; blok içi 0",
  "aday 1041: kayıt yok — lafız / Rab yok",
  "korpusta 1 (kayıt): lemma 'yedu''u', 'mâ'ûn'; kalıp 'yukezzibu bi'd-dîn', 'fe-veylun li'l-musallîn'; korpusun iki geçişi, ikisi de basıldı: kalıp 'e-ra'eyte'llezî' (96:9, 107:1), kalıp 've lâ yahuddu 'alâ ta'âmi'l-miskîn' (69:34, 107:3), lemma 'sâhî' (51:11, 107:5)",
  "bağ: kalıp / lemma eşleri okumayla (96:9, 89:17, 89:18, 69:34, 70:23, 51:11); hepsi AR + meal ile emsal listesinde basıldı; 70:22 ve 106:4 bu oturumda daha önce basılmıştı, yeniden basılmadı",
  "◈K / ◈B: ikisi de yedi ayette '—'; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 7 ayet; oturum_xy 14 sayım, 0 uyuşmaz",
  "süreç: sûre 107 dosyaları kureys_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_107.py, oturum dışı; ad 'maun'; kok_ekle ISTEK iskele içinde boş kuruldu; ilerleme yüzdesi sabiti maskelendi; sûre 96 şablonuyla normalleştirilmiş aile karşılaştırması temiz); sûre 7 ayet — tek blok, ara zip yok",
 ],
}

DUZELTME = {}
