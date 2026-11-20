# sûre 6 blok 11 (6:46-49) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b11/say2.txt'
os.environ['OLC'] = '/home/claude/b11/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Darlık ve bolluk; kulakları ve gözleri almak' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 46: "De ki: Bana haber verin, Allah işitmenizi ve gözlerinizi alsa ve kalplerinizi mühürlese, Allah'tan başka hangi ilâh onu size getirebilir? Bak, âyetleri nasıl türlü türlü açıklıyoruz; sonra onlar yüz çeviriyorlar.",
 47: "De ki: Bana haber verin, size Allah'ın azabı ansızın ya da açıkça gelse, zalim kavimden başkası mı helâk edilir?",
 48: "Biz elçileri ancak müjdeleyici ve uyarıcı olarak göndeririz. Kim iman eder ve düzeltirse, artık onlara korku yoktur ve onlar üzülmezler.",
 49: "Âyetlerimizi yalanlayanlara da yoldan çıkmakta olmaları sebebiyle azap dokunacaktır.",
}

T = {}
T[46] = ("muhatap 2MS (adsız; 'qul' — 1. kelime); muhatap 2MP (adsız; söz içi; 'era'eytum', 'sem'akum', 've ebsârakum', 'qulûbikum', 'ye'tîkum' — 2., 6., 7., 10. ve 15. kelime); "
         "'exaze' 3MS (fiil uyumu; 4. kelime — fail 5. kelime); 've xateme' 3MS (adsız; gönderge lafız 5. kelime; 8. kelime — fail 5. kelimedeki lafız); 'ye'tîkum' 3MS (adsız; gönderge 'ilâhun' 12. kelime, 15. kelime); "
         "'bih' 3MS (adsız; gönderge 'sem'akum' 6. kelime, 16. kelime); muhatap 2MS (adsız; 'unzur' — 17. kelime); konuşan 1P (adsız; 'nusarrifu' — 19. kelime); "
         "'hum', 'yasdifûn' 3MP (adsız; gönderge 6:33 11. kelime — 22. ve 23. kelime)")
T[47] = ("muhatap 2MS (adsız; 'qul' — 1. kelime); muhatap 2MS (adsız; söz içi; 'era'eytekum' — 2. kelime); muhatap 2MP (adsız; söz içi; 'era'eytekum', 'etâkum' — 2. ve 4. kelime); "
         "'etâkum' 3MS (fiil uyumu; 4. kelime — fail 5. kelime); 'yuhleku' 3MS (fiil uyumu; edilgen; naib-i faili 'l-qavmu' (13. kelimedeki ad), 11. kelime)")
T[48] = ("konuşan 1P (adsız; 'nursilu' — 2. kelime); 'âmene', 've aslaha' 3MS (adsız; gönderge 'men' 7. kelime — 8. ve 9. kelime); "
         "''aleyhim', 'hum', 'yahzenûn' 3MP (adsız; gönderge 'men' 7. kelime — 12., 14. ve 15. kelime)")
T[49] = ("'kezzebû' 3MP (adsız; gönderge 'llezîne', 2. kelime); konuşan 1P (adsız; 'bi-âyâtinâ' — 3. kelime); 'yemessuhumu' 3MS (fiil uyumu; 4. kelime — fail 5. kelime); "
         "'yemessuhumu' zamiri 3MP (adsız; gönderge 'llezîne' 1. kelime, 4. kelime); 'kânû', 'yefsuqûn' 3MP (adsız; gönderge 'llezîne' 1. kelime — 7. ve 8. kelime)")

