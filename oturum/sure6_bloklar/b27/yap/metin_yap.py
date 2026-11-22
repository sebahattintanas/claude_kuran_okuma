# sûre 6 blok 27 (6:114-117) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b27/say2.txt'
os.environ['OLC'] = '/home/claude/b27/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Hakem olarak Allah; üzerine Allah'ın adı anılan' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 114: "Allah'tan başkasını mı hakem arayayım? Size Kitabı ayrıntılı olarak indiren O'dur. Kendilerine Kitap verdiklerimiz, onun Rabbinden hak ile indirildiğini bilirler. O hâlde sakın şüphe edenlerden olma.",
 115: "Rabbinin sözü doğruluk ve adaletçe tamamlandı; O'nun sözlerini değiştirecek yoktur. O, işitendir, bilendir.",
 116: "Yeryüzündekilerin çoğuna uyarsan seni Allah'ın yolundan saptırırlar. Onlar ancak zanna uyuyor ve ancak tahminde bulunuyorlar.",
 117: "Rabbin, yolundan sapanı en iyi bilendir; doğru yolu bulanları da en iyi bilendir.",
}

T = {}
T[114] = ("konuşan 1S (adsız; 'ebteğî' — 3. kelime); 've huve' 3MS (adsız; gönderge 'llâhi' 2. kelime, 5. kelime); 'enzele' 3MS (adsız; gönderge 'llezî' 6. kelime, 7. kelime); "
          "muhatap 2MP (adsız; 'ileykumu' — 8. kelime); konuşan 1P (adsız; 'âteynâhumu' — 12. kelime); 'âteynâhumu', 'ya'lemûne' 3MP (adsız; gönderge 've'llezîne' 11. kelime — 12. ve 14. kelime); "
          "'ennehû' 3MS eki (adsız; gönderge 'l-kitâbe' 9. kelime, 15. kelime); muhatap 2MS (adsız; 'rabbike', 'tekûnenne' — 18. ve 21. kelime)")
T[115] = ("'ve temmet' 3FS (fiil uyumu; 1. kelime — fail 2. kelime); muhatap 2MS (adsız; 'rabbike' — 3. kelime); 'li-kelimâtihî' 3MS eki (adsız; gönderge 'rabbike' 3. kelime, 8. kelime); "
          "'ve huve' 3MS (adsız; gönderge 'rabbike' 3. kelime, 9. kelime)")
T[116] = ("muhatap 2MS (adsız; 'tuti', 'yudillûke' — 2. ve 7. kelime); 'yudillûke' 3MP (adsız; gönderge 'men' 4. kelime, 7. kelime); 'yettebi'ûne' 3MP (adsız; gönderge 'men' 4. kelime, 12. kelime); "
          "'hum' 3MP (adsız; gönderge 'men' 4. kelime, 16. kelime); 'yaxrusûn' 3MP (adsız; gönderge 'men' 4. kelime, 18. kelime)")
T[117] = ("muhatap 2MS (adsız; 'rabbeke' — 2. kelime); 'huve' 3MS (adsız; gönderge 'rabbeke' 2. kelime, 3. kelime); 'yedillu' 3MS (adsız; gönderge 'men' 5. kelime, 6. kelime); "
          "'sebîlihî' 3MS eki (adsız; gönderge 'rabbeke' 2. kelime, 8. kelime); 've huve' 3MS (adsız; gönderge 'rabbeke' 2. kelime, 9. kelime)")

