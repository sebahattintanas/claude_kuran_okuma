# blok 11 (5:31-32) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b11/say2.txt'
os.environ['OLC'] = '/home/claude/b11/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Âdem'in iki oğlu; bir canı öldürmek' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 31: "Derken Allah, kardeşinin cesedini nasıl örteceğini ona göstermek için yeri eşeleyen bir karga gönderdi. 'Vay bana! Şu karga gibi olup kardeşimin cesedini örtmekten âciz mi kaldım?' dedi ve pişmanlık duyanlardan oldu.",
 32: "Bu yüzden İsrâiloğullarına şunu yazdık: Kim, bir cana karşılık ya da yeryüzünde bir bozgunculuk olmaksızın bir canı öldürürse, sanki bütün insanları öldürmüş gibidir; kim de onu yaşatırsa, sanki bütün insanları yaşatmış gibidir. Andolsun, elçilerimiz onlara apaçık delillerle geldi; sonra onlardan çoğu bunun ardından yeryüzünde mutlaka aşırı gidenlerdir.",
}

T31 = ("Allah (lafız; 'be'asa' faili, 2. kelime); 'ğurâben' (mef'ûl; nekre, 3. kelime); 'yebhasu' faili 3MS (adsız; gönderge karga); 'li-yuriyehû' faili 3MS (adsız; gönderge lafız) ve mef'ûlü 3MS (adsız; gönderge katil kardeş); 'yuvârî' faili 3MS (adsız; gönderge katil kardeş); "
       "'exîh' (kardeş; 11. kelime); 'qâle' faili 3MS (adsız; 12. kelime); söz içi konuşan 1S (adsız; 'veyletâ', ''aceztu', 'ekûne', 'uvâriye', 'exî'); 'l-ğurâbi' (19. kelime); 'asbaha' faili 3MS (adsız); 'n-nâdimîn' (25. kelime)")
T32 = ("konuşan 1P (adsız; 'ketebnâ', 'rusulunâ' — gönderge lafız); 'benî isrâ'île' (adlı kavim; 6-7. kelime — ölçüm aktör); 'ennehû' 3MS (şân zamiri); 'men' (şart ismi; 9. ve 22. kelime; 'qatele' ve 'ahyâ' faili 3MS — adsız); 'nefsen' (mef'ûl; nekre, 11. kelime); "
       "'n-nâse' (mef'ûl; 20. ve 26. kelime); 'ahyâhâ' 3FS (gönderge can); 'rusulunâ' ('câ'et' faili; 30. kelime); 'câ'ethum' ve 'minhum' 3MP (adsız; gönderge kavim); 'kesîran minhum' ('inne' ismi; 34-35. kelime); 'le-musrifûn' (haber; 40. kelime)")

