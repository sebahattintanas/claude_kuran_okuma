# sûre 6 blok 39 (6:158-160) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b39/say2.txt'
os.environ['OLC'] = '/home/claude/b39/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Bekledikleri; dosdoğru din; yeryüzünün halifeleri' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 158: "Onlar, kendilerine meleklerin gelmesinden ya da Rabbinin gelmesinden ya da Rabbinin âyetlerinden bazısının gelmesinden başka bir şey mi bekliyorlar? Rabbinin âyetlerinden bazısı geldiği gün, önceden inanmamış ya da imanında bir hayır kazanmamış olan hiçbir cana imanı fayda vermez. De ki: Bekleyin; şüphesiz biz de bekleyenleriz.",
 159: "Dinlerini parçalayıp bölük bölük olanlara gelince, sen hiçbir şeyde onlardan değilsin. Onların işi ancak Allah'adır; sonra O, yapmakta olduklarını onlara haber verecektir.",
 160: "Kim bir iyilikle gelirse ona onun on misli vardır. Kim de bir kötülükle gelirse, yalnızca onun dengiyle karşılık görür; onlara zulmedilmez.",
}

T = {}
T[158] = ("'yenzurûne' 3MP (adsız; gönderge 6:157 27. kelime, 2. kelime); 'te'tiyehumu' 3FS (fiil uyumu; 5. kelime — fail 6. kelime); 'te'tiyehumu' 3MP eki (adsız; gönderge 6:157 27. kelime, 5. kelime); "
          "'ye'tiye' 3MS (fiil uyumu; 8. kelime — fail 9. kelime); muhatap 2MS eki (adsız; 'rabbuke', 'rabbik', 'rabbike' — 9., 14. ve 19. kelime); 'ye'tiye' 3MS (fiil uyumu; 11. kelime — fail 12. kelime); "
          "'ye'tî' 3MS (fiil uyumu; 16. kelime — fail 17. kelime); 'yenfe'u' 3MS (fiil uyumu; 21. kelime — fail 23. kelime); 'îmânuhâ' 3FS eki (adsız; gönderge 'nefsen' 22. kelime, 23. kelime); "
          "'tekun', 'âmenet', 'kesebet' 3FS (adsız; gönderge 'nefsen' 22. kelime — 25., 26. ve 30. kelime); 'îmânihâ' 3FS eki (adsız; gönderge 'nefsen' 22. kelime, 32. kelime); "
          "muhatap 2MS (adsız; 'quli' — 34. kelime); muhatap 2MP (adsız; söz içi; 'ntezirû' — 35. kelime); konuşan 1P eki (adsız; söz içi; 'innâ' — 36. kelime)")
T[159] = ("'ferraqû', 'kânû' 3MP (adsız; gönderge 'llezîne' 2. kelime — 3. ve 5. kelime); 'dînehum' 3MP eki (adsız; gönderge 'llezîne' 2. kelime, 4. kelime); muhatap 2MS (adsız; 'leste' — 7. kelime); "
          "'minhum', 'emruhum', 'yunebbi'uhum' 3MP eki (adsız; gönderge 'llezîne' 2. kelime — 8., 12. ve 16. kelime); 'yunebbi'uhum' 3MS (adsız; gönderge 'llâhi' 14. kelime, 16. kelime); "
          "'kânû', 'yef'alûn' 3MP (adsız; gönderge 'llezîne' 2. kelime — 18. ve 19. kelime)")
T[160] = ("'câ'e' 3MS (adsız; gönderge 'men' 1. kelime, 2. kelime); 'fe-lehû' 3MS (adsız; gönderge 'men' 1. kelime, 4. kelime); 'emsâlihâ' 3FS eki (adsız; gönderge 'l-haseneti' 3. kelime, 6. kelime); "
          "'câ'e' 3MS (adsız; gönderge 'men' 7. kelime, 8. kelime); 'yuczâ' 3MS (adsız; edilgen, naib-i faili 'men' 7. kelime, 11. kelime); 'mislehâ' 3FS eki (adsız; gönderge 's-seyyi'eti' 9. kelime, 13. kelime); "
          "'hum' 3MP (adsız; tartışmalı; gönderge 'men' 1. kelime, 14. kelime); 'yuzlemûn' 3MP (adsız; edilgen, naib-i faili 'hum' 14. kelime, 16. kelime)")

