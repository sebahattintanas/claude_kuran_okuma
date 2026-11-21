# sûre 6 blok 20 (6:84-90) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b20/say2.txt'
os.environ['OLC'] = '/home/claude/b20/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Nebiler zinciri; onların yoluna uy' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 84: "Ona İshâk'ı ve Ya'kûb'u bağışladık; hepsini doğru yola ilettik. Nûh'u da daha önce doğru yola ilettik; onun soyundan Dâvûd'u, Süleymân'ı, Eyyûb'u, Yûsuf'u, Mûsâ'yı ve Hârûn'u da. İyilik edenleri böyle ödüllendiririz.",
 85: "Zekeriyyâ'yı, Yahyâ'yı, Îsâ'yı ve İlyâs'ı da; hepsi salihlerdendir.",
 86: "İsmâîl'i, Elyesa'ı, Yûnus'u ve Lût'u da; hepsini âlemlere üstün kıldık.",
 87: "Babalarından, soylarından ve kardeşlerinden de; onları seçtik ve dosdoğru bir yola ilettik.",
 88: "Bu, Allah'ın doğru yoludur; onunla kullarından dilediğini doğru yola iletir. Eğer ortak koşsalardı, yapmakta oldukları onlardan boşa giderdi.",
 89: "Onlar, kendilerine kitabı, hükmü ve nübüvveti verdiğimiz kimselerdir. Eğer bunlar onu inkâr ederse, onu inkâr etmeyen bir kavmi ona vekil kıldık.",
 90: "Onlar Allah'ın doğru yola ilettiği kimselerdir; sen de onların doğru yoluna uy. De ki: Buna karşılık sizden bir ücret istemiyorum; o, âlemler için ancak bir hatırlatmadır.",
}

T = {}
T[84] = ("konuşan 1P (adsız; 've vehebnâ', 'hedeynâ', 'hedeynâ', 'neczi' — 1., 6., 8. ve 20. kelime); 'lehû' 3MS (adsız; gönderge 6:83 4. kelime, 2. kelime); "
         "'zurriyyetihî' 3MS (adsız; gönderge 'nûhan' 7. kelime, 12. kelime; tartışmalı — 6:83 4. kelime okuması da var)")
T[85] = ("şahıs işareti yok (ölçüm); 'kullun' 5. kelime — 1-4. kelimedeki adlar (okuma)")
T[86] = ("konuşan 1P (adsız; 'faddalnâ' — 6. kelime)")
T[87] = ("'âbâ'ihim', 've zurriyyâtihim', 've ixvânihim' 3MP (adsız; gönderge 6:84 3. kelime — 2., 3. ve 4. kelime); konuşan 1P (adsız; 've'ctebeynâhum', 've hedeynâhum' — 5. ve 6. kelime); "
         "'ve'ctebeynâhum', 've hedeynâhum' 3MP (adsız; gönderge 6:84 3. kelime — 5. ve 6. kelime)")
T[88] = ("'yehdî', 'yeşâ'u', ''ibâdihî' 3MS (adsız; gönderge 'llâh' 3. kelime — 4., 7. ve 9. kelime); 'bihî' 3MS (adsız; gönderge 'hude' 2. kelime, 5. kelime); "
         "'eşrakû', ''anhum', 'kânû', 'ya'melûn' 3MP (adsız; gönderge 6:84 3. kelime — 11., 13., 15. ve 16. kelime); 'le-habita' 3MS (adsız; gönderge 'mâ' 14. kelime, 12. kelime)")
T[89] = ("'âteynâhumu' 3MP (adsız; gönderge 'ulâ'ike' 1. kelime, 3. kelime); konuşan 1P (adsız; 'âteynâhumu', 'vekkelnâ' — 3. ve 12. kelime); "
         "'yekfur' 3MS (fiil uyumu; 8. kelime — fail 10. kelime); 'bihâ' 3FS (adsız; gönderge 'n-nubuvvete' 6. kelime — 9., 13. ve 16. kelime; tartışmalı — 4-6. kelimedeki üç ada birden okuması da var); "
         "'leysû' 3MP (adsız; gönderge 'qavmen' 14. kelime, 15. kelime)")
