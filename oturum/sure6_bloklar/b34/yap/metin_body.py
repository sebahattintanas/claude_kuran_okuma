# sûre 6 blok 34 (6:142-144) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b34/say2.txt'
os.environ['OLC'] = '/home/claude/b34/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Ekinlerde ve hayvanlarda pay; sekiz eş' bölümünde"
N1 = "isneyn qâle zeker harrame em unseyeyn emmâ iştemelet 'alâ erhâm unseyeyn"; N2 = "in kâne sâdiq"; N3 = "ezlem mimmen iftarâ 'alâ allâh kezib"; N4 = "ğayr 'ilm inne"; N5 = "fe-men ezlem mimmen"
E1 = "lâ ittebe xutuve şeytân inne _ 'aduvv mubîn"; E2 = "lâ ittebe xutuve şeytân"
SOZ = "qul e-'z-zekereyni harrame emi'l-unseyeyni emmâ'ştemelet 'aleyhi erhâmu'l-unseyeyn"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 142: "Hayvanlardan yük taşıyanı ve döşeklik olanı da O inşâ etti. Allah'ın size rızık olarak verdiğinden yiyin; şeytanın adımlarına uymayın. Şüphesiz o sizin için apaçık bir düşmandır.",
 143: "Sekiz eş: koyundan iki, keçiden iki. De ki: İki erkeği mi haram kıldı yoksa iki dişiyi mi, yoksa iki dişinin rahimlerinin içerdiğini mi? Doğru söyleyenlerseniz bana bir bilgiyle haber verin.",
 144: "Deveden iki, sığırdan iki. De ki: İki erkeği mi haram kıldı yoksa iki dişiyi mi, yoksa iki dişinin rahimlerinin içerdiğini mi? Yoksa Allah size bunu tavsiye ettiğinde şahitler miydiniz? Allah'a, insanları bilgisizce saptırmak için yalan uydurandan daha zalim kim vardır? Şüphesiz Allah zalimler kavmini doğru yola iletmez.",
}

T = {}
T[142] = ("muhatap 2MP (adsız; 'kulû', 'razaqakumu', 'tettebi'û', 'lekum' — 5., 7., 10. ve 14. kelime); 'razaqakumu' 3MS (fiil uyumu; 7. kelime — fail 8. kelime); "
          "'innehû' 3MS eki (adsız; gönderge 'ş-şeytân' 12. kelime, 13. kelime)")
T[143] = ("muhatap 2MS (adsız; 'qul' — 9. kelime); 'harrame' 3MS (adsız; söz içi; tartışmalı; gönderge 6:142 8. kelime, 11. kelime); 'ştemelet' 3FS (fiil uyumu; söz içi; 15. kelime — fail 17. kelime); "
          "''aleyhi' 3MS eki (adsız; söz içi; gönderge 'emmâ' 14. kelime, 16. kelime); muhatap 2MP (adsız; söz içi; 'nebbi'ûnî', 'kuntum' — 19. ve 22. kelime); konuşan 1S (adsız; söz içi; 'nebbi'ûnî' — 19. kelime)")
T[144] = ("muhatap 2MS (adsız; 'qul' — 7. kelime); 'harrame' 3MS (adsız; söz içi; tartışmalı; gönderge 6:142 8. kelime, 9. kelime); 'ştemelet' 3FS (fiil uyumu; söz içi; 13. kelime — fail 15. kelime); "
          "''aleyhi' 3MS eki (adsız; söz içi; gönderge 'emmâ' 12. kelime, 14. kelime); muhatap 2MP (adsız; söz içi; 'kuntum', 'vassâkumu' — 18. ve 21. kelime); 'vassâkumu' 3MS (fiil uyumu; söz içi; 21. kelime — fail 22. kelime); "
          "'fterâ', 'li-yudille' 3MS (adsız; gönderge 'mimmeni' 26. kelime — 27. ve 31. kelime); 'yehdi' 3MS (adsız; gönderge 'llâhe' 36. kelime, 38. kelime)")

