# -*- coding: utf-8 -*-
"""tekasur_kayit.py — sûre 102 (Tekasur) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 102

CIPA = {
 # blok 1-8
 1: dict(kademe=None, olgu=False, cipa=False, not_="'elhâkumu't-tekâsur' — tutum (olgu=False; 100:6 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
 2: dict(kademe=None, olgu=False, cipa=False, not_="'hattâ zurtumu'l-maqâbir' — kabirler, insan yapımı yer, ölüm (olgu=False; 100:9 kaydı emsali); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'kellâ sevfe ta'lemûn' — bilme, gelecek (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'summe kellâ sevfe ta'lemûn' — bilme, gelecek (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'kellâ lev ta'lemûne 'ilme'l-yaqîn' — bilme, şart (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'le-terawunne'l-cahîm' — âhiret, cahîm (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'summe le-terawunnehâ 'ayne'l-yaqîn' — âhiret, cahîm (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'summe le-tus'elunne yevme'izin 'ani'n-na'îm' — âhiret, sorgu (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 8): [
  "esmâ: e_oto 0 token; KARAR değişmedi (728); lafız yok, Rab yok — lafızsız ve Rabsız sûre (sûre 101 gibi); mühür yok",
  "kök tablosu: blokta yeni kök yok (1537); retroaktif yama hedefli 0, genel 0 (iki geçiş); taban kayıtları om_base ile aynı",
  "gloss (1021): kök زور 'yalan, uydurma' (102:2 'zurtum' ziyaret etme, varma), kök سأل 'isteme, dileme' (102:8 'le-tus'elunne' sorguya çekilme) — buradaki anlamları vermiyor",
  "yıldız: 102:8 ★★★ (edilgen 1/1, pas z=5,38); diğer 7 ayet yıldızsız",
  "sayı işareti (924): 102:1 'tekâsur' — kök كثر sayı adı değil; işaret kök kaynaklı",
  "biçim (924): ayet 1 harf 32 → harf3 13 (besmele ailesi); 102:2 'hattâ' sınırı ve 102:5 'lev' şartının cevapsızlığı biçim alanında görünmüyor; KELLA 102:3-5, FUT 102:3-4, COND 102:5, EMPH 102:6-8 ölçümde var",
  "fâsıla: ölçüm R 2 (102:1-2 ر), N 6 (102:3-5, 7 ن; 102:6, 8 م) — ر → ن geçişi kafiye kırığı işaretlenmedi",
  "iltifât: ölçüm 0; sahset 102:1 ['2', '3'] (3MS özne 'tekâsur'), 102:7 ['2', '3'] (3FS zamir 'cahîm'), diğerleri ['2']",
  "adsız gönderge (1017): hitap 2MP sûrenin tamamında (102:1-8) — adlandırılmadı; 102:8 soran yazılmamış (edilgen)",
  "çıpa: L0 / L1 yok; olgu=False 8 (tutum, kabir, bilme, âhiret); tarayıcı v4 blokta aday vermedi",
  "aday 1040 (kayıt): 101:11 / 102:1 sûre sınırı — ateş adıyla kapanış / 2MP hitapla açılış; fâsıla ة → ر; iki sûre de lafızsız ve Rabsız; okuma bağı 101:11 'nâr' / 102:6 'cahîm'",
  "aday 1039: ayet içi 0; blok içi 0 (''ilme'l-yaqîn' / ''ayne'l-yaqîn' paralel, metinde karşıt değil)",
  "aday 1041: kayıt yok — lafız / Rab yok",
  "esit2 BENZER (kayıt): 102:3 ↔ 102:4 oran 0,9231 — fark 'summe'; nakarat3 [3, 4] süzgeç GEÇMEZ",
  "korpusun iki geçişi, ikisi de basıldı: lemma 'tekâsur' (57:20, 102:1); kalıp 'summe kellâ' (78:5, 102:4); kalıp 'lev ta'lemûn' (56:76, 102:5); kalıp 'le-tus'elunne' (16:56, 102:8); korpusun tamamı sûre içi: kalıp 'kellâ sevfe ta'lemûn' (102:3, 102:4); korpusta 1: 'zur' (fiil), 'maqâbir', 'kellâ lev', ''ilme'l-yaqîn', 'le-terawunne', 'le-terawunnehâ', ''ayne'l-yaqîn'",
  "bağ: kalıp / lemma eşleri okumayla (101:11, 57:20, 82:4, 100:9, 11:93, 78:4, 78:5, 56:76, 56:95, 69:51, 79:36, 16:56); 82:4, 100:9, 101:11 bu oturumda daha önce basılmıştı, yeniden basılmadı; diğerleri AR + meal ile basıldı",
  "◈K / ◈B: ◈K dolu 102:8 (يوم); ◈B dolu 102:7 (عين — organ anlamı değil); 102:8 'na'îm' kök نعم S1 lemma kısıtı dışında — tetiklemedi; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz, 8 ayet; oturum_xy 16 sayım, 0 uyuşmaz",
  "süreç: sûre 102 dosyaları karia_* şablonlarından iskele betiğiyle kuruldu (yamalar/iskele_102.py, oturum dışı; ad 'tekasur'; ilerleme yüzdesi sabiti maskelendi; sûre 96 şablonuyla normalleştirilmiş aile karşılaştırması temiz); sûre 8 ayet — tek blok, ara zip yok",
 ],
}

DUZELTME = {}
