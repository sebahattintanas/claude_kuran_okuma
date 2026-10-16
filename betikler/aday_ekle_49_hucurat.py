# -*- coding: utf-8 -*-
"""aday_ekle_49_hucurat.py — sûre 49 (Hucurât) adayları (AX_hucurat) ve okuma bağları (AS_hucurat).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

HUCURAT = [
]

BAGLAR = {"AS_hucurat": [
 {'bag': '48:29 → 49:1', 'kural': "okuma — ardışık sûre sınırı; hitap → 2MP nidâ, fâsıla ا → م; 'rasûlu'llâh' / 'yedeyi'llâhi ve rasûlih'; aday 1040 alanında kayıt, test yok", 'not': 'sûre sınırı.'},
 {'bag': '48:10 → 49:1', 'kural': "okuma — 'yedu'llâh' / 'yedeyi'llâh'; aday 1041 kaydına ek", 'not': 'el.'},
 {'bag': '9:23 · 24:21 · 24:27 · 33:53 · 33:69 → 49:1 · 49:2', 'kural': "lemma dizisi 'yâ eyyuhe'llezîne âmenû lâ' 27 ayet; okundu; nakarat3 GEÇER (sûre içi 49:1, 2, 11)", 'not': 'nidâ + yasak.'},
 {'bag': '18:57 · 22:10 → 49:1', 'kural': "'qaddeme' lemma 27 ayet; okundu — 'qaddemet yedâh / yedâk' (amel) / 'beyne yedey' (önüne geçme); KAPATILAMAZ", 'not': 'öne geçme.'},
 {'bag': '24:21 · 9:103 · 24:60 → 49:1', 'kural': "lemma dizisi 'semî' + alîm' 32 ayet; okundu", 'not': 'işiten, bilen.'},
 {'bag': '31:19 · 20:108 · 17:64 → 49:2 · 49:3', 'kural': "'savt' lemma 5 ayet; okundu — 31:19 'ğadda + savt' 49:3'te de", 'not': 'ses.'},
 {'bag': '49:2 → 49:3', 'kural': "okuma — sesi yükseltme yasağı / kısanlar; 'tahbata a'mâlukum' / 'mağfiratun ve ecrun azîm'; karşıt çift (aday 1039, okuma)", 'not': 'ses ve karşılık.'},
 {'bag': '9:17 · 9:69 → 49:2', 'kural': "'habita' lemma 12 ayet; okundu — 'habitat a'mâluhum'", 'not': 'işlerin boşa gitmesi.'},
 {'bag': '47:9 · 47:28 · 47:32 → 49:2', 'kural': "okuma — 'ahbata' (IV. bab, Allah) / 'habita' (I. bab); aday 1040 alanına sınırda", 'not': 'boşa çıkarma.'},
 {'bag': '24:30 · 24:31 → 49:3', 'kural': "'ğadda' lemma 4 ayet; okundu — bakışı indirme / sesi kısma", 'not': 'indirme.'},
 {'bag': '33:35 · 48:29 → 49:3', 'kural': "lemma dizisi 'lehum mağfiratun ve ecrun azîm' 3 ayet; 33:35 okundu; 48:29 aynı ikili (aday 1040 alanına sınırda)", 'not': 'bağışlanma ve ödül.'},
 {'bag': '33:53 → 49:4', 'kural': "okuma — 'min verâ'' peygamberin evleri bağlamında; KAPATILAMAZ", 'not': 'arkadan seslenme.'},
 {'bag': '29:63 → 49:4', 'kural': "lemma dizisi 'ekseruhum lâ ya'qilûn' 3 ayet; okundu", 'not': 'akletmeyenler.'},
 {'bag': '47:21 → 49:5', 'kural': "lemma dizisi 'le-kâne hayran lehum' 6 ayet; okundu — aynı 'lev … le-kâne hayran lehum' çerçevesi", 'not': 'daha iyi olurdu.'},
 {'bag': '24:62 → 49:5 · 49:10', 'kural': "okuma — elçinin yanında izin / sabır; 'ğafûr rahîm' kapanışı; 'innema'l-mu'minûn' açılışı", 'not': 'elçi ile edep.'},
 {'bag': '47:25 · 47:32 · 9:113 → 49:6', 'kural': "'tebeyyene' lemma 17 ayet; okundu — geçişsiz / emir", 'not': 'açıklığa kavuşma.'},
 {'bag': '16:119 → 49:6', 'kural': "'cehâle' lemma 4 ayet; okundu", 'not': 'bilmeden.'},
 {'bag': '23:40 · 26:157 → 49:6', 'kural': "'nâdim' lemma 5 ayet; okundu — üçünde 'esbaha' + 'nâdim'", 'not': 'pişmanlık.'},
 {'bag': '49:2 → 49:6', 'kural': "okuma — نبأ 'nebiyy' / 'nebe''", 'not': 'peygamber ve haber.'},
 {'bag': '9:128 → 49:7', 'kural': "''anite' lemma 3 ayet; okundu — aynı 2MP 'anittum'", 'not': 'sıkıntıya düşme.'},
 {'bag': '48:12 → 49:7', 'kural': "okuma — 'zuyyine … fî qulûbikum' (edilgen, kötü zan) / 'zeyyenehû fî qulûbikum' (Allah, iman); aday 1040 alanına sınırda; KAPATILAMAZ", 'not': 'kalplerde süsleme.'},
 {'bag': '9:23 → 49:7', 'kural': "okuma — 'istehabbu'l-kufra ale'l-îmân' / 'habbebe … el-îmân … kerrehe … el-kufr'", 'not': 'sevdirme.'},
 {'bag': '9:15 · 24:58 · 48:4 → 49:8', 'kural': "lemma dizisi 've'llâhu alîmun hakîm' 20 ayet; okundu", 'not': 'bilen, hikmet sahibi.'},
 {'bag': '24:2 → 49:9', 'kural': "lemma dizisi 'tâ'ife + min + mu'min' 2 ayet; okundu", 'not': 'inananlardan topluluk.'},
 {'bag': '28:15 → 49:9', 'kural': "'iqtetele' lemma 3 ayet; okundu — iki kişi / iki topluluk; KAPATILAMAZ", 'not': 'birbiriyle savaşma.'},
 {'bag': '38:22 · 38:24 → 49:9', 'kural': "'beğâ … alâ' okundu — iki taraf, biri öbürüne; hüküm / düzeltme; KAPATILAMAZ", 'not': 'saldırı.'},
 {'bag': '49:9 → 49:10', 'kural': "okuma — 'aslihû beyne' sûre içi üç; 'iqtetelû' / 'ihveh' karşıt çift (aday 1039, okuma)", 'not': 'aralarını düzeltme.'},
 {'bag': '12:5 · 12:100 → 49:10', 'kural': "'ihve' lemma 7 ayet; okundu — Yûsuf'un kardeşleri; KAPATILAMAZ", 'not': 'kardeşler.'},
 {'bag': '24:56 · 27:46 · 36:45 → 49:10', 'kural': "lemma dizisi 'la'allekum turhamûn' 8 ayet; okundu", 'not': 'merhamet görme.'},
 {'bag': '9:79 · 9:58 → 49:11', 'kural': "'sehira' 7 ayet, 'lemeze' 3 ayet; okundu — 9:79 ikisi bir arada, 'sehira'llâhu minhum' (aday 1041 alanında kayıt)", 'not': 'alay ve kusurlama.'},
 {'bag': '49:7 → 49:11', 'kural': "okuma — 'îmân' / 'fusûq' sûre içi ikinci kez; 'ulâ'ike hum' + sıfat (49:7, 11, 15)", 'not': 'iman ve fısk.'},
 {'bag': '9:23 · 24:50 → 49:11', 'kural': "lemma dizisi 'ulâ'ike humu'z-zâlimûn' 7 ayet; okundu", 'not': 'zalimler.'},
 {'bag': '22:30 · 42:37 · 39:17 → 49:12', 'kural': "'ictenebe' lemma 9 ayet; okundu — 42:37 'ictenebe + ism'", 'not': 'kaçınma.'},
 {'bag': '48:6 · 48:12 → 49:12', 'kural': "okuma — 'zanne's-sev'' / 'ba'da'z-zanni ism'; aday 1040 alanına sınırda", 'not': 'zan.'},
 {'bag': '35:12 → 49:12', 'kural': "lemma dizisi 'ekele + lahm' 2 ayet; okundu — denizden taze et / ölü kardeş eti (temsil); KAPATILAMAZ", 'not': 'et yeme.'},
 {'bag': '9:104 · 9:118 → 49:12', 'kural': "okuma — 'et-tevvâbu'r-rahîm' kapanışı", 'not': 'tövbe kabul eden.'},
 {'bag': '49:11 → 49:12', 'kural': "okuma — 'men lem yetub' / 'tevvâb'; karşıt çift (aday 1039, okuma)", 'not': 'tövbe.'},
 {'bag': '42:50 → 49:13', 'kural': "lemma dizisi 'zeker + unsâ' 6 ayet; xref (ölçüm); okundu", 'not': 'erkek ve dişi.'},
 {'bag': '10:45 → 49:13', 'kural': "'te'ârafe' lemma 2 ayet; okundu — haşirde tanışma / dünyada tanışma", 'not': 'tanışma.'},
 {'bag': '31:34 → 49:13', 'kural': "lemma dizisi 'inne'llâhe alîmun habîr' 2 ayet; xref (ölçüm); okundu", 'not': 'bilen, haberdar.'},
 {'bag': '49:11 → 49:13', 'kural': "okuma — 'qavm' / 'nisâ'' → 'zeker' / 'unsâ'", 'not': 'iki cins.'},
 {'bag': '48:11 · 48:16 → 49:14', 'kural': "'a'râb' lemma 10 ayet; okundu — 'se-yeqûlu' / 'qâlet'; aday 1040 alanına sınırda", 'not': 'bedevîler.'},
 {'bag': '49:7 → 49:14', 'kural': "okuma — 'zeyyenehû fî qulûbikum' / 'lemmâ yedhuli'l-îmânu fî qulûbikum'; KAPATILAMAZ", 'not': 'kalplerde iman.'},
 {'bag': '49:2 → 49:14', 'kural': "okuma — 'tahbata a'mâlukum' / 'lâ yelitkum min a'mâlikum'", 'not': 'işler.'},
 {'bag': '24:62 · 49:10 → 49:15', 'kural': "lemma dizisi 'innema'l-mu'minûne'llezîne âmenû bi'llâhi ve rasûlih' 2 ayet; xref (ölçüm); okundu; sûre içi iki 'innema'l-mu'minûn'", 'not': 'inananların tanımı.'},
 {'bag': '9:45 · 24:50 → 49:15', 'kural': "'irtâbe' lemma 9 ayet; okundu", 'not': 'şüphe.'},
 {'bag': '9:41 · 9:81 → 49:15', 'kural': "lemma dizisi 'câhede bi-emvâlihim ve enfusihim fî sebîli'llâh' 4 ayet; okundu", 'not': 'mal ve canla çaba.'},
 {'bag': '12:37 → 49:16', 'kural': "okuma — ''allema' fâil Rab / fâil insan, meful Allah; aday 1041 alanında kayıt", 'not': 'öğretme.'},
 {'bag': '26:22 · 14:11 · 37:114 → 49:17', 'kural': "lemma dizisi 'menne + alâ' 6 ayet; okundu — 26:22 'temunnuhâ aleyye'; 14:11 'lâkinna'llâhe yemunnu'", 'not': 'minnet.'},
 {'bag': '49:17 (menn)', 'kural': "okuma — 'lâ temunnû' (insan) / 'bel Allâhu yemunnu' aynı ayette; aday 1041 alanında kayıt", 'not': 'minnet.'},
 {'bag': '49:14 → 49:17', 'kural': "okuma — 'eslemnâ' / 'en eslemû … islâmekum'", 'not': 'teslim olma.'},
 {'bag': '49:16 → 49:18', 'kural': "okuma — 'ya'lemu mâ fi's-semâvâti …' / 'ya'lemu ğaybe's-semâvâti …'", 'not': 'bilgi.'},
 {'bag': '11:31 · 9:105 → 49:18', 'kural': "'ğayb' okundu — Nûh 'lâ a'lemu'l-ğayb' / 'âlimi'l-ğaybi ve'ş-şehâde'", 'not': 'gayb.'},
 {'bag': '48:24 → 49:18', 'kural': "okuma — 'kâna'llâhu bimâ ta'melûne basîrâ' / 've'llâhu basîrun bimâ ta'melûn'; aday 1040 alanına sınırda", 'not': 'gören.'},
 {'bag': '49:1 → 49:18', 'kural': "okuma — sûre açılışı 'semî'un alîm' / kapanışı 'basîrun bimâ ta'melûn'", 'not': 'sûre çerçevesi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_hucurat', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in HUCURAT]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_hucurat'] = HUCURAT
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_hucurat', len(HUCURAT), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_hucurat', len(BAGLAR['AS_hucurat']))
