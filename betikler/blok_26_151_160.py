# -*- coding: utf-8 -*-
"""blok_26_151_160.py — sûre 26 on üçüncü blok (26:151-160). Sâlih kıssasının kapanışı."""
import json
DIK = json.load(open('blok_dikey_26_151_160.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
151: "Aşırı gidenlerin emrine uymayın.",
152: "Onlar yeryüzünde bozgunculuk yapar, düzeltmezler.",
153: "Dediler: Sen ancak büyülenmişlerdensin.",
154: "Sen ancak bizim gibi bir beşersin; doğru söyleyenlerdensen bir âyet getir.",
155: "Dedi: İşte bir dişi deve; su içme sırası onun, belli bir günün su içme sırası da sizin.",
156: "Ona bir kötülükle dokunmayın; yoksa büyük bir günün azabı sizi yakalar.",
157: "Onu boğazladılar; sonra pişman oldular.",
158: "Azap onları yakaladı. Bunda elbette bir âyet var; ama onların çoğu inanmıyor.",
159: "Rabbin, elbette o Azîz'dir, Rahîm'dir.",
160: "Lût'un kavmi de elçileri yalanladı.",
}

O = {
151: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim yasak, kip PRO 1 · **şahıs "
 "2MP x2 — ayette başka şahıs yok**, iltifât 0 · n=4 mora=27 harf=21 (n z=-0,89), fâsıla "
 "ٱلْمُسْرِفِينَ *(aşırı gidenler)* → ن, N sınıfı; i'râb ACC 1 · GEN 1; bab IV x1; zaman IMPF 1; "
 "**biçim NEHY — sûrenin dört NEHY'inden biri**; dış düğüm 0 · yıldız ★ yok · kökler طوع *(güç "
 "yetirme, itaat)* · أمر *(emir; iş)* · سرف *(israf, aşırılık)* · bağ: **26:150 ile bitişik çift ve "
 "TERS YÖN** — orada وَأَطِيعُونِ *(bana itaat edin)* EMİR, burada وَلَا تُطِيعُوٓا۟ أَمْرَ "
 "ٱلْمُسْرِفِينَ *(aşırı gidenlerin emrine uymayın)* YASAK; **aynı kök (طوع), bitişik iki ayet, "
 "emirden yasağa**; ayrıca 25:52'de de فَلَا تُطِعِ ٱلْكَٰفِرِينَ *(inkârcılara boyun eğme)* vardı "
 "(elle, L1, aday 713)"),
152: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · **şahıs "
 "3MP x4 — ayette başka şahıs yok**, **iltifât 1 — yön 2>3; sûrenin onuncu iltifâtı** · n=6 mora=34 "
 "harf=27 (n z=-0,68), fâsıla يُصْلِحُونَ *(düzeltmezler)* → ن, N sınıfı; i'râb GEN 1; **bab IV "
 "x2 — ayetin iki fiili de bab IV**; zaman IMPF x2; **dış düğüm 1** · yıldız ★ yok · kökler فسد "
 "*(bozgunculuk, fesat)* · أرض *(yer, yeryüzü)* · صلح *(iyi, elverişli olma; ıslah)* · bağ: xref "
 "أفسد *(bozar)* + أرض *(yer)* + أصلح *(düzeltir)* → **27:48**; **26:142 ile صلح *(salâh; Sâlih)* "
 "ikinci geçişi** — orada ÖZEL AD (Sâlih), burada FİİL (düzeltmek); **aynı kök, on ayet arayla, ad "
 "ve eylem** (elle, L1, aday 714)"),
153: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3MP x2 · 2MS x1, iltifât 0 · n=5 mora=33 harf=23 (n z=-0,79), fâsıla ٱلْمُسَحَّرِينَ "
 "*(büyülenmişler)* → ن, N sınıfı; i'râb ACC 1 · GEN 1; bab I x1; zaman PERF 1; **NAKARAT alanı = "
 "2**; **esit: 26:185 ile TAM AYET ÖZDEŞ — SÛRENİN ALTINCI NAKARAT KÜMESİ, iki üyeli** · dış düğüm "
 "0 · yıldız ★ yok · kökler قول *(söz söyleme)* · سحر *(büyü, sihir)* · bağ: **25:8 ile سحر *(büyü, "
 "sihir)* karşılaştırması** — orada رَجُلا مَّسْحُورا *(büyülenmiş bir adam)* bab I ism-i mef'ûl, "
 "burada ٱلْمُسَحَّرِين bab II ism-i mef'ûl çoğulu; **aynı suçlama, iki bab** (elle, L1, aday 715)"),
