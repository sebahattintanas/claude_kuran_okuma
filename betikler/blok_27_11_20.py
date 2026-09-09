# -*- coding: utf-8 -*-
"""blok_27_11_20.py — sûre 27 ikinci blok (27:11-20). Süleymân bölütü ve karınca vadisi."""
import json
DIK = json.load(open('blok_dikey_27_11_20.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
11: "Ancak zulmeden, sonra kötülüğün ardından iyiliğe çeviren başka; ben bağışlayanım, merhametliyim.",
12: "Elini koynuna sok; kusursuz bembeyaz çıkar. Firavun'a ve kavmine dokuz âyet içinde. Onlar yoldan çıkmış bir kavimdi.",
13: "Âyetlerimiz gözler önüne serilerek onlara gelince dediler: Bu apaçık bir büyüdür.",
14: "Kendileri bunlara kesin olarak inandıkları hâlde zulüm ve büyüklenmeyle inkâr ettiler. Bozguncuların sonu nasıl olmuş, bir bak.",
15: "Andolsun, Dâvûd'a ve Süleymân'a ilim verdik. Dediler: Bizi mümin kullarının çoğundan üstün kılan Allah'a hamdolsun.",
16: "Süleymân Dâvûd'a vâris oldu. Dedi: Ey insanlar, bize kuş dili öğretildi ve bize her şeyden verildi. Bu, apaçık bir lütuftur.",
17: "Süleymân'a cinlerden, insanlardan ve kuşlardan orduları toplandı; hepsi düzenli sevk ediliyordu.",
18: "Karınca vadisine geldiklerinde bir karınca dedi: Ey karıncalar, yuvalarınıza girin; Süleymân ve orduları farkında olmadan sizi ezmesin.",
19: "Onun sözüne gülümseyerek güldü ve dedi: Rabbim, bana ve anne babama verdiğin nimete şükretmemi, senin razı olacağın sâlih amel işlememi bana nasip et; beni rahmetinle sâlih kullarının arasına kat.",
20: "Kuşları gözden geçirdi ve dedi: Neden hüdhüdü göremiyorum? Yoksa kayıplardan mı oldu?",
}

O = {
11: ("eksen: **lafız YOK · Rab YOK** · **esmâ غَفُور *(bağışlayan)* 10. + رَحِيم *(merhametli)* 11. "
 "sırada = fâsıla — MÜHÜR; GEÇERLİ; sûrenin altı mühründen ÜÇÜNCÜSÜ ve ÜÇÜNCÜ FARKLI ÇİFT** · "
 "aktör yok · edim haber, kip RES 1 · şahıs 3MS x2 · 1S x1, iltifât 0 · n=11 mora=53 harf=39 "
 "(n z=-0,15), fâsıla رَّحِيمٌ *(merhametli)* → م, N sınıfı; **i'râb ACC 3 · GEN 1 · NOM 2**; "
 "bab I x1 · II x1; zaman PERF x2; **biçim HASR**; dış düğüm 0 · yıldız ★ yok · kökler ظلم *(zulüm, "
 "karanlık)* · بدل *(değiştirme)* · حسن *(güzellik, iyilik)* · بعد *(sonra; uzaklık)* · سوأ "
 "*(kötülük)* · غفر *(bağışlama, mağfiret)* · رحم *(rahmet, merhamet)* · bağ: **27:6 ve 27:9 ile "
 "MÜHÜR ÇEŞİTLİLİĞİ ÜÇE ÇIKTI** — حَكِيم|عَلِيم, عَزِيز|حَكِيم, غَفُور|رَحِيم; beş ayet içinde üç "
 "ayrı çift. **Sûre 26'da on mühürden dokuzu TEK çiftti** (aday 771/787) (elle, L1, aday 789)"),
12: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı فِرْعَوْن *(Firavun)* 14. sırada, "
 "rol mecrur** · edim emir, kip IMPV 1 · şahıs 2MS x3 · 3FS x1 · 3MS x1 · 3MP x3, iltifât 0 · "
 "**n=19 — blokta en uzun ayetlerden** (n z=0,70), fâsıla فَٰسِقِينَ *(yoldan çıkmışlar)* → ن, N "
 "sınıfı; **i'râb ACC 5 · GEN 7**; bab I x2 · IV x1; zaman IMPV 1 · IMPF 1 · PERF 1; **kök "
 "ikilemesi قوم *(kalkma; kavim; kıyamet)* x2**; **AÇIK SAYI SÖZCÜĞÜ: تسع *(dokuz)* → تِسْع** — "
 "okumada net bir sayı adı; simetri [3,13,16,1]; **dış düğüm 2** · yıldız ★ yok · kökler دخل "
 "*(girme)* · يدي *(el)* · جيب *(yaka, göğüs yarığı)* · خرج *(çıkma, çıkarma)* · بيض *(beyazlık)* · "
 "غير *(başka)* · سوأ *(kötülük)* · تسع *(dokuz)* · أيي *(âyet, işaret)* · قوم *(kalkma; kavim; "
 "kıyamet)* · كون *(olmak; mekân, yer)* · فسق *(fâsıklık)* · bağ: xref DÖRT 3-gram → **20:22 · "
 "28:32**; **تسع *(dokuz)* dikey ölçümü ▸sonra نعج *(dişi koyun)* x948,5 veriyor — OKUMADA GÖRÜLEN "
 "EN YÜKSEK KOMŞULUK KATI** (önceki rekor 26:181'in x661,4'üydü); kaynak 38:23'teki 'doksan dokuz "
 "dişi koyun' sahnesi — **aday 776'nın beşinci ve en uç vakası** (elle, L1, aday 790)"),
13: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُبِين *(apaçık)* 8. sırada = fâsıla, MÜHÜRSÜZ — "
 "ARTEFAKT**: gönderge سِحْر *(büyü)*; sûrenin altı مُبِين tokeninin ikincisi · aktör yok · edim "
 "haber, kip işareti yok · şahıs 3FS x1 · 3MP x3 · 1P x1, iltifât 0 · n=8 mora=54 harf=40 "
 "(n z=-0,47), fâsıla مُّبِينٌ *(apaçık)* → ن, N sınıfı; **i'râb NOM 3 · ACC 1**; bab I x2; zaman "
 "PERF x2; **biçim DIKKAT**; dış düğüm 0 · yıldız ★ yok · kökler جيأ *(gelme)* · أيي *(âyet, "
 "işaret)* · بصر *(görme, basîret)* · قول *(söz söyleme)* · سحر *(büyü, sihir)* · بين *(arası; "
 "açıklama)* · bağ: **26:34 ile سحر *(büyü, sihir)* karşılaştırması** — orada سَٰحِرٌ عَلِيمٌ "
 "*(bilgili büyücü)* elçinin niteliğiydi, burada سِحْرٌ مُّبِينٌ *(apaçık büyü)* âyetlerin "
 "niteliği; **aynı kök, kişiden olaya**; **ve مُبِين ikisinde de esmâ artefaktı** (elle, L1, "
 "aday 791)"),
