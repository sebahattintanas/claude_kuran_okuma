# -*- coding: utf-8 -*-
"""blok_26_91_100.py — sûre 26 yedinci blok (26:91-100). Mahşer sahnesi ve QASEM sınama vakası."""
import json
DIK = json.load(open('blok_dikey_26_91_100.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
91: "Cehennem, azgınlara açıkça gösterildi.",
92: "Onlara dendi: Taptıklarınız nerede?",
93: "Allah'ın yanı sıra. Size yardım ediyorlar mı, ya da kendilerine yardım edebiliyorlar mı?",
94: "Onlar ve azgınlar oraya tepetaklak atıldı.",
95: "İblis'in orduları da, hepsi.",
96: "Orada çekişerek dediler:",
97: "Allah'a andolsun, biz apaçık bir sapkınlık içindeymişiz.",
98: "Sizi âlemlerin Rabbine denk tutuyorduk.",
99: "Bizi suçlulardan başkası saptırmadı.",
100: "Artık bizim ne şefaatçilerimiz var.",
}

O = {
91: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — ٱلْجَحِيم *(cehennem, alevli ateş)* "
 "aktör tablosuna GİRMİYOR, oysa 25:11 ve 25:65'te جَهَنَّم girmişti; **iki ayrı kök, aynı gönderge, "
 "farklı hüküm** (aday 462/666 kümesi) · edim haber, kip işareti yok · **şahıs 3FS x1 — ayette "
 "başka şahıs yok**, iltifât 0 · n=3 mora=24 harf=18 (n z=-1,00), fâsıla لِلْغَاوِينَ *(azgınlar)* → "
 "ن, N sınıfı; i'râb NOM 1 · GEN 1; bab II x1; zaman PERF 1; **edilgen 1 — بُرِّزَتِ *(açıkça "
 "gösterildi)*; ayetin TEK fiili ve o da edilgen, oran 1,00**, pas z=5,38: **yıldızın TEK kaynağı**; "
 "dış düğüm 0 · **yıldız ★★★** · kökler برز *(ortaya çıkma, belirme)* · جحم *(alevli ateş, cahîm)* · "
 "غوي *(azma, azdırma)* · bağ: **26:90 ile bitişik çift ve TERS KUTUP** — orada أُزْلِفَتِ "
 "ٱلْجَنَّةُ لِلْمُتَّقِينَ *(cennet sakınanlara yaklaştırıldı)*, burada بُرِّزَتِ ٱلْجَحِيمُ "
 "لِلْغَاوِينَ *(cehennem azgınlara gösterildi)*; **ikisi de üç kelime, ikisi de tek fiil ve edilgen, "
 "ikisi de pas z=5,38, ikisi de ★★★** (elle, L1, aday 667)"),
92: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · şahıs 2MP x4 · "
 "3MS x1 · 3MP x1, iltifât 0 · n=6 mora=27 harf=22 (n z=-0,68), fâsıla تَعْبُدُونَ *(tapıyorsunuz)* → "
 "ن, N sınıfı — **26:70 ve 26:75'in fâsılasıyla AYNI KELİME, sûrede üçüncü kez**; **i'râb YOK**; "
 "bab I x3; zaman PERF x2 · IMPF x1; **edilgen 1 — قِيلَ *(dendi)*; üç fiilden biri edilgen, oran "
 "0,33**, pas z=1,57: **yıldızın TEK kaynağı**; dış düğüm 0 · **yıldız ★** · kökler قول *(söz "
 "söyleme)* · كون *(olmak; mekân, yer)* · عبد *(kul, kulluk)* · bağ: **26:70 ve 26:75 ile "
 "تَعْبُدُونَ üçlüsü** — orada İbrâhîm kavmine soruyordu (dünyada), burada mahşerde soruluyor; "
 "**aynı soru, iki sahne** (elle, L1, aday 668)"),
