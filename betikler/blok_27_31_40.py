# -*- coding: utf-8 -*-
"""blok_27_31_40.py — sûre 27 dördüncü blok (27:31-40). Mektup, istişare, hediye, taht."""
import json
DIK = json.load(open('blok_dikey_27_31_40.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
31: "Bana karşı büyüklenmeyin, teslim olmuş olarak bana gelin.",
32: "Dedi: Ey ileri gelenler, işim hakkında bana görüş bildirin; siz yanımda bulunmadıkça ben hiçbir işi kesip atmam.",
33: "Dediler: Biz güç sahibiyiz ve çetin savaş gücü sahibiyiz; buyruk senin, ne buyuracağına bak.",
34: "Dedi: Krallar bir ülkeye girdiklerinde orayı bozguna uğratır, halkının ileri gelenlerini hor kılarlar; işte böyle yaparlar.",
35: "Ben onlara bir hediye göndereceğim ve elçilerin ne ile döneceğine bakacağım.",
36: "Süleymân'a geldiklerinde dedi: Bana mal ile mi yardım ediyorsunuz? Allah'ın bana verdiği, size verdiğinden hayırlıdır. Asıl siz hediyenizle sevinirsiniz.",
37: "Onlara dön; karşı koyamayacakları ordularla üzerlerine geleceğiz ve onları hor ve küçük düşmüş olarak oradan çıkaracağız.",
38: "Dedi: Ey ileri gelenler, onlar bana teslim olmuş olarak gelmeden önce hanginiz onun tahtını bana getirir?",
39: "Cinlerden bir ifrît dedi: Sen makamından kalkmadan onu sana getiririm; ben buna güç yetiririm, güvenilirim.",
40: "Kitaptan bir ilim bulunan kişi dedi: Ben onu, gözünü açıp kapamadan sana getiririm. Onu yanında yerleşmiş görünce dedi: Bu, Rabbimin lütfundandır; şükür mü edeceğim yoksa nankörlük mü edeceğim diye beni sınamak için. Şükreden ancak kendisi için şükretmiş olur; nankörlük edene gelince, Rabbim ganîdir, kerîmdir.",
}

O = {
31: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir + yasak, kip PRO 1 · IMPV 1 "
 "· şahıs 2MP x4 · 1S x2, iltifât **1 — yön 3>12; sûrenin ikinci iltifâtı** (birincisi 27:6) · "
 "**n=5 — sûrenin okunan en kısa ayeti** (n z=-0,79), fâsıla مُسْلِمِينَ *(teslim olmuşlar)* → ن, "
 "N sınıfı; **i'râb ACC 1**; bab I x2; zaman IMPF 1 · IMPV 1; **biçim NEHY**; dış düğüm 0 · yıldız "
 "★ yok · kökler علو *(yücelik; böbürlenme)* · أتي *(gelme, getirme)* · سلم *(esenlik; teslim "
 "olma)* · bağ: **iltifât mektubun İÇİNDE gerçekleşiyor** — 27:30 üçüncü şahısla açılıyor "
 "(إِنَّهُۥ مِن سُلَيْمَٰنَ *(o Süleymân'dandır)*), burada birinci-ikinci şahsa geçiyor; **sûrede "
 "ilk kez iltifât bir alıntı metnin sınırında** (elle, L1, aday 811)"),
32: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — kraliçe adsız aktör tablosuna da "
 "GİRMİYOR · edim emir + nida, kip VOC 1 · IMPV 1 · NEG 1 · şahıs 3FS x1 · 2MP x4 · **1S x5**, "
 "iltifât 0 · n=12 mora=69 harf=51 (n z=-0,04), fâsıla تَشْهَدُونِ *(yanımda bulunursunuz)* → ن, N "
 "sınıfı; **i'râb ACC 3 · NOM 1 · GEN 1**; bab I x3 · IV x1; zaman PERF x2 · IMPV 1 · IMPF 1; "
 "**kök ikilemesi أمر *(emir; iş)* x2**; simetri [3,6,10,1]; **biçim DIKKAT**; dış düğüm 2 · iç "
 "düğüm 2 · yıldız ★ yok · kökler قول *(söz söyleme)* · أيي *(âyet, işaret)* · ملأ *(ileri "
 "gelenler (meleʼ); doldurma)* · فتي *(genç, delikanlı; fetva)* · أمر *(emir; iş)* · كون *(olmak; "
 "mekân, yer)* · قطع *(kesme)* · شهد *(şahitlik)* · bağ: xref أيّ *(ey)* + ملأ *(ileri gelenler)* "
 "+ يفتي *(görüş bildirir)* → **12:43**; قال *(dedi)* + أيّ *(ey)* + ملأ *(ileri gelenler)* → **27:29 · 27:38 · 28:38** "
 "(elle, L1)"),
