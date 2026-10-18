# -*- coding: utf-8 -*-
"""kamer_kayit.py — sûre 54 (Kamer) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 54

CIPA = {
 # blok 1-10
 1: dict(kademe='L1', olgu=True, cipa=False, not_="'ve'nşaqqa'l-qamer' — gök cismi + hâl (yarılma); süreç / ölçü / mekanizma yok — L1 (52:9 emsali); doğal süreç iddiası KAPATILAMAZ; tarayıcı vermedi"),
 7: dict(kademe='L1', olgu=True, cipa=False, not_="'ke-ennehum cerâdun munteşir' — teşbih içinde canlı (çekirge) + davranış (yayılma); ölçü / mekanizma yok — L1; tarayıcı vermedi"),
 # blok 11-20
 11: dict(kademe='L1', olgu=True, cipa=False, not_="'ebvâbe's-semâ'i bi-mâ'in munhemir' — gök + su + nitelik (boşanan); ölçü / mekanizma yok — L1; tarayıcı vermedi"),
 12: dict(kademe='L1', olgu=True, cipa=False, not_="'feccerne'l-arda uyûnen fe'ltaqa'l-mâ'u alâ emrin qad qudir' — yerden pınar + iki suyun buluşması (süreç adı); 'qudir' takdir kelimesi, birim / miktar yok — L1; L4 ölçü kolu yalnız kelime düzeyinde, KAPATILAMAZ; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'zâti elvâhin ve dusur' — insan yapımı araç (tahta, çivi), doğal olgu değil; tarayıcı vermedi"),
 19: dict(kademe='L1', olgu=True, cipa=False, not_="'rîhan sarsaran fî yevmi nahsin mustemirr' — rüzgâr + nitelik + süre adı; hız / ölçü yok — L1 (41:16 emsali); tarayıcı vermedi"),
 20: dict(kademe='L1', olgu=True, cipa=False, not_="'ke-ennehum a'câzu nahlin munqa'ir' — teşbih içinde bitki (hurma) + hâl (kökünden sökülme) — L1; tarayıcı vermedi"),
 # blok 21-30
 27: dict(kademe='L0', olgu=True, cipa=False, not_="'mursilu'n-nâqati fitneten' — canlı (dişi deve) adlanıyor, işlevi sınama; doğal süreç yok — L0; tarayıcı vermedi"),
 # blok 31-40
 31: dict(kademe='L1', olgu=True, cipa=False, not_="'ke-heşîmi'l-muhtezir' — teşbih içinde bitki kalıntısı (kuru ot) + hâl — L1 (18:45 'heşîm' emsali); tarayıcı vermedi"),
 34: dict(kademe='L0', olgu=True, cipa=False, not_="'hâsiben' — taş savuran rüzgâr adlanıyor, 'bi-sehar' vakit; süreç / ölçü yok — L0; tarayıcı vermedi"),
 # blok 41-50
 49: dict(kademe='L1', olgu=True, cipa=False, not_="'kulle şey'in halaqnâhu bi-qader' — yaratma + ölçü kelimesi ('qader'); birim / miktar / mekanizma yok — L1; L4 ölçü kolu yalnız kelime düzeyinde, KAPATILAMAZ (54:12 emsali); tarayıcı vermedi"),
 50: dict(kademe='L1', olgu=True, cipa=False, not_="'ke-lemhin bi'l-basar' — göz kırpma süresi, insan bedeni süresi, birim değil — L1 (27:40 emsali); tarayıcı vermedi"),
 # blok 51-55
 54: dict(kademe=None, olgu=False, cipa=False, not_="'fî cennâtin ve neher' — cennet ırmağı, âhiret mekânı; doğal olgu değil; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  'esmâ: blokta e_oto tokeni yok; mühür ölçümü [] — karar gerekmedi; lafız 0, Rab 1 (54:10, sûre içi [1/1])',
  'yıldız formülü: 54:10 ★★★ rab z=3,94 (5 kelimede 2. sırada Rab) — bilinen davranış',
  "edilgen: 54:9 'uzdücir' gerçek edilgen (EDİLGEN 1/4, pas z=1,10) — ölçüm doğru; engelleyen adsız",
  "fâsıla: blokta on ayetin hepsi ر (R sınıfı); kafiye kırığı yok — 'ٓ' artefaktı yok",
  "biçim (517 ailesi): 54:7 teşbih 'ke-enne', 54:2 / 54:8 / 54:9 / 54:10 alıntı sınırları, 54:10 alıntı içi 1S → 2MS emir ölçümde işaretsiz (iltifât 0); 54:5 'mâ' olumsuz / soru iki okumalı",
  "konuşan / gönderge (1017 ailesi): 54:6 muhatap 2MS ve 'ed-dâ'' (çağıran) adsız; 54:9 1P konuşan ('abdenâ') adsız, engelleyen (edilgen) adsız; 54:10 seslenen 3MS — meal adlandırmadı",
  "aday 1040 alanı (sûre sınırı; kayıt, test yok): fâsıla 53:62 ا → 54:1 ر; 53:57 'ezifeti'l-âzife' / 54:1 'iqterabeti's-sâ'a' (iki kökle 'yaklaştı'); 53:23 'yettebi'ûne … mâ tehve'l-enfus' + 've leqad câ'ehum' / 54:3 've'ttebe'û ehvâ'ehum' + 54:4 've leqad câ'ehum'; 53:56 'nuzur' + 53:26, 28 'lâ tuğnî' / 54:5 'fe-mâ tuğni'n-nuzur'; 53:29 'fe-a'rid' / 54:6 'fe-tevelle anhum'; 53:52 / 54:9 Nûh kavmi",
  "kuruluş (okuma): 52:44 ve 54:2 — 've in yerev' + nesne + 'yeqûlû' + adlandırma; 44:22 ve 54:10 — 'fe-de'â rabbehû enne / ennî'",
  "sûre içi (okuma): زجر 54:4 'muzdecer' / 54:9 'uzdücir'; دعو 54:6 ×2, 54:8 çağıran / 54:10 Rabbe seslenme",
  "lemma (sayım): 'muzdecer', 'nukur', 'asir', 'mağlûb' korpusta 1'er; 'cerâd' 2 ayet; 'ecdâs' 3 ayet",
  'karşıt çift (aday 1039, okuma): ayet içi 54:10 mağlûb / intasir; diğer dokuz ayette yok — kayıt, test yok',
  'çıpa: 54:1 L1 (ay + yarılma, KAPATILAMAZ); 54:7 L1 teşbih içinde (çekirge + yayılma); tarayıcı adayı yok',
  'okuma: 21:1, 53:57 → 54:1; 52:44, 53:29 → 54:2; 47:14, 53:23 → 54:3; 53:23 → 54:4; 10:101, 53:56 → 54:5; 51:54, 53:29, 50:41 → 54:6; 36:51 → 54:7; 14:43 → 54:8; 50:12, 53:52, 52:29 → 54:9; 44:22 → 54:10 — KAPATILAMAZ',
  'tetik: ön kuru koşu 4 tetik satırı (54:1 سوع قمر ◈K; 54:6 يوم ◈K; 54:7 بصر ◈B; 54:8 يوم ◈K) — kayıtta 0 uyuşmaz; [x/y] 0 (14 sayım); kayıttan önce okunmuş ama bu oturumda basılmamış dört grup ayet anması (47:16; 16:113, 29:39; 37:174; 22:42, 38:12, 40:5) çıkarıldı, yalnız sayı kaldı',
 ],
 (11, 20): [
  'esmâ: blokta e_oto tokeni yok; mühür ölçümü [] — karar gerekmedi; lafız 0, Rab 0',
  "yıldız formülü: 54:11, 13, 20 ★★★ hapaks z=3,28 (همر, دسر, قعر — üçü de kok_ekle_54'ten); 54:12, 14 ★ pas z=1,57 (gerçek edilgen 'qudir', 'kufir')",
  'fâsıla: on ayetin hepsi ر; kafiye kırığı yok',
  "şahıs (okuma): 54:16, 18 'azâbî' 1S — 54:11-15 1P anlatıcıdan 1S'ye geçiş; ölçüm iltifât 0 (517 ailesi)",
  "biçim (517 ailesi): 54:20 teşbih 'ke-enne', 54:19 'innâ' tekidi ölçümde işaretsiz",
  "konuşan / gönderge (1017 ailesi): 1P / 1S anlatıcı, 54:12 takdir eden (edilgen), 54:13 taşınan 'hu', 54:14 inkâr edilen (edilgen), 54:15 'hâ' göndergesi adsız; taşıyan araç metinde adlanmıyor ('zâti elvâhin ve dusur') — meal ad eklemedi",
  "nakaratlar (sayım): 'fe-keyfe kâne azâbî ve nuzur' 4 ayet, 've leqad yessernâ'l-qur'âne li'z-zikri fe-hel min muddekir' 4 ayet, 'fe-hel min muddekir' 6 ayet, 'innâ erselnâ aleyhim' 3 ayet — hepsi korpusta yalnız bu sûrede; 'muddekir' lemma yalnız bu 6 ayette",
  "gloss: عين 54:12 'uyûn' (pınar) / 54:14 'a'yuninâ' (göz) — gloss ikisini kapsıyor; حمل 'hamalnâhu' taşıma (◈B tetik, gebelik değil)",
  "sûre içi (okuma): 'mustemirr' lemma 2 ayet — 54:2 'sihr' / 54:19 'nahs'; أمر 54:3 / 54:12",
  "aday 1040 alanı (kayıt): 53:50-53 helâk sırası (Âd, Semûd, Nûh kavmi, 'mu'tefike') → 54:9-18 Nûh kavmi, Âd ile açılıyor",
  "karşıt çift (aday 1039, okuma): ayet içi 54:16, 18 'azâbî' / 'nuzur'; ayetler arası 54:11 'semâ'' / 54:12 'ard' — kayıt, test yok",
  "çıpa: 54:11, 12, 19, 20 L1 (54:12 'qudir' ölçü kelimesi, birim yok — KAPATILAMAZ; 54:20 teşbih içinde); 54:13 olgu değil (insan yapımı araç); tarayıcı adayı yok",
  'okuma: 15:14 → 54:11; 36:34, 11:44 → 54:12; 11:37, 23:27, 52:48 → 54:14; 29:35, 29:15 → 54:15; 26:123, 53:50 → 54:18; 41:16, 51:41 → 54:19; 50:10 → 54:20 — KAPATILAMAZ',
  "tetik: ön kuru koşu 7 tetik satırı (54:11 سمو موه ◈K; 54:12 أرض موه ◈K, عين ◈B; 54:13 حمل ◈B; 54:14 عين ◈B; 54:19 روح يوم ◈K; 54:20 أنس ◈B) — kayıtta 0 uyuşmaz; [x/y] 0 (15 sayım); kayıttan önce 54:13 'levh' notu okunmamış ayetler için yeniden yazıldı",
 ],
 (21, 30): [
  'esmâ: blokta e_oto tokeni yok; mühür ölçümü [] — karar gerekmedi; lafız 0, Rab 0',
  "ölçüm (924): 54:28 'biçim QASEM' — قسم kökü yemin okunmuş; 'qisme' paylaştırma, yemin yok — 53:22 ile aynı araç arızası",
  "edilgen: 54:25 'ulqiye' gerçek edilgen — ★★★ pas z=5,38 (tek fiilli ayet; formül davranışı)",
  'fâsıla: on ayetin hepsi ر; kafiye kırığı yok',
  'biçim (517 ailesi): 54:24-25 Semûd alıntısının sınırları ölçümde işaretsiz; 54:26 alıntıdan anlatıya geçiş işaretsiz',
  "konuşan / gönderge (1017 ailesi): 54:24 'beşer', 54:25 'aleyhi', 54:27 muhatap 2MS, 54:29 'sâhibuhum' ve kesilen nesne adsız; meal metin dışı ad eklemedi; 1P / 1S konuşan adsız",
  "gloss (1021 ailesi): سعر 'alevlenme, saîr' — 54:24 'su'ur' meal 'çılgınlık'; iki okuma, KAPATILAMAZ; عطو 54:29 'te'âtâ' girişme anlamı gloss 'verme'den ayrılıyor",
  "nakaratlar (sayım): 'fe-keyfe kâne azâbî ve nuzur' dört geçişini tamamladı (54:16, 18, 21, 30); 've leqad yessernâ'l-qur'ân …' ikinci (54:22)",
  "aday 1040 alanı (kayıt): 'qisme' lemma 3 ayet — 53:22 / 54:28 ardışık iki sûrede (erkek-dişi paylaştırması / su paylaştırması); 53:51 / 54:23 Semûd",
  "okuma: 38:8 'e-unzile aleyhi'z-zikru min beyninâ' / 54:25 'e-ulqiye'z-zikru aleyhi min beyninâ' — aynı soru, fiil farklı",
  "karşıt çift (aday 1039, okuma): ayet içi 54:21, 30 'azâbî' / 'nuzur'; ayetler arası 54:25 'kezzâbun eşir' (iddia) / 54:26 'meni'l-kezzâbu'l-eşir' (soru) — kayıt, test yok",
  'çıpa: 54:27 L0 (dişi deve adlanıyor); tarayıcı adayı yok',
  'okuma: 26:141, 53:51 → 54:23; 26:154 → 54:24; 38:8 → 54:25; 17:59, 11:64, 26:155, 44:59 → 54:27; 53:22, 26:155 → 54:28; 26:157, 53:34 → 54:29 — KAPATILAMAZ',
  'tetik: ön kuru koşu 1 tetik satırı (54:28 موه ◈K) — kayıtta 0 uyuşmaz; [x/y] 0 (16 sayım)',
 ],
 (31, 40): [
  'esmâ: blokta e_oto tokeni yok; mühür ölçümü [] — karar gerekmedi; lafız 0, Rab 0',
  'yıldız: blokta yıldız yok (0:10); hapaks, edilgen, kafiye kırığı yok — fâsıla on ayette ر',
  "gloss (1021 ailesi): سحر 54:2 'sihr' / 54:34 'sehar' (seher vakti) — gloss 'büyü, sihir' seher anlamını kapsamıyor; 54:34 'âl' (aile) أول sayacında, gloss 'ilk, evvel' kapsamıyor",
  "biçim (517 ailesi): 54:31 teşbih 'ke-', 54:37 ve 54:39 'fe-zûqû' alıntı sınırı ölçümde işaretsiz",
  "konuşan / gönderge (1017 ailesi): 1P / 1S konuşan adsız; 54:37 konuklar adsız; 54:36 uyaran 3MS ve 54:37 'hu' göndergesi 54:34 'Lût' (metindeki ad); 54:35 şükreden 'men' adsız",
  "nakaratlar (sayım): 've leqad yessernâ'l-qur'ân …' dört geçişini tamamladı (54:17, 22, 32, 40); 'innâ erselnâ aleyhim' üç geçişini tamamladı (54:19, 31, 34); 'fe-zûqû azâbî ve nuzur' 2 ayet (54:37, 39)",
  "aday 1040 alanı (kayıt): 'temârâ' lemma 4 ayet — 53:55 / 54:36 sûre sınırının iki yanında (dördü de okundu: 42:18, 53:12, 53:55, 54:36)",
  "okuma: 29:40 'hâsib' ve 'sayha' bir ayette → 54:31 'sayha' (Semûd), 54:34 'hâsib' (Lût kavmi); 36:66 'le-tamesnâ alâ a'yunihim' varsayım → 54:37 'fe-tamesnâ a'yunehum' olmuş (15:14 → 54:11 ile aynı kuruluş)",
  "sûre içi (okuma): عين 3/3 — pınar / 1P gözetim / silinen gözler; جزي 54:14 'kufir' / 54:35 'şeker'; 'mustaqirr' 54:3 / 54:38",
  "karşıt çift (aday 1039, okuma): ayet içi 54:34 helâk / kurtuluş ('illâ'), 54:37, 39 'azâbî' / 'nuzur'; ayetler arası 54:14 'kufir' / 54:35 'şeker' — kayıt, test yok",
  "çıpa: 54:31 L1 teşbih içinde (kuru ot); 54:34 L0 ('hâsib'); tarayıcı adayı yok",
  'okuma: 36:29, 29:40, 18:45 → 54:31; 26:160 → 54:33; 29:40, 51:18 → 54:34; 27:40 → 54:35; 44:16, 53:55 → 54:36; 36:66, 15:68 → 54:37; 27:40 → 54:38 — KAPATILAMAZ',
  'tetik: ön kuru koşu 1 tetik satırı (54:37 عين ◈B) — kayıtta 0 uyuşmaz; [x/y] 0 (13 sayım); kayıttan önce bu oturumda basılmamış ayet anmaları (36:49, 36:53, 38:15; 17:68) çıkarıldı',
 ],
 (41, 50): [
  "esmâ: 54:42 'azîz' + 'muqtedir' SON konum ÇİFT mühür, ton celâl; el kararı ilâhî ×2 (nekre 'ahze azîzin muqtedir', gönderge 1P yakalayan — sınır vakası) → geçerli mühür [42]; sûre 54'te 1-50 arasında tek geçerli mühür; lafız 0, Rab 0",
  "yıldız: 54:46 ★★★ hapaks 'edhâ' (z=3,28); 54:45 ve 54:48 ★★ pas (EDİLGEN 1/2, z=2,52) — bozguna uğratan ve sürükleyen adsız; 7 ayet yıldızsız; kafiye kırığı yok — fâsıla on ayette ر",
  "biçim (517 ailesi): 54:44 alıntı ('nahnu cemî'un muntasir'), 54:48 'zûqû' alıntı sınırı, 54:50 teşbih 'ke-' ölçümde işaretsiz; 54:47 'inne' tekidi ölçümde kip yok",
  'konuşan / gönderge (1017 ailesi): 54:41 uyarılar adsız; 54:43 muhatap 2MP adsız; 54:44 söyleyenler 3MP adsız; 54:45 topluluk adsız (metinde ad yok); 54:48 sürükleyen ve söyleyen adsız; 1P adsız',
  "kök sayacı (okuma): 54:48 'nâr' نور sayacında; سحب burada 'yushabûn' (sürükleme) — ◈K tetiği gök olgusu değil; قدر sûre içi takdir / güç / ölçü (54:12, 42, 49)",
  "kalıp sayımı imlâ farkı: 54:42 'bi-âyâtinâ kullihâ' ile 20:56 'âyâtinâ kullehâ' harekesiz kalıpta ayrılıyor (--on ile de 1) — eşleşme okumayla",
  "sûre içi (sayım): 'fî dalâlin ve su'ur' 54:24 / 54:47 ve 'su'ur' lemma yalnız bu iki ayette; 'âl' 54:34 / 54:41; ذوق 54:37, 39, 48; مرر 54:2, 19, 46; وحد 54:24, 31, 50",
  "okuma: 16:77 've mâ emru's-sâ'ati illâ ke-lemhi'l-basar' → 54:50 've mâ emrunâ illâ vâhidetun ke-lemhin bi'l-basar' (54:46 'es-sâ'a' iki ayet önce); 18:45 'heşîm' + 'muqtedir' → 54:31 / 54:42",
  "okuma: 51:45, 28:81 'muntasir' olumsuz → 54:44 olumlu iddia → 54:45 bozgun; 54:10 'fe'ntasir' / 54:44 'muntasir'",
  "karşıt çift (aday 1039, okuma): ayetler arası 54:44 'cemî'un muntasir' / 54:45 'yuhzemu'l-cem''; 54:49 'kulle şey'' / 54:50 'vâhide' — kayıt, test yok",
  'çıpa: 54:49 L1 (ölçü yalnız kelime), 54:50 L1 (göz kırpma süresi); tarayıcı adayı yok',
  'okuma: 14:6, 40:46 → 54:41; 20:56, 11:102, 18:45, 43:42 → 54:42; 9:1, 37:156, 26:196 → 54:43; 26:56, 51:45, 28:81 → 54:44; 48:22, 33:15 → 54:45; 15:43, 11:17 → 54:46; 54:24, 43:74 → 54:47; 40:71, 17:97, 25:34 → 54:48; 15:21 → 54:49; 16:77, 27:40 → 54:50 — KAPATILAMAZ',
  "tetik: ön kuru koşu 4 tetik satırı (54:46 سوع ◈K, 54:48 يوم سحب ◈K, 54:49 خلق ◈B, 54:50 بصر ◈B) — kayıtta 0 uyuşmaz; [x/y] 0 (36 sayım); kayıttan önce basılmamış ayet anmaları (52:30, 52:33) ve iki yanlış ifade (54:41 iltifât yönü, 54:46 'lemma' → 'tam kalıp') düzeltildi",
 ],
 (51, 55): [
  "esmâ: 54:53 'kebîr' SON konum mühürsüz (ölçüm) — el kararı değil (küçük / büyük işler); 54:55 'melîk' + 'muqtedir' ÇİFT mühür, ton celâl, el kararı ilâhî ×2 (nekre, 54:42 emsali) → geçerli mühür [55]; sûre 54 geçerli mühür 2: 54:42, 54:55; lafız 0, Rab 0",
  'yıldız: blokta yıldız yok (0:5); hapaks, edilgen, kafiye kırığı yok — fâsıla beş ayette ر',
  "konuşan / gönderge (1017 ailesi): 54:51 muhatap 2MP adsız ('eşyâ'akum'); 54:52 yapanlar 3MP adsız; 1P adsız; 54:55 'melîk' nekre",
  "biçim: 54:47 ve 54:54 'inne' tekidi ölçümde kip yok; 54:53, 54:54, 54:55 şahıs işareti yok",
  "nakarat (sayım): 'fe-hel min muddekir' altı geçişini tamamladı (54:15, 17, 22, 32, 40, 51) — altısı da bu sûrede",
  "sûre içi (sayım / okuma): 'fi'z-zubur' 54:43 / 54:52 (2 ayet, ikisi bu sûrede); 'kullu şey'' 54:49 / 54:52; 'muqtedir' 54:42 / 54:55; عند 54:35 / 54:55",
  "okuma: 54:47 'inne'l-mucrimîne fî dalâlin ve su'ur' / 54:54 'inne'l-muttaqîne fî cennâtin ve neher' — aynı iskelet; 15:45, 51:15, 52:17 'uyûn / na'îm' yerine 'neher' (tekil, fâsıla ر)",
  "okuma: 18:49, 10:61, 34:3 küçük / büyük + kitap → 54:53 'mustetar'; 17:58, 33:6 'mestûr' aynı kök",
  "karşıt çift (aday 1039, okuma): ayet içi 54:53 'sağîr' / 'kebîr'; ayetler arası 54:47 'mucrimîn' / 54:54 'muttaqîn' — kayıt, test yok",
  'çıpa: 54:54 cennet ırmağı — olgu değil; blokta kademe yok; tarayıcı adayı yok',
  'okuma: 34:54, 15:10, 19:69, 54:15 → 54:51; 54:43 → 54:52; 17:24, 18:49, 10:61, 34:3, 17:58, 33:6 → 54:53; 15:45, 51:15, 52:17, 44:51, 54:47 → 54:54; 9:81, 54:42 → 54:55 — KAPATILAMAZ',
  'tetik: ön kuru koşu 1 tetik satırı (54:54 نهر ◈K) — kayıtta 0 uyuşmaz; [x/y] 0 (17 sayım)',
 ],
}

DUZELTME = {
}
