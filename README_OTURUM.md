# Oturum 2 — 2026-08-08 · depoya eklenecek dosyalar

Mevcut depo dizin yapısını (`betikler/ bulgular/ tablolar/ notlar/ ciktilar/`)
aynen izler; dosyalar doğrudan ilgili klasörlere kopyalanabilir.

## Yapılan iş
**1419 ayet okundu** — korpusun %22.8'i:
sûre 1 (7), 2 (286), 3 (200), 4 (176), 5 (120), 6 (165), 7 (206), 8:1-40, 69-74 (219).

Okuma üç katmanlı: ölçüm (defterden) · matematikçi merceği (◇) · dikey okuma.

## KURULUM SIRASI (defter'i sıfırdan üretmek için)
```
betikler/defter.py    v1  temel şema (6236 ayet)
betikler/defter2.py   v2  bab / çatı / i'râb / zaman
betikler/defter3.py   v3  nüzûl, Mekkî-Medenî, esmâ, xref, yıldız
betikler/defter4.py   v4  şahıs, iltifât, kip, söz edimi
betikler/defter5.py   v5  fig alanı etiket tabanlı yeniden kuruldu
betikler/aktor2.py    v6  adlı/adsız aktör, rol, aktör tablosu
betikler/katman6.py   v7  simetri, esmâ konumu, bab profili, dağılım, kavram seyri
betikler/graf2.py     v8  ayet grafı + NAKARAT DÜZELTMESİ
```
Girdi: `veri/morph.txt`, `veri/kuran_veri.json`, `tablolar/nuzul.json`,
`tablolar/esma_listesi.json`, `tablolar/pn_lemma_listesi.json`. Süre ~3 dk.
`ciktilar/defter.json` TÜRETİLMİŞ — depoya konmayabilir.

## DEFTER ŞEMASI (43 alan)
konum: k, ai, ki, n | ölçü: mora, harf, fs | eksen: A, R, esma, esma_k
morfoloji: vf, pas, apc, ppc, irab, zmn | şahıs: sah, sahset, bask, ilt, ilt_yon
kip: kip, edim | biçim: fig, sim | sözlük: say, ikile, hapaks
bağ: xref, esit, dugum | aktör: adli, adsiz, rol | bağlam: nuz, tip | bayrak: z, yildiz

## notlar/ — dört katman, dördü de yeniden üretilemez
| dosya | içerik |
|---|---|
| `okuma_protokolu.json` | sekiz kilitli karar |
| `okuma_metni.json` | **okumanın kendisi** — sûre 1 tam, 2-8 sıkıştırılmış blok özeti |
| `mercek_kayit.json` | **307 matematikçi mercek satırı**, sûre 1-8 |
| `okuma_baglantilari.json` | **108 bağ çifti**, kural kodlu + güven etiketli + ters-bağ |
| `mercek_matematikci_ayet.json` | mercek protokolü (bağlılık kuralı, silme testi) |
| `denetim_jnn.json`, `denetim_res_exp.json` | tablo hataları |

### Bağ denetimi (bag_kurallari.py çıktısı)
108 çift: **91 doğrulandı** (L1 tam-ayet 12, L2 ortak dizi 55, L3 iskelet 22, L4 kök çifti 2),
3 zayıf (L5), **14 saf yargı (Y — lafzî temeli yok)**. Ters-bağ: 195 ayet.
Y etiketliler listelendi; bunlar bulgu değil, yorum.

## bulgular/aday_bulgular.json — 108 aday, on bölümde
KATI KURAL yürürlükte: okuma sırasında hiçbir test yapılmıyor.
**UYARI:** #13, #19, #31, #74 gibi adaylar okuma sırasında SAYILDI — yani
aranarak bulundu. Tur sonunda "N örnek var" diye değil, **"aranarak bulunmuş
N örnek"** diye işlem görmeli; testleri motive eden ayetler dışlanarak kurulmalı.

## ÖLÇÜM BORÇLARI
- `esma_listesi.json` bağlam ayırmıyor — dört istisna birikti:
  جَبَّار (5:22 kavim), بَرّ (5:96, 6:59, 6:97 = kara), عَلِيم (7:109, 7:112 = sihirbaz)
- `ربب` türevleri Rab sayılıyor: 4:23 رَبَٰٓئِب (üvey kız), 3:79/5:44/5:63 رَبَّٰنِيُّون,
  3:146 رِبِّيُّون → **Nisâ'nın Rab sayımı 7 değil 6**
- `جنن` tablo hatası (denetim_jnn.json) — 7:184 جِنَّة "delilik" ama "cennet" veriyor
- `kok_adlar.json` görüntü katmanı `kavram()` kullanmıyor: قوم→"kavim" (3:2 ٱلْقَيُّوم,
  4:34 قَوَّٰمُونَ), ولي→"velî" (تَوَلَّىٰ), عشر→sayı (4:19 عَاشِرُوهُنَّ = geçinme)
- `nuzul.json` **BELLEKTEN, doğrulanmadı** — bu alana dayanan bulgu kurulamaz
- Ayet grafında nakarat düzeltildi, iç-bağ ağırlıklandırması YAPILMADI
- **Kontrol korpusu (Kur'an dışı Arapça) YOK — projenin en büyük eksiği**

## SONRAKİ OTURUM
1. `git clone`, betikleri sırayla koştur
2. `notlar/okuma_protokolu.json` oku — sekiz karar orada
3. `notlar/okuma_metni.json` oku — 1419 ayetlik okumanın kaydı
4. **Okumaya 8:41'den devam**; sûre 9'dan itibaren okuma_metni TAM kipte yazılacak
