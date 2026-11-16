# blok 2 (5:3-4) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b02/say2.txt'
os.environ['OLC'] = '/home/claude/b02/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Ahitlere vefa; haram kılınanlar; dinin tamamlanması; helal yiyecekler' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 3: "Ölü hayvan, kan, domuz eti, Allah'tan başkasının adı anılarak kesilen, boğularak ölmüş, vurularak ölmüş, yuvarlanarak ölmüş, boynuzlanarak ölmüş ve yırtıcı hayvanın yediği, kesip temizledikleriniz dışında, dikili taşlar üzerinde boğazlanan ve fal oklarıyla kısmet aramanız size haram kılındı. Bunlar yoldan çıkmaktır. Bugün inkâr edenler dininizden ümit kesti; öyleyse onlardan korkmayın, benden korkun. Bugün dininizi sizin için tamamladım, üzerinizdeki nimetimi tamamladım ve sizin için din olarak İslâm'ı beğendim. Kim günaha meyletmeksizin açlık içinde zorda kalırsa, şüphesiz Allah bağışlayandır, merhamet edendir.",
 4: "Sana kendileri için neyin helâl kılındığını soruyorlar. De ki: 'Size temiz şeyler helâl kılındı; yırtıcı hayvanlardan, Allah'ın size öğrettiğinden onlara öğreterek avcı olarak eğittiklerinizin avı da.' Onların sizin için tuttuklarından yiyin ve üzerine Allah'ın adını anın. Allah'tan sakının. Şüphesiz Allah hesabı çabuk görendir.",
}

T3 = ("muhatap 2MP (adsız; ''aleykum', 'zekkeytum', 'testaqsimû', 'dînikum', 'taxşevhum', 'xşevni', 'lekum', 'dînekum'); "
      "'hurrimet' faili (adsız; edilgen, 1. kelime; nâib fâil 'el-meyte' ve atıfları); "
      "'uhille' faili (adsız; edilgen, 8. kelime; nâib fâil 'bihî'); Allah (lafız); 'es-sebu'' ('ekele' faili; belirli, 18. kelime); "
      "'zubiha' faili (adsız; edilgen, 23. kelime; nâib fâil zamir 3MS — gönderge 'mâ'); 'ellezîne keferû' ('ye'ise' faili, 33-34. kelime); "
      "konuşan 1S (adsız; 'xşevni', 'ekmeltu', 'etmemtu', 'ni'metî', 'radîtu'); "
      "'idturra' faili (adsız; edilgen, 52. kelime; nâib fâil zamir 3MS — gönderge 'men')")
T4 = ("'yes'elûneke' faili 3MP (adsız; 1. kelime); muhatap 2MS (adsız; 'yes'elûneke', 'qul'); "
      "'uhille' faili (adsız; edilgen, 3. kelime; nâib fâil 'mâzâ'); "
      "söz içi muhatap 2MP (adsız; 'lekum', ''allemtum', 'tu'allimûne', ''allemekum'); "
      "'uhille' faili (adsız; edilgen, 6. kelime; nâib fâil 'et-tayyibât'); Allah (lafız); "
      "'emsekne' faili 3FP (adsız; 20. kelime — gönderge 'el-cevârih'); "
      "söz dışı muhatap 2MP (adsız; 'kulû', ''aleykum', 'zkurû', 'ttequ')")

