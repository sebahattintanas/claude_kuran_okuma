# blok 30 (5:97-100) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b30/say2.txt'
os.environ['OLC'] = '/home/claude/b30/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'İhramda av; Kâbe ve haram ay; elçinin görevi' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 97: "Allah Kâbe'yi, Haram Ev'i, insanlar için bir ayakta duruş kıldı; haram ayı, kurbanlığı ve gerdanlıkları da. Bu, Allah'ın göklerde olanı ve yerde olanı bildiğini ve Allah'ın her şeyi bilen olduğunu bilmeniz içindir.",
 98: "Bilin ki Allah'ın cezası çetindir ve Allah bağışlayandır, merhamet edendir.",
 99: "Elçiye düşen yalnızca tebliğdir. Allah açığa vurduğunuzu da gizlediğinizi de bilir.",
 100: "De ki: Kötü ile temiz bir olmaz, kötünün çokluğu hoşuna gitse bile. Ey akıl sahipleri, Allah'tan sakının; umulur ki kurtuluşa erersiniz.",
}

T97 = ("'ce'ale' 3MS (fiil uyumu; 1. kelime — fail 2. kelime); 'llâhu' ('ce'ale' faili; lafız; 2. kelime); 'l-ka'bete' (adlı yer; 'ce'ale' mef'ûlü; 3. kelime); "
       "muhatap 2MP (adsız; 'li-ta'lemû' — 13. kelime); 'llâhe' ('enne' ismi; lafız; 15. kelime); 'ya'lemu' 3MS (adsız; gönderge lafız, 16. kelime); 'llâhe' ('enne' ismi; lafız; 24. kelime)")
T98 = ("muhatap 2MP (adsız; 'i'lemû' — 1. kelime); 'llâhe' ('enne' ismi; lafız; 3. kelime); 'llâhe' ('enne' ismi; lafız; 7. kelime)")
T99 = ("'r-rasûli' (adlı rol; 3. kelime); 'llâhu' (mübtedâ; lafız; 6. kelime); 'ya'lemu' 3MS (adsız; gönderge lafız, 7. kelime); "
       "muhatap 2MP (adsız; 'tubdûne', 'tektumûn' — 9. ve 11. kelime)")
T100 = ("muhatap 2MS (adsız; 'qul', 'a'cebeke' — 1. ve 7. kelime); 'yestevi' 3MS (fiil uyumu; 3. kelime — fail 4. kelime); 'l-xabîsu ve't-tayyib' ('yestevi' faili; 4-5. kelime); "
        "'a'cebeke' 3MS (fiil uyumu; 7. kelime — fail 8. kelime); 'kesratu'l-xabîs' ('a'cebeke' faili; 8-9. kelime); muhatap 2MP (adsız; söz içi; 'ttequ', 'le'allekum', 'tuflihûn' — 10., 14. ve 15. kelime); "
        "'llâhe' ('ttequ' mef'ûlü; lafız; 11. kelime); 'uli'l-elbâb' (nida edilen; 12-13. kelime)")

