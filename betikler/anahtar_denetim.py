#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
anahtar_denetim.py — ELLE YAZILMIŞ ARAPÇA ANAHTAR DENETİMİ (SALT-OKUR)
======================================================================
Neden: kök tabloları korpustan TÜRETİLDİĞİ için temiz. Bozulma, anahtarın
KLAVYEDEN girildiği yerlerde oluyor — özellikle .py dosyalarına gömülü
sabitlerde. Mevcut denetim (turkce_denetim.py, tablo_dogrula.py) sadece
.json tarıyor ve sadece YENİ üretime bakıyor. Bu betik ikisini de kapatır.

DÖRT TEST
  T1 LATIN     : Arapça dizgi içinde Latin/Kiril karakter (قدr → U+0072)
  T2 ELIF      : bare elif ا (U+0627) ile başlayan kök — korpusta hemzeli أ mı?
  T3 SIRA      : harekesiz eşleşen bir korpus formu VAR ama birebir eşleşmiyor
                 → hareke sırası/varyant farkı. DİKKAT: korpusun ham hâli ZATEN
                 NFC'dir (shadda ccc=33 > damme ccc=31). Sapan taraf elle yazılan
                 anahtardır. Ölçüt "NFC'den sapma" değil "KORPUS FORMUNDAN sapma".
  T4 KORPUS    : anahtar korpusta hiç geçmiyor mu (kök envanteri / PN lemma)

MUAFİYET
  1. Alt çizgi sonrası Latin etiket kasıtlıdır (kavram_sozlugu.json: سمو_tekil).
  2. EDAT/HAM-METİN sabitleri: kök envanterinde aranmayan, ham metinde eşleşen
     parçacıklar (أما/فأما/وأما/كلا/إن ...). Bunlar kök DEĞİL, muaf tutulur.
     Liste aşağıda EDAT_MUAF — genişletilirse GEREKÇESİYLE genişletilsin.

SALT-OKUR: hiçbir dosyayı değiştirmez, sadece rapor üretir.
"""
import json, os, re, sys, unicodedata
from collections import defaultdict

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARAPCA = lambda cp: 0x600 <= cp <= 0x6FF or 0x750 <= cp <= 0x77F

def govde(s):
    """muafiyet: alt çizgiden sonrasını at"""
    return s.split('_')[0]

# ---------- korpus referansı ----------
def korpus_yukle():
    yol = os.path.join(KOK, 'veri', 'morph.txt')
    kokler, pn_lem, lemler = set(), set(), set()
    if not os.path.exists(yol): return kokler, pn_lem, lemler
    for line in open(yol, encoding='utf-8'):
        p = line.rstrip('\n').split('\t')
        if len(p) < 4: continue
        r = re.search(r'ROOT:([^\|]+)', p[3])
        if r: kokler.add(unicodedata.normalize('NFC', r.group(1)))
        l = re.search(r'LEM:([^\|]+)', p[3])
        if l:
            lemler.add(unicodedata.normalize('NFC', l.group(1)))
            if 'PN' in p[3].split('|'):
                pn_lem.add(unicodedata.normalize('NFC', l.group(1)))
    return kokler, pn_lem, lemler

KOKLER, PN_LEM, LEMLER = korpus_yukle()
HARFSIZ = lambda s: re.sub(r'[^\u0621-\u064A]', '', s)

# ham metinde aranan parçacıklar — kök envanterinde OLMAMASI normal
EDAT_MUAF = {'أما','فأما','وأما','كلا','مائة','ين','قرى','مصب','ستو','أدرىك'}
KOK_HARFSIZ = {HARFSIZ(k): k for k in KOKLER}
LEM_HARFSIZ = {HARFSIZ(k): k for k in LEMLER}

def denetle(s):
    g = govde(s)
    ar = [c for c in g if ARAPCA(ord(c))]
    if not ar: return []
    # ELEME 1: düzyazı/yorum — boşluk, parantez ya da Arapça oranı düşük
    if ' ' in g or '(' in g or len(ar) / len(g) < 0.6: return []
    # ELEME 2: tek/iki harf — normalizasyon eşleme tabloları, anahtar değil
    if len(HARFSIZ(g)) < 3: return []
    # ELEME 3: alan öneki (ROOT:, LEM:) — anahtarın kendisi değil
    if ':' in g: g = g.split(':')[-1]
    h = []
    for ch in g:
        cp = ord(ch)
        if ch in '|: -' or ch.isdigit(): continue
        if not ARAPCA(cp):
            h.append('T1 LATIN %r %s' % (ch, hex(cp)))
    n = unicodedata.normalize('NFC', g)
    if n in EDAT_MUAF: return h
    if n and '|' not in n and n not in KOKLER and n not in LEMLER:
        hs = HARFSIZ(n)
        # harekesiz eşleşme var mı → yazım/hemze/hareke hatası
        oneri = KOK_HARFSIZ.get(hs) or LEM_HARFSIZ.get(hs)
        if oneri and oneri != n:
            etiket = 'T3 SIRA/VARYANT' if len(oneri) == len(n) else 'T2 YAZIM'
            h.append('%s → korpustaki hâli: %s' % (etiket, oneri))
        elif not oneri:
            h.append('T4 korpusta HİÇ YOK')
    return h

# ---------- kaynak toplama ----------
def json_anahtarlari(yol):
    try: d = json.load(open(yol, encoding='utf-8'))
    except Exception: return []
    return list(d.keys()) if isinstance(d, dict) else []

def py_sabitleri(yol):
    """.py içindeki tırnak içi Arapça dizgiler"""
    try: src = open(yol, encoding='utf-8').read()
    except Exception: return []
    out = []
    for m in re.finditer(r"['\"]((?:[^'\"\\\n]|\\.){1,40})['\"]", src):
        s = m.group(1)
        if any(ARAPCA(ord(c)) for c in s):
            out.append((s, src[:m.start()].count('\n') + 1))
    return out

rapor = defaultdict(list)
toplam = bozuk = 0
for kokdiz, _, dosyalar in os.walk(KOK):
    if '.git' in kokdiz or '__pycache__' in kokdiz: continue
    for f in dosyalar:
        yol = os.path.join(kokdiz, f)
        rel = os.path.relpath(yol, KOK)
        if f.endswith('.json'):
            for k in json_anahtarlari(yol):
                toplam += 1
                h = denetle(k)
                if h: bozuk += 1; rapor[rel].append((k, None, h))
        elif f.endswith('.py'):
            for s, satir in py_sabitleri(yol):
                toplam += 1
                h = denetle(s)
                if h: bozuk += 1; rapor[rel].append((s, satir, h))

print('korpus: %d kök, %d PN lemma' % (len(KOKLER), len(PN_LEM)))
print('taranan anahtar/sabit: %d   BOZUK: %d\n' % (toplam, bozuk))
for rel in sorted(rapor):
    print('── %s (%d)' % (rel, len(rapor[rel])))
    for k, satir, h in rapor[rel]:
        yer = ('sat.%d ' % satir) if satir else ''
        print('   ✗ %s%-16s %s' % (yer, k, ' | '.join(h)))
print('\n(SALT-OKUR — hiçbir dosya değiştirilmedi.)')
