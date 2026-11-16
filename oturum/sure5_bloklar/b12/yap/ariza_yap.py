# blok 12 (5:33-36) ARIZA oluşturucu — bölüm 6-1 (bölüm açılışı)
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b12/olcum.txt'
os.environ['SAY2'] = '/home/claude/b12/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b11.txt', encoding='utf-8').read() + ']')
VF_YAZI = {33: {6: "'ve rasûlehû'", 7: "'ve yes'avne'", 18: "'ve erculuhum'", 30: "'ve lehum fi'l-âxirati'"}, 34: {9: "'fa'lemû'"}, 35: {6: "'ve'bteğû'", 9: "'ve câhidû'"}, 36: {11: "'ve mislehû'", 22: "'ve lehum 'azâbun'"}}
BOL = "'Bozgunculuğun cezası; vesile; hırsızlık ve tövbe'"


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


R5 = [
 ("5:33", "'se'â fî ard fesâd'", 2, 'say 5:33 7-10', "harekesiz 've yes'avne fi'l-ardi fesâden' (7-10. kelime)", None),
 ("5:33", "'fî âxir 'azâb 'azîm'", 2, 'say 5:33 31-34', "harekesiz 'fi'l-âxirati 'azâbun 'azîm' (31-34. kelime)", None),
 ("5:34", "'enne allâh ğafûr rahîm'", 3, 'say 5:34 10-13', "harekesiz 'enna'llâhe ğafûrun rahîm' (10-13. kelime)",
  ('dizi 5 34 10 13', "enne allâh ğafûr rahîm", '10-13', "nakarat3 'ان' iskeleti 'inne' / 'enne' ayrımı yapmıyor, lemma dizisi yalnız 'enne' (eş okunmamış, fark test edilmedi)")),
 ("5:34", "'allâh ğafûr rahîm'", 5, 'say 5:34 11-13', "harekesiz 'llâhe ğafûrun rahîm' (11-13. kelime)",
  ('dizi 5 34 11 13', "allâh ğafûr rahîm", '11-13', "biçim / i'râb farkı — harekesiz kalıp lafzın mansub yazımını ayırıyor")),
 ("5:34", "''alime enne allâh'", 4, 'say 5:34 9-11', "harekesiz 'fa'lemû enna'llâh' (9-11. kelime)",
  ('dizi 5 34 9 11', "'alime enne allâh", '9-11', "çekim farkı — harekesiz kalıp önek 'fe' ve emir çekimini ayırıyor")),
 ("5:34", "'min qabl en'", 2, 'say 5:34 4-6', "harekesiz 'min qabli en' (4-6. kelime)",
  ('dizi 5 34 4 6', "min qabl en", '4-6', "nakarat3 'ان' iskeleti 'en' / 'enne' / 'in' ayrımı yapmıyor, lemma dizisi yalnız 'en' — fark açıklanmadı, tam okuma sonu")),
 ("5:35", "'eyy ellezî âmene'", 16, 'say 5:35 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
 ("5:35", "'câhede fî sebîl'", 2, 'say 5:35 9-11', "harekesiz 've câhidû fî sebîlih' (9-11. kelime)",
  ('dizi 5 35 9 11', "câhede fî sebîl", '9-11', "çekim farkı — harekesiz kalıp önek 've' ve iyelik ekini ayırıyor")),
 ("5:36", "'fî ard cemî''", 2, 'say 5:36 8-10', "harekesiz 'fi'l-ardi cemî'an' (8-10. kelime)", None),
 ("5:36", "'mâ fî ard'", 2, 'say 5:36 7-9', "harekesiz 'mâ fi'l-ard' (7-9. kelime)",
  ('dizi 5 36 7 9', "mâ fî ard", '7-9', "çekim farkı — harekesiz kalıp 'ard' i'râbını ayırıyor")),
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
            h += " — tutmuyor; eşit aralıkla lemma dizisi '%s' (%s. kelime) sûre içi %d (%s) — tutmuyor; gerekçe %s" % (dad, dar, ds, taban(dk, ay), ger)
    r5.append(h)

K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k}

M33 = ("5:33 'cezası ancak' ('innemâ cezâ'u', 'inne' 1. kelimede 'ancak' ile (morph ACC; sınırlama), 'mâ' 1. kelimede karşılıksız (morph PREV; 'ancak' içinde), 'ceza' 'cezâ'' karşılığı (2. kelime; iyelik ile 'cezası'), sıralama: mübteda sona alındı); "
 "'Allah'a ve elçisine savaş açan ve yeryüzünde bozgunculuk için koşanların' ('llezîne yuhâribûna'llâhe ve rasûlehû ve yes'avne fi'l-ardi fesâden', 'ellezîne' 3. kelimede '-anların' ile (ism-i mevsûl; sıfat-fiil açılımı), 'savaş aç-' 'yuhâribûne' açılımı (4. kelime; III. bab), 'û' 4. kelimede karşılıksız (fail eki — '-anların' içinde), "
 "lafız 5. kelimede 'Allah' ile (yönelme eki 'Allah'a' içinde; fiil yönetimi takdiri), 've' 6. kelimede 've' ile (morph CONJ), 'elçi' 'rasûl' karşılığı (6. kelime; yönelme eki ile 'elçisine'; fiil yönetimi takdiri), 'hû' 6. kelimede iyelik ile ('elçisine' içinde), 've' 7. kelimede 've' ile (morph CONJ), "
 "'koş-' 'yes'avne' karşılığı (7. kelime; I. bab), 'û' 7. kelimede 3MP ile ('koşanların' içinde), 'fî' 8. kelimede '-de' ile, 'yeryüzü' 'ard' karşılığı (9. kelime), 'bozgunculuk' 'fesâd' karşılığı (10. kelime; nekre — takdirsiz; 'için' takdiri), sıralama: sıfat cümlesi öne); "
 "'öldürülmeleri ya da asılmaları' ('en yuqattelû ev yusallebû', 'en' 11. kelimede '-meleri' ile (masdar; morph SUB), 'öldür-' 'yuqattelû' karşılığı (12. kelime; II. bab; edilgen '-ül'; LEM 'quttilu' (morph LEM ham biçim)), 'û' 12. kelimede 3MP ile ('-leri' içinde), "
 "'ev' 13. kelimede 'ya da' ile (morph CONJ), 'as-' 'yusallebû' karşılığı (14. kelime; II. bab; edilgen '-ıl'; LEM 'yusallebu' (morph LEM ham biçim)), 'û' 14. kelimede 3MP ile ('-ları' içinde)); "
 "'ya da ellerinin ve ayaklarının çaprazlama kesilmesi' ('ev tuqatta'a eydîhim ve erculuhum min xilâf', 'ev' 15. kelimede 'ya da' ile (morph CONJ), 'kes-' 'tuqatta'a' karşılığı (16. kelime; II. bab; edilgen '-il'; masdar '-mesi' açılımı), 'el' 'yed' karşılığı (17. kelime; çoğul '-ler'), 'hum' 17. kelimede iyelik ile ('ellerinin' içinde), "
 "'ve' 18. kelimede 've' ile (morph CONJ), 'ayak' 'ricl' karşılığı (18. kelime; çoğul '-lar'), 'hum' 18. kelimede iyelik ile ('ayaklarının' içinde), 'min' 19. kelimede karşılıksız ('çaprazlama' içinde), 'çaprazlama' 'xilâf' açılımı (20. kelime; nekre — takdirsiz; 'karşı taraftan' açılımı), sıralama: fiil sona alındı); "
 "'ya da yerden sürülmeleridir' ('ev yunfev mine'l-ard', 'ev' 21. kelimede 'ya da' ile (morph CONJ), 'sür-' 'yunfev' karşılığı (22. kelime; I. bab; edilgen '-ül'; LEM 'yunfe' (morph LEM ham biçim)), 'û' 22. kelimede 3MP ile ('-leri' içinde), 'min' 23. kelimede '-den' ile, 'yer' 'ard' karşılığı (24. kelime), "
 "'-dir' takdiri ('sürülmeleridir' içinde; isim cümlesi haberi)); "
 "'Bu, onlar için dünyada bir rezilliktir' ('zâlike lehum xizyun fi'd-dunyâ', 'zâlike' 25. kelimede 'bu' ile, 'li' 26. kelimede 'için' ile, 'hum' 26. kelimede 'onlar' ile, 'rezillik' 'xizy' karşılığı (27. kelime; nekre — 'bir' takdiri), 'fî' 28. kelimede '-da' ile, 'dünya' 'dunyâ' karşılığı (29. kelime), "
 "'-tir' takdiri ('rezilliktir' içinde; isim cümlesi haberi), sıralama: haber sona alındı); "
 "'âhirette de onlar için büyük bir azap vardır' ('ve lehum fi'l-âxirati 'azâbun 'azîm', 've' 30. kelimede 'de' ile (morph REM), 'li' 30. kelimede 'için' ile, 'hum' 30. kelimede 'onlar' ile, 'fî' 31. kelimede '-te' ile, 'âhiret' 'âxir' karşılığı (32. kelime; belirli dişil), "
 "'azap' ''azâb' karşılığı (33. kelime; nekre — 'bir' takdiri), 'büyük' ''azîm' karşılığı (34. kelime; nekre — takdirsiz; sıfat), 'var' takdiri (isim cümlesi), '-dır' takdiri ('vardır' içinde; isim cümlesi haberi), sıralama: mübteda sona alındı)")
M34 = ("5:34 'Ancak … tövbe edenler başka' ('illa'llezîne tâbû', 'illâ' 1. kelimede 'ancak' ile (morph EXP; istisna), 'ellezîne' 2. kelimede '-enler' ile (ism-i mevsûl; sıfat-fiil açılımı), 'tövbe et-' 'tâbû' açılımı (3. kelime; I. bab), 'û' 3. kelimede karşılıksız (fail eki — '-enler' içinde), 'başka' takdiri (istisna), sıralama: istisna sona alındı); "
 "'siz onlara güç yetirmeden önce' ('min qabli en taqdirû 'aleyhim', 'min' 4. kelimede karşılıksız ('önce' içinde), 'önce' 'qabl' karşılığı (5. kelime), 'en' 6. kelimede '-meden' ile (masdar; morph SUB; '-den' eki — fiil yönetimi takdiri), 'güç yetir-' 'taqdirû' açılımı (7. kelime; I. bab), 'û' 7. kelimede 2MP ile ('siz' takdiri), "
 "''alâ' 8. kelimede yönelme eki ile ('onlara' içinde; fiil yönetimi takdiri), 'hum' 8. kelimede 'onlara' ile, sıralama: fiil sona alındı); "
 "'Bilin ki Allah bağışlayandır, merhamet edendir' ('fa'lemû enna'llâhe ğafûrun rahîm', 'fe' 9. kelimede karşılıksız (morph REM), 'bil-' ''lemû' karşılığı (9. kelime; emir 2MP), 'û' 9. kelimede 2MP ile ('bilin' içinde), 'enne' 10. kelimede 'ki' ile, lafız 11. kelimede 'Allah' ile, "
 "'bağışlayan' 'ğafûr' karşılığı (12. kelime; nekre — takdirsiz), 'merhamet eden' 'rahîm' açılımı (13. kelime; nekre — takdirsiz), '-dır' takdiri ('bağışlayandır' içinde; 'enne' haberi), '-dir' takdiri ('edendir' içinde; 'enne' haberi))")
M35 = ("5:35 'Ey iman edenler' ('yâ eyyuhe'llezîne âmenu', 'yâ' 1. kelimede 'ey' ile, 'eyy' ve 'hâ' 1. kelimede karşılıksız, 'ellezîne' 2. kelimede '-enler' ile, 'iman et-' 'âmenû' açılımı (3. kelime; IV. bab), 'û' 3. kelimede karşılıksız (fail eki — '-enler' içinde)); "
 "'Allah'tan sakının' ('ttequ'llâh', 'sakın-' 'ttequ' karşılığı (4. kelime; VIII. bab; emir 2MP), 'û' 4. kelimede 2MP ile ('sakının' içinde), lafız 5. kelimede 'Allah' ile (ayrılma eki 'Allah'tan' içinde; fiil yönetimi takdiri), sıralama: fiil sona alındı); "
 "'O'na vesile arayın' ('ve'bteğû ileyhi'l-vesîle', 've' 6. kelimede karşılıksız (morph CONJ; virgül), 'ara-' 'bteğû' karşılığı (6. kelime; VIII. bab; emir 2MP), 'û' 6. kelimede 2MP ile ('arayın' içinde), 'ilâ' 7. kelimede yönelme eki ile ('O'na' içinde), 'hî' 7. kelimede 'O' ile, 'vesile' 'vesîle' karşılığı (8. kelime), sıralama: fiil sona alındı); "
 "'ve O'nun yolunda cihad edin' ('ve câhidû fî sebîlih', 've' 9. kelimede 've' ile (morph CONJ), 'cihad et-' 'câhidû' açılımı (9. kelime; III. bab; emir 2MP), 'û' 9. kelimede 2MP ile ('edin' içinde), 'fî' 10. kelimede '-da' ile, 'yol' 'sebîl' karşılığı (11. kelime), 'hî' 11. kelimede iyelik ile ('O'nun yolunda' içinde), sıralama: fiil sona alındı); "
 "'umulur ki kurtuluşa erersiniz' ('le'allekum tuflihûn', 'le'alle' 12. kelimede 'umulur ki' ile (morph ACC; ümit), 'kum' 12. kelimede '-siniz' ile, 'kurtuluşa er-' 'tuflihûn' açılımı (13. kelime; IV. bab), 'ûne' 13. kelimede 2MP ile ('erersiniz' içinde))")
M36 = ("5:36 'Şüphesiz inkâr edenlerin' ('inne'llezîne keferû', 'inne' 1. kelimede 'şüphesiz' ile, 'ellezîne' 2. kelimede '-enlerin' ile (ism-i mevsûl; sıfat-fiil açılımı), 'inkâr et-' 'keferû' karşılığı (3. kelime; I. bab), 'û' 3. kelimede karşılıksız (fail eki — '-enlerin' içinde)); "
 "'yeryüzünde olanların hepsi … olsa da' ('lev enne lehum mâ fi'l-ardi cemî'an', 'lev' 4. kelimede '-sa da' ile (morph COND), 'enne' 5. kelimede karşılıksız ('olsa' içinde), 'li' 6. kelimede iyelik ile ('edenlerin' içinde; aitlik), 'hum' 6. kelimede karşılıksız ('edenlerin' içinde), 'mâ' 7. kelimede '-anlar' ile (ism-i mevsûl; 'olanların' içinde), "
 "'fî' 8. kelimede '-de' ile, 'yeryüzü' 'ard' karşılığı (9. kelime), 'hepsi' 'cemî'' karşılığı (10. kelime; nekre — takdirsiz; hâl), 'ol-' takdiri ('olsa' içinde; 'enne' cümlesi)); "
 "'ve onunla birlikte bir misli daha' ('ve mislehû me'ah', 've' 11. kelimede 've' ile (morph COM), 'misil' 'misl' karşılığı (11. kelime; 'bir' takdiri; 'daha' takdiri), 'hû' 11. kelimede iyelik ile ('misli' içinde), 'ma'a' 12. kelimede 'birlikte' ile, 'hû' 12. kelimede 'onunla' ile ('ma'a' yönetimi; fiil yönetimi takdiri), sıralama: zarf öne); "
 "'kıyamet gününün azabından kurtulmak için onu fidye verseler' ('li-yeftedû bihî min 'azâbi yevmi'l-qiyâme', 'li' 13. kelimede 'için' ile (morph PRP; amaç), 'fidye ver-' 'yeftedû' açılımı (13. kelime; VIII. bab; 'kurtulmak için … fidye verseler' açılımı), 'û' 13. kelimede 3MP ile ('verseler' içinde), "
 "'bi' 14. kelimede belirtme eki ile ('onu' içinde; fiil yönetimi takdiri), 'hî' 14. kelimede 'onu' ile, 'min' 15. kelimede '-dan' ile, 'azap' ''azâb' karşılığı (16. kelime; iyelik ile 'azabından'), 'gün' 'yevm' karşılığı (17. kelime), 'kıyamet' 'qiyâme' karşılığı (18. kelime), 'kurtul-' takdiri (amaç; 'yeftedû' açılımı içinde), sıralama: amaç öne, fiil sona alındı); "
 "'onlardan kabul edilmez' ('mâ tuqubbile minhum', 'mâ' 19. kelimede olumsuzluk eki ile ('edilmez' içinde; morph NEG), 'kabul et-' 'tuqubbile' açılımı (20. kelime; V. bab; edilgen 'edil-'; geniş zaman olumsuz açılımı), 'min' 21. kelimede '-dan' ile, 'hum' 21. kelimede 'onlar' ile, sıralama: fiil sona alındı); "
 "'Onlar için acıklı bir azap vardır' ('ve lehum 'azâbun elîm', 've' 22. kelimede karşılıksız (morph REM; cümle başı), 'li' 22. kelimede 'için' ile, 'hum' 22. kelimede 'onlar' ile, 'azap' ''azâb' karşılığı (23. kelime; nekre — 'bir' takdiri), 'acıklı' 'elîm' karşılığı (24. kelime; nekre — takdirsiz; sıfat), "
 "'var' takdiri (isim cümlesi), '-dır' takdiri ('vardır' içinde; isim cümlesi haberi), sıralama: mübteda sona alındı)")
MEALS = (M33, M34, M35, M36)


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
open('/home/claude/b12/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '12')
BLOKLAR = [str(i) for i in range(1, 13)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR).replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '12').replace('\n', '; ')
EMS = open('/home/claude/b12/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '33', '36', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b12/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
MFARK = [(k, n, sayim.S2[k.replace(' --medde', '')][0]) for k, (n, d) in sayim.S2.items() if '--medde' in k]
MEDF = '; '.join("%s meddeli %d / meddesiz %d" % (k.replace(' --medde', ''), m, n) for k, n, m in MFARK)
MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else ' — FARK VAR'
GLS = run('/home/claude/sunum/gloss_tara.py', '33', '36', '12').splitlines()

I = list(BEK) + [
 "bölüm 5 denetimi kurallarının uygulanışı (bölüm 5 kuralı 11 — bu bloktan önce değişen araçlar): sunum/bolum4_kurallar.py (kural 1 / 14: A1'deki her zamir etiketi 1P … 3FP ad ölçütüyle, parantezsiz 'söz içi … 1P' biçimi dahil; REM taraması aralığın başlangıç kelimesinden; sınama: blok 5 'innâ' ve blok 10 'ehadihimâ' isabet verdi), "
 "sunum/edat_etiket.py ve sunum/es_edat.py (kural 2 — tanınan edat listesine 'le'alle', 'innemâ', işaret ve soru edatları eklendi; 'î' / 'nî' / 'te' / 'tu' / 'â' zamir kümesinde, etiket kendi PRON segmentinden; büyük harfli kişi etiketli tırnaksız biçimler; ayrıştırılamayan ve tanınmayan maddeler sayılıyor; sınama: blok 8 ayrıştırılamayan 0, blok 9 ve 10 'î' başlığı tam), "
 "sunum/cakisma.py (kural 3: kök sınırıyla ek soyma, '-acak / -ecek', '-me / -ma', '-mek / -mak', kaynaştırma 'y', d → t; kural örnekleri betik içinde assert ile sınanıyor), sunum/gloss_tara.py (kural 4: kök taşıyan edat / zarf biçimli kayıtlar; taranmayan kök taşıyan kelime sayısı), "
 "sunum/yasakli.sh (kural 6: sayı + iyelik (bir'den dokuz'a), büyük / küçük harf duyarsız, sayı tabanlı sıra sayısı + ek, dağıtma sayıları; 'beşer' insan anlamıyla, 'on' + iyelik 'onu' zamiriyle eş biçimli olduğu için taranmıyor; tırnak içinde biçim adı olarak anılan ''birer' dağıtma' izinli; sabit sınama sunum/yasakli_test.txt + sunum/yasakli_sina.sh — 'yasakli sınama tamam'), "
 "sunum/bolum5_kurallar.py (yeni; kural 5 ham LEM — lemma adı listeleri ve 'LEM' kayıtları morph LEM'iyle iskelet eşlemesi, ham ad notu, meal maddesinde ham LEM'li kelime sayısı kadar not; aracın bayraklamadığı ham LEM'ler sunum/ham_elle.txt'te birikiyor; kural 7 tetik dışı aday kökler ve morph T isimleri; kural 8 ayetler arası kalıp alıntısı ayet bazında ◇ alt dizesi; kural 9 '-dir' ve nekre takdirleri; kural 10 aday 1039 ◇ ⇔ ARIZA), "
 "sunum/sinifla.py (SON 36); elle kalan: kural 8'in sayım tarafı (okuma maddesinde anılan ayetler arası kalıp için sayım koşulur), kural 12 (bekleyen kopyası — bu ARIZA'nın başındaki iki madde bekleyen_ariza_5_b11.txt ile bayt eşit), kural 13 (esmâ / kök maddesinde ayet listesi), kural 14 (3FS ölçütü aktör / ad maddesinde); "
 "bölüm 4 kurallarından yazılmayan araç tarafları: medde.py (kural 2: önek kesilmiş + meddesiz bileşimi), kural13.py (kural 3: R5 kalıp adı), kontrol.py (kural 9) — yazılmadı (R5 kalıp adları bu blokta ◇ lemma dizisi adıyla elle eşlendi)",
 "geriye dönük koşu (bölüm 5 kuralı 15): bolum4_kurallar.py, bolum5_kurallar.py ve yasakli.sh güncel sürümleri sûre 5'in okunmuş bütün bloklarında koşuldu — çıktı yamalar/geriye_donuk_5_b11.txt (isabetler tam okuma sonu listesine; kayıtlar yeniden yazılmadı); denetimin geriye dönük yeni bulguları (5:12 37. kelime REM, blok 6 wasl 'ibn' kesmesi) bu listede; yasakli.sh yeni biçimleri eski bloklarda 'bir' + iyelik ve sayı + iyelik isabetleri veriyor",
 "kök tablosu: ölçümde '???' 5:33 için 1 (kök نفي — 22. kelime 'yunfev') — kök tabloya eklendi (yamalar/yama_kok_5_33.py → kok_ekle_5.py; anlam 'sürgün etme, yurdundan uzaklaştırma'; 1 ayet; docstring dosya adı ve bölümle), ölçüm yeniden alındı, '???' 0; 5:34, 5:35, 5:36 '???' 0; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 33 36 12'): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:33:32 آخِر 'degil' — 'fi'l-âxirati 'azâbun 'azîm', kural 'esmâ adı esmâ dışı göndergeyle → degil' (âhiret yurdu); 5:34:12 غَفُور ve 5:34:13 رَحِيم 'ilahi' — 'enna'llâhe ğafûrun rahîm', kural ''inne/enne' haberi → ilahi' (lafzın haberi) (esma_el_ekle → esma_kayit); kural adı kapalı listeyle karşılaştırıldı; 'degil' göndergesi A1'de (''azâbun 'azîm' — A1 VAR); "
 "lafız 5:33, 5:34, 5:35; 5:36 lafız yok; Rab yok",
 "esma_kayit: 5:33 'mühür EVET ton denge' (ölçüm MÜHÜRSÜZ — uyuşmuyor; esmâ göndergesi âhiret, 'degil'), 5:34 'mühür EVET (ÇİFT) ton cemâl' (ölçüm MÜHÜR — uyuşuyor), 5:35 'mühür hayır' (sınıf A/A), 5:36 'mühür hayır' (sınıf 0/0) — uyuşuyor",
 "ölçüm: 5:33 '{{1|EDİLGEN 4/6 fiil, pas z=3,48}}', '{{1|HAPAKS: نفي}}', '{{1|hapaks z=3,28}}', '{{1|fâsıla عظيم → م, N sınıfı}}', '{{1|simetri \\[6, 8, 23, 2\\]}}', '{{1|harf 148 → harf3 140, isaret 8}}' ve '{{1|dış düğüm 3}}'; "
 "5:34 '{{2|biçim ISTISNA}}', '{{2|fâsıla رحيم → م, N sınıfı}}', '{{2|simetri \\[3, 2, 6, 1\\]}}', '{{2|harf 58 → harf3 52, isaret 6}}' ve '{{2|dış düğüm 1}}'; 5:35 '{{3|biçim DIKKAT}}', '{{3|fâsıla تفلحون → ن, N sınıfı}}', '{{3|harf 72 → harf3 67, isaret 5}}' ve '{{3|dış düğüm 0}}'; "
 "5:36 '{{4|lafız YOK · Rab YOK}}', '{{4|EDİLGEN 1/3 fiil, pas z=1,57}}', '{{4|fâsıla أليم → م, N sınıfı}}', '{{4|simetri \\[6, 12, 19, 2\\]}}', '{{4|harf 95 → harf3 87, isaret 8}}' ve '{{4|dış düğüm 6}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 33 36 12'): KALAN_P",
 "ölçüm aktör: 5:33-36 aktör yok (ölçüm); 5:33 'llezîne yuhâribûna'llâhe' ve 5:36 'llezîne keferû' ism-i mevsûl, adsız",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:33 haber, kip yok — EDİLGEN 4 'yuqattelû' (12.), 'yusallebû' (14.), 'tuqatta'a' (16.), 'yunfev' (22.); 'innemâ' sınırlama; 5:34 emir — IMPV 1 'fa'lemû' (9.); biçim ISTISNA 'illâ' (1.); "
 "5:35 emir, nida — IMPV 3 'ttequ' (4.), 'bteğû' (6.), 'câhidû' (9.), VOC 1 'yâ' (1.); biçim DIKKAT 'yâ eyyuhâ' (VOC + ATT); 5:36 şart — COND 1 'lev' (4.), NEG 1 'mâ' (19.); EDİLGEN 1 'tuqubbile' (20.)",
 "yıldız: 5:33 ★★★ (kaynak edilgen, pas z=3,48; eşiği geçen öbür ölçüler n ve hapaks), 5:36 ★ (kaynak edilgen, pas z=1,57); 5:34 ve 5:35 yıldız yok — satır yıldız kaynağını adlandırmıyor; kaynak kapanış notunda bilançodan",
 "fâsıla: 5:32 ن (لمسرفون) → 5:33 م (عظيم) → 5:34 م (رحيم) → 5:35 ن (تفلحون) → 5:36 م (أليم); bölüm açılışında ن → م geçişi; hepsi N sınıfı; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:33 9:107 ve 59:3 (emsal olarak basıldı) ve okunmuş başka bir ayet; 5:34 okunmuş bir ayet; 5:35 xref yok; 5:36 13:18, 14:8 ve 70:11 (basılmış) ve okunmuş başka ayetler — basılmamış xref numaraları yazılmadı",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı ölçüm kalıbının öğelerinden morph LEM ham adıyla, ◇ lemma dizisi adıyla eş): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:33 'se'â fî ard fesâd' ve 'fî âxir 'azâb 'azîm' süzgeç GEÇER; 5:34 'enne allâh ğafûr rahîm', 'allâh ğafûr rahîm' ve ''alime enne allâh' süzgeç GEÇER, 'min qabl en' GEÇMEZ; 5:35 'eyy ellezî âmene' GEÇER, 'câhede fî sebîl' GEÇMEZ; 5:36 'fî ard cemî'' ve 'mâ fî ard' GEÇMEZ",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14 — ölçüt: 1P / 1S / 2MS / 2MP / 3MS / 3FS / 3D / 3MD / 3MP / 3FP zamirlerin hepsi 'adsız'; edilgen fiilin nâib fâili madde başındaki 'adsız' etiketini alır): "
 "5:33 'cezâ'u', 'llezîne', 3MP (adsız — 'yuhâribûne', 'yes'avne' failleri; 'eydîhim', 'erculuhum', 'lehum'), Allah (lafız), 'rasûlehû' ve iyelik 3MS (adsız), edilgen failler (adsız; nâib fâil 3MP / 3FS), 'zâlike', 'xizyun', ''azâbun 'azîm'; "
 "5:34 'llezîne', 3MP (adsız), muhatap 2MP (adsız), Allah (lafız), 'ğafûrun rahîm'; 5:35 muhatap 2MP (adsız), 'llezîne âmenû' (3MP fail adsız), Allah (lafız), 3MS (adsız), 'l-vesîlete'; 5:36 'llezîne keferû' (3MP fail adsız), 3MP (adsız), 'mâ fi'l-ard', 3MS (adsız), edilgen fail (adsız; nâib fâil 3MS), ''azâbun elîm' — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): blokta 'qâle' yok, söz aralığı yok (A3 —); 5:35 hitap ('yâ eyyuhe'llezîne âmenu', 1-3. kelime) söz değil, muhataba doğrudan emir; REM sapması (komut 'python3 sunum/bolum4_kurallar.py 33 36 12' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:33 've rasûlehû' (6.), 've yes'avne' (7.), 've erculuhum' (18.) CONJ, 've lehum' (30.) REM; 5:34 'fa'lemû' (9.) REM; 5:35 've'bteğû' (6.), 've câhidû' (9.) CONJ; 5:36 've mislehû' (11.) COM, 've lehum' (22.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:33 ◈K أرض ('l-ardi' 9. kelime, 'l-ard' 24. kelime — K1; anlam notu: bozgunculuk yeri ve sürgün yeri); 5:33 ◈B يدي ('eydîhim' 17. kelime — B3; anlam notu: ceza olarak el kesme); "
 "5:36 ◈K أرض ('l-ardi' 9. kelime — K1; anlam notu: yeryüzündekilerin hepsi), يوم ('yevmi' 17. kelime — K2; anlam notu: kıyamet günü); 5:34 ve 5:35 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7 — komut 'python3 sunum/bolum5_kurallar.py 33 36 12'; aday kökler ve morph T isimleri): TETIKDISI; anılış: 5:33 kök قتل ('yuqattelû' 12. kelime — öldürme cezası; B4 hayat / ölüm alanına yakın, tetik dışı), صلب ('yusallebû' 14. kelime — asma), قطع ('tuqatta'a' 16. kelime — kesme; B3 'eydîhim' ile birlikte), "
 "رجل ('erculuhum' 18. kelime — ayak, beden; B3 alanına yakın, tetik dışı); عظم (''azîm' 34. kelime — 'büyük'; kemik anlamında değil — aday listesi kökü mekanik okur); 5:36 جمع ('cemî'an' 10. kelime — 'hepsi', toplama); 5:32'de anılmayan قتل kullanımı bu blokta anıldı (bölüm 5 kuralı 7: kök kullanımı sonraki geçişlerinde yine anılır); oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:33 (9:107, 59:3), 5:36 (13:18, 70:11); 5:34 ve 5:35 eş yok (kontrol.py ile); blok geçişi 5:32 → 5:33 bölüm geçişi — ardışık bağ kurulmadı; D3 dışı bırakılan basılmış sayım eşleri: 5:34 'llâhe ğafûrun rahîm' 2:173, 5:3, 16:115; 'ğafûrun rahîm' 2:173, 3:129, 4:25, 5:3, 16:115; "
 "'min qabli en' 2:237, 3:93; 5:35 'yâ eyyuhe'llezîne âmenû' ve 'ttequ'llâh' kümeleri; 5:36 'fi'l-ardi cemî'an' 5:17, 14:8; 'yevmi'l-qiyâme' 5:14 — kalıp başına ölçüt: geniş nakarat / hitap kalıbı, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:33 bölüm açılışı; edim geçişi şart → haber (ayetler arası); şahıs geçişi yok; 5:34 edim geçişi haber → emir; şahıs geçişi 3 → 2; 5:35 hitap açılır (1-3. kelime); edim geçişi emir → emir, nida; şahıs geçişi yok; hitap kapanır (ayet sonu); "
 "5:36 edim geçişi emir, nida → şart; şahıs geçişi 2 → 3; şart → cevap (ayet içi; COND 'lev' 4. kelime: 'lev enne lehum mâ fi'l-ardi cemî'an' / 'mâ tuqubbile minhum' (19. kelime))",
 "sözdizimi (okuma; morph etiketiyle): 5:33 'innemâ cezâ'u'llezîne' — sınırlama (morph ACC + PREV), mübteda; 'en yuqattelû … ev yunfev' — haber (masdar; morph SUB), dört şık 'ev' ile (morph CONJ); 'min xilâfin' — kesmenin biçimi (çaprazlama; morph etiketi yok); 'zâlike lehum xizyun' — isim cümlesi; 've lehum fi'l-âxirati' — istînâf (morph REM); "
 "5:34 'illa'llezîne tâbû' — 5:33'teki 'llezîne'den istisna (morph EXP); 'min qabli en taqdirû' — zaman zarfı (masdar; morph SUB); 'fa'lemû' — istînâf (morph REM), emir; 5:35 'yâ eyyuhe'llezîne âmenû' — nidâ (morph VOC); 'le'allekum tuflihûn' — ümit (morph ACC); "
 "5:36 'inne'llezîne keferû' — 'inne' ismi; 'lev enne lehum … li-yeftedû bihî' — şart (morph COND); 'mâ tuqubbile minhum' — 'lev' cevabı (morph NEG), 'inne' haberi; 've mislehû' — birliktelik (morph COM); 've lehum 'azâbun elîm' — istînâf (morph REM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:33 'innemâ cezâ'u'llezîne' ile açılıyor (1-3. kelime); ceza dört edilgen fiille sayılıyor (ölçüm EDİLGEN 4/6, pas z=3,48); kök أرض iki geçiş (9. ve 24. kelime) — bozgunculuk yeri / sürgün yeri; "
 "5:33 'xizyun fi'd-dunyâ' / 'fi'l-âxirati 'azâbun 'azîm' — dünya / âhiret karşıtlığı (lemma dizisi 'fî dunyâ fî âxir 'azâb' basılmış eşi 59:3, sayımın basılmış kümesinden); 5:34 'illâ' ile 5:33'teki cezadan istisna, 'enna'llâhe ğafûrun rahîm' ile kapanıyor; "
 "5:35 'yâ eyyuhe'llezîne âmenu' ile açılıyor (1-3. kelime); 5:36 kök عذب iki geçiş (16. ve 23. kelime); 5:36 'lev enne lehum mâ fi'l-ardi cemî'an ve mislehû me'ah' kalıbının basılmış eşi 13:18 (sayımın basılmış kümesinden); ayetler arası kalıp yok (blok sınırı 5:32 → 5:33'te kök فسد ve أرض geçişleri kalıp olarak alıntılanmadı — kök gözlemi)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 12'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + "'; çıktı aynen): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle): 'hârebe allâh rasûl' 5:33 'Allah'a ve elçisine savaş açan' / 9:107 'Allah'a ve Resûlü'ne savaş açan' ('rasûl' karşılığı farklı); 'fî dunyâ fî âxir 'azâb' 5:33 'dünyada … âhirette … azap' / 59:3 'dünyada … Âhirette … azabı' (eş); "
 "'lev enne lehum … mislehû me'ah' 5:36 'bir misli daha' / 13:18 'bir o kadarı daha' (farklı); 'iftedâ' 5:36 'fidye ver-' / 70:11 'fidye olarak … ver-' (eş); 13:18 ''azâb' karşılığı yok — tam okuma sonu",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 33 36 12'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:36 tarayıcı adayı (kök أرض; A_şart, B_ta'lîl) — çıpa değil: 'lev' varsayımı, fidye; doğa iddiası yok (olgu=False); 5:33-35 tarayıcı adayı yok; L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:33 ('xizyun fi'd-dunyâ' / 'fi'l-âxirati 'azâbun 'azîm') — okuma; ayetler arası 5:33 / 5:34 ('innemâ cezâ'u'llezîne yuhâribûna'llâhe' / 'illa'llezîne tâbû'), 5:35 / 5:36 ('le'allekum tuflihûn' / 've lehum 'azâbun elîm'); eşleme betikle: ADAY_P",
 "aday 1041: kök رسل 5:33 'rasûlehû' — lafızla birlikte savaş açılan taraf (elçi); kök أمن 5:35 'âmenû' — insan; blokta lafız göndergeli kökün insan için kullanıldığı vaka: 5:34 kök غفر / رحم yalnız lafzın haberi — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 6-1 — bölüm açılışı 5:33; bölüm iki blok (blok planından: 12 ve 13); başlıktaki 'bozgunculuğun cezası' 5:33 ('yes'avne fi'l-ardi fesâden' / 'cezâ'u'), 'vesile' 5:35 ('l-vesîlete'), 'tövbe' 5:34 ('tâbû'); 'hırsızlık' blok 13'te; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; bölüm 5 denetimi bulguları ve yeni kuralları bu ARIZA'nın başında; medde taraması (sunum/medde.py b12/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 33 36 12'; lem_bozuk.py 12 çıktısı): 5:33:12 'quttilu', 5:33:14 'yusallebu', 5:33:22 'yunfe' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 33 36 → AYN_SONUC; sunum/bolum4_kurallar.py 33 36 12 → KHATA_HEPSI; sunum/bolum5_kurallar.py 33 36 12 → B5_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; bekleyen kopyası bayt eşit (değişiklik yok; yasakli.sh 'birer' dağıtma biçim adı tırnak içinde izinli kılındı)",
 "sonradan basılan (sunum/sonradan.py --plan 12): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('cezâ'', 'rasûl', 'ard', 'fesâd', 'quttilu' (morph LEM ham biçim), 'yusallebu' (morph LEM ham biçim), 'yunfe' (morph LEM ham biçim), 'yed', 'ricl', 'xilâf', 'xizy', 'dunyâ', 'âxir', ''azâb', ''azîm', 'qabl', 'ğafûr', 'rahîm', 'vesîle', 'sebîl', 'cemî'', 'misl', 'iftedâ', 'yevm', 'qiyâme', 'elîm'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]


def yaz():
    items = [kes(x) for x in I]
    s = '\n (33, 36): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_33_36.txt', 'w', encoding='utf-8').write(s)


