# -*- coding: utf-8 -*-
"""blok_26_201_210.py — sûre 26 on sekizinci blok (26:201-210). Mühlet ve şeytanlar bölütü."""
import json
DIK = json.load(open('blok_dikey_26_201_210.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
201: "Acıklı azabı görünceye kadar ona inanmazlar.",
202: "O, farkında olmadıkları bir sırada ansızın gelir.",
203: "Derler ki: Bize mühlet verilir mi?",
204: "Azabımızı acele mi istiyorlar?",
205: "Gördün mü: onları yıllarca yararlandırsak,",
206: "sonra kendilerine vaat edilen gelse,",
207: "yararlandırıldıkları şey onlara bir fayda sağlamaz.",
208: "Hiçbir şehri helâk etmedik ki uyarıcıları olmasın.",
209: "Hatırlatma olsun diye; ve biz zalim değiliz.",
210: "Onu şeytanlar indirmedi.",
}

O = {
201: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · şahıs "
 "3MP x4 · 3MS x1, iltifât 0 · n=7 mora=36 harf=31 (n z=-0,58), fâsıla ٱلْأَلِيمَ *(acıklı)* → م, "
 "N sınıfı; **i'râb ACC 2**; bab I x1 · IV x1; zaman IMPF x2; **dış düğüm 2** · yıldız ★ yok · "
 "kökler أمن *(güven; iman)* · رأي *(görme)* · عذب *(azap)* · ألم *(elem, acı)* · bağ: xref آمن "
 "*(iman etti)* + رأى *(gördü)* + عذاب *(azap)* → **10:88**; رأى + عذاب + أليم *(acıklı)* → "
 "**10:88 · 10:97**; **26:199 ile أمن *(güven; iman)* bitişik geçişi** — orada مَا كَانُوا۟ بِهِۦ "
 "مُؤْمِنِينَ *(ona inanmazlardı)* şartın cevabı, burada لَا يُؤْمِنُونَ بِهِۦ *(ona inanmazlar)* "
 "bir bildirimi; **aynı kök, aynı zamir (بِهِ), iki ayet arayla** (elle, L1, aday 754)"),
202: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · şahıs "
 "3MS x1 · 3MP x4, iltifât 0 · n=5 mora=27 harf=23 (n z=-0,79), fâsıla يَشْعُرُونَ *(farkına "
 "varıyorlar)* → ن, N sınıfı — **26:113'ün fâsılasıyla AYNI KÖK**; **i'râb ACC 1**; bab I x2; "
 "zaman IMPF x2; **dış düğüm 2** · yıldız ★ yok · kökler أتي *(gelme, getirme)* · بغت *(ansızın "
 "gelme)* · شعر *(şair; farkında olma)* · bağ: xref أتى *(geldi)* + بغتة *(ansızın)* + يشعر "
 "*(farkına varır)* → **29:53 · 43:66**; **26:113 ile شعر *(şair; farkında olma)* İKİNCİ geçişi ve "
 "YİNE 'farkında olma' anlamında** — sûrenin adı ٱلشُّعَرَآء *(şairler)* 26:224'te gelecek; "
 "**dikey ölçüm şعر için ▸önce بغت *(ansızın gelme)* x85,3 veriyor, yani BU AYETİN komşusu** "
 "(elle, L1, aday 755)"),
203: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · şahıs "
 "3MP x2 · 1P x1, iltifât 0 · n=4 mora=22 harf=19 (n z=-0,89), fâsıla مُنظَرُونَ *(mühlet "
 "verilenler)* → ن, N sınıfı; **i'râb NOM 1**; bab I x1; zaman IMPF 1; dış düğüm 0 · yıldız ★ yok · "
 "kökler قول *(söz söyleme)* · نظر *(bakma; mühlet verme)* · bağ: **25:22 ile نظر *(bakma; mühlet "
 "verme)* karşılaştırması** — orada 25:22'de melek görme bağlamıydı; burada 'mühlet verme' anlamı; "
 "**kök korpusta 129 geçişli ve iki anlamlı — 529 sınıfı**; ayrıca 26:33'te لِلنَّٰظِرِينَ "
 "*(bakanlar için)* 'bakma' anlamındaydı — **aynı sûrede iki anlam** (aday 714/724/738/743/749 "
 "sınıfı, ALTINCI vaka) (elle, L1, aday 756)"),
