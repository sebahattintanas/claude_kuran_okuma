# blok 7 (5:18-19) ARIZA oluşturucu — bölüm 3-3 (bölüm kapanışı)
import sys, os, ast, subprocess, re
os.environ['OLC'] = '/home/claude/b07/olcum.txt'
os.environ['SAY2'] = '/home/claude/b07/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

VF_YAZI = {18: {1: "'ve qâleti'", 3: "'ve'n-nasârâ'", 7: "'ve ehibbâ'uh'", 9: "'fe-lime'", 20: "'ve yu'azzibu'", 23: "'ve li'llâhi'", 26: "'ve'l-ardi'", 27: "'ve mâ'", 29: "'ve ileyhi'"},
           19: {18: "'ve lâ'", 20: "'fe-qad'", 23: "'ve nezîr'", 24: "'ve'llâhu'"}}
BOL = "'İsrâiloğullarının ve Nasârâ'nın misakı; kitap ehline gelen elçi; Mesih hakkında söz'"


def sd(key):
    return sayim.S2[key][1]


def sic(key):
    n, d = sayim.S2[key]
    return 1 + len([x for x in d['basilan'] if x.startswith('5:')]) + d['okunmus_si'] + d['henuz_si']


def taban(key, ay):
    n, d = sayim.S2[key]
    p = [ay] + [x for x in d['basilan'] if x.startswith('5:') and x != ay]
    if d['okunmus_si']: p.append('okunmus_si %d' % d['okunmus_si'])
    if d['henuz_si']: p.append('henuz_si %d' % d['henuz_si'])
    return ' + '.join(p)



TT = "biçim farkı — eş okunmamış, ayrıntı test edilmedi"
R5 = [
 ("5:18", "'allâh mulk semâ' ard mâ beyn'", 2, 'say 5:18 23-28', "harekesiz 've li'llâhi mulku's-semâvâti ve'l-ardi ve mâ beynehumâ' (23-28. kelime)", None),
 ("5:18", "'allâh mulk semâ' ard mâ'", 3, 'say 5:18 23-27', "harekesiz 've li'llâhi mulku's-semâvâti ve'l-ardi ve mâ' (23-27. kelime)", ('dizi 5 18 23 27', "allâh mulk semâ' ard mâ", '23-27', TT)),
 ("5:18", "'mulk semâ' ard'", 4, 'say 5:18 24-26', "harekesiz 'mulku's-semâvâti ve'l-ard' (24-26. kelime)", None),
 ("5:18", "'ğafere li men şâ'e'", 2, 'say 5:18 17-19', "harekesiz 'yağfiru li-men yeşâ'' (17-19. kelime)", ('dizi 5 18 17 19', "ğafere li men şâ'e", '17-19', TT)),
 ("5:18", "''azzebe men şâ'e'", 2, 'say 5:18 20-22', "harekesiz 've yu'azzibu men yeşâ'' (20-22. kelime)", ('dizi 5 18 20 22', "'azzebe men şâ'e", '20-22', TT)),
 ("5:18", "'men şâ'e allâh'", 2, 'say 5:18 21-23', "harekesiz 'men yeşâ' ve li'llâh' (21-23. kelime)", ('dizi 5 18 21 23', "men şâ'e allâh", '21-23', None)),
 ("5:19", "'ehl kitâb qad câ'e rasûl beyyen li' (LEM 'beyyen' morph LEM ham biçim)", 2, 'say 5:19 1-7', "harekesiz 'yâ ehle'l-kitâbi qad câ'akum rasûlunâ yubeyyinu lekum' (1-7. kelime)", None),
 ("5:19", "'allâh 'alâ kull şey' qadîr'", 3, 'say 5:19 24-28', "harekesiz 've'llâhu 'alâ kulli şey'in qadîr' (24-28. kelime)", None),
 ("5:19", "''alâ kull şey' qadîr'", 4, 'say 5:19 25-28', "harekesiz ''alâ kulli şey'in qadîr' (25-28. kelime)", None),
 ("5:19", "''alâ kull şey''", 5, 'say 5:19 25-27', "harekesiz ''alâ kulli şey'' (25-27. kelime)", None),
 ("5:19", "'en qâle mâ'", 2, 'say 5:19 12-14', "harekesiz 'en teqûlû mâ' (12-14. kelime)", ('dizi 5 19 12 14', "en qâle mâ", '12-14', TT)),
 ("5:19", "'mâ câ'e min'", 2, 'say 5:19 14-16', "harekesiz 'mâ câ'enâ min' (14-16. kelime)", ('dizi 5 19 14 16', "mâ câ'e min", '14-16', TT)),
]
r5 = []
for ay, kal, nk, key, ad, dz in R5:
    s = sic(key)
    h = "%s nakarat3 %s %d (tür ic) / %s sûre içi %d (%s)" % (ay, kal, nk, ad, s, taban(key, ay))
    if s == nk:
        h += ' — tutuyor'
    else:
        dk, dad, dar, ger = dz
        ds = sic(dk)
        if ds == nk:
            h += " — tutmuyor; eşit aralıkla lemma dizisi '%s' (%s. kelime) sûre içi %d (%s) — tutuyor; gerekçe %s" % (dad, dar, ds, taban(dk, ay), ger)
        else:
            h += (" — tutmuyor; eşit aralıkla lemma dizisi '%s' (%s. kelime) sûre içi %d (%s)" % (dad, dar, ds, taban(dk, ay))
                  + ('; tutmuyor — lemma dizisindeki fazla sûre içi eş okunmamış (fark test edilmedi)' if (sd(key)['henuz_si'] or sd(dk)['henuz_si']) else ''))
    r5.append(h)

