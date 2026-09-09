# -*- coding: utf-8 -*-
"""blok_26_221_227.py — sûre 26 SON BLOK (26:221-227). Ön-kayıt sınaması ve sûre kapanışı."""
import json
DIK = json.load(open('blok_dikey_26_221_227.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {}
for s in veri['sureler']:
    for a in s['ayetler']:
        AR[(s['no'], a['no'])] = a['ar']

MEAL = {
221: "Şeytanların kime indiğini size haber vereyim mi?",
222: "Her günahkâr yalancıya inerler.",
223: "Kulak verirler; çoğu yalancıdır.",
224: "Şairlere azgınlar uyar.",
225: "Görmez misin: onlar her vadide başıboş dolaşırlar,",
226: "ve yapmadıklarını söylerler.",
227: "Ancak iman edip sâlih amel işleyenler, Allah'ı çokça ananlar ve zulme uğradıktan sonra kendilerini savunanlar başka. Zulmedenler yakında nasıl bir devrilişle devrileceklerini bilecekler.",
}

O = {
221: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · **aktör: adlı شَيْطان *(şeytan)* 6. sırada, rol "
 "FAİL, sınıf GAYB — sûrede üçüncü gayb aktörü geçişi** · edim soru, kip INTG 1 · şahıs 1S x1 · "
 "2MP x1 · 3FS x1, iltifât 0 · n=6 mora=32 harf=24 (n z=-0,68), fâsıla ٱلشَّيَٰطِينُ *(şeytanlar)* → "
 "ن, N sınıfı — **26:210'un fâsılasıyla AYNI KELİME**; **i'râb NOM 1**; bab II x1 · **bab V x1**; "
 "zaman IMPF x2; dış düğüm 0 · yıldız ★ yok · kökler نبأ *(haber)* · نزل *(inme, indirme)* · شطن "
 "*(şeytan)* · bağ: **26:210 ile نزل *(inme, indirme)* AYNI BAB (V) ve AYNI ÖZNE** — orada وَمَا "
 "تَنَزَّلَتْ بِهِ ٱلشَّيَٰطِينُ *(onu şeytanlar indirmedi)* OLUMSUZ, burada عَلَىٰ مَن تَنَزَّلُ "
 "ٱلشَّيَٰطِينُ *(şeytanlar kime iner)* SORU; **aynı kök, aynı bab, aynı özne, olumsuzdan soruya**; "
 "**نبأ *(haber)* sûrede ÜÇÜNCÜ geçiş** (26:6 tehdit, 26:69 anlatı, burada soru) (elle, L1, "
 "aday 772)"),
222: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "3FS x1 — ayette başka şahıs yok**, iltifât 0 · n=5 mora=27 harf=18 (n z=-0,79), fâsıla أَثِيمٍ "
 "*(günahkâr)* → م, N sınıfı; **i'râb GEN 3 — beş kelimenin üçü mecrur**; **bab V x1**; zaman "
 "IMPF 1; **dış düğüm 1** · yıldız ★ yok · kökler نزل *(inme, indirme)* · كلل *(hep, bütün)* · أفك "
 "*(iftira, uydurma (ifk); döndürülme)* · أثم *(günah, ism)* · bağ: xref كلّ *(her)* + أفّاك *(çok "
 "yalancı)* + أثيم *(günahkâr)* → **45:7**; **25:4 ve 26:45 ile أفك *(uydurma)* ÜÇÜNCÜ geçişi** — "
 "25:4'te Kur'ân'a atılan iftira, 26:45'te büyücülerin uydurması, burada şeytanların indiği "
 "kişinin niteliği; **aynı kök, üç gönderge** (elle, L1, aday 773)"),
223: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip işareti yok · **şahıs "
 "3MP x3 — ayette başka şahıs yok**, iltifât 0 · n=4 mora=28 harf=22 (n z=-0,89), fâsıla "
 "كَٰذِبُونَ *(yalancılar)* → ن, N sınıfı; **i'râb ACC 1 · NOM 2**; bab IV x1; zaman IMPF 1; **açık "
 "sayı sözcüğü: كثر *(çokluk)* → أَكْثَر *(çoğu)*** — **ve bu, nakarat dışı İLK أَكْثَرُهُم "
 "geçişi** (aday 707'nin envanterinde 'farklı yapı' diye ayrılmıştı); dış düğüm 0 · yıldız ★ yok · "
 "kökler لقي *(karşılaşma, kavuşma; atma)* · سمع *(işitme)* · كثر *(çokluk)* · كذب *(yalan; "
 "yalanlama)* · bağ: **26:15, 25, 72, 212, 220 ile سمع *(işitme)* ALTINCI geçişi** — dizi kapanmış "
 "görünüyordu (aday 763) ama bir geçiş daha var: burada ŞEYTANLARIN kulak vermesi; **altı ayet, "
 "altı konum** (elle, L1, aday 774)"),
