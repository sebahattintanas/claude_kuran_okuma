# OTURUM PROTOKOLÜ — sûre 3 (Âl-i İmrân), bölüm 9'dan sona (SESSİZ OKUMA kipi)

Depo: github.com/sebahattintanas/claude_kuran_okuma · taban = **4dc8d0a** (49cc10e + `fark_49cc10e_sure3_101`; 2026-11-09 taze klonla doğrulandı: çalışma ağacıyla `diff -rq` 0 satır) + bu protokolü ve devir notunu taşıyan oturum sonu zip'i `fark_4dc8d0a_sure3_101` (yüklenince yeni HEAD). Kurulumda: taze klon → `git log 4dc8d0a..HEAD --stat` yalnız o zip'in yüklemesini (ve varsa kökteki fazla kopyaların silinmesini) göstermeli; zip'teki dosyalar repo ile dosya dosya karşılaştırılır (eksik 0 / farklı 0) — fark varsa DUR ve sor. Bilinen fazla: kökte `esma_kayit.json` ve `kok_turkce.json` (yanlış yere yüklenmiş kopyalar; doğruları `tablolar/` altında) — silinmemişlerse dokunma, kullanıcıya hatırlat.
Durum: sûre 1, 2 ve 9–114 tamam; sûre 3'te 1–101 okundu (blok planında 1–21; bölüm 8 kapandı, bölüm denetimi yapıldı); okunan 5395 / 6236 (%86,5); kok_turkce 1586; esmâ KARAR 951; AS_al_imran 323; aday havuzu 1–1042 (sonraki 1043; bu oturumda aday açılmadı); mercek arşivi 29.
Sıra: blok 22 (3:102-106, bölüm 9 açılışı) → blok 41 (3:195-200) → sûre 3 kapanışı (`al_imran_kapanis.py` / `al_imran_paket_md.py` — kullanıcıyla) → sûre 4–8.
**Devir:** `yamalar/devir_3_101.txt` — "SONRAKİ İLK BLOK ARIZA BAŞI" maddeleri blok 22'nin ARIZA'sının başına aynen kopyalanır (numarasız; `bekleyen_ariza_3_b22.txt` ile birebir, ikisi birlikte kopyalanmaz; kopyadan sonra sızıntı taraması).

