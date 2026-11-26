# sûre 7 blok 19 (7:65-69) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b19/say2.txt'
os.environ['OLC'] = '/home/claude/b19/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Nûh ve kavmi; Hûd ve Âd' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))
_AK5 = _esc(re.search(r'aktör: adlı .*?adsız `racül` 8\. sırada', _OL[4]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 65: "Âd'a kardeşleri Hûd'u gönderdik. Dedi ki: Ey kavmim, Allah'a kulluk edin. Sizin O'ndan başka bir ilâhınız yok. Sakınmaz mısınız?",
 66: "Kavminden inkâr eden ileri gelenler dedi ki: Gerçekten biz seni bir beyinsizlik içinde görüyoruz ve gerçekten biz seni yalancılardan sanıyoruz.",
 67: "Dedi ki: Ey kavmim bende bir beyinsizlik yok; fakat ben âlemlerin Rabbinden bir elçiyim.",
 68: "Size Rabbimin risaletlerini tebliğ ediyorum ve ben sizin için güvenilir bir öğüt vereniyim.",
 69: "Sizi uyarması için Rabbinizden içinizden bir adam aracılığıyla size bir zikir gelmesine mi şaştınız? Nûh kavminden sonra sizi halifeler kıldığı zamanı hatırlayın ve sizi yaratılışta genişlikçe artırdı. Öyleyse Allah'ın nimetlerini hatırlayın; ola ki kurtuluşa erersiniz.",
}

T = {}
T[65] = ("'exâhum' 3MP eki (adsız; gönderge ''âdin' 2. kelime, 3. kelime); 'qâle' 3MS (adsız; gönderge 'hûden' 4. kelime, 5. kelime); konuşan 1S eki (adsız; söz içi; 'qavmi' — 6. kelime); "
         "muhatap 2MP (adsız; söz içi; 'u'budu', 'tetteqûn' — 7. ve 15. kelime); muhatap 2MP eki (adsız; söz içi; 'lekum' — 10. kelime); 'ğayruhû' 3MS eki (adsız; söz içi; gönderge 'llâhe' 8. kelime, 13. kelime)")
T[66] = ("'qâle' 3MS (fiil uyumu; 1. kelime — fail 2. kelime); 'kefarû' 3MP (adsız; gönderge 'llezîne' 3. kelime, 4. kelime); 'qavmihî' 3MS eki (adsız; gönderge 7:65 4. kelime, 6. kelime); "
         "konuşan 1P eki (adsız; söz içi; 'innâ', 've innâ' — 7. ve 11. kelime); konuşan 1P (adsız; söz içi; 'nerâke', 'nezunnuke' — 8. ve 12. kelime); muhatap 2MS eki (adsız; söz içi; 'nerâke', 'nezunnuke' — 8. ve 12. kelime)")
T[67] = ("'qâle' 3MS (adsız; gönderge 7:65 4. kelime, 1. kelime); konuşan 1S eki (adsız; söz içi; 'qavmi' — 2. kelime); 'leyse' 3MS (fiil uyumu; söz içi; 3. kelime — fail 5. kelime); konuşan 1S eki (adsız; söz içi; 'bî', 'lâkinnî' — 4. ve 6. kelime)")
T[68] = ("konuşan 1S (adsız; söz içi; 'ubelliğukum' — 1. kelime); muhatap 2MP eki (adsız; söz içi; 'ubelliğukum', 'lekum' — 1. ve 5. kelime); konuşan 1S eki (adsız; söz içi; 'rabbî' — 3. kelime); konuşan 1S (adsız; söz içi; 'ene' — 4. kelime)")
T[69] = ("muhatap 2MP (adsız; söz içi; ''acibtum' — 1. kelime); 'câ'ekum' 3MS (fiil uyumu; söz içi; 3. kelime — fail 4. kelime); "
         "muhatap 2MP eki (adsız; söz içi; 'câ'ekum', 'rabbikum', 'minkum', 'yunzirakum', 'ce'alekum', 'zâdekum', 'le'allekum' — 3., 6., 9., 10., 13., 19. ve 26. kelime); "
         "'yunzirakum' 3MS (adsız; söz içi; gönderge 'raculin' 8. kelime, 10. kelime); muhatap 2MP (adsız; söz içi; 'zkurû', 'zkurû', 'tuflihûn' — 11., 23. ve 27. kelime); "
         "'ce'alekum', 'zâdekum' 3MS (adsız; söz içi; gönderge 'rabbikum' 6. kelime — 13. ve 19. kelime)")

D = {}
D[65] = ("◇ 've ilâ 'âdin exâhum hûden qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû e-fe-lâ tetteqûn' — "
 "'ve' + 'ilâ' + nekre özel ad ''âd' + 'ax' + 3MP + nekre özel ad 'hûd' + PERF 3MS I. bab + 'yâ' + 'qavm' + 1S + IMPV 2MP I. bab + 'allâh' + 'mâ' + 'li' + 2MP + 'min' + nekre 'ilâh' + 'ğayr' + 3MS + 'e' + 'fe' + 'lâ' + IMPF 2MP VIII. bab "
 "(ölçüm edim soru, emir, nida, kip IMPV 1 · INTG 1 · NEG 2 · VOC 1; 1S 1 · 2MP 5 · 3MP 1 · 3MS 2; bab I. bab ×2 · VIII. bab ×1). "
 "Allah lafzı 8. sırada (ölçüm allah z=0,81); Rab yok; esmâ yok (ölçüm); ölçüm '{{1|" + _AK1 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=15 (n z=0,27); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:64 ن → 7:65 ن); "
 "ölçüm '{{1|harf 62 → harf3 56, isaret 6}}' — satır aynen; ölçüm '{{1|dış düğüm 5}}' — satır aynen; ölçüm '{{1|İÇ düğüm 3}}' — satır aynen. "
 "Ölçüm '{{1|esit2 → 11:50 oran 0,8966 kademe BENZER}}' — satır aynen. "
 "Ölçüm IMPV 1: 'u'budu' (7. kelime); INTG 1: 'e-fe-lâ' (14. kelime; 'e'); NEG 2: 'mâ' (9. kelime), 'e-fe-lâ' (14. kelime; 'lâ'); VOC 1: 'yâ' (6. kelime); "
 "'ve ilâ' (1.) kelimesindeki 've' CONJ; 'e-fe-lâ' (14.) kelimesindeki 'fe' SUP (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 ('llâhe' 8. / 'ilâhin' 12. kelime) (okuma). "
 + T[65] + " (okuma). "
 + cumle(say('say 7:65 1-4', "ve ilâ 'âdin exâhum hûden", True), say('dizi 7 65 1 13', "ilâ 'âd ax hûd qâle qavm 'abede allâh mâ _ min ilâh ğayr")) + ' '
 + cumle(say('say 7:65 7-8', "u'budu'llâhe", True), say('say 7:65 9-13', "mâ lekum min ilâhin ğayruhû"), say('say 7:65 5-13', "qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû"), say('dizi 7 65 5 13', "qâle qavm 'abede allâh mâ _ min ilâh ğayr")) + ' '
 + cumle(say('say 7:65 14-15', "e-fe-lâ tetteqûn", True)) + ' ' +
 "Ölçüm xref 7:59 (basılmış), 11:50 (basılmış), 11:61 (basılmış), 11:84 (basılmış), 23:23 (basılmış), 23:32 (basılmış), okunmamış 2 ayet (sûre içi 2). "
 "Ölçüm nakarat3 kalıbı: 'qâle qavm 'abede allâh mâ _ min ilâh ğayr' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'ilâ' + nekre + izafet + nekre + PERF + 'yâ' + izafet + IMPV + lafız + 'mâ' + 'li' + 'min' + nekre + izafet + 'e' + 'fe' + 'lâ' + IMPF; "
 "D2 soru, emir, nida; IMPV ('u'budu' 7. kelime), INTG ('e-fe-lâ' 14. kelime), NEG ('mâ' 9. kelime, 'e-fe-lâ' 14. kelime), VOC ('yâ' 6. kelime); D3 أله ×2; D4 1S 1 · 2MP 5 · 3MP 1 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[65] + "; aktör adlı ''âdin' (2. kelime; ölçüm rol mecrur), adlı 'hûden' (4. kelime; ölçüm rol meful); A2 Âd'a kardeşleri Hûd'un gönderilişi; Allah'a kulluk çağrısı; O'ndan başka ilâh olmayışı; sakınmaya çağıran soru; "
 "A3 'yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû e-fe-lâ tetteqûn' (söz içi, 6-15. kelime); "
 "A4 " + BOLUM + "; söz açılır (6. kelime); söz kapanır (15. kelime, ayet içi); şahıs geçişi 3 → 2 (ayetler arası); edim geçişi haber → soru, emir, nida (ayetler arası).",
)

