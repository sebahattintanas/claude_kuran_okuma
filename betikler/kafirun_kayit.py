# -*- coding: utf-8 -*-
"""kafirun_kayit.py — sûre 109 (Kafirun) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 109

CIPA = {
 # blok 1-6
 1: dict(kademe=None, olgu=False, cipa=False, not_="'qul yâ eyyuhe'l-kâfirûn' — hitap (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'lâ a'budu mâ ta'budûn' — ibadet, tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'ve lâ entum 'âbidûne mâ a'bud' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'ve lâ ene 'âbidun mâ 'abedtum' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'ve lâ entum 'âbidûne mâ a'bud' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'lekum dînukum ve liye dîn' — tutum (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 6): [
  "esmâ: e_oto 0 token; KARAR değişmedi (728); lafız yok, Rab yok — lafızsız ve Rabsız sûre; mühür yok",
  "kök tablosu: blokta yeni kök yok (1544); retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı",
  "yıldız (1001): 109:3, 109:4, 109:5 ★ — bilanço kaynağı 'n' etiketli (z=-0,79), kafiye kırığı bayrağı açık; gerçek kaynak kafiye kırığı; diğer 3 ayet yıldızsız",
  "fâsıla: metinde ن ن د م د ن; ölçüm 109:3, 109:4, 109:5 geçişlerini KAFİYE KIRILMASI işaretledi (üçü de gerçek); 109:6 د → ن geçişi işaretsiz (924); م ölçümde ن ile aynı N sınıfı",
  "biçim (924): ayet 1 harf 33 → harf3 14 (besmele ailesi); IMPV + VOC + DIKKAT 109:1, NEG 109:2-5 ölçümde var",
  "iltifât: ölçüm 0; sahset 109:1 ['2'] → 109:2-6 ['1', '2'] — 'qul' ile açılan söz içi 1S ve 2MP; söz katmanı ölçümde ayrılmıyor (924)",
  "söz sınırı (1017): 'qul' (lemma 'qâle') sözü 109:1'de açıyor, sûre sonunda (109:6) bitiyor — meal tırnağı 109:1 / 109:6; konuşan ve hitap edilen adsız; tapılanlar 'mâ' ile adsız",
  "esit2 / nakarat3 (kayıt): 109:3 ↔ 109:5 TAM; nakarat3 'lâ entum 'âbidûne mâ a'bud' 2 ayet tam, 'عبد ما عبد' iç kalıbı 3 ayet — süzgeç GEÇER",
  "çıpa: L0 / L1 / L2 / L4 yok; olgu=False 6 (hitap, tutum); tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 108:3 / 109:1 sûre sınırı — 2MS'ye hitapla kapanış / 2MS'ye 'qul' emriyle açılış; fâsıla ر → ن; 108 Rab 1, 109 lafızsız ve Rabsız",
  "aday 1039: ayet içi 5 (109:2-6 — 1S / 2MP karşılıkları; 109:6 'lekum dînukum' / 'liye dîn'); blok içi 0",
  "aday 1041: kayıt yok — lafız / Rab yok",
  "korpusta 1 (kayıt): kalıp 'yâ eyyuhe'l-kâfirûn', 'lâ a'budu mâ ta'budûn'; sûre içi tam sayım: kök عبد [8/8], kök دين [2/2]",
  "bağ: kalıp / lemma eşleri okumayla (10:104, 43:81); ikisi de AR + meal ile emsal listesinde basıldı; 107:1 ve 108:3 bu oturumda daha önce basılmıştı, yeniden basılmadı",
  "◈K / ◈B: ikisi de altı ayette '—'; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 6 ayet; oturum_xy 8 sayım, 0 uyuşmaz",
  "süreç: sûre 109 dosyaları kevser_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_109.py, oturum dışı; ad 'kafirun'; ISTEK iskele içinde boş; kayıt dosyası CIPA / ARIZA / DUZELTME boş kuruldu — kevser_kayit.py'deki DUZELTME taşınmadı, assert'le doğrulandı; ilerleme yüzdesi sabiti maskelendi; sûre 96 şablonuyla normalleştirilmiş aile karşılaştırması temiz); sûre 6 ayet — tek blok, ara zip yok",
 ],
}

DUZELTME = {}
