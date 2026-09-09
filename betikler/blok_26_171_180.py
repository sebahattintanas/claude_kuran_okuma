# -*- coding: utf-8 -*-
"""blok_26_171_180.py — sûre 26 on beşinci blok (26:171-180). İki ön-kaydın son sınaması."""
import json
DIK = json.load(open('blok_dikey_26_171_180.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
171: "Ancak geride kalanlar arasındaki bir yaşlı kadın başka.",
172: "Sonra ötekileri yerle bir ettik.",
173: "Üzerlerine bir yağmur yağdırdık; uyarılanların yağmuru ne kötüdür.",
174: "Bunda elbette bir âyet var; ama onların çoğu inanmıyor.",
175: "Rabbin, elbette o Azîz'dir, Rahîm'dir.",
176: "Eyke halkı da elçileri yalanladı.",
177: "Şuayb onlara demişti: Sakınmıyor musunuz?",
178: "Ben size güvenilir bir elçiyim.",
179: "Allah'tan sakının ve bana itaat edin.",
180: "Buna karşılık sizden bir ücret istemiyorum; benim ücretim ancak âlemlerin Rabbine aittir.",
}

O = {
171: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — عَجُوز *(yaşlı kadın)* aktör tablosuna "
 "GİRMİYOR · edim haber, kip RES 1 · **şahıs eki YOK, fiil YOK** · n=4 mora=26 harf=18 (n z=-0,89), "
 "fâsıla ٱلْغَٰبِرِينَ *(geride kalanlar)* → ن, N sınıfı; i'râb ACC 1 · GEN 1; **biçim HASR**; "
 "**dış düğüm 1** · yıldız ★ yok · **esit: 37:135 ile TAM AYET ÖZDEŞ** · kökler عجز *(âciz bırakma; "
 "acizlik)* · غبر *(geride kalma; toz)* · bağ: **غبر *(geride kalma; toz)* korpusta SEKİZ geçişli "
 "ve dikey ölçümü ▸önce kadın x153,4 · ▸sonra yağmur x399,0 veriyor — okumada görülen EN YÜKSEK "
 "İKİNCİ komşuluk katı; 'geride kalan kadın' ve 'yağmur' üçlüsü korpusta neredeyse ayrılmaz ve "
 "İKİSİ DE bu bölütte** (elle, L1, aday 729)"),
172: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "1P x2 — ayette başka şahıs yok**, iltifât 0 · n=3 mora=22 harf=15 (n z=-1,00), fâsıla "
 "ٱلْءَاخَرِينَ *(ötekiler)* → ن, N sınıfı — **26:64 ve 26:66'nın fâsılasıyla AYNI KELİME, üçüncü "
 "kez**; **i'râb ACC 1**; bab II x1; zaman PERF 1; **dış düğüm 1** · yıldız ★ yok · **esit: 37:136 "
 "ile TAM AYET ÖZDEŞ** · kökler دمر *(yerle bir etme)* · أخر *(geciktirme, sonraya bırakma)* · "
 "bağ: **25:36 ile دمر *(yerle bir etme)* ikinci geçişi** — orada فَدَمَّرْنَٰهُمْ تَدْمِيرا "
 "*(darmadağın ettik)* fiil + mef'ûl-i mutlak, burada ثُمَّ دَمَّرْنَا ٱلْءَاخَرِينَ; **aynı kök, "
 "aynı bab II, MM'siz**; **26:64 ↔ 26:66 çiftinin ÜÇÜNCÜ eşyapılı üyesi** (elle, L1, aday 730)"),
