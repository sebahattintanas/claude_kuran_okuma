# -*- coding: utf-8 -*-
# sondan_31_60_uret.py — ters okuma 31–60 (108:2 → 103:1) tek sayfa; depo kökünden koşulur
import sys; sys.path.insert(0, 'betikler')
from ters_onluk_sayfa import sayfa_genel
AY = {103: 3, 104: 9, 105: 5, 106: 4, 107: 7}
KEYS = [(s, a) for s in range(103, 108) for a in range(1, AY[s] + 1)] + [(108, 1), (108, 2)]
K = {k: 'N' for k in KEYS}
K.update({(104,4):'E',(104,6):'L',(104,8):'E',(104,9):'E',(105,1):'R',(105,2):'O',(105,3):'O',(105,5):'O',(106,3):'R',(106,4):'O',(108,1):'B',(108,2):'R'})
HL = {(104,1):[('وَيْلٌ','sr')],(104,4):[('لَيُنۢبَذَنَّ','pas')],(104,6):[('ٱللَّهِ','laf'),('ٱلْمُوقَدَةُ','pas')],(104,8):[('مُّؤْصَدَةٌ','pas')],(104,9):[('مُّمَدَّدَةٍ','pas')],
      (105,1):[('فَعَلَ','car'),('رَبُّكَ','car')],(105,2):[('يَجْعَلْ','car')],(105,3):[('وَأَرْسَلَ','car')],(105,5):[('فَجَعَلَهُمْ','car')],
      (106,3):[('رَبَّ','car')],(106,4):[('أَطْعَمَهُم','car'),('وَءَامَنَهُم','car')],(107,3):[('طَعَامِ','sr')],(107,4):[('فَوَيْلٌ','sr'),('لِّلْمُصَلِّينَ','sr')],
      (108,1):[('إِنَّآ أَعْطَيْنَٰكَ','car')],(108,2):[('فَصَلِّ','sr'),('لِرَبِّكَ','car')]}
MEAL = {(103,1):"Asra andolsun,",(103,2):"insan gerçekten ziyandadır,",(103,3):"iman edip salih ameller işleyenler, birbirine hakkı ve sabrı tavsiye edenler hariç.",
 (104,1):"Arkadan çekiştiren, alay eden herkesin vay hâline!",(104,2):"Ki o mal toplayıp onu sayıp durdu.",(104,3):"Malının kendisini ölümsüz kılacağını sanır.",
 (104,4):"Hayır! Andolsun, Hutame'ye atılacak.",(104,5):"Hutame nedir, sana ne bildirdi?",(104,6):"Allah'ın tutuşturulmuş ateşidir,",
 (104,7):"ki gönüllerin üzerine çıkar.",(104,8):"Şüphesiz o, üzerlerine kapatılmıştır,",(104,9):"uzatılmış direkler içinde.",
 (105,1):"Rabbinin fil sahiplerine ne yaptığını görmedin mi?",(105,2):"Onların tuzağını boşa çıkarmadı mı?",(105,3):"Üzerlerine bölük bölük kuşlar gönderdi;",
 (105,4):"onlara pişmiş çamurdan taşlar atıyorlardı.",(105,5):"Sonunda onları yenilmiş ekin yaprağı gibi yaptı.",
 (106,1):"Kureyş'in ülfeti için,",(106,2):"kış ve yaz yolculuğundaki ülfetleri için,",(106,3):"bu Evin Rabbine kulluk etsinler;",
 (106,4):"ki O, onları açlıktan doyurdu ve korkudan güvende kıldı.",
 (107,1):"Dini yalanlayanı gördün mü?",(107,2):"İşte o, yetimi itip kakan,",(107,3):"yoksulu doyurmaya teşvik etmeyendir.",(107,4):"Vay hâline o namaz kılanların,",
 (107,5):"ki onlar namazlarından gafildirler,",(107,6):"ki onlar gösteriş yaparlar,",(107,7):"ve en küçük yardımı bile esirgerler.",
 (108,1):"Şüphesiz Biz sana Kevser'i verdik.",(108,2):"Öyleyse Rabbin için namaz kıl ve kurban kes."}
