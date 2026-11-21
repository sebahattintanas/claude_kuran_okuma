# sûre 6 blok 20 (6:84-90) ARIZA oluşturucu — bölüm 10-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b20/olcum.txt'
os.environ['SAY2'] = '/home/claude/b20/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b19.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {}
BOL = "'Nebiler zinciri; onların yoluna uy'"


def sd(key):
    return sayim.S2[key][1]


def sic(key):
    n, d = sayim.S2[key]
    return 1 + len([x for x in d['basilan'] if x.startswith('6:')]) + d['okunmus_si'] + d['henuz_si']


def taban(key, ay):
    n, d = sayim.S2[key]
    p = [ay] + [x for x in d['basilan'] if x.startswith('6:') and x != ay]
    if d['okunmus_si']: p.append('okunmus_si %d' % d['okunmus_si'])
    if d['henuz_si']: p.append('henuz_si %d' % d['henuz_si'])
    return ' + '.join(p)


R5 = [
 ("6:84", "'min qabl min'", 2, 'say 6:84 9-11', "harekesiz 'min qablu ve min' (9-11. kelime)", ('dizi 6 84 9 11', "min qabl min", '9-11', "biçim farkı (dizi 6 84 9 11): 6:6 zamir eki, önek")),
 ("6:87", "'ilâ sırât mustaqîm'", 2, 'say 6:87 7-9', "harekesiz 'ilâ sırâtin mustaqîm' (7-9. kelime)", None),
 ("6:88", "''an mâ kâne'", 2, 'say 6:88 13-15', "harekesiz ''anhum mâ kânû' (13-15. kelime); biçim öğesi 'kâne' çekimi (lemma dizisi sûre içi 3, nakarat3 2)", None),
 ("6:88", "'mâ kâne 'amile'", 3, 'say 6:88 14-16', "harekesiz 'mâ kânû ya'melûn' (14-16. kelime); biçim öğesi 'kâne' çekimi (lemma dizisi sûre içi 6, nakarat3 3)", None),
 ("6:89", "'ellezî âtâ kitâb'", 2, 'say 6:89 2-4', "harekesiz 'llezîne âteynâhumu'l-kitâbe' (2-4. kelime); biçim öğesi 'âtâ' çekimi (lemma dizisi sûre içi 3, nakarat3 2)", None),
]
r5 = []
for ay, kal, nk, key, ad, dz, *tr_ in R5:
    s = sic(key)
    h = "%s nakarat3 %s %d (tür %s) / %s sûre içi %d (%s)" % (ay, kal, nk, (tr_[0] if tr_ else 'ic'), ad, s, taban(key, ay))  # bölüm 11 denetimi kuralı 3
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

K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k and not (k + ' --medde' in sayim.S2 and sayim.S2[k + ' --medde'][0] != n)}  # sûre 6 bölüm 5 denetimi kuralı 6 (TEKIL_MEDDE)

