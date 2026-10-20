# OTURUM — sûre 56 (Vâqı'a) TAM · blok başı kayıt · ek mercekler

**Okunan: 3867 / 6236 ayet (%62,0)** — sûre 1 ve 9-56 TAM, sûre 2 kısmi (1-20).
Devam: **sûre 57 (Hadîd, 29 ayet)**. Sûre 2'nin 21-286'sı hâlâ sonraya.
kok_turkce **1414** kök · aday havuzu **1-1041** (sûre 56'da yeni aday yok, `AX_vakia` boş) · bağ seti `AS_vakia` 168 · esmâ KARAR 483.
Denetim tabanı: türkçe **0** · anahtar **70**, diff 0 (taban temiz klondan `PYTHONHASHSEED=0 python3 k/betikler/anahtar_denetim.py`, "taranan" satırı hariç; blok denetimi `repo/betikler/` kopyasıyla — calisma/ kopyası korpusu bulamıyor, sahte ✗ verir).
Paket: depo `dd30f51`'e göre fark (sûre 56 bu zip'te). Ara zip'ler 56:1-30 ve 56:1-60'ta verildi (aynı taban).
Sûre 56 dosyaları: `kok_ekle_56.py` · `vakia_metin_1.py` (MEAL1-10/M1-10) · `vakia_kayit.py` (CIPA, ARIZA, DUZELTME 4) · `uret_blok_56.py` · `aday_ekle_56_vakia.py` · `yama_retroaktif_gloss_56.py` · `duzeltme_56.py` · `vakia_kapanis.py` (+ `vakia_kapanis_notu.txt`; `--kuru` ile yazmadan basar) · `vakia_paket_md.py` → `notlar/sure56_vakia_okuma.md`.
Sûre 57 için şablonlar `vakia_*`'dan S=57 (yeni set adları `AX_/AS_`; numara 1042'den, `aday_ekle` sırayı doğruluyor). Sûre 44-55 dosyaları: `duhan_*` … `kamer_*`, `rahman_*` (aynı düzen).
**Oturum yardımcıları depoda** (`betikler/`, salt-okur): `oturum_ortak.py` · `oturum_say.py S:A i-j [--on] [--son]` · `oturum_lem.py S:A:W [--kok]` · `oturum_lemdizi.py S A i j` · `oturum_tetik.py S A B <metin>` · `oturum_xy.py S A B <metin>`. Her blokta tetik (0 uyuşmaz) ve [x/y] (0 uyuşmaz) bunlarla koşulur; alıntı/sayı iddiaları lemma sayımıyla. Tetik ön kuru koşusu: geçici `M={n:"◇ x\n◈K — —\n◈B — —\n◈D — x\n◈A — x" ...}` modülü (heredoc ile yaz; `python -c` içinde \n kaçışı bozuluyor), kullanımdan sonra silinir. Araç dondurma kuralına uygunluğu kullanıcı onayına açık.
**Aday 1039:** okuma kolu (karşıt çift) — ◇'de 'Karşıt çift (aday 1039, okuma)' notu her ayette sürsün (sûre 56'da 96/96).
**Aday 1040:** ardışık sûre sınırında süreklilik — test korpus sonunda; 57:1 okunurken 56:96 ile bağ kayıt olarak yazılabilir (sûre 56: 55:78 / 56:1, 55:7 / 56:3, 55:37 / 56:4-6, 55:52 / 56:7, 55:60 / 56:24).
**Aday 1041:** aynı kelimenin Allah ve insan için kullanılması — kayıt (sûre 56: 56:59 خلق, 64 زرع, 69 نزل, 72 نشأ; ayet içi insan 2MP soru / 1P).
**Çıpa:** sûre 56'da L4, L3, L2 yok; L1 18 ayet; L0 56:57, 62; olgu değil 18 ayet (insan sınıfları, cennet, cehennem); **48:29 ekin büyümesi L4 adayı, teşbih içinde — TARTIŞMALI, karar kullanıcıda**.

Ayrıntılı: `notlar/YAPILACAKLAR.md` → "SÛRE 56 VÂQI'A SONU".

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

## Bekleyenler
GitHub'da üç silme: `betikler/onarım`, `betikler/onar─▒m`, Arapça adlı `ciktilar/dikey_kisi_*.json` (SILINECEKLER.txt).
Karar bekleyen (kullanıcı: açık kalsın): ◈K tetik فلك kesinlik düzeltmesi (S2) · مأي gloss ('ne zaman' → yüz) · **48:29 çıpa (L4 adayı, teşbih içinde)**.
Esmâ ön-kaydı DONDURULDU; §9 commit `b58c430`. Yalnız veri toplanır.
