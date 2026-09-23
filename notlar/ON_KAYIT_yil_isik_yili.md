# ÖN-KAYIT — Kur'an'daki yıl sayıları, ışık yılına çevrilince astronomik ölçülere rastgeleden sık mı denk geliyor?

Yazıldı: 2026-09-22T06:47:14Z · ÖLÇÜMDEN ÖNCE
Öncül: 32:5 (1.000) ve 70:4 (50.000) → ışık hızı varsayımıyla Galaksi ölçülerine denk geldiği önerisi.

## SIZINTI BEYANI
Test sayıları hedef listesinden ÖNCE görüldü. İki olası eşleşme fark edildi: 8 ≈ Sirius, 40 ≈ Arcturus.
Liste bu bilgiden bağımsız değildir. Koruma: Kur'an sayıları AYNI listeye karşı rastgele sayılarla kıyaslanır.

## Veri kuralı
- Yıl kelimesi (سَنَة, سِنِين, عام, حِجَج) + onu DOĞRUDAN niceleyen açık sayı.
- "Birkaç" (بِضْع), sayısız çoğul ve yıl kelimesi düşmüş sayılar (12:48 سَبْعٌ, 28:27 عَشْرًا) HARİÇ.
- **Keşif ailesi HARİÇ:** 32:5, 70:4 ve aynı kalıptaki 22:47.
- **Test kümesi (9 değer):** 2 (31:14) · 7 (12:47) · 8 (28:27) · 40 (5:26) · 40 (46:15) · 100 (2:259) · 309 (18:25) · 950 (29:14) · 1000 (2:96).
- Dönüşüm: n yıl → n ışık yılı (ışık hızı varsayımı).

## Hedef listesi (ışık yılı, yaklaşık, bellekten — bir kısmı ölçüm belirsizliği taşıyor)
- **L1 (17):** Proxima 4,24 · Alfa Centauri AB 4,37 · Barnard 5,96 · Sirius 8,6 · Vega 25 · Arcturus 36,7 · Aldebaran 65,3 · Polaris 433 · Ülker 444 · Betelgeuse 548 · Orion Bulutsusu 1344 · Galaksi disk kalınlığı 1000 · Galaksi merkezi 26700 · Samanyolu yarıçapı 50000 · Büyük Macellan 160000 · Küçük Macellan 200000 · Andromeda 2500000
- **L2 (15):** L1 eksi hipotezden türeyen iki galaktik hedef (1000 ve 50000).
- **Eşleşme:** |n − t| / t ≤ 0,10.

## Test (aile = 4, Bonferroni eşiği 0,0125)
- İstatistik: test kümesindeki 9 değerden kaç tanesinin en az bir hedefle eşleştiği.
- **Boş modeller** (100000 tekrar, tohum 0; her tekrarda 9 sayı):
  - **N1:** log-düzgün, [2, 1000]
  - **N2:** yuvarlak sayılar kümesinden düzgün seçim: 2-12, 15, 20, 30, …, 100, 200, …, 1000
- p = P(boş ≥ gözlenen). Testler: L1×N1 · L1×N2 · L2×N1 · L2×N2.

## Tahminlerim
- **T1** Dört testin hiçbiri anlamlı değil.
- **T2** L2'de gözlenen eşleşme L1'dekinden az (galaktik hedefler eşleşmeyi şişiriyor).

---
## SONUÇ (ölçümden sonra eklendi; yukarısı değiştirilmedi)
Betik: `betikler/analiz/yil_isik_yili.py` · çıktı: `ciktilar/yil_isik_yili.json`

| liste | gözlenen (9 değerden) | N1 beklenen / p | N2 beklenen / p |
|---|---|---|---|
| L1 | 5 | 2,56 / 0,080 | 3,60 / 0,263 |
| L2 | 3 | 2,41 / 0,448 | 3,01 / 0,625 |

E�leşmeler:
- 28:27 (8) → Sirius
- 5:26 ve 46:15 (40) → Arcturus (aynı sayı iki kez sayıldı)
- 29:14 (950) ve 2:96 (1000) → Galaksi disk kalınlığı (hipotezden türeyen hedef)

- **T1 TUTTU:** dört testin hiçbiri anlamlı değil (en küçük p = 0,080; Bonferroni eşiği 0,0125).
- **T2 TUTTU:** galaktik hedefler çıkarılınca 5 → 3. L2'de gözlenen, boş modelin beklentisiyle aynı düzeyde.

**Yorum:** yuvarlak sayılardan rastgele seçilen 9 sayı bu listeyle ortalama 3,6 eşleşme veriyor. Kur'an'daki yıl sayılarının ışık yılına çevrildiğinde astronomik ölçülere denk gelmesi, rastgele sayıların denk gelmesinden ayırt edilemiyor.
En "güçlü" görünen eşleşme (950/1000 ↔ disk kalınlığı) yalnız hipotezin kendisinden türetilen hedef sayesinde var.
