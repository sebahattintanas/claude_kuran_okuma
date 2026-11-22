# sûre 6 blok 28 (6:118-121) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b28/say2.txt'
os.environ['OLC'] = '/home/claude/b28/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Hakem olarak Allah; üzerine Allah'ın adı anılan' bölümünde"
N1 = "ekele mimmâ zekere ism allâh 'alâ"; N2 = "zekere ism allâh 'alâ"; N3 = "zekere ism allâh"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 118: "O'nun âyetlerine inananlarsanız, üzerine Allah'ın adı anılandan yiyin.",
 119: "Size ne oluyor ki üzerine Allah'ın adı anılandan yemiyorsunuz? Oysa O, ona zorda kaldığınız şey dışında, size haram kıldığı şeyi sizin için ayrıntılı açıklamıştır. Çokları bilgisizce hevesleriyle elbette saptırıyorlar. Rabbin, haddi aşanları en iyi bilendir.",
 120: "Günahın açığını da gizlisini de bırakın. Günah kazananlar, işlemekte olduklarıyla cezalandırılacaklardır.",
 121: "Üzerine Allah'ın adı anılmayandan yemeyin; o elbette bir fısktır. Şeytanlar sizinle tartışsınlar diye dostlarına elbette fısıldarlar. Eğer onlara itaat ederseniz siz elbette ortak koşanlarsınız.",
}

T = {}
T[118] = ("muhatap 2MP (adsız; 'fe-kulû', 'kuntum' — 1. ve 8. kelime); 'zukira' 3MS (fiil uyumu; 3. kelime — edilgen; naib-i faili 'smu' (4. kelime)); "
          "''aleyhi' 3MS eki (adsız; gönderge 'mimmâ' 2. kelime, 6. kelime); 'bi-âyâtihî' 3MS eki (adsız; gönderge 'llâhi' 5. kelime, 9. kelime)")
T[119] = ("muhatap 2MP (adsız; 'lekum', 'te'kulû', 'lekum', ''aleykum' — 2., 4., 12. ve 15. kelime); muhatap 2MP (adsız; 'dturirtum' — 18. kelime; edilgen; naib-i faili muhatap zamiri); 'zukira' 3MS (fiil uyumu; 6. kelime — edilgen; naib-i faili 'smu' (7. kelime)); "
          "''aleyhi' 3MS eki (adsız; gönderge 'mimmâ' 5. kelime, 9. kelime); 'fassale', 'harrame' 3MS (adsız; gönderge 'llâhi' 8. kelime — 11. ve 14. kelime); 'ileyhi' 3MS eki (adsız; gönderge 'mâ' 13. kelime, 19. kelime); "
          "'le-yudillûne', 'bi-ehvâ'ihim' 3MP (adsız; tartışmalı; gönderge 'kesîran' 21. kelime — 22. ve 23. kelime); muhatap 2MS (adsız; 'rabbeke' — 27. kelime); 'huve' 3MS (adsız; gönderge 'rabbeke' 27. kelime, 28. kelime)")
T[120] = ("muhatap 2MP (adsız; 've zerû' — 1. kelime); 've bâtinahû' 3MS eki (adsız; gönderge 'l-ismi' 3. kelime, 4. kelime); "
          "'yeksibûne', 'kânû', 'yaqterifûn' 3MP (adsız; gönderge 'llezîne' 6. kelime — 7., 11. ve 12. kelime); 'se-yuczevne' 3MP (adsız; gönderge 'llezîne' 6. kelime, 9. kelime — edilgen; naib-i faili zamir)")
T[121] = ("muhatap 2MP (adsız; 'te'kulû', 'li-yucâdilûkum', 'eta'tumûhum', 'innekum' — 2., 16., 18. ve 19. kelime); 'yuzkeri' 3MS (fiil uyumu; 5. kelime — edilgen; naib-i faili 'smu' (6. kelime)); "
          "''aleyhi' 3MS eki (adsız; gönderge 'mimmâ' 3. kelime, 8. kelime); 've innehû' 3MS eki (adsız; tartışmalı; gönderge 'mimmâ' 3. kelime, 9. kelime); "
          "'le-yûhûne', 'li-yucâdilûkum' 3MP (adsız; gönderge 'ş-şeyâtîne' 12. kelime — 13. ve 16. kelime); 'evliyâ'ihim' 3MP eki (adsız; gönderge 'ş-şeyâtîne' 12. kelime, 15. kelime); "
          "'eta'tumûhum' 3MP eki (adsız; tartışmalı; gönderge 'ş-şeyâtîne' 12. kelime, 18. kelime)")

