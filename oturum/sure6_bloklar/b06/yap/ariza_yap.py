# sûre 6 blok 6 (6:25-28) ARIZA oluşturucu — bölüm 3-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b06/olcum.txt'
os.environ['SAY2'] = '/home/claude/b06/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Yalanlayanların toplanma sahnesi; dünya hayatı oyun'"


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
 ("6:25", "'qâle ellezî kefera in zâ illâ'", 2, 'say 6:25 25-30', "harekesiz 'yeqûlu'llezîne keferû in hâzâ illâ' (25-30. kelime)", ('dizi 6 25 25 30', "qâle ellezî kefera in zâ illâ", '25-30', "biçim farkı (dizi 6 25 25 30): 6:7 önek")),
 ("6:25", "'hattâ izâ câ'e'", 3, 'say 6:25 21-23', "harekesiz 'hattâ izâ câ'ûke' (21-23. kelime)", ('dizi 6 25 21 23', "hattâ izâ câ'e", '21-23', "biçim farkı (dizi 6 25 21 23): basılmamış eş fiil çekimi, zamir eki; basılmamış eş fiil çekimi, zamir eki")),
 ("6:26", "'illâ nefs mâ şa'ara'", 2, 'say 6:26 8-11', "harekesiz 'illâ enfusehum ve mâ yeş'urûn' (8-11. kelime)", ('dizi 6 26 8 11', "illâ nefs mâ şa'ara", '8-11', "biçim farkı (dizi 6 26 8 11): basılmamış eş i'râb, önek")),
 ("6:27", "'lev raâ iz vuqife 'alâ'", 2, 'say 6:27 1-5', "harekesiz 've lev terâ iz vuqifû 'ale' (1-5. kelime)", None),
 ("6:27", "'rabb kâne min'", 2, 'say 6:27 13-15', "harekesiz 'rabbinâ ve nekûne mine' (13-15. kelime)", ('dizi 6 27 13 15', "rabb kâne min", '13-15', "biçim farkı (dizi 6 27 13 15): basılmamış eş fiil çekimi, i'râb, zamir eki, önek")),
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

