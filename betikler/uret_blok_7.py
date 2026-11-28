# -*- coding: utf-8 -*-
"""uret_blok_7.py — sûre 7 (A'râf) blok betiklerini üretir. BLOK BAŞINA KAYIT.

Değişiklik (2026-09-24): kayıt artık tur sonunu beklemiyor. Her blok betiği koşulduğunda
okuma_metni.json, mercek_kayit.json ve ilerleme o blok için yazılır; blok bilançosu (TAM SAYIM)
ve çıpa kararları da okuma_metni'ne yapılandırılmış alan olarak girer. Oturum yarıda kalsa da
okunmuş her blok kayıtlıdır.

Sûre numarası TEK değişkende (S). olcum_bicim.olcum(S, n), AR[(S, n)], OM[str(S)] hep S'den
türer — üç kez atlanan elle-değiştirme hatası (tur sonu notu) burada yapısal olarak kapalı.
Besmele korpustan (1:1'in ilk dört kelimesinin iskeleti) ayıklanır; Arapça sabit yok.
"""
import sys
S = 7
METIN = 'araf_metin_1'
KAYIT = 'araf_kayit'
# blok başı kayıt: blok okundukça listeye eklenir (başlık okuma sonrası yazılır)
BLOKLAR = [(1, 5), (6, 10), (11, 13), (14, 18), (19, 21), (22, 25), (26, 27), (28, 30), (31, 34), (35, 37), (38, 41), (42, 43), (44, 47), (48, 51), (52, 53), (54, 56), (57, 58), (59, 64), (65, 69), (70, 72), (73, 75), (76, 79), (80, 84), (85, 87)]
BASLIK = {
 (1, 5): "7:1-5 — Kitap indirildi; helak edilen kentler; tartı; yeryüzünde yerleştirme",
 (6, 10): "7:6-10 — Kitap indirildi; helak edilen kentler; tartı; yeryüzünde yerleştirme",
 (11, 13): "7:11-13 — Âdem'e secde; İblis'in mühleti; ağaç ve iniş",
 (14, 18): "7:14-18 — Âdem'e secde; İblis'in mühleti; ağaç ve iniş",
 (19, 21): "7:19-21 — Âdem'e secde; İblis'in mühleti; ağaç ve iniş",
 (22, 25): "7:22-25 — Âdem'e secde; İblis'in mühleti; ağaç ve iniş",
 (26, 27): "7:26-27 — Ey Âdemoğulları: giysi, fitne, ziynet; haram kılınanlar",
 (28, 30): "7:28-30 — Ey Âdemoğulları: giysi, fitne, ziynet; haram kılınanlar",
 (31, 34): "7:31-34 — Ey Âdemoğulları: giysi, fitne, ziynet; haram kılınanlar",
 (35, 37): "7:35-37 — Elçiler gelince; yalanlayanların ateşte çekişmesi",
 (38, 41): "7:38-41 — Elçiler gelince; yalanlayanların ateşte çekişmesi",
 (42, 43): "7:42-43 — Cennet ehli, ateş ehli ve A'râf'takiler",
 (44, 47): "7:44-47 — Cennet ehli, ateş ehli ve A'râf'takiler",
 (48, 51): "7:48-51 — Cennet ehli, ateş ehli ve A'râf'takiler",
 (52, 53): "7:52-53 — Cennet ehli, ateş ehli ve A'râf'takiler",
 (54, 56): "7:54-56 — Altı günde yaratma; dua; rüzgâr ve ölü belde",
 (57, 58): "7:57-58 — Altı günde yaratma; dua; rüzgâr ve ölü belde",
 (59, 64): "7:59-64 — Nûh ve kavmi; Hûd ve Âd",
 (65, 69): "7:65-69 — Nûh ve kavmi; Hûd ve Âd",
 (70, 72): "7:70-72 — Nûh ve kavmi; Hûd ve Âd",
 (73, 75): "7:73-75 — Sâlih ve Semûd; Lût ve kavmi",
 (76, 79): "7:76-79 — Sâlih ve Semûd; Lût ve kavmi",
 (80, 84): "7:80-84 — Sâlih ve Semûd; Lût ve kavmi",
 (85, 87): "7:85-87 — Şuayb ve Medyen",
}

