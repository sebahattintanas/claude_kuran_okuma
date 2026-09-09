# -*- coding: utf-8 -*-
"""blok_26_131_140.py — sûre 26 on birinci blok (26:131-140). Hûd kıssasının kapanışı."""
import json
DIK = json.load(open('blok_dikey_26_131_140.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
131: "Allah'tan sakının ve bana itaat edin.",
132: "Bildiğiniz şeylerle size yardım edenden sakının.",
133: "Size davarlar ve oğullarla yardım etti.",
134: "Bahçeler ve pınarlarla.",
135: "Ben sizin adınıza büyük bir günün azabından korkuyorum.",
136: "Dediler: Öğüt versen de vermesen de bizce birdir.",
137: "Bu, öncekilerin âdetinden başka bir şey değil.",
138: "Biz azaba uğratılacak da değiliz.",
139: "Onu yalanladılar, biz de onları helâk ettik. Bunda elbette bir âyet var; ama onların çoğu inanmıyor.",
140: "Rabbin, elbette o Azîz'dir, Rahîm'dir.",
}

O = {
131: ("eksen: **ALLAH LAFZI 2. sırada — sûrenin YEDİNCİ lafzı**, **allah z=6,14: yıldızın TEK "
 "kaynağı** (n=3, oran 0,33) · Rab yok · esmâ yok · aktör yok · edim emir, kip IMPV 2 · şahıs "
 "2MP x4 · 1S x1, iltifât 0 · n=3 mora=23 harf=18 (n z=-1,00), fâsıla وَأَطِيعُونِ *(bana itaat "
 "edin)* → ن, N sınıfı; **i'râb ACC 1**; bab IV x1 · VIII x1; zaman IMPV x2; **NAKARAT alanı = 8, "
 "temsil ayet 26:108**; **esit: yedi ayetle TAM ÖZDEŞ** · dış düğüm 0 · **yıldız ★★★** · kökler "
 "وقي *(sakınma, koruma)* · أله *(ilâh; lafza-i celâl)* · طوع *(güç yetirme, itaat)* · bağ: "
 "**ÖN-KAYIT ÖĞESİ (vi) VAR — Hûd kıssasında altı öğenin altısı da tamamlandı** (aday 696); "
 "dördüncü nakarat kümesinin DÖRDÜNCÜ geçişi ve dördünde de ★★★ (elle, L1)"),
132: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir, kip IMPV 1 · **şahıs "
 "2MP x5 · 3MS x1**, iltifât 0 · n=5 mora=34 harf=25 (n z=-0,79), fâsıla تَعْلَمُونَ "
 "*(biliyorsunuz)* → ن, N sınıfı; **i'râb YOK**; bab I x1 · IV x1 · VIII x1; zaman IMPV 1 · PERF 1 · "
 "IMPF 1; dış düğüm 0 · yıldız ★ yok · kökler وقي *(sakınma, koruma)* · مدد *(uzatma, imdat)* · "
 "علم *(bilme; ilim)* · bağ: **26:131 ile bitişik çift — aynı kök (وقي) iki ayette, biri NAKARAT "
 "biri değil**: 26:131'de فَٱتَّقُوا۟ ٱللَّهَ *(Allah'tan sakının)*, burada وَٱتَّقُوا۟ ٱلَّذِىٓ "
 "أَمَدَّكُم *(size yardım edenden sakının)*; **lafızdan gönderge ٱلَّذِى'ye** (elle, L1, aday 701)"),
133: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — أَنْعَٰم *(davarlar)* aktör tablosuna "
 "girmiyor · edim haber, kip işareti yok · şahıs 3MS x1 · 2MP x1, iltifât 0 · n=3 mora=21 harf=16 "
 "(n z=-1,00), fâsıla وَبَنِينَ *(oğullar)* → ن, N sınıfı; **i'râb GEN 2**; bab IV x1; zaman PERF 1; "
 "dış düğüm 0 · yıldız ★ yok · kökler مدد *(uzatma, imdat)* · نعم *(nimet; davar)* · بني *(oğul, "
 "evlat)* · bağ: **26:88 ile مال/بنون karşılaştırması** — orada يَوْمَ لَا يَنفَعُ مَالٌ وَلَا "
 "بَنُونَ *(o gün ne mal fayda verir ne oğullar)*, burada aynı ikili bir NİMET olarak sayılıyor; "
 "**aynı çift, biri âhirette işe yaramaz, öteki dünyada nimet** (elle, L1, aday 702)"),
