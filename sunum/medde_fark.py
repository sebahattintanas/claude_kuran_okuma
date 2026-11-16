# bölüm 11 (sûre 5) denetimi kuralı 6: medde çifti (say2 '<anahtar>' / '<anahtar> --medde') farkı sinifla sınıflarıyla
# kullanım: python3 sunum/medde_fark.py bNN/say2.txt   — ARIZA 'bölüm' maddesindeki medde satırı bu çıktıyı aynen taşır
import sys, re, ast


def oku(yol):
    S2 = {}
    for blk in open(yol, encoding='utf-8').read().split('### ')[1:]:
        L = blk.strip().splitlines()
        m = re.match(r'(\d+) (\{.*\})$', L[-1].strip())
        if m: S2[L[0].strip()] = (int(m.group(1)), ast.literal_eval(m.group(2)))
    return S2


def satir(yol):
    S2 = oku(yol)
    par, fark = [], []
    for k, (n, d) in S2.items():
        if '--medde' not in k: continue
        k0 = k.replace(' --medde', '')
        m, d0 = S2[k0]
        par.append('%s meddeli %d / meddesiz %d' % (k0, m, n))
        if n != m:
            do = d['okunmus'] - d0['okunmus']; dh = d['henuz'] - d0['henuz']; dhs = d['henuz_si'] - d0['henuz_si']
            db = len(set(d['basilan']) - set(d0['basilan'])); de = d['eski'] - d0['eski']; dos = d['okunmus_si'] - d0['okunmus_si']
            p = []
            if db: p.append('basılmış %d' % db)
            if de: p.append('eski kayıt %d' % de)
            if do: p.append('okunmuş %d' % do + (' (sûre içi %d)' % dos if dos else ''))
            if dh: p.append('okunmamış %d' % dh + (' (sûre içi %d)' % dhs if dhs else ''))
            fark.append("'%s' meddesiz koşusu %s ayet daha buluyor" % (k0, ', '.join(p)))
    s = '; '.join(par)
    s += (' — FARK VAR: ' + '; '.join(fark)) if fark else ' — fark yok, yeni eş yok'
    return s


if __name__ == '__main__':
    print(satir(sys.argv[1]))
