# blok 30 (5:97-100) ARIZA oluşturucu — bölüm 13-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b30/olcum.txt'
os.environ['SAY2'] = '/home/claude/b30/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {33: {6: "'ve rasûlehû'", 7: "'ve yes'avne'", 18: "'ve erculuhum'", 30: "'ve lehum fi'l-âxirati'"}, 34: {9: "'fa'lemû'"}, 35: {6: "'ve'bteğû'", 9: "'ve câhidû'"}, 36: {11: "'ve mislehû'", 22: "'ve lehum 'azâbun'"}}
BOL = "'İhramda av; Kâbe ve haram ay; elçinin görevi'"


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
 ("5:97", "''alime enne allâh'", 4, 'say 5:97 13-15', "harekesiz 'li-ta'lemû enne'llâh' (13-15. kelime)", ('dizi 5 97 13 15', "'alime enne allâh", '13-15', "biçim farkı (dizi 5 97 13 15): basılmamış eş önek; basılmamış eş fiil çekimi, zamir eki, önek; 5:98 önek")),
 ("5:97", "'allâh 'alime mâ'", 2, 'say 5:97 15-17', "harekesiz 'llâhe ya'lemu mâ' (15-17. kelime)", ('dizi 5 97 15 17', "allâh 'alime mâ", '15-17', "biçim farkı (dizi 5 97 15 17): 5:99 i'râb, önek")),
 ("5:97", "''alime mâ fî'", 2, 'say 5:97 16-18', "harekesiz 'ya'lemu mâ fî' (16-18. kelime)", ('dizi 5 97 16 18', "'alime mâ fî", '16-18', "biçim farkı (dizi 5 97 16 18): basılmamış eş fiil çekimi")),
 ("5:97", "'mâ fî ard'", 2, 'say 5:97 20-22 --on', "önek kesilmiş 've mâ fi'l-ard' (20-22. kelime)", ('dizi 5 97 20 22', "mâ fî ard", '20-22', "biçim farkı (dizi 5 97 20 22): basılmamış eş önek")),
 ("5:98", "''alime enne allâh'", 4, 'say 5:98 1-3', "harekesiz 'i'lemû enne'llâh' (1-3. kelime)", ('dizi 5 98 1 3', "'alime enne allâh", '1-3', "biçim farkı (dizi 5 98 1 3): basılmamış eş önek; basılmamış eş fiil çekimi, zamir eki; 5:97 önek")),
 ("5:98", "'enne allâh şedîd 'iqâb'", 2, 'say 5:98 2-5', "harekesiz 'enne'llâhe şedîdu'l-'iqâb' (2-5. kelime; biçim öğesi — ölçüm kalıbı 'ان' iskeleti 'inne' / 'enne' birleşik; ◇ lemma dizisi 'dizi 5 98 2 5' sûre içi 1)", ('dizi 5 98 2 5', "enne allâh şedîd 'iqâb", '2-5', "nakarat3 'ان' iskeleti 'inne' / 'enne' birleştiriyor: 'enne' dizisi sûre içi 1 + 'inne' dizisi sûre içi 1 (blok 1 R5 satırı) = 2, toplam nakarat3 ile eşit; öneksiz eş koşusu (dizi 5 98 2 5): sûre içi eş yok")),
 ("5:98", "'enne allâh ğafûr rahîm'", 3, 'say 5:98 6-9 --on', "önek kesilmiş 've enne'llâhe ğafûrun rahîm' (6-9. kelime; biçim öğesi — ölçüm kalıbı 'ان' iskeleti 'inne' / 'enne' birleşik; ◇ lemma dizisi 'dizi 5 98 6 9' sûre içi 2)", ('dizi 5 98 6 9', "enne allâh ğafûr rahîm", '6-9', "nakarat3 'ان' iskeleti 'inne' / 'enne' birleştiriyor: 'enne' dizisi sûre içi 2 + 'inne' dizisi sûre içi 1 (blok 13 R5 satırı) = 3, toplam nakarat3 ile eşit; öneksiz eş koşusu (dizi 5 98 6 9): basılmamış eş → önek kesilmiş sûre içi 2")),
 ("5:98", "'allâh ğafûr rahîm'", 5, 'say 5:98 7-9', "harekesiz 'llâhe ğafûrun rahîm' (7-9. kelime)", ('dizi 5 98 7 9', "allâh ğafûr rahîm", '7-9', "biçim farkı (dizi 5 98 7 9): basılmamış eş yazım eş; basılmamış eş yazım eş; basılmamış eş yazım eş; 5:74 i'râb, önek")),
 ("5:99", "'allâh 'alime mâ'", 2, 'say 5:99 6-8 --on', "önek kesilmiş 've'llâhu ya'lemu mâ' (6-8. kelime)", ('dizi 5 99 6 8', "allâh 'alime mâ", '6-8', "biçim farkı (dizi 5 99 6 8): 5:97 i'râb, önek")),
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

