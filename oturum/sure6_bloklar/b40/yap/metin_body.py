# sûre 6 blok 40 (6:161-165) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b40/say2.txt'
os.environ['OLC'] = '/home/claude/b40/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Bekledikleri; dosdoğru din; yeryüzünün halifeleri' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 161: "De ki: Şüphesiz Rabbim beni dosdoğru bir yola iletti; dosdoğru bir dine, hanîf olarak İbrâhîm'in milletine. O, ortak koşanlardan değildi.",
 162: "De ki: Şüphesiz benim namazım, kurbanım, hayatım ve ölümüm âlemlerin Rabbi Allah'adır.",
 163: "O'nun ortağı yoktur. Bana bu emredildi ve ben teslim olanların öncüsüyüm.",
 164: "De ki: Allah'tan başka bir Rab mi arayayım, oysa O her şeyin Rabbidir? Her can kazandığını yalnızca kendi aleyhine kazanır. Hiçbir yük taşıyan başkasının yükünü taşımaz. Sonra dönüşünüz Rabbinizedir; O, içinde ayrılığa düşmüş olduğunuz şeyi size haber verecektir.",
 165: "Sizi yeryüzünün halifeleri kılan O'dur; kiminizi kiminizin üstüne derecelerle yükseltti, size verdiğinde sizi sınamak için. Şüphesiz Rabbinin cezası çabuktur; şüphesiz O bağışlayandır, merhamet edendir.",
}

T = {}
T[161] = ("muhatap 2MS (adsız; 'qul' — 1. kelime); konuşan 1S eki (adsız; söz içi; 'innenî', 'hedânî', 'rabbî' — 2., 3. ve 4. kelime); 'hedânî' 3MS (fiil uyumu; söz içi; 3. kelime — fail 4. kelime); "
          "'kâne' 3MS (adsız; söz içi; gönderge 'ibrâhîme' 11. kelime, 14. kelime)")
T[162] = ("muhatap 2MS (adsız; 'qul' — 1. kelime); konuşan 1S eki (adsız; söz içi; 'salâtî', 'nusukî', 'mahyâye', 'memâtî' — 3., 4., 5. ve 6. kelime)")
T[163] = ("'leh' 3MS (adsız; söz içi; gönderge 6:162 7. kelime, 3. kelime); konuşan 1S (adsız; söz içi; edilgen, naib-i faili konuşan; 'umirtu' — 5. kelime); konuşan 1S (adsız; söz içi; 'ene' — 6. kelime)")
T[164] = ("muhatap 2MS (adsız; 'qul' — 1. kelime); konuşan 1S (adsız; söz içi; 'ebğî' — 4. kelime); 'huve' 3MS (adsız; söz içi; gönderge 'llâhi' 3. kelime, 6. kelime); "
          "'teksibu' 3FS (fiil uyumu; söz içi; 11. kelime — fail 12. kelime); ''aleyhâ' 3FS eki (adsız; söz içi; gönderge 'nefsin' 13. kelime, 15. kelime); 'teziru' 3FS (fiil uyumu; söz içi; 17. kelime — fail 18. kelime); "
          "muhatap 2MP eki (adsız; söz içi; 'rabbikum', 'merci'ukum', 'fe-yunebbi'ukum' — 23., 24. ve 25. kelime); 'fe-yunebbi'ukum' 3MS (adsız; söz içi; gönderge 'rabbikum' 23. kelime, 25. kelime); "
          "muhatap 2MP (adsız; söz içi; 'kuntum', 'taxtelifûn' — 27. ve 29. kelime); 'fîhi' 3MS eki (adsız; söz içi; gönderge 'bimâ' 26. kelime, 28. kelime)")
T[165] = ("'huve' 3MS (adsız; gönderge 6:164 23. kelime, 1. kelime); 'ce'alekum', 'refe'a', 'li-yebluvekum', 'âtâkum' 3MS (adsız; gönderge 'llezî' 2. kelime — 3., 6., 11. ve 14. kelime); "
          "muhatap 2MP eki (adsız; 'ce'alekum', 'ba'dakum', 'li-yebluvekum', 'âtâkum' — 3., 7., 11. ve 14. kelime); muhatap 2MS eki (adsız; 'rabbeke' — 16. kelime); 'innehû' 3MS eki (adsız; gönderge 'rabbeke' 16. kelime, 19. kelime)")

