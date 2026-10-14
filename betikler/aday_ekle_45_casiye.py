# -*- coding: utf-8 -*-
"""aday_ekle_45_casiye.py — sûre 45 (Câsiye) adayları (AX_casiye) ve okuma bağları (AS_casiye).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

CASIYE = [
]

BAGLAR = {"AS_casiye": [
 {'bag': '40:1 · 41:1 · 42:1 · 43:1 · 44:1 → 45:1', 'kural': "esit2 TAM — 'Hâ Mîm' (ölçüm); okundu; 46:1 henüz okunmadı", 'not': 'Hâ Mîm ailesi.'},
 {'bag': '44:59 → 45:1', 'kural': "okuma — ardışık sûre sınırı; aday 1040 alanında kayıt, test yok", 'not': 'sûre sınırı.'},
 {'bag': '39:1 · 40:2 → 45:2', 'kural': "esit2 TAM 39:1, BENZER 40:2 (ölçüm); lemma dizisi 'tenzîl + kitâb + min + Allah' 4 ayet; okundu; 46:2 henüz okunmadı", 'not': 'kitabın indirilişi.'},
 {'bag': '10:6 → 45:3', 'kural': "xref (ölçüm); lemma dizisi 'fî + semâ + ard + âyet' 2 ayet; okundu", 'not': 'göklerde ve yerde âyetler.'},
 {'bag': '31:10 · 42:29 → 45:4', 'kural': "lemma 'besse' 5 ayet; okundu — yayılan canlılar", 'not': 'canlıları yayma.'},
 {'bag': '10:6 · 23:80 → 45:5', 'kural': "lemma dizisi 'ihtilâf + leyl + nehâr' 5 ayet; okundu; 2:164, 3:190 henüz okunmadı", 'not': 'gece ile gündüz.'},
 {'bag': '16:65 · 30:24 · 35:9 → 45:5', 'kural': "lemma dizisi 'ahyâ + ard + ba'd + mevt' 5 ayet; okundu — su / rizq", 'not': 'yerin diriltilmesi.'},
 {'bag': '13:4 · 16:12 · 16:67 · 30:24 · 30:28 → 45:5', 'kural': "lemma dizisi 'âyet + qavm + 'aqale' 7 ayet; okundu", 'not': 'akleden kavim.'},
 {'bag': '26:222 → 45:7', 'kural': "xref (ölçüm); lemma dizisi 'kull + effâk + esîm' 2 ayet; okundu", 'not': 'iftiracı günahkâr.'},
 {'bag': '44:44 → 45:7', 'kural': "okuma — 'esîm' önceki sûrenin sonunda ve bu sûrenin başında; aday 1040 alanında kayıt, test yok", 'not': 'günahkâr.'},
 {'bag': '31:7 → 45:8', 'kural': "lemma dizisi 'mustakbir + ke-en + lem + semi'a' 2 ayet; okundu — 'vellâ' / 'yusırru'", 'not': 'işitmemiş gibi.'},
 {'bag': '9:34 · 31:7 → 45:8', 'kural': "lemma dizisi 'beşşir + azâb + elîm' 5 ayet; okundu", 'not': 'acı azapla müjdele.'},
 {'bag': '31:6 → 45:9', 'kural': "xref (ölçüm); lemma dizisi 'ittehaze + huzuw + … + azâb + muhîn' 2 ayet; okundu — 31:6-7 / 45:8-9 ters sıra", 'not': 'alay konusu.'},
 {'bag': '14:16 → 45:10', 'kural': "lemma dizisi 'min + verâ' + cehennem' 2 ayet; okundu", 'not': 'arkalarında cehennem.'},
 {'bag': '29:41 → 45:10', 'kural': "lemma dizisi 'ittehaze + min + dûn + Allah + veliyy' 2 ayet; okundu", 'not': 'edinilen dostlar.'},
 {'bag': '44:41 → 45:10', 'kural': "okuma — 'lâ yuğnî … an … şey'en'; okundu", 'not': 'fayda vermez.'},
 {'bag': '18:105 · 34:5 → 45:11', 'kural': "xref (ölçüm); lemma dizileri 'keferû bi-âyâti rabbihim' 2 ayet, 'azâb + ricz + elîm' 2 ayet; okundu", 'not': 'riczden acı azap.'},
 {'bag': '30:46 · 16:14 · 22:65 → 45:12', 'kural': "xref 30:46 (ölçüm); lemma dizisi 'emr + ebteğâ + min + fadl + le'alle + şekera' 2 ayet; okundu", 'not': 'denizi boyun eğdirme.'},
 {'bag': '31:20 · 22:65 → 45:13', 'kural': "xref 31:20 (ölçüm); lemma dizisi 'sahhara + mâ + fî + semâ + mâ + fî' 2 ayet; okundu", 'not': 'göklerde ve yerde olanlar.'},
 {'bag': '45:3 · 45:4 · 45:5 → 45:13', 'kural': "okuma — 'âyât + kavim niteliği' dördüncü kez: 'yetefekkerûn'", 'not': 'düşünen kavim.'},
 {'bag': '14:5 → 45:14', 'kural': "okuma — 'eyyâmu'llâh'; okundu", 'not': "Allah'ın günleri."},
 {'bag': '41:46 · 32:11 → 45:15', 'kural': "xref 41:46 (ölçüm); lemma dizileri 2 ayet; okundu — aynı iki cümle, kapanış farklı", 'not': 'kendi lehine / aleyhine.'},
 {'bag': '17:70 · 10:93 → 45:16', 'kural': "xref 17:70 (ölçüm); okuma — 'razaqnâhum mine't-tayyibât'; okundu", 'not': 'temiz rızık.'},
 {'bag': '44:32 → 45:16', 'kural': "okuma — Benî İsrâîl 'ale'l-âlemîn'; okundu; aday 1040 alanında kayıt, test yok", 'not': 'âlemlere üstün.'},
 {'bag': '10:93 · 42:14 → 45:17', 'kural': "xref (ölçüm); lemma dizisi 'inne rabbe … yahtelifûn' 2 ayet, 'illâ min ba'di mâ câe' 4 ayet; okundu", 'not': 'ilimden sonra ayrılık.'},
 {'bag': '42:15 → 45:18', 'kural': "okuma — 'lâ tettebi' ehvâe'; okundu", 'not': 'heveslere uyma.'},
 {'bag': '9:71 · 45:10 → 45:19', 'kural': "lemma dizisi 'ba'd + veliyy + ba'd' 5 ayet; okundu — mü'minler / zâlimler; 'veliyy' Allah — aday 1041 alanında kayıt, test yok", 'not': 'dostlar.'},
 {'bag': '28:43 · 45:11 → 45:20', 'kural': "xref 28:43 (ölçüm); lemma dizisi 'besîra + nâs' 2 ayet; okundu", 'not': 'basiretler, hidayet, rahmet.'},
 {'bag': '38:28 · 29:4 → 45:21', 'kural': "xref 38:28 (ölçüm); lemma dizisi 'em + hasibe + ellezî' 3 ayet; okundu", 'not': 'iyiler ve kötüler bir mi.'},
 {'bag': '40:17 · 20:15 · 44:39 → 45:22', 'kural': "xref 20:15, 40:17 (ölçüm); okundu — 'tuczâ kullu nefsin bimâ kesebet'; 'bi'l-haqq'", 'not': 'her nefis karşılık görür.'},
 {'bag': '25:43 · 2:7 → 45:23', 'kural': "xref 25:43 (ölçüm); lemma dizisi 'ra'â + men + ittehaze + ilâh + hevâ'' 2 ayet; 'alâ + basar' 2 ayet (2:7); okundu", 'not': 'hevesini ilâh edinen; mühür ve perde.'},
 {'bag': '23:37 · 43:20 → 45:24', 'kural': "xref 23:37 (ölçüm); lemma dizileri 2'şer ayet; okundu", 'not': 'ancak dünya hayatı; bilgileri yok.'},
 {'bag': '44:35 · 44:36 → 45:24 · 45:25', 'kural': "xref 44:36 (ölçüm); lemma dizisi 'âbâ' + in + kâne + sâdıq' 2 ayet; okundu — aynı iki adım; aday 1040 alanında kayıt, test yok", 'not': 'atalarımızı getirin.'},
 {'bag': '44:8 · 45:24 · 40:59 → 45:26', 'kural': "okuma — dirim/ölüm sırası; xref 40:59 (ölçüm); okundu", 'not': 'diriltir, öldürür, toplar.'},
 {'bag': '30:14 · 40:78 → 45:27', 'kural': "xref 30:12, 30:14, 30:55, 40:46 (ölçüm); 'mubtıl' lemma 5 ayet; okundu", 'not': 'saatin kopacağı gün.'},
 {'bag': '17:71 → 45:28', 'kural': "okuma — her topluluğun çağrılması, kitap; okundu", 'not': 'kitabına çağrılır.'},
 {'bag': '23:62 · 45:22 → 45:29', 'kural': "xref 23:62 (ölçüm); okundu — 'kitâbun yentıqu bi'l-haqq' / 've hum lâ yuzlemûn'", 'not': 'hakkı söyleyen kitap.'},
 {'bag': '29:9 · 44:57 → 45:30', 'kural': "xref 29:9 (ölçüm); okuma — 'zâlike huve'l-fevzu'l-azîm' / '… el-mubîn'; aday 1040 alanında kayıt", 'not': 'apaçık kurtuluş.'},
 {'bag': '30:16 · 45:30 → 45:31', 'kural': "lemma dizisi 'emmâ + ellezî + kefere' 4 ayet; okundu — taksimin iki kolu", 'not': 'inkâr edenlere gelince.'},
 {'bag': '23:105 · 23:66 · 10:75 → 45:31', 'kural': "xref 23:66, 23:105 (ölçüm); lemma dizisi 'kâne + qavm + mucrim' 3 ayet; okundu", 'not': 'âyetlerim okunmuyor muydu.'},
 {'bag': '18:21 · 45:24 → 45:32', 'kural': "xref 18:21 (ölçüm); okundu — 'va'da'llâhi haqq, sâ'a lâ rayb'; zan", 'not': 'saat; zan.'},
 {'bag': '39:48 · 16:34 → 45:33', 'kural': "esit2 BENZER (ölçüm); okundu — fiil 39:48'le, nesne 16:34'le aynı", 'not': 'kötülükleri göründü.'},
 {'bag': '32:14 · 29:25 → 45:34', 'kural': "xref (ölçüm); okundu — karşılıklı unutma (sıra ters); 'me'vâkumu'n-nâr'", 'not': 'bugün sizi unutuyoruz.'},
 {'bag': '45:9 · 31:33 · 35:5 · 30:57 → 45:35', 'kural': "lemma dizileri 'ğarra + hayât + dunyâ' 6 ayet, 'yusta'tebûn' 4 ayet; okundu", 'not': 'dünya hayatı aldattı.'},
 {'bag': '1:2 · 39:75 · 40:7 → 45:36', 'kural': "lemma dizisi 'hamd + rabb' 11 ayet; okundu", 'not': 'hamd âlemlerin Rabbine.'},
 {'bag': '10:78 → 45:37', 'kural': "lemma 'kibriyâ'' 2 ayet; okundu — insanlara isnat / O'nun; aday 1041 alanında kayıt, test yok", 'not': 'büyüklük.'},
 {'bag': '45:2 → 45:37', 'kural': "okuma — 'el-azîz el-hakîm' sûrenin ikinci ve son ayeti", 'not': 'Azîz, Hakîm.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_casiye', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in CASIYE]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_casiye'] = CASIYE
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_casiye', len(CASIYE), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_casiye', len(BAGLAR['AS_casiye']))