14: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir, kip IMPV 1 · şahıs 3MP x3 · "
 "3FS x3 · 2MS x1 · 3MS x1, iltifât 0 · n=11 mora=71 harf=61 (n z=-0,15), fâsıla ٱلْمُفْسِدِينَ "
 "*(bozguncular)* → ن, N sınıfı; **i'râb NOM 2 · ACC 2 · GEN 1**; bab I x3 · **bab X x1**; zaman "
 "PERF x3 · IMPV 1; **dış düğüm 2** · yıldız ★ yok · kökler جحد *(inkâr, bile bile reddetme)* · "
 "يقن *(yakîn, kesin bilgi)* · نفس *(nefis, kişi)* · ظلم *(zulüm, karanlık)* · علو *(yücelik, "
 "üstünlük)* · نظر *(bakma; mühlet verme)* · كيف *(nasıl, keyfiyet)* · كون *(olmak; mekân, yer)* · "
 "عقب *(sonuç, âkıbet)* · فسد *(bozgunculuk, fesat)* · bağ: xref كان *(oldu)* + عاقبة *(sonuç)* + "
 "مفسد *(bozguncu)* → **7:86 · 7:103**; **27:3 ile يقن *(yakîn, kesin bilgi)* karşıtlığı** — orada "
 "müminler âhirete يُوقِنُونَ *(kesin inanırlar)*, burada inkârcılar âyetlere ٱسْتَيْقَنَتْهَآ "
 "أَنفُسُهُمْ *(içleri kesin olarak inanmışken)* inkâr ediyor; **aynı kök, iki kutup ve ikincisi "
 "bab X** (elle, L1, aday 792)"),