173: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "1P x2 · 3MP x1 · 3MS x1, iltifât 0 · n=6 mora=41 harf=33 (n z=-0,68), fâsıla ٱلْمُنذَرِينَ "
 "*(uyarılanlar)* → ن, N sınıfı; i'râb ACC 1 · NOM 1 · GEN 1; bab I x1 · IV x1; zaman PERF x2; "
 "**kök ikilemesi مطر *(yağmur; yağdırma)* x3 — SÛRE 26'DA BİR AYETTE AYNI KÖĞÜN ÜÇ KEZ GEÇTİĞİ "
 "İKİNCİ YER** (birincisi 26:19 فعل); **dış düğüm 1** · yıldız ★ yok · **esit: 27:58 ile TAM AYET "
 "ÖZDEŞ** · kökler مطر *(yağmur; yağdırma)* · سوأ *(kötülük)* · نذر *(uyarma; adak)* · bağ: xref "
 "ÜÇ 3-gram → **üçü de 27:58**; **25:40 ile مطر ikinci geçişi** — orada مَطَرَ ٱلسَّوْءِ *(kötü "
 "yağmur)* bir helâk adıydı, burada aynı terkip fiil + mef'ûl-i mutlak yapısında (elle, L1, aday 731)"),
174: ("eksen: **lafız YOK · Rab YOK** · **esmâ مُؤْمِن *(mümin)* 8. sırada = fâsıla — ARTEFAKT, on "
 "ikinci token** · aktör yok · edim haber, kip EMPH 1 · NEG 1 · şahıs 3MS x1 · 3MP x1, iltifât 0 · "
 "n=8 mora=40 harf=32 (n z=-0,47), fâsıla مُّؤْمِنِينَ → ن, N sınıfı; i'râb ACC 3 · NOM 1; bab I "
 "x1; zaman PERF 1; **açık sayı sözcüğü: كثر *(çokluk)* → أَكْثَر *(çoğu)***; **NAKARAT alanı = 6, "
 "temsil ayet 26:8**; **esit: 26:8, 67, 103, 121, 190 ile TAM AYET ÖZDEŞ** · dış düğüm 0 · yıldız "
 "★ yok · kökler أيي *(âyet, işaret)* · كون *(olmak; mekân, yer)* · كثر *(çokluk)* · أمن *(güven; "
 "iman)* · bağ: **ADAY 720'NİN ÖN-KAYDI SINANIYOR — birinci nakarat STANDALONE, GÖMÜLÜ DEĞİL; "
 "TAHMİN TUTTU** (elle, L1, aday 732)"),
175: ("eksen: **lafız YOK · رَبّ *(Rab)* 2. sırada — otuz ikinci Rab**, **rab z=3,94: yıldızın TEK "
 "kaynağı** · **esmâ عَزِيز *(azîz)* + رَحِيم *(rahîm)* = fâsıla — MÜHÜR; GEÇERLİ; yedinci mühür** · "
 "aktör yok · edim haber, kip EMPH 1 · şahıs 2MS x1 · 3MS x1, iltifât 0 · n=5 mora=28 harf=21 "
 "(n z=-0,79), fâsıla ٱلرَّحِيمُ → م, N sınıfı; **i'râb ACC 2 · NOM 2; fiil YOK**; **NAKARAT alanı "
 "= 8, temsil ayet 26:9**; **esit: yedi ayetle TAM ÖZDEŞ** · dış düğüm 0 · **yıldız ★★★** · kökler "
 "ربب *(rab, terbiye etme)* · عزز *(izzet, üstünlük)* · رحم *(rahmet, merhamet)* · bağ: **ADAY "
 "720'NİN ÖN-KAYDI TUTTU — nakarat ÇİFTİ Lût kıssasında BÜTÜN** (26:174-175, ikisi de standalone); "
 "Hûd (26:139-140) ve Sâlih (26:158-159) kırıktı (elle, L1, aday 732)"),
