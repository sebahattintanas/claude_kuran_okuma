# ÖN-KAYIT — İnsanın üç adı: insân · nâs · beşer

Yazıldı: 2026-09-18T09:51:15Z · ÖLÇÜMDEN ÖNCE · morph.txt sha256[:16] = 742bfac59941b2cb
Öncül: `ON_KAYIT_kavram_mercek.md` (insân: خلق, مسس, وزر, نطف; ayet sonu %1,4).

## Tanımlar (lemma korpustan NFC ile çözülür)
- **INS** = LEM إِنسان · **NAS** = LEM ناس · **BES** = LEM بَشَر (bütün sayılar).
- Kapsam dışı: إِنس (cin ile çift kalıbı), إِنسِيّ, أُناس.

## Ölçüm A — Birbirinden ayıran kökler (kişi merceği tasarımı)
- Özel bölge = kelimenin ±1 ayet penceresi eksi öteki ikisinin pencereleri.
- Evren = üç pencerenin birleşimi.
- Üç kelimenin kendisi sayımdan çıkarılır.
- Test: k ≥ 3 olan her (kelime, kök) çifti. Hipergeometrik tek yönlü p.
- **"Ayıran kök" koşulları:** p < 0,05 / m · ×kat ≥ 2 · ≥ 3 farklı sûre.

## Ölçüm B — Dilbilgisel ve dağılımsal profil
Her ölçüt için 3 × k çapraz tablo ve ki-kare testi (beklenen < 5 ise Monte Carlo, 20000 tekrar, tohum 0).
Aile = 5; Bonferroni eşiği 0,01.
- **B1 Hitap:** hedef kelimenin kendisi veya bir önceki kelime VOC taşıyor mu.
- **B2 Belirlilik:** DET taşıyor mu.
- **B3 Hâl:** NOM / ACC / GEN.
- **B4 Nüzul:** ayetin `tip` alanı M / D (sûre düzeyinde bir etiket).
- **B5 Ayet sonu:** kelime ayetin son kelimesi mi.

## Tahminlerim
- **T1** Hitap: NAS ≥ %10 · INS ≤ %5 · BES = 0.
- **T2** INS'in Mekkî oranı NAS'ınkinden yüksek.
- **T3** INS belirliliği ≥ %90 · BES belirliliği ≤ %20.
- **T4** INS'in ayıran kökleri arasında خلق var · BES'inkiler arasında مثل var.
- **T5** INS'in NOM oranı NAS'ınkinden yüksek.
- **T6** Üçünün de ayet sonu oranı < %10.
- **T7** B ailesinin 5 testinden en az 4'ü anlamlı (üç kelime dilbilgisel olarak farklı davranıyor).

---
## SONUÇ (ölçümden sonra eklendi; yukarısı değiştirilmedi)
Betik: `betikler/dikey/insan_uclu.py` · çıktı: `ciktilar/insan_uclu.json`
Sayım: INS 71 · NAS 241 · BES 37. Ölçüm A: m = 604, eşik 8,3e-05.

### Ölçüm A — ayıran kökler
- INS: خلق (×4,6, 21 sûre) · وزر (×44,6, "3 sûre") → **vezr ZAYIF, aşağıya bakın**
- NAS: أله (×2,4, 38 sûre)
- BES: قول (×2,1, 17 sûre) · مثل (×3,9, 10 sûre)

### Ölçüm B (Bonferroni 0,01)
| | INS | NAS | BES | p |
|---|---|---|---|---|
| B1 hitap | %2,8 | %8,3 | %0 | 0,061 (MC) |
| B2 belirli (DET) | %90,1 | %100 | %13,5 | 5e-05 (MC) |
| B3 NOM | %40,8 | %17,4 | %43,2 | 4e-10 |
| B4 Mekkî | %85,9 | %49,4 | %89,2 | 2e-10 |
| B5 ayet sonu | %1,4 | %2,1 | %10,8 | 0,022 (MC) |

Korpus tabanı Mekkî ayet oranı %74,0 (4613/6236).

### Tahminler
- **T1 DÜŞTÜ:** NAS hitabı %8,3 (< %10). INS %2,8 ve BES %0 tuttu.
- **T2 TUTTU:** INS %85,9 > NAS %49,4.
- **T3 TUTTU (sınırda):** INS %90,1 · BES %13,5.
- **T4 TUTTU:** INS → خلق · BES → مثل.
- **T5 TUTTU:** INS NOM %40,8 > NAS %17,4.
- **T6 DÜŞTÜ:** BES %10,8. Dört ayet sonu geçişinin DÖRDÜ de sûre 74'te (74:25, 29, 31, 36; fâsıla ر). Kafiye artefaktı.
- **T7 DÜŞTÜ:** 5 testten 3'ü anlamlı (B2, B3, B4).

## Ölçüm sonrası kontroller (ön-kayıtsız)
1. **INS → وزر token şişmesi + eşsesli.** 7 tokenin kaynağı:
   - 39:7 ve 53:38'deki "kimse kimsenin yükünü taşımaz" formülü; formül tek ayette 3 token → 2 ayet × 3.
   - 75:11 وَزَر = "sığınak", eşsesli.
   Eşsesli çıkınca 2 sûre kalıyor ve ≥ 3 sûre koşulu tutmuyor.
   **Aday 926 dersinin (token değil ayet say) kavram merceğindeki tekrarı. Ölçüm A'nın birimi ayet olmalıydı.**
   Kavram merceği turundaki "İnsan → وزر" kaydı da aynı kusuru taşıyor.
2. **NAS GEN yapısı (%62,7):** li'n-nâs ("insanlara / insanlar için") 51 · mine'n-nâs ("insanlardan kimi") 26 · ekseru'n-nâs ("insanların çoğu") 20 · diğer harf-i cer 23.
