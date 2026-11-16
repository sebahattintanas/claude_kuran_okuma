# blok 7 (5:18-19) metin dosyası oluşturucu — ölçüm alıntıları olcum.txt'ten (kes), sayımlar say2'den
import sys, os
os.environ['SAY2'] = '/home/claude/b07/say2.txt'
os.environ['OLC'] = '/home/claude/b07/olcum.txt'
sys.path.insert(0, '/home/claude/sunum')
from sayim import say
from kes import kes

BOLUM = "'İsrâiloğullarının ve Nasârâ'nın misakı; kitap ehline gelen elçi; Mesih hakkında söz' bölümünde"


def cumle(*parts):
    return '; '.join(parts) + '.'


MEAL = {
 18: "Yahudiler ve Nasârâ, 'Biz Allah'ın oğulları ve sevdikleriyiz' dediler. De ki: 'Öyleyse günahlarınız yüzünden size neden azap ediyor? Hayır, siz O'nun yarattıklarından bir beşersiniz. Dilediğini bağışlar, dilediğine azap eder. Göklerin, yerin ve ikisi arasındakilerin mülkü Allah'ındır; dönüş de O'nadır.'",
 19: "Ey kitap ehli! Elçimiz size geldi; elçilere ara verilmiş bir dönemde size açıklıyor, 'Bize ne bir müjdeci ne de bir uyarıcı geldi' demeyesiniz diye. İşte size bir müjdeci ve bir uyarıcı geldi. Allah her şeye güç yetirendir.",
}

T18 = ("'l-yehûdu ve'n-nasârâ' ('qâlet' faili; adlı cinsler, 2-3. kelime); söz içi konuşan 1P ('nahnu', 4. kelime); Allah (lafız; 6. ve 23. kelime); 'ehibbâ'uh' 3MS (gönderge lafız); muhatap 2MS (adsız; 'qul'); "
       "muhatap 2MP (adsız; 'yu'azzibukum', 'bi-zunûbikum', 'entum' — gönderge Yahudiler ve Nasârâ); 'yu'azzibu', 'xalaq', 'yağfiru' ve 'yeşâ'' faili 3MS (adsız; gönderge lafız); 'beşerun' (haber; nekre, 14. kelime); "
       "'men' (mevsûl; 15., 18. ve 21. kelime); 'beynehumâ' 3D (gönderge gökler ve yer); 'ileyhi' 3MS (gönderge lafız); 'l-masîr' (mübtedâ; 30. kelime)")
T19 = ("muhatap 2MP (adsız; 'ehle'l-kitâbi' — nidâ, 1-2. kelime; 'câ'akum', 'lekum', 'teqûlû'); 'rasûlunâ' ('câ'a' faili; 5. kelime); konuşan 1P (adsız; 'rasûlunâ' — gönderge lafız); 'yubeyyinu' faili 3MS (adsız; gönderge elçi); "
       "'r-rusuli' (belirli çoğul; 11. kelime); söz içi konuşan 1P ('câ'enâ' — muhatabın varsayılan sözü); 'beşîrin ve lâ nezîr' ve 'beşîrun ve nezîr' (nekre; 17-19. ve 22-23. kelime); Allah (lafız; 24. kelime)")

