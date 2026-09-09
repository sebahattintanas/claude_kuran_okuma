# -*- coding: utf-8 -*-
"""blok_26_101_110.py — sûre 26 sekizinci blok (26:101-110). Nûh kıssası ve dört nakarat."""
import json
DIK = json.load(open('blok_dikey_26_101_110.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
101: "Ne de candan bir dostumuz.",
102: "Keşke bize bir dönüş olsa da müminlerden olsak.",
103: "Bunda elbette bir âyet var; ama onların çoğu inanmıyor.",
104: "Rabbin, elbette o Azîz'dir, Rahîm'dir.",
105: "Nûh'un kavmi de elçileri yalanladı.",
106: "Kardeşleri Nûh onlara demişti: Sakınmıyor musunuz?",
107: "Ben size güvenilir bir elçiyim.",
108: "Allah'tan sakının ve bana itaat edin.",
109: "Buna karşılık sizden bir ücret istemiyorum; benim ücretim ancak âlemlerin Rabbine aittir.",
110: "Allah'tan sakının ve bana itaat edin.",
}

O = {
101: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · **şahıs eki "
 "YOK, fiil YOK** · n=3 mora=18 harf=12 — **sûrenin okunan en kısa ayetlerinden ve blokta en kısası** "
 "(n z=-1,00), fâsıla حَمِيمٍ *(candan dost, hamîm)* → م, N sınıfı; **i'râb GEN 2**; dış düğüm 0 · "
 "yıldız ★ yok · kökler صدق *(doğruluk)* · حمم *(kaynar su, hamîm)* · bağ: **26:100 ile bitişik "
 "çift** — orada شَٰفِعِينَ *(şefaatçiler)*, burada صَدِيقٍ حَمِيمٍ *(candan dost)*; **ikisi de "
 "olumsuz, ikisi de فَمَا لَنَا / وَلَا yapısında, ikisi de fiilsiz**; **حمم *(kaynar su, hamîm)* — "
 "529 kümesine yeni vaka**: kök korpusta 21 geçişli ve dikey ölçümü ▸sonra جحم *(alevli ateş, "
 "cahîm)* x39,2 veriyor, yani ağırlıkla 'kaynar su' anlamında; burada 'candan dost' (elle, L1, "
 "aday 677)"),
102: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُؤْمِن *(mümin)* 7. sırada = fâsıla, MÜHÜRSÜZ — "
 "ARTEFAKT, sûrenin beşinci مُؤْمِن tokeni** (aday 601) · aktör yok · edim şart, kip COND 1 · **şahıs "
 "1P x2 — ayette başka şahıs yok**, iltifât 0 · n=7 mora=34 harf=27 (n z=-0,58), fâsıla "
 "ٱلْمُؤْمِنِينَ → ن, N sınıfı; i'râb ACC 2 · GEN 1; bab I x1; zaman IMPF x1; dış düğüm 0 · yıldız "
 "★ yok · kökler كرر *(dönüş, kere (kerre))* · كون *(olmak; mekân, yer)* · أمن *(güven; iman)* · "
 "bağ: **كرر *(dönüş, kere (kerre))* korpusta ALTI geçişli ve dikey ölçümü hiçbir komşu vermiyor — "
 "kökün korpusta yatağı yok**; 26:99-102 dörtlüsü mahşerdeki pişmanlık sözünün kapanışı "
 "(elle, L1, aday 678)"),
103: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُؤْمِن = fâsıla — ARTEFAKT, altıncı token** · aktör "
 "yok · edim haber, kip EMPH 1 · NEG 1 · şahıs 3MS x1 · 3MP x1, **iltifât 1 — yön 1>3; sûrenin "
 "altıncı iltifâtı** · n=8 mora=40 harf=32 (n z=-0,47), fâsıla مُّؤْمِنِينَ → ن, N sınıfı; i'râb "
 "ACC 3 · NOM 1; bab I x1; zaman PERF x1; **açık sayı sözcüğü: كثر *(çokluk)* → أَكْثَر *(çoğu)*** ; "
 "**NAKARAT alanı = 6, temsil ayet 26:8**; **esit: 26:8, 67, 121, 174, 190 ile TAM AYET ÖZDEŞ** · "
 "dış düğüm 0 · yıldız ★ yok · kökler أيي *(âyet, işaret)* · كون *(olmak; mekân, yer)* · كثر "
 "*(çokluk)* · أمن *(güven; iman)* · bağ: **birinci nakaratın ÜÇÜNCÜ geçişi** (26:8, 67, 103); "
 "**26:67'de de iltifât 1>3 vardı — nakaratın iltifât yönü SABİT** (elle, L1, aday 679)"),
