# -*- coding: utf-8 -*-
"""defter.py v2 — bab / çatı / i'râb alanları eklendi.
Yeni alanlar:
  vf     {bab: fiil sayısı}            (VF etiketi yoksa bab 1)
  pas    edilgen fiil sayısı
  apc    [[kelime_sıra, kök, bab], ...]  ACT_PCPL (ism-i fâil)
  ppc    [[kelime_sıra, kök, bab], ...]  PASS_PCPL (ism-i mef'ûl)
  irab   {NOM: n, ACC: n, GEN: n}
  zmn    {PERF: n, IMPF: n, IMPV: n}
"""
import json, re, unicodedata
from collections import Counter, defaultdict

tok = defaultdict(list)
for ln in open('morph.txt', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 4: continue
    loc = p[0].split(':')
    if len(loc) == 5: loc = loc[1:]
    if len(loc) != 4: continue
    s, a, w, g = (int(x) for x in loc)
    f = p[3]
    m = re.search(r'ROOT:([^|]+)', f)
    tok[(s, a)].append({'w': w, 'pos': p[2], 'f': f, 'kok': m.group(1) if m else ''})

def bab(f):
    m = re.search(r'VF:(\d+)', f); return int(m.group(1)) if m else 1

D = json.load(open('defter.json'))
for r in D:
    k = (r['k'][0], r['k'][1])
    ts = tok.get(k, [])
    vf = Counter(); pas = 0; apc = []; ppc = []
    irab = Counter(); zmn = Counter()
    for t in ts:
        f = t['f']; parts = f.split('|')
        if t['pos'] == 'V':
            vf[bab(f)] += 1
            if 'PASS' in parts: pas += 1
            for z in ('PERF','IMPF','IMPV'):
                if z in parts: zmn[z] += 1
        if 'ACT_PCPL' in parts: apc.append([t['w'], t['kok'], bab(f)])
        if 'PASS_PCPL' in parts: ppc.append([t['w'], t['kok'], bab(f)])
        for c in ('NOM','ACC','GEN'):
            if c in parts: irab[c] += 1
    r['vf'] = {str(b): n for b, n in sorted(vf.items())}
    r['pas'] = pas
    r['apc'] = apc
    r['ppc'] = ppc
    r['irab'] = dict(irab)
    r['zmn'] = dict(zmn)
json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)

print('defter v2 yazıldı: %d ayet' % len(D))
tv = Counter(); tp = 0; ta = 0; tpp = 0
for r in D:
    for b, n in r['vf'].items(): tv[int(b)] += n
    tp += r['pas']; ta += len(r['apc']); tpp += len(r['ppc'])
print('fiil bab dağılımı:', dict(sorted(tv.items())))
print('edilgen fiil: %d | ism-i fâil: %d | ism-i mef\'ûl: %d' % (tp, ta, tpp))
ir = Counter()
for r in D:
    for c, n in r['irab'].items(): ir[c] += n
print('i\'râb:', dict(ir))
zz = Counter()
for r in D:
    for c, n in r['zmn'].items(): zz[c] += n
print('zaman:', dict(zz))
print('edilgen fiil oranı: %.3f' % (tp / sum(tv.values())))
print('ism-i mef\'ûl / ism-i fâil oranı: %.3f' % (tpp / ta))