D = {}
D[158] = ("◇ 'hel yenzurûne illâ en te'tiyehumu'l-melâ'iketu ev ye'tiye rabbuke ev ye'tiye ba'du âyâti rabbik, yevme ye'tî ba'du âyâti rabbike lâ yenfe'u nefsen îmânuhâ lem tekun âmenet min qablu ev kesebet fî îmânihâ xayrâ, quli'ntezirû innâ muntezirûn' — "
 "'hel' + IMPF 3MP I. bab + 'illâ' + 'en' + IMPF 3FS I. bab + 3MP + belirli çoğul 'melek' + 'ev' + IMPF 3MS I. bab + 'rabb' + 2MS + 'ev' + IMPF 3MS I. bab + 'ba'd' + çoğul 'âye' + 'rabb' + 2MS + "
 "'yevm' + IMPF 3MS I. bab + 'ba'd' + çoğul 'âye' + 'rabb' + 2MS + 'lâ' + IMPF 3MS I. bab + nekre 'nefs' + masdar 'îmân' + 3FS + 'lem' + IMPF 3FS I. bab + PERF 3FS IV. bab + 'min' + 'qabl' + 'ev' + PERF 3FS I. bab + 'fî' + masdar 'îmân' + 3FS + nekre 'xayr' + "
 "IMPV 2MS I. bab + IMPV 2MP VIII. bab + 'inne' + 1P + çoğul etken ortaç 'muntezir' "
 "(ölçüm edim soru, emir, kip IMPV 2 · INTG 1 · NEG 2 · RES 1; 1P 1 · 2MP 2 · 2MS 4 · 3FS 6 · 3MP 3 · 3MS 4; bab I. bab ×9 · IV. bab ×1 · VIII. bab ×1). "
 "Allah lafzı yok; Rab 9., 14. ve 19. sırada (ölçüm rab z=1,41); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=37 (n z=2,61); ölçüm '{{1|fâsıla منتظرون → ن, N sınıfı}}' — satır aynen (6:157 ن → 6:158 ن); "
 "ölçüm '{{1|simetri \\[5, 9, 14, 1\\]}}' — satır aynen; ölçüm '{{1|harf 140 → harf3 136, isaret 4}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen. "
 "Ölçüm IMPV 2: 'quli' (34.) ve 'ntezirû' (35. kelime); INTG 1: 'hel' (1. kelime); NEG 2: 'lâ' (20.) ve 'lem' (24. kelime); RES 1: 'illâ' (3. kelime); ölçüm biçim HASR ('illâ' 3. kelime); "
 "'ev' (7., 10. ve 29.) CONJ; 'en' (4.) SUB; 'innâ' (36.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) أتي ×4 ('te'tiyehumu' 5. / 'ye'tiye' 8. / 'ye'tiye' 11. / 'ye'tî' 16. kelime), أمن ×3 ('îmânuhâ' 23. / 'âmenet' 26. / 'îmânihâ' 32. kelime), أيي ×2 ('âyâti' 13. / 'âyâti' 18. kelime), بعض ×2 ('ba'du' 12. / 'ba'du' 17. kelime), "
 "ربب ×3 ('rabbuke' 9. / 'rabbik' 14. / 'rabbike' 19. kelime), نظر ×3 ('yenzurûne' 2. / 'ntezirû' 35. / 'muntezirûn' 37. kelime) (okuma). "
 + T[158] + " (okuma). "
 + cumle(say('say 6:158 1-8', "hel yenzurûne illâ en te'tiyehumu'l-melâ'iketu ev ye'tiye", True), say('dizi 6 158 1 8', "hel nazara illâ en etâ melek ev etâ")) + ' '
 + say('say 6:158 1-3', "hel yenzurûne illâ", True) + " (--medde 5 ayet: 'illâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). "
 + say('say 6:158 2-3', "yenzurûne illâ", True) + " (--medde 8 ayet: 'illâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). " +
 "Ölçüm xref 16:33 (emsal olarak basıldı) ve okunmuş 1 ayet. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K2 'yevme' (15. kelime).",
 "◈B — —",
 "◈D — D1 'hel' + IMPF + 'illâ' + 'en' + IMPF + belirli + 'ev' + IMPF + izafet + 'ev' + IMPF + izafet + 'yevm' + IMPF + izafet + 'lâ' + IMPF + nekre + izafet + 'lem' + IMPF + PERF + 'min' + 'qabl' + 'ev' + PERF + 'fî' + izafet + nekre + IMPV + IMPV + 'inne' + 'muntezir'; "
 "D2 soru, emir; IMPV ('quli' 34. kelime, 'ntezirû' 35. kelime), INTG ('hel' 1. kelime), NEG ('lâ' 20. kelime, 'lem' 24. kelime), RES ('illâ' 3. kelime); D3 16:33 eşi, أتي ×4, أمن ×3, أيي ×2, بعض ×2, ربب ×3, نظر ×3; D4 1P 1 · 2MP 2 · 2MS 4 · 3FS 6 · 3MP 3 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[158] + "; aktör yok (ölçüm); A2 bekledikleri şeyin sorulması; Rabbin âyetlerinden bazısı geldiği gün önceden inanmamış cana imanın fayda vermeyişi; bekleme emri ve karşılıklı bekleyiş; "
 "A3 'ntezirû innâ muntezirûn' (söz içi, 35-37. kelime); "
 "A4 " + BOLUM + "; söz açılır (35. kelime); söz kapanır (37. kelime, ayet içi); muhatap geçişi 2MS → 2MP (ayet içi, 'quli' / 'ntezirû'); şahıs geçişi yok (ayetler arası); edim geçişi soru, şart → soru, emir (ayetler arası); bölüm açılışı.",
)

