# -*- coding: utf-8 -*-
"""blok_25_31_40.py — sûre 25 dördüncü blok (25:31-40). İki ★★★ ayet: 25:33 ve 25:34."""
import json
DIK = json.load(open('blok_dikey_25_21_40.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
31: "Böylece her peygambere suçlulardan bir düşman kıldık. Yol gösterici ve yardımcı olarak Rabbin yeter.",
32: "İnkâr edenler dediler ki: Kur'ân ona toplu hâlde, tek seferde indirilseydi ya. Böyle — kalbini onunla sağlamlaştıralım diye; ve onu ağır ağır, tane tane okuduk.",
33: "Sana hiçbir mesel getirmezler ki biz sana hakkı ve daha güzel bir açıklamayı getirmiş olmayalım.",
34: "Yüzleri üstü cehenneme toplanacak olanlar — işte onlar yerce daha kötü, yolca daha sapkındır.",
35: "Andolsun Mûsâ'ya kitabı verdik ve kardeşi Hârûn'u onunla birlikte vezir kıldık.",
36: "Dedik ki: Âyetlerimizi yalanlayan topluluğa gidin. Sonra onları darmadağın ettik.",
37: "Nûh'un kavmini de — elçileri yalanladıklarında onları boğduk ve insanlara bir ibret kıldık. Zalimlere acı bir azap hazırladık.",
38: "Âd'ı, Semûd'u, Ress ashabını ve bunlar arasında birçok nesli de.",
39: "Her birine misaller getirdik; her birini de yerle bir ettik.",
40: "Andolsun, kötülük yağmuruna tutulan o beldeye vardılar. Onu görmüyorlar mıydı? Hayır, onlar diriltilmeyi ummuyorlardı.",
}

OLCUM = {
31: ("eksen: **lafız YOK · رَبّ *(Rab)* 9. sırada — sûrenin beşinci Rab'bi** (rab z=1,62: "
 "**yıldızın TEK kaynağı**) · **esmâ نَصِير *(yardımcı)* 11. sırada = fâsıla, MÜHÜRSÜZ — GEÇERLİ**: "
 "doğrudan رَبّ *(Rab)*'bin temyizi (كَفَىٰ بِرَبِّكَ هَادِيًۭا وَنَصِيرًۭا *(yol gösterici ve "
 "yardımcı olarak Rabbin yeter)*); NOT — هَادِيًۭا *(yol gösterici)* AYNI sözdizimsel konumda ve "
 "esmâ SAYILMIYOR: **aday 546'nın ölçüt (b) çatışmasının temiz sınama vakası** · aktör yok · edim "
 "haber, kip işareti yok · şahıs 1P x2 · 3MS x1 · 2MS x1, iltifât 0 · n=11 mora=71 harf=53 "
 "(n z=-0,15), fâsıla نَصِيرًۭا *(yardımcı)* → ا, A sınıfı, ACC; i'râb GEN 4 · ACC 3; bab I x2; "
 "zaman PERF x2; dış düğüm 1 · **yıldız ★** · kökler جعل *(kılma, var etme)* · كلل *(hep, bütün)* · "
 "نبأ *(haber; nebî)* · عدو *(düşmanlık, düşman)* · جرم *(suç, cürüm)* · كفي *(yetme, kâfi gelme)* · "
 "ربب *(rab, terbiye etme)* · هدي *(yol gösterme, hidayet)* · نصر *(yardım)* · bağ: xref جعل "
 "*(kıldı)* + كلّ *(her)* + نبيّ *(nebî)* ve كلّ *(her)* + نبيّ *(nebî)* + عدوّ *(düşman)* → **ikisi "
 "de 6:112**; **25:19 ile ortak نصر *(yardım)*** — orada نَصْرًۭا *(yardım)* olumsuzlanıyordu "
 "(فَمَا تَسْتَطِيعُونَ … نَصْرًۭا), burada aynı kök esmâ olarak olumlu (elle, L1, aday 555)"),
32: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı قُرْءان *(Kur'ân)* 7. sırada, rol "
 "FAİL — 25:30'da MEF'ÛL'dü** · edim haber, kip işareti yok · şahıs 3MS x5 · 1P x3 · 3MP x2 · "
 "2MS x1, iltifât 0 · n=15 mora=85 harf=75 (n z=0,27), fâsıla تَرْتِيلًۭا *(tane tane okuma)* → ا, "
 "A sınıfı, ACC; i'râb ACC 4 · NOM 1; bab I x2 · **II x3 — sûrede bab II'nin en yoğun ayeti**; "
 "zaman PERF x4 · IMPF x1; **edilgen 1 — نُزِّلَ *(indirilseydi)*** (pas z=0,81); **kök ikilemesi "
 "رتل *(ağır ağır ve tane tane okuma (tertîl))* x2 — fiil + mef'ûl-i mutlak**; **açık sayı sözcüğü: "
 "وحد *(bir olma, teklik)* → وَٰحِدَةً *(tek)***; simetri [3,2,10,1]; dış düğüm 0 · yıldız ★ yok · "
 "kökler قول *(söz söyleme)* · كفر *(inkâr, nankörlük)* · نزل *(inme, indirme)* · قرأ *(okuma, "
 "Kur'ân)* · جمل *(güzellik, cemîl; toplu olma (cümle); deve)* · وحد *(bir olma, teklik)* · ثبت "
 "*(sabit olma, sağlamlaştırma)* · فأد *(gönül, fuâd)* · رتل *(ağır ağır ve tane tane okuma "
 "(tertîl))* · bağ: **25:25 ile aynı fiil** — نُزِّلَ *(indirildi)* bab II, orada melekler burada "
 "Kur'ân; **رتل korpusta DÖRT geçişli, ikisi bu ayette, ikisi 73:4** (elle, L1, aday 556)"),
33: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · RES 1 · şahıs "
 "3MP x2 · 2MS x2 · 1P x2 — **üç şahıs eşit dağılmış**, iltifât 0 · n=8 mora=46 harf=36 (n z=-0,47), "
 "fâsıla تَفْسِيرًا *(açıklama, tefsir)* → ا, A sınıfı, ACC; i'râb GEN 3 · ACC 1; bab I x2; zaman "
 "IMPF x1 · PERF x1; **HAPAKS: فسر *(açıklama, tefsir)* — korpusta TEK geçiş ve FÂSILA konumunda** "
 "(hapaks z=3,38: **yıldızın TEK kaynağı**); **biçim HASR**; dış düğüm 0 · **yıldız ★★★** · kökler "
 "أتي *(gelme, getirme)* · مثل *(benzer, mesel)* · جيأ *(gelme)* · حقق *(hak, gerçeklik)* · حسن "
 "*(güzellik, iyilik)* · فسر *(açıklama, tefsir)* · bağ: **25:9 ve 25:39 ile مثل *(benzer, mesel)* "
 "üçlüsü** — 25:9'da onlar mesel getiriyor (ضَرَبُوا۟ لَكَ ٱلْأَمْثَٰلَ *(sana misaller getirdiler)*), "
 "25:33'te yine onlar getiriyor ama cevap hazır, 25:39'da mesel getiren TARAF DEĞİŞİYOR (ضَرَبْنَا "
 "لَهُ ٱلْأَمْثَٰلَ *(ona misaller getirdik)*) (elle, L1, aday 557)"),
34: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı جَهَنَّم *(cehennem)* 6. sırada, rol "
 "mecrur** · edim haber, kip işareti yok · şahıs 3MP x3, iltifât 0 · n=11 mora=67 harf=52 "
 "(n z=-0,15), fâsıla سَبِيلًۭا *(yol)* → ا, A sınıfı, ACC; i'râb GEN 2 · NOM 2 · ACC 2; bab I x1; "
 "zaman IMPF x1; **edilgen 1 — يُحْشَرُونَ *(toplanırlar)*; ayetin TEK fiili ve o da edilgen, yani "
 "edilgenlik oranı 1,00**, pas z=5,38: **okumada görülen en yüksek edilgenlik z'si ve yıldızın TEK "
 "kaynağı**; simetri [3,1,5,1]; dış düğüm 1 · **yıldız ★★★** · kökler حشر *(toplama, mahşer)* · "
 "وجه *(yüz, yön)* · شرر *(şer, kötülük)* · كون *(olmak; mekân, yer)* · ضلل *(sapma, saptırma)* · "
 "سبل *(yol)* · bağ: xref شرّ *(şer)* + مكان *(mekân)* + أضلّ *(daha sapkın)* → **5:60**; **25:9, "
 "25:17, 25:27 ile سبل *(yol)* dördüncü geçiş** ve ilk kez üstünlük kalıbında: أَضَلُّ سَبِيلًۭا "
 "*(yolca daha sapkın)* (elle, L1, aday 550)"),
