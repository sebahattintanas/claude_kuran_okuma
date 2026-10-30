# -*- coding: utf-8 -*-
"""aday_ekle_84_insikak.py — sûre 84 (İnşikâk) adayları (AX_insikak) ve okuma bağları (AS_insikak).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

INSIKAK = [
]

BAGLAR = {"AS_insikak": [
 # blok 1-9
 {'bag': '83:36 → 84:1', 'kural': "okuma — ardışık sûre sınırı: soru + 3MP ile kapanış / şart zarfı + 3FS ile açılış; ikisi de lafızsız, Rabsız; fâsıla ن → ت (aday 1040, kayıt)", 'not': 'sınır.'},
 {'bag': '82:1 → 84:1', 'kural': "okuma — harekesiz 'ize's-semâ'' korpusun iki ayeti: VII. bab PERF 3FS, kök فطر / kök شقق", 'not': 'kalıp eşi.'},
 {'bag': '69:16 → 84:1', 'kural': "okuma — lemma 'inşaqqa' + 'es-semâ'': göğün yarılması", 'not': 'lemma eşi.'},
 {'bag': '55:37 → 84:1', 'kural': "okuma — 'izâ' + lemma 'inşaqqa' + 'es-semâ''", 'not': 'lemma eşi.'},
 {'bag': '19:90 → 84:1', 'kural': "okuma — lemma 'inşaqqa': orada yer / burada gök", 'not': 'lemma eşi.'},
 {'bag': '54:1 → 84:1', 'kural': "okuma — lemma 'inşaqqa': orada ay / burada gök", 'not': 'lemma eşi.'},
 {'bag': '84:2 → 84:5', 'kural': "ölçüm esit2 TAM — 've ezinet li-rabbihâ ve huqqat': gök / yer (3FS, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '84:1 → 84:3', 'kural': "sûre içi — 'izâ' + belirli ad + fiil: gök yarıldığında / yer uzatıldığında (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '15:19 → 84:3', 'kural': "okuma — kök مدد + kök لقي + 'fîhâ': 1P yeri uzattık ve içine attık / yer edilgen uzatılır ve içindekini atar (84:3-4)", 'not': 'kurgu eşi.'},
 {'bag': '50:7 → 84:3', 'kural': "okuma — kök مدد + kök لقي + 'fîhâ' (15:19 ile aynı ilk dört kelime): içine atılan / içinden atılan", 'not': 'kurgu eşi.'},
 {'bag': '84:4 → 84:6', 'kural': "sûre içi — kök لقي [2/2]: 'elqat' atma / 'mulâqî' karşılaşma (1021)", 'not': 'sûre içi eş.'},
 {'bag': '82:6 → 84:6', 'kural': "okuma — harekesiz 'yâ eyyuhe'l-insân' korpusun iki ayeti, ikisinde de 'rabbike': soru / haber", 'not': 'kalıp eşi.'},
 {'bag': '62:8 → 84:6', 'kural': "okuma — lemma 'mulâqî' korpusun iki ayeti: ölüm sizinle karşılaşacak / sen onunla karşılaşacaksın", 'not': 'lemma eşi.'},
 {'bag': '69:19 → 84:7', 'kural': "ölçüm lemma dizisi — 'fe-emmâ men ûtiye kitâbehû bi-yemînih': devamı kişinin sözü / hesap ve dönüş", 'not': 'kalıp eşi.'},
 {'bag': '17:71 → 84:7', 'kural': "ölçüm xref — 'men ûtiye kitâbehû bi-yemînih': kitaplarını okurlar / kolay hesap", 'not': 'kalıp eşi.'},
 {'bag': '65:8 → 84:8', 'kural': "okuma — lemma 'hâsebe' + 'hisâben' + sıfat: 1P etken, 'şedîd' / edilgen, 'yesîr'", 'not': 'lemma eşi.'},
 {'bag': '83:31 → 84:9', 'kural': "okuma — ardışık sûrede 'inqalebe' + 'ilâ ehl' + hâl: keyifli (dünya) / sevinçli (âhiret) (aday 1040 ailesi)", 'not': 'kalıp eşi.'},
 # blok 10-15
 {'bag': '84:7 → 84:10', 'kural': "sûre içi — 'men ûtiye kitâbehû' + sağından / sırtının arkasından; كتب [2/2], أتي [2/2] (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '69:25 → 84:10', 'kural': "okuma — 've emmâ men ûtiye kitâbehû' + ikinci kol: soldan / sırtının arkasından (69:19 / 69:25 ↔ 84:7 / 84:10)", 'not': 'kalıp eşi.'},
 {'bag': '84:8 → 84:11', 'kural': "sûre içi — 'fe-sevfe' + fiil: kolay hesap (edilgen) / helâk çağırma (etken) (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '25:13 → 84:11', 'kural': "okuma — 'de'â' + lemma 'thubûr': ateşe atılanlar (3MP) / 3MS", 'not': 'lemma eşi.'},
 {'bag': '25:14 → 84:11', 'kural': "okuma — 'de'â' + lemma 'thubûr' (korpusun üç ayetinin biri; iki kez)", 'not': 'lemma eşi.'},
 {'bag': '82:15 → 84:12', 'kural': "okuma — lemma 'yaslâ': 3MP + cahîm zamiri / 3MS + 'se'îr'", 'not': 'lemma eşi.'},
 {'bag': '83:16 → 84:12', 'kural': "okuma — ardışık sûrede kök صلي: ortaç 'sâlu'l-cahîm' / fiil 'yaslâ se'îrâ' (aday 1040 ailesi)", 'not': 'kök eşi.'},
 {'bag': '84:9 → 84:13', 'kural': "sûre içi — 'ehlihî mesrûrâ' fâsılada: âhirette sevinçli dönüş / dünyada sevinç; lemma 'mesrûr' korpusun iki ayeti, أهل [2/2], سرر [2/2] (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '83:31 → 84:13', 'kural': "okuma — ardışık sûrede dünyada aile yanında keyif ('fekihîn') / sevinç ('mesrûrâ') (aday 1040 ailesi)", 'not': 'kurgu eşi.'},
 {'bag': '83:4 → 84:14', 'kural': "okuma — ardışık sûrede 'zanne' + diriliş: soru / sanmıştı (aday 1040 ailesi)", 'not': 'kurgu eşi.'},
 {'bag': '64:7 → 84:14', 'kural': "okuma — harekesiz 'en len' + diriliş ve ardından 'belâ': 'qul belâ ve rabbî' / 'belâ inne rabbehû' (84:14-15)", 'not': 'kalıp eşi.'},
 {'bag': '72:7 → 84:14', 'kural': "okuma — 'zanne' + 'en len' + diriliş / dönüş", 'not': 'kalıp eşi.'},
 {'bag': '17:96 → 84:15', 'kural': "okuma — 'innehû kâne bi' + ad + 'basîr': kulları / 'bihî'", 'not': 'kalıp eşi.'},
 {'bag': '84:14 → 84:15', 'kural': "sûre içi — 'len yehûr' / 'belâ': sanı ve reddi (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 # blok 16-25
 {'bag': '81:15 → 84:16', 'kural': "okuma — harekesiz 'fe-lâ uqsimu' (korpus 5): adsız ortaç / şafak; üç sûre önce", 'not': 'kalıp eşi.'},
 {'bag': '56:75 → 84:16', 'kural': "okuma — 'fe-lâ uqsimu' + 'bi': yıldızların düştüğü yerler / şafak", 'not': 'kalıp eşi.'},
 {'bag': '69:38 → 84:16', 'kural': "okuma — 'fe-lâ uqsimu' + 'bi': gördükleriniz / şafak", 'not': 'kalıp eşi.'},
 {'bag': '70:40 → 84:16', 'kural': "okuma — 'fe-lâ uqsimu' + 'bi': doğuların ve batıların Rabbi / şafak", 'not': 'kalıp eşi.'},
 {'bag': '75:1 → 84:16', 'kural': "okuma — 'lâ uqsimu' ('fe' yok): kıyamet günü / şafak", 'not': 'kalıp eşi.'},
 {'bag': '81:17 → 84:17', 'kural': "okuma — 've'l-leyli' + fiil, yemin: ''as'as' / 'mâ vesaq'", 'not': 'kurgu eşi.'},
 {'bag': '81:18 → 84:18', 'kural': "okuma — yemin edilen + 'izâ' + fiil: sabah / ay", 'not': 'kurgu eşi.'},
 {'bag': '84:17 → 84:18', 'kural': "sûre içi — kök وسق korpusun iki ayeti: 'vesaqa' / 'ittesaqa' [2/2]", 'not': 'sûre içi eş.'},
 {'bag': '67:3 → 84:19', 'kural': "okuma — kök طبق: 'tıbâq' yedi göğün katları / 'tabaqan 'an tabaq'", 'not': 'kök eşi.'},
 {'bag': '71:15 → 84:19', 'kural': "okuma — kök طبق: 'seb'a semâvâtin tıbâqâ' / insanların bineceği katlar", 'not': 'kök eşi.'},
 {'bag': '57:8 → 84:20', 'kural': "okuma — lemma dizisi 'mâ' + 'li' + zamir + 'lâ' + 'âmene': 2MP + 'bi'llâh' / 3MP, nesnesiz", 'not': 'lemma eşi.'},
 {'bag': '31:7 → 84:21', 'kural': "okuma — okunma ('tutlâ' / 'quri'e') + yüz çevirme / secde etmeme + 'fe-beşşir … bi-'azâbin elîm' (84:24)", 'not': 'kurgu eşi.'},
 {'bag': '45:8 → 84:24', 'kural': "okuma — lemma dizisi 'beşşere' + ''azâb' + 'elîm': 3MS / 3MP; önce okunma ve yüz çevirme", 'not': 'lemma eşi.'},
 {'bag': '70:18 → 84:23', 'kural': "okuma — lemma 'ev'â' korpusun iki ayeti: toplayıp biriktiren / biriktirdikleri", 'not': 'lemma eşi.'},
 {'bag': '41:8 → 84:25', 'kural': "ölçüm esit2 YAKIN + xref — 'inne'llezîne' / 'illa'llezîne' + 'âmenû ve 'amilu's-sâlihâti lehum ecrun ğayru memnûn'", 'not': 'kalıp eşi.'},
 {'bag': '68:3 → 84:25', 'kural': "okuma — lemma 'memnûn' + 'ecr' + 'ğayr': 2MS için / iman edip salih iş yapanlar için", 'not': 'lemma eşi.'},
 {'bag': '84:20 → 84:25', 'kural': "sûre içi — kök أمن [2/2]: iman etmiyorlar / iman edenler (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '84:24 → 84:25', 'kural': "sûre içi — acı azap / kesintisiz karşılık (aday 1039, okuma)", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_insikak', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in INSIKAK]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_insikak'] = INSIKAK
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_insikak', len(INSIKAK), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_insikak', len(BAGLAR['AS_insikak']))
