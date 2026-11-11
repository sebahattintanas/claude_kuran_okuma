# ÖRNEK (blok 19, 4:65-70): yeni blokta kopyalanır, BOLUM / MEAL / T / D / I içerikleri yeniden yazılır; sayim.py ve kes.py /home/claude/sunum'dan
# blok 19 (4:65-70) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b19/say2.txt'
os.environ['OLC'] = '/home/claude/b19/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Emanet ve adalet; itaat; tâğûta başvuranlar; itaat edenlerin yeri' bölümünde"

def cumle(*parts):
    return '; '.join(parts) + '.'

MEAL = {
 65: "Hayır, Rabbine andolsun ki aralarında çıkan anlaşmazlıkta seni hakem kılıp sonra verdiğin hükümden içlerinde hiçbir sıkıntı duymadan tam bir teslimiyetle teslim olmadıkça inanmazlar.",
 66: "Eğer onlara kendilerini öldürmelerini ya da yurtlarından çıkmalarını yazsaydık, içlerinden pek azı dışında bunu yapmazlardı. Kendilerine verilen öğüdü yapsalardı, bu onlar için daha hayırlı ve sağlamlaştırma bakımından daha güçlü olurdu.",
 67: "O zaman onlara katımızdan büyük bir ödül verirdik.",
 68: "Ve onları dosdoğru bir yola iletirdik.",
 69: "Kim Allah'a ve Elçi'ye itaat ederse, işte onlar Allah'ın nimet verdiği peygamberlerle, dosdoğrularla, şahitlerle ve iyilerle birliktedir. Onlar ne güzel arkadaştır.",
 70: "Bu lütuf Allah'tandır. Bilen olarak Allah yeter.",
}

T65 = "Rab ('rabbike' — kasem; muhatabın Rabbi); muhatap 2MS (adsız; 'yuhakkimûke', 'qadayte'); 'yu'minûne' / 'yuhakkimû' / 'yecidû' / 'yusellimû' faili 3MP (adsız)"
T66 = "konuşan 1P (adsız; 'ketebnâ'); 3MP (adsız; ''aleyhim', 'fe'alûhu', 'fe'alû', 'yû'azûne'); yazılan içerikte muhatap 2MP (adsız; 'qtulû', 'xrucû')"
T67 = "konuşan 1P (adsız; 'âteynâ'); 'âteynâhum' mef'ûlü 3MP (adsız)"
T68 = "konuşan 1P (adsız; 'hedeynâ'); 'hedeynâhum' mef'ûlü 3MP (adsız)"
T69 = "'yuti'' faili 3MS (adsız; şart 'men'); Allah (lafız); 'er-rasûl' ('yuti'' mef'ûlü); 'ulâ'ike' (işaret; gönderge 'men')"
T70 = "Allah (lafız)"

