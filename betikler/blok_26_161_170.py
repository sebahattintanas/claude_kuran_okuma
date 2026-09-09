# -*- coding: utf-8 -*-
"""blok_26_161_170.py — sûre 26 on dördüncü blok (26:161-170). Lût kıssası; ön-kaydın asıl sınaması."""
import json
DIK = json.load(open('blok_dikey_26_161_170.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
161: "Kardeşleri Lût onlara demişti: Sakınmıyor musunuz?",
162: "Ben size güvenilir bir elçiyim.",
163: "Allah'tan sakının ve bana itaat edin.",
164: "Buna karşılık sizden bir ücret istemiyorum; benim ücretim ancak âlemlerin Rabbine aittir.",
165: "Âlemler içinde erkeklere mi gidiyorsunuz?",
166: "Rabbinizin sizin için yarattığı eşlerinizi bırakıyorsunuz. Hayır, siz haddi aşan bir topluluksunuz.",
167: "Dediler: Ey Lût, vazgeçmezsen mutlaka çıkarılanlardan olursun.",
168: "Dedi: Ben sizin işinize kızanlardanım.",
169: "Rabbim, beni ve ailemi bunların yaptıklarından kurtar.",
170: "Onu ve bütün ailesini kurtardık.",
}

O = {
161: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı لُوط *(Lût)* 5. sırada, rol FAİL** · "
 "edim soru, kip INTG 1 · NEG 1 · şahıs 3MS x1 · 3MP x2 · 2MP x2, iltifât 0 · n=7 mora=33 harf=24 "
 "(n z=-0,58), fâsıla تَتَّقُونَ *(sakınmıyor musunuz)* → ن, N sınıfı — **26:106, 124, 142'nin "
 "fâsılasıyla AYNI KELİME, dördüncü kez**; **i'râb NOM 2**; bab I x1 · VIII x1; zaman PERF 1 · "
 "IMPF 1; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · أخو *(kardeş)* · وقي *(sakınma, "
 "koruma)* · bağ: **ÖN-KAYIT ASIL SINAMASI — öğe (ii) LÛT KISSASINDA VAR. TAHMİN TUTMADI.** "
 "26:110'da yazdığım ön-kayıt '(ii) أَلَا تَتَّقُونَ Lût ve Şuayb'da BULUNMAYABİLİR' diyordu; "
 "**Lût'ta VAR** (elle, L1, aday 722)"),
162: ("eksen: **lafız YOK · Rab YOK** · esmâ yok — **أَمِين *(güvenilir)* esmâ SAYILMIYOR ve bu "
 "DOĞRU** · aktör yok · edim haber, kip işareti yok · **şahıs eki YOK, fiil YOK** · n=4 mora=21 "
 "harf=15 (n z=-0,89), fâsıla أَمِينٌ *(güvenilir)* → ن, N sınıfı; **i'râb ACC 1 · NOM 2**; "
 "**NAKARAT alanı = 5, temsil ayet 26:107**; **esit: 26:107, 125, 143, 178 ile TAM AYET ÖZDEŞ** · "
 "dış düğüm 0 · yıldız ★ yok · kökler رسل *(gönderme, elçi)* · أمن *(güven; iman)* · bağ: "
 "**ÖN-KAYIT ÖĞESİ (iii) VAR; üçüncü nakarat kümesinin DÖRDÜNCÜ geçişi** (elle, L1, aday 722)"),
163: ("eksen: **ALLAH LAFZI 2. sırada — sûrenin ONUNCU lafzı**, **allah z=6,14: yıldızın TEK "
 "kaynağı** · Rab yok · esmâ yok · aktör yok · edim emir, kip IMPV 2 · şahıs 2MP x4 · 1S x1, "
 "iltifât 0 · n=3 mora=23 harf=18 (n z=-1,00), fâsıla وَأَطِيعُونِ *(bana itaat edin)* → ن, N "
 "sınıfı; **i'râb ACC 1**; bab IV x1 · VIII x1; zaman IMPV x2; **NAKARAT alanı = 8, temsil ayet "
 "26:108**; **esit: yedi ayetle TAM ÖZDEŞ** · dış düğüm 0 · **yıldız ★★★** · kökler وقي *(sakınma, "
 "koruma)* · أله *(ilâh; lafza-i celâl)* · طوع *(güç yetirme, itaat)* · bağ: **ÖN-KAYIT ÖĞESİ (iv) "
 "VAR; dördüncü nakarat kümesinin ALTINCI geçişi ve altısında da ★★★** (elle, L1, aday 722)"),
164: ("eksen: **lafız YOK · رَبّ *(Rab)* 10. sırada — yirmi dokuzuncu Rab** (rab z=1,62: yıldızın "
 "TEK kaynağı) · esmâ yok · aktör yok · edim haber, kip NEG 2 · RES 1 · şahıs 1S x2 · 2MP x1 · "
 "3MS x1, iltifât 0 · n=11 mora=50 harf=40 — **blokta en uzun ayetlerden** (n z=-0,15), fâsıla "
 "ٱلْعَٰلَمِينَ *(âlemler)* → ن, N sınıfı; **i'râb GEN 3 · NOM 1**; bab I x1; zaman IMPF 1; "
 "**kök ikilemesi أجر *(ücret, karşılık)* x2**; **biçim HASR**; simetri [4,1,6,1]; **NAKARAT alanı "
 "= 5, temsil ayet 26:109**; **esit: 26:109, 127, 145, 180 ile TAM ÖZDEŞ** · dış düğüm 0 · "
 "**yıldız ★** · kökler سأل *(isteme, dileme)* · أجر *(ücret, karşılık)* · ربب *(rab, terbiye "
 "etme)* · علم *(bilme; âlem)* · bağ: **ÖN-KAYIT ÖĞESİ (v) VAR; beşinci nakarat kümesinin DÖRDÜNCÜ "
 "geçişi** (elle, L1, aday 722)"),
165: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · **şahıs "
 "2MP x2 — ayette başka şahıs yok**, iltifât 0 · n=4 mora=29 harf=22 (n z=-0,89), fâsıla "
 "ٱلْعَٰلَمِينَ *(âlemler)* → ن, N sınıfı — **26:164 ile bitişik ayette AYNI FÂSILA**; i'râb ACC 1 · "
 "GEN 1; bab I x1; zaman IMPF 1; dış düğüm 0 · yıldız ★ yok · kökler أتي *(gelme, getirme)* · ذكر "
 "*(anma, zikir)* · علم *(bilme)* · bağ: **ذكر *(anma, zikir)* — 529 KÜMESİNE YENİ VAKA**: kök "
 "korpusta 292 geçişli ve ezici çoğunlukla 'anma, zikir' anlamında; burada ٱلذُّكْرَان *(erkekler)* "
 "anlamında ve **dikey satırı ▸sonra أنث *(dişi)* x13,4 veriyor, yani BU AYETİN anlamı da "
 "komşulukta** (aday 711 sınıfı, ikinci vaka) (elle, L1, aday 723)"),
