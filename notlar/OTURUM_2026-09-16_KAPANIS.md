# OTURUM KAPANIŞI — sûre 28 (Kasas) okuması, dokuz blok

Bu oturumda sûre 28 baştan sona okundu: **88 ayet, dokuz blok.**
Onarım turu yapılmadı; oturum bütünüyle okuma ve ölçüm.

## 1. OKUMA

Bloklar: 28:1-10 · 11-20 · 21-30 · 31-40 · 41-50 · 51-60 · 61-70 · 71-80 · 81-88

Okunan toplam **2130 / 6236 ayet (%34,2)**; sûre 1 ve 9-28 artık TAM.
Aday **903-919** (`bulgular/aday_bulgular.json` → `AJ_kasas`, 17 kayıt)
Bağ **AH_kasas** 22 kayıt
`kok_turkce.json` 1032 → **1052** kök (20 yeni)

### Sûre 28 kapanış bilançosu
88 ayet · ort n=16,25 · fâsıla harf olarak 81 `ن` + 3 `م` + 2 `ل` + 2 `ر` + 1 mukattaa,
SINIF olarak 84 N + 2 `ل` + 2 R + 1 `ٓ` · kafiye kırılması **1** (28:28)
★★★ 8 · ★★ 6 · ★ 13 · yıldızsız 61 (%69,3)
Yıldız kaynakları (27 yıldızlı ayet): **pas 9 · hapaks 7 · rab 5 · n 3 · allah 2 ·
kafiye 1 · içerik 0**
Esmâ 19 token: mühürlü 2 (**2/2 geçerli**), mühürsüz 17 (**15 artefakt, 2 geçerli**)
İltifât **0/88** · hapaks 7 ayet / 8 kök · edilgen 18 ayet
Lafız 27 token / 21 ayet · Rab 19 token / 19 ayet → **A/R = 1,42**
`harf` 6150 → `harf3` **5861**, isaret 270 (**%4,4**)
mm2 1 ayet / 2 kayıt · esit2 dolu 6 ayet · iç düğüm 1 (28:37↔28:85)

## 2. OTURUMUN ANA BULGUSU — yıldız formülünün iki otomatik ★★★ tetikleyicisi

| tetikleyici | ayet | z | hepsi ★★★ mi |
|---|---|---|---|
| ≥1 hapaks kök | **358** | 3,38 | **evet, istisnasız** |
| bütün fiilleri edilgen | **124** | **5,38 (tek değer)** | **evet, istisnasız** |
| birleşim | **471** | — | tüm ★★★'ların **%53,5'i** |

Sûre 28 bunu birebir doğruluyor: sekiz ★★★ = yedi hapaks ayeti + bir tam-edilgen ayet.
Kalan 409 ★★★ öbür ölçütlerin uç değerlerinden (rab 180 · allah 123 · n 86 · pas 23).

**Payda etkisi dört ayrı ölçütte gösterildi.** En saf vaka 28:71/28:72: dokuz kelimelik
nakaratı birebir paylaşan, i'râb profilleri ve lafız sayıları aynı iki ayet; **tek fark
iki kelimelik uzunluk** ve yalnız biri ★ alıyor (allah z 1,58 / 1,38).

## 3. ÜÇ AÇIK P0'A GELEN VERİ

**#3 (esit eşik türleri) — sınama kümesi hazır.** Dokuz vaka; 'yakin' kademesi (≥0,95)
sûre boyunca bir kez bile tetiklenmedi; gerçek bağlar **0,82-0,95** bandında.
En sert kaçak **28:31 ↔ 27:10**: on iki kelime birebir ortak, oran 0,8252, eşiğin
**0,025 altında** düşüyor. TAM SAYIM: on kelimelik ortak dizi paylaşan 111 çiftin
yalnız 31'i (%27,9) görülüyor; kaçan 80'in 66'sı çapraz-sûre.

**#5 (lemma katmanı) — kapsam büyüdü.** Borç yalnız gloss değil, **ölçüm** borcu da:
lemma katmanı olmadığı için `nakarat2` iki gerçek çifti göremiyor (28:5↔28:41,
28:30↔28:46). Sınama kümesi on sekize çıktı.

