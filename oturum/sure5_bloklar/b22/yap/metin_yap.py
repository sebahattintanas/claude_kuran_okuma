# blok 22 (5:67-70) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b22/say2.txt'
os.environ['OLC'] = '/home/claude/b22/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Tebliğ emri; İsrâiloğullarının misakı; Mesih ve teslis' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 67: "Ey elçi! Rabbinden sana indirileni tebliğ et; eğer yapmazsan O'nun mesajını tebliğ etmemiş olursun. Allah seni insanlardan korur. Şüphesiz Allah kâfirler kavmini doğru yola iletmez.",
 68: "De ki: Ey Kitap ehli! Tevrat'ı, İncil'i ve Rabbinizden size indirileni ayakta tutmadıkça hiçbir şey üzerinde değilsiniz. Andolsun, Rabbinden sana indirilen, onlardan çoğunun azgınlığını ve küfrünü artıracaktır. Artık kâfirler kavmi için üzülme.",
 69: "Şüphesiz iman edenler, Yahudi olanlar, Sâbiîler ve Nasârâ'dan kim Allah'a ve âhiret gününe iman eder ve iyi iş yaparsa, onlara korku yoktur ve onlar üzülmeyeceklerdir.",
 70: "Andolsun, İsrâiloğullarından ahit aldık ve onlara elçiler gönderdik. Bir elçi onlara canlarının hoşlanmadığı bir şey getirdikçe, bir kısmını yalanladılar, bir kısmını da öldürüyorlar.",
}

T67 = ("muhatap 2MS (adsız; 'yâ eyyuhe'r-rasûlu' 1-2., 'belliğ' 3., 'ileyke' 6., 'rabbike' 8., 'tef'al' 11., 'bellağte' 13., 'ya'simuke' 16. kelime); 'r-rasûlu' (nida edilen; 2. kelime); 'unzile' naib-i faili 3MS (adsız; edilgen, 5. kelime); Rab ('rabbike', 8. kelime); "
       "'risâletehû' 3MS (adsız; gönderge Rab, 14. kelime); Allah (lafız; 15. ve 20. kelime); 'ya'simu' faili 3MS (adsız; gönderge lafız, 16. kelime); 'yehdi' faili 3MS (adsız; gönderge lafız, 22. kelime); 'n-nâsi' (18. kelime); 'l-qavme'l-kâfirîn' (23-24. kelime)")
T68 = ("muhatap 2MS (adsız; 'qul' 1., 'ileyke' 21., 'rabbike' 23., 'te'se' 27. kelime); 'ehle'l-kitâbi' (nida edilen; 2-3. kelime); muhatap 2MP (adsız; söz içi; 4., 8., 13. ve 15. kelime — 'lestum', 'tuqîmu', 'ileykum', 'rabbikum'); 't-tevrâte' ve 'l-incîle' (adlı kitaplar; 9-10. kelime); "
       "'unzile' naib-i faili 3MS (adsız; edilgen, 12. ve 20. kelime); Rab ('rabbikum' 15., 'rabbike' 23. kelime); 'yezîdenne' faili 3MS (adsız; gönderge 'mâ', 16. kelime); 'kesîran' (nekre; 17. kelime); 'minhum' 3MP (adsız; 18. kelime); 'l-qavmi'l-kâfirîn' (29-30. kelime)")
T69 = ("'ellezîne âmenû' (2-3. kelime); 'âmenû' faili 3MP (adsız; 3. kelime); 've'llezîne hâdû' (4-5. kelime); 'hâdû' faili 3MP (adsız; 5. kelime); 's-sâbi'ûne' ve 'n-nasârâ' (adlı cinsler; 6-7. kelime); 'men' (şart; 8. kelime); 'âmene' faili 3MS (adsız; gönderge 'men', 9. kelime); "
       "Allah (lafız; 10. kelime); ''amile' faili 3MS (adsız; gönderge 'men', 13. kelime); ''aleyhim' 3MP (adsız; 17. kelime); 'hum' 3MP (adsız; 19. kelime); 'yahzenûn' faili 3MP (adsız; 20. kelime)")
