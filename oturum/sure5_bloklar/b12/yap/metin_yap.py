# blok 12 (5:33-36) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b12/say2.txt'
os.environ['OLC'] = '/home/claude/b12/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Bozgunculuğun cezası; vesile; hırsızlık ve tövbe' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 33: "Allah'a ve elçisine savaş açan ve yeryüzünde bozgunculuk için koşanların cezası ancak öldürülmeleri ya da asılmaları ya da ellerinin ve ayaklarının çaprazlama kesilmesi ya da yerden sürülmeleridir. Bu, onlar için dünyada bir rezilliktir; âhirette de onlar için büyük bir azap vardır.",
 34: "Ancak siz onlara güç yetirmeden önce tövbe edenler başka. Bilin ki Allah bağışlayandır, merhamet edendir.",
 35: "Ey iman edenler! Allah'tan sakının, O'na vesile arayın ve O'nun yolunda cihad edin; umulur ki kurtuluşa erersiniz.",
 36: "Şüphesiz inkâr edenlerin, yeryüzünde olanların hepsi ve onunla birlikte bir misli daha olsa da kıyamet gününün azabından kurtulmak için onu fidye verseler, onlardan kabul edilmez. Onlar için acıklı bir azap vardır.",
}

T33 = ("'cezâ'u' (mübteda; 2. kelime); 'llezîne' (ism-i mevsûl; 3. kelime); 'yuhâribûna' faili 3MP (adsız; gönderge 'llezîne'); Allah (lafız; 'yuhâribûna' mef'ûlü, 5. kelime); 'rasûlehû' (elçi; 6. kelime) ve iyelik 3MS (adsız; gönderge lafız); 'yes'avne' faili 3MP (adsız); "
       "'yuqattelû', 'yusallebû' ve 'yunfev' faili (adsız; edilgen — nâib fâil 3MP); 'tuqatta'a' faili (adsız; edilgen — nâib fâil 'eydîhim', 3FS); 'eydîhim' ve 'erculuhum' iyelik 3MP (adsız); 'zâlike' (işaret; 25. kelime); 'lehum' 3MP (adsız; 26. ve 30. kelime); 'xizyun' (nekre; 27. kelime); ''azâbun 'azîm' (nekre; 33-34. kelime)")
T34 = ("'llezîne' (ism-i mevsûl; 2. kelime); 'tâbû' faili 3MP (adsız); muhatap 2MP (adsız; 'taqdirû', ''lemû'); ''aleyhim' 3MP (adsız; gönderge 'llezîne'); Allah (lafız; enne ismi, 11. kelime); 'ğafûrun rahîm' (haber; nekre, 12-13. kelime)")
T35 = ("muhatap 2MP (adsız; 'ttequ', 'bteğû', 'câhidû', 'le'allekum', 'tuflihûn'); 'llezîne âmenu' (münâdâ; 2-3. kelime; 'âmenu' faili 3MP — adsız); Allah (lafız; 5. kelime); 'ileyhi' ve 'sebîlihî' 3MS (adsız; gönderge lafız); 'l-vesîlete' (mef'ûl; 8. kelime)")
T36 = ("'llezîne keferû' ('inne' ismi; 2-3. kelime; 'keferû' faili 3MP — adsız); 'lehum', 'minhum' ve 'lehum' 3MP (adsız; 6., 21. ve 22. kelime); 'mâ fi'l-ard' ('enne' ismi; 7-9. kelime); 'mislehû' ve 'me'ahû' 3MS (adsız; gönderge 'mâ'); 'yeftedû' faili 3MP (adsız); 'bihî' 3MS (adsız; 14. kelime); "
       "'tuqubbile' faili (adsız; edilgen — nâib fâil 3MS, fidye takdiri, 20. kelime); ''azâbun elîm' (nekre; 23-24. kelime)")

