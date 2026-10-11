<!-- Güncellendi 2026-10-11 (sûre 39 tur sonu; taban commit de1a347). Önceki sürüm sûre 21 dönemindendi (2026-08). -->
Kur'an hesaplamalı okuma projesine devam ediyoruz.
Depo: github.com/sebahattintanas/claude_kuran_okuma — taban commit de1a347 (fark zip'leri buna göre).

## İLK İŞ
1. `git clone` → `k/` (temiz taban). `OKU_BENI_OTURUM.md` → "Kurulum" bölümünü aynen uygula:
   calisma/ düz kopya (betikler/* tablolar/* veri/* ciktilar/* bulgular/* betikler/dikey/*; onarim/ alt dizin),
   `python3 onarim/04_ngram_altyapi.py`, repo/ = yüklenecek ağaç, esitle.py calisma → repo.
2. Oku: `OKU_BENI_OTURUM.md` (blok akışı, Dikkat, Bekleyenler) ve `notlar/YAPILACAKLAR.md` → "SÛRE 39 TUR SONU".
3. Taban denetimi: `turkce_denetim.py` (tablolar/'dan) = 0 · `PYTHONHASHSEED=0 anahtar_denetim.py` = 70
   (taban dosyası temiz klondan, "taranan" satırı hariç; her blokta diff 0).

## DEVAM NOKTASI
Sûre 40 (Ğâfir, 85 ayet), ayet 1. Sûre 1 ve 9-39 TAM, sûre 2 kısmi (1-20). 2925/6236 (%46,9).
Şablonlar `zumer_*`'tan S=40: `kok_ekle_40.py` (önce tüm sûre için eksik kök kontrolü), `<ad>_metin_1.py`,
`<ad>_kayit.py` (CIPA, ARIZA), `uret_blok_40.py`, `aday_ekle_40_<ad>.py` (numara 1040'tan, yeni set adları;
betik sırayı doğruluyor), `yama_retroaktif_gloss_40.py`, `duzeltme_40.py`. Blok 10 ayet.

## BİÇİM (§0 — pazarlıksız)
- Okuma SOHBETTE yapılır; dosyaya yazıp özet vermek ihlâldir.
- Her ayet `### S:N` başlığı; blok gövdesi `blok_goster_v2.py S A B <metin> --html …` çıktısının AYNISI:
  `## ` Arapça · **meal** · › ölçüm · ◇ mercek · ◈K ◈B ◈D ◈A · ▽ dikey tablo. Başlık sayısı blok sonunda yazılır.
- Amiri Quran fontlu HTML her blokta dosya olarak da gönderilir.
- › ölçüm ve ▽ dikey ASLA elle yazılmaz; elle yazılan yalnız meal, ◇ ve ◈ satırları.
- Mercek satırı tetik yoksa "—", tetik varsa dolu (◈K/◈B tetik listeleri ONKAYIT_mercekler.md; S1 düzeltmesi yalnız ileri).
- Her [x/y] ve "yalnız / hepsi / en / ilk" iddiası yazmadan önce korpusla sayılır; sayı hafızadan yazılmaz.
- Meal, metnin adlandırmadığı konuşanı adlandırmaz.
- Blok sonu: Blok bilançosu (TAM SAYIM, okuma_metni['S']['_bilanco']['A-B']) · kapanan iplik · bağlar · ARIZA · denetim tablosu · ilerleme.

## EPİSTEMİK DİSİPLİN
- Ölçüm ile yorum ayrı. Okuma gözlemi "(okumada görüldü)" ya da "KAPATILAMAZ"; okunmamış atıf "henüz okunmadı".
- Araç açığı metin hakkında kanıt değildir (aday 924). Araç geliştirme DONDURULDU.
- Betiklere elle Arapça sabit yazılmaz (korpus kök biçimindeki kök anmaları hariç).
- Okuma sırasında hipotez test edilmez; dikkat çeken şey aday olarak kaydedilir.

## HER BLOKTA DENETİM
türkçe 0 · anahtar 70 diff 0 · tetik taraması (mercek ↔ morph kökleri) · [x/y] sayım karşılaştırması
(mercek metni ↔ ölçüm satırı, 0 uyuşmaz) · esma_kayit'te e_el=? kalmadı · aday setleri repo dosyasından doğrulanır.
Her ~3 blokta ARA ZİP (değişen dosyalar, de1a347 tabanına göre).

## AÇIK DURUMLAR
- Aday 1039 (öz-tanım / benzerlik): ölçüm kolu H0 REDDEDİLMEDİ; okuma kolu (karşıt çift) AÇIK.
  Sûre 40'tan itibaren ◇'de "Karşıt çift (aday 1039, okuma): …" notu aynı biçimde sürsün — kontrol verisi.
- Kullanıcı kararıyla açık: S2 (◈K tetik فلك kesinliği) · مأي gloss.
- Esmâ ön-kaydı DONDURULDU; yalnız veri toplanır (H1-H4 tam okuma bitince).
- GitHub'da elle silinecek 3 dosya: SILINECEKLER.txt.

## SÛRE SONU
`<ad>_kapanis.py` · `<ad>_paket_md.py` → notlar/sure40_<ad>_okuma.md · YAPILACAKLAR "SÛRE 40 TUR SONU" ·
OKU_BENI_OTURUM · SILINECEKLER · tam fark zip (de1a347 tabanı).
Push yok — zip verilir, kullanıcı elle yükler.

Her "Devam" = bir sonraki blok ya da kapanış/kurulum adımı.
