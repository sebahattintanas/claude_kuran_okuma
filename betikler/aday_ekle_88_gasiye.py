# -*- coding: utf-8 -*-
"""aday_ekle_88_gasiye.py — sûre 88 (Ğâşiye) adayları (AX_gasiye) ve okuma bağları (AS_gasiye).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

GASIYE = [
]

BAGLAR = {"AS_gasiye": [
 # blok 1-7
 {'bag': '87:19 → 88:1', 'kural': "okuma — ardışık sûre sınırı: adlı iki kişi (İbrâhîm, Mûsâ) ile kapanış / 2MS'ye 'hel etâke hadîthu' sorusu ile açılış; fâsıla ى → ة (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '79:15 → 88:1', 'kural': "okuma — harekesiz 'hel etâke hadîthu': Mûsâ / 'el-ğâşiye'", 'not': 'kalıp eşi.'},
 {'bag': '85:17 → 88:1', 'kural': "okuma — harekesiz 'hel etâke hadîthu': ordular / 'el-ğâşiye' (ardışık olmayan, üç sûre önce)", 'not': 'kalıp eşi.'},
 {'bag': '51:24 → 88:1', 'kural': "okuma — harekesiz 'hel etâke hadîthu': İbrâhîm'in konukları / 'el-ğâşiye'", 'not': 'kalıp eşi.'},
 {'bag': '20:9 → 88:1', 'kural': "okuma — önekli 've hel etâke hadîthu': Mûsâ / 'el-ğâşiye'", 'not': 'kalıp eşi.'},
 {'bag': '12:107 → 88:1', 'kural': "okuma — lemma 'ğâşiye': nekre, 'azâb'a izâfetle / belirli, tek başına", 'not': 'lemma eşi.'},
 {'bag': '75:22 → 88:2', 'kural': "okuma — harekesiz 'vucûhun yevme'izin' + FS sıfat: 'nâdira' / 'xâşi'a'", 'not': 'kalıp eşi.'},
 {'bag': '80:38 → 88:2', 'kural': "okuma — harekesiz 'vucûhun yevme'izin' + FS sıfat: 'musfira' / 'xâşi'a'", 'not': 'kalıp eşi.'},
 {'bag': '79:9 → 88:2', 'kural': "okuma — ortaç 'xâşi'a': gözler / yüzler", 'not': 'lemma eşi.'},
 {'bag': '87:12 → 88:4', 'kural': "okuma — lemma 'yaslâ' + 'nâr': 3MS + belirli 'en-nâra'l-kubrâ' / 3FS + nekre 'nâran hâmiye' (aday 1040 ailesi, ardışık sûre)", 'not': 'lemma eşi.'},
 {'bag': '14:16 → 88:5', 'kural': "okuma — edilgen 'suqiya' + 'min' + nekre: 3MS + irinli su / 3FS + kaynar pınar", 'not': 'kurgu eşi.'},
 {'bag': '47:15 → 88:5', 'kural': "okuma — edilgen 'suqiya' + kaynar su: PERF 3MP 'suqû mâ'en hamîmen' / IMPF 3FS 'min 'aynin âniye'", 'not': 'kurgu eşi.'},
 {'bag': '76:15 → 88:5', 'kural': "okuma — lemma 'âniye' morph'ta birleşiyor: kaplar / kaynar (eşsesli; lemma sayısı verilmedi)", 'not': 'eşsesli lemma.'},
 {'bag': '69:36 → 88:6', 'kural': "okuma — harekesiz 'ta'âmun illâ min' korpusun iki ayeti: 'lâ' + irin / 'leyse' + 'darî''", 'not': 'kalıp eşi.'},
 {'bag': '77:31 → 88:7', 'kural': "okuma — harekesiz 've lâ yuğnî min' korpusun iki ayeti: gölge alevden korumaz / yiyecek açlıktan korumaz", 'not': 'kalıp eşi.'},
 {'bag': '88:2 → 88:6', 'kural': "sûre içi — dişil çoğul 'vucûh' (88:2-5) / eril çoğul 'lehum' (88:6): yüzler / sahipleri", 'not': 'sûre içi eş.'},
 # blok 8-16
 {'bag': '88:2 → 88:8', 'kural': "sûre içi — 'vucûhun yevme'izin' + FS ortaç: zelil / nimet içinde (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '88:3 → 88:9', 'kural': "sûre içi — çalışıp yorgun / çabasından hoşnut (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '69:21 → 88:9', 'kural': "okuma — 'râdiye' + ardından 'fî cennetin 'âliye' (69:21-22 / 88:9-10) sıralı iki ayet, ardışık olmayan sûre: hoşnut edici yaşayış / çabasından hoşnut yüzler", 'not': 'sıralı eş.'},
 {'bag': '69:22 → 88:10', 'kural': "ölçüm esit2 TAM — 'fî cennetin 'âliye' korpusun iki ayeti", 'not': 'esit2 eşi.'},
 {'bag': '78:35 → 88:11', 'kural': "okuma — 'lâ … fîhâ' + kök لغو: 3MP 'lağv' + ikinci nesne / tek fiil, 'lâğiye'", 'not': 'kurgu eşi.'},
 {'bag': '56:25 → 88:11', 'kural': "okuma — 'lâ yesme'ûne fîhâ lağven' / 'lâ tesme'u fîhâ lâğiye'", 'not': 'kurgu eşi.'},
 {'bag': '88:5 → 88:12', 'kural': "sûre içi — kök عين [2/2]: kaynar pınardan içirilir / akan pınar", 'not': 'sûre içi eş.'},
 {'bag': '69:11 → 88:12', 'kural': "okuma — lemma 'câriye': belirli, akan gemi / nekre, akan pınar", 'not': 'lemma eşi.'},
 {'bag': '52:20 → 88:13', 'kural': "okuma — lemma 'surur': dizilmiş tahtlar / yükseltilmiş tahtlar", 'not': 'lemma eşi.'},
 {'bag': '56:34 → 88:13', 'kural': "okuma — lemma 'merfû'a': döşekler / tahtlar", 'not': 'lemma eşi.'},
 {'bag': '56:18 → 88:14', 'kural': "okuma — lemma 'ekvâb': dolaştırılan kupalar / konulmuş kupalar", 'not': 'lemma eşi.'},
 {'bag': '76:15 → 88:14', 'kural': "okuma — lemma 'ekvâb': billur kupalar dolaştırılır / konulmuş", 'not': 'lemma eşi.'},
 {'bag': '52:20 → 88:15', 'kural': "okuma — lemma 'masfûfa' korpusun iki ayeti: tahtlar / yastıklar", 'not': 'lemma eşi.'},
 # blok 17-26
 {'bag': '86:5 → 88:17', 'kural': "okuma — bakma + edilgen 'xuliqa': emir lâmı, insan / soru, deve (iki sûre arayla)", 'not': 'kurgu eşi.'},
 {'bag': '50:6 → 88:17', 'kural': "okuma — soru + bakma + 'ilâ' + 'keyfe': 'e-fe-lem', 1P etken / 'e-fe-lâ', edilgen", 'not': 'kurgu eşi.'},
 {'bag': '79:28 → 88:18', 'kural': "okuma — kök رفع + gök: etken 3MS, tavan / edilgen, gök", 'not': 'kök eşi.'},
 {'bag': '88:13 → 88:18', 'kural': "sûre içi — kök رفع [2/2]: yükseltilmiş tahtlar / yükseltilen gök", 'not': 'sûre içi eş.'},
 {'bag': '79:32 → 88:19', 'kural': "okuma — dağlar + fiil: etken 'ersâ' / edilgen 'nusibat'", 'not': 'kurgu eşi.'},
 {'bag': '88:3 → 88:19', 'kural': "sûre içi — kök نصب [2/2]: 'nâsıba' (yorgun) / 'nusibat' (dikildi)", 'not': 'sûre içi eş.'},
 {'bag': '79:30 → 88:20', 'kural': "okuma — yer + yayma: etken 'dehâ' + 'ba'de zâlike' / edilgen 'sutihat'", 'not': 'kurgu eşi.'},
 {'bag': '88:18 → 88:20', 'kural': "sûre içi — gök yükseltildi / yer yayıldı (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '87:9 → 88:21', 'kural': "okuma — ardışık sûrede 'fe-zekkir': + şart 'in' / + hasr 'innemâ' (aday 1040 ailesi)", 'not': 'kalıp eşi.'},
 {'bag': '50:45 → 88:21', 'kural': "okuma — 'ente 'aleyhim bi-' + olumsuz ve 'fe-zekkir': sıra olumsuz → emir / emir → olumsuz (88:21-22)", 'not': 'kurgu eşi.'},
 {'bag': '50:45 → 88:22', 'kural': "okuma — 'mâ ente 'aleyhim bi-cebbâr' / 'leste 'aleyhim bi-musaytir'", 'not': 'kalıp eşi.'},
 {'bag': '52:37 → 88:22', 'kural': "okuma — lemma 'musaytir' korpusun iki ayeti: 3MP için soru / 2MS için olumsuz", 'not': 'lemma eşi.'},
 {'bag': '88:21 → 88:22', 'kural': "sûre içi — öğüt verici / zorlayıcı (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '88:6 → 88:22', 'kural': "sûre içi — kök ليس [2/2]: 'leyse lehum' / 'leste 'aleyhim'", 'not': 'sûre içi eş.'},
 {'bag': '9:74 → 88:23', 'kural': "okuma — 'tevellâ' + Allah'ın azabı: şart 'in', 3MP / 'men', 3MS (88:23-24)", 'not': 'kurgu eşi.'},
 {'bag': '9:74 → 88:24', 'kural': "ölçüm xref — 'azzebe' + lafız + 'azâb': nekre + 'elîm' / belirli + 'ekber'", 'not': 'xref eşi.'},
 {'bag': '32:21 → 88:24', 'kural': "okuma — harekesiz 'el-'azâbe'l-ekber' korpusun iki ayeti: 'ednâ' ile karşılaştırma / tek başına", 'not': 'kalıp eşi.'},
 {'bag': '87:12 → 88:24', 'kural': "okuma — ardışık sûrede belirli üstünlük sıfatı: 'en-nâra'l-kubrâ' / 'el-'azâbe'l-ekber' (aday 1040 ailesi)", 'not': 'kurgu eşi.'},
 {'bag': '88:25 → 88:26', 'kural': "sûre içi — 'inne' + edat + 1P + mastar + 3MP: 'ileynâ iyâbehum' / ''aleynâ hisâbehum'", 'not': 'sûre içi eş.'},
 {'bag': '75:17 → 88:26', 'kural': "okuma — 'inne 'aleynâ' + mastar + zamir: toplamak / hesap", 'not': 'kalıp eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_gasiye', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in GASIYE]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_gasiye'] = GASIYE
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_gasiye', len(GASIYE), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_gasiye', len(BAGLAR['AS_gasiye']))
