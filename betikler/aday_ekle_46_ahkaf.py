# -*- coding: utf-8 -*-
"""aday_ekle_46_ahkaf.py — sûre 46 (Ahkâf) adayları (AX_ahkaf) ve okuma bağları (AS_ahkaf).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

AHKAF = [
]

BAGLAR = {"AS_ahkaf": [
 {'bag': '40:1 · 41:1 · 42:1 · 43:1 · 44:1 · 45:1 → 46:1', 'kural': "esit2 TAM — 'Hâ Mîm' (ölçüm); hepsi okundu", 'not': 'Hâ Mîm ailesi.'},
 {'bag': '45:37 → 46:1 · 46:2', 'kural': "okuma — ardışık sûre sınırı; 'el-azîz el-hakîm'; aday 1040 alanında kayıt, test yok", 'not': 'sûre sınırı.'},
 {'bag': '39:1 · 40:2 · 45:2 → 46:2', 'kural': "esit2 TAM 39:1, 45:2, BENZER 40:2 (ölçüm); okundu", 'not': 'kitabın indirilişi.'},
 {'bag': '15:85 · 30:8 · 44:39 → 46:3', 'kural': "xref (ölçüm); lemma dizisi 'halaqa + semâ + ard + mâ + beyn + illâ + haqq' 2 ayet; okundu — 've ecelin musemmâ' 30:8", 'not': 'hak ile ve belirli süreyle.'},
 {'bag': '35:40 · 39:38 → 46:4', 'kural': "xref 35:40 (ölçüm); lemma dizisi 'erûnî mâzâ halaqû mine'l-ard em lehum şirk' 2 ayet; okundu", 'not': 'yerden neyi yarattılar.'},
 {'bag': '35:14 · 41:52 → 46:5', 'kural': "xref 35:14 (ölçüm); okuma — 'men edallu mimmen'; okundu", 'not': 'cevap vermeyene yalvaran.'},
 {'bag': '35:14 → 46:6', 'kural': "okuma — yalvarılanların inkârı; okundu", 'not': 'düşman olurlar.'},
 {'bag': '34:43 · 45:25 → 46:7', 'kural': "xref 34:43 (ölçüm); lemma dizisi 'ellezî + kefere + haqq + lemmâ + câe' 2 ayet; okundu", 'not': 'apaçık büyü.'},
 {'bag': '11:35 · 13:43 · 29:52 → 46:8', 'kural': "lemma dizisi 'qâle + in + iftarâ' 2 ayet (11:35); 'kefâ bi- … şehîden beynî ve beynekum' 13:43, 29:52; okundu", 'not': 'uydurdumsa; şahit olarak O yeter.'},
 {'bag': '10:15 · 38:70 → 46:9', 'kural': "lemma dizisi 'in ettebi'u illâ mâ yûhâ ileyy' 3 ayet; xref 38:70 (ölçüm); okundu", 'not': 'vahyedilene uyarım.'},
 {'bag': '41:52 → 46:10', 'kural': "xref (ölçüm); lemma dizisi 'ra'â + in + kâne + min + ind + Allah' 2 ayet; okundu — 41:52'nin iki parçası 46:5 ve 46:10'da", 'not': 'Allah katındansa.'},
 {'bag': '46:7 → 46:11', 'kural': "nakarat3 'qâle'llezîne keferû' (ölçüm, GEÇMEZ); lemma dizisi 'qâle + ellezî + kefere + ellezî + âmene' 4 ayet (19:73, 29:12, 36:47 okundu)", 'not': 'inkâr edenlerin sözü.'},
 {'bag': '11:17 → 46:12', 'kural': "xref (ölçüm); lemma dizisi 'min qabl + kitâb + mûsâ + imâm + rahme' 2 ayet; okundu — 11:17'de önce 'şâhidun minh', 46:10 şahit → 46:12 kitap", 'not': 'Mûsâ\'nın kitabı önder ve rahmet.'},
 {'bag': '16:103 · 26:195 → 46:12', 'kural': "lemma dizisi 'lisân + arabiyy' 3 ayet (ölçüm sayımı); okundu", 'not': 'Arapça dil.'},
 {'bag': '41:30 → 46:13', 'kural': "xref (ölçüm); lemma dizisi 'inne + ellezî + qâle + rabb + Allah + summe + isteqâme' 2 ayet; okundu — devamı farklı (melekler / haber)", 'not': 'Rabbimiz Allah deyip dosdoğru olanlar.'},
 {'bag': '10:62 → 46:13', 'kural': "lemma dizisi 'lâ havfun aleyhim ve lâ hum yahzenûn' 12 ayet; okunan 10:62", 'not': 'korku yok, üzülmezler.'},
 {'bag': '32:17 → 46:14', 'kural': "xref (ölçüm); lemma dizisi 'cezâ' + bimâ kânû ya'melûn' 3 ayet (56:24 henüz okunmadı)", 'not': 'yaptıklarına karşılık.'},
 {'bag': '29:8 · 31:14 → 46:15', 'kural': "xref (ölçüm); lemma dizisi 'vassâ + insân + vâlideyh' 3 ayet; okundu — devamı üçünde farklı; 31:14 'iki yıl' / 46:15 'otuz ay'", 'not': 'insana anne babasını tavsiye.'},
 {'bag': '27:19 → 46:15', 'kural': "xref (ölçüm); 15 lemmalık dua dizisi 2 ayet; 'evzi'' lemma 2 ayet; okundu", 'not': 'Rabbim bana ilham et.'},
 {'bag': '41:33 → 46:15', 'kural': "lemma dizisi 'inne + min + muslim' 2 ayet; okundu", 'not': 'ben teslim olanlardanım.'},
 {'bag': '24:38 · 29:7 · 39:35 → 46:16', 'kural': "lemma dizisi 'ahsene mâ amilû' 2 ayet (24:38); 29:7, 39:35 'ahsene'llezî' + kötülüklerin örtülmesi (okumada görüldü)", 'not': 'yaptıklarının en güzeli.'},
 {'bag': '17:23 · 21:67 → 46:17', 'kural': "'uff' lemma 3 ayet (ölçüm sayımı); okundu — 17:23'te anne babaya yasaklanan söz", 'not': 'öf size.'},
 {'bag': '23:35 → 46:17', 'kural': "okuma — 'va'ade' + 'ahraca' soru kalıbı (okumada görüldü)", 'not': 'çıkarılacağımı mı vaat ediyorsunuz.'},
 {'bag': '10:55 · 30:60 · 31:33 · 35:5 · 40:55 · 40:77 · 45:32 → 46:17', 'kural': "lemma dizisi 'inne va'da'llâhi haqq' 8 ayet; öbür 7'si okundu", 'not': 'Allah\'ın vaadi hak.'},
 {'bag': '16:24 · 23:83 · 25:5 · 27:68 → 46:17', 'kural': "lemma dizisi 'esâtîr + evvel' 9 ayet; okunan 4", 'not': 'öncekilerin masalları.'},
 {'bag': '41:25 → 46:18', 'kural': "xref (ölçüm); 15 lemmalık dizi 2 ayet; okundu (7:38 henüz okunmadı)", 'not': 'cin ve insan ümmetlerinde söz gerçekleşti.'},
 {'bag': '46:17 → 46:18', 'kural': "okuma — 'halâ' fiili ardışık iki ayette ('haleti'l-qurûn' → 'halet min qablihim'); tekil 'ellezî' → çoğul 'ulâ'ike'", 'not': 'gelip geçen nesiller.'},
 {'bag': '46:20 → 46:34', 'kural': "nakarat3 'yevme yu'radu'llezîne keferû ale'n-nâr' (ölçüm, GEÇER; 6 kelime); 46:34 henüz okunmadı", 'not': 'ateşe sunulma günü.'},
 {'bag': '41:15 · 40:75 · 41:17 → 46:20', 'kural': "xref (ölçüm); 'istekbere fi'l-ard bi-ğayri'l-haqq' 2 ayet (41:15); 40:75 çift 'bimâ kuntum'; 41:17 'azâbu'l-hûn' (6:93 henüz okunmadı)", 'not': 'haksız yere büyüklenme, alçaltıcı azap.'},
 {'bag': '11:50 · 26:124 → 46:21', 'kural': "okuma — Âd'ın kardeşi orada adlı, 46:21'de adsız (okumada görüldü)", 'not': 'Âd\'ın kardeşi.'},
 {'bag': '41:14 → 46:21', 'kural': "xref (ölçüm); 'min beyni … ve min half' + 'allâ ta'budû illa'llâh' — 41:14 çoğul (rusul), 46:21 tekil; okundu", 'not': 'önünden ve arkasından uyarıcılar.'},
 {'bag': '26:135 · 11:26 → 46:21', 'kural': "lemma dizisi 'innî ehâfu aleykum azâbe yevmin azîm' 3 ayet (26:135 okundu, 7:59 henüz okunmadı); xref 11:26 ('elîm')", 'not': 'büyük günün azabı.'},
 {'bag': '11:32 → 46:22', 'kural': "xref (ölçüm); lemma dizisi 'fe'tinâ bimâ te'idunâ in kunte mine's-sâdiqîn' 3 ayet; okundu (7:70 henüz okunmadı)", 'not': 'vaat ettiğini getir.'},
 {'bag': '33:63 → 46:23', 'kural': "lemma dizisi 'innema'l-ilmu inda'llâh' 4 ayet; okunan 33:63", 'not': 'bilgi Allah katındadır.'},
 {'bag': '11:57 · 11:29 → 46:23', 'kural': "11:57 'eblağtukum mâ ursiltu bihî' (okumada görüldü); xref 11:29 'erâkum qavmen techelûn' (ölçüm, lemma dizisi 2 ayet)", 'not': 'tebliğ ve bilgisizlik.'},
 {'bag': '41:16 · 13:17 → 46:24', 'kural': "okuma — Âd için rüzgâr (41:16); 'evdiye' lemma 2 ayet (13:17)", 'not': 'bulut ve rüzgâr.'},
 {'bag': '10:13 → 46:25', 'kural': "xref (ölçüm); lemma dizisi 'kezâlike neczi'l-qavme'l-mucrimîn' 2 ayet; okundu", 'not': 'suçlu kavmi böyle cezalandırırız.'},
 {'bag': '29:38 → 46:25', 'kural': "okuma — Âd ve Semûd'un meskenleri (okumada görüldü)", 'not': 'meskenler.'},
 {'bag': '16:78 · 23:78 · 32:9 → 46:26', 'kural': "lemma dizisi 'sem' + basar + fu'âd' 6 ayet (67:23 henüz okunmadı); okundu — 'lekum' + şükür / 'lehum' + yarar sağlamadı", 'not': 'kulak, göz, gönül.'},
 {'bag': '11:8 · 16:34 · 39:48 · 40:83 · 45:33 → 46:26', 'kural': "lemma dizisi 've hâqa bihim mâ kânû bihî yestehzi'ûn' 6 ayet; öbür 5'i okundu", 'not': 'alay ettikleri kuşattı.'},
 {'bag': '29:41 → 46:28', 'kural': "lemma dizisi 'ellezîne'ttehazû min dûni'llâh' 2 ayet; okundu; nakarat3 'min dûni'llâh' GEÇER (sûre içi 46:4, 46:5)", 'not': 'Allah\'ı bırakıp edinilenler.'},
 {'bag': '46:18 → 46:29', 'kural': "okuma — 'mine'l-cinni ve'l-ins' → 'mine'l-cinn' (sûre içi); 72:1 'nefer + min + cinn' henüz okunmadı", 'not': 'cinlerden bir topluluk.'},
 {'bag': '46:12 → 46:30', 'kural': "okuma — 'min qablihî kitâbu mûsâ … kitâbun musaddiq' / 'kitâben unzile min ba'di mûsâ musaddiqan' (sûre içi)", 'not': 'Mûsâ\'dan önce / sonra kitap.'},
 {'bag': '35:31 → 46:30', 'kural': "lemma dizisi 'musaddiqan limâ beyne yedeyh' 8 ayet; okunan 35:31", 'not': 'öncesindekini doğrulayan.'},
 {'bag': '46:31 → 46:32', 'kural': "nakarat3 'ecâbe + dâ'î + Allah' (ölçüm, GEÇMEZ; sûre içi)", 'not': 'Allah\'ın davetçisi.'},
 {'bag': '33:46 · 20:108 → 46:31', 'kural': "'dâ'î' lemma 4 ayet; okundu", 'not': 'davetçi.'},
 {'bag': '14:10 → 46:31', 'kural': "lemma dizisi 'yağfir lekum min zunûbikum' 3 ayet (71:4 henüz okunmadı); okundu", 'not': 'günahlarınızdan bağışlasın.'},
 {'bag': '39:22 → 46:32', 'kural': "lemma dizisi 'ulâ'ike fî dalâlin mubîn' 2 ayet; okundu", 'not': 'apaçık sapıklık.'},
 {'bag': '42:9 → 46:32', 'kural': "okuma — 'velî' lemması Allah için (42:9) / Allah'tan başkası için (46:32); aday 1041 alanında kayıt, test yok", 'not': 'velî / evliyâ.'},
 {'bag': '17:99 → 46:33', 'kural': "lemma dizisi 'e-ve lem yerev enna'llâhe'llezî halaqa's-semâvâti ve'l-ard' 2 ayet; okundu", 'not': 'gökleri ve yeri yaratan güç yetirir.'},
 {'bag': '42:9 · 41:39 → 46:33', 'kural': "xref (ölçüm) 42:9; ölüleri diriltme + 'alâ kulli şey'in qadîr' (okundu)", 'not': 'ölüleri diriltir.'},
 {'bag': '46:3 → 46:33', 'kural': "nakarat3 'halaqa + semâ + ard' (ölçüm, GEÇMEZ); sûre içi — 1P 'halaqnâ' / 3MS lafız 'halaqa'", 'not': 'gökler ve yer yaratması.'},
 {'bag': '46:20 → 46:34', 'kural': "nakarat3 'yevme yu'radu'llezîne keferû ale'n-nâr' (ölçüm, GEÇER); sûre içi, iki ayrı alıntı", 'not': 'ateşe sunulma günü.'},
 {'bag': '34:3 → 46:34', 'kural': "lemma dizisi 'qâlû belâ ve rabbinâ' 4 ayet (6:30, 64:7 henüz okunmadı); okunan 34:3", 'not': 'evet, Rabbimize andolsun.'},
 {'bag': '10:45 → 46:35', 'kural': "xref (ölçüm); lemma dizisi 'lem yelbesû illâ sâ'aten min nehâr' 2 ayet; okundu", 'not': 'gündüzün bir saati.'},
 {'bag': '46:24 → 46:35', 'kural': "okuma — 'iste'celtum' → 'lâ testa'cil' (sûre içi; عجل iki ayet)", 'not': 'acele.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_ahkaf', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in AHKAF]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_ahkaf'] = AHKAF
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_ahkaf', len(AHKAF), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_ahkaf', len(BAGLAR['AS_ahkaf']))
