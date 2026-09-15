# -*- coding: utf-8 -*-
"""blok_27_51_60.py — sûre 27 altıncı blok (27:51-60). Semûd'un kapanışı, Lût bölütü,
ve doğa bölütünün açılışı."""
import json
DIK = json.load(open('blok_dikey_27_51_60.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
51: "Bak, tuzaklarının sonu nasıl oldu: biz onları da kavimlerini de toptan yerle bir ettik.",
52: "İşte zulmetmeleri yüzünden ıssız kalmış evleri. Bilen bir topluluk için bunda bir işaret var.",
53: "İman edip sakınmakta olanları da kurtardık.",
54: "Lût'u da; kavmine demişti: Göz göre göre bu hayâsızlığı mı yapıyorsunuz?",
55: "Siz kadınları bırakıp şehvetle erkeklere mi gidiyorsunuz? Asıl siz bilgisizlik eden bir kavimsiniz.",
56: "Kavminin cevabı ancak şu olmuştu: Lût ailesini şehrinizden çıkarın; onlar temiz kalmak isteyen kimselermiş.",
57: "Onu ve ailesini kurtardık; karısı hariç — onu geride kalanlardan takdir ettik.",
58: "Üzerlerine bir yağmur yağdırdık; uyarılanların yağmuru ne kötüydü.",
59: "De ki: Hamd Allah'a, selâm da seçtiği kullarınadır. Allah mı hayırlı, yoksa ortak koştukları mı?",
60: "Yoksa gökleri ve yeri yaratan, size gökten su indiren mi? Onunla göz alıcı bahçeler bitirdik; onların ağacını bitirmek size düşmezdi. Allah'la beraber bir ilâh mı? Hayır, onlar sapan bir kavimdir.",
}

O = {
51: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir, kip IMPV 1 · şahıs 2MS x1 "
 "· 3MS x1 · 3MP x3 · 1P x3, baskın şahıs 3, iltifât 0 · n=9 mora=50 harf=41 (n z=-0,36), fâsıla "
 "أَجْمَعِينَ *(hepsi birden)* → ن, N sınıfı; **i'râb NOM 1 · GEN 1 · ACC 3**; bab I x2 · II x1; "
 "zaman IMPV 1 · PERF x2; dış düğüm 0 · yıldız ★ yok · kökler نظر *(bakma; mühlet verme)* · كيف *(nasıl, keyfiyet)* · كون *(olmak; mekân, yer)* · عقب *(sonuç, âkıbet)* · مكر *(tuzak)* · دمر *(yerle bir etme)* · "
 "قوم *(kalkma; kavim; kıyamet)* · جمع *(toplama)* · bağ: **نظر *(bakma; mühlet verme)* sûrede ALTINCI geçiş** ve yine 'sonucu bekleme' — kök sûre boyunca tek "
 "anlam alanında; **مكر *(tuzak)* 27:50'den sonra ikinci ayette, beşinci token** (elle, L1)"),
52: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip EMPH 1 · **şahıs 3MP "
 "x5, sahset ['3']** · n=11 mora=60 harf=50 (n z=-0,15), fâsıla يَعْلَمُونَ *(biliyorlar)* → ن, N "
 "sınıfı; **i'râb NOM 1 · ACC 3 · GEN 1**; bab I x2; zaman PERF 1 · IMPF 1; dış düğüm 0 · yıldız ★ "
 "yok · kökler بيت *(ev, mesken)* · خوي *(ıssız, boş)* · ظلم *(zulüm)* · أيي *(âyet, işaret)* · قوم *(kalkma; kavim; kıyamet)* · علم *(bilme)* · bağ: **خوي *(ıssız, boş)* korpusta beş geçişli ve dikey satırı "
 "▸sonra arş-taht ×167,7 veriyor — 27:23 ve 27:26'da عرش *(arş, taht)* okunurken bu satır uyarıyla "
 "işaretlenmişti; ölçüldü: üç ayrı ayetten geliyor (2:259, 18:42, 22:45)**, yani tek ayet değil "
 "tek KALIP (elle, L1, aday 835)"),
