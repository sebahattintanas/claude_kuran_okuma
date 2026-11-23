# sûre 6 blok 33 (6:139-141) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b33/say2.txt'
os.environ['OLC'] = '/home/claude/b33/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Ekinlerde ve hayvanlarda pay; sekiz eş' bölümünde"
N1 = "in kâne meyte"; N2 = "qad xasira ellezî"; N3 = "_ ellezî enşe'e"; N4 = "semer izâ esmera"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 139: "Bu hayvanların karınlarındaki, erkeklerimize mahsustur, eşlerimize haramdır, dediler. Ölü olursa onlar onda ortaktırlar. Onları nitelemeleriyle cezalandıracaktır. O, hakîmdir, bilendir.",
 140: "Çocuklarını beyinsizlikle, bilgisizce öldürenler ve Allah'ın kendilerine rızık olarak verdiğini Allah'a iftira olarak haram kılanlar ziyana uğramıştır. Kesinlikle saptılar ve doğru yolu bulanlar olmadılar.",
 141: "O, çardaklı ve çardaksız bahçeleri, ürünü çeşitli hurmayı ve ekini, birbirine benzer ve benzemez zeytini ve narı inşâ edendir. Meyve verdiğinde meyvesinden yiyin, hasat gününde hakkını da verin, israf etmeyin. Şüphesiz O, israf edenleri sevmez.",
}

T = {}
T[139] = ("'ve qâlû' 3MP (adsız; tartışmalı — 1. kelime); konuşan 1P (adsız; söz içi; 'li-zukûrinâ', 'ezvâcinâ' — 8. ve 11. kelime); 'yekun' 3MS (adsız; gönderge 'mâ' 2. kelime, 13. kelime); "
          "'fe-hum' 3MP (adsız; tartışmalı; gönderge 've qâlû' 1. kelime, 15. kelime); 'fîhi' 3MS (adsız; gönderge 'mâ' 2. kelime, 16. kelime); "
          "'se-yeczîhim' 3MS (gizli zamir, adsız; 18. kelime — fail 18. kelime içi gizli zamir, gönderge 6:138 19. kelime; 'hakîmun' 21. kelime ayrı cümlenin haberi); 'innehû' 3MS eki (adsız; gönderge 6:138 19. kelime, 20. kelime); 'se-yeczîhim', 'vasfehum' 3MP eki (adsız; gönderge 've qâlû' 1. kelime — 18. ve 19. kelime)")
T[140] = ("'xasira' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'qatelû', 'evlâdehum' 3MP (adsız; gönderge 'llezîne' 3. kelime — 4. ve 5. kelime); 've harramû' 3MP (adsız; gönderge 'llezîne' 3. kelime, 9. kelime); "
          "'razaqahumu' 3MS (fiil uyumu; 11. kelime — fail 12. kelime); 'razaqahumu' 3MP eki (adsız; gönderge 'llezîne' 3. kelime, 11. kelime); 'dallû', 'kânû' 3MP (adsız; gönderge 'llezîne' 3. kelime — 17. ve 19. kelime)")
T[141] = ("'ve huve', 'enşe'e' 3MS (adsız; gönderge 6:140 12. kelime — 1. ve 3. kelime); 'ukuluhû', 'semerihî', 'esmera', 'haqqahû', 'hasâdih' 3MS (adsız; tartışmalı; gönderge 've'n-naxle' 8. kelime — 11., 19., 21., 23. ve 25. kelime); "
          "muhatap 2MP (adsız; 'kulû', 've âtû', 'tusrifû' — 17., 22. ve 27. kelime); 'innehû', 'yuhibbu' 3MS (adsız; gönderge 6:140 12. kelime — 28. ve 30. kelime)")

