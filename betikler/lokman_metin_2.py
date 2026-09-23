# -*- coding: utf-8 -*-
"""lokman_metin_2.py — sûre 31 (Lokmân) meal ve matematikçi merceği, ayet 21-34."""
MEAL = {
 21: "Onlara 'Allah'ın indirdiğine uyun' dendiğinde, 'Hayır, biz atalarımızı üzerinde bulduğumuz şeye uyarız' derler. Şeytan onları alevli ateşin azabına çağırıyor olsa da mı?",
 22: "Kim iyilik yaparak yüzünü Allah'a teslim ederse, sağlam kulpa tutunmuş olur. İşlerin sonu Allah'a varır.",
 23: "Kim inkâr ederse, onun inkârı seni üzmesin. Dönüşleri bizedir; yaptıklarını onlara haber veririz. Şüphesiz Allah göğüslerin özünü bilendir.",
 24: "Onları biraz faydalandırır, sonra ağır bir azaba sürükleriz.",
 25: "Andolsun, onlara 'Gökleri ve yeri kim yarattı?' diye sorsan mutlaka 'Allah' derler. De ki: Hamd Allah'a mahsustur. Hayır, onların çoğu bilmez.",
 26: "Göklerde ve yerde ne varsa Allah'ındır. Şüphesiz Allah ganîdir, hamîddir.",
 27: "Eğer yeryüzündeki ağaçlar kalem olsa, deniz de ardından yedi deniz daha katılarak mürekkep olsa, Allah'ın kelimeleri tükenmezdi. Şüphesiz Allah azîzdir, hakîmdir.",
 28: "Sizin yaratılmanız da diriltilmeniz de tek bir kişininki gibidir. Şüphesiz Allah işitendir, görendir.",
 29: "Görmedin mi, Allah geceyi gündüze, gündüzü geceye katıyor; güneşi ve ayı boyun eğdirmiş, her biri belirli bir süreye kadar akıp gidiyor. Ve Allah yaptıklarınızdan haberdardır.",
 30: "Bu böyledir; çünkü Allah hakkın ta kendisidir, O'ndan başka çağırdıkları ise bâtıldır. Şüphesiz Allah yücedir, büyüktür.",
}
M = {
 21: "◇ Şeytan sûrede ilk kez adlı aktör (gayb, fail). 'Atalarımızı üzerinde bulduk' kalıbı xref 2:170, 5:104, 10:78 ile bağlı; blok 31:20'deki 'bilgisizce tartışma' ile aynı hattın devamı. Edilgen 1/8 fiil.",
 22: "◇ İki yeni kök burada: عرو ve وثق — 'sağlam kulp' (xref 2:256). حسن kökü [2/2]: 31:3'teki 'muhsinler' sûrede burada kapanıyor. ★★'nın tek kaynağı allah z=2,14 (15 kelimede 2 lafız) → payda etkisi, içerik değil.",
 23: "◇ Esmâ عَلِيم MÜHÜRSÜZ, ama yanlış pozitif DEĞİL: gerçek ilâhî ad, yalnız ayetin son kelimesi değil (13/15) ve çift oluşturmuyor. Mühür ölçütü ayet sonu ÇİFT arıyor. Blok 1-2'deki mühürsüzler ilâhî olmayan sıfatlardı; buradaki ayrım tersine.",
 24: "◇ 'Biraz faydalandırma → ağır azap' kalıbı xref 2:126. Yeni kök غلظ. Sayı işareti قَلِيل.",
 25: "◇ ★★ kaynağı yalnız allah z=2,14. Soru-cevap kalıbı ('kim yarattı?' → 'Allah') xref 29:63. خلق [4/5].",
 26: "◇ ★★★'ın tek kaynağı allah z=3,47: on kelimelik ayette iki lafız. Bu, bloktaki üçüncü yoğunluk yıldızı; hiçbiri içerikten gelmiyor. Ayrıca kafiye kırığı (د, iki ر arasında) var ama formül eklemedi (başka bileşen 1,5'in üstünde). esit2 → 22:64 BENZER (0,92).",
 27: "◇ TARAYICI v4 adayı (A_şart): ağaç-kalem ve deniz-mürekkep bir benzetme; olgular örnek olarak kullanılıyor, iddia Allah'ın kelimelerinin tükenmezliği → L1 · olgu HAYIR → yanlış pozitif. Yeni kök قلم; sayı işareti سَبْعَة.",
 28: "◇ Sûredeki ilk iltifât (ilt 1). Yaratma ile diriltme tek bir nefse eşitleniyor; خلق [5/5] sûrede son kez. Bağ yok (esit2, nakarat3, xref üçü de boş).",
 29: "◇ TARAYICI v4 adayı (G_bakış): gece-gündüz iç içe geçişi, güneş ve ayın boyun eğdirilmesi, 'belirli bir süreye kadar akış'. Süreç tarifi var, ama açık nedensellik ve ölçü birimi yok → L1'de bırakıldı, çıpa değil. Kademe kararı okumaya bağlı → KAPATILAMAZ. nakarat3 'أَلَمْ تَرَ أَنَّ ٱللَّهَ' GEÇİYOR: 31:20 ile aynı kalıp.",
 30: "◇ esit2 → 22:62 YAKIN (0,98): neredeyse aynı ayet. ★ kaynağı allah z=1,97. Mühür عَلِيّ + كَبِير geçerli.",
}

