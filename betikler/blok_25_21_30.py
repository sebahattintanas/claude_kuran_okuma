# -*- coding: utf-8 -*-
"""blok_25_21_30.py — sûre 25 üçüncü blok (25:21-30). Sûrenin ilk ★★★ ayeti burada (25:28)."""
import json
DIK = json.load(open('blok_dikey_25_21_40.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
21: "Bize kavuşmayı ummayanlar dediler ki: Bize melekler indirilseydi ya, ya da Rabbimizi görseydik. Andolsun kendi içlerinde büyüklendiler ve büyük bir taşkınlıkla azdılar.",
22: "Melekleri görecekleri gün — o gün suçlulara müjde yoktur; 'Yasak, kesin bir yasak' derler.",
23: "Yaptıkları her işe yöneldik ve onu savrulmuş toz zerrelerine çevirdik.",
24: "O gün cennet ehli, kalınacak yer bakımından daha hayırlı, dinlenilecek yer bakımından daha güzeldir.",
25: "O gün gök bulutlarla yarılır ve melekler ardarda indirilir.",
26: "O gün gerçek mülk Rahmân'ındır; inkârcılar için zor bir gündür.",
27: "O gün zalim ellerini ısırır, der ki: Keşke elçiyle birlikte bir yol tutsaydım.",
28: "Vay bana! Keşke falancayı dost edinmeseydim.",
29: "Andolsun, zikir bana geldikten sonra beni ondan o saptırdı. Şeytan insanı yardımsız bırakandır.",
30: "Elçi der ki: Rabbim, kavmim bu Kur'ân'ı terk edilmiş bıraktı.",
}

OLCUM = {
21: ("eksen: **lafız YOK · رَبّ *(Rab)* 12. sırada — sûrenin üçüncü Rab'bi** (rab z=0,80) · "
 "**esmâ كَبِير *(büyük)* 19. sırada = fâsıla — ÖLÇÜM ARTEFAKTI (aday 461/546)**: nekre ve "
 "gönderge عُتُوّ *(taşkınlık, azgınlık)*, sıfat taşkınlığın. MÜHÜRSÜZ. **Bu, aynı esmânın aynı "
 "sınıftan üçüncü yanlış pozitifi** (25:19 كَبِير, 25:18 وَلِيّ) · aktör yok · edim haber, kip "
 "NEG 1 · EMPH 1 · CERT 1 · şahıs 3MP x7 · 1P x4 · 3MS x2, iltifât 0 · n=19 mora=111 harf=88 "
 "(n z=0,70), fâsıla كَبِيرًۭا *(büyük)* → ا, A sınıfı, ACC; i'râb ACC 4 · NOM 1 · GEN 1; bab I x4 · "
 "IV x1 · X x1; zaman PERF x4 · IMPF x2; **edilgen 1 — أُنزِلَ *(indirilseydi)*** (pas z=0,62); "
 "**kök ikilemesi كبر *(büyüklük; büyüklenme)* x2 · عتو *(taşkınlık, haddi aşma)* x2**; simetri "
 "[3,6,13,1]; dış düğüm 1 · yıldız ★ yok · kökler قول *(söz söyleme)* · رجو *(umma, bekleme)* · "
 "لقي *(karşılaşma, kavuşma; atma)* · نزل *(inme, indirme)* · ملك *(mülk; melik)* · رأي *(görme)* · "
 "ربب *(rab, terbiye etme)* · كبر *(büyüklük; büyüklenme)* · نفس *(nefis, can)* · عتو *(taşkınlık, "
 "haddi aşma)* · bağ: xref قال *(dedi)* + يرجوا۟ *(ummuyorlar)* + لقاء *(kavuşma)* → **10:15**; "
 "**25:7 ile aynı istek** — orada مَلَك *(melek)* tekil isteniyordu, burada ٱلْمَلَٰٓئِكَة "
 "*(melekler)* çoğul ve marife, artı ikinci bir istek ekleniyor: نَرَىٰ رَبَّنَا *(Rabbimizi "
 "görsek)* (elle, L1, aday 547)"),
22: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · şahıs 3MP x4, "
 "iltifât 0 · n=10 mora=70 harf=53 (n z=-0,26), fâsıla مَّحْجُورًۭا *(engellenmiş, yasaklanmış)* → ا, "
 "A sınıfı, ACC; **i'râb ACC 4**; bab I x2; zaman IMPF x2; **kök ikilemesi يوم *(gün)* x2 · حجر "
 "*(taş; engel, yasak (hicr); kucak (hucûr))* x2 — ikincisi mef'ûl-i mutlak benzeri pekiştirme: "
 "حِجْرًۭا مَّحْجُورًۭا *(engel, engellenmiş)***; dış düğüm 0 · yıldız ★ yok · kökler يوم *(gün)* · "
 "رأي *(görme)* · ملك *(mülk; melik)* · بشر *(müjde; beşer)* · جرم *(suç, cürüm)* · قول *(söz "
 "söyleme)* · حجر *(taş; engel, yasak (hicr); kucak (hucûr))* · bağ: **25:21 ile bitişik cevap** — "
 "orada melek inişi İSTENİYOR, burada melek görüşü GERÇEKLEŞİYOR ve müjde değil yasak getiriyor "
 "(elle, L1, aday 547)"),
23: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "1P x4 · 3MP x2 · 3MS x1**, iltifât 0 · n=9 mora=52 harf=40 (n z=-0,36), fâsıla مَّنثُورًا "
 "*(saçılmış, savrulmuş)* → ا, A sınıfı, ACC; i'râb ACC 2 · GEN 1; bab I x3; zaman PERF x3; "
 "**kök ikilemesi عمل *(iş, amel)* x2 — fiil + iç mef'ûl: عَمِلُوا۟ مِنْ عَمَلٍۢ *(işledikleri "
 "her iş)***; dış düğüm 0 · yıldız ★ yok · kökler قدم *(öne geçme, takdim)* · عمل *(iş, amel)* · "
 "جعل *(kılma, var etme)* · هبو *(savrulan toz zerresi (hebâ))* · نثر *(saçma, dağıtma)* · bağ: "
 "**هبو *(savrulan toz zerresi (hebâ))* korpusta iki geçişli** (25:23, 56:6) ve **نثر *(saçma, "
 "dağıtma)* üç geçişli** (25:23, 76:19, 82:2); ikisi de burada bitişik"),
