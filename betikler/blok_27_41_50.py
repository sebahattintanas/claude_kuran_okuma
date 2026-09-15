# -*- coding: utf-8 -*-
"""blok_27_41_50.py — sûre 27 beşinci blok (27:41-50). Tahtın tanınmazlaştırılması,
köşk, teslim oluş; Semûd bölütünün açılışı ve dokuz kişilik komplo."""
import json
DIK = json.load(open('blok_dikey_27_41_50.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
41: "Dedi: Onun tahtını tanınmaz hâle getirin; bakalım tanıyacak mı, yoksa tanımayanlardan mı olacak.",
42: "Gelince, 'Senin tahtın böyle miydi?' denildi. Dedi: Sanki o. Bize daha önce ilim verilmişti ve biz teslim olmuştuk.",
43: "Allah'ı bırakıp taptığı şeyler onu alıkoymuştu; o, inkâr eden bir kavimdendi.",
44: "Ona 'Köşke gir' denildi. Onu görünce derin su sandı ve baldırlarını açtı. Dedi: O, camdan yapılmış düz bir köşktür. Dedi: Rabbim, ben kendime zulmetmişim; Süleymân'la beraber âlemlerin Rabbi olan Allah'a teslim oldum.",
45: "Andolsun, Semûd'a kardeşleri Sâlih'i 'Allah'a kulluk edin' diye gönderdik; bir de baktı ki çekişen iki bölük olmuşlar.",
46: "Dedi: Ey kavmim, iyilikten önce kötülüğü niçin çabuklaştırmak istiyorsunuz? Allah'tan bağışlanma dileseniz ya, belki merhamet olunursunuz.",
47: "Dediler: Senin ve seninle beraber olanların yüzünden uğursuzluğa uğradık. Dedi: Uğursuzluğunuz Allah katındadır; asıl siz sınanan bir kavimsiniz.",
48: "Şehirde dokuz kişilik bir grup vardı; yeryüzünde bozgunculuk yapıyor, düzeltmiyorlardı.",
49: "Dediler: Allah'a yemin ederek birbirinize söz verin; ona ve ailesine geceleyin baskın yapalım, sonra velisine 'Ailesinin helâkine biz tanık olmadık, biz elbette doğru söyleyenleriz' diyelim.",
50: "Bir tuzak kurdular, biz de bir tuzak kurduk; onlar farkında değildi.",
}

O = {
41: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru + emir, kip IMPV 1 · INTG 1 "
 "· NEG 1 · şahıs 3MS x1 · 2MP x2 · **3FS x4** · 1P x1 · 3MP x2, baskın şahıs 3, iltifât 0 · n=12 "
 "mora=61 harf=48 (n z=-0,04), fâsıla يَهْتَدُونَ *(yol buluyorlar)* → ن, N sınıfı; **i'râb ACC "
 "1**; bab I x3 · II x1 · **bab VIII x2**; zaman PERF 1 · IMPV 1 · **IMPF x4**; **kök ikilemesi "
 "هدي *(yol gösterme)* x2 — أَتَهْتَدِىٓ *(tanır mı)* ve لَا يَهْتَدُونَ *(tanımayanlar)*, "
 "olumlu-olumsuz çift**; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · نكر *(tanımama, "
 "inkâr; çirkin)* · عرش *(arş, taht)* · نظر *(bakma; mühlet verme)* · هدي *(yol gösterme)* · كون *(olmak; mekân, yer)* "
 "*(olmak; mekân, yer)* · bağ: **عرش *(arş, taht)* sûrede dördüncü geçiş**; **هدي *(yol gösterme)* sûrede dördüncü ve beşinci "
 "geçiş, burada 'tanıma' anlamında — üçüncü anlam alanı** (27:24 yol bulma, 27:35-36 hediye); "
 "**نظر *(bakma; mühlet verme)* sûrede beşinci geçiş, yine 'sonucu bekleme'** (elle, L1, aday 830)"),
42: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · şahıs 3FS x3 "
 "· 3MS x3 · **2FS x1** · 1P x4, iltifât 0 · n=14 mora=78 harf=62 (n z=0,17), fâsıla مُسْلِمِينَ "
 "*(teslim olmuşlar)* → ن, N sınıfı — **sûrede üçüncü kez aynı fâsıla** (27:31, 27:38, burası); "
 "**i'râb NOM 1 · ACC 3 · GEN 1**; bab I x4 · IV x1; **zaman PERF x5 — beş fiilin beşi de mâzi**; "
 "**edilgen 2 — قِيلَ *(denildi)* ve أُوتِينَا *(bize verildi)*; oran 2/5, pas z=1,95: yıldızın "
 "TEK kaynağı**; **kök ikilemesi قول *(söz söyleme)* x2 — biri edilgen (قِيلَ), biri etken "
 "(قَالَتْ *(dedi)*)**; simetri [3,1,4,1]; **biçim DIKKAT**; dış düğüm 1 · **yıldız ★** · kökler "
 "جيأ *(gelme)* · قول *(söz söyleme)* · عرش *(arş, taht)* · أتي *(gelme, getirme)* · علم *(bilme)* · قبل *(ön, "
 "önce; kabul)* · كون *(olmak; mekân, yer)* · سلم *(esenlik; teslim olma)* · bağ: xref آتى *(verdi)* + علم *(ilim)* + "
 "قبل *(önce)* → **17:107**; **عرش *(arş, taht)* sûrede beşinci ve son geçiş — dizi KAPANDI** (elle, L1, aday "
 "830)"),