D = {}
D[3] = ("◇ 'hurrimet 'aleykumu'l-meytetu ve'd-demu ve lahmu'l-xinzîri ve mâ uhille li-ğayri'llâhi bihî ve'l-munxaniqatu ve'l-mevqûzetu ve'l-muteraddiyetu ve'n-natîhatu ve mâ ekele's-sebu'u illâ mâ zekkeytum ve mâ zubiha 'ale'n-nusubi ve en testaqsimû bi'l-ezlâmi zâlikum fisquni'l-yevme ye'ise'llezîne keferû min dînikum fe-lâ taxşevhum va'xşevni'l-yevme ekmeltu lekum dînekum ve etmemtu 'aleykum ni'metî ve radîtu lekumu'l-islâme dînen fe-meni'dturra fî maxmasatin ğayra mutecânifin li-ismin fe-inna'llâhe ğafûrun rahîm' — "
 "edilgen PERF 3FS II. bab + ''alâ' + 2MP + belirli 'meyte' + 've' + belirli 'dem' + 've' + 'lahm' + belirli 'xinzîr' + 've' + 'mâ' + edilgen PERF 3MS IV. bab + 'li' + 'ğayr' + lafız + 'bi' + 3MS + 've' + belirli etken ortaç 'munxaniqa' + 've' + belirli edilgen ortaç 'mevqûze' + 've' + belirli etken ortaç 'muteraddiye' + 've' + belirli 'natîha' + 've' + 'mâ' + PERF 3MS I. bab + belirli 'sebu'' + 'illâ' + 'mâ' + PERF 2MP II. bab + 've' + 'mâ' + edilgen PERF 3MS I. bab + ''alâ' + belirli 'nusub' + 've' + 'en' + IMPF 2MP X. bab + 'bi' + belirli çoğul 'ezlâm' + 'zâlikum' + nekre 'fisq' + belirli 'yevm' + PERF 3MS I. bab + 'ellezî' + PERF 3MP I. bab + 'min' + 'dîn' + 2MP + 'fe' + 'lâ' + IMPF 2MP I. bab + 3MP + 've' + IMPV 2MP I. bab + 1S + belirli 'yevm' + PERF 1S IV. bab + 'li' + 2MP + 'dîn' + 2MP + 've' + PERF 1S IV. bab + ''alâ' + 2MP + 'ni'me' + 1S + 've' + PERF 1S I. bab + 'li' + 2MP + belirli masdar özel ad 'islâm' + nekre 'dîn' + 'fe' + 'men' + edilgen PERF 3MS VIII. bab + 'fî' + nekre 'maxmasa' + 'ğayr' + nekre etken ortaç 'mutecânif' + 'li' + nekre 'ism' + 'fe' + 'inne' + lafız + nekre 'ğafûr' + nekre 'rahîm' "
 "(ölçüm edim emir, yasak, şart, kip COND 1 · IMPV 1 · PRO 1, biçim ISTISNA + NEHY + QASEM; 1S 8 · 2MP 14 · 3FS 1 · 3MP 3 · 3MS 6; bab I. bab ×7 · II. bab ×2 · IV. bab ×3 · VIII. bab ×1 · X. bab ×1). "
 "Allah lafzı 10. ve 59. sırada (ölçüm allah z=0,13); Rab yok; ölçüm esmâ '{{1|غَفُور 60\\. sırada, SON konum, MÜHÜR \\| رَحِيم 61\\. sırada, SON konum, MÜHÜR}}' — satır aynen; esma_kayit çıktısı 'mühür EVET (ÇİFT) ton cemâl' (uyuşuyor) — 'fe-inna'llâhe ğafûrun rahîm', kural ''inne/enne' haberi → ilahi' (lafzın haberi); kural ''inne/enne' haberi → ilahi' (lafzın haberi) (okuma); ölçüm aktör '{{1|adlı إِسْلام 49\\. sırada \\(cins, rol meful\\)}}' — satır aynen. "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=61 (n z=5,16); ölçüm '{{1|biçim ISTISNA \\+ NEHY \\+ QASEM}}' — satır aynen; ölçüm '{{1|fâsıla رحيم → م, N sınıfı — KAFİYE KIRILMASI}}' — satır aynen; ölçüm '{{1|EDİLGEN 4/14 fiil, pas z=1,30}}' — satır aynen; ölçüm '{{1|HAPAKS: خنق}}' — satır aynen (hapaks z=13,81; dört hapaks kökün karşılığı bu blokta eklendi); ölçüm '{{1|sayı işareti سَبُع}}' — satır aynen; ölçüm '{{1|simetri \\[3, 7, 53, 1\\]}}' — satır aynen; ölçüm '{{1|harf 289 → harf3 276, isaret 13}}' — satır aynen; ölçüm '{{1|dış düğüm 3}}' — satır aynen. "
 "Ölçüm COND 1: 'men' (51. kelime); IMPV 1: 'xşevni' (39. kelime); PRO 1: 'lâ' (37. kelime) (okuma); ölçüm biçim ISTISNA + NEHY + QASEM — 'illâ' (19. kelime, morph EXP) istisnası ve 'fe-lâ taxşevhum' yasağı; QASEM etiketinin karşılığı olan kasem edatı yok; D2'de yazılmadı (okuma); edilgen 'hurrimet' (1. kelime), 'uhille' (8. kelime), 'zubiha' (23. kelime), 'dturra' (52. kelime) (okuma); "
 "'el-munxaniqatu' (12. kelime), 'el-muteraddiyetu' (14. kelime) ve 'mutecânifin' (56. kelime) morph ACT_PCPL, 'el-mevqûzetu' (13. kelime) PASS_PCPL — ortaç, bab ◇'de yazılmadı; 'el-islâme' (49. kelime) morph VN IV. bab — masdar, bab ◇'de yazılmadı (okuma). "
 "Kök ikilemeleri (ölçüm) أله ×2: lafız 10. ve 59. kelimede; خشي ×2: 'taxşevhum' (38. kelime) / 'xşevni' (39. kelime); دين ×3: 'dînikum' (36. kelime), 'dînekum' (43. kelime), 'dînen' (50. kelime); غير ×2: 'li-ğayri' (9. kelime) / 'ğayra' (55. kelime); يوم ×2: 'el-yevme' (31. ve 40. kelime) (okuma). "
 "'ve'd-demu' (4.), 've lahmu' (5.), 've mâ' (7., 16., 22.), 've'l-munxaniqatu' (12.), 've'l-mevqûzetu' (13.), 've'l-muteraddiyetu' (14.), 've'n-natîhatu' (15.), 've en' (26.), 'va'xşevni' (39.), 've etmemtu' (44.) ve 've radîtu' (47.)'daki 've' morph CONJ; 'fe-lâ' (37.) ve 'fe-meni' (51.)'deki 'fe' REM; 'fe-inna' (58.)'daki 'fe' RSLT (okuma). "
 + T3 + " (okuma). "
 + cumle(say('say 5:3 1-3', "hurrimet 'aleykumu'l-meyte", True), say('lem 5:3:1', "harrame"), say('say 5:3 3-6', "el-meytetu ve'd-demu ve lahmu'l-xinzîr"), say('say 5:3 5-6 --on', "ve lahmu'l-xinzîr")) + ' '
 + cumle(say('say 5:3 7-11 --on', "ve mâ uhille li-ğayri'llâhi bih", True), say('say 5:3 8-11', "uhille li-ğayri'llâhi bih"), say('lem 5:3:8', "uhille"), say('lem 5:3:12', "munxaniqa"), say('lem 5:3:13', "mevqûze"), say('lem 5:3:14', "muteraddiye"), say('lem 5:3:15', "natîha")) + ' '
 + cumle(say('say 5:3 16-18 --on', "ve mâ ekele's-sebu'", True), say('lem 5:3:18', "sebu'"), say('say 5:3 19-21', "illâ mâ zekkeytum"), say('lem 5:3:21', "zekkey"), say('say 5:3 22-25 --on', "ve mâ zubiha 'ale'n-nusub"), say('lem 5:3:25', "nusub")) + ' '
 + cumle(say('say 5:3 26-28 --on', "ve en testaqsimû bi'l-ezlâm", True), say('lem 5:3:28', "ezlâm"), say('say 5:3 29-30', "zâlikum fisq")) + ' '
 + cumle(say('say 5:3 31-34', "el-yevme ye'ise'llezîne keferû", True), say('say 5:3 33-35', "llezîne keferû min"), say('say 5:3 33-36', "llezîne keferû min dînikum"), say('say 5:3 37-39 --on', "fe-lâ taxşevhum va'xşevn"), say('say 5:3 38-39', "taxşevhum va'xşevn"), say('dizi 5 3 38 39', "xaşiye xaşiye")) + ' '
 + cumle(say('say 5:3 40-43', "el-yevme ekmeltu lekum dînekum", True), say('lem 5:3:41', "ekmel"), say('say 5:3 44-46 --on', "ve etmemtu 'aleykum ni'metî"), say('say 5:3 47-50 --on', "ve radîtu lekumu'l-islâme dînâ"), say('lem 5:3:49', "islâm")) + ' '
 + cumle(say('say 5:3 51-52 --on', "fe-meni'dturr", True), say('say 5:3 51-54 --on', "fe-meni'dturra fî maxmasa"), say('lem 5:3:54', "maxmasa"), say('say 5:3 55-57', "ğayra mutecânifin li-ism"), say('lem 5:3:56', "mutecânif")) + ' '
 + cumle(say('say 5:3 58-61 --on', "fe-inna'llâhe ğafûrun rahîm", True), say('say 5:3 59-61', "llâhe ğafûrun rahîm"), say('dizi 5 3 59 61', "allâh ğafûr rahîm")) + ' '
 "Ölçüm xref 2:173 ve 16:115 (basılmış), okunmuş bir ayet. Ölçüm nakarat3 iki kalıp: bir kalıp süzgeç GEÇER, bir kalıp süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'fe-lâ taxşevhum' / 'va'xşevni'; 'hurrimet 'aleykum' / 'illâ mâ zekkeytum' — ayetler arası: 5:3 / 5:4 ('hurrimet 'aleykum' / 'uhille lekum').",
 "◈K — K2 'el-yevme' (31. ve 40. kelime).",
 "◈B — B1 —; B2 —; B3 —; B4 'el-meytetu' (3. kelime).",
 "◈D — D1 PERF + ''alâ' + belirli + 've' + belirli + 've' + izafet + belirli + 've' + 'mâ' + PERF + 'li' + izafet + lafız + 'bi' + 've' + belirli + 've' + belirli + 've' + belirli + 've' + belirli + 've' + 'mâ' + PERF + belirli + 'illâ' + 'mâ' + PERF + 've' + 'mâ' + PERF + ''alâ' + belirli + 've' + 'en' + IMPF + 'bi' + belirli + 'zâlikum' + nekre + belirli + PERF + 'ellezî' + PERF + 'min' + izafet + 'fe' + 'lâ' + IMPF + 've' + IMPV + belirli + PERF + 'li' + izafet + 've' + PERF + ''alâ' + izafet + 've' + PERF + 'li' + belirli + nekre + 'fe' + 'men' + PERF + 'fî' + nekre + izafet + nekre + 'li' + nekre + 'fe' + 'inne' + lafız + nekre + nekre; D2 emir, yasak, şart, COND ('men' 51. kelime), IMPV ('xşevni' 39. kelime), PRO ('lâ' 37. kelime); D3 أله ×2 · خشي ×2 · دين ×3 · غير ×2 · يوم ×2; 2:150, 2:173, 2:185, 3:19, 3:85, 9:120, 16:115 ve 70:43 eşleri; D4 1S 8 · 2MP 14 · 3FS 1 · 3MP 3 · 3MS 6, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T3 + "; ölçüm aktör '{{1|adlı إِسْلام 49\\. sırada \\(cins, rol meful\\)}}'; A2 haram kılma; ölü hayvan; kan; domuz eti; başkası adına kesme; boğulma; vurulma; yuvarlanma; boynuzlanma; yırtıcının yemesi; kesip temizleme; dikili taş; fal okları; yoldan çıkma; ümit kesme; korkma; dini tamamlama; nimeti tamamlama; razı olma; zorda kalma; açlık; günaha meyletme; bağışlama; merhamet; A3 —; A4 " + BOLUM + "; edim geçişi emir, yasak, nida → emir, yasak, şart (ayetler arası); şahıs geçişi yok; şart → cevap (ayet içi; COND 'men' 51. kelime: 'fe-meni'dturra fî maxmasatin' / 'fe-inna'llâhe ğafûrun rahîm' (58. kelime)).",
)

