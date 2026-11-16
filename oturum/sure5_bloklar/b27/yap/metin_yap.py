# blok 27 (5:87-89) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b27/say2.txt'
os.environ['OLC'] = '/home/claude/b27/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Helalleri haram kılmama; yemin keffareti; içki ve kumar' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 87: "Ey iman edenler! Allah'ın size helâl kıldığı temiz şeyleri haram kılmayın ve sınırı aşmayın. Şüphesiz Allah sınırı aşanları sevmez.",
 88: "Allah'ın size rızık olarak verdiği helâl ve temiz şeylerden yiyin. İnandığınız Allah'tan sakının.",
 89: "Allah sizi yeminlerinizdeki boş sözden dolayı sorumlu tutmaz; fakat yeminleri bağlamanızdan dolayı sizi sorumlu tutar. Bunun keffareti, ehlinize yedirdiğinizin ortalamasından on yoksulu doyurmak ya da onları giydirmek ya da bir köle azat etmektir. Kim bulamazsa, üç gün oruç tutmak gerekir. Bu, yemin ettiğinizde yeminlerinizin keffaretidir. Yeminlerinizi koruyun. Allah âyetlerini size böyle açıklar; umulur ki şükredersiniz.",
}

T87 = ("hitap 'yâ eyyuhe'llezîne âmenû' (1-3. kelime); 'âmenû' faili 3MP (adsız; 3. kelime); muhatap 2MP (adsız; 'tuharrimû', 'lekum', 'ta'tedû' — 5., 10. ve 12. kelime); "
       "'ehalle' 3MS (fiil uyumu; 8. kelime — fail 9. kelime); 'llâhu' ('ehalle' faili; lafız; 9. kelime); 'llâhe' ('inne' ismi; lafız; 14. kelime); 'yuhibbu' faili 3MS (adsız; gönderge lafız, 16. kelime); 'l-mu'tedîn' ('yuhibbu' mef'ûlü; 17. kelime)")
T88 = ("muhatap 2MP (adsız; 'kulû', 'razaqakumu', 'ttequ', 'entum' — 1., 3., 7. ve 10. kelime); 'razaqakumu' 3MS (fiil uyumu; 3. kelime — fail 4. kelime); 'llâhu' ('razaqa' faili; lafız; 4. kelime); "
       "'llâhe' ('ttequ' mef'ûlü; lafız; 8. kelime); 'bihî' 3MS (adsız; gönderge lafız, 11. kelime); 'mu'minûn' ('entum' haberi; çoğul insan göndergeli — esmâ göndergesi; 12. kelime)")
T89 = ("'yu'âxizukumu' 3MS (fiil uyumu; 2. kelime — fail 3. kelime); 'llâhu' ('yu'âxizu' faili; lafız; 3. kelime); muhatap 2MP (adsız; 'yu'âxizukumu', 'eymânikum', 'yu'âxizukum', ''aqqadtumu', 'tut'imûne', 'ehlîkum', 'eymânikum', 'haleftum', 'hfezû', 'eymânekum', 'lekum', 'le'allekum', 'teşkurûn' — 2., 6., 8., 10., 19., 20., 34., 36., 37., 38., 42., 44. ve 45. kelime); "
       "'yu'âxizukum' faili 3MS (adsız; gönderge lafız, 8. kelime); 'keffâratuhû' iyelik 3MS (adsız; 12. kelime); "
       "'ehlîkum' ('tut'imûne' mef'ûlü; 20. kelime); 'kisvetuhum' iyelik 3MP (adsız; gönderge 'mesâkîne', 22. kelime); "
       "'men' (şart ismi; 'yecid' faili; 26. kelime); 'yecid' 3MS (adsız; gönderge 'men', 28. kelime); "
       "'yubeyyinu' 3MS (fiil uyumu; 40. kelime — fail 41. kelime); 'llâhu' ('yubeyyinu' faili; lafız; 41. kelime); 'âyâtihî' iyelik 3MS (adsız; gönderge lafız, 43. kelime)")

