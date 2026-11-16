import re
src = open('/home/claude/b16/yap/ariza_yap.py', encoding='utf-8').read().split('\n')
head = '\n'.join(src[:41]); mid1 = '\n'.join(src[41:57]); mid2 = '\n'.join(src[89:132]); tail = '\n'.join(src[184:])
assert src[41].startswith('r5 = []') and src[132].startswith('I = list') and src[184].startswith('def yaz')
head = head[:head.index('R5 = [')].replace('blok 16 (5:45-47)', 'blok 17 (5:48-50)').replace('/b16/', '/b17/')
R5 = r'''R5 = [
 ("5:48", "'ilâ allâh merci' cemî' nebbe'e mâ kâne'", 2, 'say 5:48 43-49', "harekesiz 'ile'llâhi merci'ukum cemî'an fe-yunebbi'ukum bi-mâ kuntum' (43-49. kelime)", None),
 ("5:48", "'musaddiq mâ beyn yed min'", 2, 'say 5:48 5-9', "harekesiz 'musaddiqan li-mâ beyne yedeyhi min' (5-9. kelime)", None),
 ("5:48", "'hakeme beyn mâ enzele allâh'", 2, 'say 5:48 13-17 --on', "önek kesilmiş 'fa'hkum beynehum bi-mâ enzele'llâh' (13-17. kelime)",
  ('dizi 5 48 13 17', "hakeme beyn mâ enzele allâh", '13-17', "önek kesilmiş sayım ('say 5:48 13-17 --on') sûre içi 1, lemma dizisi ('dizi 5 48 13 17') sûre içi 2 (5:48, 5:49) — fark açıklanmadı, tam okuma sonu")),
 ("5:48", "'mâ enzele allâh'", 5, 'say 5:48 15-17', "harekesiz 'bi-mâ enzele'llâh' (15-17. kelime)", None),
 ("5:49", "'hakeme beyn mâ enzele allâh'", 2, 'say 5:49 2-6', "harekesiz 'hkum beynehum bi-mâ enzele'llâh' (2-6. kelime)",
  ('dizi 5 49 2 6', "hakeme beyn mâ enzele allâh", '2-6', "harekesiz sayım ('say 5:49 2-6') sûre içi 1, lemma dizisi ('dizi 5 49 2 6') sûre içi 2 (5:48, 5:49) — fark açıklanmadı, tam okuma sonu")),
 ("5:49", "'in tevellâ 'alime ennemâ'", 2, 'say 5:49 19-22 --on', "önek kesilmiş 'fe-in tevellev fa'lem ennemâ' (19-22. kelime)",
  ('dizi 5 49 19 22', "in tevellâ 'alime ennemâ", '19-22', "önek kesilmiş sayım ('say 5:49 19-22 --on') sûre içi 1, lemma dizisi ('dizi 5 49 19 22') sûre içi 2 — fark açıklanmadı, tam okuma sonu")),
 ("5:49", "'mâ enzele allâh'", 5, 'say 5:49 4-6', "harekesiz 'bi-mâ enzele'llâh' (4-6. kelime)", None),
]'''
VF = '''VF_YAZI = {48: {1: "'ve enzelnâ'", 11: "'ve muheyminen'", 13: "'fa'hkum'", 18: "'ve lâ'", 29: "'ve minhâcâ'", 30: "'ve lev'", 36: "'ve lâkin'", 41: "'fe'stebiqu'", 47: "'fe-yunebbi'ukum'"}, 49: {1: "'ve eni'hkum'", 7: "'ve lâ'", 10: "'ve'hzerhum'", 19: "'fe-in'", 21: "'fa'lem'", 29: "'ve inne'"}, 50: {1: "'e-fe-hukme'", 4: "'ve men'"}}
sys.path.insert(0, '/home/claude/b17/yap')
from seg import meals
MEALS = meals()
'''
mid2 = mid2.replace('/b16/', '/b17/').replace("es_edat.py', '16'", "es_edat.py', '17'").replace('range(1, 17)', 'range(1, 18)').replace("'--plan', '16'", "'--plan', '17'").replace("'45', '47', EMS", "'48', '50', EMS").replace("gloss_tara.py', '45', '47', '16'", "gloss_tara.py', '48', '50', '17'")
tail = tail.replace('(45, 47)', '(48, 50)').replace('ariza_5_45_47', 'ariza_5_48_50').replace("'45', '47', '16'", "'48', '50', '17'").replace("'45', '47')", "'48', '50')")
tail = re.sub(r"for nn in \([^)]*\)", "for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17')", tail)
I = open('/home/claude/b17/yap/I_parca.py', encoding='utf-8').read()
out = head + R5 + '\n' + mid1 + '\n\n' + VF + '\n\n' + mid2 + '\n' + I + '\n\n' + tail
for bad in ('b16', "'16'", '45', '47'):
    for l in out.split('\n'):
        if bad in l and 'nn in' not in l and 'BOL' not in l: print('KONTROL', bad, l[:150])
open('/home/claude/b17/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
