# -*- coding: utf-8 -*-
"""blok_25_51_60.py — sûre 25 altıncı blok (25:51-60). Üç رَحْمٰن tokeni ve ikinci doğa bölütü."""
import json
DIK = json.load(open('blok_dikey_25_51_60.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
51: "Dileseydik her beldeye bir uyarıcı gönderirdik.",
52: "Öyleyse inkârcılara boyun eğme; onunla, büyük bir cihatla mücadele et.",
53: "İki denizi salıveren odur: şu tatlı ve içimi kolay, şu tuzlu ve acı. İkisinin arasına bir berzah, aşılmaz bir engel koydu.",
54: "Sudan bir beşer yaratan ve onu soy ve hısımlık sahibi kılan odur. Rabbin güç yetirendir.",
55: "Allah'ın yanı sıra, kendilerine ne fayda ne zarar verebilen şeylere tapıyorlar. İnkârcı, Rabbine karşı destekçidir.",
56: "Seni ancak bir müjdeci ve bir uyarıcı olarak gönderdik.",
57: "De ki: Buna karşılık sizden bir ücret istemiyorum; ancak dileyen Rabbine bir yol tutsun.",
58: "Ölmeyen Diri'ye tevekkül et ve onu hamd ile tesbih et. Kullarının günahlarından haberdar olarak o yeter.",
59: "Gökleri, yeri ve ikisi arasındakileri altı günde yaratan, sonra arş üzerine istivâ edendir — Rahmân. Onu haberdar olana sor.",
60: "Onlara 'Rahmân'a secde edin' dendiğinde 'Rahmân da ne? Bize emrettiğine mi secde edeceğiz?' derler; ve bu onların nefretini artırır.",
}

OLCUM = {
51: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim şart, kip COND 1 · EMPH 1 · "
 "**şahıs 1P x4 — yedi kelimede dört birinci çoğul**, iltifât 0 · n=7 mora=34 harf=28 (n z=-0,58), "
 "fâsıla نَذِيرا *(uyarıcı)* → ا, A sınıfı, ACC — **25:1 ve 25:7'nin fâsılasıyla aynı kelime, "
 "sûrede üçüncü kez**; i'râb GEN 2 · ACC 1; bab I x2; zaman PERF x2; dış düğüm 0 · yıldız ★ yok · "
 "kökler شيأ *(dileme; şey)* · بعث *(gönderme, diriltme)* · كلل *(hep, bütün)* · قري *(belde, köy)* · "
 "نذر *(uyarma; adak)* · bağ: **25:45 ile aynı şart kalıbı** — وَلَوْ شَآءَ *(dileseydi)* orada 3MS, "
 "burada وَلَوْ شِئْنَا *(dileseydik)* 1P; ikisinde de gerçekleşmemiş alternatif (elle, L1, aday 571)"),
52: ("eksen: **lafız YOK · Rab YOK** · **esmâ كَبِير *(büyük)* 7. sırada = fâsıla, MÜHÜRSÜZ — "
 "ÖLÇÜM ARTEFAKTI (aday 461/546/555)**: nekre ve gönderge جِهَاد *(cihat, mücadele)*, sıfat cihadın; "
 "ölçüt (b) dışlıyor. **Aynı esmânın aynı sınıftan DÖRDÜNCÜ yanlış pozitifi** (25:19, 25:21, 25:52 "
 "كَبِير; 25:18 وَلِيّ) · aktör yok · edim emir, kip NEG 1 · IMPV 1 · şahıs 3FS x1 · 2MS x1 · "
 "3MP x1 · 3MS x1, **iltifât 1 — yön 1>23, SÛRENİN İKİNCİ İLTİFÂTI** · n=7 mora=41 harf=34 "
 "(n z=-0,58), fâsıla كَبِيرا *(büyük)* → ا, A sınıfı, ACC; **i'râb ACC 3**; bab III x1 · IV x1; "
 "zaman IMPF x1 · IMPV 1; **kök ikilemesi جهد *(cihat, çaba)* x2 — fiil + mef'ûl-i mutlak, bab III; "
 "blokta bab III'ün TEK geçişi** (aday 559 ile karşılaştır: 25:32/36/39 bab II, 25:46 bab I); dış "
 "düğüm 0 · yıldız ★ yok · kökler طوع *(güç yetirme, itaat)* · كفر *(inkâr, nankörlük)* · جهد "
 "*(cihat, çaba)* · كبر *(büyüklük; büyüklenme)* · bağ: **25:50 ile bitişik cevap** — orada "
 "insanların çoğu direniyordu, burada direnişe karşı emir (elle, L1, aday 572)"),
53: ("eksen: **lafız YOK · Rab YOK — gönderge وَهُوَ ٱلَّذِى *(o ki)*, 25:47 ve 25:48'den sonra "
 "üçüncü kez aynı biçimle** · esmâ yok · aktör yok — ٱلْبَحْرَيْنِ *(iki deniz)* tabloya girmiyor · "
 "edim haber, kip işareti yok · şahıs 3MS x3 · **3D x1 — okumada ikinci ikil (tesniye)**, iltifât 0 · "
 "n=15 mora=88 harf=71 (n z=0,27), fâsıla مَّحْجُورا *(engellenmiş)* → ا, A sınıfı, ACC — "
 "**25:22'nin fâsılasıyla AYNI KELİME**; **i'râb NOM 5 · ACC 4 — blokta NOM'un en yüksek olduğu "
 "ayet**; bab I x2; zaman PERF x2; **kök ikilemesi حجر *(taş; engel, yasak (hicr); kucak (hucûr))* "
 "x2 — 25:22'deki حِجْرا مَّحْجُورا *(engel, engellenmiş)* terkibinin BİREBİR TEKRARI**; biçim "
 "DIKKAT; dış düğüm 1 · yıldız ★ yok · kökler مرج *(salıverme, birbirine katma; karışıklık)* · بحر "
 "*(deniz)* · عذب *(azap; tatlı su)* · فرت *(tatlı ve içimi kolay (su))* · ملح *(tuz, tuzlu)* · أجج "
 "*(acı ve tuzlu (ücâc); alevlenme)* · جعل *(kılma, var etme)* · بين *(arası; açıklama)* · برزخ "
 "*(berzah, iki şeyi ayıran engel)* · حجر *(taş; engel, yasak (hicr); kucak (hucûr))* · bağ: xref "
 "بحر *(deniz)* + عذب *(tatlı)* + فرات *(fırat)* → **35:12**; **25:22 ile terkip özdeşliği** "
 "(elle, L1, aday 573)"),
54: ("eksen: **lafız YOK · رَبّ *(Rab)* 11. sırada — sûrenin yedinci Rab'bi** (rab z=1,45; **eşiğe "
 "en yakın ama AŞMIYOR**) · **esmâ قَدِير *(kadîr, güç yetiren)* 12. sırada = fâsıla, MÜHÜRSÜZ — "
 "GEÇERLİ**: doğrudan رَبّ *(Rab)*'bin yüklemi (وَكَانَ رَبُّكَ قَدِيرا) · aktör yok · edim haber · "
 "şahıs 3MS x5 · 2MS x1, iltifât 0 · n=12 mora=62 harf=53 (n z=-0,04), fâsıla قَدِيرا *(güç "
 "yetiren)* → ا, A sınıfı, ACC; **i'râb ACC 4 · GEN 1 · NOM 1**; bab I x3; zaman PERF x3; dış düğüm "
 "0 · yıldız ★ yok · kökler خلق *(yaratma)* · موه *(su)* · بشر *(müjde; beşer)* · جعل *(kılma, var "
 "etme)* · نسب *(soy, nesep)* · صهر *(eritme; hısımlık, sıhriyet)* · كون *(olmak; mekân, yer)* · "
 "ربب *(rab, terbiye etme)* · قدر *(ölçü, güç yetirme)* · bağ: **25:2 ile قدر ikinci geçişi** — "
 "orada فَقَدَّرَهُۥ تَقْدِيرا *(ona bir ölçü biçti)* fiil, burada قَدِيرا *(güç yetiren)* sıfat; "
 "**25:49 ile موه *(su)* ikinci geçişi** — orada su canlıları suluyor, burada sudan beşer "
 "yaratılıyor (elle, L1, aday 574)"),
55: ("eksen: **ALLAH LAFZI 4. sırada — sûrenin ÜÇÜNCÜ lafzı** (allah z=0,90) · **رَبّ *(Rab)* 13. "
 "sırada — sûrenin sekizinci Rab'bi** (rab z=1,20); **AYNI AYETTE HEM LAFIZ HEM RAB — sûrede İLK KEZ** · "
 "esmâ yok · aktör yok · edim haber, kip NEG 2 · şahıs 3MP x4 · 3MS x4, iltifât 0 · n=14 mora=69 "
 "harf=58 (n z=0,17), fâsıla ظَهِيرا *(destekçi, arka çıkan)* → ا, A sınıfı, ACC; i'râb GEN 3 · "
 "NOM 1 · ACC 1; bab I x4; zaman IMPF x3 · PERF x1; **dış düğüm 2** · yıldız ★ yok · kökler عبد "
 "*(kul, kulluk)* · دون *(beriki, başkası)* · أله *(ilâh; lafza-i celâl)* · نفع *(fayda)* · ضرر "
 "*(zarar)* · كون *(olmak; mekân, yer)* · كفر *(inkâr, nankörlük)* · ربب *(rab, terbiye etme)* · "
 "ظهر *(sırt; destek çıkma)* · bağ: xref ٱللَّه *(Allah)* + نفع *(fayda)* + يضرّ *(zarar verir)* → "
 "**6:71 · 10:106**; **25:3 ile BİREBİR KÖK DİZİSİ** — دون *(beriki, başkası)* + أله *(ilâh)* + نفع "
 "*(fayda)* + ضرر *(zarar)*; orada gönderge ءَالِهَة *(ilâhlar)* ve fayda/zarar sıralaması "
 "ضَرًّا-نَفْعًا, burada göndergesiz مَا *(şey)* ve sıralama TERS: نفع-ضرر (elle, L1, aday 575)"),
56: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · RES 1 · şahıs "
 "1P x2 · 2MS x1, **iltifât 1 — yön 3>12, SÛRENİN ÜÇÜNCÜ VE SON İLTİFÂTI** · n=5 mora=35 harf=25 — "
 "**25:46 ile birlikte sûrenin okunan en kısa ayeti** (n z=-0,79), fâsıla نَذِيرا *(uyarıcı)* → ا, "
 "A sınıfı, ACC — **sûrede dördüncü kez** (25:1, 7, 51, 56); **i'râb ACC 2**; bab IV x1; zaman "
 "PERF x1; **biçim HASR**; dış düğüm 1 · yıldız ★ yok · kökler رسل *(gönderme, elçi)* · بشر *(müjde; "
 "beşer)* · نذر *(uyarma; adak)* · bağ: xref أرسل *(gönderdi)* + مبشّر *(müjdeci)* + نذير *(uyarıcı)* "
 "→ **17:105**; **25:7 ile cevap** — orada فَيَكُونَ مَعَهُۥ نَذِيرا *(yanında bir uyarıcı olsaydı)* "
 "isteniyordu, burada elçinin KENDİSİ نَذِير *(uyarıcı)* olarak tanımlanıyor (elle, L1, aday 576)"),
