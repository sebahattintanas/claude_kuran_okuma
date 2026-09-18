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

**Sûre 31 (Lokmân) ya da sûre 2'nin 21. ayeti.** Bu oturumda sûre 28, 29 ve 30 okundu;
P0 #6 kapatılıp sınandı, P0 #10/#11 onarıldı, **P0 #5'in (a) parçası (lemma kimliği)
kapatıldı** ve `nakarat` alt sınırı kararı verildi. Okunan toplam **2259/6236 (%36,2)**.

**En büyük açık borç: aday 948** — çıpa tarayıcısının üç sürümünün ortak varsayımı
("çıpa bir söz eylemi işareti taşır") sûre 30'da çürüdü; anma 4/4'ten **2/9**'a düştü.

Öbür açık P0: #3 esit eşik türleri · **#5b lemma glossu** (2537 satır; sınama kümesi 28
vaka) · #7 · #8 · #9/#12 esmâ mührü · **#13 `say` ölçüyü görmüyor** · **#14 merdiven
boşlukları + 'olgu' bayrağının tanım açığı** · **#15 yıldız formülü iki ölçütü
toplamıyor**.

Ayrıntı: `notlar/OTURUM_2026-09-16_KAPANIS.md`
