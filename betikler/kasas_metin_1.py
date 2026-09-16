# -*- coding: utf-8 -*-
"""kasas_metin_1.py — sûre 28 meal ve matematikçi merceği (28:1-44).
Ölçüm satırı burada YOK: o defterden üretilir (olcum_bicim.py)."""

MEAL = {
1: "Tâ-Sîn-Mîm.",
2: "Bunlar apaçık Kitab'ın âyetleridir.",
3: "Sana Mûsâ ile Firavun'un haberinden bir bölümünü, inanan bir topluluk için gerçek üzere okuyoruz.",
4: "Firavun yeryüzünde büyüklendi ve halkını bölük bölük ayırdı; onlardan bir bölüğü ezip güçsüz bırakıyor, oğullarını boğazlıyor, kadınlarını sağ bırakıyordu. O, bozgunculardandı.",
5: "Biz ise, yeryüzünde güçsüz bırakılanlara lütufta bulunmayı, onları öncüler kılmayı ve onları vârisler yapmayı diliyoruz.",
6: "Ve onları yeryüzünde yerleştirip Firavun'a, Hâmân'a ve o ikisinin ordularına, çekindikleri şeyi onlardan göstermeyi diliyoruz.",
7: "Mûsâ'nın annesine, \"Onu emzir; başına bir şey gelmesinden korkarsan onu suya bırak, korkma ve üzülme. Biz onu sana geri döndüreceğiz ve onu gönderilenlerden kılacağız\" diye vahyettik.",
8: "Nihayet Firavun ailesi onu bulup aldı — kendilerine düşman ve tasa olsun diye. Gerçekten Firavun, Hâmân ve orduları yanılgı içindeydi.",
9: "Firavun'un karısı dedi ki: \"Bana da sana da göz aydınlığı. Onu öldürmeyin; belki bize faydası olur, ya da onu evlât ediniriz.\" Oysa onlar farkında değillerdi.",
10: "Mûsâ'nın annesinin gönlü bomboş kaldı. İnananlardan olsun diye kalbine bağ vurmasaydık, neredeyse onu açığa vuracaktı.",
11: "Kız kardeşine, \"Onun izini sür\" dedi. O da, onlar farkında olmadan, uzaktan onu gözetledi.",
12: "Daha önce ona süt analarını haram kılmıştık. Kız kardeşi, \"Size onun bakımını üstlenecek, ona öğüt verip iyi davranacak bir aile göstereyim mi?\" dedi.",
13: "Böylece onu annesine geri döndürdük ki gözü aydın olsun, üzülmesin ve Allah'ın vaadinin gerçek olduğunu bilsin. Fakat onların çoğu bilmez.",
14: "Olgunluk çağına ulaşıp erginleşince ona hüküm ve ilim verdik. İyilik edenleri işte böyle ödüllendiririz.",
15: "Halkının habersiz olduğu bir sırada şehre girdi ve orada dövüşen iki adam buldu: biri kendi tarafından, öbürü düşmanından. Kendi tarafından olan, düşmanından olana karşı ondan yardım istedi. Mûsâ ona bir yumruk vurdu ve işini bitirdi. \"Bu şeytanın işindendir; o apaçık saptırıcı bir düşmandır\" dedi.",
16: "\"Rabbim, ben kendime zulmettim, beni bağışla\" dedi. O da onu bağışladı. Şüphesiz O, çok bağışlayan, çok merhamet edendir.",
17: "\"Rabbim, bana lütfettiğin nimetler hakkı için, artık asla suçlulara arka çıkmayacağım\" dedi.",
18: "Şehirde korku içinde, etrafı gözetleyerek sabahladı. Bir de baktı ki dün kendisinden yardım isteyen kişi yine feryat ediyor. Mûsâ ona, \"Sen gerçekten apaçık bir azgınsın\" dedi.",
19: "İkisinin de düşmanı olan kişiyi yakalamak isteyince, o adam, \"Ey Mûsâ! Dün bir cana kıydığın gibi beni de mi öldürmek istiyorsun? Sen yeryüzünde zorba olmaktan başka bir şey istemiyorsun; düzeltenlerden olmak istemiyorsun\" dedi.",
20: "Şehrin öbür ucundan bir adam koşarak geldi ve \"Ey Mûsâ! İleri gelenler seni öldürmek için aralarında konuşuyorlar. Hemen çık git; ben sana öğüt verenlerdenim\" dedi.",
21: "Oradan korka korka, etrafı gözetleyerek çıktı. \"Rabbim, beni zalimler topluluğundan kurtar\" dedi.",
22: "Medyen'e doğru yöneldiğinde, \"Umarım Rabbim beni doğru yola iletir\" dedi.",
23: "Medyen suyuna varınca, orada hayvanlarını sulayan bir insan topluluğu buldu. Onların gerisinde de sürülerini geri tutan iki kadın gördü. \"Derdiniz ne?\" dedi. \"Çobanlar sulayıp çekilmedikçe biz sulamayız; babamız da çok yaşlı bir adam\" dediler.",
24: "İkisinin hayvanlarını suladı, sonra gölgeye çekilip \"Rabbim, bana indireceğin her hayra muhtacım\" dedi.",
25: "Derken o iki kadından biri utana utana yürüyerek ona geldi: \"Babam, bize su çektiğin için ücretini vermek üzere seni çağırıyor\" dedi. Mûsâ ona gelip başından geçeni anlatınca, \"Korkma, zalim topluluktan kurtuldun\" dedi.",
26: "O iki kadından biri, \"Babacığım, onu ücretle tut; ücretle tuttuklarının en hayırlısı güçlü ve güvenilir olandır\" dedi.",
27: "\"Bana sekiz yıl çalışmana karşılık şu iki kızımdan birini sana nikâhlamak istiyorum. On yıla tamamlarsan o senden bir iyilik olur. Sana zorluk çıkarmak istemem. İnşallah beni iyilerden bulacaksın\" dedi.",
28: "\"Bu, seninle benim aramdadır. İki süreden hangisini tamamlarsam bana bir husumet yok. Söylediklerimize Allah vekildir\" dedi.",
29: "Mûsâ süreyi tamamlayıp ailesiyle yola çıkınca Tûr tarafında bir ateş fark etti. Ailesine, \"Siz durun; ben bir ateş gördüm. Belki size ondan bir haber ya da ısınasınız diye ateşten bir kor getiririm\" dedi.",
30: "Oraya gelince, bereketli yerdeki vadinin sağ kıyısından, ağaçtan şöyle seslenildi: \"Ey Mûsâ! Ben âlemlerin Rabbi Allah'ım.\"",
31: "\"Asânı at.\" Onun bir yılan gibi kıvrandığını görünce arkasını dönüp kaçtı, geri bakmadı. \"Ey Mûsâ! Beri gel, korkma; sen güvende olanlardansın.\"",
32: "\"Elini koynuna sok; kusursuz, bembeyaz çıksın. Korkudan açılan kollarını kendine çek. İşte bunlar, Firavun'a ve ileri gelenlerine karşı Rabbinden iki kesin delildir. Onlar yoldan çıkmış bir topluluktur.\"",
33: "\"Rabbim, ben onlardan bir cana kıydım; beni öldürmelerinden korkuyorum\" dedi.",
34: "\"Kardeşim Hârûn benden daha düzgün konuşur. Onu benimle birlikte, beni doğrulayan bir destek olarak gönder. Beni yalanlamalarından korkuyorum.\"",
35: "\"Kardeşinle senin gücünü pekiştireceğiz ve size öyle bir yetki vereceğiz ki size ulaşamayacaklar. Âyetlerimizle, siz ve size uyanlar üstün geleceksiniz\" dedi.",
36: "Mûsâ onlara apaçık âyetlerimizle gelince, \"Bu, uydurulmuş bir büyüden başka bir şey değil; biz bunu önceki atalarımızda da işitmedik\" dediler.",
37: "Mûsâ dedi ki: \"Katından kimin hidâyetle geldiğini ve dünya yurdunun sonunun kime ait olacağını Rabbim daha iyi bilir. Zalimler kurtuluşa eremez.\"",
38: "Firavun dedi ki: \"Ey ileri gelenler! Sizin için benden başka bir ilâh bilmiyorum. Ey Hâmân! Benim için çamuru ateşte pişir de bana bir kule yap; belki Mûsâ'nın ilâhına çıkıp bakarım. Doğrusu onu yalancılardan sanıyorum.\"",
39: "O ve orduları yeryüzünde haksız yere büyüklendiler ve bize döndürülmeyeceklerini sandılar.",
40: "Biz de onu ve ordularını yakalayıp denize attık. Bak, zalimlerin sonu nasıl oldu!",
41: "Onları, ateşe çağıran öncüler kıldık. Kıyamet günü de yardım görmezler.",
42: "Bu dünyada arkalarına bir lânet taktık; kıyamet günü de onlar iğrenç kılınmışlardandır.",
43: "Önceki nesilleri helâk ettikten sonra, insanlar için basiretler, bir hidâyet ve rahmet olarak Mûsâ'ya Kitab'ı verdik; belki düşünüp öğüt alırlar.",
44: "Mûsâ'ya o emri bildirdiğimizde sen batı yakasında değildin; tanıklardan da değildin.",
}

