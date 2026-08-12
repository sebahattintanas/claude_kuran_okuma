# OKUMA STANDARDI — sonraki oturumlar için açılış promptu

> Bu dosya bir **prompt**tur. Yeni bir oturum açıldığında bu metin Claude'a
> verilir ve okuma bu düzende sürer. Depoda `README.md` içinde de bulunur.

---

## AÇILIŞ PROMPTU (kopyala-yapıştır)

```
Kur'an derin okuma projesine devam ediyoruz. Depo:
github.com/sebahattintanas/claude_kuran_okuma

İlk iş:
1. git clone; betikleri sırayla koştur:
   defter.py → defter2 → defter3 → defter4 → defter5 → aktor2 → katman6 → graf2
   (~3 dk, defter.json'u sıfırdan kurar — 6236 ayet, 39 alan)
2. notlar/okuma_protokolu.json oku — sekiz kilitli karar
3. notlar/OKUMA_STANDARDI.md oku — okuma düzeni ve biçim kuralları
4. notlar/okuma_metni.json oku — buraya kadarki okumanın kaydı
5. bulgular/aday_bulgular.json oku — açık adaylar

Sonra kaldığımız yerden devam et. Devam noktası okuma_metni.json'un
"ilerleme" alanında yazılı.

KATI KURAL yürürlükte: okuma sırasında hiçbir hipotez test edilmez.
Her gözlem aday listesine yazılır; test tur sonunda toplu yapılır.
```

---

## OKUMA DÜZENİ

### Blok akışı
- **20 ayetlik bloklar.**
- Her sûrenin başında **makro profil**, sonunda **kapanış ölçümü**.
- Makro profil şunları içerir: ayet/kelime sayısı · Allah ve Rab yoğunlukları
  (korpus ortalamasıyla karşılaştırmalı: Allah 0.0349, Rab 0.0127) · söz edimi
  dağılımı · kafiye sınıfı · esmâ yoğunluğu ve çiftleri · tam-ayet ikizleri ·
  Allah-sessizlikleri · aktör listesi · yıldız dağılımı · en uzun/kısa ayetler.

### Ayet başına üç katman
1. **`›` Ölçüm** — defterden gelen sayılar + elle kurulan bağlar.
2. **`◇` Matematikçi merceği** — yapısal okuma. Kalıcı katman.
3. **Dikey okuma** — kökün Allah eksenine mesafesi, konum-eşli null ile.

Biyolog ve uzay bilimci mercekleri **yalnız yıldızlı (★★★) ayetlerde**.

### Mercek kuralı
Her `◇` satırı **görünür bir dilsel öğeye bağlı olmalı**. Silme testi:
merceği sil, ölçüm ayakta kalmalı. Kalmıyorsa mercek ölçüme sızmıştır.

---

## BİÇİM KURALLARI

### 1. Arapça + Türkçe — istisnasız
Metinde geçen **her** Arapça ifadenin yanında Türkçesi olacak, italik ve
parantez içinde:

> `فَبِأَىِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ` *(Rabbinizin hangi nimetlerini yalanlıyorsunuz)*

Tek kelimelik kök adları da dahil:

> `صوب` *(isabet)* · `لقي` *(atma)* · `شبه` *(benzeşme)*

**Karşılıksız Arapça bırakılmaz.** Kök adı bilinmiyorsa "kök" diye anılır.

### 2. Arapça görünürlüğü
Arapça ifadeler dar aralıklarda sıkışıyor. Bunun için:
- Ayetin **tam metni** ayrı satırda, blok alıntı olarak verilir — satır içinde değil.
- Uzun ifadeler (4+ kelime) satır içinde değil, **kendi satırında**.
- Kısa ifadeler (1–3 kelime) satır içinde kalabilir ama arkasından hemen Türkçesi gelir.
- Aynı satırda **üçten fazla Arapça ifade** yığılmaz; gerekiyorsa madde işaretine bölünür.

### 3. Meal
Claude'un **çalışma çevirisi**. Diyanet meali değildir, referans olarak
kullanılamaz. Kalın yazılır, ayetin hemen ardından.

### 4. Ölçüm ve yorum ayrımı
`›` satırı ölçüm, `◇` satırı yorum. **Karışmaz.** Ölçüm satırında yorum
cümlesi kurulmaz; mercek satırında yeni sayı verilmez.

### 5. Tablo kullanımı
Karşılaştırmalı sayılar (sûre profilleri, esmâ çiftleri, kural dağılımları)
tabloya konur. Düz metinde sayı yığmak yerine tablo tercih edilir.

---

## KATI KURAL

Okuma sırasında **hiçbir hipotez test edilmez**. Dikkat çeken her şey
`bulgular/aday_bulgular.json`'a yazılır. Test tur sonunda toplu Bonferroni ile.

**Kayıtlı uyarı:** bazı adaylar okuma sırasında sayıldı — yani aranarak bulundu.
Tur sonunda "N örnek var" diye değil, **"aranarak bulunmuş N örnek"** diye işlem
görecekler; testleri, motive eden ayetler dışlanarak kurulacak.

---

## KALICILIK — her blok sonunda

| dosya | ne tutar |
|---|---|
| `notlar/okuma_metni.json` | okumanın kendisi (meal + bağlar) |
| `notlar/mercek_kayit.json` | `◇` satırları |
| `notlar/okuma_baglantilari.json` | elle kurulan bağlar, kural kodlu |
| `bulgular/aday_bulgular.json` | adaylar |
| `ciktilar/defter.json` | ölçüm katmanı — betiklerden üretilir, elle yazılmaz |

**Sûre 9'dan itibaren** `okuma_metni.json` TAM kipte yazılır (ar + meal + ölçüm
+ mercek), okurken — sona bırakılmaz. Sûre 1 tam, 2–8 sıkıştırılmış blok özeti.

---

## ÖLÇÜM BORÇLARI (her oturumda hatırlanacak)

- `esma_listesi.json` bağlam ayırmıyor — dört istisna: `جَبَّار` (5:22, kavim),
  `بَرّ` (5:96, 6:59, 6:97 = kara), `عَلِيم` (7:109, 7:112 = sihirbaz)
- `ربب` türevleri Rab sayılıyor: 4:23 `رَبَٰٓئِب` *(üvey kız)*, 3:79/5:44/5:63
  `رَبَّٰنِيُّون`, 3:146 `رِبِّيُّون` → **Nisâ'nın Rab sayımı 7 değil 6**
- `جنن` tablo hatası — 7:184 `جِنَّة` *(delilik)* ama tablo "cennet" veriyor
- `kok_adlar.json` görüntü katmanı `kavram()` kullanmıyor
- `nuzul.json` **bellekten, doğrulanmadı** — bu alana dayanan bulgu kurulamaz
- Ayet grafında nakarat düzeltildi, **iç-bağ ağırlıklandırması yapılmadı**
- **Kontrol korpusu (Kur'an dışı Arapça) YOK — projenin en büyük eksiği**

---

## LEMMA ANAHTARI KURALI

**Arapça lemma anahtarları asla elle yazılmaz.** Korpus çıktısından kopyalanır
ya da indeks üzerinden erişilir. Bu kural iki kez ihlal edildi ve iki kez
sessiz hataya yol açtı (en sonuncusu: `aktor.py` v1'de 2989 token yanlış
sınıflandı, çünkü elle yazılan `ٱللَّه` korpustaki `اللَّه` ile eşleşmedi).
