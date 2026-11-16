# blok 3 (5:5-6) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b03/say2.txt'
os.environ['OLC'] = '/home/claude/b03/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Kitap ehlinin yemeği ve kadınları; abdest ve teyemmüm; nimeti ve misakı anma' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 5: "Bugün size temiz şeyler helâl kılındı. Kendilerine kitap verilenlerin yiyeceği sizin için helâldir, sizin yiyeceğiniz de onlar için helâldir. İnanan kadınlardan iffetli olanlar ve sizden önce kendilerine kitap verilenlerden iffetli olanlar da, onlara mehirlerini verdiğinizde, iffetli olarak, zina etmeksizin ve gizli dost tutmaksızın size helâl kılındı. Kim imanı inkâr ederse ameli boşa çıkmıştır ve o ahirette ziyana uğrayanlardandır.",
 6: "Ey iman edenler! Namaza kalktığınızda yüzlerinizi ve dirseklere kadar ellerinizi yıkayın, başlarınızı meshedin ve ayaklarınızı topuklara kadar yıkayın. Cünüpseniz yıkanarak temizlenin. Hasta ya da yolculukta olursanız, ya da sizden biri ayak yolundan gelirse, ya da kadınlara dokunmuşsanız ve su bulamamışsanız, temiz bir toprağa yönelin; ondan yüzlerinizi ve ellerinizi meshedin. Allah size bir sıkıntı vermek istemez; fakat sizi temizlemek ve size nimetini tamamlamak ister ki şükredesiniz.",
}

T5 = ("'uhille' faili (adsız; edilgen, 2. kelime; nâib fâil 't-tayyibât'); muhatap 2MP (adsız; 'lekum', 'ta'âmukum', 'qablikum', 'âteytumûhunne'); "
      "'ûtu' faili (adsız; edilgen, 7. ve 20. kelime; nâib fâil zamir 3MP — gönderge 'llezîne'); "
      "'l-muhsanâtu' (belirli çoğul edilgen ortaç; atıf, 14. ve 17. kelime); 'hunne' 3FP (adsız; 'âteytumûhunne', 'ucûrahunne' — gönderge 'l-muhsanâtu'); "
      "'muhsinîne' (muhatabın durumu; çoğul etken ortaç, 27. kelime); 'yekfur' faili 3MS (adsız; şart 'men', 34. kelime); 'huve' 3MS (adsız; 39. kelime — gönderge 'men')")
T6 = ("muhatap 2MP (adsız; 'llezîne âmenû' — nidâ, 2. ve 3. kelime; 'qumtum', 'ğsilû', 'msehû', 'kuntum', 'ttahherû', 'lâmestumu', 'tecidû', 'teyemmemû', 'yutahhirakum', ''aleykum', 'teşkurûn'); "
      "'ehadun minkum' ('câ'e' faili; nekre, 30. kelime); 'n-nisâ'e' ('lâmestumu' mef'ûlü; belirli çoğul, 36. kelime); Allah (lafız); "
      "'yec'ale', 'yurîdu' (55. kelime), 'yutahhira' ve 'yutimme' faili 3MS (adsız; gönderge lafız)")

