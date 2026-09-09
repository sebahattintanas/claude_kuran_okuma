# -*- coding: utf-8 -*-
"""blok_26_21_40.py — sûre 26 ikinci blok (26:21-40). رَبّ ٱلْعَٰلَمِينَ zinciri."""
import json
DIK = json.load(open('blok_dikey_26_21_40.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
21: "Sizden korkunca sizden kaçtım; sonra Rabbim bana hüküm bağışladı ve beni elçilerden kıldı.",
22: "Ve İsrâiloğullarını köleleştirmen — başıma kaktığın nimet bu mu?",
23: "Firavun dedi ki: Âlemlerin Rabbi de nedir?",
24: "Dedi: Göklerin, yerin ve ikisi arasındakilerin Rabbi — kesin olarak inanıyorsanız.",
25: "Çevresindekilere dedi: İşitmiyor musunuz?",
26: "Dedi: Sizin de Rabbiniz, önceki atalarınızın da Rabbi.",
27: "Dedi: Size gönderilen elçiniz gerçekten deli.",
28: "Dedi: Doğunun, batının ve ikisi arasındakilerin Rabbi — akıl ediyorsanız.",
29: "Dedi: Benden başka bir ilâh edinirsen, seni mutlaka zindana atılanlardan yaparım.",
30: "Dedi: Sana apaçık bir şey getirsem de mi?",
31: "Dedi: Doğru söyleyenlerdensen getir onu.",
32: "Asâsını attı; bir anda apaçık bir yılan oluverdi.",
33: "Elini çekip çıkardı; bakanlara bembeyaz göründü.",
34: "Çevresindeki ileri gelenlere dedi: Bu, bilgili bir büyücü.",
35: "Büyüsüyle sizi yurdunuzdan çıkarmak istiyor; ne buyurursunuz?",
36: "Dediler: Onu ve kardeşini beklet, şehirlere toplayıcılar gönder.",
37: "Bilgili her büyücüyü sana getirsinler.",
38: "Büyücüler belirlenmiş bir günün belirli vaktinde toplandı.",
39: "Halka dendi ki: Siz de toplanıyor musunuz?",
40: "Umarız, galip gelen onlar olursa büyücülere uyarız.",
}

O = {
21: ("eksen: **lafız YOK · رَبّ *(Rab)* 7. sırada — beşinci Rab** (rab z=1,62) · esmâ yok · aktör "
 "yok · edim haber · **şahıs 1S x7 — blokta en yüksek tek şahıs sayımı**; 2MP x2 · 3MS x2, iltifât "
 "0 · n=11 mora=54 harf=47 (n z=-0,15), fâsıla ٱلْمُرْسَلِينَ *(gönderilenler)* → ن, N sınıfı; "
 "i'râb NOM 1 · ACC 1 · GEN 1; bab I x4; zaman PERF x4; **edilgen 1** (pas z=1,10); dış düğüm 0 · "
 "**yıldız ★ — İKİ KAYNAK EŞİĞE YAKIN AMA YALNIZ BİRİ AŞIYOR** · kökler فرر *(kaçma, firar)* · خوف "
 "*(korku)* · وهب *(bağışlama, hibe)* · ربب *(rab, terbiye etme)* · حكم *(hüküm, hikmet)* · جعل "
 "*(kılma, var etme)* · رسل *(gönderme, elçi)* · bağ: **26:12 ve 26:14 ile korku üçlüsü tamamlanıyor** — "
 "orada أَخَافُ *(korkuyorum)* iki kez gelecek korkusuydu, burada خِفْتُكُمْ *(sizden korktum)* geçmiş "
 "korku; sûre 26'nın Mûsâ bölütünde خوف *(korku)* üç kez ve üçü de birinci şahıs (elle, L1, aday 615)"),
22: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı إِسْرائِيل *(İsrâîl)* 8. sırada, "
 "rol mecrur** · edim haber · şahıs 2MS x3 · 3FS x1 · 1S x1, iltifât 0 · n=8 mora=46 harf=32 "
 "(n z=-0,47), **fâsıla إِسْرَٰٓءِيلَ *(İsrâîl)* → ل — sûrenin dört kırılmasından İKİNCİSİ ve yine "
 "AYNI ÖZEL AD** (kafiye_kirik=1; yıldızın TEK kaynağı); i'râb NOM 2 · GEN 1; bab I x1 · II x1; "
 "zaman IMPF x1 · PERF x1; dış düğüm 0 · **yıldız ★** · kökler نعم *(nimet; davar)* · منن *(nimet "
 "verme, menn; başa kakma)* · عبد *(kul, kulluk)* · بني *(oğul, evlat)* · bağ: **26:17 ile aynı "
 "fâsıla** — sûrenin iki kırılması aynı kelimeyle (إِسْرَٰٓءِيلَ); orada Mûsâ'nın isteği, burada "
 "Firavun'a itiraz (elle, L1, aday 612)"),
23: ("eksen: **lafız YOK · رَبّ *(Rab)* 4. sırada — altıncı Rab**, **rab z=3,94: yıldızın TEK "
 "kaynağı** (n=5, oran 0,20; 26:9 ve 25:64 ile AYNI değer) · esmâ yok · **aktör: adlı فِرْعَوْن "
 "*(Firavun)* 2. sırada, rol FAİL + KONUŞAN** · edim haber, kip işareti yok · şahıs 3MS x1, iltifât "
 "0 · n=5 mora=27 harf=20 (n z=-0,79), fâsıla ٱلْعَٰلَمِينَ *(âlemler)* → ن, N sınıfı; i'râb NOM 2 · "
 "GEN 1; bab I x1; zaman PERF x1; dış düğüm 0 · **yıldız ★★★** · kökler قول *(söz söyleme)* · ربب "
 "*(rab, terbiye etme)* · علم *(bilme; âlem)* · bağ: **25:60 ile SORU BİÇİMİ ÖZDEŞLİĞİ** — orada "
 "وَمَا ٱلرَّحْمَٰنُ *(Rahmân da ne)*, burada وَمَا رَبُّ ٱلْعَٰلَمِينَ *(âlemlerin Rabbi de ne)*; "
 "**iki sûrede iki itirazcı, aynı مَا + ilâhî ad kalıbıyla soruyor** (elle, L1, aday 616)"),
24: ("eksen: **lafız YOK · رَبّ *(Rab)* 2. sırada — yedinci Rab** (rab z=2,05) · esmâ yok · aktör "
 "yok · edim şart, kip COND 1 · şahıs 3MS x1 · 3D x1 · 2MP x2, iltifât 0 · n=9 mora=52 harf=39 "
 "(n z=-0,36), fâsıla مُّوقِنِينَ *(kesin olarak inananlar)* → ن, N sınıfı; i'râb NOM 1 · GEN 2 · "
 "ACC 2; bab I x2; zaman PERF x2; **dış düğüm 3** · **yıldız ★★** · kökler قول *(söz söyleme)* · "
 "ربب *(rab, terbiye etme)* · سمو *(ad; gök)* · أرض *(yer, yeryüzü)* · بين *(arası; açıklama)* · "
 "كون *(olmak; mekân, yer)* · يقن *(yakîn, kesin bilgi)* · bağ: xref قال *(dedi)* + ربّ *(Rab)* + "
 "سماء *(gök)* → **13:16 · 23:86**; أرض *(yer)* + بين *(ara)* + كان *(oldu)* ve بين + كان + موقن "
 "*(kesin inanan)* → **44:7**; **25:59 ile terkip karşılaştırması** — orada خَلَقَ ٱلسَّمَٰوَٰتِ "
 "وَٱلْأَرْضَ وَمَا بَيْنَهُمَا *(gökleri, yeri ve ikisi arasındakileri yarattı)* bir YARATMA "
 "cümlesiydi, burada aynı üçlü bir RABLİK tanımı (elle, L1, aday 617)"),
25: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — حَوْل *(çevre)* göndergesi adsız · "
 "edim soru, kip INTG 1 · NEG 1 · şahıs 3MS x2 · 2MP x2, iltifât 0 · n=5 mora=28 harf=21 (n z=-0,79), "
 "fâsıla تَسْتَمِعُونَ *(işitiyorsunuz)* → ن, N sınıfı; i'râb ACC 1; bab I x1 · VIII x1; zaman "
 "PERF x1 · IMPF x1; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · حول *(çevre, etraf; "
 "hâl değişimi)* · سمع *(işitme)* · bağ: **26:15 ile سمع *(işitme)* karşıtlığı** — orada إِنَّا "
 "مَعَكُم مُّسْتَمِعُونَ *(biz sizinle beraber işitenleriz)* ilâhî eşlik, burada أَلَا تَسْتَمِعُونَ "
 "*(işitmiyor musunuz)* alaycı çağrı; aynı bab X, ters değer (elle, L1, aday 618)"),