134: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "eki YOK, fiil YOK** · n=2 mora=15 harf=10 — **SÛRENİN OKUNAN EN KISA AYETİ** (n z=-1,11; 26:60 "
 "ile aynı değer), fâsıla وَعُيُونٍ *(pınarlar)* → ن, N sınıfı — **26:57'nin fâsılasıyla AYNI "
 "KELİME**; **i'râb GEN 2**; dış düğüm 0 · yıldız ★ yok · kökler جنن *(örtme, gizleme; cennet; "
 "cin)* · عين *(göz; pınar)* · bağ: **26:57 ile BİREBİR AYNI İKİLİ** — orada فَأَخْرَجْنَٰهُم مِّن "
 "جَنَّٰتٍ وَعُيُونٍ *(onları bahçelerden ve pınarlardan çıkardık)* KAYIP, burada aynı ikili "
 "NİMET; **iki kelime, iki sûre bölütü, ters işaret** (elle, L1, aday 702)"),
135: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "1S x2 · 2MP x1, iltifât 0 · n=6 mora=34 harf=24 (n z=-0,68), fâsıla عَظِيمٍ *(büyük, azametli)* → "
 "م, N sınıfı; **i'râb ACC 2 · GEN 2**; bab I x1; zaman IMPF 1; dış düğüm 0 · yıldız ★ yok · kökler "
 "خوف *(korku)* · عذب *(azap)* · يوم *(gün)* · عظم *(büyüklük, azamet; kemik)* · bağ: **26:12, "
 "26:14, 26:21 ile خوف *(korku)* DÖRDÜNCÜ geçişi ve İLK KEZ BAŞKASI İÇİN** — orada Mûsâ kendisi "
 "için korkuyordu (üç kez), burada Hûd kavmi için: إِنِّىٓ أَخَافُ عَلَيْكُمْ *(sizin adınıza "
 "korkuyorum)*; **aynı fiil, ilk kez عَلَىٰ edatıyla** (elle, L1, aday 703)"),
136: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · şahıs "
 "3MP x2 · 1P x1 · 2MS x3, iltifât 0 · n=9 mora=48 harf=36 — **blokta en uzun ikinci ayet** "
 "(n z=-0,36), fâsıla ٱلْوَٰعِظِينَ *(öğüt verenler)* → ن, N sınıfı; i'râb NOM 1 · GEN 1; bab I x3; "
 "zaman PERF x2 · IMPF x1; **kök ikilemesi وعظ *(öğüt verme)* x2 — şart ve karşıtı aynı kökle: "
 "أَوَعَظْتَ أَمْ لَمْ تَكُن مِّنَ ٱلْوَٰعِظِينَ *(öğüt versen de vermesen de)***; simetri "
 "[3,3,6,1]; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · سوي *(düzenleme, denk "
 "kılma)* · وعظ *(öğüt verme)* · كون *(olmak; mekân, yer)* · bağ: **25:59 ve 26:98 ile سوي "
 "*(düzenleme, denk kılma)* ÜÇÜNCÜ geçişi** — 25:59 bab VIII 'istivâ', 26:98 bab II 'denk kılma', "
 "burada isim سَوَآء *(birdir, eşittir)*; **aynı kök, üç biçim, üç anlam** (elle, L1, aday 704)"),
