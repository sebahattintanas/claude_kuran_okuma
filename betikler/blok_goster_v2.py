# -*- coding: utf-8 -*-
"""blok_goster_v2.py — blok_goster.py'nin SUNUM sürümü (2026-10-04 biçim kararı; v1 silinmez, değişmez).
Ölçüm ve dikey İÇERİĞİ v1 ile aynı kaynaktan gelir (olcum_bicim, blok_dikey_S_A_B.json); yalnız yerleşim değişir:
  ## Arapça · **meal** · › ölçüm · ◇ mercek · ◈K ◈B ◈D ◈A (ayrı satırlar) · ▽ dikey: kök başına markdown tablosu.
Dikey açıklama paragrafı blok başında BİR kez basılır. Hiçbir dikey alan düşmez.
Kullanım: python3 blok_goster_v2.py S A1 A2 metin_modulu [--html yol.html]
Arapça sabit YOK (besmele korpustan türetilir)."""
import sys, json, importlib, re, html as _h, unicodedata as _ud

ARGS = [a for a in sys.argv[1:] if not a.startswith('--')]
HTML_YOL = None
if '--html' in sys.argv:
    HTML_YOL = sys.argv[sys.argv.index('--html') + 1]
    ARGS = [a for a in ARGS if a != HTML_YOL]
S, A1, A2, MOD = int(ARGS[0]), int(ARGS[1]), int(ARGS[2]), ARGS[3]

import olcum_bicim
T = importlib.import_module(MOD)
veri = json.load(open('kuran_veri.json', encoding='utf-8'))
AR = {(s['no'], a['no']): a['ar'] for s in veri['sureler'] for a in s['ayetler']}


def _isk(w):
    w = re.sub(r'[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]', '', _ud.normalize('NFC', w))
    return w.replace('\u0671', '\u0627').replace('\ufeff', '')


BESMELE = [_isk(w) for w in AR[(1, 1)].split()[:4]]
DIK = json.load(open(f'blok_dikey_{S}_{A1}_{A2}.json', encoding='utf-8'))


def arapca(n):
    ar = AR[(S, n)]
    if n == 1 and S not in (1, 9):
        t = ar.split()
        if [_isk(w) for w in t[:4]] == BESMELE:
            ar = ' '.join(t[4:])
    return ar


# ---- dikey ayrıştırma (v1 satırını tabloya böler; geri birleştirme ile kayıpsızlık sınanır) ----
KOK_RE = re.compile(r'^  · (?P<bas>.*?) n=(?P<n>\d+)(?P<uy> ⚠)?  ▸önce: (?P<once>.*?)  ▸sonra: (?P<sonra>.*?)  ▸Allah med=(?P<med>-?\d+)$')
KOM_RE = re.compile(r'^(?P<ad>.*?) ×(?P<kat>[0-9.]+)(?: \[(?P<kad>[^\]]*)\])?$')


def komsular(s):
    if s == '—':
        return []
    out = []
    for p in s.split(' · '):
        m = KOM_RE.match(p)
        if not m:
            raise ValueError('komşu ayrıştırılamadı: ' + p)
        out.append((m['ad'], m['kat'], m['kad']))
    return out


def kom_dizge(ks):
    if not ks:
        return '—'
    return ' · '.join(f'{a} ×{k}' + (f' [{d}]' if d else '') for a, k, d in ks)


def dikey_ayristir(metin):
    """-> (aciklama, [satir dict]) ; her satır geri birleştirildiğinde özgünle birebir aynı olmalı."""
    ls = metin.split('\n')
    acik, sat = ls[0], []
    for l in ls[1:]:
        m = KOK_RE.match(l)
        if not m:
            raise ValueError('dikey satır ayrıştırılamadı: ' + l)
        d = dict(bas=m['bas'], n=int(m['n']), uy=bool(m['uy']),
                 once=komsular(m['once']), sonra=komsular(m['sonra']), med=int(m['med']))
        geri = '  · %s n=%d%s  ▸önce: %s  ▸sonra: %s  ▸Allah med=%d' % (
            d['bas'], d['n'], ' ⚠' if d['uy'] else '', kom_dizge(d['once']), kom_dizge(d['sonra']), d['med'])
        if geri != l:
            raise ValueError('kayıpsız değil: ' + l)
        sat.append(d)
    return acik, sat


def md_kom(ks):
    if not ks:
        return '—'
    return '<br>'.join(f'{a} ×{k}' + (f' [{d}]' if d else '') for a, k, d in ks)


def mercek_satirlari(m):
    # ◇ metnini ◈K/◈B/◈D/◈A önünden böl; satır içeriği değişmez
    parcalar = re.split(r'\s*(?=◈[KBDA] —)', m.strip())
    return [p.strip() for p in parcalar if p.strip()]


AYETLER = []
ACIKLAMA = None
for n in range(A1, A2 + 1):
    d = DIK.get(f'{S}:{n}', '').strip('\n')
    acik, sat = (None, [])
    if d.strip():
        acik, sat = dikey_ayristir(d)
        ACIKLAMA = ACIKLAMA or acik
    AYETLER.append(dict(n=n, ar=arapca(n), meal=T.MEAL[n], olcum=olcum_bicim.olcum(S, n),
                        mercek=mercek_satirlari(T.M[n]), dikey=sat, ham=d))

