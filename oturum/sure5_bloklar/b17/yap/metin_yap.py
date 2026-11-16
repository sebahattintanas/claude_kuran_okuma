# blok 17 (5:48-50) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b17/say2.txt'
os.environ['OLC'] = '/home/claude/b17/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Küfürde yarışanlar; Tevrat, İncil ve Kitap ile hüküm' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 48: "Sana da Kitab'ı, önündeki Kitab'ı doğrulayıcı ve onun üzerinde gözetici olarak hak ile indirdik. Öyleyse aralarında Allah'ın indirdiğiyle hüküm ver; sana gelen haktan ayrılıp onların heveslerine uyma. Sizden herkes için bir şeriat ve bir yol kıldık. Allah dileseydi sizi bir ümmet kılardı; fakat size verdiğinde sizi sınamak için. Öyleyse hayırlarda yarışın. Dönüşünüz hep birlikte Allah'adır; o, içinde ayrılığa düşmüş olduğunuz şeyi size haber verecek.",
 49: "Aralarında Allah'ın indirdiğiyle hüküm ver, onların heveslerine uyma ve Allah'ın sana indirdiğinin bir kısmından seni saptırmalarından onlardan sakın. Yüz çevirirlerse bil ki Allah onları ancak günahlarının bir kısmıyla musibete uğratmak istiyor. İnsanlardan çoğu elbette fâsıklardır.",
 50: "Yoksa cahiliye hükmünü mü arıyorlar? Kesin bilen bir kavim için hüküm bakımından Allah'tan daha güzel kim var?",
}

T48 = ("konuşan 1P (adsız; 'enzelnâ' 1. kelime, 'ce'alnâ' 26. kelime); muhatap 2MS (adsız; 'ileyke' 2., 'fa'hkum' 13., 'tettebi' 19., 'câ'eke' 22. kelime); 'yedeyhi' 3MS (adsız; gönderge 'l-kitâbe', 8. kelime); ''aleyhi' 3MS (adsız; gönderge 'l-kitâbi', 12. kelime); 'beynehum' 3MP (adsız; 14. kelime); "
       "'enzele' faili 3MS (adsız; gönderge lafız, 16. kelime); Allah (lafız; 17., 32. ve 44. kelime); 'ehvâ'ehum' 3MP (adsız; 20. kelime); 'câ'eke' faili 3MS (adsız; gönderge 'l-haqq', 22. kelime); 'kullin' (nekre; 25. kelime); "
       "muhatap 2MP (adsız; 'minkum' 27., 'le-ce'alekum' 33., 'li-yebluvekum' 37., 'âtâkum' 40., 'fe'stebiqu' 41., 'merci'ukum' 45., 'fe-yunebbi'ukum' 47., 'kuntum' 49., 'taxtelifûn' 51. kelime); 'şir'aten ve minhâcâ' (nekre; 28-29. kelime); "
       "'şâ'e' faili 3MS (adsız; gönderge lafız, 31. kelime); 'ce'ale' faili 3MS (adsız; 33. kelime); 'ummeten vâhideten' (nekre; 34-35. kelime); 'yebluve' faili 3MS (adsız; 37. kelime); 'âtâ' faili 3MS (adsız; 40. kelime); "
       "'yunebbi'u' faili 3MS (adsız; 47. kelime); 'fîhi' 3MS (adsız; gönderge 'mâ', 50. kelime)")
T49 = ("muhatap 2MS (adsız; 'hkum' 2., 'tettebi' 8., 've'hzerhum' 10., 'yeftinûke' 12., 'ileyke' 18., 'fa'lem' 21. kelime); 'beynehum' 3MP (adsız; 3. kelime); 'enzele' faili 3MS (adsız; gönderge lafız, 5. ve 16. kelime); Allah (lafız; 6., 17. ve 24. kelime); "
       "'ehvâ'ehum' 3MP (adsız; 9. kelime); 've'hzerhum' mef'ûlü 3MP (adsız; 10. kelime); 'yeftinûke' faili 3MP (adsız; 12. kelime); 'tevellev' faili 3MP (adsız; 20. kelime); 'yurîdu' faili 3MS (adsız; gönderge lafız, 23. kelime); "
       "'yusîbehum' faili 3MS (adsız; 26. kelime); 'yusîbehum' mef'ûlü 3MP (adsız; 26. kelime); 'zunûbihim' 3MP (adsız; 28. kelime); 'kesîran mine'n-nâs' (30-32. kelime); 'le-fâsiqûn' (33. kelime)")
