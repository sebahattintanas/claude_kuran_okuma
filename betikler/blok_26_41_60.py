# -*- coding: utf-8 -*-
"""blok_26_41_60.py — sûre 26 üçüncü blok (26:41-60). Büyücülerin secdesi."""
import json
DIK = json.load(open('blok_dikey_26_41_60.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
41: "Büyücüler geldiğinde Firavun'a dediler: Galip gelenler biz olursak bize bir ücret var mı?",
42: "Dedi: Evet; o zaman siz mutlaka yakınlardan olursunuz.",
43: "Mûsâ onlara dedi: Atacağınızı atın.",
44: "İplerini ve asâlarını attılar ve dediler: Firavun'un izzetine, galip gelenler elbette biziz.",
45: "Mûsâ da asâsını attı; bir de baktılar ki uydurduklarını yutuyor.",
46: "Bunun üzerine büyücüler secdeye kapandı.",
47: "Dediler: Âlemlerin Rabbine iman ettik.",
48: "Mûsâ'nın ve Hârûn'un Rabbine.",
49: "Dedi: Ben size izin vermeden ona iman ettiniz. O, size büyüyü öğreten büyüğünüzmüş. Yakında bileceksiniz: ellerinizi ve ayaklarınızı çaprazlama keseceğim ve hepinizi asacağım.",
50: "Dediler: Zarar yok; biz Rabbimize dönenleriz.",
51: "İlk iman edenler olduğumuz için Rabbimizin hatalarımızı bağışlamasını umuyoruz.",
52: "Mûsâ'ya vahyettik: Kullarımı geceleyin yürüt; siz izleneceksiniz.",
53: "Firavun şehirlere toplayıcılar gönderdi.",
54: "Bunlar azınlık bir döküntü topluluk.",
55: "Ve onlar bizi öfkelendiriyorlar.",
56: "Biz ise tedbirli bir topluluğuz.",
57: "Böylece onları bahçelerden ve pınarlardan çıkardık.",
58: "Hazinelerden ve değerli bir konumdan.",
59: "Böyle; onları İsrâiloğullarına miras kıldık.",
60: "Güneş doğarken onların ardına düştüler.",
}

O = {
41: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı فِرْعَوْن *(Firavun)* 5. sırada, "
 "rol mecrur** · edim soru + şart, kip INTG 1 · EMPH 1 · COND 1 · şahıs 1P x4 · 3MP x2 · 3MS x1, "
 "iltifât 0 · n=12 mora=69 harf=51 (n z=-0,04), fâsıla ٱلْغَٰلِبِينَ *(galip gelenler)* → ن, N "
 "sınıfı — **26:40'ın fâsılasıyla AYNI KELİME, bitişik ayette**; i'râb ACC 3 · NOM 1 · GEN 1; "
 "bab I x3; zaman PERF x3; simetri [3,5,9,1]; **dış düğüm 2** · yıldız ★ yok · kökler جيأ *(gelme)* · "
 "سحر *(büyü, sihir)* · قول *(söz söyleme)* · أجر *(ücret, karşılık)* · كون *(olmak; mekân, yer)* · "
 "غلب *(galip gelme, üstünlük)* · bağ: xref DÖRT 3-gram → **7:113** (dördü de); جاء *(geldi)* + ساحر "
 "*(büyücü)* + قال *(dedi)* ayrıca **10:80**; **25:57 ile أجر *(ücret, karşılık)* karşıtlığı** — "
 "orada elçi 'sizden ücret istemiyorum' diyordu, burada büyücüler ücret İSTİYOR (elle, L1, aday 626)"),
42: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip EMPH 1 · şahıs 3MS x1 · "
 "2MP x1, iltifât 0 · n=6 mora=38 harf=26 (n z=-0,68), fâsıla ٱلْمُقَرَّبِينَ *(yakınlaştırılanlar)* → "
 "ن, N sınıfı; i'râb ACC 1 · GEN 1; bab I x1; zaman PERF x1; dış düğüm 0 · yıldız ★ yok · kökler "
 "قول *(söz söyleme)* · قرب *(yakınlık, yaklaşma)* · bağ: **قرب *(yakınlık, yaklaşma)* bab II ism-i "
 "mef'ûl — ücretin karşılığı para değil KONUM**; 26:58'de aynı alan مَقَامٍ كَرِيمٍ *(değerli bir "
 "konum)* olarak dönecek (elle, L1, aday 627)"),
43: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı مُوسَى *(Mûsâ)* 3. sırada, rol FAİL** · "
 "edim emir, kip IMPV 1 · şahıs 2MP x3 · 3MS x1 · 3MP x1, iltifât 0 · n=7 mora=39 harf=27 (n z=-0,58), "
 "fâsıla مُّلْقُونَ *(atanlar)* → ن, N sınıfı; i'râb NOM 2; bab I x1 · IV x1; zaman PERF x1 · IMPV 1; "
 "**kök ikilemesi لقي *(karşılaşma, kavuşma; atma)* x2 — emir + ism-i fâil: أَلْقُوا۟ مَآ أَنتُم "
 "مُّلْقُونَ *(atacağınızı atın)***; simetri [3,2,5,1]; dış düğüm 1 · yıldız ★ yok · kökler قول "
 "*(söz söyleme)* · لقي *(karşılaşma, kavuşma; atma)* · bağ: xref قال *(dedi)* + ألقى *(attı)* + "
 "ملقي *(atan)* → **10:80**; **لقي kökü 26:43-46 arasında BEŞ KEZ — dört ardışık ayette** "
 "(elle, L1, aday 628)"),