166: ("eksen: **lafız YOK · رَبّ *(Rab)* 5. sırada — otuzuncu Rab** (rab z=1,62: yıldızın TEK "
 "kaynağı) · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs 2MP x6 · 3MS x1**, "
 "iltifât 0 · n=11 mora=50 harf=41 — **blokta en uzun ayet** (n z=-0,15), fâsıla عَادُونَ *(haddi "
 "aşanlar)* → ن, N sınıfı; **i'râb NOM 3 · GEN 1**; bab I x2; zaman IMPF 1 · PERF 1; **açık sayı "
 "sözcüğü: زوج *(eş, çift)* → أَزْوَٰج**; **biçim IDRAB — SÛRENİN İKİ IDRAB'INDAN İKİNCİSİ ve "
 "SONUNCUSU** (26:74, 26:166; makro sayım 2 ve DOĞRU); simetri [3,2,6,1]; dış düğüm 0 · **yıldız "
 "★** · kökler وذر *(bırakma)* · خلق *(yaratma)* · ربب *(rab, terbiye etme)* · زوج *(eş, çift)* · "
 "قوم *(kalkma; kavim; kıyamet)* · عدو *(düşmanlık, düşman)* · bağ: **26:137 ile خلق *(yaratma)* "
 "ikinci geçişi VE TERS ANLAM** — orada خُلُق *(huy, âdet)*, burada خَلَقَ *(yarattı)*; **aynı "
 "sûrede iki anlam** (aday 705/714 sınıfı) (elle, L1, aday 724)"),
