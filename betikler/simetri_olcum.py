# -*- coding: utf-8 -*-
"""simetri_olcum.py — matematikçi merceği: düz/ters okumada simetri (KEŞİF, ön-kayıtsız; 2026-10-05).
T1 ayet uzunluğu palindromu (5 ve 7 ayetlik pencere) — null: sûre içi ayet uzunluklarını karıştırma (500 perm).
T2 aralık halkası — iki lafzın bulunduğu ayetlerin kök örtüşmesi (أله hariç) vs aynı sûrede aynı ayet uzaklığındaki rastgele ayet çiftleri.
T3 sûre halkası — ilk ve son ayetin kök örtüşmesinin, ilk ayetin diğer ayetlerle örtüşmeleri içindeki yüzdelik sırası (null beklenti 0,5).
Her test tek/çift sûre numarası yarılarında ayrı raporlanır (keşif/doğrulama ayrımı)."""
import json, random, collections, statistics as st, unicodedata as ud
N = lambda s: ud.normalize('NFC', s)
F = open('veri/morph.txt', encoding='utf-8').read().splitlines()
L_ALL = N([t for l in F if l.startswith('1:1:2:1\t') for t in l.split('\t')[3].split('|') if t.startswith('LEM:')][0])
words = collections.defaultdict(set); kok = collections.defaultdict(set); laf = []
for l in F:
    p = l.split('\t')
    if len(p) < 4 or p[0].count(':') != 3: continue
    s, a, w, _ = map(int, p[0].split(':'))
    words[(s, a)].add(w)
    t = [N(x) for x in p[3].strip().split('|')]
    for x in t:
        if x.startswith('ROOT:') and x != N('ROOT:أله'): kok[(s, a)].add(x[5:])
    if L_ALL in t: laf.append((s, a, w))