K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k}

M18 = ("5:18 'Yahudiler ve Nasârâ … dediler' ('ve qâleti'l-yehûdu ve'n-nasârâ', 've' 1. kelimede karşılıksız (morph CONJ; ayet başı), 'de-' 'qâlet' karşılığı (1. kelime; 3FS — topluluk uyumu; çoğul '-ler'), 'Yahudi' 'yehûd' karşılığı (2. kelime; özel ad; çoğul '-ler'), "
 "'ve' 3. kelimede 've' ile (morph CONJ), 'Nasârâ' 'nasrânî' karşılığı (3. kelime; özel ad — çoğul biçim), sıralama: söz araya, fiil sona alındı); "
 "'Biz Allah'ın oğulları ve sevdikleriyiz' ('nahnu ebnâ'u'llâhi ve ehibbâ'uh', 'nahnu' 4. kelimede 'biz' ile, 'oğul' 'ibn' karşılığı (5. kelime; çoğul '-lar'; iyelik), lafız 6. kelimede 'Allah'ın' ile ('-ın' takdir — izafet), 've' 7. kelimede 've' ile (morph CONJ), "
 "'sevdik' 'ehibbâ'' açılımı (7. kelime; çoğul; LEM 'ehibbâ'' — çoğul biçim (morph LEM ham biçim)), 'hû' 7. kelimede iyelik ile ('sevdikleri' içinde), '-yiz' takdir (7. kelime; 1P haber eki — 'biz' ile ortak)); "
 "'De ki' ('qul', 'de-' 'qul' karşılığı (8. kelime; emir 2MS), 'ki' takdir (8. kelime; söz açılışı)); "
 "'Öyleyse günahlarınız yüzünden size neden azap ediyor' ('fe-lime yu'azzibukum bi-zunûbikum', 'fe' 9. kelimede 'öyleyse' ile (morph REM), 'li' 9. kelimede karşılıksız ('neden' içinde), 'mâ' 9. kelimede 'neden' ile (soru; morph INTG), 'azap et-' 'yu'azzibu' açılımı (10. kelime; II. bab; '-iyor'), "
 "'kum' 10. kelimede 'size' ile ('-e' fiil yönetimi takdiri), 'bi' 11. kelimede 'yüzünden' ile (sebep), 'günah' 'zenb' karşılığı (11. kelime; çoğul '-lar'), 'kum' 11. kelimede '-ınız' iyelik ile, sıralama: sebep öne, fiil sona alındı); "
 "'Hayır, siz O'nun yarattıklarından bir beşersiniz' ('bel entum beşerun mimmen xalaq', 'bel' 12. kelimede 'hayır' ile (morph INC), 'entum' 13. kelimede 'siz' ile, 'beşer' 'beşer' karşılığı (14. kelime; nekre — 'bir' takdiri; '-siniz' haber eki), 'min' 15. kelimede '-dan' ile, "
 "'men' 15. kelimede '-dıkları' ile (ilgi), 'yarat-' 'xalaqa' karşılığı (16. kelime), 'O'nun' takdir (16. kelime; fail zamiri — gönderge lafız), sıralama: haber sona alındı); "
 "'Dilediğini bağışlar, dilediğine azap eder' ('yağfiru li-men yeşâ'u ve yu'azzibu men yeşâ'', 'bağışla-' 'yağfiru' karşılığı (17. kelime; geniş zaman), 'li' 18. kelimede karşılıksız (mef'ûl belirtme ile), 'men' 18. kelimede '-diğini' ile (ilgi), 'dile-' 'yeşâ'u' karşılığı (19. kelime), "
 "'ve' 20. kelimede karşılıksız (virgül; morph CONJ), 'azap et-' 'yu'azzibu' açılımı (20. kelime; II. bab; geniş zaman), 'men' 21. kelimede '-diğine' ile (ilgi; '-e' fiil yönetimi takdiri), 'dile-' 'yeşâ'' karşılığı (22. kelime), sıralama: tümleç öne, fiil sona alındı); "
 "'Göklerin, yerin ve ikisi arasındakilerin mülkü Allah'ındır' ('ve li'llâhi mulku's-semâvâti ve'l-ardi ve mâ beynehumâ', 've' 23. kelimede karşılıksız (nokta; morph REM), 'li' 23. kelimede '-ın' ile (aidiyet), lafız 23. kelimede 'Allah' ile, 'mülk' 'mulk' karşılığı (24. kelime; '-ü' iyelik), "
 "'gök' 'semâ'' karşılığı (25. kelime; çoğul '-ler'; izafet), 've' 26. kelimede karşılıksız (virgül; morph CONJ), 'yer' 'ard' karşılığı (26. kelime; izafet), 've' 27. kelimede 've' ile (morph CONJ), 'mâ' 27. kelimede '-kiler' ile (ilgi), "
 "'ara' 'beyn' karşılığı (28. kelime; yer eki takdiri), 'humâ' 28. kelimede 'ikisi' ile (ikil), '-dır' takdir (23. kelime; isim cümlesi), sıralama: haber sona alındı); "
 "'dönüş de O'nadır' ('ve ileyhi'l-masîr', 've' 29. kelimede 'de' ile (morph CONJ), 'ilâ' 29. kelimede yönelme eki ile ('O'na' içinde), 'hî' 29. kelimede 'O' ile (gönderge lafız), 'dönüş' 'masîr' karşılığı (30. kelime), '-dır' takdir (29. kelime; isim cümlesi), sıralama: haber sona alındı)")
