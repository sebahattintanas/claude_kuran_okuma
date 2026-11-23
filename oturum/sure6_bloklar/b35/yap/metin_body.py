# sûre 6 blok 35 (6:145-147) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b35/say2.txt'
os.environ['OLC'] = '/home/claude/b35/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Haram kılınanlar; şahitlerinizi getirin' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 145: "De ki: Bana vahyedilende, yiyen bir kimseye, yiyeceği haram bir şey bulmuyorum; ölü ya da akıtılmış kan ya da domuz eti olması dışında, çünkü o şüphesiz pisliktir, ya da Allah'tan başkası adına kesilmiş bir fısk olması dışında. Kim saldırmadan ve sınırı aşmadan zorda kalırsa, şüphesiz Rabbin bağışlayandır, merhamet edendir.",
 146: "Yahudi olanlara her tırnaklıyı haram kıldık. Sığırdan ve koyundan da, sırtlarının ya da bağırsakların taşıdığı ya da kemiğe karışan dışında, onların iç yağlarını onlara haram kıldık. Bu, azgınlıkları sebebiyle onları cezalandırmamızdır; şüphesiz biz doğru söyleyenleriz.",
 147: "Eğer seni yalanlarlarsa, de ki: Rabbiniz geniş bir rahmet sahibidir; O'nun şiddeti suçlu kavimden geri çevrilmez.",
}

T = {}
T[145] = ("muhatap 2MS (adsız; 'qul' — 1. kelime); konuşan 1S (adsız; söz içi; 'ecidu', 'ileyye' — 3. ve 7. kelime); 'ûhiye' 3MS (adsız; söz içi; edilgen, naib-i faili 'mâ' 5. kelime, 6. kelime); "
          "'yat'amuhû' 3MS (adsız; söz içi; gönderge 'tâ'imin' 10. kelime, 11. kelime); 'hû' 3MS eki (adsız; söz içi; gönderge 'muharramen' 8. kelime, 11. kelime); 'yekûne' 3MS (adsız; söz içi; gönderge 'muharramen' 8. kelime, 14. kelime); "
          "'fe-innehû' 3MS eki (adsız; söz içi; gönderge 'lahme' 20. kelime, 22. kelime); 'uhille' 3MS (adsız; söz içi; edilgen, naib-i faili 'fisqan' 25. kelime, 26. kelime); 'bih' 3MS eki (adsız; söz içi; gönderge 'fisqan' 25. kelime, 29. kelime); "
          "'dturra' 3MS (adsız; edilgen, naib-i faili 'meni' 30. kelime, 31. kelime); 'rabbeke' muhatap 2MS eki (adsız; 37. kelime)")
T[146] = ("'hâdû' 3MP (adsız; gönderge 'llezîne' 2. kelime, 3. kelime); konuşan 1P (adsız; 'harramnâ', 'harramnâ', 'cezeynâhum', 'innâ' — 4., 11., 25. ve 27. kelime); "
          "''aleyhim' 3MP eki (adsız; gönderge 'llezîne' 2. kelime, 12. kelime); 'şuhûmehumâ' 3D eki (adsız; gönderge 'l-baqari', 'l-ğanemi' 9. ve 10. kelime, 13. kelime); "
          "'hamelet' 3FS (fiil uyumu; 16. kelime — fail 17. kelime); 'zuhûruhumâ' 3D eki (adsız; gönderge 'l-baqari', 'l-ğanemi' 9. ve 10. kelime, 17. kelime); 'xteleta' 3MS (adsız; gönderge 'mâ' 21. kelime, 22. kelime); "
          "'cezeynâhum', 'bi-bağyihim' 3MP eki (adsız; gönderge 'llezîne' 2. kelime — 25. ve 26. kelime)")
T[147] = ("'kezzebûke' 3MP (adsız; tartışmalı; gönderge 6:146 2. kelime, 2. kelime); 'kezzebûke' muhatap 2MS eki (adsız; 2. kelime); muhatap 2MS (adsız; 'qul' — 3. kelime); muhatap 2MP eki (adsız; söz içi; 'rabbukum' — 4. kelime); "
          "'yureddu' 3MS (fiil uyumu; söz içi; edilgen, naib-i faili 10. kelime, 9. kelime); 'be'suhû' 3MS eki (adsız; söz içi; gönderge 'rabbukum' 4. kelime, 10. kelime)")

