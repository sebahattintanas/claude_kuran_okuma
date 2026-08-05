# -*- coding: utf-8 -*-
"""
kuran_akis.py — Kur'an kelime-akışı ve kavram çözümleme çekirdek modülü
Tek doğru yer: morph.txt'ten kelime akışı kurma + karışık kök ayrımı.
Her dikey okuma / komşuluk / mesafe analizi buradan beslenir.
"""
import re, json
from collections import defaultdict

def _ciplak(s):
    """TÜM harekeleri sil (şedde dahil) — Allah tespiti gibi şedde-duyarsız eşleştirme için."""
    return re.sub(r'[\u064B-\u0652\u0670\u0651]', '', s)

def dehareke(s):
    """Kısa harekeleri kaldır AMA şedde'yi (\u0651) KORU — şedde anlam ayırıcı
    (كذّب tekzib vs كذب kizb; tef'îl babı). Uzun harekeleri de kaldırır."""
    return re.sub(r'[\u064B-\u0650\u0652\u0670]', '', s)  # şedde hariç

def morph_yolu():
    import os
    for p in ('morph.txt','/mnt/project/morph.txt','/mnt/user-data/uploads/morph.txt'):
        if os.path.exists(p): return p
    raise FileNotFoundError("morph.txt bulunamadı")

def _kelime_segmentleri(morph_path=None):
    """(sure,ayet,kelime) -> [(kök, lemma_ham, POS), ...] segment listesi."""
    path = morph_path or morph_yolu()
    seg = defaultdict(list)
    for L in open(path, encoding='utf-8'):
        p = L.rstrip('\n').split('\t')
        if len(p) < 4: continue
        mm = re.match(r'^(\d+):(\d+):(\d+):(\d+)', p[0])
        if not mm: continue
        wid = (int(mm.group(1)), int(mm.group(2)), int(mm.group(3)))
        r = re.search(r'ROOT:([^\|]+)', p[3])
        l = re.search(r'LEM:([^\|]+)', p[3])
        seg[wid].append((r.group(1) if r else '', l.group(1) if l else '', p[2]))
    return seg

def kelime_akisi(morph_path=None):
    """
    Kur'an'ı sıralı kelime akışı olarak döndürür.
    Her kelime = benzersiz (sure,ayet,kelime_pos); anlamı, o kelimenin
    asıl segmentinden (ilk N/V/ADJ/PN) alınır — el-, ve-, fe- önekleri atlanır.
    Dönen: [ {i, wid, key, kok, lem_ham, lem_hsz, pos}, ... ]
    """
    seg = _kelime_segmentleri(morph_path)
    akis = []
    for i, wid in enumerate(sorted(seg.keys())):
        kok = lem = pos = ''
        # asıl anlamlı segment: ROOT'u olan ilk N/V/ADJ/PN
        for r, l, ps in seg[wid]:
            if r and ps in ('N', 'V', 'ADJ', 'PN'):
                kok, lem, pos = r, l, ps; break
        if not kok:  # yoksa ROOT'u olan ilk segment
            for r, l, ps in seg[wid]:
                if r: kok, lem, pos = r, l, ps; break
        lem_h = dehareke(lem)
        akis.append({
            'i': i, 'wid': wid, 'key': (wid[0], wid[1]),
            'kok': kok, 'lem_ham': lem, 'lem_hsz': lem_h, 'pos': pos,
            'is_allah': _ciplak(lem) == _ciplak('الله')
        })
    return akis

# --- Karışık kök ayrımı: kok_anlam_tablosu.json (harakat-duyarlı) ---

_TABLO = None
def _tablo(path='kok_anlam_tablosu.json'):
    global _TABLO
    if _TABLO is None:
        import os
        _TABLO = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else {}
    return _TABLO

_ISTISNA = None
def _istisna(path='kok_anlam_istisna.json'):
    global _ISTISNA
    if _ISTISNA is None:
        import os
        _ISTISNA = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else {}
    return _ISTISNA

def kavram(kok, lem, wid=None, tablo_path='kok_anlam_tablosu.json'):
    """Karışık kökü doğru kavrama çevir. Katmanlı eşleştirme:
    0) AYET-İSTİSNA: wid=(sure,ayet,pos) verilirse kok_anlam_istisna.json
       ("sure:ayet:kelime" → kavram) her şeyden önce bakılır — lemmanın
       yetmediği yerler (بَرّ kara/ebrâr, حَمِيم su/dost ...) burada çözülür
    1) tam-harekeli lemma (بَشَر vs بِشْر, عالِم vs عالَم — kısa-hareke ayrımı)
    2) şedde-korumalı (كذّب vs كذب)
    3) tam harekesiz
    Ayrım yoksa kökü döndür. lem: ham (harekeli) lemma verilmeli."""
    if wid is not None:
        ist = _istisna()
        anahtar = '%s:%s:%s' % (wid[0], wid[1], wid[2])
        if anahtar in ist: return ist[anahtar]
    t = _tablo(tablo_path)
    if kok not in t: return kok
    esl = t[kok]
    sedde = re.sub(r'[\u064B-\u0650\u0652\u0670]', '', lem)      # şedde korumalı
    ciplak = re.sub(r'[\u064B-\u0652\u0670]', '', lem)            # tam çıplak
    for anahtar in (lem, sedde, ciplak):
        if anahtar in esl: return esl[anahtar]
    return kok

def allah_indeksleri(akis):
    return [x['i'] for x in akis if x['is_allah']]

if __name__ == '__main__':
    ak = kelime_akisi()
    n_allah = sum(1 for x in ak if x['is_allah'])
    print("kelime akışı: %d kelime, Allah lafzı: %d" % (len(ak), n_allah))
    print("örnek kavram çözümü:")
    for test in [('ظلم','ظُلُمَة'),('ظلم','ظالِم'),('كذب','كَذَّبَ'),('كذب','كَذِب')]:
        print("  %s + %s → %s" % (test[0], test[1], kavram(test[0], test[1])))
