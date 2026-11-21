# sûre 6 blok 15 (6:62-67) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b15/say2.txt'
os.environ['OLC'] = '/home/claude/b15/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Gaybın anahtarları; karanlıklardan kurtaran' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 62: "Sonra gerçek mevlâları olan Allah'a döndürülürler. Bilin ki hüküm O'nundur; O, hesap görenlerin en çabuğudur.",
 63: "De ki: Kara ve denizin karanlıklarından sizi kim kurtarır? O'na yalvararak ve gizlice dua edersiniz: Bizi bundan kurtarırsa mutlaka şükredenlerden olacağız.",
 64: "De ki: Sizi ondan ve her sıkıntıdan Allah kurtarır; sonra siz ortak koşarsınız.",
 65: "De ki: O, üzerinize üstünüzden ya da ayaklarınızın altından bir azap göndermeye ya da sizi gruplar hâlinde karıştırıp kiminize kiminizin şiddetini tattırmaya kadirdir. Bak, âyetleri nasıl türlü türlü açıklıyoruz; belki anlarlar.",
 66: "Kavmin onu yalanladı; oysa o haktır. De ki: Ben sizin üzerinize vekil değilim.",
 67: "Her haberin bir karar vakti vardır; yakında bileceksiniz.",
}

T = {}
T[62] = ("'ruddû' 3MP (adsız; edilgen — naib-i faili zamir, 2. kelime); 'mevlâhumu' 3MP (adsız; gönderge 'ruddû' 2. kelime, 5. kelime); 'lehu', 've huve' 3MS (adsız; gönderge 'llâhi' 4. kelime — 8. ve 10. kelime)")
T[63] = ("muhatap 2MS (adsız; 'qul' — 1. kelime); muhatap 2MP (adsız; söz içi; 'yuneccîkum', 'ted'ûnehû' — 3. ve 8. kelime); 'yuneccîkum', 'ted'ûnehû', 'encânâ' 3MS (adsız; gönderge 'men' 2. kelime — 3., 8. ve 12. kelime); "
         "konuşan 1P (adsız; söz içi; 'encânâ', 'le-nekûnenne' — 12. ve 15. kelime)")
T[64] = ("muhatap 2MS (adsız; 'qul' — 1. kelime); 'yuneccîkum' 3MS (adsız; gönderge 'llâhu' 2. kelime, 3. kelime); muhatap 2MP (adsız; söz içi; 'yuneccîkum', 'entum', 'tuşrikûn' — 3., 9. ve 10. kelime); "
         "'minhâ' 3FS (adsız; gönderge 6:63 5. kelime, 4. kelime)")
T[65] = ("muhatap 2MS (adsız; 'qul', 'unzur' — 1. ve 22. kelime); 'huve', 'yeb'ase', 'yelbisekum', 've yuzîqa' 3MS (adsız; gönderge 6:64 2. kelime — 2., 6., 16. ve 18. kelime); "
         "muhatap 2MP (adsız; söz içi; ''aleykum', 'fevqikum', 'erculikum', 'yelbisekum', 'ba'dakum' — 7., 10., 14., 16. ve 19. kelime); konuşan 1P (adsız; 'nusarrifu' — 24. kelime); "
         "'le'allehum', 'yefqahûn' 3MP (adsız; gönderge 6:66 3. kelime — 26. ve 27. kelime)")
T[66] = ("'ve kezzebe' 3MS (fiil uyumu; 1. kelime — fail 3. kelime); 'bihî', 've huve' 3MS (adsız; gönderge 6:65 8. kelime — 2. ve 4. kelime); muhatap 2MS (adsız; 'qavmuke', 'qul' — 3. ve 6. kelime); "
         "konuşan 1S (adsız; söz içi; 'lestu' — 7. kelime); muhatap 2MP (adsız; söz içi; ''aleykum' — 8. kelime)")
T[67] = ("muhatap 2MP (adsız; 'ta'lemûn' — 5. kelime)")