204: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · şahıs 1P x1 · "
 "3MP x2, iltifât 0 · **n=2 mora=22 harf=17 — SÛRENİN EN KISA AYETLERİNDEN** (n z=-1,11; 26:60 ve "
 "26:134 ile aynı değer), fâsıla يَسْتَعْجِلُونَ *(acele istiyorlar)* → ن, N sınıfı; **i'râb "
 "GEN 1**; **bab X x1**; zaman IMPF 1; dış düğüm 0 · yıldız ★ yok · kökler عذب *(azap)* · عجل "
 "*(acele)* · bağ: **26:203 ile bitişik çift ve TERS YÖN** — orada هَلْ نَحْنُ مُنظَرُونَ *(bize "
 "mühlet verilir mi)* GECİKME isteği, burada أَفَبِعَذَابِنَا يَسْتَعْجِلُونَ *(azabımızı acele mi "
 "istiyorlar)* ACELE suçlaması; **iki ayet, iki zaman yönü** (elle, L1, aday 757)"),
205: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru + şart, kip INTG 1 · "
 "COND 1 · şahıs 2MS x2 · 1P x2 · 3MP x1, iltifât 0 · n=4 mora=24 harf=18 (n z=-0,89), fâsıla "
 "سِنِينَ *(yıllar)* → ن, N sınıfı; **i'râb ACC 1**; bab I x1 · II x1; zaman PERF x2; dış düğüm "
 "0 · yıldız ★ yok · kökler رأي *(görme)* · متع *(yararlandırma, meta)* · سنو *(yıl)* · bağ: "
 "**26:205-207 üçlüsü tek bir şart-cevap yapısı** — şart 26:205-206, cevap 26:207; **متع "
 "*(yararlandırma, meta)* iki kez (26:205 ve 26:207)**; **سنو *(yıl)* — okumada AÇIK SÜRE BİRİMİ "
 "içeren ilk ayetlerden; ama SAYI YOK, yalnız çoğul (سِنِينَ *(yıllar)*)** (elle, L1, aday 758)"),
206: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3MS x1 · 3MP x5, iltifât 0 · n=5 mora=31 harf=21 (n z=-0,79), fâsıla يُوعَدُونَ *(vaat "
 "ediliyorlar)* → ن, N sınıfı; **i'râb YOK**; bab I x3; zaman PERF x2 · IMPF 1; **edilgen 1 — "
 "يُوعَدُونَ *(vaat ediliyorlar)*; üç fiilden biri edilgen, oran 0,33**, pas z=1,57: **yıldızın "
 "TEK kaynağı**; dış düğüm 0 · **yıldız ★** · kökler جيأ *(gelme)* · كون *(olmak; mekân, yer)* · "
 "وعد *(vaat)* · bağ: **26:205 ile şart zincirinin ikinci halkası**; **وعد *(vaat)* korpusta 151 "
 "geçişli ve sûrede İLK geçiş** (elle, L1, aday 758)"),
207: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · şahıs "
 "3MS x1 · 3MP x5, iltifât 0 · n=6 mora=34 harf=24 (n z=-0,68), fâsıla يُمَتَّعُونَ "
 "*(yararlandırılıyorlar)* → ن, N sınıfı; **i'râb YOK**; bab I x2 · II x1; zaman PERF x2 · IMPF 1; "
 "**edilgen 1 — يُمَتَّعُونَ; üç fiilden biri edilgen, oran 0,33**, pas z=1,57: **yıldızın TEK "
 "kaynağı**; dış düğüm 0 · **yıldız ★** · kökler غني *(zenginlik; müstağnî olma)* · كون *(olmak; "
 "mekân, yer)* · متع *(yararlandırma, meta)* · bağ: **26:205 ile متع *(yararlandırma, meta)* kök "
 "tekrarı — şart ve cevap aynı kökle**: مَّتَّعْنَٰهُمْ *(onları yararlandırsak)* ve مَا كَانُوا۟ "
 "يُمَتَّعُونَ *(yararlandırıldıkları şey)*; **üç ayetlik yapının iki ucunda aynı kök, biri etken "
 "biri edilgen** (elle, L1, aday 758)"),