D = {}
D[161] = ("◇ 'qul innenî hedânî rabbî ilâ sırâtin mustaqîmin dînen qiyemen millete ibrâhîme hanîfâ, ve mâ kâne mine'l-muşrikîn' — "
 "IMPV 2MS I. bab + 'inne' + 1S + PERF 3MS I. bab + 1S + 'rabb' + 1S + 'ilâ' + nekre 'sırât' + nekre etken ortaç 'mustaqîm' + nekre 'dîn' + nekre 'qiyem' + 'mille' + özel ad 'ibrâhîm' + nekre 'hanîf' + 've' + 'mâ' + PERF 3MS I. bab + 'min' + belirli çoğul etken ortaç 'muşrik' "
 "(ölçüm edim emir, kip IMPV 1 · NEG 1; 1S 3 · 2MS 1 · 3MS 2; bab I. bab ×3). "
 "Allah lafzı yok; Rab 4. sırada (ölçüm rab z=1,01); esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm '{{1|aktör: adlı إِبْراهِيم 11\\. sırada \\(kisi, rol mecrur\\)}}' — satır aynen; aktör adlı 'ibrâhîme' 11. sırada — milleti anılan (okuma). "
 "Ölçüm 'yıldız yok' — satır aynen; n=16 (n z=0,38); ölçüm '{{1|fâsıla ٱلمشركين → ن, N sınıfı}}' — satır aynen (6:160 ن → 6:161 ن); "
 "ölçüm '{{1|harf 70 → harf3 64, isaret 6}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 1: 'qul' (1. kelime); NEG 1: 'mâ' (13. kelime); 've mâ' (13.) kelimesindeki 've' CIRC; 'innenî' (2.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) قوم ×2 ('mustaqîmin' 7. / 'qiyemen' 9. kelime) (okuma). "
 + T[161] + " (okuma). "
 + cumle(say('say 6:161 5-7', "ilâ sırâtin mustaqîmin", True), say('dizi 6 161 5 7', "ilâ sırât mustaqîm")) + ' '
 + cumle(say('say 6:161 14-16', "kâne mine'l-muşrikîn", True), say('dizi 6 161 14 16', "kâne min muşrik")) + ' ' +
 "Ölçüm xref okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'kâne min muşrik' süzgeç GEÇMEZ, 'ilâ sırât mustaqîm' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'inne' + PERF + izafet + 'ilâ' + nekre + nekre + nekre + nekre + 'mille' + özel ad + nekre + 've' + 'mâ' + PERF + 'min' + belirli; "
 "D2 emir; IMPV ('qul' 1. kelime), NEG ('mâ' 13. kelime); D3 قوم ×2; D4 1S 3 · 2MS 1 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[161] + "; aktör adlı 'ibrâhîme' (11. kelime; ölçüm rol mecrur); A2 Rabbin dosdoğru yola iletmesinin söylenmesi; dosdoğru din, hanîf İbrâhîm'in milleti; onun ortak koşanlardan olmayışı; "
 "A3 'innenî hedânî rabbî ilâ sırâtin mustaqîmin dînen qiyemen millete ibrâhîme hanîfâ, ve mâ kâne mine'l-muşrikîn' (söz içi, 2-16. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (16. kelime, ayet içi); şahıs geçişi 3 → 1 (ayetler arası); edim geçişi şart → emir (ayetler arası).",
)