M = {
1: ("Onarılmış `harf` alanının en sert gösterimi: ham alan üç harflik ayete 22 yazıyor (besmele "
    "gömülü), harf3 3. Oran 0,136; blokta başka hiçbir ayet 0,93'ün altına inmiyor. **TAM SAYIM:** "
    "iskeleti tek başına طسم olan ayet korpusta İKİ tane (26:1, 28:1) ve esit2 ikisini 1,0 ile "
    "eşleştiriyor — korpusun en küçük mukattaa kümesi. Sûre 27 (طس) ile bağ YOK: sıralamada komşu "
    "olan ile ölçümde eş olan farklı sûreler."),
2: ("**esit2'nin 'benzer' kademesi için ilk doğrulama vakası ve geçerli çıktı:** 28:2 ↔ 12:1 farkı "
    "yalnız الر mukattaası, oran 0,9231. Ama aynı tarama 28:2 ↔ 31:2'yi **0,8333** ile eşiğin ALTINDA "
    "bırakıyor, oysa oradaki tek fark ٱلْمُبِين/ٱلْحَكِيم — tek bir sıfat. **TAM SAYIM:** iskeletinde "
    "تلك + ءايت geçen 11 ayet var (2:252 · 3:108 · 10:1 · 12:1 · 13:1 · 15:1 · 26:2 · 27:1 · 28:2 · "
    "31:2 · 45:6); esit2 bunlardan ikisini yakalıyor, dokuzunu bırakıyor. Esmâ tokeni مُبِين mühürsüz "
    "ve göndergesi ٱلْكِتَٰب — **ARTEFAKT.**"),
3: ("İki ayet birlikte bir formülü ikiye bölüyor ve bu **tam sayımla kapanıyor**: korpusta نتلو* + "
    "بالحق dört ayette (2:252, 3:108, 45:6, burası). İlk üçünde kalıp tek ayette bütün — تِلْكَ ءَايَٰتُ "
    "ٱللَّهِ نَتْلُوهَا عَلَيْكَ بِٱلْحَقِّ; burada 28:2 baş yarısını, 28:3 ikinci yarısını taşıyor. Ve "
    "dağılırken nesne değişiyor: öbür üçünde ءَايَٰتُ ٱللَّهِ, burada نَبَإِ مُوسَىٰ وَفِرْعَوْنَ — "
    "**dördünün nesnesi âyet olmayan tek ayeti bu.** `xref` 28:3'te tamamen BOŞ: zincirin hiçbir ucunu "
    "görmüyor, çünkü lemma 3-gramları araya giren özel adlarla kırılıyor."),
4: ("Ayet ölçümde tek bir şeyle ayrışıyor: **ACC 8** ve simetri [3,2,16,1] — on dokuz kelimede on altı "
    "birimlik gövde. On üç kök, hiçbiri tekrarlanmıyor, ikisi (ذبح, نسو) sûrede yalnız burada. Yani "
    "yoğunluk tekrardan değil **tek seferlik sözcük yığılmasından** geliyor; buna rağmen hapaks yok, "
    "yıldız yok. **İçerik ağırlığı ile ölçüm ağırlığının ayrıştığı temiz vaka.** Çıpa: شِيَعًا bir "
    "sınıflama getiriyor ama olguya değil topluluğa uygulanıyor — **kademe L1** (27:17 ölçütüyle aynı "
    "yerde); 🜁/🜂 yazılmadı, ayet zaten yıldızsız."),
5: ("Bir önceki ayetin fiili يَسْتَضْعِفُ (etken, fâili Firavun), buradaki ٱسْتُضْعِفُوا۟ (edilgen, fâil "
    "silinmiş): **aynı kök, aynı bab (X), ardışık ayet, çatı ters.** Ölçüm bunu iki yerde görüyor — "
    "ضعف sûrede iki geçişli ve ikisi bitişik; pas alanı 28:5'te 1, 28:4'te 0. Ama **pas z=0,81 eşiğin "
    "altında kaldığı için yıldıza dönüşmüyor**: sûre 27'de on bir yıldızın kaynağı olan mekanizma "
    "burada eşiği geçmiyor. جعل iki kez ve ikisi de aynı gramerde; ikileme ayrı bir yıldız kaynağı "
    "değil."),
6: ("`nakarat2` blokta ilk kez doluyor ve **yorum süzgeci ilk kez fiilen iş görüyor**: فرعون همن "
    "جنودهما kalıbı 28:6 ve 28:8'de, yani **2 ayet ve 3 kelime**. Protokol ölçütü ≥3 ayet YA DA "
    "≥4 kelime; kalıp ikisini de geçemiyor — **ölçüme yazıldı, yoruma girmedi.** Eski `dugum.nakarat` "
    "alanı bu ayette de 0 (tam-ayet tekrarı yok); yeni alan kalıbı görüyor ama süzgeç onu iddiaya "
    "dönüştürmüyor. İkil şahıs işareti (جُنُودَهُمَا) blokta iki ayette var ve ikisi de bu kalıbın "
    "geçtiği ayetler: ikil, kalıbın gramer imzası."),
7: ("**TAM SAYIM (aday 899 gereği, defterden):** korpusta 2FS işareti taşıyan ayet 30; en yüksek değer "
    "9 ve iki ayette — **28:7 ve 19:26, ortak azami.** Tavan uzunluktan gelmiyor: 19:26 n=18, burası "
    "n=22, oysa 16:69 n=24 ve yalnız 5 işaret taşıyor. İkinci ölçüm: خوف iki kez, biri şart (خِفْتِ) "
    "biri yasak (لَا تَخَافِى). Çıpa: ٱلْيَمّ bir su kütlesi adlandırılıyor, başka bir şey söylenmiyor — "
    "**kademe L0** (27:24 ve 27:82 ölçütüyle aynı yerde); çıpa yok, 🜁/🜂 yazılmadı. "
    "**ALAN ARIZASI — adsiz2, tam sayımla kapatıldı:** أُمِّ مُوسَىٰ yalnız akrabalık yoluyla anılan, "
    "adı hiç verilmeyen bir aktör ve alan BOŞ. Etiket envanteri yedi kategori (karye 57 · racül 58 · "
    "ferîk 34 · imrae 26 · tâife 24 · mer 11 · nefer 4) ve hepsi 01_adsiz_lemma_listesi.py'deki ALTI "
    "okuma çıpasından türemiş; **akrabalık kategorisi yok.** Lemma أُمّ 31 ayette geçiyor, 26'sında "
    "adsiz2 boş. **Onarımın envanteri, aday 899'un yasakladığı taraflı örneklemin kendisinden "
    "türetilmiş — kavram doğru, envanter eksik.**"),
8: ("**TAM SAYIM: لقط korpusta İKİ ayet — 12:10 ve 28:8.** İkisinde de aynı bab (VIII), ikisinde de "
    "nesne bir çocuk, ikisinde de fâil çocuğu bulan taraf; iki sahne de Mısır'da. Kökün dağılımı iki "
    "elemanlı — bu yorum değil sayım. İkinci not: ACC 8, 28:4'ün değeriyle aynı ama orada n=19 burada "
    "n=13, yani yoğunluk daha yüksek ve yine yıldız yok."),
9: ("İki ardışık ayet iki ayrı alanla aynı sûreye bağlanıyor ve **bağın büyüklüğü ölçüldü: 28:9 ile "
    "12:21 ALTI kelimelik birebir iskelet n-gramı paylaşıyor** — عسا ان ينفعنا او نتخذه ولدا. 12:21'de "
    "sözü Yûsuf'u satın alan söylüyor, burada Firavun'un karısı. **Bağı hangi alanın gördüğü asıl not:** "
    "esit2 0,4467 ile doğru davranıp bağlamıyor (ayetlerin bütünü farklı); nakarat2 tanım gereği "
    "sûre-içi çalıştığı için **göremez**; yalnız xref görüyor, o da iki ayrı 3-gram olarak. "
    "**Katmanın boyu tam sayımla ölçüldü:** en az iki farklı sûrede geçen 6 kelimelik iskelet n-gramı "
    "1192 kalıp / 965 ayet (korpusun %15,5'i); esit2 bunların %18'ini, xref %88,6'sını görüyor, "
    "%3,5'inde üç alan da boş. **Uzunluk bilgisi hiçbir alanda taşınmıyor.**"),
10: ("On yedi kelimede **altı kök sûrede yalnız burada** (فأد, فرغ, كود, بدو, ربط, قلب) — blokta bu "
     "yoğunlukta başka ayet yok. Buna rağmen hapaks alanı boş: **'sûre içi tek geçiş' ile 'korpus "
     "hapaksı' ayrı şeyler ve yalnız ikincisi yıldıza dönüşüyor.** Ayet blokta tek şart yapısı ve şart "
     "karşı-olgusal: لَوْلَآ أَن رَّبَطْنَا — bağ vurulmasaydı sonuç başka olurdu. **Çıpa kademesi L2:** "
     "açık nedensel bağımlılık var ama bağlanan şey doğa olgusu değil bir iç hâl (27:62 ölçütüyle aynı "
     "yerde). Esmâ tokeni مُؤْمِن göndergesi annenin kendisi — **ARTEFAKT.**"),
11: ("**Sûrenin adını taşıyan kök burada ilk kez geçiyor ve anlatma anlamında değil:** قُصِّيهِ — "
     "'izini sür'. TAM SAYIM: قصص korpusta 25 ayette, sûre 28'de üç token / iki ayette (28:11, 28:25); "
     "ilk geçiş 'iz sürme', ikincisi 'anlatma'. **P0 #5'in sınama kümesine giren türden vaka: kök tek, "
     "anlam alanı iki, alan ayırmıyor.** İkinci ölçüm: شعر sûrede iki geçişli ve ikisi de aynı kalıpta "
     "(وَهُمْ لَا يَشْعُرُونَ, 28:9 ve burası) — iki ayet arayla birebir üç kelime, ama `nakarat2` bu "
     "ayette BOŞ; azami kalıp süzgeci daha uzun bir örtüşme aramış."),
12: ("رضع sûrede iki geçişli ve ikisi karşıt yönde: 28:7'de anneye 'onu emzir' (أَرْضِعِيهِ, emir), "
     "burada 'süt analarını ona haram kıldık' (yasak). TAM SAYIM: رضع korpusta altı ayette ve ikisi bu "
     "sûrede — **kökün üçte biri tek sahnede.** İkinci imza dar köklerde: دلل (8 ayet), كفل (10), نصح "
     "(11) — üçü de korpusun alt ucundan, üçü de sûrede tek geçişli, tek ayette toplanmış. Buna rağmen "
     "hapaks yok ve yıldız yok: **nadirlik yığılması ile hapaks ayrı şeyler; formül yalnız ikincisini "
     "görüyor.**"),
13: ("28:7'de kurulan sözün ölçülebilir kapanışı: orada إِنَّا رَآدُّوهُ إِلَيْكِ (ism-i fâil, gelecek), "
     "burada فَرَدَدْنَٰهُ إِلَىٰٓ أُمِّهِ (PERF, gerçekleşmiş) — aynı kök, aynı fâil, altı ayet arayla. "
     "Ve aynı ayette وَعْدَ ٱللَّهِ حَقٌّ, yani vaadin gerçekliği önermesi tam da vaadin gerçekleştiği "
     "cümlenin ardında. **Sûrenin ilk Allah lafzı burada, on üçüncü ayette** — ilk on iki ayet lafızsız "
     "ve Rabsızdı. `nakarat2` blokta ilk kez süzgeci geçen kalıbı veriyor: لكن اكثرهم لا يعلمون, dört "
     "kelime, iki ayet (28:13, 28:57). `dis`=5 ile blokta en bağlı ayet ve yine yıldız yok: "
     "**bağlılık ile yıldız arasında ölçüm düzeyinde bağ yok.**"),
14: ("**esit2'nin 'benzer' kademesi için ikinci ve en temiz doğrulama:** 12:22 iskeleti لما بلغ اشده "
     "ءاتينه حكما علما كذلك نجزا المحسنين; 28:14 aynısı artı **tek bir kelime (استوا)**, oran 0,9412. "
     "Fark tek kelime ve alan bunu 'benzer' yazıyor — oysa 'yakin' 0,95'ten başlıyor. Bir önceki vakada "
     "(28:2↔12:1) fark bir mukattaa idi ve oran 0,9231. **İki vakayla ortaya çıkan: kademe sınırı 0,95, "
     "korpusun asıl yoğunlaştığı yerin (tek kelimelik fark) ÜSTÜNDE duruyor; 'yakin' pratikte yalnız "
     "hareke düzeyi farkları için kalıyor.** Çıpa: أَشُدّ + ٱسْتَوَىٰ bir gelişim eşiğini iki terimle "
     "adlandırıyor, ölçü/mekanizma yok — **kademe L1**, blokta tek çıpa kaydı."),
15: ("**Sûrenin en uzun ayeti ve ilk hapaksı aynı yere düşüyor.** وكز korpusta tek geçişli. İkinci imza "
     "kök ikilemesinde: عدو üç kez, شيع iki kez, ikisi de aynı iki kişiyi ters yönlerden tanımlıyor. "
     "TAM SAYIM: bir kökü 3+ kez tekrarlayan ayet korpusta 528, 4+ kez tekrarlayan 120 — 28:15 "
     "birincide, ikincide değil. Üçüncüsü: **on sekiz şahıs işaretinin tamamı üçüncü şahıs** ve ayet "
     "baştan sona فَ ile zincirlenmiş **altı PERF fiil** taşıyor (دَخَلَ · وَجَدَ · ٱسْتَغَٰثَ · وَكَزَ · "
     "قَضَىٰ · قَالَ); blokta başka hiçbir ayette altı PERF yok. Esmâ tokeni مُبِين burada **şeytanın "
     "sıfatı** — esmâ tablosunun artefakt üretimi en sert biçimde görünüyor. **Yıldızın kaynağı: "
     "hapaks z=3,38 + n z=2,72; içerik katkısı 0.**"),
16: ("غفر üç kez ve üçü üç ayrı gramerde: ٱغْفِرْ (emir), غَفَرَ (PERF), ٱلْغَفُور (sıfat) — talep, ifa, "
     "nitelik. TAM SAYIM: غفر sûrede toplam üç geçişli, yani **kökün sûredeki tüm varlığı bu tek "
     "ayette.** Esmâ tarafında sûre 27'nin bulgusuyla tam karşıtlık: blokun dört esmâ tokeninden üçü "
     "mühürsüz ve üçü artefakt (28:15 şeytanın مُبِين'i, 28:18 مُبِين, 28:19 جَبّار), **tek mühürlü token "
     "burada ve GEÇERLİ** — çift غَفُور|رَحِيم, gönderge هُوَ, mercii رَبِّ. Fâsıla م ve sûrenin baskın "
     "ن'sinden sapıyor ama `kafiye_kirik` 0 yazıyor: **ölçüt sapmanın kendisi değil, komşuların aynı "
     "sınıfta olması** (ve -îm ile -ûn/-în aynı N sınıfında)."),
17: ("**Blokun en saf yıldız-kaynak vakası:** dokuz kelimelik, hapakssız, edilgensiz bir ayet ★★ alıyor "
     "ve tek sebebi رَبّ'in ayet içindeki yoğunluğu (rab z=2,05). 26:217'de gösterilen mekanizmanın "
     "aynısı — **yıldız içeriği değil eksen oranını ölçüyor.** Karşılaştırma bir önceki ayetle "
     "yapılabiliyor çünkü ikisi aynı yapıda açılıyor (قَالَ رَبِّ): 28:16 n=13 ile yıldızsız, 28:17 n=9 "
     "ile ★★. **Aynı token sayısı, daha kısa ayet, daha yüksek z — fark tamamen paydadan.** "
     "`nakarat2`'nin قال رب انا kalıbı bu ayette YOK, çünkü buradaki açılış قَالَ رَبِّ بِمَآ: "
     "üç kelimelik kalıp bir harfle kırılıyor ve alan bunu doğru yapıyor."),
18: ("صبح sûrede üç geçişli ve ikisi bu blokta: 28:10'da annenin gönlü 'bomboş sabahladı', burada Mûsâ "
     "'korku içinde sabahladı' — **aynı fiil, aynı أَصْبَحَ + hâl yapısı, sekiz ayet arayla, biri anne "
     "biri oğul, ikisi de bir iç hâl.** Ölçüm buna ayrı bir alan ayırmıyor: esit2 eşleştirmiyor, "
     "nakarat2 görmüyor (kalıp üç kelimeye ulaşmıyor). İkinci imza bab profilinde: beş fiil, dört ayrı "
     "bab (I, IV, V, X×2) — blokta bu dağınıklıkta başka ayet yok. Üçüncüsü aktörde: yardım isteyen "
     "kişi ikinci kez sahnede ve iki kez de adsız, ama 28:15'te رَجُلَيْنِ olarak geçtiği için adsiz2 "
     "onu ORADA görüyor, **burada ٱلَّذِى ile anıldığı için göremiyor** — 28:7'deki envanter boşluğunun "
     "ikinci tipi: **ismi mevsûlle anılan adsız aktör de alanın dışında.**"),
19: ("**رود dört kez ve dördü de ikinci şahsa yöneltilmiş:** أَرَادَ (haber) · أَتُرِيدُ (soru) · إِن "
     "تُرِيدُ إِلَّآ (hasr) · وَمَا تُرِيدُ (nefy). TAM SAYIM: رود sûrede dokuz geçişli ve **dördü tek "
     "ayette.** `fig` alanı yalnız HASR'ı etiketliyor, öbür üçünü `kip` taşıyor. Yıldız tarafında "
     "blokun üçüncü kaynağı burada: 28:15 uzunluk+hapaks, 28:17 yalnız Rab, 28:19 yalnız uzunluk — "
     "**üç yıldızlı ayet, üç ayrı kaynak profili, içerik katkısı üçünde de 0.** Esmâ tokeni جَبّار "
     "orta konumda ve göndergesi Mûsâ hakkında kurulan itham — **ARTEFAKT.**"),
20: ("نصح sûrede iki geçişli ve **ikisi de fâsılada**: 28:12'de نَٰصِحُون, burada ٱلنَّٰصِحِين — sekiz "
     "ayet arayla, biri kız kardeşin önerdiği aile hakkında, biri adamın kendisi hakkında, ikisi de "
     "ayetin son kelimesi. TAM SAYIM: نصح korpusta 11 ayette ve ikisi bu sûrede. رجل de sûrede iki "
     "geçişli ve ikisi de `adsiz2`'nin doğru yakaladığı iki adsız aktör (28:15 رَجُلَيْنِ, burada "
     "رَجُلٌ) — **alanın doğru çalıştığı iki vaka, blokun iki ucunda.** Ayırt edici not `isaret`te: "
     "harf3=74 ve isaret yalnız 1; blokta 28:15'te 13, 28:18'de 7. **Eski `harf` alanı tek sayı olarak "
     "kullanıldığında bu 13'e 1'lik fark ölçüme sessizce giriyordu.**"),
21: ("28:18 ile birebir aynı iki kelimeyi taşıyor — خَآئِفًا يَتَرَقَّبُ — üç ayet arayla; orada şehirde "
     "sabahlarken, burada şehirden çıkarken. رقب sûrede iki geçişli ve ikisi de bu terkipte. Ölçüm "
     "bunu hiçbir alanda göstermiyor: esit2 eşleştirmiyor, **nakarat2 de göremiyor — kalıp iki kelime, "
     "üç kelimelik alt sınırın altında.** Buna karşılık nakarat2 aynı ayette başka bir kalıbı "
     "yakalıyor: من القوم الظلمين (28:21, 28:25), o da üç kelime ve iki ayet — süzgeci geçemiyor. "
     "**Blokta iki ayrı tekrar, ikisi de alanın eşiklerinin dibinde: biri alt sınırın altında olduğu "
     "için hiç görünmüyor, öbürü görünüyor ama yoruma giremiyor.**"),
22: ("İki ardışık ayet, ikisi de ★, ikisinin de tek kaynağı رَبّ ve ikisi de kısa (n=10, n=11): payda "
     "küçüldüğü için z yükseliyor — 28:17'de gösterilen mekanizmanın aynısı. عسي sûrede iki geçişli ve "
     "ikisi de aynı gramerde: 28:9'da Firavun'un karısı عَسَىٰٓ أَن يَنفَعَنَا, burada Mûsâ عَسَىٰ رَبِّىٓ "
     "أَن يَهْدِيَنِى — **aynı umut kalıbı, on üç ayet arayla, biri çocuğu alıkoymak için biri yolu "
     "bulmak için.** هدي — sûre 27'de dört anlam alanıyla P0 #5'in sınama kümesine girmiş olan kök — "
     "sûre 28'de ilk kez burada ve en sık anlam alanında."),
23: ("**Yıldız formülü hakkında tam sayımla kapanan şey burada ilk kez görünüyor:** `hapaks` z değeri "
     "ayette bir hapaks kök varken **3,38** ve ★★★ eşiği mx>3. Yani **tek bir hapaks kök, başka hiçbir "
     "ölçüt tetiklenmese bile ayeti doğrudan ★★★ yapıyor.** TAM SAYIM: korpusta hapaks içeren 358 ayet "
     "var ve **358'inin de yıldızı 3 — istisnasız**; bunların 329'u (tüm ★★★'ların %37,4'ü) yıldızını "
     "YALNIZ bu ölçütten alıyor. **Sûre 27 kapanışındaki 'yıldız kaynakları: hapaks 5' satırı bu yüzden "
     "yeniden okunmalı: hapaks bir katkı değil, YETER ŞART.** İkinci imza ikil şahısta: 2D×3 ve 3FD×2, "
     "beş ikil işaret; blokta bu yoğunlukta başka ayet yok. Üçüncüsü bağda: أَبُونَا شَيْخٌ كَبِيرٌ üç "
     "kelimesiyle 12:78'e düşüyor — sûre 28'in sûre 12'ye dördüncü xref bağı."),
24: ("Blokta Rab taşıyan üçüncü ayet ve **tek yıldızsız olanı**: rab z=1,10, eşik 1,5'in altında. "
     "28:21 (n=10) ve 28:22 (n=11) aynı token sayısıyla ★ alıyordu; burada n=15 ve aynı token yıldıza "
     "dönüşmüyor — **üç ayet, aynı ölçüt, aynı token sayısı, farklı sonuç; fark yalnızca uzunlukta.** "
     "İkinci nokta doğrudan P0 #5'e ait: `kok_turkce`'de ظلل karşılığı 'sürüp gitme, olmayı sürdürme', "
     "oysa buradaki lemma ظِلّ — **gölge.** Kök tek, anlam alanı iki, tablo birini taşıyor; dikey "
     "katmanın komşuluk profili ise (üst, meyve, bulut) 'gölge' anlamını doğruluyor."),
25: ("**Sûrenin adını taşıyan kök ikinci kez ve bu kez iki anlamda birden:** وَقَصَّ عَلَيْهِ ٱلْقَصَصَ — "
     "fiil 'anlattı', mef'ûl 'anlatılan'; 28:11'de aynı kök قُصِّيهِ ile 'izini sür' demişti. "
     "**TAM SAYIM: قصص sûrede üç token / iki ayet, üç tokenin ikisi bir anlam alanında (anlatma), biri "
     "ötekinde (iz sürme) — sûre adının kökü, sûre içinde her iki anlamıyla da geçiyor.** İmza bab "
     "profilinde: **on bir fiil, on birinin de babı I**; blokta bunun karşıtı 28:29 (I×5, IV×2, VIII×1). "
     "Yıldız yok: n z=1,44 eşiğin hemen altında. **Blokun en uzun üçüncü ayeti, sıfır yıldız — 28:23 "
     "ile arasındaki tek fark bir hapaks kök.**"),
26: ("أجر iki kez ve ikisi de X. babda: ٱسْتَـْٔجِرْ (emir) ve ٱسْتَـْٔجَرْتَ (mâzî) — **aynı kök, aynı "
     "bab, aynı ayet, biri istek biri geçmiş.** Blokta bu yapının üçüncü örneği (28:16 غفر üç kip, "
     "28:19 رود dört kip). Esmâ tarafında blokun ikinci artefaktı: ٱلْقَوِىُّ ٱلْأَمِينُ — tablonun ilâhî "
     "ad saydığı iki kelime, burada bir işçinin niteliği. **Sûre 28'in ilk otuz ayetinde mühürsüz esmâ "
     "token sayısı sekiz, yedisi artefakt.** Ayrıca إِحْدَىٰهُمَا 28:25, 28:26 ve 28:27'de üç ardışık "
     "ayette ve `say` alanı üçünü de işaretliyor."),
27: ("**TAM SAYIM: korpusta üç ya da daha fazla sayı işareti taşıyan ayet 29 tane; 28:27 sûre 28'deki "
     "tek örnek.** Üç sayı üç ayrı işi yapıyor — إِحْدَى seçim, ثَمانِي yükümlülük, عَشْر isteğe bağlı "
     "fazlalık — ve üçü de sözleşme terimi. İkinci imza i'râbda: ACC 3 · NOM 3 · GEN 3, **blokta üç "
     "hâlin de eşit dağıldığı tek ayet.** Üçüncüsü yine P0 #5: بني kökünün tablo karşılığı 'bina, "
     "yapma', buradaki lemma ٱبْنَت — **kız evlat**; 28:4'te aynı kök أَبْنَآء (oğullar) olarak geçmişti. "
     "**Kökün sûredeki iki geçişinin ikisi de tablodaki karşılığın dışında.**"),
28: ("**Ölçüm bakımından blokun en tekil ayeti, iki ayrı alanda.** Birincisi kafiye: sûre 28'de ن dışı "
     "yedi fâsıla var ama **yalnız 28:28 kırılma sayılıyor**, çünkü ölçüt sapmanın kendisi değil "
     "*komşuların aynı sınıfta olması*; 28:22 ل iken komşuları N ve R (farklı, kırılma yok), burada "
     "komşuların ikisi de N. TAM SAYIM: korpusta kafiye_kirik=1 olan 230 ayet var ve **141'i yıldızını "
     "yalnız bu ölçütten alıyor**; 28:28 hem sûrenin tek kırılma kaydı hem blokun tek 'yalnız kafiye' "
     "yıldızı (|z| ölçütlerinin en büyüğü 0,81, eşiğin altında). İkincisi esmâ: وَكِيل mühürsüz ama "
     "göndergesi doğrudan ٱللَّه — **sûre 28'in ilk otuz ayetindeki sekiz mühürsüz tokenin tek GEÇERLİ "
     "olanı.** Sûre 27'de bu oran 1/21'di (27:88 خَبِير); iki sûrede de geçerli mühürsüz token var ve "
     "iki sûrede de sayısı bir. Üçüncüsü: terkip 12:66 ile birebir aynı."),
29: ("**Aynı sahne korpusta üç kez anlatılıyor ve üç alan üç ayrı şey görüyor.** 20:10, 27:7 ve 28:29 "
     "aynı ateş sahnesini veriyor; إِنَّىٓ ءَانَسْتُ نَارًا üçünde de birebir. **xref bunu ALTI ayrı "
     "3-gram'la yakalıyor** — sûrenin ilk otuz ayetinde en yüksek xref yükü. `esit2` üçünü de "
     "bağlamıyor ve bu kez doğru davranıyor: 28:29↔20:10 oranı 0,6409, ↔27:7 oranı 0,5587 ve ikisi de "
     "0,25'lik uzunluk elemesine takılıyor. Üçüncü çift ilginç: 20:10↔27:7 uzunluk farkı 0,029 ile "
     "elemeyi geçiyor ama oran 0,5652 ile eşiğin çok altında. **esit2 için temiz bir doğru negatif, "
     "xref için temiz bir doğru pozitif.** P0 #5 tarafında blokun en yoğun vakası: أنس karşılığı "
     "'insan' ama iki lemma آنَسَ (fark etti); نور karşılığı 'nûr, ışık' ama üç lemma da نار (ateş) — "
     "**tek ayette beş token, iki kök, ikisinin de tablo karşılığı yanlış anlam alanında.**"),
30: ("Ayet ölçümde iki bakımdan blokun ucunda. Birincisi konum yoğunluğu: شَٰطِئِ ٱلْوَادِ ٱلْأَيْمَنِ · "
     "ٱلْبُقْعَةِ ٱلْمُبَٰرَكَةِ · ٱلشَّجَرَةِ — **üç ayrı konum belirteci, GEN 7 ile**; blokta başka "
     "hiçbir ayette yedi cer yok, ve altı kökün beşi sûrede tek geçişli, biri hapaks. İkincisi çatı: "
     "نُودِىَ blokun tek edilgen fiili ve fâil silinmiş; ardından gelen cümlede fâil أَنَا ٱللَّهُ olarak "
     "açıkça beliriyor. **Edilgen çağrı ile birinci şahıs kimlik beyanı aynı ayette, arka arkaya** — "
     "ölçüm bunu iki ayrı alanda (pas, A+R) görüyor ama aralarındaki ilişkiyi tutan alan yok. "
     "Üçüncüsü: isaret=0, on dokuz kelimede hiç vakf işareti yok, harf/harf3 oranı tam 1,000."),
31: ("**TAM SAYIM — esit2 için oturumun en sert yanlış negatifi.** 28:31 ile 27:10 iskeletleri **on iki "
     "kelimelik kesintisiz birebir dizi** paylaşıyor (الق عصاك فلما رءاها تهتز كانها جان ولا مدبرا لم "
     "يعقب يموسا); oran **0,8252**, uzunluk farkı **0,014** — yani 0,25'lik eleme geçiliyor ama "
     "**0,85 eşiğinin 0,025 altında kalınıyor ve bağ hiç yazılmıyor.** İki ayette de esit2 boş; bağı "
     "yalnız xref görüyor, o da altı ayrı 3-gram parçası hâlinde. **Kaçağın büyüklüğü:** korpusta en az "
     "on kelimelik birebir ortak iskelet dizisi paylaşan **111 ayet çifti** var; esit2 **31'ini (%27,9) "
     "görüyor, 80'ini görmüyor**, görmediklerinin **66'sı çapraz-sûre** yani nakarat2 de ulaşamıyor. "
     "Aynı sahne dört sûrede anlatılıyor ama 28:31↔20:20, ↔26:32, ↔7:107 oranları 0,20-0,34 ve üçü de "
     "uzunluk elemesine takılıyor: **ölçüm sahnenin bir anlatımını doğru ayırt ediyor, sonra doğru "
     "olanı da eliyor.** P0 #3 için bu oturumda çıkan en temiz vaka."),
32: ("**Aynı sahne, ikinci ayet, ve bu kez esit2 başka bir mekanizmayla eliyor.** 28:32 ↔ 27:12 oranı "
     "0,7152 ama bağ oran hesaplanmadan kesiliyor: **uzunluk farkı 0,281, yani 0,25'lik ön elemenin "
     "üstünde.** Bir önceki ayette eleme geçilip eşikte düşülmüştü; burada eşiğe hiç gelinmiyor. Buna "
     "karşılık ortak dizi yine uzun: يدك فا جيبك تخرج بيضاء من غير سوء — **sekiz kelime birebir.** "
     "**İki ardışık ayet, iki ardışık ayetle eşleşiyor (28:31↔27:10, 28:32↔27:12) ve esit2 ikisini de "
     "kaçırıyor — biri eşikten, biri elemeden.** Ayetin kendi imzası dar köklerde: on altı kökün yedisi "
     "sûrede tek geçişli, ضمم korpusta yalnız iki ayette; hiçbiri hapaks değil, n z=1,34 eşiğin altında, "
     "yıldız yok."),
33: ("**Aynı z, aynı yıldız, aynı uzunluk:** 28:17 ve 28:33 ikisi de n=9, ikisi de tek رَبّ, ikisinin de "
     "rab z=2,05, ikisi de ★★ — **formülün deterministik olduğunun temiz gösterimi; içerik hiçbir rol "
     "oynamıyor.** İkincisi: nakarat2'nin üç ayetlik kalıbı burada tamamlanıyor — قَالَ رَبِّ إِنِّى, "
     "28:16 (zulüm itirafı), 28:24 (yoksulluk itirafı), 28:33 (korku itirafı); üçü de birinci şahıs, "
     "üçü de bir eksiklik beyanı, ve ≥3 ayet ölçütünü sağladığı için yoruma girebiliyor. قتل sûrede "
     "yedi geçişli ve altıncı-yedincisi burada, ikisi ters yönde (قَتَلْتُ / يَقْتُلُونِ); 28:19'da aynı "
     "çift başkasının ağzından kurulmuştu, **burada Mûsâ aynı iki fiili kendi ağzında topluyor.**"),
34: ("Sûre 28'in ikinci ★★★'ı ve ilkinden (28:15) farklı profil: orada hapaks+uzunluk, burada **yalnız "
     "hapaks ve iki kat** (z=6,98). **TAM SAYIM: korpusta iki hapaks kök taşıyan ayet 28 tane** (bir "
     "hapakslı 325, üç 3, dört 1, beş 1); sûre 27'nin çift-hapaks ayeti 27:88 de aynı kümede. İçerik "
     "tarafında dikkat çeken şey **ne ölçülüyorsa onun ölçülmediği**: ayet açık bir karşılaştırma "
     "kuruyor (أَفْصَحُ مِنِّى لِسَانًا) ama hiçbir alan karşılaştırma tutmuyor — ne `fig` ne `kip`. "
     "Ölçüm ayeti yalnız iki nadir kökten tanıyor. خوف kökü sûrede sekiz geçişli ve sekizincisi burada; "
     "son iki geçişi (28:33, 28:34) ardışık ve ikisi de أَخَافُ أَن kalıbında — **iki kelimelik olduğu "
     "için nakarat2'nin alt sınırının altında.**"),
35: ("**Dört ikil şahıs işareti — blokta ve sûrede en yüksek:** لَكُمَا · إِلَيْكُمَا · أَنتُمَا · "
     "ٱتَّبَعَكُمَا. Bir önceki ayette istenen ortaklık, bu ayette gramerin kendisine geçiyor ve `sah` "
     "alanı bunu 2D:4 olarak tutuyor; 28:23'te beş ikil vardı ama orada özne iki kadındı, **burada "
     "muhatap ikili.** عضد korpusta yalnız iki ayette. شدد sûrede üç geçişli ve ikincisi burada "
     "(birincisi 28:14'te أَشُدّ, olgunluk çağı) — **aynı kök, biri bedenin olgunlaşması biri kolun "
     "güçlendirilmesi, yirmi bir ayet arayla.** On beş kelimede beş kök sûrede tek geçişli, hapaks yok, "
     "yıldız yok."),
36: ("Ayet **iki ayrı olumsuzlamayı** üst üste koyuyor: `kip` ikisini de sayıyor (NEG 2), `fig` yalnız "
     "birini etiketliyor (HASR — مَا هَٰذَآ إِلَّا); ikinci olumsuzlama (وَمَا سَمِعْنَا) sadece NEG olarak "
     "kalıyor. **Blokta fig ile kip'in aynı olguya farklı granülerlikte baktığı ikinci vaka** "
     "(birincisi 28:19'da رود'un dört kipiydi). أبو kökü sûrede dört geçişli ve dördüncüsü burada — kök "
     "tükeniyor; ilk üçü Şuayb bağlamındaydı (28:23, 25, 26), dördüncüsü Firavun kavminin 'ataları'. "
     "xref burada iki 3-gram veriyor ve ikisi de Mûsâ anlatısı dışına düşüyor (23:24, 61:6) — "
     "**bu blokta 27 ve 12 dışına çıkan ilk bağ.**"),
37: ("**Blokun tek 'iç düğüm'ü burada ve hedefi sûrenin sonunda: 28:85.** قَالَ رَبِّى أَعْلَمُ kalıbı "
     "korpusta dört ayete düşüyor ve biri aynı sûrenin 85. ayeti — 28:37 ile 28:85 arasında kırk sekiz "
     "ayetlik bir sûre-içi bağ var ve `dugum.ic` bunu 1 olarak tutuyor; **sûre 28'in ilk kırk ayetinde "
     "tek iç düğüm bu.** İkinci not: üç ayrı 3-gram'ın üçü de 6:135'e düşüyor, yani 28:37'nin ikinci "
     "yarısı neredeyse bütünüyle 6:135 ile örtüşüyor, ama esit2 yine boş. Üçüncüsü: nakarat2'nin جاء "
     "بالهدا من kalıbı iki ayet ve üç kelime — **blokta süzgeci geçemeyen ikinci kalıp.**"),
38: ("**أله kökü burada iki kez ve ikisi de lafza-i celâl DEĞİL:** مِّنْ إِلَٰهٍ غَيْرِى ve إِلَٰهِ "
     "مُوسَىٰ — kök aynı, ikisi de cins isim. Buna karşılık ayetin `A` alanı **boş**: lafız sayacı kök "
     "geçişini sayarken lafzı saymıyor. **Kök katmanı ile lafız katmanının doğru ayrıştığı temiz "
     "vaka** — sûre 27'de esmâ tablosunun tersini yaptığı yerin karşıtı. İkincisi bağda: يَٰٓأَيُّهَا "
     "ٱلْمَلَأُ üç kelimesi **sûre 27'nin üç ayrı ayetine** düşüyor (27:29, 32, 38); orada Sebe "
     "melikesinin ileri gelenlerine hitabıydı, burada Firavun'un — **aynı hitap formülü, iki hükümdar, "
     "iki sûre.** Üçüncüsü: dokuz birinci-şahıs işareti, blokta en yüksek 1S yoğunluğu ve hepsi tek "
     "konuşmacıya ait."),
39: ("**Blokta beşinci ve son yıldız kaynağı burada ortaya çıkıyor:** on ayette dört yıldızlı ayet ve "
     "**dördü dört ayrı kaynaktan** — 28:33 Rab · 28:34 hapaks · 28:38 uzunluk · 28:39 edilgenlik. "
     "Yıldız veren beş ölçütten dördü tek blokta, birer kez, hiçbiri ikinci kez (beşincisi `allah`, "
     "blokta hiç tetiklenmedi çünkü ayetlerin hiçbirinde lafız yok). كبر sûrede iki geçişli ve ikisi "
     "karşıt: 28:23'te شَيْخٌ كَبِيرٌ (yaşlı adam), burada ٱسْتَكْبَرَ (büyüklendi) — **tablo karşılığı "
     "'büyüklük; büyüklenme' ikisini de kapsıyor, yani P0 #5'in OLUMLU örneği.** ظنن de iki geçişli ve "
     "ikisi bitişik: 28:38'de Firavun Mûsâ'yı yalancı sanıyor, burada dönüşün olmayacağını sanıyorlar."),
40: ("**Sûrenin ilk bölütü burada kapanıyor ve kapanışı يَمّ kökü yapıyor.** Kök sûrede iki geçişli: "
     "28:7'de anne bebeği denize bırakıyor (فَأَلْقِيهِ فِى ٱلْيَمِّ), 28:40'ta Firavun ve orduları "
     "denize atılıyor (فَنَبَذْنَٰهُمْ فِى ٱلْيَمِّ). TAM SAYIM: يمم korpusta on ayette ve ikisi bu sûrede; "
     "**otuz üç ayet arayla, aynı yer belirteciyle, ters yönde — biri kurtuluş biri helâk.** Ölçüm bunu "
     "hiçbir alanda bağlamıyor: esit2 boş, nakarat2 boş (فى اليم iki kelime, alt sınırın altında), "
     "xref iki ayeti birbirine değil 51:40'a bağlıyor. İkincisi kapanış formülünde: dikey katmanın iki "
     "ayrı satırında **B2 donmuş kalıp olarak 22-37 ayetten** onaylanan üçlü (نظر+كيف+عقب) burada "
     "bizzat geçiyor — **komşuluk ölçümünün haber verdiği kalıp, okumanın on ayet sonrasında metinde "
     "çıkıyor.**"),
41: ("**TAM SAYIM — sûre-içi ters çift.** İskeletinde ايمه geçen ayet korpusta beş tane (9:12 · 21:73 · "
     "28:5 · 28:41 · 32:24); dördü جعل ile kurulmuş — 21:73 ve 32:24 يهدون بامرنا, 28:5 نجعلهم ايمه, "
     "28:41 جعلنهم ايمه يدعون الا النار. **Üçü hidâyete, biri ateşe çağırıyor — ve o bir tanesi, aynı "
     "sûrede otuz altı ayet önce kurulan kalıbın tersi.** Ölçüm bunu göstermiyor ve sebebi tam olarak "
     "belirlenebilir: nakarat2 n-gram düzeyinde çalışıyor ve iki ayetteki kelime biçimleri farklı "
     "(نجعلهم / جعلنهم). **Lemma düzeyinde aynı, yüzey düzeyinde farklı; alan yüzeye bakıyor — P0 #5'in "
     "neden yalnız gloss sorunu olmadığının gösterimi: lemma katmanı yazılsaydı nakarat2 bu çifti "
     "görürdü.** Ayrıca نور kökü sûredeki dördüncü ve son geçişinde yine نار lemmasıyla: **sûredeki "
     "dört tokenin dördü de 'ateş', kök karşılığı ise 'nûr, ışık'.**"),
42: ("**Hapaks kuralının en saf gösterimi:** on kelime, tek fiil, uzunluk z=-0,26 (ortalamanın altında), "
     "edilgen yok, lafız yok, Rab yok — ve yıldız **üç.** Tek sebebi مَقْبُوحِين kökünün korpusta başka "
     "hiçbir yerde geçmemesi. Bir önceki ayet 28:41 dokuz kelimeyle ve bir edilgen fiille **★** aldı; "
     "bu ayet on kelimeyle ve sıfır edilgenle **★★★.** **İkisi arasındaki tek ölçülebilir fark bir "
     "kökün korpus sıklığı** — sûre 27 kapanışında 'içerik 0' diye yazılan satırın altındaki mekanizma "
     "tam olarak budur. xref üçlü bağın ikisini 11:60'a düşürüyor: sûre 11 ile bu sûrenin ilk bağı."),
43: ("İmza bab profilinde: **üç fiilin hiçbiri birinci babda değil** (IV×2, V×1) — blokta ve sûrenin "
     "okunan bölümünde başka örneği yok; bir önceki ayet de tek fiilliydi ve IV. babdaydı, yani "
     "**28:42-43 ikilisi beş fiil taşıyor ve beşi de artırılmış bab.** İkincisi أنس kökünde: sûrede "
     "dört geçişli ve dördüncüsü burada — dört geçişin ikisi ناس (insanlar: 28:23, 28:43), ikisi آنَسَ "
     "(fark etti: 28:29 ×2). **Tek kök, iki anlam alanı, sûrede tam yarı yarıya — ve kok_turkce yalnız "
     "birini taşıyor.** Üçüncüsü: بَصَآئِر ile 28:11'deki فَبَصُرَتْ aynı kökten ve sûrenin üç بصر "
     "geçişinden ikisi."),
44: ("**TAM SAYIM:** korpusta ما + كنت ikilisi 14 ayette geçiyor ve **dördü sûre 28'de** (28:44, 45, 46, "
     "86) — üçü ardışık; korpusun hiçbir yerinde bu yoğunlukta değil. **Ama ikili iki kelime, "
     "nakarat2'nin üç kelimelik alt sınırının altında: alan üç ardışık ayetteki tekrarı göremiyor.** "
     "28:44-45-46 üç ayrı olumsuzlama zinciri kuruyor (batı yakasında değildin · Medyen halkı içinde "
     "oturmuş değildin · Tûr yanında değildin); nakarat2 bunun **yalnız bir parçasını** görüyor "
     "(ما كنت بجانب, 28:44 ve 28:46) ve onu da süzgeçten geçiremiyor (2 ayet, 3 kelime), çünkü ortadaki "
     "28:45 بِجَانِبِ yerine ثَاوِيًا taşıyor. **Üç ayetlik gerçek bir yapı: iki kelimelik çekirdeği "
     "alanın alt sınırının altında, üç kelimelik uzantısı süzgecin üstünde ama eşiğinin altında.**"),
}
