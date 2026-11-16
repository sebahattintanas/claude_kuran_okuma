# blok 15 (5:42-44) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b15/say2.txt'
os.environ['OLC'] = '/home/claude/b15/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Küfürde yarışanlar; Tevrat, İncil ve Kitap ile hüküm' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 42: "Onlar yalana çokça kulak verenler, haramı çokça yiyenlerdir. Sana gelirlerse aralarında hüküm ver ya da onlardan yüz çevir. Onlardan yüz çevirirsen sana hiçbir şeyle zarar veremezler. Hüküm verirsen aralarında adaletle hüküm ver. Şüphesiz Allah adaletli davrananları sever.",
 43: "Yanlarında içinde Allah'ın hükmü bulunan Tevrat varken seni nasıl hakem yaparlar? Sonra bunun ardından yüz çevirirler. Onlar inananlar değildir.",
 44: "Şüphesiz Tevrat'ı biz indirdik; onda hidayet ve nur vardır. Teslim olmuş nebiler Yahudi olanlara onunla hüküm verirlerdi; rabbaniler ve âlimler de Allah'ın kitabından korumakla görevlendirildikleri şeyle hüküm verirlerdi ve onun üzerine şahitlerdi. Artık insanlardan korkmayın, benden korkun ve âyetlerimi az bir bedelle satmayın. Kim Allah'ın indirdiğiyle hüküm vermezse, işte onlar kâfirlerin ta kendileridir.",
}

T42 = ("'semmâ'ûne' ve 'ekkâlûne' (mübteda takdirli haber; 1. ve 3. kelime); muhatap 2MS (adsız; 6., 7., 10., 13., 16., 19. ve 20. kelime); 'câ'ûke' faili 3MP (adsız; 6. kelime); 3MP (adsız; 'beynehum' 8. ve 21. kelime, ''anhum' 11. ve 14. kelime); 'yedurrûke' faili 3MP (adsız; 16. kelime); "
       "'şey'â' (nekre; 17. kelime); Allah (lafız; 24. kelime); 'yuhibbu' faili 3MS (adsız; 25. kelime); 'l-muqsitîn' (26. kelime)")
T43 = ("muhatap 2MS (adsız; 'yuhakkimûneke', 2. kelime); 'yuhakkimûneke' faili 3MP (adsız); 3MP (adsız; ''indehumu' 3. kelime); 't-tevrâtu' (adlı aktör — kitap; 4. kelime); 'fîhâ' 3FS (adsız; gönderge 't-tevrâtu', 5. kelime); Allah (lafız; 7. kelime); 'yetevellevne' faili 3MP (adsız; 9. kelime); 'ulâ'ike' (işaret; 14. kelime)")
T44 = ("konuşan 1P (adsız; 'innâ' 1. kelime, 'enzelna' 2. kelime); 't-tevrâte' (adlı aktör — kitap; 3. kelime); 3FS (adsız; 'fîhâ' 4. kelime, 'bihe' 8. kelime; gönderge 't-tevrâte'); 'hudan ve nûr' (nekre; 5-6. kelime); 'yahkumu' faili 3MS (adsız; 7. kelime); 'n-nebiyyûne' (9. kelime); 'llezîne eslemû' (10-11. kelime; 3MP fail — adsız); 'llezîne hâdû' (12-13. kelime; 3MP fail — adsız); "
       "'r-rabbâniyyûne' ve 'l-ahbâru' (14-15. kelime); 'stuhfizû' faili (adsız; edilgen — nâib fâil 3MP, 17. kelime); Allah (lafız; 20. ve 38. kelime); 'kânû' faili 3MP (adsız; 21. kelime); ''aleyhi' 3MS (adsız; 22. kelime); muhatap 2MP (adsız; 25., 27. ve 29. kelime); konuşan 1S (adsız; 27. ve 30. kelime); 'n-nâse' (26. kelime); "
       "'men' (şart ismi; 33. kelime); 'yahkum' faili 3MS (adsız; 35. kelime); 'enzele' faili 3MS (adsız; gönderge lafız, 37. kelime); 'ulâ'ike humu'l-kâfirûn' (39-41. kelime; 'hum' 3MP — adsız)")

