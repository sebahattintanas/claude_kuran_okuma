# blok 16 (5:45-47) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b16/say2.txt'
os.environ['OLC'] = '/home/claude/b16/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Küfürde yarışanlar; Tevrat, İncil ve Kitap ile hüküm' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 45: "Onlara orada şunu yazdık: cana can, göze göz, buruna burun, kulağa kulak, dişe diş karşılıktır; yaralar da kısastır. Kim onu sadaka olarak bağışlarsa, bu onun için bir keffarettir. Kim Allah'ın indirdiğiyle hüküm vermezse, işte onlar zalimlerin ta kendileridir.",
 46: "Onların izleri üzerinde, önündeki Tevrat'ı doğrulayıcı olarak Meryem oğlu İsa'yı ardlarından gönderdik; ona da içinde hidayet ve nur bulunan, önündeki Tevrat'ı doğrulayıcı, sakınanlar için hidayet ve öğüt olan İncil'i verdik.",
 47: "İncil ehli, Allah'ın onda indirdiğiyle hüküm versin. Kim Allah'ın indirdiğiyle hüküm vermezse, işte onlar fâsıkların ta kendileridir.",
}

T45 = ("konuşan 1P (adsız; 'ketebnâ' 1. kelime); ''aleyhim' 3MP (adsız; 2. kelime); 'fîhâ' 3FS (adsız; gönderge Tevrat, 3. kelime); 'qısâs' (nekre; 16. kelime); 'men' (şart ismi; 17. ve 23. kelime); 'tesaddeqa' faili 3MS (adsız; 18. kelime); 'bihî' 3MS (adsız; 19. kelime); 'fe-huve' 3MS (adsız; 20. kelime); 'keffâratun' (nekre; 21. kelime); "
       "'leh' 3MS (adsız; 22. kelime); 'yahkum' faili 3MS (adsız; 25. kelime); 'enzele' faili 3MS (adsız; gönderge lafız, 27. kelime); Allah (lafız; 28. kelime); 'ulâ'ike humu'z-zâlimûn' (29-31. kelime; 'hum' 3MP — adsız)")
T46 = ("konuşan 1P (adsız; 'qaffeynâ' 1. kelime, 'âteynâhu' 13. kelime); 'âsârihim' 3MP (adsız; 3. kelime); ''îsa'bni meryeme' (adlı aktör — kişi; 4-6. kelime); 'yedeyhi' 3MS (adsız; 10. ve 21. kelime); 'âteynâhu' mef'ûlü 3MS (adsız; 13. kelime); 'l-incîle' (adlı aktör — kitap; 14. kelime); 'fîhi' 3MS (adsız; gönderge 'l-incîle', 15. kelime); "
       "'t-tevrâh' (adlı aktör — kitap; 12. ve 23. kelime); 'hudan ve nûrun' (nekre; 16-17. kelime); 'musaddiqan' (nekre; 7. ve 18. kelime); 'hudan ve mev'izatan' (nekre; 24-25. kelime); 'l-muttaqîn' (26. kelime)")
T47 = ("'ehlu'l-incîl' (adlı aktör — kitap; 'l-yahkum' faili, 2-3. kelime); 'l-yahkum' 3MS (adsız; emir; 1. kelime); 'enzele' faili 3MS (adsız; gönderge lafız, 5. ve 12. kelime); Allah (lafız; 6. ve 13. kelime); 'fîh' 3MS (adsız; gönderge 'l-incîl', 7. kelime); 'men' (şart ismi; 8. kelime); 'yahkum' faili 3MS (adsız; 10. kelime); 'ulâ'ike humu'l-fâsiqûn' (14-16. kelime; 'hum' 3MP — adsız)")

