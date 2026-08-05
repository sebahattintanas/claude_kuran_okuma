# -*- coding: utf-8 -*-
"""
kavram_uzayi.py — Kur'an kavramlarının geometrisi.
Metrik: JACCARD MESAFESİ (aksiyom-onaylı: d(x,x)=0, simetri, üçgen eşitsizliği 0 ihlal).
d(A,B) = 1 - |A∩B| / |A∪B|   (A,B = kavramın geçtiği ayet kümeleri)

kuran_akis.py çekirdeği üstüne kurulu.
"""
import sys, itertools, json
from collections import defaultdict
import kuran_akis
from kuran_akis import kelime_akisi, kavram

_KAV_AYET = None
def kavram_ayet_kumeleri():
    """her çözümlenmiş kavram -> geçtiği ayet kümesi."""
    global _KAV_AYET
    if _KAV_AYET is None:
        ak = kelime_akisi()
        d = defaultdict(set)
        for x in ak:
            if x['is_allah']:
                d['الله'].add(x['key'])          # Allah'ı da kavram olarak ekle
            elif x['kok']:
                d[kavram(x['kok'], x['lem_ham'])].add(x['key'])
        _KAV_AYET = d
    return _KAV_AYET

def jaccard(a, b):
    """Jaccard mesafesi (aksiyom-onaylı metrik)."""
    kav = kavram_ayet_kumeleri()
    A, B = kav.get(a, set()), kav.get(b, set())
    u = len(A | B)
    return 1 - len(A & B) / u if u else 1.0

def mesafe_matrisi(kavramlar):
    """simetrik Jaccard mesafe matrisi (liste-liste)."""
    n = len(kavramlar)
    M = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            d = jaccard(kavramlar[i], kavramlar[j])
            M[i][j] = M[j][i] = d
    return M

def aksiyom_testi(kavramlar):
    """metriğin aksiyomlarını veri üstünde doğrula."""
    K = kavramlar
    a1 = all(abs(jaccard(k, k)) < 1e-9 for k in K)
    a3 = all(abs(jaccard(a, b) - jaccard(b, a)) < 1e-9 for a, b in itertools.combinations(K, 2))
    ihlal = tot = 0
    for a, b, c in itertools.combinations(K, 3):
        for x, y, z in [(a,b,c),(b,c,a),(c,a,b)]:
            tot += 1
            if jaccard(x, z) > jaccard(x, y) + jaccard(y, z) + 1e-9: ihlal += 1
    return {'d(x,x)=0': a1, 'simetri': a3, 'ucgen_ihlal': ihlal, 'ucgen_toplam': tot}

# çekirdek kavram listesi (yeterli sıklık, karışıklar çözülmüş)
CEKIRDEK = ['الله','ربب','رحم','عذب','كفر','امن','علم','خلق','حكم','عبد','هدي','شرك',
 'موت','حيي','جزي','ايي','رسل','كتب','صلو','زكو','حدد','طغي','zulüm','karanlık','نور',
 'عدل','قسط','جنن','نار','دعو','غفر','قوم','nas','insan','tekzib','beşer']

def cekirdek(min_ayet=15):
    kav = kavram_ayet_kumeleri()
    return [k for k in CEKIRDEK if len(kav.get(k, set())) >= min_ayet]

if __name__ == '__main__':
    K = cekirdek()
    print("Çekirdek kavram: %d" % len(K))
    t = aksiyom_testi(K)
    print("Aksiyom sınavı: d(x,x)=0:%s simetri:%s üçgen-ihlal:%d/%d" %
          (t['d(x,x)=0'], t['simetri'], t['ucgen_ihlal'], t['ucgen_toplam']))
    # en yakın ve en uzak çiftler
    ciftler = [(jaccard(a,b), a, b) for a,b in itertools.combinations(K,2)]
    ciftler.sort()
    print("\nEN YAKIN 8 çift (metin bunları bir arada tutuyor):")
    for d,a,b in ciftler[:8]: print("  %.3f  %s ~ %s" % (d,a,b))
    print("\nEN UZAK 5 çift:")
    for d,a,b in ciftler[-5:]: print("  %.3f  %s ~ %s" % (d,a,b))