43: ("eksen: **ALLAH LAFZI 7. sırada — sûrenin SEKİZİNCİ lafzı** (allah z=1,14) · Rab yok · esmâ "
 "yok · aktör yok · edim haber · **şahıs 3MS x1 · 3FS x5, sahset ['3']** · n=12 mora=57 harf=44 "
 "(n z=-0,04), fâsıla كَٰفِرِينَ *(inkâr edenler)* → ن, N sınıfı; **i'râb GEN 4 · ACC 1**; **bab I "
 "x4**; zaman PERF x3 · IMPF 1; **kök ikilemesi كون *(olmak; mekân, yer)* x2**; simetri [3,2,8,1]; "
 "**dış düğüm 3** · yıldız ★ yok · kökler صدد *(yüz çevirme, alıkoyma)* · كون *(olmak; mekân, yer)* · عبد *(kul, "
 "kulluk)* · دون *(beriki, başkası)* · أله *(ilâh; lafza-i celâl)* · قوم *(kalkma; kavim; "
 "kıyamet)* · كفر *(inkâr, nankörlük)* · bağ: xref كان *(idi)* + عبد *(kulluk etti)* + دون *(beriki, başkası)* "
 "*(başka)* → **3:79**; صدّ *(alıkoydu)* + كان + عبد *(kul, kulluk)* → **14:10 · 34:43**; **صدد *(yüz çevirme, alıkoyma)* sûrede ikinci "
 "geçiş** — 27:24'te şeytan onları yoldan çevirmişti, burada taptıkları çeviriyor; **aynı kök, "
 "aynı işlev, fâil değişiyor** (elle, L1)"),
