# -*- coding: utf-8 -*-
"""blok_26_1_20.py — sûre 26 (Şuarâ) makro profili + ilk blok (26:1-20)."""
import json
DIK = json.load(open('blok_dikey_26_1_20.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']
AR[(26, 1)] = AR[(26, 1)].replace("بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ ", "")

MAKRO = {
 "ad": "ŞUARÂ",
 "ayet": 227, "kelime": 1318, "ort_kelime": 5.81,
 "tip": "Mekkî",
 "nuzul": "47 (BELLEKTEN; dosya GÜVENİLMEZ, kullanılmadı)",
 "eksen": ("**Allah lafzı 13 geçiş / 13 ayet (0,28x) · رَبّ *(Rab)* 36 geçiş (2,16x) · A/R = 0,36.** "
   "**A/R EKSENİNİN DÖRDÜNCÜ VERİ NOKTASI VE 'MEKKÎ 0,57' HİPOTEZİNİN İLK SINAVI — HİPOTEZ DÜŞTÜ:** "
   "sûre 23 (Mekkî) 0,57 · sûre 24 (Medenî) tanımsız · sûre 25 (Mekkî) 0,57 · sûre 26 (Mekkî) "
   "**0,36**. İki Mekkî sûrenin aynı oranı vermesi tekrarlanmadı. Ama A yoğunluğu yine düşük "
   "(0,28x, sûre 25'in 0,26x'ine yakın) ve **R yoğunluğu 2,16x — okumada görülen en yüksek**. "
   "Yani ayrışan A değil R. Lafızlı ayetler: 89, 93, 97, 108, 110, 126, 131, 144, 150, 163, 179, "
   "213, 227 — hepsi TEK token ve hepsi 89'dan SONRA; **ilk 88 ayette lafız SIFIR** (sûre 25'te "
   "ilk 16 ayetti). İlk رَبّ 26:9'da. (adaylar 470, 498, 525)"),
 "kafiye": ("**N sınıfı 222** (ن 193 · م 29) · **ل 4** · **ٓ 1** (26:1, hurûf-ı mukattaa). Saflık "
   "0,978, üç sınıf. Kırık 4: 26:17, 22, 59, 197. Sûre 25'in A/ACC kilidinden TAMAMEN FARKLI bir "
   "kafiye rejimi; ن ve م ayrı harf ama aynı sınıfta (N) toplanıyor — **sınıf tanımının denetlenmesi "
   "gerekiyor** (yeni)."),
 "esma": ("**51 token / 41 ayet / MÜHÜR 10** — okumada görülen en yüksek mühür sayısı. Dağılım: "
   "**مُؤْمِن *(mümin)* 15** · عَزِيز *(azîz)* 9 · رَحِيم *(rahîm)* 9 · مُبِين *(apaçık)* 6 · "
   "عَلِيم *(alîm)* 4 · كَرِيم *(kerîm)* 2 · رَحْمٰن *(rahmân)* · كَبِير *(büyük)* · آخِر *(sonraki)* · "
   "وارِث *(vâris)* · جَبّار *(cebbâr)* · سَمِيع *(işiten)* birer. **UYARI — مُؤْمِن'İN ON BEŞ "
   "TOKENİNİN ON BEŞİ DE ARTEFAKT**: hepsi مُؤْمِنِين *(müminler)*, yani İNSANLAR; okumada görülen "
   "en büyük tek artefakt bloğu (aday 601). Mühürlü on ayet (9, 68, 104, 122, 140, 159, 175, 191, "
   "217, 220) ve sekizi NAKARAT — عَزِيز|رَحِيم çifti."),
 "soz_edimi": "haber 151 · **emir 35 · soru 28** · şart 17 · yasak 4 · nida 2",
 "fig": "**HASR 17** · DIKKAT 5 · NEHY 4 · KELLA 2 · IDRAB 2 · **QASEM sıfır**",
 "dilbilgisi": ("i'râb ACC 205 · GEN 195 · NOM 173 — **ACC payı 0,358, sûre 25'in 0,596'sından çok "
   "düşük**; zaman PERF 167 · IMPF 128 · IMPV 47; bab I 218 · IV 57 · VIII 28 · II 26 · VII 4 · "
   "V 4 · X 3 · III 1 · VI 1; edilgen 14 fiil / 14 ayet; **iltifât 15 — okumada görülen en yüksek** "
   "(23'te 7, 24'te 0, 25'te 3). Yönler: 2>13 x4 · 1>3 x4 · 2>3 x3 · 3>2 x2 · 12>3 · 3>1 · 1>23."),
 "yildiz": {"0": 160, "1": 16, "2": 10, "3": 41},
 "yildiz3_sayi": 41,
 "yildiz3_kaynak": ("**rab tek başına 21 · allah tek başına 8 · pas 6 · hapaks 4 · hapaks+rab 1 · "
   "hapaks+pas 1.** YİRMİ DOKUZU EKSEN ORANINDAN GELİYOR. Sûrenin ayet başına ortalaması 5,81 "
   "kelime — okumada görülen en kısa; tek bir رَبّ tokeni beş kelimelik bir ayette oran 0,20 verip "
   "z=3,94 üretiyor (26:9), üç kelimelikte z=8,20 (26:26). **ADAY 583'ÜN (kısa ayet yanlılığı) "
   "DOĞRUDAN VE EN BÜYÜK KANITI** (aday 602)."),
 "hapaks": ("Altı ayette: 26:50 ضير *(zarar)* · 26:54 شرذم *(döküntü topluluk)* · 26:63 طود "
   "*(büyük dağ)* · 26:94 كبكب *(tepetaklak atma)* · 26:128 ريع *(yüksek yer, tepe)* · 26:149 فره "
   "*(ustalık, şımarıklık)*."),
 "esit": ("**44 ayet eşleşme taşıyor — sûre 25'te SIFIRDI.** Sûre içi nakarat kümeleri: "
   "(a) وَمَا كَانَ أَكْثَرُهُم مُّؤْمِنِينَ *(çoğu inanmıyor)* 6 ayet (8, 67, 103, 121, 174, 190); "
   "(b) وَإِنَّ رَبَّكَ لَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ *(Rabbin azîzdir, rahîmdir)* 8 ayet (9, 68, "
   "104, 122, 140, 159, 175, 191); (c) فَٱتَّقُوا۟ ٱللَّهَ وَأَطِيعُونِ *(Allah'tan sakının ve bana "
   "itaat edin)* 8 ayet (108, 110, 126, 131, 144, 150, 163, 179); (d) إِنِّى لَكُمْ رَسُولٌ أَمِينٌ "
   "*(ben size güvenilir bir elçiyim)* 5 ayet (107, 125, 143, 162, 178); (e) وَمَآ أَسْـَٔلُكُمْ "
   "عَلَيْهِ مِنْ أَجْرٍ *(sizden ücret istemiyorum)* 5 ayet (109, 127, 145, 164, 180). "
   "Sûre DIŞI: 26:2↔28:2 · 26:32-33↔7:107-108 · 26:47-48↔7:121-122 · 26:66↔37:82 · 26:147↔44:52 · "
   "26:153↔26:185. **NAKARAT ALANI 34 AYETTE DOLU** — okumada ilk kez nakarat yapısı bu ölçekte."),
 "aktor": ("Adlı: مُوسَى *(Mûsâ)* 8 · فِرْعَوْن *(Firavun)* 6 · إِسْرائِيل *(İsrâîl)* 4 · نُوح "
   "*(Nûh)* 3 · لُوط *(Lût)* 3 · هارُون *(Hârûn)* 2 · شَيْطان *(şeytan)* 2 · إِبْراهِيم *(İbrâhîm)* · "
   "جَنَّة *(cennet, bahçe)* · إِبْلِيس *(İblîs)* · عاد *(Âd)* · هُود *(Hûd)* · ثَمُود *(Semûd)* · "
   "صالِح *(Sâlih)* · شُعَيْب *(Şuayb)*. Adsız: ferîk *(bir bölük)* 1 — **sûre 25'in 'nefer' "
   "artefaktından sonra bu kayıt da okuma sırasında DENETLENECEK** (aday 579). "
   "AKTÖR YOĞUNLUĞU KARŞILAŞTIRMASI YAPILMAYACAK — aday 462."),
 "uzunluk": ("Ayet başına 5,81 kelime — **okumada görülen en kısa**. En uzun: 26:49 (n=21), 26:227 "
   "(n=19), 26:63 (n=13). En kısa: 26:1 (n=1, طسم), 26:60, 26:134, 26:204 (n=2)."),
}

MEAL = {
1: "Tâ, Sîn, Mîm.",
2: "Bunlar apaçık kitabın âyetleridir.",
3: "Mümin olmuyorlar diye neredeyse kendini helâk edeceksin.",
4: "Dilesek onlara gökten bir âyet indiririz de boyunları ona eğilip kalır.",
5: "Rahmân'dan kendilerine yeni bir zikir gelmeye görsün, ondan mutlaka yüz çevirirler.",
6: "Yalanladılar; alay ettikleri şeyin haberleri onlara gelecek.",
7: "Yeryüzüne bakmadılar mı — orada her güzel çiftten nicesini bitirdik.",
8: "Bunda elbette bir âyet var; ama onların çoğu inanmıyor.",
9: "Rabbin, elbette o Azîz'dir, Rahîm'dir.",
10: "Hani Rabbin Mûsâ'ya seslenmişti: Zalim topluluğa git.",
11: "Firavun'un kavmine. Sakınmıyorlar mı?",
12: "Dedi ki: Rabbim, beni yalanlamalarından korkuyorum.",
13: "Göğsüm daralır, dilim çözülmez; Hârûn'a da gönder.",
14: "Üstelik onların bana yükledikleri bir suç var; beni öldürmelerinden korkuyorum.",
15: "Buyurdu ki: Hayır. İkiniz âyetlerimizle gidin; biz sizinle beraber işitenleriz.",
16: "Firavun'a varın ve deyin ki: Biz âlemlerin Rabbinin elçisiyiz.",
17: "İsrâiloğullarını bizimle gönder.",
18: "Dedi ki: Seni çocukken içimizde yetiştirmedik mi? Ömrünün yıllarını aramızda geçirmedin mi?",
19: "Ve yapacağını yaptın; sen nankörlerdensin.",
20: "Dedi ki: Onu yaptığımda ben sapkınlardandım.",
}

OLCUM = {
1: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "eki YOK, fiil YOK, i'râb YOK, kök YOK** · n=1 mora=14 harf=22 — **okumada görülen en kısa ayet** "
 "(n z=-1,21), **fâsıla طسٓمٓ *(tâ-sîn-mîm)* → ٓ sınıfı; sûrenin ve okumanın TEK ٓ fâsılası**; dış "
 "düğüm 0 · yıldız ★ yok · **KÖK YOK — bu yüzden ▽ DİKEY OKUMA SATIRI YAZILAMAZ** (protokol: "
 "komşuluk zenginleşmesi olmadan ▽ yazılamaz); bağ: hurûf-ı mukattaa, sûrenin açılışı"),
2: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُبِين *(apaçık)* 4. sırada = fâsıla, MÜHÜRSÜZ — "
 "ÖLÇÜM ARTEFAKTI**: gönderge ٱلْكِتَٰب *(kitap)*, sıfat kitabın; ölçüt (a) dışlıyor · aktör yok · "
 "edim haber · şahıs eki yok · n=4 mora=24 harf=18 (n z=-0,89), fâsıla ٱلْمُبِينِ *(apaçık)* → ن, "
 "N sınıfı; i'râb GEN 2 · NOM 1; **fiil yok**; **dış düğüm 2** · yıldız ★ yok · **esit: 28:2 ile "
 "TAM AYET ÖZDEŞ** · kökler أيي *(âyet, işaret)* · كتب *(yazma, kitap)* · بين *(arası; açıklama; "
 "beyan)* · bağ: xref آية *(âyet)* + كتاب *(kitap)* + مبين *(apaçık)* → **12:1 · 28:2**"),
