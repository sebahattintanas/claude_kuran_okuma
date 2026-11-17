# blok 31 (5:101-105) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b31/say2.txt'
os.environ['OLC'] = '/home/claude/b31/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Soru sormama; bahîra ve sâibe; vasiyet ve şahitlik' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 101: "Ey iman edenler! Size açıklanırsa sizi üzecek şeyler hakkında sormayın. Kur'an indirilirken onlar hakkında sorarsanız size açıklanır. Allah onları affetti. Allah bağışlayandır, halîmdir.",
 102: "Sizden önce bir kavim onları sordu, sonra onlar yüzünden kâfir oldular.",
 103: "Allah ne bahîre, ne sâibe, ne vasîle ne de hâmî kıldı; fakat inkâr edenler Allah'a karşı yalan uyduruyorlar; çoğu da akletmez.",
 104: "Onlara, Allah'ın indirdiğine ve elçiye gelin denildiğinde: Atalarımızı üzerinde bulduğumuz şey bize yeter, derler. Ataları bir şey bilmeyen ve doğru yolu bulamayan kimseler olsa da mı?",
 105: "Ey iman edenler! Kendinizi gözetin. Siz doğru yolu bulduğunuzda sapan size zarar vermez. Hepinizin dönüşü Allah'adır; O size yapmakta olduğunuz şeyleri haber verecektir.",
}

T101 = ("hitap 'yâ eyyuhe'llezîne âmenû' (1-3. kelime); 'âmenû' faili 3MP (adsız; 3. kelime); muhatap 2MP (adsız; 'tes'elû', 'lekum', 'tesu'kum', 'tes'elû', 'lekum' — 5., 10., 11., 13. ve 19. kelime); "
        "'tubde' faili (adsız; edilgen — nâib fâil 3FS, gönderge 'eşyâ'e', 9. kelime); 'tesu'kum' 3FS (adsız; gönderge 'eşyâ'e', 11. kelime); ''anhâ' 3FS (adsız; gönderge 'eşyâ'e', 14. kelime); "
        "'yunezzelu' 3MS (fiil uyumu; edilgen; 16. kelime — naib-i faili 17. kelime); 'l-qur'ânu' ('yunezzelu' naib-i faili; adlı kitap; 17. kelime); 'tubde' faili (adsız; edilgen — nâib fâil 3FS, 18. kelime); "
        "''afa' 3MS (fiil uyumu; 20. kelime — fail 21. kelime); 'llâhu' (''afa' faili; lafız; 21. kelime); ''anhâ' 3FS (adsız; gönderge 'eşyâ'e', 22. kelime); 'llâhu' (mübtedâ; lafız; 23. kelime)")
T102 = ("'se'elehâ' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'se'elehâ' mef'ûlü 3FS (adsız; gönderge 5:101 7. kelime, 2. kelime); 'qavmun' ('se'elehâ' faili; nekre; 3. kelime); muhatap 2MP (adsız; 'qablikum' — 5. kelime); "
        "'asbahû' faili 3MP (adsız; gönderge 'qavmun', 7. kelime); 'bihâ' 3FS (adsız; gönderge 5:101 7. kelime, 8. kelime)")
T103 = ("'ce'ale' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'llâhu' ('ce'ale' faili; lafız; 3. kelime); 'llezîne keferû' ('lâkinne' ismi; 13-14. kelime); 'keferû' faili 3MP (adsız; gönderge 'llezîne', 14. kelime); "
        "'yefterûne' faili 3MP (adsız; 15. kelime); 'llâhi' (mecrur; lafız; 17. kelime); 'ekseruhum' iyelik 3MP (adsız; gönderge 'llezîne', 19. kelime); 'ya'qilûn' faili 3MP (adsız; 21. kelime)")