44: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı فِرْعَوْن *(Firavun)* 6. sırada, rol "
 "MEF'ÛL** · edim haber, kip EMPH 1 · şahıs 3MP x6 · 1P x2, iltifât 0 · n=9 mora=56 harf=49 "
 "(n z=-0,36), fâsıla ٱلْغَٰلِبُونَ *(galip gelenler)* → ن, N sınıfı — **üç ayette üçüncü kez aynı "
 "kök fâsılada** (26:40, 41, 44); **i'râb ACC 4 · GEN 1 · NOM 1**; bab I x1 · IV x1; zaman PERF x2; "
 "dış düğüm 1 · yıldız ★ yok · kökler لقي *(karşılaşma, kavuşma; atma)* · حبل *(ip, halat)* · عصو "
 "*(asâ, değnek)* · قول *(söz söyleme)* · عزز *(izzet, üstünlük)* · غلب *(galip gelme, üstünlük)* · "
 "bağ: xref ألقى *(attı)* + حبل *(ip)* + عصيّ *(asâlar)* → **20:66**; **عزز *(izzet, üstünlük)* — "
 "26:9'da esmâ (ٱلْعَزِيزُ *(azîz)*), burada BİR İNSANIN izzetine yemin (بِعِزَّةِ فِرْعَوْنَ "
 "*(Firavun'un izzetine)*): aynı kök, ilâhî ve beşerî iki gönderge** (elle, L1, aday 629)"),
45: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı مُوسَى *(Mûsâ)* 2. sırada, rol FAİL** · "
 "edim haber, kip işareti yok · şahıs 3MS x2 · 3FS x2 · 3MP x2, iltifât 0 · n=8 mora=40 harf=31 "
 "(n z=-0,47), fâsıla يَأْفِكُونَ *(uyduruyorlar)* → ن, N sınıfı; i'râb NOM 1 · ACC 1; bab I x2 · "
 "IV x1; zaman PERF x1 · IMPF x2; simetri [3,2,5,1]; dış düğüm 1 · yıldız ★ yok · kökler لقي "
 "*(karşılaşma, kavuşma; atma)* · عصو *(asâ, değnek)* · لقف *(kapıp yutma)* · أفك *(iftira, uydurma "
 "(ifk); döndürülme)* · bağ: xref ألقى *(attı)* + عصا *(asâ)* + تلقف *(yutuyor)* ve عصا + تلقف + أفك "
 "*(uydurma)* → **ikisi de 7:117**; **25:4 ile أفك karşılaştırması** — orada إِفْكٌ ٱفْتَرَىٰهُ "
 "*(uydurduğu bir yalan)* Kur'ân için söylenmişti, burada uyduran taraf büyücüler (elle, L1, aday 630)"),
46: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "3MS x1 — ayette başka şahıs yok**, iltifât 0 · n=3 mora=21 harf=16 — **sûrenin en kısa "
 "ayetlerinden** (n z=-1,00), fâsıla سَٰجِدِينَ *(secde edenler)* → ن, N sınıfı; i'râb NOM 1 · ACC 1; "
 "bab IV x1; zaman PERF x1; **edilgen 1 — فَأُلْقِىَ *(kapandılar, atıldılar)*; ayetin TEK fiili ve "
 "o da edilgen, oran 1,00**, pas z=5,38: **yıldızın TEK kaynağı**; **dış düğüm 2** · **yıldız ★★★** · "
 "kökler لقي *(karşılaşma, kavuşma; atma)* · سحر *(büyü, sihir)* · سجد *(secde)* · bağ: xref ألقى "
 "*(atıldı)* + ساحر *(büyücü)* + ساجد *(secde eden)* → **7:120 · 20:70**; **لقي *(atma)* dördüncü "
 "ardışık ayette ve BURADA EDİLGEN** — 26:43 emir, 26:44 büyücüler atıyor, 26:45 Mûsâ atıyor, 26:46 "
 "büyücüler ATILIYOR: aynı kök dört ayette çatı ve fâil değiştirerek (elle, L1, aday 628)"),
47: ("eksen: **lafız YOK · رَبّ *(Rab)* 3. sırada — on birinci Rab**, **rab z=5,01: yıldızın TEK "
 "kaynağı** (n=4, oran 0,25) · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs 3MP x2 · "
 "1P x2, iltifât 0 · n=4 mora=31 harf=21 (n z=-0,89), fâsıla ٱلْعَٰلَمِينَ *(âlemler)* → ن, N sınıfı; "
 "i'râb GEN 2; bab I x1 · IV x1; zaman PERF x2; **dış düğüm 2** · **yıldız ★★★** · **esit: 7:121 ile "
 "TAM AYET ÖZDEŞ** · kökler قول *(söz söyleme)* · أمن *(güven, iman)* · ربب *(rab, terbiye etme)* · "
 "علم *(bilme; âlem)* · bağ: xref قال *(dedi)* + آمن *(iman etti)* + ربّ *(Rab)* → **7:121 · 20:70**; "
 "**26:23 ile halka** — Firavun'un وَمَا رَبُّ ٱلْعَٰلَمِينَ *(âlemlerin Rabbi de ne)* sorusuna "
 "cevap, ama soruyu soran değil BÜYÜCÜLER veriyor (elle, L1, aday 631)"),
48: ("eksen: **lafız YOK · رَبّ *(Rab)* 1. sırada — on ikinci Rab**, **rab z=6,78: OKUMADA GÖRÜLEN "
 "İKİNCİ EN YÜKSEK Z** (n=3, oran 0,33) ve yıldızın TEK kaynağı · esmâ yok · **aktör: adlı مُوسَى "
 "*(Mûsâ)* 2. sırada rol FAİL, هارُون *(Hârûn)* 3. sırada rol MEF'ÛL** · edim haber, kip işareti "
 "yok · **şahıs eki YOK, fiil YOK** · n=3 mora=18 harf=11 — **sûrenin okunan en kısa ayeti** "
 "(n z=-1,00), fâsıla هَٰرُونَ *(Hârûn)* → ن, N sınıfı — **fâsıla bir ÖZEL AD ve sınıfa uyuyor** "
 "(26:13 ile aynı); i'râb GEN 1 · NOM 1 · ACC 1; dış düğüm 1 · **yıldız ★★★** · **esit: 7:122 ile "
 "TAM AYET ÖZDEŞ** · **TEK KÖK: ربب *(rab, terbiye etme)*** · bağ: **26:47-48 ↔ 7:121-122 ARDIŞIK "
 "BÖLÜT İKİZİ ve esit alanı İKİSİNİ DE YAKALIYOR** — sûre 26'da ikinci ardışık ikiz (birincisi "
 "26:32-33 ↔ 7:107-108), aday 621'e ikinci veri (elle, L1)"),
