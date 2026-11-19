# sûre 6 blok 4 (6:16-19) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b04/say2.txt'
os.environ['OLC'] = '/home/claude/b04/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Mülk kimin; şahit olarak Allah' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'



MEAL = {
 16: "O gün kimden o çevrilirse, ona gerçekten rahmet etmiştir. İşte bu, apaçık kurtuluştur.",
 17: "Allah sana bir zarar dokundurursa, onu O'ndan başka kaldıracak yoktur. Sana bir hayır dokundurursa, O her şeye gücü yetendir.",
 18: "O, kullarının üstünde kahredendir. O, hakîmdir, haberdardır.",
 19: "De ki: Şahitlikçe hangi şey daha büyüktür? De ki: Allah benim aramda ve sizin aranızda şahittir. Bu Kur'an bana, onunla sizi ve ulaştığı kimseyi uyarayım diye vahyolundu. Siz gerçekten Allah ile beraber başka ilahlar olduğuna mı şahitlik ediyorsunuz? De ki: Ben şahitlik etmem. De ki: O ancak bir ilahtır; ben sizin ortak koştuklarınızdan uzağım.",
}

T = {}
T[16] = ("'yusraf' 3MS (fiil uyumu; edilgen; naib-i faili zamir — gönderge 6:15'teki azap, 2. kelime); ''anhu' 3MS (adsız; gönderge 'men', 3. kelime); "
         "'rahimehû' 3MS (adsız; gönderge 6:15 6. kelime, 6. kelime); 'rahimehû' zamiri 3MS (adsız; gönderge 'men', 6. kelime)")
T[17] = ("muhatap 2MS (adsız; 'yemseske', 'yemseske' — 2. ve 11. kelime); 'yemseske' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'lehû' 3MS (adsız; gönderge 'durr', 7. kelime); "
         "'huve' 3MS (adsız; gönderge lafız, 9. kelime); 'yemseske' 3MS (adsız; gönderge lafız, 11. kelime); 'fe-huve' 3MS (adsız; gönderge lafız, 13. kelime)")
T[18] = ("'ve huve' 3MS (adsız; gönderge 6:17 3. kelime, 1. kelime); ''ibâdihî' 3MS (adsız; gönderge 6:17 3. kelime, 4. kelime); 've huve' 3MS (adsız; gönderge 6:17 3. kelime, 5. kelime)")
T[19] = ("muhatap 2MS (adsız; 'qul', 'qul', 'qul', 'qul' — 1., 6., 26. ve 29. kelime); konuşan 1S (adsız; söz içi; 'beynî', 'ileyye', 'li-unzirakum', 'eşhed', 'innenî' — 9., 12., 15., 28. ve 34. kelime); "
         "muhatap 2MP (adsız; söz içi; 'beynekum', 'li-unzirakum', 'e'innekum', 'le-teşhedûne', 'tuşrikûn' — 10., 15., 19., 20. ve 37. kelime); "
         "'ûhiye' 3MS (fiil uyumu; edilgen; söz içi; naib-i faili 'l-qur'ânu' (14. kelimedeki ad), 11. kelime); 'bihî', 'beleğ' 3MS (adsız; söz içi; gönderge 'l-qur'ânu' — 16. ve 18. kelime); "
         "'huve' 3MS (adsız; söz içi; gönderge lafız, 31. kelime)")