T104 = ("'qîle' 3MS (fiil uyumu; edilgen; 2. kelime — naib-i faili söz); 'lehum' 3MP (adsız; gönderge 5:103 13-14. kelime, 3. kelime); muhatap 2MP (adsız; söz içi; 'te'âlev' — 4. kelime); "
        "'enzele' 3MS (fiil uyumu; 7. kelime — fail 8. kelime); 'llâhu' ('enzele' faili; lafız; 8. kelime); 'r-rasûli' (adlı rol; 10. kelime); 'qâlû' faili 3MP (adsız; 11. kelime); "
        "konuşan 1P (adsız; söz içi; 'hasbunâ', 'vecednâ', 'âbâ'enâ' — 12., 14. ve 16. kelime); ''aleyhi' 3MS (adsız; söz içi; gönderge 'mâ', 15. kelime); "
        "'kâne' 3MS (fiil uyumu; 18. kelime — ismi 19. kelime); 'âbâ'uhum' ('kâne' ismi; iyelik 3MP adsız; 19. kelime); 'ya'lemûne' faili 3MP (adsız; 21. kelime); 'yehtedûn' faili 3MP (adsız; 24. kelime)")
T105 = ("hitap 'yâ eyyuhe'llezîne âmenû' (1-3. kelime); 'âmenû' faili 3MP (adsız; 3. kelime); muhatap 2MP (adsız; ''aleykum', 'enfusekum', 'yadurrukum', 'htedeytum', 'merci'ukum', 'fe-yunebbi'ukum', 'kuntum', 'ta'melûn' — 4., 5., 7., 11., 14., 16., 18. ve 19. kelime); "
        "'yadurrukum' 3MS (fiil uyumu; 7. kelime — fail 8. kelime); 'men dalle' ('yadurrukum' faili; ilgi; 8-9. kelime); 'dalle' 3MS (adsız; gönderge 'men', 9. kelime); "
        "'llâhi' (haber — mecrur; lafız; 13. kelime); 'fe-yunebbi'ukum' 3MS (adsız; gönderge lafız, 16. kelime)")

