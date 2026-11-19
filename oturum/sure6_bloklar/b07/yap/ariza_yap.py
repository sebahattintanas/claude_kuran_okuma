# sûre 6 blok 7 (6:29-32) ARIZA oluşturucu — bölüm 3-3
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b07/olcum.txt'
os.environ['SAY2'] = '/home/claude/b07/say2.txt'
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
 ("6:30", "'lev raâ iz vuqife 'alâ'", 2, 'say 6:30 1-5', "harekesiz 've lev terâ iz vuqifû 'alâ' (1-5. kelime)", None),
 ("6:30", "''azâb mâ kâne'", 3, 'say 6:30 16-18', "harekesiz 'l-'azâbe bimâ kuntum' (16-18. kelime)", ('dizi 6 30 16 18', "'azâb mâ kâne", '16-18', "biçim farkı (dizi 6 30 16 18): basılmamış eş fiil çekimi, zamir eki; basılmamış eş fiil çekimi, zamir eki")),
 ("6:30", "'mâ kâne kefera'", 2, 'say 6:30 17-19', "harekesiz 'bimâ kuntum tekfurûn' (17-19. kelime)", ('dizi 6 30 17 19', "mâ kâne kefera", '17-19', "biçim farkı (dizi 6 30 17 19): basılmamış eş fiil çekimi, zamir eki")),
 ("6:31", "'hattâ izâ câ'e'", 3, 'say 6:31 7-9', "harekesiz 'hattâ izâ câ'ethum' (7-9. kelime)", ('dizi 6 31 7 9', "hattâ izâ câ'e", '7-9', "biçim farkı (dizi 6 31 7 9): 6:25 fiil çekimi, zamir eki; basılmamış eş fiil çekimi, zamir eki")),
 ("6:31", "'qad xasira ellezî'", 2, 'say 6:31 1-3', "harekesiz 'qad xasira'llezîne' (1-3. kelime)", None),
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

