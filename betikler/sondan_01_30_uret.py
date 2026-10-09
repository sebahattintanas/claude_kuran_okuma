# -*- coding: utf-8 -*-
# sondan_01_30_uret.py — ters okuma 1–30 (114:6 → 108:3) tek sayfa; depo kökünden koşulur
import sys; sys.path.insert(0, 'betikler')
from ters_onluk_sayfa import sayfa_genel, W
KEYS = [(108,3)] + [(109,i) for i in range(1,7)] + [(110,i) for i in range(1,4)] + [(111,i) for i in range(1,6)] + [(112,i) for i in range(1,5)] + [(113,i) for i in range(1,6)] + [(114,i) for i in range(1,7)]
K = {k: 'N' for k in KEYS}
K.update({(114,1):'R',(114,2):'O',(114,3):'O',(113,2):'O',(113,1):'R',(112,4):'O',(112,3):'O',(112,2):'L',(112,1):'L',(110,3):'R',(110,2):'L',(110,1):'L',(109,3):'O',(109,5):'O'})
HL = {(114,1):[(W(114, 1, 3),'car')],(114,2):[(W(114, 2, 1),'car')],(114,3):[(W(114, 3, 1),'car')],(114,4):[(W(114, 4, 2),'sr')],
      (113,1):[(W(113, 1, 3),'car')],(113,2):[(W(113, 2, 2),'sr'),(W(113, 2, 4),'car')],(113,3):[(W(113, 3, 2),'sr')],(113,4):[(W(113, 4, 2),'sr')],(113,5):[(W(113, 5, 2),'sr')],
      (112,1):[(W(112, 1, 2),'car'),(W(112, 1, 3),'laf')],(112,2):[(W(112, 2, 1),'laf')],(112,3):[(W(112, 3, 2),'car')],(112,4):[(W(112, 4, 3),'car')],
      (111,1):[(W(111, 1, 2),'sr')],(111,3):[(W(111, 3, 4),'sr')],
      (110,1):[(W(110, 1, 4),'laf')],(110,2):[(W(110, 2, 6),'laf'),(W(110, 2, 5),'sr')],(110,3):[(W(110, 3, 3),'car'),(W(110, 3, 4),'car'),(W(110, 3, 6),'car')],
      (109,3):[(W(109, 3, 4, 2),'car')],(109,5):[(W(109, 5, 4, 2),'car')],(109,6):[(W(109, 6, 2),'sr')]}
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
NOT = {(114,6):W(114, 6, 3) + ' 5/5 · mushafın son kelimesi',(114,5):W(114, 5, 5) + ' 4/5',(114,4):"şerr (114'te tek)",(114,3):"İlâh — lafzın KÖKÜ (أله), lafız değil",
 (114,2):"Melik (işlev)",(114,1):"Rab",(113,5):"şerr 4/4 · حسد ×2",(113,4):"şerr 3/4",(113,3):"şerr 2/4",(113,2):'O (' + W(113, 2, 4) + ', 3MS) · şerr 1/4',
 (113,1):"Rab — kuyruğun ters okumadaki son taşıyıcısı",(112,4):'O (' + W(112, 4, 3) + ') · ' + W(112, 4, 5) + ' ikinci kez (112:1 ile halka)',(112,3):'O: ' + W(112, 3, 1, 2) + ' — fail Tanrı, 3MS',
 (112,2):'LAFIZ — ters okumada ilk lafız; mushafın son lafzı. ' + W(112, 2, 2) + ' hapaks',(112,1):W(112, 1, 2) + ' önce, lafız sonra: zamir adı ÖNCELİYOR. 112:1→112:2 aralığı tek kelime: ' + W(112, 1, 4),
 (111,5):"Taşıyıcı yok · sûre 111 lafızsız",(111,4):"Taşıyıcı yok",(111,3):'Taşıyıcı yok; 3MS (' + W(111, 3, 1) + ') Ebû Leheb. ' + W(111, 3, 4) + ' ikinci kez: ad ve alev',
 (111,2):"Taşıyıcı yok; 3MS Ebû Leheb",(111,1):'Taşıyıcı yok; eller (' + W(111, 1, 2) + ')',
 (110,3):'Rab + O (' + W(110, 3, 4) + ', ' + W(110, 3, 6) + ') + esmâ yüklem ' + W(110, 3, 8) + ' · elçiye emir (2MS)',
 (110,2):'LAFIZ (' + W(110, 2, 5, 2) + ') · ' + W(110, 2, 2) + ' burada da — 114 ile bağ. 110:1→110:2 aralığı 6 kelime, taşıyıcısız',(110,1):'LAFIZ (' + W(110, 1, 3, 2) + ')',
 (109,6):'Taşıyıcı yok · ' + W(109, 6, 2) + ": sizin dininiz / benim dinim → 110:2 Allah'ın dini",(109,5):"'Taptığım' (" + W(109, 5, 4, 2) + ") — Tanrı yalnız ilgi zamiriyle, 109:3'ün tekrarı",
 (109,4):"Taşıyıcı yok; 'taptığınız' = onların ilâhları",(109,3):"'Taptığım' (" + W(109, 3, 4, 2) + ') — Tanrı adsız, kulluk ilişkisiyle anılıyor',
 (109,2):'Taşıyıcı yok; ' + W(109, 2, 3, 2) + ' = onların ilâhları',(109,1):"Taşıyıcı yok; hitap kâfirlere",(108,3):'Taşıyıcı yok; ' + W(108, 3, 3) + ' burada kin besleyen — Tanrı değil'}
