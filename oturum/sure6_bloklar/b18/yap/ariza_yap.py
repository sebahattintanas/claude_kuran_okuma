# sûre 6 blok 18 (6:74-78) ARIZA oluşturucu — bölüm 9-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b18/olcum.txt'
os.environ['SAY2'] = '/home/claude/b18/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b17.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {}
BOL = "'İbrâhîm: yıldız, ay ve güneş'"


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
 ("6:76", "'qâle _ rabb _ efele qâle'", 2, 'say 6:76 7-12', "harekesiz 'qâle hâzâ rabbî fe-lemmâ efele qâle' (7-12. kelime)", None),
 ("6:76", "'qâle _ rabb'", 3, 'say 6:76 7-9', "harekesiz 'qâle hâzâ rabbî' (7-9. kelime)", None),
 ("6:76", "'_ efele qâle'", 3, 'say 6:76 10-12', "harekesiz 'fe-lemmâ efele qâle' (10-12. kelime)", ('dizi 6 76 10 12', "lemmâ efele qâle", '10-12', "biçim farkı (dizi 6 76 10 12): 6:77 yazım eş; 6:78 fiil çekimi")),
 ("6:77", "'qâle _ rabb _ efele qâle'", 2, 'say 6:77 5-10', "harekesiz 'qâle hâzâ rabbî fe-lemmâ efele qâle' (5-10. kelime)", None),
 ("6:77", "'qâle _ rabb'", 3, 'say 6:77 5-7', "harekesiz 'qâle hâzâ rabbî' (5-7. kelime)", None),
 ("6:77", "'_ efele qâle'", 3, 'say 6:77 8-10', "harekesiz 'fe-lemmâ efele qâle' (8-10. kelime)", ('dizi 6 77 8 10', "lemmâ efele qâle", '8-10', "biçim farkı (dizi 6 77 8 10): 6:76 yazım eş; 6:78 fiil çekimi")),
 ("6:77", "'rabb kâne _'", 2, 'say 6:77 14-16', "harekesiz 'rabbî le-ekûnenne mine' (14-16. kelime)", ('dizi 6 77 14 16', "rabb kâne min", '14-16', "biçim farkı (dizi 6 77 14 16): 6:27 fiil çekimi, i'râb, zamir eki, önek")),
 ("6:78", "'qâle _ rabb'", 3, 'say 6:78 5-7', "harekesiz 'qâle hâzâ rabbî' (5-7. kelime)", None),
 ("6:78", "'_ efele qâle'", 3, 'say 6:78 10-12', "harekesiz 'fe-lemmâ efelet qâle' (10-12. kelime)", ('dizi 6 78 10 12', "lemmâ efele qâle", '10-12', "biçim farkı (dizi 6 78 10 12): 6:76 fiil çekimi; 6:77 fiil çekimi")),
 ("6:78", "'berî' _ eşrake'", 2, 'say 6:78 15-17', "harekesiz 'berî'un mimmâ tuşrikûn' (15-17. kelime)", None),
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

