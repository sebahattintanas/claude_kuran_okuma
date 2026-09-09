# -*- coding: utf-8 -*-
"""blok_26_71_80.py — sûre 26 beşinci blok (26:71-80). İbrâhîm diyaloğu ve ٱلَّذِى zinciri."""
import json
DIK = json.load(open('blok_dikey_26_71_80.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
71: "Dediler: Putlara tapıyoruz; onlara kapanıp duruyoruz.",
72: "Dedi: Çağırdığınızda sizi işitiyorlar mı?",
73: "Ya da size fayda veya zarar veriyorlar mı?",
74: "Dediler: Hayır; atalarımızı böyle yapar bulduk.",
75: "Dedi: Neye taptığınızı gördünüz mü?",
76: "Siz ve önceki atalarınız.",
77: "Onlar benim düşmanımdır; âlemlerin Rabbi başka.",
78: "Beni yaratan odur; bana yol gösteren de o.",
79: "Bana yediren ve içiren de o.",
80: "Hastalandığımda bana şifa veren de o.",
}

O = {
71: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — أَصْنَام *(putlar)* aktör tablosuna "
 "GİRMİYOR (25:17'de مَا يَعْبُدُونَ *(taptıkları)* de girmemişti; tutarlı) · edim haber, kip "
 "işareti yok · şahıs 3MP x2 · 1P x2 · 3FS x1, iltifât 0 · n=6 mora=37 harf=29 (n z=-0,68), fâsıla "
 "عَٰكِفِينَ *(kapanıp duranlar)* → ن, N sınıfı; **i'râb ACC 2**; bab I x3; zaman PERF x1 · IMPF x2; "
 "dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · عبد *(kul, kulluk)* · صنم *(put, "
 "sanem)* · ظلل *(sürüp gitme, olmayı sürdürme)* · عكف *(bir şeye kapanma, îtikâf)* · bağ: **صنم "
 "*(put, sanem)* korpusta BEŞ geçişli ve dikey ölçümü ▸önce عبد *(kul, kulluk)* x14,1 veriyor — "
 "çift korpusta sabit; 26:70'in dikey satırı da عبد ▸sonra صنم x16,6 vermişti, yani ÇİFT İKİ "
 "YÖNDEN DE bağlı** (elle, L1, aday 647)"),
72: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · şahıs 2MP x3 · "
 "3MP x2 · 3MS x1, iltifât 0 · n=5 mora=25 harf=20 (n z=-0,79), fâsıla تَدْعُونَ *(çağırıyorsunuz)* → "
 "ن, N sınıfı; **i'râb YOK — beş kelimenin hiçbiri i'râb etiketi almıyor**; bab I x3; zaman PERF x1 · "
 "IMPF x2; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · سمع *(işitme)* · دعو *(çağırma, "
 "dua)* · bağ: **26:15, 26:25 ile سمع *(işitme)* üçüncü geçişi** — 26:15'te ilâhî eşlik "
 "(مُّسْتَمِعُونَ *(işitenler)*), 26:25'te Firavun'un alaycı çağrısı (أَلَا تَسْتَمِعُونَ *(işitmiyor "
 "musunuz)*), burada putların işitme YETİSİ sorgulanıyor; aynı kök üç konuşan (elle, L1, aday 648)"),
73: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3MP x4 · 2MP x1, iltifât 0 · n=4 mora=22 harf=17 (n z=-0,89), fâsıla يَضُرُّونَ *(zarar "
 "veriyorlar)* → ن, N sınıfı; **i'râb YOK**; bab I x2; zaman IMPF x2; dış düğüm 0 · yıldız ★ yok · "
 "kökler نفع *(fayda)* · ضرر *(zarar)* · bağ: **25:3 ve 25:55 ile نفع/ضرر çifti ÜÇÜNCÜ kez** — "
 "25:3'te sahte ilâhlar 'kendilerine' fayda/zarar veremiyor (sıra ضَرًّا-نَفْعًا), 25:55'te "
 "'tapanlara' (sıra ters: نفع-ضرر), burada yine tapanlara ve sıra نفع-ضرر; **üç geçişin ikisi aynı "
 "sıralamada, biri ters** (elle, L1, aday 649)"),
