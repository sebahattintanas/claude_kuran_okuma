# -*- coding: utf-8 -*-
"""aday_ekle_61_saff.py — sûre 61 (Saff) adayları (AX_saff) ve okuma bağları (AS_saff).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

SAFF = [
]

BAGLAR = {"AS_saff": [
 # blok 1-7
 {'bag': '60:13 → 61:1', 'kural': "okuma — ardışık sûre sınırı; nidâ ve dost edinme yasağıyla kapanış / tesbihle açılış; fâsıla ر → م (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '59:1 → 61:1', 'kural': "lemma dizisi + esit2 TAM — 'sebbaha li'llâhi mâ fi's-semâvâti ve mâ fi'l-ard … ve huve'l-azîzu'l-hakîm' (2 ayet)", 'not': 'aynı açılış.'},
 {'bag': '57:1 → 61:1', 'kural': "esit2 BENZER — 've'l-ard' / 've mâ fi'l-ard'", 'not': 'açılış eşi.'},
 {'bag': '26:226 → 61:2', 'kural': "lemma dizisi — 'qâle + mâ + lâ + fe'ale' (3 ayet): 3MP haber / 2MP sitem", 'not': 'kalıp eşi.'},
 {'bag': '61:2 → 61:3', 'kural': "nakarat3 GEÇER — 'teqûlûne mâ lâ tef'alûn'; soru → hüküm", 'not': 'sûre içi eş.'},
 {'bag': '40:35 → 61:3', 'kural': "kalıp + ölçüm xref — 'kebura maqten inde'llâh' (2 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '61:2 → 61:4', 'kural': "okuma — söyleyip yapmayanlar / kenetlenmiş safla savaşanlar (aday 1039, kayıt)", 'not': 'sûre içi karşıt.'},
 {'bag': '9:111 → 61:4', 'kural': "lemma dizisi — 'qâtele + fî + sebîl' (12 ayet)", 'not': 'lemma eşi.'},
 {'bag': '9:109 → 61:4', 'kural': "okuma — lemma 'bunyân': takvâ / yar kenarı üzerine yapı; kenetlenmiş saf yapıya benzetiliyor", 'not': 'lemma eşi.'},
 {'bag': '14:6 → 61:5', 'kural': "lemma dizisi — 'iz + qâle + mûsâ + qavm' (5 ayet): nimet hatırlatma / sitem", 'not': 'kalıp eşi.'},
 {'bag': '33:69 → 61:5', 'kural': "okuma — lemma 'âzâ', Mûsâ'ya eziyet (inananlara uyarı / Mûsâ'nın sözü)", 'not': 'aynı olay.'},
 {'bag': '9:117 → 61:5', 'kural': "okuma — lemma 'zâğa' + kalpler", 'not': 'lemma eşi.'},
 {'bag': '9:24 → 61:5', 'kural': "kalıp — 've'llâhu lâ yehdi'l-qavme'l-fâsiqîn' (4 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '61:5 → 61:6', 'kural': "nakarat3 GEÇER + okuma — 've iz qâle … yâ …' koşut kuruluş; 'rasûlu'llâhi ileykum' ('ennî' / 'innî')", 'not': 'sûre içi koşut.'},
 {'bag': '61:5 → 61:7', 'kural': "nakarat3 GEÇER — 'lafız + lâ yehdî + qavm': fâsıqîn / zâlimîn", 'not': 'sûre içi eş.'},
 {'bag': '9:111 → 61:6', 'kural': "okuma — Tevrât adı", 'not': 'ad eşi.'},
 {'bag': '43:63 → 61:6', 'kural': "ölçüm xref — 'câ'e + beyyine + qâle'; 43:63'te fail Îsâ adıyla", 'not': 'kalıp eşi.'},
 {'bag': '28:36 → 61:6', 'kural': "ölçüm xref — 'beyyine + qâle + sihr': Mûsâ'nın kanıtlarına 'sihrun mufterâ' / 'sihrun mubîn'", 'not': 'kalıp eşi.'},
 {'bag': '27:13 → 61:6', 'kural': "kalıp — 'hâzâ sihrun mubîn' (3 ayet), 'lemmâ câ'e' ile", 'not': 'ortak söz.'},
 {'bag': '46:7 → 61:6', 'kural': "kalıp — 'hâzâ sihrun mubîn' (3 ayet), 'lemmâ câ'e' ile", 'not': 'ortak söz.'},
 {'bag': '61:4 → 61:6', 'kural': "okuma — kök بني 'bunyân' / 'ibn', 'benî' (kökün iki anlamı)", 'not': 'sûre içi kök.'},
 {'bag': '11:18 → 61:7', 'kural': "lemma dizisi — 'men azlemu mimmeni'fterâ ale'llâhi kezib' (9 ayet); nekre / marife", 'not': 'kalıp eşi.'},
 {'bag': '49:17 → 61:7', 'kural': "okuma — lemma 'islâm'", 'not': 'lemma eşi.'},
 {'bag': '9:109 → 61:7', 'kural': "kalıp — 've'llâhu lâ yehdi'l-qavme'z-zâlimîn' (6 ayet); 9:109 'bunyân'ı da taşıyor (61:4)", 'not': 'ortak kapanış.'},
 # blok 8-14
 {'bag': '9:32 → 61:8', 'kural': "esit2 BENZER + ölçüm xref — nuru ağızla söndürme; 'en yutfi'û … ye'ba'llâhu illâ en yutimme' / 'li-yutfi'û … ve'llâhu mutimmu'", 'not': 'kalıp eşi.'},
 {'bag': '9:33 → 61:9', 'kural': "esit2 YAKIN — 'huve'llezî ersele rasûlehû … ve lev kerihe'l-muşrikûn' (lemma dizisi 2 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '48:28 → 61:9', 'kural': "kalıp — 'huve'llezî ersele rasûlehû … ale'd-dîni kullih' (3 ayet); kapanış 've kefâ bi'llâhi şehîdâ'", 'not': 'kalıp eşi.'},
 {'bag': '9:32-33 → 61:8-9', 'kural': "okuma — aynı sırayla iki ayet (nur söndürme / elçiyi gönderme); ardışık sûre değil, 1040 alanı değil", 'not': 'sıralı eşleşme.'},
 {'bag': '61:8 → 61:9', 'kural': "okuma — 've lev kerihe': el-kâfirûn / el-muşrikûn", 'not': 'sûre içi eş.'},
 {'bag': '61:2 → 61:10', 'kural': "nakarat3 GEÇER — 'yâ eyyuhe'llezîne âmenû' (sûre içi 3 ayet)", 'not': 'sûre içi eş.'},
 {'bag': '9:24 → 61:10', 'kural': "okuma — lemma 'ticâret': Allah'tan sevgili tutulan / azaptan kurtaran", 'not': 'lemma eşi.'},
 {'bag': '9:111 → 61:10', 'kural': "okuma — alım satım dili (mal ve can karşılığı)", 'not': 'konu eşi.'},
 {'bag': '9:20 → 61:11', 'kural': "lemma dizisi + ölçüm xref — 'câhede fî sebîli'llâhi bi-emvâl ve enfus' (2 ayet; 3MP PERF / 2MP IMPF)", 'not': 'kalıp eşi.'},
 {'bag': '61:10 → 61:11', 'kural': "okuma — sorunun cevabı, ticaretin tarifi", 'not': 'sûre içi akış.'},
 {'bag': '61:11 → 61:12', 'kural': "okuma — haber kipinde emir / cezmli cevap 'yağfir'", 'not': 'sûre içi akış.'},
 {'bag': '33:71 → 61:12', 'kural': "lemma dizisi — 'yağfir lekum zunûbekum' (6 ayet), cezmli cevap", 'not': 'kalıp eşi.'},
 {'bag': '58:22 → 61:12', 'kural': "lemma dizisi — 'yudhil + cennât + tecrî min tahtihe'l-enhâr' (11 ayet)", 'not': 'ortak kalıp.'},
 {'bag': '9:72 → 61:12', 'kural': "lemma dizisi + ölçüm xref — 'mesâkine tayyibeten fî cennâti adn' (2 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '61:10 → 61:12', 'kural': "okuma — 'ticâret' → 'el-fevzu'l-azîm'; 'azâbun elîm' / 'cennât' (aday 1039, kayıt)", 'not': 'sûre içi karşıt.'},
 {'bag': '61:4 → 61:13', 'kural': "sûre içi — kök حبب: Allah sever / siz seversiniz (aday 1041, kayıt)", 'not': 'aynı fiil iki özne.'},
 {'bag': '48:18 → 61:13', 'kural': "okuma — 'fethun qarîb': verilen ödül / vaat", 'not': 'ortak söz.'},
 {'bag': '10:87 → 61:13', 'kural': "kalıp — 've beşşiri'l-mu'minîn' (5 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '61:6 → 61:13', 'kural': "sûre içi — kök بشر: 'mubeşşiran' (Îsâ) / 'beşşir' (2MS)", 'not': 'sûre içi eş.'},
 {'bag': '61:6 → 61:14', 'kural': "nakarat3 GEÇER — 'qâle îsa'bnu meryem'; 'benî isrâ'îl' sûre içi eş", 'not': 'sûre içi eş.'},
 {'bag': '61:13 → 61:14', 'kural': "sûre içi — kök نصر: 'nasrun mina'llâh' / 'ensâru'llâh' (aday 1041, kayıt)", 'not': 'aynı kök iki gönderge.'},
 {'bag': '61:9 → 61:14', 'kural': "sûre içi — kök ظهر: 'li-yuzhirahû' (Allah) / 'zâhirîn' (inananlar) (aday 1041, kayıt)", 'not': 'aynı kök iki özne.'},
 {'bag': '57:3 → 61:14', 'kural': "okuma — lemma 'zâhir': Allah adı / inananlar (aday 1041, kayıt)", 'not': 'aynı kelime iki gönderge.'},
 {'bag': '40:29 → 61:14', 'kural': "okuma — lemma 'zâhir': kavmin üstünlüğü / inananların üstünlüğü", 'not': 'lemma eşi.'},
 {'bag': '58:22 → 61:14', 'kural': "okuma — lemma 'eyyede': inananların desteklenmesi", 'not': 'lemma eşi.'},
 {'bag': '61:1 → 61:14', 'kural': "okuma — sûre başı tesbih / sûre sonu inananların üstünlüğü; halka iddiası yok", 'not': 'sûre sınırları.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_saff', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in SAFF]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_saff'] = SAFF
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_saff', len(SAFF), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_saff', len(BAGLAR['AS_saff']))