93: ("eksen: **ALLAH LAFZI 3. sırada — sûrenin İKİNCİ lafzı** (allah z=2,33: yıldızın TEK kaynağı) · "
 "Rab yok · esmâ yok · aktör yok · edim soru, kip INTG 1 · şahıs 3MP x4 · 2MP x1, iltifât 0 · n=7 "
 "mora=34 harf=28 (n z=-0,58), fâsıla يَنتَصِرُونَ *(kendilerine yardım ederler)* → ن, N sınıfı; "
 "i'râb GEN 2; bab I x1 · VIII x1; zaman IMPF x2; **kök ikilemesi نصر *(yardım)* x2 — bab I ve "
 "bab VIII: هَلْ يَنصُرُونَكُمْ أَوْ يَنتَصِرُونَ *(size yardım ediyorlar mı, ya da kendilerine "
 "yardım edebiliyorlar mı)*; aynı kök, dışa ve içe dönük iki çatı**; dış düğüm 0 · **yıldız ★★** · "
 "kökler دون *(beriki, başkası)* · أله *(ilâh; lafza-i celâl)* · نصر *(yardım)* · bağ: **25:3, "
 "25:55, 26:73 ile aynı sorgu dizisi** — orada نفع *(fayda)* / ضرر *(zarar)* çiftiyle, burada نصر "
 "*(yardım)* kökünün iki çatısıyla; **aynı sorgu, farklı ölçüt** (elle, L1, aday 669)"),
94: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3MP x3 · 3FS x1, iltifât 0 · n=4 mora=25 harf=22 (n z=-0,89), fâsıla ٱلْغَاوُۥنَ *(azgınlar)* → "
 "ن, N sınıfı — **26:91'in fâsılasıyla aynı kök**; i'râb NOM 1; bab I x1; zaman PERF 1; **edilgen "
 "1 — كُبْكِبُوا۟ *(tepetaklak atıldılar)*; ayetin TEK fiili ve o da edilgen, oran 1,00**, "
 "pas z=5,38; **HAPAKS: كبكب *(tepetaklak atma)* — korpusta TEK geçiş** (hapaks z=3,38); dış düğüm "
 "0 · **yıldız ★★★ — İKİ KAYNAKLI: hapaks VE pas**; okumada üçüncü iki kaynaklı ayet (25:73, 26:50, "
 "burada) · kökler كبكب *(tepetaklak atma)* · غوي *(azma, azdırma)* · bağ: **26:91 ile غوي *(azma, "
 "azdırma)* ikinci geçişi** — orada لِلْغَاوِينَ *(azgınlara)* gösterilen taraf, burada "
 "ٱلْغَاوُۥنَ *(azgınlar)* atılan taraf; **üç ayet arayla mecrurdan merfûya** (elle, L1, aday 670)"),
95: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı إِبْلِيس *(İblîs)* 2. sırada, rol "
 "MEF'ÛL** · edim haber, kip işareti yok · **şahıs eki YOK, fiil YOK** · n=3 mora=21 harf=16 "
 "(n z=-1,00), fâsıla أَجْمَعُونَ *(hepsi)* → ن, N sınıfı — **26:49 ve 26:65'in fâsılasıyla aynı "
 "kök, farklı i'râb** (orada ACC أَجْمَعِينَ, burada NOM أَجْمَعُونَ); **i'râb NOM 2 · ACC 1**; "
 "dış düğüm 0 · yıldız ★ yok · kökler جند *(ordu, asker)* · جمع *(toplama)* · bağ: **26:38, 39, 49, "
 "56, 61, 65 ile جمع *(toplama)* YEDİNCİ geçişi ve yedinci biçimi** — burada NOM pekiştirme; "
 "**dikey ölçüm جمع için ▸önce غوي *(azma, azdırma)* x12,6 veriyor, yani 26:94'ün kökü** "
 "(elle, L1, aday 671)"),
96: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3MP x5 · 3FS x1, iltifât 0 · n=4 mora=25 harf=20 (n z=-0,89), fâsıla يَخْتَصِمُونَ *(çekişirler)* → "
 "ن, N sınıfı; **i'râb YOK**; bab I x1 · VIII x1; zaman PERF 1 · IMPF 1; dış düğüm 0 · yıldız ★ yok · "
 "kökler قول *(söz söyleme)* · خصم *(husumet, çekişme)* · bağ: **خصم *(husumet, çekişme)* korpusta "
 "18 geçişli ve dikey ölçümü ▸önce hiçbir komşu vermiyor, ▸sonra yalnız beyan x7,2 — kökün korpusta "
 "dar ve tek yönlü bir yatağı var** (elle, L1)"),
