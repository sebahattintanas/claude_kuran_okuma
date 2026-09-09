# -*- coding: utf-8 -*-
"""blok_26_211_220.py — sûre 26 on dokuzuncu blok (26:211-220). İkinci mühür çifti çıkıyor."""
import json
DIK = json.load(open('blok_dikey_26_211_220.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
211: "Bu onlara yaraşmaz; buna güçleri de yetmez.",
212: "Onlar işitmekten kesinlikle uzaklaştırılmışlardır.",
213: "Allah ile beraber başka bir ilâha yalvarma; yoksa azaba uğratılanlardan olursun.",
214: "En yakın aşiretini uyar.",
215: "Sana uyan müminlere kanadını indir.",
216: "Sana karşı gelirlerse de ki: Ben sizin yaptıklarınızdan uzağım.",
217: "Azîz ve Rahîm olana tevekkül et.",
218: "O, kalktığında seni görüyor.",
219: "Secde edenler arasında dolaşmanı da.",
220: "O, işitendir, bilendir.",
}

O = {
211: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 2 · şahıs 3MS x1 · "
 "3MP x3, iltifât 0 · n=5 mora=28 harf=23 (n z=-0,79), fâsıla يَسْتَطِيعُونَ *(güç yetiriyorlar)* → "
 "ن, N sınıfı; **i'râb YOK**; **bab VII x1 · bab X x1**; zaman IMPF x2; dış düğüm 0 · yıldız ★ yok · "
 "kökler بغي *(arama, isteme; azgınlık)* · طوع *(güç yetirme, itaat)* · bağ: **26:210 ile bitişik "
 "çift — kaynak reddinin gerekçesi**; **طوع *(güç yetirme, itaat)* sûrede DOKUZUNCU geçiş ama İLK "
 "KEZ 'güç yetirme' anlamında** — 26:108/110/126/131/144/150/163/179 nakaratında ve 26:151'de hep "
 "'itaat' anlamındaydı; **aynı sûrede iki anlam, 529 kümesine YEDİNCİ sûre-içi vaka** (elle, L1, "
 "aday 762)"),
212: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip EMPH 1 · **şahıs "
 "3MP x1 — ayette başka şahıs yok**, iltifât 0 · n=4 mora=25 harf=19 (n z=-0,89), fâsıla "
 "لَمَعْزُولُونَ *(uzaklaştırılmışlar)* → ن, N sınıfı; **i'râb ACC 1 · GEN 1 · NOM 1; fiil YOK**; "
 "dış düğüm 0 · yıldız ★ yok · kökler سمع *(işitme)* · عزل *(uzaklaştırma, ayırma)* · bağ: "
 "**26:15, 26:25, 26:72 ile سمع *(işitme)* DÖRDÜNCÜ geçişi ve DÖRDÜNCÜ özneyle** — 26:15 ilâhî "
 "eşlik, 26:25 Firavun'un alayı, 26:72 putların yetisi, burada ŞEYTANLARIN engellenmesi; "
 "**عزل *(uzaklaştırma, ayırma)* korpusta BEŞ geçişli**; **ÖLÇÜ TANIMI EKSİĞİ: مَعْزُولُونَ "
 "edilgen ism-i mef'ûl ama fiil olmadığı için `pas` sayacı GÖRMÜYOR** (aday 706) (elle, L1, "
 "aday 763)"),
