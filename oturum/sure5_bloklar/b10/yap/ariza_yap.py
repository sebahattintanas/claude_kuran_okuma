# blok 10 (5:27-30) ARIZA oluşturucu — bölüm 5-1 (bölüm açılışı)
import sys, os, ast, subprocess, re
os.environ['OLC'] = '/home/claude/b10/olcum.txt'
os.environ['SAY2'] = '/home/claude/b10/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

VF_YAZI = {27: {1: "'ve'tlu'", 10: "'fe-tuqubbile'", 13: "'ve lem'"}, 29: {6: "'ve ismike'", 7: "'fe-tekûne'", 11: "'ve zâlike'"},
           30: {1: "'fe-tavva'at'", 6: "'fe-qatelehû'", 7: "'fe-asbaha'"}}
BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b09.txt', encoding='utf-8').read() + ']')
BOL = "'Âdem'in iki oğlu; bir canı öldürmek'"


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



R5 = []
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

M27 = ("5:27 'Onlara Âdem'in iki oğlunun haberini gerçekle oku' ('ve'tlu 'aleyhim nebe'e'bney âdeme bi'l-haqq', 've' 1. kelimede karşılıksız (morph CONJ; ayet başı), 'oku-' 'tlu' karşılığı (1. kelime; emir 2MS), ''alâ' 2. kelimede yönelme eki ile ('onlara' içinde), 'hum' 2. kelimede 'onlar' ile, "
 "'haber' 'nebe'' karşılığı (3. kelime; iyelik ve belirtme takdiri), 'oğul' 'ibn' karşılığı (4. kelime; ikil — 'iki' sayı açılımı; iyelik), 'Âdem' 'âdem' karşılığı (5. kelime; özel ad; izafet), 'bi' 6. kelimede '-le' ile, 'gerçek' 'haqq' karşılığı (6. kelime), sıralama: tümleç öne, fiil sona alındı); "
 "'Hani onlar birer kurban sunmuşlardı' ('iz qarrabâ qurbânen', 'iz' 7. kelimede 'hani' ile (zaman; morph T), 'kurban sun-' 'qarrabâ' açılımı (8. kelime; II. bab; ikil — 'onlar' ve '-lardı' ile), 'kurban' 'qurbân' karşılığı (9. kelime; nekre — 'birer' takdiri; ölçüm mm2 — fiil ile kök eşi), sıralama: fiil sona alındı); "
 "'da birinden kabul edilmiş' ('fe-tuqubbile min ehadihimâ', 'fe' 10. kelimede 'da' ile (morph CONJ), 'kabul edil-' 'tuqubbile' açılımı (10. kelime; V. bab; edilgen; '-miş' anlatı), 'min' 11. kelimede '-den' ile, 'biri' 'ehad' karşılığı (12. kelime; iyelik ile), 'himâ' 12. kelimede iyelik ile ('birinden' içinde), sıralama: fiil sona alındı); "
 "'ötekinden kabul edilmemişti' ('ve lem yutaqabbel mine'l-âxar', 've' 13. kelimede karşılıksız (virgül; morph CONJ), 'lem' 13. kelimede '-me-' ile (olumsuz geçmiş; morph NEG), 'kabul edil-' 'yutaqabbel' açılımı (14. kelime; V. bab; edilgen), 'min' 15. kelimede '-den' ile, 'öteki' 'âxar' karşılığı (16. kelime), sıralama: fiil sona alındı); "
 "'Seni mutlaka öldüreceğim' dedi' ('qâle le-aqtulenneke', 'de-' 'qâle' karşılığı (17. kelime), 'le' 18. kelimede karşılıksız (morph EMPH; 'mutlaka' ile ortak), 'öldür-' 'aqtul' karşılığı (18. kelime; gelecek '-eceğim' açılımı), 'nne' 18. kelimede 'mutlaka' ile (morph EMPH), 'ke' 18. kelimede 'seni' ile, sıralama: söz öne, fiil sona alındı); "
 "'Öteki dedi ki' ('qâle', 'de-' 'qâle' karşılığı (19. kelime), 'öteki' takdir (19. kelime; fail açılımı), 'ki' takdir (19. kelime; söz açılışı)); "
 "'Allah ancak sakınanlardan kabul eder' ('innemâ yetaqabbelu'llâhu mine'l-muttaqîn', 'inne' 20. kelimede karşılıksız ('innemâ' — 'ancak' içinde), 'mâ' 20. kelimede 'ancak' ile (morph PREV; hasr), 'kabul et-' 'yetaqabbelu' açılımı (21. kelime; V. bab), lafız 22. kelimede 'Allah' ile, 'min' 23. kelimede '-dan' ile, "
 "'sakınan' 'muttaqî' karşılığı (24. kelime; etken ortaç; çoğul '-lar'), sıralama: fail öne, fiil sona alındı)")
