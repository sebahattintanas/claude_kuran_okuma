# -*- coding: utf-8 -*-
"""rum_kapanis.py — sûre 30 (Rûm) kapanış notları, çıpa tablosu ve ilerleme."""
import json
import gloss_gecis

ATLAMA = {
 "_cipa_tablosu_30": (
  "SÛRE 30 ÇIPA KAYITLARI — **dokuz çıpa, biri okumanın ÜÇÜNCÜ L4'ü ve boş kalan üçüncü kolu dolduruyor.** "
  "**L4 (MEKANİZMA) 30:48** — beş aşamalı bir süreç, her aşama adlandırılmış ve her biri bir öncekinden فَ ile "
  "türetilmiş: rüzgârların gönderilmesi → bulutun kaldırılması (فَتُثِيرُ سَحَابًا) → gökte yayılması "
  "(فَيَبْسُطُهُۥ) → parçalara ayrılması (وَيَجْعَلُهُۥ كِسَفًا) → yağmurun aradan çıkması (فَتَرَى ٱلْوَدْقَ "
  "يَخْرُجُ مِنْ خِلَٰلِهِۦ). Ara durumlar adlandırılıyor (سَحَاب, كِسَف, وَدْق) ve çıkışın yeri belirtiliyor. "
  "**L4'ün üç kolu artık örneklenmiş: ölçü 29:14 · sınıflama 29:40 · mekanizma 30:48.** "
  "**L2 sekiz kayıt:** 30:11 ve 30:27 (بدأ+عود döngüsü, emsal 29:19) · 30:19 (ölüden diri / diriden ölü / yerin "
  "dirilmesi) · 30:24 ve 30:50 (gökten su → yerin dirilmesi, emsal 29:63) · 30:40 (dört aşamalı döngü) · 30:46 "
  "(rüzgâr → gemilerin yüzmesi) · 30:54 (güçsüzlük → kuvvet → güçsüzlük). "
  "**MERDİVENİN ÇALIŞTIĞININ KANITI 30:24 → 30:48 karşılaştırması:** aynı olgu (yağmur), 30:24'te iki aşamada "
  "verilip L2, 30:48'de ara aşamalar açılınca L4. **Merdivenin aynı olguda iki farklı basamak verebildiğinin ilk "
  "ölçülü örneği.** "
  "**ÇIPA OLMAYAN ama kademe taşıyan dört ayet:** 30:9 ve 30:42 (L1, tarihe bakış — عقب dışlaması) · 30:33 ve "
  "30:51 (L2, olgu=HAYIR — davranış düzenliliği) · 30:41 (L2, olgu=HAYIR ama SINIRDA). "
  "Beş sûrede 379 okunan ayet, üç L4: **%0,8.**"),

 "_tarayici_cokusu_30": (
  "**TARAYICI SÛRE 30'DA ÇÖKTÜ — anma 2/9, kesinlik 2/5.** Sûre 27'de 4/4, sûre 28'de 3/3, sûre 29'da "
  "(düzeltilmiş) 3/3 idi. **Yedi çıpa kaçtı ve yedisinin ortak özelliği tek: DÜZ HABER CÜMLESİ.** Tarayıcının "
  "yedi işaret ailesi (A_şart · A_levlâ · B_ta'lîl · C_recâ · D_yeti · E_görünüş · F_ölçü · G_bakış) bir SÖZ "
  "EYLEMİ işareti arıyor — şart, ta'lîl, recâ, yeti sınırı, görünüş, ölçü ya da gözleme çağrısı. "
  "**TAM SAYIM — körlüğün boyutu: 3+ olgu kökü taşıyan 221 ayetin 135'i (%61) hiçbir işaret ailesi "
  "tetiklemiyor; bunların 22'si أيي kökü taşıyor, yani 'âyetlerinden biri de' dizisinden.** Sûre 30'da 3+ olgu "
  "köklü on ayetin sekizi kaçıyor (30:8, 30:19, 30:22, 30:23, 30:24, 30:27, 30:40, 30:48). "
  "**Bu, aday 924'ün denemesine ÜÇÜNCÜ katmanı ekliyor:** v2 kök listesine, v3 işaret ailelerine, v4 lemmaya "
  "bağlandı — **ama üç sürümün ortak varsayımı 'çıpa bir söz eylemi işareti taşır' ve sûre 30 bu varsayımı "
  "çürütüyor.** Sûre 27-29 varsayımı doğrulamış görünüyordu çünkü **o sûrelerin çıpaları tesadüfen işaretliydi.** "
  "**İKİ DOĞRU POZİTİF:** 30:46 (B_ta'lîl + C_recâ) ve 30:50 (G_bakış'ın EMİR kolu — aday 924'ün kararı burada "
  "karşılığını veriyor). **VE 30:46 ANCAK BU OTURUMDAKİ BİR ONARIM SAYESİNDE GÖRÜNÜYOR:** anahtar_denetim.py "
  "olgu kümesindeki ريح yazımının korpusta bulunmadığını, rüzgârın روح kökü altında (LEM:رِيح) olduğunu yakalamıştı "
  "(aday 946); düzeltme olmasaydı sûrenin en açık L2'lerinden biri havuza hiç girmeyecekti."),

 "_onarim_sinamalari_30": (
  "SÛRE 30, BU OTURUMDA YAPILAN ONARIMLARIN TUTULAN KÜMEDEKİ İLK SINAMASI — **dördü de tuttu.** "
  "**(1) ريح → روح (aday 946):** 30:46'da çıpa ancak düzeltmeyle görünüyor — onarımın ilk fiilî kazancı. "
  "**(2) هوي BAGLAM_GEREKLI listesine (aday 945):** 30:29'da أَهْوَآءَهُم açıkça 'hevesler' ve olgu değil; kök "
  "olgu kümesinden çıkarılmıştı ve karar doğru çıktı. "
  "**(3) قدر lemma süzgeci (aday 944):** 30:37'de رأي + INTG var, yani G_bakış'ın iki şartı sağlanıyor; üçüncü "
  "şart sağlanmıyor çünkü قدر burada يَقْدِرُ (lemma قَدَرَ) ve onarılmış tabloda bu lemma olgu değil. "
  "**Lemma süzgeci tam olması gerektiği gibi çalışıyor: rızkın genişletilmesi bir doğa olgusu değil.** "
  "**(4) عقب dışlaması (aday 924):** 30:9 ve 30:42'de İKİ KEZ doğru negatif. 30:42 kalıbı hem نظر hem emir "
  "kipiyle taşıyor — dışlama olmasaydı kesin aday olurdu. "
  "**YAN NOT:** okuma bu sûrede ilk kez ONARILMIŞ alanlarla koşuldu (hapaks2 · fig2 · nakarat3 · yildiz2 · z2 · "
  "tarayıcı v4). Sûre 30 onarımlardan ETKİLENMEDİ — yıldız değişimi yok, hapaks aynı, fig2'de yalnız sıra farkı "
  "— **yani sûre 27-29 ile karşılaştırılabilir kalıyor.**"),

 "_yildiz_kaynagi_30": (
  "SÛRE 30 YILDIZ KAYNAK TABLOSU (15 yıldızlı ayet): **pas 4 · allah 4 · n 3 · kafiye 2 · hapaks 1 · rab 1 · "
  "İÇERİK 0.** **Altı sûre boyunca kesintisiz: içerik 0.** Yıldızlı oran %25,0 — dört sûrenin en düşüğü. "
  "★★★ üç ayet: **30:2** (tek fiil edilgen, pas z=5,38 — aday 903'ün ikinci tetikleyicisi dördüncü sûrede, ve "
  "**okumada ★★★ alan en kısa ayet: İKİ kelime**) · **30:6** (allah z=3,11) · **30:17** (**hapaks z=3,38 VE "
  "allah z=2,80 — İKİ ÖLÇÜT BİRDEN eşiğin üstünde**). "
  "**30:17 okumada ★★★'ı iki bağımsız kaynaktan alan ilk ayet. TAM SAYIM: korpusta iki+ ölçütü |z|>2 olan 89 "
  "ayet; 30:17 sûre 30'daki tek örnek. Formül en büyüğünü alıyor, TOPLAMIYOR — iki bağımsız olgunun birlikteliği "
  "ölçümde kayboluyor.** "
  "**PAYDA SERİSİ altıncı ve yedinci vakayla:** 29:5 (2 lafız/12 kelime → 2,80) · 29:11 (1/6 → 2,80) · 30:5 "
  "(1/8 → **1,97**) · 30:6 (2/11 → 3,11) · 30:11 (1/8 → **1,97**) · 30:59 (1/8 → **1,97**) — **aynı oran üç kez "
  "aynı z'yi veriyor.** Ve allah z=**1,47** üç kez eşiğin 0,03 altında (29:6, 29:44, 30:60), üçü de yıldızsız. "
  "**`pas` determinizmi BEŞİNCİ doğrulama:** 28:60 · 28:88 · 29:18 · 29:49 · 30:49 — hepsi bir edilgen / iki "
  "fiil → z=2,52 → ★★. "
  "**KAFİYE: sûre 30'da iki kırılma (30:50, 30:54) ve İKİSİ DE yalnız kafiyeden ★** — okumada dördüncü ve "
  "beşinci vaka (öncekiler 28:28, 29:21, 29:22)."),

 "_esit2_30": (
  "SÛRE 30 `esit2` KAYITLARI — **okumanın en yüksek değerleri ve iki yapısal bulgu.** "
  "**(1) İKİ ARDIŞIK AYET, İKİ ARDIŞIK AYETE:** 30:52 ↔ 27:80 (**0,9888**) ve 30:53 ↔ 27:81 (**0,9905**). "
  "Okumada ilk kez bir ayet ÇİFTİ, başka bir sûredeki ayet ÇİFTİNE sırasıyla bağlanıyor — ve 0,9905 mukattaa "
  "TAM'ları dışında ölçülen en yüksek değer. **Karşı uç OKUNMUŞ bir bölüt olduğu için doğrulanabilir durumda.** "
  "**`esit2` bunu iki ayrı ikili bağla veriyor; çiftin çifte bağlandığını gören alan yok — alan AYET düzeyinde "
  "çalışıyor, BÖLÜT düzeyinde değil.** "
  "**(2) ADAY 929'UN ÜÇLÜSÜ TAMAMLANDI:** 30:34 okununca üçlü {16:55, 29:66, 30:34} üç uçtan da görüldü ve "
  "**eşkenar olmadığı** ortaya çıktı — 30:34↔16:55 = **1,0 TAM**, 30:34↔29:66 = 0,9275, 29:66↔16:55 = 0,9275. "
  "**Alan üçlüyü üç ikili bağla veriyor ve bağların AĞIRLIKLARI FARKLI; küme yapısı ancak üç ayetin üçü de "
  "okunduğunda görünüyor.** "
  "**(3) İKİNCİ 'YAKIN' KADEMESİ 30:37 ↔ 39:52 (0,9649)** — birincisi 29:28 ↔ 7:80 (0,9615). Sûre 30 bu kademeyi "
  "ÜÇ kez veriyor (30:37, 30:52, 30:53); sûre 27 ve 28'de hiç tetiklenmemişti. "
  "**(4) `xref` YOĞUN, `esit2` BOŞ — blok 4'te üç kez:** 30:33 (üç 3-gram) · 30:36 (**beş 3-gram'ın dördü "
  "42:48'e**) · 30:38 (**üç 3-gram'ın üçü de 17:26'ya**). Aday 929'un kademe dağılımı açıklıyor: **üç kademenin "
  "toplamı 1986 ayet, korpusun üçte biri; geri kalan örtüşmeler hiçbir kademeye girmiyor.**"),

 "_merdiven_bosluklari_30": (
  "MERDİVENDE İKİ BOŞLUK DAHA — ikisi de KAPATILAMAZ. "
  "**(1) KARŞILAŞTIRMALI SIRALAMA, okumada DÖRT vaka:** 29:41 (أَوْهَنَ ٱلْبُيُوتِ) · 30:10 (ٱلسُّوٓأَىٰ) · "
  "30:27 (أَهْوَنُ عَلَيْهِ) · 30:38 (ذَٰلِكَ خَيْرٌ). Dördü de bir nesneyi ya da durumu bir sınıfın ucuna "
  "yerleştiriyor; birim yok, mekanizma yok, görünüş/durum ayrımı yok. **L0-L4 merdiveninde bu iddia türü için "
  "basamak yok ve dördü de L1'e sıkışıyor.** "
  "**(2) DEĞİŞMEZLİK / DÜZENLİLİK İDDİASI, ilk vaka:** 30:30 لَا تَبْدِيلَ لِخَلْقِ ٱللَّهِ. Mekanizma yok, ölçü "
  "yok, nedensellik yok — ama bir DÜZENLİLİK iddia ediliyor. L1 verildi. "
  "**(3) 'OLGU' BAYRAĞININ TANIM BOŞLUĞU — 30:41:** kara ve deniz olgu kökleri ve iddia onlarda gerçekleşen bir "
  "DEĞİŞİMİ bildiriyor (ظَهَرَ ٱلْفَسَادُ فِى ٱلْبَرِّ وَٱلْبَحْرِ), nedensellik açık. Ama iddianın öznesi "
  "ٱلْفَسَاد — bir doğa süreci değil. **Bayrak, olgunun KONUSU mu yoksa YERİ mi sayılacağını tanımlamıyor ve "
  "sûre 27-30'da bu ilk kez belirleyici oldu.** L2/olgu-hayır verildi; **tanım netleşmeden benzer vakalar "
  "tutarsız kalır.**"),

 "_alan_bulgulari_30": (
  "SÛRE 30'DA ÖLÇÜLEN ALAN DAVRANIŞLARI. "
  "**(1) `say` ALANI ÖLÇÜYÜ GÖRMÜYOR — sûrede ÜÇ vaka.** 30:4'te بِضْع (birkaç yıl): alan on yedi sayı kökü "
  "tanıyor ve بضع aralarında yok; kökün geçtiği altı ayetin altısında da alan boş. **Bu, F_ölçü işaret ailesinin "
  "kör noktası ve tam da ölçülü bir öngörünün üzerinde** — 29:14'ün أَلْفَ سَنَةٍ إِلَّا خَمْسِينَ عَامًا'sı L4 "
  "(ölçü) olmuştu, bu ayet aynı yapıyı daha zayıf hâliyle taşıyor. 30:17-18'de **dört vakit** sıralı olarak "
  "sayılıyor (akşam, sabah, ikindi, öğle) ve hiçbir alan bunu bir DİZİ olarak tutmuyor. 30:40'ta **dört aşamalı "
  "döngü** aynı şekilde karşılıksız. **Alan SAYIYI sayıyor, ÖLÇÜYÜ değil.** "
  "**(2) NADİRLİK YIĞILMASI ≠ HAPAKS — sûrede DÖRT vaka** (28:12'nin ayrımı): 30:15 (روض 2 ayet + حبر 6) · "
  "30:48 (**ودق 2 ayet + كسف 5 + سحب 11 — okumada ölçülen en yoğun örnek**) · 30:57 (عتب 4 ayet + عذر 11) · "
  "30:54 (شيب 3 ayet). **Hiçbiri hapaks2 değil ve her seferinde ayet dar köklerden değil başka ölçütten nişan "
  "alıyor ya da hiç almıyor.** "
  "**(3) `nakarat3` ile `dugum.ic` AYNI KALIBA FARKLI DAVRANIYOR — üçüncü örnek:** 30:30 ↔ 30:43 (فاقم وجهك "
  "للدين, üç kelime) `nakarat3` süzgecini GEÇEMİYOR ama `dugum.ic` ikisini de 1 sayıyor. Sebep: dugum lemma "
  "3-gram'ı, nakarat3 yüzey/lemma n-gramı + süzgeç kullanıyor. "
  "**(4) `pas` ALANI ISM-İ MEF'ÛLÜ SAYMIYOR:** 30:15 (يُحْبَرُونَ) ★ alıyor, 30:16 (مُحْضَرُونَ) almıyor — iki "
  "ayet aynı çatıda ama ölçüm ikisini farklı sayıyor. "
  "**(5) `sim` ALANI METNİN SİMETRİSİNİ GÖRMÜYOR:** 30:44 tam simetrik bir karşıtlık taşıyor (مَن كَفَرَ ... "
  "وَمَنْ عَمِلَ صَٰلِحًا) ve `sim` None veriyor; daha az simetrik ayetlerde dolu."),

 "_sure_30_kapanis": (
  "SÛRE 30 (RÛM) KAPANIŞ — HAM SAYIMLAR. 60 ayet · ortalama n=13,62 · fâsıla SINIF olarak 57 N + 2 R + 1 "
  "mukattaa · kafiye kırılması **2** (30:50, 30:54, **ikisi de yalnız kafiyeden ★**). "
  "YILDIZ (onarılmış yildiz2): ★★★ 3 · ★★ 3 · ★ 9 · yıldızsız 45 (**%25,0 — dört sûrenin en düşük yıldızlı "
  "oranı**). EKSEN: lafız **24 token / 21 ayet** · Rab **3 token / 2 ayet** → **A/R = 8,00**; sûre 29'un 8,4'üne "
  "çok yakın, sûre 27'de 2,25 ve sûre 28'de 1,42 idi — **iki ardışık sûre lafız ağırlıklı.** "
  "İLTİFÂT **1** (30:17, yön 13>2). HAPAKS **1 ayet** (30:17, مسو — korpusta TEK ayet ve tek token). EDİLGEN 8 "
  "ayet. "
  "ESMÂ **14 token: mühürlü 6, mühürsüz 8.** Mühürlü üç çift → **3/3 GEÇERLİ** (عَزِيز|رَحِيم 30:5 · "
  "عَزِيز|حَكِيم 30:27 · عَلِيم|قَدِير 30:54); عَزِيز iki çiftte ortak, ikinci terim değişiyor. Mühürsüz 8 → "
  "**1 geçerli** (30:50 قَدِير), **7 artefakt**. **DÖRT SÛREDE MÜHÜRLÜ YANLIŞ POZİTİF SIFIR** (27: 12/12 · 28: "
  "2/2 · 29: 8/8 · 30: 6/6). "
  "AKTÖR: adlı **2 token** — رُوم (tür KAVİM, 30:2) ve قُرْءان (**tür KİTAB**, 30:58; okumada seyrek bir tür); "
  "adsız **1** (30:33 ferîk). **Okumanın en az adlı aktörlü sûresi** (28'de 37, 29'da 21). "
  "YENİ KÖK **10** → kok_turkce 1059'dan **1069**'a. harf 3654 → harf3 **3434**, isaret 201 (**%5,5**). "
  "mm2 **1** (30:25 دَعَاكُمْ دَعْوَةً — onarılmış alan üç sûrede dört kayıt). "
  "İÇ DÜĞÜM **9 ayet / 4 küme**: 30:9↔30:42 (beş kelime) · 30:11↔30:27 (dört kelime) · **30:12↔30:14↔30:55 (üç "
  "uçlu, kırk üç ayetlik açıklık)** · 30:30↔30:43. `nakarat3` dolu **31 ayet**; `ikili` dolu **32 ayet** (bu "
  "oturumda eklenen alan). "
  "529 KÜMESİ: sûreden **altı yeni vaka** — خلف (ardından gelme / caymak / farklılık, ÜÇ anlam) · ظهر (görünen "
  "yüz / öğleye ermek / belirmek, ÜÇ anlam) · سمو (gökler / adlandırılmış, **tek ayette 30:8**) · سوع (Kıyamet / "
  "bir saat, **tek ayette 30:55**) · نهر (gündüz, tablo 'ırmak') · برر (kara, esmâ artefaktı). **İkisi tek ayette "
  "iki anlam taşıyor — kümenin en keskin vakaları.** "
  "KOMŞULUK ÖLÇÜMÜ: sûrede **dört kez** metnin yakın geleceğini haber verdi (30:11 بدأ+عود · 30:36 رحم+قنط · "
  "30:46 سخر→فلك · 30:24 خوف+طمع) ve **30:59'da İLK KEZ SÛRE SINIRINI AŞTI**: 29:21'de قلب profilinde طبع ×39,4 "
  "durmuştu ve 'lemma yanlış' diye kaydedilmişti; otuz dokuz ayet ve bir sûre sonra kalıp DOĞRU lemmayla metne "
  "girdi."),
}

ATLAMA = {k: gloss_gecis.gecir(v) for k, v in ATLAMA.items()}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
OM['30'].setdefault('_mercek_atlama_notu', {}).update(ATLAMA)
OM['ilerleme']['tam'] = sorted(set(OM['ilerleme']['tam']) | {30})
OM['ilerleme']['not'] = "Sûre 1, 9-29 ve **30 TAM**. Devam: sûre 31'den ya da sûre 2'nin 21. ayetinden."
OM['ilerleme']['okunan_ayet'] = 2259
OM['ilerleme']['korpus_yuzde'] = 36.2
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 30 →', len([k for k in OM['30'] if not k.startswith('_')]),
      'ayet +', len(OM['30']['_mercek_atlama_notu']), 'kapanış notu')
print('ilerleme:', OM['ilerleme']['okunan_ayet'], 'ayet (%', OM['ilerleme']['korpus_yuzde'], ')')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK['30_atlama'] = ATLAMA
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: 30_atlama →', len(MK['30_atlama']))
