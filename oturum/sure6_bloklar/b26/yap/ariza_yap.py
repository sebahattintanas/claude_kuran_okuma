# sûre 6 blok 26 (6:109-113) ARIZA oluşturucu — bölüm 13-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b26/olcum.txt'
os.environ['SAY2'] = '/home/claude/b26/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Basiretler; yeminleri ve şeytanlar'"


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
 ("6:111", "'illâ en şâ'e'", 2, 'say 6:111 16-18', "harekesiz 'illâ en yeşâ'e' (16-18. kelime)", None),
 ("6:112", "'mâ fe'ale yezere mâ iftarâ'", 2, 'say 6:112 19-23', "harekesiz 'mâ fe'alûhu fe-zerhum ve mâ yefterûn' (19-23. kelime)", None),
 ("6:113", "'ellezî lâ âmene âxir'", 2, 'say 6:113 4-7', "harekesiz 'llezîne lâ yu'minûne bi'l-âxira' (4-7. kelime)", ('dizi 6 113 4 7', 'ellezî lâ âmene âxir', '4-7', 'biçim farkı (dizi 6 113 4 7): basılmamış eş önek')),
 ("6:113", "'ellezî lâ âmene'", 3, 'say 6:113 4-6', "harekesiz 'llezîne lâ yu'minûne' (4-6. kelime)", ('dizi 6 113 4 6', 'ellezî lâ âmene', '4-6', 'biçim farkı (dizi 6 113 4 6): basılmamış eş yazım eş; basılmamış eş önek')),
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