224: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok — ٱلشُّعَرَآء *(şairler)* aktör "
 "tablosuna GİRMİYOR · edim haber, kip işareti yok · şahıs 3MS x1 · 3MP x1, iltifât 0 · n=3 "
 "mora=28 harf=21 (n z=-1,00), fâsıla ٱلْغَاوُۥنَ *(azgınlar)* → ن, N sınıfı — **26:94'ün "
 "fâsılasıyla AYNI KELİME**; **i'râb NOM 2**; **bab VIII x1**; zaman IMPF 1; dış düğüm 0 · yıldız "
 "★ yok · kökler شعر *(şair; farkında olma)* · تبع *(uyma, ardından gitme)* · غوي *(azma, azdırma)* · "
 "bağ: **ADAY 755'İN ÖN-KAYDI SINANIYOR — TAHMİN TUTTU**: شعر kökünün üçüncü geçişi burada ve "
 "ٱلشُّعَرَآء *(şairler)* biçiminde; korpusta AZINLIK anlam (dikey satırı ▸önce بغت *(ansızın "
 "gelme)* x85,3 · مكر *(tuzak)* x21,5 veriyor, yani 'farkına varma' bağlamı); **sûre adı, sûre "
 "içindeki iki geçişin anlamıyla ÖRTÜŞMÜYOR** (elle, L1, aday 775)"),
225: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim soru, kip INTG 1 · NEG 1 · "
 "şahıs 2MS x1 · 3MP x3, iltifât 0 · n=7 mora=30 harf=23 (n z=-0,58), fâsıla يَهِيمُونَ *(başıboş "
 "dolaşırlar)* → ن, N sınıfı; **i'râb ACC 1 · GEN 2**; bab I x2; zaman IMPF x2; dış düğüm 0 · "
 "yıldız ★ yok · kökler رأي *(görme)* · كلل *(hep, bütün)* · ودي *(vâdi)* · هيم *(başıboş dolaşma; "
 "susuzluk)* · bağ: **هيم *(başıboş dolaşma; susuzluk)* korpusta İKİ geçişli ve dikey ölçümü "
 "▸önce شرب *(içme)* x297,4 veriyor, ▸sonra listesi BOŞ**; **ودي *(vâdi)* korpusta 12 geçişli ve "
 "▸sonra نمل *(karınca)* x534,8 — OKUMADA GÖRÜLEN EN YÜKSEK KOMŞULUK KATI** (önceki rekor 26:181'in "
 "x661,4'üydü; bu onun altında ama tek komşulukta ikinci) (elle, L1, aday 776)"),
