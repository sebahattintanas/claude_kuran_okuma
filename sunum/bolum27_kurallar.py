# sûre 6 bölüm 11 denetimi araç kuralları (bekleyen_ariza_6_b22.txt 2. öğe) — salt okur:
#  (1) SOZ_ICI_ETIKET_TAM: A3 '(söz içi, i-j. kelime' aralığına düşen kelimeyi anan A1 zamir / fiil kesimi 'söz içi' taşır (şahıstan bağımsız)
#  (2) A3_ALINTI_ARALIK: A3 "'Q' (söz içi, i-j. kelime" alıntısının kelime sayısı (bolum22 kelime sayımıyla) j-i+1
#  (3) GONDERGE_LOC_YASAK: A1 "gönderge 'X' N. kelime" — N. kelime morph LOC ya da T (zarf) ise hata
#  (4) GERIYE_SINIF_ES: ARIZA geriye dönük maddesinde 'X sınıfında' anılan sınıf (kayıt değişti / araç değişti / basılan değişti) maddedeki sayım satırında 0 olamaz
#  (5) ESMA_ETIKET_MORPH: bu bloğun esma_el kaydı morph T (zaman) kelimesindeyse parantez 'zarf' sözcüğünü, morph ADJ kelimesindeyse 'sıfat' sözcüğünü taşır
# (elle: SOZ_MAHZUF_TUTARLI, KONUSAN_LAFIZ_DONUS, NEKRE_BELIRTME_KARAR, AYET_ICI_SAHIS_DONUS, EMSAL_XREF_KAPSAM, SEG_YUZEY_ICINDE_SIKI)
# kullanım (/home/claude'dan): python3 sunum/bolum27_kurallar.py A B NN
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK, S
import re, sys, ast, os, subprocess, collections, glob
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
TUM = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')[(A, B)]
ITEMS = [m for m in TUM if not re.match(r'(bölüm (denetimi \(|\d+ denetiminden)|devir \()', m)]
M, MEAL = {}, {}
exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'M': M, 'MEAL': MEAL})
EN = collections.Counter()
Q = r"'((?:[^']|(?<=[A-Za-zâîûçğışöüÂÎÛ])'(?=[a-zâîûçğışöü]))+)'"
def item(bas): return [m for m in ITEMS if m.startswith(bas)]
def satir(n, bas):
    for l in M[n].split('\n'):
        if l.startswith(bas): return l
    return ''
def dia(n):
    l = M[n].split('\n')[0]
    return l.split("◇ '", 1)[1].split("' — ", 1)[0] if "◇ '" in l else ''
MOR = collections.defaultdict(dict)
_mf = _BK + 'b%s/morph.txt' % NN
if os.path.exists(_mf):
    for l in open(_mf, encoding='utf-8'):
        p = l.rstrip('\n').split('\t')
        if len(p) >= 3:
            s_, a_, w_ = p[0].split(':')[:3]
            if int(s_) == S: MOR[int(a_)][int(w_)] = p[2]

_src = open('/home/claude/sunum/bolum22_kurallar.py', encoding='utf-8').read()
_g = {'re': re}
exec(_src[_src.index('def kelime(q):'):_src.index('def aralik(')], _g)
kelime = _g['kelime']
def ust_bol(t):  # parantez dışındaki '; ' ile böl
    out, d, cur = [], 0, ''
    i = 0
    while i < len(t):
        c = t[i]
        d += c == '('; d -= c == ')'
        if d == 0 and t.startswith('; ', i): out.append(cur); cur = ''; i += 2; continue
        cur += c; i += 1
    return out + [cur]
def a_parca(n, k):
    l = satir(n, '◈A')
    i = l.find(k + ' ')
    if i < 0: return ''
    j = l.find(' A%d ' % (int(k[1]) + 1), i)
    return l[i + 3:j if j > 0 else len(l)]

# ── (1) SOZ_ICI_ETIKET_TAM ── (2) A3_ALINTI_ARALIK ──
for n in range(A, B + 1):
    a3 = a_parca(n, 'A3')
    ar = []
    for q, i_, j_ in re.findall(r"(?:^|; )'(.*?)' \(söz içi, (\d+)-(\d+)\. kelime", a3):
        i_, j_ = int(i_), int(j_); ar.append((i_, j_))
        EN['a3_alinti'] += 1
        if kelime(q) != j_ - i_ + 1: H.append("(2) %d:%d A3 alıntısı '%s' %d kelime / aralık %d-%d" % (S, n, q[:40], kelime(q), i_, j_))
    if not ar: continue
    for p in ust_bol(a_parca(n, 'A1')):
        if 'söz içi' in p or not re.search(r'\b[123][MF]?[SPD]\b|fiil uyumu|edilgen', p): continue
        nums = [int(x) for x in re.findall(r'(?<![\d:])(\d+)\. kelime', re.sub(r"gönderge [^,;)]*?\d+\. kelime", '', p))]
        EN['soz_ici_etiket'] += 1
        ic = [k for k in nums if any(i_ <= k <= j_ for i_, j_ in ar)]
        if ic: H.append("(1) %d:%d A1 kesimi söz aralığındaki %s. kelimeyi anıyor, 'söz içi' yok: %s" % (S, n, ', '.join(map(str, ic)), p[:60]))

# ── (3) GONDERGE_LOC_YASAK ──
for n in range(A, B + 1):
    for q, k in re.findall(r"gönderge " + Q + r" (\d+)\. kelime", a_parca(n, 'A1')):
        EN['gonderge_loc'] += 1
        ft = MOR.get(n, {}).get(int(k), '')
        if re.match(r'N\|(LOC|T)\b', ft): H.append("(3) %d:%d gönderge '%s' (%s. kelime) morph %s — zarf gönderge olamaz" % (S, n, q, k, ft.split('|')[1]))

# ── (4) GERIYE_SINIF_ES ──
for it in item('geriye dönük koşu'):
    for sn in ('kayıt değişti', 'araç değişti', 'basılan değişti'):
        if '%s sınıfında' % sn not in it: continue
        EN['geriye_sinif'] += 1
        m = re.search(r'%s (\d+)' % sn, it)
        if m and m.group(1) == '0': H.append("(4) geriye dönük maddesi '%s sınıfında' diyor, sayım satırında %s 0" % (sn, sn))

# ── (5) ESMA_ETIKET_MORPH ──
_ef = Y + 'esma_el_%d_%d_%d.txt' % (S, A, B)
if os.path.exists(_ef):
    for l in open(_ef, encoding='utf-8'):
        m = re.match(r"\s*'%d:(\d+):(\d+)': '\w+',\s*#.*\((.+)\)\s*$" % S, l)
        if not m: continue
        a_, w_, par = int(m.group(1)), int(m.group(2)), m.group(3)
        ft = MOR.get(a_, {}).get(w_, '')
        EN['esma_etiket'] += 1
        if re.search(r'\|T\|', ft + '|') and 'zarf' not in par: H.append("(5) %d:%d:%d esma_el parantezi '%s' — morph T (zaman), 'zarf' yok" % (S, a_, w_, par))
        if re.search(r'\bADJ\b', ft) and 'sıfat' not in par: H.append("(5) %d:%d:%d esma_el parantezi '%s' — morph ADJ, 'sıfat' yok" % (S, a_, w_, par))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum27_kurallar hata: %d' % len(H))
