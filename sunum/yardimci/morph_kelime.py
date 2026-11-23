import sys
from collections import OrderedDict
src,dst=sys.argv[1:3]; G=OrderedDict()
for l in open(src,encoding='utf-8'):
    loc,f,t,feat=l.rstrip('\n').split('\t'); k=':'.join(loc.split(':')[:3])
    G.setdefault(k,[]).append((f,t+'|'+feat))
with open(dst,'w',encoding='utf-8') as o:
    for k,v in G.items(): o.write('%s\t%s\t%s\n'%(k,''.join(x[0] for x in v),' + '.join(x[1] for x in v)))
