# -*- coding: utf-8 -*-
"""ters_onluk_sayfa.py — ters okuma (sondan başa) ↔ mushaf düzeni karşılaştırma sayfası (indirilebilir HTML).
Aralık okuması, 2026-10-05. Vurgu kalıpları NFC'ye çevrilerek uygulanır (şedde/hareke sırası hatası iki kez görüldü)."""
import json, html, unicodedata as ud
N = lambda s: ud.normalize('NFC', s)
def sayfa(S, V, K, HL, NOT, baslik, baglam, gozlem, cikti):
    o = json.load(open('notlar/okuma_metni.json', encoding='utf-8'))[str(S)]
    cnt = {}
    for l in open('veri/morph.txt', encoding='utf-8'):
        p = l.split('\t')
        if len(p) < 4 or p[0].count(':') != 3: continue
        s, a, w, _ = map(int, p[0].split(':'))
        if s == S: cnt.setdefault(a, set()).add(w)
    NN = {v: len(cnt[v]) for v in V}
    KAD = {'L': 'lafız', 'E': 'yalnız edilgen', 'B': 'Biz (Tanrı konuşuyor)', 'O': 'O (Tanrıdan söz ediliyor)', 'N': 'taşıyıcı yok'}
    def ar(v):
        t = N(html.escape(o[f'{S}:{v}']['ar'])); n = 0
        for w, c in HL.get(v, []):
            w = N(w)
            if w in t: t = t.replace(w, f'<span class="{c}">{w}</span>', 1); n += 1
        assert n == len(HL.get(v, [])), f'{S}:{v} vurgu eşleşmedi'
        return t
    def cell(v, i, side):
        return (f'<div class="c {side}"><div class="no">{i}. · {S}:{v} · {NN[v]} kelime · <span class="k k{K[v]}">{KAD[K[v]]}</span></div>'
                f'<div class="ar">{ar(v)}</div><div class="tr">{html.escape(o[f"{S}:{v}"]["meal"])}</div><div class="tag">{NOT[v]}</div></div>')
    rev = V[::-1]
    rows = ''.join(cell(rev[i], i + 1, 'l') + cell(V[i], i + 1, 'r') +
                   (f'<div class="bd"><b>Ayna noktası</b> — iki sütun burada kesişiyor: {S}:{rev[i]} ↔ {S}:{V[i]}</div>' if i == len(V) // 2 - 1 else '') for i in range(len(V)))
    strip = lambda seq: '<div class="st">' + ''.join(f'<div class="col"><div class="bar b{K[v]}" style="height:{14 + NN[v] * 6}px">{NN[v]}</div><div class="lb">{v}</div></div>' for v in seq) + '</div>'
    css = open('ciktilar/yasin_36_74_83_ters_mushaf.html', encoding='utf-8').read().split('<style>')[1].split('</style>')[0]
    css += '.bN{background:transparent;color:var(--mut);border:1px dashed var(--ln)}.kN{border:1px dashed var(--ln);color:var(--mut)}'
    H = (f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
         f'<title>{baslik}</title><link href="https://fonts.googleapis.com/css2?family=Amiri+Quran&family=Amiri&display=swap" rel="stylesheet"><style>{css}</style></head><body><main>'
         f'<h1>{baslik}</h1><p class="mut">Sol: sondan başa ({S}:{V[-1]} → {S}:{V[0]}). Sağ: mushaf sırası ({S}:{V[0]} → {S}:{V[-1]}). Meal: okuma kaydındaki çalışma çevirisi (Diyanet meali değildir). Aralık okuması, 2026-10-05.</p>'
         f'<div class="box">{baglam}</div>'
         '<div class="lg"><span><i style="background:var(--L)"></i>lafız</span><span><i style="background:var(--B)"></i>Biz (Tanrı konuşuyor)</span><span><i style="background:var(--O)"></i>O (Tanrıdan söz ediliyor)</span><span><i style="background:var(--E);border:1px solid var(--ln)"></i>yalnız edilgen</span><span><i style="border:1px dashed var(--ln)"></i>taşıyıcı yok</span></div>'
         f'<div class="sl">Mushaf düzeni → (sütun yüksekliği = kelime sayısı)</div>{strip(V)}<div class="sl">Ters okuma ←</div>{strip(rev)}'
         f'<h2>Ayet ayet</h2><div class="grid"><div class="hd">Ters okuma (sondan başa)</div><div class="hd">Mushaf düzeni</div>{rows}</div>'
         f'<div class="box"><b>Gözlemler (okuma, KAPATILAMAZ).</b><br>{gozlem}</div></main></body></html>')
    open(cikti, 'w', encoding='utf-8').write(H)
    return NN
if __name__ == '__main__':
    V = list(range(64, 74))
    K = {64: 'N', 65: 'B', 66: 'B', 67: 'B', 68: 'B', 69: 'B', 70: 'N', 71: 'B', 72: 'B', 73: 'N'}
    HL = {65: [('نَخْتِمُ', 'car'), ('وَتُكَلِّمُنَآ', 'car')], 66: [('نَشَآءُ', 'car'), ('لَطَمَسْنَا', 'car')], 67: [('نَشَآءُ', 'car'), ('لَمَسَخْنَٰهُمْ', 'car')],
          68: [('نُّعَمِّرْهُ', 'car'), ('نُنَكِّسْهُ', 'car')], 69: [('عَلَّمْنَٰهُ', 'car')], 71: [('أَنَّا', 'car'), ('خَلَقْنَا', 'car'), ('أَيْدِينَآ', 'car')], 72: [('وَذَلَّلْنَٰهَا', 'car')]}
    NOT = {64: "Taşıyıcı yok: cehennemliklere emir (ٱصْلَوْهَا, 2MP); konuşan adlandırılmıyor.",
           65: "Biz: ağızları mühürleriz. Organlar konuşuyor — eller BİZE konuşur (تُكَلِّمُنَا), ayaklar şahitlik eder.",
           66: "Biz, şart (لَوْ نَشَآءُ): gözleri silmek.", 67: "Biz, şart (لَوْ نَشَآءُ) ikinci kez: yerinde başka şekle çevirmek.",
           68: "Biz: ömür ver(ir)iz → yaratılışta tersine çeviririz (yaşlanma). أَفَلَا يَعْقِلُونَ.",
           69: "Biz: ona şiir öğretmedik. هُوَ burada Kur'an — Tanrı değil (3MS göndergesi ayrı).",
           70: "Taşıyıcı yok: لِيُنذِرَ'nin öznesi Kur'an/elçi — 3MS ama Tanrıya gitmiyor.",
           71: "Biz: ELLERİMİZin yaptığından davar yarattık — 65'te 'onların elleri', burada 'bizim ellerimiz'.",
           72: "Biz: boyun eğdirdik — binme ve yeme.", 73: "Taşıyıcı yok: faydalar, içecekler — أَفَلَا يَشْكُرُونَ."}
    baglam = ('<b>Aralık bağlamı.</b> Bu on ayette lafız YOK: 36:47 ile 36:74 arasındaki 27 ayetlik aralığın içindeler. '
              'Taşıyıcıların neredeyse hepsi <b>Biz</b> (on ayetin yedisi). İlk onluktaki Biz bloğu (76–78) burada genişliyor: ters okumada Biz sesi 78\'den 65\'e kadar, aralarda üç boşlukla sürüyor.')
    gozlem = ('1. <b>Biz baskın, ama Biz\'in iki modu var:</b> fiilen yapan (65 mühürleriz, 69 öğretmedik, 71 yarattık, 72 boyun eğdirdik) ve şartlı yapabilecek olan (66–67 <i>lev neşâu</i> ×2, 68 ömür ve tersine çevirme).<br>'
              '2. <b>Eller iki sahibe:</b> 65 أَيْدِيهِمْ (onların elleri Bize konuşur) / 71 أَيْدِينَآ (Bizim ellerimizin yaptığı). Aynı organ, iki taraf.<br>'
              '3. <b>3MS her zaman Tanrı değil:</b> 69–70\'te هُوَ ve لِيُنذِرَ Kur\'an\'a/elçiye gidiyor. 3MS sayımı (aday 1027) bu ayetleri yanlışlıkla taşıyıcı sayar.<br>'
              '4. <b>Yön:</b> ileri okumada ceza (64–67) → ömür (68) → vahiy (69–70) → nimet (71–73) → şükür sorusu. Ters okumada nimetten cezaya iniliyor.<br>'
              '5. <b>Biyolog için yoğun:</b> ağız, el, ayak, göz (65–66), yaşlanma (68 نُنَكِّسْهُ), davar, binme, yeme, içme (71–73).')
    print(sayfa(36, V, K, HL, NOT, 'Yâsîn 36:64–73 · ters okuma ↔ mushaf düzeni (ikinci onluk)', baglam, gozlem, 'ciktilar/yasin_36_64_73_ters_mushaf.html'))

def sayfa_genel(KEYS, K, HL, NOT, MEAL, baslik, baglam, gozlem, cikti, meal_notu):
    """Sûre sınırını geçebilen sürüm: KEYS mushaf sırasında (sûre, ayet); Arapça kuran_veri'den, meal dışarıdan."""
    d = json.load(open('veri/kuran_veri.json', encoding='utf-8'))['sureler']
    AR = {k: d[k[0] - 1]['ayetler'][k[1] - 1]['ar_saf'].replace('\ufeff', '') for k in KEYS}
    cnt = {}
    for l in open('veri/morph.txt', encoding='utf-8'):
        p = l.split('\t')
        if len(p) < 4 or p[0].count(':') != 3: continue
        s, a, w, _ = map(int, p[0].split(':'))
        if (s, a) in AR: cnt.setdefault((s, a), set()).add(w)
    NN = {k: len(cnt[k]) for k in KEYS}
    KAD = {'L': 'lafız', 'E': 'yalnız edilgen', 'B': 'Biz', 'O': 'O (3. şahıs)', 'R': 'Rab', 'N': 'taşıyıcı yok'}
    def ar(k):
        t = N(html.escape(AR[k])); n = 0
        for w, c in HL.get(k, []):
            w = N(w)
            if w in t: t = t.replace(w, f'<span class="{c}">{w}</span>'); n += 1
        assert n == len(HL.get(k, [])), f'{k} vurgu eşleşmedi'
        return t
    lab = lambda k: f'{k[0]}:{k[1]}'
    def cell(k, i, side):
        return (f'<div class="c {side}"><div class="no">{i}. · {lab(k)} · {NN[k]} kelime · <span class="k k{K[k]}">{KAD[K[k]]}</span></div>'
                f'<div class="ar">{ar(k)}</div><div class="tr">{html.escape(MEAL[k])}</div><div class="tag">{NOT[k]}</div></div>')
    rev = KEYS[::-1]; n = len(KEYS)
    rows = ''
    for i in range(n):
        if i > 0 and rev[i][0] != rev[i - 1][0] or i == 0:
            pass
        rows += cell(rev[i], i + 1, 'l') + cell(KEYS[i], i + 1, 'r')
        if i == n // 2 - 1: rows += f'<div class="bd"><b>Ayna noktası</b> — iki sütun burada kesişiyor: {lab(rev[i])} ↔ {lab(KEYS[i])}</div>'
    def strip(seq):
        out = []
        for j, k in enumerate(seq):
            yeni = j == 0 or seq[j - 1][0] != k[0]
            out.append(f'<div class="col"{" style=\"border-left:2px solid var(--fg);padding-left:1px\"" if yeni and j else ""}><div class="bar b{K[k]}" style="height:{14 + NN[k] * 5}px"></div><div class="lb">{(str(k[0]) + "<br>") if yeni else "<br>"}{k[1]}</div></div>')
        return '<div class="st" style="height:auto;min-height:90px;gap:2px">' + ''.join(out) + '</div>'
    css = open('ciktilar/yasin_36_74_83_ters_mushaf.html', encoding='utf-8').read().split('<style>')[1].split('</style>')[0]
    css += ('.bN{background:transparent;color:var(--mut);border:1px dashed var(--ln)}.kN{border:1px dashed var(--ln);color:var(--mut)}'
            '.bR{background:#5DCAA5;color:#04342c}.kR{background:#5DCAA5;color:#04342c}.lb{font-size:10px}')
    H = (f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
         f'<title>{baslik}</title><link href="https://fonts.googleapis.com/css2?family=Amiri+Quran&family=Amiri&display=swap" rel="stylesheet"><style>{css}</style></head><body><main>'
         f'<h1>{baslik}</h1><p class="mut">Sol: sondan başa ({lab(KEYS[-1])} → {lab(KEYS[0])}). Sağ: mushaf sırası ({lab(KEYS[0])} → {lab(KEYS[-1])}). {meal_notu} Aralık okuması, 2026-10-05.</p>'
         f'<div class="box">{baglam}</div>'
         '<div class="lg"><span><i style="background:var(--L)"></i>lafız</span><span><i style="background:#5DCAA5"></i>Rab</span><span><i style="background:var(--B)"></i>Biz</span><span><i style="background:var(--O)"></i>O (3. şahıs)</span><span><i style="background:var(--E);border:1px solid var(--ln)"></i>yalnız edilgen</span><span><i style="border:1px dashed var(--ln)"></i>taşıyıcı yok</span></div>'
         f'<div class="sl">Mushaf düzeni → (sütun yüksekliği = kelime sayısı)</div>{strip(KEYS)}<div class="sl">Ters okuma ←</div>{strip(rev)}'
         f'<h2>Ayet ayet</h2><div class="grid"><div class="hd">Ters okuma (sondan başa)</div><div class="hd">Mushaf düzeni</div>{rows}</div>'
         f'<div class="box"><b>Gözlemler (okuma, KAPATILAMAZ).</b><br>{gozlem}</div></main></body></html>')
    open(cikti, 'w', encoding='utf-8').write(H)
    return NN
