# bölüm 16 (sûre 5) denetimi araç kuralları (bekleyen_ariza_5_b36.txt 2. öğe) — salt okur:
#  (1) A1_FAIL_UYUM: 3. şahıs etken fiilin ardından (sonraki fiile, CONJ / REM / RSLT önekli kelimeye dek) zamirsiz NOM ad geliyorsa
#      A1'de 'N. kelime — fail M. kelime' (fiil uyumu); ARIZA 'A1'de gönderge olarak' alıntıları A1 alt dizesi
#  (2) IC_SOZ_KAPANIS: ayet sonundan önce biten her 'iç söz, N-M. kelime' için A4'te 'söz kapanır (M. kelime, ayet içi)'
#  (3) ESMA_LAFIZ_GONDERGE: esma_el 'lafzın haberi' kuralında kelimenin cümlesinde (önceki CONJ / REM / RSLT önekine dek) morph lafız
#      (LEM اللَّه) aranır; yoksa 'zamirin haberi' adı ya da '(onaya açık)' notu
#  (4) ESMA_KONUM_SON: ölçüm esmâ sırası ayetin kelime sayısına eşit ve konum SON değilse ARIZA'da 'ölçüm konum' notu
#  (5) A1_ALINTI_NUMARA: A1'de '— N., M. … kelime' listesindeki numara sayısı önündeki alıntı sayısına eşit
#  (6) BICIM_YERI: ARIZA biçim alanı için '(yalnız bu maddede' diyorsa ◇'de 'biçim X' yazılmaz
#  (7) GEREKCE_EMSAL: ARIZA'daki "(olumlu|olumsuz) bağlamda 'X'" gerekçesindeki X bloğun emsal metninde geçiyorsa isabet (elle bakılır)
#  (8) MEDDE_FARK_KARAR: medde 'FARK VAR' veren her sayım için ◇'de '(--medde N ayet)' eki
#  (9 ORTAC_CUMLE elle)
# kullanım (/home/claude'dan): python3 sunum/bolum16_kurallar.py A B NN
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK, S
import re, sys, ast, collections, os
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
TUM = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')[(A, B)]
ITEMS = [m for m in TUM if not re.match(r'(bölüm (denetimi \(|\d+ denetiminden)|devir \()', m)]
M, MEAL = {}, {}
exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'M': M, 'MEAL': MEAL})
W = collections.defaultdict(lambda: collections.defaultdict(list))
for l in open(_BK + 'b%s/morph%d.txt' % (NN, S), encoding='utf-8'):
    loc, f, t, feat = l.rstrip('\n').split('\t'); s_, a_, w_, p_ = map(int, loc.split(':'))
    W[a_][w_].append((f, t, feat))
O = [l.replace('**', '') for l in open(_BK + 'b%s/olcum.txt' % NN, encoding='utf-8').read().split('\n\n') if l.strip()]
Q = r"'((?:[^']|(?<=[A-Za-zâîûçğışöüÂÎÛ])'(?=[a-zâîûçğışöü]))+)'"
def satir(n, bas):
    for l in M[n].split('\n'):
        if l.startswith(bas): return l
    return ''
def a_parca(n, k):
    l = satir(n, '◈A'); m = re.search(r'\b%s (.*?)(?:; A%d |$)' % (k, int(k[1]) + 1), l)
    return m.group(1) if m else ''
def fiil(a, w): return any(t == 'V' for f, t, ft in W[a][w])
def onek(a, w): return any(re.search(r'(?:^|\|)(CONJ|REM|RSLT|CIRC|SUP)(?:\||$)', ft) for f, t, ft in W[a][w] if 'PREF' in ft)
EN = collections.Counter()

# ── (1) A1_FAIL_UYUM ──
for a in range(A, B + 1):
    a1 = a_parca(a, 'A1')
    for w in sorted(W[a]):
        vs = [ft for f, t, ft in W[a][w] if t == 'V']
        if not vs or 'PASS' in vs[0] or not re.search(r'\|3(?:MS|FS|MD|FD)\b', vs[0]): continue
        if any(t == 'N' and 'PRON' in ft and 'SUFF' not in ft for f, t, ft in W[a][w]): continue
        fail = None
        for k in range(w + 1, max(W[a]) + 1):
            if fiil(a, k) or onek(a, k) or any(t == 'P' and re.search(r'(?:^|\|)ACC(?:\||$)', ft) for f, t, ft in W[a][k]): break  # sûre 6 blok 40: 'inne' yeni cümle açar
            if any(t == 'N' and re.search(r'(?:^|\|)PRON(?:\||$)', ft) and 'SUFF' not in ft for f, t, ft in W[a][k]): break  # sûre 7 blok 3: ayrı zamir ('ene') yeni cümlenin öznesi — ardındaki NOM ad önceki fiilin faili sayılmaz
            ns = [ft for f, t, ft in W[a][k] if t == 'N' and 'PRON' not in ft]
            if ns and any(re.search(r'(?:^|\|)NOM(?:\||$)', ft) for ft in ns): fail = k; break
        if not fail: continue
        EN['fail'] += 1
        if not re.search(r'(?<![\d-])%d\. kelime — fail \d+\. kelime' % w, a1):
            H.append("(1) %d:%d %d. kelime fiil, ardında zamirsiz NOM ad (%d. kelime) — A1'de '%d. kelime — fail %d. kelime' yok" % (S, a, w, fail, w, fail))