M19 = ("5:19 'Ey kitap ehli' ('yâ ehle'l-kitâb', 'yâ' 1. kelimede 'ey' ile (morph VOC), 'ehil' 'ehl' karşılığı (1. kelime; '-i' iyelik takdiri), 'kitap' 'kitâb' karşılığı (2. kelime; izafet), sıralama: izafet Türkçe sırasıyla); "
 "'Elçimiz size geldi' ('qad câ'akum rasûlunâ', 'qad' 3. kelimede karşılıksız (morph CERT; geçmiş '-di' içinde), 'gel-' 'câ'a' karşılığı (4. kelime), 'kum' 4. kelimede 'size' ile ('-e' fiil yönetimi takdiri), 'elçi' 'rasûl' karşılığı (5. kelime), 'nâ' 5. kelimede '-miz' iyelik ile, sıralama: fail öne, fiil sona alındı); "
 "'elçilere ara verilmiş bir dönemde size açıklıyor' ('yubeyyinu lekum 'alâ fetratin mine'r-rusul', 'açıkla-' 'yubeyyinu' karşılığı (6. kelime; II. bab; LEM 'beyyen' (morph LEM ham biçim)), 'li' 7. kelimede '-e' ile, 'kum' 7. kelimede 'siz' ile, ''alâ' 8. kelimede '-de' ile (zaman), "
 "'ara verilmiş dönem' 'fetre' açılımı (9. kelime; nekre — 'bir' takdiri), 'min' 10. kelimede yönelme eki ile ('elçilere' içinde), 'elçi' 'rasûl' karşılığı (11. kelime; çoğul '-ler'), sıralama: zaman öne, fiil sona alındı); "
 "'demeyesiniz diye' ('en teqûlû', 'en' 12. kelimede 'diye' ile (masdar; morph SUB; olumsuzluk '-me-' takdiri), 'de-' 'teqûlû' karşılığı (13. kelime; istek kipi), 'û' 13. kelimede 2MP ile ('demeyesiniz' içinde)); "
 "'Bize ne bir müjdeci ne de bir uyarıcı geldi' ('mâ câ'enâ min beşîrin ve lâ nezîr', 'mâ' 14. kelimede olumsuzluk ile ('ne … ne de' içinde; morph NEG), 'gel-' 'câ'e' karşılığı (15. kelime), 'nâ' 15. kelimede 'bize' ile ('-e' fiil yönetimi takdiri), 'min' 16. kelimede karşılıksız (kapsam pekiştirmesi), "
 "'müjdeci' 'beşîr' karşılığı (17. kelime; nekre — 'bir' takdiri), 've' 18. kelimede karşılıksız ('ne de' içinde; morph CONJ), 'lâ' 18. kelimede 'ne de' ile (morph NEG), 'uyarıcı' 'nezîr' karşılığı (19. kelime; nekre — 'bir' takdiri), sıralama: söz öne alındı); "
 "'İşte size bir müjdeci ve bir uyarıcı geldi' ('fe-qad câ'akum beşîrun ve nezîr', 'fe' 20. kelimede 'işte' ile (morph REM), 'qad' 20. kelimede karşılıksız (morph CERT), 'gel-' 'câ'a' karşılığı (21. kelime), 'kum' 21. kelimede 'size' ile ('-e' fiil yönetimi takdiri), "
 "'müjdeci' 'beşîr' karşılığı (22. kelime; nekre — 'bir' takdiri), 've' 23. kelimede 've' ile (morph CONJ), 'uyarıcı' 'nezîr' karşılığı (23. kelime; nekre — 'bir' takdiri), sıralama: fiil sona alındı); "
 "'Allah her şeye güç yetirendir' ('ve'llâhu 'alâ kulli şey'in qadîr', 've' 24. kelimede karşılıksız (nokta; morph REM), lafız 24. kelimede 'Allah' ile, ''alâ' 25. kelimede '-e' ile ('-e' fiil yönetimi takdiri), 'her' 'kull' karşılığı (26. kelime), 'şey' 'şey'' karşılığı (27. kelime), "
 "'güç yetiren' 'qadîr' açılımı (28. kelime), '-dir' takdir (28. kelime), sıralama: haber sona alındı)")