26: ("eksen: **lafız YOK · رَبّ *(Rab)* 2. VE 3. sırada — sekizinci ve dokuzuncu Rab; kök ikilemesi "
 "ربب *(rab, terbiye etme)* x2**, **rab z=8,20: OKUMADA GÖRÜLEN EN YÜKSEK Z DEĞERİ** (n=5, iki Rab, "
 "oran 0,40) ve yıldızın TEK kaynağı · esmâ yok · aktör yok · edim haber · şahıs 3MS x1 · 2MP x2, "
 "iltifât 0 · n=5 mora=35 harf=24 (n z=-0,79), fâsıla ٱلْأَوَّلِينَ *(öncekiler)* → ن, N sınıfı; "
 "i'râb NOM 2 · GEN 2; bab I x1; zaman PERF x1; **dış düğüm 4** · **yıldız ★★★** · kökler قول *(söz "
 "söyleme)* · ربب *(rab, terbiye etme)* · أبو *(baba)* · أول *(ilk, evvel)* · bağ: xref قال *(dedi)* + "
 "ربّ *(Rab)* + ربّ → **18:14 · 21:56**; ربّ + ربّ + آباء *(atalar)* ve ربّ + آباء + أوّل *(evvelki)* → "
 "**37:126 · 44:8**; **ADAY 602'NİN EN UÇ VAKASI** (elle, L1)"),
27: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip EMPH 1 · şahıs 3MS x2 · "
 "2MP x2, iltifât 0 · n=7 mora=41 harf=31 (n z=-0,58), fâsıla لَمَجْنُونٌ *(deli)* → ن, N sınıfı; "
 "i'râb ACC 2 · NOM 1; bab I x1 · IV x1; zaman PERF x2; **edilgen 1 — أُرْسِلَ *(gönderildi)***, "
 "**pas z=2,52: yıldızın TEK kaynağı**; **kök ikilemesi رسل *(gönderme, elçi)* x2 — isim + edilgen "
 "fiil: رَسُولَكُمُ ٱلَّذِىٓ أُرْسِلَ *(size gönderilen elçiniz)***; dış düğüm 0 · **yıldız ★★** · "
 "kökler قول *(söz söyleme)* · رسل *(gönderme, elçi)* · جنن *(örtme, gizleme; cennet; cin; delilik)* · "
 "bağ: **جنن *(delilik)* — 529 kümesinin bilinen karışma kökü**; sûre 25'te beş geçişi de 'cennet' "
 "anlamındaydı, burada 'delilik'; kök düzeyi dikey komşuluk ayrımı yapmıyor (elle, L1, aday 619)"),
