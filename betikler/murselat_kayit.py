# -*- coding: utf-8 -*-
"""murselat_kayit.py — sûre 77 (Mürselât) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 77

CIPA = {
 # blok 1-10
 7: dict(kademe=None, olgu=False, cipa=False, not_="'innemâ tû'adûne le-vâqi'' — vaat edilen, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe='L1', olgu=True, cipa=False, not_="'fe-izâ'n-nucûmu tumiset' — âhiretteki kozmik olay: yıldız adı + süreç (silinme), mekanizma / ölçü yok — L1 (75:8-9 emsali); tarayıcı vermedi"),
 9: dict(kademe='L1', olgu=True, cipa=False, not_="'ve izâ's-semâ'u furicet' — âhiretteki kozmik olay: gök + süreç (yarılma) — L1 (75:8-9 emsali); tarayıcı vermedi"),
 10: dict(kademe='L1', olgu=True, cipa=False, not_="'ve izâ'l-cibâlu nusifet' — âhiretteki olay: dağ + süreç (savrulma) — L1 (75:8-9 emsali); tarayıcı vermedi"),
 # blok 11-20
 11: dict(kademe=None, olgu=False, cipa=False, not_="'er-rusulu uqqitat' — âhiret, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 12: dict(kademe=None, olgu=False, cipa=False, not_="'li-eyyi yevmin uccilet' — âhiret, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'li-yevmi'l-fasl' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe=None, olgu=False, cipa=False, not_="'mâ yevmu'l-fasl' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="'veylun yevme'izin' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 19: dict(kademe=None, olgu=False, cipa=False, not_="'veylun yevme'izin' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 20: dict(kademe='L1', olgu=True, cipa=False, not_="'e-lem naxluqkum min mâ'in mehîn' — madde (su) + nitelik (değersiz) + yaratma; süreç / ölçü yok — L1 (76:2 emsali); tarayıcı vermedi"),
 # blok 21-30
 21: dict(kademe='L1', olgu=True, cipa=False, not_="'fî qarârin mekîn' — oluşum dizisi (su → sağlam yer → bilinen ölçü): yer + nitelik, mekanizma yok — L1 (75:37-39 / 76:2 emsali); tarayıcı vermedi"),
 22: dict(kademe='L1', olgu=True, cipa=False, not_="'ilâ qaderin ma'lûm' — ölçü / süre adlanıyor, birim / değer yok — L1; L4 değil (ölçü sınır vakası, birimsiz); tarayıcı vermedi"),
 24: dict(kademe=None, olgu=False, cipa=False, not_="'veylun yevme'izin' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 25: dict(kademe='L1', olgu=True, cipa=False, not_="'e-lem nec'ali'l-arda kifâtâ' — yer + işlev (toplayıcı), 77:26 ile; mekanizma yok — L1; tarayıcı vermedi"),
 26: dict(kademe='L1', olgu=True, cipa=False, not_="'ahyâ'en ve emvâtâ' — yerin topladıkları, 77:25 ile birlikte L1; tarayıcı vermedi"),
 27: dict(kademe='L1', olgu=True, cipa=False, not_="'ravâsiye şâmixât … mâ'en furâtâ' — dağlar + nitelik, su + nitelik + içirme; iki olgu yan yana, ilişki yok — L1 (27:61 kaydı emsali: 'dört yapı, ilişki yok'); tarayıcı vermedi"),
 28: dict(kademe=None, olgu=False, cipa=False, not_="'veylun yevme'izin' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 29: dict(kademe=None, olgu=False, cipa=False, not_="'intaliqû ilâ mâ kuntum bihî tukezzibûn' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 30: dict(kademe=None, olgu=False, cipa=False, not_="'zıllin zî selâsi şu'ab' — âhiret, azap gölgesi (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 31-40
 31: dict(kademe=None, olgu=False, cipa=False, not_="'lâ zalîlin ve lâ yuğnî mine'l-leheb' — âhiret, azap (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 32: dict(kademe=None, olgu=False, cipa=False, not_="'bi-şererin ke'l-qasr' — âhiret; benzetme aracı (saray) (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 33: dict(kademe=None, olgu=False, cipa=False, not_="'cimâletun sufr' — âhiret; benzetme aracı (deve) (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 34: dict(kademe=None, olgu=False, cipa=False, not_="'veylun yevme'izin' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 35: dict(kademe=None, olgu=False, cipa=False, not_="'yevmu lâ yentiqûn' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 36: dict(kademe=None, olgu=False, cipa=False, not_="'lâ yu'zenu lehum' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 37: dict(kademe=None, olgu=False, cipa=False, not_="'veylun yevme'izin' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 38: dict(kademe=None, olgu=False, cipa=False, not_="'yevmu'l-fasl, cema'nâkum' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 39: dict(kademe=None, olgu=False, cipa=False, not_="'fe-kîdûn' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 40: dict(kademe=None, olgu=False, cipa=False, not_="'veylun yevme'izin' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 41-50
 41: dict(kademe=None, olgu=False, cipa=False, not_="'fî zılâlin ve 'uyûn' — cennet, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 42: dict(kademe=None, olgu=False, cipa=False, not_="'fevâkihe mimmâ yeştehûn' — cennet (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 43: dict(kademe=None, olgu=False, cipa=False, not_="'kulû veşrabû henî'en' — cennet (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 45: dict(kademe=None, olgu=False, cipa=False, not_="'veylun yevme'izin' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 46: dict(kademe=None, olgu=False, cipa=False, not_="'kulû ve temetta'û qalîlen' — dünya geçimliği, tehdit (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 47: dict(kademe=None, olgu=False, cipa=False, not_="'veylun yevme'izin' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 48: dict(kademe=None, olgu=False, cipa=False, not_="'irke'û lâ yerke'ûn' — dünya davranışı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 49: dict(kademe=None, olgu=False, cipa=False, not_="'veylun yevme'izin' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: e_oto 0 token; KARAR değişmedi (683); bilanço esma_muhur_43 [], geçerli []",
  "kök tablosu: yeni kök yok (ölçüm kök alanında '???' yok); 1478; kok_ekle_77 boş liste; retroaktif yama: hedef listesi 0 ayet, hedefli yama 0, genel geçiş 0",
  "harf alanı: ayet 1 ölçümünde harf 32 → harf3 12, isaret 0 (ayet 1 ailesi; besmele); araç alanı (924); KAPATILAMAZ",
  "yıldız (924): 77:7, 8, 9, 10 ★★★ pas z=5,38 (kısa tek fiilli edilgen) — formül davranışı, içerik iddiası değil; öbür 6 ayet yıldızsız",
  "fâsıla: 76:31 ا → 77:1 ا; 77:1-6 ا, 77:7 ع, 77:8-10 ت (ölçüm); sınıf geçişleri 77:6 → 7 ve 77:7 → 8 işaretsiz — ölçüm kafiye kırığı 0 (924)",
  "yemin biçimi (924): ölçüm QASEM yalnız 77:1'de; 77:2-5 'fe' / 've' ile atıflı yeminler biçim alanında boş (okuma, ◈D)",
  "adsız gönderge (1017): 77:1-5 yemin edilenler ('el-murselât', 'el-'âsifât', 'en-nâşirât', 'el-fâriqât', 'el-mulqiyât') adsız — tek topluluk mu, ayrı mı, ne oldukları KAPATILAMAZ; yemin eden ve 77:7 vaat eden adsız; 2MP muhatap adsız",
  "okuma ikiliği: 77:1 ''urfâ' (art arda / iyilikle) ve 77:6 ''uzran ev nuzrâ' i'râbı (mef'ûl leh / bedel) KAPATILAMAZ; 77:8-10 şart dizisinin cevabı blok dışında (henüz okunmadı)",
  "gloss (1021 ailesi): عرف 77:1 ''urf' (art arda / iyilik) — gloss 'tanıma'; نشر gloss iki anlam ('yayma, açma; diriltme') birlikte",
  "ölçüm iltifât (tanım): 77:1-6 sahset boş; 77:7 {} → {2} iltifât 0; 77:8 {2} → {3} iltifât 1",
  "aday 1040 (kayıt): 76:31 / 77:1 sûre sınırı — rahmet / hazırlanmış azapla kapanış (lafız zamirle) / lafızsız yeminle açılış; fâsıla ا → ا; ardışık üç sûrenin açılışı: 75:1 yemin, 76:1 soru, 77:1 yemin",
  "bağ: esit2, nakarat3, xref blokta boş; kalıp eşleri okumayla (20:105, 21:81, 36:66, 37:1-3, 50:6, 51:1-6, 52:7, 54:37); 81:3, 81:11 henüz okunmadı",
  "◈K / ◈B: 77:8 نجم, 77:9 سمو 'semâ'', 77:10 جبل tetik — satır dolu; ◈B tetik yok",
  "çıpa: 77:8-10 L1 olgu=True (75:8-9 emsali); 77:1-5 gönderge kapatılamadığı için merdiven uygulanmadı; 77:7 olgu=False",
  "süreç: sûre 77 dosyaları insan_* şablonlarından kuruldu; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 17 sayım 0 uyuşmaz",
 ],
 (11, 20): [
  "esmâ: e_oto 2 token (77:16:3 'evvel' — 'el-evvelîn'; 77:17:3 'âxir' — 'el-âxirîn'); ikisi de DEĞİL (topluluklar); KARAR 683 → 685; esma_kayit 'mühür EVET' ikisinde (ölçüm konumu); 77:17 ölçüm satırı 'MÜHÜRSÜZ' — ayrışma (1022); bilanço esma_muhur_43 [16, 17], geçerli []",
  "kök tablosu: yeni kök yok; 1478; retroaktif yama: hedef listesi 0 ayet, hedefli yama 0, genel geçiş 0",
  "yıldız (924): 77:11, 77:12 ★★★ pas z=5,38 (kısa tek fiilli edilgen) — formül davranışı, içerik iddiası değil; öbür 8 ayet yıldızsız",
  "fâsıla: 77:11-12 ت, 77:13-14 ل, 77:15-20 ن (ölçüm); sınıf geçişleri 77:12 → 13 ve 77:14 → 15 işaretsiz — ölçüm kafiye kırığı 0 (924)",
  "nakarat (ölçüm): 77:15 / 77:19 'veylun yevme'izin li'l-mukezzibîn' — nakarat3 GEÇER, esit2 TAM; sûre içi 10 ayet (77:15-49), korpusta + 83:10 = 11; önekli 52:11 ile 12; sûre içi geçişlerin 8'i henüz okunmadı",
  "şart cevabı: 77:8-11 dört 'izâ' — cevap metinde açık değil (77:12-13 soru / cevap ya da 77:15 nakaratı); KAPATILAMAZ",
  "adsız gönderge (1017): vakit belirleyen / erteleyen (77:11-12 edilgen), 77:12 fail 3FS, konuşan 1P (77:16-20), muhatap 2MS (77:14) ve 2MP (77:20), yalanlayanlar, öncekiler / sonrakiler, suçlular adsız",
  "ölçüm iltifât (tanım): 77:13, 15, 19 şahıssız; 77:16 1P girişi iltifât 1; 77:14 {} → {2, 3} ve 77:20 {} → {1, 2} iltifât 0 (önceki ayet şahıssız) (924)",
  "esit2: 77:18 → 37:34 BENZER 0,9189 ('innâ' farkı); 77:15 / 19 TAM (nakarat)",
  "biçim (924): 77:15 / 19 beddua ('veyl') biçim alanında yok",
  "aday 1041 ailesi (sûre dışı, kayıt değil): 'evvel / âxir' 57:3 Allah / 77:16-17 topluluklar",
  "bağ: kalıp eşleri okumayla (32:8, 37:21, 37:34, 44:40, 52:11, 56:13-14, 57:3, 69:3, 74:27); 78:17, 83:10 ve 'mâ edrâke mâ' kalıbının 9 eşi henüz okunmadı",
  "◈K / ◈B: 77:12 يوم أجل, 77:13, 14, 15, 19 يوم, 77:20 موه tetik — ◈K dolu; 77:20 خلق ◈B dolu; 'su' kozmik değil (okuma)",
  "çıpa: 77:20 L1 olgu=True (76:2 emsali; 32:8 ile ara aşama farkı); 77:16-18 tarih anlatısı, merdiven uygulanmadı; 77:11-15, 19 olgu=False",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 24 sayım 0 uyuşmaz",
 ],
 (21, 30): [
  "esmâ: e_oto 1 token (77:26:1 'hayy' — 'ahyâ'en', diriler); DEĞİL; KARAR 685 → 686; esma_kayit 'mühür EVET' (ölçüm konumu); bilanço esma_muhur_43 [26], geçerli []",
  "kök tablosu: kok_ekle_77 2 kök (كفت 77:25, شمخ 77:27; ölçüm kök alanında '???' → eklendi); 1478 → 1480; retroaktif yama: hedef listesi 0 ayet, hedefli yama 0, genel geçiş 0 (ikinci koşu da 0)",
  "hapaks (yeni kök dersi): 77:25 كفت, 77:27 شمخ ★★★ hapaks z=3,28 — yeni köklerin tek ayeti; içerik iddiası değil; öbür 8 ayet yıldızsız",
  "fâsıla: 77:21 ن, 77:22 م (ölçüm N sınıfı), 77:23-24 ن, 77:25-27 ا, 77:28-29 ن, 77:30 ب; sınıf geçişleri işaretsiz — ölçüm kafiye kırığı 0 (924)",
  "nakarat (ölçüm): 77:24, 77:28 — sûre içi 3. ve 4. geçiş; nakarat3 GEÇER, esit2 TAM",
  "sayı işareti: 77:30 'selâs' — gerçek sayı (üç kol)",
  "adsız gönderge (1017): konuşan 1P (77:21-27), muhatap 2MP; 77:29-30 emirlerin sahibi adsız, söz işaretsiz ('yuqâlu' yok) — meal tırnaksız; 77:29 'mâ' adsız",
  "okuma ikiliği: 77:23 'qadernâ' (takdir / kudret) ve 77:26 i'râbı (meful / hâl / bedel) KAPATILAMAZ; 77:21 'hu' göndergesi en yakın eril ad (su) — okuma",
  "gloss (1021 ailesi): ظلل 77:30 'zıll' (gölge) — gloss 'sürüp gitme'; قدر gloss iki anlam ('ölçü, güç yetirme') birlikte — 77:23 ikiliği gloss'ta da var",
  "ölçüm iltifât (tanım): bu blokta 0; 77:27 {} → {1, 2, 3} ve 77:29 {} → {2, 3} (önceki ayet şahıssız) (924)",
  "biçim (924): 77:23 övgü 'ni'me', 77:24 / 28 beddua biçim alanında yok",
  "bağ: kalıp eşleri okumayla (15:21, 15:22, 23:13, 25:53, 32:20, 35:22, 37:21, 51:48, 56:43-44, 72:16); 78:6, 83:17 henüz okunmadı",
  "◈K / ◈B: 77:24, 28 يوم, 77:25 أرض, 77:27 موه ◈K dolu; 77:26 حيي موت ◈B dolu; 77:27 'ravâsî' (رسو) tetik listesinde değil — gözlem ◇'de; 77:23 نعم 'ni'me' S1 kısıtıyla tetiklemiyor",
  "çıpa: 77:21, 22, 25, 26, 27 L1 olgu=True (77:22 birimsiz ölçü — L4 sınır vakası, L4 değil); 77:24, 28-30 olgu=False",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 30 sayım 0 uyuşmaz; kayıttan önce 77:23'te 51:48 alıntısındaki yazım ('ferasnâhâ' → 'feraşnâhâ') düzeltildi",
 ],
 (31, 40): [
  "esmâ: e_oto 1 token (77:38:5 'evvel' — 've'l-evvelîn'); DEĞİL; KARAR 686 → 687; esma_kayit 'mühür EVET' (ölçüm konumu); bilanço esma_muhur_43 [38], geçerli []",
  "kök tablosu: kok_ekle_77 1 kök (لهب 77:31; ölçüm kök alanında '???' → eklendi); 1480 → 1481; retroaktif yama: hedef listesi 0 ayet, hedefli yama 0, genel geçiş 0 (ikinci koşu da 0)",
  "yıldız (924): 77:36 ★★ pas z=2,52 — formül davranışı, içerik iddiası değil; öbür 9 ayet yıldızsız",
  "fâsıla: 77:31 ب, 77:32-33 ر, 77:34-40 ن (ölçüm); geçişler 77:31 → 32 ve 77:33 → 34 işaretsiz — ölçüm kafiye kırığı 0 (924)",
  "nakarat (ölçüm): 77:34, 37, 40 — sûre içi 5., 6., 7. geçiş; nakarat3 GEÇER, esit2 TAM; kalan üç geçiş (77:45, 47, 49) henüz okunmadı",
  "konuşan katmanı (924 / 1017): 77:38 1P → 77:39 1S ('kîdûn(î)') — sahset ikisini '1' sayıyor, iltifât 0; konuşan adsız; 77:29-33 adsız ses, 77:35-36 adsız ses",
  "adsız gönderge (1017): 77:32 'innehâ' 3FS (ateş / alev; 'leheb' eril) KAPATILAMAZ; izin veren (77:36 edilgen) adsız; 3MP yalanlayanlar, öncekiler adsız",
  "okuma ikiliği: 77:36 'fe-ya'tezirûn' i'râbı (atıf, sebebiyye değil) KAPATILAMAZ — meal amaç / sonuç okumasıyla",
  "gloss (1021 ailesi): شرر 77:32 'şerer' (kıvılcım) — gloss 'şer, kötülük' (76:7, 76:11 ile ardışık sûrede iki anlam); ظلل 77:31 'zalîl' — gloss 'sürüp gitme'; جمل gloss üç anlam birlikte (burada deve)",
  "biçim (924): 77:32 benzetme 'ke'l-qasr', 77:33 'ke-enne' biçim alanında yok; 77:35 ve 77:38 biçim DIKKAT işaretli (işaret + 'yevm')",
  "ölçüm iltifât: 77:31 {2} → {3} 1; 77:38 {3} → {1, 2} 1",
  "bağ: kalıp eşleri okumayla (11:55, 16:84, 27:85, 37:20, 37:21, 52:46, 56:44, 56:49-50, 66:7); sûre içi 77:6 / 36 عذر, 77:16 / 38 'evvel', 77:13-14 / 38 'yevmu'l-fasl', 77:30 / 31 gölge",
  "◈K / ◈B: 77:34, 35, 37, 38, 40 يوم ◈K dolu; ◈B tetik yok (جمل deve, أذن tetik listesinde değil)",
  "çıpa: blokun on ayeti olgu=False (âhiret; 77:32-33 benzetme araçları); tarayıcı aday vermedi",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 24 sayım 0 uyuşmaz; oturum ertesi güne taştı (2026-10-28) — çalışma ağacı ve taban 0593b8e değişmedi",
 ],
 (41, 50): [
  "esmâ: e_oto 0 token; KARAR değişmedi (687); bilanço esma_muhur_43 [], geçerli []",
  "kök tablosu: yeni kök yok; 1481; retroaktif yama: hedef listesi 0 ayet, hedefli yama 0, genel geçiş 0",
  "yıldız (924): 77:48 ★ pas z=1,57 — formül davranışı, içerik iddiası değil; öbür 9 ayet yıldızsız",
  "fâsıla: 77:41-50 hepsi ن (ölçüm); kafiye kırığı 0",
  "nakarat (ölçüm): 77:45, 47, 49 — sûre içi 8., 9., 10. (son) geçiş; on geçişin hepsi basıldı; aralıklar 3, 4, 3, 5, 2, 2, 4, 1, 1 ayet (okuma sayımı)",
  "esit2: 77:43 → 52:19 TAM (iki sûrede özdeş ayet); 77:44 → sûre 37'de üç TAM, bir BENZER eş ('innâ kezâlike neczi'l-muhsinîn'); xref 77:43 → 69:24, 77:50 → 45:6 (basıldı), 7:185 (henüz okunmadı)",
  "sayı işareti: 77:46 'qalîl' — miktar / süre azlığı, sayı değil (yanlış pozitif, 924)",
  "adsız gönderge (1017): 77:43 ve 77:46 emirlerinin söyleyeni adsız, söz işaretsiz (meal tırnaksız); 77:48 'qîle' söyleyeni adsız (alıntı işaretli); 77:44 konuşan 1P adsız; 77:50 'ba'dehû' göndergesi KAPATILAMAZ",
  "ölçüm iltifât: 77:43 {3} → {2}, 77:44 {2} → {1}, 77:46 {1} → {2} — üçü 1; 77:46'da muhatap topluluğu değişiyor (sakınanlar → suçlular), sahset bunu ayırmıyor (924)",
  "gloss (1021 ailesi): ظلل 77:41 'zılâl' — gloss 'sürüp gitme' (sûre içi üç geçişte de)",
  "aday 1039 (okuma): ayetler arası çiftler — 77:30-31 / 77:41 (azap gölgesi / sakınanların gölgeleri), 77:43 / 77:46 ('kulû' afiyetle / biraz), 77:18 / 77:44 (mucrimîn / muhsinîn); ayet içi 77:48 (emir / ret)",
  "bağ: kalıp eşleri okumayla (15:3, 37:34, 37:80, 45:6, 51:15, 52:19, 52:22, 69:24); 7:185 henüz okunmadı",
  "◈K / ◈B: 77:45, 47, 49 يوم ◈K dolu; 77:41 عين ('uyûn', pınar) ◈B dolu",
  "çıpa: blokun on ayeti olgu dışı (cennet / âhiret / dünya davranışı); tarayıcı aday vermedi",
  "süreç: tetik ön kuru koşu 0 uyuşmaz (blok ve sûre geneli 50 ayet); oturum_xy 31 sayım 0 uyuşmaz (sûre geneli 126 / 0); kayıttan önce 77:44 ve 77:42'de basılmamış okunmuş ayet numaraları (sûre 37'den üç, 56:21) liste üyesi olarak yazılmıştı — sayıya çevrildi",
 ],
}

DUZELTME = {
}