D = {}
D[16] = ("◇ 'men yusraf 'anhu yevme'izin fe-qad rahimehû ve zâlike'l-fevzu'l-mubîn' — "
 "'men' + edilgen IMPF 3MS I. bab + ''an' + 3MS + 'yevm' + 'iz' + 'fe' + 'qad' + PERF 3MS I. bab + 3MS + 've' + 'zâ' + belirli 'fevz' + belirli etken ortaç 'mubîn' "
 "(ölçüm edim şart, kip CERT 1 · COND 1; 3MS 4; bab I. bab ×2). "
 "Lafız yok; Rab yok; ölçüm '{{1|esmâ مُبِين 9\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton denge' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'l-fevzu'l-mubîn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (kurtuluşun sıfatı) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=9 (n z=-0,36); ölçüm '{{1|EDİLGEN 1/2 fiil, pas z=2,52}}' — satır aynen; "
 "ölçüm '{{1|fâsıla ٱلمبين → ن, N sınıfı}}' — satır aynen (6:15 م → 6:16 ن); "
 "ölçüm '{{1|simetri \\[3, 1, 5, 1\\]}}' — satır aynen; ölçüm '{{1|harf 39 → harf3 36, isaret 3}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen; ölçüm iltifât 1 (6:15 1S baskın → 6:16 3MS). "
 "Ölçüm COND 1: 'men' (1. kelime); CERT 1: 'fe-qad' (5. kelime); 'fe-qad' (5.) kelimesindeki 'fe' RSLT; 've zâlike' (7.) kelimesindeki 've' REM (okuma). "
 + T[16] + " (okuma). "
 + cumle(say('say 6:16 1-4', "men yusraf 'anhu yevme'izin", True), say('say 6:16 5-6', "fe-qad rahimeh"), say('say 6:16 4-4', "yevme'izin")) + ' '
 + cumle(say('say 6:16 7-9', "ve zâlike'l-fevzu'l-mubîn", True), say('say 6:16 8-9', "l-fevzu'l-mubîn"), say('dizi 6 16 7 9', "zâ fevz mubîn"), say('dizi 6 16 8 9', "fevz mubîn")) + ' '
 "Ölçüm xref 40:9 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K2 'yevme'izin' (4. kelime).",
 "◈B — —",
 "◈D — D1 'men' + IMPF + ''an' + 'yevm' + 'iz' + 'fe' + 'qad' + PERF + 've' + 'zâ' + belirli + belirli; "
 "D2 şart; COND ('men' 1. kelime), CERT ('fe-qad' 5. kelime); D3 —; 40:9 eşi; D4 3MS 4, sahset ['3'], iltifât 1.",
 "◈A — A1 " + T[16] + "; aktör yok (ölçüm); A2 o gün azabın çevrildiği kimseye rahmet; apaçık kurtuluş; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 1 → 3 (ayetler arası); edim geçişi emir → şart (ayetler arası); "
 "şart → cevap (ayet içi; COND 'men' 1. kelime: 'men yusraf 'anhu yevme'izin' / 'fe-qad rahimeh' (5. kelime)).",
)

