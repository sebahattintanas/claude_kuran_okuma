# sûre 7 blok 23 ARIZA oluşturucusu — sûre 6 blok 40 üreticisinden (s6/b40/yap/ariza_yap.py); bölüm 8-3
import re
src = open('/home/claude/s6/b40/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('\nI = [\n') + 1; k1 = src.index('\ndef yaz(II):')
R5 = '''R5 = [
 ('7:82', "'illâ en qâle'", 2, 'say 7:82 5-7', "harekesiz 'illâ en qâlû' (5-7. kelime)", ('dizi 7 82 5 7', 'illâ en qâle', '5-7', 'biçim farkı (dizi 7 82 5 7): 7:5 yazım eş')),
 ('7:84', "'nazara keyfe kâne 'âqibe'", 3, 'say 7:84 4-7', "harekesiz 'fe'nzur keyfe kâne 'âqibetu' (4-7. kelime)", ('dizi 7 84 4 7', "nazara keyfe kâne 'âqibe", '4-7', 'biçim farkı (dizi 7 84 4 7): basılmamış eş fiil çekimi, zamir eki, önek; basılmamış eş yazım eş; öneksiz eş koşusu (dizi 7 84 4 7): basılmamış eş → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 2')),
]
'''
VF = '''VF_YAZI = {80: {1: "'ve lûtan'", 4: "'li-qavmihî'", 5: "'e-te'tûne'", 9: "'bihâ'"}, 81: {2: "'le-te'tûne'"}, 82: {1: "'ve mâ'"}, 83: {1: "'fe-enceynâhu'", 2: "'ve ehlehû'"}, 84: {1: "'ve emtarnâ'", 4: "'fe'nzur'"}}
sys.path.insert(0, '/home/claude/b23/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b23/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2', '# sûre 7 blok 23 (7:80-84) ARIZA oluşturucu — bölüm 8-3'), ('/home/claude/b40/', '/home/claude/b23/'),
     ("es_edat.py', '40'", "es_edat.py', '23'"), ('range(1, 41)', 'range(1, 24)'),
     ("'--plan', '40', '--numarasiz')", "'--plan', '23', '--numarasiz')"),
     ('ariza_6_161_165', 'ariza_7_80_84'), ('bag_6_161_165', 'bag_7_80_84'), ('(161, 165)', '(80, 84)'), ("'161', '165', '40'", "'80', '84', '23'"), ("'161', '165'", "'80', '84'"),
     ("_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}", "_ON = {'7:80', '7:81', '7:82', '7:83', '7:84'}"), ('range(161, 166)', 'range(80, 85)'),
     ("x.startswith('6:')", "x.startswith('7:')"), ("== '6:%d' % a_", "== '7:%d' % a_"), ("return '6:%d: %s'", "return '7:%d: %s'"), ("r'\\b6:%d:\\d+'", "r'\\b7:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_6_*.txt')", "glob.glob('/home/claude/yamalar/ariza_7_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_7_b20k.txt'"),
     ("BOL = \"'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'\"", "BOL = \"'Sâlih ve Semûd; Lût ve kavmi'\""),
     ("for _n in range(7, 35): _J", "for _n in range(7, 44): _J"), ("B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]", "B33, B34, B35, B36, B37, B38, B39, B40, B41, B42, B43 = [_R['B%d' % _n].splitlines() for _n in range(6, 44)]"),
     ("'B34_HEPSI': (B34[-1] if B34 else '?'),", "'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'B39_HEPSI': (B39[-1] if B39 else '?'), 'B40_HEPSI': (B40[-1] if B40 else '?'), 'B41_HEPSI': (B41[-1] if B41 else '?'), 'B42_HEPSI': (B42[-1] if B42 else '?'), 'B43_HEPSI': (B43[-1] if B43 else '?'),"),
     ("B32, B33, B34): print(", "B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42, B43): print("),
     ("sûre 6'nın okunmuş bütün ARIZA dosyaları", "sûre 7'nin okunmuş bütün ARIZA dosyaları"),
     ]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
_AN = """ANILIS = "7:80 'iz' (2. kelime — morph T, zaman); 7:81 kök رجل ('r-ricâle' 3. kelime — erkek): tetik listesinde yok"\n"""
out = re.sub(r'ANILIS = ".*"\n', lambda m_: _AN, out)
out = re.sub(r"for nn in \('01', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'):", out)
for l in out.split('\n'):
    for bad in ('b40', "'40'", "'161'", "'165'", '6_161_165', "'6:", 's6/'):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b23/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