AY = collections.defaultdict(list)
for (s, a) in sorted(words): AY[s].append(a)
LEN = {k: len(v) for k, v in words.items()}
jac = lambda x, y: len(x & y) / len(x | y) if x | y else 0.0
R = {}; rng = random.Random(2026)
# T1
def pal_say(seq, w):
    return sum(1 for i in range(len(seq) - w + 1) if all(seq[i + j] == seq[i + w - 1 - j] for j in range(w // 2)))
for w in (5, 7):
    for yari, ss in (('tek', [s for s in AY if s % 2]), ('çift', [s for s in AY if s % 2 == 0])):
        obs = sum(pal_say([LEN[(s, a)] for a in AY[s]], w) for s in ss)
        nul = []
        for _ in range(500):
            tot = 0
            for s in ss:
                q = [LEN[(s, a)] for a in AY[s]]; rng.shuffle(q); tot += pal_say(q, w)
            nul.append(tot)
        R[f'T1_w{w}_{yari}'] = {'gozlenen': obs, 'null_ort': round(st.mean(nul), 1), 'p_ust': round(sum(x >= obs for x in nul) / len(nul), 3)}
# T2 aralık halkası
pairs = []
for (s1, a1, _), (s2, a2, _) in zip(laf, laf[1:]):
    if s1 == s2 and a2 > a1: pairs.append((s1, a1, a2))
for yari, f in (('tek', lambda s: s % 2), ('çift', lambda s: s % 2 == 0)):
    P = [x for x in pairs if f(x[0])]
    obs = st.mean(jac(kok[(s, a1)], kok[(s, a2)]) for s, a1, a2 in P)
    nul = []
    for _ in range(300):
        v = []
        for s, a1, a2 in P:
            d = a2 - a1; n = len(AY[s]); st0 = rng.randint(1, n - d)
            v.append(jac(kok[(s, st0)], kok[(s, st0 + d)]))
        nul.append(st.mean(v))
    R[f'T2_aralik_halkasi_{yari}'] = {'cift': len(P), 'gozlenen_jaccard': round(obs, 4), 'null_ort': round(st.mean(nul), 4),
                                     'oran': round(obs / st.mean(nul), 2), 'p_ust': round(sum(x >= obs for x in nul) / len(nul), 3)}
# T3 sûre halkası
for yari, f in (('tek', lambda s: s % 2), ('çift', lambda s: s % 2 == 0)):
    rk = []
    for s in AY:
        if not f(s) or len(AY[s]) < 6: continue
        a = AY[s]; ilk = kok[(s, a[0])]
        diger = [jac(ilk, kok[(s, x)]) for x in a[1:-1]]; son = jac(ilk, kok[(s, a[-1])])
        rk.append((sum(x < son for x in diger) + 0.5 * sum(x == son for x in diger)) / len(diger))
    R[f'T3_sure_halkasi_{yari}'] = {'sure': len(rk), 'yuzdelik_ort': round(st.mean(rk), 3), 'ust_ceyrek_orani': round(sum(x >= .75 for x in rk) / len(rk), 3)}
json.dump(R, open('ciktilar/simetri_olcum.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(R, ensure_ascii=False, indent=1))

# ---- İZLEME (sonuç görüldükten sonra eklendi — KEŞİF) ----
# T1 kimden geliyor?
katki = collections.Counter()
for s in AY:
    q = [LEN[(s, a)] for a in AY[s]]
    katki[s] = pal_say(q, 5)
R['T1_w5_en_cok_katki'] = katki.most_common(8)
NAK = {55, 77, 26, 54, 37}
for yari, ss in (('tek', [s for s in AY if s % 2 and s not in NAK]), ('çift', [s for s in AY if s % 2 == 0 and s not in NAK])):
    obs = sum(pal_say([LEN[(s, a)] for a in AY[s]], 5) for s in ss); nul = []
    for _ in range(500):
        tot = 0
        for s in ss:
            q = [LEN[(s, a)] for a in AY[s]]; rng.shuffle(q); tot += pal_say(q, 5)
        nul.append(tot)
    R[f'T1_w5_{yari}_nakaratsiz'] = {'dislanan': sorted(NAK), 'gozlenen': obs, 'null_ort': round(st.mean(nul), 1), 'p_ust': round(sum(x >= obs for x in nul) / len(nul), 3)}
# T2b: null = aynı sûrede, aynı uzaklıkta, İKİSİ DE lafız içeren ayet çifti
LV = collections.defaultdict(set)
for s, a, w in laf: LV[s].add(a)
for yari, f in (('tek', lambda s: s % 2), ('çift', lambda s: s % 2 == 0)):
    P = [x for x in pairs if f(x[0])]
    havuz = {}
    for s, a1, a2 in P:
        d = a2 - a1
        havuz[(s, d)] = [(x, x + d) for x in sorted(LV[s]) if x + d in LV[s]]
    obs = st.mean(jac(kok[(s, a1)], kok[(s, a2)]) for s, a1, a2 in P)
    nul = []
    for _ in range(300):
        nul.append(st.mean(jac(kok[(s, x)], kok[(s, y)]) for s, a1, a2 in P for (x, y) in [rng.choice(havuz[(s, a2 - a1)])]))
    R[f'T2b_lafiz_ayeti_nullu_{yari}'] = {'gozlenen': round(obs, 4), 'null_ort': round(st.mean(nul), 4), 'oran': round(obs / st.mean(nul), 2),
                                          'p_ust': round(sum(x >= obs for x in nul) / len(nul), 3)}
json.dump(R, open('ciktilar/simetri_olcum.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in R.items() if k.startswith(('T1_w5_en', 'T1_w5_tek_n', 'T1_w5_çift_n', 'T2b'))}, ensure_ascii=False, indent=1))
# T1c: TRİVİAL OLMAYAN palindrom (pencerede ≥3 farklı uzunluk) — eşit uzunluklu dizilerin (81:1–14 gibi) etkisini ayıklar
def pal3(seq, w=5):
    return sum(1 for i in range(len(seq) - w + 1) if all(seq[i + j] == seq[i + w - 1 - j] for j in range(w // 2)) and len(set(seq[i:i + w])) >= 3)
for yari, ss in (('tek', [s for s in AY if s % 2]), ('çift', [s for s in AY if s % 2 == 0])):
    obs = sum(pal3([LEN[(s, a)] for a in AY[s]]) for s in ss); nul = []
    for _ in range(500):
        tot = 0
        for s in ss:
            q = [LEN[(s, a)] for a in AY[s]]; rng.shuffle(q); tot += pal3(q)
        nul.append(tot)
    R[f'T1c_w5_3farkli_{yari}'] = {'gozlenen': obs, 'null_ort': round(st.mean(nul), 1), 'p_ust': round(sum(x >= obs for x in nul) / len(nul), 3)}
# T1d: komşu ayet uzunluk benzerliği (yerel düzen) — palindromun asıl kaynağı mı?
for yari, ss in (('tek', [s for s in AY if s % 2]), ('çift', [s for s in AY if s % 2 == 0])):
    eq = lambda q: sum(1 for i in range(len(q) - 1) if q[i] == q[i + 1])
    obs = sum(eq([LEN[(s, a)] for a in AY[s]]) for s in ss); nul = []
    for _ in range(300):
        tot = 0
        for s in ss:
            q = [LEN[(s, a)] for a in AY[s]]; rng.shuffle(q); tot += eq(q)
        nul.append(tot)
    R[f'T1d_komsu_esit_{yari}'] = {'gozlenen': obs, 'null_ort': round(st.mean(nul), 1), 'oran': round(obs / st.mean(nul), 2)}
json.dump(R, open('ciktilar/simetri_olcum.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in R.items() if k.startswith(('T1c', 'T1d'))}, ensure_ascii=False, indent=1))
