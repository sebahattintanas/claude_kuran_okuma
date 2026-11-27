# sûre 7 blok 22 metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b22/say2.txt'
os.environ['OLC'] = '/home/claude/b22/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Sâlih ve Semûd; Lût ve kavmi' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK2 = _esc(re.search(r'aktör: adlı .*?rol meful\+muhatap\)', _OL[1]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 76: "Büyüklenenler dedi ki: Gerçekten biz sizin iman ettiğinizi inkâr edenleriz.",
 77: "Bunun üzerine deveyi kestiler ve Rablerinin emrine baş kaldırdılar ve dediler ki: Ey Sâlih, elçilerdensen bize vaat ettiğin şeyi getir.",
 78: "Bunun üzerine onları sarsıntı yakaladı ve yurtlarında diz üstü çöküp kaldılar.",
 79: "Bunun üzerine onlardan yüz çevirdi ve dedi ki: Ey kavmim, andolsun size Rabbimin risaletini tebliğ ettim ve size öğüt verdim; fakat siz öğüt verenleri sevmiyorsunuz.",
}

T = {}
T[76] = ("'qâle' 3MS (fiil uyumu; 1. kelime — fail 2. kelime); 'stekberû' 3MP (adsız; gönderge 'llezîne' 2. kelime, 3. kelime); konuşan 1P eki (adsız; söz içi; 'innâ' — 4. kelime); "
         "muhatap 2MP (adsız; söz içi; 'âmentum' — 6. kelime); 'bihî' 3MS eki (adsız; söz içi; gönderge 'llezî' 5. kelime, 7. kelime)")
T[77] = ("''aqarû', ''atev', 'qâlû' 3MP (adsız; gönderge 7:76 2. kelime — 1., 3. ve 7. kelime); 'rabbihim' 3MP eki (adsız; gönderge 7:76 2. kelime, 6. kelime); "
         "muhatap 2MS (adsız; söz içi; 'i'tinâ', 'te'idunâ', 'kunte' — 9., 11. ve 13. kelime); konuşan 1P eki (adsız; söz içi; 'i'tinâ', 'te'idunâ' — 9. ve 11. kelime)")
T[78] = ("'exazethumu' 3FS (fiil uyumu; 1. kelime — fail 2. kelime); 'exazethumu' 3MP eki (adsız; gönderge 7:76 2. kelime, 1. kelime); 'esbahû' 3MP (adsız; gönderge 7:76 2. kelime, 3. kelime); "
         "'dârihim' 3MP eki (adsız; gönderge 7:76 2. kelime, 5. kelime)")
T[79] = ("'tevellâ', 'qâle' 3MS (adsız; gönderge 7:77 8. kelime — 1. ve 3. kelime); ''anhum' 3MP eki (adsız; gönderge 7:76 2. kelime, 2. kelime); "
         "konuşan 1S eki (adsız; söz içi; 'qavmi', 'rabbî' — 4. ve 8. kelime); konuşan 1S (adsız; söz içi; 'ebleğtukum', 'nasahtu' — 6. ve 9. kelime); "
         "muhatap 2MP eki (adsız; söz içi; 'ebleğtukum', 'lekum' — 6. ve 10. kelime); muhatap 2MP (adsız; söz içi; 'tuhibbûne' — 13. kelime)")

D = {}
D[76] = ("◇ 'qâle'llezîne'stekberû innâ bi'llezî âmentum bihî kâfirûn' — "
 "PERF 3MS I. bab + 'ellezî' + PERF 3MP X. bab + 'inne' + 1P + 'bi' + 'ellezî' + PERF 2MP IV. bab + 'bi' + 3MS + çoğul etken ortaç 'kâfir' "
 "(ölçüm edim haber, kip yok; 1P 1 · 2MP 2 · 3MP 2 · 3MS 2; bab I. bab ×1 · IV. bab ×1 · X. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=8 (n z=-0,47); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:75 ن → 7:76 ن); "
 "ölçüm '{{1|simetri \\[3, 2, 5, 1\\]}}' — satır aynen; ölçüm '{{1|harf 39 → harf3 37, isaret 2}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "'llezîne' (2.) REL; 'innâ' (4.) ACC; 'bi'llezî' (5.) P + REL (okuma). "
 + T[76] + " (okuma). "
 + cumle(say('say 7:76 1-3', "qâle'llezîne'stekberû", True), say('say 7:76 4-8', "innâ bi'llezî âmentum bihî kâfirûn", True)) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'âmentum' / 'kâfirûn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 PERF + 'ellezî' + PERF + 'inne' + 'bi' + 'ellezî' + PERF + 'bi' + çoğul; "
 "D2 haber; kip yok; D3 —; D4 1P 1 · 2MP 2 · 3MP 2 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[76] + "; aktör yok (ölçüm); A2 büyüklenenlerin iman edilen şeyi inkâr edişi; "
 "A3 'innâ bi'llezî âmentum bihî kâfirûn' (söz içi, 4-8. kelime); "
 "A4 " + BOLUM + "; söz açılır (4. kelime); söz kapanır (8. kelime, ayet içi); şahıs geçişi yok (ayetler arası); edim geçişi soru → haber (ayetler arası).",
)

D[77] = ("◇ 'fe-'aqarû'n-nâqate ve 'atev 'an emri rabbihim ve qâlû yâ sâlihu i'tinâ bi-mâ te'idunâ in kunte mine'l-murselîn' — "
 "'fe' + PERF 3MP I. bab + belirli 'nâqa' + 've' + PERF 3MP I. bab + ''an' + 'emr' + 'rabb' + 3MP + 've' + PERF 3MP I. bab + 'yâ' + özel ad 'sâlih' + IMPV 2MS I. bab + 1P + 'bi' + 'mâ' + IMPF 2MS I. bab + 1P + 'in' + PERF 2MS I. bab + 'min' + belirli çoğul edilgen ortaç 'mursel' "
 "(ölçüm edim emir, nida, şart, kip COND 1 · IMPV 1 · VOC 1; 1P 2 · 2MS 4 · 3MP 7; bab I. bab ×6). "
 "Allah lafzı yok; Rab 6. sırada (ölçüm rab z=1,10); esmâ yok (ölçüm); ölçüm '{{2|" + _AK2 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=15 (n z=0,27); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:76 ن → 7:77 ن); "
 "ölçüm '{{2|harf 67 → harf3 64, isaret 3}}' — satır aynen; ölçüm '{{2|dış düğüm 4}}' — satır aynen; ölçüm '{{2|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 'in' (12. kelime); IMPV 1: 'i'tinâ' (9. kelime); VOC 1: 'yâ sâlihu' (8. kelime; 'yâ'); "
 "'fe-'aqarû' (1.) kelimesindeki 'fe' REM; 've 'atev' (3.) kelimesindeki 've' CONJ; 've qâlû' (7.) kelimesindeki 've' CONJ; 'bi-mâ' (10.) P + REL (okuma). "
 + T[77] + " (okuma). "
 + cumle(say('say 7:77 1-2', "fe-'aqarû'n-nâqate", True), say('say 7:77 3-6', "ve 'atev 'an emri rabbihim", True), say('say 7:77 4-6', "'an emri rabbihim"), say('dizi 7 77 4 6', "'an emr rabb"), say('dizi 7 77 3 6', "'ate 'an emr rabb")) + ' '
 + cumle(say('say 7:77 9-11', "i'tinâ bi-mâ te'idunâ", True), say('say 7:77 12-15', "in kunte mine'l-murselîn", True), say('say 7:77 9-14', "i'tinâ bi-mâ te'idunâ in kunte mine"), say('dizi 7 77 9 14', "etâ mâ ve'ade in kâne min"), say('say 7:77 12-14', "in kunte mine"), say('dizi 7 77 12 14', "in kâne min")) + ' ' +
 "Ölçüm xref 7:70 (basılmış), 11:32 (basılmış), 46:22 (basılmış), 51:44 (emsal olarak basıldı), okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'etâ mâ ve'ade in kâne min' süzgeç GEÇER; 'in kâne min' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'fe' + PERF + belirli + 've' + PERF + ''an' + izafet + izafet + 've' + PERF + 'yâ' + özel ad + IMPV + 'bi' + 'mâ' + IMPF + 'in' + PERF + 'min' + belirli; "
 "D2 emir, nida, şart; COND ('in' 12. kelime), IMPV ('i'tinâ' 9. kelime), VOC ('yâ sâlihu' 8. kelime); D3 51:44 eşi; D4 1P 2 · 2MS 4 · 3MP 7, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[77] + "; aktör adlı 'yâ sâlihu' (8. kelime; ölçüm rol meful+muhatap); A2 devenin kesilişi; Rablerinin emrine baş kaldırış; Sâlih'ten vaat edilenin getirilmesinin istenişi; "
 "A3 'yâ sâlihu i'tinâ bi-mâ te'idunâ in kunte mine'l-murselîn' (söz içi, 8-15. kelime); "
 "A4 " + BOLUM + "; söz açılır (8. kelime); söz kapanır (15. kelime, ayet içi); şart → cevap (ayet içi; COND 'in' 12. kelime: 'in kunte mine'l-murselîn' / 'i'tinâ' (9. kelime) — cevap öne alınmış); şahıs geçişi yok (ayetler arası); edim geçişi haber → emir, nida, şart (ayetler arası).",
)

