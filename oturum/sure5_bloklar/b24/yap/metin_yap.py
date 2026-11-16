# blok 23 (5:71-74) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b24/say2.txt'
os.environ['OLC'] = '/home/claude/b24/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Tebliğ emri; İsrâiloğullarının misakı; Mesih ve teslis' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 75: "Meryem oğlu Mesih ancak bir elçidir; ondan önce de elçiler gelip geçti. Annesi de çok doğrudur. Yemek yerlerdi. Bak, onlara âyetleri nasıl açıklıyoruz; sonra bak, nasıl çevriliyorlar!",
 76: "De ki: Allah'tan başka, size ne bir zarara ne de bir faydaya güç yetiremeyen şeye mi kulluk ediyorsunuz? Allah işitendir, bilendir.",
 77: "De ki: Ey Kitap ehli! Dininizde haksız yere aşırı gitmeyin ve önceden sapmış, birçoklarını saptırmış ve doğru yoldan sapmış bir kavmin heveslerine uymayın.",
}

T75 = ("'l-mesîhu'bnu meryeme' (adlı kişi; 2-4. kelime); 'xalet' 3FS (fiil uyumu; 8. kelime — fail 11. kelime); 'r-rusulu' ('xalet' faili; 11. kelime); 'qablihi' 3MS (adsız; gönderge Mesih, 10. kelime); "
       "'ummuhû' 3MS (adsız; iyelik, gönderge Mesih, 12. kelime); 'kânâ' 3MD (adsız; gönderge Mesih ve annesi, 14. kelime); 'ye'kulâni' faili 3MD / 3D (adsız; 15. kelime); muhatap 2MS (adsız; 17. ve 23. kelime — 'nzur'); "
       "konuşan 1P (adsız; 19. kelime); 'lehumu' 3MP (adsız; 20. kelime); 'yu'fekûn' faili 3MP (adsız; edilgen, 25. kelime)")
T76 = ("muhatap 2MS (adsız; 'qul' 1. kelime); muhatap 2MP (adsız; söz içi; 2. ve 9. kelime — 'ta'budûne', 'lekum'); Allah (lafız; 5. ve 13. kelime); mevsûl 'mâ' (6. ve 8. kelime — 'yemliku' faili 3MS, adsız); "
       "'huve' 3MS (adsız; fasıl zamiri, gönderge lafız; 14. kelime)")
T77 = ("muhatap 2MS (adsız; 'qul' 1. kelime); 'ehle'l-kitâbi' (nida edilen; 2-3. kelime); muhatap 2D (adsız; söz içi; 5. kelime — morph etiketi, çoğul hitap okunur); muhatap 2MP (adsız; söz içi; 7. ve 11. kelime — 'dînikum', 'tettebi'û'); 'qavmin' (nekre; 13. kelime); "
       "'dallû' faili 3MP (adsız; gönderge 'qavmin', 15. ve 20. kelime); 'edallû' faili 3MP (adsız; 18. kelime); 'kesîran' ('edallû' mef'ûlü; nekre; 19. kelime)")

