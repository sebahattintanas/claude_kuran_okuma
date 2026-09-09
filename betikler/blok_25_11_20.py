# -*- coding: utf-8 -*-
"""blok_25_11_20.py — sûre 25 ikinci blok (25:11-20)."""
import json
DIK = json.load(open('blok_dikey_25_1_20.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
11: "Hayır, onlar o saati yalanladılar. Biz o saati yalanlayana çılgın bir alev hazırladık.",
12: "O, onları uzak bir yerden gördüğünde, onun öfkeli kaynamasını ve uğultusunu işitirler.",
13: "Zincirlerle birbirine bağlanmış olarak oradan dar bir yere atıldıklarında, orada yok oluşu çağırırlar.",
14: "Bugün bir tek yok oluşu çağırmayın; birçok yok oluşu çağırın.",
15: "De ki: Bu mu hayırlı, yoksa sakınanlara vaat edilen ebedîlik bahçesi mi? O, onlar için bir karşılık ve bir varış yeridir.",
16: "Orada, ebedî kalıcılar olarak, diledikleri her şey onlarındır. Bu, Rabbinin üstlendiği, istenmeye değer bir vaattir.",
17: "O gün, onları ve Allah'ın yanı sıra taptıklarını toplar, sonra der ki: Şu kullarımı siz mi saptırdınız, yoksa kendileri mi yoldan saptılar?",
18: "Derler ki: Seni tenzih ederiz; senin yanı sıra veliler edinmek bize yakışmazdı. Ama sen onları da atalarını da öyle nimetlendirdin ki zikri unuttular ve helâke uğramış bir topluluk oldular.",
19: "İşte söylediklerinizde sizi yalanladılar; artık ne azabı çevirebilir ne de yardım bulabilirsiniz. Sizden kim zulmederse, ona büyük bir azap tattırırız.",
20: "Senden önce gönderdiğimiz elçiler de mutlaka yemek yiyor, çarşılarda dolaşıyorlardı. Kiminizi kiminize bir sınama kıldık: sabredecek misiniz? Rabbin görendir.",
}

OLCUM = {
11: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · "
 "**şahıs 1P x2 — SÛRENİN İLK BİRİNCİ ŞAHSI**; 3MP x2 · 3MS x1, iltifât 0 · n=8 mora=49 harf=41 "
 "(n z=-0,47), fâsıla سَعِيرًا *(çılgın alev)* → ا, A sınıfı, ACC; i'râb GEN 2 · ACC 1; bab II x2 · "
 "IV x1; **zaman PERF x3 — üç fiilin üçü de mâzi**; **kök ikilemesi كذب *(yalan; yalanlama)* x2 · "
 "سوع *(saat, vakit)* x2**; **biçim IDRAB — بَلْ *(hayır, bilakis)* ile açılış**; simetri [4,1,5,1]; "
 "dış düğüm 0 · yıldız ★ yok · kökler كذب *(yalan; yalanlama)* · سوع *(saat, vakit)* · عتد "
 "*(hazırlama)* · سعر *(alevlenme, saîr)* · bağ: **25:1-10 ile eksen kırılması** — açılış onlusunda "
 "birinci şahıs SIFIRDI, buradan sonra 30 ayette var (elle, L1, aday 538)"),
12: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — özne dişil ve adsız (سَعِير "
 "*(çılgın alev)* göndergesi) · edim haber, kip işareti yok · şahıs 3MP x3 · 3FS x2, iltifât 0 · "
 "n=9 mora=51 harf=42 (n z=-0,36), fâsıla زَفِيرًۭا *(uğultu, derin soluk)* → ا, A sınıfı, ACC; "
 "i'râb GEN 2 · ACC 2; bab I x2; zaman PERF x2; dış düğüm 0 · yıldız ★ yok · kökler رأي *(görme)* · "
 "كون *(olmak; mekân, yer)* · بعد *(sonra; uzaklık)* · سمع *(işitme)* · غيظ *(öfke, gayz)* · زفر "
 "*(derin soluk, inleme)* · bağ: **زفر *(derin soluk, inleme)* korpusta üç geçişli** — 11:106, "
 "21:100, 25:12; üçü de azap sahnesi"),
13: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3MP x4 · 3FS x1, iltifât 0 · n=9 mora=62 harf=47 (n z=-0,36), fâsıla ثُبُورًۭا *(yok oluş, helâk "
 "çağrısı)* → ا, A sınıfı, ACC; **i'râb ACC 4 — dokuz kelimenin dördü mansûb**; bab I x1 · IV x1; "
 "zaman PERF x2; **edilgen 1 — أُلْقُوا۟ *(atıldıkları)***, **pas z=2,52: yıldızın TEK kaynağı**; "
 "dış düğüm 0 · **yıldız ★★** · kökler لقي *(karşılaşma, kavuşma; atma)* · كون *(olmak; mekân, "
 "yer)* · ضيق *(darlık)* · قرن *(nesil, çağ; birbirine bağlama (mukarren))* · دعو *(çağırma, dua)* · "
 "ثبر *(helâk, sabûr)* · bağ: **ثبر *(helâk, sabûr)* korpusta beş geçişli, üçü 25:13-14'te** "
 "(elle, L1, aday 531)"),
14: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir + yasak, kip PRO 1 · IMPV 1 · "
 "şahıs 2MP x4, **iltifât 1 — yön 3>2, SÛRENİN İLK İLTİFÂTI**: önceki ayet 3MP ile anlatıyordu, "
 "burada doğrudan hitaba geçiliyor · n=8 mora=51 harf=43 (n z=-0,47), fâsıla كَثِيرًۭا *(çok)* → ا, "
 "A sınıfı, ACC; **i'râb ACC 5 — sekiz kelimenin beşi mansûb**; bab I x2; zaman IMPF x1 · IMPV 1; "
 "**kök ikilemesi دعو *(çağırma, dua)* x2 · ثبر *(helâk, sabûr)* x2**; **açık sayı sözcüğü İKİ: "
 "وحد *(bir olma, teklik)* → وَٰحِدًۭا *(bir)* ve كثر *(çokluk)* → كَثِيرًۭا *(çok)***; biçim NEHY; "
 "dış düğüm 0 · yıldız ★ yok · kökler دعو *(çağırma, dua)* · يوم *(gün)* · ثبر *(helâk, sabûr)* · "
 "وحد *(bir olma, teklik)* · كثر *(çokluk)* · bağ: **25:13 ile bitişik çift** — orada anlatı "
 "(3MP, PERF), burada hitap (2MP, IMPV/PRO); aynı iki kök, ters kip (elle, L1, aday 539)"),
