# -*- coding: utf-8 -*-
"""blok_25_1_10.py — sûre 25 (Furkān) makro profili + ilk blok (25:1-10).
Blok 25:1-20 ikiye bölündü; gerekçe _blok_bolme_notu alanında.
"""
import json
DIK = json.load(open('blok_dikey_25_1_20.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']
# 25:1 metninde besmele var; okuma metnine besmelesiz girer (23:1, 24:1 emsali)
BESMELE = "بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ "
AR[(25, 1)] = AR[(25, 1)].replace(BESMELE, "")

MAKRO = {
 "ad": "FURKĀN",
 "ayet": 77,
 "kelime": 893,
 "ort_kelime": 11.60,
 "tip": "Mekkî",
 "nuzul": "42 (BELLEKTEN, doğrulanmadı — dosya GÜVENİLMEZ, kullanılmadı)",
 "eksen": ("**Allah lafzı 8 geçiş / 6 ayet (0,26x) · رَبّ *(Rab)* 14 geçiş / 14 ayet (1,24x) · "
   "A/R = 0,57.** A/R EKSENİNİN ÜÇÜNCÜ VERİ NOKTASI (adaylar 470, 498): sûre 23 (Mekkî) "
   "A/R=0,57 · sûre 24 (Medenî) R=0 dolayısıyla tanımsız · sûre 25 (Mekkî) A/R=0,57. İki "
   "Mekkî sûre aynı iki haneli oranı veriyor. KORPUS TARAMASI: kelime>=500 olan 45 sûre "
   "içinde Allah yoğunluğu en düşük 14 sûrenin ON DÖRDÜ DE MEKKÎ; sûre 25 bu sıralamada "
   "dokuzuncu. Neredeyse tam ikiz: sûre 34 (883 kelime, A=8, R=14). Lafızlı ayet yalnız "
   "17, 41, 55, 68 (x2), 70 (x2), 71 — altı ayet. İLK ON BEŞ AYETTE NE LAFIZ NE RAB VAR; "
   "gönderge ٱلَّذِى *(o ki)* ile veriliyor (25:1, 2, 6, 10). İlk رَبّ *(Rab)* 25:16'da, "
   "ilk lafız 25:17'de. Sûre çapında ٱلَّذِى sayımı SÛRE SONUNA ERTELENDİ — kalıp iddiası "
   "kuralı (aday 527). (aday 525)"),
 "kafiye": ("**A sınıfı 76 · ل 1** — kırık işaretli tek ayet 25:17, sûrenin tek ل fâsılası. "
   "Saflık 0,987, iki sınıf. Korpus bağlamı (ayet>=50): tek sınıflı sûreler 23, 21, 18, 27, "
   "54, 68; sûre 25 hemen ardında (17 ve 10 ile birlikte). Nûr dört sınıflıydı (0,844), "
   "Mü'minûn tek sınıflı (1,000). **VE FÂSILA İ'RÂBI TEK YÖNLÜ: 77 fâsıla kelimesinin 77'si "
   "de ACC.** Karşılaştırma: sûre 23 NOM 36 · GEN 27 · ACC 9; sûre 24 NOM 36 · GEN 15 · "
   "ACC 2. (aday 526)"),
 "esma": ("**22 token / 17 ayet / MÜHÜR 2** — mühürlerin ikisi de غَفُور|رَحِيم *(gafûr | rahîm)*, "
   "25:6 ve 25:70. Dağılım: رَحْمٰن *(rahmân)* 5 · كَبِير *(büyük)* 3 · غَفُور *(bağışlayan)* 2 · "
   "رَحِيم *(merhamet eden)* 2 · خَبِير *(haberdar)* 2 · سَلام *(esenlik)* 2 · وَلِيّ *(velî)* · "
   "بَصِير *(gören)* · نَصِير *(yardımcı)* · وَكِيل *(vekîl)* · قَدِير *(kadîr)* · كَرِيم *(kerîm)* "
   "birer. Mühür sayımı üçüncü veri noktası (aday 501): Mü'minûn 0 · Nûr 12 · Furkān 2. "
   "Mühürsüz 15 ayetin bağlam denetimi okuma ilerledikçe yapılacak; ESMÂ TABANLI HİÇBİR "
   "BULGU TABLO ONARILMADAN KAPATILMAZ (adaylar 461, 484, 497, 508)."),
 "soz_edimi": "haber 51 · **emir 13 · soru 9** · şart 5 · nida 3 · yasak 1",
 "fig": "**HASR 11** · DIKKAT 6 · IDRAB 3 · NEHY 1 · KELLA 1 · **QASEM SIFIR**",
 "dilbilgisi": ("i'râb **ACC 229** · GEN 98 · NOM 57 — ACC payı 0,596, i'râb tokeni>=200 olan "
   "49 sûre içinde BİRİNCİ; fâsıla kelimesi çıkarılınca pay 0,495'e düşüyor ama sûre HÂLÂ "
   "BİRİNCİ (45 sûre içinde; ikinci 19 Meryem 0,448). zaman PERF 138 · IMPF 90 · IMPV 15; "
   "bab I 167 · IV 28 · II 21 · VIII 13 · V 4 · VI 3 · X 3 · III 3 · VII 1; edilgen 16 fiil / "
   "15 ayet; **iltifât 3** — 25:14 (3>2), 25:52 (1>23), 25:56 (3>12). Mü'minûn 7, Nûr 0; "
   "Nûr'un sıfırı ADAY 517 NEDENİYLE ŞÜPHELİ, karşılaştırma onarım öncesi kurulmayacak."),
 "yildiz": {"0": 58, "1": 8, "2": 5, "3": 6},
 "yildiz3": [28, 33, 34, 64, 75, 77],
 "hapaks": ("Üç ayette ve hepsi tekil: 25:28 فلن *(falan, filan kimse)* · 25:33 فسر "
   "*(açıklama, tefsir)* · 25:77 عبأ *(değer verme, aldırma)*."),
 "esit": "**Tam-ayet ikizi YOK** — esit alanı sûre boyunca boş. (Ama 25:9 ile 17:48 birebir; aday 530.)",
 "aktor": ("Adlı: قُرْءان *(Kur'ân)* x2 · جَهَنَّم *(cehennem)* x2 · جَنَّة *(cennet, bahçe)* · "
   "شَيْطان *(şeytan)* · مُوسَى *(Mûsâ)* · هارُون *(Hârûn)* · نُوح *(Nûh)* · عاد *(Âd)* · "
   "ثَمُود *(Semûd)*. Adsız: racül *(bir adam)* 25:8 · nefer *(bir bölük)* 25:60. "
   "AKTÖR YOĞUNLUĞU KARŞILAŞTIRMASI YAPILMADI — aday 462 tasarım kararı bekliyor."),
 "sozluk": ("612 kök tokeni · 250 ayrık kök · çeşitlilik 0,408 · tek geçişli kök 137. En sık: "
   "كون *(olmak)* 24 · قول *(söz söyleme)* 22 · جعل *(kılma, var etme)* 17 · ربب "
   "*(rab, terbiye etme)* 14 · أله *(ilâh; lafza-i celâl)* 12 · يوم *(gün)* 11. **فرق "
   "*(ayırma, parçalara bölme)* SÛREDE TEK GEÇİŞ — 25:1'de ٱلْفُرْقَان *(Furkān)* olarak; "
   "sûreye adını veren kelime sûre içinde bir kere görünüyor.** تَبَارَكَ *(ne yücedir)* üç kez: "
   "25:1, 25:10, 25:61 (aday 528)."),
}

BOLME = ("Blok 25:1-20 İKİYE BÖLÜNDÜ (25:1-10 ve 25:11-20). Gerekçe iki parçalı ve ölçülü: "
 "(1) YAPI — 25:1 ve 25:10 aynı fiille açılıyor, تَبَارَكَ *(ne yücedir)*, برك *(bereket)* kökü, "
 "ikisi de PERF ve ikisi de ٱلَّذِى *(o ki)* ile devam ediyor; 25:11 بَلْ *(hayır, bilakis)* ile "
 "açılıyor ve IDRAB etiketi alıyor, sahne dünyadaki itirazdan âhirete geçiyor. Bölme çizgisi "
 "metnin kendi işaretine denk düşüyor. (2) HACİM — açılış onlusunda ayet başına ortalama 9,7 "
 "kök düşüyor (ikinci onluda 8,4); dikey katman ayet başına ortalama 1650 karakter üretiyor. "
 "Blok akışı 20 ayet kuralı okuma HIZI kuralıdır, biçim kuralı değil (24:41-45 emsali); "
 "ölçüm ve kayıt biçimi değişmedi.")

MEAL = {
1: "Âlemlere bir uyarıcı olsun diye kuluna Furkān'ı indiren ne yücedir.",
2: "Göklerin ve yerin mülkü onundur; çocuk edinmemiştir, mülkte ortağı olmamıştır. Her şeyi yaratmış, ona bir ölçü biçmiştir.",
3: "Onun yanı sıra, hiçbir şey yaratamayan — kendileri yaratılan — kendilerine ne zarar ne fayda verebilen, ölüme de hayata da dirilişe de gücü yetmeyen ilâhlar edindiler.",
4: "İnkâr edenler dediler ki: Bu, onun uydurduğu bir yalandan başka bir şey değil; başka bir topluluk da ona yardım etti. Böylece bir zulüm ve bir yalanla geldiler.",
5: "Ve dediler ki: Öncekilerin masalları; onları yazdırmış, sabah akşam kendisine okunuyor.",
6: "De ki: Onu, göklerdeki ve yerdeki sırrı bilen indirdi. O, bağışlayandır, merhamet edendir.",
7: "Ve dediler ki: Bu ne biçim elçi — yemek yiyor, çarşılarda dolaşıyor? Ona bir melek indirilseydi de yanında bir uyarıcı olsaydı ya!",
8: "Yahut kendisine bir hazine bırakılsaydı, ya da yiyeceği bir bahçesi olsaydı. Zalimler dedi ki: Siz büyülenmiş bir adamdan başkasına uymuyorsunuz.",
9: "Bak, senin için nasıl misaller getirdiler de saptılar; artık bir yol bulmaya güçleri yetmiyor.",
10: "Ne yücedir o ki, dilerse sana bundan daha hayırlısını verir: altından ırmaklar akan bahçeler; sana köşkler de verir.",
}

OLCUM = {
1: ("eksen: **Allah lafzı YOK · Rab YOK — sûre gönderge olarak ٱلَّذِى *(o ki)* ile açılıyor**; "
 "esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs 3MS x4, iltifât 0 · n=9 mora=54 "
 "harf=63 (n z=-0,36), **fâsıla نَذِيرًا *(uyarıcı)* → ا, A sınıfı, ACC**; i'râb ACC 2 · GEN 2; "
 "bab I x1 · II x1 · VI x1; zaman PERF x2 · IMPF x1; hapaks yok, kök ikilemesi yok, biçim "
 "etiketi yok; dış düğüm 0 · yıldız ★ yok · kökler برك *(bereket)* · نزل *(inme, indirme)* · "
 "فرق *(ayırma, parçalara bölme)* · عبد *(kul, kulluk)* · كون *(olmak)* · علم *(bilme; âlem)* · "
 "نذر *(uyarma; adak)* · bağ: **فرق *(ayırma, parçalara bölme)* sûrede TEK geçiş**; برك "
 "*(bereket)* 25:10 ve 25:61 ile üçlü (elle, L1, aday 528)"),
2: ("eksen: **lafız YOK · Rab YOK — gönderge yine ٱلَّذِى *(o ki)*, önceki ayetin devamı** · esmâ "
 "yok · aktör yok · edim haber, kip NEG x2 · şahıs 3MS x7, iltifât 0 · n=19 mora=87 harf=78 "
 "(n z=0,70), fâsıla تَقْدِيرًۭا *(bir ölçü biçme)* → ا, A sınıfı, ACC; i'râb GEN 4 · ACC 3 · "
 "NOM 2; bab I x2 · II x1 · VIII x1; zaman IMPF x2 · PERF x2; **kök ikilemesi ملك *(mülk; melik)* "
 "x2 · قدر *(ölçü, güç yetirme)* x2**; simetri [3,2,13,1]; **dış düğüm 2** · yıldız ★ yok · "
 "kökler ملك *(mülk; melik)* · سمو *(ad; gök)* · أرض *(yer, yeryüzü)* · أخذ *(alma, edinme)* · "
 "ولد *(doğurma, çocuk)* · كون *(olmak)* · شرك *(ortak koşma)* · خلق *(yaratma)* · كلل "
 "*(hep, bütün)* · شيأ *(dileme; şey)* · قدر *(ölçü, güç yetirme)* · bağ: xref خلق كلّ شىء "
 "*(her şeyi yarattı)* → **6:101**; اتّخذ ولد كان *(çocuk edindi, oldu)* · ولد كان شريك "
 "*(çocuk, oldu, ortak)* · كان شريك ملك *(oldu, ortak, mülk)* → **üç ayrı 3-gram, üçü de tek "
 "ayete: 17:111**"),
3: ("eksen: **lafız YOK · Rab YOK**; أله *(ilâh; lafza-i celâl)* kökü var ama ÇOĞUL ve gönderge "
 "sahte ilâhlar — ءَالِهَةً *(ilâhlar)* · esmâ yok · aktör yok · edim haber, **kip NEG x6 — blokta "
 "en yoğun olumsuzlama** · şahıs 3MP x12 · 3MS x1, iltifât 0 · n=22 mora=124 harf=102 — **bloğun "
 "en uzun ayeti** (n z=1,02), fâsıla نُشُورًۭا *(diriliş)* → ا, A sınıfı, ACC; **i'râb ACC 7 · "
 "GEN 2 — ACC baskınlığının blok içindeki en keskin örneği**; bab I x4 · VIII x1; zaman IMPF x4 · "
 "PERF x1; **edilgen 1 — يُخْلَقُونَ *(yaratılıyorlar)*** (pas z=0,81); **kök ikilemesi خلق "
 "*(yaratma)* x2 · ملك *(mülk; melik)* x2**; simetri [4,8,14,1]; **dış düğüm 3** · yıldız ★ yok · "
 "kökler أخذ *(alma, edinme)* · دون *(beriki, başkası)* · أله *(ilâh; lafza-i celâl)* · خلق "
 "*(yaratma)* · شيأ *(dileme; şey)* · ملك *(mülk; melik)* · نفس *(nefis, can)* · ضرر *(zarar)* · "
 "نفع *(fayda)* · موت *(ölüm)* · حيي *(diri olma, hayat)* · نشر *(yayma, açma; diriltme)* · "
 "bağ: xref خلق شىء خلق *(yarattı, şey, yarattı)* → **7:191 · 16:20**; ملكت نفس ضرّ *(mâlik oldu, "
 "nefis, zarar)* · نفس ضرّ نفع *(nefis, zarar, fayda)* → **10:49**; **25:2 ile karşıt çift** — "
 "orada ملك *(mülk; melik)* ve خلق *(yaratma)* olumlu ve tek özneye, burada aynı iki kök "
 "olumsuzlanmış ve çoğul özneye (elle, L1, aday 532)"),
4: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · RES 1 · "
 "CERT 1 · şahıs 3MS x6 · 3MP x4, iltifât 0 · n=16 mora=94 harf=71 (n z=0,38), fâsıla زُورًۭا "
 "*(yalan)* → ا, A sınıfı, ACC; i'râb NOM 3 · ACC 2; bab I x3 · IV x1 · VIII x1; **zaman PERF x5 "
 "— beş fiilin beşi de mâzi**; **biçim HASR + DIKKAT**; dış düğüm 0 · yıldız ★ yok · kökler قول "
 "*(söz söyleme)* · كفر *(inkâr, nankörlük)* · أفك *(iftira, uydurma (ifk); döndürülme)* · فري "
 "*(uydurma, iftira)* · عون *(yardım, destek)* · قوم *(kalkma; kavim; kıyamet)* · أخر *(geciktirme, "
 "sonraya bırakma)* · جيأ *(gelme)* · ظلم *(zulüm)* · زور *(yalan, uydurma)* · bağ: **25:5, 25:7, "
 "25:8 ile وَقَالُوا۟ *(dediler)* zinciri** — dört itiraz aynı fiille açılıyor (elle, L1, aday 533)"),
5: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3FS x3 · 3MP x2 · 3MS x2, iltifât 0 · n=9 mora=59 harf=49 (n z=-0,36), fâsıla أَصِيلًۭا "
 "*(akşamüstü)* → ا, A sınıfı, ACC; i'râb ACC 2 · NOM 1 · GEN 1; bab I x1 · IV x1 · VIII x1; zaman "
 "PERF x2 · IMPF x1; **edilgen 1 — تُمْلَىٰ *(okunuyor, yazdırılıyor)***, **pas z=1,57: yıldızın "
 "TEK kaynağı**; dış düğüm 0 · **yıldız ★** · kökler قول *(söz söyleme)* · سطر *(satır, yazma; "
 "esâtîr (masallar))* · أول *(ilk, evvel)* · كتب *(yazma, kitap)* · ملو *(uzun süre, mele; "
 "yazdırma (imlâ))* · بكر *(sabah erken)* · أصل *(kök, asıl; akşamüstü (asîl))* · bağ: **بكر "
 "*(sabah erken)* + أصل *(kök, asıl; akşamüstü (asîl))* çifti** — dikey ölçüm bu ikisini "
 "x278,9 ve x272,5 ile veriyor, korpusta sabit ikili"),
