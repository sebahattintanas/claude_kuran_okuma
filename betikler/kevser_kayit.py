# -*- coding: utf-8 -*-
"""kevser_kayit.py — sûre 108 (Kevser) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 108

CIPA = {
 # blok 1-3
 1: dict(kademe=None, olgu=False, cipa=False, not_="'innâ a'taynâke'l-kevser' — verme (olgu=False; 93:5 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'fe-salli li-rabbike ve'nhar' — ibadet emri (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'inne şâni'eke huve'l-ebter' — buğz, tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 3): [
  "esmâ: e_oto 0 token; KARAR değişmedi (728); lafız yok, Rab 1 (108:2 'li-rabbike'); mühür yok",
  "kök tablosu: blokta 3 yeni kök (نحر, شنأ, بتر; 1544); retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı; iskelet çakışması yok; retroaktif betik kök شنأ için 'daha önce okunmuş 2 ayet' saydı — okuma_metni'nde sûre 5 anahtarı başka biçimde kayıtlı (blok aralıkları), ayet kaydı yok, yama atlandı (okunmamış sûre ayetleri)",
  "yıldız: 108:2 ★★★ (rab, z=6,78; hapaks 3,28 de eşik üstü — yeni kök نحر), 108:3 ★★★ (hapaks — yeni kök بتر, z=3,28) — formül davranışı; 108:1 yıldızsız",
  "sayı işareti (924): 108:1 'kevser' — kök كثر'in çokluk anlamından; sayı adı değil",
  "biçim (924): ayet 1 harf 34 → harf3 15 (besmele ailesi); IMPV 2 108:2 ölçümde var; 108:3 'huve' ayırma zamiri hasrı biçim alanında yok",
  "fâsıla: ölçüm R 3 (108:1-3 ر) — geçiş yok",
  "iltifât: ölçüm 0; sahset 108:1 ['1', '2'] → 108:2 ['2'] (1P'nin çıkışı, Rab 3. şahıs isimle) kısmi örtüşme — 924; 108:3 ['2', '3']",
  "adsız gönderge (1017): konuşan 1P, hitap 2MS ve buğzeden adsız; 1P'nin Rab ile aynılığı metinde işaretli değil — KAPATILAMAZ",
  "çıpa: L0 / L1 / L2 / L4 yok; olgu=False 3 (verme, ibadet emri, tutum); tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 107:7 / 108:1 sûre sınırı — esirgemeyle ('yemne'ûn') kapanış / vermeyle ('a'taynâ') açılış; fâsıla ن → ر; 107 lafızsız ve Rabsız, 108 Rab 1; okuma bağı kök صلو 107:4-5 namaz kılanlara 'veyl' / 108:2 namaz emri",
  "aday 1039: ayet içi 0; blok içi 0",
  "aday 1041: kayıt yok — Rab tek geçiş, lafız yok",
  "korpusta 1 (kayıt): lemma 'kevser', 'şâni'', 'ebter'; kök نحر, بتر; kalıp 'innâ a'taynâke', 'fe-salli'",
  "bağ: kalıp / lemma eşleri okumayla (93:5, 87:15); ikisi de AR + meal ile emsal listesinde basıldı; 107:4, 107:5 ve 107:7 bu oturumda daha önce basılmıştı, yeniden basılmadı",
  "◈K / ◈B: ikisi de üç ayette '—'; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 3 ayet; oturum_xy 7 sayım, 0 uyuşmaz",
  "süreç: sûre 108 dosyaları maun_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_108.py, oturum dışı; ad 'kevser'; kok_ekle ISTEK iskele içinde boş; ilerleme yüzdesi sabiti maskelendi; sûre 96 şablonuyla normalleştirilmiş aile karşılaştırması temiz); sûre 3 ayet — tek blok, ara zip yok",
 ],
}

DUZELTME = {
 3: {'alan': 'mercek', 'eski': "Sûre 2MS zamiriyle kapanıyor; sûrenin üç ayetinin üçü ر ile bitiyor (okuma).", 'dogru': "Sûre 2MS zamiriyle değil, belirli ad 'el-ebter' ile kapanıyor (2MS zamiri '-ke' ayetin ortasında, 'şâni'eke'); fâsıla cümlesi doğru: sûrenin üç ayetinin üçü ر ile bitiyor. Kayıttan sonra, sunumdan önce yakalandı.", 'aday': None, 'blok': '1-3'},
}
