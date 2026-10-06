# -*- coding: utf-8 -*-
# sondan_01_30_uret.py — ters okuma 1–30 (114:6 → 108:3) tek sayfa; depo kökünden koşulur
import sys; sys.path.insert(0, 'betikler')
from ters_onluk_sayfa import sayfa_genel
KEYS = [(108,3)] + [(109,i) for i in range(1,7)] + [(110,i) for i in range(1,4)] + [(111,i) for i in range(1,6)] + [(112,i) for i in range(1,5)] + [(113,i) for i in range(1,6)] + [(114,i) for i in range(1,7)]
K = {k: 'N' for k in KEYS}
K.update({(114,1):'R',(114,2):'O',(114,3):'O',(113,2):'O',(113,1):'R',(112,4):'O',(112,3):'O',(112,2):'L',(112,1):'L',(110,3):'R',(110,2):'L',(110,1):'L',(109,3):'O',(109,5):'O'})
HL = {(114,1):[('بِرَبِّ','car')],(114,2):[('مَلِكِ','car')],(114,3):[('إِلَٰهِ','car')],(114,4):[('شَرِّ','sr')],
      (113,1):[('بِرَبِّ','car')],(113,2):[('شَرِّ','sr'),('خَلَقَ','car')],(113,3):[('شَرِّ','sr')],(113,4):[('شَرِّ','sr')],(113,5):[('شَرِّ','sr')],
      (112,1):[('هُوَ','car'),('ٱللَّهُ','laf')],(112,2):[('ٱللَّهُ','laf')],(112,3):[('يَلِدْ','car')],(112,4):[('لَّهُۥ','car')],
      (111,1):[('يَدَآ','sr')],(111,3):[('لَهَبٍ','sr')],
      (110,1):[('ٱللَّهِ','laf')],(110,2):[('ٱللَّهِ','laf'),('دِينِ','sr')],(110,3):[('رَبِّكَ','car'),('وَٱسْتَغْفِرْهُ','car'),('إِنَّهُۥ','car')],
      (109,3):[('مَآ أَعْبُدُ','car')],(109,5):[('مَآ أَعْبُدُ','car')],(109,6):[('دِينُكُمْ','sr')]}
MEAL = {(108,3):"Asıl soyu kesik olan, sana kin besleyendir.",(109,1):"De ki: Ey kâfirler!",(109,2):"Ben sizin taptığınıza tapmam.",
 (109,3):"Siz de benim taptığıma tapacak değilsiniz.",(109,4):"Ben de sizin taptığınıza tapacak değilim.",(109,5):"Siz de benim taptığıma tapacak değilsiniz.",
 (109,6):"Sizin dininiz size, benim dinim bana.",(110,1):"Allah'ın yardımı ve fetih geldiğinde,",(110,2):"ve insanların bölük bölük Allah'ın dinine girdiğini gördüğünde,",
 (110,3):"Rabbini hamd ile tesbih et ve O'ndan bağışlanma dile. Şüphesiz O, tövbeleri çok kabul edendir.",
 (111,1):"Ebû Leheb'in iki eli kurusun; kurudu da.",(111,2):"Malı da kazandığı da ona fayda vermedi.",(111,3):"Alevli bir ateşe girecek.",
 (111,4):"Karısı da — odun hamalı olarak,",(111,5):"boynunda hurma lifinden bükülmüş bir ip.",(112,1):"De ki: O, Allah'tır, birdir.",
 (112,2):"Allah Samed'dir.",(112,3):"Doğurmadı, doğurulmadı.",(112,4):"Hiçbir şey O'na denk olmadı.",(113,1):"De ki: Sığınırım şafağın Rabbine,",
 (113,2):"yarattığı şeylerin şerrinden,",(113,3):"çöktüğünde karanlığın şerrinden,",(113,4):"düğümlere üfleyenlerin şerrinden,",(113,5):"ve haset ettiğinde hasetçinin şerrinden.",
 (114,1):"De ki: Sığınırım insanların Rabbine,",(114,2):"insanların Melik'ine,",(114,3):"insanların İlâh'ına,",(114,4):"sinsi vesvesecinin şerrinden,",
 (114,5):"ki o, insanların göğüslerine vesvese verir,",(114,6):"cinlerden ve insanlardan."}
