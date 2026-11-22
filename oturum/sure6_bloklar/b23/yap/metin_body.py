# sûre 6 blok 23 (6:95-99) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b23/say2.txt'
os.environ['OLC'] = '/home/claude/b23/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Taneyi ve çekirdeği yaran; gözler O'nu idrak etmez' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 95: "Şüphesiz Allah taneyi ve çekirdeği yarandır; diriyi ölüden çıkarır ve ölüyü diriden çıkarandır. İşte Allah budur; o hâlde nasıl döndürülüyorsunuz?",
 96: "Sabahı yarandır; geceyi dinlenme vakti, güneşi ve ayı hesap ölçüsü kıldı. Bu, Azîz ve Alîm olanın takdiridir.",
 97: "O, size yıldızları kılandır, karanın ve denizin karanlıklarında onlarla yol bulasınız diye. Bilen bir kavim için âyetleri ayrıntılı açıkladık.",
 98: "O, sizi bir candan inşâ edendir; böylece bir karar yeri ve bir emanet yeri vardır. Anlayan bir kavim için âyetleri ayrıntılı açıkladık.",
 99: "O, gökten su indirendir; onunla her şeyin bitkisini çıkardık, ondan bir yeşillik çıkardık; ondan üst üste binmiş taneler çıkarırız; hurmanın tomurcuğundan sarkan salkımlar; üzümlerden bahçeler, zeytin ve nar, birbirine benzer ve benzemez hâlde. Meyve verdiğinde meyvesine ve olgunlaşmasına bakın. Şüphesiz bunda, inanan bir kavim için âyetler vardır.",
}

T = {}
T[95] = ("'yuxricu' 3MS (adsız; gönderge 'llâhe' 2. kelime, 6. kelime); muhatap 2MP (adsız; 'tu'fekûn' — 17. kelime); 'tu'fekûn' (17. kelime) edilgen — naib-i faili (adsız) muhatap 2MP")
T[96] = ("'ce'ale' 3MS (adsız; gönderge 6:95 2. kelime, 3. kelime)")
T[97] = ("'ve huve', 'ce'ale' 3MS (adsız; gönderge 6:95 2. kelime — 1. ve 3. kelime); muhatap 2MP (adsız; 'lekumu', 'li-tehtedû' — 4. ve 6. kelime); "
         "'bihâ' 3FS (adsız; gönderge 'n-nucûme' 5. kelime, 7. kelime); konuşan 1P (adsız; 'fassalne' — 13. kelime); 'ya'lemûn' 3MP (adsız; gönderge 'li-qavmin' 15. kelime, 16. kelime)")
T[98] = ("'ve huve', 'enşe'ekum' 3MS (adsız; gönderge 6:95 2. kelime — 1. ve 3. kelime); muhatap 2MP (adsız; 'enşe'ekum' — 3. kelime); "
         "konuşan 1P (adsız; 'fassalne' — 10. kelime); 'yefqahûn' 3MP (adsız; gönderge 'li-qavmin' 12. kelime, 13. kelime)")
T[99] = ("'ve huve', 'enzele' 3MS (adsız; gönderge 6:95 2. kelime — 1. ve 3. kelime); konuşan 1P (adsız; 'fe-axracnâ', 'fe-axracnâ', 'nuxricu' — 7., 12. ve 15. kelime); "
         "'bihî' 3MS (adsız; gönderge 'mâ'en' 6. kelime, 8. kelime); 'minhu' 3MS (adsız; tartışmalı; gönderge 'nebâte' 9. kelime, 13. kelime); 'minhu' 3MS (adsız; gönderge 'xadiran' 14. kelime, 16. kelime); "
         "'tal'ihâ' 3FS (adsız; tartışmalı; gönderge 'n-naxli' 20. kelime, 22. kelime); muhatap 2MP (adsız; 'unzurû' — 33. kelime); "
         "'semerihî', 'esmera', 've yen'ihî' 3MS (adsız; gönderge 'muteşâbihin' 32. kelime — 35., 37. ve 38. kelime; tartışmalı); 'yu'minûn' 3MP (adsız; gönderge 'li-qavmin' 43. kelime, 44. kelime)")

