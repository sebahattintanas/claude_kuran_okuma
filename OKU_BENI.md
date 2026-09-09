# PAKET İÇERİĞİ — oturum 2026-09-04 (son)

Bu zip, depo köküne (`claude_kuran_okuma/`) **olduğu gibi açılacak**; dizin
yapısı depoyla birebir aynıdır ve yalnız bu oturumda **değişen** dosyalar vardır.

```
notlar/
  okuma_metni.json              ← 1969 ayet (sûre 26 tam + sûre 27 1-20)
  mercek_kayit.json             ← mercek ve atlama kayıtları
  okuma_baglantilari.json       ← AF_suara 192 · AG_neml 19 (yeni öbek)
  YAPILACAKLAR.md               ← blok ekleri + biçim ihlâli kaydı
  OTURUM_2026-09-04_KAPANIS.md  ← OTURUM KAPANIŞI (önce bunu oku)
  OTURUM_2026-09-04_ARA.md      ← oturumun erken bölümünün kapanış notu
tablolar/
  kok_turkce.json               ← 1017 kök
bulgular/
  aday_bulgular.json            ← 799 aday (AH_neml yeni öbek)
betikler/
  blok_25_*.py  blok_26_*.py  blok_27_*.py   ← blok üretim betikleri
  makro27.py                                 ← sûre 27 makro profili
```

## Denetim durumu (paketleme anında)

```
python3 turkce_denetim.py                     → 0 ihlâl   (1017 kök)
PYTHONHASHSEED=0 python3 anahtar_denetim.py   → 58 ihlâl · taban ile diff = 0
                                                 (21686 anahtar tarandı)
```

## Devam noktası

**Sûre 27, ayet 21.**
