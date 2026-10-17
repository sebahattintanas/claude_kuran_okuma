# OTURUM — sûre 50 (Qâf) TAM · blok başı kayıt · ek mercekler

**Okunan: 3467 / 6236 ayet (%55,6)** — sûre 1 ve 9-50 TAM, sûre 2 kısmi (1-20).
Devam: **sûre 51 (Zâriyât, 60 ayet)**. Sûre 2'nin 21-286'sı hâlâ sonraya.
kok_turkce **1375** kök · aday havuzu **1-1041** (sûre 50'de yeni aday yok, `AX_qaf` boş) · bağ seti `AS_qaf` 91 · esmâ KARAR 441.
Denetim tabanı: türkçe **0** · anahtar **70**, diff 0 (taban temiz klondan `PYTHONHASHSEED=0 python3 k/betikler/anahtar_denetim.py`, "taranan" satırı hariç).
Paket: depo `279460e`'ye göre fark (sûre 47-49 o commit'te; sûre 50 bu zip'te).
Sûre 50 dosyaları: `kok_ekle_50.py` · `qaf_metin_1.py` (MEAL1-5/M1-5) · `qaf_kayit.py` (CIPA, ARIZA, DUZELTME boş) · `uret_blok_50.py` · `aday_ekle_50_qaf.py` · `yama_retroaktif_gloss_50.py` · `duzeltme_50.py` · `qaf_kapanis.py` (+ `qaf_kapanis_notu.txt`; `--kuru` ile yazmadan basar) · `qaf_paket_md.py` → `notlar/sure50_qaf_okuma.md`.
Sûre 51 için şablonlar `qaf_*`'tan S=51 (yeni set adları; numara 1042'den, `aday_ekle` sırayı doğruluyor). Sûre 44-49 dosyaları: `duhan_*`, `casiye_*`, `ahkaf_*`, `muhammed_*`, `fetih_*`, `hucurat_*` (aynı düzen).
**Oturum yardımcıları depoda** (`betikler/`, salt-okur): `oturum_ortak.py` · `oturum_say.py S:A i-j [--on] [--son]` · `oturum_lem.py S:A:W [--kok]` · `oturum_lemdizi.py S A i j` · `oturum_tetik.py S A B <metin>` · `oturum_xy.py S A B <metin>`. Her blokta tetik (0 uyuşmaz) ve [x/y] (0 uyuşmaz) bunlarla koşulur; alıntı/sayı iddiaları lemma sayımıyla. Tetik ön kuru koşusu: geçici `M={n:"◇ x\n◈K — —\n◈B — —\n◈D — x\n◈A — x" ...}` modülü, kullanımdan sonra silinir. Araç dondurma kuralına uygunluğu kullanıcı onayına açık.
**Aday 1039:** okuma kolu (karşıt çift) — ◇'de 'Karşıt çift (aday 1039, okuma)' notu her ayette sürsün (sûre 50'de 45/45).
**Aday 1040:** ardışık sûre sınırında süreklilik — test korpus sonunda; 51:1 okunurken 50:45 ile bağ kayıt olarak yazılabilir.
**Aday 1041:** aynı kelimenin Allah ve insan için kullanılması — kayıt (sûre 50: مجد, حفظ, رقب, عيي, ظلم, لغب, جبر).
**Çıpa:** sûre 50'de L4 yok (50:9, 50:11 L2; 50:38 L1, ölçü koluna sınırda); **48:29 ekin büyümesi L4 adayı, teşbih içinde — TARTIŞMALI, karar kullanıcıda**.

Ayrıntılı: `notlar/YAPILACAKLAR.md` → "SÛRE 50 TUR SONU".

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
* Emsal ayeti yalnız lemma listesinden anma; metni (ya da meâli) okunmadan 'okunanlarda X anlamında' yazılmaz — sûre 47'de dört emsal kümesi kayıttan önce okunarak yeniden yazıldı (22:62/31:30, 20:80, 16:25/17:15/35:18/39:7, 13:8/22:5/31:34/33:6).
* Gloss'a okunmamış ayet numarası yazılmaz (sûre 47: ثخن '8:67' — gloss dikey JSON'una da girer; düzeltince `blok_dikey.py` yeniden koşulur).
* ◈B / ◈K tetik listesi dışı organ ya da olgu (sûre 47: 47:15 'em'â'', 'şârib') satırı doldurmaz — satır '—', gözlem ◇'ye (ön-kayıt §4; yeni tetik sınıfı ayrı karar ister).
* `<sure>_kayit.ARIZA`'ya yeni blok eklerken önceki listenin kapanışı ' ],' korunur — sûre 48'de bir dilim hatası listeyi açık bıraktı (SyntaxError), blok betiği koşmadan yakalandı; ekleme sonrası `python3 -c 'import <sure>_kayit'` ile doğrula.
* Teşbih / mesel içindeki doğa süreci (48:29 ekin) çıpa merdiveninde ayrı yazılır: kademe süreçten, cipa kararı 'olgu benzetme aracı' notuyla açık bırakılır (39:21 doğrudan anlatım emsalinden ayrı).
* Yıldız formülü iki uçta da şişer: kısa ayette lafız (48:3, 48:7), uzun ayette n (48:29) — ★★★ içerik iddiası değil.
* 'Okunan X, Y (okumada görüldü)' listesine yalnız bu oturumda metni AR ile basılıp görülen ayet yazılır; lemma listesinde †'sız olması yetmez (sûre 49: yedi yerde kayıttan önce çıkarıldı).
* Yeni eklenen kökler (kok_ekle) korpusta tek token ise ayet ★★★ 'hapaks' alır (49:11, 12, 14) — kaynak etiketiyle birlikte yazılır, içerik iddiası değil.
* Emsal farkı ancak metin yeniden basılınca görünür: lemma dizisi aynı sayılan ayetlerin devamı ayrı olabilir (50:3 — 23:35 2MP 'mittum … muhracûn', diğer üçü 'meb'ûsûn / medînûn'); kıyas cümlesi basılan metinden yazılır.
* Ölçüm mührü ile geçerli mühür tümden ayrışabilir: sûre 50'de 9 ölçüm mührü, karar sonrası 0 geçerli (adlar kitap, kul, tanık, yer, muhatap için) — sûre profili karar sonrası bilançodan.
* `uret_blok_<S>.BASLIK` çapası: önceki satırın sonu kaçışlı tırnak içerebilir; çapa metni önce dosyadan grep ile alınır (sûre 50, 31-40'ta assert yakaladı).

## Bekleyenler
GitHub'da üç silme: `betikler/onarım`, `betikler/onar─▒m`, Arapça adlı `ciktilar/dikey_kisi_*.json` (SILINECEKLER.txt).
Karar bekleyen (kullanıcı: açık kalsın): ◈K tetik فلك kesinlik düzeltmesi (S2) · مأي gloss ('ne zaman' → yüz) · **48:29 çıpa (L4 adayı, teşbih içinde)**.
Esmâ ön-kaydı DONDURULDU; §9 commit `b58c430`. Yalnız veri toplanır.
