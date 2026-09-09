# -*- coding: utf-8 -*-
"""blok_27_1_10.py — sûre 27 (Neml) makro profil + ilk blok (27:1-10)."""
import json
DIK = json.load(open('blok_dikey_27_1_10.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MAKRO = {
 "_makro_temel": ("93 ayet · 1151 kelime · **12,38 kel/ayet** · Mekkî · nüzûl sırası 48. "
  "**Sûre 26'nın (5,81) İKİ KATINDAN fazla; okumada uzun ayetli sûreler grubunda** (sûre 24: 20,56 · "
  "sûre 25: 11,60 · sûre 23: 8,90). En uzun ayet 27:21 (n=61); en kısa 27:2 (n=3)."),
 "_makro_eksen": ("**Allah lafzı 27 (korpus tabanının 0,67 katı) · رَبّ *(Rab)* 12 (0,82 kat) · "
  "A/R = 2,25.** **OKUMADA İLK KEZ A/R > 1.** Karşılaştırma: sûre 23 → 0,57 · sûre 25 → 0,57 · "
  "sûre 26 → **0,36** · sûre 27 → **2,25**. Sûre 24'te Rab sıfırdı (A/R tanımsız). **'Mekkî 0,57' "
  "hipotezi sûre 26'da düşmüştü (aday 601 kümesi); sûre 27 onu TERS YÖNDEN de düşürüyor.** "
  "İlk lafız 27:8 (göreli konum 0,086) — sûre 25'te 0,22, sûre 26'da 0,39; **lafız gecikmesi de "
  "sûreye özgü, Mekkî'ye özgü değil** (aday 527/665). İlk Rab 27:8'de, aynı ayette."),
 "_makro_fasila": ("**Fâsıla: 93/93 N sınıfı** (ن 84 · م 9). **KIRILMA SIFIR** — sûre 26'da dört "
  "kırılma vardı ve dördü de aynı özel addı (aday 612/751). Sûre 27'de fâsıla kısıtı tam "
  "korunuyor; bu, aday 600'ün (fâsıla kısıtı karıştırıcısı) sûre 27'de de geçerli olacağı anlamına "
  "gelir."),
 "_makro_yildiz": ("**★★★ 9 (%9,7) · ★★ 9 · ★ 10 · yıldızsız 65.** ★★★ ayetler: 27:6, 8, 17, 19, "
  "20, 25, 39, 68, 88. **Sûre 26'nın ham payı %18,1, nakarat düzeltmeli %11,9 idi; sûre 27 "
  "düzeltmesiz %9,7** — ve **nakarat SIFIR** olduğu için düzeltme gerekmiyor. **Bu, aday "
  "602/683'ün korpus taraması için TEMİZ bir karşılaştırma noktası:** uzun ayetli (12,38) ve "
  "nakaratsız bir sûre."),
 "_makro_nakarat_esit": ("**NAKARAT: SIFIR.** `esit` alanı dolu olan yalnız ÜÇ ayet (27:3 → 31:4 · "
  "27:58 → 26:173 · 27:71 → beş ayet). **Sûre 26'da 44 ayet `esit` doluydu ve çoğu nakarat "
  "kümelerindendi (aday 779).** Sûre 27, tekrar yapısı bakımından sûre 26'nın tam karşıtı ve bu, "
  "nakarat düzeltmesinin ne kadar büyük bir etken olduğunu gösteren doğal bir kontrol."),
 "_makro_esma": ("**Esmâ 33 token / 26 ayet / mühür 6.** Dağılım: مُبِين 6 · آخِر 4 · مُؤْمِن 3 · "
  "عَزِيز 3 · حَكِيم 2 · عَلِيم 2 · رَحِيم 2 · كَرِيم 2 · غَفُور · رَحْمٰن · مَلِك · قَوِيّ · "
  "غَنِيّ · وَلِيّ · سَلام · بَرّ · خَبِير birer. **ARTEFAKT ADAYLARI: مُبِين (6), آخِر (4), "
  "مُؤْمِن (3) — toplam 13 token, %39.** آخِر sûre 26'da da artefakttı (26:84). Mühürlü ayetler: "
  "27:6, 9, 11, 30, 40, 78 — **ve sûre 26'nın tersine mühür ÇİFTLERİ çeşitli** (حَكِيم|عَلِيم, "
  "عَزِيز|حَكِيم, غَفُور|رَحِيم, رَحْمٰن|رَحِيم…), tek bir çiftin tekrarı değil."),
 "_makro_diger": ("**İltifât 3** (27:6 yön 3>2 · 27:31 yön 3>12 · 27:69 yön 1>23) — sûre 26'da 15'ti "
  "(nakarat düzeltmeli ≤11). **Edim: haber 46 · soru 25 · emir 24 · nida 8 · yasak 3 · şart 2** — "
  "**soru payı okumada yüksek.** Biçim: DIKKAT 13 · HASR 10 · IDRAB 6 · NEHY 3 · QASEM 1 · AMMA 1 · "
  "**MM 1**. **QASEM 1 — sûre 26'da sıfırdı ve aday 672'de yanlış ölçüm çıkmıştı; burada tagger "
  "bir QASEM buluyor, denetlenecek.** İ'râb: GEN 192 · ACC 186 · NOM 119 (ACC payı 0,374). "
  "Edilgen 22 fiil / 16 ayet. Hapaks 5 ayette: 27:19 بسم *(gülümseme)* · 27:20 هدهد *(hüdhüd)* · "
  "27:25 خبأ *(gizleme)* · 27:39 عفر *(ifrît)* · 27:88 تقن *(sağlam yapma)* + جمد *(donuk durma)*. "
  "**Adlı aktör: سُلَيْمان 7 · قُرْءان 4 · مُوسَى 3 · داوُد 2 · لُوط 2** ve birer kez فِرْعَوْن, "
  "سَبَإ, شَيْطان, ثَمُود, صالِح, إِسْرائِيل, مُسْلِم. **Adsız aktör: 'imrae' 1 (27:23) — "
  "DENETLENECEK** (aday 462/579/641: adsız aktör sayımlarının %67'si artefakt çıkmıştı)."),
}

MEAL = {
1: "Tâ-Sîn. Bunlar Kur'ân'ın ve apaçık bir kitabın âyetleridir.",
2: "Müminler için bir kılavuz ve müjdedir.",
3: "Onlar namazı kılar, zekâtı verir ve âhirete kesin olarak inanırlar.",
4: "Âhirete inanmayanların işlerini kendilerine süslü gösterdik; onlar körü körüne bocalarlar.",
5: "Azabın en kötüsü onlar içindir; âhirette de en çok ziyana uğrayanlar onlardır.",
6: "Sen bu Kur'ân'ı, hikmet sahibi ve bilen bir katından almaktasın.",
7: "Hani Mûsâ ailesine demişti: Ben bir ateş gördüm; size ondan bir haber getireceğim ya da bir kor parçası getireceğim, belki ısınırsınız.",
8: "Oraya geldiğinde seslenildi: Ateşin içindekiler de çevresindekiler de mübarek kılındı. Âlemlerin Rabbi olan Allah yücedir.",
9: "Ey Mûsâ, o benim; Azîz ve Hakîm olan Allah.",
10: "Asânı at. Onu bir yılan gibi titreşir görünce arkasını dönüp kaçtı, geri dönmedi. Ey Mûsâ, korkma; benim katımda elçiler korkmaz.",
}

O = {
1: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُبِين *(apaçık)* 6. sırada = fâsıla, MÜHÜRSÜZ — "
 "ÖLÇÜM ARTEFAKTI**: gönderge كِتَاب *(kitap)*; sûrenin altı مُبِين tokeninin birincisi · "
 "**aktör: adlı قُرْءان *(Kur'ân)* 4. sırada, sınıf KİTAB, rol mecrur** · edim haber, kip işareti "
 "yok · **şahıs eki YOK, fiil YOK** · n=6 mora=41 harf=46 (n z=-0,68), fâsıla مُبِينٍ *(apaçık)* → "
 "ن, N sınıfı; **i'râb NOM 1 · GEN 3**; dış düğüm 0 · yıldız ★ yok · kökler أيي *(âyet, işaret)* · "
 "قرأ *(okuma)* · كتب *(yazma, kitap)* · بين *(arası; açıklama)* · bağt: **26:1 ile açılış "
 "karşılaştırması** — orada طسٓمٓ ve ayette KÖK YOKTU (okumada ▽ satırı yazılamayan tek ayet); "
 "burada طسٓ artı dört kök; **iki sûre aynı harf öbeğiyle açılıyor ama sûre 27'nin açılışı "
 "ölçülebilir içerik taşıyor** (elle, L1, aday 780)"),
2: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُؤْمِن *(mümin)* 3. sırada = fâsıla — ARTEFAKT**: "
 "gönderge İNSANLAR; sûre 26'da bu lemma on beş kez artefakt çıkmıştı (aday 601/709) · aktör yok · "
 "edim haber, kip işareti yok · **şahıs eki YOK, fiil YOK** · **n=3 — SÛRENİN EN KISA AYETİ** "
 "(n z=-1,00), fâsıla لِلْمُؤْمِنِينَ *(müminler için)* → ن, N sınıfı; **i'râb GEN 2 · NOM 1**; "
 "**dış düğüm 1** · yıldız ★ yok · kökler هدي *(yol gösterme)* · بشر *(müjde; beşer)* · أمن *(güven; "
 "iman)* · bağ: xref هدى *(hidâyet)* + بشرى *(müjde)* + مؤمن *(mümin)* → **2:97**; **25:56 ile "
 "بشر *(müjde; beşer)* karşılaştırması** — orada elçi مُبَشِّرا *(müjdeci)*, burada kitap بُشْرَىٰ "
 "*(müjde)*; **aynı kök, elçiden kitaba** (elle, L1, aday 781)"),
