# sûre 6 blok 13 (6:54-58) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b13/say2.txt'
os.environ['OLC'] = '/home/claude/b13/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'De ki: gaybı bilmem; sabah akşam Rablerine dua edenler' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 54: "Âyetlerimize iman edenler sana geldiği zaman de ki: Selam size; Rabbiniz rahmeti kendi üzerine yazdı: Sizden kim bilmeyerek bir kötülük işler, sonra ardından tövbe eder ve düzeltirse, şüphesiz O bağışlayandır, merhamet edendir.",
 55: "Böylece âyetleri ayrıntılı açıklarız; suçluların yolu belli olsun diye.",
 56: "De ki: Allah'ı bırakıp dua ettiklerinize kulluk etmekten men edildim. De ki: Heveslerinize uymam; o takdirde sapmış olurum ve ben doğru yolu bulanlardan değilim.",
 57: "De ki: Şüphesiz ben Rabbimden açık bir delil üzerindeyim, siz ise onu yalanladınız. Acele istediğiniz şey yanımda değildir. Hüküm ancak Allah'ındır; hakkı söyler ve O ayırt edenlerin en hayırlısıdır.",
 58: "De ki: Acele istediğiniz şey yanımda olsaydı, benimle sizin aranızdaki iş bitirilmiş olurdu. Allah zalimleri daha iyi bilendir.",
}

T = {}
T[54] = ("konuşan 1P (adsız; 'bi-âyâtinâ' — 5. kelime); muhatap 2MS (adsız; 'câ'eke', 'fe-qul' — 2. ve 6. kelime); 'câ'eke' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); "
         "'yu'minûne' 3MP (adsız; gönderge 'llezîne' 3. kelime, 4. kelime); muhatap 2MP (adsız; söz içi; ''aleykum', 'rabbukum', 'minkum' — 8., 10. ve 17. kelime); "
         "'ketebe' 3MS (fiil uyumu; 9. kelime — fail 10. kelime); 'nefsihi', 'ennehû', 'fe-ennehû' 3MS (adsız; gönderge 'rabbukum' 10. kelime — 12., 14. ve 25. kelime); "
         "''amile', 'tâbe', 've asleha' 3MS (adsız; gönderge 'men' 15. kelime — 16., 21. ve 24. kelime); 'ba'dihî' 3MS (adsız; gönderge 'sû'en' 18. kelime, 23. kelime)")
T[55] = ("konuşan 1P (adsız; 'nufassilu' — 2. kelime); 'li-testebîne' 3FS (fiil uyumu; 4. kelime — fail 5. kelime)")
T[56] = ("muhatap 2MS (adsız; 'qul', 'qul' — 1. ve 11. kelime); konuşan 1S (adsız; söz içi; 'innî', 'a'bude', 'ettebi'u', 'dalaltu', 'ene' — 2., 5., 13., 16. ve 19. kelime); "
         "'nuhîtu' 1S (adsız; söz içi; edilgen — naib-i faili zamir, 3. kelime); muhatap 2MP (adsız; söz içi; 'ted'ûne', 'ehvâ'akum' — 7. ve 14. kelime)")
T[57] = ("muhatap 2MS (adsız; 'qul' — 1. kelime); konuşan 1S (adsız; söz içi; 'innî', 'rabbî', ''indî' — 2., 6. ve 10. kelime); muhatap 2MP (adsız; söz içi; 've kezzebtum', 'testa'cilûne' — 7. ve 12. kelime); "
         "'bih' 3MS (adsız; gönderge 'rabbî' 6. kelime, 8. kelime); 'bih' 3MS (adsız; gönderge 'mâ' 11. kelime, 13. kelime); 'yequssu', 've huve' 3MS (adsız; gönderge 'li'llâh' 17. kelime — 18. ve 20. kelime)")
T[58] = ("muhatap 2MS (adsız; 'qul' — 1. kelime); konuşan 1S (adsız; söz içi; ''indî', 'beynî' — 4. ve 10. kelime); muhatap 2MP (adsız; söz içi; 'testa'cilûne', 've beynekum' — 6. ve 11. kelime); "
         "'bihî' 3MS (adsız; gönderge 'mâ' 5. kelime, 7. kelime); 'le-qudiye' 3MS (fiil uyumu; edilgen; naib-i faili 'l-emru' (9. kelimedeki ad), 8. kelime)")