NOT = {(108,2):"Rab (لِرَبِّكَ) · elçiye emir · فَصَلِّ ↔ 107:4 namaz kılanlar",(108,1):"Biz (إِنَّآ أَعْطَيْنَٰكَ) — Tanrı konuşuyor",
 (107,7):"Taşıyıcı yok",(107,6):"Taşıyıcı yok",(107,5):"Taşıyıcı yok",(107,4):"Taşıyıcı yok · وَيْل ikinci kez (104:1) · namaz kılanlar ↔ 108:2 namaz kıl",
 (107,3):"Taşıyıcı yok; 3MS yalanlayan · طَعَام ↔ 106:4 أَطْعَمَهُم (doyurdu)",(107,2):"Taşıyıcı yok; 3MS yalanlayan",(107,1):"Taşıyıcı yok; 3MS yalanlayan — Tanrı değil",
 (106,4):"O (ٱلَّذِىٓ أَطْعَمَهُم … وَءَامَنَهُم) — Rab'dan gelen gönderim zinciri",(106,3):"Rab — sûrenin tek adı",(106,2):"Taşıyıcı yok",(106,1):"Taşıyıcı yok",
 (105,5):"O (فَجَعَلَهُمْ) — zincirin dördüncü halkası",(105,4):"Taşıyıcı yok; özne kuşlar",(105,3):"O (أَرْسَلَ)",(105,2):"O (يَجْعَلْ)",
 (105,1):"Rab + O (فَعَلَ رَبُّكَ) — sûre adı Rab ile koyuyor, sonra yalnız zamir",
 (104,9):"Edilgen (مُمَدَّدَة) — uzatan adsız",(104,8):"Edilgen (مُؤْصَدَة) — kapatan adsız",(104,7):"Taşıyıcı yok",
 (104,6):"LAFIZ — sûrenin TEK lafzı; ٱلْمُوقَدَة edilgen: tutuşturan adsız",(104,5):"Taşıyıcı yok; 'sana ne bildirdi' (genel 3MS)",
 (104,4):"Edilgen (لَيُنۢبَذَنَّ) — atan adsız",(104,3):"Taşıyıcı yok; 3MS çekiştiren",(104,2):"Taşıyıcı yok; 3MS çekiştiren",(104,1):"Taşıyıcı yok · وَيْل",
 (103,3):"Taşıyıcı yok",(103,2):"Taşıyıcı yok",(103,1):"Taşıyıcı yok · yemin (وَٱلْعَصْرِ)"}
baglam = ("<b>Aralık bağlamı.</b> Sondan 31–60 (108:2 → 103:1). Bu 30 ayette <b>tek bir lafız</b> var: 104:6 نَارُ ٱللَّهِ. 104 tek lafızlı bir sûre: lafızdan önce 5 ayet, sonra 3 ayet; "
  "sûre içinde iki lafız arası aralık yok. 103, 105, 106, 107, 108 lafızsız. Ters okuyan ilk 30 ayetteki dört lafızdan sonra burada 30 ayette yalnız bir lafızla karşılaşıyor.")
gozlem = ("1. <b>Rab, lafız gibi çapa oluyor:</b> 105:1 فَعَلَ رَبُّكَ — ad bir kez Rab olarak konuyor, sonra dört halkalı bir zamir zinciri (يَجْعَلْ · أَرْسَلَ · جَعَلَهُمْ). 106'da aynı: رَبَّ هَٰذَا ٱلْبَيْتِ → ٱلَّذِىٓ أَطْعَمَهُم. Lafızsız sûrelerde gönderim zinciri Rab'dan başlıyor.<br>"
 "2. <b>Tek lafzın çevresi edilgenle dolu:</b> 104:4 atılacak · 104:6 tutuşturulmuş · 104:8 kapatılmış · 104:9 uzatılmış. Lafız bir kez geçiyor; yapan, önünde ve arkasında adsız edilgenlerle taşınıyor.<br>"
 "3. <b>Komşu sûreler arasında kök köprüleri:</b> 106:4 أَطْعَمَهُم (doyurdu) ↔ 107:3 طَعَامِ ٱلْمِسْكِينِ (yoksulu doyurma); 107:4 ٱلْمُصَلِّينَ ↔ 108:2 فَصَلِّ; وَيْل 104:1 ve 107:4.<br>"
 "4. <b>3MS yine insan:</b> 104:2–3 çekiştiren, 107:1–3 yalanlayan — Tanrı'ya gitmiyor; 105:2–5'te Tanrı'ya gidiyor. Sayım (1027) ayıramıyor.<br>"
 "5. <b>Biz bir kez:</b> 108:1 — ters okumada Biz sesi ilk kez burada (sondan 32. ayet).")
print(sayfa_genel(KEYS, K, HL, NOT, MEAL, "Sondan 31–60 · ters okuma ↔ mushaf düzeni (108:2 → 103:1)", baglam, gozlem, 'ciktilar/sondan_31_60_ters_mushaf.html',
  "Sûre 103–108 henüz okunmadı — meal Claude'un çalışma çevirisi (Diyanet meali değildir)."))
