# -*- coding: utf-8 -*-
"""blok_26_141_150.py — sûre 26 on ikinci blok (26:141-150). Sâlih kıssası, ön-kaydın ikinci sınaması."""
import json
DIK = json.load(open('blok_dikey_26_141_150.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
141: "Semûd da elçileri yalanladı.",
142: "Kardeşleri Sâlih onlara demişti: Sakınmıyor musunuz?",
143: "Ben size güvenilir bir elçiyim.",
144: "Allah'tan sakının ve bana itaat edin.",
145: "Buna karşılık sizden bir ücret istemiyorum; benim ücretim ancak âlemlerin Rabbine aittir.",
146: "Siz burada güven içinde bırakılacak mısınız?",
147: "Bahçelerde ve pınarlarda.",
148: "Ekinlerde ve tomurcukları olgun hurmalıklarda.",
149: "Dağlardan ustalıkla evler yontuyorsunuz.",
150: "Allah'tan sakının ve bana itaat edin.",
}

O = {
141: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı ثَمُود *(Semûd)* 2. sırada, rol "
 "FAİL — SÛRENİN BEŞİNCİ KISSASI AÇILIYOR** · edim haber, kip işareti yok · **şahıs 3FS x1 — ayette "
 "başka şahıs yok**, iltifât 0 · n=3 mora=21 harf=16 (n z=-1,00), fâsıla ٱلْمُرْسَلِينَ "
 "*(gönderilenler)* → ن, N sınıfı — **26:105 ve 26:123'ün fâsılasıyla AYNI KELİME, üçüncü kez**; "
 "i'râb NOM 1 · ACC 1; bab II x1; zaman PERF 1; dış düğüm 0 · yıldız ★ yok · kökler كذب *(yalan; "
 "yalanlama)* · رسل *(gönderme, elçi)* · bağ: **ÖN-KAYIT ÖĞESİ (i) VAR — ikinci sınama** (aday "
 "685/696); **26:123 ile BİREBİR AYNI YAPI ve AYNI UZUNLUK (n=3)**: كَذَّبَتْ + kavim adı + "
 "ٱلْمُرْسَلِينَ; **tek fark kavim adı ve esit YAKALAMIYOR** (elle, L1, aday 708)"),
142: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı صالِح *(Sâlih)* 5. sırada, rol "
 "FAİL** · edim soru, kip INTG 1 · NEG 1 · şahıs 3MS x1 · 3MP x2 · 2MP x2, iltifât 0 · n=7 mora=33 "
 "harf=24 (n z=-0,58), fâsıla تَتَّقُونَ *(sakınmıyor musunuz)* → ن, N sınıfı — **26:106 ve "
 "26:124'ün fâsılasıyla AYNI KELİME, üçüncü kez**; **i'râb NOM 2**; bab I x1 · VIII x1; zaman "
 "PERF 1 · IMPF 1; dış düğüm 0 · yıldız ★ yok · kökler قول *(söz söyleme)* · أخو *(kardeş)* · صلح "
 "*(iyi, elverişli olma; ıslah)* · وقي *(sakınma, koruma)* · bağ: **ÖN-KAYIT ÖĞESİ (ii) VAR — "
 "tahminde 'Lût ve Şuayb'da bulunmayabilir' denmişti; Sâlih'te VAR**; **صلح kökü burada ÖZEL AD "
 "ama dikey ölçümü ▸önce عمل *(iş, amel)* x10,9 · توب *(tevbe, dönüş)* x5,8 veriyor — korpusta "
 "'sâlih amel' bağlamında; özel ad hiç ayrılmıyor** (aday 529 sınıfı) (elle, L1, aday 708)"),