24: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı جَنَّة *(cennet, bahçe)* 2. sırada, "
 "rol mecrur — SÛRENİN İLK ADLI AKTÖRÜ** · edim haber, kip işareti yok · **şahıs eki YOK — ayette "
 "hiç fiil yok**, iltifât 0 · n=7 mora=44 harf=36 — **bloğun en kısa ikinci ayeti** (n z=-0,58), "
 "fâsıla مَقِيلًۭا *(öğle dinlenme yeri)* → ا, A sınıfı, ACC; i'râb NOM 3 · ACC 2 · GEN 1; "
 "**bab yok · zaman yok — yedi kelimenin tamamı isim**; dış düğüm 1 · yıldız ★ yok · kökler صحب "
 "*(arkadaşlık; ehli)* · جنن *(örtme, gizleme; cennet; cin)* · يوم *(gün)* · خير *(hayır, daha "
 "iyi)* · قرر *(karar kılma, yerleşme)* · حسن *(güzellik, iyilik)* · قيل *(öğle uykusu, gündüz "
 "dinlenmesi (kaylûle))* · bağ: xref أصحاب *(ehli)* + جنّة *(cennet)* + يوم *(gün)* → **36:55**; "
 "**25:15 ile çift** — orada soru soruluyordu (أَذَٰلِكَ خَيْرٌ *(bu mu hayırlı)*), burada aynı "
 "kökle cevap veriliyor (خَيْرٌۭ مُّسْتَقَرًّۭا *(kalınacak yer bakımından daha hayırlı)*) "
 "(elle, L1, aday 548)"),
