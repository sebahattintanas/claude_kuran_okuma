# -*- coding: utf-8 -*-
"""aday_ekle_85_buruc.py — sûre 85 (Burûc) adayları (AX_buruc) ve okuma bağları (AS_buruc).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

BURUC = [
]

BAGLAR = {"AS_buruc": [
 # blok 1-9
 {'bag': '84:25 → 85:1', 'kural': "okuma — ardışık sûre sınırı: istisna + 3MP ile kapanış / yemin ile açılış, şahıs işareti yok; ikisi de lafızsız, Rabsız; fâsıla ن → ج (aday 1040, kayıt)", 'not': 'sınır.'},
 {'bag': '51:7 → 85:1', 'kural': "okuma — harekesiz 've's-semâ'i zât' + nitelik, yemin: örgü / burçlar", 'not': 'kalıp eşi.'},
 {'bag': '15:16 → 85:1', 'kural': "okuma — lemma 'burûc': göğe konan (1P fiil + 'fî') / göğün niteliği ('zât')", 'not': 'lemma eşi.'},
 {'bag': '25:61 → 85:1', 'kural': "okuma — lemma 'burûc': 'ce'ale fi's-semâ'i burûcâ' / 'zâti'l-burûc'", 'not': 'lemma eşi.'},
 {'bag': '11:103 → 85:3', 'kural': "okuma — lemma 'meşhûd': 'yevmun meşhûd' / nekre, adsız", 'not': 'lemma eşi.'},
 {'bag': '17:78 → 85:3', 'kural': "okuma — lemma 'meşhûd': sabah okuması / nekre, adsız", 'not': 'lemma eşi.'},
 {'bag': '51:10 → 85:4', 'kural': "okuma — 'qutile' + ad, cümle başında: 'el-xarrâsûn' / 'ashâbu'l-uxdûd'", 'not': 'kalıp eşi.'},
 {'bag': '74:20 → 85:4', 'kural': "okuma — 'qutile' cümle başında (kınama)", 'not': 'kalıp eşi.'},
 {'bag': '80:17 → 85:4', 'kural': "okuma — 'qutile' + ad: 'el-insân' / 'ashâbu'l-uxdûd'", 'not': 'kalıp eşi.'},
 {'bag': '85:1 → 85:5', 'kural': "sûre içi — 'zât' + belirli ad: gök + burçlar / ateş + yakıt", 'not': 'sûre içi eş.'},
 {'bag': '66:6 → 85:5', 'kural': "okuma — lemma 'veqûd': yakıtı insanlar ve taşlar / yakıtlı ateş, yakıt adsız", 'not': 'lemma eşi.'},
 {'bag': '9:83 → 85:6', 'kural': "okuma — lemma 'qu'ûd': geri oturma / ateşin başında oturma", 'not': 'lemma eşi.'},
 {'bag': '85:3 → 85:7', 'kural': "sûre içi — lemma 'şâhid': adsız tanık / hendeğin sahipleri tanık", 'not': 'sûre içi eş.'},
 {'bag': '9:74 → 85:8', 'kural': "okuma — harekesiz 've mâ neqamû' korpusun iki ayeti: 'illâ en' + fiil + lafız — zenginleştirme / iman", 'not': 'kalıp eşi.'},
 {'bag': '58:6 → 85:9', 'kural': "okuma — 've'llâhu 'alâ kulli şey'in şehîd'", 'not': 'kalıp eşi.'},
 {'bag': '85:3 → 85:9', 'kural': "sûre içi — kök شهد [4/4]: adsız tanık ve tanıklık edilen / hendeğin sahipleri tanık / Allah her şeye tanık", 'not': 'sûre içi eş.'},
 # blok 10-16
 {'bag': '22:9 → 85:10', 'kural': "okuma — lemma 'harîq' + ''azâb': 'nuzîquhû' tattırma / 'lehum'", 'not': 'lemma eşi.'},
 {'bag': '22:22 → 85:10', 'kural': "okuma — ''azâbe'l-harîq': 'zûqû' emri / 'lehum'", 'not': 'lemma eşi.'},
 {'bag': '85:10 → 85:11', 'kural': "sûre içi — 'inne'llezîne' + iki grup: fitneye uğratıp tevbe etmeyenler, azap / iman edip salih iş yapanlar, cennetler (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '84:25 → 85:11', 'kural': "okuma — ardışık sûrede 'âmenû ve 'amilu's-sâlihâti lehum': 'illâ' + 'ecrun ğayru memnûn' / 'inne' + 'cennât' (aday 1040 ailesi)", 'not': 'kalıp eşi.'},
 {'bag': '41:8 → 85:11', 'kural': "okuma — harekesiz 'inne'llezîne âmenû ve 'amilu's-sâlihâti lehum': ecr / cennetler", 'not': 'kalıp eşi.'},
 {'bag': '43:8 → 85:12', 'kural': "okuma — lemma 'batş' korpusun üç ayetinden: helâk edilenlerin yakalayış gücü / Rabbin yakalayışı", 'not': 'lemma eşi.'},
 {'bag': '50:36 → 85:12', 'kural': "okuma — lemma 'batş': 'eşeddu minhum batşâ' / 'batşa rabbike le-şedîd'", 'not': 'lemma eşi.'},
 {'bag': '29:19 → 85:13', 'kural': "okuma — lemma 'ebde'e' (IV. bab) + 'a'âde': 'el-xalq' nesneli, lafızla / nesnesiz, zamirle", 'not': 'lemma eşi.'},
 {'bag': '34:49 → 85:13', 'kural': "okuma — 'yubdi'u … yu'îd' korpusun üç ayetinden: bâtıl, olumsuz / Rab, olumlu", 'not': 'kalıp eşi.'},
 {'bag': '11:90 → 85:14', 'kural': "okuma — lemma 'vedûd' korpusun iki ayeti: 'rahîmun vedûd' / 'el-ğafûru'l-vedûd', ikisi de Rab için", 'not': 'lemma eşi.'},
 {'bag': '40:15 → 85:15', 'kural': "okuma — harekesiz 'zu'l-'arş' korpusun iki ayeti", 'not': 'kalıp eşi.'},
 {'bag': '81:20 → 85:15', 'kural': "okuma — 'zi'l-'arş' GEN / 'zu'l-'arş' NOM", 'not': 'kalıp eşi.'},
 {'bag': '11:73 → 85:15', 'kural': "okuma — lemma 'mecîd' Allah için: 'hamîdun mecîd' / 'zu'l-'arşi'l-mecîd'", 'not': 'lemma eşi.'},
 {'bag': '50:1 → 85:15', 'kural': "okuma — lemma 'mecîd': Kur'ân için / Rab için", 'not': 'lemma eşi.'},
 {'bag': '11:107 → 85:16', 'kural': "ölçüm lemma dizisi — 'fe''âlun limâ yurîd' korpusun iki ayeti: Rab adıyla / adsız haber dizisinde", 'not': 'kalıp eşi.'},
 {'bag': '85:7 → 85:16', 'kural': "sûre içi — kök فعل [2/2]: hendeğin sahiplerinin yaptıkları / Rab dilediğini yapan (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '85:7 → 85:9', 'kural': "sûre içi — kök شهد: hendeğin sahipleri tanık / Allah tanık (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 # blok 17-22
 {'bag': '79:15 → 85:17', 'kural': "okuma — harekesiz 'hel etâke hadîthu': Mûsâ / ordular", 'not': 'kalıp eşi.'},
 {'bag': '51:24 → 85:17', 'kural': "okuma — 'hel etâke hadîthu': İbrâhîm'in konukları / ordular", 'not': 'kalıp eşi.'},
 {'bag': '84:22 → 85:19', 'kural': "okuma — ardışık sûrede 'beli'llezîne keferû' + yalanlama: fiil / 'fî' + mastar (aday 1040, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '84:23 → 85:20', 'kural': "okuma — ardışık sûrede 've'llâhu' + lafız + haber, 'bel'li cümlenin ardından: a'lem / muhît; 84:22-23 / 85:19-20 iki ayetlik sıralı eşleşme (aday 1040, kayıt)", 'not': 'kurgu eşi.'},
 {'bag': '38:2 → 85:19', 'kural': "okuma — harekesiz 'beli'llezîne keferû fî' + mastar: büyüklenme ve ayrılık / yalanlama", 'not': 'kalıp eşi.'},
 {'bag': '11:92 → 85:20', 'kural': "okuma — 'verâ'' + 'muhît' aynı ayette: insanlar onu arkalarına attı / Allah onları arkalarından kuşatır", 'not': 'kurgu eşi.'},
 {'bag': '29:49 → 85:21', 'kural': "okuma — harekesiz 'bel huve' + haber: âyetler / Kur'ân", 'not': 'kalıp eşi.'},
 {'bag': '50:1 → 85:21', 'kural': "okuma — 'qur'ân' + 'mecîd': belirli, yemin / nekre, haber", 'not': 'lemma eşi.'},
 {'bag': '85:15 → 85:21', 'kural': "sûre içi — lemma 'mecîd' [2/2]: Rab / Kur'ân (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '54:13 → 85:22', 'kural': "okuma — lemma 'levh': gemi tahtaları (çoğul) / tekil levha", 'not': 'lemma eşi.'},
 {'bag': '21:32 → 85:22', 'kural': "okuma — lemma 'mahfûz' korpusun iki ayeti: korunmuş tavan (gök) / korunmuş levha", 'not': 'lemma eşi.'},
 {'bag': '85:19 → 85:21', 'kural': "sûre içi — 'bel' iki kez: inkâr edenler yalanlama içinde / o şanı yüce bir Kur'ân (aday 1039, okuma)", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_buruc', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in BURUC]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_buruc'] = BURUC
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_buruc', len(BURUC), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_buruc', len(BAGLAR['AS_buruc']))
