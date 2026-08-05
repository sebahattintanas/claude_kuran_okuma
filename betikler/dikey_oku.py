# -*- coding: utf-8 -*-
"""
dikey_oku.py — bir kavramı Allah-ekseninde "dikey" okur.
kuran_akis.py çekirdeği üstüne kurulu. Elle tekrar tekrar yazdığımız
komşuluk + Allah-mesafesi + örnek analizini tek fonksiyona indirger.

Kullanım:
    from dikey_oku import dikey_oku, gradyan_cetveli
    r = dikey_oku(kok='طغي')            # kök ile
    r = dikey_oku(kavram_ad='zulüm')    # ayrılmış kavram ile (kok_anlam_tablosu)
    print(r['ozet'])
"""
import bisect, json, re, random
from collections import Counter
import kuran_akis
from kuran_akis import kelime_akisi, kavram, allah_indeksleri

# --- akışı bir kez kur, önbelleğe al ---
_AKIS = None
_ALLAH = None
_GENEL = None      # her kavramın genel sıklığı (baseline)
_TOPLAM = None
_RAST_MED = None   # rastgele kavramın Allah'a medyan mesafesi (referans)
def _akis():
    global _AKIS, _ALLAH, _GENEL, _TOPLAM, _RAST_MED
    if _AKIS is None:
        _AKIS = kelime_akisi()
        _ALLAH = allah_indeksleri(_AKIS)
        # baseline: her kavramın genel sıklığı
        _GENEL = Counter()
        for x in _AKIS:
            if x['kok']: _GENEL[_kavram_at(x)] += 1
        _TOPLAM = sum(_GENEL.values())
        # rastgele referans: rastgele kelimelerin Allah'a medyan mesafesi
        random.seed(42)
        tum = [x['i'] for x in _AKIS if x['kok']]
        rm = []
        for ti in random.sample(tum, min(2000, len(tum))):
            pos = bisect.bisect_left(_ALLAH, ti); cand = []
            if pos < len(_ALLAH): cand.append(_ALLAH[pos])
            if pos > 0: cand.append(_ALLAH[pos-1])
            if cand: rm.append(abs(ti - min(cand, key=lambda a: abs(a-ti))))
        rm.sort()
        _RAST_MED = rm[len(rm)//2] if rm else 10
    return _AKIS, _ALLAH

def _kavram_at(x):
    """akış elemanının çözümlenmiş kavramı."""
    return kavram(x['kok'], x['lem_ham']) if x['kok'] else ''

def _hedef_indeksler(kok=None, kavram_ad=None):
    """Hedef kavramın akıştaki indeksleri.
    kok verilirse o kök; kavram_ad verilirse ayrılmış-kavram (ör 'zulüm')."""
    ak, _ = _akis()
    idx = []
    for x in ak:
        if kavram_ad is not None:
            if x['kok'] and _kavram_at(x) == kavram_ad: idx.append(x['i'])
        elif kok is not None:
            if x['kok'] == kok: idx.append(x['i'])
    return idx

def dikey_oku(kok=None, kavram_ad=None, W=6, ornek_n=5, meal=None):
    """
    Bir kavramı Allah-ekseninde okur.
    Dönen sözlük:
      geçiş, oncesi, sonrasi (Counter.most_common),
      allah_medyan, allah_ort, oncesi_allah/sonrasi_allah (yön),
      ornekler [(key, mesafe)], ozet (okunur metin)
    """
    ak, allah = _akis()
    idx = _hedef_indeksler(kok=kok, kavram_ad=kavram_ad)
    ad = kavram_ad or kok
    if not idx:
        return {'ad': ad, 'gecis': 0, 'ozet': "%s: geçiş bulunamadı" % ad}

    # A) komşuluk bandı — Allah + hedef hariç. Toplam komşu-penceresi kelime sayısı.
    once, sonra = Counter(), Counter()
    hedef_set = set(idx)
    komsu_toplam = 0
    for ti in idx:
        for d in range(1, W + 1):
            for sgn, cnt in ((-1, once), (1, sonra)):
                j = ti + sgn * d
                if 0 <= j < len(ak) and ak[j]['kok'] and not ak[j]['is_allah'] and j not in hedef_set:
                    cnt[_kavram_at(ak[j])] += 1
                    komsu_toplam += 1

    # A2) ZENGİNLEŞME: bir kavram komşulukta, genel sıklığından ne kat fazla?
    # oran = (komşulukta_pay) / (genel_pay). >1.5 = anlamlı zenginleşme.
    def zenginlik(counter):
        out = []
        for k, n in counter.items():
            if not k or n < 3: continue          # gürültü eşiği
            komsu_pay = n / max(1, komsu_toplam)
            genel_pay = _GENEL.get(k, 1) / _TOPLAM
            kat = komsu_pay / genel_pay if genel_pay else 0
            out.append((kat, k, n))
        out.sort(reverse=True)
        return out
    once_z = zenginlik(once)      # dolgu kelimeleri (كون/قول) elenir, gerçek imza kalır
    sonra_z = zenginlik(sonra)

    # B) Allah-ekseni mesafesi + yön + RASTGELE REFERANSA göre etiket
    mes, once_allah, sonra_allah = [], 0, 0
    for ti in idx:
        pos = bisect.bisect_left(allah, ti)
        cand = []
        if pos < len(allah): cand.append(allah[pos])
        if pos > 0: cand.append(allah[pos - 1])
        if not cand: continue
        yakin = min(cand, key=lambda a: abs(a - ti))
        d = ti - yakin
        mes.append(abs(d))
        if d > 0: sonra_allah += 1
        else: once_allah += 1
    mes.sort()
    medyan = mes[len(mes)//2] if mes else -1
    ort = sum(mes)/len(mes) if mes else -1
    # referansa göre etiket (rastgele ~10 kelime)
    if medyan < 0: etiket = "?"
    elif medyan <= _RAST_MED * 0.5: etiket = "YAKIN (yapışık)"
    elif medyan <= _RAST_MED * 0.85: etiket = "yakın"
    elif medyan < _RAST_MED * 1.3: etiket = "nötr (rastgele civarı)"
    else: etiket = "UZAK (çeperde)"

    # örneklem güven uyarısı
    if len(idx) < 15: guven = "⚠ çok küçük örneklem (n<15) — eğilim, kesin değil"
    elif len(idx) < 40: guven = "⚠ küçük örneklem (n<40) — dikkatli yorumla"
    else: guven = ""

    # C) örnekler
    ornek, gor = [], set()
    for ti in idx:
        key = ak[ti]['key']
        if key in gor: continue
        gor.add(key); ornek.append(key)
        if len(ornek) >= ornek_n: break

    # özet metin — zenginleşmeye göre (dolgu elendi)
    def fmt_z(zs): return ', '.join("%s(×%.1f)" % (k, kat) for kat, k, n in zs[:6])
    ozet = ("◆ %s (%d geçiş) %s\n"
            "   ÖNCESİ (zenginleşme):  %s\n"
            "   SONRASI (zenginleşme): %s\n"
            "   Allah'a medyan: %d kelime → %s  [rastgele ref: %d]\n"
            "   yön: %d önce / %d sonra"
            % (ad, len(idx), guven, fmt_z(once_z), fmt_z(sonra_z),
               medyan, etiket, _RAST_MED, once_allah, sonra_allah))
    if meal:
        ozet += "\n   örnekler:"
        for key in ornek[:3]:
            ozet += "\n     %d:%d %s" % (key[0], key[1], meal.get("%d:%d" % key, '')[:60])

    return {
        'ad': ad, 'gecis': len(idx),
        'oncesi_ham': once.most_common(10), 'sonrasi_ham': sonra.most_common(10),
        'oncesi_zengin': once_z[:8], 'sonrasi_zengin': sonra_z[:8],
        'allah_medyan': medyan, 'allah_ort': round(ort, 1), 'allah_etiket': etiket,
        'rastgele_ref': _RAST_MED, 'guven': guven,
        'oncesi_allah': once_allah, 'sonrasi_allah': sonra_allah,
        'ornekler': ornek, 'ozet': ozet,
    }

def anlamlilik(kok=None, kavram_ad=None, deneme=1000):
    """Kavramın Allah-mesafesi rastgeleden anlamlı mı sapıyor?
    Örneklem-boyutunu hesaba katan permütasyon testi. Dönen: (medyan, p, yon, anlamli)."""
    ak, allah = _akis()
    idx = _hedef_indeksler(kok=kok, kavram_ad=kavram_ad)
    if not idx: return (-1, 1.0, '?', False)
    def med(ii):
        mes = []
        for ti in ii:
            pos = bisect.bisect_left(allah, ti); c = []
            if pos < len(allah): c.append(allah[pos])
            if pos > 0: c.append(allah[pos-1])
            if c: mes.append(abs(ti - min(c, key=lambda a: abs(a-ti))))
        mes.sort()
        return mes[len(mes)//2] if mes else -1
    gm = med(idx)
    yon = 'yakin' if gm < _RAST_MED else 'uzak'
    tum = [x['i'] for x in ak if x['kok']]
    random.seed(0)
    dag = [med(random.sample(tum, len(idx))) for _ in range(deneme)]
    if yon == 'yakin': p = sum(1 for x in dag if x <= gm) / len(dag)
    else: p = sum(1 for x in dag if x >= gm) / len(dag)
    return (gm, round(p, 4), yon, p < 0.05)

def gradyan_cetveli(hedefler, W=6):
    """Birçok kavramı Allah-mesafesine göre sıralı cetvel.
    hedefler: [(tur, deger), ...] örn [('kok','حدد'),('kavram','zulüm')]"""
    satir = []
    for tur, deger in hedefler:
        r = dikey_oku(kok=deger if tur == 'kok' else None,
                      kavram_ad=deger if tur == 'kavram' else None, W=W)
        if r['gecis']:
            satir.append((r['allah_medyan'], r['ad'], r['gecis']))
    satir.sort()
    _, _ = _akis()
    out = "ALLAH-EKSENİ GRADYAN CETVELİ (medyan kelime-mesafesi)\n"
    out += "(rastgele referans: %d kelime · < yakın · > uzak)\n\n" % _RAST_MED
    for med, ad, n in satir:
        if med <= _RAST_MED * 0.5: e = "◄ YAKIN"
        elif med < _RAST_MED * 1.3: e = "· nötr"
        else: e = "► UZAK"
        uyari = " ⚠n<40" if n < 40 else ""
        out += "  %-14s %2d kelime  %-8s (%d geçiş)%s\n" % (ad, med, e, n, uyari)
    return out

if __name__ == '__main__':
    import json as _j
    meal = {}
    try:
        m = _j.load(open('/mnt/project/kuran_meal.json', encoding='utf-8'))
        meal = {k: v for k, v in m.items() if isinstance(v, str)}
    except Exception:
        pass
    # tekil test
    print(dikey_oku(kok='طغي', meal=meal)['ozet'])
    print()
    print(dikey_oku(kavram_ad='zulüm', meal=meal)['ozet'])
    print()
    # gradyan cetveli
    print(gradyan_cetveli([
        ('kok','حدد'), ('kok','طغي'), ('kok','صلو'),
        ('kavram','zulüm'), ('kavram','karanlık'),
        ('kok','رحم'), ('kok','عدل'), ('kok','شرك'),
    ]))
