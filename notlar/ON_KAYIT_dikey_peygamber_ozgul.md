# ÖN-KAYIT — Her peygamber adının kendine ait (özgül) kökleri

Yazıldı: 2026-09-18T09:33:22Z · ÖLÇÜMDEN ÖNCE · morph.txt sha256[:16] = 742bfac59941b2cb
Öncül: `ON_KAYIT_dikey_suleyman_davud.md` (sahne tanımı zayıf çıktı → sûre sayısı eklendi).

## İsim kümesi
Korpusta PN etiketli 24 peygamber lemması. Dizgeler korpustan kopyalanır, elle yazılmaz.
- Îsâ = عِيسَى + مَسِيح.
- **Kapsam dışı (PN etiketi yok):** Zülkifl ve Ahmed (61:6). Bu bir araç sınırıdır; eksiklikleri metin hakkında bir şey söylemez.

## Tanımlar
- **Pencere(N):** N'nin anma ayetleri ±1 ayet.
- **Havuz U:** 24 pencerenin birleşimi.
- **Özel bölge(N):** Pencere(N) eksi öteki 23 pencere.
- **Sayım birimi:** kelime. Bir kök bir kelimede bir kez sayılır.
- **Test:** özel bölgede k ≥ 3 olan her (N, kök) çifti test edilir.
  - Hipergeometrik tek yönlü p: çekiliş = özel bölgenin kelimeleri, evren = U'nun kelimeleri.
  - ×kat = özel bölgedeki oran ÷ U'nun geri kalanındaki oran.
- **"Kendine ait" kökün üç koşulu:**
  1. p < 0,05 / m (m = test edilen çift sayısı, Bonferroni)
  2. ×kat ≥ 3
  3. kökün özel bölgede geçtiği **farklı sûre sayısı ≥ 2**
- **Tek-sûre sınıfı:** 1. ve 2. koşulu sağlayıp 3.'yü sağlamayanlar ayrı listelenir. Kıssa artefaktı adayı sayılırlar, sonuç değil.

## Tahminlerim
- **T1** En çok "kendine ait" kökü Mûsâ taşır.
- **T2** Anması 5'in altında olan adlar (İdrîs, İlyâs, Elyesa, Muhammed, Eyyûb, Yûnus) 0 kök alır.
- **T3** İshak'ın özel bölgesi ≤ 3 ayettir (hep İbrâhim ve Yakub ile anılır).
- **T4** Tek-sûre sınıfı, "kendine ait" sınıfından büyüktür (kıssalar tek sûrede yoğunlaşır).
- **T5** Yûsuf'un tek-sûre sınıfında سجن ve قمص var; üç koşulu geçen kökü 0 (tamamen sûre 12'de).
- **T6** Süleyman ≤ 2 kök alır; Dâvûd'un أوب kökü "kendine ait" sınıfına GİRMEZ, çünkü ≥ 2 sûre koşulunu sağlasa bile k küçük.

---
## SONUÇ (ölçümden sonra eklendi; yukarısı değiştirilmedi)
Betik: `betikler/dikey/peygamber_ozgul.py` · çıktılar: `ciktilar/dikey_peygamber_ozgul.json` (ön-kayıtlı) ve `..._isimharic.json` (sapma)

**Koşu sırasında yakalanan hata:** elle yazdığım أَيُّوب ve مُحَمَّد korpusta yoktu (şedde/hareke sırası farkı; aday 945 ailesinin dördüncü tekrarı).
Bu sefer betiğe konan doğrulama satırı hatayı sessiz bırakmadı ve koşuyu durdurdu. Dizgeler NFC eşleştirmesiyle korpustan çözüldü.

### Ön-kayıttan SAPMA — kendi kökü artefaktı
Bazı adların morfolojide kendi kökü var: Âdem → أدم, Hûd → هود, Sâlih → صلح, Muhammed → حمد, el-Mesîh → مسح.
Ön-kayıt anma kelimelerini dışlamıyordu; bu beş kök totolojik olarak "kendine ait" çıktı.
- Özgün sürüm korundu: 20 ait, 8 tek-sûre, m = 641.
- Sapma sürümü (`--isim-haric`, peygamber adı olan kelimeler sayım dışı): **15 ait, 8 tek-sûre, m = 636**.

### Tahminler
- **T1 DÜŞTÜ:** en çok kök Mûsâ'da değil. Îsâ 4 (özgünde 5), Âdem 3, İbrâhim 3, Mûsâ 2.
- **T2 özgünde DÜŞTÜ** (tek istisna Muhammed → حمد, kendi kökü artefaktı) · **sapmada tutar**.
- **T3 TUTTU:** İshak özel bölgesi 2 ayet. İsmâil 0, Elyesa 0, Yakub 2.
- **T4 DÜŞTÜ:** tek-sûre sınıfı 8, ait sınıfı 15 (özgünde 20). Kıssa çekirdekleri sûreler arası tekrar ediyor.
- **T5 DÜŞTÜ (kısmen):** Yûsuf'un ait kökü 0 tuttu; ama tek-sûre sınıfında سجن ve قمص YOK. Gelenler: أبو, أخو, جهز, سرق.
- **T6 TUTTU:** Süleyman 0 ait (tek-sûre: نمل); Dâvûd'un أوب kökü ait sınıfında yok (Dâvûd'unki: بعض).

### Okuma sınırları (ölçüm sonrası; her biri bir araç açığı, metin iddiası değil)
1. **Unvan artefaktı:** Îsâ → بني kökünün 19/22'si ابْن ("Meryem oğlu" unvanı). Kendi kökü artefaktının ikinci kuşağı. Sapma sürümü bunu dışlamıyor.
2. **Ad ≠ kişi:** Hârûn → خوف (4/4 خافَ, 26 ve 28) aslında Mûsâ'nın korkusu. Mûsâ o ayetlerde zamirle anılıyor ve ada dayalı pencere zamiri görmüyor.
   Mercek "ada yakınlığı" ölçüyor, "kişiye yakınlığı" değil.
3. **Gloss borcu #5b somutlaştı:** `kok_turkce` بني = "bina" diyor ama bölgedeki kullanım "oğul". لقي = "karşılaşma" diyor ama 22/29 "atmak".
   حور ve مسح tabloda YOK (okumada karşılaşılmamış kökler).
4. **Tek-sûre sınıfı kıssaya değil sahne komşuluğuna bağlı:** Zekeriyyâ → وضع aslında Meryem'in doğumu (3:36). Pencere yan sahneyi içeri alıyor.
