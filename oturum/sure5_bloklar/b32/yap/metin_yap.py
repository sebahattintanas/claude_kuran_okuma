# blok 32 (5:106-108) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b32/say2.txt'
os.environ['OLC'] = '/home/claude/b32/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Soru sormama; bahîra ve sâibe; vasiyet ve şahitlik' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 106: "Ey iman edenler! Sizden bir kişiye ölüm geldiğinde, vasiyet vaktinde aranızdaki şahitlik, sizden iki adalet sahibi ya da yeryüzünde yolculuk eder de size ölüm musibeti isabet ederse sizden olmayan başka iki kişidir. Şüphe ederseniz onları namazdan sonra alıkoyarsınız da Allah'a yemin ederler: Akraba da olsa onu hiçbir bedele değişmeyiz, Allah'ın şahitliğini de gizlemeyiz; yoksa o zaman şüphesiz günahkârlardan oluruz.",
 107: "Eğer o iki şahidin bir günahı hak ettiği ortaya çıkarsa, aleyhlerine hak iddia edilenlerden en layık başka iki kişi onların yerine geçer ve Allah'a yemin ederler: Bizim şahitliğimiz onların şahitliğinden daha haklıdır, biz sınırı aşmadık; yoksa o zaman şüphesiz zalimlerden oluruz.",
 108: "Bu, şahitliği gerçek yüzüyle getirmelerine ya da kendi yeminlerinden sonra yeminlerin geri çevrilmesinden korkmalarına daha yakındır. Allah'tan sakının ve dinleyin. Allah fâsık kavme yol göstermez.",
}

T106 = ("hitap 'yâ eyyuhe'llezîne âmenû' (1-3. kelime); 'âmenû' faili 3MP (adsız; 3. kelime); muhatap 2MP (adsız; 'beynikum', 'ehadekumu', 'minkum', 'ğayrikum', 'entum', 'darabtum', 'fe-esâbetkum', 'tahbisûnehumâ', 'rtebtum' — 5., 8., 15., 19., 21., 22., 25., 28. ve 35. kelime); "
        "'hadara' 3MS (fiil uyumu; 7. kelime — fail 9. kelime); 'l-mevtu' ('hadara' faili; 9. kelime); 'fe-esâbetkum' 3FS (fiil uyumu; 25. kelime — fail 26. kelime); 'musîbetu'l-mevti' ('esâbe' faili; 26-27. kelime); "
        "'tahbisûnehumâ' mef'ûlü 3D (adsız; gönderge 12. ve 17. kelime, 28. kelime); 'fe-yuqsimâni' faili 3MD / 3D (adsız; 32. kelime); 'bi'llâhi' (yemin edilen; lafız; 33. kelime); "
        "konuşan 1P (adsız; söz içi; 'neşterî', 'nektumu', 'innâ' — 37., 45. ve 48. kelime); 'bihî' 3MS (adsız; söz içi; gönderge 'şehâdetu', 38. kelime); 'kâne' 3MS (adsız; söz içi; gönderge şahitlik edilen, 41. kelime); "
        "'şehâdete'llâhi' (söz içi; lafız tamlayan; 46-47. kelime)")
T107 = ("''usira' 3MS (fiil uyumu; edilgen; 2. kelime — naib-i faili 4-6. kelime); 'ennehume' 3D (adsız; gönderge 5:106 iki şahit, 4. kelime); 'stehaqqâ' faili 3MD (adsız; 5. kelime); "
        "'fe-âxarâni' (mübtedâ; ikil; 7. kelime); 'yaqûmâni' faili 3MD / 3D (adsız; 8. kelime); 'maqâmehumâ' 3D (adsız; 9. kelime); 'stehaqqa' 3MS (adsız; 12. kelime); ''aleyhimu' 3MP (adsız; 13. kelime); "
        "'l-evleyâni' (bedel; ikil; 14. kelime); 'fe-yuqsimâni' faili 3MD / 3D (adsız; 15. kelime); 'bi'llâhi' (yemin edilen; lafız; 16. kelime); "
        "konuşan 1P (adsız; söz içi; 'le-şehâdetunâ', ''tedeynâ', 'innâ' — 17., 22. ve 23. kelime); 'şehâdetihimâ' 3D (adsız; söz içi; 20. kelime)")
