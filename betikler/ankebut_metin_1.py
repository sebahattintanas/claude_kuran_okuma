# -*- coding: utf-8 -*-
"""ankebut_metin_1.py — sûre 29 meal ve matematikçi merceği (29:1-35).
Ölçüm satırı burada YOK: defterden üretilir (olcum_bicim.py)."""

MEAL = {
1: "Elif-Lâm-Mîm.",
2: "İnsanlar, \"İnandık\" demeleriyle, sınanmadan bırakılacaklarını mı sandılar?",
3: "Andolsun, onlardan öncekileri de sınadık. Allah, doğru söyleyenleri de elbette bilecek, yalancıları da elbette bilecek.",
4: "Yoksa kötülük işleyenler bizi geçeceklerini mi sandılar? Ne kötü hüküm veriyorlar!",
5: "Kim Allah'a kavuşmayı umuyorsa, Allah'ın belirlediği süre elbette gelecektir. O, işitendir, bilendir.",
6: "Kim cihad ederse ancak kendisi için cihad etmiş olur. Şüphesiz Allah, âlemlerden müstağnîdir.",
7: "İnanıp iyi işler yapanların kötülüklerini elbette örteceğiz ve onları yaptıklarının en güzeliyle elbette ödüllendireceğiz.",
8: "İnsana, anne babasına iyi davranmasını emrettik. Ama hakkında bilgin olmayan bir şeyi bana ortak koşman için seninle uğraşırlarsa, onlara itaat etme. Dönüşünüz banadır; yaptıklarınızı size haber vereceğim.",
9: "İnanıp iyi işler yapanları elbette iyilerin arasına katacağız.",
10: "İnsanlardan öylesi vardır ki, \"Allah'a inandık\" der; ama Allah uğrunda eziyet görünce insanların fitnesini Allah'ın azabı gibi sayar. Rabbinden bir yardım gelirse, \"Biz sizinle beraberdik\" derler. Allah, âlemlerin göğüslerindekini en iyi bilen değil mi?",
11: "Allah, inananları elbette bilecek; iki yüzlüleri de elbette bilecek.",
12: "İnkâr edenler inananlara, \"Bizim yolumuza uyun, sizin günahlarınızı biz yüklenelim\" dediler. Oysa onların günahlarından hiçbir şey yüklenecek değillerdir; onlar yalancıdır.",
13: "Elbette kendi yüklerini, o yüklerle birlikte başka yükleri de taşıyacaklar ve kıyamet günü uydurdukları şeylerden elbette sorguya çekilecekler.",
14: "Andolsun, Nûh'u kavmine gönderdik; aralarında elli yıl eksiğiyle bin yıl kaldı. Sonunda onlar zulmederken tufan kendilerini yakaladı.",
15: "Onu ve gemidekileri kurtardık; o gemiyi âlemler için bir ibret kıldık.",
16: "İbrâhîm'i de gönderdik. Kavmine şöyle demişti: \"Allah'a kulluk edin ve O'ndan sakının; bilirseniz bu sizin için daha hayırlıdır.\"",
17: "\"Siz Allah'tan başka sadece putlara tapıyor ve bir yalan uyduruyorsunuz. Allah'tan başka taptıklarınızın size rızık vermeye güçleri yetmez. Rızkı Allah katında arayın, O'na kulluk edin ve O'na şükredin; O'na döndürüleceksiniz.\"",
18: "Eğer yalanlarsanız, sizden önceki ümmetler de yalanlamıştı. Elçiye düşen, ancak apaçık tebliğdir.",
19: "Görmediler mi, Allah yaratmayı nasıl başlatıyor, sonra onu nasıl tekrarlıyor? Bu, Allah'a kolaydır.",
20: "De ki: \"Yeryüzünde gezin de yaratmayı nasıl başlattığına bakın. Sonra Allah son yaratmayı da inşa edecektir. Şüphesiz Allah her şeye gücü yetendir.\"",
21: "Dilediğine azap eder, dilediğine merhamet eder; O'na döndürüleceksiniz.",
22: "Siz ne yerde ne gökte âciz bırakabilirsiniz. Allah'tan başka bir dostunuz ve yardımcınız da yoktur.",
23: "Allah'ın âyetlerini ve O'na kavuşmayı inkâr edenler — işte onlar benim rahmetimden ümit kesmişlerdir; onlar için acı bir azap vardır.",
24: "Kavminin cevabı, \"Onu öldürün ya da yakın\" demekten başka bir şey olmadı. Allah onu ateşten kurtardı. Bunda inanan bir topluluk için elbette işaretler vardır.",
25: "Dedi ki: \"Siz, dünya hayatında aranızdaki sevgi yüzünden Allah'tan başka putlar edindiniz. Sonra kıyamet günü kiminiz kiminizi inkâr edecek, kiminiz kiminize lânet edecek. Varacağınız yer ateştir ve hiçbir yardımcınız yoktur.\"",
26: "Bunun üzerine Lût ona inandı. İbrâhîm, \"Ben Rabbime hicret ediyorum; O, güçlüdür, hikmet sahibidir\" dedi.",
27: "Ona İshâk'ı ve Ya'kûb'u bağışladık; soyuna peygamberliği ve kitabı verdik. Ücretini dünyada verdik; âhirette de o, elbette iyilerdendir.",
28: "Lût'u da gönderdik. Kavmine şöyle demişti: \"Siz gerçekten, âlemlerden hiç kimsenin sizden önce yapmadığı bir hayâsızlığı işliyorsunuz.\"",
29: "\"Siz gerçekten erkeklere yönelip yol kesiyor, toplantılarınızda çirkinlik yapıyor musunuz?\" Kavminin cevabı, \"Doğru söyleyenlerdensen bize Allah'ın azabını getir\" demekten başka bir şey olmadı.",
30: "\"Rabbim, bozguncu topluluğa karşı bana yardım et\" dedi.",
31: "Elçilerimiz İbrâhîm'e müjdeyle geldiklerinde, \"Biz şu şehrin halkını helâk edeceğiz; oranın halkı zalim kimselerdir\" dediler.",
32: "\"Orada Lût var\" dedi. \"Orada kimin bulunduğunu biz daha iyi biliriz. Onu ve ailesini elbette kurtaracağız — karısı hariç; o geride kalanlardan olacak\" dediler.",
33: "Elçilerimiz Lût'a geldiklerinde onların yüzünden kaygılandı, göğsü daraldı. \"Korkma, üzülme; seni ve aileni elbette kurtaracağız — karın hariç; o geride kalanlardan olacak\" dediler.",
34: "\"Biz, bu şehrin halkı üzerine, yoldan çıkmaları sebebiyle gökten bir azap indireceğiz.\"",
35: "Andolsun, akleden bir topluluk için orada apaçık bir işaret bıraktık.",
}

