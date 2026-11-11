# yakınlık / ihtiyaç sayımları: 4:36 dizisinin öğelerini taşıyan ayetler ve öğe sırası
import collections, re, json
W = collections.OrderedDict()
for l in open('/home/claude/calisma/morph.txt', encoding='utf-8'):
    p = l.rstrip('\n').split('\t'); s, a, w, seg = p[0].split(':')
    W.setdefault((int(s), int(a)), []).append((int(w), p[1], p[2], p[3]))
def lem(f):
    m = re.search(r'LEM:([^|]+)', f); return m.group(1) if m else ''
OGE = {  # lemma → öğe adı
 '\u0648\u0627\u0644\u0650\u062f': 'vâlid', '\u0642\u064f\u0631\u0652\u0628\u064e\u0649': 'qurbâ', '\u0623\u064e\u0642\u0652\u0631\u064e\u0628': 'aqrab',
 '\u064a\u064e\u062a\u0650\u064a\u0645': 'yetîm', '\u0645\u0650\u0633\u0652\u0643\u0650\u064a\u0646': 'miskîn', '\u062c\u0627\u0631': 'câr',
 '\u0635\u0627\u062d\u0650\u0628': 'sâhib', '\u0633\u064e\u0628\u0650\u064a\u0644': 'sebîl', '\u0633\u0622\u0626\u0650\u0644': 'sâ\'il', '\u0631\u064e\u0642\u064e\u0628\u064e\u0629': 'raqabe',
}
# lemma adlarını morph'tan doğrula
seen = collections.Counter()
for k, segs in W.items():
    for w, f, pos, feat in segs:
        L = lem(feat)
        if L in OGE: seen[OGE[L]] += 1
print('lemma eşleşmesi:', dict(seen))
R = []
for k, segs in W.items():
    seq = []
    for w, f, pos, feat in segs:
        L = lem(feat)
        if L in OGE:
            o = OGE[L]
            if o == 'sebîl':  # yalnız 'ibn' + 'sebîl'
                prev = [lem(x[3]) for x in segs if x[0] == w - 1]
                if '\u0627\u0628\u0652\u0646' not in prev: continue
                o = 'ibnü\'s-sebîl'
            if o == 'sâhib':
                nxt = ''.join(x[1] for x in segs if x[0] == w + 1)
                import unicodedata as ud; nxt = ''.join(c for c in nxt if not ud.combining(c) and c not in '\u06e2')
                if '\u062c\u0646\u0628' not in nxt: continue
                o = "sâhib bi'l-cenb"
            if not seq or seq[-1] != (w, o): seq.append((w, o))
        if L == '\u064a\u064e\u0645\u0650\u064a\u0646' and any(lem(x[3]).startswith("\u0645\u064e\u0644\u064e\u0643") for x in segs if x[0] == w - 1):
            seq.append((w, 'mâ meleket yemîn'))
    core = {o for _, o in seq} & {'qurbâ', 'aqrab', 'yetîm', 'miskîn', "ibnü's-sebîl", 'vâlid'}
    if len(core) >= 3: R.append((k, [o for _, o in seq]))
BAS = set(open('/home/claude/sunum/basilan.txt').read().split())
def ad(k):
    t = '%d:%d' % k
    if t in BAS: return t
    return '(okunmamış)' if 5 <= k[0] <= 8 or (k[0] == 4 and k[1] > 43) else '(okunmuş)'
for k, s in R: print(ad(k), ' → '.join(s))
# 've' CONJ yoğunluğu
cnt = {}
for k, segs in W.items():
    cnt[k] = sum(1 for w, f, pos, feat in segs if pos == 'P' and 'CONJ' in feat and f.startswith('\u0648'))
r = sorted(cnt.values(), reverse=True)
print('4:36 CONJ ve:', cnt[(4, 36)], '| bundan çok CONJ ve taşıyan ayet:', sum(1 for v in cnt.values() if v > cnt[(4, 36)]), '| eşit:', sum(1 for v in cnt.values() if v == cnt[(4, 36)]) - 1, '| korpus ayet', len(cnt))
