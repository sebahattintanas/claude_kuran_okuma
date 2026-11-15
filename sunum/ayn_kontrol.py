# bölüm 3 (sûre 5) denetimi kuralı 4: ayn / hemze ile başlayan ◇ kelimesinin alıntıda düşmesi — bütün alıntı biçimlerinde
# kullanım (/home/claude'dan): python3 sunum/ayn_kontrol.py A B   → yamalar/metin_<S>_A_B.txt + ariza_<S>_A_B.txt
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys
A, B = int(sys.argv[1]), int(sys.argv[2])
Y = '/home/claude/yamalar/'
M = {}; exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'MEAL': {}, 'M': M})
ar = open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read()
W = set()
for a in range(A, B + 1):
    tr = re.match(r"◇ '(.*?)' — ", M[a]).group(1)
    for t in tr.split():
        if t.startswith("'") and len(t) > 3:
            W.add(re.split(r"[-']", t[1:])[0])
W = {w for w in W if len(w) >= 3}
NW = set()  # bölüm 4 kuralı 13: wasl / kesmesiz başlayan kelimenin çift kesmeli alıntısı
for a in range(A, B + 1):
    tr = re.match(r"◇ '(.*?)' — ", M[a]).group(1)
    for t in tr.split():
        for p_ in re.split(r"-|(?<=[aeiuâîû])'(?=l-|ll|[a-zçğışöü]-|[bcdfğhklmnqrsştxyz]{2})", t):
            if p_ and not p_.startswith("'") and len(p_) >= 3: NW.add(p_.split("'")[0] if len(p_.split("'")[0]) >= 3 else p_)
NW -= W
hata = 0
for ad, txt in [('metin', '\n'.join(M[a] for a in range(A, B + 1))), ('ariza', ar)]:
    for w in sorted(W):
        for m in re.finditer(r"(?:(?<=\()|(?<=[,;:/—] )|(?<=^)|(?<=\n))'" + re.escape(w) + r"(?=[a-zâîû' -])", txt):
            hata += 1; print('AYN', ad, w, txt[max(0, m.start() - 30):m.end() + 20].replace('\n', ' '))
for ad, txt in [('metin', '\n'.join(M[a] for a in range(A, B + 1))), ('ariza', ar)]:
    for w in sorted(NW):
        for m in re.finditer(r"(?<![a-zâîûçğışöü'])''" + re.escape(w) + r"(?=[a-zâîû' -])", txt):
            hata += 1; print('KESME', ad, w, txt[max(0, m.start() - 30):m.end() + 20].replace('\n', ' '))
print('ayn_kontrol hata:', hata, '· ayn/hemze başlı kelime', len(W))
