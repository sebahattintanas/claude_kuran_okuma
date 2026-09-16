# -*- coding: utf-8 -*-
"""kasas_metin_2.py — sûre 28 meal ve matematikçi merceği (28:45-88)."""

MEAL = {
45: "Fakat biz nice nesiller var ettik; ömürleri uzayıp gitti. Sen Medyen halkı arasında oturmuş, onlara âyetlerimizi okuyor da değildin; fakat elçiler gönderen biziz.",
46: "Biz seslendiğimizde Tûr'un yanında da değildin. Fakat Rabbinden bir rahmet olarak, kendilerine senden önce bir uyarıcı gelmemiş bir topluluğu uyarasın diye gönderildin; belki düşünüp öğüt alırlar.",
47: "Kendi elleriyle yaptıkları yüzünden başlarına bir musibet geldiğinde, \"Rabbimiz, bize bir elçi gönderseydin de âyetlerine uyup inananlardan olsaydık\" demeyecek olsalardı...",
48: "Katımızdan onlara hak gelince, \"Mûsâ'ya verilenin benzeri ona da verilseydi ya\" dediler. Peki daha önce Mûsâ'ya verileni inkâr etmemişler miydi? \"Birbirini destekleyen iki büyü\" dediler ve \"Biz hepsini inkâr ediyoruz\" dediler.",
49: "De ki: \"Doğru söylüyorsanız, Allah katından bu ikisinden daha doğru yol gösteren bir kitap getirin de ona uyayım.\"",
50: "Sana cevap veremezlerse bil ki onlar ancak kendi heveslerine uyuyorlar. Allah'tan bir yol göstericilik olmaksızın kendi hevesine uyandan daha sapkın kim olabilir? Şüphesiz Allah zalimler topluluğunu doğru yola iletmez.",
51: "Andolsun, düşünüp öğüt alsınlar diye sözü onlara ardı ardına ulaştırdık.",
52: "Kendilerine daha önce Kitap verdiklerimiz, buna da inanırlar.",
53: "Onlara okunduğunda, \"Buna inandık; şüphesiz bu, Rabbimizden gelen gerçektir. Biz bundan önce de teslim olmuştuk\" derler.",
54: "İşte onlara, sabretmeleri sebebiyle ecirleri iki kat verilir. Onlar kötülüğü iyilikle savarlar ve kendilerine verdiğimiz rızıktan infak ederler.",
55: "Boş söz işittiklerinde ondan yüz çevirirler ve \"Bizim işlerimiz bize, sizin işleriniz size; size selâm olsun. Biz cahilleri aramayız\" derler.",
56: "Sen sevdiğini doğru yola iletemezsin; fakat Allah dilediğini doğru yola iletir. O, doğru yolu bulacakları daha iyi bilir.",
57: "\"Seninle birlikte doğru yola uyarsak yurdumuzdan kapılıp götürülürüz\" dediler. Onları, katımızdan bir rızık olarak her şeyin ürünlerinin toplandığı güvenli bir haremde yerleştirmedik mi? Fakat çokları bilmezler.",
58: "Geçim bolluğuyla şımarmış nice şehri helâk ettik. İşte meskenleri: kendilerinden sonra pek azı dışında oturulmadı. Vâris olanlar biziz.",
59: "Rabbin, ana şehirlerine, âyetlerimizi onlara okuyan bir elçi göndermedikçe şehirleri helâk edici değildi. Biz şehirleri, ancak halkı zalim olduğunda helâk ediciyiz.",
60: "Size verilen her şey dünya hayatının geçimliği ve süsüdür. Allah katındaki ise daha hayırlı ve daha kalıcıdır. Hâlâ akletmeyecek misiniz?",
61: "Kendisine güzel bir vaatte bulunduğumuz ve ona kavuşacak olan kimse, dünya hayatının geçimliğini verdiğimiz, sonra kıyamet günü hesaba çekilenlerden olacak kimse gibi midir?",
62: "O gün onlara seslenip, \"Benim ortaklarım olduğunu öne sürdükleriniz nerede?\" diyecek.",
63: "Haklarında söz gerçekleşmiş olanlar der ki: \"Rabbimiz! İşte azdırdıklarımız bunlar. Kendimiz azdığımız gibi onları da azdırdık. Sana yöneldik, onlardan uzağız; onlar aslında bize kulluk etmiyorlardı.\"",
64: "\"Ortaklarınızı çağırın\" denir; onları çağırırlar ama kendilerine cevap vermezler ve azabı görürler. Keşke doğru yolu bulmuş olsalardı!",
65: "O gün onlara seslenip, \"Gönderilen elçilere ne cevap verdiniz?\" diyecek.",
66: "O gün haberler onlara kapanır; artık birbirlerine de soramazlar.",
67: "Ama tevbe edip inanan ve iyi iş yapan kimseye gelince, umulur ki kurtuluşa erenlerden olur.",
68: "Rabbin dilediğini yaratır ve seçer; onların seçme hakkı yoktur. Allah, onların ortak koştuklarından münezzeh ve yücedir.",
69: "Rabbin, göğüslerinin gizlediğini de açığa vurduklarını da bilir.",
70: "O, Allah'tır; O'ndan başka ilâh yoktur. İlkte de sonda da hamd O'nadır. Hüküm O'nundur ve O'na döndürüleceksiniz.",
71: "De ki: \"Söyleyin bakalım, Allah geceyi üzerinize kıyamet gününe kadar sürekli kılsa, Allah'tan başka hangi ilâh size bir ışık getirebilir? Hâlâ işitmiyor musunuz?\"",
72: "De ki: \"Söyleyin bakalım, Allah gündüzü üzerinize kıyamet gününe kadar sürekli kılsa, Allah'tan başka hangi ilâh size içinde dinleneceğiniz bir gece getirebilir? Hâlâ görmüyor musunuz?\"",
73: "Rahmetinden dolayı, içinde dinlenesiniz ve lütfundan arayasınız diye geceyi ve gündüzü sizin için var etti; umulur ki şükredersiniz.",
74: "O gün onlara seslenip, \"Benim ortaklarım olduğunu öne sürdükleriniz nerede?\" diyecek.",
75: "Her ümmetten bir şahit çıkarır ve \"Delilinizi getirin\" deriz. O zaman bilirler ki gerçek Allah'ındır; uydurageldikleri şeyler de kendilerinden kaybolup gider.",
76: "Kārûn, Mûsâ'nın kavmindendi; onlara karşı azgınlık etti. Ona öyle hazineler vermiştik ki anahtarları güçlü bir topluluğa ağır geliyordu. Kavmi ona demişti ki: \"Şımarma; Allah şımaranları sevmez.\"",
77: "\"Allah'ın sana verdiğiyle âhiret yurdunu ara; dünyadan da payını unutma. Allah sana iyilik ettiği gibi sen de iyilik et. Yeryüzünde bozgunculuk arama; Allah bozguncuları sevmez.\"",
78: "\"Bu bana ancak bendeki bir bilgi sayesinde verildi\" dedi. Bilmez mi ki Allah, ondan önce, kendisinden daha güçlü ve topladığı daha çok olan nice nesilleri helâk etmişti? Suçlulara günahları sorulmaz.",
79: "Kavminin karşısına süsü içinde çıktı. Dünya hayatını isteyenler, \"Keşke Kārûn'a verilenin benzeri bizim de olsaydı; o gerçekten büyük bir paya sahip\" dediler.",
80: "Kendilerine ilim verilenler ise, \"Yazıklar olsun size! İnanıp iyi iş yapan için Allah'ın vereceği karşılık daha hayırlıdır. Ona da ancak sabredenler kavuşturulur\" dediler.",
81: "Onu da, sarayını da yerin dibine geçirdik. Allah'a karşı ona yardım edebilecek bir topluluğu olmadı; kendi kendini kurtaracaklardan da değildi.",
82: "Daha dün onun yerinde olmayı temenni edenler, \"Demek ki Allah, kullarından dilediğine rızkı genişletiyor ve daraltıyor. Allah bize lütufta bulunmasaydı bizi de yerin dibine geçirirdi. Demek ki inkârcılar kurtuluşa eremezmiş\" demeye başladılar.",
83: "İşte âhiret yurdu! Onu, yeryüzünde büyüklenmek ve bozgunculuk istemeyenlere veririz. Sonuç, sakınanlarındır.",
84: "Kim bir iyilikle gelirse ona ondan daha hayırlısı vardır. Kim de bir kötülükle gelirse, kötülük işleyenler ancak yaptıklarının karşılığını görürler.",
85: "Kur'an'ı sana farz kılan, elbette seni dönülecek yere döndürecektir. De ki: \"Rabbim, kimin hidâyetle geldiğini ve kimin apaçık bir sapkınlık içinde olduğunu daha iyi bilir.\"",
86: "Sen, Kitab'ın sana bırakılacağını ummuyordun; ancak Rabbinden bir rahmet olarak geldi. Öyleyse inkârcılara arka çıkma.",
87: "Allah'ın âyetleri sana indirildikten sonra sakın seni onlardan alıkoymasınlar. Rabbine çağır ve sakın ortak koşanlardan olma.",
88: "Allah ile birlikte başka bir ilâha yalvarma. O'ndan başka ilâh yoktur. O'nun zâtından başka her şey yok olacaktır. Hüküm O'nundur ve O'na döndürüleceksiniz.",
}

