# -*- coding: utf-8 -*-
"""kasas_kapanis.py — sûre 28 (Kasas) kapanış notları, çıpa tablosu ve ilerleme kaydı."""
import json
import gloss_gecis

ATLAMA = {
 "_cipa_tablosu_28": (
  "SÛRE 28 ÇIPA KAYITLARI (aday 897'nin L0-L4 tanımıyla). **L0 1:** 28:7 (ٱلْيَمّ — bir su "
  "kütlesi adlandırılıyor, başka bir şey söylenmiyor; 27:24 ve 27:82 ölçütüyle aynı yerde). "
  "**L1 3:** 28:4 (شِيَعًا — sınıflama var ama olguya değil topluluğa uygulanıyor, 27:17 ile "
  "aynı) · 28:14 (أَشُدّ + ٱسْتَوَىٰ — gelişim eşiği iki terimle adlandırılıyor, ölçü/mekanizma "
  "yok) · 28:73 (gece/gündüz adlandırılıp işlevi veriliyor). **L2 3:** 28:10 (لَوْلَآ أَن "
  "رَّبَطْنَا — karşı-olgusal nedensellik, ama bağlanan şey bir iç hâl, olgu değil; 27:62 ile "
  "aynı) · **28:71 ve 28:72 (إِن جَعَلَ ... سَرْمَدًا — karşı-olgusal nedensellik ve bağlanan "
  "şey GERÇEK BİR DOĞA OLGUSU: gece-gündüz döngüsü).** **L3 0 · L4 0.** "
  "**28:71-72 sûrenin tek gerçek doğa-olgusu çıpası ve okumada L2'nin ilk kez bir olguya "
  "uygulandığı yer.** Hiçbir ayette 🜁/🜂 YAZILMADI: sûrenin sekiz ★★★'ının sekizi de hapaks ya "
  "da tam edilgenlik kaynaklı, yani içerikle ilgisiz; çıpa taşıyan üç L2 ayetinin hiçbiri ★★★ "
  "değil. **Çıpa ile yıldız sûre 28'de HİÇ çakışmıyor — aday 897 için birinci dereceden veri.**"),

 "_yildiz_kaynagi_28": (
  "SÛRE 28 YILDIZ KAYNAK TABLOSU (27 yıldızlı ayet): **pas 9 · hapaks 7 · rab 5 · n 3 · allah 2 "
  "· kafiye kırılması 1 · İÇERİK 0.** ★★★'ların tamamı (8) iki otomatik tetikleyiciden: hapaks "
  "ayetleri 28:15, 23, 29, 30, 34, 42, 76 (yedi) + tam-edilgen ayet 28:70 (bir). **Kesişim yok, "
  "fazla yok, eksik yok** — korpus çapında ölçülen kural (358 hapaks ayeti + 124 tam-edilgen "
  "ayet, hepsi ★★★) sûre düzeyinde birebir örtüşüyor. PAYDA ETKİSİ dört ayrı ölçütte "
  "gösterildi: rab (28:17 n=9 ★★ / 28:24 n=15 yıldızsız, aynı token sayısı) · hapaks (28:41 ★ / "
  "28:42 ★★★, fark bir kökün korpus sıklığı) · pas (28:64 1/7 yıldızsız / 28:70 1/1 ★★★, aynı "
  "edilgen sayısı) · **allah (28:71 n=19 ★ / 28:72 n=21 yıldızsız — aynı dokuz kelimelik "
  "nakaratı paylaşan, i'râb profilleri birebir aynı iki ayet; tek fark iki kelimelik uzunluk).**"),

 "_esit2_esik_bandi_28": (
  "SÛRE 28'DEN ÇIKAN esit2 EŞİK KÜMESİ (P0 #3 için hazır sınama kümesi). TAM eşleşme 3 "
  "(28:1↔26:1 · 28:2↔26:2 · 28:62↔28:74, üçü de 1,0). BENZER 3: 28:69↔27:74 **0,9455** (fark "
  "bir te'kid إِنَّ + lâm) · 28:14↔12:22 **0,9412** (fark tek kelime ٱسْتَوَىٰ) · 28:2↔12:1 "
  "**0,9231** (fark bir mukattaa). **YAZILMAYAN ama GERÇEK olan 3:** 28:2↔31:2 **0,8333** (fark "
  "tek sıfat) · 28:31↔27:10 **0,8252** (ON İKİ KELİME birebir ortak, uzunluk farkı 0,014 yani "
  "eleme geçiliyor, eşiğin 0,025 altında düşüyor) · 28:32↔27:12 **0,7152** (sekiz kelime ortak, "
  "uzunluk farkı 0,281 ile ÖN ELEMEYE takılıyor, orana hiç bakılmıyor). "
  "**'yakin' kademesi (≥0,95) sûre boyunca BİR KEZ BİLE tetiklenmedi; gerçek bağlar 0,82-0,95 "
  "bandında yoğunlaşıyor ve kademe sınırı bandın ÜSTÜNDE duruyor.** TAM SAYIM: korpusta en az on "
  "kelimelik birebir ortak iskelet dizisi paylaşan 111 ayet çifti var; esit2 31'ini (%27,9) "
  "görüyor, 80'ini görmüyor, görmediklerinin 66'sı çapraz-sûre yani nakarat2 de ulaşamıyor."),

 "_nakarat2_bilanco_28": (
  "SÛRE 28 nakarat2 BİLANÇOSU. **Süzgeci GEÇEN 11 kalıp:** يوم يناديهم يقول اين شركاءا الذين "
  "كنتم تزعمون (8 kelime, tür 'tam', 28:62↔28:74 — sûrenin TEK tam-ayet nakaratı) · سرمدا الا "
  "يوم القيمه من اله غير الله ياتيكم (9 kelime, sûrenin en uzun kalıbı) · قل ارءيتم ان جعل الله "
  "عليكم (6) · لكن اكثرهم لا يعلمون (4, 28:13↔28:57, kırk dört ayetlik açıklık) · لا اله الا هو "
  "(4, 28:70↔28:88) · له الحكم اليه ترجعون (4, 28:70↔28:88) · ان الله لا يحب (4) · قال رب انا "
  "(3 ayet: 28:16, 24, 33) · ان الله لا (3 ayet) · يوم القيمه من (3 ayet) · يوم يناديهم يقول "
  "(3 ayet). **GEÇEMEYEN 7 kalıp, yedisi de 2 ayet/3 kelime:** فرعون همن جنودهما · جاء بالهدا من "
  "· ما كنت بجانب · رحمه من ربك · مثل ما اوتا · من القوم الظلمين · ءامن عمل صلحا. "
  "**Süzgeç tutarlı ve sınır KESKİN: geçenlerin hepsi ya ≥4 kelime ya 3 ayet; geçemeyenlerin "
  "hepsi 2 ayet ve 3 kelime.** Ama ALT SINIRIN ALTINDA kalan sekiz tekrar HİÇ ölçülmüyor: "
  "خَآئِفًا يَتَرَقَّبُ (28:18↔28:21) · أَخَافُ أَن (28:33↔28:34) · فِى ٱلْيَمِّ (28:7↔28:40) · "
  "ما كنت (28:44 ×2, 45, 46 — üç ardışık ayet) · نمكن لهم (28:6↔28:57) · عسا ان (28:9, 22, 67) "
  "· تسكنوا فيه (28:72↔28:73) · ظَهِيرًا لِ (28:17↔28:86). **Sorun eşikte değil, üç kelimelik "
  "alt sınırın altındaki katmanın hiç ölçülmüyor olmasında.**"),

 "_esma_28": (
  "SÛRE 28 ESMÂ ÇAPRAZ TABLOSU (19 token, gönderge ELLE doğrulandı). **Mühürlü 2 → 2 GEÇERLİ** "
  "(28:16 غَفُور|رَحِيم, gönderge هُوَ, mercii رَبِّ). **Mühürsüz 17 → 2 GEÇERLİ, 15 ARTEFAKT.** "
  "Geçerli mühürsüzler: 28:28 وَكِيل (gönderge ٱللَّه) ve 28:58 وارِث (gönderge نَحْنُ). KONUM "
  "kırılımı: orta 7 token → 1 geçerli (o da mühürlü) · son 12 token → 3 geçerli. **Mühürsüzler "
  "içinde orta 6/6 ARTEFAKT, son 9/11 artefakt.** En sert artefakt 28:15: مُبِين tokeninin "
  "göndergesi ŞEYTAN. **وارِث tokeni sûrede İKİ KEZ ve hükümleri ZIT** — 28:5 ezilen halk "
  "(artefakt) / 28:58 konuşan ilâhî ses (geçerli); ikisi de son konumda, ikisi de mühürsüz, "
  "**mühür alanı ikisini ayırt edemiyor.** TAM SAYIM: وارِث korpusta 7 esmâ tokeni ve yedisi de "
  "mühürsüz; üçü geçerli (15:23, 21:89, 28:58), dördü artefakt (2:233, 23:10, 26:85, 28:5). "
  "Sûre 27'de mühürlü 12/12 geçerli ve mühürsüz 20/21 artefaktti; **iki sûrede de mühür POZİTİF "
  "filtre olarak kusursuz, NEGATİF filtre olarak değil** (aday 865'in bulgusu ikinci sûrede de "
  "doğrulandı)."),

 "_sure_28_kapanis": (
  "SÛRE 28 (KASAS) KAPANIŞ — HAM SAYIMLAR. 88 ayet · ortalama n=16,25 · fâsıla 81 ن + 3 م + 2 ل "
  "+ 1 ر çifti + 1 mukattaa; SINIF olarak 84 N + 2 ل + 2 R + 1 ٓ · kafiye kırılması **1** "
  "(28:28). YILDIZ: ★★★ 8 · ★★ 6 · ★ 13 · yıldızsız 61 (%69,3). EKSEN: lafız 27 token / 21 ayet "
  "· Rab 19 token / 19 ayet → A/R = 1,42. **28:1-12 lafızsız VE Rabsız** (tam sayım: korpusta "
  "böyle 1074 dizi var, bu 56. sırada, ≥10 uzunlukta 80 dizi — OLAĞANDIŞI DEĞİL, NULL). Buna "
  "karşılık 28:71-80 bloğu tek başına 11 lafız taşıyor. İLTİFÂT **0/88** — sûre 27'de 3'tü. "
  "HAPAKS: 7 ayet, 8 kök (وكز · ذود · جذو · بقع · ردأ+فصح · قبح · نوأ). EDİLGEN: 18 ayet. "
  "AKTÖR: adlı 37 token (مُوسَى 18 · فِرْعَوْن 8 · هامان 3 · مَدْيَن 3 · قارُون 2 · شَيْطان 1 · "
  "هارُون 1 · **قُرْءان 1, tür 'kitab' — kişi/kavim olmayan tek aktör**), adsız 8 token (karye 3 "
  "· imrae 2 · racül 2 · tâife 1). YENİ KÖK 20 → kok_turkce 1032'den **1052**'ye. `harf` 6150 → "
  "`harf3` **5861**, isaret 270 (**%4,4** — onarım turunun %5,3 tahminine yakın). mm2: **1 ayet "
  "/ 2 kayıt** (28:61). esit2 dolu 6 ayet. İÇ DÜĞÜM **1** (28:37↔28:85, kırk sekiz ayetlik "
  "açıklık, kapandı). 529 KÜMESİ: sûreden **on iki yeni vaka** (ظلل · حيي · بني · أنس · نور · "
  "مدن · قصص · سلم · خير · ظهر · أمم · نهر) ve iki OLUMLU örnek (علو ve كبر karşılıkları iki "
  "anlam alanını da taşıyor). ANLATI BÖLÜTLERİ: Mûsâ 40 ayet (1-46) · Ehl-i kitap ve tevhid 29 "
  "ayet (47-75) · Kārûn 8 ayet (76-83) · kapanış 5 ayet (84-88)."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
ATLAMA = {k: gloss_gecis.gecir(v) for k, v in ATLAMA.items()}
OM['28'].setdefault('_mercek_atlama_notu', {}).update(ATLAMA)
OM['ilerleme']['tam'] = sorted(set(OM['ilerleme']['tam']) | {27, 28})
OM['ilerleme']['not'] = ("Sûre 1, 9-27 ve **28 TAM**. Devam: sûre 2'den (21. ayet) ya da yeni sûre.")
OM['ilerleme']['okunan_ayet'] = 2130
OM['ilerleme']['korpus_yuzde'] = 34.2
OM['ilerleme']['son_oturum'] = 'OTURUM_2026-09-16_KASAS.md'
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 28 →', len([k for k in OM['28'] if not k.startswith('_')]),
      'ayet + ', len(OM['28']['_mercek_atlama_notu']), 'kapanış notu')
print('ilerleme:', OM['ilerleme']['okunan_ayet'], 'ayet (%', OM['ilerleme']['korpus_yuzde'], ')')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK['28_atlama'] = ATLAMA
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: 28_atlama →', len(MK['28_atlama']))
