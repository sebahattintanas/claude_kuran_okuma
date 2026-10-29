# -*- coding: utf-8 -*-
"""aday_ekle_80_abese.py — sûre 80 ('Abese) adayları (AX_abese) ve okuma bağları (AS_abese).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

ABESE = [
]

BAGLAR = {"AS_abese": [
 # blok 1-10
 {'bag': '79:46 → 80:1', 'kural': "okuma — ardışık sûre sınırı: 3MP + saat ile kapanış / 3MS iki fiille açılış; fâsıla ا → ى (aday 1040, kayıt)", 'not': 'sınır.'},
 {'bag': '74:22 → 80:1', 'kural': "okuma — lemma ''abese' korpusun iki ayeti: 'thumme' + 'besera' / 've tevellâ'", 'not': 'lemma eşi.'},
 {'bag': '33:63 → 80:3', 'kural': "okuma — harekesiz 've mâ yudrîke' + 'le'alle' (33:63, 42:17, 80:3): saat yakın olabilir / o arınabilir", 'not': 'kalıp eşi.'},
 {'bag': '79:18 → 80:3', 'kural': "okuma — ardışık sûrede lemma 'tezekkâ': Fir'avn'a soru / körün arınma ihtimali (aday 1040 ailesi, kayıt)", 'not': 'lemma eşi.'},
 {'bag': '79:43 → 80:4', 'kural': "okuma — ardışık sûrede lemma 'zikrâ': saatin anılması / öğüt (aday 1040 ailesi, kayıt)", 'not': 'lemma eşi.'},
 {'bag': '79:37 → 80:5', 'kural': "okuma — ardışık sûrede 'emmâ men' tafsîli (79:37, 40 / 80:5, 8) (aday 1040 ailesi, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '80:6 → 80:10', 'kural': "sûre içi — 'fe-ente' + edat + 3MS + V. bab fiil: 'lehû tesaddâ' / ''anhu telehhâ' (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '80:3 → 80:7', 'kural': "sûre içi — lemma 'tezekkâ': arınma ihtimali / arınmaması (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '80:5 → 80:8', 'kural': "sûre içi — 'emmâ' tafsîlinin iki kolu: yeterli gören / koşarak gelen (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '79:22 → 80:8', 'kural': "okuma — ardışık sûrede 'yes'â': sırt dönüp koşmak / gelip koşmak (aday 1040 ailesi, kayıt)", 'not': 'lemma eşi.'},
 {'bag': '79:45 → 80:9', 'kural': "okuma — ardışık sûrede lemma 'xaşiye' + 2MS muhatap: 'men yaxşâhâ' / 've huve yaxşâ' (aday 1040 ailesi, kayıt)", 'not': 'lemma eşi.'},
 # blok 11-20
 {'bag': '74:54 → 80:11', 'kural': "okuma — 'kellâ inne… tezkira': 'innehû' (3MS) / 'innehâ' (3FS)", 'not': 'kalıp eşi.'},
 {'bag': '74:55 → 80:12', 'kural': "ölçüm esit2 TAM — 'fe-men şâ'e zekerah'; 74:54-55 zamirleri 3MS + 3MS / burada 3FS + 3MS", 'not': 'kalıp eşi.'},
 {'bag': '80:4 → 80:12', 'kural': "sûre içi — kök ذكر [4/4]: öğüt alma, öğüt / öğüt, anma", 'not': 'sûre içi eş.'},
 {'bag': '53:36 → 80:13', 'kural': "okuma — harekesiz 'fî suhuf' korpusun iki ayeti: tamlama, adlı / nekre, sıfatlı", 'not': 'kalıp eşi.'},
 {'bag': '80:13 → 80:16', 'kural': "sûre içi — kök كرم: 'mukarrama' sayfalar / 'kirâm' yazıcılar", 'not': 'sûre içi eş.'},
 {'bag': '79:35 → 80:17', 'kural': "okuma — ardışık sûrede 'el-insân' + 'mâ' (aday 1040 ailesi, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '76:2 → 80:19', 'kural': "okuma — 'min nutfa' + yaratma: 1P 'xalaqnâ' + 'emşâc' / 3MS 'xalaqahû fe-qaddarah' (ikisi L1)", 'not': 'kalıp eşi.'},
 {'bag': '76:3 → 80:20', 'kural': "okuma — 'es-sebîl' insan hakkında: 1P 'hedeynâ' / 3MS 'yessera'; 76:2-3 nutfe, sebîl, kefûr ögeleri 80:17-20'de", 'not': 'kurgu eşi.'},
 {'bag': '80:18 → 80:19', 'kural': "sûre içi — soru / cevap: 'min eyyi şey'in' / 'min nutfa'", 'not': 'sûre içi eş.'},
 # blok 21-30
 {'bag': '80:21 → 80:22', 'kural': "sûre içi — 'emâtehû' / 'enşerahû' (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '80:12 → 80:22', 'kural': "sûre içi — 'şâ'e': dileyen insan / dileyen dirilten (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '80:17 → 80:24', 'kural': "sûre içi — kök أنس [2/2]: 'qutile'l-insân' / 'fe'l-yenzuri'l-insân'", 'not': 'sûre içi eş.'},
 {'bag': '79:31 → 80:25', 'kural': "okuma — ardışık sûrede su: 3MS, yerden çıkarma / 1P, dökme (aday 1040 ailesi, kayıt)", 'not': 'kök eşi.'},
 {'bag': '78:15 → 80:27', 'kural': "okuma — 1P su + tane: 'li-nuxrice bihî' (ta'lîl, L2) / 'fe-enbetnâ fîhâ' (sıra, L1)", 'not': 'kurgu eşi.'},
 {'bag': '50:9 → 80:27', 'kural': "okuma — 'fe-enbetnâ' + tane: 'bihî' ile (L2) / 'fîhâ' ile (L1)", 'not': 'kurgu eşi.'},
 {'bag': '31:10 → 80:27', 'kural': "okuma — harekesiz 'fe-enbetnâ fîhâ' korpusun iki ayeti: 'min kulli zevcin kerîm' / 'habbâ'", 'not': 'kalıp eşi.'},
 {'bag': '16:11 → 80:29', 'kural': "okuma — zeytin, hurma, üzüm bir arada: 3MS 'yunbitu … bihî' / 1P 'enbetnâ'", 'not': 'kurgu eşi.'},
 {'bag': '78:32 → 80:30', 'kural': "okuma — lemma 'hadâ'iq' + üzüm: sakınanlara verilenler / dünya yiyeceği dizisi", 'not': 'lemma eşi.'},
 # blok 31-42
 {'bag': '79:33 → 80:32', 'kural': "ölçüm esit2 TAM — 'metâ'an lekum ve li-en'âmikum', ardışık iki sûrede yiyecek dizisinin sonu (aday 1040, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '79:34 → 80:33', 'kural': "okuma — harekesiz 'fe-izâ câ'eti' korpusun iki ayeti, ikisi de 79:33 / 80:32'nin ardından; 'et-tâmmetu'l-kubrâ' / 'es-sâxxa' (aday 1040, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '80:2 → 80:33', 'kural': "sûre içi — kök جيأ [3/3]: kör geldi / koşarak gelen / çığlık geldi", 'not': 'sûre içi eş.'},
 {'bag': '78:40 → 80:34', 'kural': "okuma — 'yevme' + 'el-mer'': bakar / kaçar (aday 1040 ailesi)", 'not': 'lemma eşi.'},
 {'bag': '70:11 → 80:34', 'kural': "okuma — âhirette yakınlar dizisi: fidye olarak verilir (oğullar, eş, kardeş) / kaçılır (kardeş, anne, baba, eş, oğullar)", 'not': 'kurgu eşi.'},
 {'bag': '70:12 → 80:36', 'kural': "okuma — 've sâhibetihî ve': 'axîh' / 'benîh'", 'not': 'kalıp eşi.'},
 {'bag': '80:5 → 80:37', 'kural': "sûre içi — kök غني: kendini yeterli gören / kendine yetecek iş", 'not': 'sûre içi eş.'},
 {'bag': '75:22 → 80:38', 'kural': "okuma — lemma dizisi 'vech + yevme'izin', iki grup yüz: 'nâdira … nâzıra' / 'musfira, dâhika, mustebşira'", 'not': 'lemma eşi.'},
 {'bag': '75:24 → 80:40', 'kural': "okuma — harekesiz 've vucûhun yevme'izin' korpusun iki ayeti: 'bâsira … fâqira' / ''aleyhâ ğabera … qatara'", 'not': 'kalıp eşi.'},
 {'bag': '80:15 → 80:38', 'kural': "sûre içi — kök سفر iki anlam: 'sefera' / 'musfira' (1021)", 'not': 'sûre içi eş.'},
 {'bag': '10:26 → 80:41', 'kural': "okuma — 'rahiqa' + 'vucûh' + kök قتر: kaplamaz (güzel davrananlar) / kaplar", 'not': 'kök eşi.'},
 {'bag': '80:17 → 80:42', 'kural': "sûre içi — kök كفر: 'mâ ekferah' (insan) / 'el-kefera'", 'not': 'sûre içi eş.'},
 {'bag': '80:38 → 80:40', 'kural': "sûre içi — iki grup yüz (aday 1039, okuma)", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_abese', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in ABESE]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_abese'] = ABESE
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_abese', len(ABESE), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_abese', len(BAGLAR['AS_abese']))
