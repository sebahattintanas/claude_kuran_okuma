# -*- coding: utf-8 -*-
"""blok_26_121_130.py — sûre 26 onuncu blok (26:121-130). Hûd kıssası ve ön-kayıt sınaması."""
import json
DIK = json.load(open('blok_dikey_26_121_130.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
121: "Bunda elbette bir âyet var; ama onların çoğu inanmıyor.",
122: "Rabbin, elbette o Azîz'dir, Rahîm'dir.",
123: "Âd de elçileri yalanladı.",
124: "Kardeşleri Hûd onlara demişti: Sakınmıyor musunuz?",
125: "Ben size güvenilir bir elçiyim.",
126: "Allah'tan sakının ve bana itaat edin.",
127: "Buna karşılık sizden bir ücret istemiyorum; benim ücretim ancak âlemlerin Rabbine aittir.",
128: "Her tepeye bir işaret dikip boş şeyle mi oyalanıyorsunuz?",
129: "Ve sanki ebedî kalacakmışsınız gibi yapılar ediniyorsunuz.",
130: "Yakaladığınızda zorbalar gibi yakalıyorsunuz.",
}

O = {
121: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُؤْمِن *(mümin)* 8. sırada = fâsıla — ARTEFAKT, "
 "dokuzuncu token** (aday 601) · aktör yok · edim haber, kip EMPH 1 · NEG 1 · şahıs 3MS x1 · "
 "3MP x1, **iltifât 1 — yön 1>3; nakaratın DÖRDÜNCÜ geçişinde de aynı yön** · n=8 mora=40 harf=32 "
 "(n z=-0,47), fâsıla مُّؤْمِنِينَ → ن, N sınıfı; i'râb ACC 3 · NOM 1; bab I x1; zaman PERF x1; "
 "**açık sayı sözcüğü: كثر *(çokluk)* → أَكْثَر *(çoğu)***; **NAKARAT alanı = 6, temsil ayet "
 "26:8**; **esit: 26:8, 67, 103, 174, 190 ile TAM AYET ÖZDEŞ** · dış düğüm 0 · yıldız ★ yok · "
 "kökler أيي *(âyet, işaret)* · كون *(olmak; mekân, yer)* · كثر *(çokluk)* · أمن *(güven; iman)* · "
 "bağ: **birinci nakaratın DÖRDÜNCÜ geçişi** (26:8, 67, 103, 121) ve **dördünde de iltifât 1>3 — "
 "aday 679 doğrulandı** (elle, L1)"),
122: ("eksen: **lafız YOK · رَبّ *(Rab)* 2. sırada — yirmi dördüncü Rab**, **rab z=3,94: yıldızın "
 "TEK kaynağı** · **esmâ عَزِيز *(azîz)* + رَحِيم *(rahîm)* = fâsıla — MÜHÜR; GEÇERLİ; dördüncü "
 "mühür** · aktör yok · edim haber, kip EMPH 1 · şahıs 2MS x1 · 3MS x1, iltifât 0 · n=5 mora=28 "
 "harf=21 (n z=-0,79), fâsıla ٱلرَّحِيمُ → م, N sınıfı; **i'râb ACC 2 · NOM 2; fiil YOK**; "
 "**NAKARAT alanı = 8, temsil ayet 26:9**; **esit: yedi ayetle TAM ÖZDEŞ** · dış düğüm 0 · **yıldız "
 "★★★** · kökler ربب *(rab, terbiye etme)* · عزز *(izzet, üstünlük)* · رحم *(rahmet, merhamet)* · "
 "bağ: **ikinci nakaratın DÖRDÜNCÜ geçişi; nakarat çifti dört konumda** — kıssaların önü (26:8-9), "
 "Mûsâ sonu (26:67-68), İbrâhîm sonu (26:103-104), Nûh sonu (26:121-122) (elle, L1, aday 683)"),
123: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı عاد *(Âd)* 2. sırada, rol FAİL — "
 "SÛRENİN DÖRDÜNCÜ KISSASI AÇILIYOR** · edim haber, kip işareti yok · **şahıs 3FS x1 — ayette başka "
 "şahıs yok**, iltifât 0 · n=3 mora=21 harf=15 (n z=-1,00), fâsıla ٱلْمُرْسَلِينَ *(gönderilenler)* → "
 "ن, N sınıfı — **26:105'in fâsılasıyla AYNI KELİME**; i'râb NOM 1 · ACC 1; bab II x1; zaman PERF 1; "
 "dış düğüm 0 · yıldız ★ yok · kökler كذب *(yalan; yalanlama)* · عود *(geri dönme)* · رسل *(gönderme, "
 "elçi)* · bağ: **ÖN-KAYIT SINAMASI (aday 685) BAŞLIYOR — öğe (i) tekzip cümlesi VAR**; 26:105 ile "
 "birebir aynı yapı: كَذَّبَتْ + kavim adı + ٱلْمُرْسَلِينَ; **26:105'te n=4 (قَوْمُ نُوحٍ), burada "
 "n=3 (عَادٌ) — tek fark kavmin adlandırılma biçimi**; esit YAKALAMIYOR (elle, L1, aday 696)"),
