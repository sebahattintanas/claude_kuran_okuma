# -*- coding: utf-8 -*-
"""okuyucu_ornek.py — ters/düz EŞZAMANLI okuyucu örneği (sondan 1–?: sayfa 320 ve 319). Depo kökünden koşulur.
Satır = ayet çifti: sol ters sıra, sağ düz sıra; sayfa içinde ortada buluşur. Meal: Claude çalışma çevirisi (taslak)."""
import json, re, html, unicodedata as ud
N = lambda s: ud.normalize('NFC', s)
h = open('ciktilar/kuran_aralik_sayfalari.html', encoding='utf-8').read()
D = json.loads(h.split('const D=')[1].split(';\nconst T=')[0]); T, P = D['tok'], D['pg']
d = json.load(open('veri/kuran_veri.json', encoding='utf-8'))['sureler']
AR = {(s['no'], a['no']): a['ar_saf'].replace('\ufeff', '') for s in d for a in s['ayetler']}
AD = {s['no']: s['ad'] for s in d}
MEAL = {}
for f in ('betikler/sondan_01_30_uret.py', 'betikler/sondan_31_60_uret.py'):
    src = open(f, encoding='utf-8').read(); g = {}
    exec(src.split('\nMEAL = ')[1].split('\nNOT = ')[0].join(['M = ', '']), g); MEAL.update(g['M'])
MEAL.update({(100,1):"Soluk soluğa koşanlara andolsun,",(100,2):"nallarıyla kıvılcım saçanlara,",(100,3):"sabah vakti baskın yapanlara,",
 (100,4):"orada tozu dumana katanlara,",(100,5):"ve böylece bir topluluğun ortasına dalanlara;",(100,6):"insan Rabbine karşı gerçekten nankördür,",
 (100,7):"ve kendisi buna elbette şahittir,",(100,8):"ve o, mal sevgisine çok düşkündür.",(100,9):"Bilmez mi ki kabirlerde olanlar dışarı saçıldığında,",
 (100,10):"ve göğüslerde olan ortaya çıkarıldığında,",(100,11):"şüphesiz Rableri o gün onlardan tamamen haberdardır.",
 (101,1):"Kapıyı çalan!",(101,2):"Nedir o kapıyı çalan?",(101,3):"Kapıyı çalanın ne olduğunu sana ne bildirdi?",(101,4):"İnsanların yayılmış pervaneler gibi olacağı gün,",
 (101,5):"ve dağların atılmış renkli yün gibi olacağı gün.",(101,6):"Kimin tartıları ağır gelirse,",(101,7):"o hoşnut bir hayat içindedir.",
 (101,8):"Kimin tartıları hafif gelirse,",(101,9):"onun varacağı yer Hâviye'dir.",(101,10):"Onun ne olduğunu sana ne bildirdi?",(101,11):"Kızgın bir ateştir.",
 (102,1):"Çokluk yarışı sizi oyaladı,",(102,2):"ta kabirleri ziyaret edinceye kadar.",(102,3):"Hayır, ileride bileceksiniz!",(102,4):"Yine hayır, ileride bileceksiniz!",
 (102,5):"Hayır, kesin bilgiyle bilseydiniz…",(102,6):"Cehennemi mutlaka göreceksiniz.",(102,7):"Sonra onu kesin bir gözle göreceksiniz.",
 (102,8):"Sonra o gün nimetlerden mutlaka sorguya çekileceksiniz."})
AI = lambda n: ''.join('٠١٢٣٤٥٦٧٨٩'[int(c)] for c in str(n))
def ayet_html(k, bayrak):
    ws = AR[k].split(); out = []; i = 0
    for w in ws:
        if re.search(r'[\u0621-\u064A\u0671]', w):
            b = bayrak[i]; i += 1; cl = []
            if b & 1: cl.append('laf')
            elif b & 32: cl.append('umm')
            else:
                if b & 2: cl.append('rab')
                if b & 4: cl.append('es')
                if b & 16: cl.append('bz')
            if b & 8: cl.append('pas')
            out.append(f'<span class="{" ".join(cl)}">{html.escape(w)}</span>' if cl else html.escape(w))
        else: out.append(f'<span class="dur">{html.escape(w)}</span>')
    assert i == len(bayrak), f'{k} kelime eşleşmedi'
    return ' '.join(out) + f' <span class="vm">﴿{AI(k[1])}﴾</span>'
