# 'sonradan basılan' (bölüm 7 kuralı 3 + bölüm 8 kuralı 1): verilen blokların say2 listelerinde, o anki sınıflamada
# 'bu' / 'basilan' olmayıp şimdi basılan listesinde bulunan ayetler. Eskiyen yoksa 'eskiyen yok' yazılır.
# kullanım (/home/claude'dan): python3 sunum/sonradan.py b14 b15 b16 b17 ...  (önceki bölümün bütün blokları + bu bölümün önceki blokları)
import re, ast, sys
B = set(l.strip() for l in open('/home/claude/sunum/basilan.txt') if l.strip())
n = 0
# bölüm 16 denetimi kuralı 3: '--plan NN' blok listesini blok planından üretir (önceki bölümün bütün blokları + bu bölümün NN'den önceki blokları)
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from sure import S
NUM = '--numarasiz' in sys.argv  # bölüm 10 denetimi kuralı 9: bu oturumda basılmamış ayetin sayım anahtarı numarasız ('say2 sıra K')
ARG = [x for x in sys.argv[1:] if x != '--numarasiz']
if ARG[:1] == ['--plan']:
    NN = int(ARG[1]); bol = []; cur = None
    for l in open('/home/claude/yamalar/blok_plani_%d.txt' % S, encoding='utf-8'):
        if l.startswith('■'): bol.append([])
        else:
            m = re.match(r'\s*(\d+)\. ', l)
            if m: bol[-1].append(int(m.group(1)))
    i = next(k for k, b in enumerate(bol) if NN in b)
    ARG = ['b%02d' % x for x in (bol[i - 1] if i else []) + [x for x in bol[i] if x < NN]]
    ARG = [a for a in ARG if os.path.exists('/home/claude/%s/say2.txt' % a)]
    print('blok listesi (plan):', ' '.join(ARG) or '—')
for blk in ARG:
    for sira, b in enumerate(open('/home/claude/%s/say2.txt' % blk).read().split('### ')[1:], 1):
        L = b.strip().splitlines(); m = re.match(r'(\d+) (\{.*\})$', L[-1].strip())
        d = ast.literal_eval(m.group(2))
        li = [l for l in L if l.startswith('liste:')]
        if li: ay = [x.strip().split('×')[0].rstrip('†') for x in li[0][6:].split(',')]
        else:  # bölüm 1 denetimi kuralı 1: lemma dizisi kayıtları ('liste:' öneksiz satır)
            ld = [l for l in L[1:-1] if re.match(r'^\d+:\d+', l.strip())]
            if not ld: continue
            ay = [x.strip().split('×')[0].rstrip('†') for x in ld[0].split(',')]
        yeni = [a for a in ay if a in B and a not in set(d['bu']) | set(d['basilan'])]
        if yeni:
            n += 1; bas = L[0]
            if NUM:
                mm = re.match(r'(say|lem) (\d+):(\d+)|(dizi) (\d+) (\d+)', bas)
                if mm and ('%s:%s' % ((mm.group(2), mm.group(3)) if mm.group(1) else (mm.group(5), mm.group(6)))) not in B:
                    bas = '%s (say2 sıra %d)' % (mm.group(1) or mm.group(4), sira)
            print(blk, bas, yeni)
print('eskiyen sayım:', n)
