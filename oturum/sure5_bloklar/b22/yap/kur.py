import re
src = open('/home/claude/b21/yap/ariza_yap.py', encoding='utf-8').read()
i0 = src.index('R5 = ['); i1 = src.index('r5 = []')
j0 = src.index('VF_YAZI = {'); j1 = src.index('MEALS = meals()') + len('MEALS = meals()')
k0 = src.index('_U = set()'); k1 = src.index('\ndef yaz(II):')
R5 = r'''R5 = [
 ("5:67", "'mâ enzele ilâ min rabb'", 3, 'say 5:67 4-8', "harekesiz 'mâ unzile ileyke min rabbik' (4-8. kelime; biçim öğesi 'ileyke' — ölçüm kalıbında 2MS biçim öğesi; ◇ lemma dizisi 'dizi 5 67 4 8' sûre içi 4, 'ileyhim' / 'ileykum' eşleri dahil)", None),
 ("5:67", "'inne allâh lâ hedâ qavm'", 2, 'say 5:67 19-23', "harekesiz 'inna'llâhe lâ yehdi'l-qavm' (19-23. kelime)", None),
 ("5:67", "'allâh lâ hedâ qavm'", 3, 'say 5:67 20-23', "harekesiz 'llâhe lâ yehdi'l-qavm' (20-23. kelime)", ('dizi 5 67 20 23', "allâh lâ hedâ qavm", '20-23', "biçim farkı (dizi 5 67 20 23): 5:51 yazım eş; basılmamış eş i'râb, önek")),
 ("5:67", "'inne allâh lâ'", 3, 'say 5:67 19-21', "harekesiz 'inna'llâhe lâ' (19-21. kelime)", None),
 ("5:68", "'zâde kesîr min mâ enzele ilâ min rabb tuğyân kufr'", 2, 'say 5:68 16-25 --on', "önek kesilmiş 've le-yezîdenne kesîran minhum mâ unzile ileyke min rabbike tuğyânen ve kufran' (16-25. kelime)", None),
 ("5:68", "'mâ enzele ilâ min rabb'", 3, 'say 5:68 19-23', "harekesiz 'mâ unzile ileyke min rabbik' (19-23. kelime; biçim öğesi 'ileyke' — ölçüm kalıbında 2MS biçim öğesi; ◇ lemma dizisi 'dizi 5 68 19 23' sûre içi 4, 'ileyhim' / 'ileykum' eşleri dahil)", None),
 ("5:68", "'eqâme tevrâ incîl mâ enzele'", 2, 'say 5:68 8-12', "harekesiz 'tuqîmu't-tevrâte ve'l-incîle ve mâ unzile' (8-12. kelime)", ('dizi 5 68 8 12', "eqâme tevrâ incîl mâ enzele", '8-12', "biçim farkı (dizi 5 68 8 12): 5:66 fiil çekimi, zamir eki")),
 ("5:68", "'fe-lâ te'se 'alâ qavm'", 2, 'say 5:68 26-29 --on', "önek kesilmiş 'fe-lâ te'se 'ale'l-qavm' (26-29. kelime)", None),
 ("5:68", "'qâle ehl kitâb'", 3, 'say 5:68 1-3', "harekesiz 'qul yâ ehle'l-kitâb' (1-3. kelime)", None),
 ("5:69", "'ellezî âmene ellezî'", 2, 'say 5:69 2-4', "harekesiz 'llezîne âmenû ve'llezîne' (2-4. kelime; biçim öğesi 've' öneki — ölçüm kalıbı 'ellezî' biçimlerini önekle ayırıyor; ◇ lemma dizisi 'dizi 5 69 2 4' sûre içi 3)", ('dizi 5 69 2 4', "ellezî âmene ellezî", '2-4', "biçim farkı (dizi 5 69 2 4): 5:55 önek; basılmamış eş önek — ölçüm kalıbı 've' önekli 'ellezî' ile öneksiz biçimi ayırmıyor; öneksiz eş koşusu (dizi 5 69 2 4): 5:55 → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 1 — kalan fark tam okuma sonu")),
 ("5:70", "'mîsâq buneyy isrâ'îl'", 2, 'say 5:70 3-5', "harekesiz 'mîsâqa benî isrâ'îl' (3-5. kelime)", None),
]
'''
VF = '''VF_YAZI = {67: {9: "'ve in'", 12: "'fe-mâ'", 15: "'ve'llâhu'"}, 68: {10: "'ve'l-incîle'", 11: "'ve mâ'", 16: "'ve le-yezîdenne'", 25: "'ve kufran'", 26: "'fe-lâ'"}, 69: {4: "'ve'llezîne'", 6: "'ve's-sâbi'ûne'", 7: "'ve'n-nasârâ'", 11: "'ve'l-yevmi'", 13: "'ve 'amile'", 15: "'fe-lâ'", 18: "'ve lâ'"}, 70: {6: "'ve erselnâ'", 18: "'ve ferîqan'"}}
sys.path.insert(0, '/home/claude/b22/yap')
from seg import meals
MEALS = meals()'''
I = open('/home/claude/b22/yap/I_parca.py', encoding='utf-8').read()
out = src[:i0] + R5 + src[i1:j0] + VF + src[j1:k0] + I + src[k1:]
R = [('/b21/', '/b22/'), ("es_edat.py', '21'", "es_edat.py', '22'"), ('range(1, 22)', 'range(1, 23)'), ("'--plan', '21'", "'--plan', '22'"), ("'64', '66', EMS", "'67', '70', EMS"),
     ('ariza_5_64_66', 'ariza_5_67_70'), ('(64, 66)', '(67, 70)'), ("'64', '66', '21'", "'67', '70', '22'"), ("'64', '66')", "'67', '70')"),
     ("BOL = \"'Kitap ehlinin tutumu; bağlı el sözü; Tevrat ve İncil'i ayakta tutma'\"", "BOL = \"'Tebliğ emri; İsrâiloğullarının misakı; Mesih ve teslis'\""),
     ("BEK = []", "BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_5_b21.txt', encoding='utf-8').read() + ']')")]
R.append(("    for k, v in REP.items(): I_cur = [x.replace(k, v) for x in I_cur]", "    for k, v in REP.items(): I_cur = I_cur[:len(BEK)] + [x.replace(k, v) for x in I_cur[len(BEK):]]  # bölüm 9 kuralı 9: taşınan denetim maddelerine yer tutucu değişimi uygulanmaz"))
for a, b in R:
    assert a in out, a
    out = out.replace(a, b)
out = re.sub(r"for nn in \([^)]*\)", "for nn in ('06', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22')", out)
for l in out.split('\n'):
    for bad in ('b21', "'21'", "'64'", "'66'"):
        if bad in l and 'nn in' not in l: print('KONTROL', bad, l[:160])
open('/home/claude/b22/yap/ariza_yap.py', 'w', encoding='utf-8').write(out)
