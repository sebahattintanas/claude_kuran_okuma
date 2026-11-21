# sûre 6 blok 14 (6:59-61) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b14/say2.txt'
os.environ['OLC'] = '/home/claude/b14/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Gaybın anahtarları; karanlıklardan kurtaran' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 59: "Gaybın anahtarları O'nun katındadır; onları ancak O bilir. Karada ve denizde olanı bilir. Düşen hiçbir yaprak yoktur ki onu bilmesin; yerin karanlıklarındaki hiçbir tane, hiçbir yaş ve hiçbir kuru yoktur ki apaçık bir kitapta olmasın.",
 60: "O, sizi geceleyin vefat ettiren ve gündüz ne işlediğinizi bilendir; sonra belirlenmiş bir süre tamamlansın diye sizi onda uyandırır; sonra dönüşünüz O'nadır; sonra size yapmakta olduklarınızı haber verir.",
 61: "O, kullarının üstünde kahredendir; üzerinize koruyucular gönderir. Nihayet birinize ölüm geldiğinde elçilerimiz onu vefat ettirir ve onlar ihmal etmezler.",
}

T = {}
T[59] = ("'ve 'indehû', 'ya'lemuhâ', 'huve', 've ya'lemu', 'ya'lemuhâ' 3MS (adsız; gönderge 6:58 12. kelime — 1., 5., 7., 8. ve 18. kelime); "
         "'ya'lemuhâ' 3FS (adsız; gönderge 'mefâtihu' 2. kelime, 5. kelime); 'tesqutu' 3FS (fiil uyumu; 14. kelime — fail 16. kelime); 'ya'lemuhâ' 3FS (adsız; gönderge 'veraqatin' 16. kelime, 18. kelime)")
T[60] = ("'ve huve', 'yeteveffâkum', 've ya'lemu', 'yeb'asukum', 'ileyhi', 'yunebbi'ukum' 3MS (adsız; gönderge 6:58 12. kelime — 1., 3., 5., 10., 16. ve 19. kelime); "
         "'fîhi' 3MS (adsız; gönderge 'n-nehâri' 8. kelime, 11. kelime); 'li-yuqdâ' 3MS (fiil uyumu; edilgen; naib-i faili 'ecelun' (13. kelimedeki ad), 12. kelime); "
         "muhatap 2MP (adsız; 'yeteveffâkum', 'cerahtum', 'yeb'asukum', 'merci'ukum', 'yunebbi'ukum', 'kuntum', 'ta'melûn' — 3., 7., 10., 17., 19., 21. ve 22. kelime)")
T[61] = ("'ve huve', ''ibâdihî', 've yursilu' 3MS (adsız; gönderge 6:58 12. kelime — 1., 4. ve 5. kelime); muhatap 2MP (adsız; ''aleykum', 'ehadekumu' — 6. ve 11. kelime); "
         "'câ'e' 3MS (fiil uyumu; 10. kelime — fail 12. kelime); 'teveffethu' 3FS (fiil uyumu; 13. kelime — fail 14. kelime); 'teveffethu' 3MS (adsız; nesne zamiri — 'ehadekumu' 11. kelimeye döner, 13. kelime); "
         "konuşan 1P (adsız; 'rusulunâ' — 14. kelime); 've hum', 'yufarritûn' 3MP (adsız; gönderge 'rusulunâ' 14. kelime — 15. ve 17. kelime)")

