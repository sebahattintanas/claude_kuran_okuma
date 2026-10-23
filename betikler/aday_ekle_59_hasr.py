# -*- coding: utf-8 -*-
"""aday_ekle_59_hasr.py — sûre 59 (Haşr) adayları (AX_hasr) ve okuma bağları (AS_hasr).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

HASR = [
]

BAGLAR = {"AS_hasr": [
 # blok 1-5
 {'bag': '58:22 → 59:1', 'kural': "okuma — ardışık sûre sınırı; grup adıyla ('hizbu'llâh … el-mufluhûn') kapanış / tesbihle açılış, lafız 2. kelimede; fâsıla ن → م (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '57:1 → 59:1', 'kural': "kalıp + esit2 BENZER — 'sebbaha lillâh' (3 ayet) ve 've huve'l-azîzu'l-hakîm'; fark 've'l-ard' / 've mâ fi'l-ard'", 'not': 'ortak açılış.'},
 {'bag': '50:44 → 59:2', 'kural': "okuma — lemma 'haşr' (2 ayet): âhiret toplanması / dünyada ilk toplanma", 'not': 'lemma eşi.'},
 {'bag': '57:3 → 59:2', 'kural': "okuma — lemma 'evvel' Allah için / toplanmanın ilki (aday 1041, kayıt)", 'not': 'aynı kelime iki gönderge.'},
 {'bag': '39:47 → 59:2', 'kural': "okuma — lemma 'yahtesib' (3 ayet): Allah'tan hesapta olmayanın gelişi", 'not': 'lemma eşi.'},
 {'bag': '16:26 → 59:2', 'kural': "okuma — lafız + 'etâ' + yapı (bina / kaleler) ve 'min haysu' + olumsuz bilme aynı ayette", 'not': 'ortak yapı.'},
 {'bag': '33:26 → 59:2', 'kural': "kalıp + ölçüm xref — 'qazefe fî qulûbihimu'r-ru'b' (2 ayet); 'min ehli'l-kitâb' + 'min' + yer çoğulu dizilimi ortak", 'not': 'kalıp eşi.'},
 {'bag': '24:44 → 59:2', 'kural': "okuma — kök عبر + 'uli'l-ebsâr' (lemma dizisi 3 ayet): ibret haberi / ibret emri", 'not': 'ortak hitap.'},
 {'bag': '58:21 → 59:3', 'kural': "okuma — lemma dizisi 'ketebe + lafız' (5 ayet): galibiyet yazılması / sürgün yazılması", 'not': 'lemma dizisi eşi.'},
 {'bag': '24:23 → 59:3', 'kural': "ölçüm xref — dünya + âhiret + 've lehum azâb'", 'not': 'xref.'},
 {'bag': '57:3 → 59:3', 'kural': "okuma — lemma 'âhir' Allah için / âhiret (aday 1041, kayıt)", 'not': 'aynı kelime iki gönderge.'},
 {'bag': '59:3 → 59:4', 'kural': "okuma — 'zâlike bi-ennehum': sürgünün ve azabın gerekçesi", 'not': 'sûre içi akış.'},
 {'bag': '16:27 → 59:4', 'kural': "okuma — lemma 'şâqqa' (5 ayet)", 'not': 'lemma eşi.'},
 {'bag': '47:32 → 59:4', 'kural': "okuma — lemma 'şâqqa': elçiye karşı gelme / Allah'a ve elçisine", 'not': 'lemma eşi.'},
 {'bag': '8:13 → 59:4', 'kural': "esit2 BENZER + ölçüm xref — 'zâlike bi-ennehum şâqqu'llâhe ve rasûleh … şedîdu'l-iqâb'; 8:13 henüz okunmadı", 'not': 'kalıp eşi.'},
 {'bag': '14:24 → 59:5', 'kural': "okuma — lemma 'asl' (3 ayet): benzetmedeki ağacın kökü / kökü üzerinde bırakılan ağaç", 'not': 'lemma eşi.'},
 {'bag': '16:27 → 59:5', 'kural': "okuma — 'yuhzî' + 'tuşâqqûn' aynı ayette / 59:4 'şâqqû' + 59:5 'li-yuhziye' ardışık", 'not': 'ortak ikili.'},
 {'bag': '59:4 → 59:5', 'kural': "okuma — karşı gelme (şâqqa) → rezil etme (ahzâ) ardışık", 'not': 'sûre içi akış.'},
 # blok 6-10
 {'bag': '33:50 → 59:6', 'kural': "okuma — lemma 'efâ'e' (3 ayet): 2MS muhataba / 'alâ rasûlih'", 'not': 'lemma eşi.'},
 {'bag': '16:8 → 59:6', 'kural': "okuma — lemma 'hayl': binilmek için / koşturulmayan binek", 'not': 'lemma eşi.'},
 {'bag': '9:39 → 59:6', 'kural': "kalıp — 've'llâhu alâ kulli şey'in qadîr' (9 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '59:6 → 59:7', 'kural': "nakarat3 GEÇER — 'mâ efâ'e'llâhu alâ rasûlih' (lemma dizisi 2 ayet)", 'not': 'sûre içi eş.'},
 {'bag': '12:109 → 59:7', 'kural': "kalıp — 'min ehli'l-qurâ' (2 ayet): elçilerin geldiği / feyin geldiği yer", 'not': 'ortak kalıp.'},
 {'bag': '59:4 → 59:7', 'kural': "sûre içi kalıp — 'inna'llâhe şedîdu'l-iqâb': şarta bağlı hüküm / takvâ emrinin gerekçesi", 'not': 'sûre içi eş.'},
 {'bag': '8:41 → 59:7', 'kural': "kalıp + ölçüm xref — 've li-zi'l-qurbâ ve'l-yetâmâ ve'l-mesâkîni ve'bni's-sebîl' (2 ayet); 8:41 henüz okunmadı", 'not': 'kalıp eşi.'},
 {'bag': '22:40 → 59:8', 'kural': "kalıp — 'ellezîne uhricû min diyârihim' (2 ayet)", 'not': 'ortak kalıp.'},
 {'bag': '48:29 → 59:8', 'kural': "kalıp + ölçüm xref — 'yebteğûne fadlen mina'llâhi ve ridvânâ' (2 ayet)", 'not': 'ortak kalıp.'},
 {'bag': '49:15 → 59:8', 'kural': "kalıp — 'ulâ'ike humu's-sâdiqûn' (2 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '59:2 → 59:8', 'kural': "okuma — 'min diyârihim'; 'ahrace' (etken, Allah) / 'uhricû' (edilgen, muhâcirler) — iki karşıt grup (aday 1039, kayıt)", 'not': 'sûre içi karşıt.'},
 {'bag': '12:91 → 59:9', 'kural': "okuma — lemma 'âthara' özne Allah / insanlar (aday 1041, kayıt)", 'not': 'aynı fiil iki gönderge.'},
 {'bag': '2:5 → 59:9', 'kural': "lemma dizisi — 'ulâ'ike humu'l-mufluhûn' (11 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '58:22 → 59:9', 'kural': "okuma — 'humu'l-mufluhûn': önceki sûrenin son kelimesi / ayet sonu", 'not': 'ortak kapanış.'},
 {'bag': '59:8 → 59:9', 'kural': "okuma — 'ulâ'ike humu's-sâdiqûn' / 'ulâ'ike humu'l-mufluhûn' ardışık; 'muhâcirîn' / 'hâcera'", 'not': 'sûre içi akış.'},
 {'bag': '64:16 → 59:9', 'kural': "kalıp + ölçüm xref — 've men yûqa şuhha nefsihî fe-ulâ'ike humu'l-mufluhûn'; 64:16 henüz okunmadı", 'not': 'kalıp eşi.'},
 {'bag': '15:47 → 59:10', 'kural': "okuma — 'ğıll' + 'ihvân' aynı ayette: göğüslerden kinin çekilmesi / kalplerde kin bırakılmaması duası", 'not': 'ortak ikili.'},
 {'bag': '16:7 → 59:10', 'kural': "lemma dizisi + ölçüm xref — 'ra'ûf + rahîm' (9 ayet), Rab haberi", 'not': 'ortak kapanış.'},
 {'bag': '59:9 → 59:10', 'kural': "okuma — 'fî sudûrihim' / 'fî qulûbinâ'; üç grup dizisinin kapanışı", 'not': 'sûre içi akış.'},
 # blok 11-17
 {'bag': '58:14 → 59:11', 'kural': "kalıp — 'e lem tera ile'llezîne' (12 ayet); yalana yemin / 'le-kâzibûn'", 'not': 'ortak açılış.'},
 {'bag': '9:107 → 59:11', 'kural': "kalıp + ölçüm xref — 've'llâhu yeşhedu innehum le-kâzibûn' (2 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '59:2 → 59:11', 'kural': "nakarat3 GEÇER + ölçüm xref — 'ellezîne keferû min ehli'l-kitâb': Allah'ın çıkardıkları / münafıkların kardeşleri", 'not': 'sûre içi eş.'},
 {'bag': '59:10 → 59:11', 'kural': "okuma — 'ihvâninâ' / 'ihvânihim': ardışık iki karşıt kardeşlik (aday 1039, kayıt)", 'not': 'sûre içi karşıt.'},
 {'bag': '59:11 → 59:12', 'kural': "okuma — üç vaat / üç olumsuzlama ('le-in' ×3)", 'not': 'sûre içi akış.'},
 {'bag': '48:22 → 59:12', 'kural': "lemma dizisi — 'vellâ + dubur' (6 ayet) + 'summe lâ' + yardım yokluğu", 'not': 'ortak yapı.'},
 {'bag': '3:111 → 59:12', 'kural': "kalıp + ölçüm xref — 'yuvellûkumu'l-edbâr … summe lâ yunsarûn'; 3:111 henüz okunmadı", 'not': 'kalıp eşi.'},
 {'bag': '9:6 → 59:13', 'kural': "lemma dizisi — 'zâlike bi-ennehum qavmun lâ' (4 ayet)", 'not': 'ortak gerekçe.'},
 {'bag': '59:9 → 59:13', 'kural': "okuma — 'fî sudûrihim': ihtiyaç duymama / korku (aday 1039, kayıt)", 'not': 'sûre içi karşıt.'},
 {'bag': '59:13 → 59:14', 'kural': "nakarat3 GEÇER — 'zâlike bi-ennehum qavmun lâ': 'yefqahûn' / 'ya'qilûn'", 'not': 'sûre içi eş.'},
 {'bag': '59:2 → 59:14', 'kural': "okuma — kök حصن: 'husûnuhum' / 'qurâ muhassana'", 'not': 'sûre içi kök.'},
 {'bag': '20:53 → 59:14', 'kural': "okuma — lemma 'şettâ' (3 ayet): bitki çeşitliliği / kalplerin dağınıklığı", 'not': 'lemma eşi.'},
 {'bag': '59:15 → 59:16', 'kural': "okuma — ardışık iki mesel 'ke-meseli'", 'not': 'sûre içi akış.'},
 {'bag': '59:13 → 59:16', 'kural': "okuma — muhataplardan korku / şeytanın 'ehâfu'llâh' sözü", 'not': 'sûre içi karşıt.'},
 {'bag': '5:28 → 59:16', 'kural': "kalıp + ölçüm xref — 'innî ehâfu'llâha rabbe'l-âlemîn' (2 ayet); 5:28 henüz okunmadı", 'not': 'kalıp eşi.'},
 {'bag': '12:109 → 59:17', 'kural': "lemma dizisi — 'kâne + âqibe' (24 ayet)", 'not': 'ortak kalıp.'},
 {'bag': '59:3 → 59:17', 'kural': "okuma — kök نور 'nâr': 'azâbu'n-nâr' / 'fi'n-nâr'", 'not': 'sûre içi kök.'},
 # blok 18-24
 {'bag': '57:28 → 59:18', 'kural': "kalıp — 'yâ eyyuhe'llezîne âmenu'tteqû'llâh' (7 ayet)", 'not': 'ortak açılış.'},
 {'bag': '24:53 → 59:18', 'kural': "kalıp — 'inna'llâhe habîrun bimâ ta'melûn' (3 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '58:12 → 59:18', 'kural': "okuma — lemma 'qaddeme': sadaka önden / yarın için önden", 'not': 'lemma eşi.'},
 {'bag': '59:7 → 59:18', 'kural': "nakarat3 GEÇER — 'vettequ'llâhe inna'llâh'", 'not': 'sûre içi eş.'},
 {'bag': '58:19 → 59:19', 'kural': "okuma — lemma 'ensâ': şeytan Allah'ın zikrini unutturur / Allah kendilerini unutturur (aday 1041, kayıt)", 'not': 'lemma eşi, iki özne.'},
 {'bag': '9:67 → 59:19', 'kural': "okuma — 'nesu'llâh' + karşılık unutma; 'humu'l-fâsiqûn' kapanışı", 'not': 'ortak ikili.'},
 {'bag': '59:5 → 59:19', 'kural': "sûre içi — lemma 'fâsiq' (59:5, 59:19)", 'not': 'sûre içi eş.'},
 {'bag': '9:20 → 59:20', 'kural': "okuma — lemma 'fâ'iz' + 'hum' kapanışı", 'not': 'ortak kapanış.'},
 {'bag': '59:17 → 59:20', 'kural': "okuma — 'fi'n-nâr' / 'ashâbu'n-nâr'; kök نور sûre içi son", 'not': 'sûre içi akış.'},
 {'bag': '59:19 → 59:20', 'kural': "okuma — 'humu'l-fâsiqûn' / 'humu'l-fâ'izûn' (aday 1039, kayıt)", 'not': 'sûre içi karşıt.'},
 {'bag': '33:72 → 59:21', 'kural': "okuma — dağ(lar) iki varsayım sahnesinde: emanetten kaçınma / Kur'an karşısında yarılma", 'not': 'lemma eşi.'},
 {'bag': '29:43 → 59:21', 'kural': "kalıp + ölçüm xref — 've tilke'l-emsâlu nadribuhâ li'n-nâs' (2 ayet)", 'not': 'ortak kalıp.'},
 {'bag': '59:15 → 59:21', 'kural': "sûre içi — mesel kökü ('ke-meseli' ×2 / 'el-emsâl'); مثل [3/3]", 'not': 'sûre içi eş.'},
 {'bag': '59:14 → 59:21', 'kural': "okuma — 'lâ ya'qilûn' / 'le-allehum yetefekkerûn'; dağın huşûsu / anlamayan topluluk (aday 1039, kayıt)", 'not': 'sûre içi karşıt.'},
 {'bag': '20:8 → 59:22', 'kural': "okuma — 'lâ ilâhe illâ hu' + 'lehu'l-esmâ'u'l-husnâ' (59:24)", 'not': 'ortak dizi.'},
 {'bag': '13:9 → 59:22', 'kural': "kalıp — 'âlimu'l-ğaybi ve'ş-şehâde' (10 ayet)", 'not': 'ortak kalıp.'},
 {'bag': '59:22 → 59:23', 'kural': "nakarat3 GEÇER — 'huve'llâhu'llezî lâ ilâhe illâ hu' (2 ayet, ikisi bu sûrede)", 'not': 'sûre içi eş.'},
 {'bag': '59:2 → 59:23', 'kural': "okuma — lemma 'mu'min' aynı sûrede inananlar (DEĞİL) / Allah (İLÂHÎ) (aday 1041, kayıt)", 'not': 'aynı kelime iki gönderge.'},
 {'bag': '40:35 → 59:23', 'kural': "okuma — 'mutekebbir' + 'cebbâr' insan kalbi / Allah (aday 1041, kayıt)", 'not': 'aynı ikili iki gönderge.'},
 {'bag': '12:54 → 59:23', 'kural': "okuma — lemma 'melik' insan kral / Allah (aday 1041, kayıt)", 'not': 'aynı kelime iki gönderge.'},
 {'bag': '52:43 → 59:23', 'kural': "kalıp + ölçüm xref — 'subhâna'llâhi ammâ yuşrikûn' (2 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '59:1 → 59:24', 'kural': "nakarat3 GEÇER — 've huve'l-azîzu'l-hakîm'; sûre halkası 'sebbaha' / 'yusebbihu' (PERF → IMPF)", 'not': 'sûre halkası.'},
 {'bag': '59:16 → 59:24', 'kural': "okuma — kök برأ: 'berî'' (uzak durma) / 'el-bâri'' (yaratan)", 'not': 'kökün iki anlamı.'},
 {'bag': '20:8 → 59:24', 'kural': "kalıp — 'lehu'l-esmâ'u'l-husnâ' (2 ayet)", 'not': 'ortak kalıp.'},
 {'bag': '24:41 → 59:24', 'kural': "ölçüm xref — 'yusebbihu lehû … fi's-semâvâti ve'l-ard': 'men' + kuşlar / 'mâ'", 'not': 'xref.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_hasr', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in HASR]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_hasr'] = HASR
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_hasr', len(HASR), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_hasr', len(BAGLAR['AS_hasr']))
