# -*- coding: utf-8 -*-
"""blok_26_61_70.py — sûre 26 dördüncü blok (26:61-70). Blok boyu ONA indirildi (biçim ihlâli önlemi)."""
import json
DIK = json.load(open('blok_dikey_26_61_70.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
61: "İki topluluk birbirini görünce Mûsâ'nın arkadaşları dedi: Bize yetiştiler.",
62: "Dedi: Hayır; Rabbim benimledir, bana yol gösterecek.",
63: "Mûsâ'ya vahyettik: Asânla denize vur. Deniz yarıldı ve her parça koca bir dağ gibi oldu.",
64: "Ötekileri de oraya yaklaştırdık.",
65: "Mûsâ'yı ve beraberindekilerin hepsini kurtardık.",
66: "Sonra ötekileri boğduk.",
67: "Bunda elbette bir âyet var; ama onların çoğu inanmıyor.",
68: "Rabbin, elbette o Azîz'dir, Rahîm'dir.",
69: "Onlara İbrâhîm'in haberini oku.",
70: "Hani babasına ve kavmine demişti: Neye tapıyorsunuz?",
}

O = {
61: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı مُوسَى *(Mûsâ)* 6. sırada, rol FAİL "
 "+ KONUŞAN** · edim haber, kip EMPH 1 · şahıs 2MS x1 · 3MS x1 · 1P x1, iltifât 0 · n=8 mora=54 "
 "harf=36 (n z=-0,47), fâsıla لَمُدْرَكُونَ *(yetişilenler)* → ن, N sınıfı; **i'râb NOM 4 · ACC 1 — "
 "blokta NOM'un en yüksek olduğu ayet**; bab I x1 · VI x1; zaman IMPF x1 · PERF x1; dış düğüm 0 · "
 "yıldız ★ yok · kökler رأي *(görme)* · جمع *(toplama)* · قول *(söz söyleme)* · صحب *(arkadaşlık; "
 "ehli)* · درك *(yetişme, erişme)* · bağ: **26:38, 39, 56 ile جمع *(toplama)* beşinci geçişi** — "
 "burada ilk kez İKİ topluluk (ٱلْجَمْعَانِ *(iki topluluk)*, tesniye) ve karşılıklı görme "
 "(تَرَٰٓءَا *(birbirini gördü)*, bab VI); kök sûrede beş ayette beş ayrı işlev (elle, L1, aday 639)"),
62: ("eksen: **lafız YOK · رَبّ *(Rab)* 5. sırada — on beşinci Rab**, **rab z=3,23: yıldızın TEK "
 "kaynağı** (n=6, oran 0,17) · esmâ yok · aktör yok · edim haber, kip FUT 1 · **şahıs 1S x3 · "
 "3MS x2**, iltifât 0 · n=6 mora=30 harf=21 (n z=-0,68), fâsıla سَيَهْدِينِ *(bana yol gösterecek)* → "
 "ن, N sınıfı; i'râb ACC 2 · NOM 1; bab I x2; zaman PERF x1 · IMPF x1; **biçim KELLA — sûrenin iki "
 "KELLA'sından ikincisi** (birincisi 26:15); dış düğüm 0 · **yıldız ★★★** · kökler قول *(söz "
 "söyleme)* · ربب *(rab, terbiye etme)* · هدي *(yol gösterme)* · bağ: **26:12 ile aynı yapı, ters "
 "duygu** — orada قَالَ رَبِّ إِنِّىٓ أَخَافُ *(dedi: Rabbim, korkuyorum)*, burada قَالَ كَلَّآ "
 "إِنَّ مَعِىَ رَبِّى *(dedi: hayır, Rabbim benimledir)*; aynı konuşan, aynı nida, korkudan güvene "
 "(elle, L1, aday 640)"),
63: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı مُوسَى *(Mûsâ)* 3. sırada rol "
 "mecrur; adsız 'ferîk' 11. sırada — ÖLÇÜM ARTEFAKTI (aday 462/579)**: 11. kelime فِرْقٍ *(parça, "
 "bölük)*, فرق *(ayırma, parçalara bölme)* kökü ve DENİZİN bir parçası; aktör dedektörü kökü "
 "'ferîk (topluluk)' sanmış. **Sûre 26 makro profilinde 'adsız aktör: ferîk' diye yazdığım kayıt "
 "GERİ ÇEKİLİYOR** — sûre 25'teki 'nefer' artefaktıyla AYNI SINIF, ikinci vaka · edim emir, kip "
 "IMPV 1 · şahıs 1P x2 · 2MS x2 · 3MS x2, iltifât 0 · n=13 mora=74 harf=59 (n z=0,06), fâsıla "
 "ٱلْعَظِيمِ *(koca, azametli)* → م, N sınıfı; **i'râb GEN 5 · ACC 1 · NOM 1**; bab I x2 · IV x1 · "
 "VII x1; zaman PERF x3 · IMPV 1; **HAPAKS: طود *(büyük dağ (tavd))* — korpusta TEK geçiş** "
 "(hapaks z=3,38: **yıldızın TEK kaynağı**); dış düğüm 0 · **yıldız ★★★** · kökler وحي *(vahiy, "
 "gizli bildirim)* · ضرب *(vurma; mesel getirme)* · عصو *(asâ, değnek)* · بحر *(deniz)* · فلق "
 "*(yarma, ikiye ayırma)* · كون *(olmak; mekân, yer)* · كلل *(hep, bütün)* · فرق *(ayırma, "
 "parçalara bölme)* · طود *(büyük dağ (tavd))* · عظم *(büyüklük, azamet; kemik)* · bağ: **25:1 ile "
 "فرق *(ayırma, parçalara bölme)* karşılaşması** — orada ٱلْفُرْقَان *(Furkān)* sûrenin adıydı ve "
 "sûrede TEK geçişti, burada aynı kök fiziksel bir yarılmanın parçası (elle, L1, aday 641)"),