**#6 (çıpa eşiği) — karara hazır.** L4 ve L3 iki sûrede de **sıfır**. L2 sûre 28'de üç
kayıt ve ikisi (28:71-72) **ilk kez gerçek bir doğa olgusuna** bağlı. Öneri: L2 +
'olgu/olgu-dışı' ikinci bayrağı. **Çıpa ile yıldız sûre 28'de hiç çakışmıyor.**

## 4. TARAFLI ÖRNEKLEM YASAĞI İLK KEZ BİR İZLENİMİ DÜŞÜRDÜ

Okuma sırasında üç blok boyunca 'sûre 28 sûre 12'ye yoğun bağlanıyor' izlenimi birikti
ve aday 899 gereği KAPATILAMAZ kaydedildi. Tam sayım izlenimi **düşürdü**: kaynak ayet
sayısına göre sûre 6 (10) ve sûre 27 (7) önde, **sûre 12 altıncı sırada (5)**.
Okuma dikkati sûre 12'yi seçmişti çünkü oradaki koşutluklar anlamca çarpıcıydı.

## 5. DENETİMLER

- `turkce_denetim.py` → **0 ihlâl** (1052 kök kapsamı)
- `anahtar_denetim.py` (PYTHONHASHSEED=0, `kok_turkce.json` DIŞARIDA) →
  **22486 anahtar, 58 ihlâl, ihlâl listesi diff = 0**; taban tazelendi
- **Retroaktif onarım:** yeni eklenen `وصل` ve `صرخ` kökleri 13:21 ve 14:22'de
  karşılıksız anma açtı, `yama_retroaktif_gloss.py` ile düzeltildi (aday 917)

## 6. YAZILAN BETİKLER

`betikler/` içine kopyalandı ve `anahtar_denetim.py` ile tarandı:

- `blok_28_1_10.py` … `blok_28_81_88.py` (dokuz blok betiği)
- `uret_blok_betikleri.py` — dokuz blok betiğini üretir
- `olcum_bicim.py` — **ölçüm satırını defterden üretir, elle yazılmaz**
- `gloss_gecis.py` — kök anmalarını `kok_turkce.json`'dan otomatik gloss geçişi
- `kasas_metin_1.py` / `kasas_metin_2.py` — meal ve matematikçi merceği
- `kasas_kapanis.py` — çıpa tablosu, yıldız kaynak tablosu, esmâ tablosu, kapanış
- `aday_ekle_28_kasas.py` — adaylar 903-919 ve 22 bağ
- `yama_retroaktif_gloss.py` — retroaktif gloss onarımı

**Yöntem notu:** bu oturumda ölçüm satırı ilk kez elle yazılmadı; `olcum_bicim.py`
bütün sayıları `defter.json`'dan okuyor ve kök anmalarını `kok_turkce.json`'dan
geçiriyor. Yorum (◇) elle yazılmaya devam ediyor. Ölçüm/yorum ayrımı böylece
dosya düzeyinde de ayrıldı.

## 7. DEVAM NOKTASI

Sûre 29 (Ankebût) ya da sûre 2'nin 21. ayeti. **Ama önce P0 #6 kapatılabilir:**
karar verisi tamam ve tek başına bir oturum gerektirmiyor.

---

## EK — P0 #6 KAPATILDI (aynı oturum, okuma sonrası)