104: ("eksen: **lafız YOK · رَبّ *(Rab)* 2. sırada — yirminci Rab**, **rab z=3,94: yıldızın TEK "
 "kaynağı** (n=5, oran 0,20) · **esmâ عَزِيز *(azîz)* 4. + رَحِيم *(rahîm)* 5. sırada = fâsıla — "
 "MÜHÜR; GEÇERLİ; sûrenin on mühründen üçüncüsü** · aktör yok · edim haber, kip EMPH 1 · şahıs "
 "2MS x1 · 3MS x1, iltifât 0 · n=5 mora=28 harf=21 (n z=-0,79), fâsıla ٱلرَّحِيمُ → م, N sınıfı; "
 "**i'râb ACC 2 · NOM 2; fiil YOK**; **NAKARAT alanı = 8, temsil ayet 26:9**; **esit: 26:9, 68, 122, "
 "140, 159, 175, 191 ile TAM AYET ÖZDEŞ** · dış düğüm 0 · **yıldız ★★★** · kökler ربب *(rab, "
 "terbiye etme)* · عزز *(izzet, üstünlük)* · رحم *(rahmet, merhamet)* · bağ: **ikinci nakaratın "
 "ÜÇÜNCÜ geçişi; 26:103-104 ikilisi 26:8-9 ve 26:67-68 ikililerinin birebir tekrarı** "
 "(elle, L1, aday 679)"),
105: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı نُوح *(Nûh)* 3. sırada, rol "
 "mecrur — SÛRENİN ÜÇÜNCÜ KISSASI AÇILIYOR** · edim haber, kip işareti yok · **şahıs 3FS x1 — "
 "ayette başka şahıs yok**, iltifât 0 · n=4 mora=24 harf=18 (n z=-0,89), fâsıla ٱلْمُرْسَلِينَ "
 "*(gönderilenler)* → ن, N sınıfı; i'râb NOM 1 · GEN 1 · ACC 1; bab II x1; zaman PERF 1; dış düğüm "
 "0 · yıldız ★ yok · kökler كذب *(yalan; yalanlama)* · قوم *(kalkma; kavim; kıyamet)* · رسل "
 "*(gönderme, elçi)* · bağ: **25:37 ile Nûh kıssası karşılaştırması** — orada tek ayette كَذَّبُوا۟ "
 "ٱلرُّسُلَ *(elçileri yalanladılar)* + boğulma + ibret + azap, burada aynı tekzip cümlesi bir "
 "kıssanın AÇILIŞI; **aynı formül, biri kapanış biri açılış** (elle, L1, aday 680)"),
106: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı نُوح *(Nûh)* 5. sırada, rol FAİL** · "
 "edim soru, kip INTG 1 · NEG 1 · şahıs 3MS x1 · 3MP x2 · 2MP x2, iltifât 0 · n=7 mora=33 harf=24 "
 "(n z=-0,58), fâsıla تَتَّقُونَ *(sakınmıyor musunuz)* → ن, N sınıfı; **i'râb NOM 2**; bab I x1 · "
 "VIII x1; zaman PERF 1 · IMPF 1; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · أخو "
 "*(kardeş)* · وقي *(sakınma, koruma)* · bağ: **26:11 ile أَلَا يَتَّقُونَ / أَلَا تَتَّقُونَ "
 "karşılaştırması** — orada 3MP ve Firavun'un kavmi için (anlatıcının sorusu), burada 2MP ve doğrudan "
 "muhataba; **aynı kök, aynı soru, üçüncü şahıstan ikinci şahsa** (elle, L1, aday 681)"),
