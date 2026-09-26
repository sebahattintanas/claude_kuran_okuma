# -*- coding: utf-8 -*-
"""Blok okumasını kayıtlı biçimde üretir: ### S:N · Arapça · **meal** · › ölçüm (defterden) · ◇ mercek · ▽ dikey (JSON'dan).
Kullanım: python3 blok_goster.py S A1 A2 metin_modulu"""
import sys, json, importlib
S,A1,A2,MOD=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),sys.argv[4]
import olcum_bicim; T=importlib.import_module(MOD)
veri=json.load(open('kuran_veri.json',encoding='utf-8'))
AR={(s['no'],a['no']):a['ar'] for s in veri['sureler'] for a in s['ayetler']}
import re as _re, unicodedata as _ud
def _isk(w):
    w=_re.sub(r'[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]','',_ud.normalize('NFC',w))
    return w.replace('\u0671','\u0627').replace('\ufeff','')
BESMELE=[_isk(w) for w in AR[(1,1)].split()[:4]]
DIK=json.load(open(f'blok_dikey_{S}_{A1}_{A2}.json',encoding='utf-8'))
for n in range(A1,A2+1):
    ar=AR[(S,n)]
    # besmele kirliliği: 112 ayette metne gömülü; kelime sayısıyla ayıklanır (Arapça sabit yok)
    if n==1 and S not in (1,9):
        # besmele korpustan türetilir (1:1'in ilk dört kelimesi) — Arapça sabit yok.
        # Eski kural (len==5) yalnız tek kelimelik açılışları ayıklıyordu; 33:1'de besmele kalıyordu.
        _t=ar.split()
        if [_isk(w) for w in _t[:4]]==BESMELE: ar=' '.join(_t[4:])
    print(f'### {S}:{n}\n')
    print(ar+'\n')
    print(f'**{T.MEAL[n]}**\n')
    print('› '+olcum_bicim.olcum(S,n)+'\n')
    print(T.M[n]+'\n')
    d=DIK.get(f'{S}:{n}','').strip()
    print('▽ '+(d.replace('\n','\n▽ ') if d else '(bu ayette dikey satır yok)')+'\n')
