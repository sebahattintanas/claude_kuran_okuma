# OTURUM PROTOKOLÜ — sûre 7 (A'râf): blok 1'den (SESSİZ OKUMA kipi)
Depo: github.com/sebahattintanas/claude_kuran_okuma · taban = **5bc0266** (sûre 7 blok planı) + sûre 7 hazırlığını, bu protokolü ve devir notunu (`yamalar/devir_6_165.txt`) taşıyan commit (HEAD). Kurulumda: taze klon → `git log --oneline 5bc0266..HEAD` yalnız hazırlık commit'ini göstermeli; başka commit varsa DUR ve sor.

**Bu protokol `notlar/OTURUM_PROMPT_sure6_1.md` ve `notlar/OTURUM_PROMPT_sure6_b32.md`'nin devamıdır.** O dosyalardaki §1 (kip), §2 (kurallar), §3 (blok akışı; b32 sürümü), §4 (bölüm sonu ajanı), §5 (denetim), §8 (tam okuma sonu), §9 (GÜVENLİK) olduğu gibi geçerlidir; sûre 6 adları (`_6`, `enam_*`, `6:A`, `cipa_tarama6`, `blok_plani_6`, `uret_blok_6`, `AX_enam` / `AS_enam`, `sure6_bloklar`, `['6']`, `denetim_6.sh`) sûre 7'de `_7`, `araf_*`, `7:A`, `cipa_tarama7`, `blok_plani_7`, `uret_blok_7`, `AX_araf` / `AS_araf`, `sure7_bloklar`, `['7']`, `denetim_7.sh` karşılıklarıyla okunur. Aşağıdaki bölümler onları günceller ve önceliklidir.

## Durum (2026-11-24)
- Sûre 1–6 ve 9–114 TAM (sûre 6 kapanışı 2026-11-24: `_bilanco_sure`, `_cipa_tablosu_6`, `_esma_profil_6`, `notlar/sure6_enam_okuma.md`); sûre 7–8 okunmamış.
- Okunan 5955 / 6236 (%95,5) · `sunum/basilan.txt` 351 satır · kok_turkce 1632 · esmâ KARAR 1305 · AS_enam 101 · aday havuzu 1–1042 (sonraki 1043) · mutasyon_sina 374 / 374 · anahtar denetimi BOZUK 70 (taban).
- `sunum/bolum4_kurallar.py` … `sunum/bolum35_kurallar.py` yürürlükte.
- Sûre 7: 206 ayet, 3320 kelime; plan `yamalar/blok_plani_7.txt` — 20 bölüm / 54 blok (kullanıcı onayı 2026-11-24). Blok aralıkları yalnız bu dosyadan okunur; basılmamış aralık ve ayet numarası hiçbir yere (sohbet dahil) yazılmaz.
- Dosya ailesi kuruldu (`yamalar/iskele_7.py`): `kok_ekle_7.py`, `araf_metin_1.py`, `araf_kayit.py`, `uret_blok_7.py`, `aday_ekle_7_araf.py`, `duzeltme_7.py`, `yama_retroaktif_gloss_7.py`, `araf_kapanis.py`, `araf_paket_md.py`, `cipa_tarama7_adaylari.json`; yamalar `yama_{kayit,metin,uret,bag}_7.py`, `yama_kok_7_sablon.py`; `sunum/denetim_7.sh`; `sunum/sure.py` ve `sinifla.py` varsayılanı 7, `SON = 0`.
- `okuma_metni['7']`'de on eski blok özeti ('A-B' anahtarlı, sıkıştırılmış dönem) okuma sayılmaz, kapanışta `_eski_ozet`'e taşınır; `mercek_kayit['7']` eski ◇ notları (35) blok yazılırken `_sikistirilmis_eski` arşivine alınır.
- Sıra: blok 1 (bölüm 1 açılışı) → … → blok 54 → sûre 7 kapanışı (kullanıcıyla) → sûre 8.
- **Devir:** `yamalar/devir_6_165.txt` — "SONRAKİ BLOK ARIZA BAŞI" maddesi blok 1 ARIZA'sının başına aynen (bayt eşit) girer: kur.py BEK satırı dosyadan `'  "devir ('` ile başlayan satırı okur (`s6/b01/yap/kur.py` emsali). `bekleyen_ariza_6_b40.txt` NUMARALIDIR — sûre 7'ye KOPYALANMAZ.

## Kullanıcı kararları (değişmez)
- "Yorum / meal sorularını oturum ortasında sorma, kayda yaz; basılmamış ayet numarasını hiçbir yere (sohbet dahil) yazma."
- Her "Devam" = bir plan bloğu; blok sonunda commit + push (main) ve SendUserFile (display attach): emsal md + blok HTML.
- Kapanış notu 7 başlık (Bilanço · Kapanan iplikler · Dikkat çeken okumalar · Bağlar · ARIZA · Denetim tablosu (markdown tablo) · İlerleme), son satır "Başlık sayısı: 7 / 7 — toplam ilerleme N ayet (%X)".
- `sunum/basilan.txt` BOŞALTILMAZ (önceki oturumlarda basılanlar basılmış sayılır).
- 2026-11-24: sûre 6 son ayetindeki söz sınırı kaydı söz dışı kalır — tam okuma bitince değerlendirilir. `notlar/okuma_metni.json` şimdilik bölünmez.
- Çalışma hızı: ARIZA koşusu bir seferde bir tane; gereksiz yinelenen koşu yapılmaz.