15: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — جَنَّة *(cennet, bahçe)* burada "
 "tamlama başı ve aktör tablosuna girmiyor · edim soru + emir, kip IMPV 1 · INTG 1 · şahıs 2MS x1 · "
 "3MS x1 · 3FS x1 · 3MP x1, iltifât 0 · n=13 mora=64 harf=53 (n z=0,06), fâsıla مَصِيرًۭا *(varış "
 "yeri)* → ا, A sınıfı, ACC; i'râb NOM 3 · ACC 2 · GEN 1; bab I x3; zaman IMPV 1 · PERF x2; "
 "**edilgen 1 — وُعِدَ *(vaat edildi)***, **pas z=1,57: yıldızın TEK kaynağı**; **أَمْ *(yoksa)* "
 "ayet İÇİNDE — muttasıla, ve ayet INTG alıyor: aday 438'in KARŞI KONTROLÜ, doğru işleniyor**; "
 "dış düğüm 0 · **yıldız ★** · kökler قول *(söz söyleme)* · خير *(hayır, daha iyi)* · جنن *(örtme, "
 "gizleme; cennet; cin)* · خلد *(ebedî kalma)* · وعد *(vaat)* · وقي *(sakınma, koruma)* · كون "
 "*(olmak; mekân, yer)* · جزي *(karşılık verme)* · صير *(dönüşme, varış)* · bağ: **25:10 ile "
 "karşılaştırma** — orada جَنَّٰت *(bahçeler)* dünyada ve şarta bağlı, burada جَنَّةُ ٱلْخُلْدِ "
 "*(ebedîlik bahçesi)* vaade bağlı (elle, L1, aday 540)"),
