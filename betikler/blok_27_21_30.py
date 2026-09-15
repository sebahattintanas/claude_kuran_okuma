# -*- coding: utf-8 -*-
"""blok_27_21_30.py — sûre 27 üçüncü blok (27:21-30). Hüdhüdün Sebe haberi ve mektup."""
import json
DIK = json.load(open('blok_dikey_27_21_30.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
21: "Ona şiddetli bir azap edeceğim yahut onu boğazlayacağım; ya da bana apaçık bir delil getirecek.",
22: "Çok geçmeden geldi ve dedi: Senin kuşatamadığın bir şeyi kuşattım; sana Sebe'den kesin bir haber getirdim.",
23: "Ben, onlara hükümdarlık eden bir kadın buldum; ona her şeyden verilmiş ve büyük bir tahtı var.",
24: "Onu ve kavmini, Allah'ı bırakıp güneşe secde ederken buldum. Şeytan onlara işlerini süslemiş ve onları yoldan çevirmiş; artık yol bulamıyorlar.",
25: "Göklerde ve yerde gizli olanı çıkaran, gizlediğinizi de açığa vurduğunuzu da bilen Allah'a secde etmesinler diye.",
26: "Allah; O'ndan başka ilâh yoktur. O, büyük arşın Rabbidir.",
27: "Dedi: Bakacağız, doğru mu söyledin yoksa yalancılardan mı oldun.",
28: "Şu mektubumu götür, onlara bırak; sonra onlardan çekil de ne cevap vereceklerine bak.",
29: "Dedi: Ey ileri gelenler, bana değerli bir mektup bırakıldı.",
30: "O, Süleymân'dandır ve o, Rahmân ve Rahîm olan Allah'ın adıyladır.",
}

O = {
21: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُبِين *(apaçık)* 9. sırada = fâsıla, MÜHÜRSÜZ — "
 "ARTEFAKT**: gönderge سُلْطَٰن *(delil)*; sûrenin altı مُبِين tokeninin DÖRDÜNCÜSÜ · aktör yok · "
 "edim haber, **kip EMPH 6** · şahıs 1S x3 · 3MS x3, iltifât 0 · n=9 mora=66 harf=51 (n z=-0,36), "
 "fâsıla مُّبِينٍ *(apaçık)* → ن, N sınıfı; **i'râb ACC 2 · GEN 2**; bab I x2 · II x1; zaman IMPF "
 "x3; **kök ikilemesi عذب *(azap)* x2**; **dış düğüm 3** · yıldız ★ yok · kökler عذب *(azap)* · "
 "شدد *(şiddet, katılık)* · ذبح *(boğazlama, kurban)* · أتي *(gelme, getirme)* · سلط *(yetki, delil "
 "(sultan))* · بين *(arası; açıklama)* · bağ: xref عذّب *(azap etti)* + عذاب *(azap)* + شديد *(şiddetli)* → **3:56**; أتى + سلطان *(delil)* + "
 "مبين → **14:10 · 44:19** (elle, L1, aday 800/801)"),
22: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı سَبَإ *(Sebe)* 12. sırada, tür "
 "kavim, rol mecrur — OKUMADA İLK SEBE** · edim haber, kip NEG 1 · **şahıs 3MS x3 · 1S x4 · 2MS x2 "
 "— sahset ['1','2','3'], üç şahıs birden**, iltifât 0 · n=14 mora=57 harf=51 (n z=0,17), fâsıla "
 "يَقِينٍ *(kesin)* → ن, N sınıfı; **i'râb ACC 1 · GEN 4**; bab I x3 · IV x2; zaman PERF x4 · IMPF "
 "1; **kök ikilemesi حوط *(kuşatma)* x2 — biri olumlu (أَحَطتُ *(kuşattım)*), biri olumsuz (لَمْ "
 "تُحِطْ *(kuşatmadın)*), yan yana**; simetri [3,5,8,1]; dış düğüm 0 · yıldız ★ yok · kökler مكث "
 "*(kalma, ağır ağır)* · غير *(başka)* · بعد *(sonra; uzaklık)* · قول *(söz söyleme)* · حوط "
 "*(kuşatma)* · جيأ *(gelme)* · **سبأ *(Sebe (yer/kavim adı))* — YENİ KÖK, korpusta n=2** · نبأ "
 "*(haber)* · يقن *(yakîn, kesin bilgi)* · bağ: **سبأ *(Sebe (yer/kavim adı))* korpusta İKİ geçiş: "
 "27:22 ve 34:15** — ikinci geçiş kendi adını taşıyan sûrede; **يقن *(yakîn, kesin bilgi)* sûrenin "
 "ÜÇÜNCÜ geçişi ve üçüncü gönderge**: 27:3 mümin · 27:14 inkârcı · burada HABER (elle, L1)"),
