# Kur'an Derin Okuma

Kur'an'ı bir metin nesnesi olarak ölçen, ölçüm ile yorumu ayrı katmanlarda
tutan ve her iddiayı ön-kayıtlı istatistiksel testle sınayan bir okuma projesi.

## Durum

**1419 ayet okundu** — korpusun %22.8'i.
Sûre 1 (7), 2 (286), 3 (200), 4 (176), 5 (120), 6 (165), 7 (206), 8:1-40, 69-74 (219).

**Devam noktası: 8:41.**

| katman | dosya | durum |
|---|---|---|
| ölçüm | `ciktilar/defter.json` | 6236 ayet, 39 alan — betiklerden üretilir |
| okuma | `notlar/okuma_metni.json` | sûre 1-8 |
| mercek | `notlar/mercek_kayit.json` | 307 satır |
| bağlar | `notlar/okuma_baglantilari.json` | 108 çift, 91'i doğrulanmış |
| adaylar | `bulgular/aday_bulgular.json` | 108 aday, hiçbiri test edilmedi |

## Okuma standardı

Okuma düzeni, biçim kuralları ve yeni oturum açılış promptu:
**[`notlar/OKUMA_STANDARDI.md`](notlar/OKUMA_STANDARDI.md)**

Özet:
- 20 ayetlik bloklar; sûre başında makro profil, sonunda kapanış ölçümü
- Ayet başına üç katman: `›` ölçüm · `◇` matematikçi merceği · dikey okuma
- **Her Arapça ifadenin yanında Türkçesi** — istisnasız
- Ölçüm ve yorum satırları karışmaz
- **Katı kural:** okuma sırasında hiçbir hipotez test edilmez

## Kurulum

```bash
git clone https://github.com/sebahattintanas/claude_kuran_okuma
cd claude_kuran_okuma
python3 betikler/defter.py
python3 betikler/defter2.py
python3 betikler/defter3.py
python3 betikler/defter4.py
python3 betikler/defter5.py
python3 betikler/aktor2.py
python3 betikler/katman6.py
python3 betikler/graf2.py
```
~3 dakika. Girdi: `veri/morph.txt` (Quranic Arabic Corpus morfolojisi,
130.030 token) ve `veri/kuran_veri.json`.

## Defter şeması (39 alan)

| grup | alanlar |
|---|---|
| konum | `k` `ai` `ki` `n` |
| ölçü | `mora` `harf` `fs` |
| eksen | `A` `R` `esma` `esma_k` |
| morfoloji | `vf` `pas` `apc` `ppc` `irab` `zmn` |
| şahıs | `sah` `sahset` `bask` `ilt` `ilt_yon` |
| kip | `kip` `edim` |
| biçim | `fig` `sim` |
| sözlük | `say` `ikile` `hapaks` |
| bağ | `xref` `esit` `dugum` |
| aktör | `adli` `adsiz` `rol` |
| bağlam | `nuz` `tip` |
| bayrak | `z` `yildiz` |

## Yöntem ilkeleri

- **Ölçüm ≠ yorum.** İki katman ayrı dosyalarda tutulur; mercek satırı
  silindiğinde ölçüm ayakta kalmalıdır.
- **Konum-eşli null.** Allah lafzı yoğunluğu metnin ilk yarısında ~1.46 kat
  yüksek; her mesafe ölçümü konum-eşli permütasyonla sınanır. Düz null ile
  yapılmış eski ölçümler geri çekildi.
- **Motive eden gözlem kendi testinden dışlanır.**
- **Bonferroni standarttır.** Düzeltmeyi geçemeyen bulgu geri çekilir ve
  geri çekme kaydedilir.
- **Lemma anahtarları elle yazılmaz.** Unicode birleşik karakter sırası
  sessiz eşleşmeme üretir; anahtarlar korpus çıktısından kopyalanır.

## Geri çekilenler

Bu proje **null sonuçları ve geri çekmeleri de kaydeder**. Bkz.
`bulgular/aday_bulgular.json` → `D_geri_cekilenler`. Şu ana kadar üç iddia
geri çekildi (özel isim Allah-mesafesi sıralaması, İblîs'in konumsal derinliği,
Kur'an sayılarının asallığı) ve altı ölçüm hatası kaydedildi.

## En büyük eksik

**Kontrol korpusu yok.** Hiçbir bulgu şu an "bu Kur'an'a mı Arapça'ya mı ait"
sorusunu cevaplayamaz. Kur'an dışı Arapça bir karşılaştırma korpusu
projenin öncelikli ihtiyacıdır.
