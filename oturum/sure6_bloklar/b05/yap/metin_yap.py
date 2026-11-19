# sûre 6 blok 5 (6:20-24) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b05/say2.txt'
os.environ['OLC'] = '/home/claude/b05/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Yalanlayanların toplanma sahnesi; dünya hayatı oyun' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'



MEAL = {
 20: "Kendilerine kitap verdiklerimiz onu, oğullarını tanıdıkları gibi tanırlar. Kendilerini ziyana uğratanlar, onlar inanmazlar.",
 21: "Allah'a karşı yalan uydurandan yahut O'nun âyetlerini yalanlayandan daha zalim kim olabilir? Şüphesiz zalimler kurtuluşa ermez.",
 22: "Onları hep birlikte toplayacağımız gün, sonra ortak koşanlara diyeceğiz: İddia etmekte olduğunuz ortaklarınız nerede?",
 23: "Sonra fitneleri ancak şunu demeleri oldu: Rabbimiz Allah'a andolsun, biz ortak koşanlar olmadık.",
 24: "Bak, kendilerine karşı nasıl yalan söylediler; uydurdukları şeyler de kendilerinden kaybolmuştur.",
}

T = {}
T[20] = ("konuşan 1P (adsız; 'âteynâhumu' — 2. kelime); 'âteynâhumu' zamiri 3MP (adsız; gönderge 'ellezîne', 2. kelime); 'ya'rifûnehû' 3MP (adsız; gönderge 'ellezîne', 4. kelime); "
         "'ya'rifûnehû' zamiri 3MS (adsız; gönderge 'l-kitâbe', 4. kelime); 'ya'rifûne', 'ebnâ'ehum' 3MP (adsız; gönderge 'ellezîne' — 6. ve 7. kelime); "
         "'xasirû', 'enfusehum', 'fe-hum', 'yu'minûn' 3MP (adsız; gönderge 'ellezîne' — 9., 10., 11. ve 13. kelime)")
T[21] = ("'fterâ' 3MS (adsız; gönderge 'men', 4. kelime); 'kezzebe' 3MS (adsız; gönderge 'men', 9. kelime); 'bi-âyâtih' 3MS (adsız; gönderge lafız, 10. kelime); "
         "'innehû' 3MS (adsız; şan zamiri, 11. kelime); 'yuflihu' 3MS (fiil uyumu; 13. kelime — fail 14. kelime)")
T[22] = ("konuşan 1P (adsız; 'nahşuruhum', 'neqûlu' — 2. ve 5. kelime); 'nahşuruhum' zamiri 3MP (adsız; gönderge 6:21 14. kelime, 2. kelime); 'eşrakû' 3MP (adsız; gönderge 'li'llezîne', 7. kelime); "
         "muhatap 2MP (adsız; söz içi; 'şurakâ'ukumu', 'kuntum', 'tez'umûn' — 9., 11. ve 12. kelime)")
T[23] = ("'tekun' 3FS (fiil uyumu; 3. kelime — fail 4. kelime); 'fitnetuhum', 'qâlû' 3MP (adsız; gönderge 6:22 7. kelime — 4. ve 7. kelime); "
         "konuşan 1P (adsız; söz içi; 'rabbinâ', 'kunnâ' — 9. ve 11. kelime)")
T[24] = ("muhatap 2MS (adsız; 'unzur' — 1. kelime); 'kezebû', 'enfusihim' 3MP (adsız; gönderge 6:23 7. kelime — 3. ve 5. kelime); 'dalle' 3MS (adsız; gönderge 'mâ', 6. kelime); "
         "''anhum' 3MP (adsız; gönderge 6:23 7. kelime, 7. kelime); 'kânû', 'yefterûn' 3MP (adsız; gönderge 6:23 7. kelime — 9. ve 10. kelime)")

