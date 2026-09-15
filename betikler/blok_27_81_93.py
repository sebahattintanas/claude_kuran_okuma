# -*- coding: utf-8 -*-
"""blok_27_81_93.py — sûre 27 dokuzuncu ve SON blok (27:81-93). Diriliş sahnesi,
dağların yürüyüşü ve sûre kapanışı."""
import json
DIK = json.load(open('blok_dikey_27_81_93.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
81: "Sen körleri sapkınlıklarından çevirip yola getiremezsin; sen ancak âyetlerimize inananlara işittirebilirsin, işte onlar teslim olmuş olanlardır.",
82: "Söz başlarına geldiğinde, onlara yerden bir dâbbe çıkarırız; insanların âyetlerimize kesin inanmadıklarını onlara söyler.",
83: "O gün her ümmetten, âyetlerimizi yalanlayanlardan bir bölük toplarız; onlar bir arada tutulurlar.",
84: "Geldiklerinde der: Âyetlerimi, ilmen kuşatmadığınız hâlde mi yalanladınız? Yoksa ne yapıyordunuz?",
85: "Zulmetmeleri yüzünden söz başlarına gelir; artık konuşamazlar.",
86: "Görmediler mi, geceyi içinde dinlensinler diye, gündüzü de aydınlık kıldık. Bunda inanan bir topluluk için işaretler var.",
87: "Sûr'a üflendiği gün, göklerde ve yerde olanlar dehşete kapılır — Allah'ın dilediği hariç. Hepsi boyun eğerek O'na gelir.",
88: "Dağları görürsün, onları donuk sanırsın; oysa onlar bulutların geçişi gibi geçer. Bu, her şeyi sapasağlam yapan Allah'ın işidir. O, yaptıklarınızdan haberdardır.",
89: "Kim iyilikle gelirse ona ondan daha hayırlısı vardır; onlar o günün dehşetinden güvendedir.",
90: "Kim kötülükle gelirse, yüzleri ateşte sürtülür: yaptıklarınızdan başkasıyla mı karşılık görüyorsunuz?",
91: "Bana ancak, bu beldenin — orayı dokunulmaz kılanın — Rabbine kulluk etmem emredildi; her şey O'nundur. Ve teslim olanlardan olmam emredildi,",
92: "ve Kur'ân'ı okumam. Kim yola gelirse kendisi için gelmiş olur; kim saparsa de ki: Ben ancak uyarıcılardanım.",
93: "Ve de ki: Hamd Allah'a. O size âyetlerini gösterecek, siz de onları tanıyacaksınız. Rabbin yaptıklarınızdan habersiz değildir.",
}

O = {
81: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, **kip NEG 2** · RES 1 · "
 "şahıs 2MS x2 · 3MP x2 · 3MS x1 · 1P x1, iltifât 0 · n=14 (n z=0,17), fâsıla مُسْلِمُونَ *(teslim "
 "olmuşlar)* → ن, N sınıfı — **sûrede dördüncü kez bu kök fâsılada** (27:31, 38, 42, burası); "
 "**i'râb GEN 4 · NOM 1**; bab IV x2; **zaman IMPF x2**; simetri [3,1,9,1]; **biçim HASR**; dış "
 "düğüm 1 · yıldız ★ yok · kökler هدي *(yol gösterme)* · عمي *(körlük)* · ضلل *(sapma, saptırma)* · سمع *(işitme)* · أمن *(güven; iman)* · أيي *(âyet, işaret)* · سلم *(esenlik; teslim olma)* · bağ: **xref DÖRT "
 "3-gram ve dördü de TEK ayete: 30:53 — ve 30:53 ile aradaki tek fark بِهَٰدِى / بِهَٰدِ, yani "
 "KELİME İÇİNDE bir yâ harfi; `esit` alanı İKİSİNDE DE BOŞ** (elle, L2, aday 869)"),
82: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · şahıs 3MS x1 "
 "· **3MP x7** · 1P x3 · 3FS x1, baskın şahıs 3, iltifât 0 · n=16 (n z=0,38), fâsıla يُوقِنُونَ "
 "*(kesin inanıyorlar)* → ن, N sınıfı; **i'râb NOM 1 · ACC 3 · GEN 2**; bab I x2 · II x1 · IV x2; "
 "zaman PERF x3 · IMPF x2; dış düğüm 2 · yıldız ★ yok · kökler وقع *(düşme, vuku)* · قول *(söz söyleme)* · خرج *(çıkma, çıkarma)* · **دبب *(debelenen "
 "canlı (dâbbe))*, n=18** · أرض *(yer, yeryüzü)* · كلم *(söz, konuşma)* · أنس *(insan)* · كون *(olmak; mekân, yer)* · أيي *(âyet, işaret)* · يقن *(yakîn, kesin bilgi)* · bağ: xref ناس + كان + آية → "
 "**48:20**; كان + آية + يوقن → **32:24**; **يقن *(yakîn, kesin bilgi)* sûrede DÖRDÜNCÜ ve son "
 "geçiş** (27:3, 14, 22, burası); **خرج *(çıkma, çıkarma)* sûrede BEŞİNCİ geçiş ve beşinci 'çıkarılan': yerden bir "
 "canlı** (elle, L2)"),
