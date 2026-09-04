# OTURUM KAPANIŞI — 2026-09-01

## Ne yapıldı

**Sûre 23 (Mü'minûn) TAM okundu (118/118)** ve **sûre 24 (Nûr) açıldı**: makro profil
+ 24:1-45. Okunan ayet **1463 → 1626** (korpusun %26,1'i).

Tam okunan sûreler: **1, 9-23**. Kısmi: 2 (1-20), 24 (1-45).

Kök tablosu **880 → 951** (71 yeni karşılık; hepsi `kok_envanteri.json`'dan NFC
eşlemesiyle KOPYALANDI). Adaylar **464 → 513**. Bağlar: `AC_muminun` 78, `AD_nur` 43.

## Denetimler

- `turkce_denetim.py` — her blok sonunda koşuldu, **on kez 0'a çekildi**.
  Üç geriye dönük onarım kümesi: 14:22 `لوم` *(kınama, levm)*, 9:6 `جور`
  *(komşuluk; sığınak verme, koruma)* ve sûre 9-12'de dokuz `برأ`
  *(uzak durma, berî olma; yaratma)* anması — yeni kök eklendiğinde eski anmanın
  karşılıksız kaldığı bilinen desen.
- `anahtar_denetim.py` (PYTHONHASHSEED=0, depo yapısında) **on kez** koşuldu.
  Her seferinde **58 ihlâl, taban listesiyle diff = 0**. Taranan anahtar
  21055 → 21604.

## İki sûrenin karşıtlığı — oturumun ana ölçümü

| | Mü'minûn (23) | Nûr (24) |
|---|---|---|
| tip | Mekkî | Medenî |
| ayet / kelime | 118 / 1050 | 64 / 1316 |
| ayet başına kelime | 8,90 | **20,56** |
| Allah | 13 = 0,35x | **80 = 1,74x** |
| Rab | 23 = 1,72x | **0** |
| kafiye sınıfı | 1 | 4 |
| esmâ / mühür | 12 / **0** | 62 / **12** |
| iltifât | 7 | **0** |
| yasak (edim) | 3 | 12 |
| adlı aktör | 9 | **1** |

**Sûre 24 korpusun en uzun sıfır-Rab sûresi** (aday 498) ve tam aynası korpusta
var: sûre 55 (Rahmân), Allah 0 / Rab 36.

## Açılan yeni P0

**Aday 487 — kaynak metin sorusu, projede İLK KEZ.** 23:85/87/89'un üçünde de
korpus `لِلَّهِ` okuyor; yaygın Hafs baskısında 23:87 ve 23:89 `ٱللَّهُ` merfûdur.
Sorular (`مَن رَّبُّ` · `مَنۢ بِيَدِهِۦ`) merfû cevap ister — korpusun okuyuşu iki
ayette soru-cevap uyumsuzluğu üretiyor. `nuzul.json` ile aynı statüde: doğrulanmadan
bu ayetlere dayanan bulgu kapatılamaz. **Tur sonu işi: korpusun kıraat tabanı.**

**Adaylar 484 + 497 — esmâ ölçütleri arası öncelik.** Aynı sözdizimsel konumdaki
sıfatlar farklı işleniyor (23:86 `ٱلْعَظِيمِ` sayılmıyor / 23:116 `ٱلْكَرِيمِ`
sayılıyor; üstünlük tamlaması üç örnekten yalnız birinde esmâ).

**Aday 501 — mühür sinyali iki yönden kanıtlı.** 23 (mühür=0 → hata %67) ve
24 (mühür=12 → mühürlü konumlar temiz).

## Ön-kayıt düzeltmesi (aday 476)

21:92-93 ↔ 23:52-53 bekleyen bağı ölçüldü ve **ön-kayıt yanlış çıktı**: "fark tam
olarak imperatifte" bekleniyordu, ölçüm iki fark verdi (açılışta bağlaç, kapanışta
imperatif). Ders YAPILACAKLAR'a yazıldı: bölüt ikizi taramasına **bağlaç** sınıfı
eklenecek.

## Mercek bilançosu

Sûre 23: 118 ayet, on altı ★★★, **on beşinde iki mercek de atlandı**; tek yazılan
mercek 23:86'nın 🜂 uzayı. **Biyolog merceği sûre 23'te hiç yazılmadı.**
Sûre 24 blok 1-20: üç ★★★, üçünde de iki mercek atlandı.

Adaylar 468 ve 472 artık tam bir sûre veri kümesine dayanıyor. **Uyarı:** şimdiye
dek yalnız KISA ayet yanlılığı ölçüldü; 24:31 (n=78) okunduğunda uzun ayet davranışı
da ölçülecek.

## Değişen dosyalar (zip'te depo yapısıyla aynı klasörlemede)

```
notlar/okuma_metni.json            (sûre 23 TAM + sûre 24 makro ve 1-20)
notlar/mercek_kayit.json
notlar/okuma_baglantilari.json     (AC_muminun 78, AD_nur 15)
notlar/YAPILACAKLAR.md
notlar/OTURUM_2026-09-01_KAPANIS.md   (bu dosya)
tablolar/kok_turkce.json           (880 → 928)
bulgular/aday_bulgular.json        (464 → 502; AE_muminun, AF_nur yeni)
betikler/blok_23_1_20.py … blok_23_101_118.py   (altı YENİ)
betikler/blok_24_1_20.py · blok_24_21_30.py · blok_24_31_40.py ·
                                   blok_24_41_45.py               (YENİ)
betikler/kok_ekle_23.py            (YENİ)
```

## Devam noktası

**Sûre 24, ayet 46.**

**ADAY 468'İN EN TEMİZ VAKASI (aday 512).** Sûre 24'te uzman merceği için çıpa
taşıyan üç ayet var ve yalnız biri eşiği tutuyor: 24:35 ★★★ (mercek yazıldı) ·
24:43 meteoroloji ★★ · 24:45 biyoloji ★. Sûrenin **biyolojik olarak en yoğun
ayeti ★ alıyor**, buna karşılık ★★★ alan on beş ayetin on dördünde çıpa yok.
Çıpa ile yıldız ters yönde ayrışıyor. **Tur sonu işi: önce ÇIPA TANIMI yazılmalı**
— şu an elle veriliyor ve ölçülebilir ölçütü yok.

**BİYOLOG MERCEĞİ SONUNDA YAZILDI (24:35).** Sûre 23 boyunca hiç çıpa bulunamamıştı;
Nûr âyetinde `زَيْتُونَة` *(zeytin ağacı)* ile ilk kez yazıldı ve sınırı açıkça
konuldu — ölçülen şey seçilen biyolojik değişkenin **ışık maruziyeti** olması,
bitki fizyolojisi değil. Uzay merceği de aynı ayette (`كَوْكَب` *(yıldız)*,
parlaklık karşılaştırması; gök modeli kurulmadı).

**YENİ P0 (aday 508):** 24:35'te esmâ `نُور` **beş kez** sayılıyor; sûredeki yedi
`نُور` tokeninin tamamı 24:35 ve 24:40'ta ve **altısı yanlış pozitif** (iyelikli
×3, nekre ×3). Tek ayette ölçülen en yoğun esmâ hatası.