D = {}
D[33] = ("◇ 'innemâ cezâ'u'llezîne yuhâribûna'llâhe ve rasûlehû ve yes'avne fi'l-ardi fesâden en yuqattelû ev yusallebû ev tuqatta'a eydîhim ve erculuhum min xilâfin ev yunfev mine'l-ard zâlike lehum xizyun fi'd-dunyâ ve lehum fi'l-âxirati 'azâbun 'azîm' — "
 "'inne' + 'mâ' + 'cezâ'' + 'ellezî' + IMPF 3MP III. bab + lafız + 've' + 'rasûl' + 3MS + 've' + IMPF 3MP I. bab + 'fî' + belirli 'ard' + nekre 'fesâd' + 'en' + IMPF 3MP II. bab (edilgen) + 'ev' + IMPF 3MP II. bab (edilgen) + 'ev' + IMPF 3FS II. bab (edilgen) + çoğul 'yed' + 3MP + 've' + çoğul 'ricl' + 3MP + 'min' + nekre 'xilâf' + "
 "'ev' + IMPF 3MP I. bab (edilgen) + 'min' + belirli 'ard' + 'zâ' + 'li' + 3MP + nekre 'xizy' + 'fî' + belirli 'dunyâ' + 've' + 'li' + 3MP + 'fî' + belirli 'âxir' + nekre ''azâb' + nekre ''azîm' "
 "(ölçüm edim haber, kip yok; 3FS 1 · 3MP 14 · 3MS 1; bab I. bab ×2 · II. bab ×3 · III. bab ×1). "
 "Allah lafzı 5. sırada (ölçüm allah z=0,06); Rab yok; ölçüm '{{1|esmâ آخِر 32\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' (uyuşmuyor) — 'fi'l-âxirati 'azâbun 'azîm', kural 'esmâ adı esmâ dışı göndergeyle → degil' (âhiret yurdu) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=34 (n z=2,29); ölçüm '{{1|EDİLGEN 4/6 fiil, pas z=3,48}}' — satır aynen; ölçüm '{{1|HAPAKS: نفي}}' — satır aynen (kök bu blokta tabloya eklendi); ölçüm '{{1|hapaks z=3,28}}' — satır aynen; "
 "ölçüm '{{1|fâsıla عظيم → م, N sınıfı}}' — satır aynen; ölçüm '{{1|simetri \\[6, 8, 23, 2\\]}}' — satır aynen; ölçüm '{{1|harf 148 → harf3 140, isaret 8}}' — satır aynen; ölçüm '{{1|dış düğüm 3}}' — satır aynen. "
 "Ölçüm EDİLGEN — 'yuqattelû' (12. kelime), 'yusallebû' (14. kelime), 'tuqatta'a' (16. kelime), 'yunfev' (22. kelime) morph PASS; ceza sayımı edilgen fiillerle, failsiz (okuma); 'innemâ' (1. kelime) morph ACC + PREV — sınırlama (okuma). "
 "Kök ikilemesi (ölçüm) أرض ×2: 'l-ardi' (9. kelime) / 'l-ard' (24. kelime) (okuma). "
 "'ve rasûlehû' (6.), 've yes'avne' (7.) ve 've erculuhum' (18.)'daki 've' morph CONJ; 've lehum' (30.)'daki 've' REM; 'ev' (13., 15. ve 21.) CONJ (okuma). "
 + T33 + " (okuma). "
 + cumle(say('say 5:33 1-3 --on', "innemâ cezâ'u'llezîne", True), say('say 5:33 2-3', "cezâ'u'llezîne"), say('say 5:33 3-6', "llezîne yuhâribûna'llâhe ve rasûleh"), say('say 5:33 4-6', "yuhâribûna'llâhe ve rasûleh"), say('dizi 5 33 4 6', "hârebe allâh rasûl")) + ' '
 + cumle(say('say 5:33 7-10', "ve yes'avne fi'l-ardi fesâden", True), say('say 5:33 8-10', "fi'l-ardi fesâden"), say('say 5:33 9-10', "l-ardi fesâden"), say('say 5:33 11-12 --on', "en yuqattelû"), say('lem 5:33:12', "quttilu"), say('lem 5:33:14', "yusallebu"), say('lem 5:33:16', "qatta'a"), say('lem 5:33:22', "yunfe")) + ' '
 + cumle(say('say 5:33 16-20', "tuqatta'a eydîhim ve erculuhum min xilâf", True), say('say 5:33 17-20', "eydîhim ve erculuhum min xilâf"), say('say 5:33 19-20', "min xilâf"), say('say 5:33 22-24', "yunfev mine'l-ard")) + ' '
 + cumle(say('say 5:33 25-27', "zâlike lehum xizyun", True), say('say 5:33 26-29', "lehum xizyun fi'd-dunyâ"), say('say 5:33 28-29', "fi'd-dunyâ"), say('dizi 5 33 28 33', "fî dunyâ fî âxir 'azâb"), say('say 5:33 30-34', "ve lehum fi'l-âxirati 'azâbun 'azîm"), say('say 5:33 31-34', "fi'l-âxirati 'azâbun 'azîm"), say('say 5:33 32-34', "l-âxirati 'azâbun 'azîm"), say('say 5:33 33-34', "'azâbun 'azîm"), say('dizi 5 33 31 34', "fî âxir 'azâb 'azîm")) + ' '
 "Ölçüm xref 9:107 ve 59:3 (emsal olarak basıldı) ve okunmuş başka bir ayet. "
 "Ölçüm nakarat3 kalıpları: 've yes'avne fi'l-ardi fesâden' süzgeç GEÇER; 'fi'l-âxirati 'azâbun 'azîm' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'xizyun fi'd-dunyâ' / 'fi'l-âxirati 'azâbun 'azîm' — ayetler arası: 5:33 / 5:34 ('innemâ cezâ'u'llezîne yuhâribûna'llâhe' / 'illa'llezîne tâbû').",
 "◈K — K1 'l-ardi' (9. kelime), 'l-ard' (24. kelime).",
 "◈B — B1 —; B2 —; B3 'eydîhim' (17. kelime); B4 —.",
 "◈D — D1 'inne' + 'mâ' + izafet + 'ellezî' + IMPF + lafız + 've' + izafet + 've' + IMPF + 'fî' + belirli + nekre + 'en' + IMPF + 'ev' + IMPF + 'ev' + IMPF + izafet + 've' + izafet + 'min' + nekre + 'ev' + IMPF + 'min' + belirli + 'zâ' + 'li' + nekre + 'fî' + belirli + 've' + 'li' + 'fî' + belirli + nekre + nekre; "
 "D2 haber, kip yok, sınırlama ('innemâ' 1. kelime); D3 أرض ×2; 59:3 ve 9:107 eşleri; D4 3FS 1 · 3MP 14 · 3MS 1, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T33 + "; aktör yok (ölçüm); A2 savaş açma; bozgunculuk; öldürülme; asılma; el ve ayak kesilmesi; sürgün; dünya rezilliği; âhiret azabı; A3 —; A4 " + BOLUM + "; bölüm açılışı; edim geçişi şart → haber (ayetler arası); şahıs geçişi yok.",
)