74: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3MP x4 · 1P x3, iltifât 0 · n=6 mora=42 harf=30 (n z=-0,68), fâsıla يَفْعَلُونَ *(yapıyorlar)* → "
 "ن, N sınıfı; **i'râb ACC 1**; bab I x3; zaman PERF x2 · IMPF x1; **biçim IDRAB — sûrenin üç "
 "IDRAB'ından biri** (makro sayım 2; bu üçüncüsü, sayım denetlenecek); dış düğüm 0 · yıldız ★ yok · "
 "kökler قول *(söz söyleme)* · وجد *(bulma)* · أبو *(baba)* · فعل *(yapma, işleme)* · bağ: **26:19-20 "
 "ile فعل *(yapma, işleme)* karşılaşması** — orada Firavun'un suçlaması ve Mûsâ'nın itirafı (dört "
 "geçiş), burada bir GELENEK savunması; aynı kök, kişisel eylemden atalar geleneğine (elle, L1, "
 "aday 650)"),
75: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · **şahıs "
 "2MP x6 — blokta en yüksek**; 3MS x1, iltifât 0 · n=5 mora=28 harf=22 (n z=-0,79), fâsıla "
 "تَعْبُدُونَ *(tapıyorsunuz)* → ن, N sınıfı — **26:70'in fâsılasıyla AYNI KELİME**; **i'râb YOK**; "
 "bab I x4; zaman PERF x3 · IMPF x1; **dış düğüm 2** · yıldız ★ yok · kökler قول *(söz söyleme)* · "
 "رأي *(görme)* · كون *(olmak; mekân, yer)* · عبد *(kul, kulluk)* · bağ: xref قال *(dedi)* + رأى "
 "*(gördü)* + كان *(oldu)* → **41:52 · 46:10**; **26:70 ile halka** — soru aynı kelimeyle açılıp "
 "aynı kelimeyle geri dönüyor (مَا تَعْبُدُونَ *(neye tapıyorsunuz)* → مَّا كُنتُمْ تَعْبُدُونَ "
 "*(neye taptığınızı)*); beş ayetlik bir bölüt halkası (elle, L1, aday 651)"),
76: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "2MP x2, iltifât 0 · n=3 mora=27 harf=20 (n z=-1,00), fâsıla ٱلْأَقْدَمُونَ *(öncekiler)* → ن, N "
 "sınıfı; **i'râb NOM 2; fiil YOK**; dış düğüm 0 · yıldız ★ yok · kökler أبو *(baba)* · قدم *(öne "
 "geçme)* · bağ: **26:26 ve 26:51 ile 'öncekiler' üçlüsü** — 26:26 ءَابَآئِكُمُ ٱلْأَوَّلِينَ "
 "*(önceki atalarınız)*, 26:51 أَوَّلَ ٱلْمُؤْمِنِينَ *(ilk iman edenler)*, burada ءَابَآؤُكُمُ "
 "ٱلْأَقْدَمُونَ *(önceki atalarınız)* — **ilk ikisi أول *(ilk, evvel)* kökünden, bu قدم *(öne "
 "geçme)* kökünden: aynı anlam alanı, iki ayrı kök** (aday 613/627 deseni) (elle, L1, aday 652)"),
