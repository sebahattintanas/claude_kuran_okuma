# sûre 6 blok 3 (6:12-15) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b03/say2.txt'
os.environ['OLC'] = '/home/claude/b03/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Mülk kimin; şahit olarak Allah' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 12: "De ki: Göklerde ve yerde olanlar kimindir? De ki: Allah'ındır. Rahmeti kendi üzerine yazmıştır. Sizi kıyamet gününe mutlaka toplayacaktır; onda şüphe yoktur. Kendilerini ziyana uğratanlar, onlar inanmazlar.",
 13: "Gecede ve gündüzde barınan şeyler O'nundur. O, işitendir, bilendir.",
 14: "De ki: Göklerin ve yerin yaratıcısı Allah'tan başkasını mı dost edinirim? O doyurur, doyurulmaz. De ki: Bana, teslim olanların öncüsü olmam emredildi. Sakın ortak koşanlardan olma.",
 15: "De ki: Rabbime isyan edersem büyük bir günün azabından korkarım.",
}

T = {}
T[12] = ("muhatap 2MS (adsız; 'qul', 'qul' — 1. ve 7. kelime); 'kataba', 'nefsihi' 3MS (adsız; gönderge lafız — 9. ve 11. kelime); "
         "'le-yecma'annekum' 3MS (adsız; gönderge lafız, 13. kelime); muhatap 2MP (adsız; 'le-yecma'annekum', 13. kelime); 'fîhi' 3MS (adsız; gönderge 'yevmi', 19. kelime); "
         "'xasirû', 'enfusehum', 'fe-hum', 'yu'minûn' 3MP (adsız; gönderge 'llezîne' — 21., 22., 23. ve 25. kelime)")
T[13] = ("'lehû' 3MS (adsız; gönderge 6:12 8. kelime, 1. kelime); 'sekene' 3MS (adsız; gönderge 'mâ', 3. kelime); 've huve' 3MS (adsız; gönderge 6:12 8. kelime, 7. kelime)")
T[14] = ("muhatap 2MS (adsız; 'qul', 'qul', 'tekûnenne' — 1., 13. ve 22. kelime); konuşan 1S (adsız; söz içi; 'ettexizu', 'innî', 'umirtu', 'ekûne' — 4., 14., 15. ve 17. kelime); "
         "'umirtu' 1S (fiil uyumu; edilgen; söz içi; naib-i faili konuşan zamir, 15. kelime); 've huve', 'yut'imu' 3MS (adsız; söz içi; gönderge lafız — 9. ve 10. kelime); "
         "'yut'amu' 3MS (fiil uyumu; edilgen; söz içi; naib-i faili zamir — gönderge lafız, 12. kelime); 'eslem' 3MS (adsız; söz içi; gönderge 'men', 20. kelime)")
T[15] = ("muhatap 2MS (adsız; 'qul', 1. kelime); konuşan 1S (adsız; söz içi; 'innî', 'exâfu', ''aseytu', 'rabbî' — 2., 3., 5. ve 6. kelime)")

