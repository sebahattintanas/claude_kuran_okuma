# -*- coding: utf-8 -*-
"""oturum_xy.py — MERCEK [x/y] ↔ ÖLÇÜM KARŞILAŞTIRMASI (salt-okur).
Kullanım: python3 oturum_xy.py S A B <metin_modülü>
Mercek metnindeki her 'KÖK [x/y]' ve 'KÖK ikilemesi [x,y/z]' anması, o ayetin ölçüm satırındaki
kök alanıyla karşılaştırılır (olcum_bicim.olcum). Ölçümde olmayan kök için yazılmış [x/y] de uyuşmazdır.
Not: '[x/y]' YALNIZ o ayetin kendi sayımı için yazılır; başka ayete ait sayı yazılacaksa '[x/y]' biçimi kullanılmaz."""
import sys, re, importlib
import olcum_bicim

S, A1, A2, MOD = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
T = importlib.import_module(MOD)
KOK = '[\u0621-\u064A]{2,4}'
OLC = re.compile(r'(%s) \*\(.*?\)\* \[([\d,]+/\d+)\]' % KOK)
MER = re.compile(r'(%s)(?: ikilemesi)? \[([\d,]+/\d+)\]' % KOK)
top = uy = 0
for n in range(A1, A2 + 1):
    o = olcum_bicim.olcum(S, n)
    ol = dict(OLC.findall(o[o.index('kökler'):] if 'kökler' in o else ''))
    for r, xy in MER.findall(T.M[n]):
        top += 1
        if ol.get(r) != xy:
            uy += 1
            print('UYUŞMAZ %d:%d %s mercek [%s] · ölçüm %s' % (S, n, r, xy, '[%s]' % ol[r] if r in ol else 'YOK'))
print('[x/y]: %d sayım, %d uyuşmaz' % (top, uy))