D = {}
D[18] = ("◇ 've qâleti'l-yehûdu ve'n-nasârâ nahnu ebnâ'u'llâhi ve ehibbâ'uh qul fe-lime yu'azzibukum bi-zunûbikum bel entum beşerun mimmen xalaq yağfiru li-men yeşâ'u ve yu'azzibu men yeşâ' ve li'llâhi mulku's-semâvâti ve'l-ardi ve mâ beynehumâ ve ileyhi'l-masîr' — "
 "'ve' + PERF 3FS I. bab + belirli özel ad 'yehûd' + 've' + belirli özel ad 'nasrânî' + 'nahnu' + çoğul 'ibn' + lafız + 've' + çoğul 'ehibbâ'' + 3MS + IMPV 2MS I. bab + 'fe' + 'li' + 'mâ' + IMPF 3MS II. bab + 2MP + 'bi' + çoğul 'zenb' + 2MP + 'bel' + 'entum' + nekre 'beşer' + 'min' + 'men' + PERF 3MS I. bab + IMPF 3MS I. bab + 'li' + 'men' + IMPF 3MS I. bab + 've' + IMPF 3MS II. bab + 'men' + IMPF 3MS I. bab + 've' + 'li' + lafız + 'mulk' + belirli çoğul 'semâ'' + 've' + belirli 'ard' + 've' + 'mâ' + 'beyn' + 3D + 've' + 'ilâ' + 3MS + belirli 'masîr' "
 "(ölçüm edim soru, emir, kip IMPV 1 · INTG 1; 1P 1 · 2MP 3 · 2MS 1 · 3D 1 · 3FS 1 · 3MS 8; bab I. bab ×6 · II. bab ×2). "
 "Allah lafzı 6. ve 23. sırada (ölçüm allah z=0,81); Rab yok; esmâ yok (ölçüm); esma_kayit çıktısı 'mühür hayır' (uyuşuyor); ölçüm aktör '{{1|adlı يَهُود 2\\. sırada \\(cins, rol fail\\+konusan\\)}}', '{{1|adlı نَصْرانِيّ 3\\. sırada \\(cins, rol fail\\)}}' — satır aynen. "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=30 (n z=1,87); ölçüm '{{1|fâsıla ٱلمصير → ر, R sınıfı}}' — satır aynen; ölçüm '{{1|simetri \\[3, 4, 21, 1\\]}}' — satır aynen; ölçüm '{{1|harf 138 → harf3 130, isaret 8}}' — satır aynen; ölçüm '{{1|dış düğüm 2}}' — satır aynen. "
 "Ölçüm IMPV 1: 'qul' (8. kelime); INTG 1: 'mâ' (9. kelime, 'lime' içinde) (okuma). "
 "Kök ikilemeleri (ölçüm) أله ×2: lafız 6. ve 23. kelimede; شيأ ×2: 'yeşâ'u' (19. kelime) / 'yeşâ'' (22. kelime); عذب ×2: 'yu'azzibukum' (10. kelime) / 'yu'azzibu' (20. kelime); قول ×2: 'qâlet' (1. kelime) / 'qul' (8. kelime) (okuma). "
 "'ve qâleti' (1.), 've'n-nasârâ' (3.), 've ehibbâ'uh' (7.), 've yu'azzibu' (20.), 've'l-ardi' (26.), 've mâ' (27.) ve 've ileyhi' (29.)'daki 've' morph CONJ; 'fe-lime' (9.)'deki 'fe' REM; 've li'llâhi' (23.)'daki 've' REM (okuma). "
 + T18 + " (okuma). "
 + cumle(say('say 5:18 1-3 --on', "ve qâleti'l-yehûdu ve'n-nasârâ", True), say('say 5:18 2-3', "l-yehûdu ve'n-nasârâ"), say('say 5:18 4-7', "nahnu ebnâ'u'llâhi ve ehibbâ'uh"), say('lem 5:18:7', "ehibbâ'")) + ' '
 + cumle(say('say 5:18 8-11', "qul fe-lime yu'azzibukum bi-zunûbikum", True), say('say 5:18 9-11', "fe-lime yu'azzibukum bi-zunûbikum"), say('say 5:18 12-16', "bel entum beşerun mimmen xalaq"), say('say 5:18 13-14', "entum beşerun")) + ' '
 + cumle(say('say 5:18 17-22', "yağfiru li-men yeşâ'u ve yu'azzibu men yeşâ'", True), say('say 5:18 17-19', "yağfiru li-men yeşâ'"), say('dizi 5 18 17 19', "ğafere li men şâ'e"), say('say 5:18 20-22', "ve yu'azzibu men yeşâ'"), say('dizi 5 18 20 22', "'azzebe men şâ'e"), say('say 5:18 21-23', "men yeşâ' ve li'llâh"), say('dizi 5 18 21 23', "men şâ'e allâh")) + ' '
 + cumle(say('say 5:18 23-28', "ve li'llâhi mulku's-semâvâti ve'l-ardi ve mâ beynehumâ", True), say('dizi 5 18 23 28', "allâh mulk semâ' ard mâ beyn"), say('say 5:18 23-27', "ve li'llâhi mulku's-semâvâti ve'l-ardi ve mâ"), say('dizi 5 18 23 27', "allâh mulk semâ' ard mâ"), say('say 5:18 24-26', "mulku's-semâvâti ve'l-ard"), say('dizi 5 18 24 26', "mulk semâ' ard"), say('say 5:18 29-30 --on', "ve ileyhi'l-masîr")) + ' '
 "Ölçüm xref 2:284 ve 3:129 (basılmış). Ölçüm nakarat3 altı kalıp: üçü süzgeç GEÇER, üçü GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'yağfiru li-men yeşâ'u' / 've yu'azzibu men yeşâ'' — ayetler arası: yok.",
 "◈K — K1 's-semâvâti' (25. kelime), 'l-ardi' (26. kelime).",
 "◈B — B1 'xalaq' (16. kelime); B2 —; B3 —; B4 —.",
 "◈D — D1 've' + PERF + belirli + 've' + belirli + 'nahnu' + izafet + lafız + 've' + izafet + IMPV + 'fe' + 'li' + 'mâ' + IMPF + 'bi' + izafet + 'bel' + 'entum' + nekre + 'min' + 'men' + PERF + IMPF + 'li' + 'men' + IMPF + 've' + IMPF + 'men' + IMPF + 've' + 'li' + lafız + izafet + belirli + 've' + belirli + 've' + 'mâ' + izafet + 've' + 'ilâ' + belirli; "
 "D2 soru, emir, IMPV ('qul' 8. kelime), INTG ('mâ' 9. kelime); D3 أله ×2 · شيأ ×2 · عذب ×2 · قول ×2; 2:284, 3:129, 30:20, 48:14 ve 64:3 eşleri; 5:17 sûre içi eşi; D4 1P 1 · 2MP 3 · 2MS 1 · 3D 1 · 3FS 1 · 3MS 8, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T18 + "; A2 söz; oğulluk iddiası; sevgi; azap; günah; beşer; yaratma; bağışlama; dileme; mülk; dönüş; A3 'nahnu ebnâ'u'llâhi ve ehibbâ'uh' (söz içi, 4-7. kelime); 'fe-lime yu'azzibukum' … 'l-masîr' (söz içi, 9-30. kelime); "
 "A4 " + BOLUM + "; edim geçişi soru, emir, şart → soru, emir (ayetler arası); şahıs geçişi yok; söz açılır (4. kelime); söz kapanır (7. kelime, ayet içi); söz açılır (9. kelime); söz kapanır (30. kelime, ayet içi).",
)

