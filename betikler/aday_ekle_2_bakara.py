# -*- coding: utf-8 -*-
"""aday_ekle_2_bakara.py — sûre 2 (Bakara) adayları (AX_bakara) ve okuma bağları (AS_bakara).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1042'den); betik sıranın kopmadığını doğrular.
"""
import json

BAKARA = [
]

BAGLAR = {"AS_bakara": [
 # blok 21-25
 {'bag': '14:32 → 2:22', 'kural': "okuma — harekesiz 've enzele mine's-semâ'i mâ'en fe-exrace bihî mine's-semerâti rizqan lekum' (korpusun iki geçişi): 'Allâhu'llezî xalaqa's-semâvâti ve'l-ard' ile / 'ellezî ce'ale lekumu'l-arda firâşâ' ile", 'not': 'kalıp eşi.'},
 {'bag': '14:30 → 2:22', 'kural': "okuma — 'ce'ale' + 'li'llâh' + lemma 'endâd': PERF 3MP haber / NEHY 2MP yasak", 'not': 'kalıp eşi.'},
 {'bag': '55:54 → 2:22', 'kural': "okuma — lemma 'firâş': çoğul 'furuş', yaslanılan döşekler / tekil, yer döşek", 'not': 'lemma eşi.'},
 {'bag': '56:34 → 2:22', 'kural': "okuma — lemma 'firâş': çoğul 'furuş', yükseltilmiş / tekil, yer (korpusun üç geçişi okundu)", 'not': 'lemma eşi.'},
 {'bag': '10:38 → 2:23', 'kural': "okuma — 'fe'tû bi-sûratin mislihî' / 'bi-sûratin min mislihî' ('min' farkı); 'meni'steta'tum' / 'şuhedâ'akum'; ikisi de 'min dûni'llâhi in kuntum sâdiqîn' ile biter", 'not': 'kalıp eşi.'},
 {'bag': '11:13 → 2:23', 'kural': "okuma — 'bi-'aşri suverin mislihî mufterayât' / 'bi-sûratin min mislihî'; soru + 'qul' / şart", 'not': 'kalıp eşi.'},
 {'bag': '66:6 → 2:24', 'kural': "okuma — harekesiz 'vaqûduhe'n-nâsu ve'l-hicâra' (korpusun iki geçişi): nekre 'nâran', 'qû' emrinin nesnesi / belirli 'en-nâr', 'ittequ' emrinin nesnesi", 'not': 'kalıp eşi.'},
 {'bag': '85:5 → 2:24', 'kural': "okuma — lemma 'vaqûd': 'zâti'l-vaqûd' / 'vaqûduhe'n-nâs'", 'not': 'lemma eşi.'},
 {'bag': '39:23 → 2:25', 'kural': "okuma — lemma 'muteşâbih': indirilen kitabın sıfatı / getirilen rızkın hâli", 'not': 'lemma eşi.'},
 {'bag': '80:14 → 2:25', 'kural': "okuma — lemma 'mutahhara': nitelenen adı o ayette olmayan sıfat / eşlerin sıfatı", 'not': 'lemma eşi.'},
 {'bag': '2:21 → 2:24', 'kural': "sûre içi — kök وقي: nesnesiz 'tetteqûn' / 'ittequ'n-nâr'; lemma 'nâs': hitap edilenler / ateşin yakıtı", 'not': 'sûre içi eş.'},
 {'bag': '2:23 → 2:24', 'kural': "sûre içi — şart zinciri: 'in kuntum fî raybin … fe'tû' / 'fe-in lem tef'alû … fe'ttequ'", 'not': 'sûre içi eş.'},
 {'bag': '2:24 → 2:25', 'kural': "sûre içi — ateş, kâfirler için hazırlanmış / bahçeler, inananlara müjde (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 # blok 26-29
 {'bag': '74:31 → 2:26', 'kural': "okuma — harekesiz 'mâzâ erâde'llâhu bi-hâzâ meselâ' (korpusun iki geçişi): sözü kalplerinde hastalık olanlar ve kâfirler, ardından 'men yeşâ'' / sözü inkâr edenler, ardından 'kesîran' + hasr 'ille'l-fâsiqîn'", 'not': 'kalıp eşi.'},
 {'bag': '22:54 → 2:26', 'kural': "okuma — 'ennehu'l-haqqu min rabb': 'rabbike' 2MS, ilim verilenler / 'rabbihim' 3MP, inananlar", 'not': 'kalıp eşi.'},
 {'bag': '33:53 → 2:26', 'kural': "okuma — lemma 'yestahyî': aynı ayette Peygamber / Allah (olumsuz, 'mine'l-haqq') / Allah (olumsuz, mesel vermekten) — aday 1041 ailesi, sûreler arası okuma notu", 'not': 'lemma eşi.'},
 {'bag': '13:25 → 2:27', 'kural': "okuma — esit2 BENZER 0,8862: ilk üç cümle aynı; 'lehumu'l-la'netu ve lehum sû'u'd-dâr' / 'humu'l-xâsirûn'", 'not': 'esit2 eşi.'},
 {'bag': '13:21 → 2:27', 'kural': "okuma — 'mâ emera'llâhu bihî en yûsal': 'yasılûne' (birleştirirler) / 'yaqta'ûne' (keserler)", 'not': 'kalıp eşi.'},
 {'bag': '22:66 → 2:28', 'kural': "okuma — harekesiz 'yumîtukum thumma yuhyîkum': 'ahyâkum' ile açılış, 'inne'l-insâne le-kefûr' ile kapanış / 'kuntum emvâten' hâli, 'ileyhi turja'ûn' ile kapanış", 'not': 'kalıp eşi.'},
 {'bag': '41:11 → 2:29', 'kural': "okuma — harekesiz 'thumma'stevâ ile's-semâ'' (korpusun iki geçişi): göğün duman hâli + söz / 'fe-sevvâhunne'", 'not': 'kalıp eşi.'},
 {'bag': '41:12 → 2:29', 'kural': "okuma — 'fe-qadâhunne seb'a semâvâtin fî yevmeyn' / 'fe-sevvâhunne seb'a semâvât' (süresiz); ikisi de ''alîm' ile biter", 'not': 'kalıp eşi.'},
 {'bag': '2:26 → 2:27', 'kural': "sûre içi — 'el-fâsiqîn' → 'ellezîne yenqudûne …' sıfat cümlesi, 'ulâ'ike humu'l-xâsirûn' ile kapanış", 'not': 'sûre içi eş.'},
 {'bag': '2:26 → 2:28', 'kural': "sûre içi — kök حيي iki anlam: 'yestahyî' (utanma) / 'ahyâ', 'yuhyî' (diriltme)", 'not': 'sûre içi eş.'},
 {'bag': '2:22 → 2:29', 'kural': "sûre içi — 'ellezî' + PERF 3MS + 'lekum' + 'el-ard' / 'es-semâ'': yeri döşek, göğü bina / yerdekileri yaratma, göğü yedi gök", 'not': 'sûre içi eş.'},
 {'bag': '2:21 → 2:29', 'kural': "sûre içi — kök خلق [1/6] ve [2/6]: 'xalaqakum' / 'xalaqa lekum mâ fi'l-ard'", 'not': 'sûre içi eş.'},
 # blok 30-33
 {'bag': '15:28 → 2:30', 'kural': "okuma — harekesiz 'qâle rabbuke li'l-melâ'ike' (korpusun üç geçişi): 'innî xâliqun beşeran min salsâl…' / 'innî câ'ilun fi'l-ardı xalîfeh'", 'not': 'kalıp eşi.'},
 {'bag': '38:71 → 2:30', 'kural': "okuma — harekesiz 'qâle rabbuke li'l-melâ'ike': 'innî xâliqun beşeran min tîn' / 'innî câ'ilun fi'l-ardı xalîfeh' ('xâliq' / 'câ'il', 'beşer' / 'xalîfe')", 'not': 'kalıp eşi.'},
 {'bag': '38:26 → 2:30', 'kural': "okuma — lemma 'xalîfe' + 'ce'ale' + 'fi'l-ard': 1P, adlı kişiye hitap / 1S, nekre, adsız", 'not': 'lemma eşi.'},
 {'bag': '12:96 → 2:30', 'kural': "okuma — 'innî a'lemu … mâ lâ ta'lemûn': basılan ayette adsız insan, araya 'mine'llâh' / Rab (aday 1041 ailesi, sûreler arası okuma notu)", 'not': 'kalıp eşi.'},
 {'bag': '66:3 → 2:31', 'kural': "okuma — lemma 'enbe'e' (korpusun üç ayeti okundu): 'men enbe'eke hâzâ' + ''alîm' / 'enbi'ûnî' emri", 'not': 'lemma eşi.'},
 {'bag': '12:96 → 2:33', 'kural': "okuma — harekesiz 'e-lem equl lekum innî a'lemu': ardından 'mine'llâhi mâ lâ ta'lemûn' / ardından 'ğaybe's-semâvâti ve'l-ard'", 'not': 'kalıp eşi.'},
 {'bag': '49:18 → 2:33', 'kural': "okuma — harekesiz 'ğaybe's-semâvâti ve'l-ard': lafız + IMPF 3MS 'ya'lemu' / 1S 'a'lemu'", 'not': 'kalıp eşi.'},
 {'bag': '2:23 → 2:31', 'kural': "sûre içi — harekesiz 'in kuntum sâdiqîn': meydan okuma, 2MP insanlara / 1S'nin emri, meleklere", 'not': 'sûre içi eş.'},
 {'bag': '2:30 → 2:33', 'kural': "sûre içi — 'innî a'lemu mâ lâ ta'lemûn' sözüne 'e-lem equl lekum innî a'lemu' ile geri dönüş", 'not': 'sûre içi eş.'},
 {'bag': '2:31 → 2:33', 'kural': "sûre içi — lemma 'enbe'e' üç geçiş: 'enbi'ûnî' (meleklere) / 'enbi'hum' (Âdem'e) / 'enbe'ehum' (Âdem haber verdi)", 'not': 'sûre içi eş.'},
 {'bag': '2:29 → 2:32', 'kural': "sûre içi — esmâ ''alîm' iki ayette: 3MS 'huve' haberi / 2MS 'ente' haberi + 'el-hakîm'", 'not': 'sûre içi eş.'},
 # blok 34-39
 {'bag': '20:116 → 2:34', 'kural': "okuma — harekesiz 've iz qulnâ li'l-melâ'ikati'scudû li-âdeme fe-secedû' (korpusun dört geçişi): 'illâ iblîse ebâ' / 'illâ iblîse ebâ ve'stekbera ve kâne mine'l-kâfirîn'", 'not': 'kalıp eşi.'},
 {'bag': '17:61 → 2:34', 'kural': "okuma — aynı kalıp: ardından İblîs'in sözü 'e-escudu li-men xalaqte tînâ' / ardından üç PERF", 'not': 'kalıp eşi.'},
 {'bag': '18:50 → 2:34', 'kural': "okuma — aynı kalıp: 'kâne mine'l-cinni fe-feseqa 'an emri rabbih' / 'kâne mine'l-kâfirîn'", 'not': 'kalıp eşi.'},
 {'bag': '38:74 → 2:34', 'kural': "okuma — 'illâ iblîse'stekbera ve kâne mine'l-kâfirîn': önekli 've'stekbera' yalnız burada, önünde 'ebâ'", 'not': 'kalıp eşi.'},
 {'bag': '20:117 → 2:35', 'kural': "okuma — 1P 'qulnâ' + 'yâ âdemu' + 'zevc' + 'el-cenne': düşmana dair uyarı / ağaca dair yasak", 'not': 'kalıp eşi.'},
 {'bag': '20:120 → 2:35', 'kural': "okuma — lemma 'şecera': şeytanın sözünde 'şeceratu'l-xuld' / 1P'nin yasağında 'hâzihi'ş-şecera'", 'not': 'lemma eşi.'},
 {'bag': '20:117 → 2:36', 'kural': "okuma — lemma 'exrace': 'fe-lâ yuxricannekumâ mine'l-cenne' uyarısı / 'fe-exracehumâ' gerçekleşme", 'not': 'lemma eşi.'},
 {'bag': '20:123 → 2:36', 'kural': "okuma — 'ihbitâ … ba'dukum li-ba'din 'aduvv' ikil emir / 'ihbitû ba'dukum li-ba'din 'aduvv' çoğul emir", 'not': 'kalıp eşi.'},
 {'bag': '20:123 → 2:38', 'kural': "okuma — 'fe-immâ ye'tiyennekum minnî hudan fe-men(i't)-tebi'a hudâye': 3MS 'qâle', 'lâ yedillu ve lâ yeşqâ' / 1P 'qulnâ', 'lâ xavfun 'aleyhim ve lâ hum yahzenûn'", 'not': 'kalıp eşi.'},
 {'bag': '46:13 → 2:38', 'kural': "okuma — harekesiz 'fe-lâ xavfun 'aleyhim ve lâ hum yahzenûn': 'qâlû rabbuna'llâhu thumme'staqâmû' / 'tebi'a hudâye'", 'not': 'kalıp eşi.'},
 {'bag': '64:10 → 2:39', 'kural': "okuma — harekesiz 've'llezîne keferû ve kezzebû bi-âyâtinâ ulâ'ike ashâbu'n-nâr' (korpusun iki geçişi): 'xâlidîne fîhâ' hâl / 'hum fîhâ xâlidûn' isim cümlesi", 'not': 'kalıp eşi.'},
 {'bag': '2:22 → 2:36', 'kural': "sûre içi — lemma 'exrace': 3MS yaratan, ürünleri / şeytân, Âdem ve eşini (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '2:36 → 2:38', 'kural': "sûre içi — 'ihbitû' iki kez: 'ba'dukum li-ba'din 'aduvv' / 'minhâ cemî'an'", 'not': 'sûre içi eş.'},
 {'bag': '2:25 → 2:39', 'kural': "sûre içi — 'hum fîhâ xâlidûn': bahçeler / ateş (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '2:38 → 2:39', 'kural': "sûre içi — iki kol: yol göstericiye uyanlar / inkâr edip yalanlayanlar (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 # blok 40-46
 {'bag': '20:80 → 2:40', 'kural': "okuma — harekesiz 'yâ benî isrâ'îl': konuşan 1P 'enceynâkum' / konuşan 1S 'en'amtu'", 'not': 'kalıp eşi.'},
 {'bag': '61:6 → 2:40', 'kural': "okuma — harekesiz 'yâ benî isrâ'îl': söz 'qâle 'îsâ'bnu meryem' ile / söz fiilsiz 1S hitap", 'not': 'kalıp eşi.'},
 {'bag': '16:51 → 2:40', 'kural': "okuma — 'fe-iyyâye fe'rhebûn' (önek kesilmiş 'fe'rhebûn' korpusta 2): 'qâle'llâh' ile açılan söz / adsız 1S hitap", 'not': 'kalıp eşi.'},
 {'bag': '23:52 → 2:41', 'kural': "okuma — önek kesilmiş 'fe'ttequn': 've ene rabbukum' / 've iyyâye'", 'not': 'kalıp eşi.'},
 {'bag': '2:22 → 2:42', 'kural': "sûre içi — 've entum ta'lemûn': 'lâ tec'alû li'llâhi endâden' / 'lâ telbisû … ve tektumû'", 'not': 'sûre içi eş.'},
 {'bag': '24:56 → 2:43', 'kural': "okuma — harekesiz 've aqîmu's-salâte ve âtu'z-zakâte': devamı 've atî'u'r-resûl' / 'verke'û ma'a'r-râki'în'", 'not': 'kalıp eşi.'},
 {'bag': '22:77 → 2:43', 'kural': "okuma — fiil lemması (kök ركع): 'irke'û ve'scudû' / 'irke'û ma'a'r-râki'în'", 'not': 'lemma eşi.'},
 {'bag': '59:19 → 2:44', 'kural': "okuma — lemma 'nesiye' + 'enfus': 'nesu'llâhe fe-ensâhum enfusehum' / 'tensevne enfusekum'", 'not': 'lemma eşi.'},
 {'bag': '23:2 → 2:45', 'kural': "okuma — lemma 'xâşi'' + 'salât': 'fî salâtihim xâşi'ûn' / 'bi's-sabri ve's-salâh … illâ 'ale'l-xâşi'în'", 'not': 'lemma eşi.'},
 {'bag': '11:29 → 2:46', 'kural': "okuma — lemma 'mulâqî': 'innehum mulâqû rabbihim' ('ve yâ qavmi' sözünde) / 'ennehum mulâqû rabbihim' (ilgi cümlesinde)", 'not': 'lemma eşi.'},
 {'bag': '2:40 → 2:41', 'kural': "sûre içi — 've iyyâye fe'rhebûn' / 've iyyâye fe'ttequn': ardışık iki kapanış", 'not': 'sûre içi eş.'},
 {'bag': '2:45 → 2:46', 'kural': "sûre içi — 'el-xâşi'în' / 'ellezîne yezunnûne': ilgi cümlesi niteleme", 'not': 'sûre içi eş.'},
 # blok 47-53
 {'bag': '2:40 → 2:47', 'kural': "sûre içi — 'yâ benî isrâ'île'zkurû ni'metiye'lletî en'amtu 'aleykum': devamı ahit ve korku / üstün kılınma", 'not': 'sûre içi eş.'},
 {'bag': '45:16 → 2:47', 'kural': "okuma — lemma 'feddale' + ''ale'l-'âlemîn': 1P 'feddalnâhum' anlatı / 1S 'feddaltukum' hitap", 'not': 'lemma eşi.'},
 {'bag': '82:19 → 2:48', 'kural': "okuma — 'yevm' + 'nefs … nefs … şey'' (ölçüm xref): 'lâ temliku … li-' / 'lâ teczî … 'an'", 'not': 'kalıp eşi.'},
 {'bag': '74:48 → 2:48', 'kural': "okuma — lemma 'şefâ'a': 'fe-mâ tenfe'uhum' (fayda yok) / 'lâ yuqbelu' (kabul yok)", 'not': 'lemma eşi.'},
 {'bag': '14:6 → 2:49', 'kural': "okuma — harekesiz 'yesûmûnekum sû'e'l-'azâb' ve 've fî zâlikum belâ'un min rabbikum 'azîm': 'qâle mûsâ' sözünde 3MS 'encâkum' / 1P 'necceynâkum' anlatısı", 'not': 'kalıp eşi.'},
 {'bag': '28:4 → 2:49', 'kural': "okuma — lemma 'yuzebbihu' + 'yestahyî' (korpusun üç geçişi): özne adlı 'fir'avn' 3MS / 'âl' 3MP", 'not': 'lemma eşi.'},
 {'bag': '2:26 → 2:49', 'kural': "sûre içi — lemma 'yestahyî': özne Allah, utanma / özne Firavun ailesi, sağ bırakma (aday 1041, kayıt)", 'not': 'sûre içi eş.'},
 {'bag': '33:53 → 2:49', 'kural': "okuma — lemma 'yestahyî': aynı ayette iki özne, utanma / sağ bırakma", 'not': 'lemma eşi.'},
 {'bag': '26:63 → 2:50', 'kural': "okuma — denizin yarılması: 'fe'nfeleqa' + 'kullu firqin' (kök فرق ad) / 'feraqnâ bikumu'l-bahr'", 'not': 'kök eşi.'},
 {'bag': '26:66 → 2:50', 'kural': "okuma — lemma 'ağraqa': 'el-âxarîn' adsız / 'âle fir'avn' adlı", 'not': 'lemma eşi.'},
 {'bag': '2:49 → 2:50', 'kural': "sûre içi — kök نجو [1/2] / [2/2]: 'necceynâkum' II. bab / 'enceynâkum' IV. bab", 'not': 'sûre içi eş.'},
 {'bag': '20:80 → 2:51', 'kural': "okuma — lemma 'vâ'ade': 'vâ'adnâkum cânibe't-tûr' (2MP, yer) / 'vâ'adnâ mûsâ erba'îne leyle' (Mûsâ, süre)", 'not': 'lemma eşi.'},
 {'bag': '20:88 → 2:51', 'kural': "okuma — lemma ''icl': çıkaranı ayette adsız, 'qâlû hâzâ ilâhukum' / 'ittexaztumu'l-'icl' 2MP", 'not': 'lemma eşi.'},
 {'bag': '2:51 → 2:52', 'kural': "sûre içi — ardışık 'thumme': 'ittexaztum … ve entum zâlimûn' / ''afevnâ 'ankum' (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 {'bag': '21:48 → 2:53', 'kural': "okuma — lemma 'furqân' + 'âteynâ mûsâ': 've hârûne'l-furqân' / ''l-kitâbe ve'l-furqân'", 'not': 'lemma eşi.'},
 {'bag': '43:10 → 2:53', 'kural': "okuma — harekesiz 'le'allekum tehtedûn': yerdeki yollar / kitap ve furqân", 'not': 'kalıp eşi.'},
 {'bag': '2:50 → 2:53', 'kural': "sûre içi — kök فرق: 'feraqnâ' (denizi yarma) / 'el-furqân'", 'not': 'sûre içi eş.'},
 # blok 54-59
 {'bag': '61:5 → 2:54', 'kural': "okuma — harekesiz 've iz qâle mûsâ li-qavmihî yâ qavmi': soru 'lime tu'zûnenî' / suçun adlanması ve tevbe emri", 'not': 'kalıp eşi.'},
 {'bag': '59:24 → 2:54', 'kural': "okuma — lemma 'bâri'': belirli, esmâ dizisinde / iyelikli 'bâri'ikum' ×2", 'not': 'lemma eşi.'},
 {'bag': '2:37 → 2:54', 'kural': "sûre içi — 'fe-tâbe 'aleyh / 'aleykum' + 'innehû huve't-tevvâbu'r-rahîm' (korpusun iki geçişi): Âdem / kavim", 'not': 'sûre içi eş.'},
 {'bag': '2:51 → 2:54', 'kural': "sûre içi — 'ittexaztumu'l-'icl' / 'bi'ttixâzikumu'l-'icl': anlatıda edim, Mûsâ'nın sözünde suç", 'not': 'sûre içi eş.'},
 {'bag': '51:44 → 2:55', 'kural': "okuma — 'fe-axazethumu's-sâ'iqatu ve hum yenzurûn' 3MP / 'fe-exazetkumu's-sâ'iqatu ve entum tenzurûn' 2MP", 'not': 'kalıp eşi.'},
 {'bag': '2:50 → 2:55', 'kural': "sûre içi — 've entum tenzurûn': kurtuluşa / yıldırıma bakış", 'not': 'sûre içi eş.'},
 {'bag': '2:52 → 2:56', 'kural': "sûre içi — 'thumme' + PERF 1P + 'min ba'di' + 'le'allekum teşkurûn': af / diriltme", 'not': 'sûre içi eş.'},
 {'bag': '25:25 → 2:57', 'kural': "okuma — lemma 'ğamâm': gök bulutla yarılıyor / bulut gölge", 'not': 'lemma eşi.'},
 {'bag': '20:80 → 2:57', 'kural': "okuma — lemma 'menn' + 'selvâ': 've nezzelnâ' (II. bab) / 've enzelnâ' (IV. bab)", 'not': 'lemma eşi.'},
 {'bag': '20:81 → 2:57', 'kural': "okuma — harekesiz 'kulû min tayyibâti mâ razaqnâkum': ardından 'lâ tatğav' uyarısı / ardından 'mâ zalemûnâ'", 'not': 'kalıp eşi.'},
 {'bag': '2:35 → 2:58', 'kural': "sûre içi — 'kulâ minhâ rağaden haysu şi'tumâ' (ikil) / 'kulû minhâ haysu şi'tum rağadâ' (çoğul); kök رغد [2/2]", 'not': 'sûre içi eş.'},
 {'bag': '29:34 → 2:58', 'kural': "okuma — lemma 'qarye' + işaret 'hâzihi': azap indirilecek halk / girilecek yer", 'not': 'lemma eşi.'},
 {'bag': '29:34 → 2:59', 'kural': "okuma — harekesiz 'riczen mine's-semâ'i bimâ kânû yefsuqûn' (korpusun iki geçişi): 'innâ munzilûne' / 'fe-enzelnâ'", 'not': 'kalıp eşi.'},
 {'bag': '14:28 → 2:59', 'kural': "okuma — lemma 'beddele': nimet değiştiriliyor / söz değiştiriliyor", 'not': 'lemma eşi.'},
 {'bag': '2:58 → 2:59', 'kural': "sûre içi — 'qûlû hittah' / 'qavlen ğayra'llezî qîle lehum' (aday 1039, okuma)", 'not': 'sûre içi eş.'},
 # blok 60-61
 {'bag': '26:63 → 2:60', 'kural': "okuma — harekesiz 'idrib bi-'asâk': denize vuruş, yarılma / taşa vuruş, fışkırma", 'not': 'kalıp eşi.'},
 {'bag': '2:24 → 2:60', 'kural': "sûre içi — kök حجر: 'el-hicâra' (ateşin yakıtı) / 'el-hacer' (su çıkan taş)", 'not': 'sûre içi eş.'},
 {'bag': '36:73 → 2:60', 'kural': "okuma — lemma 'meşrab': çoğul 'meşârib' / 'kullu unâsin meşrabehum'", 'not': 'lemma eşi.'},
 {'bag': '52:19 → 2:60', 'kural': "okuma — harekesiz 'kulû ve'şrabû': 'henî'en bimâ kuntum ta'melûn' / 'min rizqi'llâh'", 'not': 'kalıp eşi.'},
 {'bag': '29:36 → 2:60', 'kural': "okuma — harekesiz 've lâ ta'sev fi'l-ardı mufsidîn': Şu'ayb'ın sözünde / 1P sözünde", 'not': 'kalıp eşi.'},
 {'bag': '2:55 → 2:61', 'kural': "sûre içi — 've iz qultum yâ mûsâ len' + IMPF 1P: 'nu'mine' / 'nasbira' (ölçüm nakarat3)", 'not': 'sûre içi eş.'},
 {'bag': '2:36 → 2:61', 'kural': "sûre içi — kök هبط 'ihbitû': bahçeden iniş / 'ihbitû misran'", 'not': 'sûre içi eş.'},
 {'bag': '47:38 → 2:61', 'kural': "okuma — lemma 'istebdele': 'yestebdil qavmen ğayrakum' (3MS) / 'e-testebdilûne' (2MP)", 'not': 'lemma eşi.'},
 {'bag': '12:99 → 2:61', 'kural': "okuma — lemma 'misr': tenvinsiz 'udxulû misra' / tenvinli 'ihbitû misran'", 'not': 'lemma eşi.'},
 {'bag': '68:43 → 2:61', 'kural': "okuma — lemma 'zille': 'terhequhum zille' / 'duribet 'aleyhimu'z-zille'", 'not': 'lemma eşi.'},
 {'bag': '2:60 → 2:61', 'kural': "sûre içi — 'asâ': kök عصو (değnek) / kök عصي (isyan); su / yiyecek sahneleri art arda", 'not': 'sûre içi eş.'},
 # blok 62-66
 {'bag': '22:17 → 2:62', 'kural': "okuma — 'inne'llezîne âmenû ve'llezîne hâdû' + Sâbiîler ve Hıristiyanlar: altı grup, yüklem 'yefsilu beynehum' / dört grup, yüklem 'men âmene … fe-lehum ecruhum'", 'not': 'kalıp eşi.'},
 {'bag': '9:18 → 2:62', 'kural': "okuma — harekesiz 'men âmene bi'llâhi ve'l-yevmi'l-âxir': mescitleri imar / ödül", 'not': 'kalıp eşi.'},
 {'bag': '2:38 → 2:62', 'kural': "sûre içi — 'lâ xavfun 'aleyhim ve lâ hum yahzenûn': 'fe' ile (yol göstericiye uyanlar) / 've' ile (iman edip iyi iş yapanlar)", 'not': 'sûre içi eş.'},
 {'bag': '19:52 → 2:63', 'kural': "okuma — lemma 'tûr': 'cânibi't-tûri'l-eymen' / 'fevqakumu't-tûr'", 'not': 'lemma eşi.'},
 {'bag': '20:80 → 2:63', 'kural': "okuma — lemma 'tûr': 'cânibe't-tûri'l-eymen' (vaat) / 'fevqakumu't-tûr' (söz alma)", 'not': 'lemma eşi.'},
 {'bag': '2:21 → 2:63', 'kural': "sûre içi — 'le'allekum tetteqûn': kulluk emri / verileni tutma emri", 'not': 'sûre içi eş.'},
 {'bag': '2:52 → 2:64', 'kural': "sûre içi — 'thumme … min ba'di zâlik': 1P'nin affı / 2MP'nin yüz çevirmesi (ölçüm nakarat3)", 'not': 'sûre içi eş.'},
 {'bag': '24:10 → 2:64', 'kural': "okuma — 'lev lâ fadlu'llâhi 'aleykum ve rahmetuhû': cevapsız / 'lekuntum mine'l-xâsirîn'", 'not': 'kalıp eşi.'},
 {'bag': '2:27 → 2:64', 'kural': "sûre içi — lemma 'xâsir': 'ulâ'ike humu'l-xâsirûn' / 'lekuntum mine'l-xâsirîn'", 'not': 'sûre içi eş.'},
 {'bag': '16:124 → 2:65', 'kural': "okuma — lemma 'sebt': 'ce'ile's-sebt' / 'i'tedev fi's-sebt'", 'not': 'lemma eşi.'},
 {'bag': '67:4 → 2:65', 'kural': "okuma — lemma 'xâsi'': bakış için / maymunlar için", 'not': 'lemma eşi.'},
 {'bag': '2:61 → 2:65', 'kural': "sûre içi — kök عدو: 'kânû ya'tedûn' / 'i'tedev'", 'not': 'sûre içi eş.'},
 {'bag': '79:25 → 2:66', 'kural': "okuma — lemma 'nekâl': 'exazehu'llâhu nekâle'l-âxirati ve'l-ûlâ' / 'ce'alnâhâ nekâlen'", 'not': 'lemma eşi.'},
 {'bag': '10:57 → 2:66', 'kural': "okuma — lemma 'maw'iza': 'min rabbikum' (insanlara) / 'li'l-muttaqîn'", 'not': 'lemma eşi.'},
 # blok 67-70
 {'bag': '2:54 → 2:67', 'kural': "sûre içi — 'iz qâle mûsâ li-qavmihî': 'yâ qavmi innekum zalemtum' / 'inne'llâhe ye'murukum'", 'not': 'sûre içi eş.'},
 {'bag': '37:102 → 2:67', 'kural': "okuma — lemma 'zebaha': 'ennî ezbehuk' (1S, rüya) / 'en tezbehû baqara' (2MP, emir)", 'not': 'lemma eşi.'},
 {'bag': '18:56 → 2:67', 'kural': "okuma — lemma 'huzuw' + 'ittexaza': âyetleri alaya almak / 'e-tettexizunâ huzuwâ'", 'not': 'lemma eşi.'},
 {'bag': '11:46 → 2:67', 'kural': "okuma — 'en + kâne + mine'l-câhilîn': 'e'izuke' (kök وعظ) / 'e'ûzu bi'llâh' (kök عوذ)", 'not': 'kalıp eşi.'},
 {'bag': '12:43 → 2:67', 'kural': "okuma — lemma 'baqara': rüyada yedi semiz inek / boğazlanacak inek", 'not': 'lemma eşi.'},
 {'bag': '2:49 → 2:67', 'kural': "sûre içi — kök ذبح: 'yuzebbihûne ebnâ'ekum' / 'en tezbehû baqara'", 'not': 'sûre içi eş.'},
 {'bag': '43:49 → 2:68', 'kural': "okuma — önek kesilmiş 'ud'u lenâ rabbeke': 'yâ eyyuhe's-sâhir' + 'innenâ le-muhtedûn' / Mûsâ'nın kavmi", 'not': 'kalıp eşi.'},
 {'bag': '2:61 → 2:68', 'kural': "sûre içi — 'ud'u lenâ rabbeke': yiyecek isteği / ineğin ne olduğu", 'not': 'sûre içi eş.'},
 {'bag': '37:102 → 2:68', 'kural': "okuma — 'if'al mâ tu'mer' (2MS) / 'fef'alû mâ tu'merûn' (2MP)", 'not': 'kalıp eşi.'},
 {'bag': '2:68 → 2:69', 'kural': "sûre içi — 'qâlû'd'u lenâ rabbeke yubeyyin lenâ mâ …' + 'qâle innehû yaqûlu innehâ baqara': 'mâ hiye' / 'mâ levnuhâ'", 'not': 'sûre içi eş.'},
 {'bag': '15:16 → 2:69', 'kural': "okuma — lemma 'nâzır': 'zeyyennâhâ li'n-nâzırîn' (gök) / 'tesurru'n-nâzırîn' (inek)", 'not': 'lemma eşi.'},
 {'bag': '2:68 → 2:70', 'kural': "sûre içi — harfi harfine aynı açılış 'qâlû'd'u lenâ rabbeke yubeyyin lenâ mâ hiy': cevaplı / cevapsız", 'not': 'sûre içi eş.'},
 {'bag': '43:49 → 2:70', 'kural': "okuma — 'innenâ le-muhtedûn' / 'innâ in şâ'e'llâhu le-muhtedûn'", 'not': 'kalıp eşi.'},
 {'bag': '37:102 → 2:70', 'kural': "okuma — harekesiz 'in şâ'e'llâh': 'mine's-sâbirîn' / 'le-muhtedûn'", 'not': 'kalıp eşi.'},
 # blok 71-74
 {'bag': '2:68 → 2:71', 'kural': "sûre içi — 'qâle innehû yaqûlu innehâ baqaratun lâ': 'lâ fâridun ve lâ bikr' (yaş) / 'lâ zelûl' (iş)", 'not': 'sûre içi eş.'},
 {'bag': '67:15 → 2:71', 'kural': "okuma — lemma 'zelûl': yer boyun eğer kılındı / inek 'lâ zelûl'", 'not': 'lemma eşi.'},
 {'bag': '30:9 → 2:71', 'kural': "okuma — lemma 'esâra' + 'el-ard': 've esârû'l-arda' / 'tuthîru'l-arda' (olumsuz)", 'not': 'lemma eşi.'},
 {'bag': '12:51 → 2:71', 'kural': "okuma — 'el-âne' + 'el-haqq': 'hashasa'l-haqq' / 'ci'te bi'l-haqq'", 'not': 'lemma eşi.'},
 {'bag': '2:54 → 2:72', 'kural': "sûre içi — lemma dizisi 'qatele + nefs': 'faqtulû enfusekum' (emir) / 'qataltum nefsen' (haber)", 'not': 'sûre içi eş.'},
 {'bag': '28:19 → 2:72', 'kural': "okuma — lemma dizisi 'qatele + nefs': 'qatelte nefsen' (2MS) / 'qataltum nefsen' (2MP)", 'not': 'lemma eşi.'},
 {'bag': '2:33 → 2:72', 'kural': "sûre içi — önek kesilmiş 'mâ kuntum tektumûn': 'tubdûne' / 'muxric'", 'not': 'sûre içi eş.'},
 {'bag': '2:60 → 2:73', 'kural': "sûre içi — lemma 'darabe' + 'bi': 'idrib bi-'asâke'l-hacer' / 'idribûhu bi-ba'dıhâ'", 'not': 'sûre içi eş.'},
 {'bag': '2:28 → 2:73', 'kural': "sûre içi — lemma 'ahyâ': 'fe-ahyâkum … thumme yuhyîkum' / 'kezâlike yuhyi'llâhu'l-mevtâ'", 'not': 'sûre içi eş.'},
 {'bag': '40:81 → 2:73', 'kural': "okuma — önek kesilmiş 'yurîkum âyâtihî': inkâr sorusu / 'le'allekum ta'qilûn'", 'not': 'kalıp eşi.'},
 {'bag': '57:16 → 2:74', 'kural': "okuma — lemma 'qasat' + 'qulûb': 'fe-qasat qulûbuhum' (3MP) / 'thumme qasat qulûbukum' (2MP)", 'not': 'lemma eşi.'},
 {'bag': '2:64 → 2:74', 'kural': "sûre içi — 'thumme … min ba'di zâlike': 'tevelleytum' / 'qasat qulûbukum'", 'not': 'sûre içi eş.'},
 {'bag': '2:52 → 2:74', 'kural': "sûre içi — 'thumme … min ba'di zâlike': ''afevnâ 'ankum' / 'qasat qulûbukum'", 'not': 'sûre içi eş.'},
 {'bag': '2:24 → 2:74', 'kural': "sûre içi — lemma 'hicâra': ateşin yakıtı / kalplerin benzetildiği taş", 'not': 'sûre içi eş.'},
 {'bag': '2:60 → 2:74', 'kural': "sûre içi — kök فجر, taştan su: 'fe'nfecerat' / 'yetefecceru'", 'not': 'sûre içi eş.'},
 {'bag': '59:21 → 2:74', 'kural': "okuma — önek kesilmiş 'min xaşyeti'llâh': dağ 'mutesaddi'' / taş 'yeşşaqqaqu', 'yahbitu'", 'not': 'kalıp eşi.'},
 {'bag': '2:36 → 2:74', 'kural': "sûre içi — lemma 'habata': 'ihbitû' (inin) / taş 'yahbitu'", 'not': 'sûre içi eş.'},
 # blok 75-79
 {'bag': '9:6 → 2:75', 'kural': "okuma — lemma dizisi 'semi'a + kelâm + Allah': işitsin diye eman / işitip değiştirme", 'not': 'lemma eşi.'},
 {'bag': '2:44 → 2:76', 'kural': "sûre içi — harekesiz 'e-fe-lâ ta'qilûn': İsrâiloğullarına hitap / kendi aralarındaki söz", 'not': 'sûre içi eş.'},
 {'bag': '16:23 → 2:77', 'kural': "okuma — harekesiz 'enna'llâhe ya'lemu mâ yusirrûne ve mâ yu'linûn': 'lâ cerame' hükmü / soru", 'not': 'kalıp eşi.'},
 {'bag': '62:2 → 2:78', 'kural': "okuma — lemma 'ummiy': kitap öğretilen ümmîler / kitabı bilmeyen ümmîler", 'not': 'lemma eşi.'},
 {'bag': '57:14 → 2:78', 'kural': "okuma — lemma 'umniyye': 'ğarratkumu'l-emâniyy' / 'illâ emâniyy'", 'not': 'lemma eşi.'},
 {'bag': '45:24 → 2:78', 'kural': "okuma — harekesiz 'in hum illâ yazunnûn': 'mâ lehum bi-zâlike min 'ilm' / 'lâ ya'lemûne'l-kitâb'", 'not': 'kalıp eşi.'},
 {'bag': '2:46 → 2:78', 'kural': "sûre içi — lemma 'zanne': Rablerine kavuşacaklarını bilenler / yalnız zannedenler", 'not': 'sûre içi eş.'},
 {'bag': '19:37 → 2:79', 'kural': "okuma — önek kesilmiş 'fe-veylun li'llezîne': 'keferû' / 'yektubûne'l-kitâbe bi-eydîhim'", 'not': 'kalıp eşi.'},
 {'bag': '2:41 → 2:79', 'kural': "sûre içi — harekesiz 'semenen qalîlâ': 'lâ teşterû bi-âyâtî' (yasak) / 'li-yeşterû bihî' (yazılan kitapla)", 'not': 'sûre içi eş.'},
 {'bag': '9:9 → 2:79', 'kural': "okuma — harekesiz 'semenen qalîlâ': 'işteraw bi-âyâti'llâh' / 'li-yeşterû bihî'", 'not': 'kalıp eşi.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_bakara', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in BAKARA]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_bakara'] = BAKARA
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_bakara', len(BAKARA), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_bakara', len(BAGLAR['AS_bakara']))