D[4] = ("◇ 'yes'elûneke mâzâ uhille lehum qul uhille lekumu't-tayyibâtu ve mâ 'allemtum mine'l-cevârihi mukellibîne tu'allimûnehunne mimmâ 'allemekumu'llâhu fe-kulû mimmâ emsekne 'aleykum ve'zkuru'sma'llâhi 'aleyhi ve'ttequ'llâhe inna'llâhe serî'u'l-hisâb' — "
 "IMPF 3MP I. bab + 2MS + 'mâzâ' + edilgen PERF 3MS IV. bab + 'li' + 3MP + IMPV 2MS I. bab + edilgen PERF 3MS IV. bab + 'li' + 2MP + belirli çoğul 'tayyibe' + 've' + 'mâ' + PERF 2MP II. bab + 'min' + belirli çoğul 'cevârih' + çoğul etken ortaç 'mukellib' + IMPF 2MP II. bab + 3FP + 'min' + 'mâ' + PERF 3MS II. bab + 2MP + lafız + 'fe' + IMPV 2MP I. bab + 'min' + 'mâ' + PERF 3FP IV. bab + ''alâ' + 2MP + 've' + IMPV 2MP I. bab + 'ism' + lafız + ''alâ' + 3MS + 've' + IMPV 2MP VIII. bab + lafız + 'inne' + lafız + 'serî'' + belirli masdar 'hisâb' "
 "(ölçüm edim soru, emir, kip IMPV 4 · INTG 1; 2MP 13 · 2MS 2 · 3FP 3 · 3MP 3 · 3MS 4; bab I. bab ×4 · II. bab ×3 · IV. bab ×3 · VIII. bab ×1). "
 "Allah lafzı 17., 24., 27. ve 29. sırada (ölçüm allah z=2,05); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=31 (n z=1,97); ölçüm '{{2|fâsıla ٱلحساب → ب, ب sınıfı — KAFİYE KIRILMASI}}' — satır aynen; ölçüm '{{2|EDİLGEN 2/11 fiil, pas z=0,71}}' — satır aynen; ölçüm '{{2|simetri \\[3, 2, 7, 1\\]}}' — satır aynen; ölçüm '{{2|harf 144 → harf3 136, isaret 8}}' — satır aynen; ölçüm '{{2|dış düğüm 9}}' — satır aynen. "
 "Ölçüm IMPV 4: 'qul' (5. kelime), 'kulû' (18. kelime), 'zkurû' (22. kelime), 'ttequ' (26. kelime); INTG 1: 'mâzâ' (2. kelime) (okuma); edilgen 'uhille' (3. ve 6. kelime) (okuma); 'mukellibîne' (13. kelime) morph ACT_PCPL II. bab — ortaç, bab ◇'de yazılmadı; 'el-hisâb' (31. kelime) morph VN III. bab — masdar, bab ◇'de yazılmadı (okuma). "
 "Kök ikilemeleri (ölçüm) أله ×4: lafız 17., 24., 27. ve 29. kelimede; حلل ×2: 'uhille' (3. ve 6. kelime); علم ×3: ''allemtum' (10. kelime), 'tu'allimûnehunne' (14. kelime), ''allemekumu' (16. kelime) (okuma). "
 "'ve mâ' (9.), 've'zkurû' (22.) ve 've'ttequ' (26.)'daki 've' morph CONJ; 'fe-kulû' (18.)'daki 'fe' REM (okuma). "
 + T4 + " (okuma). "
 + cumle(say('say 5:4 1-2', "yes'elûneke mâzâ", True), say('say 5:4 1-4', "yes'elûneke mâzâ uhille lehum"), say('say 5:4 3-4', "uhille lehum"), say('lem 5:4:3', "ehalle")) + ' '
 + cumle(say('say 5:4 5-8', "qul uhille lekumu't-tayyibât", True), say('say 5:4 6-8', "uhille lekumu't-tayyibât"), say('say 5:4 7-8', "lekumu't-tayyibât")) + ' '
 + cumle(say('say 5:4 9-12 --on', "ve mâ 'allemtum mine'l-cevârih", True), say('lem 5:4:12', "cevârih"), say('lem 5:4:13', "mukellib"), say('say 5:4 14-17', "tu'allimûnehunne mimmâ 'allemekumu'llâh"), say('say 5:4 15-17', "mimmâ 'allemekumu'llâh")) + ' '
 + cumle(say('say 5:4 18-21 --on', "fe-kulû mimmâ emsekne 'aleykum", True), say('say 5:4 18-19 --on', "fe-kulû mimmâ"), say('say 5:4 22-24 --on', "ve'zkuru'sma'llâh"), say('say 5:4 22-25 --on', "ve'zkuru'sma'llâhi 'aleyh"), say('dizi 5 4 22 24', "zekera ism allâh")) + ' '
 + cumle(say('say 5:4 26-28 --on', "ve'ttequ'llâhe inne", True), say('dizi 5 4 26 28', "itteqâ allâh inne"), say('say 5:4 26-29 --on', "ve'ttequ'llâhe inna'llâh"), say('say 5:4 28-31', "inna'llâhe serî'u'l-hisâb"), say('say 5:4 30-31', "serî'u'l-hisâb")) + ' '
 "Ölçüm xref 3:19, 22:28, 22:34 ve 22:36 (basılmış), okunmuş bir ayet, okunmamış dört ayet. Ölçüm nakarat3 üç kalıp: ikisi süzgeç GEÇER, biri GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: 5:3 / 5:4 ('hurrimet 'aleykum' / 'uhille lekum').",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPF + 'mâzâ' + PERF + 'li' + IMPV + PERF + 'li' + belirli + 've' + 'mâ' + PERF + 'min' + belirli + çoğul + IMPF + 'min' + 'mâ' + PERF + lafız + 'fe' + IMPV + 'min' + 'mâ' + PERF + ''alâ' + 've' + IMPV + izafet + lafız + ''alâ' + 've' + IMPV + lafız + 'inne' + lafız + izafet + belirli; D2 soru, emir, IMPV ('qul' 5. kelime, 'kulû' 18. kelime, 'zkurû' 22. kelime, 'ttequ' 26. kelime), INTG ('mâzâ' 2. kelime); D3 أله ×4 · حلل ×2 · علم ×3; 3:19, 3:199, 14:51, 22:28, 22:34, 22:36 ve 40:17 eşleri; 5:1 ve 5:2 sûre içi eşleri; D4 2MP 13 · 2MS 2 · 3FP 3 · 3MP 3 · 3MS 4, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T4 + "; aktör yok (ölçüm); A2 soru; helâl kılma; temiz şeyler; öğretme; avcı hayvanlar; yeme; tutma; anma; sakınma; hesap; A3 helâl kılınanlar — temiz şeyler ve eğitilmiş avcı hayvanların avı (söz içi, 6-17. kelime); A4 " + BOLUM + "; bölüm kapanışı; edim geçişi emir, yasak, şart → soru, emir (ayetler arası); şahıs geçişi yok; soru → cevap (ayet içi; 'yes'elûneke' / 'qul'); söz açılır; söz kapanır (17. kelime, ayet içi).",
)

out = ['# ── blok 5:3-4 (2026-11-15) ──', 'MEAL2 = {']
for n in range(3, 5):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M2 = {']
for n in range(3, 5):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL2); M.update(M2)']
open('/home/claude/yamalar/metin_5_3_4.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