D = {}
D[65] = ("◇ 'fe-lâ ve rabbike lâ yu'minûne hattâ yuhakkimûke fîmâ şecere beynehum summe lâ yecidû fî enfusihim haracen mimmâ qadayte ve yusellimû teslîmâ' — "
 "'fe' + 'lâ' + 've' + 'rabb' + 2MS + 'lâ' + IMPF 3MP IV. bab + 'hattâ' + IMPF 3MP II. bab + 2MS + 'fî' + 'mâ' + PERF 3MS I. bab + 'beyne' + 3MP + 'summe' + 'lâ' + IMPF 3MP I. bab + 'fî' + çoğul 'nefs' + 3MP + nekre 'harac' + 'min' + 'mâ' + PERF 2MS I. bab + 've' + IMPF 3MP II. bab + nekre masdar 'teslîm' "
 "(ölçüm edim haber, kip NEG 3; 2MS 4 · 3MP 10 · 3MS 1; bab I. bab ×3 · II. bab ×2 · IV. bab ×1). "
 "Lafız yok; Rab 2. sırada (ölçüm rab z=0,80); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{1|yıldız yok}}' — satır aynen; n=19 (n z=0,70); ölçüm '{{1|biçim QASEM}}' — satır aynen; ölçüm '{{1|fâsıla تسليما → ا, A sınıfı}}' — satır aynen; ölçüm '{{1|mm2: \\[18, \\S+ \\*\\(esenlik; teslim olma\\)\\*\\]}}' — satır aynen; ölçüm '{{1|simetri \\[3, 1, 5, 1\\]}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen; ölçüm '{{1|bağ: YOK \\(esit2, nakarat3, xref üçü de boş\\)}}' — satır aynen. "
 "Ölçüm NEG 3: 'lâ' (1., 3. ve 11. kelime) (okuma). Ölçüm biçim alanı QASEM — D2'de yazılmadı; kasem 've rabbike' (2. kelime; 've' morph P) (okuma). "
 "Kök ikilemesi (ölçüm) سلم ×2: 've yusellimû' (18. kelime) / 'teslîmâ' (19. kelime) — mm2 ile (okuma). "
 "'fe-lâ' (1.)'daki 'fe' morph REM; 've rabbike' (2.)'deki 've' P (kasem); 'summe' (10.) CONJ; 've yusellimû' (18.)'daki 've' CONJ (okuma). "
 + T65 + " (okuma). "
 + cumle(say('say 4:65 1-4 --on', "fe-lâ ve rabbike lâ yu'minûn", True), say('say 4:65 2-2 --on', "ve rabbik"), say('say 4:65 3-4', "lâ yu'minûn"), say('say 4:65 3-6', "lâ yu'minûne hattâ yuhakkimûk"), say('lem 4:65:6', "yuhakkimu"), say('say 4:65 7-9', "fîmâ şecere beynehum"), say('lem 4:65:8', "şecere")) + ' '
 + cumle(say('say 4:65 10-15', "summe lâ yecidû fî enfusihim haracâ", True), say('say 4:65 12-15', "yecidû fî enfusihim haracâ"), say('lem 4:65:15', "harac"), say('say 4:65 16-17', "mimmâ qadayt"), say('say 4:65 18-19 --on', "ve yusellimû teslîmâ"), say('lem 4:65:19', "teslîm")) + ' '
 "Ölçüm xref yok; ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'fîmâ şecere beynehum' / 've yusellimû teslîmâ' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'şecere' (tetik شجر) — fiil, 'aralarında çıkan anlaşmazlık' anlamında, bitki değil; tetik aracı kökü mekanik okur; B2 —; B3 —; B4 —.",
 "◈D — D1 'fe' + 'lâ' + 've' + izafet + 'lâ' + IMPF + 'hattâ' + IMPF + 'fî' + 'mâ' + PERF + 'beyne' + 'summe' + 'lâ' + IMPF + 'fî' + izafet + nekre + 'min' + 'mâ' + PERF + 've' + IMPF + nekre; D2 haber, NEG ('lâ' 1., 3. ve 11. kelime); D3 سلم ×2; 33:37 ve 33:56 eşleri; D4 2MS 4 · 3MP 10 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T65 + "; aktör yok (ölçüm); A2 kasem; inanma; hakem kılma; anlaşmazlık; sıkıntı; hüküm; teslim olma; A3 —; A4 " + BOLUM + "; edim geçişi şart → haber (ayetler arası); şahıs geçişi yok.",
)

