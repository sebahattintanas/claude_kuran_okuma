# ÖN-KAYIT — Sâlihât köprüsü: olumsuz öncül → sâlihât → ödül

Yazıldı: 2026-09-18T11:26:12Z · ÖLÇÜMDEN ÖNCE · morph.txt sha256[:16] = 742bfac59941b2cb
Öncüller: kavram merceği (sâlihât–cennet 20 ayet) · sıfat istisnaları (sâlihât 4 istisnanın 3'ünde).

## Tanımlar
- **Çapa:** LEM صالِحَة + FP (sâlihât) geçen ayet.
- **Öncül penceresi:** ayet a-2, a-1, a (aynı sûrede).
- **Ardıl penceresi:** ayet a, a+1, a+2.
- **NEG (olumsuz öncül):** öncül penceresinde şu köklerden biri: كفر · ظلم · خسر · كذب · فسق · ضلل · جرم · عذب.
- **ÖDÜL (ardıl):** ardıl penceresinde LEM جَنَّة veya şu köklerden biri: أجر · فوز · غفر.
- **KÖPRÜ** = NEG VE ÖDÜL.
- Bütün kök ve lemmalar korpustan doğrulanır. Bulunamayan varsa koşu durur.

## Karşılaştırma grupları
- **TABAN:** sâlihât içermeyen bütün ayetler.
- **İMAN:** أمن kökü taşıyan ama sâlihât taşımayan ayetler.
- **Uzunluk tabakası:** pencerenin (a-2 … a+2) toplam kelime sayısına göre korpus ondalıkları.
  Beklenen = her çapa için kendi ondalığındaki grup oranlarının toplamı.
  p: tek yönlü (gözlenen ≥), bağımsız Bernoulli benzetimi, 20000 tekrar, tohum 0.

## Testler (aile = 4, Bonferroni eşiği 0,0125)
- **M1a** KÖPRÜ, sâlihât vs TABAN
- **M1b** KÖPRÜ, sâlihât vs İMAN
- **M2a** NEG, sâlihât vs TABAN
- **M2b** NEG, sâlihât vs İMAN

## Tahminler
- **T1** M1a anlamlı (sâlihât'ta köprü tabandan fazla).
- **T2** M1b ANLAMLI DEĞİL (köprü sâlihât'a değil iman bağlamına ait).
- **T3** M2a anlamlı.
- **T4** Sâlihât çapalarının ≥ %40'ı KÖPRÜ.

## Bilinen sınırlar
- ÖDÜL'ün cennet kısmı önceki bulguyla kısmen döngüsel (sâlihât–cennet aynı ayette). Yeni bilgi NEG tarafında; M2 bunun için var.
- Pencereler çakışıyor; çapalar bağımsız değil. p değerleri iyimser olabilir.

---
## SONUÇ (ölçümden sonra eklendi; yukarısı değiştirilmedi)
Betik: `betikler/dikey/salihat_kopru.py` · çıktı: `ciktilar/salihat_kopru.json`
Çapa 61 ayet · TABAN 6175 · İMAN 666.

| test | gözlenen | beklenen (uzunluk tabakalı) | p |
|---|---|---|---|
| M1a köprü vs TABAN | 33/61 | 9,04 | 5e-05 |
| M1b köprü vs İMAN | 33/61 | 10,86 | 5e-05 |
| M2a NEG vs TABAN | 49/61 | 35,43 | 0,0002 |
| M2b NEG vs İMAN | 49/61 | 38,12 | 0,00115 |

Ham oranlar:
- köprü: sâlihât %54,1 · iman %19,2 · taban %10,5
- NEG: %80,3 · %63,2 · %48,0
- ödül: %65,6 · %28,4 · %17,4

- **T1 TUTTU.**
- **T2 DÜŞTÜ:** köprü, sâlihât'ı taşımayan iman ayetlerinde yaklaşık üç kat daha az (%19 vs %54). Etki imana değil sâlihât'a ait.
- **T3 TUTTU.**
- **T4 TUTTU** (%54,1).

## Ölçüm sonrası kontroller (ön-kayıtsız)
- **Kümelenme:** 33 köprü 24 farklı sûreye dağılıyor. Sonuç tek sûreden gelmiyor.
  Pencere çakışması yine de p değerlerini iyimser kılar; kaydedildi.
- **Çerçeve düzeltmesi:** köprü öncüllerinin yalnız 6/33'ünde insân, nâs ya da beşer var.
  Öncülde en sık kökler: كفر 16 · عذب 13 · ظلم 10 · جرم 4.
  Ölçülen şey "insân'ın kusurundan çıkış" DEĞİL. Ölçülen, **inkâr / azap ile ödül arasındaki karşıtlık yapısında sâlihât'ın menteşe konumu.**
  Öncül oturumdaki insân zinciri bu testle desteklenmiş SAYILMAZ.
- Önceki turun dört istisnasından ikisi köprü değil: 95:6 (95:5 NEG listesinde yok) ve 103:3 (sûre bitiyor, ödül yok).
- 38:24 (Dâvûd'un sınanması) bir köprü ayeti: "iman edip sâlih amel işleyenler hariç" → 38:25 "onu bağışladık".
