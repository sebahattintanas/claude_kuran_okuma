# sûre 6 blok 25 (6:104-108) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b25/say2.txt'
os.environ['OLC'] = '/home/claude/b25/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Basiretler; yeminleri ve şeytanlar' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 104: "Andolsun, size Rabbinizden basiretler geldi. Kim görürse kendi lehinedir; kim kör olursa kendi aleyhinedir. Ben sizin üzerinize koruyucu değilim.",
 105: "Böylece âyetleri türlü türlü açıklıyoruz, sen ders almışsın desinler diye ve onu bilen bir kavim için açıklayalım diye.",
 106: "Rabbinden sana vahyolunana uy; O'ndan başka ilah yoktur. Ortak koşanlardan yüz çevir.",
 107: "Allah dileseydi ortak koşmazlardı. Seni onların üzerine koruyucu kılmadık; sen onlar üzerine vekil de değilsin.",
 108: "Allah'ı bırakıp dua ettiklerine sövmeyin; yoksa onlar da bilgisizce, haddi aşarak Allah'a söverler. Böylece her ümmete kendi amelini süsledik. Sonra dönüşleri Rablerinedir; yapmakta olduklarını onlara haber verecektir.",
}

T = {}
T[104] = ("'câ'ekum' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); muhatap 2MP (adsız; 'câ'ekum', 'rabbikum', ''aleykum' — 2., 5. ve 14. kelime); "
          "'ebsara' 3MS (adsız; gönderge 'fe-men' 6. kelime, 7. kelime); 'fe-li-nefsihî' 3MS eki (adsız; gönderge 'fe-men' 6. kelime, 8. kelime); ''amiye' 3MS (adsız; gönderge 've men' 9. kelime, 10. kelime); "
          "'aleyhâ' 3FS (adsız; gönderge 'fe-li-nefsihî' 8. kelime, 11. kelime); konuşan 1S (adsız; 'ene' — 13. kelime)")
T[105] = ("konuşan 1P (adsız; 'nusarrifu', 've li-nubeyyinehû' — 2. ve 6. kelime); 've li-yeqûlû' 3MP (adsız; tartışmalı — 4. kelime); 'derasta' muhatap 2MS (adsız; söz içi — 5. kelime); "
          "'ve li-nubeyyinehû' 3MS eki (adsız; tartışmalı; gönderge 'l-âyâti' 3. kelime, 6. kelime); 'ya'lemûn' 3MP (adsız; gönderge 'li-qavmin' 7. kelime, 8. kelime)")
T[106] = ("muhatap 2MS (adsız; 'ttebi', 'ileyke', 'rabbike', 've a'rid' — 1., 4., 6. ve 11. kelime); 'ûhiye' 3MS (fiil uyumu; 3. kelime — edilgen; naib-i faili 'mâ' (2. kelime)); "
          "'huve' 3MS (adsız; gönderge 'rabbike' 6. kelime, 10. kelime)")
T[107] = ("'şâ'e' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'eşrakû' 3MP (adsız; gönderge 6:106 13. kelime, 5. kelime); ''aleyhim' 3MP (adsız; gönderge 6:106 13. kelime, 8. kelime); "
          "''aleyhim' 3MP (adsız; gönderge 6:106 13. kelime, 12. kelime); konuşan 1P (adsız; 'ce'alnâke' — 7. kelime); muhatap 2MS (adsız; 'ce'alnâke', 'ente' — 7. ve 11. kelime)")
T[108] = ("muhatap 2MP (adsız; 'tesubbu' — 2. kelime); 'yed'ûne' 3MP (adsız; gönderge 6:107 5. kelime, 4. kelime); 'fe-yesubbu' 3MP (adsız; gönderge 6:107 5. kelime, 8. kelime); "
          "konuşan 1P (adsız; 'zeyyennâ' — 14. kelime); ''amelehum' 3MP eki (adsız; gönderge 'ummetin' 16. kelime, 17. kelime); "
          "'rabbihim', 'merci'uhum', 'kânû', 'ya'melûn' 3MP (adsız; tartışmalı; gönderge 'ummetin' 16. kelime — 20., 21., 24. ve 25. kelime); "
          "'fe-yunebbi'uhum' 3MS (adsız; gönderge 'rabbihim' 20. kelime, 22. kelime); 'fe-yunebbi'uhum' 3MP eki (adsız; tartışmalı; gönderge 'ummetin' 16. kelime, 22. kelime)")

