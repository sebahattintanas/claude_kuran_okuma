# Oturum kapanışı — 2026-10-05 (ayrı oturum: lafızdan lafza aralık okuması)

Sûre okumasının DIŞINDA yapılan keşif oturumu. Ana okuma konumu DEĞİŞMEDİ: sûre 36 tam, devam 37:1.

## Yapılanlar
1. **Aralık okuması** — aralık = sûre içinde ardışık iki `LEM:اللَّه` tokeni arası (2.699 lafız → 2.614 aralık). 4 tohumla 16 rastgele aralık + elle açılanlar. Özet `notlar/ARALIK_OKUMASI.md`, sayımlar `betikler/aralik_olcum.py` → `ciktilar/aralik_olcum.json`.
2. **Adaylar 1023–1036, set `X_aralik`** (`betikler/aday_ekle_aralik.py`, idempotent). 1023 DÜŞTÜ (hal geçişi), 1028 ARTEFAKT, 1030'a güncelleme eklendi (defter lafız alanı Allâhümme'yi saymıyor).
3. **Ağır okumalar (NUMARASIZ gözlemler, ARALIK_OKUMASI.md):** 35:18→22 · 16:9→18 · 10:6→10 · 53:58→62. Sayfalar `ciktilar/aralik_*.html`, dikey `ciktilar/blok_dikey_*.json`.
4. **Mercek ön-kaydı denetimi (◈B, ◈K)** — `betikler/aralik_biyolog.py`, `aralik_kozmolog.py`. Biyoloji sözlüğü lafza göre DÜZ; gök-yer sözlüğü lafızdan sonra yoğun. **Ön-kayıt tetik kusurları ölçüldü** (aşağıda).
5. **Ters okuma (mushafın sonundan)** — `ciktilar/sondan_01_30_ters_mushaf.html` (114:6→108:3), `sondan_31_60_ters_mushaf.html` (108:2→103:1); üretici `betikler/ters_onluk_sayfa.py`, `sondan_*_uret.py`. Sûre 103–114 okunmadı: meal çalışma çevirisi, gözlemler KAPATILAMAZ.
6. **KATMAN 1 — bütün Kur'an** — `ciktilar/kuran_aralik_sayfalari.html` (tek dosya ~4 MB): lafız-çapalı bloklar, eşik 200 kelime (kullanıcı kararı) → 320 sayfa; Mushaf/Ters gezinme. Üretici `betikler/kuran_aralik_sayfalari.py` + `kuran_aralik_sablon.html`. İşaretler otomatik, doğrulanmamış.
7. **Eşzamanlı okuyucu (ONAYLI tasarım):** `ciktilar/okuyucu_ornek_sondan.html`, `betikler/okuyucu_ornek.py`; taslak meal tohumu `tablolar/calisma_meali.json` (90 ayet, 100–114). Tam Kur'an sürümü yeni oturumda.
8. **Yön testi (ön-kayıtlı):** `notlar/ONKAYIT_yon_testi.md` — omnibus, L→O, L→E TUTTU; R→O KISMİ; dilbilgisi kontrolü önerildi.
9. **Simetri testleri (keşif):** `betikler/simetri_olcum.py` — genel palindrom/halka yok; yerel ritim tutarlı.
10. **Araç onarımı:** `kok_turkce.json` 1165 → **1167** (سوم, سمد; `betikler/kok_ekle_aralik.py`, `yama_retroaktif_gloss_aralik.py`). Yama 0, türkçe 0, anahtar 70 (PYTHONHASHSEED=0, ihlal farkı 0).

## Açık kararlar / borçlar (onarılmadı)
* **Mercek ön-kaydı (`ONKAYIT_mercekler.md`, dondurulmuş) kusurlu:** ◈K ölü kök `ريح` (korpus روح) ve `ساعة` (korpus سوع); yanlış kök `سنن` (yıl = سنو); سمو'da ad lemmaları. ◈B: نعم'un 107/140 tokeni nimet. Öneri §8 sapması olarak `ARALIK_OKUMASI.md`'de — UYGULANMADI.
* **145 karşılıksız kök** okunmuş ayetlerde (sûre 9–19 ağırlıklı) — `ciktilar/karsiliksiz_kokler_okunan.json`; `turkce_denetim.py` tabloda olmayan kökü görmüyor.
* **1030** — vokatif Allâhümme lafız sayılsın mı.
* **1027 / 1025** — aday 435 yeniden testine iki yönlü mesafe ve taşıyıcı duyarlılık katmanları.

## Diğer oturuma not (sûre 37)
> Depoda yeni: `X_aralik` adayları 1023–1036. Sûre 37 adayları **1037'den** başlar, set adı `AV_saffat` aynı. `kok_turkce.json` **1167** kök. Mercek ön-kaydında ölçülmüş tetik kusurları var (◈K ريح/ساعة ölü, سنن yanlış; ◈B نعم) — sûre 37'de ◈K/◈B satırları bu kusurla üretilir; §8 kararı bekliyor. Okumayı bloke eden bir şey yok.

## Denetimler
türkçe 0 · anahtar 70 (ihlal farkı 0) · `aday_bulgular.json` farkı yalnız ekleme · `okuma_metni.json` değişmedi.