176: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — **أَصْحَٰبُ لْـَٔيْكَةِ *(Eyke halkı)* "
 "aktör tablosuna GİRMİYOR; oysa عاد, ثَمُود, نُوح, لُوط girmişti** (aday 462/667) — SÛRENİN "
 "YEDİNCİ VE SON KISSASI AÇILIYOR · edim haber, kip işareti yok · **şahıs 3MS x1 — ayette başka "
 "şahıs yok**, iltifât 0 · n=4 mora=24 harf=20 (n z=-0,89), fâsıla ٱلْمُرْسَلِينَ *(gönderilenler)* → "
 "ن, N sınıfı — **beşinci kez**; i'râb NOM 1 · GEN 1 · ACC 1; bab II x1; zaman PERF 1; dış düğüm "
 "0 · yıldız ★ yok · kökler كذب *(yalan; yalanlama)* · صحب *(arkadaşlık; ehli)* · رسل *(gönderme, "
 "elçi)* · bağ: **ADAY 721'İN ÖN-KAYDI SINANIYOR — TAHMİN TUTTU**: açılış ne saf tamlama ne saf "
 "tek ad; ÜÇÜNCÜ BİR BİÇİM ve n=4. **VE ÖNGÖRMEDİĞİM BİR ÖĞE: fiil كَذَّبَ (eril), öteki dört "
 "açılışta كَذَّبَتْ (dişil)** — beş açılışın dördü dişil, biri eril (elle, L1, aday 733)"),
177: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı شُعَيْب *(Şuayb)* 4. sırada, rol "
 "FAİL** · edim soru, kip INTG 1 · NEG 1 · şahıs 3MS x1 · 3MP x1 · 2MP x2, iltifât 0 · n=6 mora=27 "
 "harf=20 (n z=-0,68), fâsıla تَتَّقُونَ *(sakınmıyor musunuz)* → ن, N sınıfı — **beşinci kez**; "
 "**i'râb NOM 1**; bab I x1 · VIII x1; zaman PERF 1 · IMPF 1; dış düğüm 0 · yıldız ★ yok · kökler "
 "قول *(söz söyleme)* · وقي *(sakınma, koruma)* · bağ: **ADAY 722'NİN SON SINAMASI — öğe (ii) "
 "ŞUAYB KISSASINDA DA VAR; TAHMİN TAMAMEN DÜŞTÜ**. **AMA ÖNGÖRMEDİĞİM BİR YAPI FARKI VAR: أخو "
 "*(kardeş)* YOK** — öteki dört kıssada إِذْ قَالَ لَهُمْ أَخُوهُمْ + elçi adı, burada إِذْ قَالَ "
 "لَهُمْ شُعَيْبٌ; **n=6, ötekiler n=7** (elle, L1, aday 734)"),
178: ("eksen: **lafız YOK · Rab YOK** · esmâ yok — **أَمِين *(güvenilir)* esmâ SAYILMIYOR ve bu "
 "DOĞRU** · aktör yok · edim haber, kip işareti yok · **şahıs eki YOK, fiil YOK** · n=4 mora=21 "
 "harf=15 (n z=-0,89), fâsıla أَمِينٌ *(güvenilir)* → ن, N sınıfı; **i'râb ACC 1 · NOM 2**; "
 "**NAKARAT alanı = 5, temsil ayet 26:107 — KÜME TAMAMLANDI (5/5)**; **esit: 26:107, 125, 143, 162 "
 "ile TAM AYET ÖZDEŞ** · dış düğüm 0 · yıldız ★ yok · kökler رسل *(gönderme, elçi)* · أمن *(güven; "
 "iman)* · bağ: **ÖN-KAYIT ÖĞESİ (iii) VAR; üçüncü nakarat kümesi TAMAMLANDI** (elle, L1, aday 734)"),
179: ("eksen: **ALLAH LAFZI 2. sırada — sûrenin ON BİRİNCİ lafzı**, **allah z=6,14: yıldızın TEK "
 "kaynağı** · Rab yok · esmâ yok · aktör yok · edim emir, kip IMPV 2 · şahıs 2MP x4 · 1S x1, "
 "iltifât 0 · n=3 mora=23 harf=18 (n z=-1,00), fâsıla وَأَطِيعُونِ *(bana itaat edin)* → ن, N "
 "sınıfı; **i'râb ACC 1**; bab IV x1 · VIII x1; zaman IMPV x2; **NAKARAT alanı = 8, temsil ayet "
 "26:108 — KÜME TAMAMLANDI (8/8)**; **esit: yedi ayetle TAM ÖZDEŞ** · dış düğüm 0 · **yıldız ★★★** · "
 "kökler وقي *(sakınma, koruma)* · أله *(ilâh; lafza-i celâl)* · طوع *(güç yetirme, itaat)* · bağ: "
 "**ÖN-KAYIT ÖĞESİ (iv) VAR; dördüncü nakarat kümesi TAMAMLANDI — SEKİZ AYETİN SEKİZİ DE ★★★ ve "
 "sekizinde de allah z=6,14** (aday 683 doğrulandı) (elle, L1, aday 734)"),