124: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı هُود *(Hûd)* 5. sırada, rol FAİL** · "
 "edim soru, kip INTG 1 · NEG 1 · şahıs 3MS x1 · 3MP x2 · 2MP x2, iltifât 0 · n=7 mora=33 harf=24 "
 "(n z=-0,58), fâsıla تَتَّقُونَ *(sakınmıyor musunuz)* → ن, N sınıfı — **26:106'nın fâsılasıyla "
 "AYNI KELİME**; **i'râb NOM 2**; bab I x1 · VIII x1; zaman PERF 1 · IMPF 1; dış düğüm 0 · yıldız "
 "★ yok · kökler قول *(söz söyleme)* · أخو *(kardeş)* · هود *(Yahudi olma; Hûd)* · وقي *(sakınma, "
 "koruma)* · bağ: **ÖN-KAYIT: öğe (ii) أَلَا تَتَّقُونَ VAR — tahminde 'bulunabilir' denmişti, "
 "TUTTU**; 26:106 ile birebir aynı yapı, tek fark elçi adı; **esit YAKALAMIYOR** çünkü elçi adı "
 "değişiyor (elle, L1, aday 696)"),
125: ("eksen: **lafız YOK · Rab YOK** · esmâ yok — **أَمِين *(güvenilir)* esmâ SAYILMIYOR ve bu "
 "DOĞRU** (aday 682/690) · aktör yok · edim haber, kip işareti yok · **şahıs eki YOK, fiil YOK** · "
 "n=4 mora=21 harf=15 (n z=-0,89), fâsıla أَمِينٌ → ن, N sınıfı; **i'râb ACC 1 · NOM 2**; **NAKARAT "
 "alanı = 5, temsil ayet 26:107**; **esit: 26:107, 143, 162, 178 ile TAM AYET ÖZDEŞ** · dış düğüm "
 "0 · yıldız ★ yok · kökler رسل *(gönderme, elçi)* · أمن *(güven; iman)* · bağ: **ÖN-KAYIT: öğe "
 "(iii) VAR; üçüncü nakarat kümesinin ikinci geçişi** (elle, L1, aday 696)"),
126: ("eksen: **ALLAH LAFZI 2. sırada — sûrenin ALTINCI lafzı**, **allah z=6,14: yıldızın TEK "
 "kaynağı** (n=3, oran 0,33) · Rab yok · esmâ yok · aktör yok · edim emir, kip IMPV 2 · şahıs "
 "2MP x4 · 1S x1, iltifât 0 · n=3 mora=23 harf=18 (n z=-1,00), fâsıla وَأَطِيعُونِ → ن, N sınıfı; "
 "**i'râb ACC 1**; bab IV x1 · VIII x1; zaman IMPV x2; **NAKARAT alanı = 8, temsil ayet 26:108**; "
 "**esit: yedi ayetle TAM ÖZDEŞ** · dış düğüm 0 · **yıldız ★★★** · kökler وقي *(sakınma, koruma)* · "
 "أله *(ilâh; lafza-i celâl)* · طوع *(güç yetirme, itaat)* · bağ: **ÖN-KAYIT: öğe (iv) VAR; "
 "dördüncü nakarat kümesinin ÜÇÜNCÜ geçişi ve üçünde de ★★★** (elle, L1, aday 696)"),
