# OTURUM PAKETİ — sûre 27 okuması + üç onarım turu

Bu paket, tek bir oturumda yapılan işin TAMAMINI içerir: yedi okuma bloğu
(27:21-93) ve ardından gelen üç onarım turu. Dosya listesi `git status`tan
üretildi; elle seçilmedi.

## 1. OKUMA — sûre 27 (Neml) tamamlandı

27:21'den 27:93'e yedi blok okundu; sûre 1 ve 9-27 artık TAM.
Okunan toplam **2042 / 6236 ayet (%32,7)**.

Bloklar: 27:21-30 · 31-40 · 41-50 · 51-60 · 61-70 · 71-80 · 81-93

Aday **800-876** (`bulgular/aday_bulgular.json` → `AH_neml`, 97 kayıt)
Bağ **AG_neml** 19 → 95
`kok_turkce.json` 1017 → 1032 kök

### Sûre 27 kapanış bilançosu (aday 871/872)
93 ayet · ort n=12,38 · fâsıla 84 `ن` + 9 `م` · kafiye kırılması 0
★★★ 9 · ★★ 9 · ★ 10 · yıldızsız 65 (%69,9)
Yıldız kaynakları (28 yıldızlı ayet): edilgenlik 11 · hapaks 5 · lafız 5 ·
Rab 5 · uzunluk 3 · **içerik 0**
Esmâ 33 token: 12 mühür tokeni (6 mühür, 6 farklı çift, **6/6 geçerli**),
21 mühürsüz (**20/21 artefakt**; tek geçerli 27:88 خَبِير)
İltifât 3 · hapaks 5 ayet / 6 kök · edilgen 16 ayet
A/R = 2,25

### Okuma sırasında bulunan beş alan arızası
| alan | doğru kavram | bağlandığı yanlış şey | aday |
|---|---|---|---|
| adsız aktör | adlandırılmamışlık | belirsizlik (INDEF) | 833 |
| nakarat | tekrar | ayet tekrarı | 844 |
| esit | benzerlik | tam dizge | 854 |
| MM | mef'ûl-i mutlak | VN etiketi (aşırı dar) | 867 |
| adlı aktör | özel ad | (teşhis 883'te düzeltildi) | 868 |

## 2. ONARIM — üç tur, on üç onarım

Aday **877-902** (`AI_onarim`, 26 kayıt).
Ayrıntı: `betikler/onarim/README_ONARIM.md` ve `notlar/YAPILACAKLAR.md`
sonundaki üç "ONARIM TURU" bölümü.

**Hiçbir eski alan silinmedi**; onarılanlar yeni adlarla yazıldı
(`adsiz2`, `esit2`, `nakarat2`, `adli2`, `mm2`, `harf2`, `harf3`, `isaret`).
`okuma_metni.json` DEĞİŞTİRİLMEDİ — okuma ölçümleri yeniden üretilebilir.

Koşturma sırası: `betikler/onarim/00_KOSTUR.sh`

### Onarımın büyük sonuçları
- adsız aktör duyarlılığı **%16 → %100**, kesinlik %36,4 → %100
- nakarat korpusta 119 → 1950 ayet; sûre 27'de **0 → 30**
- esit 253 → 520 ayet (üç kademe)
- `harf`in kuralı geri çıkarıldı: alan **harf + vakf/tilâvet işareti**
  sayıyor (%5,3 işaret) — `harf3` ve `isaret` diye ayrıldı
- çıpa tanımı beş kademeyle yazıldı (P0 #6); **L4 eşiğiyle sûre 27'de
  sıfır çıpa**

### Bu oturumda düşen kayıtlar (altı)
| aday | düşen iddia | doğrusu |
|---|---|---|
| 801 | 27:21 sûrenin en uzun ayeti (n=61) | n=9; (n,ayet) ikilisi ters okunmuş |
| 819 | 27:19 okumada ilk kez üç kök ikileniyor | okunan bölütte 107 ayet |
| 843 | `نظر` 27:51'de altıncı geçiş | yedinci; 27:14 atlanmış |
| 883 | adlı aktör envanterine cins isimler girmiş | envanter korpusla birebir; PN morfolojiden |
| **891** | sûre 26 nakaratlı / sûre 27 nakaratsız | %27,3'e %32,3; fark birim ve ağırlıkta |
| **898** | çıpa/yıldız ters ilişkisi | ilişki DÜZ; uzunluk+hapaks karıştırıcısı |

Son ikisi bir bloğu değil bir **çerçeveyi** bozdu; aday 899 bunun için
protokol maddesi koydu (taraflı örneklem yasağı).

Ve sûre 26'nın 41 ★★★'ı, nakarat düzeltmesiyle **27 ayrı yapıya** iniyor
(%18,1 → %11,9) — aday 781'in kontrollü çifti nihayet hesaplandı.

## 3. Denetim durumu

`turkce_denetim.py` → **0 ihlâl** (1032 kök)
`anahtar_denetim.py` (PYTHONHASHSEED=0, `betikler/` içinden,
`kok_turkce.json` DIŞARIDA) → **22409 anahtar / 58 ihlâl, tam diff = 0**

## 4. Devam noktası

**Sûre 30 (Rûm) ya da sûre 2'nin 21. ayeti.** Sûre 28 (Kasas, 88 ayet) ve sûre 29
(Ankebût, 69 ayet) bu oturumda tamamlandı; P0 #6 (çıpa eşiği) kapatıldı ve sûre 29'da
ilk bağımsız sınamasından geçirilip düzeltildi. Okunan toplam **2199/6236 (%35,3)**.

Açık P0: #3 esit eşik türleri (sınama kümesi hazır) · #5 529 lemma katmanı (**yirmi iki
vaka; üç ayrı alanın tavanını belirliyor**) · #7 yıldızın iki otomatik ★★★ tetikleyicisi
· #8 `adsiz2` envanteri · #9 esmâ mührü · **#10 `hapaks` ayet değil token sayıyor** ·
**#11 `fig` KELLA'yı `كُلّ` ile karıştırıyor** · **#12 esmâ mührü token düzeyinde
çalışamıyor (ikinci vaka, sûreler arası)**.

Ayrıntı: `notlar/OTURUM_2026-09-16_KAPANIS.md`