167: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı لُوط *(Lût)* 5. sırada, rol FAİL + "
 "MUHATAP — okumada ikinci kez bir aktör iki rol birden alıyor** (birincisi 26:116 Nûh) · edim "
 "nida + şart, kip EMPH 3 · COND 1 · NEG 1 · **VOC 1 — sûrenin ikinci nidası** · şahıs 3MP x2 · "
 "2MS x2, iltifât 0 · n=8 mora=43 harf=35 (n z=-0,47), fâsıla ٱلْمُخْرَجِينَ *(çıkarılanlar)* → ن, "
 "N sınıfı; i'râb NOM 1 · GEN 1; bab I x2 · VIII x1; zaman PERF 1 · IMPF x2; dış düğüm 0 · yıldız "
 "★ yok · kökler قول *(söz söyleme)* · نهي *(akıl; nehiy)* · كون *(olmak; mekân, yer)* · خرج "
 "*(çıkma, çıkarma)* · bağ: **26:29 ve 26:116 ile TEHDİT KALIBININ ÜÇÜNCÜ GEÇİŞİ** — Firavun "
 "ٱلْمَسْجُونِينَ *(zindana atılanlar)*, Nûh'un kavmi ٱلْمَرْجُومِينَ *(taşlananlar)*, burada "
 "ٱلْمُخْرَجِينَ *(çıkarılanlar)*; **üç kıssa, aynı kalıp, üç ceza** (elle, L1, aday 725)"),
168: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3MS x1 · 1S x1 · 2MP x1, iltifât 0 · n=5 mora=28 harf=21 (n z=-0,79), fâsıla ٱلْقَالِينَ "
 "*(kızanlar, hoşlanmayanlar)* → ن, N sınıfı; i'râb ACC 1 · GEN 2; bab I x1; zaman PERF 1; dış "
 "düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · عمل *(iş, amel)* · قلي *(öfkelenme, "
 "hoşlanmama (kâlî))* · bağ: **قلي *(öfkelenme, hoşlanmama (kâlî))* korpusta İKİ geçişli ve dikey "
 "ölçümü iki listede de BOŞ** — blokta 'boş komşuluk' vakası, okumadaki listeye ekleniyor (aday "
 "689); **26:112 ile عمل *(iş, amel)* ikinci geçişi** — orada Nûh 'onların yaptığına dair bilgim "
 "yok' diyordu, burada Lût 'sizin işinize kızanlardanım'; **aynı kök, bilgisizlikten öfkeye** "
 "(elle, L1, aday 726)"),
169: ("eksen: **lafız YOK · رَبّ *(Rab)* 1. sırada — otuz birinci Rab**, **rab z=3,94: yıldızın TEK "
 "kaynağı** (n=5, oran 0,20) · esmâ yok · aktör yok · edim emir, kip IMPV 1 · **şahıs 1S x3 · "
 "2MS x1 · 3MP x2**, iltifât 0 · n=5 mora=27 harf=20 (n z=-0,79), fâsıla يَعْمَلُونَ "
 "*(yapıyorlar)* → ن, N sınıfı — **26:112'nin fâsılasıyla AYNI KELİME**; **i'râb NOM 2**; bab I "
 "x1 · II x1; zaman IMPV 1 · IMPF 1; dış düğüm 0 · **yıldız ★★★** · kökler ربب *(rab, terbiye "
 "etme)* · نجو *(kurtulma, kurtarma)* · أهل *(halk, aile)* · عمل *(iş, amel)* · bağ: **26:118 ile "
 "dua karşılaştırması** — orada Nûh وَنَجِّنِى وَمَن مَّعِىَ مِنَ ٱلْمُؤْمِنِينَ *(beni ve benimle "
 "beraber olan müminleri kurtar)*, burada Lût نَجِّنِى وَأَهْلِى *(beni ve ailemi kurtar)*; **aynı "
 "fiil (نجو bab II), aynı emir, farklı kapsam: iman topluluğu / aile** (elle, L1, aday 727)"),
170: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "1P x2 · 3MS x2, iltifât 0 · n=3 mora=25 harf=18 (n z=-1,00), fâsıla أَجْمَعِينَ *(hepsi)* → ن, N "
 "sınıfı — **26:49, 26:65'in fâsılasıyla AYNI KELİME, üçüncü kez**; **i'râb ACC 2**; bab II x1; "
 "zaman PERF 1; **dış düğüm 1** · yıldız ★ yok · kökler نجو *(kurtulma, kurtarma)* · أهل *(halk, "
 "aile)* · جمع *(toplama)* · bağ: xref نجّى *(kurtardı)* + أهل *(aile)* + أجمع *(hepsi)* → "
 "**37:134**; **26:65 ve 26:119 ile نجو *(kurtulma, kurtarma)* ÜÇÜNCÜ geçişi** — Mûsâ وَمَن مَّعَهُۥٓ "
 "أَجْمَعِينَ, Nûh وَمَن مَّعَهُ فِى ٱلْفُلْكِ, burada وَأَهْلَهُۥٓ أَجْمَعِينَ; **üç kıssa, aynı "
 "fiil, üç kapsam** (elle, L1, aday 727)"),
}