16: ("eksen: **lafız YOK · SÛRENİN İLK رَبّ *(Rab)*'Bİ — 8. sırada** (rab z=1,81: **yıldızın TEK "
 "kaynağı**) · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs 3MP x3 · 3FS x1 · 3MS x1 · "
 "2MS x1, iltifât 0 · n=10 mora=61 harf=42 (n z=-0,26), fâsıla مَّسْـُٔولًۭا *(istenmeye değer)* → ا, "
 "A sınıfı, ACC; i'râb ACC 3 · GEN 1; bab I x2; zaman IMPF x1 · PERF x1; dış düğüm 0 · **yıldız ★** · "
 "kökler شيأ *(dileme; şey)* · خلد *(ebedî kalma)* · كون *(olmak; mekân, yer)* · ربب *(rab, terbiye "
 "etme)* · وعد *(vaat)* · سأل *(isteme, dileme)* · bağ: **25:15 ile bitişik çift** — orada وُعِدَ "
 "*(vaat edildi)* edilgen ve vaat edenin adı yok, burada عَلَىٰ رَبِّكَ وَعْدًۭا *(Rabbinin üzerine "
 "bir vaat)*: aynı kök, edilgenden fâil-adlı yapıya (elle, L1, aday 541)"),
17: ("eksen: **SÛRENİN İLK ALLAH LAFZI — 7. sırada** (allah z=0,72) · Rab yok · esmâ yok · aktör yok · "
 "edim soru, kip INTG 1 · **şahıs 3MP x6 · 2MP x3 · 3MS x2 · 1S x1 — sûrenin ilk tekil birinci "
 "şahsı (عِبَادِى *(kullarım)*)**, ölçüm ilt=0 · n=16 mora=85 harf=69 (n z=0,38), **fâsıla "
 "ٱلسَّبِيلَ *(yol)* → ل — SÛRENİN TEK ل FÂSILASI VE TEK KAFİYE KIRILMASI** (kafiye_kirik=1), "
 "yine de ACC; i'râb ACC 2 · GEN 2 · NOM 1; bab I x4 · IV x1; zaman IMPF x3 · PERF x2; **kök "
 "ikilemesi عبد *(kul, kulluk)* x2 · ضلل *(sapma, saptırma)* x2**; **أَمْ *(yoksa)* ayet İÇİNDE — "
 "muttasıla, ayet INTG alıyor: aday 438'in ikinci karşı kontrolü**; biçim DIKKAT; simetri [3,3,12,1]; "
 "dış düğüm 0 · **yıldız ★** · kökler يوم *(gün)* · حشر *(toplama, mahşer)* · عبد *(kul, kulluk)* · "
 "دون *(beriki, başkası)* · أله *(ilâh; lafza-i celâl)* · قول *(söz söyleme)* · ضلل *(sapma, "
 "saptırma)* · سبل *(yol)* · bağ: **25:9 ile ortak سبل *(yol)* ve ضلل *(sapma, saptırma)*** — orada "
 "sapanlar yol bulamıyor, burada sapmanın failini soru belirliyor (elle, L1, aday 542)"),
18: ("eksen: **lafız YOK · Rab YOK** · **esmâ وَلِيّ *(velî)* 12. sırada — ÖLÇÜM ARTEFAKTI (aday "
 "461)**: lemma çoğul (أَوْلِيَآء *(veliler)*) ve gönderge edinilen varlıklar; ölçüt (b) dışlıyor. "
 "MÜHÜRSÜZ — aday 501'in 'mühürsüz konumlar kirli' ölçümüyle uyumlu · aktör yok · edim haber, kip "
 "NEG 1 · şahıs 3MP x8 · 2MS x4 · 3MS x2 · 1P x2, iltifât 0 · n=21 mora=116 harf=93 — **bloğun en "
 "uzun ayeti** (n z=0,91), fâsıla بُورًۭا *(helâke uğramış)* → ا, A sınıfı, ACC; i'râb ACC 5 · "
 "GEN 2; bab I x4 · II x1 · VII x1 · VIII x1; zaman PERF x5 · IMPF x2; **kök ikilemesi كون *(olmak; "
 "mekân, yer)* x2**; simetri [3,7,11,1]; **dış düğüm 2** · yıldız ★ yok · kökler قول *(söz "
 "söyleme)* · سبح *(tesbih, tenzih)* · كون *(olmak; mekân, yer)* · بغي *(iffetsizlik; azgınlık; "
 "yakışma, uygun olma (inbiğâ))* · أخذ *(alma, edinme)* · دون *(beriki, başkası)* · ولي *(dost, "
 "veli; velâyet)* · متع *(faydalanma, geçimlik)* · أبو *(baba)* · نسي *(unutma)* · ذكر *(anma, "
 "zikir)* · قوم *(kalkma; kavim; kıyamet)* · بور *(helâk, boşa gitme)* · bağ: xref قال *(dedi)* + "
 "سبحان *(tenzih)* + كان *(oldu)* → **5:116**; كان *(oldu)* + قوم *(kavim)* + بور *(helâk)* → "
 "**48:12**; **25:3 ile halka** — orada إِلٰهة *(ilâhlar)* مِن دُونِهِ *(onun yanı sıra)* "
 "EDİNİLİYOR, burada aynı terkiple (مِن دُونِكَ *(senin yanı sıra)*) edinme REDDEDİLİYOR "
 "(elle, L1, aday 543)"),
