# blok 8 (5:20-23) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b08/say2.txt'
os.environ['OLC'] = '/home/claude/b08/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Mûsâ ve kavmi: kutsal topraklar; kırk yıl' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 20: "Hani Mûsâ kavmine demişti: 'Ey kavmim! Allah'ın üzerinizdeki nimetini anın: içinizden nebiler kıldı, sizi hükümdarlar kıldı ve âlemlerden hiç kimseye vermediğini size verdi.",
 21: "Ey kavmim! Allah'ın size yazdığı kutsal toprağa girin; arkanıza geri dönmeyin, yoksa hüsrana uğramış olarak dönersiniz.'",
 22: "Dediler ki: 'Ey Mûsâ! Orada zorba bir kavim var; onlar oradan çıkıncaya kadar biz oraya asla girmeyeceğiz. Eğer oradan çıkarlarsa, biz de mutlaka gireriz.'",
 23: "Korkanlardan, Allah'ın kendilerine nimet verdiği iki adam dedi ki: 'Onların üzerine kapıdan girin; kapıdan girdiğinizde şüphesiz galip gelirsiniz. İnanıyorsanız yalnız Allah'a dayanın.'",
}

T20 = ("Mûsâ (adlı kişi; 'qâle' faili, 3. kelime — ölçüm aktör); 'li-qavmihî' (sözün muhatabı kavim; 4. kelime; 3MS gönderge Mûsâ); söz içi konuşan 1S (adsız; 'qavmi', 5. kelime — gönderge Mûsâ); muhatap 2MP (söz içi, adsız; 'zkurû', ''aleykum', 'fîkum', 'ce'alekum', 'âtâkum'); "
       "Allah (lafız; 8. kelime); 'ce'ale', 'âtâ' ve 'yu'ti' faili 3MS (adsız; gönderge lafız); 'enbiyâ'e' (mef'ûl; çoğul, 13. kelime); 'mulûken' ('ce'alekum' tümleci; nekre çoğul, 15. kelime); 'ehaden' (olumsuz nekre; 20. kelime); 'l-'âlemîn' (belirli çoğul; 22. kelime)")
T21 = ("söz içi konuşan 1S (adsız; 'qavmi', 1. kelime — gönderge Mûsâ); muhatap 2MP (söz içi, adsız; 'dxulu', 'lekum', 'tertaddû', 'edbârikum', 'tenqalibû'); 'l-arda'l-muqaddesete' (mef'ûl; 3-4. kelime); Allah (lafız; 'ketebe' faili, 7. kelime); 'xâsirîn' (hâl; çoğul, 14. kelime)")
T22 = ("'qâlû' faili 3MP (adsız; 1. kelime — gönderge kavim); Mûsâ (adlı kişi; nidâ, 2. kelime — ölçüm aktör); söz içi konuşan 1P (adsız; 'innâ', 'nedxulehâ'); 'fîhâ', 'nedxulehâ' ve 'minhâ' 3FS (gönderge kutsal toprak); "
       "'qavmen cebbârîne' ('inne' ismi; nekre, 5-6. kelime); 'yaxrucû' faili 3MP (adsız; gönderge zorba kavim)")
T23 = ("'raculâni' ('qâle' faili; nekre ikil, 2. kelime — ölçüm aktör); 'llezîne yaxâfûne' (mevsûl; 4-5. kelime); 'yaxâfûne' faili 3MP (adsız); Allah (lafız; 'en'ame' faili, 7. kelime; 17. kelime); ''aleyhime' 3D (gönderge iki adam); "
       "muhatap 2MP (söz içi, adsız; 'dxulû', 'dexaltumûhu', 'innekum', 'tevekkelû', 'kuntum'); ''aleyhimu' 3MP (adsız; gönderge zorba kavim); 'l-bâbe' (mef'ûl; 11. kelime); 'mu'minîn' ('kuntum' haberi; çoğul, 21. kelime)")