K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k}

VF_YAZI = {97: {8: "'ve'ş-şehre'", 10: "'ve'l-hedye'", 11: "'ve'l-qalâ'ide'", 20: "'ve mâ'", 23: "'ve enne'"}, 98: {6: "'ve enne'"}, 99: {6: "'ve'llâhu'", 10: "'ve mâ'"}, 100: {5: "'ve't-tayyibu'", 6: "'ve lev'", 10: "'fe'ttequ'"}}
sys.path.insert(0, '/home/claude/b30/yap')
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
open('/home/claude/b30/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '30')
BLOKLAR = [str(i) for i in range(1, 31)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '30', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b30/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '97', '100', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b30/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b30/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '97', '100', '30').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_97_100.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:97', '5:98', '5:99', '5:100'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_97_100.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '5:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '5:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(97, 101))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "5:97 kök كعب ('l-ka'bete' 3. kelime — Kâbe; kök anlamı topuk / aşık kemiği): tetik listesinde yok, organ anlamında kullanılmıyor; 5:97 kök شهر ('ş-şehre' 8. kelime — ay; takvim birimi): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '97', '100', '30')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b30/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 31)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(97, 101))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: yalnız blok akışı (sunum/sinifla.py SON, sunum/basilan.txt — §3 adım 2 ve emsal işaretlemesi); denetim kuralı değişmedi; mutasyon_sina — MUT_SONUC; "
 "geriye dönük koşu son araç değişikliğinden sonra (blok 29) üretildi: GERI_P; blok 29'da sonradan değişen sunum/kural14.py geriye dönük kümede yok",
 "kök tablosu: ölçümde '???' 5:97, 5:98, 5:99 ve 5:100 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 97 100 30'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:97 ''alîm' (27. kelime) — esma_el 'ilahi', kural ''inne/enne' haberi' (lafzın haberi); 5:98 'ğafûrun' (8. kelime) ve 'rahîm' (9. kelime) — esma_el 'ilahi', kural ''inne/enne' haberi' (lafzın haberi); 5:99 ve 5:100 esmâ yok; "
 "lafız dört ayet (5:97, 5:98, 5:99, 5:100); Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 97 100 30'): " + EMH,
 "ölçüm: 5:97 '{{1|fâsıla عليم → م, N sınıfı}}', '{{1|simetri \\[4, 12, 21, 1\\]}}', '{{1|harf 119 → harf3 115, isaret 4}}' ve '{{1|dış düğüm 0}}'; "
 "5:98 '{{2|fâsıla رحيم → م, N sınıfı}}', '{{2|simetri \\[3, 2, 6, 1\\]}}', '{{2|harf 40 → harf3 37, isaret 3}}' ve '{{2|dış düğüm 2}}'; "
 "5:99 '{{3|fâsıla تكتمون → ن, N sınıfı}}', '{{3|simetri \\[3, 2, 8, 1\\]}}', '{{3|harf 45 → harf3 44, isaret 1}}' ve '{{3|dış düğüm 1}}'; "
 "5:100 '{{4|fâsıla تفلحون → ن, N sınıfı}}', '{{4|sayı işareti كَثْرَة}}', '{{4|harf 74 → harf3 71, isaret 3}}' ve '{{4|dış düğüm 1}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 97 100 30'): KALAN_P",
 "ölçüm aktör: 5:97 '{{1|adlı كَعْبَة 3\\. sırada \\(yer, rol meful\\)}}' — 'ce'ale' mef'ûlü; 5:98, 5:99 ve 5:100 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 5:97 haber — kip yok; 5:98 emir — IMPV 1 ''lemû' (1.); "
 "5:99 haber — NEG 1 'mâ' (1.), RES 1 'illâ' (4.); ölçüm biçim alanı '{{3|biçim HASR}}' (yalnız bu maddede); 5:100 emir, nida, şart — IMPV 2 'qul' (1.), 'ttequ' (10.), NEG 1 'lâ' (2.), COND 1 'lev' (6.), VOC 1 'yâ' (12.); "
 "morph REM ('ve' 5:97 23., 5:99 6.; 'fe' 5:100 10.), CIRC ('ve lev' 5:100 6.) ve PRP ('li' 5:97 13.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:97 ★ (kaynak allah, z=1,69); 5:98 ★★★ (kaynak allah, z=3,92); 5:99 ve 5:100 yıldız yok",
 "fâsıla: 5:96 ن (تحشرون) → 5:97 م (عليم) → 5:98 م (رحيم) → 5:99 ن (تكتمون) → 5:100 ن (تفلحون); kafiye م / ن arasında ikişerli gidiyor (ölçümde kafiye bayrağı yok); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6 — basılmamış hedefler sinifla sayısıyla): 5:97 xref yok; 5:98 2:196 (emsal olarak basıldı) ve henüz okunmamış 1 ayet; 5:99 24:29 (emsal olarak basıldı); 5:100 65:10 (emsal olarak basıldı)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:97 ''alime enne allâh' süzgeç GEÇER, 'mâ fî ard', 'allâh 'alime mâ' ve ''alime mâ fî' GEÇMEZ; 5:98 'enne allâh ğafûr rahîm', 'enne allâh şedîd 'iqâb', 'allâh ğafûr rahîm' ve ''alime enne allâh' GEÇER; 5:99 'allâh 'alime mâ' GEÇMEZ; 5:100 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "fail olmayan mecrur çoğul ad ve mecrur ilgi zamiri A1'de yazılmaz — bölüm 11 denetimi kuralları 16 ve 19; fiilden önce gelen lafız 'mübtedâ' — bölüm 12 denetimi kuralı 11; edilgen fiilde 'naib-i faili' — bölüm 11 denetimi kuralı 17): "
 "5:97 Allah (lafız; 'ce'ale' faili — 3MS fiil uyumu; 15. ve 24. kelimede 'enne' ismi), Kâbe (adlı yer; 'ce'ale' mef'ûlü), muhatap 2MP (adsız — 'li-ta'lemû'), 3MS (adsız — 'ya'lemu', gönderge lafız); "
 "5:98 muhatap 2MP (adsız — 'i'lemû'), Allah (lafız; 3. ve 7. kelimede 'enne' ismi); 5:99 elçi ('r-rasûli' — adlı rol), Allah (lafız; 6. kelimede mübtedâ), 3MS (adsız — 'ya'lemu'), muhatap 2MP (adsız — 'tubdûne', 'tektumûn'); "
 "5:100 muhatap 2MS (adsız — 'qul', 'a'cebeke'), 'l-xabîsu ve't-tayyib' ('yestevi' faili), 'kesratu'l-xabîs' ('a'cebeke' faili), muhatap 2MP (adsız; söz içi), Allah (lafız; 'ttequ' mef'ûlü), 'uli'l-elbâb' (nida edilen); "
 "'n-nâsi' (5:97 7. kelime; mecrur çoğul) ve 's-semâvâti' (5:97 19. kelime; mecrur çoğul) A1'de yazılmadı — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): 5:100 'qul' sözü (2-15. kelime) mealde tırnaksız (emsal biçimi), A3'te ve A4'te 'söz açılır' (bölüm 10 denetimi kuralı 8); 5:97, 5:98 ve 5:99 söz yok (A3 —); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 97 100 30' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:97 've'ş-şehre' (8.), 've'l-hedye' (10.), 've'l-qalâ'ide' (11.), 've mâ' (20.) CONJ, 've enne' (23.) REM; 5:98 've enne' (6.) CONJ; 5:99 've'llâhu' (6.) REM, 've mâ' (10.) CONJ; "
 "5:100 've't-tayyibu' (5.) CONJ, 've lev' (6.) CIRC, 'fe'ttequ' (10.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:97 ◈B أنس ('n-nâsi' 7. kelime — B1; anlam notu: Kâbe'nin ayakta duruş kılındığı insanlar); 5:97 ◈K سمو ('s-semâvâti' 19. kelime — K1; anlam notu: bilginin kapsamı, gökler); 5:97 ◈K أرض ('l-ardi' 22. kelime — K1; anlam notu: bilginin kapsamı, yer)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 97 100 30'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:98 (2:196), 5:99 (24:29), 5:100 (65:10); 5:97 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; 5:98 bağı ölçüm xref adıyla); "
 "ayetler arası kalıp 'enne'llâh' (5:97, 5:98) — lemma dizisi 'dizi 5 97 13 15' / 'dizi 5 98 1 3' (''alime enne allâh'); ayetler arası kalıp 'ya'lemu mâ' (5:97, 5:99) — lemma dizisi 'dizi 5 97 15 17' / 'dizi 5 99 6 8' ('allâh 'alime mâ'); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:97 edim geçişi emir → haber; şahıs geçişi 2 → 3; 5:98 edim geçişi haber → emir; şahıs geçişi 3 → 2; 5:99 edim geçişi emir → haber; "
 "5:100 bölüm kapanışı (bölüm 10 denetimi kuralı 2); söz açılır; edim geçişi haber → emir, nida, şart; şart → cevap ('lev' 6. kelime — cevap mahzuf)",
 "sözdizimi (okuma; morph etiketiyle): 5:97 'ce'ale … qiyâmen' — iki mef'ûllü 'kıl-' (morph PERF + ACC); 'l-beyte'l-harâme' — bedel (morph ACC); 'li-ta'lemû' — amaç (morph PRP); 'enne'llâhe ya'lemu' ve 've enne'llâhe … 'alîm' — 'enne' cümleleri (morph ACC); "
 "5:98 ''lemû enne' — emir ve 'enne' cümleleri (morph IMPV + ACC); 5:99 'mâ … illâ' — hasr (morph NEG + RES); 've'llâhu ya'lemu' — istînâf (morph REM); "
 "5:100 'qul' — söz emri (morph IMPV); 'lâ yestevî' — olumsuz (morph NEG); 've lev a'cebeke' — hâl şartı (morph CIRC + COND); 'fe'ttequ' — emir (morph REM + IMPV); 'yâ uli'l-elbâb' — nida (morph VOC); 'le'allekum tuflihûn' — umut (morph ACC)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:97 kök علم üçlemesi ('li-ta'lemû' 13., 'ya'lemu' 16., ''alîm' 27. kelime) ve kök حرم ikilemesi ('l-harâme' 5. / 9. kelime); "
 "5:98 'i'lemû enne'llâh' ile açılıyor; 5:100 kök خبث ikilemesi ('l-xabîsu' 4. / 'l-xabîsi' 9. kelime); 5:99 ve 5:97 'ya'lemu mâ' kalıbı (lemma dizisi 'allâh 'alime mâ')",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 30'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük): 'ya'lemu mâ tubdûne ve mâ tektumûn' 5:99 'açığa vurduğunuzu da gizlediğinizi de bilir' / 24:29 'açığa vurduğunuzu da gizlediğinizi de bilir' (emsal metninde) — çakışma değil; "
 "'fe'ttequ'llâhe yâ uli'l-elbâb' 5:100 'Ey akıl sahipleri, Allah'tan sakının' / 65:10 'ey akıl sahipleri, ey inananlar, Allah'tan sakının' (emsal metninde) — çakışma değil; "
 "'i'lemû enne'llâhe şedîdu'l-'iqâb' 5:98 'Bilin ki Allah'ın cezası çetindir' / 2:196 'bilin ki Allah'ın cezası çetindir' (emsal metninde) — çakışma değil",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 97 100 30'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:97 tarayıcı adayı (kök أرض, سمو; B_ta'lîl) — çıpa değil: gök / yer anması bilgi kapsamı, doğa iddiası yok (olgu=False); 5:98, 5:99 ve 5:100 tarayıcı vermedi (cipa_tarama5_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: ayet içi 5:97 ('fi's-semâvâti' / 'fi'l-ardi'), 5:98 ('şedîdu'l-'iqâbi' / 'ğafûrun rahîm'), 5:99 ('tubdûne' / 'tektumûn'), 5:100 ('l-xabîsu' / 't-tayyibu') — okuma; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök حرم 5:97'de ('l-harâme' 5. ve 9.) — bölümde 5:95 'hurum', 5:96 'hurrime' / 'hurumen' ile birlikte; kök هدي 5:95 'hedyen' ve 5:97 'l-hedye'; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 13-2 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm iki blok (29, 30); bu blok bölümü kapatıyor; başlıktaki 'Kâbe ve haram ay' 5:97, 'elçinin görevi' 5:99; bölüm sonu bağımsız denetimi bu bloktan sonra; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b30/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 97 100 30'; lem_bozuk.py 30 çıktısı): 5:99:9 'yubdiye' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 97 100 → AYN_SONUC; sunum/bolum4_kurallar.py 97 100 30 → KHATA_HEPSI; sunum/bolum5_kurallar.py 97 100 30 → B5_HEPSI; sunum/bolum6_kurallar.py 97 100 30 → B6_HEPSI; sunum/bolum7_kurallar.py 97 100 30 → B7_HEPSI; sunum/bolum8_kurallar.py 97 100 30 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 97 100 30 → B9_HEPSI; sunum/bolum10_kurallar.py 97 100 30 → B10_HEPSI; sunum/bolum11_kurallar.py 97 100 30 → B11_HEPSI; sunum/bolum12_kurallar.py 97 100 30 → B12_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 30 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; 2:196 bu oturumda daha önce basıldı (5:98 bağı); her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla (''alime', 'enne', 'allâh', 'mâ', 'fî', 'ard', 'şedîd', ''iqâb', 'ğafûr', 'rahîm'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (97, 100): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_97_100.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_b29.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    AYN = (run('/home/claude/sunum/ayn_kontrol.py', '97', '100').splitlines() or ['?'])[-1]
    KUR = run('/home/claude/sunum/bolum4_kurallar.py', '97', '100', '30').splitlines()
    KH = [l for l in KUR if l.startswith('HATA')]
    B5 = run('/home/claude/sunum/bolum5_kurallar.py', '97', '100', '30').splitlines()
    B5H = [l for l in B5 if l.startswith('HATA')]
    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '97', '100', '30', '--tazelik-yok').splitlines()
    B7 = run('/home/claude/sunum/bolum7_kurallar.py', '97', '100', '30').splitlines()
    B8 = run('/home/claude/sunum/bolum8_kurallar.py', '97', '100', '30').splitlines()
    B9 = run('/home/claude/sunum/bolum9_kurallar.py', '97', '100', '30').splitlines()
    B10 = run('/home/claude/sunum/bolum10_kurallar.py', '97', '100', '30').splitlines()
    B11 = run('/home/claude/sunum/bolum11_kurallar.py', '97', '100', '30').splitlines()
    B12 = run('/home/claude/sunum/bolum12_kurallar.py', '97', '100', '30').splitlines()
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
           'MUT_SONUC': (MUT[-1] if MUT else '?'), 'GERI_P': ' / '.join(x.lstrip('# ') for x in GERI), 'B6_ESMA': ('; '.join(l[5:] for l in B6 if 'esmâ kural' in l and l.startswith('HATA')) or 'sapma 0')}
    I_cur = list(I_HAM)
    for k, v in REP.items(): I_cur = I_cur[:len(BEK)] + [x.replace(k, v) for x in I_cur[len(BEK):]]  # bölüm 9 kuralı 9: taşınan denetim maddelerine yer tutucu değişimi uygulanmaz
    I_cur[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3, bölüm 6 kuralı 2 — komut 'python3 sunum/cakisma.py' + sûre 5'in okunmuş bütün ARIZA dosyaları; bu bloğun karşılıklarına dokunan gruplar ve son dosyaya dokunan KÖK grupları; grup başına tam bir kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
                  + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
    if I_cur == onceki: break
    onceki = list(I_cur)
yaz(I_cur)
print('yazıldı', len(I_cur), 'tur', tur)
print('\n'.join(CAK_L))
print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)