## §0 Kurulum (oturum başında bir kez)
- Taze klon → `/home/claude/k` (taban, dokunulmaz); `cp -a k repo` (yükleme ağacı).
- `/home/claude/calisma` = düz çalışma kopyası: `betikler/ tablolar/ veri/` düz dosyaları + `ciktilar/` düz dosyaları (yalnız calisma'da eksik olanlar) + `ciktilar/defter.json` + `betikler/onarim/` (dizin) + `ciktilar/cipa_tarama4_adaylari.json`. **`notlar/` calisma'ya KONMAZ** (kayıt betikleri notlar'ı doğrudan repo/notlar'dan okur-yazar; esitle.py calisma → repo eşitler).
- `ayet_iskelet.json` calisma'da üretilir: `python3 onarim/04_ngram_altyapi.py` (blok_dikey için).
- `/home/claude/yamalar` ← `repo/yamalar`; `/home/claude/sunum` ← `repo/sunum` (`basilan.txt` BOŞ başlar; `sinifla.py` içindeki `SON = 101`); blok çıktıları `/home/claude/bNN/`.
- Sayım yardımcısı `/home/claude/say.sh` (calisma'da `. ../say.sh`):
```
run(){ t=$1; shift; r=$1; case $t in
 say) out=$(python3 oturum_say.py "$@" 2>/dev/null);;
 lem) out=$(python3 oturum_lem.py "$@" 2>/dev/null); r=$(echo $r|cut -d: -f1,2);;
 dizi) out=$(python3 oturum_lemdizi.py "$@" 2>/dev/null); r="$1:$2";;
 esac
 echo "### $t $*"; echo "$out" | head -c 1500; echo; echo "$out" | python3 /home/claude/sunum/sinifla.py $r; echo; }
```
  Kullanım: `run say 3:A i-j [--on]` · `run lem 3:A:W [--kok]` · `run dizi 3 A i j`. Çıktıdan son `{…}` sözlüğü (bu / basilan / okunmus / henuz / henuz_si) okunur.
- Ölçüm (calisma): `python3 -c "import olcum_bicim as o; print(o.olcum(3,A))"`.
- Anahtar tabanı: `cd k && PYTHONHASHSEED=0 python3 betikler/anahtar_denetim.py > ../anahtar_taban_ham.txt; grep -v taranan ../anahtar_taban_ham.txt > ../anahtar_taban.txt` (beklenen BOZUK 70). Türkçe tabanı: `cd k/tablolar && python3 ../betikler/turkce_denetim.py` (0).
- `bash sunum/denetim.sh A B` (/home/claude'dan; sûre 3 sürümü) §5 denetimlerinin hepsini koşar (om_once_A.json ve anahtar_taban.txt gerekir).

## §1 Kip: SESSİZ OKUMA
Okuma eksiksiz yapılır; yalnız gösterim kalkar. Her "Devam" = **bir plan bloğu** (`yamalar/blok_plani_3.txt`; birleştirilmez). Blok dökümü sohbete basılmaz. Sohbete giden: (a) emsal dosyası (AR + meal), (b) blok HTML'i, (c) **kapanış notu** (§3 adım 13), (d) bölüm sonunda denetim özeti ve fark zip'i (§4, §6).
**Kullanıcı kararları (bu oturumdan):** yorum ve meal kararları tam okuma sonuna bırakılır; DUR-sor yalnız protokol durumlarında (§3 sonu); zip bölüm sonunda verilir ("bitince alayım"); zip yalnız uzak deponun kaldığı yerden farkı içerir.

## §2 Kurallar
### Kaynak ve sayım
- Ölçüm ve dikey asla elle yazılmaz; elle yazılan yalnız meal ve ◇ / ◈ satırları. Bab, kip, şahıs, z, n, nakarat3 sayıları yalnız ölçüm satırından.
- Sayım biçimi: "N ayet: <bu>, <basılanlar> (okumada görüldü), [eski kayıt N ayet,] henüz okunmamış N ayet (sûre içi k), okunmuş N ayet" ya da "korpusta 1". Kalıp türü komutla birebir adlandırılır (harekesiz = `say` / önek kesilmiş = `say --on` / lemma = `lem` / lemma dizisi / kök).
- **Emsal işaretlemesinden sonra her sayım yeniden çalıştırılır** ve metne son çıktı yazılır (bölüm 8 denetimi: bir harekesiz sayım yeniden koşulmadan başka komutun sonucundan aktarıldı).
- Harekesiz kalıp yazım farkını yakalamaz (sûre 2'de 'ibrâhîm' farklı yazılır) — gerekirse lemma ile bağlanır, ARIZA'da not.
- Ölçüm satırında '???' her ayette ayrı sayılır (`grep -o '???'`).

### Sızıntı ve yasaklı sözcükler
- **Basılmamış ayet numarası hiçbir yere yazılmaz — sohbet dahil.** "Basılmış" = bu oturumda emsal dosyasına ya da blok HTML'ine girmiş ayet (`sunum/basilan.txt`). Okunmamış ayetler (sûre 4–8 ve sûre 3'te blok sonundan sonrası) emsal olarak basılamaz (emsal.py DUR verir) — listeden çıkarılır. Aralık gösterimi yalnız basılmış ayetleri kapsar. xref'te basılmamışlar numarasız: "okunmuş iki ayet ve okunmamış üç ayet (sûre içi 1)".
- **Yasaklı** (yorum, meal ve bağ maddelerinde): "aynı", "ilk", "ikinci", "tek", "her ikisi", "ikisi de", "token", "N ayette"; meal ve bağ maddelerinde ×N. **İzinli:** "nakarat3 N kalıp: X'i süzgeç GEÇER, Y'si GEÇMEZ" / "bir kalıp: süzgeç …" / "hepsi süzgeç GEÇER"; "okunmamış N ayet"; ölçüm kök ikilemesi alıntısında ×N; "bölüm N-k"; kök karşılığı olarak 'evvel' → "ilk" (ARIZA meal maddesinde not); plan başlığından alıntılanan bölüm adı. Ölçümdeki "(2 token, …)" alıntılanmaz: "Allah lafzı 10. ve 22. sırada (ölçüm allah z=…)".
- Metin dışı adlandırma yok (emsal açıklamaları dahil).

### ◇ ve ◈ satırları
- ◇: transliterasyon + lafız dizisi (bab yalnız fiillerde, ölçüm toplamıyla birebir) + ölçüm alıntıları + okuma + sayımlar; "Karşıt çift (aday 1039, okuma): ayet içi: … — ayetler arası: …" ile biter.
- **◈K / ◈B:** yalnız tetik kökünü taşıyan kelime, önek ve edatsız ('el-' serbest). B1 canlı / insan / tayr / nebât; B2 oluşum / üreme / xalq (وضع dahil); B3 organ / duyu; B4 hayat / ölüm. K1 gök / yer / gün içi (nehâr); K2 yevm. Tetik yoksa "◈K — —".
- **◈D:** D1 lafız dizisi; **D2 yalnız ölçüm edim ve kip etiketleri** (biçim etiketi ISTISNA / DIKKAT yazılmaz, ARIZA'da not); **D3 bag listesiyle birebir** (blok içi her bağ iki ucunda da; kök ikilemeleri ayrı ayrı; bloklar arası ardışık bağ yalnız sonraki bloğun D3'ünde — önceki bloğun D3'ü geriye dönük yazılmaz); D4 ölçüm şahıs, sahset, iltifât.
- **◈A:** A1 ölçüm aktörünü tam alıntılar; **her adsız taraf "(…, adsız)"** — söz içi 1P / 1S / 2MP, 'qul' muhatabı 2MS, **edilgen fiilin faili** ("'tunezzele' faili (adsız)") dahil; ◇'de de. A2 edim adları. A3 söz içeriği (yoksa —). **A4 kapalı liste (R9):** hitap açılır; şahıs geçişi X → Y; edim geçişi X → Y; söz açılır / söz kapanır; şart → cevap; soru → cevap; bölüm açılışı / bölüm kapanışı; —. Kapsam (ayet içi) / (ayetler arası). Edim geçişleri ölçüm edim alanından **her değişimde** (blok 21 sonu: 3:101 'soru, şart'); şahıs geçişi ölçüm baskın şahıstan (3:101 baskın 2). 'söz açılır' her iç sözün açıldığı ayette, kapanıyorsa 'söz kapanır' da. '—' ile bölüm kapanışı birlikte yazılmaz. A4 bölüm adını taşır: "'<bölüm adı>' bölümünde".
- **'satır aynen'** yalnız ölçümden kesilmemiş birebir alıntıda; iki yönlü (ARIZA'da denen ◇'de de denir).
- **Yıldız:** "Ölçüm yıldız ★… — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda" ya da "Ölçüm 'yıldız yok'". Kaynak kapanış notunda `okuma_metni['3']['_bilanco']['A-B']['yildiz_kaynak']`'tan.
- **nakarat3** sayıyla özetlenir ve "süzgeç" içerir.
- Transliterasyon: wasl öncesi 've''; ث = 'th' (themen, mithl, kethîr, mîthâq).

### Tırnak ve söz
- Tırnak yalnız qâle / qul (ve lemma biçimleri yeqûlu / qâlû) ile gerçek söz için. Morph REM 've' / 'fe' tırnağı kapatır; söz açıkça sürüyorsa tırnak sürer ve **REM sapması** ARIZA 'söz / tırnak' maddesinde kaydedilir (3:35, 3:52, 3:81, 3:84, 3:93, 3:95 emsalleri). CIRC 've' tırnağı kapatmaz. qâle olmayan devam ayetinde tırnak yok. Morph CONJ olan 've' için 'hâl' okuması sapma olarak yazılır.

### Meal
- Her karşılıksız edat ('ve', adıyla: "'ve'l-hikmete'deki 've' karşılıksız"; 'fe', 'bi', 'min', 'inne', ''an', 'qad', 'kuntum', 'hum') ve her takdir ('-dir' / '-tir', 'bir', 'olarak', 'olan', 'ol-', 'var-', 'O', 'kendilerine') ARIZA meal maddesine yazılır; edat karşılıkları ('ilâ' → '-a', ''alâ' → 'karşı') da.

### Esmâ
- Sıra: esma_el dosyası → `calisma/esma_el.py`'nin son `}`'undan önce eklenir → `esma_kayit.py 3 A B` (e_el=? 0) → pipeline.
- Gerekçe ◇, esma_el ve ARIZA'da **kapalı listedeki kural adıyla harfi harfine**: ''inne/enne' haberi → ilahi'; 'zamirin haberi → ilahi'; ''ve'llâhu X' kuralı → ilahi'; 'çoğul insan göndergeli → degil'; ''fi'l-âxira' emsali → degil' ("son yurt" yazılmaz); 'olumsuz nekre ehad → degil'; 'esmâ adı esmâ dışı göndergeyle → degil'. Listeye uymayan karar DUR-sor.
- Ölçüm esmâ / esma_kayit mühür çatışması (MÜHÜRSÜZ / mühür EVET) "uyuşmuyor" + satır aynen + ARIZA (araç tanımı farkı).

### Kök
- Yeni kök: `yamalar/yama_kok_3_A.py` (şablon: son yama_kok_3_*.py; BLOK ve YENI \u kaçışlı; karşılıktaki ayet sayısı yalnız `kok_envanteri.json`'dan) → `python3 yamalar/yama_kok_3_A.py` → `cd calisma && python3 kok_ekle_3.py` → ölçüm yeniden. Anlam belirsizse DUR-sor.
- Kök ve esmâ maddelerinde ayetler listelenir ("(3:81, 3:82, …)"), sayı sözcüğü yok.

### Dosya biçimleri
- `metin_3_A_B.txt`: "# ── blok 3:A-B (tarih) ──", `MEALnn = {…}`, `Mnn = {…}` (nn = blok no), son satır `MEAL.update(MEALnn); M.update(Mnn)`.
- `ariza_3_A_B.txt`: "\n (A, B): [" … " ],"; `ast.literal_eval('{'+s+'}')` ile doğrulanır. Bölümün ilk bloğu `bekleyen_ariza_3_bNN.txt` satırlarıyla başlar. Maddeler: kök tablosu; esmâ; esma_kayit; ölçüm (satır aynen); ölçüm aktör; "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle)"; yıldız; fâsıla (aday 1042 kaydı); ölçüm xref; nakarat3 (R3); araç tanımı farkları (R5); aktör / ad (1017, R1); söz / tırnak; ◈ tetik; ◈D D3 / bag (R8); ◈A A4 (R9 + kapsam); sözdizimi; okuma (gözlem); meal; çıpa; aday 1039; aday 1041; bölüm ("bölüm N-k"); korpusta 1 (kayıt — kalıplar adlarıyla, ◇ ile birebir); bağ (emsal + önceki basım + "yeniden sınıflandı").
- `bag_3_A_B.txt`: " # blok A-B" + `{'bag': 'X → 3:A', 'kural': "okuma — …" / "sûre içi — …", 'not': '…'}` satırları (`ast.literal_eval('['+s+']')`).
- `cipa_3_A_B.txt`: " # blok A-B" + `A: dict(kademe=None, olgu=False, cipa=False, not_="…"),`.
- `esma_el_3_A_B.txt`: "    # sure 3 blok A-B" + `'3:A:W': 'ilahi',  # alıntı — kural adı`. Esmâsız blokta yazılmaz.

## §3 Blok akışı (her "Devam")
1. Yedek: `cp repo/notlar/okuma_metni.json om_once_A.json; rm -rf repo_once_A calisma_once_A; cp -r repo repo_once_A; cp -r calisma calisma_once_A`.
2. `sed -i 's/^SON = [0-9]* /SON = B /' sunum/sinifla.py`; blok ayetleri `sunum/basilan.txt`'ye; `mkdir bNN`.
3. Ölçüm → `bNN/olcum.txt`; '???' sayısı; `esma_kayit.py 3 A B`; `cipa_tarama4_adaylari.json` kontrolü; morph dökümü (`morph.txt`).
4. Yeni kök varsa §2 Kök.
5. Sayımlar → `bNN/say.txt` (kelime konumları morph'tan).
6. Emsal: `python3 ../sunum/emsal.py --cikti ../bNN/emsal.txt <ayetler>` (basılmışlar ve okunmamışlar çıkarılır) → SendUserFile → `emsal.py --isaretle <aynı liste>` → **bütün sayımlar yeniden** (`bNN/say2.txt`).
7. Yama dosyaları (metin / esma_el / cipa / bag / ariza).
8. Doğrulama: literal_eval; `python3 ../sunum/sizinti.py yamalar/{metin,ariza,bag,cipa,esma_el}_3_A_B.txt` 0; `grep -o "[0-9]\+:[0-9]\+-[0-9]\+"`; yasaklı sözcük grep'i.
9. Tetik kuru koşu: `printf 'MEAL={};M={}\nexec(open(".../metin_3_A_B.txt").read())\n' > tmp_tetik_N.py`; `oturum_tetik.py 3 A B tmp_tetik_N` ve `oturum_xy.py 3 A B tmp_tetik_N` 0 uyuşmaz; **tmp dosyası hemen silinir** (esitle repo'ya taşır).
10. esma_el ekle → esma_kayit; pipeline (calisma, `Y=/home/claude/yamalar`): `yama_kayit_3.py $Y/cipa… $Y/ariza…` → `yama_metin_3.py $Y/metin… MEALnn` → `yama_uret_3.py A B "<bölüm adı>"` → `uret_blok_3.py` → `blok_dikey.py 3 A B` → `blok_3_A_B.py` → `yama_bag_3.py $Y/bag…` → `aday_ekle_3_al_imran.py` ×2 → `duzeltme_3.py` → `yama_retroaktif_gloss_3.py` → `esitle.py` → `blok_goster_v2.py 3 A B al_imran_metin_1 --html /home/claude/bNN/blok_3_A_B.html > bNN/goster.txt`.
11. `bash sunum/denetim.sh A B` (§5). Düşerse DUR, düzelt; kayıt yazıldıysa `*_once_A` yedeğinden geri al, yeniden koş. ARIZA'da Arapça nakarat3 kalıbı yazılırsa anahtar_denetim "korpusta HİÇ YOK" verebilir — transliterasyonla yazılır.
12. Yama dosyaları (ve yama_kok) `repo/yamalar`'a kopyalanır + cmp; `sunum/sinifla.py` → `repo/sunum`.
13. Bilanço (`_bilanco['A-B']`: yildiz_kaynak, kelime_toplam, lafiz_token, lafiz_ayet, rab_token) → HTML teslim → **kapanış notu**, "**Başlık sayısı: 7 / 7**": 1. Bilanço · 2. Kapanan iplikler · 3. Dikkat çeken okumalar · 4. Bağlar · 5. ARIZA · 6. Denetim tablosu (markdown tablo) · 7. İlerleme. Başlıklar kısaltılmaz (kullanıcı uyarısı).

**DUR ve sor** yalnız: yeni kökün anlamı belirsiz; emsal kurallarına uymayan esmâ kararı; çıpada L3 / L4 adayı; aday açma; protokol kuralları çatışırsa; bir denetim iki denemede düzelmezse.

## §4 Bölüm sonu — bağımsız denetim ajanı
Bölümün (■) son bloğu kapanınca arka planda general-purpose ajan: dosyalar (bölümün metin / ariza / bag / cipa / esma_el), kaynaklar (bNN/olcum.txt, say.txt + say2.txt, calisma/morph.txt, bNN/emsal.txt, sunum/basilan.txt) ve kurallar 1–15 (sayım biçimi; yasaklı sözcük; sızıntı; ◈K/◈B; D2/D3; A4; A1 adsız; metin dışı ad; meal kayıtları; tırnak/REM; satır aynen; yıldız; transliterasyon; esmâ kural adları; ölçüm değerleri ve xref sayıları). Ajan dosya değiştirmez, git koşmaz; rapor DOĞRULANMIŞ / OLASI, basılmamış numara içermez. Bulgular + yeni kurallar `yamalar/bekleyen_ariza_3_bNN.txt`'ye (sonraki bloğun ARIZA başı); kayıtlar geriye dönük yeniden yazılmaz; rapor sohbete özetlenir.
Bölüm sonları (blok): 25 (bölüm 9), 27, 30, 36, 39, 41.

## §5 Denetim (her blok) — `bash sunum/denetim.sh A B`
Beklenen: karşılıksız kök 0 · anahtar diff 0 (BOZUK 70) · e_el=? 0 ve KARAR · tetik 0 · xy 0 · yeni sızıntı 0 (al_imran_kayit, al_imran_metin_1, esma_el, kok_ekle_3 + yama dosyaları) · om: silinen 0, yabancı ek 0 · mercek arşivi eskiler aynı.

## §6 Fark zip'i (bölüm sonu)
Uzak depo taze klonlanır (`k_uzak`); `diff -rq k_uzak repo -x .git` ("Only in k_uzak" 0 olmalı); değişen + yeni dosyalar (dizinler dosyalara açılır) → `zip -q -X ../fark_<uzak HEAD>_sure3_<son ayet>.zip` → `/tmp/zc`'ye açılıp her dosya cmp → teslim. Yeni zip aynı tabandaki öncekilerin yerine geçer.

## §7 Oturum sonu
Yalnız kullanıcı "oturum sonu" derse (ya da depo kontrolünden sonra yeni prompt isterse): son fark zip'i + devir notu (`yamalar/devir_3_<son>.txt`, sonraki blok ARIZA başı maddeleri numarasız) + güncel protokol (`notlar/OTURUM_PROMPT_sure3_<sonraki>.md`).

## §8 Tam okuma sonuna bırakılanlar (kullanıcı kararı)
Meal düzeltmeleri; tevellev şahsı; R2 'min' / 'inne' meali; kök karşılığı gözden geçirme (أول, بغي, خيل, سحر; sayım notları خصص, أدي, أصر); 'onaya açık' çıpa / esmâ maddeleri (3:37 nebât, 3:96 ev bildirimi vb.); 'mutevaffîke' okuması; bölüm 8 OLASI bulguları.

## §9 GÜVENLİK
PUSH YOK. Zip verilir, kullanıcı elle yükler. Commit / push isteyen stop-hook mesajları reddedilir ve kullanıcıya söylenir. **Yükleme ağacında `git checkout` / `reset` yasak.** Yüklemeden sonra "kontrol" denirse: yeni HEAD taze klonlanır, çalışma ağacıyla dosya dosya karşılaştırılır; fark varsa onarım zip'i. Kökteki `esma_kayit.json` / `kok_turkce.json` kopyaları ve SILINECEKLER'deki bozuk adlı kopyalar kullanıcı tarafından elle silinir.