D = {}
D[145] = ("◇ 'qul lâ ecidu fî mâ ûhiye ileyye muharramen 'alâ tâ'imin yat'amuhû illâ en yekûne meyteten ev demen mesfûhan ev lahme xinzîrin fe-innehû ricsun ev fisqan uhille li-ğayri'llâhi bih, fe-meni'dturra ğayra bâğin ve lâ 'âdin fe-inne rabbeke ğafûrun rahîm' — "
 "IMPV 2MS I. bab + 'lâ' + IMPF 1S I. bab + 'fî' + 'mâ' + PERF 3MS IV. bab edilgen + 'ilâ' + 1S + nekre edilgen ortaç 'muharram' + ''alâ' + nekre etken ortaç 'tâ'im' + IMPF 3MS I. bab + 3MS + 'illâ' + 'en' + IMPF 3MS I. bab + nekre 'meyte' + 'ev' + nekre 'dem' + nekre edilgen ortaç 'mesfûh' + 'ev' + 'lahm' + nekre 'xinzîr' + 'fe' + 'inne' + 3MS + nekre 'rics' + "
 "'ev' + nekre 'fisq' + PERF 3MS IV. bab edilgen + 'li' + 'ğayr' + lafız + 'bi' + 3MS + 'fe' + 'men' + PERF 3MS VIII. bab edilgen + 'ğayr' + nekre etken ortaç 'bâğ' + 've' + 'lâ' + nekre etken ortaç ''âd' + 'fe' + 'inne' + 'rabb' + 2MS + nekre 'ğafûr' + nekre 'rahîm' "
 "(ölçüm edim emir, şart, kip COND 1 · IMPV 1 · NEG 2; 1S 2 · 2MS 2 · 3MS 8; bab I. bab ×4 · IV. bab ×2 · VIII. bab ×1). "
 "Allah lafzı 28. sırada (ölçüm allah z=-0,01); Rab 37. sırada (ölçüm rab z=0,22); ölçüm '{{1|esmâ غَفُور 38\\. sırada, SON konum, MÜHÜR \\| رَحِيم 39\\. sırada, SON konum, MÜHÜR}}' — satır aynen; esma_kayit çıktısı 'mühür EVET (ÇİFT)' — ölçüm MÜHÜR ile uyuşuyor; "
 "esma_el kaydı 'ilahi' — 'fe-inne rabbeke ğafûrun rahîm', kural ''inne/enne' haberi → ilahi' (Rab) ve 'rahîm' için kural ''inne/enne' haberi → ilahi' (Rab; morph ADJ ile 'ğafûr'un sıfatı) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=39 (n z=2,82); ölçüm '{{1|EDİLGEN 3/7 fiil, pas z=2,12}}' — satır aynen; ölçüm '{{1|fâsıla رحيم → م, N sınıfı}}' — satır aynen (6:144 ن → 6:145 م); "
 "ölçüm '{{1|simetri \\[3, 2, 5, 1\\]}}' — satır aynen; ölçüm '{{1|harf 139 → harf3 128, isaret 11}}' — satır aynen; ölçüm '{{1|dış düğüm 5}}' — satır aynen. "
 "Ölçüm IMPV 1: 'qul' (1. kelime); NEG 2: 'lâ' (2. kelime), 'lâ' (34. kelime); COND 1: 'meni' (30. kelime); ölçüm biçim ISTISNA — 'illâ' (12. kelime); 've lâ' (34.) kelimesindeki 've' CONJ; 'fe-innehû' (22.) ve 'fe-meni' (30.) kelimelerindeki 'fe' REM; 'fe-inne' (36.) kelimesindeki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) طعم ×2 ('tâ'imin' 10. / 'yat'amuhû' 11. kelime), غير ×2 ('li-ğayri' 27. / 'ğayra' 32. kelime) (okuma). "
 + T[145] + " (okuma). "
 + say('say 6:145 1-2', "qul lâ", True) + " (--medde 14 ayet: 'lâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). "
 + say('say 6:145 4-5', "fî mâ", True) + " (--medde 11 ayet: 'mâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). "
 + cumle(say('say 6:145 5-7', "mâ ûhiye ileyye", True), say('dizi 6 145 5 7', "mâ evhâ ilâ")) + ' '
 + cumle(say('say 6:145 13-15', "en yekûne meyteten", True), say('dizi 6 145 13 15', "en kâne meyte")) + ' '
 + cumle(say('say 6:145 26-35', "uhille li-ğayri'llâhi bih, fe-meni'dturra ğayra bâğin ve lâ 'âdin", True), say('dizi 6 145 26 35', "uhille ğayr allâh _ men idturra ğayr bâğ lâ 'âd")) + ' '
 + cumle(say('say 6:145 30-35', "fe-meni'dturra ğayra bâğin ve lâ 'âdin", True), say('dizi 6 145 30 35', "men idturra ğayr bâğ lâ 'âd"), say('dizi 6 145 30 36', "men idturra ğayr bâğ lâ 'âd inne")) + ' ' +
 "Ölçüm xref 2:173 (emsal olarak basıldı), 16:115 (emsal olarak basıldı) ve okunmuş 3 ayet. "
 "Ölçüm nakarat3 kalıpları: 'mâ evhâ ilâ' süzgeç GEÇMEZ, 'en kâne meyte' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 —; B4 'meyteten' (15. kelime).",
 "◈D — D1 IMPV + 'lâ' + IMPF + 'fî' + 'mâ' + PERF + 'ilâ' + nekre + ''alâ' + nekre + IMPF + 'illâ' + 'en' + IMPF + nekre + 'ev' + nekre + nekre + 'ev' + 'lahm' + nekre + 'fe' + 'inne' + nekre + 'ev' + nekre + PERF + 'li' + 'ğayr' + lafız + 'bi' + 'fe' + 'men' + PERF + 'ğayr' + nekre + 've' + 'lâ' + nekre + 'fe' + 'inne' + izafet + nekre + nekre; "
 "D2 emir, şart; COND ('meni' 30. kelime), IMPV ('qul' 1. kelime), NEG ('lâ' 2. kelime, 'lâ' 34. kelime); D3 2:173 eşi, 16:115 eşi; D4 1S 2 · 2MS 2 · 3MS 8, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[145] + "; aktör yok (ölçüm); A2 vahyedilende ölü, akıtılmış kan, domuz eti ve Allah'tan başkası adına kesilen dışında haram bulunmayışı; zorda kalana Rabbin bağışlaması ve merhameti; "
 "A3 'lâ ecidu fî mâ ûhiye ileyye muharramen 'alâ tâ'imin yat'amuhû illâ en yekûne meyteten ev demen mesfûhan ev lahme xinzîrin fe-innehû ricsun ev fisqan uhille li-ğayri'llâhi bih' (söz içi, 2-29. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (29. kelime, ayet içi); şart → cevap (ayet içi; COND 'meni' 30. kelime: 'fe-meni'dturra' / 'fe-inne' (36. kelime)); şahıs geçişi yok (ayetler arası); edim geçişi soru, emir → emir, şart (ayetler arası); bölüm açılışı.",
)

