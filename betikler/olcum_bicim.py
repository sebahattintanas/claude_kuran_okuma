# -*- coding: utf-8 -*-
"""olcum_bicim.py — blok betiklerinin ölçüm (›) satırını defter.json'dan üretir.

Ölçüm satırı ELLE YAZILMAZ: bütün sayılar defterden okunur, kök anmaları
kok_turkce.json'dan otomatik gloss geçişinden geçer (turkce_denetim.py şartı).
Yorum (◇) ayrı tutulur ve blok betiğinde elle yazılır.
"""
import json, collections, os

_KOK = None
_IX = None
_AKIS = None


def _yukle():
    global _KOK, _IX, _AKIS
    if _IX is not None:
        return
    for p in ('defter.json', '../ciktilar/defter.json'):
        if os.path.exists(p):
            _IX = {tuple(r['k']): r for r in json.load(open(p, encoding='utf-8'))}
            break
    for p in ('kok_turkce.json', '../tablolar/kok_turkce.json'):
        if os.path.exists(p):
            _KOK = json.load(open(p, encoding='utf-8'))
            break
    import kuran_akis
    _AKIS = kuran_akis.kelime_akisi()


def _gloss(k):
    """kök anması → kök *(Türkçe karşılık)* — ELLE YAZILMAZ."""
    return "%s *(%s)*" % (k, _KOK.get(k, '???'))


ROMEN = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI',
         '7': 'VII', '8': 'VIII', '9': 'IX', '10': 'X', '11': 'XI', '12': 'XII'}


def _tr(d, ayirac=' · '):
    return ayirac.join('%s %d' % (a, b) for a, b in sorted(d.items()))


def _bab(d):
    return ' · '.join('%s. bab ×%d' % (ROMEN.get(a, a), b)
                      for a, b in sorted(d.items(), key=lambda x: int(x[0])))


