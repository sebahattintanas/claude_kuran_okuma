# ÖN-KAYIT — Süleyman × Dâvûd karşılaştırmalı kişi merceği

Yazıldı: 2026-09-18T09:27:19Z · ÖLÇÜMDEN ÖNCE · morph.txt sha256[:16] = 742bfac59941b2cb
Öncül: `ON_KAYIT_dikey_suleyman.md` (T7a KAPATILAMAZ kalmıştı).

## Tanımlar
- **Anma:** Süleyman için `LEM:سُلَيْمان`, Dâvûd için `LEM:داوُد`.
- **Pencere:** anma ayetleri ±1 ayet (sûre içinde).
- **Üç bölge:** ORTAK = iki pencerenin kesişimi · YALNIZ-S · YALNIZ-D.
- **Allah dışlaması:** dizge karşılaştırmasıyla DEĞİL, etiketle yapılır: PN ve ROOT:أله. (Geçen turdaki arızanın onarımı.)
- **Zenginleşme:** ×kat = bölgedeki gözlenen ÷ korpus beklentisi. Her kök için katkı veren FARKLI sahne sayısı yazılır.
- **"Güçlü" (T7a'nın açığı kapatılıyor):** ×kat ≥ 3 VE ≥ 2 farklı sahne. Ham sayı ölçüt DEĞİLDİR.

## Testler (aile = 2, Bonferroni eşiği 0,025)
- **K1** Süleyman ilk üçte bir oranı · **K2** Dâvûd ilk üçte bir oranı.
  - İsmin ayet içi göreli konumu = (kelime sırası − 1) / (n − 1); ilk üçte bir: ≤ 1/3.
  - Taban: korpusta Allah dışındaki bütün PN tokenlerinin ilk üçte bir oranı. Çift yönlü binom testi.
- Geri kalan her şey betimseldir.

## Tahminlerim
- **T1** Dâvûd anması 16 token.
- **T2** İki ismin birlikte geçtiği ayet sayısı ≥ 5.
- **T3** ORTAK bölge, Süleyman penceresinin yarısından büyük.
- **T4** Gizli داود dizisi isim dışında: kelime içi 0, kelime sınırını atlayan ≤ 2.
- **T5** نمل · طير · جند yalnız YALNIZ-S'de geçer; ORTAK'ta ve YALNIZ-D'de 0.
- **T6** YALNIZ-D'de حدد (demir) ve جبل (dağ) geçer; YALNIZ-S'de ikisi de 0.
- **T7** K1 ve K2 anlamlı DEĞİL (p > 0,025). Süleyman'ın 12/16'sı PN tabanından ayırt edilemez.

---
## SONUÇ (ölçümden sonra eklendi; yukarısı değiştirilmedi)
Betik: `betikler/dikey/kisi_mercek.py سُلَيْمان داوُد` · çıktı: `ciktilar/dikey_kisi_سُلَيْمان_داوُد.json`

- **T1 TUTTU:** Dâvûd 16 token, 16 ayet, 9 sûre.
- **T2 TUTTU:** iki isim 7 ayette birlikte (4:163, 6:84, 21:78, 21:79, 27:15, 27:16, 38:30).
- **T3 TUTTU (sınırda):** ORTAK 20 ayet / Süleyman penceresi 39 ayet = %51,3.
- **T4 TUTTU:** gizli داود dizisi G1 = 0, G2 = 0.
- **T5 DÜŞTÜ:** yalnız نمل tuttu (3/0/0). طير ORTAK 3 · YALNIZ-D 1 · YALNIZ-S 0. جند ORTAK 1 · YALNIZ-D 1.
- **T6 TUTTU:** YALNIZ-D'de حدد 1, جبل 2; YALNIZ-S'de ikisi de 0.
- **T7 TUTTU:**
  - K1 (Süleyman): token düzeyinde 13/17, taban 0,508, **p = 0,0495**. Nominal olarak eşiğin altında, Bonferroni sonrası (0,025) anlamlı DEĞİL.
  - K2 (Dâvûd): 8/16, p = 1,0.

## Önceki turun düzeltmesi
`ON_KAYIT_dikey_suleyman.md` komşuluk tablosunda طير (×13,2) "Süleyman komşuluğu" diye sunulmuştu.
Kontrollü ayrıştırma bu kuşların Süleyman'a özgü OLMADIĞINI gösteriyor: 3'ü ORTAK sahnelerde, 1'i yalnız Dâvûd'da (34:10), 0'ı yalnız Süleyman'da.
Özgün kayıt korunur; bu satır onun `dusuruldu` notudur.

## Ölçüm SONRASI fark edildi — ön-kayıtsız, KAPATILAMAZ
- **TAM SAYIM:** فتن 58 ayette, نوب 18 ayette geçiyor. İkisinin birlikte geçtiği ayet korpusta yalnız **iki**: 38:24 (Dâvûd) ve 38:34 (Süleyman).
  Bağımsızlık altında beklenen 58 × 18 / 6236 = 0,17.
  Desen bakıldıktan sonra seçildiği için p değeri yazılmaz.
- أَوَّاب sûre 38'de dört kez geçiyor: Dâvûd 38:17, kuşlar 38:19, Süleyman 38:30, Eyyûb 38:44. Bu iki kişiye özgü değil, sûrenin kendi motifi.

## Yöntem dersi
"Sahne" tanımı (±1 ayet pencerelerinin birleşimi) kıssa içi parçaları ayrı sahne sayıyor. Örnek: Belkıs kıssası 27:29-31 ve 27:43-45 iki sahne sayıldı.
≥2 sahne ölçütü bu yüzden sûre veya kıssa ayrılığını güvenceye almıyor. Sonraki sürümde farklı SÛRE sayısı da yazılmalı.