83: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber · şahıs 1P x2 · 3MS x1 · "
 "3MP x3, sahset ['1','3'], iltifât 0 · n=11 (n z=-0,15), fâsıla يُوزَعُونَ *(bir arada "
 "tutuluyorlar)* → ن, N sınıfı; **i'râb ACC 2 · GEN 3**; bab I x2 · II x1; **zaman IMPF x3**; "
 "**edilgen 1** (يُوزَعُونَ), pas z=1,57: **yıldızın TEK kaynağı**; dış düğüm 0 · **yıldız ★** · "
 "kökler يوم *(gün)* · حشر *(toplama, mahşer)* · كلل *(hep, bütün)* · أمم *(ümmet, topluluk)* · **فوج *(bölük, grup (fevc))* — YENİ KÖK, n=5** · كذب *(yalan; yalanlama)* · أيي *(âyet, işaret)* · وزع *(dizip düzenleme; ilham verme)* "
 "· bağ: **وزع *(bir arada tutma, durdurma)* korpusta beş geçişli ve ikisi bu sûrede** (27:17, "
 "burası) — **27:17'de Süleymân'ın orduları 'bir arada tutuluyordu', burada mahşerde toplananlar; "
 "aynı nadir fiil, aynı sûre, altmış altı ayet arayla** (elle, L1, aday 873)"),
84: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · NEG 1 · şahıs "
 "3MP x2 · 3MS x1 · **2MP x8** · 1S x1 · 3FS x1, baskın şahıs 2, iltifât 0 · n=13 (n z=0,06), "
 "fâsıla تَعْمَلُونَ *(yapıyorsunuz)* → ن, N sınıfı — **blokta üç kez bu fâsıla** (27:84, 90, 93); "
 "**i'râb GEN 1 · ACC 1**; bab I x4 · II x1 · IV x1; zaman PERF x4 · IMPF x2; dış düğüm 1 · yıldız "
 "★ yok · kökler جيأ *(gelme)* · قول *(söz söyleme)* · كذب *(yalan; yalanlama)* · أيي *(âyet, işaret)* · حوط *(kuşatma)* · علم *(bilme)* · كون *(olmak; mekân, yer)* · عمل *(iş, amel)* · bağ: xref علم *(bilme)* + كان + عمل *(iş, amel)* → "
 "**26:112**; **حوط *(kuşatma)* sûrede İKİNCİ ve son geçiş** — 27:22'de hüdhüd 'senin "
 "kuşatamadığını kuşattım' demişti, burada 'ilmen kuşatmadığınız hâlde mi yalanladınız'; **aynı "
 "kök, aynı bilgi-kuşatma kalıbı, altmış iki ayet arayla** (elle, L2)"),
85: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · **şahıs 3MS "
 "x1 · 3MP x6, sahset ['3']** · **n=8** (n z=-0,47), fâsıla يَنطِقُونَ *(konuşuyorlar)* → ن, N "
 "sınıfı; **i'râb NOM 1**; **bab I x3**; zaman PERF x2 · IMPF 1; simetri [3,3,6,1]; dış düğüm 0 · "
 "yıldız ★ yok · kökler وقع *(düşme, vuku)* · قول *(söz söyleme)* · ظلم *(zulüm)* · **نطق *(konuşma, dile gelme)*, n=12** · bağ: **وقع *(düşme, vuku)* "
 "*(düşme, vuku)* 27:82'den sonra üç ayet arayla ikinci geçiş ve İKİSİ DE aynı terkip: وَقَعَ "
 "ٱلْقَوْلُ عَلَيْهِم *(söz başlarına geldi)*** — sûre içi üçüncü ayet-içi nakarat adayı; "
 "**`nakarat` alanı ikisinde de SIFIR** (elle, L1, aday 872)"),
86: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · NEG 1 · EMPH "
 "1 · **şahıs 3MP x6** · 1P x3 · 3MS x1, iltifât 0 · n=15 (n z=0,27), fâsıla يُؤْمِنُونَ "
 "*(inanıyorlar)* → ن, N sınıfı; **i'râb ACC 5 · GEN 2**; bab I x3 · IV x1; zaman IMPF x3 · PERF "
 "1; simetri [3,1,10,1]; dış düğüm 2 · **yıldız ★ YOK** · kökler رأي *(görme)* · جعل *(kılma, var etme)* · ليل *(gece)* · سكن *(sükûn; mesken, konut)* · نهر *(ırmak)* · بصر *(görme)* "
 "· أيي *(âyet, işaret)* · قوم *(kalkma; kavim; kıyamet)* · أمن *(güven; iman)* · bağ: xref ليل *(gece)* + سكن *(sükûn; mesken, konut)* + نهار ve türevleri → **10:67 · 40:61** (elle, L2, aday "
 "873)"),