49: ("eksen: **lafız YOK · Rab YOK** · **esmâ كَبِير *(büyük)* 9. sırada, ORTA konum, MÜHÜRSÜZ — "
 "ÖLÇÜM ARTEFAKTI**: لَكَبِيرُكُمُ ٱلَّذِى عَلَّمَكُمُ ٱلسِّحْرَ *(size büyüyü öğreten "
 "büyüğünüz)*, gönderge BİR İNSAN; ölçüt (a) dışlıyor · aktör yok · edim haber, kip EMPH 6 · FUT 1 — "
 "**yedi kip işareti, okumada en yoğun** · **şahıs 2MP x10 — okumada tek şahıstan en yüksek sayım**; "
 "3MS x4 · 1S x3, iltifât 0 · n=21 mora=116 harf=102 — **sûrenin en uzun ayeti** (n z=0,91), fâsıla "
 "أَجْمَعِينَ *(hepiniz)* → ن, N sınıfı; **i'râb ACC 6 · NOM 1 · GEN 1**; bab I x3 · II x3 · IV x1; "
 "zaman PERF x3 · IMPF x4; **kök ikilemesi علم *(bilme; ilim)* x2 — öğretme ve bilme: عَلَّمَكُمُ "
 "*(size öğretti)* ve لَسَوْفَ تَعْلَمُونَ *(yakında bileceksiniz)***; simetri [3,3,8,1]; **dış "
 "düğüm 3** · yıldız ★ yok · kökler قول *(söz söyleme)* · أمن *(güven, iman)* · قبل *(ön, önce; "
 "kabul)* · أذن *(izin; kulak)* · كبر *(büyüklük; büyüklenme)* · علم *(bilme; ilim)* · سحر *(büyü, "
 "sihir)* · قطع *(kesme)* · يدي *(el)* · رجل *(adam; ayak)* · خلف *(ardıl, halef; arka)* · صلب "
 "*(katılık; asma)* · جمع *(toplama, cem)* · bağ: xref **YEDİ 3-gram** → 7:123, 7:124, 20:71 "
 "(elle, L1, aday 632)"),
50: ("eksen: **lafız YOK · رَبّ *(Rab)* 6. sırada — on üçüncü Rab** (rab z=2,72) · esmâ yok · aktör "
 "yok · edim haber, kip NEG 1 · şahıs 3MP x2 · 1P x2, iltifât 0 · n=7 mora=39 harf=29 (n z=-0,58), "
 "fâsıla مُنقَلِبُونَ *(dönenler)* → ن, N sınıfı; i'râb ACC 2 · GEN 1 · NOM 1; bab I x1; zaman "
 "PERF x1; **HAPAKS: ضير *(zarar verme)* — korpusta TEK geçiş** (hapaks z=3,38); dış düğüm 0 · "
 "**yıldız ★★★ — İKİ KAYNAKLI: rab z=2,72 VE hapaks z=3,38**; sûre 25'te yıldızı iki kaynaktan alan "
 "tek ayet vardı (25:73), sûre 26'da bu ikincisi (26:73 ile birlikte üçüncü olacak) · kökler قول "
 "*(söz söyleme)* · ضير *(zarar verme)* · ربب *(rab, terbiye etme)* · قلب *(kalp; çevrilme, dönme)* · "
 "bağ: **26:29 ile karşıtlık** — Firavun ٱلْمَسْجُونِينَ *(zindana atılanlar)* tehdidi savurmuştu, "
 "burada tehdidin muhatabı لَا ضَيْرَ *(zarar yok)* diyor (elle, L1, aday 633)"),
51: ("eksen: **lafız YOK · رَبّ *(Rab)* 6. sırada — on dördüncü Rab** (rab z=1,62: yıldızın TEK "
 "kaynağı) · **esmâ مُؤْمِن *(mümin)* 11. sırada = fâsıla — ARTEFAKT, sûrenin üçüncü مُؤْمِن "
 "tokeni** · aktör yok · edim haber, kip işareti yok · **şahıs 1P x7 — blokta en yüksek**; 3MS x1, "
 "iltifât 0 · n=11 mora=59 harf=41 (n z=-0,15), fâsıla ٱلْمُؤْمِنِينَ → ن, N sınıfı; i'râb ACC 2 · "
 "NOM 1 · GEN 2; bab I x3; zaman IMPF x2 · PERF x1; dış düğüm 0 · **yıldız ★** · kökler طمع *(tamah, "
 "umma)* · غفر *(bağışlama, mağfiret)* · ربب *(rab, terbiye etme)* · خطأ *(hata, günah)* · كون "
 "*(olmak; mekân, yer)* · أول *(ilk, evvel)* · أمن *(güven, iman)* · bağ: **26:50 ile bitişik çift** — "
 "orada dönüş yönü (مُنقَلِبُونَ *(dönenler)*), burada dönüşün beklentisi (يَغْفِرَ *(bağışlaması)*); "
 "**أول *(ilk, evvel)* — 26:26'da ٱلْأَوَّلِينَ *(öncekiler)* atalar için, burada أَوَّلَ "
 "ٱلْمُؤْمِنِينَ *(ilk iman edenler)*: aynı kök, geçmişten öncülüğe** (elle, L1, aday 634)"),