MEAL.update({
 31: "Görmedin mi, gemiler Allah'ın nimetiyle denizde akıp gidiyor; size âyetlerinden göstermek için. Şüphesiz bunda çok sabreden, çok şükreden herkes için işaretler vardır.",
 32: "Onları dağlar gibi bir dalga bürüdüğünde, dini yalnız O'na has kılarak Allah'a yalvarırlar. Onları karaya çıkarıp kurtardığında ise içlerinden bir kısmı orta yolu tutar. Âyetlerimizi, gaddar ve nankör olandan başkası bile bile inkâr etmez.",
 33: "Ey insanlar, Rabbinizden sakının ve babanın çocuğuna, çocuğun da babasına hiçbir şeyle fayda veremeyeceği bir günden korkun. Şüphesiz Allah'ın vaadi gerçektir. Dünya hayatı sizi aldatmasın; o aldatıcı da sizi Allah ile aldatmasın.",
 34: "Kıyamet saatinin bilgisi şüphesiz Allah katındadır. Yağmuru O indirir, rahimlerde olanı O bilir. Hiç kimse yarın ne kazanacağını bilmez; hiç kimse hangi yerde öleceğini bilmez. Şüphesiz Allah bilendir, haberdardır.",
})
M.update({
 31: "◇ TARAYICI v4 adayı (B_ta'lîl + G_bakış) ve sûrede tarayıcının bir olgu ayetine ilk isabeti. Kademe: olgu EVET (deniz, gemilerin akışı), ama iki olgu arasında sebep-sonuç yok ve yeti sınırı konmuyor; akışın sebebi olarak 'Allah\'ın nimeti' veriliyor → L1 → çıpa DEĞİL, yanlış pozitif. Karşı okuma (bi-ni\'metillâh bir nedensellik sayılırsa L2) savunulabilir → KAPATILAMAZ. Esmâ شَكُور burada insanın sıfatı ('çok şükreden') → yanlış pozitif. nakarat3 'أَلَمْ تَرَ أَنَّ' GEÇİYOR: 31:20 ve 31:29'dan sonra üçüncü.",
 32: "◇ ★★★'ın tek kaynağı hapaks ختر (hapaks z=3,28): sûredeki İKİNCİ otomatik hapaks ★★★ (borç #7), yine içerikten değil. Esmâ بَرّ aslında 'kara' (karaya çıkarma) → yanlış pozitif, üstelik ORTA konumda. Dalga sahnesinde olgu var ama sınıflama insanlara ait → L1, çıpa değil. xref 29:65: aynı deniz-dua-kurtuluş sahnesi.",
 33: "◇ Sûrenin ikinci ve son Rab'ı; A/R paydası burada kapanıyor. أنس [5/5] son kez. 'Ey insanlar' hitabı: insan üçlüsü turunda nâs'ın 20 hitap tokeninden biri. xref 4:1 ve 22:1 (aynı açılış), 35:5 (aldanma cümlesi neredeyse birebir). ★ kaynağı n z=1,87.",
 34: "◇ 🜁 ÇIPA adayı: L2 (bilgi sınırı) · olgu EVET — yağmurun indirilmesi ve rahimlerdekinin bilinmesi, ardından 'hiçbir nefis bilmez' ile iki kez sınır konuyor. TARTIŞMALI: ölçütteki 'yeti sınırı' fiil yetisi için yazılmıştı, burada sınır bilgiye konuyor → KAPATILAMAZ. TARAYICI vermedi. Esmâ عَلِيم + خَبِير SON konumda MÜHÜR: sûre mühürle kapanıyor. Yeni kök غيث. علم ×3, نفس ×2. ★ kaynağı n z=1,55.",
})
