# -*- coding: utf-8 -*-
"""blok_25_71_77.py — sûre 25 son blok (25:71-77) + SÛRE KAPANIŞ PROFİLİ."""
import json
DIK = json.load(open('blok_dikey_25_61_77.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
71: "Kim tövbe eder ve sâlih amel işlerse, o gerçekten Allah'a tam bir dönüşle döner.",
72: "Ve yalana şahitlik etmeyen, boş sözle karşılaştıklarında onurluca geçip gidenlerdir.",
73: "Ve Rablerinin âyetleri hatırlatıldığında onlara karşı sağır ve kör kesilip kapanmayanlardır.",
74: "Ve derler ki: Rabbimiz, eşlerimizden ve zürriyetimizden bize göz aydınlığı bağışla ve bizi sakınanlara önder kıl.",
75: "İşte onlar, sabretmelerine karşılık yüksek makamla ödüllendirilirler; orada esenlik dileği ve selâmla karşılanırlar.",
76: "Orada ebedî kalıcılar olarak. Ne güzel bir karargâh, ne güzel bir konak!",
77: "De ki: Duanız olmasa Rabbim size ne diye değer versin? Siz yalanladınız; artık bu, yakanızı bırakmayacak.",
}

OLCUM = {
71: ("eksen: **ALLAH LAFZI 8. sırada — SÛRENİN SEKİZİNCİ VE SON LAFZI** (allah z=1,69: **yıldızın "
 "TEK kaynağı**) · Rab yok · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs 3MS x4, "
 "iltifât 0 · n=9 mora=45 harf=37 (n z=-0,36), fâsıla مَتَابا *(dönüş, tövbe)* → ا, A sınıfı, ACC; "
 "i'râb ACC 3 · GEN 1; bab I x3; zaman PERF x2 · IMPF x1; **kök ikilemesi توب *(tövbe, dönüş)* x3 — "
 "SÛREDE BİR AYETTE AYNI KÖĞÜN ÜÇ KEZ GEÇTİĞİ TEK YER**: تَابَ *(tövbe etti)* mâzi, يَتُوبُ "
 "*(döner)* muzâri, مَتَابا *(bir dönüşle)* mef'ûl-i mutlak; simetri [3,1,5,1]; dış düğüm 0 · "
 "**yıldız ★** · kökler توب *(tövbe, dönüş)* · عمل *(iş, amel)* · صلح *(salâh, iyilik)* · أله "
 "*(ilâh; lafza-i celâl)* · bağ: **25:70 ile bitişik çift** — orada istisna üç fiille kuruluyordu "
 "(tövbe + iman + amel), burada iki fiile iniyor (tövbe + amel) ve tövbe fiili ÜÇ KEZ tekrarlanıyor "
 "(elle, L1, aday 591)"),
72: ("eksen: **lafız YOK · Rab YOK** · **esmâ كَرِيم *(kerîm, onurlu)* 9. sırada = fâsıla, MÜHÜRSÜZ — "
 "ÖLÇÜM ARTEFAKTI (aday 546/555/578)**: gönderge KULLAR (مَرُّوا۟ كِرَاما *(onurluca geçip "
 "giderler)*), ilâhî değil; ölçüt (a) dışlıyor · aktör yok · edim haber, kip NEG 1 · şahıs 3MP x6, "
 "iltifât 0 · n=9 mora=55 harf=45 (n z=-0,36), fâsıla كِرَاما *(onurlu)* → ا, A sınıfı, ACC; i'râb "
 "ACC 2 · GEN 1; bab I x3; zaman IMPF x1 · PERF x2; **kök ikilemesi مرر *(geçip gitme)* x2 — şart "
 "ve cevabı aynı fiille: وَإِذَا مَرُّوا۟ … مَرُّوا۟ *(geçtiklerinde … geçerler)***; dış düğüm 0 · "
 "yıldız ★ yok · kökler شهد *(şahitlik)* · زور *(yalan, uydurma)* · مرر *(geçip gitme)* · لغو "
 "*(boş söz, lağv)* · كرم *(kerem, onur)* · bağ: **25:4 ile زور *(yalan, uydurma)* İKİNCİ VE SON "
 "geçişi — kök korpusta ALTI geçişli, ikisi bu sûrede**; orada itirazcıların getirdiği yalan, "
 "burada kulların şahitlik etmediği yalan (elle, L1, aday 592)"),
73: ("eksen: **lafız YOK · رَبّ *(Rab)* 5. sırada — sûrenin on ikinci Rab'bi** (rab z=1,81) · esmâ "
 "yok · aktör yok · edim haber, kip NEG 1 · şahıs 3MP x5 · 3FS x1, iltifât 0 · n=10 mora=59 harf=49 "
 "(n z=-0,26), fâsıla وَعُمْيَانا *(körler)* → ا, A sınıfı, ACC; i'râb GEN 2 · ACC 2; bab I x1 · "
 "II x1; zaman PERF x1 · IMPF x1; **edilgen 1 — ذُكِّرُوا۟ *(hatırlatıldı)***, **pas z=2,52** (iki "
 "fiilden biri edilgen, oran 0,50); **yıldız ★★ — İKİ KAYNAKLI: rab z=1,81 VE pas z=2,52; sûrede "
 "yıldızı iki kaynaktan alan TEK ayet** · **dış düğüm 2** · kökler ذكر *(anma, zikir)* · أيي *(âyet, "
 "işaret)* · ربب *(rab, terbiye etme)* · خرر *(yıkılıp düşme, kapanma)* · صمم *(sağırlık)* · عمي "
 "*(körlük)* · bağ: xref ذكّر *(hatırlatıldı)* + آية *(âyet)* + ربّ *(Rab)* → **18:57 · 32:22**; "
 "**25:18, 25:29 ve 25:62 ile ذكر *(anma, zikir)* dördüncü geçişi** — 25:18'de unutuldu, 25:29'da "
 "ondan saptırıldı, 25:62'de amaç, burada hatırlatılıyor (elle, L1, aday 593)"),
74: ("eksen: **lafız YOK · رَبّ *(Rab)* 3. sırada — sûrenin on üçüncü ve son Rab'bi** (rab z=1,32) · "
 "esmâ yok · aktör yok · edim emir, kip IMPV 2 · **şahıs 1P x5 · 2MS x2 · 3MP x2**, iltifât 0 · "
 "n=13 mora=82 harf=63 (n z=0,06), fâsıla إِمَاما *(önder, imam)* → ا, A sınıfı, ACC; **i'râb GEN 4 · "
 "ACC 3**; bab I x3; zaman IMPF x1 · IMPV 2; **açık sayı sözcüğü yok ama zوج *(eş, çift)* ikilik "
 "taşıyor**; dış düğüm 1 · yıldız ★ yok · kökler قول *(söz söyleme)* · ربب *(rab, terbiye etme)* · "
 "وهب *(bağışlama, hibe)* · زوج *(eş, çift)* · ذرر *(zürriyet, soy; zerre)* · قرر *(karar kılma, "
 "yerleşme)* · عين *(göz; pınar)* · جعل *(kılma, var etme)* · وقي *(sakınma, koruma)* · أمم *(anne; "
 "ümmet; önder)* · bağ: xref قال *(dedi)* + ربّ *(Rab)* + وهب *(bağışla)* → **3:38**; **25:65 ile "
 "dua çifti** — orada dua bir SAVMA isteğiydi (ٱصْرِفْ *(çevir)*), burada bir VERME isteği "
 "(هَبْ *(bağışla)*) (elle, L1, aday 594)"),
75: ("eksen: **lafız YOK · Rab YOK** · **esmâ سَلام *(esenlik)* 9. sırada = fâsıla, MÜHÜRSÜZ — "
 "ÖLÇÜM ARTEFAKTI**: تَحِيَّةً وَسَلَٰما *(esenlik dileği ve selâm)*, yani KARŞILANDIKLARI SÖZ; "
 "25:63'teki سَلام artefaktıyla aynı sınıf · aktör yok · edim haber, kip işareti yok · şahıs 3MP x6 · "
 "3FS x1, iltifât 0 · n=9 mora=54 harf=46 (n z=-0,36), fâsıla وَسَلَٰما *(selâm)* → ا, A sınıfı, "
 "ACC — **25:63'ün fâsılasıyla aynı kelime**; **i'râb ACC 3**; bab I x2 · II x1; zaman IMPF x2 · "
 "PERF x1; **edilgen 2 — يُجْزَوْنَ *(ödüllendirilirler)* ve يُلَقَّوْنَ *(karşılanırlar)*; üç "
 "fiilden ikisi edilgen, oran 0,67**, pas z=3,48: **yıldızın TEK kaynağı**; dış düğüm 0 · **yıldız "
 "★★★ — SÛRENİN BEŞİNCİ ÜÇ YILDIZLISI** · kökler جزي *(karşılık verme)* · غرف *(yüksek oda, gurfe)* · "
 "صبر *(sabır)* · لقي *(karşılaşma, kavuşma; atma)* · حيي *(diri olma, hayat; tahiyye)* · سلم "
 "*(selâmet, esenlik)* · bağ: **25:15 ile جزي *(karşılık verme)* ikinci geçişi** — orada cennet "
 "جَزَآء *(karşılık)* ve مَصِير *(varış yeri)* idi, burada ٱلْغُرْفَة *(yüksek makam)* "
 "(elle, L1, aday 595)"),
76: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3FS x2, iltifât 0 · n=5 mora=35 harf=28 (n z=-0,79), fâsıla وَمُقَاما *(konak)* → ا, A sınıfı, "
 "ACC — **25:66'nın fâsılasıyla AYNI KELİME**; **i'râb ACC 3**; bab I x1; zaman PERF x1; dış düğüm "
 "0 · yıldız ★ yok · kökler خلد *(ebedî kalma)* · حسن *(güzellik, iyilik)* · قرر *(karar kılma, "
 "yerleşme)* · قوم *(kalkma; kavim; kıyamet)* · bağ: **25:66 ile NEREDEYSE TAM İKİZ — TEK FARK "
 "FİİL**: سَآءَتْ مُسْتَقَرًّۭا وَمُقَاما *(ne kötü bir karargâh ve konak)* / حَسُنَتْ مُسْتَقَرًّۭا "
 "وَمُقَاما *(ne güzel bir karargâh ve konak)*; **defter.json esit alanı İKİSİNDE DE BOŞ** — ölçü "
 "tanımı eksiği (elle, L1, aday 596)"),
77: ("eksen: **lafız YOK · رَبّ *(Rab)* 5. sırada — SÛRENİN ON DÖRDÜNCÜ VE SON Rab'bi** (rab z=1,45) · "
 "esmâ yok · aktör yok · edim emir + şart, kip IMPV 1 · NEG 1 · COND 1 · CERT 1 · FUT 1 — **beş "
 "kip işareti, sûrede en yoğun** · şahıs 2MP x4 · 3MS x2 · 2MS x1 · 1S x1, iltifât 0 · n=12 mora=56 "
 "harf=49 (n z=-0,04), fâsıla لِزَاما *(ayrılmaz, yaka bırakmaz)* → ا, A sınıfı, ACC — **SÛRENİN "
 "SON FÂSILASI**; i'râb NOM 2 · ACC 1; bab I x3 · II x1; zaman IMPV 1 · IMPF x2 · PERF x1; "
 "**HAPAKS: عبأ *(değer verme, aldırma)* — korpusta TEK geçiş** (hapaks z=3,38: **yıldızın TEK "
 "kaynağı**); simetri [3,2,6,1]; dış düğüm 0 · **yıldız ★★★ — SÛRENİN ALTINCI VE SON ÜÇ "
 "YILDIZLISI** · kökler قول *(söz söyleme)* · عبأ *(değer verme, aldırma)* · ربب *(rab, terbiye "
 "etme)* · دعو *(çağırma, dua)* · كذب *(yalan; yalanlama)* · كون *(olmak; mekân, yer)* · لزم "
 "*(ayrılmama, lüzum)* · bağ: **25:11 ve 25:19 ile كذب *(yalan; yalanlama)* DÖRDÜNCÜ VE SON "
 "geçişi — ADAY 544 KAPANIYOR**: 25:11'de fâil onlar / mef'ûl o saat, 25:19'da fâil tapılanlar / "
 "mef'ûl muhatap, burada fâil MUHATAP (كَذَّبْتُمْ *(siz yalanladınız)*) — üç geçişte üç ayrı fâil "
 "(elle, L1, aday 597)"),
}