28: ("eksen: **lafız YOK · رَبّ *(Rab)* 2. sırada — onuncu Rab** (rab z=2,05) · esmâ yok · aktör yok · "
 "edim şart, kip COND 1 · şahıs 3MS x1 · 3D x1 · 2MP x4, iltifât 0 · n=9 mora=48 harf=40 (n z=-0,36), "
 "fâsıla تَعْقِلُونَ *(akıl ediyorsunuz)* → ن, N sınıfı; i'râb NOM 1 · GEN 2 · ACC 1; bab I x3; "
 "zaman PERF x2 · IMPF x1; **dış düğüm 2** · **yıldız ★★** · kökler قول *(söz söyleme)* · ربب *(rab, "
 "terbiye etme)* · شرق *(doğu; doğuş)* · غرب *(batı; gurbet)* · بين *(arası; açıklama)* · كون *(olmak; "
 "mekân, yer)* · عقل *(akletme)* · bağ: xref ربّ *(Rab)* + مشرق *(doğu)* + مغرب *(batı)* → **70:40 · "
 "73:9**; **26:24 ile paralel yapı** — ikisi de رَبّ + üç terimli kapsam + şart cevabı; orada dikey "
 "eksen (gök-yer-ara), burada yatay eksen (doğu-batı-ara), ve şart cevabı يقن *(yakîn)*'den عقل "
 "*(akletme)*'ye geçiyor (elle, L1, aday 617)"),
29: ("eksen: **lafız YOK · Rab YOK**; أله *(ilâh; lafza-i celâl)* kökü var ama NEKRE ve sahte ilâh — "
 "إِلَٰها غَيْرِى *(benden başka bir ilâh)* · esmâ yok · aktör yok · edim şart, kip EMPH 3 · COND 1 · "
 "şahıs 3MS x1 · 2MS x3 · 1S x2, iltifât 0 · n=8 mora=47 harf=37 (n z=-0,47), fâsıla ٱلْمَسْجُونِينَ "
 "*(zindana atılanlar)* → ن, N sınıfı; i'râb ACC 1 · NOM 1 · GEN 1; bab I x2 · VIII x1; zaman PERF "
 "x2 · IMPF x1; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · أخذ *(alma, edinme)* · أله "
 "*(ilâh; lafza-i celâl)* · غير *(başka, gayrı)* · جعل *(kılma, var etme)* · سجن *(hapis, zindan)* · "
 "bağ: **25:3, 25:18, 25:42, 25:43 ve 26:29 ile أله *(ilâh)* sahte-ilâh dizisi** — sûre 25'te üç "
 "konuşan (anlatıcı, tapılanlar, tapanlar) vardı; burada DÖRDÜNCÜ bir konuşan: **ilâhlığı KENDİNE "
 "atfeden** (إِلَٰها غَيْرِى *(benden başka bir ilâh)*) (elle, L1, aday 620)"),
30: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُبِين *(apaçık)* 5. sırada = fâsıla, MÜHÜRSÜZ — "
 "ÖLÇÜM ARTEFAKTI**: gönderge شَىْء *(şey)*; sûrenin üçüncü مُبِين artefaktı · aktör yok · edim "
 "soru + şart, kip INTG 1 · COND 1 · şahıs 3MS x1 · 1S x2 · 2MS x1, iltifât 0 · n=5 mora=26 harf=21 "
 "(n z=-0,79), fâsıla مُّبِينٍ *(apaçık)* → ن, N sınıfı; i'râb GEN 2; bab I x2; zaman PERF x2; dış "
 "düğüm 1 · yıldız ★ yok · kökler قول *(söz söyleme)* · جيأ *(gelme)* · شيأ *(dileme; şey)* · بين "
 "*(arası; açıklama; beyan)* · bağ: xref قال *(dedi)* + جاء *(geldi)* + شىء *(şey)* → **19:27**"),
31: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir + şart, kip IMPV 1 · COND 1 · "
 "şahıs 3MS x2 · 2MS x3, iltifât 0 · n=7 mora=30 harf=23 (n z=-0,58), fâsıla ٱلصَّٰدِقِينَ "
 "*(doğru söyleyenler)* → ن, N sınıfı; i'râb GEN 1; bab I x3; zaman PERF x2 · IMPV 1; dış düğüm 1 · "
 "yıldız ★ yok · kökler قول *(söz söyleme)* · أتي *(gelme, getirme)* · كون *(olmak; mekân, yer)* · "
 "صدق *(doğruluk, sadaka)* · bağ: xref أتى *(getir)* + كان *(oldu)* + صادق *(doğru söyleyen)* → "
 "**7:106**; **26:30 ile bitişik çift** — şart iki ayete bölünmüş: 30'da 'getirsem de mi', 31'de "
 "'getir öyleyse'"),
32: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُبِين 6. sırada = fâsıla — ARTEFAKT, dördüncü kez**: "
 "gönderge ثُعْبَان *(yılan)* · aktör yok · edim haber · şahıs 3MS x2 · 3FS x1, iltifât 0 · n=6 "
 "mora=34 harf=26 (n z=-0,68), fâsıla مُّبِينٌ → ن, N sınıfı; i'râb ACC 1 · NOM 2; bab IV x1; zaman "
 "PERF x1; dış düğüm 1 · yıldız ★ yok · **esit: 7:107 ile TAM AYET ÖZDEŞ** · kökler لقي "
 "*(karşılaşma, kavuşma; atma)* · عصو *(asâ, değnek)* · ثعب *(büyük yılan (su'bân))* · بين *(arası; "
 "açıklama; beyan)* · bağ: xref ألقى *(attı)* + عصا *(asâ)* + ثعبان *(yılan)* ve عصا + ثعبان + مبين "
 "*(apaçık)* → **7:107**; **26:32-33 ↔ 7:107-108 ARDIŞIK BÖLÜT İKİZİ ve esit alanı İKİSİNİ DE "
 "YAKALIYOR** — 25:8-9 ↔ 17:47-48 vakasında (aday 530) esit alanı KAÇIRMIŞTI (elle, L1, aday 621)"),