def olcum(s, a, ek=''):
    """s:a ayetinin ölçüm satırını döndürür."""
    _yukle()
    r = _IX[(s, a)]
    P = []

    # eksen
    if r['A']:
        P.append('**ALLAH LAFZI** %s. sırada (%d token, allah z=%s)'
                 % (', '.join(str(x) for x in r['A']), len(r['A']), ('%.2f' % r['z']['allah']).replace('.', ','))) \
            if len(r['A']) > 1 else P.append('**ALLAH LAFZI** %d. sırada (allah z=%s)'
                                             % (r['A'][0], ('%.2f' % r['z']['allah']).replace('.', ',')))
    if r['R']:
        P.append('**رَبّ** %s. sırada (rab z=%s)'
                 % (', '.join(str(x[0]) for x in r['R']), ('%.2f' % r['z']['rab']).replace('.', ',')))
    if not r['A'] and not r['R']:
        P.append('**lafız YOK · Rab YOK**')

    # esmâ
    if r['esma']:
        ek_ = []
        for pos, e in r['esma']:
            konum = 'ORTA' if (r['esma_k'] and e in (r['esma_k']['orta'] or [])) else 'SON'
            ek_.append('%s %d. sırada, %s konum, %s'
                       % (e, pos, konum, 'MÜHÜR' if (r['esma_k'] and r['esma_k']['muhur']) else 'MÜHÜRSÜZ'))
        P.append('esmâ ' + ' | '.join(ek_))
    else:
        P.append('esmâ yok')

    # aktör
    ak = []
    for pos, ad, tip in r['adli2']:
        ak.append('adlı %s %d. sırada (%s, rol %s)' % (ad, pos, tip, '+'.join(r['rol'].get(ad, []) or ['—'])))
    for pos, et in r['adsiz2']:
        ak.append('adsız `%s` %d. sırada' % (et, pos))
    P.append('aktör: ' + ' · '.join(ak) if ak else 'aktör yok')

    # edim / kip / biçim
    P.append('edim ' + (', '.join(r['edim']) if r['edim'] else 'haber')
             + (', kip ' + _tr(r['kip'], ' · ') if r['kip'] else ', kip yok')
             + (', **biçim %s**' % ' + '.join(r['fig']) if r['fig'] else ''))

    # şahıs
    P.append('şahıs %s, sahset %s, baskın %s, iltifât %d'
             % (_tr(r['sah']) if r['sah'] else 'işaret yok',
                r['sahset'] or '—', r['bask'] or '—', r['ilt']))

    # ölçü
    P.append('n=%d (n z=%s), fâsıla %s → %s, %s sınıfı%s'
             % (r['n'], ('%.2f' % r['z']['n']).replace('.', ','), r['fs'][0], r['fs'][1], r['fs'][2],
                ' — **KAFİYE KIRILMASI**' if r['z']['kafiye_kirik'] else ''))
    P.append('i\u2019râb ' + (_tr(r['irab']) if r['irab'] else '—')
             + '; bab ' + (_bab(r['vf']) if r['vf'] else 'yok')
             + '; zaman ' + (_tr(r['zmn']) if r['zmn'] else 'yok'))

    tf = sum(r['vf'].values())
    if r['pas']:
        P.append('**EDİLGEN %d/%d fiil, pas z=%s**'
                 % (r['pas'], tf, ('%.2f' % r['z']['pas']).replace('.', ',')))
    if r['hapaks']:
        P.append('**HAPAKS: %s — hapaks z=%s**'
                 % (', '.join(_gloss(k) for k in r['hapaks']),
                    ('%.2f' % r['z']['hapaks']).replace('.', ',')))
    if r['ikile']:
        P.append('kök ikilemesi ' + ' · '.join('%s ×%d' % (_gloss(k), v) for k, v in sorted(r['ikile'].items())))
    if r['mm2']:
        P.append('**mm2: ' + ' · '.join('[%d, %s]' % (p, _gloss(k)) for p, k in r['mm2']) + '**')
    if r['say']:
        P.append('sayı işareti ' + ', '.join(x[1] for x in r['say']))
    if r['sim']:
        P.append('simetri %s' % (r['sim'],))
    P.append('harf %d → **harf3 %d**, isaret %d' % (r['harf'], r['harf3'], r['isaret']))
    P.append('dış düğüm %d%s%s · **yıldız %s**'
             % (r['dugum']['dis'],
                ' · İÇ düğüm %d' % r['dugum']['ic'] if r['dugum']['ic'] else '',
                ' · nakarat %d (temsil %s)' % (r['dugum']['nakarat'], r['dugum']['temsil'])
                if r['dugum']['nakarat'] else '',
                '★' * r['yildiz'] if r['yildiz'] else 'yok'))

    # kökler — sûre içi geçiş sayacıyla
    sk = collections.defaultdict(list)
    bu = []
    for x in _AKIS:
        ss, aa = x['key']
        if ss != s or not x['kok']:
            continue
        sk[x['kok']].append(aa)
        if aa == a and x['kok'] not in bu:
            bu.append(x['kok'])
    kl = []
    for k in bu:
        occ = sk[k]
        idx = [i + 1 for i, y in enumerate(occ) if y == a]
        kl.append('%s [%s/%d]' % (_gloss(k), ','.join(str(i) for i in idx), len(occ)))
    P.append('kökler ' + (' · '.join(kl) if kl else '—'))

    # bağ
    bg = []
    if r['esit2']:
        bg.append('**esit2 → ' + ' · '.join('%d:%d oran %s kademe %s'
                                            % (x[0], x[1], ('%.4f' % x[2]).replace('.', ','), x[3].upper())
                                            for x in r['esit2']) + '**')
    if r['nakarat2']:
        for ng, cnt, tip in r['nakarat2']:
            w = len(ng.split())
            bg.append('`nakarat2` %r (%d kelime / %d ayet, tür %s) → süzgeç **%s**'
                      % (ng, w, cnt, tip, 'GEÇER' if (cnt >= 3 or w >= 4) else 'GEÇMEZ'))
    if r['xref']:
        bg.append('xref ' + ' · '.join('%s → %s' % (g, ', '.join('%d:%d' % tuple(h) for h in hs))
                                       for g, hs in r['xref']))
    P.append('bağ: ' + (' | '.join(bg) if bg else 'YOK (esit2, nakarat2, xref üçü de boş)'))

    if ek:
        P.append(ek)
    return 'eksen: ' + ' · '.join(P)