3: ("eksen: **lafız YOK · Rab YOK** · **esmâ آخِر *(sonraki)* 7. sırada, ORTA konum, MÜHÜRSÜZ — "
 "ÖLÇÜM ARTEFAKTI**: ٱلْءَاخِرَة *(âhiret)*, bir ZAMAN/YER adı; ölçüt (a) dışlıyor; sûrenin dört "
 "آخِر tokeninin birincisi · aktör yok · edim haber, kip işareti yok · **şahıs 3MP x8 — ayette "
 "başka şahıs yok**, iltifât 0 · n=9 mora=62 harf=48 (n z=-0,36), fâsıla يُوقِنُونَ *(kesin "
 "inanırlar)* → ن, N sınıfı; **i'râb ACC 2 · GEN 1**; **bab IV x3 — ayetin üç fiili de bab IV**; "
 "zaman IMPF x3; **dış düğüm 2** · yıldız ★ yok · **esit: 31:4 ile TAM AYET ÖZDEŞ** · kökler قوم "
 "*(kalkma; kavim; kıyamet)* · صلو *(namaz, salât)* · أتي *(gelme, getirme)* · زكو *(zekât, "
 "arınma)* · أخر *(geciktirme, sonraya bırakma)* · يقن *(yakîn, kesin bilgi)* · bağ: xref آتى "
 "*(verdi)* + زكاة *(zekât)* + آخر *(âhiret)* → **31:4 · 41:7**; **قوم burada 'namaz kılma' "
 "anlamında — 529 kümesine sûre 27'nin İLK vakası**; sûre 26'da aynı kök dört anlam alanındaydı "
 "(aday 769) (elle, L1, aday 782)"),
