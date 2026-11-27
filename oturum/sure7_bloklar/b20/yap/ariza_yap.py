# sûre 7 blok 20 (7:70-72) ARIZA oluşturucu — bölüm 7-3
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b20/olcum.txt'
os.environ['SAY2'] = '/home/claude/b20/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Nûh ve kavmi; Hûd ve Âd'"


def sd(key):
    return sayim.S2[key][1]


def sic(key):
    n, d = sayim.S2[key]
    return 1 + len([x for x in d['basilan'] if x.startswith('7:')]) + d['okunmus_si'] + d['henuz_si']


def taban(key, ay):
    n, d = sayim.S2[key]
    p = [ay] + [x for x in d['basilan'] if x.startswith('7:') and x != ay]
    if d['okunmus_si']: p.append('okunmus_si %d' % d['okunmus_si'])
    if d['henuz_si']: p.append('henuz_si %d' % d['henuz_si'])
    return ' + '.join(p)


R5 = [
 ('7:70', "'etâ mâ ve'ade in kâne min'", 2, 'say 7:70 11-16', "harekesiz 'fe'tinâ bi-mâ te'idunâ in kunte mine' (11-16. kelime)", ('dizi 7 70 11 16', "etâ mâ ve'ade in kâne min", '11-16', 'biçim farkı (dizi 7 70 11 16): basılmamış eş önek; öneksiz eş koşusu (dizi 7 70 11 16): basılmamış eş → önek kesilmiş sûre içi 1')),
 ('7:70', "'in kâne min sâdiq'", 2, 'say 7:70 14-17', "harekesiz 'in kunte mine's-sâdiqîn' (14-17. kelime)", ('dizi 7 70 14 17', 'in kâne min sâdiq', '14-17', 'biçim farkı (dizi 7 70 14 17): basılmamış eş yazım eş')),
 ('7:70', "'in kâne min'", 3, 'say 7:70 14-16', "harekesiz 'in kunte mine' (14-16. kelime)", ('dizi 7 70 14 16', 'in kâne min', '14-16', 'biçim farkı (dizi 7 70 14 16): basılmamış eş yazım eş; basılmamış eş yazım eş')),
 ('7:72', "'ellezî kezzebe âye'", 5, 'say 7:72 8-10', "harekesiz 'llezîne kezzebû bi-âyâtinâ' (8-10. kelime); biçim öğesi 'ellezî' öneki (lemma dizisi sûre içi 8, nakarat3 5)", ('dizi 7 72 8 10', 'ellezî kezzebe âye', '8-10', 'biçim farkı (dizi 7 72 8 10): 7:36 önek; 7:40 yazım eş; 7:64 yazım eş; basılmamış eş önek; basılmamış eş yazım eş; basılmamış eş yazım eş; basılmamış eş önek; öneksiz eş koşusu (dizi 7 72 8 10): 7:36 → önek kesilmiş sûre içi 3; 7:40 → önek kesilmiş sûre içi 7; 7:64 → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 3; basılmamış eş → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 7; basılmamış eş → önek kesilmiş sûre içi 3')),
 ('7:72', "'encâ ellezî ma'a'", 2, 'say 7:72 1-3', "harekesiz 'fe-enceynâhu ve'llezîne me'ahû' (1-3. kelime)", ('dizi 7 72 1 3', "encâ ellezî ma'a", '1-3', 'biçim farkı (dizi 7 72 1 3): 7:64 yazım eş')),
]
r5 = []
for ay, kal, nk, key, ad, dz, *tr_ in R5:
    s = sic(key)
    h = "%s nakarat3 %s %d (tür %s) / %s sûre içi %d (%s)" % (ay, kal, nk, (tr_[0] if tr_ else 'ic'), ad, s, taban(key, ay))  # bölüm 11 denetimi kuralı 3
    if s == nk:
        h += ' — tutuyor'
    else:
        dk, dad, dar, ger = dz
        ds = sic(dk)
        if ds == nk:
            h += " — tutmuyor; eşit aralıkla lemma dizisi '%s' (%s. kelime) sûre içi %d (%s) — tutuyor; gerekçe %s" % (dad, dar, ds, taban(dk, ay), ger)
        else:
            h += " — tutmuyor; eşit aralıkla lemma dizisi '%s' (%s. kelime) sûre içi %d (%s) — tutmuyor; gerekçe %s" % (dad, dar, ds, taban(dk, ay), ger)
    r5.append(h)