D = {}
D[62] = ("◇ 'summe ruddû ile'llâhi mevlâhumu'l-haqq, elâ lehu'l-hukmu ve huve esra'u'l-hâsibîn' — "
 "'summe' + edilgen PERF 3MP I. bab + 3MP + 'ilâ' + lafız + 'mevlâ' + 3MP + belirli 'haqq' + 'alâ' + 'li' + 3MS + belirli 'hukm' + 've' + 'huve' + 'esra'' + belirli çoğul etken ortaç 'hâsib' "
 "(ölçüm edim haber, kip yok; 3MP 3 · 3MS 2; bab I. bab ×1). "
 "Allah lafzı 4. sırada (ölçüm allah z=1,14); Rab yok; ölçüm '{{1|esmâ مَوْلَى 5\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' — ölçüm MÜHÜRSÜZ ile uyuşuyor (e_el=? — karar bekliyor); "
 "'ilâ'llâhi mevlâhumu'l-haqq' — lafzın bedeli / sıfatı; kapalı listede kural yok, esma_el'e girmedi — kullanıcı kararına, tam okuma sonu (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=12 (n z=-0,04); ölçüm '{{1|EDİLGEN 1/1 fiil, pas z=5,38}}' — satır aynen; ölçüm '{{1|biçim DIKKAT}}' — satır aynen; "
 "ölçüm '{{1|fâsıla ٱلحسبين → ن, N sınıfı}}' — satır aynen (6:61 ن → 6:62 ن); ölçüm '{{1|simetri \\[3, 1, 8, 1\\]}}' — satır aynen; ölçüm '{{1|harf 49 → harf3 47, isaret 2}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen. "
 "Ölçüm kip yok; 'summe' (1.) CONJ; 'elâ lehu' (7.) kelimesindeki 'alâ' ATT; 've huve' (10.) kelimesindeki 've' REM (okuma). "
 + T[62] + " (okuma). "
 + cumle(say('say 6:62 3-6', "ile'llâhi mevlâhumu'l-haqq", True), say('dizi 6 62 2 6', "radde ilâ allâh mevlâ haqq"), say('say 6:62 8-9', "lehu'l-hukm")) + ' '
 "Ölçüm xref 10:30 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'summe' + PERF + 'ilâ' + lafız + izafet + belirli + 'alâ' + 'li' + belirli + 've' + 'huve' + izafet + belirli; "
 "D2 haber; D3 10:30 eşi; D4 3MP 3 · 3MS 2, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[62] + "; aktör yok (ölçüm); A2 gerçek mevlâya döndürülme; hükmün O'na ait olması; hesap görenlerin en çabuğu olma; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[63] = ("◇ 'qul men yuneccîkum min zulumâti'l-berri ve'l-bahri ted'ûnehû tedarru'an ve xufyeh, le-in encânâ min hâzihî le-nekûnenne mine'ş-şâkirîn' — "
 "IMPV 2MS I. bab + 'men' + IMPF 3MS II. bab + 2MP + 'min' + çoğul 'zulme' + belirli 'berr' + 've' + belirli 'bahr' + IMPF 2MP I. bab + 2MP + 3MS + nekre masdar 'tedarru'' + 've' + nekre 'xufye' + "
 "'le' + 'in' + PERF 3MS IV. bab + 1P + 'min' + 'hâ' + 'zâ' + 'le' + IMPF 1P I. bab + 'min' + belirli çoğul etken ortaç 'şâkir' "
 "(ölçüm edim soru, emir, şart, kip COND 1 · EMPH 3 · IMPV 1 · INTG 1; 1P 2 · 2MP 3 · 2MS 1 · 3MS 3; bab I. bab ×3 · II. bab ×1 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; ölçüm '{{2|esmâ بَرّ 6\\. sırada, ORTA konum, MÜHÜRSÜZ \\| شاكِر 17\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor, araç tanımı farkı (muhur_el hayır, ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'min zulumâti'l-berri ve'l-bahr', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); esma_el kaydı 'degil' — 'mine'ş-şâkirîn', kural 'çoğul insan göndergeli → degil' (insan topluluğu) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=17 (n z=0,49); ölçüm '{{2|biçim DIKKAT}}' — satır aynen; ölçüm '{{2|fâsıla ٱلشكرين → ن, N sınıfı}}' — satır aynen (6:62 ن → 6:63 ن); "
 "ölçüm '{{2|simetri \\[3, 2, 11, 1\\]}}' — satır aynen; ölçüm '{{2|harf 75 → harf3 71, isaret 4}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen; ölçüm '{{2|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 'le-in' (11. kelime); EMPH 3: 'le-in' (11. kelime), 'le-nekûnenne' (15. kelime; lâm ve tekit nûnu); IMPV 1: 'qul' (1. kelime); INTG 1: 'men' (2. kelime); 've'l-bahri' (7.) ve 've xufyeh' (10.) kelimelerindeki 've' CONJ; 'hâzihî' (14.) ATT (okuma). "
 "Kök ikilemesi (ölçüm) نجو ×2 ('yuneccîkum' 3. / 'encânâ' 12. kelime) (okuma). "
 + T[63] + " (okuma). "
 + cumle(say('say 6:63 15-17', "le-nekûnenne mine'ş-şâkirîn", True), say('dizi 6 63 11 17', "in encâ min zâ kâne min şâkir")) + ' '
 + cumle(say('say 6:63 5-7', "zulumâti'l-berri ve'l-bahr"), say('dizi 6 63 5 7', "zulme berr bahr")) + ' '
 "Ölçüm xref 10:22 (emsal olarak basıldı) ve okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıbı: 'zulme berr bahr' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'l-berri' / 've'l-bahri'; 'tedarru'an' / 've xufyeh' — ayetler arası: yok.",
 "◈K — K1 'l-bahri' (7. kelime).",
 "◈B — —",
 "◈D — D1 IMPV + 'men' + IMPF + 'min' + izafet + belirli + 've' + belirli + IMPF + nekre + 've' + nekre + 'le' + 'in' + PERF + 'min' + 'hâ' + 'zâ' + 'le' + IMPF + 'min' + belirli; "
 "D2 soru, emir, şart; COND ('le-in' 11. kelime), EMPH ('le-in' 11. kelime, 'le-nekûnenne' 15. kelime), IMPV ('qul' 1. kelime), INTG ('men' 2. kelime); D3 نجو ×2; 10:22 eşi; D4 1P 2 · 2MP 3 · 2MS 1 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[63] + "; aktör yok (ölçüm); A2 kara ve denizin karanlıklarından kurtarma sorusu; yalvararak ve gizlice dua; kurtarılırsa şükredenlerden olma sözü; "
 "A3 'men yuneccîkum min zulumâti'l-berri ve'l-bahri ted'ûnehû tedarru'an ve xufyeh, le-in encânâ min hâzihî le-nekûnenne mine'ş-şâkirîn' (söz içi, 2-17. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (17. kelime, ayet içi); şart → cevap (ayet içi; COND 'in' 11. kelime: 'le-in encânâ min hâzih' / 'le-nekûnenne mine'ş-şâkirîn' (15. kelime)); şahıs geçişi yok (ayetler arası); edim geçişi haber → soru, emir, şart (ayetler arası).",
)

