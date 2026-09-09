# -*- coding: utf-8 -*-
"""blok_26_111_120.py — sûre 26 dokuzuncu blok (26:111-120). Nûh kıssasının gövdesi."""
import json
DIK = json.load(open('blok_dikey_26_111_120.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
111: "Dediler: Sana ayaktakımı uyarken biz sana mı inanacağız?",
112: "Dedi: Onların ne yaptığına dair benim bilgim yok.",
113: "Onların hesabı ancak Rabbime aittir — bir farkında olsanız.",
114: "Ben müminleri kovacak değilim.",
115: "Ben ancak apaçık bir uyarıcıyım.",
116: "Dediler: Ey Nûh, vazgeçmezsen mutlaka taşlananlardan olursun.",
117: "Dedi: Rabbim, kavmim beni yalanladı.",
118: "Benimle onların arasını bir açışla aç; beni ve benimle beraber olan müminleri kurtar.",
119: "Onu ve beraberindekileri dolu geminin içinde kurtardık.",
120: "Sonra geride kalanları boğduk.",
}

O = {
111: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · şahıs 3MP x2 · "
 "1P x1 · 2MS x2 · 3MS x1, iltifât 0 · n=5 mora=33 harf=28 (n z=-0,79), fâsıla ٱلْأَرْذَلُونَ "
 "*(ayaktakımı, aşağı görülenler)* → ن, N sınıfı; **i'râb NOM 1**; bab I x1 · IV x1 · VIII x1; "
 "zaman PERF x2 · IMPF x1; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · أمن *(güven; "
 "iman)* · تبع *(uyma, ardından gitme)* · رذل *(rezil, aşağılık)* · bağ: **رذل *(rezil, aşağılık)* "
 "korpusta DÖRT geçişli ve dikey ölçümü ▸önce hiçbir komşu, ▸sonra yalnız ilim x12,9 veriyor — "
 "kökün korpusta dar ve tek yönlü yatağı var**; **تبع *(uyma, ardından gitme)* sûrede dördüncü "
 "geçiş** (26:40 niyet, 26:52 uyarı, 26:60 gerçekleşme, burada BİR KUSUR olarak sunuluyor) "
 "(elle, L1, aday 686)"),
112: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3MS x1 · 1S x1 · 3MP x4, iltifât 0 · n=6 mora=31 harf=25 (n z=-0,68), fâsıla يَعْمَلُونَ "
 "*(yapıyorlar)* → ن, N sınıfı; **i'râb NOM 1**; bab I x3; zaman PERF x2 · IMPF x1; **dış düğüm 1** · "
 "yıldız ★ yok · kökler قول *(söz söyleme)* · علم *(bilme; ilim)* · كون *(olmak; mekân, yer)* · "
 "عمل *(iş, amel)* · bağ: xref علم *(ilim)* + كان *(oldu)* + عمل *(amel)* → **27:84**; **26:74 ile "
 "عمل / فعل karşılaştırması** — orada kavim atalarının يَفْعَلُونَ *(yaptıklarını)* gerekçe "
 "gösteriyordu, burada elçi kavmin يَعْمَلُونَ *(yaptıkları)* hakkında bilgi sahibi OLMADIĞINI "
 "söylüyor; **iki ayrı kök, aynı 'yapma' alanı** (aday 613/627/652 deseni) (elle, L1, aday 687)"),
113: ("eksen: **lafız YOK · رَبّ *(Rab)* 5. sırada — yirmi ikinci Rab** (rab z=2,72: yıldızın TEK "
 "kaynağı) · esmâ yok · aktör yok · edim şart, kip NEG 1 · RES 1 · COND 1 · şahıs 3MP x1 · 1S x1 · "
 "2MP x2, iltifât 0 · n=7 mora=33 harf=26 (n z=-0,58), fâsıla تَشْعُرُونَ *(farkına varıyorsunuz)* → "
 "ن, N sınıfı; i'râb NOM 1 · GEN 1; bab I x1; zaman IMPF x1; **biçim HASR**; simetri [3,1,4,1]; "
 "dış düğüm 0 · **yıldız ★★** · kökler حسب *(hesap, sayma)* · ربب *(rab, terbiye etme)* · شعر "
 "*(şair; farkında olma)* · bağ: **شعر *(şair; farkında olma)* — SÛRENİN ADINI VEREN KÖK, ve İLK "
 "GEÇİŞİ BURADA 'farkında olma' anlamında**; kök korpusta 40 geçişli ve sûrenin adı (ٱلشُّعَرَآء "
 "*(şairler)*) 26:224'te gelecek; **aynı kök, iki anlam, iki uç** (aday 529 sınıfı) (elle, L1, "
 "aday 688)"),
