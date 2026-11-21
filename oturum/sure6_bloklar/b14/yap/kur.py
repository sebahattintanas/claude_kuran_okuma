# sûre 6 blok 1 ARIZA oluşturucusu — sûre 5 blok 36 üreticisinden; denetim betikleri paralel (kullanıcı uyarısı: ilerleme ağır)
import re
src = open('/home/claude/s5/b36/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("6:60", "'summe nebbe'e mâ kâne'", 2, 'say 6:60 18-21', "harekesiz 'summe yunebbi'ukum bimâ kuntum' (18-21. kelime)", ('dizi 6 60 18 21', "summe nebbe'e mâ kâne", '18-21', "biçim farkı (dizi 6 60 18 21): basılmamış eş fiil çekimi, zamir eki")),
 ("6:60", "'nebbe'e mâ kâne 'amile'", 2, 'say 6:60 19-22 --on', "önek kesilmiş 'yunebbi'ukum bimâ kuntum ta'melûn' (19-22. kelime)", ('dizi 6 60 19 22', "nebbe'e mâ kâne 'amile", '19-22', "biçim farkı (dizi 6 60 19 22): basılmamış eş fiil çekimi, zamir eki, önek")),
 ("6:60", "'nebbe'e mâ kâne'", 4, 'say 6:60 19-21 --on', "önek kesilmiş 'yunebbi'ukum bimâ kuntum' (19-21. kelime)", ('dizi 6 60 19 21', "nebbe'e mâ kâne", '19-21', "biçim farkı (dizi 6 60 19 21): basılmamış eş fiil çekimi, zamir eki, önek; basılmamış eş fiil çekimi, zamir eki; basılmamış eş önek")),
 ("6:60", "'bi-mâ kâne 'amile'", 3, 'say 6:60 20-22', "harekesiz 'bimâ kuntum ta'melûn' (20-22. kelime)", ('dizi 6 60 20 22', "bi-mâ kâne 'amile", '20-22', "biçim farkı (dizi 6 60 20 22): 6:43 fiil çekimi, zamir eki, önek; basılmamış eş fiil çekimi, zamir eki, önek; basılmamış eş fiil çekimi, zamir eki; basılmamış eş fiil çekimi, zamir eki, önek; basılmamış eş fiil çekimi, zamir eki; biçim öğesi ''amile' çekimi (lemma dizisi sûre içi 6, nakarat3 3); öneksiz eş koşusu (dizi 6 60 20 22): 6:43 → önek kesilmiş sûre içi 5; basılmamış eş → önek kesilmiş sûre içi 5; basılmamış eş → önek kesilmiş sûre içi 2; basılmamış eş → önek kesilmiş sûre içi 5; basılmamış eş → önek kesilmiş sûre içi 2")),
 ("6:61", "'_ qâhir fevq 'abd'", 2, 'say 6:61 1-4', "harekesiz 've huve'l-qâhiru fevqa 'ibâdih' (1-4. kelime)", None),
 ("6:61", "'hattâ izâ câ'e'", 3, 'say 6:61 8-10', "harekesiz 'hattâ izâ câ'e' (8-10. kelime)", ('dizi 6 61 8 10', "hattâ izâ câ'e", '8-10', "biçim farkı (dizi 6 61 8 10): 6:25 fiil çekimi, zamir eki; 6:31 fiil çekimi, zamir eki")),
]
'''
VF = '''VF_YAZI = {59: {1: "'ve 'indehû'", 8: "'ve ya'lemu'", 12: "'ve'l-bahr'", 13: "'ve mâ'", 19: "'ve lâ'", 24: "'ve lâ'", 26: "'ve lâ'"}, 60: {1: "'ve huve'", 5: "'ve ya'lemu'"}, 61: {1: "'ve huve'", 5: "'ve yursilu'", 15: "'ve hum'"}}
sys.path.insert(0, '/home/claude/b14/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b14/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b14/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
# paralel denetim koşusu
a = out.index("    AYN = (run('/home/claude/sunum/ayn_kontrol.py'"); b = out.index("    REP = {")
PAR = '''    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '59', '61'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '59', '61', '14'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '59', '61', '14'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '59', '61', '14', '--tazelik-yok')}
    for _n in range(7, 23): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '59', '61', '14')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22 = [_R['B%d' % _n].splitlines() for _n in range(6, 23)]
'''
out = out[:a] + PAR + out[b:]
R = [("K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k}", "K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k and not (k + ' --medde' in sayim.S2 and sayim.S2[k + ' --medde'][0] != n)}  # sûre 6 bölüm 5 denetimi kuralı 6 (TEKIL_MEDDE)"),
     ('# blok 36 (5:118-120) ARIZA oluşturucu — bölüm 16-2', '# sûre 6 blok 14 (6:59-61) ARIZA oluşturucu — bölüm 7-1'), ('/b36/', '/b14/'),
     ("es_edat.py', '36'", "es_edat.py', '14'"), ('range(1, 37)', 'range(1, 15)'),
     ("'--plan', '36', '--numarasiz')", "'--plan', '14', '--numarasiz')"),
     ('ariza_5_118_120', 'ariza_6_59_61'), ('bag_5_118_120', 'bag_6_59_61'), ('(118, 120)', '(59, 61)'), ("'118', '120', '36'", "'59', '61', '14'"), ("'118', '120'", "'59', '61'"),
     ("_ON = {'5:118', '5:119', '5:120'}", "_ON = {'6:59', '6:60', '6:61'}"), ('range(118, 121)', 'range(59, 62)'),
     ("x.startswith('5:')", "x.startswith('6:')"), ("== '5:%d' % a_", "== '6:%d' % a_"), ("return '5:%d: %s'", "return '6:%d: %s'"), ("r'\\b5:%d:\\d+'", "r'\\b6:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_5_*.txt')", "glob.glob('/home/claude/yamalar/ariza_6_*.txt')"),
     ("BEK = []", "BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b13.txt', encoding='utf-8').read() + ']')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b36.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_6_b13.txt'"),
     ("BOL = \"'İsâ'ya soru; doğruların fayda gördüğü gün'\"", "BOL = \"'Gaybın anahtarları; karanlıklardan kurtaran'\""),
     ("'B15_HEPSI': (B15[-1] if B15 else '?'),", "'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'),"),
     ("sûre 5'in okunmuş bütün ARIZA dosyaları", "sûre 6'nın okunmuş bütün ARIZA dosyaları"),
     ("print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)", "print(GLS)\nfor _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22): print([l for l in _x if l.startswith('HATA') or 'hata' in l])"),
     ]
R += [("MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()", "MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']")]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
out = re.sub(r"VF_YAZI_ESKI = \{.*\n", "VF_YAZI_ESKI = {}\n", out)
out = re.sub(r"for nn in \('06', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'):", out)
for l in out.split('\n'):
    for bad in ('b36', "'36'", "'118'", "'120'", '5_118_120', "'5:"):
        if bad in l: print('KONTROL', bad, l[:160])
_mk = """MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)"""
assert _mk in out
out = out.replace(_mk, _mk + "\nMKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde")
open('/home/claude/b14/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