97: ("eksen: **ALLAH LAFZI 1. sırada — sûrenin ÜÇÜNCÜ lafzı ve İLK KEZ YEMİN EDATIYLA: تَٱللَّهِ** "
 "(allah z=2,80: yıldızın TEK kaynağı) · Rab yok · **esmâ مُبِين *(apaçık)* 6. sırada = fâsıla, "
 "MÜHÜRSÜZ — ÖLÇÜM ARTEFAKTI**: gönderge ضَلَٰل *(sapkınlık)*; sûrenin beşinci مُبِين artefaktı · "
 "aktör yok · edim haber, kip CERT 1 · EMPH 1 · **şahıs 1P x2**, **iltifât 1 — yön 3>1; sûrenin "
 "beşinci iltifâtı** · n=6 mora=30 harf=21 (n z=-0,68), fâsıla مُّبِينٍ *(apaçık)* → ن, N sınıfı; "
 "**i'râb GEN 3**; bab I x1; zaman PERF 1; **biçim: QASEM YOK — ama ayet تَٱللَّهِ ile açılıyor; "
 "ADAY 443'ÜN CANLI SINAMA VAKASI**; dış düğüm 1 · **yıldız ★★** · kökler أله *(ilâh; lafza-i "
 "celâl)* · كون *(olmak; mekân, yer)* · ضلل *(sapma, saptırma)* · بين *(arası; açıklama)* · bağ: "
 "xref كان *(oldu)* + ضلال *(sapkınlık)* + مبين *(apaçık)* → **43:40**; **sûre makro profilinde "
 "'QASEM sıfır' yazılmıştı — YANLIŞ; ölçüm etiketi eksik** (elle, L1, aday 672)"),
98: ("eksen: **lafız YOK · رَبّ *(Rab)* 3. sırada — on dokuzuncu Rab**, **rab z=5,01: yıldızın TEK "
 "kaynağı** (n=4, oran 0,25) · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs 1P x1 · "
 "2MP x1, iltifât 0 · n=4 mora=25 harf=18 (n z=-0,89), fâsıla ٱلْعَٰلَمِينَ *(âlemler)* → ن, N "
 "sınıfı; **i'râb GEN 2**; bab II x1; zaman IMPF 1; dış düğüm 0 · **yıldız ★★★** · kökler سوي "
 "*(düzenleme, denk kılma)* · ربب *(rab, terbiye etme)* · علم *(bilme; âlem)* · bağ: **25:59 ile "
 "سوي *(düzenleme, denk kılma)* karşılaşması** — orada ٱسْتَوَىٰ عَلَى ٱلْعَرْشِ *(arş üzerine "
 "istivâ etti)* bab VIII ve 'yerleşme' anlamında, burada نُسَوِّيكُم *(sizi denk tutuyorduk)* bab II "
 "ve 'denk kılma' anlamında; **aynı kök, bab sınırında anlam ayrımı** (aday 569/584 sınıfı); "
 "**رَبَّ ٱلْعَٰلَمِينَ terkibinin sûrede ALTINCI geçişi** (elle, L1, aday 673)"),
99: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · RES 1 · şahıs "
 "3MS x1 · 1P x1, iltifât 0 · n=4 mora=31 harf=19 (n z=-0,89), fâsıla ٱلْمُجْرِمُونَ *(suçlular)* → "
 "ن, N sınıfı; **i'râb NOM 1**; bab IV x1; zaman PERF 1; **biçim HASR**; dış düğüm 0 · yıldız ★ yok · "
 "kökler ضلل *(sapma, saptırma)* · جرم *(suç işleme)* · bağ: **26:97 ile ضلل *(sapma, saptırma)* "
 "bitişik ikinci geçişi** — orada ضَلَٰلٍ مُّبِينٍ *(apaçık sapkınlık)* bir HÂL, burada "
 "أَضَلَّنَا *(bizi saptırdı)* bir FİİL ve FÂİLİ VAR; **iki ayet arayla hâlden faile** "
 "(elle, L1, aday 674)"),
