# sûre 6 bölüm 19 denetimi araç kuralları (bekleyen_ariza_6_b40.txt 2. öğe) — salt okur:
#  (1) SEG_ADDR_PARCA: morph'ta ADDR parçası taşıyan kelime için meal kesim notlarında 'N. kelime' ile birlikte 'ADDR' anılır
#  (2) EMSAL_ALINTI_KELIME_SINIRI: 'bayt eşit' denen emsal alıntısı mealde ve emsal metninde kelime sınırında biter
#  (3) SAY2_GENIS_ES_ANILIR: say2'de birden çok ayet bulan, en az 5 kelimelik ve daha geniş bir eş aralığın içinde kalmayan 'say' başlığı ◇'de ya da ARIZA'da adıyla geçer
#  (4) SOZ_DISI_ETIKET_CELISKISI: A3 'söz kapanışı gerekçesi' morph CONJ etiketini söz dışılık dayanağı yapmaz
#  (5) KIP_SAPMA_OLAN: kip notunda meal karşılığı 'olan…' / 'olduk…' / 'olduğ…' olan fiil kip sapma notunda anılır
# (elle: SEG_MORPH_PARCA_TAM, GONDERGE_ZINCIR_A1_ES, SOZ_SINIRI_MUHATAP, TARTISMALI_GONDERGE_KAPSAMI, EMSAL_TAKDIR_FARKI, ESMA_KARAR_SAYIM_DAYANAGI)
# kullanım (/home/claude'dan): python3 sunum/bolum35_kurallar.py A B NN
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
# ── (1) SEG_ADDR_PARCA ──
_vf = _BK + 'b%s/yap/veri.py' % NN
MK = {}
if os.path.exists(_vf):
    _sp = _iu.spec_from_file_location('veri', _vf); _v = _iu.module_from_spec(_sp); _sp.loader.exec_module(_v); MK = _v.MK
for a in range(A, B + 1):
    its = [it for tr, q, l in MK.get(a, []) for it in l]
    for w, f in sorted(MOR.get(a, {}).items()):
        if '|ADDR|' not in f + '|': continue
        EN['addr'] += 1
        if not any(re.search(r'(?<!\d)%d\. kelime' % w, it) and 'ADDR' in it for it in its): H.append("(1) %d:%d %d. kelime morph ADDR parçası — meal kesim notunda 'ADDR' kaydı yok" % (S, a, w))
# ── (2) EMSAL_ALINTI_KELIME_SINIRI ──
_ef = _BK + 'b%s/emsal_%d_%d_%d.md' % (NN, S, A, B)
EMS = open(_ef, encoding='utf-8').read() if os.path.exists(_ef) else ''
for it in item('meal (okuma'):
    for a, tr, e, tr2 in re.findall(r"%d:(\d+) '((?:[^']|'(?=[%s]))+)' / (\d+:\d+) '((?:[^']|'(?=[%s]))+)' \(emsal metninde\) — çakışma değil \(bayt eşit\)" % (S, HRF, HRF), it):
        EN['emsal_bayt'] += 1
        for ad, metin, al in (('meal %d:%s' % (S, a), MEAL.get(int(a), ''), tr), ('emsal %s' % e, EMS, tr2)):
            k = metin.find(al)
            if k >= 0 and re.match('[%s]' % HRF, metin[k + len(al):k + len(al) + 1] or ' '): H.append("(2) %s alıntısı kelime ortasında bitiyor: '…%s' + '%s'" % (ad, al[-20:], re.match('[%s]+' % HRF, metin[k + len(al):]).group(0)))
# ── (3) SAY2_GENIS_ES_ANILIR ──
ARZ = '\n'.join(ITEMS) + '\n' + '\n'.join(M[a] for a in M) + (open(Y + 'bag_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() if os.path.exists(Y + 'bag_%d_%d_%d.txt' % (S, A, B)) else '')
AR_ = collections.defaultdict(list)
for h in BAS:
    m = re.match(r'say %d:(\d+) (\d+)-(\d+)$' % S, h)
    if m and len(BAS[h]) >= 2: AR_[int(m.group(1))].append((int(m.group(2)), int(m.group(3)), h))
for a in sorted(AR_):
    for i_, j_, h in AR_[a]:
        if j_ - i_ + 1 < 5: continue
        if any((p <= i_ and j_ <= q) and (p, q) != (i_, j_) for p, q, _h in AR_[a]): continue
        EN['genis_es'] += 1
        if not re.search(re.escape(h) + r'(?!\d)', ARZ): H.append("(3) '%s' %d ayet buluyor (%d kelime) — ◇ / ARIZA'da adıyla yok" % (h, len(BAS[h]), j_ - i_ + 1))
# ── (4) SOZ_DISI_ETIKET_CELISKISI ──
for a in range(A, B + 1):
    l = satir(a, '◈A')
    m = re.search(r'söz kapanışı gerekçesi[^;]*', l)
    if not m: continue
    EN['soz_disi'] += 1
    if re.search(r'morph CONJ ile söz dışı', m.group(0)): H.append("(4) %d:%d söz kapanışı gerekçesi morph CONJ etiketine dayanıyor (CONJ söz içinde sapmasız geçer)" % (S, a))
# ── (5) KIP_SAPMA_OLAN ──
for it in item('meal (okuma'):
    if 'kip notu' not in it: continue
    kn = it.split('kip notu', 1)[1].split('kip sapma notu', 1)[0]
    ks = it.split('kip sapma notu', 1)[1] if 'kip sapma notu' in it else ''
    for v, w in re.findall(r"(?:; |: |\d )'([^;]*?)' (?:PERF|IMPF)[^;]*? — meal '(ol(?:an|duk|duğ)[^']*)'", kn):
        EN['kip_olan'] += 1
        if "'%s'" % v not in ks: H.append("(5) kip notu '%s' — meal '%s' sıfat-fiil; kip sapma notunda yok" % (v, w))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum35_kurallar hata: %d' % len(H))