D = {}
D[20] = ("◇ 've iz qâle mûsâ li-qavmihî yâ qavmi'zkurû ni'meta'llâhi 'aleykum iz ce'ale fîkum enbiyâ'e ve ce'alekum mulûken ve âtâkum mâ lem yu'ti ehaden mine'l-'âlemîn' — "
 "'ve' + 'iz' + PERF 3MS I. bab + özel ad 'mûsâ' + 'li' + 'qavm' + 3MS + 'yâ' + 'qavm' + 1S + IMPV 2MP I. bab + 'ni'me' + lafız + ''alâ' + 2MP + 'iz' + PERF 3MS I. bab + 'fî' + 2MP + çoğul 'nebiyy' + 've' + PERF 3MS I. bab + 2MP + nekre çoğul 'melik' + 've' + PERF 3MS IV. bab + 2MP + 'mâ' + 'lem' + IMPF 3MS IV. bab + nekre 'ehad' + 'min' + belirli çoğul ''âlem' "
 "(ölçüm edim emir, nida, kip IMPV 1 · NEG 1 · VOC 1; 1S 1 · 2MP 6 · 3MS 6; bab I. bab ×4 · IV. bab ×2). "
 "Allah lafzı 8. sırada (ölçüm allah z=0,38); Rab yok; ölçüm esmâ '{{1|مَلِك 15\\. sırada, ORTA konum, MÜHÜRSÜZ \\| أَحَد 20\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET (ÇİFT) ton karma' (uyuşmuyor) — "
 "'ve ce'alekum mulûken', kural 'çoğul insan göndergeli → degil' (hükümdarlar); 'mâ lem yu'ti ehaden', kural 'olumsuz nekre ehad → degil' (okuma); ölçüm '{{1|aktör: adlı مُوسَى 3\\. sırada \\(kisi, rol fail\\+konusan\\)}}' — satır aynen. "
 "Ölçüm '{{1|yıldız yok}}' — satır aynen; n=22 (n z=1,02); ölçüm '{{1|fâsıla ٱلعلمين → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|sayı işareti أَحَد}}' — satır aynen; ölçüm '{{1|simetri \\[3, 1, 10, 1\\]}}' — satır aynen; ölçüm '{{1|harf 96 → harf3 91, isaret 5}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 1: 'zkurû' (6. kelime); NEG 1: 'lem' (18. kelime); VOC 1: 'yâ' (5. kelime) (okuma); 'iz' (1. ve 10. kelime) morph T — zaman (okuma). "
 "Kök ikilemeleri (ölçüm) أتي ×2: 'âtâkum' (16. kelime) / 'yu'ti' (19. kelime); جعل ×2: 'ce'ale' (11. kelime) / 'ce'alekum' (14. kelime); قوم ×2: 'li-qavmihî' (4. kelime) / 'qavmi' (5. kelime) (okuma). "
 "'ve iz' (1.)'deki 've' morph REM; 've ce'alekum' (14.) ve 've âtâkum' (16.)'daki 've' CONJ (okuma). "
 + T20 + " (okuma). "
 + cumle(say('say 5:20 1-4 --on', "ve iz qâle mûsâ li-qavmih", True), say('say 5:20 2-4', "qâle mûsâ li-qavmih"), say('say 5:20 2-5', "qâle mûsâ li-qavmihî yâ qavmi"), say('say 5:20 5-9', "yâ qavmi'zkurû ni'meta'llâhi 'aleykum")) + ' '
 + cumle(say('say 5:20 6-9', "zkurû ni'meta'llâhi 'aleykum", True), say('dizi 5 20 6 9', "zekera ni'me allâh 'alâ"), say('say 5:20 6-10', "zkurû ni'meta'llâhi 'aleykum iz"), say('dizi 5 20 6 10', "zekera ni'me allâh 'alâ iz"), say('say 5:20 10-13', "iz ce'ale fîkum enbiyâ'")) + ' '
 + cumle(say('say 5:20 14-15 --on', "ve ce'alekum mulûken", True), say('say 5:20 16-22 --on', "ve âtâkum mâ lem yu'ti ehaden mine'l-'âlemîn"), say('say 5:20 17-20', "mâ lem yu'ti ehaden"), say('say 5:20 20-22', "ehaden mine'l-'âlemîn"), say('dizi 5 20 20 22', "ehad min 'âlem")) + ' '
 "Ölçüm xref 14:6 (basılmış). Ölçüm nakarat3 üç kalıp: ikisi süzgeç GEÇER, biri GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'iz' + PERF + özel ad + 'li' + izafet + 'yâ' + izafet + IMPV + izafet + lafız + ''alâ' + 'iz' + PERF + 'fî' + çoğul + 've' + PERF + nekre + 've' + PERF + 'mâ' + 'lem' + IMPF + nekre + 'min' + belirli; "
 "D2 emir, nida, IMPV ('zkurû' 6. kelime), NEG ('lem' 18. kelime), VOC ('yâ' 5. kelime); D3 أتي ×2 · جعل ×2 · قوم ×2; 2:54, 14:6, 33:9 ve 61:5 eşleri; 5:11 sûre içi eşi; D4 1S 1 · 2MP 6 · 3MS 6, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T20 + "; A2 nimeti anma; nebiler; hükümdarlık; verme; âlemler; A3 'yâ qavmi'zkurû' ile açılan söz (5. kelimeden; 5:21 sonuna dek); A4 " + BOLUM + "; bölüm açılışı; edim geçişi nida → emir, nida (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası); söz açılır (5. kelime).",
)