D[66] = ("◇ 'qâle'l-mele'u'llezîne kefarû min qavmihî innâ le-nerâke fî sefâhetin ve innâ le-nezunnuke mine'l-kâzibîn' — "
 "PERF 3MS I. bab + belirli 'mele'' + 'ellezî' + PERF 3MP I. bab + 'min' + 'qavm' + 3MS + 'inne' + 1P + 'le' + IMPF 1P I. bab + 2MS + 'fî' + nekre 'sefâhe' + 've' + 'inne' + 1P + 'le' + IMPF 1P I. bab + 2MS + 'min' + belirli çoğul etken ortaç 'kâzib' "
 "(ölçüm edim haber, kip EMPH 2; 1P 4 · 2MS 2 · 3MP 2 · 3MS 2; bab I. bab ×4). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=14 (n z=0,17); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:65 ن → 7:66 ن); "
 "ölçüm '{{2|simetri \\[3, 3, 7, 1\\]}}' — satır aynen; ölçüm '{{2|harf 60 → harf3 57, isaret 3}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen; ölçüm '{{2|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm EMPH 2: 'le-nerâke' (8. kelime; 'le'), 'le-nezunnuke' (12. kelime; 'le'); 've innâ' (11.) kelimesindeki 've' CONJ (okuma). "
 + T[66] + " (okuma). "
 + cumle(say('say 7:66 2-5', "l-mele'u'llezîne kefarû min", True), say('say 7:66 3-6', "llezîne kefarû min qavmihî"), say('dizi 7 66 1 6', "qâle mele' ellezî kefere min qavm"), say('dizi 7 66 1 3', "qâle mele' ellezî")) + ' '
 + cumle(say('say 7:66 7-10', "innâ le-nerâke fî sefâhetin", True), say('say 7:66 5-9', "min qavmihî innâ le-nerâke fî"), say('dizi 7 66 5 9', "min qavm inne ra'â fî")) + ' '
 + cumle(say('say 7:66 11-14', "ve innâ le-nezunnuke mine'l-kâzibîn", True)) + ' ' +
 "Ölçüm xref 11:27 (emsal olarak basıldı), 23:24 (emsal olarak basıldı), okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıbı: 'qâle mele' ellezî kefere min qavm' süzgeç GEÇER; 'min qavm inne ra'â fî' süzgeç GEÇER; 'qâle mele' ellezî' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + belirli + 'ellezî' + PERF + 'min' + izafet + 'inne' + 'le' + IMPF + 'fî' + nekre + 've' + 'inne' + 'le' + IMPF + 'min' + belirli; "
 "D2 haber; EMPH ('le-nerâke' 8. kelime, 'le-nezunnuke' 12. kelime); D3 11:27 eşi, 23:24 eşi; D4 1P 4 · 2MS 2 · 3MP 2 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[66] + "; aktör yok (ölçüm); A2 kavmin inkâr eden ileri gelenlerinin Hûd'u beyinsizlik içinde görmesi; onu yalancılardan sanmaları; "
 "A3 'innâ le-nerâke fî sefâhetin ve innâ le-nezunnuke mine'l-kâzibîn' (söz içi, 7-14. kelime); "
 "A4 " + BOLUM + "; söz açılır (7. kelime); söz kapanır (14. kelime, ayet içi); şahıs sayısında beraberlik (1P 4 · 3. şahıs 4 — ölçüm baskın 1); şahıs geçişi 2 → 1 (ayetler arası); edim geçişi soru, emir, nida → haber (ayetler arası).",
)