53: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber · şahıs 1P x2 · 3MP x6, "
 "sahset ['1','3'], iltifât 0 · **n=5 — sûrenin okunan en kısa ayetlerinden** (27:31 ile eşit; n "
 "z=-0,79), fâsıla يَتَّقُونَ *(sakınıyorlar)* → ن, N sınıfı; **i'râb boş**; bab I x1 · IV x2 · "
 "**VIII x1**; zaman PERF x3 · IMPF 1; dış düğüm 0 · yıldız ★ yok · kökler نجو *(kurtulma, kurtarma)* · أمن *(güven; iman)* · كون *(olmak; mekân, yer)* · وقي *(sakınma, koruma)* · "
 "bağ: **نجو *(kurtulma, kurtarma)* bu blokta iki kez (27:53 ve 27:57) — iki ayrı kavmin "
 "kurtuluşu, aynı kök, dört ayet arayla**; Semûd bölütü burada kapanıyor (27:45-53, dokuz ayet) "
 "(elle, L1)"),
54: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı لُوط *(Lût)* 1. sırada, tür kişi, "
 "rol MEF'ÛL** · edim soru, kip INTG 1 · şahıs 3MS x2 · 2MP x5, sahset ['2','3'], iltifât 0 · n=8 "
 "mora=52 harf=39 (n z=-0,47), fâsıla تُبْصِرُونَ *(görüyorsunuz)* → ن, N sınıfı; **i'râb ACC 2 · "
 "GEN 1**; bab I x2 · IV x1; zaman PERF 1 · IMPF x2; dış düğüm 2 · yıldız ★ yok · kökler قول *(söz söyleme)* · قوم *(kalkma; kavim; kıyamet)* "
 "· أتي *(gelme, getirme)* · فحش *(çirkinlik, hayâsızlık (fahşâ))* · بصر *(görme)* · bağ: xref قال + قوم *(kalkma; kavim; kıyamet)* + أتى → **7:80 · 29:28**; قوم *(kalkma; kavim; kıyamet)* + أتى + فاحشة → **7:80 · "
 "29:28**; **SÛRENİN DÖRDÜNCÜ ANLATI BÖLÜTÜ AÇILIYOR** — Lût (27:54-58, beş ayet) (elle, L1, aday "
 "839)"),
55: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · EMPH 1 · "
 "**şahıs 2MP x6, sahset ['2'] — blokta tek muhatap-şahıslı ayet** · iltifât 0 · n=11 mora=62 "
 "harf=50 (n z=-0,15), fâsıla تَجْهَلُونَ *(bilgisizlik ediyorsunuz)* → ن, N sınıfı; **i'râb ACC 3 "
 "· GEN 2 · NOM 1**; bab I x2; **zaman IMPF x2 — iki fiilin ikisi de muzari**; **biçim IDRAB**; "
 "dış düğüm 1 · yıldız ★ yok · kökler أتي *(gelme, getirme)* · رجل *(adam; yaya)* · شهو *(iştah, arzu)* · دون *(beriki, başkası)* · نسو *(kadınlar)* · قوم *(kalkma; kavim; kıyamet)* · جهل *(cehalet)* · bağ: **xref DÖRT "
 "3-gram ve DÖRDÜ DE TEK AYETE: 7:81** — أتى + رجال + شهوة · رجال + شهوة + دون *(beriki, başkası)* · شهوة + دون *(beriki, başkası)* + "
 "نساء · دون *(beriki, başkası)* + نساء + قوم *(kalkma; kavim; kıyamet)*; **aday 797'nin 'xref yoğunluğu' ölçütüne üçüncü veri** (27:19'da dokuz "
 "3-gram'ın sekizi tek ayete, 27:10'da altı bağ) (elle, L2)"),
56: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı لُوط *(Lût)* 10. sırada, tür kişi, "
 "rol mecrur** · edim emir, kip NEG 1 · RES 1 · IMPV 1 · şahıs 3MS x2 · 3MP x5 · 2MP x3, baskın "
 "şahıs 3, iltifât 0 · **n=15 — blokta ikinci en uzun ayet** (n z=0,27), fâsıla يَتَطَهَّرُونَ "
 "*(temiz kalıyorlar)* → ن, N sınıfı; **i'râb ACC 3 · GEN 3 · NOM 1**; bab I x2 · IV x1 · **bab V "
 "x1**; zaman PERF x2 · IMPV 1 · IMPF 1; simetri [3,5,10,1]; **biçim HASR**; **dış düğüm 3** · "
 "yıldız ★ yok · kökler كون *(olmak; mekân, yer)* · جوب *(cevap verme, icabet)* · قوم *(kalkma; kavim; kıyamet)* · قول *(söz söyleme)* · خرج *(çıkma, çıkarma)* · أول *(ilk, evvel)* · قري *(şehir, kasaba (karye))* · أنس *(insan)* · طهر *(temizlenme, tahâret)* · bağ: xref كان + "
 "جواب + قوم *(kalkma; kavim; kıyamet)* → **7:82 · 29:24 · 29:29**; جواب + قوم *(kalkma; kavim; kıyamet)* + قال → **7:82 · 29:24 · 29:29**; قوم *(kalkma; kavim; kıyamet)* + قال + "
 "أخرج → **7:82**; قرية + إنسان + تطهّر → **7:82** (elle, L2)"),
