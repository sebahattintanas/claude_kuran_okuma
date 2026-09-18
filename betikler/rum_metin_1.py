# -*- coding: utf-8 -*-
"""rum_metin_1.py — sûre 30 meal ve matematikçi merceği (30:1-30).
Ölçüm satırı burada YOK: defterden üretilir (olcum_bicim.py, ONARILMIŞ alanlarla)."""

MEAL = {
1: "Elif-Lâm-Mîm.",
2: "Rumlar yenildi.",
3: "En yakın yerde. Ama onlar, yenilgilerinden sonra galip gelecekler.",
4: "Birkaç yıl içinde. Önce de sonra da emir Allah'ındır. O gün inananlar sevinecek.",
5: "Allah'ın yardımıyla. O, dilediğine yardım eder; güçlüdür, merhametlidir.",
6: "Allah'ın vaadi. Allah vaadinden caymaz; ama insanların çoğu bilmez.",
7: "Onlar dünya hayatının görünen yüzünü bilirler; âhiretten ise habersizdirler.",
8: "Kendi içlerinde hiç düşünmediler mi? Allah, gökleri, yeri ve ikisi arasındakileri ancak gerçek üzere ve belirlenmiş bir süreyle yarattı. Ama insanların çoğu Rablerine kavuşmayı inkâr eder.",
9: "Yeryüzünde gezip kendilerinden öncekilerin sonunun nasıl olduğuna bakmadılar mı? Onlar kuvvetçe bunlardan daha güçlüydüler; toprağı sürüp kabarttılar ve onu bunların imar ettiğinden daha çok imar ettiler. Elçileri onlara apaçık delillerle geldi. Allah onlara zulmetmiyordu; asıl onlar kendilerine zulmediyorlardı.",
10: "Sonra kötülük edenlerin sonu daha da kötü oldu; çünkü Allah'ın âyetlerini yalanladılar ve onlarla alay ediyorlardı.",
11: "Allah yaratmayı başlatır, sonra onu tekrarlar; sonra O'na döndürülürsünüz.",
12: "Kıyametin koptuğu gün suçlular ümitlerini kesecekler.",
13: "Ortak koştuklarından kendilerine şefaatçi olmayacak; ortaklarını inkâr edecekler.",
14: "Kıyametin koptuğu gün, işte o gün ayrı ayrı olurlar.",
15: "İnanıp iyi işler yapanlar bir bahçede sevindirilirler.",
16: "İnkâr edip âyetlerimizi ve âhirete kavuşmayı yalanlayanlar ise azabın içinde hazır bulundurulurlar.",
17: "Öyleyse akşama girerken de sabaha ererken de Allah'ı tesbih edin.",
18: "Göklerde ve yerde hamd O'nadır; ikindide de öğle vaktine erdiğinizde de.",
19: "Diriyi ölüden çıkarır, ölüyü diriden çıkarır; yeryüzünü ölümünden sonra diriltir. Siz de işte böyle çıkarılacaksınız.",
20: "O'nun âyetlerinden biri de sizi topraktan yaratmasıdır; sonra siz birdenbire yayılan insanlar oluverdiniz.",
21: "O'nun âyetlerinden biri de, kendilerine ısınasınız diye size kendi türünüzden eşler yaratması ve aranıza sevgi ve merhamet koymasıdır. Bunda düşünen bir topluluk için elbette işaretler vardır.",
22: "O'nun âyetlerinden biri de göklerin ve yerin yaratılması, dillerinizin ve renklerinizin farklı olmasıdır. Bunda bilenler için elbette işaretler vardır.",
23: "O'nun âyetlerinden biri de gece ve gündüz uyumanız ve O'nun lütfundan istemenizdir. Bunda işiten bir topluluk için elbette işaretler vardır.",
24: "O'nun âyetlerinden biri de size korku ve umut olarak şimşeği göstermesi, gökten su indirip onunla yeryüzünü ölümünden sonra diriltmesidir. Bunda akleden bir topluluk için elbette işaretler vardır.",
25: "O'nun âyetlerinden biri de göğün ve yerin O'nun buyruğuyla ayakta durmasıdır. Sonra sizi yerden bir çağrıyla çağırdığında hemen çıkarsınız.",
26: "Göklerde ve yerde kim varsa O'nundur; hepsi O'na gönülden boyun eğmiştir.",
27: "Yaratmayı başlatan, sonra onu tekrarlayan O'dur; bu O'na daha kolaydır. Göklerde ve yerde en yüce sıfat O'nundur; O, güçlüdür, hikmet sahibidir.",
28: "Size kendinizden bir örnek verdi: Elinizin altındakilerden, size verdiğimiz rızıkta ortaklarınız var mı ki, onda eşit olasınız ve birbirinizden çekindiğiniz gibi onlardan da çekinesiniz? Akleden bir topluluk için âyetleri işte böyle açıklıyoruz.",
29: "Hayır, zulmedenler bilgisizce kendi heveslerine uydular. Allah'ın saptırdığını kim doğru yola iletebilir? Onların hiçbir yardımcısı da yoktur.",
30: "Yüzünü hanîf olarak dine çevir: Allah'ın insanları üzerinde yarattığı fıtrata. Allah'ın yaratışında değişme yoktur. Dosdoğru din budur; ama insanların çoğu bilmez.",
}

