# sûre 7 blok 6 ARIZA oluşturucusu — sûre 6 blok 40 üreticisinden (s6/b40/yap/ariza_yap.py); bölüm açılışı, BEK bekleyen_ariza_7_b02.txt'ten
import re
src = open('/home/claude/s6/b40/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('\nI = [\n') + 1; k1 = src.index('\ndef yaz(II):')
R5 = '''R5 = [
 ("7:23", "'ğafera _ rahime'", 2, 'say 7:23 7-9', "harekesiz 'teğfir lenâ ve terhamnâ' (7-9. kelime)", ('dizi 7 23 7 9', "ğafera _ rahime", '7-9', "biçim farkı (dizi 7 23 7 9): basılmamış eş fiil çekimi, önek")),
 ("7:23", "'kâne min xâsir'", 2, 'say 7:23 10-12', "harekesiz 'le-nekûnenne mine'l-xâsirîn' (10-12. kelime)", ('dizi 7 23 10 12', "kâne min xâsir", '10-12', "biçim farkı (dizi 7 23 10 12): basılmamış eş yazım eş")),
]
'''
VF = '''VF_YAZI = {22: {9: "'ve tafiqâ'", 15: "'ve nâdâhumâ'", 22: "'ve aqul'"}, 23: {5: "'ve in'", 9: "'ve terhamnâ'"}, 24: {6: "'ve lekum'", 10: "'ve metâ'un'"}, 25: {4: "'ve fîhâ'", 6: "'ve minhâ'"}}
sys.path.insert(0, '/home/claude/b06/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b06/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2', '# sûre 7 blok 6 (7:22-25) ARIZA oluşturucu — bölüm 2-4'), ('/home/claude/b40/', '/home/claude/b06/'),
     ("es_edat.py', '40'", "es_edat.py', '06'"), ('range(1, 41)', 'range(1, 7)'),
     ("'--plan', '40', '--numarasiz')", "'--plan', '6', '--numarasiz')"),
     ('ariza_6_161_165', 'ariza_7_22_25'), ('bag_6_161_165', 'bag_7_22_25'), ('(161, 165)', '(22, 25)'), ("'161', '165', '40'", "'22', '25', '06'"), ("'161', '165'", "'22', '25'"),
     ("_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}", "_ON = {'7:22', '7:23', '7:24', '7:25'}"), ('range(161, 166)', 'range(22, 26)'),
     ("x.startswith('6:')", "x.startswith('7:')"), ("== '6:%d' % a_", "== '7:%d' % a_"), ("return '6:%d: %s'", "return '7:%d: %s'"), ("r'\\b6:%d:\\d+'", "r'\\b7:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_6_*.txt')", "glob.glob('/home/claude/yamalar/ariza_7_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_7_b02k.txt'"),
     ("BOL = \"'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'\"", "BOL = \"'Âdem'e secde; İblis'in mühleti; ağaç ve iniş'\""),
     ("for _n in range(7, 35): _J", "for _n in range(7, 37): _J"), ("B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]", "B33, B34, B35, B36 = [_R['B%d' % _n].splitlines() for _n in range(6, 37)]"),
     ("'B34_HEPSI': (B34[-1] if B34 else '?'),", "'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'),"),
     ("B32, B33, B34): print(", "B32, B33, B34, B35, B36): print("),
     ("sûre 6'nın okunmuş bütün ARIZA dosyaları", "sûre 7'nin okunmuş bütün ARIZA dosyaları"),
     ]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
_AN = """ANILIS = "7:22 'lemmâ' (3. kelime — morph T, zaman); 7:22 kök سوأ ('sev'âtuhumâ' 8. kelime — çirkin yer): tetik listesinde yok; 7:23 kök نفس ('enfusenâ' 4. kelime — kendi): tetik listesinde yok"\n"""
out = re.sub(r'ANILIS = ".*"\n', lambda m_: _AN, out)
out = re.sub(r"for nn in \('01', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06'):", out)
for l in out.split('\n'):
    for bad in ('b40', "'40'", "'161'", "'165'", '6_161_165', "'6:", 's6/'):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b06/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
