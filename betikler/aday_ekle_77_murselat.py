# -*- coding: utf-8 -*-
"""aday_ekle_77_murselat.py — sûre 77 (Mürselât) adayları (AX_murselat) ve okuma bağları (AS_murselat).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

MURSELAT = [
]

BAGLAR = {"AS_murselat": [
 # blok 1-10
 {'bag': '76:31 → 77:1', 'kural': "okuma — ardışık sûre sınırı: rahmet / zalimlere hazırlanmış azapla kapanış (lafız zamirle) / lafızsız yeminle açılış; fâsıla ا → ا (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '75:1 → 77:1', 'kural': "okuma — ardışık üç sûrenin açılışı: 75:1 yemin ('lâ uqsimu'), 76:1 soru ('hel etâ'), 77:1 yemin (aday 1040 ailesi, kayıt)", 'not': 'sûre açılışı.'},
 {'bag': '51:1 → 77:1', 'kural': "okuma — dişil çoğul ortaç + mastar / nekre ile ardışık yeminler: 51:1-4 dört, 37:1-3 üç, 77:1-5 beş", 'not': 'kurgu eşi.'},
 {'bag': '37:3 → 77:5', 'kural': "okuma — yemin dizisinin son halkası ortaç + 'zikrâ': okuyanlar / bırakanlar", 'not': 'kalıp eşi.'},
 {'bag': '21:81 → 77:2', 'kural': "okuma — lemma ''âsifa' korpusun iki ayeti: rüzgârın sıfatı / niteleyen adsız", 'not': 'lemma eşi.'},
 {'bag': '51:5 → 77:7', 'kural': "okuma — 'innemâ tû'adûne' korpusun iki ayeti: yemin cevabı 'le-sâdiq' (51:6 'le-vâqi'') / 'le-vâqi''", 'not': 'kalıp eşi.'},
 {'bag': '52:7 → 77:7', 'kural': "okuma — lemma 'vâqi'': Rabbin azabı / vaat edilen", 'not': 'lemma eşi.'},
 {'bag': '54:37 → 77:8', 'kural': "okuma — lemma 'tamese': 1P etken, gözler (36:66, 54:37) / edilgen, yıldızlar", 'not': 'lemma eşi.'},
 {'bag': '50:6 → 77:9', 'kural': "okuma — kök فرج: göğün yarığı yok / gök yarılıyor", 'not': 'kök eşi.'},
 {'bag': '20:105 → 77:10', 'kural': "okuma — lemma 'nesefe' + dağlar: Rab etken, adlı / edilgen, savuran adsız", 'not': 'lemma eşi.'},
 # blok 11-20
 {'bag': '77:1 → 77:11', 'kural': "sûre içi — kök رسل iki ayet: 'el-murselât' (adsız gönderilenler) / 'er-rusul' (elçiler)", 'not': 'sûre içi eş.'},
 {'bag': '77:8 → 77:11', 'kural': "sûre içi — 'izâ' + ad + edilgen 3FS dört ayette (77:8-11): yıldızlar, gök, dağlar, elçiler; cevap KAPATILAMAZ", 'not': 'sûre içi eş.'},
 {'bag': '37:21 → 77:13', 'kural': "okuma — lemma dizisi 'yevm + fasl': yalanlanan gün / sorulan günün adı", 'not': 'kalıp eşi.'},
 {'bag': '44:40 → 77:13', 'kural': "okuma — 'yevmu'l-fasl': toplanma vakti / sorulan günün adı", 'not': 'kalıp eşi.'},
 {'bag': '69:3 → 77:14', 'kural': "okuma — 've mâ edrâke mâ': el-hâqqa / seqar (74:27) / yevmu'l-fasl", 'not': 'kalıp eşi.'},
 {'bag': '52:11 → 77:15', 'kural': "okuma — 'veylun yevme'izin li'l-mukezzibîn': 'fe' önekli / sûre nakaratı (77:15-49, 10 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '77:15 → 77:19', 'kural': "ölçüm esit2 TAM + nakarat3 — sûre nakaratının ilk iki geçişi", 'not': 'nakarat3.'},
 {'bag': '57:3 → 77:16', 'kural': "okuma — 'evvel / âxir': Allah için esmâ / topluluklar için çoğul (1041 ailesi, sûre dışı)", 'not': 'lemma eşi.'},
 {'bag': '56:13 → 77:16', 'kural': "okuma — 'el-evvelîn / el-âxirîn' çifti: öncekilerden çok, sonrakilerden az (56:13-14) / helâk ve ardınca götürme (77:16-17)", 'not': 'kalıp eşi.'},
 {'bag': '37:34 → 77:18', 'kural': "ölçüm esit2 BENZER — 'kezâlike nef'alu bi'l-mucrimîn': 'innâ' tekidiyle / tekitsiz", 'not': 'esit2.'},
 {'bag': '32:8 → 77:20', 'kural': "okuma — 'mâ'in mehîn' korpusun iki ayeti: 3MS, nesil, süzme ara aşaması / 1P, 2MP, ara aşama yok", 'not': 'kalıp eşi.'},
 # blok 21-30
 {'bag': '23:13 → 77:21', 'kural': "okuma — 'fî qarârin mekîn' korpusun iki ayeti: 'hu' insan + nutfe / 'hu' su, nutfe adı yok", 'not': 'kalıp eşi.'},
 {'bag': '15:21 → 77:22', 'kural': "okuma — 'qaderin ma'lûm' korpusun iki ayeti: indirilenin ölçüsü ('bi-') / sürecin bitiş sınırı ('ilâ')", 'not': 'kalıp eşi.'},
 {'bag': '51:48 → 77:23', 'kural': "okuma — 1P fiil + 'fe-ni'me' + 1P'yi niteleyen çoğul ortaç: 'el-mâhidûn' / 'el-qâdirûn'", 'not': 'kurgu eşi.'},
 {'bag': '77:22 → 77:23', 'kural': "sûre içi — kök قدر üç geçişin hepsi iki ayette: 'qader' / 'qadernâ' / 'qâdirûn'", 'not': 'sûre içi eş.'},
 {'bag': '35:22 → 77:26', 'kural': "okuma — 'ahyâ' / emvât': eşit olmama / aynı yerde toplanma (aday 1039 çifti)", 'not': 'kalıp eşi.'},
 {'bag': '72:16 → 77:27', 'kural': "okuma — lemma dizisi 'esqâ + mâ'' korpusun iki ayeti: şartlı bol su, 3MP / içirilmiş tatlı su, 2MP", 'not': 'lemma eşi.'},
 {'bag': '25:53 → 77:27', 'kural': "okuma — lemma 'furât': tatlı / tuzlu iki su / içirilen tatlı su", 'not': 'lemma eşi.'},
 {'bag': '77:20 → 77:27', 'kural': "sûre içi — kök موه iki ayet: değersiz su (yaratılış) / tatlı su (içirme)", 'not': 'sûre içi eş.'},
 {'bag': '76:21 → 77:27', 'kural': "okuma — kök سقي ardışık sûrelerde: 76:17 edilgen, 76:21 Rab, 77:27 1P", 'not': 'kök eşi.'},
 {'bag': '32:20 → 77:29', 'kural': "okuma — 'kuntum bihî tukezzibûn': ateşin azabı / ayırma günü (37:21) / adsız 'mâ'", 'not': 'kalıp eşi.'},
 {'bag': '56:43 → 77:30', 'kural': "okuma — azap sahnesinde gölge: 'min yahmûm', serinletmeyen / üç kollu", 'not': 'kurgu eşi.'},
 # blok 31-40
 {'bag': '56:44 → 77:31', 'kural': "okuma — azap gölgesinin 'lâ … ve lâ …' ile iki olumsuz sıfatı: serin değil, cömert değil / gölgelendirmez, alevden korumaz", 'not': 'kurgu eşi.'},
 {'bag': '77:30 → 77:31', 'kural': "sûre içi — kök ظلل: 'zıll' / 'zalîl' (cümle iki ayete yayılıyor)", 'not': 'sûre içi eş.'},
 {'bag': '76:7 → 77:32', 'kural': "okuma — kök شرر ardışık sûrelerde iki anlam: 'şer' (76:7, 76:11) / 'şerer' kıvılcım (1021)", 'not': 'kök eşi.'},
 {'bag': '37:20 → 77:35', 'kural': "okuma — 'hâzâ yevmu …' iki ardışık ayette (37:20-21) / iki kez (77:35, 77:38)", 'not': 'kalıp eşi.'},
 {'bag': '27:85 → 77:35', 'kural': "okuma — lemma 'nataqa' olumsuz: söz üzerlerine gerçekleşince / konuşamadıkları gün", 'not': 'lemma eşi.'},
 {'bag': '16:84 → 77:36', 'kural': "okuma — 'lâ yu'zenu': inkâr edenlere izin verilmemesi (edilgen) / özür için izin verilmemesi", 'not': 'kalıp eşi.'},
 {'bag': '66:7 → 77:36', 'kural': "okuma — lemma 'i'tezera': bugün özür dilemeyin (yasak) / izin verilmez ki özür dilesinler", 'not': 'lemma eşi.'},
 {'bag': '77:6 → 77:36', 'kural': "sûre içi — kök عذر iki ayet: yemin dizisinde ''uzr' / özür dileyememe", 'not': 'sûre içi eş.'},
 {'bag': '37:21 → 77:38', 'kural': "okuma — 'hâzâ yevmu'l-fasl' korpusun iki ayeti", 'not': 'kalıp eşi.'},
 {'bag': '77:16 → 77:38', 'kural': "sûre içi — lemma 'evvel': helâk edilen öncekiler / sizinle toplanan öncekiler", 'not': 'sûre içi eş.'},
 {'bag': '56:49 → 77:38', 'kural': "okuma — öncekilerin ve sonrakilerin toplanması (56:49-50) / sizin ve öncekilerin toplanması", 'not': 'kurgu eşi.'},
 {'bag': '11:55 → 77:39', 'kural': "okuma — 1S 'fe-kîdûnî': dünyada topluluğa meydan okuma / âhirette 2MP'ye", 'not': 'kalıp eşi.'},
 {'bag': '52:46 → 77:39', 'kural': "okuma — lemma 'keyd': o gün tuzağın işe yaramaması / 'hileniz varsa kurun'", 'not': 'lemma eşi.'},
 # blok 41-50
 {'bag': '51:15 → 77:41', 'kural': "okuma — 'inne'l-muttaqîne fî … ve 'uyûn': cennât / zılâl", 'not': 'kalıp eşi.'},
 {'bag': '77:30 → 77:41', 'kural': "sûre içi — kök ظلل üç geçiş: azap gölgesi (77:30-31) / sakınanların gölgeleri (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '52:22 → 77:42', 'kural': "okuma — 'mimmâ yeştehûn': meyve ve et / meyveler", 'not': 'kalıp eşi.'},
 {'bag': '52:19 → 77:43', 'kural': "ölçüm esit2 TAM — iki sûrede özdeş ayet 'kulû veşrabû henî'en bimâ kuntum ta'melûn'", 'not': 'esit2.'},
 {'bag': '69:24 → 77:43', 'kural': "ölçüm xref — aynı emir, gerekçe 'geçmiş günlerde önden gönderdikleriniz'", 'not': 'xref.'},
 {'bag': '37:80 → 77:44', 'kural': "ölçüm esit2 TAM — 'innâ kezâlike neczi'l-muhsinîn' (sûre 37'de dört geçiş)", 'not': 'esit2.'},
 {'bag': '77:18 → 77:44', 'kural': "sûre içi — 'kezâlike' + 1P fiil: suçlulara / iyilik yapanlara (aday 1039, okuma); iki kalıp sûre 37'de de (37:34, 37:80)", 'not': 'sûre içi eş.'},
 {'bag': '77:43 → 77:46', 'kural': "sûre içi — 'kulû': sakınanlara afiyetle / suçlulara biraz (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '15:3 → 77:46', 'kural': "okuma — lemma dizisi 'ekele + temetta'a' korpusun iki ayeti: 'bırak onları' (3MP) / doğrudan emir (2MP)", 'not': 'lemma eşi.'},
 {'bag': '77:15 → 77:49', 'kural': "ölçüm esit2 TAM + nakarat3 — nakaratın ilk ve son (10.) geçişi; sûre içi on geçişin hepsi okundu", 'not': 'nakarat3.'},
 {'bag': '45:6 → 77:50', 'kural': "ölçüm xref — 'fe-bi-eyyi hadîsin ba'de …': Allah'tan ve ayetlerinden sonra / ondan sonra", 'not': 'xref.'},
 {'bag': '77:12 → 77:50', 'kural': "sûre içi — kök أيي iki geçiş: 'li-eyyi yevmin' / 'fe-bi-eyyi hadîsin' — sûrenin iki 'hangi' sorusu", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_murselat', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in MURSELAT]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_murselat'] = MURSELAT
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_murselat', len(MURSELAT), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_murselat', len(BAGLAR['AS_murselat']))
