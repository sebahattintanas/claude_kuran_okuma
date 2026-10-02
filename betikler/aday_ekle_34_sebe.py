# -*- coding: utf-8 -*-
"""aday_ekle_34_sebe.py — sûre 34 (Sebe') adayları (AS_sebe) ve okuma bağları (AN_sebe).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (998'den); betik sıranın kopmadığını doğrular.
"""
import json

SEBE = [
# ---------------- blok 1-10 ----------------
{"no":998,
 "aday":"MÜHÜR SIRASI — rahîm ile gafûr korpusta 72 ayette bitişik (içerik lemması dizisi); 71'inde gafûr önce, YALNIZ 34:2'de rahîm önce.",
 "olculen":{"gafur_rahim":71,"rahim_gafur":1,"ters_ayet":"34:2","yontem":"morph.txt, kökü olan lemmaların kelime sırası, ardışık çift (TAM SAYIM)"},
 "durum":"KAYIT","oncelik":"-","kaynak":"sûre 34 okuması, blok 1-10","etiket":"gözlem — TAM SAYIM, yorum yok",
 "test_notu":"Sayım tam; 'neden' iddiası kurulmadı. Ayetin konusu (yer/gök hareket tablosu) ile sıra arasında bağ aranırsa KAPATILAMAZ (tek vaka, boş model yok)."},
{"no":999,
 "aday":"ESMÂ SINIR VAKASI — tamlama içinde ad olarak esmâ: 34:6 sırâtı'l-azîzi'l-hamîd. İsimler yüklem/sıfat değil muzâfun ileyh; göndergesi Allah. Okuyucu kararı 'ilahi'.",
 "olculen":{"ayet":"34:6","kelime":[15,16],"e_el":"ilahi","muhur_43":"ÇİFT, ton karma"},
 "durum":"ACIK","oncelik":"P1","kaynak":"sûre 34 okuması, blok 1-10","etiket":"ön-kayıt veri toplama (e_suzgec geliştirme kümesi)",
 "test_notu":"Ön-kayıt §4.2 'yüklem/sıfat konumu' diyor; bu konum türü tanımda yok. Ön-kayıt DEĞİŞTİRİLMEDİ (dondurulmuş); karar esma_el'de gerekçesiyle, süzgeç kodlanırken bu tür ayrıca ele alınacak. Sapma değil, tanımın kapsamadığı durumun kaydı."},
{"no":1000,
 "aday":"GLOSS BASKINLIĞI (aday 987 ailesi) — iki ek vaka: أخر 'geciktirme' glossu, baskın lemma âhir 155 / fiil ahhara 15 (34:1, 34:8 âhira); حدد 'demir; sınır koyma', baskın hudûd 14 / hadîd 6 (sıra ters, anlam mevcut).",
 "olculen":{"أخر":{"آخِر":155,"آخَر":70,"أَخَّرَ":15},"حدد":{"حُدُود":14,"حَدِيد":6}},
 "durum":"ACIK","oncelik":"P1","kaynak":"sûre 34 okuması, blok 1-10","etiket":"987 kalan: 1112 kökün gloss taraması",
 "test_notu":"Onarılmadı (araç dondurması). Ölçüm etkisi yok; dikey ve kök satırlarında görüntü."},
 # ---------------- blok 11-20 ----------------
{"no":1001,
 "aday":"BİLANÇO ETİKET ARIZASI (kendi aracım) — blok_bilanco.yildiz_kaynagi en büyük |z|'yi kaynak diye yazıyor, eşiği geçmese de. Formül (22_hapaks_onarim): kafiye kırığı ★'ı YALNIZ diğer bileşenlerin hepsi |z| ≤ 1,5 iken veriyor; bu ayetlerde kaynak kafiye kırığıdır.",
 "olculen":{"vaka":{"31":[14],"32":[23],"33":[],"34":[18,19]},"yanlis_etiket":{"34:18":"allah -0,53","34:19":"rab 0,80"},
   "etki":"sûre 33 kapanış bilançosu etkilenmedi (0 vaka); 31 ve 32 tur sonu kaynak sayımlarında birer vaka",
   "yontem":"defter.json z2 + yildiz2, |z| ≤ 1,5 iken ★ > 0 olan ayetler (TAM SAYIM, sûre 31-34)"},
 "durum":"ACIK","oncelik":"P1","kaynak":"sûre 34 okuması, blok 11-20","etiket":"araç açığı — kendi bilanço betiğim (aday 924: metin hakkında kanıt değil)",
 "test_notu":"Onarılmadı (araç dondurması; okumayı bloke etmiyor). Okumada bu ayetlerin ★ kaynağı elle 'kafiye kırığı' diye yazılıyor. Ayrıca borç #15'in sınırı netleşti: kırık yıldıza toplanmıyor, yalnız başka işaret yoksa ★ veriyor."},
{"no":1002,
 "aday":"ÇIPA TANIM AÇIĞI — L4 BİÇİMLİ AMA OLGUSUZ: 34:12 rüzgârın sabah gidişi bir ay, akşam dönüşü bir ay (süre birimi) ama iddia Süleyman'a verilen tasarruf, doğal düzenlilik değil.",
 "olculen":{"ayet":"34:12","kademe":"L4-biçim","olgu":False,"cipa":False,"tarayici":"aday vermedi"},
 "durum":"ACIK","oncelik":"P0","kaynak":"sûre 34 okuması, blok 11-20","etiket":"965 ailesi (çıpa merdiveni tanım açıkları)",
 "test_notu":"Eşik (onarim 18) L4'ü tanımlıyor ama olgu koşulunu çıpa kararına açıkça bağlamıyor. 27:39-40 (ifrît, göz açıp kapama) birimsiz olduğu için L1'di; burada birim var. Karar: çıpa verilmedi, tanım borcu kaydedildi."},

 # ---------------- blok 21-30 ----------------
{"no":1003,
 "aday":"KENDİ OKUMA HATAM + ARAÇ AÇIĞI — 34:3 merceğinde nakarat3'ün 7 kelimelik kalıbı 10:61'e bağlandı; kalıp SÛRE İÇİ (34:3 ↔ 34:22). Ölçüm satırı nakarat3 için eş ayeti basmıyor, yalnız 'N ayet, tür ic' yazıyor; eş xref ile karıştırıldı.",
 "olculen":{"yanlis":"34:3 mercek: 'nakarat3 10:61 ile 7 kelime'","dogru":"7 kelimelik kalıp yalnız 34:3 ve 34:22; 10:61 ile bağ xref + عزب",
   "10:61_farki":"10:61'de 'fi'l-ard ve lâ fi's-semâ' — sıra ters, kalıp yok",
   "diger_kontrol":"34:1-20'deki öteki nakarat3 anmaları eşleriyle tarandı: 34:5↔34:38, 34:7↔34:19, 34:9↔34:19 ve 34:24, 34:2↔34:22 — eş ADI verilen anmalar doğru"},
 "durum":"KAYIT","oncelik":"P2","kaynak":"sûre 34 okuması, blok 21-30","etiket":"kendi kaydım düştü — duzeltildi alanı (duzeltme_34.py); özgün mercek korundu",
 "test_notu":"Bundan sonra nakarat3 eşi yazılmadan önce defterden (nakarat3 kalıbı → ayet listesi) koşulacak. olcum_bicim'in eşi basmaması araç açığı; dondurma nedeniyle onarılmadı."},

 # ---------------- blok 31-40 ----------------
{"no":1004,
 "aday":"SAY ALANI (981 ailesi) — 'ekser' her zaman yanlış pozitif değil: 34:35'te GERÇEK karşılaştırmalı nicelik iddiası ('mal ve evlatça daha çoğuz'), 34:28 ve 34:36'da nicelik belirteci ('insanların çoğu'). Aynı lemma iki işlev.",
 "olculen":{"34:35":"karşılaştırma (nahnu ekseru emvâlen ve evlâden) — doğru pozitif sayılabilir","34:28":"belirteç — yanlış pozitif","34:36":"belirteç — yanlış pozitif"},
 "durum":"ACIK","oncelik":"P1","kaynak":"sûre 34 okuması, blok 31-40","etiket":"981/992 say alanı — yanlış pozitif sayımına düzeltme girdisi",
 "test_notu":"981'in 'a'adde 6/6 yanlış pozitif' sayımı gibi ekser için de ayrım gerek: ekser + temyiz (ACC isim) = karşılaştırma; ekser + muzâfun ileyh (en-nâs) = belirteç. Kural önerisi — kodlanmadı (dondurma)."},

 # ---------------- blok 41-50 ----------------
{"no":1005,
 "aday":"SAY ALANI GERÇEK SAYI AYETİ (981/1004 ailesi, doğru pozitif ve yanlış negatif): 34:45 mi'şâr (onda bir, lemma korpusta tek ayet) doğru pozitif; 34:46 vâhide + mesnâ doğru, furâdâ (teker teker) YAKALANMIYOR.",
 "olculen":{"34:45":{"mi'şâr":"doğru pozitif — kesir 1/10"},"34:46":{"yakalanan":["vâhide","mesnâ"],"kaçırılan":["furâdâ (6:94, 34:46)"]},
   "sure34_say_toplam":"blok bilançolarından sûre kapanışında koşulacak"},
 "durum":"ACIK","oncelik":"P1","kaynak":"sûre 34 okuması, blok 41-50","etiket":"981 — say alanının kesinlik/duyarlılık girdisi",
 "test_notu":"Sûre 34'teki say işaretleri tek tek sınıflandı: qalîl ×2 ve ekser ×3 belirteç (yanlış pozitif), ekser 34:35 karşılaştırma (sınır), mi'şâr ve vâhide/mesnâ doğru; ikil 'iki bahçe' (34:15-16), 'bir ay' (34:12), furâdâ yanlış negatif."},
{"no":1006,
 "aday":"TARAYICI v4 SAYI TETİKLEMESİ (948 birikimi) — 34:46'da aday, doğal olgu yok; tetikleyici sayı kelimeleri. Sûre 34'te üç aday (34:9, 34:14, 34:46), çıpa 0.",
 "olculen":{"adaylar":["34:9","34:14","34:46"],"cipa_L4":0,"kesinlik":"0/3 (sûre 34, 1-50)"},
 "durum":"ACIK","oncelik":"P0","kaynak":"sûre 34 okuması, blok 41-50","etiket":"948 tarayıcı borcu — sûre 33: 0/0, kesinlik 0/12 birikimine ek",
 "test_notu":"Sûre kapanışında 51-54 eklenerek son sayı koşulacak."},

]