4: ("eksen: **lafız YOK · Rab YOK** · **esmâ آخِر = ORTA konum — ARTEFAKT, ikinci token** · aktör "
 "yok · edim haber, kip NEG 1 · şahıs 3MP x7 · 1P x2, iltifât 0 · n=10 mora=58 harf=45 (n z=-0,26), "
 "fâsıla يَعْمَهُونَ *(bocalarlar)* → ن, N sınıfı; **i'râb ACC 2 · GEN 1**; bab I x1 · II x1 · "
 "IV x1; zaman IMPF x2 · PERF x1; simetri [3,1,7,1]; dış düğüm 0 · yıldız ★ yok · kökler أمن "
 "*(güven; iman)* · أخر *(geciktirme, sonraya bırakma)* · زين *(süsleme)* · عمل *(iş, amel)* · عمه "
 "*(şaşkınlık, körü körüne bocalama)* · bağ: **27:3 ile TERS KUTUP çifti** — orada müminlerin üç "
 "eylemi (namaz, zekât, yakîn), burada inanmayanların hâli; **iki bitişik ayet, aynı آخِر kelimesi, "
 "iki kutup**; **عمه *(şaşkınlık, körü körüne bocalama)* korpusta 7 geçişli** (elle, L1, aday 783)"),
5: ("eksen: **lafız YOK · Rab YOK** · **esmâ آخِر = 8. sıra — ARTEFAKT, üçüncü token** · aktör yok · "
 "edim haber, kip işareti yok · şahıs 3MP x3, iltifât 0 · n=10 mora=56 harf=45 (n z=-0,26), fâsıla "
 "ٱلْأَخْسَرُونَ *(en çok ziyana uğrayanlar)* → ن, N sınıfı; **i'râb NOM 2 · GEN 2; fiil YOK**; "
 "simetri [3,1,6,1]; dış düğüm 0 · yıldız ★ yok · kökler سوأ *(kötülük)* · عذب *(azap)* · أخر "
 "*(geciktirme, sonraya bırakma)* · خسر *(hüsran, ziyan)* · bağ: **27:3-4-5 üçlüsü — üç ardışık "
 "ayette آخِر *(âhiret)* ve üçünde de ORTA/geç konumda**; **26:181 ile خسر *(hüsran, ziyan)* "
 "karşılaştırması** — orada ٱلْمُخْسِرِينَ *(eksiltenler)* ölçüde hile, burada ٱلْأَخْسَرُونَ "
 "*(en çok ziyana uğrayanlar)* âhiret hâli; **aynı kök, iki alan** (elle, L1, aday 783)"),