D = {}
D[101] = ("◇ 'yâ eyyuhe'llezîne âmenû lâ tes'elû 'an eşyâ'e in tubde lekum tesu'kum ve in tes'elû 'anhâ hîne yunezzelu'l-qur'ânu tubde lekum 'afa'llâhu 'anhâ ve'llâhu ğafûrun halîm' — "
 "'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF 3MP IV. bab + 'lâ' + IMPF 2MP I. bab + ''an' + çoğul 'şey'' + 'in' + edilgen IMPF 3FS I. bab + 'li' + 2MP + IMPF 3FS I. bab + 2MP + 've' + 'in' + IMPF 2MP I. bab + ''an' + 3FS + 'hîn' + edilgen IMPF 3MS II. bab + belirli özel ad 'qur'ân' + "
 "edilgen IMPF 3FS I. bab + 'li' + 2MP + PERF 3MS I. bab + lafız + ''an' + 3FS + 've' + lafız + nekre 'ğafûr' + nekre 'halîm' "
 "(ölçüm edim yasak, nida, şart, kip COND 2 · PRO 1 · VOC 1; 2MP 7 · 3FS 5 · 3MP 2 · 3MS 2; bab I. bab ×6 · II. bab ×1 · IV. bab ×1; EDİLGEN 3/8 fiil). "
 "Allah lafzı 21. ve 23. sırada (ölçüm allah z=1,07); Rab yok; ölçüm '{{1|esmâ غَفُور 24\\. sırada, SON konum, MÜHÜR \\| حَلِيم 25\\. sırada, SON konum, MÜHÜR}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET (ÇİFT) ton cemâl' (uyuşuyor) — esma_el kaydı 'ilahi' — 've'llâhu ğafûrun halîm', kural ''ve'llâhu X' kuralı → ilahi' (okuma); ölçüm aktör '{{1|adlı قُرْءان 17\\. sırada \\(kitab, rol fail\\)}}' — satır aynen. "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=25 (n z=1,34); ölçüm '{{1|fâsıla حليم → م, N sınıfı}}' — satır aynen; ölçüm '{{1|EDİLGEN 3/8 fiil, pas z=1,81}}' — satır aynen ('tubde' 9., 'yunezzelu' 16., 'tubde' 18. kelime); "
 "ölçüm '{{1|simetri \\[6, 2, 10, 2\\]}}' — satır aynen; ölçüm '{{1|harf 106 → harf3 101, isaret 5}}' — satır aynen; ölçüm '{{1|dış düğüm 3}}' — satır aynen. "
 "Ölçüm VOC 1: 'yâ' (1. kelime); PRO 1: 'lâ' (4. kelime); COND 2: 'in' (8. ve 12. kelime); 've in' (12.)'daki 've' CONJ, 've'llâhu' (23.)'daki 've' REM, 'hîne' (15.) T (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhu' 21. / 23. kelime), بدو ×2 ('tubde' 9. / 18. kelime), سأل ×2 ('tes'elû' 5. / 13. kelime) (okuma). "
 + T101 + " (okuma). "
 + cumle(say('say 5:101 1-4', "yâ eyyuhe'llezîne âmenû lâ", True), say('dizi 5 101 1 4', "eyy ellezî âmene lâ"), say('say 5:101 1-3', "yâ eyyuhe'llezîne âmenû"), say('dizi 5 101 1 3', "eyy ellezî âmene")) + ' '
 + cumle(say('say 5:101 4-7', "lâ tes'elû 'an eşyâ'", True), say('say 5:101 5-7', "tes'elû 'an eşyâ'"), say('say 5:101 8-11', "in tubde lekum tesu'kum"), say('say 5:101 9-10', "tubde lekum")) + ' '
 + cumle(say('say 5:101 12-14 --on', "ve in tes'elû 'anhâ", True), say('say 5:101 15-17', "hîne yunezzelu'l-qur'ân"), say('say 5:101 16-17', "yunezzelu'l-qur'ân"), say('say 5:101 18-19', "tubde lekum")) + ' '
 + cumle(say('say 5:101 20-22', "'afa'llâhu 'anhâ", True), say('say 5:101 20-21', "'afa'llâh"), say('say 5:101 23-25 --on', "ve'llâhu ğafûrun halîm"), say('say 5:101 24-25', "ğafûrun halîm"), say('dizi 5 101 23 25', "allâh ğafûr halîm")) + ' '
 "Ölçüm xref 2:225 (emsal olarak basıldı), 3:155 (emsal olarak basıldı) ve okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'eyy ellezî âmene lâ' ve 'eyy ellezî âmene' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K2 'hîne' (15. kelime).",
 "◈B — —",
 "◈D — D1 'yâ' + 'ellezî' + PERF + 'lâ' + IMPF + ''an' + çoğul + 'in' + IMPF + 'li' + IMPF + 've' + 'in' + IMPF + ''an' + 'hîn' + IMPF + belirli + IMPF + 'li' + PERF + lafız + ''an' + 've' + lafız + nekre + nekre; "
 "D2 yasak, nida, şart, VOC ('yâ' 1. kelime), PRO ('lâ' 4. kelime), COND ('in' 8. ve 12. kelime); D3 أله ×2, بدو ×2, سأل ×2; 3:155 eşi; D4 2MP 7 · 3FS 5 · 3MP 2 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T101 + "; aktör Kur'an (ölçüm); A2 açıklanınca üzecek şeyleri sorma yasağı; Kur'an inerken sorduklarının açıklanması; Allah'ın affı; A3 —; "
 "A4 " + BOLUM + "; bölüm açılışı; hitap açılır ('yâ eyyuhe'llezîne âmenû', 1-3. kelime); edim geçişi emir, nida, şart → yasak, nida, şart (ayetler arası); "
 "şart → cevap (ayet içi; COND 'in' 8. kelime: 'in tubde lekum' / 'tesu'kum' (11. kelime)); şart → cevap (ayet içi; COND 'in' 12. kelime: 'in tes'elû 'anhâ' / 'tubde lekum' (18. kelime)).",
)