M = {
161: ("**Ön-kaydın asıl sınaması ve TAHMİN TUTMADI.** 26:110'da, kıssalar okunmadan önce şöyle "
 "yazmıştım: *'(ii) أَلَا تَتَّقُونَ Lût ve Şuayb'da BULUNMAYABİLİR (esit listesinde 26:106 için "
 "eşleşme yok, yani kalıp tekil)'.* **Lût kıssasında VAR.** Gerekçem yanlıştı: `esit` alanının "
 "26:106'yı eşleştirmemesi kalıbın tekil olduğunu değil, alanın elçi adı değiştiği için tam ayet "
 "eşleşmesi bulamadığını gösteriyordu — yani **ölçüm aracının bilinen bir eksiğini (aday 621) "
 "kalıbın yokluğu sanmıştım.** Fâsıla تَتَّقُونَ dördüncü kez ve dört kıssada da aynı."),
162: ("**Ön-kayıt öğesi (iii) var.** Üçüncü nakarat kümesinin dördüncü geçişi. Ve `أَمِين` esmâ "
 "sayılmıyor — doğru; sûrenin on bir مُؤْمِن artefaktı aynı kökten (aday 709)."),
163: ("**Ön-kayıt öğesi (iv) var.** Dördüncü nakarat kümesinin altıncı geçişi ve **altısında da "
 "★★★**, altısında da allah z=6,14. Küme sekiz üyeli; iki geçiş kaldı (26:179 ve blok dışı)."),
164: ("**Ön-kayıt öğesi (v) var.** Beşinci nakarat kümesinin dördüncü geçişi. Kök ikilemesi أجر "
 "*(ücret, karşılık)* x2 ve HASR; simetri [4,1,6,1]. Ve **aday 602'nin karşı yönlü kanıtı dördüncü "
 "kez**: aynı bölütte üç kelimelik 26:163 ★★★, on bir kelimelik bu ayet ★."),
165: ("Lût'un ilk suçlaması bir soru. Ölçülebilir bir kök tuzağı: ذكر *(anma, zikir)* korpusta 292 "
 "geçişli ve ezici çoğunlukla 'anma, zikir' anlamında; burada ٱلذُّكْرَان *(erkekler)*. **Ama dikey "
 "satırı ▸sonra أنث *(dişi)* x13,4 veriyor — yani BU AYETİN anlamı da komşulukta görünüyor**; "
 "aday 711'in (طلع, iki anlam da dikey satırında) ikinci vakası. Ve fâsıla ٱلْعَٰلَمِينَ bitişik "
 "ayetle aynı — 26:164'te 'âlemlerin Rabbi' tamlamasının ikinci terimiydi, burada tek başına bir "
 "kapsam."),
166: ("Suçlama IDRAB ile ikiye bölünüyor: bir bırakma (وَتَذَرُونَ *(bırakıyorsunuz)*) ve bir "
 "niteleme (بَلْ أَنتُمْ قَوْمٌ عَادُونَ *(hayır, siz haddi aşan bir topluluksunuz)*). **Bu, "
 "sûrenin iki IDRAB'ından ikincisi ve sonuncusu** (26:74 ve burada) — ve makro sayım 2 veriyor, "
 "**DOĞRU**. Ölçülebilir bir kök karşılaşması: خلق *(yaratma)* 26:137'de خُلُق *(huy, âdet)* "
 "anlamındaydı, burada خَلَقَ *(yarattı)* — **aynı sûrede iki anlam**, 26:142↔26:152'nin صلح "
 "vakasıyla aynı sınıf. On bir kelimede 2MP altı kez."),
167: ("Tehdit bir nida ile ve **sûrenin ikinci VOC işareti** burada. Ölçülebilir bir kalıp üçlüsü: "
 "26:29'da Firavun لَأَجْعَلَنَّكَ مِنَ ٱلْمَسْجُونِينَ *(zindana atılanlardan yaparım)*, 26:116'da "
 "Nûh'un kavmi لَتَكُونَنَّ مِنَ ٱلْمَرْجُومِينَ *(taşlananlardan olursun)*, burada لَتَكُونَنَّ "
 "مِنَ ٱلْمُخْرَجِينَ *(çıkarılanlardan olursun)*. **Üç kıssa, aynı 'لَئِن + şart + لَ + EMPH + مِنَ "
 "+ ism-i mef'ûl çoğulu' kalıbı, üç ceza: hapis, taşlanma, sürgün.** Ve Lût hem FAİL hem MUHATAP "
 "rolü alıyor — 26:116'daki Nûh'tan sonra ikinci vaka. نهي *(akıl; nehiy)* dikey ölçümü ▸sonra رجم "
 "*(taşlama, kovma)* x28,5 veriyor — **26:116'nın cezası**, yani çift korpusta bağlı ve kalıp "
 "ayete özgü değil."),
168: ("Cevap bir duygu bildirimi: إِنِّى لِعَمَلِكُم مِّنَ ٱلْقَالِينَ *(ben sizin işinize "
 "kızanlardanım)*. قلي *(öfkelenme, hoşlanmama (kâlî))* korpusta **iki** geçişli ve dikey ölçümü "
 "**iki listede de boş** — okumadaki 'boş komşuluk' listesine ekleniyor (aday 689; hepsi n≤6). Ve "
 "عمل *(iş, amel)* 26:112'den geri geliyor: orada Nûh مَا عِلْمِى بِمَا كَانُوا۟ يَعْمَلُونَ "
 "*(onların ne yaptığına dair bilgim yok)* diyordu — **bilgisizlik**; burada Lût kızgınlık "
 "bildiriyor. **Aynı kök, iki elçi, bilgisizlikten öfkeye.**"),
169: ("Dua tek emirle ve rab z=3,94 — n=5, tek Rab, oran 0,20. Ölçülebilir bir kapsam farkı: "
 "26:118'de Nûh وَنَجِّنِى وَمَن مَّعِىَ مِنَ ٱلْمُؤْمِنِينَ *(beni ve benimle beraber olan "
 "müminleri kurtar)* demişti — kapsam **iman topluluğu**; burada نَجِّنِى وَأَهْلِى *(beni ve "
 "ailemi kurtar)* — kapsam **aile**. Aynı fiil (نجو bab II), aynı emir, farklı kapsam. Ve fâsıla "
 "يَعْمَلُونَ 26:112'den geri geliyor: orada Nûh'un bilgisizliğinin nesnesi, burada Lût'un "
 "kurtulmak istediği şey."),
170: ("Üç kelime ve kurtarma gerçekleşiyor. Ölçülebilir bir üçlü: نجو *(kurtulma, kurtarma)* sûrede "
 "üçüncü kez ve üç ayrı kapsamla — 26:65 Mûsâ وَمَن مَّعَهُۥٓ أَجْمَعِينَ *(beraberindekilerin "
 "hepsi)*, 26:119 Nûh وَمَن مَّعَهُ فِى ٱلْفُلْكِ *(gemide beraberindekiler)*, burada وَأَهْلَهُۥٓ "
 "أَجْمَعِينَ *(bütün ailesi)*. **Üç kıssa, aynı fiil, üç kapsam: topluluk / gemidekiler / aile.** "
 "Ve أَجْمَعِينَ fâsıla olarak üçüncü kez (26:49 tehdit, 26:65 kurtuluş, burada kurtuluş). Tek "
 "xref 37:134'e düşüyor."),
}

