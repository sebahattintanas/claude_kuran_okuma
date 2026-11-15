# bölüm 1 (sûre 5) denetimi kuralı 2: harekesiz / önek kesilmiş kalıplarda medde yapıntısı ('ءا' / ٓ) taraması — kullanıcı: python3 sunum/medde.py bNN/say2.txt
import sys, re
for b in open(sys.argv[1], encoding='utf-8').read().split('### ')[1:]:
    L = b.strip().splitlines()
    if L[0].startswith('say') and len(L) > 1 and ('ءا' in L[1] or 'ٓ' in L[1]):
        n = re.match(r'(\d+) ', L[-1].strip()).group(1)
        print('MEDDE', L[0], '|', L[1], '|', n, 'ayet')
