# -*- coding: utf-8 -*-
"""blok_25_61_70.py — sûre 25 yedinci blok (25:61-70). عِبَادُ ٱلرَّحْمَٰنِ bölütü açılıyor."""
import json
DIK = json.load(open('blok_dikey_25_61_77.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
61: "Gökte burçlar var eden, orada bir kandil ve aydınlatan bir ay kılan ne yücedir.",
62: "Öğüt almak ya da şükretmek isteyen için geceyi ve gündüzü birbiri ardınca kılan odur.",
63: "Rahmân'ın kulları, yeryüzünde alçak gönüllülükle yürüyenlerdir; cahiller onlara laf attığında 'selâm' derler.",
64: "Ve Rablerine secde ederek, kıyamda durarak geceleyenlerdir.",
65: "Ve derler ki: Rabbimiz, cehennem azabını bizden çevir; onun azabı yakayı bırakmayan bir belâdır.",
66: "Orası ne kötü bir karargâh, ne kötü bir konaktır.",
67: "Ve harcadıklarında israf etmeyen, kısmayan; ikisi arasında dengede olanlardır.",
68: "Ve Allah ile beraber başka bir ilâha yalvarmayan, Allah'ın haram kıldığı canı haksız yere öldürmeyen, zina etmeyenlerdir. Kim bunu yaparsa bir cezaya çarpılır.",
69: "Kıyamet günü azabı katlanır ve orada aşağılanmış olarak ebedî kalır.",
70: "Ancak tövbe eden, iman eden ve sâlih amel işleyen başka; işte Allah onların kötülüklerini iyiliklere çevirir. Allah bağışlayandır, merhamet edendir.",
}

OLCUM = {
61: ("eksen: **lafız YOK · Rab YOK — gönderge ٱلَّذِى *(o ki)*** · esmâ yok · aktör yok — ٱلْقَمَر "
 "*(ay)* tabloya girmiyor · edim haber, kip işareti yok · şahıs 3MS x3 · 3FS x1, iltifât 0 · n=11 "
 "mora=71 harf=51 (n z=-0,15), fâsıla مُّنِيرا *(aydınlatan)* → ا, A sınıfı, ACC; **i'râb ACC 4 · "
 "GEN 1**; bab I x2 · VI x1; zaman PERF x3; **kök ikilemesi جعل *(kılma, var etme)* x2**; simetri "
 "[3,3,7,1]; dış düğüm 1 · yıldız ★ yok · kökler برك *(bereket)* · جعل *(kılma, var etme)* · سمو "
 "*(ad; gök)* · برج *(burç)* · سرج *(kandil, sirâc)* · قمر *(ay)* · نور *(nûr, ışık)* · bağ: xref "
 "جعل *(kıldı)* + سماء *(gök)* + بروج *(burçlar)* → **15:16**; **25:1 ve 25:10 ile تَبَارَكَ *(ne "
 "yücedir)* ÜÇLÜSÜ TAMAMLANDI — aday 528 KAPANIYOR**: üç geçişin sûre içindeki göreli konumu "
 "0,013 · 0,130 · 0,792 (elle, L1)"),
62: ("eksen: **lafız YOK · Rab YOK — gönderge وَهُوَ ٱلَّذِى *(o ki)*, sûrede dördüncü kez bu "
 "biçimle** (25:47, 48, 53, 62) · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "3MS x5 — ayette başka şahıs yok**, iltifât 0 · n=13 mora=62 harf=51 (n z=0,06), fâsıla شُكُورا "
 "*(şükür)* → ا, A sınıfı, ACC; **i'râb ACC 4**; bab I x1 · IV x2 · V x1; zaman PERF x3 · IMPF x1; "
 "**kök ikilemesi رود *(irade, isteme)* x2 — أَرَادَ … أَوْ أَرَادَ *(isteyen … ya da isteyen)*, "
 "iki seçenek aynı fiille**; simetri [3,7,11,1]; **dış düğüm 2** · yıldız ★ yok · kökler جعل "
 "*(kılma, var etme)* · ليل *(gece)* · نهر *(ırmak; gündüz)* · خلف *(ardıl, halef; arka)* · رود "
 "*(irade, isteme)* · ذكر *(anma, zikir)* · شكر *(şükür)* · bağ: xref جعل *(kıldı)* + ليل *(gece)* + "
 "نهار *(gündüz)* → **17:12 · 28:73**; **25:47 ile gece-gündüz ikinci geçişi** — orada üç öğe üç "
 "sıfatla (giysi/dinlenme/kalkış), burada iki öğe TEK sıfatla: خِلْفَة *(birbiri ardınca)* "
 "(elle, L1, aday 581)"),
63: ("eksen: **lafız YOK · Rab YOK** · **esmâ İKİ TOKEN: رَحْمٰن *(rahmân)* 2. sırada ORTA + سَلام "
 "*(esenlik)* 12. sırada = fâsıla, MÜHÜRSÜZ**. رَحْمٰن: **SÛRENİN BEŞİNCİ VE SON رَحْمٰن'I — ADAY "
 "578 KAPANIYOR**; burada عِبَادُ ٱلرَّحْمَٰنِ *(Rahmân'ın kulları)* tamlamasında MUZÂFUN İLEYH, "
 "yani yine GÖNDERGE, sıfat değil. سَلام: **ÖLÇÜM ARTEFAKTI (aday 546/555)** — قَالُوا۟ سَلَٰما "
 "*(selâm derler)*, yani KULLARIN SÖYLEDİĞİ SÖZ; ilâhî gönderge yok · aktör yok · edim haber, kip "
 "işareti yok · şahıs 3MP x5 · 3MS x1, iltifât 0 · n=12 mora=76 harf=62 (n z=-0,04), fâsıla سَلَٰما "
 "*(selâm)* → ا, A sınıfı, ACC; i'râb NOM 2 · GEN 2 · ACC 2; bab I x2 · III x1; zaman IMPF x1 · "
 "PERF x2; dış düğüm 0 · yıldız ★ yok · kökler عبد *(kul, kulluk)* · رحم *(rahmet, merhamet)* · "
 "مشي *(yürüme)* · أرض *(yer, yeryüzü)* · هون *(hafiflik; alçak gönüllülük; aşağılama)* · خطب "
 "*(hitap, söz atma)* · جهل *(cahillik)* · قول *(söz söyleme)* · سلم *(selâmet, esenlik)* · bağ: "
 "**25:7 ve 25:20 ile مشي *(yürüme)* üçüncü geçişi** — orada elçinin çarşılarda yürümesi bir "
 "İTİRAZ konusuydu, burada kulların yeryüzünde yürüyüşü bir ÖVGÜ konusu (elle, L1, aday 582)"),
64: ("eksen: **lafız YOK · رَبّ *(Rab)* 3. sırada — sûrenin onuncu Rab'bi**, **rab z=3,94: OKUMADA "
 "GÖRÜLEN EN YÜKSEK RAB Z'Sİ ve yıldızın TEK kaynağı** (beş kelimede bir Rab, oran 0,20) · esmâ "
 "yok · aktör yok · edim haber, kip işareti yok · şahıs 3MP x3, iltifât 0 · n=5 mora=37 harf=28 — "
 "**25:46 ve 25:56 ile birlikte sûrenin en kısa ayetlerinden** (n z=-0,79), fâsıla وَقِيَٰما "
 "*(kıyam, ayakta durma)* → ا, A sınıfı, ACC; **i'râb ACC 2 · GEN 1**; bab I x1; zaman IMPF x1; "
 "dış düğüm 0 · **yıldız ★★★ — SÛRENİN DÖRDÜNCÜ ÜÇ YILDIZLISI** · kökler بيت *(ev; geceleme)* · "
 "ربب *(rab, terbiye etme)* · سجد *(secde)* · قوم *(kalkma; kavim; kıyamet)* · bağ: **25:60 ile "
 "سجد *(secde)* karşıtlığı** — orada secde emri REDDEDİLİYOR (وَمَا ٱلرَّحْمَٰنُ *(Rahmân da ne)*), "
 "burada secde geceyi dolduran hâl (elle, L1, aday 583)"),
65: ("eksen: **lafız YOK · رَبّ *(Rab)* 3. sırada — on birinci Rab** (rab z=1,62: **yıldızın TEK "
 "kaynağı**) · esmâ yok · **aktör: adlı جَهَنَّم *(cehennem)* 7. sırada, rol mecrur** · edim emir, "
 "kip IMPV 1 · şahıs 3MP x2 · 1P x2 · 2MS x1 · 3FS x1 · 3MS x1, iltifât 0 · n=11 mora=64 harf=48 "
 "(n z=-0,15), fâsıla غَرَاما *(yakayı bırakmayan belâ)* → ا, A sınıfı, ACC; **i'râb ACC 5 · GEN 1**; "
 "bab I x3; zaman IMPF x1 · IMPV 1 · PERF x1; **kök ikilemesi عذب *(azap)* x2**; simetri [3,5,8,1]; "
 "dış düğüm 0 · **yıldız ★** · kökler قول *(söz söyleme)* · ربب *(rab, terbiye etme)* · صرف "
 "*(çevirme, türlü türlü açıklama)* · عذب *(azap)* · كون *(olmak; mekân, yer)* · غرم *(borç; yakayı "
 "bırakmayan azap (garâm))* · bağ: **25:19 ve 25:50 ile صرف *(çevirme)* ÜÇÜNCÜ geçişi** — 25:19'da "
 "'azabı çevirmeye güç yetiremezsiniz' (olumsuz haber), burada aynı fiil EMİR ve DUA olarak "
 "(ٱصْرِفْ عَنَّا عَذَابَ جَهَنَّمَ *(cehennem azabını bizden çevir)*): aynı kök, aynı nesne, ters "
 "kip (elle, L1, aday 584)"),
66: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3FS x2, iltifât 0 · n=4 mora=31 harf=22 — **SÛRENİN EN KISA AYETİ** (n z=-0,89), fâsıla "
 "وَمُقَاما *(konak, ikamet yeri)* → ا, A sınıfı, ACC; **i'râb ACC 3 — dört kelimenin üçü mansûb**; "
 "bab I x1; zaman PERF x1; dış düğüm 0 · yıldız ★ yok · kökler سوأ *(kötülük)* · قرر *(karar kılma, "
 "yerleşme)* · قوم *(kalkma; kavim; kıyamet)* · bağ: **25:24 ile TAM KARŞITLIK** — orada خَيْرٌۭ "
 "مُّسْتَقَرًّۭا وَأَحْسَنُ مَقِيلا *(kalınacak yer bakımından daha hayırlı, dinlenilecek yer "
 "bakımından daha güzel)*, burada سَآءَتْ مُسْتَقَرًّۭا وَمُقَاما *(ne kötü bir karargâh ve konak)*; "
 "**ortak kök قرر *(karar kılma, yerleşme)* ve aynı iki-terimli yapı** (elle, L1, aday 585)"),
67: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 2 · şahıs 3MP x6 · "
 "3MS x1, iltifât 0 · n=11 mora=57 harf=51 (n z=-0,15), fâsıla قَوَاما *(denge, kıvam)* → ا, A "
 "sınıfı, ACC; i'râb ACC 2; bab I x2 · IV x2; zaman PERF x2 · IMPF x2; dış düğüm 0 · yıldız ★ yok · "
 "kökler نفق *(infak, harcama)* · سرف *(israf, aşırılık)* · قتر *(kısma, sıkı tutma (katr))* · كون "
 "*(olmak; mekân, yer)* · بين *(arası; açıklama)* · قوم *(kalkma; kavim; kıyamet)* · bağ: **قوم "
 "*(kalkma; kavim; kıyamet)* kökü 25:64, 25:66, 25:67, 25:69'da DÖRT AYRI LEMMAYLA** — قِيَام "
 "*(kıyam)*, مُقَام *(konak)*, قَوَام *(denge)*, قِيَامَة *(kıyamet)*; dördü de fâsıla ya da "
 "fâsılaya bitişik (elle, L1, aday 586)"),
