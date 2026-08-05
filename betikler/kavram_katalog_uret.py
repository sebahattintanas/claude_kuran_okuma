"""kavram_katalogu.json üretici.
Her kavram için: hangi kökler, kaç lemma, korpusta kaç geçiş, istisna konumları.
Kaynak: kok_anlam_tablosu.json + kok_anlam_istisna.json + kelime akışı.
Çalıştır: python3 kavram_katalog_uret.py
"""
import json
from collections import defaultdict
from kuran_akis import kelime_akisi, kavram

def uret(cikti='kavram_katalogu.json'):
    tablo = json.load(open('kok_anlam_tablosu.json', encoding='utf-8'))
    ist = json.load(open('kok_anlam_istisna.json', encoding='utf-8'))
    kat = defaultdict(lambda: {'kokler': set(), 'lemmalar': set(),
                               'gecis': 0, 'istisna_konumlari': []})
    # tablodan yapı
    for kok, m in tablo.items():
        for lem, kv in m.items():
            kat[kv]['kokler'].add(kok); kat[kv]['lemmalar'].add(lem)
    # akıştan geçiş sayısı (istisna-farkındalı gerçek çözüm)
    for x in kelime_akisi():
        if not x['kok']: continue
        kv = kavram(x['kok'], x['lem_ham'], x['wid'])
        if kv in kat or kv in ist.values():
            kat[kv]['gecis'] += 1
    # istisna konumları
    for konum, kv in ist.items():
        kat[kv]['istisna_konumlari'].append(konum)
    son = {kv: {'kokler': sorted(v['kokler']), 'lemma_sayisi': len(v['lemmalar']),
                'gecis': v['gecis'], 'istisna_konumlari': sorted(v['istisna_konumlari'])}
           for kv, v in sorted(kat.items(), key=lambda kv: -kv[1]['gecis'])}
    json.dump(son, open(cikti, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    cok_koklu = {k: v['kokler'] for k, v in son.items() if len(v['kokler']) > 1}
    print(f"{len(son)} kavram → {cikti}")
    print(f"birden çok köke yayılan kavram: {len(cok_koklu)}")
    for k, v in list(cok_koklu.items())[:15]: print(f"  {k}: {' '.join(v)}")
    return son

if __name__ == '__main__': uret()
