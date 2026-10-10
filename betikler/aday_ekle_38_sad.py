# -*- coding: utf-8 -*-
"""aday_ekle_38_sad.py — sûre 38 (Sâd) adayları (AW_sad) ve okuma bağları (AR_sad).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1039'dan); betik sıranın kopmadığını doğrular.
"""
import json

SAD = [
]

BAGLAR = {"AR_sad": [
 {'bag': '37:1 → 38:1', 'kural': 'okuma — iki sûre de yeminle açılıyor (adsız topluluk / adlı kitap); KAPATILAMAZ', 'not': "ve's-sâffât / ve'l-qur'ân."},
 {'bag': '37:180 → 38:2 · 38:9', 'kural': 'kök ipliği عزز — izzet Rab\'bin (37:180) / inkârcıların (38:2) / el-azîz (38:9); okumada görüldü, KAPATILAMAZ', 'not': 'izzet.'},
 {'bag': '10:2 → 38:4', 'kural': "xref — 'qâle'l-kâfirûne … sâhir'; iki ucu okundu; 50:2 henüz okunmadı", 'not': 'büyücü.'},
 {'bag': '7:138 → 38:5', 'kural': 'xref — ilâh/âlihe çifti ters yönde (put isteme / teke indirmeye şaşma); iki ucu okundu', 'not': 'ilâh.'},
 {'bag': '37:4 → 38:5', 'kural': "okuma — 'inne ilâhekum le-vâhid' iddiası / 'e-ce'ale'l-âliheta ilâhen vâhidâ' itirazı; KAPATILAMAZ", 'not': 'tek ilâh.'},
 {'bag': '38:5 ↔ 38:6', 'kural': "nakarat3 ('inne hâzâ le-şey'un', süzgeç GEÇMEZ) — ucâb / yurâd; iki ucu okundu", 'not': 'şey.'},
 {'bag': '17:100 → 38:9', 'kural': "xref ('hazâinu rahmeti rabb') — iki ucu okundu; rabbî (1S) / rabbike (2MS)", 'not': 'rahmet hazineleri.'},
 {'bag': '37:5 → 38:10', 'kural': "metin sayımı ('es-semâvâti ve'l-ardı ve mâ beynehumâ', 17 ayet) + nakarat3 sûre içi 3 ayet — eşler henüz okunmadı; KAYIT", 'not': 'göklerin ve yerin ve arasındakilerin.'},
 {'bag': '2:251 → 38:11 · 38:20', 'kural': "kök ipliği هزم (korpusta 3 ayet: 2:251, 38:11, 54:45) + 2:251 Dâvûd'a mülk ve hikmet / 38:20; 2:251 okundu, 54:45 henüz okunmadı; KAPATILAMAZ", 'not': 'bozgun; mülk ve hikmet.'},
 {'bag': '38:11 ↔ 38:13', 'kural': "kök ipliği حزب — 'mine'l-ahzâb' / 'ulâike'l-ahzâb'; iki ucu okundu", 'not': 'hizipler.'},
 {'bag': '38:1 · 38:12 · 38:17', 'kural': "okuma — ذو (MS) üçlüsü: zi'z-zikr / zu'l-evtâd / ze'l-eyd; KAPATILAMAZ", 'not': 'zû.'},
 {'bag': '38:8 ↔ 38:14', 'kural': "okuma — 1S iyelik yâsı düşmüş, fâsıla ب: 'azâbi' / 'ıqâbi'; iki ucu okundu", 'not': 'azabım, cezam.'},
 {'bag': '36:29 · 36:49 · 36:53 → 38:15', 'kural': "metin sayımı 'sayhaten vâhideten' (5 ayet) + xref 36:49; 54:31 henüz okunmadı", 'not': 'tek çığlık.'},
 {'bag': '38:9 → 38:16', 'kural': "Rab ipliği — 'rabbike' (2MS) / 'rabbenâ' (1P, inkârcıların sözü); okumada görüldü", 'not': 'Rab.'},
 {'bag': '38:6 → 38:17 · 20:130 → 38:17', 'kural': "صبر emri iki tarafa (inkârcılar / muhatap); metin sayımı 'isbir alâ mâ yaqûlûn' 4 ayet — 20:130 okundu, 50:39 ve 73:10 henüz okunmadı", 'not': 'sabret.'},
 {'bag': '21:79 · 34:10 → 38:17-19', 'kural': "xref (21:79, 'sahhara' + 'cibâl' yalnız iki ayet) + أوب ipliği (34:10 'evvibî' / 38:17, 38:19 'evvâb'); okundu; KAPATILAMAZ", 'not': 'dağlar ve kuşlar.'},
 {'bag': '38:10 → 38:20', 'kural': "kök ipliği ملك — göklerin mülkü (soru) / Dâvûd'un mülkü (verilen); okumada görüldü", 'not': 'mülk.'},
{'bag': '3:37 · 3:39 · 19:11 → 38:21', 'kural': "metin sayımı 'el-mihrâb' 4 ayet (üçü Zekeriyyâ sahnesi); okundu; KAPATILAMAZ", 'not': 'mihrap.'},
 {'bag': '1:6 → 38:22', 'kural': "metin sayımı 'ihdinâ' 2 ayet — hidâyet + sırât (kulun duası / davacıların isteği); okundu; KAPATILAMAZ", 'not': 'bizi ilet.'},
 {'bag': '38:20 → 38:23', 'kural': "kök ipliği خطب — 'fasle'l-hıtâb' / 'azzenî fi'l-hıtâb'; okumada görüldü", 'not': 'hitap.'},
 {'bag': '38:22 ↔ 38:24', 'kural': "nakarat3 'beğâ ba'd alâ ba'd' (GEÇER) — davacının sözü / Dâvûd'un genel kuralı", 'not': 'birbirine haksızlık.'},
 {'bag': '38:22 → 38:26', 'kural': "kalıp 'fahkum beyne … bi'l-haqqi ve lâ' (metin sayımı 3 ayet: 25:68, 38:22, 38:26) — istek / emir; okumada görüldü", 'not': 'hakla hükmet.'},
 {'bag': '38:24 → 38:25', 'kural': "kök ipliği غفر — 'fe'steğfera' / 'fe-ğafernâ'; okumada görüldü", 'not': 'bağışlanma.'},
 {'bag': '38:24 ↔ 38:28', 'kural': "nakarat3 'ellezîne âmenû ve amilu's-sâlihât' (GEÇER) — istisna / karşılaştırma", 'not': 'iman edip iyi iş yapanlar.'},
 {'bag': '38:25 → 38:40', 'kural': "nakarat3 'inne lehû indenâ le-zulfâ ve husne meâb' (6 kelime, GEÇER) — 38:40 henüz okunmadı; KAYIT", 'not': 'yakınlık ve güzel dönüş.'},
 {'bag': '2:30 → 38:26', 'kural': "metin sayımı 'halîfe' (tekil) 2 ayet — câilun (1S) / ce'alnâke (1P); okundu; KAPATILAMAZ", 'not': 'halife.'},
 {'bag': '38:16 → 38:26', 'kural': "metin sayımı 'yevmi'l-hisâb' (korpus 4, sûre 3) — alay / unutma; 38:53 ve 40:27 henüz okunmadı", 'not': 'hesap günü.'},
 {'bag': '21:16 · 38:10 → 38:27', 'kural': "metin sayımı ('ve mâ halaqne's-semâe ve'l-arda ve mâ beynehumâ', 2 ayet) + nakarat3 sûre içi; okundu (üçüncü eş henüz okunmadı)", 'not': 'boşuna yaratılmadı.'},
 {'bag': '38:24 → 38:27', 'kural': "kök ipliği ظنن — Dâvûd'un zannı / inkârcıların zannı; okumada görüldü", 'not': 'zan.'},
 {'bag': '6:92 · 6:155 · 14:1 → 38:29', 'kural': "metin sayımı 'kitâbun enzelnâhu' 4 ayet + xref 6:92, 6:155; okundu", 'not': 'indirdiğimiz kitap.'},
 {'bag': '38:8 → 38:29', 'kural': "kök ipliği نزل — 'e-unzile' (edilgen, inkârcıların sorusu) / 'enzelnâhu' (1P, etken); okumada görüldü", 'not': 'indirme.'},
 {'bag': '38:17 → 38:30 · 38:9 → 38:30', 'kural': "metin sayımı 'innehû evvâb' 3 ayet (38:44 henüz okunmadı) + kök ipliği وهب (el-vehhâb / vehebnâ); okumada görüldü", 'not': 'evvâb; bağış.'},
{'bag': '38:18 → 38:31', 'kural': "metin sayımı 'bi'l-aşiyy' 4 ayet (3:41 okundu, 40:55 henüz okunmadı) + kök ipliği عشو — dağların tesbihi / atların sunuluşu", 'not': 'akşamüstü.'},
 {'bag': '38:24 → 38:34', 'kural': "kök ipliği فتن + نوب aynı sırayla — Dâvûd 'fetennâhu … enâb' / Süleymân 'fetennâ … thumme enâb'; okumada görüldü, KAPATILAMAZ", 'not': 'sınama ve inâbe.'},
 {'bag': '3:8 · 37:100 → 38:35', 'kural': "metin sayımı 'inneke ente'l-vehhâb' 2 ayet + 'heb lî' 7 ayet; okundu", 'not': 'Vehhâb.'},
 {'bag': '38:9 · 38:30 → 38:35', 'kural': "kök ipliği وهب — el-vehhâb / vehebnâ / heb lî … el-vehhâb; okumada görüldü", 'not': 'bağış.'},
 {'bag': '38:10 · 38:20 → 38:35', 'kural': "kök ipliği ملك — göklerin mülkü (soru) / Dâvûd'un mülkü / Süleymân'ın istediği mülk; okumada görüldü", 'not': 'mülk.'},
 {'bag': '38:22 · 38:24 → 38:35', 'kural': "kök ipliği بغي iki anlam — haksızlık (beğâ, yebğî) / yakışma (yenbeğî, VII. bab); okumada görüldü", 'not': 'bağy / inbiğâ.'},
 {'bag': '21:81 · 34:12 → 38:36', 'kural': "metin sayımı 'tecrî bi-emrihî' 2 ayet — âsıfa / ruhâ'; okundu; KAPATILAMAZ", 'not': 'rüzgâr.'},
 {'bag': '38:18 → 38:36', 'kural': "kök ipliği سخر — dağlar Dâvûd'la / rüzgâr Süleymân'a; okumada görüldü", 'not': 'teshir.'},
 {'bag': '21:82 → 38:37', 'kural': "kök ipliği غوص (korpusta yalnız 2 ayet) — Süleymân'a dalan şeytanlar; okundu", 'not': 'dalgıç.'},
 {'bag': '14:49 → 38:38', 'kural': "metin sayımı 'muqarranîne fi'l-asfâd' 2 ayet (صفد yalnız bu ikisi) — kıyamette mücrimler / Süleymân'a bağlı şeytanlar; okundu", 'not': 'zincirler.'},
 {'bag': '38:3 → 38:38', 'kural': "kök ipliği قرن iki anlam — qarn (nesil) / muqarran (bağlı); okumada görüldü", 'not': 'qarn.'},
 {'bag': '3:37 → 38:39', 'kural': "metin sayımı 'bi-ğayri hisâb' 7 ayet (2:212, 3:27, 3:37, 24:38 okundu; 39:10, 40:40 henüz okunmadı); 3:37 aynı zamanda mihrap ayeti (38:21 bağı)", 'not': 'hesapsız.'},
 {'bag': '38:25 ↔ 38:40', 'kural': "nakarat3 tür TAM (6 kelime) — Dâvûd anlatısı / Süleymân anlatısı aynı cümleyle kapanıyor; iki ucu okundu", 'not': 'yakınlık ve güzel dönüş.'},
{'bag': '21:83 → 38:41', 'kural': "xref ('nâdâ rabbehû ennî messeniye') + metin sayımı 'nâdâ rabbehû' 4 ayet — durr / şeytân, nusb ve azâb; okundu; KAPATILAMAZ", 'not': 'Eyyûb\'un nidâsı.'},
 {'bag': '38:3 → 38:41', 'kural': "kök ipliği ندي — helâk edilenlerin cevapsız feryadı / Eyyûb'un nidâsı; okumada görüldü", 'not': 'nidâ.'},
 {'bag': '38:17 · 38:41 · 38:45', 'kural': "metin sayımı 've'zkur abdenâ/ibâdenâ' korpusta 3 ayet, üçü bu sûrede; okumada görüldü", 'not': 'an.'},
 {'bag': '21:84 → 38:43', 'kural': "xref + metin sayımı 'ehlehû ve mislehum meahum' 2 ayet — âteynâ/âbidîn / vehebnâ/uli'l-elbâb; okundu", 'not': 'aile ve misli.'},
 {'bag': '38:29 → 38:43', 'kural': "kök ipliği لبب — 'uli'l-elbâb' iki kez; okumada görüldü", 'not': 'akıl sahipleri.'},
 {'bag': '38:30 ↔ 38:44', 'kural': "nakarat3 'ni'me'l-abdu innehû evvâb' (GEÇER) — Süleymân / Eyyûb; 'innehû evvâb' 3 ayet (17, 30, 44) tamamı okundu", 'not': 'ne güzel kul.'},
 {'bag': '38:6 · 38:17 → 38:44', 'kural': "kök ipliği صبر — inkârcılar 'isbirû' / muhatap 'isbir' / Eyyûb 'sâbiran'; okumada görüldü", 'not': 'sabır.'},
 {'bag': '21:83-85 → 38:41-48', 'kural': "okuma — iki dizide Eyyûb'dan sonra İsmâîl ve Zü'l-Kifl ('ze'l-kifl' metin sayımı 2 ayet); kapanış sâbirîn / ahyâr; okundu; KAPATILAMAZ", 'not': 'anılanlar dizisi.'},
 {'bag': '38:1 · 38:12 · 38:17 → 38:48', 'kural': "okuma — ذو (MS) dördüncü: ze'l-kifl; okumada görüldü", 'not': 'zû.'},
 {'bag': '38:32 → 38:47 · 38:48', 'kural': "kök ipliği خير — hubbe'l-hayr / el-ahyâr (×2); okumada görüldü", 'not': 'hayır.'},
 {'bag': '13:29 · 38:25 · 38:40 → 38:49', 'kural': "metin sayımı 'husne meâb' 4 ayet — lehû (Dâvûd, Süleymân) / li'l-muttaqîn; okundu", 'not': 'güzel dönüş.'},
 {'bag': '38:28 → 38:49', 'kural': "kök ipliği وقي — muttaqîn karşılaştırmada / karşılıkta; okumada görüldü", 'not': 'sakınanlar.'},
{'bag': '38:42 → 38:51', 'kural': "kök ipliği شرب — Eyyûb'a gösterilen içecek / cennette içecek; okumada görüldü", 'not': 'şarâb.'},
 {'bag': '37:48 → 38:52', 'kural': "xref + metin sayımı 'qâsırâtu't-tarf' 3 ayet (55:56 henüz okunmadı) — în / etrâb; okundu", 'not': 'bakışını sınırlayanlar.'},
 {'bag': '38:9 → 38:52', 'kural': "kök ipliği عند kapanışı — 'em indehum' (soru) / 've indehum' (karşılık); okumada görüldü", 'not': 'yanlarında.'},
 {'bag': '38:16 · 38:26 → 38:53', 'kural': "metin sayımı 'yevmi'l-hisâb' — sûredeki üç geçiş: alay / unutma / vaat; 40:27 henüz okunmadı", 'not': 'hesap günü.'},
 {'bag': '38:49 ↔ 38:55', 'kural': "okuma — 've inne li-X le-Y meâb' kalıbı: muttaqîn/husn ↔ tâğîn/şerr (nakarat3 yakalamıyor); iki ucu okundu", 'not': 'iyi / kötü dönüş.'},
 {'bag': '38:17 … 38:55', 'kural': "kök ipliği أوب kapanışı — evvâb ×4 (17, 19, 30, 44) → meâb ×4 (25, 40, 49, 55); okumada görüldü", 'not': 'evvâb / meâb.'},
 {'bag': '14:29 → 38:56 · 38:60', 'kural': "esit2 (38:56, oran 0,85) + metin sayımı 'bi'se'l-qarâr' 2 ayet — 14:29'un iki yarısı 38:56 ve 38:60'ta; okundu; KAPATILAMAZ", 'not': 'cehennem, kötü karar yeri.'},
 {'bag': '38:8 → 38:57', 'kural': "kök ipliği ذوق — 'lemmâ yezûqû' (henüz tatmadılar) / 'fe'l-yezûqûh' (tatsınlar); okumada görüldü", 'not': 'tatma.'},
 {'bag': '38:51 ↔ 38:57', 'kural': "okuma — cennette şarâb / cehennemde hamîm ve ğassâq; KAPATILAMAZ", 'not': 'içecek.'},
 {'bag': '38:59 ↔ 38:60', 'kural': "metin sayımı 'lâ merhaben' 2 ayet — karşılıklı; okumada görüldü", 'not': 'merhaba yok.'},
{'bag': '7:38 → 38:61', 'kural': "xref + metin sayımı 'azâben dı'fen' 2 ayet — sonrakilerin öncekiler için kat kat azap istemesi; okundu", 'not': 'kat kat azap.'},
 {'bag': '38:16 → 38:61', 'kural': "Rab ipliği — inkârcı ağzında 'rabbenâ' iki kez: alay / cehennemde dua; okumada görüldü", 'not': 'rabbenâ.'},
 {'bag': '38:55 → 38:62', 'kural': "kök ipliği شرر — şerra meâb / eşrâr; okumada görüldü", 'not': 'kötüler.'},
 {'bag': '23:110 · 33:10 → 38:63', 'kural': "metin sayımı 'sihriyyâ' 3 ayet + 'zâğat … el-ebsâr' 2 ayet; okundu", 'not': 'alay, kayan gözler.'},
 {'bag': '38:18 · 38:36 → 38:63', 'kural': "kök ipliği سخر iki anlam — teshir / alay; okumada görüldü", 'not': 'sahhara / sihriyy.'},
 {'bag': '38:45 → 38:63', 'kural': "kök ipliği بصر — basiret sahipleri / kayan gözler; okumada görüldü", 'not': 'ebsâr.'},
 {'bag': '38:21 · 38:64 · 38:69', 'kural': "kök ipliği خصم — davacılar / ateş ehlinin çekişmesi / yüce topluluğun tartışması; okumada görüldü", 'not': 'çekişme.'},
 {'bag': '38:5 → 38:65', 'kural': "kök ipliği وحد kapanışı — 'ilâhen vâhidâ' itirazı / 'mâ min ilâhin illa'llâhu'l-vâhid'; okumada görüldü, KAPATILAMAZ", 'not': 'tek ilâh.'},
 {'bag': '12:39 · 14:48 → 38:65', 'kural': "metin sayımı 'el-vâhidu'l-qahhâr' 5 ayet (39:4, 40:16 henüz okunmadı); okundu", 'not': 'Kahhâr.'},
 {'bag': '38:10 · 38:27 → 38:66 · 37:5 → 38:66', 'kural': "nakarat3 sûre içi üçüncü eş (üçü okundu) + metin sayımı 'rabbu's-semâvâti ve'l-ardı ve mâ beynehumâ' 6 ayet", 'not': 'göklerin ve yerin Rabbi.'},
 {'bag': '38:24 · 38:25 · 38:35 → 38:66', 'kural': "kök ipliği غفر kapanışı — isteğfera / ğafernâ / iğfir lî / el-ğaffâr; okumada görüldü", 'not': 'mağfiret.'},
 {'bag': '38:31 → 38:68', 'kural': "kök ipliği عرض iki anlam — urıda (sunuldu) / mu'ridûn (yüz çevirenler); okumada görüldü", 'not': 'arz / irâz.'},
 {'bag': '37:8 → 38:69', 'kural': "metin sayımı 'el-meleu'l-a'lâ' 2 ayet; okundu", 'not': 'yüce topluluk.'},
 {'bag': '38:4 · 38:65 → 38:70 · 29:50 → 38:70', 'kural': "kök ipliği نذر kapanışı (munzir / innemâ ene munzir / innemâ ene nezîr) + metin sayımı 'innemâ ene nezîrun mubîn' 3 ayet (67:26 henüz okunmadı)", 'not': 'uyarıcı.'},
{'bag': '15:28 · 2:30 → 38:71', 'kural': "xref — 'iz qâle rabbuke li'l-melâiketi innî …'; madde salsâl/hame' (15:28) / tîn (38:71, 'beşeren min tîn' 1 ayet); okundu", 'not': 'beşer yaratma duyurusu.'},
 {'bag': '15:29-37 → 38:72-80', 'kural': "esit2 — 72, 73, 77, 79, 80 TAM; 78 BENZER; 74-76 ayrışıyor (2:34, 7:12'ye yaslanıyor); okundu; KAPATILAMAZ", 'not': 'secde sahnesi.'},
 {'bag': '32:9 → 38:72', 'kural': "xref (sevvâ … nefaha fîhi min rûh) — 3MS / 1S; okundu", 'not': 'ruh üfleme.'},
 {'bag': '38:36 → 38:72', 'kural': "kök ipliği روح iki anlam — rîh / rûhî; okumada görüldü", 'not': 'rüzgâr / ruh.'},
 {'bag': '2:34 → 38:74', 'kural': "metin sayımı 'istekbera ve kâne mine'l-kâfirîn' 2 ayet ('ebâ' yalnız 2:34'te); okundu", 'not': 'İblîs büyüklendi.'},
 {'bag': '38:2 → 38:74', 'kural': "kök ipliği كفر kapanışı — keferû … İblîs mine'l-kâfirîn; okumada görüldü", 'not': 'küfür.'},
 {'bag': '7:12 → 38:75 · 38:76', 'kural': "xref — 'mâ meneake' + 'ene hayrun minhu halaqtenî min nârin ve halaqtehû min tîn' (cevap harfi harfine); okundu", 'not': 'ateş ve çamur.'},
 {'bag': '38:44 · 38:45 → 38:75', 'kural': "kök ipliği يدي kapanışı — Eyyûb'un eli / güç (eydî) / bi-yedeyy; okumada görüldü", 'not': 'el.'},
 {'bag': '38:27 … 38:76', 'kural': "kök ipliği نور kapanışı — cehennem ateşi (27, 59, 61, 64) / İblîs'in yaratıldığı ateş (76); okumada görüldü", 'not': 'nâr.'},
 {'bag': '38:9 … 38:79', 'kural': "Rab ipliği kapanışı (10/10) — son 'rabbi' İblîs'in ağzında; okumada görüldü", 'not': 'Rab.'},
 {'bag': '38:15 → 38:79 · 38:80', 'kural': "kök ipliği نظر iki anlam — yanzuru (bekleme) / enzirnî, munzarîn (mühlet); okumada görüldü", 'not': 'bekleme / mühlet.'},
{'bag': '15:38-40 → 38:81-83', 'kural': "esit2 (81, 83 TAM) + metin sayımı 'le-uğviyennehum ecmaîn' 2 ayet — 15:39 gerekçe 'bimâ ağveytenî' / 38:82 yemin 'bi-izzetike'; okundu", 'not': 'azdırma yemini.'},
 {'bag': '38:79 → 38:81', 'kural': "okuma — istenen gün 'yevmi yub'asûn' / verilen gün 'yevmi'l-vaqti'l-ma'lûm' (15:36-38 emsali); KAPATILAMAZ", 'not': 'mühletin sınırı.'},
 {'bag': '38:2 … 38:82', 'kural': "kök ipliği عزز kapanışı — inkârcıların izzeti → el-azîz → azzenî → el-azîz → İblîs'in yemin ettiği izzet; okumada görüldü", 'not': 'izzet.'},
 {'bag': '38:46 → 38:83', 'kural': "kök ipliği خلص — ahlasnâhum / el-muhlasîn; okumada görüldü", 'not': 'ihlâs.'},
 {'bag': '7:18 · 11:119 · 32:13 → 38:85', 'kural': "metin sayımı 'le-emleenne cehenneme' 4 ayet; okundu", 'not': 'cehennemi doldurma.'},
 {'bag': '38:6 · 38:69 → 38:85', 'kural': "kök ipliği ملأ iki anlam — mele' (topluluk) / doldurma; okumada görüldü", 'not': 'mele / doldurma.'},
 {'bag': '38:73 · 38:82 · 38:85', 'kural': "kök ipliği جمع — ecmaûn (melekler) / ecmaîn (azdırılacaklar, cehennemdekiler); okumada görüldü", 'not': 'hepsi.'},
 {'bag': '12:104 → 38:86 · 38:87', 'kural': "metin sayımı 'aleyhi min ecr' 8 ayet + 'in huve illâ zikrun li'l-âlemîn' 4 ayet — 12:104 tek ayet / burada iki ayet; esit2 38:87 → 81:27 TAM (henüz okunmadı); KAPATILAMAZ", 'not': 'ücret yok, âlemlere zikir.'},
 {'bag': '38:1 → 38:87', 'kural': "kök ipliği ذكر kapanışı — zi'z-zikr (açılış) / zikrun li'l-âlemîn (kapanış); okumada görüldü", 'not': 'zikir.'},
 {'bag': '38:3 → 38:88', 'kural': "kök ipliği حين — 'lâte hîne menâs' / 'ba'de hîn'; sûrenin üçüncü ve son ayeti; okumada görüldü, KAPATILAMAZ", 'not': 'vakit.'},
 {'bag': '38:21 · 38:67 → 38:88', 'kural': "kök ipliği نبأ kapanışı — nebeu'l-hasm / nebeun azîm / nebeehû; okumada görüldü", 'not': 'haber.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AW_sad', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in SAD]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AW_sad'] = SAD
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AW_sad', len(SAD), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AR_sad', len(BAGLAR['AR_sad']))
