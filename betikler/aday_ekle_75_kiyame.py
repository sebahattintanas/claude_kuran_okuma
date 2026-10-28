# -*- coding: utf-8 -*-
"""aday_ekle_75_kiyame.py — sûre 75 (Kıyâme) adayları (AX_kiyame) ve okuma bağları (AS_kiyame).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

KIYAME = [
]

BAGLAR = {"AS_kiyame": [
 # blok 1-10
 {'bag': '74:56 → 75:1', 'kural': "okuma — ardışık sûre sınırı; lafız + 3MS zamir + iki 'ehl' izâfetiyle kapanış / lafızsız 1S yeminle açılış; fâsıla ة → ة (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '56:75 → 75:1', 'kural': "okuma — lemma dizisi 'lâ + aqsama': 'fe-lâ uqsimu' sûre içinde / sûre açılışında 'fe'siz", 'not': 'kalıp eşi.'},
 {'bag': '69:38 → 75:1', 'kural': "okuma — lemma dizisi 'lâ + aqsama': 'fe-lâ uqsimu' sûre içinde / sûre açılışında 'fe'siz", 'not': 'kalıp eşi.'},
 {'bag': '70:40 → 75:1', 'kural': "okuma — lemma dizisi 'lâ + aqsama': 'fe-lâ uqsimu' sûre içinde / sûre açılışında 'fe'siz", 'not': 'kalıp eşi.'},
 {'bag': '75:1 → 75:2', 'kural': "sûre içi — yemin kalıbının 've' ile tekrarı: 'lâ uqsimu bi-' + belirli ad + belirli niteleyici (gün / nefs)", 'not': 'sûre içi eş.'},
 {'bag': '36:78 → 75:3', 'kural': "okuma — lemma ''izâm': kemiklerin dirilmesini soran insan / insana yöneltilen soru", 'not': 'lemma eşi.'},
 {'bag': '36:81 → 75:4', 'kural': "okuma — 'qâdir + 'alâ + en' ve 'belâ': soru önce, 'belâ' sonra / 'belâ' önce, 'qâdirîn' cevabın içinde", 'not': 'kalıp eşi.'},
 {'bag': '46:33 → 75:4', 'kural': "okuma — 'qâdir + 'alâ + en' ve 'belâ': soru önce, 'belâ' sonra / 'belâ' önce, 'qâdirîn' cevabın içinde", 'not': 'kalıp eşi.'},
 {'bag': '70:40 → 75:4', 'kural': "okuma — 'lâ uqsimu' + 1P 'qâdir': tek ayette / 75:1-2 yemin, 75:4 1P 'qâdirîn' (ardışık olmayan sûre)", 'not': 'kurgu eşi.'},
 {'bag': '75:3 → 75:4', 'kural': "sûre içi — 'len necme'a' / 'belâ qâdirîn' karşıt çift (aday 1039); 1P konuşan soruyu kendisi cevaplıyor", 'not': 'sûre içi eş.'},
 {'bag': '17:90 → 75:5', 'kural': "okuma — lemma 'yefcur' korpusun iki ayeti: yerden kaynak fışkırtma / fucûr; biçim aynı, anlam farklı (eşsesli şüphesi, sayı iddiası yok)", 'not': 'lemma eşi.'},
 {'bag': '75:3 → 75:5', 'kural': "sûre içi — 'e-yahsebu'l-insân' / 'bel yurîdu'l-insân': aynı fail, sanıdan isteğe", 'not': 'sûre içi eş.'},
 {'bag': '51:12 → 75:6', 'kural': "okuma — lemma dizisi 'se'ele + eyyâne' korpusun iki ayeti: 3MP + 'yevmu'd-dîn' / 3MS + 'yevmu'l-qiyâme'", 'not': 'kalıp eşi.'},
 {'bag': '29:13 → 75:6', 'kural': "ölçüm xref (سأل + يوم + قيامة) — kıyamet günü sorgulanan insanlar / kıyamet gününü soran insan", 'not': 'xref.'},
 {'bag': '75:1 → 75:6', 'kural': "sûre içi — 'yevmu'l-qiyâme': yemin nesnesi / soru konusu", 'not': 'sûre içi eş.'},
 {'bag': '67:16 → 75:8', 'kural': "okuma — lemma 'xasafa': geçişli, yer insanları batırır / geçişsiz, özne ay", 'not': 'lemma eşi.'},
 {'bag': '74:32 → 75:8', 'kural': "okuma — lemma 'qamar': yemin nesnesi / olayın öznesi (ardışık sûre, okuma bağı; sûre sınırı değil)", 'not': 'lemma eşi.'},
 {'bag': '71:16 → 75:9', 'kural': "okuma — güneş ve ay: ay-güneş sırası, iki fiil, ayrı işlev / güneş-ay sırası, tek edilgen fiil, bir araya getirilme", 'not': 'kurgu eşi.'},
 {'bag': '75:3 → 75:9', 'kural': "sûre içi — lemma 'ceme'a': 1P kemikleri toplar (etken) / güneş ve ay toplanır (edilgen)", 'not': 'sûre içi eş.'},
 {'bag': '75:8 → 75:9', 'kural': "sûre içi — قمر iki ardışık ayette", 'not': 'sûre içi eş.'},
 {'bag': '19:66 → 75:10', 'kural': "okuma — lemma dizisi 'qâle + insân': insan dirilişi soruyor / o gün kaçış yerini soruyor", 'not': 'kalıp eşi.'},
 {'bag': '75:6 → 75:10', 'kural': "sûre içi — insanın soruları: 'eyyâne' (ne zaman) / 'eyne' (nereye)", 'not': 'sûre içi eş.'},
 # blok 11-20
 {'bag': '75:10 → 75:11', 'kural': "sûre içi — soru / cevap: 'eyne'l-meferr' / 'kellâ lâ wazar'", 'not': 'sûre içi eş.'},
 {'bag': '53:42 → 75:12', 'kural': "okuma — 'ilâ rabbike' + belirli ad, haber önde: 'el-muntehâ' / 'el-mustaqarr'", 'not': 'kurgu eşi.'},
 {'bag': '36:38 → 75:12', 'kural': "okuma — lemma 'mustaqarr': güneşin varacağı yer / o gün varılacak yer", 'not': 'lemma eşi.'},
 {'bag': '75:12 → 75:13', 'kural': "sûre içi — 'yevme'izin' art arda iki ayette (75:10'dan sonra)", 'not': 'sûre içi eş.'},
 {'bag': '12:108 → 75:14', 'kural': "okuma — lemma 'basîra': davetin dayandığı / insanın kendine karşı", 'not': 'lemma eşi.'},
 {'bag': '17:14 → 75:14', 'kural': "okuma — nefs + ''alâ' + kendi üzerine hüküm: 'hasîb' / 'basîra' (lemma ortak değil)", 'not': 'kurgu eşi.'},
 {'bag': '75:2 → 75:14', 'kural': "sûre içi — kök نفس iki geçiş: yemin nesnesi 'en-nefsu'l-levvâme' / ''alâ nefsihî basîra'", 'not': 'sûre içi eş.'},
 {'bag': '75:7 → 75:14', 'kural': "sûre içi — kök بصر iki geçiş: organ 'el-basar' / 'basîra'", 'not': 'sûre içi eş.'},
 {'bag': '75:14 → 75:15', 'kural': "sûre içi — 'bel' cümlesi + 've lev' şartı; şartın cevabı ayrı gelmiyor", 'not': 'sûre içi eş.'},
 {'bag': '20:114 → 75:16', 'kural': "okuma — 2MS yasak + ''acile' + 'bi-': nesne 'el-qur'ân' adlı / zamir (gönderge KAPATILAMAZ)", 'not': 'kalıp eşi.'},
 {'bag': '75:3 → 75:17', 'kural': "sûre içi — kök جمع üç geçiş: kemikler (1P) / güneş ve ay (edilgen, 75:9) / zamir (1P)", 'not': 'sûre içi eş.'},
 {'bag': '75:17 → 75:18', 'kural': "sûre içi — lemma 'qur'ân' iki geçiş, zamirli masdar", 'not': 'sûre içi eş.'},
 {'bag': '17:106 → 75:18', 'kural': "okuma — 'qara'a' + 'qur'ân': 2MS okur / 1P okur, 2MS izler", 'not': 'kurgu eşi.'},
 {'bag': '75:17 → 75:19', 'kural': "sûre içi — 'inne 'aleynâ' + masdar + zamir: 'summe' ile tekrar (jem', qur'ân / beyân)", 'not': 'sûre içi eş.'},
 {'bag': '55:4 → 75:19', 'kural': "okuma — lemma 'beyân': insana öğretilen / 1P'nin üstlendiği", 'not': 'lemma eşi.'},
 {'bag': '74:53 → 75:20', 'kural': "okuma — 'kellâ + bel': 3MP 'lâ yehâfûne' / 2MP 'tuhibbûne' (ardışık sûre, okuma bağı; sûre sınırı değil)", 'not': 'kalıp eşi.'},
 {'bag': '17:18 → 75:20', 'kural': "okuma — lemma ''âcile': 'yurîdu' (isteme) / 'tuhibbûne' (sevme)", 'not': 'lemma eşi.'},
 {'bag': '75:16 → 75:20', 'kural': "sûre içi — kök عجل iki geçiş: 2MS'nin acelesi (yasak) / 2MP'nin sevdiği peşin olan", 'not': 'sûre içi eş.'},
 {'bag': '75:11 → 75:20', 'kural': "sûre içi — 'kellâ': 'kellâ lâ' / 'kellâ bel'", 'not': 'sûre içi eş.'},
 # blok 21-30
 {'bag': '75:20 → 75:21', 'kural': "sûre içi — ''âcile' / 'âxira' karşıt çift (aday 1039): 'tuhibbûne' / 'tezerûne'", 'not': 'sûre içi eş.'},
 {'bag': '17:19 → 75:21', 'kural': "okuma — ''âcile' / 'âxira' karşıtlığı ardışık iki ayette (17:18-19 / 75:20-21): 'yurîdu' / 'erâde' ↔ 'tuhibbûne' / 'tezerûne'", 'not': 'kurgu eşi.'},
 {'bag': '75:13 → 75:21', 'kural': "sûre içi — kök أخر iki geçiş: 'axxara' / 'el-âxira'", 'not': 'sûre içi eş.'},
 {'bag': '75:22 → 75:24', 'kural': "sûre içi — 'vucûhun yevme'izin' + haber: 'nâdira' / 'bâsira' karşıt çift (aday 1039)", 'not': 'sûre içi eş.'},
 {'bag': '75:22 → 75:23', 'kural': "sûre içi — ardışık fâsıla kelimeleri 'nâdira' / 'nâzira' harekesiz iskelette tek harf farkı (ض / ظ)", 'not': 'sûre içi eş.'},
 {'bag': '27:35 → 75:23', 'kural': "okuma — lemma 'nâzira' korpusun iki ayeti: 1S'nin bakıp beklemesi / yüzlerin Rabbe bakması", 'not': 'lemma eşi.'},
 {'bag': '74:22 → 75:24', 'kural': "okuma — kök بسر korpusun iki ayeti ardışık sûrelerde: fiil 'besera' / sıfat 'bâsira' (okuma bağı; sûre sınırı değil)", 'not': 'kök eşi.'},
 {'bag': '75:25 → 75:28', 'kural': "sûre içi — kök ظنن iki geçiş: yüzlerin sanısı / ölen kişinin sanısı", 'not': 'sûre içi eş.'},
 {'bag': '56:83 → 75:26', 'kural': "okuma — 'izâ belağat' + boğaz bölgesi adı, fail 3FS adsız: 'hulqûm' / 'terâqî'", 'not': 'kurgu eşi.'},
 {'bag': '75:20 → 75:26', 'kural': "sûre içi — lemma 'kellâ' üç geçiş (75:11, 75:20, 75:26)", 'not': 'sûre içi eş.'},
 {'bag': '75:10 → 75:27', 'kural': "sûre içi — kök قول iki geçiş, ikisi soru: 'eyne'l-meferr' / 'men râq'", 'not': 'sûre içi eş.'},
 {'bag': '18:78 → 75:28', 'kural': "okuma — lemma 'firâq' korpusun iki ayeti: iki kişi arası ayrılık (söz) / ölüm anı ayrılığı (sanı)", 'not': 'lemma eşi.'},
 {'bag': '68:42 → 75:29', 'kural': "okuma — lemma 'sâq': nekre, açılma / belirli, dolanma", 'not': 'lemma eşi.'},
 {'bag': '75:26 → 75:29', 'kural': "sûre içi — ölüm anı sahnesinde beden bölgeleri: köprücük kemikleri / bacak", 'not': 'sûre içi eş.'},
 {'bag': '75:12 → 75:30', 'kural': "ölçüm esit2 BENZER + nakarat3 tür ic — 'ilâ rabbike yevme'izin' + 'el-mustaqarr' / 'el-mesâq'", 'not': 'esit2.'},
 {'bag': '75:23 → 75:30', 'kural': "sûre içi — Rab üç geçişin üçü de 'ilâ' + Rab (75:12, 75:23, 75:30)", 'not': 'sûre içi eş.'},
 {'bag': '75:29 → 75:30', 'kural': "sûre içi — kök سوق üç geçiş: 'es-sâq' ×2 (bacak) / 'el-mesâq' (sevk) — aynı kök, iki anlam", 'not': 'sûre içi eş.'},
 # blok 31-40
 {'bag': '75:31 → 75:32', 'kural': "sûre içi — 'saddeqa' / 'kezzebe' karşıt çift (aday 1039); 'lâ … ve lâ' / 'lâkin … ve'", 'not': 'sûre içi eş.'},
 {'bag': '74:43 → 75:31', 'kural': "okuma — namaz kılmama: suçluların 1P sözü / 3MS anlatım (ardışık sûre, okuma bağı; lemma farklı)", 'not': 'kurgu eşi.'},
 {'bag': '20:48 → 75:32', 'kural': "okuma — lemma dizisi 'kezzebe + tevellâ': 'men' ile genel hüküm / 3MS anlatım", 'not': 'kalıp eşi.'},
 {'bag': '74:56 → 75:33', 'kural': "okuma — lemma 'ehl': Allah ('ehlu't-teqvâ') / insanın ailesi (ardışık sûre, okuma bağı; 1041 sûre içi kaydı dışı)", 'not': 'lemma eşi.'},
 {'bag': '75:34 → 75:35', 'kural': "ölçüm esit2 BENZER + nakarat3 — 'evlâ leke fe-evlâ' korpusun iki ayeti, art arda; 'summe' ile tekrar", 'not': 'esit2.'},
 {'bag': '47:20 → 75:34', 'kural': "okuma — 'fe-evlâ' + 3MP / 'evlâ leke fe-evlâ' 2MS (lemma eşsesli şüphesi)", 'not': 'kalıp eşi.'},
 {'bag': '75:32 → 75:35', 'kural': "sûre içi — kök ولي beş geçiş: 'tevellâ' / 'evlâ' ×4 — aynı kök, iki anlam", 'not': 'sûre içi eş.'},
 {'bag': '75:3 → 75:36', 'kural': "sûre içi — lemma dizisi 'hasiba + insân' korpusun iki ayeti, ikisi de bu sûrede: kemiklerin toplanmayacağı / başıboş bırakılma sanısı", 'not': 'sûre içi eş.'},
 {'bag': '23:115 → 75:36', 'kural': "okuma — 'hasiba' + boşuna yaratılma / başıboş bırakılma (''abesen' / 'sudâ')", 'not': 'kurgu eşi.'},
 {'bag': '53:46 → 75:37', 'kural': "okuma — 'nutfe' + 'tumnâ' / 'nutfe min meniyy' + 'yumnâ'", 'not': 'kalıp eşi.'},
 {'bag': '56:58 → 75:37', 'kural': "okuma — lemma 'yumnâ': 2MP soru / edilgen", 'not': 'lemma eşi.'},
 {'bag': '23:14 → 75:38', 'kural': "okuma — nutfe → 'alaqa dizisi: beş aşama adlı, 1P / 'alaqa'dan sonra fiillerle (xalaqa, sevvâ), 3MS", 'not': 'kurgu eşi.'},
 {'bag': '75:4 → 75:38', 'kural': "sûre içi — kök سوي iki geçiş: 'nusevviye benâneh' (1P) / 'fe-sevvâ' (3MS)", 'not': 'sûre içi eş.'},
 {'bag': '75:37 → 75:39', 'kural': "sûre içi — oluşum dizisi: nutfe / meni → 'alaqa → yaratma, düzenleme → iki eş (75:37-39)", 'not': 'sûre içi eş.'},
 {'bag': '53:45 → 75:39', 'kural': "ölçüm xref — 'ez-zevceyni'z-zekera ve'l-unsâ' korpusun iki ayeti: 'xalaqa' / 'ce'ale minhu'", 'not': 'xref.'},
 {'bag': '51:49 → 75:39', 'kural': "okuma (kullanıcı sorusu, onaylı 2026-10-27) — 'zevceyn' cinsiyet adı olmadan: 'min kulli şey'in xalaqnâ zevceyn' (her şeyden çift) / 75:39 'ez-zevceyn' + bedel 'ez-zekera ve'l-unsâ' — çift ilişki adı önce, cins adı açıklayıcı bedel olarak sonra (sözdizimsel sıra, zamansal öncelik iddiası değil)", 'not': 'okuma bağı.'},
 {'bag': '49:13 → 75:39', 'kural': "okuma (kullanıcı sorusu, onaylı 2026-10-27) — yön ters: 49:13 'xalaqnâkum min zekerin ve unsâ' (önce erkek ve dişi, ardından 'şu'ûben ve qabâ'il') / 75:39 'minhu' (tek kaynak) → 'ez-zevceyn' → 'ez-zekera ve'l-unsâ'", 'not': 'okuma bağı.'},
 {'bag': '46:33 → 75:40', 'kural': "ölçüm xref — 'bi-qâdirin 'alâ en yuhyiye'l-mevtâ' korpusun iki ayeti: soru + 'belâ' / cevapsız soru, sûre sonu", 'not': 'xref.'},
 {'bag': '75:4 → 75:40', 'kural': "ölçüm nakarat3 tür ic — 'qâdir + 'alâ + en': sûrenin dördüncü ayeti (1P cevap) / son ayeti ('zâlike' ile soru)", 'not': 'nakarat3.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_kiyame', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in KIYAME]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_kiyame'] = KIYAME
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_kiyame', len(KIYAME), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_kiyame', len(BAGLAR['AS_kiyame']))
