# sûre 6 blok 1 (6:1-5) ARIZA oluşturucu — bölüm 1-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b01/olcum.txt'
os.environ['SAY2'] = '/home/claude/b01/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = [l.strip().rstrip(',') for l in open('/home/claude/yamalar/devir_5_120.txt', encoding='utf-8') if l.startswith('  "devir (')]; BEK = [ast.literal_eval(x) for x in BEK]
VF_YAZI_ESKI = {}
BOL = "'Gökleri ve yeri yaratan; yüz çeviren kavimler'"


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
 ("6:1", "'ellezî xalaqa semâ' ard'", 2, 'say 6:1 3-6', "harekesiz 'llezî xalaqa's-semâvâti ve'l-ard' (3-6. kelime)", ('dizi 6 1 3 6', "ellezî xalaqa semâ' ard", '3-6', "biçim farkı (dizi 6 1 3 6): basılmamış eş yazım eş")),
 ("6:2", "'_ ellezî xalaqa'", 2, 'say 6:2 1-3', "harekesiz 'huve'llezî xalaqakum' (1-3. kelime)", ('dizi 6 2 1 3', "_ ellezî xalaqa", '1-3', "biçim farkı (dizi 6 2 1 3): basılmamış eş zamir eki, önek")),
 ("6:5", "'mâ kâne _ istuhzi'e'", 2, 'say 6:5 9-12', "harekesiz 'mâ kânû bihî yestehzi'ûn' (9-12. kelime)", ('dizi 6 5 9 12', "mâ kâne _ istuhzi'e", '9-12', "biçim farkı (dizi 6 5 9 12): basılmamış eş yazım eş")),
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