15: ("eksen: **ALLAH LAFZI 8. sırada — sûrenin üçüncü lafzı** (allah z=0,81) · Rab yok · **esmâ "
 "مُؤْمِن *(mümin)* 15. sırada = fâsıla, MÜHÜRSÜZ — ARTEFAKT**: gönderge KULLAR; sûrenin üç "
 "مُؤْمِن tokeninin ikincisi · **aktör: adlı داوُد *(Dâvûd)* 3. + سُلَيْمان *(Süleymân)* 4. "
 "sırada, ikisi de rol mecrur — SÜLEYMÂN BÖLÜTÜ AÇILIYOR** · edim haber, kip EMPH 1 · CERT 1 · "
 "şahıs 1P x3 · 3MD x2 · 3MS x2, iltifât 0 · n=15 mora=88 harf=72 (n z=0,27), fâsıla "
 "ٱلْمُؤْمِنِينَ *(müminler)* → ن, N sınıfı; **i'râb GEN 6 · ACC 1 · NOM 1**; bab I x1 · II x1 · "
 "IV x1; zaman PERF x3; **açık sayı sözcüğü: كثر *(çokluk)* → كَثِير**; simetri [3,1,9,1]; "
 "**dış düğüm 1** · yıldız ★ yok · kökler أتي *(gelme, getirme)* · علم *(bilme)* · قول *(söz "
 "söyleme)* · حمد *(hamd, övgü)* · أله *(ilâh; lafza-i celâl)* · فضل *(üstün kılma, lütuf)* · كثر "
 "*(çokluk)* · عبد *(kul, kulluk)* · أمن *(güven; iman)* · bağ: xref آتى *(verdi)* + علم *(ilim)* + "
 "قال *(dedi)* → **47:16**; **26:21 ve 26:83 ile 'verilen şey' karşılaştırması** — orada حُكْم "
 "*(hüküm)* bağışlanıyordu, burada عِلْم *(ilim)*; **aynı yapı (fiil + لِ + soyut ad), farklı "
 "nesne** (elle, L1, aday 793)"),
16: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُبِين = fâsıla — ARTEFAKT, üçüncü token**: gönderge "
 "فَضْل *(lütuf)* · **aktör: adlı سُلَيْمان *(Süleymân)* 2. sırada rol FAİL, داوُد *(Dâvûd)* 3. "
 "sırada rol MEF'ÛL** · edim nida, kip VOC 1 · EMPH 1 · şahıs 3MS x3 · 1P x4, iltifât 0 · **n=18 — "
 "blokta ikinci en uzun ayet** (n z=0,59), fâsıla ٱلْمُبِينُ *(apaçık)* → ن, N sınıfı; **i'râb "
 "NOM 4 · ACC 4 · GEN 3**; bab I x2 · II x1 · IV x1; zaman PERF x4; **edilgen 2 — عُلِّمْنَا "
 "*(bize öğretildi)* ve أُوتِينَا *(bize verildi)*; dört fiilden ikisi edilgen, oran 0,50**, "
 "pas z=2,52: **yıldızın TEK kaynağı**; **biçim DIKKAT**; simetri [3,2,14,1]; **dış düğüm 1 · iç "
 "düğüm 1** · **yıldız ★★** · kökler ورث *(vâris olma)* · قول *(söz söyleme)* · أيي *(âyet, "
 "işaret)* · أنس *(insan)* · علم *(bilme)* · نطق *(konuşma, söz söyleme)* · طير *(kuş; uçan)* · "
 "أتي *(gelme, getirme)* · كلل *(hep, bütün)* · شيأ *(dileme; şey)* · فضل *(üstün kılma, lütuf)* · "
 "بين *(arası; açıklama)* · bağ: xref آتى *(verdi)* + كلّ *(her)* + شىء *(şey)* → **18:84 · 27:23**; "
 "**نطق *(konuşma, söz söyleme)* korpusta 12 geçişli; مَنطِقَ ٱلطَّيْرِ *(kuş dili)* terkibi "
 "korpusta TEK** (elle, L1, aday 794)"),
