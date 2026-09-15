# -*- coding: utf-8 -*-
"""ONARIM 7 — dikey katmanın "AYNI SAHNE" alanı (aday 806 / 835).

Bulgular:
  806 — yüksek kat, hedef kökün değil ORTAK kökün seyrekliğinden ve katkı veren
        AYRI AYET sayısının azlığından geliyor. Mevcut n<=25 koruması on iki
        vakanın altısını kaçırıyordu.
  835 — üç tür var: A) tek ayet (bilgi yok) · B) tek sahne/kalıp, 3-5 ayet
        (bilgi VAR, kaynağıyla gösterilmeli) · C) gerçek birliktelik (>5 ayet).
  850 — SINIR: ayrı ayet sayısı, donmuş kalıbı anlamsal birliktelikten ayırmıyor.
        Bu yüzden ikinci ölçüt: ortak geçişler AYNI n-gram'ı mı paylaşıyor?
        (n-gram altyapısı — onarım 2 — burada ikinci kez kullanılıyor.)

Çıktı: blok_dikey.py'nin çağırdığı dikey_kaynak(hedef, ortak) yardımcı işlevi
ve ölçüm tablosu dikey_kaynak_ornek.json.
"""
import json, re, sys
sys.path.insert(0, '.')
from collections import defaultdict, Counter
import kuran_akis

AK = kuran_akis.kelime_akisi()
POS = defaultdict(list)
for i, x in enumerate(AK):
    if x['kok']: POS[x['kok']].append((i, x['key']))
SIK = Counter(x['kok'] for x in AK if x['kok'])
ISK = json.load(open('ayet_iskelet.json', encoding='utf-8'))

def kaynak(hedef, ortak, W=6):
    H = set()
    for i, _ in POS[hedef]: H.update(range(i - W, i + W + 1))
    ay = sorted({k for i, k in POS[ortak] if i in H})
    return ay

def ifade_ortakligi(hedef, ortak, ayetler, n=3):
    """v2 — kesişim DEĞİL, EN SIK ORTAK n-gram oranı.
    v1 arızası: bütün kaynak ayetlerin aynı n-gram'ı paylaşmasını istiyordu;
    سطر▸أول (أساطير الأولين, dokuz ayette donmuş kalıp) 0,00 veriyordu."""
    if len(ayetler) < 2: return 0.0
    sayac = Counter()
    for s, a in ayetler:
        ws = ISK.get('%d:%d' % (s, a), [])
        for g in {' '.join(ws[i:i+n]) for i in range(len(ws) - n + 1)}:
            sayac[g] += 1
    if not sayac: return 0.0
    return sayac.most_common(1)[0][1] / len(ayetler)

def sinif(hedef, ortak):
    ay = kaynak(hedef, ortak)
    k = len(ay)
    io = ifade_ortakligi(hedef, ortak, ay)
    if k <= 2:   t = 'A-tek-ayet'
    elif k <= 5: t = 'B-tek-sahne'
    elif io >= 0.50: t = 'B2-donmus-kalip'
    else:        t = 'C-birliktelik'
    return {'ayri_ayet': k, 'ifade_ortakligi': round(io, 3), 'sinif': t,
            'n_hedef': SIK[hedef], 'n_ortak': SIK[ortak], 'kaynak': ay[:8]}

if __name__ == '__main__':
    # --- okumada belgelenmiş on iki vaka + aday 850'nin sınır çifti
    VAKA = [('عظم','مضغ'), ('سجد','شطر'), ('مرأ','عقر'), ('عرش','ستت'), ('شمس','قمر'),
            ('ذبح','حيي'), ('تسع','نعج'), ('طير','هيأ'), ('سوق','لفف'), ('بيت','عنكب'),
            ('مرد','شطن'), ('مرأ','غبر'), ('خوي','عرش'), ('هات','برهن'), ('رسو','ميد'),
            ('سير','مور'), ('سطر','أول'), ('عمي','صمم'), ('كنن','وقر'), ('نفخ','صور')]
    print('=== DİKEY KAYNAK SINIFLAMASI — okumadaki vakalar ===')
    print('%-7s %-7s %6s %6s %6s %7s  %s' % ('hedef','ortak','n_hed','n_ort','ayet','ifade','sınıf'))
    T = {}
    for h, o in VAKA:
        r = sinif(h, o); T['%s|%s' % (h, o)] = r
        print('%-7s %-7s %6d %6d %6d %7.2f  %s' % (h, o, r['n_hedef'], r['n_ortak'],
              r['ayri_ayet'], r['ifade_ortakligi'], r['sinif']))
    json.dump(T, open('dikey_kaynak_ornek.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print()
    c = Counter(v['sinif'] for v in T.values())
    print('sınıf dağılımı:', dict(c))
    print()
    print('ESKİ koruma (hedef n<15 -> ⚠) bu yirmi vakanın kaçını işaretliyordu:',
          sum(1 for h, o in VAKA if SIK[h] < 15))
    print('YENİ sınıflama A ya da B diyerek kaçını işaretliyor:',
          sum(1 for v in T.values() if v['sinif'].startswith(('A', 'B'))))
