# ÖN-KAYIT — İnsâna yüklenen sıfatların istisnaları

Yazıldı: 2026-09-18T11:13:20Z · ÖLÇÜMDEN ÖNCE · morph.txt sha256[:16] = 742bfac59941b2cb
Öncül: `ON_KAYIT_insan_sifat_ve_sira.md` (A).

## Küme
**Sıfat ayetleri (17):**
- Elle onaylanan 13 ayet: 4:28 · 14:34 · 16:4 · 17:11 · 17:67 · 17:100 · 22:66 · 33:72 · 42:48 · 43:15 · 70:19 · 76:2 · 100:6
- Bilinen kaçırmalar: 11:9 · 17:83 · 18:54 · 41:49

## Tanım
- **Pencere:** sıfat ayeti + aynı sûrede sonraki 3 ayet.
- **Aday:** penceredeki her إِلّا. Morfolojinin EXP / RES etiketinden BAĞIMSIZ; etiket ayrıca kaydedilir.
- **Elle sınıflama:**
  - **İSTİSNA:** sıfatı taşıyan insanlardan bir kısmını ayırıyor.
  - **DEĞİL:** sınırlama (hasr), başka bir cümleye ait istisna vb.
- İSTİSNA olanlarda istisna edilenlerin tanımı yazılır.

## Tahminler
- **T1** 17 ayetin en az 2'sinde pencerede İSTİSNA var (beklenen: 70:19 → 70:22, 11:9 → 11:11).
- **T2** Sıfat ayetlerinin çoğunluğu (≥ %70) İSTİSNASIZ.
- **T3** Her istisnada istisna edilenler bir EYLEM ya da TUTUMLA tanımlanıyor (iman, amel, sabır, namaz), bir kimlikle değil.
- **T4** Morfoloji etiketi elle sınıflamayla tam örtüşmüyor: en az bir İSTİSNA RES etiketli (11:11).

## İkincil (betimsel)
Aynı pencere ve aynı sınıflama, insân'ın geçtiği BÜTÜN 69 ayete uygulanır. Soru: insân'dan istisna edilenler kimler?

---
## SONUÇ (ölçümden sonra eklendi; yukarısı değiştirilmedi)
Betik: `betikler/dikey/sifat_istisna.py` · çıktı: `ciktilar/sifat_istisna_aday.json`

### Sıfat kümesi (17 ayet) — 11 aday, hepsi elle
- **İSTİSNA 2:**
  - 70:19 → 70:22 إِلَّا ٱلْمُصَلِّينَ (etiket EXP)
  - 11:9 → 11:11 إِلَّا ٱلَّذِينَ صَبَرُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ (etiket **RES**)
- **DEĞİL 9:** 4:29 · 16:7 · 17:67 · 17:102 · 42:48 · 42:51 · 17:85 · 18:55 · 18:56 (sınırlama ya da başka cümle).
- **T1 TUTTU** (2) · **T2 TUTTU** (15/17 = %88 istisnasız) · **T3 TUTTU** (namaz; sabır + sâlih amel) · **T4 TUTTU** (11:11 RES etiketli).

### İkincil — bütün insân ayetleri (23 aday)
- **Gerçek istisna 4:** 11:11 · 70:22 · 95:6 · 103:3.
  - 95:6 ve 103:3 sıfat kümesinde değil. Öncülleri (95:5 أَسْفَلَ سَافِلِينَ, 103:2 لَفِى خُسْرٍ) sıfat kalıbında değil, hâl ya da durum ifadesi. (A) kuralı bunları yapısal olarak göremez.
- **İstisna edilenlerin tanımı (4/4 eylem ya da tutum):**
  - 70:22 namaz (ardından 70:23-34 nitelik zinciri)
  - 11:11 sabır + sâlih amel
  - 95:6 iman + sâlih amel
  - 103:3 iman + sâlih amel + hakkı tavsiye + sabrı tavsiye
  - **ٱلصَّٰلِحَٰت 4 istisnanın 3'ünde** (11:11, 95:6, 103:3).
- Başka istisna (insân niteliğinden değil): 7:83, 27:57 "karısı hariç" (Lût'un ailesi).
- Hasr ama dikkat çekici: 53:39 "insana ancak çalıştığı vardır" · 25:50.

## KAPSAM KAYDI
LEM إِنسان, أُناس ve أَنَاسِيّ biçimlerini de içeriyor (MP, 6 token: 7:82 ve 27:56 dahil).
Önceki turlardaki "insân 71" sayısı bu 6 tokeni içerir. Tekil insân 65.
Düzeltme yapılmadı; etkisi küçük ama tanım açığı olarak kaydedildi.
