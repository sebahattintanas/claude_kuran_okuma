# sûre 7 blok 3 (7:11-13) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b03/say2.txt'
os.environ['OLC'] = '/home/claude/b03/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Âdem'e secde; İblis'in mühleti; ağaç ve iniş' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|': t = t.replace(c, '\\' + c)
    return t
_AK = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 11: "Andolsun, sizi yarattık, sonra size biçim verdik, sonra meleklere: Âdem'e secde edin, dedik; İblîs hariç secde ettiler. O, secde edenlerden olmadı.",
 12: "Dedi ki: Sana emrettiğimde secde etmekten seni ne alıkoydu? Dedi ki: Ben ondan hayırlıyım; beni ateşten yarattın, onu ise çamurdan yarattın.",
 13: "Dedi ki: Öyleyse oradan in; orada büyüklenmek senin için olmaz. Hemen çık; sen gerçekten aşağılananlardansın.",
}

T = {}
T[11] = ("konuşan 1P (adsız; 'xalaqnâkum', 'savvernâkum', 'qulnâ' — 2., 4. ve 6. kelime); muhatap 2MP eki (adsız; 'xalaqnâkum', 'savvernâkum' — 2. ve 4. kelime); muhatap 2MP (adsız; söz içi; 'scudû' — 8. kelime); "
         "'fe-secedû' 3MP (adsız; gönderge 'l-melâ'iketi' 7. kelime, 10. kelime); 'yekun' 3MS (adsız; gönderge 'iblîs' 12. kelime, 14. kelime)")
T[12] = ("'qâle' 3MS (adsız; tartışmalı; sayı uyumsuz; gönderge 7:11 6. kelime, 1. kelime); 'mene'ake' 3MS (adsız; söz içi; gönderge 'mâ' 2. kelime, 3. kelime); muhatap 2MS eki (adsız; söz içi; 'mene'ake', 'emertuk' — 3. ve 7. kelime); "
         "muhatap 2MS (adsız; söz içi; 'tescude' — 5. kelime); konuşan 1S (adsız; söz içi; 'emertuk' — 7. kelime); 'qâle' 3MS (adsız; gönderge 7:11 12. kelime, 8. kelime); konuşan 1S (adsız; söz içi; 'ene' — 9. kelime); "
         "'minhu', 've xalaqtehû' 3MS eki (adsız; söz içi; gönderge 7:11 9. kelime — 11. ve 15. kelime); muhatap 2MS (adsız; söz içi; 'xalaqtenî', 've xalaqtehû' — 12. ve 15. kelime); konuşan 1S eki (adsız; söz içi; 'xalaqtenî' — 12. kelime)")
T[13] = ("'qâle' 3MS (adsız; tartışmalı; sayı uyumsuz; gönderge 7:11 6. kelime, 1. kelime); muhatap 2MS (adsız; söz içi; 'fe'hbit', 'tetekebbera', 'fe'xruc' — 2., 8. ve 10. kelime); "
         "'minhâ', 'fîhâ' 3FS eki (adsız; söz içi; tartışmalı; anılan yer bölümde adsız — 3. ve 9. kelime); 'yekûnu' 3MS (adsız; söz içi; gönderge 'en tetekebbera' 7-8. kelime, 5. kelime); "
         "muhatap 2MS eki (adsız; söz içi; 'leke', 'inneke' — 6. ve 11. kelime)")

