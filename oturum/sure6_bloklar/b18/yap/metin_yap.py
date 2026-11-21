# sûre 6 blok 18 (6:74-78) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b18/say2.txt'
os.environ['OLC'] = '/home/claude/b18/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'İbrâhîm: yıldız, ay ve güneş' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 74: "Hani İbrâhîm babası Âzer'e demişti: Putları ilahlar mı ediniyorsun? Ben seni ve kavmini apaçık bir sapıklık içinde görüyorum.",
 75: "Böylece İbrâhîm'e göklerin ve yerin melekûtunu gösteriyorduk; kesin bilenlerden olsun diye.",
 76: "Gece onu örtünce bir yıldız gördü; Bu benim Rabbim, dedi. Batınca: Batanları sevmem, dedi.",
 77: "Ayı doğarken görünce: Bu benim Rabbim, dedi. Batınca: Rabbim beni doğru yola iletmezse mutlaka sapık kavimden olurum, dedi.",
 78: "Güneşi doğarken görünce: Bu benim Rabbim, bu daha büyük, dedi. Batınca: Ey kavmim, ben ortak koştuklarınızdan uzağım, dedi.",
}

T = {}
T[74] = ("'qâle' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'li-ebîhi' 3MS (adsız; gönderge 'ibrâhîmu' 3. kelime, 4. kelime); "
         "muhatap 2MS (adsız; söz içi; 'e-tettexizu', 'erâke', 've qavmeke' — 6., 10. ve 11. kelime; gönderge 'âzer' 5. kelime); konuşan 1S (adsız; söz içi; 'innî', 'erâke' — 9. ve 10. kelime; gönderge 'ibrâhîmu' 3. kelime)")
T[75] = ("konuşan 1P (adsız; 'nurî' — 2. kelime); 've li-yekûne' 3MS (adsız; gönderge 'ibrâhîme' 3. kelime, 7. kelime)")
T[76] = ("'cenne' 3MS (fiil uyumu; 2. kelime — fail 4. kelime); ''aleyhi', 'ra'â', 'qâle', 'qâle' 3MS (adsız; gönderge 6:75 3. kelime — 3., 5., 7. ve 12. kelime); "
         "'efele' 3MS (adsız; gönderge 'kevkeben' 6. kelime, 11. kelime); konuşan 1S (adsız; söz içi; 'rabbî', 'uhibbu' — 9. ve 14. kelime); söz fiili notu: 7. kelime — fail 9. kelime değil (9. kelime söz içi)")
T[77] = ("'ra'a', 'qâle', 'qâle' 3MS (adsız; gönderge 6:75 3. kelime — 2., 5. ve 10. kelime); 'efele' 3MS (adsız; gönderge 'l-qamera' 3. kelime, 9. kelime); "
         "'yehdinî' 3MS (fiil uyumu; 13. kelime — fail 14. kelime; nesne zamiri 1S — konuşan, söz içi); konuşan 1S (adsız; söz içi; 'rabbî', 'rabbî', 'le-ekûnenne' — 7., 14. ve 15. kelime); söz fiili notu: 5. kelime — fail 7. kelime değil (7. kelime söz içi)")
T[78] = ("'ra'a', 'qâle', 'qâle' 3MS (adsız; gönderge 6:75 3. kelime — 2., 5. ve 12. kelime); 'efelet' 3FS (adsız; gönderge 'ş-şemse' 3. kelime, 11. kelime); "
         "konuşan 1S (adsız; söz içi; 'rabbî', 'yâ qavmi', 'innî' — 7., 13. ve 14. kelime); muhatap 2MP (adsız; söz içi; 'tuşrikûn' — 17. kelime; gönderge 'yâ qavmi' 13. kelime); söz fiili notu: 5. kelime — fail 7. kelime değil, 12. kelime — fail 15. kelime değil (7. ve 15. kelime söz içi)")

