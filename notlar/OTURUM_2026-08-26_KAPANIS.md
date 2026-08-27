# OTURUM KAPANIŞ — 2026-08-26

## Yapılan okuma

| sûre | durum |
|---|---|
| **20 Tâhâ** | **TAM** — 135/135 ayet, dört katman. Makro profil + kapanış ölçümü. |
| **21 Enbiyâ** | makro profil + **1–20** ayet. Devam noktası **21:21**. |

Kapsama: `okuma_metni.json` 1293 ayet · aday havuzu **437** · payda 429 ·
α/n = 1,17 × 10⁻⁴.

## Düzeltilen HATALAR (hepsi bu oturumda yakalandı)

1. **Dikey katman yarıya indirilmişti.** `dikey_oku()` iki ölçüm döndürüyor —
   (A) komşuluk zenginleşmesi, (B) Allah medyan mesafesi. 170 ayete `dikey`
   yazılmış, yalnız **4'ünde A parçası** vardı. 154 satır yeniden üretildi;
   A birincil, B etiketsiz ham sayı. `OKUMA_STANDARDI`'na kural yazıldı.
2. **Aday 435 ölçüldü ve doğrulandı.** Düz null bozuk: taban 20 dilimde 5–72
   arası (14,4 kat). n≥15 olan 469 kökün **154'ü (%32,8)** etiket değiştiriyor,
   11'i yön değiştiriyor. `قرأ` UZAK etiketi tamamen artefakt (fark sıfır);
   `نطق` yanlış yönlü.
   **Not: bu keşif YENİ DEĞİL** — `bulgu_konum_esli_null.json` (2026-08-05)
   kuralı zaten yazmıştı, ama `dikey_oku.py` onarılmamıştı. Kural yazıldı,
   araç düzeltilmedi; bu oturumda büyüklük ölçüldü ve borç P0'ın başına alındı.
3. **Esmâ yanlış pozitifleri — sûre 20'de beş vaka** (aday 414): 20:71 `كَبِير` ·
   20:75 ve 20:112 `مُؤْمِن` · 20:125 `بَصِير` · 20:127 `آخِر`. Esmâ sayımı 13 → 8.
   Hata oranı %38. `esma_listesi.json` geleneksel listeden türetilmiş; statüsü
   `OKUMA_STANDARDI`'na yazıldı.
4. **20:73 ölçüm hatası** (aday 421): "lafız ve Rab'ın aynı ayette bulunduğu tek
   yer" yazılmıştı; doğrusu iki yer (20:73 ve 20:114). Düzeltildi.
5. **`anahtar_denetim.py` öneri metni deterministik değil** (aday 431). İhlâl
   sayısı ve listesi kararlı (58), değişen yalnız öneri. Taban dosyası
   `PYTHONHASHSEED=0` ile yeniden üretildi.
6. **Sohbet çıktısı biçimi** iki kez düzeltildi: ayet numarası zorunlu,
   karşılıksız Arapça yok, ★★★ ayetlerde üç mercek de o ayetin kapsamında.

## Yeni ölçümler

- **GÖRME ve SÖYLEME alanları** (`notlar/derin_bakis_gorme_soyleme.json`,
  adaylar 432–436): `تلو` %39,3 ve `وحي` %36,1 edilgen (taban %5,95) ·
  `كلم` bab I hiç yok · duyu üçlüsü `سمع → بصر → فأد` **7/7 sabit sıra** ·
  `سَمْع` 22/22 tekil, hiç çoğullanmıyor.
- **HİZALAMA ölçümü** (aday 437, `ciktilar/allah_hizalama.html`): 2699 lafız
  merkeze hizalandı. **Sol = çerçeve** (`صدد` ×15,2 @−3 · `كفي` ×14,9 @−1 ·
  `دون` ×12,9 @−1 · `فري` ×12,7 @−2), **sağ = sıfat** (`عزز` ×9,0 @+1 ·
  `غفر` ×8,2 @+1 · `حكم` ×7,1 @+2). `قول` n=1722 hiçbir konumda sapmıyor.
- **Allah lafzı haritası**: 2699 token · ortalama aralık 28,7 kelime ·
  en büyük boşluk 1075 (53:62→57:1) · **29 sûrede lafız hiç yok** (%3,8).

## Tablolar

`kok_turkce.json` **314 → 720** (bu oturumda 406 kök). Zenginleşme katmanının
kavram adları da karşılık alıyor. `turkce_denetim.py` kapsamı genişletildi:
`olcum`, `mercek`, `dikey`, `derin`, `derin2`.

## Denetimler (oturum sonu)

- `turkce_denetim.py` → **0**
- `anahtar_denetim.py` → 58, taban ile aynı (yeni ihlâl yok)
- `okuma_metni.json` sûre 20: 135 ayet, dikey 135/135 (20:1 gerekçeli boş)
- `mercek_kayit.json` 20: 135 · 21: 20

## Bir sonraki oturumun İLK İŞLERİ

1. **21:21'den devam** — blok akışı 20 ayet, dört katman.
2. `dikey_oku.py` onarımı ertelenebilir; ama `▽` satırı A parçası olmadan
   yazılamaz (kural yürürlükte).
3. Tur sonu için P0 sırası: **435 (dikey null)** → **414 (esmâ tablosu)** →
   431 (denetim determinizmi) → 437 (hizalama kalıp ayrımı).
