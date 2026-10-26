# -*- coding: utf-8 -*-
"""aday_ekle_73_muzzemmil.py — sûre 73 (Müzzemmil) adayları (AX_muzzemmil) ve okuma bağları (AS_muzzemmil).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

MUZZEMMIL = [
]

BAGLAR = {"AS_muzzemmil": [
 # blok 1-10
 {'bag': '72:28 → 73:1', 'kural': "okuma — ardışık sûre sınırı; 3MS anlatımla kapanış / 2MS nidâ ile açılış; fâsıla ا → ل (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '25:32 → 73:4', 'kural': "okuma — 'rattele + tertîl': 1P 'rattelnâhu' / 2MS 'rattil'; lemmanın korpustaki iki ayeti", 'not': 'kalıp eşi.'},
 {'bag': '17:9 → 73:6', 'kural': "okuma — 'aqvem' ism tafdîl: Kur'an'ın hidayeti / gece kalkışının sözü", 'not': 'lemma eşi.'},
 {'bag': '73:6 → 73:7', 'kural': "sûre içi — gece / gündüz iki ayete bölünmüş çift", 'not': 'sûre içi eş.'},
 {'bag': '26:28 → 73:9', 'kural': "xref (ölçüm) 'rabb + meşriq + mağrib' — tekil / tekil", 'not': 'kalıp eşi.'},
 {'bag': '70:40 → 73:9', 'kural': "xref (ölçüm) 'rabb + meşriq + mağrib' — çoğul / tekil", 'not': 'kalıp eşi.'},
 {'bag': '55:17 → 73:9', 'kural': "okuma — doğu / batı ikil / tekil; rubûbiyet tamlaması", 'not': 'kurgu eşi.'},
 {'bag': '73:8 → 73:9', 'kural': "sûre içi — 'rabbike' → 'rabbu'l-meşriq' bedel / haber", 'not': 'sûre içi eş.'},
 {'bag': '20:130 → 73:10', 'kural': "okuma — 'sabera + alâ + mâ + qâle' + ardından tesbih emri / burada 'hecr'", 'not': 'kalıp eşi.'},
 {'bag': '38:17 → 73:10', 'kural': "okuma — 'sabera + alâ + mâ + qâle' + ardından zikir emri / burada 'hecr'", 'not': 'kalıp eşi.'},
 {'bag': '50:39 → 73:10', 'kural': "okuma — 'sabera + alâ + mâ + qâle' + ardından tesbih emri / burada 'hecr'", 'not': 'kalıp eşi.'},
 {'bag': '19:46 → 73:10', 'kural': "okuma — 'uhcur' emri: babadan oğula / 2MS'ye", 'not': 'lemma eşi.'},
 {'bag': '70:5 → 73:10', 'kural': "okuma — sabır emri + 'cemîl'; ardışık olmayan sûre (1040 değil)", 'not': 'kurgu eşi.'},
 {'bag': '73:5 → 73:10', 'kural': "sûre içi — قول 'qavl' (1P'nin bırakacağı) / 'yeqûlûn' (onların sözü)", 'not': 'sûre içi eş.'},
 # blok 11-19
 {'bag': '73:10 → 73:11', 'kural': "sûre içi — 'mâ yeqûlûn' söyleyenleri → 'el-mukezzibîn' (KAPATILAMAZ)", 'not': 'sûre içi eş.'},
 {'bag': '44:27 → 73:11', 'kural': "okuma — lemma 'na'me' iki ayet: bırakılan nimet / yalanlayanların sıfatı", 'not': 'lemma eşi.'},
 {'bag': '73:12 → 73:13', 'kural': "sûre içi — 'ledeynâ' altında dört ma'tûf (enkâl, cahîm, ta'âm, 'azâb)", 'not': 'sûre içi eş.'},
 {'bag': '69:14 → 73:14', 'kural': "okuma — 'ard + cebel': kaldırılıp ezilme / sarsılıp kum yığını", 'not': 'kurgu eşi.'},
 {'bag': '51:38 → 73:15', 'kural': "okuma — 'ersele + ilâ + fir'avn': elçi adlı / adsız", 'not': 'kalıp eşi.'},
 {'bag': '73:15 → 73:16', 'kural': "sûre içi — 'rasûlâ' → 'er-rasûl' belirli tekrar", 'not': 'sûre içi eş.'},
 {'bag': '54:42 → 73:16', 'kural': "okuma — 'ehaze + ahz' mef'ûl mutlak", 'not': 'kalıp eşi.'},
 {'bag': '69:10 → 73:16', 'kural': "okuma — ''asâ + rasûl + ehaze + mef'ûl mutlak' aynı dizi", 'not': 'kurgu eşi.'},
 {'bag': '26:18 → 73:17', 'kural': "okuma — lemma 'velîd': bir kişinin çocukluğu / çocuklar topluca", 'not': 'lemma eşi.'},
 {'bag': '73:14 → 73:17', 'kural': "sûre içi — 'yevme' zarf / 'yevmen' meful", 'not': 'sûre içi eş.'},
 {'bag': '17:5 → 73:18', 'kural': "xref (ölçüm) 'kâne + va'd + mef'ûl'", 'not': 'kalıp eşi.'},
 {'bag': '25:57 → 73:19', 'kural': "xref (ölçüm) 'ittehaze + ilâ + rabb + sebîl' — istisna içinde / şart cevabı", 'not': 'kalıp eşi.'},
 {'bag': '69:48 → 73:19', 'kural': "okuma — 'inne + tezkira' haber", 'not': 'lemma eşi.'},
 {'bag': '73:8 → 73:19', 'kural': "sûre içi — ذكر 'vezkur' / 'tezkira'; Rab", 'not': 'sûre içi eş.'},
 {'bag': '73:9 → 73:19', 'kural': "sûre içi — أخذ 'fe'ttehizhu vekîlâ' / 'ittehaze … sebîlâ'", 'not': 'sûre içi eş.'},
 # blok 20-20
 {'bag': '73:2 → 73:20', 'kural': "sûre içi — gece kalkışı emri ('qumi'l-leyl') / bildirimi ('tequmu ednâ min sulusey'l-leyl')", 'not': 'sûre içi eş.'},
 {'bag': '73:3 → 73:20', 'kural': "sûre içi — lemma 'nisf' iki geçiş: gecenin yarısı emirde / bildirimde", 'not': 'sûre içi eş.'},
 {'bag': '73:4 → 73:20', 'kural': "sûre içi — 'rattili'l-qur'ân' / 'fe'qra'û mâ teyessera mine'l-qur'ân'", 'not': 'sûre içi eş.'},
 {'bag': '73:9 → 73:20', 'kural': "sûre içi — iki geçerli mühür: 'vekîl' / 'ğafûr rahîm'; أله 'ilâh' → lafız ×7", 'not': 'sûre içi eş.'},
 {'bag': '27:74 → 73:20', 'kural': "okuma — 'inne + rabb + 'alime' (2MS'ye)", 'not': 'kalıp eşi.'},
 {'bag': '72:28 → 73:20', 'kural': "okuma — lemma 'ahsâ': her şeyi sayan 3MS / sayamayacak 2MP (ardışık sûre, okuma bağı; 1040 sûre sınırı değil)", 'not': 'lemma eşi.'},
 {'bag': '9:102 → 73:20', 'kural': "okuma — 've âharûne' + tevbe ('tâbe + alâ') + 'inna'llâhe ğafûrun rahîm'", 'not': 'kurgu eşi.'},
 {'bag': '62:10 → 73:20', 'kural': "xref (ölçüm) 'ard + ibteğâ + fadl' — yeryüzünde Allah'ın lütfunu arama", 'not': 'kalıp eşi.'},
 {'bag': '57:11 → 73:20', 'kural': "okuma — 'aqrada + Allâh + qard + hasen'", 'not': 'kalıp eşi.'},
 {'bag': '57:18 → 73:20', 'kural': "okuma — 'aqrada + Allâh + qard + hasen'", 'not': 'kalıp eşi.'},
 {'bag': '64:17 → 73:20', 'kural': "okuma — 'aqrada + Allâh + qard + hasen'; ardından kat kat artırma / burada 'tecidûhu 'inda'llâh'", 'not': 'kalıp eşi.'},
 {'bag': '71:10 → 73:20', 'kural': "okuma — 'istağfirû' + ğfr sıfatı (ğaffâr / ğafûr); Rab / lafız; ardışık olmayan sûre (1040 değil)", 'not': 'kurgu eşi.'},
 {'bag': '36:39 → 73:20', 'kural': "okuma — 'qaddara' + zaman olgusu (ay menzilleri / gece-gündüz); çıpa L1 emsali", 'not': 'lemma eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_muzzemmil', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in MUZZEMMIL]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_muzzemmil'] = MUZZEMMIL
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_muzzemmil', len(MUZZEMMIL), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_muzzemmil', len(BAGLAR['AS_muzzemmil']))
