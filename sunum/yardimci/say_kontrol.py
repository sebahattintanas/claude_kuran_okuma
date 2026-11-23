import re,sys
def parse(p):
    t=open(p,encoding='utf-8').read()
    d={}
    for blk in re.split(r'^### ',t,flags=re.M)[1:]:
        h=blk.split('\n',1)[0].strip()
        m=re.search(r'^ayet: (\d+)',blk,re.M)
        d.setdefault(h,[]).append(int(m.group(1)) if m else None)
    return d
if __name__=='__main__':
    d=parse(sys.argv[1])
    dup=[h for h,v in d.items() if len(v)>1]
    print('dup',len(dup))
    for h,v in d.items():
        if h.startswith('say ') and '--on' not in h and '--medde' not in h:
            on=d.get(h+' --on',[None])[0]
            if v[0]==1 and on not in (1,None): print(h,v,on, h+' --medde' in d)
