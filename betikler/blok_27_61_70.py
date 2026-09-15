# -*- coding: utf-8 -*-
"""blok_27_61_70.py — sûre 27 yedinci blok (27:61-70). Doğa bölütünün gövdesi ve kapanışı,
diriliş tartışması."""
import json
DIK = json.load(open('blok_dikey_27_61_70.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
61: "Yoksa yeri bir karar yeri kılan, aralarında ırmaklar var eden, ona sabit dağlar koyan ve iki deniz arasına bir engel çeken mi? Allah'la beraber bir ilâh mı? Hayır, çoğu bilmiyor.",
62: "Yoksa darda kalana, kendisine yalvardığında karşılık veren, kötülüğü gideren ve sizi yeryüzünün halifeleri kılan mı? Allah'la beraber bir ilâh mı? Ne kadar az düşünüyorsunuz.",
63: "Yoksa karanın ve denizin karanlıklarında size yol gösteren, rahmetinin önünde rüzgârları müjdeci gönderen mi? Allah'la beraber bir ilâh mı? Allah, onların ortak koştuklarından yücedir.",
64: "Yoksa yaratmayı başlatan, sonra onu tekrarlayan ve size gökten ve yerden rızık veren mi? Allah'la beraber bir ilâh mı? De ki: Doğru söylüyorsanız delilinizi getirin.",
65: "De ki: Göklerde ve yerde olanlar gaybı bilmez, Allah'tan başka; ne zaman diriltileceklerini de fark etmezler.",
66: "Hayır, âhiret hakkındaki bilgileri tükenmiştir; hayır, ondan şüphe içindedirler; hayır, ona karşı kördürler.",
67: "İnkâr edenler dedi: Biz de babalarımız da toprak olduğumuzda gerçekten çıkarılacak mıyız?",
68: "Andolsun, bu bize de daha önce babalarımıza da vaat edilmişti; bu, öncekilerin masallarından başka bir şey değil.",
69: "De ki: Yeryüzünde gezin de suçluların sonu nasıl olmuş, bakın.",
70: "Onlara üzülme; kurdukları tuzaktan dolayı da sıkıntıda olma.",
}

O = {
61: ("eksen: **ALLAH LAFZI 17. sırada** (allah z=0,42) · Rab yok · esmâ yok · aktör yok · edim "
 "soru, kip INTG 1 · NEG 1 · **şahıs 3MS x4 · 3FS x2 · 3MP x3, sahset ['3']** · n=21 mora=112 "
 "harf=91 (n z=0,91), fâsıla يَعْلَمُونَ *(biliyorlar)* → ن, N sınıfı; **i'râb ACC 8 · NOM 3 · GEN "
 "1**; **bab I x5**; zaman PERF x4 · IMPF 1; **kök ikilemesi جعل *(kılma, var etme)* x4 — bir "
 "ayette DÖRT kez, blokta en yüksek** · أله *(ilâh; lafza-i celâl)* x2; **SAYI ALANI: كثر *(çokluk)* → أَكْثَر *(çoğu)***; "
 "**nakarat alanı: 0 — oysa ayet `أَءِلَٰهٌ مَّعَ ٱللَّهِ` ile bitiyor**; **biçim IDRAB**; dış "
 "düğüm 1 · yıldız ★ yok · kökler جعل *(kılma, var etme)* · أرض *(yer, yeryüzü)* · قرر *(karar kılma; göz aydınlığı)* · خلل *(ara, aralık; dostluk (hulle))* · نهر *(ırmak)* · رسو *(sabit dağ)* · بين *(arası; açıklama)* · بحر *(deniz)* · **حجز *(engel, "
 "perde (hâciz))* — YENİ KÖK, n=2** · أله *(ilâh; lafza-i celâl)* · كثر *(çokluk)* · علم *(bilme)* · bağ: xref جعل *(kılma, var etme)* + أرض *(yer, yeryüzü)* + قرار → **40:64** "
 "(elle, L2, aday 844/849)"),
62: ("eksen: **ALLAH LAFZI 13. sırada** (allah z=0,72) · Rab yok · esmâ yok · aktör yok · edim "
 "soru, kip INTG 1 · şahıs 3MS x5 · 2MP x3, sahset ['2','3'], iltifât 0 · n=16 mora=99 harf=74 (n "
 "z=0,38), fâsıla تَذَكَّرُونَ *(düşünüyorsunuz)* → ن, N sınıfı; **i'râb ACC 5 · GEN 2 · NOM 1**; "
 "bab I x3 · IV x1 · **bab V x1**; **zaman IMPF x4 · PERF 1**; **kök ikilemesi أله *(ilâh; lafza-i celâl)* x2**; **SAYI "
 "ALANI: قلل *(azlık)* → قَلِيل *(az)*** — 27:61'in أَكْثَر'ının karşıtı, ardışık ayetlerde; **nakarat "
 "alanı: 0**; dış düğüm 0 · yıldız ★ yok · kökler جوب *(cevap verme, icabet)* · ضرر *(zarar)* · دعو *(çağırma, dua)* · كشف *(giderme, açma)* · سوأ *(kötülük)* · جعل *(kılma, var etme)* · خلف *(ayrılığa düşme; ardından gelme)* · أرض *(yer, yeryüzü)* · "
 "أله *(ilâh; lafza-i celâl)* · قلل *(azlık)* · ذكر *(anma, zikir)* · bağ: **كشف *(giderme, açma)* 27:44'ten sonra sûrede ikinci geçiş** — orada "
 "baldırların açılması, burada kötülüğün giderilmesi; **aynı kök, iki anlam alanı** (elle, L1, "
 "aday 844)"),
63: ("eksen: **ALLAH LAFZI İKİ KEZ — 16. ve 18. sırada** (allah z=1,47: **yıldız eşiğinin ALTINDA "
 "kalan en yüksek eksen z'si**) · Rab yok · **esmâ بَرّ *(kara; iyilik)* 5. sırada, ORTA konum, "
 "MÜHÜRSÜZ — ARTEFAKT**: gönderge ٱلْبَرِّ وَٱلْبَحْرِ *(kara ve deniz)*, bir YER/ALAN adı · aktör "
 "yok · edim soru, kip INTG 1 · şahıs 3MS x4 · 2MP x1 · 3MP x2, iltifât 0 · n=20 mora=102 harf=84 "
 "(n z=0,81), fâsıla يُشْرِكُونَ *(ortak koşuyorlar)* → ن, N sınıfı — **27:59 ile aynı fâsıla**; "
 "**i'râb GEN 5 · ACC 4 · NOM 3**; bab I x1 · IV x2 · **bab VI x1**; **kök ikilemesi أله *(ilâh; lafza-i celâl)* x3 — "
 "blokta ve sûrede en yüksek أله *(ilâh; lafza-i celâl)* yoğunluğu**; **nakarat alanı: 0**; **dış düğüm 5 — blokta en "
 "yüksek** · yıldız ★ yok · kökler هدي *(yol gösterme)* · ظلم *(zulüm)* · برر *(iyilik; kara)* · بحر *(deniz)* · رسل *(gönderme, elçi)* · روح *(ruh; rüzgâr)* · بشر *(müjde; beşer)* · بين *(arası; açıklama)* · يدي *(el)* · رحم *(rahmet, merhamet)* · أله *(ilâh; lafza-i celâl)* "
 "· علو *(yücelik; böbürlenme)* · شرك *(ortak koşma)* · bağ: xref ظلمة + برّ + بحر *(deniz)* → **6:63 · 6:97**; أرسل + ريح + بشر *(müjde; beşer)* ve türevleri → "
 "**7:57 · 25:48**; تعالى + اللّه + أشرك → **7:190** (elle, L2, aday 846/847)"),
64: ("eksen: **ALLAH LAFZI 13. sırada** (allah z=0,52) · Rab yok · esmâ yok · aktör yok · edim soru "
 "+ emir + şart, kip INTG 1 · **IMPV 2** · COND 1 · şahıs 3MS x4 · 2MP x6 · 2MS x1, baskın şahıs "
 "2, iltifât 0 · n=19 mora=94 harf=83 (n z=0,70), fâsıla صَٰدِقِينَ *(doğru söyleyenler)* → ن, N "
 "sınıfı; **i'râb ACC 4 · GEN 3 · NOM 1**; bab I x5 · IV x1; zaman IMPF x3 · IMPV x2 · PERF 1; "
 "**kök ikilemesi أله *(ilâh; lafza-i celâl)* x2**; **nakarat alanı: 0 — `أَمَّنْ` dizisinin BEŞİNCİ ve SON ayeti**; **dış "
 "düğüm 7 — blokta ve sûrede en yüksek** · yıldız ★ yok · kökler بدأ *(başlama)* · خلق *(yaratma)* · عود *(geri dönme)* · رزق *(rızık)* · سمو *(ad; gök)* · أرض *(yer, yeryüzü)* "
 "· أله *(ilâh; lafza-i celâl)* · قول *(söz söyleme)* · **هات *(getirin (getirme emri))*, n=4** · **برهن *(burhan, kesin delil)*, n=8** · "
 "كون *(olmak; mekân, yer)* · صدق *(doğruluk)* · bağ: xref هات *(getirin (getirme emri))* + برهان + كان ve برهان + كان + صادق → **2:111**; سماء + أرض *(yer, yeryüzü)* + إله → "
 "**7:158 · 35:3**; بدأ *(başlama)* + خلق *(yaratma)* + أعيد → **10:4 · 10:34 · 30:11 · 30:27** (elle, L2, aday 844/850)"),
65: ("eksen: **ALLAH LAFZI 10. sırada** (allah z=0,90) · Rab yok · esmâ yok · aktör yok · edim soru "
 "+ emir, kip IMPV 1 · **NEG 2** · RES 1 · INTG 1 · şahıs 2MS x1 · 3MS x1 · 3MP x4, iltifât 0 · "
 "n=14 mora=70 harf=56 (n z=0,17), fâsıla يُبْعَثُونَ *(diriltiliyorlar)* → ن, N sınıfı; **i'râb "
 "GEN 2 · ACC 1 · NOM 1**; **bab I x4**; zaman IMPV 1 · IMPF x3; **edilgen 1** (يُبْعَثُونَ), pas "
 "z=1,10; simetri [3,2,9,1]; **biçim HASR**; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · علم *(bilme)* · سمو *(ad; gök)* · "
 "أرض *(yer, yeryüzü)* · غيب *(gayb, görünmeyen)* · أله *(ilâh; lafza-i celâl)* · شعر *(şair; farkında olma)* · بعث *(gönderme; diriltme)* · bağ: **`أَمَّنْ` dizisi burada BİTİYOR ve kalıp değişiyor: قُلْ ile "
 "başlayan üç ayet geliyor (27:64'ün sonu, 27:65, 27:69)**; **شعر *(şair; farkında olma)* 27:50'den "
 "sonra sûrede ikinci geçiş** (elle, L1)"),
66: ("eksen: **lafız YOK — 27:59'dan beri ilk kez** · Rab yok · **esmâ آخِر *(âhiret; sonraki)* 5. "
 "sırada, ORTA konum, MÜHÜRSÜZ — ARTEFAKT**: gönderge ٱلْءَاخِرَة *(âhiret)*, bir ZAMAN/YER adı; "
 "sûrenin dört آخِر tokeninin DÖRDÜNCÜSÜ · aktör yok · edim haber · **şahıs 3MS x1 · 3MP x3 · 3FS "
 "x2, sahset ['3']** · n=14 mora=55 harf=47 (n z=0,17), fâsıla عَمُونَ *(körler)* → ن, N sınıfı; "
 "**i'râb NOM 2 · GEN 2**; **bab VI x1 — ayetin tek fiili**; zaman PERF 1; simetri [4,4,8,1]; "
 "**biçim IDRAB — ayette ÜÇ KEZ بَلْ, blokta ve sûrede en yoğun idrâb** · dış düğüm 0 · yıldız ★ "
 "yok · kökler درك *(yetişme, erişme)* · علم *(bilme)* · أخر *(geciktirme, sonraya bırakma)* · شكك *(şüphe)* · عمي *(körlük)* · bağ: **27:3, 27:4, 27:5'teki آخِر tokenleriyle aynı "
 "gönderge (âhiret) ve aynı hüküm: dördü de artefakt** (elle, L1, aday 846)"),
67: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, **kip INTG 2** · EMPH 1 · "
 "şahıs 3MS x1 · 3MP x2 · 1P x4, sahset ['1','3'], iltifât 0 · n=9 mora=67 harf=46 (n z=-0,36), "
 "fâsıla لَمُخْرَجُونَ *(çıkarılacak olanlar)* → ن, N sınıfı; **i'râb ACC 2 · NOM 2**; **bab I "
 "x3**; **zaman PERF x3**; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · كفر *(inkâr, nankörlük)* · كون *(olmak; mekân, yer)* · ترب *(toprak)* · أبو *(baba)* · خرج *(çıkma, çıkarma)* · "
 "bağ: **خرج *(çıkma, çıkarma)* sûrede dördüncü geçiş** (27:25 gizli olanın çıkarılması, 27:37 "
 "ordudan çıkarma, 27:56 şehirden çıkarma, burada topraktan çıkarılma); **dört geçiş, dört ayrı "
 "özne ve dört ayrı 'çıkarılan'** (elle, L1)"),
68: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip EMPH 1 · CERT 1 · NEG "
 "1 · RES 1 · **şahıs 1P x4, sahset ['1'] — blokta tek şahıslı tek ayet** · n=12 mora=69 harf=47 "
 "(n z=-0,04), fâsıla ٱلْأَوَّلِينَ *(öncekiler)* → ن, N sınıfı; **i'râb NOM 2 · GEN 2**; **bab I "
 "x1 — ayetin tek fiili ve o da EDİLGEN** (وُعِدْنَا *(bize vaat edildi)*); **edilgen oranı 1/1 = "
 "1,00 → pas z=5,38, KORPUS TAVANI**; simetri [4,1,6,1]; **biçim HASR + DIKKAT**; dış düğüm 1 · "
 "**yıldız ★★★ — kaynak YALNIZ edilgenlik** · kökler وعد *(vaat)* · أبو *(baba)* · قبل *(ön, önce; kabul)* · سطر *(satır, yazma; esâtîr (masallar))* · أول *(ilk, evvel)* · bağ: xref وعد *(vaat)* + "
 "آباء + قبل *(ön, önce; kabul)* ve türevleri → **ÜÇÜ DE 23:83** (elle, L1, aday 848)"),