208: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · RES 1 · "
 "şahıs 1P x2 · 3FS x1, iltifât 0 · n=7 mora=38 harf=27 (n z=-0,58), fâsıla مُنذِرُونَ "
 "*(uyarıcılar)* → ن, N sınıfı — **26:194'ün fâsılasıyla AYNI LEMMA** (orada mecrur "
 "ٱلْمُنذِرِينَ, burada merfû); **i'râb GEN 1 · NOM 1**; bab IV x1; zaman PERF 1; **biçim HASR**; "
 "dış düğüm 0 · yıldız ★ yok · kökler هلك *(helâk)* · قري *(şehir, kasaba (karye))* · نذر *(uyarma; "
 "adak)* · bağ: **26:139 ile هلك *(helâk)* ikinci geçişi** — orada فَأَهْلَكْنَٰهُمْ *(onları "
 "helâk ettik)* Hûd kavmi için, burada bir GENEL KURAL bildirimi (وَمَآ أَهْلَكْنَا مِن قَرْيَةٍ "
 "إِلَّا لَهَا مُنذِرُونَ *(hiçbir şehri helâk etmedik ki uyarıcıları olmasın)*); **aynı kök, "
 "olaydan kurala** (elle, L1, aday 759)"),
209: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · **şahıs "
 "1P x2 — ayette başka şahıs yok**, iltifât 0 · n=4 mora=23 harf=15 (n z=-0,89), fâsıla "
 "ظَٰلِمِينَ *(zalimler)* → ن, N sınıfı; **i'râb NOM 1 · ACC 1**; bab I x1; zaman PERF 1; dış "
 "düğüm 0 · yıldız ★ yok · kökler ذكر *(anma, zikir)* · كون *(olmak; mekân, yer)* · ظلم *(zulüm, "
 "karanlık)* · bağ: **26:165 ile ذكر *(anma, zikir)* İKİNCİ geçişi ve BASKIN anlamında** — orada "
 "ٱلذُّكْرَان *(erkekler)* azınlık anlamıydı (aday 723), burada ذِكْرَىٰ *(hatırlatma)* korpus "
 "baskın anlamı; **aynı sûrede iki anlam ve dikey satırı İKİSİNİ DE gösteriyordu** (aday 711/723 "
 "sinyali burada ÇALIŞIYOR) (elle, L1, aday 760)"),
210: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı شَيْطان *(şeytan)* 4. sırada, rol "
 "FAİL, sınıf GAYB — sûrede ikinci gayb aktörü** (birincisi 26:95 إِبْلِيس *(İblîs)*) · edim "
 "haber, kip NEG 1 · şahıs 3FS x1 · 3MS x1, **iltifât 1 — yön 1>3; sûrenin on üçüncü iltifâtı** · "
 "n=4 mora=24 harf=17 (n z=-0,89), fâsıla ٱلشَّيَٰطِينُ *(şeytanlar)* → ن, N sınıfı; **i'râb "
 "NOM 1**; **bab V x1**; zaman PERF 1; dış düğüm 0 · yıldız ★ yok · kökler نزل *(inme, indirme)* · "
 "شطن *(şeytan)* · bağ: **26:192-193 ile نزل *(inme, indirme)* karşıtlığı** — orada تَنزِيلُ رَبِّ "
 "ٱلْعَٰلَمِينَ *(âlemlerin Rabbinin indirmesi)* ve نَزَلَ بِهِ ٱلرُّوحُ ٱلْأَمِينُ *(Rûhu'l-Emîn "
 "indirdi)*, burada وَمَا تَنَزَّلَتْ بِهِ ٱلشَّيَٰطِينُ *(onu şeytanlar indirmedi)*; **aynı kök "
 "üç biçimde (masdar, bab I, bab V) ve üçüncüsü OLUMSUZ — kaynak bildiriminin karşıtı** "
 "(elle, L1, aday 761)"),
}