143: ("eksen: **lafız YOK · Rab YOK** · esmâ yok — **أَمِين *(güvenilir)* esmâ SAYILMIYOR ve bu "
 "DOĞRU** (aday 682/690) · aktör yok · edim haber, kip işareti yok · **şahıs eki YOK, fiil YOK** · "
 "n=4 mora=21 harf=15 (n z=-0,89), fâsıla أَمِينٌ *(güvenilir)* → ن, N sınıfı; **i'râb ACC 1 · "
 "NOM 2**; **NAKARAT alanı = 5, temsil ayet 26:107**; **esit: 26:107, 125, 162, 178 ile TAM AYET "
 "ÖZDEŞ** · dış düğüm 0 · yıldız ★ yok · kökler رسل *(gönderme, elçi)* · أمن *(güven; iman)* · "
 "bağ: **ÖN-KAYIT ÖĞESİ (iii) VAR; üçüncü nakarat kümesinin ÜÇÜNCÜ geçişi** (elle, L1, aday 708)"),
144: ("eksen: **ALLAH LAFZI 2. sırada — sûrenin SEKİZİNCİ lafzı**, **allah z=6,14: yıldızın TEK "
 "kaynağı** · Rab yok · esmâ yok · aktör yok · edim emir, kip IMPV 2 · şahıs 2MP x4 · 1S x1, "
 "iltifât 0 · n=3 mora=23 harf=18 (n z=-1,00), fâsıla وَأَطِيعُونِ *(bana itaat edin)* → ن, N "
 "sınıfı; **i'râb ACC 1**; bab IV x1 · VIII x1; zaman IMPV x2; **NAKARAT alanı = 8, temsil ayet "
 "26:108**; **esit: yedi ayetle TAM ÖZDEŞ** · dış düğüm 0 · **yıldız ★★★** · kökler وقي *(sakınma, "
 "koruma)* · أله *(ilâh; lafza-i celâl)* · طوع *(güç yetirme, itaat)* · bağ: **ÖN-KAYIT ÖĞESİ (iv) "
 "VAR; dördüncü nakarat kümesinin BEŞİNCİ geçişi ve beşinde de ★★★** (elle, L1, aday 708)"),
145: ("eksen: **lafız YOK · رَبّ *(Rab)* 10. sırada — yirmi yedinci Rab** (rab z=1,62: yıldızın TEK "
 "kaynağı) · esmâ yok · aktör yok · edim haber, kip NEG 2 · RES 1 · şahıs 1S x2 · 2MP x1 · 3MS x1, "
 "iltifât 0 · n=11 mora=50 harf=40 — **blokta en uzun ayet** (n z=-0,15), fâsıla ٱلْعَٰلَمِينَ "
 "*(âlemler)* → ن, N sınıfı; **i'râb GEN 3 · NOM 1**; bab I x1; zaman IMPF 1; **kök ikilemesi أجر "
 "*(ücret, karşılık)* x2**; **biçim HASR**; simetri [4,1,6,1]; **NAKARAT alanı = 5, temsil ayet "
 "26:109**; **esit: 26:109, 127, 164, 180 ile TAM ÖZDEŞ** · dış düğüm 0 · **yıldız ★** · kökler "
 "سأل *(isteme, dileme)* · أجر *(ücret, karşılık)* · ربب *(rab, terbiye etme)* · علم *(bilme; "
 "âlem)* · bağ: **ÖN-KAYIT ÖĞESİ (v) VAR; beşinci nakarat kümesinin ÜÇÜNCÜ geçişi** (elle, L1, "
 "aday 708)"),
146: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · **şahıs "
 "2MP x2 — ayette başka şahıs yok**, iltifât 0 · n=5 mora=31 harf=21 (n z=-0,79), fâsıla "
 "ءَامِنِينَ *(güven içinde olanlar)* → ن, N sınıfı; **i'râb ACC 1**; bab I x1; zaman IMPF 1; "
 "**edilgen 1 — تُتْرَكُونَ *(bırakılacak mısınız)*; ayetin TEK fiili ve o da edilgen, oran 1,00**, "
 "pas z=5,38: **yıldızın TEK kaynağı**; **biçim DIKKAT**; dış düğüm 0 · **yıldız ★★★** · kökler "
 "ترك *(bırakma, terk)* · أمن *(güven; iman)* · bağ: **أمن *(güven; iman)* — sûrede on beşinci "
 "kez ve İLK KEZ 'güven' anlamında ve esmâ SAYILMADAN**; on beş مُؤْمِن artefaktı, beş أَمِين "
 "nakaratı, burada ءَامِنِين — **üç lemma, üç hüküm** (aday 682/690) (elle, L1, aday 709)"),
