# sûre 7 blok 18 (7:59-64) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b18/say2.txt'
os.environ['OLC'] = '/home/claude/b18/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Nûh ve kavmi; Hûd ve Âd' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 59: "Andolsun Nûh'u kavmine gönderdik. Dedi ki: Ey kavmim, Allah'a kulluk edin. Sizin O'ndan başka bir ilâhınız yok. Gerçekten ben sizin için büyük bir günün azabından korkuyorum.",
 60: "Kavminden ileri gelenler dedi ki: Gerçekten biz seni apaçık bir sapkınlık içinde görüyoruz.",
 61: "Dedi ki: Ey kavmim bende bir sapkınlık yok; fakat ben âlemlerin Rabbinden bir elçiyim.",
 62: "Size Rabbimin risaletlerini tebliğ ediyorum ve size öğüt veriyorum ve Allah'tan bilmediğiniz şeyleri biliyorum.",
 63: "Sizi uyarması ve sakınmanız için ve ola ki merhamet olunasınız diye Rabbinizden içinizden bir adam aracılığıyla size bir zikir gelmesine mi şaştınız?",
 64: "Onu yalanladılar; onu ve gemide onunla birlikte olanları kurtardık ve âyetlerimizi yalanlayanları boğduk. Gerçekten onlar kör bir kavim idiler.",
}

T = {}
T[59] = ("konuşan 1P (adsız; 'erselnâ' — 2. kelime); 'qavmihî' 3MS eki (adsız; gönderge 'nûhan' 3. kelime, 5. kelime); 'fe-qâle' 3MS (adsız; gönderge 'nûhan' 3. kelime, 6. kelime); konuşan 1S eki (adsız; söz içi; 'qavmi' — 7. kelime); "
         "muhatap 2MP (adsız; söz içi; 'u'budu' — 8. kelime); muhatap 2MP eki (adsız; söz içi; 'lekum', ''aleykum' — 11. ve 17. kelime); 'ğayruhû' 3MS eki (adsız; söz içi; gönderge 'llâhe' 9. kelime, 14. kelime); "
         "konuşan 1S eki (adsız; söz içi; 'innî' — 15. kelime); konuşan 1S (adsız; söz içi; 'exâfu' — 16. kelime)")
T[60] = ("'qâle' 3MS (fiil uyumu; 1. kelime — fail 2. kelime); 'qavmihî' 3MS eki (adsız; gönderge 7:59 3. kelime, 4. kelime); konuşan 1P eki (adsız; söz içi; 'innâ' — 5. kelime); konuşan 1P (adsız; söz içi; 'nerâke' — 6. kelime); "
         "muhatap 2MS eki (adsız; söz içi; 'nerâke' — 6. kelime)")
T[61] = ("'qâle' 3MS (adsız; gönderge 7:59 3. kelime, 1. kelime); konuşan 1S eki (adsız; söz içi; 'qavmi' — 2. kelime); 'leyse' 3MS (fiil uyumu; söz içi; 3. kelime — fail 5. kelime); konuşan 1S eki (adsız; söz içi; 'bî', 'lâkinnî' — 4. ve 6. kelime)")
T[62] = ("konuşan 1S (adsız; söz içi; 'ubelliğukum', 'ensahu', 'a'lemu' — 1., 4. ve 6. kelime); muhatap 2MP eki (adsız; söz içi; 'ubelliğukum', 'lekum' — 1. ve 5. kelime); konuşan 1S eki (adsız; söz içi; 'rabbî' — 3. kelime); "
         "muhatap 2MP (adsız; söz içi; 'ta'lemûn' — 11. kelime)")
