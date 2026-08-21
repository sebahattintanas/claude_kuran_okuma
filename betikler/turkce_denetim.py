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
            for alan in ('olcum', 'mercek'):
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
    return top

if __name__ == '__main__':
    sys.exit(0 if main() == 0 else 1)