D = {}
D[74] = ("◇ 've iz qâle ibrâhîmu li-ebîhi âzera e-tettexizu esnâmen âliheh, innî erâke ve qavmeke fî dalâlin mubîn' — "
 "'ve' + 'iz' + PERF 3MS I. bab + özel ad 'ibrâhîm' + 'li' + 'eb' + 3MS + özel ad 'âzer' + 'e' + IMPF 2MS VIII. bab + nekre çoğul 'esnâm' + nekre çoğul 'ilâh' + 'inne' + 1S + IMPF 1S I. bab + 2MS + 've' + 'qavm' + 2MS + 'fî' + nekre 'dalâl' + nekre etken ortaç 'mubîn' "
 "(ölçüm edim soru, kip INTG 1; 1S 2 · 2MS 3 · 3MS 2; bab I. bab ×2 · VIII. bab ×1). "
 "Allah lafzı yok; Rab yok; ölçüm '{{1|esmâ مُبِين 14\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' — ölçüm MÜHÜRSÜZ ile uyuşmuyor, araç tanımı farkı (muhur_el hayır, ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'fî dalâlin mubîn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); "
 "ölçüm '{{1|aktör: adlı إِبْراهِيم 3\\. sırada \\(kisi, rol fail\\+konusan\\)}}' ve '{{1|adlı آزَر 5\\. sırada \\(kisi, rol mecrur\\)}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=14 (n z=0,17); ölçüm '{{1|fâsıla مبين → ن, N sınıfı}}' — satır aynen (6:73 ر → 6:74 ن); "
 "ölçüm '{{1|harf 62 → harf3 58, isaret 4}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen; ölçümde simetri alanı yok. "
 "Ölçüm INTG 1: 'e-tettexizu' (6. kelime); 've iz' (1.) kelimesindeki 've' REM, 'iz' T; 've qavmeke' (11.) kelimesindeki 've' CONJ; 'innî' (9.) ACC (okuma). "
 "Kök ikilemesi yok (ölçüm). "
 + T[74] + " (okuma). "
 + cumle(say('say 6:74 1-4', "ve iz qâle ibrâhîmu li-ebîh", True)) + ' '
 "Ölçüm xref yok; ölçüm bağ yok (esit2, nakarat3, xref üçü de boş). "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'iz' + PERF + özel ad + 'li' + izafet + özel ad + 'e' + IMPF + nekre + nekre + 'inne' + IMPF + 've' + izafet + 'fî' + nekre + nekre; "
 "D2 soru; INTG ('e-tettexizu' 6. kelime); D3 —; 43:26 eşi; D4 1S 2 · 2MS 3 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[74] + "; aktör adlı 'ibrâhîmu' (3. kelime; ölçüm rol fail ve konuşan), 'âzer' (5. kelime; ölçüm rol mecrur); A2 İbrâhîm'in babasına putları ilah edinme sorusu; babasını ve kavmini apaçık sapıklıkta görme; "
 "A3 'e-tettexizu esnâmen âliheh, innî erâke ve qavmeke fî dalâlin mubîn' (söz içi, 6-14. kelime); "
 "A4 " + BOLUM + "; söz açılır (6. kelime); söz kapanır (14. kelime, ayet içi); şahıs geçişi 3 → 2 (ayetler arası); edim geçişi emir → soru (ayetler arası); bölüm açılışı.",
)

D[75] = ("◇ 've kezâlike nurî ibrâhîme melekûte's-semâvâti ve'l-ardi ve li-yekûne mine'l-mûqinîn' — "
 "'ve' + 'ke' + 'zâ' + IMPF 1P IV. bab + özel ad 'ibrâhîm' + 'melekût' + belirli çoğul 'semâ'' + 've' + belirli 'ard' + 've' + 'li' + IMPF 3MS I. bab + 'min' + belirli çoğul etken ortaç 'mûqin' "
 "(ölçüm edim haber, kip yok; 1P 1 · 3MS 1; bab I. bab ×1 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm '{{2|aktör: adlı إِبْراهِيم 3\\. sırada \\(kisi, rol meful\\)}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=9 (n z=-0,36); ölçüm '{{2|fâsıla ٱلموقنين → ن, N sınıfı}}' — satır aynen (6:74 ن → 6:75 ن); "
 "ölçüm '{{2|harf 47 → harf3 47, isaret 0}}' — satır aynen; ölçüm '{{2|dış düğüm 1}}' — satır aynen; ölçümde simetri alanı yok. "
 "Ölçüm kip yok; 've kezâlike' (1.) kelimesindeki 've' REM; 've li-yekûne' (7.) kelimesindeki 've' CONJ, 'li' PRP (okuma). "
 "Kök ikilemesi yok (ölçüm). "
 + T[75] + " (okuma). "
 + cumle(say('say 6:75 4-6', "melekûte's-semâvâti ve'l-ard"), say('dizi 6 75 4 6', "melekût semâ' ard")) + ' '
 "Ölçüm xref okunmamış 1 ayet. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 's-semâvâti' / 've'l-ardi' — ayetler arası: yok.",
 "◈K — K1 's-semâvâti' (5. kelime), 'l-ardi' (6. kelime).",
 "◈B — —",
 "◈D — D1 've' + 'ke' + 'zâ' + IMPF + özel ad + izafet + belirli + 've' + belirli + 've' + 'li' + IMPF + 'min' + belirli; "
 "D2 haber; D3 —; D4 1P 1 · 3MS 1, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[75] + "; aktör adlı 'ibrâhîme' (3. kelime; ölçüm rol meful); A2 İbrâhîm'e göklerin ve yerin melekûtunu gösterme; kesin bilenlerden olması; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 1 (ayetler arası); edim geçişi soru → haber (ayetler arası); şahıs sayısında beraberlik (1P 1 / 3MS 1 — ölçüm baskın 1).",
)