D = {}
D[20] = ("◇ 'ellezîne âteynâhumu'l-kitâbe ya'rifûnehû kemâ ya'rifûne ebnâ'ehum ellezîne xasirû enfusehum fe-hum lâ yu'minûn' — "
 "'ellezî' + PERF 1P IV. bab + 3MP + belirli 'kitâb' + IMPF 3MP I. bab + 3MS + 'ke' + 'mâ' + IMPF 3MP I. bab + 'ibn' + 3MP + 'ellezî' + PERF 3MP I. bab + 'nefs' + 3MP + 'fe' + 'hum' + 'lâ' + IMPF 3MP IV. bab "
 "(ölçüm edim haber, kip NEG 1; 1P 2 · 3MP 12 · 3MS 1; bab I. bab ×3 · IV. bab ×2). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=13 (n z=0,06); ölçüm '{{1|fâsıla يؤمنون → ن, N sınıfı}}' — satır aynen (6:19 ن → 6:20 ن); "
 "ölçüm '{{1|harf 70 → harf3 67, isaret 3}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen. "
 "Ölçüm NEG 1: 'lâ' (12. kelime); 'fe-hum' (11.) kelimesindeki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) عرف ×2 ('ya'rifûnehû' 4. / 'ya'rifûne' 6. kelime) (okuma). "
 + T[20] + " (okuma). "
 + cumle(say('say 6:20 1-3', "ellezîne âteynâhumu'l-kitâbe", True), say('say 6:20 4-7', "ya'rifûnehû kemâ ya'rifûne ebnâ'ehum")) + ' '
 + cumle(say('say 6:20 8-13', "ellezîne xasirû enfusehum fe-hum lâ yu'minûn", True), say('say 6:20 9-10', "xasirû enfusehum"), say('say 6:20 11-13', "fe-hum lâ yu'minûn")) + ' '
 "Ölçüm xref 2:146 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı: 'ellezî xasira nefs _ lâ âmene' süzgeç GEÇER; 'ellezî âtâ kitâb' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'ellezî' + PERF + belirli + IMPF + 'ke' + 'mâ' + IMPF + izafet + 'ellezî' + PERF + izafet + 'fe' + 'hum' + 'lâ' + IMPF; "
 "D2 haber; NEG ('lâ' 12. kelime); D3 عرف ×2; 2:146 eşi; 11:21 eşi; D4 1P 2 · 3MP 12 · 3MS 1, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[20] + "; aktör yok (ölçüm); A2 kitap verilenlerin onu oğullarını tanır gibi tanıması; kendilerini ziyana uğratanların inanmaması; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi soru → haber (ayetler arası); bölüm açılışı.",
)

D[21] = ("◇ 've men ezlemu mimmeni'fterâ 'alâ'llâhi keziben ev kezzebe bi-âyâtih, innehû lâ yuflihu'z-zâlimûn' — "
 "'ve' + 'men' + 'ezlem' + 'min' + 'men' + PERF 3MS VIII. bab + ''alâ' + lafız + nekre 'kezib' + 'ev' + PERF 3MS II. bab + 'bi' + çoğul 'âye' + 3MS + 'inne' + 3MS + 'lâ' + IMPF 3MS IV. bab + belirli etken ortaç 'zâlim' "
 "(ölçüm edim soru, kip INTG 1 · NEG 1; 3MS 5; bab II. bab ×1 · IV. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 6. sırada (ölçüm allah z=0,90); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=14 (n z=0,17); ölçüm '{{2|fâsıla ٱلظلمون → ن, N sınıfı}}' — satır aynen (6:20 ن → 6:21 ن); "
 "ölçüm '{{2|harf 56 → harf3 53, isaret 3}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen; ölçüm '{{2|esit2 → 10:17 oran 0,9346 kademe BENZER}}' — satır aynen. "
 "Ölçüm INTG 1: 'men' (1. kelime); NEG 1: 'lâ' (12. kelime); 've men' (1.) kelimesindeki 've' REM; 'innehû' (11.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) ظلم ×2 ('ezlemu' 2. / 'z-zâlimûn' 14. kelime), كذب ×2 ('keziben' 7. / 'kezzebe' 9. kelime) (okuma). "
 + T[21] + " (okuma). "
 + cumle(say('say 6:21 1-8', "ve men ezlemu mimmeni'fterâ 'alâ'llâhi keziben ev", True), say('say 6:21 8-10', "ev kezzebe bi-âyâtih"), say('say 6:21 9-10', "kezzebe bi-âyâtih")) + ' '
 + cumle(say('say 6:21 11-14', "innehû lâ yuflihu'z-zâlimûn", True), say('say 6:21 13-14', "yuflihu'z-zâlimûn")) + ' '
 "Ölçüm xref 10:17 (emsal olarak basıldı) ve okunmamış 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'men ezlem mimmen iftarâ 'alâ allâh kezib ev' süzgeç GEÇER; 'ezlem mimmen iftarâ 'alâ allâh kezib' süzgeç GEÇER; 'inne lâ eflaha zâlim' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'men' + 'ezlem' + 'min' + 'men' + PERF + ''alâ' + lafız + nekre + 'ev' + PERF + 'bi' + izafet + 'inne' + 'lâ' + IMPF + belirli; "
 "D2 soru; INTG ('men' 1. kelime), NEG ('lâ' 12. kelime); D3 ظلم ×2, كذب ×2; 10:17 eşi; D4 3MS 5, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[21] + "; aktör yok (ölçüm); A2 Allah'a karşı yalan uyduran ya da âyetlerini yalanlayandan daha zalimi; zalimlerin kurtuluşa ermemesi; "
 "A3 —; "
 "A4 " + BOLUM + "; edim geçişi haber → soru (ayetler arası).",
)