MERCEK = {
71: ("Sûrenin sekizinci ve son Allah lafzı burada ve yıldızın tek kaynağı bu (allah z=1,69). "
 "Ölçülebilir bir yoğunluk: توب *(tövbe, dönüş)* kökü ÜÇ kez — sûrede bir ayette aynı kökün üç kez "
 "geçtiği tek yer. Üç biçim üç zamanı kapsıyor: تَابَ *(tövbe etti)* mâzi (gerçekleşmiş), "
 "يَتُوبُ *(döner)* muzâri (süregelen), مَتَابا *(bir dönüşle)* mef'ûl-i mutlak (pekiştirme). Bu, "
 "sûrenin dokuzuncu fiil + mef'ûl-i mutlak örneği ve bab I. توب korpusta 87 geçişli ve dikey ölçümü "
 "▸önce صلح *(salâh, iyilik)* x13,5 · ▸sonra صلح x15,7 veriyor — 'tövbe + sâlih amel' korpusta sabit "
 "bir eşleşme, bu ayete özgü değil."),
72: ("İki olumsuz nitelik ve ikisi de söz alanında: يَشْهَدُونَ ٱلزُّورَ *(yalana şahitlik)* ve "
 "ٱللَّغْو *(boş söz)*. زور *(yalan, uydurma)* korpusta ALTI geçişli ve ikisi bu sûrede — 25:4'te "
 "itirazcıların getirdiği yalan (فَقَدْ جَآءُو ظُلْما وَزُورا *(bir zulüm ve bir yalanla geldiler)*), "
 "burada kulların şahitlik ETMEDİĞİ yalan; aynı kök, ters özne. Ölçülebilir bir kök ikilemesi: "
 "مرر *(geçip gitme)* iki kez ve şart ile cevabı aynı fiille — وَإِذَا مَرُّوا۟ بِٱللَّغْوِ "
 "مَرُّوا۟ كِرَاما *(boş sözle karşılaştıklarında onurluca geçip giderler)*; fiil değişmiyor, "
 "yalnız hâl ekleniyor. لغو *(boş söz, lağv)* korpusta 11 geçişli."),
73: ("Sûrede yıldızı İKİ KAYNAKTAN alan tek ayet: rab z=1,81 ve pas z=2,52. Ötekilerin hepsinde tek "
 "kaynak vardı. Ölçülebilir bir olumsuzlama: لَمْ يَخِرُّوا۟ عَلَيْهَا صُمًّۭا وَعُمْيَانا *(sağır "
 "ve kör kesilip kapanmazlar)* — olumsuzlanan şey düşme fiili DEĞİL, düşmenin HÂLİ; yani kapanma "
 "olumlu, sağır-kör kapanma olumsuz. خرر *(yıkılıp düşme, kapanma)* korpusta 12 geçişli ve dikey "
 "ölçümü ▸sonra secde bağlamı veriyor. İki hâl nekre çoğul ve ikisi de duyu yitimi: صمم *(sağırlık)* "
 "ve عمي *(körlük)*; ikisi korpusta zaten bitişik. Ve ذكر *(anma, zikir)* sûrede dördüncü kez: "
 "unutuldu (25:18), ondan saptırıldı (25:29), amaç oldu (25:62), burada hatırlatılıyor."),
74: ("Sûrenin on dördüncü ve son رَبّ *(Rab)*'bi burada ve nida hâlinde — 25:30'un يَٰرَبِّ "
 "*(Rabbim)*'inden sonra ikinci doğrudan çağrı, ama bu kez çoğul: رَبَّنَا *(Rabbimiz)*. "
 "Ölçülebilir bir istek yapısı: iki emir (هَبْ *(bağışla)* ve وَٱجْعَلْنَا *(bizi kıl)*) ve ikisi "
 "de 1P'ye. İstenen şey bir DEYİM: قُرَّةَ أَعْيُنٍ *(göz aydınlığı)*, قرر *(karar kılma, "
 "yerleşme)* + عين *(göz; pınar)*; dikey ölçüm قرر ▸önce göz x21,6 · ▸sonra göz x34,6 veriyor — "
 "çift korpusta sabit, donmuş kalıp adayı (aday 437). Ve قرر kökü sûrede üçüncü kez, üç ayrı "
 "anlamda: مُسْتَقَرّ *(kalınacak yer)* 25:24 ve 25:66, قُرَّة *(aydınlık)* burada."),
75: ("Yıldızın tek kaynağı edilgenlik oranı: üç fiilin ikisi edilgen (يُجْزَوْنَ *(ödüllendirilirler)*, "
 "يُلَقَّوْنَ *(karşılanırlar)*), oran 0,67 → pas z=3,48. Ölçülebilir bir edilgenlik: kullar bütün "
 "bölüt boyunca ÖZNEYDİ (yürürler, geceleyerler, derler, harcarlar), burada ilk kez NESNE oluyorlar. "
 "غرف *(yüksek oda, gurfe)* korpusta 6 geçişli ve dikey ölçümü ▸önce ceza-karşılık bağlamı veriyor. "
 "Ve karşılanma sözü iki terimli: تَحِيَّةً وَسَلَٰما *(esenlik dileği ve selâm)*; حيي *(diri olma, "
 "hayat; tahiyye)* kökü burada 'tahiyye' anlamında — sûrede kökün dördüncü geçişi ve dördüncü "
 "anlamı (25:3 hayat, 25:49 diriltme, 25:58 Diri, burada selâmlama). Kök düzeyi dikey komşuluk bu "
 "ayrımı yapmıyor (aday 529 sınıfı, sûrede dokuzuncu vaka)."),
76: ("Beş kelime ve 25:66'nın NEREDEYSE TAM İKİZİ: سَآءَتْ مُسْتَقَرًّۭا وَمُقَاما *(ne kötü bir "
 "karargâh ve konak)* / حَسُنَتْ مُسْتَقَرًّۭا وَمُقَاما *(ne güzel bir karargâh ve konak)*. Tek "
 "fark FİİL — سوأ *(kötülük)* / حسن *(güzellik, iyilik)*; kalan üç kelime birebir aynı ve fâsıla "
 "aynı. Ölçülebilir bir üçlü yapı: 25:24 (خَيْرٌۭ مُّسْتَقَرًّۭا وَأَحْسَنُ مَقِيلا *(kalınacak yer "
 "bakımından daha hayırlı)*), 25:66 (olumsuz) ve 25:76 (olumlu) — aynı kök قرر *(karar kılma, "
 "yerleşme)* etrafında üç ayet, iki kutup. Ve defter.json esit alanı 25:66 ile 25:76 arasındaki bu "
 "yakınlığı YAKALAMIYOR; alan ikisinde de boş."),
77: ("Sûre bir hapaksla kapanıyor: يَعْبَؤُا۟ *(değer verir)*, عبأ *(değer verme, aldırma)* kökü, "
 "korpusta TEK geçiş — ve yıldızın tek kaynağı bu (hapaks z=3,38). Sûre 25 üç hapaks taşıyor ve "
 "ikisi (25:33 فسر *(açıklama, tefsir)*, 25:77 عبأ) ★★★ ayetlerde. Ölçülebilir bir kip yoğunluğu: "
 "beş kip işareti (IMPV · NEG · COND · CERT · FUT) — sûrede en yoğun. Ve كذب *(yalan; yalanlama)* "
 "kökü dördüncü ve son kez, fâil üçüncü kez değişerek: 25:11'de inkârcılar (nesne: o saat), "
 "25:19'da tapılanlar (nesne: muhatap), burada MUHATABIN KENDİSİ (كَذَّبْتُمْ *(siz yalanladınız)*). "
 "Kapanış tek kelime ve seyrek: لِزَاما *(yakayı bırakmayan)*, لزم *(ayrılmama, lüzum)* korpusta 3 "
 "geçişli — 25:65'in غَرَاما *(yakayı bırakmayan belâ)* fâsılasıyla anlamca eşleşiyor ve ikisi de "
 "sûrenin son üçte birinde."),
}