147: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "eki YOK, fiil YOK** · n=3 mora=16 harf=12 (n z=-1,00), fâsıla وَعُيُونٍ *(pınarlar)* → ن, N "
 "sınıfı — **26:57 ve 26:134'ün fâsılasıyla AYNI KELİME, üçüncü kez**; **i'râb GEN 2**; **dış "
 "düğüm 1** · yıldız ★ yok · **esit: 44:52 ile TAM AYET ÖZDEŞ** · kökler جنن *(örtme, gizleme; "
 "cennet; cin)* · عين *(göz; pınar)* · bağ: **26:57 ve 26:134 ile ÜÇÜNCÜ kez aynı ikili** — 26:57 "
 "KAYIP, 26:134 NİMET, burada yine NİMET; **üç geçişin ikisi nimet biri kayıp** (elle, L1, aday 710)"),
148: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · şahıs "
 "3FS x1, **iltifât 1 — yön 2>3; sûrenin sekizinci iltifâtı** · n=4 mora=26 harf=21 (n z=-0,89), "
 "fâsıla هَضِيمٌ *(olgun, yumuşak)* → م, N sınıfı; **i'râb GEN 2 · NOM 2; fiil YOK**; dış düğüm 0 · "
 "yıldız ★ yok · kökler زرع *(ekin, ekip bitirme)* · نخل *(hurma)* · طلع *(doğma (güneş))* · هضم "
 "*(hak yeme, eksiltme)* · bağ: **طلع *(doğma (güneş))* — 529 KÜMESİNE YENİ VAKA**: kök korpusta 19 "
 "geçişli ve dikey ölçümü ▸sonra شمس *(güneş)* x32,9 veriyor, yani korpusta ağırlıkla 'güneşin "
 "doğuşu'; burada طَلْع *(hurma tomurcuğu)*; **ve dikey satırı ▸önce نخل *(hurma)* x54,2 de veriyor, "
 "yani İKİ ANLAM DA komşulukta görünüyor** (elle, L1, aday 711)"),
149: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "2MP x2 — ayette başka şahıs yok**, **iltifât 1 — yön 3>2; sûrenin dokuzuncu iltifâtı** · n=5 "
 "mora=34 harf=26 (n z=-0,79), fâsıla فَٰرِهِينَ *(ustalıkla)* → ن, N sınıfı; **i'râb GEN 1 · "
 "ACC 2**; bab I x1; zaman IMPF 1; **HAPAKS: فره *(ustalık, mahirlik; şımarıklık)* — korpusta TEK "
 "geçiş** (hapaks z=3,38: **yıldızın TEK kaynağı**); **dış düğüm 2** · **yıldız ★★★** · kökler نحت "
 "*(yontma)* · جبل *(dağ)* · بيت *(ev, mesken)* · فره *(ustalık, mahirlik; şımarıklık)* · bağ: xref "
 "ينحت *(yontuyor)* + جبل *(dağ)* + بيت *(ev)* → **7:74 · 15:82**; **26:128-129 ile yapı üçlüsü** — "
 "orada Âd tepelere işaret dikiyor ve yapılar ediniyordu, burada Semûd dağlardan ev yontuyor; **iki "
 "kavim, iki yapı türü, aynı suçlama biçimi** (elle, L1, aday 712)"),