M = {
201: ("İnkâr bir koşula bağlanıyor: حَتَّىٰ يَرَوُا۟ ٱلْعَذَابَ ٱلْأَلِيمَ *(acıklı azabı "
 "görünceye kadar)*. Ölçülebilir bir bitişiklik: 26:199'da مَا كَانُوا۟ بِهِۦ مُؤْمِنِينَ *(ona "
 "inanmazlardı)* bir şartın cevabıydı, burada لَا يُؤْمِنُونَ بِهِۦ *(ona inanmazlar)* bir "
 "bildirim — **aynı kök, aynı zamir (بِهِ), iki ayet arayla, farazîden gerçeğe**. İki 3-gram da "
 "10:88 ve 10:97'ye düşüyor. رأي *(görme)* korpusta 328 geçişli ve dikey ölçümü ▸önce direk x16,4 "
 "veriyor — kök korpusta çok geniş bir yatağa yayılmış."),
202: ("Geliş biçimi bir zarf ve bir olumsuzlamayla veriliyor: بَغْتَةً وَهُمْ لَا يَشْعُرُونَ "
 "*(ansızın, farkında olmadıkları bir sırada)*. **Ölçülebilir bir tekrar: شعر *(şair; farkında "
 "olma)* sûrede ikinci kez ve yine 'farkında olma' anlamında** (birincisi 26:113); sûrenin adı "
 "ٱلشُّعَرَآء *(şairler)* 26:224'te gelecek ve orada üçüncü anlam çıkacak. Ve **dikey ölçüm şعر "
 "için ▸önce بغت *(ansızın gelme)* x85,3 veriyor — tam bu ayetin komşusu**; yani 'ansızın gelme + "
 "farkına varmama' çifti korpusta sabit ve iki 3-gram da 29:53, 43:66'ya düşüyor."),
203: ("Soru bir mühlet isteği: هَلْ نَحْنُ مُنظَرُونَ *(bize mühlet verilir mi)*. **Ölçülebilir "
 "bir anlam ayrımı: نظر *(bakma; mühlet verme)* korpusta 129 geçişli ve iki anlamlı; burada "
 "'mühlet verme', 26:33'te لِلنَّٰظِرِينَ *(bakanlar için)* 'bakma' anlamındaydı** — aynı sûrede "
 "iki anlam ve 529 kümesine sûre 26'nın ALTINCI sûre-içi vakası (صلح, خلق, جبل, ظلل, لسن, نظر). "
 "Dikey ölçüm bu kök için ▸sonra مهل *(mühlet)* değil, göz-bakış komşulukları veriyor — yani "
 "**dikey sinyal burada da baskın anlamı gösteriyor, ikincisini değil** (aday 749 ile aynı)."),
204: ("**İki kelime — sûrenin en kısa ayetlerinden** (26:60 ve 26:134 ile aynı n z=-1,11). "
 "أَفَبِعَذَابِنَا يَسْتَعْجِلُونَ *(azabımızı acele mi istiyorlar)*. Ölçülebilir bir ters yön: "
 "26:203'te مُنظَرُونَ *(mühlet verilenler)* bir **gecikme** isteğiydi, burada يَسْتَعْجِلُونَ "
 "bir **acele** suçlaması — bitişik iki ayet, iki zaman yönü. عجل *(acele)* bab X ve korpusta 47 "
 "geçişli; 25:15 ve 25:32'de de vardı. Ve iki kelimenin ikisi de kök taşıyor: ayet tamamen isim "
 "ve fiilden kurulu, edat yok."),
205: ("Şart üç ayetlik bir yapının ilk halkası: أَفَرَءَيْتَ إِن مَّتَّعْنَٰهُمْ سِنِينَ *(gördün "
 "mü: onları yıllarca yararlandırsak)*. **Ölçülebilir bir süre birimi: سِنِينَ *(yıllar)* — "
 "okumada açık bir süre birimi içeren ilk ayetlerden. AMA SAYI YOK, yalnız çoğul**; ne kaç yıl ne "
 "hangi ölçü. سنو *(yıl)* korpusta 20 geçişli ve dikey ölçümü ▸önce عدد *(sayı)* komşuluğu "
 "vermiyor — yani korpusta 'yıl' çoğunlukla sayısız geçiyor. **SINIR: bu bir süre ADI, ölçü "
 "değil; çıpa sayılmadı.**"),
206: ("Şartın ikinci halkası ve tek fiili edilgen: مَّا كَانُوا۟ يُوعَدُونَ *(kendilerine vaat "
 "edilen)*; üç fiilden biri edilgen, oran 0,33 → pas z=1,57, yıldızın tek kaynağı. **وعد *(vaat)* "
 "korpusta 151 geçişli ama sûrede İLK geçiş** — 206 ayette başka yerde yok. Dikey ölçümü ▸önce "
 "خلف *(ardıl; sözden dönme)* komşuluğu veriyor. Ve ayet i'râb etiketi almıyor: dördüncü i'râbsız "
 "ayet kümesi (26:72, 73, 75, 92, 96, 132, burada ve 26:207)."),
207: ("Cevap bir fayda reddi ve **kök tekrarı üç ayetlik yapının iki ucunda**: 26:205'te "
 "مَّتَّعْنَٰهُمْ *(onları yararlandırsak)* etken, burada مَا كَانُوا۟ يُمَتَّعُونَ "
 "*(yararlandırıldıkları şey)* edilgen — متع *(yararlandırma, meta)* aynı kök, iki çatı, şart ve "
 "cevap. Yıldızın tek kaynağı yine edilgenlik (pas z=1,57). غني *(zenginlik; müstağnî olma)* "
 "korpusta 73 geçişli ve burada 'fayda sağlama' anlamında — kök korpusta ağırlıkla 'zenginlik' ve "
 "'müstağnî olma' anlamlarında (529 sınıfı)."),
208: ("Bir genel kural bildiriliyor ve HASR ile: وَمَآ أَهْلَكْنَا مِن قَرْيَةٍ إِلَّا لَهَا "
 "مُنذِرُونَ *(hiçbir şehri helâk etmedik ki uyarıcıları olmasın)*. Ölçülebilir bir düzey geçişi: "
 "هلك *(helâk)* 26:139'da فَأَهْلَكْنَٰهُمْ *(onları helâk ettik)* bir OLAYDI (Hûd kavmi), burada "
 "bir KURAL. Ve fâsıla مُنذِرُونَ *(uyarıcılar)* 26:194'ün ٱلْمُنذِرِينَ'iyle **aynı lemma, farklı "
 "i'râb** — orada elçinin olacağı şey, burada her şehrin sahip olduğu şey. قري *(şehir, kasaba "
 "(karye))* korpusta 57 geçişli."),
209: ("Kuralın gerekçesi iki parçalı: ذِكْرَىٰ *(hatırlatma)* ve وَمَا كُنَّا ظَٰلِمِينَ *(biz "
 "zalim değiliz)*. **Ölçülebilir bir 529 doğrulaması: ذكر *(anma, zikir)* sûrede ikinci kez ve bu "
 "kez KORPUS BASKIN anlamında** — 26:165'te ٱلذُّكْرَان *(erkekler)* azınlık anlamıydı. Ve orada "
 "dikey satırı **iki anlamı da** göstermişti (▸sonra أنث *(dişi)* x13,4 ve ▸önce zikir "
 "komşulukları) — **yani 711/723'ün sinyali bu kökte ÇALIŞIYOR**, oysa 26:195'in لسن *(dil)* "
 "vakasında çalışmamıştı (aday 749). İki vaka birlikte sinyalin koşullu olduğunu gösteriyor."),
210: ("Son bölüt açılıyor ve bir kaynak reddi: وَمَا تَنَزَّلَتْ بِهِ ٱلشَّيَٰطِينُ *(onu şeytanlar "
 "indirmedi)*. **Ölçülebilir bir kök karşıtlığı: نزل *(inme, indirme)* sûrede üç biçimde ve "
 "üçüncüsü olumsuz** — 26:192 تَنزِيل masdar (kaynak: âlemlerin Rabbi), 26:193 نَزَلَ bab I "
 "(aracı: Rûhu'l-Emîn), burada تَنَزَّلَتْ bab V ve **olumsuz** (reddedilen: şeytanlar). Üç ayet "
 "aynı kökle bir kaynak zinciri kuruyor ve sonuncusu onu kapatıyor. Ve شَيْطان *(şeytan)* aktör "
 "tablosuna GAYB sınıfıyla giriyor — sûrede ikinci gayb aktörü (birincisi 26:95 إِبْلِيس "
 "*(İblîs)*). Sûrenin on üçüncü iltifâtı burada."),
}

