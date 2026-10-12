# -*- coding: utf-8 -*-
"""aday_ekle_42_shura.py — sûre 42 (Şûrâ) adayları (AX_shura) ve okuma bağları (AS_shura).

BLOK BAŞI KAYIT: her blok sonunda bu dosyaya o bloğun adayları ve bağları EKLENİR ve betik
yeniden koşulur. Set bütünüyle yeniden yazılır (idempotent): iki kez koşmak çift kayıt üretmez.
Numaralar havuzun sonundan devam eder (1041'den); betik sıranın kopmadığını doğrular.
"""
import json

SHURA = [
 {
  "no": 1041,
  "aday": "AYNI KELİMENİN ALLAH VE İNSAN İÇİN KULLANILMASI (test edilecek, iddia değil): sûre 42'de bir kök önce Allah'ın sıfatı/fiili, birkaç ayet sonra insanın sıfatı/fiili olarak geliyor — şekûr 42:23 (Allah) → 42:33 (sabreden-şükreden insan); ğafr 42:5 / 42:23 (Allah) → 42:37 'hum yağfirûn' (insan); afv 42:25, 30, 34 (Allah 'ya'fû') → 42:40 'fe-men afâ' (insan); istecâbe 42:26 'yestecîbu' (fâili iki okumaya açık) → 42:38 'istecâbû li-rabbihim' (insan). Ters yönde aynı yapı insan grupları arasında: şera'a 42:13 (Allah) → 42:21 (ortaklar); işfâk 42:18 (iman edenler) → 42:22 (zalimler).",
  "olculen": {
   "kok_konumlari_sure42_morph": {
    "شكر": "42:23, 42:33",
    "غفر": "42:5 (×2), 42:23, 42:37, 42:43",
    "عفو": "42:25, 42:30, 42:34, 42:40",
    "جوب": "42:16, 42:26, 42:38, 42:47",
    "شرع": "42:13, 42:21",
    "شفق": "42:18, 42:22"
   },
   "esma_kayit_kararlari": "42:23 şekûr ilâhî · 42:33 şekûr değil (blok 31-40)"
  },
  "test": "korpus sonunda (tam okuma bitince): esma_kayit'te 'ilahi' kararı verilmiş her esmâ kökü için aynı sûrede aynı kökün insan fâil/sıfatı olarak geçtiği (okuma kaydı) sûre oranı; sûre 42'nin oranı ile uzunluk eşli sûrelerin oranı karşılaştırılır (permütasyon). Sıfır hipotez: sûre 42 farklı değil. Gönderge ayrımı (Allah / insan) okuma kararıdır; ölçüm yalnız kök konumlarını verir.",
  "durum": "AÇIK — kayıt; okuma sırasında test edilmez",
  "oncelik": "P3",
  "kaynak": "sûre 42 okuması, blok 31-40 (2026-10-12)",
  "etiket": "okuma gözlemi; dört kök, tek sûre — genelleme yok, KAPATILAMAZ. 42:26 'yestecîbu'nun fâili iki okumaya açık (Allah / iman edenler); 42:43 ve 42:47 henüz okunmadı"
 },
]