35: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı مُوسَى *(Mûsâ)* 3. sırada rol FAİL, "
 "هارُون *(Hârûn)* 8. sırada rol MEF'ÛL — sûrenin ilk kişi aktörleri** · edim haber, kip EMPH 1 · "
 "CERT 1 · şahıs 1P x4 · 3MS x2, iltifât 0 · n=9 mora=56 harf=43 (n z=-0,36), fâsıla وَزِيرًۭا "
 "*(vezir, yardımcı)* → ا, A sınıfı, ACC; **i'râb ACC 4 · NOM 2**; bab I x1 · IV x1; zaman PERF x2; "
 "simetri [3,1,6,1]; **dış düğüm 2** · yıldız ★ yok · kökler أتي *(gelme, getirme)* · كتب *(yazma, "
 "kitap)* · جعل *(kılma, var etme)* · أخو *(kardeş)* · وزر *(yük; vezir)* · bağ: xref آتى *(verdi)* "
 "+ كتاب *(kitap)* + جعل *(kıldı)* → **17:2 · 19:30**; **25:1 ile karşıtlık** — orada indirilen "
 "ٱلْفُرْقَان *(Furkān)* ve alıcı tek (عَبْدِهِۦ *(kulu)*), burada verilen ٱلْكِتَٰب *(kitap)* ve "
 "alıcıya bir yardımcı EKLENİYOR (elle, L1, aday 558)"),