D = {}
D[12] = ("◇ 'qul li-men mâ fi's-semâvâti ve'l-ardi qul li'llâhi kataba 'alâ nefsihi'r-rahmete le-yecma'annekum ilâ yevmi'l-qiyâmeti lâ raybe fîhi'llezîne xasirû enfusehum fe-hum lâ yu'minûn' — "
 "IMPV 2MS I. bab + 'li' + 'men' + 'mâ' + 'fî' + belirli çoğul 'semâ'' + 've' + belirli 'ard' + IMPV 2MS I. bab + 'li' + lafız + PERF 3MS I. bab + ''alâ' + 'nefs' + 3MS + belirli 'rahme' + "
 "'le' + IMPF 3MS I. bab + 'n' + 2MP + 'ilâ' + 'yevm' + belirli 'qiyâme' + 'lâ' + 'rayb' + 'fî' + 3MS + 'ellezî' + PERF 3MP I. bab + çoğul 'nefs' + 3MP + 'fe' + 3MP + 'lâ' + IMPF 3MP IV. bab "
 "(ölçüm edim soru, emir, kip EMPH 2 · IMPV 2 · INTG 1 · NEG 2; 2MP 1 · 2MS 2 · 3MP 6 · 3MS 4; bab I. bab ×5 · IV. bab ×1). "
 "Allah lafzı 8. sırada (ölçüm allah z=0,27); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=25 (n z=1,34); ölçüm '{{1|fâsıla يؤمنون → ن, N sınıfı}}' — satır aynen (6:11 ن → 6:12 ن); "
 "ölçüm '{{1|simetri \\[3, 2, 17, 1\\]}}' — satır aynen; ölçüm '{{1|harf 102 → harf3 97, isaret 5}}' — satır aynen; ölçüm '{{1|dış düğüm 3}}' — satır aynen. "
 "Ölçüm IMPV 2: 'qul' (1. ve 7. kelime); INTG 1: 'li-men' (2. kelime); EMPH 2: 'le-yecma'annekum' (13. kelime; 'le' ve 'n'); NEG 2: 'lâ' (17. ve 24. kelime); 've'l-ardi' (6.) kelimesindeki 've' CONJ; 'fe-hum' (23.) kelimesindeki 'fe' REM (okuma). "
 "Kök ikilemesi (ölçüm) قول ×2 ('qul' 1. / 'qul' 7. kelime), نفس ×2 ('nefsihi' 11. / 'enfusehum' 22. kelime) (okuma). "
 + T[12] + " (okuma). "
 + cumle(say('say 6:12 1-6', "qul li-men mâ fi's-semâvâti ve'l-ard", True), say('say 6:12 2-6', "li-men mâ fi's-semâvâti ve'l-ard"), say('say 6:12 7-8', "qul li'llâh")) + ' '
 + cumle(say('say 6:12 9-12 --on', "kataba 'alâ nefsihi'r-rahme", True), say('say 6:12 10-12', "'alâ nefsihi'r-rahme"), say('dizi 6 12 10 12', "'alâ nefs rahme"),
         say('say 6:12 13-19', "le-yecma'annekum ilâ yevmi'l-qiyâmeti lâ raybe fîh")) + ' '
 + cumle(say('say 6:12 20-25', "llezîne xasirû enfusehum fe-hum lâ yu'minûn", True), say('dizi 6 12 20 25', "ellezî xasira nefs _ lâ âmene"), say('say 6:12 20-22', "llezîne xasirû enfusehum")) + ' '
 "Ölçüm xref 4:87 (emsal olarak basıldı) ve okunmuş 2 ayet. "
 "Ölçüm nakarat3 kalıpları: 'ellezî xasira nefs _ lâ âmene' süzgeç GEÇER, ''alâ nefs rahme' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K1 's-semâvâti' (5. kelime), 'l-ardi' (6. kelime); K2 'yevmi' (15. kelime).",
 "◈B — —",
 "◈D — D1 IMPV + 'li' + 'men' + 'mâ' + 'fî' + belirli + 've' + belirli + IMPV + 'li' + lafız + PERF + ''alâ' + izafet + belirli + 'le' + IMPF + 'ilâ' + izafet + belirli + 'lâ' + 'rayb' + 'fî' + 'ellezî' + PERF + izafet + 'fe' + 'lâ' + IMPF; "
 "D2 soru, emir; IMPV ('qul' 1. ve 7. kelime), INTG ('li-men' 2. kelime), EMPH ('le-yecma'annekum' 13. kelime), NEG ('lâ' 17. ve 24. kelime); D3 قول ×2, نفس ×2; 4:87 eşi; D4 2MP 1 · 2MS 2 · 3MP 6 · 3MS 4, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[12] + "; aktör yok (ölçüm); A2 göklerde ve yerde olanların sahibi; rahmeti kendi üzerine yazma; kıyamet gününe toplama; ziyana uğrayanların inanmaması; "
 "A3 'li-men mâ fi's-semâvâti ve'l-ard' (söz içi, 2-6. kelime); 'li'llâh' (söz içi, 8. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (6. kelime, ayet içi); söz açılır (8. kelime); söz kapanır (8. kelime, ayet içi); şahıs geçişi 2 → 3 (ayetler arası); edim geçişi emir → soru (ayetler arası); bölüm açılışı.",
)