68: ("eksen: **ALLAH LAFZI İKİ TOKEN — 5. ve 13. sırada; sûrenin dördüncü ve beşinci lafzı** "
 "(allah z=1,29) · Rab yok · esmâ yok · aktör yok · edim haber, kip NEG 3 · RES 1 · şahıs 3MP x6 · "
 "3MS x3, iltifât 0 · n=22 mora=112 harf=88 — **sûrenin en uzun ayetlerinden, 25:3 ile eşit** "
 "(n z=1,02), fâsıla أَثَاما *(ceza, vebal)* → ا, A sınıfı, ACC; **i'râb ACC 5 · GEN 2 · NOM 1**; "
 "bab I x5 · II x1; zaman IMPF x5 · PERF x1; **kök ikilemesi أله *(ilâh; lafza-i celâl)* x3 — "
 "ÜÇ GEÇİŞ: ikisi lafız, biri sahte ilâh (إِلَٰها ءَاخَرَ *(başka bir ilâh)*); okumada bir ayette "
 "aynı kökün lafız ve sahte-ilâh olarak BİRLİKTE geçtiği ilk yer**; **biçim HASR**; simetri "
 "[3,2,14,1]; **dış düğüm 2** · yıldız ★ yok · kökler دعو *(çağırma, dua)* · أله *(ilâh; lafza-i "
 "celâl)* · أخر *(geciktirme, sonraya bırakma; diğer)* · قتل *(öldürme)* · نفس *(nefis, can)* · حرم "
 "*(haram, yasak)* · حقق *(hak, gerçeklik)* · زني *(zina)* · فعل *(yapma, işleme)* · لقي "
 "*(karşılaşma, kavuşma; atma)* · أثم *(günah, vebal)* · bağ: xref ÜÇ 3-gram (قتل *(öldürdü)* + "
 "نفس *(can)* + حرّم *(haram kıldı)* · نفس + حرّم + اللّه *(Allah)* · حرّم + اللّه + حقّ *(hak)*) → "
 "**üçü de 6:151 VE 17:33** (elle, L1, aday 587)"),