17: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı سُلَيْمان *(Süleymân)* 2. sırada, "
 "rol mecrur** · edim haber, kip işareti yok · şahıs 3MS x2 · 3MP x3, iltifât 0 · n=9 mora=50 "
 "harf=43 (n z=-0,36), fâsıla يُوزَعُونَ *(düzenli sevk ediliyorlar)* → ن, N sınıfı; **i'râb GEN 4 · "
 "NOM 1**; bab I x2; zaman PERF 1 · IMPF 1; **edilgen 2 — حُشِرَ *(toplandı)* ve يُوزَعُونَ; "
 "ayetin İKİ fiili de edilgen, oran 1,00**, pas z=5,38: **yıldızın TEK kaynağı**; dış düğüm 0 · "
 "**yıldız ★★★** · kökler حشر *(toplama, mahşer)* · جند *(ordu, asker)* · جنن *(örtme, gizleme; "
 "cennet; cin)* · أنس *(insan)* · طير *(kuş; uçan)* · وزع *(dizip düzenleme; ilham verme)* · bağ: "
 "**26:38 ve 26:39 ile حشر *(toplama, mahşer)* karşılaştırması** — orada büyücüler ve halk "
 "toplanıyordu (فَجُمِعَ, جمع kökü), burada üç sınıflı bir ordu (حشر kökü); **iki ayrı kök, aynı "
 "'toplanma' alanı**; **وزع *(dizip düzenleme; ilham verme)* korpusta BEŞ geçişli ve dikey ölçümü "
 "▸sonra nimet x61,8 veriyor — 27:19'un kökü, iki ayet sonra** (elle, L1, aday 795)"),
18: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — نَمْلَة *(karınca)* aktör tablosuna "
 "GİRMİYOR; **adlı aktörü سُلَيْمان *(Süleymân)* 15. sırada, rol FAİL** · edim emir + nida, kip "
 "VOC 1 · IMPV 1 · NEG 2 · EMPH 1 · şahıs 3MP x5 · 3FS x1 · 2MP x4 · 3MS x2, iltifât 0 · **n=19 — "
 "blokta en uzun ayetlerden** (n z=0,70), fâsıla يَشْعُرُونَ *(farkına varıyorlar)* → ن, N sınıfı — "
 "**26:202'nin fâsılasıyla AYNI KELİME**; **i'râb GEN 2 · NOM 4 · ACC 2**; **bab I x5**; zaman "
 "PERF x2 · IMPV 1 · IMPF x2; **kök ikilemesi نمل *(karınca)* x3 — SÛRENİN ADINI VEREN KÖK TEK "
 "AYETTE ÜÇ KEZ**; **biçim DIKKAT**; simetri [3,1,17,1]; dış düğüm 0 · **yıldız ★ YOK** · kökler "
 "أتي *(gelme, getirme)* · ودي *(vâdi)* · نمل *(karınca)* · قول *(söz söyleme)* · أيي *(âyet, "
 "işaret)* · دخل *(girme)* · سكن *(sükûn; mesken, konut)* · حطم *(ezme, kırma)* · جند *(ordu, "
 "asker)* · شعر *(şair; farkında olma)* · bağ: **26:225 İLE DOĞRULAMA** — orada ودي *(vâdi)* "
 "dikey ölçümü ▸sonra نمل *(karınca)* x534,8 vermişti ve 'kaynak 27:18'deki karınca vadisi "
 "sahnesi' demiştim (aday 776); **burada doğrulandı**: نمل ▸önce vadi x520,0, karşılıklı bağ "
 "(elle, L1, aday 796)"),