107: ("eksen: **lafız YOK · Rab YOK** · esmâ yok — **أَمِين *(güvenilir)* esmâ SAYILMIYOR ve bu "
 "DOĞRU** (gönderge elçi); ama sûrede aynı sınıftan on beş مُؤْمِن artefaktı var, yani tablo "
 "TUTARSIZ (aday 601/629) · aktör yok · edim haber, kip işareti yok · **şahıs eki YOK, fiil YOK** · "
 "n=4 mora=21 harf=15 (n z=-0,89), fâsıla أَمِينٌ *(güvenilir)* → ن, N sınıfı; **i'râb ACC 1 · "
 "NOM 2**; **NAKARAT alanı = 5**; **esit: 26:125, 143, 162, 178 ile TAM AYET ÖZDEŞ** · dış düğüm 0 · "
 "yıldız ★ yok · kökler رسل *(gönderme, elçi)* · أمن *(güven; iman)* · bağ: **sûrenin ÜÇÜNCÜ nakarat "
 "kümesinin ilk geçişi** (26:107, 125, 143, 162, 178 — beş ayet); **25:56 ile karşılaştırma** — "
 "orada elçi مُبَشِّرا وَنَذِيرا *(müjdeci ve uyarıcı)* olarak tanımlanıyordu, burada رَسُولٌ "
 "أَمِينٌ *(güvenilir elçi)* (elle, L1, aday 682)"),
108: ("eksen: **ALLAH LAFZI 2. sırada — sûrenin DÖRDÜNCÜ lafzı**, **allah z=6,14: OKUMADA GÖRÜLEN "
 "EN YÜKSEK ALLAH Z'Sİ ve yıldızın TEK kaynağı** (n=3, oran 0,33) · Rab yok · esmâ yok · aktör yok · "
 "edim emir, kip IMPV 2 · şahıs 2MP x4 · 1S x1, iltifât 0 · n=3 mora=23 harf=18 (n z=-1,00), fâsıla "
 "وَأَطِيعُونِ *(bana itaat edin)* → ن, N sınıfı; **i'râb ACC 1**; bab IV x1 · VIII x1; **zaman "
 "IMPV x2 — ayetin iki fiili de emir**; **NAKARAT alanı = 8**; **esit: 26:110, 126, 131, 144, 150, "
 "163, 179 ile TAM AYET ÖZDEŞ** · dış düğüm 0 · **yıldız ★★★** · kökler وقي *(sakınma, koruma)* · "
 "أله *(ilâh; lafza-i celâl)* · طوع *(güç yetirme, itaat)* · bağ: **SÛRENİN DÖRDÜNCÜ NAKARAT "
 "KÜMESİNİN İLK GEÇİŞİ ve SEKİZ AYETİN SEKİZİ DE ★★★** — aday 606'nın ikinci ve daha büyük vakası "
 "(elle, L1, aday 683)"),
109: ("eksen: **lafız YOK · رَبّ *(Rab)* 10. sırada — yirmi birinci Rab** (rab z=1,62: yıldızın TEK "
 "kaynağı) · esmâ yok · aktör yok · edim haber, kip NEG 2 · RES 1 · şahıs 1S x2 · 2MP x1 · 3MS x1, "
 "iltifât 0 · n=11 mora=50 harf=40 — **blokta en uzun ayet** (n z=-0,15), fâsıla ٱلْعَٰلَمِينَ "
 "*(âlemler)* → ن, N sınıfı; **i'râb GEN 3 · NOM 1**; bab I x1; zaman IMPF 1; **kök ikilemesi أجر "
 "*(ücret, karşılık)* x2 — soru ve cevap aynı kökle: مَآ أَسْـَٔلُكُمْ عَلَيْهِ مِنْ أَجْرٍ إِنْ "
 "أَجْرِىَ إِلَّا عَلَىٰ رَبِّ ٱلْعَٰلَمِينَ**; **biçim HASR**; simetri [4,1,6,1]; **NAKARAT alanı "
 "= 5**; **esit: 26:127, 145, 164, 180 ile TAM AYET ÖZDEŞ** · dış düğüm 0 · **yıldız ★** · kökler "
 "سأل *(isteme, dileme)* · أجر *(ücret, karşılık)* · ربب *(rab, terbiye etme)* · علم *(bilme; "
 "âlem)* · bağ: **ADAY 626 KAPANIYOR** — 25:57'de elçi مَآ أَسْـَٔلُكُمْ عَلَيْهِ مِنْ أَجْرٍ "
 "*(sizden ücret istemiyorum)* diyordu ve istisna bir EYLEMDİ (إِلَّا مَن شَآءَ أَن يَتَّخِذَ "
 "*(dileyen bir yol tutsun)*); burada aynı cümle ve istisna bir ADRES (عَلَىٰ رَبِّ ٱلْعَٰلَمِينَ); "
 "26:41'de büyücüler ücret İSTİYORDU. **Üç geçiş: reddetme (25:57) → isteme (26:41) → adres "
 "gösterme (26:109)** (elle, L1, aday 684)"),
