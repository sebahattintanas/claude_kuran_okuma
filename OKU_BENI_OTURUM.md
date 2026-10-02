# OTURUM — sûre 34 (Sebe') TAM · blok başı kayıt

**Okunan: 2452 / 6236 ayet (%39,3)** — sûre 1 ve 9-34 TAM, sûre 2 kısmi (1-20).
Devam: **sûre 35 (Fâtır)**. Sûre 2'nin 21-286'sı hâlâ sonraya.
kok_turkce **1126** kök · aday havuzu **1-1006** (son set `AS_sebe` 998-1006) · bağ seti `AN_sebe` 75.
Denetim tabanı: türkçe **0** · anahtar **70**, diff 0.

Ayrıntılı tur sonu: `notlar/YAPILACAKLAR.md` → "SÛRE 34 TUR SONU".

## Kurulum
    git clone https://github.com/sebahattintanas/claude_kuran_okuma k
    # calisma/ düz: betikler/* tablolar/* veri/* ciktilar/* bulgular/* betikler/dikey/* ; onarim/ alt dizin
    python3 onarim/04_ngram_altyapi.py      # ayet_iskelet.json
    # repo/ = yüklenecek ağaç; blok betikleri /home/claude/repo/notlar/ yazar
    # esitle.py: calisma → repo (yalnız değişen/yeni dosyalar)

## Blok akışı (blok başı kayıt)
1. `kok_ekle_<S>.py` — eksik kökler, NFC eşleşmesi yoksa DUR (sûrenin tümü baştan eklenebilir)
2. `blok_dikey.py S A B`
3. okuyucu kararları `esma_el_ekle.py <dosya>` ile `esma_el.py`'ye → **SONRA** `esma_kayit.py S A B`
4. meal + mercek → `<sure>_metin_1.py`; çıpa/arıza → `<sure>_kayit.py`
5. `uret_blok_<S>.py` → `blok_<S>_A_B.py` koş — esmâ kaydından SONRA
6. `aday_ekle_<S>_<ad>.py` (idempotent, iki kez) · `yama_retroaktif_gloss_<S>.py` · `esitle.py`
7. `blok_goster.py S A B <metin>` → okuma SOHBETTE, her ayet `### S:N`, ölçüm ve dikey satırlarına dokunulmaz
8. `turkce_denetim.py` (tablolar/'dan) = 0 · `PYTHONHASHSEED=0 anahtar_denetim.py` = 70, diff 0
9. Sûre sonunda: `<sure>_kapanis.py` (esmâ kaydını ve düzeltmeleri yeniden koşar), YAPILACAKLAR eki, bu dosya, tek yükleme paketi

## Dikkat
* nakarat3 satırındaki "N ayet, tür ic" SÛRE İÇİ sayıdır; eş ayet satırda yok — defterden koş (aday 1003).
* Bilanço ★ kaynağı kafiye kırığında yanlış etiketli (aday 1001) — okumada elle düzelt.
* Kendi kaydı düzeltme: `duzeltme_<S>.py` + `<sure>_kayit.DUZELTME` (özgün alan korunur).

## Bekleyenler
GitHub'da üç silme: `betikler/onarım`, `betikler/onar─▒m`, Arapça adlı `ciktilar/dikey_kisi_*.json` (SILINECEKLER.txt).
Esmâ ön-kaydı DONDURULDU; §9 commit `b58c430`. Yalnız veri toplanır.