6: ("eksen: **lafız YOK · Rab YOK** · **esmâ حَكِيم *(hakîm)* 6. + عَلِيم *(alîm)* 7. sırada = "
 "fâsıla — MÜHÜR; GEÇERLİ; sûrenin altı mühründen birincisi** · **aktör: adlı قُرْءان *(Kur'ân)* "
 "3. sırada, rol MEF'ÛL** · edim haber, kip EMPH 1 · şahıs 2MS x2, **iltifât 1 — yön 3>2; sûrenin "
 "üç iltifâtından birincisi** · n=7 mora=40 harf=29 (n z=-0,58), fâsıla عَلِيمٍ *(alîm)* → م, N "
 "sınıfı; **i'râb ACC 2 · GEN 3**; bab II x1; zaman IMPF 1; **edilgen 1 — تُلَقَّى *(almaktasın)*; "
 "ayetin TEK fiili ve o da edilgen, oran 1,00**, pas z=5,38: **yıldızın TEK kaynağı**; dış düğüm "
 "0 · **yıldız ★★★** · kökler لقي *(karşılaşma, kavuşma; atma)* · قرأ *(okuma)* · لدن *(kat, "
 "nezd)* · حكم *(hüküm verme, hikmet)* · علم *(bilme)* · bağ: **لدن *(kat, nezd)* korpusta 18 "
 "geçişli ve dikey ölçümü ▸önce وهب *(bağışlama, hibe)* x44,0 veriyor** — 26:21 ve 26:83'ün "
 "وهب+حكم çifti (aday 660) burada üçüncü kez, bu kez لدن ile (elle, L1, aday 784)"),
7: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı مُوسَى *(Mûsâ)* 3. sırada, rol FAİL "
 "+ KONUŞAN** · edim haber, kip FUT 1 · **şahıs 1S x5 · 2MP x5** · 3MS x2 · 3FS x1, iltifât 0 · "
 "n=16 mora=96 harf=72 — **blokta ikinci en uzun ayet** (n z=0,38), fâsıla تَصْطَلُونَ *(ısınırsınız)* → "
 "ن, N sınıfı; **i'râb NOM 1 · GEN 4 · ACC 3**; bab I x3 · IV x1 · VIII x1; zaman PERF x2 · "
 "IMPF x3; **kök ikilemesi أتي *(gelme, getirme)* x2 — iki ayrı vaat: haber getirme ve kor "
 "getirme**; simetri [3,1,9,1]; **dış düğüm 2** · yıldız ★ yok · kökler قول *(söz söyleme)* · أهل "
 "*(halk, aile)* · أنس *(insan)* · نور *(nûr, ışık)* · أتي *(gelme, getirme)* · خبر *(haber; "
 "haberdar olma)* · شهب *(alev, kor parçası (şihâb))* · قبس *(kor, ateş parçası)* · صلي *(ateşe "
 "girme, yaslanma)* · bağ: xref آنس *(gördü)* + نار *(ateş)* + أتى *(getirdi)* → **20:10 · 28:29**; "
 "**26:10-16 ile Mûsâ görevlendirmesi karşılaştırması** — orada nidâ ile açılıyordu (وَإِذْ نَادَىٰ "
 "رَبُّكَ *(hani Rabbin seslenmişti)*), burada bir ATEŞ GÖRME sahnesiyle; **aynı olay, iki sûrede "
 "iki farklı giriş noktası** (elle, L1, aday 785)"),