57: ("eksen: **lafız YOK · رَبّ *(Rab)* 13. sırada — sûrenin dokuzuncu Rab'bi** (rab z=1,20) · esmâ "
 "yok · aktör yok · edim emir, kip IMPV 1 · NEG 1 · RES 1 · şahıs 3MS x4 · 2MS x1 · 1S x1 · 2MP x1, "
 "iltifât 0 · n=14 mora=58 harf=46 (n z=0,17), fâsıla سَبِيلا *(yol)* → ا, A sınıfı, ACC — **sûrede "
 "YEDİNCİ kez ve yedisi de fâsıla** (25:9, 17, 27, 34, 42, 44, 57); i'râb GEN 2 · ACC 1; bab I x3 · "
 "VIII x1; zaman IMPV 1 · IMPF x2 · PERF x1; **biçim HASR**; simetri [3,2,5,1]; **dış düğüm 2** · "
 "yıldız ★ yok · kökler قول *(söz söyleme)* · سأل *(isteme, dileme)* · أجر *(ücret, karşılık)* · "
 "شيأ *(dileme; şey)* · أخذ *(alma, edinme)* · ربب *(rab, terbiye etme)* · سبل *(yol)* · bağ: xref "
 "اتّخذ *(edindi)* + ربّ *(Rab)* + سبيل *(yol)* → **73:19 · 76:29**; **25:27 ile karşıtlık** — orada "
 "ٱتَّخَذْتُ مَعَ ٱلرَّسُولِ سَبِيلا *(elçiyle bir yol tutsaydım)* geçmiş temenni, burada aynı fiil "
 "ve aynı nesne GELECEK imkân olarak (elle, L1, adaylar 551, 564)"),
