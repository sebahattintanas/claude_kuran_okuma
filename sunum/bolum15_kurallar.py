# bölüm 15 (sûre 5) denetimi araç kuralları (bekleyen_ariza_5_b34.txt 2. öğe) — salt okur:
#  (1) ölçüm 'baskın' şahıs bir önceki ayetinkinden farklıysa A4'te 'şahıs geçişi X → Y'; bloğun başı bir önceki ayetin ölçümüyle karşılaştırılır
#  (2) A4'te 'söz sürüyor' yazılmaz; A3 'söz sürüyor (' açılış yerini 'S:N k. kelimeden' biçimiyle taşır; o ayette A4 'söz kapanır' 'ayet içi' kapsamı almaz
#  (3) A3'te ya da ARIZA söz maddesinde 'iç söz' N-M kaydı varsa A4'te 'söz açılır (N. kelime)'
#  (4) ARIZA söz maddesinde ayet için 'söz biçimli içerik' deniyorsa A3'te '(söz biçimli içerik'
#  (5) esma_muhur 'muhur EVET' ve ölçüm 'MÜHÜRSÜZ' olan ayette ◇ esma_kayit cümlesi ve ARIZA esma_kayit maddesi 'uyuşmuyor' der
#  (7) emsal meal notunda iki alıntı bayt eşit değilse karar 'çakışma — tam okuma sonu'; kalıpta fiil varsa emsal alıntısı ('X' (emsal metninde)) fiil karşılığını içerir — fiil karşılık sözcüğü bu ayetin meal kesiminden
#  (8) esma_el yorum alıntısı (' — ' öncesi) ◇ esma cümlesinde ve ARIZA esmâ maddesinde bayt eşit
#  (9) esma_el parantezinde 'sıfat' sözcüğü yalnız morph ADJ / PCPL kelimede
#  (14) '(emsal olarak basıldı)' önündeki hedef emsal olarak basılmış (bNN/ems.txt), blok ayeti değil
#  (15) es_edat 'tanınmayan' 0 (edat_etiket'e ekleme zorunlu)
#  (17) meal karşılık adının baş harfi mealdeki sözcükle eş büyüklükte (cümle başı dışında)
#  (19) ARIZA'da 'basilan satır sayısı (blok anı): N' kaydı; N ≤ basilan.txt satır sayısı
#  (kural 2 süren söz istisnası bolum13 (4)'te; kural 6 bolum14 (5)'te; kural 9 sınır eşleşmesi bolum6'da; kural 10 bolum5'te; kural 12 geriye_donuk'ta;
#   kural 13 elle — karar üyesi ile morph kelimesi eşlemesi betikle güvenilir değil; kurallar 11, 16 kullanıcı kararı; kural 18 elle)
# kullanım (/home/claude'dan): python3 sunum/bolum15_kurallar.py A B NN
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys, ast, glob, subprocess, collections, importlib.util as iu
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
TUM = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')[(A, B)]
ITEMS = [m for m in TUM if not re.match(r'bölüm (denetimi \(|\d+ denetiminden)', m)]
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
M, MEAL = {}, {}
exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'M': M, 'MEAL': MEAL})
DIA = {n: re.match(r"◇ '(.*?)' — ", M[n]).group(1) for n in range(A, B + 1)}
W = collections.defaultdict(lambda: collections.defaultdict(list))
for l in open('/home/claude/b%s/morph%d.txt' % (NN, S), encoding='utf-8'):
    loc, f, t, feat = l.rstrip('\n').split('\t'); s_, a_, w_, p_ = map(int, loc.split(':'))
    W[a_][w_].append((f, t, feat))
sp = iu.spec_from_file_location('veri', '/home/claude/b%s/yap/veri.py' % NN); veri = iu.module_from_spec(sp); sp.loader.exec_module(veri)
def satir(n, bas):
    for l in M[n].split('\n'):
        if l.startswith(bas): return l
    return ''
def a_parca(n, k):
    l = satir(n, '◈A'); m = re.search(r'\b%s (.*?)(?:; A%d |$)' % (k, int(k[1]) + 1), l)
    return m.group(1) if m else ''
def ayet_seg(it, n):  # maddenin 'S:n' ile başlayan kesimi (bir sonraki 'S:k ' anışına dek)
    m = re.search(r'(?<![\d:])%d:%d\b(.*?)(?=(?<![\d:])%d:\d+ (?!\(|kelime)|$)' % (S, n, S), it)
    return m.group(1) if m else ''
sys.path.insert(0, '/home/claude/calisma')
_cwd = _o.getcwd(); _o.chdir('/home/claude/calisma')
import olcum_bicim
def baskin(n):
    m = re.search(r'baskın (\d+)', olcum_bicim.olcum(S, n)); return m.group(1) if m else None