25: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3FS x1 · 3MS x1, iltifât 0 · n=7 mora=50 harf=37 — **bloğun en kısa ikinci ayeti** (n z=-0,58), "
 "fâsıla تَنزِيلًا *(indirme)* → ا, A sınıfı, ACC; i'râb ACC 2 · NOM 2 · GEN 1; bab II x1 · V x1; "
 "zaman IMPF x1 · PERF x1; **edilgen 1 — نُزِّلَ *(indirildi)***, **pas z=2,52: yıldızın TEK "
 "kaynağı**; **kök ikilemesi نزل *(inme, indirme)* x2 — fiil + mef'ûl-i mutlak: نُزِّلَ … تَنزِيلًا "
 "*(indirildi … bir indirilişle)***; dış düğüm 0 · **yıldız ★★** · kökler يوم *(gün)* · شقق "
 "*(yarılma, ayrılma)* · سمو *(ad; gök)* · غمم *(bulut, gam)* · نزل *(inme, indirme)* · ملك *(mülk; "
 "melik)* · bağ: **25:21 ile cevap** — orada لَوْلَآ أُنزِلَ عَلَيْنَا ٱلْمَلَٰٓئِكَةُ *(bize "
 "melekler indirilseydi ya)* isteniyordu, burada aynı kök bab II'ye çıkmış ve pekiştirilmiş "
 "(elle, L1, aday 547)"),
26: ("eksen: **lafız YOK · Rab YOK** · **esmâ رَحْمٰن *(rahmân)* 4. sırada, ORTA konum, MÜHÜRSÜZ — "
 "SÛRENİN İLK رَحْمٰن'I VE ADAY 546'NIN BÜYÜK VAKASI**: burada رَحْمٰن marife, لِ ile mecrur ve "
 "MÜLKÜN SAHİBİ konumunda, yani yüklem sıfatı değil GÖNDERGE; lafzın yerini tutuyor. Ölçüt (a) "
 "gönderge onu esmâ sayıyor, ama özel ad katmanı ayrı bir soru açıyor · aktör yok · edim haber, "
 "kip işareti yok · şahıs 3MS x1, iltifât 0 · n=9 mora=56 harf=45 (n z=-0,36), fâsıla عَسِيرًۭا "
 "*(zor)* → ا, A sınıfı, ACC; i'râb NOM 2 · GEN 2 · ACC 2; bab I x1; zaman PERF x1; **kök ikilemesi "
 "يوم *(gün)* x2**; dış düğüm 0 · yıldız ★ yok · kökler ملك *(mülk; melik)* · يوم *(gün)* · حقق "
 "*(hak, gerçeklik)* · رحم *(rahmet, merhamet)* · كون *(olmak; mekân, yer)* · كفر *(inkâr, "
 "nankörlük)* · عسر *(zorluk, güçlük)* · bağ: **25:2 ile halka** — orada مُلْكُ ٱلسَّمَٰوَٰتِ "
 "وَٱلْأَرْضِ *(göklerin ve yerin mülkü)* göndergesiz ٱلَّذِى *(o ki)*'ye aitti, burada aynı kök "
 "(ملك *(mülk; melik)*) ADLANDIRILMIŞ bir göndergeye: لِلرَّحْمَٰنِ *(Rahmân'a)* (elle, L1, aday 549)"),
27: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — ٱلظَّالِم *(zalim)* tekil ve marife "
 "ama aktör tablosuna girmiyor · edim nida, kip VOC 1 · **şahıs 3MS x3 · 1S x3 — anlatıdan iç sese "
 "geçiş**, ölçüm ilt=0 · n=11 mora=60 harf=49 (n z=-0,15), fâsıla سَبِيلًۭا *(yol)* → ا, A sınıfı, "
 "ACC; **i'râb ACC 4 · GEN 2 · NOM 1**; bab I x2 · VIII x1; zaman IMPF x2 · PERF x1; dış düğüm 0 · "
 "yıldız ★ yok · kökler يوم *(gün)* · عضض *(ısırma)* · ظلم *(zulüm)* · يدي *(el)* · قول *(söz "
 "söyleme)* · أخذ *(alma, edinme)* · رسل *(gönderme, elçi)* · سبل *(yol)* · bağ: **25:9 ve 25:17 "
 "ile üçüncü سبل *(yol)* geçişi** — 25:9'da yol bulunamıyor, 25:17'de saptıran soruluyor, burada "
 "yol TUTULMAMIŞ olarak pişmanlık nesnesi (elle, L1, aday 550); **عضض *(ısırma)* korpusta iki "
 "geçişli** (3:119, 25:27)"),
