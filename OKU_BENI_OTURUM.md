# OTURUM — sûre 46 (Ahkâf) TAM · blok başı kayıt · ek mercekler

**Okunan: 3337 / 6236 ayet (%53,5)** — sûre 1 ve 9-46 TAM, sûre 2 kısmi (1-20).
Devam: **sûre 47 (Muhammed, 38 ayet)**. Sûre 2'nin 21-286'sı hâlâ sonraya.
kok_turkce **1354** kök · aday havuzu **1-1041** (sûre 46'da yeni aday yok, `AX_ahkaf` boş) · bağ seti `AS_ahkaf` 56 · esmâ KARAR 381.
Denetim tabanı: türkçe **0** · anahtar **70**, diff 0 (taban temiz klondan `PYTHONHASHSEED=0 python3 k/betikler/anahtar_denetim.py`, "taranan" satırı hariç).
Paket: depo `5e26cf0`'a göre fark.
Sûre 46 dosyaları: `kok_ekle_46.py` · `ahkaf_metin_1.py` (MEAL1-4/M1-4) · `ahkaf_kayit.py` (CIPA, ARIZA, DUZELTME boş) · `uret_blok_46.py` · `aday_ekle_46_ahkaf.py` · `yama_retroaktif_gloss_46.py` · `duzeltme_46.py` · `ahkaf_kapanis.py` · `ahkaf_paket_md.py` → `notlar/sure46_ahkaf_okuma.md`.
Sûre 47 için şablonlar `ahkaf_*`'tan S=47 (yeni set adları; numara 1042'den, `aday_ekle` sırayı doğruluyor). Sûre 44-45 dosyaları: `duhan_*`, `casiye_*` (aynı düzen).
**Oturum yardımcıları depoda** (`betikler/`, salt-okur): `oturum_ortak.py` · `oturum_say.py S:A i-j [--on] [--son]` · `oturum_lem.py S:A:W [--kok]` · `oturum_lemdizi.py S A i j` · `oturum_tetik.py S A B <metin>` · `oturum_xy.py S A B <metin>`. Her blokta tetik (0 uyuşmaz) ve [x/y] (0 uyuşmaz) bunlarla koşulur; alıntı/sayı iddiaları lemma sayımıyla. Araç dondurma kuralına uygunluğu kullanıcı onayına açık.
**Aday 1039:** okuma kolu (karşıt çift) — ◇'de 'Karşıt çift (aday 1039, okuma)' notu her ayette sürsün (sûre 46'da 35/35 yazıldı, 19 dolu).
**Aday 1040:** ardışık sûre sınırında süreklilik — test korpus sonunda; 47:1-10 okunurken 46:26-35 ile bağ kayıt olarak yazılabilir, test edilmez. 47 Hâ Mîm dizisinin dışında.
**Aday 1041:** aynı kelimenin Allah ve insan için kullanılması — kayıt; yeni vakalar AS bağına "aday 1041" notuyla (sûre 46: شهد 46:8/10, وعد 46:16-17 sınırda; 'velî' 42:9 / 46:32).
**Çıpa:** 46:15 L4 adayı TARTIŞMALI (ölçü kolu; 31:14 ile aynı biçim) — kademe kararı okumaya bağlı, ölçüt değişmedi.

Ayrıntılı: `notlar/YAPILACAKLAR.md` → "SÛRE 46 TUR SONU".

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
* `<sure>_kayit.ARIZA` son listesi `" ],\n}"` ile biter (ekleme çapası assert'li yardımcıyla); `uret_blok_<S>.BASLIK` satırlarının sonunda virgül olmalı (sûre 40 dersi).
* Osmânî imlâ: 'el-leyl' tek lam (ليل), 'yuhyî' küçük ye, 'sunnete'llâh' açık te — harekesiz kalıbı bu biçimle kur; önekli kalıp sûre içi eşi kaçırabilir.
* Esmâ tokenlerini ölçüm satırından toplama; esma_kayit çıktısından topla (aday 1022).
* Kendi kaydı düzeltme: `duzeltme_<S>.py` + `<sure>_kayit.DUZELTME` (özgün alan korunur).
* Mercekteki her [x/y] ve üstünlük/'hepsi'/'ilk' iddiası kayıttan önce ölçüm satırı/korpusla sayılır. Kelime sayısı defterden (kuran_veri ilk ayete besmeleyi katar).
* "Henüz okunmadı" demeden önce okuma_metni'ni iki anahtar biçimiyle de oku ('S:A' ve 'A-B').
* Aktör rol alanı i'râb etiketinden türer; gayr-i munsarif adlarda yanlış (aday 1038).
* Boruyu `head` ile kesme (esitle BrokenPipe); Arapça çıktıyı `cut -c` ile kesme.
* Harekesiz kalıp: i'râb farkı görünmez ('el-insâne kefûr' ↔ 17:67), imlâ farkı ayırır ('cezâu' 10:27 / 42:40) — bağ okumayla, sayı yok (sûre 42).
* ◈K أرض mekân kullanımında ('fi'l-ard') da tetikler — satır dolu yazılır (42:27).
* Harekesiz kalıp gürültüsü (sûre 41): 'fslt'/'fasalat', 'a'dâ'/'va'd', 'qurenâ''/'qur'ân', 'teddeûn'/'ted'ûn', 'yes'emûn'/'yesemmûn' — kalıp sayımı yerine lemma sayımı.
* Metin kalıbı sayarken harekesiz eşleşmede elif-medde (آ) ve hemze-elif (ءا) ayrı karakter — sayım kaçırır.
* Çıpa L4 sınıflama kolu: okumada 29:40 'eşleme' ölçütü sabit (aday 1014).
* Lemma dizisi sayımı şahıs/önek farkını gizler — alıntıdan önce ayet metni okunur (sûre 43: 21:56, 32:27, 28:87).
* Sûre içi kök geçişi `oturum_lem.py S:A:W --kok` "sûre içi" satırından yazılır (sûre 43: أيي 'eyyuhâ', ملك 43:19).
* Sûre içi liste (Rab, 1P vb.) hafızadan yazılmaz; kök sayımı ya da morph'tan (sûre 44: 44:54, 44:57). Görülmemiş ayet anılmaz (44:56).
* Yarıda kalan turun dosyaya yazdığı taslak doğrulanmadan kaydedilmez (sûre 44: 44:41-50).
* Esmâ geçerli/yanlış mühür iddiası, okuyucu kararı eklendikten SONRA koşulan bilançodan yazılır (sûre 45: 45:2, 19, 37 — DUZELTME 45:37).
* Ölçüm satırı esmâ alanı ile esma_kayit ayrışabilir (46:17 'evvel' ölçümde yok; 46:32-33 ölçümde MÜHÜRSÜZ, esma_kayit mühür EVET) — iddia esma_kayit + karar sonrası bilançodan (sûre 46).
* Lemma dizisi ardışık iki kelimeyi terkip sanabilir; terkip iddiasından önce eş ayet metni okunur (45:14 / 40:16).

## Bekleyenler
GitHub'da üç silme: `betikler/onarım`, `betikler/onar─▒m`, Arapça adlı `ciktilar/dikey_kisi_*.json` (SILINECEKLER.txt).
Karar bekleyen (kullanıcı: açık kalsın): ◈K tetik فلك kesinlik düzeltmesi (S2) · مأي gloss ('ne zaman' → yüz).
Esmâ ön-kaydı DONDURULDU; §9 commit `b58c430`. Yalnız veri toplanır.