D[22] = ("◇ 've yevme nahşuruhum cemî'an summe neqûlu li'llezîne eşrakû eyne şurakâ'ukumu'llezîne kuntum tez'umûn' — "
 "'ve' + 'yevm' + IMPF 1P I. bab + 3MP + nekre 'cemî'' + 'summe' + IMPF 1P I. bab + 'li' + 'ellezî' + PERF 3MP IV. bab + 'eyn' + çoğul 'şerîk' + 2MP + 'ellezî' + PERF 2MP I. bab + IMPF 2MP I. bab "
 "(ölçüm edim soru, kip INTG 1; 1P 2 · 2MP 5 · 3MP 3; bab I. bab ×4 · IV. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=12 (n z=-0,04); ölçüm '{{3|fâsıla تزعمون → ن, N sınıfı}}' — satır aynen (6:21 ن → 6:22 ن); "
 "ölçüm '{{3|simetri \\[3, 4, 8, 1\\]}}' — satır aynen; ölçüm '{{3|harf 59 → harf3 57, isaret 2}}' — satır aynen; ölçüm '{{3|dış düğüm 3}}' — satır aynen; ölçüm '{{3|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm INTG 1: 'eyne' (8. kelime); 've yevme' (1.) kelimesindeki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) شرك ×2 ('eşrakû' 7. / 'şurakâ'ukumu' 9. kelime) (okuma). "
 + T[22] + " (okuma). "
 + cumle(say('say 6:22 1-3', "ve yevme nahşuruhum cemî'an", True), say('dizi 6 22 1 3', "yevm haşera cemî'"), say('say 6:22 4-7', "summe neqûlu li'llezîne eşrakû")) + ' '
 + cumle(say('say 6:22 8-9', "eyne şurakâ'ukum", True), say('say 6:22 10-12', "llezîne kuntum tez'umûn")) + ' '
 "Ölçüm xref 10:28 (emsal olarak basıldı) ve okunmuş 3 ayet ve okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıbı: 'yevm haşera cemî'' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K2 'yevme' (1. kelime).",
 "◈B — —",
 "◈D — D1 've' + 'yevm' + IMPF + nekre + 'summe' + IMPF + 'li' + 'ellezî' + PERF + 'eyn' + izafet + 'ellezî' + PERF + IMPF; "
 "D2 soru; INTG ('eyne' 8. kelime); D3 شرك ×2; 10:28 eşi; D4 1P 2 · 2MP 5 · 3MP 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[22] + "; aktör yok (ölçüm); A2 hep birlikte toplanma günü; ortak koşanlara iddia ettikleri ortakların sorulması; "
 "A3 'eyne şurakâ'ukumu'llezîne kuntum tez'umûn' (söz içi, 8-12. kelime); "
 "A4 " + BOLUM + "; söz açılır (8. kelime); söz kapanır (12. kelime, ayet içi); şahıs geçişi 3 → 2 (ayetler arası).",
)