52: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı مُوسَى *(Mûsâ)* 3. sırada, rol "
 "mecrur** · edim emir, kip IMPV 1 · şahıs 1P x2 · 2MS x1 · 1S x1 · 2MP x1, iltifât 0 · n=8 mora=53 "
 "harf=36 (n z=-0,47), fâsıla مُتَّبَعُونَ *(izlenenler)* → ن, N sınıfı; i'râb GEN 2 · ACC 1 · "
 "NOM 1; **bab IV x2**; zaman PERF x1 · IMPV 1; dış düğüm 1 · yıldız ★ yok · kökler وحي *(vahiy)* · "
 "سري *(gece yürüyüşü, isrâ)* · عبد *(kul, kulluk)* · تبع *(uyma, ardından gitme)* · bağ: xref "
 "أوحى *(vahyetti)* + أسرى *(geceleyin yürüttü)* + عبد *(kul)* → **20:77**; **تبع *(uyma, ardından "
 "gitme)* — 26:40'ta büyücülere UYMA niyeti, burada İZLENME (edilgen ism-i mef'ûl مُتَّبَعُونَ): "
 "aynı kök, ters çatı ve ters değer** (elle, L1, aday 635)"),
53: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı فِرْعَوْن *(Firavun)* 2. sırada, "
 "rol FAİL** · edim haber, kip işareti yok · şahıs 3MS x1, **iltifât 1 — yön 12>3; sûrenin ikinci "
 "iltifâtı** · n=5 mora=31 harf=24 (n z=-0,79), fâsıla حَٰشِرِينَ *(toplayıcılar)* → ن, N sınıfı — "
 "**26:36'nın fâsılasıyla AYNI KELİME**; i'râb NOM 1 · GEN 1 · ACC 1; bab IV x1; zaman PERF x1; "
 "dış düğüm 1 · yıldız ★ yok · kökler رسل *(gönderme, elçi)* · مدن *(şehir, medine)* · حشر "
 "*(toplama, mahşer)* · bağ: xref أرسل *(gönderdi)* + مدائن *(şehirler)* + حاشر *(toplayıcı)* → "
 "**7:111**; **26:36 ile TERKİP TEKRARI** — orada ileri gelenler ÖNERİYORDU (وَٱبْعَثْ فِى "
 "ٱلْمَدَآئِنِ حَٰشِرِينَ *(şehirlere toplayıcılar gönder)*), burada Firavun UYGULUYOR; öneri ve "
 "uygulama on yedi ayet arayla aynı kelimelerle (elle, L1, aday 636)"),
54: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip EMPH 1 · **şahıs eki "
 "YOK, fiil YOK** · n=4 mora=31 harf=20 (n z=-0,89), fâsıla قَلِيلُونَ *(azınlık)* → ن, N sınıfı; "
 "i'râb ACC 1 · NOM 2; **HAPAKS: شرذم *(döküntü, azınlık topluluk (şirzime))* — korpusta TEK "
 "geçiş** (hapaks z=3,38: **yıldızın TEK kaynağı**); **açık sayı sözcüğü: قلل *(azlık)* → "
 "قَلِيلُونَ *(azınlık)***; **biçim DIKKAT**; dış düğüm 0 · **yıldız ★★★** · kökler شرذم *(döküntü, "
 "azınlık topluluk (şirzime))* · قلل *(azlık)* · bağ: **26:54-56 üçlüsü — Firavun'un kendi kavmine "
 "seslenişi; üç ayet de kısa (n=4, 3, 3) ve üçü de إِنَّ *(gerçekten)* ile açılıyor** (elle, L1, "
 "aday 637)"),
55: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip EMPH 1 · şahıs 3MP x1 · "
 "1P x1, iltifât 0 · n=3 mora=23 harf=15 — **sûrenin en kısa ayetlerinden** (n z=-1,00), fâsıla "
 "لَغَآئِظُونَ *(öfkelendirenler)* → ن, N sınıfı; i'râb ACC 1 · NOM 1; **fiil yok**; dış düğüm 0 · "
 "yıldız ★ yok · **TEK KÖK: غيظ *(öfke, gayz)*** · bağ: **25:12 ile غيظ *(öfke, gayz)* ikinci "
 "geçişi** — orada ateşin öfkesi (تَغَيُّظا *(öfkeli kaynama)*), burada bir topluluğun öfkelendirmesi; "
 "kök korpusta 11 geçişli (elle, L1, aday 637)"),
56: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip EMPH 1 · şahıs 1P x1, "
 "iltifât 0 · n=3 mora=22 harf=14 (n z=-1,00), fâsıla حَٰذِرُونَ *(tedbirli olanlar)* → ن, N sınıfı; "
 "i'râb ACC 1 · NOM 2; **fiil yok**; dış düğüm 0 · yıldız ★ yok · kökler جمع *(toplama, cem)* · حذر "
 "*(sakınma, tedbir)* · bağ: **26:38-39 ile جمع *(toplama, cem)* üçüncü ve dördüncü geçişi** — "
 "orada büyücüler ve halk toplanıyordu (edilgen ve etken), burada Firavun'un kavmi kendini "
 "'toplanmış' (جَمِيع) olarak tanımlıyor; aynı kök üç ayrı özneyle (elle, L1, aday 637)"),
