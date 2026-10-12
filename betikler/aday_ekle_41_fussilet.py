# -*- coding: utf-8 -*-
"""aday_ekle_41_fussilet.py — sûre 41 (Fussilet) adayları (AX_fussilet) ve okuma bağları (AS_fussilet).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1041'den); betik sıranın kopmadığını doğrular.
"""
import json

FUSSILET = [
]

BAGLAR = {"AS_fussilet": [
 {'bag': '40:1 → 41:1', 'kural': "esit2 TAM — 'Hâ Mîm' 40:1-46:1 yedi sûre (ölçüm); 40:1 okundu", 'not': 'Hâ Mîm ailesi.'},
 {'bag': '40:2 → 41:2', 'kural': "okuma — ikinci ayette 'tenzîl' + kaynak: Allah (azîz, alîm) / Rahmân, Rahîm; aday 1040 alanı (aile içi, sınır değil), test yok", 'not': 'indirme.'},
 {'bag': '12:2 · 20:113 · 39:28 → 41:3', 'kural': "metin sayımı 'qur'ânen arabiyyâ' 6 ayet; okundu", 'not': "Arapça Kur'an."},
 {'bag': '34:28 · 35:24 → 41:4', 'kural': "metin sayımı 'beşîran ve nezîrâ' 5 ayet; okundu — orada elçi, burada kitap; okumada görüldü, KAPATILAMAZ", 'not': 'müjdeleyici, uyarıcı.'},
 {'bag': '17:46 · 18:57 → 41:5', 'kural': "lemma birlikteliği 'ekinne' + 'vaqr' 4 ayet; okundu — 1P 'ce'alnâ' / inkâr edenlerin kendi sözü; okumada görüldü, KAPATILAMAZ", 'not': 'örtü, ağırlık.'},
 {'bag': '18:110 → 41:6', 'kural': "metin sayımı 'qul innemâ ene beşerun mislukum yûhâ ileyye ennemâ ilâhukum ilâhun vâhid' 2 ayet + xref; okundu", 'not': 'sizin gibi bir insan.'},
 {'bag': '27:3 · 31:4 → 41:7', 'kural': "xref — 'yu'tûne'z-zekâte ve hum bi'l-âhirati hum yûqinûn' / 'lâ yu'tûne'z-zekâte … hum kâfirûn'; okundu, okumada görüldü", 'not': 'zekât ve âhiret.'},
 {'bag': '11:19 · 12:37 → 41:7', 'kural': "metin sayımı 've hum bi'l-âhirati hum kâfirûn' 3 ayet; okundu", 'not': 'âhireti inkâr.'},
 {'bag': '40:85 → 41:7', 'kural': "okuma — 'el-kâfirûn' sûre sonu / 'kâfirûn' ayet sonu; aday 1040 alanında kayıt, test değil", 'not': 'inkâr edenler.'},
 {'bag': '13:3 → 41:10', 'kural': "metin sayımı 've ce'ale fîhâ revâsiye' 2 ayet; okundu", 'not': 'sabit dağlar.'},
 {'bag': '41:9 → 41:10', 'kural': "okuma — sayılı gün adları 'yevmeyn' / 'erba'ati eyyâm' ayrı ayetlerde; ilişkisi metinde açıklanmıyor, KAPATILAMAZ", 'not': 'günler.'},
 {'bag': '9:53 → 41:11', 'kural': "metin sayımı 'tav'an ev kerhâ' 2 ayet; okundu — infak / gök ve yerin gelişi", 'not': 'isteyerek ya da istemeyerek.'},
 {'bag': '41:9 → 41:12', 'kural': "okuma — 'fî yevmeyn' sûre içi 2 ayet: yer / gökler", 'not': 'iki gün.'},
 {'bag': '41:6 → 41:12', 'kural': 'kök ipliği وحي kapanıyor [2/2] — insana vahy (edilgen) / göğe vahy; okumada görüldü', 'not': 'vahiy.'},
 {'bag': '36:38 → 41:12', 'kural': "metin sayımı 'zâlike taqdîru'l-azîzi'l-alîm' 3 ayet; okundu (güneşin akışı / yedi gök)", 'not': 'azîz ve alîm olanın takdiri.'},
 {'bag': '37:6 → 41:12', 'kural': 'xref — dünya göğünün süslenmesi; okundu', 'not': 'dünya göğü.'},
 {'bag': '41:10 → 41:12', 'kural': "kök ipliği قدر — 'qaddera aqvâtehâ' / 'taqdîr'", 'not': 'takdir.'},
 {'bag': '41:4 → 41:13', 'kural': "kök ipliği عرض + نذر — 'fe-a'rada ekseruhum' / 'fe-in a'radû'; 'nezîr' / 'enzertukum'", 'not': 'yüz çevirme, uyarı.'},
 {'bag': '11:2 · 11:26 → 41:14', 'kural': "metin sayımı 'ellâ ta'budû illa'llâh' 4 ayet; okundu", 'not': "Allah'tan başkasına kulluk etmeyin."},
 {'bag': '23:24 → 41:14', 'kural': "metin sayımı 'le-enzele melâike' 2 ayet; okundu — 'lev şâe'llâh' / 'lev şâe rabbunâ'", 'not': 'melek indirirdi.'},
 {'bag': '34:34 → 41:14', 'kural': "metin sayımı 'bi-mâ ursiltum bihî kâfirûn' 3 ayet; okundu", 'not': 'gönderildiğinizi inkâr.'},
 {'bag': '30:9 · 35:44 · 40:21 → 41:15', 'kural': "metin sayımı 'eşeddu minhum quvveten' 4 ayet; okundu", 'not': 'daha güçlü.'},
 {'bag': '40:75 → 41:15', 'kural': "okuma — 'fi'l-ardı bi-ğayri'l-haqq': sevinme / büyüklenme", 'not': 'haksız yere.'},
 {'bag': '40:63 → 41:15', 'kural': "okuma — 'bi-âyâti'llâhi yechadûn' / 'bi-âyâtinâ yechadûn'", 'not': 'bile bile inkâr.'},
 {'bag': '10:98 → 41:16', 'kural': "metin sayımı 'azâbe'l-hizyi fi'l-hayâti'd-dunyâ' 2 ayet; okundu — kaldırılan / tattırılan azap", 'not': 'rezillik azabı.'},
 {'bag': '9:23 · 16:107 → 41:17', 'kural': "metin sayımı 'istehabbû' 3 ayet, üçü de 'X alâ Y' kalıbı; okundu", 'not': 'tercih etme.'},
 {'bag': '41:13 → 41:17', 'kural': 'kök ipliği صعق kapanıyor [3/3] — uyarılan yıldırım / gerçekleşen yıldırım', 'not': 'yıldırım.'},
 {'bag': '41:15 ↔ 41:17', 'kural': "okuma — biçim AMMA ikilisi: 'fe-emmâ Âd' / 've emmâ Semûd'", 'not': 'Âd ve Semûd.'},
 {'bag': '27:53 → 41:18', 'kural': "esit2 YAKIN (0,9811) + metin sayımı 've necceynâ'llezîne âmenû ve kânû yetteqûn' 2 ayet; okundu — ikisinde de Semûd anlatısının sonu", 'not': 'kurtuluş.'},
 {'bag': '27:17 · 27:83 → 41:19', 'kural': "metin sayımı 'fe-hum yûza'ûn' 3 ayet; okundu", 'not': 'dizilirler.'},
 {'bag': '24:24 · 36:65 → 41:20', 'kural': 'okuma — organların şahitliği: diller-eller-ayaklar / eller-ayaklar / kulak-göz-deri; okundu, KAPATILAMAZ', 'not': 'organların şahitliği.'},
 {'bag': '18:48 · 36:79 → 41:21', 'kural': "metin sayımı 'evvele merra' 9 ayet; okunan 9:13, 9:83, 17:7, 17:51, 18:48, 36:79", 'not': 'ilk kez yaratma.'},
 {'bag': '41:20 → 41:22', 'kural': 'okuma — aynı üç organ aynı sırada, 3MP → 2MP; sûre içi', 'not': 'organ üçlüsü.'},
 {'bag': '41:12 → 41:23', 'kural': 'kök ikilemesi صبح [2/2] — mesâbîh / asbahtum; gloss iki anlam (1021)', 'not': 'صبح.'},
 {'bag': '10:95 · 11:47 · 39:65 → 41:23', 'kural': "metin sayımı 'mine'l-hâsirîn' 10 ayet; okundu", 'not': 'hüsrana uğrayanlar.'},
 {'bag': '41:14 → 41:25', 'kural': "okuma — 'beyne eydîhim … halfihim' ikilisi: elçilerin geldiği yön / yakın dostların süslediği; KAPATILAMAZ", 'not': 'önleri / arkaları.'},
 {'bag': '41:12 → 41:25', 'kural': "kök ikilemesi زين [2/2] — 1P 'zeyyennâ' / 'fe-zeyyenû'; okumada görüldü", 'not': 'süsleme.'},
 {'bag': '28:63 → 41:25', 'kural': "metin sayımı 've haqqa aleyhimu'l-qavl' 3 ayet; okundu", 'not': 'söz hak oldu.'},
 {'bag': '41:4 → 41:26', 'kural': "okuma — 'lâ yesme'ûn' / 'lâ tesme'û'; سمع", 'not': 'işitmeme / dinleme yasağı.'},
 {'bag': '39:35 → 41:27', 'kural': "metin sayımı 'esve'e'llezî' 2 ayet; okundu — bağışlanan / karşılığı verilen; KAPATILAMAZ", 'not': 'en kötüsü.'},
 {'bag': '41:15 → 41:28', 'kural': "kök ikilemesi جحد [2/2] — 'bi-âyâtinâ yechadûn' aynı kalıp; sûre içi", 'not': 'bile bile inkâr.'},
 {'bag': '41:19 → 41:28', 'kural': "okuma — 'a'dâu'llâh' sûre içi ikinci kez", 'not': 'Allah düşmanları.'},
 {'bag': '41:26 → 41:29', 'kural': "okuma — 'qâle'llezîne keferû' iki alıntı: dünya / âhiret", 'not': 'inkârcıların iki sözü.'},
 {'bag': '41:6 → 41:30', 'kural': "kök ikilemesi قوم — 'fe'staqîmû' / 'summe'staqâmû'; okumada görüldü", 'not': 'dosdoğruluk.'},
 {'bag': '41:14 → 41:30', 'kural': "kök ikilemesi ملك [2/2] — 'le-enzele melâike' / 'tetenezzelu … el-melâike'; KAPATILAMAZ", 'not': 'meleklerin inişi.'},
 {'bag': '36:63 → 41:30', 'kural': "metin sayımı 'elletî kuntum tû'adûn' 2 ayet; okundu — cehennem / cennet", 'not': 'vaat edilen.'},
 {'bag': '41:29 → 41:30', 'kural': "okuma — 'rabbenâ' (inkârcılar) / 'rabbuna'llâh'", 'not': 'iki Rab anması.'},
 {'bag': '10:64 · 14:27 → 41:31', 'kural': "metin sayımı 'fi'l-hayâti'd-dunyâ ve fi'l-âhira' 3 ayet; okundu", 'not': 'dünya ve âhiret.'},
 {'bag': '41:30 → 41:31', 'kural': "okuma — giriş fiilsiz 1P söz, 'en' sözünün devamı olarak okunabilir; 1017, KAPATILAMAZ", 'not': 'meleklerin sözü?'},
 {'bag': '41:30 → 41:32', 'kural': "kök ikilemesi نزل — 'tetenezzelu' / 'nuzul'", 'not': 'iniş / ikram.'},
 {'bag': '41:5 → 41:33', 'kural': "kök ikilemesi دعو — 'mimmâ ted'ûnâ ileyh' / 'deâ ila'llâh'; okumada görüldü", 'not': 'çağrı.'},
 {'bag': '23:96 → 41:34', 'kural': "metin sayımı 'idfa' bi'lletî hiye ahsen' 2 ayet; okundu — 23:96'da nesne açık, 41:34'te yok", 'not': 'en güzelle savma.'},
 {'bag': '41:31 → 41:34', 'kural': "kök ikilemesi ولي [2/2] — 'evliyâ' / 'velî'", 'not': 'dostluk.'},
 {'bag': '28:80 → 41:35', 'kural': "lemma 'luqqiya' + 'hâ' + 'illâ' + sabır; okundu", 'not': 'ancak sabredenler.'},
 {'bag': '28:79 → 41:35', 'kural': "metin sayımı 'zû hazzin azîm' 2 ayet; okundu — Kârûn / sabredenler; KAPATILAMAZ", 'not': 'büyük pay.'},
 {'bag': '41:24 → 41:35', 'kural': "kök ikilemesi صبر [2/2] — 'in yasbirû' / 'sabarû'", 'not': 'sabır.'},
 {'bag': '12:34 · 26:220 → 41:36', 'kural': "metin sayımı 'innehû huve's-semî'u'l-alîm' 5 ayet; okundu", 'not': 'işiten, bilen.'},
 {'bag': '12:4 · 22:18 · 27:24 → 41:37', 'kural': 'kök birlikteliği شمس + سجد 4 ayet; okundu — secde eden güneş-ay / güneşe secde eden kavim / yasak', 'not': 'güneşe secde.'},
 {'bag': '16:12 · 21:33 → 41:37', 'kural': "metin sayımı 'el-leylu ve'n-nehâru ve'ş-şemsu ve'l-qamer' 3 ayet; okundu", 'not': 'dört âyet.'},
 {'bag': '21:20 → 41:38', 'kural': "kök birlikteliği سبح + ليل + نهر; okundu — 'lâ yefterûn' / 'lâ yes'emûn'", 'not': 'usanmadan tesbih.'},
 {'bag': '41:15 → 41:38', 'kural': "kök ikilemesi كبر [2/2] — Âd 'fe'stekberû' / 'ini'stekberû'", 'not': 'büyüklenme.'},
 {'bag': '22:5 → 41:39', 'kural': "metin sayımı 'fe-izâ enzelnâ aleyhe'l-mâe'htezzet ve rabet' 2 ayet; okundu — hâmide / hâşi'a", 'not': 'yerin kabarması.'},
 {'bag': '30:50 → 41:39', 'kural': "metin sayımı 'le-muhyi'l-mevtâ' 2 ayet; okundu", 'not': 'ölüleri dirilten.'},
 {'bag': '41:35 → 41:40', 'kural': 'kök ikilemesi لقي — kavuşturulma / atılma (1021)', 'not': 'لقي iki anlam.'},
 {'bag': '41:20 · 41:22 → 41:40', 'kural': 'kök ikilemesi بصر [3/3] — organ / esmâ', 'not': 'görme.'},
 {'bag': '41:12 → 41:41', 'kural': "kök ikilemesi عزز [2/2] — esmâ 'el-azîz' / 'kitâbun azîz'", 'not': 'izzet.'},
 {'bag': '41:14 · 41:25 → 41:42', 'kural': "okuma — 'beyne yedeyhi … halfihî' ikilisi sûrede üçüncü kez, üçüncü özne (elçiler / yakın dostlar / bâtıl); KAPATILAMAZ", 'not': 'önden / arkadan.'},
 {'bag': '41:2 → 41:42', 'kural': "metin sayımı 'tenzîlun min' 4 ayet; sûre içi — Rahmân-Rahîm / Hakîm-Hamîd", 'not': 'indirme.'},
 {'bag': '13:6 → 41:43', 'kural': "metin sayımı 'le-zû mağfira' 2 ayet; okundu — mağfiret / ceza ikilisi", 'not': 'bağışlama ve ceza.'},
 {'bag': '41:3 → 41:44', 'kural': "kök ikilemeleri فصل [2/2], عرب [2/2] — 'fussilet âyâtuhû', 'arabiyy'", 'not': "ayrıntılı Arapça Kur'an."},
 {'bag': '41:5 → 41:44', 'kural': "kök ikilemesi وقر [2/2] — 'fî âzâninâ vaqr' (1P) / 'fî âzânihim vaqr' (3MP); okumada görüldü", 'not': 'kulaktaki ağırlık.'},
 {'bag': '41:17 → 41:44', 'kural': "kök ikilemesi عمي [2/2] + هدي — Semûd körlüğü / 'aleyhim amâ'", 'not': 'körlük ve hidayet.'},
 {'bag': '10:57 → 41:44', 'kural': "kök + kelime: 'şifâ'' ve 'huden' ikilisi; okundu", 'not': 'hidayet ve şifa.'},
 {'bag': '11:110 → 41:45', 'kural': 'esit2 1,0000 TAM — kelimesi kelimesine aynı ayet; okundu', 'not': "Musa'nın kitabı, ayrılık."},
 {'bag': '10:19 → 41:45', 'kural': "metin sayımı 've lev lâ kelimetun sebaqat min rabbike le-quziye beynehum' 3 ayet; okundu", 'not': 'önceden verilmiş söz.'},
 {'bag': '22:10 → 41:46', 'kural': "metin sayımı 'bi-zallâmin li'l-abîd' 5 ayet; okundu", 'not': 'kullara zulmetmez.'},
 {'bag': '31:34 → 41:47', 'kural': "metin sayımı 'ilmu's-sâ'a' 3 ayet; okundu", 'not': 'saatin bilgisi.'},
 {'bag': '35:11 → 41:47', 'kural': "metin sayımı 've mâ tahmilu min unsâ ve lâ teda'u illâ bi-ilmih' 2 ayet; okundu", 'not': 'gebelik ve doğum.'},
 {'bag': '28:62 · 28:74 → 41:47', 'kural': "metin sayımı 've yevme yunâdîhim' / 'eyne şurekâî'; okundu", 'not': 'ortaklarım nerede.'},
 {'bag': '40:74 → 41:48', 'kural': "xref 'dalle … kânû yed\\'ûne'; okundu", 'not': 'kaybolan ortaklar.'},
 {'bag': '41:38 → 41:49', 'kural': "kök ikilemesi سأم [2/2] — 'lâ yes'emûn' / 'lâ yes'emu'l-insân'; okumada görüldü", 'not': 'usanmamak.'},
 {'bag': '17:83 → 41:49', 'kural': "metin sayımı 'messehu'ş-şerr' + 'ye'ûs'; okundu", 'not': 'şer dokununca umutsuzluk.'},
 {'bag': '18:36 → 41:50', 'kural': "metin sayımı 've mâ ezunnu's-sâ'ate qâimeten' 2 ayet; okundu — bahçe sahibinin sözü", 'not': 'kıyameti sanmamak.'},
 {'bag': '11:10 → 41:50', 'kural': "xref 'ba'de darrâe messethu'; okundu", 'not': 'sıkıntıdan sonra rahmet.'},
 {'bag': '17:83 → 41:51', 'kural': "esit2 0,8515 BENZER + metin sayımı 'en'amnâ ale'l-insân' 2 ayet; okundu — aynı şart ikilisi, sonu 'ye'ûs' / 'duâin arîd'", 'not': 'nimet ve şer.'},
 {'bag': '41:49 → 41:51', 'kural': "metin sayımı 'messehu'ş-şerr' sûre içi ×2 — umutsuzluk / geniş dua; KAPATILAMAZ", 'not': 'şer dokununca.'},
 {'bag': '41:4 · 41:13 → 41:51', 'kural': "kök ikilemesi عرض [4/4] — 'a'rada' / 'a'radû' / 'a'rada' + 'arîd'", 'not': 'yüz çevirme.'},
 {'bag': '22:53 → 41:52', 'kural': "metin sayımı 'fî şiqâqin baîd' 3 ayet; okundu", 'not': 'derin ayrılık.'},
 {'bag': '28:50 → 41:52', 'kural': "metin sayımı 'men edallu mimmen' 3 ayet; okundu", 'not': 'daha sapkın kim.'},
 {'bag': '41:20 · 41:47 → 41:53', 'kural': "kök ikilemesi شهد [5/5] — organların şahitliği / 'şehîd' yok / Rab her şeye şahit", 'not': 'şahitlik.'},
 {'bag': '22:17 · 34:47 → 41:53', 'kural': "metin sayımı 'alâ kulli şey'in şehîd' 8 ayet; okundu", 'not': 'her şeye şahit.'},
 {'bag': '32:23 → 41:54', 'kural': "metin sayımı 'fî mirye'; okundu — Musa'nın kitabı + 'fî miryetin min liqâ'' tek ayette (41:45 + 41:54); KAPATILAMAZ", 'not': 'kavuşma kuşkusu.'},
 {'bag': '41:35 · 41:40 → 41:54', 'kural': 'kök ikilemesi لقي [4/4] — kavuşturulma / atılma / kavuşma (1021)', 'not': 'لقي üç kullanım.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_fussilet', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in FUSSILET]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_fussilet'] = FUSSILET
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_fussilet', len(FUSSILET), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_fussilet', len(BAGLAR['AS_fussilet']))