T70 = ("konuşan 1P (adsız; 'exaznâ' 2., 'erselnâ' 6. kelime); 'benî isrâ'îl' (adlı kavim; 4-5. kelime); 'ileyhim' 3MP (adsız; 7. kelime); 'rusulen' (nekre; 8. kelime); 'câ'ehum' 3MS (fiil uyumu; 10. kelime — fail 11. kelime); 'câ'ehum' mef'ûlü 3MP (adsız; 10. kelime); 'rasûlun' ('câ'ehum' faili; nekre; 11. kelime); "
       "'tehvâ' 3FS (fiil uyumu; 14. kelime — fail 15. kelime); 'enfus' ('tehvâ' faili; 15. kelime); 'enfusuhum' 3MP (adsız; 15. kelime); 'ferîqan' (nekre; 16. ve 18. kelime); 'kezzebû' faili 3MP (adsız; 17. kelime); 'yaqtulûn' faili 3MP (adsız; 19. kelime)")

D = {}
D[67] = ("◇ 'yâ eyyuhe'r-rasûlu belliğ mâ unzile ileyke min rabbike ve in lem tef'al fe-mâ bellağte risâletehû ve'llâhu ya'simuke mine'n-nâsi inna'llâhe lâ yehdi'l-qavme'l-kâfirîn' — "
 "'yâ' + 'eyy' + 'hâ' + belirli 'rasûl' + IMPV 2MS II. bab + 'mâ' + edilgen PERF 3MS IV. bab + 'ilâ' + 2MS + 'min' + 'rabb' + 2MS + 've' + 'in' + 'lem' + IMPF 2MS I. bab + 'fe' + 'mâ' + PERF 2MS II. bab + 'risâle' + 3MS + 've' + lafız + IMPF 3MS I. bab + 2MS + 'min' + belirli çoğul 'nâs' + 'inne' + lafız + 'lâ' + IMPF 3MS I. bab + belirli 'qavm' + belirli çoğul ortaç 'kâfir' "
 "(ölçüm edim emir, nida, şart, kip COND 1 · IMPV 1 · NEG 3 · VOC 1, biçim DIKKAT; 2MS 7 · 3MS 4; bab I. bab ×3 · II. bab ×2 · IV. bab ×1; EDİLGEN 1/6 fiil). "
 "Allah lafzı 15. ve 20. sırada (ölçüm allah z=1,14); ölçüm '{{1|رَبّ 8\\. sırada \\(rab z=0,57\\)}}' — satır aynen ('rabbike', Rab adı); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=24 (n z=1,23); ölçüm '{{1|fâsıla ٱلكفرين → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|EDİLGEN 1/6 fiil, pas z=0,62}}' — satır aynen ('unzile' 5. kelime); "
 "ölçüm '{{1|simetri \\[3, 4, 7, 1\\]}}' — satır aynen; ölçüm '{{1|harf 97 → harf3 92, isaret 5}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 1: 'belliğ' (3. kelime); VOC 1: 'yâ' (1. kelime); COND 1: 'in' (9. kelime); NEG 3: 'lem' (10.), 'mâ' (12.), 'lâ' (21. kelime); 've in' (9.) ve 've'llâhu' (15.)'daki 've' REM, 'fe-mâ' (12.)'daki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 (lafız 15., 20. kelime), بلغ ×2 ('belliğ' 3. / 'bellağte' 13. kelime), رسل ×2 ('r-rasûlu' 2. / 'risâletehû' 14. kelime) (okuma). "
 + T67 + " (okuma). "
 + cumle(say('say 5:67 1-2', "yâ eyyuhe'r-rasûl", True), say('say 5:67 2-3', "r-rasûlu belliğ"), say('say 5:67 3-8', "belliğ mâ unzile ileyke min rabbik"), say('say 5:67 4-8', "mâ unzile ileyke min rabbik"), say('dizi 5 67 4 8', "mâ enzele ilâ min rabb")) + ' '
 + cumle(say('say 5:67 9-11 --on', "ve in lem tef'al", True), say('say 5:67 10-11', "lem tef'al"), say('say 5:67 12-14 --on', "fe-mâ bellağte risâleteh"), say('say 5:67 13-14', "bellağte risâleteh")) + ' '
 + cumle(say('say 5:67 15-18 --on', "ve'llâhu ya'simuke mine'n-nâs", True), say('say 5:67 16-18', "ya'simuke mine'n-nâs"), say('lem 5:67:16', "ya'simu")) + ' '
 + cumle(say('say 5:67 19-24', "inna'llâhe lâ yehdi'l-qavme'l-kâfirîn", True), say('dizi 5 67 19 23', "inne allâh lâ hedâ qavm"), say('say 5:67 20-24', "llâhe lâ yehdi'l-qavme'l-kâfirîn"), say('dizi 5 67 20 23', "allâh lâ hedâ qavm"),
         say('dizi 5 67 19 21', "inne allâh lâ"), say('say 5:67 22-24', "yehdi'l-qavme'l-kâfirîn")) + ' '
 "Ölçüm xref 33:39 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıpları: 'mâ unzile ileyke min rabbik', 'inna'llâhe lâ yehdi'l-qavm', 'llâhe lâ yehdi'l-qavm' ve 'inna'llâhe lâ' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'belliğ' / 'fe-mâ bellağte' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'n-nâsi' (18. kelime); B2 —; B3 —; B4 —.",
 "◈D — D1 'yâ' + 'eyy' + 'hâ' + belirli + IMPV + 'mâ' + PERF + 'ilâ' + 'min' + izafet + 've' + 'in' + 'lem' + IMPF + 'fe' + 'mâ' + PERF + izafet + 've' + lafız + IMPF + 'min' + belirli + 'inne' + lafız + 'lâ' + IMPF + belirli + belirli; "
 "D2 emir, nida, şart, IMPV ('belliğ' 3. kelime), VOC ('yâ' 1. kelime), COND ('in' 9. kelime), NEG ('lem' 10., 'mâ' 12., 'lâ' 21. kelime), biçim DIKKAT; D3 أله ×2, بلغ ×2, رسل ×2; 33:39 eşi; D4 2MS 7 · 3MS 4, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T67 + "; aktör yok (ölçüm); A2 elçiye tebliğ emri; tebliğ etmemenin sonucu; Allah'ın koruması; kâfirlerin hidayetsizliği; A3 —; "
 "A4 " + BOLUM + "; edim geçişi şart → emir, nida, şart (ayetler arası); şart → cevap (ayet içi; COND 'in' 9. kelime: 've in lem tef'al' / 'fe-mâ bellağte risâletehû' (12. kelime)); şahıs geçişi 3 → 2 (ayetler arası).",
)