D[67] = ("◇ 'qâle yâ qavmi leyse bî sefâhetun ve lâkinnî rasûlun min rabbi'l-'âlemîn' — "
 "PERF 3MS I. bab + 'yâ' + 'qavm' + 1S + PERF 3MS I. bab + 'bi' + 1S + nekre 'sefâhe' + 've' + 'lâkinne' + 1S + nekre 'rasûl' + 'min' + 'rabb' + belirli çoğul ''âlem' "
 "(ölçüm edim nida, kip VOC 1; 1S 3 · 3MS 2; bab I. bab ×2). "
 "Allah lafzı yok; Rab 9. sırada (ölçüm rab z=1,81); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{3|yıldız ★}}' — satır aynen (kaynak rab, z=1,81); n=10 (n z=-0,26); ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:66 ن → 7:67 ن); "
 "ölçüm '{{3|harf 39 → harf3 37, isaret 2}}' — satır aynen; ölçüm '{{3|dış düğüm 3}}' — satır aynen; ölçüm '{{3|İÇ düğüm 2}}' — satır aynen. "
 "Ölçüm '{{3|esit2 → 7:61 oran 0,9041 kademe BENZER}}' — satır aynen. "
 "Ölçüm VOC 1: 'yâ' (2. kelime); 've lâkinnî' (6.) kelimesindeki 've' REM (okuma). "
 + T[67] + " (okuma). "
 + cumle(say('say 7:67 1-4', "qâle yâ qavmi leyse bî"), say('dizi 7 67 1 4', "qâle qavm leyse _"), say('say 7:67 2-5', "yâ qavmi leyse bî sefâhetun", True)) + ' '
 + cumle(say('say 7:67 6-10', "ve lâkinnî rasûlun min rabbi'l-'âlemîn"), say('dizi 7 67 6 10', "lâkinne rasûl min rabb 'âlem"), say('say 7:67 7-10', "rasûlun min rabbi'l-'âlemîn"), say('dizi 7 67 7 10', "rasûl min rabb 'âlem")) + ' ' +
 "Ölçüm xref 7:61 (basılmış), 26:16 (basılmış), 43:46 (basılmış), okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıbı: 'lâkinne rasûl min rabb 'âlem' süzgeç GEÇER; 'rasûl min rabb 'âlem' süzgeç GEÇER; 'qâle qavm leyse _' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + 'yâ' + izafet + PERF + 'bi' + nekre + 've' + 'lâkinne' + nekre + 'min' + izafet + belirli; "
 "D2 nida; VOC ('yâ' 2. kelime); D3 —; D4 1S 3 · 3MS 2, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[67] + "; aktör yok (ölçüm); A2 Hûd'un kendisinde beyinsizlik olmadığını bildirmesi; âlemlerin Rabbinden elçi oluşu; "
 "A3 'yâ qavmi leyse bî sefâhetun ve lâkinnî rasûlun min rabbi'l-'âlemîn' (söz içi, 2-10. kelime; ayet sonunda kapanmıyor); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); şahıs geçişi yok (ayetler arası); edim geçişi haber → nida (ayetler arası).",
)

