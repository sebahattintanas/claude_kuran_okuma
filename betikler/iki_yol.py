# -*- coding: utf-8 -*-
"""
İKİ YOL — ÖN-KAYIT (hesaplamadan önce sabitlendi)
--------------------------------------------------
Çıkış noktası (Fâtiha 1:7, ölçülmüş):
   أَنْعَمْتَ    V PERF VF:4 ROOT:نعم 2MS   -> fâil: muhatap (2. şahıs), grup: mecrûr
   ٱلْمَغْضُوبِ  PASS_PCPL VF:1 ROOT:غضب     -> grup: EDİLGEN (kendisine yapılan)
   ٱلضَّآلِّينَ  ACT_PCPL  VF:1 ROOT:ضلل     -> grup: ETKEN (kendi yaptığı)
Yani Fâtiha'nın son ayeti üç grubu üç farklı dilbilgisel rolde veriyor ve
"yanlış yol"un iki tarifi çatı bakımından birbirinin zıddı.

H2: Bu ayrım sistematiktir — hidâyet ve dalâlet kökleri ÇATI (voice) ve
    BAB (verb form) dağılımında birbirinden farklıdır. Özel olarak:
    (a) هدي'de fâil ağırlıklı olarak Allah; grubun kendi başına hidâyeti
        ayrı bir bab (VIII, اهتدى) ile verilir.
    (b) ضلل'de grup KENDİ fâili olabilir (VF:1) — hidâyette bu yok.

Ölçüm: morph.txt'ten ilgili köklerin tüm token'ları; VF (bab), PERF/IMPF,
    PASS (edilgen), ACT_PCPL / PASS_PCPL etiketleri sayılır.
Sınır: Bu bir DAĞILIM ölçümüdür. "Fâil kimdir" sorusu i'râb ayrıştırması
    gerektirir; burada bab+çatı üzerinden dolaylı ölçülüyor.
"""
import re
from collections import Counter, defaultdict

tok = []
for ln in open('morph.txt', encoding='utf-8'):
    p = ln.rstrip('\n').split('\t')
    if len(p) < 4: continue
    loc = p[0].split(':')
    if len(loc) == 5: loc = loc[1:]      # bazı satırlarda başta global indeks var
    if len(loc) != 4: continue
    s, a, w, seg = (int(x) for x in loc)
    feats = p[3]
    m = re.search(r'ROOT:([^|]+)', feats)
    tok.append({'s': s, 'a': a, 'w': w, 'pos': p[2], 'f': feats,
                'kok': m.group(1) if m else ''})
print('token: %d' % len(tok))

def vf(f):
    m = re.search(r'VF:(\d+)', f); return int(m.group(1)) if m else 1

def rapor(kok, baslik):
    h = [t for t in tok if t['kok'] == kok]
    print('\n=== %s (%s) — %d token ===' % (kok, baslik, len(h)))
    c = Counter()
    for t in h:
        f = t['f']
        if 'ACT_PCPL' in f: tip = 'ACT_PCPL (ism-i fâil)'
        elif 'PASS_PCPL' in f: tip = 'PASS_PCPL (ism-i mef\'ûl)'
        elif t['pos'] == 'V':
            tip = 'FİİL edilgen' if 'PASS' in f.split('|') else 'FİİL etken'
        elif t['pos'] == 'N': tip = 'İSİM/masdar'
        else: tip = t['pos']
        c[(tip, vf(f))] += 1
    for (tip, b), n in sorted(c.items(), key=lambda x: -x[1]):
        print('   %-26s bab %-2d  %4d' % (tip, b, n))

for k, b in [('هدي','hidâyet'), ('ضلل','dalâlet'), ('نعم','nimet'),
             ('غضب','gazap'), ('أمن','iman'), ('كفر','küfür')]:
    rapor(k, b)