33: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber · şahıs 3MS x2 · 3FS x1, "
 "iltifât 0 · n=6 mora=33 harf=26 (n z=-0,68), fâsıla لِلنَّٰظِرِينَ *(bakanlar için)* → ن, N sınıfı; "
 "i'râb ACC 1 · NOM 1 · GEN 1; bab I x1; zaman PERF x1; dış düğüm 1 · yıldız ★ yok · **esit: 7:108 "
 "ile TAM AYET ÖZDEŞ** · kökler نزع *(çekip alma, söküp çıkarma)* · يدي *(el)* · بيض *(beyazlık; "
 "yumurta)* · نظر *(bakma; mühlet verme)* · bağ: xref نزع *(çekti)* + يد *(el)* + أبيض *(bembeyaz)* "
 "ve يد + أبيض + ناظر *(bakan)* → **7:108** (elle, L1, aday 621)"),
34: ("eksen: **lafız YOK · Rab YOK** · **esmâ عَلِيم *(alîm, bilgili)* 7. sırada = fâsıla, MÜHÜRSÜZ — "
 "ÖLÇÜM ARTEFAKTI**: gönderge سَٰحِر *(büyücü)*, yani BİR İNSAN; ölçüt (a) dışlıyor · aktör yok — "
 "ٱلْمَلَأ *(ileri gelenler)* aktör tablosuna girmiyor · edim haber, kip EMPH 1 · şahıs 3MS x2, "
 "iltifât 0 · n=7 mora=38 harf=27 (n z=-0,58), fâsıla عَلِيمٌ *(bilgili)* → م, N sınıfı; i'râb "
 "GEN 1 · ACC 2 · NOM 2; bab I x1; zaman PERF x1; **biçim DIKKAT**; dış düğüm 0 · yıldız ★ yok · "
 "kökler قول *(söz söyleme)* · ملأ *(mele, ileri gelenler; doldurma)* · حول *(çevre, etraf; hâl "
 "değişimi)* · سحر *(büyü, sihir)* · علم *(bilme; ilim)* · bağ: **25:8'in رَجُلا مَّسْحُورا "
 "*(büyülenmiş bir adam)* nitelemesiyle TERS YÖN** — orada elçi büyünün NESNESİ, burada büyünün "
 "ÖZNESİ (سَٰحِرٌ عَلِيمٌ *(bilgili bir büyücü)*) (elle, L1, aday 622)"),
35: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · şahıs 3MS x3 · "
 "2MP x4, iltifât 0 · n=8 mora=42 harf=36 (n z=-0,47), fâsıla تَأْمُرُونَ *(buyuruyorsunuz)* → ن, "
 "N sınıfı; i'râb GEN 2; bab I x1 · IV x2; zaman IMPF x3; **dış düğüm 3** · yıldız ★ yok · kökler "
 "رود *(irade, isteme)* · خرج *(çıkma, çıkarma)* · أرض *(yer, yeryüzü)* · سحر *(büyü, sihir)* · أمر "
 "*(emir; iş)* · bağ: xref أراد *(istedi)* + أخرج *(çıkardı)* + أرض *(yer)* → **7:110 · 20:63**; "
 "أخرج + أرض + سحر *(büyü)* → **20:57 · 20:63**"),
36: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir, kip IMPV 2 · şahıs 3MP x2 · "
 "2MS x2 · 3MS x2, iltifât 0 · n=7 mora=44 harf=34 (n z=-0,58), fâsıla حَٰشِرِينَ *(toplayıcılar)* → "
 "ن, N sınıfı; i'râb NOM 1 · GEN 1 · ACC 1; bab I x2 · IV x1; zaman PERF x1 · IMPV 2; dış düğüm 1 · "
 "yıldız ★ yok · kökler قول *(söz söyleme)* · رجو *(umma, bekleme; erteleme)* · أخو *(kardeş)* · بعث "
 "*(gönderme, diriltme)* · مدن *(şehir, medine)* · حشر *(toplama, mahşer)* · bağ: xref قال *(dedi)* + "
 "ترجي *(ertele)* + أخ *(kardeş)* → **7:111**; **رجو *(umma, bekleme; erteleme)* — 529 kümesine yeni "
 "vaka**: 25:21 ve 25:40'ta 'umma' anlamındaydı, burada bab IV ve 'erteleme' anlamında (elle, L1, "
 "aday 623)"),
37: ("eksen: **lafız YOK · Rab YOK** · **esmâ عَلِيم *(alîm, bilgili)* 4. sırada = fâsıla — ARTEFAKT, "
 "ikinci kez ve yine gönderge سَٰحِر *(büyücü)*** · aktör yok · edim haber · şahıs 3MP x2 · 2MS x1, "
 "iltifât 0 · n=4 mora=25 harf=17 (n z=-0,89), fâsıla عَلِيمٍ → م, N sınıfı; **i'râb GEN 3 — dört "
 "kelimenin üçü mecrur**; bab I x1; zaman IMPF x1; dış düğüm 0 · yıldız ★ yok · kökler أتي *(gelme, "
 "getirme)* · كلل *(hep, bütün)* · سحر *(büyü, sihir)* · علم *(bilme; ilim)* · bağ: **26:34 ile aynı "
 "terkip** — سَٰحِرٌ عَلِيمٌ *(bilgili büyücü)* üç ayet arayla iki kez, ikisi de fâsıla; ikisi de "
 "esmâ artefaktı (elle, L1, aday 622)"),
