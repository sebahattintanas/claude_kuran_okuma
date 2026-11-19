# sûre 6 blok 1 ARIZA oluşturucusu — sûre 5 blok 36 üreticisinden; denetim betikleri paralel (kullanıcı uyarısı: ilerleme ağır)
import re
src = open('/home/claude/s5/b36/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("6:25", "'qâle ellezî kefera in zâ illâ'", 2, 'say 6:25 25-30', "harekesiz 'yeqûlu'llezîne keferû in hâzâ illâ' (25-30. kelime)", ('dizi 6 25 25 30', "qâle ellezî kefera in zâ illâ", '25-30', "biçim farkı (dizi 6 25 25 30): 6:7 önek")),
 ("6:25", "'hattâ izâ câ'e'", 3, 'say 6:25 21-23', "harekesiz 'hattâ izâ câ'ûke' (21-23. kelime)", ('dizi 6 25 21 23', "hattâ izâ câ'e", '21-23', "biçim farkı (dizi 6 25 21 23): basılmamış eş fiil çekimi, zamir eki; basılmamış eş fiil çekimi, zamir eki")),
 ("6:26", "'illâ nefs mâ şa'ara'", 2, 'say 6:26 8-11', "harekesiz 'illâ enfusehum ve mâ yeş'urûn' (8-11. kelime)", ('dizi 6 26 8 11', "illâ nefs mâ şa'ara", '8-11', "biçim farkı (dizi 6 26 8 11): basılmamış eş i'râb, önek")),
 ("6:27", "'lev raâ iz vuqife 'alâ'", 2, 'say 6:27 1-5', "harekesiz 've lev terâ iz vuqifû 'ale' (1-5. kelime)", None),
 ("6:27", "'rabb kâne min'", 2, 'say 6:27 13-15', "harekesiz 'rabbinâ ve nekûne mine' (13-15. kelime)", ('dizi 6 27 13 15', "rabb kâne min", '13-15', "biçim farkı (dizi 6 27 13 15): basılmamış eş fiil çekimi, i'râb, zamir eki, önek")),
]
'''
VF = '''VF_YAZI = {25: {1: "'ve minhum'", 5: "'ve ce'alnâ'", 11: "'ve fî'", 14: "'ve in'"}, 26: {1: "'ve hum'", 4: "'ve yen'evne'", 6: "'ve in'", 10: "'ve mâ'"}, 27: {1: "'ve lev'", 10: "'ve lâ'", 14: "'ve nekûne'"}, 28: {9: "'ve lev'", 15: "'ve innehum'"}}
sys.path.insert(0, '/home/claude/b06/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b06/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b06/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
# paralel denetim koşusu
a = out.index("    AYN = (run('/home/claude/sunum/ayn_kontrol.py'"); b = out.index("    REP = {")
PAR = '''    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '25', '28'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '25', '28', '06'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '25', '28', '06'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '25', '28', '06', '--tazelik-yok')}
    for _n in range(7, 19): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '25', '28', '06')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18 = [_R['B%d' % _n].splitlines() for _n in range(6, 19)]
'''
out = out[:a] + PAR + out[b:]
R = [('# blok 36 (5:118-120) ARIZA oluşturucu — bölüm 16-2', '# sûre 6 blok 6 (6:25-28) ARIZA oluşturucu — bölüm 3-2'), ('/b36/', '/b06/'),
     ("es_edat.py', '36'", "es_edat.py', '06'"), ('range(1, 37)', 'range(1, 7)'),
     ("'--plan', '36', '--numarasiz')", "'--plan', '6', '--numarasiz')"),
     ('ariza_5_118_120', 'ariza_6_25_28'), ('bag_5_118_120', 'bag_6_25_28'), ('(118, 120)', '(25, 28)'), ("'118', '120', '36'", "'25', '28', '06'"), ("'118', '120'", "'25', '28'"),
     ("_ON = {'5:118', '5:119', '5:120'}", "_ON = {'6:25', '6:26', '6:27', '6:28'}"), ('range(118, 121)', 'range(25, 29)'),
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
out = re.sub(r"for nn in \('06', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06'):", out)
for l in out.split('\n'):
    for bad in ('b36', "'36'", "'118'", "'120'", '5_118_120', "'5:"):
        if bad in l: print('KONTROL', bad, l[:160])
_mk = """MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)"""
assert _mk in out
out = out.replace(_mk, _mk + "\nMKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde")
open('/home/claude/b06/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
