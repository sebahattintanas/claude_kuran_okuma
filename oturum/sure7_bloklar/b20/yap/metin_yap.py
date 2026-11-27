# sûre 7 blok 20 (7:70-72) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b20/say2.txt'
os.environ['OLC'] = '/home/claude/b20/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Nûh ve kavmi; Hûd ve Âd' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 70: "Dediler ki: Yalnız Allah'a kulluk edelim ve atalarımızın kulluk etmekte olduklarını bırakalım diye mi bize geldin? Doğru söyleyenlerdensen bize vaat ettiğin şeyi getir.",
 71: "Dedi ki: Rabbinizden size bir pislik ve bir öfke düştü. Allah'ın onlara hiçbir delil indirmediği sizin ve atalarınızın taktığınız adlar hakkında mı benimle tartışıyorsunuz? Öyleyse bekleyin; gerçekten ben sizinle birlikte bekleyenlerdenim.",
 72: "Onu ve onunla birlikte olanları katımızdan bir rahmetle kurtardık ve âyetlerimizi yalanlayanların kökünü kestik. Onlar iman edenler değildi.",
}

T = {}
T[70] = ("'qâlû' 3MP (adsız; gönderge 7:66 2. kelime, 1. kelime); muhatap 2MS (adsız; söz içi; 'ci'tenâ' — 2. kelime); konuşan 1P eki (adsız; söz içi; 'ci'tenâ' — 2. kelime); konuşan 1P (adsız; söz içi; 'na'bude', 'nezera' — 3. ve 6. kelime); "
         "'vahdehû' 3MS eki (adsız; söz içi; gönderge 'llâhe' 4. kelime, 5. kelime); 'kâne' 3MS (fiil uyumu; söz içi; 8. kelime — fail 10. kelime); 'ya'budu' 3MS (fiil uyumu; söz içi; 9. kelime — fail 10. kelime); "
         "konuşan 1P eki (adsız; söz içi; 'âbâ'unâ', 'fe'tinâ', 'te'idunâ' — 10., 11. ve 13. kelime); muhatap 2MS (adsız; söz içi; 'fe'tinâ', 'te'idunâ', 'kunte' — 11., 13. ve 15. kelime)")
T[71] = ("'qâle' 3MS (adsız; gönderge 7:65 4. kelime, 1. kelime); 'veqa'a' 3MS (fiil uyumu; söz içi; 3. kelime — fail 7. kelime); muhatap 2MP eki (adsız; söz içi; ''aleykum', 'rabbikum', 'âbâ'ukum', 'me'akum' — 4., 6., 14. ve 23. kelime); "
         "muhatap 2MP (adsız; söz içi; 'tucâdilûne', 'semmeytumûhâ', 'ntazirû' — 9., 12. ve 21. kelime); konuşan 1S eki (adsız; söz içi; 'tucâdilûnenî', 'innî' — 9. ve 22. kelime); "
         "'semmeytumûhâ', 'bihâ' 3FS eki (adsız; söz içi; gönderge 'esmâ'in' 11. kelime — 12. ve 18. kelime); muhatap 2MP zamiri (adsız; söz içi; 'entum' — 13. kelime); 'nezzele' 3MS (fiil uyumu; söz içi; 16. kelime — fail 17. kelime)")
T[72] = ("konuşan 1P (adsız; 'enceynâhu', 'qata'nâ' — 1. ve 6. kelime); 'enceynâhu', 'me'ahû' 3MS eki (adsız; gönderge 7:65 4. kelime — 1. ve 3. kelime); konuşan 1P eki (adsız; 'minnâ', 'bi-âyâtinâ' — 5. ve 10. kelime); "
         "'kezzebû' 3MP (adsız; gönderge 'llezîne' 8. kelime, 9. kelime); 'kânû' 3MP (adsız; gönderge 'llezîne' 8. kelime, 12. kelime)")

