# -*- coding: utf-8 -*-
"""esitle.py — calisma/ (düz) → repo/ (ağaç). Yalnız DEĞİŞMİŞ ya da YENİ dosyalar kopyalanır;
repo'ya doğrudan yazılan dosyalar (okuma_metni, mercek_kayit, aday_bulgular, okuma_baglantilari)
calisma'daki bayat kopyalarla ezilmez (değişmedikleri için atlanır). Üretilen büyük dosyalar hariç."""
import os, filecmp, shutil
K, C, R = '/home/claude/k', '/home/claude/calisma', '/home/claude/repo'
HARIC = {'ayet_iskelet.json', 'ngram_indeks.json'}
yer = {}
for d in ('betikler', 'tablolar', 'veri', 'ciktilar', 'bulgular', 'betikler/dikey'):
    for f in os.listdir(os.path.join(K, d)):
        if os.path.isfile(os.path.join(K, d, f)): yer.setdefault(f, d)
kop = []
for f in sorted(os.listdir(C)):
    p = os.path.join(C, f)
    if not os.path.isfile(p) or f in HARIC or f.endswith('.pyc'): continue
    if f in yer:
        if filecmp.cmp(p, os.path.join(K, yer[f], f), shallow=False): continue
        d = yer[f]
    elif f.endswith('.py'): d = 'betikler'
    elif f.startswith('blok_dikey_') or f.startswith('dikey_'): d = 'ciktilar'
    elif f.endswith('.json'): d = 'tablolar'
    else: continue
    hedef = os.path.join(R, d, f)
    if os.path.exists(hedef) and filecmp.cmp(p, hedef, shallow=False): continue
    shutil.copy2(p, hedef); kop.append('%s/%s' % (d, f))
print('eşitlenen:', len(kop)); [print('  ', x) for x in kop]