M = {
1: ("**Okumada ikinci kez aynı küme:** `الم` iskeletli altı ayetin beşi burada bağlanıyor ve altıncısı 29:1'di. "
    "Sûre 29 açılışında bu küme 'korpusun ikinci büyüğü' diye kaydedilmişti; **şimdi kümenin içinden ikinci ayet "
    "okunuyor ve `esit2` simetrik davranıyor** — 29:1 bu ayeti gösteriyordu, bu ayet de 29:1'i gösteriyor. "
    "`harf`/`harf3` farkı yine **19** (besmele) ve oran 0,136 — **üç sûrede üçüncü kez aynı değer**, besmele "
    "kirliliği sabit ve ölçülebilir olmayı sürdürüyor."),
2: ("**İki kelimelik bir ayet ★★★ alıyor ve mekanizma tamamen payda tarafında.** Aday 903'ün ikinci otomatik "
    "tetikleyicisi dördüncü sûrede ve aynı değerle (28:70 · 29:57 · 30:2): tek fiil, edilgen, oran 1,00, "
    "pas z=**5,38**. **Okumada ★★★ alan en kısa ayet** — 29:59'un beş kelimesini de geçiyor. `dis`=0 ve üç bağ "
    "alanı boş: **hiçbir yere bağlanmayan iki kelime, en yüksek nişanla.** İkinci not: `رُوم` sûrenin tek "
    "kavim-türü adlı aktörü ve rolü fâil — ama fiil edilgen olduğu için 'fâil' burada gramer öznesi, eylemin "
    "faili değil; **`rol` alanı çatıyı tutmuyor.**"),
3: ("**`غلب` kökü sûrede üç geçişli ve üçü de bu iki ardışık ayette; kök iki ayette tükeniyor.** Ve üçü üç ayrı "
    "çatıda: `غُلِبَتِ` (edilgen, geçmiş) · `غَلَبِهِمْ` (isim) · `سَيَغْلِبُونَ` (etken, gelecek). **Aynı kök, "
    "iki ayet, üç çatı ve yön tersine dönüyor** — 29:12/29:13'te `حمل` kökünün aynı deseni, okumada dördüncü kez. "
    "`kip` alanında **FUT** — okumada seyrek; sekiz kelimede dört GEN ve başka hâl yok."),
4: ("**ALAN AÇIĞI — `say` alanı `بِضْع`i görmüyor.** `say` on yedi kök tanıyor (`كثر` 167 · `أحد` 85 · `زوج` 81 · "
    "`قلل` 76 · `وحد` 68 · `عدد` 57 · `ثلث` 32 · `ثني` 29 · `سبع` 28 · `عشر` 27 · `ربع` 22 · `ألف` 22 · `ثمن` 19 · "
    "`خمس` 8 · `نصف` 7 · `تسع` 7 · `سدس` 5) ve `بضع` aralarında yok; kökün geçtiği altı ayetin (12:19, 12:42, "
    "12:62, 12:65, 12:88, 30:4) altısında da alan boş. **Bu, `F_ölçü` işaret ailesinin kör noktası ve tam da bir "
    "ölçülü öngörünün üzerinde:** 30:2-4 bir yenilgiyi, bir galibiyeti ve bir zaman sınırını bağlıyor. `بِضْع` "
    "belirsiz ama **sınırlı** bir nicelik ve birim adı (`سِنِين`) veriliyor. **29:14'ün `أَلْفَ سَنَةٍ إِلَّا "
    "خَمْسِينَ عَامًا`sı L4 (ölçü) olmuştu; bu ayet aynı yapıyı daha zayıf hâliyle taşıyor ve alan hiç "
    "görmüyor.**"),
5: ("**Sûrenin ilk mühürlü esmâ çifti ve geçerli — ama çift sûre 29'un ikisinden farklı:** orada `سَمِيع|عَلِيم` "
    "ve `عَزِيز|حَكِيم` vardı, burada **`عَزِيز|رَحِيم`**; `عَزِيز` ortak, ikinci terim değişiyor. **Dört sûrede "
    "mühürlü tokenlerde yanlış pozitif hâlâ sıfır.** `نصر` iki kez ve ikisi de aynı ayette, biri isim biri fiil — "
    "**kök tek ayette iki çatı veriyor**, 29:45'te `صلو` ile aynı desen. Payda: bir lafız sekiz kelimede 1,97; "
    "29:11'de bir lafız altı kelimede 2,80 vermişti."),
6: ("**Payda etkisinin dört sûrelik serisi tamamlanıyor:** 29:5 (2 lafız / 12 kelime → 2,80) · 29:11 (1 / 6 → "
    "2,80) · 30:5 (1 / 8 → 1,97) · **30:6 (2 / 11 → 3,11)** — aynı ölçüt, dört ayrı girdi; **oran tek belirleyici "
    "olmayı sürdürüyor** (aday 931'in altıncı vakası). `وعد` iki kez ve ikisi de aynı nesneyi gösteriyor; "
    "**ikisi arasında `خلف` fiili duruyor ve kök 29:6'da 'ardından gelme' anlamındaydı, burada 'caymak' — bu "
    "üçüncü anlam alanı `kok_turkce`de yok: P0 #5'in sûre 30'daki ilk vakası.**"),
7: ("**Bir önceki ayetin son kelimesi bu ayetin ilk kelimesi:** 30:6 `لَا يَعْلَمُونَ` ile bitiyor, 30:7 "
    "`يَعْلَمُونَ` ile başlıyor — **aynı fiil, olumsuzdan olumluya, ayet sınırında.** `nakarat3` bunu göremiyor "
    "(kalıp tek kelime ve ayet sınırını aşıyor); **`ikili` alanı da göremiyor, aynı sebeple.** Okumada bu yapının "
    "ilk kaydı. Esmâ: iki token, **ikisi de artefakt** ve `ظاهِر` orta konumda — sûre 28'de orta konumdaki yedi "
    "mühürsüz tokenin altısı artefakttı, bu yedincisi. `دنو` kökü tükeniyor ve iki geçişi zıt bağlamda: 30:3 "
    "`أَدْنَى ٱلْأَرْضِ` (mekân) / 30:7 `ٱلْحَيَوٰةِ ٱلدُّنْيَا` (varlıksal)."),
8: ("**P0 #5'in en temiz vakası tek ayette: `سمو` kökü iki kez ve iki ayrı anlam alanında** — `ٱلسَّمَٰوَٰتِ` "
    "(gökler, lemma `سَماء`) ve `مُّسَمًّى` (adlandırılmış, lemma `مُسَمًّى`). **Aynı kök, aynı ayet, biri gök "
    "biri ad.** `ikile` ikisini de sayıyor; **onarılmış olgu-lemma süzgeci yalnız birincisini olgu sayıyor** — "
    "29:53'te tarayıcıyı yanıltan kusur burada doğru çalışıyor. Çıpa: süre **adlandırılıyor, ölçülmüyor** — birim "
    "yok, sayı yok; 29:14 ile karşıtlık tam. **Kademe L1**, emsal 29:44. Tarayıcı vermedi: `G_bakış` `رأي`/`نظر` "
    "arıyor, ayette `فكر` var — **doğru negatif ama sebebi dar: düşünme çağrısı da bir gözlem çağrısıdır.**"),
9: ("**TARAYICI ADAYI — ve çıpa değil; üstelik bu ayet sûre 29'da yazılan bir DIŞLAMA KURALININ sınaması.** Aday "
    "924'te `G_bakış` emir kipine açılınca `فَٱنظُرْ كَيْفَ كَانَ عَٰقِبَةُ` kalıbı toplanmış ve **'o tarihe "
    "bakış çağrısıdır, olguya değil'** denip `عقب` kökü dışlanmıştı. **30:9 tam o kalıbı taşıyor ve `G_bakış` onu "
    "doğru biçimde vermiyor**; ayet listeye `B_ta'lîl` ailesinden giriyor. **Kademe L1, olgu = HAYIR.** Dışlama "
    "kuralı tutulan kümede ilk kez sınandı ve tuttu. **`كون` dört kez — 29:25'in `بعض` dördüyle berabere, "
    "okumanın tavanı**, ve dördü dört ayrı işlevde. `عمر` tek ayette iki kez ve kök burada tükeniyor. Son cümle "
    "**29:40'ın kapanışıyla birebir** — `xref` yakalıyor, `esit2` boş."),
10: ("**Beş fiil, beş ayrı bab — blokta ve okumada nadir.** `سوأ` iki kez ve biri fiil biri ism-i tafdîl: "
     "`أَسَٰٓـُٔوا۟` / `ٱلسُّوٓأَىٰ` — **fiil ile onun üstünlük biçimi aynı ayette.** 29:41'in `أَوْهَنَ "
     "ٱلْبُيُوتِ`ünde kaydedilen **karşılaştırmalı sıralama** yapısı burada tekrar ediyor ve merdivende yine "
     "karşılığı yok. `nakarat3` `كان عقبه الذين` kalıbını üç ayete çıkarıyor — blokun tek üç-ayetli kalıbı."),
11: ("**ÇIPA — KADEME L2, olgu = evet.** Emsal 29:19 (`بدأ`+`عود` döngü iddiası) ve onun emsali 27:64. **Aynı kök "
     "çifti, aynı nesne, aynı döngü iddiası** — tek fark konuşma edimi: 29:19 soru, burada düz haber. **Kademe "
     "iddia yapısını ölçüyor, konuşma edimini değil.** 🜁 yazıldı. **TARAYICI KAÇIRDI** — `G_bakış` `رأي`/`نظر` "
     "ve soru/emir kipi arıyor, ikisi de yok. Dikey katmanın haber verdiği ikili yine metinde: `عود` profilinde "
     "`بدأ` ×83,2 **[B2 donmuş kalıp 10 ayet]** — okumada sekizinci kez. `xref` kalıbı dört ayete bağlıyor ve "
     "biri **27:64**, biri **30:27**."),
12: ("**Beş kelimelik bir ayet `dugum.ic`=2 taşıyor — blokun en yüksek iç düğümü.** `وَيَوْمَ تَقُومُ "
     "ٱلسَّاعَةُ` kalıbı sûrede **üç kez** (30:12, 30:14, 30:55) ve `xref` üçünü de görüyor; `nakarat3` ikisini "
     "bağlıyor. **Sûre 30'un ilk sûre-içi kalıbı ve üç uçlu.** `بلس` korpusta yalnız beş ayette."),
13: ("**`شرك` iki kez ve ikisi de aynı iyelikli biçimde** — ayet aynı kelimeyi iki kez kullanıp arasında bir "
     "olumsuzlama kuruyor: ortaklardan şefaatçi *çıkmayacak*, ortaklar *inkâr edilecek*. **Aynı gönderge, iki "
     "gramer işlevi, iki olumsuz yön.** Blokun üç tamamen bağsız ayetinden biri."),
14: ("**İki ayet arayla aynı beş kelimelik yapı, aynı uzunluk, aynı fâsıla sınıfı — ve ikisi de yıldızsız.** Tek "
     "fark son kelime. **`esit2` bu çifti görmüyor** — iki ayet de beş kelimelik ve üçü ortak, ama alanın "
     "benzerlik ölçütü ayetin bütününe bakıyor ve oran eşiğin altında kalıyor. **`nakarat3` görüyor, `esit2` "
     "görmüyor: iki alan aynı olguya farklı çözünürlükle bakıyor.**"),
15: ("**İki kök birden korpusun alt ucundan ve ikisi de aynı ayette: `روض` iki ayet, `حبر` altı ayet.** Ama "
     "**hiçbiri hapaks değil** — `روض` iki ayette geçiyor, `hapaks2`'nin onarılmış ölçütü bile onu almıyor. "
     "**28:12'nin 'nadirlik yığılması ile hapaks ayrı şeyler' ayrımının sûre 30'daki ilk ve en keskin vakası**; "
     "ayet yalnız `pas`tan ★ alıyor. `fig2` **AMMA** veriyor — sûre 30'da ilk kez, korpusta 52 ayet."),
16: ("**İki ayet, iki `AMMA`, tam karşıtlık — ve ikisi de edilgen fiille bitiyor:** `يُحْبَرُونَ` / "
     "`مُحْضَرُونَ`. **Ama `pas` alanı yalnız birincisini sayıyor**; `مُحْضَرُون` ism-i mef'ûl olduğu için `vf` "
     "alanına girmiyor. **İki ayet aynı çatıda ama ölçüm ikisini farklı sayıyor** — 30:15 ★, 30:16 yıldızsız. "
     "Kaydedildi."),
17: ("**İKİ ÖLÇÜT BİRDEN EŞİĞİN ÜSTÜNDE: hapaks z=3,38 VE allah z=2,80.** Formül en büyüğünü alıyor, toplamıyor. "
     "**TAM SAYIM: korpusta iki ya da daha fazla ölçütü |z|>2 olan ayet 89; 30:17 sûre 30'daki tek örnek.** "
     "**Okumada ★★★'ı iki bağımsız kaynaktan alan ilk ayet** — 29:10'da `n` ve `allah` ikisi de eşiği geçmişti "
     "ama ★★ vermişti. **Formülün 'en büyük |z|' kuralı burada bilgi kaybediyor: iki bağımsız olgunun "
     "birlikteliği tek olgudan daha dikkat çekici olabilir, ama nişan aynı.** `مسو` korpusta yalnız bu ayette ve "
     "tek token. **İltifât** (13>2) — dört sûrede iltifâtların hiçbiri yıldız vermemişti, bu ayet yıldızını başka "
     "ölçütlerden alıyor."),
18: ("**İki ayet dört vakti sayıyor ve `say` alanı hiçbirini görmüyor:** akşam · sabah · ikindi · öğle. **Dört "
     "zaman dilimi, sıralı, ve ölçüm tarafında hiçbir alan bunu bir dizi olarak tutmuyor** — 30:4'te `بِضْع`in "
     "görülmemesiyle aynı aile: **alan niceliği sayıyor, ölçüyü değil.** `ظهر` kökü burada üçüncü anlamında "
     "(öğle vaktine ermek) ve `kok_turkce` karşılığı üçüncü alanı taşımıyor: **P0 #5'in sûre 30'daki ikinci "
     "vakası.**"),
19: ("**ÇIPA — KADEME L2, olgu = evet.** İddia yapısı: iki olgu arasında **yönlü bir dönüşüm** (ölüden diri, "
     "diriden ölü) ve üçüncü olguya (yerin dirilmesi) genişletme. Emsal **29:63** ve ortak kalıp `يُحْىِ "
     "ٱلْأَرْضَ بَعْدَ مَوْتِهَا` ikisinde de var. 🜁 yazıldı. **ÜÇ KÖK, ÜÇÜ DE ÜÇER KEZ — okumada ölçülen en "
     "yoğun ikileme deseni**; önceki tavan tek kökün dört tekrarıydı. Ve üçü aynı yapıyı kuruyor: `ٱلْحَىَّ مِنَ "
     "ٱلْمَيِّتِ` / `ٱلْمَيِّتَ مِنَ ٱلْحَىِّ` — **çapraz simetri.** Dört fiilin dördü de IV. babda ve dördü de "
     "IMPF: **`vf` ve `zmn` alanlarının tek değere kilitlendiği nadir bir ayet.** **TARAYICI KAÇIRDI** — düz "
     "haber."),
20: ("**Sûrenin omurgası burada açılıyor: `وَمِنْ ءَايَٰتِهِۦٓ` dizisi.** `nakarat3` kalıbı yakalıyor ve "
     "süzgeci geçiyor (4 kelime). Çıpa: bir köken adlandırılıyor ve bir sonuç veriliyor, ama iki olgu arasında "
     "mekanizma kurulmuyor. **Kademe L1**, emsal 29:44. Dikey katman bir sonraki adımı haber veriyor: `ترب` "
     "profilinde `نطف` *(nutfe)* var."),
21: ("**Üç `nakarat3` kalıbı birden geçiyor ve üçü de sûrenin omurgasını kuruyor:** `من ءايته ان` (dizinin "
     "başlığı) · `ان فا ذلك لءايت` (kapanışı) · `ان فا ذلك لءايت لقوم` (**dört ayette**). **Ayet bir kalıbın "
     "açılışı ile kapanışını aynı anda taşıyor.** Tarayıcı adayı ama çıpa değil: `B_ta'lîl` tetikliyor, amaç "
     "bildirimi var ama **iki olgu arasında sebep-sonuç kurulmuyor**; **kademe L1**, emsal 27:86. `ودد` kökü "
     "29:25'te kınanan sevgi bağlamındaydı, burada `وَجَعَلَ بَيْنَكُم مَّوَدَّةً` — **aynı kök, aynı `بين` "
     "edatıyla, biri kınanan biri lütuf.**"),
22: ("**On üç kelimede hiç fiil yok — blokun tek fiilsiz ayeti**; yedi GEN ile i'râb tek yöne kilitlenmiş. Çıpa: "
     "iki olgu adlandırılıyor ve çeşitlilik iki alanda örneklendiriliyor — ama **sınıflar adlandırılmıyor, "
     "mekanizma yok.** **Kademe L1**, emsal 27:61. **L4'ün sınıflama koluna en çok yaklaşan ve düşen ayet:** "
     "29:40'ta dört helâk türü ayrı ayrı adlandırılıp ayrı gruplara eşlenmişti; burada çeşitliliğin *varlığı* "
     "söyleniyor, türleri sayılmıyor. `خلف` tükeniyor ve iki geçişi iki ayrı alanda — **P0 #5'in üçüncü vakası "
     "ve aynı kökün üçüncü anlamı.**"),
23: ("**Üç olgu kökü (`نوم`, `ليل`, `نهر`) ve üçü de sûrede tek geçişli — ama tarayıcı ayeti vermiyor** çünkü "
     "hiçbir işaret ailesi tetiklenmiyor. Çıpa: uyku gece ve gündüzle **ilişkilendiriliyor** ama bağ nedensel "
     "değil zamansal. **Kademe L1**, emsal 27:18. `نهر` burada 'gündüz' anlamında ve `kok_turkce` karşılığı "
     "'ırmak' — **P0 #5'in dördüncü vakası; 28:72'de aynı kök aynı sorunla kaydedilmişti. Onarılmış olgu-lemma "
     "tablosu ikisini de olgu sayıyor: tablo doğru, tabloyu okuyan gloss yanlış.**"),
24: ("**ÇIPA — KADEME L2, olgu = evet.** Emsal 27:60 ve 29:63: `وَيُنَزِّلُ مِنَ ٱلسَّمَآءِ مَآءً فَيُحْىِۦ بِهِ "
     "ٱلْأَرْضَ` — **gökten inen su ile yerin dirilmesi arasında `بِهِ` ile açık sebep-sonuç**; kalıp 29:63'le "
     "birebir aynı. 🜁 yazıldı. **TARAYICI KAÇIRDI** — `رأي` var ama `G_bakış` soru/emir kipi şart koşuyor. "
     "**Bir ayet, üç olgu ve ikisi arasında mekanizma.** `برق` korpusta yalnız yedi ayette, `طمع` on ikide. "
     "Dikey katman ikisini de doğruluyor: `طمع` profilinde `خوف` ×17,8 ve ayette bizzat yan yana. **Dört "
     "`nakarat3` kalıbı birden** — blokun en bağlı ayeti; ikisi `الارض بعد موتها` ailesinden ve öbür ucu 30:19, "
     "**yani sûre içinde iki L2 çıpası aynı kalıpla bağlanıyor.**"),
25: ("**Sûre 30'un ilk `mm2` kaydı: `دَعَاكُمْ دَعْوَةً` — mef'ûl-i mutlak.** Sûre 29'da tek vaka vardı; "
     "**onarılmış alan üç sûrede dört kayıt veriyor.** Çıpa: göğün ve yerin ayakta durması bir bağımlılık iddiası "
     "ama bağlanan şey başka bir olgu değil, ilâhî buyruk. **Kademe L1**, emsal 29:60. `أرض` iki kez ve iki ayrı "
     "ölçekte: kozmik alan / insanların çıkacağı yer."),
26: ("**Blokun ikinci fiilsiz ayeti** — sekiz kelimede hiç fiil yok. `قنت` korpusta on iki ayette ve dikey "
     "katmanda `خشع` ile ×83,7 veriyor; **29:59'un `صبر` profilinde de `قنت` ×21,5 olarak görünmüştü — kök iki "
     "sûre arayla iki kez komşuluk tablosunda çıkıp burada metne giriyor.** `nakarat3` `فا السموت الارض` kalıbını "
     "30:18 ile bağlıyor ama süzgeci geçemiyor — sûre 30'un ilk süzgeç-altı kalıbı."),
27: ("**ÇIPA — KADEME L2, olgu = evet.** 30:11 ile **birebir aynı döngü iddiası** ve `nakarat3` ikisini "
     "bağlıyor. Emsal 29:19 ve 27:64. 🜁 yazıldı. **TARAYICI KAÇIRDI** — 30:11 gibi düz haber. **`بدأ` ve `عود` "
     "burada tükeniyor ve ikisi de yalnız bu iki ayette geçti: kök çifti sûrede bir kalıp olarak var, başka "
     "hiçbir yerde yok.** Ayet 30:11'e bir şey ekliyor: **`وَهُوَ أَهْوَنُ عَلَيْهِ` — karşılaştırmalı "
     "sıralama**, 29:41 ve 30:10 ile aynı yapı, **okumada üçüncü kez** ve merdivende yine karşılığı yok. Esmâ: "
     "sûrenin ikinci mühürlü çifti ve yine geçerli."),
28: ("**Yıldızın kaynağı n z=1,55 — eşiğin 0,05 üstünde.** 29:26'da `rab` z=1,45 ile eşiğin 0,05 **altında** "
     "kalmıştı: **aynı büyüklükte fark, ters yönde.** Blokun en uzun ayeti ve **tamamen bağsız** (`dis`=0, üç bağ "
     "alanı boş) — 29:35'te kaydedildiği gibi **kısalıkla bağsızlık arasında ilişki yok, uzunlukla da yok.** "
     "`خوف` iki kez ve ikisi karşılaştırma kuruyor: `تَخَافُونَهُمْ كَخِيفَتِكُمْ` — **fiil ve mastarı, `ك` "
     "benzetme edatıyla.**"),
29: ("**`هوي` kökü burada ve onarılmış olgu tablosunun `BAGLAM_GEREKLI` listesinde.** Lemma turunda ölçülmüştü: "
     "`هَواء` lemması hem 'hava' (14:43) hem 'heva, arzu' (28:50) taşıyor ve morfoloji ayırmıyor; kök olgu "
     "kümesinden **çıkarılmıştı.** **Bu ayet o kararı doğruluyor** — `أَهْوَآءَهُم` açıkça 'hevesler' ve olgu "
     "değil. **Karar tutulan kümede ilk kez sınandı ve tuttu.** `fig2` **IDRAB** veriyor — sûre 30'da ilk kez."),
30: ("**Beş kök birden ikileniyor — okumanın tavanı** (önceki tavan 29:10'un dördüydü). `فطر` ikisi de bu ayette: "
     "isim / fiil — **kök tek ayette tükeniyor ve isimden fiile geçiyor**, 29:45'te `صلو` ile aynı desen. Çıpa: "
     "`لَا تَبْدِيلَ لِخَلْقِ ٱللَّهِ` bir **değişmezlik iddiası** — mekanizma yok, ölçü yok, nedensellik yok, "
     "ama bir **düzenlilik** iddia ediliyor. **Kademe L1 verildi ve KAPATILAMAZ kaydedildi: merdivende "
     "'değişmezlik/düzenlilik iddiası' için basamak yok** — 29:41'in karşılaştırmalı sıralama boşluğuyla aynı "
     "aile. `nakarat3` `لكن اكثر الناس لا يعلمون` kalıbını 30:6 ile bağlıyor — **altı kelime, sûrenin en uzun "
     "nakaratı.**"),
}