87: ("eksen: **ALLAH LAFZI 15. sırada** (allah z=0,58) · Rab yok · esmâ yok · aktör yok · edim "
 "haber, kip RES 1 · **şahıs 3MS x4 · 3MP x2, sahset ['3']** · **n=18 — blokta en uzun ayetlerden** "
 "(n z=0,59), fâsıla دَٰخِرِينَ *(boyun eğenler)* → ن, N sınıfı; **i'râb ACC 2 · GEN 3 · NOM 2**; "
 "**bab I x4**; zaman IMPF 1 · PERF x3; **edilgen 1** (يُنفَخُ), pas z=1,10 — eşiğin altında; "
 "simetri [3,6,9,1]; **biçim HASR**; dış düğüm 1 · yıldız ★ yok · kökler يوم *(gün)* · نفخ *(üfleme)* · **صور *(sûr; "
 "biçim)*, n=19** · **فزع *(dehşet, ürküntü)*, n=6** · سمو *(ad; gök)* · أرض *(yer, yeryüzü)* · شيأ *(dileme; şey)* · أله *(ilâh; lafza-i celâl)* · كلل *(hep, bütün)* · أتي *(gelme, getirme)* · **دخر *(boyun eğme, küçülerek gelme)* "
 "*(boyun eğme, küçülerek gelme)* — YENİ KÖK, n=4** · bağ: xref أرض *(yer, yeryüzü)* + شاء + اللّه → **39:68**; "
 "**فزع *(dehşet, ürküntü)* 27:89'da tekrar gelecek — iki ayet arayla, biri dehşet biri ondan güvende olma** (elle, "
 "L2)"),
88: ("eksen: **ALLAH LAFZI 10. sırada** (allah z=0,58) · Rab yok · **esmâ خَبِير *(haberdar)* 16. "
 "sırada, ORTA konum, MÜHÜRSÜZ — GEÇERLİ**: gönderge إِنَّهُۥ, mercii صُنْعَ ٱللَّهِ; **sûrenin 21 "
 "mühürsüz esmâ tokeninin GEÇERLİ ÇIKAN TEK TANESİ** · aktör yok · edim haber · şahıs 2MS x1 · 3FS "
 "x4 · 3MS x2 · 2MP x2, baskın şahıs 3, iltifât 0 · **n=18** (n z=0,59), fâsıla تَفْعَلُونَ "
 "*(yapıyorsunuz)* → ن, N sınıfı; **i'râb ACC 6 · GEN 3 · NOM 1**; bab I x4 · IV x1; zaman IMPF x4 "
 "· PERF 1; **İKİ HAPAKS: تقن *(sağlam ve kusursuz yapma (itkān))* ve جمد *(donuk, hareketsiz "
 "duran)* — hapaks z=6,98, SÛRENİN EN YÜKSEK z DEĞERİ ve yıldızın TEK kaynağı**; **kök ikilemesi "
 "مرر *(kere, defa)* x2**; **biçim MM (mef'ûl-i mutlak) — korpusta yalnız ÜÇ ayette** (17:26, 27:88, 84:8); dış "
 "düğüm 0 · **yıldız ★★★** · kökler رأي *(görme)* · جبل *(dağ)* · حسب *(hesap, sayma)* · **جمد *(donuk, hareketsiz duran)* — YENİ KÖK, hapaks** · مرر *(kere, defa)* · سحب *(bulut; sürükleme)* · صنع *(yapma, işleme)* "
 "· أله *(ilâh; lafza-i celâl)* · **تقن *(sağlam ve kusursuz yapma (itkān))* — YENİ KÖK, hapaks** · كلل *(hep, bütün)* · شيأ *(dileme; şey)* · خبر *(haber; haberdar olma)* · فعل *(yapma, işleme)* (elle, L1, aday 865/866/867)"),
