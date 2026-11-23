# sûre 6 blok 31 (6:131-135) ARIZA oluşturucu — bölüm 15-3
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b31/olcum.txt'
os.environ['SAY2'] = '/home/claude/b31/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Ölüyken dirilen; cin ve insan toplulukları'"


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
 ("6:135", "'inne lâ eflaha zâlim'", 2, 'say 6:135 15-18', "harekesiz 'innehû lâ yuflihu'z-zâlimûn' (15-18. kelime)", None),
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

VF_YAZI = {131: {9: "'ve ehluhâ'"}, 132: {1: "'ve li-kullin'", 5: "'ve mâ'"}, 133: {1: "'ve rabbuke'", 8: "'ve yestaxlif'"}, 134: {5: "'ve mâ'"}, 135: {}}
sys.path.insert(0, '/home/claude/b31/yap')
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
open('/home/claude/b31/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '31')
BLOKLAR = [str(i) for i in range(1, 32)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '31', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b31/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '131', '135', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b31/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b31/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '131', '135', '31').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_131_135.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:131', '6:132', '6:133', '6:134', '6:135'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_131_135.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(131, 136))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:131 kök هلك ('muhlike' 6. kelime — helâk); 6:133 kök بعد ('ba'dikum' 10. kelime — sonra), kök أخر ('âxarîn' 18. kelime — başka): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '131', '135', '31')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b31/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 32)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(131, 136))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 14 kapanışında sunum/bolum30_kurallar.py eklendi (kural 1-5), bolum19 KURAL_ATIF bölüm 14, sunum/geriye_donuk.py bolum30 satırı, sunum/mutasyon_sina.py b30 sınamaları; blok 30'da sunum/bolum19_kurallar.py CERCEVE listesine 'tamlama içinde ad, göndergesi Allah' etiketi eklendi — bölüm 19 kuralı 5; bu blokta araç değişikliği yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 298",
 "geriye dönük koşu (bölüm 14 kapanışı, komut 'python3 sunum/geriye_donuk.py b28k yamalar/geriye_donuk_6_b26k.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 131 135 31'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:133 've rabbuke'l-ğaniyyu' (1-2. kelime) — esma_el 'ilahi', kural ''ve'llâhu X' kuralı' (Rab; 've rabbuke X' kalıbı) (yamalar/esma_el_6_131_135.txt); غَنِيّ lemması sûre 6'da bu blokta; 6:131, 6:132, 6:134 ve 6:135 esmâ yok; "
 "6:131 Rab (5. kelime), 6:132 Rab (6. kelime), 6:133 Rab (1. kelime); blokta lafız yok; 6:134 ve 6:135 lafız ve Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 131 135 31'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:131 '{{1|aktör: adsız `karye` 7\\. sırada}}', '{{1|fâsıla غفلون → ن, N sınıfı}}', '{{1|harf 38 → harf3 37, isaret 1}}' ve '{{1|dış düğüm 2}}'; "
 "6:132 '{{2|fâsıla يعملون → ن, N sınıfı}}', '{{2|harf 39 → harf3 35, isaret 4}}' ve '{{2|dış düğüm 3}}'; 6:133 '{{3|esmâ غَنِيّ 2\\. sırada, ORTA konum, MÜHÜRSÜZ}}', '{{3|fâsıla ءاخرين → ن, N sınıfı}}', '{{3|simetri \\[4, 3, 9, 1\\]}}', '{{3|harf 74 → harf3 72, isaret 2}}' ve '{{3|dış düğüm 0}}'; "
 "6:134 '{{4|EDİLGEN 1/1 fiil, pas z=5,38}}', '{{4|fâsıla بمعجزين → ن, N sınıfı}}', '{{4|simetri \\[3, 1, 5, 1\\]}}', '{{4|harf 30 → harf3 28, isaret 2}}' ve '{{4|dış düğüm 0}}'; "
 "6:135 '{{5|fâsıla ٱلظلمون → ن, N sınıfı}}', '{{5|simetri \\[3, 4, 8, 1\\]}}', '{{5|harf 78 → harf3 72, isaret 6}}' ve '{{5|dış düğüm 4}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 131 135 31'): KALAN_P",
 "ölçüm aktör: 6:131 adsız `karye` 7. sırada ('l-qurâ'); 6:132, 6:133, 6:134 ve 6:135 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:131 haber — NEG 1 'lem' (3.); 6:132 haber — NEG 1 'mâ' (5.); 6:133 şart — COND 1 'in' (5.); "
 "6:134 haber — EMPH 1 'le-ât' (4.), NEG 1 'mâ' (5.); 6:135 emir, nida — IMPV 2 'qul' (1.), ''melû' (3.), VOC 1 'yâ qavmi' (2.), FUT 1 'fe-sevfe' (8.), NEG 1 'lâ' (16.); "
 "morph CIRC ('ve ehluhâ' 6:131 9.), SUB ('en' 6:131 2., 'kemâ' 6:133 13.), REM ('ve li-kullin' 6:132 1., 've mâ' 6:134 5., 'fe-sevfe' 6:135 8.), ACC ('inne' 6:134 1., 'innî' 6:135 6., 'innehû' 6:135 15.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:131 ★ (kaynak rab, z=1,81); 6:132 ★★ (kaynak rab, z=2,05); 6:134 ★★★ (kaynak pas, z=5,38); 6:133 ve 6:135 yıldız yok",
 "fâsıla: 6:130 ن → 6:131 ن (غفلون) → 6:132 ن (يعملون) → 6:133 ن (ءاخرين) → 6:134 ن (بمعجزين) → 6:135 ن (ٱلظلمون) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:131 28:59 (emsal olarak basıldı), 11:117 (emsal olarak basıldı); 6:132 46:19 (emsal olarak basıldı), 11:123 (emsal olarak basıldı), 27:93 (emsal olarak basıldı); 6:133 xref yok; 6:134 xref yok; 6:135 39:39 (emsal olarak basıldı), 11:93 (emsal olarak basıldı), 11:121 (emsal olarak basıldı), 28:37 (emsal olarak basıldı)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:135 'inne lâ eflaha zâlim' süzgeç GEÇER; 6:131, 6:132, 6:133 ve 6:134 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:131 muhatap 2MS ('rabbuke' eki), 3MS ('yekun' — fiil uyumu, fail 5. kelime), 3FS ('ehluhâ' eki — gönderge 'l-qurâ' 7. kelime); 6:132 3MP (''amilû', 'ya'melûn' — gönderge 'li-kullin' 1. kelime), muhatap 2MS ('rabbuke' eki); "
 "6:133 muhatap 2MS ('rabbuke' eki), 3MS ('yuzhibkum', 've yestaxlif', 'yeşâ'u', 'enşe'ekum' ve 6. kelime — gönderge 'rabbuke' 1. kelime), muhatap 2MP ('yuzhibkum', 'ba'dikum', 'enşe'ekum' ekleri); 6:134 muhatap 2MP ('tû'adûne' — edilgen, naib-i faili; 'entum'); "
 "6:135 muhatap 2MS ('qul'), konuşan 1S ('yâ qavmi', 'innî' — söz içi), muhatap 2MP (''melû', 'mekânetikum', 'ta'lemûne' — söz içi), 3FS ('tekûnu' — fiil uyumu, fail 13. kelime), 3MS ('lehû' — gönderge 'men' 10. kelime; 'innehû' — zamir-i şan; 'yuflihu' — fiil uyumu, fail 18. kelime)",
 "6:131-135 gönderge zinciri: 6:131 'zâlike' 6:130 elçi gönderme ve şahitliğe işaret (okuma)",
 "edilgen: 6:134 'tû'adûne' (3. kelime; naib-i faili muhatap 2MP) — ölçüm EDİLGEN 1/1 bu kelimeden",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:135 'qul' (1.) ardından söz 2-18. kelime — ayet sonuna kadar; REM sapması 6:135 (8. kelime) — 'fe-sevfe' söz içinde yeni cümle başı, söz devam ediyor (gerekçe: morph REM, 'qul' sözü 18. kelimede kapanır); 6:131, 6:132, 6:133 ve 6:134 söz yok — söz fiili yok (okuma); mealde 'De ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 131 135 31' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:131 've ehluhâ' (9.) CIRC; 6:132 've li-kullin' (1.) REM, 've mâ' (5.) CONJ; 6:133 've rabbuke' (1.), 've yestaxlif' (8.) CONJ; 6:134 've mâ' (5.) REM; 6:135 'fe-sevfe' (8.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:131, 6:132, 6:133, 6:134 ve 6:135 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 131 135 31'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:131 (28:59, 11:117), 6:132 (46:19, 11:123, 27:93), 6:135 (39:39, 11:93, 11:121, 28:37); 6:133 ve 6:134 bağ yok; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:131 şahıs geçişi yok, edim geçişi soru, nida → haber; 6:132 şahıs geçişi yok, edim geçişi yok; 6:133 şahıs geçişi yok, edim geçişi haber → şart; "
 "6:134 şahıs geçişi 3 → 2, edim geçişi şart → haber; 6:135 söz açılır (2. kelime), şahıs geçişi yok, edim geçişi haber → emir, nida; bölüm kapanışı; "
 "ölçüm iltifât 6:131-135 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:131 'zâlike en lem yekun' — gerekçe işareti ve olumsuz masdar (morph DEM + SUB + NEG); 6:132 've mâ rabbuke bi-ğâfilin' — atıf ve olumsuz isim cümlesi (morph CONJ + NEG); 6:133 'yuzhibkum ve yestaxlif' — şart cevabı ve atıf (morph CONJ); "
 "6:134 'inne mâ tû'adûne le-ât' — pekiştirmeli haber (morph ACC + EMPH); 6:135 'fe-sevfe ta'lemûne' — gelecek bildirimi (morph REM + FUT)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:131 5-6. kelime — 28:59 ile harekesiz eş (sayım: 'say 6:131 5-6'); 6:131 7-8. kelime — 11:117 ile harekesiz eş (sayım: 'say 6:131 7-8'); 6:132 1-2. kelime — 46:19 ile harekesiz eş (sayım: 'say 6:132 1-2'); 6:132 6-7. kelime — 11:123 ve 27:93 ile harekesiz eş (sayım: 'say 6:132 6-7'); 6:135 4-5. kelime — 11:93, 11:121 ve 39:39 ile harekesiz eş (sayım: 'say 6:135 4-5'); 6:135 13-14. kelime — 28:37 ile harekesiz eş (sayım: 'say 6:135 13-14'); "
 "6:132 kök عمل ikilemesi; 6:133 kök شيأ ikilemesi; 6:135 kök عمل, كون ikilemeleri",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 31'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'rabbuke muhlike' 6:131 'Rabbinin şehirleri zulümle helâk edici' / 28:59 'Rabbin, ana şehirlerine, âyetlerimizi onlara okuyan bir elçi göndermedikçe şehirleri helâk edici' (emsal metninde) — çakışma — tam okuma sonu (bağlam karşılığı); 'l-qurâ bi-zulm' 6:131 'şehirleri zulümle' / 11:117 'şehirleri haksız yere' (emsal metninde) — çakışma — tam okuma sonu (bağlam karşılığı); 've li-kullin derecât' 6:132 'Herkes için yaptıklarından dereceler' / 46:19 'Herkes için yaptıklarından dereceler' (emsal metninde) — çakışma değil (bayt eşit); 'rabbuke bi-ğâfil' 6:132 'Rabbin, yaptıklarından gafil' / 11:123 'Rabbin yaptıklarınızdan gafil' (emsal metninde) — çakışma — tam okuma sonu (bağlam karşılığı); 'rabbuke bi-ğâfil' 6:132 'Rabbin, yaptıklarından gafil' / 27:93 'Rabbin yaptıklarınızdan habersiz' (emsal metninde) — çakışma — tam okuma sonu (bağlam karşılığı); ''alâ mekânetikum' 6:135 'konumunuza göre' / 11:93 'elinizden geleni' (emsal metninde) — çakışma — tam okuma sonu (bağlam karşılığı); ''alâ mekânetikum' 6:135 'konumunuza göre' / 11:121 'Elinizden geleni' (emsal metninde) — çakışma — tam okuma sonu (bağlam karşılığı); ''alâ mekânetikum' 6:135 'konumunuza göre' / 39:39 'Bulunduğunuz konuma göre' (emsal metninde) — çakışma — tam okuma sonu (bağlam karşılığı); ''âqibetu'd-dâr' 6:135 'Yurdun sonunun' / 28:37 'dünya yurdunun sonunun' (emsal metninde) — çakışma — tam okuma sonu (bağlam karşılığı); 'innehû lâ yuflihu'z-zâlimûn' 6:135 'zalimler kurtuluşa eremez' / 28:37 'Zalimler kurtuluşa eremez' (emsal metninde) — çakışma — tam okuma sonu (cümle başı yazımı); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:131 'yekun' IMPF JUS ('lem' ile) — meal 'olmaması'; 6:132 ''amilû' PERF — meal 'yaptıklarından'; 'ya'melûn' IMPF IND — meal 'yaptıklarından'; "
 "6:133 'yeşe'' IMPF JUS (şart) — meal 'Dilerse'; 'yuzhib' IMPF JUS (cevap) — meal 'giderir'; 'yestaxlif' IMPF JUS — meal 'kılar'; 'yeşâ'u' IMPF IND — meal 'dilediğini'; 'enşe'e' PERF — meal 'ettiği'; "
 "6:134 'tû'adûne' IMPF IND edilgen — meal 'vaat edilen'; "
 "6:135 'qul' IMPV — meal 'De'; ''melû' IMPV — meal 'yapın'; 'ta'lemûne' IMPF IND ('sevfe' ile) — meal 'bileceksiniz'; 'tekûnu' IMPF IND — meal 'olacağını'; 'yuflihu' IMPF IND ('lâ' ile) — meal 'eremez'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 131 135 31'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:131, 6:132, 6:133, 6:134 ve 6:135 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:131, 6:132, 6:133, 6:134 ve 6:135 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök ربب 6:131 ('rabbuke'), 6:132 ('rabbuke') ve 6:133 ('rabbuke'); kök غفل 6:131 ('ğâfilûn') ve 6:132 ('bi-ğâfilin'); kök عمل 6:132 (''amilû', 'ya'melûn') ve 6:135 (''melû', ''âmil'); kök كون 6:131 ('yekun') ve 6:135 ('mekânetikum', 'tekûnu'); kök ظلم 6:131 ('bi-zulmin') ve 6:135 ('z-zâlimûn'); kök قوم 6:133 ('qavmin') ve 6:135 ('yâ qavmi'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 15-3 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 29, 30 ve 31; bölüm kapanışı bu blokta; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b31/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 131 135 31'; lem_bozuk.py 31 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 131 135 → AYN_SONUC; sunum/bolum4_kurallar.py 131 135 31 → KHATA_HEPSI; sunum/bolum5_kurallar.py 131 135 31 → B5_HEPSI; sunum/bolum6_kurallar.py 131 135 31 → B6_HEPSI; sunum/bolum7_kurallar.py 131 135 31 → B7_HEPSI; sunum/bolum8_kurallar.py 131 135 31 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 131 135 31 → B9_HEPSI; sunum/bolum10_kurallar.py 131 135 31 → B10_HEPSI; sunum/bolum11_kurallar.py 131 135 31 → B11_HEPSI; sunum/bolum12_kurallar.py 131 135 31 → B12_HEPSI; sunum/bolum13_kurallar.py 131 135 31 → B13_HEPSI; sunum/bolum14_kurallar.py 131 135 31 → B14_HEPSI; sunum/bolum15_kurallar.py 131 135 31 → B15_HEPSI; sunum/bolum16_kurallar.py 131 135 31 → B16_HEPSI; sunum/bolum17_kurallar.py 131 135 31 → B17_HEPSI; sunum/bolum18_kurallar.py 131 135 31 → B18_HEPSI; sunum/bolum19_kurallar.py 131 135 31 → B19_HEPSI; sunum/bolum20_kurallar.py 131 135 31 → B20_HEPSI; sunum/bolum21_kurallar.py 131 135 31 → B21_HEPSI; sunum/bolum22_kurallar.py 131 135 31 → B22_HEPSI; sunum/bolum23_kurallar.py 131 135 31 → B23_HEPSI; sunum/bolum24_kurallar.py 131 135 31 → B24_HEPSI; sunum/bolum25_kurallar.py 131 135 31 → B25_HEPSI; sunum/bolum26_kurallar.py 131 135 31 → B26_HEPSI; sunum/bolum27_kurallar.py 131 135 31 → B27_HEPSI; sunum/bolum28_kurallar.py 131 135 31 → B28_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 31 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('inne', 'lâ', 'eflaha', 'zâlim', 'kâne', 'rabb', 'muhlik', 'qarye', ''amile', ''alâ', 'mekânet', ''âmil', 'qavm', 'sevfe', ''alime', 'men', 'qâle'); joker '_' kullanılmadı; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (131, 135): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_131_135.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b28k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '131', '135'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '131', '135', '31'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '131', '135', '31'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '131', '135', '31', '--tazelik-yok')}
    for _n in range(7, 31): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '131', '135', '31')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30 = [_R['B%d' % _n].splitlines() for _n in range(6, 31)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