33: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru + emir, kip IMPV 1 · INTG 1 "
 "· şahıs 3MP x2 · 1P x1 · **2FS x4 — korpusta 2FS taşıyan 30 ayetten biri ve en yüksek dördüncü "
 "değer** · sahset ['1','2','3'], iltifât 0 · n=12 mora=64 harf=63 (n z=-0,04), fâsıla "
 "تَأْمُرِينَ *(buyurursun)* → ن, N sınıfı; **i'râb NOM 3 · GEN 3**; **bab I x3**; zaman PERF 1 · "
 "IMPV 1 · IMPF 1; **kök ikilemesi أمر *(emir; iş)* x2 — 27:32'den devam, iki ardışık ayette aynı "
 "kök iki kez**; simetri [3,3,9,1]; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · قوي "
 "*(kuvvet)* · بأس *(şiddet, azap; savaş gücü)* · شدد *(şiddet, katılık)* · أمر *(emir; iş)* · نظر "
 "*(bakma; mühlet verme)* · bağ: **نظر *(bakma; mühlet verme)* sûrede dördüncü geçiş** — 27:27 "
 "Süleymân, 27:28 hüdhüd, 27:35 kraliçe, burada kraliçeye emir; **dört geçişin dördü de 'sonucu "
 "bekleme' bağlamında** (elle, L1, aday 813)"),
34: ("eksen: **lafız YOK · Rab YOK** · **esmâ İKİ TOKEN, İKİSİ DE ARTEFAKT: مَلِك *(melik)* 3. "
 "sırada — gönderge ٱلْمُلُوك *(krallar)*, ÇOĞUL İNSAN; عَزِيز *(azîz)* 9. sırada — gönderge "
 "أَعِزَّة *(ileri gelenler)*, ÇOĞUL İNSAN; ikisi de ORTA konum, MÜHÜRSÜZ** · aktör yok · edim "
 "haber · **şahıs 3FS x3 · 3MP x8, sahset ['3'] — blokta tek şahıslı tek ayet**, iltifât 0 · n=13 "
 "mora=80 harf=65 (n z=0,06), fâsıla يَفْعَلُونَ *(yaparlar)* → ن, N sınıfı; **i'râb ACC 5 · GEN "
 "1**; bab I x4 · IV x1; zaman PERF x4 · IMPF 1; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz "
 "söyleme)* · ملك *(mülk; melik)* · دخل *(girme)* · قري *(şehir, kasaba (karye))* · فسد "
 "*(bozgunculuk, fesat)* · جعل *(kılma, var etme)* · عزز *(izzet, güç ve üstünlük)* · أهل *(halk, "
 "aile)* · ذلل *(zillet, alçalma)* · فعل *(yapma, işleme)* · bağ: **عزز *(izzet, güç ve üstünlük)* ile ذلل *(zillet, alçalma)* aynı ayette karşıt "
 "çift** — أَعِزَّةَ أَهْلِهَآ أَذِلَّةً *(halkının ileri gelenlerini hor kılarlar)*; 27:37'de "
 "أَذِلَّة yeniden geçecek (elle, L1, aday 812)"),