58: ("eksen: **lafız YOK · Rab YOK — gönderge ٱلْحَىِّ ٱلَّذِى لَا يَمُوتُ *(ölmeyen Diri)*, sûrede "
 "gönderge ilk kez BİR SIFATLA veriliyor** · **esmâ خَبِير *(haberdar)* 13. sırada = fâsıla, "
 "MÜHÜRSÜZ — GEÇERLİ**: كَفَىٰ بِهِۦ … خَبِيرا, temyiz ve göndergesi ilâhî · aktör yok · edim emir, "
 "kip IMPV 2 · NEG 1 · şahıs 3MS x5 · 2MS x2, iltifât 0 · n=13 mora=65 harf=56 (n z=0,06), fâsıla "
 "خَبِيرا *(haberdar)* → ا, A sınıfı, ACC; **i'râb GEN 4 · ACC 1**; bab I x2 · II x1 · V x1; zaman "
 "IMPV 2 · IMPF x1 · PERF x1; dış düğüm 1 · yıldız ★ yok · kökler وكل *(vekil kılma, tevekkül)* · "
 "حيي *(diri olma, hayat)* · موت *(ölüm)* · سبح *(tesbih, tenzih)* · حمد *(hamd, övgü)* · كفي "
 "*(yetme, kâfi gelme)* · ذنب *(günah, suç)* · عبد *(kul, kulluk)* · خبر *(haber; haberdar olma)* · "
 "bağ: xref ذنب *(günah)* + عبد *(kul)* + خبير *(haberdar)* → **17:17**; **25:31 ile كفي *(yetme, "
 "kâfi gelme)* ikinci geçişi** — orada كَفَىٰ بِرَبِّكَ هَادِيا وَنَصِيرا *(yol gösterici ve "
 "yardımcı olarak Rabbin yeter)*, burada كَفَىٰ بِهِۦ … خَبِيرا; **aynı kalıp, ama orada İKİ temyiz "
 "vardı ve tablo yalnız birini esmâ saymıştı** (elle, L1, aday 555); **25:3 ve 25:49 ile حيي/موت "
 "üçüncü karşılaşması** — burada ikisi TEK GÖNDERGEDE birleşiyor: ölmeyen Diri (elle, L1, aday 577)"),
