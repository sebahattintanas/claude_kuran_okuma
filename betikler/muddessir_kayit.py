# -*- coding: utf-8 -*-
"""muddessir_kayit.py — sûre 74 (Müddessir) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 74

CIPA = {
 # blok 1-10
 4: dict(kademe=None, olgu=False, cipa=False, not_="'siyâbeke' — elbise insan yapımı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe=None, olgu=False, cipa=False, not_="'nuqira fi'n-nâqûr' — âhiret / gaybî olay (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 9: dict(kademe=None, olgu=False, cipa=False, not_="'yevme'izin yevmun 'asîr' — âhiret günü (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 11-20
 17: dict(kademe=None, olgu=False, cipa=False, not_="'se-urhiquhû sa'ûdâ' — ceza yokuşu, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 21-30
 26: dict(kademe=None, olgu=False, cipa=False, not_="'se-uslîhi seqar' — Sekar, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 28: dict(kademe=None, olgu=False, cipa=False, not_="'lâ tubqî ve lâ tezer' — Sekar, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 29: dict(kademe=None, olgu=False, cipa=False, not_="'levvâhatun li'l-beşer' — Sekar, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 30: dict(kademe=None, olgu=False, cipa=False, not_="''aleyhâ tis'ate 'aşer' — sayı âhiret / gaybî varlıklar için (olgu=False); merdiven uygulanmadı; tarayıcı v4 adayı, çıpa değil"),
 # blok 31-31
 31: dict(kademe=None, olgu=False, cipa=False, not_="'ashâbe'n-nâri … melâ'ike … 'iddetehum … cunûde rabbik' — melekler, sayıları, Rabbin orduları gaybî (olgu=False); merdiven uygulanmadı; tarayıcı v4 adayı, çıpa değil"),
 # blok 32-40
 32: dict(kademe='L0', olgu=True, cipa=False, not_="'kellâ ve'l-qamer' — ay yalnız kasem nesnesi; süreç / ölçü yok — L0; tarayıcı vermedi"),
 33: dict(kademe='L1', olgu=True, cipa=False, not_="'ve'l-leyli iz edbera' — gecenin gidişi, süreç adı; mekanizma / ölçü yok — L1; tarayıcı vermedi"),
 34: dict(kademe='L1', olgu=True, cipa=False, not_="'ve's-subhi izâ esfera' — sabahın ağarması, süreç adı; mekanizma / ölçü yok — L1; tarayıcı vermedi"),
 39: dict(kademe=None, olgu=False, cipa=False, not_="'illâ ashâbe'l-yemîn' — âhiret (olgu=False); merdiven uygulanmadı"),
 40: dict(kademe=None, olgu=False, cipa=False, not_="'fî cennâtin yetesâ'elûn' — cennet, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 41-48
 42: dict(kademe=None, olgu=False, cipa=False, not_="'mâ selekekum fî seqar' — Sekar, âhiret (olgu=False); merdiven uygulanmadı"),
 46: dict(kademe=None, olgu=False, cipa=False, not_="'bi-yevmi'd-dîn' — hesap günü, âhiret (olgu=False); merdiven uygulanmadı"),
 48: dict(kademe=None, olgu=False, cipa=False, not_="'şefâ'atu'ş-şâfi'în' — âhiret (olgu=False); merdiven uygulanmadı"),
 # blok 49-56
 50: dict(kademe=None, olgu=False, cipa=False, not_="'ke-ennehum humurun mustenfira' — ürken eşekler teşbih aracı (olgu=False); merdiven uygulanmadı"),
 51: dict(kademe=None, olgu=False, cipa=False, not_="'ferrat min qasvera' — teşbih aracı (olgu=False); merdiven uygulanmadı"),
 53: dict(kademe=None, olgu=False, cipa=False, not_="'lâ yehâfûne'l-âhira' — âhiret (olgu=False); merdiven uygulanmadı"),
}

ARIZA = {
 (1, 10): [
  "esmâ: e_oto 0 token; KARAR 673 değişmedi; blokta mühür yok (esma_muhur_43 boş)",
  "kök tablosu: kok_ekle_74 2 kök (دثر 74:1, نقر 74:8; blok_dikey 'KARŞILIK YOK' → eklendi); 1465 → 1467; retroaktif yama: hedef listesi 2 ayet (sûre 4 — ayet kaydı yok, henüz okunmadı), hedefli yama 0, genel geçiş 0",
  "hapaks (yeni kök dersi): 74:1 دثر ★★★ hapaks z=3,28 — yeni kökün tek ayeti; içerik iddiası değil",
  "yıldız (924): 74:3, 74:7 ★★★ rab z=10,34 (kısa lafızsız ayette tek Rab); 74:8 ★★★ pas z=5,38 (kısa tek fiilli edilgen) — formül davranışı, içerik iddiası değil; 74:2, 4, 5, 6, 9, 10 yıldızsız",
  "harf alanı: ayet 1 ölçümünde harf 30 → harf3 11, isaret 0 (ayet 1 ailesi; besmele); araç alanı (924); KAPATILAMAZ",
  "gloss (1021 ailesi): أيي 74:1 'eyyuhâ' (nidâ edatı) — gloss 'âyet, işaret'; kök sayımı [1/2] iki ayrı lemmayı birleştiriyor olabilir — sûre içi ikinci geçiş henüz okunmadı",
  "fâsıla: 73:20 م → 74:1 ر; 74:1-10 hepsi ر (ölçüm); ölçüm kafiye kırığı 0",
  "sayı işareti: 74:6 'istekser' (كثر, çokluk) — sayı değil (kök kaynaklı yanlış alarm, okuma)",
  "ölçüm kip / biçim: 74:3, 4, 5, 7 meful (ya da câr) emirden önce — tahsis / hasr ölçümde görünmüyor (okuma, ◈D); 74:6 'testeksiru' merfû hâl fiili — i'râb alanı fiil kipini göstermiyor (—)",
  "ölçüm iltifât: 74:8 iltifât 1 (2MS → 3MS) — emirlerden haber cümlesine geçiş; okuma notu ◇'de",
  "kök ikilemesi: 74:8 نقر ×2 (fiil + alet adı; mef'ûl mutlak değil), 74:9 يوم ×2 (zarf + haber)",
  "◈K: 74:9 يوم tetik — satır dolu; 74:8 'nâqûr' tetik listesinde değil, satır '—'",
  "bağ: esit2 / nakarat3 / xref blokta boş (ölçüm); kalıp eşleri okumayla (25:26, 69:13, 73:1-2, 73:10)",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 21 sayım 0 uyuşmaz",
 ],
 (11, 20): [
  "esmâ: e_oto 0 token; KARAR 673 değişmedi; blokta mühür yok",
  "kök tablosu: blok_dikey 'KARŞILIK YOK' yok — kök eklenmedi (1467); retroaktif yama hedefli 0, genel 0",
  "yıldız (924): 74:19, 74:20 ★★ pas z=2,52 — içerik iddiası değil; 74:15 ★ kaynağı ölçümde 'n' (z=-0,89), gerçek kaynak kafiye kırığı (aday 1001)",
  "fâsıla: 74:10 ر → 74:11 ا ve 74:17 ا → 74:18 ر geçişleri ölçümde kafiye kırığı olarak işaretlenmiyor (924); 74:15 د işaretli — metindeki son harf د, gerçek geçiş",
  "ölçüm iltifât: 74:11 iltifât 1 (3. kişi → 1S / 2MS); 74:16 1P ('âyâtinâ') ve 74:17 1S'ye dönüş iltifât sayılmıyor (araç alanı, 924)",
  "konuşan katmanı: 74:11-15, 17 1S, 74:16 1P; 74:18-20 3MS anlatım — konuşan adsız, sınır metinde işaretli değil, KAPATILAMAZ (1017)",
  "gloss (1021 ailesi): بني 74:13 'benîn' (oğullar) — gloss 'bina, yapma'; مهد 74:14 'mehhedtu' (döşedi) — gloss 'beşik, döşek' (ad anlamı)",
  "eşsesli kök: أيي 74:1 'eyyuhâ' / 74:16 'âyât' — [x/2] kök sayımı iki ayrı lemmayı birleştiriyor; içerik iddiası değil",
  "sayı işareti: 74:11 'vahîd' — hâl (yalnız), sayı değil (okuma)",
  "nakarat3: 74:19 / 74:20 'qutile keyfe qaddar' — ölçüm tür 'tam' / 'ic' iki ayette farklı etiket, süzgeç GEÇMEZ; tekrar okumada yazıldı",
  "◈B: 74:11 خلق tetik — satır dolu; ◈K tetik blokta yok",
  "aday 1041 (kayıt): 'qaddara' 73:20 Allah / 74:18-20 adsız 3MS insan (ardışık sûre)",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 26 sayım 0 uyuşmaz",
 ],
 (21, 30): [
  "esmâ: e_oto 0 token; KARAR 673 değişmedi; blokta mühür yok",
  "kök tablosu: kok_ekle_74 2 kök (عبس 74:22, بسر 74:22; blok_dikey 'KARŞILIK YOK' → eklendi); 1467 → 1469; retroaktif yama: hedef listesi 2 ayet (sûre 4 — kayıt yok; عبس / بسر'ın öbür ayetleri henüz okunmadı), hedefli yama 0, genel geçiş 0",
  "yıldız (924): 74:24 ★★ pas z=2,52 — içerik iddiası değil; öbür 9 ayet yıldızsız",
  "ölçüm iltifât: 74:26 3MS anlatımdan 1S'ye ve 74:27 2MS hitaba geçiş iltifât sayılmıyor (iltifât 0; araç alanı, 924)",
  "sayı işareti: 74:30 'tis'a', ''aşer' — tek bileşik sayı (on dokuz), ölçüm iki ayrı işaret veriyor; doğru alarm (okuma)",
  "tarayıcı v4: 74:30 aday — sayı gaybî varlıklar için, olgu=False; çıpa değil",
  "lemma / meal ayrışması: 74:29 'li'l-beşer' morph lemması 'beşer' (insan); meal 'deri' yorumu — KAPATILAMAZ (okuma)",
  "nakarat3: 74:24 / 74:25 'in hâzâ illâ' — tür 'ic', süzgeç GEÇMEZ; tekrar okumada yazıldı",
  "aktör: 74:26 Sekar 'adlı yer, rol meful', 74:27 'rol fail' — 74:27'de 'mâ seqar' haber (soru cümlesinde mübtedâ 'mâ'); rol etiketi i'râbdan (aday 1038 ailesi)",
  "fâsıla: 74:21-30 hepsi ر (ölçüm); kafiye kırığı 0",
  "bağ: esit2 / xref blokta boş; kalıp eşleri okumayla (37:15, 34:43, 69:3, 23:24, 36:15)",
  "süreç: oturum ertesi güne sarktı — ortam korunmuştu (okuma_metni['74'] 20 ayet, ilerleme 4307), git fetch origin 51adf3a değişmedi; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 22 sayım 0 uyuşmaz",
  "süreç (72:1-10 dersi yinelendi): uret_blok / bağ yaması heredoc içinde assert'te durdu (BASLIK çapası metni yanlış), ardından gelen ayrı satırlı komutlar koştu — uret_blok eski BLOKLAR ile, yama_retroaktif ve aday_ekle değişmemiş dosyalarla; hiçbir dosya değişmedi (assert yazmadan önce), blok betiği koşmadı; yamalar ayrı dosyaya yazılıp && ile yeniden koşuldu",
  "süreç (kendi hatası, sûre sonunda yakalandı): bir önceki satırda bu oturumda basılmamış ayet numarası ders adı olarak yazıldı ('… dersi yinelendi'; doğrusu 'heredoc-assert dersi'); ARIZA alanı DUZELTME dışı — özgün satır korunur, bu satırla işaretlenir; ayet kayıtları değişmedi (blok betiği yalnız bilanço için yeniden koşuldu)",
 ],
 (31, 31): [
  "esmâ: e_oto 1 token (74:31:27 'mu'min' — 've'l-mu'minûn', insan çoğulu); karar DEĞİL; KARAR 673 → 674; mühür yok (esma_kayit, bilanço geçerli mühür boş)",
  "aday 1041 (kayıt): lemma 'mu'min' esmâ listesinde; burada insan çoğulu — Allah için geçişi bu oturumda basılmadı, ayet anılmaz",
  "kök tablosu: blok_dikey 'KARŞILIK YOK' yok — kök eklenmedi (1469); retroaktif yama hedefli 0, genel 0",
  "yıldız (924): 74:31 ★★★ kaynak n (57 kelime, n z=4,73) — uzun ayet formül davranışı, içerik iddiası değil",
  "ölçüm iltifât: 74:26-30 1S / 2MS / 3FS'den 74:31 1P'ye geçiş ve ayet içi 1P → 3MS (lafız) → 2MS ('rabbike') iltifât sayılmıyor (iltifât 0; araç alanı, 924)",
  "ayet içi tekrar: 'mâ ce'alnâ … illâ' ×2, 'ellezîne ûtu'l-kitâb' ×2, 'men yeşâ'' ×2 — nakarat3 alanında görünmüyor (tek ayet içi; araç alanı)",
  "sayı işareti: ''idde' (sayı adı) — sayı değil; 74:30'daki sayıya döner (okuma)",
  "tarayıcı v4: 74:31 aday — melekler / sayıları / Rabbin orduları gaybî, olgu=False; çıpa değil",
  "◈B: قلب 'qulûb' tetik — satır dolu, organ adı mecaz ('fî qulûbihim marad'); ◈K: 'nâr' tetik listesinde değil, satır '—'",
  "gönderge: 've mâ hiye illâ zikrâ' — 'hiye'nin göndergesi metinde işaretli değil, KAPATILAMAZ",
  "xref: 74:31 → 2:26 (henüz okunmadı), 14:4 (basıldı)",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 29 sayım 0 uyuşmaz; esma_el yorumunda basılmamış emsal numarası kayıttan önce 'mü'minler kuralı' diye değiştirildi",
 ],
 (32, 40): [
  "esmâ: e_oto 0 token; KARAR 674 değişmedi; blokta mühür yok",
  "kök tablosu: blok_dikey 'KARŞILIK YOK' yok — kök eklenmedi (1469); retroaktif yama hedefli 0, genel 0",
  "yıldız: blokta 9 ayetin dokuzu yıldızsız",
  "fâsıla: 74:37 ر → 74:38 ة → 74:39 ن geçişleri ölçümde kafiye kırığı olarak işaretlenmiyor (kafiye kırığı 0; araç alanı, 924)",
  "ölçüm biçim: 74:32 QASEM işaretli, 74:33 ve 74:34 kasem 've' biçim alanında yok (924)",
  "ölçüm iltifât: 74:37 2MP 'minkum' iltifât sayılmıyor (iltifât 0; 924)",
  "sayı işareti: 74:35 'ihdâ' — 'biri', sayı değil (okuma)",
  "gönderge: 74:35 'innehâ' 3FS — göndergesi metinde işaretli değil, KAPATILAMAZ",
  "aday 1041 (kayıt): fiil 'şâ'e' sûre içinde Allah için (74:31 'men yeşâ'' ×2) ve insan için (74:37 'li-men şâ'e minkum')",
  "◈K: 74:32 قمر, 74:33 ليل tetik — satırlar dolu; 74:34 'subh' tetik listesinde değil, satır '—'",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 26 sayım 0 uyuşmaz; 74:39 karşıt çift satırına yazılmış metin dışı çift ('ashâbe'n-nâr' / 'ashâbe'l-yemîn', 62:5 kuralı ailesi) kayıttan önce 'yok' yapıldı",
  "süreç (kendi hatası, kayıttan sonra yakalandı): bir önceki ARIZA satırında, bu oturumda basılmamış bir emsal ayet numarası ders adı olarak yazıldı ('… kuralı ailesi'); ARIZA alanı ayet anahtarı taşımadığı için DUZELTME betiğinin dışında — özgün satır korunur, bu satırla işaretlenir; ayet kayıtları değişmedi (blok betiği yalnız bilanço için yeniden koşuldu)",
 ],
 (41, 48): [
  "esmâ: e_oto 0 token; KARAR 674 değişmedi; blokta mühür yok",
  "kök tablosu: blok_dikey 'KARŞILIK YOK' yok — kök eklenmedi (1469); retroaktif yama hedefli 0, genel 0",
  "fâsıla: 74:41 ن → 74:42 ر KAFİYE KIRILMASI işaretli (gerçek geçiş); 74:42 ر → 74:43 ن dönüşü işaretsiz (924)",
  "yıldız (aday 1001): 74:42 ★ kaynağı ölçümde 'n' (z=-0,89), gerçek kaynak kafiye kırığı; öbür 7 ayet yıldızsız",
  "ölçüm iltifât: 74:42 2MP soru ve 74:43-47 1P alıntı iltifât sayılmıyor (iltifât 0; alıntı içi konuşan değişimi, 924)",
  "gloss (1021 ailesi): سكن 74:44 'miskîn' (yoksul) — gloss 'sükûn; mesken, konut'",
  "meal yorumu: 74:47 'el-yaqîn' meal parantezi '(ölüm)' — metinde adlı değil, okuma notu ◇'de",
  "xref: 74:46 → 83:11 (henüz okunmadı)",
  "◈K: 74:46 يوم tetik — satır dolu",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 22 sayım 0 uyuşmaz",
 ],
 (49, 56): [
  "esmâ: e_oto 1 token (74:53:5 'âhir' — 'el-âhira', âhiret); karar DEĞİL; KARAR 674 → 675; esma_kayit 'mühür EVET' (ölçüm konumu), bilanço geçerli mühür boş (esma_muhur_43 [53], geçerli [])",
  "aday 1041 (kayıt): 'erâde' 74:31 Allah / 74:52 insan; 'ehl' 11:81 insan (aile) / 74:56 Allah ('ehlu't-teqvâ ve ehlu'l-mağfira')",
  "kök tablosu: kok_ekle_74 1 kök (قسر 74:51; blok_dikey 'KARŞILIK YOK' → eklendi); 1469 → 1470; retroaktif yama: hedef listesi 2 ayet (sûre 4 — kayıt yok), hedefli yama 0, genel geçiş 0",
  "hapaks (yeni kök dersi): 74:51 قسر ★★★ hapaks z=3,28 — yeni kökün tek ayeti; içerik iddiası değil",
  "yıldız (924): 74:52 ★★ pas z=2,52 — içerik iddiası değil; öbür 6 ayet yıldızsız",
  "fâsıla: 74:49 ن → 74:50 ة geçişi ölçümde kafiye kırığı olarak işaretlenmiyor (924); 74:55 ه ölçümde H sınıfı (ة ile aynı)",
  "ölçüm biçim: 74:50 teşbih 'ke-enne' biçim alanında yok (924)",
  "gönderge: 74:54 'innehû' 3MS — göndergesi metinde işaretli değil, KAPATILAMAZ",
  "anlam: 74:51 'qasvera' (aslan / avcılar) — tek geçiş, KAPATILAMAZ; meal iki yorumu birlikte veriyor",
  "esit2: 74:55 → 80:12 TAM (henüz okunmadı)",
  "◈B: 74:50 'himâr' tetik listesinde değil — satır '—', gözlem ◇'de",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) ilk koşuda 1 uyuşmaz (74:50 ◈B satırı tetiksiz hâlde dolu yazılmıştı) → '—' yapıldı, ikinci koşu 0; oturum_xy 32 sayım 0 uyuşmaz",
 ],
}

DUZELTME = {
 35: dict(alan='meal', eski="o (Sekar), şüphesiz",
          dogru="Meal parantezi zamirin göndergesini Sekar diye kapatıyor; ◇ ve ARIZA 'innehâ' 3FS göndergesini KAPATILAMAZ yazıyor (meal ile mercek çelişkisi). Doğrusu: 'Şüphesiz o, büyük (belâ)lardan biridir,' — parantezsiz. Özgün alan korunur.",
          aday=1017, blok='32-40'),
}