57: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — جَنَّٰت *(bahçeler)* aktör tablosuna "
 "GİRMİYOR (sûre 25'te 25:24'te girmişti; tutarsızlık, aday 462) · edim haber, kip işareti yok · "
 "şahıs 1P x2 · 3MP x1, iltifât 0 · n=4 mora=26 harf=20 (n z=-0,89), fâsıla وَعُيُونٍ *(pınarlar)* → "
 "ن, N sınıfı; **i'râb GEN 2**; bab IV x1; zaman PERF x1; dış düğüm 0 · yıldız ★ yok · kökler خرج "
 "*(çıkma, çıkarma)* · جنن *(örtme, gizleme; cennet; cin; delilik)* · عين *(göz; pınar)* · bağ: "
 "**26:35 ile خرج *(çıkma, çıkarma)* karşıtlığı** — orada Firavun 'sizi yurdunuzdan çıkarmak "
 "istiyor' diye SUÇLUYORDU, burada çıkarılan KENDİLERİ oluyor; aynı kök bab IV, fâil değişiyor "
 "(elle, L1, aday 638)"),
58: ("eksen: **lafız YOK · Rab YOK** · **esmâ كَرِيم *(kerîm)* 3. sırada = fâsıla, MÜHÜRSÜZ — "
 "ÖLÇÜM ARTEFAKTI**: gönderge مَقَام *(konum, makam)*; sûrenin üçüncü كَرِيم artefaktı (26:7, 26:58 "
 "ve 26:72'de gelecek) · aktör yok · edim haber, kip işareti yok · **şahıs eki YOK, fiil YOK** · "
 "n=3 mora=22 harf=17 (n z=-1,00), fâsıla كَرِيمٍ *(değerli)* → م, N sınıfı; **i'râb GEN 3 — üç "
 "kelimenin üçü de mecrur**; dış düğüm 0 · yıldız ★ yok · kökler كنز *(hazine)* · قوم *(kalkma; "
 "kavim; kıyamet)* · كرم *(kerem, onur)* · bağ: **26:42 ile halka** — orada büyücülere vaat edilen "
 "ٱلْمُقَرَّبِينَ *(yakınlaştırılanlar)* konumuydu, burada kaybedilen مَقَامٍ كَرِيمٍ *(değerli bir "
 "konum)*; **قرب *(yakınlık)* ve قوم *(makam)* iki ayrı kök ama aynı konum alanı** (elle, L1, "
 "aday 627)"),
59: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı إِسْرائِيل *(İsrâîl)* 4. sırada, "
 "rol mecrur** · edim haber, kip işareti yok · şahıs 1P x2 · 3FS x1, iltifât 0 · n=4 mora=33 harf=21 "
 "(n z=-0,89), **fâsıla إِسْرَٰٓءِيلَ *(İsrâîl)* → ل — SÛRENİN ÜÇÜNCÜ KAFİYE KIRILMASI VE YİNE AYNI "
 "ÖZEL AD** (kafiye_kirik=1; yıldızın TEK kaynağı); i'râb ACC 1 · GEN 1; bab IV x1; zaman PERF x1; "
 "dış düğüm 0 · **yıldız ★** · kökler ورث *(miras, vâris olma)* · بني *(oğul, evlat)* · bağ: **26:17, "
 "26:22 ile ÜÇÜNCÜ kez aynı fâsıla** — sûrenin dört kırılmasından üçü aynı özel adla; **ADAY 612 "
 "GÜÇLENDİ** (elle, L1)"),
60: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3MP x3, iltifât 0 · n=2 mora=19 harf=14 — **sûrenin okunan en kısa ayetlerinden, 26:48 ile "
 "birlikte** (n z=-1,11; okumada görülen en düşük n z), fâsıla مُّشْرِقِينَ *(gün doğarken olanlar)* → "
 "ن, N sınıfı; **i'râb ACC 1**; bab IV x1; zaman PERF x1; dış düğüm 0 · yıldız ★ yok · kökler تبع "
 "*(uyma, ardından gitme)* · شرق *(doğu; doğuş)* · bağ: **26:28 ve 26:52 ile şرق *(doğu; doğuş)* ve "
 "تبع *(uyma, ardından gitme)* karşılaşması** — 26:28'de doğu bir KAPSAM terimiydi (رَبُّ "
 "ٱلْمَشْرِقِ *(doğunun Rabbi)*), burada bir ZAMAN belirteci (مُّشْرِقِينَ *(gün doğarken)*); ve "
 "26:52'de إِنَّكُم مُّتَّبَعُونَ *(izleneceksiniz)* uyarısı burada gerçekleşiyor (elle, L1, aday 635)"),
}