69: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir, **kip IMPV 3** · şahıs 2MS "
 "x1 · 2MP x4 · 3MS x1, **iltifât 1 — yön 1>23; sûrenin ÜÇÜNCÜ ve SON iltifâtı** · n=9 mora=45 "
 "harf=41 (n z=-0,36), fâsıla ٱلْمُجْرِمِينَ *(suçlular)* → ن, N sınıfı; **i'râb GEN 2 · NOM 1**; "
 "**bab I x4**; zaman IMPV x3 · PERF 1; dış düğüm 1 · yıldız ★ yok · kökler قول *(söz söyleme)* · سير *(gidiş, hâl)* · أرض *(yer, yeryüzü)* · نظر *(bakma; mühlet verme)* "
 "· كيف *(nasıl, keyfiyet)* · كون *(olmak; mekân, yer)* · عقب *(sonuç, âkıbet)* · جرم *(suç işleme)* · bağ: xref كان + عاقبة + مجرم → **7:84**; **`كَيْفَ كَانَ عَٰقِبَةُ` "
 "kalıbı sûrede ÜÇÜNCÜ kez (27:14, 27:51, burada); korpusta 21 ayette; nakarat alanı ÜÇÜNDE DE 0** "
 "(elle, L2, aday 843/845)"),
70: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim yasak, kip NEG 1 · PRO 1 · şahıs "
 "3FS x1 · 3MP x3 · 2MS x1, iltifât 0 · n=9 mora=41 harf=33 (n z=-0,36), fâsıla يَمْكُرُونَ "
 "*(tuzak kuruyorlar)* → ن, N sınıfı; **i'râb GEN 1**; **bab I x3**; **zaman IMPF x3**; simetri "
 "[3,1,4,1]; **biçim NEHY**; dış düğüm 1 · yıldız ★ yok · kökler حزن *(hüzün, tasalanma)* · كون *(olmak; mekân, yer)* · ضيق *(darlık)* · مكر *(tuzak)* · bağ: xref "
 "يحزن + كان + ضيق *(darlık)* ve كان + ضيق *(darlık)* + مكر *(tuzak)* → **İKİSİ DE 16:127**; **مكر *(tuzak)* sûrede ALTINCI ve son "
 "okunan token** (27:50 x4, 27:51, burada) — üç ayette altı geçiş (elle, L1)"),
}