D = {}
D[70] = ("◇ 'qâlû e-ci'tenâ li-na'bude'llâhe vahdehû ve nezera mâ kâne ya'budu âbâ'unâ fe'tinâ bi-mâ te'idunâ in kunte mine's-sâdiqîn' — "
 "PERF 3MP I. bab + 'e' + PERF 2MS I. bab + 1P + 'li' + IMPF 1P I. bab + 'allâh' + 'vahd' + 3MS + 've' + IMPF 1P I. bab + 'mâ' + PERF 3MS I. bab + IMPF 3MS I. bab + çoğul 'âbâ'' + 1P + 'fe' + IMPV 2MS I. bab + 1P + 'bi' + 'mâ' + IMPF 2MS I. bab + 1P + 'in' + PERF 2MS I. bab + 'min' + belirli çoğul etken ortaç 'sâdiq' "
 "(ölçüm edim soru, emir, şart, kip COND 1 · IMPV 1 · INTG 1; 1P 6 · 2MS 6 · 3MP 2 · 3MS 3; bab I. bab ×9). "
 "Allah lafzı 4. sırada (ölçüm allah z=0,65); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=17 (n z=0,49); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:69 ن → 7:70 ن); "
 "ölçüm '{{1|sayı işareti وَحْد}}' — satır aynen; ölçüm '{{1|simetri \\[3, 7, 14, 1\\]}}' — satır aynen; ölçüm '{{1|harf 74 → harf3 71, isaret 3}}' — satır aynen; ölçüm '{{1|dış düğüm 4}}' — satır aynen; ölçüm '{{1|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 'in' (14. kelime); IMPV 1: 'fe'tinâ' (11. kelime); INTG 1: 'e-ci'tenâ' (2. kelime; 'e'); 've nezera' (6.) kelimesindeki 've' CONJ; 'fe'tinâ' (11.) kelimesindeki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) عبد ×2 ('na'bude' 3. / 'ya'budu' 9. kelime); كون ×2 ('kâne' 8. / 'kunte' 15. kelime) (okuma). "
 + T[70] + " (okuma). "
 + cumle(say('say 7:70 2-10', "e-ci'tenâ li-na'bude'llâhe vahdehû ve nezera mâ kâne ya'budu âbâ'unâ", True), say('dizi 7 70 8 10', "kâne 'abede âbâ'"), say('dizi 7 70 8 11', "kâne 'abede âbâ' etâ")) + ' '
 + cumle(say('say 7:70 11-13', "fe'tinâ bi-mâ te'idunâ"), say('say 7:70 14-17', "in kunte mine's-sâdiqîn"), say('say 7:70 11-17', "fe'tinâ bi-mâ te'idunâ in kunte mine's-sâdiqîn"), say('dizi 7 70 11 17', "etâ mâ ve'ade in kâne min sâdiq"), say('dizi 7 70 11 16', "etâ mâ ve'ade in kâne min"), say('dizi 7 70 14 17', "in kâne min sâdiq"), say('dizi 7 70 14 16', "in kâne min")) + ' ' +
 "Ölçüm xref 11:32 (emsal olarak basıldı), 14:10 (emsal olarak basıldı), 46:22 (emsal olarak basıldı), okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıbı: 'etâ mâ ve'ade in kâne min' süzgeç GEÇER; 'in kâne min sâdiq' süzgeç GEÇER; 'in kâne min' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + 'e' + PERF + 'li' + IMPF + lafız + izafet + 've' + IMPF + 'mâ' + PERF + IMPF + izafet + 'fe' + IMPV + 'bi' + 'mâ' + IMPF + 'in' + PERF + 'min' + belirli; "
 "D2 soru, emir, şart; COND ('in' 14. kelime), IMPV ('fe'tinâ' 11. kelime), INTG ('e-ci'tenâ' 2. kelime); D3 11:32 eşi, 14:10 eşi, 46:22 eşi, عبد ×2, كون ×2; D4 1P 6 · 2MS 6 · 3MP 2 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[70] + "; aktör yok (ölçüm); A2 yalnız Allah'a kulluk çağrısının ve atalardan kalan kulluğu bırakmanın sorgulanması; vaat edilenin getirilmesini istemesi; "
 "A3 'e-ci'tenâ li-na'bude'llâhe vahdehû ve nezera mâ kâne ya'budu âbâ'unâ fe'tinâ bi-mâ te'idunâ in kunte mine's-sâdiqîn' (söz içi, 2-17. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (17. kelime, ayet içi); şart → cevap (ayet içi; COND 'in' 14. kelime: 'in kunte mine's-sâdiqîn' / 'fe'tinâ' (11. kelime) — cevap öne alınmış); şahıs sayısında beraberlik (1P 6 · 2MS 6 — ölçüm baskın 2); şahıs geçişi yok (ayetler arası); edim geçişi soru, emir → soru, emir, şart (ayetler arası).",
)