D[34] = ("◇ 'illa'llezîne tâbû min qabli en taqdirû 'aleyhim fa'lemû enna'llâhe ğafûrun rahîm' — "
 "'illâ' + 'ellezî' + PERF 3MP I. bab + 'min' + 'qabl' + 'en' + IMPF 2MP I. bab + ''alâ' + 3MP + 'fe' + IMPV 2MP I. bab + 'enne' + lafız + nekre 'ğafûr' + nekre 'rahîm' "
 "(ölçüm edim emir, kip IMPV 1; 2MP 4 · 3MP 3; bab I. bab ×3). "
 "Allah lafzı 11. sırada (ölçüm allah z=1,01); Rab yok; ölçüm '{{2|esmâ غَفُور 12\\. sırada, SON konum, MÜHÜR \\| رَحِيم 13\\. sırada, SON konum, MÜHÜR}}' — satır aynen; esma_kayit çıktısı 'mühür EVET (ÇİFT) ton cemâl' (uyuşuyor) — 'enna'llâhe ğafûrun rahîm', kural ''inne/enne' haberi → ilahi' (lafzın haberi) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=13 (n z=0,06); ölçüm '{{2|biçim ISTISNA}}' — satır aynen; ölçüm '{{2|fâsıla رحيم → م, N sınıfı}}' — satır aynen; ölçüm '{{2|simetri \\[3, 2, 6, 1\\]}}' — satır aynen; ölçüm '{{2|harf 58 → harf3 52, isaret 6}}' — satır aynen; ölçüm '{{2|dış düğüm 1}}' — satır aynen. "
 "Ölçüm biçim ISTISNA — 'illâ' (1. kelime, morph EXP): 5:33'teki cezadan istisna (okuma); 'fa'lemû' (9. kelime)'daki 'fe' morph REM (okuma). "
 + T34 + " (okuma). "
 + cumle(say('say 5:34 1-3', "illa'llezîne tâbû", True), say('say 5:34 4-7 --on', "min qabli en taqdirû"), say('say 5:34 4-6', "min qabli en"), say('say 5:34 7-8', "taqdirû 'aleyhim"), say('dizi 5 34 4 6', "min qabl en")) + ' '
 + cumle(say('say 5:34 9-11', "fa'lemû enna'llâh", True), say('say 5:34 9-13 --on', "fa'lemû enna'llâhe ğafûrun rahîm"), say('say 5:34 10-13', "enna'llâhe ğafûrun rahîm"), say('say 5:34 11-13', "llâhe ğafûrun rahîm"), say('say 5:34 12-13', "ğafûrun rahîm"), say('dizi 5 34 9 11', "'alime enne allâh"), say('dizi 5 34 10 13', "enne allâh ğafûr rahîm"), say('dizi 5 34 11 13', "allâh ğafûr rahîm")) + ' '
 "Ölçüm xref okunmuş bir ayet. "
 "Ölçüm nakarat3 kalıpları: 'enna'llâhe ğafûrun rahîm' süzgeç GEÇER; 'llâhe ğafûrun rahîm' süzgeç GEÇER; 'fa'lemû enna'llâh' süzgeç GEÇER; 'min qabli en' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: 5:33 / 5:34 ('innemâ cezâ'u'llezîne yuhâribûna'llâhe' / 'illa'llezîne tâbû').",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'illâ' + 'ellezî' + PERF + 'min' + 'qabl' + 'en' + IMPF + ''alâ' + 'fe' + IMPV + 'enne' + lafız + nekre + nekre; "
 "D2 emir, IMPV ('fa'lemû' 9. kelime), istisna ('illâ' 1. kelime); D3 —; eş yok; D4 2MP 4 · 3MP 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T34 + "; aktör yok (ölçüm); A2 tövbe; güç yetirme; bağışlama; merhamet; A3 —; A4 " + BOLUM + "; edim geçişi haber → emir (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası).",
)