D = {}
D[118] = ("◇ 'fe-kulû mimmâ zukira'smu'llâhi 'aleyhi in kuntum bi-âyâtihî mu'minîn' — "
 "'fe' + IMPV 2MP I. bab + 2MP + 'min' + 'mâ' + PERF 3MS I. bab edilgen + 'ism' + lafız + ''alâ' + 3MS + 'in' + PERF 2MP I. bab + 2MP + 'bi' + çoğul 'âye' + 3MS + çoğul etken ortaç 'mu'min' "
 "(ölçüm edim emir, şart, kip COND 1 · IMPV 1; 2MP 4 · 3MS 3; bab I. bab ×3). "
 "Allah lafzı 5. sırada (ölçüm allah z=1,47); Rab yok; ölçüm '{{1|esmâ مُؤْمِن 10\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor, araç tanımı farkı (muhur_el hayır, ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'in kuntum bi-âyâtihî mu'minîn', kural 'çoğul insan göndergeli → degil' (insan topluluğu) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=10 (n z=-0,26); ölçüm '{{1|EDİLGEN 1/3 fiil, pas z=1,57}}' — satır aynen; ölçüm '{{1|fâsıla مؤمنين → ن, N sınıfı}}' — satır aynen (6:117 ن → 6:118 ن); "
 "ölçüm '{{1|harf 42 → harf3 40, isaret 2}}' — satır aynen; ölçüm '{{1|dış düğüm 6}}' — satır aynen; ölçüm '{{1|İÇ düğüm 3}}' — satır aynen. "
 "Ölçüm IMPV 1: 'fe-kulû' (1. kelime); COND 1: 'in' (7. kelime); 'fe-kulû' (1.) kelimesindeki 'fe' REM (okuma). "
 + T[118] + " (okuma). "
 + cumle(say('say 6:118 1-6', "fe-kulû mimmâ zukira'smu'llâhi 'aleyhi", True), say('dizi 6 118 1 6', "ekele mimmâ zekere ism allâh 'alâ")) + ' '
 + cumle(say('say 6:118 3-6', "zukira'smu'llâhi 'aleyhi", True), say('dizi 6 118 3 6', "zekere ism allâh 'alâ")) + ' '
 + cumle(say('say 6:118 3-5', "zukira'smu'llâh", True), say('dizi 6 118 3 5', "zekere ism allâh")) + ' '
 + cumle(say('say 6:118 7-8', 'in kuntum', True)) + ' ' +
 "Ölçüm xref 6:119 (basılmış), 6:121 (basılmış) ve okunmuş 6 ayet ve okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıpları: '" + N1 + "' süzgeç GEÇER, '" + N2 + "' süzgeç GEÇER, '" + N3 + "' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'fe' + IMPV + 'min' + 'mâ' + PERF + 'ism' + lafız + ''alâ' + 'in' + PERF + 'bi' + izafet + 'mu'min'; "
 "D2 emir, şart; COND ('in' 7. kelime), IMPV ('fe-kulû' 1. kelime); D3 ayetler arası kalıp ('smu'llâhi 'aleyh'); D4 2MP 4 · 3MS 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[118] + "; aktör yok (ölçüm); A2 âyetlere inananlara üzerine Allah'ın adı anılandan yeme emri; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 2 (ayetler arası); edim geçişi haber → emir, şart (ayetler arası); şart → cevap (ayet içi; COND 'in' 7. kelime: 'in kuntum' / 'fe-kulû' (1. kelime)).",
)