154: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir + şart, kip NEG 1 · RES 1 · "
 "IMPV 1 · COND 1 · şahıs 2MS x4 · 1P x1, iltifât 0 · n=11 mora=51 harf=39 — **blokta en uzun "
 "ayet** (n z=-0,15), fâsıla ٱلصَّٰدِقِينَ *(doğru söyleyenler)* → ن, N sınıfı — **26:31'in "
 "fâsılasıyla AYNI KELİME**; i'râb NOM 2 · GEN 2; bab I x2; zaman IMPV 1 · PERF 1; **biçim HASR**; "
 "simetri [3,1,8,1]; **dış düğüm 1** · yıldız ★ yok · kökler بشر *(müjde; beşer)* · مثل *(benzer, "
 "mesel)* · أتي *(gelme, getirme)* · أيي *(âyet, işaret)* · كون *(olmak; mekân, yer)* · صدق "
 "*(doğruluk)* · bağ: xref بشر *(beşer)* + مثل *(benzer)* + أتى *(getir)* → **21:3**; **26:31 ile "
 "aynı istek yapısı** — orada Firavun فَأْتِ بِهِۦٓ إِن كُنتَ مِنَ ٱلصَّٰدِقِينَ *(doğru "
 "söyleyenlerdensen getir onu)* diyordu, burada Semûd فَأْتِ بِـَٔايَةٍ إِن كُنتَ مِنَ "
 "ٱلصَّٰدِقِينَ; **iki kavim, aynı meydan okuma kalıbı** (elle, L1, aday 716)"),
155: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — نَاقَة *(dişi deve)* aktör tablosuna "
 "GİRMİYOR · edim haber, kip işareti yok · şahıs 3MS x1 · 3FS x1 · 2MP x1, iltifât 0 · n=9 mora=44 "
 "harf=36 (n z=-0,36), fâsıla مَّعْلُومٍ *(bilinen, belirlenmiş)* → م, N sınıfı — **26:38'in "
 "fâsılasıyla AYNI KELİME**; **i'râb NOM 3 · GEN 2**; bab I x1; zaman PERF 1; **kök ikilemesi شرب "
 "*(içme)* x2 — iki tarafa iki nöbet: لَّهَا شِرْبٌ وَلَكُمْ شِرْبُ يَوْمٍ مَّعْلُومٍ**; **biçim "
 "DIKKAT**; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · نوق *(dişi deve, nâka)* · شرب "
 "*(içme)* · يوم *(gün)* · علم *(bilme; ilim)* · bağ: **26:38 ile يَوْمٍ مَّعْلُومٍ *(belirlenmiş "
 "gün)* ikinci geçişi** — orada büyücülerin toplanma vakti, burada su nöbeti günü; **aynı terkip, "
 "iki bölüşüm** (elle, L1, aday 717)"),
156: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim yasak, kip PRO 1 · şahıs 2MP x3 · "
 "3FS x1 · 3MS x1, iltifât 0 · n=7 mora=45 harf=33 (n z=-0,58), fâsıla عَظِيمٍ *(büyük)* → م, N "
 "sınıfı — **26:135'in fâsılasıyla AYNI KELİME**; **i'râb GEN 3 · NOM 1**; bab I x2; zaman IMPF x2; "
 "**biçim NEHY**; **dış düğüm 2** · yıldız ★ yok · kökler مسس *(dokunma, temas)* · سوأ *(kötülük)* · "
 "أخذ *(alma, edinme)* · عذب *(azap)* · يوم *(gün)* · عظم *(büyüklük, azamet; kemik)* · bağ: xref "
 "İKİ 3-gram (مسّ *(dokundu)* + سوء *(kötülük)* + أخذ *(aldı)* · سوء + أخذ + عذاب *(azap)*) → "
 "**ikisi de 7:73 VE 11:64**; **26:135 ile عَذَابَ يَوْمٍ عَظِيمٍ *(büyük bir günün azabı)* ikinci "
 "geçişi** — orada Hûd'un korkusu, burada Sâlih'in uyarısı (elle, L1, aday 718)"),
