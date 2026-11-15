# -*- coding: utf-8 -*-
"""oturum_say.py — HAREKESİZ KALIP SAYIMI (salt-okur). Kalıp elle yazılmaz: bir ayetin kelime aralığından alınır.
Kullanım:
  python3 oturum_say.py S:A i-j [--on] [--son]
    i-j  : ayetin 1-tabanlı kelime aralığı (durak işaretleri ve sûre başı besmele sayılmaz)
    --on : ilk kelime SONEK eşleşmesi (önündeki ve-/fe-/bi- farkı yutulur)
    --son: son kelime ÖNEK eşleşmesi (sonundaki zamir/i'râb farkı yutulur)
Çıktı: kalıp iskeleti, ayet sayısı, ayet listesi († = henüz okunmadı), sûre içi eşler.
GÜRÜLTÜ: i'râb farkı görünmez, imlâ farkı ayırır (OKU_BENI_OTURUM 'Dikkat'); şüphede oturum_lem.py."""
import sys
from oturum_ortak import AR, kelimeler, durum

ref, ara = sys.argv[1], sys.argv[2]
ON, SON = '--on' in sys.argv, '--son' in sys.argv
MEDDE = '--medde' in sys.argv  # bölüm 2 (sûre 5) denetimi kuralı 2: medde yapıntısı ('ءا' → 'ا') iki yanda da kaldırılır
S, A = map(int, ref.split(':'))
i, j = map(int, ara.split('-'))
K = kelimeler(S, A)
assert 1 <= i <= j <= len(K), 'aralık ayet dışında: %d kelime' % len(K)
P = K[i - 1:j]
MD = (lambda w: w.replace('ءا', 'ا').replace('ٓ', '')) if MEDDE else (lambda w: w)
P = [MD(x) for x in P]


def esle(w, p, k, n):
    if k == 0 and ON and n > 1:
        return w.endswith(p)
    if k == n - 1 and SON and n > 1:
        return w.startswith(p)
    if n == 1 and ON and SON:
        return p in w
    if n == 1 and ON:
        return w.endswith(p)
    if n == 1 and SON:
        return w.startswith(p)
    return w == p


bul = []
for (s, a) in AR:
    W = [MD(x) for x in kelimeler(s, a)]
    for x in range(len(W) - len(P) + 1):
        if all(esle(W[x + k], P[k], k, len(P)) for k in range(len(P))):
            bul.append((s, a)); break
print('kalıp:', ' '.join(P), '| mod:', (('on ' if ON else '') + ('son' if SON else '') or 'tam') + (' medde' if MEDDE else ''))
print('ayet:', len(bul))
print('liste:', ', '.join(durum(s, a) for s, a in bul))
print('sûre içi (%d):' % S, ', '.join('%d:%d' % x for x in bul if x[0] == S) or '—')
