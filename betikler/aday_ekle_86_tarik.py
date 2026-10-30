# -*- coding: utf-8 -*-
"""aday_ekle_86_tarik.py — sûre 86 (Târık) adayları (AX_tarik) ve okuma bağları (AS_tarik).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

TARIK = [
]

BAGLAR = {"AS_tarik": [
 # blok 1-10
 {'bag': '85:22 → 86:1', 'kural': "okuma — ardışık sûre sınırı: nekre + edilgen ortaç ile kapanış / yemin ile açılış; ikisi de lafızsız, Rabsız; fâsıla ظ → ق (aday 1040, kayıt)", 'not': 'sınır.'},
 {'bag': '85:1 → 86:1', 'kural': "okuma — ardışık iki sûre 've's-semâ'' yeminiyle açılıyor: burçlar / gece gelen (aday 1040, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '69:3 → 86:2', 'kural': "ölçüm esit2 BENZER — 've mâ edrâke mâ' + belirli ad: gerçekleşecek olan / gece gelen", 'not': 'kalıp eşi.'},
 {'bag': '82:17 → 86:2', 'kural': "okuma — 've mâ edrâke mâ': din günü / gece gelen", 'not': 'kalıp eşi.'},
 {'bag': '37:10 → 86:3', 'kural': "okuma — lemma 'sâqib' (ve kök ثقب) korpusun iki ayeti: alev / yıldız", 'not': 'lemma eşi.'},
 {'bag': '53:1 → 86:3', 'kural': "okuma — yıldız yemini: düşme anında / yeminin açıklaması", 'not': 'kurgu eşi.'},
 {'bag': '82:10 → 86:4', 'kural': "okuma — ''alâ' + zamir + 'hâfiz': üzerinizde gözetleyiciler / her canın üzerinde gözetleyici", 'not': 'kalıp eşi.'},
 {'bag': '83:33 → 86:4', 'kural': "okuma — ''alâ' + zamir + 'hâfiz': gönderilmediler / her canın üzerinde", 'not': 'kalıp eşi.'},
 {'bag': '85:22 → 86:4', 'kural': "okuma — kök حفظ sınırın iki yanında: 'mahfûz' / 'hâfiz' (aday 1040 ailesi)", 'not': 'kök eşi.'},
 {'bag': '80:24 → 86:5', 'kural': "okuma — harekesiz 'fe'l-yenzuri'l-insân' korpusun iki ayeti: yiyeceğine / neden yaratıldığına", 'not': 'kalıp eşi.'},
 {'bag': '77:20 → 86:6', 'kural': "okuma — 'min mâ'in' + nitelik: 'mehîn' / 'dâfiq'", 'not': 'kalıp eşi.'},
 {'bag': '32:8 → 86:6', 'kural': "okuma — 'min mâ'in mehîn' / 'min mâ'in dâfiq'", 'not': 'kalıp eşi.'},
 {'bag': '86:5 → 86:6', 'kural': "sûre içi — kök خلق [2/2]: soru / cevap (edilgen)", 'not': 'sûre içi eş.'},
 {'bag': '50:3 → 86:8', 'kural': "okuma — lemma 'rec'': inkârcıların sözü 'uzak bir dönüş' / geri döndürmeye gücü yeten", 'not': 'lemma eşi.'},
 {'bag': '75:40 → 86:8', 'kural': "okuma — 'qâdir' + 'alâ' + diriltme / geri döndürme", 'not': 'kurgu eşi.'},
 {'bag': '72:24 → 86:10', 'kural': "okuma — lemma 'nâsır': yardımcısı daha zayıf / ne gücü ne yardımcısı", 'not': 'lemma eşi.'},
 {'bag': '86:8 → 86:10', 'kural': "sûre içi — güç yetiren / gücü olmayan (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 # blok 11-17
 {'bag': '85:1 → 86:11', 'kural': "okuma — harekesiz 've's-semâ'i zât' ardışık iki sûrede: burçlar / dönüş (aday 1040 ailesi)", 'not': 'kalıp eşi.'},
 {'bag': '51:7 → 86:11', 'kural': "okuma — 've's-semâ'i zât' korpusun üç ayeti: örgü / dönüş", 'not': 'kalıp eşi.'},
 {'bag': '86:8 → 86:11', 'kural': "sûre içi — lemma 'rec'' [2/2]: insanın geri döndürülmesi / göğün niteliği", 'not': 'sûre içi eş.'},
 {'bag': '86:11 → 86:12', 'kural': "sûre içi — 'zât' + belirli ad: gök / yer (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '30:43 → 86:12', 'kural': "okuma — kök صدع: insanlar bölük bölük ayrılır / yerin yarılması", 'not': 'kök eşi.'},
 {'bag': '80:26 → 86:12', 'kural': "okuma — yerin yarılması: kök شقق, 1P etken / kök صدع, nitelik", 'not': 'kurgu eşi.'},
 {'bag': '69:40 → 86:13', 'kural': "okuma — harekesiz 'innehû le-qavl' korpusun üç ayeti: 'rasûlin kerîm' / 'fasl'", 'not': 'kalıp eşi.'},
 {'bag': '81:19 → 86:13', 'kural': "okuma — 'innehû le-qavl': 'rasûlin kerîm' / 'fasl'", 'not': 'kalıp eşi.'},
 {'bag': '77:13 → 86:13', 'kural': "okuma — lemma 'fasl': 'yevmu'l-fasl' / 'qavlun fasl'", 'not': 'lemma eşi.'},
 {'bag': '86:13 → 86:14', 'kural': "sûre içi — ayırıcı söz / şaka değil (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '52:42 → 86:15', 'kural': "okuma — 3MP + 'keyd': tuzak kurmak isteyenler tuzağa düşürülür / düzen kuruyorlar, 1S karşılık", 'not': 'kurgu eşi.'},
 {'bag': '86:15 → 86:16', 'kural': "sûre içi — kök كيد [4/4]: 3MP / 1S, aynı fiil ve mastar (aday 1039, okuma; aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '68:45 → 86:16', 'kural': "okuma — 1S 'keyd' + mühlet: 'umlî lehum inne keydî metîn' / 've ekîdu keydâ' + 86:17 'mehhil … emhil'", 'not': 'kurgu eşi.'},
 {'bag': '73:11 → 86:17', 'kural': "okuma — lemma 'mehhele' korpusun iki ayeti: 2MS'ye emir + mühlet + az ('qalîl' / 'ruveyd'); yalanlayıcılar / kâfirler", 'not': 'lemma eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_tarik', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in TARIK]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_tarik'] = TARIK
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_tarik', len(TARIK), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_tarik', len(BAGLAR['AS_tarik']))