D[76] = ("◇ 'fe-lemmâ cenne 'aleyhi'l-leylu ra'â kevkeben qâle hâzâ rabbî fe-lemmâ efele qâle lâ uhibbu'l-âfilîn' — "
 "'fe' + 'lemmâ' + PERF 3MS I. bab + ''alâ' + 3MS + belirli 'leyl' + PERF 3MS I. bab + nekre 'kevkeb' + PERF 3MS I. bab + 'hâ' + 'zâ' + 'rabb' + 1S + 'fe' + 'lemmâ' + PERF 3MS I. bab + PERF 3MS I. bab + 'lâ' + IMPF 1S IV. bab + belirli çoğul etken ortaç 'âfil' "
 "(ölçüm edim haber, kip NEG 1; 1S 2 · 3MS 6; bab I. bab ×5 · IV. bab ×1). "
 "Allah lafzı yok; Rab 9. sırada (ölçüm rab z=1,10); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=15 (n z=0,27); ölçüm '{{3|biçim DIKKAT}}' — satır aynen; ölçüm '{{3|fâsıla ٱلءافلين → ن, N sınıfı}}' — satır aynen (6:75 ن → 6:76 ن); "
 "ölçüm '{{3|simetri \\[3, 1, 8, 1\\]}}' — satır aynen; ölçüm '{{3|harf 57 → harf3 54, isaret 3}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 1: 'lâ' (13. kelime); 'fe-lemmâ' (1. ve 10. kelime) — 'fe' CONJ, 'lemmâ' T; 'hâzâ' (8.) ATT + DEM (okuma). "
 "Kök ikilemesi (ölçüm) أفل ×2 ('efele' 11. / 'l-âfilîn' 15. kelime), قول ×2 ('qâle' 7. / 12. kelime) (okuma). "
 + T[76] + " (okuma). "
 + cumle(say('say 6:76 7-9', "qâle hâzâ rabbî"), say('dizi 6 76 7 9', "qâle zâ rabb"), say('dizi 6 76 7 12', "qâle zâ rabb lemmâ efele qâle")) + ' '
 + cumle(say('say 6:76 10-12', "fe-lemmâ efele qâle"), say('dizi 6 76 10 12', "lemmâ efele qâle")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: 'qâle _ rabb _ efele qâle' süzgeç GEÇER, 'qâle _ rabb' süzgeç GEÇER, '_ efele qâle' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'ra'â kevkeben' / 'efele' — ayetler arası: yok.",
 "◈K — K1 'l-leylu' (4. kelime), 'kevkeben' (6. kelime).",
 "◈B — —",
 "◈D — D1 'fe' + 'lemmâ' + PERF + ''alâ' + belirli + PERF + nekre + PERF + 'hâ' + 'zâ' + izafet + 'fe' + 'lemmâ' + PERF + PERF + 'lâ' + IMPF + belirli; "
 "D2 haber; NEG ('lâ' 13. kelime); D3 أفل ×2, قول ×2; D4 1S 2 · 3MS 6, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[76] + "; aktör yok (ölçüm); A2 gece örtünce yıldızı görme; 'bu benim Rabbim' sözü; batınca batanları sevmeme; "
 "A3 'hâzâ rabbî' (söz içi, 8-9. kelime); 'lâ uhibbu'l-âfilîn' (söz içi, 13-15. kelime); "
 "A4 " + BOLUM + "; söz açılır (8. kelime); söz kapanır (9. kelime, ayet içi); söz açılır (13. kelime); söz kapanır (15. kelime, ayet içi); şahıs geçişi 1 → 3 (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[77] = ("◇ 'fe-lemmâ ra'a'l-qamera bâziğan qâle hâzâ rabbî fe-lemmâ efele qâle le-in lem yehdinî rabbî le-ekûnenne mine'l-qavmi'd-dâllîn' — "
 "'fe' + 'lemmâ' + PERF 3MS I. bab + belirli 'qamer' + nekre etken ortaç 'bâziğ' + PERF 3MS I. bab + 'hâ' + 'zâ' + 'rabb' + 1S + 'fe' + 'lemmâ' + PERF 3MS I. bab + PERF 3MS I. bab + 'le' + 'in' + 'lem' + IMPF 3MS I. bab + 1S + 'rabb' + 1S + "
 "'le' + IMPF 1S I. bab + tekit nûnu + 'min' + belirli 'qavm' + belirli çoğul etken ortaç 'dâll' "
 "(ölçüm edim şart, kip COND 1 · EMPH 3 · NEG 1; 1S 4 · 3MS 5; bab I. bab ×6). "
 "Allah lafzı yok; Rab 7. ve 14. sırada (ölçüm rab z=2,05); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=18 (n z=0,59); ölçüm '{{4|biçim DIKKAT}}' — satır aynen; ölçüm '{{4|fâsıla ٱلضآلين → ن, N sınıfı}}' — satır aynen (6:76 ن → 6:77 ن); "
 "ölçüm '{{4|simetri \\[3, 5, 10, 1\\]}}' — satır aynen; ölçüm '{{4|harf 71 → harf3 69, isaret 2}}' — satır aynen; ölçüm '{{4|dış düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 'le-in' (11. kelime); EMPH 3: 'le-in' (11. kelime), 'le-ekûnenne' (15. kelime; lâm ve tekit nûnu); NEG 1: 'lem' (12. kelime); 'fe-lemmâ' (1. ve 8. kelime) — 'fe' CONJ, 'lemmâ' T; 'hâzâ' (6.) ATT + DEM (okuma). "
 "Kök ikilemesi (ölçüm) ربب ×2 ('rabbî' 7. / 14. kelime), قول ×2 ('qâle' 5. / 10. kelime) (okuma). "
 + T[77] + " (okuma). "
 + cumle(say('say 6:77 5-7', "qâle hâzâ rabbî"), say('dizi 6 77 5 7', "qâle zâ rabb"), say('dizi 6 77 5 10', "qâle zâ rabb lemmâ efele qâle"), say('dizi 6 77 8 10', "lemmâ efele qâle")) + ' '
 + cumle(say('say 6:77 10-11', "qâle le-in")) + ' '
 "Ölçüm xref okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'qâle _ rabb _ efele qâle' süzgeç GEÇER, 'qâle _ rabb' süzgeç GEÇER, '_ efele qâle' süzgeç GEÇER, 'rabb kâne _' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'bâziğan' / 'efele' — ayetler arası: yok.",
 "◈K — K1 'l-qamera' (3. kelime).",
 "◈B — —",
 "◈D — D1 'fe' + 'lemmâ' + PERF + belirli + nekre + PERF + 'hâ' + 'zâ' + izafet + 'fe' + 'lemmâ' + PERF + PERF + 'le' + 'in' + 'lem' + IMPF + izafet + 'le' + IMPF + 'min' + belirli + belirli; "
 "D2 şart; COND ('le-in' 11. kelime), EMPH ('le-in' 11. kelime, 'le-ekûnenne' 15. kelime), NEG ('lem' 12. kelime); D3 ربب ×2, قول ×2; D4 1S 4 · 3MS 5, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[77] + "; aktör yok (ölçüm); A2 ayı doğarken görme; 'bu benim Rabbim' sözü; batınca Rabbin doğru yola iletmesi şartı; sapık kavimden olma; "
 "A3 'hâzâ rabbî' (söz içi, 6-7. kelime); 'le-in lem yehdinî rabbî le-ekûnenne mine'l-qavmi'd-dâllîn' (söz içi, 11-18. kelime); "
 "A4 " + BOLUM + "; söz açılır (6. kelime); söz kapanır (7. kelime, ayet içi); söz açılır (11. kelime); söz kapanır (18. kelime, ayet içi); "
 "şart → cevap (ayet içi; COND 'in' 11. kelime: 'le-in lem yehdinî rabbî' / 'le-ekûnenne mine'l-qavmi'd-dâllîn' (15. kelime)); şahıs geçişi yok (ayetler arası); edim geçişi haber → şart (ayetler arası).",
)

D[78] = ("◇ 'fe-lemmâ ra'a'ş-şemse bâziğaten qâle hâzâ rabbî hâzâ ekber, fe-lemmâ efelet qâle yâ qavmi innî berî'un mimmâ tuşrikûn' — "
 "'fe' + 'lemmâ' + PERF 3MS I. bab + belirli 'şems' + nekre etken ortaç 'bâziğa' + PERF 3MS I. bab + 'hâ' + 'zâ' + 'rabb' + 1S + 'hâ' + 'zâ' + 'ekber' + 'fe' + 'lemmâ' + PERF 3FS I. bab + PERF 3MS I. bab + 'yâ' + 'qavm' + 1S + 'inne' + 1S + nekre 'berî'' + 'min' + 'mâ' + IMPF 2MP IV. bab + 2MP "
 "(ölçüm edim nida, kip VOC 1; 1S 3 · 2MP 2 · 3FS 1 · 3MS 3; bab I. bab ×4 · IV. bab ×1). "
 "Allah lafzı yok; Rab 7. sırada (ölçüm rab z=0,93); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=17 (n z=0,49); ölçüm '{{5|biçim DIKKAT}}' — satır aynen; ölçüm '{{5|fâsıla تشركون → ن, N sınıfı}}' — satır aynen (6:77 ن → 6:78 ن); "
 "ölçüm '{{5|simetri \\[3, 6, 14, 1\\]}}' — satır aynen; ölçüm '{{5|harf 67 → harf3 64, isaret 3}}' — satır aynen; ölçüm '{{5|dış düğüm 1}}' — satır aynen. "
 "Ölçüm VOC 1: 'yâ qavmi' (13. kelime); 'fe-lemmâ' (1. ve 10. kelime) — 'fe' CONJ, 'lemmâ' T; 'hâzâ' (6. ve 8.) ATT + DEM; 'innî' (14.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) قول ×2 ('qâle' 5. / 12. kelime) (okuma). "
 + T[78] + " (okuma). "
 + cumle(say('say 6:78 15-17', "berî'un mimmâ tuşrikûn", True), say('dizi 6 78 15 17', "berî' mimmâ eşrake")) + ' '
 + cumle(say('say 6:78 5-7', "qâle hâzâ rabbî"), say('dizi 6 78 5 7', "qâle zâ rabb"), say('dizi 6 78 10 12', "lemmâ efele qâle"), say('say 6:78 13-14', "yâ qavmi innî")) + ' '
 "Ölçüm xref okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'qâle _ rabb' süzgeç GEÇER, '_ efele qâle' süzgeç GEÇER, 'berî' _ eşrake' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'bâziğaten' / 'efelet' — ayetler arası: yok.",
 "◈K — K1 'ş-şemse' (3. kelime).",
 "◈B — —",
 "◈D — D1 'fe' + 'lemmâ' + PERF + belirli + nekre + PERF + 'hâ' + 'zâ' + izafet + 'hâ' + 'zâ' + 'ekber' + 'fe' + 'lemmâ' + PERF + PERF + 'yâ' + izafet + 'inne' + nekre + 'min' + 'mâ' + IMPF; "
 "D2 nida; VOC ('yâ qavmi' 13. kelime); D3 قول ×2; 11:54 eşi; D4 1S 3 · 2MP 2 · 3FS 1 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[78] + "; aktör yok (ölçüm); A2 güneşi doğarken görme; 'bu benim Rabbim, bu daha büyük' sözü; batınca kavmine ortak koştuklarından uzak olduğunu söyleme; "
 "A3 'hâzâ rabbî hâzâ ekber' (söz içi, 6-9. kelime); 'yâ qavmi innî berî'un mimmâ tuşrikûn' (söz içi, 13-17. kelime); "
 "A4 " + BOLUM + "; söz açılır (6. kelime); söz kapanır (9. kelime, ayet içi); söz açılır (13. kelime); söz kapanır (17. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi şart → nida (ayetler arası).",
)
out = ['# ── blok 6:74-78 (2026-11-21) ──', 'MEAL18 = {']
for n in range(74, 79):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M18 = {']
for n in range(74, 79):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL18); M.update(M18)']
open('/home/claude/yamalar/metin_6_74_78.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