19: ("eksen: **lafız YOK · Rab YOK** · **esmâ كَبِير *(büyük)* 15. sırada = fâsıla — ÖLÇÜM ARTEFAKTI "
 "(aday 461)**: nekre ve gönderge عَذَاب *(azap)*, yani sıfat azabın; ölçüt (b) dışlıyor. MÜHÜRSÜZ · "
 "aktör yok · edim haber, kip CERT 1 · NEG 2 · **şahıs 2MP x6 · 3MP x2 · 3MS x2 · 1P x1 — hitap "
 "sürüyor**, iltifât 0 · n=15 mora=85 harf=70 (n z=0,27), fâsıla كَبِيرًۭا *(büyük)* → ا, A sınıfı, "
 "ACC; **i'râb ACC 4 — ve dördü de tek başına mansûb isim**; bab I x2 · II x1 · IV x1 · X x1; zaman "
 "IMPF x4 · PERF x1; simetri [3,1,8,1]; dış düğüm 1 · yıldız ★ yok · kökler كذب *(yalan; "
 "yalanlama)* · قول *(söz söyleme)* · طوع *(güç yetirme, itaat)* · صرف *(çevirme, türlü türlü "
 "açıklama)* · نصر *(yardım)* · ظلم *(zulüm)* · ذوق *(tatma)* · عذب *(azap)* · كبر *(büyüklük; "
 "büyüklenme)* · bağ: xref ظلم *(zulüm)* + أذاق *(tattırdı)* + عذاب *(azap)* → **22:25**; **25:11 "
 "ile ortak كذب *(yalan; yalanlama)*** — orada saati yalanlıyorlar, burada yalanlanan onlar oluyor: "
 "aynı kök, fâil ve mef'ûl yer değiştiriyor (elle, L1, aday 544)"),
20: ("eksen: **lafız YOK · رَبّ *(Rab)* 19. sırada — sûrenin ikinci Rab'bi** (rab z=0,74) · **esmâ "
 "بَصِير *(gören)* 20. sırada = fâsıla — GEÇERLİ**: doğrudan رَبّ *(Rab)*'bin yüklemi (كَانَ رَبُّكَ "
 "بَصِيرًۭا *(Rabbin görendir)*). MÜHÜRSÜZ · aktör yok · edim soru, kip NEG 1 · RES 1 · EMPH 1 · "
 "INTG 1 · **şahıs 3MP x5 · 1P x4 · 2MP x3 · 2MS x2 · 3MS x1**, iltifât 0 · n=20 mora=120 harf=100 "
 "(n z=0,81), fâsıla بَصِيرًۭا *(gören)* → ا, A sınıfı, ACC; **i'râb ACC 6 · GEN 3 · NOM 1**; bab "
 "I x5 · IV x1; zaman PERF x3 · IMPF x3; **kök ikilemesi رسل *(gönderme, elçi)* x2 · بعض *(bir "
 "kısım)* x2**; **biçim HASR**; dış düğüm 0 · yıldız ★ yok · kökler رسل *(gönderme, elçi)* · قبل "
 "*(ön, önce; kabul)* · أكل *(yeme)* · طعم *(yiyecek, yemek verme)* · مشي *(yürüme)* · سوق *(sürme, "
 "sevk etme; çarşı (sûk))* · جعل *(kılma, var etme)* · بعض *(bir kısım)* · فتن *(sınama, fitne)* · "
 "صبر *(sabır)* · كون *(olmak; mekân, yer)* · ربب *(rab, terbiye etme)* · بصر *(görme)* · bağ: "
 "**25:7 ile BÖLÜT İKİZİ KAPANDI — ön-kayıt DOĞRULANDI** (aday 535): dört farklılaşan öğenin dördü "
 "de ölçüldü"),
}

