# -*- coding: utf-8 -*-
"""blok_26_181_190.py — sûre 26 on altıncı blok (26:181-190). Şuayb ve ölçü-tartı bölütü."""
import json
DIK = json.load(open('blok_dikey_26_181_190.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
181: "Ölçüyü tam yapın, eksiltenlerden olmayın.",
182: "Doğru teraziyle tartın.",
183: "İnsanların eşyasını eksiltmeyin; yeryüzünde bozgunculuk yaparak taşkınlık etmeyin.",
184: "Sizi ve önceki nesilleri yaratandan sakının.",
185: "Dediler: Sen ancak büyülenmişlerdensin.",
186: "Sen ancak bizim gibi bir beşersin; seni yalancılardan sanıyoruz.",
187: "Doğru söyleyenlerdensen üzerimize gökten parçalar düşür.",
188: "Dedi: Rabbim yaptıklarınızı daha iyi bilir.",
189: "Onu yalanladılar; gölge gününün azabı onları yakaladı. O, büyük bir günün azabıydı.",
190: "Bunda elbette bir âyet var; ama onların çoğu inanmıyor.",
}

O = {
181: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir + yasak, kip IMPV 1 · "
 "PRO 1 · **şahıs 2MP x4 — ayette başka şahıs yok**, iltifât 0 · n=6 mora=34 harf=32 (n z=-0,68), "
 "fâsıla ٱلْمُخْسِرِينَ *(eksiltenler)* → ن, N sınıfı; i'râb ACC 1 · GEN 1; bab I x1 · IV x1; "
 "zaman IMPV 1 · IMPF 1; **biçim NEHY — sûrenin dört NEHY'inden üçüncüsü**; dış düğüm 0 · yıldız "
 "★ yok · kökler وفي *(tam verme, vefa; vefat ettirme)* · كيل *(ölçme (hacim))* · كون *(olmak; "
 "mekân, yer)* · خسر *(hüsran, ziyan)* · bağ: **كيل *(ölçme (hacim))* dikey ölçümü ▸sonra قسطس "
 "*(kıstas, doğru terazi)* x661,4 · وزن *(tartı, mîzan)* x153,4 veriyor — **OKUMADA GÖRÜLEN EN "
 "YÜKSEK KOMŞULUK KATI** ve iki komşu da BU BÖLÜTTE (26:182); üçlü korpusta neredeyse ayrılmaz** "
 "(elle, L1, aday 735)"),
182: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir, kip IMPV 1 · **şahıs "
 "2MP x2 — ayette başka şahıs yok**, iltifât 0 · n=3 mora=25 harf=22 (n z=-1,00), fâsıla "
 "ٱلْمُسْتَقِيمِ *(dosdoğru)* → م, N sınıfı; **i'râb GEN 2**; bab I x1; zaman IMPV 1; **dış düğüm "
 "1** · yıldız ★ yok · kökler وزن *(tartı, mîzan)* · قسطس *(kıstas, doğru terazi)* · قوم *(kalkma; "
 "kavim; kıyamet)* · bağ: xref وزن *(tartı)* + قسطاس *(kıstas)* + مستقيم *(dosdoğru)* → **17:35**; "
 "**قسطس *(kıstas, doğru terazi)* korpusta İKİ geçişli — OKUMADA İLK KEZ BİR ÖLÇÜ ARACI ADI**; "
 "dikey ölçümü ▸önce كيل *(ölçme (hacim))* x554,4 veriyor (elle, L1, aday 736)"),
183: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim yasak, kip PRO 2 · şahıs "
 "2MP x4 · 3MP x1, iltifât 0 · n=9 mora=51 harf=44 (n z=-0,36), fâsıla مُفْسِدِينَ *(bozguncular)* → "
 "ن, N sınıfı; **i'râb ACC 3 · GEN 1**; bab I x2; zaman IMPF x2; **biçim NEHY — dördüncü ve son "
 "NEHY**; **dış düğüm 2** · yıldız ★ yok · kökler بخس *(eksiltme, değerini düşürme)* · أنس "
 "*(insan)* · شيأ *(dileme; şey)* · عثو *(azgınlık, taşkınlık)* · أرض *(yer, yeryüzü)* · فسد "
 "*(bozgunculuk, fesat)* · bağ: xref ÜÇ 3-gram → **7:85 · 11:85**; **26:152 ile فسد *(bozgunculuk, "
 "fesat)* ikinci geçişi** — orada Semûd'un ileri gelenleri için, burada Eyke halkına yasak; "
 "**عثو *(azgınlık, taşkınlık)* korpusta BEŞ geçişli ve dikey ölçümü ▸sonra فسد x128,9 veriyor — "
 "çift korpusta neredeyse ayrılmaz** (elle, L1, aday 737)"),