157: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3MP x4 · 3FS x1, iltifât 0 · n=3 mora=25 harf=20 (n z=-1,00), fâsıla نَٰدِمِينَ *(pişman "
 "olanlar)* → ن, N sınıfı; **i'râb ACC 1**; bab I x1 · IV x1; zaman PERF x2; dış düğüm 0 · yıldız "
 "★ yok · kökler عقر *(deve boğazlama; kısırlık)* · صبح *(sabah; sabaha çıkma)* · ندم *(pişmanlık)* · "
 "bağ: **عقر *(deve boğazlama; kısırlık)* korpusta 9 geçişli**; **صبح *(sabah; sabaha çıkma)* "
 "burada 'sabaha çıkmak, olmak' anlamında ve korpusta ağırlıkla 'sabah' vakti anlamında — 529 "
 "sınıfı**; **26:44 ile ندم *(pişmanlık)* karşılaştırması yok, kök sûrede tek geçiş** (elle, L1, "
 "aday 719)"),
158: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُؤْمِن *(mümin)* 10. sırada = fâsıla — ARTEFAKT, on "
 "birinci token** · aktör yok · edim haber, kip EMPH 1 · NEG 1 · şahıs 3MS x2 · 3MP x2, iltifât 0 · "
 "n=10 mora=53 harf=45 (n z=-0,26), fâsıla مُّؤْمِنِينَ → ن, N sınıfı; i'râb NOM 2 · ACC 3; bab "
 "I x2; zaman PERF x2; **açık sayı sözcüğü: كثر *(çokluk)* → أَكْثَر *(çoğu)***; **NAKARAT alanı = "
 "0 VE esit BOŞ — AMA AYET BİRİNCİ NAKARATI İÇERİYOR**: öncesine فَأَخَذَهُمُ ٱلْعَذَابُ *(azap "
 "onları yakaladı)* eklenmiş · dış düğüm 0 · yıldız ★ yok · kökler أخذ *(alma, edinme)* · عذب "
 "*(azap)* · أيي *(âyet, işaret)* · كون *(olmak; mekân, yer)* · كثر *(çokluk)* · أمن *(güven; "
 "iman)* · bağ: **ADAY 707'NİN İKİNCİ SINAMA VAKASI — nakaratın GÖMÜLÜ biçimi, ölçüm alanı "
 "yakalamıyor**; 26:139 ile aynı yapı ama önek farklı (orada فَكَذَّبُوهُ فَأَهْلَكْنَٰهُمْ, "
 "burada فَأَخَذَهُمُ ٱلْعَذَابُ) (elle, L1, aday 720)"),
159: ("eksen: **lafız YOK · رَبّ *(Rab)* 2. sırada — yirmi sekizinci Rab**, **rab z=3,94: yıldızın "
 "TEK kaynağı** · **esmâ عَزِيز *(azîz)* + رَحِيم *(rahîm)* = fâsıla — MÜHÜR; GEÇERLİ; altıncı "
 "mühür** · aktör yok · edim haber, kip EMPH 1 · şahıs 2MS x1 · 3MS x1, iltifât 0 · n=5 mora=28 "
 "harf=21 (n z=-0,79), fâsıla ٱلرَّحِيمُ → م, N sınıfı; **i'râb ACC 2 · NOM 2; fiil YOK**; "
 "**NAKARAT alanı = 8, temsil ayet 26:9**; **esit: yedi ayetle TAM ÖZDEŞ** · dış düğüm 0 · **yıldız "
 "★★★** · kökler ربب *(rab, terbiye etme)* · عزز *(izzet, üstünlük)* · رحم *(rahmet, merhamet)* · "
 "bağ: **ikinci nakaratın ALTINCI geçişi; ve nakarat ÇİFTİ İKİNCİ KEZ BOZULUYOR** — 26:158'de "
 "birinci nakarat gömülü, 26:139-140 ile aynı desen (elle, L1, aday 720)"),
