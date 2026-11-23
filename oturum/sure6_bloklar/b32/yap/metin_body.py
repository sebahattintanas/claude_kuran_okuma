# sûre 6 blok 32 (6:136-138) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b32/say2.txt'
os.environ['OLC'] = '/home/claude/b32/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Ekinlerde ve hayvanlarda pay; sekiz eş' bölümünde"
N1 = "mâ fe'ale yezere mâ iftarâ"; N2 = "lev şâ'e allâh mâ"; N3 = "şâ'e allâh mâ"; N4 = "zekere ism allâh"; N5 = "cezâ bi-mâ kâne"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 136: "Allah'a, yarattığı ekinden ve hayvanlardan bir pay ayırdılar ve iddialarınca, bu Allah'ındır, bu da ortaklarımızındır, dediler. Ortaklarına ait olan Allah'a ulaşmaz; Allah'a ait olan ise ortaklarına ulaşır. Hükmettikleri ne kötüdür.",
 137: "Böylece ortakları, ortak koşanlardan çoğuna çocuklarını öldürmeyi süslü gösterdi ki onları helâk etsinler ve dinlerini onlara karıştırsınlar. Allah dileseydi bunu yapmazlardı. Artık onları ve uydurduklarını bırak.",
 138: "İddialarınca, bu hayvanlar ve ekin yasaktır, onları dilediğimiz dışında kimse yiyemez, dediler. Sırtları haram kılınmış hayvanlar ve üzerine Allah'ın adını anmadıkları hayvanlar da vardır; O'na iftira olarak. Uydurmakta olduklarıyla onları cezalandıracaktır.",
}

T = {}
T[136] = ("'ve ce'alû', 'fe-qâlû', 'yahkumûn' 3MP (adsız; tartışmalı — 1., 9. ve 31. kelime); 'bi-za'mihim', 'li-şurakâ'ihim', 'şurakâ'ihim' 3MP eki (adsız; gönderge 've ce'alû' 1. kelime — 12., 17. ve 28. kelime); "
          "konuşan 1P (adsız; söz içi; 'li-şurakâ'inâ' — 14. kelime); 'zera'e' 3MS (adsız; gönderge 'li'llâhi' 2. kelime, 4. kelime); 'kâne', 'yesilu' 3MS (adsız; gönderge 'fe-mâ' 15. kelime — 16. ve 19. kelime); "
          "'kâne', 'fe-huve', 'yesilu' 3MS (adsız; gönderge 've mâ' 22. kelime — 23., 25. ve 26. kelime); 'sâ'e' 3MS (adsız; gönderge 'mâ' 30. kelime, 29. kelime)")
T[137] = ("'zeyyene' 3MS (fiil uyumu; 2. kelime — fail 8. kelime); 'evlâdihim', 'şurakâ'uhum' 3MP eki (adsız; gönderge 'l-muşrikîne' 5. kelime — 7. ve 8. kelime); "
          "'li-yurdûhum', 've li-yelbisû' 3MP (adsız; gönderge 'şurakâ'uhum' 8. kelime — 9. ve 10. kelime); 'li-yurdûhum', ''aleyhim', 'dînehum' 3MP eki (adsız; gönderge 'l-muşrikîne' 5. kelime — 9., 11. ve 12. kelime); "
          "'şâ'e' 3MS (fiil uyumu; 14. kelime — fail 15. kelime); 'fe'alûh' 3MP (adsız; tartışmalı; gönderge 'l-muşrikîne' 5. kelime, 17. kelime); 'fe'alûh' 3MS eki (adsız; gönderge 'qatle' 6. kelime, 17. kelime); "
          "muhatap 2MS (adsız; 'fe-zerhum' — 18. kelime); 'fe-zerhum', 'yefterûn' 3MP (adsız; gönderge 'l-muşrikîne' 5. kelime — 18. ve 20. kelime)")