D = {}
D[97] = ("◇ 'ce'ale'llâhu'l-ka'bete'l-beyte'l-harâme qiyâmen li'n-nâsi ve'ş-şehre'l-harâme ve'l-hedye ve'l-qalâ'ide zâlike li-ta'lemû enne'llâhe ya'lemu mâ fi's-semâvâti ve mâ fi'l-ardi ve enne'llâhe bi-kulli şey'in 'alîm' — "
 "PERF 3MS I. bab + lafız + belirli özel ad 'ka'be' + belirli 'beyt' + belirli 'harâm' + nekre çoğul etken ortaç 'qâ'im' + 'li' + belirli 'nâs' + 've' + belirli 'şehr' + belirli 'harâm' + 've' + belirli 'hedy' + 've' + belirli çoğul 'qalâ'id' + "
 "'zâlike' + 'li' + IMPF 2MP I. bab + 'enne' + lafız + IMPF 3MS I. bab + 'mâ' + 'fî' + belirli çoğul 'semâ'' + 've' + 'mâ' + 'fî' + belirli 'ard' + 've' + 'enne' + lafız + 'bi' + 'kull' + nekre 'şey'' + nekre ''alîm' "
 "(ölçüm edim haber, kip yok; 2MP 2 · 3MS 2; bab I. bab ×3). "
 "Allah lafzı 2., 15. ve 24. sırada (ölçüm allah z=1,69); Rab yok; ölçüm '{{1|esmâ عَلِيم 27\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton denge' (uyuşmuyor) — esma_el kaydı 'ilahi' — 've enne'llâhe bi-kulli şey'in 'alîm', kural ''inne/enne' haberi → ilahi' (lafzın haberi) (okuma); ölçüm aktör '{{1|adlı كَعْبَة 3\\. sırada \\(yer, rol meful\\)}}' — satır aynen. "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=27 (n z=1,55); ölçüm '{{1|fâsıla عليم → م, N sınıfı}}' — satır aynen; ölçüm '{{1|simetri \\[4, 12, 21, 1\\]}}' — satır aynen; "
 "ölçüm '{{1|harf 119 → harf3 115, isaret 4}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; 've'ş-şehre' (8.), 've'l-hedye' (10.), 've'l-qalâ'ide' (11.) ve 've mâ' (20.)'daki 've' CONJ, 've enne' (23.)'daki 've' REM, 'li-ta'lemû' (13.)'daki 'li' PRP (okuma). "
 "Kök ikilemesi (ölçüm) أله ×3 ('llâhu' 2., 'llâhe' 15. ve 24. kelime), حرم ×2 ('l-harâme' 5. / 9. kelime), علم ×3 ('li-ta'lemû' 13., 'ya'lemu' 16., ''alîm' 27. kelime) (okuma). "
 + T97 + " (okuma). "
 + cumle(say('say 5:97 1-5', "ce'ale'llâhu'l-ka'bete'l-beyte'l-harâm", True), say('say 5:97 1-2', "ce'ale'llâh"), say('say 5:97 3-5', "l-ka'bete'l-beyte'l-harâm"), say('say 5:97 4-5', "l-beyte'l-harâm"), say('say 5:97 6-7', "qiyâmen li'n-nâs")) + ' '
 + cumle(say('say 5:97 8-11 --on', "ve'ş-şehre'l-harâme ve'l-hedye ve'l-qalâ'id", True), say('say 5:97 8-9 --on', "ve'ş-şehre'l-harâm"), say('say 5:97 10-11 --on', "ve'l-hedye ve'l-qalâ'id")) + ' '
 + cumle(say('say 5:97 12-13', "zâlike li-ta'lemû", True), say('say 5:97 13-16', "li-ta'lemû enne'llâhe ya'lem"), say('say 5:97 13-15', "li-ta'lemû enne'llâh"), say('dizi 5 97 13 15', "'alime enne allâh"), say('say 5:97 14-16', "enne'llâhe ya'lem"),
         say('say 5:97 15-17', "llâhe ya'lemu mâ"), say('dizi 5 97 15 17', "allâh 'alime mâ"), say('say 5:97 16-18', "ya'lemu mâ fî"), say('dizi 5 97 16 18', "'alime mâ fî")) + ' '
 + cumle(say('say 5:97 16-22', "ya'lemu mâ fi's-semâvâti ve mâ fi'l-ard", True), say('say 5:97 17-22', "mâ fi's-semâvâti ve mâ fi'l-ard"), say('say 5:97 20-22 --on', "ve mâ fi'l-ard"), say('dizi 5 97 20 22', "mâ fî ard")) + ' '
 + cumle(say('say 5:97 23-27 --on', "ve enne'llâhe bi-kulli şey'in 'alîm", True), say('say 5:97 24-27', "llâhe bi-kulli şey'in 'alîm"), say('say 5:97 25-27', "bi-kulli şey'in 'alîm")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: ''alime enne allâh' süzgeç GEÇER, 'mâ fî ard', 'allâh 'alime mâ' ve ''alime mâ fî' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'fi's-semâvâti' / 'fi'l-ardi' — ayetler arası: yok.",
 "◈K — K1 's-semâvâti' (19. kelime), 'l-ardi' (22. kelime).",
 "◈B — B1 'n-nâsi' (7. kelime); B2 —; B3 —; B4 —.",
 "◈D — D1 PERF + lafız + belirli + belirli + belirli + nekre + 'li' + belirli + 've' + belirli + belirli + 've' + belirli + 've' + belirli + 'zâlike' + 'li' + IMPF + 'enne' + lafız + IMPF + 'mâ' + 'fî' + belirli + 've' + 'mâ' + 'fî' + belirli + 've' + 'enne' + lafız + 'bi' + izafet + nekre + nekre; "
 "D2 haber; D3 أله ×3, حرم ×2, علم ×3; D4 2MP 2 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T97 + "; aktör Kâbe (ölçüm); A2 Kâbe'nin, haram ayın, kurbanlığın ve gerdanlıkların insanlar için ayakta duruş kılınması; Allah'ın gökte ve yerde olanı ve her şeyi bilmesi; A3 —; "
 "A4 " + BOLUM + "; edim geçişi emir → haber (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası).",
)

D[98] = ("◇ 'i'lemû enne'llâhe şedîdu'l-'iqâbi ve enne'llâhe ğafûrun rahîm' — "
 "IMPV 2MP I. bab + 'enne' + lafız + 'şedîd' + belirli ''iqâb' + 've' + 'enne' + lafız + nekre 'ğafûr' + nekre 'rahîm' "
 "(ölçüm edim emir, kip IMPV 1; 2MP 2; bab I. bab ×1). "
 "Allah lafzı 3. ve 7. sırada (ölçüm allah z=3,92); Rab yok; ölçüm '{{2|esmâ غَفُور 8\\. sırada, SON konum, MÜHÜR \\| رَحِيم 9\\. sırada, SON konum, MÜHÜR}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET (ÇİFT) ton cemâl' (uyuşuyor) — esma_el kaydı 'ilahi' — 've enne'llâhe ğafûrun rahîm', kural ''inne/enne' haberi → ilahi' (lafzın haberi) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=9 (n z=-0,36); ölçüm '{{2|fâsıla رحيم → م, N sınıfı}}' — satır aynen; ölçüm '{{2|simetri \\[3, 2, 6, 1\\]}}' — satır aynen; "
 "ölçüm '{{2|harf 40 → harf3 37, isaret 3}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen. "
 "Ölçüm IMPV 1: ''lemû' (1. kelime); 've enne' (6.)'daki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhe' 3. / 7. kelime) (okuma). "
 + T98 + " (okuma). "
 + cumle(say('say 5:98 1-5', "i'lemû enne'llâhe şedîdu'l-'iqâb", True), say('say 5:98 1-3', "i'lemû enne'llâh"), say('dizi 5 98 1 3', "'alime enne allâh"), say('say 5:98 2-5', "enne'llâhe şedîdu'l-'iqâb"), say('dizi 5 98 2 5', "enne allâh şedîd 'iqâb"), say('say 5:98 4-5', "şedîdu'l-'iqâb")) + ' '
 + cumle(say('say 5:98 6-9 --on', "ve enne'llâhe ğafûrun rahîm", True), say('dizi 5 98 6 9', "enne allâh ğafûr rahîm"), say('say 5:98 7-9', "llâhe ğafûrun rahîm"), say('dizi 5 98 7 9', "allâh ğafûr rahîm"), say('say 5:98 8-9', "ğafûrun rahîm")) + ' '
 "Ölçüm xref 2:196 (emsal olarak basıldı) ve henüz okunmamış 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'enne allâh ğafûr rahîm', 'enne allâh şedîd 'iqâb', 'allâh ğafûr rahîm' ve ''alime enne allâh' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'şedîdu'l-'iqâbi' / 'ğafûrun rahîm' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'enne' + lafız + izafet + belirli + 've' + 'enne' + lafız + nekre + nekre; "
 "D2 emir, IMPV (''lemû' 1. kelime); D3 أله ×2; 2:196 eşi; D4 2MP 2, sahset ['2'], iltifât 0.",
 "◈A — A1 " + T98 + "; aktör yok (ölçüm); A2 Allah'ın cezasının çetinliğini ve bağışlayıcılığını bilme emri; A3 —; "
 "A4 " + BOLUM + "; edim geçişi haber → emir (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası).",
)

D[99] = ("◇ 'mâ 'ale'r-rasûli ille'l-belâğu ve'llâhu ya'lemu mâ tubdûne ve mâ tektumûn' — "
 "'mâ' + ''alâ' + belirli 'rasûl' + 'illâ' + belirli 'belâğ' + 've' + lafız + IMPF 3MS I. bab + 'mâ' + IMPF 2MP IV. bab + 've' + 'mâ' + IMPF 2MP I. bab "
 "(ölçüm edim haber, kip NEG 1 · RES 1; 2MP 4 · 3MS 1; bab I. bab ×2 · IV. bab ×1). "
 "Allah lafzı 6. sırada (ölçüm allah z=1,29); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=11 (n z=-0,15); ölçüm '{{3|fâsıla تكتمون → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|simetri \\[3, 2, 8, 1\\]}}' — satır aynen; "
 "ölçüm '{{3|harf 45 → harf3 44, isaret 1}}' — satır aynen; ölçüm '{{3|dış düğüm 1}}' — satır aynen. "
 "Ölçüm NEG 1: 'mâ' (1. kelime); RES 1: 'illâ' (4. kelime); 've'llâhu' (6.)'daki 've' REM, 've mâ' (10.)'daki 've' CONJ (okuma). "
 + T99 + " (okuma). "
 + cumle(say('say 5:99 1-5', "mâ 'ale'r-rasûli ille'l-belâğ", True), say('say 5:99 2-5', "'ale'r-rasûli ille'l-belâğ"), say('say 5:99 2-3', "'ale'r-rasûl"), say('say 5:99 4-5', "ille'l-belâğ")) + ' '
 + cumle(say('say 5:99 6-11 --on', "ve'llâhu ya'lemu mâ tubdûne ve mâ tektumûn", True), say('say 5:99 6-8 --on', "ve'llâhu ya'lemu mâ"), say('dizi 5 99 6 8', "allâh 'alime mâ"), say('say 5:99 7-11', "ya'lemu mâ tubdûne ve mâ tektumûn"),
         say('say 5:99 8-11', "mâ tubdûne ve mâ tektumûn"), say('say 5:99 9-11', "tubdûne ve mâ tektumûn")) + ' '
 "Ölçüm xref 24:29 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı: 'allâh 'alime mâ' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'tubdûne' / 'tektumûn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'mâ' + ''alâ' + belirli + 'illâ' + belirli + 've' + lafız + IMPF + 'mâ' + IMPF + 've' + 'mâ' + IMPF; "
 "D2 haber, NEG ('mâ' 1. kelime), RES ('illâ' 4. kelime); D3 24:29 eşi; D4 2MP 4 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T99 + "; aktör yok (ölçüm); A2 elçinin görevinin yalnızca tebliğ oluşu; Allah'ın açığa vurulanı ve gizleneni bilmesi; A3 —; "
 "A4 " + BOLUM + "; edim geçişi emir → haber (ayetler arası).",
)

D[100] = ("◇ 'qul lâ yestevi'l-xabîsu ve't-tayyibu ve lev a'cebeke kesratu'l-xabîsi fe'ttequ'llâhe yâ uli'l-elbâbi le'allekum tuflihûn' — "
 "IMPV 2MS I. bab + 'lâ' + IMPF 3MS VIII. bab + belirli 'xabîs' + 've' + belirli 'tayyib' + 've' + 'lev' + PERF 3MS IV. bab + 2MS + 'kesra' + belirli 'xabîs' + 'fe' + IMPV 2MP VIII. bab + lafız + 'yâ' + çoğul 'zû' + belirli çoğul 'elbâb' + 'le'alle' + 2MP + IMPF 2MP IV. bab "
 "(ölçüm edim emir, nida, şart, kip COND 1 · IMPV 2 · NEG 1 · VOC 1; 2MP 5 · 2MS 2 · 3MS 2; bab I. bab ×1 · IV. bab ×2 · VIII. bab ×2). "
 "Allah lafzı 11. sırada (ölçüm allah z=0,81); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=15 (n z=0,27); ölçüm '{{4|fâsıla تفلحون → ن, N sınıfı}}' — satır aynen; ölçüm '{{4|sayı işareti كَثْرَة}}' — satır aynen; "
 "ölçüm '{{4|harf 74 → harf3 71, isaret 3}}' — satır aynen; ölçüm '{{4|dış düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 2: 'qul' (1. kelime), 'ttequ' (10. kelime); NEG 1: 'lâ' (2. kelime); COND 1: 'lev' (6. kelime); VOC 1: 'yâ' (12. kelime); 've't-tayyibu' (5.)'daki 've' CONJ, 've lev' (6.)'daki 've' CIRC, 'fe'ttequ' (10.)'daki 'fe' REM (okuma). "
 "Kök ikilemesi (ölçüm) خبث ×2 ('l-xabîsu' 4. / 'l-xabîsi' 9. kelime) (okuma). "
 + T100 + " (okuma). "
 + cumle(say('say 5:100 1-5', "qul lâ yestevi'l-xabîsu ve't-tayyib", True), say('say 5:100 2-5', "lâ yestevi'l-xabîsu ve't-tayyib"), say('say 5:100 3-5', "yestevi'l-xabîsu ve't-tayyib"), say('say 5:100 4-5', "l-xabîsu ve't-tayyib")) + ' '
 + cumle(say('say 5:100 6-9 --on', "ve lev a'cebeke kesratu'l-xabîs", True), say('say 5:100 7-9', "a'cebeke kesratu'l-xabîs"), say('say 5:100 8-9', "kesratu'l-xabîs")) + ' '
 + cumle(say('say 5:100 10-15 --on', "fe'ttequ'llâhe yâ uli'l-elbâbi le'allekum tuflihûn", True), say('say 5:100 10-11 --on', "fe'ttequ'llâh"), say('say 5:100 10-13 --on', "fe'ttequ'llâhe yâ uli'l-elbâb"), say('say 5:100 12-13', "yâ uli'l-elbâb"), say('say 5:100 14-15', "le'allekum tuflihûn")) + ' '
 "Ölçüm xref 65:10 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'l-xabîsu' / 't-tayyibu' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'lâ' + IMPF + belirli + 've' + belirli + 've' + 'lev' + PERF + izafet + belirli + 'fe' + IMPV + lafız + 'yâ' + izafet + belirli + 'le'alle' + IMPF; "
 "D2 emir, nida, şart, IMPV ('qul' 1., 'ttequ' 10. kelime), NEG ('lâ' 2. kelime), COND ('lev' 6. kelime), VOC ('yâ' 12. kelime); D3 خبث ×2; 65:10 eşi; D4 2MP 5 · 2MS 2 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T100 + "; aktör yok (ölçüm); A2 kötü ile temizin bir olmaması; akıl sahiplerine sakınma emri; A3 'lâ yestevi'l-xabîsu ve't-tayyib' ile açılan söz (2-15. kelime); "
 "A4 " + BOLUM + "; bölüm kapanışı; söz açılır (2. kelime); edim geçişi haber → emir, nida, şart (ayetler arası); şart → cevap (ayet içi; COND 'lev' 6. kelime: 've lev a'cebeke kesratu'l-xabîs' — cevap mahzuf (okuma)).",
)

out = ['# ── blok 5:97-100 (2026-11-17) ──', 'MEAL30 = {']
for n in range(97, 101):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M30 = {']
for n in range(97, 101):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL30); M.update(M30)']
open('/home/claude/yamalar/metin_5_97_100.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
