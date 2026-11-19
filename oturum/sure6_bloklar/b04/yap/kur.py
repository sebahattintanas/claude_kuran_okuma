# sûre 6 blok 1 ARIZA oluşturucusu — sûre 5 blok 36 üreticisinden; denetim betikleri paralel (kullanıcı uyarısı: ilerleme ağır)
import re
src = open('/home/claude/s5/b36/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("6:17", "''alâ kull şey''", 2, 'say 6:17 14-16', "harekesiz ''alâ kulli şey'' (14-16. kelime)", None),
 ("6:18", "'_ qâhir fevq 'abd'", 2, 'say 6:18 1-4', "harekesiz 've huve'l-qâhiru fevqa 'ibâdih' (1-4. kelime)", None),
 ("6:19", "'berî' mimmâ eşrake'", 2, 'say 6:19 35-37', "harekesiz 'berî'un mimmâ tuşrikûn' (35-37. kelime)", None),
]
'''
VF = '''VF_YAZI = {16: {7: "'ve zâlike'"}, 17: {1: "'ve in'", 10: "'ve in'"}, 18: {1: "'ve huve'", 5: "'ve huve'"}, 19: {10: "'ve beynekum'", 11: "'ve ûhiye'", 17: "'ve men'", 34: "'ve innenî'"}}
sys.path.insert(0, '/home/claude/b04/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b04/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b04/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
# paralel denetim koşusu
a = out.index("    AYN = (run('/home/claude/sunum/ayn_kontrol.py'"); b = out.index("    REP = {")
PAR = '''    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '16', '19'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '16', '19', '04'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '16', '19', '04'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '16', '19', '04', '--tazelik-yok')}
    for _n in range(7, 18): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '16', '19', '04')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17 = [_R['B%d' % _n].splitlines() for _n in range(6, 18)]
'''
out = out[:a] + PAR + out[b:]
R = [('# blok 36 (5:118-120) ARIZA oluşturucu — bölüm 16-2', '# sûre 6 blok 4 (6:16-19) ARIZA oluşturucu — bölüm 2-2'), ('/b36/', '/b04/'),
     ("es_edat.py', '36'", "es_edat.py', '04'"), ('range(1, 37)', 'range(1, 5)'),
     ("'--plan', '36', '--numarasiz')", "'--plan', '4', '--numarasiz')"),
     ('ariza_5_118_120', 'ariza_6_16_19'), ('bag_5_118_120', 'bag_6_16_19'), ('(118, 120)', '(16, 19)'), ("'118', '120', '36'", "'16', '19', '04'"), ("'118', '120'", "'16', '19'"),
     ("_ON = {'5:118', '5:119', '5:120'}", "_ON = {'6:16', '6:17', '6:18', '6:19'}"), ('range(118, 121)', 'range(16, 20)'),
     ("x.startswith('5:')", "x.startswith('6:')"), ("== '5:%d' % a_", "== '6:%d' % a_"), ("return '5:%d: %s'", "return '6:%d: %s'"), ("r'\\b5:%d:\\d+'", "r'\\b6:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_5_*.txt')", "glob.glob('/home/claude/yamalar/ariza_6_*.txt')"),
     ("BEK = []", "BEK = []"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b36.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_6_b03.txt'"),
     ("BOL = \"'İsâ'ya soru; doğruların fayda gördüğü gün'\"", "BOL = \"'Mülk kimin; şahit olarak Allah'\""),
     ("'B15_HEPSI': (B15[-1] if B15 else '?'),", "'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'),"),
     ("sûre 5'in okunmuş bütün ARIZA dosyaları", "sûre 6'nın okunmuş bütün ARIZA dosyaları"),
     ("print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)", "print(GLS)\nfor _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17): print([l for l in _x if l.startswith('HATA') or 'hata' in l])"),
     ]
R += [("MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()", "MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']")]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
out = re.sub(r"VF_YAZI_ESKI = \{.*\n", "VF_YAZI_ESKI = {}\n", out)
out = re.sub(r"for nn in \('06', [^)]*\):", "for nn in ('01', '02', '03', '04'):", out)
for l in out.split('\n'):
    for bad in ('b36', "'36'", "'118'", "'120'", '5_118_120', "'5:"):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b04/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