77: ("eksen: **lafız YOK · رَبّ *(Rab)* 5. sırada — on yedinci Rab**, **rab z=3,23: yıldızın TEK "
 "kaynağı** (n=6, oran 0,17) · esmâ yok · aktör yok · edim haber, kip RES 1 · şahıs 3MP x1 · 1S x1, "
 "**iltifât 1 — yön 2>13; sûrenin dördüncü iltifâtı** · n=6 mora=36 harf=23 (n z=-0,68), fâsıla "
 "ٱلْعَٰلَمِينَ *(âlemler)* → ن, N sınıfı; i'râb ACC 2 · NOM 1 · GEN 1; **fiil YOK**; **biçim "
 "HASR**; dış düğüm 0 · **yıldız ★★★** · kökler عدو *(düşmanlık, düşman)* · ربب *(rab, terbiye "
 "etme)* · علم *(bilme; âlem)* · bağ: **رَبَّ ٱلْعَٰلَمِينَ terkibinin sûrede BEŞİNCİ geçişi** "
 "(26:16, 23, 47, 77 ve 26:24/28'in kapsam cevapları); **26:23 ile karşıtlık** — orada Firavun "
 "terkibi SORU olarak kullanıyordu, burada İbrâhîm İSTİSNA olarak: 'onlar düşmanım, âlemlerin Rabbi "
 "hariç' (elle, L1, aday 653)"),
78: ("eksen: **lafız YOK · Rab YOK — gönderge ٱلَّذِى *(o ki)*; sûre 26'da ilk kez bu biçim** · "
 "esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs 3MS x3 · 1S x2, iltifât 0 · n=4 "
 "mora=21 harf=17 (n z=-0,89), fâsıla يَهْدِينِ *(bana yol gösterir)* → ن, N sınıfı; **i'râb YOK**; "
 "bab I x2; zaman PERF x1 · IMPF x1; dış düğüm 0 · yıldız ★ yok · kökler خلق *(yaratma)* · هدي "
 "*(yol gösterme)* · bağ: **26:62 ile هدي *(yol gösterme)* ikinci geçişi** — orada Mûsâ سَيَهْدِينِ "
 "*(bana yol gösterecek)* diyordu (FUT), burada İbrâhîm فَهُوَ يَهْدِينِ *(bana yol gösteren o)* "
 "(IMPF); **iki elçi, aynı kök, aynı ـِينِ eki, aynı fâsıla konumu** (elle, L1, aday 654); "
 "**25:1-2 ile ٱلَّذِى zinciri karşılaştırması** (aday 527, elle, L1, aday 655)"),
79: ("eksen: **lafız YOK · Rab YOK — gönderge وَٱلَّذِى *(ve o ki)*, bitişik ayette ikinci kez** · "
 "esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs 3MS x3 · 1S x2, iltifât 0 · n=4 "
 "mora=23 harf=19 (n z=-0,89), fâsıla يَسْقِينِ *(bana içirir)* → ن, N sınıfı; **i'râb YOK**; "
 "bab I x1 · IV x1; zaman IMPF x2; dış düğüm 0 · yıldız ★ yok · kökler طعم *(yiyecek, yemek "
 "verme)* · سقي *(sulama)* · bağ: **25:49 ile سقي *(sulama)* ikinci geçişi** — orada نُسْقِيَهُۥ … "
 "أَنْعَٰما وَأَنَاسِىَّ *(davarları ve insanları sularız)* çoğul ve tür düzeyinde, burada "
 "يَسْقِينِ *(bana içirir)* tekil ve kişisel; **aynı kök, türden bireye** (elle, L1, aday 656)"),
80: ("eksen: **lafız YOK · Rab YOK — gönderge bu kez ٱلَّذِى DEĞİL, şart cümlesi: وَإِذَا مَرِضْتُ "
 "فَهُوَ *(hastalandığımda o)*; zincirde biçim kırılması** · esmâ yok · aktör yok · edim haber, kip "
 "işareti yok · **şahıs 1S x3 · 3MS x2**, iltifât 0 · n=4 mora=20 harf=16 — **blokta en kısa "
 "ayetlerden** (n z=-0,89), fâsıla يَشْفِينِ *(bana şifa verir)* → ن, N sınıfı; **i'râb YOK**; "
 "bab I x2; zaman PERF x1 · IMPF x1; dış düğüm 0 · yıldız ★ yok · kökler مرض *(hastalık)* · شفي "
 "*(şifa verme, iyileştirme)* · bağ: **شفي *(şifa verme, iyileştirme)* korpusta ALTI geçişli**; "
 "**26:78-80 üçlüsünde fâsıla eki DEĞİŞMİYOR: يَهْدِينِ · يَسْقِينِ · يَشْفِينِ — üçü de ـِينِ** "
 "(elle, L1, aday 655)"),
}

