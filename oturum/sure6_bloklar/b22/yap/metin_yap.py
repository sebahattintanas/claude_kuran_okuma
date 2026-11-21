# sûre 6 blok 22 (6:93-94) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b22/say2.txt'
os.environ['OLC'] = '/home/claude/b22/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Kitap indirmeyi inkâr edenler; ölüm sarhoşlukları' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 93: "Allah'a karşı yalan uydurandan yahut bana vahyedildi diyenden, kendisine hiçbir şey vahyedilmemişken, ve Allah'ın indirdiğinin benzerini indireceğim diyenden daha zalim kim olabilir? Zalimler ölüm dalgaları içindeyken bir görsen; melekler ellerini uzatmış hâlde: canlarınızı çıkarın; bugün aşağılık azabıyla cezalandırılacaksınız, Allah'a karşı haksız olanı söylemeniz yüzünden ve O'nun âyetlerine karşı büyüklenmeniz yüzünden.",
 94: "Andolsun, bize yalnız başınıza geldiniz, sizi evvelce yarattığımız gibi; size verdiğimiz şeyleri arkanızda bıraktınız; sizinle birlikte, aranızda ortaklar olduklarını iddia ettiğiniz şefaatçilerinizi görmüyoruz. Andolsun, aranızdaki bağ koptu ve iddia ettiğiniz şeyler sizden kaybolup gitti.",
}

T = {}
T[93] = ("'fterâ', 'qâle', 'ileyhi' 3MS (adsız; gönderge 'mimmeni' 3. kelime — 4., 9. ve 14. kelime); 'ûhiye' 3MS (adsız; edilgen; 10. kelime — naib-i faili (adsız), söz içi); "
         "konuşan 1S (adsız; söz içi; 'ileyye' — 11. kelime; gönderge 'mimmeni' 3. kelime); 've lem yûha' 3MS (adsız; edilgen; 13. kelime — naib-i faili 'şey'un' 15. kelime); "
         "'qâle' 3MS (adsız; gönderge 've men' 16. kelime, 17. kelime); konuşan 1S (adsız; söz içi; 'se-unzilu' — 18. kelime; gönderge 've men' 16. kelime); 'enzela' 3MS (fiil uyumu; 21. kelime — fail 22. kelime); "
         "muhatap 2MS (adsız; 'terâ' — 24. kelime); 'eydîhim' 3MP (adsız; gönderge 've'l-melâ'iketu' 30. kelime, 32. kelime); "
         "muhatap 2MP (adsız; söz içi; 'exricû', 'enfusekumu', 'tuczevne', 'kuntum', 'teqûlûne', 've kuntum', 'testekbirûn' — 33., 34., 36., 40., 41., 46. ve 49. kelime); "
         "'tuczevne' (36. kelime) edilgen — naib-i faili (adsız) muhatap 2MP; 'âyâtihî' 3MS (adsız; söz içi; gönderge 'llâhi' 43. kelime, 48. kelime)")
T[94] = ("konuşan 1P (adsız; 'ci'tumûnâ', 'xalaqnâkum', 'xavvelnâkum', 'nerâ' — 2., 5., 10. ve 14. kelime); "
         "muhatap 2MP (adsız; 'ci'tumûnâ', 'xalaqnâkum', 've teraktum', 'xavvelnâkum', 'zuhûrikum', 'me'akum', 'şufe'â'ekumu', 'za'amtum', 'fîkum', 'beynekum', ''ankum', 'kuntum', 'tez'umûn' — 2., 5., 8., 10., 12., 15., 16., 18., 20., 24., 26., 28. ve 29. kelime); "
         "'ennehum' 3MP (adsız; gönderge 'şufe'â'ekumu' 16. kelime, 19. kelime); 'teqatta'a' 3MS (adsız; gönderge 'beynekum' 24. kelime, 23. kelime; tartışmalı); 've dalle' 3MS (adsız; gönderge 'mâ' 27. kelime, 25. kelime)")

