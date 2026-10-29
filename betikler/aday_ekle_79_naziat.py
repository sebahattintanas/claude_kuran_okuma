# -*- coding: utf-8 -*-
"""aday_ekle_79_naziat.py — sûre 79 (Nâzi'ât) adayları (AX_naziat) ve okuma bağları (AS_naziat).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

NAZIAT = [
]

BAGLAR = {"AS_naziat": [
 # blok 1-10
 {'bag': '78:40 → 79:1', 'kural': "okuma — ardışık sûre sınırı: kâfirin işaretli 1S dileğiyle kapanış / lafızsız yeminle açılış; fâsıla ا → ا (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '77:1 → 79:1', 'kural': "okuma — dişil çoğul ortaç + mastar / nekre ile beş yeminlik dizi (77:1-5 / 79:1-5); beşinci yeminde kalıp kırılıyor ('zikrâ' / 'emrâ'); sûreler ardışık değil", 'not': 'kurgu eşi.'},
 {'bag': '51:1 → 79:1', 'kural': "okuma — yemin dizisi açılışı: 51:1-4 dört / 37:1-3 üç / 79:1-5 beş", 'not': 'kurgu eşi.'},
 {'bag': '73:7 → 79:3', 'kural': "okuma — lemma 'sebh' korpusun iki ayeti: gündüzdeki uzun meşguliyet / yemin edilenlerin yüzüşü", 'not': 'lemma eşi.'},
 {'bag': '73:14 → 79:6', 'kural': "okuma — 'yevme tercufu': yer ve dağlar (adlı) / 'er-râcife' (adsız, aynı kökten fail)", 'not': 'kalıp eşi.'},
 {'bag': '79:6 → 79:7', 'kural': "sûre içi — 'er-râcife' / 'er-râdife': aynı vezin, ardışık iki olay, ikisi adsız", 'not': 'sûre içi eş.'},
 {'bag': '70:44 → 79:9', 'kural': "okuma — 'ebsâr' + 'xâşi'': ters sıra, hâl, 3MP (68:43, 70:44) / haber, 3FS", 'not': 'kalıp eşi.'},
 {'bag': '11:76 → 79:10', 'kural': "okuma — lemma 'merdûd' korpusun iki ayeti: geri çevrilmez azap / geri döndürülenler", 'not': 'lemma eşi.'},
 # blok 11-20
 {'bag': '17:49 → 79:11', 'kural': "okuma — 'e-izâ kunnâ 'izâmen' korpusun üç ayeti (17:49, 17:98): 'rufât' + diriltilme sorusu / 'nexira', soru önceki ayette", 'not': 'kalıp eşi.'},
 {'bag': '37:16 → 79:11', 'kural': "okuma — itiraz içinde kemik: toprak + kemik (37:16, 56:47, L1) / çürümüş kemik (L1)", 'not': 'kurgu eşi.'},
 {'bag': '37:19 → 79:13', 'kural': "okuma — 'fe-innemâ hiye zecratun vâhida' korpusun iki ayeti; 'fe-izâ hum' aynı ayette (37:19) / sonraki ayette (79:14); ölçüm esit2 yazmıyor", 'not': 'kalıp eşi.'},
 {'bag': '36:53 → 79:14', 'kural': "okuma — 'tek' + 'fe-izâ hum': 'sayha' / 'zecra'", 'not': 'kurgu eşi.'},
 {'bag': '20:9 → 79:15', 'kural': "ölçüm esit2 TAM — 'hel etâke hadîsu mûsâ' ('ve' önek farkı)", 'not': 'esit2.'},
 {'bag': '20:12 → 79:16', 'kural': "ölçüm xref — lemma dizisi 'vâd + muqaddes + tuvâ' korpusun iki ayeti: Rabbin 1S sözü / anlatıcı sesi", 'not': 'xref.'},
 {'bag': '28:30 → 79:16', 'kural': "okuma — vadi + seslenme: edilgen 'nûdiye' / etken, fail 'rabbuhû'", 'not': 'kurgu eşi.'},
 {'bag': '20:24 → 79:17', 'kural': "ölçüm esit2 TAM — 'izheb ilâ fir'avne innehû tağâ' (20:43 YAKIN, ikil)", 'not': 'esit2.'},
 {'bag': '78:22 → 79:17', 'kural': "okuma — kök طغي ardışık sûrelerde: 'et-tâğîn' / Fir'avn 'tağâ' (aday 1040 ailesi, kayıt)", 'not': 'kök eşi.'},
 {'bag': '20:44 → 79:19', 'kural': "okuma — Fir'avn'a söylenecek söz + 'xaşye': ikil, 'le'alle', 3MS / tekil, iç alıntı, 2MS", 'not': 'kurgu eşi.'},
 {'bag': '20:23 → 79:20', 'kural': "okuma — lemma dizisi 'âye + kubrâ' korpusun iki ayeti: 1P 'âyâtinâ' çoğul / tekil, tarifli", 'not': 'lemma eşi.'},
 {'bag': '79:17 → 79:19', 'kural': "sûre içi — 'tağâ' / 'taxşâ' (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 # blok 21-30
 {'bag': '79:5 → 79:22', 'kural': "sûre içi — kök دبر iki anlam: 'el-mudebbirât' (düzenleyenler) / 'edbera' (sırt döndü)", 'not': 'sûre içi eş.'},
 {'bag': '79:16 → 79:23', 'kural': "sûre içi — lemma 'nâdâ': Rab seslenir / Fir'avn seslenir (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '79:19 → 79:24', 'kural': "sûre içi — kök ربب: Rab (79:16, 19) / Fir'avn'ın 'ene rabbukum' iddiası (aday 1041, kayıt; ölçüm iddiayı Rab sayıyor, 924)", 'not': 'sûre içi eş.'},
 {'bag': '24:44 → 79:26', 'kural': "okuma — 'inne fî zâlike le-'ibra': 'li-ulî'l-ebsâr' / 'li-men yaxşâ'", 'not': 'kalıp eşi.'},
 {'bag': '79:19 → 79:26', 'kural': "sûre içi — kök خشي: Fir'avn'a umulan / ibret alan", 'not': 'sûre içi eş.'},
 {'bag': '37:11 → 79:27', 'kural': "okuma — lemma dizisi 'eşedd + xalq' korpusun iki ayeti: 3MP, 'men xalaqnâ' / 2MP, 'es-semâ''", 'not': 'lemma eşi.'},
 {'bag': '40:57 → 79:27', 'kural': "okuma — insan / gök yaratılışı karşılaştırması: haber, 'ekber' / soru, 'eşedd' (ikisi L1)", 'not': 'kurgu eşi.'},
 {'bag': '78:12 → 79:27', 'kural': "okuma — ardışık sûrede kök بني + 'şedîd': 1P, sayılan adsız / 3MS, gök adlı (aday 1040 ailesi, kayıt)", 'not': 'kök eşi.'},
 {'bag': '55:7 → 79:28', 'kural': "okuma — 'refe'a' + gök (13:2, 55:7): direksiz / mîzân / 'semk' + 'sevvâ' (L1)", 'not': 'kalıp eşi.'},
 {'bag': '78:10 → 79:29', 'kural': "okuma — ardışık sûrede gece nesne: 1P, örtü / 3MS, karartma, göğe iyelik (aday 1040 ailesi, kayıt)", 'not': 'kök eşi.'},
 {'bag': '41:11 → 79:30', 'kural': "okuma — gök ve yer sırayla: 'thumme' / 'ba'de zâlike', gök önce (ikisi L1)", 'not': 'kurgu eşi.'},
 {'bag': '78:6 → 79:30', 'kural': "okuma — ardışık sûrede yer: 1P + işlev ('mihâd') / 3MS + süreç ('dehâ') (aday 1040 ailesi, kayıt)", 'not': 'kök eşi.'},
 # blok 31-40
 {'bag': '79:29 → 79:31', 'kural': "sûre içi — kök خرج: göğün kuşluğunu / yerin suyunu çıkardı", 'not': 'sûre içi eş.'},
 {'bag': '77:27 → 79:31', 'kural': "okuma — ardışık sûrede dağ + su: 1P, içirme / 3MS, yerden çıkarma (aday 1040 ailesi, kayıt)", 'not': 'kurgu eşi.'},
 {'bag': '78:14 → 79:31', 'kural': "okuma — ardışık sûrede su: 1P, indirme / 3MS, yerden çıkarma (aday 1040 ailesi, kayıt)", 'not': 'kök eşi.'},
 {'bag': '78:7 → 79:32', 'kural': "okuma — ardışık sûrede dağlar meful öne: fiilsiz, 'evtâd' / 'ersâ' (aday 1040 ailesi, kayıt)", 'not': 'kalıp eşi.'},
 {'bag': '16:15 → 79:32', 'kural': "okuma — kök رسو (16:15, 21:31): gerekçe 'en temîde' / gerekçesiz", 'not': 'kök eşi.'},
 {'bag': '78:11 → 79:33', 'kural': "okuma — işlev adı ('me'âş' / 'metâ''), ikisi L1", 'not': 'kurgu eşi.'},
 {'bag': '79:20 → 79:34', 'kural': "sûre içi — 'kubrâ': en büyük ayet / en büyük felâket (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '79:22 → 79:35', 'kural': "sûre içi — kök سعي: Fir'avn koşturdu / insan çabaladı", 'not': 'sûre içi eş.'},
 {'bag': '26:91 → 79:36', 'kural': "okuma — lemma dizisi 'burrizet + cahîm' korpusun iki ayeti: 'li'l-ğâvîn' / 'li-men yerâ'", 'not': 'lemma eşi.'},
 {'bag': '79:17 → 79:37', 'kural': "sûre içi — kök طغي: Fir'avn'ın fiili / genel şart", 'not': 'sûre içi eş.'},
 {'bag': '78:22 → 79:39', 'kural': "okuma — ardışık sûrede azgınlar + varış yeri: 'me'âb' / 'me'vâ' (aday 1040 ailesi, kayıt)", 'not': 'kurgu eşi.'},
 {'bag': '79:36 → 79:39', 'kural': "sûre içi — lemma 'cahîm' iki geçişin ikisi", 'not': 'sûre içi eş.'},
 {'bag': '55:46 → 79:40', 'kural': "okuma — harekesiz 'xâfe maqâme rabbih' korpusun iki ayeti: cevap aynı ayette / sonraki ayette (henüz okunmadı)", 'not': 'kalıp eşi.'},
 {'bag': '79:37 → 79:40', 'kural': "sûre içi — 'emmâ' tafsîlinin iki kolu: azan / korkan (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 # blok 41-46
 {'bag': '79:39 → 79:41', 'kural': "sûre içi — 'fe-inne … hiye'l-me'vâ': cahîm / cennet (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '79:32 → 79:42', 'kural': "sûre içi — kök رسو: dağları sabitledi / saatin duracağı an", 'not': 'sûre içi eş.'},
 {'bag': '11:41 → 79:42', 'kural': "okuma — lemma 'mursâ': gemi ('qâle' içinde) / saat", 'not': 'lemma eşi.'},
 {'bag': '79:35 → 79:43', 'kural': "sûre içi — kök ذكر: insan hatırlar / saatin anılması", 'not': 'sûre içi eş.'},
 {'bag': '53:42 → 79:44', 'kural': "okuma — lemma dizisi 'rabb + muntehâ' korpusun iki ayeti: mutlak 'el-muntehâ' / 'muntehâhâ' (saatin)", 'not': 'lemma eşi.'},
 {'bag': '79:40 → 79:44', 'kural': "sûre içi — kök نهي: nefsi alıkoydu / varış noktası", 'not': 'sûre içi eş.'},
 {'bag': '13:7 → 79:45', 'kural': "okuma — harekesiz 'innemâ ente munzir' korpusun iki ayeti: ayet istemine / saat sorusuna karşılık", 'not': 'kalıp eşi.'},
 {'bag': '79:26 → 79:45', 'kural': "sûre içi — kök خشي + 'men': 'li-men yaxşâ' / 'men yaxşâhâ'", 'not': 'sûre içi eş.'},
 {'bag': '46:35 → 79:46', 'kural': "okuma — 'ke-ennehum yevme yeravne … lem yelbethû illâ': 'sâ'aten min nehâr' / ''aşiyyeten ev duhâhâ'", 'not': 'kalıp eşi.'},
 {'bag': '10:45 → 79:46', 'kural': "okuma — harekesiz 'lem yelbethû illâ' (10:45, 46:35, 79:46): kalınan süre 'sâ'a' / akşam ya da kuşluk", 'not': 'kalıp eşi.'},
 {'bag': '79:29 → 79:46', 'kural': "sûre içi — lemma 'duhâ': göğün kuşluğu / kalınan süre", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_naziat', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in NAZIAT]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_naziat'] = NAZIAT
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_naziat', len(NAZIAT), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_naziat', len(BAGLAR['AS_naziat']))
