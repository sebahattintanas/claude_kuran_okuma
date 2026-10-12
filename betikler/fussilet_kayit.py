# -*- coding: utf-8 -*-
"""fussilet_kayit.py — sûre 41 (Fussilet) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 41

CIPA = {
 # blok 1-10
 9: dict(kademe='L1', olgu=True, cipa=False, not_="yerin yaratılışı + süre ('fî yevmeyn', iki gün) — adlandırma + süre; süreç/ara durum yok; tarayıcı vermedi"),
 10: dict(kademe='L1', olgu=True, cipa=False, not_="yerde sabit dağlar, bereket, azıkların takdiri 'fî erba'ati eyyâm' — sayı + birim (gün) var ama süreç/mekanizma yok; 'gün'ün ölçü birimi mi dönem mi KAPATILAMAZ — L4 ölçü koluna sınırda, L1; tarayıcı vermedi"),
 # blok 11-20
 11: dict(kademe='L1', olgu=True, cipa=False, not_="gök 'duhân' (duman) hâlinde — ara durum adlanıyor + gök ve yere söz; süreç/neden yok — L1; tarayıcı vermedi"),
 12: dict(kademe='L1', olgu=True, cipa=False, not_="yedi gök iki günde tamamlanıyor (sayı + süre birimi), dünya göğü kandillerle süslü ve korunmuş (işlev); 41:11 'duhân' → 41:12 'seb'a semâvât' ara durum → sonuç dizisi adlı ama mekanizma yok — L4 ölçü/süreç koluna sınırda (41:10 emsali), L1, KAPATILAMAZ; tarayıcı vermedi"),
 13: dict(kademe='L0', olgu=True, cipa=False, not_="'sâiqa' (yıldırım) yalnız azap adı olarak; süreç/nitelik yok; tarayıcı v4 adayı (A_şart), çıpa değil"),
 15: dict(kademe=None, olgu=False, cipa=False, not_="tarayıcı v4 adayı (ard, halq — D_yeti, G_bakış): yeryüzünde büyüklenme ve güç karşılaştırması, doğal olgu yok, merdiven uygulanmadı"),
 16: dict(kademe='L1', olgu=True, cipa=False, not_="rüzgâr adlanıyor + nitelik ('sarsar') + süre ('eyyâmin nahisât', sayısız); ta'lîl azabın amacı — doğal olgu içi nedensellik değil — L1; tarayıcı v4 adayı (B_ta'lîl), çıpa değil"),
 24: dict(kademe=None, olgu=False, cipa=False, not_="tarayıcı v4 adayı (nûr — A_şart): 'en-nâr' azap yeri, şart cümlesi; doğal olgu yok, merdiven uygulanmadı"),
 37: dict(kademe='L0', olgu=True, cipa=False, not_="gece, gündüz, güneş, ay yalnız 'âyât' ve secde nesnesi olarak adlanıyor; nitelik/süreç/ölçü yok; tarayıcı v4 adayı (A_şart), çıpa değil"),
 38: dict(kademe='L0', olgu=True, cipa=False, not_="gece ve gündüz yalnız tesbih süresi (zarf) olarak adlanıyor (40:46 emsali); tarayıcı v4 adayı (A_şart), çıpa değil"),
 39: dict(kademe='L2', olgu=True, cipa=False, not_="yer 'hâşi'a' → su indirilince ('fe-izâ') → 'ihtezzet ve rabet': sebep + adlı ara durumlar, mekanizma/ölçü yok — L2; durum adları üçlüsü L3 görünüş/durum koluna sınırda, KAPATILAMAZ; 22:5 aynı terkip ('hâmide'); tarayıcı vermedi"),
 47: dict(kademe='L1', olgu=True, cipa=False, not_="meyvenin tomurcuktan çıkışı (yer adı 'ekmâm') + dişinin gebeliği ve doğurması: süreç fiilleri ve aşama adı (taşıma → doğurma), ara durum/mekanizma/ölçü yok — L1 (35:11 aynı terkip L1); tarayıcı vermedi"),

}

ARIZA = {
 (1, 10): [
  "veri: 41:1 Arapça satırında besmele ayet metnine bitişik (harf 21 → harf3 2; n=1) — veri biçimi, 40:1 ile aynı",
  "esmâ (1022 ailesi): 41:7 'el-âhira' — ölçüm satırı 'MÜHÜRSÜZ', esma_kayit mühür EVET; âhiret, okuyucu kararı 'değil'",
  "biçim (517 ailesi): 41:6 'innemâ' ×2 RES işaretsiz; 41:5 takdimli 'fî âzâninâ', 41:7 takdim + zamir tekrarı, 41:8 takdimli 'lehum' işaretsiz",
  "alıntı sınırı (1017 ailesi): 41:6 've veylun li'l-muşrikîn' 'qul' alıntısının içinde mi dışında mı işaretsiz; 41:9 alıntısının sonu işaretsiz, 41:10-12 devamı olabilir",
  "gloss (1021 ailesi): أذن 'izin verme; kulak' — 41:5 kulak; بشر 'müjde; beşer' iki anlam blokta birlikte (41:4 beşîr, 41:6 beşer); أخر 'geciktirme' — 41:7 âhira",
  "sayım: harekesiz 'fslt' kalıbı 'fussilet' ile 12:94 'fasalat'ı ayırmıyor — sayım ayrıştırılarak verildi",
  "sayı işareti: 41:4 'eksar' yanlış pozitif; 41:6 'vâhid' teklik; 41:10 'erba'a' gerçek sayı",
  "tetik: ilk koşuda 0 uyuşmaz; 41:5 kulaklar ('âzân'), 41:10 dağlar ('revâsî') tetik listesinde değil",
 ],
 (11, 20): [
  "esmâ (1022 ailesi): 41:16 'el-âhira' — ölçüm ORTA 'MÜHÜRSÜZ', esma_kayit mühür EVET; âhiret, okuyucu kararı 'değil'",
  "iltifât (1017 ailesi): 41:12 3MS → 1P ('zeyyennâ'), 41:15 lafız → 1P ('âyâtinâ') — ölçüm satırı iltifât 0",
  "kafiye / yıldız (1001 ailesi): 41:13 kafiye kırığı (fâsıla د) — bilanço ★ kaynağı 'allah, z=-0,53'",
  "gloss (1021 ailesi): سوي 41:11 istevâ (yönelme); صبح 41:12 mesâbîh (kandiller); عود 41:13 Âd (kavim adı); ملك 41:14 melâike; يدي 41:14 'min beyni eydîhim' deyimi; جلد 'deri; kırbaçlama' — 41:20 deri",
  'tetik: ◈B يدي (41:14 deyim — organ değil) satırı dolu yazıldı (ön-kayıt §2); ilk koşuda 0 uyuşmaz',
  "sayım: harekesiz 'a'dâ'u'llâh' kalıbı 'va'du'llâh' ile ayrılmıyor (31 ayet gürültü) — sayım iddia edilmedi; شهد + جلد birlikteliği 24:2, 24:4'te 'celde' (kırbaç) anlamı — ayrı verildi",
 ],
 (21, 30): [
  "esmâ (1022 ailesi): 41:21 'evvele merra' — ölçüm 'esmâ yok', esma_kayit mühür EVET; zarf, okuyucu kararı 'değil'",
  "iltifât / alıntı (1017 ailesi): 41:21 derilerin sözünün sonu işaretsiz ('ve huve halaqakum …' kimin); 41:22 konuşan adsız; 41:23 → 41:24 2MP → 3MP; 41:28 lafız → 1P ('âyâtinâ'); 41:30 meleklerin sözü giriş fiilsiz ('en' tefsîr) — ölçüm satırı iltifât 0",
  "kafiye / yıldız (1001 ailesi): 41:23 ★★ kaynak 'rab, z=2,05' — ayette tek Rab anması 'bi-rabbikum'",
  "gloss (1021 ailesi): صبح 41:23 'asbahtum' (oldunuz) — 41:12 kandiller; قرن 41:25 'quranâ'' (yakın dostlar); جنن 41:25/29 cin, 41:30 cennet; بشر 41:30 'ebşirû' (müjde) — 41:6 beşer",
  "biçim (517 ailesi): 41:29 harfsiz nidâ 'rabbenâ' biçim alanında yok; 41:21, 41:28 takdim işaretsiz",
  "tetik: ◈B يدي (41:25 deyim — organ değil), سمع (41:26 dinleme yasağı) satırları dolu yazıldı (ön-kayıt §2); 'qadem' (41:29) listede değil; ilk koşuda 0 uyuşmaz",
  "sayım: harekesiz 'qurenâ'' kalıbı 'qur'ân' ile ayrılmıyor — kalıp sayımı iddia edilmedi, lemma sayımı (qarîn 7) verildi; 'rabbenâ erinâ' kalıbı sayılmadı",
 ],
 (31, 40): [
  "esmâ (1022 ailesi): 41:31 'velî' ve 'âhir', 41:34 'velî', 41:39 'qadîr', 41:40 'basîr' — ölçüm 'MÜHÜRSÜZ', esma_kayit mühür EVET; okuyucu kararı 31 ve 34 'değil', 39 ve 40 ilâhî",
  "iltifât / alıntı (1017 ailesi): 41:31-32 giriş fiilsiz 1P söz (41:30 'en' sözünün devamı mı) — metin işaretlemiyor; 41:37 → 41:38 2MP → 3MP + 2MS; 41:39 3MS → 1P → 3MS; 41:40 1P → 3MS — ölçüm satırı iltifât 0",
  "kafiye / yıldız (1001 ailesi): 41:35 ★★★ kaynak 'pas, z=3,48' (iki edilgen); 41:39-40 fâsıla ر (41:1-38 ن/م)",
  "gloss (1021 ailesi): نزل 41:32 'nuzul' (ikram); حمم 41:34 'hamîm' (dost — gloss 'kaynar su'); سوي 41:34 'testevî' (eşit olma); نهر 41:37-38 gündüz; سبح 21:33/36:40 'yesbahûn' (yüzme); خشع 41:39 yer için; لقي 41:35 kavuşturulma / 41:40 atılma",
  "biçim (517 ailesi): 41:33 'men ahsenu' sorusu ölçümde kip yok (INTG yakalanmadı); 41:31 takdim işaretsiz",
  'tetik: ◈B سمع (41:36 esmâ), بصر (41:40 esmâ), حيي (41:31 dünya hayatı) satırları dolu yazıldı (ön-kayıt §2); ilk koşuda 0 uyuşmaz',
  "sayım: harekesiz 'mâ teddeûn' 'mâ ted'ûn' ile, 'yulaqqâhâ' 'yelqâhu' (17:13) ile ayrılmıyor — kalıp sayımı iddia edilmedi, lemma sayımı verildi; 've min âyâtih' 12 eşleşmenin biri (20:75) gürültü → 11",
 ],
 (41, 50): [
  "esmâ (1022 ailesi): 41:41 'azîz' (kitabın sıfatı) ve 41:47 'şehîd' (çağrılanların sözünde şahit) — ölçüm 'MÜHÜRSÜZ', esma_kayit mühür EVET; okuyucu kararı ikisi de 'değil'",
  "iltifât / alıntı (1017 ailesi): 41:44 1P → 2MS 'qul', 'qul' sözünün sonu işaretsiz; 41:45 1P → 2MS 'rabbike'; 41:50 1P → 1S alıntı → 1P — ölçüm satırı iltifât 0",
  "kafiye / yıldız (1001 ailesi): 41:43 ★★★ kaynak 'pas, z=5,38' + kafiye kırığı (م); 41:45 ★★ 'pas, z=2,52' + kafiye kırığı (ب); 41:44 ★ 'n, z=1,87', 41:46 ★ 'rab, z=1,62', 41:47 ★ 'n, z=1,65', 41:50 ★★ 'n, z=2,08'; fâsıla bu blokta ز د م د ب د د ص ط ظ",
  "gloss (1021 ailesi): خلف 41:45 'ihtulife' (ayrılığa düşme) — 41:42 'halfih' (arka); أذن 41:47 'âzennâke' (bildirme) — 41:5/44 kulak; ظنن 41:48 'zannû' (anlama); قضي 41:45 hüküm — 41:12 tamamlama",
  "biçim (517 ailesi): 41:46 iki 'men' şartı ölçümde COND yok; 41:41 'inne'nin haberi metinde yok (ölçüm alanı yok) — okumada görüldü",
  'tekrar: 41:45 = 11:110 kelimesi kelimesine (esit2 1,0000 TAM; 11:110 okundu)',
  'tetik: ◈B يدي (41:42 deyim) satırı dolu yazıldı (ön-kayıt §2); ilk koşuda 0 uyuşmaz',
  "sayım: harekesiz 'âzennâke' 28:32 'fe-zânike' ile eşleşiyor (gürültü) — korpusta 1 olarak verildi; 'ye'ûs' Osmânî imlâ — lemma sayımı verildi",
 ],
 (51, 54): [
  "esmâ (1022 ailesi): 41:53 'şehîd', 41:54 'muhît' — ölçüm 'MÜHÜRSÜZ', esma_kayit mühür EVET; okuyucu kararı ikisi de ilâhî",
  "iltifât / alıntı (1017 ailesi): 41:52 'qul' sözünün sonu ayet sonu; 41:53 1P → 2MS → 3MS — ölçüm satırı iltifât 0",
  "gloss (1021 ailesi): عرض 41:51 'arîd' (geniş) — gloss 'sunma; yüz çevirme'; شقق 41:52 'şiqâq' (ayrılık); لقي 41:54 'liqâ'' — 41:35/40 ile üç kullanım",
  "biçim (517 ailesi): 41:51 'izâ' şartları ölçümde COND yok",
  "gönderge: 41:52 'kâne'nin öznesi ve 41:53 'ennehû'nun göndergesi metinde adlanmıyor — KAPATILAMAZ",
  "sayım: harekesiz 've neâ bi-cânibih' Osmânî imlâ ('نـٔا') ile eşleşmiyor — lemma sayımı (neâ 3 ayet) ve esit2 verildi",
 ],
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_41.py uygular)
DUZELTME = {
}
