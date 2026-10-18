# -*- coding: utf-8 -*-
"""aday_ekle_52_tur.py — sûre 52 (Tûr) adayları (AX_tur) ve okuma bağları (AS_tur).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

TUR = [
]

BAGLAR = {"AS_tur": [
 {'bag': '51:60 → 52:1', 'kural': "okuma — ardışık sûre sınırı; fâsıla ن → ر; aday 1040 alanında kayıt, test yok", 'not': 'sûre sınırı.'},
 {'bag': '51:1 → 52:1', 'kural': "okuma — 've'z-zâriyât' / 've't-Tûr': ardışık iki sûre 've' yeminiyle açılıyor; aday 1040 alanında kayıt", 'not': 'yeminle açılış.'},
 {'bag': '19:52 · 20:80 · 28:29 · 28:46 · 23:20 → 52:1', 'kural': "'Tûr' lemma 10 ayet; okundu — 'cânibi't-Tûr' / 'Tûri Sînâ'' / izâfetsiz yemin nesnesi", 'not': 'Tûr.'},
 {'bag': '17:58 · 33:6 → 52:2', 'kural': "lemma dizisi 'kitâb + mestûr' 3 ayet; okundu — 'fi'l-kitâbi mestûrâ' (belirli + hâl) / 'kitâbin mestûr' (belirsiz + sıfat)", 'not': 'yazılmış kitap.'},
 {'bag': '17:13 → 52:3', 'kural': "'menşûr' lemma 2 ayet; okundu — kitap + 'menşûr' iki ayette", 'not': 'açılmış.'},
 {'bag': '52:1 → 52:6', 'kural': "okuma — beş yemin nesnesi (52:1, 2, 4, 5, 6; 52:3 sıfat zinciri); yemin ölçümde işaretsiz (517)", 'not': 'yemin dizisi.'},
 {'bag': '21:32 → 52:5', 'kural': "'saqf' lemma 4 ayet; okundu — 'ce'alne's-semâ'e saqfen mahfûzâ' / 'es-saqfi'l-merfû'' (gök adı 52:5'te yok; KAPATILAMAZ)", 'not': 'tavan.'},
 {'bag': '16:26 · 43:33 → 52:5', 'kural': "'saqf' lemma; okundu — çöken tavan / gümüş tavanlar / yükseltilmiş tavan", 'not': 'tavan.'},
 {'bag': '52:5 → 52:6', 'kural': "okuma — tavan / deniz (yüksek / alçak); karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'yukarı, aşağı.'},
 {'bag': '40:72 → 52:6', 'kural': "kök سجر 3 ayet; okundu — 'yuscerûn' ateşte / 'mescûr' deniz (iki okuma, KAPATILAMAZ)", 'not': 'mescûr.'},
 {'bag': '51:6 → 52:7', 'kural': "okuma — 'inne'd-dîne le-vâqi'' / 'inne azâbe rabbike le-vâqi'': iki sûrenin yemin cevabı; 'vâqi'' lemma 6 ayet; aday 1040 alanında kayıt", 'not': 'gerçekleşecek.'},
 {'bag': '42:22 → 52:7', 'kural': "'vâqi'' lemma 6 ayet; okundu", 'not': 'gerçekleşen.'},
 {'bag': '17:57 · 21:46 → 52:7', 'kural': "lemma dizisi 'azâb + rabb' 5 ayet; okundu — 'inne azâbe rabbike kâne mahzûrâ' / 'inne azâbe rabbike le-vâqi''", 'not': 'Rabbinin azabı.'},
 {'bag': '52:7 → 52:8', 'kural': "okuma — 'vâqi'' / 'dâfi''; 'lehû' azaba dönüyor; karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'gerçekleşen, savan.'},
 {'bag': '52:9 → 52:10', 'kural': "okuma — IMPF 3FS + özne + aynı kökten mef'ûl-i mutlak iki ayette (مور ×2, سير ×2)", 'not': 'paralel kuruluş.'},
 {'bag': '18:47 → 52:9 · 52:10', 'kural': "kök سير + جبل 5 ayet; okundu — 've yevme nusayyiru'l-cibâl' (1P, II. bab) / 'yevme … tesîru'l-cibâl' (dağlar özne, I. bab)", 'not': 'dağların yürümesi.'},
 {'bag': '13:31 → 52:10', 'kural': "kök سير + جبل; okundu — 'suyyirat bihi'l-cibâl' (edilgen, şart)", 'not': 'dağlar.'},
 {'bag': '34:18 → 52:10', 'kural': "'seyr' lemma 2 ayet; okundu — yolculuk / dağların yürüyüşü", 'not': 'seyr.'},
 {'bag': '51:60 → 52:11', 'kural': "okuma — 'fe-veylun li'llezîne keferû' / 'fe-veylun yevme'izin li'l-mukezzibîn'; aday 1040 alanında kayıt", 'not': 'veyl.'},
 {'bag': '16:36 · 43:25 → 52:11', 'kural': "'mukezzib' lemma 21 ayet; metin sûre sonunda basıldı ('âqibetu'l-mukezzibîn'; DUZELTME 52:11)", 'not': 'yalanlayanlar.'},
 {'bag': '9:65 · 43:83 → 52:12', 'kural': "kök خوض + لعب 5 ayet; okundu — 'nehûdu ve nel'ab' / 'yehûdû ve yel'abû' / 'fî havdin yel'abûn'", 'not': 'dalıp oynamak.'},
 {'bag': '43:83 → 51:60 → 52:11 · 52:12', 'kural': "okuma — 'yevmehumu'llezî yû'adûn' + 'yehûdû ve yel'abû' iki sûreye dağılıyor", 'not': 'zincir.'},
 {'bag': '52:9 · 52:10 → 52:13', 'kural': "okuma — fiil + aynı kökten mef'ûl-i mutlak üç ayette (مور, سير, دعع)", 'not': 'kuruluş.'},
 {'bag': '51:13 → 52:13', 'kural': "okuma — 'yevme hum ale'n-nâri yuftenûn' / 'yevme yuda''ûne ilâ nâri cehennem'; aday 1040 alanında kayıt", 'not': 'ateşe.'},
 {'bag': '32:20 · 34:42 · 37:21 → 52:14', 'kural': "lemma dizisi 'ellezî kâne + kezzebe' 5 ayet; xref (ölçüm); okundu", 'not': 'yalanladığınız.'},
 {'bag': '51:14 → 52:14', 'kural': "okuma — 'hâzâ'llezî kuntum bihî testa'cilûn' / 'hâzihi'n-nâru'lletî kuntum bihâ tukezzibûn'; aday 1040 alanında kayıt", 'not': 'işte bu.'},
 {'bag': '21:3 → 52:15', 'kural': "kök سحر + بصر 4 ayet; okundu — 'e-fe-te'tûne's-sihra ve entum tubsirûn' / 'e-fe-sihrun hâzâ em entum lâ tubsirûn'", 'not': 'büyü ve görme.'},
 {'bag': '15:15 · 27:13 · 36:9 → 52:15', 'kural': "kök سحر + بصر / 'lâ yubsirûn'; okundu", 'not': 'görmemek.'},
 {'bag': '36:64 → 52:16', 'kural': "'yaslâ' lemma 13 ayet; okundu — 'islevhe'l-yevme bimâ kuntum tekfurûn' / 'islevhâ … innemâ tuczevne mâ kuntum ta'melûn'", 'not': 'girin ona.'},
 {'bag': '14:21 → 52:16', 'kural': "'sevâ'' lemma 27 ayet; okundu — 'sevâ'un aleynâ e-cezi'nâ em sabarnâ' (1P) / 'fa'sbirû ev lâ tasbirû sevâ'un aleykum' (2MP)", 'not': 'birdir.'},
 {'bag': '45:28 → 52:16', 'kural': "lemma dizisi 'cezâ + mâ kâne amele' 4 ayet; okundu", 'not': 'karşılık.'},
 {'bag': '52:16', 'kural': "okuma — 'isbirû' / 'lâ tasbirû' ayet içinde; karşıt çift (aday 1039, okuma), 'sevâ'' ile eşitleniyor", 'not': 'sabır.'},
 {'bag': '15:45 · 51:15 → 52:17', 'kural': "esit2 BENZER 0,8889; lemma dizisi 'muttaqî + fî + cenne' 4 ayet; okundu — 've 'uyûn' / 've na'îm'; aday 1040 alanında kayıt", 'not': 'bahçeler.'},
 {'bag': '52:11 → 52:17', 'kural': "okuma — 'mukezzibîn' / 'muttaqîn'; ateş / bahçe; karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'iki topluluk.'},
 {'bag': '51:16 → 52:18', 'kural': "lemma dizisi 'mâ âtâ rabb' 2 ayet — korpusta yalnız 51:16 ve 52:18; okundu — 'âhizîn' / 'fâkihîn'; 51:15-16 → 52:17-18 sıralı; aday 1040 alanında kayıt", 'not': 'Rablerinin verdiği.'},
 {'bag': '36:55 · 44:27 → 52:18', 'kural': "'fâkih' lemma 3 ayet; okundu — cennet ehli / Firavun kavminin bıraktığı nimet", 'not': 'keyif sürenler.'},
 {'bag': '40:7 · 44:56 → 52:18', 'kural': "kök وقي + عذب + جحم 3 ayet; okundu — dua 'qihim' / 'veqâhum'", 'not': 'koruma.'},
 {'bag': '52:17 → 52:18', 'kural': "okuma — وقي: 'muttaqîn' sakınanlar / 'veqâhum' Rab korur (aday 1041 alanı, kök düzeyi; kayıt)", 'not': 'sakınma, koruma.'},
 {'bag': '52:16 → 52:19', 'kural': "okuma — 'mâ kuntum ta'melûn' iki zıt muhataba (ateş / bahçe); karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'aynı kapanış.'},
 {'bag': '44:54 → 52:20', 'kural': "lemma dizisi 'zuvvicet hûr în' 2 ayet; xref (ölçüm); okundu", 'not': 'eşleştirme.'},
 {'bag': '15:47 · 37:44 · 43:34 → 52:20', 'kural': "'surur' lemma 6 ayet; okundu — 'mutaqâbilîn' / 'yettekiûn' / 'mesfûfe'", 'not': 'tahtlar.'},
 {'bag': '29:12 · 47:3 → 52:21', 'kural': "lemma dizisi 'ellezî âmene ittebe'a' 3 ayet; okundu — uyan inananlar / uyan soy", 'not': 'uyma.'},
 {'bag': '13:23 · 40:8 → 52:21', 'kural': "'zurriyye' lemma 30 ayet; okundu — bahçelere soyla girme", 'not': 'soy.'},
 {'bag': '52:21', 'kural': "okuma — 'elhaqnâ' / 'mâ eletnâhum' ayet içinde; karşıt çift (aday 1039, okuma)", 'not': 'katma, eksiltme.'},
 {'bag': '36:57 · 44:55 → 52:22', 'kural': "'fâkihe' lemma 11 ayet; okundu", 'not': 'meyve.'},
 {'bag': '52:18 → 52:22', 'kural': "okuma — فكه sûre içi: 'fâkihîn' / 'fâkihe' iki anlam (1021 alanı)", 'not': 'aynı kök.'},
 {'bag': '18:21 · 20:62 → 52:23', 'kural': "'tenâza'a' lemma 7 ayet; okundu — iş üzerine çekişme / kadeh (KAPATILAMAZ)", 'not': 'yetenâze\'ûn.'},
 {'bag': '37:45 → 52:23 · 52:24', 'kural': "okuma — 'yutâfu aleyhim bi-ke's' / 'ke'sen' + 'yetûfu aleyhim ğilmân'", 'not': 'kadeh, dolaşma.'},
 {'bag': '37:49 → 52:24', 'kural': "'meknûn' lemma 4 ayet; okundu — 'ke-enne + benzetilen + meknûn' iki ayette", 'not': 'saklı.'},
 {'bag': '51:28 → 52:24', 'kural': "'ğulâm' lemma 13 ayet; okundu — müjdelenen oğul / hizmet eden delikanlılar; aday 1040 alanında kayıt", 'not': 'ğulâm.'},
 {'bag': '37:27 · 37:50 → 52:25', 'kural': "esit2 TAM; lemma dizisi 3 ayet; okundu (bağlam 37:22, 37:23, 37:24, 37:43) — zalimler / cennet ehli / bahçe ehli", 'not': 'karşılıklı soru.'},
 {'bag': '18:49 · 42:22 · 21:28 · 23:57 → 52:26', 'kural': "'muşfiq' lemma 8 ayet; okundu — hesap anında korkan / haşyetle korkan / önceden korkan", 'not': 'korku.'},
 {'bag': '52:26 → 52:27', 'kural': "okuma — 'muşfiqîn' / 'veqânâ'; karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'korku, korunma.'},
 {'bag': '12:90 · 28:82 → 52:27', 'kural': "lemma dizisi 'menne'llâhu alâ' 6 ayet; okundu", 'not': 'lütuf.'},
 {'bag': '15:27 → 52:27', 'kural': "'semûm' lemma 3 ayet; okundu — cinin yaratıldığı ateş / azap", 'not': 'semûm.'},
 {'bag': '52:17 → 52:18 → 52:27', 'kural': "okuma — وقي sûre içi [3/3]: 'muttaqîn' → 'veqâhum rabbuhum' (anlatıcı) → 'veqânâ' (lafız, bahçe ehlinin sözü)", 'not': 'koruma.'},
 {'bag': '28:53 → 52:28', 'kural': "lemma dizisi 'inne kâne min qabl' 2 ayet; okundu — 'muslimîn' / 'ned'ûhu'", 'not': 'önceden.'},
 {'bag': '19:14 · 19:32 → 52:28', 'kural': "'berr' lemma 22 ayet; okundu — insan için 'berran bi-vâlideyh / bi-vâlidetî' / Allah için 'el-berr' (aday 1041 alanında kayıt); 17:67 kara anlamı", 'not': 'berr.'},
 {'bag': '51:55 → 52:29', 'kural': "okuma — 've zekkir' / 'fe-zekkir'; aday 1040 alanında kayıt", 'not': 'öğüt ver.'},
 {'bag': '51:52 → 52:29', 'kural': "'mecnûn' lemma 11 ayet; okundu — 'sâhirun ev mecnûn' / 'bi-kâhinin ve lâ mecnûn'; aday 1040 alanında kayıt", 'not': 'mecnûn.'},
 {'bag': '15:6 · 26:27 · 44:14 · 51:39 → 52:29', 'kural': "'mecnûn' lemma; okundu — elçiye yöneltilen nitelik", 'not': 'nitelik.'},
 {'bag': '37:36 → 52:29 · 52:30', 'kural': "'şâ'ir' lemma 5 ayet; okundu — 'li-şâ'irin mecnûn' bir ayette / iki ayette", 'not': 'şair, mecnun.'},
 {'bag': '23:25 → 52:29 · 52:30', 'kural': "'terabbasa' lemma 11 ayet; okundu — 'bihî cinnetun fe-terabbasû bihî' / 'mecnûn' + 'neterabbasu bihî'", 'not': 'bekleme.'},
 {'bag': '9:52 · 20:135 · 21:5 → 52:30', 'kural': "'terabbasa', 'şâ'ir' lemmaları; okundu", 'not': 'bekleme, şair.'},
 {'bag': '52:27 → 52:30', 'kural': "okuma — منن sûre içi [1/2], [2/2]: 'menne' lütuf / 'el-menûn' zamanın felaketi (1021 alanı)", 'not': 'aynı kök.'},
 {'bag': '52:30 → 52:31', 'kural': "okuma — ربص: 'neterabbasu bihî' / 'terabbasû … mine'l-mutarabbisîn'", 'not': 'karşılıklı bekleme.'},
 {'bag': '9:52 · 20:135 → 52:31', 'kural': "'mutarabbis' lemma 3 ayet; okundu — 'innâ ma'akum mutarabbisûn' (1P) / 'innî ma'akum mine'l-mutarabbisîn' (1S)", 'not': 'bekleyin.'},
 {'bag': '51:53 → 52:32', 'kural': "lemma dizisi 'qavm tâğî' 2 ayet — korpusta yalnız 51:53 ve 52:32; okundu — 'bel hum' / 'em hum'; aday 1040 alanında kayıt", 'not': 'azgın topluluk.'},
 {'bag': '37:30 → 52:32', 'kural': "okuma — 'bel kuntum qavmen tâğîn' 2MP", 'not': 'azgınlık.'},
 {'bag': '12:44 · 21:5 → 52:32', 'kural': "'hulum' lemma 5 ayet; okundu — rüyalar / akıllar (KAPATILAMAZ)", 'not': 'ahlâm.'},
 {'bag': '10:38 · 11:13 → 52:33 · 52:34', 'kural': "okuma — 'em yeqûlûne'fterâhu … fe'tû bi-… mislihî … in kuntum sâdiqîn' bir ayette / 52:33 iddia + 52:34 meydan okuma iki ayette", 'not': 'uydurma, benzeri.'},
 {'bag': '37:157 · 17:88 → 52:34', 'kural': "lemma dizisi 'kâne sâdiq' 33 ayet; okundu — 'fe'tû bi-kitâbikum' / 'lâ ye'tûne bi-mislihî'", 'not': 'getirsinler.'},
 {'bag': '52:21 → 52:33', 'kural': "okuma — أمن [3/3]: 'âmenû' / 'lâ yu'minûn'; karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'inanmak.'},
 {'bag': '52:35', 'kural': "okuma — 'hulîqû' / 'el-hâliqûn' ayet içinde; karşıt çift (aday 1039, okuma)", 'not': 'yaratılan, yaratan.'},
 {'bag': '13:16 · 15:28 · 23:14 · 37:125 → 52:35', 'kural': "'hâliq' lemma 12 ayet; okundu — Allah için / 3MP için soru (aday 1041 alanında kayıt)", 'not': 'hâliq.'},
 {'bag': '52:35 → 52:36', 'kural': "okuma — خلق sûre içi [1,2/3] → [3/3]: kendilerinin yaratılması → göklerin ve yerin yaratılması", 'not': 'yaratma.'},
 {'bag': '13:16 → 52:36', 'kural': "'halaqa semâ ard' lemma dizisi 29 ayet; okundu — ortakların yaratması sorusu / onların yaratması sorusu", 'not': 'gökler ve yer.'},
 {'bag': '38:9 · 17:100 → 52:37', 'kural': "okuma — 'em indehum hazâ'inu rahmeti rabbike' / 'em indehum hazâ'inu rabbike'", 'not': 'hazineler.'},
 {'bag': '52:2 → 52:37', 'kural': "okuma — سطر [1/2], [2/2]: 'mestûr' / 'el-musaytirûn' (1021 alanı)", 'not': 'aynı kök.'},
 {'bag': '37:156 · 37:157 → 52:38', 'kural': "lemma dizisi 'sultân mubîn' 12 ayet; okundu — 'em lekum sultânun mubîn / fe'tû' iki ayette / bir ayette", 'not': 'apaçık delil.'},
 {'bag': '51:38 → 52:38', 'kural': "okuma — 'bi-sultânin mubîn' Mûsâ'nın getirdiği / dinleyenden istenen (dizi 12 ayet, sûre çiftine özgü değil)", 'not': 'delil.'},
 {'bag': '37:149 · 37:153 · 16:57 · 43:16 → 52:39', 'kural': "'bint' lemma 12 ayet; okundu — 'li-rabbike' / 'lehu' (gönderge adsız)", 'not': 'kızlar, oğullar.'},
 {'bag': '52:39', 'kural': "okuma — 'el-benât' / 'el-benûn', 'lehu' / 'lekum' ayet içinde; karşıt çift (aday 1039, okuma)", 'not': 'iki pay.'},
 {'bag': '36:21 → 52:40', 'kural': "lemma dizisi 'se'ele ecr' 3 ayet; okundu", 'not': 'ücret.'},
 {'bag': '9:98 → 52:30 · 52:31 · 52:40', 'kural': "'mağram' lemma 3 ayet; okundu — 'mağram' + 'terabbus' bir ayette / sûrede dağınık", 'not': 'borç, bekleme.'},
 {'bag': '52:25 → 52:40', 'kural': "okuma — سأل [1/2], [2/2]: birbirine sorma / ücret isteme", 'not': 'aynı kök.'},
 {'bag': '52:37 → 52:41', 'kural': "okuma — 'em indehum' iki kez: hazineler / gayb", 'not': 'yanlarında mı.'},
 {'bag': '52:2 → 52:41', 'kural': "okuma — كتب [1/2], [2/2]: 'kitâbin mestûr' / 'yektubûn'", 'not': 'yazma.'},
 {'bag': '21:70 · 37:98 → 52:42', 'kural': "lemma dizisi 'erâde keyd' 2 ayet; okundu — 1P ile tersine çevrilme / 'humu'l-mekîdûn' edilgen", 'not': 'tuzak.'},
 {'bag': '52:42', 'kural': "okuma — 'yurîdûne keydâ' / 'humu'l-mekîdûn' ayet içinde; karşıt çift (aday 1039, okuma)", 'not': 'tuzak kuran, düşen.'},
 {'bag': '12:76 → 52:42', 'kural': "okuma — كيد 'kidnâ' 1P / 'keyd' insanlar (aday 1041 alanı, kök düzeyi; kayıt)", 'not': 'keyd.'},
 {'bag': '28:68 · 28:71 → 52:43', 'kural': "'subhâna'llâhi … ammâ yuşrikûn' / 'ilâhun ğayru'llâh'; xref (ölçüm); okundu", 'not': 'başka ilâh.'},
 {'bag': '52:30 → 52:43', 'kural': "okuma — 'em' dizisi 12 ayette (lemma sayımı), 52:43 tenzihle kapanıyor", 'not': 'soru dizisi.'},
 {'bag': '17:92 · 26:187 · 34:9 → 52:44', 'kural': "kök كسف 5 ayet; okundu — gökten parça istenmesi / tehdit / görülüp buluta yorulması", 'not': 'gökten parça.'},
 {'bag': '24:43 · 30:48 → 52:44', 'kural': "'sehâb' lemma; okundu — 'rukâm' / 'merkûm' (ركم), 'kisefen'", 'not': 'yığılmış bulut.'},
 {'bag': '52:44', 'kural': "okuma — görülen 'kisfen mine's-semâ'' / söylenen 'sehâbun merkûm'; karşıt çift (aday 1039, okuma); çıpa L3 koluna sınırda (46:24 emsali)", 'not': 'algı, durum.'},
 {'bag': '43:83 → 52:45', 'kural': "okuma — 'fe-zerhum … hattâ yulâqû yevmehumu'llezî' ortak; 43:83'ün 'yehûdû ve yel'abû'su 52:12'de", 'not': 'bırak.'},
 {'bag': '51:44 → 52:45', 'kural': "okuma — صعق: 'es-sâ'iqa' / 'yus'aqûn'; aday 1040 alanında kayıt", 'not': 'çarpılma.'},
 {'bag': '39:68 → 52:45', 'kural': "'sa'iqa' lemma 2 ayet; okundu", 'not': 'bayılıp düşme.'},
 {'bag': '44:41 · 21:39 → 52:46', 'kural': "okuma — 'yevme lâ yuğnî … an … şey'en ve lâ hum yunsarûn' kalıbı; 'lâ hum yunsarûn' 6 ayet", 'not': 'yarar yok.'},
 {'bag': '52:42 → 52:46', 'kural': "okuma — كيد [1,2/3] → [3/3]: tuzak istenmesi → tuzağın yararsızlığı", 'not': 'keyd.'},
 {'bag': '32:21 → 52:47', 'kural': "okuma — 'dûne' ile iki azap katmanı", 'not': 'başka azap.'},
 {'bag': '10:55 · 44:39 → 52:47', 'kural': "lemma dizisi 'lâkinne ekser lâ alime' 9 ayet; okundu", 'not': 'çoğu bilmez.'},
 {'bag': '11:37 · 23:27 → 52:48', 'kural': "okuma — 'bi-a'yuninâ': gemiyi yapan / sabreden muhatap", 'not': 'gözlerimizin önünde.'},
 {'bag': '52:16 → 52:48', 'kural': "okuma — صبر [1,2/3] → [3/3]: ateş ehline 'sabır eşit' / muhataba 'sabret'; karşıt çift (aday 1039, okuma), ayetler arası", 'not': 'sabır.'},
 {'bag': '52:20 → 52:48', 'kural': "okuma — عين [1/2], [2/2]: 'în' / 'a'yun'", 'not': 'göz.'},
 {'bag': '50:39 · 50:40 → 52:48 · 52:49', 'kural': "esit2 52:49 → 50:40 BENZER 0,9048; okundu — sabır + 'sebbih bi-hamdi rabbik' + vakit, 'mine'l-leyli fe-sebbihhu ve edbâra's-sucûd / idbâra'n-nucûm' iki ayet sırasıyla (ardışık sûre değil)", 'not': 'kapanış tesbihi.'},
 {'bag': '52:43 → 52:48 → 52:49', 'kural': "okuma — سبح sûre içi [3/3]: 'subhâna'llâh' → 'sebbih' → 'fe-sebbihhu'", 'not': 'tesbih.'},
 {'bag': '52:1 → 52:49', 'kural': "okuma — sûre 've't-Tûr' yeminiyle açılıp 'idbâra'n-nucûm' ile kapanıyor (KAPATILAMAZ)", 'not': 'açılış, kapanış.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_tur', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in TUR]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_tur'] = TUR
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_tur', len(TUR), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_tur', len(BAGLAR['AS_tur']))
