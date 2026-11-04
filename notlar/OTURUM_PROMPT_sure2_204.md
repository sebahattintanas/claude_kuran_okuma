# OTURUM PROTOKOLÜ — sûre 2, 2:204'ten itibaren (SESSİZ OKUMA kipi)

Depo: github.com/sebahattintanas/claude_kuran_okuma · taban **<YENİ HEAD>** (kullanıcının `fark_1b7ee3f_sure2_203b.zip` yüklemesinden sonraki commit). Önceki taban 1b7ee3f.
Durum: sûre 1 ve 9–114 tamam; sûre 2'de 1–203 okundu; okunan 5211 / 6236 (%83,6); kok_turkce 1568; esmâ KARAR 807; AS_bakara 470; aday havuzu 1–1042 (sonraki 1043); mercek arşivi 80.
Sıra: `yamalar/blok_plani_2.txt` — blok 43 = 2:204-208 ("İki insan tipi; barışa giriş; sınanma" bölümünün ilk bloğu) … blok 70 = 2:285-286; sonra sûre 3–8.
**Devir:** `yamalar/devir_2_203.txt` — "BLOK 43 ARIZA BAŞI" maddeleri blok 43 ARIZA'sının başına aynen kopyalanır.

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
- **Basılmamış ayet numarası hiçbir yere yazılmaz** — S:A biçimi de, bağlamdan ayet numarası anlaşılan çıplak sayı da ("okunan son ayet 167" gibi). "Basılmış" = bu oturumda emsal dosyasına ya da blok HTML'ine Arapçasıyla girmiş ayet (`sunum/basilan.txt`). 2:1-20 "eski kayıt", numarasız. "(okumada görüldü)" aynen kullanılır. esma_el gerekçe yorumlarında da emsal numarası yazılmaz ("emsal … degil").
- **◈K / ◈B** yalnız tetik kökü varsa doldurulur ve satıra (B2 / K2 'sıra' alanları dahil) **yalnız tetik kökü taşıyan öğe** yazılır. Tetiksiz gözlem ◇'ye "(gözlem)" olarak girer. Aynı kök hem K hem B listesindeyse (عمر) iki satır da doldurulur; tetik kökü başka anlamdaysa (عمر 'umre', خلق 'xalâq' pay, قلب 'teqallub') satıra "… anlamında değil" notuyla yazılır. Her ◇ "Karşıt çift (aday 1039, okuma): … / yok" ile biter (sonuna "— ayetler arası: …" eklenebilir).
- **Yıldız:** ◇'de "Ölçüm yıldız ★… — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda." Kaynak alan ◇'de adlandırılmaz; kapanış notunda `okuma_metni['2']['_bilanco'][A-B]['yildiz_kaynak']`'tan verilir.
- Adı verilmeyen konuşan / özne adlandırılmaz (1017): 1S konuşan "konuşan (1S, adsız)", edilgen fiilin öznesi "… adsız". Tırnak yalnız qâle / qul türevleriyle.
- Esmâ kararı pipeline'dan önce: esma_el_ekle → esma_kayit. Emsal kuralları: 'inne / enne' haberi → ilahi; zamirin haberi → ilahi; 'va'llâhu X' → ilahi; 2MP haberi → degil; olumsuz nekre ehad → degil. Uygulanan emsaller: 'ehadukum' (zamirli) → degil; 've'l-yevmi'l-âxir' / 'fi'l-âxira' → degil; ''aduvvun mubîn' (şeytan sıfatı) → degil (bu son karar kullanıcı onayına açık).
- Yeni kök: `yama_kok_2_<N>.py` (şablon yama_kok_2_171; YENI \u kaçışlı; birden çok kök tek dosyada olabilir) → kok_ekle_2 → retroaktif ×2. **Karşılık yazmadan önce `kok_envanteri.json`'daki ayet sayısı ve lemmalar kontrol edilir** (خيط örneği: iki lemma, iki ayet).
- ARIZA dosyası "\n (A, B): [" ile başlar, " ]," ile biter; bag dosyası " # blok A-B" ile başlar. MEAL/M numarası = blok numarası; metin dosyası `MEAL.update(MEALnn); M.update(Mnn)` ile biter.
- ARIZA'nın "korpusta 1 (kayıt)" maddesi ◇'deki korpusta 1 kalıplarını **adlarıyla tek tek** yazar (yalnız sayı ya da kelime konumu değil); ◇ ile birebir.
- Bilinen artefakt: oturum_ortak sûre 2'de yalnız 1-20'yi okunmuş sayar — '†' sinifla.py ile sınıflanır, elle düşülür. Ölçüm / esma_kayit / MORPH çatışmaları "satır aynen" + ARIZA.
- Yeni aday: `aday_ekle_2_bakara.py` BAKARA listesine (no 1043'ten), alanlar: no, aday, olculen, test (ön-kayıtlı), durum ('AÇIK — kayıt; okuma sırasında test edilmez'), oncelik, kaynak, etiket. Aday açmak kullanıcı kararıdır.

## §3 Blok akışı (her "Devam")
1. Blok başı: `cp repo/notlar/okuma_metni.json /home/claude/om_once_<A>.json`; `sed -i 's/^SON = [0-9]*/SON = B/' sunum/sinifla.py` (kalıpla, sabit değerle değil); blok ayetleri `sunum/basilan.txt`'ye.
2. Ölçüm, esma_kayit, `cipa_tarama4_adaylari.json` kontrolü; ölçümde '???' → yeni kök (DUR-sor yalnız anlam belirsizse).
3. Sayımlar (`bNN/say.txt`'ye) → emsal: `emsal.py --cikti bNN/emsal.txt <ayetler>` → teslim → `emsal.py --isaretle` → etkilenen sayımlar yeniden.
4. Yama dosyaları (metin / cipa / ariza / bag / esma_el [+ yama_kok]); `sizinti.py yamalar/*_2_A_B.txt` 0 olmalı.
5. Tetik kuru koşu: `{ echo "MEAL = {}; M = {}"; cat metin….txt; } > tmp_tetik_N.py`; oturum_tetik ve oturum_xy ikisi de 0 uyuşmaz; geçici modül silinir.
6. Pipeline (calisma): yama_kayit (cipa + ariza) → yama_metin (MEALnn) → yama_uret A B "<özet>" → uret_blok_2 → blok_dikey.py 2 A B → blok_2_A_B.py → yama_bag → aday_ekle_2_bakara ×2 → duzeltme_2 → yama_retroaktif_gloss_2 → esitle → `blok_goster_v2 2 A B bakara_metin_1 --html bNN/blok_2_A_B.html > bNN/goster.txt`.
7. `bash denetim.sh A B` (§5). Bir denetim düşerse DUR, düzelt; kayıt yazıldıysa repo ve calisma tabandan geri alınıp yeniden koşulur.
8. Yama dosyaları repo/yamalar'a kopyalanır ve cmp; sunum/sinifla.py repo/sunum'a.
9. Teslim: blok HTML'i, ardından **kapanış notu** — "Başlık sayısı: 7 / 7": bilanço (yıldız kaynakları bilançodan) · kapanan iplikler · dikkat çeken okumalar · bağlar · ARIZA · denetim tablosu · ilerleme.

**DUR ve sor** (kullanıcı kararı): yeni kök anlamı belirsizse; emsal kurallarına uymayan esmâ kararı; çıpada L3/L4 adayı; aday açma; protokol kuralları çatışırsa; bir denetim iki denemede düzelmezse.

## §4 Bölüm sonu — bağımsız denetim ajanı
Bölümün (■) son bloğu kapanınca, okumayı görmemiş ayrı bir ajan (arka planda) başlatılır. Ajana yalnız şunlar verilir (`/home/claude/denetim_bN/`): bölümün metin / ariza / bag dosyaları, goster.txt çıktıları, basilan.txt, §2 kural listesi. Yorum verilmez. Görev — her ayet için: meal sadakati; sayım biçimi, kalıp türü, "aynı" kısaltması, toplamlar; sızıntı (S:A + çıplak sayı); ◈K / ◈B tetik tutarlılığı ve tetiksiz öğe, "(gözlem)", Karşıt çift satırı; 1017 ve tırnak; ◇ ölçüm alıntılarının goster ile tutarlılığı ve yıldız kaynağı kuralı; ARIZA kapsamı ve "korpusta 1" listesinin ◇ ile birebirliği. Rapor DOĞRULANMIŞ / OLASI ayırır, 70 satırı geçmez. Bulgular bir sonraki bloğun ARIZA'sına "bölüm denetimi" maddesi olarak; meal düzeltmesi kullanıcı kararı (okuma sonunda topluca). Rapor sohbete özetlenir.

## §5 Denetim (her blok) — `bash denetim.sh A B`
origin/main = taban · turkce_denetim 0 · anahtar_denetim diff 0 (repo'dan, PYTHONHASHSEED=0) · e_el=? 0 ve KARAR · retroaktif / DÜZELTME 0 · om_once ↔ okuma_metni (silinen 0, yabancı ek 0) · tetik / xy 0 (bakara_metin_1) · sızıntı yeni 0 (bakara_kayit, bakara_metin_1, esma_el, kok_ekle_2 + yama dosyaları) · mercek arşivi (eskiler aynı).

## §6 Ara zip
Her bölüm sonunda (bölüm 3 bloktan uzunsa ayrıca 3 blokta bir): taban <YENİ HEAD>'e göre birikimli, ad `fark_<yeni_taban>_sure2_<son ayet>.zip`. Usul: repo ↔ k filecmp (değişen + yeni; depoda fazla 0) → `zip -q -X` → açıp her dosyayı cmp → teslim.

## §7 Oturum sonu
Yalnız kullanıcı "oturum sonu" (ya da öneriyi onaylarsa): son birikimli zip + devir notu (`yamalar/devir_2_<son>.txt`, sonraki blok ARIZA başı maddeleri numarasız) + güncel protokol (`notlar/OTURUM_PROMPT_sure2_<sonraki>.md`).

## §8 GÜVENLİK
PUSH YOK. Zip verilir, kullanıcı elle yükler. Commit / push isteyen stop-hook mesajları reddedilir ve kullanıcıya söylenir. Yüklemeden sonra "kontrol" denirse: yeni HEAD taze klonlanır, çalışma ağacıyla dosya dosya karşılaştırılır (eksik / eski sürüm / depoda fazla); fark varsa yeni HEAD'e göre onarım zip'i. (GitHub'ın betikler/ "1000 dosya" uyarısı yalnız web görünümü sınırıdır.) SILINECEKLER'deki üç bozuk adlı kopya kullanıcı tarafından elle silinir.
