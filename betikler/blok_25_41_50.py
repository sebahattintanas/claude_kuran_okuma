# -*- coding: utf-8 -*-
"""blok_25_41_50.py — sûre 25 beşinci blok (25:41-50).
Sûrenin en yoğun doğa bölütü VE on ayetin onu da yıldızsız."""
import json
DIK = json.load(open('blok_dikey_25_41_60.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
41: "Seni gördüklerinde yalnızca alaya alıyorlar: Allah'ın elçi olarak gönderdiği bu mu?",
42: "Onlara sabretmeseydik neredeyse bizi ilâhlarımızdan saptıracaktı. Azabı görecekleri zaman kimin yolca daha sapkın olduğunu bilecekler.",
43: "Hevâsını kendine ilâh edineni gördün mü? Ona sen mi vekil olacaksın?",
44: "Yoksa onların çoğunun işittiğini ya da akıl ettiğini mi sanıyorsun? Onlar ancak davarlar gibidir; hatta yolca daha sapkındırlar.",
45: "Rabbini görmedin mi, gölgeyi nasıl uzattı? Dileseydi onu durgun kılardı. Sonra güneşi ona bir delil kıldık.",
46: "Sonra onu kolay bir kabzedişle kendimize çektik.",
47: "Geceyi size bir giysi, uykuyu bir dinlenme, gündüzü de bir kalkış kılan odur.",
48: "Rahmetinin önünde rüzgârları müjdeci olarak gönderen odur. Ve gökten tertemiz bir su indirdik.",
49: "Onunla ölü bir beldeyi diriltelim ve yarattıklarımızdan birçok davarı ve insanı onunla sulayalım diye.",
50: "Andolsun, düşünsünler diye onu aralarında türlü türlü açıkladık; ama insanların çoğu nankörlükte direndi.",
}

OLCUM = {
41: ("eksen: **ALLAH LAFZI 10. sırada — sûrenin İKİNCİ lafzı** (allah z=1,29; **yıldız eşiğini "
 "AŞMIYOR, ayet ★ almıyor**) · Rab yok · esmâ yok · aktör yok · edim soru, kip NEG 1 · RES 1 · "
 "INTG 1 · şahıs 3MP x4 · 2MS x2 · 3MS x1, iltifât 0 · n=11 mora=60 harf=44 (n z=-0,15), fâsıla "
 "رَسُولا *(elçi)* → ا, A sınıfı, ACC; i'râb ACC 2 · NOM 1; bab I x2 · VIII x1; zaman PERF x2 · "
 "IMPF x1; **biçim HASR + DIKKAT**; simetri [3,1,5,1]; dış düğüm 0 · yıldız ★ yok · kökler رأي "
 "*(görme)* · أخذ *(alma, edinme)* · هزأ *(alay etme)* · بعث *(gönderme, diriltme)* · أله *(ilâh; "
 "lafza-i celâl)* · رسل *(gönderme, elçi)* · bağ: **25:7 ile aynı itiraz, farklı kip** — orada "
 "مَالِ هَٰذَا ٱلرَّسُولِ *(bu ne biçim elçi)*, burada أَهَٰذَا ٱلَّذِى بَعَثَ ٱللَّهُ رَسُولا "
 "*(Allah'ın elçi olarak gönderdiği bu mu)*; **ve itiraz ilk kez Allah lafzını KENDİ AĞZINDA "
 "kullanıyor** (elle, L1, aday 562)"),
42: ("eksen: **lafız YOK · Rab YOK**; أله *(ilâh; lafza-i celâl)* kökü var ama ÇOĞUL ve iyelikli — "
 "ءَالِهَتِنَا *(ilâhlarımız)* · esmâ yok · aktör yok · edim şart, kip COND 2 · EMPH 1 · FUT 1 · "
 "şahıs 1P x4 · 3MP x4 · 3MS x2 · 3FS x1, iltifât 0 · n=17 mora=86 harf=70 (n z=0,49), fâsıla "
 "سَبِيلا *(yol)* → ا, A sınıfı, ACC; i'râb ACC 3 · GEN 1 · NOM 1; bab I x4 · IV x1; zaman IMPF x3 · "
 "PERF x2; **kök ikilemesi ضلل *(sapma, saptırma)* x2 — biri geçişli (لَيُضِلُّنَا *(bizi "
 "saptıracaktı)*), biri üstünlük kalıbı (أَضَلُّ *(daha sapkın)*)**; simetri [3,4,7,1]; dış düğüm 1 · "
 "yıldız ★ yok · kökler كود *(neredeyse olma)* · ضلل *(sapma, saptırma)* · أله *(ilâh; lafza-i "
 "celâl)* · صبر *(sabır)* · علم *(bilme)* · حين *(vakit, an)* · رأي *(görme)* · عذب *(azap)* · سبل "
 "*(yol)* · bağ: xref حين *(vakit)* + رأى *(gördü)* + عذاب *(azap)* → **39:58**; **25:3 ve 25:18 ile "
 "أله üçlüsü** — 25:3'te anlatıcı 'ilâhlar edindiler' diyor, 25:18'de tapılanlar reddediyor, burada "
 "tapanlar İYELİKLE sahipleniyor: ءَالِهَتِنَا *(ilâhlarımız)* (elle, L1, aday 563)"),
43: ("eksen: **lafız YOK · Rab YOK** · **esmâ وَكِيل *(vekîl)* 9. sırada = fâsıla, MÜHÜRSÜZ — ÖLÇÜM "
 "ARTEFAKTI (aday 461/546/555)**: gönderge MUHATAP (2MS, elçi), ilâhî değil; ölçüt (a) dışlıyor. "
 "**Bu, blokta ölçüt (a) ile dışlanan ilk vaka — önceki artefaktlar ölçüt (b) ile dışlanıyordu** · "
 "aktör yok · edim soru, kip INTG 2 · şahıs 2MS x4 · 3MS x4, iltifât 0 · n=9 mora=44 harf=38 "
 "(n z=-0,36), fâsıla وَكِيلا *(vekîl)* → ا, A sınıfı, ACC; **i'râb ACC 3**; bab I x2 · VIII x1; "
 "zaman PERF x2 · IMPF x1; dış düğüm 1 · yıldız ★ yok · kökler رأي *(görme)* · أخذ *(alma, edinme)* · "
 "أله *(ilâh; lafza-i celâl)* · هوي *(hevâ, arzu; düşme)* · كون *(olmak; mekân, yer)* · وكل *(vekil "
 "kılma, tevekkül)* · bağ: xref رأى *(gördü)* + اتّخذ *(edindi)* + إله *(ilâh)* ve اتّخذ + إله + "
 "هواء *(hevâ)* → **ikisi de 45:23**; **أخذ *(alma, edinme)* bab VIII sûrede altıncı geçiş** "
 "(25:3, 18, 27, 28, 30, 43) (elle, L1, aday 551)"),
44: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — أَنْعَٰم *(davarlar)* aktör tablosuna "
 "girmiyor · edim haber, kip NEG 1 · RES 1 · şahıs 3MP x7 · 2MS x1, iltifât 0 · n=15 mora=64 "
 "harf=56 (n z=0,27), fâsıla سَبِيلا *(yol)* → ا, A sınıfı, ACC — **25:42'nin fâsılasıyla aynı "
 "kelime, iki ayet arayla**; i'râb ACC 3 · GEN 1 · NOM 1; bab I x3; zaman IMPF x3; **açık sayı "
 "sözcüğü: كثر *(çokluk)* → أَكْثَر *(çoğu)***; **biçim HASR + IDRAB — sûrenin üçüncü ve son "
 "IDRAB'ı** (25:11, 25:40, 25:44; makro sayım 3, **DİZİ TAMAMLANDI**); simetri [4,6,10,1]; dış "
 "düğüm 0 · yıldız ★ yok · kökler حسب *(sanma, hesap)* · كثر *(çokluk)* · سمع *(işitme)* · عقل "
 "*(akletme)* · نعم *(nimet; davar)* · ضلل *(sapma, saptırma)* · سبل *(yol)* · bağ: **25:42 ve 25:34 "
 "ile أَضَلُّ سَبِيلا *(yolca daha sapkın)* ÜÇLÜSÜ** — üçü de aynı iki kelime, üçü de fâsıla; "
 "aday 550'nin سبل dizisi altıncı geçişe çıktı (elle, L1, aday 564)"),
45: ("eksen: **lafız YOK · رَبّ *(Rab)* 4. sırada — sûrenin altıncı Rab'bi** (rab z=1,01; **yıldız "
 "eşiğini AŞMIYOR**) · esmâ yok · aktör yok — ٱلشَّمْس *(güneş)* aktör tablosuna girmiyor · edim "
 "soru + şart, kip INTG 1 · NEG 1 · COND 1 · EMPH 1 · şahıs 3MS x5 · 1P x2 · 2MS x1 · 3FS x1, "
 "iltifât 0 · n=16 mora=74 harf=60 (n z=0,38), fâsıla دَلِيلا *(delil, gösterge)* → ا, A sınıfı, "
 "ACC; **i'râb ACC 4 · GEN 1**; **bab I x5 — hepsi birinci bab**; zaman PERF x4 · IMPF x1; **kök "
 "ikilemesi جعل *(kılma, var etme)* x2 — biri şartın cevabı (لَجَعَلَهُۥ *(onu kılardı)*, 3MS), "
 "biri gerçekleşmiş (جَعَلْنَا *(kıldık)*, 1P): AYNI KÖK, İKİ FÂİL, İKİ KİP**; simetri [3,10,13,1]; "
 "dış düğüm 0 · yıldız ★ yok · kökler رأي *(görme)* · ربب *(rab, terbiye etme)* · كيف *(nasıl, "
 "keyfiyet)* · مدد *(uzatma, med)* · ظلل *(gölge)* · شيأ *(dileme; şey)* · جعل *(kılma, var etme)* · "
 "سكن *(sükûn, durgunluk; iskân)* · شمس *(güneş)* · دلل *(delil, gösterme)* · bağ: **25:9 ve 25:17 "
 "ile ٱنظُرْ/أَلَمْ تَرَ *(bak / görmedin mi)* çağrısı üçüncü kez ve İLK KEZ DOĞAYA yöneltiliyor** "
 "— 25:9'da meselleri gör, 25:17'de haşir sahnesi, burada gölge (elle, L1, aday 565)"),
46: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "1P x3 · 3MS x1, iltifât 0 · n=5 mora=29 harf=23 — **SÛRENİN OKUNAN EN KISA AYETİ** (n z=-0,79; "
 "25:28'in altı kelimesini geçiyor), fâsıla يَسِيرا *(kolay)* → ا, A sınıfı, ACC; **i'râb ACC 2 — "
 "beş kelimenin ikisi mansûb**; bab I x1; zaman PERF x1; **kök ikilemesi قبض *(kabzetme, avuçlama)* "
 "x2 — fiil + mef'ûl-i mutlak; bab I, blokta ilk kez bab II DEĞİL** (aday 559 ile karşılaştır); "
 "dış düğüm 0 · yıldız ★ yok · kökler قبض *(kabzetme, avuçlama)* · يسر *(kolaylık)* · bağ: **25:45 "
 "ile bitişik çift — tek cümlenin ikinci yarısı**; iki ayette gölgenin uzatılması ve geri çekilmesi "
 "ثُمَّ *(sonra)* ile üç aşamaya bölünmüş (elle, L1, aday 565)"),