D[102] = ("◇ 'qad se'elehâ qavmun min qablikum summe asbahû bihâ kâfirîn' — "
 "'qad' + PERF 3MS I. bab + 3FS + nekre 'qavm' + 'min' + 'qabl' + 2MP + 'summe' + PERF 3MP IV. bab + 'bi' + 3FS + çoğul etken ortaç 'kâfir' "
 "(ölçüm edim haber, kip CERT 1; 2MP 1 · 3FS 2 · 3MP 2 · 3MS 1; bab I. bab ×1 · IV. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=9 (n z=-0,36); ölçüm '{{2|fâsıla كفرين → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|harf 35 → harf3 33, isaret 2}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (1. kelime); 'summe' (6.) CONJ (okuma). "
 + T102 + " (okuma). "
 + cumle(say('say 5:102 1-3', "qad se'elehâ qavm", True), say('say 5:102 2-3', "se'elehâ qavm"), say('say 5:102 3-5', "qavmun min qablikum"), say('say 5:102 4-5', "min qablikum")) + ' '
 + cumle(say('say 5:102 6-9', "summe asbahû bihâ kâfirîn", True), say('say 5:102 7-9', "asbahû bihâ kâfirîn"), say('say 5:102 8-9', "bihâ kâfirîn")) + ' '
 "Ölçüm xref yok ('xref üçü de boş'). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'qad' + PERF + nekre + 'min' + izafet + 'summe' + PERF + 'bi' + çoğul; "
 "D2 haber, CERT ('qad' 1. kelime); D3 —; D4 2MP 1 · 3FS 2 · 3MP 2 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T102 + "; aktör yok (ölçüm); A2 önceki bir kavmin onları sorması ve sonra onlar yüzünden kâfir olması; A3 —; "
 "A4 " + BOLUM + "; edim geçişi yasak, nida, şart → haber (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası).",
)

D[103] = ("◇ 'mâ ce'ale'llâhu min bahîratin ve lâ sâ'ibetin ve lâ vasîletin ve lâ hâmin ve lâkinne'llezîne keferû yefterûne 'ale'llâhi'l-kezibe ve ekseruhum lâ ya'qilûn' — "
 "'mâ' + PERF 3MS I. bab + lafız + 'min' + nekre 'bahîra' + 've' + 'lâ' + nekre etken ortaç 'sâ'ibe' + 've' + 'lâ' + nekre 'vaṣîle' + 've' + 'lâ' + nekre 'hâm' + 've' + 'lâkinne' + 'ellezî' + PERF 3MP I. bab + IMPF 3MP VIII. bab + ''alâ' + lafız + belirli 'kezib' + "
 "'ve' + 'eksar' + 3MP + 'lâ' + IMPF 3MP I. bab "
 "(ölçüm edim haber, kip NEG 5; 3MP 7 · 3MS 1; bab I. bab ×3 · VIII. bab ×1). "
 "Allah lafzı 3. ve 17. sırada (ölçüm allah z=1,38); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=21 (n z=0,91); ölçüm '{{3|HAPAKS: سيب}}' — satır aynen (kök bu blokta tabloya eklendi); ölçüm '{{3|hapaks z=3,28}}' — satır aynen; "
 "ölçüm '{{3|fâsıla يعقلون → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|sayı işareti أَكْثَر}}' — satır aynen; ölçüm '{{3|simetri \\[3, 4, 8, 1\\]}}' — satır aynen; ölçüm '{{3|harf 93 → harf3 85, isaret 8}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 5: 'mâ' (1. kelime), 'lâ' (6., 8., 10. ve 20. kelime); 've lâ' (6., 8., 10.)'daki 've' CONJ, 've lâkinne' (12.)'daki 've' REM, 've ekseruhum' (19.)'daki 've' CIRC (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhu' 3. / 'llâhi' 17. kelime) (okuma). "
 + T103 + " (okuma). "
 + cumle(say('say 5:103 1-3', "mâ ce'ale'llâh", True), say('say 5:103 2-3', "ce'ale'llâh"), say('say 5:103 4-11', "min bahîratin ve lâ sâ'ibetin ve lâ vasîletin ve lâ hâm"), say('say 5:103 4-5', "min bahîra"), say('say 5:103 6-7 --on', "ve lâ sâ'ibe")) + ' '
 + cumle(say('say 5:103 12-15 --on', "ve lâkinne'llezîne keferû yefterûn", True), say('say 5:103 13-14', "llezîne keferû"), say('say 5:103 14-15', "keferû yefterûn"), say('say 5:103 15-18', "yefterûne 'ale'llâhi'l-kezib"), say('say 5:103 16-18', "'ale'llâhi'l-kezib")) + ' '
 + cumle(say('say 5:103 19-21 --on', "ve ekseruhum lâ ya'qilûn", True), say('say 5:103 20-21', "lâ ya'qilûn")) + ' '
 "Ölçüm xref yok ('xref üçü de boş'). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K1 'bahîratin' (5. kelime).",
 "◈B — —",
 "◈D — D1 'mâ' + PERF + lafız + 'min' + nekre + 've' + 'lâ' + nekre + 've' + 'lâ' + nekre + 've' + 'lâ' + nekre + 've' + 'lâkinne' + 'ellezî' + PERF + IMPF + ''alâ' + lafız + belirli + 've' + izafet + 'lâ' + IMPF; "
 "D2 haber, NEG ('mâ' 1., 'lâ' 6., 8., 10. ve 20. kelime); D3 أله ×2; D4 3MP 7 · 3MS 1, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T103 + "; aktör yok (ölçüm); A2 bahîre, sâibe, vasîle ve hâmînin Allah'ça kılınmaması; inkâr edenlerin Allah'a karşı yalan uydurması; çoğunun akletmemesi; A3 —; "
 "A4 " + BOLUM + ".",
)

