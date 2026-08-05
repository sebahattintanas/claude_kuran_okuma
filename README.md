# Kuran Okuma — Hesaplamalı Metin Analizi

Kuran metnini ampirik bir korpus olarak inceleyen çok oturumlu araştırma projesi.
Yöntem: harf → kök → kavram katmanları, Jaccard uzaklığı, permütasyon testleri.
İlke: ölçülebilir ve yanlışlanabilir olmayan hiçbir iddia yok.

## Klasör Yapısı

| Klasör | İçerik |
|---|---|
| `veri/` | Ham korpus: `morph.txt` (130.030 satır morfolojik etiket), `kuran_veri.json` (Diyanet meali). Kaynaklardan yeniden indirilebilir. |
| `tablolar/` | Elle üretilmiş temel veri: kök→kavram tablosu (2.188 eşleme), ayet düzeyi istisnalar, kök denetim kayıtları, kavram sözlükleri. **Projenin asıl emeği burada.** |
| `betikler/` | Analiz altyapısı: `kuran_akis.py` (v2, kelime akışı), `dikey_oku.py` (dikey okuma + anlamlılık testi), `tablo_dogrula.py` (doğrulama) ve diğerleri. |
| `bulgular/` | `bulgu_*.json` — kalıcılık kuralı gereği her önemli bulgu adlandırılmış dosyaya yazılır. |
| `ciktilar/` | Türetilmiş görseller ve HTML okuyucular (betiklerle yeniden üretilebilir). |
| `notlar/` | `YAPILACAKLAR.md`, `OKUMA_SISTEMI_OZET.md`, deney durakları. |

## Veri Kaynakları

- Morfoloji: [mustafa0x/quran-morphology](https://github.com/mustafa0x/quran-morphology) — `quran-morphology.txt`
- Meal: [fawazahmed0/quran-api](https://github.com/fawazahmed0/quran-api) — `editions/tur-diyanetisleri.json`

## Oturum Başlangıcı (Claude için)

```bash
# Ham veriyi indir (projede tutulmaz)
curl -sL -o morph.txt https://raw.githubusercontent.com/mustafa0x/quran-morphology/master/quran-morphology.txt
# Depodan tabloları ve betikleri çek, çalışma dizinine kopyala
```

## Kritik Kurallar

- `kok_anlam_tablosu.json` anahtarları asla elle yazılmaz — Unicode birleştirme sırası farkları sessiz eşleşme hatası üretir; anahtarlar korpus çıktısından kopyalanır, NFC ile eşlenir.
- Şedde ayrıştırması: كذّب / كذب ayrı köklerdir; Allah tespiti `_ciplak()` ile yapılır.
- Her yapısal değişiklikten sonra `tablo_dogrula.py` çalıştırılır.
