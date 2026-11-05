# -*- coding: utf-8 -*-
"""uret_blok_2.py — sûre 2 (Bakara) blok betiklerini üretir. BLOK BAŞINA KAYIT.

Değişiklik (2026-09-24): kayıt artık tur sonunu beklemiyor. Her blok betiği koşulduğunda
okuma_metni.json, mercek_kayit.json ve ilerleme o blok için yazılır; blok bilançosu (TAM SAYIM)
ve çıpa kararları da okuma_metni'ne yapılandırılmış alan olarak girer. Oturum yarıda kalsa da
okunmuş her blok kayıtlıdır.

Sûre numarası TEK değişkende (S). olcum_bicim.olcum(S, n), AR[(S, n)], OM[str(S)] hep S'den
türer — üç kez atlanan elle-değiştirme hatası (tur sonu notu) burada yapısal olarak kapalı.
Besmele korpustan (1:1'in ilk dört kelimesinin iskeleti) ayıklanır; Arapça sabit yok.
"""
import sys
S = 2
METIN = 'bakara_metin_1'
KAYIT = 'bakara_kayit'
# blok başı kayıt: blok okundukça listeye eklenir (başlık okuma sonrası yazılır)
BLOKLAR = [(21, 25), (26, 29), (30, 33), (34, 39), (40, 46), (47, 53), (54, 59), (60, 61), (62, 66), (67, 70), (71, 74), (75, 79), (80, 83), (84, 86), (87, 90), (91, 95), (96, 101), (102, 103), (104, 108), (109, 112), (113, 116), (117, 121), (122, 126), (127, 132), (133, 136), (137, 141), (142, 143), (144, 147), (148, 152), (153, 159), (160, 164), (165, 167), (168, 172), (173, 176), (177, 178), (179, 182), (183, 185), (186, 188), (189, 194), (195, 196), (197, 199), (200, 203)]
BASLIK = {
 (21, 25): "2:21-25 — ey insanlar, sizi yaratan Rabbinize kulluk edin; yeri döşek, göğü bina kılan O'dur; kulumuza indirdiğimizden şüphedeyseniz benzerinden bir sûre getirin; yapamazsanız yakıtı insanlar ve taşlar olan ateşten sakının; inanıp iyi işler yapanlara altlarından ırmaklar akan bahçeleri müjdele",
 (26, 29): "2:26-29 — Allah sivrisineği ve üstündekini misal vermekten çekinmez; inananlar onun hak olduğunu bilir, inkâr edenler ne demek istedi der; ahdi bozanlar, emredileni kesenler kaybedenlerdir; ölüydünüz diriltti, öldürecek, diriltecek, O'na döndürüleceksiniz; yerdekilerin hepsini sizin için yarattı, göğe yöneldi, yedi gök olarak düzenledi",
 (30, 33): "2:30-33 — Rabbin meleklere yeryüzünde bir halife kılacağım dedi; orada bozgunculuk yapacak birini mi dediler; ben sizin bilmediğinizi bilirim dedi; Âdem'e isimlerin hepsini öğretti, meleklere sundu; bize öğrettiğinden başka bilgimiz yok dediler; ey Âdem onlara isimlerini bildir; göklerin ve yerin gaybını bilirim dememiş miydim",
 (34, 39): "2:34-39 — meleklere Âdem'e secde edin dedik, İblîs dışında secde ettiler; ey Âdem sen ve eşin bahçede oturun, şu ağaca yaklaşmayın; şeytan onları kaydırıp çıkardı, inin dedik; Âdem Rabbinden kelimeler aldı, O tevbesini kabul etti; benden yol gösterici gelirse ona uyanlara korku yok; inkâr edip yalanlayanlar ateşin halkıdır",
 (40, 46): "2:40-46 — ey İsrâiloğulları nimetimi anın, ahdimi yerine getirin, yalnız benden korkun; indirdiğime iman edin, âyetlerimi az bedele satmayın; hakkı bâtılla karıştırmayın; namazı kılın, zekâtı verin, rükû edin; insanlara iyiliği emredip kendinizi unutuyor musunuz; sabır ve namazla yardım isteyin; onlar Rablerine kavuşacaklarını düşünürler",
 (47, 53): "2:47-53 — ey İsrâiloğulları nimetimi ve sizi âlemlere üstün kıldığımı anın; kimsenin kimse yerine bir şey ödeyemeyeceği günden sakının; sizi Firavun ailesinden kurtardık; denizi yardık, Firavun ailesini boğduk; Mûsâ ile kırk gece sözleştik, buzağıyı edindiniz; sizi bağışladık; Mûsâ'ya Kitabı ve furkanı verdik",
 (54, 59): "2:54-59 — Mûsâ kavmine: buzağıyla kendinize zulmettiniz, yaratanınıza tevbe edin; Allah'ı açıkça görmedikçe inanmayız dediniz, yıldırım sizi yakaladı; ölümünüzden sonra sizi dirilttik; bulutu gölge yaptık, helva ve bıldırcın indirdik; bu kasabaya girin, hitta deyin; zulmedenler sözü değiştirdi, gökten azap indirdik",
 (60, 61): "2:60-61 — Mûsâ kavmi için su istedi, asânla taşa vur dedik, on iki pınar fışkırdı; tek yiyeceğe katlanamayız, Rabbine dua et de yerin bitirdiklerinden çıkarsın dediniz; bir şehre inin; üzerlerine aşağılık ve yoksulluk vuruldu",
 (62, 66): "2:62-66 — iman edenler, Yahudiler, Hıristiyanlar, Sâbiîler — Allah'a ve âhiret gününe inanıp iyi iş yapanlara ödül; sizden söz aldık, Tûr'u üstünüze kaldırdık; sonra yüz çevirdiniz; Sebt'te sınırı aşanlara maymun olun dedik; bunu ibret ve öğüt kıldık",
 (67, 70): "2:67-70 — Mûsâ kavmine Allah bir inek boğazlamanızı emrediyor dedi; Rabbine dua et de ne olduğunu açıklasın dediler — ne yaşlı ne genç, orta yaşlı; rengi parlak sarı, bakanlara sevinç veren; sığırlar bize benzer göründü, Allah dilerse doğru yolu buluruz",
 (71, 74): "2:71-74 — 2:71-74 — yeri sürmeyen, ekini sulamayan, kusursuz, alacasız bir inek; şimdi gerçeği getirdin dediler ve boğazladılar; bir kişiyi öldürmüş, onun hakkında tartışmıştınız; bir parçasıyla ona vurun — Allah ölüleri böyle diriltir; sonra kalpleriniz taş gibi, daha da katı oldu; taşlardan ırmak fışkıranı, yarılıp su çıkanı, Allah korkusundan düşeni var",
 (75, 79): "2:75-79 — 2:75-79 — size inanacaklarını mı umuyorsunuz, içlerinden bir grup Allah'ın sözünü işitip anladıktan sonra değiştirirdi; inananlarla karşılaşınca inandık der, baş başa kalınca Allah'ın size açtığını onlara mı anlatıyorsunuz derler; Allah gizlediklerini ve açığa vurduklarını bilir; ümmîler kitabı bilmez, yalnız kuruntu ve zan; kitabı elleriyle yazıp bu Allah katındandır diyenlere vay",
 (80, 83): "2:80-83 — ateş bize sayılı günler dışında dokunmayacak dediler; Allah katından söz mü aldınız, yoksa Allah hakkında bilmediğinizi mi söylüyorsunuz; kötülük kazanıp hatası kuşatanlar ateş halkı, inanıp iyi iş yapanlar cennet halkı; İsrâiloğullarından söz: Allah'tan başkasına kulluk yok, ana babaya, yakına, yetime, yoksula iyilik, insanlara güzel söz, namaz, zekât; sonra pek azınız dışında yüz çevirdiniz",
 (84, 86): "2:84-86 — sizden söz aldık: kanlarınızı dökmeyecek, kendinizi yurtlarınızdan çıkarmayacaksınız, kabul ettiniz; sonra kendinizi öldürüyor, bir grubunuzu yurtlarından çıkarıyor, esir gelince fidye veriyorsunuz; kitabın bir kısmına inanıp bir kısmını mı inkâr ediyorsunuz; dünyada rezillik, kıyamet günü azabın en çetini; dünya hayatını âhirete karşılık satın alanlardan azap hafifletilmez",
 (87, 90): "2:87-90 — Mûsâ'ya kitap verdik, ardından elçiler gönderdik, Meryem oğlu Îsâ'ya açık kanıtlar verdik, onu kutsal ruhla destekledik; hoşlanmadığınızı getiren her elçiye büyüklendiniz, bir kısmını yalanladınız, bir kısmını öldürüyorsunuz; kalplerimiz perdeli dediler, Allah onları lanetledi; yanlarındakini doğrulayan kitap gelince tanıdıklarını inkâr ettiler; kendilerini ne kötü şeye sattılar, gazap üstüne gazaba uğradılar",
 (91, 95): "2:91-95 — Allah'ın indirdiğine inanın denince bize indirilene inanırız deyip ötesini inkâr ederler; inanıyor idiyseniz peygamberleri neden öldürüyordunuz; Mûsâ açık kanıtlarla geldi, ardından buzağıyı edindiniz; söz alındı, Tûr kaldırıldı, işittik ve karşı geldik dediler, buzağı kalplerine içirildi; âhiret yurdu yalnız sizinse ölümü dileyin; elleriyle önden gönderdikleri yüzünden onu asla dilemeyecekler",
 (96, 101): "2:96-101 — onları insanların hayata en düşkünü bulursun, her biri bin yıl yaşatılmak ister, bu onu azaptan uzaklaştırmaz; kim Cibrîl'e düşmansa o onu Allah'ın izniyle senin kalbine indirdi; kim Allah'a, meleklerine, elçilerine, Cibrîl'e ve Mîkâl'e düşmansa Allah da kâfirlere düşmandır; sana apaçık âyetler indirdik; her söz verdiklerinde bir grup onu attı; Allah katından elçi gelince kitap verilenlerden bir grup Allah'ın kitabını sırtlarının arkasına attı",
 (102, 103): "2:102-103 — Süleymân'ın mülkü hakkında şeytanların okuduğuna uydular; Süleymân inkâr etmedi, şeytanlar inkâr etti, insanlara büyüyü ve Bâbil'de iki meleğe, Hârût ile Mârût'a indirileni öğrettiler; o ikisi biz yalnızca bir sınavız demeden kimseye öğretmezdi; kişiyle eşinin arasını ayıranı öğrendiler, Allah'ın izni olmadan kimseye zarar veremezlerdi; onu satın alanın âhirette payı yok; inanıp sakınsalardı Allah katından karşılık daha hayırlıydı",
 (104, 108): "2:104-108 — ey inananlar râ'inâ demeyin, unzurnâ deyin ve dinleyin; kitap ehlinden inkâr edenler ve ortak koşanlar size Rabbinizden hayır indirilmesini istemez, Allah rahmetini dilediğine has kılar; bir âyeti siler ya da unutturursak daha hayırlısını ya da benzerini getiririz; göklerin ve yerin mülkü Allah'ındır, O'ndan başka velî ve yardımcı yoktur; Mûsâ'ya sorulduğu gibi elçinize sormak mı istiyorsunuz, inkârı imanla değiştiren yoldan sapmıştır",
 (109, 112): "2:109-112 — kitap ehlinden birçoğu kıskançlıkla sizi imandan sonra küfre döndürmek ister, Allah emrini getirinceye kadar affedin ve hoş görün; namazı kılın, zekâtı verin, önden gönderdiğiniz hayrı Allah katında bulursunuz; Yahudi ya da Hristiyan olandan başkası cennete girmeyecek dediler, bu onların kuruntusu, delilinizi getirin; hayır, iyilik yaparak yüzünü Allah'a teslim edenin karşılığı Rabbinin katındadır",
 (113, 116): "2:113-116 — Yahudiler Hristiyanlar bir şey üzerinde değil, Hristiyanlar Yahudiler bir şey üzerinde değil dediler, Allah kıyamet günü aralarında hüküm verecek; mescitlerde Allah'ın adının anılmasını engelleyenden daha zâlim kim var, onlara dünyada rezillik âhirette büyük azap; doğu da batı da Allah'ındır, nereye dönerseniz Allah'ın yüzü oradadır; Allah çocuk edindi dediler, O münezzehtir, göklerde ve yerde ne varsa O'nundur",
 (117, 121): "2:117-121 — Allah göklerin ve yerin eşsiz yaratıcısıdır, bir işe hükmettiğinde ona Ol der o da olur; bilmeyenler Allah bizimle konuşsa ya da bize bir âyet gelse dediler, öncekiler de böyle demişti, kalpleri benzeşti; seni hak ile müjdeleyici ve uyarıcı gönderdik; onların dinine uymadıkça Yahudiler ve Hristiyanlar senden razı olmayacak, Allah'ın yolu asıl yoldur; kendilerine kitap verdiklerimiz onu hakkıyla okur",
 (122, 126): "2:122-126 — Ey İsrâiloğulları nimetimi ve sizi âlemlere üstün kıldığımı anın, kimsenin kimseye fayda veremeyeceği günden sakının; Rabbi İbrâhim'i kelimelerle sınadı, seni insanlara önder kılacağım dedi, ahdim zalimlere ulaşmaz; Evi insanlar için toplanma ve güven yeri kıldık, İbrâhim ve İsmâil'e evimi temizleyin diye ahit verdik; İbrâhim Rabbim burayı güvenli belde kıl, inananları ürünlerle rızıklandır dedi",
 (127, 132): "2:127-132 — İbrâhim ve İsmâil Evin temellerini yükseltirken Rabbimiz bizden kabul et dediler, ikimizi sana teslim olanlar kıl, soyumuzdan teslim olan bir ümmet çıkar, onlara içlerinden âyetlerini okuyan bir elçi gönder; İbrâhim'in yolundan ancak kendini bilmeyen yüz çevirir, Rabbi teslim ol dedi, âlemlerin Rabbine teslim oldum dedi; İbrâhim ve Ya'kûb oğullarına ancak teslim olmuş olarak can verin diye vasiyet etti",
 (133, 136): "2:133-136 — Ya'kûb'a ölüm geldiğinde oğullarına benden sonra neye kulluk edeceksiniz dedi, senin ve ataların İbrâhim, İsmâil ve İshâk'ın ilâhına, tek ilâha kulluk edeceğiz dediler; o geçmiş bir ümmettir, kazandıkları onlara, kazandıklarınız size; Yahudi ya da Hristiyan olun dediler, de ki hayır hanîf İbrâhim'in yolu; deyin ki Allah'a ve peygamberlere indirilene inandık, aralarında ayırım yapmayız",
 (137, 141): "2:137-141 — sizin inandığınız gibi inanırlarsa doğru yolu bulurlar, yüz çevirirlerse ayrılıktadırlar, Allah sana yeter; Allah'ın boyası, boyası Allah'ınkinden güzel kim var; de ki Allah hakkında bizimle mi tartışıyorsunuz, O bizim de sizin de Rabbinizdir; İbrâhim ve oğulları Yahudi ya da Hristiyandı mı diyorsunuz, siz mi daha iyi bilirsiniz Allah mı; o geçmiş bir ümmettir",
 (142, 143): "2:142-143 — insanlardan beyinsizler onları kıblelerinden döndüren nedir diyecek, de ki doğu da batı da Allah'ındır; sizi orta bir ümmet kıldık ki insanlara şahit olasınız, elçi de size şahit olsun; kıbleyi elçiye uyanı geri dönenden ayırt edelim diye kıldık; Allah imanınızı boşa çıkarmaz",
 (144, 147): "2:144-147 — yüzünün göğe çevrildiğini görüyoruz, seni razı olacağın kıbleye yönelteceğiz, yüzünü Mescid-i Harâm'a çevir; kitap verilenlere her âyeti getirsen kıblene uymazlar; onu oğullarını tanır gibi tanırlar, bir grup hakkı gizler; hak Rabbindendir, kuşkulananlardan olma",
 (148, 152): "2:148-152 — herkesin bir yönü vardır, hayırlarda yarışın, Allah hepinizi bir araya getirir; nereden çıkarsan yüzünü Mescid-i Harâm'a çevir; insanların size karşı delili olmasın, onlardan korkmayın benden korkun; içinizden size âyetlerimizi okuyan bir elçi gönderdik; beni anın ki ben de sizi anayım",
 (153, 159): "2:153-159 — sabırla ve namazla yardım isteyin; Allah yolunda öldürülenlere ölü demeyin, onlar diridir; sizi korku, açlık ve eksiltmeyle sınayacağız, sabredenleri müjdele; Safâ ile Merve Allah'ın nişanlarındandır; indirdiğimizi gizleyenlere Allah lânet eder",
 (160, 164): "2:160-164 — tevbe edip düzeltenlerin tevbesini kabul ederim; kâfir olarak ölenlere Allah'ın, meleklerin ve insanların lâneti; ilâhınız tek bir ilâhtır; göklerin ve yerin yaratılışında, gece ile gündüzde, gemilerde, gökten inen suda, rüzgârlarda ve bulutta akleden bir kavim için âyetler vardır",
 (165, 167): "2:165-167 — insanlardan kimi Allah'ın dışında denkler edinir, onları Allah'ı sever gibi severler, iman edenlerin Allah sevgisi daha güçlüdür; zulmedenler azabı gördüklerinde bütün kuvvetin Allah'ın olduğunu görselerdi; uyulanlar uyanlardan uzaklaşır, bağlar kopar; uyanlar keşke bir dönüş olsa da biz de onlardan uzaklaşsak der; ateşten çıkacak değillerdir",
 (168, 172): "2:168-172 — ey insanlar, yeryüzündekilerden helâl ve temiz olarak yiyin, şeytanın adımlarına uymayın; o size kötülüğü, hayâsızlığı ve Allah hakkında bilmediğinizi söylemeyi emreder; Allah'ın indirdiğine uyun denince atalarımızı üzerinde bulduğumuza uyarız derler; inkâr edenler çağrıdan ve seslenmeden başkasını işitmeyene bağıran gibidir, sağır, dilsiz, kördürler; ey iman edenler, verdiğimiz rızkın temizlerinden yiyin ve Allah'a şükredin",
 (173, 176): "2:173-176 — O size yalnızca leşi, kanı, domuz etini ve Allah'tan başkası adına kesileni haram kıldı, zorda kalana günah yoktur; Allah'ın kitaptan indirdiğini gizleyip az bedele değişenler karınlarına ateşten başkasını yemezler, Allah kıyamet günü onlarla konuşmaz; onlar sapıklığı doğru yola, azabı bağışlanmaya karşılık satın aldılar; Allah kitabı hakla indirdi, kitap hakkında ayrılığa düşenler derin bir ayrılık içindedir",
 (177, 178): "2:177-178 — İyilik yüzlerinizi doğu ve batı tarafına çevirmeniz değildir; asıl iyilik Allah'a, âhiret gününe, meleklere, kitaba ve peygamberlere iman eden, malı sevgisine rağmen yakınlara, yetimlere, yoksullara, yolda kalmışa, isteyenlere ve köleler için veren, namazı kılan, zekâtı veren, ahdine vefa gösteren ve darlıkta sabredenlerin iyiliğidir; ey iman edenler, öldürülenler hakkında size kısas yazıldı, kardeşinden bağışlanana uygun izleme ve güzellikle ödeme düşer, bu Rabbinizden bir hafifletme ve rahmettir",
 (179, 182): "2:179-182 — Ey akıl sahipleri, kısasta sizin için hayat vardır; birinize ölüm geldiğinde mal bırakacaksa anne babaya ve yakınlara uygun biçimde vasiyet size yazıldı; kim onu işittikten sonra değiştirirse günahı değiştirenlerin üzerinedir; kim vasiyet edenin haktan sapmasından korkup aralarını düzeltirse ona günah yoktur",
 (183, 185): "2:183-185 — Ey iman edenler, oruç sizden öncekilere yazıldığı gibi size de yazıldı; sayılı günlerdir, hasta ya da yolcu olan başka günlerde sayısınca tutar, güç yetirenlere bir yoksulu doyuracak fidye vardır; Ramazan ayı Kur'ân'ın indirildiği aydır, kim bu aya erişirse onu oruçla geçirsin; Allah sizin için kolaylık ister, zorluk istemez",
 (186, 188): "2:186-188 — Kullarım sana benden sorduklarında, ben yakınım, dua edenin çağrısına cevap veririm; oruç gecesinde kadınlarınıza yaklaşmak size helâl kılındı, fecirden beyaz iplik siyah iplikten ayırt edilinceye kadar yiyin, için, sonra orucu geceye kadar tamamlayın; bunlar Allah'ın sınırlarıdır; mallarınızı aranızda haksızlıkla yemeyin",
 (189, 194): "2:189-194 — Sana hilâlleri soruyorlar, de ki onlar insanlar ve hac için vakit ölçüleridir; evlere kapılarından girin; sizinle savaşanlarla Allah yolunda savaşın ama sınırı aşmayın; fitne öldürmekten daha ağırdır; Mescid-i Haram yanında sizinle savaşmadıkça savaşmayın; vazgeçerlerse Allah bağışlayandır; fitne kalmayıncaya kadar savaşın; haram ay haram aya karşılıktır, saygıya değer şeylerde kısas vardır",
 (195, 196): "2:195-196 — Allah yolunda harcayın, kendinizi tehlikeye atmayın, iyilik edin, Allah iyilik edenleri sever; haccı ve umreyi Allah için tamamlayın, engellenirseniz kolayınıza gelen kurbanlık gerekir; bulamayan hacda üç gün, döndüğünüzde yedi gün oruç tutar, bu tam on gündür; Allah'ın cezası çetindir",
 (197, 199): "2:197-199 — Hac bilinen aylardır, hacda kadına yaklaşmak, yoldan çıkmak ve kavga etmek yoktur; azık edinin, azığın en hayırlısı takvâdır; Rabbinizden lütuf aramanızda günah yoktur, Arafat'tan akın ettiğinizde Meş'ar-i Haram'ın yanında Allah'ı anın; sonra insanların akın ettiği yerden akın edin ve Allah'tan bağışlanma dileyin",
 (200, 203): "2:200-203 — Hac ibadetlerinizi bitirince atalarınızı andığınız gibi hatta daha güçlü Allah'ı anın; insanlardan kimi Rabbimiz bize dünyada ver der, onun âhirette payı yoktur; kimi de Rabbimiz bize dünyada da âhirette de iyilik ver ve bizi ateşin azabından koru der, onlar için kazandıklarından pay vardır; sayılı günlerde Allah'ı anın, O'nun huzurunda toplanacaksınız",
}

