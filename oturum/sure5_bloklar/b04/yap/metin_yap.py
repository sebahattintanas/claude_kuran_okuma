# blok 4 (5:7-11) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b04/say2.txt'
os.environ['OLC'] = '/home/claude/b04/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Kitap ehlinin yemeği ve kadınları; abdest ve teyemmüm; nimeti ve misakı anma' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 7: "Allah'ın üzerinizdeki nimetini ve 'İşittik ve itaat ettik' dediğinizde sizi kendisiyle bağladığı ahdini anın. Allah'tan sakının. Şüphesiz Allah göğüslerin özünü bilendir.",
 8: "Ey iman edenler! Allah için adaleti ayakta tutanlar, adaletle tanıklık edenler olun. Bir kavme duyduğunuz kin sizi adaletsizliğe sürüklemesin. Adaletli olun; bu takvâya daha yakındır. Allah'tan sakının. Şüphesiz Allah yaptıklarınızdan haberdardır.",
 9: "Allah iman edip salih ameller işleyenlere vaat etti: onlar için bağışlanma ve büyük bir ödül vardır.",
 10: "İnkâr edip âyetlerimizi yalanlayanlar ise, işte onlar alevli ateşin halkıdır.",
 11: "Ey iman edenler! Allah'ın üzerinizdeki nimetini anın: hani bir kavim size ellerini uzatmaya yeltenmişti de O onların ellerini sizden çekmişti. Allah'tan sakının. İnananlar yalnız Allah'a dayansınlar.",
}

T7 = ("muhatap 2MP (adsız; 'zkurû', ''aleykum', 'vâsaqakum', 'qultum', 'ttequ'); Allah (lafız); 'vâsaqa' faili 3MS (adsız; 7. kelime — gönderge lafız); "
      "söz içi konuşan 1P (adsız; 'semi'nâ', 'eta'nâ' — muhatap 2MP'nin sözü)")
T8 = ("muhatap 2MP (adsız; 'llezîne âmenû' — nidâ, 2. ve 3. kelime; 'kûnû', 'yecrimennekum', 'ta'dilu', 'ttequ', 'ta'melûn'); 'qavvâmîne' ve 'şuhedâ'e' (muhatabın haberi; çoğul, 5. ve 7. kelime); Allah (lafız); "
      "'şene'ânu qavmin' ('yecrimennekum' faili; izafet, 11-12. kelime); 'huve' 3MS (zamir; adsız — gönderge adalet, 17. kelime)")
T9 = ("Allah (lafız; 've'ade' faili); 'llezîne âmenû ve 'amilu's-sâlihâti' ('ve'ade' mef'ûlü; 3-6. kelime); 'âmenû' ve ''amilu' faili 3MP (adsız; 4. ve 5. kelime)")
T10 = ("'llezîne keferû ve kezzebû' (mübtedâ; 1-3. kelime); 'keferû' ve 'kezzebû' faili 3MP (adsız; 2. ve 3. kelime); konuşan 1P (adsız; 'âyâtinâ'); 'ulâ'ike' (işaret; gönderge 'llezîne')")
T11 = ("muhatap 2MP (adsız; 'llezîne âmenu' — nidâ, 2. ve 3. kelime; 'zkurû', ''aleykum', 'ileykum', ''ankum', 'ttequ'); Allah (lafız); 'qavmun' ('hemme' faili; nekre, 10. kelime); "
       "'yebsutû' faili 3MP (adsız; 12. kelime — gönderge 'qavm'); 'keffe' faili 3MS (adsız; 15. kelime — gönderge lafız); 'l-mu'minûn' ('yetevekkel' faili; belirli çoğul, 23. kelime)")