D = {}
D[75] = ("◇ 'me'l-mesîhu'bnu meryeme illâ rasûlun qad xalet min qablihi'r-rusulu ve ummuhû sıddîqatun kânâ ye'kulâni't-ta'âme'nzur keyfe nubeyyinu lehumu'l-âyâti summe'nzur ennâ yu'fekûn' — "
 "'mâ' + belirli özel ad 'mesîh' + 'ibn' + özel ad 'meryem' + 'illâ' + nekre 'rasûl' + 'qad' + PERF 3FS I. bab + 'min' + 'qabl' + 3MS + belirli çoğul 'rasûl' + 've' + 'umm' + 3MS + nekre 'sıddîqa' + PERF 3MD I. bab + IMPF 3MD I. bab + belirli 'ta'âm' + "
 "IMPV 2MS I. bab + 'keyf' + IMPF 1P II. bab + 'li' + 3MP + belirli çoğul 'âye' + 'summe' + IMPV 2MS I. bab + 'ennâ' + edilgen IMPF 3MP I. bab "
 "(ölçüm edim soru, emir, kip CERT 1 · IMPV 2 · INTG 1 · NEG 1 · RES 1, biçim HASR; 1P 1 · 2MS 2 · 3D 1 · 3FS 1 · 3MD 3 · 3MP 3 · 3MS 2; bab I. bab ×6 · II. bab ×1; EDİLGEN 1/7 fiil). "
 "Lafız yok; Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm aktör '{{1|adlı مَسِيح 2\\. sırada \\(kisi, rol fail\\)}}' ve '{{1|adlı مَرْيَم 4\\. sırada \\(kisi, rol mecrur\\)}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=25 (n z=1,34); ölçüm '{{1|fâsıla يؤفكون → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|EDİLGEN 1/7 fiil, pas z=0,48}}' — satır aynen ('yu'fekûn' 25. kelime); "
 "ölçüm '{{1|simetri \\[3, 4, 9, 1\\]}}' — satır aynen; ölçüm '{{1|harf 103 → harf3 98, isaret 5}}' — satır aynen; ölçüm '{{1|dış düğüm 3}}' — satır aynen. "
 "Ölçüm NEG 1: 'mâ' (1. kelime); RES 1: 'illâ' (5. kelime); CERT 1: 'qad' (7. kelime); IMPV 2: 'nzur' (17. ve 23. kelime); INTG 1: 'ennâ' (24. kelime); 've ummuhû' (12.)'daki 've' CONJ, 'summe' (22.) CONJ (okuma). "
 "Kök ikilemesi (ölçüm) رسل ×2 ('rasûlun' 6. / 'r-rusulu' 11. kelime), نظر ×2 ('nzur' 17. / 23. kelime) (okuma). "
 + T75 + " (okuma). "
 + cumle(say('say 5:75 1-6', "me'l-mesîhu'bnu meryeme illâ rasûl", True), say('say 5:75 2-4', "l-mesîhu'bnu meryem"), say('say 5:75 5-6', "illâ rasûl")) + ' '
 + cumle(say('say 5:75 6-11', "rasûlun qad xalet min qablihi'r-rusul", True), say('dizi 5 75 6 11', "rasûl qad xalâ min qabl rasûl"), say('say 5:75 7-11', "qad xalet min qablihi'r-rusul"), say('say 5:75 8-11', "xalet min qablihi'r-rusul")) + ' '
 + cumle(say('say 5:75 12-13 --on', "ve ummuhû sıddîqa", True), say('say 5:75 14-16', "kânâ ye'kulâni't-ta'âm"), say('say 5:75 15-16', "ye'kulâni't-ta'âm"), say('dizi 5 75 14 16', "kâne ekele ta'âm")) + ' '
 + cumle(say('say 5:75 17-21', "nzur keyfe nubeyyinu lehumu'l-âyât", True), say('say 5:75 18-21', "keyfe nubeyyinu lehumu'l-âyât"), say('dizi 5 75 17 21', "nazara keyf beyyenu _ âye"), say('lem 5:75:19', "beyyenu")) + ' '
 + cumle(say('say 5:75 22-25', "summe'nzur ennâ yu'fekûn", True), say('say 5:75 23-25', "nzur ennâ yu'fekûn"), say('say 5:75 24-25', "ennâ yu'fekûn"), say('lem 5:75:25', "ufike")) + ' '
 "Ölçüm xref 3:144 ve 4:171 (emsal olarak basıldı) ve okunmuş başka ayetler. "
 "Ölçüm nakarat3 kalıbı: 'l-mesîhu'bnu meryem' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'mâ' + belirli + izafet + özel ad + 'illâ' + nekre + 'qad' + PERF + 'min' + izafet + belirli + 've' + izafet + nekre + PERF + IMPF + belirli + IMPV + 'keyf' + IMPF + 'li' + belirli + 'summe' + IMPV + 'ennâ' + IMPF; "
 "D2 soru, emir, NEG ('mâ' 1. kelime), RES ('illâ' 5. kelime), CERT ('qad' 7. kelime), IMPV ('nzur' 17. ve 23. kelime), INTG ('ennâ' 24. kelime), biçim HASR; D3 رسل ×2, نظر ×2; 3:144 eşi; D4 1P 1 · 2MS 2 · 3D 1 · 3FS 1 · 3MD 3 · 3MP 3 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T75 + "; aktör Mesih ve Meryem (ölçüm); A2 Mesih'in elçiliği; önceki elçiler; annesinin doğruluğu; yemek yeme; ayetlerin açıklanması; çevrilme; A3 —; "
 "A4 " + BOLUM + "; edim geçişi soru → soru, emir (ayetler arası); şahıs geçişi yok.",
)