M = {
61: ("**Doğa bölütünün gövdesi başlıyor ve ölçülebilir bir yapı kuruyor: جعل *(kılma, var etme)* "
 "aynı ayette DÖRT kez**, her biri bir yer-yapısı için — karar yeri, ırmaklar, sabit dağlar, iki "
 "deniz arasında engel. **Sûrenin en 'yerbilimsel' ayeti bu ve YILDIZSIZ.** Aday 599/602/809 "
 "dizisine beşinci gösterim. Yeni kök حجز *(engel, perde (hâciz))* korpusta iki geçişli. Ve ayet "
 "`أَءِلَٰهٌ مَّعَ ٱللَّهِ` ile bitiyor — **`nakarat` alanı sıfır.** رسو *(sabit dağ)* korpusta on "
 "dört geçişli ve dikey satırı ▸sonra sarsılma ×452,9 veriyor; ölçüldü: **üç ayrı ayetten (16:15, "
 "21:31, 31:10) ve üçü de aynı kalıp** — 'yeri sarsmasın diye sabit dağlar' — yani aday 835'in "
 "Tür B'si."),
62: ("Dört fiil, dört ilâhî edim: karşılık verme, kötülüğü giderme, halife kılma. **Ölçülebilir bir "
 "karşıtlık ardışık ayetlerde: 27:61'in sayı alanı أَكْثَر *(çoğu)*, 27:62'ninki قَلِيل *(az)*** — "
 "aynı bölütte, aynı konumda (fâsıla öncesi), zıt nicelik. Ve **كشف *(giderme, açma)* 27:44'ten "
 "sonra sûrede ikinci geçiş: orada وَكَشَفَتْ عَن سَاقَيْهَا *(baldırlarını açtı)*, burada "
 "وَيَكْشِفُ ٱلسُّوٓءَ *(kötülüğü giderir)*** — aynı kök, iki anlam alanı, on sekiz ayet arayla. "
 "Dikey satırı yalnız 'zararı giderme' anlamından geliyor (zarar ×29,3 · مسس *(dokunma, temas)* ×19,0); **529 "
 "kümesinin sûre içi DÖRDÜNCÜ vakası ve ölçüt yine çalışmadı → 2/8.**"),
63: ("**İki lafız bir ayette ve yıldız eşiği kılpayı aşılmıyor: allah z=1,47.** Okunan ayetlerde "
 "yıldız veren en düşük z değerleri 1,55 (27:60) ve 1,57 (27:23); **eşik 1,5 civarında ve 27:63 "
 "tam altında kalıyor.** Bu, aday 827/837'nin üçüncü vakası: n=20 olduğu için iki lafız "
 "seyreliyor; 27:59'da n=12'de iki lafız z=2,80 vermişti. **Aynı eksen içeriği, ayet uzunluğuna "
 "göre ★★ ya da sıfır.** Esmâ tarafında بَرّ mühürsüz ve göndergesi ٱلْبَرِّ وَٱلْبَحْرِ *(kara ve "
 "deniz)*, yani bir yer adı — **ARTEFAKT; aday 818'in üçüncü sınaması da geçti.** Ve dış düğüm "
 "beş: ayetin rüzgâr-müjde terkibi korpusta 7:57 ve 25:48'de birebir."),
64: ("**`أَمَّنْ` dizisinin beşinci ve son ayeti; dizi kapandı: 27:60-64.** Ve kapanış bir delil "
 "talebiyle: هَاتُوا۟ بُرْهَٰنَكُمْ *(delilinizi getirin)*. **Ölçülebilir bir kalıp: هات *(getirin)* "
 "korpusta dört, برهن *(burhan, kesin delil)* sekiz geçişli ve ikisi DÖRT ayette birlikte (2:111, "
 "21:24, 27:64, 28:75) — karşılıklı kat ×914,0 ve ×810,8.** Aday 835'in Tür B'si: tek ayet değil, "
 "**tek KALIP, dört yerde.** Dış düğüm yedi — blokta ve sûrede en yüksek. **Not: sûrenin en çok "
 "dış bağı olan ayeti, hiçbir yıldız kaynağı taşımıyor.**"),
65: ("Kalıp burada değişiyor: `أَمَّنْ` dizisi bitti, قُلْ ile başlayan ayetler geliyor. Biçim HASR "
 "— لَا يَعْلَمُ ... إِلَّا ٱللَّهُ. **Ölçülebilir bir yapı: ayetin dört fiilinin dördü de birinci "
 "bab ve üçü muzari; tek edilgen fâsılada (يُبْعَثُونَ *(diriltiliyorlar)*)** ve pas z=1,10 ile "
 "eşiğin altında kalıyor. غيب *(gayb, görünmeyen)* korpusta altmış geçişli. **شعر *(farkında "
 "olma)* 27:50'den sonra sûrede ikinci geçiş ve ikisi de aynı yapıda: 'onlar farkında değil' — "
 "biri tuzak kuranlar için, biri diriliş için.**"),
66: ("**Üç kez بَلْ — blokta ve sûrede en yoğun idrâb.** Üç aşamalı bir iniş: bilgileri tükendi → "
 "şüphe içindeler → kördürler. **Ayetin tek fiili var ve o da bab VI** (ٱدَّٰرَكَ *(tükendi/erişti)*); "
 "درك *(yetişme, erişme)* korpusta on iki geçişli. Esmâ tarafında آخِر mühürsüz ve göndergesi "
 "ٱلْءَاخِرَة *(âhiret)*, bir zaman/yer adı — **ARTEFAKT; sûrenin dört آخِر tokeninin dördüncüsü ve "
 "dördü de aynı gönderge, aynı hüküm** (27:3, 27:4, 27:5, burada). **Aday 818'in dördüncü "
 "sınaması da geçti: mühürsüz tokende geçerlilik hâlâ 0/17.** Ve eksen burada kesiliyor: **27:59'dan "
 "beri her ayette lafız vardı, 27:66'da yok** — sûrenin ikinci eksen kümesi (27:59-65, yedi ayette "
 "yedi lafız) tam burada bitiyor."),
67: ("Diriliş itirazı bir soruyla: أَءِذَا كُنَّا تُرَٰبًا ... أَئِنَّا لَمُخْرَجُونَ *(toprak "
 "olduğumuzda ... çıkarılacak mıyız)*. **İki soru edatı tek ayette (INTG 2)** — blokta tek vaka. "
 "Ölçülebilir bir kök izi: **خرج *(çıkma, çıkarma)* sûrede dördüncü geçiş ve dört ayrı 'çıkarılan' "
 "veriyor**: 27:25 gizli olan, 27:37 ordudan çıkarılanlar, 27:56 şehirden çıkarılacak aile, burada "
 "topraktan çıkarılacak ölüler. **Kök tek anlam alanında ama nesnesi her seferinde başka bir "
 "katmanda.** ترب *(toprak)* korpusta yirmi iki geçişli ve dikey satırı ▸sonra نطف *(nutfe)* ×103,4 "
 "veriyor — dört ayrı ayetten (18:37, 22:5, 35:11, 40:67), yani yaratılış dizisi kalıbı."),
68: ("**Pas z korpus tavanına oturuyor: 5,38.** Ayetin tek fiili var ve o da edilgen (وُعِدْنَا "
 "*(bize vaat edildi)*), yani oran 1/1 = 1,00. **Ama tavan paylaşılıyor: korpusta 124 ayet aynı "
 "değerde** — yani z burada bir sıralama değil, bir doygunluk noktası. **★★★'ın kaynağı yalnız "
 "edilgenlik ve ★★★ bu blokta tek.** Ölçülebilir sonuç: **blokta yıldız veren tek şey, ayetin tek "
 "fiilinin çatısı.** Doğa bölütünün beş ayeti (27:60-64) toplam bir ★ almışken, bir inkâr "
 "cümlesi ★★★ alıyor — **aday 599/602'nin 'yıldız içeriği ölçmüyor' kaydına bu bloktan en keskin "
 "veri.** Ve xref: üç 3-gram'ın üçü de 23:83'e düşüyor, yani aynı itiraz korpusta birebir tekrar "
 "ediyor."),
69: ("**Sûrenin üçüncü ve son iltifâtı burada** (yön 1>23): قُلْ ... سِيرُوا۟ — tekil muhataba emir, "
 "sonra çoğula. Sûrenin üç iltifâtı: 27:6 (anlatı içi), 27:31 (alıntı sınırında), burası (emir "
 "zincirinde). **Üçü de farklı katmanda; aday 811'in sınıflandırma önerisine sûre içi tam küme.** "
 "Ve **`كَيْفَ كَانَ عَٰقِبَةُ` kalıbı sûrede ÜÇÜNCÜ kez: 27:14 (ٱلْمُفْسِدِينَ), 27:51 "
 "(مَكْرِهِمْ), burada (ٱلْمُجْرِمِينَ).** Korpusta yirmi bir ayette geçiyor. **`nakarat` alanı "
 "üçünde de sıfır** — sûrenin ikinci ayet-içi nakaratı ve alan yine kör."),
70: ("Blok bir yasakla kapanıyor: üzülme ve sıkıntıda olma. **مكر *(tuzak)* sûrede altıncı ve son "
 "okunan token** — 27:50'de dört, 27:51'de bir, burada bir; **üç ayette altı geçiş ve üçü de "
 "birbirine yirmi ayetlik bir yay içinde.** ضيق *(darlık)* korpusta on üç geçişli. Ve xref iki "
 "3-gram'ın ikisi de 16:127'ye düşüyor: **aynı iki yasak, aynı sırayla, başka bir sûrede birebir** "
 "— bu da bir donmuş kalıp. حزن *(hüzün, tasalanma)* dikey ölçümü ▸önce göz-aydınlığı ×70,9 "
 "veriyor, yani korpusta karşıtıyla birlikte anılıyor."),
}

