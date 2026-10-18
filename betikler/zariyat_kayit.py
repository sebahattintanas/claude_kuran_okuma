# -*- coding: utf-8 -*-
"""zariyat_kayit.py — sûre 51 (Zâriyât) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 51

CIPA = {
 # blok 1-10
 1: dict(kademe=None, olgu=False, cipa=False, not_="51:1-4 yemin nesneleri ('zâriyât', 'hâmilât', 'câriyât', 'muqassimât') mevsûfsuz ism-i fâil — neyin savurduğu / taşıdığı / aktığı adlanmıyor; doğal olgu iddiası metinde yok (KAPATILAMAZ); tarayıcı vermedi"),
 7: dict(kademe='L1', olgu=True, cipa=False, not_="gök 'zâti'l-hubuk' — nitelik adlanıyor (yollar / örgü); süreç / ölçü / mekanizma yok — L1; tarayıcı vermedi"),
 # blok 11-20
 17: dict(kademe='L0', olgu=True, cipa=False, not_="gece ve seher (51:18) vakit olarak adlanıyor; uyku azlığı 'qalîl' ölçüsüz — L0; tarayıcı vermedi"),
 20: dict(kademe='L0', olgu=True, cipa=False, not_="'fi'l-ardi âyât' — yer işaretlerin yeri olarak adlanıyor; nitelik / süreç yok — L0; tarayıcı vermedi"),
 # blok 21-30
 21: dict(kademe='L0', olgu=True, cipa=False, not_="'fî enfusikum' — işaretlerin yeri olarak insanın kendisi adlanıyor; nitelik / süreç yok — L0; tarayıcı vermedi"),
 22: dict(kademe='L0', olgu=True, cipa=False, not_="'fi's-semâ'i rizqukum' — rızkın yeri olarak gök adlanıyor; süreç / mekanizma yok — L0; tarayıcı vermedi"),
 29: dict(kademe='L1', olgu=True, cipa=False, not_="'acûzun aqîm' — yaşlılık ve kısırlık hâli adlanıyor (alıntı içinde); süreç / mekanizma yok — L1; tarayıcı vermedi"),
 # blok 31-40
 33: dict(kademe=None, olgu=False, cipa=False, not_="'hicâraten min tîn' — ceza anlatısı, doğal olgu iddiası değil; tarayıcı vermedi"),
 # blok 41-50
 41: dict(kademe=None, olgu=False, cipa=False, not_="'er-rîhu'l-aqîm' — ceza anlatısı (kısır rüzgâr), doğal olgu iddiası değil; 51:42 'ke'r-ramîm' benzetme; tarayıcı vermedi"),
 47: dict(kademe='L1', olgu=True, cipa=False, not_="'ve's-semâ'e beneynâhâ bi-eydin ve innâ le-mûsi'ûn' — gök bina edilmiş (nitelik); 'mûsi'ûn' iki okuma (genişleten / gücü yeten), süreç okuması KAPATILAMAZ; ölçü / mekanizma yok — L4 değil"),
 48: dict(kademe='L1', olgu=True, cipa=False, not_="'ve'l-arda feraşnâhâ' — döşenmiş yer, nitelik; süreç yok"),
 49: dict(kademe='L1', olgu=True, cipa=False, not_="'min kulli şey'in halaqnâ zevceyn' — her şey için iki eş adlanıyor; sınıf-üye eşlemesi yok (36:36, 43:12 emsali L1; 29:40 ölçütü); tarayıcı v4 adayı — aday, çıpa değil; kapsam 'kulli şey'' kesinlik iddiası olarak okunmaz"),
 # blok 51-60
 56: dict(kademe=None, olgu=False, cipa=False, not_="'mâ halaqtu'l-cinne ve'l-inse illâ li-ya'budûn' — yaratmanın amacı beyanı, doğal olgu iddiası değil; tarayıcı v4 adayı — aday, çıpa değil"),
}

ARIZA = {
 (1, 10): [
  "esmâ: blokta e_oto tokeni yok; mühür ölçümü [] — karar gerekmedi",
  "aday 1040 alanı: 50:45 → 51:1 (fâsıla د → ا; 50:1 harf + yemin / 51:1 yemin — ardışık iki sûre yeminle açılıyor); 50:32 'hâzâ mâ tû'adûn' + 50:45 'vaîd' → 51:5 'innemâ tû'adûn'; 50:44 'yesîr' → 51:3 'yusrâ'; 50:6 gök 'mâ lehâ min furûc' → 51:7 'zâti'l-hubuk' — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): yemin eden adlanmıyor; 51:1-4 dört yemin nesnesi mevsûfsuz; 51:5 vaat eden, 51:9 çeviren (edilgen) adsız; 51:9 'anhu' göndergesi açık değil — KAPATILAMAZ",
  "ölçüm (924): 51:1 harf 31 → harf3 11, n=2 — korpus metninde besmele bitişik, harf sayımı besmeleyi katıyor olabilir (49:1 kaydıyla aynı tür); QASEM yalnız 51:4'te işaretli, 51:1 ve 51:7'deki 've' yemini işaretsiz (517)",
  "yıldız formülü: 51:5, 9, 10 ★★★ pas z=5,38 (2-4 kelimelik ayette edilgen; edilgenler gerçek); 51:7 ★★★ hapaks حبك (kok_ekle_51, 1 token) — bilinen davranış, içerik iddiası değil",
  "yıldız etiketi (1001): 51:8 ★ kafiye kırığı ف'den, etiket 'n' z=-0,89",
  "gloss (1021 ailesi): ذرو 'savurma (tezrû); savuran rüzgârlar (zâriyât)' — gloss 'rüzgâr' mevsûfunu ekliyor, 51:1 metninde mevsûf yok (okuma; gloss metnin söylemediğini söylüyor — KAPATILAMAZ)",
  "gloss (1021 ailesi): دين 'din; borç' — 51:6 'ed-dîn' (karşılık / ceza) anlamını kapsamıyor olabilir — okuma, KAPATILAMAZ",
  "okuma: 42:22 → 51:6; 39:21 → 51:8; 29:61, 40:63, 46:22 → 51:9; 10:66 → 51:10 — KAPATILAMAZ",
  "tetik: ön kuru koşu 2 tetik (51:2 حمل; 51:7 سمو) — ilk koşuda 0 uyuşmaz; [x/y] ilk koşuda 0 (18 sayım)",
 ],
 (11, 20): [
  "esmâ: blokta e_oto tokeni yok; mühür ölçümü [] — karar gerekmedi; Rab 1 (51:16 'rabbuhum')",
  "aday 1041 alanı: أخذ 'âhiz' 11:56 Rab ('huve âhizun bi-nâsiyetihâ') / 51:16 sakınanlar ('âhizîne mâ âtâhum') — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 51:13 sınayan (edilgen), 51:14 'zûqû' diyen adsız — KAPATILAMAZ",
  "gloss (1021 ailesi): سحر 'büyü, sihir' — 51:18 'eshâr' (seher vakitleri) anlamını kapsamıyor; عين 'göz; pınar' — 51:15'te ◈B tetikliyor, anlam pınar (satır dolu, organ yok)",
  "yıldız formülü: 51:13 ★★★ pas z=5,38 (edilgen gerçek); 51:17 ★★★ hapaks هجع (kok_ekle_51); 51:16 ★★ rab z=2,05 (9 kelimede 1 Rab) — bilinen davranış",
  "biçim (517 ailesi): tekit 'inne' (51:15, 16), takdim 'bi'l-eshâri hum' (51:18) ölçümde işaretsiz",
  "esit2: 51:15 → 15:45 TAM 1,0000 (okundu); 52:17, 54:54 BENZER (henüz okunmadı)",
  "okuma: 23:54, 23:63 → 51:11; 27:65, 16:21 → 51:12; 10:51, 46:24 → 51:14; 15:45, 15:46 → 51:15; 11:56, 28:53 → 51:16; 26:24, 44:7 → 51:20 — KAPATILAMAZ",
  "tetik: ön kuru koşu 5 tetik (51:12, 13 يوم; 51:15 عين; 51:17 ليل; 51:20 أرض) — ilk koşuda 0 uyuşmaz; [x/y] ilk koşuda 0 (34 sayım); kayıttan önce 51:18'de görülmemiş 3:17 alıntısı çıkarıldı, 51:14 emsal ifadesi daraltıldı",
 ],
 (21, 30): [
  "esmâ: 51:25 'selâm' ×2 (selamlaşma), 51:28 'alîm' (oğlanın sıfatı) — ilâhî değil, ölçüm MÜHÜRSÜZ / esma_kayit EVET → karar 'değil' (1022); 51:30 'hakîm' + 'alîm' Rab'bin sıfatı, ilâhî, ölçüm MÜHÜR — karar sonrası bilanço geçerli mühür [30]",
  "aday 1041 alanı: علم 'alîm' 51:28 oğlan / 51:30 Rab — aynı blokta iki ayet arayla; كرم/ضيف yok — kayıt, test yok",
  "konuşan / gönderge (1017 ailesi): 51:21-23 konuşan adlanmıyor; 51:23 'innehû' göndergesi açık değil; 51:24 muhatap 2MS adsız; konuklar adsız (11:69'da 'rusulunâ'); 51:28 müjdelenen oğlan ve 51:29 karısı adsız — KAPATILAMAZ",
  "biçim (517 ailesi): 51:30 tekit 'inne' + hasr zamiri 'huve' ölçümde işaretsiz; 51:23 QASEM işaretli (Rab ile yemin), 51:1 ve 51:7 işaretsiz",
  "yıldız formülü: 51:22 ★★★ pas (edilgen gerçek); 51:29 ★★★ hapaks صكك (kok_ekle_51); 51:23 ★★ rab z=2,05, 51:30 ★★ rab z=2,34 — kısa ayette Rab; bilinen davranış",
  "◈B tetik listesi: 51:29 'vech' (yüz) ve 'aqîm' (kısır) tetik listesinde yok — satır '—', gözlem ◇'de (ön-kayıt §4)",
  "okuma: 46:35, 50:32 → 51:22; 15:51 → 51:24; 15:52, 11:69, 15:62 → 51:25; 37:91, 11:69 → 51:26; 39:3, 37:91 → 51:27; 11:70, 15:53 → 51:28; 11:72, 11:71 → 51:29; 19:9, 19:21 → 51:30 — KAPATILAMAZ",
  "tetik: ön kuru koşu 3 tetik (51:21 بصر; 51:22 سمو; 51:23 سمو أرض) — ilk koşuda 0 uyuşmaz; [x/y] ilk koşuda 0 (46 sayım); kayıttan önce 51:30'da 19:9 alıntısının biçimi düzeltildi ('kezâlike … rabbuke', 2MS)",
 ],
 (31, 40): [
  "esmâ: 51:35 'mu'min' (insanlar), 51:38 'mubîn' (delilin sıfatı) — ilâhî değil, ölçüm MÜHÜRSÜZ / esma_kayit EVET → karar 'değil' (1022) — karar sonrası bilanço geçerli mühür []",
  "konuşan / gönderge (1017 ailesi): 51:32-34 elçilerin 1P'si → 51:35 anlatıcı 1P (ölçüm iltifât 1, geçiş işaretli değil); suçlu topluluk ve şehir adlanmıyor (11:70'te 'qavmu Lût'); gönderen (edilgen 'ursilnâ') adsız — KAPATILAMAZ",
  "yıldız formülü: 51:34 ★★★ rab z=5,01 (4 kelimede 1 Rab); 51:32 ★★ pas z=2,52 (edilgen gerçek) — bilinen davranış, içerik iddiası değil",
  "biçim (517 ailesi): tekit 'innâ' (51:32), 've fî Mûsâ' atfının 51:20-21 dizisine bağlanması ölçümde yok",
  "esit2: 51:31 → 15:57, 51:32 → 15:58 TAM 1,0000 (okundu) — iki ardışık ayet 15:57-58 ile birebir; devamı 15:59 'illâ âle Lût' / 51:33 'li-nursile aleyhim hicâraten min tîn'",
  "nakarat3: 51:39 'qâle sâhirun ev mecnûn' GEÇER — sûre içi eşi 51:52 (henüz okunmadı)",
  "okuma: 15:57, 11:69 → 51:31; 15:58, 10:75, 11:70 → 51:32; 11:82, 15:74 → 51:33; 11:83 → 51:34; 11:103 → 51:37; 10:75 → 51:38; 15:6, 26:27, 44:14 → 51:39; 28:40, 20:78 → 51:40 — KAPATILAMAZ",
  "tetik: ön kuru koşu 0 tetik (blokta ◈K / ◈B tetik kökü yok) — ilk koşuda 0 uyuşmaz; [x/y] ilk koşuda 0 (40 sayım)",
 ],
 (41, 50): [
  "esmâ: 51:50 'mubîn' (uyarıcının sıfatı) — ilâhî değil, ölçüm MÜHÜRSÜZ / esma_kayit EVET → karar 'değil' (1022; KARAR 449) — karar sonrası bilanço geçerli mühür []",
  "konuşan / gönderge (1017 ailesi): 51:41, 47-49 1P adsız; 51:43 edilgen 'qîle' — söyleyen adsız (11:65'te Sâlih); 51:50 1S 'innî' adsız — KAPATILAMAZ",
  "yıldız formülü: 51:43 ★★ pas z=2,52 (edilgen gerçek); 51:44 ★★ rab z=2,34; 51:50 ★ allah z=1,97 — sûrenin ilk lafzı (51:1-49 lafız 0; ölçüm) — bilinen davranış, içerik iddiası değil",
  "biçim (517 ailesi): 51:42 teşbih 'ke-', 51:46 tekit 'inne', 51:48 övgü 'ni'me', 51:50 tekit 'innî' ölçümde işaretsiz; 51:47 EMPH işaretli",
  "kök çok-anlam: قوم 51:45 'qiyâm' (kalkma) / 51:46 'qavm' (topluluk); وسع 51:47 'mûsi'ûn' — genişlik / güç; gloss kapsıyor, seçim KAPATILAMAZ (1021 alanı)",
  "nakarat3: 51:50 'innî lekum minhu nezîrun mubîn' GEÇER — sûre içi eşi 51:51 (henüz okunmadı)",
  "okuma: 36:78 → 51:42; 11:65 → 51:43; 41:17, 11:67 → 51:44; 18:43 → 51:45; 27:12, 43:54 → 51:46; 38:17, 50:6 → 51:47; 50:7 → 51:48; 13:3, 36:36, 43:12 → 51:49; 29:50 → 51:50 — KAPATILAMAZ",
  "tetik: ön kuru koşu 5 tetik (51:41 روح; 51:43 حين; 51:47 سمو; 51:48 أرض; 51:49 خلق زوج) — ilk koşuda 0 uyuşmaz; [x/y] ilk koşuda 0 (43 sayım); kayıttan önce 51:50 'ferre' emsal listesi ölçüme indirildi (görülmemiş ayet adı çıkarıldı)",
 ],
 (51, 60): [
  "esmâ: 51:51 'mubîn' (uyarıcının sıfatı), 51:55 'mu'min' (insanlar) — ilâhî değil → karar 'değil'; 51:58 'er-razzâq', 'el-metîn' — lafzın yüklemi / sıfatı → karar 'ilâhî' (KARAR 453); ölçüm satırı 51:58'de ikisini MÜHÜRSÜZ gösteriyor, esma_kayit EVET (ÇİFT) — karar sonrası bilanço geçerli mühür [58] (sûre 51'in tek geçerli mührü; sûre bilançosu kapanışta)",
  "konuşan / gönderge (1017 ailesi): 51:51 1S 'innî' (uyarıcı) → 51:56-57, 59 1S (yaratan; 'halaqtu', hazf 'ya'budûn(i)', 'yut'imûn(i)', 'yesta'cilûn(i)') — aynı şahıs, iki gönderge; 51:57 1S → 51:58 3MS lafız — ölçüm iltifât 0 (geçişler işaretsiz); 51:54-55 muhatap 2MS adsız; 51:60 vaat eden (edilgen) adsız — KAPATILAMAZ",
  "yıldız formülü: 51:58 ★★ allah z=2,33; 51:60 ★★ pas z=2,52 (edilgen gerçek); 51:51 lafız z=1,29 yıldız yok (11 kelime) — bilinen davranış, içerik iddiası değil",
  "biçim (517 ailesi): 51:51 tekit 'innî', 51:55 tekit 'inne', 51:58 tekit 'inne' + fasl zamiri 'huve' ölçümde işaretsiz; 51:51 NEHY, 51:52 ve 51:56 HASR, 51:53 IDRAB işaretli",
  "gloss (1021 ailesi): 51:59 'zenûb' (lemma korpusta 1) — kök gloss 'günah, suç' pay / kova okumasını kapsamıyor; araç dondurulmuş, boşluk kanıt değil (924)",
  "nakarat3: 51:51 ↔ 51:50 'innî lekum minhu nezîrun mubîn' GEÇER; 51:52 ↔ 51:39 'sâhirun ev mecnûn' GEÇER — iki sûre içi eş de okundu",
  "okuma: 17:22, 17:39, 50:26 → 51:51; 51:39 → 51:52; 37:30 → 51:53; 37:174, 37:178, 17:29, 17:39, 51:39, 51:40 → 51:54; 50:45 → 51:55; 51:22 → 51:57; 27:33, 28:76 → 51:58; 21:37, 16:1, 46:35, 51:14, 51:26 → 51:59; 19:37, 38:27, 43:83, 51:5, 51:22 → 51:60 — KAPATILAMAZ",
  "tetik: ön kuru koşu 2 tetik (51:56 خلق أنس; 51:60 يوم) — ilk koşuda 0 uyuşmaz; [x/y] ilk koşuda 0 (40 sayım); kayıttan önce iki ifade düzeltildi: 51:58'de 27:33 için metinde olmayan kişi adı çıkarıldı, 51:52'de 'kezâlike' sayımının lemma dizisi (ذا + ما) olduğu yazıldı",
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_51.py uygular)
DUZELTME = {
}
