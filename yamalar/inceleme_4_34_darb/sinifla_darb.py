import json, collections
import os
R = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'darb.json')))
def oku(s, a):  # sinifla.py mantığı: 5-8 okunmamış; sûre 4'te SON=35'ten sonrası okunmamış
    if 5 <= s <= 8: return 'okunmamış'
    if s == 4 and a > 35: return 'okunmamış (sûre içi)'
    return 'okunmuş'
def cerceve(r):
    s, a, w = r['k']
    import unicodedata as ud, re as _re
    yal = lambda t: _re.sub('[\u0671]', '\u0627', ''.join(c for c in ud.normalize('NFD', t) if not ud.combining(c) and c not in '\u06e5\u06e6\u0640'))
    s0 = yal(r['sonra'][0]) if r['sonra'] else ''
    if s0.startswith('\u0628\u0639\u0635\u0627') or s0 == '\u0628\u0647' or s0 == '\u0628\u0627\u0644\u064a\u0645\u064a\u0646' or s0 == '\u0628\u0628\u0639\u0636\u0647\u0627': return "C bir aletle vurma ('bi' + alet)"  # harekeli önek eşlemesi şedde sırası yüzünden kaçırıyordu
    if '\u0647\u0630\u0627 \u0627\u0644\u0642\u0631\u0621\u0627\u0646' in yal(' '.join(r['sonra'][:5])): return 'A mesel / örnek getirme'  # 'min kulli mesel' kelime penceresinin dışında
    sonra = r['sonra']; sl = [x for L in r['sonra_lem'] for x in L]; ol = [x for L in r['once_lem'] for x in L]
    j = ' '.join(sonra[:3])
    if '\u0645\u064e\u062b\u064e\u0644' in sl[:8] or '\u0645\u064e\u062b\u064e\u0644' in ol or (r['once'] and yal(r['once'][-1]) == '\u0643\u0630\u0644\u0643') or s0 == '\u0644\u0643': return 'A mesel / örnek getirme'  # 'kezâlike yadribu'llâh' ve 'darabûhu leke' mesel çerçevesi
    if sonra and (sonra[0].startswith('\u0641\u0650\u0649') or (len(sonra) > 1 and sonra[1].startswith('\u0641\u0650\u0649') and r['kelime'].startswith('\u0636\u064e\u0631\u0652\u0628'))): return 'B yeryüzünde / yolda gitme (fî)'
    if '\u0639\u064e\u0644\u064e\u064a' in j or '\u0639\u064e\u0644\u064e\u0649\u0670' in j or '\u0639\u064e\u0644\u064e\u064a\u0652\u0647\u0650\u0645' in j or '\u0628\u064e\u064a\u0652\u0646\u064e\u0647\u064f\u0645' in j: return "D üzerine koyma / araya çekme ('alâ, beyne)"
    if sonra and sonra[0].startswith(('\u0628\u0650\u0651\u0639\u064e\u0635\u064e\u0627', '\u0628\u0650\u0651\u0647\u0650')): return "C bir aletle vurma ('bi' + alet)"
    if sonra and sonra[0].startswith('\u0644\u064e\u0647\u064f\u0645\u0652') : return 'E yol açma'
    if sonra and sonra[0].startswith('\u0628\u0650\u0623\u064e\u0631\u0652\u062c\u064f\u0644'): return "F ayakla vurma ('bi' + organ)"
    if sonra and sonra[0].startswith('\u0639\u064e\u0646'): return "G ''an' ile (çevirme, vazgeçme)"
    return 'H canlıya / bedene doğrudan vurma'
BAS = set(open('/home/claude/sunum/basilan.txt').read().split())
G = collections.defaultdict(list)
for r in R:
    G[cerceve(r)].append(r)
for g in sorted(G):
    L = G[g]
    st = collections.Counter(oku(*r['k'][:2]) for r in L)
    print(f"{g}: {len(L)} geçiş, {len({tuple(r['k'][:2]) for r in L})} ayet  {dict(st)}")
    for r in L:
        sa = '%d:%d' % tuple(r['k'][:2])
        k = ':'.join(map(str, r['k'])) if sa in BAS else '(' + oku(*r['k'][:2]) + ')'
        print('    ', k, r['kelime'], '|', ' '.join(r['sonra'][:3]))
