# OTURUM PROTOKOLÜ — sûre 6 (En'âm): blok 32'den devam (SESSİZ OKUMA kipi)
Depo: github.com/sebahattintanas/claude_kuran_okuma · taban = **29b80e0** (sûre 6 bölüm 15 kapanışı) + bu protokolü, devir notunu (`yamalar/devir_6_135.txt`) ve `sunum/yardimci/` betiklerini taşıyan commit (HEAD). Kurulumda: taze klon → `git log --oneline 29b80e0..HEAD` yalnız bu oturum sonu commit'ini göstermeli; başka commit varsa DUR ve sor.

**Bu protokol `notlar/OTURUM_PROMPT_sure6_1.md`'nin devamıdır.** §1 (kip), §2 (kurallar), §4 (bölüm sonu ajanı), §5 (denetim), §8 (tam okuma sonu), §9 (GÜVENLİK) o dosyada olduğu gibi geçerlidir; aşağıdaki bölümler onu günceller ve önceliklidir.

## Durum (2026-11-23)
- Sûre 1–5 ve 9–114 TAM; sûre 6'da bloklar 1–31 okundu (bölümler 1–15 kapandı); sûre 7–8 okunmamış.
- Okunan 5925 / 6236 (%95,0) · `sunum/basilan.txt` 298 satır · esmâ KARAR 1294 · AS_enam 77 · mutasyon_sina 333 / 333 · anahtar denetimi BOZUK 70 (taban).
- `sunum/bolum4_kurallar.py` … `sunum/bolum31_kurallar.py` yürürlükte; bolum31 (bölüm 15 denetimi) blok 32'de ilk kez ARIZA'da koşar.
- Sıra: blok 32 (bölüm 16 'Ekinlerde ve hayvanlarda pay; sekiz eş' açılışı) → … → blok 40 → sûre 6 kapanışı (kullanıcıyla) → sûre 7–8. Blok aralıkları yalnız `yamalar/blok_plani_6.txt`'ten okunur; basılmamış aralık sohbete yazılmaz.
- Devir: `yamalar/devir_6_135.txt` (onaya açık kararlar, açık soru). `yamalar/bekleyen_ariza_6_b31.txt` blok 32 ARIZA'sının başına BEK olarak (bayt eşit) girer.

## Kullanıcı kararları (değişmez)
- "Yorum / meal sorularını oturum ortasında sorma, kayda yaz; basılmamış ayet numarasını hiçbir yere (sohbet dahil) yazma."
- Her "Devam" = bir plan bloğu; blok sonunda commit + push (main) ve SendUserFile (display attach): emsal md + blok HTML.
- Kapanış notu 7 başlık (Bilanço · Kapanan iplikler · Dikkat çeken okumalar · Bağlar · ARIZA · Denetim tablosu (markdown tablo) · İlerleme), son satır "Başlık sayısı: 7 / 7 — toplam ilerleme N ayet (%X)".
- Oturumlar arası basım (varsayılan, onaya açık): önceki oturumda basılanlar (`sunum/basilan.txt`) basılmış sayılır — dosya BOŞALTILMAZ (sûre 6 kayıtları ve BEK bu numaraları taşıyor).

