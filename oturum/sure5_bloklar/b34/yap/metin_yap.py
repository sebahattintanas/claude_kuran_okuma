# blok 34 (5:111-115) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b34/say2.txt'
os.environ['OLC'] = '/home/claude/b34/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Elçilerin toplanması; İsâ'ya verilen nimetler; havariler ve sofra' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 111: "Hani havarilere vahyetmiştim: Bana ve elçime inanın. Dediler: İnandık; şahit ol ki biz teslim olanlarız.",
 112: "Hani havariler demişti: Ey Meryem oğlu Îsâ! Rabbin bize gökten bir sofra indirmeye güç yetirir mi? Demişti: Eğer inananlarsanız Allah'tan sakının.",
 113: "Dediler: İstiyoruz ki ondan yiyelim, kalplerimiz yatışsın, bize doğru söylediğini bilelim ve ona şahitlerden olalım.",
 114: "Meryem oğlu Îsâ dedi: Allah'ım, Rabbimiz! Bize gökten bir sofra indir; bizim için, öncekilerimiz ve sonrakilerimiz için bir bayram ve senden bir âyet olsun; bizi rızıklandır; sen rızık verenlerin en hayırlısısın.",
 115: "Allah dedi: Şüphesiz ben onu size indireceğim; bundan sonra sizden kim inkâr ederse, şüphesiz ben ona âlemlerden hiç kimseye etmeyeceğim bir azapla azap ederim.",
}

T = {}
T[111] = ("konuşan 1S (adsız; söz içi; 'evhaytu', 'bî', 've bi-rasûlî' — 2., 7. ve 8. kelime); muhatap 2MP (adsız; söz içi; 'âminû' — 6. kelime); "
          "'qâlû' faili 3MP (adsız; söz içi; gönderge 'l-havâriyyîne', 9. kelime); konuşan 1P (adsız; söz içi; 'âmennâ', 'bi-ennenâ' — 10. ve 12. kelime); muhatap 2MS (adsız; söz içi; 've'şhed' — 11. kelime)")
T[112] = ("'qâle' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'l-havâriyyûne' ('qâle' faili; çoğul; 3. kelime); 'yâ 'îse' (münadâ; adlı; söz içi; 4. kelime); "
          "'yestetî'u' 3MS (fiil uyumu; söz içi; 8. kelime — fail 9. kelime); 'rabbuke' ('yestetî'u' faili; söz içi; 9. kelime); muhatap 2MS (adsız; söz içi; 'rabbuke' — 9. kelime); "
          "'yunezzile' 3MS (adsız; söz içi; gönderge 'rabbuke', 11. kelime); konuşan 1P (adsız; söz içi; ''aleynâ' — 12. kelime); "
          "'qâle'ttequ' faili 3MS (adsız; gönderge 'yâ 'îse', 16. kelime); muhatap 2MP (adsız; söz içi; 'ttequ', 'kuntum' — 17. ve 20. kelime)")
T[113] = ("'qâlû' faili 3MP (adsız; gönderge havariler — 5:112, 1. kelime); konuşan 1P (adsız; söz içi; 'nurîdu', 'ne'kule', 'qulûbunâ', 've na'leme', 'sadaqtenâ', 've nekûne' — 2., 4., 7., 8., 11. ve 12. kelime); "
          "'minhâ' 3FS (adsız; söz içi; gönderge sofra — 5:112, 5. kelime); 've tatma'inne' 3FS (fiil uyumu; söz içi; 6. kelime — fail 7. kelime); 'qulûbunâ' ('tatma'inne' faili; çoğul; söz içi; 7. kelime); "
          "muhatap 2MS (adsız; söz içi; 'sadaqtenâ' — 11. kelime); ''aleyhâ' 3FS (adsız; söz içi; gönderge sofra — 5:112, 13. kelime)")
