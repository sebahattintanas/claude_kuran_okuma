# -*- coding: utf-8 -*-
"""aday_ekle_93_duha.py — sûre 93 (Duhâ) adayları (AX_duha) ve okuma bağları (AS_duha).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

DUHA = [
]

BAGLAR = {"AS_duha": [
 # blok 1-11
 {'bag': '92:21 → 93:1', 'kural': "okuma — ardışık sûre sınırı: öznesi yazılmamış 'hoşnut olacak' ile kapanış / kuşluğa yemin ile açılış; fâsıla ى → ى (aday 1040, kayıt)", 'not': 'sınır eşi.'},
 {'bag': '91:1 → 93:1', 'kural': "okuma — lemma 'duhâ' yeminde: güneşe atıflı 'duhâhâ' / tek başına 'ed-duhâ'", 'not': 'lemma eşi.'},
 {'bag': '81:17 → 93:2', 'kural': "okuma — harekesiz 've'l-leyli izâ' + fiil: ''as'as' / 'secâ'", 'not': 'kalıp eşi.'},
 {'bag': '89:4 → 93:2', 'kural': "okuma — harekesiz 've'l-leyli izâ' + fiil: 'yesr' / 'secâ'", 'not': 'kalıp eşi.'},
 {'bag': '91:4 → 93:2', 'kural': "okuma — harekesiz 've'l-leyli izâ' + fiil: 'yağşâhâ' / 'secâ' (korpusun beş geçişinden üçü 91-93'te)", 'not': 'kalıp eşi.'},
 {'bag': '92:1 → 93:2', 'kural': "okuma — ardışık sûre, harekesiz 've'l-leyli izâ' + fiil: 'yağşâ' / 'secâ' (aday 1040, okuma bağı)", 'not': 'kalıp eşi.'},
 {'bag': '93:1 → 93:2', 'kural': "sûre içi — kuşluk / gece (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '26:168 → 93:3', 'kural': "okuma — kök قلي korpusun iki ayeti: konuşanın kendisi için 'el-qâlîn' / Rab'ın 'qalâ'sı olumsuz (aday 1041, sûreler arası okuma notu)", 'not': 'kök eşi.'},
 {'bag': '17:21 → 93:4', 'kural': "okuma — harekesiz 've le'l-âxiratu' korpusun iki ayeti: derece ve üstünlükte daha büyük / ilkinden hayırlı", 'not': 'kalıp eşi.'},
 {'bag': '92:13 → 93:4', 'kural': "okuma — ardışık sûre, 'âxira' + 'ûlâ': ikisi de 1P'nin / âhiret ilkinden hayırlı (aday 1040, okuma bağı)", 'not': 'lemma eşi.'},
 {'bag': '92:21 → 93:5', 'kural': "okuma — harekesiz 've le-sevfe' korpusun iki ayeti, ardışık sûrede, ikisinde de 'radiye': 3MS / 2MS (aday 1040, okuma bağı)", 'not': 'kalıp eşi.'},
 {'bag': '92:5 → 93:5', 'kural': "okuma — ardışık sûre, lemma 'a'tâ': insan verir / Rab 2MS'ye verecek (aday 1041, sûreler arası okuma notu)", 'not': 'lemma eşi.'},
 {'bag': '89:17 → 93:6', 'kural': "okuma — lemma 'yetîm': yetime ikram etmeyen 2MP / 2MS yetim bulundu", 'not': 'lemma eşi.'},
 {'bag': '90:15 → 93:6', 'kural': "okuma — lemma 'yetîm': doyurulacak yakın yetim / 2MS yetim bulundu", 'not': 'lemma eşi.'},
 {'bag': '70:13 → 93:6', 'kural': "okuma — lemma 'âvâ': akraba barındırır / 3MS 2MS'yi barındırdı", 'not': 'lemma eşi.'},
 {'bag': '93:6 → 93:8', 'kural': "sûre içi — lemma 'vecede' + 2MS + nekre ad + 'fe' + PERF 3MS, üç ardışık ayet (93:6-8)", 'not': 'sûre içi eş.'},
 {'bag': '92:12 → 93:7', 'kural': "okuma — ardışık sûre, kök هدي: 1P'ye düşen yol göstermek / 3MS 2MS'ye yol gösterdi", 'not': 'kök eşi.'},
 {'bag': '9:28 → 93:8', 'kural': "okuma — kök عيل korpusun iki ayeti + kök غني: lafız zenginleştirecek (2MP) / 3MS zenginleştirdi (2MS)", 'not': 'kök eşi.'},
 {'bag': '69:28 → 93:8', 'kural': "okuma — lemma 'ağnâ': malı yarar sağlamadı (1S) / 3MS zenginleştirdi", 'not': 'lemma eşi.'},
 {'bag': '92:8 → 93:8', 'kural': "okuma — ardışık sûre, kök غني: kendini yeterli gören insan / 3MS zenginleştirdi (aday 1041, sûreler arası okuma notu)", 'not': 'kök eşi.'},
 {'bag': '92:11 → 93:8', 'kural': "okuma — ardışık sûre, kök غني: malı yetmez / 3MS zenginleştirdi; morph iki lemma etiketi (924)", 'not': 'kök eşi.'},
 {'bag': '93:6 → 93:9', 'kural': "sûre içi — lemma 'yetîm' iki geçiş: 2MS yetim bulundu / yetimi ezme", 'not': 'sûre içi eş.'},
 {'bag': '12:39 → 93:9', 'kural': "okuma — kök قهر: lafzın sıfatı 'el-qahhâr' / 2MS'ye yasak 'lâ teqhar' (aday 1041, sûreler arası okuma notu)", 'not': 'kök eşi.'},
 {'bag': '92:5 → 93:9', 'kural': "okuma — ardışık sûre, 'emmâ': 'emmâ' + 'men' / 'emmâ' + belirli ad", 'not': 'kalıp eşi.'},
 {'bag': '17:23 → 93:10', 'kural': "okuma — lemma 'tenhar' korpusun iki ayeti, ikisi de yasak: ana-baba / isteyen", 'not': 'lemma eşi.'},
 {'bag': '70:25 → 93:10', 'kural': "okuma — lemma 'sâ'il': mallarında hak sahibi isteyen / azarlanmayacak isteyen", 'not': 'lemma eşi.'},
 {'bag': '92:2 → 93:10', 'kural': "okuma — ardışık sûre, kök نهر iki anlamda: gündüz / azarlama", 'not': 'kök eşi.'},
 {'bag': '93:9 → 93:10', 'kural': "sûre içi — 'emmâ' + belirli ad + 'fe-lâ' + IMPF aynı iskelet: yetim / isteyen", 'not': 'sûre içi eş.'},
 {'bag': '68:2 → 93:11', 'kural': "okuma — harekesiz 'bi-ni'meti rabbike' korpusun iki ayeti: deli değilsin / anlat", 'not': 'kalıp eşi.'},
 {'bag': '92:19 → 93:11', 'kural': "okuma — ardışık sûre, lemma 'ni'meh': karşılığı verilecek nimet yok / Rab nimetini anlat", 'not': 'lemma eşi.'},
 {'bag': '93:3 → 93:11', 'kural': "sûre içi — lemma 'rabb' + 2MS [3/3] (93:3, 5, 11)", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_duha', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in DUHA]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_duha'] = DUHA
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_duha', len(DUHA), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_duha', len(BAGLAR['AS_duha']))