VF_YAZI = {1: {6: "'ve'l-arda'", 7: "'ve ce'ale'", 9: "'ve'n-nûra'"}, 2: {9: "'ve ecelun'"}, 3: {1: "'ve huve'", 5: "'ve fi'l-ardi'", 9: "'ve cehrakum'", 10: "'ve ya'lemu'"}, 4: {1: "'ve mâ'"}, 5: {1: "'fe-qad'", 6: "'fe-sevfe'"}}
sys.path.insert(0, '/home/claude/b01/yap')
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
open('/home/claude/b01/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '01')
BLOKLAR = [str(i) for i in range(1, 2)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '1', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b01/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '1', '5', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b01/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b01/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '1', '5', '01').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_1_5.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:1', '6:2', '6:3', '6:4', '6:5'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_1_5.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(1, 6))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:4 kök عرض ('mu'ridîn' 11. kelime — yüz çevirme): tetik listesinde yok; 6:5 'lemmâ' (4. kelime — morph T, zaman)"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '1', '5', '01')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b01/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 2)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(1, 6))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sûre 6 hazırlığı — sunum/sure.py sûre parametresi ortamdan ('SURE', varsayılan 6) ve blok dizini kökü ('BKOK'); "
 "blok dizinini okuyan bütün araçlar kökü sure.py'den alır (sûre 5 blok dizinleri ayrı köke taşındı); sinifla.py, bolum10_kurallar.py ve bolum13_kurallar.py okunmuş sûre kümesi 'önceki sûreler' ve 'SON' ortamı; "
 "sunum/bolum16_kurallar.py yeni (bölüm 16 denetimi kuralları 1-8; kural 9 elle); bolum6_kurallar.py esmâ KAPALI listesine 'zamirin haberi' (varsayılan karar, onaya açık — protokol §2 Esmâ listesiyle eş); "
 "geriye_donuk.py bolum16_kurallar'ı geriye dönük kümeye alır; mutasyon_sina.py sûre 5 sınamalarını sûre 5 ortamında koşar ve bölüm 16 sınamaları (kural 1-8: sûre 5 kayıtlarındaki doğal isabet; kural 1: isabetsiz kayıt; kural 2: bozuk kopya); mutasyon_sina — MUT_SONUC; "
 "sunum/bolum5_kurallar.py kural 9 ('-dir' takdiri): 'takdir' sözcüğü ek değil — istisna listesine; ARIZA üreticisi denetim betiklerini paralel koşar; "
 "geriye dönük koşu sûre 5 kayıtlarında, araç değişikliğinden sonra (GERI_P); yeni 79 — bolum16_kurallar kural 1: 59, kural 2: 1, kural 3: 3, kural 4: 1, kural 5: 3, kural 6: 1, kural 7: 1, kural 8: 2; düşen 0; kayıtlar geriye dönük yeniden yazılmadı; "
 "basilan satır sayısı (blok anı): 96",
 "kök tablosu: ölçümde '???' 6:1, 6:2, 6:3, 6:4 ve 6:5 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 1 5 01'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:1 've ce'ale'z-zulumâti ve'n-nûr' (7-9. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (yaratılan ışık); "
 "6:2, 6:3, 6:4 ve 6:5 esmâ yok; lafız 6:1 ve 6:3; Rab 6:1 ve 6:4 (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 1 5 01'; bölüm 13 denetimi kuralı 2: esma_el eklendikten sonra; bölüm 15 denetimi kuralı 5; 6:1 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı): " + EMH,
 "ölçüm: 6:1 '{{1|fâsıla يعدلون → ن, N sınıfı}}', '{{1|harf 87 → harf3 65, isaret 0}}' ve '{{1|dış düğüm 2}}'; "
 "6:2 '{{2|fâsıla تمترون → ن, N sınıfı}}', '{{2|simetri \\[3, 1, 12, 1\\]}}', '{{2|harf 55 → harf3 49, isaret 6}}' ve '{{2|dış düğüm 0}}'; "
 "6:3 '{{3|fâsıla تكسبون → ن, N sınıfı}}', '{{3|harf 51 → harf3 50, isaret 1}}' ve '{{3|dış düğüm 0}}'; "
 "6:4 '{{4|fâsıla معرضين → ن, N sınıfı}}', '{{4|simetri \\[3, 1, 8, 1\\]}}', '{{4|harf 45 → harf3 43, isaret 2}}', '{{4|dış düğüm 1}}', '{{4|İÇ düğüm 1}}' ve '{{4|esit2 → 36:46 oran 0,9882 kademe YAKIN}}'; "
 "6:5 '{{5|fâsıla يستهزءون → ن, N sınıfı}}', '{{5|simetri \\[3, 4, 9, 1\\]}}', '{{5|harf 59 → harf3 53, isaret 6}}' ve '{{5|dış düğüm 3}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 1 5 01'): KALAN_P",
 "ölçüm aktör: 6:1, 6:2, 6:3, 6:4 ve 6:5 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:1, 6:2 ve 6:3 haber, kip yok; "
 "6:4 haber — NEG 1 'mâ' (1.), RES 1 'illâ' (8.); ölçüm biçim alanı '{{4|biçim HASR}}' ('mâ … illâ'); 6:5 haber — CERT 1 'fe-qad' (1.), FUT 1 'fe-sevfe' (6.); "
 "morph RSLT ('fe' 6:5 1. ve 6.), REM ('ve' 6:2 9.; 6:4 1.), T ('lemmâ' 6:5 4.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:4 ★ (kaynak rab, z=1,62); 6:1, 6:2, 6:3 ve 6:5 yıldız yok",
 "fâsıla: 6:1 ن (يعدلون) → 6:2 ن (تمترون) → 6:3 ن (تكسبون) → 6:4 ن (معرضين) → 6:5 ن (يستهزءون) — sûre açılışı ن sınıfında; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:1 okunmuş 2 ayet; 6:2 yok; 6:3 yok; 6:4 36:46 (emsal olarak basıldı) ve okunmamış 1 ayet (sûre içi 1); 6:5 50:5 ve 26:6 (emsal olarak basıldı) ve okunmuş 1 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:1 'ellezî xalaqa semâ' ard' süzgeç GEÇER; 6:2 '_ ellezî xalaqa' GEÇMEZ; 6:5 'mâ kâne _ istuhzi'e' GEÇER; 6:3 ve 6:4 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "fail olmayan mecrur çoğul ad ve mecrur ilgi zamiri A1'de yazılmaz — bölüm 11 denetimi kuralları 16 ve 19; fiilden önce gelen lafız 'mübtedâ' — bölüm 12 denetimi kuralı 11; A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1): "
 "6:1 3MS (adsız — gönderge lafız), 3MP (adsız — gönderge 'llezîne'); 6:2 3MS (adsız — 'huve' ve göndergesi), muhatap 2MP (adsız); 6:3 3MS (adsız), lafız (haber), muhatap 2MP (adsız); "
 "6:4 3FS (adsız — gönderge 'âyetin'), 3MP (adsız — gönderge 6:1 11. kelime); 6:5 3MP (adsız), 3MS ('ye'tî' fiil uyumu, fail 'enbâ'u'; 'câ'a' ve 'bihî' adsız) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4): bu blokta söz yok ('qâle' / 'qul' yok); mealde tırnak yok; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 1 5 01' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 6:1 've'l-arda' (6.), 've ce'ale' (7.), 've'n-nûra' (9.) CONJ; 6:2 've ecelun' (9.) REM; 6:3 've huve' (1.), 've fi'l-ardi' (5.), 've cehrakum' (9.), 've ya'lemu' (10.) CONJ; 6:4 've mâ' (1.) REM; 6:5 'fe-qad' (1.) ve 'fe-sevfe' (6.) RSLT",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:1 ◈K سمو ('s-semâvâti' 5. kelime — K1; anlam notu: yaratılan gökler); 6:1 ◈K أرض ('l-arda' 6. kelime — K1; anlam notu: yaratılan yer); "
 "6:1 ◈B خلق ('xalaqa' 4. kelime — B2; anlam notu: göklerin ve yerin yaratılışı); 6:2 ◈K أجل ('ecelen' 8. kelime ve 'ecelun' 9. kelime — K2; anlam notu: takdir edilen süre); "
 "6:2 ◈B خلق ('xalaqakum' 3. kelime — B2; anlam notu: insanın çamurdan yaratılışı); 6:3 ◈K سمو ('s-semâvâti' 4. kelime — K1; anlam notu: göklerde Allah); 6:3 ◈K أرض ('l-ardi' 6. kelime — K1; anlam notu: yerde Allah); 6:4 ve 6:5 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 1 5 01'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:4 (36:46); 6:5 (50:5, 26:6); 6:1, 6:2 ve 6:3 D3 yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp yok; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:1 bölüm açılışı (sûre açılışı); 6:3 şahıs geçişi 3 → 2; 6:4 şahıs geçişi 2 → 3; 6:2 ve 6:5 şahıs geçişi yok (baskın 3); edim geçişi yok (bütün ayetler haber)",
 "sözdizimi (okuma; morph etiketiyle): 6:1 'el-hamdu li'llâh' — haber öne alınmamış isim cümlesi; 'llezî xalaqa' — ilgi cümlesi (morph REL); 'summe'llezîne keferû … ya'dilûn' — atıf ve ilgi (morph CONJ + REL); "
 "6:2 'huve'llezî' — isim cümlesi; 've ecelun musemmen 'indehû' — istînâf (morph REM); 6:3 've huve'llâhu fi's-semâvâti' — isim cümlesi; 6:4 'mâ … illâ' — olumsuzluk ve istisna (morph NEG + RES); "
 "6:5 'fe-qad' — sonuç ve tekit (morph RSLT + CERT); 'lemmâ' — zaman (morph T); 'fe-sevfe' — gelecek (morph RSLT + FUT)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:1 'el-hamdu li'llâh' ile açılıyor (sayım: 'say 6:1 1-2'); "
 "6:1 'z-zulumâti' / 'n-nûra' karşıtlığı; 6:2 kök أجل ikilemesi ('ecelen' / 've ecelun'); 6:3 kök علم ikilemesi ('ya'lemu' / 've ya'lemu'); "
 "6:4 've mâ te'tîhim min âyetin min âyâti rabbihim illâ kânû 'anhâ mu'ridîn' — 36:46 ile eş (sayım: 'say 6:4 1-7 --on'); 6:5 'mâ kânû bihî yestehzi'ûn' — 26:6 ile eş (sayım: 'say 6:5 9-12')",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 01'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7): "
 "'âyetin min âyâti rabbihim' 6:4 'Rablerinin âyetlerinden kendilerine hiçbir âyet gelmez ki ondan yüz çeviriyor olmasınlar' / 36:46 'Rablerinin âyetlerinden kendilerine hiçbir âyet gelmez ki ondan yüz çeviriyor olmasınlar' (emsal metninde) — çakışma değil; "
 "'kezzebû bi'l-haqq' 6:5 'hak kendilerine geldiğinde onu yalanladılar' / 50:5 'hak kendilerine geldiğinde onu yalanladılar' (emsal metninde) — çakışma değil; "
 "'mâ kânû bihî yestehzi'ûn' 6:5 'alay ettikleri şeyin haberleri onlara gelecek' / 26:6 'alay ettikleri şeyin haberleri onlara gelecek' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18): 6:4 'te'tî' IMPF IND — meal geniş zaman olumsuz 'gelmez'; 6:5 'sevfe ye'tî' — meal gelecek zaman 'gelecek', kip değişimi yok; 6:4 'mu'ridîn' ortaç — meal 'yüz çeviriyor olmasınlar' (36:46 emsal biçimi; bölüm 16 denetimi kuralı 9)",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or ''),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 1 5 01'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:1, 6:2, 6:3, 6:4 ve 6:5 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:1 ('z-zulumâti' / 'n-nûra'); 6:3 ('sirrakum' / 'cehrakum'); 6:2, 6:4 ve 6:5 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök خلق 6:1 ('xalaqa') ve 6:2 ('xalaqakum') — yaratılış bağı; kök أتي 6:4 ('te'tîhim') ve 6:5 ('ye'tîhim') — gelme bağı; kök كون 6:4 ('kânû') ve 6:5 ('kânû'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 1-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm iki blok (1, 2); bu blok bölümü ve sûreyi açıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b01/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 1 5 01'; lem_bozuk.py 01 çıktısı): 6:2:14 'yemteru' — lem_bozuk bayrağı; meal maddesinde '(morph LEM ham biçim)' notlu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 1 5 → AYN_SONUC; sunum/bolum4_kurallar.py 1 5 01 → KHATA_HEPSI; sunum/bolum5_kurallar.py 1 5 01 → B5_HEPSI; sunum/bolum6_kurallar.py 1 5 01 → B6_HEPSI; sunum/bolum7_kurallar.py 1 5 01 → B7_HEPSI; sunum/bolum8_kurallar.py 1 5 01 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 1 5 01 → B9_HEPSI; sunum/bolum10_kurallar.py 1 5 01 → B10_HEPSI; sunum/bolum11_kurallar.py 1 5 01 → B11_HEPSI; sunum/bolum12_kurallar.py 1 5 01 → B12_HEPSI; sunum/bolum13_kurallar.py 1 5 01 → B13_HEPSI; sunum/bolum14_kurallar.py 1 5 01 → B14_HEPSI; sunum/bolum15_kurallar.py 1 5 01 → B15_HEPSI; sunum/bolum16_kurallar.py 1 5 01 → B16_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 1 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('ellezî', 'xalaqa', 'semâ'', 'ard', 'mâ', 'kâne', 'istuhzi'e'); lemmasız öğe joker '_' ('huve', 'bi'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (1, 5): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_1_5.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01',):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()
GERI = open('/home/claude/yamalar/geriye_donuk_5_hazirlik6.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '1', '5'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '1', '5', '01'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '1', '5', '01'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '1', '5', '01', '--tazelik-yok')}
    for _n in range(7, 17): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '1', '5', '01')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16 = [_R['B%d' % _n].splitlines() for _n in range(6, 17)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
