# yer tutucu {{n|regex}} → ölçüm satırından (** sız) programla kesilen alıntı
import re, sys
O = [l.replace('**','') for l in open(__import__('os').environ.get('OLC','/home/claude/b01/olcum.txt'),encoding='utf-8').read().split('\n\n') if l.strip()]
def kes(t):
    def f(m):
        n, rx = int(m.group(1)), m.group(2)
        mm = re.search(rx, O[n-1]); assert mm, (n, rx)
        return mm.group(0)
    return re.sub(r'\{\{(\d)\|(.*?)\}\}', f, t)
if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    open(dst,'w',encoding='utf-8').write(kes(open(src,encoding='utf-8').read()))