M = {
1: ("**`esit2`'nin okumada gördüğü en geniş TAM kümesi.** TAM SAYIM: iskeleti tek başına `الم` olan ayet "
    "korpusta **altı** (2:1, 3:1, 29:1, 30:1, 31:1, 32:1) ve alan beşini birden bağlıyor. Mukattaa kümeleri: "
    "`حم` 7 · **`الم` 6** · `طسم` 2 · dördü birer. **Sûre 28 korpusun en küçük kümesiyle açılmıştı, sûre 29 "
    "ikinci büyüğüyle.** `harf`/`harf3` farkı yine 19 ve oran 0,136 — onarılmış alan ikinci sûrede de aynı "
    "değeri veriyor, yani besmele kirliliği sabit ve ölçülebilir."),
2: ("Sûre 28'de 28:78 ve 28:80'in verdiği birebir aynı değer burada üçüncü kez: iki edilgen fiil, beş toplam "
    "fiil, z=1,95, ★. **Üç ayet, üç ayrı sûre bölütü, aynı oran, aynı nişan — `pas` ölçütünün deterministik "
    "olduğunun temiz gösterimi.** İçerik tarafında ölçülebilir olan şey ikisi de edilgen olan fiillerin "
    "**fâilinin silinmiş olması**: kim bırakmıyor, kim sınıyor — ayet söylemiyor ve `pas` alanı tam da bunu "
    "sayıyor."),
3: ("**Beş te'kid işareti tek ayette** — sûre 28'de `EMPH` yedi ayete dağılmıştı ve tek ayetteki tavan ikiydi "
    "(28:87). Burada beş, ve hepsi aynı yapıdan: `وَلَقَدْ` · `فَلَيَعْلَمَنَّ` · `وَلَيَعْلَمَنَّ`. `علم` iki "
    "kez ve **ikisi de birebir aynı çekimde**, yalnız nesneleri karşıt (doğru söyleyenler / yalancılar); "
    "`ikile` sayıyor ama karşıtlık yönünü tutmuyor. Ayet yıldızsız: `allah` z=1,29, eşiğin altında."),
4: ("`حسب` kökü sûrede iki geçişli ve **ikisi de bu iki ardışık ayette, ikisi de aynı soru kalıbında**: "
    "`أَحَسِبَ ٱلنَّاسُ` (29:2) / `أَمْ حَسِبَ ٱلَّذِينَ` (29:4). **Kökün sûredeki bütün varlığı iki ayete "
    "sıkışmış ve ikisi de aynı retorik soruyu kuruyor** — arada 29:3 bir cevap cümlesi olarak duruyor. "
    "`nakarat2` bunu görmüyor: ortak dizi iki kelimeye ulaşmıyor ve alanın alt sınırı üç. **Sûre 28'de sekiz "
    "kez kaydedilen 'alt sınırın altında kalan tekrar' burada sûre 29'un ilk vakası.**"),
5: ("**Okumada ölçülen en yüksek `allah` z değeri** ve sûre 28'in tavanını (28:77, z=1,78) belirgin biçimde "
    "aşıyor — orada üç lafız yirmi altı kelimedeydi, burada iki lafız on iki kelimede. **Payda yine "
    "belirleyici.** Esmâ tarafında sûrenin ilk mühürlü tokeni ve **geçerli**: `ٱلسَّمِيعُ ٱلْعَلِيمُ` çifti, "
    "gönderge `هُوَ`, mercii lafza-i celâl. Sûre 27'de 12/12, sûre 28'de 2/2 geçerliydi; **üçüncü sûrede de "
    "yanlış pozitif yok.**"),
6: ("**Payda etkisinin bu blokta en ince örneği: `allah` z=1,47 ve eşik 1,5.** On kelimede bir lafız; 29:3'te "
    "on bir kelimede bir lafız z=1,29 vermişti, burada bir kelime kısalınca 1,47'ye çıkıyor ve **hâlâ 0,03 "
    "farkla geçemiyor.** Esmâ tarafında önemli: `غَنِيّ` **mühürsüz ama göndergesi doğrudan `اللَّه` — "
    "GEÇERLİ**; sûre 28'de mühürsüz geçerli token ikiydi ve ikisi de son konumdaydı, bu da son konumda ve "
    "sûre 29'un ilk mühürsüz geçerlisi."),
7: ("**Sûre 29'un ilk süzgeç-geçen kalıbı ve iki ölçütü birden sağlıyor:** dört kelime *ve* üç ayet. Sûre "
    "28'de süzgeci geçen on bir kalıbın çoğu ya kelime ya ayet ölçütünden geçiyordu; **ikisini birden "
    "sağlayan ilk kalıp bu.** İkinci not: dört `EMPH` ve ikisi de aynı yapıdan. `عمل` iki kez ve ayetin iki "
    "ucunda: başta yapılan iyi işler, sonda yapageldikleri — **aynı kök, aynı özne, biri nitelik biri "
    "karşılık.**"),
8: ("**Sekiz ayrı şahıs işareti — okumanın tavanı.** Sûre 28'in en dağınığı altıydı. Sebep ölçülebilir: ayet "
    "üç ayrı muhatap katmanı taşıyor — anlatıcı (1P/1S), muhatap birey (2MS), anne baba (3MD/3D) ve genel "
    "topluluk (2MP). **`sahset` bunu üçe indiriyor, `sah` sekizi de tutuyor; iki alan aynı olguyu farklı "
    "çözünürlükte ölçüyor.** Bağ tarafında: dört xref 3-gram'ın **üçü 31:15'e** düşüyor, yani ayet neredeyse "
    "bütünüyle Lokmân sûresindeki bir ayet çiftiyle örtüşüyor, **ama `esit2` boş** — sûre 28'de 28:31↔27:10 "
    "ve 28:47↔20:134'te kaydedilen aynı desen."),
9: ("**Yedi kelimede aynı kök iki kez ve ikisi ayetin iki ucunda:** `ٱلصَّٰلِحَٰتِ` (yapılan işler) ve "
    "`ٱلصَّٰلِحِينَ` (katılacak topluluk) — **aynı kök, biri eylem biri kişi, biri şart biri sonuç.** Sûre "
    "28'de 28:77'nin `ٱلْفَسَادَ`/`ٱلْمُفْسِدِين` çifti birebir aynı yapıdaydı, karşıt kutupta. Blokun en kısa "
    "ayeti ve üç dış düğüm taşıyor — **kısalıkla bağlılık arasında ilişki olmadığının vakası.**"),
10: ("**Blokun kapanışı dört kökü birden ikiliyor** — `أله` ×4, `أنس` ×2, `قول` ×2, `علم` ×2. Sûre 28'de dört "
     "kök ikilemesi iki ayette görülmüştü ve ikisi de karşıt çiftler kuruyordu; burada yapı farklı: **dördü de "
     "aynı kişiyi iki ayrı durumda gösteriyor** — eziyet anında ve yardım anında. TAM SAYIM: `أله` kökünü bir "
     "ayette 4+ kez taşıyan ayet korpusta **46**; 29:10 sûredeki ilk örnek. **GEN 10** — okumada ölçülen en "
     "yüksek cer yükü. Ve `n` ile `allah` **ikisi birden eşiği geçiyor** (1,97 ve 2,05) ama formül toplamıyor: "
     "28:50 ve 28:68'de iki ölçüt birden eşiğe *yaklaşıp* ikisi de geçememişti, **burada tersi.**"),
11: ("**Payda mekanizmasının okumada gösterilebilecek en temiz hâli.** 29:5'te **iki** lafız on iki kelimede, "
     "burada **bir** lafız altı kelimede — oran ikisinde de 1/6 ve `allah` z'si ikisinde de **tam olarak "
     "2,80.** İki ayet, farklı uzunluk, farklı token sayısı, **aynı oran → aynı z → aynı yıldız.** İkincisi: "
     "29:3'ün yapısı burada birebir tekrarlanıyor — sekiz ayet arayla, aynı fiil, aynı te'kid, karşıt nesne "
     "çiftiyle; `nakarat2` kalıbı görüyor ama süzgeçten geçiremiyor."),
12: ("**İki kök birden ikileniyor ve ikisi de aynı cümlede olumlanıp olumsuzlanıyor:** `وَلْنَحْمِلْ "
     "خَطَٰيَٰكُمْ` (emir, olumlu teklif) / `وَمَا هُم بِحَٰمِلِينَ` (olumsuz, red). `حمل` biri fiil biri "
     "ism-i fâil, `خطأ` ikisi de isim ama biri 'sizin' biri 'onların'. Sûre 28'de 28:77'nin `ٱبْتَغِ`/`لَا "
     "تَبْغِ` çifti aynı yapıdaydı; **burada iki kök birden.** `خطأ` kökü sûrede iki geçişli ve **ikisi de bu "
     "ayette** — kök tek ayette tükeniyor."),
13: ("**`ثقل` kökü üç kez ve üçü de aynı kelimede farklı iyelikle.** Kök sûrede üç geçişli ve üçü de bu tek "
     "ayette: **kök tek ayette tükeniyor** (29:12'de `خطأ` ile aynı desen, ardışık ayetlerde iki kez). Ve bir "
     "önceki ayetin reddettiği şey burada olumlanıyor: `وَمَا هُم بِحَٰمِلِينَ` → `وَلَيَحْمِلُنَّ`. **`حمل` "
     "kökü iki ardışık ayette üç kez ve yönü tersine dönüyor**; ölçüm bunu `sûre_geçiş` sayacında yan yana "
     "tutuyor, karşıtlığı tutmuyor."),
14: ("**ÇIPA — KADEME L4, olgu = evet. Okumada ölçülen İLK L4 kaydı.** `أَلْفَ سَنَةٍ إِلَّا خَمْسِينَ عَامًا` "
     "— bir süre **birimli bir nicelikle** veriliyor, üstelik iki ayrı birim adıyla (`سَنَة`, `عام`) ve bir "
     "çıkarma işlemiyle. L4 tanımı: *'MEKANİZMA/ÖLÇÜ/SINIF — süreç nasıl işliyor, hangi birimle'*. Sûre 27'de "
     "27:39 ve 27:40 **birim olmadığı için** L1'de kalmıştı; **bu ayet tam o eksiği kapatıyor.** 🜁 YAZILDI — "
     "P0 #6 kararı gereği sembol ★★★ koşuluna bağlı değil ve ayet yıldızsız. **Tarayıcı bu ayeti KAÇIRDI** "
     "(`سنو`/`عوم`/`ألف` olgu kök listesinde yok, ölçü işaret ailesi yok) → `F_ölçü` ailesi eklendi. `عوم` "
     "kökünün tablo karşılığı 'yüzme' ama lemma `عام` (yıl): **P0 #5 vakası ve tam da ölçü alanında.**"),
15: ("**`سفن` korpusun en dar köklerinden: üç ayet.** Altı kelimelik ayette iki kök sûrede tek geçişli ve biri "
     "korpusta üç ayetlik; buna karşılık `hapaks` alanı boş — **28:12'de kaydedilen 'nadirlik yığılması ile "
     "hapaks ayrı şeyler' ayrımının sûre 29'daki ilk vakası.** Dört birinci-çoğul işareti ve `bask`=1 — "
     "sûrenin ilk on beş ayetinde baskın şahsın 1 olduğu tek ayet."),
16: ("Sûrenin **ikinci adlı aktörü** ve ikisi de üç ayet arayla, ikisi de rol MEF'ÛL konumunda — 29:14 Nûh, "
     "29:16 İbrâhîm. **İki peygamber, iki ardışık bölüt, ikisi de anlatının öznesi değil gönderilenin "
     "nesnesi.** `nakarat2` `اذ قال لقومه` kalıbını yakalıyor — sûre 29'un üçüncü süzgeç-altı kalıbı. Dokuz "
     "ikinci-çoğul işareti: ayet bir peygamber sözünü doğrudan aktarıyor ve gramer bunu taşıyor."),
17: ("**Dört kök birden ikileniyor ve `عبد` ile `أله` üçer kez** — ve bu kez yapı farklı: **ayet aynı fiili "
     "(`تَعْبُدُونَ`) iki kez yanlış nesneyle, üçüncü kez (`وَٱعْبُدُوهُ`) doğru nesneyle kuruyor.** `أله` üç "
     "tokeninin **üçü de lafız** — 28:71'de üç tokenden ikisi lafız biri cins isimdi; burada oran üçte üç ve "
     "`A` alanı üçünü de sayıyor. İki `nakarat2` kalıbı birden geçiyor: `من دون الله` **dört ayette** (sûrede "
     "en yaygın kalıp). **NOM hiç yok** — yirmi yedi kelimede yedi ACC ve beş GEN."),
18: ("**Aynı `pas` değeri üçüncü sûrede üçüncü kez: iki fiilli bir ayette bir edilgen → z=2,52 → ★★.** 28:60, "
     "28:88 ve şimdi 29:18 — üç ayet, üç ayrı sûre, aynı oran, aynı nişan. `كذب` iki kez ve ikisi de II. babda, "
     "biri şart biri cevap: **şart ile cevabın aynı kökten kurulduğu ilk vaka.** Esmâ tokeni `مُبِين` mühürsüz "
     "ve göndergesi `ٱلْبَلَٰغ` — sûre 29'un ilk artefaktı; sûre 28'de `مُبِين` dört token vermiş ve dördü de "
     "artefakt çıkmıştı, **beşinci token da artefakt.**"),
19: ("**ÇIPA — KADEME L2, olgu = evet.** Emsal **27:64** (*'yaratmayı başlatma ve TEKRARLAMA — döngü iddiası'*); "
     "aynı kök çifti (`بدأ`+`عود`), aynı nesne (`ٱلْخَلْق`), aynı döngü iddiası. 🜁 yazıldı. **Dikey katmanın "
     "haber verdiği eşlenme burada metinde bizzat kuruluyor:** `عود` kökünün profilinde `بدأ` ×83,2 ve satır "
     "**[B2 donmuş kalıp 10 ayet]** — on ayrı ayetten, gerçek ve donmuş; ayet o ikilinin içinde. Üç fiilin üçü "
     "de IMPF: döngü **şimdiki zamanda süren bir süreç** olarak veriliyor, 27:64'te de aynıydı. **Tarayıcı bu "
     "ayeti KAÇIRDI** → `G_bakış` ailesi eklendi."),
20: ("**ÇIPA — KADEME L2, olgu = evet.** Bir önceki ayetin döngü iddiası burada **gözleme çağrısına** "
     "dönüşüyor: `سِيرُوا۟ فِى ٱلْأَرْضِ فَٱنظُرُوا۟ كَيْفَ بَدَأَ ٱلْخَلْقَ` — iddia doğrulanabilir bir işleme "
     "bağlanıyor. 🜁 yazıldı. **Okumanın ikinci `mm2` kaydı** (`يُنشِئُ ٱلنَّشْأَةَ`); birincisi 28:61'di. "
     "Fâsılada: 29:19 ve 29:20 ardışık ve **ikisi de R sınıfı** — sûrenin üç R fâsılasından ikisi yan yana, ve "
     "bu yüzden `kafiye_kirik` ikisinde de 0. **Ardışık sapma kırılma üretmiyor**; ölçüt komşuların "
     "hemfikirliğini arıyor. Esmâ: `آخِر` artefakt, `قَدِير` geçerli — **tek ayette biri artefakt biri "
     "geçerli.** Tarayıcı KAÇIRDI (gözleme çağrısı emir kipinde) → `G_bakış` emir kipine açıldı."),
21: ("**Okumada ikinci 'yalnız kafiyeden' yıldız** (birincisi 28:28). Mekanizma ters yönde: **29:21 sûrenin "
     "baskın sınıfına (N) UYUYOR ve yine de kırılma sayılıyor**, çünkü iki R komşusu arasında kalıyor. "
     "**Ölçüt 'sûre normundan sapma'yı değil 'yerel komşuluktan sapma'yı ölçüyor** ve bu iki şey burada zıt "
     "yönde. `i'râb` alanı tamamen boş — sekiz kelimede hiçbir hâl işareti yok."),
22: ("**İki ardışık ayet, ikisi de yalnız kafiyeden ★ alıyor — okumada ilk kez.** 29:20 (R) → 29:21 (N) → "
     "29:22 (R) → 29:23 (N): dört ayetlik bir salınım ve ortadaki ikisi koşulu ayrı ayrı sağlıyor. **TAM "
     "SAYIM: korpusta `kafiye_kirik`=1 olan 230 ayetin 35'i ardışık çift; 29:21-22 bunlardan biri.** İkinci "
     "tekillik: **hiç fiil yok** — `vf` ve `zmn` boş, on yedi kelime tamamen isim cümlesi ve `i'râb` yedi GEN "
     "ile tek hâl."),
23: ("**Sûre 28 boyunca 88 ayette hiç görülmeyen alan burada tetikleniyor.** Yön `2>13`: ayet üçüncü şahısla "
     "başlıyor, Allah'tan da üçüncü şahısla söz ediyor, sonra on üçüncü kelimede **birinci şahsa geçiyor** — "
     "`مِن رَّحْمَتِى`. **TAM SAYIM: korpusta iltifât taşıyan 328 ayet; sûre 27'de üç, sûre 28'de SIFIR, sûre "
     "29'da bir.** İltifât yıldız formülünün ölçütlerinden biri değil — dört sûrelik okumada hiçbir iltifât "
     "yıldıza dönüşmedi."),
24: ("**Tarayıcının bu blokta verdiği TEK aday ve çıpa değil.** `D_yeti` tetikledi, olgu kökü `نور` — ama "
     "lemma `نار` (ateş) ve olgu iddiası yok; ateş bir anlatı unsuru. **Kademe L0, çıpa eşiğinin altında; "
     "🜁 yazılmadı.** **Aday 923'ün ölçtüğü lemma kusuru sûre 29'da ilk kez tekrarlanıyor.** Ayetin kendi "
     "imzası `nakarat2`'de: **yedi kelimelik kalıp** — sûre 29'un en uzun nakaratı, ikinci ucu beş ayet sonra "
     "(29:29) ve aynı zamanda **sûrenin ilk iç düğümü.** `xref` kalıbı 7:82 ve 27:56'ya da bağlıyor: üç sûre, "
     "dört ayet, aynı formül."),
25: ("**`بعض` dört kez — okumada bir kökün tek ayette ulaştığı en yüksek sayı** (sûre 28'in tavanı üçtü). Ve "
     "dördü **iki simetrik çift** kuruyor: `بَعْضُكُم بِبَعْضٍ` / `بَعْضُكُم بَعْضًا` — aynı yapı, iki ayrı "
     "fiille. `ikile` dördü de sayıyor, **çift yapısını tutmuyor.** `sim[2]=24` — yirmi yedi kelimede yirmi "
     "dört birimlik gövde, okumanın en yükseği. `وثن` kökü korpusta yalnız üç ayette ve **ikisi de bu "
     "nakaratın içinde**; dikey katmanda `Allah med=1` — lafza en yakın medyanlı kök, ama anlamı putlar."),
26: ("**Payda etkisinin bu blokta en ince örneği ve bu kez `rab` ölçütünde: z=1,45, eşik 1,5.** Bir `رَبّ` on "
     "iki kelimede; 29:6'da bir lafız on kelimede 1,47 vermiş ve 0,03 farkla geçememişti, burada 0,05 farkla. "
     "**Beş ayet sonra 29:30'da bir `رَبّ` altı kelimede z=3,23 verecek.** Esmâ: sûrenin ikinci mühürlü çifti "
     "ve yine **geçerli**; üç sûrede mühürlü yanlış pozitif hâlâ sıfır. `nakarat2` `هو العزيز الحكيم` kalıbını "
     "yakalıyor ama geçiremiyor — 29:5'in `هو السميع العليم` kalıbıyla **aynı yapı, aynı sonuç.**"),
27: ("**Sûrenin beş adlı aktöründen ikisi tek ayette ve ikisi de aynı gramer konumunda (`mecrur`).** Sûre "
     "29'un adlı aktör dizisi: Nûh (mef'ûl) · İbrâhîm (mef'ûl) · Lût (fâil) · İshâk, Ya'kûb (mecrur) — **beş "
     "isim, üç ayrı i'râb konumu**; sûre 28'de otuz yedi token vardı ama Mûsâ tek başına on sekizdi, burada "
     "dağılım. `نبأ` kökü sûrede iki geçişli ve **ikisi iki ayrı anlam alanında**: 29:8'de `فَأُنَبِّئُكُم` "
     "(haber vermek), burada `ٱلنُّبُوَّة` (peygamberlik) — **P0 #5'in sûre 29'daki ikinci vakası.**"),
28: ("**OKUMADA İLK 'YAKIN' KADEMESİ.** Sûre 27 ve 28 boyunca `esit2`'nin üst kademesi (0,95-1,0) bir kez bile "
     "tetiklenmemişti; ilk kayıt burada: 29:28 ↔ 7:80, oran **0,9615**. **TAM SAYIM: korpusta 'yakin' 84 kayıt "
     "/ 74 ayet; kademe dağılımı tam 1622 · benzer 280 · yakin 84** — 'yakin' üç kademenin en seyreği ve "
     "'benzer'in üçte biri kadar. **Sûre 28'in 'gerçek bağlar 0,82-0,95 bandında yoğunlaşıyor' kaydını "
     "çürütmüyor, niceliğe bağlıyor.** Beş xref 3-gram'ın beşi de 7:80'e düşüyor; fark bir kip: soru cümlesi "
     "te'kidli habere dönüşüyor."),
29: ("**Sûrenin ilk iç düğümü burada kapanıyor:** `مَا كَانَ جَوَابَ قَوْمِهِ إِلَّآ أَن قَالُوا۟` — 29:24 "
     "(İbrâhîm'in kavmi) ve 29:29 (Lût'un kavmi), **beş ayet arayla, birebir yedi kelime**; `dugum.ic` iki "
     "ayette de 1. **İki ayrı peygamber, iki ayrı kavim, aynı formül** — ve kalıp `xref` ile 7:82 ve 27:56'ya "
     "da düşüyor. `أتي` üç kez ve **üçü üç ayrı işlevde** (yönelme, işleme, getirme): **P0 #5'in sûre 29'daki "
     "üçüncü vakası.** `edim` alanı **üç değer birden** taşıyor (soru, emir, şart) — okumada nadir."),
30: ("**Aday 903'ün iki otomatik ★★★ tetikleyicisi dışında kalan 409 ayetten biri ve mekanizması açıkta:** "
     "altı kelimede bir `رَبّ`, oran 0,167. Aynı sûrede 29:26'da bir `رَبّ` on iki kelimedeydi ve z=1,45 ile "
     "eşiği geçemiyordu; **burada payda yarıya inince z iki katından fazla artıyor (1,45 → 3,23) ve ayet "
     "doğrudan ★★★ alıyor.** Dört ayet arayla, aynı ölçüt, aynı token sayısı, biri yıldızsız biri ★★★. Sûre "
     "28'de 28:17/28:24 çifti aynı mekanizmayı ★★/yıldızsız olarak göstermişti; **burada uç noktaya taşınmış "
     "hâli.**"),
31: ("**`adsiz2` bu blokta dört kez tetikleniyor** — 29:31 `karye`, 29:32 `imrae`, 29:33 `imrae`, 29:34 "
     "`karye`; sûre 28'de sekiz token vardı ve üçü `karye`ydi, **burada dört token dört ayette ve ikişer çift "
     "hâlinde.** `أهل` iki kez ve ikisi de aynı şehrin halkı için, iki farklı i'râb konumunda. `هلك` kökü "
     "dikey katmanda `قري` ile çok ayetli gerçek bir çift kuruyor — ayet tam o çiftin içinde."),
32: ("**Sûrenin ikinci iç düğümü burada açılıyor ve tek ayet sonra kapanıyor:** `كَانَتْ مِنَ ٱلْغَٰبِرِينَ` — "
     "29:32 ve 29:33, **ardışık iki ayet, birebir üç kelime**; `dugum.ic` ikisinde de 1. Bir önceki iç düğüm "
     "beş ayetlikti; **bu bir ayetlik ve okumada ölçülen en dar iç düğüm.** Ama `nakarat2` süzgeci geçmiyor — "
     "**iç düğüm ile nakarat süzgeci bağımsız çalışıyor: `dugum` kalıbı sayıyor, `nakarat2` onu yoruma "
     "sokmuyor.** `غبر` korpusta yalnız sekiz ayette ve sûrede iki geçişli; ikisi de bu düğümün içinde."),
33: ("**Dikey katmanın üç blok önce haber verdiği donmuş ikili burada metinde kuruluyor:** `خوف`+`حزن` — sûre "
     "28'de üç kez **[B2 donmuş kalıp 19 ayet]** olarak kaydedilmişti. **Sûre 29'da ikisi de ilk kez ve tek "
     "ayette, üstelik ikisi de nehiy kipinde.** `ذرع` korpusta yalnız dört ayette ve `ضاق ... ذرعا` terkibi "
     "dört xref 3-gram'ıyla **11:77'ye** düşüyor — aynı sahnenin öbür anlatımı. **Tek ayet, iki ayrı hedefe "
     "bağlanıyor** ve `esit2` ikisinde de boş."),
34: ("**İki nakarat çifti bu dört ayette iç içe geçmiş:** `اهل هذه القريه` 29:31 ↔ 29:34 (üç ayet açıklık) ve "
     "`كانت من الغبرين` 29:32 ↔ 29:33 (bir ayet). **İkisi de 2 ayet / 3 kelime ve ikisi de süzgeçten "
     "geçemiyor** — ama biri `dugum.ic` alanında iç düğüm sayılıyor, öteki sayılmıyor. **İki alan aynı "
     "büyüklükteki iki kalıba farklı davranıyor**; sebep `dugum`un lemma 3-gram'ı, `nakarat2`'nin yüzey "
     "n-gram'ı kullanması. `رجز` korpusta dokuz ayette ve xref ikisini 2:59 ve 7:162'ye bağlıyor — **aynı azap "
     "adı iki ayrı kavme.**"),
35: ("`ترك` kökü burada tükeniyor ve iki geçişi sûrenin iki ucunu tutuyor: **29:2'de `أَن يُتْرَكُوٓا۟`** "
     "(sınanmadan bırakılmak — edilgen, olumsuz) ve burada **`تَّرَكْنَا مِنْهَآ ءَايَةً`** (işaret bırakmak — "
     "etken, olumlu). **Aynı kök, otuz üç ayet arayla, biri terk edilmemek biri geride bırakmak.** Sûre 28'de "
     "`يَمّ` kökünün 28:7 ↔ 28:40 arasındaki aynı yapıdaki karşıtlığı kaydedilmişti; **burada ikinci örnek ve "
     "yine hiçbir alan bağlamıyor** — blokun tek tamamen bağsız ayeti."),
}