M28 = ("5:28 'Andolsun, beni öldürmek için elini bana uzatsan da' ('le-in besatte ileyye yedeke li-taqtulenî', 'le' 1. kelimede 'andolsun' ile (morph EMPH), 'in' 1. kelimede şart eki ile ('uzatsan' içinde; morph COND), 'uzat-' 'besatte' karşılığı (2. kelime; '-san da' — şart ve kabul), 'te' 2. kelimede 2MS ile ('uzatsan' içinde), 'ilâ' 3. kelimede yönelme eki ile ('bana' içinde), "
 "'î' 3. kelimede 'ben' ile ('bana' içinde), 'el' 'yed' karşılığı (4. kelime; belirtme takdiri), 'ke' 4. kelimede iyelik ile ('elini' içinde), 'li' 5. kelimede 'için' ile (morph PRP; amaç), 'öldür-' 'taqtulu' karşılığı (5. kelime; masdar '-mek' açılımı), 'nî' 5. kelimede 'beni' ile, sıralama: amaç öne, fiil sona alındı); "
 "'ben seni öldürmek için elimi sana uzatacak değilim' ('mâ ene bi-bâsitin yediye ileyke li-aqtuleke', 'mâ' 6. kelimede 'değil' ile (morph NEG), 'ene' 7. kelimede 'ben' ile, 'bi' 8. kelimede karşılıksız (haber pekiştirmesi), 'uzatacak' 'bâsit' karşılığı (8. kelime; etken ortaç), 'el' 'yed' karşılığı (9. kelime; belirtme takdiri), "
 "'î' 9. kelimede iyelik ile ('elimi' içinde), 'ilâ' 10. kelimede yönelme eki ile ('sana' içinde), 'ke' 10. kelimede 'sen' ile ('sana' içinde), 'li' 11. kelimede 'için' ile (morph PRP; amaç), 'öldür-' 'aqtulu' karşılığı (11. kelime; masdar açılımı), 'ke' 11. kelimede 'seni' ile, sıralama: amaç öne, haber sona alındı); "
 "'çünkü ben âlemlerin Rabbi Allah'tan korkarım' ('innî exâfu'llâhe rabbe'l-'âlemîn', 'inne' 12. kelimede 'çünkü' ile (gerekçe okuması), 'î' 12. kelimede 'ben' ile, 'kork-' 'exâfu' karşılığı (13. kelime; geniş zaman), lafız 14. kelimede 'Allah'tan' ile ('-tan' fiil yönetimi takdiri), "
 "'Rab' 'rabb' karşılığı (15. kelime; iyelik ile 'Rabbi'), 'âlem' ''âlem' karşılığı (16. kelime; çoğul '-ler'; izafet), sıralama: sıfat öne, fiil sona alındı)")
