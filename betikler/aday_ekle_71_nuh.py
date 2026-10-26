# -*- coding: utf-8 -*-
"""aday_ekle_71_nuh.py — sûre 71 (Nûh) adayları (AX_nuh) ve okuma bağları (AS_nuh).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

NUH = [
]

BAGLAR = {"AS_nuh": [
 # blok 1-10
 {'bag': '70:44 → 71:1', 'kural': "okuma — ardışık sûre sınırı; 'zâlike'l-yevmu'llezî kânû yû'adûn' ile kapanış / 'innâ erselnâ nûhan … azâbun elîm' ile açılış; fâsıla ن → م (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '11:25 → 71:1', 'kural': "lemma dizisi 'erselnâ + nûh + ilâ + qavm' (5 ayet) — 've leqad erselnâ' / 'innâ erselnâ'", 'not': 'kalıp eşi.'},
 {'bag': '23:23 → 71:1', 'kural': "lemma dizisi 'erselnâ + nûh + ilâ + qavm' (5 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '29:14 → 71:1', 'kural': "lemma dizisi 'erselnâ + nûh + ilâ + qavm' (5 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '11:25 → 71:2', 'kural': "lemma dizisi 'qavm + inne + nezîr + mubîn' (2 ayet) / xref — 11:25 tek ayet / 71:1-2 iki ayet, araya emir giriyor", 'not': 'kalıp eşi.'},
 {'bag': '71:1 → 71:2', 'kural': "sûre içi — kök نذر: 'enzir' emri / 'nezîr' bildirimi", 'not': 'sûre içi eş.'},
 {'bag': '29:16 → 71:3', 'kural': "xref (ölçüm) / lemma dizisi 'abede + allah' — 'u'budu'llâhe ve'ttaqûh'", 'not': 'kalıp eşi.'},
 {'bag': '23:23 → 71:3', 'kural': "lemma dizisi 'abede + allah' (24 ayet) — Nûh'un çağrısı", 'not': 'kalıp eşi.'},
 {'bag': '26:108 → 71:3', 'kural': "lemma dizisi 'ittaqâ + allah + atâ'a' (10 ayet) — 71:3'te sıra 'allah + ittaqâ + atâ'a'", 'not': 'kalıp eşi.'},
 {'bag': '14:10 → 71:4', 'kural': "lemma dizisi 'ğafera + min + zenb + ahhara + ilâ' (2 ayet) / xref — 'ilâ ecelin musemmâ'", 'not': 'kalıp eşi.'},
 {'bag': '63:11 → 71:4', 'kural': "okuma — 'ahhara + izâ câ'e + ecel': etken, tekil nefs / edilgen", 'not': 'kurgu eşi.'},
 {'bag': '11:3 → 71:4', 'kural': "okuma — lemma dizisi 'ilâ + ecel' + bağışlanma dileği aynı ayette / 71:4 ve 71:10'a dağılmış", 'not': 'kurgu eşi.'},
 {'bag': '71:3 → 71:4', 'kural': "sûre içi — üç emir / meczûm cevap 'yağfir … yu'ahhirkum'", 'not': 'sûre içi eş.'},
 {'bag': '71:2 → 71:5', 'kural': "sûre içi — iki 'qâle': kavme 'yâ qavmi' / Rabbe 'rabbi'", 'not': 'sûre içi eş.'},
 {'bag': '71:5 → 71:8', 'kural': "sûre içi — kök دعو ilk / son geçiş: 'de'avtu qavmî leylen ve nehârâ' / 'de'avtuhum cihârâ'", 'not': 'sûre içi eş.'},
 {'bag': '71:5 → 71:6', 'kural': "sûre içi — kök دعو: 'de'avtu' / 'du'â'î'", 'not': 'sûre içi eş.'},
 {'bag': '2:19 → 71:7', 'kural': "lemma dizisi 'ce'ale + esâbi' + fî' (2 ayet) / xref — benzetme içi korunma / çağrıdan kaçınma", 'not': 'kalıp eşi.'},
 {'bag': '11:5 → 71:7', 'kural': "lemma dizisi 'isteğşâ + siyâb' (2 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '35:43 → 71:7', 'kural': "okuma — lemma 'istikbâr' (2 ayet)", 'not': 'lemma eşi.'},
 {'bag': '11:5 → 71:9', 'kural': "okuma — 'yusirrûne … yu'linûn' / 'a'lentu … esrartu': gizleyen-açığa vuran kavim / açıklayan-gizleyen konuşan", 'not': 'kurgu eşi.'},
 {'bag': '47:26 → 71:9', 'kural': "okuma — lemma 'isrâr' (2 ayet)", 'not': 'lemma eşi.'},
 {'bag': '71:8 → 71:9', 'kural': "sûre içi — 'summe innî' ×2; 'cihârâ' / 'isrârâ' (karşıt çift aday 1039)", 'not': 'sûre içi eş.'},
 {'bag': '11:3 → 71:10', 'kural': "lemma dizisi 'isteğfera + rabb' (6 ayet) — 've eni'steğfirû rabbekum' / 'isteğfirû rabbekum'", 'not': 'kalıp eşi.'},
 {'bag': '11:52 → 71:10', 'kural': "lemma dizisi 'isteğfera + rabb' (6 ayet) — 'yâ qavmi'steğfirû rabbekum'", 'not': 'kalıp eşi.'},
 {'bag': '20:82 → 71:10', 'kural': "okuma — lemma 'ğaffâr' (5 ayet): 1S 'le-ğaffârun' / 3MS 'kâne ğaffârâ'", 'not': 'lemma eşi.'},
 {'bag': '71:4 → 71:10', 'kural': "sûre içi — kök غفر: 'yağfir lekum' / 'isteğfirû … ğaffârâ'", 'not': 'sûre içi eş.'},
 {'bag': '71:7 → 71:10', 'kural': "sûre içi — kök غفر: 'li-tağfira lehum' (Rabbe) / 'isteğfirû rabbekum' (kavme)", 'not': 'sûre içi eş.'},
 # blok 11-20
 {'bag': '11:52 → 71:11', 'kural': "lemma dizisi 'ersele + semâ' + alâ' (3 ayet) / xref / lemma 'midrâr' — bağışlanma dileği + gökten bol yağmur tek ayette / 71:10-11 iki ayette", 'not': 'kalıp eşi.'},
 {'bag': '71:10 → 71:11', 'kural': "sûre içi — emir 'isteğfirû' / meczûm cevap 'yursil'", 'not': 'sûre içi eş.'},
 {'bag': '71:1 → 71:11', 'kural': "sûre içi — kök رسل: Nûh'u gönderme / göğü gönderme", 'not': 'sûre içi eş.'},
 {'bag': '17:6 → 71:12', 'kural': "lemma dizisi 'emedde + mâl + benîn' (2 ayet) / xref — 1P geçmiş / 3MS şarta bağlı", 'not': 'kalıp eşi.'},
 {'bag': '71:5 → 71:12', 'kural': "sûre içi — kök نهر iki anlam: 'nehâr' (gündüz) / 'enhâr' (ırmaklar)", 'not': 'sûre içi eş.'},
 {'bag': '39:6 → 71:14', 'kural': "okuma — insanın aşamalı yaratılışı, aşamalar adsız: 'halqan min ba'di halq' / 'atvârâ'", 'not': 'kurgu eşi.'},
 {'bag': '23:14 → 71:14', 'kural': "okuma — aşamalar adlı / adsız", 'not': 'kurgu eşi.'},
 {'bag': '67:3 → 71:15', 'kural': "lemma dizisi 'seb' + semâ'' (5 ayet) / lemma 'tibâq' (3 ayet) / xref — 'seb'a semâvâtin tibâqâ' aynı", 'not': 'kalıp eşi.'},
 {'bag': '71:14 → 71:15', 'kural': "sûre içi — kök خلق: insanın / göklerin yaratılışı", 'not': 'sûre içi eş.'},
 {'bag': '10:5 → 71:16', 'kural': "okuma — 'ce'ale' + güneş + ay 'nûr': güneş 'diyâ'' / 'sirâc'; sıra ters", 'not': 'kurgu eşi.'},
 {'bag': '25:61 → 71:16', 'kural': "okuma — lemma 'sirâc' (4 ayet) + ay, gökte", 'not': 'lemma eşi.'},
 {'bag': '71:15 → 71:16', 'kural': "sûre içi — 'fîhinne' → 'semâvât'", 'not': 'sûre içi eş.'},
 {'bag': '20:55 → 71:17', 'kural': "okuma — yerden yaratılış / yerden bitirilme; 20:55 üçlüsü tek ayette (1P) / 71:17-18 iki ayette", 'not': 'kurgu eşi.'},
 {'bag': '20:55 → 71:18', 'kural': "okuma — 'fîhâ nu'îdukum ve minhâ nuhricukum' / 'yu'îdukum fîhâ ve yuhricukum ihrâcâ'", 'not': 'kurgu eşi.'},
 {'bag': '71:17 → 71:18', 'kural': "sûre içi — 'mine'l-ard' → 'fîhâ'; bitirilme → dönüş → çıkarılış", 'not': 'sûre içi eş.'},
 {'bag': '71:17 → 71:19', 'kural': "sûre içi — iki 'va'llâhu' açılışı, yer", 'not': 'sûre içi eş.'},
 {'bag': '20:53 → 71:19', 'kural': "okuma — 'ce'ale lekumu'l-arda mehden ve seleke … subulen' tek ayet / 71:19-20 iki ayet", 'not': 'kurgu eşi.'},
 {'bag': '43:10 → 71:19', 'kural': "okuma — 'ce'ale lekumu'l-arda mehden … subulen' tek ayet / 71:19-20 iki ayet", 'not': 'kurgu eşi.'},
 {'bag': '20:53 → 71:20', 'kural': "okuma — lemma 'seleke' + 'subul': Allah'ın fiili / kavmin fiili", 'not': 'lemma eşi.'},
 {'bag': '21:31 → 71:20', 'kural': "okuma — lemma 'fecc' (3 ayet): 'ficâcen subulen' / 'subulen ficâcâ'", 'not': 'lemma eşi.'},
 {'bag': '71:7 → 71:19', 'kural': "sûre içi — lemma 'ce'ale' kavmin / Allah'ın fiili (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 # blok 21-28
 {'bag': '71:5 → 71:21', 'kural': "sûre içi — 'qâle rabbi' / 'qâle nûhun rabbi': Rabbe hitap adla yeniden açılıyor", 'not': 'sûre içi eş.'},
 {'bag': '71:21 → 71:26', 'kural': "nakarat3 sûre içi (ölçüm GEÇMEZ) / lemma dizisi 'qâle + nûh + rabb' (2 ayet)", 'not': 'sûre içi eş.'},
 {'bag': '14:36 → 71:21', 'kural': "okuma — isyan + uyma aynı ayette: konuşana uyan / isyan eden; konuşana isyan eden, başkasına uyan", 'not': 'kurgu eşi.'},
 {'bag': '71:6 → 71:21', 'kural': "sûre içi — 'lem yezid … illâ' hasrı: 'firârâ' / 'hasârâ'", 'not': 'sûre içi eş.'},
 {'bag': '71:12 → 71:21', 'kural': "sûre içi — kök مول: 'emvâl' vaat / 'mâluhû' zarar", 'not': 'sûre içi eş.'},
 {'bag': '71:7 → 71:22', 'kural': "sûre içi — kök كبر: 'istekberu'stikbârâ' / 'mekran kubbârâ' (mef'ûl mutlak)", 'not': 'sûre içi eş.'},
 {'bag': '71:23 → 71:26', 'kural': "sûre içi — lemma 'vezera': kavmin 'lâ tezerunne' / Nûh'un 'lâ tezer' (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '14:36 → 71:24', 'kural': "okuma — 'edlelne kesîran' / 'edallû kesîrâ'", 'not': 'kurgu eşi.'},
 {'bag': '71:24 → 71:28', 'kural': "nakarat3 sûre içi (ölçüm GEÇER) — 'lâ tezidi'z-zâlimîne illâ dalâlâ' / '… illâ tebârâ'", 'not': 'sûre içi eş.'},
 {'bag': '25:37 → 71:25', 'kural': "okuma — lemma 'ağraqa': Nûh kavmi, 1P etken / edilgen; gerekçe yalanlama / hatalar", 'not': 'lemma eşi.'},
 {'bag': '37:82 → 71:25', 'kural': "okuma — lemma 'ağraqa'", 'not': 'lemma eşi.'},
 {'bag': '29:14 → 71:25', 'kural': "okuma — Nûh kavminin sonu: 'fe-ehazehumu't-tûfân' / 'uğriqû'", 'not': 'kurgu eşi.'},
 {'bag': '71:16 → 71:25', 'kural': "sûre içi — kök نور iki anlam: 'nûr' (ışık) / 'nâr' (ateş)", 'not': 'sûre içi eş.'},
 {'bag': '71:1 → 71:25', 'kural': "sûre içi — 'azâbun elîm' uyarısı / 'uğriqû fe-udhilû nârâ'", 'not': 'sûre içi eş.'},
 {'bag': '21:89 → 71:26', 'kural': "lemma dizisi 'rabb + lâ + yezer' (2 ayet) — 'beni tek bırakma' / 'kimseyi bırakma'", 'not': 'kalıp eşi.'},
 {'bag': '71:10 → 71:27', 'kural': "sûre içi — fe''âl vezni, fâsıla 'ârâ': 'ğaffârâ' (Rab) / 'keffârâ' (doğacak nesil)", 'not': 'sûre içi eş.'},
 {'bag': '71:3 → 71:27', 'kural': "sûre içi — kök عبد: 'u'budû' / 'ibâdeke'", 'not': 'sûre içi eş.'},
 {'bag': '71:21 → 71:27', 'kural': "sûre içi — kök ولد: 'veleduhû' / 'yelidû'", 'not': 'sûre içi eş.'},
 {'bag': '14:41 → 71:28', 'kural': "lemma dizisi 'rabb + ğafera + … + vâlideyy' (2 ayet) / xref", 'not': 'kalıp eşi.'},
 {'bag': '26:118 → 71:28', 'kural': "okuma — Nûh'un duası, 'min'el-mu'minîn': kurtar / bağışla", 'not': 'kurgu eşi.'},
 {'bag': '71:10 → 71:28', 'kural': "sûre içi — kök غفر: 'isteğfirû … ğaffârâ' (kavme) / 'rabbi'ğfir lî' (Nûh'un kendisi için)", 'not': 'sûre içi eş.'},
 {'bag': '71:1 → 71:28', 'kural': "sûre içi — açılış 'innâ erselnâ nûhan' / kapanış Nûh'un duası", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_nuh', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in NUH]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_nuh'] = NUH
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_nuh', len(NUH), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_nuh', len(BAGLAR['AS_nuh']))