127: ("eksen: **lafız YOK · رَبّ *(Rab)* 10. sırada — yirmi beşinci Rab** (rab z=1,62: yıldızın TEK "
 "kaynağı) · esmâ yok · aktör yok · edim haber, kip NEG 2 · RES 1 · şahıs 1S x2 · 2MP x1 · 3MS x1, "
 "iltifât 0 · n=11 mora=50 harf=40 — **blokta en uzun ayet** (n z=-0,15), fâsıla ٱلْعَٰلَمِينَ → ن, "
 "N sınıfı; **i'râb GEN 3 · NOM 1**; bab I x1; zaman IMPF 1; **kök ikilemesi أجر *(ücret, karşılık)* "
 "x2**; **biçim HASR**; simetri [4,1,6,1]; **NAKARAT alanı = 5, temsil ayet 26:109**; **esit: "
 "26:109, 145, 164, 180 ile TAM AYET ÖZDEŞ** · dış düğüm 0 · **yıldız ★** · kökler سأل *(isteme, "
 "dileme)* · أجر *(ücret, karşılık)* · ربب *(rab, terbiye etme)* · علم *(bilme; âlem)* · bağ: "
 "**ÖN-KAYIT: öğe (v) VAR; beşinci nakarat kümesinin ikinci geçişi** (elle, L1, aday 696)"),
128: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · **şahıs "
 "2MP x4 — ayette başka şahıs yok**, iltifât 0 · n=5 mora=31 harf=23 (n z=-0,79), fâsıla "
 "تَعْبَثُونَ *(boş şeyle oyalanıyorsunuz)* → ن, N sınıfı; **i'râb GEN 2 · ACC 1**; bab I x2; zaman "
 "IMPF x2; **HAPAKS: ريع *(yüksek yer, tepe)* — korpusta TEK geçiş** (hapaks z=3,38: **yıldızın TEK "
 "kaynağı**); dış düğüm 0 · **yıldız ★★★** · kökler بني *(bina, yapma)* · كلل *(hep, bütün)* · ريع "
 "*(yüksek yer, tepe)* · أيي *(âyet, işaret)* · عبث *(boş yere, amaçsız oyalanma)* · bağ: **أيي "
 "*(âyet, işaret)* — 529 KÜMESİNE YENİ VAKA**: kök korpusta 597 geçişli ve ezici çoğunlukla 'ilâhî "
 "âyet' anlamında; burada 'yapı, anıt, işaret' anlamında ve **dikey satırı korpus anlamını "
 "getiriyor** (▸önce tafsil x6,2 · جحد *(inkâr, bile bile reddetme)* x5,8) (elle, L1, aday 697)"),
129: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "2MP x5 — ayette başka şahıs yok**, iltifât 0 · n=4 mora=30 harf=23 (n z=-0,89), fâsıla "
 "تَخْلُدُونَ *(ebedî kalıyorsunuz)* → ن, N sınıfı; **i'râb ACC 2**; bab I x1 · VIII x1; zaman "
 "IMPF x2; dış düğüm 0 · yıldız ★ yok · kökler أخذ *(alma, edinme)* · صنع *(yapma, işleme)* · خلد "
 "*(ebedî kalma)* · bağ: **أخذ *(alma, edinme)* bab VIII — sûre 25'te yedi geçişi olan kalıp, "
 "burada 'yapı edinme'**; **صنع *(yapma, işleme)* korpusta 20 geçişli ve dikey ölçümü ▸önce hiçbir "
 "komşu, ▸sonra فلك *(gemi, felek)* x40,2 veriyor — kökün korpustaki ana yatağı GEMİ YAPIMI, burada "
 "kale/köşk yapımı** (aday 529 sınıfı) (elle, L1, aday 698)"),