38: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "3MS x1 — ayette başka şahıs yok**, iltifât 0 · n=5 mora=32 harf=25 (n z=-0,79), fâsıla مَّعْلُومٍ "
 "*(bilinen, belirlenmiş)* → م, N sınıfı; **i'râb NOM 1 · GEN 3**; bab I x1; zaman PERF x1; "
 "**edilgen 1 — فَجُمِعَ *(toplandı)*; ayetin TEK fiili ve o da edilgen, oran 1,00**, pas z=5,38: "
 "**yıldızın TEK kaynağı** (25:34 ile aynı değer ve aynı sebep); dış düğüm 1 · **yıldız ★★★** · "
 "kökler جمع *(toplama, cem)* · سحر *(büyü, sihir)* · وقت *(vakit, belirlenmiş zaman)* · يوم *(gün)* · "
 "علم *(bilme; ilim)* · bağ: xref ميقات *(belirlenmiş vakit)* + يوم *(gün)* + معلوم *(bilinen)* → "
 "**56:50**; **وقت *(vakit, belirlenmiş zaman)* korpusta 13 geçişli** (elle, L1)"),
39: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · şahıs 3MS x1 · "
 "2MP x1, iltifât 0 · n=5 mora=29 harf=22 (n z=-0,79), fâsıla مُجْتَمِعُونَ *(toplananlar)* → ن, N "
 "sınıfı; i'râb GEN 1 · NOM 1; bab I x1; zaman PERF x1; **edilgen 1 — قِيلَ *(dendi)*; ayetin TEK "
 "fiili ve o da edilgen, oran 1,00**, pas z=5,38: **yıldızın TEK kaynağı** · dış düğüm 0 · **yıldız "
 "★★★** · kökler قول *(söz söyleme)* · أنس *(insan; ünsiyet)* · جمع *(toplama, cem)* · bağ: **26:38 "
 "ile bitişik çift ve İKİSİ DE ★★★, ikisinde de tek fiil edilgen** — okumada ilk kez iki ardışık "
 "ayetin ikisi de aynı kaynaktan ★★★ alıyor; **جمع *(toplama, cem)* iki ayette iki çatıda: edilgen "
 "(فَجُمِعَ) ve etken-ism-i fâil (مُجْتَمِعُونَ)** (elle, L1, aday 624)"),
40: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim şart, kip COND 1 · şahıs 1P x2 · "
 "3MP x3, iltifât 0 · n=7 mora=40 harf=32 (n z=-0,58), fâsıla ٱلْغَٰلِبِينَ *(galip gelenler)* → ن, "
 "N sınıfı; **i'râb ACC 3**; bab I x1 · VIII x1; zaman IMPF x1 · PERF x1; dış düğüm 0 · yıldız ★ yok · "
 "kökler تبع *(uyma, ardından gitme)* · سحر *(büyü, sihir)* · كون *(olmak; mekân, yer)* · غلب "
 "*(galip gelme, üstünlük)* · bağ: **25:8 ile تبع *(uyma)* karşılaştırması** — orada zalimler "
 "'siz büyülenmiş bir adama UYUYORSUNUZ' diyordu (olumsuz), burada kalabalık 'büyücülere UYARIZ' "
 "diyor (şarta bağlı olumlu); aynı kök, aynı alan, ters kutup (elle, L1, aday 625)"),
}