M29 = ("5:29 'Ben istiyorum ki' ('innî urîdu', 'inne' 1. kelimede karşılıksız (pekiştirme), 'î' 1. kelimede 'ben' ile, 'iste-' 'urîdu' karşılığı (2. kelime; IV. bab; '-iyorum'), 'ki' takdir (2. kelime; tümleç cümlesi açılışı)); "
 "'benim günahımı da kendi günahını da yüklenesin' ('en tebû'e bi-ismî ve ismik', 'en' 3. kelimede istek eki ile ('yüklenesin' içinde; morph SUB), 'yüklen-' 'tebû'e' karşılığı (4. kelime; istek 2MS), 'bi' 5. kelimede karşılıksız (mef'ûl belirtme ile), 'günah' 'ism' karşılığı (5. kelime), "
 "'î' 5. kelimede 'benim' ile, 've' 6. kelimede 'da' ile ('da … da' içinde; morph CONJ), 'günah' 'ism' karşılığı (6. kelime), 'ke' 6. kelimede 'kendi' ile ('kendi günahını' — iyelik), sıralama: fiil sona alındı); "
 "'de ateş halkından olasın' ('fe-tekûne min ashâbi'n-nâr', 'fe' 7. kelimede 'de' ile (morph CONJ), 'ol-' 'tekûne' karşılığı (7. kelime; istek 2MS), 'min' 8. kelimede '-dan' ile, 'halk' 'ashâb' karşılığı (9. kelime; LEM 'ashâb' — çoğul biçim (morph LEM ham biçim); iyelik), 'ateş' 'nâr' karşılığı (10. kelime; izafet), sıralama: fiil sona alındı); "
 "'zalimlerin cezası budur' ('ve zâlike cezâ'u'z-zâlimîn', 've' 11. kelimede karşılıksız (noktalı virgül; morph REM), 'zâlike' 11. kelimede 'bu' ile, 'ceza' 'cezâ'' karşılığı (12. kelime; iyelik ile), 'zalim' 'zâlim' karşılığı (13. kelime; etken ortaç; çoğul '-ler'; izafet), '-dur' takdir (11. kelime; isim cümlesi), sıralama: haber öne)")
M30 = ("5:30 'Sonunda nefsi ona kardeşini öldürmeyi kolay gösterdi' ('fe-tavva'at lehû nefsuhû qatle exîh', 'fe' 1. kelimede 'sonunda' ile (morph REM), 'kolay göster-' 'tavva'at' açılımı (1. kelime; II. bab; LEM 'tavva'at' (morph LEM ham biçim)), 'li' 2. kelimede yönelme eki ile ('ona' içinde), 'hû' 2. kelimede 'o' ile ('ona' içinde), "
 "'nefis' 'nefs' karşılığı (3. kelime), 'hû' 3. kelimede iyelik ile ('nefsi' içinde), 'öldürme' 'qatl' karşılığı (4. kelime; masdar; belirtme takdiri), 'kardeş' 'ex' karşılığı (5. kelime), 'hî' 5. kelimede iyelik ile ('kardeşini' içinde), sıralama: fail öne, fiil sona alındı); "
 "'onu öldürdü' ('fe-qatelehû', 'fe' 6. kelimede karşılıksız (noktalı virgül; morph CAUS), 'öldür-' 'qatele' karşılığı (6. kelime), 'hû' 6. kelimede 'onu' ile, sıralama: fiil sona alındı); "
 "'ve hüsrana uğrayanlardan oldu' ('fe-asbaha mine'l-xâsirîn', 'fe' 7. kelimede 've' ile (morph CONJ), 'ol-' 'asbaha' karşılığı (7. kelime; IV. bab; 'kâne' ailesi — 'sabahlamak' anlamı değil), 'min' 8. kelimede '-dan' ile, 'hüsrana uğrayan' 'xâsir' açılımı (9. kelime; etken ortaç; çoğul '-lar'), sıralama: fiil sona alındı)")