36: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim emir, kip IMPV 1 · **şahıs 1P x5 · "
 "3MP x3 · 2MD x1 · 2D x1 — okumada İLK İKİL (tesniye) ŞAHIS**, iltifât 0 · n=9 mora=63 harf=50 "
 "(n z=-0,36), fâsıla تَدْمِيرًۭا *(darmadağın etme)* → ا, A sınıfı, ACC; i'râb GEN 2 · ACC 1; "
 "bab I x2 · II x2; zaman PERF x3 · IMPV 1; **kök ikilemesi دمر *(helâk etme, darmadağın etme)* x2 "
 "— fiil + mef'ûl-i mutlak**; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · ذهب *(gitme; "
 "altın)* · قوم *(kalkma; kavim; kıyamet)* · كذب *(yalan; yalanlama)* · أيي *(âyet, işaret)* · دمر "
 "*(helâk etme, darmadağın etme)* · bağ: **25:32, 25:39 ile aynı yapı** — üç ayette de fiil + "
 "mef'ûl-i mutlak (رَتَّلْنَٰهُ تَرْتِيلًۭا *(tane tane okuduk)* · دَمَّرْنَٰهُمْ تَدْمِيرًۭا "
 "*(darmadağın ettik)* · تَبَّرْنَا تَتْبِيرًۭا *(yerle bir ettik)*), üçü de bab II ve üçü de "
 "1P (elle, L1, aday 559)"),
37: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı نُوح *(Nûh)* 2. sırada, rol mecrur** · "
 "edim haber, kip işareti yok · **şahıs 1P x6 — blokta en yüksek**; 3MP x4, iltifât 0 · n=13 "
 "mora=91 harf=72 (n z=0,06), fâsıla أَلِيمًۭا *(acı veren)* → ا, A sınıfı, ACC; **i'râb ACC 5 · "
 "GEN 3**; bab I x1 · II x1 · IV x2; zaman PERF x4; dış düğüm 2 · yıldız ★ yok · kökler قوم "
 "*(kalkma; kavim; kıyamet)* · كذب *(yalan; yalanlama)* · رسل *(gönderme, elçi)* · غرق *(boğulma)* · "
 "جعل *(kılma, var etme)* · أنس *(insan; ünsiyet)* · أيي *(âyet, işaret)* · عتد *(hazırlama)* · "
 "ظلم *(zulüm)* · عذب *(azap)* · ألم *(elem, acı)* · bağ: xref ظالم *(zalim)* + عذاب *(azap)* + "
 "أليم *(acı veren)* → **14:22 · 42:21**; **25:11 ile ortak عتد *(hazırlama)*** — orada سَعِيرًا "
 "*(çılgın alev)* hazırlanıyordu, burada عَذَابًا أَلِيمًۭا *(acı bir azap)*; aynı fiil, farklı nesne"),
