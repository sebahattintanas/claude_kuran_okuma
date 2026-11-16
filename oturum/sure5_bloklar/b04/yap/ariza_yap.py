# blok 4 (5:7-11) ARIZA oluşturucu — bölüm 2-2 (bölüm kapanışı)
import sys, os, ast, subprocess, re
os.environ['OLC'] = '/home/claude/b04/olcum.txt'
os.environ['SAY2'] = '/home/claude/b04/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

VF_YAZI = {7: {1: "'ve'zkurû'", 5: "'ve mîsâqahu'", 12: "'ve eta'nâ'", 13: "'ve'ttequ'"}, 8: {9: "'ve lâ'", 20: "'ve'ttequ'"},
           9: {5: "'ve 'amilu'", 9: "'ve ecrun'"}, 10: {1: "'ve'llezîne'", 3: "'ve kezzebû'"}, 11: {15: "'fe-keffe'", 18: "'ve'ttequ'", 20: "'ve 'ale'llâhi'", 22: "'fe'l-yetevekkel'"}}
BOL = "'Kitap ehlinin yemeği ve kadınları; abdest ve teyemmüm; nimeti ve misakı anma'"


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
 ("5:7", "'itteqâ allâh inne allâh'", 4, 'say 5:7 13-16 --on', "önek kesilmiş 've'ttequ'llâhe inna'llâh' (13-16. kelime)", None),
 ("5:7", "'zekera ni'me allâh 'aleykum'", 3, 'say 5:7 1-4 --on', "önek kesilmiş 've'zkurû ni'meta'llâhi 'aleykum' (1-4. kelime)", ('dizi 5 7 1 4', "zekera ni'me allâh 'alâ", '1-4', "biçim farkı — 'ni'me' yazımı ة / ت ve 've' öneki")),
 ("5:7", "'itteqâ allâh inne'", 6, 'say 5:7 13-15 --on', "önek kesilmiş 've'ttequ'llâhe inne' (13-15. kelime)", ('dizi 5 7 13 15', "itteqâ allâh inne", '13-15', None)),
 ("5:8", "'itteqâ allâh inne allâh'", 4, 'say 5:8 20-23 --on', "önek kesilmiş 've'ttequ'llâhe inna'llâh' (20-23. kelime)", None),
 ("5:8", "'lâ yecrime şene'ân qavm'", 2, 'say 5:8 9-12 --on', "önek kesilmiş 've lâ yecrimennekum şene'ânu qavm' (9-12. kelime)", None),
 ("5:8", "'eyy ellezî âmene'", 16, 'say 5:8 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
 ("5:8", "'itteqâ allâh inne'", 6, 'say 5:8 20-22 --on', "önek kesilmiş 've'ttequ'llâhe inne' (20-22. kelime)", ('dizi 5 8 20 22', "itteqâ allâh inne", '20-22', None)),
 ("5:9", "'ellezî âmene 'amile sâliha'", 2, 'say 5:9 3-6', "harekesiz 'llezîne âmenû ve 'amilu's-sâlihât' (3-6. kelime)", None),
 ("5:11", "'zekera ni'me allâh 'aleykum iz'", 2, 'say 5:11 4-8', "harekesiz 'zkurû ni'meta'llâhi 'aleykum iz' (4-8. kelime)", ('dizi 5 11 4 8', "zekera ni'me allâh 'alâ iz", '4-8', "biçim farkı — 'ni'me' yazımı ة / ت")),
 ("5:11", "'zekera ni'me allâh 'aleykum'", 3, 'say 5:11 4-7', "harekesiz 'zkurû ni'meta'llâhi 'aleykum' (4-7. kelime)", ('dizi 5 11 4 7', "zekera ni'me allâh 'alâ", '4-7', "biçim farkı — 'ni'me' yazımı ة / ت")),
 ("5:11", "'eyy ellezî âmene'", 16, 'say 5:11 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
 ("5:11", "'ve 'alâ allâh tevekkel'", 2, 'say 5:11 20-22 --on', "önek kesilmiş 've 'ale'llâhi fe'l-yetevekkel' (20-22. kelime)", ('dizi 5 11 20 22', "'alâ allâh tevekkel", '20-22', "önek farkı — 'fe' ve 'li' önekleri harekesiz kalıbı daraltıyor")),
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
            h += (" — tutmuyor; eşit aralıkla lemma dizisi '%s' (%s. kelime) sûre içi %d (%s) — olası neden: nakarat3 'ان' kök anahtarı 'inne' / 'enne' / 'en' biçimlerini birleştiriyor"
                  % (dad, dar, ds, taban(dk, ay)) + ('; fazla sûre içi eş okunmamış (fark test edilmedi)' if sd(key)['henuz_si'] else ''))
    r5.append(h)
r5.append("5:10 nakarat3 've'llezîne kefere kezzebe âye ulâ'ike ashâb cahîm' 2 (tür tam) / önek kesilmiş 've'llezîne keferû ve kezzebû bi-âyâtinâ ulâ'ike ashâbu'l-cahîm' (1-7. kelime) %d ayet — tutmuyor; 'tür tam' alanı korpus geneli sayım veriyor, önek kesilmiş sayımdaki fazla eş 57:19 (okunmuş, basılmış) — nakarat3'ün onu dışarıda bırakma nedeni test edilmedi (araç tanımı farkı)" % sayim.S2['say 5:10 1-7 --on'][0])

K1 = {'say 5:7 1-3 --on': "önek kesilmiş 've'zkurû ni'meta'llâh'", 'say 5:7 1-4 --on': "önek kesilmiş 've'zkurû ni'meta'llâhi 'aleykum'", 'say 5:7 5-7 --on': "önek kesilmiş 've mîsâqahu'llezî vâsaqakum'",
      'lem 5:7:7': "lemma 'vâsaqa'", 'say 5:7 9-12': "harekesiz 'iz qultum semi'nâ ve eta'nâ'", 'say 5:8 4-8': "harekesiz 'kûnû qavvâmîne li'llâhi şuhedâ'e bi'l-qıst'", 'dizi 5 8 4 8': "lemma dizisi 'kâne qavvâm allâh şehîd qıst'",
      'say 5:8 13-15': "harekesiz ''alâ ellâ ta'dilû'", 'say 5:8 16-19': "harekesiz 'dilû huve aqrabu li't-taqvâ'", 'say 5:11 1-7': "harekesiz 'yâ eyyuhe'llezîne âmenu'zkurû ni'meta'llâhi 'aleykum'",
      'say 5:11 4-8': "harekesiz 'zkurû ni'meta'llâhi 'aleykum iz'", 'say 5:11 8-14': "harekesiz 'iz hemme qavmun en yebsutû ileykum eydiyehum'", 'say 5:11 15-17 --on': "önek kesilmiş 'fe-keffe eydiyehum 'ankum'"}
assert all(sayim.S2[k][0] == 1 for k in K1), [k for k in K1 if sayim.S2[k][0] != 1]

M7 = ("5:7 'Allah'ın üzerinizdeki nimetini … anın' ('ve'zkurû ni'meta'llâhi 'aleykum', 've' 1. kelimede karşılıksız (morph CONJ; ayet başı), 'an-' 'zkurû' karşılığı (1. kelime; emir), 'û' 1. kelimede '-ın' ile, 'nimet' 'ni'me' karşılığı (2. kelime; '-i' iyelik takdiri), "
 "lafız 3. kelimede 'Allah'ın' ile ('-ın' takdir — izafet), ''alâ' 4. kelimede 'üzerinde' ile ('-ki' takdir), 'kum' 4. kelimede '-iniz' iyelik ile, sıralama: fiil sona alındı); "
 "'ve … sizi kendisiyle bağladığı ahdini' ('ve mîsâqahu'llezî vâsaqakum bih', 've' 5. kelimede 've' ile, 'ahit' 'mîsâq' karşılığı (5. kelime), 'hu' 5. kelimede '-i' iyelik ile, 'ellezî' 6. kelimede '-dığı' ile, 'bağla-' 'vâsaqa' açılımı (7. kelime; III. bab), "
 "'kum' 7. kelimede 'sizi' ile, 'bi' 8. kelimede '-le' ile, 'hî' 8. kelimede 'kendisi' ile ('kendi' açılım takdiri)); "
 "''İşittik ve itaat ettik' dediğinizde' ('iz qultum semi'nâ ve eta'nâ', 'iz' 9. kelimede '-diğinizde' ile (zaman), 'de-' 'qultum' karşılığı (10. kelime), 'tum' 10. kelimede '-iniz' ile, 'işit-' 'semi'nâ' karşılığı (11. kelime), "
 "'nâ' 11. kelimede '-tik' ile, 've' 12. kelimede 've' ile (morph CONJ), 'itaat et-' 'eta'nâ' açılımı (12. kelime; IV. bab; 'et-' açılım takdiri), 'nâ' 12. kelimede '-tik' ile, sıralama: söz öne alındı); "
 "'Allah'tan sakının' ('ve'ttequ'llâh', 've' 13. kelimede karşılıksız (nokta; morph CONJ), 'sakın-' 'ttequ' karşılığı (13. kelime), 'û' 13. kelimede '-ın' ile, lafız 14. kelimede 'Allah'tan' ile ('-tan' fiil yönetimi takdiri)); "
 "'Şüphesiz Allah göğüslerin özünü bilendir' ('inna'llâhe 'alîmun bi-zâti's-sudûr', 'inne' 15. kelimede 'şüphesiz' ile, lafız 16. kelimede 'Allah' ile, 'bilen' ''alîm' karşılığı (17. kelime), '-dir' takdir (17. kelime), "
 "'bi' 18. kelimede karşılıksız (mef'ûl '-ü' ile), 'öz' 'zû' açılımı (18. kelime; 'zât' — 'öz' karşılığı), 'göğüs' 'sadr' karşılığı (19. kelime; çoğul '-ler'; '-in' takdir — izafet), sıralama: haber sona alındı)")
M8 = ("5:8 'Ey iman edenler' ('yâ eyyuhe'llezîne âmenû', 'yâ' 1. kelimede 'ey' ile, 'eyy' ve 'hâ' 1. kelimede karşılıksız, 'ellezîne' 2. kelimede '-enler' ile, 'iman et-' 'âmenû' açılımı (3. kelime), 'û' 3. kelimede karşılıksız (fail eki — '-enler' içinde)); "
 "'Allah için adaleti ayakta tutanlar, adaletle tanıklık edenler olun' ('kûnû qavvâmîne li'llâhi şuhedâ'e bi'l-qıst', 'ol-' 'kûnû' karşılığı (4. kelime; emir), 'û' 4. kelimede '-un' ile, 'adaleti ayakta tutan' 'qavvâm' açılımı (5. kelime; çoğul '-lar'; 'adaleti' ve 'ayakta' açılım takdiri), "
 "'li' 6. kelimede 'için' ile, lafız 6. kelimede 'Allah' ile, 'tanıklık eden' 'şehîd' açılımı (7. kelime; çoğul '-ler'), 'bi' 8. kelimede '-le' ile, 'adalet' 'qıst' karşılığı (8. kelime), sıralama: 'li'llâhi' öne, fiil sona alındı); "
 "'Bir kavme duyduğunuz kin sizi adaletsizliğe sürüklemesin' ('ve lâ yecrimennekum şene'ânu qavmin 'alâ ellâ ta'dilu', 've' 9. kelimede karşılıksız (nokta; morph CONJ), 'lâ' 9. kelimede '-me-' ile (yasak, 3MS — '-sin'), 'sürükle-' 'yecrimennekum' karşılığı (10. kelime; EMPH 'nûn' karşılıksız), "
 "'kum' 10. kelimede 'sizi' ile, 'kin' 'şene'ân' karşılığı (11. kelime), 'kavim' 'qavm' karşılığı (12. kelime; nekre — 'bir' takdiri; '-e' fiil yönetimi takdiri), 'duyduğunuz' takdir (11-12. kelime; izafet açılımı), "
 "''alâ' 13. kelimede '-e' ile ('-e' fiil yönetimi takdiri), 'en' 14. kelimede '-liğe' ile (masdar; '-e' fiil yönetimi takdiri), 'lâ' 14. kelimede '-siz-' ile, 'adalet' 'ta'dilu' açılımı (15. kelime; 'adaletsizlik' — olumsuz masdar), 'û' 15. kelimede karşılıksız (masdar içinde), sıralama: fiil sona alındı); "
 "'Adaletli olun; bu takvâya daha yakındır' ('dilû huve aqrabu li't-taqvâ', 'adaletli ol-' 'dilû' açılımı (16. kelime; emir; 'ol-' açılım takdiri), 'û' 16. kelimede '-un' ile, 'huve' 17. kelimede 'bu' ile, 'daha yakın' 'aqrab' karşılığı (18. kelime; tafdîl), "
 "'-dır' takdir (18. kelime), 'li' 19. kelimede '-a' ile, 'takvâ' 'taqvâ' karşılığı (19. kelime)); "
 "'Allah'tan sakının' ('ve'ttequ'llâh', 've' 20. kelimede karşılıksız (nokta; morph REM), 'sakın-' 'ttequ' karşılığı (20. kelime), 'û' 20. kelimede '-ın' ile, lafız 21. kelimede 'Allah'tan' ile ('-tan' fiil yönetimi takdiri)); "
 "'Şüphesiz Allah yaptıklarınızdan haberdardır' ('inna'llâhe xabîrun bimâ ta'melûn', 'inne' 22. kelimede 'şüphesiz' ile, lafız 23. kelimede 'Allah' ile, 'haberdar' 'xabîr' karşılığı (24. kelime), '-dır' takdir (24. kelime), 'bi' 25. kelimede '-dan' ile, "
 "'mâ' 25. kelimede '-dıklarınız' ile, 'yap-' 'ta'melûn' karşılığı (26. kelime), 'ûne' 26. kelimede karşılıksız ('-dıklarınız' içinde), sıralama: haber sona alındı)")
M9 = ("5:9 'Allah iman edip salih ameller işleyenlere vaat etti' ('ve'ade'llâhu'llezîne âmenû ve 'amilu's-sâlihât', 'vaat et-' 've'ade' açılımı (1. kelime; 'et-' açılım takdiri), lafız 2. kelimede 'Allah' ile, 'ellezîne' 3. kelimede '-enlere' ile ('-e' fiil yönetimi takdiri), "
 "'iman et-' 'âmenû' açılımı (4. kelime; '-ip'), 'û' 4. kelimede karşılıksız (fail eki), 've' 5. kelimede karşılıksız ('-ip' bağlacıyla; morph CONJ), 'işle-' ''amilu' karşılığı (5. kelime), 'û' 5. kelimede karşılıksız (fail eki), "
 "'salih amel' 'sâliha' açılımı (6. kelime; çoğul '-ler'; 'amel' açılım takdiri), sıralama: fiil sona alındı); "
 "'onlar için bağışlanma ve büyük bir ödül vardır' ('lehum mağfiratun ve ecrun 'azîm', 'li' 7. kelimede 'için' ile, 'hum' 7. kelimede 'onlar' ile, 'bağışlanma' 'mağfire' karşılığı (8. kelime; nekre), 've' 9. kelimede 've' ile, 'ödül' 'ecr' karşılığı (9. kelime; nekre — 'bir' takdiri), "
 "'büyük' ''azîm' karşılığı (10. kelime), 'var' takdir (10. kelime; isim cümlesi), '-dır' takdir (10. kelime); söz biçimli içerik, tırnak yok)")
M10 = ("5:10 'İnkâr edip âyetlerimizi yalanlayanlar ise' ('ve'llezîne keferû ve kezzebû bi-âyâtinâ', 've' 1. kelimede 'ise' ile (morph REM; karşıtlık), 'ellezîne' 1. kelimede '-anlar' ile, 'inkâr et-' 'keferû' karşılığı (2. kelime; '-ip'), 'û' 2. kelimede karşılıksız (fail eki), "
 "'ve' 3. kelimede karşılıksız ('-ip' bağlacıyla; morph CONJ), 'yalanla-' 'kezzebû' karşılığı (3. kelime; II. bab), 'û' 3. kelimede karşılıksız (fail eki), 'bi' 4. kelimede karşılıksız (mef'ûl '-i' ile), 'âyet' 'âye' karşılığı (4. kelime; çoğul '-ler'), 'nâ' 4. kelimede '-imiz' iyelik ile); "
 "'işte onlar alevli ateşin halkıdır' ('ulâ'ike ashâbu'l-cahîm', 'işte onlar' 'ulâ'ike' açılımı (5. kelime; 'işte' takdir), 'halk' 'ashâb' karşılığı (6. kelime; '-ı' iyelik takdiri), 'alevli ateş' 'cahîm' karşılığı (7. kelime; '-in' takdir — izafet), '-dır' takdir (7. kelime))")
M11 = ("5:11 'Ey iman edenler' ('yâ eyyuhe'llezîne âmenu', 'yâ' 1. kelimede 'ey' ile, 'eyy' ve 'hâ' 1. kelimede karşılıksız, 'ellezîne' 2. kelimede '-enler' ile, 'iman et-' 'âmenu' açılımı (3. kelime), 'û' 3. kelimede karşılıksız (fail eki — '-enler' içinde)); "
 "'Allah'ın üzerinizdeki nimetini anın' ('zkurû ni'meta'llâhi 'aleykum', 'an-' 'zkurû' karşılığı (4. kelime; emir), 'û' 4. kelimede '-ın' ile, 'nimet' 'ni'me' karşılığı (5. kelime; '-i' iyelik takdiri), lafız 6. kelimede 'Allah'ın' ile ('-ın' takdir), "
 "''alâ' 7. kelimede 'üzerinde' ile ('-ki' takdir), 'kum' 7. kelimede '-iniz' iyelik ile, sıralama: fiil sona alındı); "
 "'hani bir kavim size ellerini uzatmaya yeltenmişti' ('iz hemme qavmun en yebsutû ileykum eydiyehum', 'iz' 8. kelimede 'hani' ile (zaman), 'yeltenmek' 'hemme' karşılığı (9. kelime; '-mişti' — geçmiş anlatı), 'kavim' 'qavm' karşılığı (10. kelime; nekre — 'bir' takdiri), "
 "'en' 11. kelimede '-maya' ile ('-a' fiil yönetimi takdiri), 'uzat-' 'yebsutû' karşılığı (12. kelime), 'û' 12. kelimede karşılıksız (masdar içinde), 'ilâ' 13. kelimede '-e' ile, 'kum' 13. kelimede 'siz' ile, 'el' 'yed' karşılığı (14. kelime; çoğul '-ler'), 'hum' 14. kelimede '-i' iyelik ile ('-lerini'), "
 "sıralama: fiil sona alındı); "
 "'de O onların ellerini sizden çekmişti' ('fe-keffe eydiyehum 'ankum', 'fe' 15. kelimede 'de' ile (morph CONJ), 'O' takdir (15. kelime; fail zamiri — gönderge lafız), 'çek-' 'keffe' karşılığı (15. kelime; '-mişti'), 'el' 'yed' karşılığı (16. kelime), 'hum' 16. kelimede 'onların … -i' ile, "
 "''an' 17. kelimede '-den' ile, 'kum' 17. kelimede 'siz' ile, sıralama: fiil sona alındı); "
 "'Allah'tan sakının' ('ve'ttequ'llâhe', 've' 18. kelimede karşılıksız (nokta; morph CONJ), 'sakın-' 'ttequ' karşılığı (18. kelime), 'û' 18. kelimede '-ın' ile, lafız 19. kelimede 'Allah'tan' ile ('-tan' fiil yönetimi takdiri)); "
 "'İnananlar yalnız Allah'a dayansınlar' ('ve 'ale'llâhi fe'l-yetevekkeli'l-mu'minûn', 've' 20. kelimede karşılıksız (nokta; morph REM), ''alâ' 20. kelimede '-a' ile, lafız 21. kelimede 'Allah'a' ile, 'yalnız' takdir (20-21. kelime; takdim ile hasr okuması), "
 "'fe' 22. kelimede karşılıksız (morph SUP), 'li' 22. kelimede '-sın' ile (emir), 'dayan-' 'yetevekkel' açılımı (22. kelime; V. bab; LEM 'tevekkel' (morph LEM ham biçim)), 'inanan' 'mu'min' karşılığı (23. kelime; çoğul '-lar'), sıralama: fail öne, fiil sona alındı)")
MEALS = (M7, M8, M9, M10, M11)
EOF_MARK = None


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
open('/home/claude/b04/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '4')
ESB = run('/home/claude/sunum/es_edat.py', '3', '4')
ESL = run('/home/claude/sunum/es_lemma.py', '3', '4').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '4').replace('\n', '; ')
EMS = "2:285 24:51 3:119 4:135 2:237 59:18 48:29 49:3 57:19 2:39 33:9 35:3 3:122 64:13"
ONC = run('/home/claude/sunum/onceki_basim.py', '7', '11', EMS)

I = [
 "kök tablosu: ölçümde '???' 5:7, 5:8, 5:9, 5:10 ve 5:11 için ayrı sayıldı — 0; yeni kök yok (okunan ayetlerde tabloda olmayan kök 0); kök صدر karşılığı 'göğüs' 5:7 'zâti's-sudûr' (göğüslerin özü) kullanımını kapsıyor; kök همم karşılığı 'kastetme, niyetlenme' 5:11 'hemme' kullanımını kapsıyor; "
 "kök قسط karşılığı 'kıst, adalet; sapma' 5:8 'bi'l-qıst' kullanımını kapsıyor; kök جحم 'alevli ateş, cahîm' 5:10 kullanımını kapsıyor",
 "esmâ: 5:7:17 عَلِيم 'ilahi' — 'inna'llâhe 'alîmun bi-zâti's-sudûr', kural ''inne/enne' haberi → ilahi' (lafzın haberi); 5:8:7 شَهِيد 'degil' — 'qavvâmîne li'llâhi şuhedâ'e', kural 'çoğul insan göndergeli → degil' (tanıklar); "
 "5:8:24 خَبِير 'ilahi' — 'inna'llâhe xabîrun bimâ ta'melûn', kural ''inne/enne' haberi → ilahi' (lafzın haberi); 5:11:23 مُؤْمِن 'degil' — 'fe'l-yetevekkeli'l-mu'minûn', kural 'çoğul insan göndergeli → degil' (inananlar) "
 "(esma_el_ekle → esma_kayit; e_el=? 0); kural adları kapalı listeyle karşılaştırıldı; 'degil' göndergeleri A1'de ('qavvâmîne' ve 'şuhedâ'e' 5:8; 'l-mu'minûn' 5:11); 5:9 ve 5:10 esmâ yok; lafız 5:7 üç, 5:8 üç, 5:9 bir, 5:11 üç geçiş; 5:10 lafız yok; Rab yok",
 "esma_kayit: 5:7 ölçüm esmâ '{{1|عَلِيم 17\\. sırada, SON konum, MÜHÜRSÜZ}}' / esma_kayit çıktısı 'mühür EVET ton denge' (uyuşmuyor); 5:8 ölçüm esmâ '{{2|شَهِيد 7\\. sırada, ORTA konum, MÜHÜRSÜZ \\| خَبِير 24\\. sırada, SON konum, MÜHÜRSÜZ}}' / esma_kayit 'mühür EVET ton denge' (uyuşmuyor); "
 "5:11 ölçüm esmâ '{{5|مُؤْمِن 23\\. sırada, SON konum, MÜHÜRSÜZ}}' / esma_kayit 'mühür EVET ton cemâl' (uyuşmuyor) — mühür ölçütleri farklı (araç tanımı farkı); 5:11'de esma_kayit 'degil' adını mühüre sayıyor (§8); 5:9 ve 5:10 'mühür hayır' (uyuşuyor) — ölçüm alıntıları satır aynen",
 "ölçüm: 5:7 '{{1|fâsıla ٱلصدور → ر, R sınıfı — KAFİYE KIRILMASI}}', '{{1|simetri \\[3, 3, 14, 1\\]}}', '{{1|harf 91 → harf3 85, isaret 6}}' ve '{{1|dış düğüm 2}}'; 5:8 '{{2|biçim DIKKAT \\+ NEHY}}', '{{2|fâsıla تعملون → ن, N sınıfı}}', '{{2|harf 127 → harf3 117, isaret 10}}' ve '{{2|dış düğüm 3}}'; "
 "5:9 '{{3|yıldız yok}}', '{{3|fâsıla عظيم → م, N sınıfı}}', '{{3|harf 51 → harf3 46, isaret 5}}' ve '{{3|dış düğüm 2}}'; 5:10 '{{4|lafız YOK · Rab YOK}}', '{{4|yıldız yok}}', '{{4|fâsıla ٱلجحيم → م, N sınıfı}}', '{{4|harf 42 → harf3 39, isaret 3}}', '{{4|dış düğüm 1}}' ve '{{4|nakarat 2 \\(temsil None\\)}}'; "
 "5:11 '{{5|biçim DIKKAT}}', '{{5|fâsıla ٱلمؤمنون → ن, N sınıfı}}', '{{5|simetri \\[3, 6, 19, 1\\]}}', '{{5|harf 113 → harf3 107, isaret 6}}' ve '{{5|dış düğüm 2}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri alanı olmayan ayetler: 5:8, 5:9, 5:10; 5:10 ölçüm esit2 alanı okunmamış bir ayetle (sûre içi 1) TAM kademe veriyor — numarası basılmadığı için alıntılanmadı",
 "ölçüm aktör: 5:7-11 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:7 emir — IMPV 2 'zkurû' (1.), 'ttequ' (13.); 5:8 emir, yasak, nida — EMPH 1 'nûn' (10.), IMPV 3 'kûnû' (4.), 'dilû' (16.), 'ttequ' (20.), NEG 1 'lâ' (14.), PRO 1 'lâ' (9.), VOC 1 'yâ' (1.); biçim DIKKAT + NEHY D2'de yazılmadı; "
 "5:9 haber — kip yok; 5:10 haber — kip yok; 5:11 emir, nida — IMPV 3 'zkurû' (4.), 'ttequ' (18.), 'l-yetevekkel' (22.; morph 'li' IMPV önekiyle), VOC 1 'yâ' (1.); biçim DIKKAT D2'de yazılmadı; 5:9 ve 5:10'da edim değişmiyor (haber → haber)",
 "yıldız: 5:7 ★★, 5:8 ★, 5:11 ★★; 5:9 ve 5:10 yıldız yok — satır yıldız kaynağını adlandırmıyor; kaynak kapanış notunda bilançodan",
 "fâsıla: 5:6 ن (تشكرون) → 5:7 ر (ٱلصدور, R sınıfı — ölçüm KAFİYE KIRILMASI) → 5:8 ن (تعملون) → 5:9 م (عظيم) → 5:10 م (ٱلجحيم) → 5:11 ن (ٱلمؤمنون); N sınıfı (ن / م) 5:8-11 boyunca, ر kırığı 5:7'de; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:7 xref okunmuş iki ayet; 5:8 xref 4:135 ve 59:18 (basılmış), okunmuş bir ayet; 5:9 xref 48:29 (basılmış), okunmuş bir ayet; 5:10 xref 57:19 (basılmış), okunmamış bir ayet (sûre içi 1); 5:11 xref 33:9 (basılmış), okunmuş bir ayet — sınıflama sinifla.py ile, basılmamışlar numarasız",
 "nakarat3 (R3: sayıyla özetlendi): 5:7 üç kalıp: hepsi süzgeç GEÇER; 5:8 dört kalıp: hepsi süzgeç GEÇER; 5:9 bir kalıp: süzgeç GEÇER; 5:10 bir kalıp: süzgeç GEÇER (tür tam); 5:11 dört kalıp: üçü süzgeç GEÇER, biri GEÇMEZ",
 "araç tanımı farkları (R5; nakarat3 'tür ic' = sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si — taban sayımın kendi sözlüğünden betikle; karşılaştırma eşit aralıkla; nakarat3 kalıp adları ham LEM ile): " + '; '.join(r5),
 "aktör / ad (1017, R1): 5:7 muhatap 2MP (adsız), Allah (lafız), 'vâsaqa' faili 3MS (adsız), söz içi konuşan 1P (adsız); 5:8 muhatap 2MP (adsız), 'qavvâmîne' / 'şuhedâ'e' (haber), 'şene'ânu qavmin' (fail), 'huve' (zamir); 5:9 Allah (lafız), 'llezîne âmenû ve 'amilu's-sâlihâti' (mef'ûl), "
 "'âmenû' / ''amilu' faili 3MP (adsız); 5:10 'llezîne keferû ve kezzebû' (mübtedâ), failler 3MP (adsız), konuşan 1P (adsız; 'âyâtinâ'), 'ulâ'ike'; 5:11 muhatap 2MP (adsız), Allah (lafız), 'qavmun', 'yebsutû' faili 3MP (adsız), 'keffe' faili 3MS (adsız), 'l-mu'minûn' — "
 "A1'e yazılmayanlar: 5:7 'bihî' (mecrur zamir), 5:9 'lehum' (mecrur zamir), 5:11 'ileykum' / ''ankum' (muhatap içinde anıldı); 5:8 'li'llâhi' (lafız ayrıca anıldı), 'bi'l-qısti' (mecrur belirli tekil); blokta mecrur ilgi zamiri yok; 'kâne / leyse' ismi nekre yok ('kûnû' ismi muhatap)",
 "söz / tırnak: 5:7 'qultum' (10. kelime) — söz 11. kelimede açılıyor, 12. kelimede kapanıyor ('semi'nâ ve eta'nâ'; 13. kelime 've'ttequ' morph CONJ — sözün açıkça bittiği yer, tırnak kapandı); 12. kelime 've eta'nâ' CONJ (söz içi); "
 "5:9 vaat içeriği 'lehum mağfiratun ve ecrun 'azîm' (söz biçimli içerik) — 'qâle'siz, A3'e '(söz biçimli içerik)', A4'te 'söz açılır' yazılmadı, mealde tırnak yok; morph 've' / 'fe' konumlarıyla kontrol edildi: 5:7 've'zkurû' (1.), 've mîsâqahu' (5.), 've eta'nâ' (12.), 've'ttequ' (13.) CONJ; "
 "5:8 've lâ' (9.) CONJ, 've'ttequ' (20.) REM; 5:9 've 'amilu' (5.), 've ecrun' (9.) CONJ; 5:10 've'llezîne' (1.) REM, 've kezzebû' (3.) CONJ; 5:11 'fe-keffe' (15.) CONJ, 've'ttequ' (18.) CONJ, 've 'ale'llâhi' (20.) REM, 'fe'l-yetevekkel' (22.) SUP",
 "◈ tetik (alıntılar önek ve edatsız): 5:7 ◈B سمع ('semi'nâ' 11. kelime — B3; anlam notu: 'işittik' itaat beyanı, duyu bildirimi değil — tetik aracı kökü mekanik okur); 5:11 ◈B يدي ('eydiyehum' 14. ve 16. kelime — B3); 5:8, 5:9, 5:10 tetik yok; "
 "tetik listesinde olmayan organ adları (bölüm 1 denetimi kuralı 9): 5:7 's-sudûr' (göğüsler; صدر); 5:10 'l-cahîm' (yer adı, tetik dışı); oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:7 (2:285, 3:119, 24:51; 5:4 sûre içi; 5:8 ve 5:11 blok içi), 5:8 (2:237, 4:135, 59:18; 5:2 sûre içi; 5:7 ve 5:11 blok içi), 5:9 (48:29, 49:3), 5:10 (2:39, 57:19), 5:11 (3:122, 33:9, 35:3, 64:13; 5:7 ve 5:8 blok içi) (kontrol.py ile); "
 "blok içi bağlar 5:7 → 5:8 (önek kesilmiş 've'ttequ'llâhe inna'llâh'), 5:7 → 5:11 (lemma dizisi 'zekera ni'me allâh 'alâ'), 5:8 → 5:11 (harekesiz 'yâ eyyuhe'llezîne âmenû') iki ayetin D3'ünde; sayımları iki ayetin ◇ satırında (bölüm 1 denetimi OLASI 8); "
 "D3 dışı bırakılan basılmış sayım eşleri (bütün sayımların 'okumada görüldü' kümesinden): 5:7 've'ttequ'llâh' sayımlarındaki 5:2, 49:1, 59:7, 59:18 (genel kalıp; 5:4 sûre içi bağı yeterli), 'zekera ni'me' lemma dizisindeki 33:9 ve 35:3 (bağları 5:11'de); "
 "5:8 'yâ eyyuhe'llezîne âmenû' sayımındaki 4:43, 5:1, 5:6, 33:9, 49:1, 60:10 ve 've'ttequ'llâh' sayımlarındaki 5:4, 49:1, 59:7 (genel kalıp); 5:11 'yâ eyyuhe'llezîne âmenû' sayımındaki 4:43, 4:135, 5:1, 5:2, 5:6, 49:1, 59:18, 60:10 ve 've'ttequ'llâh' sayımındaki 2:194, 2:196, 5:2, 5:4, 49:1, 59:7, 59:18 (genel kalıp)",
 "◈A A4 (R9 + kapsam): 5:7 edim geçişi emir, nida, şart → emir (ayetler arası); şahıs geçişi yok (2 → 2); söz açılır (11. kelime); söz kapanır (12. kelime); 5:8 hitap açılır; edim geçişi emir → emir, yasak, nida (ayetler arası); şahıs geçişi yok; "
 "5:9 edim geçişi emir, yasak, nida → haber (ayetler arası); şahıs geçişi 2 → 3 (ayetler arası); 5:10 '—' (edim haber → haber, şahıs 3 → 3); 5:11 hitap açılır; edim geçişi haber → emir, nida (ayetler arası); şahıs geçişi 3 → 2 (ayetler arası); bölüm kapanışı; "
 "'iz' (5:7 9. kelime, 5:11 8. kelime) zaman (morph T) — şart sayılmadı",
 "sözdizimi (okuma; 'atıf' / 'istînâf' / 'hâl' her geçişte morph etiketiyle; 'X'a atıf' yazımında X ma'tûf aleyh): 5:7 've'zkurû ni'meta'llâhi' — 5:6 emir dizisine atıf (morph CONJ; ayet başı); 've mîsâqahu' — 'ni'mete'ye atıf (morph CONJ); 'ellezî vâsaqakum' — 'mîsâqahu'nun sıfatı (mevsûl); "
 "'iz qultum' — zaman (morph T); 've eta'nâ' — 'semi'nâ'ya atıf (morph CONJ; söz içi); 've'ttequ'llâh' — 've'zkurû'ya atıf (morph CONJ); 'inna'llâhe 'alîmun' — 'inne' cümlesi (morph ACC); "
 "5:8 'kûnû qavvâmîne' — emir, 'kâne' haberi çoğul; 'şuhedâ'e' — 'kâne'nin haberi (mansub), 'qavvâmîne'den sonra; 've lâ yecrimennekum' — 'kûnû'ya atıf (morph CONJ), yasak; 'alâ ellâ ta'dilû' — 'en' masdar; 'dilû huve aqrab' — yeni emir cümlesi (morph etiketi yok); "
 "'ve'ttequ'llâh' — istînâf (morph REM); 5:9 've'ade'llâhu' — fiil cümlesi; 've 'amilu' — 'âmenû'ya atıf (morph CONJ); 'lehum mağfiratun' — vaat içeriği, isim cümlesi; 've ecrun' — 'mağfiratun'a atıf (morph CONJ); "
 "5:10 've'llezîne keferû' — istînâf (morph REM), 5:9'a karşıt; 've kezzebû' — 'keferû'ya atıf (morph CONJ); 'ulâ'ike ashâbu'l-cahîm' — mübtedânın haberi; 5:11 'zkurû' — emir; 'iz hemme' — zaman (morph T); 'en yebsutû' — 'en' masdar; "
 "'fe-keffe' — 'hemme'ye atıf (morph CONJ); 've'ttequ'llâh' — 'zkurû'ya atıf (morph CONJ); 've 'ale'llâhi fe'l-yetevekkel' — istînâf (morph REM), 'fe' morph SUP",
 "okuma (gözlem) (iddialar ölçüm ve morph ile denetlendi; sayı sözcükleri konum listesiyle betikle karşılaştırıldı): 5:7 ve 5:11 'zkurû ni'meta'llâhi 'aleykum' ile açılıyor (5:7 1-4. kelime, 5:11 4-7. kelime) — harekesiz yazım farkı (ة / ت), lemma dizisi eş; "
 "5:7, 5:8 ve 5:11 've'ttequ'llâh' emriyle (5:7 13. kelime, 5:8 20. kelime, 5:11 18. kelime); 5:8 kök عدل iki geçiş (15., 16. kelime) — adaletsizlik / adalet emri; 5:8 4-8. kelime 4:135 açılışının kelime sırası ters ('li'llâhi' / 'bi'l-qıst'); "
 "5:9 / 5:10 iman eden - salih amel işleyen / inkâr eden - yalanlayan karşıtlığı; 5:11 'eydiyehum' iki geçiş (14., 16. kelime) — uzatma / çekme; 5:7 söz 'semi'nâ ve eta'nâ' 2:285 ve 24:51 ile",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (sunum/es_edat.py — morph etiketli, zamirler birleşik): " + ES
 + "; bölüm 2 geneli eş edat / zamir karşılıkları (bloklar 3-4; bölüm 1 denetimi kuralı 6): " + ESB + "; eş lemmaya farklı karşılık (sunum/es_lemma.py, bloklar 3-4): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (bölüm 1 denetimi kuralı 10): 'qıst' 5:8 'adalet' / 4:135 'adalet'; 'mîsâq' 5:7 'ahit' — emsal yok; 'cahîm' 5:10 'alevli ateş' / 57:19 meali 'cehennem' — tam okuma sonu",
 "KARSILIK_CAKISMA",
 "çıpa: 5:7-11 tarayıcı aday vermedi (cipa_tarama5_adaylari.json); anma emri, adalet emri, vaat, akıbet bildirimi, geçmiş olay anma (olgu=False); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:8 (''alâ ellâ ta'dilu' / 'dilû huve aqrabu li't-taqvâ'), 5:11 ('en yebsutû ileykum eydiyehum' / 'fe-keffe eydiyehum 'ankum') — okuma; ayetler arası 5:9 / 5:10 ('llezîne âmenû ve 'amilu's-sâlihâti' / 've'llezîne keferû ve kezzebû', blok içi)",
 "aday 1041: kök أمن 5:11 'âmenu' (muhatap) ve 'l-mu'minûn' — insan; blokta lafız / Rab göndergeli kökün insan için kullanıldığı vaka yok (5:7 'vâsaqa' (lafız) ve 'mîsâq' — kök وثق blokta yalnız ilahi ahit için) — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 2-2 — bölüm kapanışı 5:11; bölüm iki blok (blok planından: 3 ve 4); başlıktaki 'nimeti ve misakı anma' 5:7 ('ve'zkurû ni'meta'llâhi 'aleykum ve mîsâqahu') ve 5:11; mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; "
 "bölüm sonu bağımsız denetimi bu bloktan sonra (bulgular yamalar/bekleyen_ariza_5_b04.txt); medde taraması (sunum/medde.py b04/say2.txt): on meddeli kalıp — 5:8 4-8 ve 5:11 1-7 'korpusta 1' lemma dizisiyle de 1 / yazım farkıyla eşli (lemma dizisi 'eyy ellezî âmene zekera ni'me allâh 'alâ' 2 ayet), yanlış 'korpusta 1' yok",
 "sonradan basılan (bölüm 8 kuralı 1; bölüm 16 denetimi kuralı 3; bölüm 1 denetimi kuralı 1 — lemma dizileri dahil; sunum/sonradan.py --plan 4): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; liste metin oluşturucusundaki say() dönüşleriyle): " + ', '.join(K1.values()),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('mîsâq', 'vâsaqa', 'hemme', 'zû', 'qavvâm', 'şehîd', 'qıst', 'aqrab', 'mağfire', 'sâliha', 'âye', 'ashâb'; morph LEM ham biçim: 'yecrime', 'tevekkel' — sunum/lem_norm.json); ortaçlarda bab etiketi ◇'de yazılmadı; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; 5:8 wasl ''dilû' (16. kelime) — hemzeli emir, ◇'de 'ta'dilu 'dilû' yazımı; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]


def yaz():
    items = [kes(x) for x in I]
    s = '\n (7, 11): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_7_11.txt', 'w', encoding='utf-8').write(s)


idx = I.index('KARSILIK_CAKISMA')
I[idx] = 'karşılık çakışması (geçici)'
yaz()
CAK = run('/home/claude/sunum/cakisma.py', '/home/claude/yamalar/ariza_5_5_6.txt', '/home/claude/yamalar/ariza_5_7_11.txt')
KARAR = {}
if os.path.exists('/home/claude/b04/yap/karar.py'): exec(open('/home/claude/b04/yap/karar.py', encoding='utf-8').read())
I[idx] = ("karşılık çakışması (sunum/cakisma.py bölüm 2 ARIZA meal maddeleri (bloklar 3-4); kararlar morph LEM eşitliğine göre): "
          + ('; '.join(KARAR.get(l.split(' ←')[0], l + ' — karar yok') for l in CAK.splitlines()) if CAK else 'çakışma yok'))
yaz()
print('yazıldı', len(I))
print(CAK)
