# blok 6 (5:15-17) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b06/say2.txt'
os.environ['OLC'] = '/home/claude/b06/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'İsrâiloğullarının ve Nasârâ'nın misakı; kitap ehline gelen elçi; Mesih hakkında söz' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 15: "Ey kitap ehli! Elçimiz size geldi; kitaptan gizlemekte olduğunuz şeylerin çoğunu size açıklıyor, çoğunu da affediyor. Size Allah'tan bir nur ve apaçık bir kitap geldi.",
 16: "Allah onunla, rızasına uyanları esenlik yollarına iletir; kendi izniyle onları karanlıklardan nura çıkarır ve onları dosdoğru bir yola iletir.",
 17: "Andolsun, 'Şüphesiz Allah, Meryem oğlu Mesih'tir' diyenler inkâr etmiştir. De ki: 'Eğer Allah Meryem oğlu Mesih'i, annesini ve yeryüzündekilerin hepsini helâk etmek isterse, Allah'a karşı kim bir şeye güç yetirebilir?' Göklerin, yerin ve ikisi arasındakilerin mülkü Allah'ındır; dilediğini yaratır. Allah her şeye güç yetirendir.",
}

T15 = ("muhatap 2MP (adsız; 'ehle'l-kitâbi' — nidâ, 1-2. kelime; 'câ'akum', 'lekum', 'kuntum', 'tuxfûne'); 'rasûlunâ' ('câ'a' faili; 5. kelime); konuşan 1P (adsız; 'rasûlunâ' — gönderge lafız); 'yubeyyinu' ve 'ya'fû' faili 3MS (adsız; 6. ve 14. kelime — gönderge elçi); "
       "Allah (lafız; 20. kelime); 'nûrun ve kitâbun mubîn' (ikinci 'câ'a' faili; nekre, 21-23. kelime)")
T16 = ("Allah (lafız; 'yehdî' faili, 3. kelime); 'bihi' 3MS (gönderge kitap); 'meni'ttebe'a ridvânehu' ('yehdî' mef'ûlü; mevsûl, 4-6. kelime); 'ttebe'a' faili 3MS (adsız; gönderge 'men'); 'ridvânehu' 3MS (gönderge lafız); "
       "'yuxricuhum' ve 'yehdîhim' faili 3MS (adsız; gönderge lafız) ve mef'ûlü 3MP (gönderge 'men'); 'bi-iznihî' 3MS (gönderge lafız)")
T17 = ("'llezîne qâlû' ('kefera' faili; 3-4. kelime); söz içi Allah (lafız; 6. kelime) ve 'l-mesîhu'bnu meryem' (adlı kişi; 8-10. kelime); muhatap 2MS (adsız; 'qul'); 'men' (soru ismi; 'yemliku' faili); "
       "'erâde' ve 'yuhlike' faili 3MS (adsız; gönderge lafız); 'l-mesîha'bne meryeme' (adlı kişi; 'yuhlike' mef'ûlü, 21-23. kelime); 'ummehû' ('l-mesîh'e atıf; 3MS gönderge Mesih); 'men fi'l-ardi' (mevsûl; 25-27. kelime); "
       "Allah (lafız; 29. ve 38. kelime); 'beynehumâ' 3D (gönderge gökler ve yer); 'yaxluqu' ve 'yeşâ'' faili 3MS (adsız; gönderge lafız)")