D[78] = ("◇ 'fe-exazethumu'r-racfetu fe-esbahû fî dârihim câsimîn' — "
 "'fe' + PERF 3FS I. bab + 3MP + belirli 'racfe' + 'fe' + PERF 3MP IV. bab + 'fî' + 'dâr' + 3MP + çoğul etken ortaç 'câsim' "
 "(ölçüm edim haber, kip yok; 3FS 1 · 3MP 4; bab I. bab ×1 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=6 (n z=-0,68); ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:77 ن → 7:78 ن); "
 "ölçüm '{{3|harf 33 → harf3 32, isaret 1}}' — satır aynen; ölçüm '{{3|dış düğüm 3}}' — satır aynen. "
 "Ölçüm esit2: 29:37 (oran 0,8986, kademe BENZER) ve basılmamış eş (kademe TAM) (okuma). "
 "'fe-exazethumu' (1.) kelimesindeki 'fe' REM; 'fe-esbahû' (3.) kelimesindeki 'fe' REM (okuma). "
 + T[78] + " (okuma). "
 + cumle(say('say 7:78 1-2', "fe-exazethumu'r-racfetu", True), say('say 7:78 3-6', "fe-esbahû fî dârihim câsimîn", True), say('say 7:78 1-6', "fe-exazethumu'r-racfetu fe-esbahû fî dârihim câsimîn"), say('dizi 7 78 1 6', "exaze racfe esbaha fî dâr câsim")) + ' ' +
 "Ölçüm xref 29:37 (emsal olarak basıldı), okunmuş 2 ayet ve okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıbı: 'exaze racfe esbaha fî dâr câsim' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'fe' + PERF + belirli + 'fe' + PERF + 'fî' + izafet + çoğul; "
 "D2 haber; kip yok; D3 29:37 eşi; D4 3FS 1 · 3MP 4, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[78] + "; aktör yok (ölçüm); A2 sarsıntının yakalayışı; yurtlarında diz üstü çöküp kalış; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi emir, nida, şart → haber (ayetler arası).",
)

