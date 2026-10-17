# -*- coding: utf-8 -*-
"""aday_ekle_50_qaf.py — sûre 50 (Qâf) adayları (AX_qaf) ve okuma bağları (AS_qaf).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

QAF = [
]

BAGLAR = {"AS_qaf": [
 {'bag': '49:18 → 50:1', 'kural': "okuma — ardışık sûre sınırı; fâsıla ن → د; 'basîrun bimâ ta'melûn' → harf + yemin (QASEM); aday 1040 alanında kayıt, test yok", 'not': 'sûre sınırı.'},
 {'bag': '38:1 → 50:1', 'kural': "okuma — tek harf + 've'l-Qur'ân' + sıfat ('zi'z-zikr' / 'el-mecîd'); aynı açılış kalıbı", 'not': 'yeminli açılış.'},
 {'bag': '11:73 → 50:1', 'kural': "'mecîd' lemma 4 ayet; okundu — Allah için / Kur'ân için; aday 1041 alanında kayıt", 'not': 'mecîd.'},
 {'bag': '38:4 → 50:2', 'kural': "xref (ölçüm); okundu — 'acibû en câ'ehum munzirun minhum … qâle'l-kâfirûn' aynı dizi, bağlaç farkı", 'not': 'şaşma.'},
 {'bag': '11:72 → 50:2', 'kural': "lemma dizisi 'şey'un acîb' 2 ayet; okundu", 'not': 'tuhaf şey.'},
 {'bag': '23:35 · 23:82 · 37:16 · 37:53 → 50:3', 'kural': "lemma dizisi 'e-izâ mitnâ ve kunnâ turâben' 6 ayet (56:47 henüz okunmadı); okundu — orada 'izâmen' + dönüş sözü, burada 'rec'un ba'îd'", 'not': 'ölüm ve toprak.'},
 {'bag': '50:3 → 50:4', 'kural': "okuma — toprak olma sorusu / 'mâ tenqusu'l-ardu minhum'; karşıt çift (aday 1039, okuma) 50:4 içinde 'tenqusu' / 'hafîz'", 'not': 'soru ve cevap.'},
 {'bag': '13:41 · 21:44 · 35:11 → 50:4', 'kural': "'neqase' lemma 7 ayet; okundu — 'nenqusuhâ min etrâfihâ' (fâil 1P) / 'tenqusu'l-ard' (fâil yer); KAPATILAMAZ", 'not': 'eksiltme.'},
 {'bag': '42:6 · 34:21 → 50:4', 'kural': "'hafîz' lemma 12 ayet; okundu — Allah / Rab için / kitap için; aday 1041 alanında kayıt", 'not': 'hafîz.'},
 {'bag': '29:68 → 50:5', 'kural': "lemma dizisi 'kezzebe bi'l-haqqi lemmâ câ'e' 3 ayet; xref (ölçüm); okundu (6:5 henüz okunmadı)", 'not': 'hakkı yalanlama.'},
 {'bag': '37:6 · 41:12 · 15:16 → 50:6', 'kural': "'zeyyene' lemma 26 ayet; okundu — göğün süslenmesi", 'not': 'gök süsü.'},
 {'bag': '15:19 → 50:7', 'kural': "esit2 BENZER 0,8817 (ölçüm); lemma dizisi 2 ayet; okundu — son kelime 'şey'in mevzûn' / 'zevcin behîc'", 'not': 'yer, dağ, bitki.'},
 {'bag': '22:5 → 50:7', 'kural': "lemma dizisi 'kulli zevcin behîc' 2 ayet; xref (ölçüm); okundu", 'not': 'göz alıcı çift.'},
 {'bag': '13:3 · 16:15 · 21:31 · 27:61 · 31:10 · 41:10 → 50:7', 'kural': "'revâsî' lemma 10 ayet; okundu", 'not': 'sabit dağlar.'},
 {'bag': '50:6 → 50:7', 'kural': "okuma — gök (bina, süs, yarıksız) / yer (uzatma, dağ, bitki); ayetler arası", 'not': 'gök ve yer.'},
 {'bag': '34:9 → 50:8', 'kural': "lemma dizisi 'kulli abdin munîb' 2 ayet; xref (ölçüm); okundu", 'not': 'yönelen kul.'},
 {'bag': '27:60 · 23:18 · 43:11 · 15:22 · 39:21 → 50:9', 'kural': "okuma — gökten su indirme kalıbı; 27:60 'fe-enbetnâ bihî' aynı bağ", 'not': 'su ve bitki.'},
 {'bag': '21:50 · 23:29 · 38:29 → 50:9', 'kural': "'mubârak' lemma 8 ayet; okundu — Kur'ân, iniş yeri, kitap / su", 'not': 'bereketli.'},
 {'bag': '10:24 · 11:100 · 21:15 · 36:33 → 50:9', 'kural': "'hasîd' lemma 4 ayet, 'habb' lemma 7 ayet; okundu — helâk benzetmesi / ekin adı", 'not': 'biçilen.'},
 {'bag': '26:148 · 37:65 → 50:10', 'kural': "'tal'' lemma 4 ayet; okundu", 'not': 'tomurcuk.'},
 {'bag': '42:27 → 50:11', 'kural': "lemma dizisi 'rizq + ibâd' 2 ayet; okundu", 'not': 'kullara rızık.'},
 {'bag': '25:49 · 43:11 → 50:11', 'kural': "lemma dizisi 'ahyâ + belde + meyt' 2 ayet (xref 25:49, ölçüm); okundu — 43:11 su → ölü belde → 'kezâlike tuhracûn' aynı sıra", 'not': 'ölü belde.'},
 {'bag': '50:11 → 50:42', 'kural': "'hurûc' lemma 5 ayet; sûre içi — 'kezâlike'l-hurûc' / 'yevmu'l-hurûc' (50:42 metin görüldü, ileride)", 'not': 'çıkış.'},
 {'bag': '22:42 · 38:12 → 50:12', 'kural': "lemma dizisi 'kezzebet qablehum qavmu Nûh' 5 ayet (40:5 bu oturumda görülmedi, 54:9 henüz okunmadı); okundu", 'not': 'yalanlayan kavimler.'},
 {'bag': '22:42 · 22:43 · 38:12 · 38:13 → 50:12 · 50:13 · 50:14', 'kural': "okuma — kavim sayımı: 5 / 6 / 8 ad; 'qavmu Lût' / 'ihvânu Lût'", 'not': 'sayım.'},
 {'bag': '25:38 → 50:12', 'kural': "'Ress' lemma 2 ayet; okundu", 'not': 'Ress.'},
 {'bag': '15:78 · 26:176 · 38:13 → 50:14', 'kural': "'Eyke' lemma 4 ayet; okundu", 'not': 'Eyke.'},
 {'bag': '44:37 → 50:14', 'kural': "'Tubba'' lemma 2 ayet; okundu", 'not': "Tubba'."},
 {'bag': '38:14 → 50:14', 'kural': "lemma dizisi 'kezzebe rasûl haqqa' 2 ayet; xref (ölçüm); okundu — 'ıqâb' / 'vaîd'", 'not': 'hak olan tehdit.'},
 {'bag': '14:14 · 20:113 → 50:14 · 50:20', 'kural': "'vaîd' lemma 6 ayet, sûre içi 4 (50:14, 20, 28, 45); okundu", 'not': 'tehdit.'},
 {'bag': '46:33 → 50:15', 'kural': "''ayiye' lemma 2 ayet; okundu — yaratmakla yorulmama / 'e-fe-ayînâ'; aday 1041 alanında kayıt", 'not': 'âciz kalma.'},
 {'bag': '13:5 → 50:3 · 50:15', 'kural': "okuma — 'kunnâ turâben' + 'halqin cedîd' 13:5'te tek ayette, 50'de iki ayete dağılmış", 'not': 'yeni yaratılış.'},
 {'bag': '50:15 → 50:15', 'kural': "karşıt çift (aday 1039, okuma) — 'el-halqi'l-evvel' / 'halqin cedîd'", 'not': 'ilk / yeni.'},
 {'bag': '15:26 · 23:12 → 50:16', 'kural': "lemma dizisi 'le-qad halaqna'l-insân' 5 ayet (90:4, 95:4 henüz okunmadı); okundu — madde / bilgi", 'not': 'insanın yaratılışı.'},
 {'bag': '24:15 · 21:103 → 50:17', 'kural': "'telaqqâ' lemma 4 ayet; 'iz telaqqâ' 2 ayet; okundu", 'not': 'alma.'},
 {'bag': '4:1 · 5:117 · 33:52 · 11:93 → 50:18', 'kural': "'raqîb' lemma 5 ayet; okundu — Allah (3) / Şuayb (1) / adsız (50:18); aday 1041 alanında kayıt", 'not': 'gözetleyici.'},
 {'bag': '15:72 → 50:19', 'kural': "'sekra' lemma 2 ayet; okundu", 'not': 'sarhoşluk.'},
 {'bag': '50:5 → 50:19', 'kural': "okuma — 'kezzebû bi'l-haqqi lemmâ câ'ehum' / 'câ'et sekratu'l-mevti bi'l-haqq'", 'not': 'hak ile gelen.'},
 {'bag': '18:99 · 20:102 · 23:101 · 27:87 · 36:51 · 39:68 → 50:20', 'kural': "lemma dizisi 'nefaha fi's-sûr' 10 ayet (6:73, 69:13, 78:18 henüz okunmadı); okundu", 'not': 'sûr.'},
 {'bag': '50:19 → 50:21', 'kural': "okuma — 'câ'et sekratu'l-mevt' / 'câ'et kullu nefs'; جيأ sûre içi", 'not': 'geliş.'},
 {'bag': '21:97 → 50:22', 'kural': "lemma dizisi 'kâne fî ğafle' 2 ayet; okundu — 1P itiraf / 2MS hitap", 'not': 'gaflet.'},
 {'bag': '18:101 → 50:22', 'kural': "'ğıtâ'' lemma 2 ayet; okundu — gözler perdede / perde kaldırıldı; karşıt çift (aday 1039, okuma)", 'not': 'perde.'},
 {'bag': '17:50 · 18:96 · 34:10 → 50:22', 'kural': "'hadîd' lemma 6 ayet; okundu — demir / keskin göz; gloss 1021", 'not': 'hadîd.'},
 {'bag': '43:36 · 43:38 · 37:51 · 41:25 → 50:23 · 50:27', 'kural': "'qarîn' lemma 7 ayet; okundu — 43:36 şeytan; burada adsız (1017)", 'not': 'yakın.'},
 {'bag': '50:23 → 50:27', 'kural': "lemma dizisi 'qâle qarîn' 2 ayet, sûre içi — teslim / savunma (okuma)", 'not': 'iki söz.'},
 {'bag': '50:18 → 50:23', 'kural': "'atîd' lemma 2 ayet, sûre içi — 'raqîbun atîd' / 'mâ ledeyye atîd'", 'not': 'hazır.'},
 {'bag': '17:39 → 50:24 · 50:26', 'kural': "lemma dizileri 'elqâ fî cehennem' 2 ayet ve 'ce'ale ma'a'llâhi ilâhen âhar' 5 ayet; xref (ölçüm); okundu — 17:39'da tek ayet, burada iki ayete ayrık", 'not': 'başka ilah, atılma.'},
 {'bag': '15:96 · 17:22 → 50:26', 'kural': "lemma dizisi 'ce'ale ma'a'llâhi ilâhen âhar' 5 ayet (51:51 henüz okunmadı); okundu", 'not': 'başka ilah.'},
 {'bag': '14:34 · 39:3 · 11:59 · 14:15 → 50:24', 'kural': "'keffâr' lemma 5 ayet, 'anîd' lemma 4 ayet; okundu — 'kullu X anîd' kalıbı", 'not': 'inatçı.'},
 {'bag': '11:62 · 14:9 · 34:54 → 50:25', 'kural': "'murîb' lemma 7 ayet; okundu — şekkin sıfatı / kişinin sıfatı", 'not': 'kuşkulu.'},
 {'bag': '26:96 · 39:31 → 50:28', 'kural': "'ihtesame' lemma 8 ayet; okundu — 'inde rabbikum' / 'ledeyye'", 'not': 'çekişme.'},
 {'bag': '22:10 · 41:46 → 50:29', 'kural': "'zallâm' lemma 5 ayet (3:182, 8:51 henüz okunmadı); okundu — 3. şahıs Allah / Rab / 1S adsız; aday 1041 alanında kayıt", 'not': 'zulmetmeyen.'},
 {'bag': '50:14 · 50:20 → 50:28', 'kural': "'vaîd' sûre içi üçüncü (okuma)", 'not': 'tehdit.'},
 {'bag': '50:30 → 50:35', 'kural': "'mezîd' lemma 2 ayet, sûre içi (50:35 henüz okunmadı)", 'not': 'fazlası.'},
 {'bag': '26:90 → 50:31', 'kural': "lemma dizisi 'uzlifeti'l-cennetu li'l-muttaqîn' 2 ayet; xref (ölçüm); okundu — aynı cümle + 'ğayra ba'îd'", 'not': 'yaklaştırılan cennet.'},
 {'bag': '27:22 → 50:31', 'kural': "lemma dizisi 'ğayra ba'îd' 2 ayet; okundu — zaman / mekân", 'not': 'uzak değil.'},
 {'bag': '50:24 · 50:26 → 50:31', 'kural': "okuma — cehenneme atma / cennetin yaklaştırılması; karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'iki sahne.'},
 {'bag': '17:25 · 38:17 · 38:30 · 38:44 → 50:32', 'kural': "'evvâb' lemma 6 ayet; okundu — Dâvûd, Süleymân, Eyyûb / sınıf", 'not': 'dönen.'},
 {'bag': '50:4 → 50:32', 'kural': "'hafîz' sûre içi — kitap / kul; aday 1041 alanında kayıt", 'not': 'koruyan.'},
 {'bag': '50:28 → 50:32', 'kural': "okuma — 'vaîd' / 'tû'adûn' (وعد); karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'tehdit / vaat.'},
 {'bag': '36:11 → 50:33', 'kural': "lemma dizisi 'haşiye'r-Rahmâne bi'l-ğayb' 2 ayet; xref (ölçüm); okundu", 'not': 'görmeden korkan.'},
 {'bag': '50:8 → 50:33', 'kural': "'munîb' sûre içi — 'abdin munîb' / 'qalbin munîb'", 'not': 'yönelen.'},
 {'bag': '15:46 → 50:34', 'kural': "lemma dizisi 'udhulûhâ bi-selâm' 2 ayet; okundu", 'not': 'esenlikle girme.'},
 {'bag': '50:20 → 50:34', 'kural': "okuma — 'zâlike yevmu'l-vaîd' / 'zâlike yevmu'l-hulûd'; karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'iki gün.'},
 {'bag': '50:30 → 50:35', 'kural': "'mezîd' lemma 2 ayet, sûre içi tamam — cehennem / 'ledeynâ'", 'not': 'fazlası.'},
 {'bag': '19:74 · 19:98 · 20:128 · 36:31 → 50:36', 'kural': "lemma dizisi 'kem ehleknâ qablehum min qarn' 5 ayet; okundu", 'not': 'helâk edilen nesiller.'},
 {'bag': '43:8 · 28:78 → 50:36', 'kural': "okuma — 'eşeddu minhum batşâ' / 'eşeddu minhu quvveten'; xref 28:78 (ölçüm)", 'not': 'daha güçlü.'},
 {'bag': '14:21 · 41:48 · 42:35 → 50:36', 'kural': "'mahîs' lemma 5 ayet (4:121 henüz okunmadı); okundu — olumsuz / soru", 'not': 'kaçış yeri.'},
 {'bag': '39:21 → 50:37', 'kural': "lemma dizisi 'inne fî zâlike le-zikrâ' 2 ayet; okundu", 'not': 'hatırlatma.'},
 {'bag': '50:8 → 50:37', 'kural': "okuma — 'tebsiraten ve zikrâ' / 'le-zikrâ'; sûre içi çerçeve", 'not': 'zikrâ.'},
 {'bag': '25:59 · 32:4 → 50:38', 'kural': "xref (ölçüm); okundu — 'halaqa … fî sitteti eyyâmin summe'stevâ' (3MS) / 'halaqnâ … ve mâ messenâ min luğûb' (1P)", 'not': 'altı gün.'},
 {'bag': '35:35 → 50:38', 'kural': "'luğûb' lemma 2 ayet; okundu — cennet ehli / yaratıcı; aday 1041 alanında kayıt", 'not': 'yorgunluk.'},
 {'bag': '50:15 → 50:38', 'kural': "okuma — 'e-fe-ayînâ bi'l-halqi'l-evvel' / 'mâ messenâ min luğûb'", 'not': 'yorulmama.'},
 {'bag': '20:130 → 50:39 · 50:40', 'kural': "xref (ölçüm); lemma dizileri 'fa'sbir alâ mâ yeqûlûn' 4 ayet, 'qable tulû'i'ş-şems … ğurûb' 2 ayet; okundu — aynı sıra, 'ğurûbihâ' / 'el-ğurûb'", 'not': 'sabır ve tesbih.'},
 {'bag': '38:17 · 15:98 → 50:39', 'kural': "lemma dizileri 'fa'sbir alâ mâ yeqûlûn' ve 'sebbih bi-hamdi rabbik' (10 ayet); okundu", 'not': 'tesbih.'},
 {'bag': '34:51 → 50:41', 'kural': "lemma dizisi 'min mekânin qarîb' 2 ayet; okundu — yakalanma / çağrı", 'not': 'yakın yer.'},
 {'bag': '50:16 → 50:41', 'kural': "'qarîb / aqrab' sûre içi (قرب)", 'not': 'yakınlık.'},
 {'bag': '36:49 · 36:53 → 50:42', 'kural': "'sayha' lemma 13 ayet; okundu — 'vâhide' / 'bi'l-haqq'", 'not': 'çığlık.'},
 {'bag': '50:11 → 50:42', 'kural': "'hurûc' sûre içi tamam — 'kezâlike'l-hurûc' / 'yevmu'l-hurûc'", 'not': 'çıkış.'},
 {'bag': '50:20 · 50:34 → 50:42', 'kural': "okuma — 'zâlike yevmu'l-vaîd / hulûd / hurûc' üç gün adı", 'not': 'günler.'},
 {'bag': '15:23 → 50:43', 'kural': "lemma dizisi 'innâ nahnu nuhyî ve numît' 2 ayet; okundu — 'vârisûn' / 'masîr'", 'not': 'diriltme, öldürme.'},
 {'bag': '22:48 → 50:43', 'kural': "lemma dizisi 'ilâ + masîr' 9 ayet; okundu — 1S / 1P", 'not': 'dönüş.'},
 {'bag': '50:11 → 50:43', 'kural': "okuma — 'ahyeynâ … meytâ' / 'nuhyî ve numît'; karşıt çift (aday 1039, okuma)", 'not': 'hayat, ölüm.'},
 {'bag': '25:25 → 50:44', 'kural': "'teşeqqaqa' lemma 3 ayet (2:74 henüz okunmadı); okundu — gök / yer", 'not': 'yarılma.'},
 {'bag': '50:4 → 50:44', 'kural': "okuma — 'tenqusu'l-ardu minhum' / 'teşeqqaqu'l-ardu anhum'", 'not': 'yer.'},
 {'bag': '50:3 → 50:44', 'kural': "okuma — 'zâlike rec'un ba'îd' / 'zâlike haşrun aleynâ yesîr'; karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'uzak / kolay.'},
 {'bag': '20:104 → 50:45', 'kural': "lemma dizisi 'nahnu a'lemu bimâ yeqûlûn' 2 ayet; okundu", 'not': 'daha iyi bilen.'},
 {'bag': '11:59 · 14:15 · 19:32 · 26:130 · 40:35 → 50:45', 'kural': "'cebbâr' lemma 10 ayet; okundu — insan için / muhatap için olumsuz; aday 1041 alanında kayıt", 'not': 'zorba.'},
 {'bag': '50:1 → 50:45', 'kural': "okuma — sûre Kur'ân yemini ile açılıp Kur'ân ile hatırlatma ile kapanıyor (قرأ 2/2)", 'not': 'çerçeve.'},
 {'bag': '50:14 · 50:20 · 50:28 → 50:45', 'kural': "'vaîd' sûre içi dört (6 ayetin 4'ü sûre 50'de; ölçüm)", 'not': 'tehdit.'},
 {'bag': '50:45 → 51:1', 'kural': "sûre sınırı — 51:1 henüz okunmadı; aday 1040 alanı sonraki turda", 'not': 'sınır.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_qaf', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in QAF]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_qaf'] = QAF
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_qaf', len(QAF), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_qaf', len(BAGLAR['AS_qaf']))
