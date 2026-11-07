# OTURUM PROTOKOLÜ — sûre 2, 2:265'ten itibaren (SESSİZ OKUMA kipi)

Depo: github.com/sebahattintanas/claude_kuran_okuma · taban = **706f39c** (1020844 + `fark_1020844_sure2_264` yüklemesi, altı commit, 68 dosya; 2026-11-07 klonla doğrulandı: eksik 0 / farklı 0 / depoda fazla 0) + oturum sonu zip'i `fark_706f39c_sure2_264` (devir notu + bu protokol; yüklenince yeni HEAD). Kurulumda: taze klon → `git log 706f39c..HEAD --stat` yalnız oturum sonu zip yüklemesini (ve varsa kökteki fazla kopyaların silinmesini) göstermeli; zip'teki dosyalar repo ile dosya dosya karşılaştırılır (eksik 0 / farklı 0) — fark varsa DUR ve sor. Bilinen fazla: kökte `esma_kayit.json` ve `kok_turkce.json` (yanlış yere yüklenmiş kopyalar; doğruları `tablolar/` altında; 706f39c'de hâlâ duruyorlar) — silinmemişlerse dokunma, kullanıcıya hatırlat.
Durum: sûre 1 ve 9–114 tamam; sûre 2'de 1–264 okundu; okunan 5272 / 6236 (%84,5); kok_turkce 1574; esmâ KARAR 870; AS_bakara 590; aday havuzu 1–1042 (sonraki 1043); mercek arşivi 105 (blok ilk yazımında eski mercek satırları arşivlenir — sayı artar, 'eskiler aynı' denetlenir).
Sıra: `yamalar/blok_plani_2.txt` — blok 63 = 2:265-267 ("İnfak meselleri" bölümünün ikinci bloğu; bölüm 62-65, 3 bloktan uzun → blok 64 sonunda ara zip; bölüm denetimi blok 65 sonunda, blok 62 dahil — blok 62'nin goster.txt'i `blok_goster_v2 2 261 264 bakara_metin_1 --html b62/…` ile yeniden üretilir) … blok 70 = 2:285-286; sonra sûre 3–8.
**Devir:** `yamalar/devir_2_264.txt` — "BLOK 63 ARIZA BAŞI" maddeleri blok 63 ARIZA'sının başına aynen kopyalanır (numarasız; kopyalamadan sonra sızıntı taraması).

## §0 Kurulum (oturum başında bir kez)
- Taze klon → `/home/claude/k` (taban, dokunulmaz); `cp -a k repo` (yükleme ağacı).
- `/home/claude/calisma` = düz çalışma kopyası: `betikler/ tablolar/ veri/` düz dosyaları + `ciktilar/` düz dosyaları (yalnız calisma'da eksik olanlar) + `ciktilar/defter.json` + `betikler/onarim/` (dizin olarak) + `ciktilar/cipa_tarama4_adaylari.json`. **`notlar/` dosyaları calisma'ya KONMAZ** (esitle.py notlar/'ı tanımıyor, onları repo/tablolar'a yazar; kayıt betikleri notlar'ı doğrudan repo/notlar'dan okur-yazar).
- `ayet_iskelet.json` calisma'da üretilir: `python3 onarim/04_ngram_altyapi.py` (blok_dikey için gerekli).
- `/home/claude/yamalar` ← `repo/yamalar`; `/home/claude/sunum` ← `repo/sunum` (`basilan.txt` boş başlar); blok çıktıları `/home/claude/bNN/`.
- Sayım yardımcısı `/home/claude/say.sh` (calisma'da `. ../say.sh`):
```
run(){ t=$1; shift; r=$1; case $t in
 say) out=$(python3 oturum_say.py "$@" 2>/dev/null);;
 lem) out=$(python3 oturum_lem.py "$@" 2>/dev/null); r=$(echo $r|cut -d: -f1,2);;
 dizi) out=$(python3 oturum_lemdizi.py "$@" 2>/dev/null); r="$1:$2";;
 esac
 echo "### $t $*"; echo "$out" | head -c 1500; echo; echo "$out" | python3 /home/claude/sunum/sinifla.py $r; echo; }
```
  Kullanım: `run say 2:A i-j [--on] [--son]` · `run lem 2:A:W [--kok]` · `run dizi 2 A i j`.
- Ölçüm (calisma'da): `python3 -c "import olcum_bicim as o; print(o.olcum(2,A))"`.
- Anahtar tabanı: `cd k && PYTHONHASHSEED=0 python3 betikler/anahtar_denetim.py > ../anahtar_taban_ham.txt; grep -v taranan ../anahtar_taban_ham.txt > ../anahtar_taban.txt` (beklenen BOZUK 70). Türkçe tabanı: `cd k/tablolar && python3 ../betikler/turkce_denetim.py` (0).
- Denetim betiği: `cp repo/sunum/denetim.sh /home/claude/` — `bash denetim.sh A B` §5 denetimlerinin hepsini koşar (om_once_A.json ve anahtar_taban.txt gerekir).

## §1 Kip: SESSİZ OKUMA
Okuma eksiksiz yapılır; yalnız **gösterim** kalkar. Her "Devam" = **bir plan bloğu** (birleştirilmez — kullanıcı kararı: veri kaçmasın). Blok dökümü sohbete basılmaz, elle kopya / NFC karşılaştırması yapılmaz — dosyalar doğrudan teslim edilir.
Sohbete giden: (a) blok sonunda **kapanış notu** (§3), (b) emsal dosyası ve blok HTML'i (SendUserFile, attach), (c) bölüm sonunda bağımsız denetim raporu (§4) ve ara zip (§6).

## §2 Kurallar
- Ölçüm ve dikey asla elle yazılmaz. Elle yazılan yalnız meal ve ◇ / ◈ satırlarıdır. Bab, kip, şahıs, z, n, nakarat3 sayıları ◇'ye yalnız ölçüm satırından alıntılanır.
- Sayımlar oturum_say / oturum_lem / oturum_lemdizi'den alınır, sinifla.py ile sınıflanır. Biçim: "N ayet: <bu>, <basılanlar> (okumada görüldü), henüz okunmamış N ayet (sûre içi k), okunmuş N ayet (sûre içi k)". Tekil: "korpusta 1". Kalıp türü her zaman adlandırılır (harekesiz / önek kesilmiş / lemma / lemma dizisi / kök). **Sayıma dayanan her cümle ("üçüncü kez" vb.) bu biçimde yazılır.**
- **"aynı …" kısaltması yasak** (ne "aynı 4 ayet" ne "lemma dizisi aynı korpusta 1"): kalıp ya da dizi her seferinde açıkça yazılır.
- **Lemma dizisi** oturum_lemdizi çıktısındaki lemma listesinden eksiksiz kopyalanır; edat lemmaları ('li', 've', 'bi' …) yazılır, boş lemma () sayılmaz.
- "önek kesilmiş" = `oturum_say --on`: ilk kelimede SONEK eşleşmesi. Baştaki ve- / fe- / li- farkı korpus tarafında eşleşmez (araç tanımı); ARIZA'da gerektiğinde not edilir.
- **Basılmamış ayet numarası hiçbir yere yazılmaz** — S:A biçimi de, bağlamdan ayet numarası anlaşılan çıplak sayı da ("okunan son ayet 167" gibi). **Sohbet dahil**: kullanıcıya sorulan sorularda (AskUserQuestion) ve okuma dışı cevaplarda emsal kayıtlarına numarasız atıf yapılır ("daha önce bir sûredeki ekin meseli kaydı"); numara gerekiyorsa önce `emsal.py` ile basılır (önceki oturumda bir çıpa sorusunda sapma oldu). Okuma dışı sorular (kullanıcı karşılaştırma isterse) korpus sayımıyla cevaplanır, ilgili okunmuş ayetler emsal dosyasıyla basılıp işaretlenir; cevap sonraki bloğun ARIZA'sına "okuma dışı karşılaştırma" maddesi olarak yazılır, bağ / aday kaydı kullanıcı kararıdır. "Basılmış" = bu oturumda emsal dosyasına ya da blok HTML'ine Arapçasıyla girmiş ayet (`sunum/basilan.txt`). 2:1-20 "eski kayıt", numarasız. "(okumada görüldü)" aynen kullanılır. esma_el gerekçe yorumlarında da emsal numarası yazılmaz ("emsal … degil").
- **◈K / ◈B** yalnız tetik kökü varsa doldurulur ve satıra (B2 / K2 'sıra' alanları dahil) **yalnız tetik kökü taşıyan öğe** yazılır. Tetiksiz gözlem ◇'ye "(gözlem)" olarak girer. Aynı kök hem K hem B listesindeyse (عمر) iki satır da doldurulur; tetik kökü başka anlamdaysa (عمر 'umre', خلق 'xalâq' pay, قلب 'teqallub') satıra "… anlamında değil" notuyla yazılır. Her ◇ "Karşıt çift (aday 1039, okuma): … / yok" ile biter (sonuna "— ayetler arası: …" eklenebilir).
- **Yıldız:** ◇'de "Ölçüm yıldız ★… — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda." Kaynak alan ◇'de adlandırılmaz; kapanış notunda `okuma_metni['2']['_bilanco'][A-B]['yildiz_kaynak']`'tan verilir.
- Adı verilmeyen konuşan / özne adlandırılmaz (1017): 1S konuşan "konuşan (1S, adsız)", edilgen fiilin öznesi "… adsız". Tırnak yalnız qâle / qul türevleriyle. **Bölüm denetimlerinin en sık bulgusu:** adsız denen konuşan aynı satırda bağlamdan adlandırılıyor ("tartışan", "peygamberin sorusu", "geçen kişi", "veren insan", edilgenin faili "söz"). Kural: adsız özne baştan sona — ◇, ◈ satırları, emsal açıklamaları ve mealde — yalnız zamir ya da şahıs etiketiyle anılır; karşılaştırılan emsalin adsız öznesi de adlandırılmaz.
- Esmâ kararı pipeline'dan önce: esma_el_ekle → esma_kayit. Emsal kuralları: 'inne / enne' haberi → ilahi; zamirin haberi → ilahi; 'va'llâhu X' → ilahi; 2MP haberi → degil; olumsuz nekre ehad → degil. Uygulanan emsaller: 'ehadukum' (zamirli) → degil; 've'l-yevmi'l-âxir' / 'fi'l-âxira' → degil; ''aduvvun mubîn' (şeytan sıfatı) → degil (bu son karar kullanıcı onayına açık).
- Yeni kök: `yama_kok_2_<N>.py` (şablon yama_kok_2_171; YENI \u kaçışlı; birden çok kök tek dosyada olabilir) → kok_ekle_2 → retroaktif ×2. **Karşılık yazmadan önce `kok_envanteri.json`'daki ayet sayısı ve lemmalar kontrol edilir** (خيط örneği: iki lemma, iki ayet).
- ARIZA dosyası "\n (A, B): [" ile başlar, " ]," ile biter; bag dosyası " # blok A-B" ile başlar. MEAL/M numarası = blok numarası; metin dosyası `MEAL.update(MEALnn); M.update(Mnn)` ile biter.
- ARIZA'nın "korpusta 1 (kayıt)" maddesi ◇'deki korpusta 1 kalıplarını **adlarıyla tek tek** yazar (yalnız sayı ya da kelime konumu değil); ◇ ile birebir.
- Bilinen artefakt: oturum_ortak sûre 2'de yalnız 1-20'yi okunmuş sayar — '†' sinifla.py ile sınıflanır, elle düşülür. Ölçüm / esma_kayit / MORPH çatışmaları "satır aynen" + ARIZA.
- Yeni aday: `aday_ekle_2_bakara.py` BAKARA listesine (no 1043'ten), alanlar: no, aday, olculen, test (ön-kayıtlı), durum ('AÇIK — kayıt; okuma sırasında test edilmez'), oncelik, kaynak, etiket. Aday açmak kullanıcı kararıdır.
- **Ölçüm satırında '???'** (karşılıksız kök) her ayette ayrı sayılır: `grep -o '???'` — çıktı kısaltılsa bile bu sayım kısaltılmaz (önceki oturumda kısaltma yüzünden bir kök kaçtı).
- **İki yönlü 'satır aynen':** ARIZA'da 'satır aynen' denen her ölçüm satırı (esma_kayit çatışması, aktör, sayı işareti, kafiye kırılması, bağ YOK, mm2 …) ◇'de de 'satır aynen' ile yazılır ve tersi; fâsıla / nakarat3 toplu maddelerinde 'satır aynen' yalnız ◇'de de yazıldıysa kullanılır.
- **Bab:** ◇ okuma kısmında kelime düzeyi bab yazılmaz; lafız dizisinde bab yalnız ölçüm toplamlarıyla birebir tutan fiillerde yazılır, mastarda yazılmaz.
- **◈A ve ◈D:** ◈A'da sayıma dayanan ya da sıra / devam bildiren ifade ('yeniden', 'üçüncü', 'ikinci örnek', 'devamı', 'sürmesi') yazılmaz; ◈D D2 etiketleri ölçüm edim / kip alanıyla sınırlıdır ('soru' / 'haber' ölçümde yoksa yazılmaz; INTG 1 ise tek soru öğesi). ◇ okumada da sıra sözcüğü ('birinci söz', 'üç kez', 'iki ayna cümle') yazılmaz. Ölçüm sayısına dayanan okuma listesi ("olumsuzlarla örülü (ölçüm NEG 5)") yalnız token token eşlenebiliyorsa yazılır.
- **◈K / ◈B alıntısı:** satıra yalnız tetik kökünü taşıyan kelime alıntılanır; yön, fiil, edat ya da tetik dışı tamlama öğesi ('mine'l-meşriq', 'ba'de') eklenmez — gerekiyorsa ◇'ye "(gözlem)".
- **Aktör alıntısı** ölçüm yazımıyla harfi harfine ('kisi'); birden çok giriş ayrı ayrı alıntılanır.
- **İmlâ iddiası** (ör. bir kelimenin ص ile yazıldığı) yazılmadan önce metin kelimesi `oturum_ortak.kelimeler` ile kontrol edilir; morph lemma etiketinin imlâsı metin imlâsı değildir.
- **Lemma dizisi:** oturum_lemdizi PREF bölütlerini (ve-, fe-, li- …) atar — dizinin içindeki atılan edat da ARIZA'da not edilir.
- **Meal takdirleri:** mealde Arapçada karşılığı olmayan her kelime (parantezli ya da parantezsiz: 'kadınların', 'eşleri', 'başka', yeterlik kipi '-ebilir', zamirle karşılanan 'O') ARIZA'nın meal maddesine yazılır; edilgen fiil etkenle karşılandıysa o da yazılır; **karşılıksız kalan her edat** ('fe', 've', 'inne', 'qad', 'zâ') de tek tek yazılır.
- **Araç tanımı farkları** (önek kesilmiş baştaki ve- / fe-; medde yazımı 'عليهمءا' / 'عليهما'; inne / enne hemzesi; lemma 'havl', 'ricâl', 'yemîn' gibi çok anlamlı lemmalar; oturum_lemdizi PREF ayrıştırması) sayım ile nakarat3 / xref arasında fark doğurduğunda ARIZA'da not edilir.
- **Çıpa kademe emsalleri (kullanıcı kararı):** biyolojik süre (emzirme) birimle verilmişse 2:233 kararı L2, cipa=True (L4 emsalleri 31:14 / 46:15 ile fark bilinçli; L3/L4 adayı görüldüğünde yine DUR-sor); hukuk süresi (iddet, îlâ, vasiyet) olgu=False; rahim + yaratılan, süreç yok → L1. **Bu oturumdan:** mucize anlatısı (ilahi öldürme / diriltme, diriltmenin gösterilmesi; kemik → et dizisi ve 'yüz yıl' anlatının parçası) → olgu=False (2:243, 2:259, 2:260); mesel içinde aşamalı doğa dizisi (tane → başak → tane; toprak → sağanak → çıplak taş) → L4 adayı, MEKANİZMA kolu, olgu=True, cipa=False, TARTIŞMALI / KAPATILAMAZ (2:261, 2:264; ekin meseli emsali); güneş + yön + getiren, ölçü / mekanizma yok → L1 (2:258, onaya açık).
- **Esmâ emsalleri (bu oturumdan):** 'melik' insan göndergeli → degil (kullanıcı kararı, yeni emsal; geriye dönük uygulanmadı); 'nûr' ışık → degil, çoğul 'evliyâ' edinilen dostlar → degil, 'allâhu veliyyu …' lafız haberi → ilahi (üçü önceki esma_el kayıtlarına dayanır, onaya açık); 'kâne' haberi 2MP 'mu'minîn' → degil (2MP haberi kuralı).

## §3 Blok akışı (her "Devam")
1. Blok başı: `cp repo/notlar/okuma_metni.json /home/claude/om_once_<A>.json`; `sed -i 's/^SON = [0-9]*/SON = B/' sunum/sinifla.py` (kalıpla, sabit değerle değil); blok ayetleri `sunum/basilan.txt`'ye.
2. Ölçüm, esma_kayit, `cipa_tarama4_adaylari.json` kontrolü; ölçümde '???' ayrı sayılır (`grep -o '???'`) → yeni kök (DUR-sor yalnız anlam belirsizse).
3. Sayımlar (`bNN/say.txt`'ye) → emsal: `emsal.py --cikti bNN/emsal.txt <ayetler>` → teslim → `emsal.py --isaretle` → etkilenen sayımlar yeniden.
4. Yama dosyaları (metin / cipa / ariza / bag / esma_el [+ yama_kok]); `sizinti.py yamalar/*_2_A_B.txt` 0 olmalı. Esmâsız blokta esma_el dosyası yazılmaz. Tek ayetlik blokta dosya adı `_2_A_A` (ör. `_2_258_258`).
5. Tetik kuru koşu: `{ echo "MEAL = {}; M = {}"; cat metin….txt; } > tmp_tetik_N.py`; oturum_tetik ve oturum_xy ikisi de 0 uyuşmaz; geçici modül silinir.
6. Pipeline (calisma): yama_kayit (cipa + ariza) → yama_metin (MEALnn) → yama_uret A B "<özet>" → uret_blok_2 → blok_dikey.py 2 A B → blok_2_A_B.py → yama_bag → aday_ekle_2_bakara ×2 → duzeltme_2 → yama_retroaktif_gloss_2 → esitle → `blok_goster_v2 2 A B bakara_metin_1 --html bNN/blok_2_A_B.html > bNN/goster.txt`.
7. `bash denetim.sh A B` (§5). Bir denetim düşerse DUR, düzelt; kayıt yazıldıysa repo ve calisma tabandan geri alınıp yeniden koşulur — bunun için blok başında (adım 1) `cp -a repo repo_once_A; cp -a calisma calisma_once_A` yedeği alınır (önceki oturumda yedek olmadığından geri alma yapılamadı).
8. Yama dosyaları repo/yamalar'a kopyalanır ve cmp; sunum/sinifla.py repo/sunum'a.
9. Teslim: blok HTML'i, ardından **kapanış notu** — "Başlık sayısı: 7 / 7": bilanço (yıldız kaynakları bilançodan) · kapanan iplikler · dikkat çeken okumalar · bağlar · ARIZA · denetim tablosu · ilerleme.

**DUR ve sor** (kullanıcı kararı): yeni kök anlamı belirsizse; emsal kurallarına uymayan esmâ kararı; çıpada L3/L4 adayı; aday açma; protokol kuralları çatışırsa; bir denetim iki denemede düzelmezse.

## §4 Bölüm sonu — bağımsız denetim ajanı
Bölümün (■) son bloğu kapanınca, okumayı görmemiş ayrı bir ajan (arka planda) başlatılır. Ajana yalnız şunlar verilir (`/home/claude/denetim_bN/`): bölümün metin / ariza / bag dosyaları, goster.txt çıktıları, basilan.txt, §2 kural listesi. Yorum verilmez. Görev — her ayet için: meal sadakati; sayım biçimi, kalıp türü, "aynı" kısaltması, toplamlar; sızıntı (S:A + çıplak sayı); ◈K / ◈B tetik tutarlılığı ve tetiksiz öğe, "(gözlem)", Karşıt çift satırı; 1017 ve tırnak; ◇ ölçüm alıntılarının goster ile tutarlılığı ve yıldız kaynağı kuralı; ARIZA kapsamı ve "korpusta 1" listesinin ◇ ile birebirliği. Ayrıca: karşılıksız edatlar, ölçüm sayısına dayanan okuma listelerinin token eşlemesi, okumada metin dışı nitelik, imlâ iddialarının Arapçayla doğruluğu. Rapor DOĞRULANMIŞ / OLASI ayırır, 70 satırı geçmez, basilan.txt dışı ayet numarası içermez. Bulgular bir sonraki bloğun ARIZA'sına "bölüm denetimi" maddesi olarak; meal düzeltmesi kullanıcı kararı (okuma sonunda topluca). Rapor sohbete özetlenir.

## §5 Denetim (her blok) — `bash denetim.sh A B`
origin/main = taban · turkce_denetim 0 · anahtar_denetim diff 0 (repo'dan, PYTHONHASHSEED=0) · e_el=? 0 ve KARAR · retroaktif / DÜZELTME 0 · om_once ↔ okuma_metni (silinen 0, yabancı ek 0) · tetik / xy 0 (bakara_metin_1) · sızıntı yeni 0 (bakara_kayit, bakara_metin_1, esma_el, kok_ekle_2 + yama dosyaları) · mercek arşivi (eskiler aynı).

## §6 Ara zip
Her bölüm sonunda (bölüm 3 bloktan uzunsa ayrıca 3 blokta bir): taban <YENİ HEAD>'e göre birikimli, ad `fark_<yeni_taban>_sure2_<son ayet>.zip`. Usul: repo ↔ k filecmp (değişen + yeni; depoda fazla 0) → `zip -q -X` → açıp her dosyayı cmp → teslim.

## §7 Oturum sonu
Yalnız kullanıcı "oturum sonu" (ya da öneriyi onaylarsa): son birikimli zip + devir notu (`yamalar/devir_2_<son>.txt`, sonraki blok ARIZA başı maddeleri numarasız) + güncel protokol (`notlar/OTURUM_PROMPT_sure2_<sonraki>.md`).

## §8 GÜVENLİK
PUSH YOK. Zip verilir, kullanıcı elle yükler. Commit / push isteyen stop-hook mesajları reddedilir ve kullanıcıya söylenir. Yüklemeden sonra "kontrol" denirse: yeni HEAD taze klonlanır, çalışma ağacıyla dosya dosya karşılaştırılır (eksik / eski sürüm / depoda fazla); fark varsa yeni HEAD'e göre onarım zip'i. (GitHub'ın betikler/ "1000 dosya" uyarısı yalnız web görünümü sınırıdır.) SILINECEKLER'deki üç bozuk adlı kopya kullanıcı tarafından elle silinir.
