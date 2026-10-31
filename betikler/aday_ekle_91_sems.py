# -*- coding: utf-8 -*-
"""aday_ekle_91_sems.py — sûre 91 (Şems) adayları (AX_sems) ve okuma bağları (AS_sems).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

SEMS = [
]

BAGLAR = {"AS_sems": [
 # blok 1-10
 {'bag': '90:20 → 91:1', 'kural': "okuma — ardışık sûre sınırı: üzerlerinde kapatılmış ateş ile kapanış / güneşe yemin ile açılış; fâsıla ة → ا (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '79:29 → 91:1', 'kural': "okuma — lemma 'duhâ' + 3FS: 3MS kuşluğu çıkarır / kuşluğa yemin", 'not': 'lemma eşi.'},
 {'bag': '91:2 → 91:4', 'kural': "sûre içi — 've' + belirli ad + 'izâ' + fiil + 'hâ' üç ayet (91:2-4): ay / gündüz / gece; PERF, PERF, IMPF", 'not': 'sûre içi eş.'},
 {'bag': '81:17 → 91:4', 'kural': "okuma — harekesiz 've'l-leyli izâ' + fiil: kararıp gelme / bürüme", 'not': 'kalıp eşi.'},
 {'bag': '89:4 → 91:4', 'kural': "okuma — harekesiz 've'l-leyli izâ' + fiil: yürüyüp gitme / bürüme", 'not': 'kalıp eşi.'},
 {'bag': '91:3 → 91:4', 'kural': "sûre içi — gündüz / gece (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '79:27 → 91:5', 'kural': "okuma — gök + 'benâhâ': soruya cevap / yemin içinde 'mâ benâhâ'", 'not': 'lemma eşi.'},
 {'bag': '90:3 → 91:5', 'kural': "okuma — 've' + 'mâ' + PERF 3MS: doğurduğu / kurduğu (ardışık sûre; 'mâ' morph REL)", 'not': 'kalıp eşi.'},
 {'bag': '79:30 → 91:6', 'kural': "okuma — yer + PERF 3MS + 'hâ', başka kök: 'dehâhâ' / 'tahâhâ' (yayma)", 'not': 'kurgu eşi.'},
 {'bag': '91:5 → 91:6', 'kural': "sûre içi — gök / yer (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '79:28 → 91:7', 'kural': "okuma — lemma 'sevvâ' + 'hâ': gök düzenlenir / nefis düzenlenir", 'not': 'lemma eşi.'},
 {'bag': '87:2 → 91:7', 'kural': "okuma — lemma 'sevvâ': 'xalaqa fe-sevvâ' nesnesiz / 'mâ sevvâhâ' nefis", 'not': 'lemma eşi.'},
 {'bag': '91:7 → 91:8', 'kural': "sûre içi — 'mâ sevvâhâ' + 'fe-elhemehâ': düzenleme, sonra ilham ('fe')", 'not': 'sûre içi eş.'},
 {'bag': '90:10 → 91:8', 'kural': "okuma — ardışık sûre: 1P iki yol gösterdi / 3MS taşkınlık ve sakınma ilham etti", 'not': 'kurgu eşi.'},
 {'bag': '87:14 → 91:9', 'kural': "ölçüm esit2 BENZER — 'qad efleha men' + PERF: V. bab 'tezekkâ' / II. bab 'zekkâhâ'", 'not': 'esit2 eşi.'},
 {'bag': '20:111 → 91:10', 'kural': "okuma — harekesiz 've qad xâbe men' + PERF: zulüm yüklenen / nefsi gömüp örten", 'not': 'kalıp eşi.'},
 {'bag': '91:9 → 91:10', 'kural': "sûre içi — 'qad' + PERF + 'men' + PERF + 'hâ': kurtuluş / hüsran, arındırma / gömme (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 # blok 11-15
 {'bag': '89:9 → 91:11', 'kural': "okuma — Semûd ardışık iki sûrede: kayaları oyan / azgınlığıyla yalanlayan", 'not': 'kurgu eşi.'},
 {'bag': '54:23 → 91:11', 'kural': "okuma — harekesiz 'kezzebet themûd' + 'bi': uyarıları / azgınlığıyla", 'not': 'kalıp eşi.'},
 {'bag': '69:4 → 91:11', 'kural': "okuma — harekesiz 'kezzebet themûd': kapıyı çalanı (Âd ile) / azgınlığıyla", 'not': 'kalıp eşi.'},
 {'bag': '87:11 → 91:12', 'kural': "okuma — lemma 'eşqâ': belirli, öğütten kaçınır / iyelikli, fırlar", 'not': 'lemma eşi.'},
 {'bag': '14:10 → 91:13', 'kural': "ölçüm xref — 'qâle' + elçi + lafız: çoğul elçiler soru sorar / tekil elçi uyarır", 'not': 'xref eşi.'},
 {'bag': '11:64 → 91:13', 'kural': "okuma — harekesiz 'nâqatu'llâh', alıntı içinde: işaret + haber / ACC uyarı", 'not': 'kalıp eşi.'},
 {'bag': '26:155 → 91:13', 'kural': "okuma — lemma 'nâqa' + su payı: 'şirb' / 'suqyâ'", 'not': 'lemma eşi.'},
 {'bag': '54:27 → 91:13', 'kural': "okuma — lemma 'nâqa': 1P sınama olarak gönderir / elçi uyarır", 'not': 'lemma eşi.'},
 {'bag': '54:29 → 91:14', 'kural': "okuma — lemma ''aqara': tekil arkadaş keser / 3MP keserler", 'not': 'lemma eşi.'},
 {'bag': '67:11 → 91:14', 'kural': "okuma — harekesiz 'bi-zenbihim' korpusun iki ayeti: itiraf / helâk sebebi", 'not': 'kalıp eşi.'},
 {'bag': '91:7 → 91:14', 'kural': "sûre içi — lemma 'sevvâ' + 3FS [2/2]: 'mâ' nefsi düzenler / Rab dümdüz eder", 'not': 'sûre içi eş.'},
 {'bag': '91:11 → 91:14', 'kural': "sûre içi — kök كذب [2/2]: 3FS kavim / 3MP", 'not': 'sûre içi eş.'},
 {'bag': '91:13 → 91:14', 'kural': "sûre içi — elçinin uyarısı / yalanlama + kesme ('fe' zinciri)", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_sems', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in SEMS]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_sems'] = SEMS
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_sems', len(SEMS), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_sems', len(BAGLAR['AS_sems']))