3: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُؤْمِن *(mümin)* 6. sırada = fâsıla, MÜHÜRSÜZ — "
 "ÖLÇÜM ARTEFAKTI**: مُؤْمِنِينَ *(müminler)* çoğul ve gönderge İNSANLAR; **sûrenin on beş مُؤْمِن "
 "tokeninin ilki ve on beşi de aynı sınıftan** (aday 601) · aktör yok · edim haber, kip NEG 1 · "
 "şahıs 2MS x2 · 3MP x2, iltifât 0 · n=6 mora=36 harf=28 (n z=-0,68), fâsıla مُؤْمِنِينَ → ن, N "
 "sınıfı; i'râb ACC 3 · NOM 1; bab I x1; zaman IMPF x1; dış düğüm 0 · yıldız ★ yok · kökler بخع "
 "*(kendini helâk etme, üzüntüden tüketme)* · نفس *(nefis, can)* · كون *(olmak; mekân, yer)* · أمن "
 "*(güven, iman)* · bağ: **بخع *(kendini helâk etme)* korpusta İKİ geçişli** (18:6, 26:3), ikisi de "
 "aynı yapıda"),
4: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim şart, kip COND 1 · şahıs 1P x2 · "
 "3MP x2 · 3FS x2, iltifât 0 · n=11 mora=60 harf=45 (n z=-0,15), fâsıla خَٰضِعِينَ *(boyun eğenler)* "
 "→ ن, N sınıfı; i'râb ACC 2 · GEN 1 · NOM 1; bab I x2 · II x1; zaman IMPF x2 · PERF x1; dış düğüm "
 "0 · yıldız ★ yok · kökler شيأ *(dileme; şey)* · نزل *(inme, indirme)* · سمو *(ad; gök)* · أيي "
 "*(âyet, işaret)* · ظلل *(gölge; süregelme)* · عنق *(boyun)* · خضع *(boyun eğme, eğilme)* · bağ: "
 "**25:21 ile aynı istek, ters yön** — orada itirazcılar gökten melek indirilmesini İSTİYORDU, "
 "burada gökten âyet indirilmesi gerçekleşmemiş bir ALTERNATİF olarak veriliyor (elle, L1, aday 603)"),
