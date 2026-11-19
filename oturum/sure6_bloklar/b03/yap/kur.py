# sûre 6 blok 1 ARIZA oluşturucusu — sûre 5 blok 36 üreticisinden; denetim betikleri paralel (kullanıcı uyarısı: ilerleme ağır)
import re
src = open('/home/claude/s5/b36/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("6:12", "'ellezî xasira nefs _ lâ âmene'", 2, 'say 6:12 20-25', "harekesiz 'llezîne xasirû enfusehum fe-hum lâ yu'minûn' (20-25. kelime)", None),
 ("6:12", "''alâ nefs rahme'", 2, 'say 6:12 10-12', "harekesiz ''alâ nefsihi'r-rahme' (10-12. kelime)", None),
 ("6:13", "'_ semî' 'alîm'", 2, 'say 6:13 7-9 --on', "önek kesilmiş 've huve's-semî'u'l-'alîm' (7-9. kelime)", None),
 ("6:14", "'qâle ğayr allâh'", 2, 'say 6:14 1-3', "harekesiz 'qul eğayra'llâh' (1-3. kelime)", None),
 ("6:14", "'kâne min muşrik'", 2, 'say 6:14 22-24', "harekesiz 'tekûnenne mine'l-muşrikîn' (22-24. kelime)", ('dizi 6 14 22 24', "kâne min muşrik", '22-24', "biçim farkı (dizi 6 14 22 24): basılmamış eş fiil çekimi")),
]
'''
VF = '''VF_YAZI = {12: {6: "'ve'l-ardi'", 23: "'fe-hum'"}, 13: {1: "'ve lehû'", 6: "'ve'n-nehâri'", 7: "'ve huve'"}, 14: {8: "'ve'l-ardi'", 9: "'ve huve'", 11: "'ve lâ yut'amu'", 21: "'ve lâ tekûnenne'"}, 15: {}}
sys.path.insert(0, '/home/claude/b03/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b03/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b03/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
# paralel denetim koşusu
a = out.index("    AYN = (run('/home/claude/sunum/ayn_kontrol.py'"); b = out.index("    REP = {")
PAR = '''    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '12', '15'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '12', '15', '03'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '12', '15', '03'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '12', '15', '03', '--tazelik-yok')}
    for _n in range(7, 18): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '12', '15', '03')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17 = [_R['B%d' % _n].splitlines() for _n in range(6, 18)]
'''
out = out[:a] + PAR + out[b:]
R = [('# blok 36 (5:118-120) ARIZA oluşturucu — bölüm 16-2', '# sûre 6 blok 3 (6:12-15) ARIZA oluşturucu — bölüm 2-1'), ('/b36/', '/b03/'),
     ("es_edat.py', '36'", "es_edat.py', '03'"), ('range(1, 37)', 'range(1, 4)'),
     ("'--plan', '36', '--numarasiz')", "'--plan', '3', '--numarasiz')"),
     ('ariza_5_118_120', 'ariza_6_12_15'), ('bag_5_118_120', 'bag_6_12_15'), ('(118, 120)', '(12, 15)'), ("'118', '120', '36'", "'12', '15', '03'"), ("'118', '120'", "'12', '15'"),
     ("_ON = {'5:118', '5:119', '5:120'}", "_ON = {'6:12', '6:13', '6:14', '6:15'}"), ('range(118, 121)', 'range(12, 16)'),
     ("x.startswith('5:')", "x.startswith('6:')"), ("== '5:%d' % a_", "== '6:%d' % a_"), ("return '5:%d: %s'", "return '6:%d: %s'"), ("r'\\b5:%d:\\d+'", "r'\\b6:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_5_*.txt')", "glob.glob('/home/claude/yamalar/ariza_6_*.txt')"),
     ("BEK = []", "BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b02.txt', encoding='utf-8').read() + ']')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b36.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_5_hazirlik6.txt'"),
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
out = re.sub(r"for nn in \('06', [^)]*\):", "for nn in ('01', '02', '03'):", out)
for l in out.split('\n'):
    for bad in ('b36', "'36'", "'118'", "'120'", '5_118_120', "'5:"):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b03/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