D = {}
D[139] = ("◇ 've qâlû mâ fî butûni hâzihi'l-en'âmi xâlisatun li-zukûrinâ ve muharramun 'alâ ezvâcinâ, ve in yekun meyteten fe-hum fîhi şurakâ', se-yeczîhim vasfehum, innehû hakîmun 'alîm' — "
 "'ve' + PERF 3MP I. bab + 3MP + 'mâ' + 'fî' + çoğul 'batn' + 'hâzihi' + belirli çoğul 'na'am' + nekre etken ortaç 'xâlisa' + 'li' + çoğul 'zeker' + 1P + 've' + nekre edilgen ortaç 'muharram' + ''alâ' + çoğul 'zevc' + 1P + "
 "'ve' + 'in' + IMPF 3MS I. bab + nekre 'meyte' + 'fe' + 'hum' + 'fî' + 3MS + çoğul 'şerîk' + 'se' + IMPF 3MS I. bab + 3MP + 'vasf' + 3MP + 'inne' + 3MS + nekre 'hakîm' + nekre ''alîm' "
 "(ölçüm edim şart, kip COND 1 · FUT 1; 1P 2 · 3MP 5 · 3MS 4; bab I. bab ×3). "
 "Allah lafzı yok; Rab yok; ölçüm '{{1|esmâ حَكِيم 21\\. sırada, SON konum, MÜHÜR \\| عَلِيم 22\\. sırada, SON konum, MÜHÜR}}' — satır aynen; esma_kayit çıktısı 'mühür EVET (ÇİFT) ton denge' — ölçüm MÜHÜR ile uyuşuyor (muhur_el EVET); "
 "esma_el kaydı 'ilahi' — 'innehû hakîmun 'alîm', kural ''inne/enne' haberi → ilahi' (Allah) ve ''alîm' için kural ''inne/enne' haberi → ilahi' (Allah; morph ADJ ile 'hakîm'in sıfatı) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=22 (n z=1,02); ölçüm '{{1|fâsıla عليم → م, N sınıfı}}' — satır aynen (6:138 ن → 6:139 م); "
 "ölçüm '{{1|sayı işareti زَوْج}}' — satır aynen; ölçüm '{{1|simetri \\[3, 2, 15, 1\\]}}' — satır aynen; ölçüm '{{1|harf 101 → harf3 93, isaret 8}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm COND 1: 'in' (12. kelime); FUT 1: 'se-yeczîhim' (18. kelime); 've qâlû' (1.), 've muharramun' (9.) ve 've in' (12.) kelimelerindeki 've' CONJ; 'fe-hum' (15.) kelimesindeki 'fe' RSLT; 'innehû' (20.) ACC (okuma). "
 + T[139] + " (okuma). "
 + cumle(say('say 6:139 12-14', 've in yekun meyteten', True), say('dizi 6 139 12 14', N1)) + ' '
 + cumle(say('say 6:139 21-22', "hakîmun 'alîm", True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: '" + N1 + "' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'li-zukûrinâ' / 'ezvâcinâ' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'l-en'âmi' (6. kelime); B2 'ezvâcinâ' (11. kelime); B3 —; B4 'meyteten' (14. kelime).",
 "◈D — D1 've' + PERF + 'mâ' + 'fî' + izafet + 'hâzihi' + belirli + nekre + 'li' + izafet + 've' + nekre + ''alâ' + izafet + 've' + 'in' + IMPF + nekre + 'fe' + 'hum' + 'fî' + 'şerîk' + 'se' + IMPF + izafet + 'inne' + nekre + nekre; "
 "D2 şart; COND ('in' 12. kelime), FUT ('se-yeczîhim' 18. kelime); D3 —; D4 1P 2 · 3MP 5 · 3MS 4, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[139] + "; aktör yok (ölçüm); A2 hayvanların karnındakini erkeklere mahsus, eşlere haram saymaları; ölü doğanda ortak olmaları; nitelemelerinin cezalandırılması; Allah'ın hakîm ve bilen oluşu; "
 "A3 'mâ fî butûni hâzihi'l-en'âmi xâlisatun li-zukûrinâ ve muharramun 'alâ ezvâcinâ' (söz içi, 2-11. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (11. kelime, ayet içi); şart → cevap (ayet içi; COND 'in' 12. kelime: 'in yekun' / 'fe-hum' (15. kelime)); şahıs geçişi yok (ayetler arası); edim geçişi haber → şart (ayetler arası).",
)

D[140] = ("◇ 'qad xasira'llezîne qatelû evlâdehum sefehen bi-ğayri 'ilmin ve harramû mâ razaqahumu'llâhu 'ftirâ'en 'ale'llâh, qad dallû ve mâ kânû muhtedîn' — "
 "'qad' + PERF 3MS I. bab + 'ellezîne' + PERF 3MP I. bab + 3MP + çoğul 'veled' + 3MP + nekre 'sefeh' + 'bi' + 'ğayr' + nekre ''ilm' + 've' + PERF 3MP II. bab + 3MP + 'mâ' + PERF 3MS I. bab + 3MP + lafız + nekre masdar 'iftirâ'' + ''alâ' + lafız + "
 "'qad' + PERF 3MP I. bab + 3MP + 've' + 'mâ' + PERF 3MP I. bab + 3MP + çoğul etken ortaç 'muhtedî' "
 "(ölçüm edim haber, kip CERT 2 · NEG 1; 3MP 10 · 3MS 2; bab I. bab ×5 · II. bab ×1). "
 "Allah lafzı 12. ve 15. sırada (ölçüm allah z=1,47); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=20 (n z=0,81); ölçüm '{{2|fâsıla مهتدين → ن, N sınıfı}}' — satır aynen (6:139 م → 6:140 ن); "
 "ölçüm '{{2|simetri \\[3, 1, 14, 1\\]}}' — satır aynen; ölçüm '{{2|harf 89 → harf3 82, isaret 7}}' — satır aynen; ölçüm '{{2|dış düğüm 1}}' — satır aynen. "
 "Ölçüm CERT 2: 'qad' (1. kelime), 'qad' (16. kelime); NEG 1: 'mâ' (18. kelime); 've harramû' (9.) kelimesindeki 've' CONJ, 've mâ' (18.) kelimesindeki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhu' 12. / 'llâh' 15. kelime) (okuma). "
 + T[140] + " (okuma). "
 + cumle(say('say 6:140 1-3', "qad xasira'llezîne", True), say('dizi 6 140 1 3', N2)) + ' '
 + cumle(say('say 6:140 18-20', 've mâ kânû muhtedîn', True)) + ' ' +
 "Ölçüm xref okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: '" + N2 + "' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'qad' + PERF + 'ellezîne' + PERF + izafet + nekre + 'bi' + 'ğayr' + nekre + 've' + PERF + 'mâ' + PERF + lafız + nekre + ''alâ' + lafız + 'qad' + PERF + 've' + 'mâ' + PERF + 'muhtedî'; "
 "D2 haber; CERT ('qad' 1. kelime, 'qad' 16. kelime), NEG ('mâ' 18. kelime); D3 أله ×2; D4 3MP 10 · 3MS 2, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[140] + "; aktör yok (ölçüm); A2 çocuklarını öldürenlerin ve Allah'ın rızkını haram kılanların ziyana uğraması; sapmaları ve doğru yolu bulamamaları; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi şart → haber (ayetler arası).",
)

D[141] = ("◇ 've huve'llezî enşe'e cennâtin ma'rûşâtin ve ğayra ma'rûşâtin ve'n-naxle ve'z-zer'a muxtelifen ukuluhû ve'z-zeytûne ve'r-rummâne muteşâbihen ve ğayra muteşâbih, kulû min semerihî izâ esmera ve âtû haqqahû yevme hasâdih, ve lâ tusrifû, innehû lâ yuhibbu'l-musrifîn' — "
 "'ve' + 'huve' + 'ellezî' + PERF 3MS IV. bab + nekre çoğul 'cenne' + nekre edilgen ortaç 'ma'rûşa' + 've' + 'ğayr' + nekre edilgen ortaç 'ma'rûşa' + 've' + belirli 'naxl' + 've' + belirli 'zer'' + nekre etken ortaç 'muxtelif' + 'ukul' + 3MS + "
 "'ve' + belirli 'zeytûn' + 've' + belirli 'rummân' + nekre etken ortaç 'muteşâbih' + 've' + 'ğayr' + nekre etken ortaç 'muteşâbih' + IMPV 2MP I. bab + 2MP + 'min' + 'semer' + 3MS + 'izâ' + PERF 3MS IV. bab + "
 "'ve' + IMPV 2MP IV. bab + 2MP + 'haqq' + 3MS + 'yevm' + 'hasâd' + 3MS + 've' + 'lâ' + IMPF 2MP IV. bab + 2MP + 'inne' + 3MS + 'lâ' + IMPF 3MS IV. bab + belirli çoğul etken ortaç 'musrif' "
 "(ölçüm edim emir, yasak, kip IMPV 2 · NEG 1 · PRO 1; 2MP 6 · 3MS 9; bab I. bab ×1 · IV. bab ×5). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=31 (n z=1,97); ölçüm '{{3|fâsıla ٱلمسرفين → ن, N sınıfı}}' — satır aynen (6:140 ن → 6:141 ن); "
 "ölçüm '{{3|simetri \\[3, 1, 28, 1\\]}}' — satır aynen; ölçüm '{{3|harf 158 → harf3 141, isaret 17}}' — satır aynen; ölçüm '{{3|dış düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 2: 'kulû' (17. kelime), 've âtû' (22. kelime); PRO 1: 'lâ' (26. kelime); NEG 1: 'lâ' (29. kelime); 've huve' (1.), 've ğayra' (6.), 've'n-naxle' (8.), 've'z-zer'a' (9.), 've'z-zeytûne' (12.), 've'r-rummâne' (13.), 've ğayra' (15.), 've âtû' (22.) ve 've lâ' (26.) kelimelerindeki 've' CONJ; 'innehû' (28.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) أكل ×2 ('ukuluhû' 11. / 'kulû' 17. kelime), ثمر ×2 ('semerihî' 19. / 'esmera' 21. kelime), سرف ×2 ('tusrifû' 27. / 'l-musrifîn' 31. kelime), شبه ×2 ('muteşâbihen' 14. / 'muteşâbih' 16. kelime), عرش ×2 ('ma'rûşâtin' 5. / 'ma'rûşâtin' 7. kelime), غير ×2 ('ve ğayra' 6. / 've ğayra' 15. kelime) (okuma). "
 + T[141] + " (okuma). "
 + cumle(say('say 6:141 1-3', "ve huve'llezî enşe'e", True), say('dizi 6 141 1 3', N3)) + ' '
 + cumle(say('say 6:141 12-13', "ve'z-zeytûne ve'r-rummâne", True)) + ' '
 + cumle(say('say 6:141 19-21', 'semerihî izâ esmera', True), say('dizi 6 141 19 21', N4)) + ' '
 + cumle(say('say 6:141 28-31', "innehû lâ yuhibbu'l-musrifîn", True)) + ' ' +
 "Ölçüm xref okunmamış 1 ayet. "
 "Ölçüm nakarat3 kalıpları: '" + N3 + "' süzgeç GEÇMEZ, '" + N4 + "' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'ma'rûşâtin' / 've ğayra ma'rûşâtin' — ayetler arası: yok.",
 "◈K — K2 'yevme' (24. kelime).",
 "◈B — —",
 "◈D — D1 've' + 'huve' + 'ellezî' + PERF + nekre + nekre + 've' + 'ğayr' + nekre + 've' + belirli + 've' + belirli + nekre + izafet + 've' + belirli + 've' + belirli + nekre + 've' + 'ğayr' + nekre + IMPV + 'min' + izafet + 'izâ' + PERF + 've' + IMPV + izafet + 'yevm' + izafet + 've' + 'lâ' + IMPF + 'inne' + 'lâ' + IMPF + belirli; "
 "D2 emir, yasak; IMPV ('kulû' 17. kelime, 've âtû' 22. kelime), PRO ('lâ' 26. kelime), NEG ('lâ' 29. kelime); D3 أكل ×2, ثمر ×2, سرف ×2, شبه ×2, عرش ×2, غير ×2; D4 2MP 6 · 3MS 9, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[141] + "; aktör yok (ölçüm); A2 bahçeleri, hurmayı, ekini, zeytini ve narı inşâ edişi; meyvesinden yeme ve hasat günü hakkını verme emri; israf yasağı; israf edenleri sevmeyişi; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi haber → emir, yasak (ayetler arası); hitap açılır (ayet içi).",
)