VF_YAZI = {109: {1: "'ve aqsemû'", 15: "'ve mâ'"}, 110: {1: "'ve nuqallibu'", 3: "'ve ebsârahum'", 10: "'ve nezeruhum'"}, 111: {1: "'ve lev'", 6: "'ve kellemehumu'", 8: "'ve haşernâ'", 20: "'ve lâkinne'"}, 112: {1: "'ve kezâlike'", 8: "'ve'l-cinni'", 16: "'ve lev'", 22: "'ve mâ'"}, 113: {1: "'ve li-tasğâ'", 8: "'ve li-yerdavhu'", 9: "'ve li-yeqterifû'"}}
sys.path.insert(0, '/home/claude/b26/yap')
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
open('/home/claude/b26/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '26')
BLOKLAR = [str(i) for i in range(1, 27)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '26', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b26/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '109', '113', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b26/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b26/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '109', '113', '26').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_109_113.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:109', '6:110', '6:111', '6:112', '6:113'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_109_113.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(109, 114))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:109 kök يمن ('eymânihim' 4. kelime — yemin), kök شعر ('yuş'irukum' 16. kelime — farkında olma), 'izâ' (18. kelime — zaman zarfı, morph T); 6:110 kök أول ('evvele' 8. kelime — başlangıç, morph T); 6:111 kök قبل ('qubulen' 12. kelime — karşı); 6:113 kök أخر ('bi'l-âxirati' 7. kelime — ahiret): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '109', '113', '26')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b26/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 27)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(109, 114))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 12 kapanışında sunum/bolum28_kurallar.py eklendi (kural 1-5), sunum/bolum19_kurallar.py KURAL_ATIF bölüm 12, sunum/geriye_donuk.py bolum28 satırı, sunum/mutasyon_sina.py b28 sınamaları — bu blokta araç değişikliği yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 256",
 "geriye dönük koşu (bölüm 12 kapanışı, komut 'python3 sunum/geriye_donuk.py b24k yamalar/geriye_donuk_6_b24.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 109 113 26'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:110 'evvele merratin' (8-9. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge; zaman zarfı) ve 6:113 'yu'minûne bi'l-âxirati' (6-7. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge) (yamalar/esma_el_6_109_113.txt); أَوَّل lemmasında 6:14:18 ve 6:94:6, آخِر lemmasında 6:32:8 ve 6:92:16 kayıtlarıyla karar eş ('degil'); 6:109, 6:111 ve 6:112 esmâ yok; "
 "6:109 lafız (2. ve 14. kelime), 6:111 lafız (19. kelime); 6:112 Rab (18. kelime); 6:110 ve 6:113 lafız ve Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 109 113 26'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 6:113 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı (muhur_el hayır, ölçümle uyuşuyor); 6:110 e_oto 1 (أَوَّل) / ölçüm esmâ yok — liste farkı): " + EMH,
 "ölçüm: 6:109 '{{1|fâsıla يؤمنون → ن, N sınıfı}}', '{{1|simetri \\[4, 5, 18, 1\\]}}', '{{1|harf 94 → harf3 90, isaret 4}}' ve '{{1|dış düğüm 2}}'; "
 "6:110 '{{2|fâsıla يعمهون → ن, N sınıfı}}', '{{2|harf 61 → harf3 58, isaret 3}}' ve '{{2|dış düğüm 1}}'; "
 "6:111 '{{3|sayı işareti أَكْثَر}}', '{{3|fâsıla يجهلون → ن, N sınıfı}}', '{{3|simetri \\[3, 1, 16, 1\\]}}', '{{3|harf 104 → harf3 99, isaret 5}}' ve '{{3|dış düğüm 1}}'; "
 "6:112 '{{4|fâsıla يفترون → ن, N sınıfı}}', '{{4|harf 99 → harf3 94, isaret 5}}' ve '{{4|dış düğüm 1}}'; "
 "6:113 '{{5|esmâ آخِر 7\\. sırada, ORTA konum, MÜHÜRSÜZ}}', '{{5|fâsıla مقترفون → ن, N sınıfı}}', '{{5|simetri \\[3, 4, 10, 1\\]}}', '{{5|harf 64 → harf3 63, isaret 1}}' ve '{{5|dış düğüm 0}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 109 113 26'): KALAN_P",
 "ölçüm aktör: 6:109, 6:110, 6:111, 6:112 ve 6:113 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:109 soru, emir, şart — COND 1 'le-in' (5.), EMPH 3 'le-in' (5.), 'le-yu'minunne' (8.), IMPV 1 'qul' (10.), INTG 1 'mâ' (15.), NEG 1 'lâ' (20.), biçim QASEM; 6:110 haber — NEG 1 'lem' (5.); "
 "6:111 şart — COND 1 've lev' (1.), NEG 1 'mâ' (13.), biçim ISTISNA ('illâ' 16.); 6:112 emir, şart — COND 1 've lev' (16.), IMPV 1 'fe-zerhum' (21.), NEG 1 'mâ' (19.); 6:113 haber — NEG 1 'lâ' (5.); "
 "morph PREV ('mâ' 6:109 11.), SUB ('mâ' 6:110 4., 'en' 6:111 17.), PRP ('li' 6:111 15.; 6:113 1., 8., 9.), EXP ('illâ' 6:111 16.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:109, 6:110, 6:111, 6:112 ve 6:113 yıldız yok",
 "fâsıla: 6:108 ن → 6:109 ن (يؤمنون) → 6:110 ن (يعمهون) → 6:111 ن (يجهلون) → 6:112 ن (يفترون) → 6:113 ن (مقترفون) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:109 35:42 (emsal olarak basıldı) ve okunmuş 1 ayet; 6:110 okunmamış 1 ayet; 6:111 okunmuş 1 ayet; 6:112 25:31 (emsal olarak basıldı); 6:113 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:109 ve 6:110 nakarat3 yok; 6:111 'illâ en şâ'e' süzgeç GEÇMEZ; 6:112 'mâ fe'ale yezere mâ iftarâ' süzgeç GEÇER; 6:113 'ellezî lâ âmene âxir' ve 'ellezî lâ âmene' süzgeç GEÇER",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:109 3MP ('ve aqsemû' — tartışmalı; 'eymânihim', 'câ'ethum', 'le-yu'minunne', 'yu'minûn' — gönderge 've aqsemû' 1. kelime), 3FS ('câ'ethum', 'câ'et' — fiil uyumu / gönderge 'âyetun' 7. kelime; 'bihâ', 'ennehâ' — gönderge 'âyetun' 7. kelime), muhatap 2MS ('qul'), 3MS ('yuş'irukum' — fiil uyumu, fail 15. kelime), muhatap 2MP ('yuş'irukum'); "
 "6:110 konuşan 1P ('ve nuqallibu', 've nezeruhum'), 3MP ('ef'idetehum', 've ebsârahum', 'yu'minû', 've nezeruhum', 'tuğyânihim', 'ya'mehûn' — gönderge 6:109 1. kelime), 3MS ('bihî' — gönderge 6:109 7. kelime, tartışmalı); "
 "6:111 konuşan 1P ('ennenâ', 'nezzelnâ', 've haşernâ'), 3MP ('ileyhimu', 've kellemehumu' eki, ''aleyhim', 'kânû', 'li-yu'minû', 'ekserehum', 'yechelûn' — gönderge 6:109 1. kelime), 3MS ('ve kellemehumu' — fiil uyumu, fail 7. kelime; 'yeşâ'e' — fiil uyumu, fail 19. kelime); "
 "6:112 konuşan 1P ('ce'alnâ'), 3MS ('yûhî' — fiil uyumu, fail 10. kelime; 'şâ'e' — fiil uyumu, fail 18. kelime; 'fe'alûhu' eki — gönderge 'zuxrufe' 13. kelime, tartışmalı), 3MP ('ba'duhum', 'fe'alûhu', 'fe-zerhum', 'yefterûn' — gönderge 'şeyâtîne' 6. kelime), muhatap 2MS ('rabbuke', 'fe-zerhum'); "
 "6:113 3FS ('li-tasğâ' — fiil uyumu, fail 3. kelime), 3MS ('ileyhi', 've li-yerdavhu' eki — gönderge 6:112 13. kelime, tartışmalı), 3MP ('yu'minûne', 've li-yerdavhu', 've li-yeqterifû', 'hum' — gönderge 'llezîne' 4. kelime) — betik denetimi: KHATA_ADSIZ; "
 "edilgen: blokta edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:109 'qul' (10.) ardından söz 11-14. kelime ('innemâ'l-âyâtu 'inde'llâh') — ayet içi kapanış; 6:110, 6:111, 6:112 ve 6:113 söz yok — söz fiili yok (okuma); mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 109 113 26' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:109 've aqsemû' (1.) REM, 've mâ' (15.) CONJ; 6:110 've nuqallibu' (1.), 've ebsârahum' (3.), 've nezeruhum' (10.) CONJ; 6:111 've lev' (1.) REM, 've kellemehumu' (6.), 've haşernâ' (8.), 've lâkinne' (20.) CONJ; 6:112 've kezâlike' (1.), 've'l-cinni' (8.), 've mâ' (22.) CONJ, 've lev' (16.) REM; 6:113 've li-tasğâ' (1.), 've li-yerdavhu' (8.), 've li-yeqterifû' (9.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:110 ◈B قلب ('nuqallibu' 1. kelime — B3); 6:110 ◈B بصر ('ebsârahum' 3. kelime — B3); 6:111 ◈B موت ('l-mevtâ' 7. kelime — B4); 6:112 ◈B أنس ('l-insi' 7. kelime — B1)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 109 113 26'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:109 (35:42); 6:112 (25:31); 6:110, 6:111 ve 6:113 bağ yok; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:109 söz açılır (11. kelime) / kapanır (14. kelime), şart → cevap ('in' 5. kelime), şahıs geçişi yok, edim geçişi yasak → soru, emir, şart; 6:110 şahıs geçişi yok, edim geçişi soru, emir, şart → haber; "
 "6:111 şahıs geçişi yok, edim geçişi haber → şart, şart → cevap ('lev' 1. kelime); 6:112 şahıs geçişi yok, edim geçişi şart → emir, şart, şart → cevap ('lev' 16. kelime); 6:113 şahıs geçişi yok, edim geçişi emir, şart → haber, bölüm kapanışı; "
 "ölçüm iltifât 6:109-113 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:109 'le-in câ'ethum âyetun le-yu'minunne bihâ' — kasem lâmı, şart ve pekiştirmeli cevap (morph EMPH + COND); 'innemâ'l-âyâtu 'inde'llâh' — hasr (morph ACC + PREV); 'mâ yuş'irukum' — soru (morph INTG); "
 "6:110 'kemâ lem yu'minû bihî' — teşbih ve olumsuzluk (morph P + SUB, NEG); 6:111 've lev ennenâ nezzelnâ' — 'lev' şartı ve cevabı (morph REM + COND); 'illâ en yeşâ'e'llâh' — istisna (morph EXP + SUB); "
 "6:112 've lev şâ'e rabbuke mâ fe'alûhu' — 'lev' şartı ve cevabı (morph REM + COND); 'fe-zerhum' — emir (morph REM); 6:113 've li-tasğâ', 've li-yerdavhu', 've li-yeqterifû' — amaç lâmı (morph CONJ + PRP)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:109 1-6. kelime — 35:42 ile lemma dizisi eşi (sayım: 'dizi 6 109 1 6'); 6:112 1-5. kelime — 25:31 ile lemma dizisi eşi (sayım: 'dizi 6 112 1 5'); "
 "6:109 kök أله, أمن, أيي, جيأ ikilemeleri; 6:111 kök شيأ ikilemesi; 6:112 kök بعض ikilemesi; 6:113 kök قرف ikilemesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 26'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'ve aqsemû bi'llâhi cehde eymânihim' 6:109 'Allah'a bütün güçleriyle yemin ettiler' / 35:42 'Allah'a bütün güçleriyle yemin ettiler' (emsal metninde) — çakışma değil (bayt eşit); 've kezâlike ce'alnâ li-kulli' 6:112 'Böylece her' / 25:31 'Böylece her' (emsal metninde) — çakışma değil (bayt eşit); ''aduvv' 6:112 'düşman kıldık' / 25:31 'düşman kıldık' (emsal metninde) — çakışma değil (bayt eşit); geniş kalıp 35:42 ve 25:31 ile lemma dizisi düzeyinde (fiil çekimi / zamir eki farkı); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:109 'aqsemû' PERF — meal 'yemin ettiler'; 'câ'ethum' PERF (şart) — meal 'gelirse'; 'yu'minunne' IMPF IND (pekiştirme nûnu) — meal 'inanacaklarına'; 'qul' IMPV — meal 'De'; 'yuş'iru' IMPF IND — meal 'bildirir'; 'câ'et' PERF ('izâ' ile) — meal 'geldiğinde'; 'yu'minûn' IMPF IND ('lâ' ile) — meal 'inanmayacaklarını'; "
 "6:110 'nuqallibu' IMPF IND — meal 'çeviririz'; 'yu'minû' IMPF JUS ('lem' ile) — meal 'inanmadıkları'; 'nezeruhum' IMPF IND — meal 'bırakırız'; 'ya'mehûn' IMPF IND — meal 'şaşkın dolaşır'; "
 "6:111 'nezzelnâ' PERF (şart) — meal 'indirseydik'; 'kelleme' PERF (şart) — meal 'konuşsaydı'; 'haşernâ' PERF (şart) — meal 'toplasaydık'; 'kânû' PERF ('mâ' ile) — meal 'değillerdi'; 'yu'minû' IMPF SUBJ — meal 'inanacak'; 'yeşâ'e' IMPF SUBJ ('en' ile) — meal 'dilemedikçe'; 'yechelûn' IMPF IND — meal 'bilmezler'; "
 "6:112 'ce'alnâ' PERF — meal 'kıldık'; 'yûhî' IMPF IND — meal 'fısıldar'; 'şâ'e' PERF (şart) — meal 'dileseydi'; 'fe'alûhu' PERF ('mâ' ile) — meal 'yapmazlardı'; 'fe-zerhum' IMPV — meal 'bırak'; 'yefterûn' IMPF IND — meal 'uydurduklarıyla'; "
 "6:113 'tasğâ' IMPF SUBJ — meal 'meyletsin'; 'yu'minûne' IMPF IND ('lâ' ile) — meal 'inanmayanların'; 'yerdavhu' IMPF SUBJ — meal 'hoşnut olsunlar'; 'yeqterifû' IMPF SUBJ — meal 'işlesinler'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 109 113 26'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:111 tarayıcı adayı (kök موت; A_şart, B_ta'lîl, D_yeti) — çıpa değil: farazi şart cümlesi, ölçü / mekanizma yok (olgu=False); 6:109, 6:110, 6:112 ve 6:113 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:109 ('le-yu'minunne' / 'lâ yu'minûn'); 6:112 ('l-insi' / 've'l-cinni'); 6:110, 6:111 ve 6:113 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök أله 6:109 ('llâhi', 'llâhi') ve 6:111 ('llâhu'); kök أمن 6:109 ('le-yu'minunne', 'yu'minûn'), 6:110 ('yu'minû'), 6:111 ('li-yu'minû') ve 6:113 ('yu'minûne'); kök قول 6:109 ('qul') ve 6:112 ('l-qavli'); kök فأد 6:110 ('ef'idetehum') ve 6:113 ('ef'idetu'); kök وذر 6:110 ('ve nezeruhum') ve 6:112 ('fe-zerhum'); kök كلل 6:111 ('kulle') ve 6:112 ('li-kulli'); kök شيأ 6:111 ('şey'in', 'yeşâ'e') ve 6:112 ('şâ'e'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 13-2 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 25 ve 26; bu blok bölümü kapatıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b26/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 109 113 26'; lem_bozuk.py 26 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 109 113 → AYN_SONUC; sunum/bolum4_kurallar.py 109 113 26 → KHATA_HEPSI; sunum/bolum5_kurallar.py 109 113 26 → B5_HEPSI; sunum/bolum6_kurallar.py 109 113 26 → B6_HEPSI; sunum/bolum7_kurallar.py 109 113 26 → B7_HEPSI; sunum/bolum8_kurallar.py 109 113 26 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 109 113 26 → B9_HEPSI; sunum/bolum10_kurallar.py 109 113 26 → B10_HEPSI; sunum/bolum11_kurallar.py 109 113 26 → B11_HEPSI; sunum/bolum12_kurallar.py 109 113 26 → B12_HEPSI; sunum/bolum13_kurallar.py 109 113 26 → B13_HEPSI; sunum/bolum14_kurallar.py 109 113 26 → B14_HEPSI; sunum/bolum15_kurallar.py 109 113 26 → B15_HEPSI; sunum/bolum16_kurallar.py 109 113 26 → B16_HEPSI; sunum/bolum17_kurallar.py 109 113 26 → B17_HEPSI; sunum/bolum18_kurallar.py 109 113 26 → B18_HEPSI; sunum/bolum19_kurallar.py 109 113 26 → B19_HEPSI; sunum/bolum20_kurallar.py 109 113 26 → B20_HEPSI; sunum/bolum21_kurallar.py 109 113 26 → B21_HEPSI; sunum/bolum22_kurallar.py 109 113 26 → B22_HEPSI; sunum/bolum23_kurallar.py 109 113 26 → B23_HEPSI; sunum/bolum24_kurallar.py 109 113 26 → B24_HEPSI; sunum/bolum25_kurallar.py 109 113 26 → B25_HEPSI; sunum/bolum26_kurallar.py 109 113 26 → B26_HEPSI; sunum/bolum27_kurallar.py 109 113 26 → B27_HEPSI; sunum/bolum28_kurallar.py 109 113 26 → B28_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 26 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('aqsemu' (morph LEM ham biçim), 'allâh', 'cehd', 'yemîn', 'in', 'câ'e', 'illâ', 'en', 'şâ'e', 'zâ', 'ce'ale', 'kull', 'nebiyy', ''aduvv', 'mâ', 'fe'ale', 'yezere' (morph LEM ham biçim), 'iftarâ', 'ellezî', 'lâ', 'âmene', 'âxir'); joker '_' kullanılmadı; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (109, 113): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_109_113.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b24k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '109', '113'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '109', '113', '26'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '109', '113', '26'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '109', '113', '26', '--tazelik-yok')}
    for _n in range(7, 29): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '109', '113', '26')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28 = [_R['B%d' % _n].splitlines() for _n in range(6, 29)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
