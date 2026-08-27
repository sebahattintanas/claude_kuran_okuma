# Depo güncellemesi — 2026-08-26 oturumu

Bu klasördeki dosyalar depodaki **aynı yollara** kopyalanır (üzerine yazılır).
Klasör yapısı depoyla birebir aynıdır.

    cp -r depo_guncelleme/* /depo/yolunuz/

## Değişen 19 dosya

### Okuma kaydı (bunlar oturumun asıl çıktısı)
- `notlar/okuma_metni.json` — sûre 20 TAM (135 ayet) + sûre 21 makro ve 1-20.
  **154 dikey satırı yeniden üretildi** (komşuluk zenginleşmesi geri geldi).
- `notlar/mercek_kayit.json` — sûre 20: 135 mercek + biyolog 13 + uzay 15 ·
  sûre 21: 20 mercek + biyolog 3 + uzay 5
- `notlar/okuma_baglantilari.json` — `Z_taha` 68 bağ · `AA_enbiya` 9 bağ
- `bulgular/aday_bulgular.json` — 415 → **437** aday

### Tablo
- `tablolar/kok_turkce.json` — **314 → 720** kök karşılığı

### Betik
- `betikler/turkce_denetim.py` — alan kapsamı genişletildi:
  `olcum`, `mercek`, **`dikey`, `derin`, `derin2`**

### Standart ve borçlar
- `notlar/OKUMA_STANDARDI.md` — dört yeni kural bölümü
- `notlar/YAPILACAKLAR.md` — 435 P0'ın başına alındı
- `notlar/OTURUM_2026-08-26_KAPANIS.md` — YENİ, açılış promptu bunu okuyor

### Yeni ölçüm dosyaları
- `notlar/derin_bakis_gorme_soyleme.json` — YENİ
- `ciktilar/allah_hizalama.html` — YENİ, görselleştirme
- `ciktilar/anahtar_denetim_raporu_tohum0.txt` — YENİ, sabit tohumlu taban

### Geçerlilik uyarısı düşülen ESKİ bulgu dosyaları (7)
İçerik silinmedi, yalnız `GECERLILIK_UYARISI_2026_08_26` alanı eklendi:
`bulgu_allah_gradyan` · `bulgu_allah_ekseni_dikey` · `bulgu_gradyan_cetveli` ·
`bulgu_karsi_kutup_mesafe` · `bulgu_zikir_ekseni` · `bulgu_hudud_ekseni` ·
`bulgu_kevser_koridoru`

## DEĞİŞMEYENLER
`veri/` · `ciktilar/defter.json` (boru hattından üretilir) · diğer `betikler/` ·
diğer `tablolar/` · diğer `bulgular/`

## Kopyaladıktan sonra doğrulama

    cd betikler && python3 turkce_denetim.py          # 0 dönmeli
    PYTHONHASHSEED=0 python3 anahtar_denetim.py        # 58, taban ile aynı

