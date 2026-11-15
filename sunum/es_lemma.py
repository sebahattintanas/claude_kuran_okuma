# bölüm 16 denetimi kuralı 11 (sûre 5): bölümün bütün meal kayıtlarından eş lemmaya farklı karşılık listesi (morph LEM'e göre)
# kullanım (/home/claude'dan): python3 sunum/es_lemma.py <blok no> [<blok no> …]  — bNN/yap/veri.py (MK) + bNN/morph<S>.txt
import sys, os, re, importlib.util as iu, collections, unicodedata as ud
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from sure import S
LEM = {}; TR = collections.defaultdict(set)
for nn in sys.argv[1:]:
    d = '/home/claude/b%02d' % int(nn)
    for l in open('%s/morph%d.txt' % (d, S), encoding='utf-8'):
        loc, f, t, feat = l.rstrip('\n').split('\t'); s, a, w, p = map(int, loc.split(':'))
        m = re.search(r'LEM:([^|]+)', feat)
        if m and 'ROOT:' in feat: LEM[(a, w)] = ud.normalize('NFC', m.group(1))
    sp = iu.spec_from_file_location('veri%s' % nn, d + '/yap/veri.py'); v = iu.module_from_spec(sp); sp.loader.exec_module(v)
    for a, L in v.MK.items():
        for tr, q, items in L:
            for it in items:
                m = re.match(r"'([^']+)' '((?:[^']|'(?=[a-zâîûçğışöü]))+)' (?:karşılığı|açılımı) \((\d+)\. kelime", it)
                if m and (a, int(m.group(3))) in LEM:
                    TR[LEM[(a, int(m.group(3)))]].add((m.group(1), '%d:%d:%s' % (S, a, m.group(3))))
for lem, s in sorted(TR.items()):
    trs = sorted({x[0] for x in s})
    if len(trs) > 1:
        print("%s: %s" % (lem, ' / '.join("'%s' (%s)" % (t, ', '.join(sorted(k for x, k in s if x == t))) for t in trs)))
