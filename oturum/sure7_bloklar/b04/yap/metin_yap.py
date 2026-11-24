# sûre 7 blok 4 (7:14-18) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b04/say2.txt'
os.environ['OLC'] = '/home/claude/b04/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Âdem'e secde; İblis'in mühleti; ağaç ve iniş' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|': t = t.replace(c, '\\' + c)
    return t
_AK = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[4]).group(0))
_E2 = _esc(re.search(r'esit2 → .*?BENZER · .*?BENZER', _OL[0]).group(0))
_ES = _esc(re.search(r'esmâ \S+ 15\. sırada, SON konum, MÜHÜRSÜZ', _OL[3]).group(0))
_SI = _esc(re.search(r'sayı işareti \S+', _OL[3]).group(0))
_HP = _esc(re.search(r'HAPAKS: \S+', _OL[4]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 14: "Dedi ki: Bana diriltilecekleri güne kadar mühlet ver.",
 15: "Dedi ki: Sen gerçekten mühlet verilenlerdensin.",
 16: "Dedi ki: Beni azdırmana karşılık, onlar için Senin dosdoğru yolunda mutlaka oturacağım.",
 17: "Sonra onlara mutlaka önlerinden, arkalarından, sağlarından ve sollarından geleceğim; onların çoğunu şükredenler olarak bulmayacaksın.",
 18: "Dedi ki: Oradan yerilmiş ve kovulmuş olarak çık. Onlardan kim sana uyarsa, cehennemi mutlaka sizin hepinizle dolduracağım.",
}

T = {}
T[14] = ("'qâle' 3MS (adsız; gönderge 7:11 12. kelime, 1. kelime); muhatap 2MS (adsız; söz içi; 'enzirnî' — 2. kelime); konuşan 1S eki (adsız; söz içi; 'enzirnî' — 2. kelime); "
         "'yub'asûn' 3MP (adsız; söz içi; tartışmalı; edilgen, naib-i faili zamir; anılanlar bölümde adsız — 5. kelime)")
T[15] = ("'qâle' 3MS (adsız; tartışmalı; sayı uyumsuz; gönderge 7:11 6. kelime, 1. kelime); muhatap 2MS eki (adsız; söz içi; 'inneke' — 2. kelime)")
T[16] = ("'qâle' 3MS (adsız; gönderge 7:11 12. kelime, 1. kelime); muhatap 2MS (adsız; söz içi; 'ağveytenî' — 3. kelime); konuşan 1S eki (adsız; söz içi; 'ağveytenî' — 3. kelime); konuşan 1S (adsız; söz içi; 'le-aq'udenne' — 4. kelime); "
         "'lehum' 3MP eki (adsız; söz içi; tartışmalı; anılanlar bölümde adsız — 5. kelime); muhatap 2MS eki (adsız; söz içi; 'sırâtake' — 6. kelime)")
T[17] = ("muhatap 2MS (adsız; söz içi; morph etiketi, okuma söz sahibi; 'le-âtiyennehum' — 2. kelime); 'le-âtiyennehum', 'eydîhim', 'xalfihim', 'eymânihim', 'şemâ'ilihim', 'ekserahum' 3MP eki (adsız; söz içi; gönderge 7:16 5. kelime — 2., 5., 7., 9., 11. ve 14. kelime); "
         "muhatap 2MS (adsız; söz içi; 'tecidu' — 13. kelime)")
T[18] = ("'qâle' 3MS (adsız; tartışmalı; sayı uyumsuz; gönderge 7:11 6. kelime, 1. kelime); muhatap 2MS (adsız; söz içi; 'xruc' — 2. kelime); 'minhâ' 3FS eki (adsız; söz içi; tartışmalı; anılan yer bölümde adsız — 3. kelime); "
         "'tebi'ake' 3MS (adsız; söz içi; gönderge 'men' 6. kelime, 7. kelime); muhatap 2MS eki (adsız; söz içi; 'tebi'ake' — 7. kelime); 'minhum' 3MP eki (adsız; söz içi; gönderge 7:16 5. kelime, 8. kelime); "
         "konuşan 1S (adsız; söz içi; 'le-emle'enne' — 9. kelime); muhatap 2MP eki (adsız; söz içi; 'minkum' — 11. kelime)")

D = {}
D[14] = ("◇ 'qâle enzirnî ilâ yevmi yub'asûn' — "
 "PERF 3MS I. bab + IMPV 2MS IV. bab + 1S + 'ilâ' + 'yevm' + IMPF 3MP I. bab edilgen "
 "(ölçüm edim emir, kip IMPV 1; 1S 1 · 2MS 1 · 3MP 2 · 3MS 1; bab I. bab ×2 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=5 (n z=-0,79); ölçüm '{{1|EDİLGEN 1/3 fiil, pas z=1,57}}' — satır aynen; ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:13 ن → 7:14 ن); "
 "ölçüm '{{1|harf 21 → harf3 21, isaret 0}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen; ölçüm '{{1|" + _E2 + "}}' — satır aynen (15:36 ve 38:79 emsal olarak basıldı). "
 "Ölçüm IMPV 1: 'enzirnî' (2. kelime) (okuma). "
 + T[14] + " (okuma). "
 + cumle(say('say 7:14 1-5', "qâle enzirnî ilâ yevmi yub'asûn", True), say('dizi 7 14 2 5', "yunzaru ilâ yevm be'ase"), say('say 7:14 3-5', "ilâ yevmi yub'asûn"), say('dizi 7 14 3 5', "ilâ yevm be'ase")) + ' ' +
 "Ölçüm xref 15:36 (emsal olarak basıldı), 38:79 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K2 'yevmi' (4. kelime).",
 "◈B — —",
 "◈D — D1 PERF + IMPV + 'ilâ' + 'yevm' + IMPF; "
 "D2 emir; IMPV ('enzirnî' 2. kelime); D3 15:36 eşi, 38:79 eşi; D4 1S 1 · 2MS 1 · 3MP 2 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[14] + "; aktör yok (ölçüm); A2 diriltilme gününe kadar mühlet isteği; "
 "A3 'enzirnî ilâ yevmi yub'asûn' (söz içi, 2-5. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (5. kelime, ayet içi); şahıs geçişi 2 → 3 (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[15] = ("◇ 'qâle inneke mine'l-munzarîn' — "
 "PERF 3MS I. bab + 'inne' + 2MS + 'min' + belirli çoğul edilgen ortaç 'munzar' "
 "(ölçüm edim haber, kip yok; 2MS 1 · 3MS 1; bab I. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=4 (n z=-0,89); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:14 ن → 7:15 ن); "
 "ölçüm '{{2|harf 16 → harf3 16, isaret 0}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm kip yok; 'inneke' (2.) ACC (okuma). "
 + T[15] + " (okuma). "
 + cumle(say('say 7:15 1-4', "qâle inneke mine'l-munzarîn", True), say('say 7:15 2-3', "inneke mine"), say('say 7:15 3-4', "mine'l-munzarîn")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + 'inne' + 'min' + belirli; "
 "D2 haber; kip yok; D3 —; D4 2MS 1 · 3MS 1, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[15] + "; aktör yok (ölçüm); A2 mühlet verilenlerden sayılma; "
 "A3 'inneke mine'l-munzarîn' (söz içi, 2-4. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (4. kelime, ayet içi); şahıs geçişi yok (ayetler arası); şahıs sayısında beraberlik (2MS 1 · 3MS 1 — ölçüm baskın 3); edim geçişi emir → haber (ayetler arası).",
)

D[16] = ("◇ 'qâle fe-bimâ ağveytenî le-aq'udenne lehum sırâtake'l-mustaqîm' — "
 "PERF 3MS I. bab + 'fe' + 'bi' + 'mâ' + PERF 2MS IV. bab + 1S + 'le' + IMPF 1S I. bab + 'n' + 'li' + 3MP + 'sırât' + 2MS + belirli etken ortaç 'mustaqîm' "
 "(ölçüm edim haber, kip EMPH 2; 1S 2 · 2MS 3 · 3MP 1 · 3MS 1; bab I. bab ×2 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=7 (n z=-0,58); ölçüm '{{3|fâsıla " + _F[2] + " → م, N sınıfı}}' — satır aynen (7:15 ن → 7:16 م); "
 "ölçüm '{{3|harf 35 → harf3 35, isaret 0}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm EMPH 2: 'le-aq'udenne' (4. kelime; 'le' ve 'n'); "
 "'fe-bimâ' (2.) kelimesindeki 'fe' REM, 'mâ' REL (okuma). "
 + T[16] + " (okuma). "
 + cumle(say('say 7:16 2-3', "fe-bimâ ağveytenî", True), say('say 7:16 4-7', "le-aq'udenne lehum sırâtake'l-mustaqîm")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + 'fe' + 'bi' + 'mâ' + PERF + 'le' + IMPF + 'li' + izafet + belirli; "
 "D2 haber; EMPH ('le-aq'udenne' 4. kelime); D3 —; D4 1S 2 · 2MS 3 · 3MP 1 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[16] + "; aktör yok (ölçüm); A2 azdırılma gerekçesiyle dosdoğru yolda onlar için oturma andı; "
 "A3 'fe-bimâ ağveytenî le-aq'udenne lehum sırâtake'l-mustaqîm' (söz içi, 2-7. kelime; söz ayet sonunda kapanmıyor); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); şahıs geçişi 3 → 2 (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[17] = ("◇ 'summe le-âtiyennehum min beyni eydîhim ve min xalfihim ve 'an eymânihim ve 'an şemâ'ilihim, ve lâ tecidu ekserahum şâkirîn' — "
 "'summe' + 'le' + IMPF 2MS I. bab + 3MP + 'min' + 'beyn' + çoğul 'yed' + 3MP + 've' + 'min' + 'xalf' + 3MP + 've' + ''an' + çoğul 'yemîn' + 3MP + 've' + ''an' + çoğul 'şemâ'il' + 3MP + 've' + 'lâ' + IMPF 2MS I. bab + 'ekser' + 3MP + çoğul etken ortaç 'şâkir' "
 "(ölçüm edim haber, kip EMPH 1 · NEG 1; 2MS 2 · 3MP 6; bab I. bab ×2). "
 "Allah lafzı yok; Rab yok; ölçüm '{{4|" + _ES + "}}' — satır aynen; "
 "esma_kayit çıktısı 'mühür EVET ton cemâl' — ölçüm MÜHÜRSÜZ ile uyuşmuyor (araç tanımı farkı; muhur_el hayır — ölçümle uyuşuyor); "
 "esma_el kaydı 'degil' — 've lâ tecidu ekserahum şâkirîn', kural 'esmâ adı esmâ dışı göndergeyle → degil' (şükreden insanlar) (okuma); aktör yok (ölçüm). "
 "Ölçüm 'yıldız yok' — satır aynen; n=15 (n z=0,27); ölçüm '{{4|fâsıla " + _F[3] + " → ن, N sınıfı}}' — satır aynen (7:16 م → 7:17 ن); "
 "ölçüm '{{4|" + _SI + "}}' — satır aynen; ölçüm '{{4|simetri \\[3, 1, 6, 1\\]}}' — satır aynen; ölçüm '{{4|harf 67 → harf3 65, isaret 2}}' — satır aynen; ölçüm '{{4|dış düğüm 0}}' — satır aynen. "
 "Ölçüm EMPH 1: 'le-âtiyennehum' (2. kelime; 'le'); NEG 1: 'lâ' (12. kelime); "
 "'summe' (1.) CONJ; 've min' (6.) kelimesindeki 've' CONJ; 've 'an' (8.) kelimesindeki 've' CONJ; 've 'an' (10.) kelimesindeki 've' CONJ; 've lâ' (12.) kelimesindeki 've' CONJ (okuma). "
 "Morph 'le-âtiyennehum' (2. kelime) fiilini 2MS etiketliyor, ölçüm şahıs sayımı da öyle; okuma konuşan 1S (söz 7:16'dan sürüyor) (okuma). "
 + T[17] + " (okuma). "
 + cumle(say('say 7:17 1-11', "summe le-âtiyennehum min beyni eydîhim ve min xalfihim ve 'an eymânihim ve 'an şemâ'ilihim", True), say('say 7:17 3-5', "min beyni eydîhim"), say('say 7:17 4-7', "beyni eydîhim ve min xalfihim")) + ' '
 + cumle(say('say 7:17 12-15', "ve lâ tecidu ekserahum şâkirîn", True), say('say 7:17 12-13', "ve lâ tecidu")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'beyni eydîhim' / 'xalfihim'; 'eymânihim' / 'şemâ'ilihim' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B3 'eydîhim' (5. kelime).",
 "◈D — D1 'summe' + 'le' + IMPF + 'min' + izafet + 've' + 'min' + izafet + 've' + ''an' + izafet + 've' + ''an' + izafet + 've' + 'lâ' + IMPF + izafet + 'şâkir'; "
 "D2 haber; EMPH ('le-âtiyennehum' 2. kelime), NEG ('lâ' 12. kelime); D3 —; D4 2MS 2 · 3MP 6, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[17] + "; aktör yok (ölçüm); A2 dört yönden gelme andı; çoğunun şükreden bulunmayacağı; "
 "A3 söz sürüyor (7:16 2. kelimeden; 1-15. kelime); "
 "A4 " + BOLUM + "; söz kapanır (15. kelime); şahıs geçişi 2 → 3 (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[18] = ("◇ 'qâle'xruc minhâ mez'ûmen medhûrâ, le-men tebi'ake minhum le-emle'enne cehenneme minkum ecma'în' — "
 "PERF 3MS I. bab + IMPV 2MS I. bab + 'min' + 3FS + nekre edilgen ortaç 'mez'ûm' + nekre edilgen ortaç 'medhûr' + 'le' + 'men' + PERF 3MS I. bab + 2MS + 'min' + 3MP + 'le' + IMPF 1S I. bab + 'n' + özel ad 'cehennem' + 'min' + 2MP + çoğul 'ecma'' "
 "(ölçüm edim emir, şart, kip COND 1 · EMPH 3 · IMPV 1; 1S 1 · 2MP 1 · 2MS 2 · 3FS 1 · 3MP 1 · 3MS 2; bab I. bab ×4). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); ölçüm '{{5|" + _AK + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=12 (n z=-0,04); ölçüm '{{5|" + _HP + "}}' — satır aynen (kök bu blokta tabloya eklendi); ölçüm '{{5|hapaks z=3,28}}' — satır aynen; "
 "ölçüm '{{5|fâsıla " + _F[4] + " → ن, N sınıfı}}' — satır aynen (7:17 ن → 7:18 ن); "
 "ölçüm '{{5|harf 57 → harf3 54, isaret 3}}' — satır aynen; ölçüm '{{5|dış düğüm 0}}' — satır aynen. "
 "Ölçüm COND 1: 'men' (6. kelime); EMPH 3: 'le-men' (6. kelime; 'le'), 'le-emle'enne' (9. kelime; 'le' ve 'n'); IMPV 1: 'xruc' (2. kelime) (okuma). "
 + T[18] + " (okuma). "
 + cumle(say('say 7:18 2-5', "xruc minhâ mez'ûmen medhûrâ", True)) + ' '
 + cumle(say('say 7:18 6-8', "le-men tebi'ake minhum", True), say('say 7:18 7-8', "tebi'ake minhum")) + ' '
 + cumle(say('say 7:18 9-12', "le-emle'enne cehenneme minkum ecma'în", True), say('say 7:18 9-10', "le-emle'enne cehenneme")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + IMPV + 'min' + nekre + nekre + 'le' + 'men' + PERF + 'min' + 'le' + IMPF + özel ad + 'min' + 'ecma''; "
 "D2 emir, şart; COND ('men' 6. kelime), EMPH ('le-men' 6. kelime, 'le-emle'enne' 9. kelime), IMPV ('xruc' 2. kelime); D3 —; D4 1S 1 · 2MP 1 · 2MS 2 · 3FS 1 · 3MP 1 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[18] + "; aktör adlı 'cehenneme' (10. kelime; ölçüm rol meful); A2 yerilmiş ve kovulmuş olarak çıkma emri; uyanlarla cehennemin doldurulacağı andı; "
 "A3 'xruc minhâ mez'ûmen medhûrâ, le-men tebi'ake minhum le-emle'enne cehenneme minkum ecma'în' (söz içi, 2-12. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (12. kelime, ayet içi); şart → cevap (ayet içi; COND 'men' 6. kelime: 'le-men tebi'ake minhum' / 'le-emle'enne' (9. kelime)); muhatap geçişi 2MS → 2MP (ayet içi, 'tebi'ake' / 'minkum'); şahıs geçişi yok (ayetler arası); edim geçişi haber → emir, şart (ayetler arası).",
)
out = ['# ── blok 7:14-18 (2026-11-24) ──', 'MEAL4 = {']
for n in range(14, 19):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M4 = {']
for n in range(14, 19):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL4); M.update(M4)']
open('/home/claude/yamalar/metin_7_14_18.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
