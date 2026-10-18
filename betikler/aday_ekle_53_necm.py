# -*- coding: utf-8 -*-
"""aday_ekle_53_necm.py — sûre 53 (Necm) adayları (AX_necm) ve okuma bağları (AS_necm).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

NECM = [
]

BAGLAR = {"AS_necm": [
 {'bag': '52:49 → 53:1', 'kural': "okuma — ardışık sûre sınırı; fâsıla م → ى; 'idbâra'n-nucûm' / 've'n-necm'; aday 1040 alanında kayıt, test yok", 'not': 'sûre sınırı.'},
 {'bag': '51:1 · 52:1 → 53:1', 'kural': "okuma — ardışık üç sûre 've' yeminiyle açılıyor; QASEM yalnız 53:1'de işaretli (517)", 'not': 'yeminle açılış.'},
 {'bag': '14:37 · 20:81 · 22:31 → 53:1', 'kural': "'hevâ' (düşmek) lemma 8 ayet; okundu — yönelme / helak / savrulma / yıldızın düşüşü", 'not': 'düşmek.'},
 {'bag': '53:1 → 53:3', 'kural': "okuma — هوي [1/4], [2/4]: 'hevâ' düştü / 'el-hevâ' arzu", 'not': 'aynı kök.'},
 {'bag': '34:46 → 53:2 · 53:4', 'kural': "'sâhib' lemma 12 ayet; okundu — 'mâ bi-sâhibikum min cinne in huve illâ nezîr' / 'mâ dalle sâhibukum' + 'in huve illâ vahyun'", 'not': 'arkadaşınız.'},
 {'bag': '52:29 → 53:2', 'kural': "okuma — olumsuzlama: 'mâ ente … bi-kâhinin ve lâ mecnûn' 2MS / 'mâ dalle sâhibukum ve mâ ğavâ' 3MS; aday 1040 alanında kayıt", 'not': 'olumsuzlama.'},
 {'bag': '20:121 · 28:63 → 53:2', 'kural': "'ğavâ' lemma 3 ayet; okundu", 'not': 'azmak.'},
 {'bag': '53:3 → 53:4', 'kural': "okuma — 'el-hevâ' / 'vahy'; karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'arzu, vahiy.'},
 {'bag': '36:69 · 12:104 · 38:87 · 23:25 → 53:4', 'kural': "lemma dizisi 'in huve illâ' 33 ayet; okundu — zikir / Kur'ân / 'racûlun bihî cinne' (inkârcı sözü) / vahiy", 'not': 'ancak.'},
 {'bag': '11:37 · 23:27 → 53:4', 'kural': "'vahy' lemma 6 ayet; okundu", 'not': 'vahiy.'},
 {'bag': '51:58 → 53:5 · 53:6', 'kural': "okuma — 'zu'l-quvveti'l-metîn' / 'şedîdu'l-quvâ', 'zû mirra' (53:5 özne adsız)", 'not': 'güç.'},
 {'bag': '20:5 · 41:11 · 28:14 · 48:29 → 53:6', 'kural': "'istevâ' lemma 33 ayet; okundu — Rahmân / göğe yönelme / ergenlik / ekin; 53:6 özne adsız (aday 1041 alanında kayıt)", 'not': 'doğruldu.'},
 {'bag': '41:53 → 53:7', 'kural': "'ufuq' lemma 3 ayet; okundu — 'âfâq' / 'el-ufuqi'l-a'lâ'", 'not': 'ufuk.'},
 {'bag': '53:7 → 53:8', 'kural': "okuma — 'el-a'lâ' / 'tedellâ'; karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'yüksek, sarkma.'},
 {'bag': '53:8 → 53:9', 'kural': "okuma — دنو [1/3] 'denâ' → [2/3] 'ednâ'", 'not': 'yakınlık.'},
 {'bag': '20:38 → 53:10', 'kural': "lemma dizisi 'mâ evhâ' 17 ayet; okundu — 'evhaynâ ilâ ummike mâ yûhâ' 1P / 'evhâ ilâ abdihî mâ evhâ' 3MS", 'not': 'vahyettiğini.'},
 {'bag': '53:4 → 53:10', 'kural': "okuma — وحي sûre içi [1,2/4] → [3,4/4]", 'not': 'vahiy.'},
 {'bag': '17:36 · 28:10 → 53:11', 'kural': "'fuâd' lemma 15 ayet; okundu — 17:36 'basar' + 'fuâd' bir ayette / 53:11 'fuâd', 53:17 'basar'", 'not': 'gönül.'},
 {'bag': '53:11 → 53:19', 'kural': "okuma — رأي sûre içi [1/8] … [5/8]: gören 3MS (53:11, 12, 13, 18) → muhatap 2MP 'e-fe-ra'eytum'", 'not': 'görme zinciri.'},
 {'bag': '53:11 → 53:12', 'kural': "okuma — 'mâ kezebe'l-fuâd' / 'e-fe-tumârûnehû'; karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'yalanlamama, tartışma.'},
 {'bag': '42:18 → 53:12', 'kural': "'tumâr' lemma 4 ayet; okundu", 'not': 'tartışma.'},
 {'bag': '53:13 → 53:20', 'kural': "okuma — أخر [1/6], [2/6]: 'nezleten uhrâ' / 'el-uhrâ'", 'not': 'öteki.'},
 {'bag': '53:14 → 53:16', 'kural': "'sidre' lemma 2 ayet — korpusta yalnız bu sûrede", 'not': 'sidre.'},
 {'bag': '32:19 → 53:15', 'kural': "lemma dizisi 'cenne + me'vâ' 3 ayet; okundu — 'cennâtu'l-me'vâ' / 'cennetu'l-me'vâ'", 'not': "me'vâ cenneti."},
 {'bag': '20:78 → 53:16', 'kural': "okuma — 'ğaşiyehum … mâ ğaşiyehum' / 'yağşe's-sidrete mâ yağşâ': aynı fiille müphem tekrar", 'not': 'bürüyen.'},
 {'bag': '53:10 → 53:16', 'kural': "okuma — 'fiil + mâ + aynı fiil' sûre içinde iki kez: 'evhâ … mâ evhâ' / 'yağşâ … mâ yağşâ'", 'not': 'müphem tekrar.'},
 {'bag': '33:10 → 53:17', 'kural': "lemma dizisi 'zâğa basar' 2 ayet; okundu — korkuda gözlerin kayması / kaymaması", 'not': 'göz.'},
 {'bag': '53:2 → 53:17', 'kural': "okuma — 'mâ … ve mâ' olumsuzlaması iki kez: sapmadı, azmadı / kaymadı, aşmadı", 'not': 'kuruluş.'},
 {'bag': '20:23 → 53:18', 'kural': "okuma — 'min âyâtine'l-kubrâ' 1P / 'min âyâti rabbihi'l-kubrâ' 3MS", 'not': 'büyük işaretler.'},
 {'bag': '26:75 · 39:38 → 53:19', 'kural': "kalıp 'e-fe-ra'eytum' 7 ayet; okundu — tapınılanlara dönük soru; burada adla", 'not': 'gördünüz mü.'},
 {'bag': '38:9 → 53:19', 'kural': "okuma — عزز 'el-azîz' Rab / 'el-Uzzâ' put adı (aday 1041 alanı, kök düzeyi; kayıt)", 'not': 'izzet.'},
 {'bag': '53:18 → 53:19', 'kural': "okuma — 'âyâti rabbihi'l-kubrâ' / 'el-Lâte ve'l-Uzzâ'; karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'işaretler, putlar.'},
 {'bag': '52:39 → 53:21', 'kural': "okuma — 'em lehu'l-benâtu ve lekumu'l-benûn' / 'e-lekumu'z-zekeru ve lehu'l-unsâ': aynı paylaştırma kuruluşu, sıra ters", 'not': 'erkek, dişi.'},
 {'bag': '12:40 → 53:23', 'kural': "lemma dizisi 'esmâ … semmeytumûhâ … min sultân' 2 ayet; okundu — tapınılanlar / adlı putlar", 'not': 'konulmuş adlar.'},
 {'bag': '10:66 → 53:23', 'kural': "tam kalıp 'in yettebi'ûne ille'z-zann' 4 ayet; okundu", 'not': 'zan.'},
 {'bag': '53:3 → 53:23', 'kural': "okuma — هوي sûre içi: 'mâ yantiqu ani'l-hevâ' / 'mâ tehve'l-enfus'", 'not': 'hevâ.'},
 {'bag': '53:23 → 53:28', 'kural': "tam kalıp 'in yettebi'ûne ille'z-zann' sûre içi iki kez (nakarat3 GEÇER)", 'not': 'zan nakaratı.'},
 {'bag': '28:70 → 53:25', 'kural': "okuma — 'fi'l-ûlâ ve'l-âhira' / 'el-âhiratu ve'l-ûlâ': aynı ikili ters sırada", 'not': 'son ve ilk.'},
 {'bag': '36:23 → 53:26', 'kural': "tam kalıp 'şefâ'atuhum şey'en' 2 ayet; okundu — tapınılan ilâhlar / melekler", 'not': 'şefaat.'},
 {'bag': '20:109 · 34:23 → 53:26', 'kural': "okuma — şefaat + izin istisnası; 20:109'da 'radiye' de", 'not': 'izin.'},
 {'bag': '37:150 · 43:19 → 53:27', 'kural': "okuma — melekleri dişi sayma: 'inâs' / 'tesmiyete'l-unsâ'", 'not': 'melekler dişi.'},
 {'bag': '53:23 → 53:27', 'kural': "okuma — سمو ad koyma ipliği: 'esmâ'un semmeytumûhâ' / 'yusemmûne … tesmiye'", 'not': 'adlandırma.'},
 {'bag': '10:36 → 53:28', 'kural': "tam kalıp 'ez-zanne lâ yuğnî mine'l-haqqi şey'â' 2 ayet; okundu", 'not': 'zan, hak.'},
 {'bag': '53:26 → 53:28', 'kural': "okuma — 'lâ tuğnî … şey'en' şefaat için / 'lâ yuğnî … şey'â' zan için", 'not': 'yaramaz.'},
 {'bag': '16:125 → 53:30', 'kural': "tam kalıp 'inne rabbeke huwa a'lemu bi-men dalle an sebîlihî' 3 ayet; okundu — 'bi'l-muhtedîn' / 'bi-meni'htedâ'", 'not': 'en iyi bilen.'},
 {'bag': '53:2 → 53:30', 'kural': "okuma — ضلل sûre içi: 'mâ dalle' olumsuz / 'men dalle' sapan", 'not': 'sapma.'},
 {'bag': '53:21 · 53:25 · 53:30', 'kural': 'okuma — ayet içi karşıt çiftler: zeker / unsâ, âhira / ûlâ, dalle / ihtedâ (aday 1039, kayıt)', 'not': 'karşıt çiftler.'},
 {'bag': '53:25 → 53:31', 'kural': "okuma — 'li'llâh' takdimi sûre içi iki kez: 'fe-li'llâhi'l-âhiratu' / 've li'llâhi mâ fi's-semâvât'", 'not': 'Allahındır.'},
 {'bag': '42:37 → 53:32', 'kural': "lemma dizisi 'yectenibûne kebâ'ira'l-ismi ve'l-fevâhiş' 2 ayet; okundu — ardından 'hum yağfirûn' / 'vâsi'u'l-mağfira' (aday 1041 alanı, kayıt)", 'not': 'kaçınanlar.'},
 {'bag': '16:78 · 39:6 → 53:32', 'kural': "tam kalıp 'butûni ummehâtikum' 3 ayet; okundu — çıkarma / ardışık yaratma / cenin hâli", 'not': 'annelerin karnı.'},
 {'bag': '35:18 → 53:32', 'kural': "okuma — زكو: 'men tezekkâ … li-nefsih' / 'fe-lâ tuzekkû enfusekum'", 'not': 'arınma.'},
 {'bag': '53:30 → 53:32', 'kural': "okuma — 'huwa a'lemu bi-men' sûre içi: dört 'a'lem' (53:30×2, 53:32×2)", 'not': 'en iyi bilen.'},
 {'bag': '19:77 · 45:23 → 53:33', 'kural': "tam kelime 'e-fe-ra'eyte' 4 ayet; okundu — 'ellezî kefera' / 'ellezî tevellâ'", 'not': 'gördün mü.'},
 {'bag': '53:29 → 53:33', 'kural': "okuma — ولي sûre içi: 'men tevellâ' / 'ellezî tevellâ'", 'not': 'arka çeviren.'},
 {'bag': '52:41 → 53:35', 'kural': "okuma — 'em indehumu'l-ğaybu fe-hum yektubûn' / 'e-'indehû ilmu'l-ğaybi fe-huwa yerâ': aynı kuruluş", 'not': 'gayb.'},
 {'bag': '17:15 · 35:18 · 39:7 → 53:38', 'kural': "tam kalıp 'teziru vâziratun vizra uhrâ' 5 ayet; okundu — 've lâ' / 'en lâ' (sahifelerin haberi)", 'not': 'yük.'},
 {'bag': '53:24 → 53:39', 'kural': "okuma — 'li'l-insân' iki kez: 'mâ temennâ' / 'illâ mâ se'â'; ayetler arası karşıt çift (aday 1039)", 'not': 'temenni, çaba.'},
 {'bag': '20:15 → 53:39', 'kural': "okuma — سعي: 'li-tuczâ kullu nefsin bi-mâ tes'â' / 'illâ mâ se'â'", 'not': 'çaba.'},
 {'bag': '53:11 → 53:40', 'kural': "okuma — رأي sûre içi [1/8] → [8/8]: gören 3MS'den edilgen 'yurâ'ya", 'not': 'görme zinciri.'},
 {'bag': '53:31 → 53:41', 'kural': "okuma — جزي sûre içi dört: 'li-yecziye … ve yecziye' / 'yuczâhu'l-cezâ'", 'not': 'karşılık.'},
 {'bag': '53:37 → 53:41', 'kural': "okuma — وفي: 'ellezî vaffâ' / 'el-cezâ'e'l-evfâ'", 'not': 'tam.'},
 {'bag': '20:15 → 53:41', 'kural': "okuma — 'sa'y' ardından edilgen 'tuczâ' / 'yuczâ'", 'not': 'çaba, karşılık.'},
 {'bag': '53:14 → 53:42', 'kural': "okuma — 'muntehâ' lemma sûre içi iki kez: 'sidrati'l-muntehâ' / 'ilâ rabbike'l-muntehâ'", 'not': 'son varış.'},
 {'bag': '53:43 · 53:44 · 53:48 · 53:49', 'kural': "tam kalıp 've ennehû huwa' 4 ayet — korpusta yalnız bu sûrede", 'not': 'O odur.'},
 {'bag': '9:82 → 53:43', 'kural': 'okuma — gülme / ağlama çifti: I. bab emir / IV. bab ettirgen', 'not': 'gülme, ağlama.'},
 {'bag': '50:43 → 53:44', 'kural': "okuma — 'nuhyî ve numît' 1P / 'emâte ve ahyâ' 3MS, sıra ters", 'not': 'ölüm, dirilik.'},
 {'bag': '53:21 → 53:45', 'kural': 'okuma — ذكر/أنث sûre içi: paylaştırma sorusu / ikisinin yaratılması', 'not': 'erkek, dişi.'},
 {'bag': '51:49 → 53:45', 'kural': "okuma — 'halaqnâ zevceyn' / 'halaqa'z-zevceyn'", 'not': 'iki eş.'},
 {'bag': '35:11 → 53:46', 'kural': 'okuma — nutfe + eşler: toprak → nutfe → eşler / eşler ← nutfe', 'not': 'nutfe.'},
 {'bag': '53:20 · 53:24 → 53:46', 'kural': 'okuma — مني sayacı üç anlam: Menât / temennâ / tumnâ (gloss 1021)', 'not': 'tek sayaç.'},
 {'bag': '29:20 → 53:47', 'kural': "lemma 'neş'e' 3 ayet; okundu — 'en-neş'ete'l-âhira' / 'en-neş'ete'l-uhrâ'", 'not': 'öteki yaratılış.'},
 {'bag': '53:32 → 53:47', 'kural': "okuma — نشأ: 'iz enşe'ekum mine'l-ard' / 'en-neş'ete'l-uhrâ'; ayetler arası karşıt çift (aday 1039)", 'not': 'ilk ve öteki.'},
 {'bag': '53:26 · 53:28 → 53:48', 'kural': "okuma — غني: 'lâ tuğnî' / 'lâ yuğnî' olumsuz / 'huwa ağnâ' olumlu", 'not': 'zengin etme.'},
 {'bag': '53:1 → 53:49', 'kural': "okuma — 've'n-necm' yemini / 'rabbu'ş-şi'râ' adlı yıldız", 'not': 'yıldız.'},
 {'bag': '51:41 → 53:50', 'kural': 'okuma — Âd helâki: 1P anlatı / 3MS haber', 'not': 'Âd.'},
 {'bag': '51:43 → 53:51', 'kural': "okuma — Semûd: 'qîle lehum temetta'û' / 'fe-mâ ebqâ'", 'not': 'Semûd.'},
 {'bag': '51:46 → 53:52', 'kural': "tam kalıp 've qavme nûhin min qabl' 2 ayet; okundu — 'qavmen fâsiqîn' / 'ezleme ve atğâ'", 'not': 'Nûh kavmi.'},
 {'bag': '9:70 → 53:50 · 53:51 · 53:52 · 53:53', 'kural': "okuma — Nûh kavmi, Âd, Semûd, 'mu'tefikât' bir ayette / 53:50-53'te dört ayete dağılmış", 'not': 'helâk listesi.'},
 {'bag': '53:17 → 53:52', 'kural': "okuma — طغي: 'mâ tağâ' (göz) / 'atğâ' (kavim); ayetler arası karşıt çift (aday 1039)", 'not': 'azgınlık.'},
 {'bag': '53:1 → 53:53', 'kural': "okuma — هوي sûre içi ilk ve son: 'izâ hevâ' / 'ehvâ'", 'not': 'düşme.'},
 {'bag': '53:10 · 53:16 → 53:54', 'kural': "okuma — 'fiil + mâ + aynı fiil' sûre içi üçüncü kez; 53:16 ile aynı kök غشو", 'not': 'müphem tekrar.'},
 {'bag': '53:12 → 53:55', 'kural': "okuma — مري: 'e-fe-tumârûnehû' 2MP / 'tetemârâ' 2MS", 'not': 'kuşku.'},
 {'bag': '51:50 → 53:56', 'kural': "okuma — 'nezîrun mubîn' / 'nezîrun mine'n-nuzuri'l-ûlâ'", 'not': 'uyarıcı.'},
 {'bag': '40:18 → 53:57', 'kural': "lemma 'âzife' 2 ayet; okundu — 'yevme'l-âzife' / 'ezifeti'l-âzife'", 'not': 'yaklaşan.'},
 {'bag': '39:38 → 53:58', 'kural': "lemma 'kâşife' 2 ayet; okundu — Allah'tan başkası giderebilir mi / Allah'tan başka giderici yok", 'not': 'giderici.'},
 {'bag': '52:34 → 53:59', 'kural': "okuma — 'bi-hadîsin mislihî' / 'hâze'l-hadîs'", 'not': 'söz.'},
 {'bag': '53:43 → 53:60', 'kural': "okuma — 'adheke ve ebkâ' / 'tadhakûne ve lâ tebkûn': ettirgen 3MS / 2MP", 'not': 'gülme, ağlama.'},
 {'bag': '41:37 → 53:62', 'kural': "okuma — 've'scudû li'llâh … ta'budûn' / 'fe'scudû li'llâhi va'budû'", 'not': 'secde, kulluk.'},
 {'bag': '53:1 → 53:62', 'kural': 'okuma — sûre yıldız yeminiyle açılıp secde emriyle kapanıyor', 'not': 'açılış, kapanış.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_necm', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in NECM]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_necm'] = NECM
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_necm', len(NECM), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_necm', len(BAGLAR['AS_necm']))
