# OTURUM — sûre 64 (Teğâbun), 65 (Talâk) ve 66 (Tahrîm) TAM · blok başı kayıt · ek mercekler

**Okunan: 4033 / 6236 ayet (%64,7)** — sûre 1 ve 9-66 TAM, sûre 2 kısmi (1-20).
Devam: **sûre 67 (Mülk, 30 ayet)**. Sûre 2'nin 21-286'sı hâlâ sonraya.
kok_turkce **1433** kök (sûre 64'te 0, sûre 65'te 1: حيض, sûre 66'da 2: صغو, ثيب) · aday havuzu **1-1041** (sûre 64-66'da yeni aday yok, `AX_tegabun` / `AX_talak` / `AX_tahrim` boş) · bağ setleri `AS_tegabun` 62, `AS_talak` 57, `AS_tahrim` 51 · esmâ KARAR 635.
Denetim tabanı: türkçe **0** · anahtar **70**, diff 0 (taban temiz klondan `PYTHONHASHSEED=0 python3 k/betikler/anahtar_denetim.py`, "taranan" satırı hariç; blok denetimi `repo/betikler/` kopyasıyla — calisma/ kopyası korpusu bulamıyor, sahte ✗ verir).
Paket: depo `fcf5e41`'e göre fark (sûre 64 + 65 + 66). Bu oturumda verilen zip'ler (aynı taban, her biri öncekini kapsar): `fark_fcf5e41_sure64_ara1.zip`, `fark_fcf5e41_sure64.zip`, `fark_fcf5e41_sure64_65ara1.zip`, `fark_fcf5e41_sure64_65.zip`, `fark_fcf5e41_sure64_65_66_ara.zip`, `fark_fcf5e41_sure64_65_66.zip` (son).
Sûre 66 dosyaları: `kok_ekle_66.py` (2 kök) · `tahrim_metin_1.py` (MEAL1-3/M1-3) · `tahrim_kayit.py` (CIPA, ARIZA, DUZELTME 0) · `uret_blok_66.py` · `aday_ekle_66_tahrim.py` · `yama_retroaktif_gloss_66.py` · `duzeltme_66.py` · `tahrim_kapanis.py` (+ `tahrim_kapanis_notu.txt`; `--kuru` ile yazmadan basar) · `tahrim_paket_md.py` → `notlar/sure66_tahrim_okuma.md`.
Sûre 65 dosyaları: `kok_ekle_65.py` (1 kök) · `talak_metin_1.py` · `talak_kayit.py` · `uret_blok_65.py` · `aday_ekle_65_talak.py` · `yama_retroaktif_gloss_65.py` · `duzeltme_65.py` · `talak_kapanis.py` (+ not) · `talak_paket_md.py` → `notlar/sure65_talak_okuma.md`.
Sûre 64 dosyaları: `kok_ekle_64.py` (boş) · `tegabun_metin_1.py` · `tegabun_kayit.py` · `uret_blok_64.py` · `aday_ekle_64_tegabun.py` · `yama_retroaktif_gloss_64.py` · `duzeltme_64.py` · `tegabun_kapanis.py` (+ not) · `tegabun_paket_md.py` → `notlar/sure64_tegabun_okuma.md`.
Sûre 67 için şablonlar `tahrim_*`'dan S=67 (yeni set adları `AX_<ad>/AS_<ad>`; numara 1042'den, `aday_ekle` sırayı doğruluyor). Sûre 44-65 dosyaları: `duhan_*` … `talak_*` (aynı düzen). Bloklar değişken uzunlukta: `<sure>_kapanis.py` ve `<sure>_paket_md.py` içindeki blok listesi elle (BLOKLAR ile aynı) — şablonu kopyalarken güncelle (kapanış betiğinde esma_kayit sûre numarası ve blok listesi de).
**Oturum yardımcıları depoda** (`betikler/`, salt-okur): `oturum_ortak.py` · `oturum_say.py S:A i-j [--on] [--son]` · `oturum_lem.py S:A:W [--kok]` · `oturum_lemdizi.py S A i j` · `oturum_tetik.py S A B <metin>` · `oturum_xy.py S A B <metin>`. Her blokta tetik (0 uyuşmaz) ve [x/y] (0 uyuşmaz) bunlarla koşulur; alıntı/sayı iddiaları lemma sayımıyla. Tetik ön kuru koşusu: geçici `M={n:"◇ x\n◈K — —\n◈B — —\n◈D — x\n◈A — x" ...}` modülü (heredoc ile yaz; `python -c` içinde \n kaçışı bozuluyor), kullanımdan sonra silinir. Araç dondurma kuralına uygunluğu kullanıcı kararına açık (okuma sonunda).
**Dikkat (sûre 66):** `oturum_lem` / `oturum_lemdizi` W / i-j indeksleri durak işaretlerini (ۖ ۚ) SAYMAZ — ayet metnini kelimeye bölüp numaralarken her durak işaretinden sonra 1 düş. 66:9 metni 9:73 ile karakter eşitliğinde aynı, esit2 0,9821 veriyor (924, kayıt). Ölçüm satırının esmâ mühür etiketi (MÜHÜR / MÜHÜRSÜZ) karar sonrası bilançoyla ayrışabiliyor (66:8) — mühür iddiası yalnız `esma_muhur_43_gecerli`'den.
**Aday 1039:** okuma kolu (karşıt çift) — ◇'de 'Karşıt çift (aday 1039, okuma)' notu her ayette sürsün (sûre 64'te 18/18, 65'te 12/12, 66'da 12/12).
**Aday 1040:** ardışık sûre sınırında süreklilik — test korpus sonunda; 67:1 okunurken 66:12 ('ve Meryeme'bnete İmrân … ve kânet mine'l-qânitîn') ile bağ kayıt olarak yazılır. Sûre 66'da: 65:12/66:1 sınır, 65:1/66:1 aynı nidâ, 64:14/65:1/66:1 eşler, 65:1/66:5, 65:5 ve 65:11/66:8.
**Aday 1041:** aynı kelimenin Allah ve insan / başka şey için kullanılması — kayıt (sûre 64'te 2, 65'te 3, 66'da 2 vaka: 'nebbe'e', 'mevlâ').
**Çıpa:** sûre 66'da doğal olgu yok. **48:29 ve 57:20 L4 adayı (teşbih içi), TARTIŞMALI — karar okuma sonunda.**
**Bekleyenler:** kullanıcı kararı (2026-10-21) — bekleyen kararların hepsine TAM OKUMA BİTTİKTEN SONRA bakılacak; oturumlarda sorulmaz, yalnız kaydedilir. Sûre 64-66'da yeni bekleyen karar yok.