69: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "3MS x4 — ayette başka şahıs yok**, iltifât 0 · n=8 mora=41 harf=35 (n z=-0,47), fâsıla مُهَانا "
 "*(aşağılanmış)* → ا, A sınıfı, ACC; i'râb NOM 1 · ACC 2 · GEN 1; bab I x1 · III x1; zaman IMPF x2; "
 "**edilgen 1 — يُضَٰعَفْ *(katlanır)***, **pas z=2,52: yıldızın TEK kaynağı** (iki fiilden biri "
 "edilgen, oran 0,50); **dış düğüm 3 — blokta en yüksek** · **yıldız ★★** · kökler ضعف *(zayıflık; "
 "kat kat artırma)* · عذب *(azap)* · يوم *(gün)* · قوم *(kalkma; kavim; kıyamet)* · خلد *(ebedî "
 "kalma)* · هون *(hafiflik; alçak gönüllülük; aşağılama)* · bağ: xref عذاب *(azap)* + يوم *(gün)* + "
 "قيامة *(kıyamet)* → **5:36 · 39:24 · 39:47**; **25:63 ile هون *(hafiflik; alçak gönüllülük; "
 "aşağılama)* karşıtlığı** — orada هَوْنا *(alçak gönüllülükle)* ÖVGÜ, burada مُهَانا *(aşağılanmış)* "
 "CEZA: aynı kök, ters kutup, altı ayet arayla (elle, L1, aday 588)"),
