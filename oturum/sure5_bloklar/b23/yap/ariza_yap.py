# blok 23 (5:71-74) ARIZA oluşturucu — bölüm 10-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b23/olcum.txt'
os.environ['SAY2'] = '/home/claude/b23/say2.txt'
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
 ("5:72", "'qad kefera ellezî qâle inne allâh _ mesîh ibn meryem qâle'", 2, 'say 5:72 1-11 --on', "önek kesilmiş 'le-qad kefera'llezîne qâlû inna'llâhe huve'l-mesîhu'bnu meryeme ve qâle' (1-11. kelime)", ('dizi 5 72 1 11', "qad kefera ellezî qâle inne allâh _ mesîh ibn meryem qâle", '1-11', "biçim farkı (dizi 5 72 1 11): 5:17 fiil çekimi, önek")),
 ("5:72", "'qad kefera ellezî qâle inne allâh'", 3, 'say 5:72 1-6', "harekesiz 'le-qad kefera'llezîne qâlû inna'llâh' (1-6. kelime)", None),
 ("5:72", "''abede allâh rabb rabb'", 2, 'say 5:72 15-18 --on', "önek kesilmiş ''budu'llâhe rabbî ve rabbekum' (15-18. kelime)", None),
 ("5:72", "'mesîh ibn meryem'", 3, 'say 5:72 8-10', "harekesiz 'l-mesîhu'bnu meryem' (8-10. kelime)", None),
 ("5:73", "'qad kefera ellezî qâle inne allâh'", 3, 'say 5:73 1-6', "harekesiz 'le-qad kefera'llezîne qâlû inna'llâh' (1-6. kelime)", None),
 ("5:73", "'ellezî kefera min'", 2, 'say 5:73 21-23', "harekesiz 'llezîne keferû minhum' (21-23. kelime; biçim öğesi 'minhum' — ölçüm kalıbında 'min' + 3MP zamir birleşik biçim; ◇ lemma dizisi 'dizi 5 73 21 23' sûre içi 4, 'min' + ad eşleri dahil)", None),
 ("5:74", "'allâh ğafûr rahîm'", 5, 'say 5:74 6-8 --on', "önek kesilmiş 've'llâhu ğafûrun rahîm' (6-8. kelime)", ('dizi 5 74 6 8', "allâh ğafûr rahîm", '6-8', "biçim farkı (dizi 5 74 6 8): basılmamış eş i'râb, önek; basılmamış eş i'râb, önek; basılmamış eş i'râb, önek; basılmamış eş i'râb, önek")),
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