180: ("eksen: **lafız YOK · رَبّ *(Rab)* 10. sırada — otuz üçüncü Rab** (rab z=1,62: yıldızın TEK "
 "kaynağı) · esmâ yok · aktör yok · edim haber, kip NEG 2 · RES 1 · şahıs 1S x2 · 2MP x1 · 3MS x1, "
 "iltifât 0 · n=11 mora=50 harf=40 — **blokta en uzun ayet** (n z=-0,15), fâsıla ٱلْعَٰلَمِينَ "
 "*(âlemler)* → ن, N sınıfı; **i'râb GEN 3 · NOM 1**; bab I x1; zaman IMPF 1; **kök ikilemesi أجر "
 "*(ücret, karşılık)* x2**; **biçim HASR**; simetri [4,1,6,1]; **NAKARAT alanı = 5, temsil ayet "
 "26:109 — KÜME TAMAMLANDI (5/5)**; **esit: 26:109, 127, 145, 164 ile TAM ÖZDEŞ** · dış düğüm 0 · "
 "**yıldız ★** · kökler سأل *(isteme, dileme)* · أجر *(ücret, karşılık)* · ربب *(rab, terbiye "
 "etme)* · علم *(bilme; âlem)* · bağ: **ÖN-KAYIT ÖĞESİ (v) VAR; beşinci nakarat kümesi TAMAMLANDI**; "
 "**aday 602'nin karşı yönlü kanıtı BEŞİNCİ kez** — üç kelimelik 26:179 ★★★, on bir kelimelik bu "
 "ayet ★ (elle, L1, aday 734)"),
}

