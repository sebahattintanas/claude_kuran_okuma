# -*- coding: utf-8 -*-
"""blok_21_41_60.py — Enbiyâ 41-60 bloğunun okuma kaydını dosyalara yazar."""
import json

DIK = json.load(open('blok_dikey_21_41_60.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
41: "Andolsun, senden önceki elçilerle de alay edildi; sonra alay edenleri, alaya aldıkları şey kuşatıverdi.",
42: "De ki: Gece gündüz sizi Rahmân'dan kim koruyabilir? Hayır, onlar Rablerinin zikrinden yüz çeviriyorlar.",
43: "Yoksa onların, kendilerini bize karşı savunacak ilâhları mı var? Onlar kendilerine bile yardım edemezler; bizden yana da korunmazlar.",
44: "Doğrusu biz onları da atalarını da, ömür kendilerine uzun gelinceye kadar geçindirdik. Görmüyorlar mı ki biz yere gelip onu uçlarından eksiltiyoruz? Üstün gelen onlar mı?",
45: "De ki: Ben sizi ancak vahiyle uyarıyorum. Ama sağırlar, uyarıldıklarında çağrıyı işitmez.",
46: "Rabbinin azabından bir esinti onlara dokunuverse, hiç şüphesiz \"Eyvah bize, biz gerçekten zalimmişiz\" derler.",
47: "Kıyamet günü için adalet terazilerini kurarız; hiçbir nefse zerrece haksızlık edilmez. Bir hardal tanesi ağırlığında bile olsa onu getiririz. Hesap görücü olarak biz yeteriz.",
48: "Andolsun, Mûsâ ile Hârûn'a furkanı — takvâ sahipleri için bir ışık ve bir zikir — verdik.",
49: "Onlar ki Rablerinden, görmedikleri hâlde haşyet duyarlar ve o saatten titrerler.",
50: "Bu da indirdiğimiz mübarek bir zikirdir. Şimdi siz onu inkâr mı ediyorsunuz?",
51: "Andolsun, daha önce İbrâhim'e de rüşdünü vermiştik; biz onu biliyorduk.",
52: "Hani babasına ve kavmine, \"Başında durup durduğunuz bu heykeller nedir?\" demişti.",
53: "\"Atalarımızı bunlara kulluk eder bulduk\" dediler.",
54: "\"Andolsun, siz de atalarınız da apaçık bir sapkınlık içindeymişsiniz\" dedi.",
55: "\"Sen bize hakkı mı getirdin, yoksa oyun oynayanlardan mısın?\" dediler.",
56: "Dedi ki: Hayır, Rabbiniz göklerin ve yerin Rabbidir; onları yarıp var edendir. Ben de buna şahitlik edenlerdenim.",
57: "Allah'a yemin olsun ki, siz arkanızı dönüp gittikten sonra putlarınıza bir tuzak kuracağım.",
58: "Derken onları paramparça etti; yalnız onların büyüğünü bıraktı — belki ona dönerler diye.",
59: "\"İlâhlarımıza bunu kim yaptı? O gerçekten zalimlerden biri\" dediler.",
60: "\"İbrâhim denen bir genci, onları diline dolarken işittik\" dediler.",
}

OLCUM = {
41: "eksen: lafız yok, Rab yok, esmâ yok · aktör: yok · edim haber, kip EMPH 1 · CERT 1 (لَقَدْ *(andolsun ki)*) · şahıs 3MS ×3 · 2MS 1 · 3MP ×7 · n=13 mora=67 harf=60, fâsıla يَسْتَهْزِءُونَ *(alaya alıyorlar)* → ن, N sınıfı; i'râb GEN 2; bab I ×3 · bab X ×2; edilgen 1 (ٱسْتُهْزِئَ *(alay edildi)*); kök ikilemesi هزأ *(alay etme)* ×2 — biri edilgen biri etken; simetri [3,7,10,1] · kökler هزأ *(alay etme)* · رسل *(gönderme, elçi)* · قبل *(ön, önce; kabul)* · حيق *(kuşatma, başına gelme)* · سخر *(alay etme; boyun eğdirme)* · كون *(olmak)* · bağ: **tam-ayet ikizi 6:10** (birebir aynı) · xref beş ayrı 3-gram, hepsi 6:10'a, biri 13:32'ye",
42: "eksen: lafız yok · Rab 12. sırada رَبّ *(Rab)*, ذِكْرِ رَبِّهِم *(Rablerinin zikri)* terkîbinde (rab z=1.32) · **esmâ رَحْمٰن *(Rahmân)* 7. sırada, orta konum** (bağlam denetlendi: ilâhî ad, yanlış pozitif değil) · aktör: yok · edim emir, kip IMPV 1 · şahıs 2MS 1 · 3MS 1 · 2MP 1 · 3MP ×2 · n=13 mora=59 harf=50, fâsıla مُّعْرِضُونَ *(yüz çevirenler)* → ن, N; i'râb GEN 5 · NOM 1; bab I ×2; **hapaks كلأ *(koruma, gözetme)* — korpusta tek geçiş (z=3.38)**; biçim IDRAB (بَلْ *(hayır, bilakis)*) · yıldız ★★★ · bağ: 21:20 ve 21:33 ile ortak ليل *(gece)*/نهر *(ırmak; gündüz)* çifti (elle, L2)",
43: "eksen: yok · aktör: yok · edim haber (ayet أَمْ *(yoksa)* ile açılıyor, soru kipi verilmedi — ÖLÇÜM ARTEFAKTI, aday 438), kip NEG 2 · şahıs 3MP ×8 · 3FS 1 · 1P ×2 · n=14 mora=71 harf=58, fâsıla يُصْحَبُونَ *(korunurlar, eşlik edilir)* → ن, N; i'râb NOM 1 · GEN 2 · ACC 1; bab I ×2 · bab X ×1; edilgen 1 (يُصْحَبُونَ, z=1.57); simetri [3,1,11,1] · yıldız ★ · kökler أله *(ilâh)* · منع *(engelleme, alıkoyma)* · دون *(beriki, başkası)* · طوع *(güç yetirme, itaat)* · نصر *(yardım)* · نفس *(nefis, can)* · صحب *(arkadaşlık, sahiplik)* · bağ: xref ٱسْتَطَاعَ … نَصْرَ … نَفْس *(güç yetirme… yardım… nefs)* → 7:192 ve 7:197",
44: "eksen: yok · aktör: yok · edim soru, kip INTG 2 · NEG 1 — iki soru (أَفَلَا يَرَوْنَ *(görmüyorlar mı)* · أَفَهُمُ ٱلْغَٰلِبُونَ *(üstün gelen onlar mı)*) · şahıs 1P ×5 · 3MP ×5 · 3MS 1 · 3FS ×2 · n=18 mora=109 harf=84 — **bloğun en uzun ayeti (mora)**, fâsıla ٱلْغَٰلِبُونَ *(üstün gelenler)* → ن, N; i'râb ACC 3 · NOM 2 · GEN 1; bab I ×4 · bab II ×1; biçim IDRAB + DIKKAT; simetri [3,1,5,1] · kökler متع *(geçimlik, faydalandırma)* · أبو *(baba)* · طول *(uzunluk)* · عمر *(ömür; imar etme)* · رأي *(görme)* · أتي *(gelme, getirme)* · أرض *(yer, yeryüzü)* · نقص *(eksiltme, azaltma)* · طرف *(uç, kenar; göz kırpma)* · غلب *(üstün gelme, galibiyet)* · bağ: xref رأي … أتي … أرض … نقص … طرف *(görme… gelme… yer… eksiltme… uç)* → 13:41 (üç ayrı 3-gram, tek ayete)",
45: "eksen: yok · aktör: yok · edim emir, kip IMPV 1 · NEG 1 · şahıs 2MS 1 · 1S 1 · 2MP 1 · 3MS 1 · 3MP ×2 · n=11 mora=62 harf=47, fâsıla يُنذَرُونَ *(uyarılırlar)* → ن, N; i'râb ACC 2 · GEN 1 · NOM 1; bab I ×3 · bab IV ×1; edilgen 1 (يُنذَرُونَ); kök ikilemesi نذر *(uyarı; adak)* ×2 — biri etken 1S, öteki edilgen 3MP · kökler قول *(söz söyleme)* · نذر *(uyarı; adak)* · وحي *(vahiy, gizli bildirim)* · سمع *(işitme)* · صمم *(sağırlık)* · دعو *(çağırma, dua)* · bağ: xref yok",
46: "eksen: lafız yok · Rab 6. sırada, عَذَابِ رَبِّكَ *(Rabbinin azabı)* terkîbinde (**rab z=1.62 — bloğun en yüksek ikinci Rab yoğunluğu**) · aktör: yok · edim nida + şart, kip EMPH ×3 · COND 1 · VOC 1 · şahıs 3FS 1 · 3MP ×2 · 2MS 1 · 1P ×4 · n=11 mora=65 harf=46, fâsıla ظَٰلِمِينَ *(zalimler)* → ن, N; i'râb NOM 2 · GEN 2 · ACC 2; bab I ×3; **hapaks نفح *(esinti, hafif dokunuş)* — korpusta tek geçiş (z=3.38)** · yıldız ★★★ · bağ: **sûre içi tekrar 21:14** (aynı قول *(söz söyleme)* · كون *(olmak)* · ظلم *(zulüm)* üçlüsü, önceki blokta kayıtlıydı) · xref قول … كون … ظلم → 7:5 ve 21:14 · ربب … قول … كون *(Rab… söz… olma)* → 29:10",
47: "eksen: yok · aktör: yok · edim şart, kip NEG 1 · COND 1 · şahıs 1P ×4 · 3FS ×2 · 3MS ×2 · n=20 mora=100 harf=85 — bloğun en uzun ikinci ayeti, fâsıla حَٰسِبِينَ *(hesap görücüler)* → ن, N; i'râb ACC 5 · GEN 4 · NOM 1; bab I ×5 · kökler وضع *(koyma, indirme)* · وزن *(tartı, mîzan)* · قسط *(kıst, adalet; sapma)* · يوم *(gün)* · قوم *(kalkma; kavim; kıyamet)* · ظلم *(zulüm)* · نفس *(nefis, can)* · شيأ *(dileme; şey)* · ثقل *(ağırlık, miskal)* · حبب *(sevgi; tane)* · خردل *(hardal (tanesi))* · أتي *(gelme, getirme)* · كفي *(yetme)* · حسب *(hesap, sayma)* · bağ: xref ظلم … نفس … شيأ *(zulüm… nefs… şey)* → 36:54 · كون … ثقل … حبب … خردل *(olma… ağırlık… tane… hardal)* → 31:16",
48: "eksen: yok · aktör: **adlı İKİ aktör** — مُوسَى *(Mûsâ)* 3. sırada (rol fâil) ve هارُون *(Hârûn)* 4. sırada (rol mef'ûl) · edim haber, kip EMPH 1 · CERT 1 · şahıs 1P ×2 — ayette yalnız TEK şahıs · n=8 mora=65 harf=45, fâsıla لِّلْمُتَّقِينَ *(takvâ sahipleri için)* → ن, N; i'râb NOM 1 · ACC 4 · GEN 1; bab IV ×1 (tek fiil) · kökler أتي *(gelme, getirme; verme)* · فرق *(ayırma; furkan)* · ضوأ *(ışık, aydınlık)* · ذكر *(anma, zikir)* · وقي *(sakınma, takvâ)* · bağ: xref yok",
49: "eksen: lafız yok · Rab 3. sırada, رَبَّهُم *(Rableri)* (**rab z=2.34 — bloğun en yüksek Rab yoğunluğu**) · aktör: yok · edim haber · şahıs 3MP ×4 · **iltifât VAR: 1>3** (önceki ayetin 1P anlatıcısından 3MP'ye) · n=8 mora=46 harf=37, fâsıla مُشْفِقُونَ *(titreyenler)* → ن, N; i'râb ACC 1 · GEN 2 · NOM 1; bab I ×1 · yıldız ★★ · kökler خشي *(haşyet, saygıyla korkma)* · ربب *(rab, terbiye etme)* · غيب *(gayb)* · سوع *(saat, vakit)* · شفق *(şafak; işfak, içi titreyerek korkma)* · bağ: xref خشي … ربب … غيب *(haşyet… Rab… gayb)* → 35:18 ve 67:12",
50: "eksen: yok · aktör: yok · edim soru, kip INTG 1 · şahıs 1P ×2 · 3MS ×2 · 2MP 1 · n=7 mora=42 harf=35, fâsıla مُنكِرُونَ *(inkâr edenler)* → ن, N; i'râb NOM 3 — tamamı NOM; bab IV ×1; biçim DIKKAT · kökler ذكر *(anma, zikir)* · برك *(bereket, mübarek kılma)* · نزل *(indirme)* · نكر *(tanımama, inkâr; münker)* · bağ: 21:24 ile ortak ذكر (elle, L2)",
51: "eksen: yok · **esmâ عالِم *(bilen)* 9. sırada — ŞÜPHELİ, bağlam denetimine alındı** (عَٰلِمِينَ, 1P çoğul haber; esmâ-i hüsnâ maddesi mi yoksa yüklem mi belirsiz — aday 414 doğrulama kümesine eklendi) · aktör: adlı إِبْراهِيم *(İbrâhim)* 3. sırada, rol mef'ûl — **sûrenin İbrâhim kıssası burada açılıyor** · edim haber, kip EMPH 1 · CERT 1 · şahıs 1P ×4 · 3MS ×2 · n=9 mora=48 harf=39, fâsıla عَٰلِمِينَ *(bilenler)* → ن, N; i'râb ACC 3 · GEN 1; bab I ×1 · bab IV ×1 · kökler أتي *(gelme, getirme; verme)* · رشد *(doğruyu bulma, rüşd)* · قبل *(ön, önce; kabul)* · كون *(olmak)* · علم *(bilme)* · bağ: 21:48 ile ortak kalıp (وَلَقَدْ ءَاتَيْنَا *(andolsun verdik)*, elle, L3)",
52: "eksen: yok · aktör: yok (İbrâhim adı geçmiyor, 3MS zamirle taşınıyor) · edim haber · şahıs 3MS ×3 · 2MP 1 · 3FS 1 · n=11 mora=60 harf=45, fâsıla عَٰكِفُونَ *(başında duranlar)* → ن, N; i'râb GEN 2 · NOM 2; bab I ×1; biçim DIKKAT; simetri [3,5,8,1] · kökler قول *(söz söyleme)* · أبو *(baba)* · قوم *(kalkma; kavim; kıyamet)* · مثل *(benzer, misil; heykel)* · عكف *(başında durma, ikâf)* · bağ: xref yok",
53: "eksen: yok · aktör: yok · edim haber · şahıs 3MP ×2 · 1P ×3 · 3FS 1 · n=5 mora=39 harf=26 — **bloğun en kısa ayeti**, fâsıla عَٰبِدِينَ *(kulluk edenler)* → ن, N; i'râb ACC 2; bab I ×2 · kökler قول *(söz söyleme)* · وجد *(bulma)* · أبو *(baba)* · عبد *(kul, kulluk)* · bağ: xref yok",
54: "eksen: yok · **esmâ مُبِين *(apaçık)* 8. sırada — ÖLÇÜM ARTEFAKTI (aday 414)**: burada ضَلَٰلٍۢ مُّبِينٍۢ *(apaçık sapkınlık)* terkîbinde SIFAT, ilâhî ad değil · aktör: yok · edim haber, kip EMPH 1 · CERT 1 · şahıs 3MS 1 · 2MP ×4 · n=8 mora=43 harf=33, fâsıla مُّبِينٍۢ *(apaçık)* → ن, N; i'râb NOM 1 · GEN 2; bab I ×2 · kökler قول *(söz söyleme)* · كون *(olmak)* · أبو *(baba)* · ضلل *(sapma, saptırma)* · بين *(arası; açıklama)* · bağ: xref قول … كون … أبو *(söz… olma… baba)* → 9:24",
55: "eksen: yok · aktör: yok · edim soru, kip INTG 1 · şahıs 3MP ×2 · 2MS ×3 · 1P 1 · n=7 mora=39 harf=31, fâsıla ٱللَّٰعِبِينَ *(oyun oynayanlar)* → ن, N; i'râb GEN 2; bab I ×2; ayet içi أَمْ *(yoksa)* — bu kez muttasıla (seçenek bağlayıcı), INTG hemzesi zaten var · kökler قول *(söz söyleme)* · جيأ *(gelme, getirme)* · حقق *(hak, gerçek)* · لعب *(oyun, oynama)* · bağ: xref قول … جيأ … حقق *(söz… gelme… hak)* → 17:81 ve 34:49",
56: "eksen: lafız yok · **Rab İKİ geçiş, 3. ve 4. sırada** — رَبُّكُمْ رَبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ *(Rabbiniz göklerin ve yerin Rabbidir)* (**rab z=2.96 — sûrede ölçülen en yüksek Rab yoğunluğu**) · aktör: yok · edim haber · şahıs 3MS ×2 · 2MP 1 · 3FP 1 · 1S 1 · n=13 mora=67 harf=53, fâsıla ٱلشَّٰهِدِينَ *(şahitlik edenler)* → ن, N; i'râb NOM 2 · GEN 3; bab I ×2; kök ikilemesi ربب *(rab, terbiye etme)* ×2; biçim IDRAB (بَل *(hayır, bilakis)*); simetri [3,7,10,1] · yıldız ★★ · kökler قول *(söz söyleme)* · ربب *(rab, terbiye etme)* · سمو *(ad; gök)* · أرض *(yer, yeryüzü)* · فطر *(yarma; yaratma-fıtrat)* · شهد *(şahitlik)* · bağ: xref قول … ربب … ربب … سمو *(söz… Rab… Rab… gök)* → 18:14 ve 26:26",
57: "eksen: **Allah lafzı ayet-içi 1. sırada — ayetin İLK kelimesi**, وَتَٱللَّهِ *(Allah'a yemin olsun)* yemin kalıbında (allah z=2.33) · Rab yok · esmâ yok · aktör: yok (konuşan İbrâhim, adı geçmiyor) · edim haber, kip EMPH ×2 (تَـ yemin edatı + لَـ + نَّ te'kid nûnu) — **biçim alanı BOŞ: QASEM etiketi VERİLMEDİ, ÖLÇÜM ARTEFAKTI (aday 443)** · şahıs 1S 1 · 2MP ×3 · n=7 mora=42 harf=35, fâsıla مُدْبِرِينَ *(arkalarını dönenler)* → ن, N; i'râb GEN 1 · ACC 3; bab I ×1 · bab II ×1; zaman IMPF ×2 · yıldız ★★ · kökler أله *(ilâh; lafza-i celâl)* · كيد *(tuzak, düzen)* · صنم *(put, sanem)* · بعد *(sonra; uzaklık)* · ولي *(dost, veli; velâyet)* · دبر *(arka; tedbir)* · bağ: xref yok",
58: "eksen: lafız yok · **esmâ كَبِير *(büyük)* 4. sırada — ÖLÇÜM ARTEFAKTI (aday 414)**: burada كَبِيرًۭا لَّهُمْ *(onların büyüğü)*, yani putların en büyüğü; ilâhî ad değil, üstelik tam KARŞIT bağlamda · aktör: yok · edim haber, kip RES 1 · şahıs 3MS ×2 · 3MP ×5 · **iltifât VAR: 12>3** · n=8 mora=55 harf=37, fâsıla يَرْجِعُونَ *(dönerler)* → ن, N; i'râb ACC 3; bab I ×2; biçim HASR (إِلَّا *(ancak, -den başka)*) · kökler جعل *(kılma, var etme)* · جذذ *(parça parça etme, kırıp dökme)* · كبر *(büyüklük; büyüklenme)* · رجع *(dönme, geri döndürme)* · bağ: xref yok",
59: "eksen: yok · aktör: yok · edim haber, kip EMPH 1 · şahıs 3MP ×2 · 3MS ×2 · 1P 1 · n=8 mora=45 harf=36, fâsıla ٱلظَّٰلِمِينَ *(zalimler)* → ن, N; i'râb GEN 2 · ACC 1; bab I ×2; biçim DIKKAT · kökler قول *(söz söyleme)* · فعل *(yapma, işleme)* · أله *(ilâh)* · ظلم *(zulüm)* · bağ: 21:29 ve 21:46 ile ortak ٱلظَّٰلِمِينَ fâsılası (elle, L2)",
60: "eksen: yok · aktör: adlı إِبْراهِيم *(İbrâhim)* 7. sırada, rol fâil — **ad bu kez FÂSILA konumunda** · edim haber · şahıs 3MP ×3 · 1P ×2 · 3MS ×3 · n=7 mora=43 harf=34, **fâsıla إِبْرَٰهِيمُ *(İbrâhim)* → م, N sınıfı** — sûrenin 112 fâsılasından 6'sı م, bu ikincisi (öteki beş: 21:4, 62, 66, 69, 76); kafiye sınıfı DEĞİŞMEDİ, kırılma yok; i'râb GEN 1 · NOM 1; bab I ×4; edilgen 1 (يُقَالُ *(denilir)*); kök ikilemesi قول *(söz söyleme)* ×2 — biri etken 1P, öteki edilgen 3MS · kökler قول *(söz söyleme)* · سمع *(işitme)* · فتي *(genç, delikanlı; fetva)* · ذكر *(anma, zikir)* · bağ: xref yok",
}

MERCEK = {
41: "Aynı kök iki kez, iki çatıda: ٱسْتُهْزِئَ *(alay edildi)* edilgen ve failsiz, يَسْتَهْزِءُونَ *(alaya alıyorlar)* etken ve failli. Aradaki فَحَاقَ *(kuşatıverdi)* ise özneyi tersine çeviriyor: alay edilen değil, alayın KENDİSİ özne oluyor (مَّا كَانُوا۟ بِهِۦ يَسْتَهْزِءُونَ *(alaya aldıkları şey)*). Cümle böylece failliği iki kez devrediyor. Ayetin tamamı 6:10 ile birebir aynı — kalıbın kendisi taşınabilir.",
42: "Soru bir koruma arıyor ve koruyucunun yerine korunulacak olanı koyuyor: مِنَ ٱلرَّحْمَٰنِ *(Rahmân'dan)*. Fiil كلأ *(koruma, gözetme)* korpusta yalnız burada geçiyor — soru, bir defalık bir kelimeyle soruluyor. Zaman kapsamı بِٱلَّيْلِ وَٱلنَّهَارِ *(gece ve gündüz)* ile veriliyor; bu çift sûrede üçüncü kez, ama her seferinde başka bir sözdizimsel rolde. Kapanış بَلْ *(hayır, bilakis)* soruyu cevapsız bırakıp yüz çevirmeye geçiyor.",
43: "İki ilâh iddiası, iki yetersizlik. Birinci cümle onlara bir işlev veriyor: تَمْنَعُهُم *(onları savunur)*. İkinci cümle işlevi geri alıyor ve nesneyi değiştiriyor: لَا يَسْتَطِيعُونَ نَصْرَ أَنفُسِهِمْ *(kendilerine bile yardım edemezler)* — savunulacak olan artık taraftarlar değil ilâhların kendisi. Üçüncü cümle edilgene geçiyor: وَلَا هُم مِّنَّا يُصْحَبُونَ *(bizden yana korunmazlar)*. Etken yetersizlikten edilgen korunmasızlığa üç adımda iniliyor.",
44: "Ayet iki karşıt hareketi üst üste koyuyor: مَتَّعْنَا … حَتَّىٰ طَالَ عَلَيْهِمُ ٱلْعُمُرُ *(geçindirdik… ömür uzun gelinceye kadar)* — uzama; ve نَنقُصُهَا مِنْ أَطْرَافِهَآ *(uçlarından eksiltiyoruz)* — kısalma. Birincisi zamanda, ikincisi mekânda. İkisinin de öznesi aynı 1P. Kapanış soru غلب *(üstün gelme, galibiyet)* köküyle geliyor: uzayan ile eksilenin arasında hangisinin üstün olduğu soruluyor.",
45: "Uyarı ile işitme arasına bir engel konuyor. Uyarının aracı tek ve sınırlı: إِنَّمَآ أُنذِرُكُم بِٱلْوَحْىِ *(sizi ancak vahiyle uyarıyorum)* — HASR işlevli إِنَّمَا. Karşı taraf ise duyu düzeyinde tanımlanıyor: ٱلصُّمُّ *(sağırlar)*. Aynı kök نذر *(uyarı; adak)* ayetin iki ucunda: başta etken ve 1S (uyaran), sonda edilgen ve 3MP (uyarılan). Etkiye açık taraf yok.",
46: "Nicelik ile tepki arasında bir orantısızlık kuruluyor. Uyaran en küçük: نَفْحَةٌۭ *(bir esinti)* — dişil, tekil, ve مِّنْ *(-den)* ile azlık bildiren bir parça (مِّنْ عَذَابِ رَبِّكَ *(Rabbinin azabından)*). Tepki en büyük: üç te'kid üst üste (لَـ + نَّ + إِنَّ) ve bir nidâ (يَٰوَيْلَنَآ *(eyvah bize)*). Kelime نفح *(esinti, hafif dokunuş)* korpusta tek geçişli; en az ölçülen nicelik en çok pekiştirilen cümleyi çekiyor.",
47: "Ölçme aleti önce kuruluyor (نَضَعُ ٱلْمَوَٰزِينَ ٱلْقِسْطَ *(adalet terazilerini kurarız)*), sonra çözünürlüğü tarif ediliyor: فَلَا تُظْلَمُ نَفْسٌۭ شَيْـًۭٔا *(hiçbir nefse zerrece haksızlık edilmez)*, ardından مِثْقَالَ حَبَّةٍۢ مِّنْ خَرْدَلٍ *(bir hardal tanesi ağırlığı)*. Üç adımda ölçek daralıyor: terazi → nefis → tane. Kapanış aleti değil ölçeni öne çıkarıyor: وَكَفَىٰ بِنَا حَٰسِبِينَ *(hesap görücü olarak biz yeteriz)*.",
48: "Tek fiil (ءَاتَيْنَا *(verdik)*), iki mef'ûl kişi (مُوسَىٰ وَهَٰرُونَ *(Mûsâ ve Hârûn)*), üç mef'ûl nesne (ٱلْفُرْقَانَ وَضِيَآءًۭ وَذِكْرًۭا *(furkan, ışık ve zikir)*). Verilen şey üç adla anılıyor ama tek nesne; üçü de ACC ve aynı fiile bağlı. Son ad ذِكْرًۭا *(zikir)* iki ayet sonra 21:50'de bu kez indirilen kitap için kullanılacak — aynı kelime, iki ayrı gönderge.",
49: "İki korku adı yan yana ama farklı yönde: خشي *(haşyet, saygıyla korkma)* fiil ve nesnesi رَبَّهُم *(Rableri)*; شفق *(şafak; işfak, içi titreyerek korkma)* ism-i fâil ve kaynağı ٱلسَّاعَةِ *(o saat)*. Biri kişiye, öteki olaya yöneliyor. Aradaki بِٱلْغَيْبِ *(görmedikleri hâlde)* ise ikisinin de görme dışında kaldığını söylüyor. Şahıs bir önceki ayetten 3MP'ye kayıyor (iltifât 1>3).",
50: "Ayetin i'râbı tamamen NOM: üç isim de merfû (ذِكْرٌۭ مُّبَارَكٌ *(mübarek bir zikir)* ve devamı). Yani cümle bir eylem değil bir tanım kuruyor. Fiil tek ve arkadan geliyor: أَنزَلْنَٰهُ *(onu indirdik)*. Kapanış soru هَٰذَا *(bu)* işaretini karşıya çeviriyor: أَفَأَنتُمْ لَهُۥ مُنكِرُونَ *(siz onu inkâr mı ediyorsunuz)* — tanım ile inkâr aynı nesneye bağlanıyor.",
51: "Kıssanın açılışı bir önceki kalıbı tekrarlıyor: 21:48'deki وَلَقَدْ ءَاتَيْنَا *(andolsun verdik)* burada aynen dönüyor, yalnız mef'ûl değişiyor — orada ٱلْفُرْقَانَ *(furkan)*, burada رُشْدَهُۥ *(rüşdü)*. İkisi de bir ayırt etme kabiliyeti adı. Ayet ayrıca zaman koyuyor: مِن قَبْلُ *(daha önce)* — Mûsâ-Hârûn anlatısından öncesine. Kapanış cümlesi bilgiye ait: وَكُنَّا بِهِۦ عَٰلِمِينَ *(biz onu biliyorduk)*, 1P ve geçmiş sürekli.",
52: "Soru bir tanım isteği: مَا هَٰذِهِ ٱلتَّمَاثِيلُ *(bu heykeller nedir)*. Sorulan şey zaten adlandırılmış (تَمَاثِيل *(heykeller)*, مثل *(benzer, misil; heykel)* kökünden — yani 'benzetilmiş şeyler'), dolayısıyla soru adı değil statüyü hedefliyor. Muhatap ikili: لِأَبِيهِ وَقَوْمِهِۦ *(babasına ve kavmine)* — biri tekil akrabalık, öteki çoğul topluluk, ikisi de aynı harf-i cere bağlı.",
53: "Cevap soruyu karşılamıyor, yerine bir tanıklık koyuyor: وَجَدْنَآ ءَابَآءَنَا *(atalarımızı bulduk)*. Yani statü sorusuna bir gözlem cümlesiyle karşılık veriliyor. Beş kelimede iki fiil, ikisi de PERF; özne 1P, nesne ءَابَآء *(atalar)*. Kulluğun kendisi ism-i fâille (عَٰبِدِينَ *(kulluk edenler)*) bir hâl olarak veriliyor, fiil olarak değil.",
54: "Karşı cevap, önceki ayetin öznesini genişletiyor: onlar 'atalarımız' demişti, bu ayet أَنتُمْ وَءَابَآؤُكُمْ *(siz ve atalarınız)* diyerek konuşanı da kapsama alıyor. Zaman da geriye çekiliyor: لَقَدْ كُنتُمْ *(andolsun… idiniz)*, PERF — hâl değil geçmiş hüküm. Hüküm tek terkiple veriliyor: ضَلَٰلٍۢ مُّبِينٍۢ *(apaçık sapkınlık)*.",
55: "Soru iki şıklı: أَجِئْتَنَا بِٱلْحَقِّ أَمْ أَنتَ مِنَ ٱللَّٰعِبِينَ *(hakkı mı getirdin, yoksa oyun oynayanlardan mısın)*. İki şık aynı düzlemde değil: birincisi bir fiil (getirme), ikincisi bir aidiyet (oyunculardan olma). Yani soru eylem ile kimlik arasında seçim yaptırıyor. أَمْ *(yoksa)* burada muttasıla — 21:21 ve 21:43'teki ayet-başı munkatı'a أَمْ'den farklı işlevde, aynı sûrede iki kullanım yan yana duruyor.",
56: "Cevap soruyu reddedip (بَل *(hayır, bilakis)*) yerine bir zincir kuruyor: رَبُّكُمْ رَبُّ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ *(Rabbiniz göklerin ve yerin Rabbidir)* — aynı kelime iki kez, birincisi muhataba bağlı (iyelik), ikincisi kapsama bağlı (izafet). Muhatabın Rabbi ile göğün Rabbi tek adımda eşitleniyor. Üçüncü hamle fiil: ٱلَّذِى فَطَرَهُنَّ *(onları yarıp var eden)*, 3FP zamir — gökleri işaret ediyor. Kapanış konuşanı tanığa çeviriyor: مِّنَ ٱلشَّٰهِدِينَ *(şahitlik edenlerden)*.",
57: "Ayet lafızla açılıyor ve lafız bir yemin edatına bitişik: وَتَٱللَّهِ *(Allah'a yemin olsun)*. Yeminin içeriği bir eylem vaadi (لَأَكِيدَنَّ *(mutlaka tuzak kuracağım)*), zamanı ise muhatabın hareketine bağlanıyor: بَعْدَ أَن تُوَلُّوا۟ مُدْبِرِينَ *(arkanızı dönüp gittikten sonra)*. Yani yemin, tanığın yokluğuna koşullu. Şahıs karşıtlığı keskin: tek 1S'e karşı üç 2MP.",
58: "Sonuç iki parçaya bölünüyor: جُذَٰذًا *(paramparça)* — hepsi; إِلَّا كَبِيرًۭا لَّهُمْ *(onların büyüğü hariç)* — istisna. HASR burada yıkımın değil, bırakılanın altını çiziyor. Bırakma gerekçesi de veriliyor: لَعَلَّهُمْ إِلَيْهِ يَرْجِعُونَ *(belki ona dönerler)* — dönüş zamiri bırakılan nesneye bağlı. Ayet ayrıca şahsı kaydırıyor (iltifât 12>3).",
59: "Soru fail arıyor: مَن فَعَلَ هَٰذَا *(bunu kim yaptı)*. Ama cevap beklenmeden hüküm veriliyor: إِنَّهُۥ لَمِنَ ٱلظَّٰلِمِينَ *(o gerçekten zalimlerden)* — fail bilinmeden sınıfı belirleniyor. Aynı fâsıla ٱلظَّٰلِمِينَ *(zalimler)* sûrede 21:29'da hüküm verenin, 21:46'da hüküm giyenin ağzındaydı; burada üçüncü bir ağızda ve yanlış hedefte.",
60: "Bilgi kulaktan geliyor ve iki katmanlı aktarılıyor: سَمِعْنَا *(işittik)* birinci elden, يُقَالُ لَهُۥٓ إِبْرَٰهِيمُ *(ona İbrâhim denir)* ikinci elden ve edilgen. Aynı kök قول *(söz söyleme)* iki kez: biri edilgen (adlandırma), öteki mastarsız. Ad, ayetin fâsılası olarak duruyor — sûrenin baskın ن kafiyesi bu ayette م'e geçiyor, ama sınıf değişmiyor: adın kendisi kafiyeye uyuyor.",
}

BIYOLOG = {
42: None,
46: None,
}
UZAY = {
42: "Çıpa: بِٱلَّيْلِ وَٱلنَّهَارِ *(gece ve gündüz)*. Bu ayette çift, cisim olarak değil SÜRE olarak kullanılıyor — harf-i cer بـ ile mecrur, yani kapsam bildiriyor ('gece boyunca ve gündüz boyunca'). Karşılaştırma aynı sûrenin içinde ölçülebiliyor: 21:33'te aynı iki kelime ACC ve yaratma fiilinin nesnesi, yanında شَّمْس *(güneş)* ve قَمَر *(ay)* var; burada iki cisim de yok. Yani gece-gündüz burada gökyüzü nesnesi değil, kesintisiz zaman ekseni. **Ölçüm sınırı:** ayette başka hiçbir gök öğesi geçmiyor; bu mercek yalnız bu tek çiftin sözdizimsel rolüne dayanıyor, daha ileri gitmiyor.",
46: None,
}

om = json.load(open('okuma_metni.json', encoding='utf-8'))
mk = json.load(open('mercek_kayit.json', encoding='utf-8'))

for n in range(41, 61):
    key = "21:%d" % n
    om['21'][key] = {'ar': AR[(21, n)], 'meal': MEAL[n], 'olcum': OLCUM[n],
                     'mercek': MERCEK[n], 'dikey': DIK[key]}
    if BIYOLOG.get(n): om['21'][key]['biyolog'] = BIYOLOG[n]
    if UZAY.get(n):    om['21'][key]['uzay'] = UZAY[n]
    mk['21'].append([key, MERCEK[n]])

for n, t in UZAY.items():
    if t: mk['21_uzay'].append(["21:%d" % n, t])

om['21']['_mercek_atlama_notu'] = (
 "★★★ ayetlerde atlanan uzman mercekleri (OKUMA_STANDARDI 2026-08-24, madde 3 — "
 "çıpası olmayan mercek YAZILMAZ): "
 "21:23 biyolog ve uzay ATLANDI (kökler سأل *(sorma, isteme)* ve فعل *(yapma, işleme)*; "
 "canlılık/gök öğesi yok). "
 "21:42 biyolog ATLANDI (canlılık öğesi yok); uzay YAZILDI (ليل *(gece)*/نهر *(ırmak; gündüz)* çifti). "
 "21:46 biyolog ve uzay ATLANDI (نفح *(esinti, hafif dokunuş)* ve مسس *(dokunma, temas)* fiziksel "
 "temas bildiriyor ama canlılık ya da gök çıpası kurmuyor; zorlama çıpa yapılmadı).")

om['ilerleme']['kismi']['21'] = "1-60 ayet düzeyinde"
om['ilerleme']['bekleyen']['21'] = "61-112"
om['ilerleme']['not'] = ("Sûre 20 TAM (135/135). Sûre 21 (Enbiyâ) makro + 21:1-60. Devam: 21:61. "
                         "Dikey katman A parçası (komşuluk zenginleşmesi) birincil, B etiketsiz.")
om['ilerleme']['okunan_ayet'] = 1333

json.dump(om, open('okuma_metni.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(mk, open('mercek_kayit.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("yazıldı · mercek 21:", len(mk['21']), "· uzay:", len(mk['21_uzay']))
