# -*- coding: utf-8 -*-
"""
defter.py — MATEMATİKÇİNİN DEFTERİ
Kur'an'ın 6236 ayetinin her biri için sabit şemalı bir ölçüm kaydı üretir.
Şemayı matematikçi merceği belirledi (mercek_matematikci_ayet.json'daki
tanıma repertuarı + sayı/konum gereksinimleri).

Bir kayıt = bir ayet. Alanlar:
  k        [sûre, ayet]
  ai       mutlak ayet indeksi (1..6236)
  ki       [ilk kelime, son kelime] mutlak kelime indeksi (1..77429)
  n        kelime sayısı
  mora,harf
  fs       fâsıla: [son kelime (haresiz), son harf, kafiye sınıfı]
  A        Allah lafzı: ayet-içi kelime sıraları
  R        Rab: [(ayet-içi sıra, lemma)]
  say      açık sayı sözcükleri [(kök, lemma)]
  ikile    aynı ayette >=2 kez geçen kökler {kök: sayı}
  hapaks   korpusta tek geçişli kökler
  fig      biçim etiketleri (repertuar): MM (fiil+mastar), MAILLA (ما/إن…إلا),
           LAILLA (لا…إلا), TAFDIL (ismi tafdil), AMMA (taksim), KELLA,
           QASEM (yemin), SUAL (وما أدراك / soru edatı), MEZID (izafet zinciri)
  esit     bu ayetle normalize-metni birebir aynı olan diğer ayetler
"""
import json, re, unicodedata
from collections import Counter, defaultdict
import kuran_akis as K

ak = K.kelime_akisi()
d = json.load(open('../repo/veri/kuran_veri.json'))

kok_toplam = Counter(x['kok'] for x in ak if x['kok'])
HAPAKS = {k for k, n in kok_toplam.items() if n == 1}
SAYI_KOK = {'أحد','وحد','ثني','ثلث','ربع','خمس','سدس','سبع','ثمن','تسع','عشر',
            'مائة','ألف','نصف','زوج','عدد','كثر','قلل'}
TAFDIL = re.compile(r'\bCOMP\b')

byv = defaultdict(list)
for x in ak: byv[(x['key'][0], x['key'][1])].append(x)

def sad(x):
    x = unicodedata.normalize('NFC', x)
    x = re.sub(r'[\u064B-\u0652\u0670\u06DD\u06D6-\u06ED\u0640]', '', x)
    x = x.replace('ٱ','ا').replace('آ','ا').replace('ى','ي').replace('ة','ه')
    return re.sub(r'\s+', ' ', re.sub(r'[^\u0621-\u064A ]', ' ', x)).strip()
def sadk(w):
    w = unicodedata.normalize('NFC', w)
    w = re.sub(r'[\u064B-\u0652\u0670\u06DD\u06D6-\u06ED\u0640]', '', w)
    return w.replace('ٱ','ا').replace('آ','ا')

def kafiye(w):
    w = re.sub(r'[\u064B-\u0652\u0670\u06DD\u06D6-\u06ED]', '', w)
    if not w: return '?', '?'
    c = w[-1]
    if w.endswith('ين') or w.endswith('ون'): s = 'N'
    elif c in 'نم': s = 'N'
    elif c in 'ةه': s = 'H'
    elif c in 'اى': s = 'A'
    elif c == 'ر': s = 'R'
    else: s = c
    return c, s

# tam-ayet özdeşliği indeksi
norm = {}
for s in d['sureler']:
    for a in s['ayetler']:
        t = sad(a['ar_saf'])
        if len(t.split()) >= 3: norm.setdefault(t, []).append((s['no'], a['no']))

AMMA = {'أما','فأما','وأما'}
KELLA = {'كلا'}
kayit = []
ai = 0
for s in d['sureler']:
    for a in s['ayetler']:
        ai += 1
        k = (s['no'], a['no'])
        v = byv[k]
        kel = [w for w in a['ar_saf'].split() if re.search(r'[\u0621-\u064A]', w)]
        sonw = re.sub(r'[\u064B-\u0652\u0670\u06DD\u06D6-\u06ED]', '', kel[-1]) if kel else ''
        sh, sn = kafiye(kel[-1] if kel else '')
        koklar = [x['kok'] for x in v if x['kok']]
        cc = Counter(koklar)
        t = sad(a['ar_saf'])
        fig = []
        # fiil + kendi mastarı (mef'ûl-i mutlak yaklaşığı): aynı kök, biri V biri N, bitişik
        for i in range(len(v)-1):
            if v[i]['kok'] and v[i]['kok'] == v[i+1]['kok'] and v[i]['pos'] == 'V' and v[i+1]['pos'] == 'N':
                fig.append('MM'); break
        if re.search(r'(^|\s)(ما|إن)\s.*\sإلا(\s|$)', sadk(a['ar_saf'])): fig.append('MAILLA')
        if re.search(r'(^|\s)لا\s.*\sإلا(\s|$)', sadk(a['ar_saf'])): fig.append('LAILLA')
        if any(sadk(w) in AMMA for w in kel): fig.append('AMMA')
        if any(sadk(w).startswith('كلا') and len(sadk(w)) <= 4 for w in kel): fig.append('KELLA')
        if any(x['kok'] == 'قسم' for x in v) or 'وَٱل' == a['ar_saf'][:4]: fig.append('QASEM')
        if 'أدرىك' in sad(a['ar_saf']).replace('ا','ا'): fig.append('SUAL')
        kayit.append({
            'k': list(k), 'ai': ai,
            'ki': [v[0]['i']+1, v[-1]['i']+1] if v else None,
            'n': len(v), 'mora': a['mora'], 'harf': a['harf'],
            'fs': [sonw, sh, sn],
            'A': [x['wid'][2] for x in v if x['is_allah']],
            'R': [[x['wid'][2], x['lem_ham']] for x in v if x['kok'] == 'ربب'],
            'say': [[x['kok'], x['lem_ham']] for x in v if x['kok'] in SAYI_KOK],
            'ikile': {kk: n for kk, n in cc.items() if n >= 2},
            'hapaks': sorted({kk for kk in koklar if kk in HAPAKS}),
            'fig': fig,
            'esit': [list(z) for z in norm.get(t, []) if z != k],
        })
json.dump(kayit, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)
print('kayıt: %d ayet' % len(kayit))
print('Allah lafzı içeren ayet: %d' % sum(1 for r in kayit if r['A']))
print('Rab içeren ayet: %d' % sum(1 for r in kayit if r['R']))
print('açık sayı sözcüğü içeren ayet: %d' % sum(1 for r in kayit if r['say']))
print('hapaks kök içeren ayet: %d' % sum(1 for r in kayit if r['hapaks']))
print('kök ikilemesi olan ayet: %d' % sum(1 for r in kayit if r['ikile']))
print('tam-ayet ikizi olan ayet: %d' % sum(1 for r in kayit if r['esit']))
fg = Counter()
for r in kayit:
    for f in r['fig']: fg[f] += 1
print('biçim etiketleri:', dict(fg))