59: ("eksen: **lafız YOK · Rab YOK — gönderge ٱلَّذِى *(o ki)* ve sonra ADLANDIRILIYOR** · **esmâ "
 "İKİ TOKEN: رَحْمٰن *(rahmân)* 14. sırada ORTA konum + خَبِير *(haberdar)* 17. sırada = fâsıla, "
 "MÜHÜRSÜZ**. رَحْمٰن: merfû, tek başına, önceki cümlenin gönderge açıklaması — **ADAY 549'un "
 "ikinci vakası, yine ÖZEL AD yönünde**. خَبِير: **GÖNDERGESİ BELİRSİZ** — فَسْـَٔلْ بِهِۦ خَبِيرا "
 "*(onu bir haberdara sor)*; 'haberdar' ilâhî de olabilir bilen bir kimse de; **KARAR VERİLMEDİ, "
 "belirsiz olarak kaydedildi** · aktör yok — ٱلْعَرْش *(arş)* tabloya girmiyor · edim emir, kip "
 "IMPV 1 · şahıs 3MS x3 · 3D x1 · 2MS x1, iltifât 0 · n=17 mora=86 harf=73 — **bloğun en uzun "
 "ayeti** (n z=0,49), fâsıla خَبِيرا *(haberdar)* → ا, A sınıfı, ACC — **25:58 ile bitişik ayette "
 "AYNI FÂSILA**; i'râb GEN 4 · ACC 3 · NOM 1; bab I x2 · VIII x1; zaman PERF x2 · IMPV 1; **açık "
 "sayı: ستت *(altı (sayı))* → سِتَّة *(altı)*, sûrede TEK sayı-adı**; simetri [3,5,10,1]; **dış "
 "düğüm 2** · yıldız ★ yok · kökler خلق *(yaratma)* · سمو *(ad; gök)* · أرض *(yer, yeryüzü)* · بين "
 "*(arası; açıklama)* · ستت *(altı (sayı))* · يوم *(gün)* · سوي *(düzenleme, denk kılma)* · عرش "
 "*(arş, taht)* · رحم *(rahmet, merhamet)* · سأل *(isteme, dileme)* · خبر *(haber; haberdar olma)* · "
 "bağ: xref أرض *(yer)* + بين *(ara)* + ستّة *(altı)* ve بين *(ara)* + ستّة *(altı)* + يوم *(gün)* → "
 "**ikisi de 32:4 VE 50:38**; **25:2 ile üçüncü halka** — orada مُلْكُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ "
 "*(göklerin ve yerin mülkü)* göndergesizdi, 25:26'da لِلرَّحْمَٰنِ *(Rahmân'a)* oldu, burada "
 "yaratma fiili + رَحْمٰن *(rahmân)* (elle, L1, aday 549)"),