19: ("eksen: **lafız YOK · رَبّ *(Rab)* 6. sırada — sûrenin ikinci Rabbi** (rab z=0,57) · esmâ "
 "yok · aktör yok · edim emir, kip IMPV 2 · **şahıs 2MS x8 · 1S x7** · 3MS x3 · 3FS x1, iltifât "
 "0 · **n=24 — SÛRENİN OKUNAN EN UZUN AYETİ** (n z=1,23), fâsıla ٱلصَّٰلِحِينَ *(sâlihler)* → ن, "
 "N sınıfı — **26:83'ün fâsılasıyla AYNI KELİME**; **i'râb ACC 4 · GEN 5**; bab I x4 · IV x3 · "
 "V x1; zaman PERF x3 · IMPV x2 · IMPF x3; **HAPAKS: بسم *(gülümseme (tebessüm))* — korpusta TEK "
 "geçiş** (hapaks z=3,38: **yıldızın TEK kaynağı**); **ÜÇ KÖK BİRDEN İKİLENİYOR: قول *(söz "
 "söyleme)* x2 · نعم *(nimet; davar)* x2 · صلح *(iyi, elverişli olma; ıslah)* x2 — OKUMADA İLK "
 "KEZ ÜÇ KÖK**; simetri [3,11,14,1]; **dış düğüm 2** · **yıldız ★★★** · bağ: xref **DOKUZ 3-gram → "
 "sekizi 46:15'e** — okumada bir ayetin tek ayete en çok bağla bağlandığı ikinci yer (birincisi "
 "27:10, altı bağ); **26:83 ile dua yapısı** — orada رَبِّ هَبْ لِى … وَأَلْحِقْنِى "
 "بِٱلصَّٰلِحِينَ *(Rabbim bana bağışla … beni sâlihlere kat)*, burada رَبِّ أَوْزِعْنِىٓ … "
 "وَأَدْخِلْنِى … فِى عِبَادِكَ ٱلصَّٰلِحِينَ; **iki elçi, iki emir, aynı fâsıla** (elle, L1, "
 "aday 797)"),
20: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · NEG 1 · şahıs "
 "3MS x3 · 1S x2, iltifât 0 · n=12 mora=59 harf=44 (n z=-0,04), fâsıla ٱلْغَآئِبِينَ *(kayıplar)* → "
 "ن, N sınıfı; **i'râb ACC 2 · GEN 1**; bab I x3 · **bab V x1**; zaman PERF x3 · IMPF 1; **HAPAKS: "
 "هدهد *(hüdhüd (ibibik))* — korpusta TEK geçiş** (hapaks z=3,38: **yıldızın TEK kaynağı**); "
 "simetri [3,4,9,1]; dış düğüm 0 · **yıldız ★★★** · kökler فقد *(yitirme, yoklamada bulamama)* · "
 "طير *(kuş; uçan)* · قول *(söz söyleme)* · رأي *(görme)* · هدهد *(hüdhüd (ibibik))* · كون *(olmak; "
 "mekân, yer)* · غيب *(gayb, görünmeyen)* · bağ: **27:16 ve 27:17 ile طير *(kuş; uçan)* ÜÇÜNCÜ "
 "geçişi** — 27:16 kuş DİLİ, 27:17 kuş ORDUSU, burada tek bir kuşun YOKLUĞU; **üç ayet, üç ölçek: "
 "dil / topluluk / birey**; **فقد *(yitirme, yoklamada bulamama)* korpusta ÜÇ geçişli** (elle, L1, "
 "aday 798)"),
}