## §0 Kurulum (OTURUM_PROMPT_sure6_1.md §0'dan farklar)
- `basilan.txt` repo'daki hâliyle kullanılır (298 satır); `sunum/sinifla.py` `SON = 135`.
- Blok dizinleri geri yüklenir: `for d in repo/oturum/sure6_bloklar/b*; do cp -r $d /home/claude/; done` (b01…b31: morph.txt, morph6.txt, olcum.txt, say.sh, say2.txt, ems.txt, emsal*.md, yap/*.py). ARIZA üreticisi b01…bNN `yap/karar.py` dosyalarını sırayla yükler — eksik blok dizini kararları düşürür.
- `/home/claude/say.sh` ← `repo/sunum/say.sh`; `sunum/yardimci/` (bu oturumda eklendi) `/home/claude/sunum/yardimci/`'ye gelir:
  - `ariza_ozet.py <ariza_yap çıktısı>` — HATA satırlarını tekilleştirip 'TOPLAM N' verir;
  - `morph_kelime.py bNN/morph6.txt bNN/morph.txt` — segment morph'unu kelime satırına çevirir;
  - `say_uret.py NN "a:i-j,k-l" … --dizi "6 a i j" …` — say.sh üretir;
  - `say_temiz.py NN` — say2/say.sh tekrar ve tam n==1 / --on n≠1 temizliği;
  - `say_kontrol.py bNN/say2.txt` — tekrar anahtar denetimi;
  - `metin_kuyruk_b31.py` — metin_yap kuyruğu şablonu (`sed`: 6:131-135 → blok aralığı, MEAL31/M31 → MEALNN/MNN, range, dosya adı).

## §3 Blok akışı (bu oturumda uygulanan; OTURUM_PROMPT_sure6_1.md §3'ü günceller)
1. `cp repo/notlar/okuma_metni.json om_once_A.json`; blok ayetleri `sunum/basilan.txt`'ye; `sed -i 's/^SON = [0-9]* /SON = B /' sunum/sinifla.py`; `mkdir -p bNN/yap`.
2. Ölçüm (calisma): `python3 -c "import olcum_bicim as o; print(o.olcum(6,a))"` ayet ayet, boş satırla → `bNN/olcum.txt`. Morph: `grep -E "^6:(a…):" calisma/morph.txt > bNN/morph6.txt; python3 sunum/yardimci/morph_kelime.py bNN/morph6.txt bNN/morph.txt`; `python3 sunum/lem_bozuk.py NN`.
3. Emsal: ölçüm xref adayları basılmamış ve okunmuşsa ön sayımla (`run say 6:a i-j` harekesiz) yoklanır; **emsal yalnız harekesiz `say` anahtarıyla bulunan xref'tir** (yalnız `dizi` ile bulunan alınmaz — bolum14 k3 / bolum17 k1 çatışır). `python3 sunum/emsal.py --cikti bNN/emsal.txt X …`; `cp bNN/emsal.txt bNN/emsal_6_A_B.md`; `bNN/ems.txt`; `python3 sunum/emsal.py --isaretle X …` — **say koşusundan ÖNCE**.
4. Meal ve `yap/seg.py` (kesimler); kesim Arapçası ◇'nin alt dizesi (vakfta pausal biçim ◇'de de).
5. `python3 sunum/yardimci/say_uret.py NN …` (kesimler + nakarat3 / emsal `dizi` satırları); calisma'dan `(timeout 3000 bash ../bNN/say.sh > ../bNN/say2.txt 2>&1; echo FIN >> ../bNN/say2.txt) &`; bitince FIN satırı silinir.
6. Medde: `(echo ". /home/claude/say.sh"; python3 sunum/medde.py bNN/say2.txt --komut) > /tmp/mdNN.sh`, calisma'da koş, çıktı say2'ye, run satırları say.sh'ye; `python3 sunum/yardimci/say_temiz.py NN`; `say_kontrol.py`.
7. Yama dosyaları: `yamalar/{esma_el,cipa,bag}_6_A_B.txt` (esma_el → `calisma/esma_el_ekle.py`, sonra `esma_kayit.py 6 A B`; `python3 sunum/esma_muhur.py A B NN`); `yap/metin_body.py` + kuyruk → `metin_yap.py` → `yamalar/metin_6_A_B.txt`; `yap/I_head.py`, `yap/I_body.py`, `yap/karar.py`, `yap/karar_meal.py`, `yap/kur.py`.
8. `python3 bNN/yap/kur.py && timeout 590 python3 bNN/yap/ariza_yap.py > /tmp/aNN.txt; python3 sunum/yardimci/ariza_ozet.py /tmp/aNN.txt` — TOPLAM 0 **iki ardışık koşuda** (ilk koşuda grup başlıkları eksik görünebilir).
9. Ek denetimler (/home/claude'dan): translit_kontrol, kelime_kontrol, kural13, kural14, kontrol, altdize, ayn_kontrol (`A B NN`); sizinti, satir_aynen_kontrol, satir_aynen_tam (`bNN/olcum.txt $F`), yasakli.sh $F, yasakli_sina.sh; tetik / xy kuru koşusu (calisma: `(echo "MEAL={};M={}"; cat ../yamalar/metin_6_A_B.txt) > tmp_mNN.py`, `oturum_tetik.py 6 A B tmp_mNN`, `oturum_xy.py …`, `rm tmp_mNN.py`).
10. Hat (calisma, `Y=/home/claude/yamalar`): `esma_kayit.py 6 A B` → `$Y/yama_kayit_6.py $Y/cipa_6_A_B.txt $Y/ariza_6_A_B.txt` (idempotent değil — bir kez) → `$Y/yama_metin_6.py $Y/metin_6_A_B.txt MEALNN` → `$Y/yama_uret_6.py A B "<bölüm adı>"` → `uret_blok_6.py` → `blok_dikey.py 6 A B` → `blok_6_A_B.py` → `$Y/yama_bag_6.py $Y/bag_6_A_B.txt` → `aday_ekle_6_enam.py` ×2 → `duzeltme_6.py` → `yama_retroaktif_gloss_6.py` → `esitle.py` → `blok_goster_v2.py 6 A B enam_metin_1 --html /home/claude/bNN/blok_6_A_B.html > ../bNN/goster.txt`.
11. `timeout 900 bash sunum/denetim_6.sh A B NN` (BOZUK 70).
12. Commit: değişen `sunum/*` cmp döngüsüyle repo'ya; beş yama dosyası `repo/yamalar/`; `tar --exclude='*.html' --exclude=__pycache__ --exclude=goster.txt -cf - bNN | tar -xf - -C repo/oturum/sure6_bloklar/`; okuma_metni sıkıştırma; commit (atıf satırları) → `git -c push.negotiate=true push -q origin main`.
13. SendUserFile (emsal md + blok HTML, attach) → 7 başlıklı not.

### kur.py türetme
- **Bölüm açılış bloğu (blok 32 dahil):** `b29/yap/kur.py`'den türetilir — BEK satırı `bekleyen_ariza_6_b31.txt`; GERI `geriye_donuk_6_b31k.txt`; BOL bölüm adı; `range(7, 31)` → `range(7, 32)`; `B6 … B30` açma satırına ve `print` listesine `B31`; `'B30_HEPSI'` yanına `'B31_HEPSI'`; `for nn in (…)` listesi bloğa kadar; R5, VF, `_ON`, aralık ve `bNN` yolları bloğa göre; I_body öz denetim maddesine `sunum/bolum31_kurallar.py A B NN → B31_HEPSI`.
- **Bölüm içi blok:** son bloğun kur.py'sinden, BEK satırı olmadan, `I_body.py` `I = [` ile.

## Bu oturumda öğrenilen kurallar (araç yakalar; yazarken uy)
- **Emsal meal kararı:** 'çakışma değil' yalnız iki alıntı bayt eşitse; değilse 'çakışma — tam okuma sonu (…)'. Kalıpta seg fiil öğesi varsa emsal alıntısı fiil karşılığının ilk üç harfini içermeli — yoksa fiilsiz bir sayım anahtarıyla bağ kurulur (blok 31: ''alâ mekânetikum'). Karar alıntısı sayım etiketinin alt dizesi, ◇'deki ilk geçişi sayım aralığında. Önek karşılığı alıntıdan düşürülmez ('ve sizi …'). Yalnız büyük harf farkı → 'çakışma değil' (bolum31 k3).
- **Ortak lemma dizisi:** emsalle en uzun ortak dizi için `dizi 6 a i j` koşulur, ◇'de anılır; bolum31 k5 ile bag kaydında da anılmalı.
- **Lemma adları:** önceki bloklardaki ad korunur (bolum12 k4: 'şa'ara', 'haşera', 'enzere', 'resûl', 'qâle', 'zâ', 'âye'); nakarat3 adı ölçüm kalıbı iskeletine uymalı (bolum7 k13) — çatışırsa nakarat3 / R5 adı ölçüm biçimiyle, dizi adı önceki adla, ikisi de lemma adları listesinde. ث = 's' ('steksertum', 'istekser'). Wasl sonrası ◇ belirteci kelime sayımını bozuyorsa ayrı yazılır ('yâ qavmi 'melû').
- **A1:** fiil + zamirsiz NOM ad → 'N. kelime — fail M. kelime' (bolum16 k1); fail gizli zamirse "(gizli zamir, adsız; N. kelime — fail N. kelime içi gizli zamir, …)" — '(adsız;' ile başlayan parantezde 'fail N.' yasak (bolum21 k5). Söz aralığındaki 1./2. şahıs 'söz içi'; 2. şahıs etiketi 'muhatap'; edilgen 2MP/3MP 'naib-i faili'. Alıntı ◇ alt dizesi ve ◇ konumuyla eş (bolum8 k14; 'li'l-' gibi önekli yazım).
- **A3 / A4:** söz fiili yoksa A3'e yazılmaz (nidâ ayrı kayıt; bolum31 k4 A4 'nidâ'); A3 'söz biçimli içerik' ile A4 'söz açılır/kapanır' birlikte olmaz (bolum14 k4); ayet sonunda biten söz için A4 'söz kapanır (N. kelime, ayet içi)'. Şart: "şart → cevap (ayet içi; COND 'x' N. kelime: 'x' / 'y' (M. kelime))" COND sayısı kadar. Şahıs geçişi ölçüm 'baskın'la; toplamlar baskınla çelişirse 'şahıs sayısında beraberlik (…)' — yalnız gerçekten berabereyse (bolum31 k1). Edim geçişi hedefi D2 ile bayt eş (bolum31 k2).
- **Meal öğeleri:** '-dir/-dır' takdiri her kelime için ayrı öğe; ek öğesi içerici kelimenin alt dizesi ('-tıkları' / 'yaptıklarından'); nekre "(N. kelime; nekre — …" hemen numaradan sonra; yönelme / belirtme eki 'fiil yönetimi takdiri'; edat başlığı tanınmıyorsa ad biçimi ("'nere' 'haysu' karşılığı …") ya da `sunum/edat_etiket.py` EDLEM eki (araç değişikliği gerekçesiyle).
- **Kararlar:** grup başlığı eksik / üye değişince `yap/karar.py`'de güncel üye listesiyle yeniden yazılır (KÖK grupları dahil); `karar_meal.py` KQ (eş edat) / KM (es_lemma satırı, anahtar bayt eş) — önceki yön korunur (ARIZA 'yön değiştirdi' hatası); 'bağlam' gerekçeli kararlar 'tam okuma sonu' (bolum22 k5). Bir KM anahtarı iki lemmaya düşerse (örn. 'ba'd') karar metni kümedeki karşılıkla başlar.
- **Esmâ:** kural adı bolum6 KAPALI listesinden; 'ilahi' kararlı lemmada çerçeve etiketleri bolum19 CERCEVE (blok 30'da 'tamlama içinde ad, göndergesi Allah' eklendi); 'degil' / 'ilahi' ayrılığında esmâ maddesi bütün 'degil' kayıtlarını konumla anar; ADJ ardışık haber parantezi önceki emsalle; ◇ mühür farkı parantezi 'muhur_el ' ile başlar; ÇİFT mühürde ARIZA esma_kayit maddesi 'ÇİFT' anar.
- **Medde:** FARK VAR anahtarı ◇'de "(--medde N ayet: 'X' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı)" ile; medde listesindeki basılmış eş ARIZA D3 dışı maddesine ('say … --medde' X). Tam elif / hançer elif farkı medde taramasına girmez (elle: RASM_ELIF_ESI).
- **Ölçüm xref cümlesi:** basılmış / emsal adlarıyla, okunmuş ve okunmamış sayı ile ('okunmuş N ayet ve okunmamış M ayet'); her ayet ayrı ('6:a xref yok; 6:b xref yok').
- **Tetik dışı kökler** I_head ANILIS: "6:a kök X ('kelime' N. kelime — anlam), …: tetik listesinde yok".
- **Yasaklı** (sohbet dahil özen): aynı, tek, ilk, ikinci, birer, peygamber (yerine 'nebi'), 'X ayette', 'önceki ayetin' kalıbı; 'te'kîdli' gibi kesmeli Türkçe sözcükler alıntı ayrıştırmasını bozar.

## §4 ek — bölüm sonu
Bölümün son bloğu commit'lendikten sonra: salt-okur bağımsız ajan → `yamalar/bekleyen_ariza_6_bNN.txt` (tam 2 öğe; yalnız basılmış numara; yasaklı-temiz) → `sunum/bolumMM_kurallar.py` (5 betik kuralı + elle listesi; MM = bölüm + 16) → `mutasyon_sina.py` var6 sınamaları (her kural için isabetli + isabetsiz) → `geriye_donuk.py` isa satırı ve 'bas' başlığı → `python3 sunum/geriye_donuk.py bNNk yamalar/geriye_donuk_6_b<önceki>k.txt` → `bolum19_kurallar.py` KURAL_ATIF → commit.

## §7 Oturum sonu
Kullanıcı yeni oturum isterse: `yamalar/devir_6_<son>.txt` + `notlar/OTURUM_PROMPT_sure6_b<sonraki blok>.md` + gerekirse `sunum/yardimci/` güncellemesi, commit + push.