28: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim nida, kip VOC 1 · NEG 1 · **şahıs "
 "1S x2 — ayette başka şahıs yok**, iltifât 0 · n=6 mora=36 harf=28 — **SÛRENİN OKUNAN EN KISA "
 "AYETİ** (n z=-0,68), fâsıla خَلِيلًۭا *(dost, halîl)* → ا, A sınıfı, ACC; **i'râb ACC 3 · NOM 1**; "
 "bab VIII x1; zaman IMPF x1; **HAPAKS: فلن *(falan, filan kimse)* — korpusta TEK geçiş** "
 "(hapaks z=3,38: **yıldızın TEK kaynağı**); dış düğüm 0 · **yıldız ★★★ — SÛRENİN İLK ÜÇ "
 "YILDIZLISI** · kökler أخذ *(alma, edinme)* · فلن *(falan, filan kimse)* · خلل *(dostluk, halîl; "
 "aralık)* · bağ: **25:27 ile bitişik ikili** — aynı kök أخذ *(alma, edinme)* bab VIII iki kez, "
 "25:27'de olumlu temenni (ٱتَّخَذْتُ *(tutsaydım)*), 25:28'de olumsuz temenni (لَمْ أَتَّخِذْ "
 "*(edinmeseydim)*): pişmanlık iki yönde de aynı fiille (elle, L1, aday 551)"),
29: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı شَيْطان *(şeytan)* 9. sırada, rol "
 "FAİL** · edim haber, kip EMPH 1 · CERT 1 · şahıs 3MS x3 · 1S x2, iltifât 0 · n=11 mora=59 harf=48 "
 "(n z=-0,15), fâsıla خَذُولًۭا *(yardımsız bırakan)* → ا, A sınıfı, ACC; i'râb GEN 2 · ACC 2 · "
 "NOM 1; bab I x2 · IV x1; zaman PERF x3; dış düğüm 1 · yıldız ★ yok · kökler ضلل *(sapma, "
 "saptırma)* · ذكر *(anma, zikir)* · بعد *(sonra; uzaklık)* · جيأ *(gelme)* · كون *(olmak; mekân, "
 "yer)* · شطن *(şeytan)* · أنس *(insan; ünsiyet)* · خذل *(yardımsız bırakma)* · bağ: xref بعد "
 "*(sonra)* + جاء *(geldi)* + كان *(oldu)* → **34:32**; **25:18 ile ortak ذكر *(anma, zikir)*** — "
 "orada نَسُوا۟ ٱلذِّكْرَ *(zikri unuttular)*, burada أَضَلَّنِى عَنِ ٱلذِّكْرِ *(beni zikirden "
 "saptırdı)*: aynı nesne, biri unutma biri saptırılma (elle, L1, aday 552)"),
30: ("eksen: **lafız YOK · رَبّ *(Rab)* 3. sırada — sûrenin dördüncü Rab'bi ve İLK NİDA HÂLİNDE "
 "(يَٰرَبِّ *(Rabbim)*)**, rab z=2,05: **yıldızın TEK kaynağı** · esmâ yok · **aktör: adlı قُرْءان "
 "*(Kur'ân)* 8. sırada, rol MEF'ÛL** · edim nida, kip VOC 1 · şahıs 3MP x2 · 1S x2 · 3MS x1, "
 "iltifât 0 · n=9 mora=54 harf=43 (n z=-0,36), fâsıla مَهْجُورًۭا *(terk edilmiş)* → ا, A sınıfı, "
 "ACC; **i'râb ACC 4 · NOM 2**; bab I x1 · VIII x1; zaman PERF x2; biçim DIKKAT; dış düğüm 0 · "
 "**yıldız ★★** · kökler قول *(söz söyleme)* · رسل *(gönderme, elçi)* · ربب *(rab, terbiye etme)* · "
 "قوم *(kalkma; kavim; kıyamet)* · أخذ *(alma, edinme)* · قرأ *(okuma, Kur'ân)* · هجر *(terk etme, "
 "hicret)* · bağ: **25:27 ve 25:28 ile üçlü** — أخذ *(alma, edinme)* bab VIII üçüncü kez ve üçüncü "
 "özneyle: zalim tutmadı, zalim dost edindi, kavim Kur'ân'ı terk edilmiş EDİNDİ (elle, L1, aday 551)"),
}

