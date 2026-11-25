# sûre 7 blok 10 ARIZA oluşturucusu — sûre 6 blok 40 üreticisinden (s6/b40/yap/ariza_yap.py); bölüm açılışı, BEK bekleyen_ariza_7_b02.txt'ten
import re
src = open('/home/claude/s6/b40/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('\nI = [\n') + 1; k1 = src.index('\ndef yaz(II):')
R5 = '''R5 = [
 ("7:36", "'kezzebe âye istekbere 'an'", 2, 'say 7:36 2-5', "harekesiz 'kezzebû bi-âyâtinâ ve'stekberû 'anhâ' (2-5. kelime)", ('dizi 7 36 2 5', "kezzebe âye istekbere 'an", '2-5', "biçim farkı (dizi 7 36 2 5): basılmamış eş yazım eş")),
 ("7:36", "'ellezî kezzebe âye'", 3, 'say 7:36 1-3', "harekesiz 've'llezîne kezzebû bi-âyâtinâ' (1-3. kelime); biçim öğesi 'ellezî' öneki (lemma dizisi sûre içi 8, nakarat3 3)", ('dizi 7 36 1 3', "ellezî kezzebe âye", '1-3', "biçim farkı (dizi 7 36 1 3): basılmamış eş önek; basılmamış eş önek; basılmamış eş önek; basılmamış eş yazım eş; basılmamış eş önek; basılmamış eş önek; basılmamış eş yazım eş")),
 ("7:36", "'_ fî xâlid'", 2, 'say 7:36 9-11', "harekesiz 'hum fîhâ xâlidûn' (9-11. kelime)", ('dizi 7 36 9 11', "_ fî xâlid", '9-11', "biçim farkı (dizi 7 36 9 11): basılmamış eş yazım eş")),
 ("7:37", "'ifterâ 'alâ allâh kezib'", 2, 'say 7:37 4-7', "harekesiz 'fterâ 'ale'llâhi keziben' (4-7. kelime)", ('dizi 7 37 4 7', "ifterâ 'alâ allâh kezib", '4-7', "biçim farkı (dizi 7 37 4 7): basılmamış eş fiil çekimi, zamir eki")),
 ("7:37", "'de'â min dûn allâh'", 2, 'say 7:37 25-28', "harekesiz 'ted'ûne min dûni'llâhi' (25-28. kelime)", ('dizi 7 37 25 28', "de'â min dûn allâh", '25-28', "biçim farkı (dizi 7 37 25 28): basılmamış eş yazım eş")),
 ("7:37", "'min dûn allâh'", 3, 'say 7:37 26-28', "harekesiz 'min dûni'llâhi' (26-28. kelime)", ('dizi 7 37 26 28', "min dûn allâh", '26-28', "biçim farkı (dizi 7 37 26 28): 7:30 yazım eş; basılmamış eş yazım eş")),
 ("7:37", "'de'â min dûn'", 3, 'say 7:37 25-27', "harekesiz 'ted'ûne min dûni' (25-27. kelime)", ('dizi 7 37 25 27', "de'â min dûn", '25-27', "biçim farkı (dizi 7 37 25 27): basılmamış eş yazım eş; basılmamış eş zamir eki")),
]
'''
VF = '''VF_YAZI = {35: {10: "'fe-meni'", 12: "'ve asleha'", 13: "'fe-lâ'", 16: "'ve lâ'"}, 36: {1: "'ve'llezîne'", 4: "'ve'stekberû'"}, 37: {1: "'fe-men'", 32: "'ve şehidû'"}}
sys.path.insert(0, '/home/claude/b10/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b10/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2', '# sûre 7 blok 10 (7:35-37) ARIZA oluşturucu — bölüm 4-1'), ('/home/claude/b40/', '/home/claude/b10/'),
     ("es_edat.py', '40'", "es_edat.py', '10'"), ('range(1, 41)', 'range(1, 11)'),
     ("'--plan', '40', '--numarasiz')", "'--plan', '10', '--numarasiz')"),
     ('ariza_6_161_165', 'ariza_7_35_37'), ('bag_6_161_165', 'bag_7_35_37'), ('(161, 165)', '(35, 37)'), ("'161', '165', '40'", "'35', '37', '10'"), ("'161', '165'", "'35', '37'"),
     ("_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}", "_ON = {'7:35', '7:36', '7:37'}"), ('range(161, 166)', 'range(35, 38)'),
     ("x.startswith('6:')", "x.startswith('7:')"), ("== '6:%d' % a_", "== '7:%d' % a_"), ("return '6:%d: %s'", "return '7:%d: %s'"), ("r'\\b6:%d:\\d+'", "r'\\b7:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_6_*.txt')", "glob.glob('/home/claude/yamalar/ariza_7_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_7_b09k.txt'"),
     ("BOL = \"'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'\"", "BOL = \"'Elçiler gelince; yalanlayanların ateşte çekişmesi'\""),
     ("for _n in range(7, 35): _J", "for _n in range(7, 39): _J"), ("B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]", "B33, B34, B35, B36, B37, B38 = [_R['B%d' % _n].splitlines() for _n in range(6, 39)]"),
     ("'B34_HEPSI': (B34[-1] if B34 else '?'),", "'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'),"),
     ("B32, B33, B34): print(", "B32, B33, B34, B35, B36, B37, B38): print("),
     ("BEK = []", "BEK = list(ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_7_b09.txt', encoding='utf-8').read() + ']'))"),
     ("sûre 6'nın okunmuş bütün ARIZA dosyaları", "sûre 7'nin okunmuş bütün ARIZA dosyaları"),
     ]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
_AN = """ANILIS = "7:37 'izâ' (17. kelime — morph T, zaman); 7:37 kök نفس ('enfusihim' 34. kelime — kendi): tetik listesinde yok"\n"""
out = re.sub(r'ANILIS = ".*"\n', lambda m_: _AN, out)
out = re.sub(r"for nn in \('01', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10'):", out)
for l in out.split('\n'):
    for bad in ('b40', "'40'", "'161'", "'165'", '6_161_165', "'6:", 's6/'):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b10/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