D = {}
D[93] = ("◇ 've men ezlemu mimmeni'fterâ 'alâ'llâhi keziben ev qâle ûhiye ileyye ve lem yûha ileyhi şey'un ve men qâle se-unzilu misle mâ enzela'llâhu ve lev terâ izi'z-zâlimûne fî ğamerâti'l-mevti ve'l-melâ'iketu bâsitû eydîhim exricû enfusekumu'l-yevme tuczevne 'azâbe'l-hûni bi-mâ kuntum teqûlûne 'ale'llâhi ğayra'l-haqqi ve kuntum 'an âyâtihî testekbirûn' — "
 "'ve' + 'men' + 'ezlem' + 'min' + 'men' + PERF 3MS VIII. bab + ''alâ' + lafız + nekre 'kezib' + 'ev' + PERF 3MS I. bab + PERF 3MS IV. bab edilgen + 'ilâ' + 1S + 've' + 'lem' + IMPF 3MS IV. bab edilgen + 'ilâ' + 3MS + nekre 'şey'' + 've' + 'men' + PERF 3MS I. bab + 'se' + IMPF 1S IV. bab + 'misl' + 'mâ' + PERF 3MS IV. bab + lafız + "
 "'ve' + 'lev' + IMPF 2MS I. bab + 'iz' + belirli çoğul etken ortaç 'zâlim' + 'fî' + çoğul 'ğamera' + belirli 'mevt' + 've' + belirli çoğul 'melek' + çoğul etken ortaç 'bâsit' + çoğul 'yed' + 3MP + IMPV 2MP IV. bab + 2MP + çoğul 'nefs' + 2MP + belirli 'yevm' + IMPF 2MP I. bab edilgen + 2MP + "
 "''azâb' + belirli 'hûn' + 'bi' + 'mâ' + PERF 2MP I. bab + 2MP + IMPF 2MP I. bab + 2MP + ''alâ' + lafız + 'ğayr' + belirli 'haqq' + 've' + PERF 2MP I. bab + 2MP + ''an' + çoğul 'âye' + 3MS + IMPF 2MP X. bab + 2MP "
 "(ölçüm edim soru, emir, şart, kip COND 1 · FUT 1 · IMPV 1 · INTG 2 · NEG 1; 1S 2 · 2MP 13 · 2MS 1 · 3MP 1 · 3MS 8; bab I. bab ×7 · IV. bab ×5 · VIII. bab ×1 · X. bab ×1). "
 "Allah lafzı 6., 22. ve 43. sırada (ölçüm allah z=0,70); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=49 (n z=3,88); ölçüm '{{1|EDİLGEN 3/14 fiil, pas z=0,89}}' — satır aynen; ölçüm '{{1|fâsıla تستكبرون → ن, N sınıfı}}' — satır aynen (6:92 ن → 6:93 ن); "
 "ölçüm '{{1|simetri \\[3, 1, 12, 1\\]}}' — satır aynen; ölçüm '{{1|harf 205 → harf3 199, isaret 6}}' — satır aynen; ölçüm '{{1|dış düğüm 5}}' — satır aynen. "
 "Ölçüm COND 1: 've lev' (23. kelime); FUT 1: 'se-unzilu' (18. kelime); IMPV 1: 'exricû' (33. kelime); INTG 2: 've men' (1. kelime), 've men' (16. kelime); NEG 1: 've lem' (12. kelime); "
 "'ve men' (1.) ve 've lev' (23.) kelimelerindeki 've' REM; 've lem' (12.), 've men' (16.) ve 've kuntum' (46.) kelimelerindeki 've' CONJ; 've'l-melâ'iketu' (30.) kelimesindeki 've' CIRC; 'ev' (8.) CONJ; 'izi' (25.) T (okuma). "
 "Kök ikilemesi (ölçüm) أله ×3 ('llâhi' 6., 'llâhu' 22., 'llâhi' 43. kelime), ظلم ×2 ('ezlemu' 2. / 'z-zâlimûne' 26. kelime), قول ×3 ('qâle' 9., 'qâle' 17., 'teqûlûne' 41. kelime), كون ×2 ('kuntum' 40. / 've kuntum' 46. kelime), نزل ×2 ('se-unzilu' 18. / 'enzela' 21. kelime), وحي ×2 ('ûhiye' 10. / 'yûha' 13. kelime) (okuma). "
 + T[93] + " (okuma). "
 + cumle(say('say 6:93 1-8', "ve men ezlemu mimmeni'fterâ 'alâ'llâhi keziben ev", True), say('dizi 6 93 1 8', "men ezlem mimmen iftarâ 'alâ allâh kezib ev")) + ' ' + cumle(say('say 6:93 2-7', "ezlemu mimmeni'fterâ 'alâ'llâhi keziben", True), say('dizi 6 93 2 7', "ezlem mimmen iftarâ 'alâ allâh kezib")) + ' ' + cumle(say('say 6:93 20-22', "mâ enzela'llâhu", True), say('dizi 6 93 20 22', "mâ enzele allâh")) + ' ' + cumle(say('say 6:93 36-38', "tuczevne 'azâbe'l-hûni", True), say('dizi 6 93 35 40', "yevm cezâ 'azâb hûn mâ kâne")) + ' ' +
 
 "Ölçüm xref 46:20 (emsal olarak basıldı) ve okunmuş 4 ayet. "
 "Ölçüm nakarat3 kalıpları: 'men ezlem mimmen iftarâ 'alâ allâh kezib ev' süzgeç GEÇER, 'ezlem mimmen iftarâ 'alâ allâh kezib' süzgeç GEÇER, 'mâ enzele allâh' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'ûhiye' / 've lem yûha' — ayetler arası: yok.",
 "◈K — K2 'l-yevme' (35. kelime).",
 "◈B — B1 —; B2 —; B3 'eydîhim' (32. kelime); B4 'l-mevti' (29. kelime).",
 "◈D — D1 've' + 'men' + 'ezlem' + 'min' + 'men' + PERF + ''alâ' + lafız + nekre + 'ev' + PERF + PERF + 'ilâ' + 've' + 'lem' + IMPF + 'ilâ' + nekre + 've' + 'men' + PERF + 'se' + IMPF + 'misl' + 'mâ' + PERF + lafız + 've' + 'lev' + IMPF + 'iz' + belirli + 'fî' + izafet + belirli + 've' + belirli + 'bâsit' + izafet + IMPV + izafet + belirli + IMPF + izafet + belirli + 'bi' + 'mâ' + PERF + IMPF + ''alâ' + lafız + 'ğayr' + belirli + 've' + PERF + ''an' + izafet + IMPF; "
 "D2 soru, emir, şart; COND ('ve lev' 23. kelime), FUT ('se-unzilu' 18. kelime), IMPV ('exricû' 33. kelime), INTG ('ve men' 1. kelime, 've men' 16. kelime), NEG ('ve lem' 12. kelime); D3 أله ×3, ظلم ×2, قول ×3, كون ×2, نزل ×2, وحي ×2; 46:20 eşi; D4 1S 2 · 2MP 13 · 2MS 1 · 3MP 1 · 3MS 8, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[93] + "; aktör yok (ölçüm); A2 Allah'a karşı yalan uyduran, vahiy almadığı hâlde vahyedildi diyen ve Allah'ın indirdiğinin benzerini indireceğini söyleyenden daha zalimin olmayışı; zalimlerin ölüm dalgaları içindeki hâli; meleklerin ellerini uzatarak canları çıkarma buyruğu; haksız söz ve büyüklenme yüzünden aşağılık azap; "
 "A3 'ûhiye ileyye' (söz içi, 10-11. kelime); 'se-unzilu misle mâ enzela'llâhu' (söz içi, 18-22. kelime); 'exricû enfusekumu'l-yevme tuczevne 'azâbe'l-hûni bi-mâ kuntum teqûlûne 'ale'llâhi ğayra'l-haqqi ve kuntum 'an âyâtihî testekbirûn' (söz içi, 33-49. kelime — söz fiili mahzuf, meleklerin sözü); "
 "A4 " + BOLUM + "; söz açılır (10. kelime); söz kapanır (11. kelime, ayet içi); söz açılır (18. kelime); söz kapanır (22. kelime, ayet içi); söz açılır (33. kelime); söz kapanır (49. kelime, ayet içi); şart → cevap (ayet içi; COND 'lev' 23. kelime: 've lev terâ' — cevap hazif (mealde ünlem)); şahıs geçişi 3 → 2 (ayetler arası); edim geçişi haber → soru, emir, şart (ayetler arası).",
)

