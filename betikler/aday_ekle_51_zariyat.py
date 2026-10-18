# -*- coding: utf-8 -*-
"""aday_ekle_51_zariyat.py — sûre 51 (Zâriyât) adayları (AX_zariyat) ve okuma bağları (AS_zariyat).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

ZARIYAT = [
]

BAGLAR = {"AS_zariyat": [
 {'bag': '50:45 → 51:1', 'kural': "okuma — ardışık sûre sınırı; fâsıla د → ا; harf + yemin / yemin; aday 1040 alanında kayıt, test yok", 'not': 'sûre sınırı.'},
 {'bag': '50:32 · 50:45 → 51:5', 'kural': "okuma — 'mâ tû'adûn', 'vaîd' / 'innemâ tû'adûne le-sâdiq' (وعد); aday 1040 alanında kayıt", 'not': 'vaat.'},
 {'bag': '50:44 → 51:3', 'kural': "okuma — 'yesîr' / 'yusrâ' (يسر); aday 1040 alanında kayıt", 'not': 'kolaylık.'},
 {'bag': '50:6 → 51:7', 'kural': "okuma — gök 'mâ lehâ min furûc' / 'zâti'l-hubuk'; aday 1040 alanında kayıt", 'not': 'gök.'},
 {'bag': '51:1 → 51:4', 'kural': "okuma — dört mevsûfsuz ism-i fâil yemin nesnesi, 'fe-' ile sıralı; QASEM yalnız 51:4'te işaretli (ölçüm)", 'not': 'yemin dizisi.'},
 {'bag': '42:22 → 51:6', 'kural': "'vâqi'' lemma 6 ayet; okundu", 'not': 'gerçekleşecek.'},
 {'bag': '39:21 → 51:8', 'kural': "'muhtelif' lemma 10 ayet; okundu — renk / söz", 'not': 'çelişkili.'},
 {'bag': '51:5 → 51:8', 'kural': "okuma — 'le-sâdiq' / 'qavlin muhtelif'; karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'doğru / çelişkili.'},
 {'bag': '29:61 · 40:63 · 46:22 → 51:9', 'kural': "'efeke' lemma 15 ayet; okundu", 'not': 'çevrilme.'},
 {'bag': '10:66 → 51:10', 'kural': "kök خرص; okundu — 'in hum illâ yahrusûn' / 'el-harrâsûn'", 'not': 'tahminciler.'},
 {'bag': '23:54 · 23:63 → 51:11', 'kural': "'ğamra' lemma 3 ayet; okundu", 'not': 'gaflet dalgası.'},
 {'bag': '27:65 · 16:21 → 51:12', 'kural': "'eyyâne' lemma 6 ayet; okundu — 'eyyâne yub'asûn' / 'eyyâne yevmu'd-dîn'", 'not': 'ne zaman.'},
 {'bag': '51:6 → 51:12', 'kural': "okuma — 'le-vâqi'' / 'eyyâne'; دين sûre içi; karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'ceza günü.'},
 {'bag': '10:51 · 46:24 → 51:14', 'kural': "'ista'cele' lemma 19 ayet; okundu", 'not': 'acele.'},
 {'bag': '15:45 → 51:15', 'kural': "esit2 TAM 1,0000; lemma dizisi 2 ayet; xref (ölçüm); okundu — devamı 15:46 'udhulûhâ' / 51:16 'âhizîne'", 'not': 'bahçeler ve pınarlar.'},
 {'bag': '51:13 → 51:15', 'kural': "okuma — ateş / bahçeler; karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'iki yer.'},
 {'bag': '11:56 → 51:16', 'kural': "'âhiz' lemma 3 ayet; okundu — Rab / sakınanlar; aday 1041 alanında kayıt", 'not': 'alan.'},
 {'bag': '28:53 → 51:16', 'kural': "xref (ölçüm); okundu — 'kunnâ min qablihî muslimîn' / 'kânû qable zâlike muhsinîn'", 'not': 'önceden.'},
 {'bag': '51:12 → 51:19', 'kural': "okuma — سأل sûre içi: soranlar / isteyen", 'not': 'sormak, istemek.'},
 {'bag': '26:24 · 44:7 → 51:20', 'kural': "'mûqin' lemma 5 ayet; okundu", 'not': 'kesin inananlar.'},
 {'bag': '51:20 → 51:21 · 51:22', 'kural': "okuma — işaretlerin yeri: yer / nefis / gök; karşıt çift (aday 1039, okuma) dış / iç", 'not': 'yer, nefis, gök.'},
 {'bag': '46:35 · 50:32 → 51:22', 'kural': "lemma dizisi 'mâ tû'adûn' 24 ayet; okundu; 51:5 sûre içi", 'not': 'vaat edilen.'},
 {'bag': '51:1 · 51:7 → 51:23', 'kural': "okuma — sûrenin üç yemini; QASEM yalnız 51:4 ve 51:23'te işaretli (ölçüm)", 'not': 'yeminler.'},
 {'bag': '15:51 → 51:24', 'kural': "'dayf İbrâhîm'; 'dayf' lemma 5 ayet; okundu", 'not': 'İbrâhîm\'in konukları.'},
 {'bag': '15:52 · 11:69 → 51:25', 'kural': "xref (ölçüm); okundu — 'dehalû aleyhi fe-qâlû selâmâ' / 'qâlû selâmen qâle selâm'", 'not': 'selam.'},
 {'bag': '15:62 → 51:25', 'kural': "lemma dizisi 'qavmun munkerûn' 2 ayet; okundu — Lût / İbrâhîm", 'not': 'tanınmadık topluluk.'},
 {'bag': '11:69 → 51:26', 'kural': "okuma — 'câ'e bi-iclin hanîz' / 'câ'e bi-iclin semîn'", 'not': 'buzağı.'},
 {'bag': '37:91 → 51:26 · 51:27', 'kural': "'râğa' lemma 3 ayet ve 'qâle e-lâ te'kulûn' 2 ayet; okundu — putlara / konuklara", 'not': 'yöneldi, yemez misiniz.'},
 {'bag': '11:70 → 51:28', 'kural': "xref (ölçüm); lemma dizisi 'evcese minhum hîfeh' 2 ayet; okundu — devamı Lût kavmi / müjde", 'not': 'korku.'},
 {'bag': '15:53 → 51:28', 'kural': "xref (ölçüm); lemma dizisi 'beşşere bi-ğulâmin alîm' 2 ayet; okundu", 'not': 'müjde.'},
 {'bag': '11:71 · 11:72 → 51:29', 'kural': "okuma — 'fe-dahiket' / 'fe-sakket vechehâ'; 'ene acûz' / 'acûzun aqîm'", 'not': 'karısı.'},
 {'bag': '19:9 · 19:21 → 51:30', 'kural': "lemma dizisi 'qâle kezâlike qâle rabbuk' 3 ayet; okundu — Zekeriyyâ (2MS) / Meryem (2FS) / İbrâhîm'in karısı (2FS)", 'not': 'Rabbin böyle dedi.'},
 {'bag': '51:28 → 51:30', 'kural': "okuma — 'ğulâmin alîm' / 'el-hakîmu'l-alîm'; aday 1041 alanında kayıt", 'not': 'alîm.'},
 {'bag': '15:57 · 15:58 → 51:31 · 51:32', 'kural': "esit2 TAM 1,0000 iki ayet; xref (ölçüm); okundu — devamı 15:59 / 51:33 ayrılıyor", 'not': 'elçilerin işi.'},
 {'bag': '11:70 → 51:32', 'kural': "okuma — 'innâ ursilnâ ilâ qavmi Lût' / 'ilâ qavmin mucrimîn' (kavim adsız)", 'not': 'gönderildik.'},
 {'bag': '11:82 · 15:74 → 51:33', 'kural': "okuma — 'hicâraten min siccîl' / 'hicâraten min tîn'", 'not': 'taşlar.'},
 {'bag': '11:83 → 51:34', 'kural': "xref (ölçüm); okundu — 'musevvemeten inde rabbik' ortak; 'zâlimîn' / 'musrifîn'", 'not': 'işaretlenmiş.'},
 {'bag': '51:35 → 51:36', 'kural': "okuma — 'mu'minîn' / 'muslimîn' aynı topluluk için", 'not': 'iki sıfat.'},
 {'bag': '11:103 → 51:37', 'kural': "xref (ölçüm); okundu — 'âyet + hâfe + azâb'", 'not': 'işaret.'},
 {'bag': '51:20 · 51:21 → 51:38', 'kural': "okuma — 've fi'l-ard', 've fî enfusikum' → 've fî Mûsâ' (işaret yeri dizisi)", 'not': 'işaret yerleri.'},
 {'bag': '15:6 · 26:27 · 44:14 → 51:39', 'kural': "'mecnûn' emsali; okundu — peygambere yöneltilen nitelik", 'not': 'mecnûn.'},
 {'bag': '51:39 → 51:52', 'kural': "nakarat3 GEÇER (ölçüm) — 'qâle sâhirun ev mecnûn' sûre içi (51:52 henüz okunmadı)", 'not': 'tekrar.'},
 {'bag': '28:40 → 51:40', 'kural': "lemma dizisi 2 ayet; xref (ölçüm); okundu — devamı 'âqibetu'z-zâlimîn' / 've huve mulîm'", 'not': 'denize atma.'},
 {'bag': '51:29 → 51:41', 'kural': "okuma — 'aqîm' sûre içi: kısır kadın → kısır rüzgâr (عقم [2/2])", 'not': 'aynı sıfat.'},
 {'bag': '36:78 → 51:42', 'kural': "'ramîm' lemma 2; okundu — kemik / benzetme", 'not': 'ramîm.'},
 {'bag': '11:65 → 51:43', 'kural': "'temetta'û' — Sâlih'in sözü 'selâsete eyyâm' / edilgen 'qîle' + 'hattâ hîn' (okuma)", 'not': 'süre.'},
 {'bag': '41:17 · 11:67 → 51:44', 'kural': "Semûd'un sonu: 'sâ'iqa' / 'sayha' (okundu) — iki ad, KAPATILAMAZ", 'not': 'iki ad.'},
 {'bag': '18:43 → 51:45', 'kural': "'mâ kâne muntasırâ' tekil → 'mâ kânû muntasırîn' çoğul (lemma dizisi 2)", 'not': 'savunamama.'},
 {'bag': '27:12 · 43:54 → 51:46', 'kural': "'innehum kânû qavmen fâsiqîn' lemma dizisi 5; okunan ikisi Firavun ve kavmi, burada Nûh kavmi", 'not': 'fâsıklar.'},
 {'bag': '51:38 · 51:41 · 51:43 → 51:46', 'kural': "okuma — 've fî X iz' kavim dizisi: Mûsâ, Âd, Semûd → Nûh kavmi (atıf)", 'not': 'dizi.'},
 {'bag': '38:17 → 51:47', 'kural': "'eyd' lemma 2; okundu — 'ze'l-eyd' güç", 'not': 'güç.'},
 {'bag': '50:6 → 51:47 · 50:7 → 51:48', 'kural': "ardışık sûre: gök 'beneynâhâ' aynı fiil; yer 'medednâhâ' / 'feraşnâhâ' (aday 1040 alanı; okuma)", 'not': 'ardışık sûre.'},
 {'bag': '13:3 · 36:36 · 43:12 → 51:49', 'kural': "çift emsali; okundu — meyveler / 'el-ezvâce kullehâ' / 'kulli şey''", 'not': 'çift.'},
 {'bag': '29:50 → 51:50', 'kural': "'nezîrun mubîn' xref; okundu", 'not': 'uyarıcı.'},
 {'bag': '51:50 → 51:51', 'kural': "nakarat3 GEÇER (ölçüm) — 'innî lekum minhu nezîrun mubîn' sûre içi (51:51 henüz okunmadı)", 'not': 'tekrar.'},
 {'bag': '17:22 · 17:39 → 51:51', 'kural': "'lâ tec'al ma'a'llâhi ilâhen âhar' 2MS → 'lâ tec'alû' 2MP (lemma dizisi 3; okundu)", 'not': 'başka ilâh.'},
 {'bag': '51:50 → 51:51', 'kural': "nakarat3 GEÇER — 'innî lekum minhu nezîrun mubîn' iki ardışık ayette (okundu)", 'not': 'tekrar.'},
 {'bag': '51:39 → 51:52', 'kural': "'sâhirun ev mecnûn' Firavun'un sözü → öncekilerin her elçiye sözü (nakarat3 GEÇER)", 'not': 'genelleme.'},
 {'bag': '37:30 → 51:53', 'kural': "'bel … qavmen tâğîn' 2MP → 'bel hum qavmun tâğûn' 3MP (okundu)", 'not': 'azgın topluluk.'},
 {'bag': '51:39 · 51:40 → 51:54', 'kural': "okuma — ولي ve لوم: Firavun 'tevellâ', 'mulîm' / muhatap 'tevelle anhum', 'mâ ente bi-melûm' (zıt yön)", 'not': 'zıt yön.'},
 {'bag': '17:39 → 51:51 · 51:54', 'kural': "okuma — 17:39'da 'ilâhen âhar' + 'melûm' bir ayette; burada iki ayette", 'not': 'dağılım.'},
 {'bag': '50:45 → 51:54 · 51:55', 'kural': "ardışık sûre: 'mâ ente aleyhim bi-cebbâr fe-zekkir' / 'mâ ente bi-melûm … ve zekkir' (aday 1040 alanı; okuma)", 'not': 'sûre sonu dizilimi.'},
 {'bag': '51:22 → 51:57 → 51:58', 'kural': "okuma — رزق sûre içi: 'rizqukum' gökte → 'min rizq' istenmiyor → 'er-razzâq'", 'not': 'rızık.'},
 {'bag': '27:33 · 28:76 → 51:58', 'kural': "'ulû / uli'l-quvve' insanlar için → 'zu'l-quvve' lafız için (aday 1041 alanı; okundu)", 'not': 'kuvvet.'},
 {'bag': '21:37 → 51:59', 'kural': "'fe-lâ testa'cilûn' / 'fe-lâ yesta'cilûn' — 1S hazf (lemma dizisi 4; okundu)", 'not': 'acele.'},
 {'bag': '43:83 → 51:60', 'kural': "'yevmehumu'llezî yû'adûn' (lemma dizisi 3; okundu)", 'not': 'vaat günü.'},
 {'bag': '51:5 · 51:22 → 51:60', 'kural': "okuma — وعد sûre içi: 'tû'adûn' 2MP ×2 → 'yû'adûn' 3MP; sûre vaatle açılıp kapanıyor (KAPATILAMAZ)", 'not': 'açılış-kapanış.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_zariyat', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in ZARIYAT]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_zariyat'] = ZARIYAT
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_zariyat', len(ZARIYAT), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_zariyat', len(BAGLAR['AS_zariyat']))