MERCEK = {
11: ("Blok bir tekzip fiiliyle açılıyor ve fiil aynı ayette iki kez, iki farklı özneyle: "
 "كَذَّبُوا۟ *(yalanladılar)* çoğul ve belirli, كَذَّبَ *(yalanlayan)* tekil ve şartlı. Ölçülebilir "
 "bir daralma: topluluktan tek kişiye. Aynı yapı ikinci kökte de var — ٱلسَّاعَةِ *(o saat)* iki kez "
 "ve ikisi de marife, yani nesne sabit kalırken özne değişiyor. Ve ayet sûrenin ilk birinci şahsını "
 "getiriyor: أَعْتَدْنَا *(hazırladık)*, عتد *(hazırlama)* kökü. عتد korpusta 16 geçişli ve dikey "
 "ölçümü ▸sonra alev x85,3 veriyor — hazırlama fiili korpusta zaten bu nesneye bağlı, bu ayete "
 "özgü değil."),
12: ("Ayet öznesi dişil bir varlığa üç eylem yüklüyor ve üçü de duyusal: görme, kaynama, uğultu. "
 "Ölçülebilir bir yön: رَأَتْهُم *(onları gördü)* — gören ateş, görülen insanlar; sonraki fiilde "
 "yön tersine dönüyor, سَمِعُوا۟ *(işittiler)* — işiten insanlar. İki duyu iki yönde. Mesafe açıkça "
 "veriliyor ve nicel değil nitel: مَكَانٍۭ بَعِيدٍۢ *(uzak bir yer)*, ikisi de nekre. زفر *(derin "
 "soluk, inleme)* korpusta yalnız üç geçişli (11:106, 21:100, 25:12) ve dikey ölçüm bu kök için "
 "eşiği aşan hiçbir komşu vermiyor — kökün korpusta bir kavram yatağı yok, üç geçişi de tek sahne "
 "türünde."),
13: ("Yıldızın tek kaynağı tek bir edilgen fiil: أُلْقُوا۟ *(atıldılar)*, لقي *(karşılaşma, "
 "kavuşma; atma)* kökü. Ölçülebilir bir daralma dizisi: مَكَانٍۭ بَعِيدٍۢ *(uzak bir yer)* 25:12'de, "
 "burada مَكَانًۭا ضَيِّقًۭا *(dar bir yer)* — aynı kelime (كون *(olmak; mekân, yer)* kökünden "
 "مَكَان) iki ayette, sıfat uzaklıktan darlığa geçiyor. Bağlanma hâl olarak veriliyor: مُقَرَّنِينَ "
 "*(birbirine bağlanmış)*, قرن *(nesil, çağ; birbirine bağlama (mukarren))* bab II ism-i mef'ûl. "
 "Ve tek fiil bir çağrı: يَدْعُونَ değil دَعَوْا۟ *(çağırdılar)*, nesnesi ثُبُورًۭا *(yok oluş)* — "
 "korpusta beş geçişli bir kökün üç geçişi bu ayet ve sonrakinde."),
14: ("Ayet bir sayı karşıtlığı kuruyor ve karşıtlığın iki ucu da açık sayı sözcüğü: وَٰحِدًۭا *(bir)* "
 "ve كَثِيرًۭا *(çok)*. Ölçülebilir bir yasak-emir çifti: aynı fiil (دعو *(çağırma, dua)*) önce "
 "yasaklanıyor (لَّا تَدْعُوا۟), sonra emrediliyor (وَٱدْعُوا۟) — nesne de aynı (ثُبُورًۭا *(yok "
 "oluş)*), değişen yalnız sayı sıfatı. Sekiz kelimelik ayette beş mansûb isim var. Ve sûrenin ilk "
 "iltifâtı burada: önceki ayet üçüncü şahısla anlatıyordu, bu ayet doğrudan hitap. Yön 3>2."),
15: ("Soru iki seçenek arasında kuruluyor ve seçenekler aynı sözdizimsel ağırlıkta değil: ilki "
 "işaret zamiri (ذَٰلِكَ *(bu)*), ikincisi üç kelimelik marife tamlama (جَنَّةُ ٱلْخُلْدِ ٱلَّتِى "
 "*(ebedîlik bahçesi ki)*). Ölçülebilir bir asimetri — sorunun iki tarafı eşit uzunlukta değil. "
 "Vaat edilme edilgen veriliyor: وُعِدَ ٱلْمُتَّقُونَ *(sakınanlara vaat edildi)*, fâil "
 "adlandırılmıyor; bir sonraki ayet bunu tamamlayacak. Kapanış iki terimli: جَزَآءًۭ *(karşılık)* "
 "ve مَصِيرًۭا *(varış yeri)* — biri değer, öteki yer; dikey ölçüm صير *(dönüşme, varış)* ▸önce "
 "ne-kötü x69,5 veriyor, yani kök korpusta ağırlıkla olumsuz kutupta ve burada olumlu kutupta "
 "kullanılıyor."),
16: ("Sûrenin ilk رَبّ *(Rab)*'bi burada ve yıldızın tek kaynağı bu: on kelimelik ayette tek Rab "
 "geçişi rab z=1,81 üretiyor. Ölçülebilir bir tamamlama: 25:15 وُعِدَ *(vaat edildi)* edilgeniyle "
 "fâili gizlemişti, bu ayet aynı kökü (وعد *(vaat)*) isim yapıp fâili adlandırıyor — عَلَىٰ رَبِّكَ "
 "وَعْدًۭا *(Rabbinin üzerine bir vaat)*. Vaadin sıfatı bir edilgen ism-i mef'ûl: مَّسْـُٔولًۭا "
 "*(istenmeye değer, istenen)*, سأل *(isteme, dileme)* kökünden. Ve kapsam sınırsız veriliyor ama "
 "tek kelimeyle: مَا يَشَآءُونَ *(diledikleri)* — dileyen artık onlar, oysa 25:10'da dileyen "
 "başkasıydı (إِن شَآءَ *(dilerse)*), aynı kök iki özneyle."),
17: ("Sûrenin ilk Allah lafzı ve tek kafiye kırılması aynı ayette. Fâsıla ٱلسَّبِيلَ *(yol)* marife "
 "ve ل ile bitiyor — sûrenin öteki yetmiş altı fâsılası ا ile. Yine de i'râbı ACC, yani kırılma "
 "harf düzeyinde, i'râb düzeyinde değil. Ölçülebilir bir simetri: عبد *(kul, kulluk)* kökü iki kez "
 "ve iki yönde — يَعْبُدُونَ *(taptıkları)* fiil, عِبَادِى *(kullarım)* isim ve iyelikli; aynı "
 "kökün bir ayette hem sahte tapınmayı hem gerçek aidiyeti taşıması. ضلل *(sapma, saptırma)* de "
 "iki kez ve iki çatıda: أَضْلَلْتُمْ *(saptırdınız)* geçişli, ضَلُّوا۟ *(saptılar)* geçişsiz — "
 "sorunun tamamı bu çatı farkı üzerine kurulu."),
18: ("Cevap bir tenzih formülüyle açılıyor ve hemen bir yakışmazlık ifadesiyle sürüyor: "
 "مَا كَانَ يَنۢبَغِى لَنَآ *(bize yakışmazdı)*, بغي *(iffetsizlik; azgınlık; yakışma, uygun olma "
 "(inbiğâ))* kökü bab VII — sûrede bu babın tek geçişi. Ölçülebilir bir terkip halkası: 25:3'te "
 "وَٱتَّخَذُوا۟ مِن دُونِهِۦٓ ءَالِهَةًۭ *(onun yanı sıra ilâhlar edindiler)*, burada aynı iki "
 "öğeyle (أخذ *(alma, edinme)* + دون *(beriki, başkası)*) ama olumsuz ve muhatap değişmiş: "
 "مِن دُونِكَ *(senin yanı sıra)*. Sorumluluk sonra nimete bağlanıyor: مَتَّعْتَهُمْ *(onları "
 "nimetlendirdin)*, متع *(faydalanma, geçimlik)* bab II, ve sonucu tek fiil: نَسُوا۟ ٱلذِّكْرَ "
 "*(zikri unuttular)*. بور *(helâk, boşa gitme)* korpusta beş geçişli ve dikey ölçümü ▸önce "
 "kavim x6,6 veriyor — قَوْمًۢا بُورًۭا *(helâke uğramış topluluk)* bir kalıp."),
19: ("Ayet muhatabı iki kez değiştiriyor ve ikisi de aynı yönde: önce 2MP (كَذَّبُوكُم *(sizi "
 "yalanladılar)*), sonra şartla tekile iniyor (وَمَن يَظْلِم مِّنكُمْ *(sizden kim zulmederse)*). "
 "Ölçülebilir bir iade: 25:11'de tekzibin öznesi onlardı ve nesnesi o saatti; burada tekzibin "
 "nesnesi onlar oluyor — aynı kök (كذب *(yalan; yalanlama)*), fâil ve mef'ûl yer değiştirmiş. İki "
 "yetersizlik yan yana ve ikisi de nekre mansûb: صَرْفًۭا *(çevirme)* ve نَصْرًۭا *(yardım)*; صرف "
 "*(çevirme, türlü türlü açıklama)* korpusta 30 geçişli ve dikey ölçümü ▸sonra Kur'ân x17,6 "
 "veriyor — kök korpusta ağırlıkla 'âyetleri türlü türlü açıklama' bağlamında, burada 'azabı "
 "çevirme' bağlamında; kök düzeyi komşuluk bu ayrımı yapmıyor (aday 529 sınıfı)."),
20: ("Bloğun kapanışı bloğun on üç ayet öncesindeki itirazı cevaplıyor ve cevap itirazın kendi "
 "cümlesini kullanıyor: يَأْكُلُونَ ٱلطَّعَامَ وَيَمْشُونَ فِى ٱلْأَسْوَاقِ *(yemek yiyorlar, "
 "çarşılarda dolaşıyorlar)*. Ölçülen dört fark: şahıs tekilden çoğula, te'kid yoktan لَ'ya, biçim "
 "INTG'den HASR'a, kapsam bir elçiden ٱلْمُرْسَلِينَ *(gönderilen elçiler)*'e. Ardından ayet ikinci "
 "bir şey yapıyor: itirazın kendisini bir sınama olarak yeniden adlandırıyor — فِتْنَةً *(sınama)*, "
 "فتن *(sınama, fitne)* kökü, ve nesnesi karşılıklı: بَعْضَكُمْ لِبَعْضٍۢ *(kiminizi kiminize)*, "
 "بعض *(bir kısım)* iki kez. Soru cümlesi tek kelime: أَتَصْبِرُونَ *(sabredecek misiniz)*. Ve "
 "kapanış sûrenin ikinci Rab'bini bir görme yüklemiyle veriyor."),
}