M = {
41: ("Büyücülerin ilk sözü bir pazarlık: أَئِنَّ لَنَا لَأَجْرا *(bize bir ücret var mı)*. "
 "Ölçülebilir bir karşıtlık: 25:57'de elçi مَآ أَسْـَٔلُكُمْ عَلَيْهِ مِنْ أَجْرٍ *(buna karşılık "
 "sizden bir ücret istemiyorum)* diyordu — أجر *(ücret, karşılık)* orada REDDEDİLEN, burada "
 "İSTENEN. Ve sûre 26'nın nakaratlarından biri de tam bu cümle (26:109, 127, 145, 164, 180; henüz "
 "okunmadı). Dört xref'in dördü de 7:113'e düşüyor: terkip korpusta sabit. Ve fâsıla ٱلْغَٰلِبِينَ "
 "*(galip gelenler)* 26:40'tan birebir geri geliyor — bitişik ayette aynı kelime."),
42: ("Firavun'un cevabı ücreti bir konuma çeviriyor: وَإِنَّكُمْ إِذا لَّمِنَ ٱلْمُقَرَّبِينَ *(o "
 "zaman siz mutlaka yakınlardan olursunuz)*. قرب *(yakınlık, yaklaşma)* bab II ism-i mef'ûl; "
 "korpusta 96 geçişli ve dikey ölçümü ▸önce melek bağlamı veriyor — kök korpusta ağırlıkla ilâhî "
 "yakınlık için, burada saray yakınlığı (aday 529 sınıfı). Ölçülebilir bir alan halkası: vaat "
 "edilen konum 26:58'de kaybedilen konum olarak dönecek — مَقَامٍ كَرِيمٍ *(değerli bir konum)*."),
43: ("Emir bir kök ikilemesiyle veriliyor: أَلْقُوا۟ مَآ أَنتُم مُّلْقُونَ *(atacağınızı atın)* — "
 "لقي *(karşılaşma, kavuşma; atma)* emir ve ism-i fâil olarak. Ölçülebilir bir yoğunluk: kök "
 "26:43-46 arasında BEŞ kez ve dört ardışık ayette. Ve her seferinde fâil ya da çatı değişiyor: "
 "burada emir (2MP), 26:44'te büyücüler atıyor (3MP), 26:45'te Mûsâ atıyor (3MS), 26:46'da "
 "büyücüler ATILIYOR (edilgen). Dört ayette bir kökün fâil-çatı yörüngesi."),
44: ("Büyücülerin yemini bir insanın izzetine: بِعِزَّةِ فِرْعَوْنَ *(Firavun'un izzetine)*. "
 "Ölçülebilir bir gönderge karşıtlığı: عزز *(izzet, üstünlük)* 26:9'da sûrenin nakarat mührünün "
 "ilk terimiydi (ٱلْعَزِيزُ *(azîz)*, ilâhî), burada beşerî. Aynı kök, iki gönderge, otuz beş ayet "
 "arayla. Ve fâsıla ٱلْغَٰلِبُونَ *(galip gelenler)* üç ayette üçüncü kez (26:40, 41, 44) — kök "
 "غلب *(galip gelme, üstünlük)* fâsılada kümeleniyor; sûrenin fâsıla kısıtı (N sınıfı, ism-i fâil "
 "çoğulu) bunu kolaylaştırıyor (aday 600 sınıfı)."),
45: ("Karşılık tek fiille geliyor: تَلْقَفُ مَا يَأْفِكُونَ *(uydurduklarını yutuyor)*. لقف *(kapıp "
 "yutma)* korpusta 3 geçişli ve dikey ölçümü ▸önce asâ bağlamı veriyor — kök yalnız bu sahnede. "
 "أفك *(iftira, uydurma (ifk); döndürülme)* ise 25:4'ten geri geliyor: orada إِفْكٌ ٱفْتَرَىٰهُ "
 "*(uydurduğu bir yalan)* Kur'ân için söylenmişti, burada uyduran taraf büyücüler — aynı kök, "
 "suçlayan ve suçlanan yer değiştirmiş. İki xref de 7:117'ye düşüyor."),
46: ("Üç kelime ve ayetin tek fiili edilgen: فَأُلْقِىَ ٱلسَّحَرَةُ سَٰجِدِينَ *(büyücüler secdeye "
 "kapandı)*. Oran 1,00 → pas z=5,38; yıldızın tek kaynağı bu. **Ölçülebilir bir çatı dönüşü:** üç "
 "ayet boyunca لقي *(karşılaşma, kavuşma; atma)* kökünün fâili insanlardı (atın, attılar, attı), "
 "burada aynı kök edilgen ve özneler nesne oluyor. Atma eyleminden atılma hâline. Ve secde "
 "26:64'te değil BURADA, yani karşılık verilmeden önce — sahne bir teslimiyetle kapanıyor."),
47: ("Dört kelime ve rab z=5,01 — n=4, tek Rab, oran 0,25. Ölçülebilir bir halka: 26:23'te Firavun "
 "وَمَا رَبُّ ٱلْعَٰلَمِينَ *(âlemlerin Rabbi de ne)* diye sormuştu; cevabı Mûsâ 26:24 ve 26:28'de "
 "vermişti ama **soruyu kapatan cevap burada, ve veren taraf BÜYÜCÜLER**. Aynı terkip "
 "(رَبِّ ٱلْعَٰلَمِينَ) yirmi dört ayet arayla soru ve ikrar olarak. Ayet 7:121 ile TAM AYET ÖZDEŞ "
 "ve esit alanı yakalıyor."),
48: ("Üç kelime, hiç fiil yok, tek kök: ربب *(rab, terbiye etme)*. **rab z=6,78 — okumada görülen "
 "ikinci en yüksek z** (n=3, oran 0,33; birincisi 26:26'da 8,20). Ölçülebilir bir belirginleştirme: "
 "26:47'de رَبِّ ٱلْعَٰلَمِينَ *(âlemlerin Rabbi)* genel, burada رَبِّ مُوسَىٰ وَهَٰرُونَ *(Mûsâ'nın "
 "ve Hârûn'un Rabbi)* özel — genelden özele, ve iki ayet ardışık. Fâsıla bir özel ad ve sınıfa "
 "uyuyor (26:13 ile aynı). **26:47-48 ↔ 7:121-122 ardışık bölüt ikizi ve esit alanı ikisini de "
 "yakalıyor** — sûre 26'da ikinci ardışık ikiz."),
49: ("Sûrenin en uzun ayeti (n=21) ve okumada tek şahıstan en yüksek sayım (2MP x10). Ölçülebilir "
 "bir kip yoğunluğu: EMPH altı kez ve FUT bir kez — yedi kip işareti, okumada en yoğun. Tehdit üç "
 "aşamalı: bilme (لَسَوْفَ تَعْلَمُونَ *(yakında bileceksiniz)*), kesme (لَأُقَطِّعَنَّ *(mutlaka "
 "keseceğim)*), asma (لَأُصَلِّبَنَّكُمْ *(mutlaka asacağım)*). Ve علم *(bilme; ilim)* kökü iki "
 "kez, iki yönde: عَلَّمَكُمُ ٱلسِّحْرَ *(size büyüyü öğretti)* ve تَعْلَمُونَ *(bileceksiniz)* — "
 "öğretme ve bilme aynı ayette karşı karşıya. Yedi xref üç ayete dağılıyor: 7:123, 7:124, 20:71."),
50: ("Cevap iki kelimeyle başlıyor ve biri hapaks: لَا ضَيْرَ *(zarar yok)*, ضير *(zarar verme)* "
 "korpusta TEK geçiş. **Ayet yıldızını İKİ kaynaktan alıyor** (rab z=2,72 ve hapaks z=3,38) — sûre "
 "25'te bu tek ayette görülmüştü (25:73), sûre 26'da ikinci. Ölçülebilir bir tehdit-cevap çifti: "
 "26:29'da Firavun ٱلْمَسْجُونِينَ *(zindana atılanlar)* tehdidi savurmuş, 26:49'da kesme ve asma "
 "eklemişti; cevap tehdidin içeriğine değil YÖNÜNE bakıyor — إِنَّآ إِلَىٰ رَبِّنَا مُنقَلِبُونَ "
 "*(biz Rabbimize dönenleriz)*. قلب *(kalp; çevrilme, dönme)* korpusta 168 geçişli ve buradaki "
 "lemma bab VII."),
51: ("Umut bir bağışlanma isteği ve gerekçesi bir öncelik: أَن كُنَّآ أَوَّلَ ٱلْمُؤْمِنِينَ *(ilk "
 "iman edenler olduğumuz için)*. أول *(ilk, evvel)* 26:26'da ٱلْأَوَّلِينَ *(öncekiler)* olarak "
 "atalar içindi, burada أَوَّلَ *(ilk)* olarak öncülük — aynı kök, geçmişten öne. Ölçülebilir bir "
 "şahıs yoğunluğu: on bir kelimede 1P yedi kez, blokta en yüksek. Ve fâsıla ٱلْمُؤْمِنِينَ esmâ "
 "sayılmış: sûrenin on beş مُؤْمِن artefaktının üçüncüsü. طمع *(tamah, umma)* korpusta 12 geçişli "
 "ve dikey ölçümü ▸önce korku bağlamı veriyor — korpusta 'korku ve umut' çifti sabit; burada korku "
 "YOK."),
52: ("Sahne değişiyor ve emir vahiyle geliyor: أَنْ أَسْرِ بِعِبَادِىٓ *(kullarımı geceleyin "
 "yürüt)*. سري *(gece yürüyüşü, isrâ)* korpusta 6 geçişli. Ölçülebilir bir çatı tersliği: تبع "
 "*(uyma, ardından gitme)* 26:40'ta kalabalığın büyücülere UYMA niyetiydi (etken), burada "
 "مُّتَّبَعُونَ *(izlenenler)* edilgen ism-i mef'ûl — aynı kök, ters çatı ve ters değer. Ve uyarı "
 "26:60'ta gerçekleşecek: فَأَتْبَعُوهُم *(ardlarına düştüler)*."),
53: ("Beş kelime ve sûrenin ikinci iltifâtı (yön 12>3). Ölçülebilir bir terkip tekrarı: 26:36'da "
 "ileri gelenler وَٱبْعَثْ فِى ٱلْمَدَآئِنِ حَٰشِرِينَ *(şehirlere toplayıcılar gönder)* diye "
 "ÖNERMİŞTİ; burada فَأَرْسَلَ فِرْعَوْنُ فِى ٱلْمَدَآئِنِ حَٰشِرِينَ *(Firavun şehirlere "
 "toplayıcılar gönderdi)* — öneri ve uygulama on yedi ayet arayla neredeyse aynı kelimelerle; "
 "değişen yalnız fiil kökü (بعث *(gönderme, diriltme)* → رسل *(gönderme, elçi)*) ve fâilin "
 "adlandırılması. Fâsıla da aynı: حَٰشِرِينَ *(toplayıcılar)*."),
54: ("Dört kelime, fiil yok, ve bir hapaks: شِرْذِمَةٌ *(döküntü topluluk)*, شرذم korpusta TEK "
 "geçiş — yıldızın tek kaynağı. Ölçülebilir bir küçültme: hem hapaks bir nitelemeyle hem açık bir "
 "sayı sözcüğüyle (قَلِيلُونَ *(azınlık)*). Ve ayet 26:54-56 üçlüsünün ilki: üç ayet de kısa (n=4, "
 "3, 3), üçü de إِنَّ *(gerçekten)* ile açılıyor ve üçü de Firavun'un kendi kavmine seslenişi — "
 "okumada ilk kez üç ardışık ayet aynı yapısal kalıpla diziliyor."),
55: ("Üç kelime, fiil yok, tek kök: غيظ *(öfke, gayz)*. Korpusta 11 geçişli ve 25:12'de de vardı — "
 "orada تَغَيُّظا *(öfkeli kaynama)* ateşin hâliydi, burada لَغَآئِظُونَ *(öfkelendirenler)* bir "
 "topluluğun eylemi; aynı kök, bir yerde özne cansız bir yerde insan. Dikey ölçüm bu kök için "
 "▸sonra نيل *(erişme, nail olma)* x157,1 veriyor — kökün korpusta dar bir yatağı var."),
56: ("Üç kelime, fiil yok. جمع *(toplama, cem)* sûrede dördüncü kez ve dördüncü öznesiyle: 26:38'de "
 "büyücüler toplandı (edilgen), 26:39'da halka 'toplanıyor musunuz' dendi (etken ism-i fâil), "
 "26:49'da أَجْمَعِينَ *(hepiniz)* tehdit kapsamıydı, burada جَمِيعٌ *(toplu, bir arada)* kendini "
 "tanımlama. Ölçülebilir: aynı kök dört ayette dört ayrı işlev. Ve حذر *(sakınma, tedbir)* korpusta "
 "21 geçişli; ism-i fâil çoğulu fâsılada."),
57: ("Çıkarma fiili taraf değiştiriyor: 26:35'te Firavun'un ileri gelenleri Mûsâ'yı يُرِيدُ أَن "
 "يُخْرِجَكُم مِّنْ أَرْضِكُم *(sizi yurdunuzdan çıkarmak istiyor)* diye suçlamıştı; burada "
 "فَأَخْرَجْنَٰهُم مِّن جَنَّٰتٍ وَعُيُونٍ *(onları bahçelerden ve pınarlardan çıkardık)* — aynı "
 "kök خرج *(çıkma, çıkarma)* bab IV, fâil 1P. Suçlama gerçekleşiyor ama fâili başkası. NOT: "
 "جَنَّٰت *(bahçeler)* burada aktör tablosuna GİRMİYOR, oysa 25:24'te جَنَّة girmişti — tablo "
 "tutarsız (aday 462)."),
58: ("Üç kelime ve üçü de mecrur — blokta en yoğun GEN. Ölçülebilir bir konum halkası: 26:42'de "
 "büyücülere ٱلْمُقَرَّبِينَ *(yakınlaştırılanlar)* konumu vaat edilmişti, burada kaybedilen "
 "مَقَامٍ كَرِيمٍ *(değerli bir konum)*. İki ayrı kök (قرب *(yakınlık, yaklaşma)* ve قوم *(kalkma; "
 "kavim; kıyamet)*) aynı konum alanında — 26:16↔26:18'deki ربب/ربو çiftiyle aynı desen (aday 613). "
 "Ve fâsıladaki كَرِيم esmâ sayılmış, oysa gönderge bir makam: sûrenin üçüncü كَرِيم artefaktı."),
59: ("Dört kelime ve sûrenin ÜÇÜNCÜ kafiye kırılması — yine إِسْرَٰٓءِيلَ *(İsrâîl)*. Ölçülebilir "
 "bir düzen: sûrenin dört kırılmasından üçü (26:17, 26:22, 26:59) aynı özel adla; dördüncüsü "
 "26:197'de ve okunmadı. **Aday 612 güçlendi: kırılma adın ses yapısına bağlı ve tek bir ad "
 "sûrenin kırılmalarının çoğunu üretiyor.** ورث *(miras, vâris olma)* korpusta 35 geçişli; kökün "
 "burada bab IV lemması, yani miras BIRAKMA değil miras KILMA."),
60: ("İki kelime — sûrenin okunan en kısa ayetlerinden ve okumada görülen en düşük n z (-1,11). "
 "Ölçülebilir bir gerçekleşme: 26:52'de إِنَّكُم مُّتَّبَعُونَ *(izleneceksiniz)* uyarısı "
 "verilmişti; burada فَأَتْبَعُوهُم *(ardlarına düştüler)* — aynı kök تبع *(uyma, ardından gitme)*, "
 "edilgen uyarıdan etken gerçekleşmeye. Ve شرق *(doğu; doğuş)* 26:28'de bir KAPSAM terimiydi "
 "(رَبُّ ٱلْمَشْرِقِ *(doğunun Rabbi)*), burada bir ZAMAN belirteci (مُّشْرِقِينَ *(gün doğarken)*) — "
 "aynı kök, kapsamdan zamana."),
}