D = {}
D[42] = ("◇ 'semmâ'ûne li'l-kezibi ekkâlûne li's-suht fe-in câ'ûke fa'hkum beynehum ev a'rid 'anhum ve in tu'rid 'anhum fe-len yedurrûke şey'â ve in hakemte fa'hkum beynehum bi'l-qist inna'llâhe yuhibbu'l-muqsitîn' — "
 "çoğul 'semmâ'' + 'li' + belirli 'kezib' + çoğul 'ekkâl' + 'li' + belirli 'suht' + 'fe' + 'in' + PERF 3MP I. bab + 2MS + 'fe' + IMPV 2MS I. bab + 'beyn' + 3MP + 'ev' + IMPV 2MS IV. bab + ''an' + 3MP + 've' + 'in' + IMPF 2MS IV. bab + ''an' + 3MP + 'fe' + 'len' + IMPF 3MP I. bab + 2MS + nekre 'şey'' + 've' + 'in' + PERF 2MS I. bab + 'fe' + IMPV 2MS I. bab + 'beyn' + 3MP + 'bi' + belirli 'qist' + 'inne' + lafız + IMPF 3MS IV. bab + belirli çoğul 'muqsit' "
 "(ölçüm edim emir, şart, kip COND 3 · IMPV 3 · NEG 1; 2MS 8 · 3MP 8 · 3MS 1; bab I. bab ×5 · IV. bab ×3). "
 "Allah lafzı 24. sırada (ölçüm allah z=0,24); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=26 (n z=1,44); ölçüm '{{1|fâsıla ٱلمقسطين → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|simetri \\[4, 5, 18, 1\\]}}' — satır aynen; ölçüm '{{1|harf 116 → harf3 111, isaret 5}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen. "
 "Ölçüm COND 3: 'in' (5., 12. ve 18. kelime); IMPV 3: 'fa'hkum' (7. ve 20. kelime), 'a'rid' (10. kelime); NEG 1: 'len' (15. kelime); 'fe-in' (5.)'deki 'fe' REM, 'fa'hkum' (7., 20.) ve 'fe-len' (15.)'deki 'fe' RSLT; 've in' (12., 18.)'deki 've' CONJ; 'ev' (9.) CONJ (okuma). "
 "Kök ikilemesi (ölçüm) حكم ×3: 'fa'hkum' (7. kelime), 'hakemte' (19. kelime), 'fa'hkum' (20. kelime); بين ×2: 'beynehum' (8. ve 21. kelime); عرض ×2: 'a'rid' (10. kelime) / 'tu'rid' (13. kelime); قسط ×2: 'l-qist' (22. kelime) / 'l-muqsitîn' (26. kelime) — adalet ve adaletli davranan (okuma). "
 + T42 + " (okuma). "
 + cumle(say('say 5:42 1-2', "semmâ'ûne li'l-kezib", True), say('say 5:42 1-4', "semmâ'ûne li'l-kezibi ekkâlûne li's-suht"), say('say 5:42 3-4', "ekkâlûne li's-suht"), say('lem 5:42:3', "ekkâl"), say('lem 5:42:4', "suht")) + ' '
 + cumle(say('say 5:42 5-7 --on', "fe-in câ'ûke fa'hkum", True), say('say 5:42 7-8', "fa'hkum beynehum"), say('say 5:42 7-11', "fa'hkum beynehum ev a'rid 'anhum"), say('say 5:42 10-11', "a'rid 'anhum"), say('say 5:42 12-14 --on', "ve in tu'rid 'anhum"), say('say 5:42 15-17 --on', "fe-len yedurrûke şey'â")) + ' '
 + cumle(say('say 5:42 18-19 --on', "ve in hakemte", True), say('say 5:42 20-22', "fa'hkum beynehum bi'l-qist"), say('say 5:42 21-22', "beynehum bi'l-qist"), say('say 5:42 23-25', "inna'llâhe yuhibb"), say('dizi 5 42 23 25', "inne allâh ahbeb"), say('say 5:42 23-26', "inna'llâhe yuhibbu'l-muqsitîn"), say('say 5:42 24-26', "llâhe yuhibbu'l-muqsitîn"), say('dizi 5 42 24 26', "allâh ahbeb muqsit")) + ' '
 "Ölçüm xref 49:9 (emsal olarak basıldı) ve okunmuş başka bir ayet. "
 "Ölçüm nakarat3 kalıbı: 'inna'llâhe yuhibb' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'fa'hkum beynehum' / 'ev a'rid 'anhum' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'semmâ'ûne' (1. kelime); B4 —.",
 "◈D — D1 çoğul + 'li' + belirli + çoğul + 'li' + belirli + 'fe' + 'in' + PERF + 'fe' + IMPV + 'beyn' + 'ev' + IMPV + ''an' + 've' + 'in' + IMPF + ''an' + 'fe' + 'len' + IMPF + nekre + 've' + 'in' + PERF + 'fe' + IMPV + 'beyn' + 'bi' + belirli + 'inne' + lafız + IMPF + belirli; "
 "D2 emir, şart, IMPV ('fa'hkum' 7. ve 20., 'a'rid' 10. kelime), COND ('in' 5., 12. ve 18. kelime), NEG ('len' 15. kelime); D3 حكم ×3, بين ×2, عرض ×2, قسط ×2; 49:9 eşi; D4 2MS 8 · 3MP 8 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T42 + "; aktör yok (ölçüm); A2 yalana kulak verme; haram yeme; hakemlik; yüz çevirme; zarar verememe; adaletle hüküm; Allah'ın sevgisi; A3 —; "
 "A4 " + BOLUM + "; edim geçişi emir, yasak, nida, şart → emir, şart (ayetler arası); şahıs geçişi yok; şart → cevap (ayet içi; COND 'in' 5. kelime: 'fe-in câ'ûke' / 'fa'hkum beynehum ev a'rid 'anhum' (7. kelime)); "
 "şart → cevap (ayet içi; COND 'in' 12. kelime: 've in tu'rid 'anhum' / 'fe-len yedurrûke şey'â' (15. kelime)); şart → cevap (ayet içi; COND 'in' 18. kelime: 've in hakemte' / 'fa'hkum beynehum bi'l-qist' (20. kelime)).",
)