Ayrıntılı: `notlar/YAPILACAKLAR.md` → "SÛRE 64 TEĞÂBUN SONU", "SÛRE 65 TALÂK SONU", "SÛRE 66 TAHRÎM SONU".

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
* ARIZA ekleme çapası: `i = t.rindex('\n ],\n}') + 4` (virgülden SONRA); `+3` yeni listeyi `]` ile `,` arasına koyar → SyntaxError (sûre 51, 41-50'de `import` denetimi yakaladı).
* `esma_el_ekle.py` girdi dosyası: yalnız sözlük satırları (`'S:A:W': 'degil',  # gerekçe`), `K = {` sarmalı ve girinti YOK; ilk satır idempotentlik başlığıdır — `# sûre S blok A-B` yorumu koy (sûre 51, 51-60).
* Mühür geçerliliği yalnız bilançodan (`esma_muhur_43_gecerli`): ölçüm satırı ilâhî adlarda da 'MÜHÜRSÜZ' yazabiliyor (51:58 razzâq / metîn); mühür iddiası karar eklendikten sonra bilançodan yazılır.
* Blok başında `git -C k fetch`: uzak depo ilerlediyse yüklenen zip ile `cmp` (dosya dosya) ve fark tabanını güncelle (sûre 51 sonunda 279460e → 0dc5351).

* `anahtar_denetim.py` kökü kendi konumundan bulur: blok denetimi `repo/betikler/` kopyasıyla koşulur; `calisma/` kopyası korpusu bulamaz (0 kök) ve sahte ✗ üretir (sûre 52 kurulumu). `turkce_denetim.py` `repo/tablolar/` içinden `python3 ../betikler/turkce_denetim.py`.
* ARIZA ekleme metni `'\n (A, B): [\n'` ile başlar, `' ],'` ile biter (sonda satır sonu YOK); çapa `t.rindex('\n ],\n}') + 4`. Başta `\n` unutulursa yeni blok önceki `],` satırına yapışır, sözdizimi geçerli kalır ama çapa kaybolur; sonraki ekleme rindex hatasıyla durur (sûre 52, 11-20 → 21-30'da yakalandı). Ekledikten sonra çapa sayısını (1) da doğrula.
* `[x/y]` yalnız o ayetin kendi ölçüm sayısı; başka ayetin sûre içi sırası `sûre içi 52:37 ve 52:41` biçiminde yazılır — `oturum_xy` yakalar (52:41).
* 'okunan X, Y' de '(okumada görüldü)' kuralına tabidir: lemma listesinde †'sız olması yetmez, bu oturumda AR metni basılmadan 'okunan' yazılmaz, bağa 'okundu' konmaz (sûre 52: 52:11'de 16:36, 43:25 — DUZELTME; 52:36'da kayıttan önce çıkarıldı).
* Emsalin bağlam nitelemesi ('ateş ehlinin', 'bahçe ehlinin' soruşması) de basılan ayetlere dayanır; bağlam ayetleri tek tek basılır ve adlanır (52:25 — 37:22, 23, 24, 43).
* Emsal metnindeki kişi / kavim adı yalnız basılan ayette varsa yazılır; komşu ayetten taşınmaz (52:45 — 51:44'te ad yok, 51:43'te var).
* `esitle.py` yalnız .py/.json eşitler; `<sure>_kapanis_notu.txt` `repo/betikler/`'e elle kopyalanır (sûre 52).
* Sûreler arası sıralı eşleşme (aynı ayet sırasıyla iki-dört ayet) ardışık sûrede 1040 alanına, ardışık değilse yalnız okuma bağına yazılır (52:48-49 ← 50:39-40).
* oturum_say / oturum_lemdizi kelime sırası duraklama işaretlerini (ۚ ۖ ۗ ۞ ۩) ATLAR — aralığı ham `split()` sırasıyla değil `oturum_lemdizi.py S A 1 99` listesiyle kur (sûre 53: 53:23, 26, 28, 30 aralıkları kaymıştı).
* Okunmamış ayeti kapsayan aralık ('53:36-41') da anmadır — yalnız okunan ayetler tek tek yazılır (sûre 53, kayıttan sonra yakalandı).
* Okunmuş ama bu oturumda Arapçası basılmamış ayet adla anılmaz; yalnız sayıya katılır (sûre 53: 26:205, 20:133 çıkarıldı).
* 'ٓ' (medd) fâsıla artefaktı: harf ى iken fâsıla 'ٓ' okunur, KAFİYE KIRILMASI ve ★ verir; ardından gelen ى ayeti de kırık işaretlenir. Gerçek sınıf geçişi (53:57 ى → ة) işaretlenmeyebilir (924).
* Kısa tek fiilli ayette gerçek edilgen ★★★ pas z=5,38 verir (53:36, 40, 41, 46) — formül davranışı; morph III. bab etkeni de PASS etiketleyebilir (53:12 'tumârûnehû').
* esma_kayit 'mühür EVET' ile bilanço `esma_muhur_43_gecerli` ayrışabilir — mühür iddiası yalnız geçerli listeden (sûre 53: 3 işaret, 0 geçerli).
* Aktör sınıf/rol etiketi metne bakılmadan alınmaz: 53:49 'Şi'râ' ölçümde 'sahte-ilah, rol fail', metinde izâfet (GEN).
* Sûre sonu e_el=? denetimi sûre anahtarıyla sınırlanır — okuma_metni'nde 34:31, 50:41, 50:45, 51:35, 51:38, 51:50 tabanda e_el=None (95f7b81'de de var); blok denetimi bunları saymaz.
* oturum_say kalıbı harekesiz imlâ farkıyla ayırır (54:42 'bi-âyâtinâ' / 20:56 'âyâtinâ', --on ile de) — eşleşme okumayla yazılır, sayı iddia edilmez.
* Nekre esmâ (54:42 'ahze azîzin muqtedir', 54:55 'inde melîkin muqtedir') göndergeye göre karar alır — sınır vakası olarak işaretlenir; karar eklendikten sonra `esma_kayit.py` yeniden koşulmadan bilanço geçerli mühürü göstermez.
* Alıntı yapılan sûre içi ayetin sözü nota metne bakılarak yazılır (54:47'de 54:24 'elçiye uyarsak' diye yanlış özetlenmişti; kayıttan sonra düzeltildi).
* Sûre 57'den itibaren: okunmamış sûre listesi 3-8, 2:21+ ve 57+ — okunan sûrenin kendi ileri ayetleri de 'henüz okunmadı'.
* Nakarat sûrelerinde ayet kalıbı yardımcıyla yazılır (sûre 55 `_nak8`), geçiş numarası ve [x/y] sayıları ölçüm satırından alınır; her blokta oturum_xy 0.
* ARIZA / not dizgelerinde iç tek tırnak kullanılırken dış tırnak çift olmalı (55:61-70 sözdizimi hatası dersi).
* Tek kelimelik ayette mühür ölçütü ile ölçüm satırının 'son konum' etiketi ayrışabilir (55:1) — mühür iddiası yazılmaz, ayrışma ARIZA'ya.
* Paket betiği sed ile kopyalanınca set anahtarı (`AX_<ad>`) elle kontrol edilir (sûre 55'te `AX_kamer` kalmıştı, düzeltildi).
* Kayıt metnine (mercek, ARIZA, DUZELTME, bağ notu) kök biçimi dışında Arapça kelime / imlâ parçası yazılmaz — `anahtar_denetim` T4 olarak sayar (sûre 56: 56:41-50'de 72, 56:81-90'da 76); imlâ farkı Latin harfle tarif edilir ('düz elif' / 'elif-medde'). Düzeltme okuma_metni'nin `duzeltildi` alanına da işlenir.
* Harekesiz kalıp 'fe-levlâ'yı düz elif (56:57, 62, 70) ve elif-medde (56:83, 86) yazımında ayrı sayar — sûre içi 'N kez' iddiası lemma sayımıyla (morph LEM) yazılır (sûre 56: DUZELTME 56:62, 70).
* Okunmamış ayetin esit2 / xref anması da 'henüz okunmadı' işareti ister (56:96 — 69:52).
* Basılan emsal ayetin sûre içi bağlamı ('cennet sahnesinin içinde') basılmamış komşu ayetlerden yazılmaz (56:95 — 37:60, kayıttan önce silindi).

* Uzun ayetli sûrede blok sınırı ayet uzunluğuna göre kurulur (sûre 57: 4-6 ayetlik 7 blok); kapanış ve paket betiklerindeki blok listesi BLOKLAR ile elle eşlenir.
* Okunmuş ama basılmamış xref ayeti de adla anılmaz: 'xref … (okunmuş 1 ayet daha)' (sûre 57: 57:21'de sûre 9 xref'i, kayıttan önce yakalandı).
* Basılan emsal ayette olmayan kişi adı, bağlamı anlatırken de yazılmaz (sûre 57: 31:18 için kayıttan önce çıkarıldı).
* Teşbih / mesel içinde 39:21 türü L4 dizisinin tekrarı (57:20) 48:29 gibi 'L4 adayı, TARTIŞMALI' yazılır; cipa=False, karar kullanıcıda — iki vaka birlikte karara bağlanabilir.
* Aynı kelimenin aynı sûrede Allah ve başka gönderge için kullanılması (57:3 / 57:13 zâhir-bâtın) esmâ kararını ayırır: 57:3 İLÂHÎ, 57:13 DEĞİL — aday 1041 alanına kayıt.
* Bağ / ARIZA dizgesinde iç tek tırnak ('ibtiğâ'e') varsa dış tırnak çift; `aday_ekle` betiği koşmadan önce SyntaxError verir (sûre 57, 27-29).
* Ayet 1 ölçümünde harf → harf3 farkı 'isaret' ile açıklanmıyor (56:1, 57:1, 58:1; besmele sayılıyor olabilir) — harf alanından ayet 1 için iddia kurulmaz (924, sûre 58).
* Esmâ 'SON konum' ölçütü ayetin son kelimesi değil: 58:13 'habîr'i 'bimâ ta'melûn' izliyor, ölçüm yine 'SON' diyor — mühür iddiası bilançodan, konum iddiası metinden (1022).
* Sayı işareti kök kaynaklı yanlış alarm verir: عدد 'e'adde' (hazırladı), عشر 'aşîre' (akraba) — sayı iddiası okumayla (sûre 58).
* Dikey ×kat küçük n'li köklerde (n ≤ 5) binlerce kata şişer (58:11 ×5800) — tablodaki değer bulgu sayılmaz (924).
* `oturum_say.py --on` ilk kelime SONEK eşleşmesi: 'fe-bi'se' kalıbı 've bi'se'yi yakalamaz — önek farklıysa lemma sayımına geç (58:8).
* 'yâ eyyuhâ' korpusta tek kelime (يأيها) — kelime aralığını ayetin kendi sayımından al (58:9).
* aday_ekle / kayıt eklerini heredoc içinde yazarken kaçış dizisini iki kez kaçırma (`\\'` sözdizimi hatası, betik koşmaz) — tek kaçış ya da çift tırnak (sûre 58).

* Yeni kök eklerken `yama_retroaktif_gloss_<S>` genel geçiş sayısı 0 değilse değişen alanlar tek tek okunur: gloss_gecis harekesiz özel ad iskeletini kök sanabilir (sûre 59: همن ↔ Hâmân, 28:6 / 28:8 nakarat2 dizgesi — `yama_haman_59.py` ile açıklama notuna çevrildi; araç değişmedi).
* Kök sayımı (أله [x/y]) lafız sayımı değildir — 'ilâh' tokenlerini de içerir; lafız sayısı bilançodan (sûre 59: 59:24 'lafız 31. ve son token' → DUZELTME; lafız 29).
* Kayıttan sonra yakalanan kendi hatası blok betiği yeniden koşularak düzeltilmez — `<sure>_kayit.DUZELTME` + `duzeltme_<S>.py` (özgün alan korunur); sûre 59'da 59:17 alıntısı yanlışlıkla yeniden koşuyla düzeltildi.
* DUZELTME 'eski' dizgesi kayıttaki alandan alınır: gloss geçişi kök anmasının ardına karşılık eklediği için kaynak metindeki kök + [x/y] parçası kayıtta birebir yoktur (sûre 59 assert yakaladı).
* Okunmuş ama bu oturumda basılmamış ayeti mercekte anmak gerekiyorsa önce sohbette Arapçası basılır, sonra '(okumada görüldü)' yazılır (sûre 59: 58:12, 9:67).
* Esmâ ölçüm satırı uzun atıfsız ad dizilerinde adları eksik gösterebilir (59:23 sekizden altı, 59:24 beşten dört) — esmâ kararları esma_kayit çıktısındaki konumlardan girilir.
* Lemma listesi eşsesli sözcükleri birleştirebilir: lemma 'asâ' (عصا) değnek ve isyan geçişlerini birlikte sayıyor (37 ayet / kök عصي 32) — eşsesli şüphesinde `oturum_lem.py --kok` ile kök sayısı alınır (sûre 60, 60:12).
* 'Nidâ' sayarken 'rabbenâ' gibi dua nidâları da nidâdır — 'yâ eyyuhe' kalıbı ayrıca sayılır (sûre 60, 60:12 kayıttan önce düzeltildi).
* Blok ARIZA'sında sûre geneline ait gibi okunan blok içi değer ('kafiye kırığı 0') blok içi diye yazılır; [x/y] sayısı son koşudan alınır (sûre 60, 60:11-13 ARIZA notu).

* Ders / emsal göndermesi ('48:3 dersi', '49:11 dersi') de ayet anmasıdır: bu oturumda basılmamış okunmuş ayetin numarası ders adı olarak da yazılmaz — 'yıldız formülü dersi' gibi numarasız yazılır (sûre 61: 61:3, 61:4 kayıttan önce yakalandı).
* Esmâ: izâfetli 'nûr' ('nûra'llâh', 'nûrihî') DEĞİL (39:69 emsali); insan çoğulları 'ensâr', 'zâhirîn' DEĞİL — 'ensâru'llâh' Allah'a izâfet olsa da göndergesi insan (sûre 61: 61:8, 61:14).
* Oturum ertesi güne sarkarsa ortamın korunduğu `okuma_metni['<S>']` anahtarları ve ilerleme sayısıyla doğrulanır; ardından `git -C k fetch origin` (sûre 61: ortam korunmuştu, 3962 ile devam edildi).
* `uret_blok_<S>.py` her koşuda bütün BLOKLAR betiklerini yeniden üretir; önceki blok betikleri yeniden KOŞULMAZ (kayıt değişmez) — esitle değişiklik göstermemeli.

* Şablon sözdizimi denetimi `python3 -m py_compile <betik>` ile yapılır; `python3 -c 'import aday_ekle_<S>_<ad>'` modül düzeyindeki kodu KOŞTURUR ve repo JSON'larını yazar (sûre 62 kurulumu: boş AX / AS yazıldı; idempotent olduğu için zarar yok).
* Karşıt çift satırına metinde söylenmeyen bir karşıt ('… / anlamaz') eklenmez; yalnız metindeki iki uç yazılır (sûre 62: 62:5 kayıttan önce silindi).
* Ardışık iki sûre aynı kalıpla açılıyorsa (61:1 / 62:1) 1040 alanına sûre sınırı bağından (son ayet → ilk ayet) ayrı olarak yazılır; ardışık olmayan eş (59:1) okuma bağıdır.
* Esmâ 'âlim' / 'alîm' lafız olmadan da ('ilâ âlimi'l-ğayb') İLÂHÎ kararı alabilir — sınıf E; mühür bilançodan (sûre 62: 62:8).

* Lemma listesindeki okunmuş ayetlerin içeriği hakkında toplu iddia ('hepsinde X') yazılmaz; bu oturumda basılmayan ayetin metni görülmemiştir — yalnız sayı yazılır (sûre 63: 63:4 'sayha', kayıttan önce silindi).
* Ölçüm xref'indeki okunmuş ama bu oturumda basılmamış ayet de adla anılmaz: "xref '…' → okunmuş 1 ayet (ölçüm)" (sûre 63: 63:6, 63:11).
* Retroaktif yama hedef listesine sûre 2'nin okunmamış ayetleri (21+) girer: betik `OKUNAN` kümesini sûre anahtarından kurar, sûre 2 kısmi kayıtlı. Kayıt yoksa atlanır; yama 0 — 'daha önce okunmuş 1 ayet' çıktısı okunmamış 2:A olabilir (sûre 63: 2:247).

* Tetik ön kuru koşu dosyasını `cat > … <<EOF` ile yazarken önce `cat` komutunun girişi açık kalmamalı: sûre 64 kurulumunda heredoc'suz `cat > dosya` komutu girdi bekleyip zaman aşımına düştü — dosya Write aracıyla ya da tam heredoc ile yazılır.
* Bilanço kafiye kırığı işaretlemesi tutarsız: sûre 64'te ر → م geçişi 64:9'da işaretlendi, 64:5 ve 64:11'de işaretlenmedi (sekiz geçiş işaretsiz) — fâsıla iddiası ölçümün 'KAFİYE KIRILMASI' etiketinden değil, ayet ayet fâsıla harfinden yazılır (924).
* Kasemde Rab ('ve rabbî', 64:7) sûre içinde ilk blokta görülünce 'sûre içi tek' yazılmaz; sonraki bloklar okunmadan sayılmamış sayılır — 'şimdiye dek' yazılır, kesin sayı sûre bilançosundan (sûre 64, kayıttan önce yakalandı).
* Kök sayımı ile lafız sayımı ayrımı (sûre 59 dersi) sûre bilançosunda da: sûre 64'te kök أله 21, lafız 20 — fark 'lâ ilâhe' tokeni (64:13).
* 'innemâ' hasrı ölçüm kip / biçim alanında HASR olarak çıkmıyor ('mâ … illâ' çıkıyor) — hasr gözlemi ◈D'ye '(okuma; ölçüm HASR yazmıyor)' notuyla (64:12, 64:15).
* Oturum ertesi güne sarktığında `git -C k fetch` uzak dalları da getirir (`origin/sebahattintanas-patch-1` görüldü); taban karşılaştırması `origin/main` ile yapılır (fcf5e41 değişmedi).

* Uzun ayetli sûrede (65) sûre içi sıralı sayılar daha sonraki bloklara taşar: bir kökün sûre içi ilk geçişini 'ilk' diye yazmadan önce önceki bloğun ölçüm satırına bakılır — 65:4 'selâse' için 'ilk gerçek sayı' yazılmıştı, 65:2 'zevey' (ikil) gözden kaçmıştı (kayıttan önce düzeltildi).
* Sayı işareti kök kaynaklı yanlış alarmı sûre 65'te de: 65:10 'e'adde' (عدد, hazırladı) — sûre 58 dersi geçerli.
* Bir sûrede hiç geçerli esmâ mührü çıkmayabilir (sûre 65: 1 ölçüm mührü, 0 geçerli) — sûre profili karar sonrası bilançodan yazılır; 'mühür yok' bir bulgu değil, kayıttır.
* Çıpa L4 'sınıf' kolu kelime düzeyinde hukukî sınıflamaya da uyabilir (65:4 aybaşı / gebelik — iddet sınıfları): 799 ilkesi ('ölçü neyi ölçüyor') uygulanır, sınır vakası notu düşülür, karar sorulmaz.
* Retroaktif yama hedefine sûre 2'nin okunmamış ayeti girmesi yinelendi (65:4 حيض → 2:222); 'daha önce okunmuş 1 ayet' çıktısı okunmamış 2:A olabilir — kayıt yoksa atlanır, yama 0.

## Bekleyenler
GitHub'da üç silme: `betikler/onarım`, `betikler/onar─▒m`, Arapça adlı `ciktilar/dikey_kisi_*.json` (SILINECEKLER.txt).
Karar bekleyen — **kullanıcı kararı (2026-10-21): hepsine tam okuma bittikten sonra bakılacak; oturumlarda karar sorulmaz, yalnız kayda yazılır**: ◈K tetik فلك kesinlik düzeltmesi (S2) · مأي gloss ('ne zaman' → yüz) · **48:29 ve 57:20 çıpa (L4 adayı, teşbih içinde)** · oturum_* yardımcılarının depoda kalması · gloss_gecis özel ad iskeleti çakışması (sûre 59).
Esmâ ön-kaydı DONDURULDU; §9 commit `b58c430`. Yalnız veri toplanır.
