# blok 29 (5:94-96) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b29/say2.txt'
os.environ['OLC'] = '/home/claude/b29/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'İhramda av; Kâbe ve haram ay; elçinin görevi' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 94: "Ey iman edenler! Allah sizi, ellerinizin ve mızraklarınızın erişeceği avdan bir şeyle mutlaka sınayacak; Allah kendisinden gaybda korkanı bilsin diye. Bundan sonra kim sınırı aşarsa, onun için acı bir azap vardır.",
 95: "Ey iman edenler! İhramlıyken avı öldürmeyin. Sizden kim onu kasten öldürürse, karşılığı, öldürdüğünün dengi bir davardır; buna sizden iki adalet sahibi hükmeder, Kâbe'ye ulaşacak bir kurban olarak; ya da yoksulların yemeği olan bir keffaret ya da bunun dengi oruçtur; işinin vebalini tatsın diye. Allah geçmişte olanı affetti. Kim dönerse Allah ondan intikam alır. Allah azîzdir, intikam sahibidir.",
 96: "Deniz avı ve onun yiyeceği, size ve yolculara bir geçimlik olarak helâl kılındı; ihramlı olduğunuz sürece kara avı size haram kılındı. Huzuruna toplanacağınız Allah'tan sakının.",
}

T94 = ("hitap 'yâ eyyuhe'llezîne âmenû' (1-3. kelime); 'âmenû' faili 3MP (adsız; 3. kelime); 'le-yeblüvennekumu' 3MS (fiil uyumu; 4. kelime — fail 5. kelime); 'llâhu' ('le-yeblüvennekumu' faili; lafız; 5. kelime); "
       "muhatap 2MP (adsız; 'le-yeblüvennekumu', 'eydîkum', 'rimâhukum' — 4., 10. ve 11. kelime); 'tenâluhû' 3FS (fiil uyumu; 9. kelime — fail 10. kelime); 'tenâluhû' mef'ûlü 3MS (adsız; gönderge 's-saydi', 9. kelime); "
       "'li-ya'leme' 3MS (fiil uyumu; 12. kelime — fail 13. kelime); 'llâhu' ('li-ya'leme' faili; lafız; 13. kelime); 'men' ('li-ya'leme' mef'ûlü; ilgi; 14. kelime); 'yaxâfuhû' 3MS (adsız; gönderge 'men', 15. kelime); "
       "'yaxâfuhû' mef'ûlü 3MS (adsız; gönderge lafız, 15. kelime); 'fe-meni'tedâ' 3MS (adsız; şart ismi 'men' göndergeli; 17-18. kelime); 'lehû' 3MS (adsız; gönderge 'men', 21. kelime); ''azâbun elîm' (22-23. kelime)")
T95 = ("hitap 'yâ eyyuhe'llezîne âmenû' (1-3. kelime); 'âmenû' faili 3MP (adsız; 3. kelime); muhatap 2MP (adsız; 'taqtulu', 'entum', 'minkum', 'minkum' — 5., 7., 11. ve 23. kelime); "
       "'men' (şart ismi; 9. kelime); 'qatelehû' 3MS (adsız; gönderge 'men', 10. kelime); 'qatelehû' mef'ûlü 3MS (adsız; gönderge 's-sayde', 10. kelime); 'qatele' 3MS (adsız; gönderge 'men', 16. kelime); "
       "'yahkumu' 3MS (fiil uyumu; 19. kelime — fail 21. kelime); 'bihî' 3MS (adsız; gönderge 'cezâ'un', 20. kelime); 'zevâ 'adlin' ('yahkumu' faili; 21-22. kelime); 'l-ka'beti' (adlı yer; 26. kelime); "
       "'li-yezûqa' 3MS (adsız; gönderge 'men', 35. kelime); 'emrihî' iyelik 3MS (adsız; 37. kelime); ''afa' 3MS (fiil uyumu; 38. kelime — fail 39. kelime); 'llâhu' (''afa' faili; lafız; 39. kelime); 'selefe' 3MS (adsız; gönderge 'mâ', 41. kelime); "
       "'men' (şart ismi; 42. kelime); ''âde' 3MS (adsız; gönderge 'men', 43. kelime); 'fe-yentaqimu' 3MS (fiil uyumu; 44. kelime — fail 45. kelime); 'llâhu' ('fe-yentaqimu' faili; lafız; 45. kelime); "
       "'minhu' 3MS (adsız; gönderge 'men', 46. kelime); 'llâhu' (mübtedâ; lafız; 47. kelime); ''azîzun' (haber; 48. kelime)")