D = {}
D[95] = ("◇ 'inna'llâhe fâliqu'l-habbi ve'n-nevâ yuxricu'l-hayye mine'l-meyyiti ve muxricu'l-meyyiti mine'l-hayyi zâlikumu'llâhu fe-ennâ tu'fekûn' — "
 "'inne' + lafız + etken ortaç 'fâliq' + belirli 'habb' + 've' + belirli 'nevâ' + IMPF 3MS IV. bab + belirli 'hayy' + 'min' + belirli 'meyyit' + 've' + etken ortaç 'muxric' + belirli 'meyyit' + 'min' + belirli 'hayy' + "
 "'zâlikum' + lafız + 'fe' + 'ennâ' + IMPF 2MP I. bab edilgen + 2MP "
 "(ölçüm edim soru, kip INTG 1; 2MP 2 · 3MS 1; bab I. bab ×1 · IV. bab ×1). "
 "Allah lafzı 2. ve 15. sırada (ölçüm allah z=1,82); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür EVET ton denge' — ölçüm esmâ yok ile uyuşmuyor, araç tanımı farkı (muhur_el hayır, ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'yuxricu'l-hayye mine'l-meyyit' ve 'muxricu'l-meyyiti mine'l-hayy', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); liste farkı: ölçüm esmâ satırında 'hayy' yok, esma_kayit e_oto 1. "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=17 (n z=0,49); ölçüm '{{1|EDİLGEN 1/2 fiil, pas z=2,52}}' — satır aynen; ölçüm '{{1|HAPAKS: نوي}}' — satır aynen (kök bu blokta tabloya eklendi); ölçüm '{{1|hapaks z=3,28}}' — satır aynen; "
 "ölçüm '{{1|fâsıla تؤفكون → ن, N sınıfı}}' — satır aynen (6:94 ن → 6:95 ن); "
 "ölçüm '{{1|simetri \\[3, 1, 14, 1\\]}}' — satır aynen; ölçüm '{{1|harf 73 → harf3 69, isaret 4}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm INTG 1: 'fe-ennâ' (16. kelime); 've'n-nevâ' (5.) ve 've muxricu' (10.) kelimelerindeki 've' CONJ; 'fe-ennâ' (16.) kelimesindeki 'fe' REM; 'inna' (1.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhe' 2. / 'llâhu' 15. kelime), حيي ×2 ('l-hayye' 7. / 'l-hayyi' 13. kelime), خرج ×2 ('yuxricu' 6. / 've muxricu' 10. kelime), موت ×2 ('l-meyyiti' 9. / 'l-meyyiti' 11. kelime) (okuma). "
 + T[95] + " (okuma). "
 + cumle(say('say 6:95 6-9', "yuxricu'l-hayye mine'l-meyyiti", True), say('dizi 6 95 6 9', "axraca hayy min meyyit")) + ' ' +
 "Ölçüm xref yok; ölçüm bağ yok (esit2, nakarat3, xref üçü de boş). "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'l-hayye' / 'l-meyyiti' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 —; B4 'l-hayye' (7. kelime), 'l-meyyiti' (9. kelime), 'l-meyyiti' (11. kelime), 'l-hayyi' (13. kelime).",
 "◈D — D1 'inne' + lafız + 'fâliq' + belirli + 've' + belirli + IMPF + belirli + 'min' + belirli + 've' + 'muxric' + belirli + 'min' + belirli + 'zâlikum' + lafız + 'fe' + 'ennâ' + IMPF; "
 "D2 soru; INTG ('fe-ennâ' 16. kelime); D3 أله ×2, حيي ×2, خرج ×2, موت ×2; D4 2MP 2 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[95] + "; aktör yok (ölçüm); A2 Allah'ın taneyi ve çekirdeği yarması; diriyi ölüden, ölüyü diriden çıkarması; 'İşte Allah budur' bildirimi; nasıl döndürüldükleri sorusu; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi haber → soru (ayetler arası); bölüm açılışı.",
)