D[159] = ("◇ 'inne'llezîne ferraqû dînehum ve kânû şiya'an leste minhum fî şey', innemâ emruhum ile'llâhi summe yunebbi'uhum bimâ kânû yef'alûn' — "
 "'inne' + 'ellezî' + PERF 3MP II. bab + 'dîn' + 3MP + 've' + PERF 3MP I. bab + nekre çoğul 'şî'a' + PERF 2MS I. bab + 'min' + 3MP + 'fî' + nekre 'şey'' + 'inne' + 'mâ' + 'emr' + 3MP + 'ilâ' + lafız + 'summe' + IMPF 3MS II. bab + 3MP + 'bi' + 'mâ' + PERF 3MP I. bab + IMPF 3MP I. bab "
 "(ölçüm edim haber, kip yok; 2MS 2 · 3MP 12 · 3MS 1; bab I. bab ×4 · II. bab ×2). "
 "Allah lafzı 14. sırada (ölçüm allah z=0,52); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=19 (n z=0,70); ölçüm '{{2|fâsıla يفعلون → ن, N sınıfı}}' — satır aynen (6:158 ن → 6:159 ن); "
 "ölçüm '{{2|simetri \\[3, 1, 8, 1\\]}}' — satır aynen; ölçüm '{{2|harf 82 → harf3 77, isaret 5}}' — satır aynen; ölçüm '{{2|dış düğüm 1}}' — satır aynen. "
 "Ölçüm kip yok; 've kânû' (5.) kelimesindeki 've' CONJ; 'summe' (15.) CONJ; 'inne' (1.) ACC; 'innemâ' (11.) ACC + PREV (okuma). "
 "Kök ikilemesi (ölçüm) كون ×2 ('kânû' 5. / 'kânû' 18. kelime) (okuma). "
 + T[159] + " (okuma). "
 + cumle(say('say 6:159 2-6', "llezîne ferraqû dînehum ve kânû şiya'an", True), say('dizi 6 159 2 6', "ellezî ferraqu dîn kâne şî'a")) + ' '
 + cumle(say('say 6:159 15-18', "summe yunebbi'uhum bimâ kânû", True), say('dizi 6 159 15 18', "summe nebbe'e mâ kâne")) + ' '
 + cumle(say('say 6:159 16-18 --on', "yunebbi'uhum bimâ kânû", True), say('dizi 6 159 16 18', "nebbe'e mâ kâne")) + ' ' +
 "Ölçüm xref 30:32 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıpları: 'summe nebbe'e mâ kâne' süzgeç GEÇER, 'nebbe'e mâ kâne' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'inne' + 'ellezî' + PERF + izafet + 've' + PERF + nekre + PERF + 'min' + 'fî' + nekre + 'inne' + 'mâ' + izafet + 'ilâ' + lafız + 'summe' + IMPF + 'bi' + 'mâ' + PERF + IMPF; "
 "D2 haber; kip yok; D3 30:32 eşi, كون ×2; D4 2MS 2 · 3MP 12 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[159] + "; aktör yok (ölçüm); A2 dinlerini parçalayıp bölük bölük olanlardan muhatabın ayrılması; işlerinin Allah'a kalması; yaptıklarının haber verilmesi; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi soru, emir → haber (ayetler arası).",
)