ATLAMA = {
 "_mercek_27_68": ("27:68 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. Kaynak: pas z=5,38 (korpus tavanı; "
  "124 ayetle paylaşılıyor). Ayet bir İTİRAZ cümlesi: 'bu bize de babalarımıza da vaat edilmişti; "
  "öncekilerin masalları'. **Hiçbir doğal olgu, süreç, ölçü ya da sınıflandırma içermiyor.** "
  "Yıldızın tek kaynağı ayetin tek fiilinin edilgen olması. **Bu ayet, yıldız alanının içerikten "
  "bağımsız çalıştığının bu bloktaki en keskin örneği: doğa bölütünün beş ayeti toplam bir ★ "
  "alırken bir inkâr cümlesi ★★★ alıyor.**"),
 "_blok_notu_27_61_70": ("BLOK BİLANÇOSU: ★★★ 1 (27:68, kaynak PAS) · ★★ 0 · ★ 0 · yıldızsız 9. "
  "**Doğa bölütünün gövdesi (27:61-64) TAMAMEN YILDIZSIZ.** Kaynaklar: pas x1 — içerikten sıfır. "
  "İltifât 1/10 (27:69, sûrenin sonuncusu). Esmâ token 2, **ikisi de artefakt** (27:63 بَرّ, "
  "27:66 آخِر). Allah lafzı 6 (27:61, 62, 63 x2, 64, 65) · Rab 0 — **iki blok üst üste Rab yok.** "
  "Adlı aktör 0 · adsız aktör 0. Yeni kök 1 (حجز *(engel, perde (hâciz))*). Hapaks 0. Kafiye kırılması 0. **`nakarat` "
  "alanı 27:60-64'ün beşinde de SIFIR — sûrenin tek gerçek nakaratı ve alan görmüyor.** **Beş "
  "blok üst üste yıldızsız oran ≥%80.**"),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))

