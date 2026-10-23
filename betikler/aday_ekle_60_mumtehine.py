# -*- coding: utf-8 -*-
"""aday_ekle_60_mumtehine.py — sûre 60 (Mümtehine) adayları (AX_mumtehine) ve okuma bağları (AS_mumtehine).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

MUMTEHINE = [
]

BAGLAR = {"AS_mumtehine": [
 # blok 1-3
 {'bag': '59:24 → 60:1', 'kural': "okuma — ardışık sûre sınırı; ad dizisi ve tesbihle kapanış / nidâ ve yasakla açılış; fâsıla م → ل (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '59:18 → 60:1', 'kural': "okuma — 'yâ eyyuhe'llezîne âmenû' nidâsı ardışık sûrelerde", 'not': 'ortak hitap.'},
 {'bag': '9:23 → 60:1', 'kural': "kalıp — 'yâ eyyuhe'llezîne âmenû lâ tettehizû … evliyâ'': babalar ve kardeşler / 'aduvvî ve aduvvekum'", 'not': 'kalıp eşi.'},
 {'bag': '59:8 → 60:1', 'kural': "okuma — lemma 'ahrace': çıkarılan muhâcirler / çıkaranlar dost edinilmez", 'not': 'ardışık sûre bağı.'},
 {'bag': '2:108 → 60:1', 'kural': "kalıp + ölçüm xref — 'fe-qad dalle sevâ'e's-sebîl' (3 ayet); 2:108 henüz okunmadı", 'not': 'kalıp eşi.'},
 {'bag': '60:1 → 60:2', 'kural': "okuma — 'meveddet' / 'veddû lev tekfurûn'; 'aduvv' → 'a'dâ'' (aday 1039, kayıt)", 'not': 'sûre içi karşıt.'},
 {'bag': '47:22 → 60:3', 'kural': "okuma — lemma 'erhâm' akrabalık bağı", 'not': 'lemma eşi.'},
 {'bag': '26:88 → 60:3', 'kural': "okuma — 'lâ yenfe'u … ve lâ': mal ve oğullar / akrabalar ve çocuklar", 'not': 'ortak yapı.'},
 {'bag': '22:17 → 60:3', 'kural': "okuma — lemma 'fasale' + 'beyne' + 'yevme'l-qiyâme'", 'not': 'ortak kalıp.'},
 {'bag': '57:4 → 60:3', 'kural': "kalıp — 've'llâhu bimâ ta'melûne basîr' (6 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '58:22 → 60:3', 'kural': "okuma — akrabalık bağı ve inanç ayrılığı", 'not': 'konu eşi.'},
 # blok 4-7
 {'bag': '33:21 → 60:4', 'kural': "okuma — lemma 'uswe' (3 ayet): 'rasûlu'llâh' / İbrâhîm ve beraberindekiler", 'not': 'lemma eşi.'},
 {'bag': '59:16 → 60:4', 'kural': "okuma — lemma 'berî'': şeytan 1S insandan / İbrâhîm ve beraberindekiler 1P kavimlerinden (aday 1041, kayıt)", 'not': 'aynı yapı iki özne.'},
 {'bag': '40:84 → 60:4', 'kural': "lemma dizisi + ölçüm xref — 'âmene + lafız + vahd' (2 ayet); iman / küfür sırası ters", 'not': 'ortak kalıp.'},
 {'bag': '19:47 → 60:4', 'kural': "okuma — İbrâhîm'in babasına istiğfar vaadi", 'not': 'aynı söz.'},
 {'bag': '9:114 → 60:4', 'kural': "okuma — İbrâhîm'in babasına istiğfarı ve vaadi", 'not': 'aynı söz.'},
 {'bag': '42:10 → 60:4', 'kural': "okuma + ölçüm xref — 'tevekkeltu … unîb' / 'tevekkelnâ … enebnâ' (1S haber / 1P dua)", 'not': 'ortak ikili.'},
 {'bag': '5:14 → 60:4', 'kural': "ölçüm xref — 'el-adâvetu ve'l-bağdâ''; 5:14 henüz okunmadı", 'not': 'xref.'},
 {'bag': '10:85 → 60:5', 'kural': "lemma dizisi + ölçüm xref — 'rabbenâ lâ tec'alnâ fitneh' (2 ayet), ikisinde de tevekkülden sonra", 'not': 'ortak dua.'},
 {'bag': '29:26 → 60:5', 'kural': "ölçüm xref — Rab + 'el-azîzu'l-hakîm' (3MS / 2MS)", 'not': 'ortak kapanış.'},
 {'bag': '60:4 → 60:5', 'kural': "okuma — dua sürüyor ('aleyke tevekkelnâ' → 'rabbenâ lâ tec'alnâ')", 'not': 'sûre içi akış.'},
 {'bag': '60:4 → 60:6', 'kural': "sûre içi — 'uswetun hasenah' açılışının tekrarı", 'not': 'sûre içi eş.'},
 {'bag': '33:21 → 60:6', 'kural': "kalıp + ölçüm xref — 'li-men kâne yercu'llâhe ve'l-yevme'l-âhir' (2 ayet)", 'not': 'ortak kalıp.'},
 {'bag': '57:24 → 60:6', 'kural': "kalıp + ölçüm xref — 've men yetevelle fe-inna'llâhe huve'l-ğaniyyu'l-hamîd' (2 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '57:3 → 60:6', 'kural': "okuma — lemma 'âhir' Allah / gün (aday 1041, kayıt)", 'not': 'aynı kelime iki gönderge.'},
 {'bag': '59:7 → 60:6', 'kural': "okuma — lemma 'ğanî' zenginler / Allah, ardışık sûrelerde (aday 1041, kayıt)", 'not': 'aynı kelime iki gönderge.'},
 {'bag': '60:1 → 60:7', 'kural': "sûre içi — 'meveddet': yasaklanan sevgi / umulan sevgi (aday 1039, kayıt)", 'not': 'sûre içi karşıt.'},
 {'bag': '60:4 → 60:7', 'kural': "okuma — 'el-adâvetu ve'l-bağdâ'u ebeden' / 'meveddeh'", 'not': 'sûre içi karşıt.'},
 {'bag': '57:28 → 60:7', 'kural': "kalıp — 've'llâhu ğafûrun rahîm' (13 ayet)", 'not': 'ortak kapanış.'},
 # blok 8-10
 {'bag': '60:8 → 60:9', 'kural': "nakarat3 GEÇER — 'lâ yenhâkumu'llâh' / 'innemâ yenhâkumu'llâh'; olumsuz / olumlu fiil çifti (aday 1039, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '60:1 → 60:8', 'kural': "sûre içi — lemma 'ahrace' (60:1, 8, 9)", 'not': 'sûre içi eş.'},
 {'bag': '49:9 → 60:8', 'kural': "kalıp + ölçüm xref — 'inna'llâhe yuhibbu'l-muqsitîn' (3 ayet); 'aqsitû' / 'tuqsitû'", 'not': 'ortak kapanış.'},
 {'bag': '59:9 → 60:8', 'kural': "okuma — lemma 'ehabbe' insanlar / Allah (aday 1041, kayıt)", 'not': 'aynı fiil iki özne.'},
 {'bag': '33:26 → 60:9', 'kural': "okuma — lemma 'zâhara' destek anlamında", 'not': 'lemma eşi.'},
 {'bag': '33:4 → 60:9', 'kural': "okuma — lemma 'zâhara' zıhâr / destek (1021 gloss)", 'not': 'anlam ayrımı.'},
 {'bag': '9:13 → 60:9', 'kural': "okuma — lemma 'ihrâc' ('ihrâci'r-rasûl' / 'ihrâcikum')", 'not': 'lemma eşi.'},
 {'bag': '9:23 → 60:9', 'kural': "kalıp — 'men yetevellehum (minkum) fe-ulâ'ike humu'z-zâlimûn'", 'not': 'ortak kapanış.'},
 {'bag': '60:1 → 60:10', 'kural': "nakarat3 GEÇER — 'yâ eyyuhe'llezîne âmenû' (sûre içi 3 ayet)", 'not': 'sûre içi eş.'},
 {'bag': '59:8 → 60:10', 'kural': "okuma — 'el-muhâcirîn' (eril) / 'muhâcirât' (dişil), ardışık sûreler", 'not': 'ardışık sûre bağı.'},
 {'bag': '49:3 → 60:10', 'kural': "okuma — lemma 'imtehane' (2 ayet): Allah sınar / inananlar sınar (aday 1041, kayıt)", 'not': 'aynı fiil iki özne.'},
 {'bag': '59:11 → 60:10', 'kural': "okuma — kök نفق: münafıklık / harcama", 'not': 'kökün iki anlamı.'},
 {'bag': '49:8 → 60:10', 'kural': "kalıp — 've'llâhu alîmun hakîm' (13 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '4:25 → 60:10', 'kural': "lemma dizisi + ölçüm xref — 'allâhu a'lemu bi-îmân'; 4:25 henüz okunmadı", 'not': 'kalıp eşi.'},
 # blok 11-13
 {'bag': '60:10 → 60:11', 'kural': "sûre içi — kök نفق 'enfaqû' (60:10 ×2, 60:11; نفق [4/4] son); gelen / giden eş, aynı ödeme ters yön (aday 1039, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '57:23 → 60:11', 'kural': "okuma — lemma 'fâte' (elden kaçan şey / elden kaçan eş)", 'not': 'lemma eşi.'},
 {'bag': '16:126 → 60:11', 'kural': "okuma — lemma 'âqabe' + 'misl', şart 'in' dizilişi", 'not': 'kalıp eşi.'},
 {'bag': '5:88 → 60:11', 'kural': "lemma dizisi + ölçüm xref — 've'ttequ'llâhe'llezî entum bihî mu'minûn'; 5:88 henüz okunmadı", 'not': 'kalıp eşi.'},
 {'bag': '60:10 → 60:12', 'kural': "sûre içi — lemma dizisi 'izâ + câ'e + mu'mine' (nakarat3 GEÇMEZ)", 'not': 'sûre içi eş.'},
 {'bag': '60:7 → 60:12', 'kural': "sûre içi — 'lafız + ğafûr + rahîm' (nakarat3 GEÇMEZ)", 'not': 'sûre içi eş.'},
 {'bag': '48:10 → 60:12', 'kural': "okuma — lemma 'bâye'a' (3MP / 3FP biat)", 'not': 'lemma eşi.'},
 {'bag': '17:31 → 60:12', 'kural': "lemma dizisi — 'qatele + veled' (2MP / 3FP)", 'not': 'yasak eşi.'},
 {'bag': '24:62 → 60:12', 'kural': "lemma dizisi — 'istağfere + lehum + lafız' + 'inna'llâhe ğafûrun rahîm'", 'not': 'ortak kapanış.'},
 {'bag': '60:1 → 60:13', 'kural': "nakarat3 GEÇER — 'yâ eyyuhe'llezîne âmenû lâ' (sûre içi 2 ayet; sûre başı / sonu dost edinme yasağı)", 'not': 'sûre halkası (okuma).'},
 {'bag': '60:9 → 60:13', 'kural': "sûre içi — kök ولي 'tevellâ' (ولي [5/5] son)", 'not': 'sûre içi eş.'},
 {'bag': '58:14 → 60:13', 'kural': "lemma dizisi + ölçüm xref — 'tevellâ + qavm + ğadibe + lafız' (anlatım / yasak)", 'not': 'ardışık sûre bağı.'},
 {'bag': '12:87 → 60:13', 'kural': "okuma — lemma 'ye'ise' ve inkârcılar", 'not': 'lemma eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_mumtehine', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in MUMTEHINE]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_mumtehine'] = MUMTEHINE
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_mumtehine', len(MUMTEHINE), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_mumtehine', len(BAGLAR['AS_mumtehine']))