89: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber · **şahıs 3MS x2 · 3FS x1 "
 "· 3MP x1, sahset ['3']** · n=11 (n z=-0,15), fâsıla ءَامِنُونَ *(güvende olanlar)* → ن, N "
 "sınıfı; **i'râb GEN 2 · NOM 2**; **bab I x1 — ayetin tek fiili**; zaman PERF 1; dış düğüm 1 · "
 "yıldız ★ yok · kökler جيأ *(gelme)* · حسن *(güzellik, iyilik)* · خير *(hayır, daha iyi)* · فزع *(dehşet, ürküntü)* · يوم *(gün)* · أمن *(güven; iman)* · bağ: xref جاء + حسنة + خير *(hayır, daha iyi)* → "
 "**28:84**; **فزع *(dehşet, ürküntü)* 27:87'den sonra iki ayet arayla ikinci geçiş; kök korpusta "
 "ALTI geçişli ve ikisi bu sûrede** (elle, L2)"),
90: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · RES 1 · "
 "**şahıs 2MP x6** · 3MS x1 · 3FS x1 · 3MP x1, baskın şahıs 2, iltifât 0 · n=13 (n z=0,06), fâsıla "
 "تَعْمَلُونَ → ن, N sınıfı; **i'râb GEN 2 · NOM 1**; **bab I x5**; zaman PERF x3 · IMPF x2; "
 "**edilgen 2** (كُبَّتْ, تُجْزَوْنَ), pas z=1,95: **yıldızın TEK kaynağı**; **biçim HASR**; dış "
 "düğüm 0 · **yıldız ★** · kökler جيأ *(gelme)* · سوأ *(kötülük)* · **كبب *(yüzüstü kapaklanma)* — YENİ KÖK, n=2** · وجه *(yüz, yön)* "
 "· نور *(nûr, ışık)* · جزي *(karşılık verme)* · كون *(olmak; mekân, yer)* · عمل *(iş, amel)* · bağ: **27:89 ile karşıt çift: جاء بالحسنة / جاء بالسيئة — aynı fiil, "
 "aynı yapı, ardışık ayetler, zıt nesne** (elle, L1)"),
91: ("eksen: lafız yok · **رَبّ 5. sırada — sûrenin DOKUZUNCU Rabbi** (rab z=0,93) · esmâ yok · "
 "**aktör: adlı مُسْلِم *(müslim)* 17. sırada, tür KAVİM — DENETLENDİ, ARTEFAKT: cins isim, özel "
 "ad değil** · edim haber · **şahıs 1S x6** · 3MS x2 · 3FS x1, baskın şahıs 1, iltifât 0 · n=17 (n "
 "z=0,49), fâsıla ٱلْمُسْلِمِينَ *(teslim olanlar)* → ن, N sınıfı; **i'râb ACC 2 · GEN 3 · NOM 1**; "
 "bab I x4 · II x1; zaman PERF x3 · IMPF x2; **edilgen 2** (أُمِرْتُ x2), pas z=1,95: **yıldızın "
 "TEK kaynağı**; **kök ikilemesi أمر *(emir; iş)* x2 — ikisi de edilgen**; **biçim DIKKAT**; dış düğüm 2 · "
 "**yıldız ★** · kökler أمر *(emir; iş)* · عبد *(kul, kulluk)* · ربب *(rab, terbiye etme)* · **بلد *(belde, şehir)*, n=19** · حرم *(haram kılma, yasak)* · كلل *(hep, bütün)* · شيأ *(dileme; şey)* · كون *(olmak; mekân, yer)* · "
 "سلم *(esenlik; teslim olma)* · bağ: xref أمر *(emir; iş)* + كان + مسلم → **10:72**; كلّ + شىء + أمر *(emir; iş)* → **46:25** (elle, L2, aday 868)"),
92: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı قُرْءان *(Kur'ân)* 3. sırada, tür "
 "kitab, rol mef'ûl — sûrede ikinci ve son** · edim emir, kip IMPV 1 · şahıs 1S x2 · 3MS x4 · 2MS "
 "x1, sahset ['1','2','3'], iltifât 0 · n=15 (n z=0,27), fâsıla ٱلْمُنذِرِينَ *(uyarıcılar)* → ن, "
 "N sınıfı; **i'râb ACC 3 · GEN 2**; bab I x3 · **bab VIII x2**; zaman IMPF x2 · PERF x2 · IMPV 1; "
 "**kök ikilemesi هدي *(yol gösterme)* x2 — ٱهْتَدَىٰ ve يَهْتَدِى**; simetri [3,4,12,1]; dış düğüm 2 · yıldız ★ "
 "yok · kökler تلو *(okuma, ardından gelme)* · قرأ *(okuma)* · هدي *(yol gösterme)* · نفس *(nefis, can)* · ضلل *(sapma, saptırma)* · قول *(söz söyleme)* · نذر *(uyarma; adak)* · bağ: xref اهتدى + اهتدى + نفس *(nefis, can)* → **10:108 "
 "· 17:15**; **هدي *(yol gösterme)* sûrede YEDİNCİ ve SEKİZİNCİ geçiş; dört anlam alanının en sık olanına "
 "(hidâyet) dönüyor** (elle, L2)"),