ATLAMA = {
 "_mercek_26_163_169": ("26:163 ve 26:169 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. 26:163 NAKARAT "
  "(dördüncü kümenin altıncı geçişi, allah z=6,14); 26:169 bir dua (rab z=3,94, n=5). İkisinde de "
  "ne canlı, ne gök cismi, ne ölçü, ne süreç."),
 "_blok_notu_26_161_170": ("BLOK BİLANÇOSU: ★★★ 2 (26:163, 169) · ★★ 0 · ★ 3 (26:164, 166) — "
  "düzeltme: ★ 2 (26:164, 166) · 6 ayet yıldızsız. Kaynaklar: allah x1 · rab x3 — hiçbiri "
  "içerikten, hiçbirinde çıpa yok. **ÖN-KAYIT ASIL SINAMASI (aday 685/696/708/722): TAHMİN "
  "TUTMADI.** 26:110'da '(ii) أَلَا تَتَّقُونَ Lût ve Şuayb'da bulunmayabilir' yazmıştım; "
  "**Lût kıssasında VAR** (26:161). Gerekçem de yanlıştı: `esit` alanının 26:106'yı eşleştirmemesi "
  "kalıbın tekil olduğunu değil, ALANIN BİLİNEN EKSİĞİNİ (aday 621) gösteriyordu — ölçüm aracının "
  "kusurunu metnin özelliği sanmışım. **ŞUAYB (26:176) HÂLÂ SINANACAK ama tahmin zaten yarı "
  "düştü.** SÛRE 26'NIN OKUNAN 170 AYETİNDE ★★★ 36."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(161, 171):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 170/227.** Devam: 26:171'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-170 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1892
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(161, 171):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
