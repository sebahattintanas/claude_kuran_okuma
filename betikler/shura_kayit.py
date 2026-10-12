# -*- coding: utf-8 -*-
"""shura_kayit.py — sûre 42 (Şûrâ) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 42

CIPA = {
 # blok 1-10
 4: dict(kademe='L0', olgu=True, cipa=False, not_="gökler ve yer yalnız mülkiyetin yeri olarak adlanıyor; nitelik/süreç yok; tarayıcı vermedi"),
 5: dict(kademe='L1', olgu=True, cipa=False, not_="göklerin üstlerinden çatlamaya yaklaşması: süreç fiili ('tefattur') + yer ('min fevqihinne'), 'tekâdu' ile gerçekleşmemiş; neden/ölçü yok — L1 (19:90 aynı terkip); tarayıcı vermedi"),
 # blok 11-20
 11: dict(kademe='L1', olgu=True, cipa=False, not_="insan ve davar için eşler + 'yezraukum' (çoğaltma) süreç fiili: sınıf adlı (insan / davar), aşama/mekanizma/sayı yok — L1 (39:6 emsalinin sayısız biçimi); tarayıcı v4 adayı (F_ölçü), çıpa değil"),
 12: dict(kademe='L0', olgu=True, cipa=False, not_="gökler ve yer yalnız 'meqâlîd' (anahtarlar) tamlamasında; nitelik/süreç yok (39:63 aynı tamlama); tarayıcı vermedi"),
 14: dict(kademe=None, olgu=False, cipa=False, not_="tarayıcı v4 adayı (ecel — A_levlâ, A_şart): 'ecelin musemmâ' hüküm erteleme süresi, doğal olgu yok, merdiven uygulanmadı"),
 # blok 21-30
 27: dict(kademe=None, olgu=False, cipa=False, not_="tarayıcı v4 adayı (A_şart): rızkın bol verilmesi / ölçüyle indirilmesi, 'fi'l-ard' yalnız taşkınlığın yeri; doğal olgu yok, merdiven uygulanmadı"),
 28: dict(kademe='L1', olgu=True, cipa=False, not_="yağmurun indirilmesi ('yunezzilu'l-ğays') + rahmetin yayılması: süreç fiili, umut kesildikten sonra (zaman); neden/ölçü yok — L1; tarayıcı vermedi"),
 29: dict(kademe='L1', olgu=True, cipa=False, not_="göklerin ve yerin yaratılışı + ikisinde canlı yayma ('besse fîhimâ min dâbbe'): süreç fiili + yer; canlı sınıfı adlı, alt sınıf/mekanizma yok — L1 (30:22 aynı giriş kalıbı); tarayıcı vermedi"),
 # blok 31-40
 32: dict(kademe='L0', olgu=True, cipa=False, not_="deniz yalnız akıp gidenlerin yeri olarak adlanıyor; 'ke'l-a'lâm' görünüş benzetmesi akıp gidenlere ait; gemi (araç) adlanmıyor (36:41 emsali); nitelik/süreç yok — L0; tarayıcı vermedi"),
 33: dict(kademe='L2', olgu=True, cipa=False, not_="rüzgârın durdurulması ('yuskini'r-rîh') → 'fe-yazlelne revâkide': nedensel bağ adlı, mekanizma/ölçü yok — L2; şartlı ('in yeşe'); tarayıcı v4 adayı (روح, A_şart), çıpa değil"),
 # blok 41-50
 49: dict(kademe='L1', olgu=True, cipa=False, not_="dişi / erkek iki sınıf adlı + 'yehebu' (bağışlama) süreç fiili; ölçüt / mekanizma yok — L1; tarayıcı vermedi"),
 50: dict(kademe='L1', olgu=True, cipa=False, not_="42:49 ile dört sonuç adlı (dişi / erkek / ikisi birlikte / kısır) + süreç fiilleri ('yuzevvicu', 'yec'alu'); ölçüt, üye eşlemesi, mekanizma yok — L1; L4 sınıflama koluna sınırda (aday 1014 ölçütü); tarayıcı vermedi"),
 # blok 51-53
 53: dict(kademe='L0', olgu=True, cipa=False, not_="gökler ve yerdekiler yalnız mülkiyetin konusu; nitelik/süreç yok (42:4 aynı terkip L0); tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ (1022 ailesi): 42:4 'aliyy', 42:6 'evliyâ'/'hafîz'/'vekîl', 42:8 'velî'/'nasîr', 42:9 'velî' ×2/'qadîr' — ölçüm 'MÜHÜRSÜZ', esma_kayit mühür EVET; okuyucu kararı: 4, 6 hafîz, 9 veliyy@8 ve qadîr ilâhî; 6 evliyâ ve vekîl, 8 ikisi, 9 evliyâ@5 değil",
  "iltifât / alıntı (1017 ailesi): 42:6 3MP → 2MS; 42:7 3MS → 1P 'evhaynâ'; 42:10 1S konuşan giriş fiilsiz ('qul' yok) — ölçüm satırı iltifât 0",
  "kafiye / yıldız (1001 ailesi): 42:10 ★★ kaynak 'allah, z=2,14' + kafiye kırığı (ب); 42:6 fâsıla ل (kırık sayılmadı)",
  "gloss (1021 ailesi): فطر 42:5 çatlama — gloss 'yarma, ilk yaratma'; حول 42:7 'havlehâ' (çevre) — gloss 'çevirme, değiştirme'",
  "biçim (517 ailesi): 42:3 fâilin sona alınması, 42:4 ve 42:10 takdimli câr-mecrûr, 42:9 'em' sorusu ve ayırma zamiri 'huve' ×3, 42:10 'mâ' şartı — ölçümde işaretsiz",
  'veri: 42:1 besmele ayet metnine bitişik (n=1, harf 21 → harf3 2) — 41:1 emsali',
  "aday 1040 alanı: 41:43 → 42:3 ('sana / senden öncekilere'), 41:3 → 42:7 ('qur'ânen arabiyyâ'), 39:75 → 40:7 → 42:5 (tesbih kalıbı) — kayıt, test yok",
  'tetik: ilk koşuda 0 uyuşmaz',
 ],
 (11, 20): [
  "esmâ (1022 ailesi): 42:12 'alîm', 42:17 'qarîb', 42:20 'âhir' ×2 — ölçüm 'MÜHÜRSÜZ', esma_kayit mühür EVET; okuyucu kararı: 12 ilâhî, 17 ve 20 değil",
  "iltifât / alıntı (1017 ailesi): 42:13 3MS → 1P → 2MP emir ('en' tefsîr, giriş fiilsiz) → 3MS; 42:15 'qul' sözünün sonu ayet sonu; 42:20 3MS → 1P — ölçüm satırı iltifât 0",
  "kafiye / yıldız (1001 ailesi): 42:17 kafiye kırığı (ب) — bilanço ★ kaynağı 'allah, z=1,29' (eşik altı; düzeltilmiş kaynak kafiye); 42:13 ★★ n 2,72, 42:15 ★★ n 2,29, 42:16 ★★ pas 2,52, 42:14 ★ pas 1,95 (n 1,87 de eşik üstü), 42:19 ★ allah 1,69",
  "gloss (1021 ailesi): قدر 42:12 'yaqdir' (daraltma) — 42:9 'qadîr'; بغي 42:14 taşkınlık; حرث 42:20 mecaz (âhiret ekini); سمو 42:14 'musemmâ' (ad)",
  "biçim (517 ailesi): 42:12, 42:16 takdimli haber; 42:17 'mâ yudrîke' sorusu ve 42:20 'men' şartları ölçümde kip yok",
  "gönderge: 42:11 'fîhi', 42:14 'teferraqû'nun öznesi, 42:16 'ustucîbe lehû' — metinde adlanmıyor, KAPATILAMAZ",
  'tetik: 42:11 ◈B سمع/بصر (esmâ) satırı ilk yazışta eksikti, kayıttan önce eklendi; tetik2 0 uyuşmaz',
  "sayım: harekesiz 'yumârûn' ('ya'murûn' ile), 'ennehe'l-haqq' ('ennehu' ile) ayrılmıyor — kalıp sayımı iddia edilmedi",
 ],
 (21, 30): [
  "esmâ (1022 ailesi): 42:22 'kebîr', 42:24 'alîm', 42:29 'qadîr' — ölçüm 'MÜHÜRSÜZ', esma_kayit mühür EVET; okuyucu kararı: 24 ve 29 ilâhî, 22 değil (lütfun sıfatı)",
  "iltifât / alıntı (1017 ailesi): 42:23 'qul' alıntısının sonu işaretsiz, 3MS → 1S → 1P → 3MS; 42:24 3MP → 2MS; 42:25 3MS → 2MP — ölçüm satırı iltifât 0",
  "kafiye / yıldız (1001 ailesi): 42:27 kafiye kırığı (ر) — ★ kaynağı 'allah, z=0,65'; 42:28 kafiye kırığı (د) — ★ kaynağı 'allah, z=-0,53'; ikisi eşik altı, düzeltilmiş kaynak kafiye; 42:24 ★★ allah 2,20, 42:23 ★ n 1,76, 42:21 ★ pas 1,57",
  "gloss (1021 ailesi): قرف 42:23 iyilik kazanma — gloss 'çoğu kötülük'; بغي 42:27 taşkınlık; قدر 42:27 'bi-qader' (ölçü)",
  "biçim (517 ailesi): 42:21 ve 42:24 'em' sorusu, 42:23 'men' şartı, 42:30 'mâ' şartı — ölçümde kip yok; 42:23 HASR işaretli",
  "gönderge: 42:23 'qurbâ' (akrabalık / yakınlık), 42:26 'yestecîbu'nun fâili, 42:28 'qanatû'nun öznesi, 42:29 'fîhimâ' (gökler dahil) — KAPATILAMAZ",
  "sayım gürültüsü: harekesiz 'bqdr' 'bi-qâdir' / 'bi-qader' ayırmıyor — o sayım iddia edilmedi",
  'tetik: 42:27 ◈K أرض satırı ilk yazışta "—" idi, tetik2 1 uyuşmaz verdi, kayıttan önce dolduruldu; tetik2 0 uyuşmaz',
 ],
 (31, 40): [
  "esmâ (1022 ailesi): 42:31 'veliyy'/'nasîr' ve 42:33 'şekûr' — ölçüm 'MÜHÜRSÜZ', esma_kayit mühür EVET; okuyucu kararı üçü de 'değil' (olumsuzlanan dost/yardımcı — 42:8 emsali; insan sıfatı)",
  "iltifât / alıntı (1017 ailesi): 42:32 ölçüm iltifât 1 (42:31 2MP → 42:32 3MS, ayetler arası); 42:35 3MS → 1P 'âyâtinâ' ve 42:38 3MP → 1P 'razaqnâhum' — ölçüm satırı iltifât 0; 1P adsız",
  "kafiye / yıldız (1001 ailesi): 42:32 kafiye kırığı (م) — ★ kaynağı 'n, z=-0,68' (eşik altı; düzeltilmiş kaynak kafiye); 42:33 ★★★ hapaks ركد 3,28; 42:36 ★ pas 1,57; 42:38 ★ rab 1,62",
  "gloss (1021 ailesi): علم 42:32 'el-a'lâm' (dağlar / yüksek işaretler) — gloss 'bilme'; ظلل 42:33 'yazlelne' (kalmak) — gloss 'sürüp gitme'; بغي 42:39 onlara yönelen taşkınlık",
  "biçim (517 ailesi): 42:36 'fe-mâ' şartı, 42:37 'izâ mâ' ve 42:39 'izâ' şartı, 42:40 'fe-men' şartı — ölçümde kip yok",
  "gönderge: 42:32 'el-cevâr' adsız (gemi kelimesi yok); 42:34 'kesebû' 3MP adsız; 42:33 'zahrih' denize — KAPATILAMAZ",
  "metin sayımı imlâsı: 10:27 'cezâu' ile 42:40 'cezâu' farklı yazılı (ء / ؤا), harekesiz sayım birleştirmiyor — sayı verilmedi, bağ okuma ile kuruldu",
  'aday: 1041 açıldı (aynı kelimenin Allah ve insan için kullanılması — kayıt, test korpus sonunda)',
  'tetik: ilk koşuda 0 uyuşmaz',
 ],
 (41, 50): [
  "esmâ (1022 ailesi): 42:44 'veliyy', 42:46 'evliyâ', 42:48 'hafîz' — ölçüm ORTA 'MÜHÜRSÜZ'; okuyucu kararı üçü de 'değil' (olumsuzlanan dost/dostlar; muhatap için olumsuz bekçi); 42:50 'alîm'/'qadîr' SON MÜHÜR, ilâhî",
  "iltifât / alıntı (1017 ailesi): 42:45 iman edenlerin sözünün sonu ('elâ inne'z-zâlimîne …' dahil mi) işaretsiz; 42:47 emri veren konuşan adsız ('qul' yok); 42:48 3MP → 2MS → 1P → 3MS → 3MP — ölçüm satırı iltifât 0",
  "kafiye / yıldız (1001 ailesi): 42:41 kafiye kırığı (ل) — ★ kaynağı 'allah, z=-0,53'; 42:45 kafiye kırığı (م) — ★ kaynağı 'n, z=1,55' (eşik üstü; kırıkla iki aday kaynak); 42:41 eşik altı, düzeltilmiş kaynak kafiye; 42:46 ★ allah 1,97, 42:48 ★ n 1,55",
  "gloss (1021 ailesi): عرض 42:45 'yu'radûne' (sunulma) / 42:48 'a'radû' (yüz çevirme) — iki anlam; ملك 42:5 'melâike' / 42:49 'mulk'; ذكر 42:49-50 erkek — gloss 'anma, zikir'",
  "biçim (517 ailesi): 42:41, 43, 44, 46 'men' şartları ve 42:42 'innemâ' hasrı ölçümde işaretsiz (42:48 'in … illâ' HASR işaretli)",
  "gönderge: 42:45 'aleyhâ' (3FS) adsız — 40:46'da ateş; 42:48 tekil 'el-insân' ↔ çoğul 'tusibhum' — KAPATILAMAZ",
  "sayı işareti: 42:50 'zuwwijat' — ayette bu biçim yok, 'yuzevvicu' eşlemesi (araç açığı, aday 924 — metin hakkında kanıt değil)",
  "metin sayımı (harekesiz): 'el-insâne kefûr' 17:67 'kâne'l-insânu kefûrâ' ile birleşiyor — i'râb farkı sayımda görünmez",
  'çıpa: 42:49-50 dörtlü sonuç kümesi L1 — L4 sınıflama koluna sınırda (aday 1014 ölçütü: üye eşlemesi yok)',
  'tetik: ilk koşuda 0 uyuşmaz',
 ],
 (51, 53): [
  "esmâ (1022 ailesi): 42:52 'nûr' — ölçüm ORTA 'MÜHÜRSÜZ', vahyedilen için, okuyucu kararı 'değil'; 42:51 'aliyy'/'hakîm' SON MÜHÜR, ilâhî",
  "iltifât / alıntı (1017 ailesi): 42:51 3MS → 42:52 1P 'evhaynâ' → 2MS — ölçüm satırı iltifât 0; 1P adsız",
  'kafiye / yıldız (1001 ailesi): kırık yok; 42:52 ★ n 1,55, 42:53 ★★ allah 2,14',
  'gloss (1021 ailesi): روح 42:33 rüzgâr / 42:52 ruh; بشر 42:23 müjde / 42:51 beşer',
  "gönderge: 42:52 'ce'alnâhu' zamiri (rûh / kitap) — KAPATILAMAZ",
  "araç (aday 924): 42:51 ölçüm şahıs '1S 1' — morfoloji 'verâi' sonunu 1S zamiri etiketliyor, metinde 1S yok; metin hakkında kanıt değil",
  "aday 1040 alanı: 42:51 'aliyyun hakîm' → 43:4 (metin sayımı 2 ayet; 43:4 henüz okunmadı) — kayıt, test yok",
  'tetik: ilk koşuda 0 uyuşmaz',
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_42.py uygular)
DUZELTME = {
}
