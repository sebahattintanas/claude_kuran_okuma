# sûre 6 blok 35 ARIZA oluşturucusu — sûre 5 blok 36 üreticisinden; denetim betikleri paralel (kullanıcı uyarısı: ilerleme ağır)
import re
src = open('/home/claude/s5/b36/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("6:161", "'kâne min muşrik'", 2, 'say 6:161 14-16', "harekesiz 'kâne mine'l-muşrikîn' (14-16. kelime)", ('dizi 6 161 14 16', "kâne min muşrik", '14-16', "biçim farkı (dizi 6 161 14 16): 6:14 fiil çekimi")),
 ("6:161", "'ilâ sırât mustaqîm'", 2, 'say 6:161 5-7', "harekesiz 'ilâ sırâtin mustaqîmin' (5-7. kelime)", ('dizi 6 161 5 7', "ilâ sırât mustaqîm", '5-7', "biçim farkı (dizi 6 161 5 7): 6:87 yazım eş")),
 ("6:162", "'allâh rabb 'âlem'", 2, 'say 6:162 7-9', "harekesiz 'lillâhi rabbi'l-'âlemîn' (7-9. kelime)", ('dizi 6 162 7 9', "allâh rabb 'âlem", '7-9', "biçim farkı (dizi 6 162 7 9): 6:45 yazım eş")),
 ("6:164", "'summe ilâ rabb merci' nebbe'e mâ kâne'", 2, 'say 6:164 21-27', "harekesiz 'summe ilâ rabbikum merci'ukum fe-yunebbi'ukum bimâ kuntum' (21-27. kelime)", ('dizi 6 164 21 27', "summe ilâ rabb merci' nebbe'e mâ kâne", '21-27', "biçim farkı (dizi 6 164 21 27): 6:108 fiil çekimi, zamir eki")),
 ("6:164", "'nebbe'e mâ kâne'", 4, 'say 6:164 25-27', "harekesiz 'fe-yunebbi'ukum bimâ kuntum' (25-27. kelime)", ('dizi 6 164 25 27', "nebbe'e mâ kâne", '25-27', "biçim farkı (dizi 6 164 25 27): 6:60 önek; 6:108 fiil çekimi, zamir eki; 6:159 fiil çekimi, zamir eki, önek")),
 ("6:164", "'summe ilâ rabb'", 3, 'say 6:164 21-23', "harekesiz 'summe ilâ rabbikum' (21-23. kelime)", ('dizi 6 164 21 23', "summe ilâ rabb", '21-23', "biçim farkı (dizi 6 164 21 23): 6:38 zamir eki; 6:108 zamir eki")),
 ("6:164", "'qâle ğayr allâh'", 2, 'say 6:164 1-3', "harekesiz 'qul e-ğayra'llâhi' (1-3. kelime)", ('dizi 6 164 1 3', "qâle ğayr allâh", '1-3', "biçim farkı (dizi 6 164 1 3): 6:14 yazım eş")),
 ("6:164", "'rabb kull şey''", 2, 'say 6:164 7-9', "harekesiz 'rabbu kulli şey'' (7-9. kelime)", ('dizi 6 164 7 9', "rabb kull şey'", '7-9', "biçim farkı (dizi 6 164 7 9): 6:80 zamir eki")),
 ("6:165", "'_ ellezî ce'ale'", 2, 'say 6:165 1-3', "harekesiz 've huve'llezî ce'alekum' (1-3. kelime)", ('dizi 6 165 1 3', "_ ellezî ce'ale", '1-3', "biçim farkı (dizi 6 165 1 3): 6:97 zamir eki")),
]
'''

VF = '''VF_YAZI = {161: {13: "'ve mâ'"}, 162: {4: "'ve nusukî'", 5: "'ve mahyâye'", 6: "'ve memâtî'"}, 163: {4: "'ve bi-zâlike'", 6: "'ve ene'"}, 164: {6: "'ve huve'", 10: "'ve lâ'", 16: "'ve lâ'"}, 165: {1: "'ve huve'", 6: "'ve refe'a'", 19: "'ve innehû'"}}
sys.path.insert(0, '/home/claude/b40/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b40/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b40/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
# paralel denetim koşusu
a = out.index("    AYN = (run('/home/claude/sunum/ayn_kontrol.py'"); b = out.index("    REP = {")
PAR = '''    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '161', '165'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '161', '165', '40'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '161', '165', '40'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '161', '165', '40', '--tazelik-yok')}
    for _n in range(7, 35): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '161', '165', '40')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]
'''
out = out[:a] + PAR + out[b:]
R = [("K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k}", "K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k and not (k + ' --medde' in sayim.S2 and sayim.S2[k + ' --medde'][0] != n)}  # sûre 6 bölüm 5 denetimi kuralı 6 (TEKIL_MEDDE)"),
     ('# blok 36 (5:118-120) ARIZA oluşturucu — bölüm 16-2', '# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2'), ('/b36/', '/b40/'),
     ("es_edat.py', '36'", "es_edat.py', '40'"), ('range(1, 37)', 'range(1, 41)'),
     ("'--plan', '36', '--numarasiz')", "'--plan', '40', '--numarasiz')"),
     ('ariza_5_118_120', 'ariza_6_161_165'), ('bag_5_118_120', 'bag_6_161_165'), ('(118, 120)', '(161, 165)'), ("'118', '120', '36'", "'161', '165', '40'"), ("'118', '120'", "'161', '165'"),
     ("_ON = {'5:118', '5:119', '5:120'}", "_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}"), ('range(118, 121)', 'range(161, 166)'),
     ("x.startswith('5:')", "x.startswith('6:')"), ("== '5:%d' % a_", "== '6:%d' % a_"), ("return '5:%d: %s'", "return '6:%d: %s'"), ("r'\\b5:%d:\\d+'", "r'\\b6:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_5_*.txt')", "glob.glob('/home/claude/yamalar/ariza_6_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b36.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt'"),
     ("BOL = \"'İsâ'ya soru; doğruların fayda gördüğü gün'\"", "BOL = \"'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'\""),
     ("'B15_HEPSI': (B15[-1] if B15 else '?'),", "'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'B34_HEPSI': (B34[-1] if B34 else '?'),"),
     ("sûre 5'in okunmuş bütün ARIZA dosyaları", "sûre 6'nın okunmuş bütün ARIZA dosyaları"),
     ("print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)", "print(GLS)\nfor _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34): print([l for l in _x if l.startswith('HATA') or 'hata' in l])"),
     ]
R += [("MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()", "MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']")]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
out = re.sub(r"VF_YAZI_ESKI = \{.*\n", "VF_YAZI_ESKI = {}\n", out)
out = re.sub(r"for nn in \('06', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40'):", out)
for l in out.split('\n'):
    for bad in ('b36', "'36'", "'118'", "'120'", '5_118_120', "'5:"):
        if bad in l: print('KONTROL', bad, l[:160])
_mk = """MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)"""
assert _mk in out
out = out.replace(_mk, _mk + "\nMKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde")
open('/home/claude/b40/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
