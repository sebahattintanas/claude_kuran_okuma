# sûre 6 blok 1 ARIZA oluşturucusu — sûre 5 blok 36 üreticisinden; denetim betikleri paralel (kullanıcı uyarısı: ilerleme ağır)
import re
src = open('/home/claude/s5/b36/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("6:106", "'rabb lâ ilâh illâ _'", 2, 'say 6:106 6-10', "harekesiz 'rabbike lâ ilâhe illâ huve' (6-10. kelime)", ('dizi 6 106 6 10', 'rabb lâ ilâh illâ _', '6-10', "biçim farkı (dizi 6 106 6 10): 6:102 i'râb, zamir eki")),
 ("6:107", "'lev şâ'e allâh mâ'", 2, 'say 6:107 1-4', "harekesiz 've lev şâ'e'llâhu mâ' (1-4. kelime); biçim öğesi 'lev' öneki (lemma dizisi sûre içi 3, nakarat3 2)", ('dizi 6 107 1 4', "lev şâ'e allâh mâ", '1-4', 'biçim farkı (dizi 6 107 1 4): basılmamış eş yazım eş; basılmamış eş önek; öneksiz eş koşusu (dizi 6 107 1 4): basılmamış eş → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 2')),
 ("6:107", "'şâ'e allâh mâ eşrake'", 2, 'say 6:107 2-5', "harekesiz 'şâ'e'llâhu mâ eşrakû' (2-5. kelime)", ('dizi 6 107 2 5', "şâ'e allâh mâ eşrake", '2-5', 'biçim farkı (dizi 6 107 2 5): basılmamış eş fiil çekimi, zamir eki')),
 ("6:107", "'şâ'e allâh mâ'", 3, 'say 6:107 2-4', "harekesiz 'şâ'e'llâhu mâ' (2-4. kelime)", ('dizi 6 107 2 4', "şâ'e allâh mâ", '2-4', 'biçim farkı (dizi 6 107 2 4): basılmamış eş yazım eş; basılmamış eş yazım eş')),
 ("6:108", "'summe ilâ rabb merci' nebbe'e mâ kâne'", 2, 'say 6:108 18-24', "harekesiz 'summe ilâ rabbihim merci'uhum fe-yunebbi'uhum bi-mâ kânû' (18-24. kelime)", ('dizi 6 108 18 24', "summe ilâ rabb merci' nebbe'e mâ kâne", '18-24', 'biçim farkı (dizi 6 108 18 24): basılmamış eş fiil çekimi, zamir eki')),
 ("6:108", "'ellezî de'â min dûn allâh'", 2, 'say 6:108 3-7', "harekesiz 'llezîne yed'ûne min dûni'llâh' (3-7. kelime)", ('dizi 6 108 3 7', "ellezî de'â min dûn allâh", '3-7', 'biçim farkı (dizi 6 108 3 7): 6:56 fiil çekimi, zamir eki')),
 ("6:108", "'de'â min dûn allâh'", 3, 'say 6:108 4-7', "harekesiz 'yed'ûne min dûni'llâh' (4-7. kelime)", ('dizi 6 108 4 7', "de'â min dûn allâh", '4-7', 'biçim farkı (dizi 6 108 4 7): 6:56 fiil çekimi, zamir eki; 6:71 fiil çekimi, zamir eki, önek')),
 ("6:108", "'nebbe'e mâ kâne 'amile'", 2, 'say 6:108 22-25', "harekesiz 'fe-yunebbi'uhum bi-mâ kânû ya'melûn' (22-25. kelime)", ('dizi 6 108 22 25', "nebbe'e mâ kâne 'amile", '22-25', 'biçim farkı (dizi 6 108 22 25): 6:60 fiil çekimi, zamir eki, önek')),
 ("6:108", "'min dûn allâh'", 4, 'say 6:108 5-7', "harekesiz 'min dûni'llâh' (5-7. kelime)", None),
 ("6:108", "'nebbe'e mâ kâne'", 4, 'say 6:108 22-24', "harekesiz 'fe-yunebbi'uhum bi-mâ kânû' (22-24. kelime)", ('dizi 6 108 22 24', "nebbe'e mâ kâne", '22-24', 'biçim farkı (dizi 6 108 22 24): 6:60 fiil çekimi, zamir eki, önek; basılmamış eş önek; basılmamış eş fiil çekimi, zamir eki')),
 ("6:108", "'summe ilâ rabb'", 3, 'say 6:108 18-20', "harekesiz 'summe ilâ rabbihim' (18-20. kelime)", ('dizi 6 108 18 20', 'summe ilâ rabb', '18-20', 'biçim farkı (dizi 6 108 18 20): 6:38 yazım eş; basılmamış eş zamir eki')),
 ("6:108", "'bi-mâ kâne 'amile'", 3, 'say 6:108 23-25', "harekesiz 'bi-mâ kânû ya'melûn' (23-25. kelime); biçim öğesi 'kâne' çekimi (lemma dizisi sûre içi 6, nakarat3 3)", ('dizi 6 108 23 25', "mâ kâne 'amile", '23-25', 'biçim farkı (dizi 6 108 23 25): 6:43 önek; 6:60 fiil çekimi, zamir eki; 6:88 önek; basılmamış eş önek; basılmamış eş yazım eş; öneksiz eş koşusu (dizi 6 108 23 25): 6:43 → önek kesilmiş sûre içi 5; 6:60 → önek kesilmiş sûre içi 1; 6:88 → önek kesilmiş sûre içi 5; basılmamış eş → önek kesilmiş sûre içi 5; basılmamış eş → önek kesilmiş sûre içi 2')),
]
'''

VF = '''VF_YAZI = {104: {9: "'ve men'", 12: "'ve mâ'"}, 105: {1: "'ve kezâlike'", 4: "'ve li-yeqûlû'", 6: "'ve li-nubeyyinehû'"}, 106: {11: "'ve a'rid'"}, 107: {1: "'ve lev'", 6: "'ve mâ'", 10: "'ve mâ'"}, 108: {1: "'ve lâ'"}}
sys.path.insert(0, '/home/claude/b25/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b25/yap/I_head.py', encoding='utf-8').read() + open('/home/claude/b25/yap/I_body.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
# paralel denetim koşusu
a = out.index("    AYN = (run('/home/claude/sunum/ayn_kontrol.py'"); b = out.index("    REP = {")
PAR = '''    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '104', '108'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '104', '108', '25'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '104', '108', '25'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '104', '108', '25', '--tazelik-yok')}
    for _n in range(7, 29): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '104', '108', '25')
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
     ('# blok 36 (5:118-120) ARIZA oluşturucu — bölüm 16-2', '# sûre 6 blok 25 (6:104-108) ARIZA oluşturucu — bölüm 13-1'), ('/b36/', '/b25/'),
     ("es_edat.py', '36'", "es_edat.py', '25'"), ('range(1, 37)', 'range(1, 26)'),
     ("'--plan', '36', '--numarasiz')", "'--plan', '25', '--numarasiz')"),
     ('ariza_5_118_120', 'ariza_6_104_108'), ('bag_5_118_120', 'bag_6_104_108'), ('(118, 120)', '(104, 108)'), ("'118', '120', '36'", "'104', '108', '25'"), ("'118', '120'", "'104', '108'"),
     ("_ON = {'5:118', '5:119', '5:120'}", "_ON = {'6:104', '6:105', '6:106', '6:107', '6:108'}"), ('range(118, 121)', 'range(104, 109)'),
     ("x.startswith('5:')", "x.startswith('6:')"), ("== '5:%d' % a_", "== '6:%d' % a_"), ("return '5:%d: %s'", "return '6:%d: %s'"), ("r'\\b5:%d:\\d+'", "r'\\b6:%d:\\d+'"),
     ("glob.glob('/home/claude/yamalar/ariza_5_*.txt')", "glob.glob('/home/claude/yamalar/ariza_6_*.txt')"),
     ("GERI = open('/home/claude/yamalar/geriye_donuk_5_b36.txt'", "GERI = open('/home/claude/yamalar/geriye_donuk_6_b24k.txt'"),
     ("BOL = \"'İsâ'ya soru; doğruların fayda gördüğü gün'\"", "BOL = \"'Basiretler; yeminleri ve şeytanlar'\""),
     ("'B15_HEPSI': (B15[-1] if B15 else '?'),", "'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'),"),
     ("sûre 5'in okunmuş bütün ARIZA dosyaları", "sûre 6'nın okunmuş bütün ARIZA dosyaları"),
     ("print(GLS); print(KUR); print(B5); print(B6); print(B7); print(B8)", "print(GLS)\nfor _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28): print([l for l in _x if l.startswith('HATA') or 'hata' in l])"),
     ]
R += [("BEK = []", "BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b24.txt', encoding='utf-8').read() + ']')")]
R += [("MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines()", "MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']")]
for x, y in R:
    assert x in out, x
    out = out.replace(x, y)
out = re.sub(r"VF_YAZI_ESKI = \{.*\n", "VF_YAZI_ESKI = {}\n", out)
out = re.sub(r"for nn in \('06', [^)]*\):", "for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25'):", out)
for l in out.split('\n'):
    for bad in ('b36', "'36'", "'118'", "'120'", '5_118_120', "'5:"):
        if bad in l: print('KONTROL', bad, l[:160])
_mk = """MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)"""
assert _mk in out
out = out.replace(_mk, _mk + "\nMKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde")
open('/home/claude/b25/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