D = {}
D[5] = ("◇ 'el-yevme uhille lekumu't-tayyibâtu ve ta'âmu'llezîne ûtu'l-kitâbe hillun lekum ve ta'âmukum hillun lehum ve'l-muhsanâtu mine'l-mu'minâti ve'l-muhsanâtu mine'llezîne ûtu'l-kitâbe min qablikum izâ âteytumûhunne ucûrahunne muhsinîne ğayra musâfihîne ve lâ muttexizî axdânin ve men yekfur bi'l-îmâni fe-qad habita 'ameluhû ve huve fi'l-âxirati mine'l-xâsirîn' — "
 "belirli 'yevm' + edilgen PERF 3MS IV. bab + 'li' + 2MP + belirli çoğul 'tayyibe' + 've' + 'ta'âm' + 'ellezî' + edilgen PERF 3MP IV. bab + belirli 'kitâb' + nekre 'hill' + 'li' + 2MP + 've' + 'ta'âm' + 2MP + nekre 'hill' + 'li' + 3MP + 've' + belirli çoğul edilgen ortaç 'muhsane' + 'min' + belirli çoğul etken ortaç 'mu'mine' + 've' + belirli çoğul edilgen ortaç 'muhsane' + 'min' + 'ellezî' + edilgen PERF 3MP IV. bab + belirli 'kitâb' + 'min' + 'qabl' + 2MP + 'izâ' + PERF 2MP IV. bab + 3FP + çoğul 'ecr' + 3FP + çoğul etken ortaç 'muhsin' + 'ğayr' + çoğul etken ortaç 'musâfih' + 've' + 'lâ' + çoğul etken ortaç 'muttexiz' + nekre çoğul 'axdân' + 've' + 'men' + IMPF 3MS I. bab + 'bi' + belirli masdar 'îmân' + 'fe' + 'qad' + PERF 3MS I. bab + ''amel' + 3MS + 've' + 'huve' + 'fî' + belirli 'âxir' + 'min' + belirli çoğul etken ortaç 'xâsir' "
 "(ölçüm edim şart, kip CERT 1 · COND 1 · NEG 1; 2MP 6 · 3FP 2 · 3MP 5 · 3MS 5; bab I. bab ×2 · IV. bab ×4). "
 "Ölçüm '{{1|lafız YOK · Rab YOK}}' — satır aynen; ölçüm esmâ '{{1|آخِر 41\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' (uyuşmuyor) — 've huve fi'l-âxirati mine'l-xâsirîn', kural ''fi'l-âxira' emsali → degil' (ahiret) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=43 (n z=3,25); ölçüm '{{1|fâsıla ٱلخسرين → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|EDİLGEN 3/6 fiil, pas z=2,52}}' — satır aynen; ölçüm '{{1|simetri \\[4, 6, 19, 1\\]}}' — satır aynen; ölçüm '{{1|harf 203 → harf3 194, isaret 9}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (36. kelime); COND 1: 'men' (33. kelime); NEG 1: 'lâ' (30. kelime) (okuma); edilgen 'uhille' (2. kelime), 'ûtu' (7. ve 20. kelime) (okuma); 'izâ' (24. kelime) morph T — zaman (okuma); "
 "'l-muhsanâtu' (14. ve 17. kelime) morph PASS_PCPL, 'l-mu'minâti' (16. kelime), 'muhsinîne' (27. kelime), 'musâfihîne' (29. kelime), 'muttexizî' (31. kelime) ve 'l-xâsirîn' (43. kelime) ACT_PCPL — ortaç, bab ◇'de yazılmadı; 'l-îmâni' (35. kelime) morph VN — masdar, bab ◇'de yazılmadı (okuma). "
 "Kök ikilemeleri (ölçüm) أتي ×3: 'ûtu' (7. ve 20. kelime), 'âteytumûhunne' (25. kelime); أمن ×2: 'l-mu'minâti' (16. kelime) / 'l-îmâni' (35. kelime); حصن ×3: 'l-muhsanâtu' (14. ve 17. kelime), 'muhsinîne' (27. kelime); حلل ×3: 'uhille' (2. kelime), 'hillun' (9. ve 12. kelime); "
 "طعم ×2: 've ta'âmu' (5. kelime) / 've ta'âmukum' (11. kelime); كتب ×2: 'l-kitâbe' (8. ve 21. kelime) (okuma). "
 "'ve ta'âmu' (5.) ve 've men' (33.)'deki 've' morph REM; 've ta'âmukum' (11.), 've'l-muhsanâtu' (14., 17.) ve 've lâ' (30.)'daki 've' CONJ; 've huve' (39.)'deki 've' CIRC; 'fe-qad' (36.)'daki 'fe' RSLT (okuma). "
 + T5 + " (okuma). "
 + cumle(say('say 5:5 1-4', "el-yevme uhille lekumu't-tayyibât", True), say('say 5:5 2-4', "uhille lekumu't-tayyibât"), say('say 5:5 5-8 --on', "ve ta'âmu'llezîne ûtu'l-kitâb"), say('lem 5:5:5', "ta'âm"), say('say 5:5 6-8', "llezîne ûtu'l-kitâb")) + ' '
 + cumle(say('say 5:5 9-10', "hillun lekum", True), say('lem 5:5:9', "hill"), say('say 5:5 11-13 --on', "ve ta'âmukum hillun lehum"), say('say 5:5 14-16 --on', "ve'l-muhsanâtu mine'l-mu'minât"), say('lem 5:5:14', "muhsane")) + ' '
 + cumle(say('say 5:5 18-23', "mine'llezîne ûtu'l-kitâbe min qablikum", True), say('say 5:5 19-23', "llezîne ûtu'l-kitâbe min qablikum"), say('say 5:5 24-26', "izâ âteytumûhunne ucûrahunne"), say('say 5:5 25-26', "âteytumûhunne ucûrahunne")) + ' '
 + cumle(say('say 5:5 27-29', "muhsinîne ğayra musâfihîn", True), say('say 5:5 28-29', "ğayra musâfihîn"), say('say 5:5 30-32 --on', "ve lâ muttexizî axdân"), say('lem 5:5:32', "axdân")) + ' '
 + cumle(say('say 5:5 33-35 --on', "ve men yekfur bi'l-îmân", True), say('say 5:5 36-38 --on', "fe-qad habita 'ameluh"), say('say 5:5 37-38', "habita 'ameluh"), say('lem 5:5:37', "habita")) + ' '
 + cumle(say('say 5:5 39-43 --on', "ve huve fi'l-âxirati mine'l-xâsirîn", True), say('say 5:5 40-43', "fi'l-âxirati mine'l-xâsirîn"), say('say 5:5 42-43', "mine'l-xâsirîn")) + ' '
 "Ölçüm xref 4:24 (basılmış). Ölçüm nakarat3 iki kalıp: bir kalıp süzgeç GEÇER, bir kalıp süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 've ta'âmu'llezîne ûtu'l-kitâbe hillun lekum' / 've ta'âmukum hillun lehum' — ayetler arası: yok.",
 "◈K — K2 'el-yevme' (1. kelime).",
 "◈B — —",
 "◈D — D1 belirli + PERF + 'li' + belirli + 've' + izafet + 'ellezî' + PERF + belirli + nekre + 'li' + 've' + izafet + nekre + 'li' + 've' + belirli + 'min' + belirli + 've' + belirli + 'min' + 'ellezî' + PERF + belirli + 'min' + izafet + 'izâ' + PERF + izafet + çoğul + izafet + çoğul + 've' + 'lâ' + izafet + nekre + 've' + 'men' + IMPF + 'bi' + belirli + 'fe' + 'qad' + PERF + izafet + 've' + 'huve' + 'fî' + belirli + 'min' + belirli; D2 şart, CERT ('qad' 36. kelime), COND ('men' 33. kelime), NEG ('lâ' 30. kelime); D3 أتي ×3 · أمن ×2 · حصن ×3 · حلل ×3 · طعم ×2 · كتب ×2; 2:217, 3:85, 3:93, 3:186, 4:24, 4:25, 39:65 ve 60:10 eşleri; D4 2MP 6 · 3FP 2 · 3MP 5 · 3MS 5, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T5 + "; aktör yok (ölçüm); A2 helâl kılma; temiz şeyler; yiyecek; kitap verilme; iffetli kadınlar; mehir verme; iffetli olma; zina etmeme; gizli dost tutmama; imanı inkâr; amelin boşa çıkması; ahirette ziyan; A3 —; A4 " + BOLUM + "; bölüm açılışı; edim geçişi soru, emir → şart (ayetler arası); şahıs geçişi yok; şart → cevap (ayet içi; COND 'men' 33. kelime: 've men yekfur bi'l-îmân' / 'fe-qad habita 'ameluh' (36. kelime)).",
)