D = {}
D[114] = ("◇ 'e-fe-ğayra'llâhi ebteğî hakemen ve huve'llezî enzele ileykumu'l-kitâbe mufassalen ve'llezîne âteynâhumu'l-kitâbe ya'lemûne ennehû munezzelun min rabbike bi'l-haqqi fe-lâ tekûnenne mine'l-mumterîn' — "
 "'e' + 'fe' + 'ğayr' + lafız + IMPF 1S VIII. bab + nekre 'hakem' + 've' + 'huve' + 'ellezî' + PERF 3MS IV. bab + 'ilâ' + 2MP + belirli 'kitâb' + nekre edilgen ortaç 'mufassal' + "
 "'ve' + 'ellezîne' + PERF 1P IV. bab + 1P + 3MP + belirli 'kitâb' + IMPF 3MP I. bab + 3MP + 'enne' + 3MS + nekre edilgen ortaç 'munezzel' + 'min' + 'rabb' + 2MS + 'bi' + belirli 'haqq' + "
 "'fe' + 'lâ' + IMPF 2MS I. bab + 'nne' + 'min' + belirli çoğul etken ortaç 'mumterî' "
 "(ölçüm edim soru, kip EMPH 1 · INTG 1 · NEG 1; 1P 2 · 1S 1 · 2MP 1 · 2MS 2 · 3MP 3 · 3MS 3; bab I. bab ×2 · IV. bab ×2 · VIII. bab ×1). "
 "Allah lafzı 2. sırada (ölçüm allah z=0,34); Rab 18. sırada (ölçüm rab z=0,60); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=23 (n z=1,12); ölçüm '{{1|fâsıla ٱلممترين → ن, N sınıfı}}' — satır aynen (6:113 ن → 6:114 ن); "
 "ölçüm '{{1|simetri \\[3, 6, 15, 1\\]}}' — satır aynen; ölçüm '{{1|harf 109 → harf3 103, isaret 6}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen. "
 "Ölçüm INTG 1: 'e-fe-ğayra' (1. kelime; soru hemzesi); EMPH 1: 'tekûnenne' (21. kelime; 'nne'); NEG 1: 'lâ' (20. kelime); 'e-fe-ğayra' (1.) kelimesindeki 'fe' SUP; "
 "'ve huve' (5.) ve 've'llezîne' (11.) kelimelerindeki 've' REM; 'fe-lâ' (20.) kelimesindeki 'fe' REM (okuma). "
 "Kök ikilemesi (ölçüm) كتب ×2 ('l-kitâbe' 9. / 'l-kitâbe' 13. kelime), نزل ×2 ('enzele' 7. / 'munezzelun' 16. kelime) (okuma). "
 + T[114] + " (okuma). "
 + cumle(say('say 6:114 11-14', "ve'llezîne âteynâhumu'l-kitâbe ya'lemûne", True), say('dizi 6 114 11 14', "ellezî âtâ kitâb 'alime"), say('dizi 6 114 11 15', "ellezî âtâ kitâb 'alime enne")) + ' '
 + cumle(say('say 6:114 20-22', "fe-lâ tekûnenne mine", True), say('dizi 6 114 20 22', 'lâ kâne min')) + ' '
 + cumle(say('say 6:114 12-13', "âteynâhumu'l-kitâb", True)) + ' ' + cumle(say('say 6:114 17-18', 'min rabbik', True)) + ' ' + cumle(say('say 6:114 5-7', "ve huve'llezî enzel", True)) + ' ' +
 "Ölçüm xref okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'fe-lâ kâne min' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'e' + 'fe' + 'ğayr' + lafız + IMPF + nekre + 've' + 'huve' + 'ellezî' + PERF + 'ilâ' + belirli + nekre + 've' + 'ellezîne' + PERF + belirli + IMPF + 'enne' + nekre + 'min' + izafet + 'bi' + belirli + 'fe' + 'lâ' + IMPF + 'min' + belirli; "
 "D2 soru; EMPH ('tekûnenne' 21. kelime), INTG ('e-fe-ğayra' 1. kelime), NEG ('lâ' 20. kelime); D3 كتب ×2, نزل ×2; D4 1P 2 · 1S 1 · 2MP 1 · 2MS 2 · 3MP 3 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[114] + "; aktör yok (ölçüm); A2 Allah'tan başka hakem aranmayışı; Kitabın ayrıntılı indirilişi; Kitap verilenlerin onun hak ile indirildiğini bilmesi; şüphe edenlerden olmama uyarısı; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi haber → soru (ayetler arası); bölüm açılışı.",
)

