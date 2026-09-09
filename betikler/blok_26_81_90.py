# -*- coding: utf-8 -*-
"""blok_26_81_90.py — sûre 26 altıncı blok (26:81-90). ٱلَّذِى zinciri kapanıyor, ilk Allah lafzı."""
import json
DIK = json.load(open('blok_dikey_26_81_90.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
81: "Beni öldüren, sonra dirilten de o.",
82: "Din günü hatamı bağışlamasını umduğum da o.",
83: "Rabbim, bana hüküm bağışla ve beni sâlihlere kat.",
84: "Sonrakiler içinde bana bir doğruluk dili nasip et.",
85: "Beni Naîm cennetinin vârislerinden kıl.",
86: "Babamı da bağışla; o sapkınlardandı.",
87: "Diriltilecekleri gün beni rezil etme.",
88: "O gün ne mal fayda verir ne oğullar.",
89: "Ancak Allah'a temiz bir kalple gelen başka.",
90: "Cennet, sakınanlara yaklaştırıldı.",
}

O = {
81: ("eksen: **lafız YOK · Rab YOK — gönderge وَٱلَّذِى *(ve o ki)*; zincirin dördüncü halkası** · "
 "esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs 3MS x2 · 1S x2, iltifât 0 · n=4 "
 "mora=24 harf=18 (n z=-0,89), fâsıla يُحْيِينِ *(beni diriltir)* → ن, N sınıfı — **ـِينِ eki "
 "dördüncü kez**; **i'râb YOK — blokta i'râbsız tek ayet**; **bab IV x2 — ayetin iki fiili de "
 "bab IV**; zaman IMPF x2; dış düğüm 0 · yıldız ★ yok · kökler موت *(ölüm)* · حيي *(diri olma, "
 "hayat)* · bağ: **25:3, 25:49, 25:58 ile موت *(ölüm)* / حيي *(diri olma, hayat)* çiftinin DÖRDÜNCÜ "
 "karşılaşması** — 25:3'te sahte ilâhlar ikisi üzerinde güçsüz (iki ayrı nesne), 25:49'da tek "
 "eylemde birleşiyor (ölü beldeyi diriltme), 25:58'de tek göndergede (ölmeyen Diri), burada "
 "SIRALI İKİ EYLEM: يُمِيتُنِى ثُمَّ يُحْيِينِ *(beni öldürür, sonra diriltir)* (elle, L1, aday 658)"),
82: ("eksen: **lafız YOK · Rab YOK — gönderge وَٱلَّذِىٓ; zincirin BEŞİNCİ VE SON halkası** · esmâ "
 "yok · aktör yok · edim haber, kip işareti yok · **şahıs 1S x3 · 3MS x1**, iltifât 0 · n=8 mora=39 "
 "harf=31 (n z=-0,47), **fâsıla ٱلدِّينِ *(din, hesap)* → ن, N sınıfı — ZİNCİRDE İLK KEZ FÂSILA "
 "BİR İSİM, ـِينِ eki KIRILIYOR**; i'râb NOM 1 · ACC 1 · GEN 1; bab I x2; zaman IMPF x2; dış düğüm "
 "0 · yıldız ★ yok · kökler طمع *(tamah, umma)* · غفر *(bağışlama, mağfiret)* · خطأ *(hata, günah)* · "
 "يوم *(gün)* · دين *(din; borç)* · bağ: **26:51 ile ÜÇ ORTAK KÖK VE AYNI YAPI** — إِنَّا نَطْمَعُ "
 "أَن يَغْفِرَ لَنَا رَبُّنَا خَطَٰيَٰنَآ *(Rabbimizin hatalarımızı bağışlamasını umuyoruz)* / "
 "وَٱلَّذِىٓ أَطْمَعُ أَن يَغْفِرَ لِى خَطِيٓـَٔتِى *(hatamı bağışlamasını umduğum)*; طمع + غفر + "
 "خطأ üçlüsü ikisinde de, **çoğuldan tekile ve büyücülerden İbrâhîm'e**; esit alanı YAKALAMIYOR "
 "(elle, L1, aday 659)"),
83: ("eksen: **lafız YOK · رَبّ *(Rab)* 1. sırada — on sekizinci Rab**, **rab z=3,23: yıldızın TEK "
 "kaynağı** (n=6, oran 0,17) · esmâ yok · aktör yok · edim emir, kip IMPV 2 · şahıs 1S x3 · 2MS x2, "
 "iltifât 0 · n=6 mora=32 harf=26 (n z=-0,68), fâsıla بِٱلصَّٰلِحِينَ *(sâlihler)* → ن, N sınıfı; "
 "i'râb NOM 1 · ACC 1 · GEN 1; bab I x1 · IV x1; **zaman IMPV x2 — ayetin iki fiili de emir**; dış "
 "düğüm 0 · **yıldız ★★★** · kökler ربب *(rab, terbiye etme)* · وهب *(bağışlama, hibe)* · حكم "
 "*(hüküm verme, hikmet)* · لحق *(katma, ulaştırma; yetişme)* · صلح *(iyi, elverişli olma; ıslah)* · "
 "bağ: **26:21 ile وهب *(bağışlama, hibe)* + حكم *(hüküm)* çifti** — orada فَوَهَبَ لِى رَبِّى "
 "حُكْما *(Rabbim bana hüküm bağışladı)* GERÇEKLEŞMİŞ (PERF, Mûsâ), burada رَبِّ هَبْ لِى حُكْما "
 "*(Rabbim bana hüküm bağışla)* İSTENEN (IMPV, İbrâhîm); **aynı iki kök, aynı sıra, iki elçi, ters "
 "kip** (elle, L1, aday 660)"),
84: ("eksen: **lafız YOK · Rab YOK** · **esmâ آخِر *(sonraki)* 6. sırada = fâsıla, MÜHÜRSÜZ — "
 "ÖLÇÜM ARTEFAKTI**: ٱلْءَاخِرِينَ *(sonrakiler)* çoğul ve gönderge İNSANLAR; ölçüt (a) ve (b) "
 "birden dışlıyor · aktör yok · edim emir, kip IMPV 1 · şahıs 2MS x1 · 1S x1, iltifât 0 · n=6 "
 "mora=31 harf=25 (n z=-0,68), fâsıla ٱلْءَاخِرِينَ *(sonrakiler)* → ن, N sınıfı — **26:64 ve "
 "26:66'nın fâsılasıyla AYNI KÖK, farklı lemma** (orada ٱلْءَاخَرِينَ *(ötekiler)*); i'râb ACC 1 · "
 "GEN 2; bab I x1; zaman IMPV 1; dış düğüm 1 · yıldız ★ yok · kökler جعل *(kılma, var etme)* · لسن "
 "*(dil)* · صدق *(doğruluk)* · أخر *(geciktirme, sonraya bırakma)* · bağ: xref جعل *(kıldı)* + لسان "
 "*(dil)* + صدق *(doğruluk)* → **19:50**; **26:13 ile لسن *(dil)* ikinci geçişi** — orada وَلَا "
 "يَنطَلِقُ لِسَانِى *(dilim çözülmez)* bir YETERSİZLİK, burada لِسَانَ صِدْقٍ *(doğruluk dili)* "
 "bir İSTEK (elle, L1, aday 661)"),
85: ("eksen: **lafız YOK · Rab YOK** · **esmâ وارِث *(vâris)* 3. sırada, ORTA konum, MÜHÜRSÜZ — "
 "ÖLÇÜM ARTEFAKTI**: وَرَثَةِ جَنَّةِ ٱلنَّعِيمِ *(Naîm cennetinin vârisleri)*, çoğul ve gönderge "
 "İNSANLAR · aktör yok — **جَنَّة *(cennet)* burada tamlama başı ve tabloya GİRMİYOR; 26:90'da "
 "marife olarak GİRECEK** (aday 462/638) · edim emir, kip IMPV 1 · şahıs 2MS x1 · 1S x1, iltifât 0 · "
 "n=5 mora=27 harf=22 (n z=-0,79), fâsıla ٱلنَّعِيمِ *(Naîm, nimet)* → م, N sınıfı; **i'râb GEN 3 — "
 "beş kelimenin üçü mecrur**; bab I x1; zaman IMPV 1; dış düğüm 0 · yıldız ★ yok · kökler جعل "
 "*(kılma, var etme)* · ورث *(vâris olma)* · جنن *(örtme, gizleme; cennet; cin)* · نعم *(nimet; "
 "davar)* · bağ: **26:59 ile ورث *(vâris olma)* ikinci geçişi** — orada أَوْرَثْنَٰهَا بَنِىٓ "
 "إِسْرَٰٓءِيلَ *(İsrâiloğullarına miras kıldık)* YURT mirası ve gerçekleşmiş, burada cennet mirası "
 "ve istenen (elle, L1, aday 662)"),
86: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — أَب *(baba)* yine adlandırılmıyor · "
 "edim emir, kip IMPV 1 · şahıs 2MS x1 · 3MS x2, iltifât 0 · n=6 mora=39 harf=25 (n z=-0,68), "
 "fâsıla ٱلضَّآلِّينَ *(sapkınlar)* → ن, N sınıfı — **26:20'nin fâsılasıyla AYNI KELİME**; i'râb "
 "GEN 2 · ACC 1; bab I x2; zaman IMPV 1 · PERF 1; dış düğüm 0 · yıldız ★ yok · kökler غفر "
 "*(bağışlama, mağfiret)* · أبو *(baba)* · كون *(olmak; mekân, yer)* · ضلل *(sapma, saptırma)* · "
 "bağ: **26:20 ile ٱلضَّآلِّينَ *(sapkınlar)* ikinci geçişi** — orada Mûsâ KENDİSİ için kullanmıştı "
 "(وَأَنَا۠ مِنَ ٱلضَّآلِّينَ *(ben sapkınlardandım)*), burada İbrâhîm BABASI için; aynı kelime, "
 "aynı fâsıla, birinci şahıstan üçüncü şahsa (elle, L1, aday 663)"),
87: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · şahıs 3FS x1 · "
 "1S x1 · 3MP x2, iltifât 0 · n=4 mora=21 harf=17 (n z=-0,89), fâsıla يُبْعَثُونَ *(diriltilirler)* → "
 "ن, N sınıfı; **i'râb ACC 1**; bab I x1 · IV x1; zaman IMPF x2; **edilgen 1 — يُبْعَثُونَ; iki "
 "fiilden biri edilgen, oran 0,50**, pas z=2,52: **yıldızın TEK kaynağı**; dış düğüm 0 · **yıldız "
 "★★** · kökler خزي *(rezil olma/etme)* · يوم *(gün)* · بعث *(gönderme; diriltme)* · bağ: **26:51'in "
 "'ilk iman edenler' umuduyla karşıtlık** — orada büyücüler bağışlanma umuyordu, burada İbrâhîm "
 "REZİL OLMAMAYI istiyor; **خزي *(rezil olma/etme)* korpusta 26 geçişli ve dikey ölçümü ▸sonra "
 "kıyâmet x11,8 veriyor — kök korpusta zaten bu güne bağlı** (elle, L1)"),
