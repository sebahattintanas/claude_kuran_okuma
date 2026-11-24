# sûre 7 blok 1 ARIZA oluşturucusu — sûre 6 blok 40 üreticisinden (s6/b40/yap/ariza_yap.py); bölüm açılışı, BEK devir notundan
import re
src = open('/home/claude/s6/b40/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('\nI = [\n') + 1; k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("7:5", "'illâ en qâle'", 2, 'say 7:5 7-9', "harekesiz 'illâ en qâlû' (7-9. kelime)", ('dizi 7 5 7 9', "illâ en qâle", '7-9', "biçim farkı (dizi 7 5 7 9): basılmamış eş yazım eş")),
]
'''
VF = '''VF_YAZI = {1: {}, 2: {12: "'ve zikrâ'"}, 3: {7: "'ve lâ'"}, 4: {1: "'ve kem'"}, 5: {}}
sys.path.insert(0, '/home/claude/b01/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b01/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2', '# sûre 7 blok 1 (7:1-5) ARIZA oluşturucu — bölüm 1-1'), ('/home/claude/b40/', '/home/claude/b01/'),
     ("es_edat.py', '40'", "es_edat.py', '01'"), ('range(1, 41)', 'range(1, 2)'),
     ("'--plan', '40', '--numarasiz')", "'--plan', '1', '--numarasiz')"),
     ('ariza_6_161_165', 'ariza_7_1_5'), ('bag_6_161_165', 'bag_7_1_5'), ('(161, 165)', '(1, 5)'), ("'161', '165', '40'", "'1', '5', '01'"), ("'161', '165'", "'1', '5'"),
     ("_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}", "_ON = {'7:1', '7:2', '7:3', '7:4', '7:5'}"), ('range(161, 166)', 'range(1, 6)'),
     ("x.startswith('6:')", "x.startswith('7:')"), ("== '6:%d' % a_", "== '7:%d' % a_"), ("return '6:%d: %s'", "return '7:%d: %s'"), ("r'\\b6:%d:\\d+'", "r'\\b7:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_6_*.txt')", "glob.glob('/home/claude/yamalar/ariza_7_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_6_b40k.txt'"),
     ("BOL = \"'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'\"", "BOL = \"'Kitap indirildi; helak edilen kentler; tartı; yeryüzünde yerleştirme'\""),
     ("for _n in range(7, 35): _J", "for _n in range(7, 36): _J"), ("B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]", "B33, B34, B35 = [_R['B%d' % _n].splitlines() for _n in range(6, 36)]"),
     ("'B34_HEPSI': (B34[-1] if B34 else '?'),", "'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'),"),
     ("B32, B33, B34): print(", "B32, B33, B34, B35): print("),
     ("sûre 6'nın okunmuş bütün ARIZA dosyaları", "sûre 7'nin okunmuş bütün ARIZA dosyaları"),
     ("BEK = []", "BEK = [l.strip().rstrip(',') for l in open('/home/claude/yamalar/devir_6_165.txt', encoding='utf-8') if l.startswith('  \"devir (')]; BEK = [ast.literal_eval(x) for x in BEK]"),
     ]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
_AN = """ANILIS = "7:2 kök صدر ('sadrike' 7. kelime — göğüs): tetik listesinde yok; 7:3 kök ولي ('evliyâ'' 11. kelime — dost): tetik listesinde yok; 7:4 kök هلك ('ehleknâhâ' 4. kelime — helâk et-): tetik listesinde yok; 7:5 'iz' (4. kelime — morph T, zaman)"\n"""
out = re.sub(r'ANILIS = ".*"\n', lambda m_: _AN, out)
out = re.sub(r"for nn in \('01', [^)]*\):", "for nn in ('01',):", out)
for l in out.split('\n'):
    for bad in ('b40', "'40'", "'161'", "'165'", '6_161_165', "'6:", 's6/'):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b01/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
