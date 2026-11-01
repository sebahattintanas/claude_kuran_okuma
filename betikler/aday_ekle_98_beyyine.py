# -*- coding: utf-8 -*-
"""aday_ekle_98_beyyine.py — sûre 98 (Beyyine) adayları (AX_beyyine) ve okuma bağları (AS_beyyine).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

BEYYINE = [
]

BAGLAR = {"AS_beyyine": [
 # blok 1-8
 {'bag': '97:5 → 98:1', 'kural': "okuma — ardışık sûre sınırı: fiilsiz 'hattâ' + tamlama ile kapanış / 'lem' + 'hattâ' + IMPF ile açılış; fâsıla ر → ة (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '59:2 → 98:1', 'kural': "okuma — 'ellezîne keferû min ehli'l-kitâb' (ölçüm xref): 'el-muşrikîn' yok / 've'l-muşrikîn' ile", 'not': 'kalıp eşi.'},
 {'bag': '90:13 → 98:1', 'kural': "okuma — kök فكك korpusun iki geçişi: 'fekku raqabe' boyun çözme / 'munfekkîn' ayrılma", 'not': 'kök eşi.'},
 {'bag': '20:133 → 98:1', 'kural': "okuma — 'beyyine' + 'suhuf': aynı ayette / 98:1-2 ardışık iki ayette", 'not': 'kuruluş eşi.'},
 {'bag': '98:1 → 98:6', 'kural': "sûre içi — harekesiz 'ellezîne keferû min ehli'l-kitâbi ve'l-muşrikîn' korpusun tamamı: 'lem yekun' ile / 'inne' ile (ölçüm nakarat3)", 'not': 'sûre içi eş.'},
 {'bag': '80:14 → 98:2', 'kural': "okuma — lemma 'suhuf' + 'mutahhara': 80:13-14 ardışık iki ayette / tek ayette", 'not': 'lemma eşi.'},
 {'bag': '65:11 → 98:2', 'kural': "okuma — 'resûl' + 'yetlû': nesne 'âyâti'llâh' / nesne 'suhufen'", 'not': 'kuruluş eşi.'},
 {'bag': '98:3 → 98:5', 'kural': "sûre içi — lemma 'qayyime' korpusun tamamı: kitaplar / din", 'not': 'sûre içi eş.'},
 {'bag': '98:1 → 98:4', 'kural': "sûre içi — 'el-beyyine' iki geçiş, ikisi de ayet sonunda: 'hattâ te'tiyehum' gelinceye kadar / 'min ba'di mâ câ'ethum' geldikten sonra (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '42:14 → 98:4', 'kural': "okuma — harekesiz 'illâ min ba'di mâ' + 'teferreqa': 'câ'ehumu'l-'ilm' + 'bağyen beynehum' / 'câ'ethumu'l-beyyine', gerekçesiz", 'not': 'kalıp eşi.'},
 {'bag': '45:17 → 98:4', 'kural': "okuma — harekesiz 'illâ min ba'di mâ': 'ixtelefû' + 'el-'ilm' / 'teferreqa' + 'el-beyyine'", 'not': 'kalıp eşi.'},
 {'bag': '40:14 → 98:5', 'kural': "okuma — harekesiz 'Allâhe muxlisîne lehu'd-dîn': IMPV 'fe'd'u' / 'li-ya'budû'", 'not': 'kalıp eşi.'},
 {'bag': '22:31 → 98:5', 'kural': "okuma — lemma 'hanîf' çoğul 'hunefâ'': 'li'llâhi ğayra muşrikîn' / 'muxlisîne lehu'd-dîn' ile", 'not': 'lemma eşi.'},
 {'bag': '98:1 → 98:5', 'kural': "sûre içi — kök أتي üç biçim: 'te'tiyehum' gelme / 98:4 'ûtû' verilme / 'yu'tû' verme", 'not': 'sûre içi eş.'},
 {'bag': '9:68 → 98:6', 'kural': "okuma — harekesiz 'nâri cehenneme' + 'xâlidîne fîhâ': vaat edilen / bulunulan yer", 'not': 'kalıp eşi.'},
 {'bag': '98:6 → 98:7', 'kural': "sûre içi — lemma 'beriyye' korpusun tamamı; aynı iskelet: 'keferû' / 'âmenû', 'şerr' / 'xayr' (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '85:11 → 98:7', 'kural': "okuma — harekesiz 'inne'llezîne âmenû ve 'amilu's-sâlihât': ardından 'lehum cennât' / 'ulâ'ike hum xayru'l-beriyye'", 'not': 'kalıp eşi.'},
 {'bag': '20:76 → 98:8', 'kural': "okuma — harekesiz 'cennâtu 'adnin tecrî min tahtihe'l-enhâr' korpusun iki geçişi: 'zâlike cezâ'u men tezekkâ' / 'cezâ'uhum' + 'zâlike li-men xaşiye rabbeh'", 'not': 'kalıp eşi.'},
 {'bag': '9:100 → 98:8', 'kural': "okuma — harekesiz 'radiya'llâhu 'anhum ve radû 'anh' + 'xâlidîne fîhâ ebedâ' aynı ayette; 'tecrî tahtehâ' ('min' yok) / 'tecrî min tahtihâ'", 'not': 'kalıp eşi.'},
 {'bag': '58:22 → 98:8', 'kural': "okuma — harekesiz 'radiya'llâhu 'anhum ve radû 'anh': ardından 'ulâ'ike hizbu'llâh' / 'zâlike li-men xaşiye rabbeh'", 'not': 'kalıp eşi.'},
 {'bag': '79:26 → 98:8', 'kural': "okuma — 'zâlike' + 'li-men' + lemma 'xaşiye': IMPF nesnesiz / PERF + 'rabbehû'", 'not': 'kuruluş eşi.'},
 {'bag': '98:6 → 98:8', 'kural': "sûre içi — 'xâlidîne fîhâ': 'ebeden' yok / 'ebeden' ile; 'nâri cehennem' / 'cennâtu 'adn' (aday 1039, okuma)", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_beyyine', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in BEYYINE]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_beyyine'] = BEYYINE
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_beyyine', len(BEYYINE), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_beyyine', len(BAGLAR['AS_beyyine']))