35: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · şahıs 1S x1 · "
 "3MP x1 · 3MS x1, iltifât 0 · n=8 mora=48 harf=41 (n z=-0,47), fâsıla ٱلْمُرْسَلُونَ *(elçiler)* "
 "→ ن, N sınıfı; **i'râb ACC 1 · NOM 3 · GEN 1**; bab I x1; zaman IMPF 1; **kök ikilemesi رسل "
 "*(gönderme, elçi)* x2 — biri ism-i fâil (مُرْسِلَة *(gönderen)*), biri ism-i mef'ûl "
 "(ٱلْمُرْسَلُونَ *(gönderilenler)*); aynı kök, aynı ayette etken ve edilgen kalıp**; dış düğüm 0 "
 "· yıldız ★ yok · kökler رسل *(gönderme, elçi)* · هدي *(yol gösterme)* · نظر *(bakma; mühlet "
 "verme)* · رجع *(dönme, geri döndürme)* · bağ: **هدي *(yol gösterme)* kökü burada هَدِيَّة "
 "*(hediye)* anlamında — sûrede daha önce 27:24'te ٱهْتَدَى *(yol buldu)* anlamındaydı; AYNI KÖK, "
 "İKİ AYRI ANLAM ALANI, 529 kümesine sûre içi vaka** (elle, L1, aday 814)"),
36: ("eksen: **ALLAH LAFZI 9. sırada — sûrenin YEDİNCİ lafzı** (allah z=0,72) · Rab yok · esmâ yok "
 "· **aktör: adlı سُلَيْمان *(Süleymân)* 3. sırada, tür kişi, rol mecrur** · edim soru, kip INTG 1 "
 "· **şahıs 2MP x7** · 3MS x4 · 1S x2, iltifât 0 · **n=16 — blokta ikinci en uzun ayet** (n "
 "z=0,38), fâsıla تَفْرَحُونَ *(seviniyorsunuz)* → ن, N sınıfı; **i'râb GEN 3 · NOM 2**; bab I x3 "
 "· IV x3; zaman PERF x4 · IMPF x2; **kök ikilemesi أتي *(gelme, getirme)* x2 — ءَاتَىٰنِۦَ "
 "*(bana verdi)* ve ءَاتَىٰكُم *(size verdi)*, aynı fiil iki muhatapla**; simetri [3,1,11,1]; "
 "**biçim IDRAB**; dış düğüm 1 · yıldız ★ yok · kökler جيأ *(gelme)* · قول *(söz söyleme)* · مدد "
 "*(uzatma, destekleme)* · مول *(mal)* · أتي *(gelme, getirme)* · أله *(ilâh; lafza-i celâl)* · "
 "خير *(hayır, daha iyi)* · هدي *(yol gösterme)* · فرح *(sevinç, şımarma)* · bağ: xref آتى "
 "*(verdi)* + اللّه *(Allah)* + خير *(hayır)* → **11:31** (elle, L1)"),
37: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir, **kip IMPV 1 · EMPH 4** · "
 "NEG 1 · şahıs 2MS x1 · 3MP x5 · 1P x2 · 3FS x2, baskın şahıs 3, iltifât 0 · n=13 mora=76 harf=61 "
 "(n z=0,06), fâsıla صَٰغِرُونَ *(küçük düşmüşler)* → ن, N sınıfı; **i'râb GEN 1 · ACC 2 · NOM 1**; "
 "bab I x2 · IV x1; zaman IMPV 1 · IMPF x2; simetri [3,5,8,1]; dış düğüm 0 · yıldız ★ yok · kökler "
 "رجع *(dönme, geri döndürme)* · أتي *(gelme, getirme)* · جند *(ordu, asker)* · قبل *(ön, önce; "
 "kabul)* · خرج *(çıkma, çıkarma)* · ذلل *(zillet, alçalma)* · **صغر *(küçüklük, aşağılanma)* — "
 "YENİ KÖK, n=13** · bağ: **ذلل *(zillet, alçalma)* 27:34'ten sonra ikinci geçiş** — orada "
 "kralların YAPTIĞI, burada Süleymân'ın TEHDİDİ; **aynı kök, aynı kalıp (أَذِلَّة), üç ayet "
 "arayla, iki ayrı ağızda**; **جند *(ordu, asker)* 27:17 ve 27:18'den sonra sûrede üçüncü geçiş** "
 "(elle, L1, aday 812)"),