M = {
11: ("İstisna bir dönüşüm koşuluyla: بَدَّلَ حُسْنا بَعْدَ سُوٓءٍ *(kötülüğün ardından iyiliğe "
 "çeviren)*. Ve **sûrenin üçüncü mührü burada: غَفُور|رَحِيم, geçerli.** Ölçülebilir bir "
 "çeşitlilik: beş ayet içinde **üç ayrı mühür çifti** — 27:6 حَكِيم|عَلِيم, 27:9 عَزِيز|حَكِيم, "
 "burada غَفُور|رَحِيم. **Sûre 26'da on mühürden dokuzu tek çiftti ve sekizi tek ayetin "
 "tekrarıydı** (aday 771); burada üç mühür, üç ayrı çift, tekrar yok. بدل *(değiştirme)* korpusta "
 "44 geçişli."),
12: ("**Okumada net bir sayı adı: تِسْعَ ءَايَٰتٍ *(dokuz âyet)*.** Ve **dikey ölçüm okumadaki en "
 "yüksek komşuluk katını veriyor: تسع *(dokuz)* ▸sonra نعج *(dişi koyun)* x948,5** — önceki rekor "
 "26:181'in x661,4'üydü. **Kaynak 38:23'teki 'doksan dokuz dişi koyun' sahnesi; kök korpusta yedi "
 "geçişli ve kat tek bir sahneden geliyor** — aday 776'nın beşinci ve en uç vakası. Dört xref "
 "20:22 ve 28:32'ye düşüyor; **el-koyun-beyazlık sahnesi korpusta üç sûrede aynı sözcüklerle**. "
 "Ve بيض *(beyazlık)* dikey ölçümü ▸önce يدي *(el)* x21,4 veriyor — çift bağlı. **SINIR: ayet bir "
 "sayı veriyor (dokuz) ama neyin sayısı olduğu dışında ölçü yok; çıpa sayılmadı.**"),
13: ("Âyetlerin karşılanışı tek bir nitelemeyle: هَٰذَا سِحْرٌ مُّبِينٌ *(bu apaçık bir büyüdür)*. "
 "Ölçülebilir bir kaydırma: 26:34'te سَٰحِرٌ عَلِيمٌ *(bilgili büyücü)* **elçinin** niteliğiydi, "
 "burada سِحْرٌ مُّبِينٌ **âyetlerin** niteliği — aynı kök, **kişiden olaya**. **Ve مُبِين ikisinde "
 "de esmâ artefaktı**: 26:34'te gönderge büyücü, burada büyü. بصر *(görme, basîret)* korpusta 148 "
 "geçişli; مُبْصِرَة *(gözler önüne serilmiş)* burada âyetlerin niteliği."),
14: ("İnkâr bir çelişkiyle anlatılıyor: وَجَحَدُوا۟ بِهَا وَٱسْتَيْقَنَتْهَآ أَنفُسُهُمْ *(içleri "
 "kesin olarak inanmışken inkâr ettiler)*. **Ölçülebilir bir kutup karşıtlığı: يقن *(yakîn, kesin "
 "bilgi)* 27:3'te müminlerin niteliğiydi (يُوقِنُونَ), burada inkârcıların iç hâli ve bab X** — "
 "aynı kök, iki kutup, on bir ayet arayla. جحد *(inkâr, bile bile reddetme)* korpusta 12 geçişli. "
 "Tek xref iki ayete düşüyor (7:86, 7:103) ve terkip orada da aynı — donmuş kalıp adayı."),
15: ("**Süleymân bölütü açılıyor** ve iki ad birlikte: دَاوُۥدَ وَسُلَيْمَٰنَ. Ölçülebilir bir "
 "karşılaştırma: 26:21 ve 26:83'te verilen/istenen şey حُكْم *(hüküm)* idi, burada عِلْم *(ilim)* — "
 "**aynı yapı (fiil + لِ + soyut ad), farklı nesne**; ve burada verme gerçekleşmiş (PERF, 1P). "
 "Sûrenin üçüncü lafzı burada ve bir HAMD cümlesinde: ٱلْحَمْدُ لِلَّهِ. Ve fâsıladaki مُؤْمِن "
 "esmâ sayılmış — sûrenin üç مُؤْمِن tokeninin ikincisi ve gönderge kullar; **27:2'de de artefakt "
 "çıkmıştı**."),
16: ("Vâris olma ve iki edilgen: عُلِّمْنَا مَنطِقَ ٱلطَّيْرِ *(bize kuş dili öğretildi)* ve "
 "أُوتِينَا مِن كُلِّ شَىْءٍ *(bize her şeyden verildi)*; oran 0,50 → pas z=2,52, yıldızın tek "
 "kaynağı. **نطق *(konuşma, söz söyleme)* korpusta 12 geçişli ve مَنطِقَ ٱلطَّيْرِ terkibi korpusta "
 "TEK.** Ve طير *(kuş; uçan)* dikey ölçümü ▸önce şekil-biçim x474,2 veriyor — kök korpusta ağırlıkla "
 "'kuş biçimi verme' bağlamında (3:49, 5:110), burada gerçek kuşlar. **SINIR — ÇIPA DEĞERLENDİRMESİ: "
 "ayet bir canlı sınıfını (kuş) ve bir yetiyi (dil) ADLANDIRIYOR; ne mekanizma, ne ölçü, ne "
 "sınıflandırma. 25:61 düzeyinde 'adlandırma + nitelik'. Ve ayet ★★, ★★★ eşiği aşılmadığı için "
 "mercek zaten yazılamaz.**"),
17: ("**Ayetin iki fiili de edilgen** (حُشِرَ *(toplandı)*, يُوزَعُونَ *(düzenli sevk ediliyorlar)*), "
 "oran 1,00 → pas z=5,38, yıldızın tek kaynağı. Ölçülebilir bir kök seçimi: 26:38-39'da toplanma "
 "جمع *(toplama, cem)* köküyle veriliyordu (büyücüler ve halk), burada حشر *(toplama, mahşer)* "
 "köküyle — **iki ayrı kök, aynı alan**; 26:16↔26:18 ve 26:42↔26:58 desenıyle aynı sınıf ama bu kez "
 "**iki sûre arasında**. Ve وزع *(dizip düzenleme; ilham verme)* korpusta **beş** geçişli; dikey "
 "ölçümü ▸sonra nimet x61,8 veriyor — **27:19'un kökü, iki ayet sonra**; aynı kök 27:19'da 'ilham "
 "verme' anlamında gelecek."),
18: ("**Sûrenin adını veren kök tek ayette üç kez: نمل *(karınca)* x3.** Ve **26:225'teki tahminim "
 "burada doğrulandı**: orada ودي *(vâdi)* dikey satırı ▸sonra نمل x534,8 vermişti ve *'kaynak "
 "27:18'deki karınca vadisi sahnesi'* demiştim (aday 776); burada نمل ▸önce vadi x520,0 — "
 "**karşılıklı bağ ve iki kat da tek sahneden**. سكن *(sükûn; mesken, konut)* ▸önce karınca x99,1 "
 "veriyor: **üçlü kilit.** حطم *(ezme, kırma)* korpusta altı geçişli ve dikey satırı iki listede "
 "de boş. **SINIR — ÇIPA DEĞERLENDİRMESİ: ayet bir canlı sınıfını (karınca), bir yaşam alanını "
 "(mesken) ve bir davranışı (girme, ezilmeden korunma) ADLANDIRIYOR — 'adlandırma + nitelik' "
 "düzeyinin biraz üstünde, bir DAVRANIŞ dizisi var. Ama ne mekanizma, ne ölçü, ne sınıflandırma. "
 "VE AYET YILDIZSIZ — sûrenin biyolojiye en yakın ayeti ve yıldız almıyor** (aday 599/602 "
 "tablosuna)."),
19: ("**Sûrenin okunan en uzun ayeti** (n=24) ve üç uç değer: **2MS x8 · 1S x7**; **üç kök birden "
 "ikileniyor — قول *(söz söyleme)*, نعم *(nimet; davar)*, صلح *(iyi, elverişli olma; ıslah)*; "
 "okumada ilk kez üç kök**; ve **dokuz 3-gram'ın sekizi 46:15'e düşüyor** — okumada bir ayetin tek "
 "ayete en çok bağla bağlandığı ikinci yer (birincisi 27:10, altı bağ). Yıldızın tek kaynağı hapaks "
 "بسم *(gülümseme (tebessüm))*. Ve ضحك *(gülme)* dikey ölçümü ▸sonra بكي *(ağlama)* x312,2 veriyor "
 "— karşıt çift korpusta kilitli, burada karşıtı yok (aday 664 sınıfı). **26:83 ile dua "
 "karşılaştırması:** orada İbrâhîm iki emirle (هَبْ *(bağışla)* + أَلْحِقْنِى *(kat)*), burada "
 "Süleymân iki emirle (أَوْزِعْنِى *(nasip et)* + أَدْخِلْنِى *(kat)*) — **iki elçi, aynı "
 "iki-emirli yapı, aynı fâsıla** (ٱلصَّٰلِحِينَ)."),
20: ("Soru bir yoklama sahnesinde: وَتَفَقَّدَ ٱلطَّيْرَ *(kuşları gözden geçirdi)*. **Ölçülebilir "
 "bir ölçek dizisi: طير *(kuş; uçan)* üç ayette üç ölçekte** — 27:16 kuş **dili** (yeti), 27:17 kuş "
 "**ordusu** (topluluk), burada tek bir kuşun **yokluğu** (birey). Yıldızın tek kaynağı hapaks "
 "هدهد *(hüdhüd (ibibik))*; kök korpusta **tek** geçiş ve dikey satırı iki listede de boş. فقد "
 "*(yitirme, yoklamada bulamama)* korpusta **üç** geçişli. **SINIR: ayet bir kuş türünü "
 "ADLANDIRIYOR ve bir yoklama eylemi bildiriyor; ne betimleme, ne ölçü, ne davranış. "
 "'Adlandırma' düzeyinin altında — 26:128'in ريع vakasıyla aynı sınıf.**"),
}