SABLON = r'''# -*- coding: utf-8 -*-
"""blok_%(S)d_%(a)d_%(b)d.py — %(baslik)s

uret_blok_%(S)d.py tarafından ÜRETİLDİ — elle düzenleme. Ölçüm (›) defterden (olcum_bicim),
dikey (▽) blok_dikey JSON'undan, bilanço blok_bilanco'dan; yalnız meal ve mercek (◇) elle.
"""
import json, re, unicodedata
import olcum_bicim, gloss_gecis, blok_bilanco
from %(metin)s import MEAL, M
from %(kayit)s import CIPA, ARIZA

S, A1, A2 = %(S)d, %(a)d, %(b)d
REPO = '/home/claude/repo/notlar/'
DIK = json.load(open('blok_dikey_%%d_%%d_%%d.json' %% (S, A1, A2), encoding='utf-8'))
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
    assert n in MEAL and n in M, 'meal/mercek eksik: %%d:%%d — DUR' %% (S, n)

p = REPO + 'okuma_metni.json'
OM = json.load(open(p, encoding='utf-8'))
OM.setdefault(str(S), {})
OM_ONCE = set(OM[str(S)])
for n in range(A1, A2 + 1):
    k = '%%d:%%d' %% (S, n)
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
OM[str(S)].setdefault('_bilanco', {})['%%d-%%d' %% (A1, A2)] = bil

# ilerleme — kayıttan koşulur (elle artırma YOK)
D = json.load(open('defter.json', encoding='utf-8'))
TAM = set(OM['ilerleme']['tam'])
assert S not in TAM, 'sûre %%d zaten TAM sayılıyor — çift sayım riski, DUR' %% S
# SÛRE 7 (iskele_7): S'nin kayıtlı ayetleri 'S:A' anahtarlarından ('S:A-B' birleşik biçimi de tanınır);
# 'A-B' biçimli eski blok özeti anahtarları ('1-20' … '181-206', sıkıştırılmış dönem) okuma SAYILMAZ.
oku_S = set()
for k in OM[str(S)]:
    m = re.fullmatch(r'%%d:(\d+)(?:-(\d+))?' %% S, k)
    if m:
        oku_S.update(range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1))
oku_S = sorted(oku_S)
assert oku_S == list(range(1, oku_S[-1] + 1)), 'sûre %%d kayıtlı ayetleri kesintili — DUR' %% S
OM['ilerleme']['kismi'][str(S)] = '1-%%d ayet düzeyinde (blok başı kayıt; %%d ayet)' %% (oku_S[-1], len(oku_S))
okunan = (sum(1 for r in D if r['k'][0] in TAM)
          + sum(1 for r in D if r['k'][0] == S and r['k'][1] in set(oku_S)))
OM['ilerleme']['okunan_ayet'] = okunan
OM['ilerleme']['korpus_yuzde'] = round(100 * okunan / len(D), 1)
json.dump(OM, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

pm = REPO + 'mercek_kayit.json'
MK = json.load(open(pm, encoding='utf-8'))
MK.setdefault(str(S), {})
# SÛRE 7: mercek_kayit['7']'de eski sıkıştırılmış ◇ notları var (35 not). Üstüne yazmadan önce
# '_sikistirilmis_eski' altına bir kez arşivlenir (blok ilk kez yazılırken; yeniden koşuda arşivlenmez).
for n in range(A1, A2 + 1):
    k = '%%d:%%d' %% (S, n)
    if k not in OM_ONCE and k in MK[str(S)]:
        MK[str(S)].setdefault('_sikistirilmis_eski', {}).setdefault(k, MK[str(S)][k])
    MK[str(S)][k] = gloss_gecis.gecir(M[n])
json.dump(MK, open(pm, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

print('blok %%d:%%d-%%d yazıldı · okuma_metni sûre %%d → %%d ayet · mercek_kayit → %%d · ilerleme %%d (%%%%%%s)'
      %% (S, A1, A2, S, len([k for k in OM[str(S)] if not k.startswith('_')]), len(MK[str(S)]),
         okunan, OM['ilerleme']['korpus_yuzde']))
print('kısmi:', OM['ilerleme']['kismi'])
'''

for a, b in BLOKLAR:
    ad = 'blok_%d_%d_%d.py' % (S, a, b)
    open(ad, 'w', encoding='utf-8').write(SABLON % dict(S=S, a=a, b=b, baslik=BASLIK[(a, b)], metin=METIN, kayit=KAYIT))
    print('üretildi:', ad)