150: ("eksen: **ALLAH LAFZI 2. sırada — sûrenin DOKUZUNCU lafzı**, **allah z=6,14: yıldızın TEK "
 "kaynağı** · Rab yok · esmâ yok · aktör yok · edim emir, kip IMPV 2 · şahıs 2MP x4 · 1S x1, "
 "iltifât 0 · n=3 mora=23 harf=18 (n z=-1,00), fâsıla وَأَطِيعُونِ → ن, N sınıfı; **i'râb ACC 1**; "
 "bab IV x1 · VIII x1; zaman IMPV x2; **NAKARAT alanı = 8, temsil ayet 26:108**; **esit: yedi "
 "ayetle TAM ÖZDEŞ** · dış düğüm 0 · **yıldız ★★★** · kökler وقي *(sakınma, koruma)* · أله *(ilâh; "
 "lafza-i celâl)* · طوع *(güç yetirme, itaat)* · bağ: **ÖN-KAYIT ÖĞESİ (vi) VAR — SÂLİH KISSASINDA "
 "DA ALTI ÖĞENİN ALTISI TAMAM**; ve örgü Hûd'unkiyle AYNI: (iv) 26:144, üç suçlama (26:146-149), "
 "(vi) 26:150 (elle, L1, aday 708)"),
}

