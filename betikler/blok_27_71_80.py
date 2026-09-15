# -*- coding: utf-8 -*-
"""blok_27_71_80.py — sûre 27 sekizinci blok (27:71-80). Vaadin zamanı, Rab kümesi,
sûrenin son mührü ve Kur'ân hakkında dört ayet."""
import json
DIK = json.load(open('blok_dikey_27_71_80.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
71: "Diyorlar: Doğru söylüyorsanız, bu vaat ne zaman?",
72: "De ki: Çabuklaştırmak istediğinizin bir kısmı belki de ardınıza takılmıştır.",
73: "Rabbin insanlara karşı lütuf sahibidir, ama çoğu şükretmiyor.",
74: "Rabbin, göğüslerinin gizlediğini de açığa vurduklarını da elbette bilir.",
75: "Gökte ve yerde gizli hiçbir şey yoktur ki apaçık bir kitapta olmasın.",
76: "Bu Kur'ân, İsrâiloğullarına, ayrılığa düştükleri şeylerin çoğunu anlatıyor.",
77: "Ve o, müminler için bir yol gösterme ve rahmettir.",
78: "Rabbin, hükmüyle aralarında karar verir; O, Azîz'dir, Alîm'dir.",
79: "Allah'a tevekkül et; sen apaçık gerçek üzeresin.",
80: "Sen ölülere işittiremezsin; arkalarını dönüp giderlerken sağırlara da çağrıyı işittiremezsin.",
}

O = {
71: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru + şart, kip INTG 1 · COND "
 "1 · şahıs 3MP x2 · 2MP x2, sahset ['2','3'], iltifât 0 · **n=7** (n z=-0,58), fâsıla "
 "صَٰدِقِينَ *(doğru söyleyenler)* → ن, N sınıfı — **27:64 ile aynı fâsıla**; **i'râb NOM 1 · ACC "
 "1**; bab I x2; zaman IMPF 1 · PERF 1; **`esit` ALANI DOLU VE BEŞ HEDEFLİ: 10:48 · 21:38 · 34:29 "
 "· 36:48 · 67:25 — okumada ilk çok hedefli eşleşme; altı ayetin altısı da BİREBİR aynı metin**; "
 "**biçim DIKKAT**; **dış düğüm 5** · yıldız ★ yok · kökler قول *(söz söyleme)* · وعد *(vaat)* · كون *(olmak; mekân, yer)* · صدق *(doğruluk)* (elle, L1, aday "
 "855)"),
72: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir, kip IMPV 1 · şahıs 2MS x1 "
 "· 3MS x3 · 2MP x3, iltifât 0 · n=9 mora=40 harf=32 (n z=-0,36), fâsıla تَسْتَعْجِلُونَ "
 "*(çabuklaştırmak istiyorsunuz)* → ن, N sınıfı; **i'râb NOM 1**; bab I x4 · **bab X x1**; zaman "
 "IMPV 1 · PERF x2 · IMPF x2; dış düğüm 1 · yıldız ★ yok · kökler قول *(söz söyleme)* · عسي *(umma, olabilme)* · كون *(olmak; mekân, yer)* · **ردف *(ardından gelme, birinin terkisine binme)* "
 "*(ardından gelme, birinin terkisine binme)* — YENİ KÖK, n=3** · بعض *(bir kısım)* · عجل *(acele)* · bağ: xref قال + "
 "عسى + كان → **17:51**; **عجل *(acele)* 27:46'dan sonra sûrede ikinci geçiş ve İKİSİ DE aynı "
 "bab X kalıbında** (تَسْتَعْجِلُونَ) — biri Semûd'a, biri Mekke'ye (elle, L1)"),