160: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı لُوط *(Lût)* 3. sırada, rol "
 "mecrur — SÛRENİN ALTINCI KISSASI AÇILIYOR** · edim haber, kip işareti yok · **şahıs 3FS x1 — "
 "ayette başka şahıs yok**, iltifât 0 · n=4 mora=24 harf=18 (n z=-0,89), fâsıla ٱلْمُرْسَلِينَ "
 "*(gönderilenler)* → ن, N sınıfı — **26:105, 123, 141'in fâsılasıyla AYNI KELİME, dördüncü kez**; "
 "i'râb NOM 1 · GEN 1 · ACC 1; bab II x1; zaman PERF 1; dış düğüm 0 · yıldız ★ yok · kökler كذب "
 "*(yalan; yalanlama)* · قوم *(kalkma; kavim; kıyamet)* · رسل *(gönderme, elçi)* · bağ: **ÖN-KAYIT "
 "ÜÇÜNCÜ SINAMA — öğe (i) VAR** (aday 685/696/708); **26:105 ile BİREBİR AYNI YAPI ve AYNI UZUNLUK "
 "(n=4)**: كَذَّبَتْ + قَوْمُ + elçi adı + ٱلْمُرْسَلِينَ; **26:123 ve 26:141'de kavim tek adla "
 "verilmişti (n=3), burada ve 26:105'te tamlamayla (n=4)** — dört açılışın ikisi tamlama, ikisi tek "
 "ad (elle, L1, aday 721)"),
}

