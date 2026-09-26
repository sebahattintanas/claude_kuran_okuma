# -*- coding: utf-8 -*-
"""blok_bilanco.py — blok bilançosunun SAYILAN kısmı. Her sayı defterden/kayıttan koşulur.

bilanco(S, a, b) → dict. Elle yazılan sayı YOK (aday 843/964 ailesi: hafızadan sayım yasağı).
Okuyucu kararları (çıpa kademesi, alan arızaları) buraya girmez; onlar <sure>_kayit.py'de.
"""
import json
from collections import Counter

_D = None
def _defter():
    global _D
    if _D is None:
        _D = {tuple(r['k']): r for r in json.load(open('defter.json', encoding='utf-8'))}
    return _D

def yildiz_kaynagi(r):
    """22_hapaks_onarim.py formülünün tersi: ★'ı hangi bileşen verdi, eşiği geçen başka hangileri var."""
    z = {k: v for k, v in r['z2'].items() if k != 'kafiye_kirik'}
    m = max(z, key=lambda k: abs(z[k]))
    return {'kaynak': m, 'z': round(z[m], 2),
            'esigi_gecen_diger': {k: round(v, 2) for k, v in z.items() if k != m and abs(v) > 1.5},
            'kafiye_kirik': bool(r['z2'].get('kafiye_kirik'))}

def _muhur_gecerli(key, x):
    """§4.3 mührü, son-üç içindeki esmâ tokenlerinden en az biri okuyucu kararında 'ilahi' ise geçerli."""
    if not x.get('muhur'): return False
    return any(x['esma_el'].get('%s:%d' % (key, w)) == 'ilahi'
               for w, L in x['son3'] if L in x['muhur_lem'])

def bilanco(S, a, b):
    D = _defter()
    B = [D[(S, n)] for n in range(a, b + 1)]
    E = json.load(open('esma_kayit.json', encoding='utf-8'))
    T = json.load(open('cipa_tarama4_adaylari.json', encoding='utf-8'))
    tar = [x['ayet'] for x in T if x['ayet'] in {'%d:%d' % (S, n) for n in range(a, b + 1)}]
    ek = [E['%d:%d' % (S, n)] for n in range(a, b + 1) if '%d:%d' % (S, n) in E]
    return {
     'etiket': 'TAM SAYIM — defter.json / esma_kayit.json / cipa_tarama4_adaylari.json',
     'ayet': len(B),
     'kelime_toplam': sum(r['n'] for r in B),
     'lafiz_token': sum(len(r['A']) for r in B),
     'lafiz_ayet': sum(1 for r in B if r['A']),
     'rab_token': sum(len(r['R']) for r in B),
     'edilgen_ayet': [r['k'][1] for r in B if r['pas']],
     'iltifat_ayet': [r['k'][1] for r in B if r['ilt']],
     'kafiye_kirik_ayet': [r['k'][1] for r in B if r['z2'].get('kafiye_kirik')],
     'hapaks2': {str(r['k'][1]): r['hapaks2'] for r in B if r['hapaks2']},
     'yildiz_dagilim': {str(k): v for k, v in sorted(Counter(r['yildiz2'] for r in B).items())},
     'yildiz_kaynak': {str(r['k'][1]): dict(yildiz=r['yildiz2'], **yildiz_kaynagi(r)) for r in B if r['yildiz2']},
     'mm2_ayet': [r['k'][1] for r in B if r['mm2']],
     'nakarat3_ayet': [r['k'][1] for r in B if r['nakarat3']],
     'say_isareti': {str(r['k'][1]): [x[1] for x in r['say']] for r in B if r['say']},
     'esma_token_oto': sum(len(x['esma']) for x in ek),
     'esma_sinif_oto': dict(Counter(x['sinif_oto'] for x in ek)),
     'esma_sinif_el': dict(Counter(x['sinif_el'] for x in ek)),
     'esma_muhur_43': [int(k.split(':')[1]) for k in ('%d:%d' % (S, n) for n in range(a, b + 1)) if E.get(k, {}).get('muhur')],
     'esma_muhur_43_gecerli': [int(k.split(':')[1]) for k in ('%d:%d' % (S, n) for n in range(a, b + 1))
                               if _muhur_gecerli(k, E.get(k, {}))],
     'tarayici_v4_aday': tar,
    }

if __name__ == '__main__':
    import sys
    print(json.dumps(bilanco(*map(int, sys.argv[1:4])), ensure_ascii=False, indent=1))
