# -*- coding: utf-8 -*-
"""blok_26_191_200.py — sûre 26 on yedinci blok (26:191-200). Sûrenin son bölütü açılıyor."""
import json
DIK = json.load(open('blok_dikey_26_191_200.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
191: "Rabbin, elbette o Azîz'dir, Rahîm'dir.",
192: "O, âlemlerin Rabbinin indirmesidir.",
193: "Onu Rûhu'l-Emîn indirdi.",
194: "Senin kalbine; uyarıcılardan olasın diye.",
195: "Apaçık Arap diliyle.",
196: "O, öncekilerin kitaplarında da vardır.",
197: "İsrâiloğulları bilginlerinin onu bilmesi onlar için bir âyet değil mi?",
198: "Onu yabancılardan birine indirseydik,",
199: "ve onu onlara okusaydı, ona inanmazlardı.",
200: "İşte onu suçluların kalplerine böyle soktuk.",
}

O = {
191: ("eksen: **lafız YOK · رَبّ *(Rab)* 2. sırada — otuz beşinci Rab**, **rab z=3,94: yıldızın TEK "
 "kaynağı** · **esmâ عَزِيز *(azîz)* + رَحِيم *(rahîm)* = fâsıla — MÜHÜR; GEÇERLİ; SEKİZİNCİ VE "
 "SON mühür bu kümede** · aktör yok · edim haber, kip EMPH 1 · şahıs 2MS x1 · 3MS x1, iltifât 0 · "
 "n=5 mora=28 harf=21 (n z=-0,79), fâsıla ٱلرَّحِيمُ → م, N sınıfı; **i'râb ACC 2 · NOM 2; fiil "
 "YOK**; **NAKARAT alanı = 8, temsil ayet 26:9 — İKİNCİ KÜME TAMAMLANDI (8/8)**; **esit: yedi "
 "ayetle TAM ÖZDEŞ** · dış düğüm 0 · **yıldız ★★★** · kökler ربب *(rab, terbiye etme)* · عزز "
 "*(izzet, üstünlük)* · رحم *(rahmet, merhamet)* · bağ: **nakarat çiftinin SEKİZİNCİ ve son geçişi; "
 "aday 744'ün tablosu tamam — Şuayb kıssasında da BÜTÜN** (elle, L1, aday 745)"),
192: ("eksen: **lafız YOK · رَبّ *(Rab)* 3. sırada — otuz altıncı Rab**, **rab z=5,01: yıldızın TEK "
 "kaynağı** (n=4, oran 0,25) · esmâ yok · aktör yok · edim haber, kip EMPH 1 · **şahıs 3MS x1 — "
 "ayette başka şahıs yok**, iltifât 0 · n=4 mora=26 harf=20 (n z=-0,89), fâsıla ٱلْعَٰلَمِينَ "
 "*(âlemler)* → ن, N sınıfı; **i'râb ACC 1 · NOM 1 · GEN 2; fiil YOK**; **dış düğüm 2** · **yıldız "
 "★★★** · kökler نزل *(indirme)* · ربب *(rab, terbiye etme)* · علم *(bilme; âlem)* · bağ: xref "
 "تنزيل *(indirme)* + ربّ *(Rab)* + عالم *(âlem)* → **56:80 · 69:43**; **رَبّ ٱلْعَٰلَمِينَ "
 "terkibinin sûrede YEDİNCİ geçişi ve İLK KEZ NAKARAT DIŞINDA, KISSA DIŞINDA** — 26:16, 23, 47, "
 "77 kıssalarda, 26:109/127/145/164/180 nakaratta, burada anlatıcı sesinde (elle, L1, aday 746)"),
193: ("eksen: **lafız YOK · Rab YOK** · esmâ yok — **أَمِين *(güvenilir)* esmâ SAYILMIYOR ve bu "
 "SEFER TARTIŞMALI**: ٱلرُّوحُ ٱلْأَمِينُ *(Rûhu'l-Emîn)* bir MELEK adı; gönderge ne ilâhî ne "
 "insan — **aday 682/709'un sınama kümesine ÜÇÜNCÜ SINIF: melek göndergesi** · aktör yok — "
 "ٱلرُّوح *(ruh)* aktör tablosuna GİRMİYOR · edim haber, kip işareti yok · **şahıs 3MS x2 — ayette "
 "başka şahıs yok**, iltifât 0 · n=4 mora=21 harf=16 (n z=-0,89), fâsıla ٱلْأَمِينُ *(güvenilir)* → "
 "ن, N sınıfı — **26:107, 125, 143, 162, 178'in fâsılasıyla AYNI KÖK, farklı gönderge**; **i'râb "
 "NOM 2**; bab I x1; zaman PERF 1; dış düğüm 0 · yıldız ★ yok · kökler نزل *(indirme)* · روح "
 "*(ruh, rüzgâr)* · أمن *(güven; iman)* · bağ: **26:192 ile bitişik çift ve نزل *(indirme)* kök "
 "tekrarı** — orada تَنزِيل *(indirme)* masdar, burada نَزَلَ *(indi)* fiil; **aynı kök, iki "
 "biçim, bitişik ayet** (elle, L1, aday 747)"),
194: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "2MS x2 — ayette başka şahıs yok**, **iltifât 1 — yön 3>2; sûrenin on birinci iltifâtı** · n=5 "
 "mora=27 harf=22 (n z=-0,79), fâsıla ٱلْمُنذِرِينَ *(uyarıcılar)* → ن, N sınıfı — **26:173'ün "
 "fâsılası ٱلْمُنذَرِينَ *(uyarılanlar)* ile AYNI KÖK, TERS ÇATI** (ism-i fâil / ism-i mef'ûl); "
 "**i'râb GEN 2**; bab I x1; zaman IMPF 1; dış düğüm 0 · yıldız ★ yok · kökler قلب *(çevirme; "
 "kalp)* · كون *(olmak; mekân, yer)* · نذر *(uyarma; adak)* · bağ: **26:89 ve 26:200 ile قلب "
 "*(kalp)* üçlüsü** — 26:89 قَلْبٍ سَلِيمٍ *(temiz kalp)* kurtuluş şartı, burada vahyin İNDİĞİ "
 "yer, 26:200 vahyin SOKULDUĞU yer; **aynı kök, üç işlev** (elle, L1, aday 748)"),
195: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُبِين *(apaçık)* 3. sırada = fâsıla, MÜHÜRSÜZ — "
 "ÖLÇÜM ARTEFAKTI**: gönderge لِسَان *(dil)*; sûrenin YEDİNCİ مُبِين artefaktı · aktör yok · edim "
 "haber, kip işareti yok · **şahıs eki YOK, fiil YOK** · n=3 mora=22 harf=15 (n z=-1,00), fâsıla "
 "مُّبِينٍ → ن, N sınıfı; **i'râb GEN 3 — üç kelimenin üçü de mecrur**; **dış düğüm 1** · yıldız "
 "★ yok · kökler لسن *(dil)* · عرب *(Arapça; bedevî)* · بين *(arası; açıklama)* · bağ: xref لسان "
 "*(dil)* + عربيّ *(Arapça)* + مبين *(apaçık)* → **16:103**; **26:13 ve 26:84 ile لسن *(dil)* "
 "ÜÇÜNCÜ geçişi ve ÜÇÜNCÜ anlamı** — 26:13 Mûsâ'nın YETERSİZLİĞİ (dil çözülmez), 26:84 İbrâhîm'in "
 "istediği NAM (doğruluk dili), burada DİL/LİSAN (Arapça); **529 kümesine sûre-içi üçlü** "
 "(elle, L1, aday 749)"),