100: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · şahıs 1P x1, "
 "iltifât 0 · n=4 mora=19 harf=13 — **blokta en kısa ayet** (n z=-0,89), fâsıla شَٰفِعِينَ "
 "*(şefaatçiler)* → ن, N sınıfı; **i'râb GEN 1; fiil YOK**; dış düğüm 0 · yıldız ★ yok · **TEK KÖK: "
 "شفع *(şefaat, çift kılma)*** · bağ: **25:3'ün نفع *(fayda)* / ضرر *(zarar)* dizisiyle dolaylı "
 "bağ** — dikey ölçüm شفع için ▸önce نفع *(fayda)* x32,3 veriyor, yani 'şefaat' ve 'fayda' korpusta "
 "bitişik; 26:93'te yardım, burada şefaat: **mahşerde işe yaramayan üçüncü şey** (elle, L1, aday 675)"),
}

M = {
91: ("Üç kelime, tek fiil ve o da edilgen — oran 1,00, pas z=5,38, yıldızın tek kaynağı. **26:90 ile "
 "bitişik çift ve ters kutup**: orada أُزْلِفَتِ ٱلْجَنَّةُ لِلْمُتَّقِينَ *(cennet sakınanlara "
 "yaklaştırıldı)*, burada بُرِّزَتِ ٱلْجَحِيمُ لِلْغَاوِينَ *(cehennem azgınlara gösterildi)*. "
 "**İkisi de üç kelime, ikisi de tek fiil ve edilgen, ikisi de pas z=5,38, ikisi de ★★★** — "
 "okumada görülen en simetrik ayet çifti. برز *(ortaya çıkma, belirme)* korpusta dokuz geçişli ve "
 "dikey ölçümü ▸sonra hiçbir komşu vermiyor. Ve جحم *(alevli ateş, cahîm)* aktör tablosuna "
 "GİRMİYOR, oysa 25:11 ve 25:65'te جَهَنَّم girmişti — iki ayrı kök, aynı gönderge, farklı hüküm."),
92: ("Soru mahşerde ve edilgen bir fiille açılıyor: وَقِيلَ لَهُمْ أَيْنَ مَا كُنتُمْ تَعْبُدُونَ "
 "*(onlara dendi: taptıklarınız nerede)*. Ölçülebilir bir sahne aktarımı: aynı soru 26:70'te "
 "İbrâhîm'in kavmine (مَا تَعْبُدُونَ *(neye tapıyorsunuz)*) ve 26:75'te yine ona (مَّا كُنتُمْ "
 "تَعْبُدُونَ *(neye taptığınızı)*) sorulmuştu — **dünyada üç kez, burada mahşerde dördüncü kez ve "
 "soranı belirsiz** (edilgen قِيلَ). Aynı fâsıla üç ayette. Ve ayet yine i'râb etiketi almıyor; "
 "sûrede i'râbsız ayetler kümesi büyüyor (26:72, 73, 75, 92, 96)."),
93: ("Sorgu bir yardım sınavına dönüşüyor ve kök ikilemesiyle: هَلْ يَنصُرُونَكُمْ أَوْ "
 "يَنتَصِرُونَ *(size yardım ediyorlar mı, ya da kendilerine yardım edebiliyorlar mı)* — نصر "
 "*(yardım)* bab I ve bab VIII, yani **dışa dönük ve içe dönük iki çatı**. Ölçülebilir bir dizi "
 "karşılaştırması: 25:3, 25:55 ve 26:73'te aynı sorgu نفع *(fayda)* / ضرر *(zarar)* çiftiyle "
 "kuruluyordu; burada ölçüt değişiyor — **aynı sorgu, farklı ölçüt**. Ve sûrenin ikinci Allah lafzı "
 "burada; yıldızın tek kaynağı bu (allah z=2,33). دون *(beriki, başkası)* dikey ölçümü ▸sonra "
 "şefaat x9,3 · zarar x7,6 · نفع *(fayda)* x6,7 veriyor — **bu bölütün üç ölçütü de korpusta zaten "
 "bu köke bağlı.**"),
94: ("Dört kelime ve **yıldız iki kaynaktan**: hapaks z=3,38 (كبكب *(tepetaklak atma)*, korpusta tek "
 "geçiş) ve pas z=5,38 (ayetin tek fiili edilgen, oran 1,00). Okumada üçüncü iki kaynaklı ayet "
 "(25:73 ve 26:50'den sonra) — ve **ilk kez iki kaynağın ikisi de en yüksek değerlerinde**. "
 "Ölçülebilir bir konum değişimi: غوي *(azma, azdırma)* 26:91'de لِلْغَاوِينَ *(azgınlara)* mecrur "
 "ve gösterilen taraftı, burada ٱلْغَاوُۥنَ *(azgınlar)* merfû ve atılan taraf — üç ayet arayla "
 "mecrurdan merfûya. Kök korpusta 22 geçişli ve dikey ölçümü ▸önce تبع *(uyma, ardından gitme)* "
 "x8,2 veriyor."),
95: ("Üç kelime, fiil yok, ve sûrenin ilk İblîs geçişi — rol mef'ûl. Ölçülebilir bir biçim: جمع "
 "*(toplama)* sûrede **yedinci** kez ve yedinci biçimiyle — 26:38 edilgen fiil, 26:39 etken ism-i "
 "fâil, 26:49 ACC pekiştirme, 26:56 sıfat, 26:61 tesniye isim, 26:65 ACC pekiştirme, burada **NOM "
 "pekiştirme** (أَجْمَعُونَ). Aynı kelime 26:49 ve 26:65'te mansûbdu, burada merfû; i'râb değişimi "
 "fâsıla konumunu değiştirmiyor. Ve dikey ölçüm جمع için ▸önce غوي *(azma, azdırma)* x12,6 veriyor "
 "— **bir önceki ayetin kökü**, yani çift korpusta bağlı."),
96: ("Dört kelime ve yine i'râb etiketi yok. خصم *(husumet, çekişme)* korpusta 18 geçişli ve dikey "
 "ölçümü ▸önce **hiçbir komşu vermiyor**, ▸sonra yalnız beyan x7,2 — kökün korpusta dar ve tek "
 "yönlü bir yatağı var. Ölçülebilir bir zaman yapısı: قَالُوا۟ *(dediler)* mâzi ve وَهُمْ فِيهَا "
 "يَخْتَصِمُونَ *(orada çekişerek)* muzâri hâl cümlesi — tamamlanmış bir söz ve süregelen bir "
 "çekişme. Ayet bir sonraki ayetin sözünü açıyor; kendi başına yüklem taşımıyor."),
97: ("**Sûrenin üçüncü Allah lafzı ve ilk kez yemin edatıyla: تَٱللَّهِ.** Ve burada bir ölçüm "
 "eksiği görünüyor: ayetin `fig` alanında QASEM YOK, sûre makro profilinde de 'QASEM sıfır' "
 "yazılmıştı. **Bu, aday 443'ün (QASEM تَٱللَّهِ etiketlenmiyor) canlı sınama vakası** — makro "
 "sayım tutarsızlığının ikinci vakası (birincisi 26:74'te IDRAB, aday 650). Ölçülebilir bir "
 "itiraf yapısı: CERT + EMPH birlikte ve 1P x2; sûrenin beşinci iltifâtı da burada (3>1). Ve "
 "fâsıladaki مُبِين esmâ sayılmış, oysa gönderge ضَلَٰل *(sapkınlık)* — sûrenin beşinci مُبِين "
 "artefaktı."),
98: ("Dört kelime ve rab z=5,01 — n=4, tek Rab, oran 0,25; 26:47 ile aynı değer ve aynı sebep. "
 "Ölçülebilir bir kök karşılaşması: سوي *(düzenleme, denk kılma)* 25:59'da ٱسْتَوَىٰ عَلَى "
 "ٱلْعَرْشِ *(arş üzerine istivâ etti)* olarak bab VIII ve 'yerleşme' anlamındaydı; burada "
 "نُسَوِّيكُم *(sizi denk tutuyorduk)* bab II ve 'denk kılma'. **Anlam ayrımı tam bab sınırında** — "
 "aday 569/584'ün bab girdisi önerisine dördüncü destek. Ve رَبَّ ٱلْعَٰلَمِينَ terkibi sûrede "
 "altıncı kez; bu kez bir İTİRAF içinde: sapkınlığın tanımı 'âlemlerin Rabbine denk tutmak'."),
99: ("Dört kelime ve HASR: وَمَآ أَضَلَّنَآ إِلَّا ٱلْمُجْرِمُونَ *(bizi suçlulardan başkası "
 "saptırmadı)*. Ölçülebilir bir geçiş: ضلل *(sapma, saptırma)* iki ayet arayla ikinci kez — "
 "26:97'de ضَلَٰلٍ مُّبِينٍ *(apaçık sapkınlık)* bir HÂL, burada أَضَلَّنَا *(bizi saptırdı)* bir "
 "FİİL ve **fâili var**. Hâlden faile, yani sorumluluk aktarımı. Bu, 25:17'nin çatı sorusuyla "
 "(أَضْلَلْتُمْ *(siz mi saptırdınız)* / ضَلُّوا۟ *(kendileri mi saptı)*) aynı alanda ve 25:29'un "
 "cevabıyla (أَضَلَّنِى *(beni saptırdı)*, fâil şeytan) aynı yapıda — **burada fâil şeytan değil "
 "ٱلْمُجْرِمُونَ *(suçlular)*, yani insanlar.**"),
100: ("Dört kelime, fiil yok, tek kök — blokta en kısa ayet. شفع *(şefaat, çift kılma)* korpusta 31 "
 "geçişli ve dikey ölçümü ▸önce نفع *(fayda)* x32,3 · suç x13,9 veriyor: **'şefaat' korpusta hem "
 "'fayda' hem 'suç' ile bitişik ve bu bölütte ikisi de var** (26:93 yardım sorgusu, 26:99 "
 "suçlular). Yani ayetin iki komşusu kökün korpus komşuluğuyla örtüşüyor. Ölçülebilir bir dizi: "
 "mahşerde işe yaramayan üç şey sayılıyor — tapılanların yardımı (26:93), mal ve oğullar (26:88), "
 "şefaatçiler (burada)."),
}

