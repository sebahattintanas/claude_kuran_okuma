# Lafızdan lafza aralık okuması (2026-10-05, ayrı oturum)

Sûre okumasının DIŞINDA yapılmış keşif turu. Ölçüm çerçevesi değişti: "bir kök Allah'a ne kadar uzak?" yerine
"iki Allah lafzı arasında ne oluyor?". Bütün sayılar betimleyici; null model yok. Adaylar: `X_aralik` 1023–1036.

## Tanım
* Aralık = sûre içinde ardışık iki `LEM:اللَّه` tokeni arasındaki kelimeler; sûre sınırını geçenler dışlandı.
* 2.699 lafız tokeni → 2.614 aralık. Uzunluk medyanı 13, ortalama 23,4, en uzun 735 (17:39→17:92).
* Sınıflar: A aynı ayet 878 · B 1–3 ayet 1.514 · C 4–10 ayet 164 · D >10 ayet 58.
* **Bilinen eksik:** `اللَّهُمَّ` (5 token) sınır sayılmadı (aday 1030). Karşılaştırılabilirlik için tanım oturum boyunca değiştirilmedi.
* Anahtarlar korpustan kopyalandı (NFC); elle yazılan lemma iki kez sessizce 0 eşleşme verdi.

## Örneklem (katmanlı, tohumlar sırayla)
| tohum | aralıklar |
|---|---|
| 2026 | 3:31 · 9:28→29 · 24:61→62 · 35:34→38 · 37:23→35 |
| 2027 | 3:4 · 22:32→34 · 2:285→286 · 2:126→132 · 12:52→64 (D katmanı 37:23 tekrar düştü, aynı tohumla yeniden çekildi) |
| 2028 | 9:127→129 · 10:6→10 · 3:23→28 |
| 2029 | 64:16→17 · 35:18→22 · 26:163→179 |
Ayrıca elle açılan: taşıyıcısız 20 aralık (≥4 ayet) ve 26:213→227.

## Seyir
1. Hal geçişi örneklemde 10'da 9 → tam sayımda DÜŞTÜ (1023).
2. Taşıyıcılar: lafız susunca Rab / Biz / Sen / O / çıplak esmâ / edilgen (1024, 1025). "Allah'a mesafe" fiilen "lafza mesafe".
3. Çıplak esmâ — gönderge vs yüklem; 26:217 (1026).
4. Ters okuma: iz var, yaklaşma yok (1027); ama dua/hitap aralıkları tırmanıyor (1029). Simetrik vs yönlü yapı (1033).
5. Araç bulguları: اللَّهُمَّ (1030), esmâ yanlış taşıyıcı (1031), nakarat sınırlı aralık (1032).
6. Ağır okuma 35:18→22 (1034, 1035, 1036) — sayfa `ciktilar/aralik_35_18_22.html`, dikey `ciktilar/blok_dikey_35_18_22.json`.

## Yeniden üretim
```
python3 betikler/aralik_olcum.py        # → ciktilar/aralik_olcum.json (örneklem dahil)
python3 betikler/aday_ekle_aralik.py    # X_aralik set, idempotent
```
`blok_dikey.py 35 18 22` düz dizinde, önce `onarim/04_ngram_altyapi.py` (ayet_iskelet.json depoda yok).

## Ağır okuma 2 — 16:9 → 16:18 (NUMARASIZ gözlemler)
Numara verilmedi: sûre 37 adayları 1037'den başlayacak; bu gözlemlere numara sûre 37 numaralarını aldıktan sonra verilecek.
Sayfa `ciktilar/aralik_16_9_18.html`, dikey `ciktilar/blok_dikey_16_9_18.json`.
* **"Taşıyıcısız" en uzun aralık en sıkı taşınan aralık:** Rab ve 1P yok, ama fail 16:16 dışındaki her ayette — هُوَ ٱلَّذِى (10, 14), fiil eki (أَنزَلَ, يُنۢبِتُ, سَخَّرَ, ذَرَأَ, أَلْقَىٰ), iyelik (بِأَمْرِهِۦ, فَضْلِهِۦ). 1025'in en güçlü vakası.
* **Hazırlanan dönüş:** ad (16:9) → zamir/ek (10–15) → İŞLEV (16:17 أَفَمَن يَخْلُقُ) → ad (16:18). 1027 ortalama profiline karşı vaka; 1029'daki hitap türünün yanında BETİMLEME ile yaklaşma türü olabilir. KAPATILAMAZ.
* **Sayım lafzı çağırıyor:** ~24 öğelik katalog (elle) `عَدَّ` + `لَا تُحْصُوهَا` ile kapanırken lafız dönüyor; عدد↔حصي ×41,7 (tek-sahne etiketi yok). Tek vaka.
* **هدي halkası:** ahlaki yol (16:9 قَصْدُ ٱلسَّبِيلِ, هَدَىٰكُمْ) → fiziksel yol (16:15 سُبُل · 16:16 بِٱلنَّجْمِ يَهْتَدُونَ). Yıldız iki işlevle: düzenin nesnesi (16:12) / yön aracı (16:16).
* **شكر lafızsız ayette:** 16:14 تَشْكُرُونَ; kökün Allah medyanı 1 (düz null, etiketsiz — 435).
* Gloss: جور 'komşuluk' — burada 'sapan' (1015 ailesi).