## §0 Kurulum (taze oturumda; sure6_1 §0 ve sure6_b32 §0'dan farklar)
- `basilan.txt` repo'daki hâliyle (351 satır); `sunum/sinifla.py` `SON` = sûre 7'de okunmuş son ayet (blok 1 öncesi 0).
- Blok dizinleri: sûre 5 → `/home/claude/s5/` (`repo/oturum/sure5_bloklar/b*`), sûre 6 → `/home/claude/s6/` (`repo/oturum/sure6_bloklar/b*`) — mutasyon_sina sûre 5 sınamaları `BKOK=/home/claude/s5/`, sûre 6 sınamaları `BKOK=/home/claude/s6/` ile koşar. Sûre 7 blokları `/home/claude/bNN/` (depoda `repo/oturum/sure7_bloklar/`; okunmuş bloklar taze oturumda oradan geri yüklenir).
- Sûre 6 kayıtlarında geriye dönük koşu gerekirse: `SURE=6 SON=165 BKOK=/home/claude/s6/` ortamıyla.
- `sunum/yardimci/say_uret.py` sûre numarasını `sunum/sure.py`'den alır (`--dizi "7 a i j"`).

## §3 Blok akışı farkları (sure6_b32 §3 üzerine)
- Komutlardaki `6` → `7`, `enam_metin_1` → `araf_metin_1`, `morph6.txt` → `morph7.txt`, `denetim_6.sh` → `denetim_7.sh`, blok arşivi `repo/oturum/sure7_bloklar/`.
- ARIZA çıktısı her koşuda boyutuyla denetlenir (`wc -c`; çökme / zaman aşımı küçük çıktı verir ve özet yanlış 'TOPLAM 0' gösterir; sağlam çıktı ≥ ~3,9 KB).
- Çakışma grupları: `python3 sunum/cakisma.py $(ls yamalar/ariza_7_*_*.txt | sort -t_ -k3 -n)` (sayısal sıra).
- kur.py: **blok 1** `s6/b39/yap/kur.py`'den (bölüm açılış biçimi) türetilir — BEK satırı devir dosyasından; GERI satırı `geriye_donuk_6_b40k.txt`; bolum35 `B35_HEPSI` listeye eklenir; önceki blok `yap/karar.py` yüklemeleri sûre 7 bloklarıyla sınırlı (blok 1'de yok). Bölüm içi blok: son bloğun kur.py'sinden, BEK satırı olmadan, `I_body.py` `I = [` ile. R5 satırlarında sûre içi sayım nakarat sayımından ayrıysa `dz` demeti (`sunum/r5_gerekce.py` çıktısıyla) zorunlu.
- Bölüm sonu (§4): salt okunur ajan → `yamalar/bekleyen_ariza_7_bNN.txt` (2 madde) → `sunum/bolumMM_kurallar.py` (sıradaki numara 36) → mutasyon sınamaları (isabetli + isabetsiz) → geriye dönük koşu → commit.

## Sûre 6'nın son bloklarında öğrenilen kurallar (araç yakalar; yazarken uy)
- Kesim fiil alıntıları yalın biçimle ('qul', 'te'tiye'); mealde 'olan' varsa "('olan' takdiri yok)" notu ya da "'X olan' … açılımı"; nekre notu bab notundan önce; içerici '-den / -e' kelimelerinde 'fiil yönetimi takdiri'.
- ADDR parçası için ayrı kesim öğesi yazılmaz (kelime_kontrol), ama taşıyan kelimenin notunda 'ADDR' "N. kelime" ile anılır (bolum35 k1).
- 'Bayt eşit' denen emsal alıntısı kelime sınırında biter (bolum35 k2); say2'de birden çok ayet bulan ≥ 5 kelimelik en geniş eş aralık ◇'de ya da ARIZA'da adıyla anılır (k3); söz kapanışı gerekçesi morph CONJ'a dayanmaz (k4); kip notunda 'olan' ile karşılanan fiil kip sapma notunda anılır (k5).
- Lemma adları önceki bloklarla eş; D1 nekre sayısı = INDEF sayısı; tetik maddesi biçimi "S:a ◈B kök ('x' N. kelime — B4)"; xref maddesi ayet başına "S:a xref yok"; yıldız maddesi "eşiği geçen öbür ölçüler"i adlandırır; söz içi REM "REM sapması S:a (N. kelime) — gerekçe"; süren söz kapanışı "söz kapanır (N. kelime)".
- Araç değişikliği gerekçesi değişen aracı, adının geçtiği yerde kural numarasıyla anar; anılan her sayım etiketinin emsal satırı bulunur; kip notu her fiili sayar (yinelenenler "(N. kelime)" ile); aday kök maddesi ≥ 2 ayet ya da "… ile bölüm içi".
- esma_el: `yamalar/esma_el_7_A_B.txt` girdileri `calisma/esma_el.py`'ye (son `}` öncesi) esma_kayit'ten önce işlenir.
