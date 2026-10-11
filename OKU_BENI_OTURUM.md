# OTURUM — sûre 39 (Zümer) TAM · blok başı kayıt · ek mercekler

**Okunan: 2925 / 6236 ayet (%46,9)** — sûre 1 ve 9-39 TAM, sûre 2 kısmi (1-20).
Devam: **sûre 40 (Ğâfir, 85 ayet)**. Sûre 2'nin 21-286'sı hâlâ sonraya.
kok_turkce **1331** kök · aday havuzu **1-1039** (sûre 39'da yeni: 1039, `AX_zumer`) · bağ seti `AS_zumer` 171 · esmâ KARAR 221.
Denetim tabanı: türkçe **0** · anahtar **70**, diff 0 (taban temiz klondan `PYTHONHASHSEED=0 python3 k/betikler/anahtar_denetim.py`, "taranan" satırı hariç).
Paket: depo `0793015`'e göre fark.
Sûre 39 dosyaları: `kok_ekle_39.py` · `zumer_metin_1.py` (MEAL1-8/M1-8) · `zumer_kayit.py` (CIPA, ARIZA) · `uret_blok_39.py` · `aday_ekle_39_zumer.py` · `yama_retroaktif_gloss_39.py` · `duzeltme_39.py` · `zumer_kapanis.py` · `zumer_paket_md.py` → `notlar/sure39_zumer_okuma.md` · **`aday1039_test.py` → `bulgular/aday1039_test.json`**.
Sûre 40 için şablonlar `zumer_*`'tan S=40 (yeni set adları; numara 1040'tan, `aday_ekle` sırayı doğruluyor).
Her blokta ayrıca: tetik taraması (mercek satırı ↔ morph kökleri) ve [x/y] sayım karşılaştırması (mercek metni ↔ ölçüm satırı) — ikisi de oturum betiği.
**Aday 1039:** ölçüm kolu H0 reddedilmedi; okuma kolu (karşıt çift) açık — sûre 40'tan ◇'de 'Karşıt çift (aday 1039, okuma)' notu aynı biçimde sürsün (kontrol verisi).

Ayrıntılı: `notlar/YAPILACAKLAR.md` → "SÛRE 39 TUR SONU".

## Kurulum
    git clone https://github.com/sebahattintanas/claude_kuran_okuma k
    # calisma/ düz: betikler/* tablolar/* veri/* ciktilar/* bulgular/* betikler/dikey/* ; onarim/ alt dizin
    python3 onarim/04_ngram_altyapi.py      # ayet_iskelet.json
    # repo/ = yüklenecek ağaç; blok betikleri /home/claude/repo/notlar/ yazar
    # esitle.py: calisma → repo (yalnız değişen/yeni dosyalar)

## Okuma biçimi (2026-10-04)
Sunum `blok_goster_v2.py S A B <metin> [--html yol]`: `### S:N` · `## ` Arapça · **meal** · › ölçüm · ◇ mercek · ◈K ◈B ◈D ◈A · ▽ kök başına tablo (açıklama blok başında bir kez). Her blok ayrıca Amiri Quran fontlu HTML.
Ek mercekler `notlar/ONKAYIT_mercekler.md` (a7e9628; §8 S1 tetik düzeltmesi 37:31'den): her ayette dört satır, tetik yoksa "—"; tetik kök listesi ölçüm satırından — yazdıktan sonra morph kökleriyle karşılaştır (tetiksiz satır da, tetiklenmiş '—' de hata).

## Blok akışı (blok başı kayıt)
1. eksik kök kontrolü → `kok_ekle_<S>.py` (NFC eşleşmesi yoksa DUR; gloss çok anlamlı, baskın lemma sayılır)
2. `blok_dikey.py S A B`
3. okuyucu kararları `esma_el_ekle.py <dosya>` → `esma_kayit.py S A B` → **çıktıda e_oto var / e_el yok kalan token var mı bak** (aday 1022), varsa karar ekle ve yeniden koş
4. meal + mercek → `<sure>_metin_1.py` (MEALn/Mn); çıpa/arıza → `<sure>_kayit.py`
5. `uret_blok_<S>.py` → `blok_<S>_A_B.py` — esmâ kaydından SONRA
6. `aday_ekle_<S>_<ad>.py` (iki kez; sayaç çıktısını kontrol et) · `yama_retroaktif_gloss_<S>.py` · `duzeltme_<S>.py` · `esitle.py`
7. `blok_goster_v2.py S A B <metin> --html …` → okuma SOHBETTE, ölçüm ve dikeye dokunulmaz
8. `turkce_denetim.py` (tablolar/'dan) = 0 · `PYTHONHASHSEED=0 anahtar_denetim.py` = 70, diff 0
9. Sûre sonunda: `<sure>_kapanis.py`, YAPILACAKLAR eki, bu dosya, SILINECEKLER, `<sure>_paket_md.py`, fark zip
10. Uzun oturumda her ~3 blokta ARA ZİP (ortam kaybı dersi, 2026-10-07)

## Dikkat
* nakarat3 satırındaki "N ayet, tür ic" SÛRE İÇİ sayıdır; eş ayet satırda yok — defterden koş (aday 1003). esit2 satırı eşi bazen iki kez yazıyor (araç tekrarı).
* Bilanço ★ kaynağı kafiye kırığında yanlış etiketli (aday 1001) — okumada elle düzelt.
* Esmâ tokenlerini ölçüm satırından toplama; esma_kayit çıktısından topla (aday 1022).
* Kendi kaydı düzeltme: `duzeltme_<S>.py` + `<sure>_kayit.DUZELTME` (özgün alan korunur).
* Mercekteki her [x/y] ve üstünlük/'hepsi'/'ilk' iddiası kayıttan önce ölçüm satırı/korpusla sayılır. Kelime sayısı defterden (kuran_veri ilk ayete besmeleyi katar).
* "Henüz okunmadı" demeden önce okuma_metni'ni iki anahtar biçimiyle de oku ('S:A' ve 'A-B').
* Aktör rol alanı i'râb etiketinden türer; gayr-i munsarif adlarda yanlış (aday 1038).
* Boruyu `head` ile kesme (esitle BrokenPipe); Arapça çıktıyı `cut -c` ile kesme.
* Metin kalıbı sayarken harekesiz eşleşmede elif-medde (آ) ve hemze-elif (ءا) ayrı karakter — sayım kaçırır.
* Çıpa L4 sınıflama kolu: okumada 29:40 'eşleme' ölçütü sabit (aday 1014).

## Bekleyenler
GitHub'da üç silme: `betikler/onarım`, `betikler/onar─▒m`, Arapça adlı `ciktilar/dikey_kisi_*.json` (SILINECEKLER.txt).
Karar bekleyen (kullanıcı: açık kalsın): ◈K tetik فلك kesinlik düzeltmesi (S2) · مأي gloss ('ne zaman' → yüz).
Esmâ ön-kaydı DONDURULDU; §9 commit `b58c430`. Yalnız veri toplanır.
