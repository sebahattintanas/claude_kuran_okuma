# sûre 6 bölüm 10 denetimi araç kuralları (bekleyen_ariza_6_b20.txt 2. öğe) — salt okur:
#  (1) GONDERGE_SAYI_UYUM: A1 "3MP|3FP (… gönderge S:a N. kelime" ya da "gönderge 'X' N. kelime" — göndergenin morph'u tekil (MS / FS ya da sayısız özel ad) ise kayıtta 'tartışmalı' ya da aralık ('N-M. kelime') var
#  (2) GOZLEM_SAYI_OLCUM: ARIZA "okuma (gözlem)" maddesinde "S:a-b <sayı> özel ad" iddiası ölçüm aktör alanındaki 'adlı' sayısıyla eş
#  (3) EKSILTI_SAHIS: ölçümü 'şahıs işaret yok' olan ayetin A4'ünde ve izleyen ayetin A4'ünde '—' içeren şahıs geçişi 'eksiltili' notu taşır
#  (4) OZEL_AD_TETIK: ◈K / ◈B satırındaki "'Q' (N. kelime)" alıntısının kelimesi morph PN ise satırda 'özel ad' notu var
#  (5) SEG_YUZEY_KARSILIK: seg.py "'X' 'Y' karşılığı|açılımı" notunda X (ya da ilk sözcüğü) meal kesiminde geçer; geçmiyorsa notta 'içinde' biçimi var
# (elle: A1_ARIZA_GONDERGE_ES, BASKIN_CIFT_SAYIM, KONUSAN_LAFIZ_DONUS, KULL_KAPSAM, EMSAL_BAG_FARK, YENI_GRUP_ISARET)
# kullanım (/home/claude'dan): python3 sunum/bolum26_kurallar.py A B NN
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

def a_parca(n, k):
    l = satir(n, '◈A')
    i = l.find(k + ' ')
    if i < 0: return ''
    j = l.find(' A%d ' % (int(k[1]) + 1), i)
    return l[i + 3:j if j > 0 else len(l)]
def tekil(feat):
    if not feat: return False
    if re.search(r'\|[MF]?[PD]\||\|P\|', feat + '|'): return False
    return bool(re.search(r'\|[MF]S\|', feat + '|')) or ('|PN|' in feat and not re.search(r'\|[MF]?P\b', feat))

# ── (1) GONDERGE_SAYI_UYUM ──
for n in range(A, B + 1):
    a1 = a_parca(n, 'A1')
    for m in re.finditer(r"3(?:M|F)P \(([^()]*?)gönderge (?:%d:(\d+) (\d+)\. kelime|%s (\d+)\. kelime)([^()]*?)\)" % (S, Q), a1):
        if m.group(2): ga, gn = int(m.group(2)), int(m.group(3))
        else: ga, gn = n, int(m.group(5))
        EN['gonderge_sayi'] += 1
        tam = m.group(0)
        if 'tartışmalı' in tam or re.search(r'gönderge (?:%d:)?\d*:?\d+-\d+\. kelime' % S, tam): continue
        if ga in MOR and tekil(MOR[ga].get(gn, '')):
            H.append("(1) %d:%d çoğul zamir göndergesi %d:%d %d. kelime morph tekil — 'tartışmalı' ya da aralık yok" % (S, n, S, ga, gn))

# ── (2) GOZLEM_SAYI_OLCUM ──
SAYI = {'bir': 1, 'iki': 2, 'üç': 3, 'dört': 4, 'beş': 5, 'altı': 6, 'yedi': 7, 'sekiz': 8, 'dokuz': 9, 'on': 10, 'yirmi': 20}
def sayi(t):
    if t.isdigit(): return int(t)
    return sum(SAYI.get(x, 0) for x in t.split()) if all(x in SAYI for x in t.split()) else None
_of = _BK + 'b%s/olcum.txt' % NN
_ob = [b_ for b_ in open(_of, encoding='utf-8').read().split('\n\n') if b_.strip()] if os.path.exists(_of) else []
def olc(n):
    k_ = n - A
    return _ob[k_] if 0 <= k_ < len(_ob) else ''