D[71] = ("◇ 'qâle qad veqa'a 'aleykum min rabbikum ricsun ve ğadabun e-tucâdilûnenî fî esmâ'in semmeytumûhâ entum ve âbâ'ukum mâ nezzele'llâhu bihâ min sultânin fe'ntazirû innî me'akum mine'l-muntazirîn' — "
 "PERF 3MS I. bab + 'qad' + PERF 3MS I. bab + ''alâ' + 2MP + 'min' + 'rabb' + 2MP + nekre 'rics' + 've' + nekre 'ğadab' + 'e' + IMPF 2MP III. bab + 1S + 'fî' + nekre çoğul 'ism' + PERF 2MP II. bab + 3FS + 2MP + 've' + çoğul 'âbâ'' + 2MP + 'mâ' + PERF 3MS II. bab + 'allâh' + 'bi' + 3FS + 'min' + nekre 'sultân' + 'fe' + IMPV 2MP VIII. bab + 'inne' + 1S + 'ma'a' + 2MP + 'min' + belirli çoğul etken ortaç 'muntazir' "
 "(ölçüm edim soru, emir, kip CERT 1 · IMPV 1 · INTG 1 · NEG 1; 1S 2 · 2MP 11 · 3FS 2 · 3MS 3; bab I. bab ×2 · II. bab ×2 · III. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 17. sırada (ölçüm allah z=0,27); Rab 6. sırada (ölçüm rab z=0,53); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=25 (n z=1,34); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:70 ن → 7:71 ن); "
 "ölçüm '{{2|simetri \\[3, 2, 13, 1\\]}}' — satır aynen; ölçüm '{{2|harf 112 → harf3 106, isaret 6}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (2. kelime); IMPV 1: 'fe'ntazirû' (21. kelime); INTG 1: 'e-tucâdilûnenî' (9. kelime; 'e'); NEG 1: 'mâ' (15. kelime); 've ğadabun' (8.) kelimesindeki 've' CONJ; 've âbâ'ukum' (14.) kelimesindeki 've' CONJ; 'fe'ntazirû' (21.) kelimesindeki 'fe' REM (okuma). "
 "Kök ikilemesi (ölçüm) سمو ×2 ('esmâ'in' 11. / 'semmeytumûhâ' 12. kelime); نظر ×2 ('ntazirû' 21. / 'l-muntazirîn' 25. kelime) (okuma). "
 + T[71] + " (okuma). "
 + cumle(say('say 7:71 2-8', "qad veqa'a 'aleykum min rabbikum ricsun ve ğadabun", True)) + ' '
 + cumle(say('say 7:71 9-20', "e-tucâdilûnenî fî esmâ'in semmeytumûhâ entum ve âbâ'ukum mâ nezzele'llâhu bihâ min sultânin", True), say('say 7:71 11-14', "esmâ'in semmeytumûhâ entum ve âbâ'ukum"), say('dizi 7 71 11 14', "ism semmâ _ âbâ'"), say('dizi 7 71 11 20', "ism semmâ _ âbâ' mâ nezzele allâh _ min sultân")) + ' '
 + cumle(say('say 7:71 22-25', "innî me'akum mine'l-muntazirîn")) + ' ' +
 "Ölçüm xref 12:40 (emsal olarak basıldı), 53:23 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + 'qad' + PERF + ''alâ' + 'min' + izafet + nekre + 've' + nekre + 'e' + IMPF + 'fî' + nekre + PERF + zamir + 've' + izafet + 'mâ' + PERF + lafız + 'bi' + 'min' + nekre + 'fe' + IMPV + 'inne' + izafet + 'min' + belirli; "
 "D2 soru, emir; CERT ('qad' 2. kelime), IMPV ('fe'ntazirû' 21. kelime), INTG ('e-tucâdilûnenî' 9. kelime), NEG ('mâ' 15. kelime); D3 12:40 eşi, 53:23 eşi, سمو ×2, نظر ×2; D4 1S 2 · 2MP 11 · 3FS 2 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[71] + "; aktör yok (ölçüm); A2 Rabden pislik ve öfkenin düşüşü; Allah'ın delil indirmediği adlar hakkında tartışmanın sorulması; bekleme çağrısı; "
 "A3 'qad veqa'a 'aleykum min rabbikum ricsun ve ğadabun e-tucâdilûnenî fî esmâ'in semmeytumûhâ entum ve âbâ'ukum mâ nezzele'llâhu bihâ min sultânin fe'ntazirû innî me'akum mine'l-muntazirîn' (söz içi, 2-25. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (25. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi soru, emir, şart → soru, emir (ayetler arası).",
)