8: ("eksen: **ALLAH LAFZI 12. sırada — SÛRENİN İLK LAFZI** (göreli konum 8/93 = 0,086) · **رَبّ "
 "*(Rab)* 13. sırada — SÛRENİN İLK RABBİ, AYNI AYETTE** (allah z=0,90 · rab z=1,20) · esmâ yok · "
 "aktör yok · edim haber, kip işareti yok · şahıs 3MS x3 · 3FS x2, iltifât 0 · n=14 mora=72 harf=55 "
 "(n z=0,17), fâsıla ٱلْعَٰلَمِينَ *(âlemler)* → ن, N sınıfı; **i'râb GEN 4 · ACC 2**; bab I x1 · "
 "**bab III x2**; zaman PERF x3; **edilgen 2 — نُودِىَ *(seslenildi)* ve بُورِكَ *(mübarek "
 "kılındı)*; üç fiilden ikisi edilgen, oran 0,67**, pas z=3,48: **yıldızın TEK kaynağı**; simetri "
 "[3,4,7,1]; **dış düğüm 1** · **yıldız ★★★** · kökler جيأ *(gelme)* · ندي *(seslenme; meclis, "
 "toplantı yeri)* · برك *(bereket)* · نور *(nûr, ışık)* · حول *(çevirme, değiştirme)* · سبح "
 "*(tesbih, tenzih)* · أله *(ilâh; lafza-i celâl)* · ربب *(rab, terbiye etme)* · علم *(bilme)* · "
 "bağ: xref سبحان *(tesbih)* + اللّه + ربّ → **21:22**; **رَبِّ ٱلْعَٰلَمِينَ terkibi sûre 27'de "
 "İLK KEZ ve LAFIZLA BİRLİKTE** — sûre 26'da yedi geçişin hiçbirinde lafız yoktu (aday 746) "
 "(elle, L1, aday 786)"),
9: ("eksen: **ALLAH LAFZI 4. sırada — sûrenin ikinci lafzı** (allah z=2,80: yıldızın TEK kaynağı) · "
 "Rab yok · **esmâ عَزِيز *(azîz)* 5. + حَكِيم *(hakîm)* 6. sırada = fâsıla — MÜHÜR; GEÇERLİ; "
 "ikinci mühür ve İKİNCİ FARKLI ÇİFT** · **aktör: adlı مُوسَى *(Mûsâ)* 1. sırada, rol FAİL + "
 "MUHATAP** · edim nida, kip VOC 1 · şahıs 3MS x1 · 1S x1, iltifât 0 · n=6 mora=42 harf=28 "
 "(n z=-0,68), fâsıla ٱلْحَكِيمُ *(hakîm)* → م, N sınıfı; **i'râb NOM 4 · ACC 1; fiil YOK**; dış "
 "düğüm 0 · **yıldız ★★** · kökler أله *(ilâh; lafza-i celâl)* · عزز *(izzet, güç ve üstünlük)* · "
 "حكم *(hüküm verme, hikmet)* · bağ: **27:6 ile mühür karşılaştırması** — orada حَكِيم|عَلِيم, "
 "burada عَزِيز|حَكِيم; **üç ayet arayla iki farklı çift ve حَكِيم ikisinde de var**; **sûre "
 "26'nın tersine mühür çiftleri ÇEŞİTLİ** (orada dokuzu tek çiftti, aday 771) (elle, L1, aday 787)"),