D[17] = ("◇ 've in yemseske'llâhu bi-durrin fe-lâ kâşife lehû illâ huve ve in yemseske bi-xayrin fe-huve 'alâ kulli şey'in qadîr' — "
 "'ve' + 'in' + IMPF 3MS I. bab + 2MS + lafız + 'bi' + nekre 'durr' + 'fe' + 'lâ' + etken ortaç 'kâşif' + 'li' + 3MS + 'illâ' + 'huve' + 've' + 'in' + IMPF 3MS I. bab + 2MS + 'bi' + nekre 'xayr' + 'fe' + 'huve' + ''alâ' + 'kull' + nekre 'şey'' + nekre 'qadîr' "
 "(ölçüm edim şart, kip COND 2 · NEG 1; 2MS 2 · 3MS 5; bab I. bab ×2). "
 "Allah lafzı 3. sırada (ölçüm allah z=0,65); Rab yok; ölçüm '{{2|esmâ قَدِير 17\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton celâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el EVET — ölçümle uyuşmuyor, tam okuma sonu); "
 "esma_el kaydı 'ilahi' — 'fe-huve 'alâ kulli şey'in qadîr', kural 'zamirin haberi → ilahi' (Allah) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=17 (n z=0,49); ölçüm '{{2|fâsıla قدير → ر, R sınıfı}}' — satır aynen (6:16 ن → 6:17 ر); "
 "ölçüm '{{2|simetri \\[3, 1, 10, 1\\]}}' — satır aynen; ölçüm '{{2|harf 62 → harf3 56, isaret 6}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen. "
 "Ölçüm COND 2: 'in' (1. ve 10. kelime); NEG 1: 'fe-lâ' (5. kelime); 've in' (1. ve 10.) kelimelerindeki 've' CONJ; 'fe-lâ' (5.) ve 'fe-huve' (13.) kelimelerindeki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) مسس ×2 ('yemseske' 2. / 'yemseske' 11. kelime) (okuma). "
 + T[17] + " (okuma). "
 + cumle(say('say 6:17 1-4', "ve in yemseske'llâhu bi-durr", True), say('say 6:17 2-4', "yemseske'llâhu bi-durr"), say('say 6:17 5-9', "fe-lâ kâşife lehû illâ huve"), say('say 6:17 6-9', "kâşife lehû illâ huve"), say('dizi 6 17 1 9', "in messe allâh durr lâ kâşif _ illâ _")) + ' '
 + cumle(say('say 6:17 10-12', "ve in yemseske bi-xayr", True), say('say 6:17 13-17', "fe-huve 'alâ kulli şey'in qadîr"), say('say 6:17 14-16', "'alâ kulli şey'"), say('say 6:17 15-17', "kulli şey'in qadîr"), say('dizi 6 17 14 17', "'alâ kull şey' qadîr")) + ' '
 "Ölçüm xref 10:107 (emsal olarak basıldı) ve okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: ''alâ kull şey'' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'durr' / 'xayr' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'in' + IMPF + lafız + 'bi' + nekre + 'fe' + 'lâ' + izafet + 'li' + 'illâ' + 'huve' + 've' + 'in' + IMPF + 'bi' + nekre + 'fe' + 'huve' + ''alâ' + izafet + nekre + nekre; "
 "D2 şart; COND ('in' 1. ve 10. kelime), NEG ('fe-lâ' 5. kelime); D3 مسس ×2; 10:107 eşi; D4 2MS 2 · 3MS 5, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[17] + "; aktör yok (ölçüm); A2 Allah'ın dokundurduğu zararı O'ndan başka kaldıracak olmaması; hayır dokundurma; her şeye gücü yeten; "
 "A3 —; "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; COND 'in' 1. kelime: 'in yemseske'llâhu bi-durr' / 'fe-lâ kâşife lehû illâ huve' (5. kelime)); "
 "şart → cevap (ayet içi; COND 'in' 10. kelime: 'in yemseske bi-xayr' / 'fe-huve 'alâ kulli şey'in qadîr' (13. kelime)).",
)