93: ("eksen: **ALLAH LAFZI 3. sırada** (allah z=1,29) **· رَبّ 8. sırada — sûrenin ONUNCU ve SON "
 "Rabbi** (rab z=1,62) · esmâ yok · aktör yok · edim emir, kip IMPV 1 · FUT 1 · NEG 1 · şahıs 2MS "
 "x2 · 3MS x2 · 2MP x5 · 3FS x1, baskın şahıs 2, iltifât 0 · n=11 (n z=-0,15), fâsıla تَعْمَلُونَ "
 "→ ن, N sınıfı — **sûrenin son fâsılası ve blokta üçüncü kez**; **i'râb NOM 2 · GEN 3**; bab I x3 "
 "· IV x1; **dış düğüm 3** · **yıldız ★** — kaynak YALNIZ Rab · kökler قول *(söz söyleme)* · حمد *(hamd, övgü)* · أله *(ilâh; lafza-i celâl)* · رأي *(görme)* · "
 "أيي *(âyet, işaret)* · عرف *(tanıma)* · ربب *(rab, terbiye etme)* · غفل *(gaflet, habersizlik)* · عمل *(iş, amel)* · bağ: xref ربّ + غافل + عمل *(iş, amel)* → **6:132 · 11:123**; اللّه + أري + "
 "آية → **31:31**; **قُلِ ٱلْحَمْدُ لِلَّهِ 27:59'dan sonra sûrede ikinci kez ve sûreyi kapatıyor** "
 "(elle, L2)"),
}