64: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "1P x2 — ayette başka şahıs yok**, iltifât 0 · n=3 mora=23 harf=17 (n z=-1,00), fâsıla "
 "ٱلْءَاخَرِينَ *(ötekiler)* → ن, N sınıfı; **i'râb ACC 1**; bab IV x1; zaman PERF x1; dış düğüm 0 · "
 "yıldız ★ yok · kökler زلف *(yaklaştırma, zülfe)* · أخر *(geciktirme, sonraya bırakma)* · bağ: "
 "**26:66 ile aynı fâsıla** — ٱلْءَاخَرِينَ *(ötekiler)* iki ayet arayla iki kez; **زلف "
 "*(yaklaştırma, zülfe)* korpusta 10 geçişli ve dikey ölçümü ▸sonra حسن *(güzellik, iyilik)* x10,6 "
 "veriyor — kök korpusta ağırlıkla OLUMLU yaklaştırma (cennete), burada helâke yaklaştırma** "
 "(aday 529 sınıfı) (elle, L1, aday 642)"),
65: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı مُوسَى *(Mûsâ)* 2. sırada, rol "
 "FAİL** · edim haber, kip işareti yok · şahıs 1P x2 · 3MS x1, iltifât 0 · n=5 mora=33 harf=24 "
 "(n z=-0,79), fâsıla أَجْمَعِينَ *(hepsi)* → ن, N sınıfı — **26:49'un fâsılasıyla AYNI KELİME**; "
 "i'râb NOM 1 · ACC 2; bab IV x1; zaman PERF x1; dış düğüm 0 · yıldız ★ yok · kökler نجو *(kurtulma, "
 "kurtarma)* · جمع *(toplama)* · bağ: **26:49 ile fâsıla karşıtlığı** — orada أَجْمَعِينَ Firavun'un "
 "TEHDİT kapsamıydı (لَأُصَلِّبَنَّكُمْ أَجْمَعِينَ *(hepinizi asacağım)*), burada KURTULUŞ kapsamı "
 "(وَمَن مَّعَهُۥٓ أَجْمَعِينَ *(beraberindekilerin hepsi)*); aynı kelime, aynı konum, ters kutup "
 "(elle, L1, aday 643)"),
