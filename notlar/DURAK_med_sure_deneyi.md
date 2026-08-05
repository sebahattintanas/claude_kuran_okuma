# DURAK — Med-Süre Değişmezlik Deneyi
*Yarın kaldığımız yer. Soğuk başlasak bile buradan devam.*

---

## ŞU AN NEREDEYİZ (tek cümle)
Boru hattı kuruldu, kurulum sınandı, veri hazır — **sıradaki tek iş: betiği koşup çıktıyı okumak.**

## HEMEN YAPILACAK (masaüstüne dönünce ilk adım)
Merdivenin EN ÜSTÜNÜ önce koş (sesli-kimliği / formant — hizalama anahtarı):
```
cd "C:\Users\sebahattin.tanas\Desktop\Kuran Analiz"
pip install scikit-learn
python formant_top_rung.py
```
Çıktıda TEK önemli satır: **AZINLIK (î/û) uyumu**. Genel uyum %78 çıkarsa bu 'hep â'
tabanıdır, anlamsız. Asıl sinyal î/û'nun karîler-arası tutarlı + metinle uyumlu
geri-üretilmesi. Şu iki satırı al:
- `1) KARÎ ↔ METİN` (genel + AZINLIK)
- `2) KARÎLER-ARASI DEĞİŞMEZLİK` (genel + azınlık-içeren)

Sonra (bu geçerse) süre katmanı:
```
python med_sure_degismezlik.py
```
`ort CV`, `ort profil-DTW`, `r=... p=...` satırlarını al.

ALTERNATİF (masaüstü olmadan): Kāf'ın iki karîsinden birkaç mp3'ü (örn. 050001,
050002, 050005) sohbete YÜKLE — Claude burada doğrudan koşup çıktıyı versin.

## KURULUM DURUMU (hepsi ✓)
- ffmpeg kuruldu; `librosa.load(...mp3)` → **mp3 OK** (ses tarafı çalışıyor).
- Python 3.14 + librosa/soundfile/scipy/numpy kurulu.
- Veri: `audio/1` ve `audio/2` = **iki farklı karî**, ikisi de **Kāf (50) tam**, 45 ayet.
- Betik ayarlandı: `RECITERS={kari1:audio/1, kari2:audio/2}`, `TEST_AYETLER=Kāf 1..45`.
- Dosya adı kalıbı `050001.mp3` = `{sure:03d}{ayet:03d}` (betikle uyumlu).

## DOSYALAR (çalışma klasöründe olmalı)
- `formant_top_rung.py`      — YENİ: merdivenin en üstü (sesli-kimliği/formant). ÖNCE bunu koş.
- `med_sure_degismezlik.py`  — süre katmanı v2 (Kāf + 2 karî ayarlı)
- `kuran_veri.json`          — **koşarken bunu kullan** (zenginleştirilmiş: med_yuku/mora_profil/med_tipleri)
- `kuran_veri_pretty.json`   — yalnız gözle incelemek için (editörü kilitlemez)

## BUGÜN EKLENEN (formant / en-üst rung)
- Kaynak–süzgeç fiziği: 0110'un "nefes–gövde–gövde–nefes" okuması, kaynak-süzgeç
  kuramının ta kendisi (inşâ metaforun MUHKEM fiziksel karşılığı). Yine de bu,
  "Kuran'a özgü" iddiasını diriltmez — metne-bağlı özellikler Arapça'nındır.
- Sesli kimliği = merdivenin en üstü: fonemik, karîden ~bağımsız olmalı. Değeri:
  (a) köprüyü DOĞRULAR, (b) süre-ölçümüne HİZALAMA verir (isimli medler).
- LPC formant kestirici KURULDU + sentetikte doğrulandı: 11 kHz'e indir, order 14;
  kırılgan F2 yerine **F1 (açık/kapalı) + HFR>1800Hz (ön î / arka û)**.
- Uçtan uca sentetik test: iki sahte karî (farklı perde/tempo/+%6 formant) planlanan
  â/û/î dizisini **%100** geri-üretti, birbirine+metne %100 hizalandı.
- Kāf metin-ayağı hazır: uzun-sesli dağılımı **â %78 · î %14 · û %8** (n=333).
- DÜRÜSTLÜK: â %78 → "hep â" %78 tutturur; asıl test AZINLIK (î/û). Betik ayrı verir.
- mp3 RİSKİ: düşük bitrate yüksek-frekansı keser → HFR bozulur → î/û ayrımı zorlaşabilir.

