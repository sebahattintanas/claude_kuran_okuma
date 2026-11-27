# sûre 7 bölüm 7 kapanış denetimi araç kuralları (bekleyen_ariza_7_b20.txt 2. öğe) — salt okur:
#  (1) EMSAL_KALIP_BAG_ESIT: bag kaydı harekesiz kalıplı her emsal için meal maddesinde kalıbı bag kalıbıyla bayt eşit emsal satırı var; yoksa o emsalin satırında 'daraltılmış kalıp' notu (gerekçeyle)
#  (2) KOK1041_ONCEKI_TAM: aday 1041 maddesindeki 'bölümün önceki blok… ortak kökler' listesi, bu bloğun morph ROOT kümesiyle bölümün önceki bloklarının morph ROOT kümesi kesişimini eksiksiz taşır
#  (3) EMSAL_ES_ARASI_NOT: bir kalıp için iki ya da daha çok emsal satırı varsa ve emsal alıntıları birbirinden farklıysa maddede 'emsaller arası' notu (fark adıyla)
#  (4) ESMA_UYUSMAZ_MUHUR_EL: ◇'de 'uyuşmuyor' taşıyan esma_kayit cümlesi muhur_el durumunu anar
#  (5) FE_SONUC_REM: ARIZA'da "sonuç 'fe'si" gerekçesi varken karşılıklı (karşılıksız değil) morph REM 'fe' için "'fe' N. kelime morph REM — anlamca sonuç" notu
# kullanım (/home/claude'dan): python3 sunum/bolum43_kurallar.py A B NN
import re, sys, ast, os, collections
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK, S
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
TUM = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')[(A, B)]
ITEMS = [m for m in TUM if not re.match(r'(bölüm (denetimi \(|\d+ denetiminden)|devir \()', m)]
M, MEAL = {}, {}
exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'M': M, 'MEAL': MEAL})
EN = collections.Counter()
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
Q = r"(?<![^\s(\[])'((?:[^']|(?<=[A-Za-zâîûçğışöüÂÎÛ])'(?=[a-zâîûçğışöü]))+)'"
MI = (item('meal (okuma') or [''])[0]
EMI = MI.split('emsal meal karşılık farkları', 1)[1].split('kip notu (', 1)[0] if 'emsal meal karşılık farkları' in MI else ''
SAT = []  # (kalıp, ayet, emsal, emsal alıntısı, satır metni)
for m in re.finditer(Q + r" %d:(\d+) " % S + Q + r" / (\d+:\d+) " + Q + r" \(emsal metninde\) — ([^;]*)", EMI):
    SAT.append((m.group(1), int(m.group(2)), m.group(4), m.group(5), m.group(0)))
def roots(nn):
    f_ = _BK + 'b%02d/morph.txt' % nn
    return set(re.findall(r'ROOT:([^|\s+]+)', open(f_, encoding='utf-8').read())) if os.path.exists(f_) else set()

# ── (1) EMSAL_KALIP_BAG_ESIT ──
_bf = Y + 'bag_%d_%d_%d.txt' % (S, A, B)
if os.path.exists(_bf):
    for b_ in ast.literal_eval('[' + open(_bf, encoding='utf-8').read() + ']'):
        e = b_['bag'].split(' → ')[0]
        hm = re.search(r"harekesiz " + Q, b_.get('kural', ''))
        if not hm: continue
        EN['bag_kalip'] += 1
        sat = [s_ for s_ in SAT if s_[2] == e]
        if not sat or any(s_[0] == hm.group(1) for s_ in sat) or any('daraltılmış kalıp' in s_[4] for s_ in sat): continue
        H.append("(1) bag %s kalıbı '%s' — emsal satırı daraltılmış ('%s'), 'daraltılmış kalıp' notu yok" % (b_['bag'], hm.group(1)[:50], "' / '".join(s_[0] for s_ in sat)[:60]))

# ── (2) KOK1041_ONCEKI_TAM ──
BI = ' '.join(item('bölüm:'))
mb = re.search(r'bölüm blokları ([\d, ve]+)', BI)
onc = [int(x) for x in re.findall(r'\d+', mb.group(1))] if mb else []
onc = [x for x in onc if x < int(NN)]
if onc:
    kes = roots(int(NN)) & set().union(*[roots(x) for x in onc])
    AD = ' '.join(item('aday 1041'))
    mo = re.search(r'bölümün önceki blo\w+ ortak kökler: (.*?)(?:; okuma|$)', AD)
    yaz = set(re.findall(r'([ء-ي]+) \(', mo.group(1))) if mo else set()
    EN['kok1041'] += len(kes)
    eks = sorted(kes - yaz)
    if eks: H.append("(2) aday 1041 önceki bloklarla ortak kök eksik: %s" % ', '.join(eks))

# ── (3) EMSAL_ES_ARASI_NOT ──
_g = collections.defaultdict(dict)
for kal, n, e, y, _ in SAT: _g[(n, kal)][e] = y
for (n, kal), d in sorted(_g.items()):
    if len(d) < 2: continue
    EN['es_arasi'] += 1
    if len(set(d.values())) > 1 and 'emsaller arası' not in EMI:
        H.append("(3) %d:%d '%s' emsal alıntıları farklı (%s) — 'emsaller arası' notu yok" % (S, n, kal[:40], ', '.join(sorted(d))))

# ── (4) ESMA_UYUSMAZ_MUHUR_EL ──
for n in range(A, B + 1):
    d = M.get(n, '').split('\n')[0]
    for m in re.finditer(r"esma_kayit çıktısı .*?(?:\.(?= [A-ZÖÇŞİÜĞ]|$))", d):
        if 'uyuşmuyor' not in m.group(0): continue
        EN['esma_uyusmaz'] += 1
        if 'muhur_el' not in m.group(0): H.append("(4) %d:%d esma_kayit 'uyuşmuyor' cümlesinde muhur_el durumu yok" % (S, n))

# ── (5) FE_SONUC_REM ──
if any("sonuç 'fe'si" in m for m in ITEMS):
    _vf = _BK + 'b%s/yap/veri.py' % NN
    MK = {}
    if os.path.exists(_vf): exec(open(_vf, encoding='utf-8').read(), {}, _d := {}); MK = _d.get('MK', {})
    for a_, L in sorted(MK.items()):
        for tr_, q_, its in L:
            for x in its:
                m = re.match(r"'fe' (\d+)\. kelimede '[^']+' ile \(morph REM\)", x)
                if not m: continue
                EN['fe_rem'] += 1
                if not any("'fe' %s. kelime morph REM — anlamca sonuç" % m.group(1) in it for it in ITEMS):
                    H.append("(5) %d:%d %s. kelime 'fe' morph REM karşılıklı — \"sonuç 'fe'si\" gerekçesine karşın 'anlamca sonuç' notu yok" % (S, a_, m.group(1)))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum43_kurallar hata: %d' % len(H))