T[114] = ("'qâle' 3MS (fiil uyumu; 1. kelime — fail 2. kelime); ''îse'bnu' ('qâle' faili; adlı; 2. kelime); 'llâhumme' (münadâ; söz içi; 5. kelime); "
          "muhatap 2MS (adsız; söz içi; 'enzil', 'minke', 've'rzuqnâ', 've ente' — 7., 18., 19. ve 20. kelime); "
          "konuşan 1P (adsız; söz içi; 'rabbenâ', ''aleynâ', 'lenâ', 'li-evvelinâ', 've âxirinâ', 've'rzuqnâ' — 6., 8., 13., 15., 16. ve 19. kelime); 'tekûnu' 3FS (adsız; söz içi; gönderge 'mâ'ideten', 12. kelime)")
T[115] = ("'qâle' 3MS (fiil uyumu; 1. kelime — fail 2. kelime); 'llâhu' ('qâle' faili; lafız; 2. kelime); konuşan 1S (adsız; söz içi; 'innî', 'fe-innî', 'u'azzibuhû' — 3., 10., 11. ve 14. kelime); "
          "'munezziluhâ' 3FS (adsız; söz içi; gönderge sofra — 5:114, 4. kelime); muhatap 2MP (adsız; söz içi; ''aleykum', 'minkum' — 5. ve 9. kelime); "
          "'yekfur' 3MS (adsız; söz içi; gönderge 'fe-men', 7. kelime); 'u'azzibuhû' 3MS (adsız; söz içi; gönderge 'fe-men', 11. kelime); 'lâ u'azzibuhû' 3MS (adsız; söz içi; gönderge ''azâben', 14. kelime)")

D = {}
D[111] = ("◇ 've iz evhaytu ile'l-havâriyyîne en âminû bî ve bi-rasûlî qâlû âmennâ ve'şhed bi-ennenâ muslimûn' — "
 "'ve' + 'iz' + PERF 1S IV. bab + 'ilâ' + belirli çoğul 'havâriyy' + 'en' + IMPV 2MP IV. bab + 'bi' + 1S + 've' + 'bi' + 'rasûl' + 1S + PERF 3MP I. bab + PERF 1P IV. bab + 've' + IMPV 2MS I. bab + 'bi' + 'enne' + 1P + çoğul etken ortaç 'muslim' "
 "(ölçüm edim emir, kip IMPV 2; 1P 3 · 1S 4 · 2MP 2 · 2MS 1 · 3MP 2; bab I. bab ×2 · IV. bab ×3). "
 "Lafız yok; Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); aktör yok (ölçüm). "
 "Ölçüm yıldız yok; n=13 (n z=0,06); ölçüm '{{1|fâsıla مسلمون → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|simetri \\[3, 1, 5, 1\\]}}' — satır aynen; ölçüm '{{1|harf 65 → harf3 62, isaret 3}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 2: 'âminû' (6. kelime), 've'şhed' (11. kelime); 'iz' (1.) T, 've'şhed' (11.)'deki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) أمن ×2 ('âminû' 6. / 'âmennâ' 10. kelime) (okuma). "
 + T[111] + " (okuma). "
 + cumle(say('say 5:111 1-4 --on', "ve iz evhaytu ile'l-havâriyyîn", True), say('say 5:111 2-4', "evhaytu ile'l-havâriyyîn")) + ' '
 + cumle(say('say 5:111 5-8', "en âminû bî ve bi-rasûlî", True), say('say 5:111 6-8', "âminû bî ve bi-rasûlî")) + ' '
 + cumle(say('say 5:111 9-13', "qâlû âmennâ ve'şhed bi-ennenâ muslimûn", True), say('say 5:111 10-13', "âmennâ ve'şhed bi-ennenâ muslimûn"), say('say 5:111 11-13 --on', "ve'şhed bi-ennenâ muslimûn"), say('say 5:111 12-13', "bi-ennenâ muslimûn"), say('dizi 5 111 11 13', "şehide enne muslim")) + ' '
 "Ölçüm xref okunmuş 1 ayet. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'iz' + PERF + 'ilâ' + belirli + 'en' + IMPV + 'bi' + 've' + 'bi' + izafet + PERF + PERF + 've' + IMPV + 'bi' + 'enne'; "
 "D2 emir, IMPV ('âminû' 6. kelime, 've'şhed' 11. kelime); D3 أمن ×2; D4 1P 3 · 1S 4 · 2MP 2 · 2MS 1 · 3MP 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[111] + "; aktör yok (ölçüm); A2 havarilere vahyetmiştim; bana ve elçime inanın; inandık, teslim olanlarız; "
 "A3 söz sürüyor (1-13. kelime); 'âmennâ ve'şhed bi-ennenâ muslimûn' (iç söz, 10-13. kelime); "
 "A4 " + BOLUM + "; söz sürüyor (5:110'dan); söz kapanır (13. kelime, ayet içi); edim geçişi emir, nida → emir (ayetler arası).",
)

