# sûre 7 bölüm 3 denetimi araç kuralları (bekleyen_ariza_7_b09.txt 2. öğe) — salt okur:
#  (1) YAZIM_FARKI_DIZI_ES: ◇'de sayılan, korpusta 1 çıkan harekesiz aralık, bloğun emsalini bulan bir lemma dizisinin aralığı içindeyse emsal karşılık maddesinde o dizi adıyla anılır
#  (2) ETIKETSIZ_EDAT: morph etiketi taşımayan edat / zamir kesim notu başlığının bu blokta çıkan yeni karşılığı, bölümün önceki bloklarında yoksa 'bölüm içi eş edat' maddesinde anılır
#  (3) KIP_SAPMA_GENIS_ZAMAN: kip notunda IMPF IND olup meal karşılığı geniş zaman ekiyle biten fiil kip sapma notunda geçer
#  (4) NAIB_FAIL_CELISKI: A1'de 'naib-i faili' kaydı olan blokta edilgen maddesi 'naib-i fail yok' diyemez
#  (5) KARSILIK_TAKDIR_CIFT: bir kesimde eş Türkçe parça hem edat / zamir karşılığı hem 'takdiri' olarak yazılamaz
# (elle: BASILMIS_ES_MEAL, A1_ZINCIR_ES, KIP_NOTU_KESIM_ES, D3_DISI_GEREKCE, BAG_EN_UZUN_ES, TARTISMALI_OLCUTU, FIIL_UYUMU_CINS, BOLUM_ICI_YALNIZ_CIFT, KOK_GRUBU_GOVDE)
# kullanım (/home/claude'dan): python3 sunum/bolum38_kurallar.py A B NN
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
def satir(n, bas):
    for l in M[n].split('\n'):
        if l.startswith(bas): return l
    return ''
def a4(a):
    l = satir(a, '◈A')
    return l.split(' A4 ', 1)[1] if ' A4 ' in l else ''
MOR = collections.defaultdict(dict)
_mf = _BK + 'b%s/morph.txt' % NN
if os.path.exists(_mf):
    for l in open(_mf, encoding='utf-8'):
        p = l.rstrip('\n').split('\t')
        if len(p) >= 3:
            s_, a_, w_ = p[0].split(':')[:3]
            if int(s_) == S: MOR[int(a_)][int(w_)] = p[2]
O = [l for l in open(_BK + 'b%s/olcum.txt' % NN, encoding='utf-8').read().replace('**', '').split('\n\n') if l.strip()] if os.path.exists(_BK + 'b%s/olcum.txt' % NN) else []
S2, BAS, LEM = {}, {}, {}
_s2 = _BK + 'b%s/say2.txt' % NN
if os.path.exists(_s2):
    for blk in re.split(r'^### ', open(_s2, encoding='utf-8').read(), flags=re.M)[1:]:
        h = blk.split('\n', 1)[0].strip()
        m = re.search(r"\{'bu'.*\}", blk)
        if m: S2[h] = ast.literal_eval(m.group(0))
        lm = re.search(r'liste: (.*)', blk)
        ls = blk.split('\n')
        if h.startswith('dizi'):
            BAS[h] = set(x.strip('†') for x in (ls[2] if len(ls) > 2 else '').split(', ') if x.strip())
            mm = re.search(r'lemma dizisi (\[.*?\]) \|', blk)
            if mm:
                try: LEM[h] = ast.literal_eval(mm.group(1))
                except Exception: pass
        elif lm: BAS[h] = set(x.strip('†') for x in lm.group(1).split(', '))
SRC = open(_BK + 'b%s/yap/metin_yap.py' % NN, encoding='utf-8').read() if os.path.exists(_BK + 'b%s/yap/metin_yap.py' % NN) else ''
DIZ = re.findall(r"say\('(dizi %d \d+ \d+ \d+)', \"([^\"]+)\"\)" % S, SRC) + re.findall(r"say\('(dizi %d \d+ \d+ \d+)', '([^']+)'\)" % S, SRC)


import importlib.util as _iu
def dia(a): 
    l = M[a].split('\n')[0] if a in M else ''
    m = re.search(r"◇ '(.*?)' — ", l)
    return m.group(1) if m else ''
HRF = 'a-zçğıöşüâîûA-ZÇĞİÖŞÜÂÎÛ'
_vf = _BK + 'b%s/yap/veri.py' % NN
MK = {}
if os.path.exists(_vf):
    _sp = _iu.spec_from_file_location('veri', _vf); _v = _iu.module_from_spec(_sp); _sp.loader.exec_module(_v); MK = _v.MK
def _ar(its):
    n = [int(x) for it in its for x in re.findall(r"(?<!\d)(\d+)\. kelime", it)]
    return (min(n), max(n)) if n else None
_pl = Y + 'blok_plani_%d.txt' % S
BOLB = []
if os.path.exists(_pl):
    grp, cur = [], None
    for l in open(_pl, encoding='utf-8'):
        if l.startswith('■'): cur = []; grp.append(cur)
        else:
            m = re.match(r'\s*(\d+)\. ', l)
            if m and cur is not None: cur.append(int(m.group(1)))
    BOLB = next((g for g in grp if int(NN) in g), [])
