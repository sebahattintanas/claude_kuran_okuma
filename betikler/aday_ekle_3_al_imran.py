# -*- coding: utf-8 -*-
"""aday_ekle_3_al_imran.py — sûre 3 (Âl-i İmrân) adayları (AX_al_imran) ve okuma bağları (AS_al_imran).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1043'ten); betik sıranın kopmadığını doğrular.
"""
import json

AL_IMRAN = [
]

BAGLAR = {"AS_al_imran": [
 # blok 1-6
 {'bag': '2:255 → 3:2', 'kural': "okuma — harekesiz 'allâhu lâ ilâhe illâ huwa'l-hayyu'l-qayyûm' (2:255'te ayetin başı, burada ayetin tamamı) (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '20:111 → 3:2', 'kural': "okuma — lemma 'qayyûm': 'li'l-hayyi'l-qayyûm' / 'huwa'l-hayyu'l-qayyûm'", 'not': 'lemma eşi.'},
 {'bag': '2:163 → 3:2', 'kural': "okuma — harekesiz 'lâ ilâhe illâ huwa'", 'not': 'kalıp eşi.'},
 {'bag': '3:2 → 3:6', 'kural': "sûre içi — harekesiz 'lâ ilâhe illâ huwa' + esmâ çifti ('el-hayyu'l-qayyûm' / 'el-'azîzu'l-hakîm')", 'not': 'sûre içi kalıp eşi.'},
 {'bag': '2:97 → 3:3', 'kural': "okuma — harekesiz 'musaddiqan li-mâ beyne yedeyh' ('nezzelehû 'alâ qalbike' / 'nezzele 'aleyke'l-kitâb')", 'not': 'kalıp eşi.'},
 {'bag': '35:31 → 3:3', 'kural': "okuma — harekesiz 'musaddiqan li-mâ beyne yedeyh' + 'el-kitâb', 'el-haqq' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '9:111 → 3:3', 'kural': "okuma — harekesiz 'et-tevrâte ve'l-incîl'", 'not': 'kalıp eşi.'},
 {'bag': '3:3 → 3:4', 'kural': "sûre içi — 'min qablu' zarfı 've enzele't-tevrâte ve'l-incîl' fiiline bağlanıyor", 'not': 'sûre içi ardışık.'},
 {'bag': '2:185 → 3:4', 'kural': "okuma — harekesiz 'huden li'n-nâs' + lemma 'furqân'", 'not': 'kalıp eşi.'},
 {'bag': '14:47 → 3:4', 'kural': "okuma — harekesiz ''azîzun zu'ntiqâm' ('inna'llâhe' / 've'llâhu')", 'not': 'kalıp eşi.'},
 {'bag': '14:38 → 3:5', 'kural': "okuma — harekesiz 'fi'l-ardi ve lâ fi's-semâ'' + lemma 'yaxfâ' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '2:129 → 3:6', 'kural': "okuma — harekesiz 'el-'azîzu'l-hakîm' (2MS 'inneke ente' / 'huwa')", 'not': 'kalıp eşi.'},
 {'bag': '30:48 → 3:6', 'kural': "okuma — harekesiz 'keyfe yeşâ'' (bulutu yayma / rahimlerde biçimlendirme)", 'not': 'kalıp eşi.'},
 {'bag': '40:64 → 3:6', 'kural': "okuma — lemma 'savvara': PERF 've savvarakum' / IMPF 'yusavvirukum'", 'not': 'lemma eşi.'},
 {'bag': '64:3 → 3:6', 'kural': "okuma — lemma 'savvara': PERF 've savvarakum' / IMPF 'yusavvirukum'", 'not': 'lemma eşi.'},
 # blok 7-9
 {'bag': '13:39 → 3:7', 'kural': "okuma — harekesiz 'ummu'l-kitâb' ('ve 'indehû ummu'l-kitâb' / 'hunne ummu'l-kitâb')", 'not': 'kalıp eşi.'},
 {'bag': '43:4 → 3:7', 'kural': "okuma — harekesiz 'ummu'l-kitâb' ('fî ummi'l-kitâbi ledeynâ' / 'hunne ummu'l-kitâb')", 'not': 'kalıp eşi.'},
 {'bag': '39:23 → 3:7', 'kural': "okuma — lemma 'muteşâbih': kitabın tamamı 'kitâben muteşâbihen' / kitabın bir kısmı 've uxaru muteşâbihât' (aday 1039 öz-tanım ipliği, test edilmez)", 'not': 'lemma eşi.'},
 {'bag': '2:25 → 3:7', 'kural': "okuma — lemma 'muteşâbih' (rızkın sıfatı / âyetlerin sıfatı)", 'not': 'lemma eşi.'},
 {'bag': '47:20 → 3:7', 'kural': "okuma — lemma 'muhkeme': 'sûratun muhkemetun' / 'âyâtun muhkemât'", 'not': 'lemma eşi.'},
 {'bag': '2:70 → 3:7', 'kural': "okuma — lemma 'teşâbehe' ('teşâbehe 'aleynâ' / 'mâ teşâbehe minhu')", 'not': 'lemma eşi.'},
 {'bag': '28:53 → 3:7', 'kural': "okuma — harekesiz 'âmennâ bihî' ('min rabbinâ' / 'min 'indi rabbinâ')", 'not': 'kalıp eşi.'},
 {'bag': '2:269 → 3:7', 'kural': "okuma — önek kesilmiş 've mâ yezzekkeru illâ ulu'l-elbâb' + lemma dizisi 'mâ' 'tezekkera' 'illâ' 'zû' 'elbâb'", 'not': 'kalıp eşi.'},
 {'bag': '3:7 → 3:8', 'kural': "sûre içi — 'fî qulûbihim zeyğ' / 'lâ tuziğ qulûbenâ' (kök زيغ + 'qalb')", 'not': 'sûre içi ardışık.'},
 {'bag': '18:10 → 3:8', 'kural': "okuma — harekesiz 'min ledunke rahmeh' ('rabbenâ âtinâ' / 'rabbenâ … ve heb lenâ')", 'not': 'kalıp eşi.'},
 {'bag': '38:35 → 3:8', 'kural': "okuma — harekesiz 'inneke ente'l-vehhâb' + IMPV 'heb'", 'not': 'kalıp eşi.'},
 {'bag': '61:5 → 3:8', 'kural': "okuma — lemma 'ezâğa' + 'qulûb' ('ezâğa'llâhu qulûbehum' / 'lâ tuziğ qulûbenâ')", 'not': 'lemma eşi.'},
 {'bag': '3:8 → 3:9', 'kural': "sûre içi — 'rabbenâ' ile açılan dua, 'inneke ente'l-vehhâb' / 'inneke câmi'u'n-nâs'", 'not': 'sûre içi ardışık.'},
 {'bag': '13:31 → 3:9', 'kural': "okuma — harekesiz 'inna'llâhe lâ yuxlifu'l-mî'âd' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '32:2 → 3:9', 'kural': "okuma — harekesiz 'lâ reybe fîh' (kitabın sıfatı / günün sıfatı)", 'not': 'kalıp eşi.'},
 # blok 10-14
 {'bag': '58:17 → 3:10', 'kural': "okuma — harekesiz 'len tuğniye 'anhum emvâluhum ve lâ evlâduhum' ('ashâbu'n-nâr' / 'vequdu'n-nâr') (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '2:24 → 3:10', 'kural': "okuma — lemma 'vequd' ('veqûduha'n-nâs' / 'hum vequdu'n-nâr')", 'not': 'lemma eşi.'},
 {'bag': '3:4 → 3:10', 'kural': "sûre içi — harekesiz 'inne'llezîne keferû'", 'not': 'sûre içi kalıp eşi.'},
 {'bag': '3:10 → 3:11', 'kural': "sûre içi — 'ke-de'bi âli fir'avn' benzetmesi önceki ayetteki 'ellezîne keferû'ya bağlanıyor", 'not': 'sûre içi ardışık.'},
 {'bag': '44:37 → 3:11', 'kural': "okuma — önek kesilmiş 've'llezîne min qablihim'", 'not': 'kalıp eşi.'},
 {'bag': '40:21 → 3:11', 'kural': "okuma — önek kesilmiş 'fe-exazehumu'llâhu bi-zunûbihim' + 'min qablihim' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '2:196 → 3:11', 'kural': "okuma — harekesiz 'şedîdu'l-'iqâb'", 'not': 'kalıp eşi.'},
 {'bag': '2:249 → 3:12', 'kural': "okuma — lemma 'ğalebe' ('ğalebet fieten kesîreten' / 'se-tuğlebûne')", 'not': 'lemma eşi.'},
 {'bag': '13:18 → 3:12', 'kural': "okuma — önek kesilmiş 've bi'se'l-mihâd' (cehennem ile)", 'not': 'kalıp eşi.'},
 {'bag': '2:249 → 3:13', 'kural': "okuma — lemma 'fie' (az / çok topluluk; karşılaşan iki topluluk)", 'not': 'lemma eşi.'},
 {'bag': '9:111 → 3:13', 'kural': "okuma — harekesiz 'fî sebîli'llâh' ile savaşma ('yuqâtilûne' / 'tuqâtilu')", 'not': 'kalıp eşi.'},
 {'bag': '24:44 → 3:13', 'kural': "okuma — harekesiz 'inne fî zâlike le-'ibraten li-uli'l-ebsâr'", 'not': 'kalıp eşi.'},
 {'bag': '79:26 → 3:13', 'kural': "okuma — harekesiz 'inne fî zâlike le-'ibrah'", 'not': 'kalıp eşi.'},
 {'bag': '19:59 → 3:14', 'kural': "okuma — lemma 'şehve' ('ve'ttebe'u'ş-şehevât' / 'hubbu'ş-şehevât')", 'not': 'lemma eşi.'},
 {'bag': '11:83 → 3:14', 'kural': "okuma — lemma 'musevveme' (''inde rabbik' / ''indehû')", 'not': 'lemma eşi.'},
 {'bag': '9:38 → 3:14', 'kural': "okuma — harekesiz 'metâ'u'l-hayâti'd-dunyâ'", 'not': 'kalıp eşi.'},
 {'bag': '13:29 → 3:14', 'kural': "okuma — lemma 'me'âb': nekre 'husnu me'âb' / belirli 'husnu'l-me'âb'", 'not': 'lemma eşi.'},
 {'bag': '38:25 → 3:14', 'kural': "okuma — lemma 'me'âb': ''indenâ … husne me'âb' / ''indehû husnu'l-me'âb'", 'not': 'lemma eşi.'},
 # blok 15-20
 {'bag': '3:14 → 3:15', 'kural': "sûre içi — 'bi-xayrin min zâlikum': 'zâlikum' önceki ayetteki 'metâ'u'l-hayâti'd-dunyâ'ya işaret", 'not': 'sûre içi ardışık.'},
 {'bag': '9:72 → 3:15', 'kural': "okuma — harekesiz 'cennâtun tecrî min tahtihe'l-enhâru xâlidîne fîhâ' + önek kesilmiş 've ridvânun mina'llâh'", 'not': 'kalıp eşi.'},
 {'bag': '14:23 → 3:15', 'kural': "okuma — harekesiz 'cennâtun tecrî min tahtihe'l-enhâru xâlidîne fîhâ' ('rabbihim' ile)", 'not': 'kalıp eşi.'},
 {'bag': '40:44 → 3:15', 'kural': "okuma — harekesiz 'basîrun bi'l-'ibâd' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '3:15 → 3:16', 'kural': "sûre içi — 'ellezîne yeqûlûne' 'li'llezîne'tteqav'a bağlanıyor", 'not': 'sûre içi ardışık.'},
 {'bag': '3:15 → 3:20', 'kural': "sûre içi — önek kesilmiş 've'llâhu basîrun bi'l-'ibâd' + 'qul' ile söz (ölçüm xref)", 'not': 'sûre içi kalıp eşi.'},
 {'bag': '2:201 → 3:16', 'kural': "okuma — önek kesilmiş 've qinâ 'azâbe'n-nâr' ('rabbenâ' ile açılan dua) (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '3:16 → 3:17', 'kural': "sûre içi — nitelik dizisi 'ellezîne yeqûlûne'ye bağlanıyor", 'not': 'sûre içi ardışık.'},
 {'bag': '51:18 → 3:17', 'kural': "okuma — lemma 'seher' + kök غفر ('bi'l-eshâri hum yesteğfirûn' / 've'l-mustağfirîne bi'l-eshâr')", 'not': 'lemma eşi.'},
 {'bag': '33:35 → 3:17', 'kural': "okuma — lemma 'qânit' + 'sâdiq', 'sâbir' nitelik dizisi", 'not': 'lemma eşi.'},
 {'bag': '3:6 → 3:18', 'kural': "sûre içi — harekesiz 'lâ ilâhe illâ huwa'l-'azîzu'l-hakîm'", 'not': 'sûre içi kalıp eşi.'},
 {'bag': '42:14 → 3:19', 'kural': "okuma — harekesiz 'illâ min ba'di mâ câ'ehumu'l-'ilmu bağyen beynehum' ('tefarraqû' / 'ixtelefe') (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '45:17 → 3:19', 'kural': "okuma — harekesiz 'illâ min ba'di mâ câ'ehumu'l-'ilmu bağyen beynehum' ('ixtelefû' / 'ixtelefe') (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '2:213 → 3:19', 'kural': "okuma — harekesiz 'bağyen beynehum' + ayrılık", 'not': 'kalıp eşi.'},
 {'bag': '98:4 → 3:19', 'kural': "okuma — harekesiz 'ellezîne ûtu'l-kitâb' + 'illâ min ba'di mâ câ'ethum' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '2:202 → 3:19', 'kural': "okuma — harekesiz 'serî'u'l-hisâb'", 'not': 'kalıp eşi.'},
 {'bag': '2:137 → 3:20', 'kural': "okuma — önek kesilmiş 'fe-qadi'htedev' + 've in tevellev fe-innemâ' şart dizisi", 'not': 'kalıp eşi.'},
 {'bag': '13:40 → 3:20', 'kural': "okuma — önek kesilmiş 'fe-innemâ 'aleyke'l-belâğ'", 'not': 'kalıp eşi.'},
 {'bag': '62:2 → 3:20', 'kural': "okuma — lemma 'ummiyy'", 'not': 'lemma eşi.'},
 # blok 21-25
 {'bag': '9:34 → 3:21', 'kural': "okuma — önek kesilmiş 'fe-beşşirhum bi-'azâbin elîm'", 'not': 'kalıp eşi.'},
 {'bag': '3:21 → 3:22', 'kural': "sûre içi — 'ulâ'ike' önceki ayetteki 'inne'llezîne …' öznelerine işaret", 'not': 'sûre içi ardışık.'},
 {'bag': '2:217 → 3:22', 'kural': "okuma — harekesiz 'habitat a'mâluhum fi'd-dunyâ ve'l-âxira' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '9:69 → 3:22', 'kural': "okuma — harekesiz 'habitat a'mâluhum fi'd-dunyâ ve'l-âxira' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '16:37 → 3:22', 'kural': "okuma — önek kesilmiş 've mâ lehum min nâsirîn'", 'not': 'kalıp eşi.'},
 {'bag': '24:47 → 3:23', 'kural': "okuma — harekesiz 'thumme yetevellâ ferîqun minhum'", 'not': 'kalıp eşi.'},
 {'bag': '24:48 → 3:23', 'kural': "okuma — harekesiz 'li-yahkume beynehum' + 'ferîqun minhum mu'ridûn' (çağrılma / yüz çevirme)", 'not': 'kalıp eşi.'},
 {'bag': '9:76 → 3:23', 'kural': "okuma — önek kesilmiş 've hum mu'ridûn' + 'tevellev'", 'not': 'kalıp eşi.'},
 {'bag': '3:23 → 3:24', 'kural': "sûre içi — 'zâlike' önceki ayetteki yüz çevirmeye işaret", 'not': 'sûre içi ardışık.'},
 {'bag': '2:80 → 3:24', 'kural': "okuma — 'len temessene'n-nâru illâ eyyâmen ma'dûdeten' / '… ma'dûdât' (tekil / çoğul sıfat; ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '2:184 → 3:24', 'kural': "okuma — harekesiz 'eyyâmen ma'dûdât' (oruç günleri / ateşin dokunacağı iddia edilen günler)", 'not': 'kalıp eşi.'},
 {'bag': '2:275 → 3:24', 'kural': "okuma — harekesiz 'zâlike bi-ennehum qâlû'", 'not': 'kalıp eşi.'},
 {'bag': '10:30 → 3:24', 'kural': "okuma — harekesiz 'mâ kânû yefterûn'", 'not': 'kalıp eşi.'},
 {'bag': '3:9 → 3:25', 'kural': "sûre içi — harekesiz 'li-yevmin lâ reybe fîh' + toplama ('câmi'' / 'ceme'nâhum')", 'not': 'sûre içi kalıp eşi.'},
 {'bag': '2:281 → 3:25', 'kural': "okuma — harekesiz 'kullu nefsin mâ kesebet' + önek kesilmiş 've hum lâ yuzlemûn' ('tuveffâ' / 'vuffiyet')", 'not': 'kalıp eşi.'},
 {'bag': '14:51 → 3:25', 'kural': "okuma — harekesiz 'kullu nefsin mâ kesebet'", 'not': 'kalıp eşi.'},
 # blok 26-28
 {'bag': '39:46 → 3:26', 'kural': "okuma — 'quli'llâhumme' + 2MS hitapla sıfat ('fâtıra's-semâvât' / 'mâlike'l-mulk'); lemma 'Allâhumme'", 'not': 'kalıp eşi.'},
 {'bag': '10:10 → 3:26', 'kural': "okuma — lemma 'Allâhumme'", 'not': 'lemma eşi.'},
 {'bag': '1:4 → 3:26', 'kural': "okuma — lemma 'mâlik' ('mâliki yevmi'd-dîn' / 'mâlike'l-mulk')", 'not': 'lemma eşi.'},
 {'bag': '2:247 → 3:26', 'kural': "okuma — mülk verme ('yu'tî mulkehû men yeşâ'' / 'tu'ti'l-mulke men teşâ'') (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '66:8 → 3:26', 'kural': "okuma — harekesiz 'inneke 'alâ kulli şey'in qadîr'", 'not': 'kalıp eşi.'},
 {'bag': '3:26 → 3:27', 'kural': "sûre içi — 'Allâhumme'ye 2MS hitap sürüyor (IMPF 2MS dizisi)", 'not': 'sûre içi ardışık.'},
 {'bag': '22:61 → 3:27', 'kural': "okuma — lemma 'yûlicu': 'yûlicu'l-leyle fi'n-nehâri ve yûlicu'n-nehâra fi'l-leyl' (3MS / 2MS)", 'not': 'lemma eşi.'},
 {'bag': '31:29 → 3:27', 'kural': "okuma — lemma 'yûlicu': gece / gündüz girdirme (3MS / 2MS)", 'not': 'lemma eşi.'},
 {'bag': '10:31 → 3:27', 'kural': "okuma — harekesiz 'el-hayye mine'l-meyyit' (soru içinde / hitap) (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '30:19 → 3:27', 'kural': "okuma — harekesiz 'el-hayye mine'l-meyyit' ters dizisiyle (3MS / 2MS) (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '2:212 → 3:27', 'kural': "okuma — harekesiz 'bi-ğayri hisâb' + rızık ve dileme ('yerzuqu men yeşâ'' / 'terzuqu men teşâ'') (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '24:38 → 3:27', 'kural': "okuma — harekesiz 'bi-ğayri hisâb' + 'yerzuqu men yeşâ'' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '2:231 → 3:28', 'kural': "okuma — önek kesilmiş 've men yef'al zâlike'", 'not': 'kalıp eşi.'},
 {'bag': '35:18 → 3:28', 'kural': "okuma — önek kesilmiş 've ile'llâhi'l-masîr' (ölçüm xref)", 'not': 'xref eşi.'},
 # blok 29-32
 {'bag': '2:284 → 3:29', 'kural': "okuma — 'in tubdû mâ fî enfusikum ev tuxfûhu' / 'in tuxfû mâ fî sudûrikum ev tubdûhu' (fiiller ters sırada) + 'mâ fi's-semâvâti ve mâ fi'l-ard' + 've'llâhu 'alâ kulli şey'in qadîr'", 'not': 'kalıp eşi.'},
 {'bag': '2:255 → 3:29', 'kural': "okuma — harekesiz 'mâ fi's-semâvâti ve mâ fi'l-ard' + bilme ('ya'lemu')", 'not': 'kalıp eşi.'},
 {'bag': '59:6 → 3:29', 'kural': "okuma — önek kesilmiş 've'llâhu 'alâ kulli şey'in qadîr'", 'not': 'kalıp eşi.'},
 {'bag': '3:26 → 3:29', 'kural': "sûre içi — ''alâ kulli şey'in qadîr' (2MS 'inneke' / lafız)", 'not': 'sûre içi kalıp eşi.'},
 {'bag': '16:111 → 3:30', 'kural': "okuma — harekesiz 'kullu nefsin mâ 'amilet' + 'yevme' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '39:70 → 3:30', 'kural': "okuma — harekesiz 'kullu nefsin mâ 'amilet' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '37:57 → 3:30', 'kural': "okuma — lemma 'muhdar'", 'not': 'lemma eşi.'},
 {'bag': '18:12 → 3:30', 'kural': "okuma — lemma 'emed' (süre)", 'not': 'lemma eşi.'},
 {'bag': '2:207 → 3:30', 'kural': "okuma — önek kesilmiş 've'llâhu ra'ûfun bi'l-'ibâd' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '3:28 → 3:30', 'kural': "sûre içi — önek kesilmiş 've yuhazzirukumu'llâhu nefseh'", 'not': 'sûre içi kalıp eşi.'},
 {'bag': '20:90 → 3:31', 'kural': "okuma — önek kesilmiş 'fe-ttebi'ûnî' (1S konuşan, 2MP muhatap)", 'not': 'kalıp eşi.'},
 {'bag': '33:71 → 3:31', 'kural': "okuma — önek kesilmiş 've yağfir lekum zunûbekum' (şart cevabı)", 'not': 'kalıp eşi.'},
 {'bag': '2:218 → 3:31', 'kural': "okuma — önek kesilmiş 've'llâhu ğafûrun rahîm'", 'not': 'kalıp eşi.'},
 {'bag': '3:31 → 3:32', 'kural': "sûre içi — 'qul' ile açılan ardışık emirler ('fe-ttebi'ûnî' / 'atî'u'llâhe ve'r-rasûl')", 'not': 'sûre içi ardışık.'},
 {'bag': '24:54 → 3:32', 'kural': "okuma — 'qul atî'u'llâhe ve atî'u'r-rasûl fe-in tevellev' / 'qul atî'u'llâhe ve'r-rasûl fe-in tevellev' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '30:45 → 3:32', 'kural': "okuma — harekesiz 'lâ yuhibbu'l-kâfirîn'", 'not': 'kalıp eşi.'},
 # blok 33-37
 {'bag': '2:47 → 3:33', 'kural': "okuma — harekesiz ''ale'l-'âlemîn' (üstün kılma / seçme)", 'not': 'kalıp eşi.'},
 {'bag': '2:132 → 3:33', 'kural': "okuma — harekesiz 'inna'llâhe'stafâ'", 'not': 'kalıp eşi.'},
 {'bag': '35:32 → 3:33', 'kural': "okuma — lemma 'istafâ'", 'not': 'lemma eşi.'},
 {'bag': '3:33 → 3:34', 'kural': "sûre içi — 'zurriyyeten' (nasb) önceki ayetteki seçilenlere bağlanıyor", 'not': 'sûre içi ardışık.'},
 {'bag': '2:224 → 3:34', 'kural': "okuma — önek kesilmiş 've'llâhu semî'un 'alîm'", 'not': 'kalıp eşi.'},
 {'bag': '2:127 → 3:35', 'kural': "okuma — 'teqabbel minnâ' / 'teqabbel minnî' + harekesiz 'inneke ente's-semî'u'l-'alîm' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '12:51 → 3:35', 'kural': "okuma — harekesiz 'qâleti'mra'et'", 'not': 'kalıp eşi.'},
 {'bag': '3:35 → 3:36', 'kural': "sûre içi — 'imra'etu 'imrân'ın sözü sürüyor ('rabbi innî' ×2)", 'not': 'sûre içi ardışık.'},
 {'bag': '16:98 → 3:36', 'kural': "okuma — harekesiz 'mine'ş-şeytâni'r-racîm' (sığınma)", 'not': 'kalıp eşi.'},
 {'bag': '39:70 → 3:36', 'kural': "okuma — harekesiz 'a'lemu bimâ'", 'not': 'kalıp eşi.'},
 {'bag': '3:36 → 3:37', 'kural': "sûre içi — 'teqabbel' isteği / 'fe-teqabbelehâ rabbuhâ'", 'not': 'sûre içi ardışık.'},
 {'bag': '2:212 → 3:37', 'kural': "okuma — harekesiz 'yerzuqu men yeşâ'u bi-ğayri hisâb' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '24:38 → 3:37', 'kural': "okuma — harekesiz 'yerzuqu men yeşâ'u bi-ğayri hisâb' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '3:27 → 3:37', 'kural': "sûre içi — 've terzuqu men teşâ'u bi-ğayri hisâb' / 'yerzuqu men yeşâ'u bi-ğayri hisâb' (ölçüm xref)", 'not': 'sûre içi xref eşi.'},
 {'bag': '19:11 → 3:37', 'kural': "okuma — lemma 'mihrâb' (Zekeriyyâ)", 'not': 'lemma eşi.'},
 {'bag': '71:17 → 3:37', 'kural': "okuma — 'enbete … nebâtâ' (insan için yetiştirme benzetmesi)", 'not': 'kalıp eşi.'},
 # blok 38-41
 {'bag': '11:45 → 3:38', 'kural': "okuma — 've nâdâ nûhun rabbehû fe-qâle rabbi' / 'de'â zekeriyyâ rabbehû qâle rabbi' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '14:39 → 3:38', 'kural': "okuma — 'le-semî'u'd-du'â'' / 'semî'u'd-du'â'' + 'vehebe lî' / 'heb lî'", 'not': 'kalıp eşi.'},
 {'bag': '25:74 → 3:38', 'kural': "okuma — 'rabbenâ heb lenâ … zurriyyâtinâ' / 'rabbi heb lî … zurriyyeten' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '3:38 → 3:39', 'kural': "sûre içi — dua / 'fe-nâdethu'l-melâ'ike' ile müjde", 'not': 'sûre içi ardışık.'},
 {'bag': '3:37 → 3:39', 'kural': "sûre içi — lemma 'mihrâb'", 'not': 'sûre içi lemma eşi.'},
 {'bag': '12:25 → 3:39', 'kural': "okuma — lemma 'seyyid'", 'not': 'lemma eşi.'},
 {'bag': '19:7 → 3:39', 'kural': "okuma — 'nubeşşiruke bi-ğulâmin ismuhû yahyâ' / 'yubeşşiruke bi-yahyâ'", 'not': 'kalıp eşi.'},
 {'bag': '3:39 → 3:40', 'kural': "sûre içi — müjde / 'ennâ yekûnu lî ğulâm'", 'not': 'sûre içi ardışık.'},
 {'bag': '19:8 → 3:40', 'kural': "okuma — harekesiz 'qâle rabbi ennâ yekûnu lî ğulâm' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '19:5 → 3:40', 'kural': "okuma — lemma ''âqir' ('imra'atî')", 'not': 'lemma eşi.'},
 {'bag': '19:7 → 3:40', 'kural': "okuma — lemma 'ğulâm'", 'not': 'lemma eşi.'},
 {'bag': '22:18 → 3:40', 'kural': "okuma — harekesiz 'allâhu yef'alu mâ yeşâ'' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '3:40 → 3:41', 'kural': "sûre içi — ardışık 'qâle rabbi' / 'qâle' söz çiftleri", 'not': 'sûre içi ardışık.'},
 {'bag': '19:10 → 3:41', 'kural': "okuma — harekesiz 'qâle rabbi'c'al lî âyeh' + 'qâle âyetuke ellâ tukellime'n-nâse thelâthe' (ölçüm xref)", 'not': 'xref eşi.'},
 {'bag': '2:196 → 3:41', 'kural': "okuma — harekesiz 'thelâthete eyyâm'", 'not': 'kalıp eşi.'},
 {'bag': '18:24 → 3:41', 'kural': "okuma — önek kesilmiş 've'zkur rabbek'", 'not': 'kalıp eşi.'},
 {'bag': '40:55 → 3:41', 'kural': "okuma — 've sebbih … bi'l-'aşiyyi ve'l-ibkâr'", 'not': 'kalıp eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_al_imran', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in AL_IMRAN]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_al_imran'] = AL_IMRAN
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_al_imran', len(AL_IMRAN), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_al_imran', len(BAGLAR['AS_al_imran']))
