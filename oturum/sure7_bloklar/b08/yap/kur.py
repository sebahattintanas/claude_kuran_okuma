# sûre 7 blok 8 ARIZA oluşturucusu — sûre 6 blok 40 üreticisinden (s6/b40/yap/ariza_yap.py); bölüm açılışı, BEK bekleyen_ariza_7_b02.txt'ten
import re
src = open('/home/claude/s6/b40/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('\nI = [\n') + 1; k1 = src.index('\ndef yaz(II):')
R5 = '''R5 = [
 ("7:28", "'qâle 'alâ allâh mâ lâ 'alime'", 2, 'say 7:28 17-22', "harekesiz 'e-teqûlûne 'ale'llâhi mâ lâ ta'lemûn' (17-22. kelime)", ('dizi 7 28 17 22', "qâle 'alâ allâh mâ lâ 'alime", '17-22', "biçim farkı (dizi 7 28 17 22): basılmamış eş önek")),
 ("7:28", "'allâh mâ lâ 'alime'", 3, 'say 7:28 19-22', "harekesiz 'llâhi mâ lâ ta'lemûn' (19-22. kelime)", ('dizi 7 28 19 22', "allâh mâ lâ 'alime", '19-22', "biçim farkı (dizi 7 28 19 22): basılmamış eş yazım eş; basılmamış eş yazım eş")),
 ("7:28", "'qâle 'alâ allâh'", 4, 'say 7:28 17-19', "harekesiz 'e-teqûlûne 'ale'llâhi' (17-19. kelime)", ('dizi 7 28 17 19', "qâle 'alâ allâh", '17-19', "biçim farkı (dizi 7 28 17 19): basılmamış eş önek; basılmamış eş fiil çekimi, zamir eki, önek; basılmamış eş fiil çekimi, zamir eki, önek")),
 ("7:28", "'qâle inne allâh'", 2, 'say 7:28 11-13', "harekesiz 'qul inne'llâhe' (11-13. kelime)", ('dizi 7 28 11 13', "qâle inne allâh", '11-13', "biçim farkı (dizi 7 28 11 13): basılmamış eş fiil çekimi, zamir eki")),
 ("7:29", "''inde kull mescid'", 2, 'say 7:29 7-9', "harekesiz ''inde kulli mescidin' (7-9. kelime)", ('dizi 7 29 7 9', "'inde kull mescid", '7-9', "biçim farkı (dizi 7 29 7 9): basılmamış eş yazım eş")),
 ("7:30", "'min dûn allâh'", 3, 'say 7:30 11-13', "harekesiz 'min dûni'llâhi' (11-13. kelime)", ('dizi 7 30 11 13', "min dûn allâh", '11-13', "biçim farkı (dizi 7 30 11 13): basılmamış eş yazım eş; basılmamış eş yazım eş")),
]
'''
VF = '''VF_YAZI = {28: {1: "'ve izâ'", 8: "'ve'llâhu'"}, 29: {5: "'ve aqîmû'", 10: "'ve'd'ûhu'"}, 30: {3: "'ve ferîqan'", 14: "'ve yahsebûne'"}}
sys.path.insert(0, '/home/claude/b08/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b08/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2', '# sûre 7 blok 8 (7:28-30) ARIZA oluşturucu — bölüm 3-2'), ('/home/claude/b40/', '/home/claude/b08/'),
     ("es_edat.py', '40'", "es_edat.py', '08'"), ('range(1, 41)', 'range(1, 9)'),
     ("'--plan', '40', '--numarasiz')", "'--plan', '8', '--numarasiz')"),
     ('ariza_6_161_165', 'ariza_7_28_30'), ('bag_6_161_165', 'bag_7_28_30'), ('(161, 165)', '(28, 30)'), ("'161', '165', '40'", "'28', '30', '08'"), ("'161', '165'", "'28', '30'"),
     ("_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}", "_ON = {'7:28', '7:29', '7:30'}"), ('range(161, 166)', 'range(28, 31)'),
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
_AN = """ANILIS = "7:28 'izâ' (1. kelime — morph T, zaman); 7:29 kök وجه ('vucûhekum' 6. kelime — yüz): tetik listesinde yok; 7:30 kök ولي ('evliyâ'e' 10. kelime — dost): tetik listesinde yok"\n"""
out = re.sub(r'ANILIS = ".*"\n', lambda m_: _AN, out)
out = re.sub(r"for nn in \('01', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08'):", out)
for l in out.split('\n'):
    for bad in ('b40', "'40'", "'161'", "'165'", '6_161_165', "'6:", 's6/'):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b08/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
