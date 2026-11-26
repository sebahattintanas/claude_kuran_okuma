# sûre 7 blok 17 (7:57-58) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b17/say2.txt'
os.environ['OLC'] = '/home/claude/b17/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Altı günde yaratma; dua; rüzgâr ve ölü belde' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_HP = _esc(re.search(r'HAPAKS: .*? — hapaks z=3,28', _OL[1]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 57: "Rahmetinin önünde rüzgârları müjdeci olarak gönderen O'dur. Nihayet ağır bulutları yüklenince onu ölü bir beldeye sürdük ve onunla suyu indirdik ve onunla her türlü üründen çıkardık. Ölüleri böyle çıkarırız; ola ki düşünürsünüz.",
 58: "Temiz beldenin bitkisi Rabbinin izniyle çıkar ve kötü olandan ancak kıt çıkar. Şükreden bir kavim için âyetleri böyle türlü türlü açıklarız.",
}

T = {}
T[57] = ("'huve' 3MS (adsız; gönderge 7:56 12. kelime, 1. kelime); 'yursilu' 3MS (adsız; gönderge 'huve' 1. kelime, 3. kelime); 'rahmetihî' 3MS eki (adsız; gönderge 'huve' 1. kelime, 8. kelime); 'eqallet' 3FS (adsız; gönderge 'r-riyâha' 4. kelime, 11. kelime); "
         "konuşan 1P (adsız; 'suqnâhu', 'fe-enzelnâ', 'fe-exracnâ', 'nuxricu' — 14., 17., 20. ve 26. kelime); 'suqnâhu' 3MS eki (adsız; gönderge 'sehâben' 12. kelime, 14. kelime); "
         "'bihi', 'bihî' 3MS eki (adsız; tartışmalı; gönderge 'li-beledin' 15. kelime — 18. ve 21. kelime); muhatap 2MP eki (adsız; 'le'allekum' — 28. kelime); muhatap 2MP (adsız; 'tezekkerûn' — 29. kelime)")
T[58] = ("'yexrucu' 3MS (fiil uyumu; 3. kelime — fail 4. kelime); 'nebâtuhû', 'rabbihî' 3MS eki (adsız; gönderge 'l-beledu' 1. kelime — 4. ve 6. kelime); 'xabuse' 3MS (adsız; gönderge 'llezî' 7. kelime, 8. kelime); "
         "'yexrucu' 3MS (adsız; gönderge 'llezî' 7. kelime, 10. kelime); konuşan 1P (adsız; 'nusarrifu' — 14. kelime); 'yeşkurûn' 3MP (adsız; gönderge 'li-qavmin' 16. kelime, 17. kelime)")

D = {}
D[57] = ("◇ 've huve'llezî yursilu'r-riyâha buşran beyne yedey rahmetihî hattâ izâ eqallet sehâben siqâlen suqnâhu li-beledin meyyitin fe-enzelnâ bihi'l-mâ'e fe-exracnâ bihî min kulli's-semerâti kezâlike nuxricu'l-mevtâ le'allekum tezekkerûn' — "
 "'ve' + 'huve' + 'ellezî' + IMPF 3MS IV. bab + belirli çoğul 'rîh' + nekre 'buşr' + 'beyn' + ikil 'yed' + 'rahme' + 3MS + 'hattâ' + 'izâ' + PERF 3FS IV. bab + nekre 'sehâb' + nekre çoğul 'saqîl' + PERF 1P I. bab + 3MS + 'li' + nekre 'beled' + nekre 'meyyit' + "
 "'fe' + PERF 1P IV. bab + 'bi' + 3MS + belirli 'mâ'' + 'fe' + PERF 1P IV. bab + 'bi' + 3MS + 'min' + 'kull' + belirli çoğul 'semere' + 'ke' + 'zâ' + IMPF 1P IV. bab + belirli çoğul 'meyyit' + 'le'alle' + 2MP + IMPF 2MP V. bab "
 "(ölçüm edim haber, kip yok; 1P 7 · 2MP 3 · 3FS 1 · 3MS 6; bab I. bab ×1 · IV. bab ×5 · V. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{1|yıldız ★}}' — satır aynen (kaynak n, z=1,76); n=29 (n z=1,76); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:56 ن → 7:57 ن); "
 "ölçüm '{{1|sayı işareti \\S+}}' — satır aynen; ölçüm '{{1|simetri \\[3, 1, 9, 1\\]}}' — satır aynen; ölçüm '{{1|harf 129 → harf3 120, isaret 9}}' — satır aynen; ölçüm '{{1|dış düğüm 3}}' — satır aynen. "
 "Ölçüm kip yok; "
 "'ve huve' (1.) kelimesindeki 've' REM; 'llezî' (2.) REL; 'beyne' (6.) LOC; 'hattâ' (9.) INC; 'izâ' (10.) T; 'fe-enzelnâ' (17.) kelimesindeki 'fe' CONJ; 'fe-exracnâ' (20.) kelimesindeki 'fe' CONJ; 'le'allekum' (28.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) خرج ×2 ('fe-exracnâ' 20. / 'nuxricu' 26. kelime); موت ×2 ('meyyitin' 16. / 'l-mevtâ' 27. kelime) (okuma). "
 + T[57] + " (okuma). "
 + cumle(say('say 7:57 1-8', "ve huve'llezî yursilu'r-riyâha buşran beyne yedey rahmetihî", True), say('say 7:57 4-8', "r-riyâha buşran beyne yedey rahmetihî"), say('dizi 7 57 4 8', "rîh buşr beyn yed rahme"), say('dizi 7 57 2 8', "ellezî ersele rîh buşr beyn yed rahme"), say('say 7:57 2-3', "llezî yursilu")) + ' '
 + cumle(say('say 7:57 9-13', "hattâ izâ eqallet sehâben siqâlen", True), say('say 7:57 14-16', "suqnâhu li-beledin meyyitin")) + ' '
 + cumle(say('say 7:57 17-19', "fe-enzelnâ bihi'l-mâ'e", True), say('say 7:57 20-24', "fe-exracnâ bihî min kulli's-semerâti"), say('say 7:57 23-24', "kulli's-semerâti")) + ' '
 + cumle(say('say 7:57 25-27', "kezâlike nuxricu'l-mevtâ", True), say('say 7:57 28-29', "le'allekum tezekkerûn")) + ' ' +
 "Ölçüm xref 25:48 (emsal olarak basıldı), 27:63 (basılmış), okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K1 'r-riyâha' (4. kelime), 'sehâben' (12. kelime), 'l-mâ'e' (19. kelime).",
 "◈B — B3 'yedey' (7. kelime); B4 'meyyitin' (16. kelime), 'l-mevtâ' (27. kelime).",
 "◈D — D1 've' + 'huve' + 'ellezî' + IMPF + belirli + nekre + izafet + izafet + 'hattâ' + 'izâ' + PERF + nekre + nekre + PERF + 'li' + nekre + nekre + 'fe' + PERF + 'bi' + belirli + 'fe' + PERF + 'bi' + 'min' + izafet + belirli + 'ke' + 'zâ' + IMPF + belirli + 'le'alle' + IMPF; "
 "D2 haber; kip yok; D3 25:48 eşi, خرج ×2, موت ×2; D4 1P 7 · 2MP 3 · 3FS 1 · 3MS 6, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[57] + "; aktör yok (ölçüm); A2 rahmetin önünde rüzgârların müjdeci gönderilişi; ağır bulutların yüklenip ölü beldeye sürülüşü; onunla suyun indirilişi ve her türlü ürünün çıkarılışı; ölülerin böyle çıkarılışı; düşünme umudu; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs sayısında beraberlik (1P 7 · 3. şahıs 7 — ölçüm baskın 1); şahıs geçişi 2 → 1 (ayetler arası); edim geçişi emir, yasak → haber (ayetler arası).",
)

D[58] = ("◇ 've'l-beledu't-tayyibu yexrucu nebâtuhû bi-izni rabbihî ve'llezî xabuse lâ yexrucu illâ nekiden kezâlike nusarrifu'l-âyâti li-qavmin yeşkurûn' — "
 "'ve' + belirli 'beled' + belirli 'tayyib' + IMPF 3MS I. bab + 'nebât' + 3MS + 'bi' + 'izn' + 'rabb' + 3MS + 've' + 'ellezî' + PERF 3MS I. bab + 'lâ' + IMPF 3MS I. bab + 'illâ' + nekre 'nekid' + 'ke' + 'zâ' + IMPF 1P II. bab + belirli çoğul 'âye' + 'li' + nekre 'qavm' + IMPF 3MP I. bab "
 "(ölçüm edim haber, kip NEG 1 · RES 1; 1P 1 · 3MP 2 · 3MS 5; bab I. bab ×4 · II. bab ×1). "
 "Allah lafzı yok; Rab 6. sırada (ölçüm rab z=0,93); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{2|yıldız ★★★}}' — satır aynen (kaynak hapaks, z=3,28); ölçüm '{{2|" + _HP + "}}' — satır aynen (yeni kök karşılığı 'kıt'); n=17 (n z=0,49); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:57 ن → 7:58 ن); "
 "ölçüm '{{2|simetri \\[3, 7, 11, 1\\]}}' — satır aynen; ölçüm '{{2|harf 78 → harf3 72, isaret 6}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 1: 'lâ' (9. kelime); RES 1: 'illâ' (11. kelime); ölçüm biçim HASR; "
 "'ve'l-beledu' (1.) kelimesindeki 've' REM; 've'llezî' (7.) kelimesindeki 've' CONJ; 'llezî' (7.) REL (okuma). "
 "Kök ikilemesi (ölçüm) خرج ×2 ('yexrucu' 3. / 'yexrucu' 10. kelime) (okuma). "
 + T[58] + " (okuma). "
 + cumle(say('say 7:58 1-6', "ve'l-beledu't-tayyibu yexrucu nebâtuhû bi-izni rabbihî", True), say('say 7:58 5-6', "bi-izni rabbihî")) + ' '
 + cumle(say('say 7:58 7-12', "ve'llezî xabuse lâ yexrucu illâ nekiden", True)) + ' '
 + cumle(say('say 7:58 13-17', "kezâlike nusarrifu'l-âyâti li-qavmin yeşkurûn", True), say('say 7:58 15-16', "l-âyâti li-qavmin")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 't-tayyibu' / 'xabuse' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'nebâtuhû' (4. kelime).",
 "◈D — D1 've' + belirli + belirli + IMPF + izafet + 'bi' + izafet + izafet + 've' + 'ellezî' + PERF + 'lâ' + IMPF + 'illâ' + nekre + 'ke' + 'zâ' + IMPF + belirli + 'li' + nekre + IMPF; "
 "D2 haber; NEG ('lâ' 9. kelime), RES ('illâ' 11. kelime); D3 خرج ×2; D4 1P 1 · 3MP 2 · 3MS 5, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[58] + "; aktör yok (ölçüm); A2 temiz beldenin bitkisinin Rabbin izniyle çıkışı; kötü olandan ancak kıt çıkışı; ayetlerin şükreden kavim için türlü türlü açıklanışı; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 1 → 3 (ayetler arası); edim geçişi yok (ayetler arası); bölüm kapanışı.",
)
out = ['# ── blok 7:57-58 (2026-11-26) ──', 'MEAL17 = {']
for n in range(57, 59):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M17 = {']
for n in range(57, 59):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL17); M.update(M17)']
open('/home/claude/yamalar/metin_7_57_58.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
