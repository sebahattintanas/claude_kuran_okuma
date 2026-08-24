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
4. notlar/ altındaki EN SON OTURUM_*_KAPANIS dosyasını oku — önceki
   oturumun durumu, açık borçlar, düzeltilmiş hatalar
5. notlar/okuma_metni.json oku — buraya kadarki okumanın kaydı
6. bulgular/aday_bulgular.json oku — açık adaylar

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
   Alan sırası **sabit**, atlanan alan yazılmaz ("aktör yok" gibi bir satır
   ancak dikkat çekiciyse konur):
   1. **eksen** — Allah lafzı konumları · Rab · esmâ ve konumu (mühür/orta)
   2. **aktör** — adlı / adsız / rol
   3. **kip ve söz edimi** — edim · kip
   4. **şahıs ve iltifât** — şahıs dağılımı · ilt ve yönü
   5. **sözlük ve biçim** — n · mora · harf · fâsıla · i'râb · bab · edilgen ·
      kök ikilemesi · hapaks · sayı sözcüğü · biçim etiketi · simetri
   6. **bağ** — xref · elle kurulan bağlar
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
ya da indeks üzerinden erişilir. Bu kural **DÖRT kez** ihlal edildi ve dördü de
sessiz hataya yol açtı — hiçbiri hata vermedi, hepsi sıfır sonuç döndürdü:

1. `aktor.py` v1 — elle yazılan `ٱللَّه`, korpustaki `اللَّه` ile eşleşmedi;
   2989 token yanlış sınıflandı.
2. (ikinci vaka, önceki kayıt)
3. `betikler/varlik_katalog.py` — 91 kayıttan 9'u düşüyor: `قدr` içinde Latin
   `r` (U+0072) · `امن`/`ارض`/`امر` + `ياجوج|ماجوج` deseninde hemzesiz elif ·
   `أَيُّوب`'ta hareke sırası korpusun tersi. Ölçülen kayıp 1.722 geçiş.
   (aday 398)
4. `betikler/varlik_makinesi.py` sat.48-50 ve `betikler/kavram_arac.py`
   sat.46-48 — `zaman_of()` kümelerinde 34 anahtardan 18'i tutmuyor.
   `ءمن`/`ايي`/`اخر`/`امر` = 1.974 geçiş kaybı; ayrıca 14 anahtar özel/cins
   isim olduğu hâlde kök tarafında aranıyor. (aday 399)

**KURALIN KAPSAMI GENİŞLETİLDİ (2026-08-22).** Önceki hâli yalnız `.json`
tablolarını kapsıyordu; oysa 3. ve 4. ihlâl **`.py` dosyalarına gömülü
sabitlerde**. Kural artık her iki dosya türünü de kapsar.

**Denetim betiği: `betikler/anahtar_denetim.py`** (SALT-OKUR).
Dört test: T1 Latin sızması · T2 yazım/hemze · T3 korpus formundan sapma ·
T4 korpusta yok. `.json` anahtarlarını VE `.py` sabitlerini tarar.

Ölçüt **"NFC'den sapma" DEĞİL, "KORPUS FORMUNDAN sapma"**. Korpusun ham hâli
zaten NFC'dir (shadda ccc=33 > damme ccc=31); sapan taraf her zaman elle
yazılan anahtardır.

Betiğin düzeltme önerileri **körü körüne uygulanmaz** — hamze-varyantı
denemesi yanlış öneri üretebiliyor (`ثمد → أمد`, `قيم → أيم` hatalıydı).
Her öneri elle doğrulanır.

Kök tabloları korpustan TÜRETİLDİĞİ için temizdir ve öyle kalmalıdır:
`kok_envanteri` 1.651 · `kok_anlam_tablosu` 430 · `kok_turkce` 314 →
üçünde de sıfır ihlâl.


---

## 2026-08-20 — BİÇİM KURALI EKLENDİ: Arapça terimlerin Türkçe karşılığı