213: ("eksen: **ALLAH LAFZI 4. sırada — sûrenin ON İKİNCİ lafzı** (allah z=1,69: yıldızın TEK "
 "kaynağı) · Rab yok · esmâ yok · aktör yok · edim haber, kip NEG 1 · şahıs 3FS x1 · 2MS x1, "
 "iltifât 0 · n=9 mora=48 harf=35 (n z=-0,36), fâsıla ٱلْمُعَذَّبِينَ *(azaba uğratılanlar)* → ن, "
 "N sınıfı — **26:138'in fâsılası بِمُعَذَّبِينَ ile AYNI LEMMA**; **i'râb ACC 3 · GEN 2**; bab I "
 "x2; zaman IMPF x2; **kök ikilemesi أله *(ilâh; lafza-i celâl)* x2 — LAFIZ ve SAHTE İLÂH aynı "
 "ayette**; **dış düğüm 1** · **yıldız ★** · kökler دعو *(çağırma, dua)* · أله *(ilâh; lafza-i "
 "celâl)* · أخر *(geciktirme, sonraya bırakma)* · كون *(olmak; mekân, yer)* · عذب *(azap)* · bağ: "
 "xref آخر *(başka)* + كان *(oldu)* + معذّب *(azaba uğratılan)* → **17:15**; **25:68 ile AYNI "
 "YAPI** — orada da lafız ve sahte ilâh tek ayette (وَلَا يَدْعُونَ مَعَ ٱللَّهِ إِلَٰهًا "
 "ءَاخَرَ *(Allah ile beraber başka bir ilâha yalvarmazlar)*); **burada 2MS emir, orada 3MP "
 "bildirim** (elle, L1, aday 764)"),
214: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir, kip IMPV 1 · **şahıs "
 "2MS x2 — ayette başka şahıs yok**, iltifât 0 · n=3 mora=23 harf=19 (n z=-1,00), fâsıla "
 "ٱلْأَقْرَبِينَ *(en yakınlar)* → ن, N sınıfı; **i'râb ACC 2**; bab IV x1; zaman IMPV 1; **açık "
 "sayı sözcüğü: عشر *(on; aşiret)* → عَشِيرَت — ÖLÇÜM ARTEFAKTI**: sayı dedektörü عشر kökünü 'on' "
 "sanmış, oysa عَشِيرَة *(aşiret)*; **aktör tablosundaki 'ferîk' artefaktıyla (aday 641) AYNI "
 "SINIF: kök düzeyinde eşleşme, lemma denetimi yok**; dış düğüm 0 · yıldız ★ yok · kökler نذر "
 "*(uyarma; adak)* · عشر *(on; aşiret)* · قرب *(yakınlık, yaklaşma)* · bağ: **26:42 ve 26:58 ile "
 "قرب *(yakınlık, yaklaşma)* ÜÇÜNCÜ geçişi** — 26:42 saray yakınlığı (vaat), 26:58 konum, burada "
 "SOY yakınlığı (elle, L1, aday 765)"),
215: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُؤْمِن *(mümin)* 6. sırada = fâsıla, MÜHÜRSÜZ — "
 "ARTEFAKT, sûrenin ON BEŞİNCİ ve SON tokeni** (aday 601 tam sayım) · aktör yok · edim emir, kip "
 "IMPV 1 · şahıs 2MS x3 · 3MS x1, iltifât 0 · n=6 mora=33 harf=28 (n z=-0,68), fâsıla "
 "ٱلْمُؤْمِنِينَ → ن, N sınıfı; **i'râb ACC 1 · GEN 1**; bab I x1 · VIII x1; zaman IMPV 1 · PERF 1; "
 "dış düğüm 0 · yıldız ★ yok · kökler خفض *(indirme, alçaltma)* · جنح *(kanat; meyletme)* · تبع "
 "*(uyma, ardından gitme)* · أمن *(güven; iman)* · bağ: **تبع *(uyma, ardından gitme)* sûrede "
 "BEŞİNCİ geçiş ve BEŞİNCİ değerle** — 26:40 niyet, 26:52 uyarı, 26:60 gerçekleşme, 26:111 kusur, "
 "burada OLUMLU BAĞLILIK; **aynı kök, beş ayet, beş değer** (elle, L1, aday 766)"),
