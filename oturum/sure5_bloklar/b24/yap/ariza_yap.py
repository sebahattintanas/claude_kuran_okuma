# blok 24 (5:75-77) ARIZA oluşturucu — bölüm 10-3
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b24/olcum.txt'
os.environ['SAY2'] = '/home/claude/b24/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {33: {6: "'ve rasûlehû'", 7: "'ve yes'avne'", 18: "'ve erculuhum'", 30: "'ve lehum fi'l-âxirati'"}, 34: {9: "'fa'lemû'"}, 35: {6: "'ve'bteğû'", 9: "'ve câhidû'"}, 36: {11: "'ve mislehû'", 22: "'ve lehum 'azâbun'"}}
BOL = "'Tebliğ emri; İsrâiloğullarının misakı; Mesih ve teslis'"


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
 ("5:75", "'mesîh ibn meryem'", 3, 'say 5:75 2-4', "harekesiz 'l-mesîhu'bnu meryem' (2-4. kelime)", None),
 ("5:76", "'min dûn allâh'", 2, 'say 5:76 3-5', "harekesiz 'min dûni'llâh' (3-5. kelime)", None),
 ("5:77", "'qâle ehl kitâb'", 3, 'say 5:77 1-3', "harekesiz 'qul yâ ehle'l-kitâb' (1-3. kelime)", None),
 ("5:77", "'lâ ittebe'a ehvâ''", 2, 'say 5:77 10-12 --on', "önek kesilmiş 've lâ tettebi'û ehvâ'' (10-12. kelime; biçim öğesi 'tettebi'û' — ölçüm kalıbında 2MP yasak biçimi; ◇ lemma dizisi 'dizi 5 77 10 12' sûre içi 3, başka çekim eşleri dahil)", ('dizi 5 77 10 12', "lâ ittebe'a ehvâ'", '10-12', "biçim farkı (dizi 5 77 10 12): basılmamış eş fiil çekimi, zamir eki; basılmamış eş fiil çekimi, zamir eki; öneksiz eş koşusu (dizi 5 77 10 12): basılmamış eş → önek kesilmiş sûre içi 2; basılmamış eş → önek kesilmiş sûre içi 2 — tutuyor")),
 ("5:77", "''an sevâ' sebîl'", 2, 'say 5:77 21-23', "harekesiz ''an sevâ'i's-sebîl' (21-23. kelime)", None),
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

