# sûre 6 blok 35 ARIZA oluşturucusu — sûre 5 blok 36 üreticisinden; denetim betikleri paralel (kullanıcı uyarısı: ilerleme ağır)
import re
src = open('/home/claude/s5/b36/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("6:153", "'zâ vassâ _ le'alle'", 3, 'say 6:153 13-16', "harekesiz 'zâlikum vassâkum bihî le'allekum' (13-16. kelime)", None),
 ("6:155", "'zâ kitâb enzele mubârak'", 2, 'say 6:155 1-4', "harekesiz 've hâzâ kitâbun enzelnâhu mubârakun' (1-4. kelime)", None),
 ("6:157", "''azâb mâ kâne'", 3, 'say 6:157 32-34', "harekesiz 'l-'azâbi bimâ kânû' (32-34. kelime)", ('dizi 6 157 32 34', "'azâb mâ kâne", '32-34', "biçim farkı (dizi 6 157 32 34): 6:30 fiil çekimi, zamir eki; 6:49 yazım eş")),
 ("6:157", "'beyyine min rabb'", 2, 'say 6:157 13-15', "harekesiz 'beyyinetun min rabbikum' (13-15. kelime)", ('dizi 6 157 13 15', "beyyine min rabb", '13-15', "biçim farkı (dizi 6 157 13 15): 6:57 zamir eki")),
 ("6:157", "'fe-men ezlem mimmen'", 2, 'say 6:157 18-20', "harekesiz 'fe-men ezlemu mimmen' (18-20. kelime)", None),
]
'''

VF = '''VF_YAZI = {153: {1: "'ve enne'", 6: "'ve lâ'"}, 154: {9: "'ve tafsîlen'", 12: "'ve huden'", 13: "'ve rahmeten'"}, 155: {1: "'ve hâzâ'", 6: "'ve'ttaqû'"}, 156: {10: "'ve in'"}, 157: {16: "'ve huden'", 17: "'ve rahmeh'", 24: "'ve sadefe'"}}
sys.path.insert(0, '/home/claude/b38/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b38/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b38/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
# paralel denetim koşusu
a = out.index("    AYN = (run('/home/claude/sunum/ayn_kontrol.py'"); b = out.index("    REP = {")
PAR = '''    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '153', '157'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '153', '157', '38'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '153', '157', '38'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '153', '157', '38', '--tazelik-yok')}
    for _n in range(7, 34): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '153', '157', '38')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33 = [_R['B%d' % _n].splitlines() for _n in range(6, 34)]
'''
out = out[:a] + PAR + out[b:]
R = [("K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k}", "K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k and not (k + ' --medde' in sayim.S2 and sayim.S2[k + ' --medde'][0] != n)}  # sûre 6 bölüm 5 denetimi kuralı 6 (TEKIL_MEDDE)"),
     ('# blok 36 (5:118-120) ARIZA oluşturucu — bölüm 16-2', '# sûre 6 blok 38 (6:153-157) ARIZA oluşturucu — bölüm 18-2'), ('/b36/', '/b38/'),
     ("es_edat.py', '36'", "es_edat.py', '38'"), ('range(1, 37)', 'range(1, 39)'),
     ("'--plan', '36', '--numarasiz')", "'--plan', '38', '--numarasiz')"),
     ('ariza_5_118_120', 'ariza_6_153_157'), ('bag_5_118_120', 'bag_6_153_157'), ('(118, 120)', '(153, 157)'), ("'118', '120', '36'", "'153', '157', '38'"), ("'118', '120'", "'153', '157'"),
     ("_ON = {'5:118', '5:119', '5:120'}", "_ON = {'6:153', '6:154', '6:155', '6:156', '6:157'}"), ('range(118, 121)', 'range(153, 158)'),
     ("x.startswith('5:')", "x.startswith('6:')"), ("== '5:%d' % a_", "== '6:%d' % a_"), ("return '5:%d: %s'", "return '6:%d: %s'"), ("r'\\b5:%d:\\d+'", "r'\\b6:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_5_*.txt')", "glob.glob('/home/claude/yamalar/ariza_6_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b36.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_6_b36k.txt'"),
     ("BOL = \"'İsâ'ya soru; doğruların fayda gördüğü gün'\"", "BOL = \"'Gelin okuyayım; dosdoğru yol; Mûsâ'ya Kitap'\""),
     ("'B15_HEPSI': (B15[-1] if B15 else '?'),", "'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'),"),
     ("sûre 5'in okunmuş bütün ARIZA dosyaları", "sûre 6'nın okunmuş bütün ARIZA dosyaları"),
     ("print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)", "print(GLS)\nfor _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33): print([l for l in _x if l.startswith('HATA') or 'hata' in l])"),
     ]
R += [("MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()", "MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']")]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
out = re.sub(r"VF_YAZI_ESKI = \{.*\n", "VF_YAZI_ESKI = {}\n", out)
out = re.sub(r"for nn in \('06', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38'):", out)
for l in out.split('\n'):
    for bad in ('b36', "'36'", "'118'", "'120'", '5_118_120', "'5:"):
        if bad in l: print('KONTROL', bad, l[:160])
_mk = """MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)"""
assert _mk in out
out = out.replace(_mk, _mk + "\nMKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde")
open('/home/claude/b38/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