184: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir, kip IMPV 1 · şahıs "
 "2MP x3 · 3MS x1, iltifât 0 · n=5 mora=36 harf=30 (n z=-0,79), fâsıla ٱلْأَوَّلِينَ *(öncekiler)* → "
 "ن, N sınıfı — **26:26, 26:76, 26:137'nin fâsılasıyla AYNI KELİME, dördüncü kez**; **i'râb ACC "
 "2**; bab I x1 · VIII x1; zaman IMPV 1 · PERF 1; dış düğüm 0 · yıldız ★ yok · kökler وقي *(sakınma, "
 "koruma)* · خلق *(yaratma)* · جبل *(dağ)* · أول *(ilk, evvel)* · bağ: **26:131-132 ile aynı yapı** — "
 "orada فَٱتَّقُوا۟ ٱللَّهَ *(Allah'tan sakının)* ve وَٱتَّقُوا۟ ٱلَّذِىٓ أَمَدَّكُم *(size yardım "
 "edenden sakının)*, burada وَٱتَّقُوا۟ ٱلَّذِى خَلَقَكُمْ *(sizi yaratandan sakının)*; **üçüncü "
 "kez aynı emir, üçüncü gönderge biçimi**; **جبل *(dağ)* kökü burada 'nesil, yığın' anlamında — "
 "529 sınıfı** (elle, L1, aday 738)"),
185: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3MP x2 · 2MS x1, iltifât 0 · n=5 mora=33 harf=23 (n z=-0,79), fâsıla ٱلْمُسَحَّرِينَ "
 "*(büyülenmişler)* → ن, N sınıfı; i'râb ACC 1 · GEN 1; bab I x1; zaman PERF 1; **NAKARAT alanı = "
 "2, temsil ayet 26:153 — ALTINCI KÜME TAMAMLANDI (2/2)**; **esit: 26:153 ile TAM AYET ÖZDEŞ** · "
 "dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · سحر *(büyü, sihir)* · bağ: **sûrenin "
 "en küçük nakarat kümesi kapandı** (aday 715) (elle, L1, aday 739)"),
186: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · RES 1 · "
 "CERT 1 · EMPH 1 · şahıs 2MS x2 · 1P x2, iltifât 0 · n=9 mora=48 harf=35 (n z=-0,36), fâsıla "
 "ٱلْكَٰذِبِينَ *(yalancılar)* → ن, N sınıfı; i'râb NOM 2 · GEN 1; bab I x1; zaman IMPF 1; **biçim "
 "HASR**; simetri [3,1,6,1]; dış düğüm 0 · yıldız ★ yok · kökler بشر *(müjde; beşer)* · مثل "
 "*(benzer, mesel)* · ظنن *(zan, sanma)* · كذب *(yalan; yalanlama)* · bağ: **26:154 ile aynı "
 "eşitleme kalıbı** — orada مَآ أَنتَ إِلَّا بَشَرٌ مِّثْلُنَا فَأْتِ بِـَٔايَةٍ *(sen ancak bizim "
 "gibi bir beşersin, bir âyet getir)*, burada aynı eşitleme ama devamı bir ZAN bildirimi "
 "(وَإِن نَّظُنُّكَ لَمِنَ ٱلْكَٰذِبِينَ *(seni yalancılardan sanıyoruz)*); **aynı ilk yarı, iki "
 "ayrı ikinci yarı** (elle, L1, aday 740)"),