D[19] = ("◇ 'yâ ehle'l-kitâbi qad câ'akum rasûlunâ yubeyyinu lekum 'alâ fetratin mine'r-rusuli en teqûlû mâ câ'enâ min beşîrin ve lâ nezîrin fe-qad câ'akum beşîrun ve nezîr ve'llâhu 'alâ kulli şey'in qadîr' — "
 "'yâ' + 'ehl' + belirli 'kitâb' + 'qad' + PERF 3MS I. bab + 2MP + 'rasûl' + 1P + IMPF 3MS II. bab + 'li' + 2MP + ''alâ' + nekre 'fetre' + 'min' + belirli çoğul 'rasûl' + 'en' + IMPF 2MP I. bab + 'mâ' + PERF 3MS I. bab + 1P + 'min' + nekre 'beşîr' + 've' + 'lâ' + nekre 'nezîr' + 'fe' + 'qad' + PERF 3MS I. bab + 2MP + nekre 'beşîr' + 've' + nekre 'nezîr' + 've' + lafız + ''alâ' + 'kull' + nekre 'şey'' + nekre 'qadîr' "
 "(ölçüm edim nida, kip CERT 2 · NEG 2 · VOC 1; 1P 2 · 2MP 5 · 3MS 4; bab I. bab ×4 · II. bab ×1). "
 "Allah lafzı 24. sırada (ölçüm allah z=0,19); Rab yok; ölçüm esmâ '{{2|قَدِير 28\\. sırada, SON konum, MÜHÜRSÜZ}}' — satır aynen; esma_kayit çıktısı 'mühür EVET ton celâl' (uyuşmuyor) — 've'llâhu 'alâ kulli şey'in qadîr', kural ''ve'llâhu X' kuralı → ilahi' (okuma); aktör yok (ölçüm). "
 "Ölçüm yıldız ★ — satır yıldız kaynağını adlandırmıyor; kaynak bilançoda; n=28 (n z=1,65); ölçüm '{{2|fâsıla قدير → ر, R sınıfı}}' — satır aynen; ölçüm '{{2|simetri \\[6, 10, 16, 2\\]}}' — satır aynen; ölçüm '{{2|harf 116 → harf3 105, isaret 11}}' — satır aynen; ölçüm '{{2|dış düğüm 2}}' — satır aynen; ölçüm '{{2|İÇ düğüm 1}}' — satır aynen. "
 "Ölçüm CERT 2: 'qad' (3. ve 20. kelime); NEG 2: 'mâ' (14. kelime), 'lâ' (18. kelime); VOC 1: 'yâ' (1. kelime) (okuma); 'en' (12. kelime) morph SUB — 'teqûlû' masdar, olumsuzluk takdiri (okuma). "
 "Kök ikilemeleri (ölçüm) بشر ×2: 'beşîrin' (17. kelime) / 'beşîrun' (22. kelime); جيأ ×3: 'câ'akum' (4. ve 21. kelime) / 'câ'enâ' (15. kelime); رسل ×2: 'rasûlunâ' (5. kelime) / 'r-rusuli' (11. kelime); نذر ×2: 'nezîrin' (19. kelime) / 'nezîr' (23. kelime) (okuma). "
 "'ve lâ' (18.) ve 've nezîr' (23.)'deki 've' morph CONJ; 'fe-qad' (20.)'daki 'fe' REM; 've'llâhu' (24.)'daki 've' REM (okuma). "
 + T19 + " (okuma). "
 + cumle(say('say 5:19 1-5', "yâ ehle'l-kitâbi qad câ'akum rasûlunâ", True), say('say 5:19 1-7', "yâ ehle'l-kitâbi qad câ'akum rasûlunâ yubeyyinu lekum"), say('dizi 5 19 1 7', "ehl kitâb qad câ'e rasûl beyyen li"), say('say 5:19 8-11', "'alâ fetratin mine'r-rusul"), say('lem 5:19:9', "fetre")) + ' '
 + cumle(say('say 5:19 12-19', "en teqûlû mâ câ'enâ min beşîrin ve lâ nezîr", True), say('say 5:19 12-14', "en teqûlû mâ"), say('dizi 5 19 12 14', "en qâle mâ"), say('say 5:19 14-16', "mâ câ'enâ min"), say('dizi 5 19 14 16', "mâ câ'e min"), say('say 5:19 14-19', "mâ câ'enâ min beşîrin ve lâ nezîr")) + ' '
 + cumle(say('say 5:19 20-23 --on', "fe-qad câ'akum beşîrun ve nezîr", True), say('say 5:19 22-23', "beşîrun ve nezîr")) + ' '
 + cumle(say('say 5:19 24-28 --on', "ve'llâhu 'alâ kulli şey'in qadîr", True), say('say 5:19 24-28', "ve'llâhu 'alâ kulli şey'in qadîr"), say('dizi 5 19 24 28', "allâh 'alâ kull şey' qadîr"), say('say 5:19 25-28', "'alâ kulli şey'in qadîr"), say('dizi 5 19 25 28', "'alâ kull şey' qadîr"), say('say 5:19 25-27', "'alâ kulli şey'"), say('dizi 5 19 25 27', "'alâ kull şey'")) + ' '
 "Ölçüm xref 5:15 (basılmış), okunmuş bir ayet, okunmamış bir ayet. Ölçüm nakarat3 altı kalıp: dördü süzgeç GEÇER, ikisi GEÇMEZ. "
 "Karşıt çift (aday 1039, okuma): ayet içi: 'mâ câ'enâ min beşîrin ve lâ nezîr' / 'fe-qad câ'akum beşîrun ve nezîr' — ayetler arası: yok.",
 "◈K — —",
 "◈B — —",
 "◈D — D1 'yâ' + izafet + belirli + 'qad' + PERF + izafet + IMPF + 'li' + ''alâ' + nekre + 'min' + belirli + 'en' + IMPF + 'mâ' + PERF + 'min' + nekre + 've' + 'lâ' + nekre + 'fe' + 'qad' + PERF + nekre + 've' + nekre + 've' + lafız + ''alâ' + izafet + nekre + nekre; "
 "D2 nida, CERT ('qad' 3. ve 20. kelime), NEG ('mâ' 14. kelime, 'lâ' 18. kelime), VOC ('yâ' 1. kelime); D3 بشر ×2 · جيأ ×3 · رسل ×2 · نذر ×2; 5:15 ve 5:17 sûre içi eşleri; D4 1P 2 · 2MP 5 · 3MS 4, sahset ['1', '2', '3'], iltifât 0.",
 "◈A — A1 " + T19 + "; aktör yok (ölçüm); A2 elçinin gelişi; açıklama; elçilere ara verilmesi; müjdeci; uyarıcı; güç yetirme; A3 'mâ câ'enâ min beşîrin ve lâ nezîr' (söz içi, 14-19. kelime); "
 "A4 " + BOLUM + "; hitap açılır ('yâ ehle'l-kitâbi', 1-2. kelime); edim geçişi soru, emir → nida (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası); söz açılır (14. kelime); söz kapanır (19. kelime, ayet içi); bölüm kapanışı.",
)

out = ['# ── blok 5:18-19 (2026-11-15) ──', 'MEAL7 = {']
for n in range(18, 20):
    assert '\\' not in MEAL[n] and '"' not in MEAL[n]
    out.append(' %d: "%s",' % (n, MEAL[n]))
out += ['}', 'M7 = {']
for n in range(18, 20):
    lines = [kes(l) for l in D[n]]
    for l in lines:
        assert '"' not in l and '\\' not in l and '{{' not in l, (n, l[:80])
    s = ' %d: "%s\\n"\n' % (n, lines[0])
    s += '\n'.join('    "%s\\n"' % l for l in lines[1:-1]) + '\n'
    s += '    "%s",' % lines[-1]
    out.append(s)
out += ['}', 'MEAL.update(MEAL7); M.update(M7)']
open('/home/claude/yamalar/metin_5_18_19.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('yazıldı')