23: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **adsız aktör: imrae 3. konumda — DENETLENDİ, "
 "DOĞRU; lemma امْرَأَت *(kadın)*, F, gerçek aktör (تَمْلِكُهُمْ *(onlara hükmediyor)* fiilinin "
 "fâili)** · edim haber · şahıs 1S x3 · 3FS x3 · 3MP x1, iltifât 0 · n=11 mora=54 harf=45 "
 "(n z=-0,15), fâsıla عَظِيمٌ *(büyük)* → **م — sûrenin AZINLIK kafiyesi (93 ayette 9 م)**, N "
 "sınıfı; **i'râb ACC 2 · GEN 2 · NOM 2**; bab I x2 · IV x1; zaman PERF x2 · IMPF 1; **edilgen 1 "
 "— أُوتِيَتْ *(ona verildi)*; pas z=1,57: yıldızın TEK kaynağı**; dış düğüm 1 · iç düğüm 1 · "
 "**yıldız ★** · kökler وجد *(bulma)* · مرأ *(kişi; kadın (imrae))* · ملك *(mülk; melik)* · أتي "
 "*(gelme, getirme)* · كلل *(hep, bütün)* · شيأ *(dileme; şey)* · عرش *(arş, taht)* · عظم "
 "*(büyüklük, azamet; kemik)* · bağ: xref آتى *(verdi)* + كلّ *(her)* + شىء *(şey)* → **18:84 · 27:16**; **27:26 ile عَرْش "
 "+ عَظِيم çifti** — burada belirsiz (عَرْشٌ عَظِيمٌ), orada belirli (ٱلْعَرْشِ ٱلْعَظِيمِ), üç "
 "ayet arayla, ikisi de fâsıla konumunda; **esit alanı İKİSİNDE DE BOŞ** (elle, L1, aday 802/805)"),
24: ("eksen: **ALLAH LAFZI 7. sırada — sûrenin DÖRDÜNCÜ lafzı** (allah z=0,65) · Rab yok · esmâ "
 "yok · **aktör: adlı شَيْطان *(şeytan)* 10. sırada, tür gayb, rol FAİL** · edim haber, kip NEG 1 · "
 "**şahıs 3MP x8** · 1S x2 · 3FS x2 · 3MS x2, baskın şahıs 3, iltifât 0 · **n=17 — blokta en uzun "
 "ayet** (n z=0,49), fâsıla يَهْتَدُونَ *(yol buluyorlar)* → ن, N sınıfı; **i'râb ACC 2 · GEN 4 · "
 "NOM 1**; bab I x3 · II x1 · **bab VIII x1**; zaman PERF x3 · IMPF x2; **dış düğüm 2** · yıldız ★ "
 "yok · kökler وجد *(bulma)* · قوم *(kalkma; kavim; kıyamet)* · سجد *(secde)* · شمس *(güneş)* · دون "
 "*(beriki, başkası)* · أله *(ilâh; lafza-i celâl)* · زين *(süsleme)* · شطن *(şeytan)* · عمل *(iş, "
 "amel)* · صدد *(yüz çevirme, alıkoyma)* · سبل *(yol)* · هدي *(yol gösterme)* · bağ: xref شيطان *(şeytan)* + "
 "عمل *(amel)* + صدّ *(çevirdi)* → **29:38**; عمل *(amel)* + صدّ *(çevirdi)* + سبيل *(yol)* → "
 "**29:38 · 40:37** (elle, L1, aday 807/809)"),