ATLAMA = {
 "_blok_notu_26_201_210": ("BLOK BİLANÇOSU: ★★★ 0 · ★★ 0 · ★ 2 (26:206, 207) · 8 ayet yıldızsız — "
  "**OKUMADA ★★★ ÇIKMAYAN İLK ON AYETLİK BLOK**. İki ★ ayetin ikisinde de kaynak edilgenlik oranı "
  "(pas z=1,57) ve ikisi de aynı üç ayetlik şart-cevap yapısının içinde. ÇIPA NOTU: 26:205'te "
  "سِنِينَ *(yıllar)* — okumada açık bir SÜRE BİRİMİ içeren ilk ayetlerden; **ama SAYI YOK, yalnız "
  "çoğul; ne kaç yıl ne hangi ölçü. Bu bir süre ADI, ölçü değil — 26:182'nin قِسْطَاس *(kıstas)* "
  "vakasıyla aynı sınıf ve orada da çıpa sayılmamıştı. ÇIPA SAYILMADI.** SÛRE 26'NIN OKUNAN 210 "
  "AYETİNDE ★★★ 41 — sûrenin toplamı; kalan 17 ayette yeni ★★★ yok."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(201, 211):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 210/227.** Devam: 26:211'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-210 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1932
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(201, 211):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