M = {
81: ("**`esit` yanlış negatifinin ikinci vakası ve bu kez fark KELİME İÇİNDE.** Ayet 30:53 ile "
 "arasındaki tek fark بِهَٰدِى / بِهَٰدِ, yani bir yâ harfi; başka hiçbir fark yok. **`esit` alanı "
 "yine ikisinde de boş.** Bir önceki blokta 27:80 ↔ 30:52 farkı baştaki bir bağlaçtı; **burada "
 "fark kelimenin içinde — yani aday 854'ün önerdiği ucuz onarım (baştaki و/ف'yi kırp) bu vakayı "
 "YAKALAMAZ.** Ve xref yine doğru çalışıyor: dört 3-gram'ın dördü de 30:53'e düşüyor. **İki "
 "ardışık ayet (27:80, 27:81) iki ardışık ayetle (30:52, 30:53) neredeyse birebir eşleşiyor ve "
 "alan hiçbirini görmüyor.** Fâsıla سلم *(esenlik; teslim olma)* kökünden — sûrede dördüncü kez."),
82: ("Yerden bir canlı çıkıyor: دَآبَّةً مِّنَ ٱلْأَرْضِ. دبب *(debelenen canlı (dâbbe))* korpusta "
 "on sekiz geçişli. **Ölçülebilir bir kök izi: خرج *(çıkma, çıkarma)* sûrede BEŞİNCİ geçiş ve "
 "beşinci 'çıkarılan'** — gizli olan (27:25) · ordudan çıkarılanlar (27:37) · şehirden çıkarılacak "
 "aile (27:56) · topraktan çıkarılacak ölüler (27:67) · **yerden çıkarılan canlı (burası)**. Kök "
 "tek anlam alanında, nesnesi beş ayrı katmanda. Ve **يقن *(yakîn, kesin bilgi)* sûrede dördüncü "
 "ve son geçiş**: mümin (27:3) · inkârcı (27:14) · haber (27:22) · **insanların âyetlere kesin "
 "inanmayışı (burası)**."),
83: ("**Nadir bir fiilin sûre içi yankısı: وزع *(bir arada tutma, durdurma)* korpusta BEŞ geçişli "
 "ve ikisi bu sûrede.** 27:17'de Süleymân'ın orduları toplanıp 'bir arada tutuluyordu' "
 "(يُوزَعُونَ), burada mahşerde toplananlar aynı fiille tutuluyor — **aynı nadir fiil, aynı vezin, "
 "aynı edilgen çatı, altmış altı ayet arayla.** Sûrenin iki ucundaki iki toplanma sahnesi tek "
 "kelimeyle bağlanıyor. Ve yıldızın tek kaynağı yine edilgenlik (pas z=1,57). Yeni kök فوج *(bölük, grup (fevc))* "
 "*(bölük, grup (fevc))* korpusta beş geçişli."),
84: ("**حوط *(kuşatma)* sûrede ikinci ve son geçiş ve iki geçiş de 'bilgiyle kuşatma' kalıbında.** "
 "27:22'de hüdhüd أَحَطتُ بِمَا لَمْ تُحِطْ بِهِۦ *(senin kuşatamadığını kuşattım)* demişti; "
 "burada وَلَمْ تُحِيطُوا۟ بِهَا عِلْمًا *(onu ilmen kuşatmadığınız hâlde)*. **Altmış iki ayet "
 "arayla, biri bir kuşun bilgi üstünlüğü, diğeri insanın bilgi eksikliği; aynı kök, karşıt yön.** "
 "Sekiz 2MP işareti — blokta en yüksek muhatap yoğunluğu. Fâsıla تَعْمَلُونَ, blokta üç kez "
 "(27:84, 90, 93)."),
85: ("**Sûrenin üçüncü ayet-içi nakarat adayı burada tamamlanıyor: وَقَعَ ٱلْقَوْلُ عَلَيْهِم "
 "*(söz başlarına geldi)* — 27:82'de ve burada, üç ayet arayla, terkip birebir aynı.** وقع *(düşme, "
 "vuku)* korpusta yirmi dört geçişli. **`nakarat` alanı ikisinde de sıfır** — aday 844/845'in "
 "üçüncü vakası. Sûrenin üç ayet-içi nakaratı: `أَءِلَٰهٌ مَّعَ ٱللَّهِ` (beş kez) · `كَيْفَ كَانَ "
 "عَٰقِبَةُ` (üç kez) · `وَقَعَ ٱلْقَوْلُ عَلَيْهِم` (iki kez). **Alan üçünü de görmüyor.** نطق *(konuşma, söz söyleme)* "
 "*(konuşma, dile gelme)* korpusta on iki geçişli."),
86: ("Gece ve gündüz bir işaret olarak veriliyor. **Ve çıpa tablosunun sûredeki SON gösterimi: "
 "sûrenin okunan ikinci gök-cismi/doğa ayeti ve YILDIZSIZ.** 27:24 güneşe secdeyi anıyordu ve "
 "yıldızsızdı; 27:61 yerin dört yapısını sayıyordu ve yıldızsızdı; burada gece-gündüz döngüsü ve "
 "yine yıldızsız. **Sûrede doğaya değen ayetlerin toplam yıldız verimi: 27:60'ın uzunluktan aldığı "
 "bir ★.** سكن *(sükûn, dinginlik)* korpusta altmış dokuz geçişli. xref üç sûreye bağlanıyor "
 "(10:67, 40:61) — **donmuş bir gece-gündüz kalıbı.**"),
87: ("Sûr'a üfleniyor. **Ölçülebilir bir çift: فزع *(dehşet, ürküntü)* korpusta ALTI geçişli ve "
 "ikisi bu sûrede, iki ayet arayla** — burada dehşete kapılma, 27:89'da o dehşetten güvende olma. "
 "**Aynı nadir kök, aynı sahne, karşıt iki durum.** Yeni kök دخر *(boyun eğme, küçülerek gelme)* "
 "korpusta dört geçişli ve dikey satırı iki listede de boş. Ve نفخ *(üfleme)* ▸sonra sûr ×318,2 — ölçüldü: "
 "bu ikili korpusta **üç ayetten** geliyor, yani aday 835'in Tür B'si: **tek kalıp, üç yerde** "
 "(sûra üfürülme formülü)."),
88: ("**Sûrenin en yüksek z değeri burada: hapaks z=6,98** — iki hapaks birden, تقن *(sağlam ve "
 "kusursuz yapma (itkān))* ve جمد *(donuk, hareketsiz duran)*. **Yıldızın tek kaynağı bu.** "
 "**Ve aday 818'in ön-kaydı BURADA SINANDI VE TUTTU: خَبِير mühürsüz bir esmâ tokeni ve göndergesi "
 "İLÂHÎ** (إِنَّهُۥ, mercii صُنْعَ ٱللَّهِ). **Sûrenin 21 mühürsüz tokeninin GEÇERLİ çıkan TEK "
 "tanesi; ayrım 32/32'den 33/34'e düştü.** Ön-kayıt yapısal bir gerekçeye dayanıyordu — 'bayrak "
 "iki esmânın bitişikliğini arıyor, tek başına gelen geçerli bir ismi tanım gereği yakalayamaz' — "
 "ve **düştüğü yer de tam olarak öngörülen yer: son ta'lîl cümlesinde tek başına duran bir isim.**"
 "\n\n**SINIR — ÇIPA DEĞERLENDİRMESİ: sûrenin en güçlü çıpa adayı ve karar verilemedi.** Ayet bir "
 "GÖRÜNÜŞ-DURUM AYRIMI kuruyor (dağları donuk sanırsın, oysa geçerler) ve bir KARŞILAŞTIRMA "
 "veriyor (bulutların geçişi gibi). **Bu, 'adlandırma'nın da 27:60'ın 'nedensel bağımlılık' "
 "katının da üstünde: gözlemcinin algısı ile nesnenin durumu açıkça ayrılıyor.** Ama ölçü yok, "
 "mekanizma yok, hız verilmiyor. **Sıkı ölçütle (mekanizma/ölçü/sınıflandırma şart) DÜŞER; "
 "27:60'ta önerilen gevşek ölçütle GEÇER.** Yani **27:88, iki aday çıpa tanımını birbirinden "
 "ayıran ayet.** Karar P0 #6'ya bırakıldı; 🜁/🜂 yazılmadı. **Not: ayet ★★★'ı bu içerikten değil, "
 "iki hapakstan alıyor.**"),
89: ("İyilikle gelene karşılık. **Ayetin tek fiili var** ve فزع *(dehşet, ürküntü)* iki ayet "
 "önceki dehşetin karşıtını kuruyor. حسن *(güzellik, iyilik)* ile خير *(hayır, daha iyi)* aynı "
 "ayette; xref 28:84'e düşüyor — **aynı karşılık formülü orada da var.** أمن *(güven; iman)* "
 "burada 'güvende olma' anlamında, 27:77'de 'iman' anlamındaydı — **kök sûrede iki anlam "
 "alanında, 529 kümesinin sûre içi ALTINCI vakası.**"),
90: ("Kötülükle gelene karşılık: **27:89 ile ardışık ve birebir karşıt çift** — جَآءَ "
 "بِٱلْحَسَنَةِ / جَآءَ بِٱلسَّيِّئَةِ, aynı fiil, aynı yapı, zıt nesne. Yeni kök كبب *(yüzüstü "
 "kapaklanma)* korpusta iki geçişli. **İki edilgen fiil ve yıldızın tek kaynağı bu** (pas z=1,95). "
 "**Ölçülebilir bir desen: sûrenin son altı yıldızlı ayetinin dördü edilgenlikten yıldız alıyor** "
 "(27:83, 90, 91 ve blok dışında 27:68). Biçim HASR."),
91: ("**Adlı aktör alanının denetimi: مُسْلِم 'kavim' türünde adlı aktör olarak sayılmış — ama bu "
 "bir CİNS İSİM, özel ad değil.** Korpus taraması: **on dört token, hepsi 'kavim' türünde.** "
 "Alanın 105 adlık envanterinde مُسْلِم ve نَصْرانِيّ gibi cins isimler var; **aday 802/833'ün "
 "adsız aktör tarafında bulduğu arızanın ADLI taraftaki karşılığı.** Ve ölçülebilir bir yapı: "
 "**أمر *(emir; iş)* iki kez ve ikisi de edilgen (أُمِرْتُ)** — peygamberin kendi konumu tümüyle "
 "edilgen kuruluyor; **yıldızın tek kaynağı da bu.** بلد *(belde, şehir)* korpusta on dokuz "
 "geçişli."),
92: ("**هدي *(yol gösterme)* sûrede yedinci ve sekizinci geçişini yapıyor ve dört anlam alanının "
 "en sık olanına dönüyor.** Kökün sûre içi bilançosu: yol bulma (27:24) · hediye (27:35, 36) · "
 "tanıma (27:41) · yol gösterme (27:63) · hidâyet (27:77, 92 x2). **Sekiz geçiş, dört anlam "
 "alanı — 529 kümesinin en dallanmış vakası ve dikey satırı sekizinde de aynı.** قُرْءان sûrede "
 "ikinci ve son kez adlı aktör; **sûrenin iki 'kitab' türü aktörü de Kur'ân'ın kendisi** (27:76, "
 "burası). Bab VIII iki kez — aynı kökün iki çekimi."),
93: ("Sûre bir hamd ve bir Rab ile kapanıyor. **قُلِ ٱلْحَمْدُ لِلَّهِ 27:59'da da vardı — sûrede "
 "iki kez ve ikisi de bir bölütü açıp kapatıyor.** Eksenin iki işareti son ayette buluşuyor "
 "(allah z=1,29 · rab z=1,62) ve **yıldızın tek kaynağı Rab.** Fâsıla تَعْمَلُونَ — blokta üçüncü, "
 "sûrenin son kelimesi. Dış düğüm üç. **Sûre 27 tamamlandı: 93 ayet, 1151 kelime, ortalama n=12,38.**"),
}