T96 = ("'uhille' 3MS (fiil uyumu; edilgen; 1. kelime — naib-i faili 3. kelime); muhatap 2MP (adsız; 'lekum', 'lekum', ''aleykum', 'dumtum', 'ttequ', 'tuhşerûn' — 2., 7., 10., 14., 16. ve 20. kelime); "
       "'saydu'l-bahri' ('uhille' naib-i faili; 3-4. kelime); 'ta'âmuhû' iyelik 3MS (adsız; gönderge 'l-bahri', 5. kelime); 'hurrime' 3MS (fiil uyumu; edilgen; 9. kelime — naib-i faili 11. kelime); "
       "'llâhe' ('ttequ' mef'ûlü; lafız; 17. kelime); 'ileyhi' 3MS (adsız; gönderge lafız, 19. kelime); 'tuhşerûn' faili (adsız; edilgen — nâib fâil muhatap 2MP, 20. kelime)")

D = {}
D[94] = ("◇ 'yâ eyyuhe'llezîne âmenû le-yeblüvennekumu'llâhu bi-şey'in mine's-saydi tenâluhû eydîkum ve rimâhukum li-ya'leme'llâhu men yaxâfuhû bi'l-ğaybi fe-meni'tedâ ba'de zâlike fe-lehû 'azâbun elîm' — "
 "'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF 3MP IV. bab + 'le' + IMPF 3MS I. bab + 'nne' + 2MP + lafız + 'bi' + nekre 'şey'' + 'min' + belirli 'sayd' + IMPF 3FS I. bab + 3MS + çoğul 'yed' + 2MP + 've' + çoğul 'rimâh' + 2MP + "
 "'li' + IMPF 3MS I. bab + lafız + 'men' + IMPF 3MS I. bab + 3MS + 'bi' + belirli 'ğayb' + 'fe' + 'men' + PERF 3MS VIII. bab + 'ba'd' + 'zâlike' + 'fe' + 'li' + 3MS + nekre ''azâb' + nekre 'elîm' "
 "(ölçüm edim nida, şart, kip COND 1 · EMPH 2 · VOC 1; 2MP 3 · 3FS 1 · 3MP 2 · 3MS 7; bab I. bab ×4 · IV. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 5. ve 13. sırada (ölçüm allah z=1,21); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=23 (n z=1,12); ölçüm '{{1|HAPAKS: رمح}}' — satır aynen (kök bu blokta tabloya eklendi); ölçüm '{{1|hapaks z=3,28}}' — satır aynen; "
 "ölçüm '{{1|fâsıla أليم → م, N sınıfı}}' — satır aynen; ölçüm '{{1|harf 111 → harf3 104, isaret 7}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen. "
 "Ölçüm VOC 1: 'yâ' (1. kelime); EMPH 2: 'le' ve 'nne' (4. kelime); COND 1: 'men' (17. kelime); 've rimâhukum' (11.)'daki 've' CONJ, 'fe-meni'tedâ' (17.)'daki 'fe' REM, 'fe-lehû' (21.)'daki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhu' 5. / 13. kelime) (okuma). "
 + T94 + " (okuma). "
 + cumle(say('say 5:94 1-3', "yâ eyyuhe'llezîne âmenû", True), say('dizi 5 94 1 3', "eyy ellezî âmene")) + ' '
 + cumle(say('say 5:94 4-8', "le-yeblüvennekumu'llâhu bi-şey'in mine's-sayd", True), say('say 5:94 4-5', "le-yeblüvennekumu'llâh"), say('say 5:94 6-8', "bi-şey'in mine's-sayd"), say('say 5:94 7-8', "mine's-sayd")) + ' '
 + cumle(say('say 5:94 9-11', "tenâluhû eydîkum ve rimâhukum", True), say('say 5:94 10-11 --on', "eydîkum ve rimâhukum")) + ' '
 + cumle(say('say 5:94 12-16', "li-ya'leme'llâhu men yaxâfuhû bi'l-ğayb", True), say('say 5:94 13-16', "llâhu men yaxâfuhû bi'l-ğayb"), say('say 5:94 14-16', "men yaxâfuhû bi'l-ğayb")) + ' '
 + cumle(say('say 5:94 17-20 --on', "fe-meni'tedâ ba'de zâlik", True), say('say 5:94 18-20', "'tedâ ba'de zâlik"), say('say 5:94 18-23', "'tedâ ba'de zâlike fe-lehû 'azâbun elîm"), say('say 5:94 21-23 --on', "fe-lehû 'azâbun elîm"), say('say 5:94 22-23', "'azâbun elîm")) + ' '
 "Ölçüm xref 2:178 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı: 'eyy ellezî âmene' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'eydîkum' (10. kelime); B4 —.",
 "◈D — D1 'yâ' + 'ellezî' + PERF + 'le' + IMPF + 'nne' + lafız + 'bi' + nekre + 'min' + belirli + IMPF + çoğul + 've' + çoğul + 'li' + IMPF + lafız + 'men' + IMPF + 'bi' + belirli + 'fe' + 'men' + PERF + 'ba'd' + 'zâlike' + 'fe' + 'li' + nekre + nekre; "
 "D2 nida, şart, VOC ('yâ' 1. kelime), EMPH ('le', 'nne' 4. kelime), COND ('men' 17. kelime); D3 أله ×2; 2:178 eşi; D4 2MP 3 · 3FS 1 · 3MP 2 · 3MS 7, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T94 + "; aktör yok (ölçüm); A2 avdan bir şeyle sınanma; gaybda korkanın bilinmesi; sınırı aşana acı azap; A3 —; "
 "A4 " + BOLUM + "; bölüm açılışı; hitap açılır ('yâ eyyuhe'llezîne âmenû', 1-3. kelime); edim geçişi haber → nida, şart (ayetler arası); şart → cevap (ayet içi; COND 'men' 17. kelime: 'meni'tedâ' / 'lehû 'azâbun elîm' (21. kelime)).",
)

