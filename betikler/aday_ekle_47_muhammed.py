# -*- coding: utf-8 -*-
"""aday_ekle_47_muhammed.py — sûre 47 (Muhammed) adayları (AX_muhammed) ve okuma bağları (AS_muhammed).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

MUHAMMED = [
]

BAGLAR = {"AS_muhammed": [
 {'bag': '46:34 · 46:35 → 47:1', 'kural': "okuma — ardışık sûre sınırı; 'ellezîne keferû' (46:34) + helâk (46:35) → 'ellezîne keferû … adalle a'mâlehum'; aday 1040 alanında kayıt, test yok", 'not': 'sûre sınırı.'},
 {'bag': '16:88 · 22:25 → 47:1', 'kural': "lemma dizisi 'ellezîne keferû ve saddû an sebîli'llâh' 6 ayet (4:167, 47:32, 47:34 henüz okunmadı); okundu", 'not': 'inkâr edip Allah yolundan alıkoyanlar.'},
 {'bag': '47:1 → 47:4 · 47:8', 'kural': "lemma dizisi 'adalle + amel' 3 ayet, sûre içi; 47:4 olumsuz ('fe-len yudılle'); karşıt çift (aday 1039, okuma)", 'not': 'işlerin boşa çıkması.'},
 {'bag': '29:7 → 47:2', 'kural': "lemma dizisi 'keffera + an + seyyie' 12 ayet; okunan 29:7 — aynı açılış ('âmenû ve amilu's-sâlihât'), 1P gelecek / 3MS geçmiş; xref 66:8 (ölçüm) henüz okunmadı", 'not': 'kötülüklerin örtülmesi.'},
 {'bag': '33:40 → 47:2', 'kural': "'muhammed' lemma 4 ayet (3:144, 48:29 henüz okunmadı); okunan 33:40; sûre içi yalnız 47:2", 'not': 'Muhammed adı.'},
 {'bag': '47:2 → 47:5', 'kural': "lemma dizisi 'asleha + bâl' 2 ayet (sûre içi); 'bâl' lemma 4 ayet (12:50, 20:51 okundu)", 'not': 'hâllerini düzeltir.'},
 {'bag': '47:1 → 47:2', 'kural': "okuma — كفر 'keferû' (insan) / 'keffera' (Rab göndergeli) kök ortak; aday 1041 alanına sınırda, kayıt", 'not': 'inkâr / örtme.'},
 {'bag': '22:62 · 31:30 → 47:3', 'kural': "okuma — 'zâlike bi-enne … el-haqq … el-bâtıl' çerçevesi (okundu): orada hak Allah, bâtıl çağrılanlar; 47:3'te iki grubun uyduğu; 'huve'l-haqq' 47:2'de indirilen için (aday 1041 alanına sınırda)", 'not': 'hak ve bâtıl.'},
 {'bag': '14:25 → 47:3', 'kural': "xref (ölçüm); 'yadribu'llâhu'l-emsâle li'n-nâs'; okundu", 'not': 'Allah örnek verir.'},
 {'bag': '47:3 → 47:9', 'kural': "lemma dizisi 'zâlike bi-enne' 34 ayet; sûre içi 47:3, 47:9 (47:11, 26, 28 henüz okunmadı)", 'not': 'gerekçe kalıbı.'},
 {'bag': '26:93 · 26:227 · 42:39 · 42:41 → 47:4', 'kural': "'intesara' lemma 7 ayet; okunanlarda öznesi insan ya da ilâhlar, 47:4'te Allah — aday 1041 alanında kayıt, test yok", 'not': 'kendini savunma / intikam.'},
 {'bag': '17:15 · 35:18 · 39:7 · 16:25 → 47:4', 'kural': "'vizr' lemma 11 ayet; okunanlarda günah yükü, 47:4'te savaşın yükü (okumada görüldü)", 'not': 'yük.'},
 {'bag': '47:4 → 47:5 · 47:6', 'kural': "okuma — 'ellezîne qutilû' haberi üç ayete yayılıyor ('len yudılle' → 'se-yehdîhim, yuslihu' → 'yudhiluhum'); zamir göndergesi 1017", 'not': 'öldürülenlerin akıbeti.'},
 {'bag': '40:8 → 47:6', 'kural': "lemma dizisi 'edhale + cenne' 16 ayet; okunan 40:8", 'not': 'cennete sokma.'},
 {'bag': '47:4 → 47:7', 'kural': "okuma — 'le'ntesara' (Allah, 'intesara') → 'tensurû'llâha yensurkum' (نصر kök ortak); aday 1041 alanında kayıt", 'not': 'yardım.'},
 {'bag': '47:7 → 47:8', 'kural': "okuma — 'yuthebbit aqdâmekum' / 'fe-ta'sen lehum'; 'ellezîne âmenû' / 'ellezîne keferû'; karşıt çift (aday 1039, okuma), KAPATILAMAZ", 'not': 'sağlam ayak / düşüş.'},
 {'bag': '47:2 → 47:9', 'kural': "okuma — 'âmenû bimâ nuzzile' / 'kerihû mâ enzela'llâh'; karşıt çift (aday 1039, okuma)", 'not': 'indirilene iman / hoş görmeme.'},
 {'bag': '33:19 → 47:9', 'kural': "'ahbata' lemma 4 ayet; lemma dizisi 'ahbata + amel' 3 ayet sûre içi (47:28, 47:32 henüz okunmadı); okunan 33:19 ('fe-ahbata'llâhu a'mâlehum')", 'not': 'işleri boşa çıkardı.'},
 {'bag': '12:109 · 30:9 · 35:44 · 40:21 · 40:82 → 47:10', 'kural': "lemma dizisi 'e-lem yesîrû fi'l-ard fe-yenzurû keyfe kâne âqıbetu'llezîne min qablihim' 6 ayet; hepsi okundu — devamı farklı", 'not': 'yeryüzünde gezip bakmadılar mı.'},
 {'bag': '46:25 → 47:10', 'kural': "'dammera' lemma 8 ayet (7:137 henüz okunmadı); ardışık sûrelerde aynı lemma (okuma; aday 1040 alanında kayıt)", 'not': 'yerle bir etme.'},
 {'bag': '44:41 · 10:30 → 47:11', 'kural': "'mevlâ' lemma 14 ayet; 'Allah + mevlâ' lemma dizisi 6 ayet (3:150, 6:62, 8:40, 66:2 henüz okunmadı); 44:41 insanlar arası — aday 1041 alanında kayıt", 'not': 'mevlâ.'},
 {'bag': '47:3 · 47:9 → 47:11', 'kural': "'zâlike bi-enne' sûre içi üçüncü (lemma dizisi 34 ayet)", 'not': 'gerekçe kalıbı.'},
 {'bag': '47:11 → 47:13', 'kural': "okuma — 'lâ mevlâ lehum' / 'fe-lâ nâsira lehum' (aynı 'lâ + ad + lehum' biçimi)", 'not': 'koruyucusuz / yardımcısız.'},
 {'bag': '22:14 · 22:23 → 47:12', 'kural': "lemma dizisi 'inna'llâhe yudhilu'llezîne âmenû ve amilu's-sâlihât' 3 ayet; xref (ölçüm); okundu — devamı farklı", 'not': 'cennete sokar.'},
 {'bag': '41:24 → 47:12', 'kural': "lemma dizisi 'en-nâr + mesvâ + lehum' 2 ayet; okundu", 'not': 'ateş barınak.'},
 {'bag': '47:12 → 47:19', 'kural': "'mesvâ' lemma sûre içi 47:12, 47:19", 'not': 'kalış yeri.'},
 {'bag': '22:45 · 22:48 → 47:13', 'kural': "lemma dizisi 've ke-eyyin min qarye' 4 ayet (65:8 henüz okunmadı); okundu — 22:45 aynı açılış + 'ehleknâ'", 'not': 'nice kasaba helâk.'},
 {'bag': '30:9 · 35:44 · 40:21 · 40:82 → 47:13', 'kural': "okuma — 'eşeddu … quvveten' karşılaştırması (47:10'un eşlerinde); 47:13'te muhatabın kasabasıyla", 'not': 'daha güçlü.'},
 {'bag': '11:17 · 35:8 → 47:14', 'kural': "lemma dizisi 'e-fe-men kâne alâ beyyinetin min rabbihî' 2 ayet (11:17); 'men zuyyine lehû sû'u amelihî' 2 ayet (35:8); xref 11:17 (ölçüm); iki açılış yan yana (okuma, KAPATILAMAZ)", 'not': 'açık delil / süslenen kötü iş.'},
 {'bag': '47:14 → 47:16', 'kural': "lemma dizisi 've'ttebe'û ehvâ'ehum' 14 ayet; sûre içi 47:14, 47:16", 'not': 'heveslere uyma.'},
 {'bag': '13:35 → 47:15', 'kural': "lemma dizisi 'meselu'l-cenneti'lletî vu'ide'l-muttaqûn' 2 ayet; xref (ölçüm); okundu — devamı farklı", 'not': 'cennetin örneği.'},
 {'bag': '16:66 · 37:46 → 47:15', 'kural': "'leben' lemma 2 ayet (16:66); 'lezzetin li'ş-şâribîn' lemma dizisi 2 ayet (37:46); okundu", 'not': 'süt, içenlere lezzet.'},
 {'bag': '44:46 · 37:67 → 47:15', 'kural': "'hamîm' lemma 19 ayet; okunan 44:46, 37:67 (okumada görüldü)", 'not': 'kaynar su.'},
 {'bag': '47:14 → 47:15', 'kural': "okuma — 'e-fe-men … ke-men' / 'meselu … ke-men' aynı karşılaştırma iskeleti (KAPATILAMAZ)", 'not': 'iki teşbihli soru.'},
 {'bag': '10:42 → 47:16', 'kural': "lemma dizisi 've minhum men yestemi'u ileyk' 3 ayet (6:25 henüz okunmadı); okundu — 10:42 çoğul fiil", 'not': 'seni dinleyenler.'},
 {'bag': '16:108 → 47:16', 'kural': "lemma dizisi 'ulâ'ike'llezîne taba'a'llâhu alâ qulûbihim' 2 ayet; okundu — 16:108 kalp + kulak + göz", 'not': 'kalplerin mühürlenmesi.'},
 {'bag': '47:16 → 47:17', 'kural': "okuma — mühürlenip hevese uyan / hidayeti artırılan; karşıt çift (aday 1039, okuma)", 'not': 'iki grup.'},
 {'bag': '9:124 → 47:17 · 47:20', 'kural': "okuma — 'unzilet sûre' + 'zâdethum îmânâ' (9:124) / 'zâdehum huden' (47:17), 'unzilet sûratun' (47:20)", 'not': 'sûre indirilince artış.'},
 {'bag': '43:66 → 47:18', 'kural': "lemma dizisi 'hel yenzurûne ille's-sâ'ate en te'tiyehum bağteh' 2 ayet; xref (ölçüm); okundu — devamı farklı", 'not': 'saati mi bekliyorlar.'},
 {'bag': '40:55 · 12:29 → 47:19', 'kural': "lemma dizisi 'istağfir li-zenbik' 4 ayet (3:135 henüz okunmadı); okundu", 'not': 'günahın için bağışlanma dile.'},
 {'bag': '47:16 → 47:19', 'kural': "okuma — علم 'ûtu'l-ilm' (insan) → 'fa'lem' (2MS) / 've'llâhu ya'lemu' (Allah) aynı ayette; aday 1041 alanında kayıt", 'not': 'bilme.'},
 {'bag': '33:12 → 47:20', 'kural': "lemma dizisi 'ellezîne fî qulûbihim marad' 10 ayet; sûre içi 47:20, 47:29 (henüz okunmadı); okunan 33:12", 'not': 'kalplerinde hastalık olanlar.'},
 {'bag': '33:19 → 47:20', 'kural': "okuma — 'ke'llezî yuğşâ aleyhi mine'l-mevt' / 'nazara'l-mağşiyyi aleyhi mine'l-mevt' (farklı kalıp, aynı benzetme)", 'not': 'ölüm baygınlığı.'},
 {'bag': '47:2 · 47:9 → 47:20', 'kural': "okuma — نزل II/IV ikiliği: 'nuzzile' / 'enzele' → 'nuzzilet' / 'unzilet'", 'not': 'indirme.'},
 {'bag': '24:53 → 47:21', 'kural': "'tâ'a' lemma 3 ayet (4:81 henüz okunmadı); okundu — 'tâ'atun ma'rûfe' / 'tâ'atun ve qavlun ma'rûf'", 'not': 'itaat.'},
 {'bag': '47:20 → 47:21', 'kural': "okuma — 'zukira fîhe'l-qıtâl … fe-evlâ lehum' → 'tâ'atun ve qavlun ma'rûf' (KAPATILAMAZ)", 'not': 'savaş anılınca.'},
 {'bag': '47:11 · 47:20 → 47:22', 'kural': "okuma — ولي kökü 'mevlâ' / 'evlâ' / 'teveleytum'", 'not': 'kök ortak.'},
 {'bag': '47:15 → 47:22', 'kural': "'qatta'a' lemma sûre içi 47:15, 47:22 (bağırsaklar / akrabalık)", 'not': 'parçalama / koparma.'},
 {'bag': '13:8 · 22:5 · 31:34 · 33:6 → 47:22', 'kural': "'erhâm' lemma 12 ayet; okunanlarda rahim (13:8, 22:5, 31:34) ve akrabalık (33:6); 47:22 akrabalık (okumada görüldü)", 'not': 'rahim / akrabalık.'},
 {'bag': '22:46 → 47:23', 'kural': "''amiye' lemma 5 ayet; okundu — 22:46 gözler değil kalpler kör olur / 47:23 gözleri kör etti (KAPATILAMAZ)", 'not': 'körlük.'},
 {'bag': '46:26 → 47:23', 'kural': "okuma — kulak/göz 46:26'da verilen, 47:23'te alınan", 'not': 'organlar.'},
 {'bag': '47:16 → 47:24', 'kural': "okuma — 'taba'a … alâ qulûbihim' / 'alâ qulûbin aqfâluhâ' (mühür / kilit)", 'not': 'kalp üzerinde.'},
 {'bag': '23:68 · 38:29 → 47:24', 'kural': "'tedebbera' lemma 4 ayet (4:82 henüz okunmadı); okundu; lemma dizisi 'e-fe-lâ yetedebberûne'l-qur'ân' 2 ayet (4:82)", 'not': 'düşünme.'},
 {'bag': '18:64 → 47:25', 'kural': "'irtedde' lemma 8 ayet; okunan 18:64 somut geri dönüş / 47:25 hidayetten dönüş", 'not': 'geri dönme.'},
 {'bag': '12:18 · 20:96 → 47:25', 'kural': "'sevvele' lemma 4 ayet; okundu — süsleyen nefis / 47:25 şeytân", 'not': 'süslü gösterme.'},
 {'bag': '13:32 · 22:44 → 47:25', 'kural': "'emlâ' lemma 8 ayet; okundu — 'fe-emleytu' (1S) / 47:25 öznesi belirsiz; aday 1041 alanına sınırda", 'not': 'mühlet / uzun ümit.'},
 {'bag': '47:25 → 47:27', 'kural': "okuma — 'dubur' lemması: 'irteddû alâ edbârihim' / 'yadribûne … edbârahum' (KAPATILAMAZ)", 'not': 'arka.'},
 {'bag': '47:9 → 47:26', 'kural': "okuma — 'kerihû mâ enzela'llâh' / 'kerihû mâ nezzela'llâh' (IV / II bab)", 'not': 'indirileni hoş görmeyenler.'},
 {'bag': '47:21 → 47:26', 'kural': "okuma — طوع 'tâ'a' / 'senutî'ukum'; أمر ''azeme'l-emr' / 'ba'di'l-emr'", 'not': 'itaat ve iş.'},
 {'bag': '16:28 · 16:32 · 32:11 → 47:27', 'kural': "lemma dizisi 'teveffâ + melâ'ike' 5 ayet (4:97 henüz okunmadı); okundu; xref 8:50 (henüz okunmadı)", 'not': 'meleklerin can alması.'},
 {'bag': '47:3 · 47:4 → 47:27', 'kural': "okuma — ضرب üç öznede: Allah (örnek), inananlar (boyun), melekler (yüz ve arka)", 'not': 'vurma.'},
 {'bag': '47:9 → 47:28', 'kural': "lemma dizisi 'ahbata + amel' sûre içi; 'kerihû … fe-ahbata a'mâlehum' iki ayette, nesne indirilen → hoşnutluk", 'not': 'işleri boşa çıkardı.'},
 {'bag': '9:72 → 47:28', 'kural': "'ridvân' lemma 13 ayet; okunan 9:21, 9:72, 9:109", 'not': 'hoşnutluk.'},
 {'bag': '47:20 → 47:29', 'kural': "nakarat3 'ellezîne fî qulûbihim marad' (ölçüm, GEÇER); sûre içi", 'not': 'kalplerinde hastalık olanlar.'},
 {'bag': '47:13 → 47:29', 'kural': "'ahraca' lemma: kasaba / Allah özne; aday 1041 alanında kayıt", 'not': 'çıkarma.'},
 {'bag': '47:26 → 47:29', 'kural': "okuma — 'ya'lemu isrârahum' / 'yuhrica … adğânehum'", 'not': 'gizli olanın açığa çıkması.'},
 {'bag': '47:4 → 47:30', 'kural': "'lev + şâ'a' lemma dizisi 38 ayet; sûre içi 47:4 (3MS lafız) / 47:30 (1P)", 'not': 'dileseydi / dileseydik.'},
 {'bag': '47:6 → 47:30', 'kural': "okuma — عرف ''arrafe' (Allah, II) / ''arafa' (2MS, I); aday 1041 alanına sınırda", 'not': 'tanıtma / tanıma.'},
 {'bag': '47:19 · 47:26 → 47:30', 'kural': "okuma — 've'llâhu ya'lemu' sûre içi üç kez", 'not': 'Allah bilir.'},
 {'bag': '47:4 → 47:31', 'kural': "'belâ' lemma 18 ayet; sûre içi 47:4 (3MS lafız) / 47:31 (1P)", 'not': 'sınama.'},
 {'bag': '21:35 · 9:94 → 47:31', 'kural': "okuma — 'nebluvkum' (21:35), 'ahbârikum' (9:94; 'ahbâr' lemma 3 ayet)", 'not': 'sınama, haberler.'},
 {'bag': '47:1 · 22:25 → 47:32 · 47:34', 'kural': "lemma dizisi 'ellezîne keferû ve saddû an sebîli'llâh' sûre içi 47:1, 32, 34 (nakarat3 GEÇER, ölçüm); 'inne' ile 4 ayet (4:167 henüz okunmadı)", 'not': 'sûre başı ve sonu.'},
 {'bag': '47:25 → 47:32', 'kural': "nakarat3 'min ba'di mâ tebeyyene lehumu'l-hudâ' (ölçüm, GEÇER)", 'not': 'hidayet belli olduktan sonra.'},
 {'bag': '9:39 → 47:32 · 47:38', 'kural': "okuma — 'lâ tedurrûhu şey'â' (→ 47:32 'len yadurru'llâhe şey'â') ve 'yestebdil qavmen ğayrakum' (→ 47:38; lemma dizisi 2 ayet, xref ölçüm); 9:39 tek ayette, 47'de iki ayete dağılmış (KAPATILAMAZ)", 'not': 'başka topluluk; zarar veremezsiniz.'},
 {'bag': '47:9 · 47:28 → 47:32', 'kural': "lemma dizisi 'ahbata + amel' 3 ayet, üçü sûre içi; 47:32 gelecek ('se-')", 'not': 'işlerin boşa çıkması.'},
 {'bag': '24:54 · 33:66 → 47:33', 'kural': "lemma dizisi 'etî'u'llâhe ve etî'u'r-rasûl' 6 ayet (4:59, 5:92, 64:12 henüz okunmadı); okundu; xref 4:59, 8:20 (ölçüm)", 'not': 'Allah\'a ve Elçi\'ye itaat.'},
 {'bag': '10:81 → 47:33', 'kural': "'ebtale' lemma 4 ayet; 10:81 Allah özne / 47:33 2MP — aday 1041 alanında kayıt", 'not': 'boşa çıkarma.'},
 {'bag': '47:32 → 47:33', 'kural': "okuma — 'se-yuhbitu a'mâlehum' / 'lâ tubtılû a'mâlekum'; karşıt çift (aday 1039, okuma)", 'not': 'işler.'},
 {'bag': '47:7 → 47:33', 'kural': "'yâ eyyuhe'llezîne âmenû' sûre içi iki nidâ (lemma dizisi 89 ayet)", 'not': 'nidâ.'},
 {'bag': '9:80 → 47:34', 'kural': "lemma dizisi 'fe-len yağfira'llâhu lehum' 3 ayet (63:6 henüz okunmadı); okundu", 'not': 'bağışlamayacak.'},
 {'bag': '47:19 → 47:34', 'kural': "okuma — 'istağfir' / 'len yağfira'; karşıt çift (aday 1039, okuma)", 'not': 'bağışlanma.'},
 {'bag': '19:4 → 47:35', 'kural': "'vehene' lemma 5 ayet; okunan 19:4 (kemik) / 47:35 (gevşeme)", 'not': 'zayıflık.'},
 {'bag': '47:1 → 47:35', 'kural': "okuma — عمل sûre içi ilk ve son: 'adalle a'mâlehum' / 'len yetirakum a'mâlekum'", 'not': 'işler.'},
 {'bag': '29:64 → 47:36', 'kural': "okuma — 'el-hayâtu'd-dunyâ … lehvun ve la'ib' sıra ters, hasr farklı; xref 6:32, 57:20 (ölçüm) henüz okunmadı", 'not': 'oyun ve oyalanma.'},
 {'bag': '47:29 → 47:37', 'kural': "'adğân' lemma 2 ayet, ikisi sûre içi; 'ahraca' lemması — 47:29 özne lafız / 47:37 özne adsız", 'not': 'kinlerin çıkması.'},
 {'bag': '9:76 → 47:37 · 47:38', 'kural': "okuma — 'bahilû … ve tevellev' (9:76) / 'tebhalû' + 'yebhal' ×3 + 'in tetevellev' (KAPATILAMAZ)", 'not': 'cimrilik ve yüz çevirme.'},
 {'bag': '29:6 · 31:12 → 47:38', 'kural': "okuma — 'men … fe-innemâ … li/an nefsih' kalıbı (cihad, şükür, cimrilik)", 'not': 'kendi aleyhine / lehine.'},
 {'bag': '35:15 → 47:38', 'kural': "lemma dizisi 'entum + faqîr' 2 ayet; okundu — sıra ters (insan → Allah / Allah → insan)", 'not': 'zengin / yoksul.'},
 {'bag': '47:22 → 47:38', 'kural': "okuma — 'in teveleytum' / 'in tetevellev': aynı şart, iki sonuç (bozgunculuk / başka topluluk)", 'not': 'yüz çevirme.'},
 {'bag': '47:3 · 47:10 · 47:15 → 47:38', 'kural': "'mesel' lemma sûre içi 4 ayet (ölçüm [4/4])", 'not': 'örnek / benzer.'},
 {'bag': '47:3 → 47:10', 'kural': "'mesel' lemma sûre içi 47:3, 47:10 (47:15, 47:38 henüz okunmadı): 'emsâlehum' / 'emsâluhâ'", 'not': 'örnekler / benzerleri.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_muhammed', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in MUHAMMED]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_muhammed'] = MUHAMMED
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_muhammed', len(MUHAMMED), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_muhammed', len(BAGLAR['AS_muhammed']))
