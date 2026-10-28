# -*- coding: utf-8 -*-
"""aday_ekle_76_insan.py — sûre 76 (İnsân) adayları (AX_insan) ve okuma bağları (AS_insan).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

INSAN = [
]

BAGLAR = {"AS_insan": [
 # blok 1-10
 {'bag': '75:40 → 76:1', 'kural': "okuma — ardışık sûre sınırı; iki yan da soru: ölüleri diriltme gücü / insanın anılmadığı süre; fâsıla ى → ا (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '75:36 → 76:1', 'kural': "okuma — ardışık sûre: 75:36-37 'el-insân' + 'nutfe' / 76:1-2 'el-insân' + 'nutfe', sınırın iki yanında aynı iki ad aynı sırada (aday 1040, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '19:67 → 76:1', 'kural': "okuma — 'lem yeku şey'â' / 'lem yekun şey'en mezkûrâ' (lemma dizisi 'kâne + şey'')", 'not': 'kalıp eşi.'},
 {'bag': '45:24 → 76:1', 'kural': "okuma — lemma 'dehr' korpusun iki ayeti: inkârcıların sözünde helâk edici / insanın anılmadığı süre", 'not': 'lemma eşi.'},
 {'bag': '16:4 → 76:2', 'kural': "ölçüm xref — 'xalaqa + insân + min nutfe': sonuç 'apaçık hasım' / 'işiten, gören'", 'not': 'xref.'},
 {'bag': '75:37 → 76:2', 'kural': "okuma — kök نطف: 'nutfeten min meniyyin yumnâ' / 'nutfetin emşâc' (ardışık sûre, okuma bağı)", 'not': 'kök eşi.'},
 {'bag': '42:11 → 76:2', 'kural': "okuma — lemma dizisi 'semî' + basîr': belirli, haber, Allah / nekre, ikinci meful, insan (1041 ailesi, sûre dışı)", 'not': 'kalıp eşi.'},
 {'bag': '17:67 → 76:3', 'kural': "okuma — lemma 'kefûr': insan için haber / insanın iki hâlinden biri", 'not': 'lemma eşi.'},
 {'bag': '76:3 → 76:5', 'kural': "sûre içi — kök كفر ardışık üç ayette üç kelime: 'kefûr' / 'kâfirîn' / 'kâfûr' (kök sayımı birlikte sayıyor)", 'not': 'sûre içi eş.'},
 {'bag': '40:71 → 76:4', 'kural': "okuma — 'ağlâl' + 'selâsil' / 'selâsil' + 'ağlâl' (sıra ters)", 'not': 'kalıp eşi.'},
 {'bag': '76:4 → 76:5', 'kural': "sûre içi — 'el-kâfirîn' / 'el-ebrâr' karşıt çift (aday 1039)", 'not': 'sûre içi eş.'},
 {'bag': '37:45 → 76:5', 'kural': "okuma — lemma 'ke's': kadeh dolaştırılıyor (edilgen) / iyiler içiyor", 'not': 'lemma eşi.'},
 {'bag': '17:91 → 76:6', 'kural': "okuma — lemma 'tefcîr' korpusun iki ayeti: inkârcıların 2MS'den istediği ırmak fışkırtma / kulların cennette pınar fışkırtması", 'not': 'lemma eşi.'},
 {'bag': '75:5 → 76:6', 'kural': "okuma — kök فجر: 'li-yefcure' (fucûr) / 'yufeccirûnehâ' (fışkırtma) — ardışık sûre, aynı kök iki anlam", 'not': 'kök eşi.'},
 {'bag': '74:44 → 76:8', 'kural': "okuma — 'at'ame + miskîn': suçluların yapmadığı / iyilerin yaptığı", 'not': 'kurgu eşi.'},
 {'bag': '30:39 → 76:9', 'kural': "okuma — 'vechallâh': 2MP 'turîdûne vechallâh' / 1P 'li-vechi'llâh'", 'not': 'kalıp eşi.'},
 {'bag': '25:62 → 76:9', 'kural': "okuma — lemma 'şukûr' korpusun iki ayeti: 'erâde şukûrâ' / 'lâ nurîdu … şukûrâ'", 'not': 'lemma eşi.'},
 {'bag': '76:8 → 76:9', 'kural': "sûre içi — kök طعم üç geçiş: 'yut'imûne't-ta'âm' (anlatım) / 'nut'imukum' (iyilerin sözü)", 'not': 'sûre içi eş.'},
 {'bag': '76:3 → 76:9', 'kural': "sûre içi — kök شكر: 'şâkir' (insanın hâli) / 'şukûr' (teşekkür)", 'not': 'sûre içi eş.'},
 {'bag': '76:7 → 76:10', 'kural': "sûre içi — kök خوف iki geçiş + 'yevmen': 3MP anlatım / 1P kendi sözü", 'not': 'sûre içi eş.'},
 {'bag': '74:22 → 76:10', 'kural': "okuma — kök عبس: kişinin kaş çatması (fiil) / günün sıfatı ''abûs'", 'not': 'kök eşi.'},
 # blok 11-20
 {'bag': '76:7 → 76:11', 'kural': "sûre içi — kök شرر iki geçiş: korkulan günün kötülüğü / o günün kötülüğünden korunma", 'not': 'sûre içi eş.'},
 {'bag': '76:10 → 76:11', 'kural': "sûre içi — iyilerin sözü 76:10'da bitiyor, 76:11 anlatıcı sesi (alıntı kapanışı metinle; 1017); 'yevmen 'abûsen' / 'nadraten ve surûrâ' karşıt çift (aday 1039)", 'not': 'sûre içi eş.'},
 {'bag': '75:22 → 76:11', 'kural': "okuma — kök نضر: 'nâdira' (yüzlerin sıfatı) / 'nadra' (kavuşturulan parlaklık) — ardışık sûre, okuma bağı", 'not': 'kök eşi.'},
 {'bag': '76:9 → 76:12', 'kural': "sûre içi — kök جزي: insanlardan istenmeyen karşılık / Allah'ın karşılığı (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '18:31 → 76:13', 'kural': "okuma — 'muttaki'îne fîhâ 'ale'l-erâ'ik' korpusun iki ayeti: altın bilezik ve ipekle / güneş ve soğuğun yokluğuyla", 'not': 'kalıp eşi.'},
 {'bag': '69:23 → 76:14', 'kural': "okuma — lemma 'qutûf' korpusun iki ayeti, ikisinde de 'dâniye': salkımlar yakın / gölgeler yakın, salkımlar boyun eğdirilmiş", 'not': 'lemma eşi.'},
 {'bag': '43:71 → 76:15', 'kural': "okuma — 'yutâfu 'aleyhim' + kap + 'min' + maden + 've ekvâb': altın / gümüş", 'not': 'kalıp eşi.'},
 {'bag': '37:45 → 76:15', 'kural': "okuma — 'yutâfu 'aleyhim bi-': kadeh / gümüş kaplar", 'not': 'kalıp eşi.'},
 {'bag': '27:44 → 76:15', 'kural': "okuma — lemma 'qavârîr' korpusun üç ayeti: camdan köşk / gümüşten billurlar (76:15-16 art arda)", 'not': 'lemma eşi.'},
 {'bag': '76:15 → 76:16', 'kural': "sûre içi — 'qavârîrâ' bir ayetin son, ötekinin ilk kelimesi", 'not': 'sûre içi eş.'},
 {'bag': '36:38 → 76:16', 'kural': "okuma — lemma 'taqdîr': esmâya izâfetle güneşin yolu / 3MP'nin kapları ölçmesi (1041 ailesi, sûre dışı)", 'not': 'lemma eşi.'},
 {'bag': '76:5 → 76:17', 'kural': "ölçüm nakarat3 — 'ke's + kâne + mizâc': kâfûr, etken / zencebîl, edilgen", 'not': 'nakarat3.'},
 {'bag': '76:6 → 76:18', 'kural': "sûre içi — ''aynen' açılışı iki kez: kulların fışkırttığı pınar / adı verilen pınar", 'not': 'sûre içi eş.'},
 {'bag': '56:17 → 76:19', 'kural': "ölçüm xref — 'yetûfu 'aleyhim vildânun muxalledûn' korpusun iki ayeti: dört kelimede biten / benzetmeyle süren", 'not': 'xref.'},
 {'bag': '52:24 → 76:19', 'kural': "okuma — dolaşan gençler + inci: 'ke-enne … meknûn' / 'hasibtehum … mensûr'", 'not': 'kurgu eşi.'},
 {'bag': '27:44 → 76:19', 'kural': "okuma — lemma dizisi 'ra'â + hasiba' korpusun iki ayeti: cam köşk derin su sanılıyor / gençler inci sanılıyor", 'not': 'kalıp eşi.'},
 {'bag': '25:23 → 76:19', 'kural': "okuma — lemma 'mensûr' korpusun iki ayeti: savrulmuş toz / saçılmış inci", 'not': 'lemma eşi.'},
 {'bag': '76:15 → 76:19', 'kural': "sûre içi — kök طوف: 'yutâfu' (dolaştıran adsız) / 'yetûfu' (dolaşan gençler adlı)", 'not': 'sûre içi eş.'},
 {'bag': '76:13 → 76:20', 'kural': "sûre içi — kök رأي dört geçiş: iyiler görmez (güneş, soğuk) / 2MS görür (gençler, nimet, mülk)", 'not': 'sûre içi eş.'},
 # blok 21-31
 {'bag': '18:31 → 76:21', 'kural': "okuma — aynı giysi lemmaları ('siyâb', 'xudr', 'sundus', 'istebraq') + bilezik: altın / gümüş, sıra farklı", 'not': 'kalıp eşi.'},
 {'bag': '76:17 → 76:21', 'kural': "sûre içi — kök سقي: 'yusqavne' (sulayan adsız) / 'seqâhum rabbuhum' (sulayan adlı)", 'not': 'sûre içi eş.'},
 {'bag': '12:41 → 76:21', 'kural': "okuma — lemma dizisi 'seqâ + rabb' korpusun iki ayeti: sulanan efendi (insan) / sulayan Rab (1041 ailesi, sûre dışı)", 'not': 'lemma eşi.'},
 {'bag': '25:48 → 76:21', 'kural': "okuma — lemma 'tahûr' korpusun iki ayeti: gökten indirilen su / Rab'bin içirdiği içecek", 'not': 'lemma eşi.'},
 {'bag': '17:19 → 76:22', 'kural': "ölçüm xref — 'kâne + sa'y + meşkûr' (lemma 'meşkûr' korpusun iki ayeti): 3MP mümin / 2MP", 'not': 'xref.'},
 {'bag': '76:9 → 76:22', 'kural': "sûre içi — lemma 'cezâ'': insanlardan istenmeyen karşılık / 'lekum cezâ'en'; kök شكر 76:3, 76:9, 76:22", 'not': 'sûre içi eş.'},
 {'bag': '15:9 → 76:23', 'kural': "okuma — 'innâ nahnu nezzelnâ' korpusun iki ayeti: zikr / qur'ân", 'not': 'kalıp eşi.'},
 {'bag': '25:32 → 76:23', 'kural': "okuma — lemma dizisi 'nezzele + 'alâ + qur'ân': inkârcıların 'toptan' isteği, edilgen + 'tertîl' / etken 1P + 'tenzîl'", 'not': 'kalıp eşi.'},
 {'bag': '68:48 → 76:24', 'kural': "ölçüm xref — 'fasbir li-hukmi rabbike' korpusun iki ayeti: bir örnekten sakındırma / itaat yasağı", 'not': 'xref.'},
 {'bag': '52:48 → 76:24', 'kural': "ölçüm xref — 'li-hukmi rabbike': güvence + tesbih / itaat yasağı", 'not': 'xref.'},
 {'bag': '33:1 → 76:24', 'kural': "okuma — 've lâ tuti'' + 'kâne 'alîmen hakîmâ': 33:1'de aynı ayette / bu sûrede 76:24 ve 76:30", 'not': 'kalıp eşi.'},
 {'bag': '76:3 → 76:24', 'kural': "sûre içi — lemma 'kefûr': insanın iki hâlinden biri / boyun eğilmeyecek kişi", 'not': 'sûre içi eş.'},
 {'bag': '76:12 → 76:24', 'kural': "sûre içi — lemma 'sabera': iyilerin sabrı, karşılığı cennet / 2MS'ye sabır emri", 'not': 'sûre içi eş.'},
 {'bag': '73:8 → 76:25', 'kural': "ölçüm xref — 'vezkuri'sme rabbike' korpusun iki ayeti: O'na yönel / sabah akşam", 'not': 'xref.'},
 {'bag': '73:7 → 76:26', 'kural': "okuma — lemma 'tavîl' korpusun iki ayeti: gündüz uzun meşguliyet / uzun gece tesbihi", 'not': 'lemma eşi.'},
 {'bag': '75:20 → 76:27', 'kural': "okuma — lemma dizisi 'ahabbe + 'âcile' korpusun iki ayeti: 2MP 'tuhibbûne … tezerûne'l-âxira' (75:20-21) / 3MP 'yuhibbûne … yezerûne verâ'ehum yevmen saqîlâ' — ardışık sûre", 'not': 'kalıp eşi.'},
 {'bag': '73:5 → 76:27', 'kural': "okuma — lemma 'saqîl': ağır söz / ağır gün", 'not': 'lemma eşi.'},
 {'bag': '56:61 → 76:28', 'kural': "okuma — lemma dizisi 'beddele + misl' korpusun iki ayeti: 2MP 'emsâlekum' / 3MP 'emsâlehum', ikisinde 1P", 'not': 'lemma eşi.'},
 {'bag': '76:8 → 76:28', 'kural': "sûre içi — kök أسر: 'esîr' (esir) / 'esr' (bağ, yapı)", 'not': 'sûre içi eş.'},
 {'bag': '73:19 → 76:29', 'kural': "ölçüm esit2 TAM — iki sûrede özdeş ayet", 'not': 'esit2.'},
 {'bag': '25:57 → 76:29', 'kural': "ölçüm xref — 'men şâ'e + ittexaze ilâ rabbihî sebîlâ'", 'not': 'xref.'},
 {'bag': '74:54 → 76:29', 'kural': "okuma — 'tezkira' + 'fe-men şâ'e': iki ayete bölünmüş (74:54-55) / tek ayette", 'not': 'kalıp eşi.'},
 {'bag': '76:3 → 76:29', 'kural': "sûre içi — lemma 'sebîl': gösterilen yol / dileyenin tuttuğu yol", 'not': 'sûre içi eş.'},
 {'bag': '74:56 → 76:30', 'kural': "okuma — 'mâ … illâ en yeşâ'a'llâh': 'yezkurûne' / 'teşâ'ûne'", 'not': 'kalıp eşi.'},
 {'bag': '33:1 → 76:30', 'kural': "ölçüm xref — 'inna'llâhe kâne 'alîmen hakîmâ' (korpusta 4 ayet)", 'not': 'xref.'},
 {'bag': '76:28 → 76:30', 'kural': "sûre içi — lemma 'şâ'e' 76:28-31 dört ardışık ayet: 1P, dileyen, 2MP, Allah (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '76:24 → 76:30', 'kural': "sûre içi — kök حكم: Rabbin hükmü / 'hakîm'", 'not': 'sûre içi eş.'},
 {'bag': '42:8 → 76:31', 'kural': "ölçüm xref — 'yudxilu men yeşâ'u fî rahmetih' + zalimler: veli / yardımcı yok / hazırlanmış acı azap", 'not': 'xref.'},
 {'bag': '76:4 → 76:31', 'kural': "sûre içi — iki topluluk iki kez: kâfirler / iyiler (76:4-5), rahmete sokulan / zalimler (76:31) (aday 1039, okuma)", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_insan', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in INSAN]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_insan'] = INSAN
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_insan', len(INSAN), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_insan', len(BAGLAR['AS_insan']))