D = {}
D[142] = ("◇ 've mine'l-en'âmi hamûleten ve ferşâ, kulû mimmâ razaqakumu'llâhu ve lâ tettebi'û xutuvâti'ş-şeytân, innehû lekum 'aduvvun mubîn' — "
 "'ve' + 'min' + belirli çoğul 'na'am' + nekre 'hamûle' + 've' + nekre 'ferş' + IMPV 2MP I. bab + 2MP + 'min' + 'mâ' + PERF 3MS I. bab + 2MP + lafız + 've' + 'lâ' + IMPF 2MP VIII. bab + 2MP + çoğul 'xutuve' + belirli 'şeytân' + 'inne' + 3MS + 'li' + 2MP + nekre ''aduvv' + nekre etken ortaç 'mubîn' "
 "(ölçüm edim emir, yasak, kip IMPV 1 · PRO 1; 2MP 6 · 3MS 2; bab I. bab ×2 · VIII. bab ×1). "
 "Allah lafzı 8. sırada (ölçüm allah z=0,72); Rab yok; ölçüm '{{1|esmâ مُبِين 16\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' — ölçüm MÜHÜRSÜZ ile uyuşmuyor, araç tanımı farkı (muhur_el hayır, ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — ''aduvvun mubîn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (düşmanın sıfatı) (okuma); "
 "ölçüm '{{1|aktör: adlı شَيْطان 12\\. sırada \\(gayb, rol mecrur\\)}}' — satır aynen; aktör adlı 'ş-şeytân' 12. sırada — adımlarına uyulmaması istenen (okuma). "
 "Ölçüm 'yıldız yok' — satır aynen; n=16 (n z=0,38); ölçüm '{{1|fâsıla مبين → ن, N sınıfı}}' — satır aynen (6:141 ن → 6:142 ن); "
 "ölçüm '{{1|harf 76 → harf3 67, isaret 9}}' — satır aynen; ölçüm '{{1|dış düğüm 5}}' — satır aynen. "
 "Ölçüm IMPV 1: 'kulû' (5. kelime); PRO 1: 'lâ' (9. kelime); 've mine' (1.), 've ferşâ' (4.) ve 've lâ' (9.) kelimelerindeki 've' CONJ; 'innehû' (13.) ACC (okuma). "
 + T[142] + " (okuma). "
 + cumle(say('say 6:142 6-8', "mimmâ razaqakumu'llâh", True)) + ' '
 + cumle(say('say 6:142 9-16', "ve lâ tettebi'û xutuvâti'ş-şeytân, innehû lekum 'aduvvun mubîn", True), say('dizi 6 142 9 16', "lâ ittebe xutuve şeytân inne _ 'aduvv mubîn")) + ' '
 + cumle(say('say 6:142 10-12', "tettebi'û xutuvâti'ş-şeytân", True), say('dizi 6 142 9 12', 'lâ ittebe xutuve şeytân')) + ' ' +
 "Ölçüm xref 2:168 (emsal olarak basıldı), 2:208 (emsal olarak basıldı), 24:21 (emsal olarak basıldı), 5:88 (basılmış), 16:114 (basılmış). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'l-en'âmi' (2. kelime); B2 'hamûleten' (3. kelime); B3 —; B4 —.",
 "◈D — D1 've' + 'min' + belirli + nekre + 've' + nekre + IMPV + 'min' + 'mâ' + PERF + lafız + 've' + 'lâ' + IMPF + izafet + 'inne' + 'li' + nekre + nekre; "
 "D2 emir, yasak; IMPV ('kulû' 5. kelime), PRO ('lâ' 9. kelime); D3 2:168 eşi, 2:208 eşi, 24:21 eşi; D4 2MP 6 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[142] + "; aktör adlı 'ş-şeytân' (12. kelime; ölçüm); A2 yük taşıyan ve döşeklik hayvanların inşâsı; rızıktan yeme emri; şeytanın adımlarına uyma yasağı; şeytanın apaçık düşmanlığı; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 2 (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[143] = ("◇ 'semâniyete ezvâc, mine'd-da'ni'sneyni ve mine'l-ma'zi'sneyn, qul e-'z-zekereyni harrame emi'l-unseyeyni emmâ'ştemelet 'aleyhi erhâmu'l-unseyeyn, nebbi'ûnî bi-'ilmin in kuntum sâdiqîn' — "
 "'semâniye' + nekre çoğul 'zevc' + 'min' + belirli 'da'n' + ikil 'isneyn' + 've' + 'min' + belirli 'ma'z' + ikil 'isneyn' + IMPV 2MS I. bab + 'e' + belirli ikil 'zeker' + PERF 3MS II. bab + 'em' + belirli ikil 'unseyeyn' + 'em' + 'mâ' + PERF 3FS VIII. bab + ''alâ' + 3MS + çoğul 'erhâm' + belirli ikil 'unseyeyn' + "
 "IMPV 2MP II. bab + 2MP + 1S + 'bi' + nekre ''ilm' + 'in' + PERF 2MP I. bab + 2MP + çoğul etken ortaç 'sâdiq' "
 "(ölçüm edim soru, emir, şart, kip COND 1 · IMPV 2 · INTG 1; 1S 1 · 2MP 4 · 2MS 1 · 3FS 1 · 3MS 2; bab I. bab ×2 · II. bab ×2 · VIII. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=23 (n z=1,12); ölçüm HAPAKS ضأن ve معز (yeni kök karşılıkları 'koyun', 'keçi'); ölçüm '{{2|fâsıla صدقين → ن, N sınıfı}}' — satır aynen (6:142 ن → 6:143 ن); "
 "ölçüm '{{2|simetri \\[3, 3, 6, 1\\]}}' — satır aynen; ölçüm '{{2|harf 108 → harf3 104, isaret 4}}' — satır aynen; ölçüm '{{2|dış düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 2: 'qul' (9. kelime), 'nebbi'ûnî' (19. kelime); INTG 1: 'e-'z-zekereyni' (10. kelime); COND 1: 'in' (21. kelime); 've mine' (6.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) أنث ×2 ('l-unseyeyni' 13. / 'l-unseyeyn' 18. kelime), ثني ×2 ('sneyni' 5. / 'sneyn' 8. kelime) (okuma). "
 + T[143] + " (okuma). "
 + cumle(say('say 6:143 8-18', "sneyn, " + SOZ, True), say('dizi 6 143 8 18', "isneyn qâle zeker harrame em unseyeyn emmâ iştemelet 'alâ erhâm unseyeyn")) + ' '
 + cumle(say('say 6:143 21-23', 'in kuntum sâdiqîn', True), say('dizi 6 143 21 23', 'in kâne sâdiq')) + ' ' +
 "Ölçüm xref okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıpları: '" + N1 + "' süzgeç GEÇER, '" + N2 + "' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'e-'z-zekereyni' / 'emi'l-unseyeyni' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 'ezvâc' (2. kelime), 'l-unseyeyni' (13. kelime), 'l-unseyeyn' (18. kelime); B3 —; B4 —.",
 "◈D — D1 'semâniye' + nekre + 'min' + belirli + 'isneyn' + 've' + 'min' + belirli + 'isneyn' + IMPV + 'e' + belirli + PERF + 'em' + belirli + 'em' + 'mâ' + PERF + ''alâ' + izafet + belirli + IMPV + 'bi' + nekre + 'in' + PERF + 'sâdiq'; "
 "D2 soru, emir, şart; COND ('in' 21. kelime), IMPV ('qul' 9. kelime, 'nebbi'ûnî' 19. kelime), INTG ('e-'z-zekereyni' 10. kelime); D3 أنث ×2, ثني ×2; D4 1S 1 · 2MP 4 · 2MS 1 · 3FS 1 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[143] + "; aktör yok (ölçüm); A2 koyun ve keçiden sekiz eş; erkeklerin mi dişilerin mi rahimlerdekinin mi haram kılındığı sorusu; bilgiyle haber verme çağrısı; "
 "A3 'e-'z-zekereyni harrame emi'l-unseyeyni emmâ'ştemelet 'aleyhi erhâmu'l-unseyeyn, nebbi'ûnî bi-'ilmin in kuntum sâdiqîn' (söz içi, 10-23. kelime); "
 "A4 " + BOLUM + "; söz açılır (10. kelime); söz kapanır (23. kelime, ayet içi); şart → cevap (ayet içi; COND 'in' 21. kelime: 'in kuntum' / 'nebbi'ûnî' (19. kelime)); şahıs geçişi yok (ayetler arası); edim geçişi emir, yasak → soru, emir, şart (ayetler arası).",
)

D[144] = ("◇ 've mine'l-ibili'sneyni ve mine'l-baqari'sneyn, qul e-'z-zekereyni harrame emi'l-unseyeyni emmâ'ştemelet 'aleyhi erhâmu'l-unseyeyn, em kuntum şuhedâ'e iz vassâkumu'llâhu bi-hâzâ, fe-men ezlemu mimmeni'fterâ 'alâ'llâhi keziben li-yudille'n-nâse bi-ğayri 'ilm, inne'llâhe lâ yehdi'l-qavme'z-zâlimîn' — "
 "'ve' + 'min' + belirli 'ibil' + ikil 'isneyn' + 've' + 'min' + belirli 'baqar' + ikil 'isneyn' + IMPV 2MS I. bab + 'e' + belirli ikil 'zeker' + PERF 3MS II. bab + 'em' + belirli ikil 'unseyeyn' + 'em' + 'mâ' + PERF 3FS VIII. bab + ''alâ' + 3MS + çoğul 'erhâm' + belirli ikil 'unseyeyn' + "
 "'em' + PERF 2MP I. bab + 2MP + çoğul 'şehîd' + 'iz' + PERF 3MS II. bab + 2MP + lafız + 'bi' + 'hâzâ' + 'fe' + 'men' + 'ezlem' + 'min' + 'men' + PERF 3MS VIII. bab + ''alâ' + lafız + nekre 'kezib' + 'li' + IMPF 3MS IV. bab + belirli 'nâs' + 'bi' + 'ğayr' + nekre ''ilm' + "
 "'inne' + lafız + 'lâ' + IMPF 3MS I. bab + belirli 'qavm' + belirli çoğul etken ortaç 'zâlim' "
 "(ölçüm edim soru, emir, kip IMPV 1 · INTG 2 · NEG 1; 2MP 3 · 2MS 1 · 3FS 1 · 3MS 6; bab I. bab ×3 · II. bab ×2 · IV. bab ×1 · VIII. bab ×2). "
 "Allah lafzı 22., 29. ve 36. sırada (ölçüm allah z=0,97); Rab yok; ölçüm '{{3|esmâ شَهِيد 19\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' — ölçüm MÜHÜRSÜZ ile uyuşuyor (muhur_el hayır); "
 "esma_el kaydı 'degil' — 'em kuntum şuhedâ'e', kural 'esmâ adı esmâ dışı göndergeyle → degil' (muhatap topluluk) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=40 (n z=2,93); ölçüm '{{3|fâsıla ٱلظلمين → ن, N sınıfı}}' — satır aynen (6:143 ن → 6:144 ن); "
 "ölçüm '{{3|simetri \\[3, 1, 4, 1\\]}}' — satır aynen; ölçüm '{{3|harf 172 → harf3 167, isaret 5}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm IMPV 1: 'qul' (7. kelime); INTG 2: 'e-'z-zekereyni' (8. kelime), 'men' (24. kelime); NEG 1: 'lâ' (37. kelime); 've mine' (1.) ve 've mine' (4.) kelimelerindeki 've' CONJ; 'fe-men' (24.) kelimesindeki 'fe' REM; 'inne' (35.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) أله ×3 ('llâhu' 22. / 'llâhi' 29. / 'llâhe' 36. kelime), أنث ×2 ('l-unseyeyni' 11. / 'l-unseyeyn' 16. kelime), ثني ×2 ('sneyni' 3. / 'sneyn' 6. kelime), ظلم ×2 ('ezlemu' 25. / 'z-zâlimîn' 40. kelime) (okuma). "
 + T[144] + " (okuma). "
 + cumle(say('say 6:144 6-16', "sneyn, " + SOZ, True), say('dizi 6 144 6 16', "isneyn qâle zeker harrame em unseyeyn emmâ iştemelet 'alâ erhâm unseyeyn")) + ' '
 + cumle(say('say 6:144 24-26', 'fe-men ezlemu mimmeni', True), say('dizi 6 144 24 26', 'fe-men ezlem mimmen')) + ' '
 + cumle(say('say 6:144 25-30', "ezlemu mimmeni'fterâ 'alâ'llâhi keziben", True), say('dizi 6 144 25 30', "ezlem mimmen iftarâ 'alâ allâh kezib")) + ' '
 + cumle(say('say 6:144 33-35', "bi-ğayri 'ilm, inne", True), say('dizi 6 144 33 35', "ğayr 'ilm inne")) + ' '
 + cumle(say('say 6:144 37-40', "lâ yehdi'l-qavme'z-zâlimîn", True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıpları: '" + N1 + "' süzgeç GEÇER, '" + N3 + "' süzgeç GEÇER, '" + N4 + "' süzgeç GEÇMEZ, '" + N5 + "' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'e-'z-zekereyni' / 'emi'l-unseyeyni' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'n-nâse' (32. kelime); B2 'l-unseyeyni' (11. kelime), 'l-unseyeyn' (16. kelime); B3 —; B4 —.",
 "◈D — D1 've' + 'min' + belirli + 'isneyn' + 've' + 'min' + belirli + 'isneyn' + IMPV + 'e' + belirli + PERF + 'em' + belirli + 'em' + 'mâ' + PERF + ''alâ' + izafet + belirli + 'em' + PERF + 'şehîd' + 'iz' + PERF + lafız + 'bi' + 'hâzâ' + 'fe' + 'men' + 'ezlem' + 'min' + 'men' + PERF + ''alâ' + lafız + nekre + 'li' + IMPF + belirli + 'bi' + 'ğayr' + nekre + 'inne' + lafız + 'lâ' + IMPF + belirli + belirli; "
 "D2 soru, emir; IMPV ('qul' 7. kelime), INTG ('e-'z-zekereyni' 8. kelime, 'men' 24. kelime), NEG ('lâ' 37. kelime); D3 أله ×3, أنث ×2, ثني ×2, ظلم ×2; D4 2MP 3 · 2MS 1 · 3FS 1 · 3MS 6, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[144] + "; aktör yok (ölçüm); A2 deve ve sığırdan iki eş; haram kılınanın sorulması; Allah'ın tavsiyesine şahitlik sorusu; insanları saptırmak için Allah'a yalan uydurandan daha zalim olmayışı; zalimlerin doğru yola iletilmeyişi; "
 "A3 'e-'z-zekereyni harrame emi'l-unseyeyni emmâ'ştemelet 'aleyhi erhâmu'l-unseyeyn, em kuntum şuhedâ'e iz vassâkumu'llâhu bi-hâzâ' (söz içi, 8-23. kelime); "
 "A4 " + BOLUM + "; söz açılır (8. kelime); söz kapanır (23. kelime, ayet içi); şahıs geçişi 2 → 3 (ayetler arası); edim geçişi soru, emir, şart → soru, emir (ayetler arası); bölüm kapanışı.",
)
