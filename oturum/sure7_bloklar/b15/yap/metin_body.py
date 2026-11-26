# sûre 7 blok 15 (7:52-53) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b15/say2.txt'
os.environ['OLC'] = '/home/claude/b15/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Cennet ehli, ateş ehli ve A'râf'takiler' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 52: "Andolsun, onlara bilgi üzere ayrıntılı açıkladığımız bir kitap getirdik; iman eden bir kavim için yol gösterici ve rahmet olarak.",
 53: "Onlar onun tevilinden başkasını mı bekliyorlar? Onun tevilinin geleceği gün, daha önce onu unutmuş olanlar derler ki: Rabbimizin elçileri hak ile geldi. Şimdi bizim şefaatçilerimiz var mı ki bize şefaat etsinler, ya da geri döndürülsek ki işlemekte olduğumuzdan başkasını işleyelim? Onlar kendilerini ziyana uğrattılar ve uydurmakta oldukları şeyler kendilerinden kaybolup gitti.",
}

T = {}
T[52] = ("konuşan 1P (adsız; 'ci'nâhum', 'fassalnâhu' — 2. ve 4. kelime); 'ci'nâhum' 3MP eki (adsız; gönderge 7:51 1. kelime, 2. kelime); 'fassalnâhu' 3MS eki (adsız; gönderge 'bi-kitâbin' 3. kelime, 4. kelime); 'yu'minûn' 3MP (adsız; gönderge 'li-qavmin' 9. kelime, 10. kelime)")
T[53] = ("'yenzurûne' 3MP (adsız; gönderge 7:52 2. kelime, 2. kelime); 'te'vîlehu', 'te'vîluhu' 3MS eki (adsız; gönderge 7:52 3. kelime — 4. ve 7. kelime); 'ye'tî' 3MS (fiil uyumu; 6. kelime — fail 7. kelime); 'yeqûlu' 3MS (fiil uyumu; 8. kelime — fail 9. kelime); "
         "'nesûhu' 3MP (adsız; gönderge 'llezîne' 9. kelime, 10. kelime); 'nesûhu' 3MS eki (adsız; gönderge 7:52 3. kelime, 10. kelime); 'câ'et' 3FS (fiil uyumu; söz içi; 14. kelime — fail 15. kelime); "
         "konuşan 1P eki (adsız; söz içi; 'rabbinâ', 'lenâ', 'lenâ', 'kunnâ' — 16., 19., 23. ve 29. kelime); 'fe-yeşfe'û' 3MP (adsız; söz içi; gönderge 'şufe'â'e' 21. kelime, 22. kelime); "
         "konuşan 1P (adsız; söz içi; edilgen, naib-i faili zamir; 'nuraddu' — 25. kelime); konuşan 1P (adsız; söz içi; 'fe-na'mele', 'kunnâ', 'na'mel' — 26., 29. ve 30. kelime); "
         "'xasirû' 3MP (adsız; gönderge 'llezîne' 9. kelime, 32. kelime); 'enfusehum', ''anhum' 3MP eki (adsız; gönderge 'llezîne' 9. kelime — 33. ve 35. kelime); 've dalle' 3MS (adsız; gönderge 'mâ' 36. kelime, 34. kelime); "
         "'kânû', 'yefterûn' 3MP (adsız; gönderge 'llezîne' 9. kelime — 37. ve 38. kelime)")

