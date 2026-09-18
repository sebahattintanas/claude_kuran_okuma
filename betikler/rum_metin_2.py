# -*- coding: utf-8 -*-
"""rum_metin_2.py — sûre 30 meal ve matematikçi merceği (30:31-60)."""

MEAL = {
31: "O'na yönelmiş olarak; O'ndan sakının, namazı kılın ve ortak koşanlardan olmayın.",
32: "Dinlerini parçalayıp bölük bölük olanlardan. Her grup kendi elindekiyle sevinmektedir.",
33: "İnsanlara bir zarar dokunduğunda Rablerine yönelerek O'na yalvarırlar. Sonra onlara kendinden bir rahmet tattırınca, içlerinden bir grup hemen Rablerine ortak koşar.",
34: "Kendilerine verdiğimizi inkâr etsinler! Bir süre faydalanın; yakında bileceksiniz.",
35: "Yoksa onlara, ortak koştukları şeyler hakkında konuşan bir delil mi indirdik?",
36: "İnsanlara bir rahmet tattırdığımızda onunla sevinirler; elleriyle işledikleri yüzünden başlarına bir kötülük gelirse hemen umutsuzluğa düşerler.",
37: "Görmediler mi, Allah dilediğine rızkı genişletir, dilediğine de ölçüyle verir. Bunda inanan bir topluluk için elbette işaretler vardır.",
38: "Akrabaya, yoksula ve yolcuya hakkını ver. Allah'ın rızasını isteyenler için bu daha hayırlıdır; kurtuluşa erenler işte onlardır.",
39: "İnsanların malları içinde artsın diye verdiğiniz ribâ, Allah katında artmaz. Allah'ın rızasını isteyerek verdiğiniz zekâta gelince — işte kat kat artıranlar onlardır.",
40: "Sizi yaratan, sonra rızıklandıran, sonra öldüren, sonra dirilten Allah'tır. Ortaklarınızdan bunlardan birini yapabilen var mı? O, onların ortak koştuklarından münezzeh ve yücedir.",
41: "İnsanların elleriyle kazandıkları yüzünden karada ve denizde bozulma belirdi; yaptıklarının bir kısmını onlara tattırsın da belki dönerler diye.",
42: "De ki: Yeryüzünde gezin de öncekilerin sonunun nasıl olduğuna bakın. Onların çoğu ortak koşanlardı.",
43: "Allah'tan geri çevrilmesi imkânsız bir gün gelmeden önce yüzünü dosdoğru dine çevir. O gün bölük bölük ayrılırlar.",
44: "Kim inkâr ederse inkârı kendi aleyhinedir; kim iyi iş yaparsa kendileri için yer hazırlamış olurlar.",
45: "İnanıp iyi işler yapanları lütfundan ödüllendirsin diye. O, inkârcıları sevmez.",
46: "O'nun âyetlerinden biri de, rüzgârları müjdeciler olarak göndermesidir: size rahmetinden tattırsın, gemiler buyruğuyla yüzsün, lütfundan arayasınız ve şükredesiniz diye.",
47: "Andolsun, senden önce de elçileri kavimlerine gönderdik; onlara apaçık delillerle geldiler. Biz de suç işleyenlerden intikam aldık. İnananlara yardım etmek üzerimize bir hak oldu.",
48: "Rüzgârları gönderen Allah'tır; onlar bulutu kaldırır, O da bulutu gökte dilediği gibi yayar ve parça parça eder; derken yağmurun onun arasından çıktığını görürsün. Onu kullarından dilediğine ulaştırınca hemen sevinirler.",
49: "Oysa onlar, kendilerine yağmur indirilmeden önce umutlarını kesmişlerdi.",
50: "Allah'ın rahmetinin izlerine bak: yeryüzünü ölümünden sonra nasıl diriltiyor. İşte O, ölüleri de mutlaka diriltecektir; O, her şeye gücü yetendir.",
51: "Andolsun, bir rüzgâr göndersek de ekini sararmış görseler, ardından mutlaka nankörlüğe saparlar.",
52: "Sen ölülere işittiremezsin; arkalarını dönüp giderken sağırlara da çağrıyı işittiremezsin.",
53: "Körleri sapkınlıklarından çevirip doğru yola iletecek de değilsin. Sen ancak âyetlerimize inananlara işittirebilirsin; onlar teslim olmuş kimselerdir.",
54: "Sizi güçsüzlükten yaratan, sonra güçsüzlüğün ardından kuvvet veren, sonra kuvvetin ardından güçsüzlük ve ak saç veren Allah'tır. O dilediğini yaratır; bilendir, gücü yetendir.",
55: "Kıyametin koptuğu gün suçlular, bir saatten fazla kalmadıklarına yemin ederler. İşte böyle çevriliyorlardı.",
56: "Kendilerine ilim ve iman verilenler ise, \"Andolsun, Allah'ın kitabınca diriliş gününe kadar kaldınız; işte bu diriliş günüdür, ama siz bilmiyordunuz\" derler.",
57: "O gün zulmedenlere mazeretleri fayda vermez; hoşnutluk kazanmaları da istenmez.",
58: "Andolsun, bu Kur'an'da insanlara her türden örnek verdik. Onlara bir âyet getirsen, inkâr edenler mutlaka, \"Siz ancak boş şeyler peşindesiniz\" derler.",
59: "Bilmeyenlerin kalplerini Allah işte böyle mühürler.",
60: "Sabret; Allah'ın vaadi gerçektir. Kesin olarak inanmayanlar sakın seni hafifliğe sürüklemesin.",
}