D[35] = ("◇ 'yâ eyyuhe'llezîne âmenu'ttequ'llâhe ve'bteğû ileyhi'l-vesîlete ve câhidû fî sebîlihî le'allekum tuflihûn' — "
 "'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF 3MP IV. bab + IMPV 2MP VIII. bab + lafız + 've' + IMPV 2MP VIII. bab + 'ilâ' + 3MS + belirli 'vesîle' + 've' + IMPV 2MP III. bab + 'fî' + 'sebîl' + 3MS + 'le'alle' + 2MP + IMPF 2MP IV. bab "
 "(ölçüm edim emir, nida, kip IMPV 3 · VOC 1; 2MP 9 · 3MP 2 · 3MS 2; bab III. bab ×1 · IV. bab ×2 · VIII. bab ×2). "
 "Allah lafzı 5. sırada (ölçüm allah z=1,01); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=13 (n z=0,06); ölçüm '{{3|biçim DIKKAT}}' — satır aynen; ölçüm '{{3|fâsıla تفلحون → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|harf 72 → harf3 67, isaret 5}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm biçim DIKKAT — 'yâ eyyuhâ' nidâsı (1. kelime, morph VOC + ATT); 'le'allekum' (12. kelime) morph ACC — ümit (okuma). "
 "'ve'bteğû' (6.) ve 've câhidû' (9.)'daki 've' morph CONJ (okuma). "
 + T35 + " (okuma). "
 + cumle(say('say 5:35 1-3', "yâ eyyuhe'llezîne âmenû", True), say('say 5:35 1-5', "yâ eyyuhe'llezîne âmenu'ttequ'llâh"), say('say 5:35 4-5', "ttequ'llâh")) + ' '
 + cumle(say('say 5:35 6-8 --on', "ve'bteğû ileyhi'l-vesîle", True), say('say 5:35 7-8', "ileyhi'l-vesîle"), say('lem 5:35:8', "vesîle"), say('say 5:35 9-11 --on', "ve câhidû fî sebîlih"), say('say 5:35 9-11', "ve câhidû fî sebîlih"), say('dizi 5 35 9 11', "câhede fî sebîl"), say('say 5:35 10-11', "fî sebîlih"), say('say 5:35 12-13', "le'allekum tuflihûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: 'yâ eyyuhe'llezîne âmenu' süzgeç GEÇER; 'câhidû fî sebîlih' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: 5:35 / 5:36 ('le'allekum tuflihûn' / 've lehum 'azâbun elîm').",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF + IMPV + lafız + 've' + IMPV + 'ilâ' + belirli + 've' + IMPV + 'fî' + izafet + 'le'alle' + IMPF; "
 "D2 emir, nida, IMPV ('ttequ' 4., 'bteğû' 6., 'câhidû' 9. kelime), VOC ('yâ' 1. kelime); D3 —; eş yok; D4 2MP 9 · 3MP 2 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T35 + "; aktör yok (ölçüm); A2 iman; takvâ; vesile arama; cihad; kurtuluş; A3 —; A4 " + BOLUM + "; hitap açılır ('yâ eyyuhe'llezîne âmenu', 1-3. kelime); edim geçişi emir → emir, nida (ayetler arası); şahıs geçişi yok; hitap kapanır (13. kelime, ayet sonu).",
)

D[36] = ("◇ 'inne'llezîne keferû lev enne lehum mâ fi'l-ardi cemî'an ve mislehû me'ahû li-yeftedû bihî min 'azâbi yevmi'l-qiyâmeti mâ tuqubbile minhum ve lehum 'azâbun elîm' — "
 "'inne' + 'ellezî' + PERF 3MP I. bab + 'lev' + 'enne' + 'li' + 3MP + 'mâ' + 'fî' + belirli 'ard' + nekre 'cemî'' + 've' + 'misl' + 3MS + 'ma'a' + 3MS + 'li' + IMPF 3MP VIII. bab + 'bi' + 3MS + 'min' + ''azâb' + 'yevm' + belirli 'qiyâme' + 'mâ' + PERF 3MS V. bab (edilgen) + 'min' + 3MP + 've' + 'li' + 3MP + nekre ''azâb' + nekre 'elîm' "
 "(ölçüm edim şart, kip COND 1 · NEG 1; 3MP 7 · 3MS 4; bab I. bab ×1 · V. bab ×1 · VIII. bab ×1). "
 "Ölçüm '{{4|lafız YOK · Rab YOK}}' — satır aynen; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=24 (n z=1,23); ölçüm '{{4|EDİLGEN 1/3 fiil, pas z=1,57}}' — satır aynen; ölçüm '{{4|fâsıla أليم → م, N sınıfı}}' — satır aynen; ölçüm '{{4|simetri \\[6, 12, 19, 2\\]}}' — satır aynen; ölçüm '{{4|harf 95 → harf3 87, isaret 8}}' — satır aynen; ölçüm '{{4|dış düğüm 6}}' — satır aynen. "
 "Ölçüm COND 1: 'lev' (4. kelime); NEG 1: 'mâ' (19. kelime) (okuma); ölçüm EDİLGEN — 'tuqubbile' (20. kelime) morph PASS (okuma); 've mislehû' (11.)'daki 've' morph COM — birliktelik; 'li-yeftedû' (13.)'daki 'li' PRP — amaç; 've lehum' (22.)'daki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) عذب ×2: ''azâbi' (16. kelime) / ''azâbun' (23. kelime) (okuma). "
 + T36 + " (okuma). "
 + cumle(say('say 5:36 1-3', "inne'llezîne keferû", True), say('say 5:36 4-6 --on', "lev enne lehum"), say('say 5:36 6-10', "lehum mâ fi'l-ardi cemî'an"), say('say 5:36 7-9', "mâ fi'l-ard"), say('say 5:36 8-10', "fi'l-ardi cemî'an"), say('say 5:36 9-10', "l-ardi cemî'an"), say('dizi 5 36 7 9', "mâ fî ard"), say('say 5:36 4-12', "lev enne lehum mâ fi'l-ardi cemî'an ve mislehû me'ah")) + ' '
 + cumle(say('say 5:36 11-12', "ve mislehû me'ah", True), say('say 5:36 13-14 --on', "li-yeftedû bih"), say('lem 5:36:13', "iftedâ"), say('say 5:36 15-18', "min 'azâbi yevmi'l-qiyâme"), say('say 5:36 16-18', "'azâbi yevmi'l-qiyâme"), say('say 5:36 17-18', "yevmi'l-qiyâme")) + ' '
 + cumle(say('say 5:36 19-21 --on', "mâ tuqubbile minhum", True), say('say 5:36 22-24', "ve lehum 'azâbun elîm"), say('say 5:36 23-24', "'azâbun elîm")) + ' '
 "Ölçüm xref 13:18, 14:8 ve 70:11 (basılmış) ve okunmuş başka ayetler. "
 "Ölçüm nakarat3 kalıpları: 'fi'l-ardi cemî'an' süzgeç GEÇMEZ; 'mâ fi'l-ard' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: 5:35 / 5:36 ('le'allekum tuflihûn' / 've lehum 'azâbun elîm').",
 "◈K — K1 'l-ardi' (9. kelime); K2 'yevmi' (17. kelime).",
 "◈B — —",
 "◈D — D1 'inne' + 'ellezî' + PERF + 'lev' + 'enne' + 'li' + 'mâ' + 'fî' + belirli + nekre + 've' + izafet + izafet + 'li' + IMPF + 'bi' + 'min' + izafet + izafet + belirli + 'mâ' + PERF + 'min' + 've' + 'li' + nekre + nekre; "
 "D2 şart, COND ('lev' 4. kelime), NEG ('mâ' 19. kelime); D3 عذب ×2; 13:18 ve 70:11 eşleri; D4 3MP 7 · 3MS 4, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T36 + "; aktör yok (ölçüm); A2 inkâr; yeryüzündekilerin hepsi; fidye; kıyamet günü azabı; kabul edilmeme; acıklı azap; A3 —; "
 "A4 " + BOLUM + "; edim geçişi emir, nida → şart (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası); şart → cevap (ayet içi; COND 'lev' 4. kelime: 'lev enne lehum mâ fi'l-ardi cemî'an' / 'mâ tuqubbile minhum' (19. kelime)).",
)

out = ['# ── blok 5:33-36 (2026-11-15) ──', 'MEAL12 = {']
for n in range(33, 37):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M12 = {']
for n in range(33, 37):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL12); M.update(M12)']
open('/home/claude/yamalar/metin_5_33_36.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
