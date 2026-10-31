# -*- coding: utf-8 -*-
"""aday_ekle_94_insirah.py — sûre 94 (İnşirâh) adayları (AX_insirah) ve okuma bağları (AS_insirah).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

INSIRAH = [
]

BAGLAR = {"AS_insirah": [
 # blok 1-8
 {'bag': '93:11 → 94:1', 'kural': "okuma — ardışık sûre sınırı: Rab nimetini anlatma emri ile kapanış / 'e-lem neşrah' sorusu ile açılış; fâsıla ث → ك (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '93:6 → 94:1', 'kural': "okuma — ardışık sûre, 'e-lem' + cezm IMPF + 2MS: 3MS bulan / 1P açan (aday 1040, okuma bağı)", 'not': 'kalıp eşi.'},
 {'bag': '20:25 → 94:1', 'kural': "okuma — lemma 'şeraha' + 'sadr': 1S dua / 1P soru", 'not': 'lemma eşi.'},
 {'bag': '39:22 → 94:1', 'kural': "okuma — lemma 'şeraha' + 'sadr': lafız özne / 1P özne", 'not': 'lemma eşi.'},
 {'bag': '53:38 → 94:2', 'kural': "okuma — lemma 'vizr': yük başkasına taşıtılmaz / 2MS'nin yükü indirildi", 'not': 'lemma eşi.'},
 {'bag': '84:10 → 94:3', 'kural': "okuma — lemma 'zahr': kitabın verildiği yön / yükün büktüğü bel", 'not': 'lemma eşi.'},
 {'bag': '94:2 → 94:4', 'kural': 'sûre içi — indirdik / yükselttik (aday 1039, okuma); 1P + 2MS edat + 2MS iyelikli nesne', 'not': 'sûre içi eş.'},
 {'bag': '39:22 → 94:4', 'kural': "okuma — lemma 'zikr': Allah'ın anılması / 2MS'nin anılması", 'not': 'lemma eşi.'},
 {'bag': '65:7 → 94:5', 'kural': "okuma — ''usr' + 'yusr': 'ba'de', ikisi nekre / 'ma'a', ''usr' belirli", 'not': 'lemma eşi.'},
 {'bag': '92:7 → 94:5', 'kural': "okuma — ardışık olmayan iki sûre önce, kök يسر: 'yusrâ' (fu'lâ) / 'yusr' (fu'l)", 'not': 'kök eşi.'},
 {'bag': '92:10 → 94:5', 'kural': "okuma — kök عسر: ''usrâ' (fu'lâ) / ''usr' (fu'l)", 'not': 'kök eşi.'},
 {'bag': '94:5 → 94:6', 'kural': "ölçüm esit2 TAM + nakarat3 — sûre içi tekrar, fark 'fe' (aday 1039: ikisinde de zorluk / kolaylık)", 'not': 'sûre içi eş.'},
 {'bag': '55:31 → 94:7', 'kural': "okuma — lemma 'feraġa' korpusun iki ayeti: 1P / 2MS", 'not': 'lemma eşi.'},
 {'bag': '88:19 → 94:7', 'kural': "okuma — aynı morph lemma etiketi iki anlamda: dağların dikilmesi / 2MS'ye 'yorul' emri (924)", 'not': 'lemma eşi.'},
 {'bag': '68:32 → 94:8', 'kural': "okuma — 'ilâ rabb' + kök رغب: 1P söz, ad / 2MS'ye emir", 'not': 'kök eşi.'},
 {'bag': '9:59 → 94:8', 'kural': "okuma — 'ilâ' + kök رغب: 'ile'llâh' / 'ilâ rabbike'", 'not': 'kök eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_insirah', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in INSIRAH]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_insirah'] = INSIRAH
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_insirah', len(INSIRAH), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_insirah', len(BAGLAR['AS_insirah']))
