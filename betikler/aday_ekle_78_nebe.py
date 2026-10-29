# -*- coding: utf-8 -*-
"""aday_ekle_78_nebe.py — sûre 78 (Nebe') adayları (AX_nebe) ve okuma bağları (AS_nebe).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

NEBE = [
]

BAGLAR = {"AS_nebe": [
 # blok 1-10
 {'bag': '77:50 → 78:1', 'kural': "okuma — ardışık sûre sınırı: soruyla kapanış ('fe-bi-eyyi hadîsin') / soruyla açılış (''amme yetesâ'elûn'); 3MP → 3MP; fâsıla ن → ن; 'hadîs' / 'nebe'' (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '77:25 → 78:6', 'kural': "okuma — ardışık sûrede 'e-lem nec'ali'l-arda' + nekre işlev: 'kifâtâ' / 'mihâdâ' (aday 1040 ailesi, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '74:40 → 78:1', 'kural': "okuma — lemma 'yetesâ'elu': cennettekiler soruşuyor / soruşanlar adsız, konu soruluyor", 'not': 'lemma eşi.'},
 {'bag': '38:67 → 78:2', 'kural': "okuma — lemma dizisi 'nebe' + 'azîm' korpusun iki ayeti: 'qul huve' ile nekre / soru-cevapta tarifli", 'not': 'lemma eşi.'},
 {'bag': '51:8 → 78:3', 'kural': "okuma — lemma 'muxtelif': 2MP, ayrılıkta söz / 3MP, haber hakkında ayrılık", 'not': 'lemma eşi.'},
 {'bag': '78:4 → 78:5', 'kural': "sûre içi — 'kellâ se-ya'lemûn' korpusun iki ayeti, 'thumme' ile tekrar; kök علم sûre içi iki geçiş", 'not': 'sûre içi eş.'},
 {'bag': '38:12 → 78:7', 'kural': "okuma — lemma 'evtâd': Fir'avn'ın sıfatı / dağlar", 'not': 'lemma eşi.'},
 {'bag': '25:47 → 78:9', 'kural': "okuma — lemma dizisi 'nevm + subât' korpusun iki ayeti: 3MS 'huve'llezî' / 1P", 'not': 'lemma eşi.'},
 {'bag': '25:47 → 78:10', 'kural': "ölçüm xref + lemma dizisi 'leyl + libâs' korpusun iki ayeti; sıra gece → uyku (25:47) / uyku → gece (78:9-10)", 'not': 'xref.'},
 {'bag': '17:12 → 78:10', 'kural': "okuma — 've ce'alne'l-leyl' korpusun iki ayeti: gece ve gündüz iki ayet / gece örtü", 'not': 'kalıp eşi.'},
 # blok 11-20
 {'bag': '78:10 → 78:11', 'kural': "sûre içi — 've ce'alnâ' + zaman adı + nekre işlev: gece / gündüz, örtü / geçim (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '23:17 → 78:12', 'kural': "okuma — lemma dizisi 'fevq + seb'' korpusun iki ayeti: 'xalaqnâ … seb'a tarâ'iq' (adlı) / 'beneynâ … seb'an şidâdâ' (adsız)", 'not': 'lemma eşi.'},
 {'bag': '12:48 → 78:12', 'kural': "okuma — lemma dizisi 'seb' + şedîd' korpusun iki ayeti; ikisinde de basılan ayette sayılan adsız", 'not': 'lemma eşi.'},
 {'bag': '71:16 → 78:13', 'kural': "okuma — lemma 'sirâc': güneşin yüklemi / adsız, sıfatlı", 'not': 'lemma eşi.'},
 {'bag': '50:9 → 78:15', 'kural': "okuma — su → 'bihî' → bitki zinciri: gökten, 'fe' ile / 'el-mu'sırât'tan, ta'lîl lâmıyla; ikisi de L2 olgu=True", 'not': 'kurgu eşi.'},
 {'bag': '44:40 → 78:17', 'kural': "okuma — 'inne yevme'l-fasl' korpusun iki ayeti: 'mîqâtuhum ecma'în' / 'kâne mîqâtâ'", 'not': 'kalıp eşi.'},
 {'bag': '37:21 → 78:17', 'kural': "ölçüm xref — 'yevmu'l-fasl': işaret + yalanlama / tekit + 'kâne mîqâtâ'", 'not': 'xref.'},
 {'bag': '77:38 → 78:17', 'kural': "okuma — ardışık sûrede 'yevmu'l-fasl' (77:13, 14, 38 / 78:17) (aday 1040 ailesi, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '20:102 → 78:18', 'kural': "okuma — 'yevme yunfaxu fi's-sûr': 1P 'nahşuru', suçlular / 2MP 'te'tûne', bölükler", 'not': 'kalıp eşi.'},
 {'bag': '77:9 → 78:19', 'kural': "okuma — ardışık sûrede gök edilgenle: 'furicet' (izâ şartı) / 'futihat … ebvâbâ' (aday 1040 ailesi, kayıt)", 'not': 'kurgu eşi.'},
 {'bag': '77:10 → 78:20', 'kural': "okuma — ardışık sûrede dağlar edilgenle: 'nusifet' / 'suyyirat … serâbâ' (aday 1040 ailesi, kayıt)", 'not': 'kurgu eşi.'},
 {'bag': '18:47 → 78:20', 'kural': "okuma — lemma dizisi 'suyyirat + cebel' korpusun iki ayeti: 1P etken / edilgen", 'not': 'lemma eşi.'},
 {'bag': '24:39 → 78:20', 'kural': "okuma — lemma 'serâb' korpusun iki ayeti: amellerin benzetmesi / dağların varacağı durum", 'not': 'lemma eşi.'},
 {'bag': '78:7 → 78:20', 'kural': "sûre içi — kök جبل iki geçiş: 'evtâd' (kazık) / 'serâb' (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 # blok 21-30
 {'bag': '78:17 → 78:21', 'kural': "sûre içi — 'inne' + ad + 'kâne / kânet' + nekre: 'yevme'l-fasli … mîqâtâ' / 'cehenneme … mirsâdâ'", 'not': 'sûre içi eş.'},
 {'bag': '38:55 → 78:22', 'kural': "okuma — 'li't-tâğîn' korpusun iki ayeti, ikisinde de 'me'âb': 'le-şerra me'âb' / nitelemesiz", 'not': 'kalıp eşi.'},
 {'bag': '44:56 → 78:24', 'kural': "okuma — 'lâ yezûqûne fîhâ … illâ': ölüm / serinlik ve içecek; istisna aynı ayette / sonraki ayette", 'not': 'kurgu eşi.'},
 {'bag': '21:69 → 78:24', 'kural': "okuma — lemma 'berd' korpusun iki ayeti: ateş serinlik olur / serinlik tadılmaz", 'not': 'lemma eşi.'},
 {'bag': '38:57 → 78:25', 'kural': "okuma — lemma dizisi 'hamîm + ğassâq' korpusun iki ayeti, ikisi de ذوق ile: emir / olumsuz + istisna", 'not': 'lemma eşi.'},
 {'bag': '78:24 → 78:25', 'kural': "sûre içi — 'berd' / 'hamîm' (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '22:57 → 78:28', 'kural': "okuma — 've kezzebû bi-âyâtinâ' (22:57, 30:16 'keferû' ile, 'fe-ulâ'ike' sonucuyla) / mef'ûl mutlakla", 'not': 'kalıp eşi.'},
 {'bag': '36:12 → 78:29', 'kural': "ölçüm xref — 've kulle şey'in ahsaynâh' korpusun iki ayeti: 'fî imâmin mubîn' / 'kitâbâ'", 'not': 'xref.'},
 {'bag': '72:28 → 78:29', 'kural': "okuma — 'ahsâ + kulle şey'': 3MS, ''adedâ' / 1P, 'kitâbâ'", 'not': 'kalıp eşi.'},
 {'bag': '78:24 → 78:30', 'kural': "sûre içi — kök ذوق iki geçiş: 'lâ yezûqûne' 3MP / 'fe-zûqû' 2MP (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 # blok 31-40
 {'bag': '78:22 → 78:31', 'kural': "sûre içi — 'li't-tâğîne me'âbâ' / 'li'l-muttaqîne mefâzâ' (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '68:34 → 78:31', 'kural': "okuma — 'inne li'l-muttaqîn' korpusun iki ayeti: 'inde rabbihim cennâti'n-na'îm' / 'mefâzâ'", 'not': 'kalıp eşi.'},
 {'bag': '56:37 → 78:33', 'kural': "okuma — lemma 'etrâb' (38:52, 56:37, 78:33): üçünde de dişil çoğulun sıfatı", 'not': 'lemma eşi.'},
 {'bag': '78:33 → 78:40', 'kural': "sûre içi — kök ترب iki anlam: 'etrâb' (yaşıt) / 'turâb' (toprak) (1021)", 'not': 'sûre içi eş.'},
 {'bag': '56:25 → 78:35', 'kural': "okuma — 'lâ yesme'ûne fîhâ lağven ve lâ': 'te'thîmâ' / 'kizzâbâ' (19:62 'illâ selâmâ' ile)", 'not': 'kalıp eşi.'},
 {'bag': '78:24 → 78:35', 'kural': "sûre içi — 'lâ + IMPF 3MP + fîhâ + nekre + ve lâ + nekre': azgınlar / sakınanlar (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '78:28 → 78:35', 'kural': "sûre içi — lemma 'kizzâb' korpusun iki ayeti: yalanlamaları / yalan işitmemeleri (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '78:26 → 78:36', 'kural': "sûre içi — kök جزي iki geçiş: 'cezâ'en vifâqâ' / 'cezâ'en min rabbike' (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '78:27 → 78:36', 'kural': "sûre içi — kök حسب iki anlam: hesap / yeterli (1021)", 'not': 'sûre içi eş.'},
 {'bag': '44:7 → 78:37', 'kural': "okuma — 'rabbi's-semâvâti ve'l-ardi ve mâ beynehumâ' (37:5, 44:7 ve okunmuş 1 ayet): 'er-rahmân' ile devam yalnız burada", 'not': 'kalıp eşi.'},
 {'bag': '70:4 → 78:38', 'kural': "okuma — melekler ve rûh birlikte: yükseliş, melekler önce / saf saf durma, rûh önce", 'not': 'kurgu eşi.'},
 {'bag': '20:109 → 78:38', 'kural': "okuma — 'illâ men ezine lehu'r-rahmânu ve' + söz: şefaat, 'radıye lehû qavlâ' / konuşma, 'qâle sevâbâ'", 'not': 'lemma eşi.'},
 {'bag': '76:29 → 78:39', 'kural': "okuma — 'fe-men şâ'e'ttexaze ilâ rabbihî' (73:19, 76:29 'sebîlâ' / 'me'âbâ')", 'not': 'kalıp eşi.'},
 {'bag': '78:22 → 78:39', 'kural': "sûre içi — kök أوب iki geçiş: azgınların varış yeri / Rabbe dönüş (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '28:47 → 78:40', 'kural': "ölçüm xref — 'qaddemet' + el + söz: çoğul, dua / tekil, dilek", 'not': 'xref.'},
 {'bag': '69:25 → 78:40', 'kural': "okuma — 'yeqûlu yâ leytenî': 'lem ûte kitâbiyeh' / 'kuntu turâbâ'", 'not': 'kalıp eşi.'},
 {'bag': '78:1 → 78:40', 'kural': "sûre içi — sûre soruyla açılıp ('amme yetesâ'elûn') 'kâfir'in dileğiyle kapanıyor", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_nebe', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in NEBE]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_nebe'] = NEBE
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_nebe', len(NEBE), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_nebe', len(BAGLAR['AS_nebe']))