70: ("eksen: **ALLAH LAFZI İKİ TOKEN — 10. ve 14. sırada; sûrenin altıncı ve yedinci lafzı**, "
 "**allah z=1,97: yıldızın TEK kaynağı** · Rab yok · **esmâ غَفُور *(bağışlayan)* 15. + رَحِيم "
 "*(merhamet eden)* 16. sırada = fâsıla — MÜHÜR; GEÇERLİ; SÛRENİN İKİNCİ VE SON MÜHRÜ ve 25:6 ile "
 "AYNI ÇİFT** · aktör yok · edim haber, kip RES 1 · şahıs 3MS x5 · 3MP x1, iltifât 0 · n=16 mora=97 "
 "harf=75 (n z=0,38), fâsıla رَّحِيما *(merhamet eden)* → ا, A sınıfı, ACC — **25:6'nın fâsılasıyla "
 "AYNI KELİME**; i'râb ACC 4 · NOM 2 · GEN 2; bab I x3 · II x1 · IV x1; zaman PERF x4 · IMPF x1; "
 "**kök ikilemesi عمل *(iş, amel)* x2 · أله *(ilâh; lafza-i celâl)* x2 — ikisi de lafız**; **biçim "
 "HASR**; dış düğüm 1 · **yıldız ★** · kökler توب *(tövbe, dönüş)* · أمن *(güven, iman)* · عمل "
 "*(iş, amel)* · صلح *(salâh, iyilik)* · بدل *(değiştirme, bedel)* · أله *(ilâh; lafza-i celâl)* · "
 "سوأ *(kötülük)* · حسن *(güzellik, iyilik)* · كون *(olmak; mekân, yer)* · غفر *(bağışlama, "
 "mağfiret)* · رحم *(rahmet, merhamet)* · bağ: xref عمل *(işledi)* + عمل *(amel)* + صالح *(sâlih)* → "
 "**18:110**; **25:6 ile SÛRE HALKASI** — sûrenin iki mührü aynı çift (غَفُور|رَحِيم) ve aynı "
 "fâsıla; 25:6 sûrenin ilk cevabı, 25:70 son bölütün istisnası (elle, L1, aday 589)"),
}

