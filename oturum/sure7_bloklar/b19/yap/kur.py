# sûre 7 blok 19 ARIZA oluşturucusu — sûre 6 blok 40 üreticisinden (s6/b40/yap/ariza_yap.py); bölüm 7-2
import re
src = open('/home/claude/s6/b40/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('\nI = [\n') + 1; k1 = src.index('\ndef yaz(II):')
R5 = '''R5 = [
 ('7:65', "'qâle qavm 'abede allâh mâ _ min ilâh ğayr'", 4, 'say 7:65 5-13', "harekesiz 'qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû' (5-13. kelime)", ('dizi 7 65 5 13', "qâle qavm 'abede allâh mâ _ min ilâh ğayr", '5-13', 'biçim farkı (dizi 7 65 5 13): 7:59 önek; basılmamış eş yazım eş; basılmamış eş yazım eş')),
 ('7:66', "'qâle mele' ellezî kefere min qavm'", 2, 'say 7:66 3-6', "harekesiz 'llezîne kefarû min qavmihî' (3-6. kelime)", ('dizi 7 66 1 6', "qâle mele' ellezî kefere min qavm", '1-6', 'biçim farkı (dizi 7 66 1 6): basılmamış eş önek')),
 ('7:66', "'min qavm inne ra'â fî'", 2, 'say 7:66 5-9', "harekesiz 'min qavmihî innâ le-nerâke fî' (5-9. kelime)", ('dizi 7 66 5 9', "min qavm inne ra'â fî", '5-9', 'biçim farkı (dizi 7 66 5 9): 7:60 yazım eş')),
 ('7:66', "'qâle mele' ellezî'", 4, 'say 7:66 2-3', "harekesiz 'l-mele'u'llezîne' (2-3. kelime)", ('dizi 7 66 1 3', "qâle mele' ellezî", '1-3', 'biçim farkı (dizi 7 66 1 3): basılmamış eş yazım eş; basılmamış eş yazım eş; basılmamış eş önek')),
 ('7:67', "'lâkinne rasûl min rabb 'âlem'", 2, 'say 7:67 6-10', "harekesiz 've lâkinnî rasûlun min rabbi'l-'âlemîn' (6-10. kelime)", ('dizi 7 67 6 10', "lâkinne rasûl min rabb 'âlem", '6-10', 'biçim farkı (dizi 7 67 6 10): 7:61 yazım eş')),
 ('7:67', "'rasûl min rabb 'âlem'", 3, 'say 7:67 7-10', "harekesiz 'rasûlun min rabbi'l-'âlemîn' (7-10. kelime)", ('dizi 7 67 7 10', "rasûl min rabb 'âlem", '7-10', 'biçim farkı (dizi 7 67 7 10): 7:61 yazım eş; basılmamış eş yazım eş')),
 ('7:67', "'qâle qavm leyse _'", 2, 'say 7:67 1-4', "harekesiz 'qâle yâ qavmi leyse bî' (1-4. kelime)", ('dizi 7 67 1 4', 'qâle qavm leyse _', '1-4', 'biçim farkı (dizi 7 67 1 4): 7:61 yazım eş')),
 ('7:68', "'belliğ risâle rabb'", 2, 'say 7:68 1-3', "harekesiz 'ubelliğukum risâlâti rabbî' (1-3. kelime)", ('dizi 7 68 1 3', 'belliğ risâle rabb', '1-3', 'biçim farkı (dizi 7 68 1 3): 7:62 yazım eş')),
 ('7:69', "''acibu en câ'e zikr min rabb 'alâ racul min enzere'", 2, 'say 7:69 1-10', "harekesiz 'e-ve-'acibtum en câ'ekum zikrun min rabbikum 'alâ raculin minkum li-yunzirakum' (1-10. kelime)", ('dizi 7 69 1 10', "'acibu en câ'e zikr min rabb 'alâ racul min enzere", '1-10', 'biçim farkı (dizi 7 69 1 10): 7:63 yazım eş')),
 ('7:69', "'zekere iz ce'ale xalîfe min ba'd'", 2, 'say 7:69 11-16', "harekesiz 've'zkurû iz ce'alekum xulefâ'e min ba'di' (11-16. kelime)", ('dizi 7 69 11 16', "zekere iz ce'ale xalîfe min ba'd", '11-16', 'biçim farkı (dizi 7 69 11 16): basılmamış eş yazım eş')),
 ('7:69', "'zekere âlâ' allâh'", 2, 'say 7:69 23-25', "harekesiz 'fe'zkurû âlâ'e'llâhi' (23-25. kelime)", ('dizi 7 69 23 25', "zekere âlâ' allâh", '23-25', 'biçim farkı (dizi 7 69 23 25): basılmamış eş yazım eş')),
]
'''
VF = '''VF_YAZI = {65: {1: "'ve ilâ'", 14: "'e-fe-lâ'"}, 66: {8: "'le-nerâke'", 11: "'ve innâ'", 12: "'le-nezunnuke'"}, 67: {4: "'bî'", 6: "'ve lâkinnî'"}, 68: {4: "'ve ene'", 5: "'lekum'"}, 69: {1: "'e-ve-'acibtum'", 10: "'li-yunzirakum'", 11: "'ve'zkurû'", 19: "'ve zâdekum'", 23: "'fe'zkurû'"}}
sys.path.insert(0, '/home/claude/b19/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b19/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2', '# sûre 7 blok 19 (7:65-69) ARIZA oluşturucu — bölüm 7-2'), ('/home/claude/b40/', '/home/claude/b19/'),
     ("es_edat.py', '40'", "es_edat.py', '19'"), ('range(1, 41)', 'range(1, 20)'),
     ("'--plan', '40', '--numarasiz')", "'--plan', '19', '--numarasiz')"),
     ('ariza_6_161_165', 'ariza_7_65_69'), ('bag_6_161_165', 'bag_7_65_69'), ('(161, 165)', '(65, 69)'), ("'161', '165', '40'", "'65', '69', '19'"), ("'161', '165'", "'65', '69'"),
     ("_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}", "_ON = {'7:65', '7:66', '7:67', '7:68', '7:69'}"), ('range(161, 166)', 'range(65, 70)'),
     ("x.startswith('6:')", "x.startswith('7:')"), ("== '6:%d' % a_", "== '7:%d' % a_"), ("return '6:%d: %s'", "return '7:%d: %s'"), ("r'\\b6:%d:\\d+'", "r'\\b7:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_6_*.txt')", "glob.glob('/home/claude/yamalar/ariza_7_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_7_b17k.txt'"),
     ("BOL = \"'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'\"", "BOL = \"'Nûh ve kavmi; Hûd ve Âd'\""),
     ("for _n in range(7, 35): _J", "for _n in range(7, 43): _J"), ("B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]", "B33, B34, B35, B36, B37, B38, B39, B40, B41, B42 = [_R['B%d' % _n].splitlines() for _n in range(6, 43)]"),
     ("'B34_HEPSI': (B34[-1] if B34 else '?'),", "'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'B39_HEPSI': (B39[-1] if B39 else '?'), 'B40_HEPSI': (B40[-1] if B40 else '?'), 'B41_HEPSI': (B41[-1] if B41 else '?'), 'B42_HEPSI': (B42[-1] if B42 else '?'),"),
     ("B32, B33, B34): print(", "B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42): print("),
     ("sûre 6'nın okunmuş bütün ARIZA dosyaları", "sûre 7'nin okunmuş bütün ARIZA dosyaları"),
     ]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
_AN = """ANILIS = "7:69 'iz' (12. kelime — morph T, zaman); 7:69 kök بعد ('ba'di' 16. kelime — sonra): tetik listesinde yok; 7:69 kök رجل ('raculin' 8. kelime — adam): tetik listesinde yok"\n"""
out = re.sub(r'ANILIS = ".*"\n', lambda m_: _AN, out)
out = re.sub(r"for nn in \('01', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'):", out)
for l in out.split('\n'):
    for bad in ('b40', "'40'", "'161'", "'165'", '6_161_165', "'6:", 's6/'):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b19/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