D[95] = ("◇ 'yâ eyyuhe'llezîne âmenû lâ taqtulu's-sayde ve entum hurumun ve men qatelehû minkum muta'ammiden fe-cezâ'un mislu mâ qatele mine'n-ne'ami yahkumu bihî zevâ 'adlin minkum hedyen bâliğa'l-ka'beti ev keffâratun ta'âmu mesâkîne ev 'adlu zâlike siyâmen li-yezûqa vebâle emrihî 'afa'llâhu 'ammâ selefe ve men 'âde fe-yentaqimu'llâhu minhu ve'llâhu 'azîzun zû'ntiqâm' — "
 "'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF 3MP IV. bab + 'lâ' + IMPF 2MP I. bab + belirli 'sayd' + 've' + 'entum' + nekre çoğul 'harâm' + 've' + 'men' + PERF 3MS I. bab + 3MS + 'min' + 2MP + nekre etken ortaç 'muta'ammid' + 'fe' + nekre 'cezâ'' + 'misl' + 'mâ' + PERF 3MS I. bab + 'min' + belirli 'ne'am' + "
 "IMPF 3MS I. bab + 'bi' + 3MS + 'zû' + nekre ''adl' + 'min' + 2MP + nekre 'hedy' + etken ortaç 'bâliğ' + belirli özel ad 'ka'be' + 'ev' + nekre 'keffâra' + 'ta'âm' + çoğul 'miskîn' + 'ev' + ''adl' + 'zâlike' + nekre 'siyâm' + 'li' + IMPF 3MS I. bab + 'vebâl' + 'emr' + 3MS + "
 "PERF 3MS I. bab + lafız + ''an' + 'mâ' + PERF 3MS I. bab + 've' + 'men' + PERF 3MS I. bab + 'fe' + IMPF 3MS VIII. bab + lafız + 'min' + 3MS + 've' + lafız + nekre ''azîz' + 'zû' + nekre masdar 'intiqâm' "
 "(ölçüm edim yasak, nida, şart, kip COND 2 · PRO 1 · VOC 1; 2MP 5 · 3MP 2 · 3MS 12; bab I. bab ×8 · IV. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 39., 45. ve 47. sırada (ölçüm allah z=0,67); Rab yok; ölçüm '{{2|esmâ عَزِيز 48\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton celâl' (uyuşmuyor) — esma_el kaydı 'ilahi' — 've'llâhu 'azîzun zû'ntiqâm', kural ''ve'llâhu X' kuralı → ilahi' (okuma); ölçüm aktör '{{2|adlı كَعْبَة 26\\. sırada \\(yer, rol mecrur\\)}}' — satır aynen. "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=50 (n z=3,99); ölçüm '{{2|fâsıla ٱنتقام → م, N sınıfı}}' — satır aynen; ölçüm '{{2|simetri \\[4, 2, 7, 1\\]}}' — satır aynen; "
 "ölçüm '{{2|harf 210 → harf3 193, isaret 17}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm VOC 1: 'yâ' (1. kelime); PRO 1: 'lâ' (4. kelime); COND 2: 'men' (9. ve 42. kelime); 've entum' (7.)'daki 've' CIRC, 've men' (9.)'daki 've' REM, 'fe-cezâ'un' (13.) ve 'fe-yentaqimu' (44.)'daki 'fe' RSLT, 'ev' (27. ve 31.) CONJ, 've men' (42.)'daki 've' CONJ, 've'llâhu' (47.)'daki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) أله ×3 ('llâhu' 39., 45., 47. kelime), عدل ×2 (''adlin' 22. / ''adlu' 32. kelime), قتل ×3 ('taqtulu' 5., 'qatelehû' 10., 'qatele' 16. kelime), نقم ×2 ('fe-yentaqimu' 44. / 'ntiqâm' 50. kelime) (okuma). "
 + T95 + " (okuma). "
 + cumle(say('say 5:95 1-4', "yâ eyyuhe'llezîne âmenû lâ", True), say('dizi 5 95 1 4', "eyy ellezî âmene lâ"), say('say 5:95 1-3', "yâ eyyuhe'llezîne âmenû"), say('dizi 5 95 1 3', "eyy ellezî âmene")) + ' '
 + cumle(say('say 5:95 4-8', "lâ taqtulu's-sayde ve entum hurum", True), say('say 5:95 5-6', "taqtulu's-sayd"), say('say 5:95 6-8', "s-sayde ve entum hurum"), say('dizi 5 95 6 8', "sayd _ harâm"), say('say 5:95 7-8 --on', "ve entum hurum")) + ' '
 + cumle(say('say 5:95 9-12 --on', "ve men qatelehû minkum muta'ammidâ", True), say('say 5:95 10-12', "qatelehû minkum muta'ammidâ"), say('say 5:95 13-18 --on', "fe-cezâ'un mislu mâ qatele mine'n-ne'am"), say('say 5:95 14-18', "mislu mâ qatele mine'n-ne'am"), say('say 5:95 15-18', "mâ qatele mine'n-ne'am")) + ' '
 + cumle(say('say 5:95 19-23', "yahkumu bihî zevâ 'adlin minkum", True), say('say 5:95 19-20', "yahkumu bih"), say('say 5:95 21-23', "zevâ 'adlin minkum"), say('dizi 5 95 21 23', "zû 'adl min"), say('say 5:95 24-26', "hedyen bâliğa'l-ka'be"), say('say 5:95 25-26', "bâliğa'l-ka'be")) + ' '
 + cumle(say('say 5:95 27-30', "ev keffâratun ta'âmu mesâkîn", True), say('say 5:95 28-30', "keffâratun ta'âmu mesâkîn"), say('say 5:95 29-30', "ta'âmu mesâkîn"), say('say 5:95 31-34', "ev 'adlu zâlike siyâmâ"), say('say 5:95 32-34', "'adlu zâlike siyâmâ"), say('say 5:95 35-37', "li-yezûqa vebâle emrih"), say('say 5:95 36-37', "vebâle emrih")) + ' '
 + cumle(say('say 5:95 38-41', "'afa'llâhu 'ammâ selef", True), say('say 5:95 38-39', "'afa'llâh"), say('say 5:95 40-41', "'ammâ selef"), say('say 5:95 42-46 --on', "ve men 'âde fe-yentaqimu'llâhu minh"), say('say 5:95 43-46', "'âde fe-yentaqimu'llâhu minh"), say('say 5:95 44-46 --on', "fe-yentaqimu'llâhu minh")) + ' '
 + cumle(say('say 5:95 47-50 --on', "ve'llâhu 'azîzun zû'ntiqâm", True), say('say 5:95 48-50', "'azîzun zû'ntiqâm")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: 'eyy ellezî âmene lâ' ve 'eyy ellezî âmene' süzgeç GEÇER, 'sayd _ harâm' ve 'zû 'adl min' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: ''afa'llâhu' / 'fe-yentaqimu'llâhu' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'n-ne'ami' (18. kelime); B2 —; B3 —; B4 —.",
 "◈D — D1 'yâ' + 'ellezî' + PERF + 'lâ' + IMPF + belirli + 've' + 'entum' + nekre + 've' + 'men' + PERF + 'min' + nekre + 'fe' + nekre + izafet + 'mâ' + PERF + 'min' + belirli + IMPF + 'bi' + izafet + nekre + 'min' + nekre + izafet + belirli + 'ev' + nekre + izafet + 'ev' + izafet + 'zâlike' + nekre + 'li' + IMPF + izafet + "
 "PERF + lafız + ''an' + 'mâ' + PERF + 've' + 'men' + PERF + 'fe' + IMPF + lafız + 'min' + 've' + lafız + nekre + 'zû' + nekre; "
 "D2 yasak, nida, şart, VOC ('yâ' 1. kelime), PRO ('lâ' 4. kelime), COND ('men' 9. ve 42. kelime); D3 أله ×3, عدل ×2, قتل ×3, نقم ×2; 3:4 eşi; D4 2MP 5 · 3MP 2 · 3MS 12, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T95 + "; aktör Kâbe (ölçüm); A2 ihramlıyken av yasağı; kasten öldürenin karşılığı (denk davar, keffaret ya da oruç); geçmişin affı; dönenden intikam; A3 —; "
 "A4 " + BOLUM + "; hitap açılır ('yâ eyyuhe'llezîne âmenû', 1-3. kelime); edim geçişi nida, şart → yasak, nida, şart (ayetler arası); şart → cevap (ayet içi; COND 'men' 9. kelime: 'men qatelehû' / 'cezâ'un mislu mâ qatele' (13. kelime)); "
 "şart → cevap (ayet içi; COND 'men' 42. kelime: 'men 'âde' / 'yentaqimu'llâhu minh' (44. kelime)).",
)

D[96] = ("◇ 'uhille lekum saydu'l-bahri ve ta'âmuhû metâ'an lekum ve li's-seyyârati ve hurrime 'aleykum saydu'l-berri mâ dumtum hurumen ve'ttequ'llâhe'llezî ileyhi tuhşerûn' — "
 "edilgen PERF 3MS IV. bab + 'li' + 2MP + 'sayd' + belirli 'bahr' + 've' + 'ta'âm' + 3MS + nekre 'metâ'' + 'li' + 2MP + 've' + 'li' + belirli 'seyyâra' + 've' + edilgen PERF 3MS II. bab + ''alâ' + 2MP + 'sayd' + belirli 'berr' + 'mâ' + PERF 2MP I. bab + nekre çoğul 'harâm' + "
 "'ve' + IMPV 2MP VIII. bab + lafız + 'ellezî' + 'ilâ' + 3MS + edilgen IMPF 2MP I. bab "
 "(ölçüm edim emir, kip IMPV 1; 2MP 9 · 3MS 4; bab I. bab ×2 · II. bab ×1 · IV. bab ×1 · VIII. bab ×1; EDİLGEN 3/5 fiil). "
 "Allah lafzı 17. sırada (ölçüm allah z=0,47); Rab yok; ölçüm '{{3|esmâ بَرّ 12\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton cemâl' (uyuşmuyor) — esma_el kaydı 'degil' — 'l-berri', kural 'esmâ adı esmâ dışı göndergeyle → degil' (kara) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=20 (n z=0,81); ölçüm '{{3|fâsıla تحشرون → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|EDİLGEN 3/5 fiil, pas z=3,10}}' — satır aynen ('uhille' 1., 'hurrime' 9., 'tuhşerûn' 20. kelime); "
 "ölçüm '{{3|simetri \\[3, 2, 10, 1\\]}}' — satır aynen; ölçüm '{{3|harf 91 → harf3 85, isaret 6}}' — satır aynen; ölçüm '{{3|dış düğüm 2}}' — satır aynen. "
 "Ölçüm IMPV 1: 'ttequ' (16. kelime); 've ta'âmuhû' (5.), 've li's-seyyârati' (8.) ve 've hurrime' (9.)'daki 've' CONJ, 've'ttequ' (16.)'daki 've' REM, 'mâ' (13.) SUB (okuma). "
 "Kök ikilemesi (ölçüm) حرم ×2 ('hurrime' 9. / 'hurumen' 15. kelime), صيد ×2 ('saydu' 3. / 11. kelime) (okuma). "
 + T96 + " (okuma). "
 + cumle(say('say 5:96 1-4', "uhille lekum saydu'l-bahr", True), say('say 5:96 1-2', "uhille lekum"), say('say 5:96 3-4', "saydu'l-bahr"), say('say 5:96 5-8 --on', "ve ta'âmuhû metâ'an lekum ve li's-seyyârat"), say('say 5:96 6-7', "metâ'an lekum")) + ' '
 + cumle(say('say 5:96 9-12 --on', "ve hurrime 'aleykum saydu'l-berr", True), say('say 5:96 10-12', "'aleykum saydu'l-berr"), say('say 5:96 11-12', "saydu'l-berr"), say('say 5:96 13-15', "mâ dumtum hurumen"), say('say 5:96 13-14', "mâ dumtum")) + ' '
 + cumle(say('say 5:96 16-20 --on', "ve'ttequ'llâhe'llezî ileyhi tuhşerûn", True), say('say 5:96 16-17 --on', "ve'ttequ'llâh"), say('say 5:96 16-18 --on', "ve'ttequ'llâhe'llezî"), say('dizi 5 96 16 18', "itteqâ allâh ellezî"), say('say 5:96 17-20', "llâhe'llezî ileyhi tuhşerûn"), say('say 5:96 19-20', "ileyhi tuhşerûn")) + ' '
 "Ölçüm xref 58:9 (emsal olarak basıldı) ve okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'itteqâ allâh ellezî' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'uhille' / 'hurrime' — ayetler arası: yok.",
 "◈K — K1 'l-bahri' (4. kelime).",
 "◈B — —",
 "◈D — D1 PERF + 'li' + izafet + belirli + 've' + izafet + nekre + 'li' + 've' + 'li' + belirli + 've' + PERF + ''alâ' + izafet + belirli + 'mâ' + PERF + nekre + 've' + IMPV + lafız + 'ellezî' + 'ilâ' + IMPF; "
 "D2 emir, IMPV ('ttequ' 16. kelime); D3 حرم ×2, صيد ×2; 58:9 eşi; D4 2MP 9 · 3MS 4, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T96 + "; aktör yok (ölçüm); A2 deniz avının helâl kılınması; ihramlıyken kara avının haram kılınması; toplanılacak Allah'tan sakınma emri; A3 —; "
 "A4 " + BOLUM + "; edim geçişi yasak, nida, şart → emir (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası).",
)

out = ['# ── blok 5:94-96 (2026-11-17) ──', 'MEAL29 = {']
for n in range(94, 97):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M29 = {']
for n in range(94, 97):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL29); M.update(M29)']
open('/home/claude/yamalar/metin_5_94_96.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