6: ("eksen: **lafız YOK · Rab YOK — fâil yine ٱلَّذِى *(o ki)* ile veriliyor**; **esmâ غَفُور "
 "*(bağışlayan)* 11. + رَحِيم *(merhamet eden)* 12. sırada = fâsıla — MÜHÜR; GEÇERLİ**: "
 "doğrudan zamir öznenin yüklemi, çift kapanış · aktör yok · edim emir, kip IMPV 1 · şahıs 3MS x5 · "
 "2MS x1, iltifât 0 · n=12 mora=68 harf=53 (n z=-0,04), fâsıla رَّحِيمًۭا *(merhamet eden)* → ا, "
 "A sınıfı, ACC; i'râb ACC 4 · GEN 2; bab I x3 · IV x1; zaman PERF x2 · IMPF x1 · IMPV 1; **dış "
 "düğüm 4 — blokta en yüksek** · yıldız ★ yok · kökler قول *(söz söyleme)* · نزل *(inme, indirme)* · "
 "علم *(bilme)* · سرر *(sır, gizleme)* · سمو *(ad; gök)* · أرض *(yer, yeryüzü)* · كون *(olmak)* · "
 "غفر *(bağışlama, mağfiret)* · رحم *(rahmet, merhamet)* · bağ: xref كان غفور رحيم *(bağışlayan ve "
 "merhamet eden oldu)* → **4:23 · 4:106 · 4:129 · 33:24**; **25:1 ile çift** — orada نَزَّلَ "
 "*(indirdi)* bab II, burada أَنزَلَ *(indirdi)* bab IV, aynı özne ve aynı nesne (elle, L1, aday 534)"),
