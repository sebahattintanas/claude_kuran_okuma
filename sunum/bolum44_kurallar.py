# sûre 7 bölüm 8 kapanış denetimi araç kuralları (bekleyen_ariza_7_b23.txt 2. öğe) — salt okur:
#  (1) GONDERGE_KISI_COGUL: A1'de 3MP / 3FP ek ya da fiil göndergesi ölçümde 'kisi' olarak geçen adlı bir özel ada gidiyorsa kayıtta topluluk notu ('ailesiyle' / 've yanındakiler') bulunur
#  (2) FIIL_UYUMU_CINSIYET: "fiil uyumu; … N. kelime — fail M. kelime" kaydında fiil 3MS iken fail morph F (ya da fiil 3FS iken fail M) ise aynı kayıtta 'mecazi müennes' / 'cinsiyet farkı' notu
#  (3) EMSAL_DEGIL_HARF_NOTU: 'çakışma değil' hükümlü emsal satırının iki Türkçe alıntısı bayt eşit değilse (yalnız harf büyüklüğü farkı) satırda 'harf büyüklüğü' notu
#  (4) EMSAL_FIIL_SATIRI: ◇'de alıntılanan sayımın listelediği her emsal için, sayım alıntısındaki fiil kelimesi (seg fiil maddesi) o emsalin bir satır kalıbında geçer; yoksa maddede "'<fiil>' <emsal> fiil satırı yok" notu
#  (5) EMSAL_ALINTI_TAM: '(emsal metninde)' satırının Arapça kalıbı alıntı ayrıştırıcısıyla bütün okunur (ham kalıp = ayrıştırılan kalıp); kesilen kalıp hata
# kullanım (/home/claude'dan): python3 sunum/bolum44_kurallar.py A B NN
import re, sys, ast, os, collections
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK, S
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
Y = '/home/claude/yamalar/'
H = []
TUM = ast.literal_eval('{' + open(Y + 'ariza_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read() + '}')[(A, B)]
ITEMS = [m for m in TUM if not re.match(r'(bölüm (denetimi \(|\d+ denetiminden)|devir \()', m)]
M, MEAL = {}, {}
exec(open(Y + 'metin_%d_%d_%d.txt' % (S, A, B), encoding='utf-8').read(), {'M': M, 'MEAL': MEAL})
EN = collections.Counter()
Q = r"(?<![^\s(\[])'((?:[^']|(?<=[A-Za-zâîûçğışöüÂÎÛ])'(?=[a-zâîûçğışöü]))+)'"
MI = ([m for m in ITEMS if m.startswith('meal (okuma')] or [''])[0]
EMI = MI.split('emsal meal karşılık farkları', 1)[1].split('kip notu (', 1)[0] if 'emsal meal karşılık farkları' in MI else ''
SAT = []
for m in re.finditer(Q + r" %d:(\d+) " % S + Q + r" / (\d+:\d+) " + Q + r" \(emsal metninde\) — ([^;]*)", EMI):
    SAT.append((m.group(1), int(m.group(2)), m.group(4), m.group(5), m.group(3), m.group(0)))
def morph(nn):
    d = {}
    f_ = _BK + 'b%02d/morph.txt' % nn
    if os.path.exists(f_):
        for l in open(f_, encoding='utf-8'):
            p = l.rstrip('\n').split('\t')
            s_, a_, w_ = p[0].split(':')[:3]
            d[(int(a_), int(w_))] = p[2] if len(p) > 2 else ''
    return d
MO = {}
for nn in range(1, int(NN) + 1): MO.update(morph(nn))
def olc(a):
    for nn in range(int(NN), 0, -1):
        f_ = _BK + 'b%02d/olcum.txt' % nn
        if not os.path.exists(f_): continue
        L = [x for x in open(f_, encoding='utf-8').read().replace('**', '').split('\n\n') if x.strip()]
        for x in L:
            pass
    return ''
_OLC = {}
for nn in range(1, int(NN) + 1):
    f_ = _BK + 'b%02d/olcum.txt' % nn
    if not os.path.exists(f_): continue
    for l in open(f_, encoding='utf-8'):
        mm = re.match(r'#+ \*?\*?%d:(\d+)' % S, l)
    # olcum dosyası ayet başlığı taşımaz: blok aralığından sırayla eşlenir
B_ARAL = {}
_pl = open(Y + 'blok_plani_%d.txt' % S, encoding='utf-8').read()
for mm in re.finditer(r'^\s+(\d+)\. %d:(\d+)-(\d+)' % S, _pl, re.M): B_ARAL[int(mm.group(1))] = (int(mm.group(2)), int(mm.group(3)))
for nn, (a0, b0) in B_ARAL.items():
    f_ = _BK + 'b%02d/olcum.txt' % nn
    if nn > int(NN) or not os.path.exists(f_): continue
    L = [x for x in open(f_, encoding='utf-8').read().replace('**', '').split('\n\n') if x.strip()]
    for i, x in enumerate(L): _OLC[a0 + i] = x

# ── (1) GONDERGE_KISI_COGUL ──
for n in range(A, B + 1):
    a1 = re.search(r'◈A — A1 (.*?); aktör', M.get(n, ''), re.S)
    if not a1: continue
    for part in re.split(r'; (?=[\'k-m])', a1.group(1)):
        if not re.search(r'\b3[MF]P\b', part): continue
        for g in re.finditer(r'gönderge (?:%d:(\d+) )?(?:\'[^\']*\' )?(\d+)\. kelime' % S, part):
            ga = int(g.group(1)) if g.group(1) else n
            gw = int(g.group(2))
            tag = MO.get((ga, gw), '')
            if 'PN' not in tag.split('|') and '|PN|' not in tag: continue
            EN['gonderge_pn'] += 1
            if re.search(r'adlı \S+ %d\. sırada \(kisi' % gw, _OLC.get(ga, '')) and not re.search(r'ailesiyle|yanındakiler|topluluk', part):
                H.append("(1) %d:%d 3MP / 3FP gönderge %d:%d %d. kelime — ölçüm 'kisi' özel ad, topluluk notu yok" % (S, n, S, ga, gw))

# ── (2) FIIL_UYUMU_CINSIYET ──
for n in range(A, B + 1):
    for m in re.finditer(r"'([^']+)' 3([MF])S \(fiil uyumu; [^)]*?(\d+)\. kelime — fail (\d+)\. kelime\)", M.get(n, '')):
        g, w = m.group(2), int(m.group(4))
        tag = MO.get((n, w), '')
        cins = 'F' if re.search(r'\|F[SPD]?\|', tag + '|') else ('M' if re.search(r'\|M[SPD]?\|', tag + '|') else '')
        EN['fiil_uyumu'] += 1
        if cins and cins != g and not re.search(r'mecazi müennes|cinsiyet farkı', m.group(0)):
            H.append("(2) %d:%d '%s' 3%sS — fail %d. kelime morph %s, cinsiyet notu yok" % (S, n, m.group(1), g, w, cins))

# ── (3) EMSAL_DEGIL_HARF_NOTU ──
for seg in EMI.split('; '):
    rm = re.match(r"\s*'(.*?)' %d:(\d+) '(.*?)' / (\d+:\d+) '(.*?)' \(emsal metninde\) — (.*)" % S, seg)
    if not rm or not rm.group(6).startswith('çakışma değil'): continue
    EN['degil'] += 1
    if rm.group(3) != rm.group(5) and 'harf büyüklüğü' not in rm.group(6):
        H.append("(3) %d:%s / %s '%s' — 'çakışma değil' alıntıları bayt eşit değil, 'harf büyüklüğü' notu yok" % (S, rm.group(2), rm.group(4), rm.group(1)[:40]))

# ── (4) EMSAL_FIIL_SATIRI ──
EMS = set(open(_BK + 'b%s/ems.txt' % NN, encoding='utf-8').read().split()) if os.path.exists(_BK + 'b%s/ems.txt' % NN) else set()
_seg = _BK + 'b%s/yap/seg.py' % NN
SEG = {}
if os.path.exists(_seg): exec(open(_seg, encoding='utf-8').read(), _g := {}); SEG = _g.get('SEG', {})
for n in range(A, B + 1):
    d = M.get(n, '').split('\n')[0]
    fiil = []
    for tr_, ar_, its in SEG.get(n, []):
        for it in its:
            fm = re.match(r"'[^']+-' '([^']+)' (?:karşılığı|açılımı)", it)
            if fm: fiil.append(fm.group(1))
    for m in re.finditer(r"(?:[Hh]arekesiz|[Öö]nek kesilmiş) " + Q + r" \d+ ayet: ([^;]*)", d):
        lab, lst = m.group(1), m.group(2)
        for e in sorted(set(re.findall(r'\d+:\d+', lst)) & EMS):
            for f in fiil:
                if f not in lab: continue
                EN['fiil_emsal'] += 1
                if any(s_[2] == e and s_[1] == n and f in s_[0] for s_ in SAT): continue
                if ("'%s' %s fiil satırı yok" % (f, e)) in MI: continue
                H.append("(4) %d:%d '%s' — sayım '%s' %s listeliyor, fiil satırı yok" % (S, n, f, lab[:40], e))

# ── (5) EMSAL_ALINTI_TAM ──
for seg in EMI.split('; '):
    if '(emsal metninde)' not in seg: continue
    hm = re.match(r"\s*'(.*?)' %d:\d+ '" % S, seg)
    if not hm: continue
    EN['alinti'] += 1
    qm = re.match(r"\s*" + Q + r" %d:\d+ " % S, seg)
    if not qm or qm.group(1) != hm.group(1):
        H.append("(5) emsal satırı kalıbı '%s' ayrıştırıcıda bütün okunmuyor" % hm.group(1)[:50])

H = list(dict.fromkeys(H))
print('denetlenen: ' + ', '.join('%s %d' % kv for kv in sorted(EN.items())))
for h in H: print('HATA ' + h)
print('bolum44_kurallar hata: %d' % len(H))