66: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "1P x2 — ayette başka şahıs yok**, iltifât 0 · n=3 mora=22 harf=16 (n z=-1,00), fâsıla "
 "ٱلْءَاخَرِينَ *(ötekiler)* → ن, N sınıfı — **26:64 ile aynı kelime**; **i'râb ACC 1**; bab IV x1; "
 "zaman PERF x1; **dış düğüm 1** · yıldız ★ yok · **esit: 37:82 ile TAM AYET ÖZDEŞ** · kökler غرق "
 "*(boğulma)* · أخر *(geciktirme, sonraya bırakma)* · bağ: **26:64 ile bitişik olmayan çift** — üç "
 "kelimelik iki ayet, aynı fâsıla, aynı bab IV, aynı 1P: يَاقْتَرَبَ *(yaklaştırdık)* ve "
 "أَغْرَقْنَا *(boğduk)*; **yaklaştırma ve boğma tek yapıda** (elle, L1, aday 642)"),
67: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُؤْمِن *(mümin)* 8. sırada = fâsıla — ARTEFAKT, "
 "sûrenin dördüncü مُؤْمِن tokeni** (aday 601) · aktör yok · edim haber, kip EMPH 1 · NEG 1 · şahıs "
 "3MS x1 · 3MP x1, **iltifât 1 — yön 1>3; sûrenin üçüncü iltifâtı** · n=8 mora=40 harf=32 "
 "(n z=-0,47), fâsıla مُّؤْمِنِينَ → ن, N sınıfı; i'râb ACC 3 · NOM 1; bab I x1; zaman PERF x1; "
 "**açık sayı sözcüğü: كثر *(çokluk)* → أَكْثَر *(çoğu)***; **NAKARAT alanı = 6, temsil ayet 26:8**; "
 "**esit: 26:8, 103, 121, 174, 190 ile TAM AYET ÖZDEŞ** · dış düğüm 0 · yıldız ★ yok · kökler أيي "
 "*(âyet, işaret)* · كون *(olmak; mekân, yer)* · كثر *(çokluk)* · أمن *(güven; iman)* · bağ: "
 "**sûrenin birinci nakaratının ikinci geçişi; ilki 26:8'de ve arada elli dokuz ayet var** "
 "(elle, L1, aday 606)"),
68: ("eksen: **lafız YOK · رَبّ *(Rab)* 2. sırada — on altıncı Rab**, **rab z=3,94: yıldızın TEK "
 "kaynağı** (n=5, oran 0,20) · **esmâ عَزِيز *(azîz)* 4. + رَحِيم *(rahîm)* 5. sırada = fâsıla — "
 "MÜHÜR; GEÇERLİ; sûrenin on mühründen ikincisi** · aktör yok · edim haber, kip EMPH 1 · şahıs "
 "2MS x1 · 3MS x1, iltifât 0 · n=5 mora=28 harf=21 (n z=-0,79), fâsıla ٱلرَّحِيمُ → م, N sınıfı; "
 "**i'râb ACC 2 · NOM 2; fiil YOK**; **NAKARAT alanı = 8, temsil ayet 26:9**; **esit: 26:9, 104, "
 "122, 140, 159, 175, 191 ile TAM AYET ÖZDEŞ** · dış düğüm 0 · **yıldız ★★★** · kökler ربب *(rab, "
 "terbiye etme)* · عزز *(izzet, üstünlük)* · رحم *(rahmet, merhamet)* · bağ: **26:9 ile nakarat "
 "çifti ikinci kez; 26:67-68 ikilisi 26:8-9 ikilisinin birebir tekrarı** (elle, L1, aday 606)"),