D[68] = ("◇ 'qul yâ ehle'l-kitâbi lestum 'alâ şey'in hattâ tuqîmu't-tevrâte ve'l-incîle ve mâ unzile ileykum min rabbikum ve le-yezîdenne kesîran minhum mâ unzile ileyke min rabbike tuğyânen ve kufran fe-lâ te'se 'ale'l-qavmi'l-kâfirîn' — "
 "IMPV 2MS I. bab + 'yâ' + 'ehl' + belirli 'kitâb' + PERF 2MP I. bab 'leyse' + ''alâ' + nekre 'şey'' + 'hattâ' + IMPF 2MP IV. bab + belirli 'tevrâ' + 've' + belirli 'incîl' + 've' + 'mâ' + edilgen PERF 3MS IV. bab + 'ilâ' + 2MP + 'min' + 'rabb' + 2MP + "
 "'ve' + 'le' + IMPF 3MS I. bab + te'kid nûnu + nekre 'kesîr' + 'min' + 3MP + 'mâ' + edilgen PERF 3MS IV. bab + 'ilâ' + 2MS + 'min' + 'rabb' + 2MS + nekre masdar 'tuğyân' + 've' + nekre 'kufr' + 'fe' + 'lâ' + IMPF 2MS I. bab + ''alâ' + belirli 'qavm' + belirli çoğul ortaç 'kâfir' "
 "(ölçüm edim emir, yasak, nida, kip EMPH 2 · IMPV 1 · PRO 1 · VOC 1, biçim NEHY; 2MP 6 · 2MS 4 · 3MP 1 · 3MS 3; bab I. bab ×4 · IV. bab ×3; EDİLGEN 2/7 fiil). "
 "Lafız yok; ölçüm '{{2|رَبّ 15, 23\\. sırada \\(rab z=1,10\\)}}' — satır aynen ('rabbikum', 'rabbike', Rab adı); esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm aktör '{{2|adlı تَوْراة 9\\. sırada \\(kitab, rol meful\\)}}' ve '{{2|adlı إِنجِيل 10\\. sırada \\(kitab, rol meful\\)}}' — satır aynen. "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=30 (n z=1,87); ölçüm '{{2|fâsıla ٱلكفرين → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|EDİLGEN 2/7 fiil, pas z=1,30}}' — satır aynen ('unzile' 12. ve 20. kelime); ölçüm '{{2|sayı işareti \\S+}}' — satır aynen ('kesîran' 17. kelime); "
 "ölçüm '{{2|simetri \\[8, 10, 18, 2\\]}}' — satır aynen; ölçüm '{{2|İÇ düğüm 2}}' — satır aynen; ölçüm '{{2|harf 131 → harf3 125, isaret 6}}' — satır aynen; ölçüm '{{2|dış düğüm 4}}' — satır aynen. "
 "Ölçüm IMPV 1: 'qul' (1. kelime); VOC 1: 'yâ' (2. kelime); EMPH 2: 'le' ve te'kid nûnu ('le-yezîdenne' 16. kelime); PRO 1: 'lâ' (26. kelime); 've'l-incîle' (10.), 've mâ' (11.) ve 've kufran' (25.)'daki 've' CONJ, 've le-yezîdenne' (16.)'daki 've' REM, 'fe-lâ' (26.)'daki 'fe' REM (okuma). "
 "Kök ikilemesi (ölçüm) ربب ×2 ('rabbikum' 15. / 'rabbike' 23. kelime), قوم ×2 ('tuqîmû' 8. / 'l-qavmi' 29. kelime), كفر ×2 ('kufran' 25. / 'l-kâfirîn' 30. kelime), نزل ×2 ('unzile' 12. / 20. kelime) (okuma). "
 + T68 + " (okuma). "
 + cumle(say('say 5:68 1-3', "qul yâ ehle'l-kitâb", True), say('say 5:68 2-3', "yâ ehle'l-kitâb"), say('dizi 5 68 1 3', "qâle ehl kitâb"), say('say 5:68 4-6', "lestum 'alâ şey'"), say('say 5:68 5-6', "'alâ şey'")) + ' '
 + cumle(say('say 5:68 7-12', "hattâ tuqîmu't-tevrâte ve'l-incîle ve mâ unzile", True), say('say 5:68 8-12', "tuqîmu't-tevrâte ve'l-incîle ve mâ unzile"), say('dizi 5 68 8 12', "eqâme tevrâ incîl mâ enzele"), say('say 5:68 11-15 --on', "ve mâ unzile ileykum min rabbikum"), say('say 5:68 12-15', "unzile ileykum min rabbikum")) + ' '
 + cumle(say('say 5:68 16-25 --on', "ve le-yezîdenne kesîran minhum mâ unzile ileyke min rabbike tuğyânen ve kufran", True), say('dizi 5 68 16 25', "zâde kesîr min mâ enzele ilâ min rabb tuğyân kufr"), say('say 5:68 19-23', "mâ unzile ileyke min rabbik"), say('dizi 5 68 19 23', "mâ enzele ilâ min rabb"), say('say 5:68 24-25', "tuğyânen ve kufran")) + ' '
 + cumle(say('say 5:68 26-30 --on', "fe-lâ te'se 'ale'l-qavmi'l-kâfirîn", True), say('dizi 5 68 26 29', "fe-lâ te'se 'alâ qavm"), say('say 5:68 27-30', "te'se 'ale'l-qavmi'l-kâfirîn"), say('say 5:68 29-30', "l-qavmi'l-kâfirîn")) + ' '
 "Ölçüm xref 3:64 ve 5:59 (basılmış) ve okunmuş ve henüz okunmamış başka ayetler. "
 "Ölçüm nakarat3 kalıpları: 'le-yezîdenne kesîran minhum mâ unzile ileyke min rabbike tuğyânen ve kufran', 'mâ unzile ileyke min rabbik', 'tuqîmu't-tevrâte ve'l-incîle ve mâ unzile', 'fe-lâ te'se 'ale'l-qavm' ve 'qul yâ ehle'l-kitâb' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'yâ' + izafet + belirli + PERF + ''alâ' + nekre + 'hattâ' + IMPF + belirli + 've' + belirli + 've' + 'mâ' + PERF + 'ilâ' + 'min' + izafet + 've' + 'le' + IMPF + nekre + 'min' + 'mâ' + PERF + 'ilâ' + 'min' + izafet + nekre + 've' + nekre + 'fe' + 'lâ' + IMPF + ''alâ' + belirli + belirli; "
 "D2 emir, yasak, nida, IMPV ('qul' 1. kelime), VOC ('yâ' 2. kelime), PRO ('lâ' 26. kelime), EMPH ('le-yezîdenne' 16. kelime), biçim NEHY; D3 ربب ×2, قوم ×2, كفر ×2, نزل ×2; D4 2MP 6 · 2MS 4 · 3MP 1 · 3MS 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T68 + "; aktör Tevrat ve İncil (ölçüm); A2 Kitap ehline hitap; Tevrat ve İncil'i ayakta tutma şartı; indirilenin artırdığı azgınlık ve küfür; üzülme yasağı; "
 "A3 'yâ ehle'l-kitâbi lestum 'alâ şey'in' ile açılan söz (söz içi, 2-15. kelime); "
 "A4 " + BOLUM + "; edim geçişi emir, nida, şart → emir, yasak, nida (ayetler arası); şahıs geçişi yok.",
)