47: ("eksen: **lafız YOK · Rab YOK — gönderge ٱلَّذِى *(o ki)*, sûrede yedinci kez** · esmâ yok · "
 "aktör yok · edim haber, kip işareti yok · şahıs 3MS x3 · 2MP x1, iltifât 0 · n=11 mora=62 harf=51 "
 "(n z=-0,15), fâsıla نُشُورا *(kalkış, diriliş)* → ا, A sınıfı, ACC — **25:3 ve 25:40'ın "
 "fâsılasıyla AYNI KELİME, sûrede üçüncü kez**; **i'râb ACC 6 — on bir kelimenin altısı mansûb, "
 "blokta en yüksek**; bab I x2; zaman PERF x2; **kök ikilemesi جعل *(kılma, var etme)* x2**; dış "
 "düğüm 1 · yıldız ★ yok · kökler جعل *(kılma, var etme)* · ليل *(gece)* · لبس *(giyinme; giysi)* · "
 "نوم *(uyku)* · سبت *(kesilme, dinlenme (sübât); Sebt günü)* · نهر *(ırmak; gündüz)* · نشر *(yayma, "
 "açma; diriltme)* · bağ: xref جعل *(kıldı)* + ليل *(gece)* + لباس *(giysi)* → **78:10**; **25:40 "
 "ile نشر ikinci karşılaşma** — orada نُشُورا *(diriliş)* inkâr ediliyordu, burada aynı kelime "
 "GÜNDELİK bir olguya veriliyor: gündüz bir kalkış (elle, L1, aday 566)"),