for it in ITEMS:
    for q in re.findall(Q + r"[^;']{0,80}A1'de gönderge olarak", it):
        if not any(q in a_parca(a, 'A1') for a in range(A, B + 1)): H.append("(1) ARIZA 'A1'de gönderge olarak' alıntısı A1'de yok: '%s'" % q)

# ── (2) IC_SOZ_KAPANIS ──
for a in range(A, B + 1):
    for n_, m_ in re.findall(r'iç söz,? (\d+)-(\d+)\. kelime', a_parca(a, 'A3')):
        EN['icsoz'] += 1
        if int(m_) < max(W[a]) and 'söz kapanır (%s. kelime, ayet içi)' % m_ not in a_parca(a, 'A4'):
            H.append("(2) %d:%d iç söz %s-%s. kelime ayet içinde bitiyor — A4'te 'söz kapanır (%s. kelime, ayet içi)' yok" % (S, a, n_, m_, m_))

# ── (3) ESMA_LAFIZ_GONDERGE ──
ep = Y + 'esma_el_%d_%d_%d.txt' % (S, A, B)
if os.path.exists(ep):
    for l in open(ep, encoding='utf-8'):
        m = re.match(r"\s*'%d:(\d+):(\d+)': '(\w+)',\s*#(.*)$" % S, l)
        if not m or 'lafzın haberi' not in m.group(4) or "kâna'llâhu" in m.group(4): continue
        a, w = int(m.group(1)), int(m.group(2)); EN['lafiz'] += 1
        bas = w
        while bas > 1 and not onek(a, bas): bas -= 1
        lafiz = any(('|PN|' in '|' + ft + '|' or ft.startswith('PN')) and 'ROOT:أله' in ft for k in range(bas, w + 1) for f, t, ft in W[a][k])
        if not lafiz and 'onaya açık' not in m.group(4):
            H.append("(3) %d:%d:%d 'lafzın haberi' — cümlede (%d-%d. kelime) lafız yok; 'zamirin haberi' ya da '(onaya açık)'" % (S, a, w, bas, w))

# ── (4) ESMA_KONUM_SON ──
for i, a in enumerate(range(A, B + 1)):
    if i >= len(O): break
    n = max(W[a])
    for s_, kon in re.findall(r'(\d+)\. sırada, (\w+) konum', O[i]):
        if int(s_) == n and kon != 'SON':
            EN['konum'] += 1
            if not any('ölçüm konum' in it and '%d:%d' % (S, a) in it for it in ITEMS):
                H.append("(4) %d:%d esmâ %s. sırada (ayet sonu) ölçümde %s — ARIZA'da 'ölçüm konum' notu yok" % (S, a, s_, kon))

# ── (5) A1_ALINTI_NUMARA ──
for a in range(A, B + 1):
    for parca in re.split(r'; (?![^()]*\))', a_parca(a, 'A1')):
        for m in re.finditer(r"\(([^()]*?) — ((?:\d+\., )*\d+\.(?: ve \d+\.)?) kelime\)", parca):
            nums = re.findall(r'\d+', m.group(2))
            if len(nums) < 2: continue
            seg = m.group(1).split('; ')[-1].strip()
            if not (seg.startswith("'") and seg.endswith("'")):
                on = parca[:parca.find(m.group(0))].strip()  # alıntılar parantezden önce: "'a', 'b' 3MP (…)"
                seg = re.sub(r" \d[A-Z]+$", '', on.split('; ')[-1].strip())
            if not (seg.startswith("'") and seg.endswith("'")): continue
            nq = seg.count("', '") + 1
            EN['a1num'] += 1
            if nq != len(nums):
                H.append("(5) %d:%d A1 alıntı %d / kelime numarası %d: %s" % (S, a, nq, len(nums), ', '.join(nums)))

# ── (6) BICIM_YERI ──
for it in ITEMS:
    if 'biçim' in it and '(yalnız bu maddede' in it:
        for a in range(A, B + 1):
            d = M[a].split('\n')[0]
            for b_ in re.findall(r'biçim ([A-ZÇĞİÖŞÜ]+)', d):
                if re.search(r"%d:%d [^;]*biçim alanı[^;]*%s" % (S, a, b_), it) or re.search(r"biçim alanı '\{?\{?.*?biçim %s" % b_, it):
                    h_ = "(6) %d:%d ◇'de 'biçim %s' — ARIZA 'yalnız bu maddede' diyor" % (S, a, b_)
                    if h_ not in H: H.append(h_)

# ── (7) GEREKCE_EMSAL ──
emp = _BK + 'b%s/emsal.txt' % NN
emt = open(emp, encoding='utf-8').read() if os.path.exists(emp) else ''
for it in ITEMS:
    for x in re.findall(r"(?:olumlu|olumsuz) bağlamda '([^']+)'", it):
        EN['gerekce'] += 1
        if emt and x in emt: H.append("(7) gerekçe 'bağlamda '%s'' — '%s' bloğun emsal metninde de geçiyor" % (x, x))

# ── (8) MEDDE_FARK_KARAR ──
for it in ITEMS:
    for k in re.findall(r"FARK VAR: '(say %d:(\d+) \d+-\d+)'" % S, it):
        key, a = k[0], int(k[1]); EN['medde'] += 1
        if a in M and '(--medde ' not in M[a].split('\n')[0]:
            H.append("(8) %d:%d medde farkı ('%s') — ◇'de '(--medde N ayet)' eki yok" % (S, a, key))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum16_kurallar hata: %d' % len(H))
