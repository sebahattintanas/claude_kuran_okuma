# -*- coding: utf-8 -*-
"""aday_ekle_36_yasin.py — sûre 36 (Yâsîn) adayları (AU_yasin) ve okuma bağları (AP_yasin).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1019'dan); betik sıranın kopmadığını doğrular.
"""
import json

YASIN = [
# ---------------- blok 11-20 ----------------
{"no":1019,
 "aday":"ESMÂ TANIM DIŞI — RAHMÂN BAĞIMSIZ AD: 36:11 (haşiye'r-rahmân, nesne) ve 36:15 (enzele'r-rahmân, özne). e_el 'ilahi' tanımı (kâne/inne haberi, kefâ temyizi, Allah'ın ya da O'na dönen zamirin sıfatı) bu kullanımı kapsamıyor; okuyucu gönderge ölçütüyle 'ilahi' verdi (999 emsali).",
 "olculen":{"36:11":"nesne","36:15":"özne (inkârcıların sözünde)","e_el":"ilahi ×2","emsal":"999 (34:6, 35:14, 36:5 — tamlama içinde ad)"},
 "durum":"ACIK","oncelik":"P1","kaynak":"sûre 36 okuması, blok 11-20","etiket":"999 ailesi — e_suzgec tanımı; ön-kayıt DONDURULMUŞ, tanım değiştirilmedi",
 "test_notu":"Süzgeç kodlanırken (tam okuma sonrası) 'esmâ özel ad olarak' sınıfı açıkça karar verilmeli: lafız gibi mi sayılır, esmâ mı? Geriye dönük e_el turunda Rahmân'ın ad kullanımları (sûre 19, 20, 21, 25…) TAM SAYIMLA bulunmalı.",
 "guncelleme_36_21_30":"Üçüncü vaka 36:23 'in yuridni'r-rahmân' — şart cümlesinde özne, konuşan şehrin ucundan gelen adam; e_el 'ilahi' (gönderge ölçütü). Sûrede Rahmân bağımsız ad ×3 (36:11, 36:15, 36:23). Tanım değiştirilmedi."},
{"no":1020,
 "aday":"★★★ KISA AYET RAB ŞİŞMESİ (1012'nin Rab karşılığı) — 36:16: 6 kelimede 1 Rab, rab z=3,23, ★★★ tek kaynak.",
 "olculen":{"36:16":{"n":6,"rab":1,"rab_z":3.23,"yildiz2":3}},
 "durum":"ACIK","oncelik":"P1","kaynak":"sûre 36 okuması, blok 11-20","etiket":"983/1012 — ★★★ otomatik kaynak; uzunluk karıştırıcısı",
 "test_notu":"Onarılmadı. Tur sonunda allah- ve rab-kaynaklı ★★★'ların n dağılımı birlikte TAM SAYIMLA (1012 ile tek test).",
 "guncelleme_36_21_30":{"36:25":{"n":4,"rab":1,"rab_z":5.01,"yildiz":3,"kaynak":"rab (tek)"},"36:27":{"n":7,"rab":1,"rab_z":2.72,"yildiz":2,"kaynak":"rab (tek)"},"not":"İkinci ★★★ vaka (36:25) ve aynı ailede ★★ (36:27); kafiye kırığı yok, kaynak etiketi doğru (1001 dışı). Onarılmadı."}},
# ---------------- blok 31-40 ----------------
{"no":1021,
 "aday":"GLOSS TARAMASI — SÛRE 36 GİRDİLERİ (1015 ailesi): okunan ayetteki anlam kökün gloss'unda yok. (a) نهر 'ırmak' — BASKIN lemma nehâr (gündüz) yok: TAM SAYIM 113 token, nehâr 57 · nehar 54 · tenher 2 (36:37, 36:40). (b) حبب 'sevgi, sevme' — habb/habbe (tane) yok: 12/95 (36:33). (c) سبح 'tesbih, tenzih' — yüzme lemmaları (yesbah 2, sabh 2, sâbiha 1) yok: 5/92 (36:40). (d) حسر 'yorgunluk' — pişmanlık lemmaları (hasra, hasrat, hasratâ) yok: 9/12, baskın (36:30).",
 "olculen":{"نهر":{"toplam":113,"nehâr":57,"nehar":54,"tenher":2},"حبب":{"toplam":95,"tane":12},"سبح":{"toplam":92,"yüzme":5},"حسر":{"toplam":12,"pişmanlık":9,"yorgunluk":3}},
 "durum":"ACIK","oncelik":"P1","kaynak":"sûre 36 okuması, blok 21-30 ve 31-40","etiket":"987/1000/1015 ailesi — gloss taraması; araç dondurulmuş, gloss DEĞİŞTİRİLMEDİ",
 "test_notu":"Tam okuma sonrası sistematik gloss taramasında baskın lemması gloss'ta olmayan kökler TAM SAYIMLA listelenmeli (ظلل ve نهر iki baskın-lemma vakası). Dikey okumadaki komşu etiketleri gloss'tan geldiği için bu köklerin ▽ satırları yanlış anlamla etiketli olabilir — test öncesi kontrol.",
 "guncelleme_36_51_60":{"بني":{"toplam":184,"akrabalık (benî 80, ibn 63, bint 17)":160,"yapı (binâ 11, bunyân 7, binâ' 2)":20,"ayet":"36:60","not":"BASKIN anlam gloss'ta yok — ظلل ve نهر ile üçüncü baskın-lemma vakası"},"ظلم":"36:37 karanlık / 36:54 zulüm (1015 kaydı)","ظلل":"36:56 zılâl (1015 kaydı)"}},

# ---------------- blok 71-83 ----------------
{"no":1022,
 "aday":"ÖLÇÜM SATIRI ESMÂ ALANI ↔ ESMÂ KAYDI AYRIŞMASI: ölçüm satırının 'esmâ' alanı D2 eşlemesine giren ya da esmâ listesindeki bazı lemmaları yazmıyor, esma_kayit e_oto=1 sayıyor — 36:70 hayy ('men kâne hayyen', ölçüm 'esmâ yok') ve 36:79 evvel ('evvele merratin', ölçüm yalnız alîm). Okuyucu kararları ölçüm satırından toplanınca iki token kararsız kaldı; esma_kayit çıktısı ve eksik denetimi (e_oto var, e_el yok) ile yakalandı.",
 "olculen":{"36:70":{"lemma":"hayy","olcum_esma":"yok","e_oto":1,"e_el":"degil"},"36:79":{"lemma":"evvel","olcum_esma":"yalnız alîm","e_oto":1,"e_el":"degil"}},
 "durum":"ACIK","oncelik":"P2","kaynak":"sûre 36 okuması, blok 61-70 ve 71-83","etiket":"esmâ ön-kaydı veri toplama süreci; ön-kayıt DONDURULMUŞ, tanım değiştirilmedi",
 "test_notu":"Süreç kuralı (araç değil): esmâ el kararları her blokta esma_kayit çıktısından ve 'e_oto var, e_el yok' eksik denetiminden toplanır. Geriye dönük: önceki sûrelerde e_el boş kalmış e_oto tokenleri TAM SAYIMLA listelenmeli (geriye dönük e_el turu öncesi)."},

]

