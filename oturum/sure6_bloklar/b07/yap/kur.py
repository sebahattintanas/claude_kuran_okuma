# sûre 6 blok 1 ARIZA oluşturucusu — sûre 5 blok 36 üreticisinden; denetim betikleri paralel (kullanıcı uyarısı: ilerleme ağır)
import re
src = open('/home/claude/s5/b36/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("6:30", "'lev raâ iz vuqife 'alâ'", 2, 'say 6:30 1-5', "harekesiz 've lev terâ iz vuqifû 'alâ' (1-5. kelime)", None),
 ("6:30", "''azâb mâ kâne'", 3, 'say 6:30 16-18', "harekesiz 'l-'azâbe bimâ kuntum' (16-18. kelime)", ('dizi 6 30 16 18', "'azâb mâ kâne", '16-18', "biçim farkı (dizi 6 30 16 18): basılmamış eş fiil çekimi, zamir eki; basılmamış eş fiil çekimi, zamir eki")),
 ("6:30", "'mâ kâne kefera'", 2, 'say 6:30 17-19', "harekesiz 'bimâ kuntum tekfurûn' (17-19. kelime)", ('dizi 6 30 17 19', "mâ kâne kefera", '17-19', "biçim farkı (dizi 6 30 17 19): basılmamış eş fiil çekimi, zamir eki")),
 ("6:31", "'hattâ izâ câ'e'", 3, 'say 6:31 7-9', "harekesiz 'hattâ izâ câ'ethum' (7-9. kelime)", ('dizi 6 31 7 9', "hattâ izâ câ'e", '7-9', "biçim farkı (dizi 6 31 7 9): 6:25 fiil çekimi, zamir eki; basılmamış eş fiil çekimi, zamir eki")),
 ("6:31", "'qad xasira ellezî'", 2, 'say 6:31 1-3', "harekesiz 'qad xasira'llezîne' (1-3. kelime)", None),
]
'''
VF = '''VF_YAZI = {29: {1: "'ve qâlû'", 7: "'ve mâ'"}, 30: {1: "'ve lev'", 13: "'ve rabbinâ'"}, 31: {18: "'ve hum'"}, 32: {1: "'ve me'", 6: "'ve lahv'", 7: "'ve le'd-dâru'"}}
sys.path.insert(0, '/home/claude/b07/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b07/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b07/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
# paralel denetim koşusu
a = out.index("    AYN = (run('/home/claude/sunum/ayn_kontrol.py'"); b = out.index("    REP = {")
PAR = '''    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '29', '32'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '29', '32', '07'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '29', '32', '07'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '29', '32', '07', '--tazelik-yok')}
    for _n in range(7, 19): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '29', '32', '07')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18 = [_R['B%d' % _n].splitlines() for _n in range(6, 19)]
'''
out = out[:a] + PAR + out[b:]
R = [('# blok 36 (5:118-120) ARIZA oluşturucu — bölüm 16-2', '# sûre 6 blok 7 (6:29-32) ARIZA oluşturucu — bölüm 3-3'), ('/b36/', '/b07/'),
     ("es_edat.py', '36'", "es_edat.py', '07'"), ('range(1, 37)', 'range(1, 8)'),
     ("'--plan', '36', '--numarasiz')", "'--plan', '7', '--numarasiz')"),
     ('ariza_5_118_120', 'ariza_6_29_32'), ('bag_5_118_120', 'bag_6_29_32'), ('(118, 120)', '(29, 32)'), ("'118', '120', '36'", "'29', '32', '07'"), ("'118', '120'", "'29', '32'"),
     ("_ON = {'5:118', '5:119', '5:120'}", "_ON = {'6:29', '6:30', '6:31', '6:32'}"), ('range(118, 121)', 'range(29, 33)'),
     ("x.startswith('5:')", "x.startswith('6:')"), ("== '5:%d' % a_", "== '6:%d' % a_"), ("return '5:%d: %s'", "return '6:%d: %s'"), ("r'\\b5:%d:\\d+'", "r'\\b6:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_5_*.txt')", "glob.glob('/home/claude/yamalar/ariza_6_*.txt')"),
     ("BEK = []", "BEK = []"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b36.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_6_b05.txt'"),
     ("BOL = \"'İsâ'ya soru; doğruların fayda gördüğü gün'\"", "BOL = \"'Yalanlayanların toplanma sahnesi; dünya hayatı oyun'\""),
     ("'B15_HEPSI': (B15[-1] if B15 else '?'),", "'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'),"),
     ("sûre 5'in okunmuş bütün ARIZA dosyaları", "sûre 6'nın okunmuş bütün ARIZA dosyaları"),
     ("print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)", "print(GLS)\nfor _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18): print([l for l in _x if l.startswith('HATA') or 'hata' in l])"),
     ]
R += [("MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()", "MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']")]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
out = re.sub(r"VF_YAZI_ESKI = \{.*\n", "VF_YAZI_ESKI = {}\n", out)
out = re.sub(r"for nn in \('06', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07'):", out)
for l in out.split('\n'):
    for bad in ('b36', "'36'", "'118'", "'120'", '5_118_120', "'5:"):
        if bad in l: print('KONTROL', bad, l[:160])
_mk = """MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)"""
assert _mk in out
out = out.replace(_mk, _mk + "\nMKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde")
open('/home/claude/b07/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
