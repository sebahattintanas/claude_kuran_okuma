# -*- coding: utf-8 -*-
"""satir_aynen_tam.py — örüntü tabanlı TAM 'satır aynen' taraması (bölüm 13 denetiminden; satir_aynen_kontrol.py bir maddedeki
yalnız son alıntıyı yakalıyordu). Ölçüm alanı kalıplarına uyan HER tırnak içi alıntıyı ölçümde ('**'sız) bayt eşitliğiyle arar.
Kullanım: python3 satir_aynen_tam.py <olcum.txt> <dosya> [<dosya> ...]"""
import re, sys
olc = open(sys.argv[1], encoding='utf-8').read().replace('**', '')
pats = [r"'(fâsıla [^']*? sınıfı)'", r"'(simetri \[[^\]]*\])'", r"'(İÇ düğüm \d+)'", r"'(EDİLGEN [^']*?)'",
        r"'(sayı işareti [^']*?)'", r"'(biçim [A-Z]+)'", r"'(\d+:\d+ oran [^']*?)'", r"'(adlı [^']*?\))'",
        r"'(\S+ \d+\. sırada, \w+ konum, \w+)'"]
bad = 0
for f in sys.argv[2:]:
    s = open(f, encoding='utf-8').read(); n = 0
    for p in pats:
        for q in re.findall(p, s):
            n += 1
            if q not in olc:
                bad += 1; print('YOK', f.split('/')[-1], repr(q))
    print(f.split('/')[-1], 'alıntı', n)
print('uyuşmayan:', bad)
