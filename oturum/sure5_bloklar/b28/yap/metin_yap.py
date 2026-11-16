# blok 28 (5:90-93) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b28/say2.txt'
os.environ['OLC'] = '/home/claude/b28/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Helalleri haram kılmama; yemin keffareti; içki ve kumar' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 90: "Ey iman edenler! İçki, kumar, dikili taşlar ve fal okları ancak şeytanın işinden bir pisliktir; ondan kaçının; umulur ki kurtuluşa erersiniz.",
 91: "Şeytan ancak içki ve kumar yoluyla aranıza düşmanlık ve öfke düşürmek ve sizi Allah'ı anmaktan ve namazdan alıkoymak ister. Artık vazgeçiyor musunuz?",
 92: "Allah'a itaat edin, elçiye itaat edin ve sakının. Eğer yüz çevirirseniz, bilin ki elçimize düşen yalnızca açık tebliğdir.",
 93: "İman edip salih ameller işleyenlere, tattıklarından dolayı bir günah yoktur; yeter ki sakınsınlar, iman etsinler ve salih ameller işlesinler, sonra sakınıp iman etsinler, sonra sakınıp iyilik etsinler. Allah iyilik edenleri sever.",
}

T90 = ("hitap 'yâ eyyuhe'llezîne âmenû' (1-3. kelime); 'âmenû' faili 3MP (adsız; 3. kelime); 'ş-şeytâni' (adlı gayb; ''ameli' muzâfun ileyhi; 12. kelime); "
       "muhatap 2MP (adsız; 'fe'ctenibûhu', 'le'allekum', 'tuflihûn' — 13., 14. ve 15. kelime); 'fe'ctenibûhu' mef'ûlü 3MS (adsız; gönderge 'ricsun', 13. kelime)")
T91 = ("'yurîdu' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'ş-şeytânu' ('yurîdu' faili; adlı gayb; 3. kelime); 'yûqi'a' faili 3MS (adsız; gönderge 'ş-şeytânu', 5. kelime); "
       "muhatap 2MP (adsız; 'beynekumu', 'yesuddekum', 'entum' — 6., 12. ve 19. kelime); 'yesuddekum' faili 3MS (adsız; gönderge 'ş-şeytânu', 12. kelime); 'llâhi' (lafız; 'zikri' muzâfun ileyhi; 15. kelime); 'muntehûn' ('entum' haberi; 20. kelime)")
T92 = ("muhatap 2MP (adsız; 'atî'u', 'atî'u', 'hzerû', 'tevelleytum', ''lemû' — 1., 3., 5., 7. ve 8. kelime); 'llâhe' ('atî'u' mef'ûlü; lafız; 2. kelime); 'r-rasûle' ('atî'u' mef'ûlü; 4. kelime); "
       "'rasûlina' iyelik 1P (adsız; konuşan, gönderge Allah; 11. kelime); 'l-belâğu'l-mubîn' ('enne' ismi; 'l-mubîn' sıfat, esmâ adı esmâ dışı göndergeyle; 12-13. kelime)")
T93 = ("'leyse' 3MS (fiil uyumu; 1. kelime — ismi 7. kelime); 'âmenû', ''amilu', 'ta'imû', 'ttaqav' faili 3MP (adsız; 4., 5., 9. ve 12. kelime); 'âmenû', ''amilu' faili 3MP (adsız; 13. ve 14. kelime); "
       "'ttaqav', 'âmenû', 'ttaqav', 'ahsenû' faili 3MP (adsız; 17., 18., 20. ve 21. kelime); 'cunâhun' ('leyse' ismi; 7. kelime); 'llâhu' ('yuhibbu' faili; lafız; 22. kelime); 'yuhibbu' 3MS (adsız; gönderge lafız, 23. kelime); 'l-muhsinîn' ('yuhibbu' mef'ûlü; 24. kelime)")