MERCEK = {
21: ("İstek 25:7'den geri geliyor ama büyümüş: orada tek bir مَلَك *(melek)* nekre isteniyordu, "
 "burada ٱلْمَلَٰٓئِكَة *(melekler)* çoğul ve marife, ve ikinci bir istek ekleniyor — نَرَىٰ "
 "رَبَّنَا *(Rabbimizi görsek)*. Ölçülebilir bir tırmanma. Ayetin kapanışı iki büyüklük kökünü "
 "yan yana koyuyor ve ikisi de aynı ayette ikileniyor: كبر *(büyüklük; büyüklenme)* önce fiil "
 "(ٱسْتَكْبَرُوا۟ *(büyüklendiler)*, bab X) sonra sıfat (كَبِيرًۭا *(büyük)*), عتو *(taşkınlık, "
 "haddi aşma)* önce fiil sonra mef'ûl-i mutlak (عَتَوْ عُتُوًّۭا *(azdılar, bir azgınlıkla)*). "
 "İki kök, iki kez, aynı yapıyla. عتو korpusta 10 geçişli ve dikey ölçümü ▸önce Semûd x62,0 "
 "veriyor — kök korpusta ağırlıkla bir kavme bağlı, burada özne adsız."),
22: ("İstek yerine getiriliyor ve getirilmesi cezanın kendisi oluyor: يَوْمَ يَرَوْنَ "
 "ٱلْمَلَٰٓئِكَةَ *(melekleri görecekleri gün)* — 25:21'in iki isteğinden biri (görme) ve nesnesi "
 "(melekler) burada gerçekleşiyor. Ölçülebilir bir olumsuzlama: لَا بُشْرَىٰ *(müjde yok)*; بشر "
 "*(müjde; beşer)* kökü korpusta 123 geçişli ve dikey ölçümü ▸sonra cennet x9,2 veriyor, yani kök "
 "korpusta olumlu kutupta ve burada olumsuzlanıyor. Kapanış bir kök ikilemesi ve pekiştirme: "
 "حِجْرًۭا مَّحْجُورًۭا *(engel, engellenmiş)* — aynı kökten isim ve ism-i mef'ûl arka arkaya; "
 "حجر *(taş; engel, yasak (hicr); kucak (hucûr))* korpusta 21 geçişli ve çoğunda 'taş' anlamında, "
 "burada 'yasak' anlamında (aday 529 sınıfı: dikey satırı taş komşuluğunu getiriyor)."),
23: ("Ayet iki fiilde bir dönüşüm ölçüyor: قَدِمْنَآ *(yöneldik)* ve جَعَلْنَٰهُ *(onu kıldık)*. "
 "Nesne kök ikilemesiyle veriliyor — مَا عَمِلُوا۟ مِنْ عَمَلٍۢ *(işledikleri her iş)*, عمل *(iş, "
 "amel)* fiil ve iç mef'ûl olarak; bu yapı 25:2'nin فَقَدَّرَهُۥ تَقْدِيرًۭا *(ona bir ölçü "
 "biçti)*'sıyla aynı sınıftan. Sonuç iki seyrek kökle veriliyor ve ikisi de bitişik: هَبَآءًۭ "
 "مَّنثُورًا *(savrulmuş toz zerresi)*; هبو *(savrulan toz zerresi (hebâ))* korpusta İKİ geçişli "
 "(25:23, 56:6), نثر *(saçma, dağıtma)* ÜÇ geçişli (25:23, 76:19, 82:2). İki seyrek kökün bir "
 "ayette buluşması ölçülebilir; dikey ölçüm ikisi için de eşiği aşan komşu vermiyor."),
24: ("Yedi kelimenin yedisi de isim — ayette tek fiil yok, tek şahıs eki yok. Ölçülebilir bir "
 "karşıtlık: önceki ayet bir yok oluş fiiliyle bitmişti (جَعَلْنَٰهُ هَبَآءًۭ *(onu toz kıldık)*), "
 "bu ayet fiilsiz bir yerleşme cümlesi. İki üstünlük sıfatı yan yana ve ikisi de temyizli: خَيْرٌۭ "
 "مُّسْتَقَرًّۭا *(kalınacak yer bakımından daha hayırlı)* ve أَحْسَنُ مَقِيلًۭا *(dinlenilecek yer "
 "bakımından daha güzel)*. قيل *(öğle uykusu, gündüz dinlenmesi (kaylûle))* korpusta İKİ geçişli "
 "(7:4, 25:24) ve öteki geçişi bir helâk sahnesinde — aynı kök burada karşıt kutupta. Ve sûrenin "
 "ilk adlı aktörü burada: جَنَّة *(cennet, bahçe)*, rol mecrur."),
25: ("Yıldızın tek kaynağı tek bir edilgen fiil: نُزِّلَ *(indirildi)*, نزل *(inme, indirme)* bab II. "
 "Ölçülebilir bir cevap: 25:21'de لَوْلَآ أُنزِلَ عَلَيْنَا ٱلْمَلَٰٓئِكَةُ *(bize melekler "
 "indirilseydi ya)* isteniyordu, o bab IV'tü; burada aynı kök bab II'ye çıkıyor ve üstüne mef'ûl-i "
 "mutlakla pekiştiriliyor — تَنزِيلًا *(bir indirilişle)*. İstek yerine geliyor ama şiddeti "
 "artırılmış biçimde. Gök fiili de edilgen değil dönüşlü: تَشَقَّقُ *(yarılır)*, شقق *(yarılma, "
 "ayrılma)* bab V; kök korpusta 28 geçişli ve dikey ölçümü ▸sonra ay x53,6 veriyor — korpusta "
 "ağırlıkla ay yarılmasına bağlı, burada gök ve bulut. SINIR: ayet gökyüzü için ne bir mekanizma "
 "ne bir ölçü veriyor; bulut yalnız وَسîle olarak anılıyor (بِٱلْغَمَٰمِ *(bulutlarla)*)."),
26: ("Sûrenin ilk رَحْمٰن *(rahmân)*'ı ve ayet onu bir yüklem sıfatı olarak değil MÜLKÜN SAHİBİ "
 "olarak kullanıyor: ٱلْمُلْكُ يَوْمَئِذٍ ٱلْحَقُّ لِلرَّحْمَٰنِ *(o gün gerçek mülk Rahmân'ındır)*. "
 "Ölçülebilir bir halka: 25:2'de aynı kök (ملك *(mülk; melik)*) göndergesiz bir ٱلَّذِى *(o ki)*'ye "
 "aitti — sûrenin açılışında mülkün sahibi ADLANDIRILMAMIŞTI; burada adlandırılıyor, ama Allah "
 "lafzıyla değil. Mülkün sıfatı da eklenmiş: ٱلْحَقُّ *(gerçek)*, yani 25:2'nin mutlak "
 "mülkiyetine burada bir nitelik giriyor. Ve gün iki kez anılıyor (يوم *(gün)* x2), ikincisi "
 "nekre ve sıfatlı: يَوْمًا … عَسِيرًۭا *(zor bir gün)*; عسر *(zorluk, güçlük)* korpusta 12 "
 "geçişli ve dikey ölçümü ▸önce kâfir x24,6 veriyor — kök korpusta zaten bu göndergeye bağlı."),
27: ("Ayet anlatıcıdan iç sese geçiyor ve geçiş şahıs sayımında görünüyor: 3MS x3 sonra 1S x3, "
 "yani ayetin ilk yarısı üçüncü şahıs anlatı, ikinci yarısı doğrudan alıntı. Ölçüm ilt=0 veriyor — "
 "çünkü geçiş ANLATICI değişimi değil, alıntı açılması. Pişmanlık bir bedensel eylemle veriliyor: "
 "يَعَضُّ … عَلَىٰ يَدَيْهِ *(ellerini ısırır)*; عضض *(ısırma)* korpusta İKİ geçişli (3:119, "
 "25:27) ve ötekinde de öfke bağlamında — dikey ölçüm ▸önce غيظ *(öfke, gayz)* x1310,7 veriyor, "
 "yani kökün iki geçişinden biri öfkeye bitişik. Ve سبل *(yol)* sûrenin üçüncü kez aynı alanda: "
 "25:9'da bulunamayan yol, 25:17'de saptıranın sorulduğu yol, burada tutulmamış yol."),
28: ("SÛRENİN İLK ★★★ AYETİ ve yıldızın TEK kaynağı bir hapaks: فُلَانًا *(falanca)*, فلن *(falan, "
 "filan kimse)* kökü, korpusta TEK geçiş (hapaks z=3,38). Ölçülebilir bir adsızlaştırma: ayet bir "
 "kişiden söz ediyor ve o kişiyi adlandırmayı REDDEDİYOR — Kur'ân'ın 'falanca' diyen tek yeri. "
 "Altı kelime, dört mansûb isim, tek fiil ve o da olumsuz temenni. Ve fiil önceki ayetten geliyor: "
 "أخذ *(alma, edinme)* bab VIII, 25:27'de ٱتَّخَذْتُ *(tutsaydım)* olumlu temenni, burada لَمْ "
 "أَتَّخِذْ *(edinmeseydim)* olumsuz temenni. Aynı kök, aynı bab, ters işaret, bitişik ayet. "
 "خلل *(dostluk, halîl; aralık)* korpusta 45 geçişli ve dikey ölçümü ▸önce edinme x15,0 veriyor — "
 "'dost edinme' korpusta sabit bir eşleşme."),
29: ("Sorumluluk devri tek fiille yapılıyor: أَضَلَّنِى *(beni saptırdı)*, ضلل *(sapma, saptırma)* "
 "bab IV, yani geçişli. 25:17'de tam bu çatı farkı bir sorunun konusuydu (أَضْلَلْتُمْ *(siz mi "
 "saptırdınız)* / ضَلُّوا۟ *(kendileri mi saptı)*); burada sapan taraf geçişli çatıyı seçiyor. "
 "Nesne 25:18'den geri geliyor: ٱلذِّكْر *(zikir)* — orada نَسُوا۟ ٱلذِّكْرَ *(zikri unuttular)*, "
 "burada عَنِ ٱلذِّكْرِ *(zikirden)*; aynı nesne, biri unutma biri saptırılma. Kapanış bir genelleme "
 "ve göndergeyi türe genişletiyor: لِلْإِنسَٰنِ *(insana)*, tekil ve cins. خذل *(yardımsız "
 "bırakma)* korpusta 4 geçişli ve dikey ölçümü ▸önce insan x232,1 veriyor — kök korpusta neredeyse "
 "yalnız bu göndergeyle."),
30: ("Yıldızın tek kaynağı tek bir رَبّ *(Rab)* geçişi (rab z=2,05) ve o geçiş sûrede ilk kez NİDA "
 "hâlinde: يَٰرَبِّ *(Rabbim)*. Ölçülebilir bir yön değişimi — sûrenin önceki üç Rab'bi anlatı "
 "içindeydi (25:16 عَلَىٰ رَبِّكَ, 25:20 رَبُّكَ, 25:21 رَبَّنَا bir istek içinde), bu ilk doğrudan "
 "çağrı. Şikâyetin nesnesi sûrenin ikinci adlı aktörü: ٱلْقُرْءَان *(Kur'ân)*, rol mef'ûl. Ve fiil "
 "yine أخذ *(alma, edinme)* bab VIII — üç ayette üçüncü kez ve üçüncü özneyle: 25:27 zalim, 25:28 "
 "zalim, burada kavim. هجر *(terk etme, hicret)* korpusta 31 geçişli ve dikey ölçümü ▸sonra "
 "güzellik x11,7 veriyor (هَجْرًۭا جَمِيلًۭا *(güzel bir ayrılış)* kalıbından) — burada o kalıp "
 "YOK, terk tek başına ve olumsuz."),
}

