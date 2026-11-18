# bölüm 1 (sûre 5) denetimi kuralı 6: eş edat / zamir karşılık listesi — morph etiketli başlıklar, zamirler birleşik ('hu' / 'hû' / 'hî' / 'hi'; 'hum' / 'him'), 'bi' dahil
# bölüm 8 kuralı 15: Türkçe hedefte kesme işaretli biçimler ('O'nun', 'O'nu', 'Allah'ın') ayrıştırılır
# bölüm 5 kuralı 2: 'î' / 'nî' / 'te' / 'tu' / 'â' zamir kümesinde (edat_etiket.ZAMIR), büyük harfli tırnaksız biçimler, ayrıştırılamayan ve tanınmayan maddeler sayılır
# kullanım (/home/claude'dan): python3 sunum/es_edat.py <blok no> [<blok no> …]  — bNN/yap/veri.py (MK) + bNN/morph<S>.txt; yalnız iki ya da daha çok geçişli başlıklar
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK
import sys, os, re, importlib.util as iu, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from sure import S
import edat_etiket as E
BIR = {"'hû'": "'hu'", "'hî'": "'hu'", "'hi'": "'hu'", "'hu'": "'hu'", "'him'": "'hum'", "'hum'": "'hum'", "'hinne'": "'hunne'", "'hunne'": "'hunne'", "'himâ'": "'humâ'", "'humâ'": "'humâ'", "'ûne'": "'û'"}
EK = ("'bel'", "'mâzâ'", "'ne'", "'ni'", "'le'alle'", "'innemâ'", "'nne'", "'ente'", "'ene'", "'entum'", "'zâlike'", "'hâzâ'", "'tilke'", "'keyfe'", "'ke'enne'", "'ke'ennemâ'", "'ba'd'", "'qabl'", "'elletî'", "'hâ'", "'iz'", "'izâ'", "'nâ'", "'tum'", "'kum'", "'û'", "'î'", "'ke'", "'â'")  # bölüm 4 denetimi kuralı 5: 'î' / 'ke' / 'â' zamirleri
HATA, TANIMSIZ = [], []
ISIM_DIS = {"'ğayr'"}  # bölüm 6 kuralı 11: 'ğayr' isim (morph N, izafet başı) — edat / zamir eş tablosu dışında bırakılır
G = collections.defaultdict(lambda: collections.defaultdict(list))
for nn in sys.argv[1:]:
    d = _BK + 'b%02d' % int(nn)
    sp = iu.spec_from_file_location('veri%s' % nn, d + '/yap/veri.py'); v = iu.module_from_spec(sp); sp.loader.exec_module(v)
    for a, L in v.MK.items():
        for tr, q, items in L:
            for it in items:
                m = re.match(r"('(?:[^']|'(?=[a-zâîûçğışöü]))+') (\d+)\. kelimede (karşılıksız|'((?:[^']|'(?=[a-zçğıöşü]))*)'(?: [a-zçğıöşü]+)? ile|([a-zçğıöşüA-Z0-9 ]+?) ile)", it)  # bölüm 2 denetimi kuralı 3: ''-i' iyelik ile' biçimi; bölüm 4 kuralı 5: tırnaksız biçimler
                if not m:
                    m0 = re.match(r"('(?:[^']|'(?=[a-zâîûçğışöü]))+') (\d+)\. kelimede ", it)
                    if m0: HATA.append('%d:%d ' % (S, a) + it[:50])  # bölüm 5 kuralı 2: kelimede kaydı olup ayrıştırılamayan her madde
                    continue
                ed, w = m.group(1), int(m.group(2))
                if ed not in E.EDLEM and ed not in E.ZAMIR and ed not in BIR and ed not in EK:
                    if not re.search(r'[A-Z]', ed) and ed not in ISIM_DIS: TANIMSIZ.append('%d:%d %s' % (S, a, ed))
                    continue
                tag = E.etiket(a, w, ed)
                bas = BIR.get(ed, ed)
                kar = 'karşılıksız' if m.group(3) == 'karşılıksız' else m.group(3)
                G['%s (%s)' % (bas, tag)][kar].append('%d:%d %d.' % (S, a, w))
out = []
for bas in sorted(G):
    tot = sum(len(x) for x in G[bas].values())
    if tot < 2: continue
    out.append(bas + ' — ' + ', '.join('%s (%s)' % (k, ', '.join(v) + ' kelime') for k, v in sorted(G[bas].items())))
print('; '.join(out) + '; ayrıştırılamayan edat / zamir maddesi %d' % len(HATA) + (' (' + ' | '.join(HATA[:5]) + ')' if HATA else '') + '; tanınmayan edat / zamir başlığı %d' % len(TANIMSIZ) + (' (' + ', '.join(TANIMSIZ[:8]) + ')' if TANIMSIZ else ''))