D = {}
D[59] = ("◇ 've 'indehû mefâtihu'l-ğaybi lâ ya'lemuhâ illâ huve, ve ya'lemu mâ fi'l-berri ve'l-bahr, ve mâ tesqutu min veraqatin illâ ya'lemuhâ ve lâ habbetin fî zulumâti'l-ardi ve lâ ratbin ve lâ yâbisin illâ fî kitâbin mubîn' — "
 "'ve' + ''inde' + 3MS + çoğul 'mefâtih' + belirli 'ğayb' + 'lâ' + IMPF 3MS I. bab + 3FS + 'illâ' + 'huve' + 've' + IMPF 3MS I. bab + 'mâ' + 'fî' + belirli 'berr' + 've' + belirli 'bahr' + "
 "'ve' + 'mâ' + IMPF 3FS I. bab + 'min' + nekre 'veraqa' + 'illâ' + IMPF 3MS I. bab + 3FS + 've' + 'lâ' + nekre 'habbe' + 'fî' + çoğul 'zulme' + belirli 'ard' + 've' + 'lâ' + nekre 'ratb' + 've' + 'lâ' + nekre etken ortaç 'yâbis' + 'illâ' + 'fî' + nekre 'kitâb' + nekre etken ortaç 'mubîn' "
 "(ölçüm edim haber, kip NEG 5 · RES 3; 3FS 3 · 3MS 5; bab I. bab ×4). "
 "Allah lafzı yok; Rab yok; ölçüm '{{1|esmâ بَرّ 11\\. sırada, ORTA konum, MÜHÜRSÜZ \\| مُبِين 31\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' — ölçüm MÜHÜRSÜZ ile uyuşmuyor, araç tanımı farkı (muhur_el hayır, ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'mâ fi'l-berri ve'l-bahr', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); esma_el kaydı 'degil' — 'illâ fî kitâbin mubîn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=31 (n z=1,97); ölçüm '{{1|biçim HASR}}' — satır aynen; "
 "ölçüm '{{1|fâsıla مبين → ن, N sınıfı}}' — satır aynen (6:58 ن → 6:59 ن); ölçüm '{{1|simetri \\[4, 4, 17, 1\\]}}' — satır aynen; ölçüm '{{1|harf 119 → harf3 111, isaret 8}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 5: 'lâ' (4. kelime), 'mâ' (13. kelime), 've lâ' (19., 24. ve 26. kelime); RES 3: 'illâ' (6., 17. ve 28. kelime); 've 'indehû' (1.) kelimesindeki 've' REM; 've ya'lemu' (8.), 've'l-bahr' (12.), 've mâ' (13.), 've lâ' (19., 24., 26.) kelimelerindeki 've' CONJ; ''indehû' (1.) LOC (okuma). "
 "Kök ikilemesi (ölçüm) علم ×3 ('ya'lemuhâ' 5. / 've ya'lemu' 8. / 'ya'lemuhâ' 18. kelime) (okuma). "
 + T[59] + " (okuma). "
 + cumle(say('say 6:59 28-31', "illâ fî kitâbin mubîn", True), say('say 6:59 4-7', "lâ ya'lemuhâ illâ huve")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'l-berri' / 've'l-bahr'; 'ratbin' / 'yâbisin' — ayetler arası: yok.",
 "◈K — K1 'l-bahr' (12. kelime), 'l-ardi' (23. kelime).",
 "◈B — —",
 "◈D — D1 've' + izafet + izafet + belirli + 'lâ' + IMPF + 'illâ' + 'huve' + 've' + IMPF + 'mâ' + 'fî' + belirli + 've' + belirli + 've' + 'mâ' + IMPF + 'min' + nekre + 'illâ' + IMPF + 've' + 'lâ' + nekre + 'fî' + izafet + belirli + 've' + 'lâ' + nekre + 've' + 'lâ' + nekre + 'illâ' + 'fî' + nekre + nekre; "
 "D2 haber; NEG ('lâ' 4. kelime, 'mâ' 13. kelime, 've lâ' 19., 24. ve 26. kelime), RES ('illâ' 6., 17. ve 28. kelime); D3 علم ×3; 10:61 eşi; D4 3FS 3 · 3MS 5, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[59] + "; aktör yok (ölçüm); A2 gaybın anahtarlarının O'nun katında olması; karada ve denizde olanın bilinmesi; düşen yaprağın, yerin karanlıklarındaki tanenin, yaşın ve kurunun kitapta olması; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi emir, şart → haber (ayetler arası); bölüm açılışı.",
)

D[60] = ("◇ 've huve'llezî yeteveffâkum bi'l-leyli ve ya'lemu mâ cerahtum bi'n-nehâri summe yeb'asukum fîhi li-yuqdâ ecelun musemmâ, summe ileyhi merci'ukum summe yunebbi'ukum bimâ kuntum ta'melûn' — "
 "'ve' + 'huve' + 'ellezî' + IMPF 3MS V. bab + 2MP + 'bi' + belirli 'leyl' + 've' + IMPF 3MS I. bab + 'mâ' + PERF 2MP I. bab + 'bi' + belirli 'nehâr' + 'summe' + IMPF 3MS I. bab + 2MP + 'fî' + 3MS + 'li' + edilgen IMPF 3MS I. bab + nekre 'ecel' + nekre edilgen ortaç 'musemmâ' + "
 "'summe' + 'ilâ' + 3MS + 'merci'' + 2MP + 'summe' + IMPF 3MS II. bab + 2MP + 'bi' + 'mâ' + PERF 2MP I. bab + IMPF 2MP I. bab "
 "(ölçüm edim haber, kip yok; 2MP 10 · 3MS 8; bab I. bab ×6 · II. bab ×1 · V. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=22 (n z=1,02); ölçüm '{{2|EDİLGEN 1/8 fiil, pas z=0,38}}' — satır aynen; ölçüm '{{2|fâsıla تعملون → ن, N sınıfı}}' — satır aynen (6:59 ن → 6:60 ن); "
 "ölçüm '{{2|simetri \\[3, 1, 15, 1\\]}}' — satır aynen; ölçüm '{{2|harf 97 → harf3 94, isaret 3}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; 've huve' (1.) ve 've ya'lemu' (5.) kelimelerindeki 've' CONJ; 'li-yuqdâ' (12.) PRP; 'summe' (9., 15. ve 18.) CONJ (okuma). "
 + T[60] + " (okuma). "
 + cumle(say('say 6:60 18-21', "summe yunebbi'ukum bimâ kuntum", True), say('dizi 6 60 18 21', "summe nebbe'e mâ kâne"), say('dizi 6 60 19 22', "nebbe'e mâ kâne 'amile")) + ' '
 + cumle(say('dizi 6 60 19 21', "nebbe'e mâ kâne"), say('dizi 6 60 20 22', "bi-mâ kâne 'amile")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: 'summe nebbe'e mâ kâne' süzgeç GEÇER, 'nebbe'e mâ kâne 'amile' süzgeç GEÇER, 'nebbe'e mâ kâne' süzgeç GEÇER, 'bi-mâ kâne 'amile' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'bi'l-leyli' / 'bi'n-nehâri'; 'yeteveffâkum' / 'yeb'asukum' — ayetler arası: yok.",
 "◈K — K1 'l-leyli' (4. kelime), 'n-nehâri' (8. kelime); K2 'ecelun' (13. kelime).",
 "◈B — —",
 "◈D — D1 've' + 'huve' + 'ellezî' + IMPF + 'bi' + belirli + 've' + IMPF + 'mâ' + PERF + 'bi' + belirli + 'summe' + IMPF + 'fî' + 'li' + IMPF + nekre + nekre + 'summe' + 'ilâ' + izafet + 'summe' + IMPF + 'bi' + 'mâ' + PERF + IMPF; "
 "D2 haber; D3 —; D4 2MP 10 · 3MS 8, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[60] + "; aktör yok (ölçüm); A2 gece vefat ettirme, gündüz işleneni bilme; belirlenmiş sürenin tamamlanması için uyandırma; dönüşün O'na olması; yapılanın haber verilmesi; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 2 (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[61] = ("◇ 've huve'l-qâhiru fevqa 'ibâdihî ve yursilu 'aleykum hafazaten, hattâ izâ câ'e ehadekumu'l-mevtu teveffethu rusulunâ ve hum lâ yufarritûn' — "
 "'ve' + 'huve' + belirli etken ortaç 'qâhir' + 'fevq' + çoğul ''abd' + 3MS + 've' + IMPF 3MS IV. bab + ''alâ' + 2MP + nekre çoğul etken ortaç 'hafîz' + 'hattâ' + 'izâ' + PERF 3MS I. bab + 'ehad' + 2MP + belirli 'mevt' + PERF 3FS V. bab + 3MS + çoğul 'resûl' + 1P + 've' + 'hum' + 'lâ' + IMPF 3MP II. bab "
 "(ölçüm edim haber, kip NEG 1; 1P 1 · 2MP 2 · 3FS 1 · 3MP 3 · 3MS 5; bab I. bab ×1 · II. bab ×1 · IV. bab ×1 · V. bab ×1). "
 "Allah lafzı yok; Rab yok; ölçüm '{{3|esmâ حَفِيظ 7\\. sırada, ORTA konum, MÜHÜRSÜZ \\| أَحَد 11\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' — ölçüm MÜHÜRSÜZ ile uyuşmuyor, araç tanımı farkı (muhur_el hayır, ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 've yursilu 'aleykum hafaza', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); esma_el kaydı 'degil' — 'câ'e ehadekumu'l-mevt', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=17 (n z=0,49); ölçüm '{{3|sayı işareti أَحَد}}' — satır aynen; ölçüm '{{3|fâsıla يفرطون → ن, N sınıfı}}' — satır aynen (6:60 ن → 6:61 ن); "
 "ölçüm '{{3|simetri \\[3, 8, 15, 1\\]}}' — satır aynen; ölçüm '{{3|harf 73 → harf3 71, isaret 2}}' — satır aynen; ölçüm '{{3|dış düğüm 1}}' — satır aynen. "
 "Ölçüm NEG 1: 'lâ' (16. kelime); 've huve' (1.) kelimesindeki 've' CONJ; 've yursilu' (5.) kelimesindeki 've' REM; 've hum' (15.) kelimesindeki 've' CIRC; 'hattâ' (8.) INC; 'izâ' (9.) T (okuma). "
 "Kök ikilemesi (ölçüm) رسل ×2 ('ve yursilu' 5. / 'rusulunâ' 14. kelime) (okuma). "
 + T[61] + " (okuma). "
 + cumle(say('say 6:61 1-4', "ve huve'l-qâhiru fevqa 'ibâdih", True), say('dizi 6 61 1 4', "_ qâhir fevq 'abd")) + ' '
 + cumle(say('say 6:61 8-10', "hattâ izâ câ'e", True), say('dizi 6 61 8 10', "hattâ izâ câ'e"), say('dizi 6 61 8 12', "hattâ izâ câ'e ehad mevt")) + ' '
 "Ölçüm xref 23:99 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıpları: '_ qâhir fevq 'abd' süzgeç GEÇER, 'hattâ izâ câ'e' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 —; B4 'l-mevtu' (12. kelime).",
 "◈D — D1 've' + 'huve' + belirli + 'fevq' + izafet + 've' + IMPF + ''alâ' + nekre + 'hattâ' + 'izâ' + PERF + izafet + belirli + PERF + izafet + 've' + 'hum' + 'lâ' + IMPF; "
 "D2 haber; NEG ('lâ' 16. kelime); D3 رسل ×2; 23:99 eşi; D4 1P 1 · 2MP 2 · 3FS 1 · 3MP 3 · 3MS 5, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[61] + "; aktör yok (ölçüm); A2 kulların üstünde kahretme; koruyucuların gönderilmesi; ölüm gelince elçilerin vefat ettirmesi; elçilerin ihmal etmemesi; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi yok (ayetler arası).",
)
