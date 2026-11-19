# sûre 6 blok 6 (6:25-28) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b06/say2.txt'
os.environ['OLC'] = '/home/claude/b06/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Yalanlayanların toplanma sahnesi; dünya hayatı oyun' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'



MEAL = {
 25: "Onlardan seni dinleyen vardır. Kalplerine, onu anlamalarına engel örtüler, kulaklarına da ağırlık koyduk. Her âyeti görseler ona inanmazlar. Hatta sana geldiklerinde seninle tartışırlar; inkâr edenler: Bu öncekilerin masallarından başka bir şey değil, derler.",
 26: "Onlar ondan alıkoyarlar ve ondan uzaklaşırlar. Ancak kendilerini helâk ederler de farkında olmazlar.",
 27: "Ateşin üzerinde durdurulduklarında bir görsen! Dediler: Keşke geri döndürülsek de Rabbimizin âyetlerini yalanlamasak ve inananlardan olsak.",
 28: "Hayır, önceden gizledikleri şey kendilerine açığa çıktı. Geri döndürülselerdi, mutlaka kendilerine yasaklanan şeye dönerlerdi. Şüphesiz onlar elbette yalancılardır.",
}

T = {}
T[25] = ("'minhum' 3MP (adsız; gönderge 6:24 7. kelime, 1. kelime); 'yestemi'u' 3MS (adsız; gönderge 'men', 3. kelime); muhatap 2MS (adsız; 'ileyke', 'câ'ûke', 'yucâdilûneke' — 4., 23. ve 24. kelime); "
         "konuşan 1P (adsız; 'ce'alnâ' — 5. kelime); 'qulûbihim', 'yefqahûhu', 'âzânihim', 'yerev', 'yu'minû', 'câ'ûke', 'yucâdilûneke' 3MP (adsız; gönderge 'minhum' — 7., 10., 12., 15., 19., 23. ve 24. kelime); "
         "'yefqahûhu' zamiri 3MS (adsız; gönderge 'yestemi'u' ile dinlenen söz, 10. kelime); 'bihâ' 3FS (adsız; gönderge 'âyetin', 20. kelime); 'yeqûlu' 3MS (fiil uyumu; 25. kelime — fail 26. kelime); "
         "'keferû' 3MP (adsız; gönderge 'llezîne', 27. kelime)")
T[26] = ("'ve hum', 'yenhevne', 'yen'evne', 'yuhlikûne', 'enfusehum', 'yeş'urûn' 3MP (adsız; gönderge 6:25 26. kelime — 1., 2., 4., 7., 9. ve 11. kelime); "
         "''anhu', ''anhu' 3MS (adsız; gönderge 6:25 10. kelimedeki zamir — 3. ve 5. kelime)")
T[27] = ("muhatap 2MS (adsız; 'terâ' — 2. kelime); 'vuqifû' 3MP (adsız; edilgen; naib-i faili zamir — gönderge 6:26 1. kelime, 4. kelime); 'fe-qâlû' 3MP (adsız; gönderge 6:26 1. kelime, 7. kelime); "
         "'nuraddu' 1P (adsız; söz içi; edilgen; naib-i faili konuşan zamir, 9. kelime); konuşan 1P (adsız; söz içi; 'leytenâ', 'nukezzibe', 'rabbinâ', 'nekûne' — 8., 11., 13. ve 14. kelime)")
T[28] = ("'bedâ' 3MS (fiil uyumu; 2. kelime — fail 4. kelime); 'lehum', 'kânû', 'yuxfûne' 3MP (adsız; gönderge 6:27 7. kelime — 3., 5. ve 6. kelime); "
         "'ruddû' 3MP (adsız; edilgen; naib-i faili zamir — gönderge 6:27 7. kelime, 10. kelime); ''âdû' 3MP (adsız; gönderge 6:27 7. kelime, 11. kelime); "
         "'nuhû' 3MP (adsız; edilgen; naib-i faili zamir — gönderge 6:27 7. kelime, 13. kelime); ''anhu' 3MS (adsız; gönderge 'li-mâ', 14. kelime); 've innehum' 3MP (adsız; gönderge 6:27 7. kelime, 15. kelime)")