D[112] = ("◇ 'iz qâle'l-havâriyyûne yâ 'îse'bne meryeme hel yestetî'u rabbuke en yunezzile 'aleynâ mâ'ideten mine's-semâ'i qâle'ttequ'llâhe in kuntum mu'minîn' — "
 "'iz' + PERF 3MS I. bab + belirli çoğul 'havâriyy' + 'yâ' + adlı ''îsâ' + 'ibn' + adlı 'meryem' + 'hel' + IMPF 3MS X. bab + 'rabb' + 2MS + 'en' + IMPF 3MS II. bab + ''alâ' + 1P + nekre 'mâ'ide' + 'min' + belirli 'semâ'' + "
 "PERF 3MS I. bab + IMPV 2MP VIII. bab + lafız + 'in' + PERF 2MP I. bab + çoğul etken ortaç 'mu'min' "
 "(ölçüm edim soru, emir, nida, şart, kip COND 1 · IMPV 1 · INTG 1 · VOC 1; 1P 1 · 2MP 4 · 2MS 1 · 3MS 4; bab I. bab ×3 · II. bab ×1 · VIII. bab ×1 · X. bab ×1). "
 "Allah lafzı 18. sırada (ölçüm allah z=0,42); Rab 9. sırada (ölçüm rab z=0,69); ölçüm '{{2|esmâ مُؤْمِن 21\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET' (araç tanımı farkı; muhur_el hayır, ölçümle uyuşuyor) — esma_el kaydı 'degil' — 'in kuntum mu'minîn', kural 'çoğul insan göndergeli → degil' (inananlar) (okuma). "
 "Ölçüm aktör '{{2|adlı عِيسَى 4\\. sırada \\(kisi, rol meful\\+muhatap\\)}}' ve '{{2|adlı مَرْيَم 6\\. sırada \\(kisi, rol mecrur\\)}}' — satır aynen. "
 "Ölçüm yıldız yok; n=21 (n z=0,91); ölçüm '{{2|fâsıla مؤمنين → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|simetri \\[3, 4, 10, 1\\]}}' — satır aynen; ölçüm '{{2|harf 88 → harf3 85, isaret 3}}' — satır aynen; "
 "ölçüm '{{2|dış düğüm 4}}' — satır aynen; ölçüm '{{2|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm VOC 1: 'yâ' (4. kelime); INTG 1: 'hel' (7. kelime); IMPV 1: 'ttequ' (17. kelime); COND 1: 'in' (19. kelime); 'iz' (1.) T (okuma). "
 "Kök ikilemesi (ölçüm) قول ×2 ('qâle' 2. / 'qâle' 16. kelime) (okuma). "
 + T[112] + " (okuma). "
 + cumle(say('say 5:112 1-6', "iz qâle'l-havâriyyûne yâ 'îse'bne meryem", True), say('say 5:112 2-3', "qâle'l-havâriyyûn"), say('say 5:112 4-6', "yâ 'îse'bne meryem"), say('dizi 5 112 4 6', "'îsâ ibn meryem")) + ' '
 + cumle(say('say 5:112 7-15', "hel yestetî'u rabbuke en yunezzile 'aleynâ mâ'ideten mine's-semâ'", True), say('say 5:112 8-9', "yestetî'u rabbuk"), say('say 5:112 11-15', "yunezzile 'aleynâ mâ'ideten mine's-semâ'"),
         say('say 5:112 12-15', "'aleynâ mâ'ideten mine's-semâ'"), say('dizi 5 112 12 15', "'alâ mâ'ide min semâ'"), say('say 5:112 13-15', "mâ'ideten mine's-semâ'")) + ' '
 + cumle(say('say 5:112 16-21', "qâle'ttequ'llâhe in kuntum mu'minîn", True), say('say 5:112 17-21', "ttequ'llâhe in kuntum mu'minîn"), say('dizi 5 112 17 21', "itteqâ allâh in kâne mu'min"),
         say('say 5:112 17-19', "ttequ'llâhe in"), say('dizi 5 112 17 19', "itteqâ allâh in"), say('say 5:112 19-21', "in kuntum mu'minîn"), say('dizi 5 112 19 21', "in kâne mu'min")) + ' '
 "Ölçüm xref okunmuş 5 ayet. "
 "Ölçüm nakarat3 kalıpları: 'itteqâ allâh in kâne mu'min', ''alâ mâ'ide min semâ'', 'itteqâ allâh in', 'in kâne mu'min' ve ''îsâ ibn meryem' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K1 's-semâ'i' (15. kelime).",
 "◈B — —",
 "◈D — D1 'iz' + PERF + belirli + 'yâ' + adlı + izafet + adlı + 'hel' + IMPF + izafet + 'en' + IMPF + ''alâ' + nekre + 'min' + belirli + PERF + IMPV + lafız + 'in' + PERF; "
 "D2 soru, emir, nida, şart, VOC ('yâ' 4. kelime), INTG ('hel' 7. kelime), IMPV ('ttequ' 17. kelime), COND ('in' 19. kelime); D3 قول ×2; 3:52 ve 61:14 eşi; D4 1P 1 · 2MP 4 · 2MS 1 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[112] + "; aktör 'yâ 'îse', 'meryeme' (ölçüm); A2 havariler; Rabbin gökten bir sofra indirmeye güç yetirir mi; Allah'tan sakının; "
 "A3 'yâ 'îse'bne meryeme hel yestetî'u rabbuke en yunezzile 'aleynâ mâ'ideten mine's-semâ'i' (söz içi, 4-15. kelime); 'ttequ'llâhe in kuntum mu'minîn' (söz içi, 17-21. kelime); "
 "A4 " + BOLUM + "; söz açılır (4. kelime); söz kapanır (15. kelime, ayet içi); söz açılır (17. kelime); söz kapanır (21. kelime, ayet içi); edim geçişi emir → soru, emir, nida, şart (ayetler arası); şart → cevap (ayet içi; COND 'in' 19. kelime: 'in kuntum mu'minîn' / 'ttequ'llâhe' (17. kelime) — cevap mahzuf, delili önde).",
)