5: ("eksen: **lafız YOK · Rab YOK** · **esmâ رَحْمٰن *(rahmân)* 6. sırada, ORTA konum, MÜHÜRSÜZ — "
 "sûrenin TEK رَحْمٰن'ı**; burada مِّنَ ٱلرَّحْمٰنِ *(Rahmân'dan)* mecrur ve KAYNAK konumunda, yani "
 "yine GÖNDERGE (aday 578 sınıfı, sûre 25'in beş vakasıyla aynı) · aktör yok · edim haber, kip NEG 1 · "
 "RES 1 · şahıs 3MS x2 · 3MP x3, iltifât 0 · n=11 mora=57 harf=45 (n z=-0,15), fâsıla مُعْرِضِينَ "
 "*(yüz çevirenler)* → ن, N sınıfı; i'râb GEN 3 · ACC 1; bab I x2; zaman IMPF x1 · PERF x1; **biçim "
 "HASR**; simetri [3,1,8,1]; dış düğüm 0 · yıldız ★ yok · kökler أتي *(gelme, getirme)* · ذكر *(anma, "
 "zikir)* · رحم *(rahmet, merhamet)* · حدث *(yeni olma, hadis)* · كون *(olmak; mekân, yer)* · عرض "
 "*(yüz çevirme; genişlik)* · bağ: **25:60 ile رَحْمٰن karşılaştırması** — orada itirazcılar adı "
 "TANIMIYORDU (وَمَا ٱلرَّحْمَٰنُ *(Rahmân da ne)*), burada adı tanıyorlar ama zikirden yüz "
 "çeviriyorlar (elle, L1, aday 604)"),
6: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip CERT 1 · FUT 1 · şahıs "
 "3MP x7 · 3MS x2, iltifât 0 · n=8 mora=47 harf=43 (n z=-0,47), fâsıla يَسْتَهْزِءُونَ *(alay "
 "ediyorlar)* → ن, N sınıfı; i'râb NOM 1; bab I x2 · II x1 · X x1; zaman PERF x2 · IMPF x2; dış "
 "düğüm 1 · yıldız ★ yok · kökler كذب *(yalan; yalanlama)* · أتي *(gelme, getirme)* · نبأ *(haber; "
 "nebî)* · كون *(olmak; mekân, yer)* · هزأ *(alay etme)* · bağ: xref أتى *(geldi)* + نبأ *(haber)* + "
 "كان *(oldu)* ve نبأ + كان + استهزئ *(alay edildi)* → **ikisi de 6:5**; **25:41 ile هزأ *(alay "
 "etme)* ikinci karşılaşması** — orada alay elçiye, burada alay 'şey'e yöneliyor"),
7: ("eksen: **lafız YOK · Rab YOK** · **esmâ كَرِيم *(kerîm)* 11. sırada = fâsıla, MÜHÜRSÜZ — "
 "ÖLÇÜM ARTEFAKTI**: gönderge زَوْج *(çift, tür)*, yani BİTKİ; ölçüt (a) dışlıyor · aktör yok · "
 "edim soru, kip INTG 1 · NEG 1 · şahıs 3MP x2 · 1P x2 · 3FS x1, iltifât 0 · n=11 mora=48 harf=42 "
 "(n z=-0,15), fâsıla كَرِيمٍ *(güzel, değerli)* → م, N sınıfı; **i'râb GEN 4 · ACC 1**; bab I x1 · "
 "IV x1; zaman IMPF x1 · PERF x1; **açık sayı sözcüğü: زوج *(eş, çift)* → زَوْج**; simetri [3,1,5,1]; "
 "dış düğüm 1 · yıldız ★ yok · kökler رأي *(görme)* · أرض *(yer, yeryüzü)* · نبت *(bitki, bitirme)* · "
 "كلل *(hep, bütün)* · زوج *(eş, çift)* · كرم *(kerem, onur)* · bağ: xref كلّ *(her)* + زوج *(çift)* + "
 "كريم *(güzel)* → **31:10**; **25:45 ile أَلَمْ يَرَوْا۟ / أَلَمْ تَرَ *(görmediler mi / görmedin "
 "mi)* çağrısı** — orada tekil muhataba ve gölgeye, burada çoğul muhataba ve bitkiye (elle, L1, "
 "aday 605)"),
8: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُؤْمِن *(mümin)* 8. sırada = fâsıla — ARTEFAKT, "
 "ikinci kez** · aktör yok · edim haber, kip EMPH 1 · NEG 1 · şahıs 3MS x1 · 3MP x1, iltifât 0 · "
 "n=8 mora=40 harf=32 (n z=-0,47), fâsıla مُّؤْمِنِينَ → ن, N sınıfı; i'râb ACC 3 · NOM 1; bab I x1; "
 "zaman PERF x1; **açık sayı sözcüğü: كثر *(çokluk)* → أَكْثَر *(çoğu)***; **NAKARAT alanı = 6** "
 "(sûre içi altı ayette birebir); **esit: 26:67, 103, 121, 174, 190 ile TAM AYET ÖZDEŞ** · dış düğüm "
 "0 · yıldız ★ yok · kökler أيي *(âyet, işaret)* · كون *(olmak; mekân, yer)* · كثر *(çokluk)* · "
 "أمن *(güven, iman)* · bağ: **sûrenin birinci nakaratı — kıssa dizisinin kapanış formülü** "
 "(elle, L1, aday 606)"),
