# OTURUM — sûre 35 TAM · sûre 36 (Yâsîn) 1-20 · blok başı kayıt

**Okunan: 2517 / 6236 ayet (%40,4)** — sûre 1 ve 9-35 TAM, sûre 2 kısmi (1-20), sûre 36 kısmi (1-20).
Devam: **36:21**. Sûre 2'nin 21-286'sı hâlâ sonraya.
kok_turkce **1144** kök (sûre 36'nın tümü eklendi) · aday havuzu **1-1020** (`AT_fatir` 1007-1018, `AU_yasin` 1019-1020) · bağ setleri `AO_fatir` 85, `AP_yasin` 19.
Denetim tabanı: türkçe **0** · anahtar **70**, diff 0.
Paket: `57fdb46`'ya göre BİRLEŞİK fark (sûre 35 + 36:1-20). Depo 57fdb46'daysa bu tek paket yüklenir.
Sûre 36 dosyaları: `yasin_metin_1.py` · `yasin_kayit.py` · `uret_blok_36.py` · `aday_ekle_36_yasin.py` · `yama_retroaktif_gloss_36.py` · `duzeltme_36.py` (kapanış ve paket_md henüz yok — fatir_* şablonundan S=36).

Ayrıntılı: `notlar/YAPILACAKLAR.md` → "SÛRE 35 TUR SONU" ve "SÛRE 36 ARA KAYIT".

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
* Mercekteki her [x/y] ve üstünlük/'hepsi' iddiası kayıttan önce ölçüm satırı/korpusla sayılır (sûre 35: beş yakalama).
* Boruyu `head` ile kesme (esitle BrokenPipe); Arapça çıktıyı `cut -c` ile kesme (çok baytlı).
* Çıpa L4 sınıflama kolu: okumada 29:40 'eşleme' ölçütü sabit (aday 1014).

## Bekleyenler
GitHub'da üç silme: `betikler/onarım`, `betikler/onar─▒m`, Arapça adlı `ciktilar/dikey_kisi_*.json` (SILINECEKLER.txt).
Esmâ ön-kaydı DONDURULDU; §9 commit `b58c430`. Yalnız veri toplanır.