25: ("eksen: **ALLAH LAFZI 3. sırada — sûrenin BEŞİNCİ lafzı** (allah z=0,90) · Rab yok · esmâ yok "
 "· aktör yok · edim haber, kip NEG 1 · şahıs 3MP x2 · 3MS x2 · **2MP x4**, sahset ['2','3'], "
 "iltifât 0 · n=14 mora=73 harf=61 (n z=0,17), fâsıla تُعْلِنُونَ *(açığa vuruyorsunuz)* → ن, N "
 "sınıfı; **i'râb GEN 3 · ACC 1**; bab I x2 · IV x3; **zaman IMPF x5 — beş fiilin BEŞİ de "
 "muzari**; **HAPAKS: خبأ *(saklı olan, gizlenmiş şey)* — korpusta TEK geçiş** (hapaks z=3,38: "
 "**yıldızın TEK kaynağı**); dış düğüm 1 · **yıldız ★★★** · kökler سجد *(secde)* · أله *(ilâh; "
 "lafza-i celâl)* · خرج *(çıkma, çıkarma)* · **خبأ *(saklı olan, gizlenmiş şey)* — YENİ KÖK** · سمو "
 "*(ad; gök)* · أرض *(yer, yeryüzü)* · علم *(bilme)* · خفي *(gizleme, gizli olan)* · علن *(açığa "
 "vurma, alenî)* · bağ: xref علم *(bildi)* + أخفي *(gizledi)* + أعلن *(açığa vurdu)* → **14:38**; **خفي *(gizleme, gizli olan)* ile علن "
 "*(açığa vurma, alenî)* korpusta üç ayette birlikte: 14:38 · 27:25 · 60:1** (elle, L1, aday "
 "806/808)"),
26: ("eksen: **ALLAH LAFZI 1. sırada** (allah z=1,97) **· رَبّ *(Rab)* 6. sırada — sûrenin ÜÇÜNCÜ "
 "Rabbi** (rab z=2,34); **blokta lafız ile Rab'ın aynı ayette bulunduğu TEK yer, sûrede 27:8'den "
 "sonra ikinci** · esmâ yok · aktör yok · edim haber, kip NEG 1 · RES 1 · **şahıs 3MS x1 — tek "
 "şahıs işareti**, iltifât 0 · n=8 mora=38 harf=28 (n z=-0,47), fâsıla ٱلْعَظِيمِ *(büyük)* → **م "
 "— azınlık kafiyesi**, N sınıfı; **i'râb NOM 2 · ACC 1 · GEN 2**; **kök ikilemesi أله *(ilâh; "
 "lafza-i celâl)* x2 — ٱللَّهُ ve إِلَٰهَ aynı ayette**; **biçim HASR**; **metinde secde işareti "
 "۩**; **dış düğüm 3** · **yıldız ★★** — kaynak allah z + rab z, ikisi birlikte · kökler أله "
 "*(ilâh; lafza-i celâl)* · ربب *(rab, terbiye etme)* · عرش *(arş, taht)* · عظم *(büyüklük, "
 "azamet; kemik)* · bağ: xref ربّ *(Rab)* + عرش *(arş)* + عظيم *(büyük)* → **9:129 · 23:86**; إله + ربّ *(Rab)* + عرش *(arş)* → **23:116**; "
 "**27:23 ile عَرْش *(arş, taht)* + عَظِيم *(büyük)* karşılıklı çifti** (elle, L1, aday 805)"),