def sayfa(pi):
    p = P[pi - 1]; vs = []; bay = {}; bas = {}
    for a, b, tip in p:
        for j in range(a, b):
            k = (T[j][0], T[j][1]); bay.setdefault(k, []).append(T[j][3])
            if not vs or vs[-1] != k: vs.append(k)
        k0 = (T[a][0], T[a][1])
        bas.setdefault(k0, []).append((tip, b - a))
    vs = list(dict.fromkeys(vs)); rev = vs[::-1]; n = len(vs)
    lafiz = sum(1 for a, b, _ in p for j in range(a, b) if T[j][3] & 1)
    def hucre(k, onceki):
        ust = []
        if onceki is None or onceki[0] != k[0]: ust.append(f'<span class="sure">{k[0]} · {html.escape(AD[k[0]])}</span>')
        for tip, nw in bas.get(k, []):
            ust.append(f'<span class="ar-et">▸ {"lafızla açılan aralık" if tip == "lafız" else ("sûre başı" if tip == "sûre" else tip)} · {nw} kelime</span>')
        m = MEAL.get(k)
        meal = f'<div class="ml">{html.escape(m)} <span class="tg">taslak</span></div>' if m else '<div class="ml yok">meal yok</div>'
        return (f'<div class="c"><div class="ust"><span class="no">{k[0]}:{k[1]}</span>{"".join(ust)}</div>'
                f'<div class="ar">{ayet_html(k, bay[k])}</div>{meal}</div>')
    rows = []
    for i in range(n):
        rows.append(hucre(rev[i], rev[i - 1] if i else None) + hucre(vs[i], vs[i - 1] if i else None))
        if i == (n - 1) // 2 and n > 1: rows.append('<div class="bul">↕ iki okuma burada buluşuyor</div>')
    a, z = vs[0], vs[-1]
    return (f'<section class="pg"><div class="ph">Sayfa {pi} · {a[0]}:{a[1]} → {z[0]}:{z[1]} · {n} ayet · {lafiz} lafız</div>'
            f'<div class="grid"><div class="hd">Ters (sondan başa)</div><div class="hd">Düz (mushaf)</div>{"".join(rows)}</div></section>')