ATLAMA = {
 "_mercek_25_28": ("25:28 ★★★ — 🜁 BİYOLOG VE 🜂 UZAY MERCEKLERİ YAZILMADI, ÇIPA YOK. Ayet altı "
  "kelime: يَٰوَيْلَتَىٰ لَيْتَنِى لَمْ أَتَّخِذْ فُلَانًا خَلِيلًۭا *(vay bana, keşke falancayı "
  "dost edinmeseydim)*. İçerik tamamen kişilerarası ve temenni kipinde; ne canlı, ne organ, ne "
  "gök cismi, ne ölçü, ne süreç anılıyor. Yıldızın kaynağı da içerik değil: TEK kaynak hapaks "
  "z=3,38 (فلن *(falan, filan kimse)*, korpusta tek geçiş). **BU, ADAY 512'NİN EN TEMİZ VAKASI "
  "OLARAK KAYDEDİLİR** (aday 553): sûrenin ilk ★★★ ayeti, çıpası SIFIR olan bir ayet, ve yıldızı "
  "tek bir sözlük istatistiğinden geliyor. 'Dostluk seçiminin sosyal bulaşma modeli' türünden bir "
  "okuma YASAKLI 'bilimsel izdüşüm' olurdu — metin böyle bir şey söylemiyor."),
 "_mercek_25_25": ("25:25 ★★ — mercek eşiği ★★★ olduğu için uzman merceği zaten yazılmazdı, ama "
  "ÇIPA TANIMI için kaydedilir: bu ayette gerçek bir gök öğesi var (ٱلسَّمَآء *(gök)* yarılıyor, "
  "ٱلْغَمَٰم *(bulutlar)* aracı). Yani sûre 25'in ilk yirmi sekiz ayetinde ÇIPALI ayet ★★ alıyor, "
  "ÇIPASIZ ayet ★★★ alıyor. Aday 512'nin sûre 24'teki ayrışması (24:45 biyolojik olarak en yoğun "
  "ayet ★ alıyordu) burada TERS YÖNDE tekrarlanıyor."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(21, 31):
    OM['25']["25:%d" % n] = {"ar": AR[(25, n)], "meal": MEAL[n], "olcum": OLCUM[n],
                             "mercek": MERCEK[n], "dikey": DIK["25:%d" % n]}
OM['25']['_mercek_atlama_notu'].update(ATLAMA)
OM['25']['_blok_bolme_notu'] += (" ÜÇÜNCÜ BÖLME: blok 25:21-40 de ikiye bölündü (25:21-30 ve "
 "25:31-40). Gerekçe ölçüm: 25:30 elçinin şikâyetiyle bir bölütü kapatıyor ve 25:31 "
 "وَكَذَٰلِكَ جَعَلْنَا لِكُلِّ نَبِىٍّ عَدُوًّۭا *(böylece her peygambere bir düşman kıldık)* ile "
 "yeni bir hareket açıyor; ayrıca 25:21-30 sûrenin ilk ★★★ ayetini (25:28) ve iki ★★ ayetini "
 "(25:25, 25:30) birlikte taşıyor, mercek kaydı bölünmeden yazılsın diye ayrı tutuldu.")
OM['ilerleme']['not'] = ("Sûre 23 TAM (118/118). Sûre 24 TAM (64/64). **Sûre 25 (Furkān) 30/77.** "
                         "Devam: 25:31'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "25": "1-30 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1675
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 25 →', len([k for k in OM['25'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(21, 31):
    MK['25']["25:%d" % n] = MERCEK[n]
MK['25_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 25 →', len(MK['25']))