BAGLAR = {"AP_yasin": [
 # blok 1-10
 {"bag":"36:7 → 36:70","kural":"nakarat3 ('haqqa'l-qavlu alâ', sûre içi; kalıp korpusta yalnız bu iki ayet)","not":"Söz çoğu üzerine hak oldu / kâfirler üzerine hak olsun."},
 {"bag":"2:6 ↔ 36:10","kural":"lemma dizisi (9 segment aynı) + xref","not":"Uyarsan da uyarmasan da birdir, iman etmezler."},
 {"bag":"17:107 · 17:109 ↔ 36:8","kural":"lemma (ezkân, TAM SAYIM 3 ayet)","not":"Çeneleri üzerine secdeye kapanırlar / çenelere kadar halka, başlar yukarı."},
 {"bag":"36:8 ↔ 36:9","kural":"okuma gözlemi (جعل 1-2/5; dikey ve yatay eksen)","not":"Boyun → çene → baş / ön ↔ arka set + örtü."},
 {"bag":"34:6 · 35:14 ↔ 36:5","kural":"esmâ sınır vakası (aday 999)","not":"Tamlama içinde ad olarak esmâ — üçüncü vaka."},
 {"bag":"36:6 → 36:10","kural":"kök (نذر 1-4/6)","not":"Uyarman için, ataları uyarılmadı / uyarsan da uyarmasan da."},
 {"bag":"36:7 ↔ 36:10","kural":"okuma gözlemi (fâsıla 'lâ yu'minûn')","not":"Blok aynı sonuçla iki kez kapanıyor."},
 # blok 11-20
 {"bag":"35:18 ↔ 36:11 ↔ 50:33","kural":"kalıp (haşye + gayb) + xref","not":"Gaybda Rablerinden korkanlar / gaybda Rahmân'dan korkan."},
 {"bag":"35:7 ↔ 36:11","kural":"okuma gözlemi (mağfiret + ecr)","not":"Büyük ödül (kebîr) / değerli ödül (kerîm)."},
 {"bag":"36:9 ↔ 36:12","kural":"okuma gözlemi (ön/arka)","not":"Önde ve arkada set / önden gönderdikleri ve bıraktıkları izler."},
 {"bag":"78:29 ↔ 36:12","kural":"xref","not":"Her şeyi saydık."},
 {"bag":"36:5 → 36:14","kural":"kök (عزز 1-2/3)","not":"Azîz (esmâ) / üçüncüyle destekledik."},
 {"bag":"36:14 ↔ 36:16","kural":"nakarat3 ('innâ ileykum murselûn', sûre içi) — DOĞRULANDI","not":"İddia / lâm-ı tekitli iddia."},
 {"bag":"36:15 → 36:47","kural":"nakarat3 ('in entum illâ', sûre içi)","not":"36:47 henüz okunmadı."},
 {"bag":"36:11 ↔ 36:15","kural":"kök (بشر 1-2/2) + esmâ Rahmân ×2 (aday 1019)","not":"Müjdele / beşer; Rahmân'dan korkan / Rahmân indirmedi."},
 {"bag":"36:18 ↔ 36:19","kural":"kök (طير 1-2/2)","not":"Sizin yüzünüzden uğursuzluk / uğursuzluğunuz sizinle."},
 {"bag":"36:13 ↔ 36:20","kural":"okuma gözlemi (karye / medîne)","not":"Aynı yer iki adla."},
 {"bag":"36:11 → 36:20","kural":"kök (تبع 1-2/3)","not":"Zikre uyan / elçilere uyun."},
 {"bag":"35:15 · 35:17 ↔ 36:16","kural":"yıldız kaynağı (kısa ayet; aday 1012/1020)","not":"Lafız ★★★ / Rab ★★★."},
 # blok 21-30
 {"bag":"36:20 → 36:21","kural":"kök (تبع 2-3/3; aynı emir fiili ardışık)","not":"Elçilere uyun / ücret istemeyenlere uyun."},
 {"bag":"36:11 → 36:21 · 36:27","kural":"kök (أجر 2/2 · غفر 2/2 · كرم 2/2) — okuma gözlemi, KAPATILAMAZ","not":"Müjdenin üç kökü (mağfiret, ecr, kerîm) adamın sözünde yeniden."},
 {"bag":"36:11 · 36:15 ↔ 36:23","kural":"esmâ Rahmân bağımsız ad (aday 1019)","not":"Nesne / özne / şart cümlesinde özne."},
 {"bag":"36:23 → 36:74","kural":"nakarat3 ('ittehaze min dûn', sûre içi; kalıp korpusta 8 ayet)","not":"36:74 henüz okunmadı."},
 {"bag":"53:26 ↔ 36:23","kural":"xref","not":"Şefaat hiçbir şey fayda vermez."},
 {"bag":"36:23 → 36:24","kural":"okuma gözlemi (şart → 'izen' sonucu)","not":"Mantıksal birim iki ayete yayılıyor."},
 {"bag":"36:12 · 36:17 ↔ 36:24","kural":"esmâ §4.3 yanlış mühür (mübîn)","not":"Kitap / tebliğ / sapıklık."},
 {"bag":"36:16 ↔ 36:25","kural":"yıldız kaynağı (kısa ayet Rab şişmesi; aday 1020)","not":"6 kelime z=3,23 / 4 kelime z=5,01."},
 {"bag":"36:25 → 36:27","kural":"okuma gözlemi (ربب 2-3/6; iyelik 2MP → 1S)","not":"Sizin Rabbiniz / Rabbim."},
 {"bag":"36:20 ↔ 36:26","kural":"okuma gözlemi (qavmî hitabı)","not":"Ey kavmim / keşke kavmim bilseydi."},
 {"bag":"2:111 · 18:39 ↔ 36:26","kural":"xref","not":"Cennete girme ve söz."},
 {"bag":"36:26 → 36:27","kural":"okuma gözlemi (ayet sınırı cümleyi bölüyor)","not":"Keşke bilseydiler — Rabbimin bağışladığını."},
 {"bag":"36:29 → 36:49 · 36:53","kural":"nakarat3 (7 kelime → 36:53; 3 kelime 'illâ sayhaten vâhideten' → 36:49, 36:53)","not":"İkisi de henüz okunmadı."},
 {"bag":"36:30 → 36:46","kural":"nakarat3 ('mâ ye'tî … min', sûre içi)","not":"36:46 henüz okunmadı."},
 {"bag":"9:65 · 15:11 ↔ 36:30","kural":"xref","not":"Elçiyle alay."},
 {"bag":"36:22 ↔ 36:30","kural":"kök (عبد 1-2/4)","not":"Kulluk etmeyeyim mi / kullara hasret."},
 # blok 31-40
 {"bag":"36:30 → 36:31","kural":"okuma gözlemi (ibâd → kurûn)","not":"Kullar / nesiller — genelleme tarihe uzanıyor."},
 {"bag":"36:22 ↔ 36:31","kural":"kök (رجع 1-2/5)","not":"O'na döndürüleceksiniz / onlara dönmezler."},
 {"bag":"6:6 ↔ 36:31","kural":"xref","not":"Kendilerinden önce nice nesli helâk ettik."},
 {"bag":"36:32 → 36:53","kural":"nakarat3 ('cemî'un ledeynâ muhdarûn', sûre içi)","not":"36:53 henüz okunmadı."},
 {"bag":"36:12 ↔ 36:33","kural":"kök çifti (حيي + موت) — okuma gözlemi, KAPATILAMAZ","not":"Ölüleri diriltiriz / ölü yeri dirilttik."},
 {"bag":"36:33 ↔ 36:37","kural":"okuma gözlemi (2 kelimelik açılış 've âyetun lehum'; nakarat3 ve ikili yakalamıyor)","not":"Ölü yer âyet / gece âyet."},
 {"bag":"36:26 ↔ 36:34","kural":"kök (جنن 1-2/3; iki anlam)","not":"Cennet / bahçeler."},
 {"bag":"17:91 ↔ 36:34","kural":"xref","not":"Hurma, üzüm, fışkırtma."},
 {"bag":"36:22 ↔ 36:36","kural":"okuma gözlemi (yaratan sılayla anılıyor)","not":"Beni yaratan / bütün çiftleri yaratan."},
 {"bag":"43:12 ↔ 36:36","kural":"xref","not":"Bütün çiftleri yaratan."},
 {"bag":"36:5 · 36:14 → 36:38","kural":"kök (عزز 3/3) + esmâ tamlama içinde ad (aday 999)","not":"Azîz / destekledik / Azîz'in takdiri."},
 {"bag":"6:96 · 41:12 ↔ 36:38","kural":"xref (taqdîru'l-azîzi'l-alîm)","not":"Aynı terkip."},
 {"bag":"36:38 → 36:39","kural":"kök (قدر 1-2/3; isim → fiil)","not":"Takdîr / takdir ettik."},
 {"bag":"36:8 ↔ 36:39","kural":"yıldız kaynağı (hapaks ★★★; aday 983)","not":"قمح / عرجن."},
 {"bag":"36:37 · 36:38 · 36:39 → 36:40","kural":"kök (شمس قمر ليل نهر hepsi 2/2)","not":"Dört iplik tek ayette kapanıyor."},
 {"bag":"36:36 ↔ 36:40","kural":"kök (سبح 1-2/3; iki anlam, aday 1021)","not":"Subhân / yüzerler."},
 {"bag":"21:33 ↔ 36:40","kural":"xref","not":"Her biri bir yörüngede yüzer."},
 # blok 41-50
 {"bag":"36:33 · 36:37 → 36:41","kural":"okuma gözlemi (3. 've âyetun lehum'; أيي 1-3/6)","not":"Ölü yer / gece / gemi."},
 {"bag":"36:40 ↔ 36:41","kural":"kök (فلك 1-2/2; iki lemma: felek / fulk)","not":"Yörünge / gemi — ardışık ayetler."},
 {"bag":"36:23 ↔ 36:43","kural":"kök (نقذ 1-2/2; etken → edilgen)","not":"Kurtaramazlar / kurtarılmazlar."},
 {"bag":"36:9 · 36:12 → 36:45","kural":"kök (يدي, خلف 2/2) + okuma gözlemi (ön/arka üçüncü kez)","not":"Önde-arkada set / önden gönderilen ve izler / önünüzden-arkanızdan sakının."},
 {"bag":"36:45 ↔ 36:47","kural":"nakarat3 ('iżâ qîle lehum', sûre içi) — DOĞRULANDI","not":"Sakının denildiğinde / harcayın denildiğinde."},
 {"bag":"36:45 → 36:46","kural":"okuma gözlemi (şart cevabı hazfı; 46 hükmü tamamlıyor)","not":"Denildiğinde — … yüz çevirirler."},
 {"bag":"36:33 · 36:37 · 36:41 → 36:46","kural":"kök (أيي 4-5/6)","not":"Âyetler sayıldı / gelen âyetten yüz çevirme."},
 {"bag":"6:4 ↔ 36:46","kural":"esit2 YAKIN (0,9882) + xref","not":"Rablerinin âyetlerinden hiçbir âyet gelmez ki yüz çevirmesinler."},
 {"bag":"36:23 → 36:47","kural":"kök (أله 1 → 2,3/5) — sûrenin ilk lafzı 36:47","not":"İlâhlar / Allah."},
 {"bag":"36:24 ↔ 36:47","kural":"kalıp ('dalâlin mübîn'; ضلل 1-2/3)","not":"Adamın şartlı hükmü / inkârcıların mü'minlere hükmü."},
 {"bag":"4:39 · 7:50 ↔ 36:47","kural":"xref","not":"Allah'ın rızkından harcama."},
 {"bag":"10:48 · 21:38 · 27:71 · 34:29 · 67:25 · 32:28 ↔ 36:48","kural":"esit2 (TAM ×4, YAKIN, BENZER)","not":"Bu vaat ne zaman?"},
 {"bag":"36:29 ↔ 36:49","kural":"nakarat3 ('illâ sayhaten vâhideten', 3 ayet) — 36:53 henüz okunmadı","not":"Geçmiş kasabanın çığlığı / beklenen çığlık."},
 {"bag":"38:15 ↔ 36:49","kural":"xref","not":"Tek çığlık beklemek."},
 {"bag":"36:31 ↔ 36:50","kural":"kök (رجع 2-3/5)","not":"Onlara dönmezler / ailelerine dönemezler."},
 # blok 51-60
 {"bag":"36:29 · 36:37 → 36:51 · 36:53","kural":"okuma gözlemi ('fe-izâ hum', metin sayımı 4)","not":"Söndüler / karanlıktalar / akın ediyorlar / huzurdalar."},
 {"bag":"36:48 → 36:52","kural":"kök (وعد 1-2/3, صدق 1-2/2) + işaret zamiri hâzâ — okuma gözlemi, KAPATILAMAZ","not":"Bu vaat ne zaman? / Bu, Rahmân'ın vaadi; elçiler doğru söyledi."},
 {"bag":"36:11 · 36:15 · 36:23 ↔ 36:52","kural":"esmâ Rahmân bağımsız ad (aday 1019)","not":"Dördüncü vaka."},
 {"bag":"36:29 ↔ 36:53","kural":"nakarat3 (7 kelime) — DOĞRULANDI","not":"Tek çığlık: söndüler / huzurdalar."},
 {"bag":"36:32 ↔ 36:53","kural":"nakarat3 ('cemî'un ledeynâ muhdarûn') — DOĞRULANDI","not":"Hepsi huzurumuza getirilecek / getirilmişler."},
 {"bag":"36:29 · 36:49 · 36:53","kural":"nakarat3 ('illâ sayhaten vâhideten', 3 ayet) — TAMAMLANDI","not":"Geçmiş kasaba / bekleyen / diriliş."},
 {"bag":"36:37 ↔ 36:54","kural":"kök (ظلم 1-2/2; iki anlam)","not":"Karanlıktalar / zulmedilmez."},
 {"bag":"21:47 ↔ 36:54","kural":"xref","not":"Hiçbir nefse hiçbir şekilde zulmedilmez."},
 {"bag":"36:13 ↔ 36:55","kural":"kalıp (ashâb + yer; صحب 1-2/2) — okuma gözlemi, KAPATILAMAZ","not":"Kasaba halkı / cennet halkı."},
 {"bag":"36:26 · 36:34 → 36:55","kural":"kök (جنن 3/3)","not":"Cennet / bahçeler / cennet."},
 {"bag":"25:24 ↔ 36:55","kural":"xref","not":"Cennet halkı o gün."},
 {"bag":"36:36 ↔ 36:56","kural":"kök (زوج 1-2/2; çiftler / eşler)","not":"say alanı iki kez yanlış pozitif."},
 {"bag":"36:55 ↔ 36:57","kural":"kök (فكه 1-2/2; keyif / meyve)","not":"Tek kök iki anlam."},
 {"bag":"36:16 · 36:25 ↔ 36:58","kural":"yıldız kaynağı (kısa ayet Rab şişmesi; aday 1020)","not":"Üçüncü vaka."},
 {"bag":"36:5 → 36:58","kural":"kök (رحم 1 → 8/8; rahîm açılış ve kapanış)","not":"Azîz-rahîm'in indirmesi / rahîm Rab'den selâm."},
 {"bag":"36:22 · 36:30 → 36:60","kural":"kök (عبد 1-3/4)","not":"Kulluk etmeyeyim mi / kullar / şeytana kulluk etmeyin."},
 # blok 61-70
 {"bag":"36:60 → 36:61","kural":"kök (عبد 4/4)","not":"Şeytana kulluk etmeyin / bana kulluk edin."},
 {"bag":"36:4 ↔ 36:61 ↔ 36:66","kural":"kök (صرط 1-3/3) + terkip 'sırât mustaqîm' (4, 61)","not":"Dosdoğru yol üzerindesin / bu dosdoğru yol / yola koşuşma."},
 {"bag":"36:24 · 36:47 → 36:62","kural":"kök (ضلل 3/3)","not":"Sapıklık: adam / inkârcılar / şeytan."},
 {"bag":"36:7 ↔ 36:62","kural":"kök (كثر 1-2/2) + say yanlış pozitif ×2","not":"Ekser / kesîr."},
 {"bag":"36:48 · 36:52 → 36:63","kural":"kök (وعد 3/3) + işaret zamiri — okuma gözlemi, KAPATILAMAZ","not":"Bu vaat ne zaman / bu Rahmân'ın vaadi / bu vaat olunan cehennem."},
 {"bag":"36:54 · 36:55 · 36:59 · 36:64 → 36:65","kural":"kök (يوم 5/5; beşi 'el-yevm')","not":"O gün ipliği."},
 {"bag":"36:20 ↔ 36:65","kural":"kök (رجل 1-2/2; adam / ayaklar)","not":"Tek kök iki anlam."},
 {"bag":"36:43 → 36:66 · 36:67","kural":"okuma gözlemi ('dilersek' 1P ×3)","not":"Boğarız / gözlerini silerdik / şekillerini değiştirirdik."},
 {"bag":"36:34 ↔ 36:66","kural":"kök (عين 1-2/2; pınar / göz)","not":"Tek kök iki anlam."},
 {"bag":"36:50 ↔ 36:67","kural":"yapı (istitâ'a + lâ yerci'ûn; طوع, رجع) — nakarat3 yakalamıyor, KAPATILAMAZ","not":"Vasiyet edemezler, dönemezler / ileri gidemezler, dönemezler."},
 {"bag":"36:8 · 36:39 ↔ 36:67","kural":"yıldız kaynağı (hapaks ★★★; aday 983)","not":"قمح / عرجن / مسخ."},
 {"bag":"36:62 → 36:68","kural":"kök (عقل 1-2/2; 2MP → 3MP)","not":"Akıl erdirmiyor muydunuz / akıl erdirmiyorlar mı."},
 {"bag":"36:2 ↔ 36:69","kural":"kök (قرأ 1-2/2)","not":"Hikmetli Kur'an / apaçık Kur'an."},
 {"bag":"36:40 ↔ 36:69","kural":"kök (بغي 1-2/2; 'yenbeğî') — okuma gözlemi, KAPATILAMAZ","not":"Güneşe yaraşmaz / ona (elçiye) yaraşmaz."},
 {"bag":"36:7 ↔ 36:70","kural":"nakarat3 ('haqqa'l-qavlu alâ') — DOĞRULANDI","not":"Söz çoğunun üzerine hak oldu / kâfirler üzerine hak olsun."},
 {"bag":"36:6 → 36:70","kural":"kök (نذر 1 → 6/6)","not":"Uyarman için / uyarsın diye."},
 # blok 71-83
 {"bag":"36:31 · 36:71 · 36:77","kural":"kök (رأي 3/3; 'e (ve) lem yera')","not":"Helâk edilen nesiller / davarlar / nutfeden insan."},
 {"bag":"36:35 ↔ 36:71","kural":"kalıp ('amile + yed'; عمل 3/3) — okuma gözlemi, KAPATILAMAZ","not":"Onların elleri yapmadı / ellerimizin yaptığından."},
 {"bag":"36:42 → 36:72","kural":"kök (ركب 2/2)","not":"Binecekleri / binekleri."},
 {"bag":"36:33 · 36:35 → 36:72","kural":"kök (أكل 3/3)","not":"Tane / meyve / davar."},
 {"bag":"36:35 ↔ 36:73","kural":"tekrar ('e-felâ yeşkurûn'; شكر 2/2) — nakarat3 yakalamıyor","not":"İki ürün listesinin sonu."},
 {"bag":"36:23 ↔ 36:74","kural":"nakarat3 ('ittehaze min dûn') — DOĞRULANDI","not":"O'ndan başka ilâhlar mı edineyim / Allah'tan başka ilâhlar edindiler."},
 {"bag":"36:47 · 36:74","kural":"lafız (sûrede tek iki ayet, 3 token)","not":"Allah'ın rızkı · Allah dileseydi / Allah'tan başka."},
 {"bag":"19:81 ↔ 36:74","kural":"xref","not":"Allah'tan başka ilâhlar edinme."},
 {"bag":"36:50 · 36:67 → 36:75","kural":"kök (طوع 3/3; üçü de 'güç yetiremez')","not":"Vasiyet / ileri gitme / yardım."},
 {"bag":"36:28 ↔ 36:75","kural":"kök (جند 1-2/2)","not":"Gökten ordu indirmedik / hazır ordu."},
 {"bag":"36:32 · 36:53 → 36:75","kural":"kök (حضر 3/3; fâsıla 'muhdarûn' ×3)","not":"Huzura getirilecekler."},
 {"bag":"36:49 ↔ 36:77","kural":"kök (خصم 1-2/2)","not":"Çekişirken / apaçık hasım."},
 {"bag":"16:4 ↔ 36:77","kural":"xref (nutfe, hasîm mübîn)","not":"Aynı terkip."},
 {"bag":"36:13 ↔ 36:78","kural":"kök (ضرب 1-2/2; misal getirme, yön tersine) — okuma gözlemi, KAPATILAMAZ","not":"Onlara misal getir / bize misal getirdi."},
 {"bag":"36:12 · 36:33 · 36:70 · 36:78 → 36:79","kural":"kök (حيي 5/5)","not":"Diriltme ipliği."},
 {"bag":"36:28 → 36:81","kural":"kök (سمو 1-2/2)","not":"Gök / gökler."},
 {"bag":"36:38 · 36:39 → 36:81","kural":"kök (قدر 3/3)","not":"Takdîr / takdir ettik / kadir."},
 {"bag":"17:99 ↔ 36:81","kural":"xref","not":"Gökleri ve yeri yaratan, benzerlerini yaratmaya kadir."},
 {"bag":"36:23 ↔ 36:82","kural":"kök (رود 1-2/2)","not":"Rahmân dilerse / dilediğinde."},
 {"bag":"36:36 ↔ 36:83","kural":"kalıp ('subhâne'llezî'; سبح 1, 3/3)","not":"Çiftleri yaratan / melekût elinde olan."},
 {"bag":"36:22 ↔ 36:83","kural":"tekrar ('ve ileyhi turja'ûn'; رجع 1, 5/5) — nakarat3 yakalamıyor, KAPATILAMAZ","not":"Adamın sözünün sonu / sûrenin sonu."},
 {"bag":"36:71 ↔ 36:83","kural":"kök (ملك 1-2/2)","not":"Davarlara sahipler / her şeyin melekûtu."},
 {"bag":"23:88 ↔ 36:83","kural":"xref","not":"Her şeyin melekûtu elinde olan."},

]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AU_yasin', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in YASIN]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AU_yasin'] = YASIN
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AU_yasin', len(YASIN), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AP_yasin', len(BAGLAR['AP_yasin']))
