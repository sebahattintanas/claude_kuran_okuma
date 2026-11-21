# sûre 6 blok 15 (6:62-67) ARIZA oluşturucu — bölüm 7-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b15/olcum.txt'
os.environ['SAY2'] = '/home/claude/b15/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Gaybın anahtarları; karanlıklardan kurtaran'"


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
 ("6:63", "'zulme berr bahr'", 2, 'say 6:63 5-7', "harekesiz 'zulumâti'l-berri ve'l-bahr' (5-7. kelime)", None),
 ("6:65", "'nazara keyf sarref âye'", 2, 'say 6:65 22-25', "harekesiz 'unzur keyfe nusarrifu'l-âyât' (22-25. kelime)", None),
 ("6:65", "'qâdir 'alâ en'", 2, 'say 6:65 3-5', "harekesiz 'l-qâdiru 'alâ en' (3-5. kelime)", ('dizi 6 65 3 5', "qâdir 'alâ en", '3-5', "biçim farkı (dizi 6 65 3 5): 6:37 önek")),
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

VF_YAZI = {62: {10: "'ve huve'"}, 63: {7: "'ve'l-bahri'", 10: "'ve xufyeh'"}, 64: {5: "'ve min'"}, 65: {18: "'ve yuzîqa'"}, 66: {1: "'ve kezzebe'", 4: "'ve huve'"}, 67: {4: "'ve sevfe'"}}
sys.path.insert(0, '/home/claude/b15/yap')
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
open('/home/claude/b15/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '15')
BLOKLAR = [str(i) for i in range(1, 16)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '15', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b15/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '62', '67', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b15/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b15/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '62', '67', '15').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_62_67.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:62', '6:63', '6:64', '6:65', '6:66', '6:67'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_62_67.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(62, 68))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:62 kök ولي ('mevlâhumu' 5. kelime — mevlâ, dost): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '62', '67', '15')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b15/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 16)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(62, 68))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/bolum6_kurallar.py esmâ kural sapması denetimi (bölüm 8 kuralı 2) emsali yalnız kural adlı ('X → karar') önceki esma_el kayıtlarından alır — kural adsız eski yorumlar ('muhatap (2MS)', '2MS'ye olumsuz haber') emsal sayılmaz (6:66 'vekîl'); mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 190",
 "geriye dönük koşu (araç değişen blok — bekleyen_ariza_6_b13 elle önerisi (8) GERIYE_DONUK_ZORUNLU; komut 'python3 sunum/geriye_donuk.py b15 yamalar/geriye_donuk_6_b14.txt'): düşen 6 (araç değişti 6, basılan değişti 0, kayıt değişti 0), yeni 28; kayıtlar geriye dönük yeniden yazılmadı; isabetler tam okuma sonu listesinde (yamalar/geriye_donuk_6_b15.txt)",
 "kök tablosu: ölçümde '???' 6:62-67 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 62 67 15'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:62 'ilâ'llâhi mevlâhumu'l-haqq' (3-6. kelime) — lafzın bedeli / sıfatı; kapalı listede kural yok (protokol: DUR-sor), oturum ortasında sorulmadı — esma_el'e girmedi, e_el=? 1, kullanıcı kararına bırakıldı (tam okuma sonu); "
 "6:63 'min zulumâti'l-berri ve'l-bahr' (4-7. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge); 6:63 'mine'ş-şâkirîn' (16-17. kelime) — esma_el 'degil', kural 'çoğul insan göndergeli' (insan topluluğu); "
 "6:66 'lestu 'aleykum bi-vekîl' (7-9. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge); 6:64, 6:65 ve 6:67 esmâ yok; "
 "lafız 6:62 ve 6:64; Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 62 67 15'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 6:63, 6:66 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı): " + EMH,
 "ölçüm: 6:62 '{{1|fâsıla ٱلحسبين → ن, N sınıfı}}', '{{1|simetri \\[3, 1, 8, 1\\]}}', '{{1|harf 49 → harf3 47, isaret 2}}', '{{1|dış düğüm 1}}', '{{1|EDİLGEN 1/1 fiil, pas z=5,38}}' ve '{{1|biçim DIKKAT}}'; "
 "6:63 '{{2|fâsıla ٱلشكرين → ن, N sınıfı}}', '{{2|simetri \\[3, 2, 11, 1\\]}}', '{{2|harf 75 → harf3 71, isaret 4}}', '{{2|dış düğüm 2}}', '{{2|İÇ düğüm 1}}' ve '{{2|biçim DIKKAT}}'; "
 "6:64 '{{3|fâsıla تشركون → ن, N sınıfı}}', '{{3|simetri \\[3, 4, 8, 1\\]}}', '{{3|harf 37 → harf3 36, isaret 1}}' ve '{{3|dış düğüm 0}}'; "
 "6:65 '{{4|fâsıla يفقهون → ن, N sınıfı}}', '{{4|simetri \\[4, 2, 9, 1\\]}}', '{{4|harf 108 → harf3 105, isaret 3}}' ve '{{4|dış düğüm 2}}'; "
 "6:66 '{{5|fâsıla بوكيل → ل, ل sınıfı — KAFİYE KIRILMASI}}', '{{5|harf 35 → harf3 32, isaret 3}}' ve '{{5|dış düğüm 0}}'; "
 "6:67 '{{6|fâsıla تعلمون → ن, N sınıfı}}', '{{6|harf 24 → harf3 21, isaret 3}}' ve '{{6|dış düğüm 0}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 62 67 15'): KALAN_P",
 "ölçüm aktör: 6:62-67 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:62 haber — kip yok; 6:63 soru, emir, şart — COND 1 'le-in' (11.), EMPH 3 'le-in' (11.), 'le-nekûnenne' (15.), IMPV 1 'qul' (1.), INTG 1 'men' (2.); "
 "6:64 emir — IMPV 1 'qul' (1.); 6:65 emir — IMPV 2 'qul' (1.), 'unzur' (22.); 6:66 emir — IMPV 1 'qul' (6.); 6:67 haber — FUT 1 've sevfe' (4.); "
 "morph ATT ('elâ' 6:62 7.; 'hâ' 6:63 14.), SUB ('en' 6:65 5.), ACC ('le'alle' 6:65 26.), CIRC ('ve' 6:66 4.), REM ('ve' 6:62 10.; 've' 6:66 1.; 've' 6:67 4.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:62 ★★★ (kaynak pas, z=5,38); 6:65 ★ (kaynak n, z=1,55); 6:66 ★ (kaynak allah, z=-0,53; kafiye kırığı); 6:63, 6:64 ve 6:67 yıldız yok",
 "fâsıla: 6:61 ن → 6:62 ن (ٱلحسبين) → 6:63 ن (ٱلشكرين) → 6:64 ن (تشركون) → 6:65 ن (يفقهون) — N sınıfı; 6:66 ل (بوكيل) — kafiye kırılması (ölçüm); 6:67 ن (تعلمون) — N sınıfına dönüş; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:62 10:30 (emsal olarak basıldı); 6:63 10:22 (emsal olarak basıldı) ve okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1); 6:65 okunmuş 2 ayet; 6:64 xref yok; 6:66 xref yok; 6:67 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:63 'zulme berr bahr' süzgeç GEÇMEZ; 6:65 'nazara keyf sarref âye' süzgeç GEÇER, 'qâdir 'alâ en' GEÇMEZ; 6:62, 6:64, 6:66 ve 6:67 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; edilgen fiilde naib-i fail — sûre 6 bölüm 2 denetimi kuralı 5; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:62 3MP ('ruddû' edilgen — naib-i faili zamir; zamirler adsız), 3MS (adsız — gönderge 'llâhi' 4. kelime); 6:63 muhatap 2MS, muhatap 2MP (söz içi), 3MS (adsız — gönderge 'men' 2. kelime), konuşan 1P (söz içi); "
 "6:64 muhatap 2MS, 3MS (adsız — gönderge 'llâhu' 2. kelime), muhatap 2MP (söz içi), 3FS (adsız — gönderge 6:63 5. kelime); 6:65 muhatap 2MS, 3MS (adsız — gönderge 6:64 2. kelime), muhatap 2MP (söz içi), konuşan 1P, 3MP (adsız — gönderge 6:66 3. kelime); "
 "6:66 3MS ('ve kezzebe' 1. kelime — fail 3. kelime; zamirler adsız — gönderge 6:65 8. kelime), muhatap 2MS, konuşan 1S (söz içi), muhatap 2MP (söz içi); 6:67 muhatap 2MP — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:63 'qul' (1.) ardından söz 2-17. kelime — içindeki 'le-in encânâ … mine'ş-şâkirîn' (11-17. kelime) dua içeriği 'qul' sözünün içinde, ayrı 'söz açılır' yazılmadı; "
 "6:64 'qul' (1.) ardından söz 2-10. kelime; 6:65 'qul' (1.) ardından söz 2-21. kelime — 'unzur' (22.) yeni hitap ile kapanış; 6:66 'qul' (6.) ardından söz 7-9. kelime; 6:62 ve 6:67 söz yok; mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 62 67 15' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:62 've huve' (10.) REM; 6:63 've'l-bahri' (7.), 've xufyeh' (10.) CONJ; 6:64 've min' (5.) CONJ; 6:65 've yuzîqa' (18.) CONJ; 6:66 've kezzebe' (1.) REM, 've huve' (4.) CIRC; 6:67 've sevfe' (4.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:63 ◈K بحر ('l-bahri' 7. kelime — K1; anlam notu: kara ve denizin karanlıkları); tetik listesinde olmayan organ adı 'erculikum' (6:65 14. kelime) not edildi",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 62 67 15'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 6 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:62 (10:30); 6:63 (10:22); 6:64, 6:65, 6:66 ve 6:67 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş (6:65 'nazara keyf sarref âye' — 6:46), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:62 şahıs geçişi yok, edim geçişi yok; 6:63 söz açılır / kapanır (2-17. kelime), şart → cevap ('in' 11. kelime / 'le-nekûnenne' 15. kelime), şahıs geçişi yok, edim geçişi haber → soru, emir, şart; "
 "6:64 söz açılır / kapanır (2-10. kelime), şahıs geçişi 3 → 2, edim geçişi soru, emir, şart → emir — 6:63 sorusu 6:64'te 'quli'llâhu yuneccîkum' ile yanıtlanıyor (okuma); 6:65 söz açılır / kapanır (2-21. kelime), şahıs geçişi yok, edim geçişi yok; "
 "6:66 söz açılır / kapanır (7-9. kelime), şahıs geçişi 2 → 3, edim geçişi yok; 6:67 şahıs geçişi 3 → 2, edim geçişi emir → haber, bölüm kapanışı; "
 "şahıs beraberliği 6:65, 6:66 (sûre 6 bölüm 1 denetimi kuralı 9); ölçüm iltifât 6:62-67 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:62 'elâ lehu'l-hukm' — dikkat çekme, haber öne (morph ATT); 've huve esra'u'l-hâsibîn' — istînâf (morph REM); 6:63 'men yuneccîkum' — soru (morph INTG); 'le-in encânâ' — yemin lâmlı şart (morph EMPH + COND); "
 "6:65 'en yeb'ase' — masdar cümleciği (morph SUB); 'le'allehum yefqahûn' — ümit (morph ACC); 6:66 've kezzebe' — istînâf (morph REM); 've huve'l-haqq' — hâl (morph CIRC); 'bi-vekîl' — 'bi' zâid; 6:67 've sevfe ta'lemûn' — istînâf (morph REM + FUT)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:62 'ile'llâhi mevlâhumu'l-haqq' — 10:30 ile eş (sayım: 'say 6:62 3-6'); "
 "6:63 'le-nekûnenne mine'ş-şâkirîn' — 10:22 ile eş (sayım: 'say 6:63 15-17'); 6:63 kök نجو ikilemesi; 6:63 'men yuneccîkum' / 6:64 'llâhu yuneccîkum' soru ve yanıt; 6:65 'unzur keyfe nusarrifu'l-âyât' — 6:46 ile eş (sayım: 'say 6:65 22-25'); 6:65 kök بعض ikilemesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 15'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'ile'llâhi mevlâhumu'l-haqq' 6:62 'gerçek mevlâları olan Allah'a' / 10:30 'Gerçek mevlâları olan Allah'a' (emsal metninde) — çakışma — tam okuma sonu ('gerçek' / 'Gerçek' cümle başı yazımı); "
 "'le-nekûnenne mine'ş-şâkirîn' 6:63 'mutlaka şükredenlerden olacağız' / 10:22 'mutlaka şükredenlerden olacağız' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:62 'ruddû' PERF edilgen — meal 'döndürülürler'; "
 "6:63 'qul' IMPV — meal 'De'; 'yuneccîkum' IMPF IND — meal 'kurtarır'; 'ted'ûnehû' IMPF IND — meal 'dua edersiniz'; 'encânâ' PERF (şart) — meal 'kurtarırsa'; 'le-nekûnenne' IMPF IND (tekitli) — meal 'olacağız'; "
 "6:64 'qul' IMPV — meal 'De'; 'yuneccîkum' IMPF IND — meal 'kurtarır'; 'tuşrikûn' IMPF IND — meal 'ortak koşarsınız'; "
 "6:65 'qul' IMPV — meal 'De'; 'yeb'ase' IMPF SUBJ — meal 'göndermeye'; 'yelbisekum' IMPF SUBJ — meal 'karıştırıp'; 've yuzîqa' IMPF SUBJ — meal 'tattırmaya'; 'unzur' IMPV — meal 'Bak'; 'nusarrifu' IMPF IND — meal 'açıklıyoruz'; 'yefqahûn' IMPF IND — meal 'anlarlar'; "
 "6:66 've kezzebe' PERF — meal 'yalanladı'; 'qul' IMPV — meal 'De'; 'lestu' PERF ('leyse') — meal 'değilim'; 6:67 'ta'lemûn' IMPF IND — meal 'bileceksiniz'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 62 67 15'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:63 tarayıcı adayı (kök بحر, ظلم; A_şart) — çıpa değil: kara ve denizin karanlıkları sıkıntı benzetmesi, doğa iddiası yok (olgu=False); 6:62, 6:64, 6:65, 6:66 ve 6:67 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:63 ('l-berri' / 've'l-bahri'; 'tedarru'an' / 've xufyeh'); 6:64 ('yuneccîkum' / 'tuşrikûn'); 6:65 ('min fevqikum' / 'min tahti erculikum'); 6:66 ('ve kezzebe' / 'l-haqq'); 6:62 yok; 6:67 yok; "
 "ayetler arası çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök نجو 6:63 ('yuneccîkum', 'encânâ') ve 6:64 ('yuneccîkum'); kök حقق 6:62 ('l-haqq') ve 6:66 ('l-haqq'); kök برر / بحر 6:59 ve 6:63; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 7-2 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 14 ve 15; bu blok bölümü kapatıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b15/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 62 67 15'; lem_bozuk.py 15 çıktısı): lem_bozuk bayrağı 6:65 16. kelime (لَبَسْ — 'yelbisekum'), 24. kelime (صَرَّفْ — 'nusarrifu') ve 27. kelime (يَفْقَهُ — 'yefqahûn'), meal kayıtlarında '(morph LEM ham biçim)' notu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 62 67 → AYN_SONUC; sunum/bolum4_kurallar.py 62 67 15 → KHATA_HEPSI; sunum/bolum5_kurallar.py 62 67 15 → B5_HEPSI; sunum/bolum6_kurallar.py 62 67 15 → B6_HEPSI; sunum/bolum7_kurallar.py 62 67 15 → B7_HEPSI; sunum/bolum8_kurallar.py 62 67 15 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 62 67 15 → B9_HEPSI; sunum/bolum10_kurallar.py 62 67 15 → B10_HEPSI; sunum/bolum11_kurallar.py 62 67 15 → B11_HEPSI; sunum/bolum12_kurallar.py 62 67 15 → B12_HEPSI; sunum/bolum13_kurallar.py 62 67 15 → B13_HEPSI; sunum/bolum14_kurallar.py 62 67 15 → B14_HEPSI; sunum/bolum15_kurallar.py 62 67 15 → B15_HEPSI; sunum/bolum16_kurallar.py 62 67 15 → B16_HEPSI; sunum/bolum17_kurallar.py 62 67 15 → B17_HEPSI; sunum/bolum18_kurallar.py 62 67 15 → B18_HEPSI; sunum/bolum19_kurallar.py 62 67 15 → B19_HEPSI; sunum/bolum20_kurallar.py 62 67 15 → B20_HEPSI; sunum/bolum21_kurallar.py 62 67 15 → B21_HEPSI; sunum/bolum22_kurallar.py 62 67 15 → B22_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 15 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('radde', 'ilâ', 'allâh', 'mevlâ', 'haqq', 'in', 'encâ', 'min', 'zâ', 'kâne', 'şâkir', 'zulme', 'berr', 'bahr', 'nazara', 'keyf', 'sarref' (morph LEM ham biçim), 'âye', 'qâdir', ''alâ', 'en'); lemmasız öğe yok, joker yok; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (62, 67): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_62_67.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b14.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '62', '67'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '62', '67', '15'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '62', '67', '15'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '62', '67', '15', '--tazelik-yok')}
    for _n in range(7, 23): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '62', '67', '15')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22 = [_R['B%d' % _n].splitlines() for _n in range(6, 23)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