M = {
151: ("Yasak bir öncekinin tam tersi: 26:150'de وَأَطِيعُونِ *(bana itaat edin)* EMİR, burada "
 "وَلَا تُطِيعُوٓا۟ أَمْرَ ٱلْمُسْرِفِينَ *(aşırı gidenlerin emrine uymayın)* YASAK. **Aynı kök "
 "(طوع *(güç yetirme, itaat)*), bitişik iki ayet, emirden yasağa.** Ve 25:52'de de aynı kökle bir "
 "yasak vardı (فَلَا تُطِعِ ٱلْكَٰفِرِينَ *(inkârcılara boyun eğme)*) — üç geçiş, iki sûre. سرف "
 "*(israf, aşırılık)* korpusta 23 geçişli ve 25:67'de de vardı; orada harcamada aşırılık, burada "
 "bir sınıf adı. Sûrenin dört NEHY'inden biri burada."),
152: ("İki fiil karşı karşıya ve ikisi de bab IV: يُفْسِدُونَ *(bozarlar)* ve لَا يُصْلِحُونَ "
 "*(düzeltmezler)*. Ölçülebilir bir kök karşılaşması: صلح *(iyi, elverişli olma; ıslah)* on ayet "
 "önce (26:142) ÖZEL AD olarak geçmişti (Sâlih), burada FİİL olarak — **aynı kök, ad ve eylem**. "
 "Bu, 26:124'ün هود *(Yahudi olma; Hûd)* vakasıyla aynı sınıfta ama tersine: orada özel ad korpus "
 "anlamına karışıyordu, burada iki anlam AYNI SÛREDE karşı karşıya geliyor. Tek xref 27:48'e "
 "düşüyor. Ve sûrenin onuncu iltifâtı burada."),
153: ("Suçlama bir büyülenme iddiası: إِنَّمَآ أَنتَ مِنَ ٱلْمُسَحَّرِينَ *(sen ancak "
 "büyülenmişlerdensin)*. **Ve bu ayet sûrenin ALTINCI nakarat kümesini açıyor** — esit alanı 26:185 "
 "ile tam özdeşlik gösteriyor, nakarat alanı 2. Önceki beş küme 5-8 üyeliydi; bu iki üyeli, "
 "**sûrenin en küçük nakaratı**. Ölçülebilir bir bab farkı: 25:8'de itirazcılar elçiyi رَجُلا "
 "مَّسْحُورا *(büyülenmiş bir adam)* diye nitelemişti — سحر *(büyü, sihir)* bab I ism-i mef'ûl; "
 "burada ٱلْمُسَحَّرِين bab II ism-i mef'ûl çoğulu. **Aynı suçlama, iki bab, iki sûre.**"),
154: ("İtiraz iki parçalı: bir eşitleme (بَشَرٌ مِّثْلُنَا *(bizim gibi bir beşer)*) ve bir meydan "
 "okuma (فَأْتِ بِـَٔايَةٍ *(bir âyet getir)*). Ölçülebilir bir kalıp tekrarı: 26:31'de Firavun "
 "فَأْتِ بِهِۦٓ إِن كُنتَ مِنَ ٱلصَّٰدِقِينَ *(doğru söyleyenlerdensen getir onu)* demişti — "
 "**aynı fiil, aynı şart, aynı fâsıla**; değişen yalnız nesne (zamir / âyet). İki kavim, aynı "
 "meydan okuma kalıbı, yüz yirmi üç ayet arayla. Tek xref 21:3'e düşüyor. Ve أيي *(âyet, işaret)* "
 "burada 'delil, mucize' anlamında — sûrede üçüncü anlam (nakaratta 'ilâhî âyet', 26:128'de "
 "'yapı, anıt')."),
155: ("Ölçülebilir bir bölüşüm: هَٰذِهِۦ نَاقَةٌ لَّهَا شِرْبٌ وَلَكُمْ شِرْبُ يَوْمٍ مَّعْلُومٍ "
 "*(işte bir dişi deve; su içme sırası onun, belli bir günün su içme sırası da sizin)*. Kök "
 "ikilemesi شرب *(içme)* x2 ve iki tarafa iki nöbet. نوق *(dişi deve, nâka)* korpusta 7 geçişli ve "
 "dikey ölçümü ▸önce âyet x50,9 · ▸sonra عقر *(deve boğazlama; kısırlık)* x113,1 veriyor — **ikinci "
 "komşu iki ayet sonranın konusu**, yani üçlü korpusta bağlı. Ve يَوْمٍ مَّعْلُومٍ *(belirlenmiş "
 "gün)* 26:38'den geri geliyor: orada büyücülerin toplanma vakti, burada su nöbeti günü. SINIR: "
 "ayet bir SIRA DÜZENİ kuruyor (iki tarafa iki gün) ama ne süre ölçüsü ne miktar veriyor; **bu, "
 "'adlandırma + nitelik' düzeyinin biraz üstünde ama 'ölçü' değil — SINIRDA bir vaka ve YILDIZ "
 "SIFIR.**"),
156: ("Yasak bir tehditle sürüyor ve iki 3-gram'ı da aynı iki ayete düşüyor (7:73, 11:64) — donmuş "
 "kalıp adayı (aday 437). Ölçülebilir bir fâsıla tekrarı: عَذَابُ يَوْمٍ عَظِيمٍ *(büyük bir günün "
 "azabı)* 26:135'te de vardı — orada Hûd'un KORKUSU (أَخَافُ عَلَيْكُمْ), burada Sâlih'in UYARISI "
 "(فَيَأْخُذَكُمْ). **Aynı terkip, iki elçi, korkudan tehdide.** مسس *(dokunma, temas)* korpusta 61 "
 "geçişli ve dikey ölçümü ▸sonra kötülük bağlamı veriyor — çift korpusta bağlı. Sûrenin ikinci "
 "NEHY'i burada."),
157: ("Üç kelime ve üç fiil-adı: فَعَقَرُوهَا فَأَصْبَحُوا۟ نَٰدِمِينَ *(onu boğazladılar, sonra "
 "pişman oldular)*. عقر *(deve boğazlama; kısırlık)* korpusta 9 geçişli ve dikey ölçümü ▸önce نوق "
 "*(dişi deve, nâka)* x113,1 veriyor — **çift korpusta neredeyse ayrılmaz**, iki ayet önceki "
 "نَاقَة'nın komşuluğu. Ve صبح *(sabah; sabaha çıkma)* burada 'olmak, hâle gelmek' anlamında; kök "
 "korpusta 46 geçişli ve ağırlıkla 'sabah' vakti anlamında — 529 sınıfı, sûre 26'nın on dördüncü "
 "vakası. ندم *(pişmanlık)* korpusta 6 geçişli ve sûrede tek geçiş."),
158: ("**Aday 707'nin ikinci sınama vakası.** Ayet sûrenin birinci nakaratını **içeriyor** ama "
 "başına فَأَخَذَهُمُ ٱلْعَذَابُ *(azap onları yakaladı)* eklenmiş; n=10 ve **nakarat alanı 0, "
 "esit alanı boş** — 26:139 ile birebir aynı davranış, yalnız önek farklı. **İki gömülü vaka da "
 "kaçırılıyor; nakarat sayımı 6 değil 8.** Ve fâsıladaki مُؤْمِن sûrenin on birinci artefaktı. أخذ "
 "*(alma, edinme)* burada 26:156'nın tehdidinin gerçekleşmesi: orada فَيَأْخُذَكُمْ *(sizi "
 "yakalar)*, burada فَأَخَذَهُمُ *(onları yakaladı)* — **aynı kök, iki ayet arayla, tehditten "
 "gerçekleşmeye**."),
159: ("İkinci nakaratın altıncı geçişi. **Ve nakarat çifti ikinci kez bozuluyor:** 26:158'de birinci "
 "nakarat gömülü, burada ikincisi ayrı ayet — 26:139-140 ile birebir aynı desen. Yani **çift yapısı "
 "Nûh, İbrâhîm ve Mûsâ kıssalarında bütün (iki ayrı ayet), Hûd ve Sâlih kıssalarında kırık (biri "
 "gömülü)**. Ölçülebilir bir mimari ayrım ve ölçüm alanı bunu göstermiyor. Sûrenin altı mühürlü "
 "konumunun altısı da geçerli (aday 501/598 ile uyumlu)."),
160: ("**Ön-kaydın üçüncü sınaması başlıyor** ve öğe (i) — **var**. Ölçülebilir bir açılış "
 "tipolojisi: dört kıssa açılışının ikisi kavmi TAMLAMAYLA veriyor (26:105 قَوْمُ نُوحٍ, burada "
 "قَوْمُ لُوطٍ; n=4), ikisi TEK ADLA (26:123 عَادٌ, 26:141 ثَمُودُ; n=3). **Yani açılış formülü "
 "sabit ama kavmin adlandırılma biçimi değişiyor** ve bu, uzunluğu bir kelime kaydırıyor. esit "
 "alanı dördünü de birbirine bağlamıyor. Ve ٱلْمُرْسَلِينَ *(gönderilenler)* dördüncü kez fâsıla."),
}