137: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · RES 1 · "
 "**şahıs eki YOK, fiil YOK** · n=5 mora=28 harf=18 (n z=-0,79), fâsıla ٱلْأَوَّلِينَ *(öncekiler)* → "
 "ن, N sınıfı — **26:26'nın fâsılasıyla AYNI KELİME**; i'râb NOM 1 · GEN 1; **biçim HASR + "
 "DIKKAT**; dış düğüm 0 · yıldız ★ yok · kökler خلق *(yaratma; huy, ahlâk)* · أول *(ilk, evvel)* · "
 "bağ: **خلق *(yaratma; huy, ahlâk)* — 529 KÜMESİNE YENİ VE ÇOK SIK KÖK VAKASI**: kök korpusta "
 "261 geçişli ve ezici çoğunlukla 'yaratma' anlamında; burada خُلُق *(huy, âdet)* anlamında ve "
 "**dikey satırı korpus anlamını getiriyor** (▸önce مضغ *(çiğnenmiş et)* x27,6 · meni x27,6 · علق "
 "*(ilişme; kan pıhtısı)* x23,7 — üçü de yaratılış bağlamı) (elle, L1, aday 705)"),
138: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · **şahıs "
 "1P x1 — ayette başka şahıs yok**, iltifât 0 · n=3 mora=18 harf=13 (n z=-1,00), fâsıla "
 "بِمُعَذَّبِينَ *(azaba uğratılanlar)* → ن, N sınıfı; **i'râb GEN 1; fiil YOK**; dış düğüm 0 · "
 "yıldız ★ yok · **TEK KÖK: عذب *(azap)*** · bağ: **26:135 ile bitişik olmayan çift, TERS KUTUP** — "
 "orada Hûd أَخَافُ عَلَيْكُمْ عَذَابَ يَوْمٍ عَظِيمٍ *(büyük bir günün azabından korkuyorum)* "
 "diyor, burada kavim وَمَا نَحْنُ بِمُعَذَّبِينَ *(biz azaba uğratılacak değiliz)* diyor; **aynı "
 "kök, üç ayet arayla, korkudan reddetmeye** (elle, L1, aday 706)"),
139: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُؤْمِن *(mümin)* 10. sırada = fâsıla — ARTEFAKT, "
 "onuncu token** · aktör yok · edim haber, kip EMPH 1 · NEG 1 · şahıs 3MP x4 · 3MS x2 · 1P x2, "
 "iltifât 0 · n=10 mora=57 harf=47 — **blokta en uzun ayet** (n z=-0,26), fâsıla مُّؤْمِنِينَ → "
 "ن, N sınıfı; i'râb ACC 3 · NOM 1; bab I x1 · II x1 · IV x1; zaman PERF x3; **açık sayı sözcüğü: "
 "كثر *(çokluk)* → أَكْثَر *(çoğu)***; **NAKARAT alanı = 0 VE esit BOŞ — AMA AYET BİRİNCİ NAKARATI "
 "İÇERİYOR**: إِنَّ فِى ذَٰلِكَ لَءَايَةً وَمَا كَانَ أَكْثَرُهُم مُّؤْمِنِينَ, öncesine "
 "فَكَذَّبُوهُ فَأَهْلَكْنَٰهُمْ *(onu yalanladılar, biz de onları helâk ettik)* eklenmiş · "
 "dış düğüm 0 · yıldız ★ yok · kökler كذب *(yalan; yalanlama)* · هلك *(helâk)* · أيي *(âyet, "
 "işaret)* · كون *(olmak; mekân, yer)* · كثر *(çokluk)* · أمن *(güven; iman)* · bağ: **NAKARATIN "
 "GÖMÜLÜ BİÇİMİ — ölçüm alanı yakalamıyor** (elle, L1, aday 707)"),