7: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — ملك *(mülk; melik)* kökü burada "
 "مَلَك *(melek)* ve aktör tablosuna girmiyor · edim soru, kip INTG 1 · şahıs 3MS x6 · 3MP x2, "
 "iltifât 0 · n=16 mora=87 harf=74 (n z=0,38), fâsıla نَذِيرًا *(uyarıcı)* → ا, A sınıfı, ACC — "
 "**25:1'in fâsılasıyla aynı kelime**; i'râb ACC 3 · GEN 2 · NOM 1; bab I x4 · IV x1; zaman IMPF x3 · "
 "PERF x2; **edilgen 1 — أُنزِلَ *(indirilse)*** (pas z=0,81); **biçim DIKKAT**; dış düğüm 0 · "
 "yıldız ★ yok · kökler قول *(söz söyleme)* · رسل *(gönderme, elçi)* · أكل *(yeme)* · طعم "
 "*(yiyecek, yemek verme)* · مشي *(yürüme)* · سوق *(sürme, sevk etme; çarşı (sûk))* · نزل "
 "*(inme, indirme)* · ملك *(mülk; melik)* · كون *(olmak)* · نذر *(uyarma; adak)* · bağ: **25:20 "
 "ile bölüt ikizi** — يَأْكُلُ ٱلطَّعَامَ وَيَمْشِى فِى ٱلْأَسْوَاقِ *(yemek yiyor, çarşılarda "
 "dolaşıyor)* orada çoğul ve cevap kipinde (elle, L1, aday 535)"),
