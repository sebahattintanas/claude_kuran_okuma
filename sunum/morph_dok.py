# blok morph dökümü (oturum dışı yardımcı): bNN/morph<S>.txt (segment) ve bNN/morph.txt (kelime) — kullanım: python3 sunum/morph_dok.py A B NN (calisma'dan)
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from sure import S
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
seg = [l.rstrip('\n') for l in open('morph.txt', encoding='utf-8') if l.startswith('%d:' % S) and A <= int(l.split(':')[1]) <= B]
open(_BK + 'b%s/morph%d.txt' % (NN, S), 'w', encoding='utf-8').write('\n'.join(seg) + '\n')
W = {}
for l in seg:
    loc, f, t, feat = l.split('\t'); s, a, w, p = loc.split(':'); W.setdefault('%s:%s:%s' % (s, a, w), []).append((f, t, feat))
with open(_BK + 'b%s/morph.txt' % NN, 'w', encoding='utf-8') as o:
    for k, v in W.items(): o.write('%s\t%s\t%s\n' % (k, ''.join(x[0] for x in v), ' + '.join(x[1] + '|' + x[2] for x in v)))
print(len(seg), 'segment ·', len(W), 'kelime')
