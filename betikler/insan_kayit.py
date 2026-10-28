# -*- coding: utf-8 -*-
"""insan_kayit.py — sûre 76 (İnsân) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 76

CIPA = {
 # blok 1-10
 1: dict(kademe='L0', olgu=True, cipa=False, not_="'hînun mine'd-dehri lem yekun şey'en mezkûrâ' — insanın anılır bir şey olmadığı zaman dilimi adlanıyor; süre / ölçü yok — L0; tarayıcı vermedi"),
 2: dict(kademe='L1', olgu=True, cipa=False, not_="'min nutfetin emşâcin … semî'an basîrâ' — madde (nutfe) + nitelik (karışık) + yetiler (işitme, görme); 'nebtelîhi' olgu dışı amaç (sınama) — L1 (67:23 ile aynı kademe), L2 sınır vakası; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'selâsile ve ağlâlen ve sa'îrâ' — âhiret, insan yapımı araçlar (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'ke'sin kâne mizâcuhâ kâfûrâ' — cennet içeceği, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="''aynen … yufeccirûnehâ tefcîrâ' — cennet pınarı, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'yevmen kâne şerruhû mustetîrâ' — âhiret günü (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'yevmen 'abûsen qamterîrâ' — âhiret günü (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 11-20
 11: dict(kademe=None, olgu=False, cipa=False, not_="'veqâhumu'llâhu şerra zâlike'l-yevm' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 12: dict(kademe=None, olgu=False, cipa=False, not_="'cennaten ve harîrâ' — cennet, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'lâ yerevne fîhâ şemsen ve lâ zemherîrâ' — cennette güneşin / soğuğun görülmemesi, âhiret; kozmik ad olumsuzlanan görmenin nesnesi (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 14: dict(kademe=None, olgu=False, cipa=False, not_="'dâniyeten … zılâluhâ … qutûfuhâ' — cennet ağaçları, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="'âniyetin min fidda … qavârîr' — cennet, insan yapımı kaplar (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 16: dict(kademe=None, olgu=False, cipa=False, not_="'qavârîra min fidda qaddarûhâ' — cennet, insan yapımı kaplar (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 17: dict(kademe=None, olgu=False, cipa=False, not_="'ke'sen … zencebîlâ' — cennet içeceği, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 18: dict(kademe=None, olgu=False, cipa=False, not_="''aynen … selsebîlâ' — cennet pınarı, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 19: dict(kademe=None, olgu=False, cipa=False, not_="'lu'lu'en mensûrâ' — cennet; inci benzetme aracı; görülen / sanılan kalıbı olgu dışı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 20: dict(kademe=None, olgu=False, cipa=False, not_="'na'îmen ve mulken kebîrâ' — cennet, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 21-31
 21: dict(kademe=None, olgu=False, cipa=False, not_="'siyâbu sundusin … esâvira min fidda … şerâben tahûrâ' — cennet, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 22: dict(kademe=None, olgu=False, cipa=False, not_="'lekum cezâ'en … sa'yukum meşkûrâ' — âhiret karşılığı (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 25: dict(kademe='L0', olgu=True, cipa=False, not_="'bukraten ve asîlâ' — sabah / akşamüstü yalnız zaman zarfı olarak adlanıyor; süreç / ölçü yok — L0 (71:5 emsali); tarayıcı vermedi"),
 26: dict(kademe='L0', olgu=True, cipa=False, not_="'mine'l-leyl … leylen tavîlâ' — gece zaman zarfı; 'tavîl' süre niteliği zarfta, olgunun niteliği değil — L0 (71:5 emsali; L1 sınır vakası); tarayıcı vermedi"),
 27: dict(kademe=None, olgu=False, cipa=False, not_="'yevmen saqîlâ' — âhiret günü (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 28: dict(kademe='L1', olgu=True, cipa=False, not_="'xalaqnâhum ve şedednâ esrahum' — yaratma + yapıya nitelik (sağlam bağ); 'izâ şi'nâ beddelnâ' şart, olgu dışı — L1 (76:2 ile aynı kademe); tarayıcı vermedi"),
 31: dict(kademe=None, olgu=False, cipa=False, not_="'rahmetih … 'azâben elîmâ' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: e_oto 4 token (76:2 semî', basîr; 76:3 şâkir; 76:5 berr) — dördü de DEĞİL (insan / insan çoğulu); KARAR 676 → 680; esma_kayit 'mühür EVET' 76:2 (ÇİFT), 76:3 (ölçüm konumu), bilanço geçerli mühür boş (esma_muhur_43 [2, 3], geçerli [])",
  "kök tablosu: kok_ekle_76 2 kök (مشج 76:2, قمطر 76:10; ölçüm kök alanında '???' → eklendi); 1475 → 1477; retroaktif yama: hedef listesi 0 ayet, hedefli yama 0, genel geçiş 0",
  "hapaks (yeni kök dersi): 76:2 مشج, 76:10 قمطر ★★★ hapaks z=3,28 — yeni köklerin tek ayeti; içerik iddiası değil (76:10'da rab z=2,72 de eşikte)",
  "yıldız (924): 76:6 ★★ allah z=2,33; öbür 7 ayet yıldızsız",
  "harf alanı: ayet 1 ölçümünde harf 60 → harf3 38, isaret 0 (ayet 1 ailesi; besmele); araç alanı (924); KAPATILAMAZ",
  "fâsıla: 75:40 ى → 76:1 ا; 76:1-10 hepsi ا (ölçüm); ölçüm kafiye kırığı 0",
  "gloss (1021 ailesi): كفر 76:5 'kâfûr' (koku / bitki adı) — gloss 'inkâr, nankörlük'; kök [x/4] 'kefûr' (76:3), 'kâfirîn' (76:4), 'kâfûr' (76:5) üç ayrı kelimeyi birlikte sayıyor; طير 76:7 'mustetîr' (yayılan) — gloss 'kuş; uçan'; غلل gloss üç anlam birlikte; lemma 'berr' kara / iyi anlamlarını birleştiriyor (eşsesli şüphesi, sayı iddiası yok)",
  "ölçüm şahıs: 76:2-4 1P (konuşan adsız) ile 76:9-10 1P (iyilerin işaretsiz alıntısı) sahset'te aynı '1' — konuşan katmanı ayrımı ölçümde yok (924); alıntının kapanışı sonraki ayetler okunmadan KAPATILAMAZ (meal tırnağı açık bırakıldı; 1017)",
  "ölçüm biçim: 76:9 'innemâ' hasrı HASR olarak çıkmıyor; 76:2-4 'innâ' tekidi biçim alanında yok (okuma, ◈D)",
  "gönderge / i'râb: 76:8 ''alâ hubbihî' zamiri ve 76:6 ''aynen' i'râbı KAPATILAMAZ",
  "nakarat3: 76:5 'ke's + kâne + mizâc' (2 ayet, tür ic) — sûre içi eşi henüz okunmadı; süzgeç GEÇMEZ",
  "bağ: xref 76:2 → 16:4 (basıldı); esit2 blokta boş; kalıp eşleri okumayla (17:67, 17:91, 19:67, 25:62, 30:39, 37:45, 40:71, 42:11, 45:24, 74:22, 74:44, 75:5, 75:37, 75:40)",
  "aday 1040 (kayıt): 75:40 / 76:1 sûre sınırı — iki yan da soru; fâsıla ى → ا; ardışık sûre okuma bağı 75:36-37 / 76:1-2 ('el-insân' + 'nutfe' aynı sırada)",
  "◈B: 76:6 ''ayn' (عين) ve 76:7 'mustetîr' (طير) tetik — satır dolu, organ / canlı anlamı değil; 76:2 سمع بصر yeti sıfatı",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 59 sayım 0 uyuşmaz; kayıttan önce 76:6 ''ibâdu'llâh korpusta 1' iddiası sayımla yanlış çıktı (harekesiz kalıp 7 ayet) — düzeltildi; 76:1 okunmuş 'hel etâ' ayetleri hakkında toplu içerik iddiası silindi",
 ],
 (11, 20): [
  "esmâ: e_oto 1 token (76:20:7 'kebîr' — 'mulken kebîrâ'); karar DEĞİL; KARAR 680 → 681; esma_kayit 'mühür EVET' (ölçüm konumu), bilanço geçerli mühür boş (esma_muhur_43 [20], geçerli [])",
  "kök tablosu: kok_ekle_76 1 kök (زمهر 76:13; ölçüm kök alanında '???' → eklendi); 1477 → 1478; retroaktif yama: hedef listesi 0 ayet, hedefli yama 0, genel geçiş 0",
  "hapaks (yeni kök dersi): 76:13 زمهر ★★★ hapaks z=3,28 — yeni kökün tek ayeti; içerik iddiası değil",
  "yıldız (924): 76:14, 76:18 ★★★ pas z=5,38 (kısa tek fiilli edilgen); 76:15, 76:17 ★★ pas z=2,52; 76:11 ★ allah z=1,97 — formül davranışı, içerik iddiası değil; öbür 4 ayet yıldızsız",
  "fâsıla: 76:11-20 hepsi ا (ölçüm); ölçüm kafiye kırığı 0",
  "alıntı (1017): 76:9'da açılan iyilerin sözü 76:11 anlatıcı sesiyle (3MP + lafız) kapanıyor — kapanış 76:10 sonunda; 76:10 meali kayıtta kapanış tırnağı olmadan kaldı (okunduğu anda KAPATILAMAZ'dı, kayıt yanlış değil)",
  "gloss (1021 ailesi): سرر 76:11 'surûr' (sevinç) — gloss 'sır, gizleme'; ظلل 76:14 'zılâl' (gölgeler) — gloss 'sürüp gitme'; أني 76:15 'âniye' (kaplar) — gloss 'vakit, ân'; قرر 76:15-16 'qavârîr' (cam, billur) — gloss 'karar kılma; göz aydınlığı'",
  "aday 1041 (kayıt): kök جزي 76:9 'cezâ'' (insanlardan istenmeyen karşılık) / 76:12 'cezâhum' (Allah'ın karşılığı) — lemma farklı (isim / fiil)",
  "gönderge / i'râb: 76:16 'qaddarûhâ' faili 3MP adsız; 76:14 'dâniyeten' i'râbı — KAPATILAMAZ; 76:12 fail 76:11 lafzından",
  "ölçüm iltifât (tanım): 76:19 {3} → {2, 3} 2MS'nin girişi iltifât 0 (924); 76:19 benzetme 'hasibtehum' biçim alanında yok",
  "nakarat3: 76:17 ↔ 76:5 'ke's + kâne + mizâc' — iki eş de basıldı (kâfûr / zencebîl; etken / edilgen); süzgeç GEÇMEZ",
  "bağ: xref 76:19 → 56:17 (basıldı); kalıp eşleri okumayla (18:31, 25:23, 27:44, 36:38, 37:45, 43:71, 52:24, 69:23, 75:22)",
  "◈K / ◈B: 76:13 شمس tetik — satır dolu (olumsuz görme); 76:18 سمو 'tusemmâ' ve 76:20 نعم 'na'îm' S1 lemma kısıtıyla tetiklemiyor — '—'; 76:18 عين pınar, satır dolu",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 46 sayım 0 uyuşmaz; kayıttan önce 76:12 'sabera' okunmamış sayısının dağınık yazımı düzeltildi",
 ],
 (21, 31): [
  "esmâ: e_oto 2 token (76:30:10 ''alîm', 76:30:11 'hakîm' — 'inna'llâhe kâne 'alîmen hakîmâ'); karar İLÂHÎ (lafzın haberi); KARAR 681 → 683; esma_kayit 'mühür EVET (ÇİFT)'; bilanço esma_muhur_43 [30], geçerli [30] — sûre 76'nın tek geçerli mühürü (76:2, 76:3, 76:20 adayları DEĞİL)",
  "kök tablosu: yeni kök yok (ölçüm kök alanında '???' yok); 1478; retroaktif yama: hedef listesi 0 ayet, hedefli yama 0, genel geçiş 0",
  "yıldız (924): 76:25 ★★★ rab z=3,94; 76:30 ★★★ allah z=3,11; 76:24, 76:29 ★★ rab z=2,05; 76:21 ★★ pas z=2,52 — formül davranışı, içerik iddiası değil; öbür 6 ayet yıldızsız",
  "fâsıla: 76:21-31 hepsi ا (ölçüm); sûre 76'da 31 ayetin 31'i ا (üç blok ölçümü); ölçüm kafiye kırığı 0",
  "sayı işareti (924 / 1021): 76:31 'e'adde' (hazırlamak) ölçümde sayı işareti — kök عدد gloss 'sayma, sayı'; yanlış pozitif, sayı yok",
  "konuşan katmanı (1017 / 924): 76:22 2MP hitabı — konuşan adsız, alıntı işaretsiz, KAPATILAMAZ (meal tırnaksız); 76:23-29 konuşan 1P + 2MS muhatap adsız; 76:2-3 1P ile aynı katman mı ölçüm sahset '1' ayırmıyor; 76:30-31 lafız 3. şahısla",
  "ölçüm iltifât (tanım): 76:21 1 (76:20 {2} → {3}); 76:22 {3} → {2, 3} 2MP girişi iltifât 0; 76:23 {2, 3} → {1, 2} iltifât 0 (kesişim 2) — sahne değişimi ölçümde görünmüyor (924)",
  "aday 1041 (kayıt): lemma 'şâ'e' sûre içi 76:28 (1P), 76:29 (dileyen), 76:30 (2MP ve Allah), 76:31 (fail 3MS, okuma: lafız) — aynı fiil insan ve Allah için; kök شكر 76:3 'şâkir' (insan) / 76:22 'meşkûr' (edilgen, fail adsız) — KAPATILAMAZ, kayıt değil",
  "gönderge / i'râb: 76:24 'minhum' ve 76:27 'hâ'ulâ'' aynı topluluk mu, 76:29 'hâzihî', 76:21 ''âliyehum' i'râbı, 76:27 'verâ'ehum' zaman / mekân, 76:31 've'z-zâlimîne' nasbı — KAPATILAMAZ",
  "gloss (1021 ailesi): أسر 76:8 'esîr' / 76:28 'esr' (bağ, yapı) — gloss iki anlamı birlikte; عدد 76:31 'e'adde' (hazırlamak) — gloss 'sayma, sayı'",
  "esit2: 76:29 → 73:19 oran 1,0000 TAM — iki sûrede özdeş ayet (ikisi de basıldı)",
  "bağ: xref 76:22 → 17:19, 76:24 → 52:48, 68:48, 76:29 → 25:57, 73:19, 76:31 → 42:8 (hepsi basıldı); 76:25 → 87:15, 76:30 → 81:29 ve sûre 4 ayetleri henüz okunmadı; kalıp eşleri okumayla (12:41, 15:9, 18:31, 25:32, 25:48, 33:1, 33:55, 56:61, 73:5, 73:7, 73:8, 74:54, 74:55, 74:56, 75:20, 75:21)",
  "◈K / ◈B: 76:26 ليل, 76:27 يوم, 76:28 خلق tetik — satır dolu; 76:25 سمو 'ism' S1 lemma kısıtıyla tetiklemiyor — '—'",
  "çıpa: 76:25, 76:26 L0 (zaman zarfı, 71:5 emsali); 76:28 L1 (yaratma + yapıya nitelik, 76:2 ile aynı kademe); tarayıcı blokta aday vermedi",
  "aday 1040 (bekliyor): sûre sınırı 76:31 → 77:1 — 77:1 henüz okunmadı, kayıt sûre 77'nin ilk bloğunda",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 60 sayım 0 uyuşmaz; 76:30 xref dış düğümleri basılan / okunmamış olarak ayrıldı (kayıttan önce)",
 ],
}

DUZELTME = {
}
