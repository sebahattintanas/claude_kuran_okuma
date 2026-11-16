# blok 1 (5:1-2) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b01/say2.txt'
os.environ['OLC'] = '/home/claude/b01/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Ahitlere vefa; haram kılınanlar; dinin tamamlanması; helal yiyecekler' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 1: "Ey iman edenler! Akitleri yerine getirin. Size okunacak olanlar dışında davar hayvanları sizin için helâl kılındı; siz ihramlı iken avı helâl saymayanlar olarak. Şüphesiz Allah dilediğine hükmeder.",
 2: "Ey iman edenler! Allah'ın nişanlarını, haram ayı, kurbanlığı, gerdanlıkları ve Rablerinden lütuf ve hoşnutluk arayarak Haram Ev'e yönelenleri helâl saymayın. İhramdan çıktığınızda avlanın. Sizi Haram Mescid'den alıkoydukları için bir kavme duyduğunuz kin sizi aşırı gitmeye sürüklemesin. İyilik ve takvâ üzerinde yardımlaşın, günah ve düşmanlık üzerinde yardımlaşmayın. Allah'tan sakının. Şüphesiz Allah'ın cezası çetindir.",
}

T1 = ("muhatap 2MP (adsız; 'ellezîne âmenû' — nidâ, 2. ve 3. kelime; 'evfû', 'lekum', ''aleykum', 'entum'); "
      "'uhillet' faili (adsız; edilgen, 6. kelime; nâib fâil 'behîmetu'l-en'âm'); "
      "'yutlâ' faili (adsız; edilgen, 12. kelime; nâib fâil zamir 3MS — gönderge 'mâ'); Allah (lafız); "
      "'yahkumu' ve 'yurîdu' faili 3MS (adsız; 21. ve 23. kelime — gönderge lafız)")
T2 = ("muhatap 2MP (adsız; 'ellezîne âmenû' — nidâ, 2. ve 3. kelime; 'tuhillû', 'halaltum', 'stâdû', 'yecrimennekum', 'saddûkum', 'ta'tedû', 'te'âvenû', 'ttequ'); "
      "Allah (lafız); 'âmmîne'l-beyte'l-harâm' (çoğul etken ortaç; 'tuhillû' mef'ûlüne atıf, 16. kelime); "
      "'yebteğûne' faili 3MP (adsız; 19. kelime — gönderge 'âmmîn'); Rab ('rabbihim' — yönelenlerin Rabbi); "
      "'şene'ânu qavmin' ('yecrimennekum' faili; izafet, 29-30. kelime); "
      "'saddûkum' faili 3MP (adsız; 32. kelime — gönderge 'qavm')")

