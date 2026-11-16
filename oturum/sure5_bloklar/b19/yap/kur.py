import re
src = open('/home/claude/b18/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:55", "'qâme salât etâ zekât'", 2, 'say 5:55 8-11', "harekesiz 'yuqîmûne's-salâte ve yu'tûne'z-zekâ' (8-11. kelime)",
  ('dizi 5 55 8 11', "qâme salât etâ zekât", '8-11', "harekesiz sayım ('say 5:55 8-11') sûre içi 1, lemma dizisi ('dizi 5 55 8 11') sûre içi 2 (5:12, 5:55) — şahıs ve zaman farkı: 5:12 PERF 2MP ('eqamtumu', 'âteytumu') / 5:55 IMPF 3MP ('yuqîmûne', 'yu'tûne')")),
 ("5:55", "'allâh rasûl ellezî âmene'", 2, 'say 5:55 3-6', "harekesiz 'llâhu ve rasûluhû ve'llezîne âmenu' (3-6. kelime)", None),
 ("5:56", "'allâh rasûl ellezî âmene'", 2, 'say 5:56 3-6', "harekesiz 'llâhe ve rasûlehû ve'llezîne âmenû' (3-6. kelime)", None),
 ("5:57", "'min ellezî etâ kitâb min qabl'", 2, 'say 5:57 11-16', "harekesiz 'mine'llezîne ûtu'l-kitâbe min qablikum' (11-16. kelime)", None),
 ("5:57", "'eyy ellezî âmene lâ ittexaze'", 2, 'say 5:57 1-5', "harekesiz 'yâ eyyuhe'llezîne âmenû lâ tettexizu' (1-5. kelime)", None),
 ("5:57", "'itteqâ allâh in kâne mu'min'", 2, 'say 5:57 19-23 --on', "önek kesilmiş 've'ttequ'llâhe in kuntum mu'minîn' (19-23. kelime)",
  ('dizi 5 57 19 23', "itteqâ allâh in kâne mu'min", '19-23', "önek kesilmiş sayım ('say 5:57 19-23 --on') sûre içi 1, lemma dizisi ('dizi 5 57 19 23') sûre içi 2; eş henüz okunmamış — çekim / yazım farkı okunduğunda yazılır, tam okuma sonu")),
 ("5:57", "'eyy ellezî âmene lâ'", 6, 'say 5:57 1-4', "harekesiz 'yâ eyyuhe'llezîne âmenû lâ' (1-4. kelime)", None),
 ("5:57", "'eyy ellezî âmene'", 16, 'say 5:57 1-3', "harekesiz 'yâ eyyuhe'llezîne âmenû' (1-3. kelime)", None),
 ("5:57", "'itteqâ allâh in'", 6, 'say 5:57 19-21 --on', "önek kesilmiş 've'ttequ'llâhe in' (19-21. kelime)",
  ('dizi 5 57 19 21', "itteqâ allâh in", '19-21', "önek kesilmiş sayım ('say 5:57 19-21 --on') sûre içi 5, lemma dizisi ('dizi 5 57 19 21') sûre içi 2 — lemma dizisi 'in' lemmasını 'inne' / 'enne'den ayırıyor, ölçüm 'ان' belirteci birleştiriyor; kalan fark açıklanmadı, tam okuma sonu")),
 ("5:57", "'in kâne mu'min'", 3, 'say 5:57 21-23', "harekesiz 'in kuntum mu'minîn' (21-23. kelime)", None),
]
'''
VF = '''VF_YAZI = {55: {4: "'ve rasûluhû'", 5: "'ve'llezîne'", 10: "'ve yu'tûne'", 12: "'ve hum'"}, 56: {1: "'ve men'", 4: "'ve rasûlehû'", 5: "'ve'llezîne'", 7: "'fe-inne'"}, 57: {10: "'ve le'iben'", 17: "'ve'l-kuffâra'", 19: "'ve'ttequ'"}, 58: {1: "'ve izâ'", 7: "'ve le'iben'"}}
sys.path.insert(0, '/home/claude/b19/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b19/yap/I_parca.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('blok 18 (5:51-54)', 'blok 19 (5:55-58)'), ('/b18/', '/b19/'),
     ("es_edat.py', '18'", "es_edat.py', '19'"), ('range(1, 19)', 'range(1, 20)'), ("'--plan', '18'", "'--plan', '19'"), ("'51', '54', EMS", "'55', '58', EMS"),
     ("gloss_tara.py', '51', '54', '18'", "gloss_tara.py', '55', '58', '19'"), ('(51, 54)', '(55, 58)'), ('ariza_5_51_54', 'ariza_5_55_58'),
     ("'51', '54', '18'", "'55', '58', '19'"), ("'51', '54')", "'55', '58')"),
     ("BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b17.txt', encoding='utf-8').read() + ']')", "BEK = []")]
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
out = re.sub(r"for nn in \([^)]*\)", "for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19')", out)
for l in out.split('\n'):
    for bad in ('b18', "'18'", '51', '54'):
        if bad in l and 'nn in' not in l and '5:51' not in l and '5:54' not in l and 'geriye_donuk' not in l: print('KONTROL', bad, l[:140])
open('/home/claude/b19/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