D[115] = ("◇ 've temmet kelimetu rabbike sidqan ve 'adlen lâ mubeddile li-kelimâtihî ve huve's-semî'u'l-'alîm' — "
 "'ve' + PERF 3FS I. bab + 'kelime' + 'rabb' + 2MS + nekre 'sidq' + 've' + nekre ''adl' + 'lâ' + etken ortaç 'mubeddil' + 'li' + çoğul 'kelime' + 3MS + 've' + 'huve' + belirli 'semî'' + belirli ''alîm' "
 "(ölçüm edim haber, kip NEG 1; 2MS 1 · 3FS 1 · 3MS 2; bab I. bab ×1). "
 "Allah lafzı yok; Rab 3. sırada (ölçüm rab z=1,62); ölçüm '{{2|esmâ سَمِيع 10\\. sırada, SON konum, MÜHÜR \\| عَلِيم 11\\. sırada, SON konum, MÜHÜR}}' — satır aynen; esma_kayit çıktısı 'mühür EVET (ÇİFT) ton denge' — ölçüm MÜHÜR ile uyuşuyor (muhur_el EVET); "
 "esma_el kaydı 'ilahi' — 've huve's-semî'u'l-'alîm', kural 'zamirin haberi → ilahi' (Rab) ve 'l-'alîm' için kural 'zamirin haberi → ilahi' (Rab; işitenin sıfatı) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=11 (n z=-0,15); ölçüm '{{2|fâsıla ٱلعليم → م, N sınıfı}}' — satır aynen (6:114 ن → 6:115 م); "
 "ölçüm '{{2|harf 52 → harf3 47, isaret 5}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen. "
 "Ölçüm NEG 1: 'lâ' (6. kelime; cins nefyi); 've temmet' (1.) ve 've huve' (9.) kelimelerindeki 've' REM; 've 'adlen' (5.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) كلم ×2 ('kelimetu' 2. / 'li-kelimâtihî' 8. kelime) (okuma). "
 + T[115] + " (okuma). "
 + cumle(say('say 6:115 1-3', 've temmet kelimetu rabbik', True), say('dizi 6 115 1 3', 'temme kelime rabb')) + ' '
 + cumle(say('say 6:115 9-11', "ve huve's-semî'u'l-'alîm", True), say('dizi 6 115 9 11', "_ semî' 'alîm")) + ' '
 + cumle(say('say 6:115 6-8', 'lâ mubeddile li-kelimâtih', True)) + ' ' +
 "Ölçüm xref okunmuş 1 ayet ve okunmamış 1 ayet. "
 "Ölçüm nakarat3 kalıbı: '_ semî' 'alîm' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 's-semî'u' (10. kelime); B4 —.",
 "◈D — D1 've' + PERF + izafet + izafet + nekre + 've' + nekre + 'lâ' + 'mubeddil' + 'li' + izafet + 've' + 'huve' + belirli + belirli; "
 "D2 haber; NEG ('lâ' 6. kelime); D3 كلم ×2; D4 2MS 1 · 3FS 1 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[115] + "; aktör yok (ölçüm); A2 Rabbin sözünün doğruluk ve adaletçe tamamlanması; sözlerini değiştirecek olmayışı; işiten ve bilen oluşu; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi soru → haber (ayetler arası).",
)

D[116] = ("◇ 've in tuti eksera men fi'l-ardi yudillûke 'an sebîli'llâhi in yettebi'ûne illa'z-zanne ve in hum illâ yaxrusûn' — "
 "'ve' + 'in' + IMPF 2MS IV. bab + 'ekser' + 'men' + 'fî' + belirli 'ard' + IMPF 3MP IV. bab + 3MP + 2MS + ''an' + 'sebîl' + lafız + 'in' + IMPF 3MP VIII. bab + 3MP + 'illâ' + belirli mastar 'zann' + "
 "'ve' + 'in' + 'hum' + 'illâ' + IMPF 3MP I. bab + 3MP "
 "(ölçüm edim şart, kip COND 1 · NEG 2 · RES 1, biçim HASR + ISTISNA; 2MS 2 · 3MP 7; bab I. bab ×1 · IV. bab ×2 · VIII. bab ×1). "
 "Allah lafzı 10. sırada (ölçüm allah z=0,58); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=18 (n z=0,59); ölçüm '{{3|sayı işareti أَكْثَر}}' — satır aynen; ölçüm '{{3|fâsıla يخرصون → ن, N sınıfı}}' — satır aynen (6:115 م → 6:116 ن); "
 "ölçüm '{{3|simetri \\[3, 4, 15, 1\\]}}' — satır aynen; ölçüm '{{3|harf 64 → harf3 63, isaret 1}}' — satır aynen; ölçüm '{{3|dış düğüm 1}}' — satır aynen; ölçüm '{{3|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 'in' (1. kelime); NEG 2: 'in' (11.) ve 'in' (15. kelime); RES 1: 'illâ' (17. kelime); biçim HASR + ISTISNA ('illâ' 13. ve 17. kelime); "
 "'ve in' (1.) ve 've in' (15.) kelimelerindeki 've' CONJ; 'illâ' (13.) EXP (okuma). "
 + T[116] + " (okuma). "
 + cumle(say('say 6:116 11-18', "in yettebi'ûne illa'z-zanne ve in hum illâ yaxrusûn", True), say('dizi 6 116 11 18', 'in ittebe illâ zann in _ illâ yaxrusu')) + ' '
 + cumle(say('say 6:116 12-18', "yettebi'ûne illa'z-zanne ve in hum illâ yaxrusûn", True), say('dizi 6 116 12 18', 'ittebe illâ zann in _ illâ yaxrusu')) + ' '
 + cumle(say('say 6:116 11-15', "in yettebi'ûne illa'z-zanne ve in", True), say('dizi 6 116 11 15', 'in ittebe illâ zann in')) + ' '
 + cumle(say('say 6:116 11-13', "in yettebi'ûne illa", True), say('dizi 6 116 11 13', 'in ittebe illâ')) + ' '
 + cumle(say('say 6:116 4-6', "men fi'l-ard", True)) + ' ' + cumle(say('say 6:116 9-10', "sebîli'llâh", True)) + ' ' +
 "Ölçüm xref 10:66 (emsal olarak basıldı) ve okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıpları: 'in ittebe illâ zann in' süzgeç GEÇER, 'in ittebe illâ' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K1 'l-ardi' (6. kelime).",
 "◈B — —",
 "◈D — D1 've' + 'in' + IMPF + izafet + 'men' + 'fî' + belirli + IMPF + ''an' + izafet + lafız + 'in' + IMPF + 'illâ' + belirli + 've' + 'in' + 'hum' + 'illâ' + IMPF; "
 "D2 şart; COND ('in' 1. kelime), NEG ('in' 11. kelime, 'in' 15. kelime), RES ('illâ' 17. kelime); D3 10:66 eşi; D4 2MS 2 · 3MP 7, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[116] + "; aktör yok (ölçüm); A2 yeryüzündekilerin çoğuna uyulursa Allah'ın yolundan saptırmaları; onların ancak zanna uyması ve tahminde bulunması; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi haber → şart (ayetler arası); şart → cevap (ayet içi; COND 'in' 1. kelime: 've in tuti' / 'yudillûke' (7. kelime)).",
)