D[66] = ("◇ 've lev ennâ ketebnâ 'aleyhim eni'qtulû enfusekum evi'xrucû min diyârikum mâ fe'alûhu illâ qalîlun minhum ve lev ennehum fe'alû mâ yû'azûne bihî le-kâne xayran lehum ve eşedde tesbîtâ' — "
 "'ve' + 'lev' + 'enne' + 1P + PERF 1P I. bab + ''alâ' + 3MP + 'en' + IMPV 2MP I. bab + çoğul 'nefs' + 2MP + 'ev' + IMPV 2MP I. bab + 'min' + çoğul 'dâr' + 2MP + 'mâ' + PERF 3MP I. bab + 3MS + 'illâ' + nekre 'qalîl' + 'min' + 3MP + 've' + 'lev' + 'enne' + 3MP + PERF 3MP I. bab + 'mâ' + edilgen IMPF 3MP I. bab + 'bi' + 3MS + 'le' + PERF 3MS I. bab + nekre 'xayr' + 'li' + 3MP + 've' + tafdîl 'eşedd' + nekre masdar 'tesbît' "
 "(ölçüm edim emir, şart, kip COND 2 · EMPH 1 · IMPV 2 · NEG 1 · RES 1; 1P 3 · 2MP 6 · 3MP 10 · 3MS 3; bab I. bab ×7). "
 "Ölçüm '{{2|lafız YOK · Rab YOK}}' — satır aynen; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=27 (n z=1,55); ölçüm '{{2|biçim HASR}}' — satır aynen; ölçüm '{{2|fâsıla تثبيتا → ا, A sınıfı}}' — satır aynen; ölçüm '{{2|EDİLGEN 1/7 fiil, pas z=0,48}}' — satır aynen; ölçüm '{{2|sayı işareti \\S+}}' — satır aynen; ölçüm '{{2|simetri \\[6, 8, 14, 2\\]}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm COND 2: 'lev' (1. ve 17. kelime); EMPH 1: 'le' (23. kelime); IMPV 2: 'qtulû' (6. kelime), 'xrucû' (9. kelime) — yazılan içerik ('en' 5. kelime, morph INT); NEG 1: 'mâ' (12. kelime); RES 1: 'illâ' (14. kelime) (okuma); edilgen 'yû'azûne' (21. kelime) (okuma). Ölçüm biçim alanı HASR — D2'de yazılmadı (okuma). "
 "Kök ikilemesi (ölçüm) فعل ×2: 'fe'alûhu' (13. kelime) / 'fe'alû' (19. kelime) (okuma). "
 "'ve lev' (1.)'deki 've' morph REM; 'ev' (8.) CONJ; 've lev' (17.) ve 've eşedde' (26.)'deki 've' CONJ (okuma). "
 + T66 + " (okuma). "
 + cumle(say('say 4:66 1-4 --on', "ve lev ennâ ketebnâ 'aleyhim", True), say('say 4:66 3-4', "ketebnâ 'aleyhim"), say('say 4:66 5-7', "eni'qtulû enfusekum"), say('say 4:66 6-7', "qtulû enfusekum"), say('say 4:66 8-11', "evi'xrucû min diyârikum"), say('say 4:66 9-11', "xrucû min diyârikum")) + ' '
 + cumle(say('say 4:66 12-16', "mâ fe'alûhu illâ qalîlun minhum", True), say('say 4:66 14-16', "illâ qalîlun minhum"), say('say 4:66 17-19 --on', "ve lev ennehum fe'alû"), say('say 4:66 20-22', "mâ yû'azûne bih")) + ' '
 + cumle(say('say 4:66 23-25', "le-kâne xayran lehum", True), say('say 4:66 24-25', "xayran lehum"), say('say 4:66 26-27 --on', "ve eşedde tesbîtâ"), say('lem 4:66:27', "tesbît")) + ' '
 "Ölçüm xref yok. Ölçüm nakarat3 bir kalıp: süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'mâ fe'alûhu illâ qalîlun minhum' / 've lev ennehum fe'alû' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'lev' + 'enne' + PERF + ''alâ' + 'en' + IMPV + izafet + 'ev' + IMPV + 'min' + izafet + 'mâ' + PERF + 'illâ' + nekre + 'min' + 've' + 'lev' + 'enne' + PERF + 'mâ' + IMPF + 'bi' + 'le' + PERF + nekre + 'li' + 've' + tafdîl + nekre; D2 emir, şart, COND ('lev' 1. ve 17. kelime), EMPH ('le'), IMPV ('qtulû', 'xrucû'), NEG ('mâ'), RES ('illâ'); D3 فعل ×2; 2:265 ve 47:21 eşleri; 4:46 sûre içi eşi; D4 1P 3 · 2MP 6 · 3MP 10 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T66 + "; aktör yok (ölçüm); A2 yazma; öldürme; çıkma; yapma; öğüt; hayır; sağlamlaştırma; A3 —; A4 " + BOLUM + "; edim geçişi haber → emir, şart (ayetler arası); şahıs geçişi yok; şart → cevap (ayet içi; 've lev ennâ ketebnâ …' / 'mâ fe'alûhu'; 've lev ennehum fe'alû …' / 'le-kâne xayran lehum').",
)

D[67] = ("◇ 've izen le-âteynâhum min ledunnâ ecran 'azîmâ' — "
 "'ve' + 'izen' + 'le' + PERF 1P IV. bab + 3MP + 'min' + 'ledun' + 1P + nekre 'ecr' + nekre ''azîm' "
 "(ölçüm edim haber, kip EMPH 1; 1P 3 · 3MP 1; bab IV. bab ×1). "
 "Ölçüm '{{3|lafız YOK · Rab YOK}}' — satır aynen; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{3|yıldız yok}}' — satır aynen; n=6 (n z=-0,68); ölçüm '{{3|fâsıla عظيما → ا, A sınıfı}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm EMPH 1: 'le' (2. kelime) (okuma); 'izen' (1. kelime) morph ANS (okuma). "
 "'ve izen' (1.)'deki 've' morph REM (okuma). "
 + T67 + " (okuma). "
 + cumle(say('say 4:67 1-2 --on', "ve izen le-âteynâhum", True), say('say 4:67 2-6', "le-âteynâhum min ledunnâ ecran 'azîmâ"), say('say 4:67 3-6', "min ledunnâ ecran 'azîmâ"), say('say 4:67 3-4', "min ledunnâ"), say('say 4:67 5-6', "ecran 'azîmâ")) + ' '
 "Ölçüm xref yok. Ölçüm nakarat3 bir kalıp: süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'izen' + 'le' + PERF + 'min' + izafet + nekre + nekre; D2 haber, EMPH ('le'); D3 kök ikilemesi yok; 21:17 eşi; 4:40 sûre içi eşi; D4 1P 3 · 3MP 1, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T67 + "; aktör yok (ölçüm); A2 verme; ödül; A3 —; A4 " + BOLUM + "; edim geçişi emir, şart → haber (ayetler arası); şahıs geçişi 3 → 1 (ayetler arası).",
)