VF_YAZI = {84: {1: "'ve vehebnâ'", 4: "'ve ya'qûbe'", 7: "'ve nûhan'", 11: "'ve min'", 14: "'ve suleymâne'", 15: "'ve eyyûbe'", 16: "'ve yûsufe'", 17: "'ve mûsâ'", 18: "'ve hârûne'", 19: "'ve kezâlike'"}, 85: {1: "'ve zekeriyyâ'", 2: "'ve yahyâ'", 3: "'ve 'îsâ'", 4: "'ve ilyâse'"}, 86: {1: "'ve ismâ'île'", 2: "'ve'l-yese'a'", 3: "'ve yûnuse'", 4: "'ve lûtan'", 5: "'ve kullen'"}, 87: {1: "'ve min'", 3: "'ve zurriyyâtihim'", 4: "'ve ixvânihim'", 5: "'ve'ctebeynâhum'", 6: "'ve hedeynâhum'"}, 88: {10: "'ve lev'"}, 89: {5: "'ve'l-hukme'", 6: "'ve'n-nubuvvete'"}}
sys.path.insert(0, '/home/claude/b20/yap')
from seg import meals
MEALS = meals()


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
open('/home/claude/b20/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '20')
BLOKLAR = [str(i) for i in range(1, 21)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '20', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b20/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '84', '90', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b20/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b20/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '84', '90', '20').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_84_90.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:84', '6:85', '6:86', '6:87', '6:88', '6:89', '6:90'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_84_90.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(84, 91))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:84 kök وهب ('ve vehebnâ' 1. kelime — bağışlama), kök قبل ('qablu' 10. kelime — önce): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '84', '90', '20')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b20/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 21)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(84, 91))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 9 kapanışında sunum/bolum25_kurallar.py eklendi (kural 1-5), sunum/bolum19_kurallar.py kuralı 5 tam etiket eşleşmesi, sunum/geriye_donuk.py bolum25 satırı, sunum/mutasyon_sina.py b25 sınamaları ; bu blokta: sunum/bolum5_kurallar.py kuralı 9 ('-dir' takdiri) — geniş zaman eki ('iletir' — 'ilet-' + '-ir') meal maddesinde 'X-' kökü kayıtlıysa '-dir' sayılmaz (6:88 yanlış isabet); sunum/mutasyon_sina.py — b5 kural 9 isabetsiz sınaması eklendi; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 221",
 "geriye dönük koşu (araç değişen blok — bekleyen_ariza_6_b13 elle önerisi (8) GERIYE_DONUK_ZORUNLU; komut 'python3 sunum/geriye_donuk.py b20 yamalar/geriye_donuk_6_b19k.txt'; metin ve karar kesinleştikten sonra): GERI_P; yeni sınıfı: blok 02 R5 6:6 ve blok 14 R5 6:60 gerekçeleri — bu blokta basılan 6:84 ve 6:88 r5_gerekce çıktısını değiştirdi (basılan değişti; kayıt geriye dönük yazılmaz, tam okuma sonu); blok 20 satırları (KAPSAMAYAN, ZAMİR KAYITSIZ) önceki koşuda taranmamış blok — zamir kayıtsız bekleyen yanlış pozitif sınıfı",
 "kök tablosu: ölçümde '???' 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 84 90 20'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: bu blokta esmâ yok — esma_el kaydı yok (yamalar/esma_el_6_84_90.txt boş); "
 "6:88 lafız (3. kelime); 6:90 lafız (4. kelime); Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 84 90 20'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:84 '{{1|fâsıla ٱلمحسنين → ن, N sınıfı}}', '{{1|simetri \\[6, 2, 13, 2\\]}}', '{{1|harf 103 → harf3 96, isaret 7}}' ve '{{1|dış düğüm 0}}'; 6:85 '{{2|fâsıla ٱلصلحين → ن, N sınıfı}}', '{{2|simetri \\[3, 1, 4, 1\\]}}', '{{2|harf 35 → harf3 33, isaret 2}}' ve '{{2|dış düğüm 0}}'; "
 "6:86 '{{3|fâsıla ٱلعلمين → ن, N sınıfı}}', '{{3|harf 45 → harf3 42, isaret 3}}' ve '{{3|dış düğüm 0}}'; 6:87 '{{4|fâsıla مستقيم → م, N sınıfı}}', '{{4|harf 55 → harf3 52, isaret 3}}' ve '{{4|dış düğüm 1}}'; "
 "6:88 '{{5|fâsıla يعملون → ن, N sınıfı}}', '{{5|simetri \\[3, 5, 13, 1\\]}}', '{{5|harf 64 → harf3 59, isaret 5}}' ve '{{5|dış düğüm 1}}'; 6:89 '{{6|biçim DIKKAT}}', '{{6|fâsıla بكفرين → ن, N sınıfı}}', '{{6|simetri \\[3, 1, 9, 1\\]}}', '{{6|harf 83 → harf3 79, isaret 4}}' ve '{{6|dış düğüm 2}}'; "
 "6:90 '{{7|biçim HASR}}', '{{7|fâsıla للعلمين → ن, N sınıfı}}', '{{7|simetri \\[3, 1, 12, 1\\]}}', '{{7|harf 69 → harf3 65, isaret 4}}' ve '{{7|dış düğüm 0}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "6:84 ve 6:86 ölçüm biçim alanı boş ('biçim ' — etiket yok); simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 84 90 20'): KALAN_P",
 "ölçüm aktör: 6:84 '{{1|aktör: adlı إِسْحاق 3\\. sırada.*?adlı هارُون 18\\. sırada \\(kisi, rol meful\\)}}'; 6:85 '{{2|aktör: adlı زَكَرِيّا 1\\. sırada.*?adlı إِلْياس 4\\. sırada \\(kisi, rol meful\\)}}'; 6:86 '{{3|aktör: adlı إِسْماعِيل 1\\. sırada.*?adlı لُوط 4\\. sırada \\(kisi, rol meful\\)}}'; 6:87, 6:88, 6:89 ve 6:90 aktör yok; "
 "6:84-86 adların hepsi 'rol meful' — 6:84 1. kelimedeki 'vehebnâ' ve 6. / 8. kelimedeki 'hedeynâ' fiillerinin nesnesi; 6:85 ve 6:86 adları fiilsiz atıfla 6:84 'hedeynâ' yönetiminde (okuma)",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:84 haber — kip yok; 6:85 haber — kip yok; 6:86 haber — kip yok; 6:87 haber — kip yok; 6:88 şart — COND 1 've lev' (10.), EMPH 1 'le-habita' (12.); "
 "6:89 şart — CERT 1 'fe-qad' (11.), COND 1 'fe-in' (7.); 6:90 emir — IMPV 2 'qtedih' (6.), 'qul' (7.), NEG 2 'lâ' (8.), 'in' (12.), RES 1 'illâ' (14.); "
 "morph REM ('ve' 6:88 10.; 'fe' 6:89 7.; 6:90 5.), RSLT ('fe' 6:89 11.), DEM ('zâlike' 6:88 1.; 'ulâ'ike' 6:89 1.; 6:90 1.; 'hâ'ulâ'i' 6:89 10.), ATT ('hâ' 6:89 10.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:84, 6:85, 6:86, 6:87, 6:88, 6:89 ve 6:90 yıldız yok",
 "fâsıla: 6:83 م → 6:84 ن (ٱلمحسنين) → 6:85 ن (ٱلصلحين) → 6:86 ن (ٱلعلمين) → 6:87 م (مستقيم) → 6:88 ن (يعملون) → 6:89 ن (بكفرين) → 6:90 ن (للعلمين) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:84 xref yok; 6:85 xref yok; 6:86 xref yok; 6:87 okunmuş 1 ayet; 6:88 okunmuş 1 ayet; 6:89 okunmuş 2 ayet; 6:90 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:84 'min qabl min' süzgeç GEÇMEZ; 6:87 'ilâ sırât mustaqîm' süzgeç GEÇMEZ; 6:88 'mâ kâne 'amile' süzgeç GEÇER ve ''an mâ kâne' süzgeç GEÇMEZ; 6:89 'ellezî âtâ kitâb' süzgeç GEÇMEZ; 6:85, 6:86 ve 6:90 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:84 konuşan 1P, 3MS ('lehû' — gönderge 6:83 4. kelime; 'zurriyyetihî' — gönderge 'nûhan' 7. kelime, tartışmalı); 6:85 şahıs işareti yok; 6:86 konuşan 1P; 6:87 3MP (gönderge 6:84 3. kelime), konuşan 1P; "
 "6:88 3MS ('yehdî', 'yeşâ'u', ''ibâdihî' — gönderge 'llâh' 3. kelime; 'bihî' — gönderge 'hude' 2. kelime; 'le-habita' — gönderge 'mâ' 14. kelime), 3MP (gönderge 6:84 3. kelime); "
 "6:89 3MP ('âteynâhumu' — gönderge 'ulâ'ike' 1. kelime; 'leysû' — gönderge 'qavmen' 14. kelime), konuşan 1P, 3MS ('yekfur' 8. kelime — fail 10. kelime), 3FS ('bihâ' — gönderge 'n-nubuvvete' 6. kelime, tartışmalı); "
 "6:90 3MS ('hede' 3. kelime — fail 4. kelime; ''aleyhi', 'huve' — söz içi, tartışmalı), 3MP ('hudâhumu'), muhatap 2MS ('qtedih', 'qul'), söz içi konuşan 1S ve muhatap 2MP — betik denetimi: KHATA_ADSIZ; "
 "6:84, 6:86, 6:87 ve 6:89 1P konuşan göndergesi adsız (okuma); 6:87 ve 6:88 3MP göndergesi 6:84-86 adları (okuma)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:90 'qul' (7.) ardından söz 8-16. kelime — ayet içi kapanış; 6:84, 6:85, 6:86, 6:87, 6:88 ve 6:89 söz yok; mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 84 90 20' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:84 1., 4., 7., 11., 14.-19. kelime CONJ; 6:85 1.-4. kelime CONJ; 6:86 1.-5. kelime CONJ; 6:87 1., 3.-6. kelime CONJ; 6:88 've lev' (10.) REM; 6:89 've'l-hukme' (5.), 've'n-nubuvvete' (6.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:85 ◈B حيي ('yahyâ' 2. kelime — B4; özel ad, kök morph ROOT etiketinden — ad gereği, hayat anlamı yok (okuma)); 6:84, 6:86-90 ◈K / ◈B tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 84 90 20'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 7 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:84 (21:72); 6:88 (39:23); 6:85, 6:86, 6:87, 6:89 ve 6:90 D3 eşi yok; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:84 şahıs geçişi yok, edim geçişi yok, bölüm açılışı; 6:85 şahıs geçişi 1 → —, edim geçişi yok; 6:86 şahıs geçişi — → 1, edim geçişi yok; 6:87 şahıs geçişi 1 → 3, edim geçişi yok; "
 "6:88 şart → cevap ('lev' 10. kelime / 'le-habita' 12. kelime), şahıs geçişi yok, edim geçişi haber → şart; 6:89 şart → cevap ('in' 7. kelime / 'fe-qad vekkelnâ' 11. kelime), şahıs geçişi 3 → 1, edim geçişi yok; "
 "6:90 söz açılır / kapanır (8. / 16. kelime), şahıs geçişi 1 → 3, edim geçişi şart → emir, bölüm kapanışı; ölçüm iltifât 6:84-90 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:84 'kullen hedeynâ' — nesne öne alınmış fiil cümlesi (morph INDEF ACC); 've kezâlike neczi'l-muhsinîn' — teşbih kalıbı (morph CONJ + DEM); 6:85 'kullun mine's-sâlihîn' — mübteda ve haber (morph NOM); 6:86 've kullen faddalnâ' — nesne öne alınmış fiil cümlesi; "
 "6:87 've min âbâ'ihim' — 6:84 'hedeynâ' yönetimine atıf (morph CONJ + P); 6:88 'zâlike hude'llâhi' — işaret ve haber (morph DEM); 've lev eşrakû le-habita' — 'lev' şartı, 'le' cevabı (morph REM + COND + EMPH); "
 "6:89 'ulâ'ike'llezîne' — işaret ve ilgi (morph DEM + REL); 'fe-in yekfur … fe-qad vekkelnâ' — şart ve cevap (morph REM + COND + RSLT + CERT); 6:90 'fe-bi-hudâhumu'qtedih' — câr mecrûr öne alınmış emir (morph REM + P + IMPV); 'in huve illâ' — hasr (morph NEG + RES)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:84 've vehebnâ lehû ishâqa ve ya'qûbe' — 21:72 ile eş (sayım: 'say 6:84 1-4'); 6:88 'zâlike hude'llâhi yehdî bihî men yeşâ'u' — 39:23 ile eş (sayım: 'say 6:88 1-7'); 6:84, 6:88 ve 6:90 kök هدي ikilemeleri; 6:89 kök كفر ikilemesi; 6:84-86 on sekiz özel ad",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 20'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'ve vehebnâ lehû ishâqa ve ya'qûbe' 6:84 'Ona İshâk'ı ve Ya'kûb'u bağışladık' / 21:72 'Ona İshâk'ı, üstüne fazladan Ya'kûb'u bağışladık' (emsal metninde) — çakışma — tam okuma sonu (21:72 ek kelime 'nâfileten' — 'üstüne fazladan'; fiil karşılığı 'bağışladık' bayt eşit); 'zâlike hude'llâhi' 6:88 'Bu, Allah'ın doğru yoludur' / 39:23 'Bu, Allah'ın hidâyetidir' (emsal metninde) — çakışma — tam okuma sonu ('doğru yol' / 'hidâyet'); 'yehdî bihî men yeşâ'u' 6:88 'onunla kullarından dilediğini doğru yola iletir' / 39:23 'onunla dilediğini yola iletir' (emsal metninde) — çakışma — tam okuma sonu ('doğru yola ilet-' / 'yola ilet-'; 'kullarından' 6:88 ek kelime); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:84 'vehebnâ' PERF — meal 'bağışladık'; 'hedeynâ' PERF (6. ve 8. kelime) — meal 'ilettik'; 'neczî' IMPF IND — meal 'ödüllendiririz'; "
 "6:86 'faddalnâ' PERF — meal 'üstün kıldık'; 6:87 'ictebeynâ' PERF — meal 'seçtik'; 'hedeynâ' PERF — meal 'ilettik'; 6:88 'yehdî' IMPF IND — meal 'iletir'; 'yeşâ'u' IMPF IND — meal 'dilediğini'; 'eşrakû' PERF (şart) — meal 'koşsalardı'; 'habita' PERF (cevap) — meal 'giderdi'; 'kânû' PERF — meal 'oldukları'; 'ya'melûn' IMPF IND — meal 'yapmakta'; "
 "6:89 'âteynâ' PERF — meal 'verdiğimiz'; 'yekfur' IMPF JUS (şart) — meal 'ederse'; 'vekkelnâ' PERF — meal 'kıldık'; 'leysû' PERF — meal 'etmeyen'; 6:90 'hede' PERF — meal 'ilettiği'; 'qtedih' IMPV — meal 'uy'; 'qul' IMPV — meal 'De'; 'es'elu' IMPF IND — meal 'istemiyorum'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 84 90 20'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:84, 6:85, 6:86, 6:87, 6:88, 6:89 ve 6:90 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:87 ('âbâ'ihim' / 've zurriyyâtihim'); 6:88 ('hude'llâhi' / 'eşrakû'); 6:89 ('yekfur' / 'leysû bihâ bi-kâfirîn'); 6:84, 6:85, 6:86 ve 6:90 karşıt çift yok; "
 "ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök هدي 6:84, 6:87, 6:88, 6:90; kök ذرر 6:84, 6:87; kök علم 6:86, 6:90; kök كلل 6:84, 6:85, 6:86; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 10-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm bloğu 20; bu blok bölümü açıyor ve kapatıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b20/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 84 90 20'; lem_bozuk.py 20 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 84 90 → AYN_SONUC; sunum/bolum4_kurallar.py 84 90 20 → KHATA_HEPSI; sunum/bolum5_kurallar.py 84 90 20 → B5_HEPSI; sunum/bolum6_kurallar.py 84 90 20 → B6_HEPSI; sunum/bolum7_kurallar.py 84 90 20 → B7_HEPSI; sunum/bolum8_kurallar.py 84 90 20 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 84 90 20 → B9_HEPSI; sunum/bolum10_kurallar.py 84 90 20 → B10_HEPSI; sunum/bolum11_kurallar.py 84 90 20 → B11_HEPSI; sunum/bolum12_kurallar.py 84 90 20 → B12_HEPSI; sunum/bolum13_kurallar.py 84 90 20 → B13_HEPSI; sunum/bolum14_kurallar.py 84 90 20 → B14_HEPSI; sunum/bolum15_kurallar.py 84 90 20 → B15_HEPSI; sunum/bolum16_kurallar.py 84 90 20 → B16_HEPSI; sunum/bolum17_kurallar.py 84 90 20 → B17_HEPSI; sunum/bolum18_kurallar.py 84 90 20 → B18_HEPSI; sunum/bolum19_kurallar.py 84 90 20 → B19_HEPSI; sunum/bolum20_kurallar.py 84 90 20 → B20_HEPSI; sunum/bolum21_kurallar.py 84 90 20 → B21_HEPSI; sunum/bolum22_kurallar.py 84 90 20 → B22_HEPSI; sunum/bolum23_kurallar.py 84 90 20 → B23_HEPSI; sunum/bolum24_kurallar.py 84 90 20 → B24_HEPSI; sunum/bolum25_kurallar.py 84 90 20 → B25_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 20 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('min', 'qabl', 'ilâ', 'sırât', 'mustaqîm', ''an', 'mâ', 'kâne', ''amile', 'ellezî', 'âtâ', 'kitâb'); joker kullanılmadı; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (84, 90): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_84_90.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b20.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '84', '90'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '84', '90', '20'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '84', '90', '20'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '84', '90', '20', '--tazelik-yok')}
    for _n in range(7, 26): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '84', '90', '20')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25 = [_R['B%d' % _n].splitlines() for _n in range(6, 26)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
           'MUT_SONUC': (MUT[-1] if MUT else '?'), 'GERI_P': ' / '.join(x.lstrip('# ') for x in GERI), 'B6_ESMA': ('; '.join(l[5:] for l in B6 if 'esmâ kural' in l and l.startswith('HATA')) or 'sapma 0')}
    I_cur = list(I_HAM)
    for k, v in REP.items(): I_cur = I_cur[:len(BEK)] + [x.replace(k, v) for x in I_cur[len(BEK):]]  # bölüm 9 kuralı 9: taşınan denetim maddelerine yer tutucu değişimi uygulanmaz
    I_cur[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3, bölüm 6 kuralı 2 — komut 'python3 sunum/cakisma.py' + sûre 6'nın okunmuş bütün ARIZA dosyaları; bu bloğun karşılıklarına dokunan gruplar ve son dosyaya dokunan KÖK grupları; grup başına tam bir kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
                  + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
    if I_cur == onceki: break
    onceki = list(I_cur)
yaz(I_cur)
print('yazıldı', len(I_cur), 'tur', tur)
print('\n'.join(CAK_L))
print(GLS)
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