187: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir + şart, kip IMPV 1 · "
 "COND 1 · şahıs 2MS x3 · 1P x1, iltifât 0 · n=9 mora=52 harf=37 (n z=-0,36), fâsıla "
 "ٱلصَّٰدِقِينَ *(doğru söyleyenler)* → ن, N sınıfı — **26:31 ve 26:154'ün fâsılasıyla AYNI "
 "KELİME, üçüncü kez**; **i'râb ACC 1 · GEN 2**; bab I x1 · IV x1; zaman IMPV 1 · PERF 1; simetri "
 "[3,2,6,1]; **dış düğüm 1** · yıldız ★ yok · kökler سقط *(düşme, düşürme)* · كسف *(tutulma, "
 "parça)* · سمو *(ad; gök)* · كون *(olmak; mekân, yer)* · صدق *(doğruluk)* · bağ: xref تسقط "
 "*(düşür)* + كسف *(parça)* + سماء *(gök)* → **34:9**; **26:31, 26:154 ile MEYDAN OKUMA KALIBININ "
 "ÜÇÜNCÜ GEÇİŞİ** — üçünde de إِن كُنتَ مِنَ ٱلصَّٰدِقِينَ; talep değişiyor: getir (zamir) / bir "
 "âyet getir / gökten parça düşür (elle, L1, aday 741)"),
188: ("eksen: **lafız YOK · رَبّ *(Rab)* 2. sırada — otuz dördüncü Rab**, **rab z=3,94: yıldızın "
 "TEK kaynağı** (n=5, oran 0,20) · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3MS x1 · 1S x1 · 2MP x2, iltifât 0 · n=5 mora=28 harf=19 (n z=-0,79), fâsıla تَعْمَلُونَ "
 "*(yapıyorsunuz)* → ن, N sınıfı; **i'râb NOM 2**; bab I x2; zaman PERF 1 · IMPF 1; **dış düğüm 4 — "
 "BLOKTA VE SÛREDE EN YÜKSEK** · **yıldız ★★★** · kökler قول *(söz söyleme)* · ربب *(rab, terbiye "
 "etme)* · علم *(bilme; ilim)* · عمل *(iş, amel)* · bağ: xref قال *(dedi)* + ربّ *(Rab)* + أعلم "
 "*(daha iyi bilir)* → **18:19 · 18:22 · 28:37 · 28:85**; **26:112 ve 26:168 ile عمل *(iş, amel)* "
 "üçüncü geçişi** — Nûh 'bilgim yok', Lût 'kızanlardanım', Şuayb 'Rabbim daha iyi bilir'; **üç "
 "elçi, üç tutum: bilgisizlik / öfke / bilgiyi Rabbe havale** (elle, L1, aday 742)"),
189: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3MP x3 · 3MS x4, iltifât 0 · n=10 mora=54 harf=43 — **blokta en uzun ayet** (n z=-0,26), fâsıla "
 "عَظِيمٍ *(büyük)* → م, N sınıfı — **26:135 ve 26:156'nın fâsılasıyla AYNI KELİME, üçüncü kez**; "
 "**i'râb NOM 1 · GEN 4 · ACC 2**; bab I x2 · II x1; zaman PERF x3; **İKİ KÖK BİRDEN İKİLENİYOR: "
 "عذب *(azap)* x2 VE يوم *(gün)* x2 — okumada ikinci vaka** (birincisi 26:118'de فتح *(açma)* ve "
 "بين *(arası; açıklama)*); simetri [3,3,8,1]; **dış düğüm 1** · yıldız ★ yok · kökler كذب *(yalan; "
 "yalanlama)* · أخذ *(alma, edinme)* · عذب *(azap)* · يوم *(gün)* · ظلل *(sürüp gitme, olmayı "
 "sürdürme)* · كون *(olmak; mekân, yer)* · عظم *(büyüklük, azamet; kemik)* · bağ: xref كذّب "
 "*(yalanladı)* + أخذ *(aldı)* + عذاب *(azap)* → **16:113**; **26:135, 26:156 ile عَذَابُ يَوْمٍ "
 "عَظِيمٍ ÜÇÜNCÜ geçişi**; **ظلل burada 'gölge' anlamında — 26:71'de 'sürdürme' anlamındaydı; aynı "
 "sûrede iki anlam** (aday 714/724 sınıfı) (elle, L1, aday 743)"),