ATLAMA = {
 "_mercek_26_46_48": ("26:46, 26:47, 26:48 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. **OKUMADA İLK KEZ ÜÇ "
  "ARDIŞIK AYET ★★★ ALIYOR** (aday 624'te iki ardışıktı). Kaynaklar: 26:46 pas z=5,38 (n=3, tek fiil "
  "edilgen, oran 1,00) · 26:47 rab z=5,01 (n=4, oran 0,25) · 26:48 rab z=6,78 (n=3, oran 0,33). "
  "ÜÇÜNDE DE AYET ÜÇ-DÖRT KELİME. İçerikler: secdeye kapanma, iman ikrarı, Rabbin belirginleştirilmesi — "
  "ne canlı, ne gök cismi, ne ölçü, ne süreç. ADAY 602/624'ÜN EN GÜÇLÜ VAKASI: kısa ayet kümelenmesi "
  "★★★ yığını üretiyor."),
 "_mercek_26_50": ("26:50 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. قَالُوا۟ لَا ضَيْرَ إِنَّآ إِلَىٰ "
  "رَبِّنَا مُنقَلِبُونَ. **İKİ KAYNAKLI**: rab z=2,72 VE hapaks z=3,38 (ضير *(zarar verme)*, "
  "korpusta tek geçiş). Sûre 25'te yıldızı iki kaynaktan alan tek ayet vardı (25:73); bu ikincisi."),
 "_mercek_26_54": ("26:54 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. إِنَّ هَٰٓؤُلَآءِ لَشِرْذِمَةٌ "
  "قَلِيلُونَ. Tek kaynak hapaks z=3,38 (شرذم *(döküntü, azınlık topluluk (şirzime))*, korpusta tek "
  "geçiş). Dört kelime, fiil yok; içerik bir küçültme nitelemesi."),
 "_blok_notu_26_41_60": ("BLOK BİLANÇOSU: ★★★ 5 (26:46, 47, 48, 50, 54) · ★★ 0 · ★ 2 (26:51, 59) · "
  "13 ayet yıldızsız. KAYNAK DAĞILIMI: pas x1 · rab x2 · hapaks x1 · rab+hapaks x1 · rab x1 (★) · "
  "kafiye kırılması x1 (★) — HİÇBİRİ İÇERİKTEN. VE HİÇBİRİNDE ÇIPA YOK; blokta çıpa taşıyabilecek "
  "ayet YOK (bölüt tamamen anlatı ve diyalog). SÛRE 26'NIN OKUNAN 60 AYETİNDE: ★★★ 11, çıpası 0; "
  "çıpalı ayet 1 (26:7) ve yıldızsız. **BEŞ ★★★ AYETİN BEŞİNDE DE n<=7 ve DÖRDÜNDE n<=4** — aday "
  "583/602/624'ün kısa ayet yanlılığı burada en yoğun hâlinde."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(41, 61):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 60/227.** Devam: 26:61'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-60 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1782
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(41, 61):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