ATLAMA = {
 "_mercek_26_159": ("26:159 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. Nakarat ayeti (ikinci kümenin "
  "altıncı geçişi), tek kaynak rab z=3,94. Bağımsız gözlem değil (adaylar 606, 683, 700, 707)."),
 "_blok_notu_26_151_160": ("BLOK BİLANÇOSU: ★★★ 1 (26:159) · ★★ 0 · ★ 0 · 9 ayet yıldızsız — "
  "26:71-80 ile birlikte okumada en az yıldızlı iki bloktan biri. **TEK ★★★ AYET NAKARAT.** "
  "ÇIPA NOTU — SINIRDA BİR VAKA: 26:155 bir SIRA DÜZENİ kuruyor (نَاقَة *(dişi deve)* için bir "
  "gün, kavim için bir gün; شرب *(içme)* kökü ikilenmiş) ve bu, aday 561'in ölçütünde 'adlandırma "
  "+ nitelik' düzeyinin biraz ÜSTÜNDE — bir BÖLÜŞÜM KURALI var. Ama ne süre ölçüsü, ne miktar, ne "
  "mekanizma veriliyor; ve olay ne biyolojik ne astronomik (bir hukuk/paylaşım düzenlemesi). "
  "**Çıpa SINIRDA sayıldı, mercek yazılmadı** — ayet zaten yıldızsız olduğu için eşik de aşılmıyor. "
  "Bu, 25:25'in (gök yarılması, 'olay var ölçü yok') sınıfına benzer bir kayıt. SÛRE 26'NIN OKUNAN "
  "160 AYETİNDE ★★★ 34."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(151, 161):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 160/227.** Devam: 26:161'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-160 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1882
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(151, 161):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
