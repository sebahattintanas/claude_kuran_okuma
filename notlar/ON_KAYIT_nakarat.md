# ÖN-KAYIT — Rahmân nakarat prozodi sınavı
Yazılma anı: ölçüm KOŞULMADAN önce. Sonuç görülüp değiştirilmedi.

## Soru
Prozodinin ne kadarı metne bağlı, ne kadarı icra serbestisi?

## Nesne
Sûre 55 (Rahmân), 78 ayet, tek kārî, ayet-ayet mp3 (everyayah).
Segmentasyon dosya sınırından gelir → hizalama hatası yok.

## Gruplar
- NAKARAT (n=31): 13,16,18,21,23,25,28,30,32,34,36,38,40,42,45,47,49,51,
  53,55,57,59,61,63,65,67,69,71,73,75,77 — HARFİ HARFİNE AYNI metin.
- KONTROL (n=46): kalan ayetler, 55:1 HARİÇ (besmele içeriyor, metin uzunluğu
  kuran_veri.json ile uyuşmuyor).

## Ölçümler (ayet başına)
d      = sessizlik kırpımı sonrası süre (sn), eşik = tepe RMS'nin %2'si
m      = mora (kuran_veri.json, metinden)
dpm    = d/m  (mora başına süre, sn)
f0     = seslendirilmiş çerçevelerin medyan F0'ı (pyin, 60–400 Hz)
egim   = F0'a zamana göre doğrusal regresyon eğimi (Hz/sn)
rms    = medyan RMS

## BİRİNCİL İSTATİSTİK (önceden seçildi)
oran = CV(dpm | nakarat) / CV(dpm | kontrol)
- oran belirgin şekilde <1 → süre profilinin metne bağlı kısmı ölçülmüş olur
- oran ≈1 veya >1 → NULL, öyle yazılır

Anlamlılık: 10.000 permütasyon (grup etiketleri karıştırılır), tek yönlü.
Bonferroni: bu bir aday bulgudur, aday_bulgular.json'a girer.

## İKİNCİL (keşif, iddia değil)
- sürüklenme: nakarat sırası (1..31) → d, f0 regresyonu
- aynı sınav f0 ve rms için tekrarlanır

## SANITY KONTROL (başarısızsa ölçüm iptal)
31 nakarat ayetinin kuran_veri.json mora değeri AYNI olmalı.
Değilse korpus tarafında hata var, ses ölçümü koşulmaz.

## PEŞİNEN KABUL EDİLEN SINIRLAR
- Tek kārî → sonuç bu kārîye aittir, genellenemez.
- Nakarat sûre boyunca dağılmış, kontrol de öyle → konum eşleşmesi kabaca sağlanır
  ama tam değil.
- mp3 kayıplı sıkıştırma; F0 ve süre için sorun değil, tını için olurdu.