216: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir + şart, kip COND 1 · "
 "IMPV 1 · şahıs 3MP x2 · 2MS x2 · 1S x1 · 2MP x2, iltifât 0 · n=7 mora=37 harf=27 (n z=-0,58), "
 "fâsıla تَعْمَلُونَ *(yapıyorsunuz)* → ن, N sınıfı — **26:188'in fâsılasıyla AYNI KELİME**; "
 "**i'râb ACC 1 · NOM 1**; bab I x3; zaman PERF 1 · IMPV 1 · IMPF 1; dış düğüm 0 · yıldız ★ yok · "
 "kökler عصي *(karşı gelme, isyan)* · قول *(söz söyleme)* · برأ *(uzak olma, berâet)* · عمل *(iş, "
 "amel)* · bağ: **26:112, 26:168, 26:188 ile عمل *(iş, amel)* DÖRDÜNCÜ geçişi ve DÖRDÜNCÜ tutumla** — "
 "Nûh bilgisizlik, Lût öfke, Şuayb bilgiyi havale, burada UZAK DURMA (بَرِىٓءٌ مِّمَّا تَعْمَلُونَ "
 "*(yaptıklarınızdan uzağım)*); **dört elçi/muhatap, dört tutum** (elle, L1, aday 767)"),
217: ("eksen: **lafız YOK · Rab YOK** · **esmâ عَزِيز *(azîz)* 3. + رَحِيم *(rahîm)* 4. sırada = "
 "fâsıla — MÜHÜR; GEÇERLİ; ve NAKARAT DIŞI İLK GEÇİŞ** (nakarat alanı 0) · aktör yok · edim emir, "
 "kip IMPV 1 · **şahıs 2MS x1 — ayette başka şahıs yok**, iltifât 0 · n=4 mora=27 harf=20 "
 "(n z=-0,89), fâsıla ٱلرَّحِيمِ → م, N sınıfı; **i'râb GEN 2**; **bab V x1**; zaman IMPV 1; dış "
 "düğüm 0 · yıldız ★ yok · kökler وكل *(vekil kılma, tevekkül)* · عزز *(izzet, üstünlük)* · رحم "
 "*(rahmet, merhamet)* · bağ: **ADAY 745'E SINAMA — عَزِيز|رَحِيم çifti sûrede DOKUZUNCU kez ama "
 "İLK KEZ NAKARAT DIŞINDA**; sekiz nakarat geçişinde ayet وَإِنَّ رَبَّكَ لَهُوَ ٱلْعَزِيزُ "
 "ٱلرَّحِيمُ ve ★★★ idi, burada وَتَوَكَّلْ عَلَى ٱلْعَزِيزِ ٱلرَّحِيمِ ve **YILDIZSIZ** — "
 "**çünkü Rab yok** (elle, L1, aday 768)"),
218: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3MS x1 · 2MS x2, iltifât 0 · n=4 mora=21 harf=15 (n z=-0,89), fâsıla تَقُومُ *(kalkıyorsun)* → "
 "م, N sınıfı; **i'râb ACC 1**; bab I x2; zaman IMPF x2; dış düğüm 0 · yıldız ★ yok · kökler رأي "
 "*(görme)* · حين *(vakit, süre)* · قوم *(kalkma; kavim; kıyamet)* · bağ: **قوم *(kalkma; kavim; "
 "kıyamet)* — sûrede ÇOK GEÇİŞLİ ama burada İLK KEZ 'kalkma' anlamında**; kıssalarda hep 'kavim' "
 "anlamındaydı (26:10, 70, 105, 117, 160, 166…); **aynı sûrede iki anlam, 529 kümesine SEKİZİNCİ "
 "sûre-içi vaka** (elle, L1, aday 769)"),
219: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "2MS x1 — ayette başka şahıs yok**, iltifât 0 · n=3 mora=20 harf=15 (n z=-1,00), fâsıla "
 "ٱلسَّٰجِدِينَ *(secde edenler)* → ن, N sınıfı — **26:46'nın fâsılasıyla AYNI KÖK**; **i'râb "
 "ACC 1 · GEN 1; fiil YOK**; dış düğüm 0 · yıldız ★ yok · kökler قلب *(çevirme; kalp)* · سجد "
 "*(secde)* · bağ: **26:46 ile سجد *(secde)* İKİNCİ geçişi** — orada büyücüler EDİLGEN olarak "
 "secdeye kapanıyordu (فَأُلْقِىَ ٱلسَّحَرَةُ سَٰجِدِينَ) ve ayet ★★★ idi; burada secde edenler "
 "bir TOPLULUK adı ve ayet yıldızsız; **قلب *(çevirme; kalp)* burada DÖRDÜNCÜ geçiş ve İLK KEZ "
 "'dolaşma, çevrilme' anlamında** — 26:89, 194, 200'de 'kalp'ti; **529 kümesine DOKUZUNCU sûre-içi "
 "vaka** (elle, L1, aday 770)"),
