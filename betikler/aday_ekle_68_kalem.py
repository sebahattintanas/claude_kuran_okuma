# -*- coding: utf-8 -*-
"""aday_ekle_68_kalem.py — sûre 68 (Kalem) adayları (AX_kalem) ve okuma bağları (AS_kalem).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

KALEM = [
]

BAGLAR = {"AS_kalem": [
 # blok 1-10
 {'bag': '67:30 → 68:1', 'kural': "okuma — ardışık sûre sınırı; cevapsız soruyla kapanış / harf ve yeminle açılış; 67:30 fâsıla ن, 68:1 'Nûn' (aday 1040, kayıt)", 'not': 'sûre sınırı.'},
 {'bag': '31:27 → 68:1', 'kural': "okuma — lemma 'qalem': ağaçların kalem olması varsayımı / yemin nesnesi", 'not': 'lemma eşi.'},
 {'bag': '52:29 → 68:2', 'kural': "lemma dizisi — 'mâ ente bi-ni'meti rabbike bi-…': 'kâhin ve lâ mecnûn' / 'mecnûn'", 'not': 'kalıp eşi.'},
 {'bag': '41:8 → 68:3', 'kural': "lemma dizisi — 'ecrun ğayru memnûn' (4 ayet): 3MP / 2MS", 'not': 'kalıp eşi.'},
 {'bag': '26:137 → 68:4', 'kural': "okuma — lemma 'huluq' (2 ayet): öncekilerin âdeti / 2MS'nin ahlâkı", 'not': 'lemma eşi.'},
 {'bag': '68:5 → 68:6', 'kural': "sûre içi — 'tubsiru ve yubsirûn' → 'bi-eyyikumu'l-meftûn' (2MS + 3MP → 2MP)", 'not': 'sûre içi eş.'},
 {'bag': '16:125 → 68:7', 'kural': "xref (ölçüm) — 'inne rabbeke huve a'lemu bi-men dalle an sebîlihî ve huve a'lemu bi'l-muhtedîn'", 'not': 'xref eşi.'},
 {'bag': '53:30 → 68:7', 'kural': "lemma dizisi — 'a'lemu bi-men dalle an sebîlih': 'bi-meni'htedâ' (fiil) / 'bi'l-muhtedîn' (isim)", 'not': 'kalıp eşi.'},
 {'bag': '25:52 → 68:8', 'kural': "lemma dizisi — 'fe-lâ tuti'' (12 ayet 'lâ + etâ'a'): kâfirler / yalanlayanlar", 'not': 'kalıp eşi.'},
 {'bag': '33:48 → 68:8', 'kural': "lemma dizisi — 'lâ tuti'': kâfirler ve münafıklar / yalanlayanlar", 'not': 'kalıp eşi.'},
 {'bag': '68:8 → 68:10', 'kural': "sûre içi — 'lâ tuti'' ×2: yalanlayanlar / 'kulle hallâfin mehîn'", 'not': 'sûre içi tekrar.'},
 {'bag': '68:5 → 68:9', 'kural': "sûre içi — 2MS / 3MP aynı fiil eşlemesi: 'tubsiru / yubsirûn', 'tudhinu / yudhinûn'", 'not': 'sûre içi eş.'},
 # blok 11-20
 {'bag': '68:10 → 68:13', 'kural': "sûre içi — dokuz sıfatlık dizi (68:10-13): hallâf … zenîm; 'fe''âl' kalıbı 68:10-12", 'not': 'sûre içi dizi.'},
 {'bag': '50:25 → 68:12', 'kural': "xref (ölçüm) — 'mennâ'in li'l-hayri mu'tedin': 'murîb' / 'esîm'", 'not': 'xref eşi.'},
 {'bag': '31:7 → 68:15', 'kural': "lemma dizisi — 'izâ tutlâ aleyhi âyâtunâ' (12 ayet): sırt çevirme / 'esâtîr' deme", 'not': 'kalıp eşi.'},
 {'bag': '25:5 → 68:15', 'kural': "lemma dizisi — 'qâle + esâtîru'l-evvelîn' (4 ayet): 3MP / 3MS", 'not': 'kalıp eşi.'},
 {'bag': '68:1 → 68:15', 'kural': "sûre içi — kök سطر: 'yesturûn' (yemin nesnesi) / 'esâtîr' (inkârcının sözü)", 'not': 'kök iki yer.'},
 {'bag': '68:6 → 68:15', 'kural': "sûre içi — kök أيي: 'eyyikum' (hangisi) / 'âyâtunâ' (iki anlam)", 'not': 'kök iki anlam.'},
 {'bag': '67:2 → 68:17', 'kural': "okuma — lemma 'belâ': 'li-yebluvekum' / 'belevnâhum' (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '36:55 → 68:17', 'kural': "lemma dizisi — 'ashâbu'l-cenne' (13 ayet): âhiret cenneti / yeryüzündeki bahçe", 'not': 'kalıp eşi.'},
 {'bag': '15:66 → 68:17', 'kural': "okuma — lemma 'musbih': kesilen kökler sabahleyin / devşirme sabahleyin", 'not': 'lemma eşi.'},
 {'bag': '68:2 → 68:17', 'kural': "sûre içi — kök جنن: 'mecnûn' / 'el-cenne' (iki anlam)", 'not': 'kök iki anlam.'},
 {'bag': '68:10 → 68:17', 'kural': "sûre içi — yemin: 'hallâf' (ölçüm QASEM yanlış) / 'aqsamû' (gerçek yemin fiili)", 'not': 'sûre içi eş.'},
 {'bag': '68:17 → 68:20', 'kural': "sûre içi — kök صرم: 'le-yasrimunnehâ' / 'ke's-sarîm'; kök صبح: 'musbihîn' / 'asbahat'", 'not': 'sûre içi eş.'},
 {'bag': '68:7 → 68:19', 'kural': "sûre içi — Rab 2MS izâfetle: 'rabbeke' / 'min rabbike' (kıssa içinde)", 'not': 'sûre içi eş.'},
 # blok 21-30
 {'bag': '68:17 → 68:21', 'kural': "sûre içi — 'musbihîn' ×2: yemin / yerine getirme; kök صبح üç geçiş (68:17, 20, 21)", 'not': 'sûre içi eş.'},
 {'bag': '68:20 → 68:22', 'kural': "sûre içi — kök صرم üç geçiş: 'le-yasrimunnehâ', 'ke's-sarîm', 'sârimîn'", 'not': 'sûre içi eş.'},
 {'bag': '20:103 → 68:23', 'kural': "okuma — lemma 'yetehâfetu' (2 ayet): fısıldaşma", 'not': 'lemma eşi.'},
 {'bag': '68:22 → 68:25', 'kural': "sûre içi — lemma 'ğadâ': emir 'iğdû' / fiil 'ğadev'", 'not': 'sûre içi eş.'},
 {'bag': '67:1 → 68:25', 'kural': "okuma — kök قدر: 'qadîr' (İLÂHÎ) / 'qâdirîn' (bahçe sahipleri) (aday 1041 alanına kök düzeyinde sınırda, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '67:27 → 68:26', 'kural': "okuma — 'fe-lemmâ ra'ev-': tehdidi yakından görme / bahçeyi görme (aday 1040, kayıt)", 'not': 'ardışık sûre bağı.'},
 {'bag': '68:7 → 68:26', 'kural': "sûre içi — kök ضلل: 'dalle an sebîlih' / 'le-dâllûn'", 'not': 'sûre içi eş.'},
 {'bag': '56:67 → 68:27', 'kural': "esit2 (TAM) — 'bel nahnu mahrûmûn'", 'not': 'tekrar ayet.'},
 {'bag': '68:28 → 68:29', 'kural': "sûre içi — kök سبح: 'levlâ tusebbihûn' / 'subhâne rabbinâ'", 'not': 'sûre içi eş.'},
 {'bag': '17:108 → 68:29', 'kural': "xref (ölçüm) — 'subhâne rabbinâ'", 'not': 'xref eşi.'},
 {'bag': '21:14 → 68:29', 'kural': "lemma dizisi — 'innâ kunnâ zâlimîn' (4 ayet): 'yâ veylenâ' / 'subhâne rabbinâ'", 'not': 'kalıp eşi.'},
 {'bag': '52:25 → 68:30', 'kural': "esit2 (BENZER) — 'aqbele ba'duhum alâ ba'din': 'yetesâ'elûn' / 'yetelâvemûn'", 'not': 'benzer ayet.'}, # blok 31-41
 {'bag': '21:14 → 68:31', 'kural': "esit2 (BENZER) — 'qâlû yâ veylenâ innâ kunnâ': 'zâlimîn' / 'tâğîn'", 'not': 'benzer ayet.'},
 {'bag': '68:29 → 68:31', 'kural': "sûre içi — 'innâ kunnâ zâlimîn' / 'innâ kunnâ tâğîn': iki itiraf", 'not': 'sûre içi eş.'},
 {'bag': '66:5 → 68:32', 'kural': "okuma — lemma 'yubdilu' (3 ayet): 'asâ rabbuhû … en yubdilehû … hayran' / 'asâ rabbunâ en yubdilenâ hayran'", 'not': 'lemma eşi.'},
 {'bag': '18:81 → 68:32', 'kural': "okuma — lemma 'yubdilu' (3 ayet): 'en yubdilehumâ rabbuhumâ hayran minhu'", 'not': 'lemma eşi.'},
 {'bag': '39:26 → 68:33', 'kural': "lemma dizisi (2 ayet) / xref — 've le-azâbu'l-âhirati ekber lev kânû ya'lemûn'", 'not': 'kalıp eşi.'},
 {'bag': '16:41 → 68:33', 'kural': "lemma dizisi (3 ayet) / xref — 'ekber lev kânû ya'lemûn': 'ecr' / 'azâb'", 'not': 'kalıp eşi.'},
 {'bag': '52:17 → 68:34', 'kural': "lemma dizisi 'cenne + na'îm' (11 ayet) — muttakîler için cennetler ve nimet", 'not': 'kalıp eşi.'},
 {'bag': '68:17 → 68:34', 'kural': "sûre içi — lemma 'cenne': bahçe sahiplerinin bahçesi / Rablerinin katında nimet cennetleri", 'not': 'sûre içi eş.'},
 {'bag': '68:33 → 68:34', 'kural': "okuma — karşıt çift (aday 1039): âhiret azabı / nimet cennetleri", 'not': 'karşıt çift.'},
 {'bag': '38:28 → 68:35', 'kural': "okuma — 'nec'alu X ke-Y' soru kurgusu: 'muttaqîn / fuccâr' / 'muslimîn / mucrimîn'", 'not': 'kurgu eşi.'},
 {'bag': '37:154 → 68:36', 'kural': "esit2 (TAM) — 'mâ lekum keyfe tahkumûn'", 'not': 'tekrar ayet.'},
 {'bag': '34:44 → 68:37', 'kural': "okuma — lemma 'deresa': okudukları kitap verilmedi / okudukları kitap soruluyor", 'not': 'lemma eşi.'},
 {'bag': '56:20 → 68:38', 'kural': "okuma — lemma 'yetehayyaru' (2 ayet): seçtikleri meyve / seçtikleri", 'not': 'lemma eşi.'},
 {'bag': '68:38 → 68:39', 'kural': "sûre içi — 'inne lekum … lemâ': 'tehayyarûn' / 'tahkumûn'", 'not': 'sûre içi eş.'},
 {'bag': '68:36 → 68:39', 'kural': "sûre içi — lemma 'hakeme': 'keyfe tahkumûn' / 'lemâ tahkumûn'", 'not': 'sûre içi eş.'},
 {'bag': '68:6 → 68:40', 'kural': "sûre içi — kök أيي: 'eyyikum' / 'eyyuhum' (soru)", 'not': 'sûre içi eş.'},
 {'bag': '52:34 → 68:41', 'kural': "harekesiz kalıp 'fe'l-ye'tû' (2 ayet) — 'in kânû sâdiqîn': 'hadîs' / 'şurakâ'", 'not': 'kalıp eşi.'}, # blok 42-52
 {'bag': '68:42 → 68:43', 'kural': "sûre içi — 'yud'avne ile's-sucûd' (nakarat3, süzgeç geçmez): o gün / önceden", 'not': 'sûre içi eş.'},
 {'bag': '10:27 → 68:43', 'kural': "lemma dizisi 'yerhaqu + zille' (3 ayet) — 'terhaquhum zilletun'", 'not': 'kalıp eşi.'},
 {'bag': '68:35 → 68:43', 'kural': "sûre içi — kök سلم: 'el-muslimîn' / 'sâlimûn'", 'not': 'sûre içi eş.'},
 {'bag': '68:8 → 68:44', 'kural': "sûre içi — kök كذب: 'el-mukezzibîn' / 'yukezzibu'", 'not': 'sûre içi eş.'},
 {'bag': '51:58 → 68:45', 'kural': "okuma — lemma 'metîn' (3 ayet): 'zu'l-quvveti'l-metîn' (İLÂHÎ) / 'keydî metîn' (aday 1041 sınır vakası, kayıt)", 'not': 'lemma eşi.'},
 {'bag': '52:40 → 68:46', 'kural': "esit2 (TAM) — 'em tes'eluhum ecran fe-hum min mağramin muskalûn'", 'not': 'tekrar ayet.'},
 {'bag': '52:41 → 68:47', 'kural': "esit2 (TAM) — 'em indehumu'l-ğaybu fe-hum yektubûn'", 'not': 'tekrar ayet.'},
 {'bag': '68:40 → 68:46', 'kural': "sûre içi — kök سأل: 'sel-hum' / 'tes'eluhum'", 'not': 'sûre içi eş.'},
 {'bag': '68:3 → 68:46', 'kural': "sûre içi — kök أجر: 2MS'ye verilecek ücret / 2MS'nin istemediği ücret", 'not': 'sûre içi eş.'},
 {'bag': '52:48 → 68:48', 'kural': "lemma dizisi 'sabera + hukm + rabb' (3 ayet) / xref — 'vasbir li-hukmi rabbike'", 'not': 'kalıp eşi.'},
 {'bag': '37:142 → 68:48', 'kural': "okuma — lemma 'hût': 've huve mulîm' / 've huve mekzûm'", 'not': 'lemma eşi.'},
 {'bag': '68:17 → 68:48', 'kural': "sûre içi — kök صحب: 'ashâbe'l-cenne' / 'sâhibi'l-hût'", 'not': 'sûre içi eş.'},
 {'bag': '68:36 → 68:48', 'kural': "sûre içi — kök حكم: 'tahkumûn' / 'li-hukmi rabbike'", 'not': 'sûre içi eş.'},
 {'bag': '37:145 → 68:49', 'kural': "lemma dizisi 'nebeze + arâ'' (2 ayet) — 'fe-nebeznâhu … saqîm' / 'le-nubize … mezmûm'", 'not': 'kalıp eşi.'},
 {'bag': '68:2 → 68:49', 'kural': "sûre içi — lemma 'ni'me': 'bi-ni'meti rabbike' / 'ni'metun min rabbihî'", 'not': 'sûre içi eş.'},
 {'bag': '68:49 → 68:50', 'kural': "okuma — karşıt çift (aday 1039): 'mezmûm' / 'mine's-sâlihîn'", 'not': 'karşıt çift.'},
 {'bag': '68:2 → 68:51', 'kural': "sûre içi — lemma 'mecnûn': nefy ile ilk geçiş / iddia ile son geçiş", 'not': 'sûre içi eş.'},
 {'bag': '15:6 → 68:51', 'kural': "okuma — 'zikr' ve 'mecnûn' aynı ayette", 'not': 'kurgu eşi.'},
 {'bag': '38:87 → 68:52', 'kural': "esit2 (BENZER) — 'illâ zikrun li'l-âlemîn': 'in huve' / 'mâ huve'", 'not': 'benzer ayet.'},
 {'bag': '68:51 → 68:52', 'kural': "sûre içi — lemma 'zikr' / karşıt çift (aday 1039): 'le-mecnûn' / 'zikrun li'l-âlemîn'", 'not': 'sûre içi eş.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_kalem', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in KALEM]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_kalem'] = KALEM
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_kalem', len(KALEM), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_kalem', len(BAGLAR['AS_kalem']))