60: ("eksen: **lafız YOK · Rab YOK** · **esmâ İKİ رَحْمٰن *(rahmân)* tokeni, 5. ve 8. sırada, ikisi "
 "de ORTA konum, MÜHÜRSÜZ — ADAY 549'UN BELİRLEYİCİ VAKASI**: ikincisi وَمَا ٱلرَّحْمَٰنُ *(Rahmân "
 "da ne)* sorusunun içinde, yani **itiraz edenler onu TANIMADIKLARI BİR AD olarak ele alıyor**; bu, "
 "esmâ (sıfat) değil ÖZEL AD kullanımının doğrudan metin içi kanıtı · **aktör: adsız 'nefer' 13. "
 "sırada — ÖLÇÜM ARTEFAKTI (aday 462)**: 13. kelime نُفُورا *(nefret, kaçış)*, نفر kökü; aktör "
 "dedektörü kökü 'nefer (bölük)' sanmış. **Sûre 25 makro profilinde 'adsız aktör: nefer' diye "
 "yazdığım kayıt bununla GERİ ÇEKİLİYOR** · edim soru + emir, kip IMPV 1 · INTG 1 · şahıs 3MP x4 · "
 "3MS x2 · 2MP x2 · 1P x2 · 2MS x1, iltifât 0 · n=13 mora=75 harf=65 (n z=0,06), fâsıla نُفُورا "
 "*(nefret, kaçış)* → ا, A sınıfı, ACC; i'râb GEN 1 · NOM 1 · ACC 1; bab I x6; zaman PERF x3 · "
 "IMPF x2 · IMPV 1; **edilgen 1 — قِيلَ *(dendi)*** (pas z=0,62); **kök ikilemesi قول *(söz "
 "söyleme)* x2 · سجد *(secde)* x2 · رحم *(rahmet, merhamet)* x2 — ÜÇ KÖK BİRDEN İKİLENİYOR, "
 "okumada ilk kez**; simetri [3,2,6,1]; dış düğüm 0 · yıldız ★ yok · **AYET SONUNDA TİLÂVET SECDESİ "
 "İŞARETİ ۩** · kökler قول *(söz söyleme)* · سجد *(secde)* · رحم *(rahmet, merhamet)* · أمر *(emir; "
 "iş)* · زيد *(artırma)* · نفر *(topluluk; kaçış, nefret)* · bağ: **25:26 ve 25:59 ile رَحْمٰن "
 "dizisi** — 25:26 mülkün sahibi, 25:59 yaratanın adı, burada TANINMAYAN ad (elle, L1, aday 549)"),
}

