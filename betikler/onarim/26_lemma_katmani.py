# -*- coding: utf-8 -*-
"""26_lemma_katmani.py — ONARIM 16 (P0 #5 parçası a: LEMMA KİMLİĞİ).

P0 #5'in iki parçası var ve maliyetleri taban tabana zıt:

  (a) LEMMA KİMLİĞİ   — morfolojideki LEM alanı; ZATEN VAR, maliyet 0.
                        `nakarat2`nin yüzey n-gram arızasını ve çıpa taramasının
                        kök→olgu eşleşme arızasını onarır.
  (b) LEMMA GLOSSU    — (kök, lemma) için Türkçe karşılık; tam tablo 3737 satır,
                        okunan ayetlerde 2537 satır. ELLE iş.

Bu betik (a)'yı yazar. (b) ayrı ele alınır.

ÜRETİLEN:
  lemma_iskelet.json   — ayet -> lemma dizisi (bağlaç önekleri atılır, ayet_iskelet
                         ile aynı bölütleme, ama yüzey biçimi yerine LEM)
  lemma_envanteri.json — kök -> {lemma: token sayısı}

ÖLÇÜLEN (aday 940): okumada belgelenmiş 28 çok-anlamlılık vakasının hangisini
hangi katman çözüyor.
"""
import re, json, unicodedata, collections

HAREKE = re.compile(r'[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u08F0-\u08FF]')


def sad(t):
    t = HAREKE.sub('', unicodedata.normalize('NFC', t))
    t = t.replace('\u0671', '\u0627')
    t = re.sub('[\u0622\u0623\u0625\u0649]', '\u0627', t)
    t = t.replace('\u0624', '\u0648').replace('\u0626', '\u064A')
    t = t.replace('\u0629', '\u0647')
    return re.sub(r'[^\u0621-\u064A]', '', t)


# --- morfolojiden kelime bölütleri: 04_ngram_altyapi.py ile AYNI bölütleme
kel = collections.defaultdict(lambda: collections.defaultdict(list))
for ln in open('morph.txt', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 4:
        continue
    loc = p[0].split(':')
    if len(loc) == 5:
        loc = loc[1:]
    if len(loc) != 4:
        continue
    s, a, w = int(loc[0]), int(loc[1]), int(loc[2])
    kel[(s, a)][w].append((p[1], p[3]))

ISKELET = {}
ENV = collections.defaultdict(collections.Counter)
for (s, a), ws in kel.items():
    diz = []
    for w in sorted(ws):
        parca = ws[w]
        # bağlaç öneki atılır (04'ün kuralı)
        govde = [x for x in parca if 'CONJ|PREF' not in x[1]]
        if not govde:
            continue
        # kelimenin lemma kimliği: kök taşıyan ilk bölütün LEM'i;
        # kök yoksa (edat, zamir) sadeleştirilmiş yüzey biçimi
        lem = None
        for yuz, etiket in govde:
            m = re.search(r'ROOT:([^|]+)', etiket)
            if m:
                l = re.search(r'LEM:([^|]+)', etiket)
                lem = '%s|%s' % (m.group(1), l.group(1) if l else '?')
                ENV[m.group(1)][l.group(1) if l else '?'] += 1
                break
        if lem is None:
            lem = sad(''.join(x[0] for x in govde))
        if lem:
            diz.append(lem)
    ISKELET['%d:%d' % (s, a)] = diz

json.dump(ISKELET, open('lemma_iskelet.json', 'w', encoding='utf-8'), ensure_ascii=False)
json.dump({k: dict(v) for k, v in ENV.items()},
          open('lemma_envanteri.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

print('=== ONARIM 16 — LEMMA KATMANI (parça a) ===')
print('lemma_iskelet.json   : %d ayet' % len(ISKELET))
print('lemma_envanteri.json : %d kök' % len(ENV))
print('toplam (kök, lemma)  : %d çift' % sum(len(v) for v in ENV.values()))
d = collections.Counter(len(v) for v in ENV.values())
print('lemma sayısı dağılımı: %s ... en yüksek %d' % (dict(sorted(d.items())[:6]), max(d)))

# --- kaybedilen == 0: lemma iskeleti, yüzey iskeletiyle aynı UZUNLUKTA olmalı
YUZ = json.load(open('ayet_iskelet.json', encoding='utf-8'))
fark = [k for k in YUZ if len(YUZ[k]) != len(ISKELET.get(k, []))]
print('\nyüzey iskeletiyle uzunluk farkı olan ayet: %d  <- sıfır olmalı' % len(fark))
if fark:
    for k in fark[:5]:
        print('   %s: yüzey %d, lemma %d' % (k, len(YUZ[k]), len(ISKELET.get(k, []))))
