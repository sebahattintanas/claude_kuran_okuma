# sûre 7 blok 5 (7:19-21) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b05/say2.txt'
os.environ['OLC'] = '/home/claude/b05/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Âdem'e secde; İblis'in mühleti; ağaç ve iniş' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|+': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))
_AK2 = _esc(re.search(r'aktör: adlı .*?rol fail\)', _OL[1]).group(0))
_E2 = _esc(re.search(r'esit2 → 2:35 oran \S+ kademe BENZER', _OL[0]).group(0))
_SI = _esc(re.search(r'sayı işareti \S+', _OL[0]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 19: "Ey Âdem, sen ve eşin bahçede oturun; dilediğiniz yerden yiyin; ama şu ağaca yaklaşmayın, yoksa zalimlerden olursunuz.",
 20: "Derken şeytan onlara vesvese verdi; kendilerinden gizlenen çirkin yerlerini onlara açmak için. Dedi ki: Rabbiniz size şu ağacı ancak iki melek olursunuz ya da ebedî kalanlardan olursunuz diye yasakladı.",
 21: "Onlara yemin etti: Ben gerçekten size öğüt verenlerdenim.",
}

T = {}
T[19] = ("muhatap 2MS (adsız; söz içi; 'skun', 'ente' — 2. ve 3. kelime); muhatap 2MS eki (adsız; söz içi; 've zevcuke' — 4. kelime); muhatap 2MD (adsız; söz içi; 'fe-kulâ' — 6. kelime); muhatap 2D eki (adsız; söz içi; 'fe-kulâ' — 6. kelime); "
         "muhatap 2D (adsız; söz içi; 'şi'tumâ', 'taqrabâ', 'fe-tekûnâ' — 9., 11. ve 14. kelime)")
T[20] = ("'fe-vesvese' 3MS (fiil uyumu; 1. kelime — fail 3. kelime); 'lehume', 'lehumâ', ''anhumâ', 'sev'âtihimâ' 3D eki (adsız; gönderge 7:19 6. kelime — 2., 5., 8. ve 10. kelime); "
         "'li-yubdiye' 3MS (adsız; gönderge 'ş-şeytânu' 3. kelime, 4. kelime); 'vûriye' 3MS (adsız; edilgen, naib-i faili 'mâ' 6. kelime, 7. kelime); 've qâle' 3MS (adsız; gönderge 'ş-şeytânu' 3. kelime, 11. kelime); "
         "'nehâkumâ' 3MS (fiil uyumu; söz içi; 13. kelime — fail 14. kelime); muhatap 2D eki (adsız; söz içi; 'nehâkumâ', 'rabbukumâ' — 13. ve 14. kelime); muhatap 2D (adsız; söz içi; 'tekûnâ', 'tekûnâ' — 20. ve 23. kelime)")
T[21] = ("'ve qâsemehumâ' 3MS (adsız; gönderge 7:20 3. kelime, 1. kelime); 've qâsemehumâ' 3D eki (adsız; gönderge 7:19 6. kelime, 1. kelime); konuşan 1S eki (adsız; söz içi; 'innî' — 2. kelime); muhatap 2D eki (adsız; söz içi; 'lekumâ' — 3. kelime)")

D = {}
D[19] = ("◇ 've yâ âdemu'skun ente ve zevcuke'l-cennete fe-kulâ min haysu şi'tumâ ve lâ taqrabâ hâzihi'ş-şecerate fe-tekûnâ mine'z-zâlimîn' — "
 "'ve' + 'yâ' + özel ad 'âdem' + IMPV 2MS I. bab + 'ente' + 've' + 'zevc' + 2MS + belirli 'cenne' + 'fe' + IMPV 2MD I. bab + 'min' + 'haysu' + PERF 2D I. bab + 've' + 'lâ' + IMPF 2D I. bab + 'hâ' + 'zâ' + belirli 'şecera' + 'fe' + IMPF 2D I. bab + 'min' + belirli çoğul etken ortaç 'zâlim' "
 "(ölçüm edim emir, yasak, nida, kip IMPV 2 · PRO 1 · VOC 1; 2D 7 · 2MD 1 · 2MS 3; bab I. bab ×5). "
 "Allah lafzı yok; Rab yok; esmâ yok (ölçüm); ölçüm '{{1|" + _AK1 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=16 (n z=0,38); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:18 ن → 7:19 ن); "
 "ölçüm '{{1|" + _SI + "}}' — satır aynen; ölçüm '{{1|harf 69 → harf3 69, isaret 0}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen; ölçüm '{{1|İÇ düğüm 1}}' — satır aynen; "
 "ölçüm '{{1|" + _E2 + "}}' — satır aynen (2:35 emsal olarak basıldı). "
 "Ölçüm IMPV 2: 'skun' (2. kelime), 'kulâ' (6. kelime); PRO 1: 'lâ' (10. kelime); VOC 1: 'yâ' (1. kelime); ölçüm biçim DIKKAT + NEHY; "
 "'ve yâ âdemu' (1.) kelimesindeki 've' CONJ; 've zevcuke' (4.) kelimesindeki 've' CONJ; 'fe-kulâ' (6.) kelimesindeki 'fe' CONJ; 've lâ' (10.) kelimesindeki 've' CONJ; 'hâzihi' (12.) kelimesindeki 'hâ' ATT; 'fe-tekûnâ' (14.) kelimesindeki 'fe' CAUS (okuma). "
 + T[19] + " (okuma). "
 + cumle(say('say 7:19 2-5', "skun ente ve zevcuke'l-cennete", True), say('dizi 7 19 2 5', "sekene _ zevc cenne"), say('dizi 7 19 1 6', "âdem sekene _ zevc cenne ekele")) + ' '
 + cumle(say('say 7:19 6-9', "fe-kulâ min haysu şi'tumâ", True), say('say 7:19 8-16', "haysu şi'tumâ ve lâ taqrabâ hâzihi'ş-şecerate fe-tekûnâ mine'z-zâlimîn"), say('dizi 7 19 8 16', "haysu şâ'e lâ yaqrabu zâ şecera kâne min zâlim")) + ' '
 + cumle(say('say 7:19 10-13', "ve lâ taqrabâ hâzihi'ş-şecerate", True), say('say 7:19 14-16', "fe-tekûnâ mine'z-zâlimîn"), say('say 7:19 10-16', "ve lâ taqrabâ hâzihi'ş-şecerate fe-tekûnâ mine'z-zâlimîn"), say('dizi 7 19 10 16', "lâ yaqrabu zâ şecera kâne min zâlim")) + ' ' +
 "Ölçüm xref 2:35 (emsal olarak basıldı), okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'ş-şecerate' (13. kelime); B2 'zevcuke' (4. kelime); B3 —; B4 —.",
 "◈D — D1 've' + 'yâ' + özel ad + IMPV + 'ente' + 've' + izafet + belirli + 'fe' + IMPV + 'min' + 'haysu' + PERF + 've' + 'lâ' + IMPF + 'zâ' + belirli + 'fe' + IMPF + 'min' + belirli; "
 "D2 emir, yasak, nida; IMPV ('skun' 2. kelime, 'kulâ' 6. kelime), PRO ('lâ' 10. kelime), VOC ('yâ' 1. kelime); D3 2:35 eşi; D4 2D 7 · 2MD 1 · 2MS 3, sahset ['2'], iltifât 0.",
 "◈A — A1 " + T[19] + "; aktör adlı 'âdemu' (1. kelime; ölçüm rol fail+muhatap), 'l-cennete' (5. kelime; ölçüm rol meful); A2 Âdem ve eşine bahçede oturma ve dilediği yerden yeme izni; ağaca yaklaşma yasağı ve zalimlerden olma uyarısı; "
 "A3 've yâ âdemu'skun ente ve zevcuke'l-cennete fe-kulâ min haysu şi'tumâ ve lâ taqrabâ hâzihi'ş-şecerate fe-tekûnâ mine'z-zâlimîn' (söz biçimli içerik, 1. kelimeden); "
 "A4 " + BOLUM + "; nidâ ('yâ âdemu' 1. kelime); cevap edatı kapsam dışı (morph CAUS 'fe-tekûnâ' 14. kelime — sebebiyye; şart / soru yok); muhatap geçişi 2MS → 2D (ayet içi, 'skun' / 'fe-kulâ'); şahıs geçişi 3 → 2 (ayetler arası); edim geçişi emir, şart → emir, yasak, nida (ayetler arası).",
)