9: ("eksen: **lafız YOK · رَبّ *(Rab)* 2. sırada — SÛRENİN İLK Rab'bi**, **rab z=3,94: yıldızın "
 "TEK kaynağı** (beş kelimede bir Rab, oran 0,20 — sûre 25'teki 25:64 ile AYNI DEĞER) · **esmâ "
 "عَزِيز *(azîz)* 4. + رَحِيم *(rahîm)* 5. sırada = fâsıla — MÜHÜR; GEÇERLİ; sûrenin on mühründen "
 "ilki** · aktör yok · edim haber, kip EMPH 1 · şahıs 2MS x1 · 3MS x1, iltifât 0 · n=5 mora=28 "
 "harf=21 (n z=-0,79), fâsıla ٱلرَّحِيمُ *(rahîm)* → م, N sınıfı; **i'râb ACC 2 · NOM 2; fiil YOK**; "
 "**NAKARAT alanı = 8**; **esit: 26:68, 104, 122, 140, 159, 175, 191 ile TAM AYET ÖZDEŞ** · dış "
 "düğüm 0 · **yıldız ★★★ — sûrenin ilk üç yıldızlısı** · kökler ربب *(rab, terbiye etme)* · عزز "
 "*(izzet, üstünlük)* · رحم *(rahmet, merhamet)* · bağ: **sûrenin ikinci nakaratı; birinciyle "
 "(26:8) BİTİŞİK ÇİFT oluşturuyor ve çift sekiz kez tekrarlanıyor** (elle, L1, aday 606)"),
10: ("eksen: **lafız YOK · رَبّ *(Rab)* 3. sırada — ikinci Rab** (rab z=2,34: yıldızın TEK kaynağı) · "
 "esmâ yok · **aktör: adlı مُوسَى *(Mûsâ)* 4. sırada, rol MEF'ÛL — sûrenin ilk adlı aktörü** · edim "
 "emir, kip IMPV 1 · şahıs 3MS x1 · 2MS x2, iltifât 0 · n=8 mora=42 harf=31 (n z=-0,47), fâsıla "
 "ٱلظَّٰلِمِينَ *(zalimler)* → ن, N sınıfı; i'râb NOM 2 · ACC 2; bab I x1 · III x1; zaman PERF x1 · "
 "IMPV 1; dış düğüm 0 · **yıldız ★★** · kökler ندي *(seslenme, nidâ)* · ربب *(rab, terbiye etme)* · "
 "أتي *(gelme, getirme)* · قوم *(kalkma; kavim; kıyamet)* · ظلم *(zulüm)* · bağ: **25:36 ile aynı "
 "görevlendirme** — orada فَقُلْنَا ٱذْهَبَآ إِلَى ٱلْقَوْمِ ٱلَّذِينَ كَذَّبُوا۟ *(dedik ki: "
 "yalanlayan topluluğa gidin)*, burada ٱئْتِ ٱلْقَوْمَ ٱلظَّٰلِمِينَ *(zalim topluluğa git)*; "
 "orada İKİL emir, burada TEKİL (elle, L1, aday 607)"),
11: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı فِرْعَوْن *(Firavun)* 2. sırada, "
 "rol MEF'ÛL** · edim soru, kip INTG 1 · NEG 1 · şahıs 3MP x2, iltifât 0 · n=4 mora=21 harf=17 "
 "(n z=-0,89), fâsıla يَتَّقُونَ *(sakınırlar)* → ن, N sınıfı; **i'râb ACC 2**; bab VIII x1; zaman "
 "IMPF x1; dış düğüm 0 · yıldız ★ yok · kökler قوم *(kalkma; kavim; kıyamet)* · وقي *(sakınma, "
 "koruma)* · bağ: **26:10 ile bitişik çift** — 26:10'da 'zalim topluluk' NİTELİKLE, burada "
 "'Firavun'un kavmi' ADLA veriliyor: aynı gönderge, iki adlandırma katmanı (elle, L1, aday 607)"),
12: ("eksen: **lafız YOK · رَبّ *(Rab)* 2. sırada — üçüncü Rab, ve İLK NİDA HÂLİNDE (رَبِّ "
 "*(Rabbim)*)**, **rab z=3,23: yıldızın TEK kaynağı** · esmâ yok · aktör yok · edim haber, kip "
 "işareti yok · **şahıs 1S x4 · 3MP x2 · 3MS x1**, iltifât 0 · n=6 mora=31 harf=20 (n z=-0,68), "
 "fâsıla يُكَذِّبُونِ *(beni yalanlarlar)* → ن, N sınıfı; i'râb NOM 1 · ACC 1; bab I x2 · II x1; "
 "zaman PERF x1 · IMPF x2; dış düğüm 1 · **yıldız ★★★** · kökler قول *(söz söyleme)* · ربب *(rab, "
 "terbiye etme)* · خوف *(korku)* · كذب *(yalan; yalanlama)* · bağ: xref قال *(dedi)* + ربّ *(Rab)* + "
 "خاف *(korktu)* → **20:45**; **25:30 ile karşılaştırma** — orada elçi يَٰرَبِّ *(Rabbim)* diye "
 "kavminin Kur'ân'ı terk etmesinden ŞİKÂYET ediyordu, burada رَبِّ diye yalanlanmaktan KORKUYOR "
 "(elle, L1, aday 608)"),
13: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı هارُون *(Hârûn)* 8. sırada, rol "
 "mecrur** · edim emir, kip NEG 1 · IMPV 1 · şahıs 3MS x2 · 1S x2 · 2MS x1, iltifât 0 · n=8 mora=42 "
 "harf=34 (n z=-0,47), fâsıla هَٰرُونَ *(Hârûn)* → ن, N sınıfı — **fâsıla bir ÖZEL AD**; i'râb "
 "NOM 2 · GEN 1; bab I x1 · IV x1 · VII x1; zaman IMPF x2 · IMPV 1; dış düğüm 0 · yıldız ★ yok · "
 "kökler ضيق *(darlık)* · صدر *(göğüs; ayrılma)* · طلق *(salıverme, boşama)* · لسن *(dil, lisan)* · "
 "رسل *(gönderme, elçi)* · bağ: **25:13 ile ضيق *(darlık)* ikinci karşılaşması** — orada مَكَانا "
 "ضَيِّقا *(dar bir yer)* fiziksel, burada يَضِيقُ صَدْرِى *(göğsüm daralır)* içsel (elle, L1, "
 "aday 609)"),
14: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3MP x3 · 1S x3, iltifât 0 · n=6 mora=29 harf=25 (n z=-0,68), fâsıla يَقْتُلُونِ *(beni "
 "öldürürler)* → ن, N sınıfı; i'râb NOM 1; bab I x2; zaman IMPF x2; dış düğüm 0 · yıldız ★ yok · "
 "kökler ذنب *(günah, suç)* · خوف *(korku)* · قتل *(öldürme)* · bağ: **26:12 ile korku çifti** — "
 "iki ayette de أَخَافُ *(korkuyorum)* ve iki ayette de fâsıla ـُونِ ekiyle bitiyor "
 "(يُكَذِّبُونِ / يَقْتُلُونِ): **aynı ek, aynı kip, iki korku** (elle, L1, aday 610)"),