196: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip EMPH 1 · **şahıs "
 "3MS x1 — ayette başka şahıs yok**, **iltifât 1 — yön 2>3; sûrenin on ikinci iltifâtı** · n=4 "
 "mora=22 harf=18 (n z=-0,89), fâsıla ٱلْأَوَّلِينَ *(öncekiler)* → ن, N sınıfı — **26:26, 76, "
 "137, 184'ün fâsılasıyla AYNI KELİME, BEŞİNCİ kez**; **i'râb ACC 1 · GEN 2; fiil YOK**; dış düğüm "
 "0 · yıldız ★ yok · kökler زبر *(kitap, sahifeler; zebûr)* · أول *(ilk, evvel)* · bağ: **زبر "
 "*(kitap, sahifeler; zebûr)* korpusta 11 geçişli**; **ٱلْأَوَّلِينَ fâsılası sûrede beş kez ve "
 "beş ayrı bağlamda**: atalar (26:26), atalar (26:76), âdet (26:137), nesiller (26:184), KİTAPLAR "
 "(burada) (elle, L1, aday 750)"),
197: ("eksen: **lafız YOK · Rab YOK** · **esmâ عَلِيم *(alîm)* 7. sırada, ORTA konum, MÜHÜRSÜZ — "
 "ÖLÇÜM ARTEFAKTI**: عُلَمَٰٓؤُا۟ بَنِىٓ إِسْرَٰٓءِيلَ *(İsrâiloğulları bilginleri)*, çoğul ve "
 "gönderge İNSANLAR; ölçüt (a) ve (b) birden dışlıyor · **aktör: adlı إِسْرائِيل *(İsrâîl)* 9. "
 "sırada, rol mecrur** · edim soru, kip INTG 1 · NEG 1 · şahıs 3MS x3 · 3MP x1, iltifât 0 · n=9 "
 "mora=49 harf=37 (n z=-0,36), **fâsıla إِسْرَٰٓءِيلَ *(İsrâîl)* → ل — SÛRENİN DÖRDÜNCÜ VE SON "
 "KAFİYE KIRILMASI** (kafiye_kirik=1; yıldızın TEK kaynağı); i'râb ACC 1 · NOM 2 · GEN 1; bab I "
 "x2; zaman IMPF x2; **kök ikilemesi علم *(bilme; ilim)* x2 — يَعْلَمَهُۥ *(bilmesi)* ve "
 "عُلَمَٰٓؤُا۟ *(bilginler)***; dış düğüm 0 · **yıldız ★** · kökler كون *(olmak; mekân, yer)* · "
 "أيي *(âyet, işaret)* · علم *(bilme; ilim)* · بني *(oğul, evlat)* · bağ: **ADAY 612 TAMAMLANDI — "
 "SÛRENİN DÖRT KAFİYE KIRILMASININ DÖRDÜ DE AYNI ÖZEL ADLA** (26:17, 22, 59, 197: إِسْرَٰٓءِيلَ) "
 "(elle, L1, aday 751)"),
