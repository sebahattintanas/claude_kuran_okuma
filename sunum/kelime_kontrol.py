# bölüm 10 denetimi kuralları 6 ve 12 (oturum dışı yardımcı; salt okur):
#  (6) ◇ / ◈ satırları ve ARIZA'daki "'X' N. kelimede" / "'X' (N. kelime" / "'tr' 'X' karşılığı (N. kelime" iddiaları morph kelimesiyle eşlenir
#  (12) meal maddesinde morph PRON (SUFF dahil) taşıyan her kelime için "'zamir' N. kelimede" kaydı aranır
# kullanım (/home/claude'dan): python3 sunum/kelime_kontrol.py A B NN   (bNN/morph4.txt: konum \t biçim \t tür \t özellik)
import re, sys, ast, collections, difflib, unicodedata as ud
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'; suf = '_4_%d_%d.txt' % (A, B)
W = collections.defaultdict(lambda: collections.defaultdict(list))
for l in open('/home/claude/b%s/morph4.txt' % NN, encoding='utf-8'):
    loc, f, t, feat = l.rstrip('\n').split('\t')
    s, a, w, p = map(int, loc.split(':'))
    W[a][w].append((f, t, feat))
N = lambda x: ud.normalize('NFC', x)
def lem(seg): m = re.search(r'LEM:([^|]+)', seg[2]); return N(m.group(1)) if m else ''
def pron(seg, kisi): return seg[2].startswith('PRON') and seg[2].split('|')[-1] == kisi
P = {
 "'inne'": lambda s: lem(s) == N('إِنّ'), "'innemâ'": lambda s: lem(s) == N('إِنّ'), "'ilâ'": lambda s: lem(s) == N('إِلَى'),
 "'bi'": lambda s: lem(s) == N('ب'), "'li'": lambda s: lem(s) == N('ل'), "'mâ'": lambda s: lem(s) == N('ما'),
 "'ve'": lambda s: lem(s) == N('و'), "'lâ'": lambda s: lem(s) == N('لا'), "''an'": lambda s: lem(s) == N('عَن'),
 "'ellezîne'": lambda s: lem(s) == N('الَّذِي'), "'min'": lambda s: lem(s) == N('مِن'), "'iz'": lambda s: lem(s) == N('إِذ'),
 "'kâne'": lambda s: lem(s) == N('كانَ'), "'hâ'": lambda s: lem(s) == N('ه'), "'fî'": lambda s: lem(s) == N('فِي'),
 "'fe'": lambda s: lem(s) == N('ف'), "'men'": lambda s: lem(s) == N('مَن'), "'em'": lambda s: lem(s) == N('أَم'),
 "''alâ'": lambda s: lem(s) == N('عَلَى'), "'ev'": lambda s: lem(s) == N('أَو'), "'summe'": lambda s: lem(s) == N('ثُمّ'),
 "'nâ'": lambda s: pron(s, '1P'), "'ke'": lambda s: pron(s, '2MS'), "'ûne'": lambda s: pron(s, '3MP'),
 "'hum'": lambda s: pron(s, '3MP'), "'him'": lambda s: pron(s, '3MP'), "'tum'": lambda s: pron(s, '2MP'),
 "'entum'": lambda s: pron(s, '2MP'), "'hû'": lambda s: pron(s, '3MS'), "'hî'": lambda s: pron(s, '3MS'),
 "'huve'": lambda s: pron(s, '3MS'), "'hi'": lambda s: pron(s, '3MS'), "'hu'": lambda s: pron(s, '3MS'),
 "'û'": lambda s: pron(s, '3MP'), "'levlâ'": lambda s: lem(s) == N('لَوْلا'), "'le'": lambda s: lem(s) == N('ل'),
 "'en'": lambda s: lem(s) == N('أَن'), "'illâ'": lambda s: lem(s) == N('إِلّا'), "'lem'": lambda s: lem(s) == N('لَم'),
 "'qad'": lambda s: lem(s) == N('قَد'), "'sevfe'": lambda s: lem(s) == N('سَوْف'), 'lafız': lambda s: lem(s) == N('اللَّه'),
}
mp = {'ب':'b','ت':'t','ث':'s','ج':'c','ح':'h','خ':'x','د':'d','ذ':'z','ر':'r','ز':'z','س':'s','ش':'ş','ص':'s','ض':'d','ط':'t','ظ':'z','ع':'','غ':'ğ','ف':'f','ق':'q','ك':'k','ل':'','م':'m','ن':'','ه':'h','ة':'','ء':'','أ':'','إ':'','ؤ':'','ئ':''}
def sk_ar(w): return re.sub(r'(.)\1+', r'\1', ''.join(mp.get(c, '') for c in ''.join(f for f, _, _ in w) if not ud.combining(c)))
def sk_la(t): return re.sub(r'(.)\1+', r'\1', ''.join(c for c in t.lower() if c in 'bcdfğhkmqrsştxz'))
bad = 0; nkon = 0
def kontrol(n, txt, yer):
    global bad, nkon
    for m in re.finditer(r"(?:(?<=[\s(])|^)('(?=[^\s'])(?:[^']|'(?=[a-zâîûçğışöü]))+'|lafız) ((?:\d+\.(?: ve |, )?)+) kelimede", txt):
        x, nums = m.group(1), [int(k) for k in re.findall(r'\d+', m.group(2))]
        for k in nums:
            nkon += 1
            if x in P:
                if not any(P[x](s) for s in W[n][k]): bad += 1; print('UYUŞMAZ', yer, n, x, k, [f for f, _, _ in W[n][k]])
            else:
                a, b = sk_ar(W[n][k]), sk_la(x)
                if b and difflib.SequenceMatcher(None, a, b).ratio() < 0.5: bad += 1; print('UYUŞMAZ?', yer, n, x, k, a, b)
    for m in re.finditer(r"(?:(?<=[\s(])|^)'(?=[^\s'])((?:[^']|'(?=[a-zâîûçğışöü]))+)' (?:karşılığı |açılımı )?\(((?:\d+\.(?: ve |, )?)+)(?: kelime)?[;)]", txt):
        x, nums = m.group(1), [int(k) for k in re.findall(r'\d+', m.group(2))]
        for k in nums:
            nkon += 1
            q = "'" + x + "'"
            if q in P:
                if not any(P[q](s) for s in W[n][k]): bad += 1; print('UYUŞMAZ', yer, n, q, k)
                continue
            a, b = sk_ar(W[n][k]), sk_la(x.split()[0] if ' ' in x and k else x)
            if ' ' in x:  # çok kelimeli alıntı: alıntının kelimeleri k'dan başlar
                b = sk_la(x.split()[0])
            if b and difflib.SequenceMatcher(None, a, b).ratio() < 0.5: bad += 1; print('UYUŞMAZ?', yer, n, x, k, a, b)
