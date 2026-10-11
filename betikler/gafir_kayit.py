# -*- coding: utf-8 -*-
"""gafir_kayit.py — sûre 40 (Ğâfir) okumasının OKUYUCU KARARLARI (sayı değil, karar).

Sayılar blok_bilanco.py'den koşulur; buraya sayı yazılmaz.
CIPA: yalnız çıpa merdiveninin değerlendirildiği ayetler. Burada olmayan ayet = olgu yok, kademe yok.
  kademe: L0-L4 (onarim/14_cipa_tanimi.py) · olgu: doğal olgu mu · cipa: L4 (çıpa eşiği) mi
ARIZA: blokta görülen alan arızaları / araç açıkları (aday 924: metin hakkında kanıt DEĞİL).
Arapça yok: kökler/lemmalar Latin harfle anılır (korpus kök biçimindeki kök anmaları istisna).
"""
S = 40

CIPA = {
 # blok 1-10: doğal olgu adlanmıyor, tarayıcı v4 adayı yok — kayıt yok
 # blok 11-20
 11: dict(kademe='L1', olgu=True, cipa=False, not_="alıntı içinde: iki ölüm + iki dirim, sayılı (isneteyn ×2), sıra ölüm → dirim; ara durum adsız, hangi ölüm/dirim olduğu söylenmiyor, nedensellik yok; 'üç karanlık' (39:6) gibi sayı + süreç, birim yok — L1; tarayıcı v4 adayı, çıpa değil"),
 13: dict(kademe='L1', olgu=True, cipa=False, not_="gökten rızık indirme: kaynak (semâ) + süreç fiili (yunezzil); indirilen şey adlanmıyor (su/yağmur yok), ara durum/ölçü yok — L1; tarayıcı vermedi"),
 # blok 21-30
 21: dict(kademe='L0', olgu=True, cipa=False, not_="yeryüzü yalnız gezilen yer ve eserlerin (âsâr) yeri olarak adlanıyor; süreç/ölçü yok (39:38 emsali); tarayıcı vermedi"),
 29: dict(kademe=None, olgu=False, cipa=False, not_="tarayıcı v4 adayı (ard, yevm — 'zâhirîne fi'l-ard'): siyasi üstünlük, doğal olgu yok, merdiven uygulanmadı"),
 # blok 31-40
 37: dict(kademe='L0', olgu=True, cipa=False, not_="gökler yalnız 'esbâbe's-semâvât' (göklerin yolları) — Firavun'un ulaşmak istediği yer olarak adlanıyor; süreç/ölçü yok; tarayıcı vermedi"),
 # blok 41-50
 46: dict(kademe='L0', olgu=True, cipa=False, not_="günün iki ucu (ğuduvv / aşiyy) yalnız zaman olarak adlanıyor — ateşe sunuluş vakti; süreç/ölçü yok; tarayıcı vermedi"),
 # blok 51-60
 55: dict(kademe='L0', olgu=True, cipa=False, not_="akşam ve sabah (aşiyy / ibkâr) yalnız tesbih vakti olarak adlanıyor; 40:46 emsali; tarayıcı vermedi"),
 57: dict(kademe='L1', olgu=True, cipa=False, not_="gökler ve yerin yaratılışı insanın yaratılışıyla karşılaştırılıyor ('ekber') — adlandırma + nitelik (büyüklük karşılaştırması); ölçü birimi, süreç, ara durum yok — L1; tarayıcı vermedi"),
 # blok 61-70
 61: dict(kademe='L2', olgu=True, cipa=False, not_="gece dinlenmek İÇİN, gündüz gösterici — işlevsel nedensellik (ta'lîl); 27:86 emsali L2 (aynı terkip 10:67'de); mekanizma/ölçü yok; tarayıcı v4 adayı (B_ta'lîl), çıpa değil"),
 64: dict(kademe='L1', olgu=True, cipa=False, not_="yer durak (qarâr), gök bina — adlandırma + nitelik; 27:61 emsali L1; ilişki/süreç yok; tarayıcı vermedi"),
 67: dict(kademe='L2', olgu=True, cipa=False, not_="toprak → nutfe → alaka → bebek → güçlü çağ → yaşlılık: altı aşama 'summe' ×5 ile sıralı, ara aşamalar ADLI; ta'lîl ('li-teblüğû', 'li-tekûnû') + 'ecel musemmâ'; süreç kolu L4'e sınırda ama mekanizma ve birim yok — L2, KAPATILAMAZ (22:5 aynı dizi); tarayıcı v4 adayı (B_ta'lîl, C_recâ), çıpa değil"),
 # blok 71-80
 79: dict(kademe='L1', olgu=True, cipa=False, not_="davarlar adlanıyor + işlev (binme, yeme) — adlandırma + işlev (27:63 emsali L1); nedensellik/ölçü yok; tarayıcı vermedi"),
 80: dict(kademe='L1', olgu=True, cipa=False, not_="davarlarda faydalar, üzerlerinde ve gemilerde taşınma; ta'lîl ('li-teblüğû … hâceten') insan ihtiyacına — işlev, doğal olgu içi nedensellik yok — L1; 'fulk' gemi, kozmik öğe değil (S2 açık); tarayıcı v4 adayı (فلك, B_ta'lîl), çıpa değil"),
 # blok 81-85
 82: dict(kademe='L0', olgu=True, cipa=False, not_="yeryüzü yalnız gezilen yer ve eserlerin (âsâr) yeri olarak adlanıyor; 40:21 emsali L0; tarayıcı vermedi"),
}