D[68] = ("◇ 'ubelliğukum risâlâti rabbî ve ene lekum nâsihun emîn' — "
 "IMPF 1S II. bab + 2MP + çoğul 'risâle' + 'rabb' + 1S + 've' + 'ene' + 'li' + 2MP + nekre etken ortaç 'nâsih' + nekre 'emîn' "
 "(ölçüm edim haber, kip yok; 1S 3 · 2MP 2; bab II. bab ×1). "
 "Allah lafzı yok; Rab 3. sırada (ölçüm rab z=2,72); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{4|yıldız ★★}}' — satır aynen (kaynak rab, z=2,72); n=7 (n z=-0,58); ölçüm '{{4|fâsıla " + _F[3] + " → ن, N sınıfı}}' — satır aynen (7:67 ن → 7:68 ن); "
 "ölçüm '{{4|harf 29 → harf3 28, isaret 1}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; 've ene' (4.) kelimesindeki 've' REM (okuma). "
 + T[68] + " (okuma). "
 + cumle(say('say 7:68 1-3', "ubelliğukum risâlâti rabbî", True), say('dizi 7 68 1 3', "belliğ risâle rabb")) + ' '
 + cumle(say('say 7:68 4-7', "ve ene lekum nâsihun emîn", True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'belliğ risâle rabb' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPF + izafet + izafet + 've' + 'ene' + 'li' + nekre + nekre; "
 "D2 haber; kip yok; D3 —; D4 1S 3 · 2MP 2, sahset ['1', '2'], iltifât 0.",
 "◈A — A1 " + T[68] + "; aktör yok (ölçüm); A2 Rabbin risaletlerinin tebliği; güvenilir öğüt veren oluş; "
 "A3 söz sürüyor (7:67 2. kelimeden, 1-7. kelime; ayet sonunda kapanmıyor); "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi nida → haber (ayetler arası).",
)

D[69] = ("◇ 'e-ve-'acibtum en câ'ekum zikrun min rabbikum 'alâ raculin minkum li-yunzirakum ve'zkurû iz ce'alekum xulefâ'e min ba'di qavmi nûhin ve zâdekum fi'l-xalqi bastaten fe'zkurû âlâ'e'llâhi le'allekum tuflihûn' — "
 "'e' + 've' + PERF 2MP I. bab + 'en' + PERF 3MS I. bab + 2MP + nekre mastar 'zikr' + 'min' + 'rabb' + 2MP + ''alâ' + nekre 'racul' + 'min' + 2MP + 'li' + IMPF 3MS IV. bab + 2MP + 've' + IMPV 2MP I. bab + 'iz' + PERF 3MS I. bab + 2MP + çoğul 'xalîfe' + 'min' + 'ba'd' + 'qavm' + özel ad 'nûh' + "
 "'ve' + PERF 3MS I. bab + 2MP + 'fî' + belirli 'xalq' + nekre 'basta' + 'fe' + IMPV 2MP I. bab + çoğul 'âlâ'' + 'allâh' + 'le'alle' + 2MP + IMPF 2MP IV. bab "
 "(ölçüm edim soru, emir, kip IMPV 2 · INTG 1; 2MP 15 · 3MS 4; bab I. bab ×6 · IV. bab ×2). "
 "Allah lafzı 25. sırada (ölçüm allah z=0,21); Rab 6. sırada (ölçüm rab z=0,47); esmâ yok (ölçüm); ölçüm '{{5|" + _AK5 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{5|yıldız ★}}' — satır aynen (kaynak n, z=1,55); n=27 (n z=1,55); ölçüm '{{5|fâsıla " + _F[4] + " → ن, N sınıfı}}' — satır aynen (7:68 ن → 7:69 ن); "
 "ölçüm '{{5|simetri \\[4, 2, 9, 1\\]}}' — satır aynen; ölçüm '{{5|harf 124 → harf3 114, isaret 10}}' — satır aynen; ölçüm '{{5|dış düğüm 0}}' — satır aynen. "
 "Ölçüm IMPV 2: 'zkurû' (11. kelime), 'zkurû' (23. kelime); INTG 1: 'e' (1. kelime); 've'zkurû' (11.) kelimesindeki 've' REM; 've zâdekum' (19.) kelimesindeki 've' CONJ; 'fe'zkurû' (23.) kelimesindeki 'fe' REM (okuma). "
 "Kök ikilemesi (ölçüm) ذكر ×3 ('zikrun' 4. / 'zkurû' 11. / 'zkurû' 23. kelime) (okuma). "
 + T[69] + " (okuma). "
 + cumle(say('say 7:69 1-9', "e-ve-'acibtum en câ'ekum zikrun min rabbikum 'alâ raculin minkum", True), say('say 7:69 1-10', "e-ve-'acibtum en câ'ekum zikrun min rabbikum 'alâ raculin minkum li-yunzirakum"), say('dizi 7 69 1 10', "'acibu en câ'e zikr min rabb 'alâ racul min enzere")) + ' '
 + cumle(say('say 7:69 11-18', "ve'zkurû iz ce'alekum xulefâ'e min ba'di qavmi nûhin", True), say('say 7:69 11-16', "ve'zkurû iz ce'alekum xulefâ'e min ba'di"), say('dizi 7 69 11 16', "zekere iz ce'ale xalîfe min ba'd")) + ' '
 + cumle(say('say 7:69 19-22', "ve zâdekum fi'l-xalqi bastaten", True), say('say 7:69 23-25', "fe'zkurû âlâ'e'llâhi"), say('dizi 7 69 23 25', "zekere âlâ' allâh"), say('say 7:69 26-27', "le'allekum tuflihûn")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: ''acibu en câ'e zikr min rabb 'alâ racul min enzere' süzgeç GEÇER; 'zekere iz ce'ale xalîfe min ba'd' süzgeç GEÇER; 'zekere âlâ' allâh' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B2 'l-xalqi' (21. kelime).",
 "◈D — D1 'e' + 've' + PERF + 'en' + PERF + nekre + 'min' + izafet + ''alâ' + nekre + 'min' + 'li' + IMPF + 've' + IMPV + 'iz' + PERF + çoğul + 'min' + izafet + izafet + özel ad + 've' + PERF + 'fî' + belirli + nekre + 'fe' + IMPV + izafet + lafız + 'le'alle' + IMPF; "
 "D2 soru, emir; IMPV ('zkurû' 11. kelime, 'zkurû' 23. kelime), INTG ('e' 1. kelime); D3 ذكر ×3; D4 2MP 15 · 3MS 4, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[69] + "; aktör adlı 'nûhin' (18. kelime; ölçüm rol mecrur), adsız 'raculin' (8. kelime; ölçüm racül); A2 içlerinden bir adam aracılığıyla gelen zikre şaşmanın sorulması; Nûh kavminden sonra halifeler kılınmanın ve yaratılışta genişliğin hatırlatılması; Allah'ın nimetlerini anma ve kurtuluş umudu; "
 "A3 söz sürüyor (7:67 2. kelimeden, 1-27. kelime); "
 "A4 " + BOLUM + "; söz kapanır (27. kelime); şahıs geçişi 1 → 2 (ayetler arası); edim geçişi haber → soru, emir (ayetler arası).",
)
out = ['# ── blok 7:65-69 (2026-11-26) ──', 'MEAL19 = {']
for n in range(65, 70):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M19 = {']
for n in range(65, 70):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL19); M.update(M19)']
open('/home/claude/yamalar/metin_7_65_69.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
