# -*- coding: utf-8 -*-
"""Altı yeni katman. Lemma anahtarları ELLE YAZILMAZ.
1 simetri  2 düğüm grafı  3 esmâ konumlanması  4 bab/çatı profili
5 dağılım (aralık varyansı + DP)  6 kavram seyri
"""
import re, json, math
from collections import defaultdict, Counter
import kuran_akis as K

ak = K.kelime_akisi()
D = json.load(open('defter.json'))
byv = defaultdict(list)
for x in ak: byv[(x['key'][0], x['key'][1])].append(x)

# ---------- 1. SİMETRİ ----------
# ayet içi iskelet tekrarı: lemma dizisinde, uzunluğu >=3 olan ve
# ARADA en az bir terim değişerek tekrarlanan alt-dizi
def simetri(v):
    L = [x['lem_hsz'] for x in v]
    n = len(L); best = None
    for w in range(3, n // 2 + 1):
        for i in range(n - 2 * w + 1):
            for j in range(i + w, n - w + 1):
                a, b = L[i:i+w], L[j:j+w]
                fark = sum(1 for p, q in zip(a, b) if p != q)
                if 1 <= fark <= max(1, w // 3) and a[0] == b[0]:
                    if not best or w > best[0]: best = [w, i+1, j+1, fark]
    return best

for r in D:
    r['sim'] = simetri(byv[(r['k'][0], r['k'][1])])

# ---------- 3. ESMÂ KONUMLANMASI ----------
for r in D:
    e = r['esma']; n = r['n']
    r['esma_k'] = None
    if e:
        son = e[-1][0] >= n - 1
        cift = [e[i][1] + '|' + e[i+1][1] for i in range(len(e)-1) if e[i+1][0] == e[i][0] + 1]
        r['esma_k'] = {'muhur': bool(son and cift), 'son_konum': e[-1][0], 'n': n,
                       'cift': cift, 'orta': [x[1] for x in e if x[0] < n - 2]}

# ---------- 4. BAB / ÇATI PROFİLİ ----------
tok = defaultdict(list)
for ln in open('morph.txt', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 4: continue
    m = re.search(r'ROOT:([^|]+)', p[3])
    if m: tok[m.group(1)].append(p[3])
def bab(f):
    m = re.search(r'VF:(\d+)', f); return int(m.group(1)) if m else (1 if 'V' in f.split('|') or 'PCPL' in f else None)
profil = {}
for kok, fs in tok.items():
    bb = Counter(); form = Counter()
    for f in fs:
        p = f.split('|')
        b = bab(f)
        if b: bb[b] += 1
        if 'ACT_PCPL' in p: form['act_pcpl'] += 1
        elif 'PASS_PCPL' in p: form['pass_pcpl'] += 1
        elif 'VN' in p: form['masdar'] += 1
        elif 'PERF' in p: form['perf'] += 1
        elif 'IMPF' in p: form['impf'] += 1
        elif 'IMPV' in p: form['impv'] += 1
        if 'PASS' in p: form['edilgen'] += 1
    profil[kok] = {'n': len(fs), 'bab': dict(sorted(bb.items())), 'form': dict(form),
                   'bab_cesit': len(bb), 'form_cesit': len(form)}

# ---------- 5. DAĞILIM ----------
kok_i = defaultdict(list)
for x in ak:
    if x['kok']: kok_i[x['kok']].append(x['i'])
N = len(ak)
sure_boy = Counter()
for x in ak: sure_boy[x['key'][0]] += 1
for kok, idx in kok_i.items():
    if len(idx) < 2:
        profil.setdefault(kok, {})['dagilim'] = None; continue
    g = [idx[0]] + [idx[i]-idx[i-1] for i in range(1, len(idx))] + [N-idx[-1]]
    mu = sum(g)/len(g)
    cv = (sum((x-mu)**2 for x in g)/len(g))**0.5 / mu if mu else 0
    c = Counter()
    for x in ak:
        if x['kok'] == kok: c[x['key'][0]] += 1
    dp = 0.5 * sum(abs(c[s]/len(idx) - sure_boy[s]/N) for s in sure_boy)
    profil.setdefault(kok, {})['dagilim'] = {'cv': round(cv, 3), 'DP': round(dp, 3), 'n': len(idx)}

json.dump(profil, open('kok_profil.json', 'w', encoding='utf-8'), ensure_ascii=False)

# ---------- 6. KAVRAM SEYRİ ----------
seyir = defaultdict(list)
for x in ak:
    if not x['kok']: continue
    kv = K.kavram(x['kok'], x['lem_ham'], x['wid'])
    seyir[x['kok']].append([x['wid'][0], x['wid'][1], kv])
sey = {}
for kok, lst in seyir.items():
    dizi = []
    for s, a, kv in lst:
        if not dizi or dizi[-1][2] != kv: dizi.append([s, a, kv])
    sey[kok] = {'n': len(lst), 'kavram_sayisi': len(set(z[2] for z in lst)), 'gecis': dizi}
json.dump(sey, open('kavram_seyri.json', 'w', encoding='utf-8'), ensure_ascii=False)

json.dump(D, open('defter.json', 'w', encoding='utf-8'), ensure_ascii=False)

print('1 SİMETRİ: %d ayette iskelet tekrarı' % sum(1 for r in D if r['sim']))
print('   en uzun:', sorted([(r['sim'][0], '%d:%d'%tuple(r['k'])) for r in D if r['sim']], reverse=True)[:8])
print('3 ESMÂ: mühür %d | orta-esmâ içeren %d' % (
    sum(1 for r in D if r['esma_k'] and r['esma_k']['muhur']),
    sum(1 for r in D if r['esma_k'] and r['esma_k']['orta'])))
cf = Counter(c for r in D if r['esma_k'] for c in r['esma_k']['cift'])
print('   en sık çift:', cf.most_common(8))
print('4 PROFİL: %d kök | tek-bablı %d | tek-formlu %d' % (
    len(profil), sum(1 for v in profil.values() if v.get('bab_cesit') == 1),
    sum(1 for v in profil.values() if v.get('form_cesit') == 1)))
dg = [(v['dagilim']['DP'], k, v['dagilim']['n']) for k, v in profil.items() if v.get('dagilim') and v['dagilim']['n'] >= 30]
dg.sort()
print('5 DAĞILIM (n>=30): en YAYGIN:', [(k, d) for d, k, n in dg[:6]])
print('   en KÜMELENMİŞ:', [(k, d) for d, k, n in dg[-6:]])
print('6 SEYİR: %d kök | 2+ kavramlı %d' % (len(sey), sum(1 for v in sey.values() if v['kavram_sayisi'] >= 2)))