140: ("eksen: **lafız YOK · رَبّ *(Rab)* 2. sırada — yirmi altıncı Rab**, **rab z=3,94: yıldızın "
 "TEK kaynağı** · **esmâ عَزِيز *(azîz)* + رَحِيم *(rahîm)* = fâsıla — MÜHÜR; GEÇERLİ; beşinci "
 "mühür** · aktör yok · edim haber, kip EMPH 1 · şahıs 2MS x1 · 3MS x1, iltifât 0 · n=5 mora=28 "
 "harf=21 (n z=-0,79), fâsıla ٱلرَّحِيمُ → م, N sınıfı; **i'râb ACC 2 · NOM 2; fiil YOK**; "
 "**NAKARAT alanı = 8, temsil ayet 26:9**; **esit: yedi ayetle TAM ÖZDEŞ** · dış düğüm 0 · "
 "**yıldız ★★★** · kökler ربب *(rab, terbiye etme)* · عزز *(izzet, üstünlük)* · رحم *(rahmet, "
 "merhamet)* · bağ: **ikinci nakaratın BEŞİNCİ geçişi; ama nakarat ÇİFTİ burada BOZULUYOR** — "
 "önceki dört konumda birinci nakarat AYRI AYETTİ (26:8, 67, 103, 121), burada 26:139'a GÖMÜLÜ "
 "(elle, L1, aday 707)"),
}

