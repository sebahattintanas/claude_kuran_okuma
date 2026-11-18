# sûre 6 blok 1 ARIZA oluşturucusu — sûre 5 blok 36 üreticisinden; denetim betikleri paralel (kullanıcı uyarısı: ilerleme ağır)
import re
src = open('/home/claude/s5/b36/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("6:1", "'ellezî xalaqa semâ' ard'", 2, 'say 6:1 3-6', "harekesiz 'llezî xalaqa's-semâvâti ve'l-ard' (3-6. kelime)", ('dizi 6 1 3 6', "ellezî xalaqa semâ' ard", '3-6', "biçim farkı (dizi 6 1 3 6): basılmamış eş yazım eş")),
 ("6:2", "'_ ellezî xalaqa'", 2, 'say 6:2 1-3', "harekesiz 'huve'llezî xalaqakum' (1-3. kelime)", ('dizi 6 2 1 3', "_ ellezî xalaqa", '1-3', "biçim farkı (dizi 6 2 1 3): basılmamış eş zamir eki, önek")),
 ("6:5", "'mâ kâne _ istuhzi'e'", 2, 'say 6:5 9-12', "harekesiz 'mâ kânû bihî yestehzi'ûn' (9-12. kelime)", ('dizi 6 5 9 12', "mâ kâne _ istuhzi'e", '9-12', "biçim farkı (dizi 6 5 9 12): basılmamış eş yazım eş")),
]
'''
VF = '''VF_YAZI = {1: {6: "'ve'l-arda'", 7: "'ve ce'ale'", 9: "'ve'n-nûra'"}, 2: {9: "'ve ecelun'"}, 3: {1: "'ve huve'", 5: "'ve fi'l-ardi'", 9: "'ve cehrakum'", 10: "'ve ya'lemu'"}, 4: {1: "'ve mâ'"}, 5: {1: "'fe-qad'", 6: "'fe-sevfe'"}}
sys.path.insert(0, '/home/claude/b01/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b01/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b01/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
# paralel denetim koşusu
a = out.index("    AYN = (run('/home/claude/sunum/ayn_kontrol.py'"); b = out.index("    REP = {")
PAR = '''    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '1', '5'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '1', '5', '01'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '1', '5', '01'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '1', '5', '01', '--tazelik-yok')}
    for _n in range(7, 17): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '1', '5', '01')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16 = [_R['B%d' % _n].splitlines() for _n in range(6, 17)]
'''
out = out[:a] + PAR + out[b:]
R = [('# blok 36 (5:118-120) ARIZA oluşturucu — bölüm 16-2', '# sûre 6 blok 1 (6:1-5) ARIZA oluşturucu — bölüm 1-1'), ('/b36/', '/b01/'),
     ("es_edat.py', '36'", "es_edat.py', '01'"), ('range(1, 37)', 'range(1, 2)'),
     ("'--plan', '36', '--numarasiz')", "'--plan', '1', '--numarasiz')"),
     ('ariza_5_118_120', 'ariza_6_1_5'), ('bag_5_118_120', 'bag_6_1_5'), ('(118, 120)', '(1, 5)'), ("'118', '120', '36'", "'1', '5', '01'"), ("'118', '120'", "'1', '5'"),
     ("_ON = {'5:118', '5:119', '5:120'}", "_ON = {'6:1', '6:2', '6:3', '6:4', '6:5'}"), ('range(118, 121)', 'range(1, 6)'),
     ("x.startswith('5:')", "x.startswith('6:')"), ("== '5:%d' % a_", "== '6:%d' % a_"), ("return '5:%d: %s'", "return '6:%d: %s'"), ("r'\\b5:%d:\\d+'", "r'\\b6:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_5_*.txt')", "glob.glob('/home/claude/yamalar/ariza_6_*.txt')"),
     ("BEK = []", "BEK = [l.strip().rstrip(',') for l in open('/home/claude/yamalar/devir_5_120.txt', encoding='utf-8') if l.startswith('  \"devir (')]; BEK = [ast.literal_eval(x) for x in BEK]"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b36.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_5_hazirlik6.txt'"),
     ("BOL = \"'İsâ'ya soru; doğruların fayda gördüğü gün'\"", "BOL = \"'Gökleri ve yeri yaratan; yüz çeviren kavimler'\""),
     ("'B15_HEPSI': (B15[-1] if B15 else '?'),", "'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'),"),
     ("sûre 5'in okunmuş bütün ARIZA dosyaları", "sûre 6'nın okunmuş bütün ARIZA dosyaları"),
     ("print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)", "print(GLS)\nfor _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16): print([l for l in _x if l.startswith('HATA') or 'hata' in l])"),
     ]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
out = re.sub(r"VF_YAZI_ESKI = \{.*\n", "VF_YAZI_ESKI = {}\n", out)
out = re.sub(r"for nn in \('06', [^)]*\):", "for nn in ('01',):", out)
for l in out.split('\n'):
    for bad in ('b36', "'36'", "'118'", "'120'", '5_118_120', "'5:"):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b01/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