38: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı عاد *(Âd)* 1. sırada rol MEF'ÛL, "
 "ثَمُود *(Semûd)* 2. sırada rol mecrur; NOT — أَصْحَٰبَ ٱلرَّسِّ *(Ress ashabı)* AKTÖR TABLOSUNA "
 "GİRMİYOR** (aday 462 kümesi) · edim haber, kip işareti yok · **şahıs eki YOK — ayette hiç fiil "
 "yok; okunan ikinci fiilsiz ayet (birincisi 25:24)**, iltifât 0 · n=8 mora=50 harf=41 (n z=-0,47), "
 "fâsıla كَثِيرًۭا *(çok)* → ا, A sınıfı, ACC; **i'râb ACC 5 · GEN 2**; **bab yok · zaman yok**; "
 "**açık sayı sözcüğü: كثر *(çokluk)* → كَثِيرًۭا *(çok)***; dış düğüm 0 · yıldız ★ yok · kökler "
 "عود *(geri dönme; Âd)* · صحب *(arkadaşlık; ehli)* · رسس *(Ress (kuyu; kavim adı))* · قرن *(nesil, "
 "çağ; birbirine bağlama (mukarren))* · بين *(arası; açıklama)* · كثر *(çokluk)* · bağ: **25:13 ile "
 "قرن *(nesil, çağ; birbirine bağlama (mukarren))* ikinci geçişi ve BURADA 'nesil' anlamında** — "
 "aynı kök sûrede iki ayrı lemmayla (elle, L1, adaylar 529, 548)"),
39: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "1P x4 · 3MS x1, iltifât 0 · n=7 mora=45 harf=36 — **bloğun en kısa ayeti** (n z=-0,58), fâsıla "
 "تَتْبِيرًۭا *(yerle bir etme)* → ا, A sınıfı, ACC; **i'râb ACC 4 — yedi kelimenin dördü mansûb**; "
 "bab I x1 · II x1; zaman PERF x2; **kök ikilemesi كلل *(hep, bütün)* x2 · تبر *(yerle bir etme)* x2 "
 "— ikincisi fiil + mef'ûl-i mutlak**; **biçim KELLA — sûrenin TEK KELLA'sı**; dış düğüm 0 · yıldız "
 "★ yok · kökler كلل *(hep, bütün)* · ضرب *(vurma; mesel getirme)* · مثل *(benzer, mesel)* · تبر "
 "*(yerle bir etme)* · bağ: **25:9 ve 25:33 ile مثل *(benzer, mesel)* üçlüsü tamamlanıyor — mesel "
 "getiren taraf DEĞİŞİYOR** (elle, L1, aday 557); **تبر *(yerle bir etme)* korpusta ALTI geçişli, "
 "ikisi bu ayette**"),
