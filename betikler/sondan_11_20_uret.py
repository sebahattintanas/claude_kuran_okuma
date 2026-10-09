# sondan_11_20_uret.py — ters okuma 11–20 (113:1 → 111:1) sayfası; depo kökünden koşulur
import sys; sys.path.insert(0,'betikler')
from ters_onluk_sayfa import sayfa_genel, W
KEYS=[(111,1),(111,2),(111,3),(111,4),(111,5),(112,1),(112,2),(112,3),(112,4),(113,1)]
K={(111,1):'N',(111,2):'N',(111,3):'N',(111,4):'N',(111,5):'N',(112,1):'L',(112,2):'L',(112,3):'O',(112,4):'O',(113,1):'R'}
HL={(112,1):[(W(112, 1, 2),'car'),(W(112, 1, 3),'laf')],(112,2):[(W(112, 2, 1),'laf')],(112,3):[(W(112, 3, 2),'car')],(112,4):[(W(112, 4, 3),'car')],(113,1):[(W(113, 1, 3),'car')],
    (111,1):[(W(111, 1, 2),'sr')],(111,3):[(W(111, 3, 4),'sr')]}
MEAL={(111,1):"Ebû Leheb'in iki eli kurusun; kurudu da.",(111,2):"Malı da kazandığı da ona fayda vermedi.",(111,3):"Alevli bir ateşe girecek.",
(111,4):"Karısı da — odun hamalı olarak,",(111,5):"boynunda hurma lifinden bükülmüş bir ip.",(112,1):"De ki: O, Allah'tır, birdir.",
(112,2):"Allah Samed'dir.",(112,3):"Doğurmadı, doğurulmadı.",(112,4):"Hiçbir şey O'na denk olmadı.",(113,1):"De ki: Sığınırım şafağın Rabbine,"}
NOT={(113,1):"Rab — ters okumada kuyruğun son taşıyıcısı.",(112,4):'O (' + W(112, 4, 3) + ') · ' + W(112, 4, 5) + ' burada ikinci kez (112:1 ile halka).',
(112,3):'O: ' + W(112, 3, 1, 2) + ' — fail Tanrı, 3MS.',(112,2):'LAFIZ — ters okumada ilk karşılaşılan lafız; mushafın SON lafzı. ' + W(112, 2, 2) + ' hapaks.',
(112,1):W(112, 1, 2) + ' önce, lafız sonra: zamir adı ÖNCELİYOR. 112:1→112:2 aralığı tek kelime: ' + W(112, 1, 4) + '.',
(111,5):"Taşıyıcı yok · sûre 111 lafızsız.",(111,4):"Taşıyıcı yok.",(111,3):'Taşıyıcı yok; 3MS (' + W(111, 3, 1) + ') Ebû Leheb — Tanrı değil. ' + W(111, 3, 4) + ' ikinci kez: ad ve alev.',
(111,2):"Taşıyıcı yok; 3MS Ebû Leheb.",(111,1):'Taşıyıcı yok; eller (' + W(111, 1, 2) + ") — 36:65 ve 36:71'deki ellerin üçüncü sahibi."}
baglam=("<b>Aralık bağlamı.</b> Sondan 11–20. ayetler. Kur'an'ın iki son lafzı burada: 112:1 ve 112:2 — aralarındaki aralık tek kelime (" + W(112, 1, 4) + '). '
 "112:2'den mushaf sonuna 52 kelimelik kuyruk; 111 sûresinin tamamı lafızsız (110:2'deki lafızdan sonra sûre sınırını geçen bir sessizlik). "
 "Ters okuyan burada ilk kez lafızla karşılaşıyor: 14. ayette (112:2).")
gozlem=('1. <b>Lafız ters okumada iki kez art arda geliyor</b> (112:2, 112:1) ve aralarında tek kelime var: ' + W(112, 1, 4) + '.<br>'
 '2. <b>Zamir adı önceliyor:</b> 112:1 ' + W(112, 1, 1, 3) + " — 'O' lafızdan önce. İleri okumada gönderim zinciri ad→zamir idi; burada zamir→ad (sonradan gönderim).<br>"
 "3. <b>Taşıyıcı merdiveni tersten:</b> Rab (113:1) → O (112:4, 112:3) → lafız (112:2, 112:1) → hiçbir şey (111). Lafızdan sonra gelen sûre (111) tamamen insan anlatısı.<br>"
 "4. <b>3MS iki tarafta:</b> 112:3'te Tanrı (" + W(112, 3, 1, 2) + "), 111:2–3'te Ebû Leheb. Aynı biçim, iki gönderge, yan yana sûrelerde.<br>"
 '5. <b>' + W(112, 1, 4) + ' halkası:</b> 112:1 ve 112:4 — sûre aynı kelimeyle açılıp kapanıyor. <b>' + W(111, 1, 4) + "</b> 111:1'de ad, 111:3'te alev.")
print(sayfa_genel(KEYS,K,HL,NOT,MEAL,"Sondan 11–20 · ters okuma ↔ mushaf düzeni (113:1 → 111:1)",baglam,gozlem,'ciktilar/sondan_11_20_ters_mushaf.html',"Sûre 111–113 henüz okunmadı — meal Claude'un çalışma çevirisi (Diyanet meali değildir)."))