D = {}
D[87] = ("◇ 'yâ eyyuhe'llezîne âmenû lâ tuharrimû tayyibâti mâ ehalle'llâhu lekum ve lâ ta'tedû inne'llâhe lâ yuhibbu'l-mu'tedîn' — "
 "'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF 3MP IV. bab + 'lâ' + IMPF 2MP II. bab + çoğul 'tayyibe' + 'mâ' + PERF 3MS IV. bab + lafız + 'li' + 2MP + 've' + 'lâ' + IMPF 2MP VIII. bab + 'inne' + lafız + 'lâ' + IMPF 3MS IV. bab + belirli çoğul etken ortaç 'mu'tedî' "
 "(ölçüm edim yasak, nida, kip NEG 1 · PRO 2 · VOC 1; 2MP 5 · 3MP 2 · 3MS 2; bab II. bab ×1 · IV. bab ×3 · VIII. bab ×1). "
 "Allah lafzı 9. ve 14. sırada (ölçüm allah z=1,82); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=17 (n z=0,49); ölçüm '{{1|fâsıla ٱلمعتدين → ن, N sınıfı}}' — satır aynen; "
 "ölçüm '{{1|simetri \\[3, 2, 11, 1\\]}}' — satır aynen; ölçüm '{{1|harf 72 → harf3 68, isaret 4}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen. "
 "Ölçüm VOC 1: 'yâ' (1. kelime); PRO 2: 'lâ' (4. ve 11. kelime); NEG 1: 'lâ' (15. kelime); 've lâ' (11.)'daki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhu' 9. / 'llâhe' 14. kelime), عدو ×2 ('ta'tedû' 12. / 'l-mu'tedîn' 17. kelime) (okuma). "
 + T87 + " (okuma). "
 + cumle(say('say 5:87 1-4', "yâ eyyuhe'llezîne âmenû lâ", True), say('dizi 5 87 1 4', "eyy ellezî âmene lâ"), say('say 5:87 1-3', "yâ eyyuhe'llezîne âmenû"), say('dizi 5 87 1 3', "eyy ellezî âmene")) + ' '
 + cumle(say('say 5:87 4-10', "lâ tuharrimû tayyibâti mâ ehalle'llâhu lekum", True), say('say 5:87 5-10', "tuharrimû tayyibâti mâ ehalle'llâhu lekum"), say('say 5:87 5-6', "tuharrimû tayyibât"), say('say 5:87 6-10', "tayyibâti mâ ehalle'llâhu lekum"), say('say 5:87 7-10', "mâ ehalle'llâhu lekum")) + ' '
 + cumle(say('say 5:87 11-17 --on', "ve lâ ta'tedû inne'llâhe lâ yuhibbu'l-mu'tedîn", True), say('say 5:87 11-12 --on', "ve lâ ta'tedû"), say('say 5:87 12-17', "ta'tedû inne'llâhe lâ yuhibbu'l-mu'tedîn"), say('say 5:87 13-17', "inne'llâhe lâ yuhibbu'l-mu'tedîn")) + ' '
 + cumle(say('say 5:87 13-15', "inne'llâhe lâ", True), say('dizi 5 87 13 15', "inne allâh lâ"), say('say 5:87 14-16', "llâhe lâ yuhibbu"), say('dizi 5 87 14 16', "allâh lâ ahbeb"), say('say 5:87 15-17', "lâ yuhibbu'l-mu'tedîn"), say('say 5:87 16-17', "yuhibbu'l-mu'tedîn")) + ' '
 "Ölçüm xref 2:190 (emsal olarak basıldı) ve okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'eyy ellezî âmene lâ', 'eyy ellezî âmene' ve 'inne allâh lâ' süzgeç GEÇER, 'allâh lâ ahbeb' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'tuharrimû' / 'ehalle' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'yâ' + 'ellezî' + PERF + 'lâ' + IMPF + çoğul + 'mâ' + PERF + lafız + 'li' + 've' + 'lâ' + IMPF + 'inne' + lafız + 'lâ' + IMPF + belirli; "
 "D2 yasak, nida, NEG ('lâ' 15. kelime), PRO ('lâ' 4. ve 11. kelime), VOC ('yâ' 1. kelime); D3 أله ×2, عدو ×2; 2:190 eşi; D4 2MP 5 · 3MP 2 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T87 + "; aktör yok (ölçüm); A2 helâli haram kılma yasağı; sınırı aşma yasağı; Allah'ın sınırı aşanları sevmemesi; A3 —; "
 "A4 " + BOLUM + "; bölüm açılışı; hitap açılır ('yâ eyyuhe'llezîne âmenû', 1-3. kelime); edim geçişi haber → yasak, nida (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası).",
)