D[117] = ("◇ 'inne rabbeke huve a'lemu men yedillu 'an sebîlihî ve huve a'lemu bi'l-muhtedîn' — "
 "'inne' + 'rabb' + 2MS + 'huve' + 'a'lem' + 'men' + IMPF 3MS I. bab + ''an' + 'sebîl' + 3MS + 've' + 'huve' + 'a'lem' + 'bi' + belirli çoğul etken ortaç 'muhtedî' "
 "(ölçüm edim haber, kip yok; 2MS 1 · 3MS 4; bab I. bab ×1). "
 "Allah lafzı yok; Rab 2. sırada (ölçüm rab z=1,62); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=11 (n z=-0,15); ölçüm '{{4|fâsıla بٱلمهتدين → ن, N sınıfı}}' — satır aynen (6:116 ن → 6:117 ن); "
 "ölçüm '{{4|simetri \\[4, 1, 7, 1\\]}}' — satır aynen; ölçüm '{{4|harf 41 → harf3 39, isaret 2}}' — satır aynen; ölçüm '{{4|dış düğüm 2}}' — satır aynen; "
 "ölçüm '{{4|esit2 → 68:7 oran 0,9610 kademe YAKIN}}' — satır aynen (68:7 emsal olarak basıldı). "
 "Ölçüm kip yok; 'inne' (1.) ACC; 've huve' (9.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) علم ×2 ('a'lemu' 4. / 'a'lemu' 10. kelime) (okuma). "
 + T[117] + " (okuma). "
 + cumle(say('say 6:117 1-4', "inne rabbeke huve a'lemu", True), say('dizi 6 117 1 4', "inne rabb _ a'lem")) + ' '
 + cumle(say('dizi 6 117 1 11', "inne rabb _ a'lem men dalle 'an sebîl _ a'lem muhtedî", True)) + ' '
 + cumle(say('dizi 6 117 5 11', "men dalle 'an sebîl _ a'lem muhtedî", True)) + ' '
 + cumle(say('say 6:117 9-11', "ve huve a'lemu bi'l-muhtedîn", True)) + ' ' + cumle(say('say 6:117 7-8', "'an sebîlihî", True)) + ' ' +
 "Ölçüm xref 16:125 ve 68:7 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı: 'inne rabb _ a'lem' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'yedillu' / 'l-muhtedîn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'inne' + izafet + 'huve' + 'a'lem' + 'men' + IMPF + ''an' + izafet + 've' + 'huve' + 'a'lem' + 'bi' + belirli; "
 "D2 haber; D3 علم ×2; 16:125 ve 68:7 eşi; D4 2MS 1 · 3MS 4, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[117] + "; aktör yok (ölçüm); A2 Rabbin yolundan sapanı ve doğru yolu bulanları en iyi bilmesi; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi şart → haber (ayetler arası).",
)
out = ['# ── blok 6:114-117 (2026-11-22) ──', 'MEAL27 = {']
for n in range(114, 118):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M27 = {']
for n in range(114, 118):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL27); M.update(M27)']
open('/home/claude/yamalar/metin_6_114_117.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