114: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُؤْمِن *(mümin)* 4. sırada = fâsıla, MÜHÜRSÜZ — "
 "ARTEFAKT, sûrenin yedinci مُؤْمِن tokeni** (aday 601) · aktör yok · edim haber, kip NEG 1 · "
 "**şahıs 1S x1 — ayette başka şahıs yok**, iltifât 0 · n=4 mora=25 harf=20 (n z=-0,89), fâsıla "
 "ٱلْمُؤْمِنِينَ → ن, N sınıfı; **i'râb GEN 2; fiil YOK**; dış düğüm 0 · yıldız ★ yok · kökler "
 "طرد *(kovma, uzaklaştırma)* · أمن *(güven; iman)* · bağ: **طرد *(kovma, uzaklaştırma)* korpusta "
 "BEŞ geçişli ve dikey ölçümü İKİ LİSTEDE DE HİÇBİR KOMŞU vermiyor** — 26:102'nin كرر *(dönüş, "
 "kere (kerre))* kökünden sonra blokta ikinci 'boş komşuluk' vakası (elle, L1, aday 689)"),
115: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُبِين *(apaçık)* 5. sırada = fâsıla, MÜHÜRSÜZ — "
 "ARTEFAKT, sûrenin altıncı مُبِين tokeni**: gönderge نَذِير *(uyarıcı)*, yani ELÇİ · aktör yok · "
 "edim haber, kip NEG 1 · RES 1 · **şahıs 1S x1 — ayette başka şahıs yok**, iltifât 0 · n=5 mora=24 "
 "harf=19 (n z=-0,79), fâsıla مُّبِينٌ → ن, N sınıfı; **i'râb NOM 2; fiil YOK**; **biçim HASR**; "
 "dış düğüm 0 · yıldız ★ yok · kökler نذر *(uyarma; adak)* · بين *(arası; açıklama)* · bağ: **25:56 "
 "ve 26:107 ile elçi tanımı üçlüsü** — 25:56 مُبَشِّرا وَنَذِيرا *(müjdeci ve uyarıcı)*, 26:107 "
 "رَسُولٌ أَمِينٌ *(güvenilir elçi)*, burada نَذِيرٌ مُّبِينٌ *(apaçık uyarıcı)*; **üçünde de HASR "
 "ya da sınırlama, üçünde de fiil yok** (elle, L1, aday 690)"),
116: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı نُوح *(Nûh)* 5. sırada, rol FAİL + "
 "MUHATAP — okumada bir aktörün İKİ ROL birden aldığı ilk kayıt** · edim nida + şart, kip EMPH 3 · "
 "COND 1 · NEG 1 · **VOC 1 — sûrenin ilk nidası** · şahıs 3MP x2 · 2MS x2, **iltifât 1 — yön 1>23; "
 "sûrenin yedinci iltifâtı** · n=8 mora=45 harf=36 (n z=-0,47), fâsıla ٱلْمَرْجُومِينَ "
 "*(taşlananlar)* → ن, N sınıfı; i'râb NOM 1 · GEN 1; bab I x2 · VIII x1; zaman PERF x1 · IMPF x2; "
 "dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · نهي *(akıl; nehiy)* · كون *(olmak; "
 "mekân, yer)* · رجم *(taşlama, kovma)* · bağ: **26:29 ile tehdit karşılaştırması** — orada Firavun "
 "لَأَجْعَلَنَّكَ مِنَ ٱلْمَسْجُونِينَ *(seni zindana atılanlardan yaparım)* demişti, burada kavim "
 "لَتَكُونَنَّ مِنَ ٱلْمَرْجُومِينَ *(taşlananlardan olursun)*; **aynı كَانَ/جَعَلَ + مِنَ + "
 "ism-i mef'ûl çoğulu kalıbı, iki tehdit** (elle, L1, aday 691)"),