198: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim şart, kip COND 1 · şahıs 1P x2 · "
 "3MS x1, iltifât 0 · n=5 mora=28 harf=22 (n z=-0,79), fâsıla ٱلْأَعْجَمِينَ *(yabancılar, Arap "
 "olmayanlar)* → ن, N sınıfı; **i'râb GEN 1 · NOM 1**; bab II x1; zaman PERF 1; dış düğüm 0 · "
 "yıldız ★ yok · kökler نزل *(indirme)* · بعض *(bir kısım)* · عجم *(a'cemî, Arapça konuşmayan)* · "
 "bağ: **26:195 ile DİL KARŞITLIĞI** — orada لِسَانٍ عَرَبِىٍّ مُّبِينٍ *(apaçık Arap dili)*, "
 "burada ٱلْأَعْجَمِينَ *(yabancılar)*; **عرب *(Arapça; bedevî)* ve عجم *(a'cemî)* üç ayet arayla "
 "karşı karşıya; iki ayrı kök, bir karşıtlık** (elle, L1, aday 752)"),
199: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُؤْمِن *(mümin)* 6. sırada = fâsıla, MÜHÜRSÜZ — "
 "ARTEFAKT, sûrenin ON DÖRDÜNCÜ tokeni** · aktör yok · edim haber, kip NEG 1 · şahıs 3MS x3 · "
 "3MP x3, iltifât 0 · n=6 mora=31 harf=28 (n z=-0,68), fâsıla مُؤْمِنِينَ → ن, N sınıfı; **i'râb "
 "ACC 1**; bab I x2; zaman PERF x2; dış düğüm 0 · yıldız ★ yok · kökler قرأ *(okuma, Kur'ân)* · "
 "كون *(olmak; mekân, yer)* · أمن *(güven; iman)* · bağ: **قرأ *(okuma, Kur'ân)* — sûrede İLK ve "
 "TEK geçiş** (okunan 200 ayette); kök korpusta 88 geçişli ve dikey ölçümü ▸önce فرق *(ayırma, "
 "parçalara bölme)* x22,4 veriyor — 25:1'in ٱلْفُرْقَان *(Furkān)* kökü (elle, L1, aday 753)"),
