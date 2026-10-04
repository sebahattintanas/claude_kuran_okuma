# -*- coding: utf-8 -*-
"""aday_ekle_35_fatir.py — sûre 35 (Fâtır) adayları (AT_fatir) ve okuma bağları (AO_fatir).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1007'den); betik sıranın kopmadığını doğrular.
"""
import json

FATIR = [
# ---------------- blok 1-10 ----------------
{"no":1007,
 "aday":"HAMD AÇILIŞI ARDIŞIK ÇİFT — ilk kelimesi hamd kökü olan sûreler korpusta dört (6, 18, 34, 35); ardışık olan tek çift 34-35.",
 "olculen":{"sureler":[6,18,34,35],"ardisik":"34-35","yontem":"morph.txt, her sûrenin 1. ayet 1. kelimesinin kökü (TAM SAYIM); Fâtiha'da hamd 1:2'de, sayılmadı"},
 "durum":"KAYIT","oncelik":"-","kaynak":"sûre 35 okuması, blok 1-10","etiket":"gözlem — TAM SAYIM, yorum yok",
 "test_notu":"Dört sûrenin dizilişi hakkında 'neden' iddiası kurulmadı; mushaf sırası ile tertip arasında bağ aranırsa KAPATILAMAZ (tek dizilim, boş model yok)."},
{"no":1008,
 "aday":"SAY ALANI DOĞRU POZİTİF — 35:1 mesnâ · sülâs · rubâ' üçü de yakalandı. Üçlü korpusta yalnız 4:3 ve 35:1'de; mesnâ ayrıca 34:46'da.",
 "olculen":{"35:1":["mesnâ","sülâs","rubâ'"],"uclu_ayet":["4:3","35:1"],"mesna_ayet":["4:3","34:46","35:1"]},
 "durum":"KAYIT","oncelik":"-","kaynak":"sûre 35 okuması, blok 1-10","etiket":"981/1004/1005 say alanı — doğru pozitif girdisi",
 "test_notu":"981 ailesinin yanlış pozitif/negatif sayımına karşı kolon: dağıtıcı sayı sıfatları (fu'âl/mef'al) doğru yakalanıyor. furâdâ (34:46) hâlâ yanlış negatif."},
{"no":1009,
 "aday":"★★★ KAYNAĞI EDİLGEN — 35:4 (11 kelime, 3 fiilin 2'si edilgen) ★★★ tek kaynak pas z=3,48; hapaks değil, uzunluk değil.",
 "olculen":{"ayet":"35:4","z2":{"pas":3.48,"n":-0.15,"allah":1.29},"yildiz2":3},
 "durum":"KAYIT","oncelik":"P1","kaynak":"sûre 35 okuması, blok 1-10","etiket":"983 birikimi — ★★★ otomatik kaynak dağılımı",
 "test_notu":"983: sûre 34'te ★★★ 4/4 hapakstan. Burada kısa ayette iki edilgen z'yi uca taşıyor; pas z'nin fiil sayısına duyarlılığı (2/3 küçük payda) ★★★'ı şişiriyor olabilir — KAPATILAMAZ, tur sonunda pas kaynaklı ★★★'ların fiil sayısı dağılımı TAM SAYIMLA."},
{"no":1010,
 "aday":"ÇIPA MERDİVENİ — AYNI OLGU, ÜÇ KADEME: rüzgâr → bulut → yağmur/dirilme 30:24'te L2 (iki aşama), 30:48'de L4 (ara durumlar adlı), 35:9'da L2 (ara durum yalnız bulut). Kademe olgunun değil anlatımın ayrıntısını ölçüyor.",
 "olculen":{"30:24":"L2","30:48":"L4 (mekanizma kolu)","35:9":"L2","olcut":"ara durumların adlandırılması (bulut, parça, yağmur, çıkış yeri)"},
 "durum":"ACIK","oncelik":"P2","kaynak":"sûre 35 okuması, blok 1-10","etiket":"965 ailesi (çıpa merdiveni tanımı) — gözlem, tanım değişikliği değil",
 "test_notu":"Tanım değiştirilmedi. Çıpa/olgu ilişkisi analiz edilirken birim 'ayet' olduğu için aynı olgu farklı kademelerle birden çok kez sayılıyor; olgu kümesi ayrıca tutulmalı mı sorusu tur sonuna."},
# ---------------- blok 11-20 ----------------
{"no":1011,
 "aday":"İKİ AYETLİK TEKRAR — 35:16-17 = 14:19'un son cümlesi + 14:20'nin tamamı, aynı sırayla. esit2 yalnız 35:17'yi (14:20, TAM 1,0000) yakalıyor; 35:16 yalnız xref'te (üç üçlü → 14:19).",
 "olculen":{"35:16":"xref 3/3 → 14:19 (son cümle)","35:17":"esit2 → 14:20 oran 1,0000 TAM","ardisik":"14:19-20 ↔ 35:16-17"},
 "durum":"KAYIT","oncelik":"P2","kaynak":"sûre 35 okuması, blok 11-20","etiket":"bağ alanları ayet birimli: ardışık ayet bloğu tekrarı tek alanda görünmüyor",
 "test_notu":"Araç açığı değil, birim seçimi sonucu. Tur sonunda: esit2/xref ile ardışık iki ayeti aynı ardışık çifte bağlayan kaç blok var — TAM SAYIM. Okurken bulunan örnek kanıt değil."},
{"no":1012,
 "aday":"★★★ KISA AYET LAFIZ ŞİŞMESİ (983 ailesi) — 35:15 (10 kelime, 2 lafız) ve 35:17 (5 kelime, 1 lafız) aynı allah z=3,47 ile ★★★; z lafız/kelime oranından geliyor, iki ayette oran aynı (0,2).",
 "olculen":{"35:15":{"n":10,"lafiz":2,"allah_z":3.47,"yildiz2":3},"35:17":{"n":5,"lafiz":1,"allah_z":3.47,"yildiz2":3}},
 "durum":"ACIK","oncelik":"P1","kaynak":"sûre 35 okuması, blok 11-20","etiket":"983 — ★★★ otomatik kaynak; uzunluk karıştırıcısı (827/837 ailesinin ters yönü)",
 "test_notu":"Onarılmadı (dondurma). 827/837'de uzun ayette lafız seyreliyordu; burada kısa ayette tek lafız uca çıkıyor. KAPATILAMAZ — tur sonunda allah-kaynaklı ★★★'ların n dağılımı TAM SAYIMLA."},
{"no":1013,
 "aday":"TARAYICI v4 TERKİP DUYARSIZLIĞI (948 ailesi) — 31:29 ve 35:13 aynı dört kök (ولج ليل نهر سخر, korpusta yalnız bu iki ayette) ve aynı kademe (L1); tarayıcı 31:29'da aday verdi (G_bakış: 'e lem tera'), 35:13'te vermedi.",
 "olculen":{"31:29":"aday, G_bakış, L1","35:13":"aday değil, L1","ortak_kok":4},
 "durum":"ACIK","oncelik":"P0","kaynak":"sûre 35 okuması, blok 11-20","etiket":"948 tarayıcı kesinlik/duyarlılık — olgu değil işaret kelimesi tetikliyor",
 "test_notu":"Kesinlik birikimine (0/19) ek olarak duyarlılık tarafı: tetik, olgunun kendisine değil çerçeve kelimesine bağlı. Onarılmadı."},
# ---------------- blok 21-30 ----------------
{"no":1014,
 "aday":"ÇIPA L4 SINIFLAMA KOLU — ÖLÇÜT İKİ EMSALDE FARKLI İFADE EDİLMİŞ: 30:22 'sınıflar adlandırılmıyor → L1', 29:40 'türler ayrı adlandırılıp ayrı gruplara eşlendi → L4'. 35:27'de sınıflar ADLI (beyaz, kırmızı, siyah) ama üye eşlemesi yok; 35:12'de iki sınıf adlı ve nitelikli, eşleme yok. İkisi de eşleme ölçütüyle L4 dışında tutuldu.",
 "olculen":{"30:22":"L1 (sınıf adı yok)","29:40":"L4 (adlandırma + eşleme)","35:12":"L1 (adlı, eşleme yok)","35:27":"L2 (nedensellik; sınıflar adlı, eşleme yok)"},
 "durum":"ACIK","oncelik":"P1","kaynak":"sûre 35 okuması, blok 21-30","etiket":"965 ailesi (çıpa merdiveni tanımı) — tanım DEĞİŞTİRİLMEDİ",
 "test_notu":"Okuma sırasında sabit ölçüt: eşleme (29:40). Kendi kaydım düştü: 35:12 gerekçesi 'ölçütsüz, 27:61 emsali' yanlıştı → DUZELTME (kademe aynı). Tam okuma sonunda 'adlı sınıf, eşlemesiz' ayetler ayrı sayılmalı; eşik analizinde iki okuma da raporlanmalı (duyarlılık)."},
{"no":1015,
 "aday":"GLOSS TARAMASI GİRDİLERİ (987/1000) — sûre 35'te okunan anlamı taşımayan gloss'lar: ملك (melek, 35:1), عذب (tatlı su, 35:12), ظلم (karanlık, 35:20; zulumât 23 ayet), ظلل (gölge, 35:21; BASKIN lemma zıll 14 — gloss azınlık anlamını veriyor), جدد (çizgi/yol, 35:27).",
 "olculen":{"ظلل":{"zıll":14,"zalle":9,"zulle":6},"ظلم":{"zulumât":23},"kaynak":"kok_envanteri.json lemmalar"},
 "durum":"ACIK","oncelik":"P1","kaynak":"sûre 35 okuması, blok 1-30","etiket":"987/1000 — gloss baskın lemmayı karşılamıyor",
 "test_notu":"Onarılmadı (araç dondurma; gloss yazımı yalnız yeni kökte). ظلل en ağır vaka: baskın lemma gloss'ta hiç yok. Tur sonu tarama: her kökün gloss'u baskın lemmayı içeriyor mu — TAM SAYIM.",
 "ek":{"blok 31-40":"ذهب 'gitme, götürme' — 35:33 zeheb (altın, lemma 8) gloss'ta yok"}},
# ---------------- blok 31-40 ----------------
{"no":1016,
 "aday":"KÖK YOĞUNLUĞU TEPESİ — 35:39'da كفر kökü 6 token (24 kelime); korpusta bu kökün bir ayette geçtiği en yüksek sayı. Sonraki 3 (2:89, 2:102, 4:137, 9:37).",
 "olculen":{"35:39":6,"sonraki":3,"ayetler_3":["2:89","2:102","4:137","9:37"],"yontem":"morph.txt ROOT:كفر token sayımı, ayet başına (TAM SAYIM)"},
 "durum":"KAYIT","oncelik":"-","kaynak":"sûre 35 okuması, blok 31-40","etiket":"gözlem — TAM SAYIM; kök ikilemesi alanının uç değeri",
 "test_notu":"Okurken görüldü, sonra sayıldı. Ayet içi kök tekrarının korpus dağılımı (her kök için ayet-başı tepe) ölçülmeden 'olağanüstü' denemez — bu yalnız bir kökün tepesi. KAPATILAMAZ değil: tur sonunda tüm kökler için tepe dağılımı TAM SAYIMLA."},
{"no":1017,
 "aday":"ŞAHIS SAYIMI KONUŞMACIYI AYIRMIYOR — 35:37'de 'biz' (1P 7) iki konuşmacıya ait: cehennem ehlinin alıntılanan sözü ('Rabbimiz, bizi çıkar') ve Allah'ın cevabı ('sizi yaşatmadık mı'). sahset/baskın tek havuzda sayıyor; ayrıca 35:34-35'te cennet ehlinin 'biz'i.",
 "olculen":{"35:37":{"1P":7,"konusmaci":["cehennem ehli (alıntı)","Allah"]},"35:34-35":"1P cennet ehli (alıntı)"},
 "durum":"ACIK","oncelik":"P2","kaynak":"sûre 35 okuması, blok 31-40","etiket":"sah/sahset/ilt alanları — alıntı sınırı yok (517 ile komşu)",
 "test_notu":"Araç açığı, metin hakkında kanıt değil (aday 924). Onarılmadı. İltifât ve baskın şahıs alanları alıntı içeren ayetlerde karışık; analizde alıntılı ayetler ayrı raporlanmalı."},
# ---------------- blok 41-45 ----------------
{"no":1018,
 "aday":"FÂSILA SINIFI GEÇİŞİ SÛRE SONUNDA — 35:39-45 yedi ayet kesintisiz ا sınıfı (hasârâ, ğurûrâ, ğafûrâ, nufûrâ, tahvîlâ, qadîrâ, basîrâ); 35:1-38'de ا fâsıla yok. kafiye_kirik alanı bu yedi ayetin hiçbirini işaretlemiyor; sûrede kırık sayılanlar 35:8 (ن), 35:12 (ن), 35:27 (د), 35:35 (ب).",
 "olculen":{"A_sinifi":["35:39","35:40","35:41","35:42","35:43","35:44","35:45"],"A_oncesi":0,"kafiye_kirik":["35:8","35:12","35:27","35:35"],"kaynak":"ölçüm satırı fâsıla alanı, 45/45"},
 "durum":"KAYIT","oncelik":"P2","kaynak":"sûre 35 okuması, blok 41-45","etiket":"kafiye alanı tanımı — kırık komşu-göreli; blok geçişi ile tekil kırık ayrımı yok",
 "test_notu":"Araç açığı değil, tanım sonucu: sürekli yeni sınıfa geçiş 'kırık' sayılmıyor, tek ayetlik sapma sayılıyor. Sûre sonu fâsıla geçişinin korpus sıklığı ölçülmedi — KAPATILAMAZ değil, tur sonunda sûre-son-blok fâsıla sınıfı dağılımı TAM SAYIMLA."},
]

