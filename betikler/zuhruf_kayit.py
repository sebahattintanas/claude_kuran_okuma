# -*- coding: utf-8 -*-
"""zuhruf_kayit.py — sûre 43 (Zuhruf) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 43

CIPA = {
 # blok 1-10
 9: dict(kademe='L0', olgu=True, cipa=False, not_="gökler ve yer yalnız yaratılan olarak adlanıyor (soru içinde); süreç/ölçü yok (39:38 emsali); tarayıcı v4 adayı, çıpa değil"),
 10: dict(kademe='L1', olgu=True, cipa=False, not_="yer 'mehd' (döşek) ve üzerinde 'subul' (yollar): işlev adı + alan; mekanizma/ölçü yok — L1 (27:61 'karar yeri' emsali); tarayıcı v4 adayı, çıpa değil"),
 # blok 11-20
 11: dict(kademe='L2', olgu=True, cipa=False, not_="gökten ölçüyle ('bi-qader') su → onunla ('bihî') ölü beldenin dirilmesi: nedensel bağ adlı, ara durum/mekanizma yok, ölçü adı birimsiz — L2 (35:9 L2 emsali); tarayıcı vermedi"),
 12: dict(kademe='L1', olgu=True, cipa=False, not_="bütün çiftlerin yaratılması (alan/üye eşlemesi yok, 36:36 emsali) + gemi ve davar binme işleviyle — L1 (40:79 emsali); 'fulk' gemi, kozmik öğe değil (S2 açık); tarayıcı vermedi"),
 13: dict(kademe='L1', olgu=True, cipa=False, not_="binilenlerin sırtına yerleşme + 'sahhara' (boyun eğdirme): canlı/araç + işlev, nedensellik/ölçü yok — L1 (40:79 emsali); tarayıcı v4 adayı, çıpa değil"),
 # blok 31-40
 32: dict(kademe=None, olgu=False, cipa=False, not_="tarayıcı v4 adayı: geçimin paylaştırılması ve derecelerle üstün kılma — toplumsal düzen, doğal olgu yok, merdiven uygulanmadı"),
 # blok 51-60
 51: dict(kademe='L1', olgu=True, cipa=False, not_="ırmaklar + akış fiili ('tecrî') + yer ('min tahtî') — Firavun'un mülk iddiası içinde; nitelik/ölçü yok — L1; tarayıcı vermedi"),
 60: dict(kademe=None, olgu=False, cipa=False, not_="tarayıcı v4 adayı: şartlı varsayım ('lev neşâu') — yeryüzünde halef olacak melekler; doğal olgu yok, merdiven uygulanmadı"),
 # blok 81-89
 82: dict(kademe='L0', olgu=True, cipa=False, not_="gökler, yer ve arş Rab'bin tamlamasında adlanıyor; nitelik/süreç yok — L0; tarayıcı vermedi"),
 84: dict(kademe='L0', olgu=True, cipa=False, not_="gök ve yer ilâhlığın iki alanı olarak adlanıyor; süreç/ölçü yok — L0; tarayıcı vermedi"),
 85: dict(kademe='L0', olgu=True, cipa=False, not_="göklerin, yerin ve 'mâ beynehumâ'nın mülkü + sâ'anın bilgisi; nitelik/süreç/ölçü yok — L0; tarayıcı vermedi"),
 87: dict(kademe='L0', olgu=True, cipa=False, not_="insanların yaratılışı soru içinde ('men halaqahum'), cevap 'Allah'; aşama/mekanizma yok — L0 (43:9 emsali); tarayıcı v4 adayı, çıpa değil"),
}

ARIZA = {
 (1, 10): [
  "esmâ (1022 ailesi): 43:2 'mubîn' (ölçüm MÜHÜRSÜZ, esma_kayit mühür EVET), 43:4 'aliyy'/'hakîm' (ölçüm MÜHÜR, ÇİFT) — kitabın sıfatı, okuyucu kararı değil; 43:6 ve 43:8 'evvel' ölçümde 'esmâ yok', esma_kayit mühür EVET — öncekiler, değil; 43:9 'azîz'/'alîm' alıntı içinde, ilâhî",
  "iltifât / alıntı (1017 ailesi): 43:7 ölçüm iltifât 1 (1>3, ayetler arası 43:6 → 43:7); 43:9 alıntı 'halaqahunne'l-azîzu'l-alîm' (sorulanların cevabı); 43:10 'ellezî … lekum' alıntı sınırı metinde işaretsiz — ölçüm iltifât 0",
  "gloss (1021 ailesi): صفح 43:5 yüz çevirip bırakma — gloss 'hoşgörü, bağışlama'; نبأ 43:6-7 'nebiyy' — gloss 'haber'; مهد 43:10 döşek — gloss 'beşik, döşek' (19:29 beşik)",
  "biçim (517 ailesi): 43:3 'innâ' tekidi, 43:6 'kem' (çokluk) ölçümde işaretsiz",
  'veri: 43:1 besmele ayet metnine bitişik (n=1, harf 21 → harf3 2) — 41:1, 42:1 emsali',
  "sayım gürültüsü: 'qur'ânen arabiyyâ' harekesiz kalıp 2 ayet, lemma dizisi 6 ayet (imlâ farkı: dagger elif) — lemma dizisi 42:7 kaydıyla tutarlı; okumada lemma dizisi kullanıldı (oturum_lemdizi.py)",
  "aday 1040 alanı: 42:7 → 43:3 ('qur'ânen arabiyyâ'), 42:51 → 43:4 ('aliyyun hakîm' — Allah / kitap) — kayıt, test yok; 42:51 → 43:4 aday 1041 alanına sınırda (gönderge insan değil, kitap)",
  'tetik: ilk koşuda 0 uyuşmaz (oturum_tetik.py)',
 ],
 (11, 20): [
  "esmâ (1022 ailesi): 43:15 ve 43:18 'mubîn' ölçüm MÜHÜRSÜZ, esma_kayit mühür EVET — insan sıfatı, değil; 43:17 'ehad' değil; 'er-rahmân' 43:17, 19, 20 bağımsız ad, ilâhî (aday 1019) — 43:20 ölçüm ORTA MÜHÜRSÜZ, esma_kayit mühür EVET",
  "iltifât / alıntı (1017 ailesi): 43:11 3MS → 1P → 2MP ve 43:16 3MS → 2MP tek ayette, ölçüm iltifât 0; 43:13 öğretilen söz 'teqûlû' ile açılıyor, 43:14 devamı mı metinde işaretsiz; 43:15 ölçüm iltifât 1 (1>3, ayetler arası)",
  "gloss (1021 ailesi): نعم 43:12 davar / 43:13 nimet; قرن 43:13 'muqrinîn' güç yetiren — gloss 'nesil; birbirine bağlama'; بني 43:16 kız / oğul — gloss 'bina, yapma'; ضرب 43:5 yüz çevirme / 43:17 mesel getirme",
  "biçim (517 ailesi): 43:11 'kezâlike' benzetmesi ve 43:16 'em' sorusu ölçümde işaretsiz",
  "sayı işareti: 43:12 'zevc' (çiftler), 43:17 'ehad' ('onlardan biri') — ölçüm alanı, sayma değil",
  "yıldız: 43:14 ★★★ kaynak rab z=5,01 (n=4, kısa ayet etkisi); 43:11, 17, 18, 19 kaynak pas — edilgen fiiller",
  "aday 1040 alanı: 42:48 → 43:15 ('el-insâne … kefûr') — kayıt, test yok",
  'tetik: ilk koşuda 1 uyuşmaz — 43:17 ◈B satırına tetiksiz gözlem (yüz) yazılmıştı, kayıttan önce "—" yapıldı; tetik 0 uyuşmaz',
  "[x/y]: ilk koşuda 1 uyuşmaz — 43:20'de başka ayetlerin sayısı [x/y] biçiminde yazılmıştı, kayıttan önce düz metne çevrildi; 0 uyuşmaz",
 ],
 (21, 30): [
  "esmâ (1022 ailesi): 43:29 'rasûlun mubîn' ölçüm MÜHÜRSÜZ, esma_kayit mühür EVET — elçinin sıfatı, değil; blokta lafız 0, Rab 0 (43:1-30 lafız 0)",
  "iltifât / alıntı (1017 ailesi): 43:21 3MP → 1P, 43:25 1P → 2MS, 43:29 3MS → 1S ('metta'tu', konuşan adsız) — ölçüm iltifât 0; 43:22-24 alıntılar (atalar sözü ×2, uyarıcının sorusu, cevap); 43:24 'qâle' konuşanı adsız",
  "gloss (1021 ailesi): أثر 43:22-23 iz — gloss 'tercih etme, üstün tutma'; أمم 43:22-23 yol/din — gloss 'ümmet, topluluk'; عقب 43:28 soy — gloss 'sonuç, âkıbet'",
  "biçim (517 ailesi): 43:21 'em' sorusu, 43:22 ve 43:26 tekit 'inne' ölçümde işaretsiz",
  "sayım gürültüsü: lemma dizisi biçim farkını gizliyor — 40:25 'câehum bi'l-haqq' 'câehumu'l-haqq' ile eşleşti; 'fatara' emsallerinde şahıs (1S / 3FP) lemma dizisinde görünmüyor — metinden okundu",
  "okuma iddiası denetimi: üç ifade kayıttan önce korpus metniyle düzeltildi (43:26 21:52'deki soru; 43:27 21:56 şahsı; 43:30 40:25 biçimi)",
  'tetik: blokta ◈K/◈B tetik kökü yok; ilk koşuda 0 uyuşmaz',
 ],
 (31, 40): [
  "araç (924): 43:32 ölçüm 'biçim QASEM' — kök قسم burada paylaştırma ('yaqsimûn', 'qasemnâ'), yemin yok; yanlış pozitif, metin hakkında kanıt değil",
  "esmâ (1022 ailesi): 43:33 ve 43:36 'er-rahmân' bağımsız ad, ilâhî (aday 1019); 43:35 'âhir' (âhiret) ölçüm MÜHÜRSÜZ, esma_kayit mühür EVET — değil; 43:40 'mubîn' (sapıklık) değil",
  "iltifât / alıntı (1017 ailesi): 43:35 ölçüm iltifât 1 (3>2), 43:36 iltifât 1 (2>13); 43:38 'qâle' 3MS → alıntı 1S/2MS; 43:39 konuşan adsız, 2MP; 43:40 2MS — ölçüm iltifât 0",
  "gloss (1021 ailesi): ظهر 43:33 üstüne çıkma (43:13 sırt); عشو 43:36 göz yumma — gloss 'akşam'; سرر 43:34 taht — gloss 'sır'; شرك 43:39 azapta ortaklık",
  "biçim (517 ailesi): 43:36 'men' şartı ölçümde işaretsiz",
  "tetik sınıfı: 43:38 'el-meşriqayn' (iki doğu) — شرق ◈K tetik listesinde yok, satır '—'; yön/ufuk tetik sınıfı ön-kayıtta yok (yeni sınıf ayrı karar ister) — kayıt",
  "sayım: harekesiz kalıp sayımında kelime numarası yanlış verildi (43:36, 43:38) — çıktı kullanılmadı; bu iddialar sayı verilmeden yazıldı",
  'tetik: ilk koşuda 0 uyuşmaz (43:32, 35 حيي; 43:33 أنس; 43:39 يوم; 43:40 سمع dolu)',
 ],
 (41, 50): [
  "esmâ (1022 ailesi): 43:42 'muqtedirûn' (1P azamet çoğulu) ölçüm MÜHÜRSÜZ, esma_kayit mühür EVET — ilâhî, sınır vakası (37:75 emsali); 43:41 'muntaqimûn' esmâ listesinde yok (ölçüm ve esma_kayit saymıyor); 43:45 'er-rahmân' ilâhî (1019)",
  "aktör rolü (1038 ailesi): 43:46 Mûsâ ölçümde 'rol fail' — 'erselnâ Mûsâ'da mef'ûl, 'fe-qâle'de fâil; rol alanı tek değer",
  "gloss / kök eşlemesi (1021 ailesi): أخو 43:48 'uhtihâ' âyetin eşi — gloss 'kardeş'; قدر 43:42 güç (43:11 ölçü); أيي 43:49 nidâ 'eyyuhâ' kök أيي'ye bağlı — gloss 'âyet, işaret'",
  "biçim (517 ailesi): 43:43 tekit, 43:47 ve 43:50 müfâcee 'izâ' ölçümde işaretsiz",
  "iltifât / alıntı (1017 ailesi): 43:44 2MS → 2MP tek ayette — ölçüm iltifât 0",
  "yıldız: 43:44 ★★★ kaynak pas z=5,38 (n=6, tek fiil edilgen)",
  'tetik: blokta ◈K/◈B tetik kökü yok; ilk koşuda 0 uyuşmaz',
 ],
 (51, 60): [
  "kafiye / yıldız (1001 ailesi): 43:59 fâsıla ل ('isrâîl') kafiye kırığı; bilanço ★ kaynak etiketi 'allah, z=-0,53' (eşik altı) — düzeltilmiş kaynak kafiye kırığı",
  "esmâ (1022 ailesi): 43:56 'el-âhirîn' ölçüm MÜHÜRSÜZ, esma_kayit mühür EVET — sonrakiler, değil",
  "aktör rolü (1038 ailesi): 43:57 Meryem 'rol meful' — tamlamada muzâfun ileyh",
  "gloss (1021 ailesi): أسف 43:55 öfkelendirme — gloss 'esef, üzüntü'; خفف 43:54 hafife alma; قرن 43:53 dizi dizi (43:13, 36, 38'de güç yetirme / arkadaş); ذهب 43:53 altın (43:41 götürme); صدد 43:57 'yesiddûn' gürültü/yüz çevirme; بني 43:57 'ibn'; ملك 43:51 'mulk' / 43:53, 60 'melâike'",
  "biçim (517 ailesi): 43:53 'levlâ' tahdîdi, 43:54 tekit, 43:57 müfâcee ölçümde işaretsiz",
  "aday 1041 alanı: أسف 7:150, 20:86 Mûsâ 'ğadbâne esifâ' → 43:55 'âsefûnâ' (1P) — kayıt, test yok",
  "okuma iddiası denetimi: 43:51'de 32:27 biçimi kayıttan önce düzeltildi ('yubsirûn', 3MP)",
  'tetik: ilk koşuda 0 uyuşmaz (43:51 نهر, بصر; 43:60 أرض dolu)',
 ],
 (61, 70): [
  "esmâ (1022 ailesi): 43:62 'mubîn' ölçüm MÜHÜRSÜZ, esma_kayit mühür EVET — şeytanın sıfatı, değil",
  "biçim (517 ailesi): 43:64 tekit 'inne' ölçümde işaretsiz (kip yalnız IMPV); 43:61 ve 43:64 'biçim DIKKAT' kaynağı ölçümde adlanmıyor",
  "konuşan sınırı (1017 ailesi): 43:63 Îsâ alıntısının 43:64'e uzanıp uzanmadığı metinde işaretsiz; 43:61 'ittebi'ûn' ve 43:68 'yâ ibâdi' 1S konuşan adsız; 43:68 → 43:69 1S → 1P ölçüm iltifât 0",
  "gloss (1021 ailesi): خلف yerine geçme (43:60) / ayrılığa düşme (43:63, 65); نظر 43:66 bekleme; قوم 43:61, 64 'mustaqîm'; حبر 43:70 sevindirilme; أيي 43:49 'eyyuhâ' kök eşlemesi",
  "lafız: sûrenin ilk Allah lafzı 43:63 (43:1-62 lafız 0, bilanço)",
  "okuma iddiası denetimi: 43:62'de 28:87 biçimi kayıttan önce düzeltildi ('yesuddunneke'); 43:69'da أيي geçişleri 'âyât' + 'eyyuhâ' olarak düzeltildi",
  'tetik: ilk koşuda 0 uyuşmaz (43:61, 66 سوع; 43:65, 67, 68 يوم; 43:70 زوج dolu)',
 ],
 (71, 80): [
  "aday 1041 alanı: برم 43:79 — kök korpusta yalnız bu ayette, 3MP 'ebramû' / 1P 'mubrimûn' — kayıt, test yok",
  "biçim (517 ailesi): 43:74 ve 43:79 tekit 'inne', 43:79-80 'em' sorusu, 43:80 'belâ' ölçümde işaretsiz",
  "konuşan sınırı (1017 ailesi): 43:77 'qâle' öznesi adsız; 43:78 1P konuşanın 43:77 alıntısıyla ilişkisi işaretsiz, ölçüm iltifât 0; 43:71 3MP → 2MP tek ayette, iltifât 0",
  "gloss (1021 ailesi): برم 'yıpranma, bezginlik' — 43:79 kesin karar; ذهب 43:71 altın; سرر 43:34 tahtlar / 43:80 gizli; ملك 43:77 Mâlik adı",
  "yıldız: 43:75 ★★★ pas z=5,38 ve 43:79 ★★★ hapaks z=3,28 — ikisi de 5-6 kelimelik ayet",
  "okuma iddiası denetimi: 43:76'da şahıs geçişi cümlesi kayıttan önce düzeltildi (43:74-75 zaten 3MP)",
  'tetik: ilk koşuda 0 uyuşmaz (43:71 عين; 43:80 سمع dolu)',
 ],
 (81, 89): [
  "esmâ (1022 ailesi): 43:81 'rahmân' ölçüm MÜHÜRSÜZ / esma_kayit mühür EVET — ilâhî (aday 1019); 43:81 'evvel' (evvelu'l-âbidîn) değil; 43:89 'selâm' ölçüm MÜHÜRSÜZ / esma_kayit EVET — selam sözü, değil; 43:84 'hakîm' + 'alîm' geçerli mühür",
  "aday 1041 alanı (sınırda): 'hakîm' 43:4 kitap / 43:84 'huve' — insan değil, kitap",
  "konuşan / gönderge (1017 ailesi): 43:86 'yemliku' öznesi 'ellezîne' mi yalvarılanlar mı açık değil; 43:88 'qîlihî' bağlantısı ve 'hû' göndergesi işaretsiz",
  "gloss (1021 ailesi): لقي 43:53 atılma / 43:83 kavuşma; ملك 43:86 'yemliku' güç yetirme",
  "edilgen: 43:83 'yû'adûn' pas z=0,81 (eşik altı, yıldız yok); 43:87 'yu'fekûn' pas z=1,10 — ★ kaynağı allah z=1,97",
  "okuma iddiası denetimi: 43:81'de 'rahmân + veled' emsalleri 'iddia reddi' diye yazılmıştı — metinde başkalarının sözü olarak aktarılıyor, düzeltildi; 43:86 ملك geçiş listesine 43:19 eklendi",
  'tetik: ilk koşuda 0 uyuşmaz (43:82, 84 سمو/أرض; 43:85 سمو/أرض/سوع; 43:83 يوم; 43:87 خلق dolu)',
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_43.py uygular)
DUZELTME = {
}