200: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "1P x2 · 3MS x1, iltifât 0 · n=5 mora=29 harf=23 (n z=-0,79), fâsıla ٱلْمُجْرِمِينَ *(suçlular)* → "
 "ن, N sınıfı — **26:99'un fâsılasıyla AYNI KÖK** (orada ٱلْمُجْرِمُونَ merfû, burada mecrur); "
 "**i'râb GEN 2**; bab I x1; zaman PERF 1; **dış düğüm 1** · yıldız ★ yok · kökler سلك *(sokma, "
 "yola girme)* · قلب *(çevirme; kalp)* · جرم *(suç işleme)* · bağ: xref سلك *(soktu)* + قلب "
 "*(kalp)* + مجرم *(suçlu)* → **15:12**; **26:194 ile قلب *(kalp)* karşıtlığı** — orada vahiy "
 "elçinin kalbine İNİYOR (نَزَلَ … عَلَىٰ قَلْبِكَ), burada suçluların kalplerine SOKULUYOR "
 "(سَلَكْنَٰهُ فِى قُلُوبِ); **aynı kök, altı ayet arayla, iki ters yön** (elle, L1, aday 748)"),
}

M = {
191: ("**İkinci nakarat kümesi tamamlandı: 8/8** (26:9, 68, 104, 122, 140, 159, 175, 191). Ve "
 "**aday 744'ün tablosu tamam**: nakarat çifti Şuayb kıssasında da bütün. Sekiz mühürlü konumun "
 "sekizi de geçerli — sûre 25'te de mühür sinyali temiz çıkmıştı (aday 501/598). Beş kelime, hiç "
 "fiil yok; rab z=3,94 sekiz ayette de aynı, çünkü sekiz ayet de aynı."),
192: ("Sûrenin son bölütü açılıyor ve ilk cümlesi bir kaynak bildirimi: وَإِنَّهُۥ لَتَنزِيلُ رَبِّ "
 "ٱلْعَٰلَمِينَ *(o, âlemlerin Rabbinin indirmesidir)*. rab z=5,01 — n=4, tek Rab, oran 0,25; "
 "26:47 ve 26:98 ile aynı değer. **Ölçülebilir bir konum yeniliği: رَبّ ٱلْعَٰلَمِينَ terkibi "
 "sûrede yedinci kez ama İLK KEZ ne kıssada ne nakaratta** — 26:16, 23, 47, 77 kıssaların içinde, "
 "26:109/127/145/164/180 nakarat kümesinde, burada **anlatıcı sesinde**. Tek 3-gram iki ayete "
 "düşüyor (56:80, 69:43) ve ikisi de aynı bildirimi taşıyor."),
193: ("İndirmenin aracısı adlandırılıyor: نَزَلَ بِهِ ٱلرُّوحُ ٱلْأَمِينُ *(onu Rûhu'l-Emîn "
 "indirdi)*. **Ölçülebilir bir esmâ sınıfı sorunu:** أَمِين *(güvenilir)* burada esmâ **sayılmıyor** "
 "— ama bu sefer hüküm **tartışmalı**: gönderge bir MELEK, yani ne ilâhî ne insan. Sûrede aynı "
 "lemma beş kez elçi için kullanılmıştı (nakarat kümesi) ve orada da sayılmamıştı. **Aday "
 "682/709'un sınama kümesine üçüncü bir sınıf giriyor: melek göndergesi.** Ve نزل *(indirme)* "
 "bitişik ayette ikinci kez: 26:192'de masdar (تَنزِيل), burada fiil (نَزَلَ). روح *(ruh, "
 "rüzgâr)* korpusta 57 geçişli."),
194: ("İniş yeri bir organ adıyla veriliyor: عَلَىٰ قَلْبِكَ *(senin kalbine)*. Ölçülebilir bir "
 "çatı karşıtlığı: fâsıla ٱلْمُنذِرِينَ *(uyarıcılar)* — 26:173'ün fâsılası ٱلْمُنذَرِينَ "
 "*(uyarılanlar)* ile **aynı kök, ters çatı** (ism-i fâil / ism-i mef'ûl); yirmi bir ayet arayla. "
 "Ve قلب *(çevirme; kalp)* sûrede üç işlevde: 26:89 قَلْبٍ سَلِيمٍ *(temiz kalp)* kurtuluş şartı, "
 "burada vahyin **indiği** yer, 26:200'de vahyin **sokulduğu** yer. **SINIR: 'kalp' burada bir "
 "organ değil bir alma yeri; anatomik hiçbir şey söylenmiyor.** Sûrenin on birinci iltifâtı burada."),
195: ("Üç kelime, üçü de mecrur, fiil yok: بِلِسَانٍ عَرَبِىٍّ مُّبِينٍ *(apaçık Arap diliyle)*. "
 "**Ölçülebilir bir üçlü: لسن *(dil)* sûrede üçüncü kez ve üçüncü anlamıyla** — 26:13 Mûsâ'nın "
 "**yetersizliği** (dili çözülmez), 26:84 İbrâhîm'in istediği **nam** (doğruluk dili), burada "
 "**dil/lisan** (Arapça). 529 kümesine sûre-içi bir üçlü ve aday 714/724/738/743'ün 'iki anlam "
 "aynı sûrede' sınıfının **üç anlamlı** ilk örneği. Tek xref 16:103'e düşüyor ve terkip orada da "
 "aynı. Ve fâsıladaki مُبِين esmâ sayılmış: sûrenin **yedinci** artefaktı."),
196: ("Dört kelime, fiil yok: وَإِنَّهُۥ لَفِى زُبُرِ ٱلْأَوَّلِينَ *(o, öncekilerin kitaplarında "
 "da vardır)*. زبر *(kitap, sahifeler; zebûr)* korpusta 11 geçişli. **Ölçülebilir bir fâsıla "
 "yoğunluğu: ٱلْأَوَّلِينَ *(öncekiler)* sûrede beşinci kez ve beş ayrı bağlamda** — 26:26 atalar, "
 "26:76 atalar, 26:137 âdet, 26:184 nesiller, burada **kitaplar**. Aynı kelime, beş gönderge. "
 "Sûrenin on ikinci iltifâtı burada (2>3)."),
197: ("**Aday 612 tamamlandı: sûrenin dört kafiye kırılmasının DÖRDÜ DE aynı özel adla** — 26:17, "
 "26:22, 26:59 ve burada, hepsi `إِسْرَٰٓءِيلَ`. Yani kırılma tek bir adın ses yapısına bağlı ve "
 "sûrenin başka hiçbir yerinde kırılma yok. Yıldızın tek kaynağı bu kırılma. Ve kök ikilemesi "
 "علم *(bilme; ilim)* ×2: يَعْلَمَهُۥ *(bilmesi)* ve عُلَمَٰٓؤُا۟ *(bilginler)* — fiil ve "
 "ism-i fâil çoğulu. Fâsıladaki عَلِيم değil ama **ortadaki** عُلَمَٰٓؤُا۟ esmâ sayılmış; gönderge "
 "İsrâiloğullarının bilginleri, yani insanlar — çoğul + insan, **iki ölçüt birden dışlıyor**."),
198: ("Şart bir dil karşıtlığı kuruyor: وَلَوْ نَزَّلْنَٰهُ عَلَىٰ بَعْضِ ٱلْأَعْجَمِينَ *(onu "
 "yabancılardan birine indirseydik)*. **Ölçülebilir bir karşıtlık: 26:195'te عرب *(Arapça; "
 "bedevî)*, burada عجم *(a'cemî, Arapça konuşmayan)* — üç ayet arayla iki ayrı kök, bir "
 "karşıtlık.** Bu, aday 613/627/652/687'nin 'iki ayrı kök, aynı alan' deseninin **karşıt** hâli: "
 "orada iki kök aynı anlamı, burada iki kök karşıt anlamı taşıyor. عجم korpusta 6 geçişli. Ve "
 "نزل *(indirme)* bu bölütte üçüncü kez (26:192, 193, burada) — bab II."),
199: ("Şartın cevabı bir inkâr: مَا كَانُوا۟ بِهِۦ مُؤْمِنِينَ *(ona inanmazlardı)*. **Ölçülebilir "
 "bir ilk: قرأ *(okuma, Kur'ân)* kökü sûrede İLK ve TEK kez burada geçiyor** — okunan 200 ayette "
 "başka geçiş yok. Kök korpusta 88 geçişli ve dikey ölçümü ▸önce فرق *(ayırma, parçalara bölme)* "
 "×22,4 veriyor — **25:1'in ٱلْفُرْقَان *(Furkān)* kökü**; iki sûrenin adları korpusta komşu. Ve "
 "fâsıladaki مُؤْمِن sûrenin **on dördüncü** artefaktı."),
200: ("Bölüt bir sokma fiiliyle kapanıyor: كَذَٰلِكَ سَلَكْنَٰهُ فِى قُلُوبِ ٱلْمُجْرِمِينَ *(işte "
 "onu suçluların kalplerine böyle soktuk)*. **Ölçülebilir bir ters yön: 26:194'te vahiy elçinin "
 "kalbine İNİYOR (نَزَلَ … عَلَىٰ قَلْبِكَ), burada suçluların kalplerine SOKULUYOR (سَلَكْنَٰهُ "
 "فِى قُلُوبِ)** — aynı kök قلب *(çevirme; kalp)*, altı ayet arayla, iki ters yön ve iki ayrı "
 "fiil (نزل *(indirme)* / سلك *(sokma, yola girme)*). Tek xref 15:12'ye düşüyor ve terkip orada "
 "da aynı — donmuş kalıp adayı. Ve fâsıla ٱلْمُجْرِمِينَ 26:99'dan geri geliyor: orada merfû ve "
 "saptıran taraf, burada mecrur ve kalpleri anılan taraf."),
}