57: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: YOK — ٱمْرَأَتَهُۥ *(karısı)* adsız "
 "aktör tablosuna GİRMİYOR; alanın YANLIŞ NEGATİFİ** · edim haber, kip RES 1 · şahıs 1P x4 · 3MS "
 "x3 · 3FS x1, iltifât 0 · **n=7 — blokta en kısa ayetlerden** (n z=-0,58), fâsıla ٱلْغَٰبِرِينَ "
 "*(geride kalanlar)* → ن, N sınıfı; **i'râb ACC 2 · GEN 1**; bab II x1 · IV x1; zaman PERF x2; "
 "**biçim HASR**; dış düğüm 2 · yıldız ★ yok · kökler نجو *(kurtulma, kurtarma)* · أهل *(halk, aile)* · **مرأ *(kişi; kadın (imrae))*** "
 "· قدر *(ölçü, güç yetirme)* · غبر *(geride kalma; toz)* · bağ: xref أنجى + أهل *(halk, aile)* + امرأت → **7:83**; امرأت + قدّر + غابر → **15:60**; "
 "**dikey satır bu ayeti ÖNCEDEN İŞARET ETMİŞTİ: 27:23'te مرأ *(kişi; kadın (imrae))* ▸sonra geride-kalan ×126,4 "
 "okunmuştu ve uyarıyla geçilmişti; ölçüldü — beş ayrı ayetten geliyor (7:83, 15:60, 27:57, "
 "29:32, 29:33) ve BEŞİ DE AYNI SAHNE** (elle, L1, aday 833/835)"),
58: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber · şahıs 1P x2 · 3MP x1 · "
 "3MS x1, iltifât 0 · **n=6 — blokta en kısa ayet** (n z=-0,68), fâsıla ٱلْمُنذَرِينَ "
 "*(uyarılanlar)* → ن, N sınıfı; **i'râb ACC 1 · NOM 1 · GEN 1**; bab I x1 · IV x1; zaman PERF x2; "
 "**kök ikilemesi مطر *(yağmur; yağdırma)* x3 — n=6'lık ayette tek kök ÜÇ kez, oran 0,50**; "
 "**`esit` ALANI DOLU: [[26,173]] — sûre 27'de esit dolu üç ayetten biri (27:3, 27:58, 27:71) ve "
 "okumada ilki**; dış düğüm 1 · yıldız ★ yok · kökler مطر *(yağmur; yağdırma)* · سوأ *(kötülük)* · نذر *(uyarma; adak)* · bağ: xref أمطرت + مطر *(yağmur; yağdırma)* + "
 "ساء · مطر *(yağmur; yağdırma)* + ساء + مطر *(yağmur; yağdırma)* · ساء + مطر *(yağmur; yağdırma)* + منذر → **ÜÇÜ DE 26:173** (elle, L1, aday 834/839)"),