D[88] = ("◇ 've kulû mimmâ razaqakumu'llâhu halâlen tayyiben ve'ttequ'llâhe'llezî entum bihî mu'minûn' — "
 "'ve' + IMPV 2MP I. bab + 'min' + 'mâ' + PERF 3MS I. bab + 2MP + lafız + nekre 'halâl' + nekre 'tayyib' + 've' + IMPV 2MP VIII. bab + lafız + 'ellezî' + 'entum' + 'bi' + 3MS + çoğul etken ortaç 'mu'min' "
 "(ölçüm edim emir, kip IMPV 2; 2MP 6 · 3MS 2; bab I. bab ×2 · VIII. bab ×1). "
 "Allah lafzı 4. ve 8. sırada (ölçüm allah z=2,80); Rab yok; ölçüm '{{2|esmâ مُؤْمِن 12\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton cemâl' (uyuşmuyor) — esma_el kaydı 'degil' — 'mu'minûn', kural 'çoğul insan göndergeli → degil' (inananlar) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=12 (n z=-0,04); ölçüm '{{2|fâsıla مؤمنون → ن, N sınıfı}}' — satır aynen; "
 "ölçüm '{{2|harf 57 → harf3 51, isaret 6}}' — satır aynen; ölçüm '{{2|dış düğüm 4}}' — satır aynen. "
 "Ölçüm IMPV 2: 'kulû' (1. kelime) ve 'ttequ' (7. kelime); 1. kelimedeki 've' REM, 've'ttequ' (7.)'daki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhu' 4. / 'llâhe' 8. kelime) (okuma). "
 + T88 + " (okuma). "
 + cumle(say('say 5:88 1-6 --on', "ve kulû mimmâ razaqakumu'llâhu halâlen tayyiben", True), say('say 5:88 1-4 --on', "ve kulû mimmâ razaqakumu'llâh"), say('say 5:88 2-6', "mimmâ razaqakumu'llâhu halâlen tayyiben"), say('say 5:88 2-4', "mimmâ razaqakumu'llâh"), say('say 5:88 3-4', "razaqakumu'llâh"), say('say 5:88 5-6', "halâlen tayyiben")) + ' '
 + cumle(say('say 5:88 7-12 --on', "ve'ttequ'llâhe'llezî entum bihî mu'minûn", True), say('say 5:88 7-8 --on', "ve'ttequ'llâh"), say('say 5:88 7-9 --on', "ve'ttequ'llâhe'llezî"), say('dizi 5 88 7 9', "ittaqâ allâh ellezî"), say('say 5:88 8-12', "llâhe'llezî entum bihî mu'minûn"), say('say 5:88 9-12', "llezî entum bihî mu'minûn"), say('say 5:88 10-12', "entum bihî mu'minûn"), say('say 5:88 11-12', "bihî mu'minûn")) + ' '
 "Ölçüm xref 16:114 ve 60:11 (emsal olarak basıldı) ve okunmamış 2 ayet. "
 "Ölçüm nakarat3 kalıbı: 'ittaqâ allâh ellezî' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: 5:87 / 5:88 ('lâ tuharrimû tayyibâti' / 'halâlen tayyiben').",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + IMPV + 'min' + 'mâ' + PERF + lafız + nekre + nekre + 've' + IMPV + lafız + 'ellezî' + 'entum' + 'bi' + ortaç; "
 "D2 emir, IMPV ('kulû' 1. ve 'ttequ' 7. kelime); D3 أله ×2; 16:114 ve 60:11 eşleri; D4 2MP 6 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T88 + "; aktör yok (ölçüm); A2 helâl ve temiz rızıktan yeme emri; Allah'tan sakınma emri; A3 —; "
 "A4 " + BOLUM + "; edim geçişi yasak, nida → emir (ayetler arası).",
)

