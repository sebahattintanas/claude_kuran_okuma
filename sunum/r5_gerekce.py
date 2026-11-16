# bölüm 9 kuralı 4: R5 'gerekçe biçim farkı' metni betikle — harekesiz kalıp ile her sûre içi eş arasındaki yazım farkı, eş başına adıyla
# fark sınıfları: 'elif yazımı' (üstün / hançer elif ↔ yazılı elif), 'zamir eki', 'fiil çekimi', 'i'râb', 'önek'; sûre dışı eş yazılmaz;
# harekesiz modda hareke farkı gerekçe olamaz (harekesiz kalıp onu siler)
# kullanım (/home/claude'dan): python3 sunum/r5_gerekce.py S A i j   (lemma dizisi anahtarı 'dizi S A i j' ile eş)
import sys, os, re, unicodedata as ud
sys.path.insert(0, '/home/claude/calisma'); os.chdir('/home/claude/calisma')
from oturum_ortak import MORPH, ozellik
from collections import OrderedDict
S, A, i, j = map(int, sys.argv[1:5])
BAS = set(open('/home/claude/sunum/basilan.txt', encoding='utf-8').read().split())
def govde(segs): return tuple(ozellik(f, 'LEM:') for t, f in segs if ozellik(f, 'LEM:') and 'PREF' not in f and 'SUFF' not in f)
def harekesiz(w): return ''.join(c for c in ud.normalize('NFD', w) if not ud.combining(c) or c == 'ٰ')
W, F = OrderedDict(), {}
for (s, a, w), segs in sorted(MORPH.items()):
    W.setdefault((s, a), []).append(govde(segs))
for _l in open('morph.txt', encoding='utf-8'):  # biçimli segmentler: (biçim, 'ETİKET|özellik|…')
    _p = _l.rstrip('\n').split('\t')
    if len(_p) < 4 or _p[0].count(':') != 3: continue
    _s, _a, _w, _ = map(int, _p[0].split(':')); F.setdefault((_s, _a, _w), []).append((_p[1], _p[2] + '|' + _p[3]))
P = W[(S, A)][i - 1:j]
def siniflar(k1, k2):
    out = []
    for n in range(len(P)):
        s1, s2 = F[k1[:2] + (k1[2] + n,)], F[k2[:2] + (k2[2] + n,)]
        f1 = ' '.join(t for t, f in s1); f2 = ' '.join(t for t, f in s2)
        if harekesiz(f1) == harekesiz(f2): continue
        h1, h2 = harekesiz(f1).replace('ٰ', 'ا'), harekesiz(f2).replace('ٰ', 'ا')
        if h1 == h2 or h1.replace('ا', '') == h2.replace('ا', ''): out.append('elif yazımı'); continue
        pron = lambda s_: tuple(re.sub(r'.*\|', '', f) for t, f in s_ if 'PRON' in f and 'SUFF' in f)
        pref = lambda s_: tuple(re.search(r'LEM:([^|]+)', f).group(1) for t, f in s_ if 'PREF' in f and 'LEM:' in f)
        stem = lambda s_: [f for t, f in s_ if 'PREF' not in f and 'SUFF' not in f]
        if pref(s1) != pref(s2): out.append('önek')
        if pron(s1) != pron(s2): out.append('zamir eki')
        st1, st2 = stem(s1), stem(s2)
        if st1 and st2 and st1[0].startswith('V') and st2[0].startswith('V') and re.sub(r'.*?\|(\d[MF]?[SDP]).*', r'\1', st1[0]) != re.sub(r'.*?\|(\d[MF]?[SDP]).*', r'\1', st2[0]): out.append('fiil çekimi')
        cs = lambda f: (re.search(r'\|(NOM|ACC|GEN)(?:\||$)', f) or [None, None])[1]
        if st1 and st2 and cs(st1[0]) != cs(st2[0]): out.append("i'râb")
    return sorted(set(out))
sonuc = []
for (s, a), v in W.items():
    if s != S or a == A: continue
    for x in range(len(v) - len(P) + 1):
        if v[x:x + len(P)] == P:
            ad = ('%d:%d' % (s, a)) if '%d:%d' % (s, a) in BAS else 'basılmamış eş'
            sonuc.append('%s %s' % (ad, ', '.join(siniflar((S, A, i), (s, a, x + 1))) or 'yazım eş'))
            break
print('biçim farkı (dizi %d %d %d %d): ' % (S, A, i, j) + ('; '.join(sonuc) if sonuc else 'sûre içi eş yok'))