D = {}
D[46] = ("◇ 'qul era'eytum in exaze'llâhu sem'akum ve ebsârakum ve xateme 'alâ qulûbikum men ilâhun ğayru'llâhi ye'tîkum bih, unzur keyfe nusarrifu'l-âyâti summe hum yasdifûn' — "
 "IMPV 2MS I. bab + 'e' + PERF 2MP I. bab + 'in' + PERF 3MS I. bab + lafız + 'sem'' + 2MP + 've' + çoğul 'basar' + 2MP + 've' + PERF 3MS I. bab + ''alâ' + çoğul 'qalb' + 2MP + 'men' + nekre 'ilâh' + 'ğayr' + lafız + "
 "IMPF 3MS I. bab + 2MP + 'bi' + 3MS + IMPV 2MS I. bab + 'keyf' + IMPF 1P II. bab + belirli çoğul 'âye' + 'summe' + 3MP + IMPF 3MP I. bab "
 "(ölçüm edim soru, emir, şart, kip COND 1 · IMPV 2 · INTG 2; 1P 1 · 2MP 6 · 2MS 2 · 3MP 3 · 3MS 4; bab I. bab ×7 · II. bab ×1). "
 "Allah lafzı 5. ve 14. sırada (ölçüm allah z=1,21); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=23 (n z=1,12); ölçüm '{{1|fâsıla يصدفون → ن, N sınıfı}}' — satır aynen (6:45 ن → 6:46 ن); "
 "ölçüm '{{1|harf 90 → harf3 89, isaret 1}}' — satır aynen; ölçüm '{{1|dış düğüm 3}}' — satır aynen. "
 "Ölçüm COND 1: 'in' (3. kelime); IMPV 2: 'qul' (1. kelime), 'unzur' (17. kelime); INTG 2: 'era'eytum' (2. kelime), 'men' (11. kelime); 've ebsârakum' (7.) ve 've xateme' (8.) kelimelerindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) أله ×3 (lafız 5., 'ilâhun' 12., lafız 14. kelime) (okuma). "
 + T[46] + " (okuma). "
  + cumle(say('say 6:46 11-15', "men ilâhun ğayru'llâhi ye'tîkum", True)) + ' '
 + cumle(say('say 6:46 17-20', "unzur keyfe nusarrifu'l-âyât", True), say('dizi 6 46 17 20', "nazara keyf sarref âye"), say('dizi 6 46 1 3', "qâle ra'â in")) + ' '
 "Ölçüm xref 28:71 (emsal olarak basıldı) ve okunmuş 2 ayet. "
 "Ölçüm nakarat3 kalıpları: 'nazara keyf sarref âye' süzgeç GEÇER, 'qâle ra'â in' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'exaze'llâhu' / 'ye'tîkum bih'; 'nusarrifu'l-âyât' / 'yasdifûn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'sem'akum' (6. kelime), 'ebsârakum' (7. kelime), 'qulûbikum' (10. kelime); B4 —.",
 "◈D — D1 IMPV + 'e' + PERF + 'in' + PERF + lafız + izafet + 've' + izafet + 've' + PERF + ''alâ' + izafet + 'men' + nekre + izafet + lafız + IMPF + 'bi' + IMPV + 'keyf' + IMPF + belirli + 'summe' + zamir + IMPF; "
 "D2 soru, emir, şart; COND ('in' 3. kelime), IMPV ('qul' 1. kelime, 'unzur' 17. kelime), INTG ('era'eytum' 2. kelime, 'men' 11. kelime); D3 أله ×3; 28:71 eşi; D4 1P 1 · 2MP 6 · 2MS 2 · 3MP 3 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[46] + "; aktör yok (ölçüm); A2 işitme, görme ve kalbin alınması sorusu; Allah'tan başka getirecek ilâh yokluğu; âyetlerin türlü türlü açıklanması; yüz çevirme; "
 "A3 'era'eytum in exaze'llâhu sem'akum ve ebsârakum ve xateme 'alâ qulûbikum men ilâhun ğayru'llâhi ye'tîkum bih' (söz içi, 2-16. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (16. kelime, ayet içi); şart → cevap (ayet içi; COND 'in' 3. kelime: 'in exaze'llâhu' / 'men ilâhun' (11. kelime)); "
 "şahıs geçişi 3 → 2 (ayetler arası); edim geçişi haber → soru, emir, şart (ayetler arası).",
)