D[21] = ("◇ 'yâ qavmi'dxulu'l-arda'l-muqaddesete'lletî ketebe'llâhu lekum ve lâ tertaddû 'alâ edbârikum fe-tenqalibû xâsirîn' — "
 "'yâ' + 'qavm' + 1S + IMPV 2MP I. bab + belirli 'ard' + belirli edilgen ortaç 'muqaddese' + 'ellezî' + PERF 3MS I. bab + lafız + 'li' + 2MP + 've' + 'lâ' + IMPF 2MP VIII. bab + ''alâ' + çoğul 'dubur' + 2MP + 'fe' + IMPF 2MP VII. bab + çoğul etken ortaç 'xâsir' "
 "(ölçüm edim emir, yasak, nida, kip IMPV 1 · PRO 1 · VOC 1, biçim NEHY; 1S 1 · 2MP 8 · 3MS 1; bab I. bab ×2 · VII. bab ×1 · VIII. bab ×1). "
 "Allah lafzı 7. sırada (ölçüm allah z=0,90); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{2|yıldız yok}}' — satır aynen; n=14 (n z=0,17); ölçüm '{{2|biçim NEHY}}' — satır aynen; ölçüm '{{2|fâsıla خسرين → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|harf 71 → harf3 68, isaret 3}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen; ölçüm '{{2|bağ: YOK \\(esit2, nakarat3, xref üçü de boş\\)}}' — satır aynen. "
 "Ölçüm IMPV 1: 'dxulu' (2. kelime); PRO 1: 'lâ' (9. kelime); VOC 1: 'yâ' (1. kelime) (okuma); ölçüm biçim NEHY — 've lâ tertaddû' yasağı; D2'de yazılmadı (okuma). "
 "'ve lâ' (9.)'daki 've' morph REM; 'fe-tenqalibû' (13.)'daki 'fe' CAUS (okuma). "
 + T21 + " (okuma). "
 + cumle(say('say 5:21 1-4', "yâ qavmi'dxulu'l-arda'l-muqaddese", True), say('say 5:21 2-4', "dxulu'l-arda'l-muqaddese"), say('say 5:21 3-4', "l-arda'l-muqaddese"), say('lem 5:21:4', "muqaddese"), say('say 5:21 5-8', "lletî ketebe'llâhu lekum")) + ' '
 + cumle(say('say 5:21 9-12 --on', "ve lâ tertaddû 'alâ edbârikum", True), say('say 5:21 11-12', "'alâ edbârikum"), say('say 5:21 13-14 --on', "fe-tenqalibû xâsirîn")) + ' '
 "Ölçüm xref yok. Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'dxulu'l-arda' / 've lâ tertaddû 'alâ edbârikum' — ayetler arası: yok.",
 "◈K — K1 'l-arda' (3. kelime).",
 "◈B — B1 —; B2 —; B3 'tenqalibû' (13. kelime); B4 —.",
 "◈D — D1 'yâ' + izafet + IMPV + belirli + belirli + 'ellezî' + PERF + lafız + 'li' + 've' + 'lâ' + IMPF + ''alâ' + izafet + 'fe' + IMPF + çoğul; "
 "D2 emir, yasak, nida, IMPV ('dxulu' 2. kelime), PRO ('lâ' 9. kelime), VOC ('yâ' 1. kelime); D3 kök ikilemesi yok; 3:149 eşi; D4 1S 1 · 2MP 8 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T21 + "; aktör yok (ölçüm); A2 kutsal toprak; girme; yazma; geri dönme; hüsran; A3 söz sürüyor (5:20 5. kelimeden; 1-14. kelime); A4 " + BOLUM + "; edim geçişi emir, nida → emir, yasak, nida (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası); söz kapanır (14. kelime).",
)