M = {
171: ("Dört kelime, fiil yok, HASR ile sınırlı: إِلَّا عَجُوزا فِى ٱلْغَٰبِرِينَ *(ancak geride "
 "kalanlar arasındaki bir yaşlı kadın başka)*. Ayet 37:135 ile TAM ÖZDEŞ ve esit yakalıyor. "
 "**Ölçülebilir bir komşuluk yoğunluğu: غبر *(geride kalma; toz)* korpusta sekiz geçişli ve dikey "
 "satırı ▸önce kadın x153,4 · ▸sonra yağmur x399,0 veriyor — okumada görülen en yüksek ikinci "
 "komşuluk katı** (birincisi 26:119'un شحن x301,6'sıydı; bu onu geçiyor). Ve **iki komşu da bu "
 "bölütte**: 'kadın' bu ayette, 'yağmur' iki ayet sonra. Yani üçlü korpusta neredeyse ayrılmaz ve "
 "sahne ayete özgü değil. عَجُوز *(yaşlı kadın)* aktör tablosuna girmiyor."),
172: ("Üç kelime ve 37:136 ile tam özdeş. Ölçülebilir bir eşyapı üçlüsü: 26:64 وَأَزْلَفْنَا ثَمَّ "
 "ٱلْءَاخَرِينَ *(ötekileri yaklaştırdık)*, 26:66 ثُمَّ أَغْرَقْنَا ٱلْءَاخَرِينَ *(sonra ötekileri "
 "boğduk)*, burada ثُمَّ دَمَّرْنَا ٱلْءَاخَرِينَ *(sonra ötekileri yerle bir ettik)* — **üç ayet, "
 "aynı n=3, aynı fâsıla, aynı 1P, değişen yalnız fiil** (aday 642'nin üçüncü üyesi). Ve دمر *(yerle "
 "bir etme)* 25:36'dan geri geliyor: orada فَدَمَّرْنَٰهُمْ تَدْمِيرا mef'ûl-i mutlaklı, burada "
 "MM'siz; aynı kök, aynı bab II, iki yapı. Kök korpusta on geçişli ve dikey ölçümü ▸önce hiçbir "
 "komşu vermiyor."),
173: ("Kök ikilemesi **üç kez**: وَأَمْطَرْنَا عَلَيْهِم مَّطَرا فَسَآءَ مَطَرُ ٱلْمُنذَرِينَ — مطر "
 "*(yağmur; yağdırma)* fiil + mef'ûl-i mutlak + isim. **Sûre 26'da bir ayette aynı kökün üç kez "
 "geçtiği ikinci yer** (birincisi 26:19'daki فعل *(yapma, işleme)*). Üç 3-gram'ın üçü de 27:58'e "
 "düşüyor ve ayet o ayetle **tam özdeş** — donmuş kalıp adayı. Ve 25:40 ile karşılaştırma: orada "
 "مَطَرَ ٱلسَّوْءِ *(kötü yağmur)* bir helâk **adıydı**, burada aynı terkip bir **eylem** yapısında. "
 "Dikey ölçüm مطر için ▸önce geride-kalan x502,7 veriyor — **okumada görülen en yüksek komşuluk "
 "katı**; iki ayet önceki ٱلْغَٰبِرِينَ."),
174: ("**Aday 720'nin ön-kaydı sınanıyor ve tutuyor.** 26:159'da şöyle yazmıştım: *'26:174 ve 26:190 "
 "nakarat listesinde standalone görünüyor, yani tahmin: Lût ve Şuayb kıssalarında çift yine bütün "
 "olacak.'* **Birinci nakarat burada STANDALONE** (n=8, nakarat alanı 6, esit beş ayet) — gömülü "
 "değil. Hûd (26:139) ve Sâlih (26:158) kıssalarında gömülüydü. Ve fâsıladaki مُؤْمِن sûrenin on "
 "ikinci artefaktı; nakarat esmâ sayımını da şişiriyor (aday 700)."),
175: ("**Ön-kayıt tuttu: nakarat çifti Lût kıssasında BÜTÜN.** Ölçülebilir mimari tablo artık beş "
 "kıssada tam: Mûsâ (26:67-68) bütün · İbrâhîm (26:103-104) bütün · Nûh (26:121-122) bütün · Hûd "
 "(26:139-140) **kırık** · Sâlih (26:158-159) **kırık** · Lût (26:174-175) bütün. **Yani kırıklık "
 "ardışık iki kıssada ve sonra düzeliyor** — ön-kaydın öngörmediği bir desen. Sûrenin yedi mühürlü "
 "konumunun yedisi de geçerli."),
176: ("**Aday 721'in ön-kaydı sınanıyor ve tutuyor.** 26:160'ta şöyle yazmıştım: *'Şuayb kıssası "
 "(26:176) — kavmi Eyke halkı olarak biliniyorsa açılış tamlama değil bir başka biçim olabilir; "
 "tahmin: n=4 ve tamlama benzeri bir yapı.'* **Sonuç: n=4 ve أَصْحَٰبُ لْـَٔيْكَةِ *(Eyke halkı)* — "
 "tamlama benzeri ama 'kavim + elçi adı' değil, bir YER/TOPLULUK adı.** Tahmin tuttu. **AMA "
 "ÖNGÖRMEDİĞİM BİR ÖĞE ÇIKTI: fiil كَذَّبَ (eril); öteki dört açılışta كَذَّبَتْ (dişil)** — beş "
 "açılışın dördü dişil, biri eril, çünkü أَصْحَٰب eril çoğul. Ve أَصْحَٰبُ لْـَٔيْكَةِ aktör "
 "tablosuna **girmiyor**, oysa عاد, ثَمُود, نُوح, لُوط girmişti (aday 462/667)."),
177: ("**Aday 722'nin son sınaması ve tahmin TAMAMEN düştü.** أَلَا تَتَّقُونَ Şuayb kıssasında da "
 "**var** — beş kıssanın beşinde de. **AMA öngörmediğim gerçek bir yapı farkı burada:** öteki dört "
 "kıssada إِذْ قَالَ لَهُمْ **أَخُوهُمْ** + elçi adı (n=7); burada **أخو *(kardeş)* YOK** — إِذْ "
 "قَالَ لَهُمْ شُعَيْبٌ (n=6). **Yani Şuayb'ın açılışı gerçekten farklı, ama farklılık benim "
 "tahmin ettiğim öğede değil.** Bu, ön-kaydın 'yön' olarak bir şey sezdiğini ama 'öğe' olarak "
 "yanlış yeri gösterdiğini kaydeder."),
178: ("**Üçüncü nakarat kümesi tamamlandı: 5/5.** Dört kelime, fiil yok. Ve `أَمِين` esmâ "
 "sayılmıyor — doğru; sûrenin on iki مُؤْمِن artefaktı aynı kökten (aday 709). Küme üyeleri: "
 "26:107 (Nûh), 125 (Hûd), 143 (Sâlih), 162 (Lût), 178 (Şuayb) — **beş kıssanın beşinde de**."),
179: ("**Dördüncü nakarat kümesi tamamlandı: 8/8 — ve sekizinin sekizi de ★★★, sekizinde de allah "
 "z=6,14.** Aday 683'ün sayımı doğrulandı: sûrenin 41 ★★★ ayetinin sekizi tek bir ayetin "
 "tekrarından geliyor. Üç kelime, iki emir, tek lafız. Küme üyeleri: 26:108, 110 (Nûh), 126, 131 "
 "(Hûd), 144, 150 (Sâlih), 163 (Lût), 179 (Şuayb)."),
180: ("**Beşinci nakarat kümesi tamamlandı: 5/5.** Kök ikilemesi أجر *(ücret, karşılık)* x2, HASR, "
 "simetri [4,1,6,1]. Ve **aday 602'nin karşı yönlü kanıtı beşinci kez**: aynı bölütte üç kelimelik "
 "26:179 ★★★ alıyor, on bir kelimelik bu ayet ★ alıyor — ikisinin de kaynağı eksen oranı, ikisinde "
 "de içerik ölçülmüyor. **Beş kıssada beş kez aynı çift**: kısa nakarat ★★★, uzun nakarat ★."),
}