D = {}
D[1] = ("◇ 'yâ eyyuhe'llezîne âmenû evfû bi'l-'uqûdi uhillet lekum behîmetu'l-en'âmi illâ mâ yutlâ 'aleykum ğayra muhilli's-saydi ve entum hurumun inna'llâhe yahkumu mâ yurîd' — "
 "'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF 3MP IV. bab + IMPV 2MP IV. bab + 'bi' + belirli çoğul ''uqûd' + edilgen PERF 3FS IV. bab + 'li' + 2MP + 'behîme' + belirli çoğul 'ne'am' + 'illâ' + 'mâ' + edilgen IMPF 3MS I. bab + ''alâ' + 2MP + 'ğayr' + çoğul etken ortaç 'muhillî' + belirli 'sayd' + 've' + 'entum' + nekre çoğul 'harâm' + 'inne' + lafız + IMPF 3MS I. bab + 'mâ' + IMPF 3MS IV. bab "
 "(ölçüm edim emir, nida, kip IMPV 1 · VOC 1, biçim DIKKAT + ISTISNA; 2MP 5 · 3FS 1 · 3MP 2 · 3MS 3; bab I. bab ×2 · IV. bab ×4). "
 "Allah lafzı 20. sırada (ölçüm allah z=0,34); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=23 (n z=1,12); ölçüm '{{1|biçim DIKKAT \\+ ISTISNA}}' — satır aynen; ölçüm '{{1|fâsıla يريد → د, د sınıfı}}' — satır aynen; ölçüm '{{1|EDİLGEN 2/6 fiil, pas z=1,57}}' — satır aynen; ölçüm '{{1|simetri \\[3, 11, 17, 1\\]}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm IMPV 1: 'evfû' (4. kelime); VOC 1: 'yâ' (1. kelime) (okuma); ölçüm biçim DIKKAT + ISTISNA — 'yâ eyyuhâ' nidâsı ve 'illâ' (10. kelime, morph EXP) istisnası; D2'de yazılmadı (okuma); edilgen 'uhillet' (6. kelime) ve 'yutlâ' (12. kelime) (okuma); 'muhilli' (15. kelime) morph ACT_PCPL IV. bab — ortaç, bab ◇'de yazılmadı (okuma). "
 "Kök ikilemesi (ölçüm) حلل ×2: 'uhillet' (6. kelime) / 'muhilli' (15. kelime) (okuma). "
 "'ve entum' (17. kelime)'daki 've' morph CIRC (okuma). "
 + T1 + " (okuma). "
 + cumle(say('say 5:1 1-3', "yâ eyyuhe'llezîne âmenû", True), say('say 5:1 4-5 --on', "evfû bi'l-'uqûd"), say('lem 5:1:5', "'uqûd")) + ' '
 + cumle(say('say 5:1 6-7', "uhillet lekum", True), say('lem 5:1:6', "ehalle"), say('say 5:1 8-9', "behîmetu'l-en'âm"), say('lem 5:1:8', "behîme")) + ' '
 + cumle(say('say 5:1 10-13', "illâ mâ yutlâ 'aleykum", True), say('say 5:1 12-13', "yutlâ 'aleykum"), say('say 5:1 14-16', "ğayra muhilli's-sayd"), say('lem 5:1:15', "muhillî")) + ' '
 + cumle(say('say 5:1 16-18 --on', "es-saydi ve entum hurum", True), say('say 5:1 17-18 --on', "ve entum hurum"), say('say 5:1 19-23', "inna'llâhe yahkumu mâ yurîd"), say('say 5:1 21-23', "yahkumu mâ yurîd")) + ' '
 "Ölçüm xref yok. Ölçüm nakarat3 iki kalıp: bir kalıp süzgeç GEÇER, bir kalıp süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'uhillet lekum' / 'ğayra muhilli's-saydi ve entum hurum' — ayetler arası: 5:1 / 5:2 ('uhillet lekum' / 'lâ tuhillû').",
 "◈K — —",
 "◈B — B1 'el-en'âm' (9. kelime); B2 —; B3 —; B4 —.",
 "◈D — D1 'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF + IMPV + 'bi' + belirli + PERF + 'li' + izafet + belirli + 'illâ' + 'mâ' + IMPF + ''alâ' + izafet + izafet + belirli + 've' + 'entum' + nekre + 'inne' + lafız + IMPF + 'mâ' + IMPF; D2 emir, nida, IMPV ('evfû' 4. kelime), VOC ('yâ' 1. kelime); D3 حلل ×2; 4:127, 22:28, 22:30 ve 22:34 eşleri; 5:2 blok içi eşi; D4 2MP 5 · 3FS 1 · 3MP 2 · 3MS 3, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T1 + "; aktör yok (ölçüm); A2 iman; akitleri yerine getirme; helâl kılma; okuma; av; ihram; hüküm; dileme; A3 —; A4 " + BOLUM + "; bölüm açılışı; hitap açılır ('yâ eyyuhe'llezîne âmenû', 1-3. kelime); edim geçişi emir, şart → emir, nida (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası).",
)

D[2] = ("◇ 'yâ eyyuhe'llezîne âmenû lâ tuhillû şe'â'ira'llâhi ve le'ş-şehra'l-harâme ve le'l-hedye ve le'l-qalâ'ide ve lâ âmmîne'l-beyte'l-harâme yebteğûne fadlen min rabbihim ve ridvânen ve izâ halaltum fe'stâdû ve lâ yecrimennekum şene'ânu qavmin en saddûkum 'ani'l-mescidi'l-harâmi en ta'tedû ve te'âvenû 'ale'l-birri ve't-taqvâ ve lâ te'âvenû 'ale'l-ismi ve'l-'udvâni ve'ttequ'llâhe inna'llâhe şedîdu'l-'iqâb' — "
 "'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF 3MP IV. bab + 'lâ' + IMPF 2MP IV. bab + çoğul 'şe'â'ir' + lafız + 've' + 'lâ' + belirli 'şehr' + belirli 'harâm' + 've' + 'lâ' + belirli 'hedy' + 've' + 'lâ' + belirli çoğul 'qalâ'id' + 've' + 'lâ' + çoğul etken ortaç 'âmm' + belirli 'beyt' + belirli 'harâm' + IMPF 3MP VIII. bab + nekre 'fadl' + 'min' + 'rabb' + 3MP + 've' + nekre 'ridvân' + 've' + 'izâ' + PERF 2MP I. bab + 'fe' + IMPV 2MP VIII. bab + 've' + 'lâ' + IMPF 3MS I. bab + 'nûn' + 2MP + 'şene'ân' + nekre 'qavm' + 'en' + PERF 3MP I. bab + 2MP + ''an' + belirli 'mescid' + belirli 'harâm' + 'en' + IMPF 2MP VIII. bab + 've' + IMPV 2MP VI. bab + ''alâ' + belirli 'birr' + 've' + belirli 'taqvâ' + 've' + 'lâ' + IMPF 2MP VI. bab + ''alâ' + belirli 'ism' + 've' + belirli ''udvân' + 've' + IMPV 2MP VIII. bab + lafız + 'inne' + lafız + 'şedîd' + belirli ''iqâb' "
 "(ölçüm edim emir, yasak, nida, kip EMPH 1 · IMPV 3 · NEG 4 · PRO 3 · VOC 1, biçim DIKKAT + NEHY; 2MP 16 · 3MP 7 · 3MS 1; bab I. bab ×3 · IV. bab ×2 · VI. bab ×2 · VIII. bab ×4). "
 "Allah lafzı 7., 48. ve 50. sırada (ölçüm allah z=0,63); Rab 22. sırada (ölçüm rab z=0,09); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=52 (n z=4,20); ölçüm '{{2|biçim DIKKAT \\+ NEHY}}' — satır aynen; ölçüm '{{2|fâsıla ٱلعقاب → ب, ب sınıfı}}' — satır aynen; ölçüm '{{2|simetri \\[4, 8, 33, 1\\]}}' — satır aynen; ölçüm '{{2|harf 255 → harf3 240, isaret 15}}' — satır aynen; ölçüm '{{2|dış düğüm 7}}' — satır aynen. "
 "Ölçüm EMPH 1: 'nûn' (28. kelime, 'yecrimennekum'); IMPV 3: 'stâdû' (26. kelime), 'te'âvenû' (38. kelime), 'ttequ' (47. kelime); NEG 4: 'lâ' (8., 11., 13. ve 15. kelime); PRO 3: 'lâ' (4., 27. ve 42. kelime); VOC 1: 'yâ' (1. kelime) (okuma); ölçüm biçim DIKKAT + NEHY — 'yâ eyyuhâ' nidâsı ve 'lâ tuhillû' yasağı; D2'de yazılmadı (okuma); 'âmmîne' (16. kelime) morph ACT_PCPL I. bab — ortaç, bab ◇'de yazılmadı (okuma); 'izâ' (24. kelime) morph T — zaman (okuma). "
 "Kök ikilemeleri (ölçüm) أله ×3: lafız 7., 48. ve 50. kelimede; حرم ×3: 'el-harâme' (10. ve 18. kelime), 'el-harâmi' (35. kelime); حلل ×2: 'tuhillû' (5. kelime) / 'halaltum' (25. kelime); عدو ×2: 'ta'tedû' (37. kelime) / 've'l-'udvâni' (46. kelime); عون ×2: 've te'âvenû' (38. kelime) / 'te'âvenû' (43. kelime); وقي ×2: 've't-taqvâ' (41. kelime) / 've'ttequ' (47. kelime) (okuma). "
 "'ve le'ş-şehra' (8.), 've le'l-hedye' (11.), 've le'l-qalâ'ide' (13.), 've lâ âmmîne' (15.), 've ridvânen' (23.), 've lâ yecrimennekum' (27.), 've't-taqvâ' (41.), 've lâ te'âvenû' (42.), 've'l-'udvâni' (46.) ve 've'ttequ' (47.)'daki 've' morph CONJ; 've izâ' (24.) ve 've te'âvenû' (38.)'daki 've' REM; 'fe'stâdû' (26.)'daki 'fe' RSLT (okuma). "
 + T2 + " (okuma). "
 + cumle(say('say 5:2 1-3', "yâ eyyuhe'llezîne âmenû", True), say('say 5:2 1-4', "yâ eyyuhe'llezîne âmenû lâ"), say('say 5:2 1-5', "yâ eyyuhe'llezîne âmenû lâ tuhillû"), say('say 5:2 4-7', "lâ tuhillû şe'â'ira'llâh"), say('say 5:2 5-7', "tuhillû şe'â'ira'llâh"), say('lem 5:2:6', "şe'â'ir")) + ' '
 + cumle(say('say 5:2 9-10', "eş-şehra'l-harâm", True), say('lem 5:2:12', "hedy"), say('lem 5:2:14', "qalâ'id"), say('say 5:2 16-18', "âmmîne'l-beyte'l-harâm"), say('say 5:2 17-18', "el-beyte'l-harâm")) + ' '
 + cumle(say('say 5:2 19-23', "yebteğûne fadlen min rabbihim ve ridvânâ", True), say('say 5:2 20-23', "fadlen min rabbihim ve ridvânâ"), say('dizi 5 2 19 20', "ibteğâ fadl"), say('dizi 5 2 19 22', "ibteğâ fadl min rabb")) + ' '
 + cumle(say('say 5:2 24-25 --on', "ve izâ halaltum", True), say('say 5:2 27-30 --on', "ve lâ yecrimennekum şene'ânu qavm"), say('lem 5:2:29', "şene'ân"), say('say 5:2 31-35', "en saddûkum 'ani'l-mescidi'l-harâm"), say('say 5:2 33-35', "'ani'l-mescidi'l-harâm")) + ' '
 + cumle(say('say 5:2 38-41 --on', "ve te'âvenû 'ale'l-birri ve't-taqvâ", True), say('say 5:2 42-46 --on', "ve lâ te'âvenû 'ale'l-ismi ve'l-'udvân"), say('say 5:2 45-46', "el-ismi ve'l-'udvân")) + ' '
 + cumle(say('say 5:2 47-48 --on', "ve'ttequ'llâh", True), say('say 5:2 47-49 --on', "ve'ttequ'llâhe inne"), say('say 5:2 47-50 --on', "ve'ttequ'llâhe inna'llâh"), say('dizi 5 2 47 50', "itteqâ allâh inne allâh"), say('say 5:2 49-52', "inna'llâhe şedîdu'l-'iqâb"), say('dizi 5 2 49 52', "inne allâh şedîd 'iqâb"), say('say 5:2 51-52', "şedîdu'l-'iqâb")) + ' '
 "Ölçüm xref 2:198, 48:25 ve 59:7 (basılmış), okunmuş iki ayet, okunmamış iki ayet. Ölçüm nakarat3 altı kalıp: hepsi süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 've te'âvenû 'ale'l-birri ve't-taqvâ' / 've lâ te'âvenû 'ale'l-ismi ve'l-'udvân' — ayetler arası: 5:1 / 5:2 ('uhillet lekum' / 'lâ tuhillû').",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'yâ' + 'eyy' + 'hâ' + 'ellezî' + PERF + 'lâ' + IMPF + izafet + lafız + 've' + 'lâ' + belirli + belirli + 've' + 'lâ' + belirli + 've' + 'lâ' + belirli + 've' + 'lâ' + çoğul + belirli + belirli + IMPF + nekre + 'min' + izafet + 've' + nekre + 've' + 'izâ' + PERF + 'fe' + IMPV + 've' + 'lâ' + IMPF + izafet + nekre + 'en' + PERF + ''an' + belirli + belirli + 'en' + IMPF + 've' + IMPV + ''alâ' + belirli + 've' + belirli + 've' + 'lâ' + IMPF + ''alâ' + belirli + 've' + belirli + 've' + IMPV + lafız + 'inne' + lafız + izafet + belirli; D2 emir, yasak, nida, EMPH ('nûn' 28. kelime), IMPV ('stâdû' 26. kelime, 'te'âvenû' 38. kelime, 'ttequ' 47. kelime), NEG ('lâ' 8., 11., 13. ve 15. kelime), PRO ('lâ' 4., 27. ve 42. kelime), VOC ('yâ' 1. kelime); D3 أله ×3 · حرم ×3 · حلل ×2 · عدو ×2 · عون ×2 · وقي ×2; 2:158, 2:194, 2:196, 2:198, 2:217, 22:32, 22:36, 48:25, 49:1 ve 59:7 eşleri; 5:1 blok içi eşi; D4 2MP 16 · 3MP 7 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T2 + "; aktör yok (ölçüm); A2 helâl saymama; nişanlar; haram ay; kurbanlık; gerdanlıklar; yönelme; lütuf arama; hoşnutluk; ihramdan çıkma; avlanma; kin; alıkoyma; aşırı gitme; yardımlaşma; iyilik; takvâ; günah; düşmanlık; sakınma; ceza; A3 —; A4 " + BOLUM + "; hitap açılır ('yâ eyyuhe'llezîne âmenû', 1-3. kelime); edim geçişi emir, nida → emir, yasak, nida (ayetler arası); şahıs geçişi yok.",
)

out = ['# ── blok 5:1-2 (2026-11-15) ──', 'MEAL1 = {']
for n in range(1, 3):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M1 = {']
for n in range(1, 3):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL1); M.update(M1)']
open('/home/claude/yamalar/metin_5_1_2.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