D = {}
D[90] = ("◇ 'yâ eyyuhe'llezîne âmenû innemâ'l-xamru ve'l-meysiru ve'l-ensâbu ve'l-ezlâmu ricsun min 'ameli'ş-şeytâni fe'ctenibûhu le'allekum tuflihûn' — "
 "'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF 3MP IV. bab + 'inne' + 'mâ' + belirli 'xamr' + 've' + belirli 'meysir' + 've' + belirli çoğul 'nusub' + 've' + belirli 'ezlâm' + nekre 'rics' + 'min' + ''amel' + belirli özel ad 'şeytân' + 'fe' + IMPV 2MP VIII. bab + 3MS + 'le'alle' + 2MP + IMPF 2MP IV. bab "
 "(ölçüm edim emir, nida, kip IMPV 1 · VOC 1; 2MP 5 · 3MP 2 · 3MS 1; bab IV. bab ×2 · VIII. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm aktör '{{1|adlı شَيْطان 12\\. sırada \\(gayb, rol mecrur\\)}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=15 (n z=0,27); ölçüm '{{1|fâsıla تفلحون → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|harf 82 → harf3 80, isaret 2}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm VOC 1: 'yâ' (1. kelime); IMPV 1: 'ctenibûhu' (13. kelime); 've'l-meysiru' (6.), 've'l-ensâbu' (7.) ve 've'l-ezlâmu' (8.)'daki 've' CONJ, 'fe'ctenibûhu' (13.)'daki 'fe' REM (okuma). "
 + T90 + " (okuma). "
 + cumle(say('say 5:90 1-3', "yâ eyyuhe'llezîne âmenû", True), say('dizi 5 90 1 3', "eyy ellezî âmene")) + ' '
 + cumle(say('say 5:90 4-8', "innemâ'l-xamru ve'l-meysiru ve'l-ensâbu ve'l-ezlâm", True), say('say 5:90 5-8', "l-xamru ve'l-meysiru ve'l-ensâbu ve'l-ezlâm"), say('say 5:90 5-6 --on', "l-xamru ve'l-meysir"), say('dizi 5 90 5 6', "xamr meysir"), say('say 5:90 7-8 --on', "ve'l-ensâbu ve'l-ezlâm")) + ' '
 + cumle(say('say 5:90 9-12', "ricsun min 'ameli'ş-şeytân", True), say('say 5:90 10-12', "min 'ameli'ş-şeytân"), say('say 5:90 11-12', "'ameli'ş-şeytân")) + ' '
 + cumle(say('say 5:90 13-15 --on', "fe'ctenibûhu le'allekum tuflihûn", True), say('say 5:90 14-15', "le'allekum tuflihûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'eyy ellezî âmene' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'yâ' + 'ellezî' + PERF + 'inne' + 'mâ' + belirli + 've' + belirli + 've' + belirli + 've' + belirli + nekre + 'min' + izafet + 'fe' + IMPV + 'le'alle' + IMPF; "
 "D2 emir, nida, VOC ('yâ' 1. kelime), IMPV ('ctenibûhu' 13. kelime); D3 —; 2:219 eşi; D4 2MP 5 · 3MP 2 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T90 + "; aktör şeytan (ölçüm); A2 içki, kumar, dikili taş ve fal oklarının pislik sayılması; kaçınma emri; kurtuluş umudu; A3 —; "
 "A4 " + BOLUM + "; hitap açılır ('yâ eyyuhe'llezîne âmenû', 1-3. kelime); edim geçişi emir, şart → emir, nida (ayetler arası).",
)

D[91] = ("◇ 'innemâ yurîdu'ş-şeytânu en yûqi'a beynekumu'l-'adâvete ve'l-bağdâ'e fi'l-xamri ve'l-meysiri ve yesuddekum 'an zikri'llâhi ve 'ani's-salâti fe-hel entum muntehûn' — "
 "'inne' + 'mâ' + IMPF 3MS IV. bab + belirli özel ad 'şeytân' + 'en' + IMPF 3MS IV. bab + 'beyn' + 2MP + belirli ''adâve' + 've' + belirli 'bağdâ'' + 'fî' + belirli 'xamr' + 've' + belirli 'meysir' + 've' + IMPF 3MS I. bab + 2MP + ''an' + masdar 'zikr' + lafız + 've' + ''an' + belirli 'salâ' + 'fe' + 'hel' + 'entum' + çoğul etken ortaç 'muntehî' "
 "(ölçüm edim soru, kip INTG 1; 2MP 3 · 3MS 3; bab I. bab ×1 · IV. bab ×2). "
 "Allah lafzı 15. sırada (ölçüm allah z=0,47); Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm aktör '{{2|adlı شَيْطان 3\\. sırada \\(gayb, rol fail\\)}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=20 (n z=0,81); ölçüm '{{2|fâsıla منتهون → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|harf 91 → harf3 90, isaret 1}}' — satır aynen; ölçüm '{{2|dış düğüm 1}}' — satır aynen; ölçüm '{{2|İÇ düğüm 2}}' — satır aynen. "
 "Ölçüm INTG 1: 'hel' (18. kelime); 've'l-bağdâ'e' (8.), 've'l-meysiri' (11.), 've yesuddekum' (12.) ve 've 'ani's-salâti' (16.)'daki 've' CONJ, 'fe-hel' (18.)'deki 'fe' REM (okuma). "
 + T91 + " (okuma). "
 + cumle(say('say 5:91 1-3', "innemâ yurîdu'ş-şeytân", True), say('say 5:91 2-3', "yurîdu'ş-şeytân"), say('say 5:91 4-8', "en yûqi'a beynekumu'l-'adâvete ve'l-bağdâ'")) + ' '
 + cumle(say('say 5:91 6-8', "beynekumu'l-'adâvete ve'l-bağdâ'", True), say('dizi 5 91 6 8', "beyn 'adâve bağdâ'"), say('say 5:91 7-8', "l-'adâvete ve'l-bağdâ'")) + ' '
 + cumle(say('say 5:91 9-11', "fi'l-xamri ve'l-meysir", True), say('dizi 5 91 10 11', "xamr meysir")) + ' '
 + cumle(say('say 5:91 12-17 --on', "ve yesuddekum 'an zikri'llâhi ve 'ani's-salât", True), say('say 5:91 13-15', "'an zikri'llâh"), say('say 5:91 14-15', "zikri'llâh"), say('say 5:91 16-17 --on', "ve 'ani's-salât")) + ' '
 + cumle(say('say 5:91 18-20 --on', "fe-hel entum muntehûn", True), say('say 5:91 19-20', "entum muntehûn")) + ' '
 "Ölçüm xref 5:14 (emsal olarak basıldı) ve okunmuş 2 ayet. "
 "Ölçüm nakarat3 kalıbı: 'beyn 'adâve bağdâ'' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'inne' + 'mâ' + IMPF + belirli + 'en' + IMPF + izafet + belirli + 've' + belirli + 'fî' + belirli + 've' + belirli + 've' + IMPF + ''an' + izafet + 've' + ''an' + belirli + 'fe' + 'hel' + 'entum' + ortaç; "
 "D2 soru, INTG ('hel' 18. kelime); D3 —; D4 2MP 3 · 3MS 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T91 + "; aktör şeytan (ölçüm); A2 şeytanın düşmanlık ve öfke düşürme isteği; Allah'ı anmaktan ve namazdan alıkoyma; vazgeçme sorusu; A3 —; "
 "A4 " + BOLUM + "; edim geçişi emir, nida → soru (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası).",
)

D[92] = ("◇ 've atî'u'llâhe ve atî'u'r-rasûle ve'hzerû fe-in tevelleytum fe'lemû ennemâ 'alâ rasûlina'l-belâğu'l-mubîn' — "
 "'ve' + IMPV 2MP IV. bab + lafız + 've' + IMPV 2MP IV. bab + belirli 'rasûl' + 've' + IMPV 2MP I. bab + 'fe' + 'in' + PERF 2MP V. bab + 'fe' + IMPV 2MP I. bab + 'enne' + 'mâ' + ''alâ' + 'rasûl' + 1P + belirli 'belâğ' + belirli etken ortaç 'mubîn' "
 "(ölçüm edim emir, şart, kip COND 1 · IMPV 4; 1P 1 · 2MP 10; bab I. bab ×2 · IV. bab ×2 · V. bab ×1). "
 "Allah lafzı 2. sırada (ölçüm allah z=1,01); Rab yok; ölçüm '{{3|esmâ مُبِين 13\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton denge' (uyuşmuyor) — esma_el kaydı 'degil' — 'l-mubîn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (tebliğin sıfatı) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=13 (n z=0,06); ölçüm '{{3|fâsıla ٱلمبين → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|harf 76 → harf3 71, isaret 5}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen; "
 "ölçüm '{{3|esit2 → 64:12 oran 0,8960 kademe BENZER}}' — satır aynen (64:12 emsal olarak basıldı). "
 "Ölçüm COND 1: 'in' (6. kelime); IMPV 4: 'atî'u' (1. ve 3. kelime), 'hzerû' (5. kelime), ''lemû' (8. kelime); 1., 3. ve 5. kelimedeki 've' CONJ, 'fe-in' (6.)'daki 'fe' REM, 'fe'lemû' (8.)'daki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) رسل ×2 ('r-rasûle' 4. / 'rasûlina' 11. kelime), طوع ×2 ('atî'u' 1. / 3. kelime) (okuma). "
 + T92 + " (okuma). "
 + cumle(say('say 5:92 1-4 --on', "ve atî'u'llâhe ve atî'u'r-rasûl", True), say('say 5:92 1-2 --on', "ve atî'u'llâh"), say('say 5:92 3-4 --on', "ve atî'u'r-rasûl")) + ' '
 + cumle(say('say 5:92 6-13 --on', "fe-in tevelleytum fe'lemû ennemâ 'alâ rasûlina'l-belâğu'l-mubîn", True), say('say 5:92 6-9 --on', "fe-in tevelleytum fe'lemû ennemâ"), say('dizi 5 92 6 9', "fe-in tevellâ 'alime enne"), say('say 5:92 9-13', "ennemâ 'alâ rasûlina'l-belâğu'l-mubîn"), say('say 5:92 10-13', "'alâ rasûlina'l-belâğu'l-mubîn"), say('say 5:92 12-13', "l-belâğu'l-mubîn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'fe-in tevellâ 'alime enne' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'atî'u'llâhe' / 'tevelleytum' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + IMPV + lafız + 've' + IMPV + belirli + 've' + IMPV + 'fe' + 'in' + PERF + 'fe' + IMPV + 'enne' + 'mâ' + ''alâ' + izafet + belirli + belirli; "
 "D2 emir, şart, COND ('in' 6. kelime), IMPV ('atî'u' 1. ve 3., 'hzerû' 5., ''lemû' 8. kelime); D3 رسل ×2, طوع ×2; 64:12 eşi; D4 1P 1 · 2MP 10, sahset ['1', '2'], iltifât 0.",
 "◈A — A1 " + T92 + "; aktör yok (ölçüm); A2 Allah'a ve elçiye itaat emri; sakınma emri; yüz çevirme şartı; elçinin görevi açık tebliğ; A3 —; "
 "A4 " + BOLUM + "; edim geçişi soru → emir, şart (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası); şart → cevap (ayet içi; COND 'in' 6. kelime: 'in tevelleytum' / ''lemû' (8. kelime)).",
)

D[93] = ("◇ 'leyse 'ale'llezîne âmenû ve 'amilu's-sâlihâti cunâhun fîmâ ta'imû izâ me'ttaqav ve âmenû ve 'amilu's-sâlihâti summe'ttaqav ve âmenû summe'ttaqav ve ahsenû ve'llâhu yuhibbu'l-muhsinîn' — "
 "PERF 3MS I. bab + ''alâ' + 'ellezî' + PERF 3MP IV. bab + 've' + PERF 3MP I. bab + belirli çoğul etken ortaç 'sâliha' + nekre 'cunâh' + 'fî' + 'mâ' + PERF 3MP I. bab + 'izâ' + 'mâ' + PERF 3MP VIII. bab + 've' + PERF 3MP IV. bab + 've' + PERF 3MP I. bab + belirli çoğul etken ortaç 'sâliha' + "
 "'summe' + PERF 3MP VIII. bab + 've' + PERF 3MP IV. bab + 'summe' + PERF 3MP VIII. bab + 've' + PERF 3MP IV. bab + 've' + lafız + IMPF 3MS IV. bab + belirli çoğul etken ortaç 'muhsin' "
 "(ölçüm edim haber, kip yok; 3MP 20 · 3MS 2; bab I. bab ×4 · IV. bab ×5 · VIII. bab ×3). "
 "Allah lafzı 22. sırada (ölçüm allah z=0,31); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=24 (n z=1,23); ölçüm '{{4|fâsıla ٱلمحسنين → ن, N sınıfı}}' — satır aynen; ölçüm '{{4|simetri \\[6, 2, 11, 2\\]}}' — satır aynen; "
 "ölçüm '{{4|harf 127 → harf3 115, isaret 12}}' — satır aynen; ölçüm '{{4|dış düğüm 3}}' — satır aynen; ölçüm '{{4|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm kip yok; 5., 13., 14., 18. ve 21. kelimedeki 've' CONJ, 'summe' (16. ve 19.) CONJ, 've'llâhu' (22.)'daki 've' REM, 'mâ' (11.) SUP (okuma). "
 "Kök ikilemesi (ölçüm) أمن ×3 ('âmenû' 4., 13., 18. kelime), حسن ×2 ('ahsenû' 21. / 'l-muhsinîn' 24. kelime), صلح ×2 ('s-sâlihâti' 6. / 15. kelime), عمل ×2 (''amilu' 5. / 14. kelime), وقي ×3 ('ttaqav' 12., 17., 20. kelime) (okuma). "
 + T93 + " (okuma). "
 + cumle(say('say 5:93 1-6', "leyse 'ale'llezîne âmenû ve 'amilu's-sâlihât", True), say('say 5:93 2-6', "'ale'llezîne âmenû ve 'amilu's-sâlihât"), say('say 5:93 3-6', "llezîne âmenû ve 'amilu's-sâlihât"), say('dizi 5 93 3 6', "ellezî âmene 'amile sâliha")) + ' '
 + cumle(say('say 5:93 7-9', "cunâhun fîmâ ta'imû", True), say('say 5:93 8-9', "fîmâ ta'imû"), say('say 5:93 10-12', "izâ me'ttaqav")) + ' '
 + cumle(say('say 5:93 13-15 --on', "ve âmenû ve 'amilu's-sâlihât", True), say('say 5:93 16-18', "summe'ttaqav ve âmenû"), say('say 5:93 19-21', "summe'ttaqav ve ahsenû")) + ' '
 + cumle(say('say 5:93 22-24 --on', "ve'llâhu yuhibbu'l-muhsinîn", True), say('dizi 5 93 22 24', "allâh ahbeb muhsin"), say('say 5:93 23-24', "yuhibbu'l-muhsinîn")) + ' '
 "Ölçüm xref 3:134 (emsal olarak basıldı) ve okunmuş 3 ayet. "
 "Ölçüm nakarat3 kalıpları: 'ellezî âmene 'amile sâliha' süzgeç GEÇER, 'allâh ahbeb muhsin' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + ''alâ' + 'ellezî' + PERF + 've' + PERF + belirli + nekre + 'fî' + 'mâ' + PERF + 'izâ' + 'mâ' + PERF + 've' + PERF + 've' + PERF + belirli + 'summe' + PERF + 've' + PERF + 'summe' + PERF + 've' + PERF + 've' + lafız + IMPF + belirli; "
 "D2 haber; D3 أمن ×3, حسن ×2, صلح ×2, عمل ×2, وقي ×3; 3:134 eşi; D4 3MP 20 · 3MS 2, sahset ['3'], iltifât 1.",
 "◈A — A1 " + T93 + "; aktör yok (ölçüm); A2 iman edip salih amel işleyenlere tattıklarından günah olmaması; sakınma, iman ve iyilik şartı; Allah'ın iyilik edenleri sevmesi; A3 —; "
 "A4 " + BOLUM + "; bölüm kapanışı; edim geçişi emir, şart → haber (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası).",
)

out = ['# ── blok 5:90-93 (2026-11-17) ──', 'MEAL28 = {']
for n in range(90, 94):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M28 = {']
for n in range(90, 94):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL28); M.update(M28)']
open('/home/claude/yamalar/metin_5_90_93.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