ATLAMA = {
 "_mercek_26_175_179": ("26:175 ve 26:179 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. İkisi de NAKARAT: "
  "26:175 ikinci kümenin yedinci geçişi (rab z=3,94), 26:179 dördüncü kümenin sekizinci ve SON "
  "geçişi (allah z=6,14). Bağımsız gözlem değil (adaylar 606, 683, 700, 707)."),
 "_blok_notu_26_171_180": ("BLOK BİLANÇOSU: ★★★ 2 (26:175, 179) · ★★ 0 · ★ 1 (26:180) · 7 ayet "
  "yıldızsız. **İKİ ★★★ AYETİN İKİSİ DE NAKARAT**; hiçbirinde çıpa yok. ÇIPA NOTU: 26:173 bir "
  "yağış olayı adlandırıyor (مَطَر *(yağmur)*) ve bir nitelik veriyor (سَآءَ *(ne kötü)*) ama ne "
  "mekanizma ne ölçü ne süreç — 25:40'ın مَطَرَ ٱلسَّوْءِ vakasıyla aynı sınıf ve orada da çıpa "
  "sayılmamıştı. **İKİ ÖN-KAYIT SINANDI: aday 720 TUTTU (nakarat çifti Lût'ta bütün), aday 721 "
  "TUTTU (Şuayb açılışı üçüncü biçim, n=4); aday 722 TAMAMEN DÜŞTÜ (öğe (ii) Şuayb'da da var) "
  "— ama Şuayb açılışında öngörmediğim gerçek bir fark çıktı: أخو *(kardeş)* YOK.** ÜÇ NAKARAT "
  "KÜMESİ TAMAMLANDI: üçüncü (5/5), dördüncü (8/8), beşinci (5/5). SÛRE 26'NIN OKUNAN 180 "
  "AYETİNDE ★★★ 38."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(171, 181):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 180/227.** Devam: 26:181'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-180 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1902
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(171, 181):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
