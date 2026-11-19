# sûre 6 blok 1 ARIZA oluşturucusu — sûre 5 blok 36 üreticisinden; denetim betikleri paralel (kullanıcı uyarısı: ilerleme ağır)
import re
src = open('/home/claude/s5/b36/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("6:37", "'qâdir 'alâ en'", 2, 'say 6:37 11-13 --on', "önek kesilmiş 'qâdirun 'alâ en' (11-13. kelime)", None),
 ("6:38", "'summe ilâ rabb'", 3, 'say 6:38 19-21', "harekesiz 'summe ilâ rabbihim' (19-21. kelime)", ('dizi 6 38 19 21', "summe ilâ rabb", '19-21', "biçim farkı (dizi 6 38 19 21): basılmamış eş yazım eş; basılmamış eş zamir eki")),
 ("6:40", "'qâle ra'â in etâ 'azâb allâh'", 2, 'say 6:40 1-6', "harekesiz 'qul era'eytekum in etâkum 'azâbu'llâh' (1-6. kelime)", None),
 ("6:40", "'qâle ra'â in'", 3, 'say 6:40 1-3', "harekesiz 'qul era'eytekum in' (1-3. kelime)", ('dizi 6 40 1 3', "qâle ra'â in", '1-3', "biçim farkı (dizi 6 40 1 3): basılmamış eş fiil çekimi, zamir eki; basılmamış eş yazım eş")),
 ("6:40", "'in kâne sâdiq'", 2, 'say 6:40 13-15', "harekesiz 'in kuntum sâdiqîn' (13-15. kelime)", None),
]
'''
VF = '''VF_YAZI = {37: {1: "'ve qâlû'", 16: "'ve lâkinne'"}, 38: {1: "'ve mâ'", 6: "'ve lâ'"}, 39: {1: "'ve'llezîne'", 5: "'ve bukmun'", 12: "'ve men'"}, 40: {}, 41: {4: "'fe-yekşifu'", 10: "'ve tensevne'"}}
sys.path.insert(0, '/home/claude/b09/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b09/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b09/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
# paralel denetim koşusu
a = out.index("    AYN = (run('/home/claude/sunum/ayn_kontrol.py'"); b = out.index("    REP = {")
PAR = '''    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '37', '41'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '37', '41', '09'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '37', '41', '09'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '37', '41', '09', '--tazelik-yok')}
    for _n in range(7, 20): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '37', '41', '09')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19 = [_R['B%d' % _n].splitlines() for _n in range(6, 20)]
'''
out = out[:a] + PAR + out[b:]
R = [('# blok 36 (5:118-120) ARIZA oluşturucu — bölüm 16-2', '# sûre 6 blok 9 (6:37-41) ARIZA oluşturucu — bölüm 4-2'), ('/b36/', '/b09/'),
     ("es_edat.py', '36'", "es_edat.py', '09'"), ('range(1, 37)', 'range(1, 10)'),
     ("'--plan', '36', '--numarasiz')", "'--plan', '9', '--numarasiz')"),
     ('ariza_5_118_120', 'ariza_6_37_41'), ('bag_5_118_120', 'bag_6_37_41'), ('(118, 120)', '(37, 41)'), ("'118', '120', '36'", "'37', '41', '09'"), ("'118', '120'", "'37', '41'"),
     ("_ON = {'5:118', '5:119', '5:120'}", "_ON = {'6:37', '6:38', '6:39', '6:40', '6:41'}"), ('range(118, 121)', 'range(37, 42)'),
     ("x.startswith('5:')", "x.startswith('6:')"), ("== '5:%d' % a_", "== '6:%d' % a_"), ("return '5:%d: %s'", "return '6:%d: %s'"), ("r'\\b5:%d:\\d+'", "r'\\b6:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_5_*.txt')", "glob.glob('/home/claude/yamalar/ariza_6_*.txt')"),
     ("BEK = []", "BEK = []"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b36.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_6_b08.txt'"),
     ("BOL = \"'İsâ'ya soru; doğruların fayda gördüğü gün'\"", "BOL = \"'Elçiye teselli; darlıkta çağrılan'\""),
     ("'B15_HEPSI': (B15[-1] if B15 else '?'),", "'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'),"),
     ("sûre 5'in okunmuş bütün ARIZA dosyaları", "sûre 6'nın okunmuş bütün ARIZA dosyaları"),
     ("print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)", "print(GLS)\nfor _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19): print([l for l in _x if l.startswith('HATA') or 'hata' in l])"),
     ]
R += [("MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()", "MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']")]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
out = re.sub(r"VF_YAZI_ESKI = \{.*\n", "VF_YAZI_ESKI = {}\n", out)
out = re.sub(r"for nn in \('06', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09'):", out)
for l in out.split('\n'):
    for bad in ('b36', "'36'", "'118'", "'120'", '5_118_120', "'5:"):
        if bad in l: print('KONTROL', bad, l[:160])
_mk = """MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)"""
assert _mk in out
out = out.replace(_mk, _mk + "\nMKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde")
open('/home/claude/b09/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