130: ("eksen: **lafız YOK · Rab YOK** · **esmâ جَبّار *(cebbâr)* 4. sırada = fâsıla, MÜHÜRSÜZ — "
 "ÖLÇÜM ARTEFAKTI**: جَبَّارِينَ *(zorbalar)* çoğul ve gönderge İNSANLAR; ölçüt (a) ve (b) birden "
 "dışlıyor · aktör yok · edim haber, kip işareti yok · **şahıs 2MP x4 — ayette başka şahıs yok** "
 "(üç ardışık ayette de aynı), iltifât 0 · n=4 mora=26 harf=20 (n z=-0,89), fâsıla جَبَّارِينَ → ن, "
 "N sınıfı; **i'râb ACC 1**; bab I x2; zaman PERF x2; **kök ikilemesi بطش *(şiddetle yakalama, "
 "kahretme)* x2 — fiil + mef'ûl-i mutlak yerine fiil + hâl: بَطَشْتُم بَطَشْتُمْ جَبَّارِينَ**; "
 "dış düğüm 0 · yıldız ★ yok · kökler بطش *(şiddetle yakalama, kahretme)* · جبر *(zorbalık)* · "
 "bağ: **26:128-130 üçlüsü — üç ayette de 2MP dört-beş kez ve başka şahıs yok; üçü de soru ya da "
 "suçlama**; **بطش korpusta 10 geçişli ve dikey ölçümü ▸önce hiçbir komşu, ▸sonra takvâ x12,0 "
 "veriyor** (elle, L1, aday 699)"),
}