T[63] = ("muhatap 2MP (adsız; söz içi; ''acibtum', 'tetteqû' — 1. ve 11. kelime); muhatap 2MP (adsız; söz içi; edilgen, naib-i faili zamir; 'turhamûn' — 13. kelime); 'câ'ekum' 3MS (fiil uyumu; söz içi; 3. kelime — fail 4. kelime); muhatap 2MP eki (adsız; söz içi; 'câ'ekum', 'rabbikum', 'minkum', 'yunzirakum', 'le'allekum' — 3., 6., 9., 10. ve 12. kelime); "
         "'yunzirakum' 3MS (adsız; söz içi; gönderge 'raculin' 8. kelime, 10. kelime)")
T[64] = ("'kezzebûhu' 3MP (adsız; gönderge 7:59 5. kelime, 1. kelime); 'kezzebûhu', 'enceynâhu', 'me'ahû' 3MS eki (adsız; gönderge 7:59 3. kelime — 1., 2. ve 4. kelime); konuşan 1P (adsız; 'enceynâhu', 'ağraqna' — 2. ve 7. kelime); "
         "'kezzebû' 3MP (adsız; gönderge 'llezîne' 8. kelime, 9. kelime); konuşan 1P eki (adsız; 'bi-âyâtinâ' — 10. kelime); 'innehum' 3MP eki (adsız; gönderge 'llezîne' 8. kelime, 11. kelime); 'kânû' 3MP (adsız; gönderge 'llezîne' 8. kelime, 12. kelime)")

D = {}
D[59] = ("◇ 'le-qad erselnâ nûhan ilâ qavmihî fe-qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû innî exâfu 'aleykum 'azâbe yevmin 'azîm' — "
 "'le' + 'qad' + PERF 1P IV. bab + özel ad 'nûh' + 'ilâ' + 'qavm' + 3MS + 'fe' + PERF 3MS I. bab + 'yâ' + 'qavm' + 1S + IMPV 2MP I. bab + 'allâh' + 'mâ' + 'li' + 2MP + 'min' + nekre 'ilâh' + 'ğayr' + 3MS + 'inne' + 1S + IMPF 1S I. bab + ''alâ' + 2MP + ''azâb' + nekre 'yevm' + nekre ''azîm' "
 "(ölçüm edim emir, nida, kip CERT 1 · EMPH 1 · IMPV 1 · NEG 1 · VOC 1; 1P 2 · 1S 3 · 2MP 4 · 3MS 3; bab I. bab ×3 · IV. bab ×1). "
 "Allah lafzı 9. sırada (ölçüm allah z=0,47); Rab yok; esmâ yok (ölçüm); ölçüm '{{1|" + _AK + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=20 (n z=0,81); ölçüm '{{1|fâsıla " + _F[0] + " → م, N sınıfı}}' — satır aynen (7:58 ن → 7:59 م); "
 "ölçüm '{{1|simetri \\[3, 1, 10, 1\\]}}' — satır aynen; ölçüm '{{1|harf 79 → harf3 75, isaret 4}}' — satır aynen; ölçüm '{{1|dış düğüm 6}}' — satır aynen; ölçüm '{{1|İÇ düğüm 3}}' — satır aynen. "
 "Ölçüm CERT 1: 'le-qad' (1. kelime; 'qad'); EMPH 1: 'le-qad' (1. kelime; 'le'); IMPV 1: 'u'budu' (8. kelime); NEG 1: 'mâ' (10. kelime); VOC 1: 'yâ' (7. kelime); "
 "'fe-qâle' (6.) kelimesindeki 'fe' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhe' 9. / 'ilâhin' 13. kelime); قوم ×2 ('qavmihî' 5. / 'qavmi' 7. kelime) (okuma). "
 + T[59] + " (okuma). "
 + cumle(say('say 7:59 2-5', "erselnâ nûhan ilâ qavmihî", True), say('dizi 7 59 1 14', "qad ersele nûh ilâ qavm qâle qavm 'abede allâh mâ _ min ilâh ğayr")) + ' '
 + cumle(say('say 7:59 8-9', "u'budu'llâhe", True), say('say 7:59 10-14', "mâ lekum min ilâhin ğayruhû"), say('say 7:59 7-14', "yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû"), say('dizi 7 59 7 14', "qavm 'abede allâh mâ _ min ilâh ğayr"), say('say 7:59 8-14', "u'budu'llâhe mâ lekum min ilâhin ğayruhû"), say('dizi 7 59 8 14', "'abede allâh mâ _ min ilâh ğayr"), say('dizi 7 59 6 14', "qâle qavm 'abede allâh mâ _ min ilâh ğayr")) + ' '
 + cumle(say('say 7:59 15-20', "innî exâfu 'aleykum 'azâbe yevmin 'azîm", True)) + ' ' +
 "Ölçüm xref 11:50 (emsal olarak basıldı), 11:61 (emsal olarak basıldı), 11:84 (emsal olarak basıldı), 23:23 (emsal olarak basıldı), 23:32 (emsal olarak basıldı), okunmuş 1 ayet ve okunmamış 3 ayet (sûre içi 3). "
 "Ölçüm nakarat3 kalıbı: 'qâle qavm 'abede allâh mâ _ min ilâh ğayr' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K2 'yevmin' (19. kelime).",
 "◈B — —",
 "◈D — D1 'le' + 'qad' + PERF + özel ad + 'ilâ' + izafet + 'fe' + PERF + 'yâ' + izafet + IMPV + lafız + 'mâ' + 'li' + 'min' + nekre + izafet + 'inne' + IMPF + ''alâ' + izafet + nekre + nekre; "
 "D2 emir, nida; CERT ('le-qad' 1. kelime), EMPH ('le-qad' 1. kelime), IMPV ('u'budu' 8. kelime), NEG ('mâ' 10. kelime), VOC ('yâ' 7. kelime); D3 11:50 eşi, 11:61 eşi, 11:84 eşi, 23:23 eşi, 23:32 eşi, أله ×2, قوم ×2; D4 1P 2 · 1S 3 · 2MP 4 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[59] + "; aktör adlı 'nûhan' (3. kelime; ölçüm rol meful); A2 Nûh'un kavmine gönderilişi; Allah'a kulluk çağrısı; O'ndan başka ilâh olmayışı; büyük günün azabından korkulması; "
 "A3 'yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû innî exâfu 'aleykum 'azâbe yevmin 'azîm' (söz içi, 7-20. kelime); "
 "A4 " + BOLUM + "; bölüm açılışı; söz açılır (7. kelime); söz kapanır (20. kelime, ayet içi); şahıs sayısında toplam farkı (1. şahıs 5 · 2MP 4 — ölçüm baskın 2); şahıs geçişi 3 → 2 (ayetler arası); edim geçişi haber → emir, nida (ayetler arası).",
)