BAS = {n: baskin(n) for n in range(max(1, A - 1), B + 1)}
_o.chdir(_cwd)

# ── (1) şahıs geçişi ──
for n in range(A, B + 1):
    p, c = BAS.get(n - 1), BAS.get(n)
    if n == 1 or not p or not c or p == c: continue
    if not re.search(r'şahıs geçişi %s → %s' % (p, c), a_parca(n, 'A4')):
        H.append("(1) %d:%d A4'te 'şahıs geçişi %s → %s' yok (ölçüm baskın %d:%d %s, %d:%d %s)" % (S, n, p, c, S, n - 1, p, S, n, c))

# ── (2) süren söz ──
for n in range(A, B + 1):
    a3, a4 = a_parca(n, 'A3'), a_parca(n, 'A4')
    if 'söz sürüyor' in a4: H.append("(2) %d:%d A4'te 'söz sürüyor' — A4 kapalı listesinde yok" % (S, n))
    if 'söz sürüyor (' in a3:
        if not re.search(r"söz sürüyor \(%d:\d+ \d+\. kelimeden" % S, a3): H.append("(2) %d:%d A3 'söz sürüyor' açılış yerini ('S:N k. kelimeden') taşımıyor" % (S, n))
        if re.search(r'söz kapanır \(\d+\. kelime, ayet içi\)', a4): H.append("(2) %d:%d süren söz A4'te 'ayet içi' kapanıyor" % (S, n))

# ── (3) iç söz açılışı ──
SOZ = (item('söz / tırnak') or [''])[0]
for n in range(A, B + 1):
    kay = a_parca(n, 'A3') + ' ' + ayet_seg(SOZ, n)
    for m in {x.groups(): x for x in re.finditer(r'iç söz,? (\d+)-(\d+)\. kelime', kay)}.values():
        if not re.search(r'söz açılır \(%s\. kelime' % m.group(1), a_parca(n, 'A4')):
            H.append("(3) %d:%d iç söz %s-%s. kelime — A4'te 'söz açılır (%s. kelime)' yok" % (S, n, m.group(1), m.group(2), m.group(1)))

# ── (4) söz biçimli içerik ──
for n in range(A, B + 1):
    if 'söz biçimli içerik' in ayet_seg(SOZ, n) and '(söz biçimli içerik' not in a_parca(n, 'A3'):
        H.append("(4) %d:%d ARIZA söz maddesi 'söz biçimli içerik' diyor — A3'te '(söz biçimli içerik' yok" % (S, n))

# ── (5) mühür uyuşmazlığı ──
_em = subprocess.run(['python3', '/home/claude/sunum/esma_muhur.py', str(A), str(B), NN], capture_output=True, text=True).stdout
EMI = (item('esma_kayit') or [''])[0]
for n in range(A, B + 1):
    m = re.search(r'%d:%d muhur (\S+) / muhur_el (\S+) / ölçüm ([^—;]+?) —' % (S, n), _em)
    if not m or not (m.group(1) == 'EVET' and 'MÜHÜRSÜZ' in m.group(3)): continue
    mc = re.search(r"esma_kayit çıktısı[^.]*", M[n])
    if not mc or 'uyuşmuyor' not in mc.group(0): H.append("(5) %d:%d muhur EVET / ölçüm MÜHÜRSÜZ — ◇ esma_kayit cümlesinde 'uyuşmuyor' yok" % (S, n))
    if 'uyuşmuyor' not in ayet_seg(EMI, n) and not re.search(r'%d:%d[^;]*uyuşmuyor' % (S, n), EMI): H.append("(5) %d:%d muhur EVET / ölçüm MÜHÜRSÜZ — ARIZA esma_kayit maddesinde 'uyuşmuyor' yok" % (S, n))

# ── (7) emsal meal notu ──
MI = (item('meal (okuma') or [''])[0]
MI = MI.split('emsal meal karşılık farkları', 1)[1].split('): ', 1)[-1] if 'emsal meal karşılık farkları' in MI else ''
Q = r"(?<![^\s(\[])'((?:[^']|(?<=[A-Za-zâîûçğışöüÂÎÛ])'(?=[a-zâîûçğışöü]))+)'"
for m in re.finditer(Q + r" %d:(\d+) " % S + Q + r" / (\d+:\d+) " + Q + r" \(emsal metninde\) — (çakışma değil|çakışma — tam okuma sonu)", MI):
    kal, n, x, e, y, kar = m.group(1), int(m.group(2)), m.group(3), m.group(4), m.group(5), m.group(6)
    if x != y and kar == 'çakışma değil': H.append("(7) %s kalıbı %d:%d '%s' / %s '%s' bayt eşit değil — karar 'çakışma değil'" % (kal, S, n, x, e, y))
    if A <= n <= B and n in veri.MK:
        _fr = r"'[^']+-' '((?:[^']|'(?=[a-zâîûçğışöü]))+)'"
        fiil = [it for tr, q, its in veri.MK[n] for it in its if re.match(_fr, it) and re.match(_fr, it).group(1) in kal]  # yalnız kalıpta geçen fiil
        if fiil and x.lower() != y.lower() and not any(re.match(r"'([^']+)-'", f).group(1)[:3].lower() in y.lower() for f in fiil):
            H.append("(7) %s kalıbında fiil var — emsal alıntısı '%s' fiil karşılığını içermiyor" % (kal, y))