M = {
31: ("**Bir önceki ayetin emri burada üç emre dağılıyor** — 30:30 `فَأَقِمْ وَجْهَكَ` (tekil), 30:31 üç çoğul "
     "emir. **Aynı `قوم` kökü iki ardışık ayette, biri 2. tekil biri 2. çoğul emir** ve `sah` alanı geçişi "
     "tutuyor, `ilt` alanı tutmuyor — **iltifât ölçütü ayet içi geçişleri sayıyor, ayet sınırındakini değil.** "
     "Blokun üç tamamen bağsız ayetinden biri."),
32: ("**İki dar kök aynı ayette ve ikisi de aynı kavramın iki adı:** `شِيَع` (11 ayet) ve `حِزْب` (17 ayet). "
     "**Ayet bir olguyu iki farklı kelimeyle iki kez adlandırıyor** ve ölçüm bunu bağlamıyor; `ikile` yalnız "
     "*aynı* kökün tekrarını sayıyor. `فرق` sûrede üç geçişli ve üçü de bu dört ayetlik bölütte, üç ayrı "
     "işlevde."),
33: ("**29:65'in davranış düzenliliği burada birebir tekrarlanıyor ve ölçüm iki ayeti bağlamıyor.** Orada gemiye "
     "binince ihlâs, karaya çıkınca şirk; burada zarar dokununca yakarış, rahmet tadınca şirk. **Aynı yapı, aynı "
     "sonuç, iki sûre — `esit2` boş, `nakarat3` boş, `xref` başka ayetlere gidiyor.** Çıpa: koşullu bağımlılık "
     "var ama bağlanan şey insan davranışı; **kademe L2, olgu = HAYIR**, emsal 29:65 ve 27:62. `رَبّ` sûrede üç "
     "geçişli ve **ikisi bu ayette** — kök neredeyse tek ayette tükeniyor, iki token ayetin iki ucunda: biri "
     "yakarışın öznesi biri şirkin nesnesi."),
34: ("**ADAY 929'UN ÜÇLÜSÜNÜN ÜÇÜNCÜ ÜYESİ OKUNDU — ve alanın davranışı doğrulandı.** Sûre 29'da 29:66'nın "
     "`esit2`'si 16:55 ve 30:34'e aynı oranla (0,9275) bağlanmıştı. **Şimdi üçüncü uçtan bakılınca oranlar "
     "simetrik DEĞİL:** 30:34 ↔ **16:55 = 1,0 (TAM)** · 30:34 ↔ 29:66 = 0,9275. **Üçlü eşkenar değil: 16:55 ile "
     "30:34 birebir aynı, 29:66 ikisinden de aynı uzaklıkta.** Aday 929'un kaydı tamamlanıyor: **alan üçlüyü üç "
     "ikili bağla veriyor ve bağların ağırlıkları farklı; küme yapısı ancak üç ayetin üçü de okunduğunda "
     "görünüyor.** Altı kelimede `i'râb` tamamen boş — **ve 29:66 da tam bu özelliği taşıyordu**; iki ayet hem "
     "`esit2` ile bağlı hem aynı gramer boşluğunu paylaşıyor, ölçüm ikincisini bağlamıyor."),
35: ("**Üç ardışık ayet aynı fâsılayla bitiyor: 30:33, 30:35 ve 30:40 hepsi `يُشْرِكُونَ`** — `شرك` kökü sûrede "
     "dokuz geçişli ve altısı bu blokta. `fs` alanı fâsılayı tutuyor ama **aynı kelimeyle biten ayetlerin "
     "dağılımını tutan alan yok**; `nakarat3` göremiyor çünkü tek kelime. Blokun ikinci tamamen bağsız ayeti."),
36: ("**Dikey katmanın üç ayet önce haber verdiği ikili burada kuruluyor:** 30:33'te `رحم` profilinde `قنط` "
     "×17,5 **[B tek sahne 5 ayet]** duruyordu; burada `رَحْمَةً ... يَقْنَطُونَ` olarak metinde — **okumada "
     "dokuzuncu kez.** `قنط` korpusta yalnız altı ayette; ayrıca **29:23'ün `يأس` profilinde de `قنط` ×61,4 "
     "olarak görünmüştü** — kök iki sûre arayla iki kez komşuluk tablosunda çıkıp burada metne giriyor. **Beş "
     "`xref` 3-gram'ının dördü tek ayete (42:48) düşüyor ama `esit2` boş.**"),
37: ("**OKUMADA İKİNCİ 'YAKIN' KADEMESİ** — 30:37 ↔ 39:52, oran **0,9649** (birincisi 29:28 ↔ 7:80, 0,9615). "
     "**`بسط`+`رزق`+`قدر` cümlesinin ÜÇÜNCÜ geçişi:** 28:82 (temenni edenlerin ağzından) · 29:62 (anlatıcı "
     "sesiyle) · 30:37 (soru kipinde). **Aynı önerme, üç sûre, üç ayrı konuşma edimi — ve üçünü bağlayan alan "
     "yok.** **Tarayıcı bu ayeti vermiyor ve bu DOĞRU:** `رأي` + `INTG` var, yani `G_bakış`ın iki şartı "
     "sağlanıyor; üçüncü şart olan olgu kökü sağlanmıyor çünkü `قدر` burada `يَقْدِرُ` (lemma `قَدَرَ`) ve "
     "onarılmış tabloda bu lemma olgu değil. **Lemma süzgeci tam olması gerektiği gibi çalışıyor: rızkın "
     "genişletilmesi bir doğa olgusu değil.**"),
38: ("**Üç `xref` 3-gram'ının üçü de tek ayete (17:26) düşüyor — neredeyse tam örtüşme — ama `esit2` boş.** "
     "30:33 ve 30:36'da da aynı desen vardı; **blokta üçüncü kez.** Aday 929'un kademe dağılımı bunu açıklıyor: "
     "**üç kademenin toplamı 1986 ayet, korpusun üçte biri; geri kalan örtüşmeler hiçbir kademeye girmiyor.** "
     "`خير` kökü burada karşılaştırmalı — **okumada dördüncü karşılaştırmalı sıralama** ve merdivende yine "
     "karşılığı yok."),
39: ("**`ربو` üç kez ve kök tek ayette tükeniyor — korpusta yalnız on beş ayetlik bir kök.** Üçü üç ayrı çatıda: "
     "isim / amaç (olumlu) / olumsuz. 30:3'te `غلب` iki ayette üç çatı vermişti, **burada tek ayette üç çatı.** "
     "Ve ayet kendi karşıtını kuruyor: `ربو` (artmaz) / `ٱلْمُضْعِفُونَ` (kat kat artıranlar) — **iki ayrı kökle "
     "aynı kavramın iki yönü**, 30:32'nin `شيع`/`حزب` çiftiyle aynı desen. Blokun üçüncü tamamen bağsız ayeti."),
40: ("**ÇIPA — KADEME L2, olgu = evet.** Dört aşamalı bir **döngü**: yaratma → rızıklandırma → öldürme → "
     "diriltme, üçü `ثُمَّ` ile sıralı. Emsal 30:11/30:27 ve 29:19. **Fark: orada iki aşama vardı, burada dört; "
     "ama yapı aynı — sıralı ve kapanan bir süreç iddiası.** 🜁 yazıldı. **TARAYICI KAÇIRDI:** `INTG` var, olgu "
     "kökleri var, ama **soru kipi tek başına bir işaret ailesi değil.** **Dört aşamalı dizi `say` alanında "
     "karşılıksız** — 30:17-18'de dört vakit, 30:4'te `بِضْع`; **sûrede üçüncü kez: alan ardışık bir diziyi sayı "
     "olarak tutmuyor.** Yedi fiil ve `bask`=3 ile 3MS yedi kez — ayet baştan sona tek özneye kilitli."),
41: ("**Tarayıcı adayı — `B_ta'lîl` ve `C_recâ` birlikte tetikliyor, olgu kökü `بحر`.** Nedensellik açık: insan "
     "kazanımı → karada ve denizde bozulma. **Ama iddianın öznesi `ٱلْفَسَاد`** — bir doğa süreci değil; kara ve "
     "deniz **olgunun yeri**, konusu değil. **Kademe L2, olgu = HAYIR**, emsal 29:65. **KAPATILAMAZ — ölçütün en "
     "sınırdaki vakası:** 'olgu' bayrağı olgunun *konusu* mu yoksa *yeri* mi sayılacağını tanımlamıyor ve sûre "
     "27-30'da bu ilk kez belirleyici oldu. `برر` kökü 'kara' anlamında ve esmâ alanı onu `بَرّ` sanıyor — "
     "**29:65'te birebir aynı artefakt.** `ظهر` tükeniyor ve üç geçişi üç ayrı alanda: 30:7 'görünen yüz', 30:18 "
     "'öğleye ermek', 30:41 'belirmek' — **P0 #5'in sûre 30'daki en zengin vakası.**"),
42: ("**`عقب` DIŞLAMA KURALI İKİNCİ KEZ SINANDI VE YİNE TUTTU.** Bu ayet kalıbı hem `نظر` hem emir kipiyle "
     "taşıyor — yani dışlama olmasaydı kesin aday olurdu — ve tarayıcı onu **doğru biçimde vermiyor.** Kademe L1, "
     "olgu = hayır. **`nakarat3` bu iki ayeti bağlıyor: 30:9 ↔ 30:42, beş kelimelik kalıp**; ve 30:43 bir sonraki "
     "ayette 30:30'a bağlanacak — **sûre kendi içinde iki ayrı uzun mesafeli halka kuruyor.**"),
43: ("**30:30'un emri on üç ayet sonra birebir tekrarlanıyor** ve `nakarat3` kalıbı görüyor ama **süzgeci "
     "geçiremiyor** (2 ayet / 3 kelime). **Sûre 30'un en belirgin sûre-içi halkalarından biri ölçümde süzgeç-altı "
     "kalıyor**; `dugum.ic` ise ikisini de 1 sayıyor. **İki alan aynı kalıba yine farklı davranıyor** — "
     "29:32↔29:33'ün üçüncü örneği. `صدع` korpusta yalnız beş ayette ve **beş ayrı lemma taşıyor** — envanterde "
     "token sayısı kadar lemma taşıyan nadir bir kök."),
44: ("**Dokuz kelimede tam simetrik bir karşıtlık ve `sim` alanı boş.** `مَن كَفَرَ ... وَمَنْ عَمِلَ صَٰلِحًا` — "
     "aynı yapı, karşıt yüklem, her iki kol da `فَ` ile sonuca bağlanıyor. **`sim` alanı bu ayette `None` "
     "veriyor ama daha az simetrik ayetlerde dolu; alanın neyi simetri saydığı ile metnin gösterdiği simetri "
     "örtüşmüyor.** `كفر` iki kez ve biri fiil biri isim — **fiil ve mastarı aynı cümlede**, 30:28'in "
     "`تَخَافُونَهُمْ كَخِيفَتِكُمْ`üyle aynı desen."),
45: ("`الذين ءامنوا وعملوا الصلحت` kalıbı sûrede **ikinci kez** (30:15, 30:45) ve `nakarat3` ikisini bağlıyor. "
     "Dikey katmanın `صلح` profilinde gösterdiği **[B2 donmuş kalıp 96 ayet]** — okumanın en yaygın donmuş "
     "kalıbı — burada ikinci kez metinde. `عمل` ve `صلح` tükeniyor ve **her geçişte yan yana: kök çifti sûrede "
     "hiç ayrılmıyor.**"),
46: ("**ÇIPA — KADEME L2, olgu = evet.** İki olgu arasında sebep-sonuç: **rüzgârların gönderilmesi → gemilerin "
     "yüzmesi.** Emsal 27:60 ve 29:63. 🜁 yazıldı. **TARAYICI YAKALADI — sûre 30'da ilk doğru pozitif.** "
     "**VE ÇIPA, BU OTURUMDA YAPILAN BİR ONARIM SAYESİNDE GÖRÜNÜYOR:** lemma turunda `anahtar_denetim.py` olgu "
     "kümesindeki `ريح` yazımının korpusta bulunmadığını ve rüzgârın `روح` kökü altında (`LEM:رِيح`) olduğunu "
     "yakalamıştı (aday 946). **Düzeltme olmasaydı bu ayet — sûrenin en açık L2'lerinden biri — havuza "
     "girmeyecekti.** Onarım tutulan kümede ilk kez fiilen iş gördü. **Dört gaye bildirimi tek ayette** ve `kip` "
     "alanı hiçbirini tutmuyor; **`B_ta'lîl` ailesi morfolojideki `PRP|PREF` etiketinden okuyor: alan ile aile "
     "farklı kaynaklara bakıyor.**"),
47: ("**`رسل` iki kez ve ikisi de aynı kökten fiil ve nesne:** `أَرْسَلْنَا ... رُسُلًا` — `mm2`'ye çok yakın "
     "bir yapı ama alan **boş**: mef'ûl-i mutlak değil, mef'ûl-i bih. **`mm2`'nin onarılmış ölçütü bu ayırımı "
     "doğru yapıyor.** **İki ayet arayla `نصر` kökünün iki ucu:** 30:5'te `بِنَصْرِ ٱللَّهِ` (Rumların "
     "galibiyeti), burada `نَصْرُ ٱلْمُؤْمِنِينَ` — **sûrenin açılışındaki tarihsel yardım ile kapanışa doğru "
     "genel ilke birbirine bağlanıyor** ve ölçüm bunu bağlamıyor."),
48: ("**ÇIPA — KADEME L4, MEKANİZMA KOLU. Okumanın ÜÇÜNCÜ L4 kaydı ve boş kalan üçüncü kolu dolduran ilk "
     "ayet.** L4'ün üç kolundan ölçü (29:14) ve sınıflama (29:40) örneklenmişti; **mekanizma kolu dört sûre "
     "boyunca boştu.** Bu ayet onu dolduruyor: **beş aşamalı bir süreç, her aşama adlandırılmış ve her biri bir "
     "öncekinden `فَ` ile türetilmiş** — rüzgârların gönderilmesi → bulutun kaldırılması (`فَتُثِيرُ سَحَابًا`) "
     "→ gökte yayılması (`فَيَبْسُطُهُۥ`) → parçalara ayrılması (`وَيَجْعَلُهُۥ كِسَفًا`) → yağmurun aradan "
     "çıkması (`فَتَرَى ٱلْوَدْقَ يَخْرُجُ مِنْ خِلَٰلِهِۦ`). **Ara durumlar adlandırılıyor** (`سَحَاب`, "
     "`كِسَف`, `وَدْق`) **ve çıkışın yeri belirtiliyor.** 30:24 aynı olguyu iki aşamada veriyordu ve L2 idi; "
     "**burada ara aşamalar açılınca kademe yükseliyor** — merdivenin aynı olguda iki farklı basamak "
     "verebildiğinin ilk ölçülü örneği. 🜁 yazıldı. **TARAYICI KAÇIRDI** — düz haber. **Üç kök korpusun en alt "
     "ucundan ve üçü de bu tek ayette: `ودق` 2 ayet · `كسف` 5 · `سحب` 11 — hiçbiri `hapaks2` değil**, ayetin "
     "yıldızı yalnız uzunluktan geliyor. `ثور` tükeniyor ve iki geçişi iki alanda: 30:9 toprağı sürmek, burada "
     "bulutu kaldırmak — **karşılık doğru.**"),
49: ("**Yıldızın kaynağı pas z=2,52 — okumada BEŞİNCİ kez tam bu değer:** 28:60 · 28:88 · 29:18 · 29:49 · 30:49, "
     "**beş ayet, dört sûre, aynı girdi-çıktı.** `قبل` iki kez ard arda ve kök sûrede yedi geçişli, son ikisi "
     "burada. `بلس` kökü sûrede iki geçişli: 30:12 (kıyamette) ve burada (yağmurdan önce) — **korpusta yalnız beş "
     "ayetlik bir kök ve ikisi bu sûrede, otuz yedi ayet arayla, biri âhiret biri dünya sahnesinde.**"),
50: ("**Yıldızın kaynağı `kafiye_kirik`=1. TEK kaynak** — en büyük |z| 0,70. **Sûre 30'un ilk kafiye kırılması "
     "ve okumada dördüncü 'yalnız kafiyeden' yıldız** (28:28, 29:21, 29:22, 30:50). **ÇIPA — KADEME L2, olgu = "
     "evet**; 30:19 ve 30:24'le aynı kalıp, emsal 29:63. 🜁 yazıldı. **TARAYICI YAKALADI — `G_bakış` ailesi, "
     "emir koluyla; sûre 30'daki ikinci doğru pozitif.** Aday 924'te `G_bakış`ı emir kipine açma kararı burada "
     "karşılığını veriyor, ve `عقب` dışlaması da doğru çalışıyor çünkü bu ayette `عقب` yok. **Sûrenin üç L2 "
     "çıpası aynı kalıbı paylaşıyor** (30:19, 30:24, 30:50) ama `nakarat3` yalnız ikisini bağlıyor: **üçünü "
     "birden gören alan yok.**"),
51: ("**Tarayıcı adayı — `A_şart`, olgu kökü `روح`.** Nedensellik var (rüzgâr → sararma → nankörlük) ama **son "
     "halka insan davranışı** ve ayetin iddiası doğa süreci hakkında değil, insanın ona tepkisi hakkında. "
     "**Kademe L2, olgu = HAYIR**, emsal 29:65 ve 30:33. **Bir önceki ayetle tam karşıtlık ve ölçüm ikisini "
     "bağlamıyor:** 30:50 rahmetin izine bakmayı emrediyor, 30:51 aynı bakışın ters sonucunu veriyor. `روح` "
     "tükeniyor — üç geçişi **rüzgârın üç ayrı işlevini** veriyor: müjdeci, bulut taşıyıcısı, ekin kurutucusu."),
52: ("**OKUMANIN EN YÜKSEK `esit2` DEĞERLERİNDEN BİRİ — ve karşı uç OKUNMUŞ bir ayet:** 30:52 ↔ 27:80, "
     "**0,9888**. Önceki 'yakin' kayıtları 0,9615 ve 0,9649 idi. **Beş `xref` 3-gram'ının beşi de aynı ayete "
     "düşüyor** — okumada ölçülen en tam örtüşme; fark tek kelimede. `سمع` sûrede dört geçişli ve ikisi bu "
     "ayette, ikisi de olumsuz."),
53: ("**İKİ ARDIŞIK AYET, İKİ ARDIŞIK AYETE BAĞLANIYOR: 30:52↔27:80 (0,9888) ve 30:53↔27:81 (0,9905).** Okumada "
     "ilk kez **bir ayet çifti, başka bir sûredeki ayet çiftine sırasıyla** bağlanıyor — ve **0,9905 okumanın en "
     "yüksek `esit2` değeri** (mukattaa TAM'ları hariç). **`esit2` bu yapıyı ikili bağlarla veriyor; çiftin çifte "
     "bağlandığını gören alan yok** — aday 929'un üçlü kaydıyla aynı aile: **alan ayet düzeyinde çalışıyor, bölüt "
     "düzeyinde değil.** `عمي` ile `صمم` iki ardışık ayette ve ikisi de aynı retorik yapıyı kuruyor; ölçüm "
     "bağlamıyor."),
54: ("**Yıldızın kaynağı `kafiye_kirik`=1. TEK kaynak** — **sûre 30'un ikinci kafiye kırılması ve okumada "
     "beşinci 'yalnız kafiyeden' yıldız.** **ÇIPA — KADEME L2, olgu = evet:** üç aşamalı bir insan ömrü döngüsü, "
     "ikisi `ثُمَّ` ile sıralı; emsal 30:40 ve 30:11/30:27. 🜁 yazıldı. **TARAYICI KAÇIRDI** — düz haber. **Beş "
     "kök birden ikileniyor ve `ضعف` üç kez** — 30:30'un beş kökle paylaştığı okuma tavanı, üstüne bir üçleme. "
     "Üç `ضعف` iki `قوي` ile **çapraz simetri** kuruyor: `ضَعْف → قُوَّة → ضَعْف` — 30:19'un üçlemesiyle aynı "
     "yapı, **ayet kendi döngüsünü kelime tekrarıyla görünür kılıyor.** Esmâ: **sûrenin üçüncü mühürlü çifti ve "
     "üçü de geçerli.**"),
55: ("**P0 #5'in sûre 30'daki en temiz vakası ve yine tek ayette: `سوع` iki kez, iki ayrı anlam alanında** — "
     "`ٱلسَّاعَةُ` (Kıyamet) ve `سَاعَةٍ` (bir saat). **Aynı kök, aynı ayet, biri eskatolojik terim biri zaman "
     "birimi, ve ayetin bütün retorik yükü tam bu ayrımın üzerinde.** `kok_turkce` karşılığı ('saat, vakit') "
     "birincisini taşımıyor; 30:8'in `سمو` vakasıyla aynı desen. **`يوم تقوم الساعه` kalıbı üç ayete çıkıyor ve "
     "süzgeci geçiyor** — sûrenin ilk bloğunda açılmış, kapanış bloğunda üçüncü ucunu veriyor: **kırk üç ayetlik "
     "açıklık.** `fig2` **QASEM** veriyor — sûre 30'da ilk kez."),
56: ("**`بعث` kökü sûrede iki geçişli ve ikisi de bu ayette, ikisi de aynı terkipte** (`يَوْمِ ٱلْبَعْثِ` ×2) — "
     "kök tek ayette tükeniyor ve **aynı ifade iki kez, biri zaman belirteci biri işaret edilen an.** `علم` de "
     "iki kez: verilen ilim / bilmiyordunuz — **aynı kök, ayetin iki ucunda, biri sahip olan biri yoksun.** Bir "
     "önceki ayetle karşıtlık tam: **suçlular 'bir saat' diyor, ilim verilenler 'diriliş gününe kadar' diyor — "
     "iki ayrı zaman ölçüsü, iki ayrı taraf**, ve ölçüm ikisini bağlamıyor."),
57: ("**İki yeni kök aynı ayette ve ikisi de korpusun alt ucundan** — `عذر` 11 ayet, `عتب` **4 ayet**; hiçbiri "
     "`hapaks2` değil. **30:48'in üç dar kökü, 30:15'in iki kökü ve burada iki kök: sûre 30'da bu desen dördüncü "
     "kez** ve her seferinde ayet dar köklerden değil başka ölçütten nişan alıyor. `عتب` korpusta dört ayette ve "
     "hepsi X. babda — **kökün neredeyse tek bir kalıba kilitli olduğu nadir bir vaka.**"),
58: ("**Dokuz kök birden burada tükeniyor** — 29:68'in dokuzuyla berabere, okumanın tavanı, ve ikisi de sûre "
     "kapanışına iki-üç ayet kala. **`أيي` kökü sûrenin en sık üçüncü kökü (17 geçiş) ve son geçişini burada "
     "veriyor** — ve son geçiş, dizinin kendisini değil ona gösterilen tepkiyi anlatıyor. **Sûre `وَمِنْ "
     "ءَايَٰتِهِۦ` dizisiyle kurulmuştu; kapanışta aynı kelime reddin nesnesi oluyor.** `adli2` `قُرْءان`ı "
     "**KİTAB türü** aktör sayıyor — sûre 30'un tek kitab-türü aktörü. **Sekiz kip işareti — okumanın tavanı.**"),
59: ("**Dikey katmanın sûre 29'da haber verdiği ikili burada metinde:** 29:21'de `قلب` kökünün profilinde `طبع` "
     "×39,4 duruyordu ve *'çok ayetli; ama buradaki lemma `قَلَبَ` (çevirme), o kalıp kalp anlamına ait: P0 #5 "
     "vakası'* diye kaydedilmişti. **Otuz dokuz ayet arayla, iki sûre sonra, `طبع` + `قلب` (kalp anlamında) tam o "
     "kalıpla metinde — ve bu kez lemma doğru. Komşuluk ölçümünün sûre sınırını aşarak doğrulandığı ilk vaka.** "
     "Yıldız `allah` z=1,97'den ve **30:5 ile 30:11 ile birebir aynı değer** (üçü de 1 lafız / 8 kelime): aynı "
     "oran → aynı z → aynı yıldız, sûre içinde üç kez."),
60: ("**`allah` z=1,47 — okumada ÜÇÜNCÜ kez tam bu değer** (29:6, 29:44, 30:60) ve **üçü de eşiğin 0,03 altında, "
     "üçü de yıldızsız.** **Sûre kapanışta açılışına dönüyor ve ölçüm bunu bağlamıyor:** 30:4'te `لِلَّهِ "
     "ٱلْأَمْرُ` ile vaat kurulmuş, 30:6'da `لَا يُخْلِفُ ٱللَّهُ وَعْدَهُۥ` ile pekiştirilmiş, burada `إِنَّ "
     "وَعْدَ ٱللَّهِ حَقٌّ` ile kapanıyor. **`وعد` kökünün üç geçişi sûrenin üç düğüm noktasında ve `nakarat3` "
     "hiçbirini bağlamıyor.** Dört kök burada tükeniyor ve biri sûrenin en sık kökü `أله` (24 geçiş)."),
}