88: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 2 · şahıs 3MS x1, "
 "iltifât 0 · n=6 mora=26 harf=20 (n z=-0,68), fâsıla بَنُونَ *(oğullar)* → ن, N sınıfı; i'râb "
 "ACC 1 · NOM 2; bab I x1; zaman IMPF x1; dış düğüm 0 · yıldız ★ yok · kökler يوم *(gün)* · نفع "
 "*(fayda)* · مول *(mal)* · بني *(bina, yapma)* · bağ: **25:3, 25:55, 26:73 ile نفع *(fayda)* "
 "DÖRDÜNCÜ geçişi — ve İLK KEZ ضرر *(zarar)* OLMADAN**; üç geçişte çift hâlindeydi, burada tek "
 "başına ve karşıtı مال/بنون *(mal/oğullar)* ikilisi; **karşıtlı kökün tek uçlu kullanımı** "
 "(25:6 سرر, 25:46 يسر, 26:60 شرق ile aynı desen) (elle, L1, aday 664)"),
89: ("eksen: **ALLAH LAFZI 4. sırada — SÛRENİN İLK LAFZI; ilk 88 ayette lafız SIFIRDI** "
 "(allah z=2,80: **yıldızın TEK kaynağı**) · Rab yok · esmâ yok · aktör yok · edim haber, kip RES 1 · "
 "şahıs 3MS x1, iltifât 0 · n=6 mora=29 harf=22 (n z=-0,68), fâsıla سَلِيمٍ *(temiz, sağlam)* → م, "
 "N sınıfı; i'râb ACC 1 · GEN 2; bab I x1; zaman PERF 1; **biçim HASR**; dış düğüm 0 · **yıldız ★★** · "
 "kökler أتي *(gelme, getirme)* · أله *(ilâh; lafza-i celâl)* · قلب *(çevirme; kalp)* · سلم "
 "*(esenlik; teslim olma)* · bağ: **25:17 ile karşılaştırma** — sûre 25'in ilk lafzı 25:17'deydi "
 "(17/77 = 0,22), sûre 26'nınki 26:89'da (89/227 = 0,39); **iki Mekkî sûrede de lafız GEÇ giriyor "
 "ama sûre 26'da çok daha geç** (aday 527/562 kümesi, elle, L1, aday 665)"),