NOT = {(114,6):"ٱلنَّاس 5/5 · mushafın son kelimesi",(114,5):"ٱلنَّاس 4/5",(114,4):"şerr (114'te tek)",(114,3):"İlâh — lafzın KÖKÜ (أله), lafız değil",
 (114,2):"Melik (işlev)",(114,1):"Rab",(113,5):"şerr 4/4 · حسد ×2",(113,4):"şerr 3/4",(113,3):"şerr 2/4",(113,2):"O (خَلَقَ, 3MS) · şerr 1/4",
 (113,1):"Rab — kuyruğun ters okumadaki son taşıyıcısı",(112,4):"O (لَّهُۥ) · أَحَد ikinci kez (112:1 ile halka)",(112,3):"O: لَمْ يَلِدْ — fail Tanrı, 3MS",
 (112,2):"LAFIZ — ters okumada ilk lafız; mushafın son lafzı. ٱلصَّمَد hapaks",(112,1):"هُوَ önce, lafız sonra: zamir adı ÖNCELİYOR. 112:1→112:2 aralığı tek kelime: أَحَدٌ",
 (111,5):"Taşıyıcı yok · sûre 111 lafızsız",(111,4):"Taşıyıcı yok",(111,3):"Taşıyıcı yok; 3MS (سَيَصْلَىٰ) Ebû Leheb. لَهَب ikinci kez: ad ve alev",
 (111,2):"Taşıyıcı yok; 3MS Ebû Leheb",(111,1):"Taşıyıcı yok; eller (يَدَا)",
 (110,3):"Rab + O (وَٱسْتَغْفِرْهُ, إِنَّهُۥ) + esmâ yüklem تَوَّاب · elçiye emir (2MS)",
 (110,2):"LAFIZ (دِينِ ٱللَّهِ) · ٱلنَّاس burada da — 114 ile bağ. 110:1→110:2 aralığı 6 kelime, taşıyıcısız",(110,1):"LAFIZ (نَصْرُ ٱللَّهِ)",
 (109,6):"Taşıyıcı yok · دِين: sizin dininiz / benim dinim → 110:2 Allah'ın dini",(109,5):"'Taptığım' (مَآ أَعْبُدُ) — Tanrı yalnız ilgi zamiriyle, 109:3'ün tekrarı",
 (109,4):"Taşıyıcı yok; 'taptığınız' = onların ilâhları",(109,3):"'Taptığım' (مَآ أَعْبُدُ) — Tanrı adsız, kulluk ilişkisiyle anılıyor",
 (109,2):"Taşıyıcı yok; مَا تَعْبُدُونَ = onların ilâhları",(109,1):"Taşıyıcı yok; hitap kâfirlere",(108,3):"Taşıyıcı yok; هُوَ burada kin besleyen — Tanrı değil"}
baglam = ("<b>Aralık bağlamı.</b> Mushafın son 30 ayeti (108:3 → 114:6), sondan başa okunuyor. Bu 30 ayette yalnız <b>4 lafız</b> var ve ikişer ikişer, "
  "tek bir sûrenin içinde: 110:1–110:2 (aralık 6 kelime) ve 112:1–112:2 (aralık 1 kelime). Mushaf sırasında 108 → 114 arasında lafız yalnız 110 ve 112'de: "
  "lafızsız ve lafızlı sûreler sırayla geliyor (108 · 109 yok — 110 var — 111 yok — 112 var — 113 · 114 yok). 112:2'den sona 52 kelimelik kuyruk.")
gozlem = ("1. <b>Lafız çiftler hâlinde ve kısa aralıklarla:</b> her iki lafızlı sûrede lafız art arda iki kez geliyor (6 ve 1 kelime arayla); aradaki sûreler tamamen lafızsız.<br>"
 "2. <b>Tanrı'ya gönderme biçimi sûreden sûreye değişiyor:</b> 114 Rab–Melik–İlâh (işlev ve kök), 113 Rab ve O, 112 O ve lafız (zamir adı önceliyor), 111 hiç, 110 lafız, Rab, O ve esmâ yüklem (تَوَّاب), 109 yalnız ilgi zamiri: 'taptığım' (مَآ أَعْبُدُ).<br>"
 "3. <b>109'da Tanrı ad almıyor:</b> iki taraf da aynı kalıpla anılıyor — 'taptığım' / 'taptığınız'. Ayrım ad üzerinden değil, kulluk ilişkisi üzerinden.<br>"
 "4. <b>Din ve insanlar zinciri:</b> 109:6 sizin dininiz / benim dinim → 110:2 Allah'ın dini; ٱلنَّاس 110:2'de ve 114'te beş kez.<br>"
 "5. <b>3MS her zaman Tanrı değil:</b> 108:3 هُوَ kin besleyen, 111:2–3 Ebû Leheb, 112:3 Tanrı — üç komşu sûrede üç gönderge.<br>"
 "6. <b>Ters okuma yönü:</b> sondan başa okuyan önce 52 kelimelik sessizlikten, sonra kısa aralıklı iki lafız çiftinden geçiyor; ilk lafza 14. ayette, ikinci çifte 22. ayette varıyor.")
print(sayfa_genel(KEYS, K, HL, NOT, MEAL, "Sondan 1–30 · ters okuma ↔ mushaf düzeni (114:6 → 108:3)", baglam, gozlem, 'ciktilar/sondan_01_30_ters_mushaf.html',
  "Sûre 108–114 henüz okunmadı — meal Claude'un çalışma çevirisi (Diyanet meali değildir)."))