10: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı مُوسَى *(Mûsâ)* 12. sırada, rol "
 "FAİL + MUHATAP** · edim emir + yasak + nida, kip IMPV 1 · NEG 2 · VOC 1 · PRO 1 · şahıs 2MS x3 · "
 "3MS x4 · 3FS x3 · 1S x2, iltifât 0 · **n=19 mora=105 harf=78 — BLOKTA EN UZUN AYET** (n z=0,70), "
 "fâsıla ٱلْمُرْسَلُونَ *(elçiler)* → ن, N sınıfı; **i'râb NOM 4 · ACC 3**; bab I x3 · II x2 · "
 "IV x1 · VIII x1; zaman IMPV 1 · PERF x2 · IMPF x4; **kök ikilemesi خوف *(korku)* x2 — yasak ve "
 "gerekçe aynı kökle: لَا تَخَفْ إِنِّى لَا يَخَافُ لَدَىَّ ٱلْمُرْسَلُونَ**; **biçim NEHY**; "
 "simetri [3,10,13,1]; **dış düğüm 1** · yıldız ★ yok · kökler لقي *(karşılaşma, kavuşma; atma)* · "
 "عصو *(asâ, değnek)* · رأي *(görme)* · هزز *(sarsılma, kıpırdanma)* · جنن *(örtme, gizleme; "
 "cennet; cin)* · ولي *(dost, veli; velâyet)* · دبر *(arka)* · عقب *(sonuç, âkıbet)* · خوف "
 "*(korku)* · رسل *(gönderme, elçi)* · bağ: xref **ALTI 3-gram → altısı da 28:31**; **26:32 ile "
 "asâ sahnesi karşılaştırması** — orada ثُعْبَانٌ مُّبِينٌ *(apaçık yılan)*, burada كَأَنَّهَا "
 "جَآنٌّ *(bir yılan gibi)*; **aynı olay, iki sûrede iki ayrı sözcük** (elle, L1, aday 788)"),
}