M = {
141: ("**Ön-kaydın ikinci sınaması başlıyor** (aday 685/696). Öğe (i) tekzip cümlesi — **var**. Ve "
 "26:123 ile **birebir aynı yapı ve aynı uzunluk** (n=3): كَذَّبَتْ + kavim adı + ٱلْمُرْسَلِينَ; "
 "tek fark kavim adı (عَادٌ / ثَمُودُ) ve **esit yakalamıyor**. Ölçülebilir bir fâsıla tekrarı: "
 "ٱلْمُرْسَلِينَ *(gönderilenler)* sûrede üçüncü kez (26:105, 123, 141) ve üçü de kıssa açılışı. "
 "كذب *(yalan; yalanlama)* dikey ölçümü ▸sonra أشر *(şımarma, azgınlık)* x37,2 veriyor — bu bölütün "
 "sonundaki فره *(ustalık, mahirlik; şımarıklık)* ile aynı anlam alanında ama farklı kök."),
142: ("**Ön-kayıt öğesi (ii) var.** Tahminde 'Lût ve Şuayb'da bulunmayabilir' demiştim; Sâlih'te "
 "**var**. 26:106 ve 26:124 ile birebir aynı yapı; tek fark elçi adı. Ölçülebilir bir kök tuzağı: "
 "صلح *(iyi, elverişli olma; ıslah)* burada ÖZEL AD ama dikey ölçümü ▸önce عمل *(iş, amel)* x10,9 · "
 "توب *(tevbe, dönüş)* x5,8 · ▸sonra kesintisiz x29,2 veriyor — **korpusta 'sâlih amel' bağlamında** "
 "ve özel ad hiç ayrılmıyor. 26:124'ün هود *(Yahudi olma; Hûd)* vakasıyla aynı: **kıssa elçilerinin "
 "adları kök düzeyinde cins ada karışıyor** (aday 529 sınıfı, sûre 26'nın on üçüncü vakası)."),
143: ("**Ön-kayıt öğesi (iii) var.** Üçüncü nakarat kümesinin üçüncü geçişi; dört kelime, fiil yok. "
 "Ve 682/690'ın tanısı üçüncü kez: أَمِين *(güvenilir)* esmâ **sayılmıyor** — doğru; ama sûrenin on "
 "أمن artefaktı aynı kökten. **Tablo aynı kökün lemmalarını liste üzerinden ayırıyor, göndergeye "
 "hiç bakmıyor.**"),
144: ("**Ön-kayıt öğesi (iv) var.** Dördüncü nakarat kümesinin beşinci geçişi ve **beşinde de ★★★**, "
 "beşinde de allah z=6,14. Üç kelime, iki emir, tek lafız. Aday 683'ün sekiz ayetlik kümesi "
 "tamamlanınca sûrenin 41 ★★★ ayetinin sekizi buradan gelecek."),
145: ("**Ön-kayıt öğesi (v) var.** Beşinci nakarat kümesinin üçüncü geçişi. Kök ikilemesi أجر "
 "*(ücret, karşılık)* x2 ve HASR; simetri [4,1,6,1]. Ve **aday 602'nin karşı yönlü kanıtı üçüncü "
 "kez**: aynı bölütte üç kelimelik 26:144 ★★★, on bir kelimelik bu ayet ★ — ikisinin de kaynağı "
 "eksen oranı."),
146: ("Sâlih'in ilk suçlaması bir soru ve ayetin tek fiili edilgen: أَتُتْرَكُونَ *(bırakılacak "
 "mısınız)*, oran 1,00 → pas z=5,38, yıldızın tek kaynağı. Ölçülebilir bir lemma üçlüsü: أمن "
 "*(güven; iman)* kökü sûrede burada ءَامِنِين *(güven içinde olanlar)* biçiminde ve **esmâ "
 "sayılmıyor**; aynı kökten مُؤْمِن on kez **sayılıyor** (artefakt), أَمِين üç kez **sayılmıyor** "
 "(doğru). **Üç lemma, üç hüküm — ve hiçbirinin göndergesi ilâhî değil.** ترك *(bırakma, terk)* "
 "korpusta 43 geçişli ve dikey ölçümü ▸sonra وصي *(vasiyet)* x25,7 veriyor — kök korpusta ağırlıkla "
 "'geride bırakma' bağlamında."),
147: ("Üç kelime, fiil yok, ve ayet 44:52 ile **tam özdeş**; esit yakalıyor. Ölçülebilir bir üçlü: "
 "جَنَّٰتٍ وَعُيُونٍ *(bahçeler ve pınarlar)* sûrede üçüncü kez — 26:57'de Firavun kavminin KAYBI, "
 "26:134'te Âd'ın NİMETİ, burada Semûd'un NİMETİ. **Üç geçişin ikisi nimet biri kayıp**; ve "
 "26:134 ile bu ayet **fâsılası aynı, i'râbı aynı, uzunluğu bir kelime farklı** (n=2 / n=3). "
 "esit 26:134 ile eşleşmeyi YAKALAMIYOR ama 44:52 ile YAKALIYOR — çünkü ikincisi tam ayet."),
148: ("Nimet listesi bir bitki betimlemesiyle sürüyor: طَلْعُهَا هَضِيمٌ *(tomurcuğu olgun)*. "
 "Ölçülebilir bir kök tuzağı: طلع *(doğma (güneş))* korpusta 19 geçişli ve dikey ölçümü ▸sonra "
 "شمس *(güneş)* x32,9 veriyor — korpusta ağırlıkla 'güneşin doğuşu'; burada طَلْع *(hurma "
 "tomurcuğu)*. **Ama dikey satırı ▸önce نخل *(hurma)* x54,2 de veriyor, yani bu ayetin anlamı da "
 "komşulukta görünüyor** — 529 kümesinde ilk kez **iki anlam da dikey satırında var**. هضم *(hak "
 "yeme, eksiltme)* korpusta İKİ geçişli ve dikey ölçümü iki listede de boş. **SINIR: ayet bir bitki "
 "organını ADLANDIRIYOR ve bir nitelik veriyor (olgun); ne süreç, ne ölçü, ne sınıflandırma.** "
 "Sûrenin ilk bitki betimlemesi ve YILDIZSIZ."),
149: ("Üçüncü suçlama bir yapı tekniğine: تَنْحِتُونَ مِنَ ٱلْجِبَالِ بُيُوتا فَٰرِهِينَ *(dağlardan "
 "ustalıkla evler yontuyorsunuz)*. نحت *(yontma)* korpusta DÖRT geçişli ve dikey ölçümü ▸sonra dağ "
 "x107,4 · ev x64,4 veriyor — **üçlü korpusta neredeyse ayrılmaz**; iki xref de aynı terkibe düşüyor "
 "(7:74, 15:82). Ve فره *(ustalık, mahirlik; şımarıklık)* korpusta TEK geçiş, yıldızın tek kaynağı. "
 "Ölçülebilir bir yapı suçlaması ikilisi: 26:128-129'da Âd tepelere işaret dikiyor ve yapılar "
 "ediniyordu, burada Semûd dağlardan ev yontuyor — **iki kavim, iki yapı türü, aynı suçlama biçimi**. "
 "SINIR: ayet bir tekniği ADLANDIRIYOR (yontma) ve bir tarz niteliği veriyor; ne alet, ne ölçü, ne "
 "süreç."),
150: ("**Ön-kayıt öğesi (vi) var — Sâlih kıssasında da altı öğenin altısı tamam.** Ve örgü "
 "Hûd'unkiyle **aynı**: (iv) nakarat 26:144, sonra üç suçlama (26:146, 148, 149), sonra (vi) "
 "nakarat 26:150. Hûd'da da (iv) 26:126, üç suçlama (26:128-130), (vi) 26:131 idi. **Yani örgü "
 "Nûh'unkinden (A-B-A, üç ardışık nakarat) farklı ama Hûd ve Sâlih arasında AYNI** — ön-kaydın "
 "öngörmediği aralık yapısı iki kıssada tekrarlanıyor."),
}

