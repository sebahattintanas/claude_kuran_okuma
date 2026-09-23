# -*- coding: utf-8 -*-
"""lokman_metin_1.py — sûre 31 (Lokmân) meal ve matematikçi merceği, ayet 1-10.
Meal ve mercek ELLE yazılır; ölçüm satırı olcum_bicim.py'den gelir."""
MEAL = {
 1: "Elif Lâm Mîm.",
 2: "Bunlar hikmetli Kitab'ın âyetleridir,",
 3: "iyilik yapanlar (muhsinler) için bir hidayet ve rahmet olarak;",
 4: "onlar ki namazı kılarlar, zekâtı verirler ve âhirete kesin olarak inanırlar.",
 5: "İşte onlar Rablerinden bir hidayet üzeredirler ve işte onlar kurtuluşa erenlerin ta kendileridir.",
 6: "İnsanlardan kimi de, bilgisizce Allah'ın yolundan saptırmak ve onu alaya almak için boş sözü satın alır. İşte onlar için alçaltıcı bir azap vardır.",
 7: "Ona âyetlerimiz okunduğunda, sanki onları hiç işitmemiş gibi, sanki kulaklarında bir ağırlık varmış gibi büyüklenerek sırtını döner. Ona acı bir azabı müjdele.",
 8: "Şüphesiz iman edip sâlih ameller işleyenler için nimet cennetleri vardır;",
 9: "orada ebedî kalacaklar. Bu, Allah'ın gerçek vaadidir. O azîzdir, hakîmdir.",
 10: "Gökleri, görebileceğiniz direkler olmaksızın yarattı; sizi sarsmasın diye yeryüzüne sabit dağlar bıraktı ve orada her türden canlıyı yaydı. Gökten de su indirdik ve orada her güzel çiftten bitirdik.",
}
M = {
 1: "◇ Altı ALM açılışından biri: esit2 beş TAM bağ veriyor (2:1, 3:1, 29:1, 30:1, 32:1). Bu oturumun ALM pilotunda (ön-kayıtlı) ayet başı ve kelime başı dizilişi rastgeleden ayırt edilemedi; buradan dizilişe dair bir iddia kurulmaz.",
 2: "◇ Esmâ alanı حَكِيم'i yakalıyor ama sıfat Kitab'ın, Allah'ın değil; MÜHÜRSÜZ işareti doğru, fakat bu, esmâ mührünün token düzeyinde çalışamamasının (#9/#12) bir örneği daha. esit2 → 10:1 BENZER (0,92).",
 3: "◇ Üç kelime, bağ yok. Okuma gözlemi (ölçülmedi): 2:2'deki 'müttakîler için hidayet'in karşılığında burada 'muhsinler için hidayet ve rahmet' var; esit2 bu çifti bağlamıyor.",
 4: "◇ esit2 → 27:3 TAM: Neml açılışındaki müminlerin tanımı kelimesi kelimesine. Esmâ alanındaki آخِر 'âhiret'tir, ilâhî ad değil → yanlış pozitif (#9/#12).",
 5: "◇ esit2 → 2:5 TAM. 31:2-5, Neml ve Bakara açılışlarının tanım cümlelerini art arda taşıyor. ★★ kaynağı yalnız rab z=2,34: 8 kelimelik ayette tek Rab → payda etkisi (aday 909), içerik değil.",
 6: "◇ 'مِنَ ٱلنَّاسِ' (insanlardan kimi): insan üçlüsü ölçümünde nâs'ın 26 'mine'n-nâs' kalıbından biri. 'بِغَيْرِ عِلْمٍ' xref 22:3, 22:8, 31:20 ile tekrar eden bir kalıp; 'azâbun mühîn' 45:9 ile neredeyse aynı cümle.",
 7: "◇ Yeni kök وقر (kulakta ağırlık) — retroaktif gloss turu gerekecek. Emir kipi 'müjdele' azapla kullanılıyor (بشر). Edilgen 1/4: 'okunduğunda'. Tekil 3MS (o) 31:6'daki çoğul 'onlar'dan tekile iniyor; iltifât alanı 0.",
 8: "◇ Sâlihât köprüsü ölçümünde (bu oturum, ön-kayıtlı) 31:8, 33 köprü çapasından biri: öncül 31:6-7'de عذب, ardıl cennât. Blok bu yapıyı birebir taşıyor: saptıran → azap / iman + sâlihât → cennet.",
 9: "◇ Esmâ عَزِيز + حَكِيم SON konumda MÜHÜR — geçerli (bloktaki tek gerçek mühür). ★ kaynağı yalnız allah z=1,97 (8 kelimede 1 lafız). nakarat3 'وعد أله حقق' süzgeci geçmiyor.",
 10: "◇ 🜁 ÇIPA ADAYI (okuma işareti): L2 · olgu EVET. İki nedensellik: dağlar → 'sizi sarsmasın diye' (أَن تَمِيدَ), gökten su → bitki çiftleri. 'Görebileceğiniz direkler olmaksızın' algı/durum ayrımına yakın ama karşılaştırma yok → L3 değil. TARAYICI v4 bu ayeti aday VERMEDİ (koşuldu): amaç أَن + muzârî ile kuruluyor, lâm ile değil — aday 948'e bir veri. xref 13:2 (direksiz gök, 'görüyorsunuz'), 16:15, 21:31 (sarsmasın diye dağlar). Esmâ كَرِيم 'güzel çift'in sıfatı → yanlış pozitif.",
}