38: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru + nida, kip VOC 1 · INTG 1 "
 "· şahıs 3MS x2 · 2MP x1 · 1S x2 · 3FS x1 · 3MP x2, baskın şahıs 3, iltifât 0 · n=10 mora=59 "
 "harf=48 (n z=-0,26), fâsıla مُسْلِمِينَ *(teslim olmuşlar)* → ن, N sınıfı — **27:31'in "
 "fâsılasıyla AYNI KELİME**; **i'râb ACC 3 · NOM 2 · GEN 1**; bab I x3; zaman PERF 1 · IMPF x2; "
 "**kök ikilemesi أيي *(âyet, işaret)* x2 · أتي *(gelme, getirme)* x2**; **biçim DIKKAT**; dış "
 "düğüm 1 · iç düğüm 2 · yıldız ★ yok · kökler قول *(söz söyleme)* · أيي *(âyet, işaret)* · ملأ "
 "*(ileri gelenler (meleʼ); doldurma)* · أتي *(gelme, getirme)* · عرش *(arş, taht)* · قبل *(ön, "
 "önce; kabul)* · سلم *(esenlik; teslim olma)* · bağ: xref قال *(dedi)* + أيّ *(ey)* + ملأ *(ileri "
 "gelenler)* → **27:29 · 27:32 · 28:38**; **عرش *(arş, taht)* sûrede üçüncü geçiş** (27:23 "
 "kraliçenin tahtı, 27:26 Rabbin arşı, burada yine kraliçenin tahtı) (elle, L1, aday 815)"),
39: ("eksen: **lafız YOK · Rab YOK** · **esmâ قَوِيّ *(güçlü)* 15. sırada, MÜHÜRSÜZ — ARTEFAKT ve "
 "YENİ GÖNDERGE SINIFI: gönderge bir CİN (ifrît) ve KENDİ HAKKINDA konuşuyor** (لَقَوِىٌّ أَمِينٌ "
 "*(güç yetiririm, güvenilirim)*) · aktör yok — عِفْرِيت *(ifrît)* aktör tablosuna GİRMİYOR · edim "
 "haber, kip EMPH 1 · şahıs 3MS x3 · 1S x3 · 2MS x3, sahset ['1','2','3'], iltifât 0 · **n=16 — "
 "blokta ikinci en uzun ayet** (n z=0,38), fâsıla أَمِين *(güvenilir)* → ن, N sınıfı; **i'râb NOM "
 "3 · GEN 2 · ACC 2**; bab I x3; zaman PERF 1 · IMPF x2; **HAPAKS: عفر *(ifrît (güçlü cin))* — "
 "korpusta TEK geçiş** (hapaks z=3,38: **yıldızın TEK kaynağı**); **kök ikilemesi قوم *(kalkma; "
 "kavim; kıyamet)* x2 — تَقُومَ *(kalkarsın)* ve مَقَام *(makam)*, aynı kök fiil ve yer adı**; "
 "simetri [3,3,7,1]; dış düğüm 0 · **yıldız ★★★** · kökler قول *(söz söyleme)* · **عفر *(ifrît "
 "(güçlü cin))* — YENİ KÖK** · جنن *(örtme, gizleme; cennet; cin)* · أتي *(gelme, getirme)* · قبل "
 "*(ön, önce; kabul)* · قوم *(kalkma; kavim; kıyamet)* · قوي *(kuvvet)* · أمن *(güven; iman)* · "
 "bağ: **قوي *(kuvvet)* 27:33'ten sonra sûrede ikinci geçiş** — orada kraliçenin danışmanları "
 "kendileri için (أُو۟لُوا۟ قُوَّةٍ *(güç sahipleri)*), burada ifrît kendisi için; **iki geçiş de "
 "KENDİ HAKKINDA güç iddiası** (elle, L1, aday 816)"),