M = {
1: ("Sûre üç harfle açılıyor: طسٓ. **Ölçülebilir bir karşılaştırma: 26:1'de طسٓمٓ vardı ve ayette "
 "KÖK YOKTU** — okumada ▽ satırı yazılamayan tek ayet (aday 527 kümesi). Burada aynı harf "
 "öbeğinden biri artı **dört kök**: âyet, Kur'ân, kitap, beyan. **Yani iki sûre akraba harf "
 "öbekleriyle açılıyor ama sûre 27'nin açılışı ölçülebilir içerik taşıyor.** Ve `قُرْءان` aktör "
 "tablosuna **KİTAB** sınıfıyla giriyor — sûrede dört kez. Fâsıladaki مُبِين esmâ sayılmış, "
 "gönderge كِتَاب *(kitap)*; sûrenin altı مُبِين tokeninin birincisi ve **sûre 26'da bu lemma "
 "yedi kez artefakt çıkmıştı**."),
2: ("**Sûrenin en kısa ayeti** (n=3) ve fiil yok: هُدًى وَبُشْرَىٰ لِلْمُؤْمِنِينَ *(müminler için "
 "bir kılavuz ve müjde)*. Tek xref 2:97'ye düşüyor. Ölçülebilir bir kaydırma: بشر *(müjde; beşer)* "
 "25:56'da elçinin niteliğiydi (مُبَشِّرا *(müjdeci)*), burada **kitabın** niteliği — aynı kök, "
 "elçiden kitaba. Ve fâsıladaki مُؤْمِن esmâ sayılmış: **sûre 26'da bu lemma on beş kez artefakt "
 "çıkmıştı** (aday 601/709) ve burada da gönderge insanlar."),
3: ("Üç eylem sayılıyor ve **üç fiil de bab IV**: namaz, zekât, yakîn. Ayet 31:4 ile **tam özdeş** "
 "ve esit yakalıyor; iki xref de 31:4 ve 41:7'ye düşüyor. **Ölçülebilir bir kök tuzağı: قوم "
 "*(kalkma; kavim; kıyamet)* burada 'namaz kılma' anlamında** — sûre 26'da aynı kök dört anlam "
 "alanındaydı (kavim/kalkma/konum/doğruluk, aday 769); bu, 529 kümesine **sûre 27'nin ilk vakası**. "
 "Ve fâsıladaki آخِر esmâ sayılmış, oysa ٱلْءَاخِرَة bir zaman/yer adı — sûrenin dört آخِر "
 "tokeninin birincisi."),
4: ("Karşıt kutup bitişik ayette: إِنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ *(âhirete "
 "inanmayanlar)*. **27:3 ve 27:4 aynı kelimeyi (ٱلْءَاخِرَة) taşıyor ve iki kutupta**: orada "
 "müminlerin yakîni, burada inanmayanların reddi. عمه *(şaşkınlık, körü körüne bocalama)* korpusta "
 "**yedi** geçişli. Ve زين *(süsleme)* bab II ile bir fâil sorusu doğuruyor: süsleyen kim — ayet "
 "1P kullanıyor (زَيَّنَّا *(süsledik)*)."),
5: ("Üçüncü ardışık آخِر: أُو۟لَٰٓئِكَ ٱلَّذِينَ لَهُمْ سُوٓءُ ٱلْعَذَابِ *(azabın en kötüsü onlar "
 "içindir)*. **Üç ardışık ayette aynı kelime ve üçünde de esmâ sayılmış** — sûrenin dört آخِر "
 "tokeninin üçü bu üçlüde. Ve خسر *(hüsran, ziyan)* 26:181'den geri geliyor: orada ٱلْمُخْسِرِينَ "
 "*(eksiltenler)* **ölçüde hile** yapanlardı, burada ٱلْأَخْسَرُونَ *(en çok ziyana uğrayanlar)* "
 "**âhiret hâli** — aynı kök, iki alan. On kelime, fiil yok."),
6: ("Yıldızın tek kaynağı tek bir edilgen fiil: تُلَقَّى *(almaktasın)*, oran 1,00 → pas z=5,38. "
 "Ve **sûrenin ilk mührü burada: حَكِيم|عَلِيم, geçerli.** Ölçülebilir bir komşuluk: لدن *(kat, "
 "nezd)* korpusta 18 geçişli ve dikey ölçümü ▸önce وهب *(bağışlama, hibe)* x44,0 veriyor — "
 "26:21'in ve 26:83'ün وهب+حكم çifti (aday 660) burada **üçüncü kez** ve bu kez لدن ile: مِن "
 "لَّدُنْ حَكِيمٍ عَلِيمٍ *(hikmet sahibi ve bilen bir katından)*. Sûrenin ilk iltifâtı da burada "
 "(3>2)."),
7: ("Mûsâ kıssası **bir ateş görme sahnesiyle** açılıyor: إِنِّىٓ ءَانَسْتُ نَارا *(ben bir ateş "
 "gördüm)*. **Ölçülebilir bir giriş farkı: 26:10'da aynı kıssa bir NİDÂ ile açılıyordu** (وَإِذْ "
 "نَادَىٰ رَبُّكَ مُوسَى *(hani Rabbin Mûsâ'ya seslenmişti)*); burada nidâ bir ayet sonra gelecek "
 "(27:8). **Aynı olay, iki sûrede iki ayrı giriş noktası.** İki xref 20:10 ve 28:29'a düşüyor. Kök "
 "ikilemesi أتي *(gelme, getirme)* x2 — iki ayrı vaat (haber ve kor). Ve iki seyrek kök bitişik: "
 "شهب *(alev, kor parçası (şihâb))* n=5 ve قبس *(kor, ateş parçası)* n=3; **قبس'in dikey satırı "
 "▸önce gelme x23,9 veriyor, yani bu ayetin fiili** — aday 735'in seyrek kök uyarısı sûre 27'nin "
 "ilk vakası."),
8: ("**Sûrenin ilk Allah lafzı ve ilk Rabbi aynı ayette** — göreli konum 0,086. Karşılaştırma: "
 "sûre 25'te ilk lafız 0,22'de, sûre 26'da 0,39'da (aday 665). **Yani lafız gecikmesi sûreye "
 "özgü, Mekkî'ye özgü değil.** İki edilgen fiil: نُودِىَ *(seslenildi)* ve بُورِكَ *(mübarek "
 "kılındı)*, oran 0,67 → pas z=3,48, yıldızın tek kaynağı. **Ve رَبِّ ٱلْعَٰلَمِينَ terkibi "
 "burada lafızla BİRLİKTE geçiyor** — sûre 26'da terkip yedi kez geçmişti ve **hiçbirinde lafız "
 "yoktu** (aday 746). سبح *(tesbih, tenzih)* korpusta 92 geçişli."),
9: ("Altı kelime, fiil yok, ve **sûrenin ikinci mührü: عَزِيز|حَكِيم**. Ölçülebilir bir çeşitlilik: "
 "27:6'da حَكِيم|عَلِيم vardı, burada عَزِيز|حَكِيم — **üç ayet arayla iki farklı çift ve حَكِيم "
 "ikisinde de var**. **Sûre 26'nın tam tersi:** orada on mühürden dokuzu tek çiftti (عَزِيز|رَحِيم) "
 "ve sekizi tek ayetin tekrarıydı (aday 771). Yıldızın tek kaynağı lafız oranı (allah z=2,80; "
 "n=6, tek lafız). Ve مُوسَى hem FAİL hem MUHATAP rolü alıyor."),
10: ("**Blokta en uzun ayet** (n=19) ve **altı 3-gram'ın altısı da 28:31'e düşüyor** — okumada bir "
 "ayetin tek bir ayete bu kadar çok bağla bağlandığı ilk yer; donmuş kalıp adayı (aday 437). Kök "
 "ikilemesi خوف *(korku)* x2: yasak ve gerekçe aynı kökle — لَا تَخَفْ *(korkma)* ve لَا يَخَافُ "
 "لَدَىَّ ٱلْمُرْسَلُونَ *(benim katımda elçiler korkmaz)*. **Ölçülebilir bir sözcük farkı: 26:32'de "
 "asâ ثُعْبَانٌ مُّبِينٌ *(apaçık yılan)* oluyordu, burada كَأَنَّهَا جَآنٌّ *(bir yılan gibi)*** — "
 "aynı olay, iki sûrede iki ayrı sözcük ve burada bir BENZETME var. Ve جنن *(örtme, gizleme; "
 "cennet; cin)* burada 'yılan/cin' anlamında — sûre 26'da 'cennet' ve 'delilik' anlamlarındaydı "
 "(aday 619); **529 kümesine üçüncü anlam**. هزز *(sarsılma, kıpırdanma)* korpusta beş geçişli ve "
 "dikey ölçümü iki listede de BOŞ."),
}