ATLAMA = {
 "_mercek_25_75": ("25:75 ★★★ — 🜁 BİYOLOG VE 🜂 UZAY MERCEKLERİ YAZILMADI, ÇIPA YOK. Ayet dokuz "
  "kelime ve tamamı karşılık/karşılanma alanında: ödüllendirme, yüksek makam, selâmlama. Ne canlı, "
  "ne organ, ne gök cismi, ne ölçü, ne süreç. Yıldızın kaynağı içerik değil: TEK kaynak pas z=3,48 "
  "(üç fiilin ikisi edilgen, oran 0,67). ADAY 590'ın BEŞİNCİ ★★★ vakası ve BEŞİ DE ÇIPASIZ."),
 "_mercek_25_77": ("25:77 ★★★ — 🜁 BİYOLOG VE 🜂 UZAY MERCEKLERİ YAZILMADI, ÇIPA YOK. Sûrenin son "
  "ayeti; içerik tamamen değer/dua/tekzip alanında. Yıldızın TEK kaynağı hapaks z=3,38 (عبأ *(değer "
  "verme, aldırma)*, korpusta tek geçiş). ADAY 590'ın ALTINCI VE SON ★★★ vakası — SÛRE 25'İN ALTI "
  "★★★ AYETİNİN ALTISINDA DA ÇIPA SIFIR."),
 "_sure_kapanis_mercek": ("SÛRE 25 MERCEK BİLANÇOSU — TAM SAYIM. Yıldız dağılımı: ★★★ 6 (25:28, "
  "33, 34, 64, 75, 77) · ★★ 5 · ★ 8 · yıldızsız 58. **ALTI ★★★ AYETİN ALTISINDA DA ÇIPA SIFIR.** "
  "Yıldız kaynakları: hapaks x3 (25:28, 33, 77), edilgenlik oranı x2 (25:34, 75), Rab oranı x1 "
  "(25:64) — ALTISI DA SÖZLÜK/BİÇİM İSTATİSTİĞİ, hiçbiri içerik. BUNA KARŞILIK ÇIPA TAŞIYAN ON BİR "
  "AYET (25:25 gök yarılması · 45-46 gölge-güneş süreci · 47 gece/uyku/gündüz · 48 rüzgâr-yağış "
  "sıralaması · 49 su ve diriltme · 53 iki su kütlesi ve ayıraç · 54 sudan beşer · 59 altı gün + "
  "istivâ + arş · 61 burçlar, kandil, aydınlatan ay · 62 gece-gündüz bağıntısı) ve BUNLARIN YALNIZ "
  "BİRİ YILDIZ ALIYOR (25:25, ★★, kaynağı edilgenlik oranı). PROTOKOL GEREĞİ SÛRE BOYUNCA HİÇBİR "
  "UZMAN MERCEĞİ YAZILMADI ve KURAL ÇİĞNENMEDİ. Ayrıca altı ★★★ ayetin beşinde ayet ortalamadan "
  "kısa (n z: -0,68 · -0,47 · -0,15 · -0,79 · -0,36 · -0,04) — KISA AYET YANLILIĞI (aday 583)."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(71, 78):
    OM['25']["25:%d" % n] = {"ar": AR[(25, n)], "meal": MEAL[n], "olcum": OLCUM[n],
                             "mercek": MERCEK[n], "dikey": DIK["25:%d" % n]}
OM['25']['_mercek_atlama_notu'].update(ATLAMA)
OM['25']['_kapanis'] = {
 "durum": "SÛRE 25 (FURKĀN) TAM — 77/77",
 "esma_yeniden_siniflandirma": ("22 token / 17 ayet ölçülmüştü. OKUMA SIRASINDA TEK TEK "
   "DENETLENDİ: GEÇERLİ 8 — 25:6 غَفُور|رَحِيم *(gafûr | rahîm)* (mühür) · 25:20 بَصِير *(gören)* · "
   "25:31 نَصِير *(yardımcı)* · 25:54 قَدِير *(kadîr)* · 25:58 خَبِير *(haberdar)* · 25:70 "
   "غَفُور|رَحِيم (mühür). ARTEFAKT 7 — 25:18 وَلِيّ *(velî)* (çoğul, edinilen varlıklar) · 25:19 "
   "كَبِير *(büyük)* (azabın sıfatı) · 25:21 كَبِير (taşkınlığın sıfatı) · 25:43 وَكِيل *(vekîl)* "
   "(gönderge muhatap) · 25:52 كَبِير (cihadın sıfatı) · 25:63 سَلام *(esenlik)* (kulların sözü) · "
   "25:72 كَرِيم *(kerîm)* (kulların hâli) · 25:75 سَلام (karşılanma sözü) — SEKİZ. BELİRSİZ 1 — "
   "25:59 خَبِير (gönderge ilâhî de olabilir bilen kimse de). ÖZEL AD 5 — رَحْمٰن *(rahmân)* 25:26, "
   "59, 60 x2, 63; beşi de gönderge konumunda, hiçbiri yüklem sıfatı değil (aday 578). "
   "SONUÇ: 22 tokenin 8'i geçerli, 8'i artefakt, 5'i özel ad, 1'i belirsiz. HATA ORANI %36. "
   "MÜHÜR SİNYALİ DOĞRULANDI: iki mühürlü konumun İKİSİ DE geçerli; artefaktların SEKİZİ DE "
   "mühürsüz (aday 501)."),
 "yildiz_cipa": ("★★★ 6 · ★★ 5 · ★ 8 · yıldızsız 58. ALTI ★★★ AYETİN ALTISINDA DA ÇIPA SIFIR; "
   "kaynaklar hapaks x3, edilgenlik oranı x2, Rab oranı x1. ÇIPA TAŞIYAN 11 AYETİN YALNIZ 1'İ "
   "yıldızlı (25:25, ★★). Yıldız ile çıpa arasında korelasyon SIFIR YA DA NEGATİF görünüyor — "
   "null sonuç, çıpa tanımı yazıldıktan sonra kaydedilecek (adaylar 553, 561, 565, 580, 590)."),
 "eksen": ("Allah lafzı 8 token / 6 ayet (17, 41, 55, 68 x2, 70 x2, 71); رَبّ *(Rab)* 14 token / "
   "14 ayet. A/R = 0,57 — sûre 23 ile aynı (aday 525). İlk lafız 25:17'de, ilk Rab 25:16'da; "
   "AÇILIŞ ON BEŞ AYETTE İKİSİ DE YOK (aday 527). Lafız ve Rab aynı ayette YALNIZ BİR KEZ: 25:55. "
   "Sekiz lafız tokeninden İKİSİ alıntı içinde (25:41 itirazcılar; 25:68 anlatı) — aday 562 "
   "sayımı tamamlandı: alıntı içi 1 (25:41), anlatı içi 7."),
 "iltifat": ("3 — 25:14 (3>2), 25:52 (1>23), 25:56 (3>12). ÜÇÜ DE ZAMİR→ZAMİR; aday 517'nin "
   "şüphelendiği lafız→zamir sınıfı sûrede YOK. AMA 25:48'de gönderge→zamir geçişi var "
   "(ٱلَّذِى أَرْسَلَ … وَأَنزَلْنَا) ve tagger 0 veriyor (aday 567) — sûrenin 'iltifât 3' ölçümü "
   "bu belirsizliği taşıyor."),
 "fasila": ("77/77 ACC; 76 ayet ا (A sınıfı), 1 ayet ل (25:17, tek kafiye kırılması). Sûre korpusta "
   "ACC payında birinci (0,596) ve fâsıla çıkarılınca da birinci (0,495) — aday 526. BU KISIT "
   "'aynı kelime farklı bağlamda' bulgularını SİSTEMATİK ÜRETİYOR olabilir: سَبِيلا 7 geçiş "
   "(hepsi fâsıla) · نُشُورا 3 (hepsi fâsıla) · نَذِيرا 4 (hepsi fâsıla) · كَثِيرا 3 · مُقَاما 2 · "
   "سَلَٰما 2. Fâsıla kısıtı altında beklenen tekrar oranı hesaplanmadan bu sınıftan hiçbir bulgu "
   "kapatılmayacak (aday 566)."),
 "mm": ("Fiil + mef'ûl-i mutlak DOKUZ örnek, dört bab: bab II x5 (25:2, 25, 32, 36, 39) · bab I x3 "
   "(25:21, 46, 71) · bab III x1 (25:52). Farklı yapı: 25:23 iç mef'ûl · 25:22 ve 25:53 isim + "
   "ism-i mef'ûl. SEKİZİ FÂSILA KONUMUNDA. defter.json'da MM alanı YOK (adaylar 559, 572)."),
 "araclar": ("SÛRE 25'TE YAKALANAN ARAÇ HATALARI: dikey katman kök-lemma karışması DOKUZ vaka "
   "(25:1 علم · 25:3 أله · 25:13 قرن · 25:19 صرف · 25:35 وزر · 25:47 سبت · 25:54 صهر · 25:64-69 "
   "قوم · 25:75 حيي) — aday 529, onarım ölçütü önerisi: dikey girdisine BAB eklensin (aday 569, "
   "584). Esmâ tablosu hata oranı %36 (yukarıda). Aktör tablosu yanlış pozitif (25:60 نُفُورا → "
   "'nefer') ve eksik pozitif (25:38 أَصْحَٰبَ ٱلرَّسِّ) — aday 579, makro kaydımız geri çekildi. "
   "esit alanı 25:9=17:48 tam özdeşliğini (imlâ farkı) ve 25:66≈25:76 ikizini yakalamıyor "
   "(adaylar 530, 596). Yıldız formülünde kısa ayet yanlılığı şüphesi (aday 583)."),
 "kok": ("612 kök tokeni, 250 ayrık kök, çeşitlilik 0,408, tek geçişli kök 137. Sûre okumasında "
   "kok_turkce.json 959 → 982 (yirmi üç yeni kök) ve altı karşılık genişletildi; GERİYE DÖNÜK İHLÂL "
   "HİÇ ÇIKMADI — aday 570'in açıklama hipotezi: kavram tablosunda karşılığı olan kökler dikey "
   "satırında Türkçe görünüyor, kök dizgisi yazılmıyor."),
}
OM['ilerleme']['not'] = ("Sûre 23 TAM (118/118). Sûre 24 TAM (64/64). **SÛRE 25 (FURKĀN) TAM "
                         "(77/77).** Devam: sûre 26 (Şuarâ) — makro profilden başla.")
OM['ilerleme']['tam'] = [1, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1722
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 25 →', len([k for k in OM['25'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(71, 78):
    MK['25']["25:%d" % n] = MERCEK[n]
MK['25_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 25 →', len(MK['25']))