BAGLAR = {"AS_shura": [
 {'bag': '40:1 · 41:1 → 42:1', 'kural': "esit2 TAM — 'Hâ Mîm' (ölçüm); okundu", 'not': 'Hâ Mîm ailesi.'},
 {'bag': '41:43 → 42:3', 'kural': "okuma — 'leke … li'r-rusuli min qablik' (edilgen, adsız) / 'ileyke ve ile'llezîne min qablik' (fâil Allah); aday 1040 alanında kayıt, test yok", 'not': 'sana ve öncekilere.'},
 {'bag': '39:65 → 42:3', 'kural': "metin sayımı 've ile'llezîne min qablik' 2 ayet; okundu — edilgen / etken", 'not': 'öncekilere vahiy.'},
 {'bag': '39:1 · 27:9 → 42:3', 'kural': "metin sayımı 'allâhu'l-azîzu'l-hakîm' 7 ayet; okundu", 'not': 'Azîz, Hakîm.'},
 {'bag': '14:2 · 34:1 → 42:4', 'kural': "metin sayımı 'lehû mâ fi's-semâvâti ve mâ fi'l-ard' 15 ayet; okundu", 'not': 'göklerdekiler ve yerdekiler.'},
 {'bag': '19:90 → 42:5', 'kural': "metin sayımı 'tekâdu's-semâvâtu yetefattarne' 2 ayet; okundu — 'minhu' / 'min fevqihinne'", 'not': 'göklerin çatlaması.'},
 {'bag': '40:7 → 42:5', 'kural': "metin sayımı 'yusabbihûne bi-hamdi rabbihim' 3 ayet + 'yesteğfirûn' 2 ayet; okundu — iman edenler için / yerdekiler için; aday 1040 alanı (39:75 → 40:7 → 42:5), test yok", 'not': 'tesbih ve istiğfar.'},
 {'bag': '39:3 → 42:6', 'kural': "metin sayımı 'ittehazû min dûnihî evliyâ'' 3 ayet; okundu", 'not': 'dost edinenler.'},
 {'bag': '39:41 → 42:6', 'kural': "metin sayımı 've mâ ente aleyhim bi-vekîl' 3 ayet; okundu", 'not': 'vekil değilsin.'},
 {'bag': '41:3 → 42:7', 'kural': "metin sayımı 'qur'ânen arabiyyâ' 6 ayet; okundu; aday 1040 alanında kayıt", 'not': "Arapça Kur'an."},
 {'bag': '16:93 → 42:8', 'kural': "metin sayımı 'ummeten vâhide' 9 ayet; okundu — 'le-cealekum' (2MP) / 'le-cealehum' (3MP)", 'not': 'tek ümmet.'},
 {'bag': '29:22 → 42:8', 'kural': "metin sayımı 'min veliyyin ve lâ nasîr' 7 ayet; okundu", 'not': 'dost ve yardımcı yok.'},
 {'bag': '42:6 → 42:9', 'kural': "okuma — 'ittehazû min dûnihî evliyâ'' sûre içi ×2; 42:9'da 'el-veliyy' Allah", 'not': 'dostlar / Dost.'},
 {'bag': '22:6 → 42:9', 'kural': "metin sayımı 'yuhyi'l-mevtâ' 4 ayet; okundu", 'not': 'ölüleri diriltir.'},
 {'bag': '11:88 → 42:10', 'kural': "metin sayımı 'aleyhi tevekkeltu ve ileyhi unîb' 2 ayet; okundu — Şuayb / adsız 1S", 'not': 'dayanma ve yönelme.'},
 {'bag': '39:3 → 42:10', 'kural': "okuma — 'ittehazû … evliyâ'' + 'yahkumu … yahtelifûn' tek ayette; 42:6/9 + 42:10; KAPATILAMAZ", 'not': 'ihtilafın hükmü.'},
 {'bag': '42:5 → 42:11', 'kural': "kök ikilemesi فطر [2/2] — 'yetefattarne' / 'fâtır'", 'not': 'çatlama / yaratma.'},
 {'bag': '16:72 · 30:21 → 42:11', 'kural': "metin sayımı 'min enfusikum ezvâcâ' 3 ayet; okundu", 'not': 'kendinizden eşler.'},
 {'bag': '40:56 · 17:1 → 42:11', 'kural': "metin sayımı 'es-semî'u'l-basîr' 4 ayet; okundu", 'not': 'işiten, gören.'},
 {'bag': '39:63 → 42:12', 'kural': "metin sayımı 'lehû meqâlîdu's-semâvâti ve'l-ard' 2 ayet; okundu", 'not': 'göklerin ve yerin anahtarları.'},
 {'bag': '39:52 · 13:26 → 42:12', 'kural': "metin sayımı 'yebsutu'r-rizqa li-men yeşâu ve yaqdir' 6 ayet; okundu", 'not': 'rızkı genişletme / daraltma.'},
 {'bag': '33:7 → 42:13', 'kural': "metin sayımı 'ibrâhîme ve mûsâ ve îsâ' 2 ayet; okundu — aynı beş kişi aynı sırada (misak / din)", 'not': 'beş peygamber.'},
 {'bag': '41:5 → 42:13', 'kural': "okuma — 'mimmâ ted'ûnâ ileyhi' (inkârcılar) / 'mâ ted'ûhum ileyh' (anlatıcı)", 'not': 'çağırılan şey.'},
 {'bag': '42:10 → 42:13', 'kural': "kök ikilemesi نوب [2/2] — 'unîb' / 'men yunîb'", 'not': 'yönelme.'},
 {'bag': '41:45 · 11:110 → 42:14', 'kural': "metin sayımı 'le-fî şekkin minhu murîb' 3 ayet + 'le-quziye beynehum'; okundu — 42:14'te 'ilâ ecelin musemmâ' eklenmiş", 'not': 'hüküm ve kuşku.'},
 {'bag': '11:112 → 42:15', 'kural': "metin sayımı 'kemâ umirt' 2 ayet; okundu — 'fe'staqim kemâ umirt'", 'not': 'dosdoğru ol.'},
 {'bag': '28:55 → 42:15', 'kural': "metin sayımı 'lenâ a'mâlunâ ve lekum a'mâlukum' 3 ayet; okundu", 'not': 'bizim işlerimiz, sizin işleriniz.'},
 {'bag': '42:15 → 42:16', 'kural': "kök ikilemesi حجج [3/3] — 'lâ hucce' / 'yuhâccûne', 'huccetuhum'", 'not': 'delil.'},
 {'bag': '40:5 → 42:16', 'kural': 'lemma دحض; okundu — hakkı çürütmek / delilleri çürük', 'not': 'çürütme.'},
 {'bag': '33:63 → 42:17', 'kural': "metin sayımı 've mâ yudrîke le'alle' 2 ayet; okundu — saat yakın", 'not': 'saat yakın.'},
 {'bag': '41:53 → 42:18', 'kural': "okuma — 'ennehu'l-haqq' (âyetler) / 'ennehe'l-haqq' (saat); KAPATILAMAZ", 'not': 'gerçek olduğu.'},
 {'bag': '11:66 → 42:19', 'kural': "metin sayımı 'el-qaviyyu'l-azîz' 2 ayet; okundu", 'not': 'güçlü, üstün.'},
 {'bag': '17:18 · 11:15 → 42:20', 'kural': "metin sayımı 'men kâne yurîd' 5 ayet; okundu — dünya / âhiret isteyen", 'not': 'dünya ve âhiret ekini.'},
 {'bag': '42:13 → 42:21', 'kural': "okuma — شرع [2/2]: 'şerea lekum mine'd-dîn' (Allah) / 'şeraû lehum mine'd-dîn' (ortaklar)", 'not': 'aynı tamlama, iki fâil.'},
 {'bag': '42:14 → 42:21', 'kural': "okuma — 'lev lâ kelimetun … le-quziye beynehum' / 'lev lâ kelimetu'l-fasl … le-quziye beynehum'", 'not': 'ertelenen hüküm.'},
 {'bag': '14:22 → 42:21', 'kural': "metin sayımı 'ez-zâlimîne lehum azâbun elîm' 2 ayet; okundu", 'not': 'zalimlere acı azap.'},
 {'bag': '42:18 → 42:22', 'kural': "okuma — شفق [2/2]: iman edenler 'muşfiqûne minhâ' / zalimler 'muşfiqîne mimmâ kesebû'", 'not': 'aynı sıfat, iki grup.'},
 {'bag': '39:34 → 42:22', 'kural': "metin sayımı 'lehum mâ yeşâûne inde rabbihim' 2 ayet; okundu", 'not': 'diledikleri Rableri katında.'},
 {'bag': '35:32 → 42:22', 'kural': "metin sayımı 'zâlike huve'l-fadlu'l-kebîr' 2 ayet; okundu", 'not': 'büyük lütuf.'},
 {'bag': '35:30 · 35:34 → 42:23', 'kural': "metin sayımı 'ğafûrun şekûr' 3 ayet; okundu", 'not': 'bağışlayan, karşılık veren.'},
 {'bag': '42:20 → 42:23', 'kural': "okuma — 'nezid lehû fî harsih' / 'nezid lehû fîhâ husnâ'", 'not': 'artırma cevabı, 1P.'},
 {'bag': '9:104 → 42:25', 'kural': "metin sayımı 'yaqbelu't-tevbete an ibâdih' 2 ayet; okundu", 'not': 'tevbe kabulü.'},
 {'bag': '42:16 → 42:26', 'kural': "okuma — 'lehum azâbun şedîd' sûre içi ikinci kez; جوب 'ustucîbe' / 'yestecîbu'", 'not': 'şiddetli azap; icabet.'},
 {'bag': '42:12 → 42:27', 'kural': "okuma — بسط [2/2]: 'yebsutu'r-rizqa' / 'lev besata'r-rizqa'", 'not': 'rızık genişletme.'},
 {'bag': '17:30 → 42:27', 'kural': "metin sayımı 'bi-ibâdihî habîrun basîr' 3 ayet; okundu — 17:30 rızık genişletme + habîr-basîr tek ayette; KAPATILAMAZ", 'not': 'kullarından haberdar, görür.'},
 {'bag': '31:34 → 42:28', 'kural': "metin sayımı 'yunezzilu'l-ğays' 2 ayet; okundu", 'not': 'yağmuru indirir.'},
 {'bag': '41:49 → 42:28', 'kural': "okuma — قنط: insanın 'qanût'u / 'min ba'di mâ qanatû'", 'not': 'umut kesme.'},
 {'bag': '30:22 → 42:29', 'kural': "metin sayımı 've min âyâtihî halqu's-semâvâti ve'l-ard' 2 ayet; okundu", 'not': 'göklerin ve yerin yaratılışı âyet.'},
 {'bag': '42:25 → 42:30', 'kural': "okuma — عفو [2/4]: 'ya'fû ani's-seyyiât' / 'ya'fû an kesîr'", 'not': 'affetme.'},
 {'bag': '42:22 → 42:30', 'kural': "okuma — كسب: 'mimmâ kesebû' / 'kesebet eydîkum'", 'not': 'kazanılan.'},
 {'bag': '29:22 → 42:31', 'kural': "esit2 BENZER 0,9000 (ölçüm) + metin sayımı 'bi-mu'cizîne fi'l-ard' 2 ayet; okundu", 'not': 'âciz bırakamazsınız.'},
 {'bag': '42:8 → 42:31', 'kural': "metin sayımı 'min veliyyin ve lâ nasîr' 7 ayet; sûre içi nakarat3 GEÇER", 'not': 'dost ve yardımcı yok.'},
 {'bag': '42:29 → 42:32', 'kural': "okuma — 've min âyâtih' giriş kalıbı", 'not': "O'nun âyetlerinden."},
 {'bag': '42:32 → 42:33', 'kural': "okuma — 'el-cevâr' (akıp gidenler) / 'revâkid' (durgun) — 3FP zamir geri döner", 'not': 'akma / durma.'},
 {'bag': '14:5 · 31:31 · 34:19 → 42:33', 'kural': "metin sayımı 'le-âyâtin li-kulli sabbârin şekûr' 4 ayet; okundu", 'not': 'sabreden, şükreden.'},
 {'bag': '42:23 → 42:33', 'kural': "okuma — شكر [2/2]: 'ğafûrun şekûr' (Allah) / 'sabbârin şekûr' (insan); aday 1041", 'not': 'şekûr iki gönderge.'},
 {'bag': '42:30 → 42:34', 'kural': "okuma — 've ya'fû an kesîr' (merfû) / 've ya'fu an kesîr' (meczûm)", 'not': 'çoğunu affeder.'},
 {'bag': '41:48 → 42:35', 'kural': "metin sayımı 'mâ lehum min mahîs' 2 ayet; okundu", 'not': 'kaçacak yer yok.'},
 {'bag': '28:60 → 42:36', 'kural': "metin sayımı 'ûtîtum min şey'', 'fe-metâ'u'l-hayâti'd-dunyâ', 'inda'llâhi hayrun ve ebqâ' — üçü de 2 ayet; okundu; xref", 'not': 'dünya geçimliği / Allah katı.'},
 {'bag': '16:42 · 16:99 · 29:59 → 42:36', 'kural': "metin sayımı 've alâ rabbihim yetevekkelûn' 5 ayet; okundu", 'not': 'Rablerine dayanırlar.'},
 {'bag': '42:5 · 42:23 → 42:37', 'kural': "okuma — غفر: Allah 'ğafûr' / insan 'hum yağfirûn'; aday 1041", 'not': 'bağışlama.'},
 {'bag': '42:37 → 42:39', 'kural': "okuma — 'izâ' + PERF + 'hum' + IMPF yapısı iki kez: bağışlarlar / karşı koyarlar", 'not': 'iki cevap.'},
 {'bag': '13:18 → 42:38', 'kural': "metin sayımı 'istecâbû li-rabbihim' 2 ayet; okundu", 'not': 'Rablerine icabet.'},
 {'bag': '22:35 · 28:54 · 32:16 → 42:38', 'kural': "metin sayımı 've mimmâ razaqnâhum yunfiqûn' 6 ayet; okundu", 'not': 'rızıktan harcama.'},
 {'bag': '42:26 → 42:38', 'kural': "okuma — جوب: 'yestecîbu' / 'istecâbû li-rabbihim'; aday 1041", 'not': 'icabet.'},
 {'bag': '42:27 → 42:39', 'kural': "okuma — بغي: 'le-beğav' / 'esâbehumu'l-bağy'", 'not': 'taşkınlık.'},
 {'bag': '10:27 → 42:40', 'kural': "okuma — 'cezâu seyyietin bi-mislihâ' / 'cezâu seyyietin seyyietun misluhâ'; imlâ farkı, metin sayımı yok", 'not': 'kötülüğün karşılığı.'},
 {'bag': '42:25 · 42:30 · 42:34 → 42:40', 'kural': "okuma — عفو [4/4]: fâil Allah / 'fe-men afâ' fâil insan; aday 1041", 'not': 'affetme.'},
 {'bag': '26:227 → 42:41', 'kural': "xref + okuma — 've'ntasarû min ba'di mâ zulimû' / 'intasara ba'de zulmih'; okundu", 'not': 'zulümden sonra savunma.'},
 {'bag': '42:39 → 42:41', 'kural': "okuma — نصر VIII. bab: 'yentasirûn' / 'intasara'", 'not': 'kendini savunma.'},
 {'bag': '9:91 · 9:93 → 42:41 · 42:42', 'kural': "metin sayımı 'innema's-sebîlu ale'llezîne' 2 ayet (9:93, 42:42); okundu — 'mâ … min sebîl' / 'innema's-sebîl' ikilisi aynı sırayla", 'not': 'yol yok / yol var.'},
 {'bag': '10:23 → 42:42', 'kural': "metin sayımı 'yebğûne fi'l-ard' 2 ayet; okundu; xref", 'not': 'yeryüzünde taşkınlık.'},
 {'bag': '29:23 → 42:42', 'kural': "metin sayımı 'ulâike lehum azâbun elîm' 3 ayet; 29:23 okundu", 'not': 'acı azap.'},
 {'bag': '31:17 → 42:43', 'kural': "metin sayımı 'min azmi'l-umûr' 3 ayet; 31:17 okundu", 'not': 'azim isteyen işler.'},
 {'bag': '42:37 → 42:43', 'kural': "okuma — غفر insan fiili: 'hum yağfirûn' / 'ğafera'; aday 1041", 'not': 'bağışlama.'},
 {'bag': '13:33 · 39:23 · 39:36 · 40:33 → 42:44', 'kural': "metin sayımı 'men yudlili'llâhu fe-mâ lehû min' 6 ayet; okundu; sûre içi 42:44 → 42:46 nakarat3 GEÇER", 'not': 'saptırılan.'},
 {'bag': '42:22 → 42:44', 'kural': "metin sayımı 'tera'z-zâlimîn' 2 ayet, sûre içi", 'not': 'zalimleri görürsün.'},
 {'bag': '40:11 → 42:44', 'kural': "okuma — 'fe-hel ilâ hurûcin min sebîl' / 'hel ilâ meraddin min sebîl'", 'not': 'dönüş yolu var mı.'},
 {'bag': '40:46 → 42:45', 'kural': "metin sayımı 'yu'radûne aleyhâ' 2 ayet; okundu — 40:46'da gönderge ateş", 'not': 'ona sunulurlar.'},
 {'bag': '39:15 → 42:45', 'kural': "metin sayımı 'el-hâsirîne'llezîne hasirû enfusehum ve ehlîhim' 2 ayet; okundu; xref — 39:15 'qul' ile, 42:45 iman edenlerin sözü", 'not': 'asıl hüsran.'},
 {'bag': '9:68 · 11:39 · 39:40 → 42:45', 'kural': "metin sayımı 'azâbun muqîm' 5 ayet; okundu", 'not': 'kalıcı azap.'},
 {'bag': '18:43 · 28:81 → 42:46', 'kural': "xref — 'yansurûnehû min dûni'llâh' (tekil); okundu", 'not': "Allah'tan başka yardım eden."},
 {'bag': '30:43 → 42:47', 'kural': "metin sayımı 'yevmun lâ meradde lehû mina'llâh' 2 ayet; okundu; xref", 'not': 'geri çevrilmeyen gün.'},
 {'bag': '42:44 → 42:47', 'kural': "okuma — ردد [2/2]: 'hel ilâ meraddin' / 'lâ meradde lehû'", 'not': 'dönüş yok.'},
 {'bag': '42:38 → 42:47', 'kural': "okuma — جوب: 'istecâbû' (haber) / 'istecîbû' (emir); aday 1041", 'not': 'icabet.'},
 {'bag': '41:13 → 42:48', 'kural': "metin sayımı 'fe-in a'radû' 2 ayet; okundu", 'not': 'yüz çevirirlerse.'},
 {'bag': '42:6 → 42:48', 'kural': "okuma — حفظ [2/2]: 'Allâhu hafîzun aleyhim' / 'fe-mâ erselnâke aleyhim hafîzâ'", 'not': 'bekçi.'},
 {'bag': '11:9 · 30:36 → 42:48', 'kural': "metin sayımı 'ezaqna'l-insâne minnâ rahmeten' 2 ayet (11:9); 30:36 aynı dizi, son farklı; okundu; xref", 'not': 'sevinç / nankörlük.'},
 {'bag': '28:68 · 30:54 · 39:4 → 42:49', 'kural': "metin sayımı 'yahluqu mâ yeşâ'' 6 ayet; okundu", 'not': 'dilediğini yaratır.'},
 {'bag': '42:11 → 42:50', 'kural': "okuma — زوج [3/3]: 'ezvâcen' ×2 / 'yuzevvicuhum'", 'not': 'eşler / çift kılma.'},
 {'bag': '16:70 · 35:44 → 42:50', 'kural': "metin sayımı 'alîmun qadîr' 3 ayet; okundu", 'not': 'bilen, gücü yeten.'},
 {'bag': '41:5 → 42:51', 'kural': "okuma — 'hicâb': inkârcıların sözü 'beyninâ ve beynike hicâb' / konuşmanın yolu 'min verâi hicâb'; okundu", 'not': 'perde.'},
 {'bag': '42:51 → 43:4', 'kural': "metin sayımı 'aliyyun hakîm' 2 ayet; 43:4 henüz okunmadı — aday 1040 alanı, kayıt", 'not': 'yüce, hakîm.'},
 {'bag': '42:3 · 42:7 · 42:13 → 42:52', 'kural': "metin sayımı 've kezâlike evhaynâ ileyk' 2 ayet (42:7, 42:52; nakarat3 GEÇER) — sûrenin vahiy çerçevesi; okuma", 'not': 'vahiy.'},
 {'bag': '40:15 → 42:52', 'kural': "okuma — rûh + emr + 'men yeşâ' + 'ibâd' dörtlüsü; okundu", 'not': 'emirden ruh.'},
 {'bag': '42:33 → 42:52', 'kural': "okuma — روح [2/2]: 'er-rîh' / 'rûhan' (gloss iki anlam)", 'not': 'rüzgâr / ruh.'},
 {'bag': '42:4 → 42:53', 'kural': "metin sayımı 'lehû mâ fi's-semâvâti ve mâ fi'l-ard' 15 ayet; sûre içi nakarat3 GEÇER — sûrenin 4. ve son ayeti", 'not': "göklerdekiler ve yerdekiler O'nun."},
 {'bag': '42:15 → 42:53', 'kural': "okuma — صير [2/2]: 'ileyhi'l-masîr' / 'tesîru'l-umûr'", 'not': 'varış.'},
]}

pa = '/home/claude/repo/bulgular/aday_bulgular.json'
AD = json.load(open(pa, encoding='utf-8'))
AD.pop('AX_shura', None)
onceki = max(x['no'] for v in AD.values() if isinstance(v, list) for x in v if isinstance(x, dict) and 'no' in x)
nos = [x['no'] for x in SHURA]
assert nos == list(range(onceki + 1, onceki + 1 + len(nos))), 'numara sırası kopuk: önceki %d, bu set %s' % (onceki, nos)
AD['AX_shura'] = SHURA
json.dump(AD, open(pa, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = sum(len(v) for v in AD.values() if isinstance(v, list))
print('AX_shura', len(SHURA), ('(%d-%d)' % (nos[0], nos[-1])) if nos else '(boş)', '| toplam aday', tot)

pb = '/home/claude/repo/notlar/okuma_baglantilari.json'
BG = json.load(open(pb, encoding='utf-8'))
BG.update(BAGLAR)
json.dump(BG, open(pb, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('okuma_baglantilari: AS_shura', len(BAGLAR['AS_shura']))