BAGLAR = {"AO_fatir": [
 # blok 1-10
 {"bag":"34:1 ↔ 35:1","kural":"kök (حمد, ilk kelime; TAM SAYIM 4 sûre)","not":"Hamdla açılan iki ardışık sûre; ötekiler 6 ve 18."},
 {"bag":"4:3 ↔ 35:1","kural":"xref + lemma (mesnâ, sülâs, rubâ' — üçlü yalnız bu iki ayette)","not":"Aynı sayı dizisi: nikâh sayısı / meleklerin kanatları."},
 {"bag":"34:46 ↔ 35:1","kural":"lemma (mesnâ, 3 ayet)","not":"İkişer ve teker teker kalkın / ikişer, üçer, dörder kanat — bitişik iki sûrede."},
 {"bag":"35:1 · 35:2 · 35:4 · 35:9","kural":"kök (رسل 1-4/6)","not":"Bir kök dört gönderge: melek elçiler, rahmetin salıverilmesi, peygamber elçiler, rüzgârların gönderilmesi."},
 {"bag":"35:1 → 35:3","kural":"kök (خلق 1-2/5)","not":"Yaratmada artırma / Allah'tan başka yaratıcı var mı."},
 {"bag":"35:3 ↔ 35:5","kural":"okuma gözlemi (nidâ 'ey insanlar', iki ayet arayla)","not":"Nimeti anın / vaat gerçektir — iki nidâ."},
 {"bag":"31:33 ↔ 35:5","kural":"xref (beş üçlü) + lemma (ğarûr 3 ayet)","not":"Dünya hayatı aldatmasın, aldatıcı Allah hakkında aldatmasın — iki sûrede aynı cümle."},
 {"bag":"35:5 → 35:6","kural":"okuma gözlemi","not":"Adsız aldatıcı → adıyla şeytan; ölçüm bu bağı kurmuyor."},
 {"bag":"35:4 → 35:25","kural":"nakarat3 ('in kezzebe fe-qad kezzebe', sûre içi)","not":"Yalanlanmanın teselli kalıbı; 35:25 henüz okunmadı."},
 {"bag":"35:7 → 35:36","kural":"nakarat3 ('ellezîne keferû lehüm', sûre içi)","not":"35:36 henüz okunmadı."},
 {"bag":"35:7 ↔ 35:10","kural":"nakarat3 ('lehüm azâbün şedîd', sûre içi; kalıp ayrıca 42:16, 42:26)","not":"İnkâr edenler / kötülük tuzağı kuranlar — aynı ceza cümlesi."},
 {"bag":"34:4-5 ↔ 35:7","kural":"okuma gözlemi (ayna çifti)","not":"Aynı ayna iki ayette / tek ayette."},
 {"bag":"9:37 · 35:8 · 40:37 · 47:14","kural":"kök (زين + سوأ + عمل, TAM SAYIM 4 ayet)","not":"Kötü amelin süslenmesi."},
 {"bag":"30:24 · 30:48 ↔ 35:9","kural":"xref (30:48, üç üçlü) + çıpa kademesi","not":"Aynı olgu: iki aşama L2 / beş aşama L4 / dört aşama L2."},
 {"bag":"35:2 ↔ 35:10","kural":"kök (عزز 1-3/5)","not":"Azîz mührü / izzetin tamamı Allah'ın."},
 # blok 11-20
 {"bag":"35:11 ↔ 35:17","kural":"nakarat3 ('zâlike ale'llâh', sûre içi) — DOĞRULANDI","not":"Bu Allah'a kolay (yesîr) / bu Allah'a güç değil (bi-azîz) — aynı çerçeve, olumlu ve olumsuz."},
 {"bag":"35:11 ↔ 41:47 · 22:70","kural":"xref","not":"Dişinin gebeliği ve doğumu O'nun bilgisiyle / kitapta, Allah'a kolay."},
 {"bag":"35:12 ↔ 16:14","kural":"xref (dokuz üçlü)","not":"Taze et, süs, suyu yaran gemiler, lütfu aramak."},
 {"bag":"25:53 ↔ 35:12","kural":"kök (بحر + عذب + ملح, TAM SAYIM 2 ayet)","not":"İki deniz: arada engel / farklı ama aynı ürünler."},
 {"bag":"35:7 · 35:10 · 35:12","kural":"kök (عذب 1-3/4)","not":"Azap, azap, tatlı su — tek kök iki anlam."},
 {"bag":"31:29 ↔ 35:13","kural":"kök (ولج + ليل + نهر + سخر, TAM SAYIM 2 ayet) + xref","not":"Aynı terkip, aynı kademe (L1); tarayıcı yalnız 31:29'da (aday 1013)."},
 {"bag":"35:13 → 35:40","kural":"nakarat3 ('ellezîne ted'ûne min dûnih', sûre içi)","not":"35:40 henüz okunmadı."},
 {"bag":"34:3 · 34:22 ↔ 35:13","kural":"okuma gözlemi (en küçük birim ölçeği)","not":"Zerre ağırlığı (bilgi, mülk) / kıtmîr (sahiplik)."},
 {"bag":"35:13 → 35:14","kural":"kök (دعو 2-4/6)","not":"Çağırdıklarınız kıtmîre sahip değil / çağırsanız işitmezler."},
 {"bag":"35:3 · 35:5 · 35:15","kural":"kök (أيي 3/3, üçü de nidâ)","not":"Sûrenin üç 'ey insanlar'ı; 'âyet' kelimesi sûrede yok."},
 {"bag":"35:1 → 35:15","kural":"kök (حمد 1-2/3)","not":"Hamd açılışı / ganî-hamîd mührü."},
 {"bag":"35:15 ↔ 47:38 · 3:181","kural":"lemma (fakîr + ganî)","not":"Siz fukarâ, Allah ganî (35:15, 47:38) / ters yönde iddia (3:181)."},
 {"bag":"35:16-17 ↔ 14:19-20","kural":"xref (14:19) + esit2 TAM (14:20)","not":"İki ardışık ayet aynı sırayla (aday 1011)."},
 {"bag":"35:18 ↔ 6:164 · 17:15 · 39:7 · 53:38","kural":"lemma (vâzira, TAM SAYIM 5 ayet)","not":"Hiçbir yük taşıyan başkasının yükünü taşımaz."},
 {"bag":"35:12 → 35:19","kural":"kök (سوي 1-2/3)","not":"İki deniz bir değil / kör ile gören bir değil."},
 {"bag":"13:16 ↔ 35:19-20","kural":"kök (عمي + بصر + سوي; ظلم + نور + سوي yalnız 13:16)","not":"Kör/gören ve karanlık/ışık: tek ayette / iki ayete bölünmüş."},
 {"bag":"34:6 ↔ 35:14","kural":"esmâ sınır vakası (aday 999)","not":"Tamlama içinde ad olarak esmâ: sırâtı'l-azîzi'l-hamîd / mislu habîr."},
 # blok 21-30
 {"bag":"35:19 · 35:20 · 35:21 · 35:22","kural":"okuma gözlemi (dört eşitsizlik çifti) + kök (سوي 2-3/3)","not":"Kör/gören, karanlık/ışık, gölge/sıcak, diri/ölü; ilk ikisi 13:16'da tek ayette."},
 {"bag":"16:81 ↔ 35:21","kural":"kök (ظلل + حرر, TAM SAYIM 2 ayet)","not":"Gölge ve sıcak."},
 {"bag":"45:21 ↔ 35:22","kural":"kök (حيي + موت + سوي, TAM SAYIM 2 ayet)","not":"Diriler ve ölüler bir olmaz."},
 {"bag":"35:14 → 35:22","kural":"kök (سمع 1-4/4)","not":"Çağrılanlar işitmez / Allah işittirir, sen işittiremezsin."},
 {"bag":"35:23 ↔ 35:24","kural":"okuma gözlemi (fâsıla nezîr ardışık) + kök (نذر 2-4/7)","not":"Sen ancak uyarıcısın / her ümmete bir uyarıcı."},
 {"bag":"35:4 ↔ 35:25","kural":"nakarat3 ('in kezzebe fe-qad kezzebe', sûre içi) — DOĞRULANDI","not":"Elçiler yalanlandı (edilgen) / öncekiler yalanladı (etken)."},
 {"bag":"3:184 ↔ 35:25","kural":"xref + kök (زبر + بين + نور, 3 ayet)","not":"Beyyinât, zübür, kitâb münîr — aynı üçlü."},
 {"bag":"35:25 → 35:44","kural":"nakarat3 ('ellezîne min qablihim', sûre içi)","not":"35:44 henüz okunmadı."},
 {"bag":"34:45 ↔ 35:26","kural":"kalıp (keyfe kâne nekîr, TAM SAYIM 4 ayet: 22:44, 34:45, 35:26, 67:18; lemma 5, 42:47 başka kalıp)","not":"Fe-keyfe kâne nekîr — bitişik iki sûrede."},
 {"bag":"35:24 → 35:26","kural":"okuma gözlemi (sahset 1P → 1S)","not":"Biz gönderdik / ben yakaladım."},
 {"bag":"35:9 ↔ 35:27","kural":"okuma gözlemi (lafız → 1P iltifâtı, ilt=0; 517 ailesi)","not":"Gökten su / ölü belde — iki ayette aynı fail geçişi."},
 {"bag":"35:27 · 35:28 ↔ 16:13 · 16:69 · 30:22 · 39:21","kural":"kök (خلف + لون, TAM SAYIM 6 ayet)","not":"Renkleri farklı; sûrede üç alan (ürün, dağ, canlı)."},
 {"bag":"35:16 → 35:27","kural":"kök (جدد 1-2/2)","not":"Yeni halk / dağdaki çizgiler — tek kök, iki anlam."},
 {"bag":"35:18 → 35:28","kural":"kök (خشي 1-2/2)","not":"Rablerinden korkanlar / Allah'tan korkan âlimler."},
 {"bag":"35:2 · 35:10 · 35:17 · 35:28","kural":"kök (عزز 1-5/5)","not":"Azîz, izzet ×2, 'güç değil', azîz — kök kapandı."},
 {"bag":"35:10 ↔ 35:29","kural":"kök (بور 1-2/2) — AYNA","not":"Tuzakları boşa çıkar / boşa çıkmayacak ticaret."},
 {"bag":"35:18 ↔ 35:29","kural":"kök (صلو 1-2/2)","not":"'Namazı dosdoğru kıldılar' iki ayette."},
 {"bag":"2:274 · 13:22 · 14:31 ↔ 35:29","kural":"kök (سرر + علن + نفق, TAM SAYIM 4 ayet) + xref","not":"Gizli ve açık harcama."},
 {"bag":"35:7 → 35:30","kural":"kök (أجر 1-2/2)","not":"Büyük ödül / ödüllerini tam verme."},
 {"bag":"35:12 ↔ 35:30","kural":"kök (شكر 1-2/3)","not":"Şükredesiniz diye (insan) / şekûr (Allah)."},
 # blok 31-40
 {"bag":"35:19 ↔ 35:31","kural":"lemma (basîr) + esmâ el kararı","not":"Aynı kelime: gören insan (değil) / Allah (ilâhî)."},
 {"bag":"35:14 → 35:31","kural":"kök (خبر 1-2/2)","not":"Mislu habîr / le-habîrun basîr."},
 {"bag":"17:17 · 17:30 · 17:96 · 42:27 ↔ 35:31","kural":"kök (عبد + خبر + بصر, TAM SAYIM 5 ayet) + xref","not":"Kullarından haberdar, gören."},
 {"bag":"29:40 · 27:17 ↔ 35:32","kural":"çıpa tanımı (aday 1014 sınaması)","not":"Üç adlı sınıf + bölüntü: eşleme ölçütü dolu, olgu değil."},
 {"bag":"35:7 ↔ 35:32","kural":"kök (كبر 1-2/3) + esmâ yanlış mühür","not":"Ecrun kebîr / el-fadlu'l-kebîr — aynı kalıp, iki yanlış mühür."},
 {"bag":"35:12 → 35:33","kural":"kök (حلي 1-2/2, لبس 1-2/2)","not":"Denizden süs çıkarırsınız / cennette süslenirler, giysileri."},
 {"bag":"35:21 → 35:33","kural":"kök (حرر 1-2/2)","not":"Sıcak (harûr) / ipek (harîr)."},
 {"bag":"22:23 · 18:31 ↔ 35:33","kural":"xref (dört üçlü 22:23)","not":"Altın bilezik, inci, ipek."},
 {"bag":"35:1 · 35:15 · 35:34","kural":"kök (حمد 1-3/3)","not":"Hamd açılışı / hamîd mührü / cennet ehlinin hamdı."},
 {"bag":"35:30 ↔ 35:34","kural":"esmâ çifti (ğafûr-şekûr) ×2","not":"Aynı mühür çifti dört ayet arayla; شكر 3/3 kapanıyor."},
 {"bag":"35:35 ↔ 35:36","kural":"okuma gözlemi (NEG 2 / NEG 2) — AYNA","not":"Cennette yorgunluk dokunmaz ×2 / cehennemde ölüm yok, hafifleme yok."},
 {"bag":"35:7 ↔ 35:36","kural":"nakarat3 ('ellezîne keferû lehüm', sûre içi) — DOĞRULANDI","not":"Çetin azap / cehennem ateşi."},
 {"bag":"35:20 · 35:25 · 35:36","kural":"kök (نور 1-3/3)","not":"Işık / aydınlatıcı kitap / ateş."},
 {"bag":"35:34 ↔ 35:37","kural":"okuma gözlemi (iki 'Rabbimiz' sözü) — AYNA","not":"Cennet ehli hamd eder / cehennem ehli çığlık atar."},
 {"bag":"35:11 → 35:37","kural":"kök (عمر 1-4/4)","not":"Ömrü uzatılan/eksiltilen / sizi yaşatmadık mı."},
 {"bag":"35:18 → 35:38","kural":"kök (غيب 1-2/2)","not":"Gaybda korkanlar / göklerin ve yerin gaybı."},
 {"bag":"35:27 · 35:28 → 35:39","kural":"kök (خلف 1-4/4)","not":"Renkleri farklı ×3 / halifeler."},
 {"bag":"35:13 ↔ 35:40","kural":"nakarat3 ('ellezîne ted'ûne min dûnih', sûre içi) — DOĞRULANDI","not":"Kıtmîre sahip değiller / ne yarattılar."},
 {"bag":"35:3 ↔ 35:40","kural":"okuma gözlemi (yaratıcı sorusu)","not":"Allah'tan başka yaratıcı var mı / ortaklar yerden ne yarattı."},
 {"bag":"35:5 ↔ 35:40","kural":"kök (وعد 1-2/2 + غرر 1-4/4) — AYNA","not":"Allah'ın vaadi hak, aldatıcı aldatmasın / zalimlerin vaadi aldatmaca."},
 # blok 41-45
 {"bag":"35:2 ↔ 35:41","kural":"kök (مسك 1-4/4, iki ayette ikişer)","not":"Rahmeti tutma / gökleri ve yeri tutma."},
 {"bag":"17:44 ↔ 35:41","kural":"xref (kâne halîmen ğafûrâ)","not":"Aynı mühür kalıbı."},
 {"bag":"35:24 → 35:42","kural":"kök (أمم 1-2/2, نذر)","not":"Her ümmete bir uyarıcı / ümmetlerin herhangi birinden daha doğru olacaklardı."},
 {"bag":"35:1 · 35:30 · 35:39 · 35:42","kural":"kök (زيد 1-5/5)","not":"Allah artırır (yaratma, lütuf) / inkâra karşı ancak gazap, ziyan, nefret artar."},
 {"bag":"35:10 ↔ 35:43","kural":"kök (مكر 1-4/4 + سوأ) — iki ayette ikişer","not":"Tuzakları boşa çıkar / kötü tuzak ancak sahibini kuşatır."},
 {"bag":"33:62 · 48:23 ↔ 35:43","kural":"xref","not":"Allah'ın sünnetinde değişme bulamazsın."},
 {"bag":"35:25 ↔ 35:44","kural":"nakarat3 ('ellezîne min qablihim', sûre içi) — DOĞRULANDI","not":"Öncekiler yalanladı / öncekilerin sonu."},
 {"bag":"35:26 ↔ 35:44","kural":"kök (كيف 1-2/2)","not":"İnkârım nasıl oldu / sonları nasıl oldu."},
 {"bag":"35:1 ↔ 35:44","kural":"kök (قدر 1-2/2 + شيأ 1-8/8) + esmâ qadîr","not":"Her şeye gücü yeten / hiçbir şey âciz bırakamaz, gücü yeten — ilk ayet ve sondan ikinci."},
 {"bag":"16:61 ↔ 35:45","kural":"xref (beş üçlü) + lemma hizası 22/32","not":"Neredeyse aynı ayet; farklar: zulüm/kazanç, üzerinde/sırtında, kapanış."},
 {"bag":"35:13 ↔ 35:45","kural":"kök (أجل 1-3/3, ecel müsemmâ)","not":"Güneş ve ay belirli süreye akar / insanlar belirli süreye ertelenir."},
 {"bag":"35:31 ↔ 35:45","kural":"kalıp (bi-ibâdihî … basîr) + kök (بصر 2-3/3)","not":"Kullarından haberdar, gören / kullarını görendir."},
 {"bag":"35:39 → 35:45","kural":"fâsıla sınıfı (ا, yedi ayet; aday 1018)","not":"Sûrenin son yedi ayeti kesintisiz ا."},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AT_fatir', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in FATIR]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AT_fatir'] = FATIR
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AT_fatir', len(FATIR), '(%d-%d) | toplam aday' % (nos[0], nos[-1]), tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AO_fatir', len(BAGLAR['AO_fatir']))