VF_YAZI = {71: {1: "'ve hasibû'", 5: "'fe-'amû'", 6: "'ve sammû'", 13: "'ve sammû'", 16: "'ve'llâhu'"}, 72: {11: "'ve qâle'", 18: "'ve rabbekum'", 23: "'fe-qad'", 28: "'ve me'vâhu'", 30: "'ve mâ'"}, 73: {9: "'ve mâ'", 15: "'ve in'"}, 74: {1: "'fe-lâ'", 5: "'ve yestağfirûnehû'", 6: "'ve'llâhu'"}}
sys.path.insert(0, '/home/claude/b23/yap')
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
open('/home/claude/b23/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '23')
BLOKLAR = [str(i) for i in range(1, 24)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR).replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '23').replace('\n', '; ')
EMS = open('/home/claude/b23/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '71', '74', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b23/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
MFARK = [(k, n, sayim.S2[k.replace(' --medde', '')][0]) for k, (n, d) in sayim.S2.items() if '--medde' in k]
MEDF = '; '.join("%s meddeli %d / meddesiz %d" % (k.replace(' --medde', ''), m, n) for k, n, m in MFARK)
MEDF += ' — fark yok, yeni eş yok' if all(n == m for k, n, m in MFARK) else ' — FARK VAR'
GLS = run('/home/claude/sunum/gloss_tara.py', '71', '74', '23').splitlines()

_BAS = {l.strip() for l in open('/home/claude/sunum/basilan.txt', encoding='utf-8') if l.strip()}
def _numarasiz(m):
    refs = [x.strip() for x in m.group(1).split(',')]
    kal = [x for x in refs if ':'.join(x.split(':')[:2]) in _BAS]
    n = len(refs) - len(kal)
    return '(' + ', '.join(kal + (['okunmuş %d konum' % n] if n else [])) + ')'
ESL = re.sub(r'\((\d+:\d+:\d+(?:, \d+:\d+:\d+)*)\)', _numarasiz, ESL)
_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_5_71_74.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'5:71', '5:72', '5:73', '5:74'}
D3DISI = ', '.join(sorted(_U - _BAG - _ON, key=lambda x: tuple(map(int, x.split(':')))))
ANILIS = "5:71 kök عمي (''amû' 5. ve 12. kelime — körlük) ve kök صمم ('sammû' 6. ve 13. kelime — sağırlık): duyu kaybı, tetik listesinde yok; 5:72 kök نور ('n-nâru' 29. kelime — ateş) ve kök جنن ('l-cennete' 27. kelime — cennet): K listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '71', '74', '23')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b23/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 24)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b5:%d:\d+' % a_, s_) for a_ in range(71, 75))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/yasakli.sh IZIN eki (bölüm 7 kuralı 11 yasaklı sıra sayısı — 5:73 'sâlisu selâse' kök karşılığı sıra sayısı içeriyor, kök karşılığı izni emsaliyle; gloss_tara çıktısındaki ثلث karşılığı; es_lemma çıktısı oturum başında basılmamış konumları numarasız verdiği için 'bir' + iyelik karşılığının eski izni yeni biçimde), sunum/yasakli_test.txt (yeni sınama satırları; yasakli_sina tamam); ARIZA üreticisi (es_lemma çıktısında bu oturumda basılmamış konumlar sinifla mantığıyla numarasız — sızıntı kuralı; oturum başı basilan.txt boş); "
 "mutasyon_sina — MUT_SONUC; geriye dönük koşu son araç değişikliğinden sonra yeniden üretildi (GERI_P); düşen 18 — araç değişti: r5_gerekce / bolum9_kurallar (4) 16 (oturum başında basilan.txt boşaldı; R5 gerekçelerindeki basılmış eş adları 'basılmamış eş' biçimine döndü, kayıt değişmedi), kural13 (2) 2 (blok 22 've' / 'fe' etiket isabetleri); "
 "yeni 19 — bolum9_kurallar (4) 18 (bu nedenle, oturum başı basilan.txt), gloss_tara KAPSAMAYAN 1 (blok 23, 15 kelime) — tam okuma sonu listesi, kayıtlar geriye dönük yeniden yazılmadı",
 "kök tablosu: ölçümde '???' 5:71-74 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 71 74 23'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 5:71 'basîrun' (17. kelime) — esma_el 'ilahi', kural ''ve'llâhu X' kuralı' (lafzın haberi); 5:72 'ensâr' (33. kelime) — esma_el 'degil', kural 'çoğul insan göndergeli' (yardımcılar; olumsuzlanan yardımcılar); "
 "5:74 'ğafûrun' (7. kelime) ve 'rahîm' (8. kelime) — esma_el 'ilahi', kural ''ve'llâhu X' kuralı' (lafzın haberi); 5:73 esmâ yok; 5:71 've'llâhu' (16.) ve 5:74 've'llâhu' (6.)'daki 've' morph REM (kuralın tipik biçimi); "
 "lafız 5:71 (2 geçiş), 5:72 (4 geçiş), 5:73, 5:74 (2 geçiş); Rab 5:72 ('rabbî', 'rabbekum', 17. ve 18. sırada) — Rab adı (bölüm 6 kuralı 14 — betikle: B6_ESMA; emsal kayıtları 'ensâr' için 'çoğul insan göndergeli' — bu kayıt da öyle)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 71 74 23'): " + EMH,
 "ölçüm: 5:71 '{{1|fâsıla يعملون → ن, N sınıfı}}', '{{1|sayı işareti \\S+}}', '{{1|simetri \\[3, 5, 12, 1\\]}}', '{{1|harf 87 → harf3 78, isaret 9}}' ve '{{1|dış düğüm 0}}'; "
 "5:72 '{{2|fâsıla أنصار → ر, R sınıfı — KAFİYE KIRILMASI}}', '{{2|simetri \\[3, 1, 5, 1\\]}}', '{{2|İÇ düğüm 1}}', '{{2|harf 143 → harf3 136, isaret 7}}' ve '{{2|dış düğüm 2}}'; "
 "5:73 '{{3|fâsıla أليم → م, N sınıfı}}', '{{3|sayı işareti \\S+, \\S+, \\S+}}', '{{3|simetri \\[4, 1, 16, 1\\]}}', '{{3|harf 102 → harf3 94, isaret 8}}' ve '{{3|dış düğüm 3}}'; "
 "5:74 '{{4|fâsıla رحيم → م, N sınıfı}}', '{{4|harf 44 → harf3 40, isaret 4}}' ve '{{4|dış düğüm 0}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 71 74 23'): KALAN_P",
 "ölçüm aktör: 5:72 '{{2|adlı مَسِيح 8\\. sırada \\(kisi, rol fail\\+konusan\\)}}' — 'qâlû' sözünde lafzın haberi (okuma; ölçüm rolü 'fail+konusan'), '{{2|adlı مَرْيَم 10\\. sırada \\(kisi, rol mecrur\\)}}' — 'bnu' muzâfun ileyhi, "
 "'{{2|adlı مَسِيح 12\\. sırada \\(kisi, rol fail\\+konusan\\)}}' — 'qâle' faili ve söz sahibi, '{{2|adlı إِسْرائِيل 14\\. sırada \\(kavim, rol mecrur\\)}}' — nida edilen 'benî' muzâfun ileyhi, '{{2|adlı \\S+ 27\\. sırada \\(yer, rol meful\\)}}' — 'harrama' mef'ûlü; 5:71, 5:73 ve 5:74 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle): 5:71 haber — NEG 1 'lâ' (2.); 5:72 emir, nida, şart — CERT 2 'qad' (1., 23.), COND 1 'men' (20.), EMPH 1 'le' (1.), IMPV 1 ''budu' (15.), NEG 1 'mâ' (30.), VOC 1 'yâ' (13.); "
 "5:73 şart — CERT 1 'qad' (1.), COND 1 'in' (15.), EMPH 3 'le' (1.), 'le' ve te'kid nûnu (20.), NEG 2 'mâ' (9.), 'lem' (16.), RES 1 'illâ' (12.), biçim HASR; 5:74 soru — INTG 1 'e' (1.), NEG 1 'lâ' (1.); morph SUP 'fe' (5:74 1.) ve CAUS 'fe' (5:71 5.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 5:71 ★ (kaynak allah, z=1,58); 5:72 ★★ (kaynak n, z=2,19; eşiği geçen başka: allah z=1,90; kafiye kırığı); 5:74 ★★★ (kaynak allah, z=4,47); 5:73 yıldız yok",
 "fâsıla: 5:71 ن (يعملون) → 5:72 ر (أنصار) → 5:73 م (أليم) → 5:74 م (رحيم); kafiye kırığı 5:72 (ölçüm 'KAFİYE KIRILMASI'); 5:73 ve 5:74 kapanışı م; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref: 5:72 5:17 (emsal olarak basıldı) ve okunmuş başka ayetler; 5:73 9:90 (emsal olarak basıldı) ve okunmuş başka ayetler; 5:71 ve 5:74 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, joker '_' ile; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 5:72 'qad kefera ellezî qâle inne allâh _ mesîh ibn meryem qâle', 'qad kefera ellezî qâle inne allâh', ''abede allâh rabb rabb' ve 'mesîh ibn meryem' süzgeç GEÇER; "
 "5:73 'qad kefera ellezî qâle inne allâh' GEÇER, 'ellezî kefera min' GEÇMEZ; 5:74 'allâh ğafûr rahîm' GEÇER; 5:71 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş): "
 "5:71 3MP (adsız — 'hasibû', ''amû', 'sammû', 'ya'melûn' failleri; ''aleyhim', 'minhum'), 'fitnetun' ('tekûne' faili — 3FS fiil uyumu), Allah (lafız; 'tâba' faili — 3MS fiil uyumu), 'kesîrun' (bedel); "
 "5:72 'llezîne qâlû' ('kefera' faili — 3MS fiil uyumu), 3MP (adsız — 'qâlû' faili), Allah (lafız), 'huve' ve 'innehû' 3MS (adsız; fasıl / şe'n zamiri), Mesih ve Meryem (adlı kişiler), 'l-mesîhu' ('qâle' faili — 3MS fiil uyumu), İsrâiloğulları (nida edilen; adlı kavim), muhatap 2MP ve konuşan 1S (adsız; söz içi), Rab, 'men' (şart), 3MS (adsız — 'yuşrik' faili; ''aleyhi', 'me'vâhu'), 'l-cennete' (adlı yer); "
 "'li'z-zâlimîne' (li + belirli çoğul, mecrur) ve 'ensâr' (min + nekre çoğul, mecrur; olumsuz isim cümlesinin mübtedası) A1'de yazılmadı — mecrur çoğul ölçütü; "
 "5:73 'llezîne qâlû' ('kefera' faili — 3MS fiil uyumu), 3MP (adsız — 'qâlû', 'yentehû', 'yeqûlûne', 'keferû' failleri; 'minhum'), Allah (lafız; söz içi), ''azâbun' ('yemessenne' faili — 3MS fiil uyumu), 'llezîne keferû' ('yemessenne' mef'ûlü); 'ilâhin' (min + nekre, mecrur) A1'de yazılmadı; "
 "5:74 3MP (adsız — 'yetûbûne', 'yestağfirûnehû' failleri), 3MS (adsız — 'yestağfirûnehû' mef'ûlü; gönderge lafız), Allah (lafız) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1): 5:72 'qâlû' sözü (A3, 5-10. kelime) ve 'qâle' sözü (A3, 13-29. kelime) — 30. kelimedeki morph REM 've' tırnağı kapatır ('ve mâ li'z-zâlimîne min ensâr' söz dışında okundu); 5:73 'qâlû' sözü (A3, 5-8. kelime); 5:71 ve 5:74 söz yok; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 71 74 23' — A3 aralığında morph REM): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 5:71 've hasibû' (1.), 've sammû' (6., 13.) CONJ, 'fe-'amû' (5.) CAUS, 've'llâhu' (16.) REM; 5:72 've qâle' (11.), 've mâ' (30.) REM, 've rabbekum' (18.) CONJ, 've me'vâhu' (28.) CIRC, 'fe-qad' (23.) RSLT; "
 "5:73 've mâ' (9.), 've in' (15.) REM; 5:74 'fe-lâ' (1.) SUP, 've yestağfirûnehû' (5.) CONJ, 've'llâhu' (6.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 5:71 ◈B بصر ('basîrun' 17. kelime — B3; anlam notu: 'basîr' sıfat, lafzın haberi — duyu organı değil); 5:72, 5:73 ve 5:74 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 71 74 23'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 5:71 (2:96), 5:72 (5:17, 3:192), 5:73 (9:90) (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde ya da ölçüm xref satırında emsali buluyor — bölüm 9 kuralı 3); 5:74 D3 eşi yok; "
 "ayetler arası kalıp 'le-qad kefera'llezîne qâlû inna'llâh' (5:72, 5:73) — sayım 'say 5:73 1-6'; blok içi tekrar (bölüm 9 kuralı 6), ardışık bağ yerine sayımla kayıt; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7 — betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 5:71 — (edim haber, baskın şahıs 3; geçiş yok); 5:72 edim geçişi haber → emir, nida, şart; şahıs geçişi yok; söz açılır / kapanır (5-10. ve 13-29. kelime); şart → cevap ('men' 20. kelime); "
 "5:73 edim geçişi emir, nida, şart → şart; şahıs geçişi yok; söz açılır / kapanır (5-8. kelime); şart → cevap ('in' 15. kelime); 5:74 edim geçişi şart → soru; şahıs geçişi yok",
 "sözdizimi (okuma; morph etiketiyle): 5:71 'ellâ tekûne fitnetun' — 'en' masdar cümlesi, 'hasibû' mef'ûlü (morph SUB + NEG); 'fe-'amû' — sonuç (morph CAUS); 'kesîrun minhum' — ''amû ve sammû' zamirinden bedel (okuma); 've'llâhu basîrun' — istînâf (morph REM); "
 "5:72 'inna'llâhe huve'l-mesîhu' — 'inne' haberi, 'huve' fasıl zamiri (morph ACC); 've qâle'l-mesîh' — istînâf (morph REM); 'yâ benî isrâ'île' — nida (morph VOC); 'innehû men yuşrik' — şe'n zamiri ve şart (morph ACC + COND); 'fe-qad harrama' — şart cevabı (morph RSLT + CERT); 've me'vâhu'n-nâru' — hâl (morph CIRC); 've mâ li'z-zâlimîne min ensâr' — olumsuz isim cümlesi, 'min' istiğrak (morph REM + NEG); "
 "5:73 'mâ min ilâhin illâ ilâhun vâhidun' — olumsuzluk ve istisna ile hasr (morph NEG + RES; ölçüm biçim HASR); 'in lem yentehû' — şart (morph COND + NEG); 'le-yemessenne' — kasem cevabı (morph EMPH ×2), şart cevabı mahzuf, kasem cevabıyla anlaşılıyor (okuma); "
 "5:74 'e-fe-lâ yetûbûne' — olumsuz soru, teşvik (morph INTG + SUP + NEG); 've'llâhu ğafûrun rahîm' — istînâf (morph REM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 5:71 kök عمي ve صمم ikilemesi ''amû' / 'sammû' — 5., 6. ve 12., 13. kelimede, araya 'summe tâba'llâhu 'aleyhim' giriyor; "
 "5:72 ve 5:73 'le-qad kefera'llezîne qâlû inna'llâh' ile açılıyor — 5:17 açılışıyla eş; 5:72 kök مسح ikilemesi 'l-mesîhu' (8., 12. kelime) — Mesih hakkında söz ve Mesih'in sözü; 5:73 kök ثلث ikilemesi 'sâlisu selâsetin' ve kök أله ikilemesi 'ilâhin' / 'ilâhun'; "
 "5:74 kök غفر ikilemesi 'yestağfirûnehû' / 'ğafûrun'",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 23'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + "'; çıktı aynen, yalnız bu oturumda basılmamış konumlar sinifla mantığıyla numarasız — sızıntı kuralı): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp): 've'llâhu basîrun bi-mâ ya'melûn' 5:71 'Allah yaptıklarını görendir' / 2:96 'Allah yaptıklarını görendir' (emsal metninde) — çakışma değil; "
 "'le-qad kefera'llezîne qâlû inna'llâh' 5:72 'Andolsun, … diyenler inkâr etmiştir' / 5:17 'Andolsun, … diyenler inkâr etmiştir' (emsal metninde) — çakışma değil; 've mâ li'z-zâlimîne min ensâr' 5:72 'Zalimler için yardımcılardan hiçbiri yoktur' / 3:192 'zalimler için yardımcılardan hiçbiri yoktur' (emsal metninde) — çakışma değil; "
 "'llezîne keferû minhum' 5:73 'onlardan inkâr edenlere' / 9:90 'Onlardan inkâr edenlere' (emsal metninde) — çakışma değil; teslis sözündeki 'sâlis' / 'selâse' karşılığı sıra sayısı ve sayı + tamlayan eki (kök karşılığı — yasakli.sh IZIN, öz denetim maddesinde)",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle): " + (MKK or 'yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 71 74 23'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 5:72 tarayıcı adayı (kök نور; A_şart) — çıpa değil: 'n-nâru' şartlı hükümde ahiret barınağı, doğa iddiası yok (olgu=False); 5:73 tarayıcı adayı (A_şart, F_ölçü) — çıpa değil: sayı sözcükleri teslis sözünde, şart azap tehdidinde, doğa iddiası yok (olgu=False); 5:71 ve 5:74 tarayıcı vermedi (cipa_tarama5_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 5:71 ('fe-'amû ve sammû' / 'summe tâba'llâhu 'aleyhim'); 5:72 ('l-cennete' / 'n-nâru'); 5:73 ('sâlisu selâsetin' / 'ilâhun vâhidun'); ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök عمي ve صمم 5:71 ''amû' / 'sammû' (5., 6. ve 12., 13. kelime) — tövbe kabulünden önce ve sonra; kök ثلث 5:73 'sâlisu' / 'selâsetin' ve kök أله 'ilâhin' / 'ilâhun' — teslis sözü ve hasr; kök غفر 5:74 'yestağfirûnehû' / 'ğafûrun' — okuma",
 "bölüm: " + BOL + " bölümü, bölüm 10-2 (bölüm 7 kuralı 9 — blok_plani_5.txt'ten) — bölüm üç blok (22, 23, 24); başlıktaki 'Mesih ve teslis' 5:72 ve 5:73; "
 "mercek_kayit['5']'teki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b23/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9 — betikle: komut 'python3 sunum/bolum5_kurallar.py 71 74 23'; lem_bozuk.py 23 çıktısı): 5:71:6 'sammu' — lem_bozuk bayrağı (5:71:13 'sammû' de bu LEM); 5:72:13 'buneyy' (sunum/ham_elle.txt) — elle ham listesi; meal maddesinde '(morph LEM ham biçim)' notlu; lemma adı listesinde notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 71 74 → AYN_SONUC; sunum/bolum4_kurallar.py 71 74 23 → KHATA_HEPSI; sunum/bolum5_kurallar.py 71 74 23 → B5_HEPSI; sunum/bolum6_kurallar.py 71 74 23 → B6_HEPSI; sunum/bolum7_kurallar.py 71 74 23 → B7_HEPSI; sunum/bolum8_kurallar.py 71 74 23 → B8_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme: es_lemma numarasız çıktısındaki 'bir' + iyelik karşılığı, 'sâlisu selâse' karşılığının meal ve meal maddesindeki biçimleri ve gloss_tara ثلث satırı (tırnaklı tam biçimler; sunum/yasakli_test.txt'e üç OLUMSUZ, iki OLUMLU satır eklendi)",
 "sonradan basılan (sunum/sonradan.py --plan 23): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('hasibe', 'en', 'lâ', 'kâne', 'fitne', ''amiye', 'sammu' (morph LEM ham biçim), 'tâbe', 'allâh', ''alâ', 'kesîr', 'min', 'basîr', 'mâ', ''amile', "
 "'qad', 'kefera', 'ellezî', 'qâle', 'inne', 'mesîh', 'ibn', 'meryem', 'buneyy' (morph LEM ham biçim), 'isrâ'îl', ''abede', 'rabb', 'men', 'eşrake', 'harrame', 'cenne', 'me'vâ', 'nâr', 'zâlim', 'nasîr', "
 "'sâlis', 'selâse', 'ilâh', 'illâ', 'vâhid', 'in', 'lem', 'intehâ', ''an', 'messe', ''azâb', 'elîm', 'ilâ', 'istağfere', 'ğafûr', 'rahîm'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; 5:72 'isrâ'île 'budu'llâhe' wasl birleşimi kelime sınırında boşlukla yazıldı (kelime sayım araçları 'e'b' birleşimini bölmüyor); wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (71, 74): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_5_71_74.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_5_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_b23.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    AYN = (run('/home/claude/sunum/ayn_kontrol.py', '71', '74').splitlines() or ['?'])[-1]
    KUR = run('/home/claude/sunum/bolum4_kurallar.py', '71', '74', '23').splitlines()
    KH = [l for l in KUR if l.startswith('HATA')]
    B5 = run('/home/claude/sunum/bolum5_kurallar.py', '71', '74', '23').splitlines()
    B5H = [l for l in B5 if l.startswith('HATA')]
    B6 = run('/home/claude/sunum/bolum6_kurallar.py', '71', '74', '23', '--tazelik-yok').splitlines()
    B7 = run('/home/claude/sunum/bolum7_kurallar.py', '71', '74', '23').splitlines()
    B8 = run('/home/claude/sunum/bolum8_kurallar.py', '71', '74', '23').splitlines()
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