44: ("eksen: **ALLAH LAFZI 26. sırada** (allah z=0,19) **· رَبّ *(Rab)* 19. VE 27. sırada — İKİ RAB "
 "TEK AYETTE** (rab z=1,20); **sûrede lafız ile Rab'ın buluştuğu üçüncü ayet (27:8, 27:26) ve İKİ "
 "Rab taşıyan İLK ayet** · esmâ yok · **aktör: adlı سُلَيْمان *(Süleymân)* 25. sırada, tür kişi, "
 "rol mecrur** · edim emir, kip IMPV 1 · şahıs 3MS x5 · 3FS x6 · **2FS x2** · 1S x7, iltifât 0 · "
 "**n=28 — sûrenin ikinci en uzun ayeti** (n z=1,65), mora=136 harf=115, fâsıla ٱلْعَٰلَمِينَ "
 "*(âlemler)* → ن, N sınıfı; **i'râb ACC 5 · GEN 6 · NOM 4**; bab I x8 · IV x1; zaman PERF x8 · "
 "IMPV 1; **edilgen 1** (قِيلَ *(denildi)*), pas z=0,30; **ÜÇ KÖK İKİLENİYOR: قول *(söz söyleme)* "
 "x3 · صرح *(köşk, yüksek yapı (sarh))* x2 · ربب *(rab, terbiye etme)* x2**; simetri [3,1,12,1]; "
 "dış düğüm 2 · **yıldız ★** — kaynak yalnız uzunluk (n z=1,65) · kökler قول *(söz söyleme)* · دخل *(girme)* · "
 "**صرح *(köşk, yüksek yapı (sarh))* — YENİ KÖK, n=4** · رأي *(görme)* · حسب *(hesap, sayma)* · لجج *(derin su, engin)* · كشف *(giderme, açma)* "
 "*(giderme, açma)* · سوق *(sürme, sevk etme; çarşı)* · مرد *(azgınlık, merîd)* · قرر *(karar "
 "kılma; göz aydınlığı)* · ربب *(rab, terbiye etme)* · ظلم *(zulüm)* · نفس *(nefis, can)* · سلم *(esenlik; teslim "
 "olma)* · أله *(ilâh; lafza-i celâl)* · علم *(bilme)* · bağ: xref قال *(dedi)* + ربّ *(Rab)* + ظلم *(zulmetti)* → **7:23 "
 "· 28:16**; ربّ + ظلم *(zulüm)* + نفس *(nefis)* → **7:23 · 28:16** (elle, L1, aday 827)"),
45: ("eksen: **ALLAH LAFZI 9. sırada — sûrenin ONUNCU lafzı** (allah z=1,01) · Rab yok · esmâ yok · "
 "**aktör: adlı ثَمُود *(Semûd)* 4. sırada, tür kavim, rol mecrur · adlı صالِح *(Sâlih)* 6. "
 "sırada, tür kişi, rol MEF'ÛL — blokta ilk mef'ûl rollü aktör** · edim emir, kip EMPH 1 · CERT 1 "
 "· IMPV 1 · şahıs 1P x2 · 3MP x4 · 2MP x2, baskın şahıs 3, iltifât 0 · n=13 mora=75 harf=58 (n "
 "z=0,06), fâsıla يَخْتَصِمُونَ *(çekişiyorlar)* → ن, N sınıfı; **i'râb GEN 1 · NOM 2 · ACC 2**; "
 "bab I x1 · IV x1 · **bab VIII x1**; zaman PERF 1 · IMPV 1 · IMPF 1; dış düğüm 0 · yıldız ★ yok · "
 "kökler رسل *(gönderme, elçi)* · أخو *(kardeş)* · صلح *(iyi, elverişli olma; ıslah)* · عبد *(kul, "
 "kulluk)* · أله *(ilâh; lafza-i celâl)* · فرق *(ayırma, parçalara bölme)* · خصم *(husumet, "
 "çekişme)* · bağ: **SÛRENİN ÜÇÜNCÜ ANLATI BÖLÜTÜ BURADA AÇILIYOR** — Mûsâ (27:7-14), "
 "Dâvûd-Süleymân (27:15-44), Semûd (27:45-53); **üç bölütün üçü de وَ + geçmiş zaman fiiliyle "
 "değil, biri لَقَدْ ile açılıyor**; صلح *(iyi, elverişli olma; ıslah)* kökü hem elçinin adı hem 27:48'in fiili (elle, L1, aday "
 "828)"),
