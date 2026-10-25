# -*- coding: utf-8 -*-
"""aday_ekle_64_tegabun.py — sûre 64 (Teğâbun) adayları (AX_tegabun) ve okuma bağları (AS_tegabun).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

TEGABUN = [
]

BAGLAR = {"AS_tegabun": [
 # blok 1-6
 {'bag': '63:11 → 64:1', 'kural': "okuma — ardışık sûre sınırı; ecelin ertelenmemesi, 'habîrun bimâ ta'melûn' / göklerin ve yerin tesbihi; fâsıla ن → ر (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '62:1 → 64:1', 'kural': "lemma dizisi + ölçüm xref — 'yusebbihu li'llâhi mâ fi's-semâvâti ve mâ fi'l-ard'; harekesiz 'yusebbihu li'llâh' 2 ayet; ad dizisi / 'lehu'l-mulku ve lehu'l-hamd'; ardışık değil", 'not': 'açılış eşi (okuma bağı).'},
 {'bag': '57:4 → 64:2', 'kural': "lemma dizisi — 've'llâhu bimâ ta'melûne basîr' (12 ayet); 'huve'llezî halaqa' gökler ve yer / 2MP", 'not': 'ortak kapanış.'},
 {'bag': '39:5 → 64:3', 'kural': "lemma dizisi — 'halaqa's-semâvâti ve'l-arda bi'l-haqq' (5 ayet); gece-gündüz / biçim", 'not': 'kalıp eşi.'},
 {'bag': '40:64 → 64:3', 'kural': "lemma dizisi + ölçüm xref — 've savvarakum fe-ahsene suverakum' (2 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '64:2 → 64:3', 'kural': "sûre içi — kök خلق: 'halaqakum' / 'halaqa' (خلق [2/2])", 'not': 'sûre içi eş.'},
 {'bag': '16:19 → 64:4', 'kural': "lemma dizisi — 'ya'lemu mâ tusirrûne ve mâ tu'linûn' (6 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '31:23 → 64:4', 'kural': "lemma dizisi — 'alîmun bi-zâti's-sudûr' (5 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '64:1 → 64:4', 'kural': "nakarat3 GEÇMEZ — 'mâ fi's-semâvât'; tesbih eden / bilinen", 'not': 'sûre içi eş.'},
 {'bag': '9:70 → 64:5', 'kural': "lemma dizisi — 'e-lem ye'ti- nebe'u'llezîne' (3 ayet); 3MP ve kavimler adlı / 2MP ve adsız", 'not': 'kalıp eşi.'},
 {'bag': '59:15 → 64:5', 'kural': "lemma dizisi + ölçüm xref — 'zâqû vebâle emrihim ve lehum azâbun elîm'", 'not': 'kalıp eşi.'},
 {'bag': '64:2 → 64:5', 'kural': "sûre içi — kök كفر: 'kâfir' / 'keferû' (كفر [2/6])", 'not': 'sûre içi eş.'},
 {'bag': '40:22 → 64:6', 'kural': "lemma dizisi + ölçüm xref — 'zâlike bi-enne- kânet te'tîhim rusuluhum bi'l-beyyinât' (2 ayet); 'bi-ennehum' / 'bi-ennehû'", 'not': 'kalıp eşi.'},
 {'bag': '9:70 → 64:6', 'kural': "ölçüm xref — 'etethum rusuluhum bi'l-beyyinât'", 'not': 'xref.'},
 {'bag': '54:24 → 64:6', 'kural': "okuma — lemma 'beşer': 'fe-qâlû e-beşeran' / 'fe-qâlû e-beşerun' soruşu", 'not': 'lemma eşi.'},
 {'bag': '14:8 → 64:6', 'kural': "lemma dizisi — 'lafız + ğaniyy + hamîd' (5 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '64:1 → 64:6', 'kural': "sûre içi — kök حمد: 'lehu'l-hamd' / 'hamîd' (حمد [2/2])", 'not': 'sûre içi eş.'},
 {'bag': '64:5 → 64:6', 'kural': "sûre içi — 'zâlike bi-enne' 64:5'in gerekçesi; kök أتي (أتي [2/2])", 'not': 'sûre içi gerekçe.'},
 # blok 7-12
 {'bag': '62:6 → 64:7', 'kural': "okuma — lemma 'zeame': 'in zeamtum' / 'zeame'llezîne keferû'", 'not': 'lemma eşi.'},
 {'bag': '58:7 → 64:7', 'kural': "lemma dizisi — 'summe + nebbe'e + mâ + amile' (2 ayet); etken 3MS / edilgen 2MP", 'not': 'kalıp eşi.'},
 {'bag': '24:64 → 64:7', 'kural': "ölçüm xref — 'nebbe'e + amel + lafız'", 'not': 'xref.'},
 {'bag': '31:23 → 64:7', 'kural': "ölçüm xref — 'nebbe'e + amel + lafız'", 'not': 'xref.'},
 {'bag': '57:22 → 64:7', 'kural': "lemma dizisi — 'zâlike ale'llâhi yesîr' (9 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '64:5 → 64:7', 'kural': "sûre içi — kök نبأ: 'nebe'u' / 'le-tunebbe'unne' (نبأ [2/2])", 'not': 'sûre içi eş.'},
 {'bag': '61:11 → 64:8', 'kural': "lemma dizisi — 'âmene + lafız + rasûl' (17 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '57:10 → 64:8', 'kural': "lemma dizisi — 've'llâhu bimâ ta'melûne habîr' (9 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '64:2 → 64:8', 'kural': "nakarat3 GEÇMEZ — 'lafız bimâ amel': 'basîr' / 'habîr'", 'not': 'sûre içi eş.'},
 {'bag': '9:100 → 64:9', 'kural': "lemma dizisi + ölçüm xref — 'hâlidîne fîhâ ebedâ zâlike'l-fevzu'l-azîm' (2 ayet); 'tecrî tahtehâ' / 'tecrî min tahtihâ'", 'not': 'kalıp eşi.'},
 {'bag': '64:7 → 64:9', 'kural': "okuma — diriltme ve haber verme / toplanma günü ('yevmu't-teğâbun')", 'not': 'sûre içi süreklilik.'},
 {'bag': '57:19 → 64:10', 'kural': "lemma dizisi — 've'llezîne keferû ve kezzebû bi-âyâtinâ ulâ'ike ashâbu-' (7 ayet); 'el-cahîm' / 'en-nâr'", 'not': 'kalıp eşi.'},
 {'bag': '58:8 → 64:10', 'kural': "lemma dizisi — 'bi'se'l-masîr' (11 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '64:9 → 64:10', 'kural': "sûre içi — inanan / inkâr eden, cennet / ateş, kurtuluş / kötü varış; kök خلد [2/2] (aday 1039, kayıt)", 'not': 'sûre içi karşıt.'},
 {'bag': '64:8 → 64:10', 'kural': "sûre içi — kök نور: 'en-nûr' / 'en-nâr' (نور [2/2])", 'not': 'kök iki anlam.'},
 {'bag': '64:3 → 64:10', 'kural': "sûre içi — kök صير: 've ileyhi'l-masîr' / 've bi'se'l-masîr' (صير [2/2])", 'not': 'sûre içi eş.'},
 {'bag': '57:22 → 64:11', 'kural': "okuma — 'mâ esâbe min musîbetin … illâ': 'fî kitâb' / 'bi-izni'llâh'", 'not': 'açılış eşi.'},
 {'bag': '63:3 → 64:11', 'kural': "okuma — lemma 'qalb': mühürlenen kalpler / yol gösterilen kalp", 'not': 'lemma karşıtı.'},
 {'bag': '58:7 → 64:11', 'kural': "lemma dizisi — 'lafız + bi-kulli şey'in alîm' (14 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '24:64 → 64:11', 'kural': "lemma dizisi — 've'llâhu bi-kulli şey'in alîm' (14 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '64:6 → 64:11', 'kural': "sûre içi — kök هدي: beşer öznesi (topluluğun sözü) / Allah öznesi (هدي [2/2]; aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '64:9 → 64:11', 'kural': "nakarat3 GEÇMEZ — 've men yu'min bi'llâh'", 'not': 'sûre içi eş.'},
 {'bag': '64:1 → 64:11', 'kural': "sûre içi — 'kulli şey'' ×2: 'qadîr' / 'alîm' (كلل [2/2], شيأ [2/2])", 'not': 'sûre içi eş.'},
 {'bag': '24:54 → 64:12', 'kural': "lemma dizisi + ölçüm xref — 'atî'u'llâhe ve atî'u'r-rasûl', 'fe-in tevellev fe-innemâ', 'el-belâğu'l-mubîn'; 'er-rasûl' / 'rasûlinâ'", 'not': 'kalıp eşi.'},
 {'bag': '64:6 → 64:12', 'kural': "sûre içi — kök ولي: 'tevellev' (3MP) / 'tevelleytum' (2MP şart) (ولي [2/2])", 'not': 'sûre içi eş.'},

 # blok 13-18
 {'bag': '9:129 → 64:13', 'kural': "lemma dizisi — 'lâ ilâhe illâ huve' (9 ayet); 'tevellev → tevhid → tevekkül' tek ayette / 64:12-13 iki ayette; ardışık değil", 'not': 'kalıp eşi (okuma bağı).'},
 {'bag': '58:10 → 64:13', 'kural': "lemma dizisi — 've ale'llâhi fe'l-yetevekkeli'l-mu'minûn' (7 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '64:12 → 64:13', 'kural': "sûre içi — 'fe-in tevelleytum' şartının ardından tevhid ve tevekkül", 'not': 'sûre içi süreklilik.'},
 {'bag': '63:4 → 64:14', 'kural': "okuma — 'aduvv' + 'ihzer-': münafıklar düşman, 2MS / eşlerin ve çocukların bir kısmı, 2MP; ardışık sûreler (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '63:9 → 64:15', 'kural': "okuma — 'emvâlukum ve evlâdukum': alıkoyan / sınav; ardışık sûreler (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '9:22 → 64:15', 'kural': "lemma dizisi + ölçüm xref — 'lafız + indehû ecrun azîm' (3 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '64:14 → 64:15', 'kural': "sûre içi — kök ولد: düşman olabilen çocuklar / sınav olan çocuklar (ولد [2/2])", 'not': 'sûre içi eş.'},
 {'bag': '64:9 → 64:15', 'kural': "sûre içi — kök عظم: 'el-fevzu'l-azîm' / 'ecrun azîm' (عظم [2/2])", 'not': 'sûre içi eş.'},
 {'bag': '59:9 → 64:16', 'kural': "lemma dizisi + ölçüm xref — 've men yûqa şuhha nefsihî fe-ulâ'ike humu'l-muflihûn' (2 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '64:12 → 64:16', 'kural': "sûre içi — 'atî'û' (طوع [4/4] son)", 'not': 'sûre içi eş.'},
 {'bag': '57:11 → 64:17', 'kural': "lemma dizisi + ölçüm xref — 'yuqridu'llâhe qardan hasenen fe-yudâ'ifehû' (4 ayet): soru / şart; 'ecrun kerîm' / 'yağfir lekum'", 'not': 'kalıp eşi.'},
 {'bag': '57:18 → 64:17', 'kural': "lemma dizisi + ölçüm xref — 'aqradu'llâhe qardan hasenen yudâ'afu' (4 ayet): edilgen / etken", 'not': 'kalıp eşi.'},
 {'bag': '64:16 → 64:17', 'kural': "sûre içi — harcama emri / güzel borcun karşılığı", 'not': 'sûre içi süreklilik.'},
 {'bag': '64:14 → 64:17', 'kural': "sûre içi — kök غفر: 'tağfirû', 'ğafûr' / 'yağfir' (غفر [3/3] son)", 'not': 'sûre içi eş.'},
 {'bag': '62:8 → 64:18', 'kural': "lemma dizisi — 'âlimu'l-ğaybi ve'ş-şehâdeh' (10 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '32:6 → 64:18', 'kural': "esit2 BENZER + ölçüm xref — 'âlimu'l-ğaybi ve'ş-şehâdeti'l-azîzu-': 'er-rahîm' / 'el-hakîm'", 'not': 'kalıp eşi.'},
 {'bag': '62:1 → 64:18', 'kural': "lemma dizisi — 'el-azîzu'l-hakîm' (47 ayet); 62:1 açılış ad dizisinin sonu / 64:18 kapanış; ardışık değil", 'not': 'okuma bağı.'},
 {'bag': '64:1 → 64:18', 'kural': "okuma — ad / sıfatla açılış ('qadîr') ve kapanış ('âlim … azîz hakîm'); halka iddiası yok", 'not': 'sûre sınırları.'},
 {'bag': '64:4 → 64:18', 'kural': "sûre içi — kök علم: 'ya'lemu' ×2, 'alîm' / 'âlim' (علم [5/5] son)", 'not': 'sûre içi eş.'},

]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_tegabun', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in TEGABUN]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_tegabun'] = TEGABUN
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_tegabun', len(TEGABUN), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_tegabun', len(BAGLAR['AS_tegabun']))