D[22] = ("◇ 'qâlû yâ mûsâ inne fîhâ qavmen cebbârîne ve innâ len nedxulehâ hattâ yaxrucû minhâ fe-in yaxrucû minhâ fe-innâ dâxilûn' — "
 "PERF 3MP I. bab + 'yâ' + özel ad 'mûsâ' + 'inne' + 'fî' + 3FS + nekre 'qavm' + çoğul 'cebbâr' + 've' + 'inne' + 1P + 'len' + IMPF 1P I. bab + 3FS + 'hattâ' + IMPF 3MP I. bab + 'min' + 3FS + 'fe' + 'in' + IMPF 3MP I. bab + 'min' + 3FS + 'fe' + 'inne' + 1P + çoğul etken ortaç 'dâxil' "
 "(ölçüm edim nida, şart, kip COND 1 · NEG 1 · VOC 1; 1P 3 · 3FS 4 · 3MP 6; bab I. bab ×4). "
 "Ölçüm '{{3|lafız YOK · Rab YOK}}' — satır aynen; ölçüm esmâ '{{3|جَبّار 6\\. sırada, ORTA konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton celâl' (uyuşmuyor) — 'qavmen cebbârîne', kural 'çoğul insan göndergeli → degil' (zorba kavim) (okuma); "
 "ölçüm '{{3|aktör: adlı مُوسَى 2\\. sırada \\(kisi, rol fail\\+muhatap\\)}}' — satır aynen. "
 "Ölçüm '{{3|yıldız yok}}' — satır aynen; n=17 (n z=0,49); ölçüm '{{3|fâsıla دخلون → ن, N sınıfı}}' — satır aynen; ölçüm '{{3|simetri \\[4, 7, 12, 1\\]}}' — satır aynen; ölçüm '{{3|harf 77 → harf3 73, isaret 4}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm COND 1: 'in' (13. kelime); NEG 1: 'len' (8. kelime); VOC 1: 'yâ' (2. kelime) (okuma). "
 "Kök ikilemeleri (ölçüm) خرج ×2: 'yaxrucû' (11. ve 14. kelime); دخل ×2: 'nedxulehâ' (9. kelime) / 'dâxilûn' (17. kelime) (okuma). "
 "'ve innâ' (7.)'daki 've' morph CONJ; 'fe-in yaxrucû' (13.)'deki 'fe' REM; 'fe-innâ' (16.)'daki 'fe' RSLT (okuma). "
 + T22 + " (okuma). "
 + cumle(say('say 5:22 1-2', "qâlû yâ mûsâ", True), say('say 5:22 3-6', "inne fîhâ qavmen cebbârîn"), say('lem 5:22:6', "cebbâr")) + ' '
 + cumle(say('say 5:22 7-9 --on', "ve innâ len nedxulehâ", True), say('say 5:22 7-9', "ve innâ len nedxulehâ"), say('dizi 5 22 7 9', "inne len dexale"), say('say 5:22 10-12', "hattâ yaxrucû minhâ"), say('say 5:22 13-15 --on', "fe-in yaxrucû minhâ"), say('say 5:22 16-17 --on', "fe-innâ dâxilûn")) + ' '
 "Ölçüm xref yok. Ölçüm nakarat3 bir kalıp: süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'len nedxulehâ' / 'fe-innâ dâxilûn' — ayetler arası: 5:21 / 5:22 ('dxulu'l-arda' / 'len nedxulehâ').",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + 'yâ' + özel ad + 'inne' + 'fî' + nekre + çoğul + 've' + 'inne' + 'len' + IMPF + 'hattâ' + IMPF + 'min' + 'fe' + 'in' + IMPF + 'min' + 'fe' + 'inne' + çoğul; "
 "D2 nida, şart, COND ('in' 13. kelime), NEG ('len' 8. kelime), VOC ('yâ' 2. kelime); D3 خرج ×2 · دخل ×2; 26:130 eşi; D4 1P 3 · 3FS 4 · 3MP 6, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T22 + "; A2 zorba kavim; girmeme; çıkma; şartlı girme; A3 'yâ mûsâ' ile açılan söz (2-17. kelime); A4 " + BOLUM + "; edim geçişi emir, yasak, nida → nida, şart (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası); söz açılır (2. kelime); söz kapanır (17. kelime, ayet içi); "
 "şart → cevap (ayet içi; COND 'in' 13. kelime: 'fe-in yaxrucû minhâ' / 'fe-innâ dâxilûn' (16. kelime)).",
)