8: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adsız racül *(bir adam)* 16. sırada** · "
 "edim haber, kip NEG 1 · RES 1 · şahıs 3MS x5 · 3FS x2 · 2MP x2, iltifât 0 · n=17 mora=89 harf=68 "
 "(n z=0,49), fâsıla مَّسْحُورًا *(büyülenmiş)* → ا, A sınıfı, ACC; i'râb NOM 3 · ACC 2; bab I x3 · "
 "IV x1 · VIII x1; zaman IMPF x4 · PERF x1; **edilgen 1 — يُلْقَىٰ *(bırakılsa)*** (pas z=0,81); "
 "**biçim HASR**; simetri [3,1,5,1]; dış düğüm 1 · yıldız ★ yok · kökler لقي *(karşılaşma, kavuşma; "
 "atma)* · كنز *(hazine)* · كون *(olmak)* · جنن *(örtme, gizleme; cennet; cin)* · أكل *(yeme)* · "
 "قول *(söz söyleme)* · ظلم *(zulüm)* · تبع *(uyma, ardından gitme)* · رجل *(adam; yaya)* · سحر "
 "*(büyü, sihir)* · bağ: xref قال ظالم اتّبع *(dedi, zalim, uydu)* · ظالم اتّبع رجل *(zalim, uydu, "
 "adam)* · اتّبع رجل مسحور *(uydu, adam, büyülenmiş)* → **üçü de 17:47**; **17:47-48 ile ARDIŞIK "
 "BÖLÜT İKİZİ, 25:9 ile birlikte** (elle, L1, aday 530)"),
