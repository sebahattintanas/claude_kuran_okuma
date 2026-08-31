# -*- coding: utf-8 -*-
"""blok_21_101_112.py — Enbiyâ'nın kapanış bloğu."""
import json

DIK = json.load(open('blok_dikey_21_101_112.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
101: "Kendilerine bizden en güzel karşılık geçmiş olanlara gelince, işte onlar ondan uzaklaştırılmışlardır.",
102: "Onun uğultusunu duymazlar; canlarının çektiği şeyler içinde ebedî kalırlar.",
103: "O en büyük dehşet onları üzmez; melekler onları karşılar: \"İşte bu, size vaat edilen gününüzdür.\"",
104: "O gün göğü, kitap sayfalarını dürer gibi düreriz. İlk yaratmaya başladığımız gibi onu yeniden döndürürüz. Bu, üzerimize aldığımız bir vaattir. Bunu yapan biziz.",
105: "Andolsun, Zikir'den sonra Zebûr'da da yazmıştık: Yere salih kullarım vâris olacak.",
106: "Kulluk eden bir topluluk için bunda bir tebliğ vardır.",
107: "Seni ancak âlemlere bir rahmet olarak gönderdik.",
108: "De ki: Bana ancak, ilâhınızın tek bir ilâh olduğu vahyediliyor. Artık teslim oluyor musunuz?",
109: "Yüz çevirirlerse de ki: Size eşit şekilde bildirdim. Size vaat edilen şey yakın mı uzak mı, bilmiyorum.",
110: "O, sözün açığa vurulanını da bilir, gizlediklerinizi de bilir.",
111: "Bilmiyorum, belki o sizin için bir sınama ve bir süreye kadar bir geçimliktir.",
112: "Dedi ki: Rabbim, hak ile hükmet. Rabbimiz Rahmân'dır; sizin nitelemelerinize karşı yardımı istenendir.",
}

OLCUM = {
101: "eksen yok · aktör yok · edim haber · şahıs 3FS ×2 · 3MP 1 · 1P 1 · n=9 mora=53 harf=39, fâsıla مُبْعَدُونَ *(uzaklaştırılmışlar)* → ن, N; i'râb ACC 1 · NOM 2; bab I ×1 (tek fiil); simetri [3,1,4,1]; ism-i mef'ûl مُبْعَدُونَ · kökler سبق *(geçme, öne geçme)* · حسن *(güzellik, iyilik)* · بعد *(sonra; uzaklık)* · bağ: 21:27 ile ortak سبق *(geçme, öne geçme)*, ters yön (elle, L2)",
102: "eksen yok · aktör yok · edim haber, kip NEG 1 · şahıs 3MP ×4 · 3FS ×2 · n=9 mora=46 harf=38, fâsıla خَٰلِدُونَ *(kalıcılar)* → ن, N — 21:99'un fâsılasıyla aynı kelime, üç ayet arayla ve TERS taraf için; i'râb ACC 1 · NOM 2; bab I ×1 · bab VIII ×1 · kökler سمع *(işitme)* · حسس *(hafif ses, uğultu; hissetme)* · شهو *(iştah, arzu)* · نفس *(nefis, can)* · خلد *(ebedî kalma)* · bağ: **21:100 ile karşıt ikiz** — orada لَا يَسْمَعُونَ *(işitmezler)* azap içinde, burada لَا يَسْمَعُونَ nimet içinde (elle, L1)",
103: "eksen yok · aktör yok — melekler ملك *(melek; mülk, sahiplik)* köküyle geçiyor, aktör tablosuna girmiyor · edim haber, kip NEG 1 · şahıs 3MS 1 · 3MP ×2 · 2MS 1 · 2MP ×5 · n=11 mora=69 harf=56, fâsıla تُوعَدُونَ *(vaat ediliyorsunuz)* → ن, N; **i'râb NOM 4 — tamamı merfû**; bab I ×3 · bab V ×1; edilgen 1 (تُوعَدُونَ, z=1.1); biçim DIKKAT · kökler حزن *(hüzün, keder)* · فزع *(dehşet, ürküntü)* · كبر *(büyüklük; büyüklenme)* · لقي *(karşılaşma, buluşma)* · ملك *(melek; mülk, sahiplik)* · يوم *(gün)* · كون *(olmak)* · وعد *(vaat)* · bağ: xref يوم *(gün)* + كون *(olmak)* + وعد *(vaat)* → 70:44",
104: "eksen yok · aktör yok · edim haber · şahıs **1P ×8** · 3MS 1 · n=16 mora=93 harf=70, fâsıla فَٰعِلِينَ *(yapanlar)* → ن, N — sûrede ÜÇÜNCÜ kez aynı fâsıla (21:68, 21:79, 21:104); i'râb ACC 6 · GEN 4; bab I ×3 · bab IV ×1; kök ikilemesi طوي *(dürme, katlama)* ×2 — biri fiil نَطْوِى *(düreriz)*, öteki masdar كَطَىِّ *(dürer gibi)* (teşbîh) · kökler يوم *(gün)* · طوي *(dürme, katlama)* · سمو *(ad; gök)* · سجل *(tomar, dürülmüş sayfa)* · كتب *(yazma, kitap)* · بدأ *(başlama, ilk yapma)* · أول *(ilk, evvel)* · خلق *(yaratma)* · عود *(dönme, tekrarlama)* · وعد *(vaat)* · كون *(olmak)* · فعل *(yapma, işleme)* · bağ: 21:30 ile ortak سمو *(ad; gök)* + خلق *(yaratma)*, ters yön (elle, L2)",
105: "eksen yok · aktör: adlı زَبُور *(Zebûr)* 4. sırada, tür **'kitab' — sûrenin tek kitap aktörü**, rol mecrur · edim haber, kip EMPH 1 · CERT 1 · şahıs 1P ×2 · 3MS 1 · 3FS 1 · 1S 1 · n=12 mora=62 harf=52, fâsıla ٱلصَّٰلِحُونَ *(salihler)* → ن, N — sûrede üçüncü kez صلح fâsılası (21:72, 21:75/86, burada), ilk kez **merfû**; i'râb GEN 3 · ACC 2 · NOM 2; bab I ×2 · kökler كتب *(yazma, kitap)* · زبر *(yazılı parça, Zebûr)* · بعد *(sonra; uzaklık)* · ذكر *(anma, zikir)* · أرض *(yer, yeryüzü)* · ورث *(miras, vâris olma)* · عبد *(kul, kulluk)* · صلح *(iyi olma, salâh)* · bağ: 21:89 ile ortak ورث *(miras, vâris olma)* (elle, L2)",
106: "eksen yok · aktör yok · edim haber, kip EMPH 1 · şahıs **alan BOŞ — ayette hiç fiil yok** · n=6 mora=37 harf=22 — **sûrenin en az harfli ayeti**, fâsıla عَٰبِدِينَ *(kulluk edenler)* → ن, N; i'râb ACC 2 · GEN 2; **bab alanı boş, zaman alanı boş — 21:85 ile birlikte sûrenin İKİ fiilsiz ayetinden biri**; biçim DIKKAT · kökler بلغ *(ulaşma, tebliğ)* · قوم *(kalkma; kavim; kıyamet)* · عبد *(kul, kulluk)* · bağ: 21:85 ile fiilsizlik ortaklığı (elle, L3)",
107: "eksen yok · aktör yok · edim haber, kip NEG 1 · RES 1 · şahıs 1P ×2 · 2MS 1 · n=5 mora=35 harf=24 — **sûrenin en kısa ikinci ayeti**, fâsıla لِّلْعَٰلَمِينَ *(âlemler için)* → ن, N — sûrede üçüncü kez (21:71, 21:91, burada); i'râb ACC 1 · GEN 1; bab IV ×1 (tek fiil); biçim HASR (إِلَّا *(ancak)*) · kökler رسل *(gönderme, elçi)* · رحم *(rahmet, merhamet)* · علم *(bilme; âlem)* · bağ: 21:25 ile ortak رسل *(gönderme, elçi)* + HASR (elle, L1)",
108: "eksen yok · aktör yok · edim soru + emir, kip IMPV 1 · INTG 1 · şahıs 2MS 1 · 3MS 1 · 1S 1 · 2MP ×2 · n=11 mora=61 harf=44, fâsıla مُّسْلِمُونَ *(teslim olanlar)* → ن, N; i'râb ACC 2 · NOM 4; bab I ×1 · bab IV ×1; **edilgen 1 (يُوحَىٰٓ *(vahyediliyor)*, z=2.52)**; kök ikilemesi أله *(ilâh)* ×2; sayı sözcüğü وَٰحِد *(bir, tek)*; simetri [3,4,9,1]; **dış düğüm 4** · yıldız ★★ · kökler قول *(söz söyleme)* · وحي *(vahiy, gizli bildirim)* · أله *(ilâh)* · وحد *(bir olma, teklik)* · سلم *(esenlik; teslim olma)* · bağ: xref إله *(ilâh)* + واحد *(tek)* + مسلم *(teslim olan)* → 2:133 · 29:46 · أوحى *(vahyetti)* + إله ×2 → 18:110 · 41:6",
109: "eksen: lafız yok · **esmâ قَرِيب *(yakın)* 9. sırada — ÖLÇÜM ARTEFAKTI (aday 444)**: أَقَرِيبٌ أَم بَعِيدٌۭ *(yakın mı uzak mı)*, göndergesi vaat edilen ŞEY, ilâhî ad değil; üstelik بَعِيد *(uzak)* ile karşıtlık içinde · aktör yok · edim soru + emir + şart, kip COND 1 · IMPV 1 · NEG 1 · INTG 1 — **dört ayrı kip, sûrenin en yoğun kip ayeti** · şahıs 3MP ×2 · 2MS 1 · 1S ×3 · 2MP ×3 · n=13 mora=70 harf=55, fâsıla تُوعَدُونَ *(vaat ediliyorsunuz)* → ن, N — 21:103'ün fâsılasıyla aynı kelime; i'râb GEN 1 · NOM 2; bab I ×3 · bab IV ×1 · bab V ×1; edilgen 1; simetri [3,5,10,1]; ayet içi أَم *(yoksa)* muttasıla · kökler ولي *(dost, veli; velâyet)* · قول *(söz söyleme)* · أذن *(izin; bildirme; kulak)* · سوي *(denk, düzleme)* · دري *(bilme, farkında olma)* · قرب *(yakınlık)* · بعد *(sonra; uzaklık)* · وعد *(vaat)* · bağ: 21:97 ile ortak قرب *(yakınlık)* + وعد *(vaat)*, ters bilgi durumu (elle, L1)",
110: "eksen yok · aktör yok · edim haber · şahıs 3MS ×3 · 2MP ×2 · n=8 mora=37 harf=33, fâsıla تَكْتُمُونَ *(gizlersiniz)* → ن, N; i'râb ACC 2 · GEN 1; bab I ×3; kök ikilemesi علم *(bilme)* ×2 — iki kez aynı fiil, iki ayrı nesne; zaman IMPF ×3 — PERF yok · kökler علم *(bilme)* · جهر *(açığa vurma, sesi yükseltme)* · قول *(söz söyleme)* · كتم *(gizleme, saklama)* · bağ: xref جهر *(açığa vurma)* + قول *(söz)* + علم *(bilme)* → 20:7",
111: "eksen yok · aktör yok · edim haber, kip NEG 1 · şahıs 1S 1 · 3MS 1 · 2MP 1 · n=8 mora=38 harf=31, fâsıla حِينٍۢ *(bir süreye kadar)* → ن, N; i'râb ACC 1 · NOM 2 · GEN 1; bab I ×1 (tek fiil); simetri [3,1,5,1]; **21:109'un وَإِنْ أَدْرِى *(bilmiyorum)* ifadesi burada aynen tekrarlanıyor — iki ayet arayla ikinci kez** · kökler دري *(bilme, farkında olma)* · فتن *(sınama, fitne)* · متع *(geçimlik, faydalandırma)* · حين *(vakit)* · bağ: 21:35 ile ortak فتن *(sınama, fitne)* (elle, L2)",
112: "eksen: lafız yok · **Rab İKİ geçiş, 2. ve 5. sırada — رَبِّ *(Rabbim)* nidâ ve رَبُّنَا *(Rabbimiz)* haber (rab z=3.94 — SÛRENİN EN YÜKSEK DEĞERİ, 21:89'un 3,55'ini geçiyor)** · **esmâ رَحْمٰن *(Rahmân)* 6. sırada — GEÇERLİ**, ٱلرَّحْمَٰنُ ٱلْمُسْتَعَانُ *(yardımı istenen Rahmân)* terkîbinde · aktör yok · edim emir, kip IMPV 1 · şahıs 3MS 1 · 1S 1 · 2MS 1 · 1P 1 · 2MP ×2 · n=10 mora=55 harf=43, fâsıla تَصِفُونَ *(nitelersiniz)* → ن, N; i'râb ACC 1 · GEN 1 · NOM 3; bab I ×3; kök ikilemesi ربب *(rab, terbiye etme)* ×2 · yıldız ★★★ · kökler قول *(söz söyleme)* · ربب *(rab, terbiye etme)* · حكم *(hüküm verme, hikmet)* · حقق *(hak, gerçek)* · رحم *(rahmet, merhamet)* · عون *(yardım, destek)* · وصف *(niteleme, vasıf)* · bağ: **21:18 ve 21:22 ile وصف *(niteleme, vasıf)* çerçevesi** (elle, L1 — bkz. aday 459)",
}

MERCEK = {
101: "Ayet bir ön-geçiş kaydediyor: سَبَقَتْ لَهُم مِّنَّا ٱلْحُسْنَىٰٓ *(kendilerine bizden en güzel karşılık geçti)* — سبق *(geçme, öne geçme)* kökü sûrede 21:27'de olumsuzlanmıştı (لَا يَسْبِقُونَهُۥ بِٱلْقَوْلِ *(sözle önüne geçmezler)*). Orada kulun öne geçmesi kaldırılıyordu, burada karşılığın önden gitmesi kuruluyor. Aynı kök, iki yön. Sonuç ism-i mef'ûl ile veriliyor: مُبْعَدُونَ *(uzaklaştırılmışlar)* — edilgen bir konum.",
102: "21:100 ile karşıt ikiz. Orada لَا يَسْمَعُونَ *(işitmezler)* azap içindekiler içindi ve yanında زَفِيرٌ *(ağır soluk)* vardı; burada aynı fiil nimet içindekiler için ve işitilmeyen şey حَسِيسَهَا *(onun uğultusu)*. Aynı olumsuzlama iki ayet arayla iki karşıt tarafa uygulanıyor. Fâsıla da eşleşiyor: خَٰلِدُونَ *(kalıcılar)* 21:99'da ateş için, burada arzu edilen şeyler için.",
103: "Ayetin i'râbı tamamen merfû (NOM 4) — cümle bir eylem değil bir durum tablosu kuruyor. İki olumsuz-olumlu çift: üzülmeme (لَا يَحْزُنُهُمُ) ve karşılanma (تَتَلَقَّىٰهُمُ ٱلْمَلَٰٓئِكَةُ *(melekler onları karşılar)*, bab V). Sonra doğrudan söz araya giriyor ve şahıs 2MP'ye kayıyor: هَٰذَا يَوْمُكُمُ *(işte bu, sizin gününüz)*. Anlatı üçüncü şahıstan hitaba geçiyor.",
104: "Teşbîh iki kez aynı kökle kuruluyor: نَطْوِى … كَطَىِّ *(düreriz… dürer gibi)* — biri fiil biri masdar, benzeyen ile benzetilen aynı kelimeden. Benzetilen şey bir yazı nesnesi: ٱلسِّجِلِّ لِلْكُتُبِ *(kitaplar için tomar)*. İkinci cümle zamanı tersine çeviriyor: كَمَا بَدَأْنَآ أَوَّلَ خَلْقٍۢ نُّعِيدُهُۥ *(ilk yaratmaya başladığımız gibi onu döndürürüz)* — بدأ *(başlama, ilk yapma)* ve عود *(dönme, tekrarlama)* aynı cümlede, biri başlangıç biri dönüş. Sekiz 1P, sûrenin en yoğun anlatıcı ayetlerinden.",
105: "Yazma iki katmanlı: كَتَبْنَا فِى ٱلزَّبُورِ مِنۢ بَعْدِ ٱلذِّكْرِ *(Zikir'den sonra Zebûr'da yazdık)* — iki kitap adı ve aralarında bir sıra (بعد *(sonra; uzaklık)*). Yazılan içerik bir miras hükmü: ٱلْأَرْضَ يَرِثُهَا عِبَادِىَ ٱلصَّٰلِحُونَ *(yere salih kullarım vâris olur)*. ورث *(miras, vâris olma)* kökü sûrede 21:89'da bir esmâ terkîbindeydi (خَيْرُ ٱلْوَٰرِثِينَ *(vârislerin en hayırlısı)*); burada vâris kullar. Aynı kök, iki taraf.",
106: "Sûrenin iki fiilsiz ayetinden ikincisi (öteki 21:85). Altı kelime, hiç fiil yok, ve en az harfli ayet. Cümle bir kapsayıcılık kuruyor: إِنَّ فِى هَٰذَا لَبَلَٰغًۭا *(bunda bir tebliğ vardır)* — هَٰذَا *(bu)* göndergesi belirsiz bırakılıyor. Alıcı ise daraltılıyor: لِّقَوْمٍ عَٰبِدِينَ *(kulluk eden bir topluluk için)*.",
107: "Beş kelime, tek fiil, HASR. Elçilik olumsuz-istisnalı kuruluyor: وَمَآ أَرْسَلْنَٰكَ إِلَّا رَحْمَةًۭ *(seni ancak bir rahmet olarak gönderdik)* — aynı kalıp 21:25'te bütün elçiler için kullanılmıştı (وَمَآ أَرْسَلْنَا … إِلَّا *(göndermedik ki… olmasın)*). Orada gönderilen şey vahiy içeriğiydi, burada gönderilenin kendisi bir nitelik olarak adlandırılıyor. Kapsam sûrede üçüncü kez aynı kelimeyle: لِّلْعَٰلَمِينَ *(âlemler için)*.",
108: "Ayet iki إِنَّمَا-benzeri sınırlayıcıyı üst üste koyuyor: إِنَّمَا يُوحَىٰٓ إِلَىَّ أَنَّمَآ *(bana ancak… olduğu vahyediliyor)*. Birincisi vahyin kapsamını, ikincisi vahyin içeriğini sınırlıyor. İçerik aynı kökün iki kez geçmesiyle kuruluyor: إِلَٰهُكُمْ إِلَٰهٌۭ وَٰحِدٌۭ *(ilâhınız tek bir ilâhtır)* — özne ve haber aynı kelime, ayıran tek şey sayı sıfatı. Fiil edilgen: kimin vahyettiği söylenmiyor.",
109: "Dört ayrı kip tek ayette (COND · IMPV · NEG · INTG) — sûrenin en yoğun kip ayeti. Bildirimin niteliği tek kelimeyle: عَلَىٰ سَوَآءٍۢ *(eşit şekilde)*, سوي *(denk, düzleme)*. Sonra konuşan kendi bilgi sınırını açıkça koyuyor: وَإِنْ أَدْرِىٓ *(bilmiyorum)*. Bilinmeyen şey bir ikilem olarak veriliyor: أَقَرِيبٌ أَم بَعِيدٌۭ *(yakın mı uzak mı)* — قرب *(yakınlık)* kökü 21:1 ve 21:97'de kesin bir yaklaşma bildiriyordu; burada aynı kök bir belirsizliğin iki ucundan biri.",
110: "Aynı fiil iki kez ve iki karşıt nesne alıyor: يَعْلَمُ ٱلْجَهْرَ مِنَ ٱلْقَوْلِ وَيَعْلَمُ مَا تَكْتُمُونَ *(sözün açığa vurulanını bilir, gizlediklerinizi de bilir)* — جهر *(açığa vurma, sesi yükseltme)* ve كتم *(gizleme, saklama)*. Bilme değişmiyor, bilinenin görünürlüğü değişiyor. Ayette PERF yok; üç fiil de IMPF.",
111: "İki ayet önceki وَإِنْ أَدْرِى *(bilmiyorum)* aynen tekrarlanıyor — bu kez bilinmeyen zaman değil amaç. İki olasılık ACC olarak sıralanıyor: فِتْنَةٌۭ لَّكُمْ وَمَتَٰعٌ إِلَىٰ حِينٍۢ *(sizin için bir sınama ve bir süreye kadar geçimlik)*. فتن *(sınama, fitne)* kökü sûrede 21:35'te ölçütün adıydı (بِٱلشَّرِّ وَٱلْخَيْرِ فِتْنَةًۭ *(şerle ve hayırla bir sınama olarak)*); burada gecikmenin kendisi sınama olarak konuluyor.",
112: "Sûrenin son ayeti ve Rab yoğunluğunun tepesi. İki Rab iki ayrı seste: رَبِّ *(Rabbim)* nidâ ve tekil-iyelikli, رَبُّنَا *(Rabbimiz)* haber ve çoğul-iyelikli — özel dua ile ortak ikrar yan yana. Kapanış fâsılası sûreyi kendi başına bağlıyor: تَصِفُونَ *(nitelersiniz)*, kök وصف *(niteleme, vasıf)*. Aynı kök 21:18'de (تَصِفُونَ) ve 21:22'de (يَصِفُونَ) de fâsılaydı; korpustaki 14 geçişin üçü bu sûrede ve üçü de ayet sonunda. Şahıs sırası 2MP → 3MP → 2MP, yani muhataptan üçüncü şahsa ve yine muhataba.",
}

om = json.load(open('okuma_metni.json', encoding='utf-8'))
mk = json.load(open('mercek_kayit.json', encoding='utf-8'))

for n in range(101, 113):
    key = "21:%d" % n
    om['21'][key] = {'ar': AR[(21, n)], 'meal': MEAL[n], 'olcum': OLCUM[n],
                     'mercek': MERCEK[n], 'dikey': DIK[key]}
    mk['21'].append([key, MERCEK[n]])

om['21']['_mercek_atlama_notu'] += (
 " 21:112 biyolog ve uzay ATLANDI — ayetin kökleri حكم *(hüküm verme, hikmet)*, حقق *(hak, gerçek)*, "
 "عون *(yardım, destek)*, وصف *(niteleme, vasıf)*; ne canlılık ne gök çıpası var. "
 "SÛRE 21 TOPLAMI: 11 ★★★ ayetin 4'ünde biyolog yazıldı (30, 79, 87, 96), 2'sinde uzay yazıldı (30, 42); "
 "geri kalanlarda çıpa bulunmadığı için mercek atlandı ve her biri burada kayıtlıdır.")

om['21']['_kapanis'] = {
 "durum": "TAM — 112/112",
 "kafiye": "112/112 N sınıfı. Son harf: 106 ayet ن, 6 ayet م (21:4, 60, 62, 66, 69, 76). "
           "Kafiye SINIFI hiç kırılmadı; م sapmalarının üçü doğrudan إِبْرَٰهِيم *(İbrâhim)* adı (aday 453).",
 "eksen": {"allah_token": 6, "allah_ayet": [22, 57, 66, 67, 98],
   "dagilim": "21:22 ×2 anlatıcı · 21:57 İbrâhim yemini · 21:66 ve 21:67 İbrâhim hitabı · 21:98 muhataba hitap",
   "min_duni_llah_kalibi": [66, 67, 98],
   "rab_token": 14, "rab_tepe": [[112, 3.94], [89, 3.55], [56, 2.96]],
   "lafiz_sessizligi": "21:1-21 (21 ayet) · 21:23-56 (34 ayet) · 21:68-97 (30 ayet)"},
 "esma": {"ham_token": 17, "gecerli": 7, "kesin_yanlis": 8, "supheli": 2,
   "hata_orani": 0.47, "supheli_dahil": 0.59, "not": "aday 444 — nihai sayım"},
 "olcumler": {"ayet": 112, "kelime": 1169, "mora": 6603,
   "hapaks_ayet": 8, "hapaks_kok": 9,
   "hapaksler": [[11,"قصم"],[18,"دمغ"],[30,"رتق"],[30,"فتق"],[42,"كلأ"],[46,"نفح"],[79,"فهم"],[87,"نون"],[96,"حدب"]],
   "edilgen_ayet": 16, "edilgen_fiil": 18,
   "yildiz": {"3": 11, "2": 8, "1": 7, "0": 86},
   "edim": {"haber": 74, "soru": 16, "emir": 15, "şart": 12, "nida": 5, "yasak": 2},
   "adli_aktor_token": 27, "adli_aktor_ayet": 21,
   "en_uzun": [87, 23], "en_kisa": [14, 4],
   "iltifat": 2, "kok_ikilemesi_ayet": 31,
   "tam_ayet_ikizi": {"38": [[10,48],[27,71],[34,29],[36,48],[67,25]], "41": [[6,10]]}},
 "cerceve": "وصف *(niteleme, vasıf)* kökü sûrede üç kez ve üçü de fâsıla: 21:18 تَصِفُونَ (2MP) · "
            "21:22 يَصِفُونَ (3MP) · 21:112 تَصِفُونَ (2MP). Korpustaki 14 geçişin üçü bu sûrede — "
            "hiçbir sûrede daha fazlası yok (aday 459).",
 "bolut_ikizleri": "Sûre üç ardışık bölüt ikizi verdi: 21:41 ↔ 6:10 (tam ayet) · "
                   "21:81-82 ↔ 38:36-37 (aday 457) · 21:92-93 ↔ 23:52-53 (aday 456).",
 "acik_borclar": "esmâ tablosu onarılmadan (aday 444) sûrenin esmâ profili kullanılamaz; "
                 "dikey satırlar aday 435 + 452 onarımından sonra yeniden üretilecek."
}

om['ilerleme']['tam'].append(21)
om['ilerleme']['kismi'].pop('21', None)
om['ilerleme']['bekleyen'].pop('21', None)
om['ilerleme']['not'] = ("Sûre 20 TAM (135/135). **Sûre 21 TAM (112/112)** — bu oturumda bitti. "
                         "Devam: sûre 22 (Hac). Dikey katman A parçası birincil, B etiketsiz.")
om['ilerleme']['okunan_ayet'] = 1385

json.dump(om, open('okuma_metni.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(mk, open('mercek_kayit.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("SÛRE 21 TAM · mercek:", len(mk['21']))