T50 = ("'l-câhiliyyeti' (adlı aktör — cins; 2. kelime); 'yebğûn' faili 3MP (adsız; 3. kelime); 'men' (soru ismi; 4. kelime); Allah (lafız; 7. kelime); 'hukman' (nekre; 8. kelime); 'qavmin' (nekre; 9. kelime); 'yûqinûn' faili 3MP (adsız; 10. kelime)")

D = {}
D[48] = ("◇ 've enzelnâ ileyke'l-kitâbe bi'l-haqqi musaddiqan li-mâ beyne yedeyhi mine'l-kitâbi ve muheyminen 'aleyhi fa'hkum beynehum bi-mâ enzele'llâhu ve lâ tettebi' ehvâ'ehum 'ammâ câ'eke mine'l-haqqi li-kullin ce'alnâ minkum şir'aten ve minhâcâ ve lev şâ'e'llâhu le-ce'alekum ummeten vâhideten ve lâkin li-yebluvekum fî mâ âtâkum fe'stebiqu'l-xayrâti ile'llâhi merci'ukum cemî'an fe-yunebbi'ukum bi-mâ kuntum fîhi taxtelifûn' — "
 "'ve' + PERF 1P IV. bab + 'ilâ' + 2MS + belirli 'kitâb' + 'bi' + belirli 'haqq' + nekre ortaç 'musaddiq' + 'li' + 'mâ' + 'beyn' + ikil 'yed' + 3MS + 'min' + belirli 'kitâb' + 've' + nekre ortaç 'muheymin' + ''alâ' + 3MS + 'fe' + IMPV 2MS I. bab + 'beyn' + 3MP + 'bi' + 'mâ' + PERF 3MS IV. bab + lafız + 've' + 'lâ' + IMPF 2MS VIII. bab + çoğul 'ehvâ'' + 3MP + ''an' + 'mâ' + PERF 3MS I. bab + 2MS + 'min' + belirli 'haqq' + "
 "'li' + nekre 'kull' + PERF 1P I. bab + 'min' + 2MP + nekre 'şir'a' + 've' + nekre 'minhâc' + 've' + 'lev' + PERF 3MS I. bab + lafız + 'le' + PERF 3MS I. bab + 2MP + nekre 'umme' + nekre 'vâhide' + 've' + 'lâkin' + 'li' + IMPF 3MS I. bab + 2MP + 'fî' + 'mâ' + PERF 3MS IV. bab + 2MP + 'fe' + IMPV 2MP VIII. bab + belirli çoğul 'xayra' + 'ilâ' + lafız + 'merci'' + 2MP + nekre 'cemî'' + 'fe' + IMPF 3MS II. bab + 2MP + 'bi' + 'mâ' + PERF 2MP I. bab + 'fî' + 3MS + IMPF 2MP VIII. bab "
 "(ölçüm edim emir, yasak, şart, kip COND 1 · EMPH 1 · IMPV 2 · PRO 1, biçim NEHY; 1P 4 · 2MP 12 · 2MS 4 · 3MP 2 · 3MS 10; bab I. bab ×7 · II. bab ×1 · IV. bab ×3 · VIII. bab ×3). "
 "Allah lafzı 17., 32. ve 44. sırada (ölçüm allah z=0,65); Rab yok; ölçüm '{{1|esmâ \\S+ 11\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor) — 've muheyminen 'aleyh', kural 'esmâ adı esmâ dışı göndergeyle → degil' (Kitap için gözetici) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=51 (n z=4,10); ölçüm hapaks نهج ('minhâcâ' 29. kelime; hapaks z=3,28); ölçüm '{{1|fâsıla تختلفون → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|simetri \\[3, 2, 9, 1\\]}}' — satır aynen; ölçüm '{{1|harf 239 → harf3 225, isaret 14}}' — satır aynen; ölçüm '{{1|dış düğüm 5}}' — satır aynen. "
 "Ölçüm IMPV 2: 'fa'hkum' (13. kelime), 'fe'stebiqu' (41. kelime); PRO 1: 'lâ' (18. kelime); COND 1: 'lev' (30. kelime); EMPH 1: 'le' (33. kelime); 've enzelnâ' (1.), 've muheyminen' (11.) ve 've minhâcâ' (29.)'daki 've' CONJ, 've lâ' (18.), 've lev' (30.) ve 've lâkin' (36.)'deki 've' REM; 'fa'hkum' (13.)'daki 'fe' CONJ, 'fe'stebiqu' (41.) ve 'fe-yunebbi'ukum' (47.)'daki 'fe' REM (okuma). "
 "Kök ikilemesi (ölçüm) أله ×3 (lafız 17., 32., 44. kelime), بين ×2 ('beyne' 7. / 'beynehum' 14. kelime), جعل ×2 ('ce'alnâ' 26. / 'le-ce'alekum' 33. kelime), حقق ×2 ('l-haqqi' 4. / 24. kelime), كتب ×2 ('l-kitâbe' 3. / 'l-kitâbi' 10. kelime), نزل ×2 ('enzelnâ' 1. / 'enzele' 16. kelime) (okuma). "
 + T48 + " (okuma). "
 + cumle(say('say 5:48 1-4 --on', "ve enzelnâ ileyke'l-kitâbe bi'l-haqq", True), say('say 5:48 2-4', "ileyke'l-kitâbe bi'l-haqq"), say('say 5:48 3-4', "l-kitâbe bi'l-haqq")) + ' '
 + cumle(say('say 5:48 5-10', "musaddiqan li-mâ beyne yedeyhi mine'l-kitâb", True), say('say 5:48 5-9', "musaddiqan li-mâ beyne yedeyhi min"), say('dizi 5 48 5 9', "musaddiq mâ beyn yed min"), say('say 5:48 6-8', "li-mâ beyne yedeyh"), say('say 5:48 7-8', "beyne yedeyh"), say('say 5:48 11-12 --on', "ve muheyminen 'aleyh")) + ' '
 + cumle(say('say 5:48 13-17 --on', "fa'hkum beynehum bi-mâ enzele'llâh", True), say('dizi 5 48 13 17', "hakeme beyn mâ enzele allâh"), say('say 5:48 14-17', "beynehum bi-mâ enzele'llâh"), say('say 5:48 15-17', "bi-mâ enzele'llâh"), say('dizi 5 48 15 17', "mâ enzele allâh")) + ' '
 + cumle(say('say 5:48 18-20 --on', "ve lâ tettebi' ehvâ'ehum", True), say('say 5:48 19-20', "tettebi' ehvâ'ehum"), say('say 5:48 21-24', "'ammâ câ'eke mine'l-haqq"), say('say 5:48 22-24', "câ'eke mine'l-haqq")) + ' '
 + cumle(say('say 5:48 25-29', "li-kullin ce'alnâ minkum şir'aten ve minhâcâ", True), say('say 5:48 26-27', "ce'alnâ minkum"), say('lem 5:48:28', "şir'a"), say('lem 5:48:29', "minhâc")) + ' '
 + cumle(say('say 5:48 30-35 --on', "ve lev şâ'e'llâhu le-ce'alekum ummeten vâhide", True), say('say 5:48 31-32', "şâ'e'llâh"), say('say 5:48 33-35', "le-ce'alekum ummeten vâhide"), say('say 5:48 34-35', "ummeten vâhide")) + ' '
 + cumle(say('say 5:48 36-40 --on', "ve lâkin li-yebluvekum fî mâ âtâkum", True), say('lem 5:48:37', "belev"), say('say 5:48 38-40', "fî mâ âtâkum"), say('say 5:48 41-42 --on', "fe'stebiqu'l-xayrât")) + ' '
 + cumle(say('say 5:48 43-46', "ile'llâhi merci'ukum cemî'an", True), say('say 5:48 43-45', "ile'llâhi merci'ukum"), say('say 5:48 43-49', "ile'llâhi merci'ukum cemî'an fe-yunebbi'ukum bi-mâ kuntum"), say('dizi 5 48 43 49', "ilâ allâh merci' cemî' nebbe'e mâ kâne")) + ' '
 + cumle(say('say 5:48 47-51 --on', "fe-yunebbi'ukum bi-mâ kuntum fîhi taxtelifûn", True), say('say 5:48 48-51', "bi-mâ kuntum fîhi taxtelifûn"), say('say 5:48 49-51', "kuntum fîhi taxtelifûn")) + ' '
 "Ölçüm xref 16:93 (emsal olarak basıldı) ve okunmuş ve henüz okunmamış başka ayetler. "
 "Ölçüm nakarat3 kalıpları: 'ile'llâhi merci'ukum cemî'an fe-yunebbi'ukum bi-mâ kuntum', 'musaddiqan li-mâ beyne yedeyhi min', 'fa'hkum beynehum bi-mâ enzele'llâh' ve 'bi-mâ enzele'llâh' süzgeç GEÇER; 'câ'eke mine'l-haqq' GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'yedeyhi' (8. kelime); B4 —.",
 "◈D — D1 've' + PERF + 'ilâ' + belirli + 'bi' + belirli + nekre + 'li' + 'mâ' + 'beyn' + izafet + 'min' + belirli + 've' + nekre + ''alâ' + 'fe' + IMPV + 'beyn' + 'bi' + 'mâ' + PERF + lafız + 've' + 'lâ' + IMPF + izafet + ''an' + 'mâ' + PERF + 'min' + belirli + 'li' + nekre + PERF + 'min' + nekre + 've' + nekre + 've' + 'lev' + PERF + lafız + 'le' + PERF + nekre + nekre + 've' + 'lâkin' + 'li' + IMPF + 'fî' + 'mâ' + PERF + 'fe' + IMPV + belirli + 'ilâ' + lafız + izafet + nekre + 'fe' + IMPF + 'bi' + 'mâ' + PERF + 'fî' + IMPF; "
 "D2 emir, yasak, şart, IMPV ('fa'hkum' 13. kelime, 'fe'stebiqu' 41. kelime), PRO ('lâ' 18. kelime), COND ('lev' 30. kelime), EMPH ('le' 33. kelime); D3 أله ×3, بين ×2, جعل ×2, حقق ×2, كتب ×2, نزل ×2; 16:93 ve 2:148 eşleri; D4 1P 4 · 2MP 12 · 2MS 4 · 3MP 2 · 3MS 10, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T48 + "; aktör yok (ölçüm); A2 Kitabın hak ile inişi; önceki Kitabı doğrulama ve gözetme; indirilenle hüküm; heveslere uymama; şeriat ve yol; ümmet; sınama; hayırlarda yarış; dönüş; ayrılık; A3 —; "
 "A4 " + BOLUM + "; edim geçişi emir, şart → emir, yasak, şart (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası); şart → cevap (ayet içi; COND 'lev' 30. kelime: 've lev şâ'e'llâh' / 'le-ce'alekum ummeten vâhide' (33. kelime)).",
)

