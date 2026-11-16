# blok 14 (5:41) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b14/say2.txt'
os.environ['OLC'] = '/home/claude/b14/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Küfürde yarışanlar; Tevrat, İncil ve Kitap ile hüküm' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 41: "Ey elçi! Ağızlarıyla «İman ettik» deyip kalpleri iman etmemiş olanlardan ve Yahudi olanlardan küfürde yarışanlar seni üzmesin. Onlar yalana çokça kulak verenler, sana gelmemiş başka bir topluluk için çokça kulak verenlerdir; kelimeleri yerlerine konduktan sonra değiştirirler, «Size bu verilirse onu alın, o size verilmezse sakının» derler. Allah kimin fitnesini isterse, onun için Allah'a karşı hiçbir şeye güç yetiremezsin. Onlar, Allah'ın kalplerini temizlemek istemediği kimselerdir. Onlar için dünyada bir rezillik, âhirette de onlar için büyük bir azap vardır.",
}

T41 = ("muhatap 'r-rasûlu' (münâdâ; 2. kelime; 2MS — adsız: 'yahzunke' 4., 'ye'tûk' 26., 'temlike' 46. kelime); 'llezîne yusâri'ûne' (5-6. kelime; 'yahzunke' faili; 'yusâri'ûne' faili 3MP — adsız); 'llezîne qâlû' (10-11. kelime; 3MP fail — adsız); söz içi konuşan 1P 'âmennâ' (söz içi, adsız; 12. kelime); "
       "iyelik 3MP (adsız; 13. ve 16. kelime); 'tu'min' faili 3FS (adsız; 'qulûbuhum', 15. kelime); 'llezîne hâdû' (18-19. kelime; 3MP fail — adsız); 'semmâ'ûne' (20. ve 22. kelime; mübteda takdiri); 'qavmin âxarîne' (nekre; 23-24. kelime); 'ye'tûk' faili 3MP (adsız; 26. kelime); "
       "'yuharrifûne' ve 'yeqûlûne' faili 3MP (adsız; 27. ve 32. kelime); iyelik 3MS (adsız; 'mevâdi'ih', 31. kelime); söz muhatabı 2MP (söz muhatabı, adsız; 34., 36., 39. ve 40. kelime); 'hâzâ' (işaret; 35. kelime); 3MS 'hu' (adsız; 36. ve 39. kelime); 'men' (şart ismi; 41. kelime); "
       "Allah (lafız; 43., 49. ve 55. kelime); 'yuridi' faili 3MS (adsız; 42. ve 54. kelime); iyelik 3MS (adsız; 'fitneteh', 44. kelime); 'lehû' 3MS (adsız; 47. kelime); 'ulâ'ike'llezîne' (51-52. kelime); 'yutahhira' faili 3MS (adsız; 57. kelime); iyelik 3MP (adsız; 'qulûbehum', 58. kelime); "
       "'lehum' 3MP (adsız; 59. ve 63. kelime); 'xizyun' (nekre; 62. kelime); ''azâbun 'azîm' (nekre; 66-67. kelime)")