220: ("eksen: **lafız YOK · Rab YOK** · **esmâ سَمِيع *(semî')* 3. + عَلِيم *(alîm)* 4. sırada = "
 "fâsıla — MÜHÜR; GEÇERLİ; VE SÛRENİN İKİNCİ MÜHÜR ÇİFTİ** (birincisi عَزِيز|رَحِيم) · aktör yok · "
 "edim haber, kip işareti yok · **şahıs 3MS x2 — ayette başka şahıs yok**, iltifât 1 — yön 2>3; "
 "sûrenin on dördüncü iltifâtı · n=4 mora=23 harf=18 (n z=-0,89), fâsıla ٱلْعَلِيمُ *(alîm)* → م, "
 "N sınıfı; **i'râb ACC 1 · NOM 2; fiil YOK**; dış düğüm 0 · yıldız ★ yok · kökler سمع *(işitme)* · "
 "علم *(bilme; ilim)* · bağ: **SÛREDE İKİNCİ MÜHÜR ÇİFTİ ÇIKIYOR — سَمِيع|عَلِيم**; sekiz nakarat "
 "geçişi + 26:217 hep عَزِيز|رَحِيم idi; **bu, sûrenin on mühründen onuncusu ve TEK FARKLI OLANI**; "
 "**سمع *(işitme)* sûrede BEŞİNCİ geçiş** (26:15, 25, 72, 212, burada) ve **İLK KEZ ilâhî sıfat "
 "olarak** (elle, L1, aday 771)"),
}