baglam = ("<b>Aralık bağlamı.</b> Mushafın son 30 ayeti (108:3 → 114:6), sondan başa okunuyor. Bu 30 ayette yalnız <b>4 lafız</b> var ve ikişer ikişer, "
  "tek bir sûrenin içinde: 110:1–110:2 (aralık 6 kelime) ve 112:1–112:2 (aralık 1 kelime). Mushaf sırasında 108 → 114 arasında lafız yalnız 110 ve 112'de: "
  "lafızsız ve lafızlı sûreler sırayla geliyor (108 · 109 yok — 110 var — 111 yok — 112 var — 113 · 114 yok). 112:2'den sona 52 kelimelik kuyruk.")
gozlem = ("1. <b>Lafız çiftler hâlinde ve kısa aralıklarla:</b> her iki lafızlı sûrede lafız art arda iki kez geliyor (6 ve 1 kelime arayla); aradaki sûreler tamamen lafızsız.<br>"
 "2. <b>Tanrı'ya gönderme biçimi sûreden sûreye değişiyor:</b> 114 Rab–Melik–İlâh (işlev ve kök), 113 Rab ve O, 112 O ve lafız (zamir adı önceliyor), 111 hiç, 110 lafız, Rab, O ve esmâ yüklem (" + W(110, 3, 8) + "), 109 yalnız ilgi zamiri: 'taptığım' (" + W(109, 3, 4, 2) + ').<br>'
 "3. <b>109'da Tanrı ad almıyor:</b> iki taraf da aynı kalıpla anılıyor — 'taptığım' / 'taptığınız'. Ayrım ad üzerinden değil, kulluk ilişkisi üzerinden.<br>"
 "4. <b>Din ve insanlar zinciri:</b> 109:6 sizin dininiz / benim dinim → 110:2 Allah'ın dini; " + W(110, 2, 2) + " 110:2'de ve 114'te beş kez.<br>"
 '5. <b>3MS her zaman Tanrı değil:</b> 108:3 ' + W(108, 3, 3) + ' kin besleyen, 111:2–3 Ebû Leheb, 112:3 Tanrı — üç komşu sûrede üç gönderge.<br>'
 "6. <b>Ters okuma yönü:</b> sondan başa okuyan önce 52 kelimelik sessizlikten, sonra kısa aralıklı iki lafız çiftinden geçiyor; ilk lafza 14. ayette, ikinci çifte 22. ayette varıyor.")
print(sayfa_genel(KEYS, K, HL, NOT, MEAL, "Sondan 1–30 · ters okuma ↔ mushaf düzeni (114:6 → 108:3)", baglam, gozlem, 'ciktilar/sondan_01_30_ters_mushaf.html',
  "Sûre 108–114 henüz okunmadı — meal Claude'un çalışma çevirisi (Diyanet meali değildir)."))
