# -*- coding: utf-8 -*-
"""aday_ekle_89_fecr.py — sûre 89 (Fecr) adayları (AX_fecr) ve okuma bağları (AS_fecr).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

FECR = [
]

BAGLAR = {"AS_fecr": [
 # blok 1-14
 {'bag': '88:26 → 89:1', 'kural': "okuma — ardışık sûre sınırı: 1P konuşanın hesap sözü ile kapanış / yemin ile açılış; fâsıla م → ر (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '81:17 → 89:4', 'kural': "okuma — harekesiz 've'l-leyli izâ' + fiil: kararıp gelme / yürüyüp gitme", 'not': 'kalıp eşi.'},
 {'bag': '89:2 → 89:4', 'kural': "sûre içi — kök ليل [2/2]: on gece / yürüyüp giden gece", 'not': 'sûre içi eş.'},
 {'bag': '56:76 → 89:5', 'kural': "okuma — lemma 'qasem' korpusun iki ayeti: büyük bir yemin (tekit) / akıl sahibi için yemin var mı (soru)", 'not': 'lemma eşi.'},
 {'bag': '38:12 → 89:6', 'kural': "okuma — ''Âd' ve 'Firavun zu'l-evtâd' aynı ayette (NOM) / 89:6 ve 89:10'da ayrı ayetlerde (GEN)", 'not': 'kurgu eşi.'},
 {'bag': '38:12 → 89:10', 'kural': "okuma — 'fir'avn' + 'zû' + 'el-evtâd': NOM / GEN (harekesiz 'zû' / 'zî' kalıbı ayırıyor)", 'not': 'kalıp eşi.'},
 {'bag': '78:7 → 89:10', 'kural': "okuma — lemma 'evtâd': dağlar kazık / Firavun'un kazıkları", 'not': 'lemma eşi.'},
 {'bag': '89:8 → 89:11', 'kural': "sûre içi — 'fi'l-bilâd' [2/2]: benzeri yaratılmamış / azdılar", 'not': 'sûre içi eş.'},
 {'bag': '80:25 → 89:13', 'kural': "okuma — lemma 'sabbe': 1P su döker / Rab azap kamçısı döker", 'not': 'lemma eşi.'},
 {'bag': '44:48 → 89:13', 'kural': "okuma — lemma 'sabbe' + azap: edilgen emir / Rab etken", 'not': 'lemma eşi.'},
 {'bag': '78:21 → 89:14', 'kural': "okuma — lemma 'mirsâd' korpusun iki ayeti: 'inne' + cehennem + 'kânet mirsâdâ' / 'inne' + Rab + 'le-bi'l-mirsâd'", 'not': 'lemma eşi.'},
 {'bag': '89:1 → 89:14', 'kural': "sûre içi — yemin dizisi (89:1-4) / cevap olarak okunabilen tekitli haber (KAPATILAMAZ)", 'not': 'sûre içi eş.'},
 {'bag': '89:6 → 89:13', 'kural': "sûre içi — Rab + kavimler: nasıl davrandı (soru) / azap kamçısı döktü (cevap)", 'not': 'sûre içi eş.'},
 # blok 15-20
 {'bag': '76:2 → 89:15', 'kural': "okuma — lemma 'ibtelâ' + insan: 1P sınama + yaratma / Rab sınar + ikram", 'not': 'lemma eşi.'},
 {'bag': '12:21 → 89:15', 'kural': "okuma — lemma 'ekrame': 'qâle' sözü içinde emir / Rab ikram eder", 'not': 'lemma eşi.'},
 {'bag': '89:15 → 89:16', 'kural': "sûre içi — 'izâ mâ ibtelâhu' + 'fe-yeqûlu rabbî' + PERF 1S: ikram etti / alçalttı (aday 1039, okuma; nakarat3 sûre içi)", 'not': 'sûre içi eş.'},
 {'bag': '22:18 → 89:16', 'kural': "okuma — kök هون + كرم: Allah alçaltırsa ikram eden yok / insanın sözünde 'ehânen' (89:15 'ekramen'); lemma 'ehâne' korpusun iki ayeti", 'not': 'kurgu eşi.'},
 {'bag': '89:15 → 89:17', 'kural': "sûre içi — kök كرم [3/3]: Rab ikram eder / siz yetime ikram etmezsiniz (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '74:53 → 89:17', 'kural': "okuma — 'kellâ bel lâ' + IMPF: 3MP âhiretten korkmuyor / 2MP yetime ikram etmiyor", 'not': 'kalıp eşi.'},
 {'bag': '69:34 → 89:18', 'kural': "ölçüm esit2 BENZER — ''alâ ta'âmi'l-miskîn': 3MS 'yehuddu' / 2MP VI. bab 'tehâddûne'", 'not': 'esit2 eşi.'},
 {'bag': '76:8 → 89:18', 'kural': "okuma — yoksul + yetim + yiyecek: sevgiye rağmen yedirenler / yetime ikram etmeyen, yoksulu doyurmaya özendirmeyenler", 'not': 'kurgu eşi.'},
 {'bag': '76:8 → 89:20', 'kural': "okuma — lemma 'hubb': yiyeceğe sevgiye rağmen yedirme / malı pek sevme", 'not': 'lemma eşi.'},
 {'bag': '89:19 → 89:20', 'kural': "sûre içi — 've' + IMPF 2MP + belirli ad + mastar + sıfat: mirası yeme / malı sevme", 'not': 'sûre içi eş.'},
 # blok 21-30
 {'bag': '75:26 → 89:21', 'kural': "okuma — harekesiz 'kellâ izâ' korpusun iki ayeti: 'izâ' + PERF 3FS / 'izâ' + edilgen PERF 3FS", 'not': 'kalıp eşi.'},
 {'bag': '69:14 → 89:21', 'kural': "okuma — lemma 'dukket' korpusun iki ayeti: yer + dağlar, tek çarpış / yer, mastar art arda iki kez", 'not': 'lemma eşi.'},
 {'bag': '89:17 → 89:21', 'kural': "sûre içi — 'kellâ' [2/2]: suç dizisini açar / o günü açar", 'not': 'sûre içi eş.'},
 {'bag': '78:38 → 89:22', 'kural': "okuma — lemma 'saff' + melek: çoğul 'el-melâ'ike' + 'saffâ' / tekil 'el-melek' + 'saffen saffâ'", 'not': 'lemma eşi.'},
 {'bag': '89:21 → 89:22', 'kural': "sûre içi — mastar art arda iki kez: 'dakkan dakkâ' / 'saffen saffâ'", 'not': 'sûre içi eş.'},
 {'bag': '89:22 → 89:23', 'kural': "sûre içi — lemma 'câ'e': Rab gelir (etken) / cehennem getirilir (edilgen)", 'not': 'sûre içi eş.'},
 {'bag': '79:35 → 89:23', 'kural': "ölçüm xref — harekesiz 'yetezekkeru'l-insân' korpusun iki ayeti: çabasını hatırlar / hatırlama + 'ennâ' sorusu", 'not': 'xref eşi.'},
 {'bag': '89:15 → 89:23', 'kural': "sûre içi — kök أنس [2/2]: sınanan insan / hatırlayan insan", 'not': 'sûre içi eş.'},
 {'bag': '69:25 → 89:24', 'kural': "okuma — 'yeqûlu' + 'yâ leytenî': kitabı solundan verilen / insan", 'not': 'kalıp eşi.'},
 {'bag': '78:40 → 89:24', 'kural': "okuma — 'qaddeme' + 'yâ leytenî': aynı ayette iki cümle / tek cümlede 'yâ leytenî qaddemtu'", 'not': 'kalıp eşi.'},
 {'bag': '89:13 → 89:25', 'kural': "sûre içi — lemma ''azâb': Rab azap kamçısı döker / 'lâ yu'azzibu 'azâbehû ehad'", 'not': 'sûre içi eş.'},
 {'bag': '89:25 → 89:26', 'kural': "sûre içi — 'lâ' + IMPF + aynı kökten ad + 3MS + 'ehad' (mm2): azap etme / bağlama; 3MS gönderge KAPATILAMAZ", 'not': 'sûre içi eş.'},
 {'bag': '47:4 → 89:26', 'kural': "okuma — lemma 'vethâq' korpusun iki ayeti: 2MP emir, bağı sıkı tutma / 'lâ' + 'ehad'", 'not': 'lemma eşi.'},
 {'bag': '16:112 → 89:27', 'kural': "okuma — lemma 'mutma'inne' korpusun iki ayeti: huzurlu belde nimeti inkâr eder / huzurlu nefse hitap", 'not': 'lemma eşi.'},
 {'bag': '75:30 → 89:28', 'kural': "okuma — harekesiz 'ilâ rabbike': o gün sevk / 2FS dönüş emri", 'not': 'kalıp eşi.'},
 {'bag': '69:21 → 89:28', 'kural': "okuma — lemma 'râdıye': hoşnut yaşayış / razı nefis", 'not': 'lemma eşi.'},
 {'bag': '88:9 → 89:28', 'kural': "okuma — lemma 'râdıye': çabasından hoşnut / razı ve razı olunmuş", 'not': 'lemma eşi.'},
 {'bag': '89:29 → 89:30', 'kural': "sûre içi — 'udxulî' + 1S iyelik: kullarım / cennetim", 'not': 'sûre içi eş.'},
 {'bag': '89:25 → 89:30', 'kural': "sûre içi — azap / cennet (aday 1039, okuma)", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_fecr', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in FECR]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_fecr'] = FECR
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_fecr', len(FECR), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_fecr', len(BAGLAR['AS_fecr']))
