# sûre 7 blok 16 (7:54-56) ARIZA oluşturucu — bölüm 6-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b16/olcum.txt'
os.environ['SAY2'] = '/home/claude/b16/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = list(ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_7_b15.txt', encoding='utf-8').read() + ']'))
VF_YAZI_ESKI = {}
BOL = "'Altı günde yaratma; dua; rüzgâr ve ölü belde'"


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
 ("7:55", "'inne lâ ahbeb'", 2, 'say 7:55 5-7', "harekesiz 'innehû lâ yuhibbu' (5-7. kelime)", ('dizi 7 55 5 7', "inne lâ ahbeb", '5-7', "biçim farkı (dizi 7 55 5 7): 7:31 yazım eş")),
 ("7:56", "'lâ efsedu fî ard ba'd islâh'", 2, 'say 7:56 1-6', "harekesiz 've lâ tufsidû fi'l-ardi ba'de islâhihâ' (1-6. kelime)", ('dizi 7 56 1 6', "lâ efsedu fî ard ba'd islâh", '1-6', "biçim farkı (dizi 7 56 1 6): basılmamış eş yazım eş")),
 ("7:56", "'efsedu fî ard'", 3, 'say 7:56 2-4', "harekesiz 'tufsidû fi'l-ardi' (2-4. kelime)", ('dizi 7 56 2 4', "efsedu fî ard", '2-4', "biçim farkı (dizi 7 56 2 4): basılmamış eş yazım eş; basılmamış eş fiil çekimi, zamir eki, önek")),
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

