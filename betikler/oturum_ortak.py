# -*- coding: utf-8 -*-
"""oturum_ortak.py — oturum yardımcılarının ortak katmanı (SALT-OKUR; hiçbir kayda yazmaz).
2026-10-12: oturum_say/lem/tetik/xy önceki oturumlarda yerel kalmış, depoya girmemişti; sûre 43
oturumunda yeniden yazıldı ve bu kez depoya konuyor. Arapça sabit YOK: kalıplar ayet metninden,
lemmalar morph.txt'ten (token sayısıyla) seçilir; tetik kökleri ONKAYIT_mercekler.md'deki kök anmalarıdır.
Okundu kuralı: ilerleme['tam'] sûreleri + 2:1-20 + okuma_metni'nde kaydı olan kısmi sûre ayetleri.
Sûre 3-8 sıkıştırılmış okundu → 'henüz okunmadı' sayılır (TAM listesinde değiller)."""
import json, re, unicodedata as ud
from collections import defaultdict, OrderedDict

N = lambda s: ud.normalize('NFC', s)
_H = re.compile('[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u0640]')
AR_HARF = re.compile('[\u0621-\u064A]')


def isk(w):
    """harekesiz iskelet: hareke/işaret/tatvil düşer, elif-vasla → elif, elif-medde → hemze+elif"""
    w = _H.sub('', N(w)).replace('\u0671', '\u0627').replace('﻿', '')
    return w.replace('\u0622', '\u0621\u0627')


_veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = OrderedDict(((s['no'], a['no']), a['ar']) for s in _veri['sureler'] for a in s['ayetler'])
_BES = [isk(w) for w in AR[(1, 1)].split()[:4]]


def kelimeler(s, a):
    """ayet kelimeleri (iskelet), durak/secde işaretleri atılır; 1:1 dışında baştaki besmele ayıklanır"""
    t = [isk(w) for w in AR[(s, a)].split()]
    t = [w for w in t if AR_HARF.search(w)]
    if a == 1 and s not in (1, 9) and t[:4] == _BES:
        t = t[4:]
    return t


# morfoloji: (s,a,w) -> [(etiket, özellikler)]
MORPH = defaultdict(list)
for _l in open('morph.txt', encoding='utf-8'):
    _p = _l.rstrip('\n').split('\t')
    if len(_p) < 4 or _p[0].count(':') != 3:
        continue
    _s, _a, _w, _ = map(int, _p[0].split(':'))
    MORPH[(_s, _a, _w)].append((_p[2], [N(x) for x in _p[3].split('|')]))


def ozellik(f, on):
    for x in f:
        if x.startswith(on):
            return x[len(on):]
    return None


_OM = json.load(open('/home/claude/repo/notlar/okuma_metni.json', encoding='utf-8'))
_TAM = set(_OM['ilerleme']['tam'])
_KISMI = {(int(k.split(':')[0]), int(k.split(':')[1])) for s, d in _OM.items() if s.isdigit() and int(s) not in _TAM and s != '2'
          for k in d if not k.startswith('_') and re.fullmatch(r'\d+:\d+', k)}


def okundu(s, a):
    return s in _TAM or (s == 2 and a <= 20) or (s, a) in _KISMI


def durum(s, a):
    return '%d:%d%s' % (s, a, '' if okundu(s, a) else '†')