Ölçüm ve mercek metinlerinde geçen HER Arapça sözcük/tamlama, hemen ardından
italik parantez içinde Türkçe karşılığıyla verilir.

    doğru:  `نُفُورًۭا` *(kaçış, ürküp uzaklaşma)*
    doğru:  `صَرَّفْنَا` *(türlü türlü açıkladık)* — bab II, çeşitlendirme
    yanlış: `نُفُورًۭا` (karşılıksız bırakmak)

Kapsam: ayet ölçüm satırları, mercek metinleri, dikey okuma özetleri,
aday_bulgular kayıtları ve okuma_baglantilari notları.
**İSTİSNA YOKTUR.** Önceki sürümdeki "üç harfli kökler muaf" maddesi
2026-08-21'de KALDIRILDI: o boşluktan geçilerek 1094 kök anması karşılıksız
kalmıştı. Kök adları da her geçişte karşılık alır.
Gerekçe: metin Türkçe okunuyor; Arapça terim karşılıksız kaldığında ölçüm
kaydı sonraki oturumlarda yeniden okunabilir olmuyor.


---

## 2026-08-21 — BİÇİM KURALI DENETİME BAĞLANDI

Kural artık niyete değil betiğe bağlı:

- `tablolar/kok_turkce.json` — 314 kök → Türkçe karşılık tablosu
  (2026-08-22 sayımı; tablo büyüdükçe bu rakam güncellenir)
- `betikler/turkce_denetim.py` — karşılıksız kök anmalarını listeler, ihlâl
  varsa çıkış kodu 1 döndürür

**Her blok kaydından sonra `python3 turkce_denetim.py` koşturulur ve
çıktı SIFIR olmadan blok kapatılmaz.**

Geriye dönük onarım: sûre 15-19 arasında 1169 (okuma_metni) + 105 (bağlantılar)
+ 153 (adaylar) = 1427 karşılık eklendi. Yeni kök geçtiğinde önce
`kok_turkce.json`a eklenir, sonra kullanılır.


---

## 2026-08-22 — ANAHTAR DENETİMİ ZİNCİRE BAĞLANDI

`turkce_denetim.py` gibi, `anahtar_denetim.py` de niyete değil betiğe bağlı:

**Boru hattı koşulduktan sonra VE elle yazılmış herhangi bir anahtar
dosyasına dokunulduğunda `python3 betikler/anahtar_denetim.py` koşturulur.**
Yeni ihlâl çıkarsa okuma durur; ihlâl kaydedilir ve düzeltme tur sonuna
yazılır (okuma sırasında ARAÇ DEĞİŞTİRİLMEZ).

Bilinen ve ERTELENMİŞ ihlâller (aday 398, 399) her koşuda çıkacaktır —
bunlar beklenen çıktıdır, okuma durdurmaz. Yeni bir ihlâl belirirse durdurur.

Muafiyetler gerekçeli tutulur:
- alt çizgi sonrası Latin etiket kasıtlıdır (`kavram_sozlugu.json`: `سمو_tekil`)
- `EDAT_MUAF` listesi: ham metinde aranan parçacıklar (`أما`, `فأما`, `وأما`,
  `كلا` …) kök envanterinde OLMAMASI normaldir
Liste körlemesine genişletilmez; her ekleme gerekçesiyle yazılır.

### Okuma hattı bu hasardan ETKİLENMİYOR — ölçüldü
`defter.py` / `defter2.py` yalnız `json, re, unicodedata, collections,
kuran_akis` kullanır; `varlik_makinesi` ve `kavram_arac` okuma hattına
GİRMEZ. `defter.json`'daki `zmn` alanı `defter2.py` sat.51'de doğrudan
morfolojiden (PERF/IMPF/IMPV) hesaplanır — `zaman_of()` ile ilgisi yoktur.
Tarama yapıldı: `okuma_metni.json`, `mercek_kayit.json`,
`okuma_baglantilari.json` içinde `varlik_katalog.json`'un `zaman` profiline
dayanan çıkarım YOK.

**`tablolar/varlik_katalog.json`'un `zaman` alanı tur sonu onarımına kadar
GÜVENİLMEZDİR; bu alana dayanan bulgu kurulamaz.**
(`nuzul.json` maddesiyle aynı statüde.)