D = {}
D[52] = ("◇ 've le-qad ci'nâhum bi-kitâbin fassalnâhu 'alâ 'ilmin huden ve rahmeten li-qavmin yu'minûn' — "
 "'ve' + 'le' + 'qad' + PERF 1P I. bab + 3MP + 'bi' + nekre 'kitâb' + PERF 1P II. bab + 3MS + ''alâ' + nekre ''ilm' + nekre 'hudâ' + 've' + nekre 'rahme' + 'li' + nekre 'qavm' + IMPF 3MP IV. bab "
 "(ölçüm edim haber, kip CERT 1 · EMPH 1; 1P 4 · 3MP 3 · 3MS 1; bab I. bab ×1 · II. bab ×1 · IV. bab ×1). "
 "Allah lafzı yok; Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=10 (n z=-0,26); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:51 ن → 7:52 ن); "
 "ölçüm '{{1|harf 46 → harf3 42, isaret 4}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen; ölçüm '{{1|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm CERT 1: 've le-qad' (1. kelime; 'qad'); EMPH 1: 've le-qad' (1. kelime; 'le'); "
 "'ve le-qad' (1.) kelimesindeki 've' REM; 've rahmeten' (8.) kelimesindeki 've' CONJ (okuma). "
 + T[52] + " (okuma). "
 + cumle(say('say 7:52 2-6', "ci'nâhum bi-kitâbin fassalnâhu 'alâ 'ilmin", True), say('say 7:52 8-10', "rahmeten li-qavmin yu'minûn"), say('dizi 7 52 8 10', "rahme qavm âmene"), say('dizi 7 52 7 10', "hudâ rahme qavm âmene")) + ' ' +
 "Ölçüm xref 16:64 (emsal olarak basıldı), 12:111 (basılmış), okunmamış 1 ayet (sûre içi 1). "
 "Ölçüm nakarat3 kalıbı: 'hudâ rahme qavm âmene' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'le' + 'qad' + PERF + 'bi' + nekre + PERF + ''alâ' + nekre + nekre + 've' + nekre + 'li' + nekre + IMPF; "
 "D2 haber; CERT ('ve le-qad' 1. kelime), EMPH ('ve le-qad' 1. kelime); D3 16:64 eşi; D4 1P 4 · 3MP 3 · 3MS 1, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[52] + "; aktör yok (ölçüm); A2 bilgi üzere ayrıntılı açıklanmış bir kitabın getirilişi; iman eden bir kavim için yol gösterici ve rahmet oluşu; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs sayısında beraberlik (1P 4 · 3. şahıs 4 — ölçüm baskın 1); şahıs geçişi 3 → 1 (ayetler arası); edim geçişi yok (ayetler arası).",
)