73: ("eksen: lafız yok · **رَبّ *(Rab)* 2. sırada — sûrenin ALTINCI Rabbi** (rab z=1,81) · esmâ "
 "yok · aktör yok · edim haber, kip EMPH 1 · NEG 1 · şahıs 2MS x1 · 3MP x3, iltifât 0 · n=10 "
 "mora=51 harf=38 (n z=-0,26), fâsıla يَشْكُرُونَ *(şükrediyorlar)* → ن, N sınıfı; **i'râb ACC 4 · "
 "NOM 1 · GEN 2**; bab I x1; zaman IMPF 1; **SAYI ALANI: كثر *(çokluk)* → أَكْثَر *(çoğu)*** — sûrede üçüncü "
 "kez; simetri [3,1,5,1]; dış düğüm 1 · **yıldız ★** — kaynak YALNIZ Rab · kökler ربب *(rab, terbiye etme)* · فضل *(üstün kılma, lütuf)* · أنس *(insan)* "
 "· كثر *(çokluk)* · شكر *(şükür)* · bağ: xref ناس + أكثر + شكر *(şükür)* → **10:60**; **شكر *(şükür)* 27:40'tan sonra sûrede "
 "ikinci geçiş: orada Süleymân'ın şükrü, burada insanların şükürsüzlüğü** (elle, L2)"),
74: ("eksen: lafız yok · **رَبّ 2. sırada — sûrenin YEDİNCİ Rabbi** (rab z=2,34) · esmâ yok · aktör "
 "yok · edim haber, kip EMPH 1 · şahıs 2MS x1 · 3MS x1 · 3FS x1 · 3MP x3, iltifât 0 · **n=8** (n "
 "z=-0,47), fâsıla يُعْلِنُونَ *(açığa vuruyorlar)* → ن, N sınıfı — **27:25 ile aynı fâsıla**; "
 "**i'râb ACC 2 · NOM 1**; bab I x1 · IV x2; **zaman IMPF x3**; dış düğüm 1 · **yıldız ★★** — "
 "kaynak YALNIZ Rab · kökler ربب *(rab, terbiye etme)* · علم *(bilme)* · **كنن *(gizleme, örtme (kinn))* — YENİ KÖK, n=12** · صدر *(göğüs)* "
 "· علن *(açığa vurma, alenî)* · bağ: xref ربّ + علم *(bilme)* + أكنن ve türevleri → **ÜÇÜ DE 28:69**; **علن *(açığa vurma, alenî)* "
 "27:25'ten sonra sûrede ikinci ve son geçiş; iki ayet de 'gizleneni ve açığa vurulanı bilme' "
 "yapısında, elli ayet arayla** (elle, L1)"),
75: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُبِين *(apaçık)* 10. sırada = fâsıla, MÜHÜRSÜZ — "
 "ARTEFAKT**: gönderge كِتَٰب *(kitap)*; sûrenin altı مُبِين tokeninin BEŞİNCİSİ · aktör yok · "
 "edim haber, kip NEG 1 · RES 1 · **şahıs işareti YOK — blokta tek vaka** · n=10 mora=54 harf=38 "
 "(n z=-0,26), fâsıla مُّبِينٍ *(apaçık)* → ن, N sınıfı; **i'râb GEN 5 — beşinin beşi de mecrur**; "
 "**fiil YOK**; simetri [3,1,7,1]; **biçim HASR**; dış düğüm 1 · yıldız ★ yok · kökler غيب *(gayb, görünmeyen)* · سمو *(ad; gök)* · "
 "أرض *(yer, yeryüzü)* · كتب *(yazma, kitap)* · بين *(arası; açıklama)* · bağ: xref سماء + أرض *(yer, yeryüzü)* + كتاب → **22:70**; **غيب *(gayb, görünmeyen)* 27:65'ten "
 "sonra sûrede ikinci geçiş, on ayet arayla** (elle, L1, aday 857/858)"),
76: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı قُرْءان *(Kur'ân)* 3. sırada, tür "
 "KİTAB, rol mef'ûl — sûrede ilk ve tek 'kitab' türü aktör · adlı إِسْرائِيل *(İsrâîl)* 7. sırada, "
 "tür kavim, rol mecrur** · edim haber · **şahıs 3MS x2 · 3MP x3, sahset ['3']** · n=12 mora=65 "
 "harf=47 (n z=-0,04), fâsıla يَخْتَلِفُونَ *(ayrılığa düşüyorlar)* → ن, N sınıfı; **i'râb ACC 3 · "
 "GEN 2**; bab I x1 · **bab VIII x1**; zaman IMPF x2; **SAYI ALANI: كثر *(çokluk)* → أَكْثَر** — ardışık "
 "ayetlerde ikinci kez (27:73, burası); simetri [3,1,9,1]; **biçim DIKKAT**; dış düğüm 0 · yıldız "
 "★ yok · kökler قرأ *(okuma)* · قصص *(anlatma; iz sürme)* · بني *(bina, yapma)* · كثر *(çokluk)* · خلف *(ayrılığa düşme; ardından gelme)* · bağ: **خلف *(ayrılığa düşme; ardından gelme)* "
 "27:62'den sonra sûrede ikinci geçiş ve İKİ ANLAM ALANI: orada خُلَفَآء *(halifeler)*, burada "
 "يَخْتَلِفُونَ *(ayrılığa düşüyorlar)*** (elle, L1, aday 861)"),