D = {}
D[54] = ("◇ 've izâ câ'eke'llezîne yu'minûne bi-âyâtinâ fe-qul selâmun 'aleykum, ketebe rabbukum 'alâ nefsihi'r-rahmete ennehû men 'amile minkum sû'en bi-cehâletin summe tâbe min ba'dihî ve asleha fe-ennehû ğafûrun rahîm' — "
 "'ve' + 'izâ' + PERF 3MS I. bab + 2MS + 'ellezî' + IMPF 3MP IV. bab + 'bi' + çoğul 'âye' + 1P + 'fe' + IMPV 2MS I. bab + nekre 'selâm' + ''alâ' + 2MP + PERF 3MS I. bab + 'rabb' + 2MP + ''alâ' + 'nefs' + 3MS + belirli 'rahme' + "
 "'enne' + 3MS + 'men' + PERF 3MS I. bab + 'min' + 2MP + nekre 'sû'' + 'bi' + nekre 'cehâle' + 'summe' + PERF 3MS I. bab + 'min' + 'ba'd' + 3MS + 've' + PERF 3MS IV. bab + 'fe' + 'enne' + 3MS + nekre 'ğafûr' + nekre 'rahîm' "
 "(ölçüm edim emir, şart, kip COND 1 · IMPV 1; 1P 1 · 2MP 3 · 2MS 2 · 3MP 2 · 3MS 9; bab I. bab ×5 · IV. bab ×2). "
 "Allah lafzı yok; Rab 10. sırada (ölçüm rab z=0,47); ölçüm '{{1|esmâ سَلام 7\\. sırada, ORTA konum, MÜHÜR \\| غَفُور 26\\. sırada, SON konum, MÜHÜR \\| رَحِيم 27\\. sırada, SON konum, MÜHÜR}}' — satır aynen; esma_kayit çıktısı 'mühür EVET (ÇİFT) ton cemâl' — ölçüm MÜHÜR ile uyuşuyor (muhur_el EVET); "
 "esma_el kaydı 'degil' — 'fe-qul selâmun 'aleykum', kural 'esmâ adı esmâ dışı göndergeyle → degil' (selamlama) (okuma); esma_el kaydı 'ilahi' — 'fe-ennehû ğafûrun rahîm', kural ''inne/enne' haberi → ilahi' (Allah) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=27 (n z=1,55); "
 "ölçüm '{{1|fâsıla رحيم → م, N sınıfı}}' — satır aynen (6:53 ن → 6:54 م); ölçüm '{{1|simetri \\[3, 1, 15, 1\\]}}' — satır aynen; ölçüm '{{1|harf 116 → harf3 106, isaret 10}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen. "
 "Ölçüm COND 1: 'men' (15. kelime); IMPV 1: 'fe-qul' (6. kelime); 've izâ' (1.) kelimesindeki 've' REM; 'fe-qul' (6.) ve 'fe-ennehû' (25.) kelimelerindeki 'fe' RSLT; 've asleha' (24.) kelimesindeki 've' CONJ; 'izâ' (1.) T; 'ennehû' (14.) ve 'fe-ennehû' (25.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) رحم ×2 ('r-rahmete' 13. / 'rahîm' 27. kelime) (okuma). "
 + T[54] + " (okuma). "
 + cumle(say('say 6:54 11-13', "'alâ nefsihi'r-rahme", True), say('dizi 6 54 11 13', "'alâ nefs rahme")) + ' '
 + cumle(say('dizi 6 54 18 23', "sû' cehâle summe tâbe min ba'd"), say('say 6:54 26-27', "ğafûrun rahîm")) + ' '
 "Ölçüm xref 16:119 (emsal olarak basıldı) ve okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: ''alâ nefs rahme' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'sû'en' / 've asleha' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'izâ' + PERF + 'ellezî' + IMPF + 'bi' + izafet + 'fe' + IMPV + nekre + ''alâ' + PERF + izafet + ''alâ' + izafet + belirli + 'enne' + 'men' + PERF + 'min' + nekre + 'bi' + nekre + 'summe' + PERF + 'min' + izafet + 've' + PERF + 'fe' + 'enne' + nekre + nekre; "
 "D2 emir, şart; COND ('men' 15. kelime), IMPV ('fe-qul' 6. kelime); D3 رحم ×2; 16:119 eşi; D4 1P 1 · 2MP 3 · 2MS 2 · 3MP 2 · 3MS 9, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[54] + "; aktör yok (ölçüm); A2 iman edenlere selam; Rabbin rahmeti kendi üzerine yazması; bilmeyerek kötülük işleyip tövbe edene bağışlama; "
 "A3 'selâmun 'aleykum, ketebe rabbukum 'alâ nefsihi'r-rahmete ennehû men 'amile minkum sû'en bi-cehâletin summe tâbe min ba'dihî ve asleha fe-ennehû ğafûrun rahîm' (söz içi, 7-27. kelime); "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; COND 'men' 15. kelime: 'men 'amile minkum sû'en bi-cehâle' / 'fe-ennehû ğafûrun rahîm' (25. kelime)); söz açılır (7. kelime); söz kapanır (27. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi soru → emir, şart (ayetler arası).",
)

