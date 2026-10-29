# -*- coding: utf-8 -*-
"""nebe_kayit.py — sûre 78 (Nebe') okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 78

CIPA = {
 # blok 1-10
 6: dict(kademe='L1', olgu=True, cipa=False, not_="'e-lem nec'ali'l-arda mihâdâ' — yer + işlev (döşek); mekanizma yok — L1 (77:25 emsali); tarayıcı vermedi"),
 7: dict(kademe='L1', olgu=True, cipa=False, not_="'ve'l-cibâle evtâdâ' — dağlar + işlev; 'kazık' benzetme aracı (olgu sayılmaz); mekanizma yok — L1; tarayıcı vermedi"),
 8: dict(kademe='L1', olgu=True, cipa=False, not_="'ve xalaqnâkum ezvâcâ' — yaratma + nitelik (çift); aşama / mekanizma yok — L1; tarayıcı vermedi"),
 9: dict(kademe='L1', olgu=True, cipa=False, not_="'ve ce'alnâ nevmekum subâtâ' — uyku + işlev (dinlenme / kesilme); mekanizma yok — L1; tarayıcı vermedi"),
 10: dict(kademe='L1', olgu=True, cipa=False, not_="'ve ce'alne'l-leyle libâsâ' — gece (nesne, zaman zarfı değil) + işlev; 'örtü' benzetme aracı; mekanizma yok — L1; tarayıcı vermedi"),
 # blok 11-20
 11: dict(kademe='L1', olgu=True, cipa=False, not_="'ve ce'alne'n-nehâra me'âşâ' — gündüz + işlev (geçim); mekanizma yok — L1; tarayıcı vermedi"),
 12: dict(kademe=None, olgu=False, cipa=False, not_="'ve beneynâ fevqakum seb'an şidâdâ' — sayılan şey adlanmıyor, gönderge KAPATILAMAZ; merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'sirâcen vehhâcâ' — kandil adsız (71:16'da güneşin yüklemi), gönderge KAPATILAMAZ; merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe='L1', olgu=True, cipa=False, not_="'mine'l-mu'sırâti mâ'en theccâcâ' — su + kaynak + nitelik; 78:15 ile zincir — L1; tarayıcı vermedi"),
 15: dict(kademe='L2', olgu=True, cipa=False, not_="'li-nuxrice bihî habben ve nebâtâ' — ta'lîl lâmı + 'bihî': su → tane ve bitki, nedensel bağ (50:9 emsali) — L2; ölçü / mekanizma yok; tarayıcı v4 adayı, çıpa değil"),
 16: dict(kademe='L1', olgu=True, cipa=False, not_="'ve cennâtin elfâfâ' — bahçeler + nitelik, 78:15 zincirinin son halkası — L1; tarayıcı vermedi"),
 17: dict(kademe=None, olgu=False, cipa=False, not_="'inne yevme'l-fasli kâne mîqâtâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 18: dict(kademe=None, olgu=False, cipa=False, not_="'yevme yunfaxu fi's-sûr' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 19: dict(kademe='L1', olgu=True, cipa=False, not_="'ve futihati's-semâ'u fe-kânet ebvâbâ' — âhiretteki kozmik olay: gök + süreç (açılma); 'kapılar' benzetme aracı — L1; tarayıcı vermedi"),
 20: dict(kademe='L1', olgu=True, cipa=False, not_="'ve suyyirati'l-cibâlu fe-kânet serâbâ' — âhiretteki kozmik olay: dağlar + süreç (yürütülme); 'serap' benzetme aracı — L1; tarayıcı vermedi"),
 # blok 21-30
 21: dict(kademe=None, olgu=False, cipa=False, not_="'inne cehenneme kânet mirsâdâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 22: dict(kademe=None, olgu=False, cipa=False, not_="'li't-tâğîne me'âbâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 23: dict(kademe=None, olgu=False, cipa=False, not_="'lâbithîne fîhâ ahqâbâ' — âhiret; süre adı birimsiz (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 24: dict(kademe=None, olgu=False, cipa=False, not_="'lâ yezûqûne fîhâ berden ve lâ şerâbâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 25: dict(kademe=None, olgu=False, cipa=False, not_="'illâ hamîmen ve ğassâqâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 26: dict(kademe=None, olgu=False, cipa=False, not_="'cezâ'en vifâqâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 27: dict(kademe=None, olgu=False, cipa=False, not_="'lâ yercûne hisâbâ' — dünya davranışı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 28: dict(kademe=None, olgu=False, cipa=False, not_="'kezzebû bi-âyâtinâ kizzâbâ' — dünya davranışı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 29: dict(kademe=None, olgu=False, cipa=False, not_="'kulle şey'in ahsaynâhu kitâbâ' — sayma / yazma, olgu değil (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 30: dict(kademe=None, olgu=False, cipa=False, not_="'fe-zûqû … illâ 'azâbâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 31-40
 31: dict(kademe=None, olgu=False, cipa=False, not_="'inne li'l-muttaqîne mefâzâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 32: dict(kademe=None, olgu=False, cipa=False, not_="'hadâ'iqa ve a'nâbâ' — cennet (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 33: dict(kademe=None, olgu=False, cipa=False, not_="'kevâ'ibe etrâbâ' — cennet (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 34: dict(kademe=None, olgu=False, cipa=False, not_="'ke'sen dihâqâ' — cennet (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 35: dict(kademe=None, olgu=False, cipa=False, not_="'lâ yesme'ûne fîhâ lağven' — cennet (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 36: dict(kademe=None, olgu=False, cipa=False, not_="'cezâ'en min rabbike' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 37: dict(kademe='L0', olgu=True, cipa=False, not_="'rabbi's-semâvâti ve'l-ardi ve mâ beynehumâ' — gökler, yer, ikisinin arası Rab tamlamasında; süreç yok — L0 (44:7, 37:5 emsali); tarayıcı vermedi"),
 38: dict(kademe=None, olgu=False, cipa=False, not_="'yevme yeqûmu'r-rûhu ve'l-melâ'iketu saffâ' — rûh ve melekler gaybî (olgu=False; 70:4 emsali); merdiven uygulanmadı; tarayıcı vermedi"),
 39: dict(kademe=None, olgu=False, cipa=False, not_="'zâlike'l-yevmu'l-haqq … me'âbâ' — âhiret / seçim (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 40: dict(kademe=None, olgu=False, cipa=False, not_="'yevme yenzuru'l-mer'u … kuntu turâbâ' — âhiret; 'turâb' dilek içinde (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: e_oto 0 token (78:2 'azîm' haberi niteliyor — otomatik süzgeç vermedi); KARAR değişmedi (687); bilanço esma_muhur_43 [], geçerli []",
  "kök tablosu: yeni kök yok (ölçüm kök alanında '???' yok); 1481; kok_ekle_78 boş liste; retroaktif yama: hedef listesi 0 ayet, hedefli yama 0, genel geçiş 0",
  "harf alanı: ayet 1 ölçümünde harf 29 → harf3 10, isaret 0 (ayet 1 ailesi; besmele); araç alanı (924); KAPATILAMAZ",
  "yıldız: blokun on ayeti yıldızsız",
  "fâsıla: 77:50 ن → 78:1 ن; 78:1 ن, 78:2 م, 78:3-5 ن, 78:6-10 ا (ölçüm); sınıf geçişi 78:5 → 6 işaretsiz — ölçüm kafiye kırığı 0 (924)",
  "biçim (924): 78:1-2 soru-cevap ('amme / 'ani) biçim alanında yok; 78:4-5 KELLA var",
  "sayı işareti: 78:8 'ezvâc' (زوج) — çoğul, sayı değeri yok; yanlış pozitif (924)",
  "adsız gönderge (1017): 78:1-5 soruşanlar / ayrılığa düşenler 3MP adsız; soran ve cevap veren ses adsız; 78:6-10 konuşan 1P adsız; 78:8-9 muhatap 2MP adsız; 77:50 ve 78:1 3MP'lerinin aynı topluluk olup olmadığı KAPATILAMAZ",
  "okuma ikiliği: 78:8 'ezvâc' (çift / eş / tür) KAPATILAMAZ; 78:3 ayrılığın konusu metinde yok",
  "ölçüm iltifât (tanım): 78:6 {3} → {1} iltifât 1; 78:8 {1} → {1, 2} iltifât 0 (kısmi örtüşme, 924)",
  "aday 1040 (kayıt): 77:50 / 78:1 sûre sınırı — soruyla kapanış / soruyla açılış, 3MP → 3MP, fâsıla ن → ن, 'hadîs' / 'nebe''; ardışık sûrede aynı kurgu 77:25 / 78:6 ('e-lem nec'ali'l-arda' + nekre işlev)",
  "bağ: esit2, nakarat3 blokta boş; xref 78:10 → 25:47 (basıldı); kalıp eşleri okumayla (17:12, 25:47, 38:12, 38:67, 51:8, 74:40, 77:25); 89:10, 90:8 henüz okunmadı",
  "◈K / ◈B: 78:6 أرض, 78:7 جبل, 78:10 ليل ◈K dolu; 78:8 خلق زوج ◈B dolu; 78:9 'nevm' (uyku) tetik listesinde değil — gözlem ◇'de",
  "çıpa: 78:6-10 L1 olgu=True (yer, dağlar, çift yaratma, uyku, gece — işlev adlanıyor, mekanizma yok; 'kazık' ve 'örtü' benzetme araçları olgu sayılmaz); 78:1-5 olgu dışı; tarayıcı aday vermedi",
  "süreç: sûre 78 dosyaları murselat_* şablonlarından kuruldu; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 20 sayım 0 uyuşmaz",
 ],
 (11, 20): [
  "esmâ: e_oto 0 token; KARAR değişmedi (687); bilanço esma_muhur_43 [], geçerli []",
  "kök tablosu: kok_ekle_78 2 kök (وهج 78:13, ثجج 78:14; ölçüm kök alanında '???' → eklendi); 1481 → 1483; retroaktif yama: hedef listesi 0 ayet, hedefli yama 0, genel geçiş 0 (ikinci koşu da 0); ثجج gloss'undaki çeviriyazı kayıttan önce düzeltildi",
  "hapaks (yeni kök dersi): 78:13 وهج, 78:14 ثجج ★★★ hapaks z=3,28 — yeni köklerin tek ayeti; içerik iddiası değil",
  "yıldız (924): 78:18, 19, 20 ★★ pas z=2,52 (edilgen 1/2) — formül davranışı, içerik iddiası değil; öbür 5 ayet yıldızsız",
  "fâsıla: 78:11-20 hepsi ا (ölçüm); kafiye kırığı 0",
  "sayı işareti: 78:12 'seb'' — gerçek sayı; sayılan şey adlanmıyor",
  "gloss (1021 ailesi): نهر 78:11 'nehâr' (gündüz) — gloss 'ırmak'; حبب 78:15 'habb' (tane) — gloss 'sevgi'; عصر gloss 'yağmur bulutu (mu'sırât)' metnin adlamadığı göndergeyi adlıyor",
  "adsız gönderge (1017): 78:12 sayılan 'yedi', 78:13 'sirâc', 78:14 'el-mu'sırât' adlanmıyor — KAPATILAMAZ; 78:18-20 üfleyen / açan / yürüten adsız (edilgen); 2MP muhatap adsız",
  "biçim (924): 78:15 ta'lîl lâmı biçim alanında yok (tarayıcı B_ta'lîl ailesinden yakaladı); 78:17 'inne' tekidi kip alanında yok",
  "ölçüm iltifât: bu blokta 0; 78:16 şahıssız, 78:17 {} → {3} (önceki ayet şahıssız); 1P'den anlatıcı 3MS'ye geçiş (78:15 → 78:17) ölçümde görünmüyor (924)",
  "aday 1040 (kayıt): ardışık sûrede gök + dağ ikilisi edilgenle — 77:9-10 / 78:19-20; 'yevmu'l-fasl' 77:13, 14, 38 / 78:17",
  "aday 1039 (okuma): ayetler arası 78:10 / 78:11 (gece / gündüz, örtü / geçim), 78:7 / 78:20 (dağlar: kazık / serap)",
  "bağ: xref 78:17 → 37:21 (basıldı); kalıp eşleri okumayla (12:48, 18:47, 20:102, 23:17, 24:39, 44:40, 50:9, 71:16, 77:9-10, 77:13-14, 77:38); 6:73 henüz okunmadı",
  "◈K / ◈B: 78:11 نهر, 78:14 موه, 78:17-18 يوم, 78:19 سمو, 78:20 جبل ◈K dolu; 78:15 نبت ◈B dolu; 78:12 سبع / بني ve 78:13 سرج tetik listesinde değil — gözlem ◇'de",
  "çıpa: 78:15 L2 olgu=True (tarayıcı v4 adayı, çıpa değil — L4 yok); 78:11, 14, 16, 19, 20 L1 olgu=True; 78:12-13 gönderge KAPATILAMAZ, merdiven uygulanmadı; 78:17-18 olgu=False",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 36 sayım 0 uyuşmaz; kayıttan önce 78:17'de basılmamış okunmuş ayetler (77:13, 14, 38) liste üyesi olarak yazılmıştı — emsal olarak basıldı",
 ],
 (21, 30): [
  "esmâ: e_oto 0 token; KARAR değişmedi (687); bilanço esma_muhur_43 [], geçerli []",
  "kök tablosu: yeni kök yok (ölçüm kök alanında '???' yok); 1483; retroaktif yama: hedef listesi 0 ayet, hedefli yama 0, genel geçiş 0",
  "yıldız: blokun on ayeti yıldızsız",
  "fâsıla: 78:21-30 hepsi ا (ölçüm); kafiye kırığı 0",
  "biçim (924): 78:25 ISTISNA, 78:30 HASR var; 78:21 ve 78:27 'inne' tekidi kip alanında yok; 78:29 mefulün öne alınması biçim alanında yok",
  "ölçüm iltifât (tanım, 924): bu blokta 0; 78:28 {3} → {1, 3} (1P iyelik girişi) ve 78:30 {1, 3} → {1, 2} (3MP anlatıdan 2MP hitaba geçiş) kısmi örtüşme — iltifât sayılmıyor",
  "konuşan katmanı (1017): 78:21-27 anlatıcı sesi; 78:28-29 1P; 78:30 1P doğrudan 2MP'ye, söz işaretsiz — meal tırnaksız; konuşan ve muhatap adsız",
  "adsız gönderge (1017): 'et-tâğîn' adsız topluluk; 78:21 'mirsâd' neyi / kimi gözetliyor KAPATILAMAZ; 78:26 karşılık veren adsız",
  "okuma ikiliği: 78:22 ve 78:26 i'râbı (bedel / ikinci haber; mef'ûl mutlak / hâl) KAPATILAMAZ; 78:23 'ahqâb' — süre birimsiz, sınırlı / sınırsız KAPATILAMAZ",
  "gloss (1021 ailesi): غسق gloss iki anlam birlikte ('gecenin karanlığı' / 'gassâk'); burada ikincisi",
  "aday 1039 (okuma): ayetler arası 78:24 / 78:25 ('berd' / 'hamîm'), 78:24 / 78:30 ('lâ yezûqûne' / 'fe-zûqû')",
  "aday 1041: kayıt yok (lafız / Rab yok; 'ahsâ' yalnız 1P)",
  "bağ: xref 78:29 → 36:12 (basıldı); kalıp eşleri okumayla (21:69, 22:57, 30:16, 38:55, 38:57, 44:56, 72:28); sûre içi 78:17 / 78:21 iskeleti",
  "◈K / ◈B: tetik yok — on ayette iki satır da '—'; 78:23 حقب (süre adı) ve 78:24 ذوق / شرب tetik listesinde değil — gözlem ◇'de",
  "çıpa: blokun on ayeti olgu=False (âhiret / dünya davranışı / sayma); tarayıcı aday vermedi",
  "süreç: oturum ertesi güne taştı (2026-10-29) — çalışma ağacı, okuma_metni['78'] 20 anahtar ve ilerleme 4484 doğrulandı, taban 7d5e727 değişmedi; tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 25 sayım 0 uyuşmaz; kayıttan önce 78:24'te 44:56 için basılmamış bağlamdan nitelik ('sakınanlar', 'cennet') yazılmıştı — basılan metne indirildi",
 ],
 (31, 40): [
  "esmâ: e_oto 3 token (78:37:6 'rahmân', 78:38:12 'rahmân', 78:40:4 'qarîb'); kararlar: iki 'rahmân' İLÂHÎ, 'qarîb' DEĞİL (azabın sıfatı); KARAR 687 → 690; bilanço esma_muhur_43 [37, 38], geçerli [37, 38]",
  "esmâ / mühür (1022): ölçüm satırı 78:37 'ORTA, MÜHÜRSÜZ', 78:38 'SON, MÜHÜRSÜZ' — bilanço ikisini geçerli sayıyor; 78:38 'sevâbâ' ile bitiyor, 'er-rahmân' son token değil — mühür iddiası bilançodan, konum metinden",
  "kök tablosu: kok_ekle_78 2 kök (كعب 78:33, دهق 78:34; ölçüm kök alanında '???' → eklendi); 1483 → 1485; كعب gloss'una okunmamış ayet numarası yazılmadı (4 ayet); retroaktif yama: 'daha önce okunmuş' çıktısı 3 ayet — kök كعب'ın sûre 5 ayetleri, okuma_metni'nde kayıt yok, atlandı; hedefli yama 0, genel geçiş 0 (ikinci koşu da 0)",
  "hapaks (yeni kök dersi): 78:34 دهق ★★★ hapaks z=3,28 — içerik iddiası değil; 78:33 كعب korpusta 4 ayet, hapaks değil",
  "yıldız (924): 78:36 ★★★ rab z=3,94, 78:39 ★★ rab z=2,05, 78:37 ★ rab z=1,81 — lafızsız ayette Rab formül davranışı; içerik iddiası değil; öbür 6 ayet yıldızsız",
  "fâsıla: 78:31-40 hepsi ا (ölçüm); sûrenin 40 ayetinde fâsıla: 78:1 ن, 78:2 م, 78:3-5 ن, 78:6-40 ا; kafiye kırığı 0",
  "gloss (1021 ailesi): ترب gloss 'toprak' — 78:33 'etrâb' (yaşıt) için uymuyor; حسب gloss 'hesap, sayma' — 78:36 'hisâbâ' (yeterli) için uymuyor",
  "◈K / ◈B tetik: 78:38 روح — S1 kısıtıyla 'rûh' tetiklemiyor, gözlem ◇'de; 78:35 سمع ◈B tetik — ilk taslakta satır '—' yazılmıştı, tetik ön kuru koşusu yakaladı, kayıttan önce dolduruldu; 78:32 عنب tetik listesinde değil",
  "ölçüm iltifât: 78:35 {1, 2} → {3}, 78:36 {3} → {2} (sûrede ilk 2MS 'rabbike'), 78:37 {2} → {3} — üçü 1; 78:40'ta 1P + 2MP + alıntı içi 1S tek ayette — sahset kümesi ['1', '2', '3'], alıntı sınırı ölçümde yok (924)",
  "konuşan katmanı (1017): 78:31-39 anlatıcı sesi (78:36'da 2MS'ye); 78:40 1P → 2MP; 'el-kâfir'in sözü 'yeqûlu' ile işaretli — meal tek tırnakla; 'el-mer'', 'el-kâfir', izin verilen, 3MP adsız",
  "adsız gönderge (1017): 78:38 'er-rûh' ne olduğu KAPATILAMAZ; 78:37 'lâ yemlikûne' öznesi adsız",
  "aday 1039 (okuma): ayetler arası 78:22 / 78:31 (azgınlar / sakınanlar), 78:24 / 78:35 ('lâ … fîhâ … ve lâ' iskeleti), 78:24 / 78:34 (içecek yok / dopdolu kadeh), 78:26 / 78:36 (cezâ'), 78:28 / 78:35 (kizzâb), 78:22 / 78:39 (me'âb); ayet içi 78:37 gökler / yer",
  "aday 1041: kayıt yok — 'şâ'e', 'ezine', 'qâle' sûre içinde Allah ile insan arasında bölünmüyor",
  "aday 1040: 78:40 → 79:1 sûre sınırı — 79:1 henüz okunmadı, kayıt sûre 79'un ilk bloğunda",
  "bağ: xref 78:40 → 28:47 (basıldı); kalıp eşleri okumayla (19:62, 20:109, 37:5, 38:52, 44:7, 56:25, 56:37, 68:34, 69:25, 70:4, 73:19, 76:29)",
  "çıpa: 78:37 L0 olgu=True (Rab tamlaması); öbür 9 ayet olgu=False (cennet / âhiret / gaybî); tarayıcı aday vermedi",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz (ilk taslakta 1 — yukarıda); sûre geneli tetik 40 ayet 0 uyuşmaz; oturum_xy blokta 50, sûre geneli 131 sayım, 0 uyuşmaz",
 ],
}

DUZELTME = {
 38: dict(alan='mercek', eski="70:4'te melekler önce, yükseliş; burada rûh önce, saf saf durma (okuma)",
          dogru="Eksik gözlem (kullanıcı sorusuyla, kayıttan sonra): 'er-rûh' tekil, 'el-melâ'ike' çoğul (morph M / MP). Lemma 'rûh' korpusta 21 geçişin 21'i tekil (çoğul biçim yok); lemma 'melek' 136 geçiş: çoğul 102, tekil 32, ikil 2. Fiil öznelerden önce ve tek: 78:38 'yeqûmu' 3MS — ilk özne 'er-rûh' (tekil eril) ile uyumlu; 70:4 'ta'ruju' 3FS — ilk özne 'el-melâ'ike' (kırık çoğul) ile uyumlu; iki ayette de fiil öndeki ada uyuyor, sıra değişince şahıs değişiyor (okuma). 'saffâ' tekil mastar iki özneye birden: rûh meleklerle aynı safta mı ayrı mı KAPATILAMAZ; ardından 'lâ yetekellemûne' 3MP — rûh'un konuşamayanlara dahil olup olmadığı KAPATILAMAZ (1017). Rûh ve melek aynı ayette korpusta 4: 70:4, 78:38, okunmuş 1 ayet daha, 97:4 (henüz okunmadı). Ölçüm satırı özne sayısını ve fiil-özne uyumunu göstermiyor (924). Özgün alan korunur.",
          aday=1017, blok='31-40'),
}