59: ("eksen: **ALLAH LAFZI İKİ KEZ — 3. ve 9. sırada** (allah z=2,80: **sûrenin en yüksek eksen "
 "z'si**) · Rab yok · **esmâ سَلام *(selâm, esenlik)* 4. sırada, ORTA konum, MÜHÜRSÜZ — "
 "ARTEFAKT**: gönderge وَسَلَٰمٌ عَلَىٰ عِبَادِهِ *(kullarına selâm)*, bir SELAMLAMA · aktör yok · "
 "edim soru + emir, kip IMPV 1 · INTG 1 · şahıs 2MS x1 · 3MS x2 · 3MP x2, iltifât 0 · n=12 mora=67 "
 "harf=50 (n z=-0,04), fâsıla يُشْرِكُونَ *(ortak koşuyorlar)* → ن, N sınıfı; **i'râb NOM 4 · GEN "
 "2**; bab I x1 · IV x1 · **VIII x1**; zaman IMPV 1 · PERF 1 · IMPF 1; **kök ikilemesi أله *(ilâh; lafza-i celâl)* x2 — "
 "ٱللَّهِ ve ءَآللَّهُ**; simetri [3,3,9,1]; **biçim AMMA**; dış düğüm 0 · **yıldız ★★** — kaynak "
 "YALNIZ eksen · kökler قول *(söz söyleme)* · حمد *(hamd, övgü)* · أله *(ilâh; lafza-i celâl)* · سلم *(esenlik; teslim olma)* · عبد *(kul, kulluk)* · صفو *(seçme, ıstıfâ; safâ)* · خير *(hayır, daha iyi)* · شرك *(ortak koşma)* · bağ: **sûrenin ikinci ve "
 "en yoğun eksen kümesi burada başlıyor: 27:59-65 arasında yedi ayetin YEDİSİNDE de lafız var** "
 "(elle, L1, aday 836/837)"),
60: ("eksen: **ALLAH LAFZI 23. sırada** (allah z=0,21) · Rab yok · esmâ yok · aktör yok · edim "
 "soru, kip NEG 1 · INTG 1 · şahıs 3MS x4 · 2MP x4 · 1P x2 · 3FS x1 · 3MP x3, baskın şahıs 3, "
 "iltifât 0 · **n=27 — sûrenin üçüncü en uzun ayeti** (n z=1,55), mora=135 harf=112, fâsıla "
 "يَعْدِلُونَ *(sapıyorlar)* → ن, N sınıfı; **i'râb GEN 4 · ACC 5 · NOM 3**; bab I x3 · IV x3; "
 "zaman PERF x4 · IMPF x2; **ÜÇ KÖK İKİLENİYOR: سمو *(ad; gök)* x2 · نبت *(bitki, bitme)* x2 · أله *(ilâh; lafza-i celâl)* x2**; simetri [4,15,22,1]; "
 "**biçim IDRAB**; dış düğüm 2 · **yıldız ★** — kaynak YALNIZ uzunluk · kökler خلق *(yaratma)* · سمو *(ad; gök)* · أرض *(yer, yeryüzü)* · "
 "نزل *(inme, indirme)* · موه *(su)* · نبت *(bitki, bitme)* · **حدق *(bahçe (hadîka))* — YENİ KÖK, n=3** · بهج *(göz alıcılık, bahçe)* · كون *(olmak; mekân, yer)* · شجر *(ağaç)* · أله *(ilâh; lafza-i celâl)* · قوم *(kalkma; kavim; kıyamet)* · عدل *(adalet)* "
 "· bağ: xref سماء + أرض *(yer, yeryüzü)* + أنزل ve أرض *(yer, yeryüzü)* + أنزل + سماء → **14:32**; سماء + ماء + أنۢبت → **31:10**; "
 "**SÛRENİN DOĞA BÖLÜTÜ BURADA AÇILIYOR (27:60-64, beş ayet)** (elle, L2, aday 838)"),
}