D[76] = ("◇ 'qul e-ta'budûne min dûni'llâhi mâ lâ yemliku lekum darran ve lâ nef'an ve'llâhu huve's-semî'u'l-'alîm' — "
 "IMPV 2MS I. bab + 'e' + IMPF 2MP I. bab + 'min' + 'dûn' + lafız + 'mâ' + 'lâ' + IMPF 3MS I. bab + 'li' + 2MP + nekre 'darr' + 've' + 'lâ' + nekre 'nef'' + 've' + lafız + 'huve' + belirli 'semî'' + belirli ''alîm' "
 "(ölçüm edim soru, emir, kip IMPV 1 · INTG 1 · NEG 2; 2MP 3 · 2MS 1 · 3MS 2; bab I. bab ×3). "
 "Allah lafzı 5. ve 13. sırada (ölçüm allah z=1,97); Rab yok; ölçüm '{{2|esmâ سَمِيع 15\\. sırada, SON konum, MÜHÜR \\| عَلِيم 16\\. sırada, SON konum, MÜHÜR}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET (ÇİFT) ton denge' (uyuşuyor) — esma_el kaydı 'ilahi' — 've'llâhu huve's-semî'u'l-'alîm', kural ''ve'llâhu X' kuralı → ilahi' (lafzın haberi) (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=16 (n z=0,38); ölçüm '{{2|fâsıla ٱلعليم → م, N sınıfı}}' — satır aynen (kafiye: 5:75 ن → 5:76 م); "
 "ölçüm '{{2|simetri \\[4, 3, 11, 1\\]}}' — satır aynen; ölçüm '{{2|harf 61 → harf3 58, isaret 3}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen. "
 "Ölçüm IMPV 1: 'qul' (1. kelime); INTG 1: 'e' (2. kelime); NEG 2: 'lâ' (7. ve 11. kelime); 've lâ' (11.)'daki 've' CONJ, 've'llâhu' (13.)'daki 've' REM (okuma). "
 "Kök ikilemesi (ölçüm) أله ×2 (lafız 5., 13. kelime) (okuma). "
 + T76 + " (okuma). "
 + cumle(say('say 5:76 1-5', "qul e-ta'budûne min dûni'llâh", True), say('say 5:76 2-5', "e-ta'budûne min dûni'llâh"), say('say 5:76 3-5', "min dûni'llâh"), say('dizi 5 76 2 5', "'abede min dûn allâh")) + ' '
 + cumle(say('say 5:76 6-12', "mâ lâ yemliku lekum darran ve lâ nef'an", True), say('say 5:76 8-12', "yemliku lekum darran ve lâ nef'an"), say('say 5:76 10-12 --on', "darran ve lâ nef'an"), say('dizi 5 76 8 12', "meleket _ darr lâ nef'"), say('lem 5:76:8', "meleket")) + ' '
 + cumle(say('say 5:76 13-16 --on', "ve'llâhu huve's-semî'u'l-'alîm", True), say('say 5:76 15-16', "s-semî'u'l-'alîm"), say('dizi 5 76 13 16', "allâh _ semî' 'alîm")) + ' '
 "Ölçüm xref 20:89 (emsal olarak basıldı) ve okunmuş başka ayetler. "
 "Ölçüm nakarat3 kalıbı: 'min dûni'llâh' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'darran' / 'nef'an' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 —; B2 —; B3 's-semî'u' (15. kelime); B4 —.",
 "◈D — D1 IMPV + 'e' + IMPF + 'min' + izafet + lafız + 'mâ' + 'lâ' + IMPF + 'li' + nekre + 've' + 'lâ' + nekre + 've' + lafız + belirli + belirli; "
 "D2 soru, emir, IMPV ('qul' 1. kelime), INTG ('e' 2. kelime), NEG ('lâ' 7. ve 11. kelime); D3 أله ×2; 20:89 eşi; D4 2MP 3 · 2MS 1 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T76 + "; aktör yok (ölçüm); A2 zarar ve faydaya güç yetiremeyene kulluk; işitme ve bilme; A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 2 (ayetler arası).",
)

