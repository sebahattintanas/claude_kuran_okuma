# sûre 7 blok 18 ARIZA oluşturucusu — sûre 6 blok 40 üreticisinden (s6/b40/yap/ariza_yap.py); bölüm açılışı, BEK bekleyen_ariza_7_b17.txt'ten
import re
src = open('/home/claude/s6/b40/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('\nI = [\n') + 1; k1 = src.index('\ndef yaz(II):')
R5 = '''R5 = [
 ('7:59', "'qâle qavm 'abede allâh mâ _ min ilâh ğayr'", 4, 'say 7:59 6-14', "harekesiz 'fe-qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû' (6-14. kelime)", ('dizi 7 59 6 14', "qâle qavm 'abede allâh mâ _ min ilâh ğayr", '6-14', 'biçim farkı (dizi 7 59 6 14): basılmamış eş önek; basılmamış eş önek; basılmamış eş önek')),
 ('7:60', "'min qavm inne ra'â fî'", 2, 'say 7:60 3-7', "harekesiz 'min qavmihî innâ le-nerâke fî' (3-7. kelime)", ('dizi 7 60 3 7', "min qavm inne ra'â fî", '3-7', 'biçim farkı (dizi 7 60 3 7): basılmamış eş yazım eş')),
 ('7:60', "'qâle mele' min qavm'", 3, 'say 7:60 2-4', "harekesiz 'l-mele'u min qavmihî' (2-4. kelime)", ('dizi 7 60 1 4', "qâle mele' min qavm", '1-4', 'biçim farkı (dizi 7 60 1 4): basılmamış eş zamir eki; basılmamış eş zamir eki, önek')),
 ('7:61', "'lâkinne rasûl min rabb 'âlem'", 2, 'say 7:61 6-10', "harekesiz 've lâkinnî rasûlun min rabbi'l-'âlemîn' (6-10. kelime)", ('dizi 7 61 6 10', "lâkinne rasûl min rabb 'âlem", '6-10', 'biçim farkı (dizi 7 61 6 10): basılmamış eş yazım eş')),
 ('7:61', "'rasûl min rabb 'âlem'", 3, 'say 7:61 7-10', "harekesiz 'rasûlun min rabbi'l-'âlemîn' (7-10. kelime)", ('dizi 7 61 7 10', "rasûl min rabb 'âlem", '7-10', 'biçim farkı (dizi 7 61 7 10): basılmamış eş yazım eş; basılmamış eş yazım eş')),
 ('7:61', "'qâle qavm leyse _'", 2, 'say 7:61 1-4', "harekesiz 'qâle yâ qavmi leyse bî' (1-4. kelime)", ('dizi 7 61 1 4', 'qâle qavm leyse _', '1-4', 'biçim farkı (dizi 7 61 1 4): basılmamış eş yazım eş')),
 ('7:62', "'allâh mâ lâ 'alime'", 3, 'say 7:62 8-11', "harekesiz 'llâhi mâ lâ ta'lemûn' (8-11. kelime)", ('dizi 7 62 8 11', "allâh mâ lâ 'alime", '8-11', 'biçim farkı (dizi 7 62 8 11): 7:28 yazım eş; 7:33 yazım eş')),
 ('7:62', "'risâle rabb nesahu _'", 3, 'say 7:62 2-5', "harekesiz 'risâlâti rabbî ve ensahu lekum' (2-5. kelime)", ('dizi 7 62 2 5', 'risâle rabb nesahu _', '2-5', 'biçim farkı (dizi 7 62 2 5): basılmamış eş zamir eki; basılmamış eş zamir eki')),
 ('7:62', "'belliğ risâle rabb'", 2, 'say 7:62 1-3', "harekesiz 'ubelliğukum risâlâti rabbî' (1-3. kelime)", ('dizi 7 62 1 3', 'belliğ risâle rabb', '1-3', 'biçim farkı (dizi 7 62 1 3): basılmamış eş yazım eş')),
 ('7:63', "''acibu en câ'e zikr min rabb 'alâ racul min enzere'", 2, 'say 7:63 1-10', "harekesiz 'e-ve-'acibtum en câ'ekum zikrun min rabbikum 'alâ raculin minkum li-yunzirakum' (1-10. kelime)", ('dizi 7 63 1 10', "'acibu en câ'e zikr min rabb 'alâ racul min enzere", '1-10', 'biçim farkı (dizi 7 63 1 10): basılmamış eş yazım eş')),
 ('7:64', "'ellezî kezzebe âye'", 5, 'say 7:64 8-10', "harekesiz 'llezîne kezzebû bi-âyâtinâ' (8-10. kelime); biçim öğesi 'ellezî' öneki (lemma dizisi sûre içi 8, nakarat3 5)", ('dizi 7 64 8 10', 'ellezî kezzebe âye', '8-10', 'biçim farkı (dizi 7 64 8 10): 7:36 önek; 7:40 yazım eş; basılmamış eş yazım eş; basılmamış eş önek; basılmamış eş yazım eş; basılmamış eş yazım eş; basılmamış eş önek; öneksiz eş koşusu (dizi 7 64 8 10): 7:36 → önek kesilmiş sûre içi 3; 7:40 → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 3; basılmamış eş → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 3')),
 ('7:64', "'encâ ellezî ma'a'", 2, 'say 7:64 2-4', "harekesiz 'fe-enceynâhu ve'llezîne me'ahû' (2-4. kelime)", ('dizi 7 64 2 4', "encâ ellezî ma'a", '2-4', 'biçim farkı (dizi 7 64 2 4): basılmamış eş yazım eş')),
]
'''
VF = '''VF_YAZI = {59: {1: "'le-qad'", 6: "'fe-qâle'"}, 60: {6: "'le-nerâke'"}, 61: {4: "'bî'", 6: "'ve lâkinnî'"}, 62: {4: "'ve ensahu'", 5: "'lekum'", 6: "'ve a'lemu'"}, 63: {1: "'e-ve-'acibtum'", 10: "'li-yunzirakum'", 11: "'ve li-tetteqû'", 12: "'ve le'allekum'"}, 64: {1: "'fe-kezzebûhu'", 2: "'fe-enceynâhu'", 3: "'ve'llezîne'", 7: "'ve ağraqna'", 10: "'bi-âyâtinâ'"}}
sys.path.insert(0, '/home/claude/b18/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b18/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2', '# sûre 7 blok 18 (7:59-64) ARIZA oluşturucu — bölüm 7-1'), ('/home/claude/b40/', '/home/claude/b18/'),
     ("es_edat.py', '40'", "es_edat.py', '18'"), ('range(1, 41)', 'range(1, 19)'),
     ("'--plan', '40', '--numarasiz')", "'--plan', '18', '--numarasiz')"),
     ('ariza_6_161_165', 'ariza_7_59_64'), ('bag_6_161_165', 'bag_7_59_64'), ('(161, 165)', '(59, 64)'), ("'161', '165', '40'", "'59', '64', '18'"), ("'161', '165'", "'59', '64'"),
     ("_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}", "_ON = {'7:59', '7:60', '7:61', '7:62', '7:63', '7:64'}"), ('range(161, 166)', 'range(59, 65)'),
     ("x.startswith('6:')", "x.startswith('7:')"), ("== '6:%d' % a_", "== '7:%d' % a_"), ("return '6:%d: %s'", "return '7:%d: %s'"), ("r'\\b6:%d:\\d+'", "r'\\b7:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_6_*.txt')", "glob.glob('/home/claude/yamalar/ariza_7_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_7_b17k.txt'"),
     ("BOL = \"'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'\"", "BOL = \"'Nûh ve kavmi; Hûd ve Âd'\""),
     ("for _n in range(7, 35): _J", "for _n in range(7, 43): _J"), ("B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]", "B33, B34, B35, B36, B37, B38, B39, B40, B41, B42 = [_R['B%d' % _n].splitlines() for _n in range(6, 43)]"),
     ("'B34_HEPSI': (B34[-1] if B34 else '?'),", "'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'B39_HEPSI': (B39[-1] if B39 else '?'), 'B40_HEPSI': (B40[-1] if B40 else '?'), 'B41_HEPSI': (B41[-1] if B41 else '?'), 'B42_HEPSI': (B42[-1] if B42 else '?'),"),
     ("B32, B33, B34): print(", "B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42): print("),
     ("BEK = []", "BEK = list(ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_7_b17.txt', encoding='utf-8').read() + ']'))"),
     ("sûre 6'nın okunmuş bütün ARIZA dosyaları", "sûre 7'nin okunmuş bütün ARIZA dosyaları"),
     ]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
_AN = """ANILIS = "7:59 kök عظم (''azîm' 20. kelime — büyük): tetik listesinde yok; 7:63 kök رجل ('raculin' 8. kelime — adam): tetik listesinde yok"\n"""
out = re.sub(r'ANILIS = ".*"\n', lambda m_: _AN, out)
out = re.sub(r"for nn in \('01', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18'):", out)
for l in out.split('\n'):
    for bad in ('b40', "'40'", "'161'", "'165'", '6_161_165', "'6:", 's6/'):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b18/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