226: ("eksen: **lafız YOK · Rab YOK** · esmâ yok · aktör yok · edim haber, kip NEG 1 · **şahıs "
 "3MP x5 — ayette başka şahıs yok**, iltifât 0 · n=5 mora=29 harf=21 (n z=-0,79), fâsıla "
 "يَفْعَلُونَ *(yapıyorlar)* → ن, N sınıfı — **26:19 ve 26:74'ün fâsılasıyla AYNI KELİME**; "
 "**i'râb ACC 1**; bab I x2; zaman IMPF x2; dış düğüm 0 · yıldız ★ yok · **TEK İKİ KÖK: قول *(söz "
 "söyleme)* · فعل *(yapma, işleme)*** · bağ: **26:19, 26:20, 26:74 ile فعل *(yapma, işleme)* "
 "BEŞİNCİ geçişi** — 26:19'da üç kez (Firavun'un suçlaması), 26:20'de bir kez (Mûsâ'nın itirafı), "
 "26:74'te bir kez (atalar geleneği), burada söz-eylem UYUMSUZLUĞU; **قول *(söz söyleme)* ve فعل "
 "*(yapma, işleme)* karşı karşıya: يَقُولُونَ مَا لَا يَفْعَلُونَ *(yapmadıklarını söylerler)*** "
 "(elle, L1, aday 777)"),
227: ("eksen: **ALLAH LAFZI 7. sırada — sûrenin ON ÜÇÜNCÜ VE SON lafzı** (allah z=0,52) · Rab yok · "
 "esmâ yok · aktör yok · edim soru, kip RES 1 · FUT 1 · INTG 1 · **şahıs 3MP x14 — OKUMADA TEK "
 "ŞAHISTAN EN YÜKSEK SAYIM**; 3MS x1, iltifât 0 · n=19 mora=112 harf=101 — **SÛRENİN İKİNCİ EN "
 "UZUN AYETİ** (n z=0,70; en uzunu 26:49, n=21), fâsıla يَنقَلِبُونَ *(devrilirler)* → ن, N "
 "sınıfı; **i'râb GEN 3 · ACC 2**; bab I x5 · IV x1 · VII x1 · VIII x1; zaman PERF x6 · IMPF x2; "
 "**edilgen 1** (pas z=0,38); **İKİ KÖK BİRDEN İKİLENİYOR: ظلم *(zulüm, karanlık)* x2 VE قلب "
 "*(çevirme; kalp)* x2 — okumada ÜÇÜNCÜ vaka**; **biçim HASR**; **simetri [3,12,15,1] — okumada "
 "görülen en uzun ikinci bölüt**; **açık sayı sözcüğü: كثر *(çokluk)* → كَثِير**; **dış düğüm 2** · "
 "yıldız ★ yok · kökler أمن *(güven; iman)* · عمل *(iş, amel)* · صلح *(iyi, elverişli olma; ıslah)* · "
 "ذكر *(anma, zikir)* · أله *(ilâh; lafza-i celâl)* · كثر *(çokluk)* · نصر *(yardım)* · بعد *(sonra; "
 "uzaklık)* · ظلم *(zulüm, karanlık)* · علم *(bilme; ilim)* · أيي *(âyet, işaret)* · قلب *(çevirme; "
 "kalp)* · bağ: xref عمل *(amel)* + صالحة *(sâlih)* + ذكر *(zikir)* → **4:124**; انتصر *(kendini "
 "savundu)* + بعد *(sonra)* + ظلم *(zulüm)* → **42:41** (elle, L1, aday 778)"),
}