D[23] = ("◇ 'summe lem tekun fitnetuhum illâ en qâlû ve'llâhi rabbinâ mâ kunnâ muşrikîn' — "
 "'summe' + 'lem' + IMPF 3FS I. bab + 'fitne' + 3MP + 'illâ' + 'en' + PERF 3MP I. bab + 've' + lafız + 'rabb' + 1P + 'mâ' + PERF 1P I. bab + çoğul etken ortaç 'muşrik' "
 "(ölçüm edim haber, kip NEG 2 · RES 1; 1P 3 · 3FS 1 · 3MP 3; bab I. bab ×3). "
 "Allah lafzı 8. sırada (ölçüm allah z=1,14); Rab 9. sırada (ölçüm rab z=1,45); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=12 (n z=-0,04); ölçüm '{{4|fâsıla مشركين → ن, N sınıfı}}' — satır aynen (6:22 ن → 6:23 ن); "
 "ölçüm '{{4|simetri \\[3, 1, 5, 1\\]}}' — satır aynen; ölçüm '{{4|harf 44 → harf3 43, isaret 1}}' — satır aynen; ölçüm '{{4|dış düğüm 2}}' — satır aynen. "
 "Ölçüm NEG 2: 'lem' (2. kelime), 'mâ' (10. kelime); RES 1: 'illâ' (5. kelime); 've'llâhi' (8.) kelimesindeki 've' yemin edatı (morph P) (okuma). "
 "Kök ikilemesi (ölçüm) كون ×2 ('tekun' 3. / 'kunnâ' 11. kelime) (okuma). "
 + T[23] + " (okuma). "
 + cumle(say('say 6:23 1-7', "summe lem tekun fitnetuhum illâ en qâlû", True), say('say 6:23 5-7', "illâ en qâlû"), say('say 6:23 8-9', "ve'llâhi rabbinâ")) + ' '
 + cumle(say('say 6:23 10-12', "mâ kunnâ muşrikîn", True), say('say 6:23 11-12', "kunnâ muşrikîn")) + ' '
 "Ölçüm xref okunmuş 2 ayet. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'summe' + 'lem' + IMPF + izafet + 'illâ' + 'en' + PERF + 've' + lafız + izafet + 'mâ' + PERF + çoğul; "
 "D2 haber; NEG ('lem' 2. kelime, 'mâ' 10. kelime), RES ('illâ' 5. kelime); D3 كون ×2; D4 1P 3 · 3FS 1 · 3MP 3, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[23] + "; aktör yok (ölçüm); A2 fitnelerinin ancak ortak koşmadıklarına yemin etmeleri; "
 "A3 've'llâhi rabbinâ mâ kunnâ muşrikîn' (söz içi, 8-12. kelime); "
 "A4 " + BOLUM + "; söz açılır (8. kelime); söz kapanır (12. kelime, ayet içi); şahıs geçişi 2 → 3 (ayetler arası); edim geçişi soru → haber (ayetler arası).",
)

D[24] = ("◇ 'unzur keyfe kezebû 'alâ enfusihim ve dalle 'anhum mâ kânû yefterûn' — "
 "IMPV 2MS I. bab + 'keyf' + PERF 3MP I. bab + ''alâ' + 'nefs' + 3MP + 've' + PERF 3MS I. bab + ''an' + 3MP + 'mâ' + PERF 3MP I. bab + IMPF 3MP VIII. bab "
 "(ölçüm edim emir, kip IMPV 1; 2MS 1 · 3MP 8 · 3MS 1; bab I. bab ×4 · VIII. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=10 (n z=-0,26); ölçüm '{{5|fâsıla يفترون → ن, N sınıfı}}' — satır aynen (6:23 ن → 6:24 ن); "
 "ölçüm '{{5|harf 44 → harf3 41, isaret 3}}' — satır aynen; ölçüm '{{5|dış düğüm 2}}' — satır aynen. "
 "Ölçüm IMPV 1: 'unzur' (1. kelime); 've dalle' (6.) kelimesindeki 've' CONJ (okuma). "
 + T[24] + " (okuma). "
 + cumle(say('say 6:24 1-3', "unzur keyfe kezebû", True), say('say 6:24 4-5', "'alâ enfusihim")) + ' '
 + cumle(say('say 6:24 6-10', "ve dalle 'anhum mâ kânû yefterûn", True), say('say 6:24 7-9', "'anhum mâ kânû"), say('say 6:24 8-10', "mâ kânû yefterûn"), say('dizi 6 24 6 10', "dalle 'an mâ kâne iftarâ")) + ' '
 "Ölçüm xref 11:21 (emsal olarak basıldı) ve okunmamış 1 ayet. "
 "Ölçüm nakarat3 kalıbı: ''an mâ kâne' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'keyf' + PERF + ''alâ' + izafet + 've' + PERF + ''an' + 'mâ' + PERF + IMPF; "
 "D2 emir; IMPV ('unzur' 1. kelime); D3 —; 11:21 eşi; D4 2MS 1 · 3MP 8 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[24] + "; aktör yok (ölçüm); A2 kendilerine karşı nasıl yalan söyledikleri; uydurdukları şeylerin kaybolması; "
 "A3 —; "
 "A4 " + BOLUM + "; edim geçişi haber → emir (ayetler arası).",
)
out = ['# ── blok 6:20-24 (2026-11-19) ──', 'MEAL5 = {']
for n in range(20, 25):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M5 = {']
for n in range(20, 25):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL5); M.update(M5)']
open('/home/claude/yamalar/metin_6_20_24.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