D[69] = ("◇ 'inne'llezîne âmenû ve'llezîne hâdû ve's-sâbi'ûne ve'n-nasârâ men âmene bi'llâhi ve'l-yevmi'l-âxiri ve 'amile sâlihan fe-lâ xavfun 'aleyhim ve lâ hum yahzenûn' — "
 "'inne' + 'ellezî' + PERF 3MP IV. bab + 've' + 'ellezî' + PERF 3MP I. bab + 've' + belirli çoğul ortaç 'sâbi'' + 've' + belirli çoğul 'nasrânî' + 'men' + PERF 3MS IV. bab + 'bi' + lafız + 've' + belirli 'yevm' + belirli 'âxir' + 've' + PERF 3MS I. bab + nekre ortaç 'sâlih' + 'fe' + 'lâ' + nekre 'xavf' + ''alâ' + 3MP + 've' + 'lâ' + 3MP + IMPF 3MP I. bab "
 "(ölçüm edim şart, kip COND 1 · NEG 2; 3MP 8 · 3MS 2; bab I. bab ×3 · IV. bab ×2). "
 "Allah lafzı 10. sırada (ölçüm allah z=0,47); Rab yok; ölçüm '{{3|esmâ آخِر 12\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_el kaydı 'degil' — 've'l-yevmi'l-âxir', kural 'esmâ adı esmâ dışı göndergeyle → degil' (günün sıfatı, âhiret günü); ölçüm aktör '{{3|adlı صابِئ 6\\. sırada \\(cins, rol fail\\)}}' ve '{{3|adlı نَصْرانِيّ 7\\. sırada \\(cins, rol fail\\)}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=20 (n z=0,81); ölçüm '{{3|fâsıla يحزنون → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|simetri \\[3, 1, 17, 1\\]}}' — satır aynen; ölçüm '{{3|harf 95 → harf3 92, isaret 3}}' — satır aynen; ölçüm '{{3|dış düğüm 2}}' — satır aynen. "
 "Ölçüm COND 1: 'men' (8. kelime); NEG 2: 'lâ' (15. ve 18. kelime); 've'llezîne' (4.), 've's-sâbi'ûne' (6.), 've'n-nasârâ' (7.), 've'l-yevmi' (11.), 've 'amile' (13.) ve 've lâ' (18.)'daki 've' CONJ, 'fe-lâ' (15.)'daki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) أمن ×2 ('âmenû' 3. / 'âmene' 9. kelime) (okuma). "
 + T69 + " (okuma). "
 + cumle(say('say 5:69 1-5', "inne'llezîne âmenû ve'llezîne hâdû", True), say('say 5:69 2-3', "llezîne âmenû"), say('say 5:69 2-4', "llezîne âmenû ve'llezîne"), say('dizi 5 69 2 4', "ellezî âmene ellezî"), say('say 5:69 4-7 --on', "ve'llezîne hâdû ve's-sâbi'ûne ve'n-nasârâ"), say('say 5:69 5-7', "hâdû ve's-sâbi'ûne ve'n-nasârâ")) + ' '
 + cumle(say('say 5:69 8-12', "men âmene bi'llâhi ve'l-yevmi'l-âxir", True), say('say 5:69 9-12', "âmene bi'llâhi ve'l-yevmi'l-âxir"), say('say 5:69 11-12 --on', "ve'l-yevmi'l-âxir"), say('say 5:69 13-14 --on', "ve 'amile sâlihan")) + ' '
 + cumle(say('say 5:69 15-20 --on', "fe-lâ xavfun 'aleyhim ve lâ hum yahzenûn", True), say('say 5:69 16-20', "xavfun 'aleyhim ve lâ hum yahzenûn"), say('say 5:69 18-20 --on', "ve lâ hum yahzenûn")) + ' '
 "Ölçüm xref 2:62 (emsal olarak basıldı) ve okunmuş başka ayetler. "
 "Ölçüm nakarat3 kalıpları: 'llezîne âmenû ve'llezîne' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K2 'l-yevmi' (11. kelime).",
 "◈B — —",
 "◈D — D1 'inne' + 'ellezî' + PERF + 've' + 'ellezî' + PERF + 've' + belirli + 've' + belirli + 'men' + PERF + 'bi' + lafız + 've' + belirli + belirli + 've' + PERF + nekre + 'fe' + 'lâ' + nekre + ''alâ' + 've' + 'lâ' + IMPF; "
 "D2 şart, COND ('men' 8. kelime), NEG ('lâ' 15. ve 18. kelime); D3 أمن ×2; 2:62 eşi; D4 3MP 8 · 3MS 2, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T69 + "; aktör Sâbiîler ve Nasârâ (ölçüm); A2 iman edenler, Yahudi olanlar, Sâbiîler ve Nasârâ; Allah'a ve âhiret gününe iman; iyi iş; korkusuzluk ve üzülmeme; A3 —; "
 "A4 " + BOLUM + "; edim geçişi emir, yasak, nida → şart (ayetler arası); şart → cevap (ayet içi; COND 'men' 8. kelime: 'men âmene bi'llâhi ve'l-yevmi'l-âxiri ve 'amile sâlihan' / 'fe-lâ xavfun 'aleyhim' (15. kelime)); şahıs geçişi 2 → 3 (ayetler arası).",
)