M = {
211: ("Kaynak reddinin gerekçesi iki olumsuzlamayla: وَمَا يَنۢبَغِى لَهُمْ وَمَا يَسْتَطِيعُونَ "
 "*(bu onlara yaraşmaz; buna güçleri de yetmez)*. **Ölçülebilir bir anlam kayması: طوع *(güç "
 "yetirme, itaat)* sûrede dokuzuncu geçiş ama ilk kez 'güç yetirme' anlamında** — sekiz nakarat "
 "geçişinde (26:108, 110, 126, 131, 144, 150, 163, 179) ve 26:151'de hep **'itaat'** anlamındaydı. "
 "Aynı sûrede iki anlam; 529 kümesine sûre 26'nın **yedinci** sûre-içi vakası. Ve بغي *(arama, "
 "isteme; azgınlık)* burada 'yaraşma' anlamında — kök korpusta 96 geçişli ve ağırlıkla 'azgınlık, "
 "haddi aşma' bağlamında. Ayet i'râb etiketi almıyor."),
212: ("Dört kelime, fiil yok: إِنَّهُمْ عَنِ ٱلسَّمْعِ لَمَعْزُولُونَ *(işitmekten kesinlikle "
 "uzaklaştırılmışlardır)*. **Ölçülebilir bir dizi: سمع *(işitme)* sûrede dördüncü kez ve dördüncü "
 "özneyle** — 26:15 ilâhî eşlik (مُّسْتَمِعُونَ), 26:25 Firavun'un alayı (أَلَا تَسْتَمِعُونَ), "
 "26:72 putların yetisi (هَلْ يَسْمَعُونَكُمْ), burada şeytanların **engellenmesi**. Dört ayet, "
 "dört özne katmanı. عزل *(uzaklaştırma, ayırma)* korpusta **beş** geçişli. **ÖLÇÜ TANIMI EKSİĞİ: "
 "مَعْزُولُونَ edilgen ism-i mef'ûl ama fiil olmadığı için `pas` sayacı görmüyor** — aday 706'nın "
 "ikinci vakası."),
213: ("Emir bir yasak biçiminde ve **kök ikilemesi أله *(ilâh; lafza-i celâl)* ×2**: فَلَا تَدْعُ "
 "مَعَ ٱللَّهِ إِلَٰهًا ءَاخَرَ *(Allah ile beraber başka bir ilâha yalvarma)* — **lafız ve sahte "
 "ilâh aynı ayette**. 25:68'de de aynı yapı vardı; **fark: orada 3MP bildirim (وَلَا يَدْعُونَ "
 "*(yalvarmazlar)*), burada 2MS emir.** Yıldızın tek kaynağı bu lafız (allah z=1,69). Ve fâsıla "
 "ٱلْمُعَذَّبِينَ 26:138'in بِمُعَذَّبِينَ'iyle aynı lemma — orada kavmin **reddi**, burada elçiye "
 "**uyarı**. Tek xref 17:15'e düşüyor."),
214: ("Üç kelime ve bir **ölçüm artefaktı**: وَأَنذِرْ عَشِيرَتَكَ ٱلْأَقْرَبِينَ *(en yakın "
 "aşiretini uyar)*. `say` alanı عشر *(on; aşiret)* kökünü **açık sayı sözcüğü** saymış — oysa "
 "عَشِيرَة *(aşiret)*, sayı değil. **Bu, aktör tablosundaki 'ferîk' artefaktıyla (aday 641) aynı "
 "sınıf: kök düzeyinde eşleşme, lemma denetimi yok.** Ve قرب *(yakınlık, yaklaşma)* sûrede üçüncü "
 "kez ve üçüncü türde: 26:42 **saray** yakınlığı (vaat), 26:58 **konum**, burada **soy** yakınlığı."),
215: ("Emir bir alçalma imgesiyle: وَٱخْفِضْ جَنَاحَكَ *(kanadını indir)*. جنح *(kanat; meyletme)* "
 "korpusta 15 geçişli ve dikey ölçümü ▸önce خفض *(indirme, alçaltma)* komşuluğu veriyor — çift "
 "korpusta bağlı. **Ölçülebilir bir kök izleği: تبع *(uyma, ardından gitme)* sûrede beşinci geçiş "
 "ve beşinci değerle** — 26:40 niyet, 26:52 uyarı (edilgen), 26:60 gerçekleşme, 26:111 **kusur**, "
 "burada **olumlu bağlılık** (ٱتَّبَعَكَ مِنَ ٱلْمُؤْمِنِينَ *(sana uyan müminler)*). Aynı kök, "
 "beş ayet, beş değer. Ve fâsıladaki مُؤْمِن sûrenin **on beşinci ve son** artefaktı — aday 601'in "
 "tam sayımı: on beş token, on beşi artefakt."),
216: ("Şartın cevabı bir uzak durma bildirimi: إِنِّى بَرِىٓءٌ مِّمَّا تَعْمَلُونَ *(ben sizin "
 "yaptıklarınızdan uzağım)*. **Ölçülebilir bir dörtlü: عمل *(iş, amel)* sûrede dördüncü kez ve "
 "dördüncü tutumla** — Nûh 26:112 **bilgisizlik**, Lût 26:168 **öfke**, Şuayb 26:188 **bilgiyi "
 "havale**, burada **uzak durma**. Dört ayet, dört tutum. Ve fâsıla تَعْمَلُونَ 26:188'inkiyle "
 "aynı kelime. برأ *(uzak olma, berâet)* korpusta 31 geçişli."),
217: ("**Aday 745'e sınama ve sonuç ölçülebilir: عَزِيز|رَحِيم çifti sûrede dokuzuncu kez ama ilk "
 "kez nakarat dışında** (nakarat alanı 0). Sekiz nakarat geçişinde ayet وَإِنَّ رَبَّكَ لَهُوَ "
 "ٱلْعَزِيزُ ٱلرَّحِيمُ ve **★★★** idi; burada وَتَوَكَّلْ عَلَى ٱلْعَزِيزِ ٱلرَّحِيمِ *(Azîz ve "
 "Rahîm olana tevekkül et)* ve **yıldızsız**. **Fark tek ve ölçülebilir: burada رَبّ yok.** Yani "
 "sekiz ★★★'ın kaynağı esmâ çifti değil, ayetteki Rab oranıydı — **aday 602/745'in en temiz "
 "gösterimi.** Mühür yine GEÇERLİ. وكل *(vekil kılma, tevekkül)* korpusta 70 geçişli, bab V."),
218: ("Dört kelime: ٱلَّذِى يَرَىٰكَ حِينَ تَقُومُ *(kalktığında seni gören)*. **Ölçülebilir bir "
 "anlam kayması: قوم *(kalkma; kavim; kıyamet)* sûrede çok geçişli ama burada ilk kez 'kalkma' "
 "anlamında** — kıssalarda hep 'kavim' anlamındaydı (26:10, 70, 105, 117, 160, 166…). Aynı sûrede "
 "iki anlam; 529 kümesine **sekizinci** sûre-içi vaka. حين *(vakit, süre)* korpusta 32 geçişli ve "
 "burada bir zaman zarfı. **SINIR: ayet bir görme ilişkisi bildiriyor, ne mekanizma ne ölçü; çıpa "
 "sayılmadı.**"),
219: ("Üç kelime, fiil yok: وَتَقَلُّبَكَ فِى ٱلسَّٰجِدِينَ *(secde edenler arasında dolaşmanı)*. "
 "**Ölçülebilir bir anlam kayması: قلب *(çevirme; kalp)* sûrede dördüncü geçiş ve ilk kez "
 "'dolaşma, çevrilme' anlamında** — 26:89, 194, 200'de 'kalp'ti; 529 kümesine **dokuzuncu** "
 "sûre-içi vaka. Ve سجد *(secde)* 26:46'dan geri geliyor: orada büyücüler **edilgen** olarak "
 "secdeye kapanıyordu ve ayet **★★★** idi (pas z=5,38); burada secde edenler bir **topluluk adı** "
 "ve ayet yıldızsız — **aynı kök, iki çatı, iki yıldız durumu.**"),
220: ("**Sûrenin ikinci mühür çifti burada çıkıyor: سَمِيع|عَلِيم.** Sekiz nakarat geçişi ve 26:217 "
 "hep عَزِيز|رَحِيم idi; bu, sûrenin on mühründen **onuncusu ve tek farklı olanı**. Mühür GEÇERLİ. "
 "Ve **سمع *(işitme)* sûrede beşinci geçiş** (26:15, 25, 72, 212, burada) ve **ilk kez ilâhî sıfat "
 "olarak** — önceki dördü sırasıyla ilâhî eşlik (fiil), Firavun'un alayı, putların yetisi, "
 "şeytanların engellenmesi. Aynı kök, beş ayet, beş konum ve sonuncusu bir esmâ. Sûrenin on "
 "dördüncü iltifâtı burada."),
}