VF_YAZI = {25: {1: "'ve minhum'", 5: "'ve ce'alnâ'", 11: "'ve fî'", 14: "'ve in'"}, 26: {1: "'ve hum'", 4: "'ve yen'evne'", 6: "'ve in'", 10: "'ve mâ'"}, 27: {1: "'ve lev'", 10: "'ve lâ'", 14: "'ve nekûne'"}, 28: {9: "'ve lev'", 15: "'ve innehum'"}}
sys.path.insert(0, '/home/claude/b06/yap')
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
open('/home/claude/b06/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '06')
BLOKLAR = [str(i) for i in range(1, 7)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '6', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b06/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '25', '28', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b06/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b06/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '25', '28', '06').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_25_28.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:25', '6:26', '6:27', '6:28'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_25_28.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(25, 29))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:25 kök أذن ('âzânihim' 12. kelime — kulak): tetik listesinde yok; 6:25 'izâ' (22. kelime — morph T, zaman); 6:26 kök هلك ('yuhlikûne' 7. kelime — helâk et-), kök نفس ('enfusehum' 9. kelime — kendi), kök شعر ('yeş'urûn' 11. kelime — farkında ol-): tetik listesinde yok; 6:27 'iz' (3. kelime — morph T, zaman); 6:28 kök قبل ('qabl' 8. kelime — önce): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '25', '28', '06')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b06/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 7)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(25, 29))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/bolum5_kurallar.py kural 5 (ham LEM) edat adı denetiminde 'â' ile biten adda elif maksûre ى kabul edildi ('hattâ' → حتى; önceden LEM dışı sayılıyordu); sunum/yasakli.sh IZIN'e ('ariza_6_25_28.txt', 'ilk, evvel') çifti — bölüm 10 denetimi kuralı 10: kapsamayan kök listesindeki أول kök anlamı araç çıktısı aynen (blok 3 emsali); sunum/edat_etiket.py EDLEM'e 'leyte' (ليت) ve 'bel' (بل) — bölüm 15 denetimi kuralı 15: es_edat 6:27 'leyte' ve 6:28 'bel' başlıklarını tanımamasın diye; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 132",
 "kök tablosu: ölçümde '???' 6:25-28 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 25 28 06'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:25 'esâtîru'l-evvelîn' (31-32. kelime) — esma_el 'degil', kural 'çoğul insan göndergeli' (insan topluluğu) — liste farkı: 'evvel' esma_kayit son3'te var, ölçüm esmâ satırında yok (sûre 6 bölüm 2 denetimi kuralı 9); 6:27 'mine'l-mu'minîn' (15-16. kelime) — esma_el 'degil', kural 'çoğul insan göndergeli' (insan topluluğu); "
 "lafız yok; Rab 6:27 (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 25 28 06'; bölüm 13 denetimi kuralı 2: esma_el eklendikten sonra; bölüm 15 denetimi kuralı 5; 6:25 ve 6:27 muhur EVET / ölçüm uyuşmuyor — araç tanımı farkı): " + EMH,
 "ölçüm: 6:25 '{{1|fâsıla ٱلأولين → ن, N sınıfı}}', '{{1|simetri \\[6, 18, 26, 2\\]}}', '{{1|harf 141 → harf3 133, isaret 8}}' ve '{{1|dış düğüm 3}}'; "
 "6:26 '{{2|fâsıla يشعرون → ن, N sınıfı}}', '{{2|simetri \\[3, 1, 6, 1\\]}}', '{{2|harf 48 → harf3 47, isaret 1}}' ve '{{2|dış düğüm 0}}'; "
 "6:27 '{{3|fâsıla ٱلمؤمنين → ن, N sınıfı}}', '{{3|simetri \\[3, 1, 8, 1\\]}}', '{{3|harf 69 → harf3 67, isaret 2}}', '{{3|dış düğüm 2}}', '{{3|İÇ düğüm 1}}' ve '{{3|EDİLGEN 2/6 fiil, pas z=1,57}}'; "
 "6:28 '{{4|fâsıla لكذبون → ن, N sınıfı}}', '{{4|simetri \\[4, 1, 12, 1\\]}}', '{{4|harf 64 → harf3 59, isaret 5}}', '{{4|dış düğüm 0}}' ve '{{4|EDİLGEN 2/6 fiil, pas z=1,57}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 25 28 06'): KALAN_P",
 "ölçüm aktör: 6:25-28 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:25 şart — COND 1 've in' (14.), NEG 2 'lâ' (18.), 'in' (28.), RES 1 'illâ' (30.); 6:26 haber — NEG 2 'in' (6.), 'mâ' (10.), RES 1 'illâ' (8.); "
 "6:27 nida, şart — COND 1 've lev' (1.), NEG 1 'lâ' (10.), VOC 1 'yâ' (8.); 6:28 şart — COND 1 've lev' (9.), EMPH 2 'le-'âdû' (11.), 'le-kâzibûn' (16.); "
 "morph REM ('ve' 6:25 1. ve 14.; 6:26 6.; 6:28 9. ve 15.), CIRC ('ve' 6:26 1.), RET ('bel' 6:28 1.), ACC ('leyte' 6:27 8.; 'inne' 6:28 15.), SUB ('en' 6:25 9.), INC ('hattâ' 6:25 21.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:25 ★★ (kaynak n, z=2,08); 6:27 ★ (kaynak pas, z=1,57); 6:28 ★ (kaynak pas, z=1,57); 6:26 yıldız yok",
 "fâsıla: 6:24 ن → 6:25 ن (ٱلأولين) → 6:26 ن (يشعرون) → 6:27 ن (ٱلمؤمنين) → 6:28 ن (لكذبون) — N sınıfı sürüyor; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:25 17:46 (emsal olarak basıldı), okunmuş 1 ayet ve okunmamış 1 ayet; 6:26 yok; "
 "6:27 6:4 (basılmış), 36:46 (basılmış) ve okunmamış 1 ayet; 6:28 yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:25 'qâle ellezî kefera in zâ illâ' ve 'hattâ izâ câ'e' süzgeç GEÇER; 6:26 'illâ nefs mâ şa'ara' GEÇER; 6:27 'lev raâ iz vuqife 'alâ' GEÇER, 'rabb kâne min' GEÇMEZ; "
 "6:28 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; edilgen fiilde naib-i faili zamir 'adsız' ile — sûre 6 bölüm 2 denetimi kuralı 5; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8): "
 "6:25 3MP, 3MS, 3FS (adsız — gönderge 6:24 7. kelime, 'men', 'âyetin'), muhatap 2MS, konuşan 1P (adsız), 'yeqûlu' 25. kelime — fail 26. kelime; 6:26 3MP ve 3MS (adsız — gönderge 6:25 26. ve 10. kelime); "
 "6:27 muhatap 2MS (adsız), 3MP (adsız; 'vuqifû' edilgen — naib-i faili zamir), konuşan 1P (adsız; söz içi; 'nuraddu' edilgen — naib-i faili konuşan zamir); "
 "6:28 3MS ('bedâ' 2. kelime — fail 4. kelime; ''anhu' adsız), 3MP (adsız — gönderge 6:27 7. kelime; 'ruddû', 'nuhû' edilgen — naib-i faili zamir) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): "
 "6:25 'yeqûlu' (25.) ve fail (26.) ardından söz 28-32. kelime; 6:27 'fe-qâlû' (7.) ardından söz 8-16. kelime — ayet içi kapanışlar; 6:26 ve 6:28 söz yok; mealde tırnaksız, iki nokta ile (blok meal biçimi); A3'te ve A4'te 'söz açılır' / 'söz kapanır'; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 25 28 06' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 6:25 've minhum' (1.), 've in' (14.) REM, 've ce'alnâ' (5.), 've fî' (11.) CONJ; 6:26 've hum' (1.) CIRC, 've yen'evne' (4.), 've mâ' (10.) CONJ, 've in' (6.) REM; 6:27 've lev' (1.), 've lâ' (10.), 've nekûne' (14.) CONJ, 'fe-qâlû' (7.) CONJ; 6:28 've lev' (9.), 've innehum' (15.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:25 ◈B سمع ('yestemi'u' 3. kelime — B3), قلب ('qulûbihim' 7. kelime — B3; anlam notu: dinleme ve kalp, anlamaya engel örtü)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 25 28 06'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:25 (17:46); 6:26, 6:27 ve 6:28 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp yok; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:25 şart → cevap ('in' 14. kelime / 'lâ yu'minû bihâ' 18. kelime), söz açılır / kapanır (28-32. kelime), edim geçişi emir → şart; 6:26 edim geçişi şart → haber; "
 "6:27 şart → cevap ('lev' 1. kelime — cevap hazif), söz açılır / kapanır (8-16. kelime), şahıs geçişi 3 → 1, edim geçişi haber → nida; 6:28 şart → cevap ('lev' 9. kelime / ''âdû' 11. kelime; tekit 'le-kâzibûn' 16. kelime REM ile ayrı cümle), şahıs geçişi 1 → 3, edim geçişi nida → şart; şahıs beraberliği yok (sûre 6 bölüm 1 denetimi kuralı 9); ölçüm iltifât 6:25-28 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:25 'men yestemi'u' — ilgi (morph REL); 'en yefqahûhu' — mastar (morph SUB); 'in yerev' — şart (morph COND); 'in hâzâ illâ' — kasr (morph NEG + RES); "
 "6:26 've hum yenhevne' — hal (morph CIRC); 'in yuhlikûne illâ' — kasr (morph NEG + RES); 6:27 'lev terâ' — şart, cevap hazif (morph COND); 'yâ leytenâ' — temenni (morph VOC + ACC); "
 "6:28 'bel' — idrâb (morph RET); 'lev ruddû le-'âdû' — şart ve cevap (morph COND + EMPH); 'innehum le-kâzibûn' — tekit (morph ACC + EMPH)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:25 5-13. kelime 17:46 ile eş (sayım: 'say 6:25 5-13'); "
 "6:25 'yeqûlu'llezîne keferû in hâzâ illâ' — 6:7 ile lemma dizisinde eş (sayım: 'dizi 6 25 25 30'); 6:27 'yâ leytenâ nuraddu' — geri dönüş temennisi; "
 "6:28 'ruddû' — 6:27 'nuraddu' ile kök ردد; 'bedâ' / 'yuxfûne' karşıtlığı",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 05'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'en yefqahûhu' 6:25 'onu anlamalarına engel' / 17:46 'onu anlamalarına engel' (emsal metninde) — çakışma değil; "
 "'ve fî âzânihim vaqrâ' 6:25 'kulaklarına da ağırlık' / 17:46 'kulaklarına da ağırlık' (emsal metninde) — çakışma değil; "
 "'âzânihim vaqrâ' 6:25 'kulaklarına da ağırlık' / 17:46 'kulaklarına da ağırlık' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:25 'yestemi'u' IMPF IND — meal sıfat-fiil 'dinleyen'; 'ce'alnâ' PERF — meal geçmiş '-duk'; 'yefqahûhu' IMPF SUBJ — meal mastar 'anlamalarına'; 'yerev' IMPF JUS (şart) — meal şart 'görseler'; 'yu'minû' IMPF JUS (cevap) — meal geniş zaman olumsuz; 'câ'ûke' PERF — meal 'geldiklerinde'; 'yucâdilûneke' IMPF IND — meal geniş zaman; 'yeqûlu' IMPF IND — meal 'derler'; 'keferû' PERF — meal sıfat-fiil 'edenler'; "
 "6:26 'yenhevne', 'yen'evne', 'yuhlikûne', 'yeş'urûn' IMPF IND — meal geniş zaman; 6:27 'terâ' IMPF IND (lev ile) — meal istek-şart 'görsen'; 'vuqifû' PERF edilgen — meal 'durdurulduklarında'; 'fe-qâlû' PERF — meal '-diler'; 'nuraddu' IMPF IND edilgen — meal temenni '-sek'; 'nukezzibe', 'nekûne' IMPF SUBJ — meal temenni '-sak'; "
 "6:28 'bedâ' PERF — meal geçmiş '-tı'; 'kânû yuxfûne' PERF + IMPF — meal 'gizledikleri'; 'ruddû' PERF edilgen (lev ile) — meal varsayım '-selerdi'; ''âdû' PERF (cevap) — meal '-erlerdi'; 'nuhû' PERF edilgen — meal sıfat-fiil 'yasaklanan'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 25 28 06'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:25-28 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:27 ('nukezzibe' / 'l-mu'minîn'); 6:28 ('bedâ' / 'yuxfûne'); 6:25 ve 6:26 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök ردد 6:27 ('nuraddu') ve 6:28 ('ruddû') — geri döndürülme bağı; kök نهي 6:26 ('yenhevne') ve 6:28 ('nuhû'); kök كذب 6:27 ('nukezzibe') ve 6:28 ('le-kâzibûn'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 3-2 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm üç blok (5, 6, 7); "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b06/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 25 28 06'; lem_bozuk.py 06 çıktısı): lem_bozuk bayrağı 6:26 11. kelime يَشْعُرُ, 6:27 4. kelime وُقِفُ, 6:28 6. kelime أُخْفِيَ — meal maddelerinde (morph LEM ham biçim) notu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 25 28 → AYN_SONUC; sunum/bolum4_kurallar.py 25 28 06 → KHATA_HEPSI; sunum/bolum5_kurallar.py 25 28 06 → B5_HEPSI; sunum/bolum6_kurallar.py 25 28 06 → B6_HEPSI; sunum/bolum7_kurallar.py 25 28 06 → B7_HEPSI; sunum/bolum8_kurallar.py 25 28 06 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 25 28 06 → B9_HEPSI; sunum/bolum10_kurallar.py 25 28 06 → B10_HEPSI; sunum/bolum11_kurallar.py 25 28 06 → B11_HEPSI; sunum/bolum12_kurallar.py 25 28 06 → B12_HEPSI; sunum/bolum13_kurallar.py 25 28 06 → B13_HEPSI; sunum/bolum14_kurallar.py 25 28 06 → B14_HEPSI; sunum/bolum15_kurallar.py 25 28 06 → B15_HEPSI; sunum/bolum16_kurallar.py 25 28 06 → B16_HEPSI; sunum/bolum17_kurallar.py 25 28 06 → B17_HEPSI; sunum/bolum18_kurallar.py 25 28 06 → B18_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta 'ariza_6_25_28.txt' için 'ilk, evvel' eklendi",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 6 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('qâle', 'ellezî', 'kefera', 'in', 'zâ', 'illâ', 'hattâ', 'izâ', 'câ'e', 'nefs', 'mâ', 'şa'ara' (morph LEM ham biçim), 'lev', 'raâ', 'iz', 'vuqife' (morph LEM ham biçim), ''alâ', 'rabb', 'kâne', 'min'); lemmasız öğe joker yok; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (25, 28): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_25_28.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b05.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '25', '28'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '25', '28', '06'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '25', '28', '06'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '25', '28', '06', '--tazelik-yok')}
    for _n in range(7, 19): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '25', '28', '06')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18 = [_R['B%d' % _n].splitlines() for _n in range(6, 19)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