D[79] = ("◇ 'fe-tevellâ 'anhum ve qâle yâ qavmi le-qad ebleğtukum risâlete rabbî ve nasahtu lekum ve lâkin lâ tuhibbûne'n-nâsihîn' — "
 "'fe' + PERF 3MS V. bab + ''an' + 3MP + 've' + PERF 3MS I. bab + 'yâ' + 'qavm' + 1S + 'le' + 'qad' + PERF 1S IV. bab + 2MP + 'risâle' + 'rabb' + 1S + 've' + PERF 1S I. bab + 'li' + 2MP + 've' + 'lâkin' + 'lâ' + IMPF 2MP IV. bab + belirli çoğul etken ortaç 'nâsih' "
 "(ölçüm edim nida, kip CERT 1 · EMPH 1 · NEG 1 · VOC 1; 1S 6 · 2MP 4 · 3MP 1 · 3MS 2; bab I. bab ×2 · IV. bab ×2 · V. bab ×1). "
 "Allah lafzı yok; Rab 8. sırada (ölçüm rab z=1,20); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=14 (n z=0,17); ölçüm '{{4|fâsıla " + _F[3] + " → ن, N sınıfı}}' — satır aynen (7:78 ن → 7:79 ن); "
 "ölçüm '{{4|harf 61 → harf3 61, isaret 0}}' — satır aynen; ölçüm '{{4|dış düğüm 1}}' — satır aynen; ölçüm '{{4|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm CERT 1: 'le-qad' (5. kelime; 'qad'); EMPH 1: 'le-qad' (5. kelime; 'le'); NEG 1: 'lâ' (12. kelime); VOC 1: 'yâ qavmi' (4. kelime; 'yâ'); "
 "'fe-tevellâ' (1.) kelimesindeki 'fe' REM; 've qâle' (3.) kelimesindeki 've' CONJ; 've nasahtu' (9.) kelimesindeki 've' CONJ; 've lâkin' (11.) kelimesindeki 've' REM, 'lâkin' AMD (okuma). "
 "Kök ikilemesi (ölçüm) نصح ×2 ('nasahtu' 9. / 'n-nâsihîn' 14. kelime) (okuma). "
 + T[79] + " (okuma). "
 + cumle(say('say 7:79 1-2', "fe-tevellâ 'anhum", True), say('say 7:79 1-10', "fe-tevellâ 'anhum ve qâle yâ qavmi le-qad ebleğtukum risâlete rabbî ve nasahtu lekum"), say('dizi 7 79 1 10', "tevellâ 'an qâle qavm qad ebleğu risâle rabb nesahu _")) + ' '
 + cumle(say('say 7:79 5-8', "le-qad ebleğtukum risâlete rabbî", True), say('say 7:79 9-10', "ve nasahtu lekum", True), say('say 7:79 7-10', "risâlete rabbî ve nasahtu lekum"), say('dizi 7 79 7 10', "risâle rabb nesahu _")) + ' '
 + cumle(say('say 7:79 11-14', "ve lâkin lâ tuhibbûne'n-nâsihîn", True)) + ' ' +
 "Ölçüm xref okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıbı: 'tevellâ 'an qâle qavm qad ebleğu risâle rabb nesahu _' süzgeç GEÇER; 'risâle rabb nesahu _' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'fe' + PERF + ''an' + 've' + PERF + 'yâ' + izafet + 'le' + 'qad' + PERF + izafet + izafet + 've' + PERF + 'li' + 've' + 'lâkin' + 'lâ' + IMPF + belirli; "
 "D2 nida; CERT ('le-qad' 5. kelime), EMPH ('le-qad' 5. kelime), NEG ('lâ' 12. kelime), VOC ('yâ qavmi' 4. kelime); D3 نصح ×2; D4 1S 6 · 2MP 4 · 3MP 1 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[79] + "; aktör yok (ölçüm); A2 elçinin kavminden yüz çevirişi; risaletin tebliği ve öğüt; öğüt verenlerin sevilmeyişi; "
 "A3 'yâ qavmi le-qad ebleğtukum risâlete rabbî ve nasahtu lekum ve lâkin lâ tuhibbûne'n-nâsihîn' (söz içi, 4-14. kelime); "
 "A4 " + BOLUM + "; söz açılır (4. kelime); söz kapanır (14. kelime, ayet içi); şahıs geçişi 3 → 1 (ayetler arası); edim geçişi haber → nida (ayetler arası).",
)
out = ['# ── blok 7:76-79 (2026-11-27) ──', 'MEAL22 = {']
for n in range(76, 80):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M22 = {']
for n in range(76, 80):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL22); M.update(M22)']
open('/home/claude/yamalar/metin_7_76_79.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