D = {}
D[104] = ("◇ 'qad câ'ekum besâ'iru min rabbikum fe-men ebsara fe-li-nefsihî ve men 'amiye fe-'aleyhâ ve mâ ene 'aleykum bi-hafîz' — "
 "'qad' + PERF 3MS I. bab + 2MP + çoğul 'basîre' + 'min' + 'rabb' + 2MP + 'fe' + 'men' + PERF 3MS IV. bab + 'fe' + 'li' + 'nefs' + 3MS + 've' + 'men' + PERF 3MS I. bab + 'fe' + ''alâ' + 3FS + "
 "'ve' + 'mâ' + 'ene' + ''alâ' + 2MP + 'bi' + nekre etken ortaç 'hafîz' "
 "(ölçüm edim şart, kip CERT 1 · COND 2 · NEG 1; 1S 1 · 2MP 3 · 3FS 1 · 3MS 4; bab I. bab ×2 · IV. bab ×1). "
 "Allah lafzı yok; Rab 5. sırada (ölçüm rab z=1,10); ölçüm '{{1|esmâ حَفِيظ 15\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor, araç tanımı farkı (tam okuma sonu); "
 "esma_el kaydı 'degil' — 've mâ ene 'aleykum bi-hafîz', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=15 (n z=0,27); ölçüm '{{1|fâsıla بحفيظ → ظ, ظ sınıfı}}' — satır aynen (6:103 ر → 6:104 ظ); "
 "ölçüm '{{1|simetri \\[3, 4, 9, 1\\]}}' — satır aynen; ölçüm '{{1|harf 65 → harf3 59, isaret 6}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (1. kelime); COND 2: 'fe-men' (6.) ve 've men' (9. kelime); NEG 1: 've mâ' (12. kelime); 'fe-men' (6.) kelimesindeki 'fe' ve 've mâ' (12.) kelimesindeki 've' REM; 've men' (9.) kelimesindeki 've' CONJ; "
 "'fe-li-nefsihî' (8.) ve 'fe-'aleyhâ' (11.) kelimelerindeki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) بصر ×2 ('besâ'iru' 3. / 'ebsara' 7. kelime) (okuma). "
 + T[104] + " (okuma). "
 "Ölçüm xref yok; ölçüm bağ yok (esit2, nakarat3, xref üçü de boş). "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'ebsara' / ''amiye' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'besâ'iru' (3. kelime), 'ebsara' (7. kelime); B4 —.",
 "◈D — D1 'qad' + PERF + 'basîre' + 'min' + izafet + 'fe' + 'men' + PERF + 'fe' + 'li' + izafet + 've' + 'men' + PERF + 'fe' + ''alâ' + 've' + 'mâ' + 'ene' + ''alâ' + 'bi' + nekre; "
 "D2 şart; CERT ('qad' 1. kelime), COND ('fe-men' 6. kelime, 've men' 9. kelime), NEG ('ve mâ' 12. kelime); D3 بصر ×2; D4 1S 1 · 2MP 3 · 3FS 1 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[104] + "; aktör yok (ölçüm); A2 Rabden gelen basiretler; gören kendi lehine, kör olan kendi aleyhine; konuşanın koruyucu olmayışı; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi haber → şart (ayetler arası); şart → cevap (ayet içi; COND 'men' 6. kelime: 'fe-men ebsara' / 'fe-li-nefsihî' (8. kelime)); "
 "şart → cevap (ayet içi; COND 'men' 9. kelime: 've men ''amiye' / 'fe-'aleyhâ' (11. kelime)); bölüm açılışı.",
)