D[96] = ("◇ 'fâliqu'l-isbâhi ve ce'ale'l-leyle sekenen ve'ş-şemse ve'l-qamera husbânen zâlike taqdîru'l-'azîzi'l-'alîm' — "
 "etken ortaç 'fâliq' + belirli mastar 'isbâh' + 've' + PERF 3MS I. bab + belirli 'leyl' + nekre 'seken' + 've' + belirli 'şems' + 've' + belirli 'qamer' + nekre 'husbân' + 'zâlike' + mastar 'taqdîr' + belirli ''azîz' + belirli ''alîm' "
 "(ölçüm edim haber, kip yok; 3MS 1; bab I. bab ×1). "
 "Allah lafzı yok; Rab yok; ölçüm '{{2|esmâ عَزِيز 11\\. sırada, SON konum, MÜHÜR \\| عَلِيم 12\\. sırada, SON konum, MÜHÜR}}' — satır aynen; esma_kayit çıktısı 'mühür EVET (ÇİFT)' (uyuşuyor); "
 "'zâlike taqdîru'l-'azîzi'l-'alîm' — tamlama içinde ad (tamlayan), göndergesi Allah; kapalı listede kural yok, esma_el'e girmedi — kullanıcı kararına, tam okuma sonu (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=12 (n z=-0,04); ölçüm '{{2|fâsıla ٱلعليم → م, N sınıfı}}' — satır aynen (6:95 ن → 6:96 م); "
 "ölçüm '{{2|harf 64 → harf3 61, isaret 3}}' — satır aynen; ölçüm '{{2|dış düğüm 3}}' — satır aynen. "
 "Ölçüm kip yok; 've ce'ale' (3.), 've'ş-şemse' (6.) ve 've'l-qamera' (7.) kelimelerindeki 've' CONJ (okuma). "
 + T[96] + " (okuma). "
 + cumle(say('say 6:96 9-12', "zâlike taqdîru'l-'azîzi'l-'alîm", True), say('dizi 6 96 9 12', "zâ taqdîr 'azîz 'alîm")) + ' ' +
 "Ölçüm xref 36:38 (emsal olarak basıldı) ve okunmuş 2 ayet. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'l-isbâhi' / 'l-leyle' — ayetler arası: yok.",
 "◈K — K1 'l-leyle' (4. kelime), 'ş-şemse' (6. kelime), 'l-qamera' (7. kelime).",
 "◈B — —",
 "◈D — D1 'fâliq' + belirli + 've' + PERF + belirli + nekre + 've' + belirli + 've' + belirli + nekre + 'zâlike' + izafet + belirli + belirli; "
 "D2 haber; D3 36:38 eşi; D4 3MS 1, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[96] + "; aktör yok (ölçüm); A2 sabahı yarma; gecenin dinlenme vakti, güneşin ve ayın hesap ölçüsü kılınması; Azîz ve Alîm olanın takdiri; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi soru → haber (ayetler arası).",
)

D[97] = ("◇ 've huve'llezî ce'ale lekumu'n-nucûme li-tehtedû bihâ fî zulumâti'l-berri ve'l-bahri qad fassalne'l-âyâti li-qavmin ya'lemûn' — "
 "'ve' + 'huve' + 'ellezî' + PERF 3MS I. bab + 'li' + 2MP + belirli çoğul 'necm' + 'li' + IMPF 2MP VIII. bab + 2MP + 'bi' + 3FS + 'fî' + çoğul 'zulme' + belirli 'berr' + 've' + belirli 'bahr' + "
 "'qad' + PERF 1P II. bab + 1P + belirli çoğul 'âye' + 'li' + nekre 'qavm' + IMPF 3MP I. bab + 3MP "
 "(ölçüm edim haber, kip CERT 1; 1P 2 · 2MP 3 · 3FS 1 · 3MP 2 · 3MS 2; bab I. bab ×2 · II. bab ×1 · VIII. bab ×1). "
 "Allah lafzı yok; Rab yok; ölçüm '{{3|esmâ بَرّ 10\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor); "
 "esma_el kaydı 'degil' — 'fî zulumâti'l-berri ve'l-bahr', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=16 (n z=0,38); ölçüm '{{3|fâsıla يعلمون → ن, N sınıfı}}' — satır aynen (6:96 م → 6:97 ن); "
 "ölçüm '{{3|simetri \\[3, 1, 7, 1\\]}}' — satır aynen; ölçüm '{{3|harf 71 → harf3 68, isaret 3}}' — satır aynen; ölçüm '{{3|dış düğüm 1}}' — satır aynen; ölçüm '{{3|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (12. kelime); 've huve' (1.) ve 've'l-bahri' (11.) kelimelerindeki 've' CONJ; 'li-tehtedû' (6.) kelimesindeki 'li' PRP (okuma). "
 + T[97] + " (okuma). "
 + cumle(say('say 6:97 12-15', "qad fassalne'l-âyâti li-qavmin", True), say('dizi 6 97 12 15', "qad fassale âye qavm")) + ' ' + cumle(say('say 6:97 9-11', "zulumâti'l-berri ve'l-bahr", True), say('dizi 6 97 9 11', "zulme berr bahr")) + ' ' + cumle(say('say 6:97 1-3', "ve huve'llezî ce'ale", True), say('dizi 6 97 1 3', "_ ellezî ce'ale")) + ' ' +
 "Ölçüm xref 6:63 (basılmış) ve 27:63 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıpları: 'qad fassale âye qavm' süzgeç GEÇER, 'zulme berr bahr' süzgeç GEÇMEZ, '_ ellezî ce'ale' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'l-berri' / 've'l-bahri' — ayetler arası: yok.",
 "◈K — K1 'n-nucûme' (5. kelime), 'l-bahri' (11. kelime).",
 "◈B — —",
 "◈D — D1 've' + 'huve' + 'ellezî' + PERF + 'li' + belirli + 'li' + IMPF + 'bi' + 'fî' + izafet + belirli + 've' + belirli + 'qad' + PERF + belirli + 'li' + nekre + IMPF; "
 "D2 haber; CERT ('qad' 12. kelime); D3 27:63 eşi; D4 1P 2 · 2MP 3 · 3FS 1 · 3MP 2 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[97] + "; aktör yok (ölçüm); A2 karanın ve denizin karanlıklarında yol bulmak için yıldızların kılınması; bilen bir kavim için âyetlerin ayrıntılı açıklanması; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 2 (ayetler arası); şahıs sayısında beraberlik yok (1. şahıs 2 · 2. şahıs 3 · 3. şahıs 5 — ölçüm baskın 2, araç tanımı farkı); edim geçişi yok (ayetler arası).",
)

