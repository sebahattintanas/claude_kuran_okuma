# OTURUM KAPANIŞI — 2026-08-27

## Ne yapıldı

Boru hattı sıfırdan koşturuldu (`defter.py → defter2 → defter3 → defter4 → defter5 →
aktor2 → katman6 → graf2`); `defter.json` 6236 ayet × 39 alan doğrulandı.

**İki sûre TAM okundu:**

| | başlangıç | bitiş |
|---|---|---|
| Sûre 21 (Enbiyâ) | 21:21'den devam | **TAM 112/112** |
| Sûre 22 (Hac) | makro profil sıfırdan | **TAM 78/78** |

Okunan ayet **1293 → 1463** (korpusun %23,5'i). Tam okunan sûre: 1, 9, 10, 11, 12, 13,
14, 15, 16, 17, 18, 19, 20, **21, 22**.

Kök tablosu **720 → 880** (160 yeni karşılık). Bütün anahtarlar `kok_envanteri.json`'dan
NFC eşlemesiyle KOPYALANDI, hiçbiri elle yazılmadı.

Adaylar **437 → 464** (27 yeni). Bağlar: `AA_enbiya` 9 → 25, yeni küme `AB_hac` 9.

## Denetimler

- `turkce_denetim.py` → **0**, her blok sonunda. Yeni kökler eklendikçe sûre 9, 10, 11,
  12, 13, 17'de toplam 30'a yakın ESKİ karşılıksız anma açığa çıktı ve geriye dönük onarıldı.
- `anahtar_denetim.py` (PYTHONHASHSEED=0, depo yapısında) **üç kez** koşuldu:
  21:21-40 sonrası, sûre 21 kapanışında, sûre 22 kapanışında.
  Her seferinde **58 ihlâl, taban listesiyle diff = 0**. Yeni ihlâl yok.
  Taranan anahtar sayısı 21055 → 21495 (tablo büyümesi ve yeni betikler).

## Bulunan araç hataları (hepsi kayıtlı, hiçbiri okuma sırasında onarılmadı)

| aday | konu | büyüklük |
|---|---|---|
| **461** | esmâ: `مُؤْمِن` tek başına tablonun %9,7'si, hata %99,5 | P0, 414+444 ile birleşti |
| **452** | dikey katman lemma ayırmıyor (`طرف` ×564,8 sahte) | P0, 435 ile tek geçişte |
| **451** | jackknife kırılganlığı (`نقص`→ömür ×156,1, iki ayetten) | P0 |
| **462** | aktör tablosu isim/fiil ayrımı tutarsız (`يَهُود` vs `هَادُوا۟`) | P0, KARAR verilmedi |
| 443 | QASEM `تَٱللَّهِ` 0/9 | P1 |
| 438 | munkatı'a `أَمْ` 61 ayetin 4'ü INTG | P1 |

## Ölçülen esmâ hata oranları (aday 444/461)

- Sûre 20: **%38** (önceki oturumdan)
- Sûre 21: **%47** — 17 tokenin 8'i kesin yanlış, 2'si şüpheli
- Sûre 22: **%29** — 38 tokenin 11'i yanlış

Sûre 22'nin düşük oranının sebebi ölçüldü: esmâların çoğu MÜHÜR konumunda ve mühür
konumu bağlamı sabitliyor. Bu, onarım ölçütlerine yedinci sinyal olarak eklendi.

Tekrarlanan yanlış pozitif lemmalar: `كَبِير` (20:71 · 21:58 · 21:63 — ama 22:62'de
GEÇERLİ), `مُبِين` (21:54 · 22:11 · 22:49), `آخِر` (22:11 · 22:15), `مُؤْمِن` (21:88 ·
21:94 · 22:? ), `شَهِيد` (22:78 ×2), `مَوْلَى` (22:13 — ama 22:78'de GEÇERLİ).
`مَوْلَى` vakası en temiz örnek: 22:13 yergi kalıbında bir PUT için, 22:78 övgü
kalıbında Allah için — aynı lemma, aynı kalıp ailesi, iki karşıt gönderge.

## İki sûrenin karşıtlığı (ölçüldü)

| | Enbiyâ (21) | Hac (22) |
|---|---|---|
| Allah | 6 token = **0,15x** | 75 token = **1,69x** |
| Rab | 14 = 0,95x | 8 = 0,50x |
| A/R | **0,43** | **9,38** |
| kafiye sınıfı | **1** (mümkün olan minimum) | **10** (20+ ayetlik sûrelerde ikinci en yüksek) |
| esmâ / mühür | 17 / 1 | 38 / **11 (hepsi ÇİFT)** |
| tam-ayet ikizi | 2 | 0 |
| tip | Mekkî | Medenî |

Komşu iki sûre lafız yoğunluğunda 11 kat, oranda 22 kat, kafiye çeşitliliğinde
mümkün olan iki uç değerde ayrışıyor.

## Mercek disiplini — bu oturumun en dikkat çekici sonucu

- Sûre 21: 11 ★★★ ayetin **4'ünde biyolog** (30, 79, 87, 96), **2'sinde uzay** (30, 42).
- Sûre 22: 18 ★★★ ayetin **6'sında biyolog** (2, 5, 20, 27, 36, 73), **uzay HİÇBİRİNDE**.

Sûre 22'de gök öğesi taşıyan beş ayet var (18, 61, 63, 65, 70) ama **hiçbiri ★★★ değil**;
★★★ ayetlerin hiçbirinde de gök çıpası yok. Protokol iki yönde de kısıtladı ve zorlama
yapılmadı. Bu, YAPILACAKLAR'daki "yıldız formülü uzay merceğinin kapsamını daraltıyor"
borcunun (adaylar 129, 160, 246) yeni ve güçlü kanıtı — sapma vakası sayısı 9'dan
en az 14'e çıktı.

Atlanan her mercek `okuma_metni.json` → `_mercek_atlama_notu` alanında gerekçesiyle kayıtlı.

## Kullanıcı sorusuyla açılan üç derin bakış

`okuma_metni.json` → ilgili ayetin `derin` alanına yazıldı:

1. **21:44** — `نَأْتِى ٱلْأَرْضَ نَنقُصُهَا مِنْ أَطْرَافِهَا`. 13:41 ile segment düzeyinde özdeş
   bölüt; çerçeveler ters (korpusun en yaygın ve en seyrek görme-sorusu kalıbı, 53 vs 4).
   `نقص` tam envanteri; yer hem nesne (13:41, 21:44) hem özne (50:4). `أَتَى` + doğrudan
   ACC "yer" korpusta yalnız bu iki ayette (41 konumdan 2'si). `طَرَف` beş geçişinin
   işlev ayrımı: zaman ucuna ibadet konuyor, mekân/topluluk ucundan parça alınıyor (5/5).
   Adaylar 447-452.
2. **22:15** — göğe ip uzatma. Üç lâmü'l-emr korpusta beş ayette, dördü pratik talimat;
   22:15 tek "meydan okuma". Soru içinde te'kid nûnu (21 ayet). `لْيَقْطَعْ` mef'ûlsüz.
   `سبب` dokuz isim geçişinin üçü göğe çıkış bağlamında (22:15 · 38:10 · 40:37).
   `قطع`+`سبب` ve `ذهب`+`غيظ` ikilileri korpusta ikişer yerde. Aday 460.
3. **22:17** — "iman edenler aktör olabilir mi?" Cevap: mevcut ölçüte göre hayır,
   ama ölçüt tutarsız. Bu soru esmâ/PN tablo asimetrisini ve `مُؤْمِن` %99,5 hatasını
   açığa çıkardı. Adaylar 461, 462.

## Yeni adaylar (437 → 464)

**Enbiyâ (438-446, 453-455, 459):** munkatı'a `أَمْ` · 21:23↔34:25 çift edilgen ·
çift-hapaks ayetler (33/6236) · 21:22 tek lafız+Rab ayeti · `شمس`/`قمر` simetrisi ·
QASEM `تَٱللَّهِ` · esmâ yanlış pozitifleri · `ليل`/`نهار` üç rol · İbrâhim'in ağzındaki
lafızlar (446 → 455 ile kapandı) · `إِبْرَٰهِيم` kafiye sapmaları · `حُكْمًا وَعِلْمًا` ·
`وصف` çerçevesi.

**21:44 derin bakış (447-452):** `أَتَى`+ACC "yer" · `طَرَف` işlev ayrımı ·
`نقص`+kayıt terimi · bölüt ikizi çerçeve farkı · jackknife · lemma karışması.

**22:15/17 derin bakış (460-462):** lâmü'l-emr zinciri · `مُؤْمِن` %99,5 · aktör tasarımı.

**Hac (457, 463, 464):** 21:81-82↔38:36-37 · `ذِكْرُ ٱسْمِ ٱللَّهِ` nakaratı (9 ayetin 4'ü
tek blokta, dördüncüsü edilgen) · 22:61-65 beş ardışık ayetin sûre 31'e xref'i.

## Devam noktası

**Sûre 23 (Mü'minûn)** — makro profil sıfırdan çıkarılacak. `okuma_metni.json`
→ `ilerleme` alanı buna göre güncellendi.

Not: sûre 23 bu oturumda iki kez adaylara girdi — 21:92-93 ↔ 23:52-53 ardışık bölüt
ikizi (aday 456) ve 22:51'in xref'i 34:5/34:38. Okumaya başlarken bu iki bağ hazır.

## Değişen dosyalar (zip'te depo yapısıyla aynı klasörlemede)

```
notlar/okuma_metni.json          (21:21-112 + sûre 22 makro + 22:1-78 + 3 derin + 2 kapanış)
notlar/mercek_kayit.json         (21 → 112 mercek, 22 → 78 mercek, 22_biyolog yeni)
notlar/okuma_baglantilari.json   (AA_enbiya 25, AB_hac 9 yeni küme)
notlar/YAPILACAKLAR.md           (2026-08-27 bölümü: dört P0 + iki P1 + tarama işi)
notlar/OTURUM_2026-08-27_KAPANIS.md   (bu dosya)
tablolar/kok_turkce.json         (720 → 880)
bulgular/aday_bulgular.json      (437 → 464)
betikler/blok_dikey.py           (YENİ — blok ▽ satırı üreteci)
betikler/kok_ekle_2126.py        (YENİ — anahtar-kopyalayan kök ekleyici, şablon)
betikler/blok_21_*.py            (YENİ ×5 — blok kayıt betikleri)
betikler/blok_22_*.py            (YENİ ×4)
betikler/aday_ekle_21_21_40.py   (YENİ)
```

## Bir sonraki oturuma uyarı

`YAPILACAKLAR.md`'deki dört P0 borcunun **ikisi tek geçişte koşulmalı** (435 + 452):
ikisi de dikey satırlarını yeniden ürettiriyor, ayrı koşulursa 154+ satır iki kez üretilir.

**Aday 462 bir KARAR gerektiriyor, bir onarım değil.** Karar verilene kadar aktör
yoğunluğuna dayanan hiçbir karşılaştırma alıntılanmayacak.