D[43] = ("◇ 've keyfe yuhakkimûneke ve 'indehumu't-tevrâtu fîhâ hukmu'llâhi summe yetevellevne min ba'di zâlik ve mâ ulâ'ike bi'l-mu'minîn' — "
 "'ve' + 'keyfe' + IMPF 3MP II. bab + 2MS + 've' + ''inde' + 3MP + belirli 'tevrâ' + 'fî' + 3FS + 'hukm' + lafız + 'summe' + IMPF 3MP V. bab + 'min' + 'ba'd' + 'zâ' + 'li' + 've' + 'mâ' + 'ulâ' + 'ke' + 'bi' + belirli çoğul 'mu'min' "
 "(ölçüm edim soru, kip INTG 1 · NEG 1; 2MS 1 · 3FS 1 · 3MP 5; bab II. bab ×1 · V. bab ×1). "
 "Allah lafzı 7. sırada (ölçüm allah z=0,81); Rab yok; ölçüm '{{2|esmâ مُؤْمِن 15\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton cemâl' (uyuşmuyor) — 've mâ ulâ'ike bi'l-mu'minîn', kural 'çoğul insan göndergeli → degil' (inananlar) (okuma); ölçüm '{{2|aktör: adlı تَوْراة 4\\. sırada \\(kitab, rol fail\\)}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=15 (n z=0,27); ölçüm '{{2|fâsıla بٱلمؤمنين → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|simetri \\[3, 4, 12, 1\\]}}' — satır aynen; ölçüm '{{2|harf 71 → harf3 68, isaret 3}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm INTG 1: 'keyfe' (1. kelime); NEG 1: 'mâ' (13. kelime; morph NEG, 'kâne' ailesi — haberi 'bi' ile); 've keyfe' (1.) ve 've mâ' (13.)'daki 've' REM; 've 'indehumu' (3.)'daki 've' CIRC; 'summe' (8.) CONJ (okuma). "
 "Kök ikilemesi (ölçüm) حكم ×2: 'yuhakkimûneke' (2. kelime; II. bab, hakem yapma) / 'hukmu' (6. kelime) (okuma). "
 + T43 + " (okuma). "
 + cumle(say('say 5:43 1-2 --on', "ve keyfe yuhakkimûnek", True), say('say 5:43 3-4 --on', "ve 'indehumu't-tevrâh"), say('say 5:43 5-7', "fîhâ hukmu'llâh"), say('say 5:43 6-7', "hukmu'llâh")) + ' '
 + cumle(say('say 5:43 8-9', "summe yetevellevne", True), say('say 5:43 9-12', "yetevellevne min ba'di zâlik"), say('say 5:43 10-12', "min ba'di zâlik"), say('say 5:43 13-15 --on', "ve mâ ulâ'ike bi'l-mu'minîn"), say('say 5:43 14-15', "ulâ'ike bi'l-mu'minîn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'keyfe' + IMPF + 've' + ''inde' + belirli + 'fî' + izafet + lafız + 'summe' + IMPF + 'min' + izafet + 'zâ' + 'li' + 've' + 'mâ' + 'ulâ' + 'ke' + 'bi' + belirli; "
 "D2 soru, INTG ('keyfe' 1. kelime), NEG ('mâ' 13. kelime); D3 حكم ×2; 24:47 eşi; D4 2MS 1 · 3FS 1 · 3MP 5, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T43 + "; ölçüm aktör adlı Tevrat (kitap, fail); A2 hakem yapma; Tevrat'taki hüküm; yüz çevirme; iman etmeme; A3 —; A4 " + BOLUM + "; edim geçişi emir, şart → soru (ayetler arası); şahıs geçişi yok.",
)

D[44] = ("◇ 'innâ enzelna't-tevrâte fîhâ hudan ve nûr yahkumu bihe'n-nebiyyûne'llezîne eslemû li'llezîne hâdû ve'r-rabbâniyyûne ve'l-ahbâru bi-me'stuhfizû min kitâbi'llâhi ve kânû 'aleyhi şuhedâ' fe-lâ taxşevu'n-nâse ve'xşevni ve lâ teşterû bi-âyâtî semenen qalîlâ ve men lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike humu'l-kâfirûn' — "
 "'inne' + 1P + PERF 1P IV. bab + belirli 'tevrâ' + 'fî' + 3FS + nekre 'hudâ' + 've' + nekre 'nûr' + IMPF 3MS I. bab + 'bi' + 3FS + belirli çoğul 'nebiyy' + 'ellezî' + PERF 3MP IV. bab + 'li' + 'ellezî' + PERF 3MP I. bab + 've' + belirli çoğul 'rabbâniyyîn' + 've' + belirli çoğul 'hibr' + 'bi' + 'mâ' + PERF 3MP X. bab (edilgen) + 'min' + 'kitâb' + lafız + 've' + PERF 3MP I. bab + ''alâ' + 3MS + çoğul 'şehîd' + "
 "'fe' + 'lâ' + IMPF 2MP I. bab + belirli 'nâs' + 've' + IMPV 2MP I. bab + 1S + 've' + 'lâ' + IMPF 2MP VIII. bab + 'bi' + çoğul 'âye' + 1S + nekre 'semen' + nekre 'qalîl' + 've' + 'men' + 'lem' + IMPF 3MS I. bab + 'bi' + 'mâ' + PERF 3MS IV. bab + lafız + 'fe' + 'ulâ' + 'ke' + 'hum' + belirli çoğul 'kâfir' "
 "(ölçüm edim emir, yasak, şart, kip COND 1 · IMPV 1 · NEG 1 · PRO 2; 1P 3 · 1S 2 · 2MP 6 · 3FS 2 · 3MP 9 · 3MS 4; bab I. bab ×6 · IV. bab ×3 · VIII. bab ×1 · X. bab ×1). "
 "Allah lafzı 20. ve 38. sırada (ölçüm allah z=0,45); ölçüm Rab 14. sırada (rab z=0,20) — 'r-rabbâniyyûne' (14. kelime, kök ربب), Rab adı değil (okuma); ölçüm '{{3|esmâ نُور 6\\. sırada, ORTA konum, MÜHÜRSÜZ \\| شَهِيد 23\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor) — "
 "'hudan ve nûr', kural 'esmâ adı esmâ dışı göndergeyle → degil' (Tevrat'taki nur); 've kânû 'aleyhi şuhedâ'', kural 'çoğul insan göndergeli → degil' (şahitler) (okuma); ölçüm '{{3|aktör: adlı تَوْراة 3\\. sırada \\(kitab, rol meful\\)}}' — satır aynen. "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=41 (n z=3,04); ölçüm '{{3|biçim NEHY}}' — satır aynen; ölçüm '{{3|EDİLGEN 1/11 fiil, pas z=0,19}}' — satır aynen; ölçüm '{{3|sayı işareti ثَمَن, قَلِيل}}' — satır aynen; ölçüm '{{3|fâsıla ٱلكفرون → ن, N sınıfı}}' — satır aynen; "
 "ölçüm '{{3|simetri \\[4, 1, 36, 1\\]}}' — satır aynen; ölçüm '{{3|harf 206 → harf3 192, isaret 14}}' — satır aynen; ölçüm '{{3|dış düğüm 2}}' — satır aynen. "
 "Ölçüm biçim NEHY — 'fe-lâ taxşevu' (24. kelime, morph PRO) ve 've lâ teşterû' (28. kelime, morph PRO); IMPV 1: 've'xşevni' (27. kelime); COND 1: 'men' (33. kelime); NEG 1: 'lem' (34. kelime); EDİLGEN — 'stuhfizû' (17. kelime) morph PASS (okuma); "
 "'ve nûr' (6.), 've'r-rabbâniyyûne' (14.), 've'l-ahbâru' (15.) ve 've lâ' (28.)'daki 've' CONJ; 've kânû' (21.)'daki 've' CIRC; 've'xşevni' (27.) ve 've men' (33.)'deki 've' REM; 'fe-lâ' (24.)'daki 'fe' REM, 'fe-ulâ'ike' (39.)'daki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) نزل ×2: 'enzelna' (2. kelime; 1P) / 'enzele' (37. kelime; lafız); حكم ×2: 'yahkumu' (7. kelime) / 'yahkum' (35. kelime); خشي ×2: 'taxşevu' (25. kelime) / 'xşevni' (27. kelime) — insanlardan / benden; أله ×2: lafız 20. ve 38. kelime (okuma). "
 + T44 + " (okuma). "
 + cumle(say('say 5:44 1-3', "innâ enzelna't-tevrâh", True), say('say 5:44 2-3', "enzelna't-tevrâh"), say('say 5:44 4-6', "fîhâ hudan ve nûr"), say('say 5:44 5-6', "hudan ve nûr")) + ' '
 + cumle(say('say 5:44 7-9', "yahkumu bihe'n-nebiyyûn", True), say('say 5:44 9-11', "n-nebiyyûne'llezîne eslemû"), say('say 5:44 12-13', "li'llezîne hâdû"), say('say 5:44 14-15', "ve'r-rabbâniyyûne ve'l-ahbâr"), say('lem 5:44:14', "rabbâniyyîn"), say('say 5:44 16-17', "bi-me'stuhfizû")) + ' '
 + cumle(say('say 5:44 18-20', "min kitâbi'llâh", True), say('say 5:44 19-20', "kitâbi'llâh"), say('say 5:44 21-23 --on', "ve kânû 'aleyhi şuhedâ'"), say('say 5:44 24-26 --on', "fe-lâ taxşevu'n-nâs"), say('say 5:44 27-27 --on', "ve'xşevn")) + ' '
 + cumle(say('say 5:44 28-32 --on', "ve lâ teşterû bi-âyâtî semenen qalîlâ", True), say('say 5:44 29-32', "teşterû bi-âyâtî semenen qalîlâ"), say('say 5:44 31-32', "semenen qalîlâ"), say('dizi 5 44 29 32', "işterâ âye semen qalîl")) + ' '
 + cumle(say('say 5:44 33-41 --on', "ve men lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike humu'l-kâfirûn", True), say('say 5:44 34-40', "lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike hum"), say('dizi 5 44 34 40', "lem hakeme mâ enzele allâh zâ _"),
         say('say 5:44 36-38', "bi-mâ enzele'llâh"), say('dizi 5 44 36 38', "mâ enzele allâh"), say('say 5:44 39-41', "fe-ulâ'ike humu'l-kâfirûn"), say('say 5:44 40-41', "humu'l-kâfirûn")) + ' '
 "Ölçüm xref 2:41 (emsal olarak basıldı) ve okunmuş başka bir ayet. "
 "Ölçüm nakarat3 kalıpları: 'lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike hum' süzgeç GEÇER; 'bi-mâ enzele'llâh' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'fe-lâ taxşevu'n-nâse' / 've'xşevni' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'n-nâse' (26. kelime); B2 —; B3 —; B4 —.",
 "◈D — D1 'inne' + PERF + belirli + 'fî' + nekre + 've' + nekre + IMPF + 'bi' + belirli + 'ellezî' + PERF + 'li' + 'ellezî' + PERF + 've' + belirli + 've' + belirli + 'bi' + 'mâ' + PERF + 'min' + izafet + lafız + 've' + PERF + ''alâ' + çoğul + 'fe' + 'lâ' + IMPF + belirli + 've' + IMPV + 've' + 'lâ' + IMPF + 'bi' + izafet + nekre + nekre + 've' + 'men' + 'lem' + IMPF + 'bi' + 'mâ' + PERF + lafız + 'fe' + 'ulâ' + 'ke' + 'hum' + belirli; "
 "D2 emir, yasak, şart, IMPV ('ve'xşevni' 27. kelime), PRO ('lâ' 24. ve 28. kelime), COND ('men' 33. kelime), NEG ('lem' 34. kelime); D3 نزل ×2, حكم ×2, خشي ×2, أله ×2; 2:41 ve 3:79 eşleri; D4 1P 3 · 1S 2 · 2MP 6 · 3FS 2 · 3MP 9 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T44 + "; ölçüm aktör adlı Tevrat (kitap, meful); A2 Tevrat'ın indirilişi; hidayet ve nur; nebilerin, rabbanilerin ve âlimlerin hükmü; kitabı koruma; şahitlik; korkma yasağı; âyetleri satma yasağı; indirilenle hüküm; A3 —; "
 "A4 " + BOLUM + "; edim geçişi soru → emir, yasak, şart (ayetler arası); şahıs geçişi yok; şart → cevap (ayet içi; COND 'men' 33. kelime: 've men lem yahkum bi-mâ enzele'llâh' / 'fe-ulâ'ike humu'l-kâfirûn' (39. kelime)).",
)

out = ['# ── blok 5:42-44 (2026-11-15) ──', 'MEAL15 = {']
for n in range(42, 45):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M15 = {']
for n in range(42, 45):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL15); M.update(M15)']
open('/home/claude/yamalar/metin_5_42_44.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
