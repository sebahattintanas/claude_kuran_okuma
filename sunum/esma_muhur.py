# bölüm 8 kuralı 3: esma_kayit maddesi betikle — esma_kayit.json 'muhur' (e_oto son3), el kararlarıyla 'muhur_el' (son3'te 'ilahi' kararlı esmâ adı) ve ölçüm MÜHÜR alanı (olcum_bicim esma_k) yan yana
# uyuşmazlık 'araç tanımı farkı' adıyla sınıflanır; 'el kararları degil' gerekçe yerine geçmez
# kullanım (/home/claude'dan): python3 sunum/esma_muhur.py A B NN  → tek satır
import sys as _sy; _sy.path.insert(0, '/home/claude/sunum'); from sure import BK as _BK
import sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); from sure import S
A, B, NN = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
K = json.load(open('/home/claude/calisma/esma_kayit.json', encoding='utf-8'))
olc = [l.replace('**', '') for l in open(_BK + 'b%s/olcum.txt' % NN, encoding='utf-8').read().split('\n\n') if l.strip()]
out = []
for a in range(A, B + 1):
    r = K.get('%d:%d' % (S, a), {})
    m = bool(r.get('muhur'))
    el = r.get('esma_el', {}) or {}
    son3 = [w for w, ad in r.get('son3', []) if ad != 'اللَّه']
    mel = any(el.get('%d:%d:%d' % (S, a, w)) == 'ilahi' for w in son3) and m
    o = olc[a - A]
    om = 'MÜHÜR' if re.search(r'MÜHÜR(?!SÜZ)', o) else ('MÜHÜRSÜZ' if 'MÜHÜRSÜZ' in o else 'esmâ yok')
    ob = om == 'MÜHÜR'
    if m == ob and mel == ob: s = 'uyuşuyor'
    elif mel == ob: s = "araç tanımı farkı (muhur e_oto son3'ten, el kararları dışında; muhur_el ölçümle uyuşuyor)"
    else: s = 'araç tanımı farkı (muhur_el ölçümle uyuşmuyor — tam okuma sonu)'
    out.append('%d:%d muhur %s / muhur_el %s / ölçüm %s — %s' % (S, a, 'EVET' if m else 'hayır', 'EVET' if mel else 'hayır', om, s))
print('; '.join(out))
