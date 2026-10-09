# -*- coding: utf-8 -*-
"""
turkce_denetim.py — Arapça terimlerin Türkçe karşılığı denetimi.

OKUMA_STANDARDI biçim kuralı: ölçüm ve mercek metinlerinde geçen HER Arapça
kök adı, hemen ardından parantez içinde Türkçe karşılığıyla verilir.
Bu betik kuralın ihlâllerini listeler. İSTİSNA YOKTUR.

Kullanım:  python3 turkce_denetim.py [sure_no ...]
"""
import json, re, sys, os

KOK = json.load(open('kok_turkce.json', encoding='utf-8'))
ROOTS = set(KOK)
AR = re.compile(r'[\u0621-\u064A]{2,5}')
# kokten hemen sonra Turkce karsilik: (…) veya *(…)* icinde en az 3 latin harf
KARSILIK = re.compile(r'^\s*\*?\(([^)]{2,})\)')  # 2 harflik karşılık da geçerli (ör. 'ev')

def denetle(metin):
    """metin içinde karşılıksız kalan kök adlarını döndürür"""
    eksik = []
    for m in AR.finditer(metin):
        w = m.group()
        if w not in ROOTS:
            continue
        kuyruk = metin[m.end():m.end()+120]
        if not KARSILIK.match(kuyruk):
            eksik.append((w, KOK[w], metin[max(0,m.start()-30):m.end()+30]))
    return eksik

def main():
    d = json.load(open('okuma_metni.json', encoding='utf-8')) if os.path.exists('okuma_metni.json') \
        else json.load(open('../notlar/okuma_metni.json', encoding='utf-8'))
    sureler = sys.argv[1:] or [s for s in d if s.isdigit()]
    top = 0
    for s in sorted(sureler, key=int):
        if s not in d: continue
        ayet_eksik = {}
        for k, v in d[s].items():
            if not k.startswith(s + ':'): continue
            e = []
            for alan in ('olcum', 'mercek', 'dikey', 'derin', 'derin2'):
                e += denetle(v.get(alan, ''))
            if e: ayet_eksik[k] = e
        n = sum(len(v) for v in ayet_eksik.values())
        top += n
        print("sûre %-4s karşılıksız kök anması: %4d  (etkilenen ayet: %d)" % (s, n, len(ayet_eksik)))
        for k in sorted(ayet_eksik, key=lambda x: int(x.split(':')[1]))[:5]:
            kokler = sorted(set(x[0] for x in ayet_eksik[k]))
            print("    %-8s %s" % (k, ' '.join(kokler)))
        if len(ayet_eksik) > 5: print("    … (+%d ayet daha)" % (len(ayet_eksik)-5))
    print("\nTOPLAM karşılıksız kök anması:", top)
    print("kok_turkce.json kapsamı:", len(ROOTS), "kök")
    kap = kapsam(d) if not sys.argv[1:] else 0
    return top + kap

def kapsam(d):
    """İKİNCİ TEST (2026-10-06, sûre 37 oturumu): okunmuş ayetlerde morfolojide geçen ama kok_turkce.json'da
    OLMAYAN kökler. Birinci test yalnız tablodaki kökleri tarar; tabloda olmayan kök ona görünmez (aralık
    oturumunda 145 kök böyle bulundu). Bu test o kör noktayı kapatır."""
    import unicodedata as ud
    yol = next((y for y in ('../veri/morph.txt', 'morph.txt', 'veri/morph.txt') if os.path.exists(y)), None)
    if yol is None:
        print('kapsam testi: morph.txt bulunamadı'); return 1
    okunan = set()
    for s in d:
        if not s.isdigit(): continue
        for k in d[s]:
            m = re.fullmatch(r'(\d+):(\d+)(?:-(\d+))?', k)   # birleşik kayıt anahtarı da (2:11-12)
            if m:
                for a in range(int(m.group(2)), int(m.group(3) or m.group(2)) + 1):
                    okunan.add((int(m.group(1)), a))
    tablo = {ud.normalize('NFC', k) for k in ROOTS}
    eksik = {}
    for l in open(yol, encoding='utf-8'):
        p = l.rstrip('\n').split('\t')
        if len(p) < 4: continue
        m = re.search(r'ROOT:([^|]+)', p[3])
        if not m: continue
        sa = tuple(map(int, p[0].split(':')[:2]))
        r = ud.normalize('NFC', m.group(1))
        if sa in okunan and r not in tablo:
            eksik.setdefault(r, set()).add(sa)
    print("okunan ayette tabloda OLMAYAN kök:", len(eksik), "(okunan ayet: %d)" % len(okunan))
    for r in sorted(eksik)[:10]:
        print("    %s  %s" % (r, ' '.join('%d:%d' % x for x in sorted(eksik[r])[:3])))
    return len(eksik)

if __name__ == '__main__':
    sys.exit(0 if main() == 0 else 1)