VF_YAZI = {75: {12: "'ve ummuhû'"}, 76: {11: "'ve lâ'", 13: "'ve'llâhu'"}, 77: {10: "'ve lâ'", 18: "'ve edallû'", 20: "'ve dallû'"}}
sys.path.insert(0, '/home/claude/b24/yap')
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
open('/home/claude/b24/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '24')
BLOKLAR = [str(i) for i in range(1, 25)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR).replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '24').replace('\n', '; ')
EMS = open('/home/claude/b24/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '75', '77', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b24/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
MFARK = [(k, n, sayim.S2[k.replace(' --medde', '')][0]) for k, (n, d) in sayim.S2.items() if '--medde' in k]
MEDF = '; '.join("%s meddeli %d / meddesiz %d" % (k.replace(' --medde', ''), m, n) for k, n, m in MFARK)
MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else ' — FARK VAR'
GLS = run('/home/claude/sunum/gloss_tara.py', '75', '77', '24').splitlines()

_BAS = {l.strip() for l in open('/home/claude/sunum/basilan.txt', encoding='utf-8') if l.strip()}
def _numarasiz(m):
    refs = [x.strip() for x in m.group(1).split(',')]
    kal = [x for x in refs if ':'.join(x.split(':')[:2]) in _BAS]
    n = len(refs) - len(kal)
    return '(' + ', '.join(kal + (['okunmuş %d konum' % n] if n else [])) + ')'
def _son(e):
    m = re.match(r'(b\d+) (say|dizi|lem) (\S+)( \S+)?( \S+)?( \S+)? (\[.*\])$', e.strip())
    if not m: return e
    p = [x.strip() for x in m.groups()[2:6] if x]
    ay = p[0].split(':')[0] + ':' + p[0].split(':')[1] if ':' in p[0] else p[0] + ':' + p[1]
    return e if ay in _BAS else '%s %s numarasız %s' % (m.group(1), m.group(2), m.group(7))
SON = '; '.join(_son(e) for e in SON.split('; '))
ESL = re.sub(r'\((\d+:\d+:\d+(?:, \d+:\d+:\d+)*)\)', _numarasiz, ESL)
_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_75_77.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:75', '5:76', '5:77'}
D3DISI = ', '.join(sorted(_U - _BAG - _ON, key=lambda x: tuple(map(int, x.split(':')))))
ANILIS = "5:75 kök أكل ('ye'kulâni' 15. kelime — yeme) ve kök طعم ('t-ta'âma' 16. kelime — yemek): beslenme, tetik listesinde yok; 5:75 kök نظر ('nzur' 17. ve 23. kelime — bakma): emir, duyu tetik listesinde yok; 5:76 kök ضرر / نفع ('darran' 10., 'nef'an' 12. kelime): tetik listesinde yok; 5:75 kök خلو (\'xalet\' 8. kelime — gelip geçme) ve kök قبل (\'qablihi\' 10. kelime; 5:77 \'qablu\' 17. kelime — önce): zaman, tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '75', '77', '24')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b24/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 25)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(75, 78))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC,
 "kök tablosu: ölçümde '???' 5:75-77 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 75 77 24'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:76 's-semî'u' (15. kelime) ve 'l-'alîm' (16. kelime) — esma_el 'ilahi', kural ''ve'llâhu X' kuralı' (lafzın haberi; araya fasıl zamiri 'huve' giriyor); 5:75 ve 5:77 esmâ yok; 5:76 've'llâhu' (13.)'daki 've' morph REM (kuralın tipik biçimi); "
 "lafız 5:76 (2 geçiş); 5:75 ve 5:77 lafız yok; Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 75 77 24'): " + EMH,
 "ölçüm: 5:75 '{{1|fâsıla يؤفكون → ن, N sınıfı}}', '{{1|EDİLGEN 1/7 fiil, pas z=0,48}}', '{{1|simetri \\[3, 4, 9, 1\\]}}', '{{1|harf 103 → harf3 98, isaret 5}}' ve '{{1|dış düğüm 3}}'; "
 "5:76 '{{2|fâsıla ٱلعليم → م, N sınıfı}}', '{{2|simetri \\[4, 3, 11, 1\\]}}', '{{2|harf 61 → harf3 58, isaret 3}}' ve '{{2|dış düğüm 2}}'; "
 "5:77 '{{3|fâsıla ٱلسبيل → ل, ل sınıfı — KAFİYE KIRILMASI}}', '{{3|sayı işareti \\S+}}', '{{3|simetri \\[3, 4, 14, 1\\]}}', '{{3|İÇ düğüm 3}}', '{{3|harf 95 → harf3 88, isaret 7}}' ve '{{3|dış düğüm 6}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 75 77 24'): KALAN_P",
 "ölçüm aktör: 5:75 '{{1|adlı مَسِيح 2\\. sırada \\(kisi, rol fail\\)}}' — 'mâ … illâ' hasrında mübteda (okuma; ölçüm rolü 'fail'), '{{1|adlı مَرْيَم 4\\. sırada \\(kisi, rol mecrur\\)}}' — 'bnu' muzâfun ileyhi; 5:76 ve 5:77 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:75 soru, emir — NEG 1 'mâ' (1.), RES 1 'illâ' (5.), CERT 1 'qad' (7.), IMPV 2 'nzur' (17., 23.), INTG 1 'ennâ' (24.), biçim HASR; "
 "5:76 soru, emir — IMPV 1 'qul' (1.), INTG 1 'e' (2.), NEG 2 'lâ' (7., 11.); 5:77 emir, yasak, nida — IMPV 1 'qul' (1.), VOC 1 'yâ' (2.), PRO 2 'lâ' (4., 10.), CERT 1 'qad' (14.), biçim NEHY; 'keyfe' (5:75 18.) morph INTG etiketsiz, ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:76 ★ (kaynak allah, z=1,97); 5:77 ★ (kaynak n, z=1,12; kafiye kırığı); 5:75 yıldız yok",
 "fâsıla: 5:75 ن (يؤفكون) → 5:76 م (ٱلعليم) → 5:77 ل (ٱلسبيل); kafiye kırığı 5:77 (ölçüm 'KAFİYE KIRILMASI'); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:75 3:144 ve 4:171 (emsal olarak basıldı) ve okunmuş başka ayetler; 5:76 20:89 (emsal olarak basıldı) ve okunmuş başka ayetler; 5:77 4:171 (emsal olarak basıldı) ve okunmuş başka ayetler",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, joker '_' ile; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:75 'mesîh ibn meryem' süzgeç GEÇER; 5:76 'min dûn allâh' GEÇMEZ; 5:77 'qâle ehl kitâb' GEÇER, 'lâ ittebe'a ehvâ'' ve ''an sevâ' sebîl' GEÇMEZ",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş): "
 "5:75 Mesih ve Meryem (adlı kişiler), 'r-rusulu' ('xalet' faili — 3FS fiil uyumu), 3MS (adsız — 'qablihi', 'ummuhû'; gönderge Mesih), 3MD (adsız — 'kânâ', 'ye'kulâni'; Mesih ve annesi), muhatap 2MS (adsız — 'nzur'), konuşan 1P (adsız — 'nubeyyinu'), 3MP (adsız — 'lehumu'; 'yu'fekûn' edilgen faili); "
 "5:76 muhatap 2MS (adsız — 'qul'), muhatap 2MP (adsız; söz içi), Allah (lafız), mevsûl 'mâ' ve 'yemliku' faili 3MS (adsız), 'huve' 3MS (adsız; fasıl zamiri); "
 "5:77 muhatap 2MS (adsız — 'qul'), 'ehle'l-kitâbi' (nida edilen), muhatap 2MP (adsız; söz içi — 'teğlû' morph 2D etiketli, çoğul hitap), 'qavmin' (nekre), 3MP (adsız — 'dallû', 'edallû' failleri), 'kesîran' ('edallû' mef'ûlü) — betik denetimi: KHATA_ADSIZ; "
 "ikil zamir 5:75 3MD / 3D mealde çoğul '-ler' ile çevrildi (not)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): 5:76 ve 5:77 'qul' sözü mealde tırnaksız (emsal biçimi); 5:76 13. kelimedeki morph REM 've' — 've'llâhu huve's-semî'u'l-'alîm' istînâf; 5:75 söz yok; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 75 77 24' — A3 aralığında morph REM): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 5:75 've ummuhû' (12.) CONJ, 'summe' (22.) CONJ; 5:76 've lâ' (11.) CONJ, 've'llâhu' (13.) REM; 5:77 've lâ' (10.), 've edallû' (18.), 've dallû' (20.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:76 ◈B سمع ('s-semî'u' 15. kelime — B3; anlam notu: 'semî'' sıfat, lafzın haberi — duyu organı değil); 5:75 ve 5:77 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 75 77 24'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:75 (3:144), 5:76 (20:89), 5:77 (4:171, 5:60) (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde ya da ölçüm xref satırında emsali buluyor — bölüm 9 kuralı 3); "
 "4:171 ölçüm xref'inde 5:75 için de var ('mesîh ibn rasûl'), bağ 5:77'ye kuruldu; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7 — betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:75 edim geçişi soru → soru, emir; şahıs geçişi yok; 5:76 edim değişmiyor (soru, emir); şahıs geçişi 3 → 2; 5:77 edim geçişi soru, emir → emir, yasak, nida; şahıs geçişi 2 → 3",
 "sözdizimi (okuma; morph etiketiyle): 5:75 'me'l-mesîhu … illâ rasûlun' — olumsuzluk ve istisna ile hasr (morph NEG + RES; ölçüm biçim HASR); 'qad xalet min qablihi'r-rusulu' — 'rasûlun' sıfatı (okuma); 've ummuhû sıddîqatun' — atıf (morph CONJ); "
 "'kânâ ye'kulâni't-ta'âme' — 'kâne' + muzâri' geçmiş hikâye; 'nzur keyfe … summe'nzur ennâ' — iki emir, iki soru edatı (morph INTG 'ennâ'); 'yu'fekûn' — edilgen (ölçüm EDİLGEN 1/7); "
 "5:76 'e-ta'budûne' — soru (morph INTG); 'mâ lâ yemliku' — mevsûl ve sıla (morph REL + NEG); 'darran ve lâ nef'an' — 'lâ' tekrarlı olumsuzluk; 've'llâhu huve's-semî'u'l-'alîm' — istînâf, 'huve' fasıl zamiri (morph REM); "
 "5:77 'yâ ehle'l-kitâbi' — nida (morph VOC); 'lâ teğlû … ve lâ tettebi'û' — iki yasak (morph PRO; ölçüm biçim NEHY); 'qad dallû … ve edallû … ve dallû' — 'qavmin' sıfat cümleleri (okuma)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:75 kök رسل ikilemesi 'rasûlun' / 'r-rusulu' (6., 11. kelime) ve kök نظر ikilemesi 'nzur' (17., 23. kelime); "
 "5:76 ve 5:77 'qul' ile açılıyor; 5:77 kök ضلل üçlemesi 'dallû' / 'edallû' / 'dallû' (15., 18., 20. kelime)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 24'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + "'; çıktı aynen, yalnız bu oturumda basılmamış konumlar sinifla mantığıyla numarasız — sızıntı kuralı; bölüm kapanışı: bölümün bütün meal kayıtları dahil): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp): 'qad xalet min qablihi'r-rusul' 5:75 'ondan önce de elçiler gelip geçti' / 3:144 'ondan önce de elçiler gelip geçti' (emsal metninde) — çakışma değil; "
 "'darran ve lâ nef'an' 5:76 'ne bir zarara ne de bir faydaya güç yetiremeyen' / 20:89 'ne bir zarara ne bir faydaya gücü yetiyor' (emsal metninde) — çakışma değil (fiil karşılığı 'güç yetir-' / 'gücü yet-'; tam okuma sonu); "
 "'lâ teğlû' 5:77 'aşırı gitmeyin' / 4:171 'aşırı gitmeyin' (emsal metninde) — çakışma değil; "
 "''an sevâ'i's-sebîl' 5:77 'doğru yoldan' / 5:60 'doğru yoldan' (emsal metninde) — çakışma değil",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle): " + (MKK or 'yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 75 77 24'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:75, 5:76 ve 5:77 tarayıcı vermedi (cipa_tarama5_adaylari.json); 5:75 'kânâ ye'kulâni't-ta'âme' anlatı, doğa iddiası değil (olgu=False); L3 / L4 adayı yok",
 "aday 1039: 5:76 ('darran' / 'nef'an'); 5:75 ve 5:77 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök رسل 5:75 'rasûlun' / 'r-rusulu' — Mesih elçi, önceki elçiler; kök ضلل 5:77 'dallû' / 'edallû' / 'dallû' — sapma ve saptırma; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 10-3 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm üç blok (22, 23, 24); bu blok bölümü kapatıyor; başlıktaki 'Mesih ve teslis' 5:75'te Mesih'in elçiliği ve annesinin anılmasıyla sürüyor; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b24/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9 — betikle: komut 'python3 sunum/bolum5_kurallar.py 75 77 24'; lem_bozuk.py 24 çıktısı): 5:75:19 'beyyenu', 5:75:25 'ufike', 5:76:8 'meleket' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 75 77 → AYN_SONUC; sunum/bolum4_kurallar.py 75 77 24 → KHATA_HEPSI; sunum/bolum5_kurallar.py 75 77 24 → B5_HEPSI; sunum/bolum6_kurallar.py 75 77 24 → B6_HEPSI; sunum/bolum7_kurallar.py 75 77 24 → B7_HEPSI; sunum/bolum8_kurallar.py 75 77 24 → B8_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (sunum/sonradan.py --plan 24; bu oturumda basılmamış ayetlerin sayım anahtarları numarasız — sızıntı kuralı): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('mesîh', 'ibn', 'meryem', 'illâ', 'rasûl', 'qad', 'xalâ', 'min', 'qabl', 'umm', 'sıddîqa', 'kâne', 'ekele', 'ta'âm', 'nazara', 'keyf', 'beyyenu' (morph LEM ham biçim), 'âye', 'ennâ', 'ufike' (morph LEM ham biçim), "
 "'qâle', ''abede', 'dûn', 'allâh', 'mâ', 'lâ', 'meleket' (morph LEM ham biçim), 'darr', 'nef'', 'semî'', ''alîm', 'ehl', 'kitâb', 'teğlû', 'fî', 'dîn', 'ğayr', 'haqq', 'ittebe'a', 'ehvâ'', 'qavm', 'dalle', 'edalle', 'kesîr', ''an', 'sevâ'', 'sebîl'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (75, 77): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_75_77.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_b23.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    AYN = (run('/home/claude/sunum/ayn_kontrol.py', '75', '77').splitlines() or ['?'])[-1]
    KUR = run('/home/claude/sunum/bolum4_kurallar.py', '75', '77', '24').splitlines()
    KH = [l for l in KUR if l.startswith('HATA')]
    B5 = run('/home/claude/sunum/bolum5_kurallar.py', '75', '77', '24').splitlines()
    B5H = [l for l in B5 if l.startswith('HATA')]
    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '75', '77', '24', '--tazelik-yok').splitlines()
    B7 = run('/home/claude/sunum/bolum7_kurallar.py', '75', '77', '24').splitlines()
    B8 = run('/home/claude/sunum/bolum8_kurallar.py', '75', '77', '24').splitlines()
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