15: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir, kip IMPV 1 · **şahıs 2MD x1 · "
 "2D x1 · 1P x2 · 3MS x1 · 2MP x1 — okumada ikinci kez tesniye emir** (birincisi 25:36), iltifât 0 · "
 "n=7 mora=47 harf=35 (n z=-0,58), fâsıla مُّسْتَمِعُونَ *(işitenler)* → ن, N sınıfı; i'râb ACC 2 · "
 "GEN 1 · NOM 1; bab I x2; zaman PERF x1 · IMPV 1; **biçim KELLA** — sûrenin iki KELLA'sından ilki; "
 "dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · ذهب *(gitme; altın)* · أيي *(âyet, "
 "işaret)* · سمع *(işitme)* · bağ: **25:36 ile ikil emir karşılaştırması** — ikisinde de ٱذْهَبَا "
 "*(ikiniz gidin)*, orada helâk hemen ardından geliyordu, burada eşlik vaadi geliyor "
 "(elle, L1, aday 607)"),
16: ("eksen: **lafız YOK · رَبّ *(Rab)* 6. sırada — dördüncü Rab** (rab z=2,72: yıldızın TEK "
 "kaynağı) · esmâ yok · **aktör: adlı فِرْعَوْن *(Firavun)* 2. sırada, rol MEF'ÛL** · edim emir, "
 "kip IMPV 2 · **şahıs 2MD x1 · 2D x3 · 1P x1**, iltifât 0 · n=7 mora=44 harf=31 (n z=-0,58), "
 "fâsıla ٱلْعَٰلَمِينَ *(âlemler)* → ن, N sınıfı; i'râb ACC 2 · GEN 2 · NOM 1; bab I x2; zaman "
 "IMPV 2; **dış düğüm 5 — blokta en yüksek** · **yıldız ★★** · kökler أتي *(gelme, getirme)* · قول "
 "*(söz söyleme)* · رسل *(gönderme, elçi)* · ربب *(rab, terbiye etme)* · علم *(bilme; âlem)* · bağ: "
 "xref رسول *(elçi)* + ربّ *(Rab)* + عالم *(âlem)* → **7:61 · 7:67 · 7:104 · 43:46**; أتى *(geldi)* + "
 "قال *(dedi)* + رسول *(elçi)* → **20:47**; **25:1 ile عالمين *(âlemler)* ikinci karşılaşması** — "
 "orada indirilen kitap âlemlere UYARICI, burada elçi âlemlerin RABBİNDEN (elle, L1, aday 611)"),
17: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı إِسْرائِيل *(İsrâîl)* 5. sırada, "
 "rol mecrur** · edim emir, kip IMPV 1 · şahıs 2MS x1 · 1P x1, iltifât 0 · n=5 mora=29 harf=19 "
 "(n z=-0,79), **fâsıla إِسْرَٰٓءِيلَ *(İsrâîl)* → ل — SÛRENİN DÖRT KAFİYE KIRILMASINDAN İLKİ** "
 "(kafiye_kirik=1; yıldızın TEK kaynağı); i'râb ACC 1 · NOM 1 · GEN 1; bab IV x1; zaman IMPV 1; dış "
 "düğüm 0 · **yıldız ★** · kökler رسل *(gönderme, elçi)* · بني *(oğul, evlat)* · bağ: **kırılan "
 "fâsıla bir ÖZEL AD** — 26:13'ün هَٰرُونَ fâsılası da özel ad ama o ن ile bitip sınıfa uyuyor; "
 "burada ad kafiyeyi kırıyor (elle, L1, aday 612)"),
18: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · NEG 1 · şahıs "
 "2MS x4 · 1P x3 · 3MS x1, iltifât 0 · n=10 mora=50 harf=39 (n z=-0,26), fâsıla سِنِينَ *(yıllar)* "
 "→ ن, N sınıfı; i'râb ACC 2 · GEN 1; bab I x2 · II x1; zaman PERF x2 · IMPF x1; dış düğüm 0 · "
 "yıldız ★ yok · kökler قول *(söz söyleme)* · ربو *(yetiştirme, büyütme; ribâ)* · ولد *(doğurma, "
 "çocuk)* · لبث *(kalma, durma)* · عمر *(ömür, yaşam)* · سنو *(yıl)* · bağ: **ربو *(yetiştirme)* ve "
 "ربب *(rab, terbiye etme)* — İKİ AYRI KÖK, AYNI ANLAM ALANI**: 26:16'da elçi رَبّ ٱلْعَٰلَمِينَ "
 "*(âlemlerin Rabbi)* diyor, 26:18'de Firavun نُرَبِّكَ *(seni yetiştirdik)* diyor; iki kök "
 "korpusta ayrı ama terbiye alanında karşı karşıya (elle, L1, aday 613)"),
19: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "2MS x6 — ayette başka şahıs yok**, iltifât 0 · n=7 mora=36 harf=31 (n z=-0,58), fâsıla "
 "ٱلْكَٰفِرِينَ *(nankörler)* → ن, N sınıfı; i'râb NOM 1 · GEN 1; bab I x2; zaman PERF x2; **kök "
 "ikilemesi فعل *(yapma, işleme)* x3 — sûrede bir ayette aynı kökün üç kez geçtiği ilk yer** "
 "(فَعَلْتَ · فَعْلَتَكَ · … ); simetri [3,1,4,1]; dış düğüm 0 · yıldız ★ yok · kökler فعل *(yapma, "
 "işleme)* · كفر *(inkâr, nankörlük)* · bağ: **25:71 ile karşılaştırma** — orada توب *(tövbe, "
 "dönüş)* üç kez ve OLUMLU, burada فعل *(yapma, işleme)* üç kez ve SUÇLAMA (elle, L1, aday 614)"),
20: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3MS x1 · 1S x3 · 3FS x1, **iltifât 1 — yön 2>13; SÛRENİN İLK İLTİFÂTI** · n=6 mora=40 harf=27 "
 "(n z=-0,68), fâsıla ٱلضَّآلِّينَ *(sapkınlar)* → ن, N sınıfı; i'râb GEN 1; bab I x2; zaman PERF "
 "x2; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · فعل *(yapma, işleme)* · ضلل *(sapma, "
 "saptırma)* · bağ: **26:19 ile bitişik çift** — Firavun'un فَعَلْتَ *(yaptın)* suçlaması ve "
 "Mûsâ'nın فَعَلْتُهَآ *(onu yaptım)* kabulü; aynı kök, suçlamadan itirafa (elle, L1, aday 614)"),
}