40: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — ٱلْقَرْيَة *(belde)* adsız · edim soru, "
 "kip EMPH 1 · CERT 1 · INTG 1 · NEG 2 · **şahıs 3MP x10 — okunan ayetler içinde tek şahıstan en "
 "yüksek sayım**; 3FS x2, iltifât 0 · n=16 mora=82 harf=75 (n z=0,38), fâsıla نُشُورًۭا *(diriliş)* "
 "→ ا, A sınıfı, ACC — **25:3'ün fâsılasıyla aynı kelime**; i'râb GEN 2 · ACC 2; bab I x5 · IV x1; "
 "zaman PERF x3 · IMPF x3; **edilgen 1 — أُمْطِرَتْ *(yağdırıldı)*** (pas z=0,62); **kök ikilemesi "
 "مطر *(yağmur; yağdırma)* x2 — edilgen fiil + iç mef'ûl: أُمْطِرَتْ مَطَرَ ٱلسَّوْءِ *(kötülük "
 "yağmuruna tutuldu)*; كون *(olmak; mekân, yer)* x2**; **biçim IDRAB — بَلْ *(hayır, bilakis)*, "
 "sûrenin ikinci IDRAB'ı; birincisi 25:11**; simetri [3,1,12,1]; dış düğüm 0 · yıldız ★ yok · "
 "kökler أتي *(gelme, getirme)* · قري *(belde, köy)* · مطر *(yağmur; yağdırma)* · سوأ *(kötülük)* · "
 "كون *(olmak; mekân, yer)* · رأي *(görme)* · رجو *(umma, bekleme)* · نشر *(yayma, açma; diriltme)* · "
 "bağ: **25:3 ile halka** — orada نُشُورًۭا *(diriliş)* sahte ilâhların yetersizlik listesinin son "
 "terimiydi, burada aynı kelime inkârın son gerekçesi; **25:21 ile ortak رجو *(umma, bekleme)*** — "
 "orada لَا يَرْجُونَ لِقَآءَنَا *(bize kavuşmayı ummayanlar)*, burada كَانُوا۟ لَا يَرْجُونَ "
 "نُشُورًۭا *(dirilişi ummuyorlardı)* (elle, L1, aday 560)"),
}

