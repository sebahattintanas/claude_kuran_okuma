# ÖN-KAYIT — Elçi kıssası kalıbı: Nûh · Hûd · Sâlih · Şuayb · Lût ortak söz dağarcığı taşıyor mu?

Yazıldı: 2026-09-18T09:41:02Z · ÖLÇÜMDEN ÖNCE · morph.txt sha256[:16] = 742bfac59941b2cb
Öncül: `ON_KAYIT_dikey_peygamber_ozgul.md` (Nûh 78 ayetlik özel bölgeye rağmen 0 kök aldı).

## Veri düzeltmesi (tasarım sırasında bulundu, ölçümden önce)
Morfoloji 2:111, 2:135 ve 2:140'taki هُودًا ("Yahudi") kelimesini PN Hûd olarak etiketliyor.
Hûd anmasının 3/10'u yanlış. Bu üç token Hûd anmasından ÇIKARILIR.
Önceki turun Hûd sonucu bu hatayla kirlidir; özgün kayıt korunur.

## Tanımlar
- **Özel bölge:** önceki turla aynı. ±1 ayet pencere, öteki 23 pencere çıkarılır.
  Peygamber adı olan kelimeler sayım dışıdır (önceki turun sapması artık standart ve burada ölçümden önce ilan ediliyor).
- **Evren:** özel bölgesi ≥ 10 ayet olan adlar.
- **Grup E:** Nûh, Hûd, Sâlih, Şuayb, Lût.
- **Vektör:** her adın özel bölgesindeki kök sayımı.
  - Ağırlık: tf × idf, idf = ln(evrendeki ad sayısı / o kökü taşıyan ad sayısı).
  - Benzerlik: kosinüs.

## Testler (aile = 2, Bonferroni eşiği 0,025)
- **M1:** E'nin 10 çiftinin ortalama kosinüsü.
  Boş model: evrenden seçilebilecek bütün 5'li kümeler (tam sayım). p = ortalaması ≥ E'ninki olan küme oranı.
- **M2 (sûre karıştırıcısı ayıklanmış):** her çift (A, B) için A'nın vektörü yalnız B'nin HİÇ özel ayeti olmayan sûrelerden, B'ninki yalnız A'nınkinin olmadığı sûrelerden kurulur.
  Böylece iki ad aynı sûrede anlatılıyorsa o sûre ikisinin karşılaştırmasına girmez. İki taraftan biri 30 kelimenin altına düşerse çift düşürülür.
  Boş model M1 ile aynı: tam sayım, tüm 5'li kümeler.
- **M3 (betimsel):** E'nin özel bölgeleri birleşiminde, E'nin 5 adından en az 4'ünün bölgesinde geçen kökler.
  Evrenin geri kalanına göre ×kat ile sıralanır.

## Tahminlerim
- **T1** M1 anlamlı (p < 0,025).
- **T2** M2 de anlamlı (p < 0,025), ama M1'den zayıf.
- **T3** M3 listesinde قوم, كذب, رسل, عذب bulunur.
- **T4** E içinde öteki dördüne ortalama benzerliği en yüksek olan Hûd'dur.

---
## SONUÇ (ölçümden sonra eklendi; yukarısı değiştirilmedi)
Betik: `betikler/dikey/elci_kalibi.py` · çıktı: `ciktilar/elci_kalibi.json`
Evren 14 ad · tüm 5'li kümeler 2002 · Hûd düzeltmesi uygulandı (3 token).

- **T1 DÜŞTÜ.** M1: E ortalaması 0,151; 2002 kümede 413. sıra; **p = 0,206**.
  - Nûh'un en yakın üç komşusu E'den değil: Mûsâ 0,329 · İbrâhim 0,266 · Îsâ 0,258. Lût'unki de Mûsâ.
  - E içinde tek güçlü çift Sâlih–Şuayb (0,309). Bu, 2002 kümenin en yüksek ortalamasından (0,27) bile büyük.
    Ama ikisi aynı üç sûrede (7, 11, 26) anlatılıyor.
- **T2 DEĞERLENDİRİLEMEZ — M2 ÇÖKTÜ.** E'nin 10 çiftinin 9'u, ortak sûreler çıkarılınca 30 kelimenin altına düştü; geriye tek çift kaldı (Lût–Nûh).
  Bu beş kıssa sûre dağılımından AYRILAMIYOR. p = 0,964 tek çifte dayanıyor ve bilgi taşımıyor. KAPATILAMAZ.
- **T3 TUTTU.** قوم (×3,3) · كذب (×4,7) · رسل (×2,3) · عذب (×1,7) M3'te; dördü de 5/5 adda.
  M3'ün başı: عود ×13,7 · نجو ×7,3 (5/5) · غير ×6,5 · كذب ×4,7 · جرم ×3,4.
- **T4 DÜŞTÜ.** E içi ortalama benzerlikte en yüksek Sâlih (0,179); Hûd 0,144.

## Ölçüm sonrası (ön-kayıtsız, KAPATILAMAZ)
- TAM SAYIM: "مَا لَكُم مِّنْ إِلَٰهٍ غَيْرُهُۥ" korpusta 9 ayette geçiyor:
  7:59, 7:65, 7:73, 7:85, 11:50, 11:61, 11:84, 23:23, 23:32.
  Nûh 2 · Hûd 2 · Sâlih 2 · Şuayb 2 · adsız elçi 1. Lût 0 · Mûsâ 0 · İbrâhim 0.
- **Yöntem dersi (projenin tekrar eden dersi: doğru kavram, yanlış birim).** Kalıp birkaç formül kökünden oluşan küçük bir çekirdek.
  Bütün söz dağarcığı kosinüsü onu seyreltiyor. Kalıbı sınayacak birim KELİME VEKTÖRÜ DEĞİL, FORMÜL (n-gram) düzeyi.

## Araç kaydı
Morfoloji 2:111, 2:135 ve 2:140'ta "hûden" (Yahudi) kelimesini PN Hûd olarak etiketliyor.
`pn_turleri.json` ve adlı aktör alanları (`adli`, `adli2`) bundan etkilenmiş olabilir — kontrol edilmedi. Dondurulmuş borç: kaydedildi, onarılmadı.
