# -*- coding: utf-8 -*-
"""esma_kayit.py — ön-kayıt (notlar/ONKAYIT_esma_katmanlari.md) için ayet düzeyi KAYIT.

BU BİR ÖLÇÜM DEĞİLDİR. Hipotez testi, oran, permütasyon YOK. Yalnız §4.1 (a/r/e bayrakları),
§4.3 (mühür, çift, ton) ve §4.4 (bant) alanlarını blok blok toplar.
Kullanım: python3 esma_kayit.py S A1 A2   → esma_kayit.json güncellenir, blok özeti basılır.

Anahtarlar ELLE YAZILMAZ:
  * Allah / Rab / Allâhümme lemmaları korpustaki ÇAPA konumlarından alınır ve çapalar doğrulanır.
  * Esmâ seti esma_listesi.json'dan NFC ile alınır; korpusta LEM karşılığı olmayan girdi düşer ve
    listelenir (§4.2). 'Hâdî' / 'Hayy' girdileri için karar verilmediği için bunların iskelet eşleri AYRICA
    işaretlenir (karar bekliyor), e bayrağına KATILMAZ.
e bayrağı iki sürümle tutulur:
  e_oto — lemma eşleşmesi (üst sınır; §4.2 son cümlesi)
  e_el  — okuyucu kararı: ilâhî yüklem/sıfat konumunda mı (esma_el.py). Karar yoksa None.
Bant: §4.4 kapı koşulu (aday 435, pozisyon-eşli gradyan) sağlanmadı → 'KAPI_KAPALI'.
"""
import sys, json, re, unicodedata, hashlib, os
from collections import defaultdict

S, A1, A2 = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
nfc = lambda s: unicodedata.normalize('NFC', s)
HAR = re.compile(r'[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]')
isk = lambda s: HAR.sub('', nfc(s))

