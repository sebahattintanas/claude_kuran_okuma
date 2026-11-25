# sûre 7 blok 10 (7:35-37) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b10/say2.txt'
os.environ['OLC'] = '/home/claude/b10/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Elçiler gelince; yalanlayanların ateşte çekişmesi' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol mecrur\)', _OL[0]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 35: "Ey Âdemoğulları, size içinizden size âyetlerimi anlatan elçiler gelirse, kim sakınır ve düzeltirse, artık onlara korku yoktur ve onlar üzülmezler.",
 36: "Âyetlerimizi yalanlayıp onlara karşı büyüklenenler, işte onlar ateşin halkıdır; onlar orada ebedî kalanlardır.",
 37: "Allah'a karşı yalan uydurandan yahut O'nun âyetlerini yalanlayandan daha zalim kim olabilir? İşte onlara kitaptan payları erişir. Nihayet elçilerimiz onları vefat ettirmek üzere onlara geldiğinde dediler ki: Allah'tan başka dua etmekte olduklarınız nerede? Dediler ki: Bizden kaybolup gittiler. Ve kâfir olduklarına kendi aleyhlerine şahitlik ettiler.",
}

T = {}
T[35] = ("'ye'tiyennekum' 3MS (fiil uyumu; 4. kelime — fail 5. kelime); muhatap 2MP eki (adsız; 'ye'tiyennekum', 'minkum', ''aleykum' — 4., 6. ve 8. kelime); 'yaqussûne' 3MP (adsız; gönderge 'rusulun' 5. kelime, 7. kelime); konuşan 1S eki (adsız; 'âyâtî' — 9. kelime); "
         "'ttaqâ', 've asleha' 3MS (adsız; gönderge 'fe-meni' 10. kelime — 11. ve 12. kelime); ''aleyhim' 3MP eki (adsız; tartışmalı; sayı uyumsuz; gönderge 'fe-meni' 10. kelime, 15. kelime); 'hum' 3MP (adsız; tartışmalı; sayı uyumsuz; gönderge 'fe-meni' 10. kelime, 17. kelime); "
         "'yahzenûn' 3MP (adsız; tartışmalı; sayı uyumsuz; gönderge 'fe-meni' 10. kelime, 18. kelime)")
T[36] = ("'kezzebû', 've'stekberû' 3MP (adsız; gönderge 've'llezîne' 1. kelime — 2. ve 4. kelime); konuşan 1P eki (adsız; 'bi-âyâtinâ' — 3. kelime); ''anhâ' 3FS eki (adsız; gönderge 'bi-âyâtinâ' 3. kelime, 5. kelime); 'hum' 3MP (adsız; gönderge 've'llezîne' 1. kelime, 9. kelime); "
         "'fîhâ' 3FS eki (adsız; gönderge 'n-nâri' 8. kelime, 10. kelime)")
T[37] = ("'fterâ', 'kezzebe' 3MS (adsız; gönderge 'mimmeni' 3. kelime — 4. ve 9. kelime); 'bi-âyâtihî' 3MS eki (adsız; gönderge 'llâhi' 6. kelime, 10. kelime); 'yenâluhum' 3MS (fiil uyumu; 12. kelime — fail 13. kelime); "
         "'yenâluhum', 'nasîbuhum', 'câ'ethum', 'yeteveffevnehum' 3MP eki (adsız; gönderge 'ulâ'ike' 11. kelime — 12., 13., 18. ve 20. kelime); 'câ'ethum' 3FS (fiil uyumu; 18. kelime — fail 19. kelime); konuşan 1P eki (adsız; 'rusulunâ' — 19. kelime); "
         "'yeteveffevnehum', 'qâlû' 3MP (adsız; gönderge 'rusulunâ' 19. kelime — 20. ve 21. kelime); muhatap 2MP (adsız; söz içi; 'kuntum', 'ted'ûne' — 24. ve 25. kelime); 'qâlû' 3MP (adsız; gönderge 'ulâ'ike' 11. kelime, 29. kelime); "
         "'dallû' 3MP (adsız; söz içi; gönderge 'mâ' 23. kelime, 30. kelime); konuşan 1P eki (adsız; söz içi; ''annâ' — 31. kelime); 've şehidû', 'kânû' 3MP (adsız; gönderge 'ulâ'ike' 11. kelime — 32. ve 36. kelime); "
         "'enfusihim', 'ennehum' 3MP eki (adsız; gönderge 'ulâ'ike' 11. kelime — 34. ve 35. kelime)")