D[119] = ("◇ 've mâ lekum ellâ te'kulû mimmâ zukira'smu'llâhi 'aleyhi ve qad fassale lekum mâ harrame 'aleykum illâ ma'dturirtum ileyhi ve inne kesîran le-yudillûne bi-ehvâ'ihim bi-ğayri 'ilmin inne rabbeke huve a'lemu bi'l-mu'tedîn' — "
 "'ve' + 'mâ' + 'li' + 2MP + 'en' + 'lâ' + IMPF 2MP I. bab + 2MP + 'min' + 'mâ' + PERF 3MS I. bab edilgen + 'ism' + lafız + ''alâ' + 3MS + 've' + 'qad' + PERF 3MS II. bab + 'li' + 2MP + 'mâ' + PERF 3MS II. bab + ''alâ' + 2MP + "
 "'illâ' + 'mâ' + PERF 2MP VIII. bab edilgen + 2MP + 'ilâ' + 3MS + 've' + 'inne' + nekre 'kesîr' + 'le' + IMPF 3MP IV. bab + 3MP + 'bi' + çoğul 'hevâ' + 3MP + 'bi' + 'ğayr' + nekre ''ilm' + "
 "'inne' + 'rabb' + 2MS + 'huve' + 'a'lem' + 'bi' + belirli çoğul etken ortaç 'mu'tedî' "
 "(ölçüm edim soru, kip CERT 1 · EMPH 1 · INTG 1 · NEG 1, biçim ISTISNA; 2MP 7 · 2MS 1 · 3MP 3 · 3MS 6; bab I. bab ×2 · II. bab ×2 · IV. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 8. sırada (ölçüm allah z=0,14); Rab 27. sırada (ölçüm rab z=0,39); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=30 (n z=1,87); ölçüm '{{2|EDİLGEN 2/6 fiil, pas z=1,57}}' — satır aynen; ölçüm '{{2|sayı işareti كَثِير}}' — satır aynen; "
 "ölçüm '{{2|fâsıla بٱلمعتدين → ن, N sınıfı}}' — satır aynen (6:118 ن → 6:119 ن); ölçüm '{{2|simetri \\[6, 1, 15, 2\\]}}' — satır aynen; ölçüm '{{2|harf 120 → harf3 116, isaret 4}}' — satır aynen; "
 "ölçüm '{{2|dış düğüm 7}}' — satır aynen; ölçüm '{{2|İÇ düğüm 3}}' — satır aynen. "
 "Ölçüm INTG 1: 'mâ' (1. kelime); NEG 1: 'ellâ' (3. kelime; 'lâ'); CERT 1: 'qad' (10. kelime); EMPH 1: 'le-yudillûne' (22. kelime); biçim ISTISNA ('illâ' 16. kelime); "
 "'ve mâ' (1.) kelimesindeki 've' REM; 've qad' (10.) ve 've inne' (20.) kelimelerindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) علم ×2 (''ilmin' 25. / 'a'lemu' 29. kelime) (okuma). "
 + T[119] + " (okuma). "
 + cumle(say('say 6:119 4-9', "te'kulû mimmâ zukira'smu'llâhi 'aleyhi", True), say('dizi 6 119 4 9', "ekele mimmâ zekere ism allâh 'alâ")) + ' '
 + cumle(say('say 6:119 6-9', "zukira'smu'llâhi 'aleyhi", True), say('dizi 6 119 6 9', "zekere ism allâh 'alâ")) + ' '
 + cumle(say('say 6:119 6-8', "zukira'smu'llâh", True), say('dizi 6 119 6 8', "zekere ism allâh")) + ' '
 + cumle(say('say 6:119 26-29', "inne rabbeke huve a'lemu", True), say('dizi 6 119 26 29', "inne rabb _ a'lem")) + ' '
 + cumle(say('say 6:119 24-26', "bi-ğayri 'ilmin inne", True), say('dizi 6 119 24 26', "ğayr 'ilm inne")) + ' '
 + cumle(say('dizi 6 119 25 27', "'ilm inne rabb", True)) + ' ' + cumle(say('say 6:119 1-2', 've mâ lekum', True)) + ' ' + cumle(say('say 6:119 16-17', 'illâ mâ', True)) + ' ' +
 "Ölçüm xref 53:30 (emsal olarak basıldı), 6:118 (basılmış), 6:121 (basılmış) ve okunmuş 6 ayet ve okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıpları: '" + N1 + "' süzgeç GEÇER, '" + N2 + "' süzgeç GEÇER, 'inne rabb _ a'lem' süzgeç GEÇER, '" + N3 + "' süzgeç GEÇER, 'ğayr 'ilm inne' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'mâ' + 'li' + 'en' + 'lâ' + IMPF + 'min' + 'mâ' + PERF + 'ism' + lafız + ''alâ' + 've' + 'qad' + PERF + 'li' + 'mâ' + PERF + ''alâ' + 'illâ' + 'mâ' + PERF + 'ilâ' + "
 "'ve' + 'inne' + nekre + 'le' + IMPF + 'bi' + izafet + 'bi' + 'ğayr' + nekre + 'inne' + izafet + 'huve' + 'a'lem' + 'bi' + belirli; "
 "D2 soru; CERT ('qad' 10. kelime), EMPH ('le-yudillûne' 22. kelime), INTG ('mâ' 1. kelime), NEG ('ellâ' 3. kelime); D3 علم ×2; 53:30 eşi; ayetler arası kalıp ('smu'llâhi 'aleyh'); "
 "D4 2MP 7 · 2MS 1 · 3MP 3 · 3MS 6, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[119] + "; aktör yok (ölçüm); A2 üzerine Allah'ın adı anılandan yememe sorusu; zorda kalma dışında haram kılınanın açıklanmış oluşu; çoklarının bilgisizce hevesleriyle saptırması; Rabbin haddi aşanları en iyi bilmesi; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); şahıs sayısında beraberlik (2. şahıs 8 · 3. şahıs 9 — ölçüm baskın 2); edim geçişi emir, şart → soru (ayetler arası).",
)

