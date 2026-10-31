# -*- coding: utf-8 -*-
"""aday_ekle_87_ala.py — sûre 87 (A'lâ) adayları (AX_ala) ve okuma bağları (AS_ala).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

ALA = [
]

BAGLAR = {"AS_ala": [
 # blok 1-8
 {'bag': '86:17 → 87:1', 'kural': "okuma — ardışık sûre sınırı: 2MS'ye emir ile kapanış ('mehhil', 'emhil') / 2MS'ye emir ile açılış ('sebbih'); 86 lafızsız ve Rabsız, 87:1 Rab; fâsıla ا → ى (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '56:74 → 87:1', 'kural': "ölçüm xref — 'fe-sebbih bi-smi rabbike'l-'azîm' / 'sebbihi'sme rabbike'l-a'lâ': 'fe' ve 'bi' yok, 'ism' ACC, sıfat farklı", 'not': 'xref eşi.'},
 {'bag': '56:96 → 87:1', 'kural': "ölçüm xref — 56:74 ile aynı", 'not': 'xref eşi.'},
 {'bag': '69:52 → 87:1', 'kural': "ölçüm xref — 56:74 ile aynı", 'not': 'xref eşi.'},
 {'bag': '55:78 → 87:1', 'kural': "okuma — harekesiz 'isme rabbik': adın kutlanması (ad özne) / adın tesbihi (ad nesne)", 'not': 'kalıp eşi.'},
 {'bag': '73:8 → 87:1', 'kural': "okuma — harekesiz 'isme rabbik' + 2MS'ye emir: anma / tesbih", 'not': 'kalıp eşi.'},
 {'bag': '76:25 → 87:1', 'kural': "okuma — harekesiz 'isme rabbik' + 2MS'ye emir: anma / tesbih", 'not': 'kalıp eşi.'},
 {'bag': '79:24 → 87:1', 'kural': "okuma — 'rabb' + 'a'lâ': bir kişinin kendisi için iddiası ('qâle' ile) / 2MS'nin Rabbi (aday 1041 ailesi, sûreler arası)", 'not': 'tamlama eşi.'},
 {'bag': '53:7 → 87:1', 'kural': "okuma — lemma 'a'lâ': ufuk / Rab", 'not': 'lemma eşi.'},
 {'bag': '75:38 → 87:2', 'kural': "okuma — önekli kalıp 'xalaqa fe-sevvâ' korpusun iki ayeti: ara aşama ('alaqa) adlı / nesnesiz", 'not': 'kalıp eşi.'},
 {'bag': '82:7 → 87:2', 'kural': "okuma — 'ellezî' + 'xalaqa' + 'fe-sevvâ': 2MS nesne zamirli, üç fiil / nesnesiz, iki fiil", 'not': 'kurgu eşi.'},
 {'bag': '80:19 → 87:3', 'kural': "okuma — lemma 'qaddara': 'xalaqahû fe-qaddarah' (nutfe adlı) / 'qaddara fe-hedâ' (nesnesiz)", 'not': 'lemma eşi.'},
 {'bag': '20:50 → 87:3', 'kural': "okuma — 'ellezî' + verme / ölçü + 'hedâ': 'qâle' ile işaretli söz içinde 'thumme hedâ' / anlatıcı sesinde 'fe-hedâ'", 'not': 'kurgu eşi.'},
 {'bag': '87:2 → 87:3', 'kural': "sûre içi — ilgi zamiri + fiil + 'fe' + fiil, nesnesiz (kalıp eşi; 'ellezî' dizisi 87:2-4)", 'not': 'sûre içi eş.'},
 {'bag': '79:31 → 87:4', 'kural': "okuma — lemma 'mer'â' korpusun iki ayeti, ikisinde de 'axraca' 3MS: yerden su ve otlak / otlak", 'not': 'lemma eşi.'},
 {'bag': '23:41 → 87:5', 'kural': "okuma — lemma 'ğuthâ'' korpusun iki ayeti, ikisinde de 'fe-ce'ale' + zamir: 1P + helak edilen kavim / 3MS + otlak", 'not': 'lemma eşi.'},
 {'bag': '87:4 → 87:5', 'kural': "sûre içi — otlak çıkarılır / çerçöp kılınır ('fe' ile sıralı; 'hû' en yakın ad 'el-mer'â')", 'not': 'sûre içi eş.'},
 {'bag': '75:17 → 87:6', 'kural': "okuma — 1P + kök قرأ: toplamak ve okutmak bize düşer / okutacağız", 'not': 'kök eşi.'},
 {'bag': '75:18 → 87:6', 'kural': "okuma — 1P + kök قرأ + 2MS: okunuşu izle (emir) / unutmayacaksın (olumsuz haber)", 'not': 'kök eşi.'},
 {'bag': '87:6 → 87:7', 'kural': "sûre içi — 'fe-lâ tensâ' + istisna 'illâ mâ şâ'a'llâh'; 1P konuşandan lafza (iltifât, aynılık metinde işaretli değil)", 'not': 'sûre içi eş.'},
 {'bag': '21:110 → 87:7', 'kural': "okuma — harekesiz 'innehû ya'lemu'l-cehr' korpusun iki ayeti: sözün açığı + 2MP'nin gizlediği / açık + gizli kalan", 'not': 'kalıp eşi.'},
 {'bag': '80:20 → 87:8', 'kural': "okuma — lemma 'yessara': 3MS + 'es-sebîl' + 3MS zamir / 1P + 2MS zamir + 'li'l-yusrâ'", 'not': 'lemma eşi.'},
 {'bag': '87:6 → 87:8', 'kural': "sûre içi — 1P fiil + 2MS nesne zamiri: okutacağız / kolaylaştıracağız", 'not': 'sûre içi eş.'},
 # blok 9-19
 {'bag': '51:55 → 87:9', 'kural': "okuma — 'zekkir' + 'zikrâ' + 'nefe'a': 'fe-inne' gerekçesi, fayda inananlara / şart 'in'", 'not': 'kurgu eşi.'},
 {'bag': '80:4 → 87:9', 'kural': "okuma — 'zikrâ' + 'nefe'a': 'fe' ile sonuç / şart 'in'", 'not': 'kurgu eşi.'},
 {'bag': '80:4 → 87:10', 'kural': "okuma — aynı biçim 'yezzekkeru' 3MS: 'ev' ile / 'se' ile gelecek, öznesi 'men yaxşâ'", 'not': 'biçim eşi.'},
 {'bag': '87:10 → 87:11', 'kural': "sûre içi — öğüt alır / öğütten kaçınır: 'men yaxşâ' / 'el-eşqâ' (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '84:12 → 87:12', 'kural': "okuma — lemma 'yaslâ' 3MS: nekre 'se'îr' / belirli 'en-nâra'l-kubrâ'", 'not': 'lemma eşi.'},
 {'bag': '87:2 → 87:12', 'kural': "sûre içi — ilgi zamiri 'ellezî' (87:2-4) Rab / en bedbaht (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '20:74 → 87:13', 'kural': "okuma — harekesiz 'lâ yemûtu fîhâ ve lâ yahyâ' korpusun iki ayeti: cehennem, Rabbine suçlu gelen / en büyük ateş, en bedbaht", 'not': 'kalıp eşi.'},
 {'bag': '79:18 → 87:14', 'kural': "okuma — lemma 'tezekkâ': 'qul' ile işaretli söz içinde soru, 2MS / 'men' ile genel, PERF", 'not': 'lemma eşi.'},
 {'bag': '87:11 → 87:14', 'kural': "sûre içi — en bedbaht / arınan (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '87:10 → 87:14', 'kural': "sûre içi — 'men' + fiil: korkan / arınan", 'not': 'sûre içi eş.'},
 {'bag': '73:8 → 87:15', 'kural': "ölçüm xref — 'isme rabb' + anma: 2MS'ye emir / 3MS haber", 'not': 'xref eşi.'},
 {'bag': '76:25 → 87:15', 'kural': "ölçüm xref — 73:8 ile aynı", 'not': 'xref eşi.'},
 {'bag': '87:1 → 87:15', 'kural': "sûre içi — 'isme rabb' + zamir: 2MS emir (tesbih) / 3MS haber (anma); sûrenin iki Rab'ı", 'not': 'sûre içi eş.'},
 {'bag': '79:38 → 87:16', 'kural': "ölçüm xref — 'âthera'l-hayâte'd-dunyâ': 3MS PERF, şart dizisi içinde / 2MP IMPF, 'bel' ile", 'not': 'xref eşi.'},
 {'bag': '42:36 → 87:17', 'kural': "okuma — harekesiz 'xayrun ve ebqâ' + 'el-hayâtu'd-dunyâ' ile karşılaştırma: Allah katında olan / âhiret", 'not': 'kalıp eşi.'},
 {'bag': '87:16 → 87:17', 'kural': "sûre içi — dünya hayatı / âhiret (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '20:133 → 87:18', 'kural': "okuma — harekesiz 'es-suhufi'l-ûlâ' korpusun iki ayeti: 'qâlû' sözünün ardından soru / tekitli haber", 'not': 'kalıp eşi.'},
 {'bag': '53:36 → 87:19', 'kural': "okuma — 'suhuf' + Mûsâ ve İbrâhîm: sıra Mûsâ → İbrâhîm, iki ayette (53:37) / İbrâhîm → Mûsâ, tek ayette", 'not': 'kurgu eşi.'},
 {'bag': '53:37 → 87:19', 'kural': "okuma — İbrâhîm ilgi zamiriyle nitelenmiş ('ellezî veffâ') / niteleme yok", 'not': 'kurgu eşi.'},
 {'bag': '87:18 → 87:19', 'kural': "sûre içi — lemma 'suhuf' [2/2]: 'es-suhufi'l-ûlâ' / bedel 'suhufi ibrâhîme ve mûsâ'", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_ala', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in ALA]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_ala'] = ALA
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_ala', len(ALA), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_ala', len(BAGLAR['AS_ala']))
