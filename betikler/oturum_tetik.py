# -*- coding: utf-8 -*-
"""oturum_tetik.py — ◈K / ◈B TETİK TARAMASI (salt-okur; 'tetik2' denetiminin depoya giren sürümü).
Kullanım: python3 oturum_tetik.py S A B <metin_modülü>
Kural (OKU_BENI_OTURUM, ONKAYIT_mercekler §3-4 + §8 S1): ayette tetik kökü varsa satır DOLU olmalı,
yoksa satır '—' olmalı; ikisinin de tersi uyuşmazdır. Tetik kökleri ön-kayıttaki kök anmalarıdır;
S1 lemma kısıtları (روح سوع سنو سمو / نعم) lemma ELLE YAZILMADAN, S1'in verdiği korpus token
sayısıyla morph.txt'ten seçilir (her sayı tek lemma seçmeli — assert)."""
import sys, importlib
from collections import Counter, defaultdict
from oturum_ortak import MORPH, ozellik, N

S, A1, A2, MOD = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
T = importlib.import_module(MOD)

K_KOK = 'سمو أرض شمس قمر نجم كوكب ليل نهر فلك سحب روح موه بحر جبل يوم أجل سنو عمر سوع دهر أبد حين'
B_KOK = 'أنس دبب نعم طير نبت شجر خلق نطف علق زوج حمل وضع أنث عنق ذقن يدي عين سمع بصر جلد قلب حيي موت عمر'
# S1 (2026-10-06): kök → izinli lemmaların korpus token sayısı
S1 = {'روح': [29], 'سوع': [48], 'سنو': [12, 7], 'سمو': [310], 'نعم': [33]}

say = defaultdict(Counter)
for segs in MORPH.values():
    for t, f in segs:
        r, l = ozellik(f, 'ROOT:'), ozellik(f, 'LEM:')
        if r and l:
            say[r][l] += 1
IZIN = {}
for r, ns in S1.items():
    r = N(r)
    sec = [l for l, c in say[r].items() if c in ns]
    assert len(sec) == len(ns), 'S1 lemma seçimi tekil değil: %s %s' % (r, sec)
    IZIN[r] = set(sec)
KS = {N(x) for x in K_KOK.split()}
BS = {N(x) for x in B_KOK.split()}
assert all(r in say for r in KS | BS), 'ölü tetik kökü: %s' % [r for r in KS | BS if r not in say]


def tetik(n, kume):
    out = []
    for (s, a, w), segs in sorted(MORPH.items()):
        if (s, a) != (S, n):
            continue
        for t, f in segs:
            r, l = ozellik(f, 'ROOT:'), ozellik(f, 'LEM:')
            if r in kume and (r not in IZIN or l in IZIN[r]) and r not in out:
                out.append(r)
    return out


def satir(n, tag):
    for ln in T.M[n].split('\n'):
        if ln.startswith(tag + ' — '):
            return ln[len(tag) + 3:].strip()
    return None


uy = 0
for n in range(A1, A2 + 1):
    for tag, kume in (('◈K', KS), ('◈B', BS)):
        tk = tetik(n, kume); st = satir(n, tag)
        if st is None:
            print('UYUŞMAZ %d:%d %s satırı YOK' % (S, n, tag)); uy += 1; continue
        dolu = st != '—'
        if bool(tk) != dolu:
            uy += 1
            print('UYUŞMAZ %d:%d %s tetik=%s satır=%s' % (S, n, tag, ' '.join(tk) or '—', 'dolu' if dolu else '—'))
        else:
            print('  %d:%d %s tetik=%s satır=%s' % (S, n, tag, ' '.join(tk) or '—', 'dolu' if dolu else '—'))
    for tag in ('◈D', '◈A'):
        if satir(n, tag) is None:
            print('UYUŞMAZ %d:%d %s satırı YOK' % (S, n, tag)); uy += 1
print('tetik: %d ayet, %d uyuşmaz' % (A2 - A1 + 1, uy))