M = {
131: ("**Ön-kayıt öğesi (vi) var** — Hûd kıssasında altı öğenin altısı da tamamlandı (aday 696). "
 "Dördüncü nakarat kümesinin dördüncü geçişi ve dördünde de ★★★, dördünde de allah z=6,14. "
 "Ölçülebilir bir sıkışma: 26:126 ve 26:131 arasında yalnız dört ayet var ve ikisi de aynı nakarat; "
 "26:108-110'daki A-B-A örgüsünden farklı olarak burada araya Hûd'un üç suçlaması giriyor "
 "(26:128-130). **Yani örgü kıssadan kıssaya değişiyor** — 685'in ön-kaydı öğelerin VARLIĞINI "
 "doğru bildi ama ARALIKLARINI öngörmemişti."),
132: ("Emir bir öncekinin devamı ama gönderge değişiyor: 26:131'de فَٱتَّقُوا۟ ٱللَّهَ *(Allah'tan "
 "sakının)* — lafız; burada وَٱتَّقُوا۟ ٱلَّذِىٓ أَمَدَّكُم *(size yardım edenden sakının)* — "
 "gönderge ٱلَّذِى *(o ki)*. **Aynı kök (وقي *(sakınma, koruma)*), bitişik iki ayet, lafızdan "
 "göndergeye.** Bu, sûre 25'in ٱلَّذِى zinciriyle (aday 527) ve 26:78-82'nin zinciriyle (aday 655) "
 "aynı sınıfta ama burada zincir tek halkalı. مدد *(uzatma, imdat)* korpusta 52 geçişli ve dikey "
 "ölçümü ▸önce deniz x20,3 · kalem x16,9 veriyor — 'imdat' anlamı azınlık. Ve ayet i'râb etiketi "
 "almıyor."),
133: ("Yardımın içeriği sayılıyor: بِأَنْعَٰمٍ وَبَنِينَ *(davarlar ve oğullar)*. Ölçülebilir bir "
 "kutup tersliği: 26:88'de يَوْمَ لَا يَنفَعُ مَالٌ وَلَا بَنُونَ *(o gün ne mal fayda verir ne "
 "oğullar)* denmişti — aynı ikili orada âhirette **işe yaramaz**, burada dünyada **nimet**. Kırk "
 "beş ayet arayla aynı çift, ters işaret. نعم *(nimet; davar)* korpusta 140 geçişli ve dikey ölçümü "
 "▸önce ilham-nasip x102,3 veriyor. Ve أَنْعَٰم aktör tablosuna girmiyor — 25:44 ve 25:49'da da "
 "girmemişti; **tutarlı.**"),
134: ("İki kelime — **sûrenin okunan en kısa ayeti** (26:60 ile aynı n z=-1,11). Ölçülebilir bir "
 "birebir tekrar: جَنَّٰتٍ وَعُيُونٍ *(bahçeler ve pınarlar)* 26:57'de de vardı — orada "
 "فَأَخْرَجْنَٰهُم مِّن جَنَّٰتٍ وَعُيُونٍ *(onları bahçelerden ve pınarlardan çıkardık)*, yani "
 "**kayıp**; burada **nimet**. Aynı iki kelime, aynı i'râb (GEN 2), yetmiş yedi ayet arayla, ters "
 "işaret. عين *(göz; pınar)* korpusta 65 geçişli ve dikey ölçümü ▸sonra burun x196,0 · diş x147,0 "
 "veriyor — kök korpusta ezici çoğunlukla ORGAN anlamında, burada pınar (aday 529 sınıfı)."),
135: ("Korku ilk kez başkası için: إِنِّىٓ أَخَافُ عَلَيْكُمْ *(sizin adınıza korkuyorum)*. "
 "Ölçülebilir bir edat farkı: خوف *(korku)* sûrede dördüncü geçiş — 26:12 أَخَافُ أَن *(korkuyorum "
 "ki)*, 26:14 aynı, 26:21 خِفْتُكُمْ *(sizden korktum)*, burada **ilk kez عَلَىٰ edatıyla** ve "
 "nesne muhatabın kendisi. Üç geçiş kendisi için, dördüncüsü başkası için. عظم *(büyüklük, azamet; "
 "kemik)* dikey ölçümü ▸önce مضغ *(çiğnenmiş et)* x69,8 veriyor — kök korpusta 'kemik' anlamıyla "
 "da yüklü; burada 'azametli'."),
136: ("Kavmin cevabı bir kayıtsızlık bildirimi ve kök ikilemesiyle: أَوَعَظْتَ أَمْ لَمْ تَكُن مِّنَ "
 "ٱلْوَٰعِظِينَ *(öğüt versen de vermesen de)* — وعظ *(öğüt verme)* fiil ve ism-i fâil olarak, şart "
 "ve karşıtı aynı kökle. Ölçülebilir bir kök izleği: سوي *(düzenleme, denk kılma)* okumada üçüncü "
 "geçiş ve üçüncü biçimi — 25:59 bab VIII 'istivâ', 26:98 bab II 'denk kılma', burada isim سَوَآء "
 "*(birdir)*. **Aynı kök, üç biçim, üç anlam, iki sûre.** Ve simetri [3,3,6,1]: ayet dört bölütlü."),
137: ("Beş kelime, fiil yok, HASR + DIKKAT. Ölçülebilir bir anlam kayması: خلق *(yaratma; huy, "
 "ahlâk)* korpusta **261 geçişli** ve ezici çoğunlukla 'yaratma' anlamında; burada خُلُق *(huy, "
 "âdet)* anlamında. **Ve dikey satırı korpus anlamını getiriyor**: ▸önce مضغ *(çiğnenmiş et)* "
 "x27,6 · meni x27,6 · علق *(ilişme; kan pıhtısı)* x23,7 — üçü de yaratılış bağlamı, bu ayetle "
 "ilgisi yok. 529 kümesine sûre 26'nın on ikinci vakası ve 26:128'in أيي *(âyet, işaret)* vakasından "
 "sonra ikinci 'çok sık kök' örneği. Ve fâsıla ٱلْأَوَّلِينَ 26:26'dan geri geliyor."),
138: ("Üç kelime, fiil yok, tek kök. Ölçülebilir bir kutup tersliği: عذب *(azap)* 26:135'te Hûd'un "
 "**korkusuydu** (أَخَافُ عَلَيْكُمْ عَذَابَ يَوْمٍ عَظِيمٍ), burada kavmin **reddi** (وَمَا "
 "نَحْنُ بِمُعَذَّبِينَ). Üç ayet arayla aynı kök, korkudan reddetmeye. Ve ayet edilgen ism-i "
 "mef'ûl taşıyor (مُعَذَّبِينَ) ama fiil yok, yani `pas` sayacı bunu görmüyor — **ölçü tanımı "
 "eksiği: edilgen ism-i mef'ûl `pas` alanına girmiyor** (yeni not)."),
139: ("Blokta en uzun ayet ve **ölçüm alanının bir boşluğu burada görünüyor**: ayet sûrenin birinci "
 "nakaratını (إِنَّ فِى ذَٰلِكَ لَءَايَةً وَمَا كَانَ أَكْثَرُهُم مُّؤْمِنِينَ) **içeriyor** ama "
 "başına فَكَذَّبُوهُ فَأَهْلَكْنَٰهُمْ *(onu yalanladılar, biz de onları helâk ettik)* eklenmiş; "
 "n=10 ve **nakarat alanı 0, esit alanı boş**. Yani nakarat ölçümü yalnız TAM AYET eşleşmesini "
 "sayıyor; **gömülü nakaratı kaçırıyor**. Korpus taraması gösteriyor ki أَكْثَرُهُم dokuz ayette "
 "geçiyor (26:8, 67, 103, 121, 139, 158, 174, 190, 223) ve altısı standalone nakarat, ikisi gömülü "
 "(139, 158), biri farklı (223). **Nakarat sayımı 6 değil en az 8 olmalı.**"),
140: ("İkinci nakaratın beşinci geçişi. **Ama nakarat ÇİFTİ burada bozuluyor**: önceki dört konumda "
 "(26:8-9, 67-68, 103-104, 121-122) birinci nakarat AYRI BİR AYETTİ; burada 26:139'a gömülü. Yani "
 "çift yapısı Hûd kıssasının sonunda değişiyor — **ölçülebilir bir mimari kırılma**. rab z=3,94 "
 "beş ayette de aynı. Sûrenin on mühründen beşincisi ve mühür GEÇERLİ; mühürlü konumlar sûre 25'te "
 "de temiz çıkmıştı (aday 501/598) ve sûre 26'da beş mühürlü konumun beşi de geçerli."),
}

