# ÖN-KAYIT — Dikey mercek pilotu: ا-ل-م harf dizisi (mukattaa dışı)

Yazıldı: 2026-09-18T09:11:24Z · ÖLÇÜMDEN ÖNCE · morph.txt sha256[:16] = 742bfac59941b2cb

## Soru
ا-ل-م harf dizisi, mukattaa kelimeleri dışında, kökten bağımsız olarak nerede ve hangi ölçekte yan yana geliyor?

## Normalizasyon (rasm)
- Hareke, sükûn, şedde, tenvin, dagger elif (U+0670), küçük harfler (U+06D6-06ED), tatvîl çıkarılır.
- ٱ أ إ آ → ا. ء, ى, ة ayrı harf olarak kalır.
- Kelime = morph.txt'te aynı (sûre:ayet:kelime) segmentlerinin birleşimi.
- INL etiketli kelimeler (mukattaa) sayıma girmez; ayrı raporlanır.

## Ölçekler
- **Ö1** kelime içinde bitişik ا ل م
- **Ö2** ayet içinde boşluklar silindiğinde bitişik ا ل م — yalnız kelime sınırını ATLAYAN ek vakalar
- **Ö3** ayet içinde ardışık üç kelimenin ilk harfleri ا, ل, م
- **Ö4** sûre içinde ardışık üç ayetin ilk harfleri ا, ل, م (akrostiş)

## Boş modeller
- Ö1/Ö2: vakalar morfolojiye göre ayrıştırılır (ال harf-i tarifi mi, أَلَمْ mı, kök içi mi).
- Ö3: ayet içinde kelime sırası permütasyonu, 1000 tekrar, tohum 0.
- Ö4: sûre içinde ayet sırası permütasyonu, 1000 tekrar, tohum 0.
- Tek yönlü p = (gözlenen kadar veya daha büyük permütasyon sayısı + 1) / 1001. İki test → Bonferroni eşiği 0,025.

## Tahminlerim (ölçümden önce)
- **T1** Ö1 vakalarının %90'dan fazlası ال harf-i tarifi + م ile başlayan kelimeden gelir (tanım harfi artefaktı).
- **T2** Ö1 içinde rasmı tam olarak "الم" olan kelime = أَلَمْ; mukattaa ile aynı iskelet. Ayrı sayılır.
- **T3** Ö3, permütasyon boşuna göre anlamlı DEĞİL (p > 0,025).
- **T4** Ö4, permütasyon boşuna göre anlamlı DEĞİL (p > 0,025).

---
## SONUÇ (ölçümden sonra eklendi; yukarısı değiştirilmedi)
Betik: `betikler/dikey/alm_pilot.py` · çıktı: `ciktilar/dikey_alm_pilot.json`

| | gözlenen | boş model | sonuç |
|---|---|---|---|
| Ö1 kelime içi | 1179 | — | ال+م 1087 (%92,2) · أَلَمْ 78 · kök içi 14 |
| Ö2 sınır atlayan | 151 | — | ek vaka, ayrıştırılmadı |
| Ö3 kelime başları | 87 | 88,5 ± 9,5 | p = 0,58 |
| Ö4 ayet başları | 2 (13:33, 41:41) | 1,16 ± 1,08 | p = 0,33 |

- T1 TUTTU (%92,2 > %90) · T2 TUTTU (78/78 = أَ + لَمْ, morfolojiyle doğrulandı) · T3 TUTTU · T4 TUTTU
- Yan kayıt (bulgu değil): أَلَمْ iki sûrenin ilk kelimesi (94:1, 105:1); rasmı mukattaa الٓمٓ ile aynı.
  "Sûre başı dikeyi" merceğine devredilir, orada ön-kayıtla sınanır.
