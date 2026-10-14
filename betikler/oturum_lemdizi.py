# oturum_lemdizi.py — LEMMA DİZİSİ SAYIMI (salt-okur; harekesiz kalıbın imlâ gürültüsünü aşar). Kullanım: S A i j — bir ayetteki ardışık morph kelimelerinin gövde lemmaları dizisini korpusta arar
import sys
from oturum_ortak import MORPH, ozellik, durum
from collections import OrderedDict
S,A,i,j=map(int,sys.argv[1:5])
def govde(segs):
    return tuple(ozellik(f,'LEM:') for t,f in segs if ozellik(f,'LEM:') and 'PREF' not in f and 'SUFF' not in f)
W=OrderedDict()
for (s,a,w),segs in sorted(MORPH.items()): W.setdefault((s,a),[]).append(govde(segs))
P=W[(S,A)][i-1:j]
bul=[k for k,v in W.items() if any(v[x:x+len(P)]==P for x in range(len(v)-len(P)+1))]
print('lemma dizisi', P, '| ayet', len(bul)); print(', '.join(durum(*k) for k in bul))
