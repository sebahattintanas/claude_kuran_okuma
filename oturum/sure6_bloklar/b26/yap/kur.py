# sûre 6 blok 1 ARIZA oluşturucusu — sûre 5 blok 36 üreticisinden; denetim betikleri paralel (kullanıcı uyarısı: ilerleme ağır)
import re
src = open('/home/claude/s5/b36/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("6:111", "'illâ en şâ'e'", 2, 'say 6:111 16-18', "harekesiz 'illâ en yeşâ'e' (16-18. kelime)", None),
 ("6:112", "'mâ fe'ale yezere mâ iftarâ'", 2, 'say 6:112 19-23', "harekesiz 'mâ fe'alûhu fe-zerhum ve mâ yefterûn' (19-23. kelime)", None),
 ("6:113", "'ellezî lâ âmene âxir'", 2, 'say 6:113 4-7', "harekesiz 'llezîne lâ yu'minûne bi'l-âxira' (4-7. kelime)", ('dizi 6 113 4 7', 'ellezî lâ âmene âxir', '4-7', 'biçim farkı (dizi 6 113 4 7): basılmamış eş önek')),
 ("6:113", "'ellezî lâ âmene'", 3, 'say 6:113 4-6', "harekesiz 'llezîne lâ yu'minûne' (4-6. kelime)", ('dizi 6 113 4 6', 'ellezî lâ âmene', '4-6', 'biçim farkı (dizi 6 113 4 6): basılmamış eş yazım eş; basılmamış eş önek')),
]
'''

VF = '''VF_YAZI = {109: {1: "'ve aqsemû'", 15: "'ve mâ'"}, 110: {1: "'ve nuqallibu'", 3: "'ve ebsârahum'", 10: "'ve nezeruhum'"}, 111: {1: "'ve lev'", 6: "'ve kellemehumu'", 8: "'ve haşernâ'", 20: "'ve lâkinne'"}, 112: {1: "'ve kezâlike'", 8: "'ve'l-cinni'", 16: "'ve lev'", 22: "'ve mâ'"}, 113: {1: "'ve li-tasğâ'", 8: "'ve li-yerdavhu'", 9: "'ve li-yeqterifû'"}}
sys.path.insert(0, '/home/claude/b26/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b26/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b26/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
# paralel denetim koşusu
a = out.index("    AYN = (run('/home/claude/sunum/ayn_kontrol.py'"); b = out.index("    REP = {")
PAR = '''    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '109', '113'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '109', '113', '26'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '109', '113', '26'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '109', '113', '26', '--tazelik-yok')}
    for _n in range(7, 29): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '109', '113', '26')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28 = [_R['B%d' % _n].splitlines() for _n in range(6, 29)]
'''
out = out[:a] + PAR + out[b:]
R = [("K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k}", "K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k and not (k + ' --medde' in sayim.S2 and sayim.S2[k + ' --medde'][0] != n)}  # sûre 6 bölüm 5 denetimi kuralı 6 (TEKIL_MEDDE)"),
     ('# blok 36 (5:118-120) ARIZA oluşturucu — bölüm 16-2', '# sûre 6 blok 26 (6:109-113) ARIZA oluşturucu — bölüm 13-2'), ('/b36/', '/b26/'),
     ("es_edat.py', '36'", "es_edat.py', '26'"), ('range(1, 37)', 'range(1, 27)'),
     ("'--plan', '36', '--numarasiz')", "'--plan', '26', '--numarasiz')"),
     ('ariza_5_118_120', 'ariza_6_109_113'), ('bag_5_118_120', 'bag_6_109_113'), ('(118, 120)', '(109, 113)'), ("'118', '120', '36'", "'109', '113', '26'"), ("'118', '120'", "'109', '113'"),
     ("_ON = {'5:118', '5:119', '5:120'}", "_ON = {'6:109', '6:110', '6:111', '6:112', '6:113'}"), ('range(118, 121)', 'range(109, 114)'),
     ("x.startswith('5:')", "x.startswith('6:')"), ("== '5:%d' % a_", "== '6:%d' % a_"), ("return '5:%d: %s'", "return '6:%d: %s'"), ("r'\\b5:%d:\\d+'", "r'\\b6:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_5_*.txt')", "glob.glob('/home/claude/yamalar/ariza_6_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b36.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_6_b24k.txt'"),
     ("BOL = \"'İsâ'ya soru; doğruların fayda gördüğü gün'\"", "BOL = \"'Basiretler; yeminleri ve şeytanlar'\""),
     ("'B15_HEPSI': (B15[-1] if B15 else '?'),", "'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'),"),
     ("sûre 5'in okunmuş bütün ARIZA dosyaları", "sûre 6'nın okunmuş bütün ARIZA dosyaları"),
     ("print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)", "print(GLS)\nfor _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28): print([l for l in _x if l.startswith('HATA') or 'hata' in l])"),
     ]
R += [("MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()", "MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']")]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
out = re.sub(r"VF_YAZI_ESKI = \{.*\n", "VF_YAZI_ESKI = {}\n", out)
out = re.sub(r"for nn in \('06', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'):", out)
for l in out.split('\n'):
    for bad in ('b36', "'36'", "'118'", "'120'", '5_118_120', "'5:"):
        if bad in l: print('KONTROL', bad, l[:160])
_mk = """MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)"""
assert _mk in out
out = out.replace(_mk, _mk + "\nMKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde")
open('/home/claude/b26/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