ATLAMA = {
 "_mercek_27_6_8": ("27:6 ve 27:8 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. İkisinde de tek kaynak "
  "edilgenlik oranı (pas z=5,38 ve 3,48). 27:6 bir kaynak bildirimi, 27:8 bir nidâ sahnesi; "
  "ikisinde de ne canlı, ne gök cismi, ne ölçü, ne süreç. **NOT: 27:8'de نَار *(ateş)* ve "
  "بُورِكَ *(mübarek kılındı)* geçiyor ama ateşin ne yapısı ne davranışı anlatılıyor — "
  "adlandırma düzeyinin altında; çıpa sayılmadı.**"),
 "_blok_notu_27_1_10": ("BLOK BİLANÇOSU: ★★★ 2 (27:6, 8) · ★★ 1 (27:9) · ★ 0 · 7 ayet yıldızsız. "
  "Kaynaklar: pas x2 · allah x1 — hiçbiri içerikten, hiçbirinde çıpa yok. **SÛRE 27'NİN AÇILIŞI "
  "SÛRE 26'NIN TERSİ: A/R = 2,25 (okumada ilk kez >1), nakarat SIFIR, kafiye kırılması SIFIR, "
  "mühür çiftleri ÇEŞİTLİ, iltifât 3.** ÇIPA NOTU: 27:10'da asâ-yılan dönüşümü var ama benzetme "
  "düzeyinde (كَأَنَّهَا جَآنٌّ *(bir yılan gibi)*); 26:32'nin ثُعْبَان vakasıyla aynı sınıf ve "
  "orada da çıpa sayılmamıştı."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
OM['27'] = dict(MAKRO)
OM['27']['_mercek_atlama_notu'] = dict(ATLAMA)
for n in range(1, 11):
    OM['27']["27:%d" % n] = {"ar": AR[(27, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["27:%d" % n]}
OM['ilerleme']['not'] = ("Sûre 1 ve 9-26 TAM. **Sûre 27 (Neml) 10/93.** Devam: 27:11'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "27": "1-10 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1959
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 27 →', len([k for k in OM['27'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK['27'] = {}
for n in range(1, 11):
    MK['27']["27:%d" % n] = M[n]
MK['27_atlama'] = dict(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 27 →', len(MK['27']))