D[47] = ("◇ 'qul era'eytekum in etâkum 'azâbu'llâhi bağteten ev cehreten hel yuhleku illa'l-qavmu'z-zâlimûn' — "
 "IMPV 2MS I. bab + 'e' + PERF 2MS I. bab + 2MS + 2MP + 'in' + PERF 3MS I. bab + 2MP + ''azâb' + lafız + nekre 'bağte' + 'ev' + nekre 'cehre' + 'hel' + edilgen IMPF 3MS IV. bab + 'illâ' + belirli 'qavm' + belirli çoğul etken ortaç 'zâlim' "
 "(ölçüm edim soru, emir, şart, kip COND 1 · IMPV 1 · INTG 2 · RES 1; 2MP 2 · 2MS 3 · 3MS 2; bab I. bab ×3 · IV. bab ×1). "
 "Allah lafzı 6. sırada (ölçüm allah z=0,90); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=14 (n z=0,17); ölçüm '{{2|biçim HASR}}' — satır aynen; ölçüm '{{2|EDİLGEN 1/4 fiil, pas z=1,10}}' — satır aynen; "
 "ölçüm '{{2|fâsıla ٱلظلمون → ن, N sınıfı}}' — satır aynen (6:46 ن → 6:47 ن); ölçüm '{{2|harf 55 → harf3 55, isaret 0}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' ve '{{2|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 'in' (3. kelime); IMPV 1: 'qul' (1. kelime); INTG 2: 'era'eytekum' (2. kelime), 'hel' (10. kelime); RES 1: 'illâ' (12. kelime) (okuma). "
 + T[47] + " (okuma). "
 + cumle(say('say 6:47 1-3', "qul era'eytekum in", True), say('dizi 6 47 1 3', "qâle ra'â in")) + ' '
 + cumle(say('say 6:47 7-9', "bağteten ev cehreten", True)) + ' '
 "Ölçüm xref 6:40 (basılmış) ve okunmuş 2 ayet. "
 "Ölçüm nakarat3 kalıpları: 'qâle ra'â in etâ 'azâb allâh' süzgeç GEÇER, 'qâle ra'â in' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'bağteten' / 'cehreten' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'e' + PERF + 'in' + PERF + izafet + lafız + nekre + 'ev' + nekre + 'hel' + IMPF + 'illâ' + belirli + belirli; "
 "D2 soru, emir, şart; COND ('in' 3. kelime), IMPV ('qul' 1. kelime), INTG ('era'eytekum' 2. kelime, 'hel' 10. kelime), RES ('illâ' 12. kelime); D3 —; D4 2MP 2 · 2MS 3 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[47] + "; aktör yok (ölçüm); A2 azabın ansızın ya da açıkça gelmesi; helâk edilenin zalim kavim oluşu; "
 "A3 'era'eytekum in etâkum 'azâbu'llâhi bağteten ev cehreten hel yuhleku illa'l-qavmu'z-zâlimûn' (söz içi, 2-14. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (14. kelime, ayet içi); şart → cevap (ayet içi; COND 'in' 3. kelime: 'in etâkum' / 'hel yuhleku' (10. kelime)); şahıs geçişi yok (ayetler arası).",
)