9: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir, kip IMPV 1 · NEG 1 · şahıs "
 "3MP x6 · 2MS x2, iltifât 0 · n=9 mora=49 harf=44 (n z=-0,36), fâsıla سَبِيلًۭا *(yol)* → ا, "
 "A sınıfı, ACC; i'râb ACC 2; bab I x3 · X x1; zaman PERF x2 · IMPV 1 · IMPF x1; dış düğüm 1 · "
 "yıldız ★ yok · kökler نظر *(bakma; mühlet verme)* · كيف *(nasıl, keyfiyet)* · ضرب *(vurma; mesel "
 "getirme)* · مثل *(benzer, mesel)* · ضلل *(sapma, saptırma)* · طوع *(güç yetirme, itaat)* · سبل "
 "*(yol)* · bağ: xref نظر كيف ضرب *(bak, nasıl, getirdiler)* · كيف ضرب مثل *(nasıl, getirdiler, "
 "mesel)* · ضرب مثل ضلّ *(getirdiler, mesel, saptılar)* · مثل ضلّ استطاع *(mesel, saptılar, güç "
 "yetirdiler)* · ضلّ استطاع سبيل *(saptılar, güç yetirdiler, yol)* → **BEŞ 3-gram, beşi de tek "
 "ayete: 17:48**; **ayet 17:48 ile BİREBİR ÖZDEŞ** (tek fark imlâ: ٱلْأَمْثَٰلَ / ٱلْأَمْثَالَ), "
 "ama defter.json esit alanı BOŞ — ölçü tanımı eksiği (elle, L1, aday 530)"),
