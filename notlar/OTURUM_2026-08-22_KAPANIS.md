# OTURUM KAPANIŞI — 2026-08-22

Bu oturumda **okuma yapılmadı.** İki iş yapıldı: ses/prozodi ölçümü ve
repo geneli anahtar denetimi. Okuma bir sonraki oturumda 20:1'den başlar.

---

## 1. NAKARAT PROZODİ SINAVI — KOŞULDU

Ön-kayıt: `notlar/ON_KAYIT_nakarat.md` (ölçümden ÖNCE yazıldı)
Betik: `betikler/nakarat_olcum.py` · Sonuç: `bulgular/bulgu_nakarat_prozodi.json`

Nesne: Sûre 55 (Rahmân), 78/78 ayet, ayet-ayet mp3 (everyayah),
kārî **Mahmûd Halîl el-Husarî (murattal)**.
Segmentasyon dosya sınırından geldi → hizalama hatası yok.

Sanity kontrolü GEÇTİ: 31 nakarat ayetinin `mora`=31 ve `ritim_kod` tek varyant.

**Birincil (mora başına süre CV oranı):**
| ölçü | CV(nakarat, n=31) | CV(kontrol, n=46) | oran | p |
|---|---|---|---|---|
| dpm (süre/mora) | 0,0364 | 0,1395 | **0,261** | <0,0001 |
| F0 | — | — | 0,577 | 0,016 |
| RMS | — | — | 0,583 | 0,0006 |

10.000 permütasyon, tek yönlü. **Sıralama: süre < perde/şiddet.**
Metnin en sıkı buyurduğu prozodik boyut SÜRE. Bu, `tilavet_sentez.py`'deki
"perde keyfî, süre metinden" ayrımını BAĞIMSIZ veriyle doğruluyor.

Nakarat 31 kez ort. 11,19 sn, sd 0,41, tüm yayılım %16,4.

**İkincil (POST-HOC, iddia değil):** sürüklenme — tekrar sırası ilerledikçe
süre +0,022 sn/tekrar (r=+0,49), F0 +0,387 Hz/tekrar (r=+0,25).
Sınanacaksa BAĞIMSIZ kārî/sûre gerekir; karşılaştırma **murattal-murattal**
olmalı (mujawwad'da sapmanın ne kadarı icra süslemesi ayırt edilemez).

Adaylar: **395, 396**

## 2. KAFİYE SESLENDİRME SETLERİ
`betikler/kafiye_seslendirme.py` → `ciktilar/kafiye_seslendirme/`
Çapraz tablo (aday **397**): kafiye sınıfı ile fâsıla tipi büyük ölçüde AYNI
şeyi ölçüyor — N %98,6 ârız, A %97,6 açık. Ayrışan tek sınıf **R** (335 ârız /
115 çarpık); kadans ile kafiye harfini ayırmak isteyen tasarım R'yi kullanmalı.

## 3. ANAHTAR DENETİMİ — İKİ AYRI HASAR
`betikler/anahtar_denetim.py` (SALT-OKUR, T1–T4), rapor:
`ciktilar/anahtar_denetim_raporu.txt`

- **`varlik_katalog.py`**: 91 kayıttan 9'u sessizce sıfır dönüyor (aday **398**)
- **`zaman_of()` kümeleri**: 34 anahtardan 18'i tutmuyor, 1.974 geçiş kaybı,
  iki dosyada kopyalı (aday **399**)

Ayrıntı ve tur-sonu düzeltme listesi: `notlar/YAPILACAKLAR.md`.

### Kapsam ölçüldü — okuma ETKİLENMİYOR
- `defter.py`/`defter2.py` yalnız `json, re, unicodedata, collections, kuran_akis`
  kullanıyor. `varlik_makinesi` ve `kavram_arac` okuma hattına GİRMİYOR.
- `defter.json`'daki `zmn` alanı `defter2.py` sat.51'de doğrudan morfolojiden
  (PERF/IMPF/IMPV) hesaplanıyor — `zaman_of()` ile İLGİSİ YOK.
- Tarama yapıldı: `okuma_metni.json`, `mercek_kayit.json`,
  `okuma_baglantilari.json` içindeki hiçbir "zaman" geçişi
  `varlik_katalog.json`'un `zaman` profiline dayanmıyor. Hepsi ya sıradan
  Türkçe ya morfolojik kip.
=> **1.138 ayetlik okuma tekrar edilmeyecek. Karşılaştırılabilirlik bozulmuyor.**

### NEDEN OLDU — tarih kanıtı
`varlik_katalog.py` 5 Ağustos'ta ilk toplu yüklemede geldi, o günden beri
BİR KEZ BİLE değişmedi (`قدr` hatası doğduğu gün içindeydi). Aradan 17 günde
246 dosya dokunuşu oldu, bu dosya hiçbirine dahil değil.
`turkce_denetim.py` **21 Ağustos**'ta yazıldı.
Kök tabloları korpustan TÜRETİLDİĞİ için temiz: `kok_envanteri` 1.651,
`kok_anlam_tablosu` 430, `kok_turkce` 314 → hepsinde SIFIR ihlâl.
**Bozulma denetim öncesi dönemin ürünü; kural ihlâl edilmedi, kuralın KAPSAMI
dışında bir dosya vardı.**

## 4. DÜZELTİLEN KENDİ HATALARIM (tur sonunda bunlara dayanılmasın)
1. `morph.txt` konum alanını 5 parçalı sandım — gerçekte **4 parçalı**
   (`sûre:ayet:kelime:segment`). "PN etiketi hiç yok, 36/36 düşmüş" demiştim,
   YANLIŞTI. Doğrusu: 3.911 PN kelime, 2.464 ayet, 106 PN lemma, 36'dan 4'ü düşüyor.
2. T3 testini "NFC'den sapma" diye tanımlayıp korpusu suçladım. Ölçüldü:
   korpusun ham hâli ZATEN NFC (shadda ccc=33 > damme ccc=31). Sapan taraf
   elle yazılan `أَيُّوب`. Ölçüt **"korpus formundan sapma"** olarak düzeltildi.
3. Devam noktasını 19:61 sandım — Sûre 19 TAM (98/98). Doğru nokta **20:1**.
   Kapsama %41 değil **1.138/6.236**. `ilerleme` alanı zaten doğruydu.

## 5. ANLATI MODU — AYRI PROJE, ERTELENDİ
Karara bağlananlar `YAPILACAKLAR.md` P1'de. Özet:
- **Süre katmanı Türkçe'ye DEVROLMUYOR** (mora Arapça'ya ait). Meal tarafında
  "ritmi metinden aldık" iddiası kurulamaz.
- Devrolan: anlatı yapısı — konuşan/muhatap (`sah`,`bask`), doğrudan söz
  (قول fiili 1.322 ayet), nakarat (119 ayet/15 sûre), edim, adlı aktör.
- Telif: `kuran_meal.json` repoda YOK, yerelde. Meal Claude'un çalışma
  çevirisidir (`okuma_metni.json` `sema.meal`). Yayım düşünülürse
  Elmalılı 1935 orijinali kamu malı.
- Türkçe TTS bu ortamda yok.

---

## SONRAKİ OTURUM: 20:1 (Tâhâ)
`OKUMA_STANDARDI.md` açılış promptu geçerli. Okuma sırasında araç
değiştirme YASAK — tüm düzeltmeler tur sonuna.