# ---- morfoloji: kelime → bölütler
W = defaultdict(list)            # (s,a,w) -> [(tag, feats)]
for ln in open('morph.txt', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 4: continue
    s, a, w, g = map(int, p[0].split(':'))
    W[(s, a, w)].append((p[2], p[3].split('|')))

def lem(f):
    for x in f:
        if x.startswith('LEM:'): return nfc(x[4:])
    return None

def capa(s, a, w):
    for t, f in W[(s, a, w)]:
        if t == 'N' and lem(f): return lem(f), f
    raise SystemExit('çapa boş: %d:%d:%d' % (s, a, w))

ALLAH, f = capa(1, 1, 2); assert 'PN' in f, 'Allah çapası PN değil'
RAB, f = capa(1, 2, 3);   assert RAB != ALLAH and any(x.startswith('ROOT:') for x in f), 'Rab çapası tutmadı'
HUMME, f = capa(3, 26, 2)
assert HUMME != ALLAH and isk(HUMME).startswith(isk(ALLAH)[:-1]), 'Allâhümme çapası tutmadı'

TUM_LEM = defaultdict(int)
for k, v in W.items():
    for t, f in v:
        if lem(f): TUM_LEM[lem(f)] += 1

EL = json.load(open('esma_listesi.json', encoding='utf-8'))['lemmalar']
SHA = hashlib.sha256(open('esma_listesi.json', 'rb').read()).hexdigest()
SET, DUSEN = [], []
for x in EL:
    (SET if nfc(x) in TUM_LEM else DUSEN).append(nfc(x))
for x in SET: assert TUM_LEM[x] > 0          # ölü etiket koruması (§4.1)
BEKLEYEN = {isk(x).rstrip('ٍ'): x for x in DUSEN}   # iskelet → düşen girdi (karar bekliyor)

# ---- ton: varlik_katalog alt_tur, lem alanından (NFC)
KAT = json.load(open('varlik_katalog.json', encoding='utf-8'))
TON = {nfc(v['lem']): v['alt_tur'] for v in KAT.values()
       if v.get('tur') == 'ilâhî-isim' and v.get('lem')}

ZAMIR = {'PRON', 'DEM', 'REL', 'T', 'LOC', 'COND', 'INTG'}
def icerik(f):
    return lem(f) and not (set(f) & ZAMIR) and (any(x.startswith('ROOT:') for x in f) or 'PN' in f)

try:
    import esma_el; EL_KARAR = esma_el.KARAR
except ImportError:
    EL_KARAR = {}

KAYIT = {}
for a in range(A1, A2 + 1):
    ws = sorted(w for (s, aa, w) in W if s == S and aa == a)
    toks, ic = [], []
    for w in ws:
        for t, f in W[(S, a, w)]:
            L = lem(f)
            if t != 'N' or not L: continue
            toks.append((w, L))
            if icerik(f): ic.append((w, L))
    A_ = [w for w, L in toks if L == ALLAH]
    R_ = [w for w, L in toks if L == RAB]
    H_ = [w for w, L in toks if L == HUMME]
    E_ = [(w, L) for w, L in toks if L in SET]
    B_ = [(w, L) for w, L in toks if isk(L) in BEKLEYEN]
    son3 = ic[-3:]
    mh = [(w, L) for w, L in son3 if L in SET]
    tonlar = sorted({TON.get(L, 'katalog-dışı') for w, L in mh})
    ton = None if not mh else (tonlar[0] if len(tonlar) == 1 else 'karma')
    key = '%d:%d' % (S, a)
    el = {}
    for w, L in E_:
        k2 = '%s:%d' % (key, w)
        el[k2] = EL_KARAR.get(k2)
    e_el = None if any(v is None for v in el.values()) else any(v == 'ilahi' for v in el.values())
    a_, r_, e_ = bool(A_), bool(R_), bool(E_)
    sinif = 'AR' if a_ and r_ else 'A' if a_ else 'R' if r_ else 'E' if e_ else '0'
    sinif_el = sinif if (a_ or r_ or e_el is None) else ('E' if e_el else '0')
    KAYIT[key] = dict(a=a_, r=r_, e_oto=e_, e_el=e_el, humme=bool(H_),
                      sinif_oto=sinif, sinif_el=sinif_el,
                      esma=[[w, L] for w, L in E_], esma_el=el,
                      bekleyen=[[w, L] for w, L in B_],
                      son3=[[w, L] for w, L in son3],
                      muhur=bool(mh), cift=len(mh) >= 2, muhur_lem=[L for w, L in mh],
                      ton=ton, bant='KAPI_KAPALI')

p = 'esma_kayit.json'
T = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}
T.setdefault('_meta', {})
T['_meta'].update(onkayit='notlar/ONKAYIT_esma_katmanlari.md', esma_listesi_sha256=SHA,
                  set_boyutu=len(SET), dusen=DUSEN, ton_katalogda=len(TON),
                  capalar={'allah': '1:1:2', 'rab': '1:2:3', 'humme': '3:26:2'},
                  uyari='KAYIT — ölçüm değil. H1-H4 tam okuma bitmeden koşulmaz.')
T.update(KAYIT)
json.dump(T, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1, sort_keys=True)

print('esmâ listesi SHA-256: %s…  set %d / düşen %d %s  · ton katalogda %d lemma'
      % (SHA[:16], len(SET), len(DUSEN), DUSEN, len(TON)))
for key, r in KAYIT.items():
    print('%-6s a=%d r=%d e_oto=%d e_el=%s · sınıf %s/%s · esmâ %s · mühür %s%s ton %s · son3 %s%s'
          % (key, r['a'], r['r'], r['e_oto'], {None: '?', True: 1, False: 0}[r['e_el']],
             r['sinif_oto'], r['sinif_el'],
             ' '.join('%s@%d' % (L, w) for w, L in r['esma']) or '—',
             'EVET' if r['muhur'] else 'hayır', ' (ÇİFT)' if r['cift'] else '', r['ton'],
             ' '.join(L for w, L in r['son3']),
             ' · BEKLEYEN ' + ' '.join(L for w, L in r['bekleyen']) if r['bekleyen'] else ''))
