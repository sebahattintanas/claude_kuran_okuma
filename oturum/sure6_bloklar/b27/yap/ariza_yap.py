# sûre 6 blok 27 (6:114-117) ARIZA oluşturucu — bölüm 14-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b27/olcum.txt'
os.environ['SAY2'] = '/home/claude/b27/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b26.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {}
BOL = "'Hakem olarak Allah; üzerine Allah'ın adı anılan'"


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
 ("6:114", "'fe-lâ kâne min'", 2, 'say 6:114 20-22', "harekesiz 'fe-lâ tekûnenne mine' (20-22. kelime)", None),
 ("6:115", "'_ semî' 'alîm'", 2, 'say 6:115 9-11', "harekesiz 've huve's-semî'u'l-'alîm' (9-11. kelime)", None),
 ("6:116", "'in ittebe illâ zann in'", 2, 'say 6:116 11-15', "harekesiz 'in yettebi'ûne illa'z-zanne ve in' (11-15. kelime)", ('dizi 6 116 11 15', 'in ittebe illâ zann in', '11-15', 'biçim farkı (dizi 6 116 11 15): basılmamış eş fiil çekimi, zamir eki')),
 ("6:116", "'in ittebe illâ'", 3, 'say 6:116 11-13', "harekesiz 'in yettebi'ûne illa' (11-13. kelime)", ('dizi 6 116 11 13', 'in ittebe illâ', '11-13', 'biçim farkı (dizi 6 116 11 13): 6:50 fiil çekimi, zamir eki; basılmamış eş fiil çekimi, zamir eki')),
 ("6:117", "'inne rabb _ a'lem'", 2, 'say 6:117 1-4', "harekesiz 'inne rabbeke huve a'lemu' (1-4. kelime)", None),
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