D[113] = ("◇ 'qâlû nurîdu en ne'kule minhâ ve tatma'inne qulûbunâ ve na'leme en qad sadaqtenâ ve nekûne 'aleyhâ mine'ş-şâhidîn' — "
 "PERF 3MP I. bab + IMPF 1P IV. bab + 'en' + IMPF 1P I. bab + 'min' + 3FS + 've' + IMPF 3FS IV. bab + çoğul 'qalb' + 1P + 've' + IMPF 1P I. bab + 'en' + 'qad' + PERF 2MS I. bab + 1P + 've' + IMPF 1P I. bab + ''alâ' + 3FS + 'min' + belirli çoğul etken ortaç 'şâhid' "
 "(ölçüm edim haber, kip CERT 1; 1P 6 · 2MS 2 · 3FS 3 · 3MP 2; bab I. bab ×5 · IV. bab ×2). "
 "Lafız yok; Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); aktör yok (ölçüm). "
 "Ölçüm yıldız yok; n=15 (n z=0,27); ölçüm '{{3|fâsıla ٱلشهدين → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|simetri \\[3, 9, 13, 1\\]}}' — satır aynen; ölçüm '{{3|harf 66 → harf3 65, isaret 1}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (10. kelime) (okuma). "
 + T[113] + " (okuma). "
 + cumle(say('say 5:113 1-5', "qâlû nurîdu en ne'kule minhâ", True), say('say 5:113 2-5', "nurîdu en ne'kule minhâ")) + ' '
 + cumle(say('say 5:113 6-7 --on', "ve tatma'inne qulûbunâ", True)) + ' '
 + cumle(say('say 5:113 8-11 --on', "ve na'leme en qad sadaqtenâ", True), say('say 5:113 10-11', "qad sadaqtenâ")) + ' '
 + cumle(say('say 5:113 12-15 --on', "ve nekûne 'aleyhâ mine'ş-şâhidîn", True), say('say 5:113 14-15', "mine'ş-şâhidîn")) + ' '
 "Ölçüm xref yok ('xref üçü de boş'). "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B3 'qulûbunâ' (7. kelime).",
 "◈D — D1 PERF + IMPF + 'en' + IMPF + 'min' + 've' + IMPF + izafet + 've' + IMPF + 'en' + 'qad' + PERF + 've' + IMPF + ''alâ' + 'min' + belirli; "
 "D2 haber, CERT ('qad' 10. kelime); D3 —; D4 1P 6 · 2MS 2 · 3FS 3 · 3MP 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[113] + "; aktör yok (ölçüm); A2 ondan yiyelim; kalplerimiz yatışsın; doğru söylediğini bilelim; şahitlerden olalım; "
 "A3 'nurîdu en ne'kule minhâ ve tatma'inne qulûbunâ ve na'leme en qad sadaqtenâ ve nekûne 'aleyhâ mine'ş-şâhidîn' (söz içi, 2-15. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (15. kelime, ayet içi); edim geçişi soru, emir, nida, şart → haber (ayetler arası).",
)

