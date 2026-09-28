# OTURUM — sûre 33 (Ahzâb) TAM · blok başı kayıt

**Okunan: 2398 / 6236 ayet (%38,5)** — sûre 1 ve 9-33 TAM, sûre 2 kısmi (1-20).
Devam: **sûre 34 (Sebe')**. Sûre 2'nin 21-286'sı onarılmamış alanlar yüzünden hâlâ sonraya.

Ayrıntılı tur sonu: `notlar/YAPILACAKLAR.md` → "SÛRE 33 TUR SONU".

## Kurulum
    git clone https://github.com/sebahattintanas/claude_kuran_okuma k
    # calisma/ düz: betikler/* tablolar/* veri/* ciktilar/* bulgular/* betikler/dikey/* ; onarim/ alt dizin
    python3 onarim/04_ngram_altyapi.py      # ayet_iskelet.json
    # repo/ = yüklenecek ağaç; blok betikleri /home/claude/repo/notlar/ yazar

## Blok akışı (blok başı kayıt)
1. `kok_ekle_<S>.py` — eksik kökler, NFC eşleşmesi yoksa DUR
2. `blok_dikey.py S A B`
3. `esma_kayit.py S A B` + okuyucu kararları `esma_el.py`
4. meal + mercek → `<sure>_metin_1.py`; çıpa/arıza → `<sure>_kayit.py`
5. `uret_blok_<S>.py` → `blok_<S>_A_B.py` koş (okuma_metni, mercek_kayit, bilanço, ilerleme)
6. `aday_ekle_<S>_<ad>.py` (idempotent) · `yama_retroaktif_gloss_<S>.py`
7. `blok_goster.py S A B <metin>` → okuma SOHBETTE, her ayet `### S:N`, ölçüm ve dikey satırlarına dokunulmaz
8. `turkce_denetim.py` (tablolar/'dan) = 0 · `PYTHONHASHSEED=0 anahtar_denetim.py` = 70, diff 0
9. Sûre sonunda: `<sure>_kapanis.py`, YAPILACAKLAR eki, bu dosya, tek yükleme paketi

## Bekleyen kararlar
Esmâ ön-kaydının dondurulması öncesi beş nokta (YAPILACAKLAR → "DONDURMA ÖNCESİ BEŞ KARAR NOKTASI").
GitHub'da üç silme: `betikler/onarım`, `betikler/onar─▒m`, Arapça adlı `ciktilar/dikey_kisi_*.json`.