27: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip FUT 1 · INTG 1 · şahıs "
 "3MS x1 · 1P x1 · **2MS x4**, iltifât 0 · **n=7 — blokta en kısa ayet** (n z=-0,58), fâsıla "
 "ٱلْكَٰذِبِينَ *(yalancılar)* → ن, N sınıfı; **i'râb GEN 1**; **bab I x4 — dört fiilin dördü de "
 "birinci bab**; zaman PERF x3 · IMPF 1; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · "
 "نظر *(bakma; mühlet verme)* · صدق *(doğruluk)* · كون *(olmak; mekân, yer)* · كذب *(yalan; "
 "yalanlama)* · bağ: **صدق *(doğruluk)* ile كذب *(yalan; yalanlama)* aynı ayette karşıt çift** — "
 "أَصَدَقْتَ أَمْ كُنتَ مِنَ ٱلْكَٰذِبِينَ *(doğru mu söyledin yoksa yalancılardan mı oldun)*; xref "
 "yok (elle, L1)"),
28: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru + emir, **kip IMPV 4** · "
 "INTG 1 · şahıs 2MS x4 · 3MS x1 · 3MP x4, iltifât 0 · n=11 mora=57 harf=46 (n z=-0,15), fâsıla "
 "يَرْجِعُونَ *(dönüyorlar)* → ن, N sınıfı; **i'râb GEN 1**; bab I x3 · IV x1 · V x1; **zaman IMPV "
 "4 · IMPF 1 — beş fiilin DÖRDÜ emir, oran 0,80**; simetri [3,3,6,1]; **biçim DIKKAT**; dış düğüm "
 "0 · yıldız ★ yok · kökler ذهب *(gitme, götürme)* · كتب *(yazma, kitap)* · لقي *(karşılaşma, "
 "kavuşma; atma)* · ولي *(dost, veli; velâyet)* · نظر *(bakma; mühlet verme)* · رجع *(dönme, geri "
 "döndürme)* · bağ: **نظر *(bakma; mühlet verme)* 27:27'den sonra ikinci geçiş — ardışık iki "
 "ayette**; 27:27'de سَنَنظُرُ *(bakacağız)* Süleymân'ın kendi bakışı, burada فَٱنظُرْ *(bak)* "
 "hüdhüde verilen emir; **aynı kök, aynı bab, özneden nesneye** (elle, L1)"),
29: ("eksen: **lafız YOK · Rab YOK** · **esmâ كَرِيم *(değerli)* 8. sırada = fâsıla, MÜHÜRSÜZ — "
 "ARTEFAKT**: gönderge كِتَٰب *(mektup)*; sûrenin iki كَرِيم tokeninin BİRİNCİSİ · aktör yok · edim "
 "nida, kip VOC 1 · şahıs 3FS x1 · 1S x2 · 3MS x1, iltifât 0 · n=8 mora=48 harf=34 (n z=-0,47), "
 "fâsıla كَرِيمٌ *(değerli)* → **م — azınlık kafiyesi**, N sınıfı; **i'râb ACC 2 · NOM 3**; bab I "
 "x1 · IV x1; zaman PERF x2; **edilgen 1 — أُلْقِىَ *(bırakıldı)*; iki fiilden biri edilgen, oran "
 "0,50**, pas z=2,52: **yıldızın TEK kaynağı**; **biçim DIKKAT**; dış düğüm 1 · **iç düğüm 2** · "
 "**yıldız ★★** · kökler قول *(söz söyleme)* · أيي *(âyet, işaret)* · ملأ *(ileri gelenler (meleʼ); "
 "doldurma)* · لقي *(karşılaşma, kavuşma; atma)* · كتب *(yazma, kitap)* · كرم *(üstün tutma, "
 "ikram)* · bağ: xref قال *(dedi)* + أيّ *(ey)* + ملأ *(ileri gelenler)* → **27:32 · 27:38 · 28:38** — üç bağın İKİSİ sûre içi; "
 "**لقي *(karşılaşma, kavuşma; atma)* 27:28'den sonra ikinci geçiş: orada emir (فَأَلْقِهْ "
 "*(bırak)*), burada edilgen (أُلْقِىَ *(bırakıldı)*) — aynı kök, emirden edilgene** (elle, L1)"),