ATLAMA = {
 "_mercek_27_17_19_20": ("27:17, 27:19, 27:20 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. Kaynaklar: 27:17 "
  "pas z=5,38 (iki fiil de edilgen, oran 1,00) · 27:19 hapaks z=3,38 (بسم *(gülümseme)*) · 27:20 "
  "hapaks z=3,38 (هدهد *(hüdhüd)*). **ÜÇÜNDE DE ÇIPA YOK ve bu, sûrenin en 'canlı' bölütünde "
  "oluyor:** 27:16 kuş dili, 27:17 kuş ordusu, 27:18 karınca vadisi, 27:20 hüdhüd. **27:20 bir kuş "
  "TÜRÜNÜ adlandırıyor ama betimleme yok — 'adlandırma' düzeyinin altında (26:128'in ريع vakası "
  "sınıfı). 27:19 bir DUYGU ifadesi (gülümseme) ve yine betimleme yok.**"),
 "_blok_notu_27_11_20": ("BLOK BİLANÇOSU: ★★★ 3 (27:17, 19, 20) · ★★ 1 (27:16) · ★ 0 · 6 ayet "
  "yıldızsız. Kaynaklar: pas x2 · hapaks x2 — hiçbiri içerikten. **ÇIPA TABLOSU — SÛRENİN "
  "BİYOLOJİYE EN YAKIN BÖLÜTÜ VE YILDIZ DAĞILIMI TERS: 27:16 (kuş dili, adlandırma+nitelik) ★★ · "
  "27:17 (üç sınıflı ordu) ★★★ ama kaynak edilgenlik · 27:18 (KARINCA VADİSİ — canlı sınıfı + "
  "yaşam alanı + davranış dizisi, sûrenin EN GÜÇLÜ çıpa adayı) YILDIZSIZ · 27:19 (gülümseme) ★★★ "
  "hapakstan · 27:20 (hüdhüd adı) ★★★ hapakstan.** Yani **çıpası en güçlü ayet yıldızsız, çıpası "
  "olmayan iki ayet ★★★** — aday 599/602'nin sûre 27'deki ilk ve en temiz gösterimi."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(11, 21):
    OM['27']["27:%d" % n] = {"ar": AR[(27, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["27:%d" % n]}
OM['27']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-26 TAM. **Sûre 27 (Neml) 20/93.** Devam: 27:21'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "27": "1-20 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1969
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 27 →', len([k for k in OM['27'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(11, 21):
    MK['27']["27:%d" % n] = M[n]
MK['27_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 27 →', len(MK['27']))