D[60] = ("◇ 'qâle'l-mele'u min qavmihî innâ le-nerâke fî dalâlin mubîn' — "
 "PERF 3MS I. bab + belirli 'mele'' + 'min' + 'qavm' + 3MS + 'inne' + 1P + 'le' + IMPF 1P I. bab + 2MS + 'fî' + nekre 'dalâl' + nekre etken ortaç 'mubîn' "
 "(ölçüm edim haber, kip EMPH 1; 1P 2 · 2MS 1 · 3MS 2; bab I. bab ×2). "
 "Allah lafzı yok; Rab yok; ölçüm '{{2|esmâ مُبِين 9. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' (uyuşmuyor) — esma_el kaydı 'degil' — 'fî dalâlin mubîn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (sapkınlığın sıfatı) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=9 (n z=-0,36); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:59 م → 7:60 ن); "
 "ölçüm '{{2|harf 34 → harf3 31, isaret 3}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen; ölçüm '{{2|İÇ düğüm 2}}' — satır aynen. "
 "Ölçüm EMPH 1: 'le-nerâke' (6. kelime; 'le') (okuma). "
 + T[60] + " (okuma). "
 + cumle(say('say 7:60 2-4', "l-mele'u min qavmihî"), say('dizi 7 60 1 4', "qâle mele' min qavm")) + ' '
 + cumle(say('say 7:60 5-9', "innâ le-nerâke fî dalâlin mubîn", True), say('dizi 7 60 5 9', "inne ra'â fî dalâl mubîn"), say('say 7:60 7-9', "fî dalâlin mubîn"), say('say 7:60 3-7', "min qavmihî innâ le-nerâke fî"), say('dizi 7 60 3 7', "min qavm inne ra'â fî")) + ' ' +
 "Ölçüm xref 12:30 (emsal olarak basıldı), 23:33 (emsal olarak basıldı), okunmamış 2 ayet (sûre içi 2). "
 "Ölçüm nakarat3 kalıbı: 'min qavm inne ra'â fî' süzgeç GEÇER; 'qâle mele' min qavm' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + belirli + 'min' + izafet + 'inne' + 'le' + IMPF + 'fî' + nekre + nekre; "
 "D2 haber; EMPH ('le-nerâke' 6. kelime); D3 12:30 eşi, 23:33 eşi; D4 1P 2 · 2MS 1 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[60] + "; aktör yok (ölçüm); A2 kavmin ileri gelenlerinin Nûh'u apaçık sapıklıkta görmesi; "
 "A3 'innâ le-nerâke fî dalâlin mubîn' (söz içi, 5-9. kelime); "
 "A4 " + BOLUM + "; söz açılır (5. kelime); söz kapanır (9. kelime, ayet içi); şahıs sayısında beraberlik (1P 2 · 3. şahıs 2 — ölçüm baskın 3); şahıs geçişi 2 → 3 (ayetler arası); edim geçişi emir, nida → haber (ayetler arası).",
)