77: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُؤْمِن *(mümin)* 4. sırada = fâsıla, MÜHÜRSÜZ — "
 "ARTEFAKT**: gönderge ٱلْمُؤْمِنِينَ *(müminler)*, İNSAN ÇOĞUL; sûrenin üç مُؤْمِن tokeninin "
 "ÜÇÜNCÜSÜ ve son · aktör yok · edim haber, kip EMPH 1 · **şahıs 3MS x1, sahset ['3']** · **n=4 — "
 "sûrenin ikinci en kısa ayeti** (27:2'de n=3; n z=-0,89), fâsıla لِّلْمُؤْمِنِينَ *(müminler "
 "için)* → ن, N sınıfı; **i'râb ACC 1 · GEN 2 · NOM 1**; **fiil YOK**; dış düğüm 1 · yıldız ★ yok "
 "· kökler هدي *(yol gösterme)* · رحم *(rahmet, merhamet)* · أمن *(güven; iman)* · bağ: xref هدى + رحمة + مؤمن → **10:57**; **هدي *(yol gösterme)* "
 "sûrede ALTINCI geçiş** (27:24, 35, 36, 41, 63, burası) **ve DÖRDÜNCÜ anlam alanı: burada "
 "'hidâyet'** — yol bulma, hediye, tanıma, hidâyet (elle, L1, aday 857/861)"),
78: ("eksen: lafız yok · **رَبّ 2. sırada — sûrenin SEKİZİNCİ Rabbi** (rab z=2,34) · **esmâ عَزِيز "
 "*(azîz)* 7. + عَلِيم *(alîm)* 8. sırada = fâsıla — MÜHÜR; GEÇERLİ (gönderge هُوَ, mercii "
 "رَبّ); sûrenin ALTINCI ve SON mührü, ALTINCI FARKLI ÇİFT** · aktör yok · edim haber · şahıs 2MS "
 "x1 · 3MS x3 · 3MP x1, iltifât 0 · **n=8** (n z=-0,47), fâsıla ٱلْعَلِيمُ *(Alîm)* → **م — "
 "azınlık kafiyesi; sûrenin dokuz م fâsılasının SONUNCUSU**, N sınıfı; **i'râb ACC 3 · GEN 1 · NOM "
 "2**; bab I x1; zaman IMPF 1; dış düğüm 0 · **yıldız ★★** — kaynak YALNIZ Rab · kökler ربب *(rab, terbiye etme)* · قضي *(hükmetme, bitirme)* "
 "· بين *(arası; açıklama)* · حكم *(hüküm verme, hikmet)* · عزز *(izzet, güç ve üstünlük)* · علم *(bilme)* · bağ: **ADAY 804'ÜN İKİNCİ VE SON ÖN-KAYIT SINAMASI — TUTTU** (elle, "
 "L1, aday 856)"),
79: ("eksen: **ALLAH LAFZI 3. sırada** (allah z=2,33) · Rab yok · **esmâ مُبِين 7. sırada = fâsıla, "
 "MÜHÜRSÜZ — ARTEFAKT**: gönderge ٱلْحَقّ *(gerçek)*, soyut kavram; **sûrenin altı مُبِين "
 "tokeninin ALTINCISI ve SON — dizi KAPANDI** · aktör yok · edim emir, kip IMPV 1 · **şahıs 2MS "
 "x2, sahset ['2']** · **n=7** (n z=-0,58), fâsıla ٱلْمُبِينِ *(apaçık)* → ن, N sınıfı; **i'râb "
 "GEN 3 · ACC 1**; **bab V x1 — ayetin tek fiili**; zaman IMPV 1; dış düğüm 1 · **yıldız ★★** — "
 "kaynak YALNIZ eksen · kökler وكل *(vekil kılma, tevekkül)* · أله *(ilâh; lafza-i celâl)* · حقق *(hak, gerçek)* · بين *(arası; açıklama)* · bağ: xref اللّه + حقّ + مبين → **24:25** "
 "(elle, L1, aday 857/858)"),
