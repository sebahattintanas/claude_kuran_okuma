# sûre 6 blok 19 (6:79-83) ARIZA oluşturucu — bölüm 9-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b19/olcum.txt'
os.environ['SAY2'] = '/home/claude/b19/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
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
 ("6:79", "'_ _ _'", 2, 'say 6:79 9-11', "harekesiz 've mâ ene mine' (9-11. kelime)", None),
 ("6:80", "'xâfe _ eşrake'", 2, 'say 6:80 10-12', "harekesiz 'exâfu mâ tuşrikûne' (10-12. kelime)", ('dizi 6 80 10 12', "xâfe mâ eşrake", '10-12', "biçim farkı (dizi 6 80 10 12): 6:81 yazım eş")),
 ("6:80", "'_ _ şâ'e'", 2, 'say 6:80 14-16', "harekesiz 'illâ en yeşâ'e' (14-16. kelime)", None),
 ("6:80", "'rabb kull şey''", 2, 'say 6:80 20-22', "harekesiz 'rabbî kulle şey'' (20-22. kelime)", ('dizi 6 80 20 22', "rabb kull şey'", '20-22', "biçim farkı (dizi 6 80 20 22): basılmamış eş zamir eki")),
 ("6:81", "'xâfe _ eşrake'", 2, 'say 6:81 2-4', "harekesiz 'exâfu mâ eşraktum' (2-4. kelime)", ('dizi 6 81 2 4', "xâfe mâ eşrake", '2-4', "biçim farkı (dizi 6 81 2 4): 6:80 yazım eş")),
 ("6:81", "'_ eşrake _'", 2, 'say 6:81 3-5', "harekesiz 'mâ eşraktum ve lâ' (3-5. kelime)", ('dizi 6 81 3 5', "mâ eşrake lâ", '3-5', "biçim farkı (dizi 6 81 3 5): basılmamış eş fiil çekimi, zamir eki")),
 ("6:83", "'_ rabb hakîm 'alîm'", 2, 'say 6:83 11-14', "harekesiz 'inne rabbeke hakîmun 'alîm' (11-14. kelime)", None),
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

