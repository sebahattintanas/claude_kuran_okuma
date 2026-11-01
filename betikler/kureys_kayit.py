# -*- coding: utf-8 -*-
"""kureys_kayit.py — sûre 106 (Kureys) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 106

CIPA = {
 # blok 1-4
 1: dict(kademe=None, olgu=False, cipa=False, not_="'li-îlâfi qureyş' — kavim adı, ülfet (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe='L0', olgu=True, cipa=False, not_="'rihlete'ş-şitâ'i ve's-sayf' — mevsim adları (kış / yaz), yolculuğun zamanı; süreç yok — L0 (93:1 kaydı emsali — adlı zaman); tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'fe-l-ya'budû rabbe hâze'l-beyt' — ibadet emri (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'ellezî at'amehum min cû'in ve âmenehum min xavf' — doyurma, güven; insan durumu (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 4): [
  "esmâ: e_oto 0 token; KARAR değişmedi (728); lafız yok, Rab 1 (106:3 'rabbe hâze'l-beyt'); mühür yok",
  "kök tablosu: blokta 3 yeni kök (قرش, شتو, صيف; 1541); retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı; iskelet çakışması yok",
  "iskele (süreç): kok_ekle_106 iskele ile kok_ekle_105'in ISTEK satırını (فيل) taşıdı ve ad değişimi gloss'taki 'fil' sözcüğünü de 'kureys' yaptı — kayıttan önce yakalandı, ISTEK ayrı yamayla boşaltıldı (yamalar/yama_kok_106_bosalt.py); kök tablosu etkilenmedi (فيل gloss'u 'fil'); '_profil_106' / '_esma_profil_106' anahtarları iskele assert'iyle doğrulandı",
  "yıldız: 106:1 ★★★ (hapaks — yeni kök قرش, z=3,28), 106:2 ★★★ (hapaks — yeni kökler شتو, صيف, z=6,79), 106:3 ★★★ (rab, z=5,01; kafiye kırığı bayrağı da açık) — formül davranışı; 106:4 yıldızsız",
  "sayı işareti (924): 106:1 ve 106:2 'îlâf' — kök ألف'in 'bin' anlamından; sayı adı değil, ülfet",
  "biçim (924): ayet 1 harf 28 → harf3 9 (besmele ailesi); IMPV + DIKKAT 106:3 ölçümde var; 106:1-2 fiilsiz 'li-' öbeğinin bağlanması biçim alanında görünmüyor",
  "fâsıla (924): metinde ش → ف → ت → ف; ölçüm yalnız 106:3'ü KAFİYE KIRILMASI işaretledi, 106:2 ve 106:4 geçişleri işaretsiz",
  "iltifât: ölçüm 0; sahset 106:2-4 ['3'], 106:1 —",
  "gönderge: 106:4 'ellezî' 106:3'teki 'rabb'ı niteliyor (okuma); 106:1 'li-' öbeğinin bağlandığı fiil KAPATILAMAZ",
  "adsız gönderge (1017): emreden / konuşan adsız; Kureyş adlı (kavim)",
  "çıpa: L0 1 (106:2 — mevsim adları); L1 / L2 / L4 yok; olgu=False 3 (kavim adı, ibadet emri, insan durumu); tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 105:5 / 106:1 sûre sınırı — teşbihle kapanış / fiilsiz 'li-' öbeğiyle açılış; fâsıla ل → ش; iki sûre de lafız 0, Rab 1; 106:1 öbeğinin önceki sûreye bağlanıp bağlanmadığı metinden KAPATILAMAZ",
  "aday 1039: ayet içi 2 (106:2 'şitâ'' / 'sayf'; 106:4 'âmenehum' / 'xavf' ve 'at'amehum' / 'cû''); blok içi 0",
  "aday 1041: sûre içi kayıt yok — Rab tek geçiş; sûreler arası okuma notu lemma 'âmene' 103:3 insanlar (iman) / 106:4 Rab (güvene kavuşturma) — eşsesli lemma birleşmesi",
  "korpusta 1 (kayıt): kök قرش, شتو, صيف; lemma 'rihle'; kalıp 'rabbe hâze'l-beyt'; korpusun tamamı sûre içi: lemma 'îlâf' (106:1, 106:2); kalıp 'min cû'' 2 ayet (88:7, 106:4)",
  "bağ: kalıp / lemma eşleri okumayla (27:91, 16:112, 88:7); hepsi AR + meal ile emsal listesinde basıldı; 93:1, 103:3 ve 105:5 bu oturumda daha önce basılmıştı, yeniden basılmadı",
  "◈K / ◈B: ikisi de dört ayette '—' (106:2 mevsim adları ◈K tetik listesinde değil — gözlem ◇'de); tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 4 ayet; oturum_xy 13 sayım, 0 uyuşmaz",
  "süreç: sûre 106 dosyaları fil_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_106.py, oturum dışı; ad 'kureys'; ad değişimi önek / sonek kuralları da harf sınırıyla — 'profil' korunur; ilerleme yüzdesi sabiti maskelendi; sûre 96 şablonuyla normalleştirilmiş aile karşılaştırması temiz); sûre 4 ayet — tek blok, ara zip yok",
 ],
}

DUZELTME = {}