D = {}
D[35] = ("◇ 'yâ benî âdeme immâ ye'tiyennekum rusulun minkum yaqussûne 'aleykum âyâtî fe-meni'ttaqâ ve asleha fe-lâ xavfun 'aleyhim ve lâ hum yahzenûn' — "
 "'yâ' + çoğul 'bunayy' + özel ad 'âdem' + 'in' + 'mâ' + IMPF 3MS I. bab + 'n' + 2MP + nekre çoğul 'rasûl' + 'min' + 2MP + IMPF 3MP I. bab + ''alâ' + 2MP + çoğul 'âye' + 1S + 'fe' + 'men' + PERF 3MS VIII. bab + 've' + PERF 3MS IV. bab + 'fe' + 'lâ' + nekre 'xavf' + ''alâ' + 3MP + 've' + 'lâ' + 'hum' + IMPF 3MP I. bab "
 "(ölçüm edim nida, şart, kip COND 2 · EMPH 1 · NEG 2 · VOC 1; 1S 1 · 2MP 3 · 3MP 6 · 3MS 3; bab I. bab ×3 · IV. bab ×1 · VIII. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); ölçüm '{{1|" + _AK1 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=18 (n z=0,59); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:34 ن → 7:35 ن); "
 "ölçüm '{{1|simetri \\[3, 6, 13, 1\\]}}' — satır aynen; ölçüm '{{1|harf 76 → harf3 74, isaret 2}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen. "
 "Ölçüm COND 2: 'immâ' (3. kelime; 'in'), 'fe-meni' (10. kelime; 'men'); EMPH 1: 'ye'tiyennekum' (4. kelime; 'n'); NEG 2: 'lâ' (13. kelime), 'lâ' (16. kelime); VOC 1: 'yâ' (1. kelime); "
 "'immâ' (3.) COND + SUP; 'fe-meni' (10.) kelimesindeki 'fe' RSLT; 've asleha' (12.) kelimesindeki 've' CONJ; 'fe-lâ' (13.) kelimesindeki 'fe' RSLT; 've lâ' (16.) kelimesindeki 've' CONJ (okuma). "
 + T[35] + " (okuma). "
 + cumle(say('say 7:35 1-2', "yâ benî âdeme", True), say('dizi 7 35 1 2', "bunayy âdem")) + ' '
 + cumle(say('say 7:35 3-9', "immâ ye'tiyennekum rusulun minkum yaqussûne 'aleykum âyâtî", True), say('say 7:35 5-9', "rusulun minkum yaqussûne 'aleykum âyâtî"), say('dizi 7 35 5 9', "rasûl min qassa 'alâ âye")) + ' '
 + cumle(say('say 7:35 10-12', "fe-meni'ttaqâ ve asleha", True), say('say 7:35 13-15', "fe-lâ xavfun 'aleyhim"), say('say 7:35 16-18', "ve lâ hum yahzenûn"), say('say 7:35 12-18', "ve asleha fe-lâ xavfun 'aleyhim ve lâ hum yahzenûn")) + ' ' +
 "Ölçüm xref 6:48 (basılmış), 6:130 (basılmış). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'yâ' + izafet + özel ad + 'in' + 'mâ' + IMPF + 'n' + nekre + 'min' + IMPF + ''alâ' + izafet + 'fe' + 'men' + PERF + 've' + PERF + 'fe' + 'lâ' + nekre + ''alâ' + 've' + 'lâ' + 'hum' + IMPF; "
 "D2 nida, şart; COND ('immâ' 3. kelime, 'fe-meni' 10. kelime), EMPH ('ye'tiyennekum' 4. kelime), NEG ('lâ' 13. kelime, 'lâ' 16. kelime), VOC ('yâ' 1. kelime); D3 —; D4 1S 1 · 2MP 3 · 3MP 6 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[35] + "; aktör adlı 'âdeme' (2. kelime; ölçüm rol mecrur); A2 Âdemoğullarına içlerinden âyetleri anlatan elçilerin gelişi; sakınıp düzeltene korku ve üzüntü olmayışı; "
 "A3 —; "
 "A4 " + BOLUM + "; bölüm açılışı; nidâ ('yâ benî âdeme' 1. kelime); şart → cevap (ayet içi; COND 'in' 3. kelime: 'ye'tiyennekum rusulun' / 'fe-meni'ttaqâ' (10. kelime)); şart → cevap (ayet içi; COND 'men' 10. kelime: 'ttaqâ ve asleha' / 'fe-lâ xavfun' (13. kelime)); şahıs geçişi yok (ayetler arası); edim geçişi haber → nida, şart (ayetler arası).",
)