110: ("eksen: **ALLAH LAFZI 2. sırada — sûrenin BEŞİNCİ lafzı**, **allah z=6,14: yıldızın TEK "
 "kaynağı**; 26:108 ile BİREBİR AYNI AYET · Rab yok · esmâ yok · aktör yok · edim emir, kip IMPV 2 · "
 "şahıs 2MP x4 · 1S x1, iltifât 0 · n=3 mora=23 harf=18 (n z=-1,00), fâsıla وَأَطِيعُونِ → ن, N "
 "sınıfı; **i'râb ACC 1**; bab IV x1 · VIII x1; zaman IMPV x2; **NAKARAT alanı = 8, temsil ayet "
 "26:108**; **esit: 26:108, 126, 131, 144, 150, 163, 179 ile TAM AYET ÖZDEŞ** · dış düğüm 0 · "
 "**yıldız ★★★** · kökler وقي *(sakınma, koruma)* · أله *(ilâh; lafza-i celâl)* · طوع *(güç "
 "yetirme, itaat)* · bağ: **26:108 ile İKİ AYET ARAYLA BİREBİR TEKRAR — nakarat kümesi içinde EN "
 "KISA aralık**; aradaki 26:109 da nakarat (dördüncü küme); **üç ardışık ayetin üçü de nakarat** "
 "(elle, L1, aday 683)"),
}