46: ("eksen: **ALLAH LAFZI 10. sırada — sûrenin ON BİRİNCİ lafzı** (allah z=1,14) · Rab yok · esmâ "
 "yok · aktör yok · edim soru + nida, kip VOC 1 · INTG 1 · **şahıs 2MP x7** · 3MS x1 · 1S x1, "
 "iltifât 0 · n=12 mora=72 harf=61 (n z=-0,04), fâsıla تُرْحَمُونَ *(merhamet olunursunuz)* → ن, N "
 "sınıfı; **i'râb NOM 1 · GEN 2 · ACC 3**; bab I x2 · **bab X x2**; zaman PERF 1 · IMPF x3; "
 "**edilgen 1** (تُرْحَمُونَ), pas z=1,10; dış düğüm 1 · yıldız ★ yok · kökler قول *(söz "
 "söyleme)* · قوم *(kalkma; kavim; kıyamet)* · عجل *(acele)* · سوأ *(kötülük)* · قبل *(ön, önce; "
 "kabul)* · حسن *(güzellik, iyilik)* · غفر *(bağışlama, mağfiret)* · أله *(ilâh; lafza-i celâl)* · رحم *(rahmet, "
 "merhamet)* · bağ: xref استعجل *(acele istedi)* + سيّئة *(kötülük)* + قبل *(önce)* → **13:6**; "
 "سيّئة + قبل *(ön, önce; kabul)* + حسنة *(iyilik)* → **13:6**; **سوأ *(kötülük)* ile حسن *(güzellik, iyilik)* aynı ayette karşıt çift** (elle, L1)"),
47: ("eksen: **ALLAH LAFZI 9. sırada — sûrenin ON İKİNCİ lafzı** (allah z=1,01) · Rab yok · esmâ "
 "yok · aktör yok · edim haber · şahıs 3MP x2 · 1P x2 · 2MS x2 · 3MS x1 · 2MP x4, iltifât 0 · n=13 "
 "mora=64 harf=54 (n z=0,06), fâsıla تُفْتَنُونَ *(sınanıyorsunuz)* → ن, N sınıfı; **i'râb ACC 2 · "
 "NOM 2 · GEN 1**; bab I x3 · **bab V x1**; zaman PERF x3 · IMPF 1; **edilgen 1** (تُفْتَنُونَ), "
 "pas z=1,10; **kök ikilemesi قول *(söz söyleme)* x2 · طير *(kuş; uçan)* x2**; simetri [3,3,10,1]; "
 "**biçim IDRAB**; dış düğüm 2 · yıldız ★ yok · kökler قول *(söz söyleme)* · **طير *(kuş; uçan)* — SÛREDE "
 "DÖRDÜNCÜ GEÇİŞ VE İKİNCİ ANLAM ALANI** · عند *(kat, yan)* · أله *(ilâh; lafza-i celâl)* · قوم *(kalkma; kavim; kıyamet)* · فتن *(sınama, fitne)* · "
 "bağ: xref عند *(kat)* + اللّه *(Allah)* + قوم *(kavim)* → **4:78**; طائر *(uğur, kuş)* + عند *(kat, yan)* + "
 "اللّه → **7:131** (elle, L1, aday 823)"),
48: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · **şahıs 3MS "
 "x1 · 3MP x4, sahset ['3']** · n=10 mora=50 harf=43 (n z=-0,26), fâsıla يُصْلِحُونَ *(düzeltirler)* "
 "→ ن, N sınıfı; **i'râb GEN 3 · NOM 1**; bab I x1 · IV x2; zaman PERF 1 · IMPF x2; **SAYI ALANI "
 "DOLU: تسع *(dokuz)* → تِسْعَة *(dokuz kişi)*** — sûrede ikinci sayı; dış düğüm 1 · yıldız ★ yok "
 "· kökler كون *(olmak; mekân, yer)* · مدن *(şehir; Medyen)* · **تسع *(dokuz)*, n=7** · **رهط *(grup, takım (reht))* "
 "*(grup, takım (reht))* — YENİ KÖK, n=3** · فسد *(bozgunculuk, fesat)* · أرض *(yer, yeryüzü)* · "
 "صلح *(iyi, elverişli olma; ıslah)* · bağ: xref أفسد *(bozdu)* + أرض *(yer)* + أصلح *(düzeltti)* "
 "→ **26:152** — **Semûd bölütünün sûre 26'daki karşılığında birebir aynı formül**; **فسد *(bozgunculuk, fesat)* ile صلح *(iyi, elverişli olma; ıslah)* "
 "aynı ayette karşıt çift** (elle, L1, aday 829)"),