40: ("eksen: **lafız YOK · رَبّ *(Rab)* 23. VE 36. sırada — İKİ RAB TEK AYETTE, sûrenin dördüncü ve "
 "beşinci Rabbi** (rab z=0,80) · **esmâ غَنِيّ *(ganî)* 37. + كَرِيم *(kerîm)* 38. sırada = fâsıla "
 "— MÜHÜR; GEÇERLİ (gönderge رَبِّى *(Rabbim)*); sûrenin BEŞİNCİ mührü ve BEŞİNCİ FARKLI ÇİFT** · "
 "aktör yok · edim soru, kip INTG 1 · **şahıs 3MS x13 · 1S x7 · 2MS x3**, iltifât 0 · **n=38 — "
 "SÛRENİN EN UZUN AYETİ ve korpusun en uzun 130. ayeti** (n z=2,72), mora=167 harf=148, fâsıla "
 "كَرِيمٌ *(kerîm)* → **م — azınlık kafiyesi**, N sınıfı; **i'râb ACC 6 · NOM 6 · GEN 3**; bab I "
 "x10 · **bab VIII x1**; zaman PERF x5 · IMPF x6; **BEŞ KÖK BİRDEN İKİLENİYOR: قول *(söz "
 "söyleme)* x2 · عند *(kat, yan)* x2 · ربب *(rab, terbiye etme)* x2 · شكر *(şükür)* x3 · كفر "
 "*(inkâr, nankörlük)* x2 — sûrenin en çok ikilenen ayeti**; simetri [4,26,33,1]; **biçim "
 "DIKKAT**; **dış düğüm 3** · **yıldız ★★** — kaynak n z=2,72 · kökler قول *(söz söyleme)* · عند *(kat, yan)* · "
 "علم *(bilme)* · كتب *(yazma, kitap)* · أتي *(gelme, getirme)* · قبل *(ön, önce; kabul)* · ردد "
 "*(geri döndürme, dönüş)* · طرف *(uç, kenar)* · رأي *(görme)* · قرر *(karar kılma; göz "
 "aydınlığı)* · فضل *(üstün kılma, lütuf)* · ربب *(rab, terbiye etme)* · بلو *(eskiyip yıpranma)* · شكر *(şükür)* · كفر "
 "*(inkâr, nankörlük)* · نفس *(nefis, can)* · غني *(zenginlik, ganî olma)* · كرم *(üstün tutma, "
 "ikram)* · bağ: xref قال *(dedi)* + عند *(kat)* + علم *(ilim)* → **6:148**; عند *(kat)* + علم *(ilim)* + كتاب "
 "*(kitap)* → **13:43**; شكر *(şükretti)* + شكر *(şükür)* + نفس *(nefis)* → **31:12**; شكر *(şükür)* + نفس *(nefis)* + كفر "
 "*(nankörlük etti)* → **31:12** (elle, L1, aday 817/818)"),
}