MERCEK = {
61: ("Sûrenin açılış fiili üçüncü ve son kez: تَبَارَكَ *(ne yücedir)*, برك *(bereket)* kökü bab VI "
 "PERF, ve yine ٱلَّذِى *(o ki)* ile devam ediyor — 25:1, 25:10, 25:61. Aday 528'in üç noktalı "
 "dizisi tamamlandı; göreli konumlar 0,013 · 0,130 · 0,792. Ölçülebilir bir ışık ayrımı: سِرَاجا "
 "*(kandil)* ve قَمَرا مُّنِيرا *(aydınlatan ay)* — biri سرج *(kandil, sirâc)* kökünden ve sıfatsız, "
 "öteki نور *(nûr, ışık)* kökünden bir sıfat taşıyor. Metin iki gök cismini iki farklı kökle "
 "adlandırıyor. سرج korpusta 4 geçişli ve dikey ölçümü ▸önce ay x272,5 veriyor — çift korpusta "
 "sabit. برج *(burç)* korpusta 4 geçişli. SINIR: ayet iki cismi ADLANDIRIYOR ve birine bir ışık "
 "sıfatı veriyor, ama ne ışığın kaynağı ne yörünge ne ölçü hakkında bir şey söylüyor; buradan bir "
 "astronomi okuması çıkarmak yasaklı 'bilimsel izdüşüm' olurdu."),
62: ("Gece ve gündüz sûrede ikinci kez birlikte, ama yapı değişmiş: 25:47'de üç öğe üç ayrı sıfat "
 "alıyordu (gece giysi, uyku dinlenme, gündüz kalkış), burada iki öğe TEK sıfat alıyor: خِلْفَة "
 "*(birbiri ardınca)*, خلف *(ardıl, halef; arka)* kökü. Ölçülebilir bir sadeleşme: üç eşleşmeden "
 "bir bağıntıya. Ve amaç iki seçenekle veriliyor, ikisi de AYNI FİİLLE: لِّمَنْ أَرَادَ أَن "
 "يَذَّكَّرَ أَوْ أَرَادَ شُكُورا *(öğüt almak isteyen ya da şükretmek isteyen için)* — رود *(irade, "
 "isteme)* iki kez, ikisi de mâzi, aralarında yalnız أَوْ *(ya da)*. شكر *(şükür)* korpusta 75 "
 "geçişli ve dikey ölçümü ▸önce sabır bağlamı veriyor; burada o bağlam yok, zikirle eşleşiyor."),
63: ("Sûrenin beşinci ve son رَحْمٰن *(rahmân)*'ı burada ve yine gönderge konumunda: عِبَادُ "
 "ٱلرَّحْمَٰنِ *(Rahmân'ın kulları)* — muzâfun ileyh, sıfat değil. Aday 578'in beş tokeni tamamlandı "
 "ve beşi de sıfat-esmâ değil gönderge/özel ad kullanımı. Ölçülebilir bir yürüyüş karşıtlığı: مشي "
 "*(yürüme)* sûrede üçüncü kez — 25:7 ve 25:20'de elçinin çarşılarda yürümesi bir İTİRAZ konusuydu, "
 "burada kulların yeryüzünde yürüyüşü bir ÖVGÜ konusu; aynı kök, ters değer. هون *(hafiflik; alçak "
 "gönüllülük; aşağılama)* korpusta 26 geçişli ve iki kutuplu; burada olumlu kutupta, 25:69'da "
 "olumsuz kutupta olacak. Ve fâsıla سَلَٰما *(selâm)* esmâ sayılmış, oysa kulların söylediği söz."),
64: ("Beş kelime ve okumada görülen en yüksek رَبّ *(Rab)* z'si: 3,94. Sebebi ölçülebilir — ayet "
 "kısa (n=5) ve içinde tek Rab var, oran 0,20; z, Rab SAYISINI değil ORANINI ölçüyor. Yıldızın tek "
 "kaynağı bu. Ölçülebilir bir hâl çifti: سُجَّدا وَقِيَٰما *(secde ederek ve kıyamda durarak)* — "
 "ikisi de çoğul hâl, ikisi de mansûb, ve ikisi birbirinin karşıtı konumda (yere kapanma / ayakta "
 "durma). بيت *(ev; geceleme)* kökü burada FİİL (يَبِيتُونَ *(geceleri geçirirler)*) ve korpusta bu "
 "lemma seyrek; kökün 73 geçişinin çoğu 'ev' anlamında — kök düzeyi dikey komşuluk bu ayrımı "
 "yapmıyor (aday 529 sınıfı). Ve secde 25:60'ın karşıtı: orada secde emri reddediliyordu."),
65: ("Dua bir emir kipiyle kuruluyor ve fiil sûrede üçüncü kez: ٱصْرِفْ *(çevir)*, صرف *(çevirme, "
 "türlü türlü açıklama)*. Ölçülebilir bir kip tersliği: 25:19'da فَمَا تَسْتَطِيعُونَ صَرْفا "
 "*(çevirmeye güç yetiremezsiniz)* olumsuz haberdi, 25:50'de صَرَّفْنَٰهُ *(türlü türlü açıkladık)* "
 "başka anlamdı, burada aynı kök EMİR ve DUA. Aynı nesne (azap) ve ters kip. عذب *(azap)* iki kez "
 "ve ikisi de mansûb-mecrur tamlamada. Kapanış tek kelime ve seyrek: غَرَاما *(yakayı bırakmayan "
 "belâ)*, غرم *(borç; yakayı bırakmayan azap (garâm))* korpusta 6 geçişli ve dikey ölçümü eşiği "
 "aşan komşu vermiyor."),
66: ("Dört kelime — sûrenin en kısa ayeti (n z=-0,89), ve üçü mansûb. Ölçülebilir bir tam "
 "karşıtlık: 25:24 خَيْرٌۭ مُّسْتَقَرًّۭا وَأَحْسَنُ مَقِيلا *(kalınacak yer bakımından daha "
 "hayırlı, dinlenilecek yer bakımından daha güzel)*, burada سَآءَتْ مُسْتَقَرًّۭا وَمُقَاما *(ne "
 "kötü bir karargâh ve konak)*. Ortak kök قرر *(karar kılma, yerleşme)* ve aynı iki-terimli yapı; "
 "değişen kutup ve ikinci terim (مَقِيل *(öğle dinlenme yeri)* → مُقَام *(konak)*). Bu, 25:24 ↔ "
 "25:34 karşıtlığından sonra sûrenin İKİNCİ 'aynı kalıp, ters kutup' çifti."),
67: ("İki olumsuzlama ve bir orta terim: لَمْ يُسْرِفُوا۟ *(israf etmediler)*, وَلَمْ يَقْتُرُوا۟ "
 "*(kısmadılar)*, وَكَانَ بَيْنَ ذَٰلِكَ قَوَاما *(ikisi arasında denge)*. Ölçülebilir bir "
 "üçlü yapı: iki uç ve bir orta, ve orta terim fâsıla. سرف *(israf, aşırılık)* korpusta 23 geçişli, "
 "قتر *(kısma, sıkı tutma (katr))* 3 geçişli — biri sık biri seyrek, ve burada karşıt çift olarak "
 "kullanılıyorlar; قتر'ın üç geçişinden biri bu. Ve قوم *(kalkma; kavim; kıyamet)* kökü blokta "
 "dördüncü lemmasını veriyor: قِيَام *(kıyam, 25:64)*, مُقَام *(konak, 25:66)*, قَوَام *(denge, "
 "burada)*, قِيَامَة *(kıyamet, 25:69)* — dört ayette dört ayrı anlam, dördü de fâsıla ya da ona "
 "bitişik konumda."),
68: ("Yirmi iki kelime ve üç yasak: şirk, adam öldürme, zina. Ölçülebilir bir kök yoğunluğu: أله "
 "*(ilâh; lafza-i celâl)* ÜÇ kez ve iki farklı göndergeyle — ikisi lafız (مَعَ ٱللَّهِ *(Allah ile "
 "beraber)*, حَرَّمَ ٱللَّهُ *(Allah haram kıldı)*), biri sahte ilâh (إِلَٰها ءَاخَرَ *(başka bir "
 "ilâh)*). Okumada bir ayette aynı kökün lafız ve sahte-ilâh olarak birlikte geçtiği ilk yer; aday "
 "563'ün sınıflandırma sorusu burada tek ayette görünür hâle geliyor. İkinci yasak bir istisnayla "
 "sınırlanıyor (إِلَّا بِٱلْحَقِّ *(haksız yere olmaksızın)*, HASR) ve üç 3-gram'ı da aynı iki "
 "ayete bağlanıyor: 6:151 ve 17:33 — donmuş kalıp adayı (aday 437). زني *(zina)* korpusta 9 geçişli "
 "ve dikey ölçümü ▸önce şirk x20,6 veriyor; üçlü sıralama korpusta zaten bağlı."),
69: ("Yıldızın tek kaynağı tek bir edilgen fiil: يُضَٰعَفْ *(katlanır)*, ضعف *(zayıflık; kat kat "
 "artırma)* bab III — iki fiilden biri edilgen, oran 0,50, pas z=2,52. Ölçülebilir bir kök "
 "karşıtlığı: هون *(hafiflik; alçak gönüllülük; aşağılama)* sûrede ikinci kez ve ters kutupta — "
 "25:63'te هَوْنا *(alçak gönüllülükle)* övgüydü, burada مُهَانا *(aşağılanmış)* ceza. Altı ayet "
 "arayla aynı kök, ters değer; 25:7↔25:63'teki مشي *(yürüme)* karşıtlığıyla aynı sınıf. Ve dış "
 "düğüm 3 — blokta en yüksek; üç bağın kaynağı tek bir 3-gram (عذاب *(azap)* + يوم *(gün)* + "
 "قيامة *(kıyamet)*), yani terkip korpusta üç ayrı ayette."),
70: ("İstisna üç fiille kuruluyor ve üçü de mâzi: تَابَ *(tövbe etti)*, ءَامَنَ *(iman etti)*, "
 "عَمِلَ عَمَلا صَٰلِحا *(sâlih amel işledi)* — sonuncusu kök ikilemesi. Ölçülebilir bir dönüşüm: "
 "يُبَدِّلُ ٱللَّهُ سَيِّـَٔاتِهِمْ حَسَنَٰتٍ *(Allah kötülüklerini iyiliklere çevirir)*, بدل "
 "*(değiştirme, bedel)* bab II; سوأ *(kötülük)* ve حسن *(güzellik, iyilik)* aynı cümlede karşıt "
 "çift. Ve sûrenin iki mühründen ikincisi burada: غَفُور|رَحِيم *(gafûr | rahîm)*, 25:6'nın "
 "AYNISI ve fâsıla da aynı kelime. Sûre ilk cevabını (25:6) ve son bölütünün istisnasını (25:70) "
 "aynı iki adla kapatıyor. Allah lafzı da iki kez ve yıldızın tek kaynağı bu (allah z=1,97)."),
}