D[98] = ("◇ 've huve'llezî enşe'ekum min nefsin vâhidetin fe-mustaqarrun ve mustevda'un qad fassalne'l-âyâti li-qavmin yefqahûn' — "
 "'ve' + 'huve' + 'ellezî' + PERF 3MS IV. bab + 2MP + 'min' + nekre 'nefs' + nekre 'vâhide' + 'fe' + nekre edilgen ortaç 'mustaqarr' + 've' + nekre edilgen ortaç 'mustevda'' + "
 "'qad' + PERF 1P II. bab + 1P + belirli çoğul 'âye' + 'li' + nekre 'qavm' + IMPF 3MP I. bab + 3MP "
 "(ölçüm edim haber, kip CERT 1; 1P 2 · 2MP 1 · 3MP 2 · 3MS 2; bab I. bab ×1 · II. bab ×1 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=13 (n z=0,06); ölçüm '{{4|sayı işareti واحِدَة}}' — satır aynen; ölçüm '{{4|fâsıla يفقهون → ن, N sınıfı}}' — satır aynen (6:97 ن → 6:98 ن); "
 "ölçüm '{{4|harf 64 → harf3 58, isaret 6}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (9. kelime); 've huve' (1.) ve 've mustevda'un' (8.) kelimelerindeki 've' CONJ; 'fe-mustaqarrun' (7.) kelimesindeki 'fe' REM (okuma). "
 + T[98] + " (okuma). "
 + cumle(say('say 6:98 9-12', "qad fassalne'l-âyâti li-qavmin", True), say('dizi 6 98 9 12', "qad fassale âye qavm")) + ' ' + cumle(say('say 6:98 1-3', "ve huve'llezî enşe'ekum", True), say('dizi 6 98 1 3', "_ ellezî enşe'e")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: 'qad fassale âye qavm' süzgeç GEÇER, '_ ellezî enşe'e' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'fe-mustaqarrun' / 've mustevda'un' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'huve' + 'ellezî' + PERF + 'min' + nekre + nekre + 'fe' + nekre + 've' + nekre + 'qad' + PERF + belirli + 'li' + nekre + IMPF; "
 "D2 haber; CERT ('qad' 9. kelime); D3 —; D4 1P 2 · 2MP 1 · 3MP 2 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[98] + "; aktör yok (ölçüm); A2 bir candan inşâ; karar yeri ve emanet yeri; anlayan bir kavim için âyetlerin ayrıntılı açıklanması; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[99] = ("◇ 've huve'llezî enzele mine's-semâ'i mâ'en fe-axracnâ bihî nebâte kulli şey'in fe-axracnâ minhu xadiran nuxricu minhu habben muterâkiben ve mine'n-naxli min tal'ihâ qinvânun dâniyetun ve cennâtin min a'nâbin ve'z-zeytûne ve'r-rummâne muştebihen ve ğayra muteşâbihin unzurû ilâ semerihî izâ esmera ve yen'ihî inne fî zâlikum le-âyâtin li-qavmin yu'minûn' — "
 "'ve' + 'huve' + 'ellezî' + PERF 3MS IV. bab + 'min' + belirli 'semâ'' + nekre 'mâ'' + 'fe' + PERF 1P IV. bab + 1P + 'bi' + 3MS + 'nebât' + 'kull' + nekre 'şey'' + 'fe' + PERF 1P IV. bab + 1P + 'min' + 3MS + nekre 'xadir' + IMPF 1P IV. bab + 'min' + 3MS + nekre 'habb' + nekre etken ortaç 'muterâkib' + "
 "'ve' + 'min' + belirli 'naxl' + 'min' + 'tal'' + 3FS + nekre çoğul 'qinvân' + nekre etken ortaç 'dâniye' + 've' + nekre çoğul 'cenne' + 'min' + nekre çoğul ''ineb' + 've' + belirli 'zeytûn' + 've' + belirli 'rummân' + nekre etken ortaç 'muştebih' + 've' + 'ğayr' + nekre etken ortaç 'muteşâbih' + "
 "IMPV 2MP I. bab + 2MP + 'ilâ' + 'semer' + 3MS + 'izâ' + PERF 3MS IV. bab + 've' + 'yen'' + 3MS + 'inne' + 'fî' + 'zâlikum' + 'le' + nekre çoğul 'âye' + 'li' + nekre 'qavm' + IMPF 3MP IV. bab + 3MP "
 "(ölçüm edim emir, kip EMPH 1 · IMPV 1; 1P 5 · 2MP 2 · 3FS 1 · 3MP 2 · 3MS 8; bab I. bab ×1 · IV. bab ×6). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=44 (n z=3,35); ölçüm '{{5|HAPAKS: قنو}}' — satır aynen (kök bu blokta tabloya eklendi); ölçüm '{{5|hapaks z=6,79}}' — satır aynen; "
 "ölçüm '{{5|fâsıla يؤمنون → ن, N sınıfı}}' — satır aynen (6:98 ن → 6:99 ن); "
 "ölçüm '{{5|simetri \\[3, 1, 39, 1\\]}}' — satır aynen; ölçüm '{{5|harf 203 → harf3 185, isaret 18}}' — satır aynen; ölçüm '{{5|dış düğüm 0}}' — satır aynen. "
 "Ölçüm EMPH 1: 'le-âyâtin' (42. kelime); IMPV 1: 'unzurû' (33. kelime); 've mine'n-naxli' (19.) kelimesindeki 've' REM; 've huve' (1.), 've cennâtin' (25.), 've'z-zeytûne' (28.), 've'r-rummâne' (29.), 've ğayra' (31.) ve 've yen'ihî' (38.) kelimelerindeki 've' CONJ; "
 "'fe-axracnâ' (7. ve 12.) kelimelerindeki 'fe' CONJ; 'izâ' (36.) T; 'inne' (39.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) ثمر ×2 ('semerihî' 35. / 'esmera' 37. kelime), خرج ×3 ('fe-axracnâ' 7., 'fe-axracnâ' 12., 'nuxricu' 15. kelime), شبه ×2 ('muştebihen' 30. / 'muteşâbihin' 32. kelime) (okuma). "
 + T[99] + " (okuma). "
 + cumle(say('say 6:99 35-37', "semerihî izâ esmera", True), say('dizi 6 99 35 37', "semer izâ esmera")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'semer izâ esmera' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'muştebihen' / 've ğayra muteşâbihin' — ayetler arası: yok.",
 "◈K — K1 's-semâ'i' (5. kelime), 'mâ'en' (6. kelime).",
 "◈B — B1 'nebâte' (9. kelime); B2 —; B3 —; B4 —.",
 "◈D — D1 've' + 'huve' + 'ellezî' + PERF + 'min' + belirli + nekre + 'fe' + PERF + 'bi' + izafet + 'kull' + nekre + 'fe' + PERF + 'min' + nekre + IMPF + 'min' + nekre + nekre + 've' + 'min' + belirli + 'min' + izafet + nekre + nekre + 've' + nekre + 'min' + nekre + 've' + belirli + 've' + belirli + nekre + 've' + 'ğayr' + nekre + "
 "IMPV + 'ilâ' + izafet + 'izâ' + PERF + 've' + izafet + 'inne' + 'fî' + 'zâlikum' + 'le' + nekre + 'li' + nekre + IMPF; "
 "D2 emir; EMPH ('le-âyâtin' 42. kelime), IMPV ('unzurû' 33. kelime); D3 ثمر ×2, خرج ×3, شبه ×2; D4 1P 5 · 2MP 2 · 3FS 1 · 3MP 2 · 3MS 8, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[99] + "; aktör yok (ölçüm); A2 gökten indirilen su; onunla çıkarılan bitki, yeşillik ve üst üste binmiş taneler; hurma salkımları; üzüm bahçeleri, zeytin ve nar; meyveye ve olgunlaşmaya bakma emri; inanan bir kavim için âyetler; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi haber → emir (ayetler arası).",
)