D[68] = ("◇ 've le-hedeynâhum sırâtan mustaqîmâ' — "
 "'ve' + 'le' + PERF 1P I. bab + 3MP + nekre 'sırât' + nekre etken ortaç 'mustaqîm' "
 "(ölçüm edim haber, kip EMPH 1; 1P 2 · 3MP 1; bab I. bab ×1). "
 "Ölçüm '{{4|lafız YOK · Rab YOK}}' — satır aynen; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{4|yıldız yok}}' — satır aynen; n=3 (n z=-1,00); ölçüm '{{4|fâsıla مستقيما → ا, A sınıfı}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen; ölçüm '{{4|bağ: YOK \\(esit2, nakarat3, xref üçü de boş\\)}}' — satır aynen. "
 "Ölçüm EMPH 1: 'le' (1. kelime) (okuma). "
 "'ve le-hedeynâhum' (1.)'deki 've' morph CONJ (okuma). "
 + T68 + " (okuma). "
 + cumle(say('say 4:68 1-1 --on', "ve le-hedeynâhum", True), say('say 4:68 1-3 --on', "ve le-hedeynâhum sırâtan mustaqîmâ"), say('say 4:68 2-3', "sırâtan mustaqîmâ")) + ' '
 "Ölçüm xref yok; ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'le' + PERF + nekre + nekre; D2 haber, EMPH ('le'); D3 kök ikilemesi yok; 48:2 eşi; D4 1P 2 · 3MP 1, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T68 + "; aktör yok (ölçüm); A2 yola iletme; A3 —; A4 " + BOLUM + "; şahıs geçişi yok.",
)

D[69] = ("◇ 've men yuti'i'llâhe ve'r-rasûle fe-ulâ'ike ma'a'llezîne en'ame'llâhu 'aleyhim mine'n-nebiyyîne ve's-sıddîqîne ve'ş-şuhedâ'i ve's-sâlihîne ve hasune ulâ'ike rafîqâ' — "
 "'ve' + 'men' + IMPF 3MS IV. bab + lafız + 've' + belirli 'rasûl' + 'fe' + 'ulâ'ike' + 'ma'a' + 'ellezîne' + PERF 3MS IV. bab + lafız + ''alâ' + 3MP + 'min' + belirli çoğul 'nebiyy' + 've' + belirli çoğul 'sıddîq' + 've' + belirli çoğul 'şehîd' + 've' + belirli çoğul etken ortaç 'sâlih' + 've' + PERF 3MS I. bab + 'ulâ'ike' + nekre 'rafîq' "
 "(ölçüm edim şart, kip COND 1; 3MP 1 · 3MS 3; bab I. bab ×1 · IV. bab ×2). "
 "Allah lafzı 3. ve 9. sırada (ölçüm allah z=1,69); Rab yok; ölçüm esmâ '{{5|\\S+ 14\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' (uyuşmuyor) — 've'ş-şuhedâ'i', kural 'esmâ adı esmâ dışı göndergeyle → degil' (insan göndergeli, çoğul) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=18 (n z=0,59); ölçüm '{{5|fâsıla رفيقا → ا, A sınıfı}}' — satır aynen; ölçüm '{{5|simetri \\[3, 1, 7, 1\\]}}' — satır aynen; ölçüm '{{5|dış düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 'men' (1. kelime) (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2: lafız 3. ve 9. kelimede (okuma). "
 "'ve men' (1.) ve 've hasune' (16.)'daki 've' morph REM; 've'r-rasûle' (4.), 've's-sıddîqîne' (13.), 've'ş-şuhedâ'i' (14.) ve 've's-sâlihîne' (15.)'deki 've' CONJ; 'fe-ulâ'ike' (5.)'deki 'fe' RSLT (okuma). "
 + T69 + " (okuma). "
 + cumle(say('say 4:69 1-4 --on', "ve men yuti'i'llâhe ve'r-rasûl", True), say('say 4:69 2-4', "yuti'i'llâhe ve'r-rasûl"), say('say 4:69 5-10 --on', "fe-ulâ'ike ma'a'llezîne en'ame'llâhu 'aleyhim"), say('say 4:69 7-10', "ellezîne en'ame'llâhu 'aleyhim")) + ' '
 + cumle(say('say 4:69 11-15', "mine'n-nebiyyîne ve's-sıddîqîne ve'ş-şuhedâ'i ve's-sâlihîn", True), say('say 4:69 12-13', "en-nebiyyîne ve's-sıddîqîn"), say('say 4:69 16-18 --on', "ve hasune ulâ'ike rafîqâ"), say('say 4:69 17-18', "ulâ'ike rafîqâ"), say('lem 4:69:18', "rafîq")) + ' '
 "Ölçüm xref 19:58 (basılmış). Ölçüm nakarat3 bir kalıp: süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'men' + IMPF + lafız + 've' + belirli + 'fe' + 'ulâ'ike' + 'ma'a' + 'ellezîne' + PERF + lafız + ''alâ' + 'min' + belirli + 've' + belirli + 've' + belirli + 've' + belirli + 've' + PERF + 'ulâ'ike' + nekre; D2 şart, COND ('men'); D3 أله ×2; 19:58 eşi; D4 3MP 1 · 3MS 3, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T69 + "; aktör yok (ölçüm); A2 itaat; nimet verme; birliktelik; arkadaşlık; A3 —; A4 " + BOLUM + "; edim geçişi haber → şart (ayetler arası); şahıs geçişi 1 → 3 (ayetler arası); şart → cevap (ayet içi; 've men yuti'i'llâhe ve'r-rasûl' / 'fe-ulâ'ike …').",
)