190: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُؤْمِن *(mümin)* 8. sırada = fâsıla — ARTEFAKT, on "
 "üçüncü token** · aktör yok · edim haber, kip EMPH 1 · NEG 1 · şahıs 3MS x1 · 3MP x1, iltifât 0 · "
 "n=8 mora=40 harf=32 (n z=-0,47), fâsıla مُّؤْمِنِينَ → ن, N sınıfı; i'râb ACC 3 · NOM 1; bab I "
 "x1; zaman PERF 1; **açık sayı sözcüğü: كثر *(çokluk)* → أَكْثَر *(çoğu)***; **NAKARAT alanı = 6, "
 "temsil ayet 26:8 — BİRİNCİ KÜME TAMAMLANDI (6/6 standalone)**; **esit: 26:8, 67, 103, 121, 174 "
 "ile TAM AYET ÖZDEŞ** · dış düğüm 0 · yıldız ★ yok · kökler أيي *(âyet, işaret)* · كون *(olmak; "
 "mekân, yer)* · كثر *(çokluk)* · أمن *(güven; iman)* · bağ: **ADAY 732'NİN ŞUAYB SINAMASI — "
 "birinci nakarat STANDALONE; TAHMİN TUTTU** (elle, L1, aday 744)"),
}

M = {
181: ("Bölüt bir emir ve bir yasakla açılıyor: أَوْفُوا۟ ٱلْكَيْلَ وَلَا تَكُونُوا۟ مِنَ "
 "ٱلْمُخْسِرِينَ *(ölçüyü tam yapın, eksiltenlerden olmayın)*. **Ölçülebilir bir komşuluk "
 "yoğunluğu: كيل *(ölçme (hacim))* korpusta 16 geçişli ve dikey satırı ▸sonra قسطس *(kıstas, doğru "
 "terazi)* x661,4 · وزن *(tartı, mîzan)* x153,4 veriyor — OKUMADA GÖRÜLEN EN YÜKSEK KOMŞULUK "
 "KATI** (önceki rekor 26:173'ün x502,7'siydi). Ve **iki komşu da bu bölütte**: `وزن` ve `قسطاس` "
 "bir sonraki ayette. Üçlü korpusta neredeyse ayrılmaz; ölçü-tartı terkibi bu sûreye özgü değil. "
 "Sûrenin dört NEHY'inden üçüncüsü burada."),
182: ("Üç kelime ve okumada **ilk kez bir ölçü aracı adı**: بِٱلْقِسْطَاسِ ٱلْمُسْتَقِيمِ *(doğru "
 "teraziyle)*. قسطس *(kıstas, doğru terazi)* korpusta **iki** geçişli ve dikey ölçümü ▸önce كيل "
 "*(ölçme (hacim))* x554,4 veriyor, ▸sonra listesi boş — kökün korpusta tek bir yatağı var. Tek "
 "xref 17:35'e düşüyor ve terkip orada da aynı. **SINIR — ÇIPA DEĞERLENDİRMESİ: ayet bir ÖLÇÜ "
 "ARACINI adlandırıyor ve bir nitelik veriyor (مُسْتَقِيم *(dosdoğru)*), yani aday 561'in ölçütünde "
 "'adlandırma + nitelik' düzeyinde — 25:61 ve 26:63 ile aynı sınıf. AMA burada ölçü bir FİZİK "
 "büyüklüğü değil bir ADALET ölçütü; ne birim, ne yöntem, ne değer veriliyor. Ve olay ne biyolojik "
 "ne astronomik. Çıpa sayılmadı; ayet zaten yıldızsız.**"),
183: ("Yasak üç parçalı: eksiltme (بخس *(eksiltme, değerini düşürme)*), taşkınlık (عثو *(azgınlık, "
 "taşkınlık)*), bozgunculuk (فسد *(bozgunculuk, fesat)*). Üç 3-gram'ı 7:85 ve 11:85'e düşüyor — "
 "**donmuş kalıp adayı** (aday 437) ve iki ayet de Şuayb kıssasının başka sûrelerdeki anlatımı. "
 "عثو korpusta **beş** geçişli ve dikey ölçümü ▸sonra فسد x128,9 veriyor; فسد de ▸önce عثو x141,6 "
 "veriyor — **karşılıklı bağ, çift korpusta neredeyse ayrılmaz**. Ve فسد 26:152'den geri geliyor: "
 "orada Semûd'un ileri gelenlerinin niteliği, burada Eyke halkına yasak."),
184: ("Emir üçüncü kez ve gönderge üçüncü biçimde: 26:131'de فَٱتَّقُوا۟ ٱللَّهَ *(Allah'tan "
 "sakının)* — **lafız**; 26:132'de وَٱتَّقُوا۟ ٱلَّذِىٓ أَمَدَّكُم *(size yardım edenden sakının)* — "
 "**yardım eden**; burada وَٱتَّقُوا۟ ٱلَّذِى خَلَقَكُمْ *(sizi yaratandan sakının)* — **yaratan**. "
 "Aynı kök, aynı bab VIII, üç gönderge. Ve جبل *(dağ)* kökü burada **'nesil, yığın'** anlamında "
 "(ٱلْجِبِلَّةَ ٱلْأَوَّلِينَ *(önceki nesiller)*) — kök korpusta 41 geçişli ve dikey ölçümü ▸önce "
 "نحت *(yontma)* x108,3 · نجم *(yıldız)* x33,3 veriyor, yani ağırlıkla **dağ** anlamında; 26:149'da "
 "da 'dağ'dı. **Aynı sûrede iki anlam** (aday 714/724 sınıfı, 529 kümesine on altıncı vaka)."),
185: ("**Sûrenin altıncı ve en küçük nakarat kümesi kapandı: 2/2** (26:153, 185). Beş kelime, "
 "26:153 ile tam özdeş. Ölçülebilir bir simetri: iki geçiş de bir kavmin elçiye aynı suçlamayı "
 "yöneltmesi — Semûd (26:153) ve Eyke halkı (burada). **İki üyeli bir tekrarın 'nakarat' sayılıp "
 "sayılmayacağı hâlâ tanımsız** (aday 715) ve bu, sûrenin nakarat sayımını doğrudan etkiliyor."),
186: ("Suçlama iki parçalı ve ilk yarısı 26:154'ten birebir: مَآ أَنتَ إِلَّا بَشَرٌ مِّثْلُنَا "
 "*(sen ancak bizim gibi bir beşersin)*. **Değişen ikinci yarı:** orada bir talep (فَأْتِ "
 "بِـَٔايَةٍ *(bir âyet getir)*), burada bir zan bildirimi (وَإِن نَّظُنُّكَ لَمِنَ ٱلْكَٰذِبِينَ "
 "*(seni yalancılardan sanıyoruz)*). **Aynı ilk yarı, iki ayrı ikinci yarı** — ve `esit` bunu "
 "yakalamıyor. ظنن *(zan, sanma)* korpusta 69 geçişli. Dört kip işareti (NEG, RES, CERT, EMPH) "
 "tek ayette."),
187: ("Meydan okuma kalıbı **üçüncü kez** ve talep en somut biçimde: فَأَسْقِطْ عَلَيْنَا كِسَفا "
 "مِّنَ ٱلسَّمَآءِ *(üzerimize gökten parçalar düşür)*. Üç geçişin üçünde de إِن كُنتَ مِنَ "
 "ٱلصَّٰدِقِينَ *(doğru söyleyenlerdensen)*; talep değişiyor — 26:31 'getir onu' (zamir), 26:154 "
 "'bir âyet getir', burada 'gökten parça düşür'. **Somutluk artıyor.** سقط *(düşme, düşürme)* "
 "korpusta sekiz, كسف *(tutulma, parça)* beş geçişli ve **karşılıklı bağ**: سقط ▸sonra كسف x520,0, "
 "كسف ▸önce سقط x554,4 — iki seyrek kök birbirine kilitli. SINIR: ayet gökten bir düşüş **talep "
 "ediyor**, ne madde ne mekanizma ne ölçü tanımlıyor; 25:25 sınıfı."),
188: ("Cevap bilgiyi Rabbe havale ediyor: رَبِّى أَعْلَمُ بِمَا تَعْمَلُونَ *(Rabbim yaptıklarınızı "
 "daha iyi bilir)*. **Dış düğüm 4 — blokta ve sûrede en yüksek**; tek 3-gram dört ayete bağlanıyor "
 "(18:19, 18:22, 28:37, 28:85). Ölçülebilir bir üçlü: عمل *(iş, amel)* üç elçide üç tutum — Nûh "
 "26:112 'bilgim yok', Lût 26:168 'kızanlardanım', Şuayb burada 'Rabbim daha iyi bilir'. "
 "**Bilgisizlik / öfke / bilgiyi havale.** Ve fâsıla تَعْمَلُونَ; 26:112 ve 26:169'da يَعْمَلُونَ "
 "idi — aynı kök, şahıs değişiyor."),
189: ("**İki kök birden ikileniyor: عذب *(azap)* x2 ve يوم *(gün)* x2** — okumada ikinci vaka "
 "(birincisi 26:118'de فتح *(açma)* ve بين *(arası; açıklama)*). Ve عَذَابُ يَوْمٍ عَظِيمٍ *(büyük "
 "bir günün azabı)* sûrede **üçüncü** kez: 26:135 Hûd'un korkusu, 26:156 Sâlih'in tehdidi, burada "
 "Şuayb kıssasında **gerçekleşme**. Ölçülebilir bir kök tuzağı: ظلل *(sürüp gitme, olmayı "
 "sürdürme)* burada **'gölge'** anlamında (يَوْمِ ٱلظُّلَّةِ *(gölge günü)*), oysa 26:71'de "
 "**'sürdürme'** anlamındaydı — aynı sûrede iki anlam. Dikey ölçümü ▸sonra bulut x42,4 veriyor, "
 "yani 'gölge' anlamı komşulukta var."),
190: ("**Aday 732'nin Şuayb sınaması ve tahmin tuttu.** Birinci nakarat burada **standalone** "
 "(n=8, nakarat alanı 6) — gömülü değil. **Birinci küme tamamlandı: 6/6 standalone** (26:8, 67, "
 "103, 121, 174, 190) — artı iki gömülü vaka (26:139, 158) ki ölçüm alanı onları saymıyor "
 "(aday 707/720). **Tam tablo: çift Mûsâ/İbrâhîm/Nûh'ta bütün, Hûd/Sâlih'te kırık, Lût/Şuayb'da "
 "yine bütün** — kırıklık ardışık iki kıssada kümelenmiş ve iki yandan bütün kıssalarla "
 "çevrelenmiş. Ve fâsıladaki مُؤْمِن sûrenin on üçüncü artefaktı."),
}

