# -*- coding: utf-8 -*-
"""aday_ekle_83_mutaffifin.py — sûre 83 (Mutaffifîn) adayları (AX_mutaffifin) ve okuma bağları (AS_mutaffifin).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

MUTAFFIFIN = [
]

BAGLAR = {"AS_mutaffifin": [
 # blok 1-10
 {'bag': '82:19 → 83:1', 'kural': "okuma — ardışık sûre sınırı: 'li' + lafız ile kapanış / 'veyl' + 'li' + ortaç ile açılış; fâsıla ه → ن (aday 1040, kayıt)", 'not': 'sınır.'},
 {'bag': '12:63 → 83:2', 'kural': "okuma — lemma 'iktâle' korpusun iki ayeti: ölçek almak isteyen kardeşler / insanlardan tam alanlar", 'not': 'lemma eşi.'},
 {'bag': '17:35 → 83:3', 'kural': "okuma — 'keyl' + 'vezene' emirde (tam ölçün, doğru tartın) / eksik ölçüp tartma", 'not': 'kurgu eşi.'},
 {'bag': '26:181 → 83:2', 'kural': "okuma — 'evfu'l-keyl' + 'muxsirîn': emir / 'yestevfûn' + 'yuxsirûn' fiil", 'not': 'kurgu eşi.'},
 {'bag': '26:182 → 83:3', 'kural': "okuma — lemma 'vezene': doğru teraziyle tartın / tartıp eksik verme", 'not': 'lemma eşi.'},
 {'bag': '55:9 → 83:3', 'kural': "okuma — lemma 'axsara' korpusun iki ayeti: yasak (2MP) / fiil (3MP)", 'not': 'lemma eşi.'},
 {'bag': '83:2 → 83:3', 'kural': "sûre içi — alırken tam / verirken eksik; kök كيل [2/2] (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '56:47 → 83:4', 'kural': "okuma — lemma 'meb'ûth': inkârcıların sorusu (1P) / onlara yöneltilen soru (3MP)", 'not': 'lemma eşi.'},
 {'bag': '78:38 → 83:6', 'kural': "okuma — harekesiz 'yevme yeqûm' (4 ayet): rûh ve melekler / insanlar", 'not': 'kalıp eşi.'},
 {'bag': '40:51 → 83:6', 'kural': "okuma — harekesiz 'yevme yeqûm': şahitler / insanlar", 'not': 'kalıp eşi.'},
 {'bag': '40:66 → 83:6', 'kural': "okuma — harekesiz 'li-rabbi'l-'âlemîn' (4 ayet): teslim olmak / kalkmak", 'not': 'kalıp eşi.'},
 {'bag': '83:2 → 83:6', 'kural': "sûre içi — kök أنس [2/2]: ölçüp aldıkları insanlar / Rabbe kalkan insanlar", 'not': 'sûre içi eş.'},
 {'bag': '82:14 → 83:7', 'kural': "okuma — ardışık sûrede iskelet 'inne' + 'el-fuccâr' + 'le-fî' + nekre: cehennem / siccîn (aday 1040, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '38:28 → 83:7', 'kural': "okuma — lemma 'fuccâr' (4 ayet; 83:7 korpusun son geçişi)", 'not': 'lemma eşi.'},
 {'bag': '82:17 → 83:8', 'kural': "okuma — ardışık sûrede 've mâ edrâke mâ' + âhiret adı: 'yevmu'd-dîn' / 'siccîn' (aday 1040 ailesi)", 'not': 'kalıp eşi.'},
 {'bag': '83:7 → 83:9', 'kural': "sûre içi — 'kitâb' + 'siccîn' sorusu + 'kitâbun merqûm' cevabı (83:7-9)", 'not': 'sûre içi eş.'},
 {'bag': '77:15 → 83:10', 'kural': "ölçüm esit2 TAM — 'veylun yevme'izin li'l-mukezzibîn' (sûre 77 nakaratı, 10 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '52:11 → 83:10', 'kural': "okuma — 'fe-veylun' / 'veylun' + 'yevme'izin li'l-mukezzibîn'", 'not': 'kalıp eşi.'},
 {'bag': '83:1 → 83:10', 'kural': "sûre içi — 'veyl' [2/2]: eksik ölçenler / yalanlayanlar", 'not': 'sûre içi eş.'},
 # blok 11-20
 {'bag': '74:46 → 83:11', 'kural': "ölçüm xref — 'kezzebe bi-yevmi'd-dîn': cehennemliklerin 1P itirafı / 3MP tarif", 'not': 'kalıp eşi.'},
 {'bag': '82:9 → 83:11', 'kural': "okuma — ardışık sûrede 'kezzebe bi'd-dîn': 2MP / 3MP (aday 1040 ailesi)", 'not': 'kalıp eşi.'},
 {'bag': '68:12 → 83:12', 'kural': "okuma — 'mu'tedin esîm' ikilisi; 68:12 / 68:15 ve 83:12 / 83:13 sırası", 'not': 'kurgu eşi.'},
 {'bag': '68:15 → 83:13', 'kural': "ölçüm esit2 TAM — 'izâ tutlâ 'aleyhi âyâtunâ qâle esâtîru'l-evvelîn'", 'not': 'kalıp eşi.'},
 {'bag': '31:7 → 83:13', 'kural': "okuma — harekesiz 'izâ tutlâ 'aleyhi âyâtunâ' (3 ayet): sırt dönme / 'masallar' sözü", 'not': 'kalıp eşi.'},
 {'bag': '82:9 → 83:14', 'kural': "okuma — harekesiz 'kellâ bel', ardışık sûrede", 'not': 'kalıp eşi.'},
 {'bag': '83:6 → 83:15', 'kural': "sûre içi — kök ربب [2/2]: insanlar Rabbe kalkar / yalanlayanlar Rablerinden perdelenmiş", 'not': 'sûre içi eş.'},
 {'bag': '38:59 → 83:16', 'kural': "okuma — lemma 'sâl' korpusun iki ayeti: ateş / cehennem", 'not': 'lemma eşi.'},
 {'bag': '82:14 → 83:16', 'kural': "okuma — ardışık sûrede günahkârlar + 'cahîm' + kök صلي (aday 1040 ailesi)", 'not': 'kurgu eşi.'},
 {'bag': '37:21 → 83:17', 'kural': "okuma — 'hâzâ … ellezî kuntum bihî tukezzibûn': ayırma günü / gönderge adsız", 'not': 'kalıp eşi.'},
 {'bag': '77:29 → 83:17', 'kural': "okuma — harekesiz 'kuntum bihî tukezzibûn' (4 ayet)", 'not': 'kalıp eşi.'},
 {'bag': '83:10 → 83:17', 'kural': "sûre içi — kök كذب [4/4]: yalanlayanlar (83:10-12, 17)", 'not': 'sûre içi eş.'},
 {'bag': '83:7 → 83:18', 'kural': "sûre içi — ölçüm nakarat3 'kellâ inne kitâb': günahkârlar, siccîn / iyiler, 'illiyyîn (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '82:13 → 83:18', 'kural': "okuma — ardışık sûrede iyiler / günahkârlar ikilisi 'inne' + 'le-fî' (82:13-14 / 83:7, 18; sıra ters) (aday 1040, kayıt)", 'not': 'kurgu eşi.'},
 {'bag': '83:8 → 83:19', 'kural': "sûre içi — 've mâ edrâke mâ': siccîn / 'illiyyûn (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '83:9 → 83:20', 'kural': "ölçüm esit2 TAM — 'kitâbun merqûm'; 83:7-9 / 83:18-20 üç ayetlik dizi aynı sırayla", 'not': 'sûre içi eş.'},
 # blok 21-28
 {'bag': '56:11 → 83:21', 'kural': "okuma — lemma 'muqarrab': üç grubun biri / kitaba tanık olanlar", 'not': 'lemma eşi.'},
 {'bag': '82:13 → 83:22', 'kural': "ölçüm esit2 TAM — 'inne'l-ebrâra le-fî na'îm', ardışık sûrede (aday 1040, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '83:18 → 83:22', 'kural': "sûre içi — kök برر [2/2]: iyilerin kitabı / iyiler", 'not': 'sûre içi eş.'},
 {'bag': '76:13 → 83:23', 'kural': "okuma — harekesiz ''ale'l-erâ'ik' (5 ayet): yaslanırlar / bakarlar", 'not': 'kalıp eşi.'},
 {'bag': '75:22 → 83:24', 'kural': "okuma — kök نضر korpusun üç ayeti: yüz + parlaklık (sıfat / ad)", 'not': 'kök eşi.'},
 {'bag': '76:11 → 83:24', 'kural': "okuma — lemma 'nadra' korpusun iki ayeti", 'not': 'lemma eşi.'},
 {'bag': '76:17 → 83:25', 'kural': "okuma — 'yusqavne' + 'mizâc' (76:17 / 83:25, 27); 83:25 'suqiye' lemmasının korpustaki son geçişi", 'not': 'kurgu eşi.'},
 {'bag': '83:25 → 83:26', 'kural': "sûre içi — kök ختم [2/2]: 'maxtûm' / 'xitâm'", 'not': 'sûre içi eş.'},
 {'bag': '76:5 → 83:27', 'kural': "okuma — lemma 'mizâc' korpusun üç ayeti (kâfûr / zencebîl / tesnîm)", 'not': 'lemma eşi.'},
 {'bag': '76:6 → 83:28', 'kural': "okuma — harekesiz ''aynen yeşrabu bihâ' korpusun iki ayeti: 'ibâdu'llâh / el-muqarrabûn; 76:5-6 / 83:27-28 'mizâc' + pınar sırası", 'not': 'kalıp eşi.'},
 {'bag': '83:21 → 83:28', 'kural': "sûre içi — kök قرب [2/2]: 'el-muqarrabûn' tanık olur / içer", 'not': 'sûre içi eş.'},
 # blok 29-36
 {'bag': '23:110 → 83:29', 'kural': "okuma — 'min' + gülme, geçmişte süren: 2MP hitap / 3MP anlatı", 'not': 'kurgu eşi.'},
 {'bag': '83:29 → 83:34', 'kural': "sûre içi — kök ضحك [2/2]: suçlular müminlere gülerdi / bugün müminler kâfirlere güler — roller ters (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '44:27 → 83:31', 'kural': "okuma — kök فكه: 'fâkihîn' dünyada keyif / 'fekihîn' eve keyifli dönüş", 'not': 'kök eşi.'},
 {'bag': '52:18 → 83:31', 'kural': "okuma — kök فكه: cennette keyif / dünyada alaycı keyif", 'not': 'kök eşi.'},
 {'bag': '83:14 → 83:31', 'kural': "sûre içi — kök قلب [3/3]: kalpler / dönme (1021)", 'not': 'sûre içi eş.'},
 {'bag': '68:26 → 83:32', 'kural': "ölçüm xref — görünce + 'qâlû' + 'le-dâllûn': kendileri için (1P) / müminler için", 'not': 'kalıp eşi.'},
 {'bag': '83:13 → 83:32', 'kural': "sûre içi — kök قول [3/3]: 'qâle' / 'yuqâlu' / 'qâlû'", 'not': 'sûre içi eş.'},
 {'bag': '82:10 → 83:33', 'kural': "okuma — ardışık sûrede 'alâ' + zamir + 'hâfizîn': gözetleyiciler var / gözetleyici gönderilmediler (aday 1040 ailesi)", 'not': 'kalıp eşi.'},
 {'bag': '83:23 → 83:35', 'kural': "ölçüm esit2 TAM — ''ale'l-erâ'iki yenzurûn': iyiler / iman edenler", 'not': 'sûre içi eş.'},
 {'bag': '83:34 → 83:36', 'kural': "sûre içi — kök كفر [2/2]: 'el-kuffâr' gülünenler / karşılık görenler", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_mutaffifin', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in MUTAFFIFIN]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_mutaffifin'] = MUTAFFIFIN
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_mutaffifin', len(MUTAFFIFIN), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_mutaffifin', len(BAGLAR['AS_mutaffifin']))
