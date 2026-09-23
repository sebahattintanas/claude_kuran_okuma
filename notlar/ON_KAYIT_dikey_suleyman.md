# ÖN-KAYIT — Süleyman merceği (açık anma · gizli dizi · dikey yığın)

Yazıldı: 2026-09-18T09:16:19Z · ÖLÇÜMDEN ÖNCE · morph.txt sha256[:16] = 742bfac59941b2cb
Normalizasyon: ALM pilotuyla aynı (`ON_KAYIT_dikey_ALM.md`).

## Tanımlar
- **Açık anma:** `LEM:سُلَيْمان` taşıyan kelime.
- **Gizli dizi:** isim DIŞINDA harf dizisi. Birincil biçim rasm **سليمن**; ikincil biçim tam yazım **سليمان**.
  - G1 kelime içi · G2 ayet içinde kelime sınırı atlayan · G3 ardışık kelimelerin baş harfleri
- **İskelet:** isim dışında bitişik س-ل-م dizisi; kaynağı morfolojiden ayrıştırılır.
- **Dikey yığın:** Süleyman ayetleri alt alta konur. Sütunlar: ilk kelime, son kelime (fâsıla), ismin ayet içi konumu, bir üst ayet ve bir alt ayet.
- **Komşuluk:** Süleyman ayetleri ile ±1 ayetlerindeki kökler. ×kat = gözlenen ÷ korpus beklentisi.
  Her kök için katkı veren FARKLI sahne sayısı da yazılır (sahne = aynı sûrede ardışık ayet kümesi).

## Boş modeller
- G2: ayet içinde kelime sırası permütasyonu, 1000 tekrar, tohum 0.
- G3: aynı permütasyon.
- Komşuluk: test yok, betimsel. Tek sahneden gelen yüksek ×kat artefakt sayılır (önceki bulgu, ×534,8 vakası).

## Tahminlerim
- **T1** Açık anma 17 token.
- **T2** 7 sûreye dağılır: 2, 4, 6, 21, 27, 34, 38.
- **T3** En çok anma sûre 27'de.
- **T4** G1+G2 (سليمن) isim dışında 3 vakayı geçmez; G2 permütasyon boşunun üstünde DEĞİL.
- **T5** G3 = 0.
- **T6** İsim dışındaki س-ل-م iskeletinin %90'dan fazlası سلم kökünden.
- **T7** Komşulukta en güçlü PN داود. ≥3 farklı sahneden katkı alan zenginleşmiş kök sayısı ≤5.

---
## SONUÇ (ölçümden sonra eklendi; yukarısı değiştirilmedi)
Betik: `betikler/dikey/suleyman_mercek.py` · çıktı: `ciktilar/dikey_suleyman.json`
Pozitif kontrol: sınır atlayan "قال|موسى" 17 kez bulundu; gizli dizi araması kör değil.

- **T1 TUTTU:** 17 token, 16 ayet (2:102'de iki anma).
- **T2 TUTTU:** 7 sûre (2, 4, 6, 21, 27, 34, 38).
- **T3 TUTTU:** sûre 27, 7 anma.
- **T4 TUTTU:** سليمن ve سليمان isim dışında G1 = 0, G2 = 0.
- **T5 TUTTU:** G3 = 0.
- **T6 TUTTU:** isim dışındaki س-ل-م iskeletinin 135/135'i (%100) سلم kökünden.
- **T7a KAPATILAMAZ:** "en güçlü PN" tanımsız bırakılmıştı. Ham sayıda اللَّه 12, داود 8; ×kat ölçüsünde داود önde.
  Lehte okuma seçilmedi. Ayrıca betikteki Allah dışlama süzgeci ÇALIŞMADI: elle yazdığım lemma dizgesinde
  şedde/hareke sırası korpustan farklı (bilinen hata, aday 945 ailesi).
- **T7b TUTTU (sınırda):** ≥3 sahne ve ×3 koşulunu sağlayan 5 kök: وهب, شكر, صلح, عمل, أتي.

## Yan kayıt: yatay alanların göremediği dikey çift (bulgu değil, tek vaka)
21:81 ve 34:12 aynı iki kelimeyle açılıyor: وَلِسُلَيْمَٰنَ ٱلرِّيحَ. Korpusta ikinci kelimesi الريح olan üç ayetten ikisi bunlar.
Çifti yakalamayan alanlar:
- `esit2`: bütün ayet benzerliği düşük.
- `nakarat3`: alt sınır 3 kelime.
- `ikili`: iki kelimenin ikisinin de köklü olmasını istiyor; Süleyman adının kökü yok.
**Araç açığı:** köksüz özel adlar `ikili`de yapısal olarak görünmez. Dondurulmuş borç listesine kaydedilir, onarılmaz.

## Tur sonu notu (anahtar denetimi)
Betikteki elle yazılmış hedef dizgeler anahtar_denetim.py'de ihlâl verdi (korpusta yok — zaten bulgunun kendisi).
Betik, hedefi ismin korpustaki rasm biçiminden TÜRETECEK şekilde düzeltildi. Bunun bedeli: ikincil hedef (tam yazım
سليمان) artık türetilemiyor. O biçimin sonucu ilk koşudan geçerlidir: G1 = 0, G2 = 0. Rasm biçimi (birincil) yeniden
koşuldu ve aynı sonucu verdi.
