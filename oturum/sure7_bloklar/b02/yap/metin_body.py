# sûre 7 blok 2 (7:6-10) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b02/say2.txt'
os.environ['OLC'] = '/home/claude/b02/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Kitap indirildi; helak edilen kentler; tartı; yeryüzünde yerleştirme' bölümünde"
_OL = [l for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 6: "Kendilerine elçi gönderilenlere mutlaka soracağız, elçilere de mutlaka soracağız.",
 7: "Onlara mutlaka bir bilgiyle anlatacağız; biz uzakta değildik.",
 8: "O gün tartı haktır. Tartıları ağır gelenler, işte onlar kurtuluşa erenlerdir.",
 9: "Tartıları hafif gelenler, işte onlar kendilerini ziyana uğratanlardır; âyetlerimize zulmetmekte olmaları yüzünden.",
 10: "Andolsun, sizi yeryüzünde yerleştirdik ve orada size geçimlikler var ettik. Pek az şükrediyorsunuz.",
}

T = {}
T[6] = ("konuşan 1P (adsız; 'fe-le-nes'elenne', 've le-nes'elenne' — 1. ve 5. kelime); 'ursile' 3MS (adsız; edilgen, naib-i faili 'ileyhim' 4. kelime, 3. kelime); 'ileyhim' 3MP eki (adsız; gönderge 'llezîne' 2. kelime, 4. kelime)")
T[7] = ("konuşan 1P (adsız; 'fe-le-nequssanne', 'kunnâ' — 1. ve 5. kelime); ''aleyhim' 3MP eki (adsız; tartışmalı; gönderge 7:6 2. kelime, 2. kelime)")
T[8] = ("'sequlet' 3FS (fiil uyumu; 5. kelime — fail 6. kelime); 'mevâzînuhû' 3MS eki (adsız; gönderge 'men' 4. kelime, 6. kelime); 'humu' 3MP (adsız; gönderge 'ulâ'ike' 7. kelime, 8. kelime)")
T[9] = ("'xaffet' 3FS (fiil uyumu; 2. kelime — fail 3. kelime); 'mevâzînuhû' 3MS eki (adsız; gönderge 'men' 1. kelime, 3. kelime); 'xasirû', 'kânû', 'yazlimûn' 3MP (adsız; gönderge 'llezîne' 5. kelime — 6., 9. ve 11. kelime); "
        "'enfusehum' 3MP eki (adsız; gönderge 'llezîne' 5. kelime, 7. kelime); konuşan 1P eki (adsız; 'bi-âyâtinâ' — 10. kelime)")
T[10] = ("konuşan 1P (adsız; 'mekkennâkum', 've ce'alnâ' — 2. ve 5. kelime); muhatap 2MP eki (adsız; 'mekkennâkum', 'lekum' — 2. ve 6. kelime); 'fîhâ' 3FS eki (adsız; gönderge 'l-ardi' 4. kelime, 7. kelime); muhatap 2MP (adsız; 'teşkurûn' — 11. kelime)")