ATLAMA = {
 "_blok_notu_26_211_220": ("BLOK BİLANÇOSU: ★★★ 0 · ★★ 0 · ★ 1 (26:213) · 9 ayet yıldızsız — "
  "**okumada ★★★ çıkmayan İKİNCİ ardışık blok**. Tek ★ ayetin kaynağı lafız oranı (allah z=1,69). "
  "**ADAY 745/602'NİN EN TEMİZ GÖSTERİMİ 26:217'DE: عَزِيز|رَحِيم mühür çifti sûrede dokuzuncu kez "
  "ama İLK KEZ NAKARAT DIŞINDA ve İLK KEZ YILDIZSIZ — çünkü ayette رَبّ yok. Yani sekiz ★★★'ın "
  "kaynağı esmâ çifti DEĞİL, Rab oranıydı.** VE 26:220'DE SÛRENİN İKİNCİ MÜHÜR ÇİFTİ ÇIKIYOR "
  "(سَمِيع|عَلِيم) — on mühürden onuncusu ve tek farklı olanı; mühür GEÇERLİ. ÇIPA NOTU: 26:218 "
  "bir görme ilişkisi bildiriyor (يَرَىٰكَ حِينَ تَقُومُ), ne mekanizma ne ölçü — çıpa sayılmadı. "
  "SÛRE 26'NIN OKUNAN 220 AYETİNDE ★★★ 41 — sûrenin toplamı; kalan 7 ayette yeni ★★★ yok."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(211, 221):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 220/227.** Devam: 26:221'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-220 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1942
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(211, 221):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
