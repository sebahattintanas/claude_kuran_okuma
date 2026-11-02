# -*- coding: utf-8 -*-
"""aile_kars_2.py — bakara_* ailesini sûre 96 (alak_*) ailesiyle normalleştirilmiş karşılaştırır (oturum dışı)."""
import re, difflib, os
os.chdir('/home/claude/calisma')
H = r'[^\W\d_]'
def norm(t, ad, AD, Ad, no):
    for a, y in ((ad, 'X'), (AD, 'XX'), (Ad, 'Xx')):
        t = re.sub(r'(?<!%s)%s(?!%s)' % (H, a, H), y, t)
    return re.sub(r'(?<!\d)%s(?!\d)' % no, 'S', t)
CIFT = [('kok_ekle_96.py', 'kok_ekle_2.py'), ('uret_blok_96.py', 'uret_blok_2.py'), ('duzeltme_96.py', 'duzeltme_2.py'),
        ('yama_retroaktif_gloss_96.py', 'yama_retroaktif_gloss_2.py'), ('alak_kapanis.py', 'bakara_kapanis.py'),
        ('alak_paket_md.py', 'bakara_paket_md.py'), ('aday_ekle_96_alak.py', 'aday_ekle_2_bakara.py')]
for a, b in CIFT:
    A = open(a, encoding='utf-8').read()
    for x, y in (('alak', 'bakara'), ('ALAK', 'BAKARA'), ('Alak', 'Bakara')):
        A = re.sub(r'(?<!%s)%s(?!%s)' % (H, x, H), y, A)
    A = re.sub(r'(?<!\d)96(?!\d)', '2', A).split('\n')
    B = open(b, encoding='utf-8').read().split('\n')
    d = [l for l in difflib.unified_diff(A, B, lineterm='', n=0) if l[:1] in '+-' and l[:3] not in ('+++', '---')]
    print('=== %s / %s: %d fark satırı' % (a, b, len(d)))
    for l in d: print('   ', l[:170])
