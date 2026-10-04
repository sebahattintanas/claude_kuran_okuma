# -*- coding: utf-8 -*-
"""yasin_metin_1.py — sûre 36 (Yâsîn) meal ve matematikçi merceği, ayet 1-83.
Arapça sabit YOK: kökler yalnız korpus kök biçimiyle anılır, kelime biçimleri Latin harfle."""
MEAL = {}
M = {}
MEAL1 = {
 1: "Yâ Sîn.",
 2: "Hikmetli Kur'an'a andolsun ki,",
 3: "sen elbette gönderilen elçilerdensin,",
 4: "dosdoğru bir yol üzerindesin.",
 5: "(Bu Kur'an) mutlak güç sahibi, çok merhametli olanın indirmesidir;",
 6: "ataları uyarılmamış, bu yüzden gafil kalmış bir kavmi uyarman için.",
 7: "Andolsun, onların çoğu üzerine söz hak olmuştur; artık onlar iman etmezler.",
 8: "Biz onların boyunlarına halkalar geçirdik; o halkalar çenelerine kadardır, bu yüzden başları yukarı kalkık kalmıştır.",
 9: "Önlerine bir set, arkalarına bir set çektik; onları örttük, artık görmezler.",
 10: "Onları uyarsan da uyarmasan da onlar için birdir; iman etmezler.",
}
M1 = {
 1: "◇ Tek kelime, iki harf (hurûf-u mukattaa): n=1, kök yok, bağ yok. Ölçüm harf 21 → harf3 2 — yazım alanı harf adlarını değil işaretleri sayıyor. Fâsıla sınıfı ayrı (ٓ). Lafız YOK, Rab YOK, sınıf 0.",
 2: "◇ YEMİN (QASEM): 'hikmetli Kur'an'a andolsun'. Adlı aktör Kur'an (kitap, mecrur). Esmâ hakîm burada Kur'an'ın sıfatı → değil; §4.3 mühür e_oto EVET, e_el YOK: YANLIŞ MÜHÜR, sûrede ilk. حكم [1/1], قرأ [1/2]. n=2.",
 3: "◇ Yeminin cevabı: 'sen elbette gönderilenlerdensin' — 2MS, EMPH. رسل [1/8] (sûre içi 8 anma — sûre 35'te 6'ydı). n=3.",
 4: "◇ 'Dosdoğru bir yol üzerinde' — صرط [1/3], قوم [1/7]. 36:1-5 beş ayet: n = 1, 2, 3, 3, 3 — sûre beş kısa ayetle açılıyor (n 1-3); 36:2-5 fâsılası N sınıfı (م, ن).",
 5: "◇ 'Azîz ve rahîm olanın indirmesi': azîz-rahîm yüklem değil, tenzîl'in muzâfun ileyhi — tamlama içinde ad olarak esmâ, göndergesi Allah: e_el 'ilahi', aday 999'un ÜÇÜNCÜ vakası (34:6, 35:14, 36:5). §4.3 mühür ÇİFT geçerli, ton karma. Lafız YOK, Rab YOK — esmâ zamirsiz ve lafızsız: sınıf E. نزل [1/5], عزز [1/3], رحم [1/8].",
 6: "◇ Uyarma kökü iki kez, iki yönde: 'uyarman için' (tunzira, etken) / 'ataları uyarılmadı' (unzira, EDİLGEN) — نذر [1,2/6]. 7 kelimede 2 fiilin 1'i edilgen: ★★ tek kaynak pas z=2,52. Sonuç: gaflet (غفل [1/1]). أبو [1/1].",
 7: "◇ 'Söz onların çoğu üzerine hak oldu' — nakarat3 'haqqa'l-qavlu alâ' sûre içi, eşi 36:70 (defterden; kalıp korpusta yalnız bu iki ayette). say alanı ekser'i ('çoğu') sayı işareti saydı — belirteç, sayı değil (1004/1005 ailesi, yanlış pozitif). Fâsıla 'lâ yu'minûn' — 36:10 da aynı iki kelimeyle bitiyor.",
 8: "◇ DİKEY eksen: boyunlarda halkalar (ağlâl) → çenelere kadar (ezkân) → başlar yukarı kalkık (muqmahûn). Konuşan 1P (innâ ce'alnâ). قمح korpusta YALNIZ bu ayette: ★★★ tek kaynak hapaks z=3,28 (983 birikimi, hapaks kaynaklı). ذقن [1/1] — ezkân lemması korpusta 3 ayet; öteki ikisi 17:107 ve 17:109: 'çeneleri üzerine (yere) kapanırlar' (secde). Aynı organ zıt yönde: secdede çene yere / burada çene zincirde, baş yukarı. Yeni kökler ذقن ve قمح.",
 9: "◇ YATAY eksen: önlerinde set / arkalarında set — سدد [1,2/2] iki kez, ön ve arka; sonra 'örttük' (ağşeynâ, غشو [1/1]) → 'görmezler'. 36:8 dikey (boyun → çene → baş), 36:9 yatay (ön ↔ arka) + örtü: iki ayet, iki eksen, sonuç görmeme. جعل [2/5] iki ayette aynı fiil (ce'alnâ). بصر [1/2].",
 10: "◇ Simetrik bir eşitlik: 'uyarsan da uyarmasan da birdir' — نذر [3,4/6], olumlu/olumsuz aynı fiil; سوي [1/1]. 36:10, 2:6'nın 'inkâr edenler' öznesinden sonraki kısmıyla lemma lemma AYNI (morfoloji, 9 segment; 36:10 başta yalnız 've' ekliyor; xref iki üçlü). 'lâ yu'minûn' 36:7'yi tekrar ediyor: blok iki kez aynı sonuçla kapanıyor. Blokta نذر dört anma (36:6 ×2, 36:10 ×2), lafız ve Rab hiç yok.",
}
MEAL.update(MEAL1); M.update(M1)
MEAL2 = {
 11: "Sen ancak zikre uyan ve görmediği hâlde Rahmân'dan korkan kimseyi uyarırsın. Onu bağışlanma ve değerli bir ödülle müjdele.",
 12: "Şüphesiz ölüleri biz diriltiriz; onların önden gönderdiklerini ve bıraktıkları izleri yazarız. Her şeyi apaçık bir kitapta tek tek saymışızdır.",
 13: "Onlara o kasaba halkını örnek ver: Hani oraya elçiler gelmişti.",
 14: "Hani onlara iki elçi göndermiştik, onları yalanlamışlardı; biz de üçüncüsüyle destekledik. 'Biz size gönderilmiş elçileriz' dediler.",
 15: "Dediler ki: 'Siz ancak bizim gibi insanlarsınız. Rahmân hiçbir şey indirmemiştir. Siz ancak yalan söylüyorsunuz.'",
 16: "Dediler ki: 'Rabbimiz biliyor ki biz size elbette gönderilmiş elçileriz.",
 17: "Bize düşen ancak apaçık tebliğdir.'",
 18: "Dediler ki: 'Biz sizin yüzünüzden uğursuzluğa uğradık. Eğer vazgeçmezseniz sizi mutlaka taşlarız; bizden size acı bir azap dokunur.'",
 19: "Dediler ki: 'Uğursuzluğunuz sizinle beraberdir. Size öğüt verildi diye mi (böyle diyorsunuz)? Hayır, siz aşırı giden bir kavimsiniz.'",
 20: "Şehrin en uzak ucundan bir adam koşarak geldi. 'Ey kavmim, elçilere uyun' dedi.",
}
M2 = {
 11: "◇ Uyarının muhatabı daraltılıyor: 'ancak' zikre uyan ve 'gaybda Rahmân'dan korkan'. Aynı kalıp 35:18'de 'gaybda Rablerinden korkanlar'dı — burada Rab yerine Rahmân (xref 50:33: gaybda Rahmân'dan korkan). Rahmân sıfat değil bağımsız ad (nesne), göndergesi Allah: e_el 'ilahi' — e_el tanımı bu kullanımı saymıyor (aday 1019, 999 emsali). Müjde: bağışlanma + değerli ödül (ecrun kerîm; kerîm ödülün sıfatı → değil). 35:7 'mağfiret ve büyük ödül' ile aynı çift, sıfat değişiyor (kebîr → kerîm). نذر [5/6], خشي [1/1], غيب [1/1]. Lafız YOK, Rab YOK, sınıf oto E → el E.",
 12: "◇ Konuşan 1P, altı kez: diriltiriz · yazarız · saydık. İki yazım nesnesi: önden gönderdikleri (qaddemû) ve bıraktıkları izler (âsâr) — öne ve arkaya, 36:9'daki ön/arka ekseninin zaman karşılığı. 'Her şeyi saydık' (ahsaynâ): حصي [1/1], كلل [1/6], شيأ [1/10]; xref 78:29. Esmâ mübîn kitabın sıfatı → değil; §4.3 mühür e_oto EVET, e_el YOK: YANLIŞ MÜHÜR. حيي [1/5], موت [1/2]. Doğal olgu yok (diriltme anlatı), merdiven uygulanmadı.",
 13: "◇ Mesel açılışı: 'o kasabanın halkını örnek ver' — adsız aktör karye. ضرب [1/2], مثل [1/5], قري [1/1]. Elçiler geldi: رسل [2/8]. Fâsıla murselûn. Mesel anlatısı burada açılıyor; sınırı ileriki bloklarda okunacak.",
 14: "◇ Sayılı bir dizi: İKİ elçi → yalanladılar → ÜÇÜNCÜ ile destekledik. say alanı isneyn ve sâlis'i yakaladı: DOĞRU POZİTİF ×2. İkil şahıs 3D (iki elçi). عزز [2/3]: 36:5 'azîz' (esmâ) → 36:14 'azzeznâ' (destekledik) — aynı kök, Allah'ın sıfatı ve Allah'ın eylemi. كذب [1/2]. nakarat3 'innâ ileykum murselûn' sûre içi, eşi 36:16 (defterden). TARAYICI v4 ADAY VERDİ (F_ölçü — sayı kelimeleri), doğal olgu değil, merdiven uygulanmadı (35:1 ile aynı tetik).",
 15: "◇ Halkın cevabı, iki HASR: 'siz ANCAK bizim gibi insanlarsınız' / 'siz ANCAK yalan söylüyorsunuz'; arada 'Rahmân hiçbir şey indirmedi' (NEG 3). Rahmân bu kez inkârcıların ağzında, özne — gönderge yine Allah: e_el 'ilahi' (aday 1019). بشر [2/2] kapanıyor: 36:11 'müjdele' (beşşir) / 36:15 'beşer' (insan) — tek kök, iki anlam, gloss ikisini de taşıyor. كذب [2/2] kapanıyor: yalanladılar (36:14) → 'siz yalan söylüyorsunuz' (36:15) — suçlama yön değiştiriyor. nakarat3 'in entum illâ' sûre içi, eşi 36:47.",
 16: "◇ Elçilerin ikinci cümlesi, 36:14'ün PEKİŞTİRİLMİŞİ: 'innâ ileykum murselûn' → 'innâ ileykum LE-murselûn' (lâm-ı tekit eklendi) ve tanık olarak 'Rabbimiz biliyor'. İddia → inkâr → tekitli iddia. 6 kelimede bir Rab: ★★★ tek kaynak rab z=3,23 — 35:15/35:17'deki kısa ayet lafız şişmesinin Rab karşılığı (aday 1020, 1012 ailesi). Sûrede ilk Rab. ربب [1/6], علم [1/8], رسل [5/8]. xref 21:4.",
 17: "◇ 5 kelime, HASR: 'bize düşen ANCAK apaçık tebliğ'. بلغ [1/1]. Esmâ mübîn tebliğin sıfatı → değil; YANLIŞ MÜHÜR (36:12 ile aynı kelime, aynı karar). Elçilerin sözü 36:16-17 iki ayete yayılıyor.",
 18: "◇ Halkın ikinci cevabı, tehdit: 'sizin yüzünüzden uğursuzluğa uğradık' (tetayyernâ) → vazgeçmezseniz TAŞLARIZ → acı azap dokunur. Pekiştirme (EMPH) 5 — blokta en yüksek kip sayısı (36:11-20 ölçüm satırları). طير [1/2] uğursuzluk anlamında; gloss 'kuş; uçan', uğursuzluk anlamı yok (aday 1000 ailesi). رجم [1/1], مسس [1/1], عذب [1/1], ألم [1/1]. xref 11:48 (acı azap dokunur).",
 19: "◇ Elçilerin cevabı: 'uğursuzluğunuz SİZİNLE' — طير [2/2] kapanıyor; uğursuzluk dışarıdan (elçilerden) içeriye (onların kendisine) çevriliyor: 36:18'in tersine çevrilmesi. 'Size öğüt verildi diye mi' (zukkirtum, EDİLGEN): ★★ tek kaynak pas z=2,52. IDRAB: 'hayır, siz aşırı giden bir kavimsiniz' — سرف [1/1]. ذكر [2/3] (36:11 'zikre uyan'). TARAYICI v4 ADAY VERDİ (şart; طير kökü 'kuş' olarak tetikliyor olabilir), doğal olgu yok.",
 20: "◇ Yeni aktör: adsız bir adam (racül), şehrin EN UZAK ucundan, KOŞARAK. 36:13'te 'kasaba' (karye, قري [1/1]), burada 'şehir' (medîne, مدن [1/1]) — aynı yer iki adla. Nidâ: 'ey kavmim, elçilere uyun' — تبع [2/3]: 36:11 'zikre uyan' / 36:20 'elçilere uyun'. Konuşma sırası 36:14-20: elçiler (14) → halk (15) → elçiler (16-17) → halk (18) → elçiler (19) → adam (20); قول kökü yedi ayetin altısında (14, 15, 16, 18, 19, 20). Fâsıla murselîn: 36:1-20'de mursel- ile biten ayet 5 (3, 13, 14, 16, 20).",
}
MEAL.update(MEAL2); M.update(M2)