30: ("eksen: **ALLAH LAFZI 6. sırada — sûrenin ALTINCI lafzı** (allah z=1,97) · Rab yok · **esmâ "
 "رَحْمٰن *(Rahmân)* 7. + رَحِيم *(Rahîm)* 8. sırada = fâsıla — MÜHÜR; GEÇERLİ; sûrenin altı "
 "mühründen DÖRDÜNCÜSÜ ve DÖRDÜNCÜ FARKLI ÇİFT** · **aktör: adlı سُلَيْمان *(Süleymân)* 3. sırada, "
 "tür kişi, rol mecrur** · edim haber, kip işareti yok · şahıs 3MS x2, iltifât 0 · n=8 mora=43 "
 "harf=35 (n z=-0,47), fâsıla ٱلرَّحِيمِ *(Rahîm)* → **م — azınlık kafiyesi**, N sınıfı; **i'râb "
 "ACC 2 · GEN 5**; **kök ikilemesi رحم *(rahmet, merhamet)* x2**; dış düğüm 1 · **yıldız ★** · "
 "kökler سمو *(ad; gök)* · أله *(ilâh; lafza-i celâl)* · رحم *(rahmet, merhamet)* · bağ: xref اسم *(ad)* + "
 "اللّه + رحمن *(Rahmân)* → **1:1**; اللّه + رحمن *(Rahmân)* + رحيم *(Rahîm)* → **1:1**; **tam besmele korpusta 114 kez sûre "
 "başında ve ayet içinde YALNIZ BURADA**; **رَحْمٰن *(Rahmân)* korpusta 57 esmâ tokeni, sûre 27'de "
 "YALNIZ BURADA** (elle, L1, aday 803/804)"),
}