D[114] = ("◇ 'qâle 'îse'bnu meryeme'llâhumme rabbenâ enzil 'aleynâ mâ'ideten mine's-semâ'i tekûnu lenâ 'îden li-evvelinâ ve âxirinâ ve âyeten minke ve'rzuqnâ ve ente xayru'r-râziqîn' — "
 "PERF 3MS I. bab + adlı ''îsâ' + 'ibn' + adlı 'meryem' + 'allâhumme' + 'rabb' + 1P + IMPV 2MS IV. bab + ''alâ' + 1P + nekre 'mâ'ide' + 'min' + belirli 'semâ'' + IMPF 3FS I. bab + 'li' + 1P + nekre ''îd' + "
 "'li' + 'evvel' + 1P + 've' + 'âxir' + 1P + 've' + nekre 'âye' + 'min' + 2MS + 've' + IMPV 2MS I. bab + 1P + 've' + 'ente' + 'xayr' + belirli çoğul etken ortaç 'râziq' "
 "(ölçüm edim emir, nida, kip IMPV 2 · VOC 1; 1P 6 · 2MS 4 · 3FS 1 · 3MS 1; bab I. bab ×3 · IV. bab ×1). "
 "Lafız yok; Rab 6. sırada (ölçüm rab z=0,65); ölçüm '{{4|esmâ آخِر 16\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor) — esma_el kaydı 'degil' — 've âxirinâ', kural 'esmâ adı esmâ dışı göndergeyle → degil' (sonrakilerimiz) (okuma). "
 "Ölçüm aktör '{{4|adlı عِيسَى 2\\. sırada \\(kisi, rol fail\\+konusan\\)}}', '{{4|adlı مَرْيَم 4\\. sırada \\(kisi, rol mecrur\\)}}' ve '{{4|adlı \\S+ 5\\. sırada \\(diger, rol meful\\)}}' — satır aynen. "
 "Ölçüm yıldız yok; n=22 (n z=1,02); ölçüm '{{4|fâsıla ٱلرزقين → ن, N sınıfı}}' — satır aynen; ölçüm '{{4|simetri \\[3, 2, 8, 1\\]}}' — satır aynen; ölçüm '{{4|harf 102 → harf3 98, isaret 4}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm VOC 1: 'llâhumme' (5. kelime — mîm eki); IMPV 2: 'enzil' (7. kelime), 've'rzuqnâ' (19. kelime); 've ente' (20.)'deki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) رزق ×2 ('ve'rzuqnâ' 19. / 'r-râziqîn' 22. kelime) (okuma). "
 + T[114] + " (okuma). "
 + cumle(say('say 5:114 1-4', "qâle 'îse'bnu meryem", True), say('say 5:114 2-4', "'îse'bnu meryem"), say('dizi 5 114 2 4', "'îsâ ibn meryem")) + ' '
 + cumle(say('say 5:114 5-6', "llâhumme rabbenâ", True)) + ' '
 + cumle(say('say 5:114 7-11', "enzil 'aleynâ mâ'ideten mine's-semâ'", True), say('say 5:114 8-11', "'aleynâ mâ'ideten mine's-semâ'"), say('dizi 5 114 8 11', "'alâ mâ'ide min semâ'")) + ' '
 + cumle(say('say 5:114 12-18', "tekûnu lenâ 'îden li-evvelinâ ve âxirinâ ve âyeten mink", True), say('say 5:114 12-14', "tekûnu lenâ 'îden"), say('say 5:114 15-16', "li-evvelinâ ve âxirinâ"), say('say 5:114 17-18 --on', "ve âyeten mink")) + ' '
 + cumle(say('say 5:114 20-22 --on', "ve ente xayru'r-râziqîn", True), say('say 5:114 21-22', "xayru'r-râziqîn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: ''alâ mâ'ide min semâ'' süzgeç GEÇER, ''îsâ ibn meryem' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'li-evvelinâ' / 've âxirinâ' — ayetler arası: yok.",
 "◈K — K1 's-semâ'i' (11. kelime).",
 "◈B — —",
 "◈D — D1 PERF + adlı + izafet + adlı + 'allâhumme' + izafet + IMPV + ''alâ' + nekre + 'min' + belirli + IMPF + 'li' + nekre + 'li' + izafet + 've' + izafet + 've' + nekre + 'min' + 've' + IMPV + 've' + 'ente' + izafet + belirli; "
 "D2 emir, nida, VOC ('llâhumme' 5. kelime), IMPV ('enzil' 7. kelime, 've'rzuqnâ' 19. kelime); D3 رزق ×2; D4 1P 6 · 2MS 4 · 3FS 1 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[114] + "; aktör ''îse'bnu', 'meryeme', 'llâhumme' (ölçüm); A2 Allah'ım, Rabbimiz; gökten bir sofra indir; bayram ve âyet olsun; rızık verenlerin en hayırlısı; "
 "A3 'llâhumme rabbenâ enzil 'aleynâ mâ'ideten mine's-semâ'i tekûnu lenâ 'îden li-evvelinâ ve âxirinâ ve âyeten minke ve'rzuqnâ ve ente xayru'r-râziqîn' (söz içi, 5-22. kelime); "
 "A4 " + BOLUM + "; söz açılır (5. kelime); söz kapanır (22. kelime, ayet içi); edim geçişi haber → emir, nida (ayetler arası).",
)

D[115] = ("◇ 'qâle'llâhu innî munezziluhâ 'aleykum fe-men yekfur ba'du minkum fe-innî u'azzibuhû 'azâben lâ u'azzibuhû ehaden mine'l-'âlemîn' — "
 "PERF 3MS I. bab + lafız + 'inne' + 1S + etken ortaç 'munezzil' + 3FS + ''alâ' + 2MP + 'fe' + 'men' + IMPF 3MS I. bab + 'ba'd' + 'min' + 2MP + 'fe' + 'inne' + 1S + IMPF 1S II. bab + 3MS + nekre ''azâb' + 'lâ' + IMPF 1S II. bab + 3MS + nekre 'ehad' + 'min' + belirli çoğul ''âlem' "
 "(ölçüm edim şart, kip COND 1 · NEG 1; 1S 4 · 2MP 2 · 3FS 1 · 3MS 4; bab I. bab ×2 · II. bab ×2). "
 "Allah lafzı 2. sırada (ölçüm allah z=0,65); Rab yok; ölçüm '{{5|esmâ أَحَد 15\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET' (araç tanımı farkı; muhur_el hayır, ölçümle uyuşuyor) — esma_el kaydı 'degil' — 'lâ u'azzibuhû ehaden', kural 'olumsuz nekre ehad → degil' (hiç kimse) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız yok; n=17 (n z=0,49); ölçüm '{{5|fâsıla ٱلعلمين → ن, N sınıfı}}' — satır aynen; ölçüm '{{5|mm2: \\[11, عذب}}' — satır aynen; ölçüm '{{5|sayı işareti أَحَد}}' — satır aynen; "
 "ölçüm '{{5|simetri \\[3, 5, 9, 1\\]}}' — satır aynen; ölçüm '{{5|harf 74 → harf3 69, isaret 5}}' — satır aynen; ölçüm '{{5|dış düğüm 0}}' — satır aynen. "
 "Ölçüm COND 1: 'fe-men' (6. kelime); NEG 1: 'lâ' (13. kelime); 'fe-men' (6.)'daki 'fe' REM, 'fe-innî' (10.)'daki 'fe' RSLT, 'ba'du' (8.) T (okuma). "
 "Kök ikilemesi (ölçüm) عذب ×3 ('u'azzibuhû' 11., ''azâben' 12. ve 'u'azzibuhû' 14. kelime) (okuma). "
 + T[115] + " (okuma). "
 + cumle(say('say 5:115 1-5', "qâle'llâhu innî munezziluhâ 'aleykum", True), say('say 5:115 1-3', "qâle'llâhu innî"), say('dizi 5 115 1 3', "qâle allâh inne"), say('say 5:115 3-5', "innî munezziluhâ 'aleykum")) + ' '
 + cumle(say('say 5:115 6-9 --on', "fe-men yekfur ba'du minkum", True), say('say 5:115 6-8 --on', "fe-men yekfur ba'd"), say('dizi 5 115 6 8', "fe-men kefera ba'd")) + ' '
 + cumle(say('say 5:115 10-12 --on', "fe-innî u'azzibuhû 'azâben", True), say('say 5:115 13-17', "lâ u'azzibuhû ehaden mine'l-'âlemîn"), say('say 5:115 15-17', "ehaden mine'l-'âlemîn"), say('dizi 5 115 15 17', "ehad min 'âlem")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: 'qâle allâh inne', 'fe-men kefera ba'd' ve 'ehad min 'âlem' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + lafız + 'inne' + izafet + ''alâ' + 'fe' + 'men' + IMPF + 'ba'd' + 'min' + 'fe' + 'inne' + IMPF + nekre + 'lâ' + IMPF + nekre + 'min' + belirli; "
 "D2 şart, COND ('fe-men' 6. kelime), NEG ('lâ' 13. kelime); D3 عذب ×3; D4 1S 4 · 2MP 2 · 3FS 1 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[115] + "; aktör yok (ölçüm); A2 onu size indireceğim; sizden kim inkâr ederse; hiç kimseye etmeyeceğim bir azap; "
 "A3 'innî munezziluhâ 'aleykum fe-men yekfur ba'du minkum fe-innî u'azzibuhû 'azâben lâ u'azzibuhû ehaden mine'l-'âlemîn' (söz içi, 3-17. kelime); "
 "A4 " + BOLUM + "; söz açılır (3. kelime); söz kapanır (17. kelime, ayet içi); bölüm kapanışı; edim geçişi emir, nida → şart (ayetler arası); şart → cevap (ayet içi; COND 'men' 6. kelime: 'fe-men yekfur' / 'fe-innî u'azzibuhû' (10. kelime)).",
)

out = ['# ── blok 5:111-115 (2026-11-18) ──', 'MEAL34 = {']
for n in range(111, 116):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M34 = {']
for n in range(111, 116):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL34); M.update(M34)']
open('/home/claude/yamalar/metin_5_111_115.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