M = {
121: ("Birinci nakaratın dördüncü geçişi (26:8, 67, 103, 121) ve **dördünde de iltifât 1 ve yön "
 "1>3** — aday 679 doğrulandı: nakaratın iltifâtı sabit ve sayaç tekrarları da sayıyor. Sûrenin "
 "'iltifât 15' ölçümünün en az dördü tek bir ayetten geliyor. Ve fâsıladaki مُؤْمِن sûrenin "
 "dokuzuncu artefaktı; nakarat tekrarları esmâ sayımını da şişiriyor — **altı geçişin altısı da "
 "aynı token.**"),
122: ("İkinci nakaratın dördüncü geçişi. Ölçülebilir bir mimari tamamlanıyor: nakarat çifti artık "
 "**dört konumda** — kıssaların önünde (26:8-9), Mûsâ kıssasının sonunda (26:67-68), İbrâhîm "
 "kıssasının sonunda (26:103-104), Nûh kıssasının sonunda (26:121-122). rab z=3,94 dört ayette de "
 "aynı, çünkü dört ayet de aynı. Sûrenin on mühründen dördüncüsü ve mühür GEÇERLİ — mühürlü "
 "konumlar sûre 25'te de temiz çıkmıştı (aday 501/598)."),
123: ("**Ön-kayıt sınaması başlıyor** (aday 685). Öğe (i) tekzip cümlesi: كَذَّبَتْ عَادٌ "
 "ٱلْمُرْسَلِينَ *(Âd elçileri yalanladı)* — **VAR**. 26:105 ile birebir aynı yapı (كَذَّبَتْ + "
 "kavim adı + ٱلْمُرْسَلِينَ); tek fark kavmin adlandırılma biçimi: orada tamlama (قَوْمُ نُوحٍ, "
 "n=4), burada tek ad (عَادٌ, n=3). **esit alanı bunu yakalamıyor.** عود *(geri dönme)* burada "
 "'Âd' özel adı olarak kodlanmış ve dikey ölçümü ▸önce بدأ *(başlama)* x83,2 · ▸sonra Hûd x45,4 "
 "veriyor — **ikinci komşu tam bir sonraki ayetin konusu**, yani 'Âd + Hûd' çifti korpusta bağlı."),
124: ("**Ön-kayıt öğesi (ii) VAR.** Tahminde 'Lût ve Şuayb'da bulunmayabilir' demiştim, Hûd için "
 "'bulunabilir' bırakmıştım — **tuttu.** 26:106 ile birebir aynı yapı (إِذْ قَالَ لَهُمْ أَخُوهُمْ "
 "+ elçi adı + أَلَا تَتَّقُونَ); tek fark elçi adı ve `esit` bunu **yakalamıyor**. Ölçülebilir bir "
 "kök tuzağı: هود *(Yahudi olma; Hûd)* kökü burada ÖZEL AD ama dikey ölçümü ▸sonra صبأ *(sâbiî)* "
 "x226,4 · Hristiyan x196,2 veriyor — **korpusta ezici çoğunlukla 'Yahudi' anlamında**; kök düzeyi "
 "komşuluk özel adı hiç ayırmıyor (aday 529 sınıfı, sûre 26'nın onuncu vakası)."),
125: ("**Ön-kayıt öğesi (iii) VAR.** Üçüncü nakarat kümesinin ikinci geçişi; dört kelime, fiil yok. "
 "Ve burada 682/690'ın tanısı bir kez daha görünüyor: أَمِين *(güvenilir)* esmâ **sayılmıyor** ve "
 "bu doğru — ama sûrenin dokuz مُؤْمِن artefaktı aynı kökten. **Tablo aynı kökün iki lemmasını iki "
 "ayrı hükümle işliyor ve fark gönderge değil, LİSTE.**"),
126: ("**Ön-kayıt öğesi (iv) VAR.** Dördüncü nakarat kümesinin üçüncü geçişi ve **üçünde de ★★★**, "
 "üçünde de allah z=6,14. Bu, aday 683'ün sekiz ayetlik kümesinin üçüncü örneği; küme tamamlandığında "
 "sûrenin 41 ★★★ ayetinin sekizi buradan gelecek. Üç kelime, iki emir, tek lafız."),
127: ("**Ön-kayıt öğesi (v) VAR.** Beşinci nakarat kümesinin ikinci geçişi. Kök ikilemesi أجر "
 "*(ücret, karşılık)* x2 ve HASR; simetri [4,1,6,1]. Blokta en uzun ayet ve yıldızı yalnız ★ — "
 "**aday 602'nin karşı yönlü kanıtı bir kez daha**: aynı bölütte üç kelimelik 26:126 ★★★ alıyor, "
 "on bir kelimelik bu ayet ★ alıyor, ve ikisinin de kaynağı eksen oranı."),
128: ("Hûd'un ilk suçlaması bir soru ve bir hapaks taşıyor: بِكُلِّ رِيعٍ ءَايَةً *(her tepeye bir "
 "işaret)*, ريع *(yüksek yer, tepe)* korpusta TEK geçiş ve yıldızın tek kaynağı. Ölçülebilir bir "
 "anlam kayması: أيي *(âyet, işaret)* korpusta 597 geçişli ve ezici çoğunlukla 'ilâhî âyet' "
 "anlamında; burada 'yapı, anıt, işaret'. **Ve dikey satırı korpus anlamını getiriyor** (▸önce "
 "tafsil x6,2 · جحد *(inkâr, bile bile reddetme)* x5,8) — 529 kümesine yeni ve çok sık bir kök. "
 "عبث *(boş yere, amaçsız oyalanma)* korpusta İKİ geçişli ve dikey ölçümü iki listede de boş. "
 "SINIR: ayet bir yapı türünü ADLANDIRIYOR ama ne malzeme ne ölçü ne teknik veriyor."),
129: ("İkinci suçlama bir kalıcılık iddiasına yöneliyor: لَعَلَّكُمْ تَخْلُدُونَ *(sanki ebedî "
 "kalacakmışsınız gibi)*. صنع *(yapma, işleme)* korpusta 20 geçişli ve dikey ölçümü ▸önce hiçbir "
 "komşu, ▸sonra فلك *(gemi, felek)* x40,2 veriyor — **kökün korpustaki ana yatağı GEMİ YAPIMI** "
 "(Nûh kıssası), burada kale/köşk yapımı; aday 529 sınıfı ve ilginç olan, gemi kıssasının dokuz "
 "ayet önce bitmiş olması. Ve أخذ *(alma, edinme)* bab VIII — sûre 25'te yedi geçişi olan kalıp, "
 "burada 'yapı edinme' anlamında. SINIR: ayet yapıların yapıldığını SÖYLÜYOR, ne türünü ne ölçüsünü "
 "veriyor."),
130: ("Üçüncü suçlama bir davranış biçimine: بَطَشْتُم بَطَشْتُمْ جَبَّارِينَ *(yakaladığınızda "
 "zorbalar gibi yakalıyorsunuz)*. Kök ikilemesi بطش *(şiddetle yakalama, kahretme)* x2 ama yapı "
 "mef'ûl-i mutlak DEĞİL — fiil + fiil + hâl. Kök korpusta 10 geçişli ve dikey ölçümü ▸önce hiçbir "
 "komşu, ▸sonra takvâ x12,0 veriyor. Ölçülebilir bir bölüt yapısı: **26:128, 129, 130 — üç ayette "
 "de 2MP dört-beş kez ve başka şahıs yok**; üçü de suçlama. Ve fâsıladaki جَبَّار esmâ sayılmış, "
 "oysa çoğul ve gönderge insanlar — iki ölçüt birden dışlıyor; sûrenin esmâ artefaktları büyüyor."),
}