M = {
71: ("Cevap iki fiille veriliyor ve ikisi de süreklilik bildiriyor: نَعْبُدُ أَصْنَاما *(putlara "
 "tapıyoruz)* ve فَنَظَلُّ لَهَا عَٰكِفِينَ *(onlara kapanıp duruyoruz)*. ظلل *(sürüp gitme, olmayı "
 "sürdürme)* burada 'gölge' değil 'sürdürme' anlamında — kök korpusta 33 geçişli ve dikey ölçümü "
 "▸sonra meyve x45,5 · bulut x42,4 veriyor, yani korpusta ağırlıkla GÖLGE bağlamında; burada azınlık "
 "anlamı (aday 529 sınıfı, sûre 26'da yeni vaka). صنم *(put, sanem)* korpusta beş geçişli ve dikey "
 "ölçümü ▸önce عبد *(kul, kulluk)* x14,1 veriyor; bir önceki ayetin dikey satırı da عبد ▸sonra "
 "صنم x16,6 vermişti — **çift korpusta iki yönden de bağlı**, yani terkip bu sahneye özgü değil. "
 "عكف *(bir şeye kapanma, îtikâf)* korpusta dokuz geçişli."),
72: ("Soru bir yeti sorgusu ve en kısa biçimde: هَلْ يَسْمَعُونَكُمْ إِذْ تَدْعُونَ *(çağırdığınızda "
 "sizi işitiyorlar mı)*. Ölçülebilir bir boşluk: beş kelimenin hiçbiri i'râb etiketi almıyor — ayet "
 "tamamen fiil ve edattan kurulu. سمع *(işitme)* sûrede üçüncü kez ve üçüncü konuşanla: 26:15'te "
 "ilâhî eşlik (إِنَّا مَعَكُم مُّسْتَمِعُونَ *(biz sizinle beraber işitenleriz)*), 26:25'te "
 "Firavun'un alayı (أَلَا تَسْتَمِعُونَ *(işitmiyor musunuz)*), burada putların yetisi. Üç ayette "
 "aynı kök, üç ayrı özne ve üç ayrı işlev."),
73: ("İkinci soru fayda ve zararı birlikte sınıyor: أَوْ يَنفَعُونَكُمْ أَوْ يَضُرُّونَ *(size fayda "
 "veya zarar veriyorlar mı)*. Bu çift okumada ÜÇÜNCÜ kez: 25:3'te sahte ilâhlar KENDİLERİNE fayda "
 "ya da zarar veremiyordu (sıra ضَرًّا-نَفْعًا), 25:55'te TAPANLARA (sıra ters: نفع-ضرر), burada yine "
 "tapanlara ve yine نفع-ضرر. **Üç geçişin ikisi aynı sıralamada.** Dikey ölçüm çiftin korpusta "
 "sabit olduğunu gösteriyor: نفع *(fayda)* ▸önce zarar x20,5, ضرر *(zarar)* ▸sonra نفع x19,0 — iki "
 "yönlü bağ. Dört kelime ve yine hiç i'râb etiketi yok."),
74: ("Savunma bir gelenek iddiasına dayanıyor: بَلْ وَجَدْنَآ ءَابَآءَنَا كَذَٰلِكَ يَفْعَلُونَ "
 "*(hayır; atalarımızı böyle yapar bulduk)*. Ölçülebilir bir kök karşılaşması: فعل *(yapma, "
 "işleme)* 26:19-20'de dört kez geçmişti — Firavun'un suçlaması (üç kez) ve Mûsâ'nın itirafı (bir "
 "kez), hepsi KİŞİSEL eylem; burada ATALAR GELENEĞİ. Aynı kök, bireyden geleneğe. Ve ayet IDRAB ile "
 "açılıyor; makro sayım sûrede IDRAB'ı 2 veriyor ama bu üçüncü — **makro sayım denetlenecek** "
 "(yeni ölçüm notu). وجد *(bulma)* korpusta 107 geçişli."),
75: ("Soru bir görme emriyle çerçeveleniyor: أَفَرَءَيْتُم مَّا كُنتُمْ تَعْبُدُونَ *(neye "
 "taptığınızı gördünüz mü)*. Ölçülebilir bir halka: 26:70'te bölüt مَا تَعْبُدُونَ *(neye "
 "tapıyorsunuz)* ile açılmıştı; burada aynı kelimeyle kapanıyor — **beş ayetlik bir bölüt halkası** "
 "ve iki fâsıla aynı kelime. Beş kelimede 2MP altı kez, blokta en yüksek. Ve yine hiç i'râb "
 "etiketi yok: 26:72, 73 ve 75 — **üç ayet i'râbsız**, blokta bu bir küme."),
76: ("Üç kelime, fiil yok, iki merfû isim. Ölçülebilir bir kök seçimi: 'öncekiler' burada قدم *(öne "
 "geçme)* kökünden (ٱلْأَقْدَمُونَ *(öncekiler)*), oysa 26:26'da أول *(ilk, evvel)* kökündendi "
 "(ءَابَآئِكُمُ ٱلْأَوَّلِينَ *(önceki atalarınız)*) — **aynı anlam alanı, iki ayrı kök**; 26:16↔26:18'in "
 "ربب/ربو ve 26:42↔26:58'in قرب/قوم çiftleriyle aynı desen. Sûre 26'da bu üçüncü vaka. قدم korpusta "
 "48 geçişli ve dikey ölçümü ▸önce حرق *(yakma)* x45,0 · ▸sonra erteleme x23,3 veriyor — kök "
 "korpusta ağırlıkla 'öne sürme / takdim' bağlamında."),
77: ("İstisna cümlesi bir düşmanlık bildirimiyle kuruluyor: فَإِنَّهُمْ عَدُوٌّ لِّى إِلَّا رَبَّ "
 "ٱلْعَٰلَمِينَ *(onlar benim düşmanımdır; âlemlerin Rabbi başka)*. Ölçülebilir bir sayı uyumsuzluğu: "
 "عَدُوّ *(düşman)* TEKİL ama gönderge çoğul (putlar) — okumada ikinci sayı uyumsuzluğu (birincisi "
 "26:16'da رَسُول tekil, zamir çoğuldu). Ve رَبَّ ٱلْعَٰلَمِينَ terkibi sûrede beşinci kez: 26:16 "
 "elçilik iddiası, 26:23 Firavun'un sorusu, 26:47 büyücülerin ikrarı, burada İbrâhîm'in istisnası. "
 "**Aynı terkip dört ayrı konuşanda dört ayrı işlev.** Sûrenin dördüncü iltifâtı da burada (2>13)."),
78: ("ٱلَّذِى zinciri açılıyor ve sûre 26'da bu ilk kez. Ölçülebilir bir yapı: iki fiil, biri mâzi "
 "biri muzâri — خَلَقَنِى *(beni yarattı)* ve فَهُوَ يَهْدِينِ *(bana yol gösteren o)*; tamamlanmış "
 "bir eylem ve süregelen bir eylem. هدي *(yol gösterme)* sûrede ikinci kez: 26:62'de Mûsâ "
 "سَيَهْدِينِ *(bana yol gösterecek)* demişti, FUT; burada İbrâhîm يَهْدِينِ, IMPF. **İki elçi, "
 "aynı kök, aynı ـِينِ eki, aynı fâsıla konumu, iki zaman.** Ve zincirin biçimi sûre 25'inkinden "
 "farklı: orada ٱلَّذِى göndergesi bir üçüncü şahsa aitti (25:1-2, 6, 10), burada birinci şahsın "
 "kendi Rabbine (aday 527 ile karşılaştırma)."),
79: ("Zincirin ikinci halkası ve yine dört kelime: وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ *(bana "
 "yediren ve içiren de o)*. Ölçülebilir bir çift: طعم *(yiyecek, yemek verme)* ve سقي *(sulama)* — "
 "ikisi de korpusta seyrek sayılabilir (48 ve 25) ve burada bitişik. سقي 25:49'da da vardı: orada "
 "نُسْقِيَهُۥ … أَنْعَٰما وَأَنَاسِىَّ *(davarları ve insanları sularız)* çoğul ve TÜR düzeyindeydi, "
 "burada يَسْقِينِ *(bana içirir)* tekil ve KİŞİSEL. Aynı kök, türden bireye. Dikey ölçüm سقي için "
 "▸sonra موه *(su)* x19,8 veriyor — kök korpusta suya bağlı ve burada su ANILMIYOR."),
80: ("Zincirde bir biçim kırılması: 26:78 ve 26:79 ٱلَّذِى ile başlıyordu, bu ayet وَإِذَا مَرِضْتُ "
 "*(hastalandığımda)* ile — şart cümlesi. Ölçülebilir bir fark: zincirin öteki halkaları koşulsuz, "
 "bu halka koşullu; ve koşul birinci şahsın kendi hâli. Buna karşılık fâsıla eki değişmiyor: "
 "يَهْدِينِ · يَسْقِينِ · يَشْفِينِ — üçü de ـِينِ, yani biçim kırılsa da ses düzeni sürüyor. شفي "
 "*(şifa verme, iyileştirme)* korpusta ALTI geçişli ve dikey ölçümü ▸önce hiçbir komşu vermiyor, "
 "▸sonra yalnız iman x5,4 — kökün korpusta dar ve tek yönlü bir yatağı var. مرض *(hastalık)* ise "
 "24 geçişli ve ▸önce kalp x31,5 · nifak x26,0 veriyor: **kök korpusta ağırlıkla KALP HASTALIĞI "
 "(nifak) için, burada BEDENSEL hastalık** (aday 529 sınıfı)."),
}

