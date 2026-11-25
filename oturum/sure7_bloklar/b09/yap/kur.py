# sûre 7 blok 9 ARIZA oluşturucusu — sûre 6 blok 40 üreticisinden (s6/b40/yap/ariza_yap.py); bölüm açılışı, BEK bekleyen_ariza_7_b02.txt'ten
import re
src = open('/home/claude/s6/b40/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('\nI = [\n') + 1; k1 = src.index('\ndef yaz(II):')
R5 = '''R5 = [
 ("7:31", "''inde kull mescid'", 2, 'say 7:31 5-7', "harekesiz ''inde kulli mescidin' (5-7. kelime)", ('dizi 7 31 5 7', "'inde kull mescid", '5-7', "biçim farkı (dizi 7 31 5 7): 7:29 yazım eş")),
 ("7:31", "'inne lâ ahbeb'", 2, 'say 7:31 12-14', "harekesiz 'innehû lâ yuhibbu' (12-14. kelime)", ('dizi 7 31 12 14', "inne lâ ahbeb", '12-14', "biçim farkı (dizi 7 31 12 14): basılmamış eş yazım eş")),
 ("7:32", "'fî hayâ dunyâ'", 2, 'say 7:32 16-18', "harekesiz 'fi'l-hayâti'd-dunyâ' (16-18. kelime)", ('dizi 7 32 16 18', "fî hayâ dunyâ", '16-18', "biçim farkı (dizi 7 32 16 18): basılmamış eş yazım eş")),
 ("7:33", "'qâle 'alâ allâh mâ lâ 'alime'", 2, 'say 7:33 24-29', "harekesiz 'teqûlû 'ale'llâhi mâ lâ ta'lemûn' (24-29. kelime)", ('dizi 7 33 24 29', "qâle 'alâ allâh mâ lâ 'alime", '24-29', "biçim farkı (dizi 7 33 24 29): 7:28 önek")),
 ("7:33", "'allâh mâ lâ 'alime'", 3, 'say 7:33 26-29', "harekesiz 'llâhi mâ lâ ta'lemûn' (26-29. kelime)", ('dizi 7 33 26 29', "allâh mâ lâ 'alime", '26-29', "biçim farkı (dizi 7 33 26 29): 7:28 yazım eş; basılmamış eş yazım eş")),
 ("7:33", "'qâle 'alâ allâh'", 4, 'say 7:33 24-26', "harekesiz 'teqûlû 'ale'llâhi' (24-26. kelime)", ('dizi 7 33 24 26', "qâle 'alâ allâh", '24-26', "biçim farkı (dizi 7 33 24 26): 7:28 önek; basılmamış eş fiil çekimi, zamir eki; basılmamış eş fiil çekimi, zamir eki")),
]
'''
VF = '''VF_YAZI = {31: {8: "'ve kulû'", 9: "'ve'şrabû'", 10: "'ve lâ'"}, 32: {9: "'ve't-tayyibâti'"}, 33: {9: "'ve mâ'", 11: "'ve'l-isme'", 12: "'ve'l-bağye'", 15: "'ve en'", 23: "'ve en'"}, 34: {1: "'ve li-kulli'", 4: "'fe-izâ'", 10: "'ve lâ'"}}
sys.path.insert(0, '/home/claude/b09/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b09/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2', '# sûre 7 blok 9 (7:31-34) ARIZA oluşturucu — bölüm 3-3'), ('/home/claude/b40/', '/home/claude/b09/'),
     ("es_edat.py', '40'", "es_edat.py', '09'"), ('range(1, 41)', 'range(1, 10)'),
     ("'--plan', '40', '--numarasiz')", "'--plan', '9', '--numarasiz')"),
     ('ariza_6_161_165', 'ariza_7_31_34'), ('bag_6_161_165', 'bag_7_31_34'), ('(161, 165)', '(31, 34)'), ("'161', '165', '40'", "'31', '34', '09'"), ("'161', '165'", "'31', '34'"),
     ("_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}", "_ON = {'7:31', '7:32', '7:33', '7:34'}"), ('range(161, 166)', 'range(31, 35)'),
     ("x.startswith('6:')", "x.startswith('7:')"), ("== '6:%d' % a_", "== '7:%d' % a_"), ("return '6:%d: %s'", "return '7:%d: %s'"), ("r'\\b6:%d:\\d+'", "r'\\b7:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_6_*.txt')", "glob.glob('/home/claude/yamalar/ariza_7_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_7_b06k.txt'"),
     ("BOL = \"'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'\"", "BOL = \"'Ey Âdemoğulları: giysi, fitne, ziynet; haram kılınanlar'\""),
     ("for _n in range(7, 35): _J", "for _n in range(7, 38): _J"), ("B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]", "B33, B34, B35, B36, B37 = [_R['B%d' % _n].splitlines() for _n in range(6, 38)]"),
     ("'B34_HEPSI': (B34[-1] if B34 else '?'),", "'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'),"),
     ("B32, B33, B34): print(", "B32, B33, B34, B35, B36, B37): print("),
     ("sûre 6'nın okunmuş bütün ARIZA dosyaları", "sûre 7'nin okunmuş bütün ARIZA dosyaları"),
     ]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
_AN = """ANILIS = "7:32 kök دنو ('d-dunyâ' 18. kelime — dünya): tetik listesinde yok; 7:33 kök ظهر ('zahera' 7. kelime — açık): tetik listesinde yok; 7:33 kök بطن ('betane' 10. kelime — gizli): tetik listesinde yok; 7:34 'izâ' (4. kelime — morph T, zaman); 7:34 kök أخر ('yeste'xirûne' 8. kelime — geri kal-): tetik listesinde yok"\n"""
out = re.sub(r'ANILIS = ".*"\n', lambda m_: _AN, out)
out = re.sub(r"for nn in \('01', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09'):", out)
for l in out.split('\n'):
    for bad in ('b40', "'40'", "'161'", "'165'", '6_161_165', "'6:", 's6/'):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b09/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