D = {}
D[25] = ("◇ 've minhum men yestemi'u ileyke ve ce'alnâ 'alâ qulûbihim ekinneten en yefqahûhu ve fî âzânihim vaqrâ, ve in yerev kulle âyetin lâ yu'minû bihâ, hattâ izâ câ'ûke yucâdilûneke yeqûlu'llezîne keferû in hâzâ illâ esâtîru'l-evvelîn' — "
 "'ve' + 'min' + 3MP + 'men' + IMPF 3MS VIII. bab + 'ilâ' + 2MS + 've' + PERF 1P I. bab + ''alâ' + çoğul 'qalb' + 3MP + nekre 'ekinne' + 'en' + IMPF 3MP I. bab + 3MS + 've' + 'fî' + çoğul 'uzun' + 3MP + nekre 'vaqr' + "
 "'ve' + 'in' + IMPF 3MP I. bab + 'kull' + nekre 'âye' + 'lâ' + IMPF 3MP IV. bab + 'bi' + 3FS + 'hattâ' + 'izâ' + PERF 3MP I. bab + 2MS + IMPF 3MP III. bab + 2MS + IMPF 3MS I. bab + 'ellezî' + PERF 3MP I. bab + 'in' + 'hâ' + 'zâ' + 'illâ' + çoğul 'esâtîr' + belirli çoğul 'evvel' "
 "(ölçüm edim şart, kip COND 1 · NEG 2 · RES 1; 1P 2 · 2MS 3 · 3FS 1 · 3MP 15 · 3MS 3; bab I. bab ×6 · III. bab ×1 · IV. bab ×1 · VIII. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür EVET ton denge' — ölçüm esmâ yok ile uyuşmuyor (liste farkı: esma_kayit son3'teki 'evvel' ölçüm esmâ satırında yok; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'esâtîru'l-evvelîn', kural 'çoğul insan göndergeli → degil' (insan topluluğu) (okuma). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=32 (n z=2,08); ölçüm '{{1|fâsıla ٱلأولين → ن, N sınıfı}}' — satır aynen (6:24 ن → 6:25 ن); "
 "ölçüm '{{1|simetri \\[6, 18, 26, 2\\]}}' — satır aynen; ölçüm '{{1|harf 141 → harf3 133, isaret 8}}' — satır aynen; ölçüm '{{1|dış düğüm 3}}' — satır aynen. "
 "Ölçüm COND 1: 've in' (14. kelime); NEG 2: 'lâ' (18. kelime), 'in' (28. kelime); RES 1: 'illâ' (30. kelime); 've minhum' (1.) ve 've in' (14.) kelimelerindeki 've' REM; 've ce'alnâ' (5.) ve 've fî' (11.) kelimelerindeki 've' CONJ (okuma). "
 + T[25] + " (okuma). "
 + cumle(say('say 6:25 1-4', "ve minhum men yestemi'u ileyk", True), say('say 6:25 9-10', "en yefqahûhu"), say('say 6:25 11-13', "ve fî âzânihim vaqrâ"), say('say 6:25 12-13', "âzânihim vaqrâ")) + ' '
 + cumle(say('say 6:25 14-20', "ve in yerev kulle âyetin lâ yu'minû bihâ", True), say('say 6:25 18-20', "lâ yu'minû bihâ"), say('say 6:25 21-23', "hattâ izâ câ'ûke"), say('dizi 6 25 21 23', "hattâ izâ câ'e")) + ' '
 + cumle(say('say 6:25 25-30', "yeqûlu'llezîne keferû in hâzâ illâ", True), say('dizi 6 25 25 30', "qâle ellezî kefera in zâ illâ"), say('say 6:25 31-32', "esâtîru'l-evvelîn")) + ' '
 "Ölçüm xref 17:46 (emsal olarak basıldı) ve okunmuş 1 ayet ve okunmamış 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'qâle ellezî kefera in zâ illâ' süzgeç GEÇER; 'hattâ izâ câ'e' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'yestemi'u' (3. kelime), 'qulûbihim' (7. kelime); B4 —.",
 "◈D — D1 've' + 'min' + 'men' + IMPF + 'ilâ' + 've' + PERF + ''alâ' + izafet + nekre + 'en' + IMPF + 've' + 'fî' + izafet + nekre + 've' + 'in' + IMPF + 'kull' + nekre + 'lâ' + IMPF + 'bi' + 'hattâ' + 'izâ' + PERF + IMPF + IMPF + 'ellezî' + PERF + 'in' + 'hâ' + 'zâ' + 'illâ' + izafet + belirli; "
 "D2 şart; COND ('ve in' 14. kelime), NEG ('lâ' 18. kelime, 'in' 28. kelime), RES ('illâ' 30. kelime); D3 —; 17:46 eşi; D4 1P 2 · 2MS 3 · 3FS 1 · 3MP 15 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[25] + "; aktör yok (ölçüm); A2 dinleyip anlamayanlar; kalplere örtü, kulaklara ağırlık; her âyete inanmama; tartışma ve 'öncekilerin masalları' sözü; "
 "A3 'in hâzâ illâ esâtîru'l-evvelîn' (söz içi, 28-32. kelime); "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; COND 'in' 14. kelime: 'in yerev kulle âyetin' / 'lâ yu'minû bihâ' (18. kelime)); söz açılır (28. kelime); söz kapanır (32. kelime, ayet içi); "
 "edim geçişi emir → şart (ayetler arası).",
)

