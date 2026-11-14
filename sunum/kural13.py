# bölüm 12 denetimi kuralları (blok 33'ten itibaren) — betik denetimi
# kullanım (/home/claude'dan): python3 sunum/kural13.py A B NN
# (1) okuma (gözlem) maddesinde sayı sözcüğü + 'geçiş' / 'ayet' / 'kelime' ↔ ardından gelen konum listesinin uzunluğu
# (2) sözdizimi maddesinde 'atıf' / 'istînâf' / 'hâl' ↔ aynı cümleciğin 'morph X' etiketi (istînâf=REM, atıf=CONJ, hâl=CIRC) ya da 'sapma'
#     ve anılan etiket, alıntının açıldığı 've' / 'fe' kelimesinin morph etiketiyle (VF_YAZI üzerinden)
# (4) ◇ ve ARIZA'da "lemma 'X'" anmaları ↔ blok morph LEM transliterasyonu ya da önceki blokların lemma adları (iskelet karşılaştırması)
# (6) R5 maddesinde her 'tutuyor' / 'tutmuyor' hükmünde taban dökümü '(4:A' 
import re, sys, ast, importlib.util as iu, unicodedata as ud
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
ar = ast.literal_eval('{' + open(Y + 'ariza_4_%d_%d.txt' % (A, B), encoding='utf-8').read() + '}')[(A, B)]
M = {}; exec(open(Y + 'metin_4_%d_%d.txt' % (A, B), encoding='utf-8').read(), {'MEAL': {}, 'M': M})
sp = iu.spec_from_file_location('ay', '/home/claude/b%s/yap/ariza_bas.py' % NN)
import os; _f = '/home/claude/b%s/yap/ariza_bas.py' % NN; _f = _f if os.path.exists(_f) else _f.replace('ariza_bas', 'ariza_yap'); src = open(_f, encoding='utf-8').read()
VF = ast.literal_eval(re.search(r'VF_YAZI = (\{.*?\}\})', src, re.S).group(1))
MOR = {}
for l in open('/home/claude/b%s/morph4.txt' % NN, encoding='utf-8'):
    loc, f, t, feat = l.rstrip('\n').split('\t'); s, a, w, p = map(int, loc.split(':'))
    MOR.setdefault(a, {}).setdefault(w, []).append((f, t, feat))
hata = 0
def H(*x):
    global hata; hata += 1; print('HATA', *x)
SAYI = {'bir': 1, 'iki': 2, 'üç': 3, 'dört': 4, 'beş': 5, 'altı': 6, 'yedi': 7, 'sekiz': 8, 'dokuz': 9, 'on': 10}
ok = [x for x in ar if x.startswith('okuma (gözlem)')]
for x in ok:
    for m in re.finditer(r'\b(bir|iki|üç|dört|beş|altı|yedi|sekiz|dokuz|on) (geçiş|ayet|kelime)\w* \(([^)]*)\)', x):
        n = len(re.findall(r'\d+\.', m.group(3))) or len(re.findall(r'\d+:\d+', m.group(3)))
        if n != SAYI[m.group(1)]: H('(1)', m.group(0))
        else: print('(1) tamam:', m.group(0))
TAG = {'istînâf': 'REM', 'atıf': 'CONJ', 'hâl': 'CIRC'}
sz = [x for x in ar if x.startswith('sözdizimi')][0]
cur = None
for parca in re.split(r'(?<![\d:])4:(\d+) ', sz)[1:]:
    if parca.isdigit(): cur = int(parca); continue
    for cl in re.split(r"; (?=')", parca):
        kel = re.findall(r'\b(istînâf|atıf|hâl)\b', cl)
        tg = re.findall(r'morph ([A-Z]+)', cl)
        q = re.match(r"'((?:[^']|'(?=[a-zâîûçğışöü]))+)'", cl)
        for k in kel:
            if 'sapma' in cl: continue
            if TAG[k] not in tg: H('(2)', cur, k, tg, cl[:70])
        if q and tg:
            qq = q.group(1)
            for w, yaz in VF.get(cur, {}).items():
                y = yaz.strip("'")
                if qq.startswith(y) or y.startswith(qq):
                    gercek = [feat.split('|')[0] for f, t, feat in MOR[cur][w] if 'PREF' in feat and re.search(r'LEM:[وف](\||$)', feat)]
                    if gercek and gercek[0] != tg[0]: H('(2) etiket', cur, w, yaz, tg[0], '≠ morph', gercek[0])
mp = {'ب':'b','ت':'t','ث':'s','ج':'c','ح':'h','خ':'x','د':'d','ذ':'z','ر':'r','ز':'z','س':'s','ش':'ş','ص':'s','ض':'d','ط':'t','ظ':'z','ع':'','غ':'ğ','ف':'f','ق':'q','ك':'k','ل':'l','م':'m','ن':'n','ه':'h','ة':'','ء':'','أ':'','إ':'','ؤ':'','ئ':'','و':'v','ي':'y','ى':''}
def ska(w): return re.sub(r'(.)\1+', r'\1', ''.join(mp.get(c, '') for c in ud.normalize('NFC', w) if not ud.combining(c)))
def skl(t): return re.sub(r'(.)\1+', r'\1', ''.join(c for c in t.lower().replace('x', 'x') if c in 'bcdfğhklmnqrsştxzvy'))
LEMS = set()
import glob
for f in glob.glob('/home/claude/b*/morph4.txt'):
    for l in open(f, encoding='utf-8'):
        m = re.search(r'LEM:([^|\t\n]+)', l)
        if m: LEMS.add(ska(m.group(1)))
nl = 0
for n in range(A, B + 1):
    d0 = M[n].split(' — ', 1)[1].split(' (ölçüm')[0]
    for x in re.findall(r"(?:nekre|belirli|çoğul|ortaç|masdar|bab|özel ad) '((?:[^']|'(?=[a-zâîûçğışöü]))+)'", d0):
        nl += 1; s_ = skl(x)
        if not any(s_ == L or s_.replace('y', '') == L.replace('y', '') or s_.replace('v', '') == L.replace('v', '') for L in LEMS): H('(4) ◇ lemma', n, x, s_)
metin = '\n'.join(M[n] for n in range(A, B + 1)) + '\n' + '\n'.join(x for x in ar if not x.startswith(('bölüm denetimi', 'bölüm 12 denetiminden', 'kullanıcı kararı')))
for m in re.finditer(r"lemma(?:ları)? ((?:'(?:[^']|'(?=[a-zâîûçğışöü]))+'(?:, | ve )?)+)", metin):
    for x in re.findall(r"'((?:[^']|'(?=[a-zâîûçğışöü]))+)'", m.group(1)):
        s = skl(x); nl += 1
        if not any(s == L or s.replace('y', '') == L.replace('y', '') or s.replace('v', '') == L.replace('v', '') for L in LEMS):
            H('(4) lemma', x, s)
r5 = [x for x in ar if x.startswith('araç tanımı')][0]
for h in re.split(r'; (?=4:\d+ |\')', r5):
    if re.search(r'tutuyor|tutmuyor', h) and 'sûre içi' in h and not re.search(r'\(4:\d+', h): H('(6)', h[:80])
print('(4) denetlenen lemma adı:', nl); print('kural13 hata:', hata)