D[49] = ("◇ 've eni'hkum beynehum bi-mâ enzele'llâhu ve lâ tettebi' ehvâ'ehum ve'hzerhum en yeftinûke 'an ba'di mâ enzele'llâhu ileyke fe-in tevellev fa'lem ennemâ yurîdu'llâhu en yusîbehum bi-ba'di zunûbihim ve inne kesîran mine'n-nâsi le-fâsiqûn' — "
 "'ve' + 'en' + IMPV 2MS I. bab + 'beyn' + 3MP + 'bi' + 'mâ' + PERF 3MS IV. bab + lafız + 've' + 'lâ' + IMPF 2MS VIII. bab + çoğul 'ehvâ'' + 3MP + 've' + IMPV 2MS I. bab + 3MP + 'en' + IMPF 3MP I. bab + 2MS + ''an' + 'ba'd' + 'mâ' + PERF 3MS IV. bab + lafız + 'ilâ' + 2MS + 'fe' + 'in' + PERF 3MP V. bab + 'fe' + IMPV 2MS I. bab + 'enne' + 'mâ' + IMPF 3MS IV. bab + lafız + 'en' + IMPF 3MS IV. bab + 3MP + 'bi' + 'ba'd' + çoğul 'zenb' + 3MP + 've' + 'inne' + nekre 'kesîr' + 'min' + belirli çoğul 'nâs' + 'le' + çoğul 'fâsiq' "
 "(ölçüm edim emir, yasak, şart, kip COND 1 · EMPH 1 · IMPV 3 · PRO 1, biçim NEHY; 2MS 6 · 3MP 9 · 3MS 4; bab I. bab ×4 · IV. bab ×4 · V. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 6., 17. ve 24. sırada (ölçüm allah z=1,29); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=33 (n z=2,19); ölçüm '{{2|fâsıla لفسقون → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|simetri \\[6, 4, 15, 2\\]}}' — satır aynen; ölçüm '{{2|harf 140 → harf3 135, isaret 5}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm IMPV 3: 'hkum' (2. kelime), 've'hzerhum' (10. kelime), 'fa'lem' (21. kelime); PRO 1: 'lâ' (7. kelime); COND 1: 'in' (19. kelime); EMPH 1: 'le' (33. kelime); 've eni'hkum' (1.), 've lâ' (7.) ve 've'hzerhum' (10.)'daki 've' CONJ, 've inne' (29.)'deki 've' REM; 'fe-in' (19.)'deki 'fe' REM, 'fa'lem' (21.)'deki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) أله ×3 (lafız 6., 17., 24. kelime), بعض ×2 ('ba'di' 14. / 'bi-ba'di' 27. kelime), نزل ×2 ('enzele' 5. / 16. kelime) (okuma). "
 + T49 + " (okuma). "
 + cumle(say('say 5:49 1-6 --on', "ve eni'hkum beynehum bi-mâ enzele'llâh", True), say('say 5:49 2-6', "hkum beynehum bi-mâ enzele'llâh"), say('dizi 5 49 2 6', "hakeme beyn mâ enzele allâh"), say('say 5:49 4-6', "bi-mâ enzele'llâh")) + ' '
 + cumle(say('say 5:49 7-9 --on', "ve lâ tettebi' ehvâ'ehum", True), say('say 5:49 8-9', "tettebi' ehvâ'ehum"), say('say 5:49 10-12 --on', "ve'hzerhum en yeftinûke"), say('lem 5:49:10', "yahzeru"), say('lem 5:49:12', "fetenu")) + ' '
 + cumle(say('say 5:49 13-18', "'an ba'di mâ enzele'llâhu ileyk", True), say('say 5:49 14-17', "ba'di mâ enzele'llâh"), say('say 5:49 15-17', "mâ enzele'llâh")) + ' '
 + cumle(say('say 5:49 19-22 --on', "fe-in tevellev fa'lem ennemâ", True), say('dizi 5 49 19 22', "in tevellâ 'alime ennemâ"), say('say 5:49 19-20 --on', "fe-in tevellev"), say('say 5:49 21-24 --on', "fa'lem ennemâ yurîdu'llâh"), say('say 5:49 23-24', "yurîdu'llâh")) + ' '
 + cumle(say('say 5:49 25-28', "en yusîbehum bi-ba'di zunûbihim", True), say('say 5:49 27-28', "bi-ba'di zunûbihim"), say('say 5:49 29-33 --on', "ve inne kesîran mine'n-nâsi le-fâsiqûn"), say('say 5:49 30-32', "kesîran mine'n-nâs"), say('say 5:49 31-33', "mine'n-nâsi le-fâsiqûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: 'hkum beynehum bi-mâ enzele'llâh', 'fe-in tevellev fa'lem ennemâ' ve 'bi-mâ enzele'llâh' süzgeç GEÇER; 'yurîdu'llâhu en', 'lâ tettebi' ehvâ'ehum' ve 'mâ enzele'llâh' GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'n-nâsi' (32. kelime); B2 —; B3 —; B4 —.",
 "◈D — D1 've' + 'en' + IMPV + 'beyn' + 'bi' + 'mâ' + PERF + lafız + 've' + 'lâ' + IMPF + izafet + 've' + IMPV + 'en' + IMPF + ''an' + 'ba'd' + 'mâ' + PERF + lafız + 'ilâ' + 'fe' + 'in' + PERF + 'fe' + IMPV + 'enne' + 'mâ' + IMPF + lafız + 'en' + IMPF + 'bi' + 'ba'd' + izafet + 've' + 'inne' + nekre + 'min' + belirli + 'le' + çoğul; "
 "D2 emir, yasak, şart, IMPV ('hkum' 2. kelime, 've'hzerhum' 10. kelime, 'fa'lem' 21. kelime), PRO ('lâ' 7. kelime), COND ('in' 19. kelime), EMPH ('le' 33. kelime); D3 أله ×3, بعض ×2, نزل ×2; D4 2MS 6 · 3MP 9 · 3MS 4, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T49 + "; aktör yok (ölçüm); A2 indirilenle hüküm; heveslere uymama; fitneden sakınma; yüz çevirme; günah ve musibet; fâsıklık; A3 —; "
 "A4 " + BOLUM + "; edim geçişi yok (emir, yasak, şart); şahıs geçişi 2 → 3 (ayetler arası); şart → cevap (ayet içi; COND 'in' 19. kelime: 'fe-in tevellev' / 'fa'lem ennemâ yurîdu'llâhu en yusîbehum bi-ba'di zunûbihim' (21. kelime)).",
)

D[50] = ("◇ 'e-fe-hukme'l-câhiliyyeti yebğûn ve men ahsenu mine'llâhi hukman li-qavmin yûqinûn' — "
 "'e' + 'fe' + 'hukm' + belirli 'câhiliyye' + IMPF 3MP I. bab + 've' + 'men' + 'ahsen' + 'min' + lafız + nekre 'hukm' + 'li' + nekre 'qavm' + IMPF 3MP IV. bab "
 "(ölçüm edim soru, kip INTG 2; 3MP 4; bab I. bab ×1 · IV. bab ×1). "
 "Allah lafzı 7. sırada (ölçüm allah z=1,47); Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm '{{3|aktör: adlı \\S+ 2\\. sırada \\(cins, rol mecrur\\)}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=10 (n z=-0,26); ölçüm '{{3|fâsıla يوقنون → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|harf 47 → harf3 44, isaret 3}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm INTG 2: 'e' (1. kelime), 'men' (4. kelime); 'e-fe' (1.)'deki 'fe' SUP; 've men' (4.)'deki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) حكم ×2 ('hukme' 1. / 'hukman' 8. kelime) (okuma). "
 + T50 + " (okuma). "
 + cumle(say('say 5:50 1-3 --on', "e-fe-hukme'l-câhiliyyeti yebğûn", True), say('say 5:50 1-2 --on', "e-fe-hukme'l-câhiliyye")) + ' '
 + cumle(say('say 5:50 4-8 --on', "ve men ahsenu mine'llâhi hukman", True), say('say 5:50 5-7', "ahsenu mine'llâh"), say('say 5:50 8-10', "hukman li-qavmin yûqinûn"), say('say 5:50 9-10', "li-qavmin yûqinûn"), say('lem 5:50:10', "yûqinu")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'e' + 'fe' + izafet + belirli + IMPF + 've' + 'men' + 'ahsen' + 'min' + lafız + nekre + 'li' + nekre + IMPF; "
 "D2 soru, INTG ('e' 1. kelime, 'men' 4. kelime); D3 حكم ×2; 2:138 eşi; D4 3MP 4, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T50 + "; ölçüm aktör adlı cahiliye (cins, mecrur); A2 cahiliye hükmü; Allah'ın hükmü; kesin bilen kavim; A3 —; "
 "A4 " + BOLUM + "; edim geçişi emir, yasak, şart → soru (ayetler arası); şahıs geçişi yok.",
)

out = ['# ── blok 5:48-50 (2026-11-15) ──', 'MEAL17 = {']
for n in range(48, 51):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M17 = {']
for n in range(48, 51):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL17); M.update(M17)']
open('/home/claude/yamalar/metin_5_48_50.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