## OKURKEN AKILDA TUTULACAK (dürüstlük)
1. **Eşikler 8 karî içindi.** 2 karîde CV doğal olarak daha oynak → sayıya bak, ✓/✗ etiketine değil.
2. **Bu yalnız 1. kapı** (değişmezlik). Geçse bile "Kuran'a özgü mü?" sorusu **2. kapıyı** ister:
   aynı iki karînin **Kuran-dışı makamlı** okuması ile kontrol. O ses henüz yok.
3. Ses ölçümü fonem-hizalaması yapmaz: "hangi med" değil, **"uzun tutulan yer nerede"** der.

## SONUCA GÖRE ÇATAL
- **Değişmez + metin öngörüyor** → süre-imzası metne ait; sezgi (ayetin sesi) 1. kapıyı geçti → kontrol korpusuna geç.
- **Değişken / öngörmüyor** → performans; ölçümü sıkılaştır (F0 katmanı ekle) ya da daha çok karî indir (everyayah 8 karî).
- Ölçüm gürültülüyse: çekirdek-ölçümünü "sürekli seslendirilmiş + sabit-perde bölge" olarak rafine et.

---

## ARKA PLAN — buraya nasıl geldik (kısa)
- **Turn 1:** ses/söz insan ucunda; "kun"un sesliliği = gayb; fHz/ses ipliği tilâvete (geri-okuyuş) oturtuldu.
- **Bit katmanı:** 0110-çekirdeği +%20,3 (kompozisyon-kontrollü, z≈27) — gerçek. Makas 0110↑/0111↓; sûre bazında en keskin An-Nebe' (+78,9), ters uç Fecr (−68,2) → **fâsıla/kafiye** izliyor. Zarfı açan baskın harf **elif** (sadık alt-kümede taban %58 → açıcı %62/%70).
- **Geri-çözüm:** depolanmış `bits` yazıdan değil **tecvîdli tilâvetten** türetilmiş (tenvin=nûn ama idgamda düşer; kelime-arası idgam ünsüz eritir). Tam bit-sadakati = tecvîd motoru işi.
- **KRİTİK KONTROL:** aynı kodlama Buhârî hadisine uygulandı → 0110 +%14,9 (**Kuran +%12,5'in üstünde**), elif-baskınlığı aynı. **Sonuç: 0110 ve elif bulguları Kuran'a değil, ARAPÇA'ya ait.** "Bit yapısı Kuran'ı gösteriyor" çıkış noktası doğrulanmadı.
- **Sezgi yeniden konumlandı:** `fHz` alanı fiziksel frekans değil (600×4.33^oran, döngüsel inşâ). Gerçek frekans tilâvetin sesinde (F0/formant/**süre**). Sezginin çürütülebilir hâli: **karî-değişmezliği.**
- **Seçim:** ilk katman = **med-süre** (F0'dan gürbüz). Boru hattı yazıldı, sınandı → bu durak.

## PROZODİ HARİTASI (sessiz, metinden — ayrı bir iş kolu)
Öngörücü tamamlandı: gövde ritmi + **fâsıla kadansı** (med-i ârız). JSON'a eklendi:
`mora_profil_waqf`, `med_yuku_waqf`, `fasila_tipi` (açık/ârız/çarpık/ıvaz).
- Âyet-içi ritim zarfı: gövde akar, fâsıla'da YÜKSELİR (son bölge 1,37→1,64) = kadans.
- Fâsıla tipleri (tüm Kuran): **ârız %74 · açık %20 · çarpık %6 · ıvaz %0**.
  => âyetlerin %94'ü UZUN kadansla iniyor. (Kuran-biçimsel; düzyazıda yok. Ama
     tuğlalar Arapça'nın; gerçek sınav secî'li Arapçaya karşı olurdu.)
- İKİ NABIZ (ort mora/ayet, dosyalar outputs'ta):
  * `kuran_nabiz.png`        — MUSHAF sırası: uzun açılış → kısalan kapanış (ilk yarı 83, son 47)
  * `kuran_nabiz_nuzul.png`  — NÜZUL sırası: kısa/vurucu ilk vahiyler → uzun geç dönem
    (Mekkî ort 51 → Medenî 108). Mushaf'ın ~tersi. Bilinen Mekkî→Medenî üslûp
    kaymasıyla örtüşüyor (uydurma değil, tanınan olgunun ölçümü).
- Nüzul sırası: Tanzil/Kahire standardı; Mekkî/Medenî ile çapraz-doğrulandı (0 hata).
  Nöldeke farklı sıralar (rekonstrüksiyon; tek doğru yok).
- DÜRÜST SINIR: "mora/ayet" büyük ölçüde âyet-uzunluğunun vekili; gördüğümüz onun
  ritmik ifadesi. Keyfî değil ama devrim de değil.

## BUGÜN (imza çözümlemesi — SES sezgisinin son sınavı)
Soru: "her ayetin okuyucudan bağımsız bir ses-imzası var mı?"
- formant_top_rung.py (sesli-kimliği): HİZALAMADA ÇÖKTÜ. Metin↔ses uyumu tabanın
  ALTINDA (â %78 metin, ses %38-54 üretti), karîler-arası azınlık uyumu %38 (rastlantı).
  Sebep: segment≠med hizalaması + mp3 HF kaybı (HFR bozulur).
- med_sure_degismezlik.py (süre): DEĞİŞMEZLİK güçlü görünüyor (CV 0.06, karî-DTW 0.61)
  AMA metin-öngörüsü tutmadı (şekil-uyumu boş-modelle aynı, r=-0.26).
- imza_nedir.py (4 özellik × boş-model): KESİN CEVAP. Hiçbir özellikte ayete-özgü imza yok.
  enerji aynı0.87/farklı0.86 · süre 0.63/0.57 · F0 0.67/0.63 · tını 0.81/0.74.
  Yüksek "aynı" + yüksek "farklı" = imza değil; karî A'nın bir ayeti B'nin RASTGELE
  ayetine de benziyor. Yani "değişmezlik" ayet-ayrımı yapmıyor — sadece tilâvet
  üslûbunun genel dokusu (boş-model bunu ele verdi, hadis dersi gibi).
- SONUÇ: "ayete-özgü ses-imzası" sezgisi bu veride DESTEKLENMEDİ. Elenen zincir tam:
  bit=Arapça · fHz=keyfî · formant=hizalama çöktü · süre/ezgi=ayete-özgü değil.
  Başarısızlık değil, disiplinli eleme. Açık kalan: KONTROL (Kuran-dışı makamlı Arapça).
- Yeni dosyalar: formant_top_rung.py, imza_nedir.py, güncel med_sure_degismezlik.py.

## YARIN — YENİ ODAK: "SESİN YOLCULUĞU"
Kuran'da farklı KONUŞUCULARIN sözü var: melek (Cebrail/vahiy), insan (dua, tilâvet,
peygamber sözü), İblîs/şeytan (vesvese), Allah kelâmı. Bunlar metinde işaretli (çoğu
"kâle/kul/... dedi" ile). Fikir: bu SÖZ-KATMANLARINI ayırıp bizim ses-fiziğimizle
(mora, med, fâsıla, prozodi) kesiştirmek — "kimin sözü, nasıl bir ses dokusu taşıyor?"
- ör: melek sözü mü, insan yakarışı mı, şeytan vesvesesi mi — prozodik parmak izleri
  farklı mı? (özne/cümle-tip etiketi yalnız 44 ayette dolu; genişletme gerekir —
  mealden "dedi/de ki/rabbenâ" gibi imlerle proxy kurulabilir, hadis-dersiyle dikkatli.)
- Bu, ses ipini "insan ucunda" bırakıp (turn 1) farklı konuşucuların sesine taşır:
  55:4 "ona beyânı öğretti" ekseni — konuşmanın kime, nasıl verildiği.
- DÜRÜSTLÜK aynı: proxy etiket çeviriden gelir; boş-model + kontrol şart.

## KAVRAMSAL MODEL (bu deneyden bağımsız, el değmemiş)
"Kuran nasıl düşünür" işi — on-kavram alanı, aynalar, zıt-çiftler — bit/fHz katmanına dayanmıyordu; bu çöküş onu teğet geçmiyor. İstenirse oraya da dönülebilir.
