# OTURUM KAPANIŞI — 2026-09-04 (SON)

> Bu oturumun erken bölümünün kapanış notu `OTURUM_2026-09-04_ARA.md` dosyasında
> korunmuştur (sûre 25 açılışı ve sûre 26'nın ilk blokları).

## Durum

| | değer |
|---|---|
| Okunan ayet | **1969 / 6236 (%31,6)** |
| Tam okunan sûreler | **1, 9-26** |
| Kısmi | sûre 2 (1-20/286) · **sûre 27 (1-20/93)** |
| Aday bulgu | **799** (`AF_suara` 255 · `AH_neml` 20, yeni öbek) |
| Bağ | `AF_suara` **192** · `AG_neml` **19** (yeni öbek) |
| `kok_turkce.json` | **1017 kök** |
| `turkce_denetim.py` | **0 ihlâl** |
| `anahtar_denetim.py` | 58 ihlâl · **taban ile diff = 0** (21686 anahtar) |

## Bu oturumda yapılanlar

- **Sûre 26 (Şuarâ) TAMAMLANDI** — 26:21'den 26:227'ye, yirmi bir blok.
- **Sûre 27 (Neml) açıldı** — makro profil + 20 ayet.
- Adaylar **614 → 799** (185 yeni); bağlar `AF_suara` 15 → **192**.
- Kök tablosu **985 → 1017** (32 yeni kök).

---

# SÛRE 26 KAPANIŞ BİLANÇOSU

| ölçüm | ham | **nakarat düzeltmeli** |
|---|---|---|
| ★★★ payı | 41 (%18,1) | **25 (%11,9)** |
| esmâ token | 51 | ≈29 |
| iltifât | 15 | ≤11 |
| mühür | 10 | **3** |
| `esit` dolu ayet | 44 | çok daha düşük |
| kök sayımı örn. `طوع` | 9 | **2** |

**Nakarat envanteri:** altı küme, **34 standalone + 2 gömülü = 36 ayet (%15,9)**.
**Altı ölçüm birden şişmiş.**

**41 ★★★'ın 40'ında çıpa yok.** Çıpası olan tek ★★★ 26:63 ve o da yıldızını
hapakstan alıyor.

**En temiz gösterim (aday 768):** 26:217'de `عَزِيز|رَحِيم` mühür çifti nakarat
dışında geçiyor ve **yıldızsız** — sekiz nakarat geçişinde ★★★'tı. **Fark tek:
Rab varlığı. Yani sekiz ★★★'ın kaynağı esmâ değil, Rab oranıydı.**

**Dört kafiye kırılmasının dördü de `إِسْرَٰٓءِيلَ`** (aday 751) — kırılma adın
son harfine bağlı; "anlamlı vurgu" yorumu düştü.

# SÛRE 27 — SÛRE 26'NIN DOĞAL KONTROLÜ

| ölçüm | 26 | 27 |
|---|---|---|
| ort. kelime | 5,81 | **12,38** |
| A/R | **0,36** | **2,25** (okumada ilk kez >1) |
| nakarat ayet | 36 | **0** |
| `esit` dolu | 44 | **3** |
| kafiye kırılması | 4 | **0** |
| iltifât | 15 | **3** |
| mühür / bağımsız | 10 / 3 | 6 / **6** |
| ★★★ payı | %11,9 (düzeltmeli) | **%9,7** (düzeltme gerekmiyor) |

**Kontrollü karşılaştırma için ideal çift: kısa/uzun ayet, nakaratlı/nakaratsız.**

---

# P0 BORÇLAR — TUR SONU ONARIM EVRESİ

## 1. Ölçüm alanlarının ortak tasarım hatası (aday 765)

**Dört alan aynı hatayı taşıyor: hiçbiri lemma + bağlam denetimi yapmıyor.**

| alan | hata | vaka |
|---|---|---|
| aktör | kök eşleşmesi | `نُفُورا`→nefer (462/579) · `فِرْقٍ`→ferîk (641) |
| esmâ | lemma listesi, gönderge yok | `مُؤْمِن` sûre 26'da 15/15 artefakt (682/709) |
| sayı | kök eşleşmesi | `عَشِيرَة`→"on" (765) |
| dikey (529) | kök düzeyi | sûre 26'da 17 sûre-içi vaka |

**Esmâ gönderge sınıfları envanteri gerekli** (aday 747): ilâhî / insan /
**melek** / soyut kavram / yapı / makam — her sınıf için hüküm yazılacak.

## 2. Dikey katmanın sınırı (689/694/729/735/776/790/796)

**Seyrek kökler tek bir sahnede kümelendiğinde zenginleşme katı yüzlerle
ölçülüyor ve istatistiksel olarak anlamsız.** Sûre 26'da dokuz vaka, sûre 27'de
şimdiden üç.

En uç: `تسع` ×948,5 (kaynak 38:23) · `كيل` ×661,4 · `قسطس` ×554,4 ·
`ودي` ×534,8 · `نمل` ×520,0 · `مطر` ×502,7.

**27:18 doğrudan doğruladı:** üç kök kilitli (`ودي`↔`نمل`↔`سكن`) ve üçü tek
ayette.

**Zorunlu: "bir kökün geçişlerinin kaçı aynı sahnede" alanı. Bu alan olmadan
n≤25 köklerin dikey satırları KULLANILAMAZ.**

## 3. `esit` alanı — yedi eşik türü sınama vakalarıyla hazır

| eşik | sınama vakası |
|---|---|
| `esit_tam` (mevcut) | 26:32-33=7:107-108 · 27:3=31:4 |
| `esit_yakin` (n−1) | 25:66≈25:76 · 26:64≈26:66 · 26:66≈26:120 |
| **n−2** | 26:116≈26:167 (yalnız iki kelime farklı) |
| `esit_yapi` (iskelet) | 26:90≈26:91 · 26:64·66·172 üçlüsü |
| **k-ardışık** | 26:154≈26:186 (4 kelime) · 25:68≈26:213 (5 kelime) |
| **gömülü/kısmi** | 26:139 · 26:158 (nakarat gömülü) |
| **xref yoğunluğu** (otomatik) | 27:10 (6/6→28:31) · 27:19 (8/9→46:15) |

## 4. `nakarat` alanı yeniden tanımı (707/715/739/779)

- **Gömülü nakaratı kaçırıyor** (26:139, 26:158) — sayım 6 değil 8.
- **Eşik tanımsız:** iki üyeli küme (26:153/185) nakarat mı?
- **Sûre 26'nın altı ölçümü nakarat düzeltmeli yeniden hesaplanacak.**

## 5. 529 kümesi — üç katmanlı onarım

| katman | çözdüğü | vakalar |
|---|---|---|
| bab | çoğu | `صرف`·`قرن`·`رجو`·`طلق`·`سوي`·`قلب` |
| lemma | isim-kalıplı | `جنن`·`صلح`·`جبل` |
| **bağlam** | aynı lemma iki anlam | `أيي`·`خلق`·`لسن`·`نظر`·`قوم`·`ذكر`·`طوع` |

**En geniş vaka: `قوم` — dört anlam alanı tek sûrede** (n=660).

**Otomatik tespit ölçütü adayı** (711/723/749/756/760): "iki anlam da dikey
satırında görünüyor" — **dört vakada ikisi çalıştı** (`طلع`, `ذكر`), **ikisi
çalışmadı** (`لسن`, `نظر`). Hipotez: ikinci anlamın korpus sıklığı belirleyici.

## 6. Diğer P0

- **`pas` alanı edilgen ism-i mef'ûlü saymıyor** (706): 26:138, 26:212.
  **Tanım değişikliği yıldız dağılımını değiştirir; geriye dönük etkisi
  ölçülmeli.**
- **QASEM `تَٱللَّهِ` etiketlenmiyor** (443/672) — 26:97 sınama vakası. Sûre 27
  makro QASEM=1; **denetlenecek**.
- **Aday 602'nin korpus taraması** (r=−0,367) nakarat düzeltmeli yeniden
  koşulacak; **sûre 26+27 kontrollü çift** (781).
- **Çıpa tanımı** (468/561/646/736/799): yeni madde önerisi — *"ölçü sözcüğü
  geçmesi çıpa yapmaz; ölçünün NEYİ ölçtüğü belirleyici."* **Çıpa/yıldız ters
  ilişkisi iki sûrede de görüldü** (27:18 en güçlü çıpa, yıldızsız).
- **Üçüncü mercek sınıfı kararı** (646) — **kullanıcı onayı bekliyor.**

---

# ÖN-KAYIT BİLANÇOSU

| aday | tahmin | sonuç |
|---|---|---|
| 720/732/744 | nakarat çifti Lût ve Şuayb'da bütün | **TUTTU** |
| 721/733 | Şuayb açılışı üçüncü biçim, n=4 | **TUTTU** |
| **722/734** | `أَلَا تَتَّقُونَ` Lût/Şuayb'da olmayabilir | **DÜŞTÜ** |
| 755/775 | `شعر` üçüncü geçişi azınlık anlam | **TUTTU** |
| 776/796 | `ودي` katının kaynağı 27:18 | **TUTTU** |

**Desen: çalışan alan üzerinden kurulan dört ön-kayıt tuttu, eksik alan üzerinden
kurulan bir ön-kayıt düştü.**

**Kural: ön-kayıt kurulurken kullanılan ölçüm alanının hangi kısmının güvenilir
olduğu açıkça denetlenecek; eksik alan üzerinden tahmin kurulmayacak.**

# GERİ ÇEKİLEN KAYITLAR

- **650 (IDRAB tutarsızlığı)** → tam sayım yapıldı, makro doğru (aday 728).
- **666 (aktör ölçütü "belirlilik")** → ölçüt adlı aktör listesi (aday 667).
- **763 ("`سمع` dizisi esmâda kapanıyor")** → altıncı geçiş var (aday 774).
- **"Mekkî A/R ~0,57"** → iki kez düştü (26'da aşağı, 27'de yukarı; aday 780).

**Ders (774):** bir dizi "kapandı" denmeden önce sûrenin sonuna kadar okunmalı.
**Ders (728):** "makro sayım tutarsız" demeden önce tam sayım koşulmalı.
**Ders (780):** dört sûrelik bir aralıktan hipotez kurmak erken.

# BİÇİM İHLÂLİ — İKİNCİ KEZ VE ÖNLEM DÜZELTİLDİ

Blok 26:191-200'de altı ayet gruplanıp meal satırları düşürüldü; kullanıcı
uyarısıyla tam kipte yeniden yazıldı.

**Birinci ihlâlin önlemi (blok boyu ON) tutmadı çünkü yanlış değişkeni
hedefliyordu** — blok zaten on ayetti; ihlâl blok içinde "benzer ayetleri
gruplama" eğiliminden geldi.

**YENİ ÖNLEM:** her ayet kendi başlığını, Arapça satırını, Türkçe mealini, ölçüm
satırını, ◇ ve ▽ satırlarını alır; iki ayet tek başlık altında birleştirilmez.
**Denetim ölçütü: blok on ayetse sohbette ON `### S:A` başlığı olmalı.**

---

# DEVAM NOKTASI

**Sûre 27, ayet 21.** Blok 27:21-30 (on ayet). Beklenenler:

- **27:21 — sûrenin en uzun ayeti (n=61)**
- 27:22-26 hüdhüdün Sebe haberi
- **27:23'te `imrae` adsız aktörü — DENETLENECEK** (önceki hata oranı %67;
  adsız aktör sayımları kullanılmıyor, aday 641)
- **27:25 ★★★** ve hapaks `خبأ` *(gizleme)*
- 27:26 ★★
- **27:30'da besmele** (`بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ`) ve
  `رَحْمٰن|رَحِيم` mührü — sûrenin dördüncü mührü ve dördüncü farklı çift olacak
  mı, aday 789'a veri.