69: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı إِبْراهِيم *(İbrâhîm)* 4. sırada, "
 "rol mecrur — sûrenin ikinci kıssası açılıyor** · edim emir, kip IMPV 1 · şahıs 2MS x1 · 3MP x1, "
 "iltifât 0 · n=4 mora=22 harf=18 (n z=-0,89), fâsıla إِبْرَٰهِيمَ *(İbrâhîm)* → م, N sınıfı — "
 "**fâsıla bir ÖZEL AD ve sınıfa uyuyor** (26:13 هَٰرُونَ, 26:48 هَٰرُونَ ile aynı sınıf); i'râb "
 "ACC 1 · GEN 1; bab I x1; zaman IMPV 1; dış düğüm 0 · yıldız ★ yok · kökler تلو *(okuma, ardından "
 "gelme)* · نبأ *(haber)* · bağ: **26:6 ile نبأ *(haber)* ikinci geçişi** — orada أَنۢبَٰٓؤُا۟ مَا "
 "كَانُوا۟ بِهِۦ يَسْتَهْزِءُونَ *(alay ettiklerinin haberleri)* tehdit, burada نَبَأَ إِبْرَٰهِيمَ "
 "*(İbrâhîm'in haberi)* anlatı (elle, L1, aday 644)"),
70: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — أَب *(baba)* ve قَوْم *(kavim)* "
 "adlandırılmıyor · edim haber, kip işareti yok · şahıs 3MS x3 · 2MP x2, iltifât 0 · n=6 mora=29 "
 "harf=24 (n z=-0,68), fâsıla تَعْبُدُونَ *(tapıyorsunuz)* → ن, N sınıfı; **i'râb GEN 2**; bab I x2; "
 "zaman PERF x1 · IMPF x1; dış düğüm 1 · yıldız ★ yok · kökler قول *(söz söyleme)* · أبو *(baba)* · "
 "قوم *(kalkma; kavim; kıyamet)* · عبد *(kul, kulluk)* · bağ: xref أب *(baba)* + قوم *(kavim)* + "
 "عبد *(kulluk)* → **37:85**; **26:18 ile أبو *(baba)* karşılaştırması** — orada Firavun ata-oğul "
 "ilişkisini bir BORÇ olarak kuruyordu (نُرَبِّكَ *(seni yetiştirdik)*), burada İbrâhîm babasına "
 "SORU soruyor (elle, L1, aday 645)"),
}