90: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı جَنَّة *(cennet)* 2. sırada, rol "
 "FAİL — ve 26:85'te aynı kök tabloya GİRMEMİŞTİ**; fark: burada marife (ٱلْجَنَّةُ), orada tamlama "
 "başı (جَنَّةِ ٱلنَّعِيمِ) — **aktör tablosunun tanım ölçütü için tanı** (aday 462/638) · edim "
 "haber, kip işareti yok · **şahıs 3FS x1 — ayette başka şahıs yok**, iltifât 0 · n=3 mora=23 "
 "harf=18 (n z=-1,00), fâsıla لِلْمُتَّقِينَ *(sakınanlar)* → ن, N sınıfı; i'râb NOM 1 · GEN 1; "
 "bab IV x1; zaman PERF 1; **edilgen 1 — أُزْلِفَتِ *(yaklaştırıldı)*; ayetin TEK fiili ve o da "
 "edilgen, oran 1,00**, pas z=5,38: **yıldızın TEK kaynağı**; **dış düğüm 1** · **yıldız ★★★** · "
 "kökler زلف *(yaklaştırma, zülfe)* · جنن *(örtme, gizleme; cennet; cin)* · وقي *(sakınma, koruma)* · "
 "bağ: xref أزلفت *(yaklaştırıldı)* + جنّة *(cennet)* + متّقي *(sakınan)* → **50:31**; **26:64 ile "
 "زلف *(yaklaştırma, zülfe)* ikinci geçişi — VE KUTUP DÜZELİYOR**: orada helâke yaklaştırma (etken, "
 "azınlık anlamı), burada cennete yaklaştırma (edilgen, korpus taban anlamı) (elle, L1, aday 666)"),
}

