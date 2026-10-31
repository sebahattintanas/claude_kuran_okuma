# -*- coding: utf-8 -*-
"""aday_ekle_90_beled.py — sûre 90 (Beled) adayları (AX_beled) ve okuma bağları (AS_beled).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

BELED = [
]

BAGLAR = {"AS_beled": [
 # blok 1-10
 {'bag': '89:30 → 90:1', 'kural': "okuma — ardışık sûre sınırı: 1S konuşanın giriş emri ile kapanış / 1S yemin ile açılış; fâsıla ى → د (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '75:1 → 90:1', 'kural': "okuma — harekesiz 'lâ uqsimu' korpusun iki ayeti: kıyamet günü / bu belde", 'not': 'kalıp eşi.'},
 {'bag': '89:11 → 90:1', 'kural': "okuma — lemma 'beled': ülkelerde azdılar / bu beldeye yemin (ardışık sûre)", 'not': 'lemma eşi.'},
 {'bag': '90:1 → 90:2', 'kural': "sûre içi — 'bi-hâze'l-beled' korpusun iki ayeti: yemin / 2MS'nin bu beldedeki hâli", 'not': 'sûre içi eş.'},
 {'bag': '75:3 → 90:5', 'kural': "okuma — harekesiz 'e-yahsebu' + 'en' / 'ellen' + olumsuz: özne 'el-insân' yazılı / yazılmamış", 'not': 'kalıp eşi.'},
 {'bag': '75:36 → 90:7', 'kural': "okuma — 'e-yahsebu' + 'en' + IMPF: başıboş bırakılma / kimsenin görmemesi", 'not': 'kalıp eşi.'},
 {'bag': '90:5 → 90:7', 'kural': "sûre içi — 'e-yahsebu en' + olumsuz + fiil + 'ehad': güç yetirmek / görmek", 'not': 'sûre içi eş.'},
 {'bag': '89:25 → 90:5', 'kural': "okuma — olumsuz cümlede nekre 'ehad' (e_el değil): ardışık sûrede iki ayet + iki ayet", 'not': 'lemma eşi.'},
 {'bag': '89:20 → 90:6', 'kural': "okuma — lemma 'mâl': 2MP malı pek sever / 1S yığın yığın mal tükettim der", 'not': 'lemma eşi.'},
 {'bag': '78:6 → 90:8', 'kural': "okuma — harekesiz 'e-lem nec'al': yer döşek / insana iki göz", 'not': 'kalıp eşi.'},
 {'bag': '77:25 → 90:8', 'kural': "okuma — harekesiz 'e-lem nec'al': yer toplayıcı / insana iki göz", 'not': 'kalıp eşi.'},
 {'bag': '90:8 → 90:9', 'kural': "sûre içi — 'nec'al'ın nesneleri: iki göz / dil + iki dudak", 'not': 'sûre içi eş.'},
 {'bag': '76:3 → 90:10', 'kural': "okuma — 1P + 'hedâ' + 3MS: tek yol + iki sonuç / iki yüksek yol", 'not': 'kalıp eşi.'},
 {'bag': '90:4 → 90:10', 'kural': "sûre içi — 1P konuşan: insanı zorluk içinde yarattık / ona iki yol gösterdik", 'not': 'sûre içi eş.'},
 # blok 11-20
 {'bag': '90:11 → 90:12', 'kural': "sûre içi — lemma ''aqabe' korpusun iki ayeti: atılmadı / ne olduğu soruluyor", 'not': 'sûre içi eş.'},
 {'bag': '69:3 → 90:12', 'kural': "ölçüm esit2 BENZER — 've mâ edrâke mâ' + belirli ad: gerçekleşecek olan / sarp yokuş", 'not': 'esit2 eşi.'},
 {'bag': '74:27 → 90:12', 'kural': "okuma — 've mâ edrâke mâ' + ad: Sekar / sarp yokuş", 'not': 'kalıp eşi.'},
 {'bag': '47:4 → 90:13', 'kural': "okuma — lemma 'raqabe': boyun vurma / boyun çözme", 'not': 'lemma eşi.'},
 {'bag': '89:18 → 90:14', 'kural': "okuma — kök طعم + yoksul: 2MP doyurmaya özendirmez / açlık gününde doyurmak (ardışık sûre)", 'not': 'kurgu eşi.'},
 {'bag': '76:8 → 90:14', 'kural': "okuma — kök طعم + yoksul + yetim: 3MP yedirir / mastar, öznesiz", 'not': 'kurgu eşi.'},
 {'bag': '89:17 → 90:15', 'kural': "okuma — lemma 'yetîm': 2MP ikram etmez / yetimi doyurmak (ardışık sûre)", 'not': 'lemma eşi.'},
 {'bag': '69:34 → 90:16', 'kural': "okuma — lemma 'miskîn': doyurmaya özendirmiyordu / yoksulu doyurmak", 'not': 'lemma eşi.'},
 {'bag': '90:15 → 90:16', 'kural': "sûre içi — nekre ad + 'zâ' + 'me-' önekli nekre ad: yakınlığı olan yetim / toprağa bulanmış yoksul", 'not': 'sûre içi eş.'},
 {'bag': '83:29 → 90:17', 'kural': "okuma — harekesiz 'mine'llezîne âmenû': iman edenlere gülme / onlardan olmak", 'not': 'kalıp eşi.'},
 {'bag': '56:8 → 90:18', 'kural': "okuma — 'ashâbu'l-meymene' korpusun iki ayeti: soru-tekrar / işaret + haber", 'not': 'kalıp eşi.'},
 {'bag': '56:9 → 90:19', 'kural': "okuma — 'ashâbu'l-meş'eme' korpusun iki ayeti; 56:8-9 / 90:18-19 aynı sıra", 'not': 'kalıp eşi.'},
 {'bag': '90:17 → 90:19', 'kural': "sûre içi — iman ettiler / inkâr ettiler (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '90:18 → 90:19', 'kural': "sûre içi — sağ / sol (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '90:19 → 90:20', 'kural': "sûre içi — inkâr edenler / üzerlerinde kapatılmış ateş", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_beled', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in BELED]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_beled'] = BELED
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_beled', len(BELED), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_beled', len(BAGLAR['AS_beled']))