D[48] = ("◇ 've mâ nursilu'l-murselîne illâ mubeşşirîne ve munzirîn, fe-men âmene ve aslaha fe-lâ xavfun 'aleyhim ve lâ hum yahzenûn' — "
 "'ve' + 'mâ' + IMPF 1P IV. bab + belirli çoğul edilgen ortaç 'mursel' + 'illâ' + çoğul etken ortaç 'mubeşşir' + 've' + çoğul etken ortaç 'munzir' + 'fe' + 'men' + PERF 3MS IV. bab + 've' + PERF 3MS IV. bab + "
 "'fe' + 'lâ' + nekre 'xavf' + ''alâ' + 3MP + 've' + 'lâ' + 3MP + IMPF 3MP I. bab "
 "(ölçüm edim şart, kip COND 1 · NEG 3 · RES 1; 1P 1 · 3MP 4 · 3MS 2; bab I. bab ×1 · IV. bab ×3). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=15 (n z=0,27); ölçüm '{{3|biçim HASR}}' — satır aynen; ölçüm '{{3|fâsıla يحزنون → ن, N sınıfı}}' — satır aynen (6:47 ن → 6:48 ن); "
 "ölçüm '{{3|harf 66 → harf3 65, isaret 1}}' — satır aynen; ölçüm '{{3|dış düğüm 2}}' — satır aynen. "
 "Ölçüm COND 1: 'men' (7. kelime); NEG 3: 'mâ' (1. kelime), 'lâ' (10. kelime), 'lâ' (13. kelime); RES 1: 'illâ' (4. kelime); 've mâ' (1.) kelimesindeki 've' CONJ; 'fe-men' (7.) kelimesindeki 'fe' REM; 'fe-lâ' (10.) kelimesindeki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) رسل ×2 ('nursilu' 2. / 'l-murselîne' 3. kelime) (okuma). "
 + T[48] + " (okuma). "
 + cumle(say('say 6:48 1-6', "ve mâ nursilu'l-murselîne illâ mubeşşirîne ve munzirîn", True)) + ' '
 + cumle(say('say 6:48 10-11', "fe-lâ xavfun", True), say('say 6:48 13-15', "ve lâ hum yahzenûn")) + ' '
 "Ölçüm xref 18:56 (emsal olarak basıldı) ve okunmamış 1 ayet. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'mubeşşirîne' / 'munzirîn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'mâ' + IMPF + belirli + 'illâ' + edilgen ortaç + 've' + etken ortaç + 'fe' + 'men' + PERF + 've' + PERF + 'fe' + 'lâ' + nekre + ''alâ' + 've' + 'lâ' + zamir + IMPF; "
 "D2 şart; COND ('men' 7. kelime), NEG ('mâ' 1. kelime, 'lâ' 10. kelime, 'lâ' 13. kelime), RES ('illâ' 4. kelime); D3 رسل ×2; 18:56 eşi; D4 1P 1 · 3MP 4 · 3MS 2, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[48] + "; aktör yok (ölçüm); A2 elçilerin müjdeleyici ve uyarıcı oluşu; iman edip düzeltene korku ve üzüntü yokluğu; "
 "A3 —; "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; COND 'men' 7. kelime: 'fe-men âmene' / 'fe-lâ xavfun' (10. kelime)); şahıs geçişi 2 → 3 (ayetler arası); edim geçişi soru, emir, şart → şart (ayetler arası).",
)

D[49] = ("◇ 've'llezîne kezzebû bi-âyâtinâ yemessuhumu'l-'azâbu bi-mâ kânû yefsuqûn' — "
 "'ve' + 'ellezî' + PERF 3MP II. bab + 'bi' + çoğul 'âye' + 1P + IMPF 3MS I. bab + 3MP + belirli ''azâb' + 'bi' + 'mâ' + PERF 3MP I. bab + IMPF 3MP I. bab "
 "(ölçüm edim haber, kip yok; 1P 1 · 3MP 7 · 3MS 1; bab I. bab ×3 · II. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=8 (n z=-0,47); ölçüm '{{4|fâsıla يفسقون → ن, N sınıfı}}' — satır aynen (6:48 ن → 6:49 ن); "
 "ölçüm '{{4|harf 45 → harf3 43, isaret 2}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; 've'llezîne' (1.) kelimesindeki 've' CONJ (okuma). "
 + T[49] + " (okuma). "
 + cumle(say('say 6:49 1-3', "ve'llezîne kezzebû bi-âyâtinâ", True), say('say 6:49 2-3', "kezzebû bi-âyâtinâ")) + ' '
 + cumle(say('say 6:49 6-8', "bi-mâ kânû yefsuqûn", True), say('dizi 6 49 5 7', "'azâb mâ kâne")) + ' '
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: ''azâb mâ kâne' süzgeç GEÇER, 'ellezî kezzebe âye' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: 6:48 / 6:49 ('fe-men âmene' / 've'llezîne kezzebû').",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'ellezî' + PERF + 'bi' + izafet + IMPF + belirli + 'bi' + 'mâ' + PERF + IMPF; "
 "D2 haber; kip yok; D3 —; D4 1P 1 · 3MP 7 · 3MS 1, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[49] + "; aktör yok (ölçüm); A2 yalanlayanlara azabın dokunması; yoldan çıkma sebebi; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi şart → haber (ayetler arası); bölüm kapanışı.",
)
out = ['# ── blok 6:46-49 (2026-11-20) ──', 'MEAL11 = {']
for n in range(46, 50):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M11 = {']
for n in range(46, 50):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL11); M.update(M11)']
open('/home/claude/yamalar/metin_6_46_49.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
