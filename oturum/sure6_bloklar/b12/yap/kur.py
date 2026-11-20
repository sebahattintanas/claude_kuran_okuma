# sûre 6 blok 1 ARIZA oluşturucusu — sûre 5 blok 36 üreticisinden; denetim betikleri paralel (kullanıcı uyarısı: ilerleme ağır)
import re
src = open('/home/claude/s5/b36/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("6:50", "'in ittebe illâ'", 3, 'say 6:50 16-18', "harekesiz 'in ettebi'u illâ' (16-18. kelime)", ('dizi 6 50 16 18', "in ittebe illâ", '16-18', "biçim farkı (dizi 6 50 16 18): basılmamış eş fiil çekimi, zamir eki; basılmamış eş fiil çekimi, zamir eki")),
 ("6:50", "'mâ evhâ ilâ'", 2, 'say 6:50 19-21 --on', "önek kesilmiş 'mâ yûhâ ileyy' (19-21. kelime)", ('dizi 6 50 19 21', "mâ evhâ ilâ", '19-21', "biçim farkı (dizi 6 50 19 21): basılmamış eş zamir eki; basılmamış eş yazım eş; biçim öğesi 'evhâ' çekimi (lemma dizisi sûre içi 3, nakarat3 2); öneksiz eş koşusu (dizi 6 50 19 21): basılmamış eş → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 1")),
 ("6:51", "'veliyy lâ şefî''", 2, 'say 6:51 13-15', "harekesiz 'veliyyun ve lâ şefî'' (13-15. kelime)", None),
 ("6:52", "'min hisâb min şey''", 2, 'say 6:52 12-15', "harekesiz 'min hisâbihim min şey'' (12-15. kelime)", None),
]
'''
VF = '''VF_YAZI = {50: {8: "'ve lâ'", 11: "'ve lâ'", 26: "'ve'l-basîr'", 27: "'e-fe-lâ'"}, 51: {1: "'ve enzir'", 14: "'ve lâ'"}, 52: {1: "'ve lâ'", 7: "'ve'l-'aşiyyi'", 16: "'ve mâ'", 22: "'fe-tatrudehum'", 23: "'fe-tekûne'"}, 53: {1: "'ve kezâlike'"}}
sys.path.insert(0, '/home/claude/b12/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b12/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b12/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
# paralel denetim koşusu
a = out.index("    AYN = (run('/home/claude/sunum/ayn_kontrol.py'"); b = out.index("    REP = {")
PAR = '''    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '50', '53'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '50', '53', '12'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '50', '53', '12'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '50', '53', '12', '--tazelik-yok')}
    for _n in range(7, 22): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '50', '53', '12')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21 = [_R['B%d' % _n].splitlines() for _n in range(6, 22)]
'''
out = out[:a] + PAR + out[b:]
R = [("K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k}", "K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k and not (k + ' --medde' in sayim.S2 and sayim.S2[k + ' --medde'][0] != n)}  # sûre 6 bölüm 5 denetimi kuralı 6 (TEKIL_MEDDE)"),
     ('# blok 36 (5:118-120) ARIZA oluşturucu — bölüm 16-2', '# sûre 6 blok 12 (6:50-53) ARIZA oluşturucu — bölüm 6-1'), ('/b36/', '/b12/'),
     ("es_edat.py', '36'", "es_edat.py', '12'"), ('range(1, 37)', 'range(1, 13)'),
     ("'--plan', '36', '--numarasiz')", "'--plan', '12', '--numarasiz')"),
     ('ariza_5_118_120', 'ariza_6_50_53'), ('bag_5_118_120', 'bag_6_50_53'), ('(118, 120)', '(50, 53)'), ("'118', '120', '36'", "'50', '53', '12'"), ("'118', '120'", "'50', '53'"),
     ("_ON = {'5:118', '5:119', '5:120'}", "_ON = {'6:50', '6:51', '6:52', '6:53'}"), ('range(118, 121)', 'range(50, 54)'),
     ("x.startswith('5:')", "x.startswith('6:')"), ("== '5:%d' % a_", "== '6:%d' % a_"), ("return '5:%d: %s'", "return '6:%d: %s'"), ("r'\\b5:%d:\\d+'", "r'\\b6:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_5_*.txt')", "glob.glob('/home/claude/yamalar/ariza_6_*.txt')"),
     ("BEK = []", "BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b11.txt', encoding='utf-8').read() + ']')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b36.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_6_b11.txt'"),
     ("BOL = \"'İsâ'ya soru; doğruların fayda gördüğü gün'\"", "BOL = \"'De ki: gaybı bilmem; sabah akşam Rablerine dua edenler'\""),
     ("'B15_HEPSI': (B15[-1] if B15 else '?'),", "'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'),"),
     ("sûre 5'in okunmuş bütün ARIZA dosyaları", "sûre 6'nın okunmuş bütün ARIZA dosyaları"),
     ("print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)", "print(GLS)\nfor _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21): print([l for l in _x if l.startswith('HATA') or 'hata' in l])"),
     ]
R += [("MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()", "MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']")]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
out = re.sub(r"VF_YAZI_ESKI = \{.*\n", "VF_YAZI_ESKI = {}\n", out)
out = re.sub(r"for nn in \('06', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'):", out)
for l in out.split('\n'):
    for bad in ('b36', "'36'", "'118'", "'120'", '5_118_120', "'5:"):
        if bad in l: print('KONTROL', bad, l[:160])
_mk = """MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)"""
assert _mk in out
out = out.replace(_mk, _mk + "\nMKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde")
open('/home/claude/b12/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