MERCEK = {
1: ("Bir kelimelik ayet ve o kelime bir kök taşımıyor: طسٓمٓ *(tâ-sîn-mîm)*. Ölçülebilir üç "
 "boşluk: fiil yok, i'râb yok, şahıs eki yok. n=1 ile okumada görülen en kısa ayet (n z=-1,21) ve "
 "fâsılası sûrenin tek ٓ sınıfı. **Bu, ▽ satırının yazılamadığı ilk ayet** — protokol komşuluk "
 "zenginleşmesi olmadan ▽ yazılmasını yasaklıyor ve burada zenginleşme hesaplanacak kök yok. "
 "Ölçüm katmanının kendisi bu ayette büyük ölçüde boş kalıyor; bu bir eksiklik değil, metnin "
 "biçiminin ölçüm biçimine yansıması."),
2: ("Dört kelime ve hiç fiil yok. Ölçülebilir bir özdeşlik: ayet 28:2 ile TAM AYET ÖZDEŞ ve "
 "defter.json esit alanı bunu YAKALIYOR — sûre 25'te esit alanı sûre boyunca boştu (aday 596), "
 "burada ilk ayetten itibaren dolu. Sûre 26 esit bakımından sûre 25'in tam karşıtı: 44 ayet "
 "eşleşme taşıyor. Ve fâsıla bir esmâ sayılıyor: ٱلْمُبِينِ *(apaçık)* — oysa gönderge ٱلْكِتَٰب "
 "*(kitap)*; sûrenin ilk esmâ artefaktı, daha ikinci ayette."),
3: ("Ayet bir aşırılık ölçüyor: لَعَلَّكَ بَٰخِعٌۭ نَّفْسَكَ *(neredeyse kendini helâk edeceksin)*. "
 "بخع *(kendini helâk etme, üzüntüden tüketme)* korpusta İKİ geçişli (18:6 ve burada) ve ikisi de "
 "aynı yapıda — kök korpusta yalnız bu kalıpla var, donmuş kalıp adayı (aday 437). Ve fâsıla "
 "مُؤْمِنِينَ *(müminler)* esmâ sayılmış: sûrenin on beş مُؤْمِن tokeninin ilki, ve on beşinin de "
 "göndergesi insanlar. Okumada görülen en büyük tek artefakt bloğu burada başlıyor."),
4: ("Şart gerçekleşmemiş bir alternatif kuruyor ve sonucu bedensel: فَظَلَّتْ أَعْنَٰقُهُمْ لَهَا "
 "خَٰضِعِينَ *(boyunları ona eğilip kalır)*. عنق *(boyun)* korpusta 8 geçişli, خضع *(boyun eğme, "
 "eğilme)* 3 geçişli — ikisi de seyrek ve burada bitişik. Ölçülebilir bir karşıtlık: 25:21'de "
 "itirazcılar gökten MELEK indirilmesini istiyordu ve istek reddedilmiyordu; burada gökten ÂYET "
 "indirilmesi gerçekleşmemiş bir alternatif ve sonucu zorlama bir teslimiyet. İki sûre aynı isteği "
 "iki ayrı yönden ele alıyor."),
5: ("Sûrenin tek رَحْمٰن *(rahmân)*'ı burada ve yine gönderge konumunda — مِّنَ ٱلرَّحْمٰنِ "
 "*(Rahmân'dan)*, kaynak. Sûre 25'in beş vakasıyla aynı sınıf (aday 578). Ölçülebilir bir "
 "karşılaştırma: 25:60'ta itirazcılar adı TANIMIYORDU (وَمَا ٱلرَّحْمَٰنُ *(Rahmân da ne)*), burada "
 "tanıma sorunu yok — sorun zikre yüz çevirmek. حدث *(yeni olma, hadis)* kökü burada 'yeni' "
 "anlamında ve korpusta 36 geçişli; dikey ölçümü ▸önce zikir bağlamı veriyor. Ve HASR ile "
 "sınırlama: إِلَّا كَانُوا۟ عَنْهُ مُعْرِضِينَ *(mutlaka ondan yüz çevirirler)*."),
6: ("İki fiil karşı karşıya ve ikisi de aynı özneye: فَقَدْ كَذَّبُوا۟ *(yalanladılar)* mâzi ve "
 "يَسْتَهْزِءُونَ *(alay ediyorlar)* muzâri. Ölçülebilir bir zaman yapısı: tamamlanmış tekzip ve "
 "süregelen alay. Aradaki cümle geleceğe atıyor: فَسَيَأْتِيهِمْ أَنۢبَٰٓؤُا۟ *(haberleri "
 "gelecek)* — üç zaman katmanı sekiz kelimede. İki xref'in de aynı ayete (6:5) düşmesi terkibin "
 "korpusta sabit olduğunu gösteriyor. هزأ *(alay etme)* sûre 25'te de vardı (25:41) ama orada "
 "nesne elçiydi, burada 'şey'."),
7: ("Bakma çağrısı sûre 25'in üç çağrısından sonra dördüncü kez ve ilk kez BİTKİYE: أَوَلَمْ "
 "يَرَوْا۟ إِلَى ٱلْأَرْضِ كَمْ أَنۢبَتْنَا فِيهَا *(yeryüzüne bakmadılar mı, orada nicesini "
 "bitirdik)*. 25:45'te أَلَمْ تَرَ *(görmedin mi)* tekil muhataba ve gölgeye yöneltilmişti; burada "
 "çoğul muhataba. Ölçülebilir bir sayı işareti: كَمْ *(nice)* — belirsiz çokluk. نبت *(bitki, "
 "bitirme)* korpusta 26 geçişli ve dikey ölçümü ▸önce su bağlamı veriyor; burada su YOK. SINIR: "
 "ayet bitki çeşitliliğini bir SAYIYLA değil bir sıfatla veriyor (زَوْجٍۢ كَرِيمٍ *(güzel çift)*) "
 "ve ne mekanizma ne ölçü söylüyor."),
8: ("Sûrenin birinci nakaratı burada başlıyor: وَمَا كَانَ أَكْثَرُهُم مُّؤْمِنِينَ *(çoğu "
 "inanmıyor)* — altı ayette birebir aynı (26:8, 67, 103, 121, 174, 190). Ölçülebilir bir yapı: "
 "nakarat alanı 6, esit alanı beş ayeti gösteriyor. Sûre 25'te nakarat alanı sûre boyunca SIFIRDI; "
 "burada 34 ayet dolu. Ve bu nakarat bir sonrakiyle (26:9) BİTİŞİK ÇİFT oluşturuyor: 'çoğu inanmadı' "
 "+ 'Rabbin azîzdir, rahîmdir'. Çift sekiz kıssanın kapanışında tekrarlanıyor — okumada ilk kez bu "
 "ölçekte bir yapı."),
9: ("Beş kelime, hiç fiil yok, ve okumada ikinci kez rab z=3,94 (birincisi 25:64 — aynı değer, aynı "
 "sebep: n=5 ve tek Rab, oran 0,20). Yıldızın tek kaynağı bu. Ölçülebilir bir mühür: عَزِيز|رَحِيم "
 "*(azîz | rahîm)* çifti ve sûrenin on mühründen ilki; sûre 25'in iki mührü غَفُور|رَحِيم idi — "
 "ikinci ad aynı, birinci ad farklı. عزز *(izzet, üstünlük)* korpusta 119 geçişli ve dikey ölçümü "
 "▸sonra rahmet bağlamı veriyor: çift korpusta sabit, bu sûreye özgü değil. Ayet 26:68, 104, 122, "
 "140, 159, 175, 191 ile TAM ÖZDEŞ."),
10: ("Kıssa dizisi bir nidâ ile açılıyor: نَادَىٰ رَبُّكَ مُوسَىٰٓ *(Rabbin Mûsâ'ya seslendi)*. "
 "ندي *(seslenme, nidâ)* korpusta 51 geçişli. Ölçülebilir bir görevlendirme karşılaştırması: "
 "25:36'da فَقُلْنَا ٱذْهَبَآ *(dedik ki: ikiniz gidin)* — İKİL emir ve fâil 1P; burada ٱئْتِ "
 "ٱلْقَوْمَ ٱلظَّٰلِمِينَ *(zalim topluluğa git)* — TEKİL emir ve fâil رَبّ *(Rab)*. Aynı sahne, "
 "iki sûrede iki farklı sıkıştırma: sûre 25 görevlendirmeyi ve helâki tek ayete sığdırmıştı, sûre "
 "26 onu bir diyaloga açıyor. Ve sûrenin ilk adlı aktörü burada, rol mef'ûl."),
11: ("Dört kelime ve ayet bir öncekinin tamamlayıcısı: 26:10'da topluluk NİTELİKLE verilmişti "
 "(ٱلْقَوْمَ ٱلظَّٰلِمِينَ *(zalim topluluk)*), burada ADLA (قَوْمَ فِرْعَوْنَ *(Firavun'un "
 "kavmi)*). Ölçülebilir bir adlandırma sırası: önce nitelik, sonra ad. Kapanış bir soru ve muhatabı "
 "belirsiz: أَلَا يَتَّقُونَ *(sakınmıyorlar mı)* — soru ne Mûsâ'ya ne Firavun'a, anlatıya açık. "
 "وقي *(sakınma, koruma)* sûrede sık bir kök olacak; korpusta 258 geçişli."),
12: ("Cevap bir korkuyla açılıyor ve korku nesnesi tekzip: أَخَافُ أَن يُكَذِّبُونِ *(beni "
 "yalanlamalarından korkuyorum)*. Ölçülebilir bir şahıs yoğunluğu: altı kelimede 1S x4. Yıldızın "
 "tek kaynağı rab z=3,23 — yine kısa ayet ve tek Rab. Ve sûre 25 ile karşıtlık: 25:30'da elçi "
 "يَٰرَبِّ *(Rabbim)* diye kavminin Kur'ân'ı terk etmesinden ŞİKÂYET ediyordu (gerçekleşmiş bir "
 "durum), burada رَبِّ diye yalanlanmaktan KORKUYOR (gerçekleşmemiş bir olasılık). İki sûrede aynı "
 "nida, iki ayrı zaman kipi."),
13: ("İki yetersizlik sayılıyor ve ikisi de bedensel: يَضِيقُ صَدْرِى *(göğsüm daralır)* ve لَا "
 "يَنطَلِقُ لِسَانِى *(dilim çözülmez)*. ضيق *(darlık)* sûre 25'te de vardı (25:13, مَكَانا ضَيِّقا "
 "*(dar bir yer)*) ama orada fiziksel bir yer, burada içsel bir hâl — aynı kök, iki katman. طلق "
 "*(salıverme, boşama)* korpusta 23 geçişli ve çoğu 'boşama' anlamında; burada bab VII ve 'çözülme' "
 "anlamında — kök düzeyi dikey komşuluk bu ayrımı yapmıyor (aday 529 sınıfı). Ve fâsıla bir özel "
 "ad: هَٰرُونَ *(Hârûn)*, ن ile bittiği için kafiye sınıfına uyuyor."),
14: ("Üçüncü bir korku ekleniyor ve nesnesi ölüm: أَخَافُ أَن يَقْتُلُونِ *(beni öldürmelerinden "
 "korkuyorum)*. Ölçülebilir bir fâsıla eşleşmesi: 26:12 يُكَذِّبُونِ *(beni yalanlarlar)* ve burada "
 "يَقْتُلُونِ *(beni öldürürler)* — aynı ek (ـُونِ, nûn-i vikâye + yâ düşmesi), aynı kip, aynı "
 "korku fiili. İki ayet arasında 26:13 duruyor ve onun fâsılası bir özel ad. Yani üç ayette iki "
 "farklı fâsıla tipi dönüşümlü. ذنب *(günah, suç)* sûre 25'te de vardı (25:58) ama orada kulların "
 "günahlarından haberdar olma, burada bir suç isnadı."),
15: ("Emir ikil kipte ve okumada ikinci kez: ٱذْهَبَا *(ikiniz gidin)* — birincisi 25:36'daydı. "
 "Ölçülebilir bir fark: orada emri فَدَمَّرْنَٰهُمْ تَدْمِيرا *(onları darmadağın ettik)* izliyordu, "
 "burada إِنَّا مَعَكُم مُّسْتَمِعُونَ *(biz sizinle beraber işitenleriz)* izliyor. Aynı fiil, iki "
 "sonuç: helâk ve eşlik. Ayet KELLA ile açılıyor — sûrenin iki KELLA'sından ilki. Ve fâsıla bir "
 "ism-i fâil çoğulu: مُّسْتَمِعُونَ *(işitenler)*, سمع *(işitme)* bab X."),
16: ("Blokta en yüksek dış düğüm (5) ve iki xref'ten biri DÖRT ayete birden bağlanıyor: رَسُولُ "
 "رَبِّ ٱلْعَٰلَمِينَ *(âlemlerin Rabbinin elçisi)* terkibi 7:61, 7:67, 7:104 ve 43:46'da. Donmuş "
 "kalıp adayı (aday 437). Ölçülebilir bir şahıs yapısı: emir ikil (فَأْتِيَا *(varın)*, فَقُولَآ "
 "*(deyin)*) ama söylenen söz TEKİL (إِنَّا رَسُولُ *(biz elçisiyiz)* — رَسُول tekil, zamir çoğul). "
 "İki kişi, tek elçilik. Ve علم *(bilme; âlem)* kökü sûre 25'in ilk ayetiyle karşılaşıyor: orada "
 "kitap لِلْعَٰلَمِينَ *(âlemlere)* uyarıcı, burada elçi رَبِّ ٱلْعَٰلَمِينَ'den."),
17: ("Beş kelime ve sûrenin dört kafiye kırılmasından ilki: fâsıla إِسْرَٰٓءِيلَ *(İsrâîl)*, ل ile "
 "bitiyor ve N sınıfına uymuyor. Ölçülebilir bir düzen: kırılan fâsıla bir ÖZEL AD — ve 26:13'ün "
 "fâsılası da özel ad (هَٰرُونَ *(Hârûn)*) ama o ن ile bitip sınıfa uyuyor. Yani sûre özel adları "
 "fâsılaya koyuyor ve bazıları kafiyeyi kırıyor, bazıları kırmıyor; kırılma adın kendi ses yapısına "
 "bağlı. Yıldızın tek kaynağı bu kırılma (kafiye_kirik=1). Sûre 25'te tek kırılma vardı ve o da "
 "fâsılası ٱلسَّبِيلَ *(yol)* olan 25:17'ydi — orada kırılan bir cins ad."),
18: ("Firavun'un cevabı bir hatırlatma ve fiil kökü dikkat çekici: أَلَمْ نُرَبِّكَ فِينَا وَلِيدا "
 "*(seni çocukken içimizde yetiştirmedik mi)*, ربو *(yetiştirme, büyütme; ribâ)* kökü bab II. İki "
 "ayet önce Mûsâ رَبِّ ٱلْعَٰلَمِينَ *(âlemlerin Rabbi)* demişti, ربب *(rab, terbiye etme)* "
 "kökünden. İKİ AYRI KÖK, AYNI ANLAM ALANI: terbiye etme. Firavun'un iddiası bir terbiye "
 "iddiasıdır ve Mûsâ'nın getirdiği elçilik de bir terbiye kaynağına dayanır. Ölçülebilir olan: "
 "iki kökün korpusta ayrı olması (ربب n=980, ربو n=20) ve burada iki ayet arayla karşı karşıya "
 "gelmesi. Zaman ölçüsü de veriliyor: سِنِينَ *(yıllar)*, سنو *(yıl)* kökü — sayı verilmiyor."),
19: ("Yedi kelimede 2MS altı kez — ayette başka şahıs yok. Ölçülebilir bir kök yoğunluğu: فعل "
 "*(yapma, işleme)* ÜÇ kez (وَفَعَلْتَ فَعْلَتَكَ ٱلَّتِى فَعَلْتَ *(ve yaptın o yaptığını)*) — "
 "okumada bir ayette aynı kökün üç kez geçtiği ikinci yer; birincisi 25:71'deki توب *(tövbe, "
 "dönüş)* üçlüsüydü. Karşıtlık tam: orada üç geçiş de OLUMLU (tövbe eden, döner, bir dönüşle), "
 "burada üçü de SUÇLAMA. Aynı biçimsel yoğunluk, ters değer. Ve fâsıla ٱلْكَٰفِرِينَ *(nankörler)* "
 "— كفر *(inkâr, nankörlük)* burada 'nankörlük' anlamında, 'inkâr' değil."),
20: ("Sûrenin ilk iltifâtı burada, yön 2>13. Ölçülebilir bir kabul: Mûsâ suçlamayı reddetmiyor, "
 "fiili aynı kökle üstleniyor — فَعَلْتُهَآ *(onu yaptım)*, فعل *(yapma, işleme)* kökü, bir önceki "
 "ayetin üç geçişinden sonra dördüncü. Bitişik iki ayette aynı kök dört kez. Nitelemeyi ise "
 "değiştiriyor: Firavun ٱلْكَٰفِرِينَ *(nankörler)* demişti, Mûsâ ٱلضَّآلِّينَ *(sapkınlar)* diyor. "
 "İki fâsıla, iki sınıf adı, aynı ism-i fâil çoğul kalıbı. ضلل *(sapma, saptırma)* sûre 25'te altı "
 "geçişliydi ve hep başkaları için kullanılıyordu; burada konuşan kendisi için kullanıyor."),
}