ATLAMA = {
 "_mercek_26_91": ("26:91 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. وَبُرِّزَتِ ٱلْجَحِيمُ لِلْغَاوِينَ. "
  "Tek kaynak pas z=5,38 (n=3, ayetin tek fiili edilgen, oran 1,00). İçerik bir âhiret sahnesi; "
  "26:90 ile birebir simetrik (ikisi de üç kelime, tek edilgen fiil, aynı z, ikisi de ★★★)."),
 "_mercek_26_94": ("26:94 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. فَكُبْكِبُوا۟ فِيهَا هُمْ "
  "وَٱلْغَاوُۥنَ. **İKİ KAYNAKLI**: hapaks z=3,38 (كبكب *(tepetaklak atma)*, korpusta tek geçiş) VE "
  "pas z=5,38. Okumada üçüncü iki kaynaklı ayet (25:73, 26:50) ve İLK KEZ iki kaynağın ikisi de en "
  "yüksek değerlerinde. İçerik bir âhiret sahnesi."),
 "_mercek_26_98": ("26:98 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. إِذْ نُسَوِّيكُم بِرَبِّ "
  "ٱلْعَٰلَمِينَ. Tek kaynak rab z=5,01 (n=4, oran 0,25). İçerik bir itiraf."),
 "_blok_notu_26_91_100": ("BLOK BİLANÇOSU: ★★★ 3 (26:91, 94, 98) · ★★ 2 (26:93, 97) · ★ 1 (26:92) · "
  "4 ayet yıldızsız — **okumada görülen EN YILDIZLI on ayetlik blok** (altı yıldızlı ayet). "
  "Kaynaklar: pas x3 · allah x2 · rab x1 · hapaks x1 (26:94'te pas ile birlikte) — HİÇBİRİ "
  "İÇERİKTEN, hiçbirinde çıpa yok. **UYARI (aday 602/624): altı yıldızlı ayetin altısı da n<=7 ve "
  "üçü n<=4; blok ortalaması n=4,4 — sûre ortalamasının (5,81) altında.** Bu blok, kısa ayet "
  "yanlılığının doğrudan sonucu gibi görünüyor. SÛRE 26'NIN OKUNAN 100 AYETİNDE ★★★ 20; çıpası "
  "olan tek ★★★ hâlâ 26:63."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(91, 101):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 100/227.** Devam: 26:101'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-100 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1822
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(91, 101):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