ATLAMA = {
 "_mercek_27_88": ("27:88 ★★★ — 🜁 ve 🜂 YAZILMADI, KARAR VERİLEMEDİ (çıpa tanımı yazılmadan "
  "kapatılamaz). Kaynak: hapaks z=6,98 (iki hapaks: تقن *(sağlam ve kusursuz yapma (itkān))*, جمد *(donuk, hareketsiz duran)*) — **içerikle ilgisi yok.** Ayet bir "
  "GÖRÜNÜŞ-DURUM AYRIMI (dağları donuk sanırsın, oysa geçerler) ve bir KARŞILAŞTIRMA (bulutların "
  "geçişi gibi) kuruyor. **Bu kat, 'adlandırma'nın ve 27:60'ın 'nedensel bağımlılık + yeti "
  "sınırı' katının üstünde: gözlemcinin algısı ile nesnenin durumu açıkça ayrılıyor.** Ama ölçü, "
  "mekanizma ve hız yok. **SIKI ölçütle düşer, 27:60'ta önerilen GEVŞEK ölçütle geçer — yani "
  "27:88 iki aday çıpa tanımını birbirinden AYIRAN ayettir.** Karar P0 #6'ya bırakıldı. Sûre "
  "27'nin en güçlü çıpa adayı budur ve ★★★'ını içerikten değil iki hapakstan alıyor."),
 "_blok_notu_27_81_93": ("BLOK BİLANÇOSU (on üç ayet): ★★★ 1 (27:88, hapaks) · ★★ 0 · ★ 4 "
  "(27:83 pas, 27:90 pas, 27:91 pas, 27:93 Rab) · yıldızsız 8. Kaynaklar: hapaks 1 · pas 3 · Rab "
  "1 — **içerikten sıfır.** İltifât 0/13. Esmâ token 1 (27:88 خَبِير, **GEÇERLİ — sûrenin tek "
  "geçerli mühürsüz tokeni**). Allah lafzı 3 (27:87, 88, 93) · Rab 2 (27:91, 93). Adlı aktör 2 "
  "(مُسْلِم ARTEFAKT, قُرْءان) · adsız aktör 0. Yeni kök 5 (فوج *(bölük, grup (fevc))*, دخر *(boyun eğme, küçülerek gelme)*, جمد *(donuk, hareketsiz duran)*, تقن *(sağlam ve kusursuz yapma (itkān))*, كبب *(yüzüstü kapaklanma)*). **Hapaks 2 "
  "— sûrenin tek çift-hapaks ayeti.** Kafiye kırılması 0."),
 "_sure_27_kapanis": ("SÛRE 27 (NEML) KAPANIŞ — HAM SAYIMLAR. 93 ayet · ortalama n=12,38 · fâsıla "
  "84 ن + 9 م · kafiye kırılması 0. YILDIZ: ★★★ 9 · ★★ 9 · ★ 10 · yıldızsız 65 (%69,9). YILDIZ "
  "KAYNAKLARI (28 yıldızlı ayet): **edilgenlik 11 · hapaks 5 · lafız 5 · Rab 5 · uzunluk 3 — "
  "İÇERİK 0.** EKSEN: lafız 27 token / 25 ayet · Rab 12 token / 10 ayet → A/R = 2,25. ESMÂ: 33 "
  "token; 12'si mühür tokeni (6 mühür, 6 farklı çift, **6/6 GEÇERLİ**), 21'i mühürsüz ve "
  "**20/21 ARTEFAKT** (tek geçerli: 27:88 خَبِير). İLTİFÂT 3 (27:6 anlatı içi · 27:31 alıntı "
  "sınırı · 27:69 emir zinciri — üçü üç ayrı katmanda). NAKARAT ALANI: **0** — oysa üç ayet-içi "
  "nakarat var. ESİT: 3 ayet dolu (27:3, 58, 71); **en az iki yanlış negatif** (27:80↔30:52, "
  "27:81↔30:53). HAPAKS: 5 ayet, 6 kök (بسم *(gülümseme (tebessüm))*, هدهد *(hüdhüd (ibibik))*, خبأ *(saklı olan, gizlenmiş şey)*, عفر *(ifrît (güçlü cin))*, تقن *(sağlam ve kusursuz yapma (itkān))*+جمد *(donuk, hareketsiz duran)*). AKTÖR: adlı 25 token "
  "(en az biri artefakt), **adsız 1 token** (27:23, doğru). EDİLGEN: 16 ayet. 529 KÜMESİ: "
  "**altı vaka** (سمو *(ad; gök)*, هدي *(yol gösterme)* [dört anlam alanı], طير *(kuş; uçan)*, كشف *(giderme, açma)*, خلف *(ayrılığa düşme; ardından gelme)*, أمن *(güven; iman)*). ANLATI BÖLÜTLERİ: Mûsâ 8 · "
  "Dâvûd-Süleymân 30 · Semûd 9 · Lût 5 · doğa 5 ayet."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(81, 94):
    OM['27']["27:%d" % n] = {"ar": AR[(27, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["27:%d" % n]}
OM['27']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1, 9-26 ve **27 TAM**. Devam: sûre 2'den (21. ayet) ya da yeni sûre.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 2042
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 27 →', len([k for k in OM['27'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(81, 94):
    MK['27']["27:%d" % n] = M[n]
MK['27_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 27 →', len(MK['27']))
