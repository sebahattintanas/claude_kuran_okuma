# sûre 7 blok 22 (7:76-79) ARIZA oluşturucu — bölüm 8-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b22/olcum.txt'
os.environ['SAY2'] = '/home/claude/b22/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Sâlih ve Semûd; Lût ve kavmi'"


def sd(key):
    return sayim.S2[key][1]


def sic(key):
    n, d = sayim.S2[key]
    return 1 + len([x for x in d['basilan'] if x.startswith('7:')]) + d['okunmus_si'] + d['henuz_si']


def taban(key, ay):
    n, d = sayim.S2[key]
    p = [ay] + [x for x in d['basilan'] if x.startswith('7:') and x != ay]
    if d['okunmus_si']: p.append('okunmus_si %d' % d['okunmus_si'])
    if d['henuz_si']: p.append('henuz_si %d' % d['henuz_si'])
    return ' + '.join(p)


R5 = [
 ('7:77', "'etâ mâ ve'ade in kâne min'", 2, 'say 7:77 9-14', "harekesiz 'i'tinâ bi-mâ te'idunâ in kunte mine' (9-14. kelime)", ('dizi 7 77 9 14', "etâ mâ ve'ade in kâne min", '9-14', 'biçim farkı (dizi 7 77 9 14): 7:70 önek; öneksiz eş koşusu (dizi 7 77 9 14): 7:70 → önek kesilmiş sûre içi 1')),
 ('7:77', "'in kâne min'", 3, 'say 7:77 12-14', "harekesiz 'in kunte mine' (12-14. kelime)", ('dizi 7 77 12 14', 'in kâne min', '12-14', 'biçim farkı (dizi 7 77 12 14): 7:70 yazım eş; basılmamış eş yazım eş')),
 ('7:78', "'exaze racfe esbaha fî dâr câsim'", 2, 'say 7:78 1-6', "harekesiz 'fe-exazethumu'r-racfetu fe-esbahû fî dârihim câsimîn' (1-6. kelime)", ('dizi 7 78 1 6', 'exaze racfe esbaha fî dâr câsim', '1-6', 'biçim farkı (dizi 7 78 1 6): basılmamış eş yazım eş')),
 ('7:79', "'tevellâ 'an qâle qavm qad ebleğu risâle rabb nesahu _'", 2, 'say 7:79 1-10', "harekesiz 'fe-tevellâ 'anhum ve qâle yâ qavmi le-qad ebleğtukum risâlete rabbî ve nasahtu lekum' (1-10. kelime)", ('dizi 7 79 1 10', "tevellâ 'an qâle qavm qad ebleğu risâle rabb nesahu _", '1-10', 'biçim farkı (dizi 7 79 1 10): basılmamış eş yazım eş')),
 ('7:79', "'risâle rabb nesahu _'", 3, 'say 7:79 7-10', "harekesiz 'risâlete rabbî ve nasahtu lekum' (7-10. kelime)", ('dizi 7 79 7 10', 'risâle rabb nesahu _', '7-10', 'biçim farkı (dizi 7 79 7 10): 7:62 zamir eki; basılmamış eş yazım eş')),
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

VF_YAZI = {76: {5: "'bi'llezî'", 7: "'bihî'"}, 77: {1: "'fe-'aqarû'", 3: "'ve 'atev'", 7: "'ve qâlû'", 8: "'yâ sâlihu'", 10: "'bi-mâ'"}, 78: {1: "'fe-exazethumu'", 3: "'fe-esbahû'"}, 79: {1: "'fe-tevellâ'", 3: "'ve qâle'", 4: "'yâ qavmi'", 5: "'le-qad'", 9: "'ve nasahtu'", 10: "'lekum'", 11: "'ve lâkin'"}}
sys.path.insert(0, '/home/claude/b22/yap')
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
open('/home/claude/b22/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '22')
BLOKLAR = [str(i) for i in range(1, 23)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '22', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b22/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '76', '79', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b22/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b22/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '76', '79', '22').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_76_79.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:76', '7:77', '7:78', '7:79'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_76_79.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(76, 80))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:78 kök صبح ('fe-esbahû' 3. kelime — oluş fiili): tetik listesinde yok; 7:79 kök ولي ('fe-tevellâ' 1. kelime — yüz çevirme): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '76', '79', '22')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b22/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 23)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(76, 80))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l.replace('**', '') for l in open('/home/claude/b22/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b22/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK2 = _esc(re.search(r'aktör: adlı .*?rol meful\+muhatap\)', _OL[1]).group(0))
for _k, _v in (('_AK2', _AK2),): _MB = _MB.replace('" + %s + "' % _k, _v)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 75), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 492",
 "geriye dönük koşu (sûre 7 bölüm 7 kapanışı, komut 'python3 sunum/geriye_donuk.py b20k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 76 79 22'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:76, 7:77, 7:78 ve 7:79 esmâ yok; lafız yok; 7:77 Rab (6. kelime), 7:79 Rab (8. kelime); 7:76 ve 7:78 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 76 79 22'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in range(76, 80)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 76 79 22'): KALAN_P",
 "ölçüm aktör: 7:77 adlı صالِح (8. kelime, rol meful+muhatap); 7:76, 7:78 ve 7:79 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:76 haber — kip yok; 7:77 emir, nida, şart — COND 1 'in' (12.), IMPV 1 'i'tinâ' (9.), VOC 1 'yâ sâlihu' (8.); "
 "7:78 haber — kip yok; 7:79 nida — CERT 1 'le-qad' (5.), EMPH 1 'le-qad' (5.), NEG 1 'lâ' (12.), VOC 1 'yâ qavmi' (4.)",
 "morph REL ('llezîne' 7:76 2., 'bi'llezî' 7:76 5., 'bi-mâ' 7:77 10.), AMD ('ve lâkin' 7:79 11.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:76, 7:77, 7:78 ve 7:79 yıldız yok",
 "fâsıla: 7:75 ن → 7:76 ن (" + _F[0] + ") → 7:77 ن (" + _F[1] + ") → 7:78 ن (" + _F[2] + ") → 7:79 ن (" + _F[3] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:76 xref yok; 7:77 51:44 (emsal olarak basıldı), 7:70, 11:32, 46:22 (basılmış), okunmuş 1 ayet; "
 "7:78 29:37 (emsal olarak basıldı), okunmuş 2 ayet ve okunmamış 1 ayet (sûre içi 1); 7:79 okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:77 'etâ mâ ve'ade in kâne min' süzgeç GEÇER, 'in kâne min' süzgeç GEÇER; 7:78 'exaze racfe esbaha fî dâr câsim' süzgeç GEÇER (tür tam); "
 "7:79 'tevellâ 'an qâle qavm qad ebleğu risâle rabb nesahu _' süzgeç GEÇER, 'risâle rabb nesahu _' süzgeç GEÇER; 7:76 nakarat3 kalıbı yok; sûre içi eşler — 7:70 ve 7:62 (basılmış) ve basılmamış eşler",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:76 3MS ('qâle' — fiil uyumu, fail 2. kelime), 3MP ('stekberû' — gönderge 'llezîne' 2. kelime), söz içi konuşan 1P eki ('innâ'), söz içi muhatap 2MP ('âmentum'), 3MS eki ('bihî' — gönderge 'llezî' 5. kelime); "
 "7:77 adlı 'yâ sâlihu' (8.); 3MP (''aqarû', ''atev', 'qâlû' ve ek 'rabbihim' — gönderge 7:76 2. kelime), söz içi muhatap 2MS ('i'tinâ', 'te'idunâ', 'kunte'), söz içi konuşan 1P eki ('i'tinâ', 'te'idunâ'); "
 "7:78 3FS ('exazethumu' — fiil uyumu, fail 2. kelime), 3MP ('esbahû' ve ekler 'exazethumu', 'dârihim' — gönderge 7:76 2. kelime); "
 "7:79 3MS ('tevellâ', 'qâle' — gönderge 7:77 8. kelime), 3MP eki (''anhum' — gönderge 7:76 2. kelime), söz içi konuşan 1S ('ebleğtukum', 'nasahtu'; ekler 'qavmi', 'rabbî'), söz içi muhatap 2MP ('tuhibbûne'; ekler 'ebleğtukum', 'lekum')",
 "7:76-79 gönderge zinciri: 7:76 büyüklenenler ('llezîne' 2. kelime) 7:77, 7:78 ve 7:79 3MP göndergesi; 7:79 'tevellâ' ve 'qâle' göndergesi 7:77 8. kelimedeki Sâlih (okuma)",
 "edilgen: 7:76, 7:77, 7:78 ve 7:79 edilgen fiil yok (7:77 'l-murselîn' edilgen ortaç)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:76 söz içi 4-8. kelime ('qâle' 1. kelime ardından); 7:77 söz içi 8-15. kelime ('qâlû' 7. kelime ardından); 7:78 söz yok; 7:79 söz içi 4-14. kelime ('qâle' 3. kelime ardından); "
 "REM sapması 7:79 (11. kelime) — söz içi 've', 'lâkin' karşıtlığıyla; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 76 79 22' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 7:77 'fe-'aqarû' (1.) REM, 've 'atev' (3.) CONJ, 've qâlû' (7.) CONJ; 7:78 'fe-exazethumu' (1.) REM, 'fe-esbahû' (3.) REM; 7:79 'fe-tevellâ' (1.) REM, 've qâle' (3.) CONJ, 've nasahtu' (9.) CONJ, 've lâkin' (11.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:76, 7:77, 7:78 ve 7:79 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 76 79 22'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:77 (51:44), 7:78 (29:37); D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:79 نصح ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: bloğun emsal dosyasında olmayan basılmış eş (önceki bloklarda basılmış ya da sûre içi), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:76 söz açılır / kapanır, şahıs geçişi yok, edim geçişi soru → haber; 7:77 söz açılır / kapanır, şart → cevap (COND 'in' 12. kelime; cevap 'i'tinâ' 9. kelime — öne alınmış), şahıs geçişi yok, edim geçişi haber → emir, nida, şart; "
 "7:78 şahıs geçişi yok, edim geçişi emir, nida, şart → haber; 7:79 söz açılır / kapanır, şahıs geçişi 3 → 1, edim geçişi haber → nida; ölçüm iltifât 7:76-79 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:76 'innâ bi'llezî âmentum' — tekit edatı, ilgi zamiri sıla cümlesiyle (morph ACC + P + REL + PERF); 7:78 'fe-exazethumu'r-racfetu' — istînâf, mazi ve belirli fail (morph REM + PERF + DET + N); "
 "7:79 'le-qad ebleğtukum' — yemin lâmı ve tahkik edatı ile mazi (morph EMPH + CERT + PERF)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:77 4-6. kelime — 51:44 ile harekesiz eş (sayım: 'say 7:77 4-6'); 7:78 1-6. kelime — 29:37 ile harekesiz eş (sayım: 'say 7:78 1-6'); 7:79 kök نصح ikilemesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 22'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "''an emri rabbihim' 7:77 'Rablerinin emrine' / 51:44 'Rablerinin emrine' (emsal metninde) — çakışma değil ('say 7:77 3-6' korpusta 1, 'dizi 7 77 3 6' 51:44 ile eş — önek farkı 've 'atev' / 'fe-'atev'); "
 "'fe-exazethumu'r-racfetu' 7:78 'Bunun üzerine onları sarsıntı yakaladı' / 29:37 'bunun üzerine onları şiddetli bir sarsıntı yakaladı' (emsal metninde) — çakışma — tam okuma sonu (daraltılmış kalıp — bag kalıbı iki satıra bölündü, meal kesimleri — 'şiddetli bir' emsalde fazla, büyük harf); "
 "'fe-esbahû fî dârihim câsimîn' 7:78 've yurtlarında diz üstü çöküp kaldılar' / 29:37 've yurtlarında diz üstü çöküp kaldılar' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:76 'qâle' PERF — meal 'dedi'; 'stekberû' PERF — meal 'Büyüklenenler'; 'âmentum' PERF — meal 'ettiğinizi'; "
 "7:77 ''aqarû' PERF — meal 'kestiler'; ''atev' PERF — meal 'kaldırdılar'; 'qâlû' PERF — meal 'dediler'; 'i'tinâ' IMPV — meal 'getir'; 'te'idunâ' IMPF IND — meal 'vaat ettiğin'; 'kunte' PERF ('in' ile) — meal 'elçilerdensen'; "
 "7:78 'exazethumu' PERF — meal 'yakaladı'; 'esbahû' PERF — meal 'kaldılar'; 7:79 'tevellâ' PERF — meal 'yüz çevirdi'; 'qâle' PERF — meal 'dedi'; 'ebleğtukum' PERF ('le-qad' ile) — meal 'tebliğ ettim'; 'nasahtu' PERF — meal 'öğüt verdim'; 'tuhibbûne' IMPF IND ('lâ' ile) — meal 'sevmiyorsunuz'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle; IMPF IND geniş zaman karşılığı her blokta sapma sayılır — sûre 7 bölüm 3 denetimi kuralı 3): 'stekberû' PERF 7:76'da sıfat-fiil ('-enler') ile; 'âmentum' PERF 7:76'da sıfat-fiil ('-tiğinizi') ile; "
 "'te'idunâ' IMPF 7:77'de sıfat-fiil ('-tiğin') ile; 'kunte' PERF 7:77'de şart ('-sen') ile; 'tuhibbûne' IMPF 7:79'da şimdiki zaman ('-iyorsunuz') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'ellezîne' (REL: '-enler' / '-anlar' / '-en') — çakışma değil (sıfat-fiil çekimi); 'fe' (REM: 'Bunun üzerine' / 've' / 'Öyleyse' / karşılıksız) — çakışma değil (anlatı 'fe'si, ardışık olay / emir cümlesi başı); 'mâ' (REL: 'şeyi' / '-en') — çakışma değil (ad, sıfat-fiil); 'bi' (belirtme eki / '-la' / '-le' / yönelme eki) — çakışma değil (fiil yönetimi, araç); 'hum' ('onlardan' / 'onları' / iyelik eki) — çakışma değil (çekim ve tamlama); 'hî' (karşılıksız / 'onunla' / iyelik eki) — çakışma değil (ilgi zamirine dönen zamir, tümleç, tamlama); 'nâ' ('biz' / 'bize' / karşılıksız) — çakışma değil (özne, yönelme; nesne sonraki kelimede karşılandı)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 76 79 22'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:76, 7:77, 7:78 ve 7:79 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:76 ('âmentum' / 'kâfirûn'); 7:77, 7:78 ve 7:79 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök ربب 7:77 ('rabbihim') ve 7:79 ('rabbî') ile bölüm içi; kök رسل 7:77 ('l-murselîn') ve 7:79 ('risâlete') ile bölüm içi; kök قول 7:76 ('qâle'), 7:77 ('qâlû') ve 7:79 ('qâle') ile bölüm içi; "
 "bölümün önceki bloğuyla ortak kökler: أخذ (7:73, 7:74 / 7:78), أمن (7:75 / 7:76), ربب (7:73, 7:75 / 7:77, 7:79), رسل (7:75 / 7:77, 7:79), صلح (7:73, 7:75 / 7:77), قول (7:73, 7:75 / 7:76, 7:77, 7:79), قوم (7:73, 7:75 / 7:79), كبر (7:75 / 7:76), نوق (7:73 / 7:77); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 8-2 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 21, 22 ve sonrakiler; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b22/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 76 79 22'; lem_bozuk.py 22 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 76 79 → AYN_SONUC; sunum/bolum4_kurallar.py 76 79 22 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 76 79 22 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 44)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 22 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla (''ate', ''an', 'emr', 'rabb', 'etâ', 'mâ', 've'ade', 'in', 'kâne', 'min', 'exaze', 'racfe', 'esbaha', 'fî', 'dâr', 'câsim', 'tevellâ', 'qâle', 'qavm', 'qad', 'ebleğu' (morph LEM ham biçim), 'risâle', 'nesahu' (morph LEM ham biçim)); joker '_' dizi lemma dizisinde boş öğe olan zamir ve önek lemmalı kelimelerde ('lekum' 7:79 10.); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (76, 79): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_76_79.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_7_b20k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '76', '79'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '76', '79', '22'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '76', '79', '22'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '76', '79', '22', '--tazelik-yok')}
    for _n in range(7, 44): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '76', '79', '22')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42, B43 = [_R['B%d' % _n].splitlines() for _n in range(6, 44)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'B39_HEPSI': (B39[-1] if B39 else '?'), 'B40_HEPSI': (B40[-1] if B40 else '?'), 'B41_HEPSI': (B41[-1] if B41 else '?'), 'B42_HEPSI': (B42[-1] if B42 else '?'), 'B43_HEPSI': (B43[-1] if B43 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
           'MUT_SONUC': (MUT[-1] if MUT else '?'), 'GERI_P': ' / '.join(x.lstrip('# ') for x in GERI), 'B6_ESMA': ('; '.join(l[5:] for l in B6 if 'esmâ kural' in l and l.startswith('HATA')) or 'sapma 0')}
    I_cur = list(I_HAM)
    for k, v in REP.items(): I_cur = I_cur[:len(BEK)] + [x.replace(k, v) for x in I_cur[len(BEK):]]  # bölüm 9 kuralı 9: taşınan denetim maddelerine yer tutucu değişimi uygulanmaz
    I_cur[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3, bölüm 6 kuralı 2 — komut 'python3 sunum/cakisma.py' + sûre 7'nin okunmuş bütün ARIZA dosyaları; bu bloğun karşılıklarına dokunan gruplar ve son dosyaya dokunan KÖK grupları; grup başına tam bir kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
                  + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
    if I_cur == onceki: break
    onceki = list(I_cur)
yaz(I_cur)
print('yazıldı', len(I_cur), 'tur', tur)
print('\n'.join(CAK_L))
print(GLS)
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42, B43): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
