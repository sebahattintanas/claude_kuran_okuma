# sûre 7 blok 14 ARIZA oluşturucusu — sûre 6 blok 40 üreticisinden (s6/b40/yap/ariza_yap.py); bölüm açılışı, BEK bekleyen_ariza_7_b02.txt'ten
import re
src = open('/home/claude/s6/b40/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('\nI = [\n') + 1; k1 = src.index('\ndef yaz(II):')
R5 = '''R5 = [
 ("7:48", "'a'râf ricâl 'arafe'", 2, 'say 7:48 3-5', "harekesiz 'l-a'râfi ricâlen ya'rifûnehum' (3-5. kelime)", ('dizi 7 48 3 5', "a'râf ricâl 'arafe", '3-5', "biçim farkı (dizi 7 48 3 5): 7:46 elif yazımı, zamir eki")),
 ("7:50", "'qâle inne allâh'", 2, 'say 7:50 15-17', "harekesiz 'qâlû inne'llâhe' (15-17. kelime)", ('dizi 7 50 15 17', "qâle inne allâh", '15-17', "biçim farkı (dizi 7 50 15 17): 7:28 fiil çekimi, zamir eki")),
 ("7:50", "'ashâb cenne en'", 2, 'say 7:50 4-6', "harekesiz 'ashâbe'l-cenneti en' (4-6. kelime)", ('dizi 7 50 4 6', "ashâb cenne en", '4-6', "biçim farkı (dizi 7 50 4 6): 7:46 yazım eş")),
]
'''
VF = '''VF_YAZI = {48: {1: "'ve nâdâ'", 12: "'ve mâ'"}, 49: {13: "'ve lâ'"}, 50: {1: "'ve nâdâ'"}, 51: {5: "'ve la'iben'", 6: "'ve ğarrathumu'", 9: "'fe'l-yevme'", 16: "'ve mâ'"}}
sys.path.insert(0, '/home/claude/b14/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b14/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2', '# sûre 7 blok 14 (7:48-51) ARIZA oluşturucu — bölüm 5-3'), ('/home/claude/b40/', '/home/claude/b14/'),
     ("es_edat.py', '40'", "es_edat.py', '14'"), ('range(1, 41)', 'range(1, 15)'),
     ("'--plan', '40', '--numarasiz')", "'--plan', '14', '--numarasiz')"),
     ('ariza_6_161_165', 'ariza_7_48_51'), ('bag_6_161_165', 'bag_7_48_51'), ('(161, 165)', '(48, 51)'), ("'161', '165', '40'", "'48', '51', '14'"), ("'161', '165'", "'48', '51'"),
     ("_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}", "_ON = {'7:48', '7:49', '7:50', '7:51'}"), ('range(161, 166)', 'range(48, 52)'),
     ("x.startswith('6:')", "x.startswith('7:')"), ("== '6:%d' % a_", "== '7:%d' % a_"), ("return '6:%d: %s'", "return '7:%d: %s'"), ("r'\\b6:%d:\\d+'", "r'\\b7:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_6_*.txt')", "glob.glob('/home/claude/yamalar/ariza_7_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_7_b11k.txt'"),
     ("BOL = \"'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'\"", "BOL = \"'Cennet ehli, ateş ehli ve A'râf'takiler'\""),
     ("for _n in range(7, 35): _J", "for _n in range(7, 40): _J"), ("B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]", "B33, B34, B35, B36, B37, B38, B39 = [_R['B%d' % _n].splitlines() for _n in range(6, 40)]"),
     ("'B34_HEPSI': (B34[-1] if B34 else '?'),", "'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'B39_HEPSI': (B39[-1] if B39 else '?'),"),
     ("B32, B33, B34): print(", "B32, B33, B34, B35, B36, B37, B38, B39): print("),
     ("sûre 6'nın okunmuş bütün ARIZA dosyaları", "sûre 7'nin okunmuş bütün ARIZA dosyaları"),
     ]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
_AN = """ANILIS = "7:48 kök رجل ('ricâlen' 4. kelime — adam): tetik listesinde yok; 7:48 kök جمع ('cem'ukum' 11. kelime — topluluk): tetik listesinde yok; 7:51 kök دنو ('d-dunyâ' 8. kelime — dünya): tetik listesinde yok"\n"""
out = re.sub(r'ANILIS = ".*"\n', lambda m_: _AN, out)
out = re.sub(r"for nn in \('01', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'):", out)
for l in out.split('\n'):
    for bad in ('b40', "'40'", "'161'", "'165'", '6_161_165', "'6:", 's6/'):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b14/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
