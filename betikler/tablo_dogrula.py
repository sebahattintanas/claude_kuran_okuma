# -*- coding: utf-8 -*-
"""tablo_dogrula.py — her karışık kök ayrımının dağılımını raporlar."""
import sys, json; sys.path.insert(0,'.')
for m in list(sys.modules):
    if m.startswith('kuran_akis'): del sys.modules[m]
import kuran_akis; kuran_akis._TABLO=None
from kuran_akis import kelime_akisi, kavram
from collections import Counter, defaultdict

def dogrula():
    ak=kelime_akisi()
    tablo=json.load(open('kok_anlam_tablosu.json',encoding='utf-8'))
    print("KÖK AYRIMI DOĞRULAMA (%d kök)\n"%len(tablo))
    for kok in tablo:
        say=Counter()
        for x in ak:
            if x['kok']==kok: say[kavram(kok,x['lem_ham'])]+=1
        cozulen=sum(v for k,v in say.items() if k!=kok)
        toplam=sum(say.values())
        oran=100*cozulen/toplam if toplam else 0
        durum="✓" if oran>90 else ("~" if oran>60 else "✗ eksik")
        print("  %s %-5s → %s  [çözülme %%%.0f]"%(durum,kok,dict(say),oran))

if __name__=='__main__': dogrula()