D = {}
D[7] = ("◇ 've'zkurû ni'meta'llâhi 'aleykum ve mîsâqahu'llezî vâsaqakum bihî iz qultum semi'nâ ve eta'nâ ve'ttequ'llâhe inna'llâhe 'alîmun bi-zâti's-sudûr' — "
 "'ve' + IMPV 2MP I. bab + 'ni'me' + lafız + ''alâ' + 2MP + 've' + 'mîsâq' + 3MS + 'ellezî' + PERF 3MS III. bab + 2MP + 'bi' + 3MS + 'iz' + PERF 2MP I. bab + PERF 1P I. bab + 've' + PERF 1P IV. bab + 've' + IMPV 2MP VIII. bab + lafız + 'inne' + lafız + nekre ''alîm' + 'bi' + 'zû' + belirli çoğul 'sadr' "
 "(ölçüm edim emir, kip IMPV 2; 1P 4 · 2MP 8 · 3MS 3; bab I. bab ×3 · III. bab ×1 · IV. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 3., 14. ve 16. sırada (ölçüm allah z=2,63); Rab yok; ölçüm esmâ '{{1|عَلِيم 17\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' (uyuşmuyor) — 'inna'llâhe 'alîmun bi-zâti's-sudûr', kural ''inne/enne' haberi → ilahi' (lafzın haberi) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=19 (n z=0,70); ölçüm '{{1|fâsıla ٱلصدور → ر, R sınıfı — KAFİYE KIRILMASI}}' — satır aynen; ölçüm '{{1|simetri \\[3, 3, 14, 1\\]}}' — satır aynen; ölçüm '{{1|harf 91 → harf3 85, isaret 6}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen. "
 "Ölçüm IMPV 2: 'zkurû' (1. kelime), 'ttequ' (13. kelime) (okuma); 'iz' (9. kelime) morph T — zaman (okuma). "
 "Kök ikilemeleri (ölçüm) أله ×3: lafız 3., 14. ve 16. kelimede; وثق ×2: 've mîsâqahu' (5. kelime) / 'vâsaqakum' (7. kelime) (okuma). "
 "'ve'zkurû' (1.), 've mîsâqahu' (5.), 've eta'nâ' (12.) ve 've'ttequ' (13.)'daki 've' morph CONJ (okuma). "
 + T7 + " (okuma). "
 + cumle(say('say 5:7 1-3 --on', "ve'zkurû ni'meta'llâh", True), say('say 5:7 1-4 --on', "ve'zkurû ni'meta'llâhi 'aleykum"), say('dizi 5 7 1 4', "zekera ni'me allâh 'alâ"), say('say 5:7 5-7 --on', "ve mîsâqahu'llezî vâsaqakum"), say('lem 5:7:5', "mîsâq"), say('lem 5:7:7', "vâsaqa")) + ' '
 + cumle(say('say 5:7 9-12', "iz qultum semi'nâ ve eta'nâ", True), say('say 5:7 11-12', "semi'nâ ve eta'nâ")) + ' '
 + cumle(say('say 5:7 13-15 --on', "ve'ttequ'llâhe inne", True), say('dizi 5 7 13 15', "itteqâ allâh inne"), say('say 5:7 13-16 --on', "ve'ttequ'llâhe inna'llâh"), say('say 5:7 15-19', "inna'llâhe 'alîmun bi-zâti's-sudûr"), say('say 5:7 17-19', "'alîmun bi-zâti's-sudûr")) + ' '
 "Ölçüm xref okunmuş iki ayet. Ölçüm nakarat3 üç kalıp: hepsi süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'semi'nâ' (11. kelime); B4 —.",
 "◈D — D1 've' + IMPV + izafet + lafız + ''alâ' + 've' + izafet + 'ellezî' + PERF + 'bi' + 'iz' + PERF + PERF + 've' + PERF + 've' + IMPV + lafız + 'inne' + lafız + nekre + 'bi' + izafet + belirli; D2 emir, IMPV ('zkurû' 1. kelime, 'ttequ' 13. kelime); D3 أله ×3 · وثق ×2; 2:285, 3:119 ve 24:51 eşleri; 5:4 sûre içi eşi; 5:8 ve 5:11 blok içi eşleri; D4 1P 4 · 2MP 8 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T7 + "; aktör yok (ölçüm); A2 nimeti anma; ahit; bağlama; işitme; itaat; sakınma; bilme; A3 'semi'nâ ve eta'nâ' (söz içi, 11-12. kelime); A4 " + BOLUM + "; edim geçişi emir, nida, şart → emir (ayetler arası); şahıs geçişi yok; söz açılır (11. kelime); söz kapanır (12. kelime, ayet içi).",
)