VF_YAZI = {79: {7: "'ve'l-arda'", 9: "'ve mâ'"}, 80: {1: "'ve hâccehû'", 7: "'ve qad'", 9: "'ve lâ'"}, 81: {1: "'ve keyfe'", 5: "'ve lâ'"}, 82: {3: "'ve lem'", 10: "'ve hum'"}, 83: {1: "'ve tilke'"}}
sys.path.insert(0, '/home/claude/b19/yap')
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
open('/home/claude/b19/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '19')
BLOKLAR = [str(i) for i in range(1, 20)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '19', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b19/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '79', '83', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b19/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b19/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '79', '83', '19').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_79_83.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:79', '6:80', '6:81', '6:82', '6:83'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_79_83.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(79, 84))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:79 kök وجه ('veccehtu' 2. kelime — yöneltme), kök وجه ('vechiye' 3. kelime — yüz), kök فطر ('fatara' 5. kelime — yaratma), kök حنف ('hanîfen' 8. kelime — hanîf); 6:80 kök حجج ('ve hâccehû' 1. kelime — tartışma); 6:83 kök رفع ('nerfe'u' 7. kelime — yükseltme): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '79', '83', '19')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b19/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 20)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(79, 84))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/bolum19_kurallar.py kuralı 5 (ESMA_LEMMA_BIR) — 'ilahi' kararlı esmâ lemmasında kapalı listedeki sözdizimi çerçeve etiketleri ayrık olabilir (6:83 'inne/enne' haberi / 6:18 ve 6:73 zamirin haberi — 'hakîm'; 6:13 / 6:83 — ''alîm'), 'degil' kararlı ya da karar değeri ayrık lemma hata olarak kalıyor (6:14 / 6:25 'evvel' sınaması sürüyor); sunum/mutasyon_sina.py — b19 kural 5 isabetsiz sınaması eklendi; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 214",
 "geriye dönük koşu (araç değişen blok — bekleyen_ariza_6_b13 elle önerisi (8) GERIYE_DONUK_ZORUNLU; komut 'python3 sunum/geriye_donuk.py b19 yamalar/geriye_donuk_6_b17k.txt'; metin ve karar kesinleştikten sonra): GERI_P; yeni sınıfı: blok 06 R5 6:27 'rabb kâne _' gerekçesi — sonradan basılan 6:77 r5_gerekce çıktısını değiştirdi (basılan değişti; kayıt geriye dönük yazılmaz, tam okuma sonu); blok 18 ve blok 19 satırları (KAPSAMAYAN, ZAMİR KAYITSIZ) önceki koşuda taranmamış bloklar — zamir kayıtsız bekleyen yanlış pozitif sınıfı",
 "kök tablosu: ölçümde '???' 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 79 83 19'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:83 'inne rabbeke hakîmun 'alîm' (11-14. kelime) — esma_el 'ilahi', kural ''inne/enne' haberi' (Rab) (yamalar/esma_el_6_79_83.txt); 6:79-82 esmâ yok; "
 "lafız 6:80 (6. kelime), 6:81 (9. kelime); Rab 6:80 (17. ve 20. kelime), 6:83 (12. kelime) (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 79 83 19'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:79 '{{1|fâsıla ٱلمشركين → ن, N sınıfı}}', '{{1|harf 54 → harf3 51, isaret 3}}' ve '{{1|dış düğüm 0}}'; 6:80 '{{2|biçim ISTISNA}}', '{{2|EDİLGEN 1/9 fiil, pas z=0,30}}', '{{2|fâsıla تتذكرون → ن, N sınıfı}}', '{{2|simetri \\[3, 5, 9, 1\\]}}', '{{2|harf 99 → harf3 91, isaret 8}}' ve '{{2|dış düğüm 2}}'; "
 "6:81 '{{3|fâsıla تعلمون → ن, N sınıfı}}', '{{3|simetri \\[4, 2, 6, 1\\]}}', '{{3|harf 96 → harf3 92, isaret 4}}' ve '{{3|dış düğüm 2}}'; 6:82 '{{4|fâsıla مهتدون → ن, N sınıfı}}', '{{4|simetri \\[3, 1, 8, 1\\]}}', '{{4|harf 55 → harf3 52, isaret 3}}' ve '{{4|dış düğüm 0}}'; "
 "6:83 '{{5|fâsıla عليم → م, N sınıfı}}', '{{5|harf 61 → harf3 56, isaret 5}}', '{{5|dış düğüm 2}}' ve '{{5|İÇ düğüm 1}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 79 83 19'): KALAN_P",
 "ölçüm aktör: 6:81 '{{3|aktör: adsız `ferîk` 17\\. sırada}}'; 6:83 '{{5|aktör: adlı إِبْراهِيم 4\\. sırada \\(kisi, rol meful\\)}}'; 6:79, 6:80 ve 6:82 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:79 haber — NEG 1 've mâ' (9.); 6:80 soru — CERT 1 've qad' (7.), INTG 2 'e-tuhâccûnnî' (4.), 'e-fe-lâ' (24.), NEG 2 've lâ' (9.), 'e-fe-lâ' (24.); "
 "6:81 soru, şart — COND 1 'in' (20.), INTG 2 've keyfe' (1.), 'fe-eyyu'l-ferîqayni' (16.), NEG 2 've lâ' (5.), 'lem' (11.); 6:82 haber — NEG 1 've lem' (3.); 6:83 haber — kip yok; "
 "morph ACC ('inne' 6:79 1.; 6:83 11.; 'enne' 6:81 7.), REM ('ve' 6:79 9.; 6:80 1.; 6:81 1.; 6:83 1.; 'fe' 6:81 16.), CIRC ('ve' 6:80 7.), EXP ('illâ' 6:80 14.), SUB ('en' 6:80 15.), SUP ('fe' 6:80 24.), DEM ('ulâ'ike' 6:82 7.; 'tilke' 6:83 1.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:79, 6:80, 6:81, 6:82 ve 6:83 yıldız yok",
 "fâsıla: 6:78 ن → 6:79 ن (ٱلمشركين) → 6:80 ن (تتذكرون) → 6:81 ن (تعلمون) → 6:82 ن (مهتدون) → 6:83 م (عليم) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:79 xref yok; 6:80 okunmuş 1 ayet ve okunmamış 1 ayet; 6:81 3:151 (emsal olarak basıldı) ve okunmamış 1 ayet; 6:82 xref yok; 6:83 12:76 (emsal olarak basıldı), okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:79 '_ _ _' süzgeç GEÇMEZ; 6:80 'xâfe _ eşrake', '_ _ şâ'e' ve 'rabb kull şey'' süzgeç GEÇMEZ; 6:81 'xâfe _ eşrake' ve '_ eşrake _' süzgeç GEÇMEZ; 6:83 '_ rabb hakîm 'alîm' süzgeç GEÇER; 6:82 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:79 konuşan 1S (söz içi; gönderge 6:75 3. kelime), 3MS ('fatara' — gönderge 'li'llezî' 4. kelime); 6:80 3MS ('ve hâccehû' 1. kelime — fail 2. kelime; 'yeşâ'e' 16. kelime — fail 17. kelime; 'vesi'a' 19. kelime — fail 20. kelime; öbürleri gönderge 6:75 3. kelime, 'llâh' 6. kelime ve 'mâ' 11. kelime), konuşan 1S ve muhatap 2MP (söz içi); "
 "6:81 konuşan 1S ve muhatap 2MP (söz içi), 3MS ('yunezzil' — gönderge 'llâhi' 9. kelime; 'bihî' — gönderge 'mâ' 10. kelime); 6:82 3MP ('ellezîne' 1. kelime ve 'ulâ'ike' 7. kelime göndergeli); 6:83 konuşan 1P, 3FS ('âteynâhâ' — gönderge 'huccetunâ' 2. kelime), 3MS ('qavmih' — gönderge 'ibrâhîme' 4. kelime), muhatap 2MS — betik denetimi: KHATA_ADSIZ; "
 "'e-tuhâccûnnî' (6:80 4. kelime) morph PASS etiketi — okuma etken III. bab, naib-i faili (adsız) muhatap 2MP; ölçüm EDİLGEN 1/9 bu etiketten (araç tanımı farkı, tam okuma sonu); "
 "6:83 1P konuşan göndergesi adsız (okuma); 6:81 'l-ferîqayni' taraflar: ortak koşanlar ve İbrâhîm (okuma)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2; 'qâle'siz söz biçimli içerik — İbrâhîm sözünün sürmesi, önceki blokta söz 6:78 17. kelimede ayet içi kapandı, söz sınırı tam okuma sonu: A3'e '(söz biçimli içerik, 1. kelimeden)', A4'te 'söz açılır' / 'söz kapanır' yazılmadı): 6:79 'qâle'siz söz biçimli içerik 1-12. kelime (REM sapması 6:79 (9. kelime) — 've mâ ene' söz içinde istînâf, konuşan 1S sürer, söz 12. kelimeye dek sürer); "
 "6:80 'qâle' (3.) ardından söz 4-25. kelime — ayet içi kapanış; 6:81 'qâle'siz söz biçimli içerik 1-22. kelime (REM sapması 6:81 (1. kelime) — 've keyfe' söz başında istînâf, konuşan 1S sürer; REM sapması 6:81 (16. kelime) — 'fe-eyyu'l-ferîqayni' söz içinde istînâf, muhatap 2MP sürer, söz 22. kelimeye dek sürer); 6:79 söz içi REM: 9. kelime ('ve mâ' — istînâf); 6:81 söz içi REM: 1. ve 16. kelime ('ve keyfe', 'fe-eyyu'l-ferîqayni' — istînâf); 6:82 ve 6:83 söz yok; "
 "mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 79 83 19' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:79 've'l-arda' (7.) CONJ, 've mâ' (9.) REM; 6:80 've hâccehû' (1.) REM, 've qad' (7.) CIRC, 've lâ' (9.) CONJ; 6:81 've keyfe' (1.) REM, 've lâ' (5.) CONJ; 6:82 've lem' (3.), 've hum' (10.) CONJ; 6:83 've tilke' (1.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:79 ◈K سمو ('s-semâvâti' 6. kelime — K1); 6:79 ◈K أرض ('l-arda' 7. kelime — K1)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 79 83 19'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:81 (3:151); 6:83 (12:76); 6:79, 6:80 ve 6:82 D3 eşi yok; ayetler arası kalıp 'exâfu mâ' (6:80, 6:81) — lemma dizisi 'dizi 6 80 10 12' / 'dizi 6 81 2 4' (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş (6:79 've mâ ene mine' — 6:56), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:79 şahıs geçişi 3 → 1, edim geçişi nida → haber; 6:80 söz açılır / kapanır (4. / 25. kelime), şahıs geçişi 1 → 3, edim geçişi haber → soru; "
 "6:81 şart → cevap ('in' 20. kelime / 'fe-eyyu'l-ferîqayni' 16. kelime — cevap şarttan önce, 6:15 biçimi), şahıs geçişi 3 → 2, edim geçişi soru → soru, şart; 6:82 şahıs geçişi 2 → 3, edim geçişi soru, şart → haber; 6:83 şahıs geçişi 3 → 1, edim geçişi yok, bölüm kapanışı; "
 "ölçüm iltifât 6:79-83 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:79 'innî veccehtu' — tekit (morph ACC); 've mâ ene' — olumsuz isim cümlesi (morph REM + NEG); 6:80 've qad hedân' — hâl cümlesi (morph CIRC + CERT); 'illâ en yeşâ'e' — istisna (morph EXP + SUB); 'e-fe-lâ' — inkâri soru (morph INTG + SUP + NEG); "
 "6:81 've keyfe' — inkâri soru (morph REM + INTG); 'ennekum eşraktum' — masdar cümlesi (morph ACC); 'in kuntum ta'lemûn' — cevabı önde şart (morph COND); 6:82 'ellezîne … ulâ'ike' — mübteda ve haber cümlesi (morph REL + DEM); 6:83 've tilke huccetunâ' — işaret ve haber (morph REM + DEM); 'inne rabbeke' — tekit (morph ACC)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:81 'bi'llâhi mâ lem yunezzil' — 3:151 ile eş (sayım: 'say 6:81 9-12'); 6:83 'nerfe'u deracâtin men neşâ'u' — 12:76 ile eş (sayım: 'say 6:83 7-10'); "
 "6:80 ve 6:81 'exâfu mâ' — sûre içi eş (sayım: 'dizi 6 80 10 12'); 6:80 kök حجج, ربب, شيأ ikilemeleri; 6:81 kök خوف, شرك ikilemeleri; 6:82 kök أمن ×3; 6:81 'bi'l-emni' ve 6:82 'l-emnu' kök أمن",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 19'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'illâ en yeşâ'e' 6:80 'meğer ki Rabbim bir şey dilesin' / 12:76 'Allah dilemeseydi' (emsal metninde) — çakışma — tam okuma sonu ('meğer ki … dilesin' istisna / 'dilemeseydi' olumsuz şart karşılığı); 'bi'llâhi mâ lem yunezzil' 6:81 'hakkında size hiçbir delil indirmediği şeyleri Allah'a ortak koşmaktan' / 3:151 'Hakkında hiçbir delil indirmediği şeyi Allah'a ortak koştukları için' (emsal metninde) — çakışma — tam okuma sonu ('şeyleri' / 'şeyi' çoğul takdiri; 'size' takdiri); "
 "'nerfe'u deracâtin men neşâ'u' 6:83 'Dilediğimiz kimseyi derecelerle yükseltiriz' / 12:76 'Dilediğimizi derecelerle yükseltiriz' (emsal metninde) — çakışma — tam okuma sonu ('kimseyi' takdiri); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:79 'veccehtu' PERF — meal 'çevirdim'; 'fatara' PERF — meal 'yaratana'; "
 "6:80 'hâcce' PERF — meal 'tartıştı'; 'qâle' PERF — meal 'Dedi'; 'tuhâccûnnî' IMPF IND (soru) — meal 'tartışıyor musunuz'; 'hedâni' PERF — meal 'iletti'; 'exâfu' IMPF IND — meal 'korkmam'; 'tuşrikûne' IMPF IND — meal 'ortak koştuğunuz'; 'yeşâ'e' IMPF SUBJ — meal 'dilesin'; 'vesi'a' PERF — meal 'kuşatmıştır'; 'tetezekkerûn' IMPF IND (soru) — meal 'Düşünmez misiniz'; "
 "6:81 'exâfu' IMPF IND (soru) — meal 'korkarım'; 'eşraktum' PERF — meal 'Ortak koştuklarınızdan', 'ortak koşmaktan'; 'texâfûne' IMPF IND — meal 'korkmuyorsunuz'; 'yunezzil' IMPF JUS (olumsuz geçmiş) — meal 'indirmediği'; 'kuntum' PERF — meal 'biliyorsanız' içinde; 'ta'lemûn' IMPF IND — meal 'biliyorsanız'; "
 "6:82 'âmenû' PERF — meal 'İman edip'; 'yelbisû' IMPF JUS (olumsuz geçmiş) — meal 'karıştırmayanlar'; 6:83 'âteynâ' PERF — meal 'verdiğimiz'; 'nerfe'u' IMPF IND — meal 'yükseltiriz'; 'neşâ'u' IMPF IND — meal 'Dilediğimiz'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; ayetler arası kalıplar: 'exâfu mâ' — çakışma değil (6:80 'korkmam' / 6:81 'korkarım' — olumsuz ve soru çekimi)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 79 83 19'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:79, 6:80, 6:81, 6:82 ve 6:83 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:79 ('s-semâvâti' / 've'l-arda'); 6:81 ('exâfu' / 'bi'l-emni'); 6:82 ('âmenû' / 'bi-zulmin'); 6:80 ve 6:83 karşıt çift yok; "
 "ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök شرك 6:79, 6:80, 6:81; kök خوف 6:80, 6:81; kök أمن 6:81, 6:82; kök حجج 6:80, 6:83; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 9-2 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 18 ve 19; bu blok bölümü kapatıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b19/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 79 83 19'; lem_bozuk.py 19 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 79 83 → AYN_SONUC; sunum/bolum4_kurallar.py 79 83 19 → KHATA_HEPSI; sunum/bolum5_kurallar.py 79 83 19 → B5_HEPSI; sunum/bolum6_kurallar.py 79 83 19 → B6_HEPSI; sunum/bolum7_kurallar.py 79 83 19 → B7_HEPSI; sunum/bolum8_kurallar.py 79 83 19 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 79 83 19 → B9_HEPSI; sunum/bolum10_kurallar.py 79 83 19 → B10_HEPSI; sunum/bolum11_kurallar.py 79 83 19 → B11_HEPSI; sunum/bolum12_kurallar.py 79 83 19 → B12_HEPSI; sunum/bolum13_kurallar.py 79 83 19 → B13_HEPSI; sunum/bolum14_kurallar.py 79 83 19 → B14_HEPSI; sunum/bolum15_kurallar.py 79 83 19 → B15_HEPSI; sunum/bolum16_kurallar.py 79 83 19 → B16_HEPSI; sunum/bolum17_kurallar.py 79 83 19 → B17_HEPSI; sunum/bolum18_kurallar.py 79 83 19 → B18_HEPSI; sunum/bolum19_kurallar.py 79 83 19 → B19_HEPSI; sunum/bolum20_kurallar.py 79 83 19 → B20_HEPSI; sunum/bolum21_kurallar.py 79 83 19 → B21_HEPSI; sunum/bolum22_kurallar.py 79 83 19 → B22_HEPSI; sunum/bolum23_kurallar.py 79 83 19 → B23_HEPSI; sunum/bolum24_kurallar.py 79 83 19 → B24_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 19 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('xâfe', 'eşrake', 'şâ'e', 'rabb', 'kull', 'şey'', 'hakîm', ''alîm', 'illâ', 'en', 'mâ', 'lâ', 'inne'); joker '_' yalnız nakarat3 lemmasız öğede; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (79, 83): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_79_83.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b19.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '79', '83'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '79', '83', '19'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '79', '83', '19'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '79', '83', '19', '--tazelik-yok')}
    for _n in range(7, 25): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '79', '83', '19')
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