D[162] = ("◇ 'qul inne salâtî ve nusukî ve mahyâye ve memâtî lillâhi rabbi'l-'âlemîn' — "
 "IMPV 2MS I. bab + 'inne' + 'salât' + 1S + 've' + 'nusuk' + 1S + 've' + 'mahyâ' + 1S + 've' + 'memât' + 1S + 'li' + lafız + 'rabb' + belirli çoğul ''âlem' "
 "(ölçüm edim emir, kip IMPV 1; 1S 4 · 2MS 1; bab I. bab ×1). "
 "Allah lafzı 7. sırada (ölçüm allah z=1,69); Rab 8. sırada (ölçüm rab z=2,05); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=9 (n z=-0,36); ölçüm '{{2|fâsıla ٱلعلمين → ن, N sınıfı}}' — satır aynen (6:161 ن → 6:162 ن); "
 "ölçüm '{{2|harf 38 → harf3 38, isaret 0}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm IMPV 1: 'qul' (1. kelime); 've nusukî' (4.), 've mahyâye' (5.) ve 've memâtî' (6.) kelimelerindeki 've' CONJ; 'inne' (2.) ACC (okuma). "
 + T[162] + " (okuma). "
 + cumle(say('say 6:162 7-9', "lillâhi rabbi'l-'âlemîn", True), say('dizi 6 162 7 9', "allâh rabb 'âlem")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: 'allâh rabb 'âlem' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'mahyâye' / 'memâtî' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 —; B4 'mahyâye' (5. kelime), 'memâtî' (6. kelime).",
 "◈D — D1 IMPV + 'inne' + izafet + 've' + izafet + 've' + izafet + 've' + izafet + 'li' + lafız + izafet; "
 "D2 emir; IMPV ('qul' 1. kelime); D3 —; D4 1S 4 · 2MS 1, sahset ['1', '2'], iltifât 0.",
 "◈A — A1 " + T[162] + "; aktör yok (ölçüm); A2 namazın, kurbanın, hayatın ve ölümün âlemlerin Rabbi Allah'a ait oluşunun söylenmesi; "
 "A3 'inne salâtî ve nusukî ve mahyâye ve memâtî lillâhi rabbi'l-'âlemîn' (söz içi, 2-9. kelime; söz ayet sonunda kapanmıyor); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); şahıs geçişi yok (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[163] = ("◇ 'lâ şerîke leh, ve bi-zâlike umirtu ve ene evvelu'l-muslimîn' — "
 "'lâ' + 'şerîk' + 'li' + 3MS + 've' + 'bi' + 'zâ' + PERF 1S I. bab edilgen + 've' + 'ene' + 'evvel' + belirli çoğul etken ortaç 'muslim' "
 "(ölçüm edim haber, kip NEG 1; 1S 3 · 3MS 1; bab I. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür EVET ton denge' — ölçüm 'esmâ yok' ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); esma_el kaydı 'degil' — 'evvelu'l-muslimîn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); ölçüm '{{3|aktör: adlı مُسْلِم 8\\. sırada \\(cins, rol mecrur\\)}}' — satır aynen; aktör adlı 'l-muslimîn' 8. sırada — cins adı (okuma). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=8 (n z=-0,47); ölçüm '{{3|EDİLGEN 1/1 fiil, pas z=5,38}}' — satır aynen; ölçüm '{{3|fâsıla ٱلمسلمين → ن, N sınıfı}}' — satır aynen (6:162 ن → 6:163 ن); "
 "ölçüm '{{3|simetri \\[3, 1, 4, 1\\]}}' — satır aynen; ölçüm '{{3|harf 35 → harf3 32, isaret 3}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 1: 'lâ' (1. kelime); 've bi-zâlike' (4.) ve 've ene' (6.) kelimelerindeki 've' REM (okuma). "
 + T[163] + " (okuma). "
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'lâ' + 'şerîk' + 'li' + 've' + 'bi' + 'zâ' + PERF + 've' + 'ene' + izafet; "
 "D2 haber; NEG ('lâ' 1. kelime); D3 —; D4 1S 3 · 3MS 1, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[163] + "; aktör adlı 'l-muslimîn' (8. kelime; ölçüm rol mecrur); A2 ortağın yokluğu; bununla emredilme; teslim olanların öncüsü oluş; "
 "A3 söz sürüyor (6:162 2. kelimeden; 1-8. kelime); "
 "A4 " + BOLUM + "; söz kapanır (8. kelime); şahıs geçişi yok (ayetler arası); edim geçişi emir → haber (ayetler arası).",
)

D[164] = ("◇ 'qul e-ğayra'llâhi ebğî rabben ve huve rabbu kulli şey', ve lâ teksibu kullu nefsin illâ 'aleyhâ, ve lâ teziru vâziretun vizra uxrâ, summe ilâ rabbikum merci'ukum fe-yunebbi'ukum bimâ kuntum fîhi taxtelifûn' — "
 "IMPV 2MS I. bab + 'e' + 'ğayr' + lafız + IMPF 1S I. bab + nekre 'rabb' + 've' + 'huve' + 'rabb' + 'kull' + nekre 'şey'' + 've' + 'lâ' + IMPF 3FS I. bab + 'kull' + nekre 'nefs' + 'illâ' + ''alâ' + 3FS + 've' + 'lâ' + IMPF 3FS I. bab + nekre etken ortaç 'vâzire' + 'vizr' + 'âxar' + "
 "'summe' + 'ilâ' + 'rabb' + 2MP + 'merci'' + 2MP + 'fe' + IMPF 3MS II. bab + 2MP + 'bi' + 'mâ' + PERF 2MP I. bab + 'fî' + 3MS + IMPF 2MP VIII. bab "
 "(ölçüm edim soru, emir, kip IMPV 1 · INTG 1 · NEG 2; 1S 1 · 2MP 7 · 2MS 1 · 3FS 3 · 3MS 3; bab I. bab ×5 · II. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 3. sırada (ölçüm allah z=0,16); Rab 5., 7. ve 23. sırada (ölçüm rab z=1,88); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=29 (n z=1,76); ölçüm '{{4|fâsıla تختلفون → ن, N sınıfı}}' — satır aynen (6:163 ن → 6:164 ن); "
 "ölçüm '{{4|simetri \\[3, 6, 10, 1\\]}}' — satır aynen; ölçüm '{{4|harf 110 → harf3 104, isaret 6}}' — satır aynen; ölçüm '{{4|dış düğüm 6}}' — satır aynen; ölçüm '{{4|İÇ düğüm 2}}' — satır aynen. "
 "Ölçüm IMPV 1: 'qul' (1. kelime); INTG 1: 'e-ğayra' (2. kelime); NEG 2: 'lâ' (10.) ve 'lâ' (16. kelime); ölçüm biçim ISTISNA ('illâ' 14. kelime); "
 "'ve huve' (6.) kelimesindeki 've' REM; 've lâ' (10.) ve 've lâ' (16.) kelimelerindeki 've' CONJ; 'summe' (21.) CONJ; 'fe-yunebbi'ukum' (25.) kelimesindeki 'fe' REM (okuma). "
 "Kök ikilemesi (ölçüm) ربب ×3 ('rabben' 5. / 'rabbu' 7. / 'rabbikum' 23. kelime), كلل ×2 ('kulli' 8. / 'kullu' 12. kelime), وزر ×3 ('teziru' 17. / 'vâziretun' 18. / 'vizra' 19. kelime) (okuma). "
 + T[164] + " (okuma). "
 + cumle(say('say 6:164 1-3', "qul e-ğayra'llâhi", True), say('dizi 6 164 1 3', "qâle ğayr allâh")) + ' '
 + cumle(say('say 6:164 7-9', "rabbu kulli şey'", True), say('dizi 6 164 7 9', "rabb kull şey'")) + ' '
 + cumle(say('say 6:164 11-13', "teksibu kullu nefsin", True), say('dizi 6 164 11 13', "kesebe kull nefs")) + ' '
 + cumle(say('say 6:164 21-27', "summe ilâ rabbikum merci'ukum fe-yunebbi'ukum bimâ kuntum", True), say('dizi 6 164 21 27', "summe ilâ rabb merci' nebbe'e mâ kâne")) + ' '
 + cumle(say('say 6:164 21-23', "summe ilâ rabbikum", True), say('dizi 6 164 21 23', "summe ilâ rabb")) + ' '
 + cumle(say('say 6:164 25-27', "fe-yunebbi'ukum bimâ kuntum", True), say('dizi 6 164 25 27', "nebbe'e mâ kâne")) + ' '
 + cumle(say('say 6:164 25-29', "fe-yunebbi'ukum bimâ kuntum fîhi taxtelifûn", True), say('dizi 6 164 25 29', "nebbe'e mâ kâne fî ixtelefe")) + ' ' +
 "Ölçüm xref 5:48 (emsal olarak basıldı), 6:14 (basılmış), 6:108 (basılmış), 13:42 (emsal olarak basıldı), 39:7 (basılmış), okunmuş 2 ayet ve okunmamış 1 ayet. "
 "Ölçüm nakarat3 kalıpları: 'summe ilâ rabb merci' nebbe'e mâ kâne' süzgeç GEÇER, 'nebbe'e mâ kâne' süzgeç GEÇER, 'summe ilâ rabb' süzgeç GEÇER, 'qâle ğayr allâh' süzgeç GEÇMEZ, 'rabb kull şey'' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'e' + izafet + IMPF + nekre + 've' + 'huve' + 'rabb' + 'kull' + nekre + 've' + 'lâ' + IMPF + 'kull' + nekre + 'illâ' + ''alâ' + 've' + 'lâ' + IMPF + nekre + izafet + 'summe' + 'ilâ' + izafet + izafet + 'fe' + IMPF + 'bi' + 'mâ' + PERF + 'fî' + IMPF; "
 "D2 soru, emir; IMPV ('qul' 1. kelime), INTG ('e-ğayra' 2. kelime), NEG ('lâ' 10. kelime, 'lâ' 16. kelime); D3 5:48 eşi, 13:42 eşi, ربب ×3, كلل ×2, وزر ×3; D4 1S 1 · 2MP 7 · 2MS 1 · 3FS 3 · 3MS 3, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[164] + "; aktör yok (ölçüm); A2 Allah'tan başka Rab aramanın sorulması; her canın kazancının kendi aleyhine oluşu; yük taşıyanın başkasının yükünü taşımayışı; dönüşün Rabbe oluşu ve ayrılığa düşülen şeyin haber verilmesi; "
 "A3 'e-ğayra'llâhi ebğî rabben ve huve rabbu kulli şey', ve lâ teksibu kullu nefsin illâ 'aleyhâ, ve lâ teziru vâziretun vizra uxrâ, summe ilâ rabbikum merci'ukum fe-yunebbi'ukum bimâ kuntum fîhi taxtelifûn' (söz içi, 2-29. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (29. kelime, ayet içi); muhatap geçişi 2MS → 2MP (ayet içi, 'qul' / 'rabbikum'); şahıs geçişi 1 → 2 (ayetler arası); edim geçişi haber → soru, emir (ayetler arası).",
)

D[165] = ("◇ 've huve'llezî ce'alekum xalâ'ife'l-ardi ve refe'a ba'dakum fevqa ba'din deracâtin li-yebluvekum fî mâ âtâkum, inne rabbeke serî'u'l-'iqâbi ve innehû le-ğafûrun rahîm' — "
 "'ve' + 'huve' + 'ellezî' + PERF 3MS I. bab + 2MP + çoğul 'xalîfe' + belirli 'ard' + 've' + PERF 3MS I. bab + 'ba'd' + 2MP + 'fevq' + nekre 'ba'd' + nekre çoğul 'derece' + 'li' + IMPF 3MS I. bab + 2MP + 'fî' + 'mâ' + PERF 3MS IV. bab + 2MP + "
 "'inne' + 'rabb' + 2MS + 'serî'' + belirli ''iqâb' + 've' + 'inne' + 3MS + 'le' + nekre 'ğafûr' + nekre 'rahîm' "
 "(ölçüm edim haber, kip EMPH 1; 2MP 4 · 2MS 1 · 3MS 6; bab I. bab ×3 · IV. bab ×1). "
 "Allah lafzı yok; Rab 16. sırada (ölçüm rab z=0,69); ölçüm '{{5|esmâ غَفُور 20\\. sırada, SON konum, MÜHÜR \\| رَحِيم 21\\. sırada, SON konum, MÜHÜR}}' — satır aynen; esma_kayit çıktısı 'mühür EVET (ÇİFT)' — ölçüm MÜHÜR ile uyuşuyor; "
 "esma_el kaydı 'ilahi' — 've innehû le-ğafûrun rahîm', kural ''inne/enne' haberi → ilahi' (Rab) ve 'rahîm' için kural ''inne/enne' haberi → ilahi' (Rab; morph ADJ ile 'ğafûr'un sıfatı) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=21 (n z=0,91); ölçüm '{{5|fâsıla رحيم → م, N sınıfı}}' — satır aynen (6:164 ن → 6:165 م); "
 "ölçüm '{{5|simetri \\[3, 1, 12, 1\\]}}' — satır aynen; ölçüm '{{5|harf 91 → harf3 85, isaret 6}}' — satır aynen; ölçüm '{{5|dış düğüm 3}}' — satır aynen. "
 "Ölçüm EMPH 1: 'le-ğafûrun' (20. kelime); 've huve' (1.), 've refe'a' (6.) ve 've innehû' (19.) kelimelerindeki 've' CONJ; 'li-yebluvekum' (11.) kelimesindeki 'li' PRP; 'inne' (15.) ve 've innehû' (19.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) بعض ×2 ('ba'dakum' 7. / 'ba'din' 9. kelime) (okuma). "
 + T[165] + " (okuma). "
 + cumle(say('say 6:165 1-3', "ve huve'llezî ce'alekum", True), say('dizi 6 165 1 3', "_ ellezî ce'ale")) + ' '
 + cumle(say('say 6:165 8-10', "fevqa ba'din deracâtin", True), say('dizi 6 165 6 10', "refe'a ba'd fevq ba'd derece")) + ' '
 + cumle(say('say 6:165 11-14', "li-yebluvekum fî mâ âtâkum", True), say('dizi 6 165 11 14', "belev fî mâ âtâ")) + ' '
 + say('say 6:165 12-13', "fî mâ", True) + " (--medde 11 ayet: 'mâ' yazım farkı ile; harekesiz sayım elif / medde yazımına bağlı). " +
 "Ölçüm xref 43:32 (emsal olarak basıldı), okunmuş 1 ayet ve okunmamış 1 ayet. "
 "Ölçüm nakarat3 kalıpları: '_ ellezî ce'ale' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K1 'l-ardi' (5. kelime).",
 "◈B — —",
 "◈D — D1 've' + 'huve' + 'ellezî' + PERF + izafet + 've' + PERF + izafet + 'fevq' + nekre + nekre + 'li' + IMPF + 'fî' + 'mâ' + PERF + 'inne' + izafet + izafet + 've' + 'inne' + 'le' + nekre + nekre; "
 "D2 haber; EMPH ('le-ğafûrun' 20. kelime); D3 5:48 eşi, 43:32 eşi, بعض ×2; D4 2MP 4 · 2MS 1 · 3MS 6, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[165] + "; aktör yok (ölçüm); A2 muhatapların yeryüzünün halifeleri kılınması; derecelerle yükseltme ve verilende sınama; Rabbin cezasının çabukluğu, bağışlaması ve merhameti; "
 "A3 —; söz kapanışı gerekçesi: 6:164 sözü 29. kelimede kapanır, 've huve'llezî' (1. kelime) morph CONJ ile söz dışı anlatı, muhatap 2MS 'rabbeke' (16. kelime) (okuma); "
 "A4 " + BOLUM + "; muhatap geçişi 2MP → 2MS (ayet içi, 'ce'alekum' / 'rabbeke'); şahıs geçişi 2 → 3 (ayetler arası); edim geçişi soru, emir → haber (ayetler arası); bölüm kapanışı; sûre kapanışı.",
)
