# say2.txt -> 'N ayet: ...' cümleleri (sinifla sözlüğünden; elle sayı yazılmaz). SAY2 ortam değişkeni = bNN/say2.txt
import re, ast
S2 = {}
for blk in open(__import__('os').environ.get('SAY2','/home/claude/b10/say2.txt'), encoding='utf-8').read().split('### ')[1:]:
    L = blk.strip().splitlines()
    key = L[0].strip()
    m = re.match(r'(\d+) (\{.*\})$', L[-1].strip())
    S2[key] = (int(m.group(1)), ast.literal_eval(m.group(2)))
SAYI = {1:'bir',2:'iki',3:'üç',4:'dört',5:'beş',6:'altı',7:'yedi',8:'sekiz',9:'dokuz',10:'on'}
TUR = {'say': 'harekesiz', 'say--on': 'önek kesilmiş', 'lem': 'lemma', 'dizi': 'lemma dizisi', 'kok': 'kök'}
def tur(key):
    t = key.split()[0]
    if t == 'say' and '--on' in key: return TUR['say--on']
    if t == 'lem' and '--kok' in key: return TUR['kok']
    return TUR[t]
def say(key, ad, bas=False):
    n, d = S2[key]
    lab = tur(key) + " '" + ad + "'"
    if bas: lab = lab[0].upper() + lab[1:]
    if n == 1:
        assert d['bu'] and not d['basilan'] and not d['okunmus'] and not d['henuz'] and not d['eski']
        return lab + ' korpusta 1'
    p = [d['bu'][0]]
    s = ', '.join(p + d['basilan'])
    if d['basilan']: s += ' (okumada görüldü)'
    if d['eski']: s += ', eski kayıt %d ayet' % d['eski']
    if d['henuz']:
        s += ', henüz okunmamış %d ayet' % d['henuz'] + (' (sûre içi %d)' % d['henuz_si'] if d['henuz_si'] else '')
    if d['okunmus']:
        s += ', okunmuş %d ayet' % d['okunmus'] + (' (sûre içi %d)' % d['okunmus_si'] if d['okunmus_si'] else '')
    tot = 1 + len(d['basilan']) + d['eski'] + d['henuz'] + d['okunmus']
    assert tot == n, (key, tot, n)
    return lab + ' %d ayet: ' % n + s