D[61] = ("◇ 'qâle yâ qavmi leyse bî dalâletun ve lâkinnî rasûlun min rabbi'l-'âlemîn' — "
 "PERF 3MS I. bab + 'yâ' + 'qavm' + 1S + PERF 3MS I. bab + 'bi' + 1S + nekre 'dalâle' + 've' + 'lâkinne' + 1S + nekre 'rasûl' + 'min' + 'rabb' + belirli çoğul ''âlem' "
 "(ölçüm edim nida, kip VOC 1; 1S 3 · 3MS 2; bab I. bab ×2). "
 "Allah lafzı yok; Rab 9. sırada (ölçüm rab z=1,81); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{3|yıldız ★}}' — satır aynen (kaynak rab, z=1,81); n=10 (n z=-0,26); ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:60 ن → 7:61 ن); "
 "ölçüm '{{3|harf 38 → harf3 36, isaret 2}}' — satır aynen; ölçüm '{{3|dış düğüm 3}}' — satır aynen; ölçüm '{{3|İÇ düğüm 2}}' — satır aynen. "
 "Ölçüm esit2 okunmamış 1 ayet (sûre içi 1), ölçüm 'kademe BENZER' — satır aynen. "
 "Ölçüm VOC 1: 'yâ' (2. kelime); 've lâkinnî' (6.) kelimesindeki 've' REM (okuma). "
 + T[61] + " (okuma). "
 + cumle(say('say 7:61 1-4', "qâle yâ qavmi leyse bî"), say('dizi 7 61 1 4', "qâle qavm leyse _"), say('say 7:61 2-5', "yâ qavmi leyse bî dalâletun", True)) + ' '
 + cumle(say('say 7:61 6-10', "ve lâkinnî rasûlun min rabbi'l-'âlemîn"), say('dizi 7 61 6 10', "lâkinne rasûl min rabb 'âlem"), say('say 7:61 7-10', "rasûlun min rabbi'l-'âlemîn"), say('dizi 7 61 7 10', "rasûl min rabb 'âlem"), say('say 7:61 9-10', "rabbi'l-'âlemîn"), say('dizi 7 61 9 10', "rabb 'âlem")) + ' ' +
 "Ölçüm xref 26:16 (emsal olarak basıldı), 43:46 (emsal olarak basıldı), okunmuş 1 ayet ve okunmamış 2 ayet (sûre içi 2). "
 "Ölçüm nakarat3 kalıbı: 'lâkinne rasûl min rabb 'âlem' süzgeç GEÇER; 'rasûl min rabb 'âlem' süzgeç GEÇER; 'qâle qavm leyse _' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + 'yâ' + izafet + PERF + 'bi' + nekre + 've' + 'lâkinne' + nekre + 'min' + izafet + belirli; "
 "D2 nida; VOC ('yâ' 2. kelime); D3 26:16 eşi, 43:46 eşi; D4 1S 3 · 3MS 2, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[61] + "; aktör yok (ölçüm); A2 Nûh'un kendisinde sapıklık olmadığını bildirmesi; âlemlerin Rabbinden elçi oluşu; "
 "A3 'yâ qavmi leyse bî dalâletun ve lâkinnî rasûlun min rabbi'l-'âlemîn' (söz içi, 2-10. kelime; ayet sonunda kapanmıyor); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); şahıs geçişi 3 → 1 (ayetler arası); edim geçişi haber → nida (ayetler arası).",
)