**YENİ P1 (aday 509):** sûrenin azınlık kafiye sınıfları **tek bitişik kuşakta**
(24:36-45, on ayet), ve kuşak Nûr âyetinin hemen ardından açılıyor.

**ADAY 472 DÜZELTİLDİ (aday 503).** Sûre 24, "yıldız formülü kısa ayete kayıyor"
iddiasını yanlışladı: 15 ★★★'ın beşi **n kaynaklı** ve uzunlukları n=78 · 76 · 49 ·
48 · 48. Formül uzunluğu değil, **ortalamadan sapmayı** seçiyor. Aynı ders ikinci
kez de düştü: aday 500'ün "mühür ↔ cevapsızlık" örüntüsü dördüncü örnekte bozuldu
(aday 505). Kalıp iddiaları, kalıbın sûredeki tüm geçişleri sayılmadan
kaydedilmeyecek.

**24:35 uyarısı:** Nûr âyetinde hem biyolog hem uzay merceği için ilk kez gerçek
çıpa var (`زَيْتُونَة` *(zeytin ağacı)*, `كَوْكَب` *(yıldız)*); ayrıca `نُور` *(nûr)*
kökü altı kez ve esmâ tablosu beşini esmâ sayıyor — aday 461 için büyük vaka.

Açık borçlar (435+452+474 tek geçişte, 461+467+484+497+501,
451, 462, 431, 437, 443, 438+483, 472+468, 487) bu oturumda da ONARILMADI —
katı kural gereği.