80: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, **kip NEG 2** · şahıs 2MS "
 "x2 · 3FS x1 · 3MP x2, iltifât 0 · n=11 mora=59 harf=46 (n z=-0,15), fâsıla مُدْبِرِينَ *(arkasını "
 "dönenler)* → ن, N sınıfı; **i'râb ACC 4 · NOM 1**; bab II x1 · IV x2; zaman IMPF x2 · PERF 1; "
 "**kök ikilemesi سمع *(işitme)* x2 — ikisi de olumsuz (لَا تُسْمِعُ)**; simetri [3,2,5,1]; dış "
 "düğüm 1 · yıldız ★ yok · kökler سمع *(işitme)* · موت *(ölüm)* · صمم *(sağırlık)* · دعو *(çağırma, dua)* · ولي *(dost, veli; velâyet)* · دبر *(arka)* · bağ: **xref BEŞ 3-gram ve "
 "beşi de TEK ayete: 30:52**; **ve 30:52 ile aradaki tek fark baştaki فَ — `esit` alanı İKİSİNDE "
 "DE BOŞ** (elle, L2, aday 854/860)"),
}

M = {
71: ("Yedi kelimelik bir soru ve **okumada ilk çok hedefli `esit`: beş hedef** — 10:48, 21:38, "
 "34:29, 36:48, 67:25. Ölçüldü: **altı ayetin altısı da BİREBİR aynı metin**, tek harf farkı bile "
 "yok. Alan burada tam olarak yapması gerekeni yapıyor. **Bu, `esit`in ne olduğunu netleştiriyor: "
 "ayet düzeyinde TAM DİZGE eşleşmesi.** Ve hemen ardından sınırı da görülecek — 27:80'de aynı alan "
 "tek harf yüzünden kör kalıyor. Fâsıla 27:64 ile aynı (صَٰدِقِينَ): orada delil isteniyordu, "
 "burada zaman soruluyor; **aynı fâsıla, karşılıklı iki meydan okuma.**"),
72: ("Cevap bir ihtimalle: عَسَىٰٓ أَن يَكُونَ رَدِفَ لَكُم *(belki ardınıza takılmıştır)*. Yeni "
 "kök ردف *(ardından gelme, birinin terkisine binme)* korpusta üç geçişli ve dikey satırı iki "
 "listede de boş. **Ölçülebilir bir kalıp tekrarı: عجل *(acele)* sûrede ikinci geçiş ve ikisi de "
 "aynı bab X kalıbında** — 27:46'da Semûd'a تَسْتَعْجِلُونَ بِٱلسَّيِّئَةِ, burada Mekke'ye "
 "تَسْتَعْجِلُونَ. **İki ayrı kavim, aynı fiil, aynı vezin, yirmi altı ayet arayla; ikisi de "
 "azabın çabuklaştırılmasını isteme bağlamında.** Fâsıla da aynı kökten."),
73: ("**Sûrenin son Rab kümesi burada başlıyor: 27:73, 27:74, 27:78 — üçünde de رَبّ ikinci "
 "sırada.** Bu ayette rab z=1,81 ve **yıldızın tek kaynağı bu.** Sûrede Rab on ayette geçiyor "
 "(27:8, 19, 26, 40, 44, 73, 74, 78, 91, 93) ve bunların üçü bu blokta. **Ölçülebilir bir "
 "karşıtlık: 27:40'ta Süleymân şükrediyordu (شكر *(şükür)* üç kez), burada insanların çoğu "
 "şükretmiyor** — aynı kök, aynı sûre, karşıt yön. Ve **sayı alanı أَكْثَر sûrede üçüncü kez** "
 "(27:61, 73, 76); üçünde de olumsuz bir yargıyla birlikte."),
74: ("İkinci Rab ve **rab z=2,34 — sûrede 27:26 ve 27:78 ile eşit, en yüksek Rab değeri.** "
 "Yıldızın tek kaynağı yine Rab. **Ölçülebilir bir yankı: علن *(açığa vurma, alenî)* sûrede "
 "ikinci ve son geçiş ve iki ayet de aynı yapıda** — 27:25 'gizlediğinizi de açığa vurduğunuzu da "
 "bilir', burada 'göğüslerinin gizlediğini de açığa vurduklarını da bilir'; **elli ayet arayla, "
 "biri hüdhüdün ağzında biri anlatıcının.** Yeni kök كنن *(gizleme, örtme (kinn))* korpusta on iki "
 "geçişli ve dikey satırı ▸sonra kulak-ağırlığı ×380,8 veriyor — **ölçüldü: bu kalıp (kalplere "
 "örtü, kulaklara ağırlık) korpusta dört ayette ve dördü de aynı donmuş terkip**, yani aday "
 "835'in Tür B'si. Ve xref üç 3-gram'ın üçü de 28:69'a düşüyor."),
75: ("**Ayette ne fiil var ne şahıs işareti — blokta tek vaka** ve beş ismin beşi de mecrur. "
 "Biçim HASR: 'hiçbir gizli yoktur ki ... olmasın'. Esmâ tarafında مُبِين mühürsüz ve göndergesi "
 "كِتَٰب *(kitap)* — **ARTEFAKT; sûrenin altı مُبِين tokeninin beşincisi.** Aday 803'ün dizisi "
 "burada beşe çıkıyor ve dört ayet sonra kapanacak. **غيب *(gayb, görünmeyen)* sûrede ikinci "
 "geçiş: 27:65'te 'Allah'tan başkası gaybı bilmez', burada 'gökte ve yerde gizli hiçbir şey "
 "yoktur ki kitapta olmasın'** — **on ayet arayla aynı konunun iki yüzü: bilinmezlik ve kayıt.**"),
76: ("**Sûrede ilk ve tek 'kitab' türü adlı aktör: قُرْءان *(Kur'ân)*.** Sûrenin aktör türü "
 "envanteri burada tamamlanıyor: kişi, kavim, gayb, kitab. Ve ölçülebilir bir kök izi: **خلف *(ayrılığa düşme; ardından gelme)* "
 "*(ayrılığa düşme; ardından gelme)* sûrede ikinci geçiş ve iki anlam alanı** — 27:62'de "
 "خُلَفَآء *(halifeler)*, burada يَخْتَلِفُونَ *(ayrılığa düşüyorlar)*. **529 kümesinin sûre içi "
 "BEŞİNCİ vakası** (سمو *(ad; gök)*, هدي *(yol gösterme)*, طير *(kuş; uçan)*, كشف *(giderme, açma)*, خلف *(ayrılığa düşme; ardından gelme)*) ve dikey satırı yine tek anlam alanından geliyor; "
 "**ölçüt 2/9'a düştü.** Sayı alanı أَكْثَر üçüncü kez."),
77: ("Dört kelime — **sûrenin ikinci en kısa ayeti** (27:2'de n=3). Esmâ tarafında مُؤْمِن "
 "mühürsüz, gönderge ٱلْمُؤْمِنِينَ, yani insan çoğul — **ARTEFAKT; sûrenin üç مُؤْمِن tokeninin "
 "üçüncüsü ve dizi burada kapanıyor: 3/3 artefakt, üçünde de gönderge insan** (27:2, 15, 77). "
 "Sûre 26'da aynı lemma 15/15 artefakt çıkmıştı (aday 601/709); **iki sûre, on sekiz token, "
 "hepsi artefakt.** Ve **هدي *(yol gösterme)* sûrede ALTINCI geçiş ve DÖRDÜNCÜ anlam alanı**: yol "
 "bulma (27:24, 41 tanıma) · hediye (27:35, 36) · yol gösterme (27:63) · **hidâyet (burası)**. "
 "**Tek kök, tek sûre, dört anlam alanı — 529 kümesinin en dallanmış vakası.**"),
78: ("**Sûrenin altıncı ve son mührü; aday 804'ün ikinci ve son ön-kayıt sınaması TUTTU.** "
 "`عَزِيز|عَلِيم`, gönderge هُوَ ve mercii bir önceki رَبّ — **GEÇERLİ.** Ve dizi artık tam "
 "sayımla kapanabilir: **sûrede altı mühür, altı FARKLI çift, altısı da `م` fâsılalı ve altısı da "
 "GEÇERLİ.** (27:6 حَكِيم|عَلِيم · 27:9 عَزِيز|حَكِيم · 27:11 غَفُور|رَحِيم · 27:30 "
 "رَحْمٰن|رَحِيم · 27:40 غَنِيّ|كَرِيم · 27:78 عَزِيز|عَلِيم.) Sûrenin dokuz `م` fâsılasının altısı "
 "mühür, üçü değil (27:23, 26, 29) — **ve üçü de okundu, yani aday 804 kapandı.** Yıldızın tek "
 "kaynağı yine Rab (z=2,34); **mührün kendisi yıldıza katkı vermiyor.**"),
79: ("**Lafız üçüncü sırada ve allah z=2,33 — sûrenin ikinci en yüksek eksen z'si** (27:59'da "
 "2,80). n=7'lik bir ayette tek lafız bu değeri veriyor; **27:63'te n=20'de İKİ lafız 1,47 "
 "vermişti.** Aday 847'nin dördüncü vakası ve en çarpıcısı: **tek lafız, iki lafızdan yüksek z.** "
 "Esmâ tarafında مُبِين mühürsüz, gönderge ٱلْحَقّ *(gerçek)* — **ARTEFAKT ve dizi KAPANDI: "
 "sûrenin altı مُبِين tokeninin ALTISI DA artefakt** (27:1 kitâb · 27:13 sihr · 27:16 fadl · 27:21 "
 "sultân · 27:75 kitâb · 27:79 hak). **Hiçbirinde gönderge ilâhî değil; altısı da fâsıla konumunda; "
 "altısı da mühürsüz.** Aday 803 kapandı."),
80: ("**`esit` alanının sınırı burada görünüyor.** Ayet 30:52 ile **tek harf farkla** aynı — orada "
 "başta bir فَ var, başka hiçbir fark yok. **`esit` alanı İKİSİNDE DE BOŞ.** Oysa dokuz ayet önce "
 "27:71'de aynı alan beş hedefi birden yakalamıştı. **Mekanizma kesin: alan TAM DİZGE eşleşmesi "
 "yapıyor ve baştaki tek bir bağlaç harfi eşleşmeyi tümüyle bozuyor.** Ölçüldü: korpusta tam aynı "
 "metinli 87 küme var (257 ayet); baştaki و/ف atılınca 94 küme (273 ayet) oluyor — **yani dokuz "
 "küme, yirmi dokuz ayet yalnız bu tek harf yüzünden kaçıyor.** İçlerinde 1:2 ↔ 37:182 ve "
 "**94:5 ↔ 94:6 (ARDIŞIK iki ayet!)** de var. Ve xref tarafı doğru çalışıyor: **beş 3-gram'ın "
 "beşi de 30:52'ye düşüyor** — yani bağ zaten görünüyordu, `esit` görmedi."),
}

