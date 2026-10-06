# ÖN-KAYIT — Yön testi: lafzın etrafında "ok" var mı? (2026-10-05, aralık oturumu)

Bu belge sonuç görülmeden yazıldı (2026-10-06T06:19:55Z); betik (`betikler/yon_testi.py`) bu belgeden SONRA yazılıp koşulur. Sapma §6'ya.

## 1. Soru
Lafız ve taşıyıcılar metinde belirli bir sırayla mı diziliyor (önce ad, sonra izi), yoksa düz ve ters sıra istatistiksel olarak ayırt edilemez mi?

## 2. Veri ve olay dizisi
`veri/morph.txt`, her kelime için tek bir durum (öncelik sırasıyla): L = LEM اللَّه · R = LEM رَبّ · E = esmâ_listesi lemması · O = PRON + 3MS (bağımsız ya da ek zamir) · B = 1P içeren kelime · P = PASS içeren kelime · 0 = hiçbiri.
Olay dizisi: 0'lar atılır, ardışık olaylar sayılır; yalnız AYNI SÛRE içindeki geçişler. Aynı durumun tekrarı (i→i) sayılmaz.
Not: O, B, E göndergesi doğrulanmamıştır (insan 3MS, kulun 1P'si, insana sıfat esmâ dahil) — bu gürültü testi zorlaştırır, yanlış pozitif üretmez.

## 3. Null model
Her AYET içindeki olay sırası 0,5 olasılıkla ters çevrilir (1.000 tekrar, tohum 2026). İçerik ve ayet sırası korunur, ayet içi yön bilgisi yok edilir.

## 4. Hipotezler (yönleri önceden belirlenmiş)
* **H0 (omnibus):** zaman-tersinme asimetrisi A = Σ_{i<j} |n(i→j) − n(j→i)| / Σ_{i≠j} n(i→j); düz dizide null'un üst %5'inin üstünde.
* **P1:** n(L→O) − n(O→L) > 0 ve null'un üst %5'inin üstünde (önce ad, sonra zamir).
* **P2:** n(L→E) − n(E→L) > 0, aynı ölçüt (ad, sonra sıfat/yüklem).
* **P3:** n(R→O) − n(O→R) > 0, aynı ölçüt (Rab da çapa — 105/106 gözlemi).

## 5. Karar kuralı
Korpus tek/çift sûre numarasına göre iki yarıya bölünür. Bir hipotez ancak İKİ YARIDA DA tek yönlü p < 0,05 ise "tuttu" sayılır. Tek yarıda tutan "kısmi"; hiçbirinde tutmayan "tutmadı". Çoklu karşılaştırma: 4 hipotez × 2 yarı; iki yarıda birden şartı Bonferroni yerine kullanılır (her biri 0,05² ≈ 0,0025 ortak yanlış pozitif).

## 6. Sapmalar
(boş)

## 7. Sonuç (koşu sonrası eklendi; betik ve null ön-kayıttaki gibi, sapma yok)
`ciktilar/yon_testi.json`. Olay geçişi: tek 4.468 · çift 4.973.
| | tek (gözlenen / null / p) | çift (gözlenen / null / p) | karar |
|---|---|---|---|
| A omnibus | 0,0815 / 0,0322 / 0,001 | 0,0855 / 0,0316 / 0,001 | **TUTTU** |
| P1 L→O − O→L | +47 (362/315) / 1,8 / 0,003 | +53 (445/392) / 12,7 / 0,011 | **TUTTU** |
| P2 L→E − E→L | +24 (267/243) / −0,6 / 0,031 | +38 (315/277) / −4,7 / 0,002 | **TUTTU** |
| P3 R→O − O→R | +9 (122/113) / −10,5 / 0,039 | +20 (143/123) / 7,0 / 0,118 | **KISMİ** |
**Yorum sınırı:** yön var; ama P1 Arapçada zamirin öncülünden sonra gelmesiyle, P2 ad cümlesinde öznenin yüklemden önce gelmesiyle (إِنَّ ٱللَّهَ عَلِيمٌ) beklenen yönde. Test, yönün METNE ÖZGÜ mü yoksa DİLBİLGİSİNDEN mi geldiğini ayırmıyor.
**Önerilen sonraki ön-kayıt (kontrol):** aynı istatistik başka özel isimlerle (مُوسَى, إِبْرَٰهِيم, فِرْعَوْن …) → 3MS; lafzın asimetrisi bu kontrol isimlerinkinden büyük mü?
