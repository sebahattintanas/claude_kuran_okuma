# -*- coding: utf-8 -*-
"""aday_ekle_aralik.py — LAFIZDAN LAFZA ARALIK OKUMASI adayları (set X_aralik), 2026-10-05 ayrı oturum.
Sûre okumasının DIŞINDA, ayrı bir sohbette yapıldı; sayımlar betikler/aralik_olcum.py → ciktilar/aralik_olcum.json.
Set adı sûre dizisinin dışında seçildi (X), çünkü AV_saffat sûre 37'ye ayrılmış. Numaralar havuz sonundan (1023'ten);
BU SET YÜKLENDİKTEN SONRA sûre 37 adayları 1037'den başlar (aday_ekle_37_saffat.py sırayı kendisi doğrular).
İdempotent: set bütünüyle yeniden yazılır. Depo kökünden koşulur."""
import json
ORT = {"kaynak": "aralık okuması 2026-10-05 (ayrı oturum)", "olcum_betigi": "betikler/aralik_olcum.py"}
ARALIK = [
{"no":1023,
 "aday":"NULL — HAL GEÇİŞİ ADAYI DÜŞTÜ. Rastgele 10 aralıkta (tohum 2026+2027) başlangıç ve bitiş lafzının hali 9'unda farklıydı (beklenti 6,5; şans olasılığı ≈0,08). TAM SAYIM: 2.614 aralıkta farklı hal oranı 0,591 — bağımsızlık beklentisi 0,646'nın ALTINDA; ardışık lafızlar beklenenden SIK aynı halde. Geçiş matrisi simetrik (NOM→GEN 384 / GEN→NOM 382; NOM→ACC 184 / ACC→NOM 192; ACC→GEN 196 / GEN→ACC 208): yön bilgisi yok.",
 "olculen":{"farkli_gozlenen":0.591,"farkli_bagimsizlik":0.646,"diyagonal":{"NOM":379,"ACC":189,"GEN":500},"ornek":"9/10"},
 "durum":"DÜŞTÜ","oncelik":"P2",**ORT,"etiket":"küçük örneklem yanılgısı — null kaydı",
 "test_notu":"Düşük farklı-hal oranı (aynı hal yığılması) ayrı bir aday DEĞİL; konum-eşli null olmadan yorumlanamaz (aynı ayetteki lafızlar aynı kalıbı paylaşır)."},
{"no":1024,
 "aday":"TAŞIYICI PROFİLİ — lafız susunca Rab ve 1. çoğul uzun aralıklarda korpus ortalamasının üstünde: >10 ayetlik 58 aralığın 57'sinde Rab ya da 1P var; Rab/100 kelime 0,38 (aynı ayet) → 0,80 → 1,67 → 1,92 (>10 ayet), korpus 1,26; 1P 1,62 → 6,70, korpus 4,03.",
 "olculen":"ciktilar/aralik_olcum.json → tasiyici",
 "durum":"ACIK","oncelik":"P1",**ORT,"etiket":"sûre karıştırıcısı — uzun aralıklar Rab-yoğun Mekkî sûrelerde yığılıyor",
 "test_notu":"Tur sonu: sûre- ve konum-eşli null. 1P etiketi tanrısal 'Biz'i insan 1P'sinden ayırmıyor — test öncesi ya ayrıştırılmalı ya da duyarlılık analizi olarak raporlanmalı."},
{"no":1025,
 "aday":"TAŞIYICI TİPOLOJİSİ — Rab ve 1P'nin OLMADIĞI 20 aralık (≥4 ayet) elle açıldı; hiçbiri boş değil: O/هُوَ ٱلَّذِى (16:9→18), çıplak esmâ (26:213→227: 26:217), edilgen (4:19→23 حُرِّمَتْ; 64:16 يُوقَ), Sen/إِنَّكَ أَنتَ + esmâ (2:127-129). Harita: lafız · Rab · Biz · Sen · O · çıplak esmâ · edilgen. Sen ve O gönderge (coreference) takibi ister — ARAÇ YOK. Sonuç: projedeki 'Allah'a mesafe' ölçümleri fiilen 'LAFZA mesafe'.",
 "olculen":{"tasiyicisiz_aralik":20,"liste":"ciktilar/aralik_olcum.json → tasiyicisiz_4plus"},
 "durum":"ACIK","oncelik":"P1",**ORT,"etiket":"araç açığı (gönderge takibi) — metin bulgusu olarak KULLANILAMAZ; aday 435'e bağlı",
 "test_notu":"Aday 435 yeniden testinde duyarlılık: (a) yalnız lafız, (b) lafız+Rab+tanrısal 1P, (c) +edilgen (PASS etiketi), (d) +gönderge-esmâ. Sen/O ölçülemediği sürece (d)'ye kadar."},
{"no":1026,
 "aday":"ESMÂ İKİ İŞLEV — GÖNDERGE ve YÜKLEM: 26:217 تَوَكَّلْ عَلَى ٱلْعَزِيزِ ٱلرَّحِيمِ (gönderge, edat ardında GEN) / 26:220 إِنَّهُۥ هُوَ ٱلسَّمِيعُ ٱلْعَلِيمُ (yüklem). Lafız ve Rab'sız ayetlerde belirli+GEN esmâ taraması (ham 146 token, gürültülü) elle süzülünce ≈34 ayet: Rahmân ≈26 (19:11 ayet, 43:6…), تَقْدِيرُ ٱلْعَزِيزِ ٱلْعَلِيمِ ×3 (6:96, 36:38, 41:12 — üçü kozmik), تَنزِيل kalıbı ×2 (36:5, 41:2), tekil: 20:111, 22:24, 26:217. Bir emir fiilinin doğrudan nesnesi olan tek çıplak esmâ 26:217. 'Nakarat eğitimi' açıklaması (sekiz وَإِنَّ رَبَّكَ لَهُوَ ٱلْعَزِيزُ ٱلرَّحِيمُ'den sonra Rab düşüyor) 26:217 için mümkün, genel DEĞİL: 36:5 sûre başında, eğitim yok.",
 "olculen":{"ham_token":146,"suzulmus_ayet":"≈34 (elle)","rahman":"≈26","takdir":["6:96","36:38","41:12"],"tenzil":["36:5","41:2"],"tekil":["20:111","22:24","26:217"]},
 "durum":"ACIK","oncelik":"P2",**ORT,"etiket":"999/1019 ailesi — esmâ ön-kaydı DONDURULMUŞ, tanım değiştirilmedi",
 "test_notu":"Süzgeç kodlanırken gönderge/yüklem ayrımı açıkça karar verilmeli; mühür bayrağı yalnız yüklem işlevini tanımlıyor. Elle süzme okuma kararıdır — tam sayım tur sonunda."},
{"no":1027,
 "aday":"YÖNLÜ PROFİL — İZ VAR, YAKLAŞMA YOK: ≥10 kelimelik 1.626 aralıkta onda-birlik yoğunluk (100 kelimede) 3MS zamir 7,0→3,8, esmâ 6,5→1,5, Rab 1,3→0,7 (son dilim en düşük). İleri okumada lafızdan sonra sönen bir gönderim izi; geri okumada bitiş lafzından önce yükselen bir taşıyıcı yok. ÖNERİ: Allah mesafesi 'lafızdan beri' ve 'lafza kadar' AYRI ölçülmeli.",
 "olculen":"ciktilar/aralik_olcum.json → onda_birlik_profil_10plus",
 "durum":"ACIK","oncelik":"P1",**ORT,"etiket":"karıştırıcılar: esmâ zirvesi mühür bitişikliği (إِنَّ ٱللَّهَ عَلِيمٌ حَكِيمٌ); 3MS etiketi tüm 3MS zamirleri sayıyor",
 "test_notu":"Aday 435 yeniden testine iki yönlü mesafe olarak eklenmeli (konum-eşli null). Mühür tokenleri dışlanarak duyarlılık."},
{"no":1028,
 "aday":"ARTEFAKT — AYET İÇİ KONUM ASİMETRİSİ: ayet sınırını geçen 1.736 aralıkta başlangıç lafzı ayetin sonlarında (medyan 0,69), bitiş lafzı önde (0,40). Seçim etkisi: baş lafzı tanım gereği o ayetin SON lafzı, bitiş lafzı İLK lafzı.",
 "olculen":{"n":1736,"bas_medyan":0.69,"son_medyan":0.40},
 "durum":"ARTEFAKT","oncelik":"P3",**ORT,"etiket":"tanım sonucu — test edilmeyecek",
 "test_notu":"Yalnız konum-eşli null ile anlam taşıyabilir; şimdilik kayıt."},
{"no":1029,
 "aday":"İKİ ARALIK TÜRÜ? — korpus profili 'habersiz dönüş' derken iki örnek tersini gösteriyor: 10:6→10:10 (Biz → Rab → سُبْحَٰنَكَ ٱللَّهُمَّ → ٱلْحَمْدُ لِلَّهِ) ve 3:23→3:28 (Biz → قُلِ ٱللَّهُمَّ + 16 adet 2. tekil biçim → lafız): hitap/dua ile TIRMANAN aralıklar. Uzun aralıkların kapanış lafzı sık sık bir kulun ağzında (2:132 İbrâhîm, 12:64 Yakup, 37:35 alıntı).",
 "olculen":{"tirmanan":["10:6→10:10","3:23→3:28"],"kul_agzinda_kapanis":["2:132","12:64","37:35"]},
 "durum":"KAPATILAMAZ","oncelik":"P2",**ORT,"etiket":"okuma dikkati + araç açığı (konuşan/söz alanı yok)",
 "test_notu":"Taraflı örneklem kuralı: tam sayım ancak 'kim konuşuyor' alanı kurulursa. Kurulana dek test YOK."},
{"no":1030,
 "aday":"ARAÇ — اللَّهُمَّ AYRI LEMMA: morfoloji Allâhümme'yi LEM:اللَّهُمَّ (kök أله, PN, ACC + VOC eki) olarak ayırıyor; 5 token: 3:26, 5:114, 8:32, 10:10, 39:46. LEM=اللَّه tanımı (2.699 token) bunları dışarıda bırakıyor; aralık tanımında iki rastgele örnek (10:6→10, 3:23→28) içinde 'Allah'ım' geçtiği halde 'sessiz' sayıldı. betikler/ içinde اللَّهُمَّ hiç geçmiyor.",
 "olculen":{"token":["3:26:2:1","5:114:5:1","8:32:3:1","10:10:4:1","39:46:2:1"]},
 "durum":"ACIK","oncelik":"P1",**ORT,"etiket":"araç tanımı — okumayı BLOKE ETMİYOR, onarılmadı",
 "test_notu":"Aday 435 ve defter lafız alanı (allah z, eksen) bu beş tokeni nasıl sayıyor — test öncesi kontrol. Karar: vokatif lafız lafız mı sayılır?",
 "guncelleme_10_10":"Kısmi cevap (ağır okuma 10:6→10): defter LAFIZ alanı Allâhümme'yi SAYMIYOR (10:10'da yalnız 12. sıradaki lafız); AKTÖR alanı onu 'adlı اللَّهُمَّ, sınıf diger, rol meful' olarak alıyor; kök ikilemesi أله ×2 kök düzeyinde ikisini de görüyor. Üç alan aynı tokene üç farklı statü veriyor."},
{"no":1031,
 "aday":"ESMÂ YANLIŞ TAŞIYICI — gönderge denetimsiz esmâ sayımı lafızsız aralıkları 'taşıyıcılı' gösteriyor: 12:30 ٱلْعَزِيز (Mısır'ın azîzi), 9:128 رَءُوفٌ رَّحِيمٌ (elçi), 35:19 ٱلْبَصِير (insan), 35:20 ٱلنُّور (ışık), ayrıca kitaba sıfat: ٱلْكِتَٰبِ ٱلْحَكِيمِ (10:1, 31:2), ٱلْقُرْءَانِ ٱلْمَجِيدِ (50:1). 35:18→22 aralığı gerçekte tamamen sessiz; esmâ alanı iki taşıyıcı görüyor.",
 "olculen":{"vakalar":["12:30","9:128","35:19","35:20","10:1","31:2","36:2","50:1"]},
 "durum":"ACIK","oncelik":"P2",**ORT,"etiket":"§4.3 yanlış mühür ailesi — ön-kayıt DONDURULMUŞ",
 "test_notu":"Aralık/mesafe ölçümünde esmâ taşıyıcı olarak ancak e_el = ilahi ise sayılır (35:19, 35:20 zaten YANLIŞ MÜHÜR kayıtlı)."},
{"no":1032,
 "aday":"NAKARAT SINIRLI ARALIKLAR AYRI SINIF — 26:163→26:179 (89 kelime, 16 ayet): iki uç AYNI cümle (فَٱتَّقُوا۟ ٱللَّهَ وَأَطِيعُونِ, Lût / Şuayb); aralığın uzunluğu ve içeriği kalıptan geliyor. Ters okumada çerçeve değişmiyor.",
 "olculen":{"ornek":"26:163→26:179"},
 "durum":"ACIK","oncelik":"P1",**ORT,"etiket":"nakarat şişmesi dersinin aralık düzeyi karşılığı",
 "test_notu":"Her aralık istatistiğinden önce iki ucu nakarat3 kalıbında olan aralıklar işaretlenmeli ve ayrı raporlanmalı (sayısı henüz ölçülmedi)."},
{"no":1033,
 "aday":"TERS OKUMA AYRIMI — yön çevirince DEĞİŞMEYEN yapılar (35:19-22 halkası, nakarat çerçevesi) ile BOZULAN yapılar (gönderim zinciri: 26:217 esmâ → 218 ٱلَّذِى → 220 هُوَ; dua→icabet: 26:169 رَبِّ نَجِّنِى → 26:170 فَنَجَّيْنَٰهُ). Aralık okumasında sınıflama ölçütü adayı. Ek gözlem: 26:213→227 iki yarı — 213-220 taşıyıcılı hitap, 221-226 taşıyıcısız sahte söz (şeytan, şair); lafız istisnada (وَذَكَرُوا۟ ٱللَّهَ) dönüyor.",
 "olculen":{"simetrik":["35:19-22","26:163→179"],"yonlu":["26:217-220","26:169-170"],"iki_yari":"26:213→227"},
 "durum":"KAPATILAMAZ","oncelik":"P3",**ORT,"etiket":"okuma gözlemi",
 "test_notu":"Taraflı örneklem kuralı. Ölçülebilir hale gelmesi için yön-duyarlı bir yapı tanımı gerekir; şimdilik yok."},
{"no":1034,
 "aday":"35:19-22 ALAN HALKASI — dört eşitsizlik çifti: kör/gören (biyolojik) · karanlık/ışık (fiziksel) · gölge/sıcak (fiziksel) · diri/ölü (biyolojik). Fiil çerçevesi aynı eksende halka: يَسْتَوِى · لا…لا · لا…لا · يَسْتَوِى (لا sayısı 0,2,2,1 — tam ayna değil). Kutup dizisi – + – + + – + – sondan başa aynı (dört çiftte şans 1/4). Fâsıla 5/5 ر. Ortadaki üç kısa ayet monoton kısalıyor: harf3 21→17→16, mora 26→25→23. İçerik simetrik, çerçeve yönlü: ileri okuma 'dönüş Allah'a' → 'Allah işittirir'.",
 "olculen":{"harf3":[21,17,16],"mora":[26,25,23],"fasila":"ر ×5","kutup_palindrom_sans":0.25},
 "durum":"KAPATILAMAZ","oncelik":"P3",**ORT,"etiket":"okuma dikkati; ağır okuma 35:18→22",
 "test_notu":"Alan sınıflaması (biyolojik/fiziksel) mercek yorumu, ölçüm değil. Tek vaka."},
{"no":1035,
 "aday":"DİKEY BAĞIN BÖLÜNMESİ — korpus körlüğü sağırlığa sıkı bağlıyor (عمي ▸önce صمم ×93,1 · ▸sonra ×62,1, tek-sahne etiketi yok); 35:18→22 bu çifti iki uca bölüyor: körlük açılışta (35:19), işitmeme kapanışta (35:22 وَمَآ أَنتَ بِمُسْمِعٍ مَّن فِى ٱلْقُبُورِ), صمم kökü hiç geçmiyor.",
 "olculen":{"dikey":"ciktilar/blok_dikey_35_18_22.json","عمي_صمم":[93.1,62.1],"سمع_sonra_صمم":27.1},
 "durum":"ACIK","oncelik":"P3",**ORT,"etiket":"dikey katman + okuma",
 "test_notu":"Tam sayım mümkün: عمي geçişlerinin kaçında ±N kelimede صمم yok ama aynı birimde سمع olumsuzu var. Pencere önce önkayıtla sabitlenmeli."},
{"no":1036,
 "aday":"KORPUS SAYIMI — ظُلُمَة lemması 23/23 token ÇOĞUL, نُور 43/43 token TEKİL. Karanlık hep çok, ışık hep bir.",
 "olculen":{"ظُلُمَة":{"çoğul":23},"نُور":{"tekil":43}},
 "durum":"KAYIT","oncelik":"P3",**ORT,"etiket":"bulunurken bulundu; tam sayım — dış literatürde bilinen gözlem",
 "test_notu":"Test gerektirmiyor (istisnasız sayım). Gloss: ظلم kökünün gloss'u 'zulüm' — zulumât anlamı yok (aday 1000/1015 ailesi)."},
]
pa = 'bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('X_aralik', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and isinstance(x.get('no'), int))
nos = [x['no'] for x in ARALIK]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['X_aralik'] = ARALIK
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('X_aralik', len(ARALIK), '(%d-%d)' % (nos[0], nos[-1]), '| toplam aday', tot)