MERCEK = {
31: ("Yıldızın tek kaynağı tek bir رَبّ *(Rab)* geçişi (rab z=1,62). Ölçülebilir bir yeterlilik "
 "cümlesi: كَفَىٰ بِرَبِّكَ *(Rabbin yeter)*, كفي *(yetme, kâfi gelme)* korpusta 33 geçişli ve "
 "dikey ölçümü hem ▸önce hem ▸sonra وكل *(vekil kılma, tevekkül)* veriyor (x9,3 ve x18,6) — kalıp "
 "korpusta sabit. İki temyiz yan yana: هَادِيًۭا *(yol gösterici)* ve نَصِيرًۭا *(yardımcı)*, ikisi "
 "de nekre mansûb ve ikisi de aynı sözdizimsel konumda. **Ama esmâ tablosu yalnız ikincisini esmâ "
 "sayıyor.** Bu, ayette görülebilen en temiz ölçüt çatışması — aday 546'nın (b) maddesi. Ve düşman "
 "atanması bir genelleme: لِكُلِّ نَبِىٍّ *(her peygambere)*, نبأ *(haber; nebî)* kökü; sûre bu "
 "kökü ilk kez burada kullanıyor."),
32: ("İtiraz biçimle ilgili: Kur'ân'ın parça parça inişine. جُمْلَةًۭ وَٰحِدَةًۭ *(toplu hâlde, tek "
 "seferde)* — جمل *(güzellik, cemîl; toplu olma (cümle); deve)* korpusta 11 geçişli ve bu lemma "
 "(جُمْلَة) tek geçiş; kökün öteki geçişleri 'güzel' ve 'deve'. Cevap itirazı reddetmiyor, "
 "GEREKÇELENDİRİYOR: كَذَٰلِكَ *(böyle)* + amaç cümlesi (لِنُثَبِّتَ بِهِۦ فُؤَادَكَ *(kalbini "
 "onunla sağlamlaştıralım diye)*). Ölçülebilir bir kapanış: رَتَّلْنَٰهُ تَرْتِيلًۭا *(onu tane "
 "tane okuduk)* — رتل *(ağır ağır ve tane tane okuma (tertîl))* korpusta DÖRT geçişli ve dördü iki "
 "ayette: 25:32 ve 73:4, her ikisinde de aynı fiil + mef'ûl-i mutlak yapısı. Kök korpusta yalnız "
 "bu kalıpla var. Ve fiil nesnesi 25:30'da mef'ûl olan Kur'ân'ı burada FAİL yapıyor (نُزِّلَ … "
 "ٱلْقُرْءَانُ *(Kur'ân indirilseydi)*)."),
33: ("SÛRENİN İKİNCİ ★★★ AYETİ ve yıldızın TEK kaynağı yine bir hapaks: تَفْسِيرًا *(açıklama, "
 "tefsir)*, فسر *(açıklama, tefsir)* kökü, korpusta TEK geçiş — ve fâsıla konumunda. Ölçülebilir bir "
 "yapı: ayet bir olumsuzlama ve bir istisnayla kurulu (وَلَا … إِلَّا), yani HASR; iki fiil karşı "
 "karşıya ve ikisi de gelme fiili ama farklı köklerden — يَأْتُونَكَ *(sana getirirler)* أتي *(gelme, "
 "getirme)*, جِئْنَٰكَ *(sana getirdik)* جيأ *(gelme)*. Aynı anlam alanı, iki ayrı kök, ters yön. "
 "Zaman da karşıt: muzâri (onların getirmesi sürekli) ve mâzi (cevabın önceden hazır olması). "
 "Getirilen iki şey: ٱلْحَقّ *(hak)* marife ve أَحْسَنَ تَفْسِيرًا *(daha güzel bir açıklama)* "
 "üstünlük kalıbında."),
34: ("SÛRENİN ÜÇÜNCÜ ★★★ AYETİ ve yıldızın kaynağı bu kez hapaks değil: pas z=5,38, okumada görülen "
 "en yüksek edilgenlik z'si. Sebebi ölçülebilir — ayetin TEK fiili var ve o da edilgen "
 "(يُحْشَرُونَ *(toplanırlar)*), yani edilgenlik oranı 1,00; z, edilgen SAYISINI değil edilgen "
 "ORANINI ölçüyor. Ölçülebilir bir edilgenlik: özneler kendi hareketlerinin faili değil. Ve konum "
 "hâl olarak veriliyor: عَلَىٰ وُجُوهِهِمْ *(yüzleri üstü)*, وجه *(yüz, yön)* kökü. İki üstünlük "
 "sıfatı kapanışta ve ikisi de temyizli: شَرٌّۭ مَّكَانًۭا *(yerce daha kötü)*, أَضَلُّ سَبِيلًۭا "
 "*(yolca daha sapkın)* — 25:24'ün خَيْرٌۭ مُّسْتَقَرًّۭا وَأَحْسَنُ مَقِيلًۭا *(kalınacak yer "
 "bakımından daha hayırlı, dinlenilecek yer bakımından daha güzel)* yapısının birebir tersi: aynı "
 "kalıp, ters kutup, ve ikisi de fiilsiz-benzeri (25:24 tam fiilsiz, burada tek fiil ve o edilgen)."),
35: ("Kıssa dizisi tek ayetlik bir verme cümlesiyle açılıyor ve ayet iki kişiyi birden adlandırıyor — "
 "sûrenin ilk kişi aktörleri. Ölçülebilir bir rol dağılımı: مُوسَى *(Mûsâ)* fâil konumunda "
 "(verilenin alıcısı), هارُون *(Hârûn)* mef'ûl konumunda (kılınanın kendisi). İki fiil de 1P: "
 "ءَاتَيْنَا *(verdik)* ve جَعَلْنَا *(kıldık)*. وزر *(yük; vezir)* korpusta 15 geçişli ve "
 "çoğunda 'günah yükü' anlamında; burada 'yardımcı' anlamında — kök düzeyi komşuluk bu ayrımı "
 "yapmıyor (aday 529 sınıfı). Ve karşıtlık sûrenin açılışıyla: 25:1'de iniş TEK alıcıya "
 "(عَبْدِهِۦ *(kulu)*), burada alıcıya bir yardımcı ekleniyor."),
36: ("Emir ikil kipte veriliyor: ٱذْهَبَآ *(ikiniz gidin)* — okumada ilk kez tesniye şahıs "
 "(2MD/2D). Ölçülebilir bir sıkıştırma: dokuz kelimede görevlendirme ve sonuç birlikte veriliyor, "
 "arada hiçbir anlatı yok; emirle helâk arasında tek bağlaç var (فَ *(ve böylece)*). Kapanış yine "
 "fiil + mef'ûl-i mutlak: دَمَّرْنَٰهُمْ تَدْمِيرًۭا *(onları darmadağın ettik)*, دمر *(helâk etme, "
 "darmadağın etme)* bab II. Bu yapı blokta üçüncü kez: 25:32 رَتَّلْنَٰهُ تَرْتِيلًۭا *(tane tane "
 "okuduk)*, 25:36 burada, 25:39 تَبَّرْنَا تَتْبِيرًۭا *(yerle bir ettik)*. Üçü de bab II, üçü de "
 "1P, üçü de fâsıla konumunda."),
37: ("Kıssa formülü sıkışıyor: kavim adı, tekzip, helâk ve ibret tek ayette. Ölçülebilir bir şahıs "
 "dağılımı: 1P x6, blokta en yüksek — helâk anlatısı boyunca fâil sürekli birinci çoğul. Boğulma "
 "fiili tek: أَغْرَقْنَٰهُمْ *(onları boğduk)*, غرق *(boğulma)* korpusta 23 geçişli ve dikey "
 "ölçümü ▸önce Firavun ailesi bağlamına yakın komşular veriyor. Sonuç iki katmanlı: önce ibret "
 "(ءَايَةً *(bir âyet, ibret)*, ve muhatabı لِلنَّاسِ *(insanlara)* — türe genişletilmiş), sonra "
 "azap. Ve hazırlama fiili 25:11'den geri geliyor: عتد *(hazırlama)*, orada nesne سَعِيرًا *(çılgın "
 "alev)*, burada عَذَابًا أَلِيمًۭا *(acı bir azap)* — aynı fiil, iki farklı nesne, ikisi de fâsıla "
 "konumunda."),
38: ("Ayette hiç fiil yok — okunan ayetler içinde ikinci fiilsiz ayet (birincisi 25:24). Sekiz "
 "kelimenin beşi mansûb ve hepsi bir önceki ayetin fiiline bağlanıyor: liste, kendi yüklemi olmayan "
 "bir sıralama. Ölçülebilir bir sayım kapanışı: قُرُونًۢا بَيْنَ ذَٰلِكَ كَثِيرًۭا *(bunlar arasında "
 "birçok nesil)* — قرن *(nesil, çağ; birbirine bağlama (mukarren))* burada 'nesil' anlamında, oysa "
 "25:13'te aynı kök مُقَرَّنِينَ *(birbirine bağlanmış)* idi; sûre bu kökü iki ayrı lemmayla "
 "kullanıyor. رسس *(Ress (kuyu; kavim adı))* korpusta İKİ geçişli (25:38, 50:12) ve dikey ölçümü "
 "eşiği aşan komşu vermiyor. NOT: أَصْحَٰبَ ٱلرَّسِّ *(Ress ashabı)* aktör tablosuna girmiyor, "
 "oysa عاد *(Âd)* ve ثَمُود *(Semûd)* giriyor — tabloda kavim tanımı tutarsız (aday 462)."),
39: ("Yedi kelime, iki kök ikilemesi ve tek biçim etiketi. كلل *(hep, bütün)* iki kez ve ikisi de "
 "nekre mansûb (وَكُلًّۭا *(her birine)*), ayeti iki eşit yarıya bölüyor — ilk yarı mesel, ikinci "
 "yarı helâk. Ölçülebilir bir simetri: iki yarı da aynı yapıda (كُلًّۭا + 1P fiil + tümleç). "
 "Kapanış üçüncü kez fiil + mef'ûl-i mutlak: تَبَّرْنَا تَتْبِيرًۭا *(yerle bir ettik)*; تبر "
 "*(yerle bir etme)* korpusta ALTI geçişli ve ikisi bu ayette. Ve mesel getirme fiili taraf "
 "değiştiriyor: 25:9'da ضَرَبُوا۟ لَكَ ٱلْأَمْثَٰلَ *(sana misaller getirdiler)*, burada ضَرَبْنَا "
 "لَهُ ٱلْأَمْثَٰلَ *(ona misaller getirdik)* — aynı kök, aynı kalıp, fâil ve mef'ûl yer "
 "değiştirmiş."),
40: ("Bloğun kapanışı bir soru ve bir düzeltme: أَفَلَمْ يَكُونُوا۟ يَرَوْنَهَا *(onu görmüyorlar "
 "mıydı)* sonra بَلْ *(hayır, bilakis)* — sûrenin ikinci IDRAB'ı; birincisi 25:11'de bloğu "
 "açmıştı. Ölçülebilir bir çerçeve: sûrenin iki IDRAB'ı da bir inkâr fiilini düzeltiyor ve ikisi "
 "de aynı alanda — 25:11 كَذَّبُوا۟ بِٱلسَّاعَةِ *(o saati yalanladılar)*, burada لَا يَرْجُونَ "
 "نُشُورًۭا *(dirilişi ummuyorlardı)*. Yağmur kök ikilemesiyle veriliyor ve edilgen: أُمْطِرَتْ "
 "مَطَرَ ٱلسَّوْءِ *(kötülük yağmuruna tutuldu)*; مطر *(yağmur; yağdırma)* korpusta 15 geçişli ve "
 "onunda bu edilgen kalıpta — kök korpusta ağırlıkla azap yağmuru için. SINIR: ayet yağış için ne "
 "bir mekanizma ne bir ölçü veriyor; 'yağmur' burada bir helâk adı, meteorolojik bir olay değil. "
 "Ve fâsıla 25:3'ün fâsılasıyla aynı kelime: نُشُورًۭا *(diriliş)*."),
}

