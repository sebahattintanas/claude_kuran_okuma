# -*- coding: utf-8 -*-
"""sizinti.py — basılmamış ayet numarası sızıntı taraması. OTURUM DIŞI yardımcı.
Regex (?<![\\d])(\\d{1,3}:\\d{1,3})\\b ile bulunan her ayet numarası basilan.txt'te (bu oturumda Arapçası
basılmış) ya da --ek ile verilen listede (bu turda basılacak ayetler) olmalı; değilse SIZINTI.
Şablon kod yorumlarındaki isabetler okuma metni değildir: tarama metin / kayıt / not dosyalarına uygulanır.
Kullanım: python3 sizinti.py dosya [dosya ...] [--ek S:A S:A-B ...]"""
import sys, re, os

BASILAN = '/home/claude/sunum/basilan.txt'
RX = re.compile(r'(?<![\d])(\d{1,3}:\d{1,3})\b')
args = sys.argv[1:]
ek = set()
if '--ek' in args:
    i = args.index('--ek')
    for x in args[i + 1:]:
        m = re.fullmatch(r'(\d+):(\d+)(?:-(\d+))?', x)
        assert m, x
        for a in range(int(m.group(2)), int(m.group(3) or m.group(2)) + 1):
            ek.add('%s:%d' % (m.group(1), a))
    args = args[:i]
izin = set(ek)
if os.path.exists(BASILAN):
    izin |= {l.strip() for l in open(BASILAN, encoding='utf-8') if l.strip()}
top = 0
for p in args:
    for no, l in enumerate(open(p, encoding='utf-8'), 1):
        for m in RX.finditer(l):
            if m.group(1) not in izin:
                top += 1
                print('SIZINTI %s:%d  %s  …%s…' % (os.path.basename(p), no, m.group(1),
                                                   l[max(0, m.start() - 40):m.end() + 40].strip()))
print('sızıntı: %d (izinli ayet %d)' % (top, len(izin)))
sys.exit(1 if top else 0)
