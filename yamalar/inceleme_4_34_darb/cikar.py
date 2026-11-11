import collections, json
W = collections.OrderedDict()
for l in open('/home/claude/calisma/morph.txt', encoding='utf-8'):
    p = l.rstrip('\n').split('\t'); s, a, w, seg = p[0].split(':')
    W.setdefault((int(s), int(a), int(w)), []).append((p[1], p[2], p[3]))
keys = list(W)
idx = {k: i for i, k in enumerate(keys)}
def bilgi(k):
    segs = W[k]; return ''.join(x[0] for x in segs), ' || '.join(f'{x[1]}:{x[2]}' for x in segs)
def lem(k):
    out = []
    for x in W[k]:
        for f in x[2].split('|'):
            if f.startswith('LEM:'): out.append(f[4:])
    return out
R = []
for k in keys:
    feats = ' '.join(x[2] for x in W[k])
    if 'ROOT:\u0636\u0631\u0628' not in feats: continue
    i = idx[k]
    ctx = [keys[j] for j in range(i - 3, i + 5) if 0 <= j < len(keys) and keys[j][:2] == k[:2]]
    R.append(dict(k=k, kelime=bilgi(k)[0], morph=bilgi(k)[1], sonra=[bilgi(c)[0] for c in ctx if c[2] > k[2]], once=[bilgi(c)[0] for c in ctx if c[2] < k[2]],
                  sonra_lem=[lem(c) for c in ctx if c[2] > k[2]], once_lem=[lem(c) for c in ctx if c[2] < k[2]]))
json.dump([dict(r, k=list(r['k'])) for r in R], open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), 'darb.json'), 'w'), ensure_ascii=False, indent=0)
print(len(R), 'geçiş', len({r['k'][:2] for r in R}), 'ayet')