D[160] = ("◇ 'men câ'e bi'l-haseneti fe-lehû 'aşru emsâlihâ, ve men câ'e bi's-seyyi'eti fe-lâ yuczâ illâ mislehâ ve hum lâ yuzlemûn' — "
 "'men' + PERF 3MS I. bab + 'bi' + belirli 'hasene' + 'fe' + 'li' + 3MS + ''aşr' + çoğul 'mesel' + 3FS + 've' + 'men' + PERF 3MS I. bab + 'bi' + belirli 'seyyi'e' + 'fe' + 'lâ' + IMPF 3MS I. bab edilgen + 'illâ' + 'misl' + 3FS + 've' + 'hum' + 'lâ' + IMPF 3MP I. bab edilgen "
 "(ölçüm edim şart, kip COND 2 · NEG 2 · RES 1; 3FS 2 · 3MP 3 · 3MS 4; bab I. bab ×4). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=16 (n z=0,38); ölçüm '{{3|EDİLGEN 2/4 fiil, pas z=2,52}}' — satır aynen; ölçüm '{{3|fâsıla يظلمون → ن, N sınıfı}}' — satır aynen (6:159 ن → 6:160 ن); "
 "ölçüm '{{3|sayı işareti عَشْر}}' — satır aynen; ölçüm '{{3|simetri \\[4, 1, 7, 1\\]}}' — satır aynen; ölçüm '{{3|harf 66 → harf3 64, isaret 2}}' — satır aynen; ölçüm '{{3|dış düğüm 2}}' — satır aynen. "
 "Ölçüm COND 2: 'men' (1.) ve 'men' (7. kelime); NEG 2: 'lâ' (10.) ve 'lâ' (15. kelime); RES 1: 'illâ' (12. kelime); ölçüm biçim HASR ('illâ' 12. kelime); "
 "'ve men' (7.) kelimesindeki 've' CONJ; 've hum' (14.) kelimesindeki 've' CIRC; 'fe-lehû' (4.) ve 'fe-lâ' (10.) kelimelerindeki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) جيأ ×2 ('câ'e' 2. / 'câ'e' 8. kelime), مثل ×2 ('emsâlihâ' 6. / 'mislehâ' 13. kelime) (okuma). "
 + T[160] + " (okuma). "
 + cumle(say('say 6:160 7-11', "ve men câ'e bi's-seyyi'eti fe-lâ yuczâ", True), say('say 6:160 1-4', "men câ'e bi'l-haseneti fe-lehû", False), say('dizi 6 160 7 11', "men câ'e seyyi'e lâ cezâ")) + ' '
 + cumle(say('say 6:160 10-13', "fe-lâ yuczâ illâ mislehâ", True), say('dizi 6 160 9 13', "seyyi'e lâ cezâ illâ misl")) + ' ' +
 "Ölçüm xref 28:84 (emsal olarak basıldı), 40:40 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'bi'l-haseneti' / 'bi's-seyyi'eti' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'men' + PERF + 'bi' + belirli + 'fe' + 'li' + izafet + 've' + 'men' + PERF + 'bi' + belirli + 'fe' + 'lâ' + IMPF + 'illâ' + izafet + 've' + 'hum' + 'lâ' + IMPF; "
 "D2 şart; COND ('men' 1. kelime, 'men' 7. kelime), NEG ('lâ' 10. kelime, 'lâ' 15. kelime), RES ('illâ' 12. kelime); D3 28:84 eşi, 40:40 eşi, جيأ ×2, مثل ×2; D4 3FS 2 · 3MP 3 · 3MS 4, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[160] + "; aktör yok (ölçüm); A2 iyilikle gelene on misli; kötülükle gelene yalnızca dengi; zulmedilmeme; "
 "A3 —; "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; COND 'men' 1. kelime: 'men câ'e bi'l-haseneti' / 'fe-lehû' (4. kelime)); şart → cevap (ayet içi; COND 'men' 7. kelime: 've men câ'e bi's-seyyi'eti' / 'fe-lâ' (10. kelime)); "
 "şahıs geçişi yok (ayetler arası); edim geçişi haber → şart (ayetler arası).",
)
