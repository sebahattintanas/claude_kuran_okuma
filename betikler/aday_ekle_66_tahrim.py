# -*- coding: utf-8 -*-
"""aday_ekle_66_tahrim.py — sûre 66 (Tahrîm) adayları (AX_tahrim) ve okuma bağları (AS_tahrim).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

TAHRIM = [
]

BAGLAR = {"AS_tahrim": [
 # blok 1-4
 {'bag': '65:12 → 66:1', 'kural': "okuma — ardışık sûre sınırı; bilgiyle kapanış / soru ve nidâyla açılış; fâsıla ا → م (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '65:1 → 66:1', 'kural': "lemma dizisi — 'yâ eyyuhe'n-nebiyy' (13 ayet): ardışık iki sûre aynı nidâyla açılıyor (aday 1040, kayıt)", 'not': 'açılış eşi.'},
 {'bag': '64:14 → 66:1', 'kural': "okuma — 'ezvâc': 64:14, 65:1 ('en-nisâ''), 66:1 — üç ardışık sûrede eşler (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '33:28 → 66:1', 'kural': "okuma — 'yâ eyyuhe'n-nebiyyu qul li-ezvâcik' / 'tebteğî mardâte ezvâcik'", 'not': 'nidâ + eşler.'},
 {'bag': '9:29 → 66:1', 'kural': "okuma — lemma 'harrama': Allah'ın haram kıldığını haram saymayanlar / helâl kıldığını haram kılan", 'not': 'lemma karşıtı.'},
 {'bag': '64:14 → 66:1', 'kural': "lemma dizisi — 'lafız + ğafûr + rahîm' (46 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '33:38 → 66:2', 'kural': "okuma — lemma 'farada': 'farada'llâhu lehû' (Peygamber) / 'farada'llâhu lekum'", 'not': 'lemma eşi.'},
 {'bag': '47:11 → 66:2', 'kural': "lemma dizisi — 'lafız + mevlâ' (6 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '33:1 → 66:2', 'kural': "lemma dizisi — 'alîm + hakîm' (29 ayet)", 'not': 'ortak kapanış.'},
 {'bag': '66:1 → 66:2', 'kural': "sûre içi — kök حلل: 'ehalla'llâh' / 'tahille' (حلل [2/2]); 2MS → 2MP", 'not': 'sûre içi eş.'},
 {'bag': '64:4 → 66:3', 'kural': "okuma — lemma 'esarra': Allah'ın gizlenenleri bilmesi / Peygamberin gizli sözü ve açığa çıkması (ardışık değil, okuma bağı)", 'not': 'lemma eşi.'},
 {'bag': '64:7 → 66:3', 'kural': "okuma — lemma 'nebbe'e': yapılanın haber verilmesi / sözün haber verilmesi", 'not': 'lemma eşi.'},
 {'bag': '31:34 → 66:3', 'kural': "okuma — 'alîmun habîr' / 'el-alîmu'l-habîr' (fail, lafızsız)", 'not': 'sıfat çifti.'},
 {'bag': '28:86 → 66:4', 'kural': "okuma — lemma 'zahîr': kâfirlere destekçi olma / melekler destekçi", 'not': 'lemma eşi.'},
 {'bag': '66:2 → 66:4', 'kural': "sûre içi — 'mevlâ' ×2 (ولي [2/2]): 'mevlâkum' / 'huve mevlâhu ve Cibrîlu ve sâlihu'l-mu'minîn' (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '66:3 → 66:4', 'kural': "sûre içi — kök ظهر: 'azharahu' / 'tezâherâ', 'zahîr' (iki anlam)", 'not': 'kök iki anlam.'},
 # blok 5-8
 {'bag': '65:1 → 66:5', 'kural': "okuma — lemma 'tallaqa': 'izâ tallaqtumu'n-nisâ'' / 'in tallaqakunne' (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '33:49 → 66:5', 'kural': "okuma — lemma 'tallaqa': 2MP boşayanlar / 3MS Peygamber", 'not': 'lemma eşi.'},
 {'bag': '33:35 → 66:5', 'kural': "okuma — sıfat dizisi 'muslimât, mu'minât, qânitât': erkek / kadın çiftleri 've' ile / yalnız kadın çoğulu, atıfsız", 'not': 'dizi eşi.'},
 {'bag': '56:36 → 66:5', 'kural': "okuma — lemma 'bikr' (3 ayet)", 'not': 'lemma eşi.'},
 {'bag': '66:4 → 66:5', 'kural': "sûre içi — kök توب: 'tetûbâ' / 'tâ'ibât'", 'not': 'sûre içi eş.'},
 {'bag': '64:16 → 66:6', 'kural': "okuma — lemma 'vaqâ': edilgen 'yûqa' / emir 'qû'", 'not': 'lemma eşi.'},
 {'bag': '16:50 → 66:6', 'kural': "lemma dizisi — 've yef'alûne mâ yu'merûn' (5 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '66:4 → 66:6', 'kural': "sûre içi — 'melâ'ike' (ملك [2/2]): Peygambere destekçi / ateşin başında", 'not': 'sûre içi eş.'},
 {'bag': '9:66 → 66:7', 'kural': "okuma — 'lâ ta'tezirû': dünyada / 'el-yevm'", 'not': 'lemma dizisi eşi.'},
 {'bag': '52:16 → 66:7', 'kural': "lemma dizisi — 'innemâ tuczevne mâ kuntum ta'melûn' (2 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '45:28 → 66:7', 'kural': "xref (ölçüm) — 'el-yevme tuczevne mâ kuntum ta'melûn'", 'not': 'xref eşi.'},
 {'bag': '66:6 → 66:7', 'kural': "sûre içi — ardışık nidâ 'ellezîne âmenû' / 'ellezîne keferû' (karşıt çift, okuma)", 'not': 'sûre içi karşıt.'},
 {'bag': '66:4 → 66:8', 'kural': "nakarat3 (GEÇMEZ) — 'tâbe ilâ lafız': ikil şart / çoğul emir", 'not': 'sûre içi eş.'},
 {'bag': '66:5 → 66:8', 'kural': "nakarat3 (GEÇMEZ) — 'asâ rabb en': daha iyi eşler / kötülüklerin örtülmesi", 'not': 'sûre içi eş.'},
 {'bag': '64:9 → 66:8', 'kural': "lemma dizisi — 'yukeffir an seyyi'ât + yudhil cennâtin tecrî min tahtihe'l-enhâr' (4 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '47:2 → 66:8', 'kural': "xref (ölçüm) — 'keffera anhum seyyi'âtihim'", 'not': 'xref eşi.'},
 {'bag': '65:5 → 66:8', 'kural': "okuma — 'yukeffir anhu seyyi'âtihî' / 'yukeffire ankum seyyi'âtikum' (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '65:11 → 66:8', 'kural': "lemma dizisi — 'yudhil cennâtin tecrî min tahtihe'l-enhâr' (11 ayet) (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '57:12 → 66:8', 'kural': "xref (ölçüm) — 'yes'â nûruhum beyne eydîhim ve bi-eymânihim': inanan erkekler ve kadınlar / Peygamber ve onunla inananlar", 'not': 'xref eşi.'},
 {'bag': '66:2 → 66:8', 'kural': "sûre içi — lemma 'yemîn': yeminler / sağ yanlar (iki anlam)", 'not': 'lemma iki anlam.'},
 {'bag': '66:6 → 66:8', 'kural': "sûre içi — kök نور: 'nâr' / 'nûr' (karşıt çift, okuma)", 'not': 'kök iki anlam.'},
 # blok 9-12
 {'bag': '9:73 → 66:9', 'kural': "esit2 (YAKIN 0,9821; karakter karşılaştırmasında eşit) — ayet metni aynı", 'not': 'tekrar ayet.'},
 {'bag': '66:1 → 66:9', 'kural': "sûre içi — 'yâ eyyuhe'n-nebiyy' ×2: sitem / emir", 'not': 'sûre içi eş.'},
 {'bag': '66:6 → 66:9', 'kural': "sûre içi — kök غلظ: 'ğılâz' (melekler) / 've'ğluz' (Peygambere emir)", 'not': 'sûre içi eş.'},
 {'bag': '45:19 → 66:10', 'kural': "lemma dizisi — 'ağnâ an … mine'llâhi şey'â' (2 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '12:67 → 66:10', 'kural': "xref (ölçüm) — 'mâ uğnî ankum mine'llâhi min şey''", 'not': 'xref eşi.'},
 {'bag': '66:10 → 66:11', 'kural': "nakarat3 (GEÇER) — 'daraba'llâhu meselen li'llezîne': keferû / âmenû; ateş / cennette ev (karşıt çift, okuma)", 'not': 'sûre içi karşıt.'},
 {'bag': '66:4 → 66:10', 'kural': "sûre içi — kök صلح: 'sâlihu'l-mu'minîn' / 'abdeyni … sâlihayn'", 'not': 'sûre içi eş.'},
 {'bag': '28:9 → 66:11', 'kural': "lemma dizisi — 'imraete fir'avn' (2 ayet): konuşma / dua", 'not': 'kalıp eşi.'},
 {'bag': '28:21 → 66:11', 'kural': "xref (ölçüm) — 'rabbi necciniî mine'l-qavmi'z-zâlimîn': 3MS / 3FS aynı dua", 'not': 'xref eşi.'},
 {'bag': '23:28 → 66:11', 'kural': "xref (ölçüm) — 'neccânâ mine'l-qavmi'z-zâlimîn'", 'not': 'xref eşi.'},
 {'bag': '21:91 → 66:12', 'kural': "lemma dizisi — 'elletî ahsanet fercehâ fe-nefahnâ fî- min rûhinâ' (2 ayet): 'fîhâ' / 'fîhi'", 'not': 'kalıp eşi.'},
 {'bag': '28:27 → 66:12', 'kural': "okuma — lemma 'ibnet' (2 ayet)", 'not': 'lemma eşi.'},
 {'bag': '66:11 → 66:12', 'kural': "sûre içi — kök بني: 'ibni' (yap) / 'ibnete' (kız) (iki anlam, 1021)", 'not': 'kök iki anlam.'},
 {'bag': '66:5 → 66:12', 'kural': "sûre içi — kök قنت: 'qânitât' / 'mine'l-qânitîn' — sûre aynı kökle kapanıyor (okuma)", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_tahrim', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in TAHRIM]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_tahrim'] = TAHRIM
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_tahrim', len(TAHRIM), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_tahrim', len(BAGLAR['AS_tahrim']))
