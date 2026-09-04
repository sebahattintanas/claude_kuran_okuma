# -*- coding: utf-8 -*-
"""blok_23_1_20.py — sûre 23 makro profili + blok 23:1-20 kaydı."""
import json

DIK = json.load(open('blok_dikey_23_1_20.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MAKRO = {
 "ad": "MÜ'MİNÛN", "ayet": 118, "kelime": 1050, "ort_kelime": 8.90,
 "tip": "Mekkî", "nuzul": "74 (BELLEKTEN, doğrulanmadı)",
 "eksen": "**Allah 13 geçiş (0,0124 = 0,35x) · Rab 23 geçiş (0,0219 = 1,72x) · A/R = 0,57.** Üç komşu sûre A/R'de 0,43 (21) → 9,38 (22) → 0,57 (23) çiziyor: Hac tek başına bir tepe, Mü'minûn Enbiyâ'nın oranına dönüyor ama AYNI YERDEN DEĞİL — Enbiyâ'da hem lafız hem Rab düşüktü, burada lafız düşük ve **Rab okumada bugüne dek görülen en yüksek yoğunlukta**. Allah 12 ayette: 14, 23, 24, 28, 32, 38, 85, 87, 89, 91, 116, 117. Rab 22 ayette: 26, 29, 39, 52, 57, 58, 59, 60, 72, 76, 86, 93, 94, 97, 98, 99, 106, 107, 109, 116, 117, 118. **En uzun Allah-sessizliği 23:39-84 = 46 ayet** (sûrenin %39'u). (aday 470)",
 "kafiye": "**118/118 ayet tek sınıf: N.** Son harf ن 114 · م 4. Kafiye kırılması işaretli ayet SIFIR. Korpusta 50+ ayetli tek-sınıflı sûreler: **23 (118) · 21 (112) · 18 (110) · 27 (93) · 54 (55) · 68 (52)** — Mü'minûn korpusun en uzun tek-kafiye-sınıfı sûresi, ikincisi iki sûre önce okunan Enbiyâ; aralarında duran Hac ise 10 sınıfla üst uçta. (aday 466)",
 "esma": "**12 token / 11 ayet / mühür SIFIR** (Hac'ta 38 token, 11 mühür). مُؤْمِن *(mü'min)* ×2 · آخِر *(son; âhiret)* ×2 · وارِث *(vâris)* · خالِق *(yaratan)* · مُبِين *(apaçık)* · عَلِيم *(alîm)* · عالِم *(bilen)* · أَحَد *(bir, biri)* · مَلِك *(melik)* · كَرِيم *(kerîm)*. **BAĞLAM DENETİMİ (adaylar 444/461): 8/12 kesin yanlış pozitif = %67, okumada ölçülen EN YÜKSEK oran** (20: %38 · 21: %47 · 22: %29). Yanlış: 23:1 · 23:10 · 23:33 · 23:38 · 23:45 · 23:74 · 23:99 · 23:116 كَرِيم. Geçerli: 23:51 عَلِيم · 23:92 عالِم · 23:116 مَلِك. ŞÜPHELİ: 23:14 خالِق — çoğul (ölçüt b dışlıyor) ama أَحْسَنُ ٱلْخَٰلِقِينَ *(yaratanların en güzeli)* lafza bağlıyor (ölçüt a tutuyor); iki ölçüt çatışıyor. Mühürsüz sûrede hata tavan yapıyor — yedinci onarım ölçütünün tersten doğrulaması. (aday 467)",
 "soz_edimi": "haber 76 · emir 26 · soru 14 · şart 9 · yasak 3 · nida 2",
 "fig": "HASR 11 · DIKKAT 6 · IDRAB 6 · NEHY 3 · KELLA 1",
 "dilbilgisi": "i'râb ACC 155 · GEN 150 · NOM 130 · zaman PERF 126 · IMPF 95 · IMPV 32 · bab I 174 · IV 42 · VIII 11 · II 9 · V 6 · III 4 · VI 4 · X 3 · edilgen 17 fiil / 17 ayet · **iltifât 7 ayette: 23:12 (3>1) · 23:15 (13>2) · 23:37 (2>13) · 23:53 (12>3) · 23:84 (1>23) · 23:116 (12>3) · 23:118 (3>12)** — Hac'ta yalnız 1 vardı",
 "yildiz": {"0": 81, "1": 7, "2": 14, "3": 16},
 "yildiz3": [16, 22, 26, 36, 39, 58, 59, 83, 85, 86, 87, 89, 93, 94, 98, 104],
 "hapaks": "**Yalnız tek ayette: 23:104** — كلح *(dişlerin sırıtacağı biçimde yüzün buruşması)* ve لفح *(alevin yüzü yalaması)*, ikisi bir arada. 118 ayette bir tek hapaks ayeti, ve o da çift-hapaks (aday 440'ın 33 vakasından biri).",
 "esit": "**23:5-8 ↔ 70:29-32 — dört ardışık ayet birebir aynı; korpus taraması bunun EN UZUN ardışık tam-ayet ikizi dizisi olduğunu verdi** (ikinciler üçlü: 15:36-38 ↔ 38:79-81 ve sûre 26 nakaratları). Ayrıca 23:26 ↔ 23:39 (sûre içi) ve 23:43 ↔ 15:5. (aday 465)",
 "aktor": "Dokuz ad: فِرْدَوْس *(Firdevs)* · سَيْناء *(Sînâ)* · نُوح *(Nûh)* · مُوسَى *(Mûsâ)* ×2 · هارُون *(Hârûn)* · فِرْعَوْن *(Firavun)* · مَرْيَم *(Meryem)* · شَيْطان *(şeytan)* · جَهَنَّم *(cehennem)*; adsız racül *(bir adam)* ×2 (23:25, 23:38) ve ferîk *(bir bölük)* ×1 (23:109). **Aday 462 gereği aktör yoğunluğu KARŞILAŞTIRMASI yapılmadı.**",
 "sozluk": "271 farklı kök / 639 kök-token. Korpus payına göre zenginleşme: خلق *(yaratma)* ×3,01 · كذب *(yalanlama)* ×2,23 · ربب *(rab, terbiye etme)* ×1,85 · قول *(söz söyleme)* ×1,60 · قوم *(kalkma; kavim; kıyamet)* ×1,55 · رسل *(gönderme, elçi)* ×1,38; buna karşılık أله *(ilâh; lafza-i celâl)* ×0,52.",
 "en_uzun_kisa": "En uzun **23:27 (n=32)**; en kısa **23:1 ve 23:10 (n=3)**.",
 "not": "Sûre 22 (Hac) TAM okundu (78/78). Blok akışı 20 ayet. Bu sûre Mekkî. Hazır iki bağ: 21:92-93 ↔ 23:52-53 bölüt ikizi (aday 456) ve 23:1-9 sıfat zinciri (ön-kayıtlı testin altı örneğinden biri, aday 469)."
}

MEAL = {
1:"Mü'minler kurtuluşa erdi.",
2:"Onlar ki namazlarında huşû içindedirler.",
3:"Onlar ki boş sözden yüz çevirirler.",
4:"Onlar ki zekâtı işleyenlerdir.",
5:"Onlar ki ırzlarını korurlar.",
6:"Eşleri ya da ellerinin altındakiler dışında; onlar kınanmazlar.",
7:"Kim bunun ötesini ararsa, işte onlar haddi aşanlardır.",
8:"Onlar ki emanetlerini ve ahitlerini gözetirler.",
9:"Onlar ki namazlarını korurlar.",
10:"İşte onlar vâris olanlardır.",
11:"Onlar ki Firdevs'e vâris olurlar; orada kalıcıdırlar.",
12:"Andolsun, insanı çamurdan süzülmüş bir özden yarattık.",
13:"Sonra onu sağlam bir karargâhta nutfe kıldık.",
14:"Sonra nutfeyi alaka olarak yarattık, alakayı bir çiğnem et olarak yarattık, o eti kemikler olarak yarattık, kemiklere et giydirdik; sonra onu bambaşka bir yaratılışla inşa ettik. Yaratanların en güzeli olan Allah ne yücedir.",
15:"Sonra bunun ardından siz elbette öleceksiniz.",
16:"Sonra kıyamet günü siz diriltileceksiniz.",
17:"Andolsun, üstünüzde yedi yol yarattık; yaratmadan da habersiz değiliz.",
18:"Gökten bir ölçüyle su indirdik ve onu yerde durdurduk; onu gidermeye de elbette gücümüz yeter.",
19:"Onunla sizin için hurma ve üzüm bahçeleri inşa ettik; orada sizin için çok meyve var, onlardan yiyorsunuz.",
20:"Ve Sînâ Dağı'ndan çıkan bir ağaç; yağ ve yiyenlere katık bitirir.",
}

OLCUM = {
1:"eksen: lafız yok · Rab yok · **esmâ مُؤْمِن *(mü'min)* 3. sırada — ÖLÇÜM ARTEFAKTI (aday 461)**: ٱلْمُؤْمِنُونَ *(mü'minler)* çoğul, göndergesi insanlar; sûre tablonun en büyük tek hatasıyla açılıyor · aktör yok · edim haber, kip CERT 1 (قَدْ *(muhakkak)*) · şahıs 3MS 1 · n=3 mora=17 harf=33 — **sûrenin en kısa iki ayetinden biri** (öteki 23:10), fâsıla ٱلْمُؤْمِنُونَ → ن, N sınıfı; i'râb NOM 1; bab IV ×1; zaman PERF 1 · yıldız ★ yok · kökler فلح *(kurtuluşa erme, felâh)* · أمن *(güven; iman)* · bağ yok. NOT: besmele okuma metnine dâhil edilmedi; defter de saymıyor (n=3).",
2:"eksen yok · aktör yok · edim haber · şahıs 3MP ×2 · n=5 mora=27 harf=20, fâsıla خَٰشِعُونَ *(huşû duyanlar)* → ن, N sınıfı; i'râb GEN 1 · NOM 1; **fiil yok** · yıldız ★ yok · kökler صلو *(namaz, salât)* · خشع *(huşû, boyun eğme)* · bağ: **23:9 ile halka** — zincirin birinci ve altıncı halkası aynı kök صلو (elle, L1)",
3:"eksen yok · aktör yok · edim haber · şahıs 3MP 1 · n=5 mora=27 harf=21, fâsıla مُعْرِضُونَ *(yüz çevirenler)* → ن, N sınıfı; i'râb GEN 1 · NOM 1; fiil yok · yıldız ★ yok · kökler لغو *(boş söz)* · عرض *(sunma; yüz çevirme)* · bağ yok",
4:"eksen yok · aktör yok · edim haber · şahıs 3MP 1 · n=4 mora=27 harf=19, fâsıla فَٰعِلُونَ *(işleyenler)* → ن, N sınıfı; i'râb GEN 1 · NOM 1; fiil yok · yıldız ★ yok · kökler زكو *(arınma, temizlik)* · فعل *(yapma, işleme)* · bağ: **21:73 ile ters eşleşme** — orada فِعْلَ ٱلْخَيْرَٰتِ … وَإِيتَآءَ ٱلزَّكَوٰةِ *(hayırlar işlemek… ve zekât vermek)*, burada زكاة doğrudan فعل'in nesnesi; korpusta زكو 56 ayette, أتي *(verme)* ile 32 · قوم *(ikame)* ile 30 · فعل ile yalnız 3 (elle, L1, aday 471)",
5:"eksen yok · aktör yok · edim haber · şahıs 3MP ×2 · n=4 mora=27 harf=20, fâsıla حَٰفِظُونَ *(koruyanlar)* → ن, N sınıfı; i'râb GEN 1 · NOM 1; fiil yok; dış düğüm 1 · yıldız ★ yok · kökler فرج *(ırz; yarık, aralık)* · حفظ *(koruma)* · bağ: **tam-ayet ikizi 70:29** — dört ardışık ikizin ilki (aday 465)",
6:"eksen yok · aktör yok · edim haber, kip RES 1 · şahıs 3MP ×3 · 3FS 1 · n=10 mora=53 harf=40, fâsıla مَلُومِينَ *(kınananlar)* → ن, N sınıfı; i'râb GEN 2 · NOM 2 · ACC 1; bab I ×1; zaman PERF 1; sayı sözcüğü زَوْج *(eş, çift)*; biçim HASR; simetri [3,1,4,1]; dış düğüm 2 · yıldız ★ yok · kökler زوج *(eş, çift)* · ملك *(mülk; melik)* · يمن *(sağ el, sağ yan)* · غير *(başka)* · لوم *(kınama, levm)* · bağ: **tam-ayet ikizi 70:30**; xref زوج + ملكت + يمين → 33:50 ve 70:30 (aday 465)",
7:"eksen yok · aktör yok · edim haber · şahıs 3MS 1 · 3MP 1 · n=7 mora=41 harf=31, fâsıla ٱلْعَادُونَ *(haddi aşanlar)* → ن, N sınıfı; i'râb ACC 1 · NOM 1; bab VIII ×1; zaman PERF 1; dış düğüm 1 · yıldız ★ yok · kökler بغي *(iffetsizlik; azgınlık; arama)* · وري *(arka, öte; gizleme)* · عدو *(düşmanlık, düşman)* · bağ: **tam-ayet ikizi 70:31**; xref ابتغى + وراء + عاد → 70:31 (aday 465)",
8:"eksen yok · aktör yok · edim haber · şahıs 3MP ×3 · n=5 mora=33 harf=25, fâsıla رَٰعُونَ *(gözetenler)* → ن, N sınıfı; i'râb GEN 2 · NOM 1; fiil yok; dış düğüm 1 · yıldız ★ yok · kökler أمن *(güven; iman → burada emanet)* · عهد *(ahit, antlaşma)* · رعي *(otlatma, güdme)* · bağ: **tam-ayet ikizi 70:32**; xref أمانة + عهد + راعي → 70:32 (aday 465)",
9:"eksen yok · aktör yok · edim haber · şahıs 3MP ×4 · n=5 mora=32 harf=24, fâsıla يُحَافِظُونَ *(korurlar)* → ن, N sınıfı; i'râb GEN 1; **bab III ×1 · zaman IMPF 1 — zincirin altı halkasında TEK fiil** · yıldız ★ yok · kökler صلو *(namaz, salât)* · حفظ *(koruma)* · bağ: **23:2 ile dış halka (صلو)** ve **23:5 ile iç halka (حفظ)** (elle, L1, aday 469)",
10:"eksen: lafız yok · **esmâ وارِث *(vâris)* 3. sırada — ÖLÇÜM ARTEFAKTI (aday 461)**: ٱلْوَٰرِثُونَ çoğul, göndergesi zincirdeki insanlar · aktör yok · edim haber · şahıs 3MP 1 · n=3 mora=20 harf=15 — **sûrenin en kısa iki ayetinden biri** (öteki 23:1), fâsıla ٱلْوَٰرِثُونَ → ن, N sınıfı; i'râb NOM 1; fiil yok · yıldız ★ yok · kök ورث *(vâris olma)* · bağ: **23:7 ile aynı kalıp** — أُو۟لَٰٓئِكَ هُمُ *(işte onlar)* + ism-i fâil; biri ihlâli biri ödülü işaretliyor (elle, L1)",
11:"eksen yok · **aktör: adlı فِرْدَوْس *(Firdevs)* 3. sırada, tür 'yer', rol mef'ûl** · edim haber · şahıs 3MP ×3 · 3FS 1 · n=6 mora=37 harf=28, fâsıla خَٰلِدُونَ *(kalıcılar)* → ن, N sınıfı; i'râb ACC 1 · NOM 1; bab I ×1; zaman IMPF 1 · yıldız ★ yok · kökler ورث *(vâris olma)* · خلد *(ebedî kalma)* · bağ yok",
12:"eksen yok · aktör yok · edim haber, kip EMPH 1 · CERT 1 · şahıs 1P ×2 · **iltifât 1 (3>1) — sûrenin yedi iltifâtından ilki** · n=7 mora=35 harf=28, fâsıla طِينٍۢ *(çamur)* → ن, N sınıfı; i'râb ACC 1 · GEN 2; bab I ×1; zaman PERF 1 · yıldız ★ yok · kökler خلق *(yaratma)* · أنس *(insan)* · سلل *(süzülüp çıkan öz, sülâle)* · طين *(çamur)* · bağ yok",
13:"eksen yok · aktör yok · edim haber · şahıs 1P ×2 · 3MS 1 · n=6 mora=31 harf=24, fâsıla مَّكِينٍۢ *(sağlam yerleşik)* → ن, N sınıfı; i'râb ACC 1 · GEN 2; bab I ×1; zaman PERF 1 · yıldız ★ yok · kökler جعل *(kılma, var etme)* · نطف *(nutfe)* · قرر *(karar kılma; göz aydınlığı)* · مكن *(yerleştirme, imkân)* · bağ yok",
14:"eksen: **Allah lafzı 19. sırada** (allah z=0,42) · **esmâ خالِق *(yaratan)* 21. sırada — ŞÜPHELİ (aday 461)**: ٱلْخَٰلِقِينَ çoğul biçim, onarım ölçütü (b) çoğulu dışlıyor; ama üstünlük tamlaması أَحْسَنُ ٱلْخَٰلِقِينَ *(yaratanların en güzeli)* göndergeyi lafza bağlıyor — ölçüt (a) ile (b) çatışıyor, kayıt açık bırakıldı · aktör yok · edim haber · şahıs 1P ×10 · 3MS ×2 · **n=21 mora=128 harf=106 — bloğun en uzun ayeti** (n z=0,91), fâsıla ٱلْخَٰلِقِينَ → ن, N sınıfı; i'râb ACC 10 · NOM 2 · GEN 1; bab I ×4 · bab IV ×1 · bab VI ×1; **zaman PERF ×6 — altı fiil, altısı da geçmiş**; **kök ikilemesi خلق *(yaratma)* ×5 · علق *(ilişme, alaka; kan pıhtısı)* ×2 · مضغ *(çiğnenmiş et)* ×2 · عظم *(büyüklük, azamet; kemik)* ×2 — dört ayrı kök tekrarlanıyor** · yıldız ★ yok · kökler خلق · نطف *(nutfe)* · علق · مضغ · عظم · كسو *(giydirme, örtü giydirme)* · لحم *(et)* · نشأ *(inşâ etme, yeni bir şey var etme)* · أخر *(geciktirme, sonraya bırakma; diğer)* · برك *(bereket)* · أله *(ilâh; lafza-i celâl)* · حسن *(güzellik, iyilik)* · bağ yok",
15:"eksen yok · aktör yok · edim haber, kip EMPH 1 · şahıs 2MP 1 · **iltifât 1 (13>2)** · n=5 mora=25 harf=18, fâsıla لَمَيِّتُونَ *(ölecek olanlar)* → ن, N sınıfı; i'râb ACC 2 · NOM 1; **fiil yok** · yıldız ★ yok · kökler بعد *(sonra; uzaklık)* · موت *(ölüm)* · bağ: **23:16 ile aynı açılış** ثُمَّ إِنَّكُمْ *(sonra siz)* (elle, L1)",
16:"eksen yok · aktör yok · edim haber · şahıs 2MP ×3 · n=5 mora=27 harf=21, fâsıla تُبْعَثُونَ *(diriltilirsiniz)* → ن, N sınıfı; i'râb ACC 2 · GEN 1; bab I ×1; zaman IMPF 1; **edilgen 1 — n=5'te tek fiil ve o fiil edilgen, pas z=5,38: bloğun ve yıldızın tek kaynağı** · yıldız ★★★ · kökler يوم *(gün)* · قوم *(kalkma; kavim; kıyamet)* · بعث *(gönderme; diriltme)* · bağ: **23:15 ile aynı açılış** ثُمَّ إِنَّكُمْ *(sonra siz)* (elle, L1)",
17:"eksen yok · aktör yok · edim haber, kip EMPH 1 · CERT 1 · NEG 1 · şahıs 1P ×4 · 2MP 1 · n=10 mora=51 harf=40, fâsıla غَٰفِلِينَ *(habersiz olanlar)* → ن, N sınıfı; i'râb ACC 4 · GEN 1; bab I ×2; zaman PERF ×2; **kök ikilemesi خلق *(yaratma)* ×2 — biri fiil biri masdar**; sayı sözcüğü سَبْع *(yedi)*; simetri [3,1,8,1] · yıldız ★ yok · kökler خلق · فوق *(üst, üstünde)* · سبع *(yedi)* · طرق *(yol)* · كون *(olmak)* · غفل *(gaflet, habersizlik)* · bağ: **23:12 ile aynı açılış** وَلَقَدْ خَلَقْنَا *(andolsun yarattık)*, nesne varlıktan konuma geçiyor (elle, L1)",
18:"eksen yok · aktör yok · edim haber, kip EMPH 1 · şahıs 1P ×5 · 3MS ×2 · n=13 mora=74 harf=59, fâsıla لَقَٰدِرُونَ *(güç yetirenler)* → ن, N sınıfı; i'râb GEN 4 · ACC 2 · NOM 1; bab IV ×2; zaman PERF ×2; **kök ikilemesi قدر ×2 — biri ölçü (بِقَدَرٍ *(bir ölçüyle)*), öteki güç (لَقَٰدِرُونَ *(güç yetirenler)*)**; simetri [3,7,10,1]; dış düğüm 1 · yıldız ★ yok · kökler نزل *(inme, indirme)* · سمو *(ad; gök)* · موه *(su)* · قدر *(ölçü, güç yetirme)* · سكن *(sükûn; mesken, konut)* · أرض *(yer, yeryüzü)* · ذهب *(gitme, götürme)* · bağ: xref سماء + ماء + قدر → **43:11**",
19:"eksen yok · aktör yok · edim haber · şahıs 1P ×2 · 2MP ×4 · 3MS 1 · 3FS ×2 · n=13 mora=72 harf=58, fâsıla تَأْكُلُونَ *(yersiniz)* → ن, N sınıfı; i'râb ACC 1 · GEN 2 · NOM 2; bab I ×1 · bab IV ×1; zaman PERF 1 · IMPF 1; sayı sözcüğü كَثِيرَة *(çok)*; simetri [3,2,8,1] · yıldız ★ yok · kökler نشأ *(inşâ etme, yeni bir şey var etme)* · جنن *(örtme, gizleme; cennet; cin)* · نخل *(hurma)* · عنب *(üzüm)* · فكه *(meyve; şakalaşma)* · كثر *(çokluk)* · أكل *(yeme)* · bağ: **23:14 ile ortak نشأ** — orada insanın son aşaması, burada bahçeler (elle, L2)",
20:"eksen yok · **aktör: adlı سَيْناء *(Sînâ)* 5. sırada, tür 'yer', rol mecrur** · edim haber · şahıs 3FS ×2 · n=9 mora=53 harf=44, fâsıla لِّلْءَاكِلِينَ *(yiyenler için)* → ن, N sınıfı; i'râb ACC 1 · GEN 5; bab I ×2; zaman IMPF ×2 · yıldız ★ yok · kökler شجر *(ağaç)* · خرج *(çıkma, çıkarma)* · طور *(Tûr dağı)* · نبت *(bitki, bitme)* · دهن *(yağ; yağ gibi yumuşama, müdâhene)* · صبغ *(boya; katık)* · أكل *(yeme)* · bağ: **23:19 ile ortak أكل *(yeme)*** — orada muhatap yiyor (تَأْكُلُونَ *(yersiniz)*), burada yiyenler üçüncü şahıs ism-i fâil (ٱلْءَاكِلِينَ *(yiyenler)*) (elle, L1)",
}

MERCEK = {
1:"Üç kelime, üç iş: kesinlik parçacığı, geçmiş zaman fiili, özne. Sonuç en başta ve PERF ile veriliyor — kurtuluş olmuş bitmiş sayılıyor, koşulları henüz sayılmadan. Sözdizimi bunu mümkün kılıyor: özne cümlenin sonunda durduğu için ardına dokuz ayetlik bir niteleme zinciri asılabiliyor. أَفْلَحَ *(kurtuluşa erdi)* bab IV, yani geçişsiz görünen kökün ettirgen kalıbı.",
2:"Zincirin kalıbı burada kuruluyor: ٱلَّذِينَ هُمْ *(onlar ki)* + mecrur + ism-i fâil. Yüklem fiil değil isim — nitelik sürekli hâl olarak veriliyor, olay olarak değil. Edat فِى *(içinde)*, yani konum içerlek. صَلَاة *(namaz)* burada tekil.",
3:"İkinci halka kalıbı korurken edatı değiştiriyor: فِى *(içinde)* → عَنْ *(...den)*. Birincisi bir şeyin içinde bulunmayı, ikincisi bir şeyden uzaklaşmayı kuruyor. Yani zincir olumlu konumdan olumsuz konuma geçiyor ve bunu tek harfle yapıyor. لَغْو *(boş söz)* korpusta 11 geçişli seyrek kök; komşuluğunda tek belirgin öğe سمع *(işitme)*.",
4:"Üçüncü halka üçüncü edatı getiriyor: لِـ *(için)*. Üç halka üç edat — فِى · عَنْ · لِـ. Yüklem seçimi ölçülebilir biçimde sıra dışı: زكو *(arınma, zekât)* korpusta 56 ayette geçiyor ve bunların 32'sinde أتي *(verme)*, 30'unda قوم *(kalkma, ikame)* ile birlikte; فعل *(yapma)* ile yalnız üç ayette (21:73 · 23:4 · 58:13). Bu üçün ikisinde de fiil zekâta değil başka bir nesneye bağlı; zekâtın doğrudan فعل ile eşleştiği tek yer bu ayet.",
5:"Dördüncü halka edatı üçüncüyle aynı tutuyor (لِـ) ama nesneyi bedene taşıyor. Bu, zincirde ilk kez bir sonraki ayete taşan halka: 23:6 ve 23:7 bu halkanın istisnasını ve ihlâlini yazıyor. Yani altı halkadan yalnız biri kendi ayetiyle kapanmıyor. حفظ *(koruma)* kökü zincirin sonunda ikinci kez dönecek.",
6:"İstisna cümlesi zincirin kalıbını bozuyor: ٱلَّذِينَ هُمْ *(onlar ki)* açılışı yok, yerine إِلَّا *(ancak)* var. Ve yüklem ilk kez ism-i mef'ûl: مَلُومِينَ *(kınananlar)*, yani özne edilgen konuma geçiyor. Altı halkanın tamamı ism-i fâil ile kuruluyken istisna cümlesi tersine dönüyor — nitelik yapan değil, yapılmayan üzerinden veriliyor: غَيْرُ مَلُومِينَ *(kınanmış değiller)*.",
7:"İstisnanın da bir sınırı yazılıyor ve bu üçüncü bir kalıpla yapılıyor: şart cümlesi (مَنْ *(kim)* + PERF) ve cevabında işaret zamiri (أُو۟لَٰٓئِكَ *(işte onlar)*). Bu işaret zamiri zincirin kapanışında da kullanılacak (23:10). Yani aynı biçimsel araç bir kez ihlâli, bir kez ödülü işaretlemek için kullanılıyor. وَرَآءَ *(ötesi, arkası)* bir mekân kelimesiyle sınır çiziyor.",
8:"Beşinci halka kalıba dönüyor (ٱلَّذِينَ هُمْ *(onlar ki)* + لِـ + ism-i fâil) ve tek halkada iki nesne taşıyan tek halka: أَمَٰنَٰت *(emanetler)* ve عَهْد *(ahit)*. Kök tarafında ölçülebilir bir dönüş var: أمن *(güven; iman)* kökü sûrenin ilk ayetinde iman anlamındaydı, burada emanet anlamında — aynı kök, kavram katmanında ayrı okunuyor. Yüklem رَٰعُونَ *(gözetenler)*, kökü çobanlık: koruma değil güdme.",
9:"Kapanış halkası aynı anda üç şeyi değiştiriyor ve üçü de ölçülebilir: (1) edat dördüncü kez değişiyor — عَلَىٰ *(üzerine)*; (2) صَلَاة *(namaz)* tekilden صَلَوَٰت *(namazlar)* çoğuluna geçiyor; (3) yüklem ism-i fâil olmaktan çıkıp çekimli fiile dönüyor, ve babı da değişiyor: 23:5'in حَٰفِظُونَ *(koruyanlar)* bab I iken burada يُحَافِظُونَ *(korurlar)* bab III. Ve halkanın iki kökü de zincirde daha önce kullanılmış — altı halkanın yeni kök getirmeyen tek halkası bu. Zincir kapanırken sözlüğünü genişletmiyor, daraltıyor.",
10:"Kapanış 23:1'in aynasında duruyor: sûre üç kelimeyle açıldı, zincir üç kelimeyle kapanıyor, ve iki ayet de fâsılasında bir ism-i fâil çoğulu taşıyor — ٱلْمُؤْمِنُونَ *(mü'minler)* ve ٱلْوَٰرِثُونَ *(vâris olanlar)*. Aradaki fark biçimsel değil zamansal: birincisi fiille (أَفْلَحَ *(kurtuluşa erdi)*), ikincisi fiilsiz kuruluyor.",
11:"Kalıp bir kez daha dönüyor (ٱلَّذِينَ *(onlar ki)*) ama bu kez ardından fiil geliyor, ism-i fâil değil: يَرِثُونَ *(vâris olurlar)*, IMPF. Yani 23:10'un isim cümlesi 23:11'de fiile açılıyor ve fiilin nesnesi bir yer adı. ورث *(vâris olma)* kökü iki ayette üst üste, biri ism-i fâil biri fiil — 23:9'daki حفظ *(koruma)* dönüşümünün aynısı, iki ayet sonra tekrarlanıyor.",
12:"Şahıs burada değişiyor: on bir ayet boyunca üçüncü şahıs anlatılıyordu, ilk kez birinci çoğul konuşuyor — خَلَقْنَا *(yarattık)*. Ve yeni bölüm bir madde adıyla açılıyor. İki ardışık مِنْ *(...den)* bir hiyerarşi kuruyor: özün kaynağı çamur, insanın kaynağı öz. سُلَٰلَة *(süzülüp çıkan öz)* korpusta üç geçişli seyrek kök ve komşuluğunda eşik üstü hiçbir kavram yok — yalıtık duruyor.",
13:"Dizinin ikinci adımı ve fiil değişiyor: خلق *(yaratma)* → جعل *(kılma)*. Yer bilgisi ilk kez veriliyor ve iki kelimeyle: قَرَار *(karargâh, durulan yer)* ve niteleyicisi مَّكِين *(sağlam yerleşik)* — ikisi de yerleşme kökünden değil ama ikisi de yerleşme anlamında; biri durmayı, öteki dayanıklılığı taşıyor. Yer, organ adıyla değil sağlamlık niteliğiyle anılıyor.",
14:"Ayet bir zincir kuruyor ve zinciri sözdizimiyle görünür kılıyor: her adımın nesnesi bir öncekinin yüklemi — نُطْفَة *(nutfe)* → عَلَقَة *(alaka)*, sonra ٱلْعَلَقَة → مُضْغَة *(çiğnem et)*, sonra ٱلْمُضْغَة → عِظَٰم *(kemikler)*. Belirsizlikten belirliliğe geçiş her seferinde harf-i tarifle işaretleniyor: yeni gelen öğe nekre, bir sonraki adımda marife. Dördüncü adımda fiil değişiyor: خلق *(yaratma)* yerine كسو *(giydirme)* — kemik ile et arasındaki ilişki yaratma değil örtme olarak veriliyor. Beşinci adımda hem fiil hem terim değişiyor: أَنشَأْنَٰهُ خَلْقًا ءَاخَرَ *(onu bambaşka bir yaratılışla inşa ettik)* — نشأ *(inşâ)* ve خَلْق burada masdar. Yani beş adımlık dizide dört kez aynı fiil, sonra iki kez başka fiil, ve kapanışta lafız. Ölçülebilir bir asimetri: on ayrı birinci-çoğul şahıs ekinden sonra ayetin son üç kelimesi üçüncü şahsa geçiyor ve fâil olarak lafız adlandırılıyor.",
15:"Şahıs ikinci kez değişiyor: yaratılış dizisi 'o insan' hakkındaydı, burada doğrudan muhataba dönülüyor — إِنَّكُمْ *(siz)*. Ve dizi devam ediyormuş gibi ثُمَّ *(sonra)* ile bağlanıyor, ama önceki adımların hepsi fiille kuruluyken bu adım fiilsiz, ism-i fâil ile: مَيِّتُونَ *(ölecek olanlar)*. Yani ölüm bir eylem olarak değil bir nitelik olarak yazılıyor.",
16:"İki ayet aynı üç kelimeyle açılıp aynı fâsıla sınıfında kapanıyor, ama çatı değişiyor: 23:15 fiilsiz ve edilgen anlamı ism-i fâile yüklüyor, 23:16 çekimli ve edilgen — تُبْعَثُونَ *(diriltilirsiniz)*. Fâil silinmiş. On üç ayettir süren خَلَقْنَا / جَعَلْنَا / أَنشَأْنَا *(yarattık / kıldık / inşa ettik)* birinci-çoğul fâil dizisi burada ilk kez ortadan kalkıyor: yapan söylenmeden yapılan söyleniyor. Zaman da tersine dönüyor — dizinin bütün fiilleri PERF idi, bu IMPF.",
17:"Bölüm 23:12'nin açılışını birebir tekrarlıyor: وَلَقَدْ خَلَقْنَا *(andolsun yarattık)*. Ama nesne yer değiştiriyor — orada ٱلْإِنسَٰن *(insan)*, burada فَوْقَكُمْ *(üstünüzde)*, yani bir varlık değil bir konum. İki yarım aynı kökle bağlanıyor ve kök iki ayrı biçimde geçiyor: fiil خَلَقْنَا, sonra masdar ٱلْخَلْق *(yaratma)*. İkinci yarım olumsuz kuruluyor (مَا كُنَّا … غَٰفِلِينَ *(habersiz değildik)*) — yani yaratma bilgisi doğrudan değil, karşıtının reddiyle veriliyor. طَرِيقَة *(yol)* korpusta 11 geçişli seyrek kök; komşuluğunda eşik üstü tek kavram hidâyet.",
18:"Ayetin ekseni tek kökün iki anlamı: قدر *(ölçü, güç yetirme)* önce indirilen suyun niceliğini, sonra indirenin yetisini adlandırıyor. Aradaki fiil bunu bir yerleştirmeye bağlıyor: أَسْكَنَّٰهُ *(onu durdurduk)*, sükûn kökünden — su hareketle değil hareketsizlikle tarif ediliyor. Ve son cümle işlemi tersine çevirebilme gücünü ekliyor: ذَهَاب *(gidermek)*, yani indirme ile giderme aynı yetiye bağlanıyor. İki fiil de bab IV, yani ikisi de ettirgen.",
19:"Fiil 23:14'ün kapanışından geri geliyor: أَنشَأْنَا *(inşa ettik)* — orada insanın son aşamasını adlandırıyordu, burada bahçeleri. Aynı fiil iki farklı diziyi aynı kelimeyle bitiriyor. Ayet muhataba iki kez لَـ *(için)* ile dönüyor ve ikisinin arasında sahiplik ile bulunma ayrılıyor: لَكُم … لَّكُمْ فِيهَا *(sizin için… orada sizin için)*. Ve kapanış zamanı değiştiriyor: dizinin fiili PERF, son yüklem IMPF — yapılan geçmişte, yenen şimdide.",
20:"Önceki ayet bahçeleri çoğul saymıştı; bu ayet tek bir ağaca iniyor ve tek bir yere bağlıyor — sûrenin ikinci ve son yer adı. İki fiil de üçüncü tekil dişil ve IMPF, yani ağaç kendi eylemiyle anlatılıyor: تَخْرُجُ *(çıkar)* ve تَنۢبُتُ *(bitirir)*. Ürün iki kelimeyle veriliyor ve ikisi de üründen çok kullanımı adlandırıyor: دُهْن *(yağ)* ve صِبْغ *(katık)* — ikincisi kökü boya olan, yani daldırılan şey. صبغ *(boya; katık)* korpusta üç geçişli; öteki ikisi 2:138'de ve orada anlam boya. Aynı kök, iki gönderge.",
}

ATLAMA = {
 "23:16": "★★★ ayet. 🜁 biyolog YAZILMADI — ayette biyolojik çıpa yok: بعث *(gönderme; diriltme)* korpusta iki işlevli, يوم *(gün)* ve قوم *(kalkma; kavim; kıyamet)* zaman terimleri. 🜂 uzay YAZILMADI — gök öğesi, cisim adı ya da yörünge/zaman ölçüsü terimi geçmiyor. Yıldızın tek kaynağı pas z=5,38. NOT: bloğun biyolojik olarak en yoğun ayeti 23:14 yıldız almıyor, dolayısıyla orada da biyolog merceği yazılamıyor (aday 468)."
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
OM.setdefault('23', {})
OM['23']['_makro'] = MAKRO
OM['23']['_mercek_atlama_notu'] = ATLAMA
for n in range(1, 21):
    k = "23:%d" % n
    ar = AR[(23, n)]
    if n == 1:
        ar = ' '.join(ar.split()[4:])   # besmele (4 kelime) çıkarıldı; elle Arapça yazılmadı
    OM['23'][k] = {"ar": ar, "meal": MEAL[n], "olcum": OLCUM[n],
                   "mercek": MERCEK[n], "dikey": DIK[k]}
OM['ilerleme']['not'] = ("Sûre 22 TAM (78/78). Sûre 23 (Mü'minûn) makro profil çıkarıldı, "
                         "23:1-20 okundu. Devam: 23:21. Dikey katman A parçası birincil, B etiketsiz.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "23": "1-20 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1483
OM['ilerleme']['son_oturum'] = 'OTURUM_2026-08-31_KAPANIS.md'
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni.json: sûre 23 →', len([k for k in OM['23'] if not k.startswith('_')]), 'ayet + makro')

# mercek kaydı
pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK.setdefault('23', {})
for n in range(1, 21):
    MK['23']["23:%d" % n] = MERCEK[n]
MK.setdefault('23_atlama', {}).update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit.json: sûre 23 →', len(MK['23']), 'mercek')
