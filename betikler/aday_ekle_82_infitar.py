# -*- coding: utf-8 -*-
"""aday_ekle_82_infitar.py — sûre 82 (İnfitâr) adayları (AX_infitar) ve okuma bağları (AS_infitar).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

INFITAR = [
]

BAGLAR = {"AS_infitar": [
 # blok 1-10
 {'bag': '81:29 → 82:1', 'kural': "okuma — ardışık sûre sınırı: lafız + Rab + hasr ile kapanış / lafızsız şart zarfı ile açılış; fâsıla ن → ت (aday 1040, kayıt)", 'not': 'sınır.'},
 {'bag': '81:11 → 82:1', 'kural': "okuma — harekesiz 'ize's-semâ'' (4 ayet), ardışık sûrede: 'kuşitat' / 'infatarat' (aday 1040 ailesi)", 'not': 'kalıp eşi.'},
 {'bag': '73:18 → 82:1', 'kural': "okuma — gök + kök فطر VII. bab: 'munfatır' / 'infatarat'", 'not': 'kök eşi.'},
 {'bag': '81:2 → 82:2', 'kural': "okuma — ardışık sûrede 've izâ' + yıldız adı + dönüşlü PERF 3FS: 'nucûm … inkederet' / 'kevâkib … intetharat' (aday 1040 ailesi)", 'not': 'kurgu eşi.'},
 {'bag': '37:6 → 82:2', 'kural': "okuma — lemma 'kevkeb': dünya göğünün süsü / saçılan yıldızlar", 'not': 'lemma eşi.'},
 {'bag': '81:6 → 82:3', 'kural': "okuma — harekesiz 've ize'l-bihâr' korpusun iki ayeti, ardışık iki sûrede: 'succirat' / 'fuccirat' (aday 1040, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '54:12 → 82:3', 'kural': "okuma — lemma 'feccara': 1P etken, yerden pınarlar / edilgen, denizler", 'not': 'lemma eşi.'},
 {'bag': '81:14 → 82:5', 'kural': "okuma — harekesiz ''alimet nefs' korpusun iki ayeti, ardışık iki sûrede şart dizisinin cevabı: 'mâ ahdarat' / 'mâ qaddemet ve axxarat' (aday 1040, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '75:13 → 82:5', 'kural': "okuma — 'qaddeme ve axxara' çifti: insana haber verilir / can bilir", 'not': 'kalıp eşi.'},
 {'bag': '81:19 → 82:6', 'kural': "okuma — ardışık sûrede 'kerîm': elçi / Rab (aday 1040 ailesi)", 'not': 'lemma eşi.'},
 {'bag': '31:33 → 82:6', 'kural': "okuma — 'ğarra' + 'bi' + ilâhî gönderge: 'bi'llâh' / 'bi-rabbike'l-kerîm'", 'not': 'kalıp eşi.'},
 {'bag': '18:37 → 82:7', 'kural': "okuma — 'ellezî xalaqaka' + 2MS 'sevvâke': aşamalar (toprak, nutfe) adlı / aşama adsız, ''adeleke' ile", 'not': 'kalıp eşi.'},
 {'bag': '75:38 → 82:7', 'kural': "okuma — 'fe-xalaqa fe-sevvâ' sırası: 3MS / 2MS nesneli (ikisi L1)", 'not': 'kurgu eşi.'},
 {'bag': '40:64 → 82:8', 'kural': "okuma — lemma 'sûra' (3 ayet): 2MP 'savvera … suver' / 2MS 'sûra … rakkebe'", 'not': 'lemma eşi.'},
 {'bag': '64:3 → 82:8', 'kural': "okuma — lemma 'sûra': 'savverakum fe-ahsene suverakum' / 'fî eyyi sûratin'", 'not': 'lemma eşi.'},
 {'bag': '74:53 → 82:9', 'kural': "okuma — harekesiz 'kellâ bel' (6 ayet): âhiretten korkmuyorlar / dini yalanlıyorsunuz", 'not': 'kalıp eşi.'},
 {'bag': '82:3 → 82:5', 'kural': "sûre içi — 'izâ' şart dizisi (82:1-4) / tek cevap", 'not': 'sûre içi eş.'},
 # blok 11-19
 {'bag': '82:6 → 82:11', 'kural': "sûre içi — kök كرم [2/2]: 'rabbike'l-kerîm' (İLÂHÎ) / 'kirâmen kâtibîn' (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '80:16 → 82:11', 'kural': "okuma — 'kirâm' yazıcıların sıfatı (iki sûre önce): 'kirâmin berara' / 'kirâmen kâtibîn'", 'not': 'lemma eşi.'},
 {'bag': '82:5 → 82:12', 'kural': "sûre içi — kök علم [2/2]: can bilir / yazıcılar bilir", 'not': 'sûre içi eş.'},
 {'bag': '76:5 → 82:13', 'kural': "okuma — 'inne'l-ebrâr' açılışı: içecek / nimet", 'not': 'kalıp eşi.'},
 {'bag': '82:13 → 82:14', 'kural': "sûre içi — aynı iskelet, iyiler / günahkârlar, nimet / cehennem (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '38:28 → 82:14', 'kural': "okuma — lemma 'fuccâr': sakınanlar / günahkârlar soru içinde / iyiler / günahkârlar iki ayette", 'not': 'lemma eşi.'},
 {'bag': '80:42 → 82:14', 'kural': "okuma — lemma 'fuccâr' (iki sûre önce): 'el-kefaratu'l-fecera' / 'el-fuccâr'", 'not': 'lemma eşi.'},
 {'bag': '82:3 → 82:14', 'kural': "sûre içi — kök فجر [2/2]: denizler fışkırtıldı / günahkârlar (1021)", 'not': 'sûre içi eş.'},
 {'bag': '1:4 → 82:15', 'kural': "okuma — harekesiz 'yevme'd-dîn' (13 ayet); 1:4 kök ملك + din günü / 82:19 can bir cana malik değil", 'not': 'kalıp eşi.'},
 {'bag': '69:3 → 82:17', 'kural': "okuma — 've mâ edrâke mâ' + âhiret adı: 'el-hâqqa' / 'yevmu'd-dîn'", 'not': 'kalıp eşi.'},
 {'bag': '77:14 → 82:17', 'kural': "okuma — 've mâ edrâke mâ yevmu' + ad: 'el-fasl' / 'ed-dîn'", 'not': 'kalıp eşi.'},
 {'bag': '82:17 → 82:18', 'kural': "ölçüm esit2 BENZER + nakarat3 — 've / thumme mâ edrâke mâ yevmu'd-dîn'", 'not': 'sûre içi eş.'},
 {'bag': '82:8 → 82:19', 'kural': "sûre içi — kök شيأ [2/2]: 'mâ şâ'e' / 'şey'â' (1021)", 'not': 'sûre içi eş.'},
 {'bag': '81:29 → 82:19', 'kural': "okuma — ardışık iki sûre lafızla biten ayetle kapanıyor (aday 1040 ailesi)", 'not': 'kurgu eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_infitar', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in INFITAR]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_infitar'] = INFITAR
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_infitar', len(INFITAR), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_infitar', len(BAGLAR['AS_infitar']))