MERCEK = {
51: ("Şart kalıbı 25:45'ten geri geliyor ama fâili değişmiş: orada وَلَوْ شَآءَ *(dileseydi)* 3MS, "
 "burada وَلَوْ شِئْنَا *(dileseydik)* 1P. İkisi de gerçekleşmemiş alternatif kuruyor — biri "
 "gölgenin durgunluğu, biri her beldeye ayrı uyarıcı. Ölçülebilir bir yoğunluk: yedi kelimede dört "
 "birinci çoğul. Ve fâsıla نَذِيرا *(uyarıcı)* sûrede üçüncü kez (25:1, 25:7, burada); üçünde de "
 "nekre ve mansûb. قري *(belde, köy)* korpusta 57 geçişli ve dikey ölçümü ▸önce helâk x9,1 veriyor — "
 "kök korpusta ağırlıkla helâk bağlamında, burada uyarı bağlamında."),
52: ("Emir iki parçalı ve ikisi de aynı muhataba: bir yasak (فَلَا تُطِعِ *(boyun eğme)*) ve bir "
 "emir (وَجَٰهِدْهُم *(mücadele et)*). Ölçülebilir bir araç göstergesi: بِهِۦ *(onunla)* — zamirin "
 "göndergesi bir önceki bölütün ٱلْقُرْءَان'ı, yani mücadele aracı metin. جهد *(cihat, çaba)* iki "
 "kez ve fiil + mef'ûl-i mutlak yapısında; **bab III** — sûrede bu yapının dördüncü örneği ve "
 "ilk kez bab III (25:32/36/39 bab II, 25:46 bab I). Ve sûrenin ikinci iltifâtı burada, yön 1>23. "
 "جهد korpusta 41 geçişli ve dikey ölçümü ▸önce mal-can bağlamı veriyor; burada o bağlam YOK."),
53: ("Ayet iki su kütlesini karşı karşıya koyuyor ve her birini İKİ sıfatla niteliyor: عَذْبٌۭ "
 "فُرَاتٌۭ *(tatlı, içimi kolay)* ve مِلْحٌ أُجَاجٌۭ *(tuzlu, acı)*. Ölçülebilir bir simetri: iki "
 "yan, iki sıfat, ve dört sıfatın dördü de merfû nekre — ayetin NOM 5 sayımı buradan. Üç kök "
 "korpusta son derece seyrek: فرت *(tatlı ve içimi kolay (su))* n=3, أجج *(acı ve tuzlu (ücâc); "
 "alevlenme)* n=3, ملح *(tuz, tuzlu)* n=2 — üçü de bir arada yalnız burada ve 35:12'de. Ayıraç iki "
 "terimle veriliyor: بَرْزَخًۭا *(berzah)* ve وَحِجْرًۭا مَّحْجُورا *(aşılmaz engel)*; ikinci terim "
 "25:22'den BİREBİR geliyor — orada suçluların melekleri gördüğü gündü, burada iki su arasındaki "
 "sınır. برزخ *(berzah, iki şeyi ayıran engel)* korpusta 3 geçişli ve dikey ölçümü eşiği aşan "
 "komşu vermiyor. SINIR: ayet iki suyun karışmamasını SÖYLÜYOR, ayıraca iki ad veriyor, ama ne "
 "mekanizma ne ölçü veriyor."),
54: ("Yaratma tek maddeden veriliyor: خَلَقَ مِنَ ٱلْمَآءِ بَشَرا *(sudan bir beşer yarattı)*. "
 "Ölçülebilir bir ikili sonuç: نَسَبًۭا وَصِهْرا *(soy ve hısımlık)* — biri kan bağı, öteki evlilik "
 "bağı, ikisi de nekre mansûb ve yan yana. نسب *(soy, nesep)* korpusta 3 geçişli, صهر *(eritme; "
 "hısımlık, sıhriyet)* 2 geçişli; ikisi de seyrek ve burada bitişik — 25:23'ün هبو/نثر çiftiyle "
 "aynı desen. صهر'in tablodaki karşılığı 'eritme'ydi ve burada 'hısımlık'; kök düzeyi dikey "
 "komşuluk bu ayrımı yapmıyor (aday 529 sınıfı, sûrede yedinci vaka). Ve موه *(su)* sûrede ikinci "
 "kez: 25:49'da su canlıları suluyordu, burada sudan beşer yaratılıyor — aynı madde, iki işlev. "
 "SINIR: ayet suyu bir başlangıç maddesi olarak ADLANDIRIYOR ama ne süreç ne oran veriyor; "
 "'nesep ve sıhriyet' bir toplumsal sınıflandırma, biyolojik bir mekanizma değil."),
55: ("Sûrede ilk kez Allah lafzı ve رَبّ *(Rab)* AYNI AYETTE. Ölçülebilir bir konum: lafız 4. "
 "sırada ve مِن دُونِ ٱللَّهِ *(Allah'ın yanı sıra)* terkibinde, Rab 13. sırada ve عَلَىٰ رَبِّهِۦ "
 "*(Rabbine karşı)* terkibinde — biri tapınmanın dışlandığı taraf, öteki karşı çıkılan taraf. "
 "Ayet 25:3'ün kök dizisini birebir tekrarlıyor (دون *(beriki, başkası)* + أله *(ilâh)* + نفع "
 "*(fayda)* + ضرر *(zarar)*) ama iki fark var: 25:3'te gönderge ءَالِهَة *(ilâhlar)* açıkça "
 "adlandırılmıştı, burada مَا *(şey)* ile bırakılıyor; ve fayda/zarar sırası TERS (orada "
 "ضَرًّا-نَفْعًا, burada نفع-ضرر). ظهر *(sırt; destek çıkma)* korpusta 59 geçişli ve bu lemma "
 "(ظَهِير) seyrek; dikey ölçümü ▸önce arka-sırt bağlamı veriyor."),
56: ("Beş kelime — 25:46 ile birlikte sûrenin okunan en kısa ayeti. Ölçülebilir bir sınırlama: "
 "مَآ … إِلَّا, yani HASR; elçinin işlevi iki terime indiriliyor ve ikisi de nekre mansûb. Ve "
 "ikinci terim 25:7'nin isteğine doğrudan cevap: orada itirazcılar فَيَكُونَ مَعَهُۥ نَذِيرا "
 "*(yanında bir uyarıcı olsaydı)* diyordu — ikinci bir kişi istiyorlardı; burada elçinin KENDİSİ "
 "نَذِير *(uyarıcı)* olarak tanımlanıyor. İstek bir ekleme istiyordu, cevap bir özdeşleme veriyor. "
 "Sûrenin üçüncü ve son iltifâtı da burada, yön 3>12."),
57: ("Ücret reddi HASR ile kuruluyor ve istisna beklenmedik: مَآ أَسْـَٔلُكُمْ … مِنْ أَجْرٍ إِلَّا "
 "مَن شَآءَ *(sizden ücret istemiyorum, ancak dileyen…)* — istisna bir MİKTAR değil bir EYLEM. "
 "Ölçülebilir bir devir: istenen tek şey muhatabın kendi lehine bir eylemi. Fiil yine أخذ *(alma, "
 "edinme)* bab VIII, sûrede yedinci geçiş, ve nesne yine سَبِيلا *(yol)* — 25:27'de aynı fiil aynı "
 "nesneyle geçmiş temenniydi (ٱتَّخَذْتُ *(tutsaydım)*), burada gelecek imkân (يَتَّخِذَ *(tutsun)*). "
 "Ve سبل *(yol)* sûrede yedinci kez, yedisi de fâsıla konumunda (aday 564'ün karıştırıcı uyarısı "
 "burada yedinci kez doğrulanıyor)."),
58: ("Gönderge sûrede ilk kez bir SIFATLA veriliyor: ٱلْحَىِّ ٱلَّذِى لَا يَمُوتُ *(ölmeyen Diri)* — "
 "önceki yedi ٱلَّذِى *(o ki)* göndergesi bir FİİLLE tanımlıyordu (indiren, yaratan, kılan, "
 "gönderen, salıveren). Ölçülebilir bir fark: fiil-tanımından sıfat-tanımına geçiş. Ve حيي *(diri "
 "olma, hayat)* ile موت *(ölüm)* sûrede üçüncü kez karşılaşıyor, bu kez TEK GÖNDERGEDE: 25:3'te "
 "sahte ilâhlar ikisi üzerinde güçsüzdü, 25:49'da ikisi tek eylemde birleşiyordu, burada ikisi tek "
 "sıfatta — diri olan ve ölmeyen. كفي *(yetme, kâfi gelme)* 25:31'den geri geliyor ve kalıp aynı "
 "(كَفَىٰ بِ… + temyiz), ama orada İKİ temyiz vardı ve esmâ tablosu yalnız fâsıla olanı saymıştı; "
 "burada tek temyiz var ve sayılıyor. Aday 555'in konum-yanlılığı savı bu ayetle uyumlu."),
59: ("Ayet bir yaratma cümlesi kurup sonunda göndergeyi ADLANDIRIYOR: ٱلرَّحْمَٰنُ *(Rahmân)*, "
 "merfû ve tek başına. Ölçülebilir bir sözdizim: ad, cümlenin yüklemi değil; önceki ٱلَّذِى *(o ki)* "
 "göndergesinin açıklaması. Bu, 25:26'daki لِلرَّحْمَٰنِ *(Rahmân'a)* kullanımıyla aynı sınıfta — "
 "gönderge, sıfat değil. Sayı tek ve açık: سِتَّةِ أَيَّامٍ *(altı gün)*, ستت *(altı (sayı))* "
 "korpusta 8 geçişli ve dikey ölçümü ▸sonra arş-taht x179,3 · istivâ x123,8 veriyor — kök korpusta "
 "neredeyse yalnız bu terkiple, yani 'altı gün + istivâ + arş' donmuş bir dizi (aday 437 sınıfı) ve "
 "iki xref'in de aynı iki ayete düşmesi bundan. SINIR: ayet bir süre ADI veriyor (altı gün) ama ne "
 "sürenin ölçüsü ne içeriği tanımlanıyor; 'gün' burada takvim birimi olarak tanımlanmıyor."),
60: ("Bloğun kapanışı aday 549'u belirliyor: وَمَا ٱلرَّحْمَٰنُ *(Rahmân da ne)* — itiraz edenler "
 "adı TANIMADIKLARI bir ad olarak ele alıyor. Bir sıfat için bu soru sorulamaz; sorulabilmesi, "
 "kelimenin metin içinde ÖZEL AD gibi işlediğini gösteriyor. Ölçülebilir bir yoğunluk: üç kök birden "
 "ikileniyor — قول *(söz söyleme)*, سجد *(secde)*, رحم *(rahmet, merhamet)*; okumada ilk kez bir "
 "ayette üç ikileme. On üç kelimenin altı fiili de bab I. Kapanış نُفُورا *(nefret, kaçış)*; دikey "
 "ölçüm زيد *(artırma)* ▸sonra kaçış-nefret x54,8 veriyor — 'artırdı + nefret' korpusta sabit bir "
 "eşleşme. NOT — ÖLÇÜM ARTEFAKTI: aktör tablosu bu kelimeyi 'nefer (bölük)' sanıp adsız aktör "
 "olarak kaydetmiş; sûre makro profilinde bunu ben de aktarmıştım, GERİ ÇEKİLİYOR (aday 462)."),
}