D[105] = ("◇ 've kezâlike nusarrifu'l-âyâti ve li-yeqûlû derasta ve li-nubeyyinehû li-qavmin ya'lemûn' — "
 "'ve' + 'ke' + 'zâlike' + IMPF 1P II. bab + belirli çoğul 'âye' + 've' + 'li' + IMPF 3MP I. bab + 3MP + PERF 2MS I. bab + 2MS + 've' + 'li' + IMPF 1P II. bab + 3MS + 'li' + nekre 'qavm' + IMPF 3MP I. bab + 3MP "
 "(ölçüm edim haber, kip yok; 1P 2 · 2MS 2 · 3MP 4 · 3MS 1; bab I. bab ×3 · II. bab ×2). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=8 (n z=-0,47); ölçüm '{{2|fâsıla يعلمون → ن, N sınıfı}}' — satır aynen (6:104 ظ → 6:105 ن); "
 "ölçüm '{{2|harf 47 → harf3 44, isaret 3}}' — satır aynen; ölçüm '{{2|dış düğüm 1}}' — satır aynen. "
 "Ölçüm kip yok; 've kezâlike' (1.), 've li-yeqûlû' (4.) ve 've li-nubeyyinehû' (6.) kelimelerindeki 've' CONJ; 've li-yeqûlû' (4.) ve 've li-nubeyyinehû' (6.) kelimelerindeki 'li' PRP (okuma). "
 + T[105] + " (okuma). "
 + cumle(say('say 6:105 6-8', "ve li-nubeyyinehû li-qavmin ya'lemûn", True)) + ' ' +
 "Ölçüm xref okunmuş 1 ayet. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'ke' + 'zâlike' + IMPF + belirli + 've' + 'li' + IMPF + PERF + 've' + 'li' + IMPF + 'li' + nekre + IMPF; "
 "D2 haber; D3 —; D4 1P 2 · 2MS 2 · 3MP 4 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[105] + "; aktör yok (ölçüm); A2 âyetlerin türlü türlü açıklanması; 'ders almışsın' sözü; bilen bir kavim için açıklama; "
 "A3 'derasta' (söz içi, 5-5. kelime); "
 "A4 " + BOLUM + "; söz açılır (5. kelime); söz kapanır (5. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi şart → haber (ayetler arası).",
)

D[106] = ("◇ 'ittebi' mâ ûhiye ileyke min rabbike lâ ilâhe illâ huve ve a'rid 'ani'l-muşrikîn' — "
 "IMPV 2MS VIII. bab + 'mâ' + PERF 3MS IV. bab edilgen + 'ilâ' + 2MS + 'min' + 'rabb' + 2MS + 'lâ' + 'ilâh' + 'illâ' + 'huve' + 've' + IMPV 2MS IV. bab + ''an' + belirli çoğul etken ortaç 'muşrik' "
 "(ölçüm edim emir, kip IMPV 2 · NEG 1, biçim ISTISNA; 2MS 4 · 3MS 2; bab IV. bab ×2 · VIII. bab ×1). "
 "Allah lafzı yok; Rab 6. sırada (ölçüm rab z=1,32); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=13 (n z=0,06); ölçüm '{{3|EDİLGEN 1/3 fiil, pas z=1,57}}' — satır aynen; ölçüm '{{3|fâsıla ٱلمشركين → ن, N sınıfı}}' — satır aynen (6:105 ن → 6:106 ن); "
 "ölçüm '{{3|simetri \\[4, 2, 7, 1\\]}}' — satır aynen; ölçüm '{{3|harf 46 → harf3 44, isaret 2}}' — satır aynen; ölçüm '{{3|dış düğüm 2}}' — satır aynen. "
 "Ölçüm IMPV 2: 'ttebi' (1. kelime) ve 've a'rid' (11. kelime); NEG 1: 'lâ' (7. kelime); biçim ISTISNA ('illâ' 9. kelime); 've a'rid' (11.) kelimesindeki 've' CONJ (okuma). "
 + T[106] + " (okuma). "
 + cumle(say('say 6:106 1-6', "ittebi' mâ ûhiye ileyke min rabbik", True), say('dizi 6 106 1 6', 'ittebe mâ evhâ ilâ min rabb')) + ' ' + cumle(say('say 6:106 6-10', 'rabbike lâ ilâhe illâ huve', True), say('dizi 6 106 6 10', 'rabb lâ ilâh illâ _')) + ' ' +
 "Ölçüm xref 33:2 (emsal olarak basıldı) ve okunmamış 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'rabb lâ ilâh illâ _' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'mâ' + PERF + 'ilâ' + 'min' + izafet + 'lâ' + 'ilâh' + 'illâ' + 'huve' + 've' + IMPV + ''an' + belirli; "
 "D2 emir; IMPV ('ttebi' 1. kelime, 've a'rid' 11. kelime), NEG ('lâ' 7. kelime); D3 33:2 eşi; D4 2MS 4 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[106] + "; aktör yok (ölçüm); A2 Rabden vahyolunana uyma emri; O'ndan başka ilah olmaması; müşriklerden yüz çevirme emri; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 2 (ayetler arası); edim geçişi haber → emir (ayetler arası).",
)

