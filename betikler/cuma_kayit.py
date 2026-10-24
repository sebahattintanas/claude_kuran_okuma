# -*- coding: utf-8 -*-
"""cuma_kayit.py — sûre 62 (Cuma) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 62

CIPA = {
 # blok 1-5
 1: dict(kademe='L0', olgu=True, cipa=False, not_="'yusebbihu li'llâhi mâ fi's-semâvâti ve mâ fi'l-ard' — gökler ve yer tesbih edenlerin yeri olarak adlanıyor; süreç / ölçü yok — L0 (57:1, 59:1, 61:1 emsali); tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'ke-meseli'l-himâri yahmilu esfârâ' — teşbihte hayvan benzetme aracı, doğal süreç yok; merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 6-11
 6: dict(kademe='L0', olgu=True, cipa=False, not_="'fe-temennevu'l-mevt' — ölüm dilenecek şey olarak adlanıyor; süreç / ölçü yok — L0; tarayıcı v4 adayı, çıpa değil"),
 8: dict(kademe='L0', olgu=True, cipa=False, not_="'inne'l-mevte'llezî teferrûne minhu fe-innehû mulâqîkum' — ölüm kaçınılmaz olarak adlanıyor; süreç yok — L0; dönüş ve haber verme âhiret, olgu değil; tarayıcı vermedi"),
 10: dict(kademe='L0', olgu=True, cipa=False, not_="'fe'nteşirû fi'l-ard' — yeryüzü dağılma yeri olarak adlanıyor; süreç / ölçü yok — L0; tarayıcı v4 adayı, çıpa değil"),
}

ARIZA = {
 (1, 5): [
  "esmâ: e_oto 7 token (62:1 'melik', 'quddûs', 'azîz', 'hakîm'; 62:2 'mubîn'; 62:3 'azîz', 'hakîm'); 62:1 ve 62:3 İLÂHÎ, 62:2 'mubîn' DEĞİL ('dalâl'in sıfatı); KARAR 588 → 595; bilanço geçerli mühür 62:1, 62:3; 62:2 esma_kayit mühür EVET, karar sonrası geçersiz (1022 ailesi)",
  "esmâ ölçüm satırı (1022): 62:1 dört adlı dizide 'quddûs'u göstermiyor (59:23 ailesi); karar esma_kayit konumundan (62:1:10)",
  "harf alanı: ayet 1 ölçümünde harf 69 → harf3 50, isaret 0 (56:1-61:1 ailesi); 62:2-5'te fark = isaret — besmele harfleri olabilir; araç alanı, metin hakkında kanıt değil (aday 924); KAPATILAMAZ",
  "kök tablosu: sûre 62 blok 1-5'te eksik kök yok (kok_ekle_62 boş); retroaktif yama 0",
  "kip (924): 62:2 've in kânû min qablu lefî dalâlin mubîn' — 'in' muhaffefe (lâm ile), ölçüm kipi 'şart' (COND) yazıyor",
  "lemma eşsesli (924, 'asâ dersi): lemma 'esfâr' 34:19 yolculuklar / 62:5 kitaplar birlikte sayılıyor (2 ayet); kök سفر 12 ayet; gloss iki anlamı da taşıyor",
  "gloss (1021 ailesi): kök بأس tablosu 'şiddet, azap; savaş gücü' — 62:5 zem fiili 'bi'se' (ne kötü) anlamı yazılmıyor",
  "yıldız (924): 62:4 ★★★ allah z=3,47 — 10 kelimede 2 lafız; içerik iddiası değil",
  "esmâ sınıfı (okuma): 62:2-3 lafız yok; 62:3 'huve'l-azîzu'l-hakîm' zamirle Allah (sınıf E), 62:2 karar sonrası 0",
  "aday 1040 (kayıt): 61:14 → 62:1 sûre sınırı — ardışık iki sûre aynı tesbih cümlesiyle açılıyor (61:1 PERF / 62:1 IMPF; esit2 BENZER); 61:9 / 62:2 'huve'llezî ersele / be'ase'; 61:7 / 62:5 aynı kapanış 've'llâhu lâ yehdi'l-qavme'z-zâlimîn'; 61:6 / 62:5 Tevrât; fâsıla ن → م; test yok",
  "aday 1041 (kayıt): kök حكم 62:1, 62:3 'el-hakîm' (Allah adı) / 62:2 'el-hikmeh' (elçinin öğrettiği)",
  "adsız (aday 1017): 62:2 elçi ('rasûlen minhum'), ümmîler; 62:3 sonradan gelenler; 62:4 'men yeşâ''; 62:5 Tevrât yüklenenler (edilgen), yükleyen, yalanlayan topluluk — ad verilmedi",
  "çıpa: 62:1 L0 (gökler ve yer); 62:5 teşbih hayvanı, süreç yok, olgu False; L4 yok; tarayıcı adayı yok",
  "karşıt çift (aday 1039, okuma): 62:2 arındırma / önceki sapkınlık; 62:3 'minhum' / 'lemmâ yelhaqû'; 62:5 'hummilû' / 'lem yahmilûhâ'; 62:4 yok — kayıt, test yok",
  "okuma: 59:1, 61:1, 61:14, 59:23 → 62:1; 61:9, 26:97, 12:8 → 62:2; 61:1, 59:1 → 62:3; 57:21, 57:29 → 62:4; 24:54, 16:8, 31:19, 34:19, 61:6, 61:7, 9:109 → 62:5 — KAPATILAMAZ",
  "tetik: ön kuru koşu 2 uyuşmaz (62:1 ◈K سمو أرض, 62:5 ◈B حمل) → satırlar dolduruldu; kayıtta 0 uyuşmaz; [x/y] 0 (41 sayım)",
 ],
 (6, 11): [
  "esmâ: e_oto 3 token (62:6 'evliyâ''; 62:7 'alîm'; 62:8 'âlim'); 'evliyâ'' DEĞİL (iddia edenler, çoğul), 'alîm' ve 'âlim' İLÂHÎ; KARAR 595 → 598; bilanço geçerli mühür 62:7, 62:8",
  "esmâ konum (1022): 62:7 'alîm' ölçümde 'SON' konum, ardından 'bi'z-zâlimîn' geliyor — mühür iddiası bilançodan, konum iddiası metinden",
  "esmâ sınıfı (okuma): 62:8 lafız yok, 'âlimi'l-ğaybi ve'ş-şehâde' (sınıf E)",
  "tarayıcı v4 adayları 62:6 (ölüm), 62:10 (yeryüzü) — ikisi L0, çıpa değil; 62:8 ölüm L0 (tarayıcı vermedi); kesinlik 0/2",
  "sayı işareti (924): 62:10 'kesîr' çokluk niteliği, sayı değil",
  "yıldız (924): 62:7 ★ ve 62:10 ★★ lafız kaynaklı — içerik iddiası değil",
  "edilgen (ölçüm): 62:8 'turaddûne', 62:9 'nûdiye', 62:10 'qudiyet' — fail adlanmıyor (1017)",
  "aday 1040 (kayıt): 61:11 / 62:9 'zâlikum hayrun lekum in kuntum ta'lemûn' (ardışık sûrelerde aynı kapanış); 61:10 / 62:11 'ticâret' (azaptan kurtaran / koşulup gidilen); test yok",
  "aday 1041 (kayıt): kök علم 62:7 'alîm', 62:8 'âlim' (Allah) / 62:9 'ta'lemûn' (inananlar); lemma 'veliyy' esmâ / 62:6 'evliyâ'u li'llâh' (iddia edenler)",
  "adsız (aday 1017): 'qul' muhatabı 2MS (62:6, 8, 11), 62:11 ayakta bırakılan 2MS; 'ellezîne hâdû' (sınıf); çağıran, bitiren, döndüren (edilgen); dağılıp gidenler — ad verilmedi",
  "okuma ikiliği yok; 62:5 Tevrât yüklenenler ile 62:6 'ellezîne hâdû' göndergesi eşlenmedi (okuma)",
  "kapanan sûre içi eşler: مني 62:6 → 62:7; موت 62:6 → 62:8; فضل 62:4 → 62:10; ذكر, صلو 62:9 → 62:10; خير 62:9 → 62:11; علم 62:2 → 62:9 (son); sûre içinde açık eş kalmadı",
  "fâsıla: bu blokta altı ayet ن; kafiye kırığı 0",
  "karşıt çift (aday 1039, okuma): 62:6 iddia / sınama; 62:6 / 62:7 dileyin / asla dilemezler; 62:8 kaçmak / karşılaşmak, ğayb / şehâde; 62:9 koşun / bırakın; 62:9 / 62:10 alışverişi bırakın / lütuf arayın; 62:11 dağılmak / ayakta bırakmak — kayıt, test yok",
  "okuma: 22:17 → 62:6; 9:47 → 62:7; 33:16, 9:94, 9:105, 59:22 → 62:8; 24:37, 9:111, 61:11 → 62:9; 30:20 → 62:10; 57:20, 61:10, 24:37, 22:58 → 62:11 — KAPATILAMAZ",
  "kendi kaydı (kayıttan önce): 62:11 'son geçişler' listesinde خير [3/3] yazılmıştı (oturum_xy yakaladı) → [2,3/3]; 62:6 ve 62:7'de basılmamış iki okunmuş ayet ders / emsal numarasıyla anılmıştı → numarasız",
  "tetik: ön kuru koşu 6 uyuşmaz (62:6 ◈B أنس موت, 62:7 ◈K أبد ve ◈B يدي, 62:8 ◈B موت, 62:9 ◈K يوم, 62:10 ◈K أرض) → satırlar dolduruldu; kayıtta 0 uyuşmaz; [x/y] 0 (73 sayım)",
 ],
}

DUZELTME = {
}
