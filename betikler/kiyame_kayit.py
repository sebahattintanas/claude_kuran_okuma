# -*- coding: utf-8 -*-
"""kiyame_kayit.py — sûre 75 (Kıyâme) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 75

CIPA = {
 # blok 1-10
 1: dict(kademe=None, olgu=False, cipa=False, not_="'bi-yevmi'l-qiyâme' — kıyamet günü, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 3: dict(kademe=None, olgu=False, cipa=False, not_="'ellen necme'a 'izâmeh' — kemiklerin toplanması, diriliş, gaybî olay (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 4: dict(kademe=None, olgu=False, cipa=False, not_="'en nusevviye benâneh' — parmak uçlarının düzenlenmesi, diriliş, gaybî olay (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 5: dict(kademe=None, olgu=False, cipa=False, not_="'li-yefcure emâmeh' — fucûr (günaha dalma), doğal olgu değil (olgu=False); tarayıcı v4 adayı, çıpa değil"),
 6: dict(kademe=None, olgu=False, cipa=False, not_="'eyyâne yevmu'l-qiyâme' — kıyamet günü, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 7: dict(kademe=None, olgu=False, cipa=False, not_="'bariqa'l-basar' — gözün kamaşması, âhiret sahnesi (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 8: dict(kademe='L1', olgu=True, cipa=False, not_="'xasafe'l-qamer' — âhiretteki kozmik olay (ay), süreç adı; mekanizma / ölçü yok — L1; tarayıcı vermedi"),
 9: dict(kademe='L1', olgu=True, cipa=False, not_="'cumi'a'ş-şemsu ve'l-qamer' — âhiretteki kozmik olay (güneş ve ay), süreç adı; mekanizma / ölçü yok — L1; tarayıcı vermedi"),
 10: dict(kademe=None, olgu=False, cipa=False, not_="'yevme'izin eyne'l-meferr' — o gün, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 11-20
 11: dict(kademe=None, olgu=False, cipa=False, not_="'kellâ lâ wazar' — sığınak yokluğu, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 12: dict(kademe=None, olgu=False, cipa=False, not_="'yevme'izini'l-mustaqarr' — o gün varılacak yer, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 13: dict(kademe=None, olgu=False, cipa=False, not_="'yunebbe'u'l-insânu yevme'izin' — o gün, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 21-30
 21: dict(kademe=None, olgu=False, cipa=False, not_="'tezerûne'l-âxira' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 22: dict(kademe=None, olgu=False, cipa=False, not_="'vucûhun yevme'izin nâdira' — âhiret, yüzlerin hâli (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 23: dict(kademe=None, olgu=False, cipa=False, not_="'ilâ rabbihâ nâzira' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 24: dict(kademe=None, olgu=False, cipa=False, not_="'vucûhun yevme'izin bâsira' — âhiret, yüzlerin hâli (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 25: dict(kademe=None, olgu=False, cipa=False, not_="'en yuf'ale bihâ fâqira' — âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 26: dict(kademe='L1', olgu=True, cipa=False, not_="'izâ belağati't-terâqî' — ölüm anı + organ adı (köprücük kemikleri); fail adsız; süreç / mekanizma yok — L1 (56:83 ile aynı kademe); tarayıcı vermedi"),
 29: dict(kademe='L1', olgu=True, cipa=False, not_="'velteffeti's-sâqu bi's-sâq' — ölüm anı + organ adı (bacak); mekanizma / ölçü yok — L1; mecaz okuması da mümkün (KAPATILAMAZ); tarayıcı vermedi"),
 30: dict(kademe=None, olgu=False, cipa=False, not_="'yevme'izini'l-mesâq' — o gün sevk, âhiret (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
 # blok 31-40
 37: dict(kademe='L1', olgu=True, cipa=False, not_="'nutfeten min meniyyin yumnâ' — madde (nutfe, meni) + hâl (dökülme), aşama ardışıklığı yok — L1 (53:46 ile aynı kademe); tarayıcı vermedi"),
 38: dict(kademe='L1', olgu=True, cipa=False, not_="'summe kâne 'alaqaten fe-xalaqa fe-sevvâ' — aşama ardışıklığı, ara aşama 'alaqa adlı; nedensellik / ta'lîl / ölçü yok — L1; tarayıcı vermedi"),
 39: dict(kademe='L1', olgu=True, cipa=False, not_="'ez-zevceyni'z-zekera ve'l-unsâ' — iki sınıf adlanıyor, sınıflama ölçütü yok — L1 (53:45 ile aynı kademe); L4 sınıf kolu sınır vakası (799); tarayıcı vermedi"),
 40: dict(kademe=None, olgu=False, cipa=False, not_="'en yuhyiye'l-mevtâ' — ölülerin diriltilmesi, gaybî (olgu=False); merdiven uygulanmadı; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "esmâ: e_oto 0 token; KARAR 675 değişmedi; blokta mühür yok (esma_muhur_43 boş)",
  "kök tablosu: kok_ekle_75 1 kök (بنن 75:4; ölçüm kök alanında '???' → eklendi); 1470 → 1471; retroaktif yama: hedef listesi 1 ayet (sûre 8 — ayet kaydı yok, henüz okunmadı), hedefli yama 0, genel geçiş 0",
  "harf alanı: ayet 1 ölçümünde harf 35 → harf3 16, isaret 0 (ayet 1 ailesi; besmele); araç alanı (924); KAPATILAMAZ",
  "yıldız (924): 75:9 ★★★ pas z=5,38 (kısa tek fiilli edilgen) — formül davranışı, içerik iddiası değil; öbür 9 ayet yıldızsız",
  "fâsıla: 74:56 ة → 75:1 ة; 75:1-2 ة, 75:3-5 ه, 75:6 ة, 75:7-10 ر; ة ve ه ölçümde aynı H sınıfı; 75:6 → 75:7 H → R sınıf geçişi kafiye kırığı olarak işaretlenmiyor (bilanço kafiye kırığı boş; 924)",
  "gloss (1021 ailesi): أمم 75:5 'emâm' (ön) — gloss 'ümmet, topluluk'; فجر 75:5 'li-yefcure' (fucûr) — gloss 'fışkırtma; fecir'; lemma 'yefcur' iki geçişi (fışkırtma / fucûr) eşsesli şüphesi — sayı iddiası yok",
  "tarayıcı v4: 75:5 aday (فجر kökü) — fucûr, doğal olgu değil; çıpa değil",
  "çıpa: 75:8, 75:9 L1 olgu=True (âhiretteki kozmik olay); L4 yok; olgu=False 7",
  "ölçüm kip / biçim: 75:1-2 yemin fiilinin başındaki 'lâ' kip alanında NEG sayılıyor (biçim QASEM ile birlikte); 75:4 cevap edatı 'belâ' biçim alanında yok (—)",
  "ölçüm iltifât: 75:2 → 75:3 konuşan 1S → 1P ayetler arası geçişi ölçümde görünmüyor (iltifât ayet içi; ◈A'da)",
  "nakarat3: 75:4 'qâdir + 'alâ + en' (2 ayet, tür ic) — sûre içi eşi henüz okunmadı; süzgeç GEÇMEZ",
  "bağ: xref 75:6 → 29:13 (basıldı); esit2 blokta boş; kalıp eşleri okumayla (19:66, 36:78, 36:81, 46:33, 51:12, 56:75, 67:16, 69:38, 70:40, 71:16, 74:32)",
  "◈B: 75:3 kemik (عظم), 75:4 parmak ucu (بنن) tetik listesinde değil — gözlem ◇'de; 75:4 ◈B '—'",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 31 sayım 0 uyuşmaz",
 ],
 (11, 20): [
  "esmâ: e_oto 0 token; KARAR 675 değişmedi; blokta mühür yok (esma_muhur_43 boş); 75:12 Rab sınıf R",
  "kök tablosu: kok_ekle_75 1 kök (حرك 75:16; ölçüm kök alanında '???' → eklendi); 1471 → 1472; retroaktif yama: hedef listesi 1 ayet (sûre 8 — ayet kaydı yok, henüz okunmadı; önceki bloğun kökünden), hedefli yama 0, genel geçiş 0",
  "hapaks (yeni kök dersi): 75:16 حرك ★★★ hapaks z=3,28 — yeni kökün tek ayeti; içerik iddiası değil",
  "yıldız (924): 75:12 ★★★ rab z=5,01 (kısa lafızsız ayette tek Rab); 75:13 ★ pas z=1,57; 75:16 ★★★ hapaks — formül davranışı, içerik iddiası değil; öbür 7 ayet yıldızsız",
  "fâsıla (924): 75:16 son harf medde işareti sayılıyor ('ٓ'), sahte KAFİYE KIRILMASI (bilanço kafiye kırığı [16]; yıldız kaynağında kafiye_kirik True) — metinde son harf ه; 75:13 ر → 75:14 ة (R → H) sınıf geçişi işaretlenmiyor",
  "ölçüm iltifât (tanım): iltifât yalnız önceki ayetle şahıs kümesi AYRIKSA 1 (defter4); sahset kişi düzeyinde, tekil / çoğul ayırmıyor — 75:15 {3} → 75:16 {2, 3} 2MS'nin girişi 0; 75:12 3 → 2, 75:13 2 → 3, 75:20 13 → 2 işaretli",
  "ek (blok 1-10 ARIZA satırı için): 'ölçüm iltifât: 75:2 → 75:3 … (iltifât ayet içi; ◈A'da)' satırındaki gerekçe yanlış — iltifât ayet içi değil, önceki ayetle şahıs kümesi ayrıklığına bakıyor; 1S ve 1P aynı küme ('1') sayıldığı için geçiş görünmüyor. Özgün satır korunur; 75:3 mercek DUZELTME (aday 924)",
  "gloss (1021 ailesi): وزر 75:11 'wazar' (sığınak) — gloss 'yük, günah yükü'",
  "ölçüm biçim: 75:12 haber öne alınmış ('ilâ rabbike'), 75:17 ve 75:19 'inne 'aleynâ' tekidi — biçim alanında yok (okuma, ◈D)",
  "gönderge: 75:16-19 3MS zamirler ('bihî', 'jem'ahû', 'qur'ânah', 'beyânah') — metinde adlı değil, KAPATILAMAZ; meal parantezsiz",
  "i'râb: 75:14 mübteda müzekker / haber müennes ('basîra') — KAPATILAMAZ",
  "nakarat3 / esit2: 75:12 'ilâ + rabb + yevme'izin' tür ic ve esit2 BENZER — eş henüz okunmadı; süzgeç GEÇMEZ",
  "◈B: 75:16 dil (لسن) tetik listesinde değil — '—', gözlem ◇'de; 75:14 'basîra' بصر tetik — satır dolu, organ anlamı değil",
  "bağ: xref blokta yok; kalıp eşleri okumayla (12:108, 17:14, 17:18, 17:106, 20:114, 36:38, 53:42, 55:4, 74:53)",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 25 sayım 0 uyuşmaz",
 ],
 (21, 30): [
  "esmâ: e_oto 1 token (75:21:2 'âxir' — 'el-âxira', âhiret); karar DEĞİL; KARAR 675 → 676; esma_kayit 'mühür EVET' (ölçüm konumu), bilanço geçerli mühür boş (esma_muhur_43 [21], geçerli []); 75:23, 75:30 Rab sınıf R",
  "kök tablosu: kok_ekle_75 2 kök (نضر 75:22, ترق 75:26; ölçüm kök alanında '???' → eklendi); 1472 → 1474; retroaktif yama: hedef listesi 1 ayet (sûre 8 — ayet kaydı yok, henüz okunmadı; önceki bloğun kökünden), hedefli yama 0, genel geçiş 0",
  "hapaks (yeni kök dersi): 75:26 ترق ★★★ hapaks z=3,28 — yeni kökün tek ayeti; içerik iddiası değil",
  "yıldız (924): 75:23 ★★★ rab z=6,78, 75:30 ★★★ rab z=5,01 (kısa lafızsız ayette tek Rab); 75:27 ★★★ pas z=5,38; 75:25 ★★ pas z=2,52; 75:26 ★★★ hapaks — formül davranışı, içerik iddiası değil; öbür 5 ayet yıldızsız",
  "fâsıla (924): 75:21-25 ة, 75:26 ى (A sınıfı), 75:27-30 ق; 75:25 → 75:26 (H → A) ve 75:26 → 75:27 (A → ق) sınıf geçişleri kafiye kırığı olarak işaretlenmiyor (bilanço kafiye kırığı boş)",
  "gloss (1021 ailesi): فقر 75:25 'fâqira' (bel kıran belâ) — gloss 'fakirlik'; سوق 75:29 'sâq' (bacak) — gloss 'sürme, sevk etme; çarşı'; kök سوق [x/3] iki anlamı birlikte sayıyor (bacak ×2 / sevk) — kök sayısı lafız sayısı değil",
  "gönderge: 75:26 fail 3FS ve 75:28 'ennehû' — metinde adlı değil, KAPATILAMAZ; meal parantezsiz; 75:27 'râq' iki okuma (tedavi eden / yükselten) KAPATILAMAZ",
  "çıpa: 75:26, 75:29 L1 olgu=True (ölüm anı + organ adı; 75:29 mecaz okuması da mümkün); L4 yok; olgu=False 6",
  "ölçüm biçim: 75:23, 75:30 haber öne alınmış ('ilâ rabb-') — biçim alanında yok (okuma, ◈D)",
  "esit2 / nakarat3: 75:30 ↔ 75:12 BENZER / tür ic — iki eş de basıldı; son kelime farklı (mustaqarr / mesâq); süzgeç GEÇMEZ",
  "◈B: 75:26 köprücük kemikleri (ترق), 75:29 bacak (سوق) tetik listesinde değil — '—', gözlem ◇'de; 75:22-25 'vucûh' (وجه) tetik dışı",
  "bağ: xref blokta yok; kalıp eşleri okumayla (17:18, 17:19, 18:78, 27:35, 56:83, 68:42, 74:22)",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 24 sayım 0 uyuşmaz",
 ],
 (31, 40): [
  "esmâ: e_oto 0 token; KARAR 676 değişmedi; blokta mühür yok (esma_muhur_43 boş)",
  "kök tablosu: kok_ekle_75 1 kök (سدي 75:36; ölçüm kök alanında '???' → eklendi); 1474 → 1475; retroaktif yama: hedef listesi 1 ayet (sûre 8 — ayet kaydı yok, henüz okunmadı; önceki bloğun kökünden), hedefli yama 0, genel geçiş 0",
  "hapaks: 75:33 مطو (kök tabloda vardı) ve 75:36 سدي (yeni kök) ★★★ hapaks z=3,28 — tek ayetli kökler; içerik iddiası değil",
  "yıldız (924 / 1001): 75:36 ★★★ hapaks (pas 2,52 de eşikte); 75:37 ★★ pas z=2,52; 75:34, 75:35, 75:39 ★ — kaynak 'n' etiketli, ama kafiye_kirik True (sahte kırıktan; 1001 ailesi); öbür 4 ayet yıldızsız",
  "fâsıla (924): 75:31-40 on ayetin onu metinde ى; ölçüm 75:33, 75:35, 75:39'da medde işaretini ('ٓ') son harf sayıyor, 75:34'ü de (medde artefaktından sonra gelen ى) kırık işaretliyor — bilanço kafiye kırığı [33, 34, 35, 39] dördü de sahte; 75:30 ق → 75:31 ى sınıf geçişi işaretlenmiyor",
  "gloss (1021 ailesi): مطو 75:33 'yetemettâ' (çalımla yürüme) — gloss 'uzatma, mühlet'; مني 75:37 gloss 'temenni, kuruntu; meni' iki anlamı birlikte taşıyor; lemma 'evlâ' 75:34-35 'daha yakın / lâyık' anlamlı geçişlerle birleşiyor (eşsesli şüphesi, sayı iddiası yok)",
  "sayı işareti: 75:39 'zevc' — 'ez-zevceyn' ikil, iki eş: çift adı, sayım değil (kök kaynaklı)",
  "gönderge: 75:31-33 adsız 3MS (adlandırılmaz); 75:38 'xalaqa / sevvâ' faili ve 75:39 'minhu' — metinde adlı değil, KAPATILAMAZ; meal parantezsiz",
  "çıpa: 75:37, 75:38, 75:39 L1 olgu=True (oluşum dizisi: nutfe / meni → 'alaqa → yaratma / düzenleme → iki eş); L4 yok; 75:39 L4 sınıf kolu sınır vakası (799); olgu=False 1 (75:40)",
  "esit2 / nakarat3: 75:34 ↔ 75:35 (tür tam / tür ic, BENZER) — iki eş de basıldı; 75:40 ↔ 75:4 tür ic — iki eş de basıldı; süzgeç GEÇMEZ",
  "bağ: xref 75:39 → 53:45, 75:40 → 46:33 (ikisi de basıldı); kalıp eşleri okumayla (20:48, 23:14, 23:115, 47:20, 53:46, 56:58, 74:43, 74:56)",
  "aday 1040: 75:40 → 76:1 sûre sınırı — 76:1 henüz okunmadı (bağ 76:1 okunurken yazılır)",
  "aday 1041: sûre 75'te aynı kelimenin Allah ve insan için kullanımı kaydı yok ('sevvâ' 75:4 / 75:38 ve 'qâdir' 75:4 / 75:40 ikisi de insan dışı gönderge)",
  "süreç: tetik ön kuru koşu (geçici modül, silindi) 0 uyuşmaz; oturum_xy 28 sayım 0 uyuşmaz (sûre geneli 75:1-40: 108 sayım, 0 uyuşmaz)",
 ],
}

DUZELTME = {
 3: dict(alan='mercek', eski="iltifât ayet içi sayılıyor",
         dogru="Gerekçe yanlış: ölçüm iltifâtı ayet içi değil, önceki ayetle şahıs kümesi AYRIKSA 1 (defter4); sahset kişi düzeyinde, tekil / çoğul ayırmıyor — 75:2 {1} → 75:3 {1, 3} ayrık değil, 1S → 1P geçişi bu yüzden görünmüyor. Özgün alan korunur.",
         aday=924, blok='1-10'),
}