D[53] = ("◇ 'hel yenzurûne illâ te'vîlehu yevme ye'tî te'vîluhu yeqûlu'llezîne nesûhu min qablu qad câ'et rusulu rabbinâ bi'l-haqqi fe-hel lenâ min şufe'â'e fe-yeşfe'û lenâ ev nuraddu fe-na'mele ğayra'llezî kunnâ na'mel qad xasirû enfusehum ve dalle 'anhum mâ kânû yefterûn' — "
 "'hel' + IMPF 3MP I. bab + 'illâ' + mastar 'te'vîl' + 3MS + 'yevm' + IMPF 3MS I. bab + mastar 'te'vîl' + 3MS + IMPF 3MS I. bab + 'ellezî' + PERF 3MP I. bab + 3MS + 'min' + 'qabl' + 'qad' + PERF 3FS I. bab + çoğul 'rasûl' + 'rabb' + 1P + 'bi' + belirli 'haqq' + "
 "'fe' + 'hel' + 'li' + 1P + 'min' + çoğul 'şefî'' + 'fe' + IMPF 3MP I. bab + 'li' + 1P + 'ev' + IMPF 1P I. bab edilgen + 'fe' + IMPF 1P I. bab + 'ğayr' + 'ellezî' + PERF 1P I. bab + IMPF 1P I. bab + 'qad' + PERF 3MP I. bab + çoğul 'nefs' + 3MP + 've' + PERF 3MS I. bab + ''an' + 3MP + 'mâ' + PERF 3MP I. bab + IMPF 3MP VIII. bab "
 "(ölçüm edim soru, kip CERT 2 · INTG 2 · RES 1; 1P 8 · 3FS 1 · 3MP 14 · 3MS 6; bab I. bab ×13 · VIII. bab ×1). "
 "Allah lafzı yok; Rab 16. sırada (ölçüm rab z=0,24); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{2|yıldız ★★}}' — satır aynen (kaynak n, z=2,72); n=38 (n z=2,72); ölçüm '{{2|EDİLGEN 1/14 fiil, pas z=0,08}}' — satır aynen; ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:52 ن → 7:53 ن); "
 "ölçüm '{{2|simetri \\[3, 1, 9, 1\\]}}' — satır aynen; ölçüm '{{2|harf 153 → harf3 146, isaret 7}}' — satır aynen; ölçüm '{{2|dış düğüm 4}}' — satır aynen. "
 "Ölçüm CERT 2: 'qad' (13. kelime), 'qad' (31. kelime); INTG 2: 'hel' (1. kelime), 'fe-hel' (18. kelime; 'hel'); RES 1: 'illâ' (3. kelime); ölçüm biçim HASR; "
 "'llezîne' (9.) REL; 'fe-hel' (18.) kelimesindeki 'fe' REM; 'fe-yeşfe'û' (22.) kelimesindeki 'fe' CAUS; 'ev' (24.) CONJ; 'fe-na'mele' (26.) kelimesindeki 'fe' CAUS; 'llezî' (28.) REL; 've dalle' (34.) kelimesindeki 've' CONJ; 'mâ' (36.) REL (okuma). "
 "Kök ikilemesi (ölçüm) أول ×2 ('te'vîlehu' 4. / 'te'vîluhu' 7. kelime); شفع ×2 ('şufe'â'e' 21. / 'fe-yeşfe'û' 22. kelime); عمل ×2 ('fe-na'mele' 26. / 'na'mel' 30. kelime); كون ×2 ('kunnâ' 29. / 'kânû' 37. kelime) (okuma). "
 + T[53] + " (okuma). "
 + cumle(say('say 7:53 1-4', "hel yenzurûne illâ te'vîlehu", True), say('say 7:53 1-3', "hel yenzurûne illâ"), say('say 7:53 5-7', "yevme ye'tî te'vîluhu"), say('say 7:53 8-12', "yeqûlu'llezîne nesûhu min qablu")) + ' '
 + cumle(say('say 7:53 14-17', "câ'et rusulu rabbinâ bi'l-haqqi", True), say('dizi 7 53 14 17', "câ'e rasûl rabb haqq"), say('say 7:53 16-18', "rabbinâ bi'l-haqqi fe-hel"), say('dizi 7 53 16 18', "rabb haqq hel")) + ' '
 + cumle(say('say 7:53 18-23', "fe-hel lenâ min şufe'â'e fe-yeşfe'û lenâ", True), say('say 7:53 24-30', "ev nuraddu fe-na'mele ğayra'llezî kunnâ na'mel"), say('say 7:53 27-30', "ğayra'llezî kunnâ na'mel"), say('dizi 7 53 27 30', "ğayr ellezî kâne 'amile"), say('say 7:53 28-30', "llezî kunnâ na'mel")) + ' '
 + cumle(say('say 7:53 31-33', "qad xasirû enfusehum", True), say('say 7:53 34-38', "ve dalle 'anhum mâ kânû yefterûn"), say('say 7:53 33-38', "enfusehum ve dalle 'anhum mâ kânû yefterûn"), say('say 7:53 37-38', "kânû yefterûn")) + ' ' +
 "Ölçüm xref 6:24 (basılmış), 11:21 (basılmış), 35:37 (emsal olarak basıldı), okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'câ'e rasûl rabb haqq' süzgeç GEÇER; 'rabb haqq hel' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — K2 'yevme' (5. kelime).",
 "◈B — —",
 "◈D — D1 'hel' + IMPF + 'illâ' + izafet + 'yevm' + IMPF + izafet + IMPF + 'ellezî' + PERF + 'min' + 'qabl' + 'qad' + PERF + izafet + izafet + 'bi' + belirli + 'fe' + 'hel' + 'li' + 'min' + 'şefî'' + 'fe' + IMPF + 'li' + 'ev' + IMPF + 'fe' + IMPF + 'ğayr' + 'ellezî' + PERF + IMPF + 'qad' + PERF + izafet + 've' + PERF + ''an' + 'mâ' + PERF + IMPF; "
 "D2 soru; CERT ('qad' 13. kelime, 'qad' 31. kelime), INTG ('hel' 1. kelime, 'fe-hel' 18. kelime), RES ('illâ' 3. kelime); D3 35:37 eşi, أول ×2, شفع ×2, عمل ×2, كون ×2; D4 1P 8 · 3FS 1 · 3MP 14 · 3MS 6, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T[53] + "; aktör yok (ölçüm); A2 kitabın tevilinin beklenişi; tevilin geldiği gün unutanların elçilerin hak ile geldiğini söyleyip şefaatçi ya da dönüş isteyişi; kendilerini ziyana uğratışları ve uydurduklarının kayboluşu; "
 "A3 'qad câ'et rusulu rabbinâ bi'l-haqqi fe-hel lenâ min şufe'â'e fe-yeşfe'û lenâ ev nuraddu fe-na'mele ğayra'llezî kunnâ na'mel' (söz içi, 13-30. kelime); "
 "A4 " + BOLUM + "; söz açılır (13. kelime); söz kapanır (30. kelime, ayet içi); soru → cevap (ayet içi; INTG 'fe-hel' 18. kelime: 'lenâ min şufe'â'e' / 'fe-yeşfe'û' (22. kelime)); soru → cevap (ayet içi; 'ev nuraddu' / 'fe-na'mele' (26. kelime)); şahıs geçişi 1 → 3 (ayetler arası); edim geçişi haber → soru (ayetler arası); bölüm kapanışı.",
)
out = ['# ── blok 7:52-53 (2026-11-25) ──', 'MEAL15 = {']
for n in range(52, 54):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M15 = {']
for n in range(52, 54):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL15); M.update(M15)']
open('/home/claude/yamalar/metin_7_52_53.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
