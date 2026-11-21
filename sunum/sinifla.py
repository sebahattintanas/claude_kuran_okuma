# -*- coding: utf-8 -*-
# sinifla.py - oturum disi: oturum_say/lem listesini siniflar (bu ayet / basilan / eski kayit / okunmus / henuz okunmamis)
import sys, re
SON = 92  # sûre 6 okunmuş son ayet; her blok başında blok son ayetine güncellenir (sed)
import os as _os
S_OKU = int(_os.environ.get('SURE', '6')); SON_ = int(_os.environ.get('SON') or SON)
BAS = {l.strip() for l in open('/home/claude/sunum/basilan.txt') if l.strip()}
ref = sys.argv[1]; S = int(ref.split(':')[0])
txt = '\n'.join(l for l in sys.stdin.read().splitlines() if not l.startswith(('sûre içi','kalıp','lemma dizisi','lemma ','kök ')))
lst = re.findall(r'(\d+):(\d+)(†)?(?:×\d+)?', txt)
def oku(s, a):
    # sûre 2 TAM (2026-11-08), sûre 3 TAM (2026-11-09), sûre 4 TAM (2026-11-15); sûre 5 okunuyor; 6-8 sıkıştırılmış dönem → henüz okunmamış
    if s == S_OKU: return a <= SON_
    return s < S_OKU or s >= 9
out = {'bu': [], 'basilan': [], 'eski': 0, 'okunmus': 0, 'okunmus_si': 0, 'henuz': 0, 'henuz_si': 0}
seen = set()
for s, a, _ in lst:
    s, a = int(s), int(a)
    k = '%d:%d' % (s, a)
    if k in seen: continue
    seen.add(k)
    if k == ref: out['bu'].append(k)
    elif k in BAS and oku(s, a): out['basilan'].append(k)
    elif s == 2 and a <= 20: out['eski'] += 1
    elif oku(s, a):
        out['okunmus'] += 1
        if s == S: out['okunmus_si'] += 1
    else:
        out['henuz'] += 1
        if s == S: out['henuz_si'] += 1
print(len(seen), out)