D = {}
D[41] = ("◇ 'yâ eyyuhe'r-rasûlu lâ yahzunke'llezîne yusâri'ûne fi'l-kufri mine'llezîne qâlû âmennâ bi-efvâhihim ve lem tu'min qulûbuhum ve mine'llezîne hâdû semmâ'ûne li'l-kezibi semmâ'ûne li-qavmin âxarîne lem ye'tûk yuharrifûne'l-kelime min ba'di mevâdi'ih yeqûlûne in ûtîtum hâzâ fe-xuzûhu ve in lem tu'tevhu fa'hzerû ve men yuridi'llâhu fitnetehû fe-len temlike lehû mina'llâhi şey'â ulâ'ike'llezîne lem yuridi'llâhu en yutahhira qulûbehum lehum fi'd-dunyâ xizyun ve lehum fi'l-âxirati 'azâbun 'azîm' — "
 "'yâ' + 'eyy' + 'hâ' + belirli 'rasûl' + 'lâ' + IMPF 3MS I. bab + 2MS + 'ellezî' + IMPF 3MP III. bab + 'fî' + belirli 'kufr' + 'min' + 'ellezî' + PERF 3MP I. bab + PERF 1P IV. bab + 'bi' + çoğul 'fûh' + 3MP + 've' + 'lem' + IMPF 3FS IV. bab + çoğul 'qalb' + 3MP + 've' + 'min' + 'ellezî' + PERF 3MP I. bab + çoğul 'semmâ'' + 'li' + belirli 'kezib' + çoğul 'semmâ'' + 'li' + nekre 'qavm' + çoğul 'âxar' + 'lem' + IMPF 3MP I. bab + 2MS + "
 "IMPF 3MP II. bab + belirli 'kelim' + 'min' + 'ba'd' + çoğul 'mevdi'' + 3MS + IMPF 3MP I. bab + 'in' + PERF 2MP IV. bab (edilgen) + 'hâ' + 'zâ' + 'fe' + IMPV 2MP I. bab + 3MS + 've' + 'in' + 'lem' + IMPF 2MP IV. bab (edilgen) + 3MS + 'fe' + IMPV 2MP I. bab + 've' + 'men' + IMPF 3MS IV. bab + lafız + 'fitne' + 3MS + 'fe' + 'len' + IMPF 2MS I. bab + 'li' + 3MS + 'min' + lafız + nekre 'şey'' + "
 "'ulâ' + 'ke' + 'ellezî' + 'lem' + IMPF 3MS IV. bab + lafız + 'en' + IMPF 3MS II. bab + çoğul 'qalb' + 3MP + 'li' + 3MP + 'fî' + belirli 'dunyâ' + nekre 'xizy' + 've' + 'li' + 3MP + 'fî' + belirli 'âxir' + nekre ''azâb' + nekre ''azîm' "
 "(ölçüm edim emir, yasak, nida, şart, kip COND 3 · IMPV 2 · NEG 5 · PRO 1 · VOC 1; 1P 2 · 2MP 8 · 2MS 3 · 3FS 1 · 3MP 17 · 3MS 9; bab I. bab ×8 · II. bab ×2 · III. bab ×1 · IV. bab ×6). "
 "Allah lafzı 43., 49. ve 55. sırada (ölçüm allah z=0,37); Rab yok; ölçüm '{{1|esmâ آخِر 65\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton denge' (uyuşmuyor) — 'fi'l-âxirati 'azâbun 'azîm', kural ''fi'l-âxira' emsali → degil' (âhiret) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=67 (n z=5,80); ölçüm '{{1|biçim DIKKAT \\+ NEHY}}' — satır aynen; ölçüm '{{1|EDİLGEN 2/17 fiil, pas z=0,34}}' — satır aynen; ölçüm '{{1|fâsıla عظيم → م, N sınıfı}}' — satır aynen; ölçüm '{{1|simetri \\[6, 5, 33, 2\\]}}' — satır aynen; "
 "ölçüm '{{1|harf 298 → harf3 279, isaret 19}}' — satır aynen; ölçüm '{{1|dış düğüm 3}}' — satır aynen; ölçüm '{{1|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm biçim DIKKAT + NEHY — 'yâ eyyuhe'r-rasûl' nidâsı (1. kelime, morph VOC + ATT) ve 'lâ yahzunke' yasağı (3. kelime, morph PRO); NEG 5: 'lem' (14., 25., 38. ve 53. kelime), 'len' (45. kelime); COND 3: 'in' (33. ve 37. kelime), 'men' (41. kelime); EDİLGEN — 'ûtîtum' (34. kelime), 'tu'tevhu' (39. kelime) morph PASS (okuma). "
 "'ve lem' (14.) ve 've men' (41.)'deki 've' morph REM; 've mine' (17.), 've in' (37.) ve 've lehum' (63.)'deki 've' CONJ; 'fe-xuzûhu' (36.), 'fa'hzerû' (40.) ve 'fe-len' (45.)'deki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) أتي ×3: 'ye'tûk' (26. kelime), 'ûtîtum' (34. kelime), 'tu'tevhu' (39. kelime); أخر ×2: 'âxarîne' (24. kelime) / 'l-âxirati' (65. kelime); أله ×3: lafız 43., 49. ve 55. kelime; أمن ×2: 'âmennâ' (12. kelime) / 'tu'min' (15. kelime) — söz / kalp; "
 "رود ×2: 'yuridi' (42. ve 54. kelime); سمع ×2: 'semmâ'ûne' (20. ve 22. kelime); قلب ×2: 'qulûbuhum' (16. kelime) / 'qulûbehum' (58. kelime); قول ×2: 'qâlû' (11. kelime) / 'yeqûlûne' (32. kelime) (okuma). "
 + T41 + " (okuma). "
 + cumle(say('say 5:41 1-2', "yâ eyyuhe'r-rasûl", True), say('say 5:41 3-6 --on', "lâ yahzunke'llezîne yusâri'ûne"), say('say 5:41 4-8', "yahzunke'llezîne yusâri'ûne fi'l-kufr"), say('say 5:41 6-8', "yusâri'ûne fi'l-kufr"), say('say 5:41 7-8', "fi'l-kufr"), say('lem 5:41:6', "yusâri'u")) + ' '
 + cumle(say('say 5:41 9-11', "mine'llezîne qâlû", True), say('dizi 5 41 9 11', "min ellezî qâle"), say('say 5:41 11-12 --on', "qâlû âmennâ"), say('say 5:41 12-13', "âmennâ bi-efvâhihim"), say('say 5:41 14-16 --on', "ve lem tu'min qulûbuhum"), say('say 5:41 17-19', "ve mine'llezîne hâdû")) + ' '
 + cumle(say('say 5:41 20-21', "semmâ'ûne li'l-kezib", True), say('lem 5:41:20', "semmâ'"), say('say 5:41 22-24', "semmâ'ûne li-qavmin âxarîne"), say('say 5:41 23-24', "li-qavmin âxarîne"), say('say 5:41 25-26 --on', "lem ye'tûk")) + ' '
 + cumle(say('say 5:41 27-28', "yuharrifûne'l-kelim", True), say('say 5:41 27-31', "yuharrifûne'l-kelime min ba'di mevâdi'ih"), say('dizi 5 41 27 31', "yuharrifu kelim min ba'd mevâdi'"), say('say 5:41 29-31', "min ba'di mevâdi'ih"), say('lem 5:41:31', "mevâdi'")) + ' '
 + cumle(say('say 5:41 33-35 --on', "in ûtîtum hâzâ", True), say('say 5:41 36-36', "fe-xuzûh"), say('say 5:41 37-40 --on', "ve in lem tu'tevhu fa'hzerû")) + ' '
 + cumle(say('say 5:41 41-44 --on', "ve men yuridi'llâhu fitneteh", True), say('say 5:41 42-43', "yuridi'llâh"), say('say 5:41 45-50 --on', "fe-len temlike lehû mina'llâhi şey'â"), say('say 5:41 48-50', "mina'llâhi şey'â"), say('dizi 5 41 48 50', "min allâh şey'")) + ' '
 + cumle(say('say 5:41 51-52', "ulâ'ike'llezîne", True), say('say 5:41 53-56 --on', "lem yuridi'llâhu en"), say('say 5:41 54-56', "yuridi'llâhu en"), say('dizi 5 41 54 56', "erâde allâh en"), say('say 5:41 57-58', "yutahhira qulûbehum")) + ' '
 + cumle(say('say 5:41 59-62', "lehum fi'd-dunyâ xizyun", True), say('say 5:41 60-61', "fi'd-dunyâ"), say('dizi 5 41 59 62', "_ fî dunyâ xizy"), say('say 5:41 63-67', "ve lehum fi'l-âxirati 'azâbun 'azîm"), say('say 5:41 64-67', "fi'l-âxirati 'azâbun 'azîm"),
         say('say 5:41 65-67', "l-âxirati 'azâbun 'azîm"), say('say 5:41 66-67', "'azâbun 'azîm"), say('dizi 5 41 64 67', "fî âxir 'azâb 'azîm")) + ' '
 "Ölçüm xref 48:11 (basılmış), 2:114 ve 3:176 (emsal olarak basıldı) ve 5:17 (basılmış). "
 "Ölçüm nakarat3 kalıpları: 'fi'l-âxirati 'azâbun 'azîm' süzgeç GEÇER; 'mine'llezîne qâlû', 'mina'llâhi şey'â' ve 'yuridi'llâhu en' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'âmennâ bi-efvâhihim' / 've lem tu'min qulûbuhum'; 'fe-xuzûhu' / 'fa'hzerû'; 'lehum fi'd-dunyâ xizyun' / 've lehum fi'l-âxirati 'azâbun 'azîm' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 'qulûbuhum' (16. kelime), 'qulûbehum' (58. kelime); B4 —.",
 "◈D — D1 'yâ' + 'eyy' + 'hâ' + belirli + 'lâ' + IMPF + 'ellezî' + IMPF + 'fî' + belirli + 'min' + 'ellezî' + PERF + PERF + 'bi' + izafet + 've' + 'lem' + IMPF + izafet + 've' + 'min' + 'ellezî' + PERF + çoğul + 'li' + belirli + çoğul + 'li' + nekre + sıfat + 'lem' + IMPF + IMPF + belirli + 'min' + izafet + izafet + IMPF + 'in' + PERF + 'hâ' + 'zâ' + 'fe' + IMPV + 've' + 'in' + 'lem' + IMPF + 'fe' + IMPV + 've' + 'men' + IMPF + lafız + izafet + 'fe' + 'len' + IMPF + 'li' + 'min' + lafız + nekre + 'ulâ' + 'ke' + 'ellezî' + 'lem' + IMPF + lafız + 'en' + IMPF + izafet + 'li' + 'fî' + belirli + nekre + 've' + 'li' + 'fî' + belirli + nekre + nekre; "
 "D2 emir, yasak, nida, şart, IMPV ('fe-xuzûhu' 36., 'fa'hzerû' 40. kelime), PRO ('lâ' 3. kelime), VOC ('yâ' 1. kelime), COND ('in' 33. ve 37., 'men' 41. kelime), NEG ('lem' 14., 25., 38. ve 53., 'len' 45. kelime); D3 أتي ×3, أله ×3, أخر ×2, أمن ×2, رود ×2, سمع ×2, قلب ×2, قول ×2; 2:114, 3:176, 4:28 ve 9:47 eşleri; D4 1P 2 · 2MP 8 · 2MS 3 · 3FS 1 · 3MP 17 · 3MS 9, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T41 + "; aktör yok (ölçüm); A2 elçiye hitap; küfürde yarışma; ağızla iman; kalbin iman etmemesi; yalana kulak verme; kelimeleri değiştirme; fitne; kalplerin temizlenmemesi; dünya rezilliği; âhiret azabı; "
 "A3 'âmennâ' (söz içi, 12-12. kelime); 'in ûtîtum hâzâ' ile açılan söz (33-40. kelime); "
 "A4 " + BOLUM + "; bölüm açılışı; hitap açılır ('yâ eyyuhe'r-rasûl', 1-2. kelime); edim geçişi soru → emir, yasak, nida, şart (ayetler arası); şahıs geçişi yok; "
 "şart → cevap (ayet içi; COND 'in' 33. kelime: 'in ûtîtum hâzâ' / 'fe-xuzûhu' (36. kelime)); şart → cevap (ayet içi; COND 'in' 37. kelime: 've in lem tu'tevhu' / 'fa'hzerû' (40. kelime)); şart → cevap (ayet içi; COND 'men' 41. kelime: 've men yuridi'llâhu fitnetehû' / 'fe-len temlike lehû mina'llâhi şey'â' (45. kelime)).",
)

out = ['# ── blok 5:41-41 (2026-11-15) ──', 'MEAL14 = {']
for n in range(41, 42):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M14 = {']
for n in range(41, 42):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL14); M.update(M14)']
open('/home/claude/yamalar/metin_5_41_41.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
