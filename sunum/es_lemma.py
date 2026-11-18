# bölüm 16 denetimi kuralı 11 (sûre 5): bölümün bütün meal kayıtlarından eş lemmaya farklı karşılık listesi (morph LEM'e göre)
# kullanım (/home/claude'dan): python3 sunum/es_lemma.py <blok no> [<blok no> …]  — bNN/yap/veri.py (MK) + bNN/morph<S>.txt
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK
import sys, os, re, importlib.util as iu, collections, unicodedata as ud
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from sure import S
LEM = {}; TR = collections.defaultdict(set)
NUM = '--numarasiz' in sys.argv  # bölüm 10 denetimi kuralı 9: bu oturumda basılmamış konumlar numarasız ('okunmuş N konum')
BAS = {l.strip() for l in open('/home/claude/sunum/basilan.txt') if l.strip()}
def _liste(ks):
    if not NUM: return ', '.join(ks)
    kal = [k for k in ks if ':'.join(k.split(':')[:2]) in BAS]; n = len(ks) - len(kal)
    return ', '.join(kal + (['okunmuş %d konum' % n] if n else []))
for nn in [x for x in sys.argv[1:] if x != '--numarasiz']:
    d = _BK + 'b%02d' % int(nn)
    for l in open('%s/morph%d.txt' % (d, S), encoding='utf-8'):
        loc, f, t, feat = l.rstrip('\n').split('\t'); s, a, w, p = map(int, loc.split(':'))
        m = re.search(r'LEM:([^|]+)', feat)
        if m and 'ROOT:' in feat: LEM[(a, w)] = ud.normalize('NFC', m.group(1))
    sp = iu.spec_from_file_location('veri%s' % nn, d + '/yap/veri.py'); v = iu.module_from_spec(sp); sp.loader.exec_module(v)
    for a, L in v.MK.items():
        for tr, q, items in L:
            for it in items:
                m = re.match(r"'([^']+)' '((?:[^']|'(?=[a-zâîûçğışöü])|'(?=' ))+)' (?:karşılığı|açılımı) \(((?:\d+(?:-\d+)?\.,? (?:ve )?)+)kelime", it)  # bölüm 7 kuralı 5: "(N. ve M. kelime" her numara
                if not m: continue
                for x in re.findall(r'(\d+)(?:-(\d+))?\.', m.group(3)):
                    for w in range(int(x[0]), int(x[1] or x[0]) + 1):
                        if (a, w) in LEM: TR[LEM[(a, w)]].add((m.group(1), '%d:%d:%d' % (S, a, w), m.group(2)))
for lem, s in sorted(TR.items()):
    trs = sorted({x[0] for x in s})
    if len(trs) > 1:  # Arapça lemma yazılmaz: eş lemmanın ◇ biçimleriyle anılır
        adl = ' / '.join("'%s'" % a for a in sorted({x[2] for x in s}))
        print("%s (morph LEM eşit): %s" % (adl, ' / '.join("'%s' (%s)" % (t, _liste(sorted(k for x, k, _ in s if x == t))) for t in trs)))