K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k and not (k + ' --medde' in sayim.S2 and sayim.S2[k + ' --medde'][0] != n)}  # sûre 6 bölüm 5 denetimi kuralı 6 (TEKIL_MEDDE)

VF_YAZI = {70: {2: "'e-ci'tenâ'", 3: "'li-na'bude'", 6: "'ve nezera'", 11: "'fe'tinâ'", 12: "'bi-mâ'"}, 71: {8: "'ve ğadabun'", 9: "'e-tucâdilûnenî'", 14: "'ve âbâ'ukum'", 18: "'bihâ'", 21: "'fe'ntazirû'"}, 72: {1: "'fe-enceynâhu'", 2: "'ve'llezîne'", 4: "'bi-rahmetin'", 6: "'ve qata'nâ'", 10: "'bi-âyâtinâ'", 11: "'ve mâ'"}}
sys.path.insert(0, '/home/claude/b20/yap')
from seg import meals
MEALS = meals()


def _bol(s, sep):
    out, d, cur, i = [], 0, '', 0
    while i < len(s):
        c = s[i]
        if c == '(': d += 1
        elif c == ')': d -= 1
        if d == 0 and s.startswith(sep, i):
            out.append(cur); cur = ''; i += len(sep); continue
        cur += c; i += 1
    out.append(cur)
    return out


MK = {}
for blok in MEALS:
    n = int(blok.split(' ', 1)[0].split(':')[1]); govde = blok.split(' ', 1)[1]
    for seg in _bol(govde, "; '"):
        seg = seg if seg.startswith("'") else "'" + seg
        j = seg.index("' (")
        tr = seg[1:j]; ic = seg[j + 3:].rstrip(')')
        parca = _bol(ic, ', ')
        MK.setdefault(n, []).append((tr, parca[0].strip("'"), parca[1:]))