D[62] = ("◇ 'ubelliğukum risâlâti rabbî ve ensahu lekum ve a'lemu mine'llâhi mâ lâ ta'lemûn' — "
 "IMPF 1S II. bab + 2MP + çoğul 'risâle' + 'rabb' + 1S + 've' + IMPF 1S I. bab + 'li' + 2MP + 've' + IMPF 1S I. bab + 'min' + 'allâh' + 'mâ' + 'lâ' + IMPF 2MP I. bab "
 "(ölçüm edim haber, kip NEG 1; 1S 4 · 2MP 4; bab I. bab ×3 · II. bab ×1). "
 "Allah lafzı 8. sırada (ölçüm allah z=1,29); Rab 3. sırada (ölçüm rab z=1,62); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{4|yıldız ★}}' — satır aynen (kaynak rab, z=1,62); n=11 (n z=-0,15); ölçüm '{{4|fâsıla " + _F[3] + " → ن, N sınıfı}}' — satır aynen (7:61 ن → 7:62 ن); "
 "ölçüm '{{4|harf 42 → harf3 42, isaret 0}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 1: 'lâ' (10. kelime); 've ensahu' (4.) kelimesindeki 've' CONJ; 've a'lemu' (6.) kelimesindeki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) علم ×2 ('a'lemu' 6. / 'ta'lemûn' 11. kelime) (okuma). "
 + T[62] + " (okuma). "
 + cumle(say('say 7:62 1-3', "ubelliğukum risâlâti rabbî", True), say('dizi 7 62 1 3', "belliğ risâle rabb"), say('say 7:62 2-5', "risâlâti rabbî ve ensahu lekum"), say('dizi 7 62 2 5', "risâle rabb nesahu _")) + ' '
 + cumle(say('say 7:62 4-5', "ve ensahu lekum", True), say('say 7:62 6-11', "ve a'lemu mine'llâhi mâ lâ ta'lemûn", True), say('say 7:62 8-11', "llâhi mâ lâ ta'lemûn"), say('dizi 7 62 8 11', "allâh mâ lâ 'alime")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'allâh mâ lâ 'alime' süzgeç GEÇER; 'risâle rabb nesahu _' süzgeç GEÇER; 'belliğ risâle rabb' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPF + izafet + izafet + 've' + IMPF + 'li' + 've' + IMPF + 'min' + lafız + 'mâ' + 'lâ' + IMPF; "
 "D2 haber; NEG ('lâ' 10. kelime); D3 علم ×2; D4 1S 4 · 2MP 4, sahset ['1', '2'], iltifât 0.",
 "◈A — A1 " + T[62] + "; aktör yok (ölçüm); A2 Rabbin risaletlerinin tebliği; öğüt verme; Allah'tan bilinmeyeni bilme; "
 "A3 söz sürüyor (7:61 2. kelimeden, 1-11. kelime; ayet sonunda kapanmıyor); "
 "A4 " + BOLUM + "; şahıs sayısında beraberlik (1S 4 · 2MP 4 — ölçüm baskın 1); şahıs geçişi yok (ayetler arası); edim geçişi nida → haber (ayetler arası).",
)

D[63] = ("◇ 'e-ve-'acibtum en câ'ekum zikrun min rabbikum 'alâ raculin minkum li-yunzirakum ve li-tetteqû ve le'allekum turhamûn' — "
 "'e' + 've' + PERF 2MP I. bab + 'en' + PERF 3MS I. bab + 2MP + nekre mastar 'zikr' + 'min' + 'rabb' + 2MP + ''alâ' + nekre 'racul' + 'min' + 2MP + 'li' + IMPF 3MS IV. bab + 2MP + 've' + 'li' + IMPF 2MP VIII. bab + 've' + 'le'alle' + 2MP + IMPF 2MP I. bab edilgen "
 "(ölçüm edim soru, kip INTG 1; 2MP 11 · 3MS 2; bab I. bab ×3 · IV. bab ×1 · VIII. bab ×1). "
 "Allah lafzı yok; Rab 6. sırada (ölçüm rab z=1,32); esmâ yok (ölçüm); ölçüm '{{5|aktör: adsız `racül` 8. sırada}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=13 (n z=0,06); ölçüm '{{5|fâsıla " + _F[4] + " → ن, N sınıfı}}' — satır aynen (7:62 ن → 7:63 ن); "
 "ölçüm '{{5|EDİLGEN 1/5 fiil, pas z=0,81}}' — satır aynen; ölçüm '{{5|harf 62 → harf3 59, isaret 3}}' — satır aynen; ölçüm '{{5|dış düğüm 0}}' — satır aynen. "
 "Ölçüm INTG 1: 'e' (1. kelime); 've li-tetteqû' (11.) kelimesindeki 've' CONJ; 've le'allekum' (12.) kelimesindeki 've' REM (okuma). "
 + T[63] + " (okuma). "
 + cumle(say('say 7:63 1-9', "e-ve-'acibtum en câ'ekum zikrun min rabbikum 'alâ raculin minkum", True), say('say 7:63 1-10', "e-ve-'acibtum en câ'ekum zikrun min rabbikum 'alâ raculin minkum li-yunzirakum"), say('dizi 7 63 1 10', "'acibu en câ'e zikr min rabb 'alâ racul min enzere")) + ' '
 + cumle(say('say 7:63 10-11', "li-yunzirakum ve li-tetteqû", True), say('say 7:63 12-13', "ve le'allekum turhamûn", True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: ''acibu en câ'e zikr min rabb 'alâ racul min enzere' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'e' + 've' + PERF + 'en' + PERF + nekre + 'min' + izafet + ''alâ' + nekre + 'min' + 'li' + IMPF + 've' + 'li' + IMPF + 've' + 'le'alle' + IMPF; "
 "D2 soru; INTG ('e' 1. kelime); D3 —; D4 2MP 11 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[63] + "; aktör adsız 'raculin' (8. kelime; ölçüm racül); A2 içlerinden bir adam aracılığıyla gelen zikre şaşmanın sorulması; uyarma, sakınma ve merhamet amacı; "
 "A3 söz sürüyor (7:61 2. kelimeden, 1-13. kelime); "
 "A4 " + BOLUM + "; söz kapanır (13. kelime); şahıs geçişi 1 → 2 (ayetler arası); edim geçişi haber → soru (ayetler arası).",
)

D[64] = ("◇ 'fe-kezzebûhu fe-enceynâhu ve'llezîne me'ahû fi'l-fulki ve ağraqna'llezîne kezzebû bi-âyâtinâ innehum kânû qavmen 'amîn' — "
 "'fe' + PERF 3MP II. bab + 3MS + 'fe' + PERF 1P IV. bab + 3MS + 've' + 'ellezî' + 'ma'a' + 3MS + 'fî' + belirli 'fulk' + 've' + PERF 1P IV. bab + 'ellezî' + PERF 3MP II. bab + 'bi' + çoğul 'âye' + 1P + 'inne' + 3MP + PERF 3MP I. bab + nekre 'qavm' + çoğul ''amî' "
 "(ölçüm edim haber, kip yok; 1P 5 · 3MP 7 · 3MS 3; bab I. bab ×1 · II. bab ×2 · IV. bab ×2). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=14 (n z=0,17); ölçüm '{{6|fâsıla " + _F[5] + " → ن, N sınıfı}}' — satır aynen (7:63 ن → 7:64 ن); "
 "ölçüm '{{6|simetri \\[3, 1, 9, 1\\]}}' — satır aynen; ölçüm '{{6|harf 74 → harf3 70, isaret 4}}' — satır aynen; ölçüm '{{6|dış düğüm 2}}' — satır aynen; ölçüm '{{6|İÇ düğüm 3}}' — satır aynen. "
 "Ölçüm kip yok; 'fe-kezzebûhu' (1.) kelimesindeki 'fe' REM; 'fe-enceynâhu' (2.) kelimesindeki 'fe' REM; 've'llezîne' (3.) kelimesindeki 've' CONJ; 'me'ahû' (4.) LOC; 've ağraqna' (7.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) كذب ×2 ('fe-kezzebûhu' 1. / 'kezzebû' 9. kelime) (okuma). "
 + T[64] + " (okuma). "
 + cumle(say('say 7:64 2-6', "fe-enceynâhu ve'llezîne me'ahû fi'l-fulki", True), say('dizi 7 64 2 4', "encâ ellezî ma'a"), say('say 7:64 4-6', "me'ahû fi'l-fulki")) + ' '
 + cumle(say('say 7:64 7-10', "ve ağraqna'llezîne kezzebû bi-âyâtinâ", True) + " (--medde 2 ayet: 'bi-âyâtinâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı)", say('dizi 7 64 7 10', "uğriqu ellezî kezzebe âye"), say('say 7:64 8-10', "llezîne kezzebû bi-âyâtinâ"), say('dizi 7 64 8 10', "ellezî kezzebe âye"), say('dizi 7 64 8 13', "ellezî kezzebe âye inne kâne qavm")) + ' '
 + cumle(say('say 7:64 11-14', "innehum kânû qavmen 'amîn", True)) + ' ' +
 "Ölçüm xref 10:73 (emsal olarak basıldı), 21:77 (emsal olarak basıldı), okunmamış 3 ayet (sûre içi 3). "
 "Ölçüm nakarat3 kalıbı: 'ellezî kezzebe âye' süzgeç GEÇER; 'encâ ellezî ma'a' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'fe-enceynâhu' / 've ağraqna' — ayetler arası: yok.",
 "◈K — K1 'l-fulki' (6. kelime).",
 "◈B — —",
 "◈D — D1 'fe' + PERF + 'fe' + PERF + 've' + 'ellezî' + izafet + 'fî' + belirli + 've' + PERF + 'ellezî' + PERF + 'bi' + izafet + 'inne' + PERF + nekre + çoğul; "
 "D2 haber; kip yok; D3 10:73 eşi, 21:77 eşi, كذب ×2; D4 1P 5 · 3MP 7 · 3MS 3, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[64] + "; aktör yok (ölçüm); A2 Nûh'un yalanlanışı; onun ve gemide onunla birlikte olanların kurtarılışı; âyetleri yalanlayanların boğuluşu; kör bir kavim oluşları; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi soru → haber (ayetler arası).",
)
out = ['# ── blok 7:59-64 (2026-11-26) ──', 'MEAL18 = {']
for n in range(59, 65):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M18 = {']
for n in range(59, 65):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL18); M.update(M18)']
open('/home/claude/yamalar/metin_7_59_64.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
