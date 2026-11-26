# sûre 7 blok 15 ARIZA oluşturucusu — sûre 6 blok 40 üreticisinden (s6/b40/yap/ariza_yap.py); bölüm açılışı, BEK bekleyen_ariza_7_b02.txt'ten
import re
src = open('/home/claude/s6/b40/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('\nI = [\n') + 1; k1 = src.index('\ndef yaz(II):')
R5 = '''R5 = [
 ("7:52", "'hudâ rahme qavm âmene'", 2, 'say 7:52 8-10', "harekesiz 'rahmeten li-qavmin yu'minûn' (8-10. kelime)", ('dizi 7 52 7 10', "hudâ rahme qavm âmene", '7-10', "biçim farkı (dizi 7 52 7 10): basılmamış eş i'râb, önek")),
 ("7:53", "'câ'e rasûl rabb haqq'", 2, 'say 7:53 14-17', "harekesiz 'câ'et rusulu rabbinâ bi'l-haqqi' (14-17. kelime)", ('dizi 7 53 14 17', "câ'e rasûl rabb haqq", '14-17', "biçim farkı (dizi 7 53 14 17): 7:43 yazım eş")),
 ("7:53", "'rabb haqq hel'", 2, 'say 7:53 16-18', "harekesiz 'rabbinâ bi'l-haqqi fe-hel' (16-18. kelime)", ('dizi 7 53 16 18', "rabb haqq hel", '16-18', "biçim farkı (dizi 7 53 16 18): 7:44 i'râb, önek")),
]
'''
VF = '''VF_YAZI = {52: {1: "'ve le-qad'", 8: "'ve rahmeten'"}, 53: {18: "'fe-hel'", 22: "'fe-yeşfe'û'", 26: "'fe-na'mele'", 34: "'ve dalle'"}}
sys.path.insert(0, '/home/claude/b15/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b15/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2', '# sûre 7 blok 15 (7:52-53) ARIZA oluşturucu — bölüm 5-4'), ('/home/claude/b40/', '/home/claude/b15/'),
     ("es_edat.py', '40'", "es_edat.py', '15'"), ('range(1, 41)', 'range(1, 16)'),
     ("'--plan', '40', '--numarasiz')", "'--plan', '15', '--numarasiz')"),
     ('ariza_6_161_165', 'ariza_7_52_53'), ('bag_6_161_165', 'bag_7_52_53'), ('(161, 165)', '(52, 53)'), ("'161', '165', '40'", "'52', '53', '15'"), ("'161', '165'", "'52', '53'"),
     ("_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}", "_ON = {'7:52', '7:53'}"), ('range(161, 166)', 'range(52, 54)'),
     ("x.startswith('6:')", "x.startswith('7:')"), ("== '6:%d' % a_", "== '7:%d' % a_"), ("return '6:%d: %s'", "return '7:%d: %s'"), ("r'\\b6:%d:\\d+'", "r'\\b7:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_6_*.txt')", "glob.glob('/home/claude/yamalar/ariza_7_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_7_b14k.txt'"),
     ("BOL = \"'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'\"", "BOL = \"'Cennet ehli, ateş ehli ve A'râf'takiler'\""),
     ("for _n in range(7, 35): _J", "for _n in range(7, 41): _J"), ("B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]", "B33, B34, B35, B36, B37, B38, B39, B40 = [_R['B%d' % _n].splitlines() for _n in range(6, 41)]"),
     ("'B34_HEPSI': (B34[-1] if B34 else '?'),", "'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'B39_HEPSI': (B39[-1] if B39 else '?'), 'B40_HEPSI': (B40[-1] if B40 else '?'),"),
     ("B32, B33, B34): print(", "B32, B33, B34, B35, B36, B37, B38, B39, B40): print("),
     ("BEK = []", "BEK = list(ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_7_b14.txt', encoding='utf-8').read() + ']'))"),
     ("sûre 6'nın okunmuş bütün ARIZA dosyaları", "sûre 7'nin okunmuş bütün ARIZA dosyaları"),
     ]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
_AN = """ANILIS = "7:53 kök قبل ('qablu' 12. kelime — önce): tetik listesinde yok; 7:53 kök نفس ('enfusehum' 33. kelime — kendi): tetik listesinde yok"\n"""
out = re.sub(r'ANILIS = ".*"\n', lambda m_: _AN, out)
out = re.sub(r"for nn in \('01', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15'):", out)
for l in out.split('\n'):
    for bad in ('b40', "'40'", "'161'", "'165'", '6_161_165', "'6:", 's6/'):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b15/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