D = {}
D[11] = ("◇ 've le-qad xalaqnâkum summe savvernâkum summe qulnâ li'l-melâ'iketi'scudû li-âdeme fe-secedû illâ iblîs, lem yekun mine's-sâcidîn' — "
 "'ve' + 'le' + 'qad' + PERF 1P I. bab + 2MP + 'summe' + PERF 1P II. bab + 2MP + 'summe' + PERF 1P I. bab + 'li' + belirli çoğul 'melek' + IMPV 2MP I. bab + 'li' + özel ad 'âdem' + 'fe' + PERF 3MP I. bab + 'illâ' + özel ad 'iblîs' + 'lem' + IMPF 3MS I. bab + 'min' + belirli çoğul etken ortaç 'sâcid' "
 "(ölçüm edim emir, kip CERT 1 · EMPH 1 · IMPV 1 · NEG 1; 1P 6 · 2MP 4 · 3MP 2 · 3MS 1; bab I. bab ×5 · II. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); ölçüm '{{1|" + _AK + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=16 (n z=0,38); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:10 ن → 7:11 ن); "
 "ölçüm '{{1|simetri \\[3, 1, 11, 1\\]}}' — satır aynen; ölçüm '{{1|harf 72 → harf3 70, isaret 2}}' — satır aynen; ölçüm '{{1|dış düğüm 1}}' — satır aynen. "
 "Ölçüm CERT 1: 've le-qad' (1. kelime); EMPH 1: 've le-qad' (1. kelime; 'le'); IMPV 1: 'scudû' (8. kelime); NEG 1: 'lem' (13. kelime); ölçüm biçim ISTISNA ('illâ' 11. kelime); "
 "'ve le-qad' (1.) kelimesindeki 've' CONJ; 'summe' (3.) CONJ; 'summe' (5.) CONJ; 'fe-secedû' (10.) kelimesindeki 'fe' REM (okuma). "
 "Kök ikilemesi (ölçüm) سجد ×3 ('scudû' 8. / 'fe-secedû' 10. / 's-sâcidîn' 16. kelime) (okuma). "
 + T[11] + " (okuma). "
 + cumle(say('say 7:11 1-2', "ve le-qad xalaqnâkum", True), say('say 7:11 3-4', "summe savvernâkum")) + ' '
 + cumle(say('say 7:11 5-9', "summe qulnâ li'l-melâ'iketi'scudû li-âdeme", True), say('say 7:11 6-12', "qulnâ li'l-melâ'iketi'scudû li-âdeme fe-secedû illâ iblîs"), say('dizi 7 11 6 12', "qâle melek secede âdem secede illâ iblîs"), say('say 7:11 10-12', "fe-secedû illâ iblîs")) + ' '
 + cumle(say('say 7:11 13-16', "lem yekun mine's-sâcidîn", True), say('say 7:11 13-14', "lem yekun")) + ' ' +
 "Ölçüm xref 18:50 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B2 'xalaqnâkum' (2. kelime).",
 "◈D — D1 've' + 'le' + 'qad' + PERF + 'summe' + PERF + 'summe' + PERF + 'li' + belirli + IMPV + 'li' + özel ad + 'fe' + PERF + 'illâ' + özel ad + 'lem' + IMPF + 'min' + belirli; "
 "D2 emir; CERT ('ve le-qad' 1. kelime), EMPH ('ve le-qad' 1. kelime), IMPV ('scudû' 8. kelime), NEG ('lem' 13. kelime); D3 18:50 eşi, سجد ×3; D4 1P 6 · 2MP 4 · 3MP 2 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[11] + "; aktör adlı 'âdeme' (9. kelime; ölçüm rol mecrur), 'iblîs' (12. kelime; ölçüm rol meful); A2 yaratma ve biçim verme; meleklere Âdem'e secde emri; İblîs dışında secde edilmesi; "
 "A3 'scudû li-âdeme' (söz içi, 8-9. kelime); "
 "A4 " + BOLUM + "; bölüm açılışı; söz açılır (8. kelime); söz kapanır (9. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi haber → emir (ayetler arası).",
)

D[12] = ("◇ 'qâle mâ mene'ake ellâ tescude iz emertuk, qâle ene xayrun minhu xalaqtenî min nârin ve xalaqtehû min tîn' — "
 "PERF 3MS I. bab + 'mâ' + PERF 3MS I. bab + 2MS + 'en' + 'lâ' + IMPF 2MS I. bab + 'iz' + PERF 1S I. bab + 2MS + PERF 3MS I. bab + 'ene' + nekre 'xayr' + 'min' + 3MS + PERF 2MS I. bab + 1S + 'min' + nekre 'nâr' + 've' + PERF 2MS I. bab + 3MS + 'min' + nekre 'tîn' "
 "(ölçüm edim soru, kip INTG 1 · NEG 1; 1S 4 · 2MS 7 · 3MS 5; bab I. bab ×7). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=17 (n z=0,49); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:11 ن → 7:12 ن); "
 "ölçüm '{{2|simetri \\[6, 1, 8, 2\\]}}' — satır aynen; ölçüm '{{2|harf 63 → harf3 57, isaret 6}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen. "
 "Ölçüm INTG 1: 'mâ' (2. kelime); NEG 1: 'ellâ' (4. kelime; 'lâ'); "
 "'ellâ' (4.) kelimesindeki 'en' SUB; 'iz' (6.) T; 've xalaqtehû' (15.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) خلق ×2 ('xalaqtenî' 12. / 've xalaqtehû' 15. kelime), قول ×2 ('qâle' 1. / 'qâle' 8. kelime) (okuma). "
 + T[12] + " (okuma). "
 + cumle(say('say 7:12 2-7', "mâ mene'ake ellâ tescude iz emertuk", True), say('say 7:12 2-3', "mâ mene'ake"), say('dizi 7 12 2 3', "mâ mene'a")) + ' '
 + cumle(say('say 7:12 8-17', "qâle ene xayrun minhu xalaqtenî min nârin ve xalaqtehû min tîn", True), say('dizi 7 12 8 17', "qâle _ xayr min xalaqa min nâr xalaqa min tîn"), say('say 7:12 9-11', "ene xayrun minhu"), say('say 7:12 12-14', "xalaqtenî min nârin"), say('say 7:12 15-17', "ve xalaqtehû min tîn")) + ' ' +
 "Ölçüm xref 38:75 (emsal olarak basıldı), 38:76 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'xalaqtenî min nârin' / 've xalaqtehû min tîn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B2 'xalaqtenî' (12. kelime), 'xalaqtehû' (15. kelime).",
 "◈D — D1 PERF + 'mâ' + PERF + 'en' + 'lâ' + IMPF + 'iz' + PERF + PERF + 'ene' + nekre + 'min' + PERF + 'min' + nekre + 've' + PERF + 'min' + nekre; "
 "D2 soru; INTG ('mâ' 2. kelime), NEG ('ellâ' 4. kelime); D3 38:75 eşi, 38:76 eşi, خلق ×2, قول ×2; D4 1S 4 · 2MS 7 · 3MS 5, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[12] + "; aktör yok (ölçüm); A2 secdeden alıkoyanın sorulması; ateşten ve çamurdan yaratılış gerekçesiyle üstünlük savı; "
 "A3 'mâ mene'ake ellâ tescude iz emertuk' (söz içi, 2-7. kelime); 'ene xayrun minhu xalaqtenî min nârin ve xalaqtehû min tîn' (söz içi, 9-17. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (7. kelime, ayet içi); söz açılır (9. kelime); söz kapanır (17. kelime, ayet içi); şahıs geçişi 1 → 2 (ayetler arası); edim geçişi emir → soru (ayetler arası).",
)

