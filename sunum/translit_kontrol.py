# ◇ transliterasyonu ile morph Arapça iskelet karşılaştırması (bölüm 4 kuralı: bütün kelimelerde betikle)
# kullanım (/home/claude'dan): python3 sunum/translit_kontrol.py A B NN   → yamalar/metin_<S>_A_B.txt + bNN/morph.txt
# 'yalnız tanvin farkı' dışındaki farklar elle bakılır: l / n birleşmesi (şemsî harf, idğam), ة, tanvin yapıntıdır;
# harf değişimi (ör. غ 'ğ' yerine 'x') hatadır.
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys, difflib, unicodedata as ud
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
M = {}
exec(open('/home/claude/yamalar/metin_%d_%d_%d.txt' % (S, A, B)).read(), {'MEAL': {}, 'M': M})
AR = {}
for l in open(_BK + 'b%s/morph.txt' % NN, encoding='utf-8'):
    k, w, _ = l.split('\t'); a = int(k.split(':')[1]); AR.setdefault(a, []).append(w)
mp = {'ب':'b','ت':'t','ث':'s','ج':'c','ح':'h','خ':'x','د':'d','ذ':'z','ر':'r','ز':'z','س':'s','ش':'ş','ص':'s','ض':'d','ط':'t','ظ':'z','ع':"'",'غ':'ğ','ف':'f','ق':'q','ك':'k','ل':'l','م':'m','ن':'n','ه':'h','ة':'','ء':"'",'أ':"'",'إ':"'",'ؤ':"'",'ئ':"'"}
def iske_ar(ws):
    out = []
    for w in ws:
        w = ''.join(c for c in ud.normalize('NFC', w) if not ud.combining(c) and c not in 'ـ')
        w = w.replace('ٱ', '').replace('ا', '').replace('ى', '')
        out.append(''.join(mp.get(c, '') for c in w))
    return re.sub(r'(.)\1+', r'\1', ''.join(out))
def iske_la(t):
    s = ''.join(c for c in t.lower() if c in "bcdfğhklmnqrsştxz'")
    return re.sub(r'(.)\1+', r'\1', s)
for a in range(A, B + 1):
    tr = re.match(r"◇ '(.*?)' — ", M[a]).group(1)
    x, y = iske_ar(AR[a]).replace("'", ''), iske_la(tr).replace("'", '')
    sm = difflib.SequenceMatcher(None, x, y, autojunk=False)
    bad = [(op, x[i1:i2], y[j1:j2]) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal' and not (op == 'insert' and set(y[j1:j2]) <= {'n'})]
    print(a, bad or 'yalnız tanvin farkı')
# bölüm 7 kuralı 6: bag alıntıları da taranır — hedef ayetin ◇ transliterasyonunda alt dize olmalı (harf değişimi, ör. خ için 'h', burada yakalanır)
import ast
for b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + ']'):
    x, y = b['bag'].split(' → ')
    q = re.search(r"(?:harekesiz|önek kesilmiş) '((?:[^']|'(?=[a-zâîûçğışöü]))+)'", b['kural'])
    if q and y.startswith('%d:' % S) and A <= int(y.split(':')[1]) <= B:
        tr = re.match(r"◇ '(.*?)' — ", M[int(y.split(':')[1])]).group(1)
        print('bag', b['bag'], 'tamam' if q.group(1) in tr else 'HATA ◇ dışı: ' + q.group(1))
