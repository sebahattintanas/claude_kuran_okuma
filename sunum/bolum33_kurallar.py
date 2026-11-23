# sûre 6 bölüm 17 denetimi araç kuralları (bekleyen_ariza_6_b36.txt 2. öğe) — salt okur:
#  (1) D3_KOK_IKILEME: ölçümdeki her 'kök ikilemesi' öğesi (kök ×k) ◈D D3'te yer alır; D3 '—' yalnız bag eşi de ikileme de yoksa
#  (2) ALINTI_KELIME_SINIRI: seg Arapça kesimi ve ARIZA R5 'harekesiz' alıntısı ◇ içinde kelime sınırında biter (ardından boşluk, virgül ya da ◇ sonu)
#  (3) BERABERLIK_YER: ◈A satırında 'beraberlik' yalnız A4'te geçer; 'beraberlik değil' kalıbı yazılmaz (ayrışma 'toplam farkı' ile)
#  (4) ADAY1041_KELIME_TAM: aday 1041 maddesinde 'kök X S:a (…)' biçiminde anılan kökün o ayetteki bütün kelimeleri parantezde alıntılanır (morph ROOT sayısı)
#  (5) MUHATAP_GECIS_SIRA: morph'ta ayet içi 2MS / 2MP dizisindeki her geçiş (X → Y) A4'te 'muhatap geçişi X → Y' olarak yer alır
# (elle: METIN_DISI_AD_ZINCIR, SORU_CEVAP_TANIM, SESTES_KOK_GRUBU, NE_EDAT_KAYDI, KM_BUYUK_HARF_GEREKCE, A2_SAHIS_KORU, ESMA_PARANTEZ_BIR, A1_EK_AYRIMI)
# kullanım (/home/claude'dan): python3 sunum/bolum33_kurallar.py A B NN
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK, S
import re, sys, ast, os, collections
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
# ── (1) D3_KOK_IKILEME ──
for k, a in enumerate(range(A, B + 1)):
    if k >= len(O): break
    m = re.search(r'kök ikilemesi (.+?) · (?:simetri|harf )', O[k])
    if not m: continue
    d3 = re.search(r'D3 (.*?); D4', satir(a, '◈D'))
    d3 = d3.group(1) if d3 else ''
    for kok, n in re.findall(r'(\S+) \*\(.*?\)\* ×(\d+)', m.group(1)):
        EN['d3_kok'] += 1
        if '%s ×%s' % (kok, n) not in d3: H.append("(1) %d:%d D3 ölçüm kök ikilemesi '%s ×%s' yok" % (S, a, kok, n))
# ── (2) ALINTI_KELIME_SINIRI ──
def sinirda(q, d):
    for mm in re.finditer(re.escape(q), d):
        e = mm.end()
        if e == len(d) or d[e] in " ,.;'": return True  # ' : wasl sınırı
    return False
_vp = _BK + 'b%s/yap/veri.py' % NN
if os.path.exists(_vp):
    _sp = _iu.spec_from_file_location('veri33', _vp); _v = _iu.module_from_spec(_sp); _sp.loader.exec_module(_v)
    for a, L in _v.MK.items():
        if not A <= a <= B: continue
        for tr, q, its in L:
            EN['sinir_seg'] += 1
            if not sinirda(q, dia(a)): H.append("(2) %d:%d seg kesimi '%s' ◇'de kelime sınırında bitmiyor" % (S, a, q))
R5I = ' '.join(item('araç tanımı farkları'))
for m in re.finditer(r"(?<![\d:])%d:(\d+) nakarat3 [^;]*?harekesiz '((?:[^']|'(?=[a-zâîûçğışöü]))+)' \((\d+)-(\d+)\. kelime\)" % S, R5I):
    a, q = int(m.group(1)), m.group(2)
    if not A <= a <= B: continue
    EN['sinir_r5'] += 1
    if not sinirda(q, dia(a)): H.append("(2) %d:%d R5 harekesiz alıntı '%s' ◇'de kelime sınırında bitmiyor" % (S, a, q))
# ── (3) BERABERLIK_YER ──
for a in range(A, B + 1):
    l = satir(a, '◈A')
    if 'beraberlik' not in l: continue
    EN['beraberlik_yer'] += 1
    dis = l.split(' A4 ', 1)[0] if ' A4 ' in l else l
    if 'beraberlik' in dis: H.append("(3) %d:%d 'beraberlik' ◈A'da A4 dışında" % (S, a))
    if 'beraberlik değil' in l: H.append("(3) %d:%d 'beraberlik değil' kalıbı — ayrışma 'toplam farkı' ile yazılır" % (S, a))
# ── (4) ADAY1041_KELIME_TAM ──
RK = collections.defaultdict(lambda: collections.Counter())
_mf6 = _BK + 'b%s/morph%d.txt' % (NN, S)
if os.path.exists(_mf6):
    _gor = set()
    for l in open(_mf6, encoding='utf-8'):
        p = l.rstrip('\n').split('\t')
        if len(p) < 4: continue
        s_, a_, w_ = p[0].split(':')[:3]
        r = re.search(r'ROOT:([^|]+)', p[3])
        if r and (a_, w_, r.group(1)) not in _gor:
            _gor.add((a_, w_, r.group(1))); RK[r.group(1)][int(a_)] += 1
AD = ' '.join(item('aday 1041'))
Qx = r"'(?:[^']|'(?=[a-zâîûçğışöü]))+'"
for parca in re.split(r'(?=\bkök )', AD):
    mk = re.match(r'kök (\S+) ', parca)
    if not mk: continue
    kok = mk.group(1)
    for ma in re.finditer(r'(?<![\d:])%d:(\d+) \(((?:%s)(?:, %s)*)\)' % (S, Qx, Qx), parca):
        a = int(ma.group(1))
        if not A <= a <= B or kok not in RK: continue
        n = len(re.findall(Qx, ma.group(2)))
        EN['aday1041'] += 1
        if n < RK[kok][a]: H.append("(4) %d:%d aday 1041 kök %s %d alıntı / morph %d kelime" % (S, a, kok, n, RK[kok][a]))
# ── (5) MUHATAP_GECIS_SIRA ──
for a in range(A, B + 1):
    ws = MOR.get(a, {})
    diz = []
    for w in sorted(ws):
        t = re.findall(r'\|(2M[SP])(?:\||$)', ws[w])
        if len(set(t)) == 1 and (not diz or diz[-1] != t[0]): diz.append(t[0])
    gec = list(zip(diz, diz[1:]))
    if not gec: continue
    EN['muhatap_sira'] += 1
    var = re.findall(r'muhatap geçişi ((?:\S+ → )+\S+)', a4(a))
    yaz = set()
    for v in var:
        x = v.split(' → '); yaz |= set(zip(x, x[1:]))
    for g in gec:
        if g not in yaz: H.append("(5) %d:%d morph muhatap geçişi %s → %s — A4'te yok" % (S, a, g[0], g[1]))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum33_kurallar hata: %d' % len(H))