# --- DÜŞEN KAYIT ONARIMI (aday 843): 27:51 mercek metninde نظر *(bakma; mühlet verme)* sayımı yanlıştı ---
eski = "**نظر *(bakma; mühlet verme)* sûrede ALTINCI geçiş ve altısı da 'sonucu bekleme' bağlamında** — 27:27, 28, 33, 35, 41, 51."
yeni = ("**نظر *(bakma; mühlet verme)* sûrede YEDİNCİ geçiş** — 27:14, 27, 28, 33, 35, 41, 51. "
        "*(DÜZELTME, aday 843: bu satır önce 'altıncı geçiş' diyordu ve 27:14 atlanmıştı; "
        "27:14 de aynı `فَٱنظُرْ كَيْفَ كَانَ عَٰقِبَةُ` kalıbını taşıyor.)*")
if eski in OM['27']['27:51']['mercek']:
    OM['27']['27:51']['mercek'] = OM['27']['27:51']['mercek'].replace(eski, yeni)
    print('27:51 düzeltildi')
else:
    print('UYARI: 27:51 düzeltme dizgesi bulunamadı')

for n in range(61, 71):
    OM['27']["27:%d" % n] = {"ar": AR[(27, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["27:%d" % n]}
OM['27']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-26 TAM. **Sûre 27 (Neml) 70/93.** Devam: 27:71'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "27": "1-70 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 2019
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 27 →', len([k for k in OM['27'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
if eski in MK['27'].get('27:51', ''):
    MK['27']['27:51'] = MK['27']['27:51'].replace(eski, yeni)
for n in range(61, 71):
    MK['27']["27:%d" % n] = M[n]
MK['27_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 27 →', len(MK['27']))
