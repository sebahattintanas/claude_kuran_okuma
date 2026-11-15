# karşılık çakışması çıkarıcı (bölüm 9 denetimi kuralı 3): ARIZA meal maddelerinden "'TR' 'AR' karşılığı/açılımı" çiftleri
import sys, ast, re, collections
TR = collections.defaultdict(set)
SON = set()  # son dosyadaki karşılıklar — KÖK eşlemesi yalnız bunlara dokunan gruplar için
for f in sys.argv[1:]:
    s = open(f, encoding='utf-8').read()
    d = ast.literal_eval('{' + s + '}')
    for v in d.values():
        for m in v:
            if not m.startswith('meal'): continue
            for tr, ar in re.findall(r"'([^']+)' '((?:[^' ]|'(?=[a-zâîûçğışöü])|'(?=' ))+)' (?:karşılığı|açılımı)", m):
                TR[tr].add(ar)
                if f == sys.argv[-1]: SON.add(tr)
for tr, ars in sorted(TR.items()):
    if len(ars) > 1: print(tr, '←', sorted(ars))

# bölüm 4 (sûre 5) denetimi kuralı 4: Türkçe fiil kökü eşlemesi — açılımın fiil öğesi ('nimet ver-' → 'ver-', 'haram kılınmış' → 'kıl-', 'giren' → 'gir-')
# bölüm 5 kuralı 3: ek soyma kök sınırıyla; '-acak / -ecek', '-me / -ma', '-mek / -mak', kaynaştırma 'y', ünsüz değişimi d → t
EKLER = ('ınmış', 'inmiş', 'unmuş', 'ünmüş', 'ılmış', 'ilmiş', 'ulmuş', 'ülmüş', 'acak', 'ecek', 'mak', 'mek', 'mış', 'miş', 'muş', 'müş', 'ma', 'me', 'an', 'en', '-')
def kok(tr):
    w = tr.split()[-1].rstrip('-')
    for e in EKLER:
        if w.endswith(e) and len(w) - len(e) >= 2:
            w = w[:-len(e)]
            if e in ('an', 'en', 'acak', 'ecek'):
                if len(w) >= 3 and w[-1] == 'y' and w[-2] in 'aeıioöuü': w = w[:-1]
                elif w[-1] == 'd': w = w[:-1] + 't'
            break
    return w
for _t, _k in [('güç yetiren', 'yetir'), ('güç yetir-', 'yetir'), ('aşırı giden', 'git'), ('aşırı git-', 'git'), ('uzatacak', 'uzat'), ('uzat-', 'uzat'),
               ('öldürme', 'öldür'), ('öldür-', 'öldür'), ('hüsrana uğrayan', 'uğra'), ('giren', 'gir'), ('haram kılınmış', 'kıl'), ('kabul eden', 'et')]:
    assert kok(_t) == _k, (_t, kok(_t))
KG = collections.defaultdict(dict)
for tr, ars in TR.items():
    KG[kok(tr)][tr] = ars
for k, d in sorted(KG.items()):
    if len(d) > 1 and SON & set(d):
        print('KÖK %s- ←' % k, '; '.join('%s %s' % (t, sorted(a)) for t, a in sorted(d.items())))