# ── (8) / (9) esma_el alıntısı ve 'sıfat' ──
ESI = (item('esmâ:') or [''])[0]
EL = Y + 'esma_el_%d_%d_%d.txt' % (S, A, B)
for l in (open(EL, encoding='utf-8').read().split('\n') if _o.path.exists(EL) else []):
    m = re.match(r"\s*'%d:(\d+):(\d+)': '(\w+)',\s*# (.*?) — (.*)$" % S, l)
    if not m: continue
    n, k, q, rest = int(m.group(1)), int(m.group(2)), m.group(4), m.group(5)
    if not A <= n <= B: continue
    if q not in M[n]: H.append("(8) %d:%d:%d esma_el alıntısı %s ◇'de bayt eşit yok" % (S, n, k, q))
    if q not in ESI: H.append("(8) %d:%d:%d esma_el alıntısı %s ARIZA esmâ maddesinde bayt eşit yok" % (S, n, k, q))
    par = re.search(r'\(([^()]*)\)\s*$', rest)
    if par and re.search(r'\bsıfat', par.group(1)):
        tg = ' '.join(t + '|' + ft for f, t, ft in W[n][k])
        if not re.search(r'\bADJ\b|PCPL', tg): H.append("(9) %d:%d:%d esmâ parantezinde 'sıfat' — morph ADJ / PCPL yok (%s)" % (S, n, k, tg[:60]))

# ── (14) emsal olarak basıldı ──
EMS = set()
for f in glob.glob('/home/claude/b*/ems.txt'): EMS |= set(open(f, encoding='utf-8').read().split())
for kay in [M[n] for n in range(A, B + 1)] + ITEMS:
    for m in re.finditer(r'((?:\d+:\d+(?:, | ve )?)+) \(emsal olarak basıldı\)', kay):
        for h in re.findall(r'\d+:\d+', m.group(1)):
            if h not in EMS: H.append("(14) %s '(emsal olarak basıldı)' — emsal olarak basılmadı (blok ayeti: '(basılmış)')" % h)

# ── (15) es_edat tanınmayan ──
_es = subprocess.run(['python3', '/home/claude/sunum/es_edat.py', NN], capture_output=True, text=True).stdout
mt = re.search(r'tanınmayan[^:]*?(\d+)', _es)
if mt and mt.group(1) != '0': H.append("(15) es_edat tanınmayan %s — edat_etiket.py'ye ekleme yok" % mt.group(1))

# ── (17) karşılık adının baş harfi ──
for n in range(A, B + 1):
    for tr, q, its in veri.MK.get(n, []):
        for it in its:
            m = re.match(r"'([^' ]+)' '(?:[^']|'(?=[a-zâîûçğışöü]))+' (?:karşılığı|açılımı)", it)
            if not m: continue
            x = m.group(1).rstrip('-')
            if len(x) < 3 or not x[0].isalpha(): continue
            occ = [mm for mm in re.finditer(r'(?i)(?<![\wâîûçğışöüÂÎÛÇĞİÖŞÜ])' + re.escape(x), tr)]
            if not occ: continue
            ok = any(tr[o.start()] == x[0] for o in occ)
            bas = all(o.start() == 0 or re.search(r'[.!?:]\s*$', tr[:o.start()]) for o in occ if tr[o.start()] != x[0])
            if not ok and not bas: H.append("(17) %d:%d karşılık adı '%s' — mealde '%s' (baş harf farkı)" % (S, n, m.group(1), tr[occ[0].start():occ[0].start() + len(x)]))

# ── (19) basilan anı ──
nb = len(open('/home/claude/sunum/basilan.txt', encoding='utf-8').read().split())
mb = re.search(r'basilan satır sayısı \(blok anı\): (\d+)', ' '.join(ITEMS))
if not mb: H.append("(19) ARIZA'da 'basilan satır sayısı (blok anı): N' yok")
elif int(mb.group(1)) > nb: H.append("(19) basilan satır sayısı %s > güncel %d" % (mb.group(1), nb))

for h in H: print('HATA', h)
print('bolum15_kurallar hata: %d' % len(H))
