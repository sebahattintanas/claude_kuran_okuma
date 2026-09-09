# OTURUM KAPANIŞI — 2026-09-04

## Ne yapıldı

**SÛRE 25 (FURKĀN) AÇILDI.** Makro profil sıfırdan çıkarıldı; **25:1-10**,
sekiz blok halinde **25:1-77 TAM** okundu (**SÛRE 25 TAMAMLANDI**), ardından
**SÛRE 26 (ŞUARÂ) AÇILDI**: makro profil + 26:1-60 (üç blok). Okunan ayet
**1645 → 1782** (korpusun %28,6'sı). Tam okunan sûreler: 1, 9-25. Tam okunan sûreler: 1, 9-24.
Kısmi: 2 (1-20), 25 (1-10).

Boru hattı sıfırdan koşturuldu (`defter.py` → `graf2.py`); çıktılar taban değerlerle
uyumlu (i'râb GEN 12626 · NOM 8806 · ACC 12824; yıldız {0:4029, 1:748, 2:579, 3:880};
esmâ 1463 ayet / 2077 token; aktör tablosu 61 aktör).

Adaylar **524 → 638** (yeni `AG_furkan`, 114 aday). Bağlar: `AE_furkan` 96 ve
`AF_suara` 43 bağ.
Kök tablosu **959 → 982** (yirmi üç yeni kök); ayrıca **altı karşılık genişletildi**
(`ملو` · `سوق` · `قرن` · `بغي` · `كون` · `صهر`).

## Denetimler

- `turkce_denetim.py` → **0**. İlk koşuda 18 ihlâl; **hepsi aynı sınıftan** —
  `bağ:` alanındaki xref lemma 3-gram'larının içindeki karşılıksız kök anmaları
  (`خلق` · `ولد` · `نفس` · `رجل` · `نظر` · `كيف` · `ضرب` · `مثل`). Onarım: 3-gram
  tokenleri tek tek karşılık alacak biçimde yeniden yazıldı. **Bu yeni bir desen** —
  önceki turlarda ihlâller yeni kök eklemesinden geriye dönük açığa çıkıyordu;
  burada kaynak xref biçiminin kendisi.
- İkinci blokta `turkce_denetim.py` ilk koşuda **1** ihlâl (`عتد`), onarıldı → 0.
- `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, taban listesiyle diff = 0**;
  iki blokta da ayrı koşuldu. Taranan anahtar 21614 → **21619**.

## Blok bölme

**25:1-20 ikiye bölündü (25:1-10 / 25:11-20).** Gerekçe `okuma_metni.json` →
`25/_blok_bolme_notu`: (1) yapı — 25:1 ve 25:10 aynı fiille (`تَبَارَكَ`) açılıyor,
25:11 `بَلْ` ile açılıp IDRAB alıyor ve sahne âhirete geçiyor; (2) hacim — açılış
onlusu ayet başına 9,7 kök taşıyor, dikey katman ayet başına ~1650 karakter üretiyor.

## Öne çıkan ölçümler

**A/R üçüncü veri noktası (aday 525).** 23 (Mekkî) 0,57 → 24 (Medenî) tanımsız →
25 (Mekkî) 0,57. Korpusta Allah yoğunluğu en düşük 14 sûrenin on dördü de Mekkî.
Neredeyse tam ikiz: sûre 34.

**Fâsıla i'râbı tek yönlü (aday 526).** 77/77 ACC. Sûre, ACC payında korpus birincisi
(0,596) ve **fâsıla kelimesi çıkarıldığında da birinci** (0,495).

**25:9 = 17:48 tam ayet özdeş ama `esit` boş (aday 530).** Tek fark imlâ. xref
katmanı yakalıyor (beş 3-gram), `esit` yakalamıyor. 25:8-9 ↔ 17:47-48 ardışık
bölüt ikizi.

**Dikey katman — üç yeni lemma karışması vakası (aday 529).** En büyüğü 25:3:
`ءَالِهَة` *(ilâhlar)* için `أله` kökünün n=2851'lik lafız komşuluğu geliyor.

**Karşılık tablosu — beş vaka (aday 537).** Sûre 23 bir vaka vermişti; 25 beş.

## Mercek

Blokta **★★★ ayet yok**; iki uzman merceği yazılmadı. Adaylar 468/512 için veri:
bu blokta yıldız ile çıpa **aynı yönde** (ikisi de yok) — sûre 24'te ters yönde
ayrışmışlardı.

## Onarılmayan borçlar

Katı kural gereği bu oturumda da **hiçbir araç onarılmadı**: 435+452+474, esmâ
kümesi (461, 467, 484, 497, 501, 508), 487 (kaynak metni), 468/472/503/512,
517, 438+483, 462, 451/431/437/443, ölçü tanımı eksikleri (496, 500, 507, 522).
Yeni eklenenler: **529** (452/474 kümesine), **530** (496 kümesine), **537**
(480 kümesine).

## İkinci blok (25:11-20) — öne çıkanlar

**Birinci şahıs tam 25:11'de başlıyor (aday 538).** 25:1-10'da 1P ve 1S sıfır;
sûrede birinci şahıs taşıyan 31 ayetin 30'u 25:11'den sonra. Kırılma noktası blok
bölme çizgisiyle çakışıyor — **bölme kararı bu ölçümden önce ve başka gerekçeyle
verildi; post hoc doğrulama, ön-kayıt değil**.

**Aday 535 kapandı, ön-kayıt tuttu (aday 545).** 25:7 ↔ 25:20; dört farklılaşan
öğenin dördü doğrulandı. 456→476'da ön-kayıt düşmüştü; bu kez bağlaç ve kip
düzeyinde yazıldığı için tuttu.

**Aday 438'e iki karşı kontrol daha.** 25:15 ve 25:17'de `أَمْ` muttasıla ve iki
ayet de INTG alıyor.

**Esmâ: blokta üç token, mühür sıfır, yanlış pozitif 2/3 (aday 546).** Payda 3 —
sûre 23'ün %67'siyle sayısal karşılaştırma yapılmayacak.

**Aday 529'a dördüncü vaka.** 25:19 `صرف` — kök komşuluğu "âyetleri açıklama",
ayet "azabı çevirme".

**Mercek ara bilanço (20/77):** ★★★ sıfır · ★★ bir · ★ dört · çıpa sıfır.

## Üçüncü blok (25:21-30) — öne çıkanlar

**Aday 512'nin en temiz vakası (aday 553).** Sûrenin ilk ★★★ ayeti 25:28 ve
çıpası sıfır; yıldızın tek kaynağı `hapaks z=3,38`. Buna karşılık gerçek gök
öğesi taşıyan 25:25 yalnız ★★ alıyor. Sûre 24'te ayrışma ters yöndeydi.

**Aday 546'nın büyük vakası açıldı (aday 549).** 25:26'da `رَحْمٰن` marife, `لِ`
ile mecrur, mülkün sahibi konumunda — sözdizimsel kanıt **özel ad** yönünde.
Ayrım çözülmeden sûrenin esmâ sayımı kullanılamaz.

**Esmâ yanlış pozitifi: aynı sınıftan üçüncü vaka.** 25:18 `وَلِيّ`, 25:19 ve
25:21 `كَبِير` — üçü de mühürsüz, üçü de ölçüt (b) ile dışlanıyor.

**Kök tablosu ilk kez bu turda büyüdü (959 → 970) ve geriye dönük ihlâl açığa
çıkmadı (aday 554)** — önceki turların desenine aykırı; eklenen on bir kökün
sekizi korpusta ≤4 geçişli.

**İki yeni ölçü tanımı eksiği (496 kümesi):** fiilsiz ayet alanı yok (548), çatı
alanı yok (552).

## Dördüncü blok (25:31-40) — öne çıkanlar

**Aday 553 güçlendi (aday 561).** Sûrenin okunan kırk ayetinde **üç ★★★ ayetin
üçünde de çıpa sıfır** (25:28 ve 25:33 hapaks kaynaklı, 25:34 edilgenlik oranı
1,00 ile z=5,38). Çıpa taşıyan iki ayet ise ★★ (25:25) ve yıldızsız (25:40).
Çıpa tanımı için ölçüt önerisi yazıldı: **öğenin anılması çıpa değildir**, ayetin
o öğe hakkında ölçülebilir bir şey söylemesi gerekir.

**Esmâ ölçüt çatışmasının en temiz vakası (aday 555).** 25:31'de `هَادِيًۭا` ve
`نَصِيرًۭا` aynı ayette, aynı konumda, aynı i'râbda — tablo yalnız fâsıla olanı
esmâ sayıyor. Tablo sözdizimini değil konumu kullanıyor olabilir.

**MM etiketleme işinin gerekçesi (aday 559).** Blokta fiil + mef'ûl-i mutlak üç
kez, üçü de bab II · 1P · fâsıla. `defter.json`'da MM alanı yok. Sûrenin ACC
baskınlığıyla karışma riski var.

**İkinci fiilsiz ayet ve aktör tablosu tutarsızlığı.** 25:38 fiilsiz; `عاد` ve
`ثَمُود` aktör tablosuna giriyor, `أَصْحَٰبَ ٱلرَّسِّ` girmiyor (aday 462).

## Beşinci blok (25:41-50) — oturumun en güçlü ölçümü

**On ayet, sıfır yıldız, sûrenin en yoğun doğa bölütü (adaylar 561, 565).**
25:45-46 gölgenin uzatılması → gerçekleşmemiş alternatif → güneşin gösterge
kılınması → kademeli çekilme; 25:47 gece/uyku/gündüz; 25:48 rüzgâr-yağış
sıralaması; 25:49 suyun ölü beldeyi diriltmesi. **★★★ 0 · ★★ 0 · ★ 0.**
Protokol gereği 🜁 ve 🜂 yazılamadı; kural çiğnenmedi, ama **yıldız formülünün
içeriği hiç ölçmediği** en açık biçimde görüldü.

**Yeni ölçüm sorunu (aday 566):** sûrenin fâsılası A sınıfı ve %100 ACC; bu kısıt
"aynı kelime farklı bağlamda" bulgularını sistematik üretiyor olabilir. Fâsıla
kısıtı altında beklenen tekrar oranı hesaplanmadan bu sınıftan hiçbir bulgu
kapatılmayacak.

**Aday 554 düştü ve 570 olarak düzeltildi.** `ذنب` n=39 eklendi, geriye dönük
ihlâl yine çıkmadı — "seyreklik" açıklaması yetersiz. Hipotez sessizce
değiştirilmedi, düşürüldüğü belgelendi.

**Aday 529 sûre 25'te altı vakaya çıktı** ve bir onarım ölçütü önerisi doğdu
(aday 569): dikey satırına kökün **bab'ı** girdi olarak katılsın.

## Altıncı blok (25:51-60) — üç P0

**Aday 549 belirlendi (aday 578).** `رَحْمٰن` sûre 25'te özel ad gibi işliyor;
belirleyici kanıt 25:60'ta: `وَمَا ٱلرَّحْمَٰنُ` *(Rahmân da ne)* — itiraz
edenler adı tanımadıkları bir ad olarak ele alıyor. **Esmâ tablosu sıfat-esmâ ile
özel adı ayırmıyor**; sûrenin "22 token" sayımı beş token düşebilir.

**Aday 462 doğrulandı ve kendi kaydımız geri çekildi (aday 579).** Makro
profilde yazdığım "adsız aktör: nefer 25:60", `نُفُورا` *(nefret)* kelimesinin
kök düzeyinde yanlış eşleşmesiymiş. `25/_makro/aktor` alanında geri çekildi.

**Aday 580 — yirmi ardışık yıldızsız ayet (25:41-60)** ve sûrenin bütün doğa
bölütü içlerinde. Çıpa taşıyan dokuz ayetin yalnız biri yıldızlı; üç ★★★ ayetin
üçü de çıpasız. Yıldız-çıpa korelasyonu **sıfır ya da negatif** görünüyor.

## Yedinci blok (25:61-70) — iki aday kapandı, bir yeni P0

**528 → 581 kapandı.** `تَبَارَكَ` üç geçiş (25:1, 10, 61); göreli konumlar
0,013 · 0,130 · 0,792. **549/578 kapandı:** beş `رَحْمٰن` tokeninin beşi de
gönderge/özel ad kullanımı.

**Aday 580 → 590.** 25:61 sûrenin en açık gök-cismi ayeti (`سرج` *(kandil)* /
`قمر مُّنِير` *(aydınlatan ay)*) ve **yıldızı sıfır**. Sûrenin çıpalı ayet
sayısı 11, yıldız alan 1; ★★★ dört ayetin dördü çıpasız.

**Yeni P0 — kısa ayet yanlılığı (aday 583).** 25:64'te n=5 ve tek `رَبّ` →
rab z=3,94, okumadaki en yüksek. Dört ★★★ ayetin hepsinde ayet ortalamadan kısa.
**Yıldız formülü kısa ayetleri sistematik kayırıyor olabilir.**

**Aday 529'a sekizinci vaka (586):** `قوم` altı ayet içinde dört ayrı lemma,
dikey satırı dördü için aynı komşuluğu getiriyor.

## Sekizinci blok (25:71-77) ve SÛRE KAPANIŞI

**Esmâ tam denetimi — hata oranı %36 (aday 598).** 22 tokenin 8'i geçerli, 8'i
artefakt, 5'i özel ad, 1'i belirsiz. **Mühür sinyali üçüncü sûrede de
doğrulandı:** iki mühürlü konum geçerli, sekiz artefaktın hepsi mühürsüz.

**Yıldız/çıpa tam tablosu (aday 599).** ★★★ 6 · ★★ 5 · ★ 8 · yıldızsız 58.
**Altı ★★★ ayetin altısında da çıpa sıfır**; çıpa taşıyan on bir ayetin yalnız
biri yıldızlı. Yıldız ile çıpa arasında korelasyon sıfır ya da negatif.

**Fâsıla kısıtı — kendi bulgularımızın karıştırıcısı (aday 600).** 77/77 ACC
fâsıla, kelime seçim uzayını daraltıyor. Sûrenin yedi "aynı kelime farklı
katmanda" bulgusu bu kısıt altında üretilmiş olabilir; taban dağılımı
hesaplanmadan hiçbiri kapatılmayacak.

**Beş aday kapandı:** 528→581 · 535→545 · 549/578 · 544→597 · 562.

## Sûre 26 (Şuarâ) açılışı — üç P0

**"Mekkî 0,57" hipotezi ilk sınavda düştü.** 23 (0,57) → 24 (∞) → 25 (0,57) →
**26 (0,36)**. A yoğunluğu yine düşük (0,28x) ama **R yoğunluğu 2,16x, okumada
en yüksek** — ayrışan A değil R.

**Aday 583 doğrulandı (602).** Sûre 26 ayet başına 5,81 kelime (en kısa) ve
%18,1 ★★★; 41 ★★★ ayetin 29'u eksen oranından. 26:26'da rab z=8,20. Korpus
taraması r = −0,367 (betimsel, anlamlılık testi koşulmadı).

**Yıldız sayımının bağımsızlık ihlâli (606) — kritik.** Sûre 26'da 34 nakarat
ayeti; `عَزِيز|رَحِيم` nakaratı sekiz ayette birebir aynı **ve sekizi de ★★★**.
Bunlar bağımsız gözlem değil. Düzeltilmiş pay %15,0.

**Esmâ: okumada en büyük artefakt bloğu (601).** `مُؤْمِن` on beş token, on beşi
de artefakt; sûrenin 51 tokeninin %29'u.

**26:1'de ▽ satırı yazılamadı** — `طسٓمٓ` kök taşımıyor; okumada ilk kez.

## Sûre 26 ikinci blok (26:21-40)

**Aday 621 — `esit` alanının davranışı artık tam tanımlı.** 26:32-33 ↔ 7:107-108
ardışık ikizini **yakalıyor**; 25:9 = 17:48'i (imlâ) ve 25:66 ≈ 25:76'yı (tek
kelime) kaçırıyor. Alan **üçe** bölünecek: `esit_tam` · `esit_normal` ·
`esit_yakin`. Sınama kümesi hazır.

**Aday 602'nin en uç vakası:** 26:26'da **rab z = 8,20** (n=5, iki Rab).
Ve **aday 624 — okumada ilk kez iki ardışık ayet aynı kaynaktan ★★★** (26:38-39,
ikisinde de tek fiil edilgen, oran 1,00). ★★★ sayımı hem tekrar hem kısa-ayet
kümelenmesiyle şişiyor.

**Aday 578'e karşı örnek (616).** 26:23'te `وَمَا رَبُّ ٱلْعَٰلَمِينَ` — aynı
soru kalıbı bir sıfat tamlamasına uygulanıyor; 578'in üçüncü kanıtı zayıfladı.
Kendi bulgumuzu düşürebilecek veri açıkça yazıldı.

**Aday 529 onuncu vakaya çıktı ve onarımın iki katmanlı olması gerektiği
görüldü:** bab girdisi `صرف`/`قرن`/`رجو`/`طلق`'ı çözüyor, ama `جنن`'de
(cennet/cin/delilik, üçü de isim kalıbı) **lemma düzeyi zorunlu**.

## Sûre 26 üçüncü blok (26:41-60) — kısa ayet yanlılığının üç temiz gösterimi

**(1) Üç ardışık ★★★** (26:46-48), üçünde de ayet 3-4 kelime; 26:48'de
`rab z=6,78`. **(2) Sûrenin en uzun ayeti (26:49, n=21, yedi kip işareti, yedi
xref) YILDIZSIZ** (aday 632). **(3) 26:54-56'da aynı kalıptaki üç ayetten yalnız
biri ★★★ ve ayrım tek bir hapakstan** (aday 637).

**Aday 621'e ikinci veri:** 26:47-48 ↔ 7:121-122 ikizini `esit` **yakalıyor**;
26:36 ↔ 26:53 (öneri → uygulama) **yakalamıyor** — `esit_yakin` için üçüncü
sınama vakası.

**Esmâ onarımı için kritik veri (629):** tablo 26:44'te gönderge denetimini
doğru yapıyor ama 26:34 ve 26:49'da yapmıyor — muhtemelen **doğru sonuç yanlış
sebeple** (lemma eşleşmemesi).

**Yeni sınıf: çatı yörüngesi** (628, 635). `لقي` dört ardışık ayette emir →
çoğul → tekil → edilgen; `تبع` niyet → uyarı → gerçekleşme.

## Devam noktası

**Sûre 26, ayet 61.** Blok 25:21-40; sûrenin kıssa yoğunluğu orada başlıyor
(25:35 Mûsâ/Hârûn, 25:37 Nûh, 25:38 Âd/Semûd) ve üç ★★★ ayet orada (28, 33, 34).

## Değişen dosyalar (zip'te)

```
notlar/okuma_metni.json · mercek_kayit.json · okuma_baglantilari.json
notlar/YAPILACAKLAR.md · OTURUM_2026-09-04_KAPANIS.md (YENİ)
tablolar/kok_turkce.json (959 → 991, otuz iki yeni kök + altı karşılık genişletildi)
bulgular/aday_bulgular.json (524 → 638)
betikler/blok_25_1_10.py · blok_25_11_20.py · blok_25_21_30.py ·
           blok_25_31_40.py · blok_25_41_50.py · blok_25_51_60.py · blok_25_61_70.py · blok_25_71_77.py · blok_26_1_20.py · blok_26_21_40.py · blok_26_41_60.py (YENİ)
```