D[64] = ("◇ 'quli'llâhu yuneccîkum minhâ ve min kulli kerbin summe entum tuşrikûn' — "
 "IMPV 2MS I. bab + lafız + IMPF 3MS II. bab + 2MP + 'min' + 3FS + 've' + 'min' + 'kull' + nekre 'kerb' + 'summe' + 'entum' + IMPF 2MP IV. bab "
 "(ölçüm edim emir, kip IMPV 1; 2MP 4 · 2MS 1 · 3FS 1 · 3MS 1; bab I. bab ×1 · II. bab ×1 · IV. bab ×1). "
 "Allah lafzı 2. sırada (ölçüm allah z=1,47); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=10 (n z=-0,26); ölçüm '{{3|fâsıla تشركون → ن, N sınıfı}}' — satır aynen (6:63 ن → 6:64 ن); "
 "ölçüm '{{3|simetri \\[3, 4, 8, 1\\]}}' — satır aynen; ölçüm '{{3|harf 37 → harf3 36, isaret 1}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm IMPV 1: 'qul' (1. kelime); 've min' (5.) kelimesindeki 've' CONJ; 'summe' (8.) CONJ (okuma). "
 + T[64] + " (okuma). "
 + cumle(say('say 6:64 2-3', "llâhu yuneccîkum", True), say('say 6:64 8-10', "summe entum tuşrikûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'yuneccîkum' / 'tuşrikûn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + lafız + IMPF + 'min' + 've' + 'min' + izafet + nekre + 'summe' + 'entum' + IMPF; "
 "D2 emir; IMPV ('qul' 1. kelime); D3 —; D4 2MP 4 · 2MS 1 · 3FS 1 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[64] + "; aktör yok (ölçüm); A2 kurtaranın Allah olması; her sıkıntıdan kurtarma; ardından ortak koşma; "
 "A3 'llâhu yuneccîkum minhâ ve min kulli kerbin summe entum tuşrikûn' (söz içi, 2-10. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (10. kelime, ayet içi); şahıs geçişi 3 → 2 (ayetler arası); edim geçişi soru, emir, şart → emir (ayetler arası).",
)

D[65] = ("◇ 'qul huve'l-qâdiru 'alâ en yeb'ase 'aleykum 'azâben min fevqikum ev min tahti erculikum ev yelbisekum şiya'an ve yuzîqa ba'dakum be'se ba'd, unzur keyfe nusarrifu'l-âyâti le'allehum yefqahûn' — "
 "IMPV 2MS I. bab + 'huve' + belirli etken ortaç 'qâdir' + ''alâ' + 'en' + IMPF 3MS I. bab + ''alâ' + 2MP + nekre ''azâb' + 'min' + 'fevq' + 2MP + 'ev' + 'min' + 'taht' + çoğul 'ricl' + 2MP + "
 "'ev' + IMPF 3MS I. bab + 2MP + nekre çoğul 'şî'a' + 've' + IMPF 3MS IV. bab + 'ba'd' + 2MP + 'be's' + nekre 'ba'd' + IMPV 2MS I. bab + 'keyf' + IMPF 1P II. bab + belirli çoğul 'âye' + 'le'alle' + 3MP + IMPF 3MP I. bab "
 "(ölçüm edim emir, kip IMPV 2; 1P 1 · 2MP 5 · 2MS 2 · 3MP 3 · 3MS 4; bab I. bab ×5 · II. bab ×1 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=27 (n z=1,55); ölçüm '{{4|fâsıla يفقهون → ن, N sınıfı}}' — satır aynen (6:64 ن → 6:65 ن); "
 "ölçüm '{{4|simetri \\[4, 2, 9, 1\\]}}' — satır aynen; ölçüm '{{4|harf 108 → harf3 105, isaret 3}}' — satır aynen; ölçüm '{{4|dış düğüm 2}}' — satır aynen. "
 "Ölçüm IMPV 2: 'qul' (1. kelime), 'unzur' (22. kelime); 'ev' (11., 15.) CONJ; 've yuzîqa' (18.) kelimesindeki 've' CONJ; 'en' (5.) SUB; 'le'allehum' (26.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) بعض ×2 ('ba'dakum' 19. / 'ba'd' 21. kelime) (okuma). "
 + T[65] + " (okuma). "
 + cumle(say('say 6:65 22-25', "unzur keyfe nusarrifu'l-âyât", True), say('dizi 6 65 22 25', "nazara keyf sarref âye")) + ' '
 + cumle(say('say 6:65 3-5', "l-qâdiru 'alâ en"), say('dizi 6 65 3 5', "qâdir 'alâ en"), say('say 6:65 9-14', "min fevqikum ev min tahti erculikum")) + ' '
 "Ölçüm xref okunmuş 2 ayet. "
 "Ölçüm nakarat3 kalıpları: 'nazara keyf sarref âye' süzgeç GEÇER, 'qâdir 'alâ en' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'min fevqikum' / 'min tahti erculikum' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'huve' + belirli + ''alâ' + 'en' + IMPF + ''alâ' + nekre + 'min' + izafet + 'ev' + 'min' + izafet + izafet + 'ev' + IMPF + nekre + 've' + IMPF + izafet + izafet + nekre + IMPV + 'keyf' + IMPF + belirli + 'le'alle' + IMPF; "
 "D2 emir; IMPV ('qul' 1. kelime, 'unzur' 22. kelime); D3 بعض ×2; D4 1P 1 · 2MP 5 · 2MS 2 · 3MP 3 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[65] + "; aktör yok (ölçüm); A2 üstten ya da alttan azap göndermeye kadir olma; gruplar hâlinde karıştırma; kiminin şiddetini kimine tattırma; âyetlerin türlü türlü açıklanması; "
 "A3 'huve'l-qâdiru 'alâ en yeb'ase 'aleykum 'azâben min fevqikum ev min tahti erculikum ev yelbisekum şiya'an ve yuzîqa ba'dakum be'se ba'd' (söz içi, 2-21. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (21. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi yok (ayetler arası); şahıs sayısında beraberlik (2MP 5 · 2MS 2 / 3MP 3 · 3MS 4 — ölçüm baskın 2).",
)

D[66] = ("◇ 've kezzebe bihî qavmuke ve huve'l-haqq, qul lestu 'aleykum bi-vekîl' — "
 "'ve' + PERF 3MS II. bab + 'bi' + 3MS + 'qavm' + 2MS + 've' + 'huve' + belirli 'haqq' + IMPV 2MS I. bab + PERF 1S I. bab + ''alâ' + 2MP + 'bi' + nekre 'vekîl' "
 "(ölçüm edim emir, kip IMPV 1; 1S 2 · 2MP 1 · 2MS 2 · 3MS 3; bab I. bab ×2 · II. bab ×1). "
 "Allah lafzı yok; Rab yok; ölçüm '{{5|esmâ وَكِيل 9\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor, araç tanımı farkı (muhur_el hayır, ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'lestu 'aleykum bi-vekîl', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=9 (n z=-0,36); ölçüm '{{5|fâsıla بوكيل → ل, ل sınıfı — KAFİYE KIRILMASI}}' — satır aynen (6:65 ن → 6:66 ل); "
 "ölçüm '{{5|harf 35 → harf3 32, isaret 3}}' — satır aynen; ölçüm '{{5|dış düğüm 0}}' — satır aynen. "
 "Ölçüm IMPV 1: 'qul' (6. kelime); 've kezzebe' (1.) kelimesindeki 've' REM; 've huve' (4.) kelimesindeki 've' CIRC (okuma). "
 + T[66] + " (okuma). "
 + cumle(say('say 6:66 8-9', "'aleykum bi-vekîl", True), say('say 6:66 4-5', "ve huve'l-haqq")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 've kezzebe' / 'l-haqq' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + PERF + 'bi' + izafet + 've' + 'huve' + belirli + IMPV + PERF + ''alâ' + 'bi' + nekre; "
 "D2 emir; IMPV ('qul' 6. kelime); D3 —; D4 1S 2 · 2MP 1 · 2MS 2 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[66] + "; aktör yok (ölçüm); A2 kavmin yalanlaması; onun hak olması; vekil olmama; "
 "A3 'lestu 'aleykum bi-vekîl' (söz içi, 7-9. kelime); "
 "A4 " + BOLUM + "; söz açılır (7. kelime); söz kapanır (9. kelime, ayet içi); şahıs geçişi 2 → 3 (ayetler arası); edim geçişi yok (ayetler arası); şahıs sayısında beraberlik (2MP 1 · 2MS 2 / 3MS 3 — ölçüm baskın 3).",
)

D[67] = ("◇ 'li-kulli nebe'in mustaqarr, ve sevfe ta'lemûn' — "
 "'li' + 'kull' + nekre 'nebe'' + nekre edilgen ortaç 'mustaqarr' + 've' + 'sevfe' + IMPF 2MP I. bab "
 "(ölçüm edim haber, kip FUT 1; 2MP 2; bab I. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=5 (n z=-0,79); ölçüm '{{6|fâsıla تعلمون → ن, N sınıfı}}' — satır aynen (6:66 ل → 6:67 ن); "
 "ölçüm '{{6|harf 24 → harf3 21, isaret 3}}' — satır aynen; ölçüm '{{6|dış düğüm 0}}' — satır aynen. "
 "Ölçüm FUT 1: 've sevfe' (4. kelime); 've sevfe' (4.) kelimesindeki 've' REM (okuma). "
 + T[67] + " (okuma). "
 + cumle(say('say 6:67 1-3', "li-kulli nebe'in mustaqarr", True), say('say 6:67 4-5', "ve sevfe ta'lemûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'li' + izafet + nekre + nekre + 've' + 'sevfe' + IMPF; "
 "D2 haber; FUT ('ve sevfe' 4. kelime); D3 —; D4 2MP 2, sahset ['2'], iltifât 0.",
 "◈A — A1 " + T[67] + "; aktör yok (ölçüm); A2 her haberin bir karar vakti olması; yakında bilme; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 2 (ayetler arası); edim geçişi emir → haber (ayetler arası); bölüm kapanışı.",
)
out = ['# ── blok 6:62-67 (2026-11-20) ──', 'MEAL15 = {']
for n in range(62, 68):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M15 = {']
for n in range(62, 68):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL15); M.update(M15)']
open('/home/claude/yamalar/metin_6_62_67.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