ATLAMA = {
 "_blok_notu_25_11_20": ("Blokta ★★★ AYET YOK — en yüksek 25:13'te ★★ ve tek kaynağı tek bir "
  "edilgen fiil (pas z=2,52). Protokol gereği 🜁 biyolog ve 🜂 uzay mercekleri YAZILMADI: eşik ★★★. "
  "Bilgi olarak: blokta çıpa taşıyabilecek tek öğe 25:12'nin غَيْظ *(öfke, gayz)* ve زَفِير "
  "*(uğultu, derin soluk)* terkibidir — solunum ya da ses fiziği okuması YASAKLI 'bilimsel "
  "izdüşüm' olurdu; ayet ne organ ne mekanizma ne ölçü veriyor, gönderge bir azap sahnesi ve "
  "özne ateş. Çıpa sayılmadı. SÛRE 25 ARA BİLANÇO (20/77 ayet): ★★★ sıfır, ★★ bir, ★ dört; "
  "çıpa sıfır. Adaylar 468/512 için: ilk yirmi ayette yıldız ile çıpa AYNI YÖNDE."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(11, 21):
    OM['25']["25:%d" % n] = {"ar": AR[(25, n)], "meal": MEAL[n], "olcum": OLCUM[n],
                             "mercek": MERCEK[n], "dikey": DIK["25:%d" % n]}
OM['25']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 23 TAM (118/118). Sûre 24 TAM (64/64). **Sûre 25 (Furkān) 20/77.** "
                         "Devam: 25:21'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "25": "1-20 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1665
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 25 →', len([k for k in OM['25'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(11, 21):
    MK['25']["25:%d" % n] = MERCEK[n]
MK['25_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 25 →', len(MK['25']))
