# -*- coding: utf-8 -*-
"""aday_ekle_58_mucadele.py — sûre 58 (Mücâdele) adayları (AX_mucadele) ve okuma bağları (AS_mucadele).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

MUCADELE = [
]

BAGLAR = {"AS_mucadele": [
 {'bag': '57:29 → 58:1', 'kural': "okuma — ardışık sûre sınırı; lafızla kapanış / lafız 3. kelimede açılış; 'ya'lem' / 'semi'a'; fâsıla م → ر (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '3:181 → 58:1', 'kural': "ölçüm xref — 'qad semi'a'llâhu qavl' kalıbı (2 ayet); 3:181 henüz okunmadı", 'not': 'kalıp eşi.'},
 {'bag': '12:86 → 58:1', 'kural': "okuma — şikâyet Allah'a ('ila'llâh'), kök شكو", 'not': 'ortak yön.'},
 {'bag': '24:35 → 58:1', 'kural': "okuma — kök شكو ikinci anlam (kandil yuvası); kök tablosu ayrı yazıyor", 'not': 'anlam ayrımı.'},
 {'bag': '22:75 → 58:1', 'kural': "kalıp — 'inne'llâhe semî'un basîr' (3 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '31:28 → 58:1', 'kural': "kalıp — 'inne'llâhe semî'un basîr' (3 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '11:24 → 58:1', 'kural': "okuma — lemma 'semî'' ve 'basîr' insan benzetmesinde / lafzın haberi (aday 1041, kayıt)", 'not': 'aynı kelime iki gönderge.'},
 {'bag': '33:4 → 58:2', 'kural': "okuma — zıhâr; 'mâ ce'ale … ummehâtikum' / 'mâ hunne ummehâtihim' + hasr; 'qavlukum' / 'munkeran mine'l-qavl'", 'not': 'aynı hüküm.'},
 {'bag': '33:26 → 58:2', 'kural': "okuma — lemma 'zâhara' arka çıkma anlamında (1021 gloss)", 'not': 'anlam ayrımı.'},
 {'bag': '33:6 → 58:2', 'kural': "okuma — nebînin eşleri 'ummehât' / zıhârla 'anne' denen eş anne değil (aday 1039 okuma)", 'not': 'karşıt kullanım.'},
 {'bag': '22:30 → 58:2', 'kural': "okuma — 'qavl' + 'zûr' birlikte", 'not': 'ortak söz.'},
 {'bag': '25:4 → 58:2', 'kural': "okuma — lemma 'zûr' ('zulmen ve zûrâ')", 'not': 'lemma eşi.'},
 {'bag': '22:60 → 58:2', 'kural': "kalıp + ölçüm xref — 'allâhe le-afuvvun ğafûr' (2 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '57:10 → 58:3', 'kural': "kalıp — 've'llâhu bimâ ta'melûne habîr' (7 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '4:92 → 58:3', 'kural': "kalıp + ölçüm xref — 'fe-tahrîru raqabe', 'fe-siyâmu şehreyni mutetâbi'ayn'; 4:92 henüz okunmadı", 'not': 'kalıp eşi.'},
 {'bag': '48:9 → 58:4', 'kural': "kalıp — 'li-tu'minû bi'llâhi ve rasûlih' (2 ayet); gönderilişin / hükmün amacı", 'not': 'ortak amaç cümlesi.'},
 {'bag': '58:4 → 58:5', 'kural': "okuma — kök حدد ardışık: 'hudûdu'llâh' (sınırlar) / 'yuhâddûna'llâh' (karşı durma); 'azâbun elîm' / 'azâbun muhîn'", 'not': 'ardışık kök.'},
 {'bag': '57:25 → 58:5', 'kural': "okuma — kök حدد ('el-hadîd'); kök tablosu 'demir; sınır koyma'", 'not': 'kök eşi.'},
 {'bag': '24:64 → 58:6', 'kural': "kalıp — 'fe-yunebbi'uhum bimâ amilû' (2 ayet)", 'not': 'ortak haber verme.'},
 {'bag': '18:49 → 58:6', 'kural': "okuma — lemma 'ahsâ': kitap sayıyor / Allah sayıyor", 'not': 'lemma eşi.'},
 {'bag': '36:12 → 58:6', 'kural': "okuma — lemma 'ahsâ': 1P 'kulle şey'in ahsaynâh' / lafız", 'not': 'lemma eşi.'},
 {'bag': '9:67 → 58:6', 'kural': "okuma — lemma 'nesiye' insan ve Allah için / yalnız insan; karşıt 'ahsâ' (aday 1041, 1039 kayıt)", 'not': 'aynı fiil iki gönderge.'},
 {'bag': '22:17 → 58:6', 'kural': "kalıp — 'alâ kulli şey'in şehîd' (6 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '24:6 → 58:6', 'kural': "okuma — lemma 'şehîd' insan tanıklar / lafzın haberi (aday 1041, kayıt)", 'not': 'aynı kelime iki gönderge.'},
 {'bag': '49:16 → 58:7', 'kural': "kalıp — 'ya'lemu mâ fi's-semâvâti ve mâ fi'l-ard' (3 ayet)", 'not': 'ortak kalıp.'},
 {'bag': '9:78 → 58:7', 'kural': "okuma — lemma 'necvâ': Allah gizli konuşmayı bilir", 'not': 'lemma eşi.'},
 {'bag': '43:80 → 58:7', 'kural': "okuma — lemma 'necvâ': işitme + yazan elçiler", 'not': 'lemma eşi.'},
 {'bag': '18:22 → 58:7', 'kural': "okuma — 'râbi'uhum', 'sâdisuhum' yalnız iki ayette: köpek / 'huve' (aday 1041, kayıt)", 'not': 'aynı sayı kalıbı iki gönderge.'},
 {'bag': '57:4 → 58:7', 'kural': "okuma — 'huve me'akum eyne mâ kuntum' / 'huve me'ahum eyne mâ kânû'", 'not': 'aynı beraberlik çerçevesi.'},
 {'bag': '22:17 → 58:7', 'kural': "ölçüm xref — 'yevme'l-qiyâme' + 'kulli şey''", 'not': 'xref.'},
 {'bag': '9:115 → 58:7', 'kural': "kalıp — 'inne'llâhe bi-kulli şey'in alîm' (4 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '29:62 → 58:7', 'kural': "kalıp — 'inne'llâhe bi-kulli şey'in alîm' (4 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '51:28 → 58:7', 'kural': "okuma — lemma 'alîm' insan için / lafzın haberi (aday 1041, kayıt)", 'not': 'aynı kelime iki gönderge.'},
 {'bag': '14:28 → 58:8', 'kural': "kalıp — 'e lem tera ile'llezîne' (12 ayet)", 'not': 'ortak açılış.'},
 {'bag': '40:69 → 58:8', 'kural': "kalıp — 'e lem tera ile'llezîne' (12 ayet)", 'not': 'ortak açılış.'},
 {'bag': '58:7 → 58:8', 'kural': "okuma — ardışık 'e lem tera' açılışları: Allah'ın bilgisi / fısıldaşanlar; 'necvâ' sürüyor", 'not': 'sûre içi akış.'},
 {'bag': '58:3 → 58:8', 'kural': "kalıp — 'ya'ûdûne limâ' (2 ayet): kendi sözüne / yasaklanana dönüş", 'not': 'sûre içi eş.'},
 {'bag': '24:61 → 58:8', 'kural': "okuma — 'tahiyyeten min indi'llâh' / Allah'ın selamlamadığı selam", 'not': 'karşıt kullanım.'},
 {'bag': '57:15 → 58:8', 'kural': "okuma — lemma 'masîr' ('bi'se'l-masîr')", 'not': 'lemma eşi.'},
 {'bag': '22:72 → 58:8', 'kural': "okuma — lemma 'masîr' ('bi'se'l-masîr')", 'not': 'lemma eşi.'},
 {'bag': '58:8 → 58:9', 'kural': "okuma + nakarat3 — 'bi'l-ismi ve'l-udvâni ve ma'siyeti'r-rasûl' 3MP / 2MP yasak; karşıtı 'birr, taqvâ' (aday 1039 kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '58:6 → 58:9', 'kural': "okuma — 'yeb'asuhumu'llâhu cemî'an' / 'ileyhi tuhşerûn'", 'not': 'sûre içi akış.'},
 {'bag': '14:11 → 58:10', 'kural': "kalıp — 'bi-izni'llâhi ve ale'llâh' (2 ayet) + 've ale'llâhi fe-l-yetevekkeli'l-mu'minûn' (7 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '9:51 → 58:10', 'kural': "kalıp — 've ale'llâhi fe-l-yetevekkeli'l-mu'minûn' (7 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '9:38 → 58:11', 'kural': "kalıp — 'izâ qîle lekum' (2 ayet): 'çıkın' denince ağırlaşma / 'yer açın' emri", 'not': 'ortak kalıp.'},
 {'bag': '24:28 → 58:11', 'kural': "okuma — 'qîle … + aynı fiilin emri' yapısı ('ırci'û fe'rci'û' / 'unşuzû fe'nşuzû')", 'not': 'ortak yapı.'},
 {'bag': '12:76 → 58:11', 'kural': "okuma — 'rafa'a' + 'derece' aynı ayette (1P / lafız)", 'not': 'lemma eşi.'},
 {'bag': '43:32 → 58:11', 'kural': "okuma — 'rafa'a' + 'derece' aynı ayette (1P / lafız)", 'not': 'lemma eşi.'},
 {'bag': '17:107 → 58:11', 'kural': "kalıp + ölçüm xref — 'ûtu'l-ilm' (9 ayet)", 'not': 'ortak kalıp.'},
 {'bag': '58:3 → 58:11', 'kural': "kalıp + nakarat3 — 've'llâhu bimâ ta'melûne habîr' (7 ayet)", 'not': 'sûre içi eş.'},
 {'bag': '49:1 → 58:12', 'kural': "okuma + ölçüm xref — 'qaddime beyne yedey': yasak / emir (aday 1039 kayıt)", 'not': 'karşıt kullanım.'},
 {'bag': '11:78 → 58:12', 'kural': "okuma — lemma 'athar'", 'not': 'lemma eşi.'},
 {'bag': '33:53 → 58:12', 'kural': "okuma — lemma 'athar' ('zâlikum atharu li-qulûbikum')", 'not': 'lemma eşi.'},
 {'bag': '24:28 → 58:12', 'kural': "kalıp — 'fe-in lem tecidû' (2 ayet)", 'not': 'ortak kalıp.'},
 {'bag': '58:4 → 58:12', 'kural': "okuma — 'lem yecid' / 'lem tecidû' muafiyetleri", 'not': 'sûre içi eş.'},
 {'bag': '16:115 → 58:12', 'kural': "kalıp — 'fe-inna'llâhe ğafûrun rahîm' (8 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '24:5 → 58:12', 'kural': "kalıp — 'fe-inna'llâhe ğafûrun rahîm' (8 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '58:12 → 58:13', 'kural': "nakarat3 — 'qaddime beyne yedey necvâkum sadaqa'; emir / yapılmayış", 'not': 'sûre içi eş.'},
 {'bag': '33:72 → 58:13', 'kural': "okuma — lemma 'eşfaqa' (2 ayet): gökler-yer-dağlar / inananlar", 'not': 'lemma eşi.'},
 {'bag': '24:5 → 58:13', 'kural': "okuma — lemma 'tâbe' insanlar / Allah (aday 1041, kayıt)", 'not': 'aynı fiil iki gönderge.'},
 {'bag': '22:78 → 58:13', 'kural': "kalıp — 'fe-eqîmu's-salâte ve âtu'z-zekâh' (2 ayet)", 'not': 'ortak kalıp.'},
 {'bag': '9:16 → 58:13', 'kural': "kalıp — 've'llâhu habîrun bimâ ta'melûn' (4 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '58:11 → 58:13', 'kural': "okuma — 'bimâ ta'melûne habîr' / 'habîrun bimâ ta'melûn' ters sıra", 'not': 'sûre içi.'},
 {'bag': '58:8 → 58:14', 'kural': "nakarat3 — 'e lem tera ile'llezîne': fısıldaşanlar / dost edinenler", 'not': 'sûre içi eş.'},
 {'bag': '48:6 → 58:14', 'kural': "okuma — 'ğadiba'llâhu aleyhim' + 'e'adde lehum'", 'not': 'lemma eşi.'},
 {'bag': '9:56 → 58:14', 'kural': "okuma — yemin + 'mâ hum minkum'", 'not': 'ortak yapı.'},
 {'bag': '43:86 → 58:14', 'kural': "kalıp — 've hum ya'lemûn' (7 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '9:89 → 58:15', 'kural': "kalıp — 'e'adda'llâhu lehum': cennet / azap (aday 1039 kayıt)", 'not': 'karşıt kullanım.'},
 {'bag': '33:35 → 58:15', 'kural': "kalıp — 'e'adda'llâhu lehum': bağış / azap (aday 1039 kayıt)", 'not': 'karşıt kullanım.'},
 {'bag': '9:9 → 58:15', 'kural': "kalıp + ölçüm xref — 'innehum sâ'e mâ kânû ya'melûn' (3 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '9:9 → 58:16', 'kural': "okuma — 'fe-saddû an sebîlih' / 'fe-saddû an sebîli'llâh'", 'not': 'ortak fiil.'},
 {'bag': '56:27 → 58:16', 'kural': "okuma — lemma 'yemîn' sağ yan / yeminler (1021)", 'not': 'lemma ayrımı.'},
 {'bag': '58:5 → 58:16', 'kural': "okuma — 'azâbun muhîn' sûre içi eşi", 'not': 'sûre içi eş.'},
 {'bag': '10:27 → 58:17', 'kural': "kalıp — 'ulâ'ike ashâbu'n-nâri hum fîhâ hâlidûn' (5 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '58:6 → 58:18', 'kural': "nakarat3 — 'yevme yeb'asuhumu'llâhu cemî'an': haber verme / yemin", 'not': 'sûre içi eş.'},
 {'bag': '9:62 → 58:18', 'kural': "okuma — 'yahlifûne … lekum'", 'not': 'ortak yapı.'},
 {'bag': '18:104 → 58:18', 'kural': "okuma — 'yahsebûne ennehum'", 'not': 'ortak yapı.'},
 {'bag': '43:37 → 58:18', 'kural': "okuma — 'yahsebûne ennehum'", 'not': 'ortak yapı.'},
 {'bag': '58:14 → 58:18', 'kural': "okuma — 'el-kezib' / 'el-kâzibûn'; حلف sûre içi", 'not': 'sûre içi.'},
 {'bag': '18:63 → 58:19', 'kural': "okuma — lemma 'ensâ': unutturan şeytan", 'not': 'lemma eşi.'},
 {'bag': '58:6 → 58:19', 'kural': "okuma — نسي: 'nesûh' (kendileri unuttu) / 'fe-ensâhum' (şeytan unutturdu)", 'not': 'sûre içi.'},
 {'bag': '58:10 → 58:19', 'kural': "okuma — şeytan sûre içinde (necvâ kaynağı / kuşatan)", 'not': 'sûre içi.'},
 {'bag': '58:5 → 58:20', 'kural': "nakarat3 — 'inne'llezîne yuhâddûna'llâhe ve rasûleh': kubitû / ezellîn", 'not': 'sûre içi eş.'},
 {'bag': '57:25 → 58:21', 'kural': "kalıp — 'inne'llâhe qaviyyun azîz' yalnız iki ayet, ardışık sûreler (aday 1040 kayıt)", 'not': 'ortak kapanış.'},
 {'bag': '22:40 → 58:21', 'kural': "okuma — 'le-qaviyyun azîz' biçim farkı", 'not': 'yakın kapanış.'},
 {'bag': '58:21 → 58:22', 'kural': "okuma — كتب: 'keteba'llâh' / 'ketebe fî qulûbihim'", 'not': 'sûre içi.'},
 {'bag': '9:44 → 58:22', 'kural': "kalıp — 'yu'minûne bi'llâhi ve'l-yevmi'l-âhir' (4 ayet)", 'not': 'ortak kalıp.'},
 {'bag': '9:63 → 58:22', 'kural': "okuma + ölçüm xref — lemma 'hâdde' (2 ayet)", 'not': 'lemma eşi.'},
 {'bag': '9:24 → 58:22', 'kural': "okuma + ölçüm xref — baba, oğul, kardeş, aşiret dizisi", 'not': 'ortak dizi.'},
 {'bag': '9:89 → 58:22', 'kural': "kalıp — 'cennâtin tecrî … hâlidîne fîhâ' (10 ayet)", 'not': 'ortak kalıp.'},
 {'bag': '57:12 → 58:22', 'kural': "kalıp — 'cennâtin tecrî … hâlidîne fîhâ' (10 ayet)", 'not': 'ortak kalıp.'},
 {'bag': '9:100 → 58:22', 'kural': "kalıp — 'radiya'llâhu anhum ve radû anh' (4 ayet); رضو iki gönderge (aday 1041 kayıt)", 'not': 'ortak kalıp.'},
 {'bag': '57:3 → 58:22', 'kural': "okuma — 'âhir' Allah / gün (aday 1041 kayıt)", 'not': 'aynı kelime iki gönderge.'},
 {'bag': '58:19 → 58:22', 'kural': "okuma — 'elâ inne hizb': hizbu'ş-şeytân / hizbu'llâh, hâsirûn / mufluhûn (aday 1039 kayıt)", 'not': 'sûre kapanışı.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_mucadele', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in MUCADELE]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_mucadele'] = MUCADELE
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_mucadele', len(MUCADELE), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_mucadele', len(BAGLAR['AS_mucadele']))