GZ = ' '.join(item('okuma (gözlem)'))
for m in re.finditer(r"%d:(\d+)(?:-(\d+))? ((?:\d+|(?:(?:bir|iki|üç|dört|beş|altı|yedi|sekiz|dokuz|on|yirmi) ?)+)) özel ad" % S, GZ):
    a_, b_ = int(m.group(1)), int(m.group(2) or m.group(1)); v = sayi(m.group(3).strip())
    if v is None or not (A <= a_ <= B and A <= b_ <= B): continue
    EN['gozlem_sayi'] += 1
    g = sum(olc(x).count('adlı ') for x in range(a_, b_ + 1))
    if g != v: H.append("(2) okuma (gözlem) %d:%d-%d '%s özel ad' / ölçüm aktör adlı %d" % (S, a_, b_, m.group(3).strip(), g))

# ── (3) EKSILTI_SAHIS ──
for n in range(A, B + 1):
    if 'şahıs işaret yok' not in olc(n): continue
    for k_ in (n, n + 1):
        if k_ > B: continue
        a4 = a_parca(k_, 'A4')
        m = re.search(r'şahıs geçişi [^;]*—[^;]*', a4)
        if not m: continue
        EN['eksilti'] += 1
        if 'eksiltili' not in m.group(0): H.append("(3) %d:%d A4 '%s' — şahıs işareti olmayan ayet, 'eksiltili' notu yok" % (S, k_, m.group(0)[:40]))

# ── (4) OZEL_AD_TETIK ──
for n in range(A, B + 1):
    for l in M[n].split('\n')[1:]:
        if not l.startswith(('◈K', '◈B')): continue
        for q, k in re.findall(Q + r" \((\d+)\. kelime\)", l):
            EN['ozel_ad_tetik'] += 1
            if '|PN|' in MOR.get(n, {}).get(int(k), '') + '|' and 'özel ad' not in l:
                H.append("(4) %d:%d %s '%s' (%s. kelime) morph PN — satırda 'özel ad' notu yok" % (S, n, l[:2], q, k))

# ── (5) SEG_YUZEY_KARSILIK ──
_sp = _BK + 'b%s/yap/seg.py' % NN
if os.path.exists(_sp):
    _g = {}
    try: exec(open(_sp, encoding='utf-8').read(), _g)
    except Exception: _g = {}
    for n, segs in sorted(_g.get('SEG', {}).items()):
        if not (A <= n <= B): continue
        for tr, ar, its in segs:
            low = tr.lower().replace('İ', 'i').replace('I', 'ı')
            for it in its:
                m = re.match(r"'([^']+)' '(?:[^' ]|'(?=[a-zâîû]))+' (?:karşılığı|açılımı)", it)
                if not m: continue
                EN['seg_yuzey'] += 1
                x = m.group(1).rstrip('-').lower()
                ilk = x.split()[0]
                kok = ilk[:-1] if len(ilk) >= 4 else ilk  # ünsüz yumuşaması / ünlü daralması ('azap' → 'azabı', 'de-' → 'diye-') için son harf düşer
                if len(ilk) == 3 and ilk[-1] in 'pçtk': kok = ilk[:-1]
                ady = [kok] + ([ilk[:-2] + ilk[-1]] if len(ilk) >= 4 else []) + ([ilk[0] + 'i'] if len(ilk) == 2 and ilk[1] == 'e' else [])  # ünlü düşmesi ('kavim' → 'kavmi'), daralma ('de-' → 'diye-')
                if any(k_ in low for k_ in ady) or 'içinde' in it or 'açılımı' in it: continue
                H.append("(5) %d:%d seg notu '%s' — meal kesiminde ('%s') geçmiyor, 'içinde' biçimi yok" % (S, n, m.group(1), tr[:40]))

print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum26_kurallar hata: %d' % len(H))