M = {
221: ("Son bölüt bir soruyla açılıyor: هَلْ أُنَبِّئُكُمْ عَلَىٰ مَن تَنَزَّلُ ٱلشَّيَٰطِينُ "
 "*(şeytanların kime indiğini size haber vereyim mi)*. **Ölçülebilir bir eşleşme: 26:210'da وَمَا "
 "تَنَزَّلَتْ بِهِ ٱلشَّيَٰطِينُ *(onu şeytanlar indirmedi)* — aynı kök, aynı bab V, aynı özne, "
 "aynı fâsıla; olumsuzdan soruya.** On bir ayet arayla iki ayet birbirinin devamı gibi. Ve نبأ "
 "*(haber)* sûrede üçüncü kez: 26:6 tehdit (alay ettiklerinin haberleri gelecek), 26:69 anlatı "
 "malzemesi (İbrâhîm'in haberi), burada bir soru. Dikey ölçüm نزل *(inme, indirme)* için ▸sonra "
 "sekîne x21,5 · sûre x20,7 veriyor — kök korpusta vahiy alanına bağlı ve burada ters yönde "
 "kullanılıyor."),
222: ("Cevap bir nitelemeyle: عَلَىٰ كُلِّ أَفَّاكٍ أَثِيمٍ *(her günahkâr yalancıya)*. Tek xref "
 "45:7'ye düşüyor ve terkip orada da aynı — donmuş kalıp adayı (aday 437). **Ölçülebilir bir üçlü: "
 "أفك *(iftira, uydurma (ifk); döndürülme)* okumada üçüncü kez ve üç ayrı göndergeyle** — 25:4'te "
 "Kur'ân'a atılan iftira (إِفْكٌ ٱفْتَرَىٰهُ), 26:45'te büyücülerin uydurması (مَا يَأْفِكُونَ), "
 "burada şeytanların indiği kişinin niteliği (أَفَّاك). Aynı kök, üç gönderge, iki sûre. أثم "
 "*(günah, ism)* korpusta 48 geçişli ve dikey ölçümü ▸önce جنف *(haktan sapma, meyletme)* x216,7 "
 "veriyor. Beş kelimenin üçü mecrur."),
223: ("İki fiil ve bir sayı sözcüğü: يُلْقُونَ ٱلسَّمْعَ وَأَكْثَرُهُمْ كَٰذِبُونَ *(kulak verirler; "
 "çoğu yalancıdır)*. **Ölçülebilir bir envanter düzeltmesi: bu, أَكْثَرُهُم'ün nakarat DIŞI tek "
 "geçişi** — aday 707'nin envanterinde 'farklı yapı' diye ayrılmıştı ve doğru ayrılmış: burada "
 "nakaratın hiçbir öğesi yok, yalnız aynı sayı sözcüğü. **Ve سمع *(işitme)* sûrede altıncı kez** — "
 "aday 763'te 'dizi kapandı' demiştim (26:220'de esmâ ile), ama bir geçiş daha varmış: burada "
 "şeytanların kulak vermesi. **Altı ayet, altı konum ve dizi esmâdan sonra tekrar gayb'a dönüyor.** "
 "Ve لقي *(karşılaşma, kavuşma; atma)* sûrede altıncı geçiş — 26:43-46'daki beş geçişten sonra."),
224: ("**Aday 755'in ön-kaydı sınanıyor ve tahmin tuttu.** 26:202'de, kıssa okunmadan önce şöyle "
 "yazmıştım: *'şعر kökünün üçüncü geçişi 26:224'te ٱلشُّعَرَآء *(şairler)* biçiminde olacak ve bu, "
 "korpusta AZINLIK anlamı; dolayısıyla sûre adı, sûrenin kendi içindeki iki geçişin anlamıyla "
 "ÖRTÜŞMEYECEK.'* **Sonuç: geçiş burada, biçim ٱلشُّعَرَآء, ve dikey satırı ▸önce بغت *(ansızın "
 "gelme)* x85,3 · مكر *(tuzak)* x21,5 veriyor — yani korpus komşuluğu 'farkına varma' bağlamı, "
 "'şair' değil.** Sûrenin iki önceki geçişi (26:113, 26:202) de 'farkına varma' anlamındaydı. "
 "**Tahmin tuttu ve bu, çalışan bir alana (kök sayımı) dayanan üçüncü başarılı ön-kayıt.** Ve "
 "fâsıla ٱلْغَاوُۥنَ 26:94'ten geri geliyor: orada mahşerde atılan taraf, burada şairlere uyanlar."),
225: ("Soru bir imgeyle: فِى كُلِّ وَادٍ يَهِيمُونَ *(her vadide başıboş dolaşırlar)*. **İki seyrek "
 "kök ve ikisi de uç komşuluk katları veriyor: هيم *(başıboş dolaşma; susuzluk)* korpusta İKİ "
 "geçişli, ▸önce شرب *(içme)* x297,4 ve ▸sonra listesi BOŞ; ودي *(vâdi)* korpusta 12 geçişli, "
 "▸sonra نمل *(karınca)* x534,8.** İkinci kat, okumada görülen en yüksek ikinci tek komşuluk "
 "(rekor 26:181'in x661,4'ü). **Ve 735'in uyarısı burada dördüncü kez geçerli: iki kök de seyrek "
 "ve komşulukları tek bir sahneden geliyor** (نمل komşuluğu 27:18'deki karınca vadisi). "
 "İstatistiksel olarak anlamsız."),
226: ("Beş kelime ve **yalnız iki kök**: وَأَنَّهُمْ يَقُولُونَ مَا لَا يَفْعَلُونَ *(yapmadıklarını "
 "söylerler)* — قول *(söz söyleme)* ve فعل *(yapma, işleme)* karşı karşıya. **Ölçülebilir bir "
 "kapanış: فعل sûrede beşinci kez** — 26:19'da üç kez (Firavun'un suçlaması: 'o yaptığını yaptın'), "
 "26:20'de bir kez (Mûsâ'nın itirafı), 26:74'te bir kez (atalar geleneği), burada **söz-eylem "
 "uyumsuzluğu**. Ve fâsıla يَفْعَلُونَ 26:19 ve 26:74'ünkiyle aynı kelime — sûre, ilk kıssada "
 "açtığı kökle kapanıyor."),
227: ("**Sûrenin son ayeti** ve okumada üç uç değer taşıyor: **3MP x14 — tek şahıstan en yüksek "
 "sayım**; n=19 — sûrenin ikinci en uzun ayeti (en uzunu 26:49, n=21); simetri [3,12,15,1] — "
 "okumada en uzun ikinci bölüt. **Ve iki kök birden ikileniyor: ظلم *(zulüm, karanlık)* x2 ve قلب "
 "*(çevirme; kalp)* x2** — okumada üçüncü vaka (26:118 فتح/بين, 26:189 عذب/يوم). Ölçülebilir bir "
 "halka: قلب sûrede beşinci ve son geçiş — 26:89 kurtuluş şartı (temiz kalp), 26:194 vahyin indiği "
 "yer, 26:200 sokulduğu yer, 26:219 dolaşma, burada **devriliş** (يَنقَلِبُونَ, bab VII). **Beş "
 "geçiş, üç anlam alanı.** Ve sûrenin son lafzı burada; on üç lafzın hepsi 26:89'dan sonraydı "
 "(aday 665). İki xref 4:124 ve 42:41'e düşüyor."),
}

