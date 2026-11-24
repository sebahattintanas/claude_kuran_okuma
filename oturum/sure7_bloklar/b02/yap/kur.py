# sûre 7 blok 2 ARIZA oluşturucusu — sûre 6 blok 40 üreticisinden (s6/b40/yap/ariza_yap.py); bölüm içi blok (BEK yok)
import re
src = open('/home/claude/s6/b40/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('\nI = [\n') + 1; k1 = src.index('\ndef yaz(II):')
R5 = '''R5 = [
]
'''
VF = '''VF_YAZI = {6: {5: "'ve le-nes'elenne'"}, 7: {4: "'ve mâ'"}, 8: {1: "'ve'l-veznu'"}, 9: {1: "'ve men'"}, 10: {1: "'ve le-qad'", 5: "'ve ce'alnâ'"}}
sys.path.insert(0, '/home/claude/b02/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b02/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2', '# sûre 7 blok 2 (7:6-10) ARIZA oluşturucu — bölüm 1-2'), ('/home/claude/b40/', '/home/claude/b02/'),
     ("es_edat.py', '40'", "es_edat.py', '02'"), ('range(1, 41)', 'range(1, 3)'),
     ("'--plan', '40', '--numarasiz')", "'--plan', '2', '--numarasiz')"),
     ('ariza_6_161_165', 'ariza_7_6_10'), ('bag_6_161_165', 'bag_7_6_10'), ('(161, 165)', '(6, 10)'), ("'161', '165', '40'", "'6', '10', '02'"), ("'161', '165'", "'6', '10'"),
     ("_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}", "_ON = {'7:6', '7:7', '7:8', '7:9', '7:10'}"), ('range(161, 166)', 'range(6, 11)'),
     ("x.startswith('6:')", "x.startswith('7:')"), ("== '6:%d' % a_", "== '7:%d' % a_"), ("return '6:%d: %s'", "return '7:%d: %s'"), ("r'\\b6:%d:\\d+'", "r'\\b7:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_6_*.txt')", "glob.glob('/home/claude/yamalar/ariza_7_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_6_b40k.txt'"),
     ("BOL = \"'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'\"", "BOL = \"'Kitap indirildi; helak edilen kentler; tartı; yeryüzünde yerleştirme'\""),
     ("for _n in range(7, 35): _J", "for _n in range(7, 36): _J"), ("B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]", "B33, B34, B35 = [_R['B%d' % _n].splitlines() for _n in range(6, 36)]"),
     ("'B34_HEPSI': (B34[-1] if B34 else '?'),", "'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'),"),
     ("B32, B33, B34): print(", "B32, B33, B34, B35): print("),
     ("sûre 6'nın okunmuş bütün ARIZA dosyaları", "sûre 7'nin okunmuş bütün ARIZA dosyaları"),
     ]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
_AN = """ANILIS = "7:9 kök نفس ('enfusehum' 7. kelime — kendi): tetik listesinde yok"\n"""
out = re.sub(r'ANILIS = ".*"\n', lambda m_: _AN, out)
out = re.sub(r"for nn in \('01', [^)]*\):", "for nn in ('01', '02'):", out)
for l in out.split('\n'):
    for bad in ('b40', "'40'", "'161'", "'165'", '6_161_165', "'6:", 's6/'):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b02/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