D[72] = ("◇ 'fe-enceynâhu ve'llezîne me'ahû bi-rahmetin minnâ ve qata'nâ dâbira'llezîne kezzebû bi-âyâtinâ ve mâ kânû mu'minîn' — "
 "'fe' + PERF 1P IV. bab + 3MS + 've' + 'ellezî' + 'ma'a' + 3MS + 'bi' + nekre 'rahme' + 'min' + 1P + 've' + PERF 1P I. bab + 'dâbir' + 'ellezî' + PERF 3MP II. bab + 'bi' + çoğul 'âye' + 1P + 've' + 'mâ' + PERF 3MP I. bab + çoğul etken ortaç 'mu'min' "
 "(ölçüm edim haber, kip NEG 1; 1P 6 · 3MP 4 · 3MS 2; bab I. bab ×2 · II. bab ×1 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; ölçüm '{{3|esmâ مُؤْمِن 13\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 've mâ kânû mu'minîn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (yalanlayanların sıfatı) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=13 (n z=0,06); ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:71 ن → 7:72 ن); "
 "ölçüm '{{3|harf 70 → harf3 65, isaret 5}}' — satır aynen; ölçüm '{{3|dış düğüm 1}}' — satır aynen; ölçüm '{{3|İÇ düğüm 3}}' — satır aynen. "
 "Ölçüm NEG 1: 've mâ' (11. kelime; 'mâ'); 'fe-enceynâhu' (1.) kelimesindeki 'fe' REM; 've'llezîne' (2.) kelimesindeki 've' CONJ; 'me'ahû' (3.) LOC; 've qata'nâ' (6.) kelimesindeki 've' CONJ; 've mâ' (11.) kelimesindeki 've' REM (okuma). "
 + T[72] + " (okuma). "
 + cumle(say('say 7:72 1-5', "fe-enceynâhu ve'llezîne me'ahû bi-rahmetin minnâ", True), say('say 7:72 1-3', "fe-enceynâhu ve'llezîne me'ahû"), say('dizi 7 72 1 3', "encâ ellezî ma'a")) + ' '
 + cumle(say('say 7:72 6-10', "ve qata'nâ dâbira'llezîne kezzebû bi-âyâtinâ", True), say('say 7:72 8-10', "llezîne kezzebû bi-âyâtinâ"), say('dizi 7 72 8 10', "ellezî kezzebe âye")) + ' '
 + cumle(say('say 7:72 11-13', "ve mâ kânû mu'minîn", True)) + ' ' +
 "Ölçüm xref 7:64 (basılmış), 21:77 (basılmış), okunmamış 2 ayet (sûre içi 2). "
 "Ölçüm nakarat3 kalıbı: 'ellezî kezzebe âye' süzgeç GEÇER; 'encâ ellezî ma'a' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'fe' + PERF + 've' + 'ellezî' + izafet + 'bi' + nekre + 'min' + 've' + PERF + izafet + 'ellezî' + PERF + 'bi' + izafet + 've' + 'mâ' + PERF + çoğul; "
 "D2 haber; NEG ('ve mâ' 11. kelime); D3 —; D4 1P 6 · 3MP 4 · 3MS 2, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[72] + "; aktör yok (ölçüm); A2 elçinin ve onunla birlikte olanların rahmetle kurtarılışı; âyetleri yalanlayanların kökünün kesilişi; iman eden olmayışları; "
 "A3 —; "
 "A4 " + BOLUM + "; bölüm kapanışı; şahıs sayısında beraberlik (1P 6 · 3. şahıs 6 — ölçüm baskın 1); şahıs geçişi 2 → 1 (ayetler arası); edim geçişi soru, emir → haber (ayetler arası).",
)
out = ['# ── blok 7:70-72 (2026-11-27) ──', 'MEAL20 = {']
for n in range(70, 73):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M20 = {']
for n in range(70, 73):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL20); M.update(M20)']
open('/home/claude/yamalar/metin_7_70_72.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