M = {
45: ("Zincirin ortası ve **kalıptan sapan halka**: وَمَا كُنتَ ثَاوِيًا — öbür ikisindeki بِجَانِبِ "
     "yerine ثَاوِيًا; bu tek kelimelik sapma yüzünden nakarat2'nin üç kelimelik kalıbı ayeti dışarıda "
     "bırakıyor. İmza fiil sayısında: beş fiil, dört ayrı bab, ve تَطَاوَلَ blokun tek VI. bab fiili. "
     "تلو sûrede dört geçişli ve ikincisi burada — **28:3'te 'sana okuyoruz' (1. şahıs, olumlu), burada "
     "'sen onlara okuyor değildin' (2. şahıs, olumsuz), kırk iki ayet arayla.** مدن kökü burada "
     "tükeniyor: sûrede altı geçiş ve **ilk üçü 'şehir' (Mısır), son üçü 'Medyen' — aynı kök, iki ayrı "
     "yer adı, ölçüm ayırmıyor: P0 #5 vakası.**"),
46: ("**28:30 ile birebir ters kurulmuş bir ayet ve ölçüm ikisini bağlamıyor:** 28:30'da نُودِىَ مِن "
     "شَٰطِئِ ٱلْوَادِ (edilgen, fâil silinmiş, Mûsâ çağrılıyor), burada إِذْ نَادَيْنَا (etken, birinci "
     "çoğul) ve muhatap **çağrılmayan** kişi. ندي sûrede beş geçişli ve ikinci geçişi burada; iki geçiş "
     "de aynı sahneye bakıyor, biri içeriden biri dışarıdan. esit2 boş, nakarat2 görmüyor — "
     "**نادينا/نودى yüzey biçimleri farklı: 28:41'dekiyle aynı lemma-katmanı arızası, blokta ikinci "
     "kez.** جنب kökü de burada tükeniyor: dört geçiş, dördü de bir 'yan/taraf' konumu, ikisi aynı "
     "dağın yanı."),
47: ("Ayette iki kök de kendi mastarıyla eşleniyor — تُصِيبَهُم مُّصِيبَةٌ ve أَرْسَلْتَ ... رَسُولًا — "
     "ikisi de mef'ûl-i mutlak yapısına yakın duruyor **ama `mm2` alanı BOŞ**, çünkü onarılmış tanım "
     "'V + aynı kök + ACC isim': مُّصِيبَةٌ NOM (fâil), رَسُولًا ACC ama mef'ûl-i bih. **Alan doğru "
     "davranıyor; onarımın kendi sınırının temiz gösterimi** (14 ayet sonra 28:61'de aynı alan doğru "
     "pozitif verecek). İkinci not: yedi xref 3-gram'ın **dördü tek ayete (20:134)** düşüyor ve o ayet "
     "bunun neredeyse tıpkısı; esit2 yine boş — **28:31↔27:10 ile aynı desen: xref yoğun, esit2 "
     "sessiz.** Esmâ tokeni مُؤْمِن blokun tek esmâsı ve **ARTEFAKT.**"),
48: ("**Blokun en yoğun tekrar ayeti: üç قول, üç أتي, iki كفر** — ve أتي'nin üç tokeni de aynı edilgen "
     "kalıpta (أُوتِىَ), yani ayetin edilgenlik sayacı ile kök ikileme sayacı **aynı üç kelimeyi** "
     "ölçüyor. **İki alanın bağımsız olmadığının temiz örneği:** pas=3 ve ikile[أتي]=3, ikisi de tek "
     "bir tekrarın türevi; yıldız formülü yalnız birini (pas) ölçüte alıyor, ikileme yıldız kaynağı "
     "değil. TAM SAYIM: bir ayette 3+ edilgen fiil taşıyan ayet korpusta 35 (tavan 4, beş ayette); "
     "**28:48 sûre 28'in tek örneği.** İkincisi: on üç kelime içinde iki kez مُوسَىٰ — sûrenin okunan "
     "bölümünde tek çift-tokenli Mûsâ ayeti. Üçüncüsü: ظهر sûrede üçüncü geçişi ve **üç geçişin hiçbiri "
     "'zuhur' değil** — kök karşılığı yine eksik."),
49: ("Ayet bir önceki ayetin ikilini (سِحْرَانِ) zamirle geri alıyor: مِنْهُمَآ — `sah` alanı bunu 3D×1 "
     "olarak tutuyor. **İki ardışık ayet, ikisinde de ikil işareti, ve ikinci ayetin ikili birinci "
     "ayetten gönderge alıyor; ölçüm bu göndergeyi tutmuyor.** İkincisi karşılaştırma yapısı: أَهْدَىٰ "
     "مِنْهُمَآ — ism-i tafdîl + مِن, yani açık üstünlük karşılaştırması; **28:34'teki أَفْصَحُ مِنِّى "
     "ile aynı gramer kalıbı, on beş ayet arayla, ve ikisi de hiçbir alanda etiketlenmiyor.** `fig` "
     "alanı HASR, MM, NEHY, DIKKAT, QASEM, KELLA, AMMA tutuyor; **karşılaştırma yapısı için karşılığı "
     "yok** — sûrede iki vaka birikti, **KAPATILAMAZ.**"),
50: ("**Dört ayrı kökün aynı ayette ikilenmesi — blokta ve okunan kırk ayette tek örnek:** تبع, هوي, "
     "هدي, أله; dördü de aynı önermeyi iki kez, önce genel sonra soru biçiminde kuruyor. `ikile` alanı "
     "dördünü de sayıyor ama **hiçbiri yıldız kaynağı değil**: ayet dört ikileme, iki lafız ve n=23 ile "
     "yıldızsız kalıyor — allah z=1,21 ve n z=1,12, ikisi de 1,5 eşiğinin altında. **İki ölçüt birden "
     "eşiğe yaklaşıp ikisi de geçemiyor; formül toplamıyor, yalnız en büyüğüne bakıyor (mx=max|z|)** — "
     "oturumda ilk kez görülen durum. هوي kökü sûrede iki geçişli ve ikisi de bu ayette, yani kök tek "
     "ayette tükeniyor."),
51: ("**Altı kelime, üç kök, ve üçü de sûrede tükeniyor.** وصل ikinci ve son geçişi — birincisi "
     "28:35'te فَلَا يَصِلُونَ إِلَيْكُمَا ('size ulaşamazlar'), burada sözün ulaştırılması: **aynı kök, "
     "biri olumsuz IMPF biri olumlu PERF II. bab, tam ters yönde.** esit2, nakarat2, xref üçü de boş — "
     "**blokta bağsız ilk ayet.** Altı kelimede iki fiil ve **ikisi de artırılmış bab** (II ve V); "
     "EMPH+CERT ikilisi (وَلَقَدْ) blokta tek örnek."),
52: ("İki ardışık ayet, ikisi de blokun en kısaları (n=6, n=8), ikisinde de **birinci bab hiç yok** ve "
     "ikisinde de üç alan birden boş. Ölçümde görünür sonucu şu: **kısa ayet + artırılmış bab + "
     "bağsızlık üçlüsü, formülün hiçbir ölçütünü tetiklemiyor.** أتي sûrede on dokuz geçişli ve onuncusu "
     "burada; كتب beş geçişli ve **üçü 28:43-52 arasındaki on ayete sıkışmış** (28:43, 49, 52)."),
53: ("تلو kökünün üçüncü geçişi ve **üç geçişin üçü de ayrı çatıda**: 28:3 نَتْلُوا۟ (etken, 1. çoğul) · "
     "28:45 تَتْلُوا۟ (etken, 2. tekil, olumsuz) · 28:53 يُتْلَىٰ (**edilgen**, fâil silinmiş); dördüncüsü "
     "28:59'da gelecek. **Aynı kök, dört geçiş, dört ayrı şahıs-çatı bileşimi** — ölçüm bunu zmn, sah "
     "ve pas alanlarında ayrı ayrı tutuyor ama diziyi tutan alan yok. İkincisi: pas z=1,10, dört fiilden "
     "biri edilgen (oran 0,25), eşiğin altında; buna karşılık **aynı blokta 28:60'ta iki fiilden biri "
     "edilgen olacak (oran 0,50) ve z=2,52 ile ★★ verecek** — pas ölçütü mutlak sayıyı değil oranı "
     "ölçüyor."),
54: ("أجر kökü burada tükeniyor: sûrede beş geçiş ve **beşi de bir ücret/karşılık sözleşmesine ait** — "
     "28:25 (su çekmenin ücreti), 28:26 ×2, 28:27 (sekiz yıl çalışma) ve burada أَجْرَهُم مَّرَّتَيْنِ. "
     "**Dördü Şuayb sahnesinin somut iş sözleşmesinde, beşincisi soyut bir karşılıkta; kök aynı, ölçek "
     "farklı.** مَرَّتَيْنِ ikil ve `say` bunu işaretliyor — sûrede say işaretli beşinci ayet. İkinci "
     "not: يَدْرَءُونَ بِٱلْحَسَنَةِ ٱلسَّيِّئَةَ — حسن ve سوأ aynı cümlede karşıt konumda ve ikisi de "
     "sûrede ikinci geçişleri; درأ korpusta beş ayetlik dar bir kök."),
55: ("**Esmâ tablosunun bu blokta ürettiği ilk artefakt ve konum bakımından da ilginç:** سَلام **orta "
     "konumda** (11/15) ve göndergesi bir ilâhî ad değil, bir vedalaşma formülü (سَلَٰمٌ عَلَيْكُمْ). "
     "Sûre 28'de orta konumdaki mühürsüz tokenler şimdiye kadar ikisi de artefakt (28:19 جَبّار, burası). "
     "İkincisi: سلم kökü sûrede iki geçişli ve **ikisi iki ayrı anlam alanında** — 28:53'te مُسْلِمِين "
     "(teslim olanlar), burada سَلَٰم (esenlik), iki ayet arayla: **P0 #5'in blok içindeki ilk vakası.** "
     "عمل ikilemesi لَنَآ أَعْمَٰلُنَا وَلَكُمْ أَعْمَٰلُكُمْ — aynı kelime, iki zamirle, karşıt taraflara; "
     "`ikile` sayıyor ama **simetrik-karşıtlık yapısını tutan alan yok.**"),
56: ("**TAM SAYIM: هدي kökünü bir ayette üç ya da daha fazla kez taşıyan ayet korpusta yedi tane** — "
     "2:185 · 2:196 · 6:71 · 7:43 · 10:35 · **28:56** · 39:23; sûre 28'deki tek örnek. On üç kelimede "
     "aynı kök üç kez ve üçü üç ayrı gramerde: تَهْدِى (2. tekil, olumsuz IMPF) · يَهْدِى (3. tekil, "
     "olumlu IMPF) · ٱلْمُهْتَدِين (VIII. bab ism-i fâil) — **fiil-fiil-isim, olumsuz-olumlu-nitelik.** "
     "Sûrede dördüncü kez görülen yapı (28:16 غفر, 28:19 رود, 28:26 أجر). Ölçüm hepsini `ikile`'de "
     "tutuyor ama **hiçbiri yıldız kaynağı değil**: ayet n=13, tek lafız, allah z=1,01 ile eşiğin "
     "altında, yıldızsız."),
57: ("**Beşinci blokun açtığı kalıp burada kapanıyor:** nakarat2'nin لكن اكثرهم لا يعلمون kalıbı ilk "
     "ucunu 28:13'te vermişti, ikinci ve son ucu burada — **kırk dört ayet sonra.** Dört kelimelik "
     "olduğu için ≥4 kelime ölçütünü sağlıyor ve **iki ayetle yoruma girebiliyor** — süzgecin 'ya ≥3 "
     "ayet ya ≥4 kelime' tasarımının tam da hedeflediği vaka. İkinci not: تبع, مكن ve حرم üçü de burada "
     "tükeniyor; مكن kökünün iki geçişi (28:6 وَنُمَكِّنَ لَهُمْ فِى ٱلْأَرْضِ ve burada أَوَلَمْ نُمَكِّن "
     "لَّهُمْ حَرَمًا) **aynı fiil, aynı bab, aynı dolaylı nesne kalıbı** — ama nakarat2 bunu da görmüyor "
     "(نمكن لهم iki kelime, alt sınırın altında)."),
58: ("**TAM SAYIM — esmâ tablosunun وارِث tokeni ve mühürün yetersizliği:** korpusta yedi ayette ve "
     "**yedisi de MÜHÜRSÜZ** — 2:233 (insan mirasçı) · 15:23 · 21:89 · 23:10 (müminler) · 26:85 · "
     "**28:5** · **28:58**; üçü geçerli, dördü artefakt, ve mühür alanı yedisini de aynı işaretliyor. "
     "**Sûre 28 aynı tokeni iki kez taşıyor ve hükümleri zıt:** 28:5'te gönderge ezilen halk "
     "(ARTEFAKT), burada وَكُنَّا نَحْنُ ٱلْوَٰرِثِينَ, gönderge konuşan ilâhî ses (**GEÇERLİ**); ikisi de "
     "son konumda, ikisi de mühürsüz. **Mühür alanı ikisini ayırt edemiyor; ayıran tek şey gönderge ve "
     "onu tutan alan yok.** Sûre 27'de kurulan 'mühürlü geçerli / mühürsüz artefakt' eğiliminin iç "
     "sınırı budur. İkinci not: adsiz2 `karye`'yi yakalıyor ve **sûrede ilk kez tetikleniyor.**"),
59: ("**Ayet kendi içinde iki kez kurulan tek bir önermeden ibaret** ve ölçüm bunu üç ayrı kök "
     "ikilemesinde birden görüyor: كون, هلك, قري — üçü de ayetin iki yarısında birer kez. İkinci yarı "
     "birinciyi başka bir şartla tekrarlıyor (حَتَّىٰ يَبْعَثَ ... رَسُولًا / إِلَّا وَأَهْلُهَا "
     "ظَٰلِمُونَ); `fig` yalnız **HASR**'ı etiketliyor, birinci yarının حَتَّىٰ yapısı için karşılık yok. "
     "İkincisi: adsiz2 bu ayette **iki kez** tetikleniyor ve 28:58 ile birlikte blokta üç `karye` "
     "tokeni — alanın sûrede ilk kez çalıştığı bölge burası. Üçüncüsü: **تلو'nun dördüncü ve son "
     "geçişi — dört geçiş, dört ayrı şahıs-çatı.**"),
60: ("**`pas` ölçütünün oran tabanlı olduğunun en temiz gösterimi blok içinde yan yana duruyor:** "
     "28:57'de **iki** edilgen fiil var ve z=1,57 (★); burada **bir** edilgen fiil var ve z=2,52 (★★) "
     "— fark paydada (altı fiile karşı iki). Aynı blokta 28:53 (dört fiilden biri) z=1,10 ile eşiğin "
     "altında, 28:54 (beş fiilden biri) z=0,81 ile yıldızsız. **Dört ayet, dört farklı edilgenlik "
     "oranı, dört farklı sonuç — hiçbiri edilgen fiil sayısıyla sıralanmıyor.** Bu, rab ölçütünde "
     "28:17/28:24'te ve hapaks ölçütünde 28:41/28:42'de görülen mekanizmanın üçüncü alanda tekrarı: "
     "**formülün beş ölçütünden üçünün paydası ayet uzunluğu ya da fiil sayısı.** İkinci not: dis=4 ile "
     "blokun en bağlı ayeti ve dört xref'in üçü tek ayete (42:36) düşüyor; esit2 yine boş."),
61: ("**TAM SAYIM: onarılan `mm2` alanı (V + aynı kök + ACC isim) korpusta 125 ayette dolu ve 28:61 "
     "sûre 28'in TEK mm2 ayeti** — üstelik iki kayıt birden: وَعَدْنَٰهُ وَعْدًا ve مَتَّعْنَٰهُ مَتَٰعَ, "
     "simetrik konumlarda (2. ve 8. kelime). **Bir önceki blokta 28:47'de benzer görünen iki yapı alan "
     "tarafından DOĞRU biçimde reddedilmişti** (biri NOM, öteki mef'ûl-i bih): alan iki blok arayla bir "
     "doğru negatif ve bir doğru pozitif verdi — **onarımın tanımı ayrıştırıcı.** İkinci not: ayet iki "
     "fiille on yedi kelime taşıyor ve ikisi de PERF; وعد ve متع kökleri sûrede burada tükeniyor."),
62: ("**Sûre 28'de esit2'nin ilk TAM eşleşmesi ve okumada ilk gerçek nakarat.** 28:62 ile 28:74 "
     "kelimesi kelimesine aynı (oran 1,0); nakarat2 bunu `tür='tam'` olarak etiketliyor ve "
     "`dugum.nakarat`=2 yazıyor. **Sekiz kelimelik olduğu için ≥4 kelime süzgecini rahatça geçiyor** — "
     "sûre 26'da nakaratların altı ölçütü şişirdiği bulgusunun ardından sûre 28'de ilk kez ölçülen "
     "tam-ayet tekrarı ve **sûrenin tek örneği.** Aynı ayet ikinci bir kalıba da katılıyor: يوم "
     "يناديهم يقول üç kelime ve **üç ayette** (28:62, 65, 74), yani ≥3 ayet ölçütünden geçiyor — "
     "**tek ayet, iki ayrı süzgeç ölçütünü iki ayrı kalıpla sağlıyor.**"),
63: ("**غوي kökü üç kez ve üçü de ayetin tek cümlesinde:** أَغْوَيْنَآ · أَغْوَيْنَٰهُمْ · غَوَيْنَا; ilk "
     "ikisi IV. bab (azdırmak), üçüncüsü I. bab (azmak) — **aynı kök, iki bab, fâil ve mef'ûl aynı "
     "taraf.** Kök sûrede dört geçişli ve üçü bu ayette; dördüncüsü 28:18'deydi (Mûsâ'nın ithamı). "
     "İkinci imza şahısta: **on birinci-çoğul işareti** — okumada görülen en yüksek değer (önceki tavan "
     "28:45'te yediydi) ve hepsi tek bir konuşmacı grubuna ait. Buna karşılık ayet **yıldızsız**: "
     "**on kelimelik bir ikileme yoğunluğu ve on birinci-çoğul işareti, formülün hiçbir ölçütünde "
     "karşılık bulmuyor.**"),
64: ("دعو ikilemesi ters yönde çalışıyor: ٱدْعُوا۟ (emir, 2. çoğul) ve فَدَعَوْهُمْ (PERF, 3. çoğul) — "
     "emir ve icrası aynı cümlede. Ardından فَلَمْ يَسْتَجِيبُوا۟ ve **dikey katmanın 28:50'de ölçtüğü "
     "دعو/جوب çifti burada metinde bizzat kuruluyor** — komşuluk ölçümünün haber verdiği eşlenme, üç "
     "blok sonra ayette karşılığını buluyor (28:40'taki نظر+كيف+عقب vakasının ikinci örneği). İkinci "
     "not: pas z=0,48 — bir edilgen fiil ama yedi fiil içinde, oran 0,14; **aynı blokta 28:70'te bir "
     "edilgen fiil olacak ve z=5,38 verecek, aradaki tek fark payda (7'ye karşı 1).** عذب kökü 336 "
     "ayetlik korpus sıklığına rağmen sûrede yalnız burada."),
65: ("**Kalıbın orta ucu:** وَيَوْمَ يُنَادِيهِمْ فَيَقُولُ — 28:62, **28:65**, 28:74; üç geçişin ilki ve "
     "sonuncusu tam ayet olarak birbirinin tıpkısı (esit2 1,0), ortadaki yani bu ayet aynı açılışı "
     "taşıyıp farklı bir soruyla devam ediyor. Ölçüm bunu iki katmanda ayrı ayrı görüyor: **esit2 "
     "yalnız 62↔74'ü bağlıyor (bu ayeti dışarıda bırakıyor, doğru), nakarat2 üçünü birden bir kalıpta "
     "topluyor.** **İki alanın birbirini tam olarak tamamladığı ilk vaka** — esit2 tam ayet düzeyinde, "
     "nakarat2 n-gram düzeyinde, ve üç ayetin yapısı ancak ikisi birlikte okununca görünüyor. جوب "
     "sûrede üç geçişli ve **üçü de bu blokta** (28:50, 64, 65)."),
66: ("نبأ kökü burada tükeniyor ve iki geçişi sûrenin iki ucunu tutuyor: **28:3'te مِن نَّبَإِ مُوسَىٰ "
     "وَفِرْعَوْنَ** (sana okuduğumuz haber) ve burada **فَعَمِيَتْ عَلَيْهِمُ ٱلْأَنۢبَآءُ** (haberler "
     "onlara kapandı) — **aynı kök, altmış üç ayet arayla, biri açılan haber biri kapanan haber.** "
     "Ölçüm bunu bağlamıyor: esit2, nakarat2, xref üçü de boş; kökün iki geçişi yalnız `sûre_geçiş` "
     "sayacında yan yana duruyor. İkinci not: yedi kelime, iki fiil, biri VI. bab — sûrede VI. bab "
     "üçüncü kez (28:45, 28:68, burası). عمي kökü dikey katmanda صمم ile çok ayetli gerçek bir çift "
     "oluşturuyor."),
67: ("عسي kökü burada tükeniyor ve üç geçişinin üçü de aynı umut yapısında: **28:9** (Firavun'un karısı) "
     "· **28:22** (Mûsâ) · **28:67** (anlatıcı) — **üç geçiş, üç ayrı konuşmacı, aynı sözdizimi**; ilk "
     "ikisi somut bir kişi hakkında, üçüncüsü genel bir hüküm. nakarat2 bu üçlüyü göremiyor (عسا ان iki "
     "kelime, alt sınırın altında); onun yerine ءامن عمل صلحا kalıbını yakalıyor ama o da süzgeçten "
     "geçemiyor (2 ayet, 3 kelime) — **blokta süzgeci geçemeyen tek kalıp.** `fig` alanı **AMMA** "
     "etiketini veriyor: sûre 28'de ilk ve tek kez."),
68: ("**Lafız ve Rab aynı ayette ve ikisi de eşiğin altında kalıyor:** rab z=1,20 ve allah z=0,90, ikisi "
     "birden 1,5'in altında, **yıldız yok.** Bir önceki blokta 28:50'de görülen durumun tekrarı ve "
     "mekanizması aynı: **formül max|z| alıyor, toplamıyor** — iki eksen ölçütü birden tetiklenmeye "
     "yaklaşıp ikisi de geçemiyor. İkinci not: خير ikilemesi **iki ayrı anlam alanında** — وَيَخْتَارُ "
     "(seçer, VIII. bab) ve ٱلْخِيَرَةُ (seçme hakkı); kok_turkce'deki 'hayır, daha iyi' ikisini de tam "
     "karşılamıyor. Sûrenin خير geçişleri: 28:26, 28:60 ve burada ikisi — **yedi geçiş, en az üç anlam "
     "alanı: P0 #5 vakası.** خلق kökü 218 ayetlik korpus sıklığına rağmen sûrede yalnız burada."),
69: ("**esit2'nin 'benzer' kademesi için ÜÇÜNCÜ doğrulama vakası ve en incesi:** 27:74 iskeleti ان ربك "
     "ليعلم ما تكن صدورهم ما يعلنون, 28:69 ise ربك يعلم ما تكن صدورهم ما يعلنون — **fark yalnız baştaki "
     "إِنَّ ve fiilin te'kid lâmı**; oran **0,9455**, 'yakin' eşiğinin (0,95) **0,0045 altında.** "
     "**Oturumda esit2 eşik bandına düşen beş vakanın dördüncüsü ve bandın kalibresizliğini tamamlayan "
     "parça:** 28:2↔12:1 0,9231 (bir mukattaa) · 28:69↔27:74 0,9455 (bir te'kid edatı) · 28:14↔12:22 "
     "0,9412 (bir kelime) · 28:2↔31:2 0,8333 (bir sıfat, eşiğin altında) · 28:31↔27:10 0,8252 (on iki "
     "kelime ortak, eşiğin altında). **Beş vaka, beşi de gerçek bağ, hiçbiri 'yakin' değil, ikisi bağ "
     "olarak hiç yazılmadı; 'yakin' kademesi bu okumada bir kez bile tetiklenmedi.** Yıldız kaynağı: "
     "rab z=2,72 — **okumada ölçülen en yüksek rab değeri**, yedi kelimede bir رَبّ."),
70: ("**TAM SAYIM — yıldız formülünün İKİNCİ otomatik tetikleyicisi bulundu.** Ayetin tek fiili var ve "
     "o da edilgen: oran 1,00 → pas z=**5,38** → ★★★. Bütün fiilleri edilgen olan ayet korpusta **124 "
     "tane** ve **hepsinin pas z değeri tam olarak 5,38**; **124'ünün de yıldızı 3, istisnasız.** Bir "
     "hapaks kök (z=3,38) gibi, **tam edilgenlik de tek başına ★★★ için YETER ŞART.** İki tetikleyicinin "
     "kesişimi 11, birleşimi **471** ve bu, korpustaki **880 ★★★ ayetin %53,5'i**; geri kalan 409 ★★★ "
     "öbür ölçütlerin uç değerlerinden geliyor (rab 180, allah 123, n 86, pas 23). **★★★ nişanının "
     "yarısından fazlası iki mekanik koşuldan üretiliyor ve ikisi de içerikle ilgisiz: biri bir kökün "
     "korpus sıklığı, öteki bir ayetteki fiil sayısının küçüklüğü.** İkinci not: أله iki kez ve ikisi "
     "farklı statüde (ٱللَّهُ lafız, إِلَٰهَ cins isim); alan ikisini doğru ayırıyor."),
71: ("**Sûrenin en uzun nakarat2 kalıbı burada başlıyor: dokuz kelime** (سرمدا الا يوم القيمه من اله غير "
     "الله ياتيكم), 28:71 ve 28:72'de birebir ve süzgecin ≥4 kelime ölçütünü iki kattan fazla aşıyor. "
     "**Aynı ayet üç ayrı kalıba birden katılıyor** (9, 6 ve 3 kelimelik) ve üçü de süzgeci geçiyor — "
     "**okumada tek ayetin üç geçerli nakarat kalıbına katıldığı ilk vaka.** İkinci not: أله üç kez ve "
     "**üçü iki ayrı statüde** — ٱللَّهُ ve ٱللَّهِ lafız (A alanında [5,15]), إِلَٰهٌ cins isim "
     "(sayılmıyor): **kök sayacı üç, lafız sayacı iki, alan ayrımı doğru.** TAM SAYIM: أله kökünü bir "
     "ayette 3+ kez taşıyan ayet korpusta 207; sûre 28'de dört tane (28:71, 72, 77, 88). ضوأ korpusta "
     "yalnız altı ayette — sûrede نور'un dört tokeni 'ateş'ti, burada 'ışık' için ayrı bir kök var."),
72: ("**İki ayet, aynı kalıp, farklı yıldız — ve sebep tam olarak ölçülebilir.** 28:71 ve 28:72 dokuz "
     "kelimelik nakaratı paylaşıyor, i'râb profilleri **birebir aynı** (NOM 3 · ACC 2 · GEN 4), lafız "
     "sayıları aynı (2), أله ikilemeleri aynı (3). **Fark yalnızca uzunlukta: n=19 ve n=21.** allah "
     "z'si 1,58'den 1,38'e düşüyor ve 1,5 eşiğini geçemiyor: **birincisi ★, ikincisi yıldızsız.** "
     "**İki kelimelik uzunluk farkı, aynı içeriği taşıyan iki ayetin birini nişanlıyor** — rab "
     "(28:17/28:24), pas (28:64/28:70) ve hapaks (28:41/28:42) ölçütlerinde görülen mekanizmanın "
     "dördüncü ve en saf örneği, çünkü burada iki ayet arasındaki tek gerçek fark uzunluk. سرمد kökü "
     "korpusta yalnız bu iki ayette: **kökün korpustaki bütün varlığı bu nakaratın içinde.**"),
73: ("**Üç ayetlik bölütün kapanışı ve dört kökün birden tükendiği yer:** ليل, نهار, سكن — üçü de "
     "28:71-73 arasında sûredeki varlıklarını bitiriyor. İki soru ayetinde karşıtlık olarak kurulan "
     "gece/gündüz, burada **tek cümlede yan yana** getiriliyor; ve 28:72'de şart cümlesinin içinde geçen "
     "تَسْكُنُونَ فِيهِ burada gerekçe cümlesine dönüşüyor (لِتَسْكُنُوا۟ فِيهِ) — **aynı iki kelime, "
     "ardışık ayette, biri IMPF haber biri IMPF ta'lîl; nakarat2 görmüyor, iki kelime alt sınırın "
     "altında.** Çıpa: 28:71-72 gece/gündüz döngüsü üzerine **karşı-olgusal nedensellik** kuruyor "
     "(إِن جَعَلَ ... سَرْمَدًا) — **kademe L2 ve sûrede ilk kez L2 gerçek bir doğa olgusuna "
     "uygulanıyor**; bu ayet aynı olguyu adlandırıp işlevini veriyor — **kademe L1.** Mekanizma, ölçü "
     "ya da sayısal ilişki yok: **L3 ve L4 yok.**"),
74: ("**Sûrenin tek tam-ayet nakaratının ikinci ucu ve `dugum` alanı burada temsilciyi kaydediyor: "
     "temsil=[28,62].** Alan, iki özdeş ayetten hangisinin 'asıl' sayılacağını belirliyor — 28:62 "
     "temsilci, 28:74 tekrar. **Sûre 26'da nakaratların altı ölçütü şişirdiği bulgusunun düzeltme "
     "mekanizması bu alan** (26'da 41 ★★★ → 27 ayrı yapı, %18,1 → %11,9); sûre 28'de tek kez "
     "kullanılıyor ve **ikisi de yıldızsız olduğu için yıldız sayısını hiç değiştirmiyor.** يوم, ندي, "
     "زعم üçü de burada tükeniyor; ندي'nin beş geçişinin **üçü nakaratın içinde** (28:62, 65, 74), "
     "ikisi Mûsâ sahnesinde (28:30, 46)."),
75: ("**Beş kök burada tükeniyor** (أمم, شهد, برهن, حقق, فري). برهن kökünün iki geçişi sûrenin iki ucunu "
     "tutuyor: **28:32'de فَذَٰنِكَ بُرْهَٰنَانِ مِن رَّبِّكَ** (Mûsâ'ya verilen iki delil) ve burada "
     "**هَاتُوا۟ بُرْهَٰنَكُمْ** (ortak koşanlardan istenen delil) — kırk üç ayet arayla, biri verilen "
     "biri istenen. Dikey katman bunu هات+برهن çarpanıyla haber veriyordu (×914,0 / ×810,8) ama satır "
     "**[B tek sahne 4 ayet]**, yani çarpan tek bir sahneden geliyor: **artefakt tipi, yorumlanmadı.** "
     "Esmâ tokeni شَهِيد orta konumda, mühürsüz, göndergesi her ümmetten çıkarılan bir tanık — "
     "**ARTEFAKT**; sûrenin on üçüncü mühürsüz tokeni, on birinci artefakt."),
76: ("**Sûrenin üçüncü ve son adlı aktörü burada giriyor** — Firavun, Hâmân, Hârûn'dan sonra Kārûn; "
     "sûrenin adlı aktör envanteri böylece yedi isimle kapanıyor. İmza iki yerde: **simetri sim[0]=9, "
     "okumada ölçülen en yüksek değer**; ve hapaks نوأ, korpusta tek ayette bulunan bir fiil ve tam da "
     "hazinenin ağırlığını anlatan kelime. **Dördüncü kez aynı desen: sûrenin en uzun ayetlerinden biri "
     "bir hapaks taşıyor ve ★★★ alıyor** (28:15 n=38, 28:76 n=29). فرح kökü sûrede iki geçişli ve ikisi "
     "de bu ayette, biri nehiy biri sıfat — 28:16'nın غفر üçlemesiyle aynı yapı."),
77: ("**Dört ayrı kökün ikilendiği ikinci ayet** (birincisi 28:50) ve burada üçü **karşıt çift** olarak "
     "kuruluyor: ٱبْتَغِ/لَا تَبْغِ (ara/arama), أَحْسِن/أَحْسَنَ (sen iyilik et/O iyilik etti), "
     "ٱلْفَسَادَ/ٱلْمُفْسِدِين. **بغي kökünün aynı ayette biri emir biri nehiy olması** — ve aradaki tek "
     "farkın nesnede olması — sûrede görülen kök-ikileme yapılarının en simetriği; `ikile` sayıyor ama "
     "karşıtlık yönünü tutmuyor. **Üç lafız token ile sûrenin en yüksek lafız yoğunluğu** (allah "
     "z=1,78) ve yıldızın tek kaynağı bu. Esmâ tokeni آخِر orta konumda, sûrede ikinci kez ve yine "
     "artefakt; ikisinin de göndergesi âhiret."),
78: ("**Sekiz kök burada tükeniyor** (عند, قبل, قرن, شدد, قوي, كثر, سأل, جرم) — okumada tek ayette en "
     "çok kök tüketen vaka. Üçü (شدد, قوي, كثر) **tek bir karşılaştırma cümlesinde** toplanıyor: "
     "أَشَدُّ مِنْهُ قُوَّةً وَأَكْثَرُ جَمْعًا — ve bu, sûrede ölçülen **üçüncü ve dördüncü açık üstünlük "
     "karşılaştırması** (28:34 أَفْصَحُ مِنِّى, 28:49 أَهْدَىٰ مِنْهُمَآ, burada iki tane birden). "
     "**Hâlâ hiçbir alanda etiketlenmiyor**; fig boş, kip yalnız INTG/NEG/CERT tutuyor. **Sûrede dört "
     "karşılaştırma vakası birikti ve hiçbiri ölçülmüyor — KAPATILAMAZ.** قوي kökünün üç geçişi: 28:26 "
     "(işçi övgüsü) · 28:76 (hazineyi taşıyanlar) · 28:78 (helâk edilenler) — **üç ayrı özne, üçü de "
     "bir güç kıyaslamasında.**"),
79: ("**Kafiye alanının tanımı burada kesinleşiyor.** Fâsıla عَظِيم, harfi **م**, komşuları ن — bu, "
     "28:28'deki kırılma koşulunun aynısı görünüyor ama kafiye_kirik=0. **Sebep: `fs` alanının üçüncü "
     "ögesi harf değil SINIF ve -îm ile -ûn/-în aynı N sınıfında.** Sûre 28'in ن-dışı yedi fâsılası "
     "sınıflarıyla: 28:1 (ٓ) · 28:16 ٱلرَّحِيم (**N**) · 28:22 ٱلسَّبِيل (ل) · 28:23-24 (R) · **28:28 "
     "وَكِيل (ل, KIRIK)** · 28:79 عَظِيم (**N**). **Alan tutarlı: sapan harf kırılma saymıyor, sapan "
     "sınıf sayıyor.** İkinci not: yedi kök burada tükeniyor — 28:78'in sekizinden sonra ikinci en "
     "yüksek."),
80: ("**Blok, aynı z değerinin iki ayrı ayette tekrarlanmasıyla kapanıyor:** 28:78 ve 28:80 ikisi de iki "
     "edilgen fiil / beş toplam fiil taşıyor, ikisinin de pas z'si **1,95**, ikisi de ★ — aradaki fark "
     "n=28 ve n=16, yani uzunluk iki katına yakın farklı ama **pas ölçütü uzunluğa bakmıyor, yalnız "
     "fiil oranına.** **Formülün beş ölçütünün paydaları farklı:** n mutlak, allah ve rab kelime "
     "sayısına bölünüyor, pas fiil sayısına, hapaks mutlak sayı — bu blok dördünü de canlı gösterdi. "
     "أتي kökü burada tükeniyor: sûrede on dokuz geçiş, قول (50) ve كون (37) dışında en yüksek. ثوب "
     "kökü sûrede yalnız burada ve tablo karşılığı iki anlam alanını da taşıyor: **karşılık doğru.**"),
81: ("نصر kökü burada tükeniyor ve **ikisi de bu ayette, biri fiil biri ism-i fâil**: يَنصُرُونَهُ (ona "
     "yardım ederler) ve ٱلْمُنتَصِرِين (kendini kurtaranlar, VIII. bab) — **aynı kök, iki bab, biri "
     "dışarıdan gelen yardım biri kendi kendine kurtuluş, ve ayet ikisini de olumsuzluyor** (kip NEG 2). "
     "İkinci not: dört xref 3-gram'ın dördü de **tek ayete (18:43)** düşüyor — okumada bir ayetin tüm "
     "xref yükünü tek hedefe yönelttiği üçüncü vaka (28:47→20:134, 28:60→42:36); esit2 yine boş."),
82: ("**صبح kökü burada tükeniyor ve sûredeki üç geçişi anlatının üç dönüm noktasını tutuyor:** 28:10 "
     "(annenin boşalan gönlü) · 28:18 (Mûsâ'nın korkusu) · 28:82 (temenni edenlerin dönüşü) — **üçü de "
     "أَصْبَحَ + hâl yapısında, üçü de bir iç hâlin değiştiği sabahta.** Hiçbir alan bunu bağlamıyor: "
     "esit2 boş, nakarat2 görmüyor (kalıp iki kelimeye ulaşmıyor), xref başka yönlere düşüyor — "
     "**sûrede kök-düzeyi bir yapının üç uca yayıldığı ve hiçbir ölçüm aracının göremediği en net "
     "örnek.** منن kökü de burada tükeniyor ve iki geçişi ters yönde: 28:5'te ezilenlere lütuf, burada "
     "konuşanlara lütuf. **Yedi kök tek ayette tükeniyor** — 28:78'in sekizinden sonra ikinci."),
83: ("**Sekiz kök tek ayette tükeniyor** — 28:78 ile berabere, okumanın tavanı. Ve ayet sûrenin açılış "
     "bölütüyle ölçülebilir bir karşıtlık kuruyor: عُلُوًّا فِى ٱلْأَرْضِ — **28:4'te Firavun için "
     "kullanılan tam ifade** (إِنَّ فِرْعَوْنَ عَلَا فِى ٱلْأَرْضِ) burada olumsuzlanarak âhiret yurdunun "
     "şartı hâline geliyor. علو sûrede üç geçişli (28:4 Firavun · 28:68 ilâhî yücelik · 28:83 "
     "büyüklenmeyenler) ve **kok_turkce karşılığı 'yücelik; böbürlenme' ikisini de taşıyor — P0 #5'in "
     "OLUMLU örneği.** فسد de dört geçişle tükeniyor ve ilk geçişi yine 28:4'teydi: **sûrenin ilk on "
     "ayetinde Firavun'a atfedilen iki nitelik, son on ayette âhiret yurdunun olumsuz şartı olarak "
     "yeniden kuruluyor — ve bunu ölçen tek şey sûre_geçiş sayacı.** Blokta üç alanın da boş olduğu tek "
     "ayet."),
84: ("**Üç kök birden ikileniyor ve üçü de ayetin iki yarısını simetrik kuruyor** — جيأ (kim gelirse / "
     "kim gelirse), سوأ (kötülükle / kötülükler), عمل (işleyenler / yaptıkları); `sim` alanı [6,1,7,2] "
     "yazıyor ve sim[0]=6 blokta en yüksek (28:76'nın 9'undan sonra ikinci). Bağ tarafında: جاء حسنة "
     "خير üç kelimesi **27:89**'a düşüyor — oturumun açılışında işaret edilen üç sûre-27 bağından "
     "**üçüncüsü ve sonuncusu.** حسن, خير, سوأ, جزي, عمل — beş kök burada tükeniyor."),
85: ("**Sûrenin tek iç düğümü burada kapanıyor:** 28:37'de açılan قَالَ رَبِّى أَعْلَمُ kalıbı kırk sekiz "
     "ayet sonra ikinci ucunu veriyor ve `dugum.ic`=1 iki ayette de kayıtlı — **sûre 28'in tek sûre-içi "
     "xref bağı bu.** Ve nakarat2 aynı iki ayeti جاء بالهدا من kalıbıyla da bağlıyor ama o kalıp "
     "süzgeçten geçemiyor (2 ayet, 3 kelime): **aynı iki ayet arasındaki bağ, iki farklı alanda iki "
     "farklı kalıpla görünüyor ve biri geçerli biri değil.** قول kökü **ellinci ve son geçişini** burada "
     "yapıyor; علم, جيأ, هدي, ضلل, بين, ردد de bitiyor — yedi kök. قُرْءان ise adli2'de **tip='kitab'** "
     "olarak kaydediliyor: sûrenin otuz yedi adlı aktör tokeni içinde kişi ya da kavim olmayan tek "
     "örnek. Esmâ tokeni مُبِين göndergesi ضَلَٰل — **ARTEFAKT**, sûrenin dördüncü مبين'i."),
86: ("**ظهر kökü burada tükeniyor ve sûredeki üç geçişi üç ayrı anlam alanına dağılıyor:** 28:17 "
     "ظَهِيرًا لِّلْمُجْرِمِينَ · 28:48 سِحْرَانِ تَظَٰهَرَا · 28:86 ظَهِيرًا لِّلْكَٰفِرِينَ. **Birinci ve "
     "üçüncü geçiş aynı kalıpta — ظَهِيرًا لِ + mefûl — ve altmış dokuz ayet arayla, biri Mûsâ'nın kendi "
     "ahdi, biri muhataba verilen emir**; nakarat2 görmüyor (iki kelime, alt sınırın altında). "
     "kok_turkce karşılığı 'sırt; zuhur, açığa çıkma' ve **üç tokenin hiçbiri 'zuhur' değil — P0 #5 "
     "vakası.** لقي, كتب, رحم, كفر de burada tükeniyor."),
87: ("**ربب ve كون sûredeki son geçişlerini burada yapıyor** — كون otuz yedi geçişle sûrenin en sık "
     "ikinci kökü, ربب on dokuz geçişle. İmza kip alanında: **NEG 2 + EMPH 2** — iki olumsuzlama ve "
     "ikisi de te'kid nûnuyla (يَصُدُّنَّكَ, تَكُونَنَّ); sûre 28'de EMPH etiketi yedi ayette geçiyor ve "
     "**ikisinin tek ayette toplandığı tek yer burası.** Aradaki tek olumlu emir وَٱدْعُ إِلَىٰ رَبِّكَ "
     "ve o da sûrenin son رَبّ'ini taşıyor: **iki yasak arasında bir emir, ve emrin nesnesi Rab** — "
     "ölçüm bunu üç ayrı alanda tutuyor (kip, edim, R) ama üçlü yapıyı tutan alan yok. نزل sûrede iki "
     "geçişli ve ikisi ters çatıda: 28:24 أَنزَلْتَ إِلَىَّ (etken), burada أُنزِلَتْ إِلَيْكَ (edilgen)."),
88: ("**Sûre, on sekiz ayet önce açılan iki kalıbın kapanışıyla bitiyor:** 28:70'in لَآ إِلَٰهَ إِلَّا "
     "هُوَ ve لَهُ ٱلْحُكْمُ وَإِلَيْهِ تُرْجَعُونَ ifadeleri burada birebir tekrarlanıyor — ikisi de dört "
     "kelime, ikisi de süzgeci geçiyor. **Ama esit2 iki ayeti bağlamıyor:** ortak dizi ayetin yarısından "
     "az, oran eşiğin altında — **nakarat2 iki kalıbı ayrı ayrı görüyor, esit2 bütünü görmüyor: iki "
     "alanın bölünmüş gördüğü bir yapı.** **Dokuz kök burada tükeniyor** (دعو, أله, أخر, كلل, شيأ, هلك, "
     "وجه, حكم, رجع) — okumanın tavanı. أله üç kez ve **biri lafız ikisi cins isim**; 28:71-72'de oran "
     "tersineydi (ikisi lafız biri cins) ve alan yine doğru ayırıyor. Yıldız kaynağı pas z=2,52, 28:60 "
     "ile birebir aynı değer ve aynı mekanizma."),
}
