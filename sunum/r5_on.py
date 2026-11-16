# bölüm 8 kuralı 1: R5 'tutmuyor' satırında önek kesilmiş terim varsa, lemma dizisinin her sûre içi eşinin (henüz okunmamış eş dahil) kendi anahtarıyla öneksiz '--on' sayımı koşulur
# çıktı basılmamış eşin numarasını yazmaz; yalnız sayısını ve sûre içi sonucu yazar
# kullanım (/home/claude'dan): python3 sunum/r5_on.py S A i j  (lemma dizisi anahtarı 'dizi S A i j' ile eş)
import sys, os, re, subprocess
sys.path.insert(0, '/home/claude/calisma'); os.chdir('/home/claude/calisma')
from oturum_ortak import MORPH, ozellik
from collections import OrderedDict
S, A, i, j = map(int, sys.argv[1:5])
BAS = set(open('/home/claude/sunum/basilan.txt', encoding='utf-8').read().split())
def govde(segs):
    return tuple(ozellik(f, 'LEM:') for t, f in segs if ozellik(f, 'LEM:') and 'PREF' not in f and 'SUFF' not in f)
W = OrderedDict()
for (s, a, w), segs in sorted(MORPH.items()): W.setdefault((s, a), []).append(govde(segs))
P = W[(S, A)][i - 1:j]
sonuc = []
for (s, a), v in W.items():
    if s != S or a == A: continue
    for x in range(len(v) - len(P) + 1):
        if v[x:x + len(P)] == P:
            out = subprocess.run(['python3', 'oturum_say.py', '%d:%d' % (s, a), '%d-%d' % (x + 1, x + len(P)), '--on'], capture_output=True, text=True).stdout
            m = re.search(r'sûre içi \(%d\): (.*)' % S, out)
            n = len(m.group(1).split(', ')) if m and m.group(1).strip() else 0
            ad = ('%d:%d' % (s, a)) if '%d:%d' % (s, a) in BAS else 'basılmamış eş'
            sonuc.append((ad, n))
            break
print('öneksiz eş koşusu (dizi %d %d %d %d): ' % (S, A, i, j) + ('; '.join('%s → önek kesilmiş sûre içi %d' % x for x in sonuc) if sonuc else 'sûre içi eş yok'))