48: ("eksen: **lafız YOK · Rab YOK — gönderge yine ٱلَّذِى *(o ki)*, bitişik ayette ikinci kez** · "
 "esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs 3MS x3 · 1P x2 — **fâil ortada 3MS'den "
 "1P'ye geçiyor** (أَرْسَلَ *(gönderdi)* → وَأَنزَلْنَا *(indirdik)*), ölçüm ilt=0 · n=13 mora=74 "
 "harf=59 (n z=0,06), fâsıla طَهُورا *(tertemiz)* → ا, A sınıfı, ACC; **i'râb ACC 5 · GEN 2 · "
 "NOM 1**; **bab IV x2 — ayetin iki fiili de bab IV**; zaman PERF x2; dış düğüm 2 · yıldız ★ yok · "
 "kökler رسل *(gönderme, elçi)* · روح *(rüzgâr; ruh)* · بشر *(müjde; beşer)* · بين *(arası; "
 "açıklama)* · يدي *(el)* · رحم *(rahmet, merhamet)* · نزل *(inme, indirme)* · سمو *(ad; gök)* · "
 "موه *(su)* · طهر *(temizlik, tahâret)* · bağ: xref DÖRT 3-gram (أرسل *(gönderdi)* + ريح *(rüzgâr)* "
 "+ بشر *(müjde)* · ريح + بشر + بين *(ara)* · بشر + بين + يد *(el)* · بين + يد + رحمة *(rahmet)*) → "
 "**dördü de 7:57 VE 27:63**; **sûrenin en yoğun xref ayeti** (elle, L1, aday 567)"),
