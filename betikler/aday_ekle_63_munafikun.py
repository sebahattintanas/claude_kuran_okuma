# -*- coding: utf-8 -*-
"""aday_ekle_63_munafikun.py — sûre 63 (Münâfikûn) adayları (AX_munafikun) ve okuma bağları (AS_munafikun).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

MUNAFIKUN = [
]

BAGLAR = {"AS_munafikun": [
 # blok 1-5
 {'bag': '62:11 → 63:1', 'kural': "okuma — ardışık sûre sınırı; 2MS'i bırakıp gidenler / 2MS'e gelen münafıklar; fâsıla ن → ن (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '9:67 → 63:1', 'kural': "okuma — lemma 'munâfiq': 'humu'l-fâsiqûn' / 'le-kâzibûn'", 'not': 'lemma eşi.'},
 {'bag': '49:7 → 63:1', 'kural': "ölçüm xref — 'alime + rasûl + lafız'", 'not': 'xref.'},
 {'bag': '61:5 → 63:1', 'kural': "ölçüm xref — 'alime + rasûl + lafız' (Mûsâ'nın elçiliği / 2MS'in elçiliği)", 'not': 'xref.'},
 {'bag': '58:16 → 63:2', 'kural': "lemma dizisi + ölçüm xref — 'ittehazû eymânehum cunneten fe-saddû an sebîli'llâh' (2 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '58:15 → 63:2', 'kural': "kalıp + ölçüm xref — 'innehum sâ'e mâ kânû ya'melûn' (3 ayet); 58:15-16 iki ayet / 63:2 tek ayet", 'not': 'kalıp eşi.'},
 {'bag': '9:9 → 63:2', 'kural': "kalıp + ölçüm xref — 'fe-saddû an sebîlih' + 'innehum sâ'e mâ kânû ya'melûn'", 'not': 'kalıp eşi.'},
 {'bag': '9:87 → 63:3', 'kural': "lemma dizisi + ölçüm xref — 'tubi'a alâ qulûbihim fe-hum lâ yefqahûn' (2 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '9:85 → 63:4', 'kural': "okuma — lemma 'a'cebe' 2MS: mal ve çocuklar / gövdeler", 'not': 'lemma eşi.'},
 {'bag': '48:29 → 63:4', 'kural': "okuma — lemma 'a'cebe': ekin ekicileri hoşnut eder / gövdeler 2MS'in hoşuna gider", 'not': 'lemma eşi.'},
 {'bag': '9:30 → 63:4', 'kural': "kalıp + ölçüm xref — 'qâtelehumu'llâhu ennâ yu'fekûn' (2 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '33:28 → 63:5', 'kural': "okuma — lemma 'te'âle' (gelin)", 'not': 'lemma eşi.'},
 {'bag': '16:23 → 63:5', 'kural': "okuma — lemma 'mustekbir'", 'not': 'lemma eşi.'},
 {'bag': '63:2 → 63:5', 'kural': "sûre içi — kök صدد: 'fe-saddû' / 'yesuddûn' (صدد [2/2])", 'not': 'sûre içi eş.'},
 {'bag': '63:4 → 63:5', 'kural': "sûre içi — 2MS 'ra'eytehum' ×2: gövdelerini gören / yüz çevirdiklerini gören", 'not': 'sûre içi eş.'},
 # blok 6-11
 {'bag': '9:80 → 63:6', 'kural': "lemma dizisi — 'len yağfira'llâhu lehum' (3 ayet) + 'lâ yehdi'l-qavme'l-fâsiqîn'; emir ve sayı / eşitlik", 'not': 'kalıp eşi.'},
 {'bag': '47:34 → 63:6', 'kural': "lemma dizisi — 'fe-len yağfira'llâhu lehum' (3 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '61:5 → 63:6', 'kural': "lemma dizisi — 'lafız + lâ yehdî + qavm + fâsiq' (5 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '63:5 → 63:6', 'kural': "sûre içi — kök غفر: 'yestağfir lekum' çağrısı / 'estağferte em lem testağfir' (غفر [4/4] son)", 'not': 'sûre içi eş.'},
 {'bag': '49:3 → 63:7', 'kural': "ölçüm xref — 'inde rasûli'llâh'", 'not': 'xref.'},
 {'bag': '62:11 → 63:7', 'kural': "okuma — lemma 'infadda': ticarete dağılanlar / dağılması istenenler; ardışık sûreler (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '15:21 → 63:7', 'kural': "okuma — lemma 'hazâ'in': her şeyin hazineleri / göklerin ve yerin hazineleri", 'not': 'lemma eşi.'},
 {'bag': '63:7 → 63:8', 'kural': "nakarat3 GEÇMEZ — 've lâkinne'l-munâfiqîne lâ yefqahûn / lâ ya'lemûn'", 'not': 'sûre içi eş.'},
 {'bag': '11:92 → 63:8', 'kural': "okuma — lemma 'e'azz': topluluğun güçlü sayılması", 'not': 'lemma eşi.'},
 {'bag': '10:65 → 63:8', 'kural': "okuma — lemma 'izze' li'llâh: yalnız Allah / Allah, elçi ve inananlar", 'not': 'lemma eşi.'},
 {'bag': '9:85 → 63:9', 'kural': "okuma — 'emvâl ve evlâd' ikilisi", 'not': 'ikili eşi.'},
 {'bag': '57:20 → 63:9', 'kural': "okuma — 'emvâl ve evlâd' ve 'lehv'", 'not': 'konu eşi.'},
 {'bag': '62:9 → 63:9', 'kural': "okuma — 'zikri'llâh' ve 'yâ eyyuhe'llezîne âmenû': alışveriş / mal ve çocuklar; ardışık sûreler (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '9:69 → 63:9', 'kural': "lemma dizisi — 'ulâ'ike humu'l-hâsirûn' (8 ayet), mal ve çocuklarla", 'not': 'ortak kapanış.'},
 {'bag': '63:7 → 63:10', 'kural': "sûre içi — kök نفق: 'lâ tunfiqû' (münafıklar) / 'enfiqû' (inananlara); نفق [6/6] son (aday 1039, kayıt)", 'not': 'sûre içi karşıt.'},
 {'bag': '62:11 → 63:10', 'kural': "okuma — rızık: 'hayru'r-râziqîn' / 'razaqnâkum'; ardışık sûreler (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '23:99 → 63:10', 'kural': "lemma dizisi — 'ehad + mevt + qâle' (3 ayet): 'rabbi'rci'ûn' / 'rabbi lev lâ ahhartenî'", 'not': 'kalıp eşi.'},
 {'bag': '14:44 → 63:10', 'kural': "lemma dizisi — 'ehhara + ilâ + ecel + qarîb' (3 ayet): 1P azap günü / 1S ölüm", 'not': 'kalıp eşi.'},
 {'bag': '9:75 → 63:10', 'kural': "lemma dizisi + ölçüm xref — 'tesaddaqa + kâne + min + sâlih' (2 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '63:10 → 63:11', 'kural': "sûre içi — kök أخر, أجل: erteleme dileği / ertelenmeme (aday 1039, kayıt)", 'not': 'sûre içi cevap.'},
 {'bag': '16:61 → 63:11', 'kural': "lemma dizisi — 'izâ câ'e ecel' (5 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '9:16 → 63:11', 'kural': "kalıp — 've'llâhu habîrun bimâ ta'melûn' (4 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '63:1 → 63:11', 'kural': "okuma — 'izâ câ'e' ile açılış (münafıklar) ve kapanış (ecel); halka iddiası yok", 'not': 'sûre sınırları.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_munafikun', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in MUNAFIKUN]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_munafikun'] = MUNAFIKUN
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_munafikun', len(MUNAFIKUN), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_munafikun', len(BAGLAR['AS_munafikun']))