MEALS = (M18, M19)


def _bol(s, sep):
    out, d, cur, i = [], 0, '', 0
    while i < len(s):
        c = s[i]
        if c == '(': d += 1
        elif c == ')': d -= 1
        if d == 0 and s.startswith(sep, i):
            out.append(cur); cur = ''; i += len(sep); continue
        cur += c; i += 1
    out.append(cur)
    return out


MK = {}
for blok in MEALS:
    n = int(blok.split(' ', 1)[0].split(':')[1]); govde = blok.split(' ', 1)[1]
    for seg in _bol(govde, "; '"):
        seg = seg if seg.startswith("'") else "'" + seg
        j = seg.index("' (")
        tr = seg[1:j]; ic = seg[j + 3:].rstrip(')')
        parca = _bol(ic, ', ')
        MK.setdefault(n, []).append((tr, parca[0].strip("'"), parca[1:]))
open('/home/claude/b07/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '7')
ESL = run('/home/claude/sunum/es_lemma.py', '5', '7').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '7').replace('\n', '; ')
EMS = open('/home/claude/b07/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '18', '19', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b07/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
MFARK = [(k, n, sayim.S2[k.replace(' --medde', '')][0]) for k, (n, d) in sayim.S2.items() if '--medde' in k]
MEDF = '; '.join("%s meddeli %d / meddesiz %d" % (k.replace(' --medde', ''), m, n) for k, n, m in MFARK)
MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else ' — FARK VAR'


I = [
 "kök tablosu: ölçümde '???' 5:18 ve 5:19 için ayrı sayıldı — 0; yeni kök yok (okunan ayetlerde tabloda olmayan kök 0); ölçüm glossunun karşılamadığı kullanımlar (bölüm 2 denetimi kuralı 9, tarama): kök بني 'bina, yapma' 5:18 'ebnâ'u' (oğullar) kullanımını kapsamıyor (bloklar 5-6'da da kayıtlı); "
 "kök نصر 'yardım' 5:18 'n-nasârâ' (özel ad) kullanımını kapsamıyor (blok 5'te de kayıtlı); kök هود 'Yahudi olma; Hûd' 5:18 'l-yehûdu' kullanımını kapsıyor; kök فتر 'gevşeme, ara verme' 5:19 'fetratin'; kök صير 'dönüşme, varış' 5:18 'l-masîr'; kök بشر 'müjde; beşer' 5:18 'beşerun' ve 5:19 'beşîr' — iki anlamı da kapsıyor; tam okuma sonu",
 "esmâ: 5:19:28 قَدِير 'ilahi' — 've'llâhu 'alâ kulli şey'in qadîr', kural ''ve'llâhu X' kuralı → ilahi' (esma_el_ekle → esma_kayit; e_el=? 0); kural adı kapalı listeyle karşılaştırıldı; 5:18 esmâ yok; lafız 5:18 iki, 5:19 bir geçiş; Rab yok",
 "esma_kayit: 5:18 'mühür hayır' (uyuşuyor; ölçüm esmâ yok); 5:19 ölçüm esmâ '{{2|قَدِير 28\\. sırada, SON konum, MÜHÜRSÜZ}}' / esma_kayit 'mühür EVET ton celâl' (uyuşmuyor) — mühür ölçütleri farklı (araç tanımı farkı)",
 "ölçüm: 5:18 '{{1|fâsıla ٱلمصير → ر, R sınıfı}}', '{{1|simetri \\[3, 4, 21, 1\\]}}', '{{1|harf 138 → harf3 130, isaret 8}}' ve '{{1|dış düğüm 2}}'; 5:19 '{{2|fâsıla قدير → ر, R sınıfı}}', '{{2|simetri \\[6, 10, 16, 2\\]}}', '{{2|harf 116 → harf3 105, isaret 11}}', '{{2|dış düğüm 2}}' ve '{{2|İÇ düğüm 1}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); 5:18'de İÇ düğüm alanı yok",
 "ölçüm aktör: 5:18 '{{1|adlı يَهُود 2\\. sırada \\(cins, rol fail\\+konusan\\)}}', '{{1|adlı نَصْرانِيّ 3\\. sırada \\(cins, rol fail\\)}}' — sözdiziminde 'qâlet' faili ve sözün sahibi; ölçüm Yahudilere 'konusan' rolü veriyor, Nasârâ'ya vermiyor — atıflı iki fail ayırt ediliyor (araç tanımı farkı, §8); 5:19 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:18 soru, emir — IMPV 1 'qul' (8.), INTG 1 'mâ' (9., 'lime' içinde); 5:19 nida — CERT 2 'qad' (3., 20.), NEG 2 'mâ' (14.), 'lâ' (18.), VOC 1 'yâ' (1.); 5:19 'en' (12.) morph SUB; blokta edilgen fiil yok",
 "yıldız: 5:18 ★, 5:19 ★ — satır yıldız kaynağını adlandırmıyor; kaynak kapanış notunda bilançodan",
 "fâsıla: 5:17 ر (قدير) → 5:18 ر (ٱلمصير) → 5:19 ر (قدير); bölüm sonu R sınıfında üç ayet; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:18 xref 2:284 ve 3:129 (basılmış); 5:19 xref 5:15 (basılmış), okunmuş bir ayet, okunmamış bir ayet — sınıflama sinifla.py ile, basılmamışlar numarasız",
 "nakarat3 (R3: sayıyla özetlendi): 5:18 altı kalıp: üçü süzgeç GEÇER, üçü GEÇMEZ; 5:19 altı kalıp: dördü süzgeç GEÇER, ikisi GEÇMEZ; bütün kalıplar tür ic",
 "araç tanımı farkları (R5; bölüm 2 denetimi kuralı 1: nakarat3 'tür' alanı 'tam' ya da 'ic' — ikisi de sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si — taban sayımın kendi sözlüğünden betikle; karşılaştırma eşit aralıkla; nakarat3 kalıp adları ham LEM ile, bozuk LEM notlu): " + '; '.join(r5),
 "aktör / ad (1017, R1): 5:18 'l-yehûdu ve'n-nasârâ' (adlı cinsler), söz içi konuşan 1P ('nahnu'), Allah (lafız), muhatap 2MS (adsız; 'qul'), muhatap 2MP (adsız — Yahudiler ve Nasârâ), 3MS (adsız — lafız), 'beşerun', 'men', 3D 'beynehumâ', 'l-masîr'; "
 "5:19 muhatap 2MP (adsız; nidâ 'ehle'l-kitâbi'), 'rasûlunâ', konuşan 1P (adsız), 3MS (adsız — elçi), 'r-rusuli', söz içi 1P ('câ'enâ'), 'beşîr' / 'nezîr' (nekre), Allah (lafız) — A1'e yazılmayanlar: 5:18 'mimmen' içindeki 'men' (A1'de 'men' olarak anıldı), 5:19 'lekum' (muhatap içinde); blokta 'kâne / leyse' ismi nekre yok",
 "söz / tırnak: 5:18 'qâlet' (1. kelime) — söz 4. kelimede açılıyor, 7. kelimede kapanıyor ('nahnu ebnâ'u'llâhi ve ehibbâ'uh'); 'qul' (8. kelime) — söz 9. kelimede açılıyor, 30. kelimede ayet sonunda kapanıyor (23. kelime 've li'llâhi' morph REM — söz içinde de okunabilir; okuma kararı: ayet sonuna dek söz, tam okuma sonu); "
 "5:19 'en teqûlû' (13. kelime) — varsayılan söz 14-19. kelime ('mâ câ'enâ min beşîrin ve lâ nezîr'; 20. kelime 'fe-qad' REM — söz dışı); morph 've' / 'fe' konumlarıyla kontrol edildi: 5:18 've qâleti' (1.), 've'n-nasârâ' (3.), 've ehibbâ'uh' (7.), 've yu'azzibu' (20.), 've'l-ardi' (26.), 've mâ' (27.), 've ileyhi' (29.) CONJ, "
 "'fe-lime' (9.) REM, 've li'llâhi' (23.) REM; 5:19 've lâ' (18.), 've nezîr' (23.) CONJ, 'fe-qad' (20.) REM, 've'llâhu' (24.) REM",
 "◈ tetik (alıntılar önek ve edatsız): 5:18 ◈K سمو ('s-semâvâti' 25. kelime — K1), أرض ('l-ardi' 26. kelime — K1); 5:18 ◈B خلق ('xalaq' 16. kelime — B1); 5:19 tetik yok; "
 "tetik listesinde olmayan zaman adı ve organ adı (bölüm 2 denetimi kuralı 9, tarama): 5:19 'fetratin' (9. kelime; ara dönem — zaman adı, tetik dışı); 5:18 'l-masîr' (30. kelime; varış — zaman / yer adı, tetik dışı); 5:18 'beşerun' (14. kelime; insan — B1 kökü أنس değil, tetik dışı); organ adı yok; oturum_tetik kuru koşu 2 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:18 (2:284, 3:129, 30:20, 48:14, 64:3; 5:17 sûre içi), 5:19 (5:15 ve 5:17 sûre içi) (kontrol.py ile); bölüm içi blok geçişi 5:17 → 5:18 ('ve li'llâhi mulku's-semâvâti ve'l-ardi ve mâ beynehumâ') ve 5:17 → 5:19 ('ve'llâhu 'alâ kulli şey'in qadîr'); "
 "5:15 → 5:19 bağı yedi kelimelik kalıpla ('yâ ehle'l-kitâbi qad câ'akum rasûlunâ yubeyyinu lekum') — bölüm 2 denetimi kuralı 10'daki genel hitap 'yâ ehle'l-kitâb' (iki kelime) bağ ölçütü değil, blok 6 kararı sürüyor; 5:15 ve 5:17'nin D3 satırları geriye dönük güncellenmedi (bağ bu blokta kayıtlı); "
 "D3 dışı bırakılan basılmış sayım eşleri: 5:19 lemma dizisi 'mâ câ'e min' sayımındaki 60:1 (genel dizi; bağı blok 5'te); 5:19 ''alâ kulli şey'' sayımlarındaki 2:284 (genel kalıp; bağları 5:17 ve 5:18'de)",
 "◈A A4 (R9 + kapsam): 5:18 edim geçişi soru, emir, şart → soru, emir (ayetler arası); şahıs geçişi yok (3 → 3); söz açılır / kapanır (4-7. ve 9-30. kelime); 5:19 hitap açılır ('yâ ehle'l-kitâbi', 1-2. kelime); edim geçişi soru, emir → nida (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası); söz açılır (14. kelime); söz kapanır (19. kelime); bölüm kapanışı",
 "sözdizimi (okuma; 'atıf' / 'istînâf' / 'hâl' her geçişte morph etiketiyle; 'X'a atıf' yazımında X ma'tûf aleyh): 5:18 've qâleti'l-yehûdu' — 5:17'ye atıf (morph CONJ); 've'n-nasârâ' — 'l-yehûdu'ya atıf (morph CONJ); 'nahnu ebnâ'u'llâhi' — söz, isim cümlesi; 've ehibbâ'uh' — 'ebnâ'u'ya atıf (morph CONJ); 'qul' — emir; "
 "'fe-lime yu'azzibukum' — istînâf (morph REM), soru; 'bel entum beşerun' — idrâb (morph INC); 'mimmen xalaq' — 'beşerun'un sıfatı; 'yağfiru li-men yeşâ'u' — yeni cümle (morph etiketi yok); 've yu'azzibu' — 'yağfiru'ya atıf (morph CONJ); 've li'llâhi mulku' — istînâf (morph REM); 've ileyhi'l-masîr' — 've li'llâhi'ye atıf (morph CONJ); "
 "5:19 'yâ ehle'l-kitâbi' — nidâ; 'yubeyyinu lekum' — 'rasûlunâ'nın hâli ya da sıfatı (morph etiketi yok); ''alâ fetratin' — zaman; 'en teqûlû' — masdar (morph SUB), 'li-' / 'lâ' takdirli; 've lâ nezîrin' — 'beşîrin'e atıf (morph CONJ); 'fe-qad câ'akum' — istînâf (morph REM); 've'llâhu' — istînâf (morph REM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile denetlendi; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için): 5:19 'yâ ehle'l-kitâbi qad câ'akum rasûlunâ yubeyyinu lekum' ile açılıyor (1-7. kelime) — 5:15 açılışıyla yedi kelime eş (ölçüm nakarat3 süzgeç GEÇER), bölüm içinde hitap ve elçi bildirimi iki geçiş; "
 "5:18 've li'llâhi mulku's-semâvâti ve'l-ardi ve mâ beynehumâ' (23-28. kelime) 5:17 (29-34. kelime) ile eş; 5:19 ''alâ kulli şey'in qadîr' 5:17 ile eş — bölümün iki ayetinde kudret kapanışı; 5:18 'ebnâ'u' — 5:17 ''bnu meryem' ile kök بني, oğulluk iddiası 5:17 (Mesih) ve 5:18'de (kitap ehli); "
 "5:18 'yağfiru li-men yeşâ'u ve yu'azzibu men yeşâ'' 3:129 ve 48:14 ile; 5:19 'beşîr' iki geçiş (17. ve 22. kelime), 'nezîr' iki geçiş (19. ve 23. kelime) — söz içinde olumsuz, söz dışında olumlu",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (sunum/es_edat.py — morph etiketli, zamirler birleşik): " + ES
 + "; eş lemmaya farklı karşılık (sunum/es_lemma.py, bloklar 5-7): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (bölüm 2 denetimi kuralı 6): 'ğafere' / ''azzebe' 5:18 'bağışla-' / 'azap et-' — 3:129 ve 48:14 (eş); 'mulk' 5:18 'mülk' / 48:14 'mülk' (eş); 'beşer' 5:18 'beşer' / 30:20 'insan' (fark); 'masîr' 5:18 'dönüş' / 64:3 'dönüş' (eş) — tam okuma sonu",
 "KARSILIK_CAKISMA",
 "çıpa: 5:18 ve 5:19 tarayıcı vermedi (cipa_tarama5_adaylari.json); mülk ve dönüş bildirimi, elçinin gelişi bildirimi (olgu=False); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:18 ('yağfiru li-men yeşâ'u' / 've yu'azzibu men yeşâ''; 'nahnu ebnâ'u'llâhi' / 'bel entum beşerun'), 5:19 ('mâ câ'enâ min beşîrin ve lâ nezîr' / 'fe-qad câ'akum beşîrun ve nezîr') — okuma; ayetler arası yok",
 "aday 1041: kök حبب 5:18 'ehibbâ'uh' — insanların kendilerini lafzın sevdikleri olarak anması (söz içi iddia); kök بني 5:18 'ebnâ'u'llâhi' — lafza izafe edilen oğulluk iddiası, 'bel entum beşerun' ile reddediliyor — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 3-3 — bölüm kapanışı 5:19; bölüm üç blok (blok planından: 5, 6 ve 7); başlıktaki 'İsrâiloğullarının ve Nasârâ'nın misakı' (5:12, 5:14), 'kitap ehline gelen elçi' (5:15, 5:19) ve 'Mesih hakkında söz' (5:17) bölüm içinde kapsandı; 5:18 Yahudiler ve Nasârâ'nın oğulluk sözü; mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; "
 "bölüm sonu bağımsız denetimi bu bloktan sonra (bulgular yamalar/bekleyen_ariza_5_b07.txt); medde taraması (bölüm 2 denetimi kuralı 2; sunum/medde.py b07/say2.txt — --medde satırları say2'de): " + MED + "; " + MEDF,
 "ham LEM (bölüm 2 denetimi kuralları 4-5; sunum/lem_bozuk.py 07): 5:19:6 'beyyen' — meal maddesinde ve R5 kalıp adında '(morph LEM ham biçim)' notlu; aracın bayraklamadığı ham biçim: 5:18:7 'ehibbâ'' (çoğul biçim LEM) — notlu",
 "sonradan basılan (bölüm 8 kuralı 1; bölüm 16 denetimi kuralı 3; bölüm 1 denetimi kuralı 1 — lemma dizileri dahil; sunum/sonradan.py --plan 7): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('yehûd', 'nasrânî', 'ibn', 'ehibbâ'', 'zenb', 'beşer', 'mulk', 'semâ'', 'ard', 'beyn', 'masîr', 'ehl', 'kitâb', 'rasûl', 'fetre', 'beşîr', 'nezîr', 'kull', 'şey'', 'qadîr'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları ve 5:18 'llâhi ve ehibbâ'' hemze sınırı yapıntısı (translit_kontrol 'h' farkı — iskelet tekilleştirmesi hemze ayrımından önce); wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]


def yaz():
    items = [kes(x) for x in I]
    s = '\n (18, 19): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_18_19.txt', 'w', encoding='utf-8').write(s)


idx = I.index('KARSILIK_CAKISMA')
I[idx] = 'karşılık çakışması (geçici)'
yaz()
CAK = run('/home/claude/sunum/cakisma.py', '/home/claude/yamalar/ariza_5_12_14.txt', '/home/claude/yamalar/ariza_5_15_17.txt', '/home/claude/yamalar/ariza_5_18_19.txt')
KARAR = {}
exec(open('/home/claude/b05/yap/karar.py', encoding='utf-8').read())
exec(open('/home/claude/b06/yap/karar.py', encoding='utf-8').read())
if os.path.exists('/home/claude/b07/yap/karar.py'): exec(open('/home/claude/b07/yap/karar.py', encoding='utf-8').read())
I[idx] = ("karşılık çakışması (sunum/cakisma.py bölüm 3 ARIZA meal maddeleri (bloklar 5-7); kararlar morph LEM eşitliğine göre): "
          + ('; '.join(KARAR.get(l.split(' ←')[0], l + ' — karar yok') for l in CAK.splitlines()) if CAK else 'çakışma yok'))
yaz()
print('yazıldı', len(I))
print(CAK)
print('\n'.join(r5))
print(MEDF)