49: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — أَنْعَٰم *(davarlar)* yine tabloya "
 "girmiyor · edim haber, kip işareti yok · şahıs 1P x4 · 3MS x2, iltifât 0 · n=10 mora=62 harf=51 "
 "(n z=-0,26), fâsıla كَثِيرا *(çok)* → ا, A sınıfı, ACC — **25:14 ve 25:38'in fâsılasıyla aynı "
 "kelime, sûrede üçüncü kez**; **i'râb ACC 5 — on kelimenin beşi mansûb**; bab I x1 · IV x2; zaman "
 "IMPF x2 · PERF x1; **açık sayı sözcüğü: كثر *(çokluk)***; dış düğüm 1 · yıldız ★ yok · kökler "
 "حيي *(diri olma, hayat)* · بلد *(belde, şehir)* · موت *(ölüm)* · سقي *(sulama, su verme)* · خلق "
 "*(yaratma)* · نعم *(nimet; davar)* · أنس *(insan; ünsiyet)* · كثر *(çokluk)* · bağ: xref أحيا "
 "*(diriltti)* + بلدة *(belde)* + ميت *(ölü)* → **50:11**; **25:3 ile حيي/موت çifti ikinci kez** — "
 "orada sahte ilâhlar موت *(ölüm)* ve حيوة *(hayat)* üzerinde güçsüzdü, burada aynı iki kök bir "
 "eylemde birleşiyor: ölü beldeyi diriltme (elle, L1, aday 568)"),