49: ("eksen: **ALLAH LAFZI 3. sırada — sûrenin ON ÜÇÜNCÜ lafzı** (allah z=0,90) · Rab yok · **esmâ "
 "وَلِيّ *(velî)* 8. sırada, ORTA konum, MÜHÜRSÜZ — ARTEFAKT**: gönderge لِوَلِيِّهِۦ *(velisine)*, "
 "Sâlih'in kan bağıyla yakını, İNSAN TEKİL · aktör yok · edim emir, **kip IMPV 1 · EMPH 5** · NEG "
 "1 · şahıs 3MP x2 · 2MP x2 · **1P x5** · 3MS x4, iltifât 0 · n=14 mora=84 harf=73 (n z=0,17), "
 "fâsıla لَصَٰدِقُونَ *(doğru söyleyenler)* → ن, N sınıfı; **i'râb GEN 3 · ACC 3 · NOM 1**; bab I "
 "x3 · II x1 · **bab VI x1**; zaman PERF x2 · IMPV 1 · IMPF x2; **kök ikilemesi قول *(söz "
 "söyleme)* x2 · أهل *(halk, aile)* x2**; simetri [3,5,12,1]; **biçim QASEM — SÛRENİN TEK "
 "YEMİNİ**; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · قسم *(paylaştırma; yemin)* · أله *(ilâh; "
 "lafza-i celâl)* · بيت *(ev, mesken)* · أهل *(halk, aile)* · ولي *(dost, veli; velâyet)* · شهد *(şahitlik)* · "
 "هلك *(helâk)* · صدق *(doğruluk)* · bağ: **korpusta 71 QASEM ayeti var; sûre 27'de yalnız burası** "
 "(elle, L1, aday 825/826)"),
50: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · şahıs 3MP x5 "
 "· 1P x2, sahset ['1','3'], iltifât 0 · **n=7 — blokta en kısa ayet** (n z=-0,58), fâsıla "
 "يَشْعُرُونَ *(farkına varıyorlar)* → ن, N sınıfı; **i'râb ACC 2**; **bab I x3**; zaman PERF x2 · "
 "IMPF 1; **KÖK İKİLEMESİ مكر *(tuzak)* x4 — n=7'lik ayette tek kök DÖRT kez; oran 0,57, korpusun "
 "ikinci en yüksek tek-kök yoğunluğu** (53:38'de 3/5 = 0,60; mutlak sayıda 27:50 daha yüksek); dış "
 "düğüm 0 · yıldız ★ yok · kökler مكر *(tuzak)* · شعر *(şair; farkında olma)* · bağ: **iki kök, "
 "yedi kelime — blokta en az kök çeşitliliği** (elle, L1, aday 822)"),
}

