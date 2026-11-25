# sûre 7 blok 11 (7:38-41) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b11/say2.txt'
os.environ['OLC'] = '/home/claude/b11/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Elçiler gelince; yalanlayanların ateşte çekişmesi' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK3 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[2]).group(0))
_AK4 = _esc(re.search(r'aktör: adlı .*?rol mecrur\)', _OL[3]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 38: "Dedi ki: Sizden önce gelip geçmiş cinlerden ve insanlardan ümmetler arasında ateşe girin. Bir ümmet girdikçe kardeşine lânet etti. Nihayet hepsi orada birbirine yetiştiğinde sonrakileri evvelkileri için dedi ki: Rabbimiz, bizi bunlar saptırdı; onlara ateşten iki kat azap ver. Dedi ki: Herkes için iki kat vardır, fakat bilmiyorsunuz.",
 39: "Evvelkileri de sonrakileri için dedi ki: Sizin bize bir üstünlüğünüz olmadı; kazanmakta olduklarınızdan dolayı azabı tadın.",
 40: "Gerçekten âyetlerimizi yalanlayıp onlara karşı büyüklenenlere göğün kapıları açılmaz ve deve iğnenin deliğine girinceye kadar bahçeye girmezler. Suçluları böyle cezalandırırız.",
 41: "Onlar için cehennemden bir döşek ve üstlerinde örtüler vardır. Zalimleri böyle cezalandırırız.",
}

T = {}
T[38] = ("'qâle' 3MS (adsız; tartışmalı; gönderge 7:37 6. kelime, 1. kelime); muhatap 2MP (adsız; söz içi; 'dxulû' — 2. kelime); 'xalet' 3FS (adsız; söz içi; gönderge 'umemin' 4. kelime, 6. kelime); muhatap 2MP eki (adsız; söz içi; 'qablikum' — 8. kelime); "
         "'dexalet' 3FS (fiil uyumu; 15. kelime — fail 16. kelime); 'le'anet' 3FS (adsız; gönderge 'ummetun' 16. kelime, 17. kelime); 'uxtehâ' 3FS eki (adsız; gönderge 'ummetun' 16. kelime, 18. kelime); "
         "muhatap 2MP (adsız; 'ddârakû' — 21. kelime; morph IMPV 2MP etiketi korundu, okuma PERF 3MP; tartışmalı; cins uyumsuz; gönderge 'umemin' 4. kelime); 'fîhâ' 3FS eki (adsız; gönderge 'n-nâri' 13. kelime, 22. kelime); 'qâlet' 3FS (fiil uyumu; 24. kelime — fail 25. kelime); "
         "'uxrâhum', 'li-ûlâhum' 3MP eki (adsız; tartışmalı; cins uyumsuz; gönderge 'umemin' 4. kelime — 25. ve 26. kelime); konuşan 1P eki (adsız; söz içi; 'rabbenâ', 'edallûnâ' — 27. ve 29. kelime); 'edallûnâ' 3MP (adsız; söz içi; gönderge 'hâ'ulâ'i' 28. kelime, 29. kelime); "
         "muhatap 2MS (adsız; söz içi; 'fe-âtihim' — 30. kelime); 'fe-âtihim' 3MP eki (adsız; söz içi; gönderge 'hâ'ulâ'i' 28. kelime, 30. kelime); 'qâle' 3MS (adsız; tartışmalı; gönderge 7:37 6. kelime, 35. kelime); 'dı'fun' 37. kelime (söz içi mübteda; 35. kelime — fail 37. kelime okuması alınmadı); muhatap 2MP (adsız; söz içi; 'ta'lemûn' — 40. kelime)")
T[39] = ("'ve qâlet' 3FS (fiil uyumu; 1. kelime — fail 2. kelime); 'ûlâhum', 'li-uxrâhum' 3MP eki (adsız; tartışmalı; cins uyumsuz; gönderge 7:38 4. kelime — 2. ve 3. kelime); 'kâne' 3MS (fiil uyumu; söz içi; 5. kelime — fail 9. kelime); "
         "muhatap 2MP eki (adsız; söz içi; 'lekum' — 6. kelime); konuşan 1P eki (adsız; söz içi; ''aleynâ' — 7. kelime); muhatap 2MP (adsız; söz içi; 'fe-zûqu', 'kuntum', 'teksibûn' — 10., 13. ve 14. kelime)")
T[40] = ("'kezzebû', 've'stekberû', 'yedxulûne' 3MP (adsız; gönderge 'llezîne' 2. kelime — 3., 5. ve 13. kelime); konuşan 1P eki (adsız; 'bi-âyâtinâ' — 4. kelime); ''anhâ' 3FS eki (adsız; gönderge 'bi-âyâtinâ' 4. kelime, 6. kelime); "
         "'tufettehu' 3FS (adsız; edilgen, naib-i faili 'ebvâbu' 10. kelime, 8. kelime); 'lehum' 3MP eki (adsız; gönderge 'llezîne' 2. kelime, 9. kelime); 'yelice' 3MS (fiil uyumu; 16. kelime — fail 17. kelime); konuşan 1P (adsız; 'neczi' — 22. kelime)")
T[41] = ("'lehum', 'fevqıhim' 3MP eki (adsız; gönderge 7:40 2. kelime — 1. ve 6. kelime); konuşan 1P (adsız; 'neczi' — 9. kelime)")

D = {}
D[38] = ("◇ 'qâle'dxulû fî umemin qad xalet min qablikum mine'l-cinni ve'l-insi fi'n-nâri kullemâ dexalet ummetun le'anet uxtehâ hattâ ize'ddârakû fîhâ cemî'an qâlet uxrâhum li-ûlâhum rabbenâ hâ'ulâ'i edallûnâ fe-âtihim 'azâben dı'fen mine'n-nâri qâle li-kullin dı'fun ve lâkin lâ ta'lemûn' — "
 "PERF 3MS I. bab + IMPV 2MP I. bab + 'fî' + nekre çoğul 'umme' + 'qad' + PERF 3FS I. bab + 'min' + 'qabl' + 2MP + 'min' + belirli 'cinn' + 've' + belirli 'ins' + 'fî' + belirli 'nâr' + 'kullemâ' + PERF 3FS I. bab + nekre 'umme' + PERF 3FS I. bab + 'uxt' + 3FS + 'hattâ' + 'izâ' + IMPV 2MP VI. bab + 'fî' + 3FS + nekre 'cemî'' + "
 "PERF 3FS I. bab + 'âxar' + 3MP + 'li' + 'evvel' + 3MP + 'rabb' + 1P + 'hâ' + 'ulâ'i' + PERF 3MP IV. bab + 1P + 'fe' + IMPV 2MS IV. bab + 3MP + nekre ''azâb' + nekre 'dı'f' + 'min' + belirli 'nâr' + PERF 3MS I. bab + 'li' + nekre 'kull' + nekre 'dı'f' + 've' + 'lâkin' + 'lâ' + IMPF 2MP I. bab "
 "(ölçüm edim emir, kip CERT 1 · IMPV 3 · NEG 1; 1P 2 · 2MP 7 · 2MS 1 · 3FS 6 · 3MP 5 · 3MS 2; bab I. bab ×8 · IV. bab ×2 · VI. bab ×1). "
 "Allah lafzı yok; Rab 27. sırada (ölçüm rab z=0,21); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); esma_el kaydı 'degil' — 'qâlet uxrâhum li-ûlâhum', kural 'esmâ adı esmâ dışı göndergeyle → degil' (ümmetlerin evvelkileri) (okuma). "
 "Ölçüm '{{1|yıldız ★★}}' — satır aynen (kaynak n, z=2,93); n=40 (n z=2,93); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:37 ن → 7:38 ن); "
 "ölçüm '{{1|simetri \\[3, 3, 7, 1\\]}}' — satır aynen; ölçüm '{{1|harf 174 → harf3 162, isaret 12}}' — satır aynen; ölçüm '{{1|dış düğüm 3}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (5. kelime); IMPV 3: 'dxulû' (2. kelime), 'ddârakû' (21. kelime; morph IMPV 2MP etiketi korundu, okuma PERF 3MP), 'fe-âtihim' (30. kelime); NEG 1: 'lâ' (39. kelime); ölçüm biçim DIKKAT; "
 "'ve'l-insi' (11.) kelimesindeki 've' CONJ; 'kullemâ' (14.) T; 'hattâ' (19.) INC; 'ize' (20.) T; 'hâ'ulâ'i' (28.) ATT + DEM; 'fe-âtihim' (30.) kelimesindeki 'fe' REM; 've lâkin' (38.) REM + AMD (okuma). "
 "Kök ikilemesi (ölçüm) أمم ×2 ('umemin' 4. / 'ummetun' 16. kelime); دخل ×2 ('dxulû' 2. / 'dexalet' 15. kelime); ضعف ×2 ('dı'fen' 32. / 'dı'fun' 37. kelime); قول ×3 ('qâle' 1. / 'qâlet' 24. / 'qâle' 35. kelime); كلل ×2 ('kullemâ' 14. / 'li-kullin' 36. kelime); نور ×2 ('n-nâri' 13. / 'n-nâri' 34. kelime) (okuma). "
 + T[38] + " (okuma). "
 + cumle(say('say 7:38 2-13', "dxulû fî umemin qad xalet min qablikum mine'l-cinni ve'l-insi fi'n-nâri", True), say('say 7:38 9-11', "mine'l-cinni ve'l-insi"), say('dizi 7 38 9 11', "min cinn ins"), say('dizi 7 38 3 11', "fî umme qad xalâ min qabl min cinn ins")) + ' '
 + cumle(say('say 7:38 14-18', "kullemâ dexalet ummetun le'anet uxtehâ", True), say('say 7:38 19-23', "hattâ ize'ddârakû fîhâ cemî'an"), say('say 7:38 24-26', "qâlet uxrâhum li-ûlâhum")) + ' '
 + cumle(say('say 7:38 28-29', "hâ'ulâ'i edallûnâ", True), say('say 7:38 30-34', "fe-âtihim 'azâben dı'fen mine'n-nâri"), say('say 7:38 31-32', "'azâben dı'fen"), say('dizi 7 38 31 32', "'azâb dı'f")) + ' '
 + cumle(say('say 7:38 36-37', "li-kullin dı'fun", True), say('say 7:38 38-40', "ve lâkin lâ ta'lemûn")) + ' ' +
 "Ölçüm xref 41:25 (emsal olarak basıldı), 46:18 (emsal olarak basıldı), 38:61 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı: 'min cinn ins' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'l-insi' (11. kelime).",
 "◈D — D1 PERF + IMPV + 'fî' + nekre + 'qad' + PERF + 'min' + izafet + 'min' + belirli + 've' + belirli + 'fî' + belirli + 'kullemâ' + PERF + nekre + PERF + izafet + 'hattâ' + 'izâ' + IMPV + 'fî' + nekre + PERF + izafet + 'li' + izafet + izafet + 'hâ' + 'ulâ'i' + PERF + 'fe' + IMPV + nekre + nekre + 'min' + belirli + PERF + 'li' + nekre + nekre + 've' + 'lâkin' + 'lâ' + IMPF; "
 "D2 emir; CERT ('qad' 5. kelime), IMPV ('dxulû' 2. kelime, 'ddârakû' 21. kelime, 'fe-âtihim' 30. kelime), NEG ('lâ' 39. kelime); D3 41:25 eşi, 46:18 eşi, 38:61 eşi, أمم ×2, دخل ×2, ضعف ×2, قول ×3, كلل ×2, نور ×2; D4 1P 2 · 2MP 7 · 2MS 1 · 3FS 6 · 3MP 5 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[38] + "; aktör yok (ölçüm); A2 daha önce geçmiş cin ve insan ümmetleri arasında ateşe girme emri; giren ümmetin kardeşine lâneti; orada yetişince sonrakilerin evvelkiler için iki kat azap dileği; herkes için iki kat oluşu; "
 "A3 'dxulû fî umemin qad xalet min qablikum mine'l-cinni ve'l-insi fi'n-nâri' (söz içi, 2-13. kelime); 'rabbenâ hâ'ulâ'i edallûnâ fe-âtihim 'azâben dı'fen mine'n-nâri' (söz içi, 27-34. kelime); 'li-kullin dı'fun ve lâkin lâ ta'lemûn' (söz içi, 36-40. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (13. kelime, ayet içi); söz açılır (27. kelime); söz kapanır (34. kelime, ayet içi); söz açılır (36. kelime); söz kapanır (40. kelime, ayet içi); muhatap geçişi 2MP → 2MS (ayet içi, 'dxulû' / 'fe-âtihim'); muhatap geçişi 2MS → 2MP (ayet içi, 'fe-âtihim' / 'ta'lemûn'); "
 "şahıs geçişi 3 → 2 (ayetler arası); şahıs sayısında toplam farkı (2MP 7 · 2MS 1 · 3. şahıs 13 — ölçüm baskın 2); edim geçişi soru → emir (ayetler arası).",
)

D[39] = ("◇ 've qâlet ûlâhum li-uxrâhum fe-mâ kâne lekum 'aleynâ min fadlin fe-zûqu'l-'azâbe bimâ kuntum teksibûn' — "
 "'ve' + PERF 3FS I. bab + 'evvel' + 3MP + 'li' + 'âxar' + 3MP + 'fe' + 'mâ' + PERF 3MS I. bab + 'li' + 2MP + ''alâ' + 1P + 'min' + nekre 'fadl' + 'fe' + IMPV 2MP I. bab + belirli ''azâb' + 'bi' + 'mâ' + PERF 2MP I. bab + IMPF 2MP I. bab "
 "(ölçüm edim emir, kip IMPV 1 · NEG 1; 1P 1 · 2MP 7 · 3FS 1 · 3MP 2 · 3MS 1; bab I. bab ×5). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); esma_el kaydı 'degil' — 've qâlet ûlâhum li-uxrâhum', kural 'esmâ adı esmâ dışı göndergeyle → degil' (ümmetlerin evvelkileri) (okuma). "
 "Ölçüm 'yıldız yok' — satır aynen; n=14 (n z=0,17); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:38 ن → 7:39 ن); "
 "ölçüm '{{2|simetri \\[3, 4, 12, 1\\]}}' — satır aynen; ölçüm '{{2|harf 64 → harf3 62, isaret 2}}' — satır aynen; ölçüm '{{2|dış düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 1: 'fe-zûqu' (10. kelime); NEG 1: 'fe-mâ' (4. kelime; 'mâ'); "
 "'ve qâlet' (1.) kelimesindeki 've' CONJ; 'fe-mâ' (4.) kelimesindeki 'fe' CONJ; 'fe-zûqu' (10.) kelimesindeki 'fe' REM; 'bimâ' (12.) P + REL (okuma). "
 "Kök ikilemesi (ölçüm) كون ×2 ('kâne' 5. / 'kuntum' 13. kelime) (okuma). "
 + T[39] + " (okuma). "
 + cumle(say('say 7:39 1-3', "ve qâlet ûlâhum li-uxrâhum", True), say('say 7:39 4-9', "fe-mâ kâne lekum 'aleynâ min fadlin")) + ' '
 + cumle(say('say 7:39 10-14', "fe-zûqu'l-'azâbe bimâ kuntum teksibûn", True), say('say 7:39 10-11', "fe-zûqu'l-'azâbe"), say('say 7:39 12-14', "bimâ kuntum teksibûn"), say('dizi 7 39 12 14', "mâ kâne kesebe")) + ' ' +
 "Ölçüm xref okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'bi-mâ kâne kesebe' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + PERF + izafet + 'li' + izafet + 'fe' + 'mâ' + PERF + 'li' + ''alâ' + 'min' + nekre + 'fe' + IMPV + belirli + 'bi' + 'mâ' + PERF + IMPF; "
 "D2 emir; IMPV ('fe-zûqu' 10. kelime), NEG ('fe-mâ' 4. kelime); D3 كون ×2; D4 1P 1 · 2MP 7 · 3FS 1 · 3MP 2 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[39] + "; aktör yok (ölçüm); A2 evvelkilerin sonrakilere cevabı: üstünlük olmayışı ve kazanılanlardan dolayı azabı tatma emri; "
 "A3 'fe-mâ kâne lekum 'aleynâ min fadlin fe-zûqu'l-'azâbe bimâ kuntum teksibûn' (söz içi, 4-14. kelime); "
 "A4 " + BOLUM + "; söz açılır (4. kelime); söz kapanır (14. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[40] = ("◇ 'inne'llezîne kezzebû bi-âyâtinâ ve'stekberû 'anhâ lâ tufettehu lehum ebvâbu's-semâ'i ve lâ yedxulûne'l-cennete hattâ yelice'l-cemelu fî semmi'l-xiyâti ve kezâlike neczi'l-mucrimîn' — "
 "'inne' + 'ellezî' + PERF 3MP II. bab + 'bi' + çoğul 'âye' + 1P + 've' + PERF 3MP X. bab + ''an' + 3FS + 'lâ' + IMPF 3FS II. bab edilgen + 'li' + 3MP + çoğul 'bâb' + belirli 'semâ'' + 've' + 'lâ' + IMPF 3MP I. bab + belirli 'cenne' + 'hattâ' + IMPF 3MS I. bab + belirli 'cemel' + 'fî' + 'semm' + belirli 'xiyât' + "
 "'ve' + 'ke' + 'zâ' + IMPF 1P I. bab + belirli çoğul etken ortaç 'mucrim' "
 "(ölçüm edim haber, kip NEG 2; 1P 2 · 3FS 2 · 3MP 7 · 3MS 1; bab I. bab ×3 · II. bab ×2 · X. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); ölçüm '{{3|" + _AK3 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=23 (n z=1,12); ölçüm '{{3|EDİLGEN 1/6 fiil, pas z=0,62}}' — satır aynen; ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:39 ن → 7:40 ن); "
 "ölçüm '{{3|simetri \\[3, 1, 6, 1\\]}}' — satır aynen; ölçüm '{{3|harf 106 → harf3 103, isaret 3}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 2: 'lâ' (7. kelime), 've lâ' (12. kelime; 'lâ'); "
 "'inne' (1.) ACC; 'llezîne' (2.) REL; 've'stekberû' (5.) kelimesindeki 've' CONJ; 've lâ' (12.) kelimesindeki 've' CONJ; 'hattâ' (15.) P; 've kezâlike' (21.) kelimesindeki 've' REM; 've kezâlike' (21.) P + DEM + DIST + ADDR (okuma). "
 + T[40] + " (okuma). "
 + cumle(say('say 7:40 1-11', "inne'llezîne kezzebû bi-âyâtinâ ve'stekberû 'anhâ lâ tufettehu lehum ebvâbu's-semâ'i", True), say('say 7:40 3-6', "kezzebû bi-âyâtinâ ve'stekberû 'anhâ"), say('dizi 7 40 3 6', "kezzebe âye istekbere 'an"), say('say 7:40 2-4', "llezîne kezzebû bi-âyâtinâ"), say('dizi 7 40 2 4', "ellezî kezzebe âye")) + ' '
 + cumle(say('say 7:40 12-20', "ve lâ yedxulûne'l-cennete hattâ yelice'l-cemelu fî semmi'l-xiyâti", True)) + ' '
 + cumle(say('say 7:40 21-23', "ve kezâlike neczi'l-mucrimîn", True), say('say 7:40 21-22', "ve kezâlike neczi"), say('dizi 7 40 21 22', "zâ cezâ")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'kezzebe âye istekbere 'an' süzgeç GEÇER; 'ellezî kezzebe âye' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K1 's-semâ'i' (11. kelime).",
 "◈B — —",
 "◈D — D1 'inne' + 'ellezî' + PERF + 'bi' + izafet + 've' + PERF + ''an' + 'lâ' + IMPF + 'li' + izafet + belirli + 've' + 'lâ' + IMPF + belirli + 'hattâ' + IMPF + belirli + 'fî' + izafet + belirli + 've' + 'ke' + 'zâ' + IMPF + belirli; "
 "D2 haber; NEG ('lâ' 7. kelime, 've lâ' 12. kelime); D3 —; D4 1P 2 · 3FS 2 · 3MP 7 · 3MS 1, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[40] + "; aktör adlı 'l-cennete' (14. kelime; ölçüm rol meful); A2 âyetleri yalanlayıp onlara karşı büyüklenenlere gök kapılarının açılmayışı; deve iğne deliğine girene dek bahçeye girmeyişleri; suçluların böyle cezalandırılışı; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi emir → haber (ayetler arası).",
)

D[41] = ("◇ 'lehum min cehenneme mihâdun ve min fevqıhim ğavâşin ve kezâlike neczi'z-zâlimîn' — "
 "'li' + 3MP + 'min' + özel ad 'cehennem' + nekre 'mihâd' + 've' + 'min' + 'fevq' + 3MP + nekre çoğul etken ortaç 'ğâşiye' + 've' + 'ke' + 'zâ' + IMPF 1P I. bab + belirli çoğul etken ortaç 'zâlim' "
 "(ölçüm edim haber, kip yok; 1P 1 · 3MP 2; bab I. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); ölçüm '{{4|" + _AK4 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=10 (n z=-0,26); ölçüm '{{4|fâsıla " + _F[3] + " → ن, N sınıfı}}' — satır aynen (7:40 ن → 7:41 ن); "
 "ölçüm '{{4|harf 44 → harf3 41, isaret 3}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; "
 "'ve min' (5.) kelimesindeki 've' CONJ; 've kezâlike' (8.) kelimesindeki 've' REM; 've kezâlike' (8.) P + DEM + DIST + ADDR (okuma). "
 + T[41] + " (okuma). "
 + cumle(say('say 7:41 1-4', "lehum min cehenneme mihâdun", True), say('say 7:41 5-7', "ve min fevqıhim ğavâşin")) + ' '
 + cumle(say('say 7:41 8-10', "ve kezâlike neczi'z-zâlimîn", True), say('say 7:41 8-9', "ve kezâlike neczi"), say('dizi 7 41 8 9', "zâ cezâ"), say('say 7:41 9-10', "neczi'z-zâlimîn")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'li' + 'min' + özel ad + nekre + 've' + 'min' + izafet + nekre + 've' + 'ke' + 'zâ' + IMPF + belirli; "
 "D2 haber; kip yok; D3 —; D4 1P 1 · 3MP 2, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[41] + "; aktör adlı 'cehenneme' (3. kelime; ölçüm rol mecrur); A2 onlar için cehennemden döşek ve üstlerinde örtüler; zalimlerin böyle cezalandırılışı; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi yok (ayetler arası); bölüm kapanışı.",
)
out = ['# ── blok 7:38-41 (2026-11-25) ──', 'MEAL11 = {']
for n in range(38, 42):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M11 = {']
for n in range(38, 42):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL11); M.update(M11)']
open('/home/claude/yamalar/metin_7_38_41.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