**ÇIPA ÖLÇÜTÜ: (L2+) VE (olgu = evet).** İki sûrelik (181 ayet) sonuç: L4+ → 0 ·
L3+ → 1 (27:88) · L2+ → 9 ama tekdüze değil (2'si olgu-dışı) → ikinci bayrak şart.
**Çıpa: 27:60 · 27:64 · 27:86 · 27:88 · 28:71 · 28:72 · 28:73 (7 ayet, %3,9).**

**Ölçüt mekanikleştirildi (aday 921):** beş morfolojik işaret ailesi — A_şart (339+14) ·
B_ta'lîl `PRP|PREF` (132) · C_recâ (52) · D_yeti (93) · E_görünüş `CIRC|PREF` (12).
**537 aday ayet (%8,6), anma 7/7 (%100), kesinlik 7/17 (%41).**

**Çıpa ile yıldız BAĞIMSIZ (aday 922):** 3/7 yıldızlı (%42,9) vs taban %30,4;
binom p=0,362, anlamlı değil. Kademe × yıldız ters yönde: L0 %44 · L1 %50 · L2 %25.
**🜁/🜂 ★★★ koşuluna bağlanamaz** — bağlansaydı yedi çıpanın altısı düşerdi.

**P0 #6'nın tavanını P0 #5 belirliyor (aday 923):** yanlış pozitiflerin %40'ı lemma
kusurundan; lemma katmanıyla kesinlik %41 → %54.

**Dört kaydım düştü, silinmedi (aday 910'a `dusuruldu` alanı):** L3 sayısı, sûre 27'nin
L2'lerinin olgu durumu, "ilk kez" iddiası ve 28:73'ün kademesi. Ortak sebep: dördü de
sûre 27'nin tablosuna bakılmadan hatıradan kuruldu — **aday 843'ün çıpa tarafındaki eşi.**

**Denetimin yakaladığı kendi kusurum:** `anahtar_denetim.py` yeni betiklerimde elle
yazılmış Arapça edatları (لولا/لعل/حتا/لكيلا) BOZUK işaretledi — ikisi yazım hatası,
ikisi korpusta hiç yok. Eşleme morfoloji lemmasına taşındı; havuz 586→537, **anma 7/7
korundu, kesinlik %33→%41 yükseldi.** Ayrıca Arapça sabitlerin içine kaçan Latin ok
karakteri (0x2192) 35 yerde ayrıldı.

Denetimler: `turkce_denetim.py` → **0** · `anahtar_denetim.py` → **22601 anahtar,
58 ihlâl, diff = 0**.

Adaylar **920-923** (`AJ_kasas` 17 → 21 kayıt).

---

## EK 2 — SÛRE 29 (ANKEBÛT) OKUNDU, 69 AYET, YEDİ BLOK

Bloklar: 29:1-10 · 11-20 · 21-30 · 31-40 · 41-50 · 51-60 · 61-69
Okunan toplam **2199 / 6236 ayet (%35,3)**; sûre 1 ve 9-29 tam.
Aday **924-936** (`AK_ankebut`, 13 kayıt) · bağ **AI_ankebut** 23 kayıt
`kok_turkce.json` 1052 → **1059** (üç sûrede toplam 27 yeni kök)

### Sûre 29 kapanış bilançosu
69 ayet · ort n=14,14 · fâsıla sınıf 65 N + 3 R + 1 mukattaa · **kafiye kırılması 2 ve
ARDIŞIK** (29:21-22) · ★★★ 4 · ★★ 7 · ★ 11 · yıldızsız 47 (%68,1)
Yıldız kaynakları: **allah 9 · pas 6 · kafiye 2 · n 2 · rab 2 · hapaks 1 · içerik 0**
Lafız **42 token / 30 ayet** · Rab **5 / 5** → **A/R = 8,4** (27'de 2,25, 28'de 1,42)
Esmâ 25 token: **mühürlü 8 → 8 geçerli** · mühürsüz 17 → 3 geçerli, 14 artefakt
İltifât **1** (29:23) · hapaks **1 ayet** · edilgen 15 ayet
Adlı aktör **21 token / 16 ad** — sûre 28'in 37 tokenine karşı çok daha dağınık
`harf` 4498 → `harf3` **4256**, isaret 223 (%5,0) · `mm2` 1 · iç düğüm 4 ayet / 2 çift

### Bu turun ana bulgusu — P0 #6'nın ilk bağımsız sınaması

Tarayıcı kurulum kümesi dışında ilk kez sınandı ve **üç çıpayı kaçırdı.** Aday 921'in
"anma %100" kaydı **döngüseldi**. İki yeni işaret ailesi (`F_ölçü`, `G_bakış`) eklendi;
havuz 537 → 680, **tutulan kümede anma 3/3.**

**DERS: bir tarayıcının kendi kurulum kümesindeki anması bilgi taşımaz** — aday 899'un
ölçüm tarafındaki eşi.

### Okumanın ilk iki L4 kaydı

**29:14 (ölçü)** ve **29:40 (sınıflama)** — L4'ün üç kolundan ikisi örneklendi, üçüncüsü
(mekanizma) hâlâ boş. Dört sûrede 319 ayet, iki L4: **%0,6.**

### Üç alan denetimi

- **`hapaks` ayet değil token sayıyor** (aday 926): tek ayette geçen 420 kökün 21'i
  nişandan düşüyor; **29:41'in `عنكب`'i (sûrenin adı) bunlardan biri ve ayet yıldızsız.**
- **`fig` KELLA'yı `كُلّ` ile karıştırıyor** (aday 927): 48 ayetin 15'i (%31) yanlış
  pozitif, yanlış negatif sıfır.
- **`esit2` onarımı yanlış negatif üretmemiş** (aday 928, olumlu): eski 253, yeni 520,
  **kesişim tam 253.**

### Denetimler
- `turkce_denetim.py` → **0 ihlâl** (1059 kök)
- `anahtar_denetim.py` → **22754 anahtar, 58 ihlâl, ihlâl listesi diff = 0**
- **Denetimin yakaladığı kendi kusurum:** lafza-i celâl'i korpus lemma biçiminden farklı
  yazmışım (`ٱللَّه` yerine `اللَّه` olmalıydı) — sekiz yerde düzeltildi.
- **Retroaktif onarım (aday 917'nin ikinci vakası):** yeni eklenen `ركب` ve `يأس` kökleri
  11:42, 12:87 ve 12:110'da karşılıksız anma açtı; `yama_retroaktif_gloss_29.py` ile
  düzeltildi.

### Devam noktası
Sûre 30 (Rûm) ya da sûre 2'nin 21. ayeti. Açık P0: #3 · #5 (kapsam üçüncü kez büyüdü) ·
#7 · #8 · #9 · **#10 hapaks tanımı · #11 fig KELLA · #12 esmâ mührü (ikinci vaka)**.

---

## EK 3 — ONARIM 14 ve 15 (P0 #10 ve #11 kapandı)

Protokole uygun: **hiçbir eski alan silinmedi**, `okuma_metni.json` değiştirilmedi.
Yeni alanlar: **`hapaks2`** · **`z2`** · **`yildiz2`** · **`fig2`** (defter 47 → 51 alan).

**Onarım 14 — `hapaks2`:** ölçüt TOKEN'dan AYET'e taşındı. Korpusta tek ayette geçen
420 kökün 21'i, o ayette birden çok token taşıdığı için düşüyordu. **kaybedilen = 0 ·
sınama 12/12 · hapaks ayeti 358 → 375 · yıldız değiştiren 10 ayet (beşi ★0 → ★★★).**
En çarpıcı düzeltme **29:41**: sûrenin adını taşıyan kök (`عنكب`) korpusta yalnız o
ayette geçiyor ve ayet yıldızsızdı, artık ★★★.

**Onarım 15 — `fig2`:** KELLA etiketi `LEM:كَلّا`ya bağlandı. 48 → 33 ayet, **yanlış
pozitif %31, yanlış negatif sıfır, sınama 8/8.** Aday 927'nin on üç vakalık listesi tam
sayımla **on beşe** tamamlandı (25:39, 57:10).

**Aday 903 tazelendi:** hapaks2 içeren 375 ayetin 375'i ★★★, tam-edilgen 124 ayetin
124'ü ★★★, birleşim **486** = ★★★'ların **%54,6'sı**. Tek hapaksın z'si 3,38 → 3,28,
hâlâ eşiğin üstünde — **hapaks tek başına yeter şart olmayı sürdürüyor.**

**Düşen iki kayıt (aday 926'nın kendi öngörüleri):** "358 → 379" gerçekte 358 → 375;
"beş yeni ★★★" gerçekte on ayet değişti, beşi yıldızsızdan. **Ortak sebep: kaçan 21
kökün AYET dağılımı hesaplanmadan kök sayısından ayet sayısına geçilmişti** — aday
843'ün üçüncü tekrarı, bu kez hafızadan değil koşulmamış bir aritmetikten.

Adaylar **937-939** (`AL_onarim2`). Denetimler: `turkce_denetim.py` → **0** ·
`anahtar_denetim.py` → **22793 anahtar, 58 ihlâl, diff = 0**.