D[13] = ("◇ 've lehû mâ sekene fi'l-leyli ve'n-nehâri ve huve's-semî'u'l-'alîm' — "
 "'ve' + 'li' + 3MS + 'mâ' + PERF 3MS I. bab + 'fî' + belirli 'leyl' + 've' + belirli 'nehâr' + 've' + 'huve' + belirli 'semî'' + belirli ''alîm' "
 "(ölçüm edim haber, kip yok; 3MS 3; bab I. bab ×1). "
 "Lafız yok; Rab yok; ölçüm '{{2|esmâ سَمِيع 8\\. sırada, SON konum, MÜHÜR \\| عَلِيم 9\\. sırada, SON konum, MÜHÜR}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET (ÇİFT) ton denge' (uyuşuyor) — esma_el kaydı 'ilahi' — 've huve's-semî'u'l-'alîm', kural 'zamirin haberi → ilahi' (Allah) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=9 (n z=-0,36); ölçüm '{{2|fâsıla ٱلعليم → م, N sınıfı}}' — satır aynen (6:12 ن → 6:13 م); "
 "ölçüm '{{2|harf 39 → harf3 36, isaret 3}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; 've lehû' (1.) ve 've'n-nehâri' (6.) kelimelerindeki 've' CONJ; 've huve' (7.) kelimesindeki 've' REM (okuma). "
 + T[13] + " (okuma). "
 + cumle(say('say 6:13 1-6 --on', "ve lehû mâ sekene fi'l-leyli ve'n-nehâr", True), say('say 6:13 7-9 --on', "ve huve's-semî'u'l-'alîm"), say('dizi 6 13 7 9', "_ semî' 'alîm")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: '_ semî' 'alîm' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'l-leyli' / 'n-nehâri' — ayetler arası: yok.",
 "◈K — K1 'l-leyli' (5. kelime), 'n-nehâri' (6. kelime).",
 "◈B — B3 's-semî'u' (8. kelime).",
 "◈D — D1 've' + 'li' + 'mâ' + PERF + 'fî' + belirli + 've' + belirli + 've' + 'huve' + belirli + belirli; "
 "D2 haber; D3 —; D4 3MS 3, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[13] + "; aktör yok (ölçüm); A2 gecede ve gündüzde barınanların O'na ait oluşu; işiten ve bilen; "
 "A3 —; "
 "A4 " + BOLUM + "; edim geçişi soru → haber (ayetler arası).",
)

D[14] = ("◇ 'qul eğayra'llâhi ettexizu veliyyen fâtıri's-semâvâti ve'l-ardi ve huve yut'imu ve lâ yut'amu qul innî umirtu en ekûne evvele men eslema ve lâ tekûnenne mine'l-muşrikîn' — "
 "IMPV 2MS I. bab + 'e' + 'ğayr' + lafız + IMPF 1S VIII. bab + nekre 'veliyy' + etken ortaç 'fâtır' + belirli çoğul 'semâ'' + 've' + belirli 'ard' + 've' + 'huve' + IMPF 3MS IV. bab + 've' + 'lâ' + edilgen IMPF 3MS IV. bab + "
 "IMPV 2MS I. bab + 'inne' + 1S + edilgen PERF 1S I. bab + 'en' + IMPF 1S I. bab + 'evvel' + 'men' + PERF 3MS IV. bab + 've' + 'lâ' + IMPF 2MS I. bab + 'n' + 'min' + belirli çoğul etken ortaç 'muşrik' "
 "(ölçüm edim soru, emir, kip EMPH 1 · IMPV 2 · INTG 1 · NEG 2; 1S 5 · 2MS 3 · 3MS 4; bab I. bab ×5 · IV. bab ×3 · VIII. bab ×1). "
 "Allah lafzı 3. sırada (ölçüm allah z=0,31); Rab yok; ölçüm '{{3|esmâ وَلِيّ 5\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton denge' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kayıtları 'degil' — 'eğayra'llâhi ettexizu veliyyen' ve 'evvele men eslem', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=24 (n z=1,23); ölçüm '{{3|EDİLGEN 2/9 fiil, pas z=0,94}}' — satır aynen; ölçüm '{{3|fâsıla ٱلمشركين → ن, N sınıfı}}' — satır aynen (6:13 م → 6:14 ن); "
 "ölçüm '{{3|simetri \\[4, 14, 19, 1\\]}}' — satır aynen; ölçüm '{{3|harf 93 → harf3 90, isaret 3}}' — satır aynen; ölçüm '{{3|dış düğüm 3}}' — satır aynen; ölçüm '{{3|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 2: 'qul' (1. ve 13. kelime); INTG 1: 'eğayra' (2. kelime); NEG 2: 'lâ' (11. ve 21. kelime); EMPH 1: 'tekûnenne' (22. kelime); "
 "'ve'l-ardi' (8.) ve 've lâ yut'amu' (11.) kelimelerindeki 've' CONJ; 've huve' (9.) ve 've lâ tekûnenne' (21.) kelimelerindeki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) طعم ×2 ('yut'imu' 10. / 'yut'amu' 12. kelime), قول ×2 ('qul' 1. / 'qul' 13. kelime), كون ×2 ('ekûne' 17. / 'tekûnenne' 22. kelime) (okuma). "
 + T[14] + " (okuma). "
 + cumle(say('say 6:14 1-5', "qul eğayra'llâhi ettexizu veliyy", True), say('say 6:14 1-3', "qul eğayra'llâh"), say('dizi 6 14 1 3', "qâle ğayr allâh"), say('say 6:14 6-8', "fâtıri's-semâvâti ve'l-ard")) + ' '
 + cumle(say('say 6:14 9-12 --on', "ve huve yut'imu ve lâ yut'am", True), say('say 6:14 13-20', "qul innî umirtu en ekûne evvele men eslem"), say('say 6:14 14-20', "innî umirtu en ekûne evvele men eslem")) + ' '
 + cumle(say('say 6:14 21-24 --on', "ve lâ tekûnenne mine'l-muşrikîn", True), say('say 6:14 22-24', "tekûnenne mine'l-muşrikîn"), say('dizi 6 14 22 24', "kâne min muşrik")) + ' '
 "Ölçüm xref okunmuş 2 ayet ve okunmamış 2 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıpları: 'qâle ğayr allâh' süzgeç GEÇMEZ, 'kâne min muşrik' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'yut'imu' / 'yut'amu' — ayetler arası: yok.",
 "◈K — K1 's-semâvâti' (7. kelime), 'l-ardi' (8. kelime).",
 "◈B — —",
 "◈D — D1 IMPV + 'e' + izafet + lafız + IMPF + nekre + izafet + belirli + 've' + belirli + 've' + 'huve' + IMPF + 've' + 'lâ' + IMPF + IMPV + 'inne' + PERF + 'en' + IMPF + izafet + 'men' + PERF + 've' + 'lâ' + IMPF + 'min' + belirli; "
 "D2 soru, emir; IMPV ('qul' 1. ve 13. kelime), INTG ('eğayra' 2. kelime), NEG ('lâ' 11. ve 21. kelime), EMPH ('tekûnenne' 22. kelime); D3 طعم ×2, قول ×2, كون ×2; D4 1S 5 · 2MS 3 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[14] + "; aktör yok (ölçüm); A2 Allah'tan başkasını dost edinmeme; doyuran ve doyurulmayan; teslim olanların öncüsü olma emri; ortak koşmama; "
 "A3 'eğayra'llâhi ettexizu veliyyen fâtıri's-semâvâti ve'l-ardi ve huve yut'imu ve lâ yut'am' (söz içi, 2-12. kelime); 'innî umirtu en ekûne evvele men eslem' (söz içi, 14-20. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (12. kelime, ayet içi); söz açılır (14. kelime); söz kapanır (20. kelime, ayet içi); şahıs geçişi 3 → 1 (ayetler arası); edim geçişi haber → soru (ayetler arası).",
)

D[15] = ("◇ 'qul innî exâfu in 'aseytu rabbî 'azâbe yevmin 'azîm' — "
 "IMPV 2MS I. bab + 'inne' + 1S + IMPF 1S I. bab + 'in' + PERF 1S I. bab + 'rabb' + 1S + ''azâb' + nekre 'yevm' + nekre ''azîm' "
 "(ölçüm edim emir, şart, kip COND 1 · IMPV 1; 1S 5 · 2MS 1; bab I. bab ×3). "
 "Lafız yok; Rab 6. sırada (ölçüm rab z=2,05); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=9 (n z=-0,36); ölçüm '{{4|fâsıla عظيم → م, N sınıfı}}' — satır aynen (6:14 ن → 6:15 م); "
 "ölçüm '{{4|harf 30 → harf3 29, isaret 1}}' — satır aynen; ölçüm '{{4|dış düğüm 2}}' — satır aynen; "
 "ölçüm '{{4|esit2 → 39:13 oran 1,0000 kademe TAM · 39:13 oran 1,0000 kademe TAM}}' — satır aynen (39:13 emsal olarak basıldı). "
 "Ölçüm IMPV 1: 'qul' (1. kelime); COND 1: 'in' (4. kelime) (okuma). "
 + T[15] + " (okuma). "
 + cumle(say('say 6:15 1-9', "qul innî exâfu in 'aseytu rabbî 'azâbe yevmin 'azîm", True), say('say 6:15 2-9', "innî exâfu in 'aseytu rabbî 'azâbe yevmin 'azîm"), say('say 6:15 7-9', "'azâbe yevmin 'azîm")) + ' '
 "Ölçüm xref 39:13 (emsal olarak basıldı) ve okunmuş 1 ayet. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K2 'yevmin' (8. kelime).",
 "◈B — —",
 "◈D — D1 IMPV + 'inne' + IMPF + 'in' + PERF + izafet + izafet + nekre + nekre; "
 "D2 emir, şart; IMPV ('qul' 1. kelime), COND ('in' 4. kelime); D3 —; 39:13 eşi; D4 1S 5 · 2MS 1, sahset ['1', '2'], iltifât 0.",
 "◈A — A1 " + T[15] + "; aktör yok (ölçüm); A2 Rabbe isyan hâlinde büyük günün azabından korkma; "
 "A3 'innî exâfu in 'aseytu rabbî 'azâbe yevmin 'azîm' (söz içi, 2-9. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (9. kelime, ayet içi); edim geçişi soru → emir (ayetler arası); "
 "şart → cevap (ayet içi; COND 'in' 4. kelime: 'in 'aseytu rabbî' / 'innî exâfu' (3. kelime)).",
)

out = ['# ── blok 6:12-15 (2026-11-19) ──', 'MEAL3 = {']
for n in range(12, 16):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M3 = {']
for n in range(12, 16):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL3); M.update(M3)']
open('/home/claude/yamalar/metin_6_12_15.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