open('/home/claude/b20/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '20')
BLOKLAR = [str(i) for i in range(1, 21)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '20', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b20/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '70', '72', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b20/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b20/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '70', '72', '20').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_70_72.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:70', '7:71', '7:72'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_70_72.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(70, 73))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:72 kök قطع ('qata'nâ' 6. kelime — kesme): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '70', '72', '20')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b20/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 21)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(70, 73))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l.replace('**', '') for l in open('/home/claude/b20/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b20/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 69), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 478",
 "geriye dönük koşu (sûre 7 bölüm 6 kapanışı, komut 'python3 sunum/geriye_donuk.py b17k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 70 72 20'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:72 've mâ kânû mu'minîn' (11-13. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (yalanlayanların sıfatı) (yamalar/esma_el_7_70_72.txt); 7:70 ve 7:71 esmâ yok; 7:70 lafız (4. kelime), 7:71 lafız (17. kelime); 7:72 lafız yok; 7:71 Rab (6. kelime); 7:70 ve 7:72 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 70 72 20'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 7:72 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı; muhur_el hayır): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in range(70, 73)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 70 72 20'): KALAN_P",
 "ölçüm aktör: 7:70, 7:71 ve 7:72 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:70 soru, emir, şart — COND 1 'in' (14.), IMPV 1 'fe'tinâ' (11.), INTG 1 'e-ci'tenâ' (2.); "
 "7:71 soru, emir — CERT 1 'qad' (2.), IMPV 1 'fe'ntazirû' (21.), INTG 1 'e-tucâdilûnenî' (9.), NEG 1 'mâ' (15.); 7:72 haber — NEG 1 've mâ' (11.)",
 "morph REL ('mâ' 7:70 7., 'bi-mâ' 7:70 12., 've'llezîne' 7:72 2., 'llezîne' 7:72 8.), PRP ('li-na'bude' 7:70 3.), RSLT ('fe'tinâ' 7:70 11.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:70, 7:71 ve 7:72 yıldız yok",
 "fâsıla: 7:69 ن → 7:70 ن (" + _F[0] + ") → 7:71 ن (" + _F[1] + ") → 7:72 ن (" + _F[2] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:70 11:32, 14:10, 46:22 (emsal olarak basıldı), okunmuş 1 ayet ve okunmamış 1 ayet (sûre içi 1); 7:71 12:40, 53:23 (emsal olarak basıldı); "
 "7:72 7:64, 21:77 (basılmış), okunmamış 2 ayet (sûre içi 2)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:70 'etâ mâ ve'ade in kâne min' süzgeç GEÇER, 'in kâne min sâdiq' süzgeç GEÇER, 'in kâne min' süzgeç GEÇER; 7:71 nakarat3 kalıbı yok; "
 "7:72 'ellezî kezzebe âye' süzgeç GEÇER, 'encâ ellezî ma'a' süzgeç GEÇMEZ; sûre içi eşler — bölüm 7-1 bloğundaki Nûh kıssası ayetleri (basılmış) ve basılmamış eşler",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:70 3MP ('qâlû' — gönderge 7:66 2. kelime), söz içi konuşan 1P ('na'bude', 'nezera'; ekler 'ci'tenâ', 'âbâ'unâ', 'fe'tinâ', 'te'idunâ'), söz içi muhatap 2MS ('ci'tenâ', 'fe'tinâ', 'te'idunâ', 'kunte'), 3MS ('kâne', 'ya'budu' — söz içi, fiil uyumu, fail 10. kelime; ek 'vahdehû' — söz içi, gönderge 'llâhe' 4. kelime); "
 "7:71 3MS ('qâle' — gönderge 7:65 4. kelime; 'veqa'a' — söz içi, fiil uyumu, fail 7. kelime; 'nezzele' — söz içi, fiil uyumu, fail 17. kelime), söz içi muhatap 2MP ('tucâdilûne', 'semmeytumûhâ', 'ntazirû'; zamir 'entum'; ekler ''aleykum', 'rabbikum', 'âbâ'ukum', 'me'akum'), söz içi konuşan 1S eki ('tucâdilûnenî', 'innî'), 3FS eki ('semmeytumûhâ', 'bihâ' — söz içi, gönderge 'esmâ'in' 11. kelime); "
 "7:72 konuşan 1P ('enceynâhu', 'qata'nâ'; ekler 'minnâ', 'bi-âyâtinâ'), 3MS eki ('enceynâhu', 'me'ahû' — gönderge 7:65 4. kelime), 3MP ('kezzebû', 'kânû' — gönderge 'llezîne' 8. kelime)",
 "7:70-72 gönderge zinciri: 7:70 'qâlû' göndergesi 7:66 2. kelimedeki ileri gelenler; 7:70 söz içi muhatap 2MS Hûd; 7:71 'qâle' göndergesi 7:65 4. kelimedeki Hûd; 7:71 söz içi muhatap 2MP kavmi; 7:72 'enceynâhu' ve 'me'ahû' göndergesi 7:65 4. kelimedeki Hûd; 7:72 'kezzebû', 'kânû' göndergesi 'llezîne' (8. kelime) (okuma)",
 "edilgen: 7:70, 7:71 ve 7:72 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:70 söz içi 2-17. kelime ('qâlû' 1. kelime ardından; ayet içinde kapanıyor); 7:71 söz içi 2-25. kelime ('qâle' 1. kelime ardından; ayet içinde kapanıyor); 7:72 söz yok; "
 "REM sapması 7:71 (21. kelime) — söz içi sonuç 'fe'si, emir cümlesi başı; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 70 72 20' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 7:70 've nezera' (6.) CONJ, 'fe'tinâ' (11.) RSLT; 7:71 've ğadabun' (8.) CONJ, 've âbâ'ukum' (14.) CONJ, 'fe'ntazirû' (21.) REM; 7:72 'fe-enceynâhu' (1.) REM, 've'llezîne' (2.) CONJ, 've qata'nâ' (6.) CONJ, 've mâ' (11.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:70, 7:71 ve 7:72 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 70 72 20'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:70 (11:32, 14:10, 46:22), 7:71 (12:40, 53:23); D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:70 عبد ×2, كون ×2; 7:71 سمو ×2, نظر ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: bloğun emsal dosyasında olmayan basılmış eş (önceki bloklarda basılmış ya da sûre içi), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:70 söz açılır / kapanır, şart → cevap (COND 'in' 14. kelime; cevap 'fe'tinâ' 11. kelime — öne alınmış), şahıs sayısında beraberlik (1P 6 · 2MS 6 — ölçüm baskın 2), şahıs geçişi yok, edim geçişi soru, emir → soru, emir, şart; 7:71 söz açılır / kapanır, şahıs geçişi yok, edim geçişi soru, emir, şart → soru, emir; "
 "7:72 bölüm kapanışı, şahıs sayısında beraberlik (1P 6 · 3. şahıs 6 — ölçüm baskın 1), şahıs geçişi 2 → 1, edim geçişi soru, emir → haber; ölçüm iltifât 7:70-72 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:70 'e-ci'tenâ li-na'bude'llâhe' — soru edatı ile mazi, amaç lâmı ile muzâri ve lafız (morph INTG + PERF + PRP + IMPF + PN); 7:71 'qad veqa'a 'aleykum min rabbikum' — tahkik edatı ile mazi ve tümleçler (morph CERT + PERF + P + P + N); "
 "7:72 'fe-enceynâhu ve'llezîne me'ahû' — istînâf, mazi ve atıfla ism-i mevsûl (morph REM + PERF + CONJ + REL + LOC)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:70 11-13. kelime — 11:32 ve 46:22 ile harekesiz eş (sayım: 'say 7:70 11-13'); 7:70 8-11. kelime — 14:10 ile lemma dizisi eşi (sayım: 'dizi 7 70 8 11'); "
 "7:71 11-14. kelime — 12:40 ve 53:23 ile harekesiz eş (sayım: 'say 7:71 11-14'); 7:70 kök عبد ve كون ikilemesi; 7:71 kök سمو ve نظر ikilemesi; geniş eşli sayımlar: 'say 7:70 11-17', 'say 7:70 11-16'",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 20'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'fe'tinâ bi-mâ te'idunâ' 7:70 'bize vaat ettiğin şeyi getir' / 11:32 'bizi tehdit ettiğin şeyi getir' (emsal metninde) — çakışma — tam okuma sonu ('vaat et-' / 'tehdit et-' — ve'ade karşılığı); "
 "'fe'tinâ bi-mâ te'idunâ' 7:70 'bize vaat ettiğin şeyi getir' / 46:22 'bize vaat ettiğin şeyi getir' (emsal metninde) — çakışma değil; "
 "'in kunte mine's-sâdiqîn' 7:70 'Doğru söyleyenlerdensen' / 11:32 'Doğru söyleyenlerdensen' (emsal metninde) — çakışma değil; "
 "'âbâ'unâ' 7:70 'atalarımızın' / 14:10 'atalarımızın' (emsal metninde) — çakışma değil; "
 "'mine's-sâdiqîn' 7:70 'Doğru söyleyenlerden' / 46:22 'Doğrulardan' (emsal metninde) — çakışma — tam okuma sonu ('doğru söyleyen' / 'doğru' — sâdiq karşılığı); "
 "'esmâ'in semmeytumûhâ entum ve âbâ'ukum' 7:71 'sizin ve atalarınızın taktığınız adlar' / 12:40 'sizin ve atalarınızın taktığı adlar' (emsal metninde) — çakışma — tam okuma sonu ('-dığınız' / '-dığı' — sıfat-fiil şahıs eki); "
 "'entum ve âbâ'ukum' 7:71 'sizin ve atalarınızın' / 53:23 'sizin ve atalarınızın' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:70 'qâlû' PERF — meal 'Dediler'; 'ci'tenâ' PERF ('e' ile) — meal 'geldin'; 'na'bude' IMPF SUBJ ('li' ile) — meal 'kulluk edelim'; 'nezera' IMPF SUBJ — meal 'bırakalım'; "
 "'kâne' PERF — meal 'olduklarını'; 'ya'budu' IMPF IND — meal 'kulluk etmekte'; 'fe'tinâ' IMPV — meal 'getir'; 'te'idunâ' IMPF IND — meal 'vaat ettiğin'; 'kunte' PERF ('in' ile) — meal 'söyleyenlerdensen'; "
 "7:71 'qâle' PERF — meal 'Dedi'; 'veqa'a' PERF ('qad' ile) — meal 'düştü'; 'tucâdilûnenî' IMPF IND ('e' ile) — meal 'tartışıyorsunuz'; 'semmeytumûhâ' PERF — meal 'taktığınız'; 'nezzele' PERF ('mâ' ile) — meal 'indirmediği'; 'fe'ntazirû' IMPV — meal 'bekleyin'; "
 "7:72 'enceynâhu' PERF — meal 'kurtardık'; 'qata'nâ' PERF — meal 'kestik'; 'kezzebû' PERF — meal 'yalanlayanların'; 'kânû' PERF ('mâ' ile) — meal 'değildi'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle; IMPF IND geniş zaman karşılığı her blokta sapma sayılır — sûre 7 bölüm 3 denetimi kuralı 3): 'na'bude', 'nezera' IMPF 7:70'te istek kipi ('-elim', '-alım') ile; 'kâne' PERF 7:70'te sıfat-fiil ('-duklarını') ile; 'ya'budu' IMPF 7:70'te sürerlik ('-mekte') ile; "
 "'te'idunâ' IMPF 7:70'te sıfat-fiil ('-tiğin') ile; 'kunte' PERF 7:70'te şart ('-sen') ile; 'tucâdilûnenî' IMPF 7:71'de şimdiki zaman ('-ıyorsunuz') ile; 'semmeytumûhâ' PERF 7:71'de sıfat-fiil ('-tığınız') ile; 'nezzele' PERF 7:71'de sıfat-fiil ('-mediği') ile; 'kezzebû' PERF 7:72'de sıfat-fiil ('-yanların') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'ellezîne' (REL: '-anları' / '-anların' / '-en') — çakışma değil (sıfat-fiil çekimi); 'li' (PRP: 'diye' / 'için') — çakışma değil (amaç lâmı; söz içi soruda 'diye'); 'mâ' (NEG: 'değil' / olumsuzluk eki / 'yok') — çakışma değil (isim, fiil ve varlık olumsuzluğu); 'mâ' (REL: '-dukları' / 'şeyi' / 'şeyleri') — çakışma değil (sıfat-fiil, ad); ''alâ' (yönelme eki / 'aracılığıyla' / 'için') — çakışma değil (fiil yönetimi); 'bi' ('-le' / belirtme eki / yönelme eki / bulunma eki) — çakışma değil (fiil yönetimi); 'fî' ('hakkında' / 'içinde' / bulunma eki) — çakışma değil (konu ve yer); 'hû' ('onunla' / karşılıksız / 'O'ndan') — çakışma değil (tümleç, tamlama); 'kum' ('size' / 'sizinle' / iyelik eki / 'sizi' / 'sizin' / karşılıksız) — çakışma değil (tümleç, tamlama); 'nâ' ('bize' / iyelik eki / karşılıksız / 'biz') — çakışma değil (tümleç, tamlama)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 70 72 20'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:70, 7:71 ve 7:72 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:70, 7:71 ve 7:72 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök قول 7:70 ('qâlû') ve 7:71 ('qâle') ile bölüm içi; kök أبو 7:70 ('âbâ'unâ') ve 7:71 ('âbâ'ukum') ile bölüm içi; kök أله 7:70 ('llâhe') ve 7:71 ('llâhu') ile bölüm içi; kök كون 7:70 ('kâne', 'kunte') ve 7:72 ('kânû') ile bölüm içi; "
 "bölümün önceki bloklarıyla ortak kökler: أله (7:59, 7:62, 7:65, 7:69 / 7:70, 7:71), أمن (7:68 / 7:72), أيي (7:64 / 7:72), جيأ (7:63, 7:69 / 7:70), ربب (7:61, 7:62, 7:63, 7:67, 7:68, 7:69 / 7:71), رحم (7:63 / 7:72), عبد (7:59, 7:65 / 7:70), قول (7:59, 7:60, 7:61, 7:65, 7:66, 7:67 / 7:70, 7:71), كذب (7:64, 7:66 / 7:72), كون (7:64 / 7:70, 7:72), نجو (7:64 / 7:72); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 7-3 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 18, 19 ve 20; bölüm kapanışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b20/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 70 72 20'; lem_bozuk.py 20 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 70 72 → AYN_SONUC; sunum/bolum4_kurallar.py 70 72 20 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 70 72 20 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 43)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 20 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('etâ', 'mâ', 've'ade', 'in', 'kâne', 'min', 'sâdiq', ''abede', 'âbâ'', 'ism', 'semmâ', 'nezzele', 'allâh', 'sultân', 'ellezî', 'kezzebe', 'âye', 'encâ', 'ma'a'); joker '_' dizi lemma dizisinde boş öğe olan zamir ve önek lemmalı kelimelerde ('entum' 7:71 13., 'bihâ' 7:71 18.); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (70, 72): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_70_72.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_7_b17k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '70', '72'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '70', '72', '20'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '70', '72', '20'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '70', '72', '20', '--tazelik-yok')}
    for _n in range(7, 43): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '70', '72', '20')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42 = [_R['B%d' % _n].splitlines() for _n in range(6, 43)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'B39_HEPSI': (B39[-1] if B39 else '?'), 'B40_HEPSI': (B40[-1] if B40 else '?'), 'B41_HEPSI': (B41[-1] if B41 else '?'), 'B42_HEPSI': (B42[-1] if B42 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
           'MUT_SONUC': (MUT[-1] if MUT else '?'), 'GERI_P': ' / '.join(x.lstrip('# ') for x in GERI), 'B6_ESMA': ('; '.join(l[5:] for l in B6 if 'esmâ kural' in l and l.startswith('HATA')) or 'sapma 0')}
    I_cur = list(I_HAM)
    for k, v in REP.items(): I_cur = I_cur[:len(BEK)] + [x.replace(k, v) for x in I_cur[len(BEK):]]  # bölüm 9 kuralı 9: taşınan denetim maddelerine yer tutucu değişimi uygulanmaz
    I_cur[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3, bölüm 6 kuralı 2 — komut 'python3 sunum/cakisma.py' + sûre 7'nin okunmuş bütün ARIZA dosyaları; bu bloğun karşılıklarına dokunan gruplar ve son dosyaya dokunan KÖK grupları; grup başına tam bir kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
                  + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
    if I_cur == onceki: break
    onceki = list(I_cur)
yaz(I_cur)
print('yazıldı', len(I_cur), 'tur', tur)
print('\n'.join(CAK_L))
print(GLS)
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39, B40, B41, B42): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
