# sûre 7 blok 3 (7:11-13) ARIZA oluşturucu — bölüm 2-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b03/olcum.txt'
os.environ['SAY2'] = '/home/claude/b03/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = list(ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_7_b02.txt', encoding='utf-8').read() + ']'))
VF_YAZI_ESKI = {}
BOL = "'Âdem'e secde; İblis'in mühleti; ağaç ve iniş'"


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

VF_YAZI = {11: {1: "'ve le-qad'"}, 12: {15: "'ve xalaqtehû'"}, 13: {}}
sys.path.insert(0, '/home/claude/b03/yap')
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
open('/home/claude/b03/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '03')
BLOKLAR = [str(i) for i in range(1, 4)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '3', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b03/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '11', '13', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b03/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b03/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '11', '13', '03').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_11_13.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:11', '7:12', '7:13'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_11_13.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(11, 14))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:12 'iz' (6. kelime — morph T, zaman)"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '11', '13', '03')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b03/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 4)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(11, 14))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l.replace('**', '') for l in open('/home/claude/b03/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b03/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 10), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
def _esc(t):
    for c in '.()[]|': t = t.replace(c, '\\' + c)
    return t
_AK = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))
_MB = _MB.replace('" + _AK + "', _AK)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta sunum/bolum16_kurallar.py (kural 1) fiilin ardındaki ayrı zamiri yeni cümlenin öznesi sayar — 7:12 8. kelime 'qâle' ardındaki 'ene xayrun' isim cümlesi, 10. kelime fail değil; sunum/bolum17_kurallar.py (kural 3) çok lemmalı kelimeyi bütün lemmalarıyla eşler — 7:12 4. kelime 'ellâ' ('en' + 'lâ') 38:75'teki 'en' ile eş sayılmaz; bölüm 1 kapanışında sunum/bolum36_kurallar.py (kural 1-5) eklendi, sunum/geriye_donuk.py ve mutasyon_sina buna göre güncellendi — önceki commit'te, kapanış mutasyon sınaması 384 / 384; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 371",
 "geriye dönük koşu (sûre 7 bölüm 1 kapanışı, komut 'python3 sunum/geriye_donuk.py b02k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 11 13 03'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:11, 7:12 ve 7:13 esmâ yok; 7:11, 7:12 ve 7:13 lafız ve Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 11 13 03'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (11, 12, 13)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 11 13 03'): KALAN_P",
 "ölçüm aktör: 7:11 '{{1|" + _AK + "}}' (A1'de 'âdeme' ve 'iblîs'); 7:12 ve 7:13 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:11 emir — CERT 1 've le-qad' (1.), EMPH 1 've le-qad' (1.; 'le'), IMPV 1 'scudû' (8.), NEG 1 'lem' (13.); ölçüm biçim ISTISNA (D2'de yazılmadı); "
 "7:12 soru — INTG 1 'mâ' (2.), NEG 1 'ellâ' (4.; 'lâ'); 7:13 emir — IMPV 2 'hbit' (2.), 'xruc' (10.), NEG 1 'mâ' (4.); "
 "morph REM ('fe-secedû' 7:11 10., 'fe-mâ' 7:13 4., 'fe'xruc' 7:13 10.), EXP ('illâ' 7:11 11.), SUB ('ellâ' 7:12 4., 'en' 7:13 7.), SUP ('fe'hbit' 7:13 2.), ACC ('inneke' 7:13 11.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:11, 7:12 ve 7:13 yıldız yok",
 "fâsıla: 7:10 ن → 7:11 ن (" + _F[0] + ") → 7:12 ن (" + _F[1] + ") → 7:13 ن (" + _F[2] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:11 18:50 (emsal olarak basıldı); 7:12 38:75 (emsal olarak basıldı), 38:76 (emsal olarak basıldı); 7:13 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok (7:11, 7:12 ve 7:13 ölçümünde nakarat3 alanı boş)'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:11, 7:12 ve 7:13 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:11 konuşan 1P ('xalaqnâkum', 'savvernâkum', 'qulnâ'), muhatap 2MP ('scudû' — söz içi; ekler 'xalaqnâkum', 'savvernâkum'), 3MP ('fe-secedû' — gönderge 'l-melâ'iketi' 7. kelime), 3MS ('yekun' — gönderge 'iblîs' 12. kelime), aktör adlı 'âdeme' ve 'iblîs'; "
 "7:12 3MS ('qâle' 1. kelime — tartışmalı, sayı uyumsuz, gönderge 7:11 6. kelime; 'mene'ake' — söz içi, gönderge 'mâ' 2. kelime; 'qâle' 8. kelime — gönderge 7:11 12. kelime; ekler 'minhu', 've xalaqtehû' — söz içi, gönderge 7:11 9. kelime), "
 "muhatap 2MS ('tescude', 'xalaqtenî', 've xalaqtehû' — söz içi; ekler 'mene'ake', 'emertuk' — söz içi), konuşan 1S ('emertuk', 'ene' — söz içi; ek 'xalaqtenî' — söz içi); "
 "7:13 3MS ('qâle' — tartışmalı, sayı uyumsuz, gönderge 7:11 6. kelime; 'yekûnu' — söz içi, gönderge 'en tetekebbera' 7-8. kelime), muhatap 2MS ('fe'hbit', 'tetekebbera', 'fe'xruc' — söz içi; ekler 'leke', 'inneke' — söz içi), 3FS eki ('minhâ', 'fîhâ' — söz içi, tartışmalı, anılan yer bölümde adsız)",
 "7:11-13 gönderge zinciri: konuşan 1P (adsız) 7:11'de, 7:10'dan sürer; 7:11 muhatap 2MP ekleri 7:10 muhatabıyla sürer, söz içi muhatap 2MP ise melekler ('l-melâ'iketi' 7. kelime); 7:12 ve 7:13 'qâle' (1. kelime) göndergesi 7:11 6. kelime ('qulnâ' konuşanı) — tartışmalı (sayı uyumu yok: 1P / 3MS; gönderge A1'de de 7:11 6. kelime); "
 "7:12 8. kelime fiilinin göndergesi 7:11 12. kelime ('iblîs'); 7:12 3MS ekleri 7:11 9. kelime ('li-âdeme'); 7:13 3FS ekleri ('minhâ', 'fîhâ') — tartışmalı, anılan yer bölümde adsız; 7:12 ve 7:13 söz içi 1S ve 2MS konuşana göre yer değiştirir (okuma)",
 "edilgen: 7:11, 7:12 ve 7:13 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:11 'qulnâ' (6.) ardından söz 8-9. kelime, ayet içi kapanış; 7:12 'qâle' (1.) ardından söz 2-7. kelime, 'qâle' (8.) ardından söz 9-17. kelime — ayet içi kapanışlar; "
 "7:13 'qâle' (1.) ardından söz 2-13. kelime (REM sapması 7:13 (4. kelime) — 'fe-mâ yekûnu' söz içinde istînâf, muhatap 2MS sürer; REM sapması 7:13 (10. kelime) — 'fe'xruc' söz içinde istînâf, muhatap 2MS sürer), ayet sonunda kapanır (okuma); mealde 'dedik' öncesinde ve 'Dedi ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 11 13 03' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:11 've le-qad' (1.) CONJ; 7:12 've xalaqtehû' (15.) CONJ; "
 "'fe' konumları: 7:11 'fe-secedû' (10.) REM; 7:13 'fe'hbit' (2.) SUP, 'fe-mâ' (4.) REM, 'fe'xruc' (10.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:11 ◈B خلق ('xalaqnâkum' 2. kelime — B2; anlam notu: muhatapların yaratılışı); 7:12 ◈B خلق ('xalaqtenî' 12. kelime — B2; anlam notu: ateşten yaratılış), 7:12 ◈B خلق ('xalaqtehû' 15. kelime — B2; anlam notu: çamurdan yaratılış); 7:13 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 11 13 03'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:11 (18:50); 7:12 (38:75, 38:76); 7:13 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:11 سجد ×3; 7:12 خلق ×2, قول ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:11 bölüm açılışı, söz açılır (8. kelime), söz kapanır (9. kelime, ayet içi), şahıs geçişi yok, edim geçişi haber → emir; 7:12 söz açılır (2. kelime), söz kapanır (7. kelime, ayet içi), söz açılır (9. kelime), söz kapanır (17. kelime, ayet içi), şahıs geçişi 1 → 2, edim geçişi emir → soru; "
 "7:13 söz açılır (2. kelime), söz kapanır (13. kelime, ayet içi), şahıs geçişi yok, edim geçişi soru → emir; "
 "ölçüm iltifât 7:11-13 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:11 've le-qad' — pekiştirme (morph CONJ + EMPH + CERT); 7:11 'summe' ile sıralı atıf (morph CONJ); 7:11 'illâ iblîs' — istisna (morph EXP); 7:11 'lem yekun mine's-sâcidîn' — olumsuz geçmiş (morph NEG + JUS); "
 "7:12 'mâ mene'ake ellâ tescude' — soru ve mastar cümlesi, olumsuzluk edatı zâid okundu (morph INTG + SUB + NEG); 7:12 'iz emertuk' — zaman cümlesi (morph T); 7:13 'fe'hbit' — söz başında 'fe' (morph SUP); 7:13 'en tetekebbera' — mastar cümlesi (morph SUB); 7:13 'inneke mine's-sâğirîn' — tekitli isim cümlesi (morph ACC)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:11 6-12. kelime — 18:50 ile harekesiz eş (sayım: 'say 7:11 6-12'); 7:12 2-3. kelime — 38:75 ile harekesiz eş (sayım: 'say 7:12 2-3'); 7:12 8-17. kelime — 38:76 ile harekesiz eş (sayım: 'say 7:12 8-17'); "
 "7:11 kök سجد üçlemesi; 7:12 kök خلق, قول ikilemeleri",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 03'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'qulnâ li'l-melâ'iketi'scudû li-âdeme fe-secedû illâ iblîs' 7:11 'meleklere: Âdem'e secde edin, dedik; İblîs hariç secde ettiler' / 18:50 'Meleklere: Âdem'e secde edin, demiştik; İblîs hariç secde ettiler' (emsal metninde) — çakışma — tam okuma sonu ('dedik' / 'demiştik' kip farkı ve cümle başı büyük harf); "
 "'fe-secedû illâ iblîs' 7:11 'İblîs hariç secde ettiler' / 18:50 'İblîs hariç secde ettiler' (emsal metninde) — çakışma değil (bayt eşit); "
 "'mâ mene'ake' 7:12 'seni ne alıkoydu' / 38:75 'seni ne alıkoydu' (emsal metninde) — çakışma değil (bayt eşit); "
 "'qâle ene xayrun minhu xalaqtenî min nârin ve xalaqtehû min tîn' 7:12 'Ben ondan hayırlıyım; beni ateşten yarattın, onu ise çamurdan yarattın' / 38:76 'Ben ondan hayırlıyım; beni ateşten yarattın, onu ise çamurdan yarattın' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ene xayrun minhu' 7:12 'Ben ondan hayırlıyım' / 38:76 'Ben ondan hayırlıyım' (emsal metninde) — çakışma değil (bayt eşit); "
 "'xalaqtenî min nârin' 7:12 'beni ateşten yarattın' / 38:76 'beni ateşten yarattın' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ve xalaqtehû min tîn' 7:12 'onu ise çamurdan yarattın' / 38:76 'onu ise çamurdan yarattın' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:11 'xalaqnâ' PERF — meal 'yarattık'; 'savvernâ' PERF — meal 'verdik'; 'qulnâ' PERF — meal 'dedik'; 'scudû' IMPV — meal 'edin'; 'secedû' PERF — meal 'ettiler'; 'yekun' IMPF JUS ('lem' ile) — meal 'olmadı'; "
 "7:12 'qâle' PERF (1. kelime) — meal 'Dedi'; 'mene'a' PERF — meal 'alıkoydu'; 'tescude' IMPF SUBJ ('en' ile) — meal 'etmekten'; 'emertu' PERF — meal 'emrettiğimde'; 'qâle' PERF (8. kelime) — meal 'Dedi'; 'xalaqte' PERF (12. kelime) — meal 'yarattın'; 'xalaqte' PERF (15. kelime) — meal 'yarattın'; "
 "7:13 'qâle' PERF — meal 'Dedi'; 'hbit' IMPV — meal 'in'; 'yekûnu' IMPF IND ('mâ' ile) — meal 'olmaz'; 'tetekebbera' IMPF SUBJ ('en' ile) — meal 'büyüklenmek'; 'xruc' IMPV — meal 'çık'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'yekun' IMPF JUS 7:11'de 'lem' ile geçmiş zaman ('-dı') ile; 'tescude' IMPF SUBJ 7:12'de ad-fiil ('-mek') ile; 'emertu' PERF 7:12'de zarf-fiil ('-diğimde') ile; 'tetekebbera' IMPF SUBJ 7:13'te ad-fiil ('-mek') ile; 'yekûnu' IMPF IND 7:13'te geniş zaman olumsuzu ('-maz') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): bölümün önceki bloğu yok",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 11 13 03'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:11, 7:12 ve 7:13 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:12 ('xalaqtenî min nârin' / 've xalaqtehû min tîn'); 7:13 ('tetekebbera' / 's-sâğirîn'); 7:11 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök سجد 7:11 ('scudû', 'fe-secedû', 's-sâcidîn') ve 7:12 ('tescude'); kök خلق 7:11 ('xalaqnâkum') ve 7:12 ('xalaqtenî', 've xalaqtehû'); kök قول 7:11 ('qulnâ'), 7:12 ('qâle', 'qâle') ve 7:13 ('qâle'); kök كون 7:11 ('yekun') ve 7:13 ('yekûnu'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 2-1 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 3, 4, 5 ve 6; bu blok bölümü açıyor; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b03/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 11 13 03'; lem_bozuk.py 03 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 11 13 → AYN_SONUC; sunum/bolum4_kurallar.py 11 13 03 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 11 13 03 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 37)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 3 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('qâle', 'melek', 'secede', 'âdem', 'illâ', 'iblîs', 'mâ', 'mene'a', 'xayr', 'min', 'xalaqa', 'nâr', 'tîn'); joker '_' yalnız lemmasız 'ene' öğesinde ('dizi 7 12 8 17'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (11, 13): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_11_13.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_7_b02k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '11', '13'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '11', '13', '03'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '11', '13', '03'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '11', '13', '03', '--tazelik-yok')}
    for _n in range(7, 37): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '11', '13', '03')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36 = [_R['B%d' % _n].splitlines() for _n in range(6, 37)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
