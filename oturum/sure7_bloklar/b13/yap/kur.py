# sûre 7 blok 13 ARIZA oluşturucusu — sûre 6 blok 40 üreticisinden (s6/b40/yap/ariza_yap.py); bölüm açılışı, BEK bekleyen_ariza_7_b02.txt'ten
import re
src = open('/home/claude/s6/b40/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('\nI = [\n') + 1; k1 = src.index('\ndef yaz(II):')
R5 = '''R5 = [
 ("7:44", "'nâdâ ashâb cenne'", 2, 'say 7:44 1-3', "harekesiz 've nâdâ ashâbu'l-cenneti' (1-3. kelime)", ('dizi 7 44 1 3', "nâdâ ashâb cenne", '1-3', "biçim farkı (dizi 7 44 1 3): 7:46 fiil çekimi, zamir eki")),
 ("7:44", "'rabb haqq hel'", 2, 'say 7:44 11-13', "harekesiz 'rabbunâ haqqan fe-hel' (11-13. kelime)", ('dizi 7 44 11 13', "rabb haqq hel", '11-13', "biçim farkı (dizi 7 44 11 13): basılmamış eş i'râb, önek")),
 ("7:45", "'sadde 'an sebîl allâh'", 2, 'say 7:45 2-5', "harekesiz 'yasuddûne 'an sebîli'llâhi' (2-5. kelime)", ('dizi 7 45 2 5', "sadde 'an sebîl allâh", '2-5', "biçim farkı (dizi 7 45 2 5): basılmamış eş fiil çekimi, zamir eki, önek")),
 ("7:46", "'nâdâ ashâb cenne'", 2, 'say 7:46 9-11', "harekesiz 've nâdev ashâbe'l-cenneti' (9-11. kelime)", ('dizi 7 46 9 11', "nâdâ ashâb cenne", '9-11', "biçim farkı (dizi 7 46 9 11): 7:44 fiil çekimi, zamir eki")),
 ("7:46", "'a'râf ricâl 'arafe'", 2, 'say 7:46 4-6', "harekesiz 'l-a'râfi ricâlun ya'rifûne' (4-6. kelime)", ('dizi 7 46 4 6', "a'râf ricâl 'arafe", '4-6', "biçim farkı (dizi 7 46 4 6): basılmamış eş elif yazımı, zamir eki")),
 ("7:46", "'ashâb cenne en'", 2, 'say 7:46 10-12', "harekesiz 'ashâbe'l-cenneti en' (10-12. kelime)", ('dizi 7 46 10 12', "ashâb cenne en", '10-12', "biçim farkı (dizi 7 46 10 12): basılmamış eş yazım eş")),
 ("7:47", "'lâ ce'ale ma'a qavm zâlim'", 2, 'say 7:47 9-13', "harekesiz 'lâ tec'alnâ ma'a'l-qavmi'z-zâlimîn' (9-13. kelime)", ('dizi 7 47 9 13', "lâ ce'ale ma'a qavm zâlim", '9-13', "biçim farkı (dizi 7 47 9 13): basılmamış eş zamir eki, önek")),
]
'''
VF = '''VF_YAZI = {44: {1: "'ve nâdâ'", 13: "'fe-hel'", 21: "'fe-ezzene'"}, 45: {6: "'ve yebğûnehâ'", 8: "'ve hum'"}, 46: {1: "'ve beynehumâ'", 3: "'ve 'ale'", 9: "'ve nâdev'", 17: "'ve hum'"}, 47: {1: "'ve izâ'"}}
sys.path.insert(0, '/home/claude/b13/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b13/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2', '# sûre 7 blok 13 (7:44-47) ARIZA oluşturucu — bölüm 5-2'), ('/home/claude/b40/', '/home/claude/b13/'),
     ("es_edat.py', '40'", "es_edat.py', '13'"), ('range(1, 41)', 'range(1, 14)'),
     ("'--plan', '40', '--numarasiz')", "'--plan', '13', '--numarasiz')"),
     ('ariza_6_161_165', 'ariza_7_44_47'), ('bag_6_161_165', 'bag_7_44_47'), ('(161, 165)', '(44, 47)'), ("'161', '165', '40'", "'44', '47', '13'"), ("'161', '165'", "'44', '47'"),
     ("_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}", "_ON = {'7:44', '7:45', '7:46', '7:47'}"), ('range(161, 166)', 'range(44, 48)'),
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
_AN = """ANILIS = "7:44 kök أذن ('fe-ezzene' 21. kelime — duyur-): tetik listesinde yok; 7:44 kök أذن ('mu'ezzinun' 22. kelime — duyurucu): tetik listesinde yok; 7:45 kök صدد ('yasuddûne' 2. kelime — alıkoy-): tetik listesinde yok; 7:45 kök أخر ('bi'l-âxirati' 9. kelime — âhiret): tetik listesinde yok; 7:46 kök رجل ('ricâlun' 5. kelime — adam): tetik listesinde yok; 7:47 'izâ' (1. kelime — morph T, zaman)"\n"""
out = re.sub(r'ANILIS = ".*"\n', lambda m_: _AN, out)
out = re.sub(r"for nn in \('01', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'):", out)
for l in out.split('\n'):
    for bad in ('b40', "'40'", "'161'", "'165'", '6_161_165', "'6:", 's6/'):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b13/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