ATLAMA = {
 "_mercek_26_144_150": ("26:144 ve 26:150 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. İkisi de NAKARAT "
  "(dördüncü kümenin beşinci ve altıncı geçişi), ikisinde de allah z=6,14. Bağımsız gözlem değil "
  "(adaylar 606, 683, 700, 707)."),
 "_mercek_26_146": ("26:146 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. أَتُتْرَكُونَ فِى مَا هَٰهُنَآ "
  "ءَامِنِينَ. Tek kaynak pas z=5,38 (n=5, ayetin tek fiili edilgen, oran 1,00). İçerik bir soru; "
  "ne canlı, ne gök cismi, ne ölçü, ne süreç."),
 "_mercek_26_149": ("26:149 ★★★ — 🜁 ve 🜂 YAZILMADI, ÇIPA YOK. تَنْحِتُونَ مِنَ ٱلْجِبَالِ بُيُوتا "
  "فَٰرِهِينَ. Tek kaynak hapaks z=3,38 (فره, korpusta tek geçiş). ÇIPA DEĞERLENDİRMESİ: ayet bir "
  "yapı tekniğini ADLANDIRIYOR (dağdan ev yontma) ve bir tarz niteliği veriyor (ustalıkla), ama ne "
  "alet, ne ölçü, ne süreç veriyor — 26:128-129 (Âd'ın yapıları) ile aynı sınıf ve orada da çıpa "
  "sayılmamıştı. Ayrıca mimari/taş işçiliği ne biyoloji ne astronomi; aday 646'nın 'sınıf yok' "
  "gerekçesi de geçerli olurdu. **Çıpa sayılmadı.**"),
 "_blok_notu_26_141_150": ("BLOK BİLANÇOSU: ★★★ 4 (26:144, 146, 149, 150) · ★★ 0 · ★ 1 (26:145) · "
  "5 ayet yıldızsız. **DÖRT ★★★ AYETİN İKİSİ NAKARAT**, biri edilgenlik, biri hapaks kaynaklı; "
  "hiçbirinde çıpa yok. **ÖN-KAYIT SINAMASI (aday 685/696/708): SÂLİH KISSASINDA DA ALTI ÖĞENİN "
  "ALTISI VAR** — (i) 26:141, (ii) 26:142, (iii) 26:143, (iv) 26:144, (v) 26:145, (vi) 26:150. "
  "Tahminde (ii) için 'Lût ve Şuayb'da bulunmayabilir' denmişti; Sâlih'te VAR. **ASIL SINAMA HÂLÂ "
  "LÛT (26:160-) VE ŞUAYB (26:176-)'DA.** ÇIPA NOTU: 26:148 sûrenin ilk bitki betimlemesi "
  "(طَلْعُهَا هَضِيمٌ *(tomurcuğu olgun)*) ve YILDIZSIZ — 'adlandırma + nitelik' düzeyinde, "
  "25:61 ve 26:63 ile aynı sınıf; biyolog merceğinin alanına düşüyor ama ★★★ eşiği aşılmadığı için "
  "mercek zaten yazılamazdı. SÛRE 26'NIN OKUNAN 150 AYETİNDE ★★★ 33."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(141, 151):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-25 TAM. **Sûre 26 (Şuarâ) 150/227.** Devam: 26:151'den.")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde", "26": "1-150 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1872
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(141, 151):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