D = {}
D[45] = ("◇ 've ketebnâ 'aleyhim fîhâ enne'n-nefse bi'n-nefsi ve'l-'ayne bi'l-'ayni ve'l-enfe bi'l-enfi ve'l-uzune bi'l-uzuni ve's-sinne bi's-sinni ve'l-curûha qısâs fe-men tesaddeqa bihî fe-huve keffâratun leh ve men lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike humu'z-zâlimûn' — "
 "'ve' + PERF 1P I. bab + ''alâ' + 3MP + 'fî' + 3FS + 'enne' + belirli 'nefs' + 'bi' + belirli 'nefs' + 've' + belirli ''ayn' + 'bi' + belirli ''ayn' + 've' + belirli 'enf' + 'bi' + belirli 'enf' + 've' + belirli 'uzun' + 'bi' + belirli 'uzun' + 've' + belirli 'sinn' + 'bi' + belirli 'sinn' + 've' + belirli çoğul 'curûh' + nekre 'qısâs' + "
 "'fe' + 'men' + PERF 3MS V. bab + 'bi' + 3MS + 'fe' + 'huve' + nekre 'keffâra' + 'li' + 3MS + 've' + 'men' + 'lem' + IMPF 3MS I. bab + 'bi' + 'mâ' + PERF 3MS IV. bab + lafız + 'fe' + 'ulâ' + 'ke' + 'hum' + belirli çoğul 'zâlim' "
 "(ölçüm edim şart, kip COND 2 · NEG 1; 1P 2 · 3FS 1 · 3MP 2 · 3MS 6; bab I. bab ×2 · IV. bab ×1 · V. bab ×1). "
 "Allah lafzı 28. sırada (ölçüm allah z=0,12); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=31 (n z=1,97); ölçüm '{{1|fâsıla ٱلظلمون → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|simetri \\[4, 2, 22, 1\\]}}' — satır aynen; ölçüm '{{1|harf 146 → harf3 139, isaret 7}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm COND 2: 'men' (17. ve 23. kelime); NEG 1: 'lem' (24. kelime); 've ketebnâ' (1.), 've'l-'ayne' (7.), 've'l-enfe' (9.), 've'l-uzune' (11.), 've's-sinne' (13.), 've'l-curûha' (15.) ve 've men' (23.)'deki 've' CONJ; 'fe-men' (17.)'deki 'fe' REM, 'fe-huve' (20.) ve 'fe-ulâ'ike' (29.)'daki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) نفس ×2 ('n-nefse' 5. / 'n-nefsi' 6. kelime), عين ×2 (7. / 8. kelime), أنف ×2 (9. / 10. kelime), أذن ×2 (11. / 12. kelime), سنن ×2 (13. / 14. kelime) — beş organ çifti 'bi' ile (karşılık) (okuma). "
 + T45 + " (okuma). "
 + cumle(say('say 5:45 1-3 --on', "ve ketebnâ 'aleyhim fîhâ", True), say('say 5:45 4-6', "enne'n-nefse bi'n-nefs"), say('say 5:45 5-6', "n-nefse bi'n-nefs"), say('say 5:45 7-8 --on', "ve'l-'ayne bi'l-'ayn"), say('say 5:45 9-10 --on', "ve'l-enfe bi'l-enf"), say('say 5:45 11-12 --on', "ve'l-uzune bi'l-uzun"), say('say 5:45 13-14 --on', "ve's-sinne bi's-sinn")) + ' '
 + cumle(say('say 5:45 15-16 --on', "ve'l-curûha qısâs", True), say('lem 5:45:16', "qısâs"), say('say 5:45 17-19 --on', "fe-men tesaddeqa bih"), say('say 5:45 20-22 --on', "fe-huve keffâratun leh"), say('lem 5:45:21', "keffâra")) + ' '
 + cumle(say('say 5:45 23-31 --on', "ve men lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike humu'z-zâlimûn", True), say('say 5:45 23-30 --on', "ve men lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike hum"), say('dizi 5 45 23 30', "men lem hakeme mâ enzele allâh zâ _"), say('say 5:45 24-30', "lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike hum"), say('dizi 5 45 24 30', "lem hakeme mâ enzele allâh zâ _"),
         say('say 5:45 26-28', "bi-mâ enzele'llâh"), say('dizi 5 45 26 28', "mâ enzele allâh"), say('say 5:45 29-31', "fe-ulâ'ike humu'z-zâlimûn"), say('say 5:45 30-31', "humu'z-zâlimûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: 've men lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike hum', 'lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike hum' ve 'bi-mâ enzele'llâh' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'l-'ayne' (7. kelime), 'l-'ayni' (8. kelime); B4 —.",
 "◈D — D1 've' + PERF + ''alâ' + 'fî' + 'enne' + belirli + 'bi' + belirli + 've' + belirli + 'bi' + belirli + 've' + belirli + 'bi' + belirli + 've' + belirli + 'bi' + belirli + 've' + belirli + 'bi' + belirli + 've' + belirli + nekre + 'fe' + 'men' + PERF + 'bi' + 'fe' + 'huve' + nekre + 'li' + 've' + 'men' + 'lem' + IMPF + 'bi' + 'mâ' + PERF + lafız + 'fe' + 'ulâ' + 'ke' + 'hum' + belirli; "
 "D2 şart, COND ('men' 17. ve 23. kelime), NEG ('lem' 24. kelime); D3 نفس ×2, عين ×2, أنف ×2, أذن ×2, سنن ×2; 2:178 eşi; D4 1P 2 · 3FS 1 · 3MP 2 · 3MS 6, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T45 + "; aktör yok (ölçüm); A2 Tevrat'ta yazılan kısas; can, göz, burun, kulak, diş; yaralar; sadaka; keffaret; indirilenle hüküm; zulüm; A3 —; "
 "A4 " + BOLUM + "; edim geçişi emir, yasak, şart → şart (ayetler arası); şahıs geçişi yok; şart → cevap (ayet içi; COND 'men' 17. kelime: 'fe-men tesaddeqa bih' / 'fe-huve keffâratun leh' (20. kelime)); şart → cevap (ayet içi; COND 'men' 23. kelime: 've men lem yahkum bi-mâ enzele'llâh' / 'fe-ulâ'ike humu'z-zâlimûn' (29. kelime)).",
)

D[46] = ("◇ 've qaffeynâ 'alâ âsârihim bi-'îsa'bni meryeme musaddiqan li-mâ beyne yedeyhi mine't-tevrâh ve âteynâhu'l-incîle fîhi hudan ve nûrun ve musaddiqan li-mâ beyne yedeyhi mine't-tevrâti ve hudan ve mev'izatan li'l-muttaqîn' — "
 "'ve' + PERF 1P II. bab + ''alâ' + çoğul 'eser' + 3MP + 'bi' + ''îsâ' + 'ibn' + 'meryem' + nekre ortaç 'musaddiq' + 'li' + 'mâ' + 'beyn' + ikil 'yed' + 3MS + 'min' + belirli 'tevrâ' + 've' + PERF 1P IV. bab + 3MS + belirli 'incîl' + 'fî' + 3MS + nekre 'hudâ' + 've' + nekre 'nûr' + 've' + nekre ortaç 'musaddiq' + 'li' + 'mâ' + 'beyn' + ikil 'yed' + 3MS + 'min' + belirli 'tevrâ' + 've' + nekre 'hudâ' + 've' + nekre 'mev'iza' + 'li' + belirli çoğul 'muttaqî' "
 "(ölçüm edim haber, kip yok; 1P 4 · 3MP 1 · 3MS 4; bab II. bab ×1 · IV. bab ×1). "
 "Ölçüm '{{2|lafız YOK · Rab YOK}}' — satır aynen; ölçüm '{{2|esmâ نُور 17\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor) — 'hudan ve nûrun', kural 'esmâ adı esmâ dışı göndergeyle → degil' (İncil'deki nur) (okuma); "
 "ölçüm '{{2|aktör: adlı عِيسَى 4\\. sırada \\(kisi, rol mecrur\\)}}', '{{2|adlı مَرْيَم 6\\. sırada \\(kisi, rol mecrur\\)}}', '{{2|adlı إِنجِيل 14\\. sırada \\(kitab, rol meful\\)}}' — satır aynen; Tevrat 12. ve 23. sırada (kitap, mecrur). "
 "Ölçüm 'yıldız yok' — satır aynen; n=26 (n z=1,44); ölçüm '{{2|fâsıla للمتقين → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|simetri \\[10, 4, 15, 3\\]}}' — satır aynen; ölçüm '{{2|harf 124 → harf3 117, isaret 7}}' — satır aynen; ölçüm '{{2|dış düğüm 3}}' — satır aynen. "
 "'ve qaffeynâ' (1.), 've âteynâhu' (13.), 've nûrun' (17.), 've musaddiqan' (18.), 've hudan' (24.) ve 've mev'izatan' (25.)'daki 've' morph CONJ (okuma). "
 "Kök ikilemesi (ölçüm) صدق ×2 ('musaddiqan' 7. ve 18. kelime), بين ×2 (9. ve 20. kelime), يدي ×2 ('yedeyhi' 10. ve 21. kelime), هدي ×2 ('hudan' 16. ve 24. kelime) — 'musaddiqan li-mâ beyne yedeyhi mine't-tevrâh' ayet içinde İsa ve İncil için tekrarlanıyor (okuma). "
 + T46 + " (okuma). "
 + cumle(say('say 5:46 1-4 --on', "ve qaffeynâ 'alâ âsârihim bi-'îsâ", True), say('lem 5:46:1', "qaffey"), say('say 5:46 2-3', "'alâ âsârihim"), say('say 5:46 4-6', "bi-'îsa'bni meryem"), say('say 5:46 5-6', "bni meryem")) + ' '
 + cumle(say('say 5:46 7-11', "musaddiqan li-mâ beyne yedeyhi min", True), say('dizi 5 46 7 11', "musaddiq mâ beyn yed min"), say('say 5:46 7-12', "musaddiqan li-mâ beyne yedeyhi mine't-tevrâh"), say('say 5:46 8-10', "li-mâ beyne yedeyh"), say('say 5:46 9-10', "beyne yedeyh")) + ' '
 + cumle(say('say 5:46 13-14 --on', "ve âteynâhu'l-incîl", True), say('say 5:46 15-17', "fîhi hudan ve nûr"), say('say 5:46 16-17', "hudan ve nûr"), say('say 5:46 18-23 --on', "ve musaddiqan li-mâ beyne yedeyhi mine't-tevrâh")) + ' '
 + cumle(say('say 5:46 24-26 --on', "ve hudan ve mev'izatan li'l-muttaqîn", True), say('say 5:46 25-26', "mev'izatan li'l-muttaqîn"), say('lem 5:46:25', "mev'iza")) + ' '
 "Ölçüm xref 3:138 (emsal olarak basıldı) ve okunmuş başka ayetler. "
 "Ölçüm nakarat3 kalıbı: 'musaddiqan li-mâ beyne yedeyhi min' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'yedeyhi' (10. kelime), 'yedeyhi' (21. kelime); B4 —.",
 "◈D — D1 've' + PERF + ''alâ' + izafet + 'bi' + özel ad + izafet + özel ad + nekre + 'li' + 'mâ' + 'beyn' + izafet + 'min' + belirli + 've' + PERF + belirli + 'fî' + nekre + 've' + nekre + 've' + nekre + 'li' + 'mâ' + 'beyn' + izafet + 'min' + belirli + 've' + nekre + 've' + nekre + 'li' + belirli; "
 "D2 haber, kip yok; D3 صدق ×2, بين ×2, يدي ×2, هدي ×2; 57:27 ve 3:138 eşleri; D4 1P 4 · 3MP 1 · 3MS 4, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T46 + "; ölçüm aktör adlı İsa, Meryem (kişi), İncil, Tevrat (kitap); A2 izden gönderme; İsa; Tevrat'ı doğrulama; İncil'in verilişi; hidayet ve nur; öğüt; sakınanlar; A3 —; A4 " + BOLUM + "; edim geçişi şart → haber (ayetler arası); şahıs geçişi 3 → 1 (ayetler arası).",
)

D[47] = ("◇ 've'l-yahkum ehlu'l-incîli bi-mâ enzele'llâhu fîh ve men lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike humu'l-fâsiqûn' — "
 "'ve' + 'li' + IMPF 3MS I. bab + 'ehl' + belirli 'incîl' + 'bi' + 'mâ' + PERF 3MS IV. bab + lafız + 'fî' + 3MS + 've' + 'men' + 'lem' + IMPF 3MS I. bab + 'bi' + 'mâ' + PERF 3MS IV. bab + lafız + 'fe' + 'ulâ' + 'ke' + 'hum' + belirli çoğul 'fâsiq' "
 "(ölçüm edim emir, şart, kip COND 1 · IMPV 1 · NEG 1; 3MP 1 · 3MS 5; bab I. bab ×2 · IV. bab ×2). "
 "Allah lafzı 6. ve 13. sırada (ölçüm allah z=1,97); Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm '{{3|aktör: adlı إِنجِيل 3\\. sırada \\(kitab, rol mecrur\\)}}' — satır aynen. "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=16 (n z=0,38); ölçüm '{{3|fâsıla ٱلفسقون → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|simetri \\[6, 4, 11, 1\\]}}' — satır aynen; ölçüm '{{3|harf 67 → harf3 65, isaret 2}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm IMPV 1: 'l-yahkum' (1. kelime; morph 'li' IMPV önek); COND 1: 'men' (8. kelime); NEG 1: 'lem' (9. kelime); 've'l-yahkum' (1.) ve 've men' (8.)'deki 've' CONJ; 'fe-ulâ'ike' (14.)'daki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) حكم ×2 ('l-yahkum' 1. / 'yahkum' 10. kelime), نزل ×2 ('enzele' 5. / 12. kelime), أله ×2 (lafız 6. / 13. kelime) (okuma). "
 + T47 + " (okuma). "
 + cumle(say('say 5:47 1-3 --on', "ve'l-yahkum ehlu'l-incîl", True), say('say 5:47 2-3', "ehlu'l-incîl"), say('say 5:47 4-6', "bi-mâ enzele'llâh"), say('say 5:47 4-7', "bi-mâ enzele'llâhu fîh")) + ' '
 + cumle(say('say 5:47 8-15 --on', "ve men lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike hum", True), say('dizi 5 47 8 15', "men lem hakeme mâ enzele allâh zâ _"), say('say 5:47 9-15', "lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike hum"), say('dizi 5 47 9 15', "lem hakeme mâ enzele allâh zâ _"),
         say('say 5:47 11-13', "bi-mâ enzele'llâh"), say('dizi 5 47 11 13', "mâ enzele allâh"), say('say 5:47 14-16', "fe-ulâ'ike humu'l-fâsiqûn"), say('say 5:47 15-16', "humu'l-fâsiqûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: 've men lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike hum', 'lem yahkum bi-mâ enzele'llâhu fe-ulâ'ike hum' ve 'bi-mâ enzele'llâh' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'li' + IMPF + izafet + belirli + 'bi' + 'mâ' + PERF + lafız + 'fî' + 've' + 'men' + 'lem' + IMPF + 'bi' + 'mâ' + PERF + lafız + 'fe' + 'ulâ' + 'ke' + 'hum' + belirli; "
 "D2 emir, şart, IMPV ('l-yahkum' 1. kelime), COND ('men' 8. kelime), NEG ('lem' 9. kelime); D3 حكم ×2, نزل ×2, أله ×2; 3:82 eşi; D4 3MP 1 · 3MS 5, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T47 + "; ölçüm aktör adlı İncil (kitap, mecrur); A2 İncil ehlinin hükmü; indirilenle hüküm; fâsıklık; A3 —; "
 "A4 " + BOLUM + "; edim geçişi haber → emir, şart (ayetler arası); şahıs geçişi 1 → 3 (ayetler arası); şart → cevap (ayet içi; COND 'men' 8. kelime: 've men lem yahkum bi-mâ enzele'llâh' / 'fe-ulâ'ike humu'l-fâsiqûn' (14. kelime)).",
)

out = ['# ── blok 5:45-47 (2026-11-15) ──', 'MEAL16 = {']
for n in range(45, 48):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M16 = {']
for n in range(45, 48):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL16); M.update(M16)']
open('/home/claude/yamalar/metin_5_45_47.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
