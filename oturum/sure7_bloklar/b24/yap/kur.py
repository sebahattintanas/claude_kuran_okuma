# sûre 7 blok 24 ARIZA oluşturucusu — sûre 6 blok 40 üreticisinden (s6/b40/yap/ariza_yap.py); bölüm açılışı, BEK bekleyen_ariza_7_b23.txt'ten
import re
src = open('/home/claude/s6/b40/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('\nI = [\n') + 1; k1 = src.index('\ndef yaz(II):')
R5 = '''R5 = [
 ('7:85', "'qâle qavm 'abede allâh mâ _ min ilâh ğayr qad câ'e beyyine min rabb'", 2, 'say 7:85 5-18', "harekesiz 'qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû qad câ'etkum beyyinetun min rabbikum' (5-18. kelime)", ('dizi 7 85 5 18', "qâle qavm 'abede allâh mâ _ min ilâh ğayr qad câ'e beyyine min rabb", '5-18', "biçim farkı (dizi 7 85 5 18): 7:73 yazım eş")),
 ('7:85', "'qâle qavm 'abede allâh mâ _ min ilâh ğayr'", 4, 'say 7:85 5-13', "harekesiz 'qâle yâ qavmi u'budu'llâhe mâ lekum min ilâhin ğayruhû' (5-13. kelime)", ('dizi 7 85 5 13', "qâle qavm 'abede allâh mâ _ min ilâh ğayr", '5-13', "biçim farkı (dizi 7 85 5 13): 7:59 önek; 7:65 yazım eş; 7:73 yazım eş; öneksiz eş koşusu (dizi 7 85 5 13): 7:59 → önek kesilmiş sûre içi 1; 7:65 → önek kesilmiş sûre içi 4; 7:73 → önek kesilmiş sûre içi 4")),
 ('7:85', "'lâ efsedu fî ard ba'd islâh'", 2, 'say 7:85 26-31', "harekesiz 've lâ tufsidû fi'l-ardi ba'de islâhihâ' (26-31. kelime)", ('dizi 7 85 26 31', "lâ efsedu fî ard ba'd islâh", '26-31', "biçim farkı (dizi 7 85 26 31): 7:56 yazım eş")),
 ('7:85', "'qad câ'e beyyine min rabb'", 3, 'say 7:85 14-18', "harekesiz 'qad câ'etkum beyyinetun min rabbikum' (14-18. kelime)", ('dizi 7 85 14 18', "qad câ'e beyyine min rabb", '14-18', "biçim farkı (dizi 7 85 14 18): 7:73 yazım eş; basılmamış eş fiil çekimi, i'râb, zamir eki, önek; öneksiz eş koşusu (dizi 7 85 14 18): 7:73 → önek kesilmiş sûre içi 2; basılmamış eş → önek kesilmiş sûre içi 1")),
 ('7:85', "'efsedu fî ard'", 3, 'say 7:85 27-29', "harekesiz 'tufsidû fi'l-ardi' (27-29. kelime)", ('dizi 7 85 27 29', "efsedu fî ard", '27-29', "biçim farkı (dizi 7 85 27 29): 7:56 yazım eş; basılmamış eş fiil çekimi, zamir eki, önek; öneksiz eş koşusu (dizi 7 85 27 29): 7:56 → önek kesilmiş sûre içi 2; basılmamış eş → önek kesilmiş sûre içi 1")),
 ('7:85', "'_ in kâne'", 2, 'say 7:85 34-36', "harekesiz 'lekum in kuntum' (34-36. kelime); biçim öğesi 'kum' zamir eki (lemma dizisi sûre içi 3, nakarat3 2)", ('dizi 7 85 34 36', "_ in kâne", '34-36', "biçim farkı (dizi 7 85 34 36): basılmamış eş fiil çekimi, zamir eki, önek; basılmamış eş yazım eş; öneksiz eş koşusu (dizi 7 85 34 36): basılmamış eş → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 2")),
 ('7:86', "'nazara keyfe kâne 'âqibe mufsid'", 2, 'say 7:86 20-24', "harekesiz 've'nzurû keyfe kâne 'âqibetu'l-mufsidîn' (20-24. kelime)", ('dizi 7 86 20 24', "nazara keyfe kâne 'âqibe mufsid", '20-24', "biçim farkı (dizi 7 86 20 24): basılmamış eş fiil çekimi, zamir eki, önek; öneksiz eş koşusu (dizi 7 86 20 24): basılmamış eş → önek kesilmiş sûre içi 1")),
 ('7:86', "'nazara keyfe kâne 'âqibe'", 3, 'say 7:86 20-23', "harekesiz 've'nzurû keyfe kâne 'âqibetu' (20-23. kelime)", ('dizi 7 86 20 23', "nazara keyfe kâne 'âqibe", '20-23', "biçim farkı (dizi 7 86 20 23): 7:84 fiil çekimi, zamir eki, önek; basılmamış eş fiil çekimi, zamir eki, önek; öneksiz eş koşusu (dizi 7 86 20 23): 7:84 → önek kesilmiş sûre içi 2; basılmamış eş → önek kesilmiş sûre içi 2")),
 ('7:86', "'sadde 'an sebîl allâh'", 2, 'say 7:86 6-9', "harekesiz 've tesuddûne 'an sebîli'llâhi' (6-9. kelime)", ('dizi 7 86 6 9', "sadde 'an sebîl allâh", '6-9', "biçim farkı (dizi 7 86 6 9): 7:45 fiil çekimi, zamir eki, önek; öneksiz eş koşusu (dizi 7 86 6 9): 7:45 → önek kesilmiş sûre içi 1")),
]
'''
VF = '''VF_YAZI = {85: {1: "'ve ilâ'", 6: "'yâ qavmi'", 10: "'lekum'", 19: "'fe-evfu'", 21: "'ve'l-mîzâne'", 22: "'ve lâ'", 26: "'ve lâ'", 34: "'lekum'"}, 86: {1: "'ve lâ'", 3: "'bi-kulli'", 6: "'ve tesuddûne'", 12: "'bihî'", 13: "'ve tebğûnehâ'", 15: "'ve'zkurû'", 19: "'fe-kesserakum'", 20: "'ve'nzurû'"}, 87: {1: "'ve in'", 6: "'bi'llezî'", 8: "'bihî'", 9: "'ve tâ'ifetun'", 12: "'fe'sbirû'", 17: "'ve huve'"}}
sys.path.insert(0, '/home/claude/b24/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b24/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2', '# sûre 7 blok 24 (7:85-87) ARIZA oluşturucu — bölüm 9-1'), ('/home/claude/b40/', '/home/claude/b24/'),
     ("es_edat.py', '40'", "es_edat.py', '24'"), ('range(1, 41)', 'range(1, 25)'),
     ("'--plan', '40', '--numarasiz')", "'--plan', '24', '--numarasiz')"),
     ('ariza_6_161_165', 'ariza_7_85_87'), ('bag_6_161_165', 'bag_7_85_87'), ('(161, 165)', '(85, 87)'), ("'161', '165', '40'", "'85', '87', '24'"), ("'161', '165'", "'85', '87'"),
     ("_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}", "_ON = {'7:85', '7:86', '7:87'}"), ('range(161, 166)', 'range(85, 88)'),
     ("x.startswith('6:')", "x.startswith('7:')"), ("== '6:%d' % a_", "== '7:%d' % a_"), ("return '6:%d: %s'", "return '7:%d: %s'"), ("r'\\b6:%d:\\d+'", "r'\\b7:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_6_*.txt')", "glob.glob('/home/claude/yamalar/ariza_7_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_7_b23k.txt'"),
     ("BOL = \"'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'\"", "BOL = \"'Şuayb ve Medyen'\""),
     ("for _n in range(7, 35): _J", "for _n in range(7, 45): _J"), ("B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]", "B33, B34, B35, B36, B37, B38, B39, B40, B41, B42, B43, B44 = [_R['B%d' % _n].splitlines() for _n in range(6, 45)]"),
     ("'B34_HEPSI': (B34[-1] if B34 else '?'),", "'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'B39_HEPSI': (B39[-1] if B39 else '?'), 'B40_HEPSI': (B40[-1] if B40 else '?'), 'B41_HEPSI': (B41[-1] if B41 else '?'), 'B42_HEPSI': (B42[-1] if B42 else '?'), 'B43_HEPSI': (B43[-1] if B43 else '?'), 'B44_HEPSI': (B44[-1] if B44 else '?'),"),
     ("B32, B33, B34): print(", "B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42, B43, B44): print("),
     ("BEK = []", "BEK = list(ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_7_b23.txt', encoding='utf-8').read() + ']'))"),
     ("sûre 6'nın okunmuş bütün ARIZA dosyaları", "sûre 7'nin okunmuş bütün ARIZA dosyaları"),
     ]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
_AN = """ANILIS = "7:85 kök بعد ('ba'de' 30. kelime — morph T, zaman); 7:86 kök صدد ('tesuddûne' 6. kelime — alıkoyma); 7:86 'iz' (16. kelime — morph T, zaman): tetik listesinde yok"\n"""
out = re.sub(r'ANILIS = ".*"\n', lambda m_: _AN, out)
out = re.sub(r"for nn in \('01', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24'):", out)
for l in out.split('\n'):
    for bad in ('b40', "'40'", "'161'", "'165'", '6_161_165', "'6:", 's6/'):
        if bad in l: print('KONTROL', bad, l[:160])
open('/home/claude/b24/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