ATLAMA = {
 "_blok_notu_27_71_80": ("BLOK BİLANÇOSU: ★★★ 0 · ★★ 3 (27:74 Rab, 27:78 Rab, 27:79 eksen) · ★ 1 "
  "(27:73 Rab) · yıldızsız 6. **Kaynaklar: Rab x3 · lafız x1 — içerikten sıfır, ve okumada ilk "
  "kez yıldızların TAMAMI eksenden.** İltifât 0/10. Esmâ token 5: **üçü artefakt (27:75 مُبِين, "
  "27:77 مُؤْمِن, 27:79 مُبِين), ikisi geçerli mühür (27:78).** Allah lafzı 1 · **Rab 3 — okumada "
  "en yüksek blok Rab sayısı.** Adlı aktör 2 (قُرْءان, إِسْرائِيل) · adsız aktör 0. Yeni kök 2 "
  "(ردف *(ardından gelme, birinin terkisine binme)*, كنن *(gizleme, örtme (kinn))*). Hapaks 0. Kafiye kırılması 0. **Üç dizi KAPANDI: مُبِين 6/6 artefakt · مُؤْمِن 3/3 "
  "artefakt · mühür 6/6 geçerli.** **Yıldızsız oran %60 — altı blok sonra ilk kez %80'in "
  "altında.**"),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(71, 81):
    OM['27']["27:%d" % n] = {"ar": AR[(27, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["27:%d" % n]}
OM['27']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-26 TAM. **Sûre 27 (Neml) 80/93.** Devam: 27:81'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "27": "1-80 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 2029
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 27 →', len([k for k in OM['27'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(71, 81):
    MK['27']["27:%d" % n] = M[n]
MK['27_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 27 →', len(MK['27']))