M = {
41: ("Tanıma bir sınava çevriliyor: نَكِّرُوا۟ لَهَا عَرْشَهَا *(tahtını tanınmaz hâle getirin)*. "
 "Ölçülebilir bir kök izi: **هدي *(yol gösterme)* bu ayette iki kez ve sûrede ÜÇÜNCÜ anlam "
 "alanında** — 27:24'te 'yol bulma', 27:35-36'da 'hediye', burada 'tanıma'. Aday 814 iki anlam "
 "alanı saymıştı; **üç oldu.** Ve **نظر *(bakma; mühlet verme)* sûrede beşinci geçiş ve beşi de "
 "aynı bağlamda** — sonucu bekleme; kök hiç sapmıyor. **İki kök, aynı sûre, biri üç anlam alanına "
 "yayılıyor diğeri tek alanda kalıyor: 529 kümesinin sorusu kökün kendisinde, dağılımında değil.** "
 "نكر *(tanımama, inkâr; çirkin)* korpusta 37 geçişli."),
42: ("Cevap iki edilgenle geliyor: قِيلَ *(denildi)* ve أُوتِينَا *(bize verildi)*; **beş fiilin "
 "ikisi edilgen, oran 0,40 → pas z=1,95, yıldızın tek kaynağı.** Ve قول *(söz söyleme)* aynı "
 "ayette iki kez, biri edilgen biri etken — soruyu kimin sorduğu söylenmiyor, cevabı verenin adı "
 "söyleniyor. **Fâsıla مُسْلِمِينَ sûrede üçüncü kez** (27:31 mektubun son sözü, 27:38 Süleymân'ın "
 "cümlesi, burada kraliçenin kendi sözü) — **mektubun talebi, on bir ayet sonra muhatabın ağzında "
 "yerine gelmiş olarak dönüyor.** عرش *(arş, taht)* burada sûredeki beşinci ve son geçişini "
 "yapıyor: belirsiz (27:23) → belirli (27:26) → iyelikli (27:23'ün sahibine, 27:38) → nesne olarak "
 "(27:41) → **soruda (27:42)**. **Dizi kapandı: sûre içi beş geçişin beşi de okundu.**"),
43: ("Bir alıkoyma cümlesi: وَصَدَّهَا مَا كَانَت تَّعْبُدُ مِن دُونِ ٱللَّهِ *(Allah'ı bırakıp "
 "taptığı şeyler onu alıkoymuştu)*. Ölçülebilir bir yankı: **صدد *(yüz çevirme, alıkoyma)* sûrede "
 "ikinci geçiş ve işlev aynı, fâil değişiyor** — 27:24'te şeytan onları yoldan çeviriyordu, burada "
 "taptıkları çeviriyor. Kök korpusta 42 geçişli ve dikey ölçümü ▸önce زين *(süsleme)* ×15,6 "
 "veriyor; **27:24'te tam olarak زين *(süsleme)* ile birlikteydi** — yani dikey satır bu sûre içi çifti "
 "korpus düzeyinde de doğruluyor. Ayet dış düğümü üç: bu terkip korpusta üç yerde daha var."),
44: ("**Sûrenin ikinci en uzun ayeti** ve **eksenin üç işaretinin buluştuğu ilk yer: lafız bir kez, "
 "Rab İKİ kez** — sûrede lafızla Rab 27:8 ve 27:26'da da buluşmuştu ama iki Rab taşıyan ilk ayet "
 "bu. Birincisi seslenme (رَبِّ *(Rabbim)*), ikincisi tamlama (رَبِّ ٱلْعَٰلَمِينَ *(âlemlerin "
 "Rabbi)*) — **ikisi de bağlı, Rab'ın %99,4 bağlı olduğu kaydıyla uyumlu.** Üç kök ikileniyor. "
 "Yeni kök صرح *(köşk, yüksek yapı (sarh))* korpusta dört geçişli ve dikey satırı neredeyse boş. "
 "**Ölçülebilir bir yıldız kaynağı sorusu: ayet ★ alıyor ve kaynağı YALNIZ uzunluk** (n z=1,65); "
 "eksenin üç işareti eşiği aşmıyor çünkü allah z=0,19 ve rab z=1,20. **Sûrenin en yoğun eksen "
 "ayeti, eksen üzerinden yıldız almıyor.**"),
45: ("**Sûrenin üçüncü anlatı bölütü burada açılıyor**: Mûsâ (27:7-14), Dâvûd-Süleymân (27:15-44), "
 "Semûd (27:45-53). Ölçülebilir bir eksen sıçraması: **27:43-49 arasında yedi ayetin ALTISINDA "
 "Allah lafzı var** (43, 44, 45, 46, 47, 49); sûrenin ilk kırk iki ayetinde toplam sekiz lafız "
 "vardı. **Sûre 27'nin ilk eksen kümesi bu.** Okunan korpusta yedi ayetlik pencerede en yüksek "
 "değer 7/7 ve yalnız sûre 24'te görülüyor; sûre 27'nin kendi azamisi 27:59-65'te 7/7 (okunmadı). "
 "Ve bir ad örtüşmesi: **صلح *(iyi, elverişli olma; ıslah)* hem elçinin adı (صالِح) hem 27:48'in "
 "fiili (يُصْلِحُونَ)** — üç ayet arayla aynı kök, biri özel ad biri fiil."),
46: ("Sâlih'in ilk sözü bir zamanlama sorusu: لِمَ تَسْتَعْجِلُونَ بِٱلسَّيِّئَةِ قَبْلَ "
 "ٱلْحَسَنَةِ *(iyilikten önce kötülüğü niçin çabuklaştırmak istiyorsunuz)*. **Karşıt çift tek "
 "ayette: سوأ *(kötülük)* (n=167) ve حسن *(güzellik, iyilik)* (n=194)** — blokta ikinci karşıt "
 "çift (27:48'de فسد *(bozgunculuk, fesat)*/صلح *(iyi, elverişli olma; ıslah)* gelecek). Bab dağılımında iki bab X (تَسْتَعْجِلُونَ *(acele "
 "istiyorsunuz)*, تَسْتَغْفِرُونَ *(bağışlanma diliyorsunuz)*) — **aynı vezinde iki karşıt istek: "
 "azabı istemek ve affı istemek.** عجل *(acele)* korpusta 47 geçişli."),
47: ("**Sûrenin üçüncü 529 vakası ve en keskini: طير *(kuş; uçan)* sûrede dördüncü geçişini "
 "yapıyor ve anlam alanı değişiyor.** 27:16 (kuş dili), 27:17 (kuş orduları), 27:20 (kuşları "
 "denetlemesi) — üçü de canlı; burada ٱطَّيَّرْنَا *(uğursuzluğa uğradık)* ve طَٰٓئِرُكُمْ "
 "*(uğursuzluğunuz)*, yani **fal/uğur**. Aynı kök, aynı sûre, yirmi yedi ayet arayla. Ve dikey "
 "satırı yine yalnız çoğunluk anlamından geliyor (şekil-biçim ×474,2 · طين *(çamur)* ×59,3 · dağ "
 "×18,2 — hepsi 'kuş'); **otomatik tespit ölçütü YEDİNCİ vakada da çalışmadı → 2/7.** Üstelik bu "
 "vakada azınlık anlamı korpusta seyrek DEĞİL; ölçüt yalnız sıklık yüzünden değil, **birlikte "
 "geçen köklerin anlam alanını hiç kullanmadığı için** kör."),
48: ("Dokuz kişilik bir grup: تِسْعَةُ رَهْطٍ. **Ölçülebilir bir onarım: dikey katmanın sûre "
 "27'deki üç uyarı vakasından biri tam burada ve aday 806'nın ölçütü onu açıklıyor.** تسع *(dokuz)* "
 "satırı ▸sonra نعج *(dişi koyun)* ×948,5 veriyor; ölçüldü: **نعج *(dişi koyun)* korpusta dört geçişli ve "
 "komşuluktaki ikisi de TEK ayette (38:23, doksan dokuz koyun)** — tek sahne, satır artefakt. Aynı "
 "ölçüt diğer iki uyarı vakasını da açıklıyor: **ودي *(vâdi)* ×534,8 ve نمل *(karınca)* ×520,0'ın ikisi de tek ayetten "
 "geliyor (27:18, karınca vadisi).** Ve xref burada sûreler arası bir formül veriyor: أفسد + أرض *(yer, yeryüzü)* + "
 "أصلح **26:152'de birebir aynı** — sûre 26'nın Semûd bölütünde. **İki sûre, aynı kavim, aynı "
 "formül.** فسد *(bozgunculuk, fesat)* ile صلح *(ıslah)* aynı ayette karşıt çift."),
49: ("**Sûrenin tek yemini ve bir suikast yemini.** Korpusta 71 QASEM ayeti var; sûre 27'de yalnız "
 "burası, ve **yemin edenler bir peygamberi ve ailesini geceleyin öldürmeye ant içiyor, üstelik "
 "بِٱللَّهِ *(Allah'a)* diyerek.** Beş tekit işareti (EMPH 5) — 27:21'in altısından sonra sûrenin "
 "ikinci en tekitli ayeti. Ve **aday 818'in ön-kaydı burada ilk kez sınandı: وَلِيّ mühürsüz bir "
 "esmâ tokeni ve göndergesi لِوَلِيِّهِۦ, yani Sâlih'in kan yakını — ARTEFAKT.** Ayrım bozulmadı: "
 "sûrede mühürsüz token sayısı on üçten on dörde çıktı, geçerli sayısı hâlâ sıfır. **Sekiz "
 "sınamanın birincisi geçti; ön-kayıt ayakta.** هلك *(helâk)* korpusta 68 geçişli ve burada "
 "'ailesinin helâki' terkibinde, yani failin kendi eyleminin adı olarak kullanılıyor."),
50: ("Yedi kelime, iki kök. **Ölçülebilir bir uç değer: مكر *(tuzak)* aynı ayette DÖRT kez; oran "
 "4/7 = 0,57, korpusun ikinci en yüksek tek-kök yoğunluğu** — 53:38'de 3/5 = 0,60 daha yüksek ama "
 "mutlak sayıda 27:50 önde. Yapı simetrik: iki kez onlar, iki kez biz; **aynı kök, aynı vezin, "
 "özne değişiyor.** Bu, 27:43'ün (صدد *(yüz çevirme, alıkoyma)*, fâil değişiyor) ve 27:36'nın (أتي *(gelme, getirme)*, muhatap değişiyor) "
 "kurduğu kalıbın üçüncü ve en sıkı biçimi — **blokta üç kez aynı yapı: kök sabit, konum sabit, "
 "özne ya da muhatap karşıt.** شعر *(şair; farkında olma)* dikey ölçümü ▸önce مكر *(tuzak)* ×21,5 veriyor; "
 "iki kök korpusta karşılıklı bağlı."),
}