M = {
81: ("Zincirin dördüncü halkası ve iki fiil de bab IV: يُمِيتُنِى ثُمَّ يُحْيِينِ *(beni öldürür, "
 "sonra diriltir)*. Ölçülebilir bir sıra: موت *(ölüm)* ve حيي *(diri olma, hayat)* okumada dördüncü "
 "kez karşılaşıyor ve her seferinde başka bir yapıda — 25:3'te iki ayrı nesne (sahte ilâhlar "
 "ikisinde de güçsüz), 25:49'da tek eylem (ölü beldeyi diriltme), 25:58'de tek gönderge (ölmeyen "
 "Diri), burada **sıralı iki eylem** ve ثُمَّ *(sonra)* ile ayrılmış. Dört ayet, dört yapı. Dikey "
 "ölçüm çiftin iki yönden bağlı olduğunu gösteriyor: موت ▸önce hayat x15,2, حيي ▸sonra موت x12,9. "
 "Ve ayet blokta i'râb etiketi almayan tek ayet."),
82: ("Zincirin beşinci ve son halkası; **ٱلَّذِى beş kez, biçim bir kez kırılıyor (26:80, şart "
 "cümlesi) ve kırılma zincirin TAM ORTASINDA.** Fâsıla eki de burada kırılıyor: 26:78-81'de dört "
 "kez ـِينِ (fiil + nûn-i vikâye), burada ٱلدِّينِ *(din, hesap)* bir İSİM. Yani **biçim ortada, "
 "ses sonda kırılıyor.** Ve ayet 26:51 ile üç kök paylaşıyor: طمع *(tamah, umma)* + غفر *(bağışlama, "
 "mağfiret)* + خطأ *(hata, günah)* — orada büyücüler çoğul olarak umuyordu (نَطْمَعُ … لَنَا … "
 "خَطَٰيَٰنَا), burada İbrâhîm tekil (أَطْمَعُ … لِى … خَطِيٓـَٔتِى). Aynı üçlü, iki konuşan, "
 "çoğuldan tekile; **esit alanı bunu yakalamıyor.**"),
83: ("Dua iki emirle açılıyor ve ikisi de 1S'ye: هَبْ لِى حُكْما *(bana hüküm bağışla)* ve "
 "أَلْحِقْنِى بِٱلصَّٰلِحِينَ *(beni sâlihlere kat)*. Ölçülebilir bir çift: وهب *(bağışlama, "
 "hibe)* + حكم *(hüküm verme, hikmet)* 26:21'de de bitişikti — فَوَهَبَ لِى رَبِّى حُكْما *(Rabbim "
 "bana hüküm bağışladı)*, ama orada PERF ve konuşan Mûsâ; burada IMPV ve konuşan İbrâhîm. **Aynı "
 "iki kök, aynı sıra, iki elçi, gerçekleşmişten istenene.** لحق *(katma, ulaştırma; yetişme)* "
 "korpusta ALTI geçişli ve dikey ölçümü hiçbir komşu vermiyor — kökün korpusta yatağı yok."),
84: ("İstek bir deyimle veriliyor: لِسَانَ صِدْقٍ *(doğruluk dili)*, لسن *(dil)* + صدق *(doğruluk)*. "
 "Terkip 19:50 ile ortak ve tek xref'i oraya düşüyor. لسن korpusta 25 geçişli ve dikey ölçümü "
 "▸sonra Arapça x76,2 veriyor — kök korpusta ağırlıkla dil-lisan bağlamında; burada 'anılma, nam' "
 "anlamında (aday 529 sınıfı). Ve kök 26:13'ten geri geliyor: orada وَلَا يَنطَلِقُ لِسَانِى "
 "*(dilim çözülmez)* Mûsâ'nın YETERSİZLİĞİYDİ, burada İbrâhîm'in İSTEĞİ. Fâsıladaki ٱلْءَاخِرِينَ "
 "esmâ sayılmış — çoğul ve gönderge insanlar; iki ölçüt birden dışlıyor."),
85: ("İkinci istek bir miras: وَرَثَةِ جَنَّةِ ٱلنَّعِيمِ *(Naîm cennetinin vârisleri)*. ورث *(vâris "
 "olma)* 26:59'dan geri geliyor: orada أَوْرَثْنَٰهَا بَنِىٓ إِسْرَٰٓءِيلَ *(İsrâiloğullarına miras "
 "kıldık)* YURT mirasıydı ve gerçekleşmişti, burada cennet mirası ve isteniyor. Dikey ölçüm ورث için "
 "▸önce cennet x5,0 · ▸sonra cennet x3,8 veriyor — **çift korpusta iki yönden bağlı**, terkip bu "
 "ayete özgü değil. Ve جَنَّة *(cennet)* burada tamlama başı olduğu için aktör tablosuna GİRMİYOR; "
 "26:90'da marife olarak girecek — **tablonun ölçütü belirlilik gibi görünüyor** (aday 462/638)."),
86: ("Üçüncü istek babası için: وَٱغْفِرْ لِأَبِىٓ *(babamı da bağışla)*. Ölçülebilir bir fâsıla "
 "tekrarı: ٱلضَّآلِّينَ *(sapkınlar)* 26:20'de de fâsılaydı — orada Mûsâ KENDİSİ için kullanmıştı "
 "(وَأَنَا۠ مِنَ ٱلضَّآلِّينَ *(ben sapkınlardandım)*), burada İbrâhîm BABASI için. Aynı kelime, "
 "aynı konum, birinci şahıstan üçüncü şahsa. Ve غفر *(bağışlama, mağfiret)* bitişik ayette ikinci "
 "kez (26:82 ve burada); dikey ölçümü ▸sonra günah x16,6 veriyor. Baba yine adlandırılmıyor — "
 "26:70'te de öyleydi."),
87: ("Yıldızın tek kaynağı tek bir edilgen fiil: يُبْعَثُونَ *(diriltilirler)*, iki fiilden biri, "
 "oran 0,50. Ölçülebilir bir istek yönü: dua bir OLUMSUZLAMA — وَلَا تُخْزِنِى *(beni rezil etme)*; "
 "önceki üç istek olumluydu (bağışla, kat, nasip et, kıl), bu dördüncü ve olumsuz. خزي *(rezil "
 "olma/etme)* korpusta 26 geçişli ve dikey ölçümü ▸sonra kıyâmet x11,8 · dünya x12,0 veriyor — "
 "**kök korpusta zaten bu güne bağlı**, yani terkip bu ayete özgü değil. Ve بعث *(gönderme; "
 "diriltme)* burada 'diriltme' anlamında; 26:36 ve 26:51'de 'gönderme' anlamındaydı (aday 529 "
 "sınıfı)."),
88: ("Ölçülebilir bir tek uçlu kullanım: نفع *(fayda)* okumada dördüncü kez ve **ilk kez ضرر "
 "*(zarar)* olmadan**. Önceki üç geçişte (25:3, 25:55, 26:73) çift hâlindeydi ve dikey ölçüm çiftin "
 "iki yönden bağlı olduğunu gösteriyordu; burada karşıtı yok ve yerine مَالٌ وَلَا بَنُونَ *(mal ve "
 "oğullar)* ikilisi geçiyor. Bu, 25:6'daki سرر *(sır, gizleme)*, 25:46'daki يسر *(kolaylık)* ve "
 "26:60'taki شرق *(doğu, tan)* ile aynı desen: **korpusta karşıtıyla yaşayan kök tek uçlu "
 "kullanılıyor.** مول *(mal)* korpusta 86 geçişli ve dikey ölçümü ▸sonra ولد *(doğurma, çocuk)* "
 "x12,3 veriyor — 'mal ve evlat' çifti korpusta sabit."),
89: ("**Sûrenin ilk Allah lafzı burada — ilk 88 ayette lafız sıfırdı.** allah z=2,80 ve yıldızın tek "
 "kaynağı. Ölçülebilir bir gecikme karşılaştırması: sûre 25'in ilk lafzı 25:17'deydi (göreli konum "
 "0,22), sûre 26'nınki 26:89'da (0,39) — **iki Mekkî sûrede de lafız geç giriyor ama sûre 26'da çok "
 "daha geç.** İstisna HASR ile kuruluyor ve şart bir hâl: بِقَلْبٍ سَلِيمٍ *(temiz bir kalple)*. "
 "قلب *(çevirme; kalp)* korpusta 168 geçişli ve dikey ölçümü ▸önce طبع *(mühürleme)* x39,4 · قسو "
 "*(katılaşma, kasvet)* x31,0 veriyor — **kök korpusta ağırlıkla kalbin BOZULMASI bağlamında, burada "
 "sağlamlığı**; karşıt kutup. SINIR: 'kalp' burada bir organ değil bir hâl adı; anatomik hiçbir şey "
 "söylenmiyor."),
90: ("Üç kelime, tek fiil ve o da edilgen — oran 1,00, pas z=5,38, yıldızın tek kaynağı. Ölçülebilir "
 "bir kutup düzelmesi: زلف *(yaklaştırma, zülfe)* 26:64'te أَزْلَفْنَا ثَمَّ ٱلْءَاخَرِينَ "
 "*(ötekileri oraya yaklaştırdık)* ETKEN ve helâke yaklaştırmaydı; dikey ölçüm o zaman kökün korpus "
 "tabanının OLUMLU olduğunu göstermişti (▸sonra حسن *(güzellik, iyilik)* x10,6). Burada أُزْلِفَتِ "
 "ٱلْجَنَّةُ لِلْمُتَّقِينَ *(cennet sakınanlara yaklaştırıldı)* — EDİLGEN ve korpus taban anlamı. "
 "**26:64 azınlık kullanımdı, 26:90 çoğunluk.** Ve جَنَّة *(cennet)* burada marife olduğu için aktör "
 "tablosuna giriyor, oysa 26:85'te tamlama başıydı ve girmemişti — tablonun ölçütü belirlilik gibi "
 "görünüyor."),
}

