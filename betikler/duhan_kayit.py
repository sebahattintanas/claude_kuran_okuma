# -*- coding: utf-8 -*-
"""duhan_kayit.py — sûre 44 (Duhân) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 44

CIPA = {
 # blok 1-10
 7: dict(kademe='L0', olgu=True, cipa=False, not_="gökler, yer ve 'mâ beynehumâ' Rab'bin tamlamasında (26:24 emsali); süreç yok — L0; tarayıcı v4 adayı, çıpa değil"),
 10: dict(kademe='L1', olgu=True, cipa=False, not_="göğün 'apaçık bir duman' getireceği gün: öğe (gök, duman) + nitelik ('mubîn'), mekanizma/ölçü yok — L1; 41:11 've hiye duhân' ile kök/lemma bağı (okumada); tarayıcı vermedi"),
 # blok 21-30
 24: dict(kademe='L1', olgu=True, cipa=False, not_="deniz + nitelik 'rehv' (açık / sakin; kök korpusta yalnız burada); 20:77 'yebes' (kuru) ile iki niteleme; mekanizma/ölçü yok — L1; tarayıcı vermedi"),
 29: dict(kademe='L0', olgu=True, cipa=False, not_="gök ve yer ağlama fiilinin (olumsuz) öznesi — figür; süreç/ölçü yok — L0; tarayıcı vermedi"),
 # blok 31-40
 38: dict(kademe='L0', olgu=True, cipa=False, not_="gökler, yer ve 'mâ beynehumâ' yaratılan olarak, amaç olumsuzlanıyor ('lâ'ibîn'); 21:16 emsali; süreç/ölçü yok — L0; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ (1022 ailesi): 44:2 'mubîn' (kitap), 44:4 'hakîm' (iş), 44:8 'evvel' (atalar), 44:10 'mubîn' (duman) ölçüm MÜHÜRSÜZ / esma_kayit mühür EVET — değil; 44:6 'semî'' + 'alîm' geçerli mühür",
  "biçim (517 ailesi): 44:3, 5, 6 tekit 'innâ' / 'inne' ölçümde işaretsiz",
  "aday 1040 alanı: 43:2 → 44:2 ('ve'l-kitâbi'l-mubîn' esit2 TAM; devamı farklı); 43:83 → 44:9 ('yel'abû' / 'yel'abûn'); 43:89 → 44:1 sûre sınırı — kayıt, test yok",
  "aday 1041 alanı: 'munzir' 1P 44:3 / Peygamber 13:7, 38:65; 'hakîm' kitap 43:4 / 'huve' 43:84 / iş 44:4 (sınırda) — kayıt, test yok",
  "şahıs geçişi (1017 ailesi): 44:9 2MP → 3MP, 44:10 3MP → 2MS ölçüm iltifât 0; 44:5 (3>1) ve 44:6 (1>23) iltifât 1",
  "gloss (1021 ailesi): أمر 44:4 iş / 44:5 emir",
  'tetik: ilk koşuda 0 uyuşmaz (44:3 ليل; 44:6 سمع esmâ; 44:7, 10 سمو/أرض/يوم; 44:8 حيي/موت dolu)',
 ],
 (11, 20): [
  "esmâ (1022 ailesi): 44:12 'mu'min' (isteyenler), 44:13 'mubîn' (elçi), 44:17 'kerîm' (elçi), 44:19 'mubîn' (delil) ölçüm MÜHÜRSÜZ / esma_kayit mühür EVET — değil",
  "aday 1040 alanı: 43:49-50 → 44:12-15 (istek, vaat, azabın kaldırılması, dönüş dörtlüsü); 43:41 → 44:16 'muntaqimûn'; Firavun anlatısı 43:46-56 → 44:17 — kayıt, test yok",
  "aday 1041 alanı: 'bataşa' insan (26:130 Hûd'un kavmi, 28:19 Mûsâ) / 1P (44:16) — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 44:11 'hâzâ azâbun elîm' kimin sözü işaretsiz; 44:12 1P konuşanlar adsız; 44:17-20 elçi adsız (40:27'de aynı söz adlı Mûsâ'nın)",
  "biçim (517 ailesi): 44:12, 15, 16, 18, 20 tekit 'inne' ölçümde işaretsiz",
  "gloss (1021 ailesi): ولي 44:14 yüz çevirme; جنن 44:14 'mecnûn'",
  'tetik: ilk koşuda 0 uyuşmaz (44:11 أنس; 44:16 يوم dolu)',
 ],
 (21, 30): [
  "esmâ (1022 ailesi): 44:26 'kerîm' (makam) ölçüm MÜHÜRSÜZ / esma_kayit mühür EVET — değil",
  "aday 1040 alanı: 43:88 'inne hâulâi qavmun lâ yu'minûn' → 44:22 'enne hâulâi qavmun mucrimûn' — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 44:21-24 elçi ve emir veren 1S adsız; 44:23 muhatap 2MS adsız (26:52'de adlı Mûsâ); 44:28 'qavmen âharîn' adsız (26:59'da 'benî isrâîl') — KAPATILAMAZ",
  "biçim (517 ailesi): 44:23, 24 tekit; 44:25 'kem'; 44:28 'kezâlike' ölçümde işaretsiz",
  "gloss (1021 ailesi): عين 44:25 pınar; قوم 44:26 'maqâm'; نظر 44:29 'munzar' mühlet",
  'tetik: ilk koşuda 0 uyuşmaz (44:23 ليل; 44:24 بحر; 44:25 عين (pınar, organ değil); 44:29 سمو/أرض)',
 ],
 (31, 40): [
  "esmâ (1022 ailesi): 44:33 'mubîn' (sınav), 44:35 'ûlâ' (ölüm) ölçüm MÜHÜRSÜZ / esma_kayit mühür EVET — değil",
  "aday 1040 alanı: 43:52, 43:58 'hayr … em' → 44:37 'e-hum hayrun em qavmu tubba''; 44:36 → 45:25 (henüz okunmadı, xref) — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 44:34 'hâulâi' göndergesi adsız; 44:36 muhatap 2MP adsız; 44:31 ölçüm iltifât 1 (1>3)",
  "biçim (517 ailesi): 44:31, 37, 40 tekit ölçümde işaretsiz",
  "gloss (1021 ailesi): علو 44:31 büyüklenme; علم 44:32 'ilm' / 'âlemîn'; خير 44:32 'ihtâra' seçme",
  "okuma: 37:59 cennet ehlinin sözü ile 44:35 inkârcıların sözü aynı kalıp ('mevtetune'l-ûlâ … ve mâ nahnu bi-'); 44:38-39 = 21:16 + 15:85 — KAPATILAMAZ",
  'tetik: ilk koşuda 0 uyuşmaz (44:35 موت; 44:38 سمو/أرض/خلق; 44:39 خلق; 44:40 يوم)',
 ],
 (41, 50): [
  "esmâ (1022 ailesi): 44:41 'mevlâ' ×2 (insanlar) ölçüm MÜHÜRSÜZ / esma_kayit EVET — değil; 44:49 'azîz' + 'kerîm' ölçüm MÜHÜR, esma_kayit ÇİFT — muhatap azaptaki insan, değil (mühür yanlış); 44:42 'azîz' + 'rahîm' geçerli mühür",
  "aday 1041 alanı: 'el-azîz' 44:42 (Allah) / 44:49 (azaptaki insan) / 12:30, 12:78 (Mısır yöneticisi); 'mevlâ' 22:78 (Allah) / 44:41 (insanlar) — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 44:47-50 emir veren ve konuşan adsız, muhatap 2MP adsız; 44:49 2MS → 44:50 2MP ölçüm iltifât 0; 44:49 sözün alaycı olup olmadığı işaretsiz (KAPATILAMAZ)",
  "biçim (517 ailesi): 44:42, 43, 49, 50 tekit; 44:45, 46 benzetme 'ke' ölçümde işaretsiz",
  "gloss (1021 ailesi): ولي 44:14 yüz çevirme / 44:41 dost; مهل 44:45 erimiş maden",
  "oturum notu: blok taslağı (MEAL5/M5) bir önceki yarıda kalan turda yazılmıştı; kayıttan önce bütün sayım ve alıntılar yeniden doğrulandı, bir iddia düzeltildi (44:49 'zâqa' için doğrulanmamış 'çoğu 2MP' ifadesi çıkarıldı) ve bir gloss alıntısı tamlandı (44:45 مهل)",
  'tetik: ilk koşuda 0 uyuşmaz (44:41 يوم; 44:43 شجر)',
 ],
 (51, 59): [
  "esmâ (1022 ailesi): 44:56 'ûlâ' (evvel) — ölümün sıfatı; ölçüm 'esmâ yok', esma_kayit e_oto 1 mühür EVET — değil (mühür yanlış, bilanço esma_muhur_43 [56], geçerli [])",
  "konuşan / gönderge (1017 ailesi): 44:56 'vekâhum' öznesi 3MS adsız (44:57 'rabbike' ardından); 44:58 'yessernâhu' zamir göndergesi adsız (44:2-3 'el-kitâb … enzelnâhu' sûre başında) — KAPATILAMAZ",
  "aday 1040 alanı: 43:89 'fe-sfah anhum ve qul selâm, fe-sevfe ya'lemûn' / 44:59 'fe-rtaqib innehum murtaqibûn' — iki sûre de 'fe' + 2MS emir ve 3MP hakkında bir cümleyle bitiyor; kayıt, test yok",
  "sayı işareti 44:54 'zevvecnâ' — eşleştirme fiili, sayı değil (yanlış pozitif; 37:22 emsali)",
  "biçim (517 ailesi): 44:51, 59 tekit; 44:54 'kezâlike'; 44:58 'innemâ' ölçümde işaretsiz",
  "gloss (1021 ailesi): عين 44:52 pınar / 44:54 göz (iri gözlü); حور 44:54 hûr",
  "oturum notu: kayıttan önce 4 ifade sayıma göre düzeltildi (44:54 sûre içi 1P listesi çıkarıldı; 44:55 'âmin' okunan listesi tamlandı; 44:56 görülmemiş 52:18 anması çıkarıldı; 44:57 sûre içi Rab listesi kök sayımıyla değiştirildi); esma_el 44:49 yorumundaki 'alaycı' → 'alay işaretsiz' (ARIZA (41,50) ile uyum)",
  'tetik: ilk koşuda 0 uyuşmaz (44:52 عين; 44:54 زوج, عين; 44:56 موت)',
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_44.py uygular)
DUZELTME = {
}