117: ("eksen: **lafız YOK · رَبّ *(Rab)* 2. sırada — yirmi üçüncü Rab**, **rab z=3,94: yıldızın TEK "
 "kaynağı** (n=5, oran 0,20) · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs 3MS x1 · "
 "1S x3 · 3MP x2, iltifât 0 · n=5 mora=23 harf=16 (n z=-0,79), fâsıla كَذَّبُونِ *(beni "
 "yalanladılar)* → ن, N sınıfı — **ـُونِ eki; 26:12 ve 26:14 ile aynı ek**; i'râb NOM 2 · ACC 1; "
 "bab I x1 · II x1; zaman PERF x2; dış düğüm 0 · **yıldız ★★★** · kökler قول *(söz söyleme)* · ربب "
 "*(rab, terbiye etme)* · قوم *(kalkma; kavim; kıyamet)* · كذب *(yalan; yalanlama)* · bağ: **26:12 "
 "ile karşılaştırma** — orada Mûsâ رَبِّ إِنِّىٓ أَخَافُ أَن يُكَذِّبُونِ *(Rabbim, beni "
 "yalanlamalarından korkuyorum)* diyordu (KORKU, gerçekleşmemiş), burada Nûh رَبِّ إِنَّ قَوْمِى "
 "كَذَّبُونِ *(Rabbim, kavmim beni yalanladı)* diyor (BİLDİRİM, gerçekleşmiş); **aynı nida, aynı "
 "kök, aynı ek, korkudan gerçekleşmeye** (elle, L1, aday 692)"),
118: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُؤْمِن = fâsıla — ARTEFAKT, sekizinci token** · "
 "aktör yok · edim emir, kip IMPV 2 · şahıs 2MS x2 · 1S x3 · 3MP x1, iltifât 0 · n=9 mora=47 "
 "harf=41 — **blokta en uzun ayet** (n z=-0,36), fâsıla ٱلْمُؤْمِنِينَ → ن, N sınıfı; **i'râb "
 "ACC 3 · GEN 1**; bab I x1 · II x1; **zaman IMPV x2 — ayetin iki fiili de emir**; **kök ikilemesi "
 "فتح *(açma)* x2 VE بين *(arası; açıklama)* x2 — İKİ KÖK BİRDEN İKİLENİYOR**; **dış düğüm 1** · "
 "yıldız ★ yok · kökler فتح *(açma)* · بين *(arası; açıklama)* · نجو *(kurtulma, kurtarma)* · أمن "
 "*(güven; iman)* · bağ: xref فتح *(açtı)* + بين *(ara)* + بين → **7:89**; **26:83 ile dua yapısı "
 "karşılaştırması** — orada İbrâhîm iki emirle (هَبْ *(bağışla)* + أَلْحِقْنِى *(kat)*), burada Nûh "
 "iki emirle (ٱفْتَحْ *(aç)* + نَجِّنِى *(kurtar)*); **iki elçi, aynı iki-emirli dua yapısı** "
 "(elle, L1, aday 693)"),
119: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "1P x2 · 3MS x2, iltifât 0 · n=6 mora=32 harf=28 (n z=-0,68), fâsıla ٱلْمَشْحُونِ *(dolu, yüklü)* → "
 "ن, N sınıfı; i'râb ACC 1 · GEN 2; bab IV x1; zaman PERF 1; dış düğüm 0 · yıldız ★ yok · kökler "
 "نجو *(kurtulma, kurtarma)* · فلك *(gemi, felek)* · شحن *(yükleme, doldurma)* · bağ: **شحن "
 "*(yükleme, doldurma)* korpusta ÜÇ geçişli ve dikey ölçümü ▸önce فلك *(gemi, felek)* x301,6 "
 "veriyor — okumada görülen EN YÜKSEK TEK KOMŞULUK KATI; çift korpusta neredeyse ayrılmaz**; "
 "**26:65 ile نجو *(kurtulma, kurtarma)* ikinci geçişi** — orada Mûsâ ve beraberindekiler, burada "
 "Nûh ve beraberindekiler; **aynı fiil, iki kıssa, aynı yapı** (elle, L1, aday 694)"),