VF_YAZI = {29: {1: "'ve qâlû'", 7: "'ve mâ'"}, 30: {1: "'ve lev'", 13: "'ve rabbinâ'"}, 31: {18: "'ve hum'"}, 32: {1: "'ve me'", 6: "'ve lahv'", 7: "'ve le'd-dâru'"}}
sys.path.insert(0, '/home/claude/b07/yap')
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
open('/home/claude/b07/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '07')
BLOKLAR = [str(i) for i in range(1, 8)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '7', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b07/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '29', '32', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b07/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b07/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '29', '32', '07').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_29_32.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:29', '6:30', '6:31', '6:32'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_29_32.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(29, 33))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:29 kök دنو ('d-dunyâ' 6. kelime — dünya): tetik listesinde yok; 6:30 'iz' (3. kelime — morph T, zaman); 6:31 'izâ' (8. kelime — morph T, zaman); 6:31 kök ظهر ('zuhûrihim' 22. kelime — sırt), kök سوأ ('sâ'e' 24. kelime — kötü): tetik listesinde yok; 6:32 kök دنو ('d-dunyâ' 3. kelime — dünya), kök أخر ('l-âxiratu' 8. kelime — âhiret): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '29', '32', '07')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b07/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 8)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(29, 33))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/edat_etiket.py EDLEM'e 'hiye' (هي), 'belâ' (بلي), 'elâ' (الا) — bölüm 15 denetimi kuralı 15: es_edat 6:29, 6:30 ve 6:31 başlıklarını tanımıyordu; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 139",
 "kök tablosu: ölçümde '???' 6:29-32 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 29 32 07'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:32 'l-âxiratu' (8. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (yurdun sıfatı); "
 "lafız 6:31; Rab 6:30 (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 29 32 07'; bölüm 13 denetimi kuralı 2: esma_el eklendikten sonra; bölüm 15 denetimi kuralı 5; 6:32 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı): " + EMH,
 "ölçüm: 6:29 '{{1|fâsıla بمبعوثين → ن, N sınıfı}}', '{{1|simetri \\[3, 2, 7, 1\\]}}', '{{1|harf 40 → harf3 39, isaret 1}}' ve '{{1|dış düğüm 1}}'; "
 "6:30 '{{2|fâsıla تكفرون → ن, N sınıfı}}', '{{2|simetri \\[4, 5, 12, 1\\]}}', '{{2|harf 82 → harf3 76, isaret 6}}', '{{2|dış düğüm 3}}' ve '{{2|EDİLGEN 1/9 fiil, pas z=0,30}}'; "
 "6:31 '{{3|fâsıla يزرون → ن, N sınıfı}}', '{{3|simetri \\[3, 1, 15, 1\\]}}', '{{3|harf 115 → harf3 110, isaret 5}}' ve '{{3|dış düğüm 1}}'; "
 "6:32 '{{4|fâsıla تعقلون → ن, N sınıfı}}', '{{4|harf 66 → harf3 61, isaret 5}}' ve '{{4|dış düğüm 4}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 29 32 07'): KALAN_P",
 "ölçüm aktör: 6:29-32 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:29 haber — NEG 2 'in' (2.), 'mâ' (7.), RES 1 'illâ' (4.); 6:30 soru, emir, şart — COND 1 've lev' (1.), INTG 1 'eleyse' (8.), IMPV 1 'fe-zûqu' (15.); "
 "6:31 nida — CERT 1 'qad' (1.), VOC 1 'yâ' (13.); 6:32 soru — NEG 2 'mâ' (1.), 'lâ' (12.), RES 1 'illâ' (4.), EMPH 1 'le' (7.), INTG 1 'e-fe-lâ' (12.); "
 "morph REM ('ve' 6:29 1.; 6:32 1.), CIRC ('ve' 6:31 18.), ANS ('belâ' 6:30 12.), SUP ('fe' 6:30 15.; 6:32 12.), ATT ('elâ' 6:31 23.), INC ('hattâ' 6:31 7.), yemin 've' (6:30 13., morph P) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:30 ★ (kaynak rab, z=1,92); 6:29, 6:31 ve 6:32 yıldız yok",
 "fâsıla: 6:28 ن → 6:29 ن (بمبعوثين) → 6:30 ن (تكفرون) → 6:31 ن (يزرون) → 6:32 ن (تعقلون) — N sınıfı sürüyor; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:29 okunmuş 1 ayet; 6:30 46:34 (emsal olarak basıldı), 5:116 (basılmış) ve okunmuş 1 ayet; "
 "6:31 10:45 (emsal olarak basıldı); 6:32 47:36 (emsal olarak basıldı), okunmuş 2 ayet ve okunmamış 1 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:30 'lev raâ iz vuqife 'alâ' ve ''azâb mâ kâne' süzgeç GEÇER, 'mâ kâne kefera' GEÇMEZ; 6:31 'hattâ izâ câ'e' GEÇER, 'qad xasira ellezî' GEÇMEZ; "
 "6:29 ve 6:32 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; edilgen fiilde naib-i faili zamir 'adsız' ile — sûre 6 bölüm 2 denetimi kuralı 5; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8): "
 "6:29 3MP, 3FS (adsız — gönderge 6:28 15. kelime, 'hayâtunâ'), konuşan 1P (adsız; söz içi); 6:30 muhatap 2MS, 3MP ('vuqifû' edilgen — naib-i faili zamir; adsız), 3MS (adsız — gönderge 'rabbihim', 'hâzâ'), konuşan 1P ve muhatap 2MP (adsız; söz içi); "
 "6:31 'xasira' 2. kelime — fail 3. kelime; 'câ'ethumu' 9. kelime — fail 10. kelime; 3MP (adsız — gönderge 'llezîne'), konuşan 1P ve 3FS (adsız; söz içi), 3MS ('sâ'e' — gönderge 'mâ'); "
 "6:32 3MP (adsız — gönderge 'llezîne'), muhatap 2MP (adsız) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): "
 "6:29 've qâlû' (1.) ardından söz 2-9. kelime; 6:30 'qâle' (7.) ardından söz 8-10., 'qâlû' (11.) ardından söz 12-13., 'qâle' (14.) ardından söz 15-19. kelime; 6:31 'qâlû' (12.) ardından söz 13-17. kelime — ayet içi kapanışlar; 6:32 söz yok; mealde tırnaksız, iki nokta ile (blok meal biçimi); A3'te ve A4'te 'söz açılır' / 'söz kapanır'; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 29 32 07' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 6:29 've qâlû' (1.) REM, 've mâ' (7.) CONJ; 6:30 've lev' (1.) CONJ, 've rabbinâ' (13.) yemin edatı (morph P), 'fe-zûqu' (15.) SUP; 6:31 've hum' (18.) CIRC; 6:32 've me'l-hayâtu' (1.) REM, 've lahv' (6.), 've le'd-dâru' (7.) CONJ, 'e-fe-lâ' (12.) SUP",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:29 ◈B حيي ('hayâtunâ' 5. kelime — B4); 6:31 ◈K سوع ('s-sâ'atu' 10. kelime — K2), ◈B حمل ('yahmilûne' 19. kelime — B2); 6:32 ◈B حيي ('l-hayâtu' 2. kelime — B4; anlam notu: dünya hayatı)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 29 32 07'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:30 (46:34); 6:31 (10:45); 6:32 (47:36); 6:29 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp yok; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:29 söz açılır / kapanır (2-9. kelime), edim geçişi şart → haber; 6:30 şart → cevap ('lev' 1. kelime — cevap hazif), söz açılır / kapanır (8-10., 12-13., 15-19. kelime), şahıs geçişi 3 → 2, edim geçişi haber → soru; "
 "6:31 söz açılır / kapanır (13-17. kelime), şahıs geçişi 2 → 3, edim geçişi soru → nida; 6:32 edim geçişi nida → soru, şahıs beraberliği (2MP 2 · 3MP 2), bölüm kapanışı; öteki ayetlerde şahıs beraberliği yok (sûre 6 bölüm 1 denetimi kuralı 9); ölçüm iltifât 6:29-32 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:29 'in hiye illâ' — kasr (morph NEG + RES); 'mâ nahnu bi-meb'ûsîn' — olumsuz isim cümlesi (morph NEG); 6:30 'lev terâ' — şart, cevap hazif (morph COND); 'eleyse' — soru (morph INTG); 'belâ' — cevap (morph ANS); "
 "6:31 'qad xasira' — tahkik (morph CERT); 'hattâ izâ' — zaman (morph INC); 'yâ hasratenâ' — nida (morph VOC); 'elâ sâ'e' — dikkat çekme (morph ATT); "
 "6:32 'mâ … illâ' — kasr (morph NEG + RES); 'le'd-dâru' — tekit (morph EMPH); 'e-fe-lâ' — soru (morph INTG)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:30 8-19. kelime 46:34 ile lemma dizisinde eş (sayım: 'dizi 6 30 8 19'); "
 "6:31 'qad xasira'llezîne kezzebû bi-liqâ'i'llâh' ile açılıyor — 10:45 ile eş (sayım: 'say 6:31 1-6'); 6:31 kök وزر ikilemesi; "
 "6:32 'la'ibun ve lahv' — 47:36 ile eş (sayım: 'say 6:32 5-6'); 6:29 'hayâtunâ'd-dunyâ' / 6:32 'l-hayâtu'd-dunyâ' — dünya hayatı bağı",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 05'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'eleyse hâzâ bi'l-haqq' 6:30 'Bu gerçek değil mi' / 46:34 'Bu gerçek değil mi' (emsal metninde) — çakışma değil; "
 "'qâlû belâ ve rabbinâ' 6:30 'Evet, Rabbimize andolsun' / 46:34 'Evet, Rabbimize andolsun' (emsal metninde) — çakışma değil; "
 "'belâ ve rabbinâ' 6:30 'Evet, Rabbimize andolsun' / 46:34 'Evet, Rabbimize andolsun' (emsal metninde) — çakışma değil; "
 "'bimâ kuntum tekfurûn' 6:30 'inkâr ettiğinize karşılık' / 46:34 'inkâr ettiğinize karşılık' (emsal metninde) — çakışma değil; "
 "'kuntum tekfurûn' 6:30 'inkâr ettiğinize' / 46:34 'inkâr ettiğinize' (emsal metninde) — çakışma değil; "
 "'qad xasira'llezîne kezzebû bi-liqâ'i'llâh' 6:31 'Allah'a kavuşmayı yalanlayanlar gerçekten ziyana uğramıştır' / 10:45 'Allah'a kavuşmayı yalanlayanlar gerçekten ziyana uğramıştır' (emsal metninde) — çakışma değil; "
 "'qad xasira'llezîne' 6:31 'gerçekten ziyana uğramıştır' / 10:45 'gerçekten ziyana uğramıştır' (emsal metninde) — çakışma değil; "
 "'kezzebû bi-liqâ'i'llâh' 6:31 'Allah'a kavuşmayı yalanlayanlar' / 10:45 'Allah'a kavuşmayı yalanlayanlar' (emsal metninde) — çakışma değil; "
 "'la'ibun ve lahv' 6:32 'bir oyun ve oyalanmadır' / 47:36 'bir oyun ve oyalanmadır' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:29 've qâlû' PERF — meal '-diler'; 6:30 'terâ' IMPF IND (lev ile) — meal istek-şart 'görsen'; 'vuqifû' PERF edilgen — meal 'durdurulduklarında'; 'qâle', 'qâlû' PERF — meal '-di' / '-diler'; 'leyse' PERF (olumsuzluk) — meal 'değil'; 'fe-zûqu' IMPV — meal emir 'tadın'; 'kuntum tekfurûn' PERF + IMPF — meal 'inkâr ettiğinize'; "
 "6:31 'xasira' PERF — meal '-mıştır'; 'kezzebû' PERF — meal sıfat-fiil '-anlar'; 'câ'ethumu' PERF (izâ ile) — meal 'geldiğinde'; 'qâlû' PERF (izâ cevabı) — meal geniş zaman 'derler'; 'farratnâ' PERF — meal 'ihmal ettiğimiz'; 'yahmilûne' IMPF IND — meal geniş zaman; 'sâ'e' PERF — meal 'ne kötüdür'; 'yezirûn' IMPF IND — meal 'yüklendikleri'; "
 "6:32 'yetteqûn' IMPF IND — meal sıfat-fiil 'sakınanlar'; 'ta'qilûn' IMPF IND — meal geniş zaman olumsuz soru",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 29 32 07'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:29-32 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:32 ('l-hayâtu'd-dunyâ' / 'd-dâru'l-âxiratu'); 6:29, 6:30 ve 6:31 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök حيي ve دنو 6:29 ('hayâtunâ'd-dunyâ') ve 6:32 ('l-hayâtu'd-dunyâ') — dünya hayatı bağı; kök قول 6:29 ('qâlû'), 6:30 ('qâle', 'qâlû') ve 6:31 ('qâlû'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 3-3 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm üç blok (5, 6, 7); bu blok bölümü kapatıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b07/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 29 32 07'; lem_bozuk.py 07 çıktısı): lem_bozuk bayrağı 6:30 4. kelime وُقِفُ, 6:30 15. kelime ذاقُ, 6:31 26. kelime يَزِرُ, 6:32 13. kelime عَقَلُ — meal maddelerinde (morph LEM ham biçim) notu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 29 32 → AYN_SONUC; sunum/bolum4_kurallar.py 29 32 07 → KHATA_HEPSI; sunum/bolum5_kurallar.py 29 32 07 → B5_HEPSI; sunum/bolum6_kurallar.py 29 32 07 → B6_HEPSI; sunum/bolum7_kurallar.py 29 32 07 → B7_HEPSI; sunum/bolum8_kurallar.py 29 32 07 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 29 32 07 → B9_HEPSI; sunum/bolum10_kurallar.py 29 32 07 → B10_HEPSI; sunum/bolum11_kurallar.py 29 32 07 → B11_HEPSI; sunum/bolum12_kurallar.py 29 32 07 → B12_HEPSI; sunum/bolum13_kurallar.py 29 32 07 → B13_HEPSI; sunum/bolum14_kurallar.py 29 32 07 → B14_HEPSI; sunum/bolum15_kurallar.py 29 32 07 → B15_HEPSI; sunum/bolum16_kurallar.py 29 32 07 → B16_HEPSI; sunum/bolum17_kurallar.py 29 32 07 → B17_HEPSI; sunum/bolum18_kurallar.py 29 32 07 → B18_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 7 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('lev', 'raâ', 'iz', 'vuqife' (morph LEM ham biçim), ''alâ', ''azâb', 'mâ', 'kâne', 'kefera', 'hattâ', 'izâ', 'câ'e', 'qad', 'xasira', 'ellezî'); lemmasız öğe joker yok; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (29, 32): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_29_32.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b05.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '29', '32'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '29', '32', '07'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '29', '32', '07'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '29', '32', '07', '--tazelik-yok')}
    for _n in range(7, 19): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '29', '32', '07')
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