T[138] = ("'ve qâlû' 3MP (adsız; tartışmalı — 1. kelime); 'yat'amuhâ' 3MS (adsız; söz içi; gönderge 'men' 9. kelime, 7. kelime); 'yat'amuhâ' 3FS eki (adsız; söz içi; gönderge 'en'âmun' 3. kelime, 7. kelime); "
          "konuşan 1P (adsız; söz içi; 'neşâ'u' — 10. kelime); 'bi-za'mihim' 3MP eki (adsız; tartışmalı; gönderge 've qâlû' 1. kelime, 11. kelime); "
          "'hurrimet' 3FS (fiil uyumu; 13. kelime — edilgen; naib-i faili 'zuhûruhâ' (14. kelime)); 'zuhûruhâ' 3FS eki (adsız; gönderge 've en'âmun' 12. kelime, 14. kelime); "
          "'yezkurûne' 3MP (adsız; gönderge 've qâlû' 1. kelime, 17. kelime); ''aleyhâ' 3FS eki (adsız; gönderge 've en'âmun' 15. kelime, 20. kelime); ''aleyh' 3MS eki (adsız; gönderge 'llâhi' 19. kelime, 22. kelime); "
          "'se-yeczîhim' 3MS (adsız; gönderge 'llâhi' 19. kelime, 23. kelime); 'se-yeczîhim', 'kânû', 'yefterûn' 3MP (adsız; gönderge 've qâlû' 1. kelime — 23., 25. ve 26. kelime)")