VF_YAZI = {54: {7: "'ve'l-arda'", 20: "'ve'ş-şemse'", 21: "'ve'l-qamera'", 22: "'ve'n-nucûme'", 24: "'bi-emrihî'", 26: "'lehu'", 28: "'ve'l-emru'"}, 55: {4: "'ve xufyeten'"}, 56: {1: "'ve lâ'", 7: "'ve'd'ûhu'", 9: "'ve tama'an'"}}
sys.path.insert(0, '/home/claude/b16/yap')
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
open('/home/claude/b16/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '16')
BLOKLAR = [str(i) for i in range(1, 17)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '16', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b16/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '54', '56', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b16/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b16/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '54', '56', '16').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_54_56.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:54', '7:55', '7:56'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_54_56.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(54, 57))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:56 'ba'de' (5. kelime — morph T, zaman)"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '54', '56', '16')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b16/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 17)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(54, 57))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l.replace('**', '') for l in open('/home/claude/b16/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b16/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_HP = _esc(re.search(r'HAPAKS: .*? — hapaks z=3,28', _OL[0]).group(0))
for _k, _v in (('_HP', _HP),): _MB = _MB.replace('" + %s + "' % _k, _v)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 53), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; bölüm 5 kapanışında sunum/bolum41_kurallar.py (kural 1-5) eklendi, sunum/geriye_donuk.py ve mutasyon_sina buna göre güncellendi — önceki commit'te, kapanış mutasyon sınaması 435 / 435; "
 "yeni kök حثث (7:54 19. kelime 'hasîsen'; yamalar/yama_kok_7_54.py → kok_ekle_7.py, kok_turkce 1635; ölçüm yeniden alındı); mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 443",
 "geriye dönük koşu (sûre 7 bölüm 5 kapanışı, komut 'python3 sunum/geriye_donuk.py b15k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 54 56 16'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:56 'rahmeta'llâhi qarîbun' (11-13. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (rahmetin yakınlığı) (yamalar/esma_el_7_54_56.txt); 7:56 esma_kayit 'mühür EVET' / ölçüm MÜHÜRSÜZ — uyuşmuyor (esma_el 'degil' kararı; muhur_el ölçümle eş); 7:54 ve 7:55 esmâ yok; "
 "7:54 lafız (3. ve 30. kelime), 7:56 lafız (12. kelime); 7:55 lafız yok; 7:54 Rab (2. ve 31. kelime), 7:55 Rab (2. kelime); 7:56 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 54 56 16'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 7:56 mühür EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, esma_el 'degil' kararı): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (54, 55, 56)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 54 56 16'): KALAN_P",
 "ölçüm aktör: 7:54, 7:55 ve 7:56 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:54 haber — kip yok; ölçüm biçim DIKKAT (D2'de yazılmadı); 7:55 emir — IMPV 1 'ud'û' (1.), NEG 1 'lâ' (6.); 7:56 emir, yasak — IMPV 1 've'd'ûhu' (7.), PRO 1 'lâ' (1.); ölçüm biçim NEHY (D2'de yazılmadı); "
 "morph REL ('llezî' 7:54 4.), ATT ('elâ' 7:54 25.), T ('ba'de' 7:56 5.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:54 ★★★ (kaynak hapaks, z=3,28); 7:55 ★★ (kaynak rab, z=2,34); 7:56 yıldız yok",
 "fâsıla: 7:53 ن → 7:54 ن (" + _F[0] + ") → 7:55 ن (" + _F[1] + ") → 7:56 ن (" + _F[2] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:54 10:3 (emsal olarak basıldı), 13:3 (emsal olarak basıldı), 16:12 (emsal olarak basıldı), 22:18 (emsal olarak basıldı), okunmuş 1 ayet; 7:55 xref yok; 7:56 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:54 nakarat3 yok; 7:55 'inne lâ ahbeb' süzgeç GEÇMEZ; 7:56 'lâ efsedu fî ard ba'd islâh' süzgeç GEÇER, 'efsedu fî ard' süzgeç GEÇER; sûre içi eşler — 7:55 kalıbında 7:31 (basılmış), 7:56 kalıplarında basılmamış",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:54 muhatap 2MP eki ('rabbekumu'), 3MS ('xalaqa', 'stevâ' — gönderge 'llezî' 4. kelime; 'yuğşi' — gönderge 'llâhu' 3. kelime; 'yatlubuhû' — tartışmalı; gönderge 'l-leyle' 16. kelime; 'tebâraka' — fiil uyumu, fail 30. kelime; ekler 'yatlubuhû' — tartışmalı; gönderge 7:54 17. kelime; 'bi-emrihî', 'lehu' — gönderge 'llâhu' 3. kelime); "
 "7:55 muhatap 2MP ('ud'û'), muhatap 2MP eki ('rabbekum'), 3MS ('yuhibbu' — gönderge 'rabbekum' 2. kelime; ek 'innehû' — gönderge 'rabbekum' 2. kelime); "
 "7:56 muhatap 2MP ('tufsidû', 've'd'ûhu'), 3FS eki ('islâhihâ' — gönderge 'l-ardi' 4. kelime), 3MS eki ('ve'd'ûhu' — gönderge 7:55 2. kelime)",
 "7:54-56 gönderge zinciri: 7:54 muhatap 2MP eki ('rabbekumu' 2. kelime) bölüm açılışında genel hitap; 7:55 muhatap 2MP ('ud'û' 1. kelime, 'rabbekum' 2. kelime) 7:54 hitabıyla eş; 7:55 'innehû' ve 'yuhibbu' 3MS göndergesi 'rabbekum' (2. kelime); 7:56 muhatap 2MP ('tufsidû' 2. kelime, 've'd'ûhu' 7. kelime) 7:55 hitabıyla eş; 7:56 've'd'ûhu' 3MS eki 7:55 2. kelimedeki Rab (okuma)",
 "edilgen: 7:54, 7:55 ve 7:56 edilgen fiil yok; 7:54 'musaxxarâtin' (23. kelime) edilgen ortaç (ad)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:54, 7:55 ve 7:56 söz fiili yok, A3 '—'; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 54 56 16' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:54 've'l-arda' (7.), 've'ş-şemse' (20.), 've'l-qamera' (21.), 've'n-nucûme' (22.), 've'l-emru' (28.) CONJ; 7:55 've xufyeten' (4.) CONJ; 7:56 've lâ' (1.), 've'd'ûhu' (7.), 've tama'an' (9.) CONJ; 'fe' konumu yok",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:54 ◈K سمو ('s-semâvâti' 6. kelime — K1), 7:54 ◈K أرض ('l-arda' 7. kelime — K1), 7:54 ◈K يوم ('eyyâmin' 10. kelime — K2), 7:54 ◈K ليل ('l-leyle' 16. kelime — K1), 7:54 ◈K نهر ('n-nehâra' 17. kelime — K1), 7:54 ◈K شمس ('ş-şemse' 20. kelime — K1), 7:54 ◈K قمر ('l-qamera' 21. kelime — K1), 7:54 ◈K نجم ('n-nucûme' 22. kelime — K1), "
 "7:54 ◈B خلق ('xalaqa' 5. kelime — B2), 7:54 ◈B خلق ('l-xalqu' 27. kelime — B2); 7:56 ◈K أرض ('l-ardi' 4. kelime — K1); 7:55 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 54 56 16'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:54 (10:3, 13:3, 16:12, 22:18); D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:54 أله ×2, أمر ×2, خلق ×2, ربب ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: bloğun emsal dosyasında olmayan basılmış eş (önceki bloklarda basılmış ya da sûre içi), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:54 bölüm açılışı, şahıs geçişi yok, edim geçişi soru → haber; 7:55 şahıs geçişi 3 → 2, edim geçişi haber → emir; 7:56 şahıs geçişi yok, edim geçişi emir → emir, yasak; ölçüm iltifât 7:54-56 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:54 'inne rabbekumu'llâhu'llezî xalaqa' — tekit edatı, isim cümlesi ve ilgi cümlesi (morph ACC + PN + REL + PERF); 7:54 'yuğşi'l-leyle'n-nehâra' — iki nesneli muzâri (morph IMPF + ACC + ACC); 7:54 've'ş-şemse ve'l-qamera ve'n-nucûme musaxxarâtin' — 5. kelimedeki fiile atıflı nesneler ve mansub edilgen ortaç (morph CONJ + ACC + PASS_PCPL); "
 "7:54 'elâ lehu'l-xalqu ve'l-emru' — dikkat edatı, öne alınmış haber (morph ATT + P + NOM); 7:55 'ud'û rabbekum tadarru'an ve xufyeten' — emir ve mansub mastar (morph IMPV + VN); 7:56 've lâ tufsidû' — atıf ve nehiy, meczum muzâri (morph CONJ + PRO + JUS); 7:56 'inne rahmeta'llâhi qarîbun' — tekit edatı ve müzekker haber (morph ACC + NOM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:54 1-14. kelime ile açılıyor — 10:3 ile harekesiz eş (sayım: 'say 7:54 1-14'); 7:54 15-17. kelime — 13:3 ile harekesiz eş (sayım: 'say 7:54 15-17'); "
 "7:54 20-24. kelime — 16:12 ile harekesiz eş (sayım: 'say 7:54 20-24'); 7:54 20-22. kelime — 16:12 ve 22:18 ile harekesiz eş (sayım: 'say 7:54 20-22'); 7:54 kök أله, أمر, خلق ve ربب ikilemeleri; 7:56 1-6. kelime ile açılıyor — sûre içi basılmamış eşi var (sayım: 'say 7:56 1-6')",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 16'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'inne rabbekumu'llâhu'llezî xalaqa's-semâvâti ve'l-arda fî sitteti eyyâmin summe'stevâ 'ale'l-'arşi' 7:54 'Gerçekten Rabbiniz gökleri ve yeri altı günde yaratıp sonra arşa istivâ eden Allah'tır' / 10:3 'gökleri ve yeri altı günde yaratan, sonra arşa istivâ eden Allah'tır' (emsal metninde) — çakışma — tam okuma sonu ('-ıp' / '-an'); "
 "'yuğşi'l-leyle'n-nehâra' 7:54 'Geceyi gündüze bürür' / 13:3 'Geceyi gündüze bürüyor' (emsal metninde) — çakışma — tam okuma sonu ('-r' / '-yor'); "
 "'ve'ş-şemse ve'l-qamera ve'n-nucûme musaxxarâtin bi-emrihî' 7:54 'Güneşi ve ayı ve yıldızları O'nun emriyle boyun eğdirilmiş' / 16:12 'yıldızlar da O'nun emriyle boyun eğmiştir' (emsal metninde) — çakışma — tam okuma sonu ('boyun eğdir-' / 'boyun eğ-'); "
 "'ve'ş-şemse ve'l-qamera ve'n-nucûme' 7:54 'Güneşi ve ayı ve yıldızları' / 22:18 'güneş, ay, yıldızlar' (emsal metninde) — çakışma — tam okuma sonu (belirtme eki fiil yönetiminden); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:54 'xalaqa' PERF — meal 'yaratıp'; 'stevâ' PERF — meal 'eden'; 'yuğşî' IMPF IND — meal 'bürür'; 'yatlubu' IMPF IND — meal 'arar'; 'tebâraka' PERF — meal 'ne yücedir'; "
 "7:55 'ud'û' IMPV — meal 'dua edin'; 'yuhibbu' IMPF IND ('lâ' ile) — meal 'sevmez'; 7:56 'tufsidû' IMPF JUS ('lâ' ile) — meal 'yapmayın'; 've'd'ûhu' IMPV — meal 'dua edin'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle; IMPF IND geniş zaman karşılığı her blokta sapma sayılır — sûre 7 bölüm 3 denetimi kuralı 3): 'xalaqa' PERF 7:54'te zarf-fiil ('-ıp') ile; 'stevâ' PERF 7:54'te sıfat-fiil ('-en') ile; 'yuğşî' IMPF 7:54'te geniş zaman ('-r') ile; 'yatlubu' IMPF 7:54'te geniş zaman ('-r') ile; 'tebâraka' PERF 7:54'te ünlem cümlesi ('ne yücedir') ile; 'yuhibbu' IMPF 7:55'te geniş zaman ('-mez') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 54 56 16'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:54, 7:55 ve 7:56 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:54 ('l-leyle' / 'n-nehâra'); 7:56 ('xavfen' / 'tama'an'); 7:55 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök ربب 7:54 ('rabbekumu', 'rabbu') ve 7:55 ('rabbekum') ile bölüm içi; kök دعو 7:55 ('ud'û') ve 7:56 ('ve'd'ûhu') ile bölüm içi; kök أرض 7:54 ('ve'l-arda') ve 7:56 ('fi'l-ardi') ile bölüm içi; kök أله 7:54 ('llâhu', 'llâhu') ve 7:56 ('llâhi') ile bölüm içi; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 6-1 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 16 ve 17; bölüm açılışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b16/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 54 56 16'; lem_bozuk.py 16 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 54 56 → AYN_SONUC; sunum/bolum4_kurallar.py 54 56 16 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 54 56 16 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 42)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 16 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('inne', 'rabb', 'allâh', 'ellezî', 'xalaqa', 'semâ'', 'ard', 'sitte', 'yevm', 'summe', 'istevâ', ''alâ', ''arş', 'uğşiyet' (morph LEM ham biçim), 'leyl', 'nehâr', 'şems', 'qamer', 'necm', 'musaxxare', 'emr', 'lâ', 'ahbeb' (morph LEM ham biçim), 'efsedu' (morph LEM ham biçim), 'fî', 'ba'd', 'islâh'); joker '_' bu blokta yok; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (54, 56): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_54_56.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_7_b15k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '54', '56'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '54', '56', '16'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '54', '56', '16'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '54', '56', '16', '--tazelik-yok')}
    for _n in range(7, 42): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '54', '56', '16')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39, B40, B41 = [_R['B%d' % _n].splitlines() for _n in range(6, 42)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'B39_HEPSI': (B39[-1] if B39 else '?'), 'B40_HEPSI': (B40[-1] if B40 else '?'), 'B41_HEPSI': (B41[-1] if B41 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39, B40, B41): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