D[89] = ("◇ 'lâ yu'âxizukumu'llâhu bi'l-lağvi fî eymânikum ve lâkin yu'âxizukum bi-mâ 'aqqadtumu'l-eymâne fe-keffâratuhû it'âmu 'aşerati mesâkîne min evsati mâ tut'imûne ehlîkum ev kisvetuhum ev tahrîru raqabetin fe-men lem yecid fe-siyâmu selâseti eyyâmin zâlike keffâratu eymânikum izâ haleftum ve'hfezû eymânekum kezâlike yubeyyinu'llâhu lekum âyâtihî le'allekum teşkurûn' — "
 "'lâ' + IMPF 3MS III. bab + 2MP + lafız + 'bi' + belirli 'lağv' + 'fî' + çoğul 'yemîn' + 2MP + 've' + 'lâkin' + IMPF 3MS III. bab + 2MP + 'bi' + 'mâ' + PERF 2MP II. bab + belirli çoğul 'yemîn' + 'fe' + 'keffâra' + 3MS + masdar 'it'âm' + ''aşere' + çoğul 'miskîn' + 'min' + ism-i tafdîl 'evsat' + 'mâ' + IMPF 2MP IV. bab + 'ehl' + 2MP + 'ev' + 'kisve' + 3MP + 'ev' + masdar 'tahrîr' + nekre 'raqabe' + "
 "'fe' + 'men' + 'lem' + IMPF 3MS I. bab + 'fe' + 'siyâm' + 'selâse' + çoğul nekre 'yevm' + 'zâlike' + 'keffâra' + çoğul 'yemîn' + 2MP + 'izâ' + PERF 2MP I. bab + 've' + IMPV 2MP I. bab + çoğul 'yemîn' + 2MP + 'ke' + 'zâlike' + IMPF 3MS II. bab + lafız + 'li' + 2MP + çoğul 'âye' + 3MS + 'le'alle' + 2MP + IMPF 2MP I. bab "
 "(ölçüm edim emir, şart, kip COND 1 · IMPV 1 · NEG 2; 2MP 18 · 3MP 1 · 3MS 6; bab I. bab ×4 · II. bab ×2 · III. bab ×2 · IV. bab ×1). "
 "Allah lafzı 3. ve 41. sırada (ölçüm allah z=0,36); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=45 (n z=3,46); ölçüm '{{3|fâsıla تشكرون → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|sayı işareti عَشَرَة, ثَلاثَة}}' — satır aynen (''aşerati' 14. ve 'selâseti' 30. kelime); "
 "ölçüm '{{3|simetri \\[3, 1, 7, 1\\]}}' — satır aynen; ölçüm '{{3|harf 207 → harf3 197, isaret 10}}' — satır aynen; ölçüm '{{3|dış düğüm 2}}' — satır aynen. "
 "Ölçüm COND 1: 'men' (26. kelime); NEG 2: 'lâ' (1. kelime) ve 'lem' (27. kelime); IMPV 1: 'hfezû' (37. kelime); 've lâkin' (7.), 'fe-keffâratuhû' (12.), 'fe-men' (26.) ve 've'hfezû' (37.)'daki önek REM, 'fe-siyâmu' (29.)'daki 'fe' RSLT, 'ev' (21. ve 23.) CONJ (okuma). "
 "Kök ikilemesi (ölçüm) أخذ ×2 ('yu'âxizukumu' 2. / 'yu'âxizukum' 8. kelime), أله ×2 ('llâhu' 3. / 41. kelime), طعم ×2 ('it'âmu' 13. / 'tut'imûne' 19. kelime), كفر ×2 ('keffâratuhû' 12. / 'keffâratu' 33. kelime), يمن ×4 ('eymânikum' 6. ve 34., 'l-eymâne' 11., 'eymânekum' 38. kelime) (okuma). "
 + T89 + " (okuma). "
 + cumle(say('say 5:89 1-6', "lâ yu'âxizukumu'llâhu bi'l-lağvi fî eymânikum", True), say('say 5:89 1-3', "lâ yu'âxizukumu'llâh"), say('say 5:89 4-6', "bi'l-lağvi fî eymânikum")) + ' '
 + cumle(say('say 5:89 7-11 --on', "ve lâkin yu'âxizukum bi-mâ 'aqqadtumu'l-eymân", True), say('say 5:89 8-11', "yu'âxizukum bi-mâ 'aqqadtumu'l-eymân"), say('say 5:89 9-11', "bi-mâ 'aqqadtumu'l-eymân")) + ' '
 + cumle(say('say 5:89 12-15 --on', "fe-keffâratuhû it'âmu 'aşerati mesâkîn", True), say('say 5:89 13-15', "it'âmu 'aşerati mesâkîn"), say('say 5:89 16-20', "min evsati mâ tut'imûne ehlîkum"), say('say 5:89 17-19', "evsati mâ tut'imûn"), say('say 5:89 21-25', "ev kisvetuhum ev tahrîru raqabetin"), say('say 5:89 24-25', "tahrîru raqabetin")) + ' '
 + cumle(say('say 5:89 26-31 --on', "fe-men lem yecid fe-siyâmu selâseti eyyâmin", True), say('say 5:89 27-31', "lem yecid fe-siyâmu selâseti eyyâmin"), say('say 5:89 29-31 --on', "fe-siyâmu selâseti eyyâmin"), say('say 5:89 30-31', "selâseti eyyâmin")) + ' '
 + cumle(say('say 5:89 32-34', "zâlike keffâratu eymânikum", True), say('say 5:89 33-34', "keffâratu eymânikum"), say('say 5:89 35-36', "izâ haleftum"), say('say 5:89 37-38 --on', "ve'hfezû eymânekum")) + ' '
 + cumle(say('say 5:89 39-45 --on', "kezâlike yubeyyinu'llâhu lekum âyâtihî le'allekum teşkurûn", True), say('say 5:89 39-41 --on', "kezâlike yubeyyinu'llâh"), say('say 5:89 40-43', "yubeyyinu'llâhu lekum âyâtih"), say('say 5:89 44-45', "le'allekum teşkurûn")) + ' '
 "Ölçüm xref 2:196 ve 2:225 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'lâ yu'âxizukumu'llâhu bi'l-lağvi' / 'yu'âxizukum bi-mâ 'aqqadtumu'l-eymâne' — ayetler arası: yok.",
 "◈K — K2 'eyyâmin' (31. kelime).",
 "◈B — —",
 "◈D — D1 'lâ' + IMPF + lafız + 'bi' + belirli + 'fî' + izafet + 've' + 'lâkin' + IMPF + 'bi' + 'mâ' + PERF + belirli + 'fe' + izafet + masdar + izafet + 'min' + izafet + 'mâ' + IMPF + izafet + 'ev' + izafet + 'ev' + masdar + nekre + 'fe' + 'men' + 'lem' + IMPF + 'fe' + izafet + nekre + 'zâlike' + izafet + 'izâ' + PERF + 've' + IMPV + izafet + 'ke' + 'zâlike' + IMPF + lafız + 'li' + izafet + 'le'alle' + IMPF; "
 "D2 emir, şart, COND ('men' 26. kelime), IMPV ('hfezû' 37. kelime), NEG ('lâ' 1. ve 'lem' 27. kelime); D3 أخذ ×2, أله ×2, طعم ×2, كفر ×2, يمن ×4; 2:225 ve 2:196 eşleri; D4 2MP 18 · 3MP 1 · 3MS 6, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T89 + "; aktör yok (ölçüm); A2 boş yeminden sorumlu tutmama; bağlanan yeminden sorumlu tutma; keffaret (doyurma, giydirme, azat); bulamayana üç gün oruç; yeminleri koruma emri; âyetleri açıklama; A3 —; "
 "A4 " + BOLUM + "; edim geçişi emir → emir, şart (ayetler arası); şart → cevap (ayet içi; COND 'men' 26. kelime: 'men lem yecid' / 'siyâmu selâseti eyyâmin' (29. kelime)).",
)

out = ['# ── blok 5:87-89 (2026-11-16) ──', 'MEAL27 = {']
for n in range(87, 90):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M27 = {']
for n in range(87, 90):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL27); M.update(M27)']
open('/home/claude/yamalar/metin_5_87_89.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
