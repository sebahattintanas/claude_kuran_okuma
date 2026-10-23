# -*- coding: utf-8 -*-
"""hasr_kayit.py — sûre 59 (Haşr) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 59

CIPA = {
 # blok 1-5
 1: dict(kademe='L0', olgu=True, cipa=False, not_="'sebbaha lillâhi mâ fi's-semâvâti ve mâ fi'l-ard' — gökler ve yer tesbih edenlerin yeri olarak adlanıyor; süreç / ölçü yok — L0 (57:1 emsali); tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'ve lehum fi'l-âhirati azâbu'n-nâr' — âhiret ateşi; doğal olgu değil; tarayıcı v4 adayı, çıpa değil"),
 5: dict(kademe='L0', olgu=True, cipa=False, not_="'lîne … qâ'imeten alâ usûlihâ' — hurma ağacı kökü üzerinde ayakta; doğal nesne adlanıyor, eylem insanın (kesme / bırakma), doğa süreci / ölçü yok — L0; tarayıcı vermedi"),
 # blok 6-10
 6: dict(kademe='L0', olgu=True, cipa=False, not_="'min haylin ve lâ rikâb' — atlar ve binekler adlanıyor (koşturulmadıkları söyleniyor); süreç / ölçü yok — L0; tarayıcı vermedi"),
 # blok 11-17
 17: dict(kademe=None, olgu=False, cipa=False, not_="'fi'n-nâri hâlideyni fîhâ' — ateş, âhiret; doğal olgu değil; tarayıcı vermedi"),
 # blok 18-24
 20: dict(kademe=None, olgu=False, cipa=False, not_="'ashâbu'n-nâri ve ashâbu'l-cenne' — ateş ve cennet, âhiret; doğal olgu değil; tarayıcı vermedi"),
 21: dict(kademe='L0', olgu=True, cipa=False, not_="'lev enzelnâ hâze'l-qur'âne alâ cebelin … hâşi'an mutesaddi'an' — dağ adlanıyor; varsayım ('lev') içinde, yarılma doğa süreci olarak değil Kur'an'a tepki olarak anılıyor — süreç / ölçü yok, L0; teşbih / mesel çerçevesi (48:29, 57:20 ailesinden ayrı: orada doğa süreci var, burada yok); tarayıcı v4 adayı, çıpa değil"),
 24: dict(kademe='L0', olgu=True, cipa=False, not_="'yusebbihu lehû mâ fi's-semâvâti ve'l-ard' — gökler ve yer tesbih edenlerin yeri olarak adlanıyor; süreç / ölçü yok — L0 (59:1 emsali); tarayıcı vermedi"),
}

ARIZA = {
 (1, 5): [
  "esmâ: e_oto 5 token (59:1×2, 59:2×2, 59:3); okuyucu kararı 59:1 'azîz', 'hakîm' İLÂHÎ (zamir 'huve'nin haberi); 59:2 'evvel' (sürgünün ilki), 'mu'minîn' (çoğul inananlar), 59:3 'âhira' (âhiret) DEĞİL; KARAR 533 → 538; bilanço geçerli mühür yalnız 59:1",
  "esmâ ayrışması: esma_kayit 'mühür EVET' 59:2 ve 59:3 için (ölçüm satırı ikisinde 'MÜHÜRSÜZ'), karar sonrası geçersiz — mühür iddiası yalnız bilançodan (aday 1022 ailesi)",
  "harf alanı: ayet 1 ölçümünde harf 61 → harf3 41, isaret 0 (56:1, 57:1, 58:1 ailesi); 59:2-5'te fark = isaret (10, 1, 3, 0) — sûre başı besmele harfleri 'harf' alanına giriyor olabilir; araç alanı, metin hakkında kanıt değil (aday 924); araç donuk, KAPATILAMAZ",
  "gloss (1021 ailesi): kök لين tablosu 'yumuşaklık' — 59:5 'lîne' (hurma ağacı) anlamı ayrı yazılmıyor",
  "kök tablosu: خرب ve جلو bu blokta eklendi (kok_ekle_59; 1419 → 1421); retroaktif yama 0 (yeni kök taşıyan okunmuş 3 ayet, karşılıksız anma yok)",
  "adsız (aday 1017): 59:2 çıkarılanlar ('ellezîne keferû min ehli'l-kitâb'), yurt, kaleler adsız; 59:2 ve 59:5 muhatap 2MP adsız; 59:4 elçi adsız — ad verilmedi",
  "aday 1040 alanı (kayıt, test yok): 58:22 → 59:1 — grup adıyla ('hizbu'llâh … el-mufluhûn') kapanış / tesbihle açılış, lafız 2. kelimede; fâsıla ن → م",
  "aday 1041 alanı (kayıt, test yok): lemma 'evvel' 57:3 Allah / 59:2 toplanmanın ilki; lemma 'âhir' 57:3 Allah / 59:3 âhiret; lemma 'mu'min' 59:2 çoğul inananlar / sûre içi 59:23 henüz okunmadı",
  "karşıt çift (aday 1039, okuma): 59:1 gökler / yer; 59:2 iki tarafın zannı, kendi elleri / inananların elleri, korunma sanısı / hesapta olmayan yerden geliş; 59:3 dünya / âhiret, sürgün / azap; 59:5 kesme / ayakta bırakma; 59:4 yok — kayıt, test yok",
  "yıldız: 59:2 ★★ n z=2,93 (40 kelime); 59:4 ★★★ allah z=4,47 (3 lafız / 12 kelime) — bloğun tek ★★★ ayeti; 59:1, 3, 5 yıldızsız",
  "kalıp: 'allâhe şedîdu'l-iqâb' harekesiz 8 ayet, okunmuş ayetlerde eşi yok — 59:4 okumadaki ilk görülüş; sûre içi eşi 59:7 henüz okunmadı",
  "sûre içi kalıp eşleri henüz okunmadı: 59:1 → 59:24 ('ve huve'l-azîzu'l-hakîm', nakarat3 GEÇER), 59:2 → 59:11 ('ellezîne keferû min ehli'l-kitâb', nakarat3 GEÇER), 59:4 → 59:7 ('şedîdu'l-iqâb', nakarat3 GEÇMEZ) — okuma eşin bloğunda",
  "çıpa: 59:1 L0 (gökler / yer adı), 59:5 L0 (ağaç kökü üzerinde, eylem insanın); 59:3 âhiret, olgu değil (tarayıcı v4 adayı); 59:2 kaleler / evler insan yapımı, olgu değil; L4 yok",
  "okuma: 57:1, 58:22 → 59:1; 50:44, 57:3, 39:47, 16:26, 33:26, 24:44 → 59:2; 58:21, 24:23, 57:3 → 59:3; 59:3, 16:27, 47:32 → 59:4; 14:24, 16:27, 59:4 → 59:5 — KAPATILAMAZ",
  "tetik: ön kuru koşu 2 tetik satırı (59:1 K, 59:2 B) — kayıtta 0 uyuşmaz; [x/y] 0 (50 sayım)",
 ],
 (6, 10): [
  "esmâ: e_oto 4 token (59:6 'qadîr', 59:7 'ağniyâ'', 59:10 'ra'ûf', 'rahîm'); 'qadîr' (lafzın haberi), 'ra'ûf', 'rahîm' (Rab hitabının haberi) İLÂHÎ; 'ağniyâ'' (çoğul zenginler) DEĞİL; KARAR 538 → 542; bilanço geçerli mühür 59:6, 59:10",
  "esmâ ayrışması: ölçüm satırı 59:6 'qadîr' için 'MÜHÜRSÜZ', bilanço geçerli mühür (58:6, 58:7 emsali) — mühür iddiası yalnız bilançodan (aday 1022 ailesi)",
  "morph etiketi (924, 517 ailesi): 59:9:2 'tebevve'û' IMPV 2MP etiketli — ölçüm satırı 'edim emir, IMPV 1, 2MP 2', sahset ['2', '3'] bu etiketten; okumada mevsûl sılası, 3MP geçmiş. Araç alanı, metin hakkında kanıt değil; araç donuk, KAPATILAMAZ",
  "gloss (1021 ailesi): kök خيل tablosu 'hayal, gözde canlanma' — 59:6 'hayl' (atlar) anlamı ayrı yazılmıyor",
  "lemma (1021 ailesi): morph lemması 'ğıll' (kin) 'ağlâl' (zincirler) çoğulunu da kapsıyor — lemma sayımı (9 ayet) iki anlamı karıştırıyor; kök tablosu ikisini ayrı yazıyor",
  "kök tablosu: وجف, دول, خصص bu blokta eklendi (kok_ekle_59; 1421 → 1424); retroaktif yama 0 (yeni kök taşıyan okunmuş 7 ayet, karşılıksız anma yok)",
  "adsız (aday 1017): 59:6-7 elçi adsız; 59:7 kasabalar adsız (aktör adsız karye); 59:8 muhâcirler, 59:9 yurda ve imana yerleşmiş olanlar, 59:10 sonra gelenler — üç grup sınıf olarak, ad verilmedi; yurt adsız ('ed-dâr')",
  "alıntı (1017 alanı): 59:10 iç söz 1P dua ('yeqûlûn' sonrası) — sahset 1/2/3, iltifât 0",
  "aday 1041 alanı (kayıt, test yok): lemma 'âthara' 12:91 özne Allah / 59:9 insanlar; lemma 'ğanî' esmâ listesinde / 59:7 zenginler",
  "karşıt çift (aday 1039, okuma): 59:6 sizin koşturmanız yok / Allah'ın musallat etmesi; 59:7 verdiği / men ettiği, alın / geri durun, zenginler / yetim-yoksul; 59:2 'ahrace' / 59:8 'uhricû' (çıkaran / çıkarılan, iki karşıt grup); 59:9 ihtiyaç duymama / darlık, kendine tercih / nefsin cimriliği; 59:10 sonra gelen / önce geçen, kin / kardeşlik — kayıt, test yok",
  "yıldız: 59:7 ★★ n z=2,61 (allah z=1,63 de eşikte); 59:6 ★ allah, 59:8 ★ allah (pas z=1,57 eşikte), 59:9 ★ n, 59:10 ★ rab — yıldızsız ayet yok",
  "lafız / Rab: 59:9 bloğun lafız ve Rab taşımayan tek ayeti; 59:10 Rab 2 token (vokatif), lafız yok",
  "kapanan sûre içi eşler: 59:4 → 59:7 ('şedîdu'l-iqâb'), 59:6 ↔ 59:7 ('mâ efâ'e'llâhu alâ rasûlih', nakarat3 GEÇER), 59:2 → 59:8 ('min diyârihim'; 'ahrace' / 'uhricû'); henüz okunmayan: 59:7 → 59:14 ('qarye'), 59:9 → 64:16, 59:10 → 59:16 (Rab)",
  "çıpa: 59:6 L0 (atlar, binekler adı, süreç yok); diğerleri değerlendirilmedi (doğal olgu yok); tarayıcı adayı yok; L4 yok",
  "okuma: 33:50, 16:8, 9:39 → 59:6; 12:109, 59:4, 59:6 → 59:7; 22:40, 48:29, 49:15, 59:2 → 59:8; 12:91, 2:5, 58:22, 59:8 → 59:9; 15:47, 16:7, 59:9 → 59:10 — KAPATILAMAZ",
  "tetik: ön kuru koşu 1 tetik satırı (59:10 B) — kayıtta 0 uyuşmaz; [x/y] 0 (72 sayım)",
 ],
 (11, 17): [
  "esmâ: e_oto 2 token (59:11 'ehad', 59:15 'qarîb'); ikisi DEĞİL ('hiç kimse'; 'yakın zamanda'); KARAR 542 → 544; bilanço geçerli mühür yok (esma_kayit 59:11 'mühür EVET', karar sonrası geçersiz)",
  "sayı işareti (aday 924): 59:11 'ehad' ('lâ nutî'u fîkum ehaden', hiç kimse) sayı işareti aldı — anlam sayı değil (58:22 'aşîre' emsali)",
  "kök tablosu: وبل bu blokta eklendi (kok_ekle_59; 1424 → 1425); retroaktif yama 0",
  "adsız (aday 1017): 59:11 münafıklar ve kardeşleri (sınıf), muhatap 2MS; 59:14 kasabalar (aktör adsız karye); 59:15 'ellezîne min qablihim qarîbâ' — ad verilmedi; 59:16 'el-insân' cins; tek adlı aktör şeytan (59:16)",
  "alıntı (1017 alanı): 59:11 iç söz 1P (münafıkların vaadi), 59:16 iç söz 2MS emir + 1S (şeytan) — iltifât 0",
  "aday 1041 alanı (kayıt, test yok): lemma 'qarîb' esmâ listesinde / 59:15 zaman yakınlığı; lemma 'ehad' esmâ adayı / 59:11 'hiç kimse'",
  "karşıt çift (aday 1039, okuma): 59:10 'ihvâninâ' / 59:11 'ihvânihim' (iki kardeşlik); 59:11 vaatler / 59:12 olumsuzlamalar; 59:9 / 59:13 'fî sudûrihim' (ihtiyaç duymama / korku); 59:14 'cemî'an' / 'şettâ'; 59:16 'ukfur' / 'innî berî'un minke'; 59:15, 59:17 yok — kayıt, test yok",
  "yıldız: 59:12 ★★ pas z=2,12 (3/7 edilgen); 59:11 ★ n; 59:13-17 yıldızsız",
  "lafız / Rab: lafız 3 ayette (59:11, 13, 16), Rab 1 (59:16, sûre içi son); 59:12, 14, 15, 17 lafızsız ve Rabsız",
  "kapanan sûre içi eşler: 59:2 → 59:11 ('ellezîne keferû min ehli'l-kitâb', nakarat3 GEÇER); 59:13 ↔ 59:14 ('zâlike bi-ennehum qavmun lâ', nakarat3 GEÇER); 59:2 → 59:14 (kök حصن); 59:7 → 59:14 (qarye); 59:3 → 59:17 (nâr); kök خرج ve شدد sûre içi son geçişleri bu blokta; henüz okunmayan: 59:15-16 → 59:21 (mesel), 59:17 → 59:20 (nâr)",
  "çıpa: 59:17 âhiret ateşi, olgu değil; 59:14 kasabalar / duvarlar insan yapımı; doğal olgu yok, tarayıcı adayı yok; L4 yok",
  "okuma: 58:14, 9:107, 59:2, 59:10 → 59:11; 48:22, 59:11 → 59:12; 9:6, 59:9 → 59:13; 20:53, 59:2, 59:7, 59:13 → 59:14; 59:15 → 59:16; 12:109, 59:3 → 59:17 — KAPATILAMAZ",
  "tetik: ön kuru koşu 3 tetik satırı (59:11 K, 59:14 B, 59:16 B) — kayıtta 0 uyuşmaz; [x/y] 0 (69 sayım)",
 ],
 (18, 24): [
  "esmâ: e_oto 17 token (59:18 'habîr'; 59:22 'âlim', 'rahmân', 'rahîm'; 59:23 'melik', 'quddûs', 'selâm', 'mu'min', 'muheymin', 'azîz', 'cebbâr', 'mutekebbir'; 59:24 'hâliq', 'bâri'', 'musavvir', 'azîz', 'hakîm'); hepsi İLÂHÎ; KARAR 544 → 561; bilanço geçerli mühür 59:18, 22, 23, 24",
  "esmâ ayrışması (1022 ailesi): ölçüm satırı 59:23'te altı ad gösteriyor (esma_kayit sekiz; 'quddûs', 'mutekebbir' ölçümde yok), 59:24'te dört ad ('musavvir' ölçümde yok); 59:23 ölçümde sekizi de 'ORTA, MÜHÜRSÜZ', bilanço geçerli mühür (son kelime 'yuşrikûn'); 59:18 'habîr' ölçümde 'SON, MÜHÜRSÜZ', ardından 'bimâ ta'melûn' (58:13 emsali) — mühür iddiası yalnız bilançodan, konum metinden",
  "GLOSS ÇAKIŞMASI (924 ailesi, araç açığı): kök همن (muheymin) eklenince yama_retroaktif_gloss_59 genel geçişi 28:6 olcum + mercek ve 28:8 olcum alanlarındaki nakarat2 dizgesinde Hâmân adının harekesiz iskeletini kök sandı ve 'muheymin' glossunu yapıştırdı (3 alan). gloss_gecis harekesiz iskelet ile kök anmasını ayırmıyor. Araç değiştirilmedi (dondurma); yama_haman_59.py yanlış glossu açıklama notuyla değiştirdi (idempotent; turkce_denetim 0 korunuyor). mercek_kayit.json'daki iki çıplak anma (28:6, 28_atlama) denetim dışı, dokunulmadı. Aynı risk başka özel ad iskeletleri için açık — KAPATILAMAZ, okuma sonu kararına",
  "kök tablosu: همن bu blokta eklendi (kok_ekle_59; 1425 → 1426); hedefli retroaktif yama 0, genel geçiş 3 (yukarıdaki çakışma)",
  "adsız (aday 1017): 59:18 inananlar ve 'nefs' (genel), 59:19 'ellezîne nesu'llâh', 59:20 ateşin ve cennetin halkı, 59:23 ortak koşanlar — sınıf, ad verilmedi; 59:21 muhatap 2MS adsız",
  "aday 1041 alanı (kayıt, test yok): lemma 'mu'min' aynı sûrede 59:2 inananlar (DEĞİL) / 59:23 Allah (İLÂHÎ) — 57:3 / 57:13 emsali; 'cebbâr' ve 'mutekebbir' 40:35 insan kalbi / 59:23 Allah; 'melik' 12:54 insan kral / 59:23 Allah; kök نسي 59:19 'nesû' (insan) / 'ensâhum' (Allah)",
  "aday 1040 alanı: sûre son ayeti 59:24 → 60:1 henüz okunmadı — sınır kaydı sûre 60'ın ilk bloğunda",
  "karşıt çift (aday 1039, okuma): 59:18 önden gönderilen / yarın; 59:19 Allah'ı unutma / kendini unutturulma; 59:20 ateşin / cennetin halkı, 59:19 'el-fâsiqûn' / 59:20 'el-fâ'izûn'; 59:21 dağın huşûsu / 59:13-14 anlamayan topluluk; 59:22 gayb / şehâde; 59:23 tek ilah / ortak koşulanlar; 59:24 gökler / yer — kayıt, test yok",
  "sûre halkası (okuma, KAPATILAMAZ): 59:1 'sebbaha … ve mâ fi'l-ard … ve huve'l-azîzu'l-hakîm' / 59:24 'yusebbihu … ve'l-ard, ve huve'l-azîzu'l-hakîm' — PERF → IMPF; nakarat3 GEÇER (ölçüm); kök سبح sûre içi 3 kez (59:1, 23, 24)",
  "yıldız: 59:18 ★★ allah z=3,00 (3 lafız / 17 kelime); 59:23 ★ allah; 59:19-22, 24 yıldızsız",
  "kapanan sûre içi eşler: 59:7 → 59:18 ('vettequ'llâh', nakarat3 GEÇER); 59:5 → 59:19 (fâsiq); 59:17 → 59:20 (nâr; نور [3/3]); 59:15-16 → 59:21 (mesel; مثل [3/3]); 59:22 ↔ 59:23 ('huve'llâhu'llezî lâ ilâhe illâ hu'); 59:1 → 59:24 ('ve huve'l-azîzu'l-hakîm'); 59:16 → 59:24 (kök برأ iki anlam); 59:2 → 59:23 (mu'min). Sûre içinde açık sûre içi eş kalmadı",
  "çıpa: 59:21 L0 (dağ, varsayım içinde; tarayıcı v4 adayı, çıpa değil), 59:24 L0 (gökler / yer); 59:20 âhiret; L4 yok",
  "okuma: 57:28, 24:53, 58:12, 59:7 → 59:18; 58:19, 9:67, 59:5 → 59:19; 9:20, 59:17, 59:19 → 59:20; 33:72, 29:43, 59:13, 59:14, 59:15, 59:16 → 59:21; 20:8, 13:9 → 59:22; 59:2, 59:22, 40:35, 12:54, 52:43 → 59:23; 59:1, 59:16, 20:8, 24:41 → 59:24 — KAPATILAMAZ",
  "tetik: ön kuru koşu 4 tetik satırı (59:21 K, B; 59:24 K, B) — kayıtta 0 uyuşmaz (ilk mercek taslağında 59:18 ◈K tetiksiz dolu yazılmıştı, kayıttan önce '—'); [x/y] 0 (67 sayım)",
  "kendi kaydı (kayıttan önce düzeltildi): okunmuş ama bu oturumda basılmamış 58:12, 9:67, 24:4, 24:55 adla anılmıştı — 58:12 ve 9:67 sohbette basıldı, 24:4 / 24:55 sayıya çevrildi; 'cebel' (20 → 21 okunmuş, 15 → 14 okunmamış) ve 'hâliq' (9 → 10, 2 → 1) sayıları lemma listesinden düzeltildi; sayılmamış 'en uzun' iddiası silindi",
 ],
}

DUZELTME = {
 24: {'alan': 'mercek', 'eski': "Lafız sûre içi 31. ve son token", 'dogru': "Kök أله sayımı (31) lafızla birlikte 59:22 ve 59:23'teki 'lâ ilâhe' tokenlerini de içeriyor; sûre bilançosu lafız 29 token / 17 ayet (hasr_kapanis). 59:24'teki token kök أله'nin sûre içi 31. ve son geçişi, lafzın sûre içi 29. ve son tokeni. Kapanış kuru koşusunda yakalandı; özgün alan korunur.", 'aday': None, 'blok': '18-24'},
}
