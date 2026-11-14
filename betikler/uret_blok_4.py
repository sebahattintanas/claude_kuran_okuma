# -*- coding: utf-8 -*-
"""uret_blok_4.py — sûre 4 (Nisâ) blok betiklerini üretir. BLOK BAŞINA KAYIT.

Değişiklik (2026-09-24): kayıt artık tur sonunu beklemiyor. Her blok betiği koşulduğunda
okuma_metni.json, mercek_kayit.json ve ilerleme o blok için yazılır; blok bilançosu (TAM SAYIM)
ve çıpa kararları da okuma_metni'ne yapılandırılmış alan olarak girer. Oturum yarıda kalsa da
okunmuş her blok kayıtlıdır.

Sûre numarası TEK değişkende (S). olcum_bicim.olcum(S, n), AR[(S, n)], OM[str(S)] hep S'den
türer — üç kez atlanan elle-değiştirme hatası (tur sonu notu) burada yapısal olarak kapalı.
Besmele korpustan (1:1'in ilk dört kelimesinin iskeleti) ayıklanır; Arapça sabit yok.
"""
import sys
S = 4
METIN = 'nisa_metin_1'
KAYIT = 'nisa_kayit'
# blok başı kayıt: blok okundukça listeye eklenir (başlık okuma sonrası yazılır)
BLOKLAR = [(1, 5), (6, 10), (11, 11), (12, 12), (13, 14), (15, 18), (19, 22), (23, 24), (25, 28), (29, 32), (33, 35), (36, 39), (40, 43), (44, 47), (48, 52), (53, 57), (58, 60), (61, 64), (65, 70), (71, 75), (76, 78), (79, 83), (84, 87), (88, 90), (91, 92), (93, 96), (97, 101), (102, 104), (105, 111), (112, 115), (116, 121), (122, 126), (127, 129), (130, 134)]
BASLIK = {
 (1, 5): "4:1-5 — Tek nefisten yaratılış; yetimlerin malları; evlilik ve mehir",
 (6, 10): "4:6-10 — Tek nefisten yaratılış; yetimlerin malları; evlilik ve mehir",
 (11, 11): "4:11-11 — Miras payları ve Allah'ın sınırları",
 (12, 12): "4:12-12 — Miras payları ve Allah'ın sınırları",
 (13, 14): "4:13-14 — Miras payları ve Allah'ın sınırları",
 (15, 18): "4:15-18 — Hayâsızlığın cezası; tövbe; kadınlarla güzel geçim; evlenme yasakları",
 (19, 22): "4:19-22 — Hayâsızlığın cezası; tövbe; kadınlarla güzel geçim; evlenme yasakları",
 (23, 24): "4:23-24 — Evlenilmesi yasak olanlar; evlilik izni; Allah'ın hafifletmesi",
 (25, 28): "4:25-28 — 4:25-28 — Evlenilmesi yasak olanlar; evlilik izni; Allah'ın hafifletmesi",
 (29, 32): "4:29-32 — Malları haksız yere yememe; büyük günahlar; aile içi düzen ve hakem",
 (33, 35): "4:33-35 — Malları haksız yere yememe; büyük günahlar; aile içi düzen ve hakem",
 (36, 39): "4:36-39 — Ana babaya ve yakınlara iyilik; cimriler ve gösterişçiler; namaz ve teyemmüm",
 (40, 43): "4:40-43 — Ana babaya ve yakınlara iyilik; cimriler ve gösterişçiler; namaz ve teyemmüm",
 (44, 47): "4:44-47 — Kitap ehlinden bir kesim; şirkin bağışlanmaması; ateş ve cennet",
 (48, 52): "4:48-52 — Kitap ehlinden bir kesim; şirkin bağışlanmaması; ateş ve cennet",
 (53, 57): "4:53-57 — Kitap ehlinden bir kesim; şirkin bağışlanmaması; ateş ve cennet",
 (58, 60): "4:58-60 — Emanet ve adalet; itaat; tâğûta başvuranlar; itaat edenlerin yeri",
 (61, 64): "4:61-64 — Emanet ve adalet; itaat; tâğûta başvuranlar; itaat edenlerin yeri",
 (65, 70): "4:65-70 — Emanet ve adalet; itaat; tâğûta başvuranlar; itaat edenlerin yeri",
 (71, 75): "4:71-75 — Savaşa hazırlık; Allah yolunda savaş; ölüm; münafıkların tutumu; selam",
 (76, 78): "4:76-78 — Savaşa hazırlık; Allah yolunda savaş; ölüm; münafıkların tutumu; selam",
 (79, 83): "4:79-83 — Savaşa hazırlık; Allah yolunda savaş; ölüm; münafıkların tutumu; selam",
 (84, 87): "4:84-87 — Savaşa hazırlık; Allah yolunda savaş; ölüm; münafıkların tutumu; selam",
 (88, 90): "4:88-90 — Münafıklar hakkında ayrılık; öldürme ve diyet; hicret; korku namazı",
 (91, 92): "4:91-92 — Münafıklar hakkında ayrılık; öldürme ve diyet; hicret; korku namazı",
 (93, 96): "4:93-96 — Münafıklar hakkında ayrılık; öldürme ve diyet; hicret; korku namazı",
 (97, 101): "4:97-101 — Münafıklar hakkında ayrılık; öldürme ve diyet; hicret; korku namazı",
 (102, 104): "4:102-104 — Münafıklar hakkında ayrılık; öldürme ve diyet; hicret; korku namazı",
 (105, 111): "4:105-111 — Hainleri savunmama; gizli konuşma; elçiye muhalefet",
 (112, 115): "4:112-115 — Hainleri savunmama; gizli konuşma; elçiye muhalefet",
 (116, 121): "4:116-121 — Şirk; şeytanın vaadi; iman ve salih amel; İbrâhîm milleti",
 (122, 126): "4:122-126 — Şirk; şeytanın vaadi; iman ve salih amel; İbrâhîm milleti",
 (127, 129): "4:127-129 — Kadınlar ve yetimler hakkında fetva; geçimsizlikte barış; adalet",
 (130, 134): "4:130-134 — Kadınlar ve yetimler hakkında fetva; geçimsizlikte barış; adalet",
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
# SÛRE 4 (iskele_4): S'nin kayıtlı ayetleri 'S:A' anahtarlarından ('S:A-B' birleşik biçimi de tanınır);
# 'A-B' biçimli eski blok özeti anahtarları ('1-20' … '141-176', sıkıştırılmış dönem) okuma SAYILMAZ.
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
# SÛRE 4: mercek_kayit['4']'te eski sıkıştırılmış ◇ notları var (19 not). Üstüne yazmadan önce
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