D[20] = ("◇ 'fe-vesvese lehume'ş-şeytânu li-yubdiye lehumâ mâ vûriye 'anhumâ min sev'âtihimâ ve qâle mâ nehâkumâ rabbukumâ 'an hâzihi'ş-şecerati illâ en tekûnâ melekeyni ev tekûnâ mine'l-xâlidîn' — "
 "'fe' + PERF 3MS I. bab + 'li' + 3D + belirli 'şeytân' + 'li' + IMPF 3MS IV. bab + 'li' + 3D + 'mâ' + PERF 3MS III. bab edilgen + ''an' + 3D + 'min' + çoğul 'sev'e' + 3D + 've' + PERF 3MS I. bab + 'mâ' + PERF 3MS I. bab + 2D + 'rabb' + 2D + ''an' + 'hâ' + 'zâ' + belirli 'şecera' + 'illâ' + 'en' + IMPF 2D I. bab + ikil 'melek' + 'ev' + IMPF 2D I. bab + 'min' + belirli çoğul etken ortaç 'xâlid' "
 "(ölçüm edim haber, kip NEG 1 · RES 1; 2D 6 · 3D 4 · 3MS 5; bab I. bab ×5 · III. bab ×1 · IV. bab ×1). "
 "Allah lafzı yok; Rab 14. sırada (ölçüm rab z=0,53); esmâ yok (ölçüm); ölçüm '{{2|" + _AK2 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=25 (n z=1,34); ölçüm '{{2|EDİLGEN 1/7 fiil, pas z=0,48}}' — satır aynen; ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:19 ن → 7:20 ن); "
 "ölçüm '{{2|simetri \\[6, 5, 15, 2\\]}}' — satır aynen; ölçüm '{{2|harf 103 → harf3 102, isaret 1}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm NEG 1: 'mâ' (12. kelime); RES 1: 'illâ' (18. kelime); ölçüm biçim DIKKAT + HASR; "
 "'fe-vesvese' (1.) kelimesindeki 'fe' REM; 'li-yubdiye' (4.) kelimesindeki 'li' PRP; 'mâ' (6.) REL; 've qâle' (11.) kelimesindeki 've' CONJ; 'hâzihi' (16.) kelimesindeki 'hâ' ATT; 'en' (19.) SUB; 'ev' (22.) CONJ (okuma). "
 "Kök ikilemesi (ölçüm) كون ×2 ('tekûnâ' 20. / 'tekûnâ' 23. kelime) (okuma). "
 + T[20] + " (okuma). "
 + cumle(say('say 7:20 1-3', "fe-vesvese lehume'ş-şeytânu", True), say('say 7:20 4-10', "li-yubdiye lehumâ mâ vûriye 'anhumâ min sev'âtihimâ")) + ' '
 + cumle(say('say 7:20 12-25', "mâ nehâkumâ rabbukumâ 'an hâzihi'ş-şecerati illâ en tekûnâ melekeyni ev tekûnâ mine'l-xâlidîn", True), say('say 7:20 18-19', "illâ en")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'li-yubdiye' / 'vûriye' — ayetler arası: yok.",
 "◈K — —",
 "◈B — B1 'ş-şecerati' (17. kelime).",
 "◈D — D1 'fe' + PERF + 'li' + belirli + 'li' + IMPF + 'li' + 'mâ' + PERF + ''an' + 'min' + izafet + 've' + PERF + 'mâ' + PERF + izafet + ''an' + 'zâ' + belirli + 'illâ' + 'en' + IMPF + 'melek' + 'ev' + IMPF + 'min' + belirli; "
 "D2 haber; NEG ('mâ' 12. kelime), RES ('illâ' 18. kelime); D3 كون ×2; D4 2D 6 · 3D 4 · 3MS 5, sahset ['2', '3'], iltifât 0.",
 "◈A — A1 " + T[20] + "; aktör adlı 'ş-şeytânu' (3. kelime; ölçüm rol fail — 'fe-vesvese' faili); A2 şeytanın gizlenen çirkin yerleri açmak için vesvesesi; yasağın melek ya da ebedî olma gerekçesine bağlanması; "
 "A3 'mâ nehâkumâ rabbukumâ 'an hâzihi'ş-şecerati illâ en tekûnâ melekeyni ev tekûnâ mine'l-xâlidîn' (söz içi, 12-25. kelime); "
 "A4 " + BOLUM + "; söz açılır (12. kelime); söz kapanır (25. kelime, ayet içi); şahıs geçişi yok (ayetler arası); şahıs sayısında toplam farkı (2D 6 · 3. şahıs 9 — ölçüm baskın 2); edim geçişi emir, yasak, nida → haber (ayetler arası).",
)