M = {
21: ("Üç seçenek, üçü de tekitli: **n=9'luk bir ayette ALTI tekit işareti**. Ölçülebilir bir uç "
 "değer: **EMPH/n = 0,67 korpusun en yüksek tekit yoğunluğu**; aynı orana ulaşan yalnız iki ayet "
 "daha var (29:11 ve 7:6, ikisi de 4/6) ve **mutlak tekit sayısında 27:21 hepsinden yüksek**. "
 "İkinci en yüksek mutlak sayı 4:119'da (12/21, oran 0,57). Ve **kapanış notundaki tahmin burada "
 "düştü**: not 27:21'i *'sûrenin en uzun ayeti (n=61)'* diye kaydetmişti; ölçülen n=9. Sûrenin en "
 "uzun ayetleri 27:40 (n=38) · 27:44 (n=28) · 27:60 (n=27) · 27:19 (n=24) · 27:61 (n=21). "
 "**'n=61' kaydı (n=21, ayet 61) ikilisinin ters okunmasından geldi.** Ayet gerçekten bir uç "
 "değer taşıyor — ama uzunlukta değil, tekitte. عذب *(azap)* korpusta 373 geçişli."),
22: ("Haberin gelişi bir zaman ölçüsüyle: فَمَكَثَ غَيْرَ بَعِيدٍ *(çok geçmeden)*. مكث *(kalma, "
 "ağır ağır)* korpusta **yedi** geçişli. **Ölçülebilir bir yapı: حوط *(kuşatma)* aynı ayette iki "
 "kez ve zıt kutupta** — أَحَطتُ بِمَا لَمْ تُحِطْ بِهِۦ *(senin kuşatamadığını kuşattım)*; kök "
 "korpusta 28 geçişli, bu terkip bilgi üstünlüğünü tek kökle kuruyor. Ve **يقن *(yakîn, kesin "
 "bilgi)* sûrede üçüncü kez, üçüncü göndergeyle**: 27:3'te müminlerin âhirete inanışı, 27:14'te "
 "inkârcıların iç hâli, burada bir **haberin** niteliği — kişi, karşıt kişi, sonra nesne. سبأ "
 "*(Sebe (yer/kavim adı))* korpusta **iki** geçişli ve ikincisi 34:15, yani kendi adını taşıyan "
 "sûrede; okumada ilk kez bir yer adı sonraki bir sûrenin adını önceden veriyor."),
23: ("**Adsız aktör denetimi — bu blokun asıl işi.** 27:23'ün imrae etiketi **DOĞRU**: lemma "
 "امْرَأَت *(kadın)*, dişil, ve sözcük gerçek bir aktör (تَمْلِكُهُمْ *(onlara hükmediyor)* "
 "fiilinin fâili). Denetimi korpusun tamamına genişlettim: **imrae etiketli 11 tokenin 4'ü doğru** "
 "(4:12 · 4:128 · 27:23 · 33:50), **6'sı eril** (4:176 · 24:11 · 52:21 · 70:38 · 74:52 · 80:37 — "
 "lemma امْرِئ / امْرُؤٌا, yani 'adam', dişil etiketle işaretlenmiş), **1'i kişi bile değil** (4:4, "
 "مَّرِيٓـًٔا *(afiyetli)*, sıfat). **Hata oranı 7/11 = %63,6.** Mekanizma açık: alan kök düzeyinde "
 "eşleşiyor — مرأ *(kişi; kadın (imrae))* kökü üç lemma taşıyor ve üçü de tek etikete iniyor. "
 "**Önceki 'adsız aktörde %67 hata' kaydı artık tam sayımla ve mekanizmasıyla belgelenmiş "
 "durumda.** Ve bir sınıf yeni: cinsiyet TERSİNE dönüyor — bu, نُفُورا→nefer ve فِرْقٍ→ferîk "
 "vakalarından farklı bir hata türü."),
24: ("Secde bir yanlış yöne düşüyor: يَسْجُدُونَ لِلشَّمْسِ مِن دُونِ ٱللَّهِ *(Allah'ı bırakıp "
 "güneşe secde ediyorlar)*. **Ölçülebilir bir eksen sıçraması: 27:24-25-26 üç ardışık ayetin "
 "üçünde de Allah lafzı** — sûre 27'de ilk kez. Okunan sûrelerde 3+ ardışık lafız dizisi 60 kez "
 "geçiyor ama **hepsi Medenî ya da lafız-yoğun sûrelerde** (9, 10, 11, 12, 13, 14, 16, 18, 22, "
 "24); sûre 27 ilk yirmi ayette üç dağınık lafız verirken burada üçünü art arda veriyor. Ve "
 "**çıpa/yıldız ilişkisi yine ters**: ayet güneşi (شمس *(güneş)*, korpusta 33 geçiş) adlandırıyor "
 "— sûrenin gök cismi içeren tek okunan ayeti — ve **yıldızsız**; iki ayet sonra hiçbir gök cismi "
 "anmayan 27:25 hapakstan ★★★ alıyor. زين *(süsleme)* dikey ölçümü ▸sonra شطن *(şeytan)* ×12,7 "
 "veriyor; iki kök korpusta karşılıklı bağlı."),
25: ("Ayet bir çıkarma fiili kuruyor: يُخْرِجُ ٱلْخَبْءَ *(gizli olanı çıkarır)*. **Yıldızın tek "
 "kaynağı hapaks خبأ *(saklı olan, gizlenmiş şey)* — korpusta tek geçiş ve dikey satırı iki listede "
 "de boş.** Ölçülebilir bir kutup çifti: خفي *(gizleme, gizli olan)* (n=34) ile علن *(açığa vurma, "
 "alenî)* (n=16) korpusta **üç ayette** birlikte — 14:38, burası ve 60:1; üçünde de aynı ikili "
 "yapı. Ve **bir 529 vakası bu blokta doğrudan görünüyor: سمو *(ad; gök)* burada ٱلسَّمَٰوَٰتِ "
 "*(gökler)*, beş ayet sonra 27:30'da ٱسْم *(ad)* — aynı kök, iki anlam alanı, aynı blok**; kök "
 "sözlüğünde iki anlam zaten yazılı ama dikey katman ikisini tek satırda topluyor. **SINIR — ÇIPA "
 "DEĞERLENDİRMESİ (aday 799 ölçütüyle): ayet bir SÜREÇ (gizli olanın çıkarılması) ve bir ALAN "
 "(gökler ve yer) adlandırıyor; ne mekanizma, ne ölçü, ne sınıflandırma var — ٱلْخَبْء *(gizli "
 "olan)* neyin gizlisi olduğu açılmadan bırakılıyor. 'Adlandırma + alan' düzeyi; çıpa sayılmadı.**"),
26: ("Sekiz kelimede eksenin ikisi birden: **lafız birinci sırada, Rab altıncı sırada** ve **yıldızı "
 "üreten tek şey bu** (allah z=1,97 · rab z=2,34); blokta lafızla Rab'ın buluştuğu tek ayet. "
 "**Kök ikilemesi eksenin kendisinde: أله *(ilâh; lafza-i celâl)* iki kez — ٱللَّهُ ve إِلَٰهَ**; "
 "biçim HASR, yani olumsuzlama + istisna. Ve **27:23 ile karşılıklı bir çift**: orada عَرْشٌ "
 "عَظِيمٌ *(büyük bir taht)* belirsiz ve bir kadına ait, burada ٱلْعَرْشِ ٱلْعَظِيمِ *(büyük arş)* "
 "belirli ve Rabbe ait; **iki isim, aynı sıra, aynı fâsıla konumu, üç ayet arayla, belirsizden "
 "belirliye**. **`esit` alanı ikisinde de boş** — bu, alanın yedi eşik türünden 'yapı/iskelet' "
 "türü için temiz bir sınama vakası. Metinde secde işareti ۩ bu ayette."),
27: ("Yedi kelimede bir sınama kuruluyor: سَنَنظُرُ أَصَدَقْتَ أَمْ كُنتَ مِنَ ٱلْكَٰذِبِينَ "
 "*(bakacağız, doğru mu söyledin yoksa yalancılardan mı oldun)*. **Karşıt çift tek ayette: صدق "
 "*(doğruluk)* (n=155) ve كذب *(yalan; yalanlama)* (n=282).** Bab dağılımı da tek: dört fiilin "
 "dördü de birinci bab. Ayet blokun en kısası (n=7) ve dış düğümü sıfır — xref yok; yani bu "
 "terkip korpusta başka yerde bu haliyle bulunmuyor. Yıldız yok, kaynak da yok."),
28: ("Dört emir arka arkaya: ٱذْهَب *(götür)* · فَأَلْقِهْ *(bırak)* · تَوَلَّ *(çekil)* · "
 "فَٱنظُرْ *(bak)*; **beş fiilin dördü emir, oran 0,80**. Ölçülebilir bir kök izi: **نظر *(bakma; "
 "mühlet verme)* iki ardışık ayette** — 27:27'de سَنَنظُرُ *(bakacağız)* Süleymân'ın kendi "
 "bakışı, burada فَٱنظُرْ *(bak)* hüdhüde verilen emir; **aynı kök, aynı bab, özneden nesneye "
 "geçiyor.** Kök korpusta 129 geçişli ve dikey ölçümü ▸sonra عقب *(âkıbet)* ×29,7 veriyor — "
 "korpusta ağırlıkla 'sonuca bakma' kalıbında, burada bir cevaba bakma."),
29: ("Mektubun karşılanışı bir edilgenle: أُلْقِىَ إِلَىَّ كِتَٰبٌ كَرِيمٌ *(bana değerli bir "
 "mektup bırakıldı)*; iki fiilden biri edilgen, oran 0,50 → pas z=2,52, yıldızın tek kaynağı. "
 "**Ölçülebilir bir çatı çevrimi: لقي *(karşılaşma, kavuşma; atma)* bir önceki ayette EMİR "
 "(فَأَلْقِهْ *(bırak)*), burada EDİLGEN (أُلْقِىَ *(bırakıldı)*)** — emri veren Süleymân, "
 "edilgeni söyleyen kraliçe; aynı kök iki ağızda çatı değiştiriyor. Ve fâsıladaki كَرِيم "
 "*(değerli)* esmâ sayılmış — gönderge mektup, **artefakt**; sûrenin iki كَرِيم tokeninin "
 "birincisi. **هَٰذَا + isim + sıfat kalıbı yok ama sonuç aynı: isim + sıfat tamlaması esmâ "
 "listesine takılıyor** (aday 791'in üçüncü vakası)."),
30: ("**Besmele ayet içinde.** Ölçülebilir bir teklik: tam besmele metinde 114 kez sûre başında "
 "geçiyor (1:1'de ayet olarak) ve **ayet içinde yalnız burada**; kısa biçim بِسْمِ ٱللَّهِ ayrıca "
 "11:41'de. Ve **رَحْمٰن *(Rahmân)* korpusta 57 esmâ tokeni taşıyor ama sûre 27'nin tek tokeni "
 "burada** — sûrenin dördüncü mührü ve **dördüncü farklı çift**. Sûre 26'da on mühürden dokuzu "
 "tek çiftti (aday 771/787); sûre 27'de dört mühür, dört ayrı çift, tekrar yok. **Sûrenin "
 "tamamında altı mühür ölçüldü ve altısı da ayrı çift** (27:6 حَكِيم|عَلِيم · 27:9 عَزِيز|حَكِيم · "
 "27:11 غَفُور|رَحِيم · 27:30 رَحْمٰن|رَحِيم · 27:40 غَنِيّ|كَرِيم · 27:78 عَزِيز|عَلِيم) — ama "
 "**27:40 ve 27:78 okunmadı; mühürlerin geçerliliği okuma denetiminden geçmediği için dizi "
 "KAPATILAMAZ.**"),
}