10: ("eksen: **lafız YOK · Rab YOK — gönderge dördüncü kez ٱلَّذِى *(o ki)*, ve fiil 25:1'in "
 "fiiliyle aynı: تَبَارَكَ *(ne yücedir)*** · esmâ yok · aktör yok · edim şart, kip COND 1 · şahıs "
 "3MS x4 · 2MS x2 · 3FS x2, iltifât 0 · n=17 mora=84 harf=63 (n z=0,49), fâsıla قُصُورًۢا *(köşkler)* "
 "→ ا, A sınıfı, ACC; i'râb ACC 2 · GEN 2 · NOM 1; bab I x4 · VI x1; zaman PERF x3 · IMPF x2; "
 "**kök ikilemesi جعل *(kılma, var etme)* x2 — biri PERF biri IMPF**; simetri [3,2,8,1]; dış düğüm 0 · "
 "yıldız ★ yok · kökler برك *(bereket)* · شيأ *(dileme; şey)* · جعل *(kılma, var etme)* · خير "
 "*(hayır, daha iyi)* · جنن *(örtme, gizleme; cennet; cin)* · جري *(akma)* · تحت *(alt, altında)* · "
 "نهر *(ırmak)* · قصر *(köşk; kısaltma)* · bağ: **25:1 ile blok halkası** — aynı fiil تَبَارَكَ "
 "*(ne yücedir)* + aynı bağlaç ٱلَّذِى *(o ki)*; **25:8 ile karşıt çift** — orada istenen كَنز "
 "*(hazine)* ve جَنَّة *(bahçe)*, burada verilen جَنَّٰت *(bahçeler)* ve قُصُور *(köşkler)* "
 "(elle, L1, adaylar 528, 536)"),
}