D[23] = ("◇ 'qâle raculâni mine'llezîne yaxâfûne en'ame'llâhu 'aleyhime'dxulû 'aleyhimu'l-bâbe fe-izâ dexaltumûhu fe-innekum ğâlibûn ve 'ale'llâhi fe-tevekkelû in kuntum mu'minîn' — "
 "PERF 3MS I. bab + ikil 'racul' + 'min' + 'ellezî' + IMPF 3MP I. bab + PERF 3MS IV. bab + lafız + ''alâ' + 3D + IMPV 2MP I. bab + ''alâ' + 3MP + belirli 'bâb' + 'fe' + 'izâ' + PERF 2MP I. bab + 3MS + 'fe' + 'inne' + 2MP + çoğul etken ortaç 'ğâlib' + 've' + ''alâ' + lafız + 'fe' + IMPV 2MP V. bab + 'in' + PERF 2MP I. bab + çoğul etken ortaç 'mu'min' "
 "(ölçüm edim emir, şart, kip COND 1 · IMPV 2; 2MP 9 · 3D 1 · 3MP 3 · 3MS 3; bab I. bab ×5 · IV. bab ×1 · V. bab ×1). "
 "Allah lafzı 7. ve 17. sırada (ölçüm allah z=1,38); Rab yok; ölçüm esmâ '{{4|مُؤْمِن 21\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton cemâl' (uyuşmuyor) — 'in kuntum mu'minîn', kural 'çoğul insan göndergeli → degil' (inananlar) (okuma); "
 "ölçüm '{{4|aktör: adsız `racül` 2\\. sırada}}' — satır aynen. "
 "Ölçüm '{{4|yıldız yok}}' — satır aynen; n=21 (n z=0,91); ölçüm '{{4|fâsıla مؤمنين → ن, N sınıfı}}' — satır aynen; ölçüm '{{4|simetri \\[4, 8, 12, 1\\]}}' — satır aynen; ölçüm '{{4|harf 102 → harf3 99, isaret 3}}' — satır aynen; ölçüm '{{4|dış düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 'in' (19. kelime); IMPV 2: 'dxulû' (9. kelime), 'tevekkelû' (18. kelime) (okuma); 'izâ' (12. kelime) morph T — zaman, cevaplı ('fe-innekum'); ölçüm COND sayımında değil (okuma). "
 "Kök ikilemeleri (ölçüm) أله ×2: lafız 7. ve 17. kelimede; دخل ×2: 'dxulû' (9. kelime) / 'dexaltumûhu' (13. kelime) (okuma). "
 "'fe-izâ' (12.)'daki 'fe' morph REM; 'fe-innekum' (14.)'daki 'fe' RSLT; 've 'ale'llâhi' (16.)'daki 've' REM; 'fe-tevekkelû' (18.)'daki 'fe' SUP (okuma). "
 + T23 + " (okuma). "
 + cumle(say('say 5:23 1-2', "qâle raculâni", True), say('say 5:23 3-5', "mine'llezîne yaxâfûn"), say('say 5:23 6-8', "en'ame'llâhu 'aleyhimâ"), say('say 5:23 9-11', "dxulû 'aleyhimu'l-bâb")) + ' '
 + cumle(say('say 5:23 12-13 --on', "fe-izâ dexaltumûh", True), say('say 5:23 14-15 --on', "fe-innekum ğâlibûn")) + ' '
 + cumle(say('say 5:23 16-18 --on', "ve 'ale'llâhi fe-tevekkelû", True), say('say 5:23 16-18', "ve 'ale'llâhi fe-tevekkelû"), say('dizi 5 23 16 18', "'alâ allâh tevekkel"), say('say 5:23 16-21 --on', "ve 'ale'llâhi fe-tevekkelû in kuntum mu'minîn"), say('say 5:23 18-21', "fe-tevekkelû in kuntum mu'minîn"), say('say 5:23 19-21', "in kuntum mu'minîn"), say('dizi 5 23 19 21', "in kâne mu'min")) + ' '
 "Ölçüm xref okunmuş bir ayet. Ölçüm nakarat3 iki kalıp: biri süzgeç GEÇER, biri GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: 5:22 / 5:23 ('len nedxulehâ' / ''dxulû 'aleyhimu'l-bâb').",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + ikil + 'min' + 'ellezî' + IMPF + PERF + lafız + ''alâ' + IMPV + ''alâ' + belirli + 'fe' + 'izâ' + PERF + 'fe' + 'inne' + çoğul + 've' + ''alâ' + lafız + 'fe' + IMPV + 'in' + PERF + çoğul; "
 "D2 emir, şart, COND ('in' 19. kelime), IMPV ('dxulû' 9. kelime, 'tevekkelû' 18. kelime); D3 أله ×2 · دخل ×2; eş yok; D4 2MP 9 · 3D 1 · 3MP 3 · 3MS 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T23 + "; A2 korku; nimet; kapıdan girme; galibiyet; tevekkül; iman; A3 ''dxulû 'aleyhimu'l-bâbe' ile açılan söz (9-21. kelime); A4 " + BOLUM + "; edim geçişi nida, şart → emir, şart (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası); söz açılır (9. kelime); söz kapanır (21. kelime, ayet içi); "
 "şart → cevap (ayet içi; COND 'in' 19. kelime: 'in kuntum mu'minîn' / 'fe-tevekkelû' (18. kelime)).",
)

out = ['# ── blok 5:20-23 (2026-11-15) ──', 'MEAL8 = {']
for n in range(20, 24):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M8 = {']
for n in range(20, 24):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL8); M.update(M8)']
open('/home/claude/yamalar/metin_5_20_23.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
