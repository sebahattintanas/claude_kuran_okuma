# karşılık çakışması çıkarıcı (bölüm 9 denetimi kuralı 3): ARIZA meal maddelerinden "'TR' 'AR' karşılığı/açılımı" çiftleri
import sys, ast, re, collections
TR = collections.defaultdict(set)
for f in sys.argv[1:]:
    s = open(f, encoding='utf-8').read()
    d = ast.literal_eval('{' + s + '}')
    for v in d.values():
        for m in v:
            if not m.startswith('meal'): continue
            for tr, ar in re.findall(r"'([^']+)' '((?:[^' ]|'(?=[a-zâîûçğışöü]))+)' (?:karşılığı|açılımı)", m):
                TR[tr].add(ar)
for tr, ars in sorted(TR.items()):
    if len(ars) > 1: print(tr, '←', sorted(ars))
