# bölüm 2 (sûre 5) denetimi kuralı 4-5: bloktaki bozuk biçimli fiil LEM'leri (muzâri / emir / edilgen biçimli LEM) — lem_norm kuralı: ham ad + '(morph LEM ham biçim)' notu
# kullanım (/home/claude'dan): python3 sunum/lem_bozuk.py NN   — bNN/morph<S>.txt; çıktı: konum, LEM; sezgisel: fiil LEM'i fetha ile bitmiyorsa ya da ي / تُ ile başlıyorsa
import sys, os, re, unicodedata as ud
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from sure import S
nn = sys.argv[1]
gor = set()
for l in open('/home/claude/b%s/morph%d.txt' % (nn, S), encoding='utf-8'):
    loc, f, t, feat = l.rstrip('\n').split('\t')
    if t != 'V': continue
    m = re.search(r'LEM:([^|]+)', feat)
    if not m: continue
    L = ud.normalize('NFC', m.group(1)); son = L.rstrip('\u0651')[-1]
    YA = {ud.normalize('NFC', 'يَئِسَ')}  # gerçek mazi ي ile başlayan
    bozuk = son in ('\u0652', '\u064f') or (L.startswith('يَ') and L not in YA) or ('PASS' in feat and '\u064f' in L[:4])
    if bozuk and L not in gor:
        gor.add(L); print(':'.join(loc.split(':')[:3]), L)