T108 = ("'ye'tû' faili 3MP (adsız; 4. kelime); 'vechihâ' 3FS (adsız; gönderge 'şehâdeti', 7. kelime); 'yaxâfû' faili 3MP (adsız; 9. kelime); 'turadde' 3FS (fiil uyumu; edilgen; 11. kelime — naib-i faili 12. kelime); "
        "'eymânun' ('turadde' naib-i faili; nekre; 12. kelime); 'eymânihim' 3MP (adsız; 14. kelime); muhatap 2MP (adsız; 'ttequ', 'sme'û' — 15. ve 17. kelime); 'llâhe' ('ttequ' mef'ûlü; lafız; 16. kelime); "
        "'llâhu' (mübtedâ; lafız; 18. kelime); 'yehdi' 3MS (adsız; gönderge lafız, 20. kelime)")

D = {}
D[106] = ("◇ 'yâ eyyuhe'llezîne âmenû şehâdetu beynikum izâ hadara ehadekumu'l-mevtu hîne'l-vasiyyeti'snâni zevâ 'adlin minkum ev âxarâni min ğayrikum in entum darabtum fi'l-ardi fe-esâbetkum musîbetu'l-mevti "
 "tahbisûnehumâ min ba'di's-salâti fe-yuqsimâni bi'llâhi ini'rtebtum lâ neşterî bihî semenen ve lev kâne zâ qurbâ ve lâ nektumu şehâdete'llâhi innâ izen le-mine'l-âsimîn' — "
 "'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF 3MP IV. bab + 'şehâde' + 'beyn' + 2MP + 'izâ' + PERF 3MS I. bab + 'ehad' + 2MP + belirli 'mevt' + 'hîn' + belirli 'vasiyye' + ikil 'isneyn' + ikil 'zû' + nekre ''adl' + 'min' + 2MP + "
 "'ev' + ikil 'âxar' + 'min' + 'ğayr' + 2MP + 'in' + 2MP zamir + PERF 2MP I. bab + 'fî' + belirli 'ard' + 'fe' + PERF 3FS IV. bab + 2MP + etken ortaç 'musîbe' + belirli 'mevt' + IMPF 2MP I. bab + 3D + 'min' + 'ba'd' + belirli 'salâ' + "
 "'fe' + IMPF 3MD IV. bab + 'bi' + lafız + 'in' + PERF 2MP VIII. bab + 'lâ' + IMPF 1P VIII. bab + 'bi' + 3MS + nekre 'semen' + 've' + 'lev' + PERF 3MS I. bab + 'zû' + 'qurbâ' + 've' + 'lâ' + IMPF 1P I. bab + 'şehâde' + lafız + "
 "'inne' + 1P + 'izen' + 'le' + 'min' + belirli çoğul etken ortaç 'âsim' "
 "(ölçüm edim nida, şart, kip COND 3 · EMPH 1 · NEG 2 · VOC 1; 1P 3 · 2MP 12 · 3D 2 · 3FS 1 · 3MD 1 · 3MP 2 · 3MS 3; bab I. bab ×5 · IV. bab ×3 · VIII. bab ×2). "
 "Allah lafzı 33. ve 47. sırada (ölçüm allah z=0,26); Rab yok; ölçüm '{{1|esmâ أَحَد 8\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür hayır' (uyuşuyor) — esma_el kaydı 'degil' — 'ehadekumu', kural 'çoğul insan göndergeli → degil' (biriniz; 'kum' zamirli, insan öznesi) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=51 (n z=4,10); ölçüm '{{1|fâsıla ٱلءاثمين → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|sayı işareti أَحَد, اثْنَيْن, ثَمَن}}' — satır aynen; "
 "ölçüm '{{1|simetri \\[4, 13, 18, 1\\]}}' — satır aynen; ölçüm '{{1|harf 220 → harf3 212, isaret 8}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen. "
 "Ölçüm VOC 1: 'yâ' (1. kelime); COND 3: 'in' (20. ve 34. kelime), 'lev' (40. kelime); NEG 2: 'lâ' (36. ve 44. kelime); EMPH 1: 'le' (50. kelime); 'fe-esâbetkum' (25.)'daki 'fe' CONJ, 'fe-yuqsimâni' (32.)'daki 'fe' REM, 've lev' (40.)'daki 've' REM, 've lâ' (44.)'daki 've' CONJ, 'izâ' (6.) ve 'hîne' (10.) T, 'izen' (49.) ANS (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('bi'llâhi' 33. / 'şehâdete'llâhi' 47. kelime), شهد ×2 ('şehâdetu' 4. / 'şehâdete' 46. kelime), صوب ×2 ('fe-esâbetkum' 25. / 'musîbetu' 26. kelime), موت ×2 ('l-mevtu' 9. / 'l-mevti' 27. kelime) (okuma). "
 + T106 + " (okuma). "
 + cumle(say('say 5:106 1-3', "yâ eyyuhe'llezîne âmenû", True), say('dizi 5 106 1 3', "eyy ellezî âmene"), say('say 5:106 4-5', "şehâdetu beynikum"), say('say 5:106 6-9', "izâ hadara ehadekumu'l-mevt"), say('say 5:106 8-9', "ehadekumu'l-mevt"), say('say 5:106 10-11', "hîne'l-vasiyye")) + ' '
 + cumle(say('say 5:106 12-15', "snâni zevâ 'adlin minkum", True), say('say 5:106 13-15', "zevâ 'adlin minkum"), say('dizi 5 106 13 15', "zû 'adl min"), say('say 5:106 16-19', "ev âxarâni min ğayrikum")) + ' '
 + cumle(say('say 5:106 20-24', "in entum darabtum fi'l-ard", True), say('say 5:106 25-27', "fe-esâbetkum musîbetu'l-mevt"), say('say 5:106 28-31', "tahbisûnehumâ min ba'di's-salât"), say('say 5:106 32-33 --on', "fe-yuqsimâni bi'llâh"), say('say 5:106 34-35', "ini'rtebtum")) + ' '
 + cumle(say('say 5:106 36-39', "lâ neşterî bihî semenen", True), say('say 5:106 40-43 --on', "ve lev kâne zâ qurbâ"), say('say 5:106 44-47 --on', "ve lâ nektumu şehâdete'llâh"), say('say 5:106 46-47', "şehâdete'llâh")) + ' '
 + cumle(say('say 5:106 48-51', "innâ izen le-mine'l-âsimîn", True), say('say 5:106 48-50', "innâ izen le-mine"), say('dizi 5 106 48 50', "inne izen min")) + ' '
 "Ölçüm xref 2:180 (emsal olarak basıldı) ve okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'eyy ellezî âmene' süzgeç GEÇER, 'zû 'adl min' ve 'inne izen min' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'minkum' / 'min ğayrikum' — ayetler arası: yok.",
 "◈K — K1 'l-ardi' (24. kelime); K2 'hîne' (10. kelime).",
 "◈B — B4 'l-mevtu' (9. kelime), 'l-mevti' (27. kelime).",
 "◈D — D1 'yâ' + 'ellezî' + PERF + izafet + 'izâ' + PERF + izafet + belirli + 'hîn' + belirli + ikil + ikil + nekre + 'min' + 'ev' + ikil + 'min' + izafet + 'in' + zamir + PERF + 'fî' + belirli + 'fe' + PERF + izafet + belirli + IMPF + 'min' + izafet + belirli + "
 "'fe' + IMPF + 'bi' + lafız + 'in' + PERF + 'lâ' + IMPF + 'bi' + nekre + 've' + 'lev' + PERF + izafet + 've' + 'lâ' + IMPF + izafet + lafız + 'inne' + 'izen' + 'le' + 'min' + belirli; "
 "D2 nida, şart, VOC ('yâ' 1. kelime), COND ('in' 20. ve 34., 'lev' 40. kelime), NEG ('lâ' 36. ve 44. kelime), EMPH ('le' 50. kelime); D3 أله ×2, شهد ×2, صوب ×2, موت ×2; 2:180 eşi; D4 1P 3 · 2MP 12 · 3D 2 · 3FS 1 · 3MD 1 · 3MP 2 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T106 + "; aktör yok (ölçüm); A2 ölüm anında vasiyete iki adil şahit; yolculukta başka iki kişi; şüphede namazdan sonra alıkonup Allah adına yemin; "
 "A3 'lâ neşterî bihî semenen ve lev kâne zâ qurbâ ve lâ nektumu şehâdete'llâhi innâ izen le-mine'l-âsimîn' (söz içi, 36-51. kelime); "
 "A4 " + BOLUM + "; hitap açılır ('yâ eyyuhe'llezîne âmenû', 1-3. kelime); söz açılır (36. kelime); söz kapanır (51. kelime, ayet içi); edim geçişi emir, nida → nida, şart (ayetler arası); "
 "şart → cevap (ayet içi; COND 'in' 20. kelime: 'in entum darabtum fi'l-ard' / 'âxarâni min ğayrikum' (17-19. kelime)); şart → cevap (ayet içi; COND 'in' 34. kelime: 'ini'rtebtum' / 'fe-yuqsimâni bi'llâh' (32-33. kelime)); "
 "şart → cevap (ayet içi; COND 'lev' 40. kelime: 've lev kâne zâ qurbâ' — cevap mahzuf (okuma)).",
)