D = {}
D[15] = ("◇ 'yâ ehle'l-kitâbi qad câ'akum rasûlunâ yubeyyinu lekum kesîran mimmâ kuntum tuxfûne mine'l-kitâbi ve ya'fû 'an kesîrin qad câ'akum mina'llâhi nûrun ve kitâbun mubîn' — "
 "'yâ' + 'ehl' + belirli 'kitâb' + 'qad' + PERF 3MS I. bab + 2MP + 'rasûl' + 1P + IMPF 3MS II. bab + 'li' + 2MP + nekre 'kesîr' + 'min' + 'mâ' + PERF 2MP I. bab + IMPF 2MP IV. bab + 'min' + belirli 'kitâb' + 've' + IMPF 3MS I. bab + ''an' + nekre 'kesîr' + 'qad' + PERF 3MS I. bab + 2MP + 'min' + lafız + nekre 'nûr' + 've' + nekre 'kitâb' + nekre etken ortaç 'mubîn' "
 "(ölçüm edim nida, kip CERT 2 · VOC 1; 1P 1 · 2MP 7 · 3MS 4; bab I. bab ×4 · II. bab ×1 · IV. bab ×1). "
 "Allah lafzı 20. sırada (ölçüm allah z=0,34); Rab yok; ölçüm esmâ '{{1|نُور 21\\. sırada, SON konum, MÜHÜRSÜZ \\| مُبِين 23\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET (ÇİFT) ton denge' (uyuşmuyor) — "
 "'qad câ'akum mina'llâhi nûrun', kural 'esmâ adı esmâ dışı göndergeyle → degil' (gelen nur); 'nûrun ve kitâbun mubîn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (kitabın sıfatı) (okuma); aktör yok (ölçüm). "
 "Ölçüm '{{1|yıldız yok}}' — satır aynen; n=23 (n z=1,12); ölçüm '{{1|fâsıla مبين → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|sayı işareti كَثِير, كَثِير}}' — satır aynen; ölçüm '{{1|simetri \\[4, 7, 15, 1\\]}}' — satır aynen; ölçüm '{{1|harf 96 → harf3 89, isaret 7}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen; ölçüm '{{1|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm CERT 2: 'qad' (3. ve 17. kelime); VOC 1: 'yâ' (1. kelime) (okuma). "
 "Kök ikilemeleri (ölçüm) بين ×2: 'yubeyyinu' (6. kelime) / 'mubîn' (23. kelime); جيأ ×2: 'câ'akum' (4. ve 18. kelime); كتب ×3: 'l-kitâbi' (2. ve 13. kelime) / 'kitâbun' (22. kelime); كثر ×2: 'kesîran' (8. kelime) / 'kesîrin' (16. kelime) (okuma). "
 "'ve ya'fû' (14.) ve 've kitâbun' (22.)'daki 've' morph CONJ (okuma). "
 + T15 + " (okuma). "
 + cumle(say('say 5:15 1-2', "yâ ehle'l-kitâb", True), say('say 5:15 1-5', "yâ ehle'l-kitâbi qad câ'akum rasûlunâ"), say('say 5:15 1-7', "yâ ehle'l-kitâbi qad câ'akum rasûlunâ yubeyyinu lekum"), say('dizi 5 15 1 7', "ehl kitâb qad câ'e rasûl beyyen li"), say('say 5:15 3-5', "qad câ'akum rasûlunâ")) + ' '
 + cumle(say('say 5:15 6-8', "yubeyyinu lekum kesîran", True), say('say 5:15 8-13', "kesîran mimmâ kuntum tuxfûne mine'l-kitâb"), say('say 5:15 10-11', "kuntum tuxfûn"), say('lem 5:15:11', "uxfiye")) + ' '
 + cumle(say('say 5:15 14-16 --on', "ve ya'fû 'an kesîr", True), say('say 5:15 15-16', "'an kesîr")) + ' '
 + cumle(say('say 5:15 17-21', "qad câ'akum mina'llâhi nûr", True), say('say 5:15 19-21', "mina'llâhi nûr"), say('say 5:15 21-23', "nûrun ve kitâbun mubîn"), say('say 5:15 22-23', "ve kitâbun mubîn")) + ' '
 "Ölçüm xref okunmamış iki ayet (sûre içi 1). Ölçüm nakarat3 bir kalıp: süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'yubeyyinu lekum kesîran' / 've ya'fû 'an kesîr' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'yâ' + izafet + belirli + 'qad' + PERF + izafet + IMPF + 'li' + nekre + 'min' + 'mâ' + PERF + IMPF + 'min' + belirli + 've' + IMPF + ''an' + nekre + 'qad' + PERF + 'min' + lafız + nekre + 've' + nekre + nekre; "
 "D2 nida, CERT ('qad' 3. ve 17. kelime), VOC ('yâ' 1. kelime); D3 بين ×2 · جيأ ×2 · كتب ×3 · كثر ×2; 42:30 eşi; D4 1P 1 · 2MP 7 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T15 + "; aktör yok (ölçüm); A2 elçinin gelişi; açıklama; gizleme; af; nur; apaçık kitap; A3 —; A4 " + BOLUM + "; hitap açılır ('yâ ehle'l-kitâbi', 1-2. kelime); edim geçişi haber → nida (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası).",
)

D[16] = ("◇ 'yehdî bihi'llâhu meni'ttebe'a ridvânehu subule's-selâmi ve yuxricuhum mine'z-zulumâti ile'n-nûri bi-iznihî ve yehdîhim ilâ sırâtin mustaqîm' — "
 "IMPF 3MS I. bab + 'bi' + 3MS + lafız + 'men' + PERF 3MS VIII. bab + 'ridvân' + 3MS + çoğul 'sebîl' + belirli 'selâm' + 've' + IMPF 3MS IV. bab + 3MP + 'min' + belirli çoğul 'zuleme' + 'ilâ' + belirli 'nûr' + 'bi' + 'izn' + 3MS + 've' + IMPF 3MS I. bab + 3MP + 'ilâ' + nekre 'sırât' + nekre etken ortaç 'mustaqîm' "
 "(ölçüm edim haber, kip yok; 3MP 2 · 3MS 7; bab I. bab ×2 · IV. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 3. sırada (ölçüm allah z=0,58); Rab yok; ölçüm esmâ '{{2|سَلام 8\\. sırada, ORTA konum, MÜHÜRSÜZ \\| نُور 13\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor) — "
 "'subule's-selâm', kural 'esmâ adı esmâ dışı göndergeyle → degil' (yolların izafeti); 'mine'z-zulumâti ile'n-nûr', kural 'esmâ adı esmâ dışı göndergeyle → degil' (karanlıklar karşıtı) (okuma); aktör yok (ölçüm). "
 "Ölçüm '{{2|yıldız yok}}' — satır aynen; n=18 (n z=0,59); ölçüm '{{2|fâsıla مستقيم → م, N sınıfı}}' — satır aynen; ölçüm '{{2|simetri \\[3, 1, 15, 1\\]}}' — satır aynen; ölçüm '{{2|harf 80 → harf3 76, isaret 4}}' — satır aynen; ölçüm '{{2|dış düğüm 1}}' — satır aynen. "
 "Kök ikilemeleri (ölçüm) هدي ×2: 'yehdî' (1. kelime) / 'yehdîhim' (15. kelime) (okuma). "
 "'ve yuxricuhum' (9.) ve 've yehdîhim' (15.)'deki 've' morph CONJ (okuma). "
 + T16 + " (okuma). "
 + cumle(say('say 5:16 1-3', "yehdî bihi'llâh", True), say('say 5:16 4-6', "meni'ttebe'a ridvânehu"), say('lem 5:16:6', "ridvân"), say('say 5:16 7-8', "subule's-selâm")) + ' '
 + cumle(say('say 5:16 9-13 --on', "ve yuxricuhum mine'z-zulumâti ile'n-nûr", True), say('say 5:16 10-13', "mine'z-zulumâti ile'n-nûr"), say('say 5:16 10-14', "mine'z-zulumâti ile'n-nûri bi-iznih"), say('dizi 5 16 11 14', "zuleme ilâ nûr izn")) + ' '
 + cumle(say('say 5:16 15-18 --on', "ve yehdîhim ilâ sırâtin mustaqîm", True), say('say 5:16 16-18', "ilâ sırâtin mustaqîm"), say('say 5:16 17-18', "sırâtin mustaqîm")) + ' '
 "Ölçüm xref 14:1 (basılmış). Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'z-zulumâti' / 'n-nûri' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPF + 'bi' + lafız + 'men' + PERF + izafet + izafet + belirli + 've' + IMPF + 'min' + belirli + 'ilâ' + belirli + 'bi' + izafet + 've' + IMPF + 'ilâ' + nekre + nekre; "
 "D2 haber; D3 هدي ×2; 2:142, 2:257 ve 14:1 eşleri; D4 3MP 2 · 3MS 7, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T16 + "; aktör yok (ölçüm); A2 yol gösterme; rızaya uyma; esenlik yolları; karanlıktan nura çıkarma; izin; dosdoğru yol; A3 —; A4 " + BOLUM + "; edim geçişi nida → haber (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası).",
)

D[17] = ("◇ 'leqad kefera'llezîne qâlû inna'llâhe huve'l-mesîhu'bnu meryem qul fe-men yemliku mina'llâhi şey'en in erâde en yuhlike'l-mesîha'bne meryeme ve ummehû ve men fi'l-ardi cemî'an ve li'llâhi mulku's-semâvâti ve'l-ardi ve mâ beynehumâ yaxluqu mâ yeşâ' ve'llâhu 'alâ kulli şey'in qadîr' — "
 "'le' + 'qad' + PERF 3MS I. bab + 'ellezî' + PERF 3MP I. bab + 'inne' + lafız + 'huve' + belirli özel ad 'mesîh' + 'ibn' + özel ad 'meryem' + IMPV 2MS I. bab + 'fe' + 'men' + IMPF 3MS I. bab + 'min' + lafız + nekre 'şey'' + 'in' + PERF 3MS IV. bab + 'en' + IMPF 3MS IV. bab + belirli özel ad 'mesîh' + 'ibn' + özel ad 'meryem' + 've' + 'umm' + 3MS + 've' + 'men' + 'fî' + belirli 'ard' + nekre 'cemî'' + 've' + 'li' + lafız + 'mulk' + belirli çoğul 'semâ'' + 've' + belirli 'ard' + 've' + 'mâ' + 'beyn' + 3D + IMPF 3MS I. bab + 'mâ' + IMPF 3MS I. bab + 've' + lafız + ''alâ' + 'kull' + nekre 'şey'' + nekre 'qadîr' "
 "(ölçüm edim soru, emir, şart, kip CERT 1 · COND 1 · EMPH 1 · IMPV 1 · INTG 1; 2MS 1 · 3D 1 · 3MP 2 · 3MS 8; bab I. bab ×6 · IV. bab ×2). "
 "Allah lafzı 6., 15., 29. ve 38. sırada (ölçüm allah z=1,38); Rab yok; ölçüm esmâ '{{3|قَدِير 42\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton celâl' (uyuşmuyor) — 've'llâhu 'alâ kulli şey'in qadîr', kural ''ve'llâhu X' kuralı → ilahi' (okuma); "
 "ölçüm aktör '{{3|adlı مَسِيح 8\\. sırada \\(kisi, rol fail\\+meful\\)}}', '{{3|adlı مَرْيَم 10\\. sırada \\(kisi, rol mecrur\\)}}', '{{3|adlı مَسِيح 21\\. sırada \\(kisi, rol fail\\+meful\\)}}', '{{3|adlı مَرْيَم 23\\. sırada \\(kisi, rol mecrur\\)}}' — satır aynen. "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=42 (n z=3,14); ölçüm '{{3|fâsıla قدير → ر, R sınıfı}}' — satır aynen; ölçüm '{{3|simetri \\[6, 1, 10, 2\\]}}' — satır aynen; ölçüm '{{3|harf 164 → harf3 155, isaret 9}}' — satır aynen; ölçüm '{{3|dış düğüm 5}}' — satır aynen; ölçüm '{{3|İÇ düğüm 2}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (1. kelime); COND 1: 'in' (17. kelime); EMPH 1: 'le' (1. kelime); IMPV 1: 'qul' (11. kelime); INTG 1: 'men' (12. kelime) (okuma). "
 "Kök ikilemeleri (ölçüm) أرض ×2: 'l-ardi' (27. ve 32. kelime); أله ×4: lafız 6., 15., 29. ve 38. kelimede; بني ×2: ''bnu' (9. kelime) / ''bne' (22. kelime); شيأ ×3: 'şey'en' (16. kelime) / 'yeşâ'' (37. kelime) / 'şey'in' (41. kelime); "
 "قول ×2: 'qâlû' (4. kelime) / 'qul' (11. kelime); مسح ×2: 'l-mesîhu' (8. kelime) / 'l-mesîha' (21. kelime); ملك ×2: 'yemliku' (13. kelime) / 'mulku' (30. kelime) (okuma). "
 "'fe-men' (12.)'deki 'fe' morph SUP; 've ummehû' (24.), 've men' (25.), 've'l-ardi' (32.) ve 've mâ' (33.)'daki 've' CONJ; 've li'llâhi' (29.) ve 've'llâhu' (38.)'daki 've' REM (okuma). "
 + T17 + " (okuma). "
 + cumle(say('say 5:17 1-4', "leqad kefera'llezîne qâlû", True), say('say 5:17 1-6', "leqad kefera'llezîne qâlû inna'llâh"), say('dizi 5 17 1 6', "qad kefera ellezî qâle inne allâh"), say('say 5:17 1-11', "leqad kefera'llezîne qâlû inna'llâhe huve'l-mesîhu'bnu meryeme qul"), say('dizi 5 17 1 11', "qad kefera ellezî qâle inne allâh huve mesîh ibn meryem qâle"), say('say 5:17 8-10', "l-mesîhu'bnu meryem"), say('dizi 5 17 8 10', "mesîh ibn meryem")) + ' '
 + cumle(say('say 5:17 11-16', "qul fe-men yemliku mina'llâhi şey'en", True), say('say 5:17 12-16', "fe-men yemliku mina'llâhi şey'en"), say('say 5:17 14-16', "mina'llâhi şey'en"), say('dizi 5 17 14 16', "min allâh şey'"), say('say 5:17 17-20', "in erâde en yuhlik"), say('say 5:17 21-23', "l-mesîha'bne meryem")) + ' '
 + cumle(say('say 5:17 25-28 --on', "ve men fi'l-ardi cemî'an", True), say('say 5:17 26-28', "fi'l-ardi cemî'an"), say('dizi 5 17 26 28', "fî ard cemî'")) + ' '
 + cumle(say('say 5:17 29-34 --on', "ve li'llâhi mulku's-semâvâti ve'l-ardi ve mâ beynehumâ", True), say('say 5:17 29-34', "ve li'llâhi mulku's-semâvâti ve'l-ardi ve mâ beynehumâ"), say('dizi 5 17 29 34', "allâh mulk semâ' ard mâ beyn"), say('say 5:17 29-33', "ve li'llâhi mulku's-semâvâti ve'l-ardi ve mâ"), say('dizi 5 17 29 33', "allâh mulk semâ' ard mâ"), say('say 5:17 30-32', "mulku's-semâvâti ve'l-ard"), say('dizi 5 17 30 32', "mulk semâ' ard")) + ' '
 + cumle(say('say 5:17 35-37', "yaxluqu mâ yeşâ'", True), say('say 5:17 37-42', "yeşâ' ve'llâhu 'alâ kulli şey'in qadîr"), say('dizi 5 17 37 42', "şâ'e allâh 'alâ kull şey' qadîr"), say('say 5:17 38-42 --on', "ve'llâhu 'alâ kulli şey'in qadîr"), say('say 5:17 38-42', "ve'llâhu 'alâ kulli şey'in qadîr"), say('dizi 5 17 38 42', "allâh 'alâ kull şey' qadîr"), say('say 5:17 39-42', "'alâ kulli şey'in qadîr"), say('dizi 5 17 39 42', "'alâ kull şey' qadîr"), say('say 5:17 39-41', "'alâ kulli şey'"), say('dizi 5 17 39 41', "'alâ kull şey'")) + ' '
 "Ölçüm xref 9:31, 14:8 ve 48:11 (basılmış), okunmuş iki ayet, okunmamış iki ayet (sûre içi 2). Ölçüm nakarat3 on iki kalıp: onu süzgeç GEÇER, ikisi GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'inna'llâhe huve'l-mesîhu'bnu meryem' / 'en yuhlike'l-mesîha'bne meryeme' — ayetler arası: yok.",
 "◈K — K1 's-semâvâti' (31. kelime), 'l-ardi' (27. ve 32. kelime).",
 "◈B — B1 'yaxluqu' (35. kelime); B2 —; B3 —; B4 —.",
 "◈D — D1 'le' + 'qad' + PERF + 'ellezî' + PERF + 'inne' + lafız + 'huve' + belirli + izafet + özel ad + IMPV + 'fe' + 'men' + IMPF + 'min' + lafız + nekre + 'in' + PERF + 'en' + IMPF + belirli + izafet + özel ad + 've' + izafet + 've' + 'men' + 'fî' + belirli + nekre + 've' + 'li' + lafız + izafet + belirli + 've' + belirli + 've' + 'mâ' + izafet + IMPF + 'mâ' + IMPF + 've' + lafız + ''alâ' + izafet + nekre + nekre; "
 "D2 soru, emir, şart, CERT ('qad' 1. kelime), COND ('in' 17. kelime), EMPH ('le' 1. kelime), IMPV ('qul' 11. kelime), INTG ('men' 12. kelime); D3 أرض ×2 · أله ×4 · بني ×2 · شيأ ×3 · قول ×2 · مسح ×2 · ملك ×2; 2:284, 3:47, 9:31, 14:8 ve 48:11 eşleri; D4 2MS 1 · 3D 1 · 3MP 2 · 3MS 8, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T17 + "; A2 inkâr; söz; Mesih; helâk; anne; yeryüzü; mülk; gökler ve yer; yaratma; dileme; güç yetirme; A3 'inna'llâhe huve'l-mesîhu'bnu meryem' (söz içi, 5-10. kelime); 'fe-men yemliku mina'llâhi şey'en' … 'cemî'an' (söz içi, 12-28. kelime); "
 "A4 " + BOLUM + "; edim geçişi haber → soru, emir, şart (ayetler arası); şahıs geçişi yok; söz açılır (5. kelime); söz kapanır (10. kelime, ayet içi); söz açılır (12. kelime); söz kapanır (28. kelime, ayet içi); "
 "şart COND 'in' 17. kelime: 'erâde en yuhlike' / 'fe-men yemliku' — cevap öne alınmış.",
)

out = ['# ── blok 5:15-17 (2026-11-15) ──', 'MEAL6 = {']
for n in range(15, 18):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M6 = {']
for n in range(15, 18):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL6); M.update(M6)']
open('/home/claude/yamalar/metin_5_15_17.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
