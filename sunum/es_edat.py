# bölüm 1 (sûre 5) denetimi kuralı 6: eş edat / zamir karşılık listesi — morph etiketli başlıklar, zamirler birleşik ('hu' / 'hû' / 'hî' / 'hi'; 'hum' / 'him'), 'bi' dahil
# kullanım (/home/claude'dan): python3 sunum/es_edat.py <blok no> [<blok no> …]  — bNN/yap/veri.py (MK) + bNN/morph<S>.txt; yalnız iki ya da daha çok geçişli başlıklar
import sys, os, re, importlib.util as iu, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from sure import S
import edat_etiket as E
BIR = {"'hû'": "'hu'", "'hî'": "'hu'", "'hi'": "'hu'", "'hu'": "'hu'", "'him'": "'hum'", "'hum'": "'hum'", "'hinne'": "'hunne'", "'hunne'": "'hunne'", "'himâ'": "'humâ'", "'humâ'": "'humâ'", "'ûne'": "'û'"}
G = collections.defaultdict(lambda: collections.defaultdict(list))
for nn in sys.argv[1:]:
    d = '/home/claude/b%02d' % int(nn)
    sp = iu.spec_from_file_location('veri%s' % nn, d + '/yap/veri.py'); v = iu.module_from_spec(sp); sp.loader.exec_module(v)
    for a, L in v.MK.items():
        for tr, q, items in L:
            for it in items:
                m = re.match(r"('(?:[^']|'(?=[a-zâîûçğışöü]))+') (\d+)\. kelimede (karşılıksız|'([^']*)' ile)", it)
                if not m: continue
                ed, w = m.group(1), int(m.group(2))
                if ed not in E.EDLEM and ed not in E.ZAMIR and ed not in BIR and ed != "'hâ'": continue
                tag = E.etiket(a, w, ed)
                bas = BIR.get(ed, ed)
                kar = 'karşılıksız' if m.group(3) == 'karşılıksız' else "'%s' ile" % m.group(4)
                G['%s (%s)' % (bas, tag)][kar].append('%d:%d %d.' % (S, a, w))
out = []
for bas in sorted(G):
    tot = sum(len(x) for x in G[bas].values())
    if tot < 2: continue
    out.append(bas + ' — ' + ', '.join('%s (%s)' % (k, ', '.join(v) + ' kelime') for k, v in sorted(G[bas].items())))
print('; '.join(out))