BAGLAR = {"AN_sebe": [
 # blok 1-10
 {"bag":"34:1 → 34:6","kural":"kök (حمد 3/3)","not":"Hamd ipliği sûrenin ilk altı ayetinde açılıp kapanıyor: iki alanlı hamd (gökler-yer / âhiret) → azîz-hamîd'in yolu."},
 {"bag":"28:70 ↔ 34:1","kural":"lemma (hamd + âhir, TAM SAYIM 4 ayet)","not":"Hamdın âhirete konduğu iki ayet: ûlâ ve âhira / gökler-yer ve âhira."},
 {"bag":"34:2 ↔ 57:4","kural":"xref (7 lemmalık dizi)","not":"Yere giren/çıkan, gökten inen/yükselen; 57:4'te yaratılış ve istivâdan sonra, mühür basîr. 57 okunmadı."},
 {"bag":"10:61 ↔ 34:3","kural":"nakarat3 (7 kelime) + xref + kök (عزب 2/2)","not":"Zerre ölçeği: referans nokta + daha küçüğü ve büyüğü; عزب korpusta yalnız bu iki ayette.","duzeltildi":"nakarat3 kuralı YANLIŞ — kalıp sûre içi (34:22); bu bağın dayanağı yalnız xref + عزب (aday 1003)"},
 {"bag":"34:4-5 ↔ 22:50-51","kural":"esit2 (22:50 BENZER 0,8706) + xref","not":"Aynı ayna çifti: iman+amel → mağfiret+kerîm rızık / âyetleri boşa çıkarmaya çabalayanlar → azap."},
 {"bag":"34:5 → 34:38","kural":"lemma (mu'âcizîn 3 ayet)","not":"Aynı çaba ifadesi sûrede ikinci kez; 34:38 henüz okunmadı."},
 {"bag":"34:3 · 34:7-8","kural":"okuma gözlemi","not":"Kâfirlerin iki sözü ikisi de âhiret inkârı: saat gelmez / yeni yaratılışı haber veren adam; 34:8 cevabı ikisini tek sınıfa topluyor."},
 {"bag":"34:7 → 34:19","kural":"nakarat3 + kök (مزق, korpusta yalnız bu iki ayet)","not":"Paramparça dağılma: iddianın konusu (beden) → 34:19 henüz okunmadı."},
 {"bag":"26:187 ↔ 34:9","kural":"xref (düşürmek · parça · gök)","not":"Aynı ifade iki yönde: kavmin talebi (26:187) / tehdit (34:9)."},
 {"bag":"21:79 ↔ 34:10","kural":"kök (جبل + طير birlikte 3 ayet)","not":"Dâvûd ile tesbih eden dağlar ve kuşlar — aynı sahne iki sûrede."},
 # blok 11-20
 {"bag":"34:3 ↔ 34:14","kural":"kök (غيب 1-2/4)","not":"Gaybın bilicisi Rab / gaybı bilmeyen cinler — aynı kök iki zıt özne."},
 {"bag":"34:11 · 34:18","kural":"kök (قدر)","not":"Örgüde ölçü (zırh) / yolda ölçü (kasabalar arası yürüyüş)."},
 {"bag":"34:13 · 34:15 · 34:19","kural":"kök (شكر 4/4)","not":"Şükür ipliği: şükür olarak çalışın + az olan şekûr / şükredin / sabbâr şekûr."},
 {"bag":"34:15 → 34:16","kural":"okuma gözlemi (ikil korunuyor)","not":"İki bahçe → iki bahçe; sayı ve yön kalıyor, meyve ve ağaç değişiyor."},
 {"bag":"34:17 · 33:3","kural":"okuma gözlemi (iki kök ikişer, kapalı halka)","not":"Kısa ayette kök çiftlerinin kendi içinde kapanması."},
 {"bag":"34:18 ↔ 34:19","kural":"kök (بين 5-7/16)","not":"Aralarına görünen kasabalar kıldık / aramızı uzaklaştır — nimetin tersine çevrilen talebi."},
 {"bag":"34:7 → 34:19","kural":"nakarat3 + kök (مزق 4/4) — DOĞRULANDI","not":"Kâfirlerin alay ettiği bedensel dağılma → kavmin dağıtılması; iplik 34:19'da kapanıyor."},
 {"bag":"34:9 ↔ 34:19","kural":"nakarat3 (5 kelime)","not":"Bunda ... her ... için âyet(ler): abdin münîb / sabbârin şekûr."},
 {"bag":"34:13 ↔ 34:20","kural":"okuma gözlemi","not":"Az olan şükreden kullar / uymayan bir grup mü'min — iki azınlık ifadesi."},
 {"bag":"21:81 ↔ 34:12","kural":"okuma gözlemi (borç 972)","not":"Süleyman ve rüzgâr; köksüz ad ikili alanında görünmüyor."},
 {"bag":"27:22 ↔ 34:15","kural":"aktör (PN Sebe', korpusta 2 ayet)","not":"Hüdhüdün getirdiği haber / sûrenin adı olan kavmin iki bahçesi."},
 {"bag":"34:16 · 53:14 · 53:16 · 56:28","kural":"kök (سدر, 4 ayet)","not":"Sidr: cezanın bitkisi (34:16) / sidre ve cennet sidri (öteki üç)."},
 # blok 21-30
 {"bag":"34:3 ↔ 34:22","kural":"nakarat3 (7 kelime, sûre içi) + kök (ثقل 2/2, ذرر 2/2)","not":"Aynı zerre ölçeği: bilginin kapsamı (hiçbir şey O'ndan gizli değil) / mülkün kapsamı (onlar hiçbir şeye sahip değil)."},
 {"bag":"34:12 ↔ 34:23","kural":"kök (أذن 2/2)","not":"Cinler Rabbinin izniyle çalışıyor / şefaat ancak izinle."},
 {"bag":"34:18 ↔ 34:22","kural":"kök (ظهر 2/2)","not":"Görünen kasabalar / yardımcı — aynı kök iki anlam."},
 {"bag":"34:22 → 34:27","kural":"kök (شرك 2/2)","not":"Ortaklıkları yok / ortaklarınızı gösterin — hayır."},
 {"bag":"34:1 · 34:6 → 34:27","kural":"kök (حكم 2/2, عزز 2/2)","not":"Sûrenin ilk iki esmâ kökü 34:27'deki azîz-hakîm mührüyle kapanıyor."},
 {"bag":"34:2 ↔ 34:24","kural":"okuma gözlemi (2×2 tablo)","not":"Yer/gök × giriş/çıkış (hücreler dolu) / biz-siz × hidayet-sapıklık (hücre ataması açık)."},
 {"bag":"34:9 ↔ 34:24","kural":"nakarat3 (min semâ ve ard, sûre içi)","not":"Gökten ve yerden: tehdit / rızık."},
 {"bag":"34:23 · 34:26 · 34:27","kural":"mühür (üç çift, art arda)","not":"alîy-kebîr · fettâh-alîm · azîz-hakîm."},
 {"bag":"34:3 · 34:7 · 34:29","kural":"okuma gözlemi","not":"Kâfirlerin üç sözü, üçü de âhiretin gerçekliği/zamanı üzerine."},
 {"bag":"34:3 ↔ 34:30","kural":"kök (سوع 2/2)","not":"es-sâ'a (kıyamet) / sâ'aten (bir an) — aynı kelime iki ölçek."},
 {"bag":"34:29 ↔ 10:48 · 21:38 · 27:71 · 36:48","kural":"esit2 TAM","not":"'Doğruysanız bu vaat ne zaman?' beş sûrede aynı."},
 {"bag":"34:28 → 34:36","kural":"nakarat3 (5 kelime, sûre içi)","not":"Fakat insanların çoğu bilmez — sûrede ikinci kez; 34:36 henüz okunmadı."},
 {"bag":"34:21 → 34:47","kural":"nakarat3 ('alâ kulli şey', sûre içi)","not":"Her şeyi koruyan / her şeye şahit — 34:47 henüz okunmadı."},
 # blok 31-40
 {"bag":"34:31 ↔ 34:33","kural":"nakarat3 (5 kelime, sûre içi)","not":"Zayıf düşürülenler büyüklenenlere dedi — diyalog ضعف → كبر → ضعف."},
 {"bag":"34:31 → 34:51","kural":"nakarat3 (lev terâ iz, sûre içi)","not":"'Bir görsen' sahnesi sûrede ikinci kez; 34:51 henüz okunmadı."},
 {"bag":"34:25 ↔ 34:32","kural":"kök (جرم 2/2)","not":"Suçu kendine yazmak (ecremnâ) / suçu karşıya yazmak (mücrimîn)."},
 {"bag":"34:18 ↔ 34:33","kural":"kök (ليل 2/2)","not":"Geceler ve günler güvenle yürüyün / gece ve gündüzün tuzağı."},
 {"bag":"34:17 ↔ 34:33","kural":"okuma gözlemi (soru-HASR + جزي)","not":"Biz nankörden başkasını mı cezalandırırız / yaptıklarından başkasıyla mı cezalandırılırlar."},
 {"bag":"34:7 ↔ 34:33","kural":"nakarat3 (ellezîne keferû hel, sûre içi)","not":"Kâfirler 'gösterelim mi' / kâfirlerin boyunlarına halkalar — 'hel' ile iki soru."},
 {"bag":"34:18 ↔ 34:34","kural":"kök (قري 3/3)","not":"Bereketlendirilmiş kasabalar / müterefleri inkâr eden kasaba."},
 {"bag":"34:35 → 34:36 → 34:37","kural":"kök (كثر, مول 2/2, ولد 2/2)","not":"Daha çoğuz / insanların çoğu bilmez / mal ve evlat yaklaştırmaz."},
 {"bag":"34:31-33 → 34:37","kural":"kök (ضعف 4/4)","not":"Zayıf düşürülmek ×3 / kat kat karşılık — aynı kök zayıflık ve katlanma."},
 {"bag":"34:18 ↔ 34:37","kural":"lemma (âmin)","not":"Yolda güvende / köşklerde güvende."},
 {"bag":"34:4-5 ↔ 34:37-38","kural":"nakarat3 (34:5↔34:38, 6 kelime) + okuma gözlemi (ayna çifti)","not":"İman+amel → ödül / âyetleri boşa çıkarma → azap; sûrede iki kez."},
 {"bag":"34:36 ↔ 34:39","kural":"nakarat3 (7 kelime, sûre içi)","not":"Rızık kuralı iki kez; ikincide 'kullarından', 'ona' ve harcananın yerine konması ekleniyor."},
 {"bag":"34:9 ↔ 34:39","kural":"kök (خلف 2/2)","not":"Arkalarındaki / yerine koyar."},
 {"bag":"34:11 · 34:18 · 34:36 · 34:39","kural":"kök (قدر 5/5)","not":"Zırhın ölçüsü / yolun ölçüsü / rızkın daraltılması ×2 — bir kök, üç anlam."},
 {"bag":"34:26 ↔ 34:40","kural":"kök (جمع 2/2)","not":"Rabbimiz aramızı toplar / hepsini toplayacağı gün."},
 # blok 41-50
 {"bag":"34:40 → 34:41","kural":"okuma gözlemi (soru-cevap)","not":"Meleklere soru: bunlar size mi taptı / cevap: hayır, cinlere."},
 {"bag":"34:8 · 34:12 · 34:14 · 34:15-16 · 34:41 · 34:46","kural":"kök (جنن 8/8)","not":"Tek kök üç anlam: cinnet, cin, bahçe."},
 {"bag":"34:8 → 34:46","kural":"kök (جنن) + okuma gözlemi","not":"'Onda cinnet mi var?' sorusu 38 ayet sonra cevaplanıyor: 'arkadaşınızda cinnet yok'."},
 {"bag":"34:31 ↔ 34:42","kural":"kök (بعض 4/4)","not":"Birbirlerine söz çevirmek / birbirinize fayda-zarar yok."},
 {"bag":"34:12 ↔ 34:42","kural":"kök (ذوق 2/2)","not":"Sapan cinlere azap tattırırız / zalimlere 'tadın'."},
 {"bag":"32:20 ↔ 34:42","kural":"xref (ateşin azabını tadın, yalanladığınız)","not":"Aynı hüküm iki sûrede."},
 {"bag":"34:7 ↔ 34:43","kural":"aktör (adsız racül)","not":"Peygamber iki kez adıyla değil 'bir adam' diye anılıyor."},
 {"bag":"34:8 ↔ 34:43","kural":"kök (فري 2/2)","not":"'Yalan mı uydurdu?' sorusu / 'uydurulmuş yalan' iddiası."},
 {"bag":"34:3 ↔ 34:44","kural":"kök (كتب 2/2)","not":"Her şeyi içeren apaçık kitap / onlara verilmemiş kitaplar."},
 {"bag":"34:25 ↔ 34:47","kural":"kök (سأل 3/3)","not":"Sorulmazsınız, sorulmayız / sizden istemedim."},
 {"bag":"34:21 ↔ 34:47","kural":"nakarat3 ('alâ kulli şey', sûre içi) — DOĞRULANDI","not":"Rab her şeyi koruyan (hafîz) / Allah her şeye şahit (şehîd)."},
 {"bag":"34:3 · 34:14 · 34:48","kural":"kök (غيب 3/4)","not":"Gaybın bilicisi (tekil) / gaybı bilmeyen cinler / gaybları çok bilen (çoğul)."},
 {"bag":"34:48 → 34:53","kural":"kök (قذف 1-2/2)","not":"Rab hakkı fırlatır / 34:53 henüz okunmadı."},
 {"bag":"21:18 ↔ 34:48","kural":"okuma gözlemi (قذف + hak)","not":"Hakkı bâtılın üstüne fırlatmak — iki sûrede."},
 {"bag":"34:36 · 34:39 · 34:48","kural":"nakarat3 ('qul inne Rabbî', sûre içi, 3 ayet)","not":"Rızık ×2 ve hakkın fırlatılması aynı açılışla."},
 {"bag":"17:81 ↔ 34:49","kural":"xref (hak geldi)","not":"Bâtıl yok oldu / bâtıl ne başlatır ne tekrarlar."},
 {"bag":"34:25 ↔ 34:50","kural":"okuma gözlemi (asimetri)","not":"Bizim suçumuz-sizin amelimiz / sapmam bana, hidayetim Rabbimin vahyinden."},
 # blok 51-54
 {"bag":"34:31 ↔ 34:51","kural":"nakarat3 (lev terâ iz, sûre içi) — DOĞRULANDI","not":"Rab katında durdurulmuşlar / korkuya kapılmışlar."},
 {"bag":"34:23 ↔ 34:51","kural":"kök (فزع 2/2)","not":"Kalplerden korku giderilir / korkuya kapılırlar."},
 {"bag":"34:50 ↔ 34:51","kural":"lemma (karîb)","not":"Rab yakındır (esmâ, geçerli) / yakın bir yerden yakalanırlar (mekân, değil)."},
 {"bag":"34:48 ↔ 34:53","kural":"kök (قذف 2/2) — DOĞRULANDI","not":"Rab hakkı fırlatır / onlar gayba taş atar — aynı fiil, ters yön."},
 {"bag":"34:3 · 34:14 · 34:48 · 34:53","kural":"kök (غيب 4/4)","not":"Gaybın bilicisi / gaybı bilmeyen cinler / gaybları çok bilen / gayba atış."},
 {"bag":"34:51 · 34:52 · 34:53","kural":"nakarat3 (min mekânin ba'îd, 52-53) + okuma gözlemi","not":"Üç ayet 'yer' ile bitiyor: yakın · uzak · uzak."},
 {"bag":"34:18 · 34:19 · 34:54","kural":"kök (بين 16/16)","not":"Aralarına kasabalar / aramızı uzaklaştır / aralarına engel."},
 {"bag":"34:21 ↔ 34:54","kural":"kök (شكك 2/2)","not":"Şüphede olanı ayırmak / kuşku verici şüphe — sûrenin son kelimesi."},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AS_sebe', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in SEBE]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AS_sebe'] = SEBE
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AS_sebe', len(SEBE), '(%d-%d) | toplam aday' % (nos[0], nos[-1]), tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AN_sebe', len(BAGLAR['AN_sebe']))