## Araç onarımı — سوم (okumayı bloke eden arıza istisnası)
16:10 تُسِيمُونَ: ölçüm `???`, dikey `KARŞILIK YOK`. `betikler/kok_ekle_aralik.py` ile eklendi (1165 → 1166; lemma: sîmâ 6 · yesûmu 4 · musavvem 4 · tusîmu 1).
Geriye dönük yama (`yama_retroaktif_gloss_aralik.py`): hedef 11 ayet, yama 0, genel geçiş 0. Denetimler: türkçe 0 · anahtar 70 (PYTHONHASHSEED=0, ihlal farkı 0; taranan sayısı yeni betiklerle arttı).
**Açığa çıkan kapsam:** okunmuş ayetlerde karşılıksız kök **145** daha (sûre 9–19 ve 2:13, 2:16) — liste `ciktilar/karsiliksiz_kokler_okunan.json`. `turkce_denetim.py` yalnız kok_turkce içindeki kökleri tarıyor; tabloda olmayan kök ona görünmez.

## Ağır okuma 3 — 10:6 → 10:10 (NUMARASIZ gözlemler)
Sayfa `ciktilar/aralik_10_6_10.html`, dikey `ciktilar/blok_dikey_10_6_10.json`.
* **Şahıs merdiveni:** inkâr edenler kısmında Tanrı NESNE konumunda 1P (10:7 لِقَآءَنَا, ءَايَٰتِنَا) → 10:8 hiç yok (مَأْوَىٰهُمُ ٱلنَّارُ, fail adsız); iman edenler kısmında ÖZNE konumunda 3. şahıs Rab (10:9 يَهْدِيهِمْ رَبُّهُم) → 2. şahıs hitap (10:10 سُبْحَٰنَكَ ٱللَّهُمَّ) → ad (ٱلْحَمْدُ لِلَّهِ). Uzaklık burada şahıs ve konumla kodlanmış görünüyor. 1029 'tırmanan' türünün ayrıntılı vakası; okuma gözlemi, KAPATILAMAZ.
* **Uzunluk palindromu (bulunurken bulundu, ölçüm):** n = 14 · 15 · 6 · 15 · 14 ve sınırları aralığın iki lafzıyla çakışıyor. Korpus sayımı (sûre içi 5 ayetlik pencere, 5.783 pencere): tam palindrom 109 (%1,9); en az 3 farklı değerli 35 (%0,6). 'Merkez en kısa ve en uzun ≥12' biçimini taşıyan TEK pencere 10:6–10 — ama bu biçim ölçütü görüldükten SONRA kuruldu (post-hoc), adil taban %1,9 / %0,6.
* **حيي iki uçta iki anlam:** 10:7 ٱلْحَيَوٰةِ ٱلدُّنْيَا (inkâr edenlerin yetindiği hayat) / 10:10 تَحِيَّتُهُمْ (cennettekilerin selamı).
* **Ölçüm:** 1030 güncellendi (lafız alanı Allâhümme'yi saymıyor, aktör alanı 'diğer'). Esmâ alanı 10:10'da سَلام ve آخِر işaretliyor — yanlış taşıyıcı (1031 ailesi).
* 10:6 lafzı anlatıcıda, 10:10 lafzı cennettekilerin ağzında (1029).

## Ağır okuma 4 — 53:58 → 53:62 (NUMARASIZ; sûre 53 henüz okunmadı, meal çalışma çevirisi)
Sayfa `ciktilar/aralik_53_58_62.html`, dikey `ciktilar/blok_dikey_53_58_62.json`. 11 kelime — okunan en kısa aralık.
* **Hitap kesintisiz, Tanrı yok:** 53:59–61 baştan sona 2MP dinleyene hitap (تَعْجَبُونَ · تَضْحَكُونَ · لَا تَبْكُونَ · سَٰمِدُونَ); taşıyıcı yok. Lafız aynı 2MP'ye EMİRLE dönüyor (فَٱسْجُدُوا۟ لِلَّهِ). Dördüncü dönüş türü adayı: emirle dönüş (habersiz / betimleme / hitap / emir).
* **Uzunluk sıkışması (ölçüm):** n = 6 · 4 · 3 · 2 → 3. Aralık en kısa ayette (sâmidûn, n=2) dibe vuruyor, lafız bir sonrakinde.
* **İşlevle açılış:** aralığın ilk kelimesi كَاشِفَةٌ — 'Allah'tan başka giderecek yok'; işlev olumsuzlanarak O'na veriliyor (16:17 'yaratan' ile aynı mekanizma, ters uçta).
* **Gülme/ağlama:** ضحك + بكي aynı ayette korpusta 3 kez (9:82, 53:43, 53:60); ikisi bu sûrede. 53:43'te fail هُوَ (güldüren ve ağlatan O), 53:60'ta dinleyen — ve yalnız gülüyor.
* **سمد ↔ سجد:** bitişik iki ayette, yalnız orta harfi farklı iki kök; 'başı dik/kayıtsız' (anlam tartışmalı — mercek) ile 'secde'. Kapanış bir beden eylemi ve âyet secde âyeti: aralığın dönüşü okuyucunun hareketine bağlanıyor. KAPATILAMAZ.
* **Ölçüm:** 53:61 ★★★ hapaks kaynaklı, 53:62 ★★★ allah z=6,14 (kısa ayet şişmesi, 1012 ailesi).
* **Araç:** سمد gloss'suzdu (ölçüm ???) — `kok_ekle_aralik.py` ile eklendi; `kok_turkce.json` **1167**. Yama 0, türkçe 0, anahtar 70 (ihlal farkı 0).

## ◈B Biyolog merceği aralıklara (2026-10-05, NUMARASIZ)
Tetik listesi `ONKAYIT_mercekler.md` §4'ten DEĞİŞTİRİLMEDEN alındı (commit a7e9628). Okuma kayıtlarına yazılmadı (§7 geriye dönük doldurma yasağı). Betik `betikler/aralik_biyolog.py` → `ciktilar/aralik_biyolog.json`.
* **Korpus düzeyi — DÜZ:** biyoloji tetiği 100 kelimede korpus 2,77 · aralık içi 2,74 · lafız ±6 kelime 2,63. ≥10 kelimelik 1.626 aralıkta onda-birlik profil 2,5–3,1 arasında, eğim yok; dört sınıfın (canlı, oluşum, organ, dirim) hiçbirinde lafız yakını/uzağı farkı yok. Taşıyıcıların (zamir, esmâ, Rab) sönen profiliyle karşıt: biyoloji sözlüğü lafza göre konumlanmıyor.
* **Dört aralık:** 35:18→22 tetik 3 (بصر, حيي, موت) · 16:9→18 tetik 5 · 10:6→10 tetik 3 · 53:58→62 tetik 0.
* **Tetik listesi kesinlik sorunu:** نعم 'canlı' sınıfında, ama kökün 140 tokeninden yalnız 33'ü نَعَم (davar); 50 نِعْمَة, 17 نَعِيم, 17 أَنْعَمَ, 18 نِعْمَ… Aralıklardaki iki نعم tetiğinin ikisi de nimet (16:18 نِعْمَةَ ٱللَّهِ, 10:9 جَنَّٰتِ ٱلنَّعِيمِ).
* **Tetik listesi duyarlılık sorunu:** 16:10–14'teki ekin, zeytin, hurma, üzüm, meyve, içme, otlatma, taze et (زرع زيت نخل عنب ثمر شرب سوم لحم) listede yok; 53:60–62'deki beden eylemleri (ضحك بكي سجد) da yok. 16:9→18'de biyolojik öğelerin yaklaşık yarısı tetiklenmiyor (elle).
* **§8 sapma önerisi (UYGULANMADI):** نعم için lemma süzgeci (yalnız نَعَم); besin/ürün ve beden eylemi alt sınıfları. Ön-kayıt dondurulmuş — karar kullanıcının, sûre 37 oturumuyla birlikte.

## ◈K Kozmolog merceği aralıklara (2026-10-05, NUMARASIZ)
Tetik listesi `ONKAYIT_mercekler.md` §3'ten DEĞİŞTİRİLMEDEN (a7e9628). Betik `betikler/aralik_kozmolog.py` → `ciktilar/aralik_kozmolog.json`.
* **Korpus düzeyi — gök-yer İZ TARAFINDA:** 100 kelimede korpus 2,52 · aralık içi 2,44 · lafız ±6 2,25. Onda-birlik (≥10 kelime, 1.626 aralık) gök-yer 2,0 → 1,1 (son dilim en düşük); zaman 0,6–0,9 düz. Gök-yer sözlüğü lafızdan SONRA yoğun, lafızdan ÖNCE seyrek — taşıyıcı profiline benzer. Olası karıştırıcı: لِلَّهِ مَا فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ / خَلَقَ ٱللَّهُ ٱلسَّمَٰوَٰتِ kalıpları (lafız + gök-yer bitişik). Biyoloji düz, kozmoloji eğimli: KAPATILAMAZ değil — tam sayımla konum-eşli test edilebilir.
* **Dört aralık:** 35:18→22 tetik 0 (karanlık/ışık, gölge/sıcak listede yok) · 16:9→18 tetik 13 · 10:6→10 tetik 3 (10:9 نهر = cennet ırmakları) · 53:58→62 tetik 0.
* **ÖN-KAYIT KUSURLARI (§3, ölçüldü):**
  - ÖLÜ kök ×2 — korpusta hiç eşleşmiyor: `ريح` (rüzgâr; korpus kökü روح — 29 token رِيح görünmüyor), `ساعة` (kıyamet saati; korpus kökü سوع — 48 token görünmüyor). Aynı hata sınıfı daha önce ريح/زتن ile anahtar_denetim'de yakalanmıştı.
  - YANLIŞ kök ×1 — `سنن` 'yıl' diye listede, ama korpusta سُنَّة 16 · سِنّ 2 · مَسْنُون 3 eşleşiyor (yıl değil); yıl kökü سنو (سِنِين 12 · سَنَة 7) listede yok.
  - Çok anlamlılık: سمو 381 tokenin 71'i ad (اسْم 39, مُسَمًّى 21…); فلك 25 tokenin 23'ü gemi (فُلْك), 2'si yörünge.
  - Duyarlılık: ışık/karanlık/gölge/sıcaklık (نور ظلم ظلل حرر ضوأ) listede yok.
  - `anahtar_denetim.py` .md dosyasını taramıyor: ön-kayıttaki elle yazılmış kökler hiçbir denetimden geçmemiş.
* **§8 sapma önerisi (UYGULANMADI):** ريح→روح (lemma رِيح), ساعة→سوع, سنن→سنو; سمو için lemma süzgeci (سَماء). Karar sûre 37 oturumuyla.

## Ters okuma — mushafın sonundan, onluk onluk (2026-10-05)
"Bizim okuma düzenimiz, en sondan" = mushafın sonundan başa (114:6 →). Sayfalar: `ciktilar/sondan_01_30_ters_mushaf.html` (1–30 tek sayfa; 114:6 → 108:3), üretici `betikler/sondan_01_30_uret.py` (+ `ters_onluk_sayfa.py`). Sûre 108–114 okunmadı — meal çalışma çevirisi.
Gözlemler (NUMARASIZ, KAPATILAMAZ): son 30 ayette 4 lafız, ikişer ikişer tek sûre içinde (110:1–2, 6 kelime; 112:1–2, 1 kelime); 109'da Tanrı yalnız 'taptığım' (مَآ أَعْبُدُ) ile; 3MS üç komşu sûrede üç gönderge (108:3 kin besleyen, 111 Ebû Leheb, 112:3 Tanrı).
Sondan 31–60: `ciktilar/sondan_31_60_ters_mushaf.html` (108:2 → 103:1), üretici `betikler/sondan_31_60_uret.py`. 30 ayette tek lafız (104:6); Rab-çapalı zincirler (105, 106); tek lafzın çevresi edilgen (104:4, 6, 8, 9).

## KATMAN 1 — bütün Kur'an, lafız-çapalı sayfalar (2026-10-05)
Kullanıcı kararı: blok eşiği **200 kelime**. `betikler/kuran_aralik_sayfalari.py` + `betikler/kuran_aralik_sablon.html` → `ciktilar/kuran_aralik_sayfalari.html` (tek dosya, ~4 MB, çevrimdışı çalışır; yazı tipi için internet gerekir, yoksa yedek yazı tipi).
* Kesim: ham sınırlar lafız + sûre başı (2.822 kesit); >400 kelimelik kesit ayet sınırında bölünür — birikim ≥200 iken Rab içeren ayette (ikincil çapa), Rab yoksa 400'de düz. Açgözlü birleştirme, blok ≥200.
* Sonuç: **320 sayfa**, medyan 219 kelime, en az 136 (mushafın son sayfası 108:1→114:6), en çok 584. Sayfa açılışları: lafız 293 · sûre başı 18 · Rab 9.
* Görüntüleyici: Mushaf/Ters düğmesi, sayfa numarası, kaydırıcı, sûre seçici, 'sûre:ayet' ile atlama; sayfa başına aralık şeridi; sol aralıklar, sağ mushaf ayetleri + kayıtlı meal (2.578 ayet).
* İşaretler otomatik, doğrulanmamış: lafız · Rab · esmâ? · 1P? · edilgen · Allâhümme (lafız sayılmaz, 1030). Okunmamış ayete not yok.

## Matematikçi — düz/ters simetri testleri (KEŞİF, ön-kayıtsız; NUMARASIZ)
Betik `betikler/simetri_olcum.py` → `ciktilar/simetri_olcum.json`. Null: sûre içi karıştırma / aynı uzaklıkta çift; tek/çift sûre yarıları ayrı (keşif/doğrulama).
* **T1 ayet uzunluğu palindromu:** 5'li pencere tek sûrelerde 76 (null 44), çift sûrelerde 33 (null 31) — YARILAR TUTMUYOR. Katkı 37, 55, 81, 77 (nakarat ve eşit uzunluklu diziler). Trivial olmayan (≥3 farklı değer): tek 23/15 (p .036), çift 12/15 (p .83) → genel palindrom örüntüsü YOK; 10:6–10 tekil vaka.
* **T1d yerel düzen:** komşu ayetlerin eşit uzunlukta olması her iki yarıda null'un 1,17–1,18 katı — TUTARLI. Palindrom fazlalığının asıl kaynağı ayna değil, yerel ritim dizileri.
* **T2 aralık halkası:** iki lafız ayetinin kök örtüşmesi rastgele ayet çiftine göre 1,11 / 1,20 — ama null 'ikisi de lafız içeren ayet çifti' olunca 1,00 / 0,99 → halka değil, lafız ayetlerinin ortak kalıp sözlüğü.
* **T3 sûre halkası (ilk–son ayet):** yüzdelik ort. 0,49 / 0,54 → genel bir başlangıç–son yankısı YOK.
* Sonuç: korpus düzeyinde düz/ters simetri yok; tutarlı olanlar (a) yerel ritim dizileri, (b) lafız çevresindeki YÖNLÜ asimetri (1027 profili, gök-yer eğimi). Elle görülen aynalar (10:6–10, 35:19–22) yerel.

## Yön testi (ÖN-KAYITLI: `notlar/ONKAYIT_yon_testi.md`)
Ayet içi sıra rastgele çevrilen null'a karşı, iki yarıda: omnibus asimetri TUTTU (2,5×), L→O TUTTU, L→E TUTTU, R→O KISMİ. Yön var; dilbilgisinden ayrıştırılmadı — kontrol isimli ön-kayıt önerildi.

## Eşzamanlı okuyucu — ONAYLANAN tasarım (2026-10-05)
Örnek `ciktilar/okuyucu_ornek_sondan.html` (sayfa 320 + 319, 90 ayet), üretici `betikler/okuyucu_ornek.py` — kullanıcı onayladı.
Satır = ayet çifti (sol ters, sağ düz), tek kaydırma, sayfa ortasında buluşma; hücrede numara · sûre adı (değişince) · aralık etiketi · mushaf metni · meal (taslak etiketi). Varsayılan yalnız lafız; Rab/esmâ?/1P?/edilgen düğmeyle.
Taslak meal tohumu: `tablolar/calisma_meali.json` — 90 ayet (100:1–114:6), durum 'taslak'. okuma_metni.json mealleri önceliklidir.