D[94] = ("◇ 've le-qad ci'tumûnâ furâdâ kemâ xalaqnâkum evvele merratin ve teraktum mâ xavvelnâkum verâ'e zuhûrikum ve mâ nerâ me'akum şufe'â'ekumu'llezîne za'amtum ennehum fîkum şurakâ'u le-qad teqatta'a beynekum ve dalle 'ankum mâ kuntum tez'umûn' — "
 "'ve' + 'le' + 'qad' + PERF 2MP I. bab + 2MP + 1P + 'furâdâ' + 'ke' + 'mâ' + PERF 1P I. bab + 1P + 2MP + 'evvel' + nekre 'merra' + 've' + PERF 2MP I. bab + 2MP + 'mâ' + PERF 1P II. bab + 1P + 2MP + 'verâ'' + çoğul 'zahr' + 2MP + 've' + 'mâ' + IMPF 1P I. bab + 'ma'a' + 2MP + çoğul 'şefî'' + 2MP + 'ellezî' + PERF 2MP I. bab + 2MP + 'enne' + 3MP + 'fî' + 2MP + çoğul 'şerîk' + "
 "'le' + 'qad' + PERF 3MS V. bab + 'beyn' + 2MP + 've' + PERF 3MS I. bab + ''an' + 2MP + 'mâ' + PERF 2MP I. bab + 2MP + IMPF 2MP I. bab + 2MP "
 "(ölçüm edim haber, kip CERT 2 · EMPH 2 · NEG 1; 1P 6 · 2MP 18 · 3MP 1 · 3MS 2; bab I. bab ×8 · II. bab ×1 · V. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); esma_el kaydı 'degil' — 'evvele merratin', kural 'esmâ adı esmâ dışı göndergeyle → degil' (esmâ dışı gönderge) (okuma); liste farkı: ölçüm esmâ satırında 'evvele' yok, esma_kayit e_oto 1. "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=29 (n z=1,76); ölçüm '{{2|fâsıla تزعمون → ن, N sınıfı}}' — satır aynen (6:93 ن → 6:94 ن); "
 "ölçüm '{{2|simetri \\[3, 13, 17, 1\\]}}' — satır aynen; ölçüm '{{2|harf 129 → harf3 125, isaret 4}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen. "
 "Ölçüm CERT 2: 've le-qad' (1. kelime), 'le-qad' (22. kelime); EMPH 2: 've le-qad' (1. kelime), 'le-qad' (22. kelime); NEG 1: 've mâ' (13. kelime); "
 "'ve le-qad' (1.), 've teraktum' (8.), 've mâ' (13.) ve 've dalle' (25.) kelimelerindeki 've' CONJ; 'kemâ' (4.) SUB; 'ennehum' (19.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) زعم ×2 ('za'amtum' 18. / 'tez'umûn' 29. kelime) (okuma). "
 + T[94] + " (okuma). "
 + cumle(say('say 6:94 4-5', "kemâ xalaqnâkum", True)) + ' ' +
 
 "Ölçüm xref 18:48 (emsal olarak basıldı) ve okunmuş 1 ayet. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'ci'tumûnâ' / 've teraktum' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 'xalaqnâkum' (5. kelime); B3 —; B4 —.",
 "◈D — D1 've' + 'le' + 'qad' + PERF + 'furâdâ' + 'ke' + 'mâ' + PERF + 'evvel' + nekre + 've' + PERF + 'mâ' + PERF + 'verâ'' + izafet + 've' + 'mâ' + IMPF + 'ma'a' + izafet + 'ellezî' + PERF + 'enne' + 'fî' + çoğul + 'le' + 'qad' + PERF + 'beyn' + 've' + PERF + ''an' + 'mâ' + PERF + IMPF; "
 "D2 haber; CERT ('ve le-qad' 1. kelime, 'le-qad' 22. kelime), EMPH ('ve le-qad' 1. kelime, 'le-qad' 22. kelime), NEG ('ve mâ' 13. kelime); D3 زعم ×2; 18:48 eşi; D4 1P 6 · 2MP 18 · 3MP 1 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[94] + "; aktör yok (ölçüm); A2 yalnız başına, başlangıçtaki yaratılış gibi gelme; verilenlerin arkada bırakılması; şefaatçi sanılanların görünmemesi; aradaki bağın kopması ve iddia edilenlerin kaybolması; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi soru, emir, şart → haber (ayetler arası); söz kapanışı gerekçesi: 6:93 meleklerin sözü 49. kelimede kapandı, 6:94 konuşan 1P — yeni hitap, söz fiili yok (okuma); bölüm kapanışı.",
)
out = ['# ── blok 6:93-94 (2026-11-21) ──', 'MEAL22 = {']
for n in range(93, 95):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M22 = {']
for n in range(93, 95):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL22); M.update(M22)']
open('/home/claude/yamalar/metin_6_93_94.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
