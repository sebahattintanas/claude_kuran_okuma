# eş edat listesi için morph etiketi (bölüm 14 denetimi kuralı 1): edatın lemmasıyla eşlenen segmentin etiketi
import glob, re, unicodedata as ud, collections
MORALL = collections.defaultdict(list)
for f in sorted(glob.glob('/home/claude/b*/morph4.txt')):
    for l in open(f, encoding='utf-8'):
        loc, fo, t, feat = l.rstrip('\n').split('\t'); s, a, w, p = map(int, loc.split(':'))
        if s != 4: continue
        if (w, p) not in {(x[0], x[1]) for x in MORALL[a]}:
            MORALL[a].append((w, p, fo, t, feat))
def _n(x):
    x = ''.join(c for c in ud.normalize('NFD', x) if not ud.combining(c))
    return x.replace('إ', 'ا').replace('أ', 'ا').replace('آ', 'ا').replace('ٱ', 'ا').replace('ى', 'ي').replace('ٰ', '')
EDLEM = {"'lâ'": 'لا', "'li'": 'ل', "'bi'": 'ب', "'fe'": 'ف', "'ve'": 'و', "'in'": 'ان', "'inne'": 'ان', "'en'": 'ان', "'enne'": 'ان',
         "'e'": 'ا', "'mâ'": 'ما', "'men'": 'من', "'min'": 'من', "'fî'": 'في', "''alâ'": 'علي', "'ilâ'": 'الي', "'ma'a'": 'مع',
         "'izâ'": 'اذا', "'izen'": 'اذا', "'len'": 'لن', "'lem'": 'لم', "'qad'": 'قد', "'sevfe'": 'سوف', "'summe'": 'ثم', "'ev'": 'او',
         "'illâ'": 'الا', "'yâ'": 'ي', "'hattâ'": 'حتي', "'ellezîne'": 'الذي', "'ellezî'": 'الذي', "'ellâtî'": 'الذي', "''an'": 'عن',
         "'lev'": 'لو', "'ke'": 'ك', "'kâne'": 'كان', "'le'": 'ل'}
ZAMIR = {"'kum'", "'hum'", "'hu'", "'hû'", "'hî'", "'hi'", "'hinne'", "'hunne'", "'himâ'", "'humâ'", "'nâ'", "'û'", "'ûne'", "'tum'", "'him'", "'huve'"}
def etiket(n, w, ed):
    seg = [(feat.split('|')[0], feat) for ww, p, f, t, feat in MORALL[n] if ww == w]
    if not seg: return '?'
    if ed in ZAMIR: return 'PRON'
    if ed == "'hâ'":
        tags = [t for t, _ in seg]
        return 'PRON' if 'PRON' in tags else ('ATT' if 'ATT' in tags else tags[0])
    if ed == "'ke'":
        tags = [t for t, _ in seg]
        return 'PRON' if 'PRON' in tags else 'P'
    hedef = EDLEM.get(ed)
    if hedef:
        for t, feat in seg:
            m = re.search(r'LEM:([^|]+)', feat)
            if m and _n(m.group(1)).rstrip('ّ') == hedef: return 'V' if t in ('PERF', 'IMPF') else t
    return seg[0][0]