D[70] = ("◇ 'le-qad exaznâ mîsâqa benî isrâ'île ve erselnâ ileyhim rusulen kullemâ câ'ehum rasûlun bi-mâ lâ tehvâ enfusuhum ferîqan kezzebû ve ferîqan yaqtulûn' — "
 "'le' + 'qad' + PERF 1P I. bab + 'mîsâq' + çoğul 'buneyy' (morph LEM ham biçim) + özel ad 'isrâ'îl' + 've' + PERF 1P IV. bab + 'ilâ' + 3MP + nekre çoğul 'rasûl' + 'kullemâ' + PERF 3MS I. bab + 3MP + nekre 'rasûl' + 'bi' + 'mâ' + 'lâ' + IMPF 3FS I. bab + çoğul 'nefs' + 3MP + nekre 'ferîq' + PERF 3MP II. bab + 've' + nekre 'ferîq' + IMPF 3MP I. bab "
 "(ölçüm edim haber, kip CERT 1 · EMPH 1 · NEG 1; 1P 4 · 3FS 1 · 3MP 7 · 3MS 1; bab I. bab ×4 · II. bab ×1 · IV. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm aktör '{{4|adlı إِسْرائِيل 5\\. sırada \\(kavim, rol mecrur\\)}}' — satır aynen; ölçüm '{{4|adsız `ferîk` 16\\. sırada}}' ve '{{4|adsız `ferîk` 18\\. sırada}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=19 (n z=0,70); ölçüm '{{4|fâsıla يقتلون → ن, N sınıfı}}' — satır aynen; ölçüm '{{4|harf 93 → harf3 87, isaret 6}}' — satır aynen; ölçüm '{{4|dış düğüm 2}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (1. kelime); EMPH 1: 'le' (1. kelime); NEG 1: 'lâ' (13. kelime); morph T 'kullemâ' (9. kelime); 've erselnâ' (6.) ve 've ferîqan' (18.)'daki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) رسل ×3 ('erselnâ' 6., 'rusulen' 8., 'rasûlun' 11. kelime), فرق ×2 ('ferîqan' 16. / 18. kelime) (okuma). "
 + T70 + " (okuma). "
 + cumle(say('say 5:70 1-5 --on', "le-qad exaznâ mîsâqa benî isrâ'îl", True), say('say 5:70 2-5', "exaznâ mîsâqa benî isrâ'îl"), say('say 5:70 3-5', "mîsâqa benî isrâ'îl"), say('dizi 5 70 3 5', "mîsâq buneyy isrâ'îl"), say('say 5:70 6-8 --on', "ve erselnâ ileyhim rusulen")) + ' '
 + cumle(say('say 5:70 9-11', "kullemâ câ'ehum rasûl", True), say('say 5:70 9-15', "kullemâ câ'ehum rasûlun bi-mâ lâ tehvâ enfusuhum"), say('say 5:70 12-15', "bi-mâ lâ tehvâ enfusuhum"), say('say 5:70 13-15', "lâ tehvâ enfusuhum")) + ' '
 + cumle(say('say 5:70 16-19', "ferîqan kezzebû ve ferîqan yaqtulûn", True), say('say 5:70 16-17', "ferîqan kezzebû"), say('say 5:70 18-19 --on', "ve ferîqan yaqtulûn")) + ' '
 "Ölçüm xref 2:87 (emsal olarak basıldı) ve okunmuş başka ayetler. "
 "Ölçüm nakarat3 kalıpları: 'mîsâqa benî isrâ'îl' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'ferîqan kezzebû' / 'ferîqan yaqtulûn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'le' + 'qad' + PERF + izafet + izafet + özel ad + 've' + PERF + 'ilâ' + nekre + 'kullemâ' + PERF + nekre + 'bi' + 'mâ' + 'lâ' + IMPF + izafet + nekre + PERF + 've' + nekre + IMPF; "
 "D2 haber, CERT ('qad' 1. kelime), EMPH ('le' 1. kelime), NEG ('lâ' 13. kelime); D3 رسل ×3, فرق ×2; 2:87 eşi; D4 1P 4 · 3FS 1 · 3MP 7 · 3MS 1, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T70 + "; aktör İsrâiloğulları (ölçüm); A2 ahit alma; elçi gönderme; canlarının hoşlanmadığı; yalanlama ve öldürme; A3 —; "
 "A4 " + BOLUM + "; edim geçişi şart → haber (ayetler arası); şahıs geçişi 3 → 1 (ayetler arası).",
)

out = ['# ── blok 5:67-70 (2026-11-16) ──', 'MEAL22 = {']
for n in range(67, 71):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M22 = {']
for n in range(67, 71):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL22); M.update(M22)']
open('/home/claude/yamalar/metin_5_67_70.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
