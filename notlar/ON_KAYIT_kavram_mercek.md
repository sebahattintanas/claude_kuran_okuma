# ÖN-KAYIT — Kavram merceği: Cennet · Sâlih kullar · Sâlih ameller · İnsan

Yazıldı: 2026-09-18T09:46:29Z · ÖLÇÜMDEN ÖNCE · morph.txt sha256[:16] = 742bfac59941b2cb
Öncüller: kişi merceği turları. Dersler: kendi kökü artefaktı · sûre ölçütü · lemma dizgesi korpustan çözülür.

## Kavram tanımları (lemma korpustan NFC ile çözülür)
- **C_dar** Cennet: LEM جَنَّة + PN (51).
- **C_genis** Cennet: LEM جَنَّة, bütün biçimler (149; dünyadaki bahçeleri de içerir).
- **S_kul** Sâlih kullar: LEM صالِح, PN değil, sayı MP veya MD (31).
- **S_amel** Sâlih ameller: LEM صالِحَة, FP (62).
- **I** İnsan: LEM إِنسان (71).
- Kapsam dışı ve ölçüm yapılmadan bırakılan: ناس, بَشَر, tekil صالِح.

## Ölçüm 1 — Kendine ait kökler (her kavram ayrı)
- Pencere: kavram ayetleri ±1 ayet.
- Kavram kelimesinin KENDİSİ sayımdan çıkarılır. Aynı köke ait başka kelimeler sayılır (örn. cin).
- Test: pencerede k ≥ 3 olan her kök. Hipergeometrik tek yönlü p; evren = korpus, çekiliş = pencere.
- **"Kendine ait" kökün üç koşulu:**
  1. p < 0,05 / m (m = beş kavramdaki toplam test sayısı)
  2. ×kat ≥ 2
  3. pencerede ≥ 3 farklı sûre
- **Sağlamlık:** Cennet sonucu yalnız C_dar ve C_genis'in İKİSİNDE de geçerse "sağlam" sayılır.

## Ölçüm 2 — Ayet sonu konumu (dikey sütun)
- Kavram tokeninin ayetin son kelimesi olma oranı.
- Taban: korpustaki bütün isim (N) tokenlerinin son kelime olma oranı.
- Çift yönlü binom. Aile = 4 (C_genis, S_kul, S_amel, I); Bonferroni eşiği 0,0125.

## Ölçüm 3 — Aynı ayette birliktelik
- 6 çift: C_genis, S_kul, S_amel, I.
- Hipergeometrik: evren 6236 ayet; gözlenen = ikisini birlikte taşıyan ayet sayısı.
- Yön, gözlenenin beklenenden büyük ya da küçük olmasına göre belirlenir; p çift yönlü.
- Aile = 6; Bonferroni eşiği 0,0083.

## Tahminlerim
- **T1** C_genis–S_amel birlikteliği beklenenin ÜSTÜNDE ve anlamlı.
- **T2** I–C_genis birlikteliği beklenenin ALTINDA (yalnız yön).
- **T3** S_kul ayet sonu oranı tabandan anlamlı YÜKSEK.
- **T4** I'nın kendine ait kökleri arasında خلق var ve كفر, ظلم, عجل, جهل'den en az biri var.
- **T5** Cennet'in sağlam kökleri arasında جري, نهر, خلد var.
- **T6** S_kul ≤ 3 kendine ait kök alır.
- **T7** C_dar'ın kendine ait köklerinin en az yarısı C_genis'te de geçerli.

---
## SONUÇ (ölçümden sonra eklendi; yukarısı değiştirilmedi)
Betik: `betikler/dikey/kavram_mercek.py` · çıktı: `ciktilar/kavram_mercek.json` · m = 823, eşik 6,1e-05

**Ön-kayıttaki kendi hatam:** C_genis'i 149 yazmıştım, gerçek sayı **147**. Envanterdeki جُنَّة ("kalkan", AYRI lemma, 2 geçiş) kaleme karışmış.
Tanım lemmaya bağlı olduğu için ölçüm doğru; yanlış olan yalnız ön-kayıttaki sayı. Koşulmamış aritmetik (aday 843 ailesi).

### Kendine ait kökler
| kavram | kökler |
|---|---|
| C_dar (5) | صحب · دخل · خلد · أدم · عمل |
| C_genis (17) | تحت · خلد · جري · دخل · نهر · فوز · صحب · صلح · عمل · نخل · أكل · عنب · ثمر · نور · نعم · رضو · أدم |
| S_kul (2) | وهب · نبأ |
| S_amel (9) | عمل · أمن · تحت · جري · جنن · خلد · أجر · كفر · نهر |
| I (4) | خلق · مسس · وزر · نطف |

### Tahminler
- **T1 TUTTU:** C–S_amel birlikte 20 ayet, beklenen 1,4, p = 2,4e-18.
- **T2 TUTTU (yön):** I–C 0 ayet, beklenen 1,58. Anlamlı değil (p = 0,40); tahmin yalnız yöndü.
- **T3 TUTTU:** S_kul ayet sonu 24/31 (%77,4), taban %10,6.
- **T4 DÜŞTÜ (kısmen):** خلق var; كفر, ظلم, عجل, جهل'den hiçbiri yok. Gelenler: مسس, وزر, نطف.
- **T5 DÜŞTÜ:** sağlam Cennet kökleri صحب, دخل, خلد, أدم, عمل. خلد var; جري ve نهر yalnız C_genis'te.
- **T6 TUTTU:** S_kul 2 kök.
- **T7 TUTTU:** C_dar'ın 5 kökünün 5'i C_genis'te de geçerli.

### Ayet sonu (Bonferroni 0,0125)
- S_kul %77,4 → YÜKSEK.
- C_genis %2,0 (p = 0,00013) · S_amel **%0,0** (p = 0,0015) · I %1,4 (p = 0,006) → üçü de anlamlı DÜŞÜK.
  Bu yön ön-kayıtta tahmin edilmemişti.

## Ölçüm SONRASI kontroller (ön-kayıtsız, KAPATILAMAZ)
1. **Formül cennetin çoğul biçimine bağlı.** Aynı ayette تحت + جري + نهر = 40 ayet (TAM SAYIM).
   - Cennet biçimi: çoğul cennât (FP) **33** · PN "el-Cenne" **3** · tekil 1 · cennet kelimesi yok 3.
   - T5'in düşmesinin açıklaması: "altından ırmaklar akan" formülü çoğul cennâta aittir; tekil PN'nin çevresi صحب / دخل / خلد'dir.
2. **Sâlihîn'in ayet sonu eğilimi kafiyeyle açıklanmıyor.**
   - Taban: öteki eril çoğul isimler (MP) %29,0 (1717/5925).
   - Sâlihîn %80,0 (24/30), binom p = 1,0e-08.
   - "-în" ekinin fâsıla uyumu tabanı %10,6'dan %29'a çıkarıyor, ama sâlihîn'i açıklamaya yetmiyor.
