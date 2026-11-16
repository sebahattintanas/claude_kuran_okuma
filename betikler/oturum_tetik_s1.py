# -*- coding: utf-8 -*-
"""oturum_tetik_s1.py — oturum_tetik.py'deki S1 lemma kısıtının salt-okur kopyası (denetim araçları için).
izinli(kök, lemma) → True: kök S1 kısıtlı değilse ya da lemma S1'in seçtiği izinli lemmalardansa."""
from collections import Counter, defaultdict
from oturum_ortak import MORPH, ozellik, N

S1 = {'روح': [29], 'سوع': [48], 'سنو': [12, 7], 'سمو': [310], 'نعم': [33]}
_say = defaultdict(Counter)
for segs in MORPH.values():
    for t, f in segs:
        r, l = ozellik(f, 'ROOT:'), ozellik(f, 'LEM:')
        if r and l: _say[r][l] += 1
IZIN = {}
for r, ns in S1.items():
    r = N(r)
    sec = [l for l, c in _say[r].items() if c in ns]
    assert len(sec) == len(ns), 'S1 lemma seçimi tekil değil: %s %s' % (r, sec)
    IZIN[r] = set(sec)


def izinli(kok, lem):
    k = N(kok)
    return k not in IZIN or N(lem or '') in {N(x) for x in IZIN[k]}