SABLON = r'''# -*- coding: utf-8 -*-
"""blok_%(S)d_%(a)d_%(b)d.py — %(baslik)s

uret_blok_%(S)d.py tarafından ÜRETİLDİ — elle düzenleme. Ölçüm (›) defterden (olcum_bicim),
dikey (▽) blok_dikey JSON'undan, bilanço blok_bilanco'dan; yalnız meal ve mercek (◇) elle.
"""
import json, re, unicodedata
import olcum_bicim, gloss_gecis, blok_bilanco
from %(metin)s import MEAL, M
from %(kayit)s import CIPA, ARIZA

S, A1, A2 = %(S)d, %(a)d, %(b)d
REPO = '/home/claude/repo/notlar/'
DIK = json.load(open('blok_dikey_%%d_%%d_%%d.json' %% (S, A1, A2), encoding='utf-8'))
ESMA = json.load(open('esma_kayit.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {(s['no'], a['no']): a['ar'] for s in veri['sureler'] for a in s['ayetler']}
_H = re.compile('[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]')
_isk = lambda w: _H.sub('', unicodedata.normalize('NFC', w)).replace('\u0671', '\u0627').replace('\ufeff', '')
BESMELE = [_isk(w) for w in AR[(1, 1)].split()[:4]]
if A1 == 1 and S not in (1, 9):
    _t = AR[(S, 1)].split()
    if [_isk(w) for w in _t[:4]] == BESMELE:
        AR[(S, 1)] = ' '.join(_t[4:])
    assert [_isk(w) for w in AR[(S, 1)].split()[:4]] != BESMELE, 'besmele ayıklanmadı — DUR'
for n in range(A1, A2 + 1):
    assert n in MEAL and n in M, 'meal/mercek eksik: %%d:%%d — DUR' %% (S, n)

p = REPO + 'okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
OM.setdefault(str(S), {})
OM_ONCE = set(OM[str(S)])
for n in range(A1, A2 + 1):
    k = '%%d:%%d' %% (S, n)
    e = ESMA.get(k, {})
    OM[str(S)][k] = {"ar": AR[(S, n)], "meal": MEAL[n],
                     "olcum": olcum_bicim.olcum(S, n),
                     "mercek": M[n],
                     "dikey": DIK.get(k, "  · (ayette kök bulunmuyor — dikey satır yok)"),
                     "cipa": CIPA.get(n, dict(kademe=None, olgu=False, cipa=False)),
                     "esma": {x: e.get(x) for x in ('sinif_oto', 'sinif_el', 'e_oto', 'e_el', 'muhur', 'cift', 'ton', 'ton_kismi', 'bant')}}
    gloss_gecis.gecir_kayit(OM[str(S)][k])
bil = blok_bilanco.bilanco(S, A1, A2)
bil['ariza'] = ARIZA.get((A1, A2), [])
bil['cipa_L4'] = [n for n in range(A1, A2 + 1) if CIPA.get(n, {}).get('cipa')]
bil['tarayici_isabet'] = [a for a in bil['tarayici_v4_aday'] if CIPA.get(int(a.split(':')[1]), {}).get('cipa')]
OM[str(S)].setdefault('_bilanco', {})['%%d-%%d' %% (A1, A2)] = bil

# ilerleme — kayıttan koşulur (elle artırma YOK)
D = json.load(open('defter.json', encoding='utf-8'))
TAM = set(OM['ilerleme']['tam'])
assert S not in TAM, 'sûre %%d zaten TAM sayılıyor — çift sayım riski, DUR' %% S
# SÛRE 2 ONARIMI (iskele_2): S'nin kayıtlı ayetleri 'S:A' ve eski birleşik 'S:A-B' anahtarlarından
# (eski kayıt 1-20: iki birleşik anahtar). 'A-B' biçimli eski blok özeti anahtarları okuma SAYILMAZ.
# 2:1-20 bu kümenin içinde olduğu için ayrıca eklenmez — çift sayım yok (şablonun 2:1-20 terimi kaldırıldı).
oku_S = set()
for k in OM[str(S)]:
    m = re.fullmatch(r'%%d:(\d+)(?:-(\d+))?' %% S, k)
    if m:
        oku_S.update(range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1))
oku_S = sorted(oku_S)
assert oku_S == list(range(1, oku_S[-1] + 1)), 'sûre %%d kayıtlı ayetleri kesintili — DUR' %% S
OM['ilerleme']['kismi'][str(S)] = '1-%%d ayet düzeyinde (1-20 eski kayıt + 21-%%d blok başı kayıt; %%d ayet)' %% (oku_S[-1], oku_S[-1], len(oku_S))
okunan = (sum(1 for r in D if r['k'][0] in TAM)
          + sum(1 for r in D if r['k'][0] == S and r['k'][1] in set(oku_S)))
OM['ilerleme']['okunan_ayet'] = okunan
OM['ilerleme']['korpus_yuzde'] = round(100 * okunan / len(D), 1)
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

pm = REPO + 'mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK.setdefault(str(S), {})
# SÛRE 2: mercek_kayit['2']'de eski sıkıştırılmış ◇ notları var (2:22, 2:24 …). Üstüne yazmadan önce
# '_sikistirilmis_eski' altına bir kez arşivlenir (blok ilk kez yazılırken; yeniden koşuda arşivlenmez).
for n in range(A1, A2 + 1):
    k = '%%d:%%d' %% (S, n)
    if k not in OM_ONCE and k in MK[str(S)]:
        MK[str(S)].setdefault('_sikistirilmis_eski', {}).setdefault(k, MK[str(S)][k])
    MK[str(S)][k] = gloss_gecis.gecir(M[n])
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

print('blok %%d:%%d-%%d yazıldı · okuma_metni sûre %%d → %%d ayet · mercek_kayit → %%d · ilerleme %%d (%%%%%%s)'
      %% (S, A1, A2, S, len([k for k in OM[str(S)] if not k.startswith('_')]), len(MK[str(S)]),
         okunan, OM['ilerleme']['korpus_yuzde']))
print('kısmi:', OM['ilerleme']['kismi'])
'''

for a, b in BLOKLAR:
    ad = 'blok_%d_%d_%d.py' % (S, a, b)
    open(ad, 'w', encoding='utf-8').write(SABLON % dict(S=S, a=a, b=b, baslik=BASLIK[(a, b)], metin=METIN, kayit=KAYIT))
    print('üretildi:', ad)