50: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip EMPH 1 · CERT 1 · "
 "RES 1 · şahıs 3MP x3 · 1P x2 · 3MS x2, iltifât 0 · n=9 mora=56 harf=44 (n z=-0,36), fâsıla "
 "كُفُورا *(nankörlük)* → ا, A sınıfı, ACC; i'râb ACC 2 · NOM 1 · GEN 1; bab I x1 · II x1 · V x1; "
 "zaman PERF x2 · IMPF x1; **açık sayı sözcüğü: كثر *(çokluk)* → أَكْثَر *(çoğu)*, bitişik ayette "
 "ikinci kez**; **biçim HASR**; dış düğüm 1 · yıldız ★ yok · kökler صرف *(çevirme, türlü türlü "
 "açıklama)* · بين *(arası; açıklama)* · ذكر *(anma, zikir)* · أبي *(direnme, çekinme)* · كثر "
 "*(çokluk)* · أنس *(insan; ünsiyet)* · كفر *(inkâr, nankörlük)* · bağ: xref أبى *(direndi)* + أكثر "
 "*(çoğu)* + ناس *(insanlar)* ve أكثر + ناس + كفور *(nankörlük)* → **ikisi de 17:89**; **25:19 ile "
 "صرف ikinci geçişi ve BURADA 'türlü türlü açıklama' anlamında** — orada 'azabı çevirme'ydi; sûre "
 "bu kökü iki ayrı anlamda kullanıyor (elle, L1, adaylar 529, 569)"),
}