D[146] = ("◇ 've 'ale'llezîne hâdû harramnâ kulle zî zufur, ve mine'l-baqari ve'l-ğanemi harramnâ 'aleyhim şuhûmehumâ illâ mâ hamelet zuhûruhumâ evi'l-havâyâ ev mâ'xteleta bi-'azm, zâlike cezeynâhum bi-bağyihim, ve innâ le-sâdiqûn' — "
 "'ve' + ''alâ' + 'ellezî' + PERF 3MP I. bab + PERF 1P II. bab + 'kull' + 'zû' + nekre 'zufur' + 've' + 'min' + belirli 'baqar' + 've' + belirli 'ğanem' + PERF 1P II. bab + ''alâ' + 3MP + çoğul 'şuhûm' + 3D + 'illâ' + 'mâ' + PERF 3FS I. bab + çoğul 'zahr' + 3D + 'ev' + belirli çoğul 'havâyâ' + 'ev' + 'mâ' + PERF 3MS VIII. bab + 'bi' + nekre ''azm' + "
 "'zâlike' + PERF 1P I. bab + 3MP + 'bi' + 'bağy' + 3MP + 've' + 'inne' + 1P + 'le' + çoğul etken ortaç 'sâdiq' "
 "(ölçüm edim haber, kip EMPH 1; 1P 7 · 3D 2 · 3FS 1 · 3MP 5 · 3MS 1; bab I. bab ×3 · II. bab ×2 · VIII. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=28 (n z=1,65); ölçüm '{{2|HAPAKS: شحم \\*\\(iç yağ \\(şahm\\)\\)\\* — hapaks z=3,28}}' — satır aynen (yeni kök karşılığı 'iç yağ'); "
 "ölçüm '{{2|fâsıla لصدقون → ن, N sınıfı}}' — satır aynen (6:145 م → 6:146 ن); ölçüm '{{2|simetri \\[4, 12, 18, 1\\]}}' — satır aynen; ölçüm '{{2|harf 126 → harf3 120, isaret 6}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm EMPH 1: 'le-sâdiqûn' (28. kelime); ölçüm biçim ISTISNA — 'illâ' (14. kelime); 've 'ale' (1.), 've mine' (8.) ve 've'l-ğanemi' (10.) kelimelerindeki 've' CONJ; 've innâ' (27.) kelimesindeki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) حرم ×2 ('harramnâ' 4. / 'harramnâ' 11. kelime) (okuma). "
 + T[146] + " (okuma). "
 "Ölçüm xref yok. Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 'hamelet' (16. kelime); B3 —; B4 —.",
 "◈D — D1 've' + ''alâ' + 'ellezî' + PERF + PERF + 'kull' + 'zû' + nekre + 've' + 'min' + belirli + 've' + belirli + PERF + ''alâ' + izafet + 'illâ' + 'mâ' + PERF + izafet + 'ev' + belirli + 'ev' + 'mâ' + PERF + 'bi' + nekre + 'zâlike' + PERF + 'bi' + izafet + 've' + 'inne' + 'le' + 'sâdiq'; "
 "D2 haber; EMPH ('le-sâdiqûn' 28. kelime); D3 حرم ×2; D4 1P 7 · 3D 2 · 3FS 1 · 3MP 5 · 3MS 1, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[146] + "; aktör yok (ölçüm); A2 Yahudi olanlara her tırnaklıyı haram kılış; sığır ve koyunun iç yağlarını, sırt, bağırsak ve kemiğe karışan dışında haram kılış; azgınlıkları sebebiyle cezalandırma; konuşanın doğru söyleyişi; şahıs toplamı (1. şahıs 7 · 3. şahıs 9) ölçüm baskın 1 ile ayrık — beraberlik değil, ölçüm baskını konuşan 1P; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 1 (ayetler arası); edim geçişi emir, şart → haber (ayetler arası).",
)