CSS = '''
:root{box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);
--bg:#fbfaf6;--fg:#1d1b16;--mut:#77715f;--ln:#e6e1d4;--card:#fff;--acc:#8a5a00;--laf:#b4471f;--lafbg:#fbe9e1;--rab:#0f6e56;--es:#534ab7;--bz:#185fa5;--pas:#5f5e5a}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#14130f;--fg:#ece8dc;--mut:#a39d8c;--ln:#302d27;--card:#1c1b16;--acc:#e0b45a;--laf:#f0997b;--lafbg:#4a1b0c;--rab:#5dcaa5;--es:#afa9ec;--bz:#85b7eb;--pas:#b4b2a9}}
:root[data-theme="dark"]{--bg:#14130f;--fg:#ece8dc;--mut:#a39d8c;--ln:#302d27;--card:#1c1b16;--acc:#e0b45a;--laf:#f0997b;--lafbg:#4a1b0c;--rab:#5dcaa5;--es:#afa9ec;--bz:#85b7eb;--pas:#b4b2a9}
html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
main{max-width:1100px;margin:0 auto;padding:10px}
h1{font-size:1.1rem;margin:.3rem 0}.mut{color:var(--mut);font-size:.82rem;margin:.2rem 0 .6rem}
.tb{position:sticky;top:env(safe-area-inset-top,0px);z-index:3;background:var(--bg);padding:6px 0;border-bottom:1px solid var(--ln);display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:.82rem}
.tb label{display:flex;gap:4px;align-items:center;border:1px solid var(--ln);border-radius:999px;padding:3px 10px;background:var(--card);cursor:pointer}
.pg{margin:14px 0 26px}.ph{font-size:.85rem;color:var(--acc);font-weight:600;margin:0 0 6px}
.grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);border:1px solid var(--ln);border-radius:12px;overflow:hidden;background:var(--card)}
.hd{position:sticky;top:calc(env(safe-area-inset-top,0px) + 40px);z-index:2;background:var(--card);font-size:.78rem;font-weight:600;color:var(--mut);padding:6px 10px;border-bottom:1px solid var(--ln)}
.hd+.hd,.c:nth-child(even){border-left:1px solid var(--ln)}
.c{padding:8px 10px 10px;border-bottom:1px solid var(--ln);min-width:0}
.ust{display:flex;flex-wrap:wrap;gap:4px 8px;align-items:center;font-size:.72rem;color:var(--mut);margin-bottom:2px}
.no{font-variant-numeric:tabular-nums;font-weight:600}.sure{color:var(--acc)}.ar-et{color:var(--laf)}
.ar{font-family:"Amiri Quran","Amiri","Traditional Arabic",serif;font-size:1.45rem;line-height:2.15;direction:rtl;text-align:right}
.ml{font-size:.86rem;line-height:1.45;margin-top:2px}.ml.yok{color:var(--mut);font-style:italic}
.tg{font-size:.65rem;color:var(--mut);border:1px solid var(--ln);border-radius:4px;padding:0 4px;vertical-align:1px}
.vm{color:var(--mut);font-size:.8em}.dur{color:var(--mut)}
.laf{color:var(--laf);background:var(--lafbg);border-radius:4px;padding:0 2px}
.umm{color:var(--laf)}
body.r .rab{color:var(--rab);font-weight:700}
body.e .es{color:var(--es);text-decoration:underline dotted 2px;text-underline-offset:6px}
body.b .bz{color:var(--bz)}
body.p .pas{text-decoration:underline dashed var(--pas) 1.5px;text-underline-offset:7px}
.bul{grid-column:1/-1;text-align:center;font-size:.75rem;color:var(--acc);padding:4px;background:var(--bg);border-bottom:1px solid var(--ln)}
@media (max-width:600px){main{padding:6px}.ar{font-size:1.12rem;line-height:1.95}.ml{font-size:.76rem}.c{padding:6px 7px 8px}.hd{padding:5px 7px}}
'''
SAY = [320, 319]
H = (f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
     f'<title>Ters ↔ düz eşzamanlı okuyucu · örnek</title><link href="https://fonts.googleapis.com/css2?family=Amiri+Quran&family=Amiri&display=swap" rel="stylesheet"><style>{CSS}</style></head><body><main>'
     '<h1>Ters ↔ düz eşzamanlı okuyucu · örnek (sayfa 320 ve 319)</h1>'
     '<p class="mut">Her satır bir ayet çifti: solda ters sıra, sağda mushaf sırası; tek kaydırma, sayfanın ortasında buluşurlar. Sayfa = lafız-çapalı blok (≥200 kelime; mushafın son sayfası 136). Meal: Claude\'un çalışma çevirisi, taslak (Diyanet meali değildir; sûre 100–114 henüz okunmadı). Lafız varsayılan vurgu; diğer işaretler otomatik ve doğrulanmamış.</p>'
     '<div class="tb"><span>İşaretler:</span>'
     '<label><input type="checkbox" data-c="r">Rab</label><label><input type="checkbox" data-c="e">esmâ?</label>'
     '<label><input type="checkbox" data-c="b">1P?</label><label><input type="checkbox" data-c="p">edilgen</label></div>'
     + ''.join(sayfa(x) for x in SAY) +
     '</main><script>document.querySelectorAll(".tb input").forEach(i=>i.onchange=()=>document.body.classList.toggle(i.dataset.c,i.checked));</script></body></html>')
open('ciktilar/okuyucu_ornek_sondan.html', 'w', encoding='utf-8').write(H)
print('ok', len(H))