ARIZA = {
 (1, 10): [
  "veri: 40:1 Arapça satırında besmele ayet metnine bitişik (harf 21 → harf3 2; n=1) — veri biçimi, 39:1 ile aynı",
  "esmâ: 40:3 dört tamlama (ğâfiru'z-zenb, qâbilu't-tevb, şedîdu'l-iqâb, zû't-tavl) esmâ satırında 'yok', eksen 'lafız YOK · Rab YOK' — tamlamalar 40:2'nin lafzına bağlı, set 72 dışında (924 ailesi)",
  "biçim (517 ailesi): 40:7 ve 40:8 harfsiz nidâ 'rabbenâ' biçim alanında yok; 40:3 takdimli 'ileyhi'l-masîr' işaretsiz; 40:9 ayırma zamiri 'huve' işaretsiz",
  "alıntı sınırı (1017 ailesi): 40:7-9 dua, giriş fiili söz fiili değil ('yestağfirûn'); bitişi 40:9 son cümlede KAPATILAMAZ",
  "sayı işareti: 40:8 zevc (ezvâc, eşler) yanlış pozitif — 39:6 emsali",
  "gloss (1021 ailesi): حول 'çevirme, değiştirme' — 40:7 havl (çevre), 39:75 emsali",
  "tetik: ◈B قلب (40:4 teqallub, dolaşma), حمل (40:7 Arş'ı taşıma), زوج (40:8 eşler) — tetik kökü organ/oluşum anlamında değil; satır dolu yazıldı (ön-kayıt §2)",
  "sayım: harekesiz metin eşleşmesinde 1S 'fe-ehaztuhum' ile 3FS 'fe-ehazethum' ayrılmıyor — o sayım iddia edilmedi",
 ],
 (11, 20): [
  "esmâ (1022 ailesi): 40:16 ölçüm satırı qahhâr 'MÜHÜRSÜZ', esma_kayit ve bilanço mühür EVET (geçerli); 'vâhid' esmâ satırında yok (sayı işareti olarak var)",
  "esmâ (924 ailesi): 40:15 'rafî'u'd-derecât', 'zu'l-arş'; 40:17 'serî'u'l-hisâb' — lafızsız tamlamalar/haberler esmâ satırında yok (40:3 emsali)",
  "biçim (517 ailesi): 40:11 harfsiz nidâ; 40:12 takdimli 'li'llâh'; 40:16 soru-cevap ('li-meni'l-mulk' / 'li'llâh') edim 'haber'; 40:20 ayırma zamiri 'huve'",
  "alıntı sınırı (1017 ailesi): 40:12 konuşanı adsız 2MP hitap; 40:16 soru ve cevap tırnaksız, ikisinin konuşanı da adsız; 40:17 cevabın devamı mı anlatıcı mı KAPATILAMAZ",
  "tetik: ◈B سمع, بصر (40:20) esmâ sıfatı olarak — organ değil",
  "sayım: harekesiz eşleşmede 'emettenâ' ile 'mitnâ' ayrılmıyor; 'hâinete' ile 'hıyânete' ayrılmıyor — o sayımlar iddia edilmedi (lemma sayımı kullanıldı)",
 ],
 (21, 30): [
  "bilanço ★ kaynağı (1001 ailesi): 40:23 'n, z=-0,68', 40:29 'n, z=1,44', 40:30 'allah, z=-0,53' — üçü de kafiye kırığı ayeti, gerçek kaynak kafiye kırığı",
  "esmâ (1022 ailesi): 40:22 qaviyy ölçüm satırında 'MÜHÜRSÜZ', esma_kayit/bilanço EVET; 40:27 'mutekebbir' ölçüm satırında 'esmâ yok', esma_kayit e_oto (karar: değil)",
  "esmâ (okuyucu kararı 'değil' ×4): 40:23 mubîn (sultân), 40:27 mutekebbir, 40:28 mu'min (adam), 40:29 zâhirîn — set eşleşmesi insan sıfatlarına düşüyor",
  "alıntı sınırı (1017 ailesi): 40:24 konuşan 3MP, üç adlı aktörden hangileri KAPATILAMAZ; 40:25 son cümle alıntı mı anlatıcı mı; 40:29 'yâ qavmi' konuşanı adsız (40:28 alıntısının devamı olarak okunuyor); 40:30 'ellezî âmen' = 40:28 adamı mı KAPATILAMAZ",
  "biçim (517 ailesi): 40:21 zamir tekidi 'hum' işaretsiz; iltifât alanı 40:23 (3 → 1P) ve 40:24 (1 — alıntıya geçiş) işaretli, 40:5 1S geçişi işaretsizdi",
  "sayım: 'yâ qavmi' harekesiz eşleşmede fiillerle karışıyor ('yeqûm'); 'sebîle'r-reşâd' ile 'sebîle'r-ruşd' ayrılmıyor — lemma sayımı kullanıldı",
 ],
 (31, 40): [
  "alıntı sınırı (1017 ailesi): 40:30-33 tek alıntı (40:31 'misle de'b' 40:30 'misl'inin bedeli); 40:34-35 konuşanı (iman eden mi anlatıcı mı) KAPATILAMAZ; 40:37 alıntı ayet ortasında bitiyor, anlatıcı devralıyor; 40:38'de açılan alıntının bitişi 40:39/40:40'ta işaretsiz",
  "esmâ (okuyucu kararı 'değil' ×5): 40:33 hâd, 40:35 mutekebbir + cebbâr (kalbin sıfatları), 40:39 âhira, 40:40 mu'min — set eşleşmesi yine insan/nesne sıfatlarına düşüyor; bilanço geçerli mühür 0",
  "biçim (517 ailesi): 40:39 'innemâ' hasrı 'DIKKAT' olarak işaretli, hasr yok; 'hiye' ayırma zamiri işaretsiz; 40:33 ve 40:40 şart cümleleri edim 'haber'; 40:36 terecci ('le'alle') işaretsiz",
  "bilanço ★ kaynağı (1001 ailesi): 40:35 'allah, z=2,08' ve 40:40 'pas, z=1,95' — ikisi de kafiye kırığı ayeti; kaynaklar eşiği geçiyor, kafiye kırığı ayrıca",
  "gloss (1021 ailesi): بني 'bina, yapma' — 40:25 ebnâ (oğullar) / 40:36 ibni (yap); ذكر 'anma, zikir' — 40:40 zeker (erkek)",
  "sayım: 'yâ Hâmân', 'el-hayâtu'd-dunyâ', 'etâhum' harekesiz eşleşmede ilk kalıpla 0 verdi (ٰ ve elif-maksûre) — Osmanlı imlâsıyla yeniden sayıldı; 'yâ Hâmân' lemma birlikteliğiyle sayıldı",
 ],
 (41, 50): [
  "alıntı sınırı (1017 ailesi): 40:41-44 iman edenin konuşması giriş fiilsiz sürüyor (40:38'den), bitişi 40:44'te işaretsiz; 40:46 'edhilû' emrinin konuşanı ve muhatabı adsız, giriş fiilsiz; 40:50 üç 'qâlû' — konuşan sırası (bekçiler / ateştekiler / bekçiler) okumadan, son cümle bekçilerin mi anlatıcının mı KAPATILAMAZ",
  "esmâ (1022 ailesi): 40:44 basîr ölçüm satırında 'MÜHÜRSÜZ', esma_kayit mühür EVET",
  "biçim (517 ailesi): 40:41 'mâ lî' sorusu edim alanında yok (nidâ); 40:43 'lâ cerame' + 'enne' ×3 + 'hum' tekidi işaretsiz",
  "gloss (1021 ailesi): أول 'ilk, evvel' — 40:28, 40:45, 40:46 'âl' (aile)",
  "tetik: ◈B بصر (40:44) esmâ olarak — organ değil",
  "sayım: 'seyyiâti mâ mekerû' ve 'bi'l-ğuduvvi ve'l-aşiyy' harekesiz kalıpla 0 verdi (imlâ) — iddia edilmedi; غدو + عشو lemma birlikteliği kullanıldı",
 ],
 (51, 60): [
  "biçim (517 ailesi): 40:52 takdimli 'lehum' ×2 işaretsiz; 40:56 ayırma zamiri 'huve' işaretsiz",
  "sayı işareti: 40:57, 40:59 'eksar' ve 40:58 'qalîl' yanlış pozitif (39:8, 39:29 emsali)",
  "esmâ: 40:58 'basîr' (gören insan, körün karşıtı) set eşleşmesi — okuyucu kararı 'değil'; 40:56 aynı kelime esmâ",
  "gloss (1021 ailesi): بني 'bina, yapma' — 40:53 benî (oğulları); قوم 'kalkma; kavim; kıyamet' üç anlam blokta birlikte (40:51 yeqûmu'l-eşhâd)",
  "tetik: ilk koşuda 2 uyuşmaz — 40:55 ◈K dolu yazılmıştı (عشو, بكر tetik değil), 40:59 ◈B '—' yazılmıştı (أنس tetik) — kayıttan önce düzeltildi",
  "sayım: 'el-eşhâd' harekesiz eşleşmede 'eş-şuhedâ' ile, 'lâ rayba fîhâ' 'fîhi' ile ayrılmıyor — o sayımlar iddia edilmedi; 'eşhâd' lemması 'şâhid' altında",
 ],
 (61, 70): [
  "esmâ (1022 ailesi): 40:65 'el-hayy' ölçüm satırında 'esmâ yok', esma_kayit D2 eşlemesiyle e_oto 1 — iki araç ayrışıyor; okuyucu kararı ilâhî",
  "alıntı sınırı (1017 ailesi): 40:66 'qul' alıntısının bitişi işaretsiz — 40:67'nin 2MP hitabı devam da olabilir, meal ayet sonunda kapattı; 40:65 'el-hamdu li'llâh' cümlesinin konuşanı adsız",
  "biçim (517 ailesi): 40:68 'innemâ' (RES) biçim alanında yok; 40:68 'kun' 2MS etiketi — muhatap 'emr' (iş), şahıs etiketi biçimsel",
  "gloss (1021 ailesi): سمو 'ad; gök' — 40:67 musemmâ (adlandırılmış), sûredeki önceki dört geçiş 'gök'; شدد 'şiddet, katılık' — 40:67 eşudd (güçlü çağ)",
  "yıldız (924 ailesi): 40:62 ★★★ kaynağı pas z=5,38 — ayette tek fiil, edilgen oranı 1/1; küçük paydalı oran, metin hakkında kanıt değil",
  "tetik: ilk koşuda 0 uyuşmaz; 40:64 'savvera' (صور) ve 40:61 'li-teskunû' (سكن) tetik listesinde değil — ◈B 40:64 '—'",
  "sayım: Osmânî imlâda 'el-leyl' tek lam ve vasıl elifiyle, 'yuhyî' sonu küçük ye ile yazılı — harekesiz kalıplar bu imlâya göre kuruldu (ilk denemede 0 verdi); harekesiz 'qul' 'qâle' ile ayrılmıyor — 'qul' sayımı iddia edilmedi",
 ],
 (71, 80): [
  "esmâ (1022 ailesi): 40:76 'el-mutekebbirîn' — ölçüm satırı 'esmâ yok', esma_kayit son konumda mühür EVET; çoğul, insan — okuyucu kararı 'değil'",
  "alıntı sınırı (1017 ailesi): 40:73 sorusu 40:74 'min dûni'llâh' ile bitiyor (ayet sınırını aşıyor); 40:75-76 konuşanı adsız, alıntı işaretsiz başlıyor; 40:76 'fe-bi'se mesve'l-mutekebbirîn' içeride mi dışarıda mı KAPATILAMAZ",
  "biçim (517 ailesi): 40:77 takdimli 'ileynâ', 40:79 'minhâ', 40:80 'lekum' ve 'aleyhâ' işaretsiz",
  "gloss (1021 ailesi): حمم 'kaynar su, hamîm' — 40:18 hamîm (yakın dost); نور 'nûr, ışık; nâr, ateş' — sûredeki 8 geçişin hepsi 'nâr'",
  "tetik: ◈K سحب (40:71 yushabûn, sürüklenme — bulut değil) ve فلك (40:80 fulk, gemi — S2 açık, 37:140 emsali) — tetik kökü kozmik anlamda değil; satırlar dolu yazıldı (ön-kayıt §2); ilk koşuda 0 uyuşmaz",
  "yıldız (924 ailesi): 40:71 ve 40:72 ★★★ kaynağı pas z=5,38 — ikisinde de tek fiil, edilgen oranı 1/1 (40:62 emsali)",
  "sayım: 'ce'ale lekumu'l-en'âm' ve 'menâfi'' Osmânî imlâya göre harekesiz kalıpla sayıldı; 'dallû annâ' 3 ayet / 'qâlû dallû annâ' 2 ayet ayrı verildi",
 ],
 (81, 85): [
  "gloss (1021 ailesi): أيي 'âyet, işaret' — 40:81 'eyye' (hangi) aynı kök kaydında; أثر 'tercih etme, üstün tutma' — 40:21 ve 40:82 'âsâr' (izler, eserler)",
  "sayı işareti: 40:82 'eksar' yanlış pozitif; 40:84 'vahd' teklik — sayım değil",
  "sayım: 'sunnete'llâh' açık te imlâsıyla harekesiz kalıpta 2 ayet; yuvarlak te ile yazılan yerler (33:38, 33:62, 48:23 xref) bu kalıba girmiyor — lemma 'sunne' 15 ayet ayrıca verildi; 'yurîkum âyâtih' kalıbı başta 've' ile 1 sûre içi ayeti kaçırdı, 've'siz yeniden sayıldı (3 ayet)",
  "sûre sınırı: 40:85 → 41:1 bağı aday 1040 alanında — 41 henüz okunmadı; sınır gözlemi yazılmadı, test sonda",
  "tetik: 0 uyuşmaz",
 ]
}

# Kendi kaydım düştüğünde özgün alan korunur; düzeltme ayrı alana yazılır (duzeltme_40.py uygular)
DUZELTME = {
 30: dict(alan='meal', eski="bir benzerinden korkuyorum.\"",
          dogru="40:30 meali tırnağı ayet sonunda kapattı; oysa 40:31 'misle de'bi qavmi Nûh…' 40:30 'misle yevmi'l-ahzâb'ın bedeli — alıntı 40:31-33'te sürüyor (40:34-35 konuşanı KAPATILAMAZ). Özgün meal korunur; doğru okuma: tırnak 40:33 sonuna dek açık.",
          aday=None, blok='31-40'),
}
