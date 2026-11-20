# sûre 6 blok 1 ARIZA oluşturucusu — sûre 5 blok 36 üreticisinden; denetim betikleri paralel (kullanıcı uyarısı: ilerleme ağır)
import re
src = open('/home/claude/s5/b36/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("6:46", "'nazara keyf sarref âye'", 2, 'say 6:46 17-20', "harekesiz 'unzur keyfe nusarrifu'l-âyât' (17-20. kelime)", None),
 ("6:46", "'qâle ra'â in'", 3, 'say 6:46 1-3', "harekesiz 'qul era'eytum in' (1-3. kelime)", ('dizi 6 46 1 3', "qâle ra'â in", '1-3', "biçim farkı (dizi 6 46 1 3): 6:40 fiil çekimi, zamir eki; 6:47 fiil çekimi, zamir eki")),
 ("6:47", "'qâle ra'â in etâ 'azâb allâh'", 2, 'say 6:47 1-6', "harekesiz 'qul era'eytekum in etâkum 'azâbu'llâh' (1-6. kelime)", None),
 ("6:47", "'qâle ra'â in'", 3, 'say 6:47 1-3', "harekesiz 'qul era'eytekum in' (1-3. kelime)", ('dizi 6 47 1 3', "qâle ra'â in", '1-3', "biçim farkı (dizi 6 47 1 3): 6:40 yazım eş; 6:46 fiil çekimi, zamir eki")),
 ("6:49", "''azâb mâ kâne'", 3, 'say 6:49 5-7', "harekesiz 'l-'azâbu bi-mâ kânû' (5-7. kelime)", ('dizi 6 49 5 7', "'azâb mâ kâne", '5-7', "biçim farkı (dizi 6 49 5 7): 6:30 fiil çekimi, zamir eki; basılmamış eş yazım eş")),
 ("6:49", "'ellezî kezzebe âye'", 2, 'say 6:49 1-3', "harekesiz 've'llezîne kezzebû bi-âyâtinâ' (1-3. kelime)", None),
]
'''
VF = '''VF_YAZI = {46: {7: "'ve ebsârakum'", 8: "'ve xateme'"}, 47: {}, 48: {1: "'ve mâ'", 6: "'ve munzirîn'", 7: "'fe-men'", 9: "'ve aslaha'", 10: "'fe-lâ'", 13: "'ve lâ'"}, 49: {1: "'ve'llezîne'"}}
sys.path.insert(0, '/home/claude/b11/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b11/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b11/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
# paralel denetim koşusu
a = out.index("    AYN = (run('/home/claude/sunum/ayn_kontrol.py'"); b = out.index("    REP = {")
PAR = '''    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '46', '49'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '46', '49', '11'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '46', '49', '11'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '46', '49', '11', '--tazelik-yok')}
    for _n in range(7, 21): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '46', '49', '11')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20 = [_R['B%d' % _n].splitlines() for _n in range(6, 21)]
'''
out = out[:a] + PAR + out[b:]
R = [('# blok 36 (5:118-120) ARIZA oluşturucu — bölüm 16-2', '# sûre 6 blok 11 (6:46-49) ARIZA oluşturucu — bölüm 5-2'), ('/b36/', '/b11/'),
     ("es_edat.py', '36'", "es_edat.py', '11'"), ('range(1, 37)', 'range(1, 12)'),
     ("'--plan', '36', '--numarasiz')", "'--plan', '11', '--numarasiz')"),
     ('ariza_5_118_120', 'ariza_6_46_49'), ('bag_5_118_120', 'bag_6_46_49'), ('(118, 120)', '(46, 49)'), ("'118', '120', '36'", "'46', '49', '11'"), ("'118', '120'", "'46', '49'"),
     ("_ON = {'5:118', '5:119', '5:120'}", "_ON = {'6:46', '6:47', '6:48', '6:49'}"), ('range(118, 121)', 'range(46, 50)'),
     ("x.startswith('5:')", "x.startswith('6:')"), ("== '5:%d' % a_", "== '6:%d' % a_"), ("return '5:%d: %s'", "return '6:%d: %s'"), ("r'\\b5:%d:\\d+'", "r'\\b6:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_5_*.txt')", "glob.glob('/home/claude/yamalar/ariza_6_*.txt')"),
     ("BEK = []", "BEK = []"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b36.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_6_b09.txt'"),
     ("BOL = \"'İsâ'ya soru; doğruların fayda gördüğü gün'\"", "BOL = \"'Darlık ve bolluk; kulakları ve gözleri almak'\""),
     ("'B15_HEPSI': (B15[-1] if B15 else '?'),", "'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'),"),
     ("sûre 5'in okunmuş bütün ARIZA dosyaları", "sûre 6'nın okunmuş bütün ARIZA dosyaları"),
     ("print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)", "print(GLS)\nfor _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20): print([l for l in _x if l.startswith('HATA') or 'hata' in l])"),
     ]
R += [("MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()", "MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']")]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
out = re.sub(r"VF_YAZI_ESKI = \{.*\n", "VF_YAZI_ESKI = {}\n", out)
out = re.sub(r"for nn in \('06', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11'):", out)
for l in out.split('\n'):
    for bad in ('b36', "'36'", "'118'", "'120'", '5_118_120', "'5:"):
        if bad in l: print('KONTROL', bad, l[:160])
_mk = """MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)"""
assert _mk in out
out = out.replace(_mk, _mk + "\nMKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde")
open('/home/claude/b11/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