MERCEK = {
41: ("Sûrenin ikinci Allah lafzı burada ve ilk kez İTİRAZ EDENİN AĞZINDA: أَهَٰذَا ٱلَّذِى بَعَثَ "
 "ٱللَّهُ رَسُولا *(Allah'ın elçi olarak gönderdiği bu mu)*. Ölçülebilir bir ayrım — 25:17'de lafız "
 "anlatı içindeydi (mahşer sahnesinin toplayıcısı), burada alıntı içinde. Alay fiili HASR ile "
 "sınırlanıyor: إِن يَتَّخِذُونَكَ إِلَّا هُزُوًا *(seni ancak alaya alıyorlar)*; هزأ *(alay etme)* "
 "korpusta 34 geçişli ve dikey ölçümü ▸önce edinme x11,7 veriyor — 'alaya alma' korpusta zaten أخذ "
 "*(alma, edinme)* bab VIII'e bağlı, bu ayete özgü değil. Ve fâsıla رَسُولا *(elçi)* nekre; 25:7'de "
 "aynı kelime marife ve işaretliydi (هَٰذَا ٱلرَّسُولِ *(bu elçi)*)."),
42: ("İtiraz kendi başarısızlığını itiraf ederek kuruluyor: إِن كَادَ لَيُضِلُّنَا *(neredeyse bizi "
 "saptıracaktı)*, كود *(neredeyse olma)* kökü — gerçekleşmemiş bir yaklaşma. Ölçülebilir bir sahiplik "
 "işareti: ءَالِهَتِنَا *(ilâhlarımız)* iyelikli; sûrede أله *(ilâh; lafza-i celâl)* kökü üçüncü kez "
 "sahte ilâhlar için ve ilk kez BİRİNCİ ÇOĞUL iyelikle. Ayet sonra zamanı ileri atıyor: وَسَوْفَ "
 "يَعْلَمُونَ *(bilecekler)*, FUT — sûrede tek FUT işareti. Ve ضلل *(sapma, saptırma)* iki kez, iki "
 "biçimde: geçişli fiil ve üstünlük sıfatı; ikinci biçim (أَضَلُّ سَبِيلا *(yolca daha sapkın)*) "
 "25:34'ten birebir geliyor ve 25:44'te üçüncü kez gelecek."),
43: ("Soru bir tersine çevirme kuruyor: ٱتَّخَذَ إِلَٰهَهُۥ هَوَىٰهُ *(hevâsını kendine ilâh "
 "edindi)* — mef'ûl ve ikinci mef'ûl yer değiştirebilir, dolayısıyla ayet hem 'hevâsını ilâh edindi' "
 "hem 'ilâhını hevâsı yaptı' okunabilir; ölçülebilir olan, iki ismin de mansûb olması. هوي *(hevâ, "
 "arzu; düşme)* korpusta 38 geçişli ve dikey ölçümü ▸önce edinme x30,5 veriyor — 'hevâyı ilâh "
 "edinme' korpusta sabit bir eşleşme, iki xref'in de tek ayete (45:23) düşmesi bundan. Ve esmâ "
 "tablosu fâsıladaki وَكِيلا *(vekîl)*'i esmâ sayıyor, oysa gönderge MUHATAP: أَفَأَنتَ تَكُونُ "
 "عَلَيْهِ وَكِيلا *(ona sen mi vekil olacaksın)*. Ölçüt (a) ile dışlanan ilk artefakt."),
44: ("Ayet bir karşılaştırma kuruyor ve karşılaştırmayı iki aşamada bozuyor: önce eşitlik "
 "(كَٱلْأَنْعَٰمِ *(davarlar gibi)*), sonra IDRAB ile üstünlük (بَلْ هُمْ أَضَلُّ *(hayır, daha "
 "sapkın)*). Ölçülebilir bir yapı: HASR ve IDRAB aynı ayette — sûrede bu birleşim tek. İki yeti "
 "sayılıyor ve ikisi de muzâri: يَسْمَعُونَ *(işitirler)*, يَعْقِلُونَ *(akıl ederler)*. نعم *(nimet; "
 "davar)* korpusta 143 geçişli ve dikey ölçümü ▸önce insan ve ▸sonra su-içme bağlamları veriyor — "
 "kök korpusta hem 'nimet' hem 'davar' taşıyor ve kök düzeyi komşuluk ikisini ayırmıyor (aday 529 "
 "sınıfı). Ve bu ayet sûrenin ÜÇÜNCÜ VE SON IDRAB'ı: dizi 25:11, 25:40, 25:44 ile tamamlandı."),
45: ("Bakma çağrısı sûrede üçüncü kez ve İLK KEZ DOĞAYA: أَلَمْ تَرَ إِلَىٰ رَبِّكَ كَيْفَ مَدَّ "
 "ٱلظِّلَّ *(Rabbini görmedin mi, gölgeyi nasıl uzattı)*. 25:9'da ٱنظُرْ كَيْفَ *(bak nasıl)* "
 "mesellere, 25:17'de haşir sahnesine, burada bir fiziksel sürece. Ölçülebilir bir üç aşama: "
 "uzatma (مَدَّ *(uzattı)*, مدد *(uzatma, med)*), varsayılan alternatif (سَاكِنًۭا *(durgun)*, سكن "
 "*(sükûn, durgunluk; iskân)* — gerçekleşmemiş), ve gösterge atama (جَعَلْنَا ٱلشَّمْسَ عَلَيْهِ "
 "دَلِيلا *(güneşi ona bir delil kıldık)*). جعل *(kılma, var etme)* iki kez ve fâili değiştiriyor: "
 "şartın cevabında 3MS, gerçekleşende 1P. دلل *(delil, gösterme)* korpusta 8 geçişli ve dikey ölçümü "
 "eşiği aşan tek komşu vermiyor — kökün dar bir yatağı yok."),
46: ("Beş kelime — sûrenin okunan en kısa ayeti, 25:28'in altı kelimesinin de altında. Ölçülebilir "
 "bir yapı: ayet tek başına bir cümle değil, 25:45'in üçüncü aşaması; ثُمَّ *(sonra)* iki ayette de "
 "aynı işi yapıyor (25:45'te güneşin atanması, burada gölgenin çekilmesi). قبض *(kabzetme, avuçlama)* "
 "iki kez ve fiil + mef'ûl-i mutlak yapısında — ama BAB I, oysa 25:32/36/39'daki üç örnek bab II'ydi "
 "(aday 559). Kabzedişin sıfatı: يَسِيرا *(kolay)*, يسر *(kolaylık)* kökü; korpusta 44 geçişli ve "
 "dikey ölçümü ▸önce zorluk x36,9 veriyor — kök korpusta karşıtıyla birlikte yaşıyor, burada karşıtı "
 "YOK. Bu, 25:6'daki سرر *(sır, gizleme)* ile aynı desen: karşıtlı kök tek uçlu kullanılıyor."),
47: ("Üç öğe üç sıfatla eşleştiriliyor ve üçü de mansûb: ٱلَّيْلَ لِبَاسًۭا *(geceyi bir giysi)*, "
 "ٱلنَّوْمَ سُبَاتًۭا *(uykuyu bir dinlenme)*, ٱلنَّهَارَ نُشُورا *(gündüzü bir kalkış)*. Ölçülebilir "
 "bir yoğunluk: on bir kelimenin altısı mansûb, blokta en yüksek. سبت *(kesilme, dinlenme (sübât); "
 "Sebt günü)* korpusta 9 geçişli ve sekizi 'Sebt günü' anlamında; bu lemma (سُبات) TEK geçiş — kök "
 "düzeyi komşuluk yanıltıcı (aday 529 sınıfı). Ve fâsıla نُشُورا *(kalkış, diriliş)*, sûrede üçüncü "
 "kez: 25:3'te sahte ilâhların yetersizliği, 25:40'ta inkâr edilen diriliş, burada gündelik bir "
 "olgu — aynı kelime üç farklı katmanda."),
48: ("Ayet sûrenin en yoğun xref'ini taşıyor: dört 3-gram ve dördü de aynı iki ayete (7:57 ve 27:63). "
 "Yani terkip korpusta neredeyse birebir tekrarlanıyor — donmuş kalıp adayı (aday 437 sınıfı). "
 "Ölçülebilir bir fâil kayması: ilk yarıda 3MS (أَرْسَلَ *(gönderdi)*), ikinci yarıda 1P "
 "(وَأَنزَلْنَا *(indirdik)*); iltifât sayacı bunu 0 veriyor çünkü geçiş ٱلَّذِى *(o ki)* "
 "göndergesinden birinci çoğula, yani lafız→zamir değil gönderge→zamir. **ADAY 517'NİN SINAMA "
 "VAKASI OLABİLİR** — tagger'ın hangi geçişleri saydığı belirsiz. Suyun sıfatı tek kelime: طَهُورا "
 "*(tertemiz)*, طهر *(temizlik, tahâret)* korpusta 31 geçişli ve bu lemma tek geçiş. SINIR: ayet "
 "rüzgâr ile yağış arasındaki ilişkiyi SIRALIYOR (rüzgâr rahmetin önünde) ama ne mekanizma ne ölçü "
 "veriyor."),
49: ("Amaç cümlesi iki fiille kuruluyor ve ikisi de bab IV: لِّنُحْۦِىَ *(diriltelim diye)* ve "
 "وَنُسْقِيَهُۥ *(sulayalım diye)*. Ölçülebilir bir sıra: önce yer (بَلْدَةًۭ مَّيْتًۭا *(ölü bir "
 "belde)*), sonra canlılar (أَنْعَٰمًۭا وَأَنَاسِىَّ *(davarlar ve insanlar)*) — ve canlı sırası "
 "davar önce, insan sonra. حيي *(diri olma, hayat)* ve موت *(ölüm)* aynı ayette, 25:3'ten sonra "
 "ikinci kez: orada sahte ilâhlar bu ikisi üzerinde güçsüzdü, burada ikisi tek eylemde birleşiyor. "
 "سقي *(sulama, su verme)* korpusta 25 geçişli ve dikey ölçümü ▸sonra davar bağlamı veriyor. "
 "SINIR: ayet suyun canlılar için gerekliliğini SÖYLÜYOR ama ne miktar, ne mekanizma, ne sınıflandırma "
 "veriyor; 'ölü belde' bir hâl adı, bir toprak ölçüsü değil."),
50: ("Bloğun kapanışı bir dağıtım fiili ve bir direnç: صَرَّفْنَٰهُ بَيْنَهُمْ *(onu aralarında türlü "
 "türlü açıkladık)*. صرف *(çevirme, türlü türlü açıklama)* sûrede ikinci kez ve BURADA farklı "
 "anlamda — 25:19'da 'azabı çevirme'ydi; dikey ölçüm bu kök için ▸sonra Kur'ân x17,6 veriyor, yani "
 "korpus taban anlamı burada geçerli, 25:19'daki geçiş ise azınlık anlamıydı. Direnç fiili tek ve "
 "HASR ile sınırlı: فَأَبَىٰٓ … إِلَّا كُفُورا *(nankörlükten başkasını kabul etmedi)*; أبي *(direnme, "
 "çekinme)* korpusta 13 geçişli. Ve كثر *(çokluk)* bitişik iki ayette ikinci kez, ikisi de أَكْثَر "
 "*(çoğu)* biçiminde — 25:44 ve 25:50, ikisi de insanların çoğunu olumsuzluyor."),
}