D[21] = ("◇ 've qâsemehumâ innî lekumâ le-mine'n-nâsihîn' — "
 "'ve' + PERF 3MS III. bab + 3D + 'inne' + 1S + 'li' + 2D + 'le' + 'min' + belirli çoğul etken ortaç 'nâsih' "
 "(ölçüm edim haber, kip EMPH 1; 1S 1 · 2D 1 · 3D 1 · 3MS 1; bab III. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=5 (n z=-0,79); ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:20 ن → 7:21 ن); "
 "ölçüm '{{3|harf 25 → harf3 25, isaret 0}}' — satır aynen; ölçüm '{{3|dış düğüm 0}}' — satır aynen. "
 "Ölçüm EMPH 1: 'le-mine' (4. kelime; 'le'); ölçüm biçim QASEM; "
 "'ve qâsemehumâ' (1.) kelimesindeki 've' CONJ; 'innî' (2.) ACC (okuma). "
 + T[21] + " (okuma). "
 + cumle(say('say 7:21 2-5', "innî lekumâ le-mine'n-nâsihîn", True), say('say 7:21 1-5', "ve qâsemehumâ innî lekumâ le-mine'n-nâsihîn")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + PERF + 'inne' + 'li' + 'le' + 'min' + belirli; "
 "D2 haber; EMPH ('le-mine' 4. kelime); D3 —; D4 1S 1 · 2D 1 · 3D 1 · 3MS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[21] + "; aktör yok (ölçüm); A2 öğüt verenlerden olduğuna dair yemin; "
 "A3 'innî lekumâ le-mine'n-nâsihîn' (söz biçimli içerik, 2. kelimeden); "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi yok (ayetler arası).",
)
out = ['# ── blok 7:19-21 (2026-11-25) ──', 'MEAL5 = {']
for n in range(19, 22):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M5 = {']
for n in range(19, 22):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL5); M.update(M5)']
open('/home/claude/yamalar/metin_7_19_21.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