M = {
61: ("İki topluluğun karşılaşması bir görme fiiliyle veriliyor ve fiil KARŞILIKLI: تَرَٰٓءَا "
 "ٱلْجَمْعَانِ *(iki topluluk birbirini gördü)*, رأي *(görme)* bab VI ve özne tesniye. Ölçülebilir "
 "bir kök işlevi: جمع *(toplama)* sûrede beşinci kez ve beşinci işleviyle — 26:38 edilgen fiil, "
 "26:39 etken ism-i fâil, 26:49 pekiştirme (أَجْمَعِينَ), 26:56 sıfat (جَمِيع), burada TESNİYE İSİM "
 "(ٱلْجَمْعَانِ). Beş ayet, beş biçim. Ve درك *(yetişme, erişme)* korpusta 12 geçişli; dikey ölçümü "
 "▸önce hiçbir komşu vermiyor, ▸sonra بصر *(görme)* x12,4 — kök korpusta görme alanına bağlı ve "
 "burada da öyle. Sekiz kelimede NOM dört: karşılaşma cümlesi isim ağırlıklı."),
62: ("Cevap bir KELLA ile açılıyor — sûrenin iki KELLA'sından ikincisi (birincisi 26:15'te, orada "
 "da Mûsâ'ya cevaptı). Ölçülebilir bir duygu tersliği: 26:12'de aynı konuşan aynı nidayla قَالَ "
 "رَبِّ إِنِّىٓ أَخَافُ *(dedi: Rabbim, korkuyorum)* diyordu; burada قَالَ كَلَّآ إِنَّ مَعِىَ "
 "رَبِّى *(dedi: hayır, Rabbim benimledir)* — korkudan güvene, elli ayet arayla. Ve fiil geleceğe "
 "atıyor: سَيَهْدِينِ *(bana yol gösterecek)*, FUT; هدي *(yol gösterme)* korpusta 316 geçişli ve "
 "dikey ölçümü ▸önce ضلل *(sapma, saptırma)* x3,7 veriyor — kök korpusta karşıtıyla birlikte, "
 "burada karşıtı yok. Altı kelimede 1S üç kez."),
63: ("Emir tek fiille veriliyor ve nesnesi asâ: ٱضْرِب بِّعَصَاكَ ٱلْبَحْرَ *(asânla denize vur)*. "
 "ضرب *(vurma; mesel getirme)* korpusta 58 geçişli ve dikey ölçümü ▸sonra mesel x33,8 · عصو *(asâ, "
 "değnek)* x28,6 veriyor — kök korpusta ağırlıkla 'mesel getirme', burada fiziksel vurma; ikinci "
 "komşu bu sahneden geliyor. Sonuç iki aşamalı: فَٱنفَلَقَ *(yarıldı)*, فلق *(yarma, ikiye "
 "ayırma)* bab VII, korpusta 4 geçişli; sonra bir ölçek benzetmesi — كُلُّ فِرْقٍ كَٱلطَّوْدِ "
 "ٱلْعَظِيمِ *(her parça koca bir dağ gibi)*, طود *(büyük dağ (tavd))* korpusta TEK geçiş ve "
 "yıldızın tek kaynağı. Ve فرق *(ayırma, parçalara bölme)* burada fiziksel bir parça; 25:1'de aynı "
 "kök ٱلْفُرْقَان *(Furkān)* olarak bir kitabın adıydı ve o sûrede tek geçişti."),
64: ("Üç kelime ve tek fiil: وَأَزْلَفْنَا ثَمَّ ٱلْءَاخَرِينَ *(ötekileri de oraya yaklaştırdık)*. "
 "زلف *(yaklaştırma, zülfe)* korpusta 10 geçişli ve dikey ölçümü ▸sonra حسن *(güzellik, iyilik)* "
 "x10,6 veriyor — **kök korpusta ağırlıkla OLUMLU yaklaştırma bağlamında (cennetin yaklaştırılması)**, "
 "burada helâke yaklaştırma; kök düzeyi dikey komşuluk bu kutup farkını göstermiyor (aday 529 "
 "sınıfı). Ölçülebilir bir örtüşme: ayet 26:66 ile aynı fâsılayı (ٱلْءَاخَرِينَ *(ötekiler)*), aynı "
 "uzunluğu (n=3), aynı babı (IV) ve aynı şahsı (1P x2) paylaşıyor — iki ayet arayla iki eşyapılı "
 "cümle: yaklaştırma ve boğma."),
65: ("Kurtarma tek fiille ve kapsamı bir pekiştirmeyle: وَمَن مَّعَهُۥٓ أَجْمَعِينَ *(beraberindekilerin "
 "hepsi)*. Ölçülebilir bir fâsıla karşıtlığı: 26:49'da Firavun لَأُصَلِّبَنَّكُمْ أَجْمَعِينَ "
 "*(hepinizi asacağım)* demişti — aynı kelime, aynı fâsıla konumu, tehdit kapsamı; burada kurtuluş "
 "kapsamı. On altı ayet arayla aynı kelime iki kutupta. نجو *(kurtulma, kurtarma)* korpusta 84 "
 "geçişli ve dikey ölçümü ▸sonra كرب *(sıkıntı, keder)* x86,8 · geride-kalan x74,4 veriyor — kök "
 "korpusta 'sıkıntıdan kurtarma' ve 'geride kalanlar' ile eşleşiyor; ikincisi tam bir sonraki "
 "ayetin konusu."),
66: ("Üç kelime ve tek fiil: ثُمَّ أَغْرَقْنَا ٱلْءَاخَرِينَ *(sonra ötekileri boğduk)*. Ayet 37:82 "
 "ile TAM AYET ÖZDEŞ ve esit alanı yakalıyor. Ölçülebilir bir eşyapı: 26:64 ile aynı uzunluk (n=3), "
 "aynı fâsıla (ٱلْءَاخَرِينَ *(ötekiler)*), aynı bab (IV), aynı şahıs (1P x2) — iki ayet iki fiille "
 "ayrılıyor: أَزْلَفْنَا *(yaklaştırdık)* ve أَغْرَقْنَا *(boğduk)*. Yaklaştırma ve boğma tek "
 "kalıpta. غرق *(boğulma)* korpusta 23 geçişli ve dikey ölçümü ▸önce فلك *(gemi, felek)* x36,1 · "
 "kurtuluş x13,5 veriyor — 'kurtuluş' komşuluğu bir önceki ayetten geliyor, yani çift korpusta "
 "sabit."),
67: ("Sûrenin birinci nakaratı ikinci kez ve arada elli dokuz ayet var (26:8 → 26:67). Ölçülebilir "
 "bir yapı: defter.json nakarat alanı 6, temsil ayet 26:8, ve esit alanı beş ayeti gösteriyor. "
 "**Bu, sûre 26'nın nakarat mimarisinin ilk kapanışı**: 26:8-9 çifti kıssanın ÖNÜNDE duruyordu, "
 "26:67-68 çifti kıssanın ARKASINDA — aynı iki ayet, iki konumda. Ve sûrenin üçüncü iltifâtı "
 "burada (yön 1>3): anlatı birinci çoğuldan üçüncü şahsa geçiyor, tam nakarata girerken."),
68: ("Beş kelime, hiç fiil yok, ve nakarat çiftinin ikinci terimi. rab z=3,94 — 26:9 ile birebir "
 "aynı değer, çünkü ayet birebir aynı. **Ölçülebilir bir bağımsızlık sorunu: 26:9 ve 26:68 AYNI "
 "AYET ve İKİSİ DE ★★★; sûrenin 41 ★★★ ayetinin sekizi bu tek nakarattan geliyor** (aday 606). "
 "Sûrenin on mühründen ikincisi ve mühür GEÇERLİ — sûre 25'in tam denetiminde de iki mühürlü konum "
 "geçerli çıkmıştı (aday 598). Mühür sinyali sûre 26'da da tutuyor gibi görünüyor ama tam denetim "
 "sûre sonunda yapılacak."),
69: ("Dört kelime ve sûrenin ikinci kıssası açılıyor. Ölçülebilir bir geçiş biçimi: emir kipiyle "
 "(وَٱتْلُ *(oku)*) ve muhatabı anlatının dışındaki elçi — Mûsâ kıssası bir nakaratla kapandı, "
 "İbrâhîm kıssası bir emirle açılıyor. تلو *(okuma, ardından gelme)* korpusta 63 geçişli ve dikey "
 "ölçümü ▸sonra hikmet x28,6 · arınma x16,9 veriyor — kök korpusta ağırlıkla kitap okuma bağlamında. "
 "Ve نبأ *(haber)* 26:6'dan geri geliyor: orada tehdit (alay ettiklerinin haberleri gelecek), burada "
 "anlatı malzemesi. Fâsıla bir özel ad ve م ile bitip sınıfa uyuyor."),
70: ("Kıssa bir soruyla açılıyor ve soru en kısa biçimde: مَا تَعْبُدُونَ *(neye tapıyorsunuz)*. "
 "Ölçülebilir bir adsızlık: baba ve kavim adlandırılmıyor (أَبِيهِ وَقَوْمِهِ *(babasına ve "
 "kavmine)*), yalnız ilişkiyle veriliyor — aktör tablosu ikisini de almıyor. عبد *(kul, kulluk)* "
 "korpusta 275 geçişli ve dikey ölçümü ▸sonra صنم *(put, sanem)* x16,6 · tâğût x13,8 veriyor — "
 "kökün korpustaki komşuluğu tam bu sahnenin konusu, yani terkip bu ayete özgü değil. Ve أبو "
 "*(baba)* 26:18'den geri geliyor: orada Firavun ata-oğul ilişkisini bir BORÇ olarak kurmuştu, "
 "burada İbrâhîm o ilişkiyi bir SORUYLA açıyor."),
}

