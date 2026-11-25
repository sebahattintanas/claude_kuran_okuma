# sûre 7 blok 8 (7:28-30) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os, re
os.environ['SAY2'] = '/home/claude/b08/say2.txt'
os.environ['OLC'] = '/home/claude/b08/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'Ey Âdemoğulları: giysi, fitne, ziynet; haram kılınanlar' bölümünde"
_OL = [l.replace('**', '') for l in open(os.environ['OLC'], encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK3 = _esc(re.search(r'aktör: adlı .*adsız `ferîk` 3\. sırada', _OL[2]).group(0))
_ES3 = _esc(re.search(r'esmâ \S+ 10\. sırada, ORTA konum, MÜHÜRSÜZ', _OL[2]).group(0))


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 28: "Bir hayâsızlık yaptıklarında derler ki: Atalarımızı bunun üzerinde bulduk; Allah da bize bunu emretti. De ki: Gerçekten Allah hayâsızlığı emretmez. Allah hakkında bilmediğiniz şeyi mi söylüyorsunuz?",
 29: "De ki: Rabbim adaleti emretti. Her mescidin yanında yüzlerinizi doğrultun ve dini O'na hâlis kılarak O'na dua edin. Sizi başlattığı gibi döneceksiniz.",
 30: "Bir bölüğe yol gösterdi; bir bölüğe de sapkınlık hak oldu. Gerçekten onlar Allah'tan başka şeytanları dostlar edindiler ve kendilerinin doğru yolu bulmuş olduklarını sanıyorlar.",
}

T = {}
T[28] = ("'fe'alû', 'qâlû' 3MP (adsız; tartışmalı; gönderge 7:27 28. kelime — 2. ve 4. kelime); konuşan 1P (adsız; söz içi; 'vecednâ' — 5. kelime); konuşan 1P eki (adsız; söz içi; 'âbâ'enâ', 'emeranâ' — 7. ve 9. kelime); "
         "''aleyhâ', 'bihâ' 3FS eki (adsız; söz içi; gönderge 'fâhişeten' 3. kelime — 6. ve 10. kelime); 'emeranâ' 3MS (adsız; söz içi; gönderge 've'llâhu' 8. kelime, 9. kelime); muhatap 2MS (adsız; 'qul' — 11. kelime); "
         "'ye'muru' 3MS (adsız; söz içi; gönderge 'llâhe' 13. kelime, 15. kelime); muhatap 2MP (adsız; söz içi; 'e-teqûlûne', 'ta'lemûn' — 17. ve 22. kelime)")
T[29] = ("muhatap 2MS (adsız; 'qul' — 1. kelime); 'emera' 3MS (fiil uyumu; söz içi; 2. kelime — fail 3. kelime); konuşan 1S eki (adsız; söz içi; 'rabbî' — 3. kelime); muhatap 2MP (adsız; söz içi; 've aqîmû', 've'd'ûhu', 'te'ûdûn' — 5., 10. ve 16. kelime); "
         "muhatap 2MP eki (adsız; söz içi; 'vucûhekum', 'bede'ekum' — 6. ve 15. kelime); 've'd'ûhu', 'lehu' 3MS eki (adsız; söz içi; gönderge 'rabbî' 3. kelime — 10. ve 12. kelime); 'bede'ekum' 3MS (adsız; söz içi; gönderge 'rabbî' 3. kelime, 15. kelime)")
T[30] = ("'hedâ' 3MS (adsız; gönderge 7:29 3. kelime, 2. kelime); 'haqqa' 3MS (fiil uyumu; 4. kelime — fail 6. kelime); ''aleyhimu', 'innehumu', 'ennehum' 3MP eki (adsız; gönderge 've ferîqan' 3. kelime — 5., 7. ve 15. kelime); "
         "'ttexazu', 've yahsebûne' 3MP (adsız; gönderge 've ferîqan' 3. kelime — 8. ve 14. kelime)")

D = {}
D[28] = ("◇ 've izâ fe'alû fâhişeten qâlû vecednâ 'aleyhâ âbâ'enâ ve'llâhu emeranâ bihâ qul inne'llâhe lâ ye'muru bi'l-fahşâ'i e-teqûlûne 'ale'llâhi mâ lâ ta'lemûn' — "
 "'ve' + 'izâ' + PERF 3MP I. bab + nekre 'fâhişe' + PERF 3MP I. bab + PERF 1P I. bab + ''alâ' + 3FS + çoğul 'âbâ'' + 1P + 've' + 'allâh' + PERF 3MS I. bab + 1P + 'bi' + 3FS + IMPV 2MS I. bab + 'inne' + 'allâh' + 'lâ' + IMPF 3MS I. bab + 'bi' + belirli 'fahşâ'' + 'e' + IMPF 2MP I. bab + ''alâ' + 'allâh' + 'mâ' + 'lâ' + IMPF 2MP I. bab "
 "(ölçüm edim soru, emir, kip IMPV 1 · INTG 1 · NEG 2; 1P 4 · 2MP 4 · 2MS 1 · 3FS 2 · 3MP 4 · 3MS 2; bab I. bab ×8). "
 "Allah lafzı 8., 13. ve 19. sırada (ölçüm allah z=2,20); Rab yok; esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm '{{1|yıldız ★★}}' — satır aynen (kaynak allah, z=2,20); n=22 (n z=1,02); ölçüm '{{1|fâsıla " + _F[0] + " → ن, N sınıfı}}' — satır aynen (7:27 ن → 7:28 ن); "
 "ölçüm '{{1|simetri \\[6, 9, 15, 1\\]}}' — satır aynen; ölçüm '{{1|harf 99 → harf3 94, isaret 5}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen. "
 "Ölçüm IMPV 1: 'qul' (11. kelime); INTG 1: 'e-teqûlûne' (17. kelime; 'e'); NEG 2: 'lâ' (14. kelime), 'lâ' (21. kelime); "
 "'ve izâ' (1.) kelimesindeki 've' REM, 'izâ' T; 've'llâhu' (8.) kelimesindeki 've' REM; 'inne' (12.) ACC; 'mâ' (20.) REL (okuma). "
 "Kök ikilemesi (ölçüm) أله ×3 ('ve'llâhu' 8. / 'llâhe' 13. / 'llâhi' 19. kelime); أمر ×2 ('emeranâ' 9. / 'ye'muru' 15. kelime); فحش ×2 ('fâhişeten' 3. / 'bi'l-fahşâ'i' 16. kelime); قول ×3 ('qâlû' 4. / 'qul' 11. / 'e-teqûlûne' 17. kelime) (okuma). "
 + T[28] + " (okuma). "
 + cumle(say('say 7:28 1-3', "ve izâ fe'alû fâhişeten", True), say('say 7:28 5-7', "vecednâ 'aleyhâ âbâ'enâ"), say('say 7:28 8-10', "ve'llâhu emeranâ bihâ")) + ' '
 + cumle(say('say 7:28 12-16', "inne'llâhe lâ ye'muru bi'l-fahşâ'i", True), say('say 7:28 11-13', "qul inne'llâhe"), say('dizi 7 28 11 13', "qâle inne allâh"), say('say 7:28 15-16', "ye'muru bi'l-fahşâ'i")) + ' '
 + cumle(say('say 7:28 17-22', "e-teqûlûne 'ale'llâhi mâ lâ ta'lemûn", True), say('dizi 7 28 17 22', "qâle 'alâ allâh mâ lâ 'alime"), say('say 7:28 18-22', "'ale'llâhi mâ lâ ta'lemûn"), say('say 7:28 19-22', "llâhi mâ lâ ta'lemûn"), say('dizi 7 28 19 22', "allâh mâ lâ 'alime"),
         say('say 7:28 17-19', "e-teqûlûne 'ale'llâhi"), say('dizi 7 28 17 19', "qâle 'alâ allâh")) + ' ' +
 "Ölçüm xref 2:169 (emsal olarak basıldı), okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'qâle 'alâ allâh mâ lâ 'alime' süzgeç GEÇER; 'allâh mâ lâ 'alime' süzgeç GEÇER; 'qâle 'alâ allâh' süzgeç GEÇER; 'qâle inne allâh' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: yok — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 've' + 'izâ' + PERF + nekre + PERF + PERF + ''alâ' + izafet + 've' + lafız + PERF + 'bi' + IMPV + 'inne' + lafız + 'lâ' + IMPF + 'bi' + belirli + 'e' + IMPF + ''alâ' + lafız + 'mâ' + 'lâ' + IMPF; "
 "D2 soru, emir; IMPV ('qul' 11. kelime), INTG ('e-teqûlûne' 17. kelime), NEG ('lâ' 14. kelime, 'lâ' 21. kelime); D3 2:169 eşi, أله ×3, أمر ×2, فحش ×2, قول ×3; D4 1P 4 · 2MP 4 · 2MS 1 · 3FS 2 · 3MP 4 · 3MS 2, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[28] + "; aktör yok (ölçüm); A2 hayâsızlığı atalara ve Allah'ın emrine dayandırma; Allah'ın hayâsızlığı emretmediği; Allah hakkında bilmeden söz söylemenin sorgulanması; "
 "A3 'vecednâ 'aleyhâ âbâ'enâ ve'llâhu emeranâ bihâ' (söz içi, 5-10. kelime); 'inne'llâhe lâ ye'muru bi'l-fahşâ'i e-teqûlûne 'ale'llâhi mâ lâ ta'lemûn' (söz içi, 12-22. kelime); "
 "A4 " + BOLUM + "; söz açılır (5. kelime); söz kapanır (10. kelime, ayet içi); söz açılır (12. kelime); söz kapanır (22. kelime, ayet içi); muhatap geçişi 2MS → 2MP (ayet içi, 'qul' / 'e-teqûlûne'); şahıs geçişi yok (ayetler arası); edim geçişi nida → soru, emir (ayetler arası).",
)

D[29] = ("◇ 'qul emera rabbî bi'l-qısti ve aqîmû vucûhekum 'inde kulli mescidin ve'd'ûhu muxlisîne lehu'd-dîne kemâ bede'ekum te'ûdûn' — "
 "IMPV 2MS I. bab + PERF 3MS I. bab + 'rabb' + 1S + 'bi' + belirli 'qıst' + 've' + IMPV 2MP IV. bab + çoğul 'vech' + 2MP + ''inde' + 'kull' + nekre 'mescid' + 've' + IMPV 2MP I. bab + 3MS + çoğul etken ortaç 'muxlis' + 'li' + 3MS + belirli 'dîn' + 'ke' + 'mâ' + PERF 3MS I. bab + 2MP + IMPF 2MP I. bab "
 "(ölçüm edim emir, kip IMPV 3; 1S 1 · 2MP 8 · 2MS 1 · 3MS 4; bab I. bab ×5 · IV. bab ×1). "
 "Allah lafzı yok; Rab 3. sırada (ölçüm rab z=1,01); esmâ yok, aktör yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor). "
 "Ölçüm 'yıldız yok' — satır aynen; n=16 (n z=0,38); ölçüm '{{2|fâsıla " + _F[1] + " → ن, N sınıfı}}' — satır aynen (7:28 ن → 7:29 ن); "
 "ölçüm '{{2|harf 73 → harf3 69, isaret 4}}' — satır aynen; ölçüm '{{2|dış düğüm 1}}' — satır aynen. "
 "Ölçüm IMPV 3: 'qul' (1. kelime), 'aqîmû' (5. kelime), 'd'ûhu' (10. kelime); "
 "'ve aqîmû' (5.) kelimesindeki 've' CONJ; 've'd'ûhu' (10.) kelimesindeki 've' CONJ; 'kemâ' (14.) P + SUB (okuma). "
 + T[29] + " (okuma). "
 + cumle(say('say 7:29 2-4', "emera rabbî bi'l-qısti", True), say('say 7:29 5-9', "ve aqîmû vucûhekum 'inde kulli mescidin"), say('say 7:29 7-9', "'inde kulli mescidin"), say('dizi 7 29 7 9', "'inde kull mescid")) + ' '
 + cumle(say('say 7:29 10-13', "ve'd'ûhu muxlisîne lehu'd-dîne", True), say('say 7:29 11-13', "muxlisîne lehu'd-dîne"), say('dizi 7 29 10 13', "de'â muxlis _ dîn"), say('say 7:29 14-16', "kemâ bede'ekum te'ûdûn")) + ' ' +
 "Ölçüm xref 40:65 (emsal olarak basıldı). "
 "Ölçüm nakarat3 kalıbı: ''inde kull mescid' süzgeç GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'bede'ekum' / 'te'ûdûn' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 IMPV + PERF + izafet + 'bi' + belirli + 've' + IMPV + izafet + ''inde' + 'kull' + nekre + 've' + IMPV + 'muxlis' + 'li' + belirli + 'ke' + 'mâ' + PERF + IMPF; "
 "D2 emir; IMPV ('qul' 1. kelime, 'aqîmû' 5. kelime, 'd'ûhu' 10. kelime); D3 40:65 eşi; D4 1S 1 · 2MP 8 · 2MS 1 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T[29] + "; aktör yok (ölçüm); A2 Rabbin adaleti emretmesi; her mescidin yanında yüzleri doğrultma ve dini O'na hâlis kılarak dua etme emri; başlatıldığı gibi dönüş; "
 "A3 'emera rabbî bi'l-qısti ve aqîmû vucûhekum 'inde kulli mescidin ve'd'ûhu muxlisîne lehu'd-dîne kemâ bede'ekum te'ûdûn' (söz içi, 2-16. kelime); "
 "A4 " + BOLUM + "; söz açılır (2. kelime); söz kapanır (16. kelime, ayet içi); muhatap geçişi 2MS → 2MP (ayet içi, 'qul' / 've aqîmû'); şahıs geçişi 3 → 2 (ayetler arası); edim geçişi soru, emir → emir (ayetler arası).",
)

D[30] = ("◇ 'ferîqan hedâ ve ferîqan haqqa 'aleyhimu'd-dalâletu innehumu'ttexazu'ş-şeyâtîne evliyâ'e min dûni'llâhi ve yahsebûne ennehum muhtedûn' — "
 "nekre 'ferîq' + PERF 3MS I. bab + 've' + nekre 'ferîq' + PERF 3MS I. bab + ''alâ' + 3MP + belirli 'dalâle' + 'inne' + 3MP + PERF 3MP VIII. bab + belirli çoğul 'şeytân' + çoğul 'velî' + 'min' + 'dûn' + 'allâh' + 've' + IMPF 3MP I. bab + 'enne' + 3MP + çoğul etken ortaç 'muhtedî' "
 "(ölçüm edim haber, kip yok; 3MP 7 · 3MS 2; bab I. bab ×3 · VIII. bab ×1). "
 "Allah lafzı 13. sırada (ölçüm allah z=0,72); Rab yok; ölçüm '{{3|" + _ES3 + "}}' — satır aynen; esma_kayit çıktısı 'mühür hayır' (uyuşuyor); "
 "esma_el kaydı 'degil' — 'innehumu'ttexazu'ş-şeyâtîne evliyâ'e min dûni'llâhi', kural 'esmâ adı esmâ dışı göndergeyle → degil' (dost edinilen şeytanlar) (okuma); ölçüm '{{3|" + _AK3 + "}}' — satır aynen. "
 "Ölçüm 'yıldız yok' — satır aynen; n=16 (n z=0,38); ölçüm '{{3|fâsıla " + _F[2] + " → ن, N sınıfı}}' — satır aynen (7:29 ن → 7:30 ن); "
 "ölçüm '{{3|harf 78 → harf3 76, isaret 2}}' — satır aynen; ölçüm '{{3|dış düğüm 1}}' — satır aynen. "
 "Ölçüm kip yok; "
 "'ve ferîqan' (3.) kelimesindeki 've' CONJ; 'innehumu' (7.) ACC; 've yahsebûne' (14.) kelimesindeki 've' CIRC; 'ennehum' (15.) ACC (okuma). "
 "Kök ikilemesi (ölçüm) فرق ×2 ('ferîqan' 1. / 've ferîqan' 3. kelime); هدي ×2 ('hedâ' 2. / 'muhtedûn' 16. kelime) (okuma). "
 + T[30] + " (okuma). "
 + cumle(say('say 7:30 1-2', "ferîqan hedâ", True), say('say 7:30 3-6', "ve ferîqan haqqa 'aleyhimu'd-dalâletu")) + ' '
 + cumle(say('say 7:30 7-13', "innehumu'ttexazu'ş-şeyâtîne evliyâ'e min dûni'llâhi", True), say('say 7:30 11-13', "min dûni'llâhi"), say('dizi 7 30 11 13', "min dûn allâh"), say('say 7:30 14-16', "ve yahsebûne ennehum muhtedûn")) + ' ' +
 "Ölçüm xref okunmuş 1 ayet. "
 "Ölçüm nakarat3 kalıbı: 'min dûn allâh' süzgeç GEÇER. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'hedâ' / 'd-dalâletu' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 nekre + PERF + 've' + nekre + PERF + ''alâ' + belirli + 'inne' + PERF + belirli + 'velî' + 'min' + 'dûn' + lafız + 've' + IMPF + 'enne' + 'muhtedî'; "
 "D2 haber; kip yok; D3 فرق ×2, هدي ×2; D4 3MP 7 · 3MS 2, sahset ['3'], iltifât 0.",
 "◈A — A1 " + T[30] + "; aktör adlı 'ş-şeyâtîne' (9. kelime; ölçüm rol meful); aktör adsız 'ferîqan' (1. kelime), 've ferîqan' (3. kelime); A2 bir bölüğe yol gösterilmesi, bir bölüğe sapkınlığın hak oluşu; Allah'tan başka şeytanları dost edinme ve doğru yolda olduğunu sanma; "
 "A3 —; "
 "A4 " + BOLUM + "; şahıs geçişi 2 → 3 (ayetler arası); edim geçişi emir → haber (ayetler arası).",
)
out = ['# ── blok 7:28-30 (2026-11-25) ──', 'MEAL8 = {']
for n in range(28, 31):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M8 = {']
for n in range(28, 31):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL8); M.update(M8)']
open('/home/claude/yamalar/metin_7_28_30.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