MERCEK = {
1: ("Ayet bir adlandırma yapıyor ve adı BİR KEZ kullanıyor: ٱلْفُرْقَان *(Furkān)*, فرق "
 "*(ayırma, parçalara bölme)* kökünden; sûrede bir daha geçmiyor. Kök korpusta 72 geçişli, yani "
 "seyrek değil — seyrek olan sûre içindeki kullanımı. Yüklem نَزَّلَ *(indirdi)*, نزل *(inme, "
 "indirme)* kökü bab II; sûredeki sekiz نزل *(inme, indirme)* geçişinin ilki ve sûre bu kökü iki "
 "babda birden kullanıyor (II ve IV). Alıcı tekil ve belirli: عَبْدِهِۦ *(kulu)*, عبد *(kul, "
 "kulluk)*; kapsam çoğul ve belirli: لِلْعَٰلَمِينَ *(âlemlere)*. Ölçülebilir bir daralma-genişleme: "
 "iniş tek bir alıcıya, işlev bütün âlemlere. Fâsıla نَذِيرًا *(uyarıcı)* nekre — sûrenin yetmiş "
 "yedi ACC fâsılasının ilki."),
2: ("Ayet olumlu bir mülkiyet cümlesiyle açılıp İKİ olumsuzlamayla sürüyor, ikisi de لَمْ *(…medi)* "
 "ile ve ikisi de aynı alanda: وَلَدًۭا *(çocuk)* ve شَرِيكٌۭ *(ortak)*. ملك *(mülk; melik)* kökü "
 "ayeti çerçeveliyor — ilk kelimede مُلْكُ *(mülkü)* tamlama başı, ikinci kez ٱلْمُلْكِ *(mülkte)* "
 "marife; olumsuzlamanın kapsamı ilk cümlenin kapsamına eşitleniyor. Kapanış ikinci bir ikileme: "
 "فَقَدَّرَهُۥ تَقْدِيرًۭا *(ona ölçü biçti, bir ölçü biçme)* — قدر *(ölçü, güç yetirme)* kökü fiil "
 "ve mef'ûl-i mutlak olarak arka arkaya. Ayetin dört xref'inden üçü tek ayete (17:111) bağlanıyor "
 "ve bu, iki olumsuzlamanın ortak diziliminden geliyor."),
3: ("Ayet bir yetersizlik listesi kuruyor ve listeyi çift kutuplu terimlerle yapıyor: ضَرًّۭا "
 "*(zarar)* / نَفْعًۭا *(fayda)*, مَوْتًۭا *(ölüm)* / حَيَوٰةًۭ *(hayat)*, ve üçüncü terim çiftsiz: "
 "نُشُورًۭا *(diriliş)*. Ölçülebilir bir asimetri — iki karşıt çiftten sonra tek terim, ve o terim "
 "fâsıla. Olumsuzlama altı kez, hepsi لَا *(değil)*. İki kök 25:2'den birebir geri geliyor ve işareti "
 "değişiyor: خلق *(yaratma)* orada olumlu ve tek özneye, burada يَخْلُقُونَ *(yaratırlar)* olumsuz ve "
 "hemen ardından edilgen وَهُمْ يُخْلَقُونَ *(kendileri yaratılıyorlar)*; ملك *(mülk; melik)* orada "
 "mülkiyet, burada güç yetirme. Ayetin tek edilgeni tam da bu ters çevirmeyi taşıyor."),
4: ("İtiraz bir isnat cümlesi ve iki suç adıyla kapanıyor: ظُلْمًۭا *(zulüm)* ve زُورًۭا *(yalan)*. "
 "زور *(yalan, uydurma)* korpusta yalnız altı geçişli ve ikisi bu sûrede (25:4 ve 25:72) — dikey "
 "ölçüm bu kök için tek bir zenginleşme veriyor, قول *(söz söyleme)* x2,0, yani kök korpusta zaten "
 "söz fiiline bağlı. İki uydurma kökü arka arkaya kullanılıyor: إِفْكٌ *(ifk, yalan)* أفك *(iftira, "
 "uydurma (ifk); döndürülme)* ve ٱفْتَرَىٰهُ *(uydurdu)* فري *(uydurma, iftira)*; dikey ölçüm فري "
 "*(uydurma, iftira)* ▸önce ifk-yalan x37,7 veriyor — çift korpusta sabit, bu ayete özgü değil. "
 "Ve beş fiilin beşi de mâzi: itiraz tamamlanmış bir eylem olarak sunuluyor."),
5: ("Ayetin yıldızının tek kaynağı tek bir edilgen fiil: تُمْلَىٰ *(okunuyor)*, ملو *(uzun süre, "
 "mele; yazdırma (imlâ))*. Ölçülebilir bir zaman kayması: ٱكْتَتَبَهَا *(yazdırdı)* mâzi ve fâili "
 "belli, تُمْلَىٰ *(okunuyor)* muzâri ve fâili yok — itiraz geçmişten şimdiye geçerken özneyi "
 "düşürüyor. Zaman zarfı iki uçlu ve bitişik: بُكْرَةًۭ وَأَصِيلًۭا *(sabah ve akşam)*; korpusta bu "
 "çift sabit — dikey ölçüm بكر *(sabah erken)* ▸sonra akşam-vakti x278,9 ve أصل *(kök, asıl; "
 "akşamüstü (asîl))* ▸önce sabah-erken x272,5 veriyor, yani ikisi neredeyse yalnız birlikte "
 "geçiyor. سطر *(satır, yazma; esâtîr (masallar))* kökü korpusta 16 geçişli ve dikey ölçümü "
 "▸sonra evvel x49,7 veriyor: أَسَٰطِيرُ ٱلْأَوَّلِينَ *(öncekilerin masalları)* bir donmuş kalıp "
 "(aday 437 sınıfı — ayrım tanımı henüz yazılmadı)."),
6: ("Cevap tek cümlede iki şey yapıyor: fâili yeniden ٱلَّذِى *(o ki)* ile veriyor ve fâili bir "
 "bilme yüklemiyle niteliyor — يَعْلَمُ ٱلسِّرَّ *(sırrı bilir)*. Ölçülebilir bir kapsam: bilinen "
 "şey ٱلسِّرَّ *(sır)* tekil ve marife, kapsamı ise ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ *(gökler ve yer)*. "
 "سرر *(sır, gizleme)* kökü korpusta 44 geçişli ve dikey ölçüm ▸sonra علن *(açığa vurma, alenî)* "
 "x97,6 veriyor: kök korpusta karşıtıyla birlikte yaşıyor, burada karşıtı YOK — tek uçlu kullanım. "
 "Ve indirme fiili 25:1'den bab değiştirerek geri geliyor: orada نَزَّلَ *(indirdi)* bab II, burada "
 "أَنزَلَهُ *(onu indirdi)* bab IV, aynı özne ve aynı nesne. Kapanış sûrenin iki mühüründen ilki."),
7: ("İtiraz elçinin iki fiilini sayıyor ve ikisi de gündelik: يَأْكُلُ ٱلطَّعَامَ *(yemek yiyor)* ve "
 "يَمْشِى فِى ٱلْأَسْوَاقِ *(çarşılarda dolaşıyor)*. Ölçülebilir bir seyreklik: سوق *(sürme, sevk "
 "etme; çarşı (sûk))* korpusta 17 geçişli, مشي *(yürüme)* 23 — ikisi de seyrek kökler ve burada "
 "bitişik. İstenen alternatif de iki parçalı ve ikisi de inişle geliyor: مَلَكٌۭ *(melek)* ve "
 "نَذِيرًا *(uyarıcı)*; ikinci terim 25:1'in fâsılasının aynısı — orada indirilen kitabın işlevi, "
 "burada istenen ikinci kişi. Ayetin tek edilgeni أُنزِلَ *(indirilse)*, yani itiraz iniş fiilini "
 "kabul edip yalnız muhatabını değiştirmek istiyor."),
8: ("İstek listesi üç maddeye çıkıyor ve üçü de أَوْ *(yahut)* ile bağlanıyor: melek, كَنز "
 "*(hazine)*, جَنَّة *(bahçe)*. كنز *(hazine)* korpusta dokuz geçişli, dikey ölçümü eşiği aşan tek "
 "komşu vermiyor — kök korpusta belirgin bir kavram yatağına oturmuyor. Kapanış konuşanı "
 "değiştiriyor: ilk yarı adsız çoğul, ikinci yarı ٱلظَّٰلِمُونَ *(zalimler)* — aynı itirazın öznesi "
 "adlandırılıyor. Ve nitelenen kişi adsız bırakılıyor: رَجُلًۭا مَّسْحُورًا *(büyülenmiş bir adam)*, "
 "aktör tablosunda adsız racül *(bir adam)*. Ölçülebilir bir simetri: iki taraf da karşısındakini "
 "adsızlaştırıyor."),
9: ("Ayet bir bakma emriyle açılıyor ve emrin nesnesi bir ölçüm: كَيْفَ *(nasıl)*. نظر *(bakma; "
 "mühlet verme)* ve كيف *(nasıl, keyfiyet)* dikey ölçümde birbirini çağırıyor — نظر ▸sonra كيف "
 "x23,3, كيف ▸önce نظر x20,8; çift korpusta sabit, bu ayete özgü değil. Sonuç iki aşamalı ve ikisi "
 "de فَ *(ve böylece)* ile bağlı: فَضَلُّوا۟ *(saptılar)* mâzi, فَلَا يَسْتَطِيعُونَ *(güçleri "
 "yetmiyor)* muzâri — tamamlanmış bir eylem ve süregelen bir yetersizlik. Kapanış سَبِيلًۭا *(yol)* "
 "nekre; dikey ölçüm ضلل *(sapma, saptırma)* ▸sonra سبل *(yol)* x7,5 veriyor, yani sapma ile yol "
 "korpusta zaten komşu."),
10: ("Blok açıldığı fiille kapanıyor: تَبَارَكَ *(ne yücedir)*, برك *(bereket)* kökü, 25:1'deki "
 "biçimin aynısı ve yine ٱلَّذِى *(o ki)* ile devam ediyor. Ölçülebilir bir cevap yapısı: 25:8'in "
 "istek listesindeki iki madde burada karşılanıyor ve büyütülüyor — جَنَّة *(bahçe)* tekilken "
 "جَنَّٰتٍۢ *(bahçeler)* çoğul oluyor, كَنز *(hazine)* yerine قُصُورًۢا *(köşkler)* geliyor. قصر "
 "*(köşk; kısaltma)* korpusta 11 geçişli ve dikey ölçümü ▸sonra طرف *(uç, kenar)* x154,0 veriyor — "
 "seyrek kökün dar bir yatağı var. جعل *(kılma, var etme)* iki kez ve zaman değiştiriyor: جَعَلَ "
 "*(kıldı)* mâzi, وَيَجْعَل *(ve kılar)* meczum muzâri; şartın cevabı iki zamanda birden veriliyor."),
}

