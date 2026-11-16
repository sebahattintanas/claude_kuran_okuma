# bölüm 6 kuralı 9: bütün bölüm araçlarını sûrenin okunmuş bütün bloklarında koşar; yamalar/geriye_donuk_<S>_<etiket>.txt yazar;
# başına önceki geriye dönük dosyayla farkı (düşen / yeni isabet) koyar; bölüm 8 kuralı 10: düşenler 'kayıt değişti' / 'araç değişti' diye sınıflanır. Kayıtlar yeniden yazılmaz; isabetler tam okuma sonu listesi.
# kullanım (/home/claude'dan): python3 sunum/geriye_donuk.py b13 [yamalar/geriye_donuk_5_b11.txt]
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); from sure import S
import re, sys, glob, subprocess, datetime
ET = sys.argv[1]; ONC = sys.argv[2] if len(sys.argv) > 2 else None
Y = '/home/claude/yamalar/'
def run(cmd): return subprocess.run(cmd, capture_output=True, text=True, cwd='/home/claude', shell=isinstance(cmd, str)).stdout
BL = []
for f in sorted(glob.glob(Y + 'metin_%d_*_*.txt' % S), key=lambda p: int(p.split('_')[-2])):
    a, b = map(int, re.findall(r'_(\d+)_(\d+)\.txt$', f)[0])
    nn = next((d[-3:-1] for d in sorted(glob.glob('/home/claude/b[0-9][0-9]/')) if any(l.startswith('%d:%d:' % (S, a)) for l in open(d + 'morph.txt', encoding='utf-8'))), None) if glob.glob('/home/claude/b[0-9][0-9]/morph.txt') else None
    BL.append((a, b, nn))
out, ISA = [], []
for a, b, nn in BL:
    out.append('## blok %s (%d:%d-%d)' % (nn, S, a, b))
    if not nn: out.append('(blok klasörü yok — atlandı)'); continue
    isa = []
    for arac in ('bolum4_kurallar.py', 'bolum5_kurallar.py'):
        isa += ['%s: %s' % (arac.split('.')[0], l[5:]) for l in run(['python3', 'sunum/' + arac, str(a), str(b), nn]).splitlines() if l.startswith('HATA')]
    if _o.path.exists('/home/claude/b%s/yap/veri.py' % nn):
        isa += ['bolum6_kurallar: ' + l[5:] for l in run(['python3', 'sunum/bolum6_kurallar.py', str(a), str(b), nn, '--tazelik-yok']).splitlines() if l.startswith('HATA')]
        isa += ['bolum7_kurallar: ' + l[5:] for l in run(['python3', 'sunum/bolum7_kurallar.py', str(a), str(b), nn]).splitlines() if l.startswith('HATA')]  # bölüm 7 kuralları
        isa += ['bolum8_kurallar: ' + l[5:] for l in run(['python3', 'sunum/bolum8_kurallar.py', str(a), str(b), nn]).splitlines() if l.startswith('HATA')]  # bölüm 8 kuralları
        es = run(['python3', 'sunum/es_edat.py', nn])
        m = re.search(r'tanınmayan edat / zamir başlığı (\d+)(?: \(([^)]*)\))?', es)
        if m and m.group(1) != '0': isa.append('es_edat: tanınmayan %s (%s)' % (m.group(1), m.group(2)))
        gl = run(['python3', 'sunum/gloss_tara.py', str(a), str(b), nn])
        m = re.search(r'KAPSAMAYAN (\d+)', gl)
        if m and m.group(1) != '0': isa.append('gloss_tara: KAPSAMAYAN %s' % m.group(1))
    kk = run(['python3', 'sunum/kelime_kontrol.py', str(a), str(b), nn])
    isa += ['kelime_kontrol: ' + l for l in kk.splitlines() if l.startswith(('UYUŞMAZ', 'ZAMİR KAYITSIZ'))]
    dos = [Y + '%s_%d_%d_%d.txt' % (k, S, a, b) for k in ('metin', 'ariza', 'bag', 'cipa', 'esma_el') if _o.path.exists(Y + '%s_%d_%d_%d.txt' % (k, S, a, b))]
    isa += ['yasakli: ' + l.split('/')[-1] for l in run(['bash', 'sunum/yasakli.sh'] + dos).splitlines() if 'bitti' not in l and l.strip()]
    out += isa; ISA += ['blok %s %s' % (nn, x) for x in isa]
bas = ['# geriye dönük koşu (%s, %s): bolum4_kurallar, bolum5_kurallar, bolum6_kurallar (--tazelik-yok), bolum7_kurallar, bolum8_kurallar, es_edat tanınmayan, gloss_tara KAPSAMAYAN, kelime_kontrol, yasakli.sh — okunmuş bütün bloklar (sûre %d); isabet %d' % (ET, datetime.date.today(), S, len(ISA))]
if ONC and _o.path.exists(ONC):
    eski = set()
    blk = None
    for l in open(ONC, encoding='utf-8'):
        l = l.rstrip('\n')
        m = re.match(r'## blok (\S+)', l)
        if m: blk = m.group(1); continue
        if l.startswith(('HATA ', 'YASAKLI ')) and blk: eski.add('blok %s %s' % (blk, l))
        elif l and not l.startswith('#') and blk: eski.add('blok %s %s' % (blk, l))
    yeni = set(ISA)
    def anahtar(x): return re.sub(r'^(blok \S+ )(?:HATA |YASAKLI |\w+_?\w*: )', r'\1', x)
    ek, ey = {anahtar(x) for x in eski}, {anahtar(x) for x in yeni}
    dus = sorted(ek - ey); yen = sorted(ey - ek)
    bas.append('# önceki dosyayla fark (%s): düşen %d, yeni %d' % (ONC.split('/')[-1], len(dus), len(yen)))
    # bölüm 8 kuralı 10: düşen isabet sınıflanır — 'kayıt değişti' (önceki dosyanın commit'inden bu yana blok kayıt dosyası farkı) / 'araç değişti' (kayıt aynen)
    R_ = '/home/claude/repo'
    C_ = subprocess.run(['git', 'log', '--format=%H', '-1', '--', 'yamalar/' + ONC.split('/')[-1]], capture_output=True, text=True, cwd=R_).stdout.strip()
    def sinif(x):
        nn_ = x.split()[1]; ab = next(((a_, b_) for a_, b_, n_ in BL if n_ == nn_), None)
        if not C_ or not ab: return 'sınıflanamadı'
        for k in ('metin', 'ariza', 'bag', 'cipa', 'esma_el'):
            f_ = '%s_%d_%d_%d.txt' % (k, S, ab[0], ab[1])
            eskif = subprocess.run(['git', 'show', '%s:yamalar/%s' % (C_, f_)], capture_output=True, cwd=R_).stdout
            simdi = open(Y + f_, 'rb').read() if _o.path.exists(Y + f_) else b''
            if eskif != simdi: return 'kayıt değişti'
        return 'araç değişti'
    sn = [(x, sinif(x)) for x in dus]
    bas.append('#   düşen sınıfı: kayıt değişti %d, araç değişti %d' % (sum(1 for _, c in sn if c == 'kayıt değişti'), sum(1 for _, c in sn if c == 'araç değişti')))
    bas += ['#   düşen (%s): %s' % (c, x) for x, c in sn] + ['#   yeni: ' + x for x in yen]
open(Y + 'geriye_donuk_%d_%s.txt' % (S, ET), 'w', encoding='utf-8').write('\n'.join(bas + out) + '\n')
print('\n'.join(bas[:2])); print('yazıldı: yamalar/geriye_donuk_%d_%s.txt' % (S, ET))
