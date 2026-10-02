import sys
from collections import defaultdict
S,A1,A2=map(int,sys.argv[1:4])
W=defaultdict(list)
for ln in open('morph.txt',encoding='utf-8'):
    p=ln.rstrip('\n').split('\t')
    if len(p)<4: continue
    s,a,w,g=map(int,p[0].split(':'))
    if s==S and A1<=a<=A2: W[(a,w)].append(p[1])
cur=None
for (a,w),v in sorted(W.items()):
    if a!=cur: print('\n%d:%d'%(S,a),end=' '); cur=a
    print('%d.%s'%(w,''.join(v)),end=' ')
print()