ATLAMA = {
 "_mercek_26_77": ("26:77 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. فَإِنَّهُمْ عَدُوٌّ لِّى إِلَّا رَبَّ "
  "ٱلْعَٰلَمِينَ. Tek kaynak rab z=3,23 (n=6, oran 0,17). İçerik bir düşmanlık bildirimi ve istisna; "
  "ne canlı, ne gök cismi, ne ölçü, ne süreç."),
 "_blok_notu_26_71_80": ("BLOK BİLANÇOSU: ★★★ 1 (26:77) · ★★ 0 · ★ 0 · 9 ayet yıldızsız — okumada "
  "görülen EN AZ YILDIZLI on ayetlik blok. Tek yıldızın kaynağı rab oranı. ÇIPA: 26:79 (yedirme, "
  "içirme) ve 26:80 (hastalık, şifa) çıpa TAŞIYABİLECEK ayetler ve İKİSİ DE YILDIZSIZ — aday "
  "599/602 tablosuna ekleniyor. **SINIR NOTU: 26:80 bir hastalık ve iyileşme ADI veriyor ama ne "
  "mekanizma ne süreç ne ölçü tanımlıyor; 'şifanın biyolojisi' üzerine hiçbir şey söylenmedi ve "
  "söylenmeyecek — yasaklı 'bilimsel izdüşüm'.** Ayrıca üç ayet (26:72, 73, 75) HİÇ İ'RÂB ETİKETİ "
  "ALMIYOR; blokta bu bir küme ve okumada ilk kez ölçülüyor."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(71, 81):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 80/227.** Devam: 26:81'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-80 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1802
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(71, 81):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
