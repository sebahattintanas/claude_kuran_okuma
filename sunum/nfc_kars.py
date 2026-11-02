# -*- coding: utf-8 -*-
"""nfc_kars.py — iki dosyayı NFC altında satır satır karşılaştırır (difflib). OTURUM DIŞI yardımcı.
Kullanım: python3 nfc_kars.py betik_ciktisi.txt gonderilecek.txt  → "NFC fark satırı: N" (N=0 olmadan gönderilmez)."""
import sys, difflib, unicodedata as ud

def oku(p):
    t = ud.normalize('NFC', open(p, encoding='utf-8').read())
    return [l.rstrip() for l in t.strip('\n').split('\n')]

a, b = oku(sys.argv[1]), oku(sys.argv[2])
fark = [l for l in difflib.unified_diff(a, b, lineterm='', n=0)
        if (l.startswith('+') or l.startswith('-')) and not l.startswith(('+++', '---'))]
for l in fark[:20]:
    print(l[:200])
print('NFC fark satırı: %d' % len(fark))
sys.exit(1 if fark else 0)