M = {
51: ("Tuzağın sonucu bir bakış emriyle veriliyor: فَٱنظُرْ كَيْفَ كَانَ عَٰقِبَةُ مَكْرِهِمْ *(bak, "
 "tuzaklarının sonu nasıl oldu)*. **Ölçülebilir bir kök izi: نظر *(bakma; mühlet verme)* sûrede ALTINCI geçiş ve altısı da "
 "'sonucu bekleme' bağlamında** — 27:27, 28, 33, 35, 41, 51. Kök korpusta 129 geçişli ve dikey "
 "ölçümü ▸sonra âkıbet ×29,7 · كيف *(nasıl, keyfiyet)* ×23,3 veriyor; **bu ayette üç kök de yan yana: نظر *(bakma; mühlet verme)* + كيف *(nasıl, keyfiyet)* + "
 "عقب *(sonuç, âkıbet)*.** Yani dikey satırın öncelikli iki ortağı burada metinde birebir görünüyor — **satırın "
 "kalıbı doğrulandı, ama bu bir keşif değil: kalıp zaten korpusta on dört kez tekrar eden donmuş "
 "bir terkip.** دمر *(yerle bir etme)* korpusta on geçişli."),
52: ("Issız evler bir işaret sayılıyor. Ölçülebilir bir geri dönüş: **خوي *(ıssız, boş)* korpusta "
 "beş geçişli ve dikey satırı ▸sonra arş-taht ×167,7 veriyor — bu satır 27:23 ve 27:26'da عرش *(arş, taht)* "
 "okunurken uyarıyla işaretlenmişti.** Şimdi kökün kendisine geldik. Ölçüldü: satır **üç ayrı "
 "ayetten** geliyor (2:259, 18:42, 22:45) ve üçü de aynı kalıbın varyantı — 'çatıları üstüne "
 "çökmüş ıssız yapı'. **Yani tek ayetten değil tek KALIPTAN; aday 806'nın eşiğinde 3-5 bandında, "
 "'uyarı' kategorisinde.** Ve burada kalıbın kendisi metinde yok: 27:52'de عرش *(arş, taht)* geçmiyor, yalnız "
 "خَاوِيَة var. **Dikey satır kalıbı taşıyor, ayeti değil.**"),
53: ("Beş kelime, dört kök. **نجو *(kurtulma, kurtarma)* bu blokta iki kez geçecek** — burada "
 "Semûd'un müminleri, 27:57'de Lût ve ailesi; **iki ayrı kavim, aynı kök, dört ayet arayla, ikisi "
 "de 1P fâille (أَنجَيْنَا).** Semûd bölütü burada kapanıyor: 27:45-53, dokuz ayet. Bölüt "
 "yapısı sabit — gönderme, uyarı, komplo, helâk, kurtarılanlar. **Sûre 26'daki Semûd bölütü "
 "(26:141-159) on dokuz ayet ve nakaratlı; buradaki dokuz ayet ve nakaratsız** (aday 829'un "
 "sınama çifti). وقي *(sakınma, koruma)* korpusta 258 geçişli."),
54: ("**Sûrenin dördüncü anlatı bölütü açılıyor: Lût (27:54-58, BEŞ ayet).** Bölüt uzunlukları "
 "ölçülebilir bir dizi veriyor: Mûsâ 27:7-14 (sekiz) · Dâvûd-Süleymân 27:15-44 (otuz) · Semûd "
 "27:45-53 (dokuz) · Lût 27:54-58 (beş). **Dört bölüt, uzunlukları 8 · 30 · 9 · 5 — ortadaki "
 "bölüt diğer üçünün toplamının üstünde.** Ve xref iki ayrı sûreye tek kalıpla bağlanıyor: قال + "
 "قوم *(kalkma; kavim; kıyamet)* + أتى ve قوم *(kalkma; kavim; kıyamet)* + أتى + فاحشة, ikisi de **7:80 ve 29:28**. فحش *(çirkinlik, hayâsızlık)* "
 "korpusta 24 geçişli."),
55: ("**Ölçülebilir bir xref yoğunluğu: dört 3-gram ve dördü de TEK ayete düşüyor — 7:81.** "
 "Aday 797'nin 'xref yoğunluğu' ölçütüne üçüncü veri: 27:10'da altı bağ, 27:19'da dokuz 3-gram'ın "
 "sekizi tek ayete, burada dördün dördü. **Üç vakanın üçünde de hedef ayet bir BAŞKA SÛREDEKİ "
 "aynı sahnenin anlatımı.** Bu, xref yoğunluğunun ölçtüğü şeyi netleştiriyor: **ortak kelime "
 "değil, ortak SAHNE.** Ayet blokta tek muhatap-şahıslı ayet (sahset yalnız 2) — altı işaretin "
 "altısı da 2MP. شهو *(iştah, arzu)* korpusta on üç geçişli; جهل *(cehalet)* 24."),
56: ("Cevap bir çıkarma emri: أَخْرِجُوٓا۟ ءَالَ لُوطٍ مِّن قَرْيَتِكُمْ *(Lût ailesini şehrinizden "
 "çıkarın)*. Biçim HASR — فَمَا كَانَ ... إِلَّآ, yani 'cevabı ancak şu oldu'. **Dış düğüm üç ve "
 "xref dört bağın üçü 7:82'ye, ikisi 29:24 ve 29:29'a düşüyor; yani aynı sahne korpusta en az üç "
 "sûrede anlatılıyor ve terkipler neredeyse birebir.** Ve bir ters çevirme: **طهر *(temizlenme, "
 "tahâret)* burada bir SUÇLAMA olarak kullanılıyor** — 'onlar temiz kalmak isteyen kimselermiş'. "
 "Kök korpusta 31 geçişli ve dikey satırı ▸önce sevgi ×14,0 · ev ×10,7 veriyor, yani korpusta "
 "ağırlıkla olumlu bağlamda; **bu ayet kökün kutbunu tersine çeviren bir vaka.**"),
57: ("**Adsız aktör alanının YANLIŞ NEGATİFİ burada görünüyor.** ٱمْرَأَتَهُۥ *(karısı)* gerçek bir "
 "adsız aktör — Lût'un karısı, adı verilmeyen ve anlatıda rolü olan bir kişi — ve alan onu "
 "SAYMIYOR. Aday 802'de alanın yanlış pozitiflerini ölçmüştüm (11 tokenin 7'si hatalı); **şimdi "
 "yanlış negatifleri de ölçtüm: korpusta امْرَأَت lemmalı 25 ayet var, alan yalnız DÖRDÜNÜ "
 "yakalıyor.** Mekanizma kesin: **yakalanan dördünün dördü de INDEF (belirsiz), kaçan yirmi "
 "ikisinin yirmi ikisi de belirli ya da izâfetli — istisna sıfır.** Yani alan 'adsız'ı "
 "'belirsiz'le karıştırıyor; **Lût'un karısı, Firavun'un karısı, İmrân'ın karısı — adı verilmeyen "
 "ama dilbilgisel olarak belirli aktörlerin tamamı görünmez.** Ve dikey satır bu ayeti önceden "
 "işaret etmişti: 27:23'te مرأ *(kişi; kadın (imrae))* ▸sonra geride-kalan ×126,4 okunmuş ve uyarıyla geçilmişti; ölçüldü "
 "— **beş ayrı ayetten geliyor ve beşi de aynı sahne** (7:83, 15:60, 27:57, 29:32, 29:33)."),
58: ("**`esit` alanı okumada ilk kez dolu: [[26,173]].** Sûre 27'de esit dolu üç ayet var (27:3, "
 "27:58, 27:71) ve bu ikincisi. Eşleşme sağlam: **üç xref 3-gram'ın üçü de aynı ayete, 26:173'e "
 "düşüyor** ve iki ayet neredeyse birebir. **Bu, aday 829'un sınama çiftini ayet düzeyine "
 "indiriyor: aynı kavim, aynı cümle, iki sûre — biri nakaratlı bölütte (26:160-175, on altı "
 "ayet), diğeri nakaratsız bölütte (27:54-58, beş ayet).** Nakarat alanının yeniden tanımı (P0 #4) "
 "için bundan daha temiz bir çift zor bulunur. Ve ayet kendi içinde bir yoğunluk taşıyor: **مطر *(yağmur; yağdırma)* "
 "*(yağmur; yağdırma)* n=6'lık ayette üç kez, oran 0,50** — 27:50'nin مكر *(tuzak)* ×4'ünden sonra blokta "
 "ikinci tek-kök yoğunluğu."),
59: ("**Sûrenin en yüksek eksen z'si burada: allah z=2,80**, çünkü n=12'lik bir ayette lafız İKİ "
 "kez ve ikisi de ayetin ilk yarısında (3. ve 9. sıra). **Yıldızın kaynağı yalnız eksen — okumada "
 "ilk kez bir ayet ★★'yi tek başına eksenden alıyor** (27:26 ★★ almıştı ama orada lafız ve Rab "
 "birlikteydi). Ve bu, 27:44'ün tersi: orada üç eksen işareti n=28'de seyrelmişti, burada iki "
 "işaret n=12'de yoğunlaşıyor. **İkisi birlikte z'nin uzunluk normalizasyonunun ne yaptığını "
 "gösteriyor** (aday 827). Esmâ tarafında سَلام *(selâm, esenlik)* mühürsüz ve göndergesi bir "
 "selamlama — **ARTEFAKT; aday 818'in ikinci sınaması da geçti, ayrım 10/10 ve 0/15.** Sûrenin "
 "ikinci eksen kümesi burada başlıyor: **27:59-65 arasında yedi ayetin YEDİSİNDE de lafız var** "
 "— sûrenin kendi azamisi ve 27:43-49'un 6/7'sinden bir yukarısı."),
60: ("**Sûrenin doğa bölütü burada açılıyor (27:60-64, beş ayet)** ve anlatıdan tabiata geçiş "
 "bir soru kalıbıyla yapılıyor: أَمَّنْ خَلَقَ *(yoksa yaratan mı)*. Üç kök ikileniyor ve "
 "**نبت *(bitki, bitme)* ikisi de aynı süreçte: فَأَنۢبَتْنَا *(bitirdik)* ve أَن تُنۢبِتُوا۟ "
 "*(bitirmeniz)* — aynı fiil, biri ilâhî fâille biri insan fâille, ve ikincisi olumsuzlanıyor.** "
 "**SINIR — ÇIPA DEĞERLENDİRMESİ (aday 799 ölçütüyle): ayet bir NEDENSEL BAĞIMLILIK kuruyor "
 "(gökten su → bahçeler) ve bir YETİ SINIRI koyuyor (ağacı siz bitiremezdiniz). Bu, sûrede "
 "şimdiye kadarki en çıpaya yakın yapı — 'adlandırma' değil, bir süreç ve bir kısıt. Ama ölçü "
 "yok, mekanizma açılmıyor, sınıflandırma yok: su neyi nasıl yapar, ağaç neden insan elinden "
 "çıkmaz — bunlar söylenmiyor. Eşik yine aşılmadı; ama bu vaka eşiğin NEREDE olduğunu sûrede en "
 "iyi gösteren örnek.** Ve ölçülebilir sonuç: **ayet ★ alıyor ve kaynağı yalnız uzunluk** "
 "(n z=1,55); eksen işareti 23. sırada ve z=0,21. **Sûrenin doğaya en yakın ayeti, doğadan değil "
 "uzunluktan yıldız alıyor** — aday 599/602/809'un dizisine dördüncü gösterim."),
}