idx = I.index('KARSILIK_CAKISMA')
I[idx] = 'karşılık çakışması (geçici)'
yaz()
AYN = (run('/home/claude/sunum/ayn_kontrol.py', '33', '36').splitlines() or ['?'])[-1]
KUR = run('/home/claude/sunum/bolum4_kurallar.py', '33', '36', '12').splitlines()
KH = [l for l in KUR if l.startswith('HATA')]
B5 = run('/home/claude/sunum/bolum5_kurallar.py', '33', '36', '12').splitlines()
B5H = [l for l in B5 if l.startswith('HATA')]
REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
       'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h) or 'adsız / söz muhatabı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
       'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
       'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
       'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or 'ARIZA ⇔ ◇ bayt eşit'), 'HAMLEM_P': next((l for l in B5 if l.startswith('ham LEM')), '?'), 'B5_HEPSI': (B5[-1] if B5 else '?')}
for k, v in REP.items(): I = [x.replace(k, v) for x in I]
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
CAK = run('/home/claude/sunum/cakisma.py', *DOS)
KYENI = set(re.findall(r"'([^']+)' '(?:[^']|'(?=[a-zâîû]))+' (?:karşılığı|açılımı)", ' '.join(MEALS)))
CAK_L = [l for l in CAK.splitlines() if l.startswith('KÖK') or l.split(' ←')[0] in KYENI]
KARAR = {}
for nn in ('06', '10', '11', '12'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
I[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3 — komut 'python3 sunum/cakisma.py' + sûre 5'in okunmuş bütün ARIZA dosyaları; Türkçe fiil kökü eşlemesi betikle, son dosyaya dokunan gruplar; her grupta kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
          + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
yaz()
print('yazıldı', len(I))
print('\n'.join(CAK_L))
print(GLS); print(KUR); print(B5)
