# -*- coding: utf-8 -*-
"""aday_ekle_55_rahman.py — sûre 55 (Rahmân) adayları (AX_rahman) ve okuma bağları (AS_rahman).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

RAHMAN = [
]

BAGLAR = {"AS_rahman": [
 {'bag': '54:55 → 55:1', 'kural': "okuma — ardışık sûre sınırı; fâsıla ر → ن; 'melîk muqtedir' / 'er-rahmân' (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '20:5 → 55:1', 'kural': "tam kalıp 'er-rahmân' 45 ayet — ayet başı mübteda / tek kelimelik ayet", 'not': 'Rahmân.'},
 {'bag': '53:5 → 55:2', 'kural': "lemma 'allema' 35 ayet — öğreten 'şedîdu'l-quvâ' / 'er-rahmân'", 'not': 'öğretti.'},
 {'bag': '54:17 · 54:22 · 54:32 · 54:40 → 55:2', 'kural': "okuma — 'yessernâ'l-qur'ân' / ''allema'l-qur'ân' (aday 1040, kayıt)", 'not': "Kur'ân."},
 {'bag': '16:4 · 21:37 · 32:7 → 55:3', 'kural': "tam kalıp 'halaqa'l-insân' 6 ayet (55:14, 96:2 henüz okunmadı)", 'not': 'insanı yarattı.'},
 {'bag': '55:2 · 55:3 · 55:4', 'kural': 'okuma — öğretti / yarattı / öğretti', 'not': 'dizi.'},
 {'bag': '13:2 · 39:5 → 55:5', 'kural': "tam kalıp 'eş-şems ve'l-qamer' 8 ayet — 'sahhara … li-ecelin musemmâ' / 'bi-husbân'", 'not': 'güneş ve ay.'},
 {'bag': '18:40 → 55:5', 'kural': "lemma 'husbân' 3 ayet — yıkım / hesap", 'not': 'hesap.'},
 {'bag': '54:1 → 55:5', 'kural': "okuma — 'el-qamer' sûre sınırının iki yanında (aday 1040, kayıt)", 'not': 'ay.'},
 {'bag': '22:18 · 16:49 → 55:6', 'kural': 'okuma — secde edenler listesi', 'not': 'secde.'},
 {'bag': '53:1 → 55:6', 'kural': "okuma — 've'n-necm' (aday 1040 alanı; ardışık değil, kayıt)", 'not': 'necm.'},
 {'bag': '13:2 → 55:7', 'kural': "okuma — 'rafe'a' + gök", 'not': 'yükseltti.'},
 {'bag': '42:17 · 21:47 → 55:7', 'kural': "lemma 'mîzân' 16 ayet", 'not': 'ölçü.'},
 {'bag': '20:81 → 55:8', 'kural': "okuma — 'lâ tatğav fî'", 'not': 'taşkınlık.'},
 {'bag': '18:105 → 55:9', 'kural': "lemma 'vezn' 3 ayet — 'nuqîmu … veznâ' / 'eqîmû'l-vezn'", 'not': 'tartı.'},
 {'bag': '11:85 · 17:35 · 26:182 → 55:9', 'kural': 'okuma — ölçü + adalet emri', 'not': 'adalet.'},
 {'bag': '55:7 · 55:10', 'kural': 'okuma — gök yükseltildi / yer konuldu (aday 1039, kayıt)', 'not': 'gök / yer.'},
 {'bag': '41:47 → 55:11', 'kural': "lemma 'ekmâm' 2 ayet", 'not': 'tomurcuk kabuğu.'},
 {'bag': '36:57 · 43:73 → 55:11', 'kural': "lemma 'fâkihe' 11 ayet — 'fîhâ fâkiha' cennette / yeryüzünde", 'not': 'meyve.'},
 {'bag': '54:20 → 55:11', 'kural': "okuma — 'nahl' sûre sınırının iki yanında (aday 1040, kayıt)", 'not': 'hurma.'},
 {'bag': '53:55 → 55:13', 'kural': "lemma 'âlâ'' 34 ayet — 'fe-bi-eyyi âlâ'i rabbike' 2MS / 'rabbikumâ' 2D (aday 1040 alanı, ardışık değil)", 'not': 'nimetler.'},
 {'bag': '55:13 · 55:16 · 55:18', 'kural': "tam kalıp 'fe-bi-eyyi âlâ'i rabbikumâ tukezzibân' 31 ayet, hepsi bu sûrede", 'not': 'nakarat.'},
 {'bag': '15:26 → 55:14', 'kural': "lemma 'salsâl' 4 ayet; xref ölçümde", 'not': 'balçık.'},
 {'bag': '15:27 → 55:15', 'kural': "lemma 'cânn' 7 ayet — insan / cânn sırası iki sûrede aynı", 'not': 'cânn.'},
 {'bag': '26:28 · 37:5 · 43:38 → 55:17', 'kural': "lemma 'meşriq' 11 ayet — tekil / çoğul / ikil", 'not': 'doğular.'},
 {'bag': '25:53 → 55:19 · 55:20', 'kural': "tam kalıp 'meraca'l-bahrayn' 2 ayet ve 'beynehumâ berzah' 2 ayet", 'not': 'iki deniz.'},
 {'bag': '27:61 → 55:19', 'kural': "okuma — iki deniz arası engel ('hâciz')", 'not': 'engel.'},
 {'bag': '54:12 → 55:19', 'kural': "lemma 'iltaqâ' 7 ayet — iki su buluşuyor (aday 1040, kayıt)", 'not': 'buluşma.'},
 {'bag': '23:100 → 55:20', 'kural': "lemma 'berzah' 3 ayet — ölüm-diriliş arası / iki deniz arası", 'not': 'berzah.'},
 {'bag': '35:12 → 55:22', 'kural': 'okuma — iki denizden çıkan süs / inci ve mercan', 'not': 'deniz ürünleri.'},
 {'bag': '52:24 → 55:22', 'kural': "lemma 'lu'lu'' 6 ayet — teşbih / denizden çıkan", 'not': 'inci.'},
 {'bag': '42:32 → 55:24', 'kural': "tam kalıp 'fi'l-bahri ke'l-a'lâm' 2 ayet — 'min âyâtihî' / 'lehû'", 'not': 'gemiler.'},
 {'bag': '28:88 → 55:26 · 55:27', 'kural': "okuma — 'kullu şey'in hâlikun illâ vechehû' bir ayette / iki ayette", 'not': 'yok oluş, kalış.'},
 {'bag': '53:51 → 55:27', 'kural': "lemma 'baqiye' 3 ayet — 'fe-mâ ebqâ' / 'yebqâ'", 'not': 'kalma.'},
 {'bag': '30:26 → 55:29', 'kural': "tam kalıp 'men fi's-semâvâti ve'l-ard' (harekesiz, 2 ayet) — 'lehû' / 'yes'eluhû'", 'not': 'gök ve yerdekiler.'},
 {'bag': '10:61 → 55:29', 'kural': "lemma 'şe'n' 4 ayet", 'not': 'iş.'},
 {'bag': '55:21 · 55:23 · 55:25 · 55:28 · 55:30', 'kural': 'nakarat geçişleri 4-8 / 31', 'not': 'nakarat.'},
 {'bag': '55:31 · 55:33 → nakarat', 'kural': "okuma — 2D muhatap metinde adlanıyor: 'es-seqalân', 'ma'şera'l-cinni ve'l-ins'", 'not': 'muhatap.'},
 {'bag': '17:88 → 55:33', 'kural': 'okuma — insan + cin için yeti sınırı (çıpa L2 emsali)', 'not': 'yeti sınırı.'},
 {'bag': '33:14 → 55:33', 'kural': "lemma 'aqtâr' 2 ayet — şehrin / göklerin ve yerin çevresi", 'not': 'çevreler.'},
 {'bag': '54:10 → 55:35', 'kural': "lemma 'intasara' 7 ayet — 'fe'ntasir' / 'fe-lâ tentasirân' (aday 1040, kayıt)", 'not': 'kurtulma.'},
 {'bag': '54:1 · 19:90 → 55:37', 'kural': "lemma 'inşaqqa' 5 ayet — ay / yer / gök", 'not': 'yarılma.'},
 {'bag': '21:23 · 28:78 → 55:39', 'kural': "tam kalıp 'lâ yus'elu' 2 ayet; 28:78 'an zunûbihim'", 'not': 'sorulmaz.'},
 {'bag': '55:29 · 55:39', 'kural': "okuma — سأل 'yes'eluhû' / 'lâ yus'elu'", 'not': 'isteme / sorulma.'},
 {'bag': '55:37 → 55:39', 'kural': "okuma — 'izâ' şartı ve cevabı arasında nakarat (55:38)", 'not': 'şart-cevap.'},
 {'bag': '47:30 → 55:41', 'kural': "lemma 'sîmâ' 6 ayet — 'fe-le-araftehum' / 'yu'rafu'", 'not': 'belirti.'},
 {'bag': '11:56 → 55:41', 'kural': "okuma — 'ehaze' + 'nâsiye' / 'yu'hazu bi'n-nevâsî'", 'not': 'perçem.'},
 {'bag': '36:63 · 52:14 → 55:43', 'kural': "tam kalıp 'hâzihî cehennem' 2 ayet; 52:14 'hâzihi'n-nâru'lletî … tukezzibûn'", 'not': 'işte bu.'},
 {'bag': '52:24 → 55:44', 'kural': "lemma 'tâfe' 8 ayet — cennette / cehennemde dolaşma", 'not': 'dolaşma.'},
 {'bag': '14:14 → 55:46', 'kural': "okuma — 'li-men hâfe maqâmî' / 'li-men hâfe maqâme rabbihî' (79:40 henüz okunmadı)", 'not': 'makamdan korkan.'},
 {'bag': '34:15 · 18:32 → 55:46', 'kural': 'okuma — dünyada iki bahçe / âhirette iki cennet', 'not': 'iki cennet.'},
 {'bag': '34:16 → 55:48', 'kural': "okuma — 'zevâtey ukul' / 'zevâtâ efnân'", 'not': 'ikil.'},
 {'bag': '54:12 → 55:50', 'kural': "okuma — 'uyûn' yerde / 'aynân' cennette (aday 1040, kayıt)", 'not': 'pınar.'},
 {'bag': '13:3 · 51:49 → 55:52', 'kural': "okuma — 'min kull … zevceyn' yeryüzü / her şey / cennet", 'not': 'çiftler.'},
 {'bag': '18:31 · 44:53 → 55:54', 'kural': "lemma 'istebraq' 4 ayet — giysi / döşek astarı", 'not': 'ipek.'},
 {'bag': '18:31 · 38:51 → 55:54', 'kural': "lemma 'muttaki'' 8 ayet", 'not': 'yaslanma.'},
 {'bag': '37:48 · 38:52 → 55:56', 'kural': "tam kalıp 'qâsirâtu't-tarf' 3 ayet", 'not': 'bakışlarını sınırlı tutanlar.'},
 {'bag': '37:49 → 55:58', 'kural': "tam kalıp 'ke-ennehunne' 2 ayet — 37:48-49 dizisi 55:56, 58'de", 'not': 'teşbih.'},
 {'bag': '55:22 · 55:58', 'kural': "lemma 'mercân' 2 ayet, ikisi bu sûrede — denizden / teşbih", 'not': 'mercan.'},
 {'bag': '34:33 → 55:60', 'kural': "okuma — 'hel yuczevne illâ' / 'hel cezâ'u … illâ'", 'not': 'karşılık.'},
 {'bag': '55:46 · 55:62', 'kural': "okuma — iki çift cennet; ikinci dizi 'min dûnihimâ' ile başlıyor", 'not': 'paralel dizi.'},
 {'bag': '55:48 · 55:64', 'kural': 'okuma — paralel dizide dal / renk', 'not': 'paralel.'},
 {'bag': '55:50 · 55:66', 'kural': "tam kalıp 'fîhimâ aynân' 2 ayet, ikisi bu sûrede — akan / fışkıran", 'not': 'pınarlar.'},
 {'bag': '55:11 · 55:68', 'kural': "okuma — 'fî- fâkihetun ve nahl' yeryüzü / cennet", 'not': 'meyve, hurma.'},
 {'bag': '55:56 · 55:70', 'kural': "okuma — 'fîhinne' + kadınların niteliği", 'not': 'paralel.'},
 {'bag': '55:1 · 55:64', 'kural': 'okuma — sûrenin iki tek kelimelik ayeti', 'not': 'tek kelime.'},
 {'bag': '55:56 · 55:72', 'kural': "okuma — kök قصر: 'qâsirât' etken / 'maqsûrât' edilgen", 'not': 'karşıt çift.'},
 {'bag': '55:56 · 55:74', 'kural': "tam kalıp 'lem yatmishunne insun qablehum ve lâ cânn' 2 ayet, ikisi bu sûrede", 'not': 'tekrar.'},
 {'bag': '55:54 · 55:76', 'kural': "tam kalıp 'muttaki'îne alâ' — iki dizinin yaslanma ayetleri; sıra ters", 'not': 'paralel.'},
 {'bag': '55:70 · 55:76', 'kural': "okuma — 'hisân' fâsıla; kadınlar / halılar", 'not': 'aynı sıfat.'},
 {'bag': '55:64 · 55:76', 'kural': 'okuma — ikinci dizide iki yeşil (دهم / خضر)', 'not': 'renk.'},
 {'bag': '55:27 · 55:78', 'kural': "okuma — 'rabbike zu/zi'l-celâli ve'l-ikrâm'; sûrede 2MS hitabın iki ayeti; NOM / GEN", 'not': 'kapanış.'},
 {'bag': '55:1 · 55:78', 'kural': "okuma — sûre 'er-rahmân' ile açılıp 'ismu rabbik' ile kapanıyor", 'not': 'baş / son.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_rahman', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in RAHMAN]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_rahman'] = RAHMAN
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_rahman', len(RAHMAN), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_rahman', len(BAGLAR['AS_rahman']))
