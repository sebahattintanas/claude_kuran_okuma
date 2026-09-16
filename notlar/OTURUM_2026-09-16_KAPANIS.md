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
