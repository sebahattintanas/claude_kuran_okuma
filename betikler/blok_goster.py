# -*- coding: utf-8 -*-
"""Blok okumasını kayıtlı biçimde üretir: ### S:N · Arapça · **meal** · › ölçüm (defterden) · ◇ mercek · ▽ dikey (JSON'dan).
Kullanım: python3 blok_goster.py S A1 A2 metin_modulu"""
import sys, json, importlib
S,A1,A2,MOD=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
import olcum_bicim; T=importlib.import_module(MOD)
veri=json.load(open('kuran_veri.json',encoding='utf-8'))
AR={(s['no'],a['no']):a['ar'] for s in veri['sureler'] for a in s['ayetler']}
DIK=json.load(open(f'blok_dikey_{S}_{A1}_{A2}.json',encoding='utf-8'))
for n in range(A1,A2+1):
    ar=AR[(S,n)]
    # besmele kirliliği: 112 ayette metne gömülü; kelime sayısıyla ayıklanır (Arapça sabit yok)
    if n==1 and S not in (1,9):
        _t=ar.split()
        if len(_t)==5: ar=_t[-1]
    print(f'### {S}:{n}\n')
    print(ar+'\n')
    print(f'**{T.MEAL[n]}**\n')
    print('› '+olcum_bicim.olcum(S,n)+'\n')
    print(T.M[n]+'\n')
    d=DIK.get(f'{S}:{n}','').strip()
    print('▽ '+(d.replace('\n','\n▽ ') if d else '(bu ayette dikey satır yok)')+'\n')