onc = [n for n in BOLB if n < int(NN)]
def _veri(nn):
    f_ = _BK + 'b%02d/yap/veri.py' % nn
    if not os.path.exists(f_): return {}
    sp_ = _iu.spec_from_file_location('veri%d' % nn, f_); v_ = _iu.module_from_spec(sp_); sp_.loader.exec_module(v_)
    return v_.MK
bie = ' '.join(m.split('bölüm içi eş edat', 1)[1] for m in ITEMS if 'bölüm içi eş edat' in m)
MI = (item('meal (okuma') or [''])[0]
EMI = MI.split('emsal meal karşılık farkları', 1)[1].split('kip notu (', 1)[0] if 'emsal meal karşılık farkları' in MI else ''
KN = MI.split('kip notu (', 1)[1].split('kip sapma notu', 1)[0] if 'kip notu (' in MI else ''
KS = MI.split('kip sapma notu', 1)[1] if 'kip sapma notu' in MI else ''
_ef = _BK + 'b%s/ems.txt' % NN
EMS = set(open(_ef, encoding='utf-8').read().split()) if os.path.exists(_ef) else set()
def _top(d): return len(d.get('bu', [])) + len(d.get('basilan', [])) + sum(d.get(k_, 0) if isinstance(d.get(k_, 0), int) else len(d.get(k_, [])) for k_ in ('eski', 'okunmus', 'okunmus_si', 'henuz', 'henuz_si'))
# ── (1) YAZIM_FARKI_DIZI_ES ──
for h in sorted(S2):
    m = re.match(r'say %d:(\d+) (\d+)-(\d+)$' % S, h)
    if not m or "say('%s'" % h not in SRC or _top(S2[h]) != 1: continue
    a_, i_, j_ = map(int, m.groups())
    if j_ - i_ < 1: continue
    for d in sorted(BAS):
        md = re.match(r'dizi %d (\d+) (\d+) (\d+)$' % S, d)
        if not md or int(md.group(1)) != a_: continue
        p_, q_ = int(md.group(2)), int(md.group(3))
        es = sorted(BAS[d] & EMS)
        if p_ <= i_ and j_ <= q_ and es:
            EN['yazim'] += 1
            if d not in EMI: H.append("(1) '%s' korpusta 1 — '%s' emsal %s buluyor (yazım / çekim farkı); emsal karşılık maddesinde dizi adı yok" % (h, d, ', '.join(es)))
            break
# ── (2) ETIKETSIZ_EDAT ──
def _edat0(mk):
    d = {}
    for a_, L in mk.items():
        for tr_, q_, its in L:
            for x in its:
                m = re.match(r"'((?:[^']|'(?=[%s]))+)' \d+\. kelimede (.*)$" % HRF, x)
                if m and 'morph ' not in x:
                    d.setdefault(m.group(1), set()).add(re.sub(r" ile$", '', re.sub(r' \(.*$', '', m.group(2)).strip()).lower())
    return d
if onc:
    bu = _edat0(MK); es = {}
    for n in onc:
        for k_, v_ in _edat0(_veri(n)).items(): es.setdefault(k_, set()).update(v_)
    for k_ in sorted(set(bu) & set(es)):
        EN['edat0'] += 1
        if (bu[k_] - es[k_]) and "'%s' (" % k_ not in bie: H.append("(2) '%s' bölüm içi yeni karşılık: bu blok %s / önceki %s — 'bölüm içi eş edat' maddesinde anılmamış" % (k_, sorted(bu[k_]), sorted(es[k_])))
# ── (3) KIP_SAPMA_GENIS_ZAMAN ──
GZ = re.compile(r"(?:[ae]r|[ıiuü]r|m[ae]z)$")
for f_, w_ in re.findall(r"'([^\s';]+(?:'[^\s';]+)*)' IMPF IND[^;]*? — meal '([^']+)'", KN):
    g_ = re.sub(r"(?:l[ae]r|s[ıiuü]n[ıiuü]z|[ıiuü]z|[ıiuü]m|s[ıiuü]n)$", '', w_)
    if GZ.search(g_) and 'yor' not in w_:
        EN['genis'] += 1
        if "'%s'" % f_ not in KS: H.append("(3) kip notu '%s' IMPF IND — meal '%s' geniş zaman; kip sapma notunda yok" % (f_, w_))
# ── (4) NAIB_FAIL_CELISKI ──
ed = ' '.join(item('edilgen:'))
for a in range(A, B + 1):
    a1 = satir(a, '◈A').split(' A2 ')[0]
    if 'naib-i faili' in a1:
        EN['naib'] += 1
        if 'naib-i fail yok' in ed and '%d:%d ' % (S, a) in ed: H.append("(4) %d:%d A1 'naib-i faili' kaydı / edilgen maddesi 'naib-i fail yok'" % (S, a))
# ── (5) KARSILIK_TAKDIR_CIFT ──
for a_, L in sorted(MK.items()):
    for tr_, q_, its in L:
        tk = set(re.findall(r"^'([^']+)' takdiri", ' \n'.join(its), flags=re.M))
        kr = set(re.findall(r"kelimede '([^']+)' ile", ' '.join(its)))
        for x in sorted(tk & kr):
            EN['cift'] += 1
            H.append("(5) %d:%d kesim '%s' — '%s' hem karşılık hem takdir" % (S, a_, tr_[:30], x))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum38_kurallar hata: %d' % len(H))
