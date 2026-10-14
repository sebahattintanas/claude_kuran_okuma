# -*- coding: utf-8 -*-
"""aday_ekle_44_duhan.py — sûre 44 (Duhân) adayları (AX_duhan) ve okuma bağları (AS_duhan).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

DUHAN = [
]

BAGLAR = {"AS_duhan": [
 {'bag': '40:1 · 41:1 · 42:1 · 43:1 → 44:1', 'kural': "esit2 TAM — 'Hâ Mîm' (ölçüm); okundu; 45:1, 46:1 henüz okunmadı", 'not': 'Hâ Mîm ailesi.'},
 {'bag': '43:89 → 44:1', 'kural': "okuma — ardışık sûre sınırı; aday 1040 alanında kayıt, test yok", 'not': 'sûre sınırı.'},
 {'bag': '43:2 → 44:2', 'kural': "esit2 TAM (ölçüm); okundu — aynı yemin, devamı 'ce'alnâhu qur'ânen arabiyyâ' / 'enzelnâhu fî leyletin mubârake'; aday 1040 alanında kayıt", 'not': 'apaçık Kitap.'},
 {'bag': '28:30 · 24:35 · 24:61 → 44:3', 'kural': "lemma 'mubârake' 4 ayet; okundu — yer / ağaç / selam / gece", 'not': 'mübarek.'},
 {'bag': '13:7 · 38:65 → 44:3', 'kural': "lemma 'munzir' 15 ayet; okundu — Peygamber 'munzir' / 1P 'munzirîn'; aday 1041 alanında kayıt, test yok", 'not': 'uyarıcı.'},
 {'bag': '17:106 → 44:4', 'kural': "okuma — 'faraqa': Kur'an'ı ayırdık / her hikmetli iş ayrılır; okundu", 'not': 'ayırma.'},
 {'bag': '43:4 · 43:84 → 44:4', 'kural': "okuma — 'hakîm': kitap / 'huve' / iş — aday 1041 alanına sınırda", 'not': 'hakîm.'},
 {'bag': '28:45 · 28:46 → 44:5 · 44:6', 'kural': "okuma — 'kunnâ mursilîn' → 'rahmeten min rabbik' aynı iki parça aynı sırayla; okundu", 'not': 'gönderenleriz; Rabbinden rahmet.'},
 {'bag': '26:24 → 44:7', 'kural': "esit2 YAKIN (0,9565, ölçüm); lemma dizisi 2 ayet; okundu — Mûsâ'nın Firavun'a cevabı / 'qâle'siz bedel", 'not': 'göklerin ve yerin Rabbi.'},
 {'bag': '26:26 · 37:126 → 44:8', 'kural': "lemma dizisi 'rabbukum ve rabbu âbâikumu'l-evvelîn' 3 ayet; okundu — Mûsâ / İlyâs; 44:7-8'de 26:24 ve 26:26 art arda (26:25 yok), KAPATILAMAZ", 'not': 'atalarınızın Rabbi.'},
 {'bag': '43:83 → 44:9', 'kural': "okuma — 'la'ibe': 'yehûdû ve yel'abû' / 'fî şekkin yel'abûn'; aday 1040 alanında kayıt, test yok", 'not': 'oynama.'},
 {'bag': '41:11 → 44:10', 'kural': "lemma 'duhân' korpusta 2 ayet; okundu — göğün yaratılıştaki duman hâli / göğün duman getireceği gün; KAPATILAMAZ", 'not': 'duman.'},
 {'bag': '11:93 → 44:10', 'kural': "lemma 'irtaqib' 4 ayet; okundu; sûre içi 44:59 henüz okunmadı", 'not': 'gözetle.'},
 {'bag': '44:10 → 44:11', 'kural': "okuma — 'yağşe' öznesi 'duhân'", 'not': 'duman bürür.'},
 {'bag': '43:49 · 43:50 → 44:12 · 44:15', 'kural': "lemma dizisi 'keşefe + an + azâb' 3 ayet; okundu — istek, vaat, kaldırma, dönüş sırası ardışık sûrelerde; aday 1040 alanında kayıt, test yok", 'not': 'azabı kaldır.'},
 {'bag': '10:98 → 44:12', 'kural': "lemma dizisi 'keşefe + an + azâb'; okundu — Yûnus kavmi iman edince kaldırıldı", 'not': 'azabın kaldırılması.'},
 {'bag': '37:36 → 44:14', 'kural': "okuma — elçiye 'şâirun mecnûn' / 'mu'allemun mecnûn'; okundu", 'not': 'deli dediler.'},
 {'bag': '26:130 · 28:19 → 44:16', 'kural': "lemma 'bataşa' 4 ayet; okundu — insan / 1P; aday 1041 alanında kayıt, test yok", 'not': 'yakalayış.'},
 {'bag': '43:41 · 32:22 → 44:16', 'kural': "lemma 'muntaqim' 3 ayet; okundu — 43:41 → 44:16 aday 1040 alanında kayıt", 'not': 'öç alanlarız.'},
 {'bag': '43:46 → 44:17', 'kural': "okuma — Firavun anlatısı ardışık sûrede yeniden açılıyor (43:46-56 / 44:17-); aday 1040 alanında kayıt", 'not': 'Firavun kavmi.'},
 {'bag': '26:107 · 26:125 · 26:143 · 26:162 · 26:178 → 44:18', 'kural': "lemma dizisi 'innî lekum rasûlun emîn' 6 ayet; okundu — Şuarâ'daki elçilerin nakaratı", 'not': 'güvenilir elçi.'},
 {'bag': '27:31 → 44:19', 'kural': "okuma — 'ellâ ta'lû aleyye' (Süleyman) / 'en lâ ta'lû ala'llâh'; okundu", 'not': 'büyüklenmeyin.'},
 {'bag': '14:10 · 27:21 → 44:19', 'kural': "lemma dizisi 'etâ + sultân + mubîn' 3 ayet; xref (ölçüm); okundu — istenen delil / getirilen delil", 'not': 'apaçık delil.'},
 {'bag': '40:27 → 44:20', 'kural': "lemma dizisi 'âze + rabb + rabb' 2 ayet; xref (ölçüm); okundu — 40:27 konuşan adlı Mûsâ, 44:20 adsız elçi", 'not': 'Rabbime sığındım.'},
 {'bag': '19:48 → 44:21', 'kural': "okuma — 'i'tezele': İbrâhîm 'e'tezilukum' / elçi 'fa'tezilûn'; okundu", 'not': 'uzak durun.'},
 {'bag': '43:88 → 44:22', 'kural': "okuma — 'hâulâi qavmun …' şikâyeti: 'lâ yu'minûn' / 'mucrimûn'; aday 1040 alanında kayıt, test yok", 'not': 'suçlu kavim.'},
 {'bag': '26:52 · 20:77 · 17:1 → 44:23', 'kural': "lemma dizisi 'esrâ + abd' 4 ayet; 'inne + muttebe'' 2 ayet (26:52); xref 17:1 (ölçüm); okundu — 26:52'de muhatap adlı Mûsâ", 'not': 'geceleyin yola çık.'},
 {'bag': '20:77 → 44:24', 'kural': "okuma — deniz: 'tarîqan fi'l-bahri yebesâ' / 'rehvâ'; okundu", 'not': 'deniz.'},
 {'bag': '11:37 · 11:43 · 23:27 → 44:24', 'kural': "lemma 'muğraq' 4 ayet; okundu — Nûh kavmi / Firavun ordusu", 'not': 'boğulacaklar.'},
 {'bag': '26:57 · 26:58 → 44:25 · 44:26', 'kural': "okuma — 'min cennâtin ve uyûn … ve maqâmin kerîm'; lemma dizisi 'maqâm + kerîm' 2 ayet; okundu — 'ahracnâhum' / 'terakû', 'kunûz' / 'zurû''", 'not': 'bahçeler, pınarlar.'},
 {'bag': '36:55 → 44:27', 'kural': "lemma 'fâkih' 3 ayet; okundu — cennet ehli / Firavun'un kavmi", 'not': 'keyif sürenler.'},
 {'bag': '26:59 → 44:28', 'kural': "okuma — 'kezâlike ve evrasnâhâ': 'benî isrâîl' / 'qavmen âharîn'; okundu; KAPATILAMAZ", 'not': 'miras.'},
 {'bag': '20:80 → 44:30', 'kural': "okuma — İsrâiloğullarının kurtarılması: 'enceynâ' / 'neccaynâ'; okundu", 'not': 'kurtardık.'},
 {'bag': '10:83 → 44:31', 'kural': "okuma — Firavun 'âlî' ve 'musrif'; okundu", 'not': 'büyüklenen, aşırı giden.'},
 {'bag': '44:19 → 44:31', 'kural': "okuma — علو [2/2] kapanıyor: 'lâ ta'lû' / 'âliyen'", 'not': 'büyüklenme.'},
 {'bag': '37:106 → 44:33', 'kural': "lemma dizisi 'belâ' + mubîn' 2 ayet; okundu", 'not': 'apaçık sınav.'},
 {'bag': '37:58 · 37:59 → 44:35', 'kural': "okuma — 'mevtetune'l-ûlâ … ve mâ nahnu bi-': cennet ehli 'mu'azzebîn' / inkârcılar 'munşerîn'; okundu", 'not': 'ilk ölüm.'},
 {'bag': '44:36 → 45:25', 'kural': "lemma dizisi 'etâ + âbâ' + in kâne + sâdiq' 2 ayet; xref (ölçüm); 45:25 henüz okunmadı — aday 1040 alanında kayıt", 'not': 'atalarımızı getirin.'},
 {'bag': '43:52 · 43:58 → 44:37', 'kural': "okuma — 'hayr … em' karşılaştırması ardışık sûrede; aday 1040 alanında kayıt", 'not': 'onlar mı hayırlı.'},
 {'bag': '21:16 · 38:27 → 44:38', 'kural': "esit2 BENZER 21:16 (0,9355, ölçüm); lemma dizisi 2 ayet; okundu — 'lâ'ibîn' / 'bâtılâ'", 'not': 'oyun için yaratmadık.'},
 {'bag': '44:9 → 44:38', 'kural': "okuma — لعب [2/2]: onlar oynuyor / oynayarak yaratmadık", 'not': 'oyun.'},
 {'bag': '15:85 → 44:39', 'kural': "okuma — 'mâ halaqnâ … illâ bi'l-haqq'; okundu; 44:38-39 = 21:16 + 15:85, KAPATILAMAZ", 'not': 'hak ile.'},
 {'bag': '10:55 · 28:13 → 44:39', 'kural': "lemma dizisi 'lâkinne ekserehum lâ ya'lemûn' 9 ayet; xref (ölçüm); okundu", 'not': 'çokları bilmez.'},
 {'bag': '37:21 → 44:40', 'kural': "okuma — 'yevmu'l-fasl'; okundu; 78:17 henüz okunmadı", 'not': 'ayrım günü.'},
 {'bag': '22:78 · 22:13 · 16:76 → 44:41', 'kural': "lemma 'mevlâ' 14 ayet; okundu — Allah / yalvarılan / sahip / insanlar; aday 1041 alanında kayıt, test yok", 'not': 'dost dosta.'},
 {'bag': '44:14 → 44:41', 'kural': "okuma — ولي [3/3] kapanıyor: 'tevellev' yüz çevirme / 'mevlâ' dost (gloss iki anlam, 1021)", 'not': 'velî.'},
 {'bag': '11:43 → 44:42', 'kural': "okuma — 'illâ men rahim' istisnâsı; okundu", 'not': 'rahmet ettikleri hariç.'},
 {'bag': '26:9 · 26:68 · 26:104 · 26:122 · 26:140 · 26:159 · 26:175 · 26:191 · 30:5 → 44:42', 'kural': "lemma dizisi '… azîz + rahîm' 10 ayet; okundu — Şuarâ nakaratı", 'not': 'Azîz, Rahîm.'},
 {'bag': '37:62 · 37:66 · 37:67 · 37:68 → 44:43 · 44:45 · 44:46 · 44:47', 'kural': "lemma dizisi 'şecere + zaqqûm' 2 ayet; okundu — zakkum, karınlar, hamîm, cahîm dörtlüsü", 'not': 'zakkum ağacı.'},
 {'bag': '18:29 → 44:45', 'kural': "lemma 'muhl' 3 ayet; okundu — yüzleri kavuran su / karınlarda kaynayan yiyecek", 'not': 'erimiş maden.'},
 {'bag': '37:55 → 44:47', 'kural': "okuma — 'sevâi'l-cahîm'; okundu", 'not': 'cehennemin ortası.'},
 {'bag': '22:19 → 44:48', 'kural': "xref (ölçüm); okundu — 'yusabbu min fevqi ruûsihimu'l-hamîm' edilgen çoğul / 'subbû fevqa ra'sihî' emir tekil", 'not': 'başın üstüne dökün.'},
 {'bag': '44:42 · 12:30 · 12:78 → 44:49', 'kural': "okuma — 'el-azîz': Allah / Mısır yöneticisi / azaptaki insan; aday 1041 alanında kayıt, test yok", 'not': 'azîz.'},
 {'bag': '43:61 · 15:63 → 44:50', 'kural': "okuma — 'imterâ': 'fe-lâ temterunna bihâ' / 'bi-mâ kânû fîhi yemterûn' / 'mâ kuntum bihî temterûn'; okundu", 'not': 'şüphe ettiğiniz.'},
 {'bag': '44:26 → 44:51', 'kural': "okuma — 'maqâm': 'maqâmin kerîm' (Firavun ve ordusunun bıraktığı) / 'maqâmin emîn' (takvâ sahiplerinin)", 'not': 'makam.'},
 {'bag': '15:45 · 26:147 · 44:25 → 44:52', 'kural': "esit2 TAM 26:147 (ölçüm); lemma dizisi 'fî + cennet + uyûn' 4 ayet; okundu — 44:25 bırakılan bahçeler ve pınarlar", 'not': 'bahçeler ve pınarlar.'},
 {'bag': '18:31 · 15:47 · 37:44 → 44:53', 'kural': "lemma dizisi 'sundus + istebraq' 2 ayet; 'mutaqâbil' 4 ayet; okundu", 'not': 'ipek, karşı karşıya.'},
 {'bag': '37:48 → 44:54', 'kural': "lemma 'în' 4 ayet; okundu; xref 52:20 henüz okunmadı", 'not': 'iri gözlü.'},
 {'bag': '38:51 · 15:46 → 44:55', 'kural': "lemma dizisi 'de'â + fî' 3 ayet; 'âmin' 16 ayet; okundu", 'not': 'meyve, güven.'},
 {'bag': '37:59 · 44:35 → 44:56', 'kural': "lemma dizisi 'illâ + mevtet' 3 ayet; okundu — cennet ehli / inkârcılar / anlatı", 'not': 'ilk ölüm.'},
 {'bag': '40:7 → 44:56', 'kural': "xref (ölçüm); lemma dizisi 'vekâ + azâb + cahîm' 2 ayet; okundu — dua / gerçekleşme", 'not': 'cehennem azabından koruma.'},
 {'bag': '37:58 · 37:59 · 37:60 → 44:56 · 44:57', 'kural': "okuma — 'mevtete'l-ûlâ' ardından 'huve'l-fevzu'l-azîm' aynı sıra; okundu", 'not': 'büyük kurtuluş.'},
 {'bag': '9:72 · 9:111 · 10:64 · 40:9 → 44:57', 'kural': "lemma dizisi 'zâ + (zamir) + fevz + azîm' 7 ayet; okundu; 57:12 henüz okunmadı", 'not': 'büyük kurtuluş.'},
 {'bag': '19:97 → 44:58', 'kural': "lemma dizisi 'innemâ + yessera + lisân' 2 ayet; okundu — aynı açılış, amaç: müjde-uyarı / öğüt", 'not': 'dilinle kolaylaştırdık.'},
 {'bag': '44:2 · 44:3 → 44:58', 'kural': "okuma — 1P + 'hu' ('enzelnâhu' / 'yessernâhu'), sûre başı ve sonu; zamir göndergesi adsız (KAPATILAMAZ)", 'not': 'onu.'},
 {'bag': '44:10 · 11:93 → 44:59', 'kural': "lemma 'irtaqib' 4 ayet; okundu — sûre içi aynı 2MS emir iki kez", 'not': 'bekle.'},
 {'bag': '43:89 → 44:59', 'kural': "okuma — iki sûre sonu: 'fe' + 2MS emir + 3MP hakkında cümle; aday 1040 alanında kayıt, test yok", 'not': 'sûre sonu.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_duhan', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in DUHAN]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_duhan'] = DUHAN
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_duhan', len(DUHAN), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_duhan', len(BAGLAR['AS_duhan']))