M = {
21: ("Mûsâ'nın cevabı geçmiş bir korkuyla açılıyor: فَفَرَرْتُ مِنكُمْ لَمَّا خِفْتُكُمْ *(sizden "
 "korkunca kaçtım)*. Ölçülebilir bir korku dizisi: 26:12'de أَخَافُ أَن يُكَذِّبُونِ *(yalanlamalarından "
 "korkuyorum)*, 26:14'te أَخَافُ أَن يَقْتُلُونِ *(öldürmelerinden korkuyorum)* — ikisi de gelecek; "
 "burada خِفْتُكُمْ *(sizden korktum)* mâzi. Üç geçiş, üçü de birinci şahıs, iki gelecek bir geçmiş. "
 "فرر *(kaçma, firar)* korpusta 15 geçişli. Ve on bir kelimede 1S yedi kez — blokta en yüksek tek "
 "şahıs sayımı. Yıldız tek: rab z=1,62 eşiği aşıyor, pas z=1,10 aşmıyor."),
22: ("İtiraz bir soru biçiminde ve nesnesi bir nimet iddiası: وَتِلْكَ نِعْمَةٌ تَمُنُّهَا عَلَىَّ "
 "*(başıma kaktığın nimet bu mu)*. منن *(nimet verme, menn; başa kakma)* korpusta 27 geçişli ve iki "
 "kutuplu — 'nimet verme' ve 'başa kakma'; burada ikinci kutupta (aday 529 sınıfı). Ölçülebilir bir "
 "fâsıla tekrarı: إِسْرَٰٓءِيلَ *(İsrâîl)* sûrenin ikinci kafiye kırılması ve **26:17 ile aynı "
 "kelime** — iki kırılma tek özel adla. Sûre 25'te tek kırılma vardı ve fâsılası bir cins addı."),
23: ("Firavun'un sorusu bir tanım talebi: وَمَا رَبُّ ٱلْعَٰلَمِينَ *(âlemlerin Rabbi de ne)*. "
 "Ölçülebilir bir kalıp özdeşliği: 25:60'ta itirazcılar وَمَا ٱلرَّحْمَٰنُ *(Rahmân da ne)* diye "
 "sormuştu — **iki sûrede iki itirazcı, aynı مَا + ilâhî ad kalıbı**. Sûre 25'te bu, adın özel ad "
 "gibi işlediğinin kanıtıydı (aday 578); burada soru bir SIFAT TAMLAMASINA yöneltiliyor (رَبُّ "
 "ٱلْعَٰلَمِينَ), yani aynı kalıp iki farklı dilbilgisel nesneye uygulanıyor. Beş kelime, tek Rab, "
 "rab z=3,94 — yıldızın tek kaynağı. Ve Firavun sûrede ilk kez rol FAİL + KONUŞAN."),
24: ("Cevap bir kapsam tanımıyla veriliyor ve kapsam üç terimli: ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَمَا "
 "بَيْنَهُمَآ *(gökler, yer ve ikisi arasındakiler)*. Ölçülebilir bir terkip karşılaştırması: 25:59'da "
 "aynı üçlü bir YARATMA cümlesinin nesnesiydi (خَلَقَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ وَمَا بَيْنَهُمَا "
 "*(gökleri, yeri ve ikisi arasındakileri yarattı)*), burada bir RABLİK tanımının kapsamı. Cevap bir "
 "şartla bitiyor: إِن كُنتُم مُّوقِنِينَ *(kesin olarak inanıyorsanız)*; يقن *(yakîn, kesin bilgi)* "
 "korpusta 28 geçişli. Üç xref'ten ikisi tek ayete (44:7) düşüyor."),
25: ("Beş kelime ve bir yön değişimi: Firavun cevabı Mûsâ'ya değil çevresine iletiyor — قَالَ "
 "لِمَنْ حَوْلَهُۥٓ *(çevresindekilere dedi)*. Ölçülebilir bir muhatap kayması: diyalog iki kişilikken "
 "üçüncü bir taraf devreye giriyor. Ve fiil سمع *(işitme)* bab X: أَلَا تَسْتَمِعُونَ *(işitmiyor "
 "musunuz)* — 26:15'te aynı bab ve aynı kök ilâhî eşlik bildiriyordu (إِنَّا مَعَكُم مُّسْتَمِعُونَ "
 "*(biz sizinle beraber işitenleriz)*). Aynı kalıp, on ayet arayla, ters değer."),
26: ("**Okumada görülen en yüksek z değeri burada: rab z=8,20.** Sebebi ölçülebilir — ayet beş "
 "kelime ve içinde İKİ رَبّ var, oran 0,40; z, Rab sayısını değil oranını ölçüyor ve payda küçük. "
 "Kök ikilemesi رَبُّكُمْ وَرَبُّ ءَابَآئِكُمُ ٱلْأَوَّلِينَ *(sizin Rabbiniz ve önceki "
 "atalarınızın Rabbi)* — aynı kelime iki iyelikle, biri şimdiki muhataba biri geçmişe. Üç xref'ten "
 "ikisi aynı iki ayete (37:126, 44:8) düşüyor, yani terkip korpusta sabit. Ve dış düğüm 4 — blokta "
 "26:26 ile 26:24 en bağlantılı ayetler."),
27: ("Firavun'un ikinci hamlesi bir niteleme: إِنَّ رَسُولَكُمُ ٱلَّذِىٓ أُرْسِلَ إِلَيْكُمْ "
 "لَمَجْنُونٌ *(size gönderilen elçiniz gerçekten deli)*. Ölçülebilir bir kök ikilemesi: رسل "
 "*(gönderme, elçi)* isim ve edilgen fiil olarak arka arkaya — 'elçiniz' ve 'gönderilen'; yani "
 "niteleme, elçiliği kabul edip aklı reddediyor. Yıldızın tek kaynağı bu edilgen (pas z=2,52). Ve "
 "جنن *(delilik)* — 529 kümesinin bilinen karışma kökü: sûre 25'te beş geçişin beşi de 'cennet' "
 "anlamındaydı, burada 'delilik'."),
28: ("Üçüncü cevap yönü değiştiriyor: 26:24'te kapsam DİKEY (gök-yer-ara), burada YATAY "
 "(ٱلْمَشْرِقِ وَٱلْمَغْرِبِ وَمَا بَيْنَهُمَآ *(doğu, batı ve ikisi arasındakiler)*). Ölçülebilir "
 "bir paralel yapı: ikisi de رَبّ + üç terimli kapsam + şart cevabı; şart cevabı da değişiyor — "
 "يقن *(yakîn, kesin bilgi)*'den عقل *(akletme)*'ye. İki ayet arasında Firavun'un iki alaycı sözü "
 "duruyor (26:25 ve 26:27). شرق *(doğu; doğuş)* korpusta 17, غرب *(batı; gurbet)* 17 geçişli ve "
 "dikey ölçüm ikisini de birbirine bağlıyor."),
29: ("Tehdit bir ilâhlık iddiası taşıyor: لَئِنِ ٱتَّخَذْتَ إِلَٰها غَيْرِى *(benden başka bir ilâh "
 "edinirsen)*. Ölçülebilir bir dizi tamamlanması: sûre 25'te أله *(ilâh)* kökü sahte ilâh için üç "
 "konuşanla kullanılmıştı — anlatıcı (25:3), tapılanlar (25:18), tapanlar (25:42) — burada DÖRDÜNCÜ "
 "konuşan: ilâhlığı KENDİNE atfeden. Ve fiil yine أخذ *(alma, edinme)* bab VIII, sûre 25'te yedi "
 "geçişi olan kalıp. سجن *(hapis, zindan)* korpusta 14 geçişli ve dikey ölçümü ▸önce Yûsuf bağlamı "
 "veriyor — kökün korpustaki ana yatağı başka bir kıssa."),
30: ("Beş kelime ve bir şart sorusu: أَوَلَوْ جِئْتُكَ بِشَىْءٍ مُّبِينٍ *(sana apaçık bir şey "
 "getirsem de mi)*. Ölçülebilir bir belirsizlik: getirilecek şey شَىْء *(şey)* ile bırakılıyor — "
 "adlandırılmıyor, yalnız nitelikle veriliyor (مُّبِين *(apaçık)*). Ve o nitelik esmâ sayılmış: "
 "sûrenin üçüncü مُبِين artefaktı, göndergesi bir 'şey'. Sûre 26'nın altı مُبِين tokeninin ilk üçü "
 "sırasıyla kitap, şey ve yılan için — üçü de artefakt."),
31: ("Yedi kelime ve şart 26:30'dan devralınıyor: قَالَ فَأْتِ بِهِۦٓ إِن كُنتَ مِنَ ٱلصَّٰدِقِينَ "
 "*(getir onu, doğru söyleyenlerdensen)*. Ölçülebilir bir şart zinciri: 26:30 şartı açıyor "
 "(أَوَلَوْ *(de mi)*), 26:31 kapatıyor (إِن كُنتَ *(eğer isen)*) — iki ayet tek koşullu yapı. Ve "
 "صدق *(doğruluk, sadaka)* korpusta 155 geçişli; buradaki lemma ٱلصَّٰدِقِين *(doğru söyleyenler)*, "
 "yani 'sadaka' değil 'doğruluk' kutbunda."),
32: ("Asâ olayı tek cümlede: فَأَلْقَىٰ عَصَاهُ فَإِذَا هِىَ ثُعْبَانٌ مُّبِينٌ *(asâsını attı; bir "
 "anda apaçık bir yılan oluverdi)*. ثعب *(büyük yılan (su'bân))* korpusta İKİ geçişli (7:107 ve "
 "burada) ve ikisi de aynı cümlede. **Ölçülebilir bir ikizlik: 26:32 ile 7:107, 26:33 ile 7:108 TAM "
 "AYET ÖZDEŞ ve defter.json esit alanı İKİSİNİ DE YAKALIYOR.** Bu, 25:8-9 ↔ 17:47-48 vakasının "
 "(aday 530) tam karşıtı: orada esit alanı imlâ farkı yüzünden kaçırmıştı. İki vaka birlikte alanın "
 "neyi yakalayıp neyi kaçırdığını gösteriyor."),
33: ("İkinci mucize ve yine tek cümlede: وَنَزَعَ يَدَهُۥ فَإِذَا هِىَ بَيْضَآءُ لِلنَّٰظِرِينَ "
 "*(elini çekip çıkardı; bakanlara bembeyaz göründü)*. Ölçülebilir bir yapı özdeşliği: 26:32 ile "
 "aynı kalıp — fiil + فَإِذَا هِىَ *(bir anda o)* + yüklem. İki ayet aynı sözdizimsel iskelette. "
 "بيض *(beyazlık; yumurta)* korpusta 12 geçişli ve dikey ölçümü ▸önce göz-yüz bağlamı veriyor. "
 "Ve tanık ekleniyor: لِلنَّٰظِرِينَ *(bakanlar için)* — mucize bir izleyici kitlesiyle birlikte "
 "tanımlanıyor."),
34: ("Firavun'un nitelemesi bir uzmanlık iddiası: إِنَّ هَٰذَا لَسَٰحِرٌ عَلِيمٌ *(bu, bilgili bir "
 "büyücü)*. Ölçülebilir bir ters yön: 25:8'de zalimler elçiyi رَجُلا مَّسْحُورا *(büyülenmiş bir "
 "adam)* diye nitelemişti — büyünün NESNESİ; burada سَٰحِرٌ عَلِيمٌ *(bilgili bir büyücü)* — "
 "büyünün ÖZNESİ. Aynı kök (سحر *(büyü, sihir)*), aynı reddetme işlevi, ters çatı. Ve fâsıladaki "
 "عَلِيم *(alîm)* esmâ sayılmış, oysa göndergesi bir insan; sûrenin dört عَلِيم tokeninin ikisi "
 "burada ve 26:37'de, ikisi de aynı terkipte ve ikisi de artefakt."),
35: ("Suçlama siyasî bir amaca bağlanıyor: يُرِيدُ أَن يُخْرِجَكُم مِّنْ أَرْضِكُم بِسِحْرِهِۦ "
 "*(büyüsüyle sizi yurdunuzdan çıkarmak istiyor)*. Ölçülebilir bir xref yoğunluğu: iki 3-gram dört "
 "ayete (7:110, 20:57, 20:63) bağlanıyor — terkip korpusta sabit, donmuş kalıp adayı (aday 437). "
 "Ve soru bir danışma: فَمَاذَا تَأْمُرُونَ *(ne buyurursunuz)*; أمر *(emir; iş)* burada "
 "Firavun'un DEĞİL çevresinin fiili — otoritenin yönü tersine dönüyor."),
36: ("Cevap iki emirle veriliyor: أَرْجِهْ وَأَخَاهُ وَٱبْعَثْ *(onu ve kardeşini beklet ve gönder)*. "
 "رجو *(umma, bekleme; erteleme)* burada bab IV ve 'erteleme' anlamında; sûre 25'te iki geçişi de "
 "(25:21, 25:40) 'umma' anlamındaydı — kök düzeyi dikey komşuluk bu ayrımı yapmıyor, 529 kümesine "
 "yeni vaka. Ve مدن *(şehir, medine)* korpusta 17 geçişli; toplama görevlileri şehirlere "
 "gönderiliyor — حشر *(toplama, mahşer)* kökü burada dünyevî bir toplama için, oysa 25:17 ve "
 "25:34'te haşir sahnesindeydi."),
37: ("Dört kelime ve üçü mecrur — blokta en yoğun GEN oranı. Terkip 26:34'ten birebir geri geliyor: "
 "سَٰحِرٍ عَلِيمٍ *(bilgili büyücü)*, üç ayet arayla ikinci kez ve ikisi de fâsıla. Ölçülebilir bir "
 "genelleme: 26:34'te tekil ve işaretli (هَٰذَا *(bu)*), burada كُلِّ سَٰحِرٍ *(her büyücü)* — "
 "bireyden sınıfa. Ve ikisi de esmâ artefaktı; sûrenin esmâ sayımı bu tekrarları da içeriyor."),
38: ("Yıldızın tek kaynağı tek bir edilgen fiil ve oran 1,00: فَجُمِعَ ٱلسَّحَرَةُ *(büyücüler "
 "toplandı)* — ayetin tek fiili ve edilgen. 25:34 ile aynı değer (pas z=5,38) ve aynı sebep. "
 "Ölçülebilir bir zaman belirlemesi: لِمِيقَٰتِ يَوْمٍ مَّعْلُومٍ *(belirlenmiş bir günün belirli "
 "vaktinde)* — وقت *(vakit, belirlenmiş zaman)* korpusta 13 geçişli ve buradaki lemma مِيقَات; "
 "terkip 56:50 ile ortak. SINIR: ayet bir vakit ADI veriyor ama ne ölçü ne süre tanımlıyor."),
39: ("Beş kelime, tek fiil, ve o da edilgen: وَقِيلَ لِلنَّاسِ *(halka dendi)* — oran 1,00, pas "
 "z=5,38. **26:38 ile bitişik çift ve ikisi de ★★★, ikisinde de kaynak aynı.** Okumada ilk kez iki "
 "ardışık ayet aynı kaynaktan ★★★ alıyor. Ölçülebilir bir çatı çifti: جمع *(toplama, cem)* iki "
 "ayette iki çatıda — 26:38'de edilgen fiil (فَجُمِعَ), burada etken ism-i fâil (مُّجْتَمِعُونَ "
 "*(toplananlar)*). Toplanan büyücüler edilgen, toplanan halk etken."),
40: ("Kalabalığın umudu bir şarta bağlı: لَعَلَّنَا نَتَّبِعُ ٱلسَّحَرَةَ إِن كَانُوا۟ هُمُ "
 "ٱلْغَٰلِبِينَ *(galip gelen onlar olursa büyücülere uyarız)*. Ölçülebilir bir kutup tersliği: "
 "25:8'de zalimler إِن تَتَّبِعُونَ إِلَّا رَجُلا مَّسْحُورا *(siz büyülenmiş bir adamdan "
 "başkasına uymuyorsunuz)* demişti — تبع *(uyma, ardından gitme)* olumsuz ve suçlama; burada aynı "
 "kök olumlu ve şarta bağlı bir niyet. Ve غلب *(galip gelme, üstünlük)* korpusta 31 geçişli; "
 "kalabalık hakikate değil galibiyete göre hizalanacağını söylüyor — ölçülen, şartın ölçütünün "
 "doğruluk değil üstünlük olması."),
}