D[55] = ("◇ 've kezâlike nufassilu'l-âyâti ve li-testebîne sebîlu'l-mucrimîn' — "
 "'ve' + 'ke' + 'zâlike' + IMPF 1P II. bab + belirli çoğul 'âye' + 've' + 'li' + IMPF 3FS X. bab + 'sebîl' + belirli çoğul etken ortaç 'mucrim' "
 "(ölçüm edim haber, kip yok; 1P 1 · 3FS 1; bab II. bab ×1 · X. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=6 (n z=-0,68); ölçüm '{{2|fâsıla ٱلمجرمين → ن, N sınıfı}}' — satır aynen (6:54 م → 6:55 ن); "
 "ölçüm '{{2|harf 35 → harf3 35, isaret 0}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; 've kezâlike' (1.) kelimesindeki 've' REM; 've li-testebîne' (4.) kelimesindeki 've' CONJ, 'li' PRP (okuma). "
 + T[55] + " (okuma). "
 + cumle(say('say 6:55 1-3', "ve kezâlike nufassilu'l-âyât", True), say('say 6:55 2-3', "nufassilu'l-âyât")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'ke' + 'zâlike' + IMPF + belirli + 've' + 'li' + IMPF + izafet + belirli; "
 "D2 haber; D3 —; D4 1P 1 · 3FS 1, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[55] + "; aktör yok (ölçüm); A2 âyetlerin ayrıntılı açıklanması; suçluların yolunun belli olması; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 1 (ayetler arası); edim geçişi emir, şart → haber (ayetler arası); şahıs sayısında beraberlik (1P 1 · 3FS 1 — ölçüm baskın 1).",
)

D[56] = ("◇ 'qul innî nuhîtu en a'bude'llezîne ted'ûne min dûni'llâh, qul lâ ettebi'u ehvâ'akum qad dalaltu izen ve mâ ene mine'l-muhtedîn' — "
 "IMPV 2MS I. bab + 'inne' + 1S + edilgen PERF 1S I. bab + 'en' + IMPF 1S I. bab + 'ellezî' + IMPF 2MP I. bab + 'min' + 'dûn' + lafız + IMPV 2MS I. bab + 'lâ' + IMPF 1S VIII. bab + çoğul 'ehvâ'' + 2MP + 'qad' + PERF 1S I. bab + 'izen' + 've' + 'mâ' + 'ene' + 'min' + belirli çoğul etken ortaç 'muhtedî' "
 "(ölçüm edim emir, kip CERT 1 · IMPV 2 · NEG 2; 1S 8 · 2MP 3 · 2MS 2; bab I. bab ×6 · VIII. bab ×1). "
 "Allah lafzı 10. sırada (ölçüm allah z=0,42); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=21 (n z=0,91); ölçüm '{{3|EDİLGEN 1/7 fiil, pas z=0,48}}' — satır aynen; ölçüm '{{3|fâsıla ٱلمهتدين → ن, N sınıfı}}' — satır aynen (6:55 ن → 6:56 ن); "
 "ölçüm '{{3|simetri \\[3, 1, 11, 1\\]}}' — satır aynen; ölçüm '{{3|harf 78 → harf3 74, isaret 4}}' — satır aynen; ölçüm '{{3|dış düğüm 1}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (15. kelime); IMPV 2: 'qul' (1. ve 11. kelime); NEG 2: 'lâ' (12. kelime), 've mâ' (18. kelime); 've mâ' (18.) kelimesindeki 've' REM; 'innî' (2.) ACC; 'en' (4.) SUB; 'izen' (17.) ANS (okuma). "
 "Kök ikilemesi (ölçüm) قول ×2 ('qul' 1. / 'qul' 11. kelime) (okuma). "
 + T[56] + " (okuma). "
 + cumle(say('say 6:56 1-10', "qul innî nuhîtu en a'bude'llezîne ted'ûne min dûni'llâh", True), say('dizi 6 56 6 10', "ellezî de'â min dûn allâh"), say('dizi 6 56 7 10', "de'â min dûn allâh")) + ' '
 + cumle(say('say 6:56 12-14', "lâ ettebi'u ehvâ'akum", True), say('dizi 6 56 12 14', "lâ ittebe ehvâ'"), say('say 6:56 18-20', "ve mâ ene mine")) + ' '
 "Ölçüm xref 40:66 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıpları: 'ellezî de'â min dûn allâh' süzgeç GEÇER, 'de'â min dûn allâh' süzgeç GEÇER, 'min dûn allâh' süzgeç GEÇER, 'lâ ittebe ehvâ'' süzgeç GEÇMEZ, 'mâ ene min' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'dalaltu' / 'l-muhtedîn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'inne' + PERF + 'en' + IMPF + 'ellezî' + IMPF + 'min' + izafet + lafız + IMPV + 'lâ' + IMPF + izafet + 'qad' + PERF + 'izen' + 've' + 'mâ' + 'ene' + 'min' + belirli; "
 "D2 emir; IMPV ('qul' 1. kelime, 'qul' 11. kelime), NEG ('lâ' 12. kelime, 've mâ' 18. kelime), CERT ('qad' 15. kelime); D3 قول ×2; 40:66 eşi; D4 1S 8 · 2MP 3 · 2MS 2, sahset ['1', '2'], iltifât 0.",
 "◈A — A1 " + T[56] + "; aktör yok (ölçüm); A2 Allah'ı bırakıp dua edilenlere kulluk yasağı; heveslere uymama; sapma ve doğru yoldan olmama; "
 "A3 'innî nuhîtu en a'bude'llezîne ted'ûne min dûni'llâh' (söz içi, 2-10. kelime); 'lâ ettebi'u ehvâ'akum qad dalaltu izen ve mâ ene mine'l-muhtedîn' (söz içi, 12-21. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (10. kelime, ayet içi); söz açılır (12. kelime); söz kapanır (21. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi haber → emir (ayetler arası).",
)

D[57] = ("◇ 'qul innî 'alâ beyyinetin min rabbî ve kezzebtum bih, mâ 'indî mâ testa'cilûne bih, ini'l-hukmu illâ li'llâh, yequssu'l-haqqa ve huve xayru'l-fâsilîn' — "
 "IMPV 2MS I. bab + 'inne' + 1S + ''alâ' + nekre 'beyyine' + 'min' + 'rabb' + 1S + 've' + PERF 2MP II. bab + 'bi' + 3MS + 'mâ' + ''inde' + 1S + 'mâ' + IMPF 2MP X. bab + 'bi' + 3MS + 'in' + belirli 'hukm' + 'illâ' + 'li' + lafız + IMPF 3MS I. bab + belirli 'haqq' + 've' + 'huve' + 'xayr' + belirli çoğul etken ortaç 'fâsil' "
 "(ölçüm edim emir, kip IMPV 1 · NEG 2 · RES 1; 1S 3 · 2MP 4 · 2MS 1 · 3MS 4; bab I. bab ×2 · II. bab ×1 · X. bab ×1). "
 "Allah lafzı 17. sırada (ölçüm allah z=0,38); Rab 6. sırada (ölçüm rab z=0,65); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=22 (n z=1,02); ölçüm '{{4|biçim HASR}}' — satır aynen; ölçüm '{{4|fâsıla ٱلفصلين → ن, N sınıfı}}' — satır aynen (6:56 ن → 6:57 ن); "
 "ölçüm '{{4|simetri \\[4, 2, 8, 1\\]}}' — satır aynen; ölçüm '{{4|harf 83 → harf3 76, isaret 7}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm IMPV 1: 'qul' (1. kelime); NEG 2: 'mâ' (9. kelime), 'in' (14. kelime); RES 1: 'illâ' (16. kelime); 've kezzebtum' (7.) kelimesindeki 've' CONJ; 've huve' (20.) kelimesindeki 've' REM; 'innî' (2.) ACC (okuma). "
 + T[57] + " (okuma). "
 + cumle(say('say 6:57 10-13', "'indî mâ testa'cilûne bih", True), say('dizi 6 57 10 13', "'ind mâ ista'cele _")) + ' '
 + cumle(say('say 6:57 4-6', "beyyinetin min rabbî", True), say('dizi 6 57 4 6', "beyyine min rabb"), say('say 6:57 14-17', "ini'l-hukmu illâ li'llâh")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: ''ind mâ ista'cele _' süzgeç GEÇER, 'beyyine min rabb' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'inne' + ''alâ' + nekre + 'min' + izafet + 've' + PERF + 'bi' + 'mâ' + ''inde' + 'mâ' + IMPF + 'bi' + 'in' + belirli + 'illâ' + 'li' + lafız + IMPF + belirli + 've' + 'huve' + izafet + belirli; "
 "D2 emir; IMPV ('qul' 1. kelime), NEG ('mâ' 9. kelime, 'in' 14. kelime), RES ('illâ' 16. kelime); D3 —; D4 1S 3 · 2MP 4 · 2MS 1 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[57] + "; aktör yok (ölçüm); A2 Rabden açık delil üzerinde olma; yalanlama; acele istenenin elde olmaması; hükmün Allah'a ait olması; hakkı söyleme; "
 "A3 'innî 'alâ beyyinetin min rabbî ve kezzebtum bih, mâ 'indî mâ testa'cilûne bih, ini'l-hukmu illâ li'llâh, yequssu'l-haqq' (söz içi, 2-19. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (19. kelime, ayet içi); şahıs geçişi 1 → 2 (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[58] = ("◇ 'qul lev enne 'indî mâ testa'cilûne bihî le-qudiye'l-emru beynî ve beynekum, ve'llâhu a'lemu bi'z-zâlimîn' — "
 "IMPV 2MS I. bab + 'lev' + 'enne' + ''inde' + 1S + 'mâ' + IMPF 2MP X. bab + 'bi' + 3MS + 'le' + edilgen PERF 3MS I. bab + belirli 'emr' + 'beyn' + 1S + 've' + 'beyn' + 2MP + 've' + lafız + 'a'lem' + 'bi' + belirli çoğul etken ortaç 'zâlim' "
 "(ölçüm edim emir, şart, kip COND 1 · EMPH 1 · IMPV 1; 1S 2 · 2MP 3 · 2MS 1 · 3MS 2; bab I. bab ×2 · X. bab ×1). "
 "Allah lafzı 12. sırada (ölçüm allah z=0,90); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=14 (n z=0,17); ölçüm '{{5|EDİLGEN 1/3 fiil, pas z=1,57}}' — satır aynen; ölçüm '{{5|fâsıla بٱلظلمين → ن, N sınıfı}}' — satır aynen (6:57 ن → 6:58 ن); "
 "ölçüm '{{5|harf 60 → harf3 58, isaret 2}}' — satır aynen; ölçüm '{{5|dış düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 'lev' (2. kelime); EMPH 1: 'le-qudiye' (8. kelime); IMPV 1: 'qul' (1. kelime); 've beynekum' (11.) kelimesindeki 've' CONJ; 've'llâhu' (12.) kelimesindeki 've' REM; 'enne' (3.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) بين ×2 ('beynî' 10. / 've beynekum' 11. kelime) (okuma). "
 + T[58] + " (okuma). "
 + cumle(say('say 6:58 4-7', "'indî mâ testa'cilûne bih", True), say('dizi 6 58 4 7', "'ind mâ ista'cele _")) + ' '
 + cumle(say('say 6:58 8-9', "le-qudiye'l-emr", True), say('say 6:58 10-11', "beynî ve beynekum")) + ' '
 "Ölçüm xref okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: ''ind mâ ista'cele _' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'beynî' / 've beynekum' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'lev' + 'enne' + ''inde' + 'mâ' + IMPF + 'bi' + 'le' + PERF + belirli + izafet + 've' + izafet + 've' + lafız + 'a'lem' + 'bi' + belirli; "
 "D2 emir, şart; COND ('lev' 2. kelime), EMPH ('le-qudiye' 8. kelime), IMPV ('qul' 1. kelime); D3 بين ×2; D4 1S 2 · 2MP 3 · 2MS 1 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[58] + "; aktör yok (ölçüm); A2 acele istenen elde olsaydı işin bitirilmesi; Allah'ın zalimleri daha iyi bilmesi; "
 "A3 'lev enne 'indî mâ testa'cilûne bihî le-qudiye'l-emru beynî ve beynekum' (söz içi, 2-11. kelime); "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; COND 'lev' 2. kelime: 'lev enne 'indî mâ testa'cilûne bih' / 'le-qudiye'l-emru beynî ve beynekum' (8. kelime)); söz açılır (2. kelime); söz kapanır (11. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi emir → emir, şart (ayetler arası); bölüm kapanışı.",
)
out = ['# ── blok 6:54-58 (2026-11-20) ──', 'MEAL13 = {']
for n in range(54, 59):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M13 = {']
for n in range(54, 59):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL13); M.update(M13)']
open('/home/claude/yamalar/metin_6_54_58.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