ATLAMA = {
 "_mercek_26_9": ("26:9 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. Beş kelimelik nakarat ayeti: وَإِنَّ "
  "رَبَّكَ لَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ. Tek kaynak rab z=3,94 (n=5, tek Rab, oran 0,20 — 25:64 "
  "ile AYNI değer ve aynı sebep). İçerik tamamen esmâ bildirimi. ADAY 599/602'nin sûre 26'daki "
  "ilk vakası."),
 "_mercek_26_12": ("26:12 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. قَالَ رَبِّ إِنِّىٓ أَخَافُ أَن "
  "يُكَذِّبُونِ *(dedi ki: Rabbim, beni yalanlamalarından korkuyorum)*. Tek kaynak rab z=3,23 "
  "(n=6, tek Rab). İçerik tamamen duygu/korku bildirimi. ADAY 599/602'nin ikinci vakası."),
 "_blok_notu_26_1_20": ("BLOK BİLANÇOSU: ★★★ 2 (26:9, 26:12) · ★★ 2 (26:10, 26:16) · ★ 1 (26:17) · "
  "15 ayet yıldızsız. **DÖRT YILDIZLI AYETİN DÖRDÜNDE DE TEK KAYNAK رَبّ ORANI**, beşincisinde "
  "kafiye kırılması. **HİÇBİRİNDE ÇIPA YOK.** Blokta çıpa taşıyabilecek tek ayet 26:7 (yeryüzünde "
  "bitki çeşitliliği) ve YILDIZSIZ — sûre 25'in deseninin aynen tekrarı. AYRICA 26:1 KÖK "
  "TAŞIMADIĞI İÇİN ▽ SATIRI YAZILAMADI; okumada bu ilk kez oluyor ve protokol gereği (komşuluk "
  "zenginleşmesi olmadan ▽ yazılamaz) satır ATLANDI, gerekçesi buraya kaydedildi."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
OM['26'] = {"_makro": MAKRO, "_mercek_atlama_notu": dict(ATLAMA)}
for n in range(1, 21):
    e = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": OLCUM[n], "mercek": MERCEK[n]}
    if ("26:%d" % n) in DIK:
        e["dikey"] = DIK["26:%d" % n]
    else:
        e["dikey"] = "▽ YAZILAMADI — ayette kök yok (26:1, hurûf-ı mukattaa). Gerekçe _mercek_atlama_notu'nda."
    OM['26']["26:%d" % n] = e
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) AÇILDI — makro profil + 26:1-20.** "
                         "Devam: 26:21'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-20 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1742
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK['26'] = {"26:%d" % n: MERCEK[n] for n in range(1, 21)}
MK['26_atlama'] = dict(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
