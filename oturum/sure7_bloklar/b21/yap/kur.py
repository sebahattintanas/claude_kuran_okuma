# sûre 7 blok 21 ARIZA oluşturucusu — sûre 6 blok 40 üreticisinden (s6/b40/yap/ariza_yap.py); bölüm açılışı, BEK bekleyen_ariza_7_b20.txt'ten
import re
src = open('/home/claude/s6/b40/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('\nI = [\n') + 1; k1 = src.index('\ndef yaz(II):')
R5 = '''R5 = [
 ('7:73', "'qâle qavm 'abede allâh mâ _ min ilâh ğayr qad câ'e beyyine min rabb'", 2, 'say 7:73 5-18', "harekesiz 'qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû qad câ'etkum beyyinetun min rabbikum' (5-18. kelime)", ('dizi 7 73 5 18', "qâle qavm 'abede allâh mâ _ min ilâh ğayr qad câ'e beyyine min rabb", '5-18', 'biçim farkı (dizi 7 73 5 18): basılmamış eş yazım eş')),
 ('7:73', "'qâle qavm 'abede allâh mâ _ min ilâh ğayr'", 4, 'say 7:73 5-13', "harekesiz 'qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû' (5-13. kelime)", ('dizi 7 73 5 13', "qâle qavm 'abede allâh mâ _ min ilâh ğayr", '5-13', 'biçim farkı (dizi 7 73 5 13): 7:59 önek; 7:65 yazım eş; basılmamış eş yazım eş; öneksiz eş koşusu (dizi 7 73 5 13): 7:59 → önek kesilmiş sûre içi 1; 7:65 → önek kesilmiş sûre içi 4; basılmamış eş → önek kesilmiş sûre içi 4')),
 ('7:73', "'qad câ'e beyyine min rabb'", 3, 'say 7:73 14-18', "harekesiz 'qad câ'etkum beyyinetun min rabbikum' (14-18. kelime)", ('dizi 7 73 14 18', "qad câ'e beyyine min rabb", '14-18', "biçim farkı (dizi 7 73 14 18): basılmamış eş yazım eş; basılmamış eş fiil çekimi, i'râb, zamir eki, önek; öneksiz eş koşusu (dizi 7 73 14 18): basılmamış eş → önek kesilmiş sûre içi 2; basılmamış eş → önek kesilmiş sûre içi 1")),
 ('7:74', "'zekere iz ce'ale xalîfe min ba'd'", 2, 'say 7:74 1-6', "harekesiz 've'zkurû iz ce'alekum xulefâ'e min ba'di' (1-6. kelime)", ('dizi 7 74 1 6', "zekere iz ce'ale xalîfe min ba'd", '1-6', 'biçim farkı (dizi 7 74 1 6): 7:69 yazım eş')),
 ('7:74', "'zekere âlâ' allâh'", 2, 'say 7:74 18-20', "harekesiz 'fe'zkurû âlâ'e'llâhi' (18-20. kelime)", ('dizi 7 74 18 20', "zekere âlâ' allâh", '18-20', 'biçim farkı (dizi 7 74 18 20): 7:69 yazım eş')),
 ('7:75', "'qâle mele' ellezî istekbere min qavm'", 2, 'say 7:75 1-6', "harekesiz 'qâle'l-mele'u'llezîne'stekberû min qavmihî' (1-6. kelime)", ('dizi 7 75 1 6', "qâle mele' ellezî istekbere min qavm", '1-6', 'biçim farkı (dizi 7 75 1 6): basılmamış eş yazım eş')),
 ('7:75', "'qâle mele' ellezî'", 4, 'say 7:75 1-3', "harekesiz 'qâle'l-mele'u'llezîne' (1-3. kelime)", ('dizi 7 75 1 3', "qâle mele' ellezî", '1-3', 'biçim farkı (dizi 7 75 1 3): 7:66 yazım eş; basılmamış eş yazım eş; basılmamış eş önek; öneksiz eş koşusu (dizi 7 75 1 3): 7:66 → önek kesilmiş sûre içi 4; basılmamış eş → önek kesilmiş sûre içi 4; basılmamış eş → önek kesilmiş sûre içi 1')),
]
'''
VF = '''VF_YAZI = {73: {1: "'ve ilâ'", 6: "'yâ qavmi'", 10: "'lekum'", 22: "'lekum'", 24: "'fe-zerûhâ'", 29: "'ve lâ'", 31: "'bi-sû'in'", 32: "'fe-ye'xuzekum'"}, 74: {1: "'ve'zkurû'", 8: "'ve bevve'ekum'", 15: "'ve tenhitûne'", 18: "'fe'zkurû'", 21: "'ve lâ'"}, 75: {7: "'li'llezîne'", 9: "'li-men'", 12: "'e-ta'lemûne'", 20: "'bi-mâ'", 22: "'bihî'"}}
sys.path.insert(0, '/home/claude/b21/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b21/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2', '# sûre 7 blok 21 (7:73-75) ARIZA oluşturucu — bölüm 8-1'), ('/home/claude/b40/', '/home/claude/b21/'),
     ("es_edat.py', '40'", "es_edat.py', '21'"), ('range(1, 41)', 'range(1, 22)'),
     ("'--plan', '40', '--numarasiz')", "'--plan', '21', '--numarasiz')"),
     ('ariza_6_161_165', 'ariza_7_73_75'), ('bag_6_161_165', 'bag_7_73_75'), ('(161, 165)', '(73, 75)'), ("'161', '165', '40'", "'73', '75', '21'"), ("'161', '165'", "'73', '75'"),
     ("_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}", "_ON = {'7:73', '7:74', '7:75'}"), ('range(161, 166)', 'range(73, 76)'),
     ("x.startswith('6:')", "x.startswith('7:')"), ("== '6:%d' % a_", "== '7:%d' % a_"), ("return '6:%d: %s'", "return '7:%d: %s'"), ("r'\\b6:%d:\\d+'", "r'\\b7:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_6_*.txt')", "glob.glob('/home/claude/yamalar/ariza_7_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_7_b20k.txt'"),
     ("BOL = \"'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'\"", "BOL = \"'Sâlih ve Semûd; Lût ve kavmi'\""),
     ("for _n in range(7, 35): _J", "for _n in range(7, 44): _J"), ("B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]", "B33, B34, B35, B36, B37, B38, B39, B40, B41, B42, B43 = [_R['B%d' % _n].splitlines() for _n in range(6, 44)]"),
     ("'B34_HEPSI': (B34[-1] if B34 else '?'),", "'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'B39_HEPSI': (B39[-1] if B39 else '?'), 'B40_HEPSI': (B40[-1] if B40 else '?'), 'B41_HEPSI': (B41[-1] if B41 else '?'), 'B42_HEPSI': (B42[-1] if B42 else '?'), 'B43_HEPSI': (B43[-1] if B43 else '?'),"),
     ("B32, B33, B34): print(", "B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42, B43): print("),
     ("BEK = []", "BEK = list(ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_7_b20.txt', encoding='utf-8').read() + ']'))"),
     ("sûre 6'nın okunmuş bütün ARIZA dosyaları", "sûre 7'nin okunmuş bütün ARIZA dosyaları"),
     ]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
_AN = """ANILIS = "7:73 kök سوأ ('bi-sû'in' 31. kelime — kötülük): tetik listesinde yok; 7:74 'iz' (2. kelime — morph T, zaman); 7:74 kök بعد ('ba'di' 6. kelime — sonra): tetik listesinde yok"\n"""
out = re.sub(r'ANILIS = ".*"\n', lambda m_: _AN, out)
out = re.sub(r"for nn in \('01', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'):", out)
for l in out.split('\n'):
    for bad in ('b40', "'40'", "'161'", "'165'", '6_161_165', "'6:", 's6/'):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b21/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