D[104] = ("◇ 've izâ qîle lehum te'âlev ilâ mâ enzele'llâhu ve ile'r-rasûli qâlû hasbunâ mâ vecednâ 'aleyhi âbâ'enâ e-ve-lev kâne âbâ'uhum lâ ya'lemûne şey'en ve lâ yehtedûn' — "
 "'ve' + 'izâ' + edilgen PERF 3MS I. bab + 'li' + 3MP + IMPV 2MP IV. bab + 'ilâ' + 'mâ' + PERF 3MS IV. bab + lafız + 've' + 'ilâ' + belirli 'rasûl' + PERF 3MP I. bab + 'hasb' + 1P + 'mâ' + PERF 1P I. bab + ''alâ' + 3MS + çoğul 'âbâ'' + 1P + "
 "'e' + 've' + 'lev' + PERF 3MS I. bab + çoğul 'âbâ'' + 3MP + 'lâ' + IMPF 3MP I. bab + nekre 'şey'' + 've' + 'lâ' + IMPF 3MP VIII. bab "
 "(ölçüm edim soru, emir, şart, kip COND 1 · IMPV 1 · INTG 1 · NEG 2; 1P 4 · 2MP 2 · 3MP 8 · 3MS 4; bab I. bab ×5 · IV. bab ×2 · VIII. bab ×1; EDİLGEN 1/8 fiil). "
 "Allah lafzı 8. sırada (ölçüm allah z=0,31); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=24 (n z=1,23); ölçüm '{{4|fâsıla يهتدون → ن, N sınıfı}}' — satır aynen; ölçüm '{{4|EDİLGEN 1/8 fiil, pas z=0,38}}' — satır aynen ('qîle' 2. kelime); "
 "ölçüm '{{4|simetri \\[3, 1, 13, 1\\]}}' — satır aynen; ölçüm '{{4|harf 106 → harf3 102, isaret 4}}' — satır aynen; ölçüm '{{4|dış düğüm 8}}' — satır aynen; ölçüm '{{4|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 'lev' (17. kelime); IMPV 1: 'te'âlev' (4. kelime); INTG 1: 'e' (17. kelime); NEG 2: 'lâ' (20. ve 23. kelime); 've izâ' (1.)'daki 've' REM ve 'izâ' T, 've ile'r-rasûli' (9.) ve 've lâ' (23.)'daki 've' CONJ, 'e-ve-lev' (17.)'daki 've' SUP (okuma). "
 "Kök ikilemesi (ölçüm) أبو ×2 ('âbâ'enâ' 16. / 'âbâ'uhum' 19. kelime), قول ×2 ('qîle' 2. / 'qâlû' 11. kelime) (okuma). "
 + T104 + " (okuma). "
 + cumle(say('say 5:104 1-3 --on', "ve izâ qîle lehum", True), say('say 5:104 2-3', "qîle lehum"), say('say 5:104 4-8', "te'âlev ilâ mâ enzele'llâh"), say('say 5:104 6-8', "mâ enzele'llâh"), say('dizi 5 104 6 8', "mâ enzele allâh"), say('say 5:104 9-10 --on', "ve ile'r-rasûl")) + ' '
 + cumle(say('say 5:104 11-16', "qâlû hasbunâ mâ vecednâ 'aleyhi âbâ'enâ", True), say('say 5:104 13-16', "mâ vecednâ 'aleyhi âbâ'enâ")) + ' '
 + cumle(say('say 5:104 17-24', "e-ve-lev kâne âbâ'uhum lâ ya'lemûne şey'en ve lâ yehtedûn", True), say('say 5:104 17-19', "e-ve-lev kâne âbâ'uhum"), say('say 5:104 20-22', "lâ ya'lemûne şey'en"), say('say 5:104 23-24 --on', "ve lâ yehtedûn")) + ' '
 "Ölçüm xref 2:170 (emsal olarak basıldı), 4:171 (emsal olarak basıldı), okunmuş 6 ayet ve henüz okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıbı: 'mâ enzele allâh' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'izâ' + PERF + 'li' + IMPV + 'ilâ' + 'mâ' + PERF + lafız + 've' + 'ilâ' + belirli + PERF + izafet + 'mâ' + PERF + ''alâ' + çoğul + 'e' + 've' + 'lev' + PERF + çoğul + 'lâ' + IMPF + nekre + 've' + 'lâ' + IMPF; "
 "D2 soru, emir, şart, COND ('lev' 17. kelime), IMPV ('te'âlev' 4. kelime), INTG ('e' 17. kelime), NEG ('lâ' 20. ve 23. kelime); D3 أبو ×2, قول ×2; 2:170 eşi; D4 1P 4 · 2MP 2 · 3MP 8 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T104 + "; aktör yok (ölçüm); A2 Allah'ın indirdiğine ve elçiye çağrı; ataların yoluna bağlılık sözü; bilmeyen ve doğru yolu bulamayan atalara uymanın kınanması; "
 "A3 'te'âlev ilâ mâ enzele'llâhu ve ile'r-rasûl' (söz içi, 4-10. kelime); 'hasbunâ mâ vecednâ 'aleyhi âbâ'enâ' (söz içi, 12-16. kelime); "
 "A4 " + BOLUM + "; söz açılır (4. kelime); söz kapanır (10. kelime, ayet içi); söz açılır (12. kelime); söz kapanır (16. kelime, ayet içi); edim geçişi haber → soru, emir, şart (ayetler arası); "
 "şart → cevap (ayet içi; COND 'lev' 17. kelime: 'e-ve-lev kâne âbâ'uhum' — cevap mahzuf (okuma)).",
)