D[120] = ("◇ 've zerû zâhira'l-ismi ve bâtinahû inne'llezîne yeksibûne'l-isme se-yuczevne bi-mâ kânû yaqterifûn' — "
 "'ve' + IMPV 2MP I. bab + 2MP + etken ortaç 'zâhir' + belirli 'ism' + 've' + etken ortaç 'bâtin' + 3MS + 'inne' + 'ellezîne' + IMPF 3MP I. bab + 3MP + belirli 'ism' + "
 "'se' + IMPF 3MP I. bab edilgen + 3MP + 'bi' + 'mâ' + PERF 3MP I. bab + 3MP + IMPF 3MP VIII. bab + 3MP "
 "(ölçüm edim emir, kip FUT 1 · IMPV 1; 2MP 2 · 3MP 8 · 3MS 1; bab I. bab ×4 · VIII. bab ×1). "
 "Allah lafzı yok; Rab yok; ölçüm '{{3|esmâ ظاهِر 2\\. sırada, ORTA konum, MÜHÜRSÜZ \\| باطِن 4\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' — ölçüm MÜHÜRSÜZ ile uyuşmuyor, araç tanımı farkı (muhur_el hayır, ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 've zerû zâhira'l-ismi ve bâtinahû', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=12 (n z=-0,04); ölçüm '{{3|EDİLGEN 1/5 fiil, pas z=0,81}}' — satır aynen; ölçüm '{{3|fâsıla يقترفون → ن, N sınıfı}}' — satır aynen (6:119 ن → 6:120 ن); "
 "ölçüm '{{3|simetri \\[3, 3, 8, 1\\]}}' — satır aynen; ölçüm '{{3|harf 62 → harf3 58, isaret 4}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm IMPV 1: 've zerû' (1. kelime); FUT 1: 'se-yuczevne' (9. kelime); 've zerû' (1.) kelimesindeki 've' REM; 've bâtinahû' (4.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) أثم ×2 ('l-ismi' 3. / 'l-isme' 8. kelime) (okuma). "
 + T[120] + " (okuma). "
 + cumle(say('say 6:120 9-11', 'se-yuczevne bi-mâ kânû', True), say('dizi 6 120 9 11', 'cezâ mâ kâne')) + ' '
 + cumle(say('say 6:120 10-11', 'bi-mâ kânû', True)) + ' ' + cumle(say('say 6:120 5-6', "inne'llezîne", True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı: 'cezâ bi-mâ kâne' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'zâhira' / 've bâtinahû' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + IMPV + 'zâhir' + belirli + 've' + izafet + 'inne' + 'ellezîne' + IMPF + belirli + 'se' + IMPF + 'bi' + 'mâ' + PERF + IMPF; "
 "D2 emir; FUT ('se-yuczevne' 9. kelime), IMPV ('ve zerû' 1. kelime); D3 أثم ×2; D4 2MP 2 · 3MP 8 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[120] + "; aktör yok (ölçüm); A2 günahın açığını ve gizlisini bırakma emri; günah kazananların işlediklerinin karşılığını görmesi; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi soru → emir (ayetler arası).",
)

D[121] = ("◇ 've lâ te'kulû mimmâ lem yuzkeri'smu'llâhi 'aleyhi ve innehû le-fisqun ve inne'ş-şeyâtîne le-yûhûne ilâ evliyâ'ihim li-yucâdilûkum ve in eta'tumûhum innekum le-muşrikûn' — "
 "'ve' + 'lâ' + IMPF 2MP I. bab + 2MP + 'min' + 'mâ' + 'lem' + IMPF 3MS I. bab edilgen + 'ism' + lafız + ''alâ' + 3MS + 've' + 'inne' + 3MS + 'le' + nekre 'fisq' + "
 "'ve' + 'inne' + belirli çoğul 'şeytân' + 'le' + IMPF 3MP IV. bab + 3MP + 'ilâ' + çoğul 'veliyy' + 3MP + 'li' + IMPF 3MP III. bab + 3MP + 2MP + "
 "'ve' + 'in' + PERF 2MP IV. bab + 2MP + 3MP + 'inne' + 2MP + 'le' + çoğul etken ortaç 'muşrik' "
 "(ölçüm edim yasak, şart, kip COND 1 · EMPH 3 · NEG 1 · PRO 1, biçim NEHY; 2MP 6 · 3MP 6 · 3MS 3; bab I. bab ×2 · III. bab ×1 · IV. bab ×2). "
 "Allah lafzı 7. sırada (ölçüm allah z=0,47); Rab yok; ölçüm '{{4|esmâ وَلِيّ 15\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor, araç tanımı farkı (muhur_el hayır, ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 'ilâ evliyâ'ihim', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); ölçüm '{{4|aktör: adlı شَيْطان 12\\. sırada \\(gayb, rol meful\\)}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=20 (n z=0,81); ölçüm '{{4|EDİLGEN 1/5 fiil, pas z=0,81}}' — satır aynen; ölçüm '{{4|fâsıla لمشركون → ن, N sınıfı}}' — satır aynen (6:120 ن → 6:121 ن); "
 "ölçüm '{{4|simetri \\[3, 1, 9, 1\\]}}' — satır aynen; ölçüm '{{4|harf 99 → harf3 94, isaret 5}}' — satır aynen; ölçüm '{{4|dış düğüm 5}}' — satır aynen; ölçüm '{{4|İÇ düğüm 3}}' — satır aynen. "
 "Ölçüm PRO 1: 'lâ' (1. kelime), biçim NEHY; NEG 1: 'lem' (4. kelime); EMPH 3: 'le-fisqun' (10.), 'le-yûhûne' (13.) ve 'le-muşrikûn' (20. kelime); COND 1: 'in' (17. kelime); "
 "'ve lâ' (1.), 've innehû' (9.) ve 've in' (17.) kelimelerindeki 've' REM; 've inne' (11.) kelimesindeki 've' CONJ; 'li-yucâdilûkum' (16.) PRP (okuma). "
 + T[121] + " (okuma). "
 + cumle(say('say 6:121 5-8', "yuzkeri'smu'llâhi 'aleyhi", True), say('dizi 6 121 5 8', "zekere ism allâh 'alâ")) + ' '
 + cumle(say('say 6:121 5-7', "yuzkeri'smu'llâh", True), say('dizi 6 121 5 7', "zekere ism allâh")) + ' '
 + cumle(say('say 6:121 2-3', "te'kulû mimmâ", True)) + ' ' +
 "Ölçüm xref 6:118 (basılmış), 6:119 (basılmış) ve okunmuş 5 ayet ve okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıpları: '" + N2 + "' süzgeç GEÇER, '" + N3 + "' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'lâ' + IMPF + 'min' + 'mâ' + 'lem' + IMPF + 'ism' + lafız + ''alâ' + 've' + 'inne' + 'le' + nekre + 've' + 'inne' + belirli + 'le' + IMPF + 'ilâ' + izafet + 'li' + IMPF + "
 "'ve' + 'in' + PERF + 'inne' + 'le' + 'muşrik'; "
 "D2 yasak, şart; COND ('in' 17. kelime), EMPH ('le-fisqun' 10. kelime, 'le-yûhûne' 13. kelime, 'le-muşrikûn' 20. kelime), NEG ('lem' 4. kelime), PRO ('lâ' 1. kelime); "
 "D3 ayetler arası kalıp ('smu'llâhi 'aleyh'); D4 2MP 6 · 3MP 6 · 3MS 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[121] + "; aktör adlı 'ş-şeyâtîne' (12. kelime; ölçüm rol meful — 'inne' ismi); A2 üzerine Allah'ın adı anılmayandan yeme yasağı; onun fısk oluşu; şeytanların dostlarına fısıldaması; itaat edenlerin ortak koşanlar oluşu; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 2 (ayetler arası); şahıs sayısında beraberlik (2. şahıs 6 · 3. şahıs 9 — ölçüm baskın 2); edim geçişi emir → yasak, şart (ayetler arası); şart → cevap (ayet içi; COND 'in' 17. kelime: 've in eta'tumûhum' / 'innekum' (19. kelime)); bölüm kapanışı.",
)
out = ['# ── blok 6:118-121 (2026-11-22) ──', 'MEAL28 = {']
for n in range(118, 122):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M28 = {']
for n in range(118, 122):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL28); M.update(M28)']
open('/home/claude/yamalar/metin_6_118_121.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
