# -*- coding: utf-8 -*-
"""oturum_lem.py — LEMMA SAYIMI (salt-okur). Lemma elle yazılmaz: morph.txt'teki bir kelimeden alınır.
Kullanım:
  python3 oturum_lem.py S:A:W [--kok]
    S:A:W : morph kelime numarası (ölçüm/esma_kayit konumlarıyla aynı numaralama)
    --kok : lemma yerine kök sayılır
Çıktı: lemma (ya da kök), korpus token ve ayet sayısı, ayet listesi († = henüz okunmadı), sûre içi."""
import sys
from collections import OrderedDict
from oturum_ortak import MORPH, ozellik, durum

S, A, W = map(int, sys.argv[1].split(':'))
KOK = '--kok' in sys.argv
on = 'ROOT:' if KOK else 'LEM:'
hedef = [ozellik(f, on) for t, f in MORPH[(S, A, W)] if ozellik(f, on) and 'PREF' not in f and 'SUFF' not in f]
assert hedef, '%d:%d:%d kelimesinde %s yok' % (S, A, W, on)
h = hedef[0]   # gövde bölütü (önek/sonek bölütleri atlanır)
tok = 0; ay = OrderedDict()
for (s, a, w), segs in MORPH.items():
    for t, f in segs:
        if ozellik(f, on) == h:
            tok += 1; ay[(s, a)] = ay.get((s, a), 0) + 1
print(('kök' if KOK else 'lemma'), h, '| token', tok, '| ayet', len(ay))
print('liste:', ', '.join(durum(s, a) + ('×%d' % n if n > 1 else '') for (s, a), n in ay.items()))
print('sûre içi (%d):' % S, ', '.join('%d:%d' % x + ('×%d' % n if n > 1 else '') for x, n in ay.items() if x[0] == S) or '—')