ATLAMA = {
 "_mercek_27_25": ("27:25 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. Kaynak: hapaks z=3,38 (خبأ *(saklı "
  "olan, gizlenmiş şey)*). Ayet bir SÜREÇ (gizli olanın çıkarılması) ve bir ALAN (gökler ve yer) "
  "adlandırıyor; **ٱلْخَبْء *(gizli olan)* korpusta tek geçiş ve neyin gizlisi olduğu "
  "belirtilmiyor** — mekanizma, ölçü ya da sınıflandırma yok. Aday 799'un önerdiği ölçütle "
  "('ölçü sözcüğü geçmesi çıpa yapmaz; ölçünün NEYİ ölçtüğü belirleyici') 'adlandırma + alan' "
  "düzeyi; eşik aşılmadı."),
 "_blok_notu_27_21_30": ("BLOK BİLANÇOSU: ★★★ 1 (27:25) · ★★ 2 (27:26, 27:29) · ★ 2 (27:23, "
  "27:30) · yıldızsız 5. Kaynaklar: hapaks x1 · pas x2 · eksen (allah+rab) x1 · eksen (allah) x1 — "
  "**hiçbiri içerikten**. **ÇIPA TABLOSU İKİNCİ GÖSTERİM: 27:24 sûrenin okunan tek gök cismi "
  "ayeti (شمس *(güneş)*) ve YILDIZSIZ; 27:25 hiçbir gök cismi anmıyor ve hapakstan ★★★.** İltifât "
  "0/10. Esmâ token 3: ikisi artefakt (مُبِين 27:21 · كَرِيم 27:29), biri geçerli mühür (27:30). "
  "Azınlık kafiyesi م blokta DÖRT kez (27:23, 26, 29, 30) — sûrenin dokuz م ayetinin dördü bu on "
  "ayette."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(21, 31):
    OM['27']["27:%d" % n] = {"ar": AR[(27, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["27:%d" % n]}
OM['27']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-26 TAM. **Sûre 27 (Neml) 30/93.** Devam: 27:31'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "27": "1-30 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1979
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 27 →', len([k for k in OM['27'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(21, 31):
    MK['27']["27:%d" % n] = M[n]
MK['27_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 27 →', len(MK['27']))