D[70] = ("◇ 'zâlike'l-fadlu mine'llâhi ve kefâ bi'llâhi 'alîmâ' — "
 "'zâlike' + belirli 'fadl' + 'min' + lafız + 've' + PERF 3MS I. bab + 'bi' + lafız + nekre ''alîm' "
 "(ölçüm edim haber, kip yok; 3MS 1; bab I. bab ×1). "
 "Allah lafzı 4. ve 6. sırada (ölçüm allah z=5,18); Rab yok; ölçüm esmâ '{{6|\\S+ 7\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' (uyuşmuyor) — 've kefâ bi'llâhi 'alîmâ', kural ''kefâ bi'llâhi X' temyizi → ilahi' (sûre 4 oturum 1 kullanıcı kararı, onaya açık) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=7 (n z=-0,58); ölçüm '{{6|fâsıla عليما → ا, A sınıfı}}' — satır aynen; ölçüm '{{6|dış düğüm 3 · İÇ düğüm 1}}' — satır aynen. "
 "Kök ikilemesi (ölçüm) أله ×2: lafız 4. ve 6. kelimede (okuma). "
 "'ve kefâ' (5.)'daki 've' morph REM (okuma). "
 + T70 + " (okuma). "
 + cumle(say('say 4:70 1-4', "zâlike'l-fadlu mine'llâh", True), say('say 4:70 2-4', "el-fadlu mine'llâh"), say('say 4:70 4-6', "llâhi ve kefâ bi'llâh"), say('say 4:70 5-6 --on', "ve kefâ bi'llâh"), say('say 4:70 5-7 --on', "ve kefâ bi'llâhi 'alîmâ"), say('say 4:70 6-7', "bi'llâhi 'alîmâ")) + ' '
 "Ölçüm xref 33:3 (basılmış), okunmuş iki ayet, okunmamış bir ayet (sûre içi 1). Ölçüm nakarat3 iki kalıp: hepsi süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'zâlike' + belirli + 'min' + lafız + 've' + PERF + 'bi' + lafız + nekre; D2 haber; D3 أله ×2; 33:3 eşi; 4:45 sûre içi eşi; D4 3MS 1, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T70 + "; aktör yok (ölçüm); A2 lütuf; yetme; bilme; A3 —; A4 " + BOLUM + "; bölüm kapanışı; edim geçişi şart → haber (ayetler arası); şahıs geçişi yok.",
)

out = ['# ── blok 4:65-70 (2026-11-10) ──', 'MEAL19 = {']
for n in range(65, 71):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M19 = {']
for n in range(65, 71):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL19); M.update(M19)']
open('/home/claude/yamalar/metin_4_65_70.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