D[105] = ("◇ 'yâ eyyuhe'llezîne âmenû 'aleykum enfusekum lâ yadurrukum men dalle izâ'htedeytum ile'llâhi merci'ukum cemî'an fe-yunebbi'ukum bi-mâ kuntum ta'melûn' — "
 "'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF 3MP IV. bab + ism-i fiil ''alâ' + 2MP + çoğul 'nefs' + 2MP + 'lâ' + IMPF 3MS I. bab + 2MP + 'men' + PERF 3MS I. bab + 'izâ' + PERF 2MP VIII. bab + 'ilâ' + lafız + 'merci'' + 2MP + nekre 'cemî'' + "
 "'fe' + IMPF 3MS II. bab + 2MP + 'bi' + 'mâ' + PERF 2MP I. bab + IMPF 2MP I. bab "
 "(ölçüm edim emir, nida, kip IMPV 1 · NEG 1 · VOC 1; 2MP 11 · 3MP 2 · 3MS 3; bab I. bab ×4 · II. bab ×1 · IV. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 13. sırada (ölçüm allah z=0,52); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=19 (n z=0,70); ölçüm '{{5|fâsıla تعملون → ن, N sınıfı}}' — satır aynen; ölçüm '{{5|simetri \\[3, 2, 6, 1\\]}}' — satır aynen; "
 "ölçüm '{{5|harf 90 → harf3 86, isaret 4}}' — satır aynen; ölçüm '{{5|dış düğüm 0}}' — satır aynen. "
 "Ölçüm VOC 1: 'yâ' (1. kelime); IMPV 1: ''aleykum' (4. kelime; morph NV IMPV); NEG 1: 'lâ' (6. kelime); 'fe-yunebbi'ukum' (16.)'daki 'fe' REM, 'izâ' (10.) T (okuma). "
 + T105 + " (okuma). "
 + cumle(say('say 5:105 1-3', "yâ eyyuhe'llezîne âmenû", True), say('dizi 5 105 1 3', "eyy ellezî âmene"), say('say 5:105 4-5', "'aleykum enfusekum")) + ' '
 + cumle(say('say 5:105 6-9', "lâ yadurrukum men dalle", True), say('say 5:105 10-11', "izâ'htedeytum")) + ' '
 + cumle(say('say 5:105 12-18', "ile'llâhi merci'ukum cemî'an fe-yunebbi'ukum bi-mâ kuntum", True), say('dizi 5 105 12 18', "ilâ allâh merci' cemî' nebbe'e mâ kâne"), say('say 5:105 12-14', "ile'llâhi merci'ukum"),
         say('say 5:105 16-19 --on', "fe-yunebbi'ukum bi-mâ kuntum ta'melûn"), say('say 5:105 17-19', "bi-mâ kuntum ta'melûn"), say('say 5:105 18-19', "kuntum ta'melûn")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: 'ilâ allâh merci' cemî' nebbe'e mâ kâne' ve 'eyy ellezî âmene' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'dalle' / 'htedeytum' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'yâ' + 'ellezî' + PERF + IMPV + çoğul + 'lâ' + IMPF + 'men' + PERF + 'izâ' + PERF + 'ilâ' + lafız + izafet + nekre + 'fe' + IMPF + 'bi' + 'mâ' + PERF + IMPF; "
 "D2 emir, nida, VOC ('yâ' 1. kelime), IMPV (''aleykum' 4. kelime), NEG ('lâ' 6. kelime); D3 —; D4 2MP 11 · 3MP 2 · 3MS 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T105 + "; aktör yok (ölçüm); A2 kendini gözetme emri; doğru yolu bulana sapanın zarar vermemesi; hepsinin Allah'a dönüşü ve yapılanın haber verilmesi; A3 —; "
 "A4 " + BOLUM + "; hitap açılır ('yâ eyyuhe'llezîne âmenû', 1-3. kelime); edim geçişi soru, emir, şart → emir, nida (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası).",
)

out = ['# ── blok 5:101-105 (2026-11-17) ──', 'MEAL31 = {']
for n in range(101, 106):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M31 = {']
for n in range(101, 106):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL31); M.update(M31)']
open('/home/claude/yamalar/metin_5_101_105.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