ATLAMA = {
 "_mercek_26_188": ("26:188 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. قَالَ رَبِّى أَعْلَمُ بِمَا "
  "تَعْمَلُونَ. Tek kaynak rab z=3,94 (n=5, oran 0,20). İçerik bir bilgi havalesi."),
 "_blok_notu_26_181_190": ("BLOK BİLANÇOSU: ★★★ 1 (26:188) · ★★ 0 · ★ 0 · 9 ayet yıldızsız — "
  "26:71-80 ve 26:151-160 ile birlikte okumada en az yıldızlı bloklardan. Tek ★★★ kaynağı rab "
  "oranı. **ÇIPA DEĞERLENDİRMESİ — SÛRENİN EN GÜÇLÜ ADAY BÖLÜTÜ VE YİNE YILDIZSIZ:** 26:181-183 "
  "ölçü-tartı bölütü (كيل *(ölçme (hacim))* · وزن *(tartı, mîzan)* · قسطاس *(kıstas, doğru "
  "terazi)* · بخس *(eksiltme)*) ve 26:182 OKUMADA İLK KEZ BİR ÖLÇÜ ARACINI ADLANDIRIYOR + nitelik "
  "veriyor (مُسْتَقِيم *(dosdoğru)*) — aday 561'in 'adlandırma + nitelik' düzeyi, 25:61 ve 26:63 "
  "ile aynı sınıf. **AMA ölçü burada bir FİZİK büyüklüğü değil bir ADALET ölçütü; ne birim, ne "
  "yöntem, ne değer var. Ve olay ne biyolojik ne astronomik — aday 646'nın 'sınıf yok' gerekçesi "
  "de geçerli. ÇIPA SAYILMADI.** 26:187 (gökten parça düşürme talebi) de 25:25 sınıfı: olay "
  "adlandırılıyor, ölçü yok. **DÖRT AYET (181, 182, 183, 187) ÇIPA TAŞIYABİLECEK BÖLÜTTE VE "
  "DÖRDÜ DE YILDIZSIZ** — aday 599/602 tablosuna eklendi. SÛRE 26'NIN OKUNAN 190 AYETİNDE ★★★ 39."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(181, 191):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 190/227.** Devam: 26:191'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-190 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1912
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(181, 191):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