120: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "1P x2 — ayette başka şahıs yok**, iltifât 0 · n=4 mora=24 harf=18 (n z=-0,89), fâsıla "
 "ٱلْبَاقِينَ *(geride kalanlar)* → ن, N sınıfı; **i'râb ACC 1**; bab IV x1; zaman PERF 1; dış "
 "düğüm 0 · yıldız ★ yok · kökler غرق *(boğulma)* · بعد *(sonra; uzaklık)* · بقي *(kalıcı olma)* · "
 "bağ: **26:66 ile غرق *(boğulma)* ikinci geçişi ve NEREDEYSE AYNI YAPI** — orada ثُمَّ أَغْرَقْنَا "
 "ٱلْءَاخَرِينَ *(sonra ötekileri boğduk)* (n=3), burada ثُمَّ أَغْرَقْنَا بَعْدُ ٱلْبَاقِينَ "
 "*(sonra geride kalanları boğduk)* (n=4); **ortak üç öğe (ثُمَّ + أَغْرَقْنَا + marife çoğul "
 "nesne), değişen yalnız nesne ve bir zarf**; esit YAKALAMIYOR (elle, L1, aday 695)"),
}

M = {
111: ("İtiraz bir sınıf ayrımına dayanıyor: وَٱتَّبَعَكَ ٱلْأَرْذَلُونَ *(sana ayaktakımı uydu)*. "
 "رذل *(rezil, aşağılık)* korpusta DÖRT geçişli ve dikey ölçümü ▸önce hiçbir komşu, ▸sonra yalnız "
 "ilim x12,9 veriyor — kökün korpusta dar ve tek yönlü bir yatağı var. Ölçülebilir bir kök izleği: "
 "تبع *(uyma, ardından gitme)* sûrede dördüncü geçiş ve dördüncü değeriyle — 26:40 kalabalığın "
 "niyeti (olumlu), 26:52 ilâhî uyarı (edilgen), 26:60 gerçekleşme (etken), burada bir KUSUR olarak "
 "sunuluyor. Aynı kök, dört ayet, dört değer."),
112: ("Cevap bir bilgi reddi: مَا عِلْمِى بِمَا كَانُوا۟ يَعْمَلُونَ *(onların ne yaptığına dair "
 "benim bilgim yok)*. Ölçülebilir bir kök seçimi: 26:74'te kavim atalarının يَفْعَلُونَ "
 "*(yaptıklarını)* gerekçe göstermişti, فعل *(yapma, işleme)* kökünden; burada عمل *(iş, amel)* "
 "kökü — **iki ayrı kök, aynı 'yapma' alanı**, 26:16↔26:18 (ربب *(rab)* / ربو *(yetiştirme)*), "
 "26:42↔26:58 (قرب *(yakınlık)* / قوم *(makam)*) ve 26:26↔26:76 (أول *(evvel)* / قدم *(öne "
 "geçme)*) çiftleriyle aynı desen. Sûre 26'da bu **dördüncü** vaka. Tek xref 27:84'e düşüyor."),
113: ("**Sûrenin adını veren kök burada ve 'farkında olma' anlamında**: لَوْ تَشْعُرُونَ *(bir "
 "farkında olsanız)*, شعر *(şair; farkında olma)*. Kök korpusta 40 geçişli; sûrenin adı "
 "ٱلشُّعَرَآء *(şairler)* 26:224'te gelecek — **aynı kök, iki anlam, sûrenin iki ucu** (aday 529 "
 "sınıfı, ama burada iki anlam sûre içinde karşılaşacak). Dikey ölçüm kök için ▸önce بغت *(ansızın "
 "gelme)* x85,3 · مكر *(tuzak)* x21,5 veriyor — korpusta ağırlıkla 'farkına varmadan' bağlamında; "
 "'şair' anlamı azınlık. Ve hesap HASR ile Rabbe havale ediliyor; yıldızın tek kaynağı bu Rab."),
114: ("Dört kelime, fiil yok, ve bir seyrek kök: طرد *(kovma, uzaklaştırma)* korpusta BEŞ geçişli ve "
 "dikey ölçümü **iki listede de hiçbir komşu vermiyor** — blokta ikinci 'boş komşuluk' vakası "
 "(birincisi 26:102'nin كرر *(dönüş, kere (kerre))* kökü). Ölçülebilir bir olumsuzlama: elçi bir "
 "eylemi reddediyor ve reddettiği şey itirazcıların istediği şey — 26:111'de 'ayaktakımı sana uydu' "
 "demişlerdi, burada 'onları kovacak değilim'. Ve fâsıla ٱلْمُؤْمِنِينَ esmâ sayılmış: sûrenin on "
 "beş مُؤْمِن artefaktının yedincisi."),
115: ("Beş kelime, fiil yok, HASR ile sınırlı: إِنْ أَنَا۠ إِلَّا نَذِيرٌ مُّبِينٌ *(ben ancak "
 "apaçık bir uyarıcıyım)*. Ölçülebilir bir elçi tanımı üçlüsü: 25:56 مُبَشِّرا وَنَذِيرا *(müjdeci "
 "ve uyarıcı)*, 26:107 رَسُولٌ أَمِينٌ *(güvenilir elçi)*, burada نَذِيرٌ مُّبِينٌ *(apaçık "
 "uyarıcı)* — **üçünde de HASR ya da sınırlama, üçünde de fiil yok, üçü de fâsıla**. Ve fâsıladaki "
 "مُبِين esmâ sayılmış, oysa gönderge نَذِير *(uyarıcı)*, yani elçi; sûrenin altıncı مُبِين "
 "artefaktı."),
116: ("Tehdit bir nida ile açılıyor — **sûrenin ilk VOC işareti**: لَئِن لَّمْ تَنتَهِ يَٰنُوحُ "
 "*(ey Nûh, vazgeçmezsen)*. Ölçülebilir bir kalıp eşleşmesi: 26:29'da Firavun لَأَجْعَلَنَّكَ مِنَ "
 "ٱلْمَسْجُونِينَ *(seni zindana atılanlardan yaparım)* demişti; burada لَتَكُونَنَّ مِنَ "
 "ٱلْمَرْجُومِينَ *(taşlananlardan olursun)* — **aynı 'fiil + مِنَ + ism-i mef'ûl çoğulu' kalıbı, "
 "iki kıssada iki tehdit**. رجم *(taşlama, kovma)* korpusta 14 geçişli ve dikey ölçümü ▸önce عوذ "
 "*(sığınma)* x86,1 · vazgeçme x86,1 veriyor — **'vazgeçme' komşuluğu tam bu ayetten**, yani çift "
 "korpusta bağlı. Ve aktör نُوح hem FAİL hem MUHATAP rolü alıyor; okumada bir aktörün iki rol "
 "birden aldığı ilk kayıt."),
117: ("Beş kelime ve rab z=3,94 — n=5, tek Rab, oran 0,20. Ölçülebilir bir kip karşıtlığı: 26:12'de "
 "Mûsâ رَبِّ إِنِّىٓ أَخَافُ أَن يُكَذِّبُونِ *(Rabbim, beni yalanlamalarından korkuyorum)* "
 "diyordu — KORKU ve gerçekleşmemiş; burada Nûh رَبِّ إِنَّ قَوْمِى كَذَّبُونِ *(Rabbim, kavmim "
 "beni yalanladı)* diyor — BİLDİRİM ve gerçekleşmiş. **Aynı nida, aynı kök, aynı ـُونِ eki, aynı "
 "fâsıla konumu; korkudan gerçekleşmeye.** Ve iki ayet de ★★★, ikisinde de kaynak rab oranı — "
 "aday 602 karıştırıcısı bu çifti de mekanik olarak yıldızlı gösteriyor."),
118: ("Dua iki emirle ve **iki kök birden ikileniyor**: فَٱفْتَحْ بَيْنِى وَبَيْنَهُمْ فَتْحا "
 "*(benimle onların arasını bir açışla aç)* — فتح *(açma)* fiil + mef'ûl-i mutlak, بين *(arası; "
 "açıklama)* iki kez. Okumada bir ayette iki ayrı kökün birden ikilendiği ilk yer. Ölçülebilir bir "
 "dua yapısı: 26:83'te İbrâhîm iki emirle dua ediyordu (هَبْ *(bağışla)* + أَلْحِقْنِى *(kat)*), "
 "burada Nûh iki emirle (ٱفْتَحْ *(aç)* + نَجِّنِى *(kurtar)*) — **iki elçi, aynı iki-emirli "
 "yapı**. فتح korpusta 38 geçişli ve dikey ölçümü ▸sonra بوب *(kapı)* x63,0 veriyor; burada kapı "
 "yok, 'hüküm verme' anlamında."),
119: ("Kurtarma bir araçla veriliyor: فِى ٱلْفُلْكِ ٱلْمَشْحُونِ *(dolu geminin içinde)*. شحن "
 "*(yükleme, doldurma)* korpusta ÜÇ geçişli ve dikey ölçümü ▸önce فلك *(gemi, felek)* x301,6 "
 "veriyor — **okumada görülen en yüksek tek komşuluk katı**; çift korpusta neredeyse ayrılmaz, yani "
 "'dolu gemi' terkibi bu ayete özgü değil. Ve نجو *(kurtulma, kurtarma)* 26:65'ten geri geliyor: "
 "orada وَأَنجَيْنَا مُوسَىٰ وَمَن مَّعَهُۥٓ *(Mûsâ'yı ve beraberindekileri kurtardık)*, burada "
 "فَأَنجَيْنَٰهُ وَمَن مَّعَهُۥ *(onu ve beraberindekileri kurtardık)* — **aynı fiil, aynı "
 "وَمَن مَّعَهُ yapısı, iki kıssa**. SINIR: ayet bir taşıt ADLANDIRIYOR ve bir sıfat veriyor "
 "(dolu), ama ne yapı ne ölçü ne mekanizma söylüyor."),
120: ("Dört kelime ve 26:66 ile neredeyse aynı yapı: ثُمَّ أَغْرَقْنَا ٱلْءَاخَرِينَ *(sonra "
 "ötekileri boğduk)* / ثُمَّ أَغْرَقْنَا بَعْدُ ٱلْبَاقِينَ *(sonra geride kalanları boğduk)*. "
 "**Ortak üç öğe** (ثُمَّ + أَغْرَقْنَا + marife çoğul nesne), değişen yalnız nesne ve bir zarf "
 "(بَعْدُ *(sonra)*). esit alanı bunu YAKALAMIYOR — aday 621'in 'esit_yakin' önerisine altıncı "
 "sınama vakası. غرق *(boğulma)* dikey ölçümü ▸önce فلك *(gemi, felek)* x36,1 · kurtuluş x13,5 "
 "veriyor: **ayetin iki komşusu da bir önceki ayette**, yani üçlü korpusta bağlı. Ve بقي *(kalıcı "
 "olma)* korpusta 21 geçişli; dikey ölçümü ▸önce dünya x13,9 · hayır x8,5 veriyor — kök korpusta "
 "ağırlıkla 'kalıcı olan hayır' bağlamında, burada 'geride kalan helâk edilenler' (aday 529 "
 "sınıfı)."),
}

