# ÖN-KAYIT — (1) Ayırt eden kökler AYET birimiyle · (2) insân dikey yığını

Yazıldı: 2026-09-18T10:15:06Z · ÖLÇÜMDEN ÖNCE · morph.txt sha256[:16] = 742bfac59941b2cb
Öncül: `ON_KAYIT_insan_uclu.md` (وزر token şişmesi + eşsesli; aday 926 dersi).

## (1) Birim düzeltmesi
Bir kök bir ayette kaç kez geçerse geçsin **1** sayılır. Test birimi ayettir:
- evren = pencere birleşimindeki ayetler,
- çekiliş = özel bölgenin ayetleri,
- k = kökü taşıyan özel bölge ayeti sayısı.
Hipergeometrik tek yönlü p. Kavramın kendi kelimesi yine sayım dışı.
Koşullar önceki turla aynı: p < 0,05 / m · ×kat ≥ 2 · ≥ 3 sûre · k ≥ 3.

İki koşu:
- **1a** insân / nâs / beşer karşılaştırması (evren = üç pencerenin birleşimi).
- **1b** insân tek başına, korpusa karşı (evren = 6236 ayet). Kavram merceği turundaki INS sonucunun düzeltmesi.

### Tahminler
- **T1** وزر 1a'da da 1b'de de düşer.
- **T2** خلق 1a'da ve 1b'de kalır.
- **T3** مثل 1a'da BES için kalır.
- **T4** 1b'de نطف ve مسس kalır.

## (2) Dikey yığın — BETİMSEL, test yok
insân'ın geçtiği her ayet bir satır. Sütunlar:
- ayet · Mekkî/Medenî
- iniş sırası — `nuzul.json` DOĞRULANMAMIŞ; yalnız betimsel sütun
- insân'ın hâli (NOM / ACC / GEN) ve ayet içi göreli konumu
- aynı ayetteki fiiller (lemma), en yakın fiil
- ayette خلق veya مسس var mı
- Arapça metin

Yığından çıkan her örüntü KAPATILAMAZ olarak kaydedilir ve ancak ayrı bir ön-kayıtla sınanabilir (aday 899: taraflı örneklem yasağı).

---
## SONUÇ (ölçümden sonra eklendi; yukarısı değiştirilmedi)
Betikler: `betikler/dikey/insan_ayet_birimi.py`, `insan_yigin.py`
Çıktılar: `ciktilar/insan_ayet_birimi.json`, `insan_yigin.json`, `insan_yigin.md`

### (1) Ayet birimi
- **1a** (m = 575):
  - INS: خلق (30 ayet, ×2,9, 21 sûre)
  - NAS: أله ×3,3 · أيي ×3,0 · أمن ×2,4 · كثر ×4,2
  - BES: قول ×2,2 · مثل ×4,1
- **1b** INS korpusa karşı (m = 128): خلق ×5,3 · مسس ×6,6 · نطف ×22,1 · **شرر ×7,7 (yeni)**

Tahminler: **T1 TUTTU** (وزر iki koşuda da yok) · **T2 TUTTU** · **T3 TUTTU** · **T4 TUTTU**.
Kavram merceği turundaki "INS → وزر" ve insân üçlüsündeki "INS → وزر" kayıtları DÜŞTÜ: sebep token birimi + eşsesli (75:11).

### (2) Dikey yığın — betimsel, KAPATILAMAZ
- 71 token / 69 ayet. Hâl: NOM 29 · ACC 28 · GEN 14. İlk üçte bir konumu: 43/71.
- En yakın fiil: خلق 14 · كون 6 · قول 4 · علم, مسس, ذكر, وصي 3'er.
- خلق içeren ayetlerde insân: ACC 12 · NOM 5 · GEN 1 (yaratılan = nesne).
- **"Zarar / dua / nimet" döngüsü:** katı tanımla (مسس + دعو + {نعم, خول, رحم} aynı ayette) korpusta 4 ayet:
  39:8, 39:49, 41:51 (insân) · 30:33 (nâs).
  Yığında aynı sahneyi taşıyıp tanıma girmeyenler: 10:12 (كشف), 17:67, 17:83 (دعو yok), 41:49.
  **Tanım sahneyi yakalamıyor; iki ayetlik pencere + كشف ile yeniden tanımlanıp ön-kayıtla sınanmalı.**
- **Gloss borcu #5b yine:** `kok_turkce` عرض = "sunma", ama أَعْرَضَ (17:83, 41:51) = "yüz çevirdi".
  Yığının "en yakın fiil" sütunu kök gloss'u kullandığı için bu satırlarda anlam yanlış görünüyor.