ATLAMA = {
 "_mercek_25_64": ("25:64 ★★★ — 🜁 BİYOLOG VE 🜂 UZAY MERCEKLERİ YAZILMADI, ÇIPA YOK. Ayet beş "
  "kelime: وَٱلَّذِينَ يَبِيتُونَ لِرَبِّهِمْ سُجَّدا وَقِيَٰما *(Rablerine secde ederek ve kıyamda "
  "durarak geceleyenler)*. İçerik tamamen ibadet hâli; ne canlı, ne organ, ne gök cismi, ne ölçü, "
  "ne süreç. Yıldızın kaynağı da içerik değil: TEK kaynak rab z=3,94 (beş kelimede bir Rab, oran "
  "0,20) — OKUMADA GÖRÜLEN EN YÜKSEK RAB Z'Sİ. 'Gece ibadetinin sirkadiyen ritmi' türünden bir "
  "okuma YASAKLI 'bilimsel izdüşüm' olurdu. ADAY 580'in dördüncü ★★★ vakası ve DÖRDÜ DE ÇIPASIZ."),
 "_blok_notu_25_61_70": ("BLOK BİLANÇOSU: bir ★★★ (25:64), bir ★★ (25:69), iki ★ (25:65, 25:70); "
  "altı ayet yıldızsız. **VE ADAY 580'İN SON KESKİN VAKASI 25:61'DE:** تَبَارَكَ ٱلَّذِى جَعَلَ فِى "
  "ٱلسَّمَآءِ بُرُوجا وَجَعَلَ فِيهَا سِرَٰجا وَقَمَرا مُّنِيرا — sûrenin en açık gök-cismi ayeti; "
  "iki cisim iki ayrı kökle adlandırılıyor (سرج *(kandil, sirâc)* / قمر *(ay)*) ve ikincisi bir ışık "
  "sıfatı alıyor (مُّنِير *(aydınlatan)*, نور *(nûr, ışık)* kökünden). **YILDIZ SIFIR.** Aynı blokta "
  "25:62 gece-gündüz bağıntısı (خِلْفَة *(birbiri ardınca)*) — yine yıldız sıfır. Sûre 25'in çıpa "
  "taşıyan ayet sayısı 9 → 11 (25:61 ve 25:62 eklendi) ve yıldız alan çıpalı ayet sayısı hâlâ 1 "
  "(25:25, ★★). SINIR NOTU: 25:61 iki gök cismini ADLANDIRIYOR ve birine bir ışık sıfatı veriyor, "
  "ama ne ışığın kaynağı, ne yörünge, ne ölçü hakkında bir şey söylüyor — buradan astronomi "
  "okuması çıkarmak yasaklı 'bilimsel izdüşüm'dür ve YAPILMADI."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(61, 71):
    OM['25']["25:%d" % n] = {"ar": AR[(25, n)], "meal": MEAL[n], "olcum": OLCUM[n],
                             "mercek": MERCEK[n], "dikey": DIK["25:%d" % n]}
OM['25']['_mercek_atlama_notu'].update(ATLAMA)
OM['25']['_blok_bolme_notu'] += (" BEŞİNCİ BÖLME: son blok 25:61-77 de ikiye bölündü (25:61-70 ve "
 "25:71-77). Gerekçe ölçüm: 25:70 sûrenin İKİNCİ VE SON MÜHRÜYLE (غَفُور|رَحِيم) kapanıyor ve bu "
 "mühür 25:6'nınkiyle aynı çift; 25:71 وَمَن تَابَ *(kim tövbe ederse)* ile istisnayı yeni bir "
 "cümlede sürdürüyor. Ayrıca 25:61-70 عِبَادُ ٱلرَّحْمَٰنِ *(Rahmân'ın kulları)* bölütünün açılışını "
 "ve sûrenin son رَحْمٰن tokenini birlikte taşıyor.")
OM['ilerleme']['not'] = ("Sûre 23 TAM (118/118). Sûre 24 TAM (64/64). **Sûre 25 (Furkān) 70/77.** "
                         "Devam: 25:71'den (son yedi ayet).")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "25": "1-70 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1715
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 25 →', len([k for k in OM['25'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(61, 71):
    MK['25']["25:%d" % n] = MERCEK[n]
MK['25_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 25 →', len(MK['25']))