ATLAMA = {
 "_mercek_26_83": ("26:83 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. رَبِّ هَبْ لِى حُكْما وَأَلْحِقْنِى "
  "بِٱلصَّٰلِحِينَ. Tek kaynak rab z=3,23 (n=6, oran 0,17). İçerik bir dua."),
 "_mercek_26_90": ("26:90 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. وَأُزْلِفَتِ ٱلْجَنَّةُ لِلْمُتَّقِينَ. "
  "Tek kaynak pas z=5,38 (n=3, ayetin tek fiili edilgen, oran 1,00). İçerik bir âhiret sahnesi."),
 "_blok_notu_26_81_90": ("BLOK BİLANÇOSU: ★★★ 2 (26:83, 26:90) · ★★ 2 (26:87, 26:89) · ★ 0 · 6 ayet "
  "yıldızsız. Kaynaklar: rab x1 · pas x2 · allah x1 — HİÇBİRİ İÇERİKTEN, ve hiçbirinde çıpa yok. "
  "SÛRE 26'NIN OKUNAN 90 AYETİNDE ★★★ 17; çıpası olan tek ★★★ ayet hâlâ 26:63 (aday 646). "
  "**26:89 SÛRENİN İLK ALLAH LAFZI**: ilk 88 ayette lafız sıfır; sûre 25'te ilk 16 ayetti. "
  "İki Mekkî sûrede de lafız geç giriyor, sûre 26'da çok daha geç (göreli konum 0,22 / 0,39)."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(81, 91):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 90/227.** Devam: 26:91'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-90 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1812
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(81, 91):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