ATLAMA = {
 "_blok_notu_25_41_50": ("BLOK BİLANÇOSU VE ADAY 561'İN EN KESKİN VAKASI. **ON AYETİN ONU DA "
  "YILDIZSIZ** (★★★ 0, ★★ 0, ★ 0) — okumada görülen en uzun yıldızsız dizi. BUNA KARŞILIK BU BLOK "
  "SÛRENİN EN YOĞUN DOĞA BÖLÜTÜ: 25:45-46 gölgenin uzatılması, güneşin gösterge kılınması ve "
  "gölgenin kademeli çekilmesi (ÜÇ AŞAMALI BİR SÜREÇ, açık bir gösterge ilişkisiyle) · 25:47 gece / "
  "uyku / gündüz üçlüsü (biyolojik ritim) · 25:48 rüzgârların yağıştan ÖNCE gönderilmesi (SIRALAMA "
  "ilişkisi) · 25:49 suyun ölü beldeyi diriltmesi ve canlıları sulaması (davar ve insan ayrı ayrı "
  "sayılıyor). PROTOKOL GEREĞİ 🜁 BİYOLOG VE 🜂 UZAY MERCEKLERİ YAZILAMADI — eşik ★★★ ve bu blokta "
  "★ bile yok. Kural ÇİĞNENMEDİ. Ama kaydedilir: sûrenin çıpa bakımından en zengin on ayeti, yıldız "
  "formülü tarafından tamamen görünmez kılınıyor. Aday 561'e yazıldı; 468/472/503/512/553 kümesinin "
  "en güçlü kanıtı. NOT — YILDIZ EŞİĞİ: 25:41'de allah z=1,29 ve 25:45'te rab z=1,01, ikisi de "
  "eşiğin (≈1,5) altında; blokta hiçbir z eşiği aşmıyor çünkü bölütte hapaks yok, edilgen yok, "
  "kafiye kırılması yok ve ayet uzunlukları ortalamaya yakın. Yıldız formülü İÇERİĞİ HİÇ "
  "ÖLÇMÜYOR — bu blok bunun en açık gösterimi."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(41, 51):
    OM['25']["25:%d" % n] = {"ar": AR[(25, n)], "meal": MEAL[n], "olcum": OLCUM[n],
                             "mercek": MERCEK[n], "dikey": DIK["25:%d" % n]}
OM['25']['_mercek_atlama_notu'].update(ATLAMA)
OM['25']['_blok_bolme_notu'] += (" DÖRDÜNCÜ BÖLME: blok 25:41-60 de ikiye bölündü (25:41-50 ve "
 "25:51-60). Gerekçe ölçüm: 25:50 bir kapanış hükmüyle bölütü bitiriyor (فَأَبَىٰٓ أَكْثَرُ "
 "ٱلنَّاسِ إِلَّا كُفُورا *(insanların çoğu nankörlükten başkasını kabul etmedi)*) ve 25:51 "
 "وَلَوْ شِئْنَا *(dileseydik)* ile yeni bir şart hareketi açıyor; ayrıca 25:41-50 sûrenin doğa "
 "bölütünü bütün hâlinde taşıyor ve mercek kaydı bölünmesin diye ayrı tutuldu.")
OM['ilerleme']['not'] = ("Sûre 23 TAM (118/118). Sûre 24 TAM (64/64). **Sûre 25 (Furkān) 50/77.** "
                         "Devam: 25:51'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "25": "1-50 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1695
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 25 →', len([k for k in OM['25'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(41, 51):
    MK['25']["25:%d" % n] = MERCEK[n]
MK['25_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 25 →', len(MK['25']))