M = {
31: ("Mektup beş kelimede bitiyor ve **sûrenin okunan en kısa ayeti burası** (n=5). Ölçülebilir bir "
 "yer: **iltifât mektubun İÇİNDE**. 27:30 üçüncü şahısla açılmıştı (إِنَّهُۥ مِن سُلَيْمَٰنَ *(o "
 "Süleymân'dandır)*); burada birinci-ikinci şahsa geçiliyor ve alan bunu 3>12 diye kaydediyor. "
 "**Sûrede ilk kez iltifât bir ALINTI METNİN sınırında oluyor** — 27:6'daki iltifât anlatı "
 "kipindeydi. Bu, iltifât alanının bilinen eksiklerinden birine (ad→zamir geçişleri, aday "
 "461/517) yeni bir açı: burada geçiş **anlatıcı katmanından alıntı katmanına** düşüyor ve alan "
 "onu yakalıyor. علو *(yücelik; böbürlenme)* korpusta 70 geçişli."),
32: ("Kraliçenin ilk sözü bir istişare: أَفْتُونِى فِىٓ أَمْرِى *(işim hakkında bana görüş "
 "bildirin)*. فتي *(genç, delikanlı; fetva)* korpusta 21 geçişli. Ve **kraliçe hiçbir aktör "
 "tablosuna girmiyor**: 27:23'te adsız aktör olarak `imrae` etiketiyle sayılmıştı, burada "
 "konuşan o ve alan boş — **çünkü alan sözcüğü arıyor, gönderge sürekliliğini değil.** Aday 802'nin "
 "ikinci yüzü: alan yalnız yanlış pozitif üretmiyor, **aynı kişiyi sahneden sahneye izleyemiyor** "
 "da. Ve أمر *(emir; iş)* burada iki kez, bir sonraki ayette yine iki kez — **iki ardışık ayette "
 "aynı kök dört kez.**"),
33: ("Danışmanların cevabı bir güç beyanı, ama kararı devrediyor: وَٱلْأَمْرُ إِلَيْكِ *(buyruk "
 "senin)*. **Ölçülebilir bir seyreklik: 2FS — korpusun 6236 ayetinden yalnız 30'unda var (%0,48) "
 "ve 27:33 dört işaretle en yüksek dördüncü değer** (28:7 ve 19:26 dokuzla başta). Sûre 27'de "
 "toplam üç 2FS ayeti var (27:33, 27:42, 27:44) ve üçü de aynı kişiye. Ve **نظر *(bakma; mühlet "
 "verme)* sûrede dördüncü geçiş**: 27:27 Süleymân bakacak, 27:28 hüdhüde 'bak' emri, burada "
 "kraliçeye 'bak' emri, 27:35 kraliçe bakacak. **Dördü de bir sonucu bekleme bağlamında ve ikisi "
 "emir, ikisi haber** — kök sûre boyunca tek anlam alanında kalıyor, 529 sınıfı bir sapma yok."),
34: ("**İki esmâ tokeni, ikisi de artefakt ve ikisi de ÇOĞUL İNSAN.** مَلِك'in göndergesi "
 "ٱلْمُلُوك *(krallar)*, عَزِيز'inki أَعِزَّةَ أَهْلِهَا *(halkının ileri gelenleri)*. **Bu, esmâ "
 "gönderge sınıfları envanterine (aday 747) 'çoğul insan' sınıfının ilk çift vakası** — sûre "
 "26'nın مُؤْمِن vakaları ve 27:29'un كَرِيم'i tekildi. Ve ayet kendi içinde bir karşıt çift "
 "kuruyor: **عزز *(izzet)* ile ذلل *(zillet)* aynı cümlede**, biri diğerine dönüştürülüyor. ذلل *(zillet, alçalma)* "
 "korpusta 24 geçişli ve dikey ölçümü ▸önce رهق *(yük bindirme)* ×113,6 veriyor — **n=24, koruma "
 "sınırının içinde; satır yorumlanmadı.** Ayet blokta tek şahıslı tek ayet (sahset yalnız 3)."),
35: ("Hediye kararı ve bir bekleyiş: فَنَاظِرَةٌۢ بِمَ يَرْجِعُ ٱلْمُرْسَلُونَ *(elçilerin ne ile "
 "döneceğine bakacağım)*. **Ölçülebilir bir kalıp: رسل *(gönderme, elçi)* aynı ayette iki kez, "
 "biri ism-i fâil (مُرْسِلَة *(gönderen)*), biri ism-i mef'ûl (ٱلْمُرْسَلُونَ *(gönderilenler)*)** "
 "— aynı kök tek ayette etken ve edilgen kalıpta. Ve **bir 529 vakası daha: هدي *(yol gösterme)* "
 "burada هَدِيَّة *(hediye)* anlamında; sûrede 27:24'te ٱهْتَدَى *(yol buldu)* anlamındaydı** — "
 "aynı kök, iki anlam alanı, on bir ayet arayla. Dikey satırı yine yalnız 'yol gösterme' "
 "anlamından geliyor (صرط *(sırât)* ×13,7 · furkan ×10,6); **otomatik tespit ölçütü burada da "
 "çalışmadı — 2/6'ya düştü.**"),
36: ("Süleymân'ın cevabı bir kıyas: فَمَآ ءَاتَىٰنِۦَ ٱللَّهُ خَيْرٌ مِّمَّآ ءَاتَىٰكُم *(Allah'ın "
 "bana verdiği, size verdiğinden hayırlıdır)*. **Kök ikilemesi kıyasın kendisini taşıyor: أتي "
 "*(gelme, getirme)* iki kez, aynı fiil iki ayrı muhatapla** — verenin tek olduğu, alanın "
 "değiştiği bir yapı. Sûrenin yedinci lafzı burada ve **veren özne konumunda**. Biçim IDRAB (بَلْ "
 "*(asıl)*) — sûrede 27:36'dan önce 27:47 ve 27:55'te de var ama okunmadı. مدد *(uzatma, "
 "destekleme)* korpusta 32 geçişli; أَتُمِدُّونَنِ بِمَالٍ *(bana mal ile mi yardım "
 "ediyorsunuz)* terkibinde 'destek' anlamında."),
37: ("Tehdit dört tekitle: **EMPH 4** — لَنَأْتِيَنَّهُم *(onlara mutlaka geleceğiz)* ve "
 "وَلَنُخْرِجَنَّهُم *(onları mutlaka çıkaracağız)*. Ölçülebilir bir yankı: **ذلل *(zillet, "
 "alçalma)* 27:34'te kraliçenin ağzında kralların YAPTIĞI şeydi (أَعِزَّةَ أَهْلِهَآ أَذِلَّةً), "
 "burada Süleymân'ın ağzında bir TEHDİT (أَذِلَّةً)** — aynı kök, aynı kalıp, üç ayet arayla, iki "
 "ayrı ağızda. **Kraliçenin kralların yapacağını söylediği şey, cevabında ona söyleniyor.** Ve "
 "yeni kök: صغر *(küçüklük, aşağılanma)* korpusta 13 geçişli; dikey satırı ▸sonra büyüklük ×32,5 "
 "veriyor ama **n=13, koruma sınırının içinde; yorumlanmadı**. جند *(ordu, asker)* sûrede üçüncü "
 "geçiş — 27:17 Süleymân'ın orduları, 27:18 aynı ordu, burada sefer ordusu."),
38: ("Meclis çağrısı üçüncü kez: قَالَ يَٰٓأَيُّهَا ٱلْمَلَؤُا۟ *(dedi: ey ileri gelenler)*. "
 "**Ölçülebilir bir simetri: xref kalıbı sûre içinde üç kez ve üçü de iki ayrı meclis** — 27:29 ve "
 "27:32 kraliçenin meclisi, burada Süleymân'ın meclisi; dördüncü bağ 28:38'de Firavun'un ağzında. "
 "**Aynı hitap formülü üç hükümdarda.** Ve fâsıla 27:31'in fâsılasıyla aynı kelime "
 "(مُسْلِمِينَ) — mektubun son sözü, yedi ayet sonra Süleymân'ın kendi cümlesinde geri dönüyor. "
 "عرش *(arş, taht)* sûrede üçüncü geçiş; **27:23 ve 27:26'daki belirsiz/belirli çifti burada "
 "üçüncü bir kipe giriyor: iyelikli (بِعَرْشِهَا *(onun tahtı)*)** — aday 805'in çiftine üçüncü "
 "üye."),
39: ("**Yıldızın tek kaynağı hapaks عفر *(ifrît (güçlü cin))* — korpusta tek geçiş ve dikey satırı "
 "iki listede de boş.** Ve esmâ alanı burada **yeni bir gönderge sınıfı üretiyor: قَوِيّ'nin "
 "göndergesi bir CİN ve cin KENDİ HAKKINDA konuşuyor** (إِنِّى عَلَيْهِ لَقَوِىٌّ أَمِينٌ). Şimdiye "
 "kadar sayılan gönderge sınıfları insan, nesne, soyut kavram ve yapıydı; **gayb varlığının "
 "kendini nitelemesi yeni.** Aday 747'nin envanterine 'gayb varlığı, birinci şahıs' sınıfı "
 "ekleniyor. Ölçülebilir bir yankı: **قوي *(kuvvet)* sûrede ikinci geçiş ve ikisi de KENDİ "
 "HAKKINDA güç iddiası** — 27:33'te danışmanlar (نَحْنُ أُو۟لُوا۟ قُوَّةٍ *(biz güç sahibiyiz)*), "
 "burada ifrît. **İkisi de sonuçsuz kalıyor: danışmanların gücü kullanılmıyor, ifrîtin teklifi "
 "kabul edilmiyor.**"),
40: ("**Sûrenin en uzun ayeti** (n=38; korpusun en uzun 130. ayeti, üst %2,1) ve **sûrenin en çok "
 "ikilenen ayeti: beş kök birden, biri üç kez** (شكر *(şükür)* x3). **Aday 804'ün ön-kaydı burada "
 "SINANDI ve TUTTU: 27:40'ın غَنِيّ|كَرِيم mührü GEÇERLİ** (gönderge رَبِّى) ve fâsıla harfi م — "
 "sûrenin beşinci mührü, beşinci farklı çift, beşinci م fâsıla. **Kayıt ÇALIŞAN alan (fs) "
 "tarafında tuttu; EKSİK alan (esma_k geçerliliği) tarafında da tuttu ama tek gözlemle; 27:78 "
 "okunmadan dizi KAPATILAMAZ.** Ve bir ölçüm daha: **sûrenin ilk kırk ayetinde 23 esmâ tokeni "
 "var; 10'u mühür tokeni ve onunun onu da GEÇERLİ, 13'ü mühürsüz ve on üçünün on üçü de "
 "ARTEFAKT** — mühür bayrağı bu bölütte gönderge geçerliliğini kusursuz ayırıyor. **Ama bayrak "
 "yapısal (iki esmânın bitişikliği + son konum); tek başına gelen geçerli bir ismi yakalayamaz, "
 "bu yüzden ayrımın sûre sonuna kadar süreceğini beklemiyorum.** İki Rab tek ayette ve ikisi de "
 "iyelikli (رَبِّى) — Rab'ın %99,4 bağlı olduğu kaydıyla uyumlu."),
}