D[18] = ("◇ 've huve'l-qâhiru fevqa 'ibâdihî ve huve'l-hakîmu'l-xabîr' — "
 "'ve' + 'huve' + belirli etken ortaç 'qâhir' + 'fevq' + çoğul ''abd' + 3MS + 've' + 'huve' + belirli 'hakîm' + belirli 'xabîr' "
 "(ölçüm edim haber, kip yok; 3MS 3; bab yok). "
 "Lafız yok; Rab yok; ölçüm '{{3|esmâ حَكِيم 6\\. sırada, SON konum, MÜHÜR \\| خَبِير 7\\. sırada, SON konum, MÜHÜR}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET (ÇİFT) ton denge' (uyuşuyor) — esma_el kaydı 'ilahi' — 've huve'l-hakîmu'l-xabîr', kural 'zamirin haberi → ilahi' (Allah) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=7 (n z=-0,58); ölçüm '{{3|fâsıla ٱلخبير → ر, R sınıfı}}' — satır aynen (6:17 ر → 6:18 ر); "
 "ölçüm '{{3|harf 34 → harf3 32, isaret 2}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; 've huve' (1. ve 5.) kelimelerindeki 've' CONJ (okuma). "
 + T[18] + " (okuma). "
 + cumle(say('say 6:18 1-4', "ve huve'l-qâhiru fevqa 'ibâdih", True), say('say 6:18 2-4', "l-qâhiru fevqa 'ibâdih"), say('dizi 6 18 1 4', "_ qâhir fevq 'abd")) + ' '
 + cumle(say('say 6:18 5-7', "ve huve'l-hakîmu'l-xabîr", True), say('say 6:18 6-7', "l-hakîmu'l-xabîr"), say('dizi 6 18 5 7', "_ hakîm xabîr")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: '_ qâhir fevq 'abd' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'huve' + belirli + 'fevq' + izafet + 've' + 'huve' + belirli + belirli; "
 "D2 haber; D3 —; D4 3MS 3, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[18] + "; aktör yok (ölçüm); A2 kullarının üstünde kahreden; hakîm ve haberdar; "
 "A3 —; "
 "A4 " + BOLUM + "; edim geçişi şart → haber (ayetler arası).",
)

D[19] = ("◇ 'qul eyyu şey'in ekberu şehâdeten quli'llâhu şehîdun beynî ve beynekum ve ûhiye ileyye hâze'l-qur'ânu li-unzirakum bihî ve men beleğ e'innekum le-teşhedûne enne ma'a'llâhi âliheten uxrâ qul lâ eşhed qul innemâ huve ilâhun vâhidun ve innenî berî'un mimmâ tuşrikûn' — "
 "IMPV 2MS I. bab + 'eyy' + nekre 'şey'' + 'ekber' + nekre 'şehâde' + IMPV 2MS I. bab + lafız + nekre 'şehîd' + 'beyn' + 1S + 've' + 'beyn' + 2MP + 've' + edilgen PERF 3MS IV. bab + 'ilâ' + 1S + 'hâ' + 'zâ' + belirli 'qur'ân' + "
 "'li' + IMPF 1S IV. bab + 2MP + 'bi' + 3MS + 've' + 'men' + PERF 3MS I. bab + 'e' + 'inne' + 2MP + 'le' + IMPF 2MP I. bab + 'enne' + 'ma'a' + lafız + nekre çoğul 'ilâh' + 'âxar' + "
 "IMPV 2MS I. bab + 'lâ' + IMPF 1S I. bab + IMPV 2MS I. bab + 'inne' + 'mâ' + 'huve' + nekre 'ilâh' + nekre 'vâhid' + 've' + 'inne' + 1S + nekre 'berî'' + 'min' + 'mâ' + IMPF 2MP IV. bab "
 "(ölçüm edim soru, emir, kip EMPH 1 · IMPV 4 · INTG 2 · NEG 1; 1S 5 · 2MP 7 · 2MS 4 · 3MS 4; bab I. bab ×7 · IV. bab ×3). "
 "Allah lafzı 7. ve 23. sırada (ölçüm allah z=0,55); Rab yok; ölçüm '{{4|esmâ شَهِيد 8\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür hayır' (uyuşuyor) — esma_el kaydı 'ilahi' — 'llâhu şehîdun beynî ve beynekum', kural 'lafzın haberi → ilahi' (Allah) (okuma); "
 "ölçüm '{{4|aktör: adlı قُرْءان 14\\. sırada \\(kitab, rol fail\\)}}' — satır aynen. "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=37 (n z=2,61); ölçüm '{{4|EDİLGEN 1/10 fiil, pas z=0,24}}' — satır aynen; "
 "ölçüm '{{4|fâsıla تشركون → ن, N sınıfı}}' — satır aynen (6:18 ر → 6:19 ن); ölçüm '{{4|sayı işareti واحِد}}' — satır aynen; "
 "ölçüm '{{4|simetri \\[6, 19, 27, 2\\]}}' — satır aynen; ölçüm '{{4|harf 150 → harf3 137, isaret 13}}' — satır aynen; ölçüm '{{4|dış düğüm 2}}' — satır aynen. "
 "Ölçüm IMPV 4: 'qul' (1., 6., 26. ve 29. kelime); INTG 2: 'eyyu' (2. kelime), 'e'innekum' (19. kelime); EMPH 1: 'le-teşhedûne' (20. kelime); NEG 1: 'lâ' (27. kelime); "
 "'ve beynekum' (10.), 've men' (17.) ve 've innenî' (34.) kelimelerindeki 've' CONJ; 've ûhiye' (11.) kelimesindeki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) أله ×4 ('llâhu' 7. / 'llâhi' 23. / 'âliheten' 24. / 'ilâhun' 32. kelime), بين ×2 ('beynî' 9. / 'beynekum' 10. kelime), شهد ×4 ('şehâdeten' 5. / 'şehîdun' 8. / 'le-teşhedûne' 20. / 'eşhed' 28. kelime), "
 "قول ×4 ('qul' 1. / 'quli' 6. / 'qul' 26. / 'qul' 29. kelime) (okuma). "
 + T[19] + " (okuma). "
 + cumle(say('say 6:19 1-5', "qul eyyu şey'in ekberu şehâde", True), say('say 6:19 2-5', "eyyu şey'in ekberu şehâde"), say('say 6:19 6-10', "quli'llâhu şehîdun beynî ve beynekum"), say('say 6:19 7-10', "llâhu şehîdun beynî ve beynekum")) + ' '
 + cumle(say('say 6:19 11-16', "ve ûhiye ileyye hâze'l-qur'ânu li-unzirakum bih", True), say('say 6:19 11-14', "ve ûhiye ileyye hâze'l-qur'ân"), say('say 6:19 17-18', "ve men beleğ")) + ' '
 + cumle(say('say 6:19 19-25', "e'innekum le-teşhedûne enne ma'a'llâhi âliheten uxrâ", True), say('say 6:19 20-25', "le-teşhedûne enne ma'a'llâhi âliheten uxrâ"), say('dizi 6 19 19 25', "inne şehide enne ma'a allâh ilâh âxar"),
         say('say 6:19 26-28', "qul lâ eşhed"), say('say 6:19 27-28', "lâ eşhed")) + ' '
 + cumle(say('say 6:19 29-33', "qul innemâ huve ilâhun vâhid", True), say('say 6:19 30-33', "innemâ huve ilâhun vâhid"), say('say 6:19 34-37', "ve innenî berî'un mimmâ tuşrikûn"),
         say('say 6:19 35-37', "berî'un mimmâ tuşrikûn"), say('dizi 6 19 35 37', "berî' mimmâ eşrake")) + ' '
 "Ölçüm xref 3:18 (emsal olarak basıldı) ve okunmamış 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'berî' mimmâ eşrake' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'âliheten uxrâ' / 'ilâhun vâhid' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'eyy' + nekre + 'ekber' + nekre + IMPV + lafız + nekre + 'beyn' + 've' + 'beyn' + 've' + PERF + 'ilâ' + 'hâ' + 'zâ' + belirli + 'li' + IMPF + 'bi' + 've' + 'men' + PERF + 'e' + 'inne' + 'le' + IMPF + 'enne' + 'ma'a' + lafız + nekre + 'âxar' + "
 "IMPV + 'lâ' + IMPF + IMPV + 'inne' + 'mâ' + 'huve' + nekre + nekre + 've' + 'inne' + nekre + 'min' + 'mâ' + IMPF; "
 "D2 soru, emir; IMPV ('qul' 1., 6., 26. ve 29. kelime), INTG ('eyyu' 2. kelime, 'e'innekum' 19. kelime), EMPH ('le-teşhedûne' 20. kelime), NEG ('lâ' 27. kelime); D3 أله ×4, بين ×2, شهد ×4, قول ×4; 3:18 eşi; "
 "D4 1S 5 · 2MP 7 · 2MS 4 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[19] + "; aktör adlı 'l-qur'ânu' (14. kelime; ölçüm rol fail — edilgen 'ûhiye' naib-i faili); A2 en büyük şahitlik sorusu; Allah'ın şahitliği; Kur'an ile uyarma; başka ilahlara şahitlik etmeme; bir ilah; ortak koşulanlardan uzak olma; "
 "A3 'eyyu şey'in ekberu şehâde' (söz içi, 2-5. kelime); 'llâhu şehîdun beynî ve beynekum ve ûhiye ileyye hâze'l-qur'ânu li-unzirakum bihî ve men beleğ e'innekum le-teşhedûne enne ma'a'llâhi âliheten uxrâ' (söz içi, 7-25. kelime); "
 "'lâ eşhed' (söz içi, 27-28. kelime); 'innemâ huve ilâhun vâhidun ve innenî berî'un mimmâ tuşrikûn' (söz içi, 30-37. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (5. kelime, ayet içi); söz açılır (7. kelime); söz kapanır (25. kelime, ayet içi); söz açılır (27. kelime); söz kapanır (28. kelime, ayet içi); "
 "söz açılır (30. kelime); söz kapanır (37. kelime, ayet içi); şahıs geçişi 3 → 2 (ayetler arası); edim geçişi haber → soru (ayetler arası); bölüm kapanışı.",
)
out = ['# ── blok 6:16-19 (2026-11-19) ──', 'MEAL4 = {']
for n in range(16, 20):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M4 = {']
for n in range(16, 20):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL4); M.update(M4)']
open('/home/claude/yamalar/metin_6_16_19.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
