# TUR SONU ONARIM EVRESİ — üç tur (on üç onarım) + iki ek onarım

Bu dizin, sûre 27 okumasından sonra yapılan alan onarımlarını ve sûre 28-29
okumasından sonra yapılan iki ek onarımı içerir.
Adaylar: `bulgular/aday_bulgular.json` → **`AI_onarim`** (877-902) ve
**`AL_onarim2`** (937-939).

## Ek onarımlar (sûre 29 sonrası)

| no | betik | arıza | aday |
|---|---|---|---|
| **14** | `22_hapaks_onarim.py` | `hapaks` nadirliği TOKEN sayarak ölçüyordu, AYET değil | 926 → 937 |
| **15** | `23_fig_kella_onarim.py` | `fig` KELLA'yı `كُلّ` ile karıştırıyordu (%31 yanlış pozitif) | 927 → 938 |
| **16** | `26_lemma_katmani.py` | P0 #5a: lemma kimliği hiç kullanılmıyordu (maliyet 0) | 940 → 941 |
| **17** | `27_nakarat3.py` | `nakarat2` YÜZEY n-gramı kullanıyor, lemmayı değil | 906 → 942 |
| **18** | `28_olgu_lemma.py` | çıpa taramasında olgu eşleşmesi KÖK düzeyindeydi | 923 → 944 |
| **19** | `29_cipa_tarama4.py` | tarayıcı v4: olgu eşleşmesi (kök, lemma) çiftinde | 923 → 944 |
| **20** | `31_ikili.py` | `nakarat` alt sınırı: 3'te kaldı, 2 kelimelik köklü çiftler ayrı alanda | 907/935/943 → 947 |

Sınama: `24_onarim_sinama.py` — **onarım 14: 12/12 · onarım 15: 8/8**, iki sınama
kümesi de okuma kayıtlarından kuruldu (onarım yazılırken değil).
Kapanış ve aday 903'ün tazelenmesi: `25_onarim_14_15_kapanis.py`.
Ayrıntılı kayıt: `notlar/YAPILACAKLAR.md` sonundaki üç "ONARIM TURU" bölümü.

## Temel kural

**Hiçbir eski alan silinmedi.** Onarılan alanlar YENİ adlarla yazıldı:

| eski | yeni | ne değişti |
|---|---|---|
| `adsiz` | `adsiz2` | kök → lemma eşleşmesi; belirlilik koşulu kaldırıldı; ölü anahtar onarıldı |
| `esit` | `esit2` | tam dizge → üç kademe (tam / yakin ≥0,95 / benzer ≥0,85) |
| `dugum.nakarat` | `nakarat2` | ayet düzeyi → n-gram düzeyi |
| `adli` | `adli2` | mensubiyet/soyut adlar `cins` türüne ayrıldı |
| `fig` içindeki `MM` | `mm2` | V+VN (3 ayet) → V + aynı kök + ACC isim (125 ayet) |
| `harf` | `harf2`, `harf3`, `isaret` | besmele kirliliği çıkarıldı; alan harf ve vakf işareti diye ayrıldı |
| `hapaks` | `hapaks2` | ölçüt TOKEN'dan AYET'e taşındı (399 → 420 kök); `yildiz2`, `z2` ayrıca yazıldı |
| `fig` içindeki `KELLA` | `fig2` | yüzey biçimi → `LEM:كَلّا`; 48 → 33 ayet, yanlış pozitif %31 ayıklandı |
| `nakarat2` | `nakarat3` | yüzey n-gram → LEMMA n-gramı; 1950 → 2260 ayet, bir yanlış pozitif düştü |
| çıpa taraması v3 | v4 | olgu eşleşmesi kök → (kök, lemma); havuz 680 → 477, kesinlik %35 → %47 |

Böylece sûre 27 okumasının (okuma_metni.json) ölçümleri yeniden üretilebilir kalır.
**`okuma_metni.json` DEĞİŞTİRİLMEDİ.**

## Koşturma

`00_KOSTUR.sh` — sıra önemlidir; `04` diğerlerinin altyapısını üretir.

## Onarım protokolü (bu turda konuldu)

1. **`kaybedilen == 0` savı:** hiçbir onarım, eski alanın yakaladıklarının tamamını
   yakaladığı gösterilmeden kabul edilmez. Bu turda ÜÇ onarım ilk sürümünde kendi
   yanlış negatifini üretti (esit v1: 46 ayet · MM ara v1: iki ayet · dikey ifade
   ölçütü v1: donmuş kalıplar).
2. **Sınama kümesi:** her onarım, okumada belgelenmiş vakalardan kurulu bir kümeyle
   sınanır ve sonuç `n/n` olarak yazılır.
3. **Çapa doğrulaması:** korpustan türetilen anahtarlar çapa konumlarıyla alınır ve
   çapaların kendisi doğrulanır (bu turda altı çapanın ikisi yanlış çıktı).
4. **Taraflı örneklem yasağı (aday 899):** okuma sırasında "X'li ayetler Y oluyor"
   iddiası kurulursa KAPATILAMAZ etiketiyle kaydedilir, tur sonunda TAM SAYIMLA
   sınanır. Okuma notlarından toplanan örneklerle sınanamaz.

## Üretilen veri dosyaları

`tablolar/` içinde: `adsiz_lemma_listesi.json` · `nakarat_kaliplari.json` ·
`dikey_kaynak_ornek.json` · `cipa_kademe_27.json` · `harf_sayilan_kodnoktalari.json`

`ayet_iskelet.json` ve `ngram_indeks.json` depoya KONULMADI — büyük ve
`04_ngram_altyapi.py` ile yeniden üretilebilir.

## Bu turda düşen okuma kayıtları

| aday | düşen iddia | doğrusu |
|---|---|---|
| 883 | "adlı aktör envanterine cins isimler girmiş" | envanter korpusla birebir; PN etiketi morfolojiden |
| 891 | "sûre 26 nakaratlı / 27 nakaratsız" | %27,3'e %32,3; fark birim ve ağırlıkta |
| 898 | "çıpa/yıldız ters ilişkisi" | ilişki DÜZ; uzunluk ve hapaks karıştırıcısı |

Ayrıca sûre 26'nın 41 ★★★'ı, nakarat düzeltmesiyle **27 ayrı yapıya** iner (%18,1 → %11,9).