VF_YAZI = {74: {1: "'ve iz'", 11: "'ve qavmeke'"}, 75: {1: "'ve kezâlike'", 6: "'ve'l-ardi'", 7: "'ve li-yekûne'"}}
sys.path.insert(0, '/home/claude/b18/yap')
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
open('/home/claude/b18/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '18')
BLOKLAR = [str(i) for i in range(1, 19)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '18', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b18/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '74', '78', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b18/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b18/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '74', '78', '18').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_74_78.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:74', '6:75', '6:76', '6:77', '6:78'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_74_78.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(74, 79))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:74 'iz' (1. kelime — morph T, zaman), kök صنم ('esnâmen' 7. kelime — put); 6:76 'fe-lemmâ' (1. kelime — morph T, zaman), 'fe-lemmâ' (10. kelime — morph T, zaman), kök جنن ('cenne' 2. kelime — örtme), kök أفل ('efele' 11. kelime — batma); 6:77 'fe-lemmâ' (1. kelime — morph T, zaman), 'fe-lemmâ' (8. kelime — morph T, zaman), kök بزغ ('bâziğan' 4. kelime — doğma), kök أفل ('efele' 9. kelime — batma); 6:78 'fe-lemmâ' (1. kelime — morph T, zaman), 'fe-lemmâ' (10. kelime — morph T, zaman), kök بزغ ('bâziğaten' 4. kelime — doğma), kök أفل ('efelet' 11. kelime — batma), kök برأ ('berî'un' 15. kelime — uzaklık): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '74', '78', '18')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b18/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 19)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(74, 79))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: araç değişmedi ise yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 207",
 "kök tablosu: ölçümde '???' 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 74 78 18'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:74 'fî dalâlin mubîn' (12-14. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge) (yamalar/esma_el_6_74_78.txt); 6:75-78 esmâ yok; "
 "lafız yok; Rab 6:76 (9. kelime), 6:77 (7. ve 14. kelime), 6:78 (7. kelime) (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 74 78 18'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 6:74 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı): " + EMH,
 "ölçüm: 6:74 '{{1|fâsıla مبين → ن, N sınıfı}}', '{{1|harf 62 → harf3 58, isaret 4}}' ve '{{1|dış düğüm 0}}'; 6:75 '{{2|fâsıla ٱلموقنين → ن, N sınıfı}}', '{{2|harf 47 → harf3 47, isaret 0}}' ve '{{2|dış düğüm 1}}'; "
 "6:76 '{{3|biçim DIKKAT}}', '{{3|simetri \\[3, 1, 8, 1\\]}}', '{{3|harf 57 → harf3 54, isaret 3}}' ve '{{3|dış düğüm 0}}'; 6:77 '{{4|biçim DIKKAT}}', '{{4|simetri \\[3, 5, 10, 1\\]}}', '{{4|harf 71 → harf3 69, isaret 2}}' ve '{{4|dış düğüm 1}}'; "
 "6:78 '{{5|biçim DIKKAT}}', '{{5|simetri \\[3, 6, 14, 1\\]}}', '{{5|harf 67 → harf3 64, isaret 3}}' ve '{{5|dış düğüm 1}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 74 78 18'): KALAN_P",
 "ölçüm aktör: 6:74 '{{1|aktör: adlı إِبْراهِيم 3\\. sırada \\(kisi, rol fail\\+konusan\\)}}' ve '{{1|adlı آزَر 5\\. sırada \\(kisi, rol mecrur\\)}}'; 6:75 '{{2|aktör: adlı إِبْراهِيم 3\\. sırada \\(kisi, rol meful\\)}}'; 6:76-78 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:74 soru — INTG 1 'e-tettexizu' (6.); 6:75 haber — kip yok; 6:76 haber — NEG 1 'lâ' (13.); "
 "6:77 şart — COND 1 'le-in' (11.), EMPH 3 'le-in' (11.), 'le-ekûnenne' (15.), NEG 1 'lem' (12.); 6:78 nida — VOC 1 'yâ qavmi' (13.); "
 "morph T ('iz' 6:74 1.; 'lemmâ' 6:76 1., 10.; 6:77 1., 8.; 6:78 1., 10.), ACC ('inne' 6:74 9.; 6:78 14.), PRP ('li' 6:75 7.), ATT ('hâ' 6:76 8.; 6:77 6.; 6:78 6., 8.), REM ('ve' 6:74 1.; 6:75 1.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:77 ★★ (kaynak rab, z=2,05); 6:74, 6:75, 6:76 ve 6:78 yıldız yok",
 "fâsıla: 6:73 ر → 6:74 ن (مبين) → 6:75 ن (ٱلموقنين) → 6:76 ن (ٱلءافلين) → 6:77 ن (ٱلضآلين) → 6:78 ن (تشركون) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:74 xref yok; 6:75 okunmamış 1 ayet; 6:76 xref yok; 6:77 okunmuş 1 ayet; 6:78 okunmuş 1 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:76 'qâle _ rabb _ efele qâle', 'qâle _ rabb' ve '_ efele qâle' süzgeç GEÇER; 6:77 'qâle _ rabb _ efele qâle', 'qâle _ rabb' ve '_ efele qâle' süzgeç GEÇER, 'rabb kâne _' GEÇMEZ; 6:78 'qâle _ rabb' ve '_ efele qâle' süzgeç GEÇER, 'berî' _ eşrake' GEÇMEZ; 6:74 ve 6:75 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:74 3MS ('qâle' 2. kelime — fail 3. kelime; 'li-ebîhi' — gönderge 'ibrâhîmu' 3. kelime), muhatap 2MS ve konuşan 1S (söz içi); 6:75 konuşan 1P, 3MS ('ve li-yekûne' — gönderge 'ibrâhîme' 3. kelime); "
 "6:76 3MS ('cenne' 2. kelime — fail 4. kelime; öbürleri gönderge 6:75 3. kelime; 'efele' — gönderge 'kevkeben' 6. kelime), konuşan 1S (söz içi); "
 "6:77 3MS ('yehdinî' 13. kelime — fail 14. kelime; 'efele' — gönderge 'l-qamera' 3. kelime), konuşan 1S (söz içi); 6:78 3FS ('efelet' — gönderge 'ş-şemse' 3. kelime), konuşan 1S ve muhatap 2MP (söz içi) — betik denetimi: KHATA_ADSIZ; "
 "tartışmalı gönderge (bekleyen_ariza_6_b15 elle önerisi (10), bekleyen_ariza_6_b17 bolum24 kuralı 4): 6:78 'hâzâ' (6. ve 8. kelime) eril işaret dişil 'ş-şemse' (3. kelime) için — 'doğan / bu görünen' anlamıyla (okuma, tam okuma sonu); "
 "6:76-78 'rabbî' (söz içi) göndergesi yıldız, ay, güneş; 6:77 14. kelime 'rabbî' — İbrâhîm'in Rabbi (okuma)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:74 söz 6-14. kelime; 6:76 söz 8-9. ve 13-15. kelime; 6:77 söz 6-7. ve 11-18. kelime; 6:78 söz 6-9. ve 13-17. kelime; 6:75 söz yok; mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 74 78 18' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:74 've iz' (1.) REM, 've qavmeke' (11.) CONJ; 6:75 've kezâlike' (1.) REM, 've'l-ardi' (6.), 've li-yekûne' (7.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:75 ◈K سمو ('s-semâvâti' 5. kelime — K1); 6:75 ◈K أرض ('l-ardi' 6. kelime — K1); 6:76 ◈K ليل ('l-leylu' 4. kelime — K1); 6:76 ◈K كوكب ('kevkeben' 6. kelime — K1); 6:77 ◈K قمر ('l-qamera' 3. kelime — K1); 6:78 ◈K شمس ('ş-şemse' 3. kelime — K1)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 74 78 18'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:74 (43:26); 6:78 (11:54); 6:75, 6:76 ve 6:77 D3 eşi yok; ayetler arası kalıp 'qâle hâzâ rabbî' (6:76, 6:77, 6:78) — lemma dizisi 'dizi 6 76 7 9' / 'dizi 6 77 5 7' / 'dizi 6 78 5 7'; ayetler arası kalıp 'fe-lemmâ efel' (6:76, 6:77, 6:78) — lemma dizisi 'dizi 6 76 10 12' / 'dizi 6 77 8 10' / 'dizi 6 78 10 12'; ayetler arası kalıp 'qâle hâzâ rabbî fe-lemmâ efele qâle' (6:76, 6:77) — lemma dizisi 'dizi 6 76 7 12' / 'dizi 6 77 5 10' (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş (6:78 'berî'un mimmâ tuşrikûn' — 6:19), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:74 söz açılır / kapanır (6. / 14. kelime), şahıs geçişi 3 → 2, edim geçişi emir → soru, bölüm açılışı; 6:75 şahıs geçişi 2 → 1, edim geçişi soru → haber; "
 "6:76 söz açılır / kapanır (8. / 9. kelime; 13. / 15. kelime), şahıs geçişi 1 → 3, edim geçişi yok; 6:77 söz açılır / kapanır (6. / 7. kelime; 11. / 18. kelime), şart → cevap ('in' 11. kelime / 'le-ekûnenne' 15. kelime), şahıs geçişi yok, edim geçişi haber → şart; "
 "6:78 söz açılır / kapanır (6. / 9. kelime; 13. / 17. kelime), şahıs geçişi yok, edim geçişi şart → nida; "
 "şahıs beraberliği 6:75 (kişi toplamı 1. şahıs 1 / 3. şahıs 1, ölçüm baskın 1 — bölüm 23 denetimi kuralı 3, sûre 6 bölüm 1 denetimi kuralı 9); ölçüm iltifât 6:74-78 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:74 've iz qâle' — zaman zarfı (morph REM + T); 'e-tettexizu' — inkâri soru (morph INTG); 'innî erâke' — tekit (morph ACC); 6:75 've kezâlike' — benzetme (morph REM + P + DEM); 've li-yekûne' — amaç lâmı (morph CONJ + PRP); "
 "6:76-78 'fe-lemmâ' — zaman şartı, cevap 'ra'â' / 'qâle' (morph CONJ + T); 6:77 'le-in lem yehdinî' — yemin lâmlı şart (morph EMPH + COND); 6:78 'yâ qavmi' — nida (morph VOC); 'innî berî'un' — tekit (morph ACC)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:74 've iz qâle ibrâhîmu li-ebîh' — 43:26 ile eş, ile açılıyor (sayım: 'say 6:74 1-4'); "
 "6:76, 6:77 ve 6:78 'qâle hâzâ rabbî' — sûre içi eş (sayım: 'say 6:76 7-9'); 6:76 ve 6:77 'fe-lemmâ efele qâle' (sayım: 'say 6:76 10-12'); 6:78 'berî'un mimmâ tuşrikûn' — 11:54 ile eş, 6:19 ile sûre içi eş (sayım: 'say 6:78 15-17'); "
 "6:76 kök أفل, قول ikilemeleri; 6:77 kök ربب, قول ikilemeleri; yıldız → ay → güneş sırası 6:76, 6:77, 6:78",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 18'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'ve iz qâle ibrâhîmu li-ebîh' 6:74 'Hani İbrâhîm babası Âzer'e demişti' / 43:26 'Hani İbrâhîm babasına ve kavmine şöyle demişti' (emsal metninde) — çakışma — tam okuma sonu ('babası … Âzer'e' bedel / 'babasına ve kavmine'; 'şöyle' takdiri); "
 "'berî'un mimmâ tuşrikûn' 6:78 'ortak koştuklarınızdan uzağım' / 11:54 'sizin ortak koştuklarınızdan uzağım' (emsal metninde) — çakışma — tam okuma sonu ('sizin' takdiri); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:74 'qâle' PERF — meal 'demişti'; 'e-tettexizu' IMPF IND (soru) — meal 'ediniyorsun'; 'erâke' IMPF IND — meal 'görüyorum'; "
 "6:75 'nurî' IMPF IND (hikâye) — meal 'gösteriyorduk'; 'li-yekûne' IMPF SUBJ — meal 'olsun diye'; 6:76 'cenne' PERF — meal 'örtünce'; 'ra'â' PERF — meal 'gördü'; 'qâle' PERF — meal 'dedi'; 'efele' PERF — meal 'Batınca'; 'uhibbu' IMPF IND — meal 'sevmem'; "
 "6:77 'ra'a' PERF — meal 'görünce'; 'efele' PERF — meal 'Batınca'; 'yehdinî' IMPF JUS (olumsuz şart) — meal 'iletmezse'; 'le-ekûnenne' IMPF IND (tekitli) — meal 'olurum'; 6:78 'ra'a' PERF — meal 'görünce'; 'efelet' PERF — meal 'Batınca'; 'tuşrikûn' IMPF IND — meal 'ortak koştuklarınızdan'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; ayetler arası kalıplar: 'qâle hâzâ rabbî' — çakışma değil (6:76, 6:77, 6:78 'Bu benim Rabbim, dedi' — bayt eşit); 'fe-lemmâ efel' — çakışma değil (6:76, 6:77, 6:78 'Batınca' — bayt eşit); 'qâle hâzâ rabbî fe-lemmâ efele qâle' — çakışma değil (6:76, 6:77 'Bu benim Rabbim, dedi. Batınca' — bayt eşit)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 74 78 18'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:74, 6:75, 6:76, 6:77 ve 6:78 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:75 ('s-semâvâti' / 've'l-ardi'); 6:76 ('ra'â kevkeben' / 'efele'); 6:77 ('bâziğan' / 'efele'); 6:78 ('bâziğaten' / 'efelet'); 6:74 karşıt çift yok; "
 "ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök أفل 6:76, 6:77, 6:78; kök بزغ 6:77 ('bâziğan'), 6:78 ('bâziğaten'); kök رأي 6:74, 6:75, 6:76, 6:77, 6:78; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 9-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 18 ve 19; bu blok bölümü açıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b18/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 74 78 18'; lem_bozuk.py 18 çıktısı): lem_bozuk bayrağı 6:75 2. kelime (أَرَيْ — 'nurî') ve 6:76 14. kelime (أَحْبَبْ — 'uhibbu'), meal kayıtlarında '(morph LEM ham biçim)' notu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 74 78 → AYN_SONUC; sunum/bolum4_kurallar.py 74 78 18 → KHATA_HEPSI; sunum/bolum5_kurallar.py 74 78 18 → B5_HEPSI; sunum/bolum6_kurallar.py 74 78 18 → B6_HEPSI; sunum/bolum7_kurallar.py 74 78 18 → B7_HEPSI; sunum/bolum8_kurallar.py 74 78 18 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 74 78 18 → B9_HEPSI; sunum/bolum10_kurallar.py 74 78 18 → B10_HEPSI; sunum/bolum11_kurallar.py 74 78 18 → B11_HEPSI; sunum/bolum12_kurallar.py 74 78 18 → B12_HEPSI; sunum/bolum13_kurallar.py 74 78 18 → B13_HEPSI; sunum/bolum14_kurallar.py 74 78 18 → B14_HEPSI; sunum/bolum15_kurallar.py 74 78 18 → B15_HEPSI; sunum/bolum16_kurallar.py 74 78 18 → B16_HEPSI; sunum/bolum17_kurallar.py 74 78 18 → B17_HEPSI; sunum/bolum18_kurallar.py 74 78 18 → B18_HEPSI; sunum/bolum19_kurallar.py 74 78 18 → B19_HEPSI; sunum/bolum20_kurallar.py 74 78 18 → B20_HEPSI; sunum/bolum21_kurallar.py 74 78 18 → B21_HEPSI; sunum/bolum22_kurallar.py 74 78 18 → B22_HEPSI; sunum/bolum23_kurallar.py 74 78 18 → B23_HEPSI; sunum/bolum24_kurallar.py 74 78 18 → B24_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 18 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('melekût', 'semâ'', 'ard', 'qâle', 'zâ', 'rabb', 'lemmâ', 'efele', 'berî'', 'mimmâ', 'eşrake', 'kâne', 'min'); joker '_' yalnız nakarat3 lemmasız öğede; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (74, 78): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_74_78.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b17k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '74', '78'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '74', '78', '18'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '74', '78', '18'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '74', '78', '18', '--tazelik-yok')}
    for _n in range(7, 25): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '74', '78', '18')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24 = [_R['B%d' % _n].splitlines() for _n in range(6, 25)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