ATLAMA = {
 "_mercek_26_23": ("26:23 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. قَالَ فِرْعَوْنُ وَمَا رَبُّ "
  "ٱلْعَٰلَمِينَ. Tek kaynak rab z=3,94 (n=5, oran 0,20). İçerik bir tanım sorusu."),
 "_mercek_26_26": ("26:26 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. قَالَ رَبُّكُمْ وَرَبُّ ءَابَآئِكُمُ "
  "ٱلْأَوَّلِينَ. Tek kaynak **rab z=8,20 — OKUMADA GÖRÜLEN EN YÜKSEK Z DEĞERİ** (n=5, iki Rab, "
  "oran 0,40). İçerik bir rablik tanımı. ADAY 602'NİN EN UÇ VAKASI."),
 "_mercek_26_38_39": ("26:38 ve 26:39 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. İkisinde de tek kaynak "
  "pas z=5,38 ve ikisinde de sebep aynı: ayetin TEK fiili edilgen, oran 1,00. **OKUMADA İLK KEZ İKİ "
  "ARDIŞIK AYET AYNI KAYNAKTAN ★★★ ALIYOR.** 26:38 bir toplanma sahnesi, 26:39 bir çağrı; ikisinde "
  "de ne canlı, ne gök cismi, ne ölçü, ne süreç. 26:38'de bir VAKİT adı geçiyor (مِيقَٰتِ يَوْمٍ "
  "مَّعْلُومٍ) ama ne ölçü ne süre tanımlanıyor — çıpa sayılmadı."),
 "_blok_notu_26_21_40": ("BLOK BİLANÇOSU: ★★★ 4 (26:23, 26, 38, 39) · ★★ 3 (26:24, 27, 28) · ★ 2 "
  "(26:21, 22) · 11 ayet yıldızsız. **DOKUZ YILDIZLI AYETİN KAYNAK DAĞILIMI: rab x5 · pas x3 · "
  "kafiye kırılması x1 — HİÇBİRİ İÇERİKTEN.** VE HİÇBİRİNDE ÇIPA YOK. Blokta çıpa taşıyabilecek "
  "ayet YOK: bölüt tamamen diyalog. ADAY 599/602 tablosuna: sûre 26'nın okunan 40 ayetinde ★★★ 6, "
  "çıpası 0; çıpalı ayet 1 (26:7) ve yıldızsız."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(21, 41):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 40/227.** Devam: 26:41'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-40 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1762
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(21, 41):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