ns = {'MEAL': {}, 'M': {}}; exec(open(Y + 'metin' + suf).read(), ns)
for n in range(A, B + 1):
    for ln in ns['M'][n].split('\n'):
        kontrol(n, ln, ln[:2])
ar = ast.literal_eval('{' + open(Y + 'ariza' + suf).read() + '}')[(A, B)]
for it in ar:
    if it.startswith(('devir', 'bölüm denetimi', 'bölüm 10 denetiminden', 'karşılık çakışması', 'korpusta 1', 'bağ:')): continue
    if it.startswith('meal'): it = it.split(' içi eş edat / lemma karşılıkları')[0]
    parca = re.split(r'(?<![\d:])(4:(\d+))(?![\d:-])', it)
    cur = None
    for i in range(0, len(parca)):
        if i % 3 == 1: continue
        if i % 3 == 2:
            v = int(parca[i]); cur = v if A <= v <= B else cur; continue
        if cur: kontrol(cur, parca[i], 'ARIZA:' + it[:12])
# kural 12: zamir kayıtları
meal = [it for it in ar if it.startswith('meal')][0]
seg = {int(m.group(1)): m.start() for m in re.finditer(r"(?:^|; )4:(\d+) '", meal)}
keys = sorted(seg)
eksik = 0
for i, n in enumerate(keys):
    t = meal[seg[n]: seg[keys[i + 1]] if i + 1 < len(keys) else len(meal)]
    for w, segs in W[n].items():
        for s in segs:
            if s[2].startswith('PRON'):
                kisi = s[2].split('|')[-1]
                ad = [k for k, f in P.items() if k.startswith("'") and f(s)]
                if not any(re.search(re.escape(a) + r' %d\. kelimede' % w, t) for a in ad):
                    eksik += 1; print('ZAMİR KAYITSIZ', n, w, s[0], kisi)
print('kelime iddiası denetlendi:', nkon, '· uyuşmaz:', bad, '· zamir kayıtsız:', eksik)