D = {}
D[6] = ("◇ 'fe-le-nes'elenne'llezîne ursile ileyhim ve le-nes'elenne'l-murselîn' — "
 "'fe' + 'le' + IMPF 1P I. bab + 'n' + 'ellezî' + PERF 3MS IV. bab edilgen + 'ilâ' + 3MP + 've' + 'le' + IMPF 1P I. bab + 'n' + belirli çoğul edilgen ortaç 'mursel' "
 "(ölçüm edim haber, kip EMPH 4; 1P 2 · 3MP 1 · 3MS 1; bab I. bab ×2 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=6 (n z=-0,68); ölçüm '{{1|EDİLGEN 1/3 fiil, pas z=1,57}}' — satır aynen; ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:5 ن → 7:6 ن); "
 "ölçüm '{{1|harf 36 → harf3 36, isaret 0}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen. "
 "Ölçüm EMPH 4: 'fe-le-nes'elenne' (1. kelime; 'le' ve 'n'), 've le-nes'elenne' (5. kelime; 'le' ve 'n'); "
 "'fe-le-nes'elenne' (1.) kelimesindeki 'fe' REM; 've le-nes'elenne' (5.) kelimesindeki 've' CONJ (okuma). "
 "Kök ikilemesi (ölçüm) رسل ×2 ('ursile' 3. / 'l-murselîn' 6. kelime), سأل ×2 ('fe-le-nes'elenne' 1. / 've le-nes'elenne' 5. kelime) (okuma). "
 + T[6] + " (okuma). "
 + cumle(say('say 7:6 1-4', "fe-le-nes'elenne'llezîne ursile ileyhim", True), say('say 7:6 5-6', "ve le-nes'elenne'l-murselîn")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'fe' + 'le' + IMPF + 'ellezî' + PERF + 'ilâ' + 've' + 'le' + IMPF + belirli; "
 "D2 haber; EMPH ('fe-le-nes'elenne' 1. kelime, 've le-nes'elenne' 5. kelime); D3 رسل ×2, سأل ×2; D4 1P 2 · 3MP 1 · 3MS 1, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[6] + "; aktör yok (ölçüm); A2 kendilerine elçi gönderilenlerin ve elçilerin sorgulanacağı; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 1 (ayetler arası); şahıs sayısında beraberlik (1P 2 · 3MP 1 · 3MS 1 — ölçüm baskın 1); edim geçişi yok (ayetler arası).",
)

D[7] = ("◇ 'fe-le-nequssanne 'aleyhim bi-'ilmin ve mâ kunnâ ğâ'ibîn' — "
 "'fe' + 'le' + IMPF 1P I. bab + 'n' + ''alâ' + 3MP + 'bi' + nekre ''ilm' + 've' + 'mâ' + PERF 1P I. bab + çoğul etken ortaç 'ğâ'ib' "
 "(ölçüm edim haber, kip EMPH 2 · NEG 1; 1P 3 · 3MP 1; bab I. bab ×2). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=6 (n z=-0,68); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:6 ن → 7:7 ن); "
 "ölçüm '{{2|harf 29 → harf3 27, isaret 2}}' — satır aynen; ölçüm '{{2|dış düğüm 0}}' — satır aynen. "
 "Ölçüm EMPH 2: 'fe-le-nequssanne' (1. kelime; 'le' ve 'n'); NEG 1: 'mâ' (4. kelime); "
 "'fe-le-nequssanne' (1.) kelimesindeki 'fe' CONJ; 've mâ' (4.) kelimesindeki 've' REM (okuma). "
 + T[7] + " (okuma). "
 + cumle(say('say 7:7 1-3', "fe-le-nequssanne 'aleyhim bi-'ilmin", True), say('say 7:7 4-6', "ve mâ kunnâ ğâ'ibîn"), say('say 7:7 4-5', "ve mâ kunnâ")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'fe' + 'le' + IMPF + ''alâ' + 'bi' + nekre + 've' + 'mâ' + PERF + 'ğâ'ib'; "
 "D2 haber; EMPH ('fe-le-nequssanne' 1. kelime), NEG ('mâ' 4. kelime); D3 —; D4 1P 3 · 3MP 1, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[7] + "; aktör yok (ölçüm); A2 olanların onlara bilgiyle anlatılacağı; konuşanın uzakta olmadığı; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi yok (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[8] = ("◇ 've'l-veznu yevme'izini'l-haqq, fe-men sequlet mevâzînuhû fe-ulâ'ike humu'l-muflihûn' — "
 "'ve' + belirli 'vezn' + 'yevm' + 'iz' + belirli 'haqq' + 'fe' + 'men' + PERF 3FS I. bab + çoğul 'mîzân' + 3MS + 'fe' + 'ulâ'i' + 'ke' + 'hum' + belirli çoğul etken ortaç 'muflih' "
 "(ölçüm edim şart, kip COND 1; 3FS 1 · 3MP 1 · 3MS 1; bab I. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=9 (n z=-0,36); ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:7 ن → 7:8 ن); "
 "ölçüm '{{3|harf 47 → harf3 44, isaret 3}}' — satır aynen; ölçüm '{{3|dış düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 'men' (4. kelime); "
 "'ve'l-veznu' (1.) kelimesindeki 've' CONJ; 'fe-men' (4.) kelimesindeki 'fe' REM; 'fe-ulâ'ike' (7.) kelimesindeki 'fe' RSLT (okuma). "
 "Kök ikilemesi (ölçüm) وزن ×2 ('l-veznu' 1. / 'mevâzînuhû' 6. kelime) (okuma). "
 + T[8] + " (okuma). "
 + cumle(say('say 7:8 1-3', "ve'l-veznu yevme'izini'l-haqq", True), say('say 7:8 2-3', "yevme'izini'l-haqq")) + ' '
 + cumle(say('say 7:8 4-9', "fe-men sequlet mevâzînuhû fe-ulâ'ike humu'l-muflihûn", True), say('dizi 7 8 4 9', "men sequlet mîzân zâ _ muflih"), say('say 7:8 4-6', "fe-men sequlet mevâzînuhû"), say('say 7:8 7-9', "fe-ulâ'ike humu'l-muflihûn")) + ' ' +
 "Ölçüm xref 23:102 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K2 'yevme'izin' (2. kelime).",
 "◈B — —",
 "◈D — D1 've' + belirli + 'yevm' + 'iz' + belirli + 'fe' + 'men' + PERF + izafet + 'fe' + 'ulâ'i' + 'hum' + belirli; "
 "D2 şart; COND ('men' 4. kelime); D3 23:102 eşi, وزن ×2; D4 3FS 1 · 3MP 1 · 3MS 1, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[8] + "; aktör yok (ölçüm); A2 o gün tartının hak oluşu; tartıları ağır gelenlerin kurtuluşa ermesi; "
 "A3 —; "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; COND 'men' 4. kelime: 'fe-men sequlet mevâzînuhû' / 'fe-ulâ'ike' (7. kelime)); şahıs geçişi 1 → 3 (ayetler arası); edim geçişi haber → şart (ayetler arası).",
)

D[9] = ("◇ 've men xaffet mevâzînuhû fe-ulâ'ike'llezîne xasirû enfusehum bimâ kânû bi-âyâtinâ yazlimûn' — "
 "'ve' + 'men' + PERF 3FS I. bab + çoğul 'mîzân' + 3MS + 'fe' + 'ulâ'i' + 'ke' + 'ellezî' + PERF 3MP I. bab + çoğul 'nefs' + 3MP + 'bi' + 'mâ' + PERF 3MP I. bab + 'bi' + çoğul 'âye' + 1P + IMPF 3MP I. bab "
 "(ölçüm edim şart, kip COND 1; 1P 1 · 3FS 1 · 3MP 7 · 3MS 1; bab I. bab ×4). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=11 (n z=-0,15); ölçüm '{{4|fâsıla " + _F[3] + " → ن, N sınıfı}}' — satır aynen (7:8 ن → 7:9 ن); "
 "ölçüm '{{4|harf 59 → harf3 55, isaret 4}}' — satır aynen; ölçüm '{{4|dış düğüm 1}}' — satır aynen. "
 "Ölçüm COND 1: 'men' (1. kelime); "
 "'ve men' (1.) kelimesindeki 've' CONJ; 'fe-ulâ'ike' (4.) kelimesindeki 'fe' RSLT; 'bimâ' (8.) kelimesindeki 'mâ' REL (okuma). "
 + T[9] + " (okuma). "
 + cumle(say('say 7:9 1-7', "ve men xaffet mevâzînuhû fe-ulâ'ike'llezîne xasirû enfusehum", True), say('dizi 7 9 1 7', "men xaffet mîzân zâ ellezî xasira nefs"), say('say 7:9 1-3', "ve men xaffet mevâzînuhû"), say('say 7:9 4-7', "fe-ulâ'ike'llezîne xasirû enfusehum"), say('say 7:9 5-7', "llezîne xasirû enfusehum")) + ' '
 + cumle(say('say 7:9 8-11', "bimâ kânû bi-âyâtinâ yazlimûn", True), say('say 7:9 8-10', "bimâ kânû bi-âyâtinâ")) + ' ' +
 "Ölçüm xref 23:103 (emsal olarak basıldı). "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: 7:8 / 7:9 ('sequlet' / 'xaffet').",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'men' + PERF + izafet + 'fe' + 'ulâ'i' + 'ellezî' + PERF + izafet + 'bi' + 'mâ' + PERF + 'bi' + izafet + IMPF; "
 "D2 şart; COND ('men' 1. kelime); D3 23:103 eşi; D4 1P 1 · 3FS 1 · 3MP 7 · 3MS 1, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[9] + "; aktör yok (ölçüm); A2 tartıları hafif gelenlerin kendilerini ziyana uğratması; âyetlere zulmün gerekçe oluşu; "
 "A3 —; "
 "A4 " + BOLUM + "; şart → cevap (ayet içi; COND 'men' 1. kelime: 've men xaffet mevâzînuhû' / 'fe-ulâ'ike' (4. kelime)); şahıs geçişi yok (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[10] = ("◇ 've le-qad mekkennâkum fi'l-ardi ve ce'alnâ lekum fîhâ me'âyiş, qalîlen mâ teşkurûn' — "
 "'ve' + 'le' + 'qad' + PERF 1P II. bab + 2MP + 'fî' + belirli 'ard' + 've' + PERF 1P I. bab + 'li' + 2MP + 'fî' + 3FS + çoğul 'me'âyiş' + nekre 'qalîl' + 'mâ' + IMPF 2MP I. bab "
 "(ölçüm edim haber, kip CERT 1 · EMPH 1; 1P 4 · 2MP 4 · 3FS 1; bab I. bab ×2 · II. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=11 (n z=-0,15); ölçüm '{{5|fâsıla " + _F[4] + " → ن, N sınıfı}}' — satır aynen (7:9 ن → 7:10 ن); "
 "ölçüm '{{5|sayı işareti قَلِيل}}' — satır aynen; ölçüm '{{5|harf 48 → harf3 46, isaret 2}}' — satır aynen; ölçüm '{{5|dış düğüm 0}}' — satır aynen. "
 "Ölçüm CERT 1: 've le-qad' (1. kelime); EMPH 1: 've le-qad' (1. kelime; 'le'); "
 "'ve le-qad' (1.) kelimesindeki 've' REM; 've ce'alnâ' (5.) kelimesindeki 've' CONJ; 'mâ' (10.) SUP (okuma). "
 + T[10] + " (okuma). "
 + cumle(say('say 7:10 1-4', "ve le-qad mekkennâkum fi'l-ardi", True)) + ' '
 + cumle(say('say 7:10 5-8', "ve ce'alnâ lekum fîhâ me'âyiş", True)) + ' '
 + cumle(say('say 7:10 9-11', "qalîlen mâ teşkurûn", True), say('say 7:10 9-10', "qalîlen mâ")) + ' ' +
 "Ölçüm xref yok. "
 "Ölçüm nakarat3 yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K1 'l-ardi' (4. kelime).",
 "◈B — —",
 "◈D — D1 've' + 'le' + 'qad' + PERF + 'fî' + belirli + 've' + PERF + 'li' + 'fî' + 'me'âyiş' + nekre + 'mâ' + IMPF; "
 "D2 haber; CERT ('ve le-qad' 1. kelime), EMPH ('ve le-qad' 1. kelime); D3 —; D4 1P 4 · 2MP 4 · 3FS 1, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[10] + "; aktör yok (ölçüm); A2 yeryüzünde yerleştirme; orada geçimliklerin var edilmesi; az şükretme; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 3 → 1 (ayetler arası); şahıs sayısında beraberlik (1P 4 · 2MP 4 — ölçüm baskın 1); edim geçişi şart → haber (ayetler arası); bölüm kapanışı.",
)
out = ['# ── blok 7:6-10 (2026-11-24) ──', 'MEAL2 = {']
for n in range(6, 11):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M2 = {']
for n in range(6, 11):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL2); M.update(M2)']
open('/home/claude/yamalar/metin_7_6_10.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