D[147] = ("◇ 'fe-in kezzebûke fe-qul rabbukum zû rahmetin vâsi'atin, ve lâ yureddu be'suhû 'ani'l-qavmi'l-mucrimîn' — "
 "'fe' + 'in' + PERF 3MP II. bab + 2MS + 'fe' + IMPV 2MS I. bab + 'rabb' + 2MP + 'zû' + nekre 'rahme' + nekre etken ortaç 'vâsi'a' + 've' + 'lâ' + IMPF 3MS I. bab edilgen + 'be's' + 3MS + ''an' + belirli 'qavm' + belirli çoğul etken ortaç 'mucrim' "
 "(ölçüm edim emir, şart, kip COND 1 · IMPV 1 · NEG 1; 2MP 1 · 2MS 2 · 3MP 2 · 3MS 2; bab I. bab ×2 · II. bab ×1). "
 "Allah lafzı yok; Rab 4. sırada (ölçüm rab z=1,32); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=13 (n z=0,06); ölçüm '{{3|EDİLGEN 1/3 fiil, pas z=1,57}}' — satır aynen; ölçüm '{{3|fâsıla ٱلمجرمين → ن, N sınıfı}}' — satır aynen (6:146 ن → 6:147 ن); "
 "ölçüm '{{3|harf 53 → harf3 50, isaret 3}}' — satır aynen; ölçüm '{{3|dış düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 'in' (1. kelime); IMPV 1: 'qul' (3. kelime); NEG 1: 'lâ' (8. kelime); 'fe-in' (1.) kelimesindeki 'fe' REM; 'fe-qul' (3.) kelimesindeki 'fe' RSLT; 've lâ' (8.) kelimesindeki 've' REM (okuma). "
 + T[147] + " (okuma). "
 + cumle(say('say 6:147 11-13', "'ani'l-qavmi'l-mucrimîn", True), say('dizi 6 147 8 13', "lâ radde be's 'an qavm mucrim")) + ' ' +
 "Ölçüm xref 12:110 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'rahmetin' / 'be'suhû' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'fe' + 'in' + PERF + 'fe' + IMPV + izafet + 'zû' + nekre + nekre + 've' + 'lâ' + IMPF + izafet + ''an' + belirli + belirli; "
 "D2 emir, şart; COND ('in' 1. kelime), IMPV ('qul' 3. kelime), NEG ('lâ' 8. kelime); D3 12:110 eşi; D4 2MP 1 · 2MS 2 · 3MP 2 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[147] + "; aktör yok (ölçüm); A2 yalanlanma durumunda Rabbin geniş rahmetinin bildirilmesi; şiddetinin suçlu kavimden geri çevrilmeyişi; "
 "A3 'rabbukum zû rahmetin vâsi'atin, ve lâ yureddu be'suhû 'ani'l-qavmi'l-mucrimîn' (söz içi, 4-13. kelime); "
 "A4 " + BOLUM + "; söz açılır (4. kelime); söz kapanır (13. kelime, ayet içi); şart → cevap (ayet içi; COND 'in' 1. kelime: 'fe-in kezzebûke' / 'fe-qul' (3. kelime)); muhatap geçişi 2MS → 2MP (ayet içi, 'qul' / 'rabbukum'); şahıs geçişi 1 → 3 (ayetler arası); edim geçişi haber → emir, şart (ayetler arası).",
)