ATLAMA = {
 "_blok_notu_25_51_60": ("BLOK BİLANÇOSU: **on ayetin onu da yıldızsız** — 25:41-50 ile birlikte "
  "**YİRMİ ARDIŞIK YILDIZSIZ AYET (25:41-60)**, okumada görülen en uzun dizi. Ve bu yirmi ayet "
  "sûrenin doğa/kozmoloji bölütünün TAMAMINI taşıyor. Bu blokta çıpa taşıyan üç ayet: **25:53** "
  "iki su kütlesi, her biri iki sıfatla, aralarında iki adlı ayıraç (بَرْزَخ *(berzah)* + حِجْر "
  "مَّحْجُور *(aşılmaz engel)*) · **25:54** sudan beşer yaratılması ve iki bağ türü (نَسَب *(soy)* / "
  "صِهْر *(hısımlık)*) · **25:59** altı gün + istivâ + arş. Üçü de YILDIZSIZ. En yüksek z değerleri "
  "25:54'te rab z=1,45 (eşiğin hemen altında). 🜁 ve 🜂 protokol gereği YAZILMADI (eşik ★★★). Kural "
  "çiğnenmedi. ADAY 561/565'e eklendi: sûre 25'in çıpa taşıyan SEKİZ ayetinin (25:25, 45, 46, 47, "
  "48, 49, 53, 54, 59) yalnız BİRİ yıldız alıyor (25:25, ★★, ve onun da kaynağı edilgenlik oranı, "
  "içerik değil). SINIR NOTU — üç ayet için de aynı: metin bir OLGU adlandırıyor ama ne mekanizma "
  "ne ölçü veriyor; 'berzahın fiziksel karşılığı', 'sudan yaratılışın biyokimyası' ya da 'altı "
  "günün süresi' üzerine hiçbir şey söylenmedi ve söylenmeyecek — yasaklı 'bilimsel izdüşüm'."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(51, 61):
    OM['25']["25:%d" % n] = {"ar": AR[(25, n)], "meal": MEAL[n], "olcum": OLCUM[n],
                             "mercek": MERCEK[n], "dikey": DIK["25:%d" % n]}
OM['25']['_mercek_atlama_notu'].update(ATLAMA)
OM['25']['_makro']['aktor'] = OM['25']['_makro']['aktor'].replace(
    "Adsız: racül *(bir adam)* 25:8 · nefer *(bir bölük)* 25:60.",
    "Adsız: racül *(bir adam)* 25:8. **GERİ ÇEKİLDİ: 'nefer *(bir bölük)* 25:60' kaydı ÖLÇÜM "
    "ARTEFAKTIDIR** — 25:60'ın 13. kelimesi نُفُورا *(nefret, kaçış)*, نفر kökü; aktör dedektörü "
    "kökü 'nefer (bölük)' sanmış (aday 462, okuma blok 25:51-60'ta yakalandı).")
OM['ilerleme']['not'] = ("Sûre 23 TAM (118/118). Sûre 24 TAM (64/64). **Sûre 25 (Furkān) 60/77.** "
                         "Devam: 25:61'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "25": "1-60 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1705
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 25 →', len([k for k in OM['25'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(51, 61):
    MK['25']["25:%d" % n] = MERCEK[n]
MK['25_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 25 →', len(MK['25']))