ATLAMA = {
 "_mercek_26_191_192": ("26:191 ve 26:192 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. 26:191 NAKARAT "
  "(ikinci kümenin sekizinci ve SON geçişi, rab z=3,94); 26:192 bir kaynak bildirimi (rab z=5,01, "
  "n=4). İkisinde de ne canlı, ne gök cismi, ne ölçü, ne süreç."),
 "_blok_notu_26_191_200": ("BLOK BİLANÇOSU: ★★★ 2 (26:191, 192) · ★★ 0 · ★ 1 (26:197) · 7 ayet "
  "yıldızsız. Kaynaklar: rab x2 · kafiye kırılması x1 — HİÇBİRİ İÇERİKTEN, hiçbirinde çıpa yok. "
  "**ADAY 612 TAMAMLANDI: sûrenin dört kafiye kırılmasının DÖRDÜ DE aynı özel adla** (26:17, 22, "
  "59, 197 — hepsi إِسْرَٰٓءِيلَ). **İKİNCİ NAKARAT KÜMESİ TAMAMLANDI (8/8) ve sekiz mühürlü "
  "konumun sekizi de GEÇERLİ.** ÇIPA NOTU: 26:194 ve 26:200 'kalp' anıyor ama organ olarak değil "
  "alma/sokma yeri olarak; anatomik hiçbir şey yok — 26:89'un قَلْبٍ سَلِيمٍ vakasıyla aynı sınıf "
  "ve orada da çıpa sayılmamıştı. SÛRE 26'NIN OKUNAN 200 AYETİNDE ★★★ 41 — **SÛRENİN TOPLAM ★★★ "
  "SAYISINA ULAŞILDI; kalan 27 ayette yeni ★★★ YOK** (defter sayımı 41)."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(191, 201):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 200/227.** Devam: 26:201'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-200 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1922
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(191, 201):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