D[6] = ("◇ 'yâ eyyuhe'llezîne âmenû izâ qumtum ile's-salâti fe'ğsilû vucûhekum ve eydiyekum ile'l-merâfiqi ve'msehû bi-ru'ûsikum ve erculekum ile'l-ka'beyni ve in kuntum cunuben fe'ttahherû ve in kuntum merdâ ev 'alâ seferin ev câ'e ehadun minkum mine'l-ğâ'iti ev lâmestumu'n-nisâ'e fe-lem tecidû mâ'en fe-teyemmemû sa'îden tayyiben fe'msehû bi-vucûhikum ve eydîkum minhu mâ yurîdu'llâhu li-yec'ale 'aleykum min haracin ve lâkin yurîdu li-yutahhirakum ve li-yutimme ni'metehû 'aleykum le'allekum teşkurûn' — "
 "'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF 3MP IV. bab + 'izâ' + PERF 2MP I. bab + 'ilâ' + belirli 'salâ' + 'fe' + IMPV 2MP I. bab + çoğul 'vech' + 2MP + 've' + çoğul 'yed' + 2MP + 'ilâ' + belirli 'merâfiq' + 've' + IMPV 2MP I. bab + 'bi' + çoğul 're's' + 2MP + 've' + çoğul 'ricl' + 2MP + 'ilâ' + belirli ikil 'ka'beyn' + 've' + 'in' + PERF 2MP I. bab + nekre 'cunub' + 'fe' + IMPV 2MP V. bab + 've' + 'in' + PERF 2MP I. bab + çoğul 'merîd' + 'ev' + ''alâ' + nekre 'sefer' + 'ev' + PERF 3MS I. bab + nekre 'ehad' + 'min' + 2MP + 'min' + belirli 'ğâ'it' + 'ev' + PERF 2MP I. bab + belirli çoğul 'nisâ'' + 'fe' + 'lem' + IMPF 2MP I. bab + nekre 'mâ'' + 'fe' + IMPV 2MP V. bab + nekre 'sa'îd' + nekre 'tayyib' + 'fe' + IMPV 2MP I. bab + 'bi' + çoğul 'vech' + 2MP + 've' + çoğul 'yed' + 2MP + 'min' + 3MS + 'mâ' + IMPF 3MS IV. bab + lafız + 'li' + IMPF 3MS I. bab + ''alâ' + 2MP + 'min' + nekre 'harac' + 've' + 'lâkin' + IMPF 3MS IV. bab + 'li' + IMPF 3MS II. bab + 2MP + 've' + 'li' + IMPF 3MS IV. bab + 'ni'me' + 3MS + ''alâ' + 2MP + 'le'alle' + 2MP + IMPF 2MP I. bab "
 "(ölçüm edim emir, nida, şart, kip COND 2 · IMPV 5 · NEG 2 · VOC 1, biçim DIKKAT; 2MP 33 · 3MP 2 · 3MS 8; bab I. bab ×11 · II. bab ×1 · IV. bab ×4 · V. bab ×2). "
 "Allah lafzı 49. sırada (ölçüm allah z=-0,20); Rab yok; ölçüm esmâ '{{2|أَحَد 30\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor) — 'ev câ'e ehadun minkum', kural 'esmâ adı esmâ dışı göndergeyle → degil' (biriniz) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=61 (n z=5,16); ölçüm '{{2|biçim DIKKAT}}' — satır aynen; ölçüm '{{2|fâsıla تشكرون → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|sayı işareti أَحَد}}' — satır aynen; ölçüm '{{2|simetri \\[4, 9, 44, 1\\]}}' — satır aynen; ölçüm '{{2|harf 297 → harf3 280, isaret 17}}' — satır aynen; ölçüm '{{2|dış düğüm 4}}' — satır aynen. "
 "Ölçüm COND 2: 'in' (18. ve 22. kelime); IMPV 5: 'ğsilû' (8. kelime), 'msehû' (13. ve 43. kelime), 'ttahherû' (21. kelime), 'teyemmemû' (40. kelime); NEG 2: 'lem' (37. kelime), 'mâ' (47. kelime); VOC 1: 'yâ' (1. kelime) (okuma); ölçüm biçim DIKKAT — 'yâ eyyuhâ' nidâsı; D2'de yazılmadı (okuma); 'izâ' (4. kelime) morph T — zaman; 'li' (50., 56. ve 57. kelime) morph PRP (okuma). "
 "Kök ikilemeleri (ölçüm) رود ×2: 'yurîdu' (48. ve 55. kelime); طهر ×2: 'ttahherû' (21. kelime) / 'yutahhirakum' (56. kelime); كون ×2: 'kuntum' (19. ve 23. kelime); مسح ×2: 'msehû' (13. ve 43. kelime); وجه ×2: 'vucûhekum' (9. kelime) / 'vucûhikum' (44. kelime); يدي ×2: 've eydiyekum' (10. kelime) / 've eydîkum' (45. kelime) (okuma). "
 "'ve eydiyekum' (10.), 've'msehû' (13.), 've erculekum' (15.), 've in' (22.), 've eydîkum' (45.) ve 've li-yutimme' (57.)'deki 've' morph CONJ; 've in' (18.) ve 've lâkin' (54.)'deki 've' REM; 'fe'ğsilû' (8.), 'fe'ttahherû' (21.) ve 'fe-teyemmemû' (40.)'daki 'fe' RSLT; 'fe-lem' (37.) ve 'fe'msehû' (43.)'daki 'fe' CONJ (okuma). "
 + T6 + " (okuma). "
 + cumle(say('say 5:6 1-3', "yâ eyyuhe'llezîne âmenû", True), say('say 5:6 4-7', "izâ qumtum ile's-salâh"), say('say 5:6 5-7', "qumtum ile's-salâh")) + ' '
 + cumle(say('say 5:6 8-10 --on', "fe'ğsilû vucûhekum ve eydiyekum", True), say('lem 5:6:8', "ğsilu"), say('say 5:6 11-12', "ile'l-merâfiq"), say('lem 5:6:12', "merâfiq"), say('say 5:6 13-14 --on', "ve'msehû bi-ru'ûsikum"), say('say 5:6 15-17 --on', "ve erculekum ile'l-ka'beyn"), say('lem 5:6:17', "ka'beyn")) + ' '
 + cumle(say('say 5:6 18-21 --on', "ve in kuntum cunuben fe'ttahherû", True), say('say 5:6 19-20', "kuntum cunubâ"), say('say 5:6 22-27 --on', "ve in kuntum merdâ ev 'alâ sefer"), say('say 5:6 23-27', "kuntum merdâ ev 'alâ sefer"), say('dizi 5 6 24 27', "merîd ev 'alâ sefer")) + ' '
 + cumle(say('say 5:6 28-33', "ev câ'e ehadun minkum mine'l-ğâ'it", True), say('say 5:6 34-39', "ev lâmestumu'n-nisâ'e fe-lem tecidû mâ'â"), say('say 5:6 40-42 --on', "fe-teyemmemû sa'îden tayyibâ"), say('say 5:6 43-45 --on', "fe'msehû bi-vucûhikum ve eydîkum"), say('say 5:6 43-46 --on', "fe'msehû bi-vucûhikum ve eydîkum minh")) + ' '
 + cumle(say('say 5:6 47-49', "mâ yurîdu'llâh", True), say('say 5:6 47-53', "mâ yurîdu'llâhu li-yec'ale 'aleykum min harac"), say('lem 5:6:53', "harac"), say('say 5:6 54-56 --on', "ve lâkin yurîdu li-yutahhirakum"), say('lem 5:6:56', "tahhara")) + ' '
 + cumle(say('say 5:6 57-59 --on', "ve li-yutimme ni'metehû 'aleykum", True), say('dizi 5 6 57 58', "etemme ni'me"), say('say 5:6 60-61', "le'allekum teşkurûn")) + ' '
 "Ölçüm xref 2:184, 2:185 ve 4:43 (basılmış), okunmuş bir ayet. Ölçüm nakarat3 bir kalıp: süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'mâ yurîdu'llâhu li-yec'ale 'aleykum min haracin' / 've lâkin yurîdu li-yutahhirakum' — ayetler arası: yok.",
 "◈K — K1 'mâ'en' (39. kelime).",
 "◈B — B1 —; B2 —; B3 'eydiyekum' (10. kelime), 'eydîkum' (45. kelime); B4 —.",
 "◈D — D1 'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF + 'izâ' + PERF + 'ilâ' + belirli + 'fe' + IMPV + izafet + 've' + izafet + 'ilâ' + belirli + 've' + IMPV + 'bi' + izafet + 've' + izafet + 'ilâ' + belirli + 've' + 'in' + PERF + nekre + 'fe' + IMPV + 've' + 'in' + PERF + çoğul + 'ev' + ''alâ' + nekre + 'ev' + PERF + nekre + 'min' + 'min' + belirli + 'ev' + PERF + belirli + 'fe' + 'lem' + IMPF + nekre + 'fe' + IMPV + nekre + nekre + 'fe' + IMPV + 'bi' + izafet + 've' + izafet + 'min' + 'mâ' + IMPF + lafız + 'li' + IMPF + ''alâ' + 'min' + nekre + 've' + 'lâkin' + IMPF + 'li' + IMPF + 've' + 'li' + IMPF + izafet + ''alâ' + 'le'alle' + IMPF; D2 emir, nida, şart, COND ('in' 18. ve 22. kelime), IMPV ('ğsilû' 8. kelime, 'msehû' 13. ve 43. kelime, 'ttahherû' 21. kelime, 'teyemmemû' 40. kelime), NEG ('lem' 37. kelime, 'mâ' 47. kelime), VOC ('yâ' 1. kelime); D3 رود ×2 · طهر ×2 · كون ×2 · مسح ×2 · وجه ×2 · يدي ×2; 2:150, 2:184, 2:185, 4:43, 12:6, 16:81, 22:78 ve 48:2 eşleri; 5:1 sûre içi eşi; D4 2MP 33 · 3MP 2 · 3MS 8, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T6 + "; aktör yok (ölçüm); A2 iman; namaza kalkma; yıkama; meshetme; cünüplük; temizlenme; hastalık; yolculuk; ayak yolu; dokunma; su bulmama; teyemmüm; sıkıntı vermeme; temizleme; nimeti tamamlama; şükür; A3 —; A4 " + BOLUM + "; hitap açılır ('yâ eyyuhe'llezîne âmenû', 1-3. kelime); edim geçişi şart → emir, nida, şart (ayetler arası); şahıs geçişi yok; şart → cevap (ayet içi; COND 'in' 18. kelime: 've in kuntum cunuben' / 'fe'ttahherû' (21. kelime)); şart → cevap (ayet içi; COND 'in' 22. kelime: 've in kuntum merdâ ev 'alâ seferin' / 'fe-teyemmemû sa'îden tayyiben' (40. kelime)).",
)

out = ['# ── blok 5:5-6 (2026-11-15) ──', 'MEAL3 = {']
for n in range(5, 7):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M3 = {']
for n in range(5, 7):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL3); M.update(M3)']
open('/home/claude/yamalar/metin_5_5_6.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
