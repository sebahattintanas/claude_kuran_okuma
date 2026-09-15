# TUR SONU ONARIM EVRESİ — üç tur, on üç onarım

Bu dizin, sûre 27 okumasından sonra yapılan alan onarımlarını içerir.
Adaylar: `bulgular/aday_bulgular.json` → **`AI_onarim`** kümesi (877-902).
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