VF_YAZI = {114: {5: "'ve huve'", 11: "'ve'llezîne'"}, 115: {1: "'ve temmet'", 5: "'ve 'adlen'", 9: "'ve huve'"}, 116: {1: "'ve in'", 15: "'ve in'"}, 117: {9: "'ve huve'"}}
sys.path.insert(0, '/home/claude/b27/yap')
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
open('/home/claude/b27/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '27')
BLOKLAR = [str(i) for i in range(1, 28)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '27', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b27/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '114', '117', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b27/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b27/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '114', '117', '27').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_114_117.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:114', '6:115', '6:116', '6:117'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_114_117.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(114, 118))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "ANILIS_YAZ"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '114', '117', '27')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b27/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 28)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(114, 118))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 13 kapanışında sunum/bolum29_kurallar.py eklendi (kural 1-5), sunum/bolum19_kurallar.py KURAL_ATIF bölüm 13, sunum/geriye_donuk.py bolum29 satırı, sunum/mutasyon_sina.py b29 sınamaları — bu blokta araç değişikliği yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 262",
 "geriye dönük koşu (bölüm 13 kapanışı, komut 'python3 sunum/geriye_donuk.py b26k yamalar/geriye_donuk_6_b24k.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 114 117 27'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:115 've huve's-semî'u'l-'alîm' (9-11. kelime) — esma_el 'ilahi', kural 'zamirin haberi' (Rab) ve 11. kelime için kural 'zamirin haberi' (Rab; işitenin sıfatı) (yamalar/esma_el_6_114_117.txt); سَمِيع ve عَلِيم lemmalarında önceki kayıtlarla karar eş ('ilahi'), gönderge ayrılığı (önceki kayıtta Allah, bu blokta Rab); 6:114, 6:116 ve 6:117 esmâ yok; "
 "6:114 lafız (2. kelime), 6:116 lafız (10. kelime); 6:114 Rab (18. kelime), 6:115 Rab (3. kelime), 6:117 Rab (2. kelime) (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 114 117 27'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 6:115 muhur EVET / muhur_el EVET / ölçüm MÜHÜR — uyuşuyor): " + EMH,
 "ölçüm: 6:114 '{{1|fâsıla ٱلممترين → ن, N sınıfı}}', '{{1|simetri \\[3, 6, 15, 1\\]}}', '{{1|harf 109 → harf3 103, isaret 6}}' ve '{{1|dış düğüm 1}}'; "
 "6:115 '{{2|esmâ سَمِيع 10\\. sırada, SON konum, MÜHÜR \\| عَلِيم 11\\. sırada, SON konum, MÜHÜR}}', '{{2|fâsıla ٱلعليم → م, N sınıfı}}', '{{2|harf 52 → harf3 47, isaret 5}}' ve '{{2|dış düğüm 2}}'; "
 "6:116 '{{3|sayı işareti أَكْثَر}}', '{{3|fâsıla يخرصون → ن, N sınıfı}}', '{{3|simetri \\[3, 4, 15, 1\\]}}', '{{3|harf 64 → harf3 63, isaret 1}}', '{{3|dış düğüm 1}}' ve '{{3|İÇ düğüm 1}}'; "
 "6:117 '{{4|fâsıla بٱلمهتدين → ن, N sınıfı}}', '{{4|simetri \\[4, 1, 7, 1\\]}}', '{{4|harf 41 → harf3 39, isaret 2}}', '{{4|dış düğüm 2}}' ve '{{4|esit2 → 68:7 oran 0,9610 kademe YAKIN}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 114 117 27'): KALAN_P",
 "ölçüm aktör: 6:114, 6:115, 6:116 ve 6:117 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:114 soru — EMPH 1 'tekûnenne' (21.), INTG 1 'e-fe-ğayra' (1.), NEG 1 'lâ' (20.); 6:115 haber — NEG 1 'lâ' (6.); "
 "6:116 şart — COND 1 'in' (1.), NEG 2 'in' (11., 15.), RES 1 'illâ' (17.), biçim HASR + ISTISNA; 6:117 haber — kip yok; "
 "morph SUP ('fe' 6:114 1.), EXP ('illâ' 6:116 13.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:115 ★ (kaynak rab, z=1,62); 6:117 ★ (kaynak rab, z=1,62); 6:114 ve 6:116 yıldız yok",
 "fâsıla: 6:113 ن → 6:114 ن (ٱلممترين) → 6:115 م (ٱلعليم) → 6:116 ن (يخرصون) → 6:117 ن (بٱلمهتدين) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:114 okunmuş 1 ayet; 6:115 okunmuş 1 ayet ve okunmamış 1 ayet; 6:116 10:66 (emsal olarak basıldı) ve okunmamış 1 ayet (sûre içi 1); 6:117 16:125 ve 68:7 (emsal olarak basıldı)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:114 'fe-lâ kâne min' süzgeç GEÇMEZ; 6:115 '_ semî' 'alîm' süzgeç GEÇMEZ; 6:116 'in ittebe illâ zann in' ve 'in ittebe illâ' süzgeç GEÇER; 6:117 'inne rabb _ a'lem' süzgeç GEÇER",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:114 konuşan 1S ('ebteğî'), 3MS ('ve huve' — gönderge 'llâhi' 2. kelime; 'enzele' — gönderge 'llezî' 6. kelime; 'ennehû' eki — gönderge 'l-kitâbe' 9. kelime), muhatap 2MP ('ileykumu'), konuşan 1P ('âteynâhumu'), 3MP ('âteynâhumu', 'ya'lemûne' — gönderge 've'llezîne' 11. kelime), muhatap 2MS ('rabbike', 'tekûnenne'); "
 "6:115 3FS ('ve temmet' — fiil uyumu, fail 2. kelime), muhatap 2MS ('rabbike'), 3MS ('li-kelimâtihî' eki, 've huve' — gönderge 'rabbike' 3. kelime); "
 "6:116 muhatap 2MS ('tuti', 'yudillûke'), 3MP ('yudillûke', 'yettebi'ûne', 'hum', 'yaxrusûn' — gönderge 'men' 4. kelime); "
 "6:117 muhatap 2MS ('rabbeke'), 3MS ('huve', 'sebîlihî' eki, 've huve' — gönderge 'rabbeke' 2. kelime; 'yedillu' — gönderge 'men' 5. kelime) — betik denetimi: KHATA_ADSIZ; "
 "edilgen: blokta edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:114, 6:115, 6:116 ve 6:117 söz yok — söz fiili yok (okuma); mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 114 117 27' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:114 've huve' (5.), 've'llezîne' (11.) REM; 6:115 've temmet' (1.), 've huve' (9.) REM, 've 'adlen' (5.) CONJ; 6:116 've in' (1.), 've in' (15.) CONJ; 6:117 've huve' (9.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:115 ◈B سمع ('s-semî'u' 10. kelime — B3; anlam notu: esmâ, işiten sıfatı; organ anlamı yok); 6:116 ◈K أرض ('l-ardi' 6. kelime — K1; anlam notu: yeryüzündeki insanlar)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 114 117 27'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:116 (10:66); 6:117 (16:125, 68:7); 6:114 ve 6:115 bağ yok; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:114 şahıs geçişi yok, edim geçişi haber → soru, bölüm açılışı; 6:115 şahıs geçişi yok, edim geçişi soru → haber; "
 "6:116 şahıs geçişi yok, edim geçişi haber → şart, şart → cevap ('in' 1. kelime); 6:117 şahıs geçişi yok, edim geçişi şart → haber; "
 "ölçüm iltifât 6:114-117 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:114 'e-fe-ğayra'llâhi ebteğî' — inkârî soru (morph INTG + SUP); 'fe-lâ tekûnenne' — pekiştirmeli olumsuz emir (morph REM + NEG, EMPH); "
 "6:115 'lâ mubeddile li-kelimâtihî' — cins nefyi (morph NEG); 've huve's-semî'u'l-'alîm' — zamir ve haber (morph REM + PRON); "
 "6:116 've in tuti' — şart ve cevabı (morph CONJ + COND); 'in yettebi'ûne illa'z-zanne' — olumsuzluk ve istisna ile hasr (morph NEG + EXP); 've in hum illâ yaxrusûn' — hasr (morph CONJ + NEG, RES); 6:117 'inne rabbeke huve a'lemu' — te'kid ve ayırma zamiri (morph ACC + PRON)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): "
 "6:116 12-18. kelime — 10:66 ile lemma dizisi eşi (sayım: 'dizi 6 116 12 18'); 6:117 1-11. kelime — 16:125 ve 68:7 ile lemma dizisi eşi (sayım: 'dizi 6 117 1 11'); 6:114 kök كتب, نزل ikilemeleri; 6:115 kök كلم ikilemesi; 6:117 kök علم ikilemesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 27'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 ""
 "'men fi'l-ard' 6:116 'Yeryüzündekiler' / 10:66 'yerde kim varsa' (emsal metninde) — çakışma — tam okuma sonu ('Yeryüzündekiler' / 'yerde kim varsa' kalıp karşılığı); 'in yettebi'ûne illa' 6:116 'Onlar ancak' / 10:66 'Onlar ancak' (emsal metninde) — çakışma değil (bayt eşit); 'yettebi'ûne' 6:116 'uyuyor' / 10:66 'uyuyor' (emsal metninde) — çakışma değil (bayt eşit); 'illa'z-zanne ve in' 6:116 'zanna uyuyor ve ancak' / 10:66 'zanna uyuyor ve ancak' (emsal metninde) — çakışma değil (bayt eşit); 've in hum illâ yaxrusûn' 6:116 've ancak tahminde bulunuyorlar' / 10:66 've ancak tahminde bulunuyorlar' (emsal metninde) — çakışma değil (bayt eşit); "
 "'inne rabbeke' 6:117 'Rabbin' / 68:7 'Rabbin' (emsal metninde) — çakışma değil (bayt eşit); 'huve a'lemu' 6:117 'en iyi bilendir' / 68:7 'en iyi bilendir' (emsal metninde) — çakışma değil (bayt eşit); ''an sebîlihî' 6:117 'yolundan' / 68:7 'yolundan' (emsal metninde) — çakışma değil (bayt eşit); 've huve a'lemu bi'l-muhtedîn' 6:117 'doğru yolu bulanları da en iyi bilendir' / 68:7 'doğru yolu bulanları da en iyi bilendir' (emsal metninde) — çakışma değil (bayt eşit); "
 "'inne rabbeke' 6:117 'Rabbin' / 16:125 'Rabbin' (emsal metninde) — çakışma değil (bayt eşit); 'huve a'lemu' 6:117 'en iyi bilendir' / 16:125 'en iyi bilendir' (emsal metninde) — çakışma değil (bayt eşit); ''an sebîlihî' 6:117 'yolundan' / 16:125 'yolundan' (emsal metninde) — çakışma değil (bayt eşit); 've huve a'lemu bi'l-muhtedîn' 6:117 'doğru yolu bulanları da en iyi bilendir' / 16:125 'doğru yolda olanları da en iyi bilendir' (emsal metninde) — çakışma — tam okuma sonu ('doğru yolu bulan' / 'doğru yolda olan' karşılığı); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:114 'ebteğî' IMPF IND (soru) — meal 'arayayım'; 'enzele' PERF — meal 'indiren'; 'âteynâ' PERF — meal 'verdiklerimiz'; 'ya'lemûne' IMPF IND — meal 'bilirler'; 'tekûnenne' IMPF IND ('lâ' ve te'kid nûnu ile) — meal 'olma'; "
 "6:115 'temmet' PERF — meal 'tamamlandı'; 6:116 'tuti' IMPF JUS (şart) — meal 'uyarsan'; 'yudillû' IMPF JUS (cevap) — meal 'saptırırlar'; 'yettebi'ûne' IMPF IND — meal 'uyuyor'; 'yaxrusûn' IMPF IND — meal 'tahminde bulunuyorlar'; "
 "6:117 'yedillu' IMPF IND — meal 'sapanı'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 114 117 27'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:116 tarayıcı adayı (kök أرض; A_şart) — çıpa değil: yeryüzü insan topluluğu anlamında, doğa iddiası yok (olgu=False); 6:114, 6:115 ve 6:117 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:117 ('yedillu' / 'l-muhtedîn'); 6:114, 6:115 ve 6:116 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök أله 6:114 ('llâhi') ve 6:116 ('llâhi'); kök علم 6:114 ('ya'lemûne'), 6:115 ('l-'alîm') ve 6:117 ('a'lemu', 'a'lemu'); kök ربب 6:114 ('rabbike'), 6:115 ('rabbike') ve 6:117 ('rabbeke'); kök ضلل 6:116 ('yudillûke') ve 6:117 ('yedillu'); kök سبل 6:116 ('sebîli') ve 6:117 ('sebîlihî'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 14-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 27 ve 28; bu blok bölümü açıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b27/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 114 117 27'; lem_bozuk.py 27 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 114 117 → AYN_SONUC; sunum/bolum4_kurallar.py 114 117 27 → KHATA_HEPSI; sunum/bolum5_kurallar.py 114 117 27 → B5_HEPSI; sunum/bolum6_kurallar.py 114 117 27 → B6_HEPSI; sunum/bolum7_kurallar.py 114 117 27 → B7_HEPSI; sunum/bolum8_kurallar.py 114 117 27 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 114 117 27 → B9_HEPSI; sunum/bolum10_kurallar.py 114 117 27 → B10_HEPSI; sunum/bolum11_kurallar.py 114 117 27 → B11_HEPSI; sunum/bolum12_kurallar.py 114 117 27 → B12_HEPSI; sunum/bolum13_kurallar.py 114 117 27 → B13_HEPSI; sunum/bolum14_kurallar.py 114 117 27 → B14_HEPSI; sunum/bolum15_kurallar.py 114 117 27 → B15_HEPSI; sunum/bolum16_kurallar.py 114 117 27 → B16_HEPSI; sunum/bolum17_kurallar.py 114 117 27 → B17_HEPSI; sunum/bolum18_kurallar.py 114 117 27 → B18_HEPSI; sunum/bolum19_kurallar.py 114 117 27 → B19_HEPSI; sunum/bolum20_kurallar.py 114 117 27 → B20_HEPSI; sunum/bolum21_kurallar.py 114 117 27 → B21_HEPSI; sunum/bolum22_kurallar.py 114 117 27 → B22_HEPSI; sunum/bolum23_kurallar.py 114 117 27 → B23_HEPSI; sunum/bolum24_kurallar.py 114 117 27 → B24_HEPSI; sunum/bolum25_kurallar.py 114 117 27 → B25_HEPSI; sunum/bolum26_kurallar.py 114 117 27 → B26_HEPSI; sunum/bolum27_kurallar.py 114 117 27 → B27_HEPSI; sunum/bolum28_kurallar.py 114 117 27 → B28_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 27 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('ellezî', 'âtâ', 'kitâb', ''alime', 'enne', 'fe-lâ', 'lâ', 'kâne', 'min', 'temme', 'kelime', 'rabb', 'semî'', ''alîm', 'in', 'ittebe', 'illâ', 'zann', 'yaxrusu' (morph LEM ham biçim), 'inne', 'a'lem', 'men', 'dalle', ''an', 'sebîl', 'muhtedî'); joker '_' lemmasız öğede ('dizi 6 115 9 11', 'dizi 6 116 11 18', 'dizi 6 117 1 4' — 'huve' / 'hum'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (114, 117): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_114_117.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b26k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '114', '117'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '114', '117', '27'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '114', '117', '27'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '114', '117', '27', '--tazelik-yok')}
    for _n in range(7, 30): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '114', '117', '27')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29 = [_R['B%d' % _n].splitlines() for _n in range(6, 30)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