ATLAMA = {
 "_mercek_26_117": ("26:117 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. قَالَ رَبِّ إِنَّ قَوْمِى "
  "كَذَّبُونِ. Tek kaynak rab z=3,94 (n=5, oran 0,20). İçerik bir şikâyet bildirimi."),
 "_blok_notu_26_111_120": ("BLOK BİLANÇOSU: ★★★ 1 (26:117) · ★★ 1 (26:113) · ★ 0 · 8 ayet yıldızsız. "
  "Kaynaklar: rab x2 — ikisi de eksen oranından, hiçbiri içerikten. **ÇIPA NOTU: 26:119 (dolu gemi) "
  "ve 26:120 (boğulma) çıpa TAŞIYABİLECEK ayetler ve İKİSİ DE YILDIZSIZ.** 26:119 bir taşıt "
  "adlandırıyor ve bir sıfat veriyor (مَشْحُون *(dolu, yüklü)*) ama ne yapı ne ölçü ne mekanizma "
  "söylüyor — aday 561'in önerdiği ölçütle 'adlandırma + nitelik' düzeyi, yani 25:61 ve 26:63 ile "
  "aynı sınıf. AMA 26:63'ten farklı olarak burada olay ne jeofizik ne astronomik ne biyolojik; "
  "**bir taşıt betimlemesi hiçbir mercek sınıfına düşmüyor** — aday 646'nın 'sınıf yok' gerekçesi "
  "burada da geçerli ve ayet zaten yıldızsız olduğu için mercek eşiği de aşılmıyor. SÛRE 26'NIN "
  "OKUNAN 120 AYETİNDE ★★★ 24; çıpası olan tek ★★★ hâlâ 26:63."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(111, 121):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 120/227.** Devam: 26:121'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-120 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1842
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(111, 121):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