D[107] = ("◇ 've lev şâ'e'llâhu mâ eşrakû ve mâ ce'alnâke 'aleyhim hafîzan ve mâ ente 'aleyhim bi-vekîl' — "
 "'ve' + 'lev' + PERF 3MS I. bab + lafız + 'mâ' + PERF 3MP IV. bab + 3MP + 've' + 'mâ' + PERF 1P I. bab + 1P + 2MS + ''alâ' + 3MP + nekre etken ortaç 'hafîz' + 've' + 'mâ' + 'ente' + ''alâ' + 3MP + 'bi' + nekre 'vekîl' "
 "(ölçüm edim şart, kip COND 1 · NEG 3; 1P 2 · 2MS 2 · 3MP 4 · 3MS 1; bab I. bab ×2 · IV. bab ×1). "
 "Allah lafzı 3. sırada (ölçüm allah z=1,01); Rab yok; ölçüm '{{4|esmâ حَفِيظ 9\\. sırada, ORTA konum, MÜHÜRSÜZ \\| وَكِيل 13\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET (ÇİFT) ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor, araç tanımı farkı (tam okuma sonu); "
 "esma_el kaydı 'degil' — 've mâ ce'alnâke 'aleyhim hafîz' ve 've mâ ente 'aleyhim bi-vekîl', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=13 (n z=0,06); ölçüm '{{4|fâsıla بوكيل → ل, ل sınıfı — KAFİYE KIRILMASI}}' — satır aynen (6:106 ن → 6:107 ل); "
 "ölçüm '{{4|simetri \\[3, 4, 8, 1\\]}}' — satır aynen; ölçüm '{{4|harf 57 → harf3 52, isaret 5}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm COND 1: 've lev' (1. kelime); NEG 3: 'mâ' (4.), 've mâ' (6.) ve 've mâ' (10. kelime); 've lev' (1.) kelimesindeki 've' REM; 've mâ' (6. ve 10.) kelimelerindeki 've' CONJ (okuma). "
 + T[107] + " (okuma). "
 + cumle(say('say 6:107 1-4', "ve lev şâ'e'llâhu mâ", True), say('dizi 6 107 1 4', "lev şâ'e allâh mâ")) + ' ' + cumle(say('say 6:107 2-5', "şâ'e'llâhu mâ eşrakû", True), say('dizi 6 107 2 5', "şâ'e allâh mâ eşrake")) + ' ' + cumle(say('say 6:107 2-4', "şâ'e'llâhu mâ", True), say('dizi 6 107 2 4', "şâ'e allâh mâ")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: 'lev şâ'e allâh mâ' süzgeç GEÇER, 'şâ'e allâh mâ eşrake' süzgeç GEÇER, 'şâ'e allâh mâ' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'lev' + PERF + lafız + 'mâ' + PERF + 've' + 'mâ' + PERF + ''alâ' + nekre + 've' + 'mâ' + 'ente' + ''alâ' + 'bi' + nekre; "
 "D2 şart; COND ('ve lev' 1. kelime), NEG ('mâ' 4. kelime, 've mâ' 6. kelime, 've mâ' 10. kelime); D3 —; D4 1P 2 · 2MS 2 · 3MP 4 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[107] + "; aktör yok (ölçüm); A2 Allah dileseydi ortak koşmayacakları; muhatabın onlar üzerine koruyucu ve vekil olmayışı; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi emir → şart (ayetler arası); şart → cevap (ayet içi; COND 'lev' 1. kelime: 've lev şâ'e'llâhu' / 'mâ eşrakû' (4. kelime)).",
)

D[108] = ("◇ 've lâ tesubbu'llezîne yed'ûne min dûni'llâhi fe-yesubbu'llâhe 'advan bi-ğayri 'ilmin kezâlike zeyyennâ li-kulli ummetin 'amelehum summe ilâ rabbihim merci'uhum fe-yunebbi'uhum bi-mâ kânû ya'melûn' — "
 "'ve' + 'lâ' + IMPF 2MP I. bab + 2MP + 'ellezîne' + IMPF 3MP I. bab + 3MP + 'min' + 'dûn' + lafız + 'fe' + IMPF 3MP I. bab + 3MP + lafız + nekre ''adv' + 'bi' + 'ğayr' + nekre ''ilm' + 'ke' + 'zâlike' + PERF 1P II. bab + 1P + "
 "'li' + 'kull' + nekre 'umme' + ''amel' + 3MP + 'summe' + 'ilâ' + 'rabb' + 3MP + 'merci'' + 3MP + 'fe' + IMPF 3MS II. bab + 3MP + 'bi' + 'mâ' + PERF 3MP I. bab + 3MP + IMPF 3MP I. bab + 3MP "
 "(ölçüm edim yasak, kip PRO 1, biçim NEHY; 1P 2 · 2MP 2 · 3MP 12 · 3MS 1; bab I. bab ×5 · II. bab ×2). "
 "Allah lafzı 7. ve 9. sırada (ölçüm allah z=1,07); Rab 20. sırada (ölçüm rab z=0,53); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=25 (n z=1,34); ölçüm '{{5|fâsıla يعملون → ن, N sınıfı}}' — satır aynen (6:107 ل → 6:108 ن); "
 "ölçüm '{{5|harf 109 → harf3 103, isaret 6}}' — satır aynen; ölçüm '{{5|dış düğüm 1}}' — satır aynen; ölçüm '{{5|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm PRO 1: 've lâ' (1. kelime), biçim NEHY; 've lâ' (1.) kelimesindeki 've' REM; 'fe-yesubbu' (8.) kelimesindeki 'fe' CAUS; 'fe-yunebbi'uhum' (22.) kelimesindeki 'fe' REM; 'summe' (18.) CONJ (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhi' 7. / 'llâhe' 9. kelime), سبب ×2 ('tesubbu' 2. / 'fe-yesubbu' 8. kelime), عمل ×2 (''amelehum' 17. / 'ya'melûn' 25. kelime) (okuma). "
 + T[108] + " (okuma). "
 + cumle(say('say 6:108 18-24', "summe ilâ rabbihim merci'uhum fe-yunebbi'uhum bi-mâ kânû", True), say('dizi 6 108 18 24', "summe ilâ rabb merci' nebbe'e mâ kâne"), say('dizi 6 108 18 25', "summe ilâ rabb merci' nebbe'e mâ kâne 'amile")) + ' ' + cumle(say('say 6:108 3-7', "llezîne yed'ûne min dûni'llâh", True), say('dizi 6 108 3 7', "ellezî de'â min dûn allâh")) + ' ' + cumle(say('say 6:108 4-7', "yed'ûne min dûni'llâh", True), say('dizi 6 108 4 7', "de'â min dûn allâh")) + ' ' + cumle(say('say 6:108 5-7', "min dûni'llâh", True), say('dizi 6 108 5 7', 'min dûn allâh')) + ' ' + cumle(say('say 6:108 22-25', "fe-yunebbi'uhum bi-mâ kânû ya'melûn", True)) + ' ' + cumle(say('say 6:108 22-24', "fe-yunebbi'uhum bi-mâ kânû", True)) + ' ' + cumle(say('say 6:108 18-20', 'summe ilâ rabbihim', True), say('dizi 6 108 18 20', 'summe ilâ rabb')) + ' ' + cumle(say('say 6:108 23-25', "bi-mâ kânû ya'melûn", True)) + ' ' +
 "Ölçüm xref 39:7 (emsal olarak basıldı) ve okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıpları: 'summe ilâ rabb merci' nebbe'e mâ kâne' süzgeç GEÇER, 'ellezî de'â min dûn allâh' süzgeç GEÇER, 'de'â min dûn allâh' süzgeç GEÇER, 'nebbe'e mâ kâne 'amile' süzgeç GEÇER, 'min dûn allâh' süzgeç GEÇER, 'nebbe'e mâ kâne' süzgeç GEÇER, 'summe ilâ rabb' süzgeç GEÇER, 'bi-mâ kâne 'amile' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'lâ' + IMPF + 'ellezîne' + IMPF + 'min' + izafet + lafız + 'fe' + IMPF + lafız + nekre + 'bi' + 'ğayr' + nekre + 'ke' + 'zâlike' + PERF + 'li' + 'kull' + nekre + izafet + 'summe' + 'ilâ' + izafet + izafet + 'fe' + IMPF + 'bi' + 'mâ' + PERF + IMPF; "
 "D2 yasak; PRO ('ve lâ' 1. kelime); D3 أله ×2, سبب ×2, عمل ×2; 39:7 eşi; D4 1P 2 · 2MP 2 · 3MP 12 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[108] + "; aktör yok (ölçüm); A2 Allah'ı bırakıp dua edilenlere sövme yasağı; karşılığında Allah'a sövülmesi; her ümmete amelinin süslenmesi; dönüşün Rablerine oluşu ve yapılanların haber verilmesi; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi şart → yasak (ayetler arası); nehy → cevap (ayet içi; PRO 'lâ' 1. kelime: 've lâ tesubbu'llezîne' / 'fe-yesubbu'llâhe' (8. kelime)).",
)
out = ['# ── blok 6:104-108 (2026-11-22) ──', 'MEAL25 = {']
for n in range(104, 109):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M25 = {']
for n in range(104, 109):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL25); M.update(M25)']
open('/home/claude/yamalar/metin_6_104_108.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