D[77] = ("◇ 'qul yâ ehle'l-kitâbi lâ teğlû fî dînikum ğayra'l-haqqi ve lâ tettebi'û ehvâ'e qavmin qad dallû min qablu ve edallû kesîran ve dallû 'an sevâ'i's-sebîl' — "
 "IMPV 2MS I. bab + 'yâ' + 'ehl' + belirli 'kitâb' + 'lâ' + IMPF 2D I. bab + 'fî' + 'dîn' + 2MP + 'ğayr' + belirli 'haqq' + 've' + 'lâ' + IMPF 2MP VIII. bab + çoğul 'ehvâ'' + nekre 'qavm' + 'qad' + PERF 3MP I. bab + 'min' + 'qabl' + "
 "'ve' + PERF 3MP IV. bab + nekre 'kesîr' + 've' + PERF 3MP I. bab + ''an' + 'sevâ'' + belirli 'sebîl' "
 "(ölçüm edim emir, yasak, nida, kip CERT 1 · IMPV 1 · PRO 2 · VOC 1, biçim NEHY; 2D 2 · 2MP 3 · 2MS 1 · 3MP 6; bab I. bab ×4 · IV. bab ×1 · VIII. bab ×1). "
 "Lafız yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=23 (n z=1,12); ölçüm '{{3|fâsıla ٱلسبيل → ل, ل sınıfı — KAFİYE KIRILMASI}}' — satır aynen (kafiye kırılması: 5:76 م → 5:77 ل); "
 "ölçüm '{{3|sayı işareti \\S+}}' — satır aynen ('kesîran' 19. kelime); ölçüm '{{3|simetri \\[3, 4, 14, 1\\]}}' — satır aynen; ölçüm '{{3|İÇ düğüm 3}}' — satır aynen; ölçüm '{{3|harf 95 → harf3 88, isaret 7}}' — satır aynen; ölçüm '{{3|dış düğüm 6}}' — satır aynen. "
 "Ölçüm IMPV 1: 'qul' (1. kelime); VOC 1: 'yâ' (2. kelime); PRO 2: 'lâ' (4. ve 10. kelime); CERT 1: 'qad' (14. kelime); 've lâ' (10.), 've edallû' (18.) ve 've dallû' (20.)'daki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) ضلل ×3 ('dallû' 15. / 'edallû' 18. / 'dallû' 20. kelime) (okuma). "
 + T77 + " (okuma). "
 + cumle(say('say 5:77 1-3', "qul yâ ehle'l-kitâb", True), say('say 5:77 2-3', "yâ ehle'l-kitâb"), say('dizi 5 77 3 7', "kitâb lâ teğlû fî dîn")) + ' '
 + cumle(say('say 5:77 4-9', "lâ teğlû fî dînikum ğayra'l-haqq", True), say('say 5:77 4-5', "lâ teğlû"), say('say 5:77 6-9', "fî dînikum ğayra'l-haqq")) + ' '
 + cumle(say('say 5:77 10-13 --on', "ve lâ tettebi'û ehvâ'e qavm", True), say('say 5:77 10-12 --on', "ve lâ tettebi'û ehvâ'"), say('dizi 5 77 10 12', "lâ ittebe'a ehvâ'"), say('say 5:77 11-12', "tettebi'û ehvâ'"), say('dizi 5 77 11 13', "ittebe'a ehvâ' qavm")) + ' '
 + cumle(say('say 5:77 14-17', "qad dallû min qabl", True), say('say 5:77 15-17', "dallû min qabl"), say('say 5:77 18-19 --on', "ve edallû kesîran")) + ' '
 + cumle(say('say 5:77 20-23 --on', "ve dallû 'an sevâ'i's-sebîl", True), say('dizi 5 77 20 23', "dalle 'an sevâ' sebîl"), say('say 5:77 21-23', "'an sevâ'i's-sebîl"), say('dizi 5 77 22 23', "sevâ' sebîl")) + ' '
 "Ölçüm xref 4:171 (emsal olarak basıldı) ve okunmuş başka ayetler. "
 "Ölçüm nakarat3 kalıpları: 'qul yâ ehle'l-kitâb' süzgeç GEÇER; 've lâ tettebi'û ehvâ'' ve ''an sevâ'i's-sebîl' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + 'yâ' + izafet + belirli + 'lâ' + IMPF + 'fî' + izafet + izafet + belirli + 've' + 'lâ' + IMPF + izafet + nekre + 'qad' + PERF + 'min' + 'qabl' + 've' + PERF + nekre + 've' + PERF + ''an' + izafet + belirli; "
 "D2 emir, yasak, nida, IMPV ('qul' 1. kelime), VOC ('yâ' 2. kelime), PRO ('lâ' 4. ve 10. kelime), CERT ('qad' 14. kelime), biçim NEHY; D3 ضلل ×3; 4:171 ve 5:60 eşleri; D4 2D 2 · 2MP 3 · 2MS 1 · 3MP 6, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T77 + "; aktör yok (ölçüm); A2 dinde aşırılık yasağı; sapmış kavmin heveslerine uyma yasağı; sapma ve saptırma; A3 —; "
 "A4 " + BOLUM + "; edim geçişi soru, emir → emir, yasak, nida (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası).",
)

out = ['# ── blok 5:75-77 (2026-11-16) ──', 'MEAL24 = {']
for n in range(75, 78):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M24 = {']
for n in range(75, 78):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL24); M.update(M24)']
open('/home/claude/yamalar/metin_5_75_77.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