D[8] = ("◇ 'yâ eyyuhe'llezîne âmenû kûnû qavvâmîne li'llâhi şuhedâ'e bi'l-qısti ve lâ yecrimennekum şene'ânu qavmin 'alâ ellâ ta'dilu 'dilû huve aqrabu li't-taqvâ ve'ttequ'llâhe inna'llâhe xabîrun bimâ ta'melûn' — "
 "'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF 3MP IV. bab + IMPV 2MP I. bab + çoğul 'qavvâm' + 'li' + lafız + çoğul 'şehîd' + 'bi' + belirli 'qıst' + 've' + 'lâ' + IMPF 3MS I. bab + 'nûn' + 2MP + 'şene'ân' + nekre 'qavm' + ''alâ' + 'en' + 'lâ' + IMPF 2MP I. bab + IMPV 2MP I. bab + 'huve' + tafdîl 'aqrab' + 'li' + belirli 'taqvâ' + 've' + IMPV 2MP VIII. bab + lafız + 'inne' + lafız + nekre 'xabîr' + 'bi' + 'mâ' + IMPF 2MP I. bab "
 "(ölçüm edim emir, yasak, nida, kip EMPH 1 · IMPV 3 · NEG 1 · PRO 1 · VOC 1, biçim DIKKAT + NEHY; 2MP 11 · 3MP 2 · 3MS 2; bab I. bab ×5 · IV. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 6., 21. ve 23. sırada (ölçüm allah z=1,78); Rab yok; ölçüm esmâ '{{2|شَهِيد 7\\. sırada, ORTA konum, MÜHÜRSÜZ \\| خَبِير 24\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' (uyuşmuyor) — 'qavvâmîne li'llâhi şuhedâ'e', kural 'çoğul insan göndergeli → degil' (tanıklar); 'inna'llâhe xabîrun bimâ ta'melûn', kural ''inne/enne' haberi → ilahi' (lafzın haberi) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=26 (n z=1,44); ölçüm '{{2|biçim DIKKAT \\+ NEHY}}' — satır aynen; ölçüm '{{2|fâsıla تعملون → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|harf 127 → harf3 117, isaret 10}}' — satır aynen; ölçüm '{{2|dış düğüm 3}}' — satır aynen. "
 "Ölçüm EMPH 1: 'nûn' (10. kelime); IMPV 3: 'kûnû' (4. kelime), 'dilû' (16. kelime), 'ttequ' (20. kelime); NEG 1: 'lâ' (14. kelime, 'ellâ' içinde); PRO 1: 'lâ' (9. kelime); VOC 1: 'yâ' (1. kelime) (okuma); ölçüm biçim DIKKAT + NEHY — 'yâ eyyuhâ' nidâsı ve 've lâ yecrimennekum' yasağı; D2'de yazılmadı (okuma). "
 "Kök ikilemeleri (ölçüm) أله ×3: lafız 6., 21. ve 23. kelimede; عدل ×2: 'ta'dilu' (15. kelime) / 'dilû' (16. kelime); قوم ×2: 'qavvâmîne' (5. kelime) / 'qavmin' (12. kelime); وقي ×2: 'li't-taqvâ' (19. kelime) / 've'ttequ' (20. kelime) (okuma). "
 "'ve lâ' (9.)'daki 've' morph CONJ; 've'ttequ' (20.)'daki 've' REM (okuma). "
 + T8 + " (okuma). "
 + cumle(say('say 5:8 1-3', "yâ eyyuhe'llezîne âmenû", True), say('say 5:8 1-4', "yâ eyyuhe'llezîne âmenû kûnû"), say('say 5:8 4-8', "kûnû qavvâmîne li'llâhi şuhedâ'e bi'l-qıst"), say('dizi 5 8 4 8', "kâne qavvâm allâh şehîd qıst")) + ' '
 + cumle(say('say 5:8 9-12 --on', "ve lâ yecrimennekum şene'ânu qavm", True), say('say 5:8 13-15', "'alâ ellâ ta'dilû"), say('say 5:8 16-19', "dilû huve aqrabu li't-taqvâ"), say('say 5:8 18-19', "aqrabu li't-taqvâ")) + ' '
 + cumle(say('say 5:8 20-22 --on', "ve'ttequ'llâhe inne", True), say('dizi 5 8 20 22', "itteqâ allâh inne"), say('say 5:8 20-23 --on', "ve'ttequ'llâhe inna'llâh"), say('say 5:8 22-26', "inna'llâhe xabîrun bimâ ta'melûn"), say('say 5:8 24-26', "xabîrun bimâ ta'melûn")) + ' '
 "Ölçüm xref 4:135 ve 59:18 (basılmış), okunmuş bir ayet. Ölçüm nakarat3 dört kalıp: hepsi süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: ''alâ ellâ ta'dilu' / 'dilû huve aqrabu li't-taqvâ' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF + IMPV + çoğul + 'li' + lafız + çoğul + 'bi' + belirli + 've' + 'lâ' + IMPF + izafet + nekre + ''alâ' + 'en' + 'lâ' + IMPF + IMPV + 'huve' + tafdîl + 'li' + belirli + 've' + IMPV + lafız + 'inne' + lafız + nekre + 'bi' + 'mâ' + IMPF; D2 emir, yasak, nida, EMPH ('nûn' 10. kelime), IMPV ('kûnû' 4. kelime, 'dilû' 16. kelime, 'ttequ' 20. kelime), NEG ('lâ' 14. kelime), PRO ('lâ' 9. kelime), VOC ('yâ' 1. kelime); D3 أله ×3 · عدل ×2 · قوم ×2 · وقي ×2; 2:237, 4:135 ve 59:18 eşleri; 5:2 sûre içi eşi; 5:7 ve 5:11 blok içi eşleri; D4 2MP 11 · 3MP 2 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T8 + "; aktör yok (ölçüm); A2 adaleti ayakta tutma; tanıklık; kin; adaletsizlik; adalet; takvâya yakınlık; sakınma; haberdar olma; A3 —; A4 " + BOLUM + "; hitap açılır ('yâ eyyuhe'llezîne âmenû', 1-3. kelime); edim geçişi emir → emir, yasak, nida (ayetler arası); şahıs geçişi yok.",
)

D[9] = ("◇ 've'ade'llâhu'llezîne âmenû ve 'amilu's-sâlihâti lehum mağfiratun ve ecrun 'azîm' — "
 "PERF 3MS I. bab + lafız + 'ellezî' + PERF 3MP IV. bab + 've' + PERF 3MP I. bab + belirli çoğul etken ortaç 'sâliha' + 'li' + 3MP + nekre 'mağfire' + 've' + nekre 'ecr' + nekre ''azîm' "
 "(ölçüm edim haber, kip yok; 3MP 5 · 3MS 1; bab I. bab ×2 · IV. bab ×1). "
 "Allah lafzı 2. sırada (ölçüm allah z=1,47); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{3|yıldız yok}}' — satır aynen; n=10 (n z=-0,26); ölçüm '{{3|fâsıla عظيم → م, N sınıfı}}' — satır aynen; ölçüm '{{3|harf 51 → harf3 46, isaret 5}}' — satır aynen; ölçüm '{{3|dış düğüm 2}}' — satır aynen. "
 "'ve 'amilu' (5.) ve 've ecrun' (9.)'daki 've' morph CONJ; 've'ade' (1. kelime) kök وعد — 've' önek değil (okuma). "
 + T9 + " (okuma). "
 + cumle(say('say 5:9 1-4', "ve'ade'llâhu'llezîne âmenû", True), say('say 5:9 1-6', "ve'ade'llâhu'llezîne âmenû ve 'amilu's-sâlihât"), say('say 5:9 3-6', "llezîne âmenû ve 'amilu's-sâlihât")) + ' '
 + cumle(say('say 5:9 7-10', "lehum mağfiratun ve ecrun 'azîm", True), say('say 5:9 8-10', "mağfiratun ve ecrun 'azîm")) + ' '
 "Ölçüm xref 48:29 (basılmış), okunmuş bir ayet. Ölçüm nakarat3 bir kalıp: süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: 5:9 / 5:10 ('llezîne âmenû ve 'amilu's-sâlihâti' / 've'llezîne keferû ve kezzebû').",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + lafız + 'ellezî' + PERF + 've' + PERF + belirli + 'li' + nekre + 've' + nekre + nekre; D2 haber; D3 kök ikilemesi yok; 48:29 ve 49:3 eşleri; D4 3MP 5 · 3MS 1, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T9 + "; aktör yok (ölçüm); A2 vaat; iman; salih amel; bağışlanma; ödül; A3 vaat — bağışlanma ve büyük ödül (söz biçimli içerik, 7-10. kelime); A4 " + BOLUM + "; edim geçişi emir, yasak, nida → haber (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası).",
)

D[10] = ("◇ 've'llezîne keferû ve kezzebû bi-âyâtinâ ulâ'ike ashâbu'l-cahîm' — "
 "'ve' + 'ellezî' + PERF 3MP I. bab + 've' + PERF 3MP II. bab + 'bi' + çoğul 'âye' + 1P + 'ulâ'ike' + çoğul 'ashâb' + belirli 'cahîm' "
 "(ölçüm edim haber, kip yok; 1P 1 · 3MP 4; bab I. bab ×1 · II. bab ×1). "
 "Ölçüm '{{4|lafız YOK · Rab YOK}}' — satır aynen; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{4|yıldız yok}}' — satır aynen; n=7 (n z=-0,58); ölçüm '{{4|fâsıla ٱلجحيم → م, N sınıfı}}' — satır aynen; ölçüm '{{4|harf 42 → harf3 39, isaret 3}}' — satır aynen; ölçüm '{{4|dış düğüm 1}}' — satır aynen; ölçüm '{{4|nakarat 2 \\(temsil None\\)}}' — satır aynen; ölçüm esit2 alanı okunmamış bir ayetle (sûre içi 1) TAM kademe veriyor. "
 "'ve'llezîne' (1.)'deki 've' morph REM; 've kezzebû' (3.)'daki 've' CONJ (okuma). "
 + T10 + " (okuma). "
 + cumle(say('say 5:10 1-4 --on', "ve'llezîne keferû ve kezzebû bi-âyâtinâ", True), say('say 5:10 1-7 --on', "ve'llezîne keferû ve kezzebû bi-âyâtinâ ulâ'ike ashâbu'l-cahîm"), say('say 5:10 5-7', "ulâ'ike ashâbu'l-cahîm"), say('say 5:10 6-7', "ashâbu'l-cahîm")) + ' '
 "Ölçüm xref 57:19 (basılmış), okunmamış bir ayet (sûre içi 1). Ölçüm nakarat3 bir kalıp: süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: 5:9 / 5:10 ('llezîne âmenû ve 'amilu's-sâlihâti' / 've'llezîne keferû ve kezzebû').",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'ellezî' + PERF + 've' + PERF + 'bi' + izafet + 'ulâ'ike' + izafet + belirli; D2 haber; D3 kök ikilemesi yok; 2:39 ve 57:19 eşleri; D4 1P 1 · 3MP 4, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T10 + "; aktör yok (ölçüm); A2 inkâr; yalanlama; âyetler; ateş halkı; A3 —; A4 " + BOLUM + "; —.",
)

D[11] = ("◇ 'yâ eyyuhe'llezîne âmenu'zkurû ni'meta'llâhi 'aleykum iz hemme qavmun en yebsutû ileykum eydiyehum fe-keffe eydiyehum 'ankum ve'ttequ'llâhe ve 'ale'llâhi fe'l-yetevekkeli'l-mu'minûn' — "
 "'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF 3MP IV. bab + IMPV 2MP I. bab + 'ni'me' + lafız + ''alâ' + 2MP + 'iz' + PERF 3MS I. bab + nekre 'qavm' + 'en' + IMPF 3MP I. bab + 'ilâ' + 2MP + çoğul 'yed' + 3MP + 'fe' + PERF 3MS I. bab + çoğul 'yed' + 3MP + ''an' + 2MP + 've' + IMPV 2MP VIII. bab + lafız + 've' + ''alâ' + lafız + 'fe' + 'li' + IMPF 3MS V. bab + belirli çoğul etken ortaç 'mu'min' "
 "(ölçüm edim emir, nida, kip IMPV 3 · VOC 1, biçim DIKKAT; 2MP 7 · 3MP 6 · 3MS 3; bab I. bab ×4 · IV. bab ×1 · V. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 6., 19. ve 21. sırada (ölçüm allah z=2,08); Rab yok; ölçüm esmâ '{{5|مُؤْمِن 23\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton cemâl' (uyuşmuyor) — 'fe'l-yetevekkeli'l-mu'minûn', kural 'çoğul insan göndergeli → degil' (inananlar) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=23 (n z=1,12); ölçüm '{{5|biçim DIKKAT}}' — satır aynen; ölçüm '{{5|fâsıla ٱلمؤمنون → ن, N sınıfı}}' — satır aynen; ölçüm '{{5|simetri \\[3, 6, 19, 1\\]}}' — satır aynen; ölçüm '{{5|harf 113 → harf3 107, isaret 6}}' — satır aynen; ölçüm '{{5|dış düğüm 2}}' — satır aynen. "
 "Ölçüm IMPV 3: 'zkurû' (4. kelime), 'ttequ' (18. kelime), 'l-yetevekkel' (22. kelime, morph IMPV 'li'); VOC 1: 'yâ' (1. kelime) (okuma); ölçüm biçim DIKKAT — 'yâ eyyuhâ' nidâsı; D2'de yazılmadı (okuma); 'iz' (8. kelime) morph T — zaman; 'l-mu'minûn' (23. kelime) morph ACT_PCPL — ortaç, bab ◇'de yazılmadı (okuma). "
 "Kök ikilemeleri (ölçüm) أله ×3: lafız 6., 19. ve 21. kelimede; أمن ×2: 'âmenu' (3. kelime) / 'l-mu'minûn' (23. kelime); يدي ×2: 'eydiyehum' (14. ve 16. kelime) (okuma). "
 "'fe-keffe' (15.)'deki 'fe' morph CONJ; 've'ttequ' (18.)'daki 've' CONJ; 've 'ale'llâhi' (20.)'deki 've' REM; 'fe'l-yetevekkel' (22.)'deki 'fe' SUP (okuma). "
 + T11 + " (okuma). "
 + cumle(say('say 5:11 1-3', "yâ eyyuhe'llezîne âmenû", True), say('say 5:11 1-7', "yâ eyyuhe'llezîne âmenu'zkurû ni'meta'llâhi 'aleykum"), say('dizi 5 11 1 7', "eyy ellezî âmene zekera ni'me allâh 'alâ"), say('say 5:11 4-7', "zkurû ni'meta'llâhi 'aleykum"), say('dizi 5 11 4 7', "zekera ni'me allâh 'alâ"), say('say 5:11 4-8', "zkurû ni'meta'llâhi 'aleykum iz"), say('dizi 5 11 4 8', "zekera ni'me allâh 'alâ iz")) + ' '
 + cumle(say('say 5:11 8-14', "iz hemme qavmun en yebsutû ileykum eydiyehum", True), say('lem 5:11:9', "hemme"), say('say 5:11 15-17 --on', "fe-keffe eydiyehum 'ankum")) + ' '
 + cumle(say('say 5:11 18-19 --on', "ve'ttequ'llâh", True), say('say 5:11 20-22 --on', "ve 'ale'llâhi fe'l-yetevekkel"), say('dizi 5 11 20 22', "'alâ allâh tevekkel"), say('say 5:11 20-23 --on', "ve 'ale'llâhi fe'l-yetevekkeli'l-mu'minûn")) + ' '
 "Ölçüm xref 33:9 (basılmış), okunmuş bir ayet. Ölçüm nakarat3 dört kalıp: üçü süzgeç GEÇER, biri GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'en yebsutû ileykum eydiyehum' / 'fe-keffe eydiyehum 'ankum' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'eydiyehum' (14. ve 16. kelime); B4 —.",
 "◈D — D1 'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF + IMPV + izafet + lafız + ''alâ' + 'iz' + PERF + nekre + 'en' + IMPF + 'ilâ' + izafet + 'fe' + PERF + izafet + ''an' + 've' + IMPV + lafız + 've' + ''alâ' + lafız + 'fe' + 'li' + IMPF + belirli; D2 emir, nida, IMPV ('zkurû' 4. kelime, 'ttequ' 18. kelime, 'l-yetevekkel' 22. kelime), VOC ('yâ' 1. kelime); D3 أله ×3 · أمن ×2 · يدي ×2; 3:122, 33:9, 35:3 ve 64:13 eşleri; 5:7 ve 5:8 blok içi eşleri; D4 2MP 7 · 3MP 6 · 3MS 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T11 + "; aktör yok (ölçüm); A2 nimeti anma; yeltenme; el uzatma; el çekme; sakınma; tevekkül; A3 —; A4 " + BOLUM + "; hitap açılır ('yâ eyyuhe'llezîne âmenu', 1-3. kelime); edim geçişi haber → emir, nida (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası); bölüm kapanışı.",
)

out = ['# ── blok 5:7-11 (2026-11-15) ──', 'MEAL4 = {']
for n in range(7, 12):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M4 = {']
for n in range(7, 12):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL4); M.update(M4)']
open('/home/claude/yamalar/metin_5_7_11.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