MEALS = (M27, M28, M29, M30)


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
open('/home/claude/b10/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '10')
ESL = run('/home/claude/sunum/es_lemma.py', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '10').replace('\n', '; ')
EMS = open('/home/claude/b10/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '27', '30', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b10/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
MFARK = [(k, n, sayim.S2[k.replace(' --medde', '')][0]) for k, (n, d) in sayim.S2.items() if '--medde' in k]
MEDF = '; '.join("%s meddeli %d / meddesiz %d" % (k.replace(' --medde', ''), m, n) for k, n, m in MFARK)
MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else ' — FARK VAR'


M = {}; exec(open('/home/claude/yamalar/metin_5_27_30.txt', encoding='utf-8').read(), {'MEAL': {}, 'M': M})
M_A1 = ' '.join(M[a][M[a].index('◈A'):M[a].index(' A2 ')] for a in range(27, 31))
GLS = run('/home/claude/sunum/gloss_tara.py', '27', '30', '10').splitlines()
GKAP = GLS[0] if GLS else 'KAPSAMAYAN ?'

KUR = run('/home/claude/sunum/bolum4_kurallar.py', '27', '30', '10').splitlines()
KREM = '; '.join(l[4:] for l in KUR if l.startswith('REM '))
KALAN = [l[10:] for l in KUR if l.startswith('ALAN YOK: ')]
KHATA = [l for l in KUR if l.startswith('HATA')]
AYN = 'AYN_SONUC'
BEK = [b.replace("(blok 9 ham LEM maddesi bu ikisini ham biçim sayıyor)", "(blok 9 ham LEM maddesi bu iki adı ham biçim sayıyor)").replace("'dört ayetin' ardından 'üç' + iyelik + bulunma eki biçimi", "sayı + 'ayetin' ardından sayı + iyelik + bulunma eki biçimi").replace("('ikisinde', 'üçünde', 'dördünde' …)", "(sayı + iyelik + bulunma eki biçimleri)") for b in BEK]  # yasakli.sh kuralı 12 sonrası: denetimin alıntıladığı yasaklı örnekler biçim adıyla
I = list(BEK) + [
 "kök tablosu: ölçümde '???' 5:27, 5:28, 5:29 ve 5:30 için ayrı sayıldı — 0; yeni kök yok (okunan ayetlerde tabloda olmayan kök 0); gloss kapsam taraması (bölüm 3 denetimi kuralı 8, bölüm 4 kuralı 7; komut 'python3 sunum/gloss_tara.py 27 30 10' — meal karşılığının baştaki dört harfi ölçüm glossunda aranır): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:27:12 أَحَد 'degil' — 'min ehadihimâ', kural 'esmâ adı esmâ dışı göndergeyle → degil' (iki oğuldan biri) (esma_el_ekle → esma_kayit; e_el=? 0); kural adı kapalı listeyle karşılaştırıldı; 'degil' göndergesi A1'de ('ehadihimâ' — " + ('A1 VAR' if "'ehadihimâ'" in M_A1 else 'A1 YOK') + "); "
 "lafız 5:27 bir, 5:28 bir geçiş; Rab 5:28 'rabbe'l-'âlemîn' (15. kelime; lafzın sıfatı, söz içi); 5:29 ve 5:30 lafız ve Rab yok",
 "esma_kayit: 5:27 'mühür hayır' (ölçüm esmâ MÜHÜRSÜZ — uyuşuyor), 5:28 'mühür hayır' (sınıf AR/AR), 5:29 ve 5:30 'mühür hayır' (sınıf 0/0) — uyuşuyor",
 "ölçüm: 5:27 '{{1|yıldız yok}}', '{{1|EDİLGEN 2/8 fiil, pas z=1,10}}', '{{1|mm2: \\[8, قرب}}', '{{1|sayı işareti أَحَد}}', '{{1|fâsıla ٱلمتقين → ن, N sınıfı}}', '{{1|simetri \\[3, 10, 14, 1\\]}}', '{{1|harf 104 → harf3 101, isaret 3}}' ve '{{1|dış düğüm 0}}'; "
 "5:28 '{{2|رَبّ 15\\. sırada \\(rab z=1,01\\)}}', '{{2|yıldız yok}}', '{{2|fâsıla ٱلعلمين → ن, N sınıfı}}', '{{2|simetri \\[3, 1, 10, 1\\]}}', '{{2|harf 67 → harf3 63, isaret 4}}' ve '{{2|dış düğüm 1}}'; 5:29 '{{3|lafız YOK · Rab YOK}}', '{{3|fâsıla ٱلظلمين → ن, N sınıfı}}', '{{3|harf 56 → harf3 54, isaret 2}}' ve '{{3|dış düğüm 0}}'; "
 "5:30 '{{4|lafız YOK · Rab YOK}}', '{{4|iltifât 1}}', '{{4|fâsıla ٱلخسرين → ن, N sınıfı}}', '{{4|harf 40 → harf3 37, isaret 3}}' ve '{{4|dış düğüm 0}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (bölüm 4 denetimi kuralı 10; komut 'python3 sunum/bolum4_kurallar.py 27 30 10'): " + '; '.join(KALAN),
 "ölçüm aktör: 5:27 '{{1|aktör: adlı آدَم 5\\. sırada \\(kisi, rol mecrur\\)}}' — sözdiziminde 'bney'in muzâfun ileyhi; 5:28-30 aktör yok (konuşanlar adsız: kurbanı kabul edilen / edilmeyen kardeş, A1'de)",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:27 emir — EMPH 2 'le' ve 'nne' (18.), IMPV 1 'tlu' (1.), NEG 1 'lem' (13.); EDİLGEN 'tuqubbile' (10.), 'yutaqabbel' (14.) — morph PASS; 5:28 şart — COND 1 'in' (1.), EMPH 1 'le' (1.), NEG 1 'mâ' (6.); 'li' (5. ve 11.) morph PRP; "
 "5:29 haber — kip yok; 'en' (3.) morph SUB; 5:30 haber — kip yok; ölçüm iltifât 1 (5:30) — 3FS 'tavva'at' ile 3MS fiiller arası okunuyor; aday kayıt, tam okuma sonu",
 "yıldız: blokta yıldız yok (5:27-30)",
 "fâsıla: 5:26 ن (ٱلفسقين) → 5:27 ن (ٱلمتقين) → 5:28 ن (ٱلعلمين) → 5:29 ن (ٱلظلمين) → 5:30 ن (ٱلخسرين); bölüm açılışında N sınıfı sürüyor; dört ayet belirli çoğul etken ortaç / isimle bitiyor; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:28 xref 59:16 (basılmış); 5:27, 5:29, 5:30 xref yok — sınıflama sinifla.py ile",
 "araç tanımı farkları (R5): blokta nakarat3 kalıbı yok — karşılaştırılacak madde yok (bölüm 4 kuralı 11 şablonu aşağıdaki nakarat3 maddesinde)",
 "nakarat3 (R3: sayıyla özetlendi): blokta nakarat3 kalıbı yok (5:27, 5:29, 5:30 'bağ: YOK'; 5:28 yalnız xref) — R5 maddesi yok (bölüm 4 denetimi kuralı 11 şablonu: nakarat3 'tür' alanı 'tam' / 'ic' — sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; eşi okunmamış hükümde '(eş okunmamış, fark test edilmedi)')",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9 — söz içi 1P / 1S / 2MP / 2MS ve 3D / 3MD zamirler 'adsız'): 5:27 muhatap 2MS (adsız), 3MP (adsız), 'bney âdeme' (adlı aktör içeren izafet), 3MD (adsız), 'qurbânen', edilgen failler (adsız; nâib fâil), 3D (adsız), 'l-âxar', iki 'qâle' faili 3MS (adsız), söz içi 1S / 2MS (adsız), Allah (lafız), 'l-muttaqîn'; "
 "5:28 söz içi 1S / 2MS (adsız), Allah (lafız), Rab; 5:29 söz içi 1S / 2MS (adsız), 'ashâbi'n-nâr', 'zâlike', 'z-zâlimîn'; 5:30 'nefsuhû', 3MS (adsız), 'exîhi', 'l-xâsirîn' — betik denetimi (sunum/bolum4_kurallar.py): " + ('; '.join(h for h in KHATA if 'adsız' in h or 'muhatab' in h) or 'adsız / söz muhatabı hatası 0') + "; blokta 'li-X' söz muhatabı yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): 5:27 'qâle' (17. kelime) — söz 18. kelimede açılıp kapanıyor ('le-aqtulenneke'); 'qâle' (19. kelime) — söz 20. kelimede açılıyor, 5:28 boyunca sürüyor, 5:29 13. kelimede kapanıyor (tırnak 5:27 mealinde açılıp 5:29 mealinde kapandı); 5:30 anlatı; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 27 30 10' — A3 söz aralığı içinde morph REM): " + KREM + " — 5:29 11. kelime 've zâlike' (morph REM) söz içinde sürdürüldü: 'REM sapması', gerekçe 2MS / 1S zamirleri yok ama 'zâlike' göndergesi sözdeki ateş halkı olmak — sözün kapanışı okuması (anlatıcı yorumu da okunabilir; tam okuma sonu); "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:27 've'tlu' (1.) CONJ, 'fe-tuqubbile' (10.) CONJ, 've lem' (13.) CONJ; 5:29 've ismike' (6.) CONJ, 'fe-tekûne' (7.) CONJ, 've zâlike' (11.) REM; 5:30 'fe-tavva'at' (1.) REM, 'fe-qatelehû' (6.) CAUS, 'fe-asbaha' (7.) CONJ; 5:28 've' / 'fe' yok",
 "◈ tetik (alıntılar önek ve edatsız; bölüm 3 kuralı 3 — alt sınıf kökten, betikle: sunum/bolum4_kurallar.py ◈ denetimi " + ('; '.join(h for h in KHATA if h.startswith('HATA ◈')) or '0') + "): 5:28 ◈B يدي ('yedeke' 4. kelime, 'yediye' 9. kelime — B3; anlam notu: el uzatma, öldürme kastıyla); 5:27, 5:29, 5:30 tetik yok; "
 "tetik listesinde olmayan zaman / organ / yer adları (bölüm 2 kuralı 9, tarama — elle): 5:27 'iz' (7. kelime; zaman edatı); 5:30 'nefsuhû' (3. kelime; nefis — kök نفس tetik dışı), 'asbaha' (7. kelime; kök صبح 'sabah' — burada 'oldu', zaman anlamı yok); 5:29 'n-nâr' (10. kelime; ateş — kök نور tetik dışı); oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8; bölüm 3 kuralı 11): D3 eşleri bag listesiyle birebir — 5:27 (3:183, 10:71), 5:28 (59:16), 5:29 (28:27, 59:17), 5:30 eş yok (kontrol.py ile); bölüm geçişi 5:26 → 5:27 bağ kurulmadı; blok içi bağ yok; "
 "D3 dışı bırakılan basılmış sayım eşleri: 5:30 'mine'l-xâsirîn' (genel kalıp; korpusta on ayet) sayımındaki 3:85, 5:5, 39:65 — gerekçe: genel kalıpta bağ yok, basılmış eşlerin hiçbirine (ölçüt bir); 5:28 'rabbe'l-'âlemîn' (genel kalıp, otuz dört ayet) sayımındaki 59:16 — bağ dört kelimelik kalıpla ('exâfu'llâhe rabbe'l-'âlemîn')",
 "◈A A4 (R9 + kapsam; bölüm 3 kuralı 2 — betikle: " + ('; '.join(h for h in KHATA if 'A4' in h) or 'A4 şart → cevap hatası 0') + "): 5:27 bölüm açılışı; edim geçişi haber → emir (ayetler arası); şahıs geçişi yok; söz açılır / kapanır (18. kelime); söz açılır (20. kelime); 5:28 edim geçişi emir → şart; şahıs geçişi 3 → 1; şart → cevap (ayet içi; COND 'in' 1. kelime); "
 "5:29 edim geçişi şart → haber; şahıs geçişi yok; söz kapanır (13. kelime); 5:30 edim geçişi yok (haber → haber); şahıs geçişi 1 → 3",
 "sözdizimi (okuma; 'atıf' / 'istînâf' / 'hâl' her geçişte morph etiketiyle): 5:27 've'tlu' — 5:26 anlatısına bağlanan emir (morph CONJ); 'bi'l-haqqi' — 'tlu'nun hâli ya da 'nebe'e'nin niteliği; 'iz qarrabâ' — zaman (morph T); 'fe-tuqubbile' — 'qarrabâ'ya atıf (morph CONJ); 've lem yutaqabbel' — 'tuqubbile'ye atıf (morph CONJ); "
 "'qâle le-aqtulenneke' — yeni cümle, yemin; 'qâle innemâ' — yeni cümle; 'innemâ' — hasr (morph PREV); 5:28 'le-in' — yemin + şart (morph EMPH + COND); 'li-taqtulenî' ve 'li-aqtuleke' — amaç (morph PRP); 'mâ ene bi-bâsitin' — yemin cevabı (şart cevabı yerinde), 'mâ' hicâzî olumsuzluk, 'bi' pekiştirme; 'innî exâfu' — 'inne' cümlesi, gerekçe; "
 "5:29 'innî urîdu en tebû'e' — 'en' masdar (morph SUB); 've ismike' — 'ismî'ye atıf (morph CONJ); 'fe-tekûne' — 'tebû'e'ye atıf (morph CONJ, mansub); 've zâlike' — istînâf (morph REM); 5:30 'fe-tavva'at' — istînâf (morph REM); 'fe-qatelehû' — sonuç (morph CAUS); 'fe-asbaha' — 'qatelehû'ya atıf (morph CONJ)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; kalıp eşleri sayımın basılmış kümesinden betikle — elle karşılaştırıldı): 5:27 've'tlu 'aleyhim nebe'' ile açılıyor (1-3. kelime) — sayımın basılmış eşi 10:71; 5:27 kök قبل üç geçiş (ölçüm kök ikilemesi; 10., 14., 21. kelime) — kabul / kabul edilmeme / ancak sakınanlardan kabul; "
 "5:28 ayet içinde karşılıklı yapı: 'besatte … yedeke … li-taqtulenî' / 'bi-bâsitin yediye … li-aqtuleke' (ölçüm kök ikilemesi بسط, يدي, قتل); 5:29 'cezâ'u'z-zâlimîn' — sayımın basılmış eşi 59:17; 5:30 kök قتل iki geçiş (4. ve 6. kelime) — öldürme isteği / öldürme; 5:27 'qâle' iki geçiş — iki kardeşin adsız konuşması",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 10' — tırnaksız biçimler ve 'î' / 'ke' / 'â' zamirleri dahil): " + ES
 + "; eş lemmaya farklı karşılık (bölüm 4 kuralı 8 — komut 'python3 sunum/es_lemma.py 1 2 3 4 5 6 7 8 9 10', sûre 5'in okunmuş bütün blokları; çıktı aynen): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (bölüm 2 kuralı 6 — elle): 'tlu … nebe'e' 5:27 'haberini oku' / 10:71 'haberini oku' (eş); 'qurbân' 5:27 'kurban' / 3:183 'kurban' (eş); 'exâfu'llâhe rabbe'l-'âlemîn' 5:28 / 59:16 'âlemlerin Rabbi Allah'tan korkarım' (eş); "
 "'urîdu en' 5:29 'istiyorum ki … -esin' / 28:27 'istiyorum' (eş); 've zâlike cezâ'u'z-zâlimîn' 5:29 'zalimlerin cezası budur' / 59:17 'İşte bu, zalimlerin cezasıdır' (yakın) — tam okuma sonu",
 "KARSILIK_CAKISMA",
 "çıpa: 5:27-30 tarayıcı aday vermedi (cipa_tarama5_adaylari.json); anlatı, söz, sonuç bildirimi (olgu=False); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:27 ('fe-tuqubbile min ehadihimâ' / 've lem yutaqabbel mine'l-âxar'; 'le-aqtulenneke' / 'innemâ yetaqabbelu'llâhu mine'l-muttaqîn'), 5:28 ('le-in besatte ileyye yedeke li-taqtulenî' / 'mâ ene bi-bâsitin yediye ileyke li-aqtuleke'), 5:29 ('bi-ismî' / 've ismike') — okuma; ayetler arası 5:27 / 5:28 ('le-aqtulenneke' / 'mâ ene bi-bâsitin'), 5:28 / 5:30 ('mâ ene bi-bâsitin' / 'fe-qatelehû') — blok içi",
 "aday 1041: kök قبل 5:27 'yetaqabbelu'llâhu' — lafzın kabulü; insan için kullanım yok; kök ربب 5:28 'rabbe'l-'âlemîn' — söz içinde lafzın sıfatı — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 5-1 — bölüm açılışı 5:27; bölüm iki blok (blok planından: 10 ve 11); başlıktaki 'Âdem'in iki oğlu' 5:27 ('nebe'e'bney âdeme'), 'bir canı öldürmek' 5:30 ('fe-qatelehû') ve blok 11'de; mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; "
 "bölüm 4 denetimi bulguları ve yeni kuralları bu ARIZA'nın başında; uygulanan araç değişiklikleri (bölüm 4 kuralı 15 — bu bloktan önce): sunum/es_edat.py (kural 5: tırnaksız biçimler, 'î' / 'ke' / 'â' zamirleri, ayrıştırılamayan sayısı), sunum/cakisma.py (kural 4: Türkçe fiil kökü eşlemesi, son dosyaya dokunan gruplar), sunum/gloss_tara.py (kural 7: hemze / ayn ile biten lemma, atlanan sayısı), "
 "sunum/yasakli.sh (kural 12: sayı + iyelik çekimleri, 'N ayetin'), sunum/ayn_kontrol.py (kural 13: fazladan kesme), sunum/bolum4_kurallar.py (kurallar 1, 9, 10 ve bölüm 3 kuralları 2-4: REM sapması, A4 şart, adsız, ◈ alt sınıf, aralık eşlemesi, simetri / İÇ düğüm alanı); elle kalanlar: kural 2 (R5 önek / medde sınaması — blokta R5 yok), kural 3 (kalıp adı — blokta nakarat3 yok), kural 6 (ham LEM notu taraması), kural 14 (gözlem kalıp eşi); "
 "medde taraması (sunum/medde.py b10/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 2 kuralları 4-5, bölüm 3 kuralı 9, bölüm 4 kuralı 6 — elle): sunum/lem_bozuk.py 10 çıktısı 5:30:1 'tavva'at' — meal maddesinde '(morph LEM ham biçim)' notlu; aracın bayraklamadığı ham biçim: 5:29:9 'ashâb' (çoğul biçim LEM) — notlu; başka maddede bu adlar geçmiyor",
 "öz denetim (bölüm 4 kuralı 13 — ayrı madde): sunum/ayn_kontrol.py 27 30 → " + AYN + "; blok 8'in fazladan kesme hatası (wasl 'dxulu' / 'dxulû' çift kesmeyle) yeni araçla yeniden üretildi (ayn_kontrol 20 23: KESME 3 isabet) — geriye dönük yeniden yazılmadı (§8); bloklar 5-9'da es_lemma.py blok listesi eksik verilmişti (araç aralık değil liste alıyor) — bu bloktan itibaren sûrenin bütün bloklarıyla",
 "sonradan basılan (bölüm 8 kuralı 1; bölüm 16 denetimi kuralı 3; bölüm 1 denetimi kuralı 1 — lemma dizileri dahil; sunum/sonradan.py --plan 10): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('nebe'', 'ibn', 'âdem', 'haqq', 'qurbân', 'ehad', 'âxar', 'muttaqî', 'yed', 'bâsit', 'rabb', ''âlem', 'ism', 'ashâb', 'nâr', 'cezâ'', 'zâlim', 'nefs', 'qatl', 'ex', 'xâsir'); "
 "transliterasyon yalnız 'l' birleşme / tanvin yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]


def yaz():
    items = [kes(x) for x in I]
    s = '\n (27, 30): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_27_30.txt', 'w', encoding='utf-8').write(s)


idx = I.index('KARSILIK_CAKISMA')
I[idx] = 'karşılık çakışması (geçici)'
yaz()
AYN = (run('/home/claude/sunum/ayn_kontrol.py', '27', '30').splitlines() or ['?'])[-1]
I = [x.replace('AYN_SONUC', AYN) for x in I]
import glob
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
CAK = run('/home/claude/sunum/cakisma.py', *DOS)
KYENI = set(re.findall(r"'([^']+)' '(?:[^']|'(?=[a-zâîû]))+' (?:karşılığı|açılımı)", ' '.join(MEALS)))
CAK_L = [l for l in CAK.splitlines() if any(x in l for x in ("'ashâb'", "'âxar'", "'âdem'")) or l.startswith('KÖK') or l.split(' ←')[0] in KYENI]
KARAR = {}
exec(open('/home/claude/b06/yap/karar.py', encoding='utf-8').read())
if os.path.exists('/home/claude/b10/yap/karar.py'): exec(open('/home/claude/b10/yap/karar.py', encoding='utf-8').read())
I[idx] = ("karşılık çakışması (bölüm 4 kuralı 4 — komut 'python3 sunum/cakisma.py' + sûre 5'in okunmuş bütün ARIZA dosyaları; Türkçe fiil kökü eşlemesi betikle, son dosyaya dokunan gruplar; kararlar morph LEM eşitliğine göre): "
          + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
yaz()
print('yazıldı', len(I))
print('\n'.join(CAK_L))
print(GLS); print(KUR)
