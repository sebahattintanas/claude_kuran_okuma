# -*- coding: utf-8 -*-
"""blok_3_10_14.py — 3:10-14 — İnkâr edenlere malın ve evladın yararsızlığı; Firavun ailesinin gidişi; karşılaşan iki topluluk ibreti; dünya süsü ve Allah katındaki dönüş

uret_blok_3.py tarafından ÜRETİLDİ — elle düzenleme. Ölçüm (›) defterden (olcum_bicim),
dikey (▽) blok_dikey JSON'undan, bilanço blok_bilanco'dan; yalnız meal ve mercek (◇) elle.
"""
import json, re, unicodedata
import olcum_bicim, gloss_gecis, blok_bilanco
from al_imran_metin_1 import MEAL, M
from al_imran_kayit import CIPA, ARIZA

S, A1, A2 = 3, 10, 14
REPO = '/home/claude/repo/notlar/'
DIK = json.load(open('blok_dikey_%d_%d_%d.json' % (S, A1, A2), encoding='utf-8'))
ESMA = json.load(open('esma_kayit.json', encoding='utf-8'))
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {(s['no'], a['no']): a['ar'] for s in veri['sureler'] for a in s['ayetler']}
_H = re.compile('[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]')
_isk = lambda w: _H.sub('', unicodedata.normalize('NFC', w)).replace('\u0671', '\u0627').replace('\ufeff', '')
BESMELE = [_isk(w) for w in AR[(1, 1)].split()[:4]]
if A1 == 1 and S not in (1, 9):
    _t = AR[(S, 1)].split()
    if [_isk(w) for w in _t[:4]] == BESMELE:
        AR[(S, 1)] = ' '.join(_t[4:])
    assert [_isk(w) for w in AR[(S, 1)].split()[:4]] != BESMELE, 'besmele ayıklanmadı — DUR'
for n in range(A1, A2 + 1):
    assert n in MEAL and n in M, 'meal/mercek eksik: %d:%d — DUR' % (S, n)

p = REPO + 'okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
OM.setdefault(str(S), {})
OM_ONCE = set(OM[str(S)])
for n in range(A1, A2 + 1):
    k = '%d:%d' % (S, n)
    e = ESMA.get(k, {})
    OM[str(S)][k] = {"ar": AR[(S, n)], "meal": MEAL[n],
                     "olcum": olcum_bicim.olcum(S, n),
                     "mercek": M[n],
                     "dikey": DIK.get(k, "  · (ayette kök bulunmuyor — dikey satır yok)"),
                     "cipa": CIPA.get(n, dict(kademe=None, olgu=False, cipa=False)),
                     "esma": {x: e.get(x) for x in ('sinif_oto', 'sinif_el', 'e_oto', 'e_el', 'muhur', 'cift', 'ton', 'ton_kismi', 'bant')}}
    gloss_gecis.gecir_kayit(OM[str(S)][k])
bil = blok_bilanco.bilanco(S, A1, A2)
bil['ariza'] = ARIZA.get((A1, A2), [])
bil['cipa_L4'] = [n for n in range(A1, A2 + 1) if CIPA.get(n, {}).get('cipa')]
bil['tarayici_isabet'] = [a for a in bil['tarayici_v4_aday'] if CIPA.get(int(a.split(':')[1]), {}).get('cipa')]
OM[str(S)].setdefault('_bilanco', {})['%d-%d' % (A1, A2)] = bil

# ilerleme — kayıttan koşulur (elle artırma YOK)
D = json.load(open('defter.json', encoding='utf-8'))
TAM = set(OM['ilerleme']['tam'])
assert S not in TAM, 'sûre %d zaten TAM sayılıyor — çift sayım riski, DUR' % S
# SÛRE 3 (iskele_3): S'nin kayıtlı ayetleri 'S:A' anahtarlarından ('S:A-B' birleşik biçimi de tanınır);
# 'A-B' biçimli eski blok özeti anahtarları ('1-20' …, sıkıştırılmış dönem) okuma SAYILMAZ.
oku_S = set()
for k in OM[str(S)]:
    m = re.fullmatch(r'%d:(\d+)(?:-(\d+))?' % S, k)
    if m:
        oku_S.update(range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1))
oku_S = sorted(oku_S)
assert oku_S == list(range(1, oku_S[-1] + 1)), 'sûre %d kayıtlı ayetleri kesintili — DUR' % S
OM['ilerleme']['kismi'][str(S)] = '1-%d ayet düzeyinde (blok başı kayıt; %d ayet)' % (oku_S[-1], len(oku_S))
okunan = (sum(1 for r in D if r['k'][0] in TAM)
          + sum(1 for r in D if r['k'][0] == S and r['k'][1] in set(oku_S)))
OM['ilerleme']['okunan_ayet'] = okunan
OM['ilerleme']['korpus_yuzde'] = round(100 * okunan / len(D), 1)
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

pm = REPO + 'mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK.setdefault(str(S), {})
# SÛRE 3: mercek_kayit['3']'te eski sıkıştırılmış ◇ notları var (52 not). Üstüne yazmadan önce
# '_sikistirilmis_eski' altına bir kez arşivlenir (blok ilk kez yazılırken; yeniden koşuda arşivlenmez).
for n in range(A1, A2 + 1):
    k = '%d:%d' % (S, n)
    if k not in OM_ONCE and k in MK[str(S)]:
        MK[str(S)].setdefault('_sikistirilmis_eski', {}).setdefault(k, MK[str(S)][k])
    MK[str(S)][k] = gloss_gecis.gecir(M[n])
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

print('blok %d:%d-%d yazıldı · okuma_metni sûre %d → %d ayet · mercek_kayit → %d · ilerleme %d (%%%s)'
      % (S, A1, A2, S, len([k for k in OM[str(S)] if not k.startswith('_')]), len(MK[str(S)]),
         okunan, OM['ilerleme']['korpus_yuzde']))
print('kısmi:', OM['ilerleme']['kismi'])