ATLAMA = {
 "_mercek_26_62": ("26:62 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. قَالَ كَلَّآ إِنَّ مَعِىَ رَبِّى "
  "سَيَهْدِينِ. Tek kaynak rab z=3,23 (n=6, oran 0,17). İçerik bir güven bildirimi."),
 "_mercek_26_63": ("26:63 ★★★ — 🜁 ve 🜂 YAZILMADI. **AMA GEREKÇE YENİ VE ÖNCEKİLERDEN FARKLI: ÇIPA "
  "VAR, MERCEK SINIFINA DÜŞMÜYOR.** Ayet fiziksel bir olay veriyor (فَٱنفَلَقَ *(yarıldı)*, فلق "
  "*(yarma, ikiye ayırma)* bab VII) ve bir ÖLÇEK BENZETMESİ ekliyor (كُلُّ فِرْقٍ كَٱلطَّوْدِ "
  "ٱلْعَظِيمِ *(her parça koca bir dağ gibi)*). Bu, aday 561'in önerdiği çıpa ölçütünün 'adlandırma "
  "+ nitelik' düzeyine girer — 25:61'in (burçlar, kandil, aydınlatan ay) düzeyiyle aynı. ANCAK iki "
  "uzman merceği BİYOLOG ve UZAY; olay ne biyolojik ne astronomik. Bir su kütlesinin yarılması "
  "jeofizik/hidrodinamik alanına düşer ve BU PROJEDE MERCEK SINIFI YOK. Mercek yazmak için üçüncü "
  "bir sınıf açmak gerekirdi; AÇILMADI. **BU, OKUMADA İLK KEZ GÖRÜLEN ATLAMA GEREKÇESİ SINIFIDIR** "
  "(aday 646): önceki tüm atlamalar 'çıpa yok' gerekçesiyleydi. SINIR AYRICA YAZILIR: ayet ölçek "
  "için bir BENZETME veriyor (dağ gibi), sayı ya da ölçü vermiyor; 'denizin yarılmasının fiziği' "
  "üzerine hiçbir şey söylenmedi ve söylenmeyecek — yasaklı 'bilimsel izdüşüm'."),
 "_mercek_26_68": ("26:68 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. Nakarat ayeti (26:9'un birebir "
  "tekrarı). Tek kaynak rab z=3,94. **26:9 ile AYNI AYET VE İKİSİ DE ★★★ — bağımsız gözlem değil** "
  "(aday 606)."),
 "_blok_notu_26_61_70": ("BLOK BOYU ONA İNDİRİLDİ. Gerekçe: 26:41-60 bloğunda on altı ayet sohbete "
  "tam kipte yazılamayıp özete sıkıştırıldı (biçim ihlâli, kullanıcı uyarısıyla düzeltildi). "
  "YAPILACAKLAR'a 'BİÇİM İHLÂLİ KAYDI' başlığıyla yazıldı; önlem: çıktı hacmi tam kipi "
  "kaldırmıyorsa özete kayılmaz, BLOK BÖLÜNÜR. Sûre 26'nın kalan blokları ON ayet. "
  "BLOK BİLANÇOSU: ★★★ 3 (26:62, 63, 68) · ★★ 0 · ★ 0 · 7 ayet yıldızsız. Kaynaklar: rab x2, "
  "hapaks x1. 26:63 DIŞINDA hiçbirinde çıpa yok; 26:63'te çıpa var ama mercek sınıfına düşmüyor "
  "(yukarıda). SÛRE 26'NIN OKUNAN 70 AYETİNDE ★★★ 14; **çıpası olan tek ★★★ ayet 26:63** ve o da "
  "yıldızını çıpadan değil hapakstan alıyor."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(61, 71):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['26']['_makro']['aktor'] = OM['26']['_makro']['aktor'].replace(
    "Adsız: ferîk *(bir bölük)* 1 — **sûre 25'in 'nefer' artefaktından sonra bu kayıt da okuma "
    "sırasında DENETLENECEK** (aday 579).",
    "Adsız: **YOK. GERİ ÇEKİLDİ: 'ferîk *(bir bölük)* 1' kaydı ÖLÇÜM ARTEFAKTIDIR** — 26:63'ün 11. "
    "kelimesi فِرْقٍ *(parça, bölük)*, فرق *(ayırma, parçalara bölme)* kökü ve DENİZİN bir parçası; "
    "aktör dedektörü kökü 'ferîk (topluluk)' sanmış. Sûre 25'teki 'nefer' artefaktıyla AYNI SINIF, "
    "ikinci vaka (adaylar 462, 579, 641).")
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 70/227.** Devam: 26:71'den. "
                         "NOT: blok boyu ONA indirildi (biçim ihlâli önlemi).")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-70 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1792
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(61, 71):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
