# -*- coding: utf-8 -*-
"""saff_kayit.py — sûre 61 (Saff) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 61

CIPA = {
 # blok 1-7
 1: dict(kademe='L0', olgu=True, cipa=False, not_="'sebbaha li'llâhi mâ fi's-semâvâti ve mâ fi'l-ard' — gökler ve yer tesbih edenlerin yeri olarak adlanıyor; süreç / ölçü yok — L0 (57:1, 59:1 emsali); tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'ke-ennehum bunyânun mersûs' — yapı insan yapımı, teşbih aracı; doğal olgu değil; tarayıcı vermedi"),
 # blok 8-14
 8: dict(kademe=None, olgu=False, cipa=False, not_="'li-yutfi'û nûra'llâhi bi-efvâhihim' — nur ağızla söndürülecek şey, mecaz; doğal olgu değil, merdiven uygulanmadı; tarayıcı v4 adayı, çıpa değil"),
 12: dict(kademe=None, olgu=False, cipa=False, not_="'cennâtin tecrî min tahtihe'l-enhâr' — cennet ırmakları, âhiret; doğal olgu değil; tarayıcı vermedi"),
}

ARIZA = {
 (1, 7): [
  "esmâ: e_oto 3 token (61:1 'azîz', 'hakîm'; 61:6 'mubîn'); 'azîz', 'hakîm' İLÂHÎ ('huve' zamirinin haberi), 'mubîn' DEĞİL ('sihr'in sıfatı); KARAR 577 → 580; bilanço geçerli mühür yalnız 61:1; 61:6 esma_kayit mühür EVET, ölçüm 'MÜHÜRSÜZ', geçerli değil (1022 ailesi)",
  "harf alanı: ayet 1 ölçümünde harf 61 → harf3 41, isaret 0 (56:1-60:1 ailesi); 61:2-7'de fark = isaret — besmele harfleri olabilir; araç alanı, metin hakkında kanıt değil (aday 924); KAPATILAMAZ",
  "kök tablosu: kok_ekle_61 1 kök (رصص, 61:4); yama_retroaktif hedefli 0, genel geçiş 0",
  "yıldız (924): 61:4 ★★★ kaynağı hapaks — yeni eklenen kökün tek token'ı (رصص); 61:3 ve 61:7 ★ ile 61:5 ★★ lafız kaynaklı; 61:6 ★ n — içerik iddiası değil",
  "fâsıla: blok içi kafiye kırığı 61:4 (ص); diğer altı ayet م / ن",
  "aktör rol (aday 1038): 61:6 'ahmed' ölçümde 'kisi, rol fail'; metinde 'ismuhû'nun haberi (gayr-i munsarif ad) — rol etiketi i'râbdan türüyor",
  "okuma ikiliği: 61:6 'fe-lemmâ câ'ehum bi'l-beyyinât' fail zamiri 3MS, gönderge Îsâ ya da 'ahmed' adlı elçi — iki yöne açık, karar verilmedi",
  "nakarat3 harekesiz eşleşme (924): 61:5 'ennî rasûlu'llâhi ileykum' / 61:6 'innî rasûlu'llâhi ileykum' — lemma dizisi farklı ('enne' / 'inne'), nakarat3 ikisini eşliyor; bağ okumayla yazıldı",
  "esit2 61:1 → 62:1 BENZER: 62:1 henüz okunmadı — bağ yazılmadı",
  "adsız (aday 1017): 61:2-3 muhatap inananlar ve soran; 61:4 savaşanlar; 61:5 Mûsâ'nın kavmi; 61:6 'qâlû' diyenler; 61:7 Allah'a yalan uyduran ve çağıran (edilgen) — ad verilmedi; 'ahmed' adı metinde, metin dışı kişiyle eşlenmedi",
  "aday 1041 (kayıt): 61:5 kök زيغ 'zâğû' (insan, I. bab) / 'ezâğa'llâhu' (Allah, IV. bab) aynı ayette; 61:4 lemma 'ehabbe' Allah öznesi, sûre içi eş henüz okunmadı",
  "aday 1040 (kayıt): 60:13 → 61:1 sûre sınırı — nidâ ve dost edinme yasağıyla kapanış / tesbihle açılış; fâsıla ر → م; test yok",
  "karşıt çift (aday 1039, okuma): 61:2-3 'teqûlûn' / 'lâ tef'alûn'; 61:2-3 / 61:4 söz / saf; 61:5 'zâğû' / 'ezâğa'llâh'; 61:6 'beyne yedeyye' / 'min ba'dî', 'musaddiq' / 'mubeşşir', 'el-beyyinât' / 'sihrun mubîn'; 61:7 'iftirâ' / 'yud'â ile'l-islâm' — kayıt, test yok",
  "kök iki anlam (okuma, D3): بني 61:4 'bunyân' (yapı) / 61:6 'ibn', 'benî' (oğul); سمو 61:1 'es-semâvât' / 61:6 'ismuhû' — gloss tablosu iki anlamı da taşıyor",
  "okuma: 59:1, 57:1, 60:13 → 61:1; 26:226 → 61:2; 40:35 → 61:3; 9:111, 9:109 → 61:4; 14:6, 33:69, 9:117, 9:24 → 61:5; 9:111, 43:63, 28:36, 27:13, 46:7 → 61:6; 11:18, 49:17, 9:109 → 61:7 — KAPATILAMAZ",
  "tetik: ön kuru koşu 3 uyuşmaz (61:1 ◈K سمو أرض, 61:5 ◈B قلب, 61:6 ◈B يدي) → satırlar dolduruldu; kayıtta 0 uyuşmaz; [x/y] 0 (55 sayım)",
 ],
 (8, 14): [
  "esmâ: e_oto 8 token (61:8 'nûr' ×2; 61:13 'qarîb', 'mu'minîn'; 61:14 'ensâr' ×3, 'zâhirîn'); hepsi DEĞİL (izâfetli nur, fethin sıfatı, insan çoğulları); KARAR 580 → 588; esma_kayit mühür EVET 61:8, 13, 14 — bilanço geçerli mühür 0 (1022 ailesi)",
  "yıldız (924): 61:8 ★★★ ve 61:11 ★★, 61:13 ★ lafız kaynaklı (kısa ayette 2 lafız: 61:8 allah z=3,11); 61:14 ★★ n — içerik iddiası değil",
  "tarayıcı adayı 61:8 (nûr) — mecaz, doğal olgu değil; çıpa yok (CIPA 8 olgu False)",
  "biçim (517 ailesi): 61:14 lafız 3MS 'ensâra'llâh' → 1P 'eyyednâ' geçişi; ölçüm iltifât 0",
  "D1 kip (okuma): 61:11 IMPF haber kipi emir anlamında, 61:12 cezmli cevap — ölçüm kipi yalnız 'şart'; araç alanı, kanıt değil (924)",
  "mm2 (ölçüm): 61:9 [3, رسل] — 'ersele rasûlehû'; alan okumada açıklanmadı",
  "kalıp (okuma): 61:12 'zâlike'l-fevzu'l-azîm' 5 ayet; 9:72 'zâlike huve'l-fevzu'l-azîm' harekesiz kalıba girmiyor — sayım iddiası yok",
  "sıralı eşleşme (okuma): 9:32-33 → 61:8-9 aynı sırayla iki ayet; ardışık sûre değil — 1040 alanına yazılmadı, okuma bağı",
  "aday 1041 (kayıt): 61:4 / 61:13 kök حبب ('yuhibbu' Allah / 'tuhibbûnehâ' inananlar); 61:13 / 61:14 kök نصر ('nasrun mina'llâh' / 'ensâru'llâh'); 61:9 / 61:14 kök ظهر ('li-yuzhirahû' Allah / 'zâhirîn' inananlar); 57:3 / 40:29 / 61:14 lemma 'zâhir' (Allah adı / kavim / inananlar)",
  "adsız (aday 1017): 61:8 söndürmek isteyenler; 61:9 elçi; 61:10 konuşan 1S; 61:13 'beşşir' muhatabı; 61:14 iki 'tâ'ife', düşmanlar, konuşan 1P — ad verilmedi; Îsâ, Meryem, İsrâ'îl, 'adn' ölçümde adlı",
  "kapanan sûre içi eşler: 61:2 → 61:10 → 61:14 ('yâ eyyuhe'llezîne âmenû', nakarat3 GEÇER); 61:6 → 61:14 ('qâle îsa'bnu meryem', GEÇER; 'benî isrâ'îl'); 61:4 → 61:13 (حبب [2/2]); 61:6 → 61:13 (بشر [2/2]); 61:9 → 61:14 (ظهر [2/2]); 61:4 → 61:11 (سبل [2/2]); sûre içinde açık eş kalmadı",
  "fâsıla: bu blokta kafiye kırığı 0 (sûre içi kırık 61:4, blok 1-7); 61:10, 12 م, diğerleri ن",
  "karşıt çift (aday 1039, okuma): 61:8 'li-yutfi'û' / 'mutimm'; 61:9 'dînu'l-haqq' / 'ed-dînu kulluh'; 61:10 'ticâret' / 'azâb'; 61:10 / 61:12 azap / cennet; 61:12 / 61:13 âhiret / dünya karşılığı; 61:14 'âmenet' / 'keferet'; 61:11 yok — kayıt, test yok",
  "okuma: 9:32 → 61:8; 9:33, 48:28 → 61:9; 9:24, 9:111 → 61:10; 9:20 → 61:11; 33:71, 58:22, 9:72 → 61:12; 48:18, 10:87 → 61:13; 58:22, 57:3, 40:29 → 61:14 — KAPATILAMAZ",
  "tetik: ön kuru koşu 1 uyuşmaz (61:12 ◈K نهر) → satır dolduruldu; kayıtta 0 uyuşmaz; [x/y] 0 (74 sayım)",
 ],
}

DUZELTME = {
}