ATLAMA = {
 "_mercek_26_131_140": ("26:131 ve 26:140 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. İkisi de NAKARAT: "
  "26:131 dördüncü kümenin dördüncü geçişi (allah z=6,14), 26:140 ikinci kümenin beşinci geçişi "
  "(rab z=3,94). Bağımsız gözlem değil (adaylar 606, 683, 700)."),
 "_blok_notu_26_131_140": ("BLOK BİLANÇOSU: ★★★ 2 (26:131, 140) · ★★ 0 · ★ 0 · 8 ayet yıldızsız. "
  "**İKİ ★★★ AYETİN İKİSİ DE NAKARAT**; hiçbirinde çıpa yok. ÇIPA NOTU: 26:133-134 nimet listesi "
  "(davarlar, oğullar, bahçeler, pınarlar) çıpa TAŞIMIYOR — liste bir sayım, ne mekanizma ne ölçü "
  "ne süreç var; aday 561'in ölçütüyle 'adlandırma' düzeyinin altında. SÛRE 26'NIN OKUNAN 140 "
  "AYETİNDE ★★★ 29; çıpası olan tek ★★★ hâlâ 26:63. **ÖN-KAYIT (aday 685/696): Hûd kıssasında "
  "altı öğenin altısı da tamamlandı; ama örgü 26:108-110'dakinden FARKLI — araya Hûd'un üç "
  "suçlaması girdi. Ön-kayıt öğelerin VARLIĞINI doğru bildi, ARALIKLARINI öngörmedi.**"),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(131, 141):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 140/227.** Devam: 26:141'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-140 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1862
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(131, 141):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