D[107] = ("◇ 'fe-in 'usira 'alâ ennehume'stehaqqâ ismen fe-âxarâni yaqûmâni maqâmehumâ mine'llezîne'stehaqqa 'aleyhimu'l-evleyâni fe-yuqsimâni bi'llâhi le-şehâdetunâ ehaqqu min şehâdetihimâ ve mâ 'tedeynâ innâ izen le-mine'z-zâlimîn' — "
 "'fe' + 'in' + edilgen PERF 3MS I. bab + ''alâ' + 'enne' + 3D + PERF 3MD X. bab + nekre 'ism' + 'fe' + ikil 'âxar' + IMPF 3MD I. bab + 'maqâm' + 3D + 'min' + 'ellezî' + PERF 3MS X. bab + ''alâ' + 3MP + belirli ikil 'evleyân' + "
 "'fe' + IMPF 3MD IV. bab + 'bi' + lafız + 'le' + 'şehâde' + 1P + 'ehaqq' + 'min' + 'şehâde' + 3D + 've' + 'mâ' + PERF 1P VIII. bab + 'inne' + 1P + 'izen' + 'le' + 'min' + belirli çoğul etken ortaç 'zâlim' "
 "(ölçüm edim şart, kip COND 1 · EMPH 2 · NEG 1; 1P 4 · 3D 5 · 3MD 4 · 3MP 1 · 3MS 2; bab I. bab ×2 · IV. bab ×1 · VIII. bab ×1 · X. bab ×2; EDİLGEN 1/6 fiil). "
 "Allah lafzı 16. sırada (ölçüm allah z=0,24); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=26 (n z=1,44); ölçüm '{{2|fâsıla ٱلظلمين → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|EDİLGEN 1/6 fiil, pas z=0,62}}' — satır aynen (''usira' 2. kelime); "
 "ölçüm '{{2|simetri \\[4, 1, 21, 1\\]}}' — satır aynen; ölçüm '{{2|harf 127 → harf3 125, isaret 2}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm COND 1: 'in' (1. kelime); EMPH 2: 'le' (17. ve 25. kelime); NEG 1: 'mâ' (21. kelime); 'fe-in' (1.) ve 'fe-yuqsimâni' (15.)'daki 'fe' CONJ, 'fe-âxarâni' (7.)'daki 'fe' RSLT, 've mâ' (21.)'daki 've' REM, 'izen' (24.) ANS (okuma). "
 "Kök ikilemesi (ölçüm) حقق ×3 ('stehaqqâ' 5., 'stehaqqa' 12., 'ehaqqu' 18. kelime), شهد ×2 ('le-şehâdetunâ' 17. / 'şehâdetihimâ' 20. kelime), قوم ×2 ('yaqûmâni' 8. / 'maqâmehumâ' 9. kelime); ölçüm '{{2|mm2: \\[8, قوم}}' — satır aynen (okuma). "
 + T107 + " (okuma). "
 + cumle(say('say 5:107 1-2 --on', "fe-in 'usira", True), say('say 5:107 3-6', "'alâ ennehume'stehaqqâ ismen"), say('say 5:107 4-6', "ennehume'stehaqqâ ismen")) + ' '
 + cumle(say('say 5:107 7-9 --on', "fe-âxarâni yaqûmâni maqâmehumâ", True), say('say 5:107 10-14', "mine'llezîne'stehaqqa 'aleyhimu'l-evleyân"), say('say 5:107 12-14', "stehaqqa 'aleyhimu'l-evleyân"), say('say 5:107 15-16 --on', "fe-yuqsimâni bi'llâh")) + ' '
 + cumle(say('say 5:107 17-20', "le-şehâdetunâ ehaqqu min şehâdetihimâ", True), say('say 5:107 18-20', "ehaqqu min şehâdetihimâ"), say('say 5:107 21-22 --on', "ve mâ 'tedeynâ")) + ' '
 + cumle(say('say 5:107 23-26', "innâ izen le-mine'z-zâlimîn", True), say('say 5:107 23-25', "innâ izen le-mine"), say('dizi 5 107 23 25', "inne izen min")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'inne izen min' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'le-şehâdetunâ' / 'şehâdetihimâ' — ayetler arası: 'l-âsimîn' (5:106) / 'z-zâlimîn' (5:107) kapanış eşliği (okuma).",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'fe' + 'in' + PERF + ''alâ' + 'enne' + PERF + nekre + 'fe' + ikil + IMPF + izafet + 'min' + 'ellezî' + PERF + ''alâ' + belirli + 'fe' + IMPF + 'bi' + lafız + 'le' + izafet + 'ehaqq' + 'min' + izafet + 've' + 'mâ' + PERF + 'inne' + 'izen' + 'le' + 'min' + belirli; "
 "D2 şart, COND ('in' 1. kelime), EMPH ('le' 17. ve 25. kelime), NEG ('mâ' 21. kelime); D3 حقق ×3, شهد ×2, قوم ×2; D4 1P 4 · 3D 5 · 3MD 4 · 3MP 1 · 3MS 2, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T107 + "; aktör yok (ölçüm); A2 iki şahidin günahı ortaya çıkınca en yakın iki kişinin yerlerine geçmesi ve Allah adına yemin; "
 "A3 'le-şehâdetunâ ehaqqu min şehâdetihimâ ve mâ 'tedeynâ innâ izen le-mine'z-zâlimîn' (söz içi, 17-26. kelime); "
 "A4 " + BOLUM + "; söz açılır (17. kelime); söz kapanır (26. kelime, ayet içi); edim geçişi nida, şart → şart (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası); "
 "şart → cevap (ayet içi; COND 'in' 1. kelime: 'fe-in 'usira' / 'fe-âxarâni yaqûmâni' (7-8. kelime)).",
)

D[108] = ("◇ 'zâlike ednâ en ye'tû bi'ş-şehâdeti 'alâ vechihâ ev yaxâfû en turadde eymânun ba'de eymânihim ve'ttequ'llâhe ve'sme'û ve'llâhu lâ yehdi'l-qavme'l-fâsiqîn' — "
 "'zâlike' + 'ednâ' + 'en' + IMPF 3MP I. bab + 'bi' + belirli 'şehâde' + ''alâ' + 'vech' + 3FS + 'ev' + IMPF 3MP I. bab + 'en' + edilgen IMPF 3FS I. bab + nekre çoğul 'yemîn' + 'ba'd' + çoğul 'yemîn' + 3MP + "
 "'ve' + IMPV 2MP VIII. bab + lafız + 've' + IMPV 2MP I. bab + 've' + lafız + 'lâ' + IMPF 3MS I. bab + belirli 'qavm' + belirli çoğul etken ortaç 'fâsiq' "
 "(ölçüm edim emir, kip IMPV 2 · NEG 1; 2MP 4 · 3FS 2 · 3MP 5 · 3MS 1; bab I. bab ×5 · VIII. bab ×1; EDİLGEN 1/6 fiil). "
 "Allah lafzı 16. ve 18. sırada (ölçüm allah z=1,29); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=22 (n z=1,02); ölçüm '{{3|fâsıla ٱلفسقين → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|EDİLGEN 1/6 fiil, pas z=0,62}}' — satır aynen ('turadde' 11. kelime); "
 "ölçüm '{{3|simetri \\[3, 1, 6, 1\\]}}' — satır aynen; ölçüm '{{3|harf 102 → harf3 95, isaret 7}}' — satır aynen; ölçüm '{{3|dış düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 2: 'ttequ' (15. kelime), 'sme'û' (17. kelime); NEG 1: 'lâ' (19. kelime); 've'ttequ' (15.) ve 've'llâhu' (18.)'daki 've' REM, 've'sme'û' (17.)'daki 've' CONJ, 'ba'de' (13.) T (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhe' 16. / 'llâhu' 18. kelime), يمن ×2 ('eymânun' 12. / 'eymânihim' 14. kelime) (okuma). "
 + T108 + " (okuma). "
 + cumle(say('say 5:108 1-7', "zâlike ednâ en ye'tû bi'ş-şehâdeti 'alâ vechihâ", True), say('say 5:108 1-2', "zâlike ednâ"), say('say 5:108 3-5', "en ye'tû bi'ş-şehâde"), say('say 5:108 6-7', "'alâ vechihâ")) + ' '
 + cumle(say('say 5:108 8-11', "ev yaxâfû en turadde", True), say('say 5:108 9-11', "yaxâfû en turadde"), say('say 5:108 11-14', "turadde eymânun ba'de eymânihim"), say('say 5:108 12-14', "eymânun ba'de eymânihim")) + ' '
 + cumle(say('say 5:108 15-17 --on', "ve'ttequ'llâhe ve'sme'û", True), say('say 5:108 15-16 --on', "ve'ttequ'llâh")) + ' '
 + cumle(say('say 5:108 18-22 --on', "ve'llâhu lâ yehdi'l-qavme'l-fâsiqîn", True), say('say 5:108 18-21 --on', "ve'llâhu lâ yehdi'l-qavm"), say('dizi 5 108 18 21', "allâh lâ hedâ qavm"), say('say 5:108 19-22', "lâ yehdi'l-qavme'l-fâsiqîn"), say('say 5:108 20-22', "yehdi'l-qavme'l-fâsiqîn")) + ' '
 "Ölçüm xref okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'allâh lâ hedâ qavm' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'eymânun' / 'eymânihim' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B3 'sme'û' (17. kelime).",
 "◈D — D1 'zâlike' + 'ednâ' + 'en' + IMPF + 'bi' + belirli + ''alâ' + izafet + 'ev' + IMPF + 'en' + IMPF + nekre + 'ba'd' + izafet + 've' + IMPV + lafız + 've' + IMPV + 've' + lafız + 'lâ' + IMPF + belirli + belirli; "
 "D2 emir, IMPV ('ttequ' 15., 'sme'û' 17. kelime), NEG ('lâ' 19. kelime); D3 أله ×2, يمن ×2; D4 2MP 4 · 3FS 2 · 3MP 5 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T108 + "; aktör yok (ölçüm); A2 hükmün şahitliği gerçek yüzüyle getirmeye ve yeminlerin geri çevrilmesinden korkmaya daha yakın oluşu; sakınma ve dinleme emri; A3 —; "
 "A4 " + BOLUM + "; bölüm kapanışı; edim geçişi şart → emir (ayetler arası).",
)

out = ['# ── blok 5:106-108 (2026-11-17) ──', 'MEAL32 = {']
for n in range(106, 109):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M32 = {']
for n in range(106, 109):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL32); M.update(M32)']
open('/home/claude/yamalar/metin_5_106_108.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