D[26] = ("◇ 've hum yenhevne 'anhu ve yen'evne 'anhu ve in yuhlikûne illâ enfusehum ve mâ yeş'urûn' — "
 "'ve' + 'hum' + IMPF 3MP I. bab + ''an' + 3MS + 've' + IMPF 3MP I. bab + ''an' + 3MS + 've' + 'in' + IMPF 3MP IV. bab + 'illâ' + 'nefs' + 3MP + 've' + 'mâ' + IMPF 3MP I. bab "
 "(ölçüm edim haber, kip NEG 2 · RES 1; 3MP 10 · 3MS 2; bab I. bab ×3 · IV. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=11 (n z=-0,15); ölçüm '{{2|fâsıla يشعرون → ن, N sınıfı}}' — satır aynen (6:25 ن → 6:26 ن); "
 "ölçüm '{{2|simetri \\[3, 1, 6, 1\\]}}' — satır aynen; ölçüm '{{2|harf 48 → harf3 47, isaret 1}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 2: 'in' (6. kelime), 'mâ' (10. kelime); RES 1: 'illâ' (8. kelime); 've hum' (1.) kelimesindeki 've' CIRC; 've in' (6.) kelimesindeki 've' REM (okuma). "
 + T[26] + " (okuma). "
 + cumle(say('say 6:26 1-5', "ve hum yenhevne 'anhu ve yen'evne 'anh", True), say('say 6:26 6-9', "ve in yuhlikûne illâ enfusehum")) + ' '
 + cumle(say('say 6:26 8-11', "illâ enfusehum ve mâ yeş'urûn", True), say('dizi 6 26 8 11', "illâ nefs mâ şa'ara"), say('say 6:26 10-11', "ve mâ yeş'urûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'illâ nefs mâ şa'ara' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'hum' + IMPF + ''an' + 've' + IMPF + ''an' + 've' + 'in' + IMPF + 'illâ' + izafet + 've' + 'mâ' + IMPF; "
 "D2 haber; NEG ('in' 6. kelime, 'mâ' 10. kelime), RES ('illâ' 8. kelime); D3 —; D4 3MP 10 · 3MS 2, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[26] + "; aktör yok (ölçüm); A2 alıkoyma ve uzaklaşma; ancak kendilerini helâk etme; farkında olmama; "
 "A3 —; "
 "A4 " + BOLUM + "; edim geçişi şart → haber (ayetler arası).",
)

D[27] = ("◇ 've lev terâ iz vuqifû 'ale'n-nâri fe-qâlû yâ leytenâ nuraddu ve lâ nukezzibe bi-âyâti rabbinâ ve nekûne mine'l-mu'minîn' — "
 "'ve' + 'lev' + IMPF 2MS I. bab + 'iz' + edilgen PERF 3MP I. bab + ''alâ' + belirli 'nâr' + 'fe' + PERF 3MP I. bab + 'yâ' + 'leyte' + 1P + edilgen IMPF 1P I. bab + 've' + 'lâ' + IMPF 1P II. bab + 'bi' + çoğul 'âye' + 'rabb' + 1P + 've' + IMPF 1P I. bab + 'min' + belirli çoğul etken ortaç 'mu'min' "
 "(ölçüm edim nida, şart, kip COND 1 · NEG 1 · VOC 1; 1P 5 · 2MS 1 · 3MP 4; bab I. bab ×5 · II. bab ×1). "
 "Lafız yok; Rab 13. sırada (ölçüm rab z=1,01); ölçüm '{{3|esmâ مُؤْمِن 16\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'mine'l-mu'minîn', kural 'çoğul insan göndergeli → degil' (insan topluluğu) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=16 (n z=0,38); ölçüm '{{3|EDİLGEN 2/6 fiil, pas z=1,57}}' — satır aynen; "
 "ölçüm '{{3|fâsıla ٱلمؤمنين → ن, N sınıfı}}' — satır aynen (6:26 ن → 6:27 ن); ölçüm '{{3|simetri \\[3, 1, 8, 1\\]}}' — satır aynen; ölçüm '{{3|harf 69 → harf3 67, isaret 2}}' — satır aynen; "
 "ölçüm '{{3|dış düğüm 2}}' — satır aynen; ölçüm '{{3|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 've lev' (1. kelime); NEG 1: 'lâ' (10. kelime); VOC 1: 'yâ' (8. kelime); 've lev' (1.), 've lâ' (10.) ve 've nekûne' (14.) kelimelerindeki 've' CONJ; 'fe-qâlû' (7.) kelimesindeki 'fe' CONJ; 'leytenâ' (8.) ACC (okuma). "
 + T[27] + " (okuma). "
 + cumle(say('say 6:27 1-5', "ve lev terâ iz vuqifû 'ale", True), say('say 6:27 4-6', "vuqifû 'ale'n-nâr"), say('say 6:27 7-9', "fe-qâlû yâ leytenâ nuradd")) + ' '
 + cumle(say('say 6:27 10-13', "ve lâ nukezzibe bi-âyâti rabbinâ", True), say('say 6:27 12-13', "bi-âyâti rabbinâ"), say('say 6:27 13-15', "rabbinâ ve nekûne mine"), say('dizi 6 27 13 15', "rabb kâne min"), say('say 6:27 14-16', "ve nekûne mine'l-mu'minîn")) + ' '
 "Ölçüm xref 6:4 (basılmış), 36:46 (basılmış) ve okunmamış 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'lev raâ iz vuqife 'alâ' süzgeç GEÇER; 'rabb kâne min' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'nukezzibe' / 'l-mu'minîn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'lev' + IMPF + 'iz' + PERF + ''alâ' + belirli + 'fe' + PERF + 'yâ' + 'leyte' + IMPF + 've' + 'lâ' + IMPF + 'bi' + izafet + 've' + IMPF + 'min' + belirli; "
 "D2 nida, şart; COND ('ve lev' 1. kelime), NEG ('lâ' 10. kelime), VOC ('yâ' 8. kelime); D3 —; D4 1P 5 · 2MS 1 · 3MP 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[27] + "; aktör yok (ölçüm); A2 ateşin üzerinde durdurulma; geri döndürülme temennisi; yalanlamama ve inananlardan olma dileği; "
 "A3 'yâ leytenâ nuraddu ve lâ nukezzibe bi-âyâti rabbinâ ve nekûne mine'l-mu'minîn' (söz içi, 8-16. kelime); "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; COND 'lev' 1. kelime: 'lev terâ iz vuqifû' — cevap hazif (mealde ünlem)); söz açılır (8. kelime); söz kapanır (16. kelime, ayet içi); şahıs geçişi 3 → 1 (ayetler arası); edim geçişi haber → nida (ayetler arası).",
)

D[28] = ("◇ 'bel bedâ lehum mâ kânû yuxfûne min qabl, ve lev ruddû le-'âdû li-mâ nuhû 'anhu ve innehum le-kâzibûn' — "
 "'bel' + PERF 3MS I. bab + 'li' + 3MP + 'mâ' + PERF 3MP I. bab + IMPF 3MP IV. bab + 'min' + 'qabl' + 've' + 'lev' + edilgen PERF 3MP I. bab + 'le' + PERF 3MP I. bab + 'li' + 'mâ' + edilgen PERF 3MP I. bab + ''an' + 3MS + 've' + 'inne' + 3MP + 'le' + çoğul etken ortaç 'kâzib' "
 "(ölçüm edim şart, kip COND 1 · EMPH 2; 3MP 12 · 3MS 2; bab I. bab ×5 · IV. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=16 (n z=0,38); ölçüm '{{4|EDİLGEN 2/6 fiil, pas z=1,57}}' — satır aynen; "
 "ölçüm '{{4|fâsıla لكذبون → ن, N sınıfı}}' — satır aynen (6:27 ن → 6:28 ن); ölçüm '{{4|simetri \\[4, 1, 12, 1\\]}}' — satır aynen; ölçüm '{{4|harf 64 → harf3 59, isaret 5}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm COND 1: 've lev' (9. kelime); EMPH 2: 'le-'âdû' (11. kelime), 'le-kâzibûn' (16. kelime); 've lev' (9.) ve 've innehum' (15.) kelimelerindeki 've' REM; 'bel' (1.) RET; 'innehum' (15.) ACC (okuma). "
 + T[28] + " (okuma). "
 + cumle(say('say 6:28 1-8', "bel bedâ lehum mâ kânû yuxfûne min qabl", True), say('say 6:28 4-6', "mâ kânû yuxfûn")) + ' '
 + cumle(say('say 6:28 9-14', "ve lev ruddû le-'âdû li-mâ nuhû 'anh", True), say('say 6:28 12-14', "li-mâ nuhû 'anh"), say('say 6:28 15-16', "ve innehum le-kâzibûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'bedâ' / 'yuxfûne' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'bel' + PERF + 'li' + 'mâ' + PERF + IMPF + 'min' + 'qabl' + 've' + 'lev' + PERF + 'le' + PERF + 'li' + 'mâ' + PERF + ''an' + 've' + 'inne' + 'le' + çoğul; "
 "D2 şart; COND ('ve lev' 9. kelime), EMPH ('le-'âdû' 11. kelime, 'le-kâzibûn' 16. kelime); D3 —; D4 3MP 12 · 3MS 2, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[28] + "; aktör yok (ölçüm); A2 gizlenenin açığa çıkması; geri döndürülseler yasaklanana dönmeleri; yalancılık; "
 "A3 —; "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; COND 'lev' 9. kelime: 'lev ruddû' / ''âdû' (11. kelime)); şart → cevap kapsamı dışı: 've innehum le-kâzibûn' REM ile yeni cümle, tekit 'le' (16. kelime); şahıs geçişi 1 → 3 (ayetler arası); edim geçişi nida → şart (ayetler arası).",
)
out = ['# ── blok 6:25-28 (2026-11-19) ──', 'MEAL6 = {']
for n in range(25, 29):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M6 = {']
for n in range(25, 29):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL6); M.update(M6)']
open('/home/claude/yamalar/metin_6_25_28.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