D[13] = ("◇ 'qâle fe'hbit minhâ fe-mâ yekûnu leke en tetekebbera fîhâ fe'xruc inneke mine's-sâğirîn' — "
 "PERF 3MS I. bab + 'fe' + IMPV 2MS I. bab + 'min' + 3FS + 'fe' + 'mâ' + IMPF 3MS I. bab + 'li' + 2MS + 'en' + IMPF 2MS V. bab + 'fî' + 3FS + 'fe' + IMPV 2MS I. bab + 'inne' + 2MS + 'min' + belirli çoğul etken ortaç 'sâğir' "
 "(ölçüm edim emir, kip IMPV 2 · NEG 1; 2MS 5 · 3FS 2 · 3MS 2; bab I. bab ×4 · V. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=13 (n z=0,06); ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:12 ن → 7:13 ن); "
 "ölçüm '{{3|simetri \\[4, 4, 9, 1\\]}}' — satır aynen; ölçüm '{{3|harf 49 → harf3 49, isaret 0}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm IMPV 2: 'hbit' (2. kelime), 'xruc' (10. kelime); NEG 1: 'mâ' (4. kelime); "
 "'fe'hbit' (2.) kelimesindeki 'fe' SUP; 'fe-mâ' (4.) kelimesindeki 'fe' REM; 'en' (7.) SUB; 'fe'xruc' (10.) kelimesindeki 'fe' REM; 'inneke' (11.) ACC (okuma). "
 + T[13] + " (okuma). "
 + cumle(say('say 7:13 2-3', "fe'hbit minhâ", True), say('say 7:13 4-9', "fe-mâ yekûnu leke en tetekebbera fîhâ")) + ' '
 + cumle(say('say 7:13 11-13', "inneke mine's-sâğirîn", True), say('say 7:13 11-12', "inneke mine")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'tetekebbera' / 's-sâğirîn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + 'fe' + IMPV + 'min' + 'fe' + 'mâ' + IMPF + 'li' + 'en' + IMPF + 'fî' + 'fe' + IMPV + 'inne' + 'min' + belirli; "
 "D2 emir; IMPV ('hbit' 2. kelime, 'xruc' 10. kelime), NEG ('mâ' 4. kelime); D3 —; D4 2MS 5 · 3FS 2 · 3MS 2, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[13] + "; aktör yok (ölçüm); A2 inme emri; orada büyüklenmenin yeri olmadığı; çıkma emri ve aşağılananlardan sayılma; "
 "A3 'fe'hbit minhâ fe-mâ yekûnu leke en tetekebbera fîhâ fe'xruc inneke mine's-sâğirîn' (söz içi, 2-13. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (13. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi soru → emir (ayetler arası).",
)
out = ['# ── blok 7:11-13 (2026-11-24) ──', 'MEAL3 = {']
for n in range(11, 14):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M3 = {']
for n in range(11, 14):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL3); M.update(M3)']
open('/home/claude/yamalar/metin_7_11_13.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