D[36] = ("◇ 've'llezîne kezzebû bi-âyâtinâ ve'stekberû 'anhâ ulâ'ike ashâbu'n-nâri hum fîhâ xâlidûn' — "
 "'ve' + 'ellezî' + PERF 3MP II. bab + 'bi' + çoğul 'âye' + 1P + 've' + PERF 3MP X. bab + ''an' + 3FS + 'ulâ'i' + 'ashâb' + belirli 'nâr' + 'hum' + 'fî' + 3FS + çoğul etken ortaç 'xâlid' "
 "(ölçüm edim haber, kip yok; 1P 1 · 3FS 2 · 3MP 5; bab II. bab ×1 · X. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=11 (n z=-0,15); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:35 ن → 7:36 ن); "
 "ölçüm '{{2|simetri \\[3, 5, 9, 1\\]}}' — satır aynen; ölçüm '{{2|harf 60 → harf3 56, isaret 4}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; "
 "'ve'llezîne' (1.) REM + REL; 've'stekberû' (4.) kelimesindeki 've' CONJ; 'ulâ'ike' (6.) DEM + ADDR (okuma). "
 + T[36] + " (okuma). "
 + cumle(say('say 7:36 1-5', "ve'llezîne kezzebû bi-âyâtinâ ve'stekberû 'anhâ", True), say('say 7:36 1-3', "ve'llezîne kezzebû bi-âyâtinâ"), say('dizi 7 36 1 3', "ellezî kezzebe âye")) + ' '
 + say('say 7:36 2-5', "kezzebû bi-âyâtinâ ve'stekberû 'anhâ", True) + " (--medde 2 ayet: 'bi-âyâtinâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı); " + cumle(say('dizi 7 36 2 5', "kezzebe âye istekbere 'an")) + ' '
 + cumle(say('say 7:36 6-8', "ulâ'ike ashâbu'n-nâri", True), say('say 7:36 9-11', "hum fîhâ xâlidûn"), say('dizi 7 36 9 11', "_ fî xâlid"), say('say 7:36 6-11', "ulâ'ike ashâbu'n-nâri hum fîhâ xâlidûn")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'kezzebe âye istekbere 'an' süzgeç GEÇER; 'ellezî kezzebe âye' süzgeç GEÇER; '_ fî xâlid' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'ellezî' + PERF + 'bi' + izafet + 've' + PERF + ''an' + 'ulâ'i' + izafet + belirli + 'hum' + 'fî' + 'xâlid'; "
 "D2 haber; kip yok; D3 —; D4 1P 1 · 3FS 2 · 3MP 5, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[36] + "; aktör yok (ölçüm); A2 âyetleri yalanlayıp onlara karşı büyüklenenlerin ateş halkı oluşu ve orada ebedî kalışı; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi nida, şart → haber (ayetler arası).",
)

D[37] = ("◇ 'fe-men azlemu mimmeni'fterâ 'ale'llâhi keziben ev kezzebe bi-âyâtihî ulâ'ike yenâluhum nasîbuhum mine'l-kitâbi hattâ izâ câ'ethum rusulunâ yeteveffevnehum qâlû eyne mâ kuntum ted'ûne min dûni'llâhi qâlû dallû 'annâ ve şehidû 'alâ enfusihim ennehum kânû kâfirîn' — "
 "'fe' + 'men' + 'azlem' + 'min' + 'men' + PERF 3MS VIII. bab + ''alâ' + 'allâh' + nekre 'kezib' + 'ev' + PERF 3MS II. bab + 'bi' + çoğul 'âye' + 3MS + 'ulâ'i' + IMPF 3MS I. bab + 3MP + 'nasîb' + 3MP + 'min' + belirli 'kitâb' + 'hattâ' + 'izâ' + PERF 3FS I. bab + 3MP + çoğul 'rasûl' + 1P + IMPF 3MP V. bab + 3MP + "
 "PERF 3MP I. bab + 'eyne' + 'mâ' + PERF 2MP I. bab + IMPF 2MP I. bab + 'min' + 'dûn' + 'allâh' + PERF 3MP I. bab + PERF 3MP I. bab + ''an' + 1P + 've' + PERF 3MP I. bab + ''alâ' + çoğul 'nefs' + 3MP + 'enne' + 3MP + PERF 3MP I. bab + çoğul etken ortaç 'kâfir' "
 "(ölçüm edim soru, kip INTG 2; 1P 2 · 2MP 4 · 3FS 1 · 3MP 18 · 3MS 4; bab I. bab ×9 · II. bab ×1 · V. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 6. ve 28. sırada (ölçüm allah z=0,55); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{3|yıldız ★★}}' — satır aynen (kaynak n, z=2,61); n=37 (n z=2,61); ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:36 ن → 7:37 ن); "
 "ölçüm '{{3|simetri \\[3, 1, 14, 1\\]}}' — satır aynen; ölçüm '{{3|harf 165 → harf3 155, isaret 10}}' — satır aynen; ölçüm '{{3|dış düğüm 7}}' — satır aynen. "
 "Ölçüm INTG 2: 'fe-men' (1. kelime; 'men'), 'eyne' (22. kelime); "
 "'fe-men' (1.) kelimesindeki 'fe' REM; 'mimmeni' (3.) P + REL; 'ev' (8.) CONJ; 'ulâ'ike' (11.) DEM + ADDR; 'hattâ' (16.) INC; 'izâ' (17.) T; 'mâ' (23.) REL; 've şehidû' (32.) kelimesindeki 've' CONJ; 'ennehum' (35.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhi' 6. / 'llâhi' 28. kelime); قول ×2 ('qâlû' 21. / 'qâlû' 29. kelime); كذب ×2 ('keziben' 7. / 'kezzebe' 9. kelime); كون ×2 ('kuntum' 24. / 'kânû' 36. kelime) (okuma). "
 + T[37] + " (okuma). "
 + cumle(say('say 7:37 1-10', "fe-men azlemu mimmeni'fterâ 'ale'llâhi keziben ev kezzebe bi-âyâtihî", True), say('say 7:37 2-10', "azlemu mimmeni'fterâ 'ale'llâhi keziben ev kezzebe bi-âyâtihî"), say('say 7:37 4-7', "fterâ 'ale'llâhi keziben"), say('dizi 7 37 4 7', "ifterâ 'alâ allâh kezib")) + ' '
 + cumle(say('say 7:37 11-15', "ulâ'ike yenâluhum nasîbuhum mine'l-kitâbi", True), say('say 7:37 16-20', "hattâ izâ câ'ethum rusulunâ yeteveffevnehum")) + ' '
 + cumle(say('say 7:37 22-28', "eyne mâ kuntum ted'ûne min dûni'llâhi", True), say('say 7:37 25-28', "ted'ûne min dûni'llâhi"), say('dizi 7 37 25 28', "de'â min dûn allâh"), say('say 7:37 26-28', "min dûni'llâhi"), say('dizi 7 37 26 28', "min dûn allâh"), say('say 7:37 25-27', "ted'ûne min dûni"), say('dizi 7 37 25 27', "de'â min dûn")) + ' '
 + cumle(say('say 7:37 30-31', "dallû 'annâ", True), say('dizi 7 37 26 31', "min dûn allâh qâle dalle 'an"), say('say 7:37 32-37', "ve şehidû 'alâ enfusihim ennehum kânû kâfirîn")) + ' ' +
 "Ölçüm xref 6:21 (basılmış), 6:130 (basılmış), 10:17 (basılmış), 40:74 (emsal olarak basıldı), okunmuş 3 ayet. "
 "Ölçüm nakarat3 kalıbı: 'ifterâ 'alâ allâh kezib' süzgeç GEÇER; 'de'â min dûn allâh' süzgeç GEÇER; 'min dûn allâh' süzgeç GEÇER; 'de'â min dûn' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'fe' + 'men' + 'azlem' + 'min' + 'men' + PERF + ''alâ' + lafız + nekre + 'ev' + PERF + 'bi' + izafet + 'ulâ'i' + IMPF + izafet + 'min' + belirli + 'hattâ' + 'izâ' + PERF + izafet + IMPF + PERF + 'eyne' + 'mâ' + PERF + IMPF + 'min' + 'dûn' + lafız + PERF + PERF + ''an' + 've' + PERF + ''alâ' + izafet + 'enne' + PERF + 'kâfir'; "
 "D2 soru; INTG ('fe-men' 1. kelime, 'eyne' 22. kelime); D3 40:74 eşi, أله ×2, قول ×2, كذب ×2, كون ×2; D4 1P 2 · 2MP 4 · 3FS 1 · 3MP 18 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[37] + "; aktör yok (ölçüm); A2 Allah'a karşı yalan uyduranın ya da âyetlerini yalanlayanın zalimliği; kitaptan paylarının erişmesi; vefat ettiren elçilerin sorusu, dua edilenlerin kayboluşu ve kâfirliğe kendi aleyhlerine şahitlik; "
 "A3 'eyne mâ kuntum ted'ûne min dûni'llâhi' (söz içi, 22-28. kelime); 'dallû 'annâ' (söz içi, 30-31. kelime); "
 "A4 " + BOLUM + "; söz açılır (22. kelime); söz kapanır (28. kelime, ayet içi); söz açılır (30. kelime); söz kapanır (31. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi haber → soru (ayetler arası).",
)
out = ['# ── blok 7:35-37 (2026-11-25) ──', 'MEAL10 = {']
for n in range(35, 38):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M10 = {']
for n in range(35, 38):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL10); M.update(M10)']
open('/home/claude/yamalar/metin_7_35_37.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