D = {}
D[31] = ("◇ 'fe-be'asa'llâhu ğurâben yebhasu fi'l-ardi li-yuriyehû keyfe yuvârî sev'ete exîh qâle yâ veyletâ e-'aceztu en ekûne misle hâze'l-ğurâbi fe-uvâriye sev'ete exî fe-asbaha mine'n-nâdimîn' — "
 "'fe' + PERF 3MS I. bab + lafız + nekre 'ğurâb' + IMPF 3MS I. bab + 'fî' + belirli 'ard' + 'li' + IMPF 3MS IV. bab + 3MS + 'keyfe' + IMPF 3MS III. bab + 'sev'e' + 'ex' + 3MS + PERF 3MS I. bab + 'yâ' + 'veyl' + 1S + 'e' + PERF 1S I. bab + 'en' + IMPF 1S I. bab + 'misl' + 'hâ' + 'zâ' + belirli 'ğurâb' + 'fe' + IMPF 1S III. bab + 'sev'e' + 'ex' + 1S + 'fe' + PERF 3MS IV. bab + 'min' + belirli çoğul etken ortaç 'nâdim' "
 "(ölçüm edim soru, nida, kip INTG 1 · VOC 1, biçim DIKKAT; 1S 6 · 3MS 8; bab I. bab ×5 · III. bab ×2 · IV. bab ×2). "
 "Allah lafzı 2. sırada (ölçüm allah z=0,27); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm yıldız ★★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=25 (n z=1,34); ölçüm '{{1|biçim DIKKAT}}' — satır aynen; ölçüm '{{1|EDİLGEN 1/9 fiil, pas z=0,30}}' — satır aynen; ölçüm '{{1|HAPAKS: بحث}}' — satır aynen (kök bu blokta tabloya eklendi); ölçüm '{{1|hapaks z=3,28}}' — satır aynen; "
 "ölçüm '{{1|fâsıla ٱلندمين → ن, N sınıfı}}' — satır aynen; ölçüm '{{1|simetri \\[6, 9, 20, 2\\]}}' — satır aynen; ölçüm '{{1|harf 106 → harf3 102, isaret 4}}' — satır aynen; ölçüm '{{1|dış düğüm 0}}' — satır aynen; ölçüm '{{1|bağ: YOK \\(esit2, nakarat3, xref üçü de boş\\)}}' — satır aynen. "
 "Ölçüm INTG 1: 'e' (14. kelime); VOC 1: 'yâ' (13. kelime) (okuma); ölçüm biçim DIKKAT — 'yâ veyletâ' nidâsı ve 'hâze' (18. kelime, morph ATT); D2'de yazılmadı (okuma); ölçüm EDİLGEN — 'li-yuriyehû' (7. kelime) morph PASS etiketli, anlam etken ('göstermek'; IV. bab) — morph etiketi tartışmalı (okuma; aday kayıt); 'li' (7. kelime) morph PRP — amaç (okuma). "
 "Kök ikilemeleri (ölçüm) أخو ×2: 'exîh' (11. kelime) / 'exî' (22. kelime); سوأ ×2: 'sev'ete' (10. ve 21. kelime); غرب ×2: 'ğurâben' (3. kelime) / 'l-ğurâbi' (19. kelime); وري ×2: 'yuvârî' (9. kelime) / 'fe-uvâriye' (20. kelime) (okuma). "
 "'fe-be'asa' (1.)'daki 'fe' morph CONJ; 'fe-uvâriye' (20.) ve 'fe-asbaha' (23.)'daki 'fe' CAUS (okuma). "
 + T31 + " (okuma). "
 + cumle(say('say 5:31 1-3 --on', "fe-be'asa'llâhu ğurâben", True), say('say 5:31 2-3', "llâhu ğurâben"), say('lem 5:31:3', "ğurâb"), say('say 5:31 4-6', "yebhasu fi'l-ard")) + ' '
 + cumle(say('say 5:31 7-11 --on', "li-yuriyehû keyfe yuvârî sev'ete exîh", True), say('say 5:31 9-11', "yuvârî sev'ete exîh"), say('say 5:31 10-11', "sev'ete exîh")) + ' '
 + cumle(say('say 5:31 12-13', "qâle yâ veyletâ", True), say('lem 5:31:13', "veyl"), say('say 5:31 14-19 --on', "e-'aceztu en ekûne misle hâze'l-ğurâb"), say('say 5:31 15-17', "en ekûne misle")) + ' '
 + cumle(say('say 5:31 20-22 --on', "fe-uvâriye sev'ete exî", True), say('say 5:31 21-22', "sev'ete exî"), say('say 5:31 23-25 --on', "fe-asbaha mine'n-nâdimîn"), say('say 5:31 24-25', "mine'n-nâdimîn")) + ' '
 "Ölçüm xref yok. Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'yuvârî sev'ete exîh' (karganın gösterdiği) / 'e-'aceztu' (âciz kalma) — ayetler arası: yok.",
 "◈K — K1 'l-ardi' (6. kelime).",
 "◈B — —",
 "◈D — D1 'fe' + PERF + lafız + nekre + IMPF + 'fî' + belirli + 'li' + IMPF + 'keyfe' + IMPF + izafet + izafet + PERF + 'yâ' + izafet + 'e' + PERF + 'en' + IMPF + izafet + 'hâ' + 'zâ' + belirli + 'fe' + IMPF + izafet + izafet + 'fe' + PERF + 'min' + belirli; "
 "D2 soru, nida, INTG ('e' 14. kelime), VOC ('yâ' 13. kelime); D3 أخو ×2 · سوأ ×2 · غرب ×2 · وري ×2; eş yok; D4 1S 6 · 3MS 8, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T31 + "; aktör yok (ölçüm); A2 gönderme; eşeleme; gösterme; ceset örtme; âcizlik; pişmanlık; A3 'yâ veyletâ' ile açılan söz (13-22. kelime); A4 " + BOLUM + "; edim geçişi haber → soru, nida (ayetler arası); şahıs geçişi yok; söz açılır (13. kelime); söz kapanır (22. kelime, ayet içi).",
)