M = {
101: ("Üç kelime, fiil yok — blokta en kısa ayet. **26:100 ile bitişik çift**: orada فَمَا لَنَا مِن "
 "شَٰفِعِينَ *(bizim ne şefaatçilerimiz var)*, burada وَلَا صَدِيقٍ حَمِيمٍ *(ne de candan bir "
 "dostumuz)* — ikisi de olumsuz, ikisi de fiilsiz, ikisi de aynı yapının parçası. حمم *(kaynar su, "
 "hamîm)* korpusta 21 geçişli ve dikey ölçümü ▸önce sol x101,9 · شرب *(içme)* x34,8 · ▸sonra جحم "
 "*(alevli ateş, cahîm)* x39,2 veriyor — **kök korpusta ezici çoğunlukla 'kaynar su' anlamında**, "
 "burada 'candan dost' (aday 529 sınıfı). İlginç olan, kökün korpus komşuluğunun (cahîm) bu bölütün "
 "on ayet öncesindeki 26:91'de geçmiş olması."),
102: ("Pişmanlık bir gerçekleşmemiş dilekle kapanıyor: فَلَوْ أَنَّ لَنَا كَرَّةً *(keşke bize bir "
 "dönüş olsa)*. كرر *(dönüş, kere (kerre))* korpusta ALTI geçişli ve dikey ölçümü **hiçbir komşu "
 "vermiyor** — kökün korpusta bir yatağı yok. Ölçülebilir bir şahıs yoğunluğu: yedi kelimede 1P iki "
 "kez ve başka şahıs yok. Ve fâsıla ٱلْمُؤْمِنِينَ esmâ sayılmış — sûrenin on beş مُؤْمِن "
 "artefaktının beşincisi; ayrıca üç ayet sonra (26:103) altıncısı gelecek."),
103: ("Sûrenin birinci nakaratı **üçüncü** kez (26:8, 67, 103). Ölçülebilir bir sabitlik: 26:67'de "
 "de iltifât 1 ve yön 1>3'tü, burada da aynı — **nakaratın iltifât yönü sabit**, yani iltifât "
 "sayacı tekrarları da sayıyor. Bu, sûrenin 'iltifât 15' ölçümünün de nakarat tekrarlarını "
 "içerdiğini gösteriyor (aday 606 sınıfı: bağımsızlık ihlâli iltifât sayımına da yayılıyor). "
 "Nakarat alanı 6, temsil ayet 26:8; esit alanı beş ayeti gösteriyor."),
104: ("Sûrenin ikinci nakaratı üçüncü kez ve **26:103-104 ikilisi 26:8-9 ile 26:67-68 ikililerinin "
 "birebir tekrarı**. rab z=3,94 — üç ayette de aynı değer, çünkü üç ayet de aynı. Ölçülebilir bir "
 "mimari: nakarat çifti kıssanın önünde (26:8-9), Mûsâ kıssasının arkasında (26:67-68), İbrâhîm "
 "kıssasının arkasında (26:103-104). **Üç konum, aynı iki ayet.** Sûrenin on mühründen üçüncüsü ve "
 "mühür GEÇERLİ."),
105: ("Üçüncü kıssa açılıyor ve açılış biçimi öncekilerden farklı: Mûsâ nidâ ile (26:10), İbrâhîm "
 "emirle (26:69), Nûh **doğrudan bir tekzip cümlesiyle** — كَذَّبَتْ قَوْمُ نُوحٍ ٱلْمُرْسَلِينَ "
 "*(Nûh'un kavmi elçileri yalanladı)*. Ölçülebilir bir sayı uyumsuzluğu: قَوْم *(kavim)* tekil ama "
 "nesne ٱلْمُرْسَلِينَ *(gönderilenler)* çoğul — **bir kavim, çoğul elçi**; okumada üçüncü sayı "
 "uyumsuzluğu (26:16 رَسُول tekil+çoğul zamir, 26:77 عَدُوّ tekil+çoğul gönderge). Ve 25:37 ile "
 "karşılaştırma: orada aynı tekzip cümlesi bir kıssanın TAMAMIYDI (tek ayette tekzip + boğulma + "
 "ibret + azap), burada bir kıssanın AÇILIŞI."),
106: ("Nûh'un ilk sözü bir soru: أَلَا تَتَّقُونَ *(sakınmıyor musunuz)*. Ölçülebilir bir şahıs "
 "kayması: 26:11'de aynı kök ve aynı soru vardı — أَلَا يَتَّقُونَ *(sakınmıyorlar mı)*, ama 3MP ve "
 "Firavun'un kavmi için, anlatıcının ağzından; burada 2MP ve **doğrudan muhataba**. Aynı kök, aynı "
 "soru, üçüncü şahıstan ikinci şahsa. Ve أخو *(kardeş)* burada bir elçi-kavim ilişkisi bildiriyor "
 "(أَخُوهُمْ نُوحٌ *(kardeşleri Nûh)*); kök korpusta 96 geçişli ve dikey ölçümü ▸sonra Hûd x19,5 · "
 "Lût x15,2 veriyor — **korpusta zaten bu formüle bağlı**, yani terkip bu ayete özgü değil."),
107: ("Sûrenin **üçüncü nakarat kümesinin** ilk geçişi: إِنِّى لَكُمْ رَسُولٌ أَمِينٌ *(ben size "
 "güvenilir bir elçiyim)* — beş ayette birebir (26:107, 125, 143, 162, 178). Dört kelime, fiil yok. "
 "Ölçülebilir bir tablo tutarsızlığı: أَمِين *(güvenilir)* burada esmâ SAYILMIYOR ve bu **doğru** "
 "(gönderge elçi); ama sûrede aynı sınıftan on beş مُؤْمِن artefaktı var — **tablo bir yerde doğru, "
 "başka yerde yanlış** (aday 601/629 deseni). Ve 25:56 ile karşılaştırma: orada elçi مُبَشِّرا "
 "وَنَذِيرا *(müjdeci ve uyarıcı)* olarak tanımlanıyordu, burada رَسُولٌ أَمِينٌ."),
108: ("**Okumada görülen en yüksek Allah z'si: 6,14.** Sebebi ölçülebilir — ayet üç kelime ve içinde "
 "tek lafız, oran 0,33; z lafız SAYISINI değil ORANINI ölçüyor. Ve bu ayet sûrenin **dördüncü "
 "nakarat kümesinin** ilk geçişi: فَٱتَّقُوا۟ ٱللَّهَ وَأَطِيعُونِ *(Allah'tan sakının ve bana "
 "itaat edin)*, **sekiz ayette birebir** (26:108, 110, 126, 131, 144, 150, 163, 179). "
 "**SEKİZ AYETİN SEKİZİ DE ★★★ ve sekizinde de allah z=6,14.** Bu, aday 606'nın ikinci ve daha "
 "büyük vakası: sûrenin 41 ★★★ ayetinin 16'sı iki nakarattan geliyor."),
109: ("**Aday 626 kapanıyor.** أجر *(ücret, karşılık)* kök ikilemesiyle: soru ve cevap aynı kökle — "
 "مَآ أَسْـَٔلُكُمْ عَلَيْهِ مِنْ أَجْرٍ إِنْ أَجْرِىَ إِلَّا عَلَىٰ رَبِّ ٱلْعَٰلَمِينَ. Üç "
 "geçişlik bir dizi tamamlandı: 25:57 elçi ücreti **reddediyor** ve istisna bir EYLEM (dileyen bir "
 "yol tutsun); 26:41 büyücüler ücret **istiyor**; burada elçi ücreti reddedip **adres gösteriyor** "
 "(âlemlerin Rabbi). Dikey ölçüm أجر için ▸önce سأل *(isteme, dileme)* x13,2 · ▸sonra âlem x11,2 "
 "veriyor — **ayetin üç ana kökü de korpusta bu köke bağlı**, terkip donmuş kalıp adayı (aday 437). "
 "Blokta en uzun ayet ve simetri [4,1,6,1]."),
110: ("Dördüncü nakarat kümesinin ikinci geçişi ve **26:108 ile arada yalnız bir ayet var** — "
 "kümenin en kısa aralığı. Ve aradaki 26:109 da nakarat (üçüncü küme). **Üç ardışık ayetin üçü de "
 "nakarat**: 26:108 (dördüncü küme), 26:109 (beşinci küme), 26:110 (dördüncü küme yine). Ölçülebilir "
 "bir mimari: nakaratlar tek tek değil KÜME hâlinde diziliyor ve kıssa açılışlarında A-B-A örgüsü "
 "kuruyor. Bu örgü sûrenin kalan beş kıssasında da tekrarlanacak (26:125-127, 143-145, 162-164, "
 "178-180) — **okumada ilk kez bir sûrenin mimarisi önceden ölçülebilir hâle geliyor.**"),
}