ATLAMA = {
 "_blok_notu_27_41_50": ("BLOK BİLANÇOSU: ★★★ 0 · ★★ 0 · ★ 2 (27:42 pas, 27:44 uzunluk) · "
  "yıldızsız 8. **Blokta ★★ ve üstü HİÇ YOK — okumada ilk kez.** Kaynaklar: pas x1 · uzunluk x1 "
  "— içerikten sıfır. İltifât 0/10. Esmâ token 1 (27:49 وَلِيّ, ARTEFAKT). **Allah lafzı 6 — "
  "blok rekoru; 27:43-49 arasında yedi ayetin altısında** · Rab 2 (ikisi de 27:44'te). Adlı aktör "
  "3 (سُلَيْمان, ثَمُود, صالِح) · adsız aktör 0 — **kraliçe yine hiçbir aktör alanına girmiyor, "
  "üstelik 27:42 ve 27:44'te KONUŞAN o.** Yeni kök 2 (صرح *(köşk, yüksek yapı (sarh))*, رهط *(grup, takım (reht))*). Hapaks 0. Kafiye kırılması 0. "
  "**Üç blok üst üste yıldızsız oran ≥%80.**"),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(41, 51):
    OM['27']["27:%d" % n] = {"ar": AR[(27, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["27:%d" % n]}
OM['27']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-26 TAM. **Sûre 27 (Neml) 50/93.** Devam: 27:51'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "27": "1-50 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1999
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 27 →', len([k for k in OM['27'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(41, 51):
    MK['27']["27:%d" % n] = M[n]
MK['27_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 27 →', len(MK['27']))