D = {}
D[136] = ("◇ 've ce'alû li'llâhi mimmâ zera'e mine'l-harsi ve'l-en'âmi nasîben fe-qâlû hâzâ li'llâhi bi-za'mihim ve hâzâ li-şurakâ'inâ, fe-mâ kâne li-şurakâ'ihim fe-lâ yesilu ilâ'llâh, ve mâ kâne li'llâhi fe-huve yesilu ilâ şurakâ'ihim, sâ'e mâ yahkumûn' — "
 "'ve' + PERF 3MP I. bab + 3MP + 'li' + lafız + 'min' + 'mâ' + PERF 3MS I. bab + 'min' + belirli 'hars' + 've' + belirli çoğul 'na'am' + nekre 'nasîb' + 'fe' + PERF 3MP I. bab + 3MP + 'hâzâ' + 'li' + lafız + 'bi' + 'za'm' + 3MP + 've' + 'hâzâ' + 'li' + çoğul 'şerîk' + 1P + "
 "'fe' + 'mâ' + PERF 3MS I. bab + 'li' + çoğul 'şerîk' + 3MP + 'fe' + 'lâ' + IMPF 3MS I. bab + 'ilâ' + lafız + 've' + 'mâ' + PERF 3MS I. bab + 'li' + lafız + 'fe' + 'huve' + IMPF 3MS I. bab + 'ilâ' + çoğul 'şerîk' + 3MP + PERF 3MS I. bab + 'mâ' + IMPF 3MP I. bab + 3MP "
 "(ölçüm edim haber, kip NEG 1; 1P 1 · 3MP 9 · 3MS 7; bab I. bab ×9). "
 "Allah lafzı 2., 11., 21. ve 24. sırada (ölçüm allah z=2,05); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=31 (n z=1,97); ölçüm '{{1|fâsıla يحكمون → ن, N sınıfı}}' — satır aynen (6:135 ن → 6:136 ن); "
 "ölçüm '{{1|simetri \\[7, 13, 20, 2\\]}}' — satır aynen; ölçüm '{{1|harf 133 → harf3 127, isaret 6}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 1: 'fe-lâ' (18. kelime); 've ce'alû' (1.) kelimesindeki 've' REM, 've'l-en'âmi' (7.), 've hâzâ' (13.) ve 've mâ' (22.) kelimelerindeki 've' CONJ; 'fe-qâlû' (9.) kelimesindeki 'fe' CONJ, 'fe-mâ' (15.) kelimesindeki 'fe' REM, 'fe-lâ' (18.) ve 'fe-huve' (25.) kelimelerindeki 'fe' SUP (okuma). "
 "Kök ikilemesi (ölçüm) أله ×4 ('li'llâhi' 2. / 'li'llâhi' 11. / 'llâh' 21. / 'li'llâhi' 24. kelime), شرك ×3 ('li-şurakâ'inâ' 14. / 'li-şurakâ'ihim' 17. / 'şurakâ'ihim' 28. kelime), كون ×2 ('kâne' 16. / 'kâne' 23. kelime), وصل ×2 ('yesilu' 19. / 'yesilu' 26. kelime) (okuma). "
 + T[136] + " (okuma). "
 + cumle(say('say 6:136 1-2', "ve ce'alû li'llâh", True)) + ' '
 + cumle(say('say 6:136 11-12', "li'llâhi bi-za'mihim", True)) + ' '
 + cumle(say('say 6:136 29-31', "sâ'e mâ yahkumûn", True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'fe-lâ yesilu ilâ'llâh' / 'fe-huve yesilu ilâ şurakâ'ihim' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'l-en'âmi' (7. kelime); B2 —; B3 —; B4 —.",
 "◈D — D1 've' + PERF + 'li' + lafız + 'min' + 'mâ' + PERF + 'min' + belirli + 've' + belirli + nekre + 'fe' + PERF + 'hâzâ' + 'li' + lafız + 'bi' + izafet + 've' + 'hâzâ' + 'li' + izafet + "
 "'fe' + 'mâ' + PERF + 'li' + izafet + 'fe' + 'lâ' + IMPF + 'ilâ' + lafız + 've' + 'mâ' + PERF + 'li' + lafız + 'fe' + 'huve' + IMPF + 'ilâ' + izafet + PERF + 'mâ' + IMPF; "
 "D2 haber; NEG ('fe-lâ' 18. kelime); D3 أله ×4, شرك ×3, كون ×2, وصل ×2; D4 1P 1 · 3MP 9 · 3MS 7, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[136] + "; aktör yok (ölçüm); A2 Allah'ın yarattığı ekinden ve hayvanlardan Allah'a pay ayırmaları; payı Allah'a ve ortaklarına bölmeleri; ortakların payının Allah'a ulaşmaması, Allah'ın payının ortaklara ulaşması; hükümlerinin kötülüğü; "
 "A3 'hâzâ li'llâhi bi-za'mihim ve hâzâ li-şurakâ'inâ' (söz içi, 10-14. kelime); "
 "A4 " + BOLUM + "; söz açılır (10. kelime); söz kapanır (14. kelime, ayet içi); şahıs geçişi 2 → 3 (ayetler arası); edim geçişi emir, nida → haber (ayetler arası); bölüm açılışı.",
)

D[137] = ("◇ 've kezâlike zeyyene li-kesîrin mine'l-muşrikîne qatle evlâdihim şurakâ'uhum li-yurdûhum ve li-yelbisû 'aleyhim dînehum, ve lev şâ'e'llâhu mâ fe'alûh, fe-zerhum ve mâ yefterûn' — "
 "'ve' + 'ke' + 'zâlike' + PERF 3MS II. bab + 'li' + nekre 'kesîr' + 'min' + belirli çoğul etken ortaç 'muşrik' + masdar 'qatl' + çoğul 'veled' + 3MP + çoğul 'şerîk' + 3MP + 'li' + IMPF 3MP IV. bab + 3MP + 3MP + 've' + 'li' + IMPF 3MP I. bab + 3MP + ''alâ' + 3MP + 'dîn' + 3MP + "
 "'ve' + 'lev' + PERF 3MS I. bab + lafız + 'mâ' + PERF 3MP I. bab + 3MP + 3MS + 'fe' + IMPV 2MS I. bab + 3MP + 've' + 'mâ' + IMPF 3MP VIII. bab + 3MP "
 "(ölçüm edim emir, şart, kip COND 1 · IMPV 1 · NEG 1; 2MS 1 · 3MP 14 · 3MS 3; bab I. bab ×4 · II. bab ×1 · IV. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 15. sırada (ölçüm allah z=0,47); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=20 (n z=0,81); ölçüm '{{2|fâsıla يفترون → ن, N sınıfı}}' — satır aynen (6:136 ن → 6:137 ن); "
 "ölçüm '{{2|sayı işareti كَثِير}}' — satır aynen; ölçüm '{{2|harf 99 → harf3 95, isaret 4}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm COND 1: 'lev' (13. kelime); NEG 1: 'mâ' (16. kelime); IMPV 1: 'fe-zerhum' (18. kelime); 've kezâlike' (1.), 've li-yelbisû' (10.) ve 've mâ' (19.) kelimelerindeki 've' CONJ, 've lev' (13.) kelimesindeki 've' REM; 'fe-zerhum' (18.) kelimesindeki 'fe' REM (okuma). "
 "Kök ikilemesi (ölçüm) شرك ×2 ('l-muşrikîne' 5. / 'şurakâ'uhum' 8. kelime) (okuma). "
 + T[137] + " (okuma). "
 + cumle(say('say 6:137 1-2', 've kezâlike zeyyene', True)) + ' '
 + cumle(say('say 6:137 13-17', "ve lev şâ'e'llâhu mâ fe'alûh", True)) + ' '
 + cumle(say('say 6:137 13-16', "ve lev şâ'e'llâhu mâ", True), say('dizi 6 137 13 16', N2)) + " (--medde 3 ayet: 'mâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). "
 + cumle(say('say 6:137 14-16', "şâ'e'llâhu mâ", True), say('dizi 6 137 14 16', N3)) + " (--medde 6 ayet: 'mâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). "
 + cumle(say('say 6:137 16-20', "mâ fe'alûh, fe-zerhum ve mâ yefterûn", True), say('dizi 6 137 16 20', N1)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: '" + N1 + "' süzgeç GEÇER, '" + N2 + "' süzgeç GEÇER, '" + N3 + "' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'ke' + 'zâlike' + PERF + 'li' + nekre + 'min' + belirli + masdar + izafet + izafet + 'li' + IMPF + 've' + 'li' + IMPF + ''alâ' + izafet + 've' + 'lev' + PERF + lafız + 'mâ' + PERF + 'fe' + IMPV + 've' + 'mâ' + IMPF; "
 "D2 emir, şart; COND ('lev' 13. kelime), NEG ('mâ' 16. kelime), IMPV ('fe-zerhum' 18. kelime); D3 شرك ×2; D4 2MS 1 · 3MP 14 · 3MS 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[137] + "; aktör yok (ölçüm); A2 ortakların, ortak koşanlardan çoğuna çocuklarını öldürmeyi süslü göstermesi; amaç olarak onları helâk etmeleri ve dinlerini karıştırmaları; Allah dileseydi yapmayacakları; onları ve uydurduklarını bırakma emri; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi haber → emir, şart (ayetler arası); şart → cevap (ayet içi; COND 'lev' 13. kelime: 'lev şâ'e'llâhu' / 'mâ fe'alûh' (16. kelime)); hitap açılır (ayet içi).",
)

D[138] = ("◇ 've qâlû hâzihî en'âmun ve harsun hicrun lâ yat'amuhâ illâ men neşâ'u bi-za'mihim ve en'âmun hurrimet zuhûruhâ ve en'âmun lâ yezkurûne isma'llâhi 'aleyhâ 'ftirâ'en 'aleyh, se-yeczîhim bi-mâ kânû yefterûn' — "
 "'ve' + PERF 3MP I. bab + 3MP + 'hâzihî' + nekre çoğul 'na'am' + 've' + nekre 'hars' + nekre 'hicr' + 'lâ' + IMPF 3MS I. bab + 3FS + 'illâ' + 'men' + IMPF 1P I. bab + 'bi' + 'za'm' + 3MP + 've' + nekre çoğul 'na'am' + edilgen PERF 3FS II. bab + çoğul 'zahr' + 3FS + "
 "'ve' + nekre çoğul 'na'am' + 'lâ' + IMPF 3MP I. bab + 3MP + 'ism' + lafız + ''alâ' + 3FS + nekre masdar 'iftirâ'' + ''alâ' + 3MS + 'se' + IMPF 3MS I. bab + 3MP + 'bi' + 'mâ' + PERF 3MP I. bab + 3MP + IMPF 3MP VIII. bab + 3MP "
 "(ölçüm edim haber, kip FUT 1 · NEG 2 · RES 1; 1P 1 · 3FS 4 · 3MP 10 · 3MS 3; bab I. bab ×6 · II. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 19. sırada (ölçüm allah z=0,24); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=26 (n z=1,44); ölçüm '{{3|EDİLGEN 1/8 fiil, pas z=0,38}}' — satır aynen; ölçüm '{{3|fâsıla يفترون → ن, N sınıfı}}' — satır aynen (6:137 ن → 6:138 ن); "
 "ölçüm '{{3|simetri \\[3, 6, 20, 1\\]}}' — satır aynen; ölçüm '{{3|harf 121 → harf3 114, isaret 7}}' — satır aynen; ölçüm '{{3|dış düğüm 5}}' — satır aynen; ölçüm '{{3|İÇ düğüm 3}}' — satır aynen. "
 "Ölçüm NEG 2: 'lâ' (6. kelime), 'lâ' (16. kelime); RES 1: 'illâ' (8. kelime); FUT 1: 'se-yeczîhim' (23. kelime); 've qâlû' (1.), 've harsun' (4.), 've en'âmun' (12.) ve 've en'âmun' (15.) kelimelerindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) فري ×2 (''ftirâ'en' 21. / 'yefterûn' 26. kelime), نعم ×3 ('en'âmun' 3. / 've en'âmun' 12. / 've en'âmun' 15. kelime) (okuma). "
 + T[138] + " (okuma). "
 + cumle(say('say 6:138 17-19', "yezkurûne isma'llâh", True), say('dizi 6 138 17 19', N4)) + ' '
 + cumle(say('say 6:138 18-20', "isma'llâhi 'aleyhâ", True), say('dizi 6 138 17 20', "zekere ism allâh 'alâ")) + ' '
 + cumle(say('say 6:138 23-26', 'se-yeczîhim bi-mâ kânû yefterûn', True), say('dizi 6 138 23 25', N5)) + ' ' +
 "Ölçüm xref 22:36 (emsal olarak basıldı), 6:118 (basılmış), 6:119 (basılmış), 6:121 (basılmış) ve okunmuş 4 ayet. "
 "Ölçüm nakarat3 kalıpları: '" + N4 + "' süzgeç GEÇER, '" + N5 + "' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'en'âmun' (3. kelime), 'en'âmun' (12. kelime), 'en'âmun' (15. kelime); B2 —; B3 —; B4 —.",
 "◈D — D1 've' + PERF + 'hâzihî' + nekre + 've' + nekre + nekre + 'lâ' + IMPF + 'illâ' + 'men' + IMPF + 'bi' + izafet + 've' + nekre + PERF + izafet + 've' + nekre + 'lâ' + IMPF + 'ism' + lafız + ''alâ' + nekre + ''alâ' + 'se' + IMPF + 'bi' + 'mâ' + PERF + IMPF; "
 "D2 haber; NEG ('lâ' 6. kelime, 'lâ' 16. kelime), RES ('illâ' 8. kelime), FUT ('se-yeczîhim' 23. kelime); D3 فري ×2, نعم ×3; 22:36 eşi; D4 1P 1 · 3FS 4 · 3MP 10 · 3MS 3, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[138] + "; aktör yok (ölçüm); A2 hayvanlar ve ekin için yasak iddiası; sırtları haram kılınmış hayvanlar; üzerine Allah'ın adı anılmayan hayvanlar; uydurdukları için cezalandırılmaları; "
 "A3 'hâzihî en'âmun ve harsun hicrun lâ yat'amuhâ illâ men neşâ'u' (söz içi, 2-10. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (10. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi emir, şart → haber (ayetler arası).",
)
