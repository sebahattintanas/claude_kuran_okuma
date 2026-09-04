# OTURUM KAPANIŞI — 2026-09-03

## Ne yapıldı

**SÛRE 24 (NÛR) TAM OKUNDU — 64/64.** Bu oturumda 24:46-64 (üç blok).
Okunan ayet **1626 → 1645** (korpusun %26,4'ü).
Tam okunan sûreler: **1, 9-24**. Kısmi: 2 (1-20).

Kök tablosu **951 → 959** (`برج` · `حذر` · `خول` · `رجو` · `شأن` · `عرج` · `قعد` · `لوذ`;
hepsi `kok_envanteri.json`'dan NFC eşlemesiyle kopyalandı). Adaylar **513 → 524**.
Bağlar `AD_nur` **43 → 65**.

## Denetimler

- `turkce_denetim.py` → **0** (üç kez). İlk blokta dokuz ihlâl; üçü sûre 9'dan geriye dönük
  (`قعد` ×2, `حذر` ×1) — bilinen desen.
- `anahtar_denetim.py` (PYTHONHASHSEED=0) → **58 ihlâl, taban listesiyle diff = 0**.
  Taranan anahtar 21613 → 21614 (üç kez).

## Ölçümler

**Kafiye kuşağı kapanışı doğrulandı.** 24:46 م ile bitiyor, N sınıfına dönüş;
24:36-45 on ayetlik kuşak kapandı (aday 509). Kuşak iki ucundan aynı formülle
çevreleniyor: 24:34 ve 24:46 `أَنزَلْنَآ ءَايَٰتٍ مُّبَيِّنَٰتٍ` — sûrenin açılış
üçlüsünün (aday 507) üçüncü ve dördüncü geçişi.

**Aynalı çağrı kalıbı (aday 514).** 24:48 ↔ 24:51: sekiz kelime birebir aynı,
sonuç ters. Arada ardışık iki hapaks (24:49 `ذعن`, 24:50 `حيف`), ikisi de aynı z.
24:47 ↔ 24:51 alıntıları da karşıt: `ءَامَنَّا … وَأَطَعْنَا` reddediliyor,
`سَمِعْنَا وَأَطَعْنَا` onaylanıyor.

**Kurtuluş çifti iki sûrede (aday 515).** 23:102/23:111 ↔ 24:51/24:52: aynı iki
fâsıla, aynı sıra, ara 9 → 0. Ve 24:52'de haşyet ile takvâ lafza bağlı — sûre 23'ün
zincirinde Rab'be bağlıydı (aday 498 ile uyumlu).

## İkinci blok (24:53-60) — araç sorusu

**Aday 517 (P1):** 24:55'te lafız 3MS'den ayet ortasında 1S'e geçiyor
(`يَعْبُدُونَنِى … بِى`), ölçüm `ilt=0`. İltifât tagger'ı lafız→zamir geçişini
işlemiyor olabilir; öyleyse sûre 24'ün "iltifât sıfır" ölçümü ve 23↔24
karşılaştırması geçersiz. Onarım öncesi kapatılmayacak.

Sûrenin tek QASEM'i (24:53) yeminin kendisini reddediyor; `طوع` üç ardışık ayette
beş kez (aday 516); 24:58 ↔ 24:59 bitişik ikiz kapanış, tek zamir farkı (aday 519);
on iki mühürün sonuncusu 24:60'ta.

## Mercek

Üç ★★★ (49, 50, 52), üçünde de iki mercek atlandı. 24:50'nin `مرض` *(hastalık)*
terimi patolojik okunmadı — dikey komşuluğu nifak ×26,0, gönderge zihinsel-ahlâkî.

## Devam noktası

**Sûre 25 (Furkān)** — makro profilden başla, sonra 25:1'den oku.

Sûre 25 **Mekkî**; 23 (Mekkî) → 24 (Medenî) → 25 (Mekkî) dizisi, A/R eksen
karşılaştırması (adaylar 470, 498) için üçüncü veri noktası olacak.

## Sûre 24 kapanış ölçümleri

**Sûrenin halkası (aday 524):** 24:42 ↔ 24:64, ortak terkip
`لِلَّهِ` + `ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ`; nesne `مُلْك` → `مَا فِى`. Sûre 23'ün halkası
açılıştan kapanışaydı, bunun ortadan — **yeni alt sınıf**.

**İki kök doruğu:** `بيت` 24:61'de tek ayette **on kez**; `أذن` 24:62'de dört kez
ve sûrede dört bölüme yayılan bir işlev ilerlemesi (adaylar 521, 522).

**Mercek bilançosu:** 64 ayet, on beş ★★★, **on dördünde iki mercek de atlandı**;
yalnız 24:35'te ikisi yazıldı. Çıpalı öteki iki ayet eşiğin altında (aday 512).

## Değişen dosyalar (zip'te)

```
notlar/okuma_metni.json · mercek_kayit.json · okuma_baglantilari.json
notlar/YAPILACAKLAR.md · OTURUM_2026-09-03_KAPANIS.md
tablolar/kok_turkce.json (951 → 959)
bulgular/aday_bulgular.json (513 → 515)
betikler/blok_24_46_52.py · blok_24_53_60.py (YENİ)
```