ATLAMA = {
 "_mercek_26_104": ("26:104 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. Nakarat ayeti (26:9'un üçüncü "
  "geçişi). Tek kaynak rab z=3,94. 26:9 ve 26:68 ile AYNI AYET; bağımsız gözlem değil (aday 606)."),
 "_mercek_26_108_110": ("26:108 ve 26:110 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. İkisi de BİREBİR AYNI "
  "AYET (فَٱتَّقُوا۟ ٱللَّهَ وَأَطِيعُونِ) ve ikisinde de tek kaynak **allah z=6,14 — OKUMADA "
  "GÖRÜLEN EN YÜKSEK ALLAH Z'Sİ** (n=3, tek lafız, oran 0,33). Bu nakarat sûrede SEKİZ ayette "
  "birebir tekrarlanıyor ve **SEKİZİNİN SEKİZİ DE ★★★**. İçerik bir emir; ne canlı, ne gök cismi, "
  "ne ölçü, ne süreç."),
 "_blok_notu_26_101_110": ("BLOK BİLANÇOSU: ★★★ 3 (26:104, 108, 110) · ★★ 0 · ★ 1 (26:109) · 6 ayet "
  "yıldızsız. **ÜÇ ★★★ AYETİN ÜÇÜ DE NAKARAT** ve hiçbirinde çıpa yok. Kaynaklar: rab x1 · "
  "allah x2. SÛRE 26'NIN OKUNAN 110 AYETİNDE ★★★ 23; çıpası olan tek ★★★ hâlâ 26:63. "
  "**ADAY 606'NIN TAM ÖLÇÜMÜ BU BLOKTA YAPILDI: sûrenin 41 ★★★ ayetinin 16'sı iki nakarattan "
  "geliyor (عَزِيز|رَحِيم 8, فَٱتَّقُوا۟ ٱللَّهَ 8); bağımsız ★★★ sayısı 25, düzeltilmiş pay "
  "(41-14)/227 = %11,9** — makro profildeki %18,1 değil."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(101, 111):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 110/227.** Devam: 26:111'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-110 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1832
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(101, 111):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
