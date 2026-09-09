# YAMA — 2026-09-09, depo denetimi sonrası

Depo klonlandı, denetimler koşuldu, **bir yazım hatası bulundu ve onarıldı**.

## Ne bulundu

`anahtar_denetim.py` yalnız `betikler/` dizinini tarar. Oturum boyunca blok
betikleri düz çalışma dizininde yazıldı ve `betikler/` içine kopyalanmadı →
**bu oturumun yirmi iki blok betiği oturum boyunca hiç denetlenmedi.**

Yükleme sonrası denetim: **21910 anahtar / 59 ihlâl** (taban 58). Tek yeni ihlâl:

```
betikler/blok_26_151_160.py sat.158
  ✗ نَاقَة  → T2 YAZIM · korpustaki hâli: ناقَة
```

## Onarım

`نَاقَة` → `ناقَة` (üç dosyada): blok betiği, `okuma_metni.json` 26:157 mercek,
`mercek_kayit.json` 26:157.

**Onarım sonrası: 21910 / 58 · taban ile diff = 0 · turkce_denetim → 0.**

## Bu zipteki dosyalar (depo köküne açılacak, üzerine yazacak)

```
betikler/blok_26_151_160.py
notlar/okuma_metni.json
notlar/mercek_kayit.json
notlar/YAPILACAKLAR.md      ← denetim kaydı ve yeni önlem eklendi
```

## Yeni önlem

**Blok betiği yazıldıktan sonra `betikler/` içine kopyalanacak ve
`anahtar_denetim.py` ORADAN koşulacak.**