ATLAMA = {
 "_blok_notu_26_221_227": ("SON BLOK BİLANÇOSU: ★★★ 0 · ★★ 0 · ★ 0 · **YEDİ AYETİN YEDİSİ DE "
  "YILDIZSIZ** — okumada görülen ilk tamamen yıldızsız blok. **ADAY 755'İN ÖN-KAYDI TUTTU** "
  "(26:224). ÇIPA NOTU: 26:225'te وَادٍ *(vâdi)* bir coğrafî ad ve هيم *(başıboş dolaşma)* bir "
  "davranış; ne ölçü ne mekanizma — çıpa sayılmadı. SÛRE 26 TAMAMLANDI: 227/227."),
}

p = '/home/claude/repo/notlar/okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
for n in range(221, 228):
    OM['26']["26:%d" % n] = {"ar": AR[(26, n)], "meal": MEAL[n], "olcum": O[n],
                             "mercek": M[n], "dikey": DIK["26:%d" % n]}
OM['26']['_mercek_atlama_notu'].update(ATLAMA)
OM['ilerleme']['not'] = ("Sûre 1 ve 9-26 TAM. Devam: sûre 27'den (ya da tur sonu onarım evresi).")
OM['ilerleme']['kismi'] = {"2": "1-20 ayet düzeyinde"}
OM['ilerleme']['okunan_ayet'] = 1949
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_metni: sûre 26 →', len([k for k in OM['26'] if not k.startswith('_')]), 'ayet')

pm = '/home/claude/repo/notlar/mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
for n in range(221, 228):
    MK['26']["26:%d" % n] = M[n]
MK['26_atlama'].update(ATLAMA)
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('mercek_kayit: sûre 26 →', len(MK['26']))