T[90] = ("'hede' 3MS (fiil uyumu; 3. kelime — fail 4. kelime); 'hudâhumu' 3MP (adsız; gönderge 'ulâ'ike' 1. kelime, 5. kelime); muhatap 2MS (adsız; 'qtedih', 'qul' — 6. ve 7. kelime); "
         "konuşan 1S (adsız; söz içi; 'es'elukum' — 9. kelime); muhatap 2MP (adsız; söz içi; 'es'elukum' — 9. kelime); ''aleyhi', 'huve' 3MS (adsız; söz içi; gönderge 'hudâhumu' 5. kelime — 10. ve 13. kelime; tartışmalı)")

AKT84 = "{{1|aktör: adlı إِسْحاق 3\\. sırada.*?adlı هارُون 18\\. sırada \\(kisi, rol meful\\)}}"
AKT85 = "{{2|aktör: adlı زَكَرِيّا 1\\. sırada.*?adlı إِلْياس 4\\. sırada \\(kisi, rol meful\\)}}"
AKT86 = "{{3|aktör: adlı إِسْماعِيل 1\\. sırada.*?adlı لُوط 4\\. sırada \\(kisi, rol meful\\)}}"

D = {}
D[84] = ("◇ 've vehebnâ lehû ishâqa ve ya'qûbe kullen hedeynâ ve nûhan hedeynâ min qablu ve min zurriyyetihî dâvûde ve suleymâne ve eyyûbe ve yûsufe ve mûsâ ve hârûne ve kezâlike neczi'l-muhsinîn' — "
 "'ve' + PERF 1P I. bab + 1P + 'li' + 3MS + özel ad 'ishâq' + 've' + özel ad 'ya'qûb' + nekre 'kull' + PERF 1P I. bab + 1P + 've' + özel ad 'nûh' + PERF 1P I. bab + 1P + 'min' + 'qabl' + 've' + 'min' + 'zurriyye' + 3MS + "
 "özel ad 'dâvûd' + 've' + özel ad 'suleymân' + 've' + özel ad 'eyyûb' + 've' + özel ad 'yûsuf' + 've' + özel ad 'mûsâ' + 've' + özel ad 'hârûn' + 've' + 'ke' + 'zâ' + IMPF 1P I. bab + belirli çoğul etken ortaç 'muhsin' "
 "(ölçüm edim haber, kip yok; 1P 7 · 3MS 2; bab I. bab ×4). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm '" + AKT84 + "' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=21 (n z=0,91); ölçüm '{{1|fâsıla ٱلمحسنين → ن, N sınıfı}}' — satır aynen (6:83 م → 6:84 ن); "
 "ölçüm '{{1|simetri \\[6, 2, 13, 2\\]}}' — satır aynen; ölçüm '{{1|harf 103 → harf3 96, isaret 7}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; 've vehebnâ' (1.), 've ya'qûbe' (4.), 've nûhan' (7.), 've min' (11.), 've suleymâne' (14.), 've eyyûbe' (15.), 've yûsufe' (16.), 've mûsâ' (17.), 've hârûne' (18.) ve 've kezâlike' (19.) kelimelerindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) هدي ×2 ('hedeynâ' 6. / 8. kelime) (okuma). "
 + T[84] + " (okuma). "
 + cumle(say('say 6:84 1-4', "ve vehebnâ lehû ishâqa ve ya'qûbe", True)) + ' ' + cumle(say('say 6:84 9-11', "min qablu ve min", True), say('dizi 6 84 9 11', "min qabl min")) + ' ' + cumle(say('say 6:84 19-21', "ve kezâlike neczi'l-muhsinîn", True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'min qabl min' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + PERF + 'li' + özel ad + 've' + özel ad + nekre + PERF + 've' + özel ad + PERF + 'min' + 'qabl' + 've' + 'min' + izafet + özel ad + 've' + özel ad + 've' + özel ad + 've' + özel ad + 've' + özel ad + 've' + özel ad + 've' + 'ke' + 'zâ' + IMPF + belirli; "
 "D2 haber; D3 هدي ×2; 21:72 eşi; D4 1P 7 · 3MS 2, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[84] + "; aktör adlı 'ishâqa' (3. kelime; ölçüm rol meful), 'ya'qûbe' (4. kelime; ölçüm rol meful), 'nûhan' (7. kelime; ölçüm rol meful), 'dâvûde' (13. kelime; ölçüm rol meful), 'suleymâne' (14. kelime; ölçüm rol meful), "
 "'eyyûbe' (15. kelime; ölçüm rol meful), 'yûsufe' (16. kelime; ölçüm rol meful), 'mûsâ' (17. kelime; ölçüm rol meful), 'hârûne' (18. kelime; ölçüm rol meful); "
 "A2 İbrâhîm'e İshâk ve Ya'kûb'un bağışlanması; hepsinin ve önceden Nûh'un doğru yola iletilmesi; Nûh soyundan adı sayılanlar; iyilik edenlerin ödüllendirilmesi; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi yok (ayetler arası); bölüm açılışı.",
)

D[85] = ("◇ 've zekeriyyâ ve yahyâ ve 'îsâ ve ilyâse kullun mine's-sâlihîn' — "
 "'ve' + özel ad 'zekeriyyâ' + 've' + özel ad 'yahyâ' + 've' + özel ad ''îsâ' + 've' + özel ad 'ilyâs' + nekre 'kull' + 'min' + belirli çoğul etken ortaç 'sâlih' "
 "(ölçüm edim haber, kip yok; şahıs işareti yok; bab yok). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm '" + AKT85 + "' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=7 (n z=-0,58); ölçüm '{{2|fâsıla ٱلصلحين → ن, N sınıfı}}' — satır aynen (6:84 ن → 6:85 ن); "
 "ölçüm '{{2|simetri \\[3, 1, 4, 1\\]}}' — satır aynen; ölçüm '{{2|harf 35 → harf3 33, isaret 2}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; 've zekeriyyâ' (1.), 've yahyâ' (2.), 've 'îsâ' (3.) ve 've ilyâse' (4.) kelimelerindeki 've' CONJ (okuma). "
 "Kök ikilemesi yok (ölçüm). "
 + T[85] + ". "
 + cumle(say('say 6:85 5-7', "kullun mine's-sâlihîn", True)) + ' ' +
 "Ölçüm xref yok; ölçüm bağ yok (esit2, nakarat3, xref üçü de boş). "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 —; B4 'yahyâ' (2. kelime).",
 "◈D — D1 've' + özel ad + 've' + özel ad + 've' + özel ad + 've' + özel ad + nekre + 'min' + belirli; "
 "D2 haber; D3 —; D4 şahıs işareti yok, sahset —, iltifât 0.",
 "◈A — A1 " + T[85] + "; aktör adlı 'zekeriyyâ' (1. kelime; ölçüm rol meful), 'yahyâ' (2. kelime; ölçüm rol meful), ''îsâ' (3. kelime; ölçüm rol meful), 'ilyâse' (4. kelime; ölçüm rol meful); "
 "A2 adı sayılanlar; hepsinin salihlerden oluşu; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 1 → — (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[86] = ("◇ 've ismâ'île ve'l-yese'a ve yûnuse ve lûtan ve kullen faddalnâ 'ale'l-'âlemîn' — "
 "'ve' + özel ad 'ismâ'îl' + 've' + belirli özel ad 'l-yese'' + 've' + özel ad 'yûnus' + 've' + özel ad 'lût' + 've' + nekre 'kull' + PERF 1P II. bab + 1P + ''alâ' + belirli çoğul ''âlem' "
 "(ölçüm edim haber, kip yok; 1P 2; bab II. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm '" + AKT86 + "' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=8 (n z=-0,47); ölçüm '{{3|fâsıla ٱلعلمين → ن, N sınıfı}}' — satır aynen (6:85 ن → 6:86 ن); "
 "ölçüm '{{3|harf 45 → harf3 42, isaret 3}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen; ölçümde simetri alanı yok. "
 "Ölçüm kip yok; 've ismâ'île' (1.), 've'l-yese'a' (2.), 've yûnuse' (3.), 've lûtan' (4.) ve 've kullen' (5.) kelimelerindeki 've' CONJ (okuma). "
 "Kök ikilemesi yok (ölçüm). "
 + T[86] + " (okuma). "
 + cumle(say('say 6:86 5-8', "ve kullen faddalnâ 'ale'l-'âlemîn", True)) + ' ' +
 "Ölçüm xref yok; ölçüm bağ yok (esit2, nakarat3, xref üçü de boş). "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + özel ad + 've' + belirli özel ad + 've' + özel ad + 've' + özel ad + 've' + nekre + PERF + ''alâ' + belirli; "
 "D2 haber; D3 —; D4 1P 2, sahset ['1'], iltifât 0.",
 "◈A — A1 " + T[86] + "; aktör adlı 'ismâ'île' (1. kelime; ölçüm rol meful), 'l-yese'a' (2. kelime; ölçüm rol meful), 'yûnuse' (3. kelime; ölçüm rol meful), 'lûtan' (4. kelime; ölçüm rol meful); "
 "A2 adı sayılanlar; hepsinin âlemlere üstün kılınması; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi — → 1 (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[87] = ("◇ 've min âbâ'ihim ve zurriyyâtihim ve ixvânihim ve'ctebeynâhum ve hedeynâhum ilâ sırâtin mustaqîm' — "
 "'ve' + 'min' + çoğul 'âbâ'' + 3MP + 've' + çoğul 'zurriyye' + 3MP + 've' + çoğul 'ex' + 3MP + 've' + PERF 1P VIII. bab + 1P + 3MP + 've' + PERF 1P I. bab + 1P + 3MP + 'ilâ' + nekre 'sırât' + nekre etken ortaç 'mustaqîm' "
 "(ölçüm edim haber, kip yok; 1P 4 · 3MP 5; bab I. bab ×1 · VIII. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=9 (n z=-0,36); ölçüm '{{4|fâsıla مستقيم → م, N sınıfı}}' — satır aynen (6:86 ن → 6:87 م); "
 "ölçüm '{{4|harf 55 → harf3 52, isaret 3}}' — satır aynen; ölçüm '{{4|dış düğüm 1}}' — satır aynen; ölçümde simetri alanı yok. "
 "Ölçüm kip yok; 've min' (1.), 've zurriyyâtihim' (3.), 've ixvânihim' (4.), 've'ctebeynâhum' (5.) ve 've hedeynâhum' (6.) kelimelerindeki 've' CONJ (okuma). "
 "Kök ikilemesi yok (ölçüm). "
 + T[87] + " (okuma). "
 + cumle(say('say 6:87 7-9', "ilâ sırâtin mustaqîm", True), say('dizi 6 87 7 9', "ilâ sırât mustaqîm")) + ' ' +
 "Ölçüm xref okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'ilâ sırât mustaqîm' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'âbâ'ihim' / 've zurriyyâtihim' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'min' + izafet + 've' + izafet + 've' + izafet + 've' + PERF + 've' + PERF + 'ilâ' + nekre + nekre; "
 "D2 haber; D3 —; D4 1P 4 · 3MP 5, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[87] + "; aktör yok (ölçüm); A2 adı sayılanların babalarından, soylarından ve kardeşlerinden seçilenler; dosdoğru yola iletilme; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 1 → 3 (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[88] = ("◇ 'zâlike hude'llâhi yehdî bihî men yeşâ'u min 'ibâdihî ve lev eşrakû le-habita 'anhum mâ kânû ya'melûn' — "
 "'zâ' + 'li' + 'ke' + 'hudâ' + lafız + IMPF 3MS I. bab + 'bi' + 3MS + 'men' + IMPF 3MS I. bab + 'min' + çoğul ''abd' + 3MS + 've' + 'lev' + PERF 3MP IV. bab + 3MP + 'le' + PERF 3MS I. bab + ''an' + 3MP + 'mâ' + PERF 3MP I. bab + 3MP + IMPF 3MP I. bab + 3MP "
 "(ölçüm edim şart, kip COND 1 · EMPH 1; 3MP 7 · 3MS 5; bab I. bab ×5 · IV. bab ×1). "
 "Allah lafzı 3. sırada (ölçüm allah z=0,72); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=16 (n z=0,38); ölçüm '{{5|fâsıla يعملون → ن, N sınıfı}}' — satır aynen (6:87 م → 6:88 ن); "
 "ölçüm '{{5|simetri \\[3, 5, 13, 1\\]}}' — satır aynen; ölçüm '{{5|harf 64 → harf3 59, isaret 5}}' — satır aynen; ölçüm '{{5|dış düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 've lev' (10. kelime); EMPH 1: 'le-habita' (12. kelime); 've lev' (10.) kelimesindeki 've' REM; 'zâlike' (1.) DEM (okuma). "
 "Kök ikilemesi (ölçüm) هدي ×2 ('hude' 2. / 'yehdî' 4. kelime) (okuma). "
 + T[88] + " (okuma). "
 + cumle(say('say 6:88 1-7', "zâlike hude'llâhi yehdî bihî men yeşâ'u", True)) + ' ' + cumle(say('say 6:88 4-7', "yehdî bihî men yeşâ'u", True)) + ' ' + cumle(say('say 6:88 13-15', "'anhum mâ kânû", True), say('dizi 6 88 13 15', "'an mâ kâne")) + ' ' + cumle(say('say 6:88 14-16', "mâ kânû ya'melûn", True), say('dizi 6 88 14 16', "mâ kâne 'amile")) + ' ' +
 "Ölçüm xref okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'mâ kâne 'amile' süzgeç GEÇER, ''an mâ kâne' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'hude'llâhi' / 'eşrakû' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'zâ' + izafet + lafız + IMPF + 'bi' + 'men' + IMPF + 'min' + izafet + 've' + 'lev' + PERF + 'le' + PERF + ''an' + 'mâ' + PERF + IMPF; "
 "D2 şart; COND ('ve lev' 10. kelime), EMPH ('le-habita' 12. kelime); D3 هدي ×2; 39:23 eşi; D4 3MP 7 · 3MS 5, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[88] + "; aktör yok (ölçüm); A2 Allah'ın doğru yolu; kullarından dilediğini doğru yola iletmesi; ortak koşma hâlinde amellerin boşa gitmesi; "
 "A3 —; "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; COND 'lev' 10. kelime: 've lev eşrakû' / 'le-habita' (12. kelime)); şahıs geçişi yok (ayetler arası); edim geçişi haber → şart (ayetler arası).",
)

D[89] = ("◇ 'ulâ'ike'llezîne âteynâhumu'l-kitâbe ve'l-hukme ve'n-nubuvvete fe-in yekfur bihâ hâ'ulâ'i fe-qad vekkelnâ bihâ qavmen leysû bihâ bi-kâfirîn' — "
 "'ulâ'i' + 'ke' + 'ellezî' + PERF 1P IV. bab + 1P + 3MP + belirli 'kitâb' + 've' + belirli 'hukm' + 've' + belirli 'nubuvve' + 'fe' + 'in' + IMPF 3MS I. bab + 'bi' + 3FS + 'hâ' + 'ulâ'i' + 'fe' + 'qad' + PERF 1P II. bab + 1P + 'bi' + 3FS + nekre 'qavm' + PERF 3MP I. bab + 3MP + 'bi' + 3FS + 'bi' + çoğul etken ortaç 'kâfir' "
 "(ölçüm edim şart, kip CERT 1 · COND 1; 1P 4 · 3FS 3 · 3MP 3 · 3MS 1; bab I. bab ×2 · II. bab ×1 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=17 (n z=0,49); ölçüm '{{6|biçim DIKKAT}}' — satır aynen; ölçüm '{{6|fâsıla بكفرين → ن, N sınıfı}}' — satır aynen (6:88 ن → 6:89 ن); "
 "ölçüm '{{6|simetri \\[3, 1, 9, 1\\]}}' — satır aynen; ölçüm '{{6|harf 83 → harf3 79, isaret 4}}' — satır aynen; ölçüm '{{6|dış düğüm 2}}' — satır aynen. "
 "Ölçüm CERT 1: 'fe-qad' (11. kelime); COND 1: 'fe-in' (7. kelime); 've'l-hukme' (5.) ve 've'n-nubuvvete' (6.) kelimelerindeki 've' CONJ; 'fe-in' (7.) kelimesindeki 'fe' REM; 'fe-qad' (11.) kelimesindeki 'fe' RSLT; 'ulâ'ike' (1.) ve 'hâ'ulâ'i' (10.) DEM (okuma). "
 "Kök ikilemesi (ölçüm) كفر ×2 ('yekfur' 8. / 'bi-kâfirîn' 17. kelime) (okuma). "
 + T[89] + " (okuma). "
 + cumle(say('say 6:89 2-4', "llezîne âteynâhumu'l-kitâbe", True), say('dizi 6 89 2 4', "ellezî âtâ kitâb")) + ' ' + cumle(say('say 6:89 4-6', "l-kitâbe ve'l-hukme ve'n-nubuvvete", True)) + ' ' +
 "Ölçüm xref okunmuş 2 ayet. "
 "Ölçüm nakarat3 kalıbı: 'ellezî âtâ kitâb' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'yekfur' / 'leysû bihâ bi-kâfirîn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'ulâ'i' + 'ellezî' + PERF + belirli + 've' + belirli + 've' + belirli + 'fe' + 'in' + IMPF + 'bi' + 'hâ' + 'ulâ'i' + 'fe' + 'qad' + PERF + 'bi' + nekre + PERF + 'bi' + 'bi' + 'kâfir'; "
 "D2 şart; CERT ('fe-qad' 11. kelime), COND ('fe-in' 7. kelime); D3 كفر ×2; D4 1P 4 · 3FS 3 · 3MP 3 · 3MS 1, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[89] + "; aktör yok (ölçüm); A2 adı sayılanlara kitap, hüküm ve nübüvvetin verilmesi; bunların inkârı hâlinde inkâr etmeyen bir kavmin vekil kılınması; "
 "A3 —; "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; COND 'in' 7. kelime: 'fe-in yekfur bihâ hâ'ulâ'i' / 'fe-qad vekkelnâ' (11. kelime)); şahıs geçişi 3 → 1 (ayetler arası; şahıs sayısında 3. şahıs toplamı 7 · 1P 4 — ölçüm baskın 1, beraberlik değil, araç tanımı farkı); edim geçişi yok (ayetler arası).",
)

D[90] = ("◇ 'ulâ'ike'llezîne hede'llâhu fe-bi-hudâhumu'qtedih qul lâ es'elukum 'aleyhi ecran in huve illâ zikrâ li'l-'âlemîn' — "
 "'ulâ'i' + 'ke' + 'ellezî' + PERF 3MS I. bab + lafız + 'fe' + 'bi' + 'hudâ' + 3MP + IMPV 2MS VIII. bab + IMPV 2MS I. bab + 'lâ' + IMPF 1S I. bab + 2MP + ''alâ' + 3MS + nekre 'ecr' + 'in' + 3MS + 'illâ' + 'zikrâ' + 'li' + belirli çoğul ''âlem' "
 "(ölçüm edim emir, kip IMPV 2 · NEG 2 · RES 1; 1S 1 · 2MP 1 · 2MS 2 · 3MP 1 · 3MS 3; bab I. bab ×3 · VIII. bab ×1). "
 "Allah lafzı 4. sırada (ölçüm allah z=0,72); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=16 (n z=0,38); ölçüm '{{7|biçim HASR}}' — satır aynen; ölçüm '{{7|fâsıla للعلمين → ن, N sınıfı}}' — satır aynen (6:89 ن → 6:90 ن); "
 "ölçüm '{{7|simetri \\[3, 1, 12, 1\\]}}' — satır aynen; ölçüm '{{7|harf 69 → harf3 65, isaret 4}}' — satır aynen; ölçüm '{{7|dış düğüm 0}}' — satır aynen. "
 "Ölçüm IMPV 2: 'qtedih' (6. kelime), 'qul' (7. kelime); NEG 2: 'lâ' (8. kelime), 'in' (12. kelime); RES 1: 'illâ' (14. kelime); 'fe-bi-hudâhumu' (5.) kelimesindeki 'fe' REM; 'ulâ'ike' (1.) DEM (okuma). "
 "Kök ikilemesi (ölçüm) هدي ×2 ('hede' 3. / 'hudâhumu' 5. kelime) (okuma). "
 + T[90] + " (okuma). "
 + cumle(say('say 6:90 8-11', "lâ es'elukum 'aleyhi ecran", True)) + ' ' +
 "Ölçüm xref yok; ölçüm bağ yok (esit2, nakarat3, xref üçü de boş). "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'ulâ'i' + 'ellezî' + PERF + lafız + 'fe' + 'bi' + izafet + IMPV + IMPV + 'lâ' + IMPF + ''alâ' + nekre + 'in' + 'huve' + 'illâ' + 'zikrâ' + 'li' + belirli; "
 "D2 emir; IMPV ('qtedih' 6. kelime, 'qul' 7. kelime), NEG ('lâ' 8. kelime, 'in' 12. kelime), RES ('illâ' 14. kelime); D3 هدي ×2; D4 1S 1 · 2MP 1 · 2MS 2 · 3MP 1 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[90] + "; aktör yok (ölçüm); A2 Allah'ın doğru yola ilettikleri; onların doğru yoluna uyma emri; ücret istememe; âlemler için hatırlatma; "
 "A3 'lâ es'elukum 'aleyhi ecran in huve illâ zikrâ li'l-'âlemîn' (söz içi, 8-16. kelime); "
 "A4 " + BOLUM + "; söz açılır (8. kelime); söz kapanır (16. kelime, ayet içi); şahıs geçişi 1 → 3 (ayetler arası); edim geçişi şart → emir (ayetler arası); bölüm kapanışı.",
)
out = ['# ── blok 6:84-90 (2026-11-21) ──', 'MEAL20 = {']
for n in range(84, 91):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M20 = {']
for n in range(84, 91):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL20); M.update(M20)']
open('/home/claude/yamalar/metin_6_84_90.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