D[32] = ("◇ 'min ecli zâlike ketebnâ 'alâ benî isrâ'île ennehû men qatele nefsen bi-ğayri nefsin ev fesâdin fi'l-ardi fe-ke'ennemâ qatele'n-nâse cemî'an ve men ahyâhâ fe-ke'ennemâ ahye'n-nâse cemî'an ve leqad câ'ethum rusulunâ bi'l-beyyinâti summe inne kesîran minhum ba'de zâlike fi'l-ardi le-musrifûn' — "
 "'min' + 'ecl' + 'zâ' + PERF 1P I. bab + ''alâ' + çoğul 'buneyy' + özel ad 'isrâ'îl' + 'enne' + 3MS + 'men' + PERF 3MS I. bab + nekre 'nefs' + 'bi' + 'ğayr' + nekre 'nefs' + 'ev' + nekre 'fesâd' + 'fî' + belirli 'ard' + 'fe' + 'ke'enne' + 'mâ' + PERF 3MS I. bab + belirli 'nâs' + nekre 'cemî'' + 've' + 'men' + PERF 3MS IV. bab + 3FS + 'fe' + 'ke'enne' + 'mâ' + PERF 3MS IV. bab + belirli 'nâs' + nekre 'cemî'' + "
 "'ve' + 'le' + 'qad' + PERF 3FS I. bab + 3MP + çoğul 'rasûl' + 1P + 'bi' + belirli çoğul 'beyyine' + 'summe' + 'inne' + nekre 'kesîr' + 'min' + 3MP + 'ba'd' + 'zâ' + 'fî' + belirli 'ard' + 'le' + çoğul etken ortaç 'musrif' "
 "(ölçüm edim şart, kip CERT 1 · COND 2 · EMPH 2; 1P 3 · 3FS 2 · 3MP 2 · 3MS 5; bab I. bab ×4 · IV. bab ×2). "
 "Ölçüm '{{2|lafız YOK · Rab YOK}}' — satır aynen; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm '{{2|aktör: adlı إِسْرائِيل 7\\. sırada \\(kavim, rol mecrur\\)}}' — satır aynen. "
 "Ölçüm yıldız ★★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=40 (n z=2,93); ölçüm '{{2|sayı işareti كَثِير}}' — satır aynen; ölçüm '{{2|fâsıla لمسرفون → ن, N sınıfı}}' — satır aynen; ölçüm '{{2|simetri \\[6, 3, 33, 2\\]}}' — satır aynen; ölçüm '{{2|harf 167 → harf3 160, isaret 7}}' — satır aynen; "
 "ölçüm '{{2|dış düğüm 0}}' — satır aynen; ölçüm '{{2|bağ: YOK \\(esit2, nakarat3, xref üçü de boş\\)}}' — satır aynen. "
 "Ölçüm CERT 1: 'qad' (28. kelime); COND 2: 'men' (9. ve 22. kelime); EMPH 2: 'le' (28. ve 40. kelime) (okuma); 'fe-ke'ennemâ' (18. ve 24. kelime) morph RSLT + 'ke'enne' + PREV 'mâ' — benzetme (okuma). "
 "Kök ikilemeleri (ölçüm) أرض ×2: 'l-ardi' (17. ve 39. kelime); أنس ×2: 'n-nâse' (20. ve 26. kelime); جمع ×2: 'cemî'an' (21. ve 27. kelime); حيي ×2: 'ahyâhâ' (23. kelime) / 'ahye' (25. kelime); قتل ×2: 'qatele' (10. ve 19. kelime); نفس ×2: 'nefsen' (11. kelime) / 'nefsin' (13. kelime) (okuma). "
 "'ev' (14.) ve 'summe' (32.) morph CONJ; 'fe-ke'ennemâ' (18. ve 24.)'daki 'fe' RSLT; 've men' (22.)'deki 've' CONJ; 've leqad' (28.)'deki 've' REM (okuma). "
 + T32 + " (okuma). "
 + cumle(say('say 5:32 1-3', "min ecli zâlik", True), say('say 5:32 4-7', "ketebnâ 'alâ benî isrâ'îl"), say('say 5:32 5-7', "'alâ benî isrâ'îl"), say('say 5:32 8-11', "ennehû men qatele nefsen"), say('say 5:32 9-13', "men qatele nefsen bi-ğayri nefs"), say('say 5:32 12-13', "bi-ğayri nefs"), say('say 5:32 14-17', "ev fesâdin fi'l-ard")) + ' '
 + cumle(say('say 5:32 18-21 --on', "fe-ke'ennemâ qatele'n-nâse cemî'an", True), say('say 5:32 19-21', "qatele'n-nâse cemî'an"), say('say 5:32 20-21', "n-nâse cemî'an"), say('say 5:32 22-27 --on', "ve men ahyâhâ fe-ke'ennemâ ahye'n-nâse cemî'an"), say('say 5:32 22-23 --on', "ve men ahyâhâ")) + ' '
 + cumle(say('say 5:32 28-31 --on', "ve leqad câ'ethum rusulunâ bi'l-beyyinât", True), say('say 5:32 29-31', "câ'ethum rusulunâ bi'l-beyyinât"), say('say 5:32 30-31', "rusulunâ bi'l-beyyinât"), say('say 5:32 32-35', "summe inne kesîran minhum"), say('say 5:32 33-35', "inne kesîran minhum"), say('say 5:32 36-40', "ba'de zâlike fi'l-ardi le-musrifûn"), say('say 5:32 38-40', "fi'l-ardi le-musrifûn")) + ' '
 "Ölçüm xref yok. Ölçüm nakarat3 kalıbı yok. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'fe-ke'ennemâ qatele'n-nâse cemî'an' / 'fe-ke'ennemâ ahye'n-nâse cemî'an' — ayetler arası: 5:30 / 5:32 (5:30 6. kelimedeki öldürme / 'men qatele nefsen').",
 "◈K — K1 'l-ardi' (17. ve 39. kelime); K2 'ecli' (2. kelime).",
 "◈B — B1 'n-nâse' (20. ve 26. kelime); B2 —; B3 —; B4 'ahyâhâ' (23. kelime), 'ahye' (25. kelime).",
 "◈D — D1 'min' + izafet + 'zâ' + PERF + ''alâ' + izafet + özel ad + 'enne' + 'men' + PERF + nekre + 'bi' + izafet + nekre + 'ev' + nekre + 'fî' + belirli + 'fe' + 'ke'enne' + 'mâ' + PERF + belirli + nekre + 've' + 'men' + PERF + 'fe' + 'ke'enne' + 'mâ' + PERF + belirli + nekre + 've' + 'le' + 'qad' + PERF + izafet + 'bi' + belirli + 'summe' + 'inne' + nekre + 'min' + 'ba'd' + 'zâ' + 'fî' + belirli + 'le' + çoğul; "
 "D2 şart, CERT ('qad' 28. kelime), COND ('men' 9. ve 22. kelime), EMPH ('le' 28. ve 40. kelime); D3 أرض ×2 · أنس ×2 · جمع ×2 · حيي ×2 · قتل ×2 · نفس ×2; 13:31, 18:74, 27:76 ve 57:25 eşleri; D4 1P 3 · 3FS 2 · 3MP 2 · 3MS 5, sahset ['1', '3'], iltifât 0.",
 "◈A — A1 " + T32 + "; A2 yazma (hüküm); can öldürme; bozgunculuk; bütün insanlar; yaşatma; elçiler; apaçık deliller; aşırılık; A3 'ennehû men qatele nefsen' ile başlayan yazılı hüküm (8-27. kelime; söz biçimli içerik, tırnak yok); "
 "A4 " + BOLUM + "; edim geçişi soru, nida → şart (ayetler arası); şahıs geçişi yok; şart → cevap (ayet içi; COND 'men' 9. kelime: 'men qatele nefsen' / 'fe-ke'ennemâ qatele'n-nâse cemî'an' (18. kelime)); şart → cevap (ayet içi; COND 'men' 22. kelime: 've men ahyâhâ' / 'fe-ke'ennemâ ahye'n-nâse cemî'an' (24. kelime)); bölüm kapanışı.",
)

out = ['# ── blok 5:31-32 (2026-11-15) ──', 'MEAL11 = {']
for n in range(31, 33):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M11 = {']
for n in range(31, 33):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL11); M.update(M11)']
open('/home/claude/yamalar/metin_5_31_32.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