ATLAMA = {
 "_mercek_27_39": ("27:39 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. Kaynak: hapaks z=3,38 (عفر *(ifrît "
  "(güçlü cin))*). Ayet bir GAYB VARLIĞI SINIFINI (ifrît, cinlerden) adlandırıyor ve bir hız "
  "iddiası kuruyor ('sen makamından kalkmadan'). **Hız iddiası bir ÖLÇÜ gibi görünüyor ama "
  "neyi ölçtüğü belirsiz: birim yok, karşılaştırma yok, mekanizma yok** — aday 799'un önerdiği "
  "ölçütün ('ölçü sözcüğü geçmesi çıpa yapmaz; ölçünün NEYİ ölçtüğü belirleyici') doğrudan "
  "vakası. 27:40'ta aynı iddia daha kısa bir süreyle tekrarlanıyor (gözünü açıp kapamadan) ve "
  "**orada da ölçü yok, yalnız bir insan-bedeni süresi**. İkisi de 'adlandırma + iddia' "
  "düzeyinde; eşik aşılmadı."),
 "_blok_notu_27_31_40": ("BLOK BİLANÇOSU: ★★★ 1 (27:39) · ★★ 1 (27:40) · ★ 0 · yıldızsız 8. "
  "Kaynaklar: hapaks x1 · uzunluk (n z) x1 — **yine hiçbiri içerikten**. İltifât 1/10 (27:31). "
  "Esmâ token 5: **üçü artefakt (27:34 x2, 27:39), ikisi geçerli mühür (27:40)**. Allah lafzı 1 "
  "(27:36) · Rab 2 (27:40, tek ayette). Adlı aktör 1 (سُلَيْمان) · adsız aktör 0 — **kraliçe "
  "blok boyunca konuşuyor ve hiçbir aktör alanına girmiyor** (aday 802'nin ikinci yüzü). Yeni kök "
  "2 (صغر, عفر). Hapaks 1 (عفر). Kafiye kırılması 0. **Yıldız dağılımı blokta en aşağıda: on "
  "ayetin sekizi yıldızsız — okumada görülen en düşük yıldız payı olabilir, KAPATILAMAZ (tam "
  "sayım koşulmadı).**"),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(31, 41):
    OM['27']["27:%d" % n] = {"ar": AR[(27, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["27:%d" % n]}
OM['27']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-26 TAM. **Sûre 27 (Neml) 40/93.** Devam: 27:41'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "27": "1-40 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1989
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 27 →', len([k for k in OM['27'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(31, 41):
    MK['27']["27:%d" % n] = M[n]
MK['27_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 27 →', len(MK['27']))
