# -*- coding: utf-8 -*-
"""aday_ekle_92_leyl.py — sûre 92 (Leyl) adayları (AX_leyl) ve okuma bağları (AS_leyl).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

LEYL = [
]

BAGLAR = {"AS_leyl": [
 # blok 1-11
 {'bag': '91:15 → 92:1', 'kural': "okuma — ardışık sûre sınırı: öznesi açık olmayan 'korkmaz' ile kapanış / geceye yemin ile açılış; fâsıla ا → ى (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '91:4 → 92:1', 'kural': "okuma — ardışık sûrede aynı lemma dizisi 'leyl' + 'izâ' + 'ğaşiye': 3FS nesneli / nesnesiz (aday 1040, okuma bağı)", 'not': 'lemma dizisi eşi.'},
 {'bag': '91:3 → 92:2', 'kural': "okuma — harekesiz 've'n-nehâri izâ' + kök جلو: II. bab nesneli 'cellâhâ' / V. bab nesnesiz 'tecellâ' (aday 1040, okuma bağı)", 'not': 'kalıp eşi.'},
 {'bag': '92:1 → 92:2', 'kural': "sûre içi — gece / gündüz; bürüme / açığa çıkma (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '10:6 → 92:3', 'kural': "okuma — harekesiz 've mâ xalaqa': özne lafız, yer gökler ve yer / özne yazılmamış, nesne erkek ve dişi", 'not': 'kalıp eşi.'},
 {'bag': '49:13 → 92:3', 'kural': "ölçüm xref — 'xalaqa' + 'zeker' + 'unthâ': 1P + 2MP nesne, nekre / 3MS 'mâ' + belirli nesne", 'not': 'xref eşi.'},
 {'bag': '76:22 → 92:4', 'kural': "okuma — lemma 'sa'y' + 2MP: çabanız şükranla karşılanmış / çabanız türlü türlü", 'not': 'lemma eşi.'},
 {'bag': '53:40 → 92:4', 'kural': "okuma — lemma 'sa'y': 3MS çabası görülecek / 2MP çaba türlü türlü", 'not': 'lemma eşi.'},
 {'bag': '20:53 → 92:4', 'kural': "okuma — lemma 'şettâ': türlü türlü bitkiler / türlü türlü çaba", 'not': 'lemma eşi.'},
 {'bag': '79:37 → 92:5', 'kural': "okuma — harekesiz 'fe-emmâ men' + PERF: azan / veren ve sakınan", 'not': 'kalıp eşi.'},
 {'bag': '53:34 → 92:5', 'kural': "okuma — lemma 'a'tâ': az verip kesen / nesnesiz verip sakınan", 'not': 'lemma eşi.'},
 {'bag': '87:8 → 92:7', 'kural': "okuma — lemma dizisi 'yessara' + 'yusrâ': 2MS nesne / 3MS nesne + 'se'", 'not': 'lemma dizisi eşi.'},
 {'bag': '79:40 → 92:8', 'kural': "okuma — harekesiz 've emmâ men' + PERF: Rabbinin makamından korkan / cimrilik eden", 'not': 'kalıp eşi.'},
 {'bag': '80:8 → 92:8', 'kural': "okuma — harekesiz 've emmâ men' + PERF: koşarak gelen / cimrilik eden", 'not': 'kalıp eşi.'},
 {'bag': '80:5 → 92:8', 'kural': "okuma — 'emmâ' + 'men' + lemma 'istağnâ': tek başına / 'bexile'ye atıflı", 'not': 'lemma eşi.'},
 {'bag': '57:24 → 92:8', 'kural': "okuma — kök بخل insan + kök غني lafız ('el-ğaniyy') / ikisi de insan (aday 1041, sûreler arası okuma notu)", 'not': 'kök eşi.'},
 {'bag': '47:38 → 92:8', 'kural': "okuma — kök بخل insan + kök غني lafız ('el-ğaniyy') / ikisi de insan (aday 1041, sûreler arası okuma notu)", 'not': 'kök eşi.'},
 {'bag': '92:5 → 92:8', 'kural': "sûre içi — 'emmâ' + 'men' + iki PERF aynı iskelet: verdi / cimrilik etti (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '92:6 → 92:9', 'kural': "sûre içi — PERF + 'bi'l-husnâ' aynı iskelet: doğruladı / yalanladı (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '92:7 → 92:10', 'kural': "sûre içi — 'fe-se-nuyessiruhû li-' aynı iskelet: en kolay / en zor (aday 1039, okuma); kök يسر [3/3]", 'not': 'sûre içi eş.'},
 {'bag': '74:9 → 92:10', 'kural': "okuma — kök عسر: çetin gün / en zor olan", 'not': 'kök eşi.'},
 {'bag': '69:28 → 92:11', 'kural': "okuma — lemma 'ağnâ' + 'mâl': PERF 1S kendi sözü / IMPF 3MS anlatı", 'not': 'lemma eşi.'},
 {'bag': '92:8 → 92:11', 'kural': "sûre içi — kök غني [2/2]: kendini yeterli gördü / malı yetmez", 'not': 'sûre içi eş.'},
 # blok 12-21
 {'bag': '75:17 → 92:12', 'kural': "okuma — harekesiz 'inne 'aleynâ': toplamak ve okutmak / yol göstermek", 'not': 'kalıp eşi.'},
 {'bag': '75:19 → 92:12', 'kural': "okuma — harekesiz 'inne 'aleynâ': açıklamak / yol göstermek", 'not': 'kalıp eşi.'},
 {'bag': '88:26 → 92:12', 'kural': "okuma — harekesiz 'inne 'aleynâ': hesap / yol göstermek", 'not': 'kalıp eşi.'},
 {'bag': '22:67 → 92:12', 'kural': "okuma — lemma dizisi (bütün ayet) 'inne' + ''alâ' + 'hudâ': 2MS + nekre / 1P + belirli", 'not': 'lemma dizisi eşi.'},
 {'bag': '53:25 → 92:13', 'kural': "okuma — lemma dizisi 'âxira' + 'ûlâ': 'li' + lafız / 'li' + 1P", 'not': 'lemma dizisi eşi.'},
 {'bag': '79:25 → 92:13', 'kural': "okuma — lemma dizisi 'âxira' + 'ûlâ': iki âlemin cezası / iki âlem 1P'nin", 'not': 'lemma dizisi eşi.'},
 {'bag': '92:12 → 92:13', 'kural': "sûre içi — 'inne' + edat + 1P + 'le' + belirli ad: ''aleynâ' / 'lenâ'", 'not': 'sûre içi eş.'},
 {'bag': '70:15 → 92:14', 'kural': "okuma — aynı harfler: morph'ta özel ad 'lezâ' (kök yok) / fiil 'telezzâ' (kök لظي)", 'not': 'harf eşi.'},
 {'bag': '87:12 → 92:14', 'kural': "okuma — lemma 'nâr': en büyük ateş / alev saçan ateş", 'not': 'lemma eşi.'},
 {'bag': '87:12 → 92:15', 'kural': "okuma — lemma 'yaslâ': 'ellezî yaslâ'n-nâr' / 'lâ yaslâhâ ille'l-eşqâ'", 'not': 'lemma eşi.'},
 {'bag': '87:11 → 92:15', 'kural': "okuma — lemma 'eşqâ' belirli; 87:11-12 'el-eşqâ' + 'ellezî yaslâ' / 92:15-16 'yaslâhâ' + 'el-eşqâ' + 'ellezî' (sıra farklı)", 'not': 'lemma eşi.'},
 {'bag': '91:12 → 92:15', 'kural': "okuma — ardışık sûre, lemma 'eşqâ': iyelikli / belirli; korpusun üç geçişi okundu (aday 1040, okuma bağı)", 'not': 'lemma eşi.'},
 {'bag': '20:48 → 92:16', 'kural': "okuma — harekesiz 'kezzebe ve tevellâ': 'men' ile / 'ellezî' ile", 'not': 'kalıp eşi.'},
 {'bag': '75:32 → 92:16', 'kural': "okuma — harekesiz 'kezzebe ve tevellâ': 'lâkin' ile / 'ellezî' ile", 'not': 'kalıp eşi.'},
 {'bag': '92:9 → 92:16', 'kural': "sûre içi — lemma 'kezzebe' iki geçiş: 'bi'l-husnâ' / 've tevellâ'", 'not': 'sûre içi eş.'},
 {'bag': '87:11 → 92:17', 'kural': "okuma — kök جنب + 3FS + belirli üstünlük adı: V. bab etken 'el-eşqâ' / II. bab edilgen 'el-etqâ'", 'not': 'kök eşi.'},
 {'bag': '49:13 → 92:17', 'kural': "okuma — lemma 'etqâ' korpusun iki geçişi: 'etqâkum' / 'el-etqâ'", 'not': 'lemma eşi.'},
 {'bag': '92:5 → 92:17', 'kural': "sûre içi — kök وقي iki geçiş: 'ittaqâ' / 'el-etqâ'", 'not': 'sûre içi eş.'},
 {'bag': '92:15 → 92:17', 'kural': "sûre içi — en bedbaht / en sakınan; ona girer / ondan uzak tutulur (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '87:14 → 92:18', 'kural': "okuma — lemma 'tezekkâ': 'men tezekkâ' kurtuluşa erer / 'ellezî … yetezekkâ'", 'not': 'lemma eşi.'},
 {'bag': '79:18 → 92:18', 'kural': "okuma — lemma 'tezekkâ': arınmaya çağrı / malını verip arınan", 'not': 'lemma eşi.'},
 {'bag': '92:11 → 92:18', 'kural': "sûre içi — lemma 'mâl' iki geçiş: malı yarar sağlamaz / malını verir", 'not': 'sûre içi eş.'},
 {'bag': '92:5 → 92:18', 'kural': "sûre içi — verme iki kökle: 'a'tâ' (عطو) / 'yu'tî' (أتي)", 'not': 'sûre içi eş.'},
 {'bag': '13:22 → 92:20', 'kural': "ölçüm xref — 'ibtiğâ'e vechi rabb': 3MP sabredenler / 3MS + 'el-a'lâ'", 'not': 'xref eşi.'},
 {'bag': '87:1 → 92:20', 'kural': "okuma — 'rabb' + 'el-a'lâ': 2MS iyelik / 3MS iyelik", 'not': 'lemma eşi.'},
 {'bag': '79:24 → 92:20', 'kural': "okuma — 'rabb' + 'el-a'lâ': konuşanın kendisi için iddiası / Rab tamlaması (aday 1041, sûreler arası okuma notu)", 'not': 'lemma eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_leyl', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in LEYL]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_leyl'] = LEYL
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_leyl', len(LEYL), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_leyl', len(BAGLAR['AS_leyl']))