ATLAMA = {
 "_blok_notu_25_1_10": ("Blokta ★★★ AYET YOK — en yüksek yıldız 25:5'te ★ ve tek kaynağı tek bir "
  "edilgen fiil (pas z=1,57). Protokol gereği 🜁 biyolog ve 🜂 uzay mercekleri YAZILMADI: eşik "
  "★★★. Bilgi olarak kaydedilir — blokta çıpa taşıyabilecek tek öğe 25:10'un جَنَّٰت *(bahçeler)* "
  "ve أَنْهَٰر *(ırmaklar)* terkibidir, ama ayet bitki, su döngüsü ya da yer ölçüsü hakkında hiçbir "
  "şey söylemiyor; çıpa sayılmadı. Adaylar 468/512 için veri: bu blokta yıldız ile çıpa AYNI YÖNDE "
  "— ikisi de yok."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
OM['25'] = {"_makro": MAKRO, "_blok_bolme_notu": BOLME, "_mercek_atlama_notu": dict(ATLAMA)}
for n in range(1, 11):
    OM['25']["25:%d" % n] = {"ar": AR[(25, n)], "meal": MEAL[n], "olcum": OLCUM[n],
                             "mercek": MERCEK[n], "dikey": DIK["25:%d" % n]}
OM['ilerleme']['not'] = ("Sûre 23 TAM (118/118). Sûre 24 TAM (64/64). **Sûre 25 (Furkān) AÇILDI — "
                         "makro profil + 25:1-10.** Devam: 25:11'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "25": "1-10 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1655
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 25 →', len([k for k in OM['25'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK['25'] = {"25:%d" % n: MERCEK[n] for n in range(1, 11)}
MK['25_atlama'] = dict(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 25 →', len(MK['25']))