ATLAMA = {
 "_mercek_27_60": ("27:60 ★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. (Kural ★★★ için; bu ayet ★, ama "
  "sûrenin doğa bölütünün açılışı olduğu için ayrıca değerlendirildi.) Ayet bir NEDENSEL "
  "BAĞIMLILIK (gökten su → göz alıcı bahçeler) ve bir YETİ SINIRI (ağacını siz bitiremezdiniz) "
  "kuruyor — sûrede şimdiye kadarki en çıpaya yakın yapı. **Ama ölçü, mekanizma ve "
  "sınıflandırma yok**: suyun ne yaptığı, ağacın neden insan elinden çıkmadığı açılmıyor. Aday "
  "799'un ölçütüyle eşik aşılmadı; **bu vaka eşiğin nerede durduğunu sûrede en iyi gösteren "
  "örnek olarak kaydedildi.**"),
 "_blok_notu_27_51_60": ("BLOK BİLANÇOSU: ★★★ 0 · ★★ 1 (27:59, kaynak EKSEN) · ★ 1 (27:60, "
  "kaynak uzunluk) · yıldızsız 8. **Okumada ilk kez bir ayet ★★'yi tek başına eksenden aldı.** "
  "İltifât 0/10. Esmâ token 1 (27:59 سَلام, ARTEFAKT). Allah lafzı 3 (27:59 x2, 27:60) · Rab 0 "
  "— **okumada ilk kez bir blokta Rab hiç yok.** Adlı aktör 2 (لُوط x2) · adsız aktör 0 — ama "
  "**27:57'de gerçek bir adsız aktör var ve alan onu kaçırıyor** (aday 833). Yeni kök 1 (حدق *(bahçe (hadîka))*). "
  "Hapaks 0. Kafiye kırılması 0. **`esit` alanı okumada ilk kez dolu (27:58 ↔ 26:173).** "
  "**Dört blok üst üste yıldızsız oran ≥%80.**"),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(51, 61):
    OM['27']["27:%d" % n] = {"ar": AR[(27, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["27:%d" % n]}
OM['27']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-26 TAM. **Sûre 27 (Neml) 60/93.** Devam: 27:61'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "27": "1-60 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 2009
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 27 →', len([k for k in OM['27'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(51, 61):
    MK['27']["27:%d" % n] = M[n]
MK['27_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 27 →', len(MK['27']))