MEAL.update({
 11: "Bu, Allah'ın yaratmasıdır. Şimdi gösterin bana, O'ndan başkaları ne yarattı? Hayır, zalimler apaçık bir sapkınlık içindedir.",
 12: "Andolsun, Lokmân'a 'Allah'a şükret' diye hikmet verdik. Kim şükrederse ancak kendisi için şükreder; kim nankörlük ederse, şüphesiz Allah ganîdir, hamîddir.",
 13: "Hani Lokmân oğluna öğüt vererek demişti ki: 'Yavrucuğum, Allah'a ortak koşma; şüphesiz şirk büyük bir zulümdür.'",
 14: "İnsana da anne babası hakkında tavsiyede bulunduk — annesi onu zayıflık üstüne zayıflıkla taşıdı, sütten kesilmesi de iki yıl içindedir —: 'Bana ve anne babana şükret; dönüş banadır.'",
 15: "Eğer seni, hakkında bilgin olmayan bir şeyi bana ortak koşman için zorlarlarsa onlara itaat etme; dünyada onlarla iyi geçin ve bana yönelenin yoluna uy. Sonra dönüşünüz banadır; ben de size yapmakta olduklarınızı haber veririm.",
 16: "'Yavrucuğum, o bir hardal tanesi ağırlığında olsa da, bir kayanın içinde, göklerde ya da yerde bulunsa da Allah onu getirir. Şüphesiz Allah latîftir, habîrdir.'",
 17: "'Yavrucuğum, namazı kıl, iyiliği emret, kötülükten alıkoy ve başına gelene sabret; şüphesiz bunlar azim gerektiren işlerdendir.'",
 18: "'İnsanlara yanağını kibirle çevirme, yeryüzünde şımarık yürüme; şüphesiz Allah kendini beğenmiş, övünüp duran hiç kimseyi sevmez.'",
 19: "'Yürüyüşünde ölçülü ol, sesini alçalt; şüphesiz seslerin en çirkini eşeklerin sesidir.'",
 20: "Görmediniz mi, Allah göklerdekini ve yerdekini size boyun eğdirdi, açık ve gizli nimetlerini üzerinize bolca verdi? İnsanlardan kimi de bir bilgi, bir yol gösterici ve aydınlatıcı bir kitap olmadan Allah hakkında tartışır.",
})
M.update({
 11: "◇ TARAYICI v4 adayı (G_bakış, 'gösterin bana'): olgu yok, genel yaratma ve meydan okuma → L0 · olgu HAYIR → tarayıcı yanlış pozitifi. xref 35:40, 46:4: fiil-khalk turundaki (bu oturum) meydan okuma listesinin ayetleri. Ama o turun kişi-etiketi kuralı 31:11'i kaçırmıştı: fiil 3MS, özne 'O'ndan başkaları' (çoğul) → kişi etiketi özneyi vermiyor, ikinci vaka. Esmâ مُبِين 'sapkınlığın' sıfatı → yanlış pozitif.",
 12: "◇ Lokmân adlı aktör olarak ilk kez. حكم kökü 31:2'deki 'hikmetli Kitab'dan sonra burada 'hikmet verdik'. شكر ×3. Mühür غَنِيّ + حَمِيد geçerli. xref 27:40: Süleyman'ın 'kim şükrederse kendisi için şükreder…' sözüyle aynı yapı; şükür, Süleyman merceğinde üç sahneli köklerden biriydi. ★ kaynağı allah z=1,69; kafiye kırığı (د, iki ن arasında) gerçek ama formül eklemedi (mx > 1,5).",
 13: "◇ Lokmân fail ve konuşan. Ölçüm satırındaki بني 'bina, yapma' gloss'u yanlış: buradaki lemma ابن (يَٰبُنَىَّ, yavrucuğum) → gloss borcu #5b. 'Şirk büyük zulümdür': ظلم sûrede ikinci kez (31:11 zalimler).",
 14: "◇ Okuma gözlemi: Lokmân'ın öğüdü 31:13'te başlayıp 31:16'da sürüyor; 14-15 araya giren 1P/1S ilâhî söz ('tavsiye ettik… bana şükret'). İltifât alanı 0. 🜁 ÇIPA (okuma işareti): L4 adayı · olgu EVET: süreç (zayıflık üstüne zayıflıkla taşıma) + zaman birimi (sütten kesme iki yıl). Mekanizma yok, ölçü var → kademe TARTIŞMALI, KAPATILAMAZ (sûre 27-28 kademe tablosunda L4 hiç yoktu). TARAYICI v4 vermedi. ★'ın tek kaynağı kafiye kırığı: N→R geçişinin ilk ر'sı. xref 29:8, 46:15 (46:15: taşıma + sütten kesme otuz ay).",
 15: "◇ xref 29:8 neredeyse kelimesi kelimesine. Kafiye kırığı bayrağı var ama fâsıla ن, sûrenin önceki baskın sınıfı: iki ر komşusu arasında kalan son ن → geçiş bölgesi artefaktı. ★ kaynağı n z=1,76. نوب 'bana yönelen (inâbe)'.",
 16: "◇ TARAYICI v4 adayı (A_şart): hardal tanesi ağırlığı bir ölçü birimi, ama iddia bilgiye dair ve olgu örnek olarak kullanılıyor → L1 · olgu HAYIR → yanlış pozitif (sınırda; kademe okumaya bağlı). Mühür لَطِيف + خَبِير geçerli. xref 21:47 (hardal tanesi), 22:63 (latîf-habîr).",
 17: "◇ Okuma gözlemi (ölçülmedi): istisna turunda insân sıfatlarından istisna edilenleri tanımlayan iki tutum (namaz 70:22, sabır 11:11 ve 103:3) burada öğüt olarak art arda geçiyor. xref 42:38.",
 18: "◇ ★★★'ın tek kaynağı hapaks صعر (hapaks z=3,28): yıldızın otomatik ★★★ tetikleyicisi (borç #7), içerik değil. Blokta üç yeni kök: صعر, خدد, فخر. فَخُور mübalağa kalıbında. xref 17:37 (şımarık yürüme), 57:23 (her kibirli övüngen).",
 19: "◇ Bağ yok. 'Seslerin en çirkini' bir karşılaştırma, ama olgu adlandırma + nitelik düzeyinde → L1, çıpa değil. Yeni kökler قصد ve حمر.",
 20: "◇ TARAYICI v4 adayı (D_yeti, G_bakış): gök ve yerin boyun eğdirilmesi olgu adlandırma + işlev, nedensellik yok → L1 · olgu evet ama L2 altı → yanlış pozitif. nakarat3 'أَلَمْ تَرَوْا أَنَّ ٱللَّهَ' süzgeci GEÇİYOR (sûre içi tekrar). 'Mine'n-nâs' + 'bi-ğayri ilm' 31:6'dakinin aynısı: blok 31:6'nın kalıbıyla kapanıyor. Son cümle 22:8 ile neredeyse aynı. ★ kaynağı n z=1,87.",
})