# ---- sohbet (markdown) çıktısı ----
out = []
if ACIKLAMA:
    out.append('▽ ' + ACIKLAMA + '\n')
for a in AYETLER:
    out.append(f"### {S}:{a['n']}\n")
    out.append('## ' + a['ar'] + '\n')
    out.append(f"**{a['meal']}**\n")
    out.append('› ' + a['olcum'] + '\n')
    for s in a['mercek']:
        out.append(s + '\n')
    if a['dikey']:
        out.append('▽ dikey\n')
        out.append('| kök | n | önce (×kat [kademe]) | sonra (×kat [kademe]) | Allah med |')
        out.append('|---|---|---|---|---|')
        for d in a['dikey']:
            out.append('| %s | %d%s | %s | %s | %d |' % (d['bas'].replace('|', '/'), d['n'], ' ⚠' if d['uy'] else '',
                                                    md_kom(d['once']), md_kom(d['sonra']), d['med']))
        out.append('')
    else:
        out.append('▽ (bu ayette dikey satır yok)\n')
print('\n'.join(out))

# ---- HTML ----
if HTML_YOL:
    E = _h.escape

    def gloss_html(s):
        # *(...)* → <i>(...)</i>
        return re.sub(r'\*(\(.*?\))\*', r'<i>\1</i>', E(s))

    def kom_html(ks):
        if not ks:
            return '—'
        return '<br>'.join(gloss_html(a) + f' <b>×{k}</b>' + (f' <span class="kad">[{E(d)}]</span>' if d else '')
                           for a, k, d in ks)

    gov = []
    if ACIKLAMA:
        gov.append(f'<p class="acik">▽ {E(ACIKLAMA)}</p>')
    for a in AYETLER:
        gov.append(f'<section id="a{a["n"]}"><h3>{S}:{a["n"]}</h3>')
        gov.append(f'<p class="ar" dir="rtl" lang="ar">{E(a["ar"])}</p>')
        gov.append(f'<p class="meal"><b>{E(a["meal"])}</b></p>')
        gov.append(f'<p class="olcum">› {E(a["olcum"])}</p>')
        for s in a['mercek']:
            cls = 'mercek' if s.startswith('◇') else 'ek'
            gov.append(f'<p class="{cls}">{E(s)}</p>')
        if a['dikey']:
            gov.append('<div class="tk"><table><thead><tr><th>kök</th><th>n</th><th>önce</th><th>sonra</th><th>Allah med</th></tr></thead><tbody>')
            for d in a['dikey']:
                gov.append(f'<tr><td>{gloss_html(d["bas"])}</td><td>{d["n"]}{" ⚠" if d["uy"] else ""}</td>'
                           f'<td>{kom_html(d["once"])}</td><td>{kom_html(d["sonra"])}</td><td>{d["med"]}</td></tr>')
            gov.append('</tbody></table></div>')
        else:
            gov.append('<p class="ek">▽ (bu ayette dikey satır yok)</p>')
        gov.append('</section>')
    sayfa = f'''<!DOCTYPE html>
<html lang="tr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{S}:{A1}-{A2} okuma</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Amiri+Quran&family=Amiri&display=swap" rel="stylesheet">
<style>
:root{{--bg:#fbf8f1;--fg:#1d1b16;--soft:#6b6457;--line:#ddd4c2;--acc:#7a4b12;--card:#fffdf8;--th:#f1ead9;
 box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#16140f;--fg:#ece5d6;--soft:#a69d8c;--line:#3a352b;--acc:#e0b26a;--card:#1e1b15;--th:#2a261e}}}}
:root[data-theme="dark"]{{--bg:#16140f;--fg:#ece5d6;--soft:#a69d8c;--line:#3a352b;--acc:#e0b26a;--card:#1e1b15;--th:#2a261e}}
html{{scroll-padding-top:env(safe-area-inset-top,0px)}}
body{{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}}
main{{max-width:920px;margin:0 auto;padding:16px}}
h1{{font-size:1.2rem;color:var(--acc)}} h3{{margin:0 0 .4rem;color:var(--acc);font-size:1.05rem}}
section{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:18px 0}}
.ar{{font-family:'Amiri Quran','Amiri','Traditional Arabic','Scheherazade New',serif;font-size:32px;line-height:2.4;text-align:right;margin:.2rem 0 .6rem}}
.meal{{font-size:1.05rem}} .olcum{{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.82rem;color:var(--soft);word-break:break-word}}
.mercek{{border-left:3px solid var(--acc);padding-left:10px}} .ek{{padding-left:13px;color:var(--fg)}}
.acik{{font-size:.85rem;color:var(--soft)}}
.tk{{overflow-x:auto}} table{{border-collapse:collapse;width:100%;font-size:.85rem}}
th,td{{border:1px solid var(--line);padding:5px 7px;vertical-align:top;text-align:left}} th{{background:var(--th)}}
td:first-child{{min-width:9em}} .kad{{color:var(--soft)}}
</style></head><body><main>
<h1>Sûre {S} · {A1}-{A2} — blok okuması</h1>
{chr(10).join(gov)}
</main></body></html>'''
    open(HTML_YOL, 'w', encoding='utf-8').write(sayfa)
    print(f'[html yazıldı: {HTML_YOL}]', file=sys.stderr)