ATLAMA = {
 "_mercek_26_122_126": ("26:122 ve 26:126 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. İkisi de NAKARAT: "
  "26:122 ikinci kümenin dördüncü geçişi (rab z=3,94), 26:126 dördüncü kümenin üçüncü geçişi "
  "(allah z=6,14). Bağımsız gözlem değil (adaylar 606, 683)."),
 "_mercek_26_128": ("26:128 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. أَتَبْنُونَ بِكُلِّ رِيعٍ ءَايَةً "
  "تَعْبَثُونَ. Tek kaynak hapaks z=3,38 (ريع *(yüksek yer, tepe)*, korpusta tek geçiş). ÇIPA "
  "DEĞERLENDİRMESİ: ayet bir yapı türünü ADLANDIRIYOR (her tepeye bir işaret) ama ne malzeme, ne "
  "ölçü, ne teknik, ne süreç veriyor — aday 561'in ölçütüyle 'adlandırma' düzeyinin de ALTINDA "
  "(nitelik bile yok). Ayrıca 26:63 gibi bir mercek sınıfı sorusu da doğurmuyor; mimari ne biyoloji "
  "ne astronomi. **Çıpa sayılmadı.**"),
 "_blok_notu_26_121_130": ("BLOK BİLANÇOSU: ★★★ 3 (26:122, 126, 128) · ★★ 0 · ★ 1 (26:127) · 6 ayet "
  "yıldızsız. **ÜÇ ★★★ AYETİN İKİSİ NAKARAT**, üçüncüsü hapaks kaynaklı; hiçbirinde çıpa yok. "
  "**ÖN-KAYIT SINAMASI (aday 685): Hûd kıssasında ALTI ÖĞENİN ALTISI DA VAR** — (i) 26:123, "
  "(ii) 26:124, (iii) 26:125, (iv) 26:126, (v) 26:127, (vi) 26:131 (blok dışı, esit listesinde). "
  "Tahminde (ii) için 'Lût ve Şuayb'da bulunmayabilir' denmişti; Hûd için belirsiz bırakılmıştı ve "
  "VAR ÇIKTI. **ASIL SINAMA LÛT (26:160-) VE ŞUAYB (26:176-) KISSALARINDA.** SÛRE 26'NIN OKUNAN "
  "130 AYETİNDE ★★★ 27; çıpası olan tek ★★★ hâlâ 26:63."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(121, 131):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 130/227.** Devam: 26:131'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-130 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1852
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(121, 131):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
