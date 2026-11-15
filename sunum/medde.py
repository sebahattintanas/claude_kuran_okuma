# bölüm 1-2 (sûre 5) denetimi kuralı 2: harekesiz / önek kesilmiş kalıplarda medde yapıntısı ('ءا' / ٓ) taraması
# kullanım: python3 sunum/medde.py bNN/say.txt [--komut]  — --komut: her meddeli kalıp için meddesiz yeniden sayım satırı ('run say … --medde') basar
import sys, re
K = '--komut' in sys.argv
for b in open(sys.argv[1], encoding='utf-8').read().split('### ')[1:]:
    L = b.strip().splitlines()
    if L[0].startswith('say') and '--medde' not in L[0] and len(L) > 1 and ('ءا' in L[1] or 'ٓ' in L[1]):
        n = re.match(r'(\d+) ', L[-1].strip()).group(1)
        print(('run %s --medde' % L[0]) if K else ('MEDDE %s | %s | %s ayet' % (L[0], L[1], n)))