ATLAMA = {
 "_mercek_25_33": ("25:33 ★★★ — 🜁 BİYOLOG VE 🜂 UZAY MERCEKLERİ YAZILMADI, ÇIPA YOK. Ayet sekiz "
  "kelime ve tamamı söz/karşı-söz alanında: mesel getirme, hak, açıklama. Ne canlı, ne organ, ne "
  "gök cismi, ne ölçü, ne süreç. Yıldızın kaynağı içerik değil: TEK kaynak hapaks z=3,38 (فسر "
  "*(açıklama, tefsir)*, korpusta tek geçiş, fâsıla konumunda). ADAY 553'ün ikinci vakası."),
 "_mercek_25_34": ("25:34 ★★★ — 🜁 BİYOLOG VE 🜂 UZAY MERCEKLERİ YAZILMADI, ÇIPA YOK. Ayette bir "
  "beden öğesi geçiyor (وُجُوه *(yüzler)*) ama bir HÂL bildirimi olarak: عَلَىٰ وُجُوهِهِمْ "
  "*(yüzleri üstü)*. Bunu 'yüzüstü hareket biyomekaniği' ya da benzeri bir okumaya çevirmek "
  "YASAKLI 'bilimsel izdüşüm' olurdu — ayet ne anatomi, ne hareket, ne ölçü veriyor; gönderge bir "
  "haşir sahnesi. ÇIPA TANIMI için önemli sınama: BEDEN ÖĞESİNİN GEÇMESİ ÇIPA DEĞİLDİR; çıpa için "
  "ayetin o öğe hakkında ölçülebilir bir şey söylemesi gerekir. Yıldızın kaynağı da içerik değil: "
  "TEK kaynak pas z=5,38 (ayetin tek fiili edilgen, oran 1,00). ADAY 553'ün üçüncü vakası."),
 "_blok_notu_25_31_40": ("BLOK BİLANÇOSU: iki ★★★ (25:33, 25:34), bir ★ (25:31), on ayetin "
  "yedisi yıldızsız. **İKİ ★★★ AYETİN İKİSİNDE DE ÇIPA SIFIR.** Buna karşılık blokta ÇIPA "
  "TAŞIYABİLECEK ayet var ve YILDIZSIZ: 25:40, أُمْطِرَتْ مَطَرَ ٱلسَّوْءِ *(kötülük yağmuruna "
  "tutuldu)* — gerçek bir yağış olayı anılıyor, yıldız 0. Bu, aday 553'ün en keskin karşıtlığı: "
  "sûre 25'in okunan kırk ayetinde üç ★★★ ayetin ÜÇÜNDE DE çıpa sıfır, çıpa taşıyan iki ayet ise "
  "★★ (25:25) ve ★ yok (25:40) alıyor."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(31, 41):
    OM['25']["25:%d" % n] = {"ar": AR[(25, n)], "meal": MEAL[n], "olcum": OLCUM[n],
                             "mercek": MERCEK[n], "dikey": DIK["25:%d" % n]}
OM['25']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 23 TAM (118/118). Sûre 24 TAM (64/64). **Sûre 25 (Furkān) 40/77.** "
                         "Devam: 25:41'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "25": "1-40 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1685
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 25 →', len([k for k in OM['25'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(31, 41):
    MK['25']["25:%d" % n] = MERCEK[n]
MK['25_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 25 →', len(MK['25']))
