# sûre 7 blok 2 (7:6-10) ARIZA oluşturucu — bölüm 1-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b02/olcum.txt'
os.environ['SAY2'] = '/home/claude/b02/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Kitap indirildi; helak edilen kentler; tartı; yeryüzünde yerleştirme'"


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

VF_YAZI = {6: {5: "'ve le-nes'elenne'"}, 7: {4: "'ve mâ'"}, 8: {1: "'ve'l-veznu'"}, 9: {1: "'ve men'"}, 10: {1: "'ve le-qad'", 5: "'ve ce'alnâ'"}}
sys.path.insert(0, '/home/claude/b02/yap')
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
open('/home/claude/b02/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '02')
BLOKLAR = [str(i) for i in range(1, 3)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '2', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b02/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '6', '10', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b02/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b02/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '6', '10', '02').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_6_10.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:6', '7:7', '7:8', '7:9', '7:10'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_6_10.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(6, 11))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:9 kök نفس ('enfusehum' 7. kelime — kendi): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '6', '10', '02')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b02/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 3)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(6, 11))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l for l in open('/home/claude/b02/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b02/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 5), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; blok 1'de sunum/kelime_kontrol.py (bölüm 10 denetimi kuralı 6) morph INL istisnası önceki commit'te; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 365",
 "geriye dönük koşu (bölüm 19 kapanışı, sûre 6 kayıtlarında, komut 'python3 sunum/geriye_donuk.py b40k yamalar/geriye_donuk_6_b38k.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 6 10 02'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:6, 7:7, 7:8, 7:9 ve 7:10 esmâ yok; 7:6, 7:7, 7:8, 7:9 ve 7:10 lafız ve Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 6 10 02'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (6, 7, 8, 9, 10)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 6 10 02'): KALAN_P",
 "ölçüm aktör: 7:6, 7:7, 7:8, 7:9 ve 7:10 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:6 haber — EMPH 4 'fe-le-nes'elenne' (1.; 'le' ve 'n'), 've le-nes'elenne' (5.; 'le' ve 'n'); 7:7 haber — EMPH 2 'fe-le-nequssanne' (1.; 'le' ve 'n'), NEG 1 'mâ' (4.); "
 "7:8 şart — COND 1 'men' (4.); 7:9 şart — COND 1 'men' (1.); 7:10 haber — CERT 1 've le-qad' (1.), EMPH 1 've le-qad' (1.; 'le'); "
 "morph REM ('fe-le-nes'elenne' 7:6 1., 've mâ' 7:7 4., 'fe-men' 7:8 4., 've le-qad' 7:10 1.), RSLT ('fe-ulâ'ike' 7:8 7., 'fe-ulâ'ike' 7:9 4.), SUP ('mâ' 7:10 10.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:6 ★ (kaynak pas, z=1,57); 7:7, 7:8, 7:9 ve 7:10 yıldız yok",
 "fâsıla: 7:5 ن → 7:6 ن (" + _F[0] + ") → 7:7 ن (" + _F[1] + ") → 7:8 ن (" + _F[2] + ") → 7:9 ن (" + _F[3] + ") → 7:10 ن (" + _F[4] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:6 xref yok; 7:7 xref yok; 7:8 23:102 (emsal olarak basıldı); 7:9 23:103 (emsal olarak basıldı); 7:10 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok (7:6, 7:7, 7:8, 7:9 ve 7:10 ölçümünde nakarat3 alanı boş)'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:6, 7:7, 7:8, 7:9 ve 7:10 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:6 konuşan 1P ('fe-le-nes'elenne', 've le-nes'elenne'), 3MS ('ursile' — edilgen, naib-i faili 'ileyhim' 4. kelime), 3MP eki ('ileyhim' — gönderge 'llezîne' 2. kelime); "
 "7:7 konuşan 1P ('fe-le-nequssanne', 'kunnâ'), 3MP eki (''aleyhim' — tartışmalı, gönderge 7:6 2. kelime); "
 "7:8 3FS ('sequlet' — fiil uyumu, fail 6. kelime), 3MS eki ('mevâzînuhû' — gönderge 'men' 4. kelime), 3MP ('humu' — gönderge 'ulâ'ike' 7. kelime); "
 "7:9 3FS ('xaffet' — fiil uyumu, fail 3. kelime), 3MS eki ('mevâzînuhû' — gönderge 'men' 1. kelime), 3MP ('xasirû', 'kânû', 'yazlimûn' — gönderge 'llezîne' 5. kelime; ek 'enfusehum' — gönderge 'llezîne' 5. kelime), konuşan 1P eki ('bi-âyâtinâ'); "
 "7:10 konuşan 1P ('mekkennâkum', 've ce'alnâ'), muhatap 2MP ('teşkurûn'; ekler 'mekkennâkum', 'lekum'), 3FS eki ('fîhâ' — gönderge 'l-ardi' 4. kelime)",
 "7:6-10 gönderge zinciri: konuşan 1P (adsız) 7:6, 7:7, 7:9 ('bi-âyâtinâ' 10. kelime) ve 7:10'da, 7:4 ve 7:5'ten sürer; 7:6 'llezîne' (2. kelime) kendilerine gönderilenler; 7:7 ''aleyhim' göndergesi 7:6 2. kelime — tartışmalı (7:6 6. kelime 'l-murselîn' de kapsanabilir; gönderge A1'de de 7:6 2. kelime); "
 "7:8 ve 7:9 'men' göndergeleri 'ulâ'ike' ile çoğula geçer; 7:10 muhatap 2MP (adsız), 7:3 muhatabından sonra yeniden (okuma)",
 "edilgen: 7:6 'ursile' (3. kelime; naib-i faili 'ileyhim') — ölçüm EDİLGEN 1/3; 7:7, 7:8, 7:9 ve 7:10 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:6, 7:7, 7:8, 7:9 ve 7:10 söz yok (okuma); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 6 10 02' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:6 've le-nes'elenne' (5.) CONJ; 7:7 've mâ' (4.) REM; 7:8 've'l-veznu' (1.) CONJ; 7:9 've men' (1.) CONJ; 7:10 've le-qad' (1.) REM, 've ce'alnâ' (5.) CONJ; "
 "'fe' konumları: 7:6 'fe-le-nes'elenne' (1.) REM; 7:7 'fe-le-nequssanne' (1.) CONJ; 7:8 'fe-men' (4.) REM, 'fe-ulâ'ike' (7.) RSLT; 7:9 'fe-ulâ'ike' (4.) RSLT",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:8 ◈K يوم ('yevme'izin' 2. kelime — K2); 7:10 ◈K أرض ('l-ardi' 4. kelime — K1); 7:6, 7:7 ve 7:9 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 6 10 02'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:8 (23:102); 7:9 (23:103); 7:6, 7:7 ve 7:10 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:6 رسل ×2, سأل ×2; 7:8 وزن ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:6 şahıs geçişi 3 → 1, şahıs sayısında beraberlik (1P 2 · 3MP 1 · 3MS 1 — ölçüm baskın 1), edim geçişi yok; 7:7 şahıs geçişi yok, edim geçişi yok; 7:8 şart → cevap ('men' 4. kelime / 'fe-ulâ'ike' 7. kelime), şahıs geçişi 1 → 3, edim geçişi haber → şart; "
 "7:9 şart → cevap ('men' 1. kelime / 'fe-ulâ'ike' 4. kelime), şahıs geçişi yok, edim geçişi yok; 7:10 şahıs geçişi 3 → 1, şahıs sayısında beraberlik (1P 4 · 2MP 4 — ölçüm baskın 1), edim geçişi şart → haber; bölüm kapanışı; "
 "ölçüm iltifât 7:6-10 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:6 'fe-le-nes'elenne' — pekiştirme lâmı ve nûnu (morph EMPH); 7:7 've mâ kunnâ ğâ'ibîn' — olumsuz isim cümlesi (morph REM + NEG); 7:8 've'l-veznu yevme'izini'l-haqq' — isim cümlesi, zaman zarfı arada (morph CONJ + T); "
 "7:8 'fe-men sequlet mevâzînuhû fe-ulâ'ike' — şart ve cevap (morph REM + COND + RSLT); 7:9 've men xaffet mevâzînuhû fe-ulâ'ike' — şart ve cevap (morph CONJ + COND + RSLT); 7:9 'bimâ kânû bi-âyâtinâ yazlimûn' — sebep bildiren ilgi cümlesi (morph REL); "
 "7:10 've le-qad' — pekiştirme (morph REM + EMPH + CERT); 7:10 'qalîlen mâ teşkurûn' — zâid 'mâ' ile pekiştirme (morph SUP)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:8 4-9. kelime — 23:102 ile harekesiz eş (sayım: 'say 7:8 4-9'); 7:9 1-7. kelime — 23:103 ile harekesiz eş (sayım: 'say 7:9 1-7'); "
 "7:10 9-10. kelime — 7:3 ile harekesiz eş (sayım: 'say 7:10 9-10'); 7:6 kök رسل, سأل ikilemeleri; 7:8 kök وزن ikilemesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 02'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'fe-men sequlet mevâzînuhû fe-ulâ'ike humu'l-muflihûn' 7:8 'Tartıları ağır gelenler, işte onlar kurtuluşa erenlerdir' / 23:102 'Tartıları ağır gelenler, işte onlar kurtuluşa erenlerdir' (emsal metninde) — çakışma değil (bayt eşit); "
 "'fe-men sequlet mevâzînuhû' 7:8 'Tartıları ağır gelenler' / 23:102 'Tartıları ağır gelenler' (emsal metninde) — çakışma değil (bayt eşit); "
 "'fe-ulâ'ike humu'l-muflihûn' 7:8 'işte onlar kurtuluşa erenlerdir' / 23:102 'işte onlar kurtuluşa erenlerdir' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ve men xaffet mevâzînuhû fe-ulâ'ike'llezîne xasirû enfusehum' 7:9 'Tartıları hafif gelenler, işte onlar kendilerini ziyana uğratanlardır' / 23:103 'Tartıları hafif gelenler, işte onlar kendilerini ziyana uğratanlardır' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ve men xaffet mevâzînuhû' 7:9 'Tartıları hafif gelenler' / 23:103 'Tartıları hafif gelenler' (emsal metninde) — çakışma değil (bayt eşit); "
 "'fe-ulâ'ike'llezîne xasirû enfusehum' 7:9 'işte onlar kendilerini ziyana uğratanlardır' / 23:103 'işte onlar kendilerini ziyana uğratanlardır' (emsal metninde) — çakışma değil (bayt eşit); "
 "'llezîne xasirû enfusehum' 7:9 'kendilerini ziyana uğratanlardır' / 23:103 'kendilerini ziyana uğratanlardır' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:6 'nes'ele' IMPF IND (1. kelime; 'le' ve 'n' ile) — meal 'soracağız'; 'ursile' PERF PASS — meal 'gönderilenlere'; 'nes'ele' IMPF IND (5. kelime; 'le' ve 'n' ile) — meal 'soracağız'; "
 "7:7 'nequssa' IMPF IND ('le' ve 'n' ile) — meal 'anlatacağız'; 'kunnâ' PERF ('mâ' ile) — meal 'değildik'; 7:8 'sequlet' PERF — meal 'gelenler'; 7:9 'xaffet' PERF — meal 'gelenler'; 'xasirû' PERF — meal 'uğratanlardır'; 'kânû' PERF — meal 'olmaları'; 'yazlimûn' IMPF IND — meal 'zulmetmekte'; "
 "7:10 'mekkennâ' PERF — meal 'yerleştirdik'; 'ce'alnâ' PERF — meal 'ettik'; 'teşkurûn' IMPF IND — meal 'şükrediyorsunuz'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'nes'ele' IMPF 7:6'da ve 'nequssa' IMPF 7:7'de gelecek zaman ('-acağız') ile; 'ursile' PERF 7:6'da sıfat-fiil ('-en') ile; 'sequlet' PERF 7:8'de ve 'xaffet' PERF 7:9'da sıfat-fiil ('-en') ile; 'xasirû' PERF 7:9'da sıfat-fiil ('-an') ile; 'kânû' PERF 7:9'da ad-fiil ('-maları') ile; 'yazlimûn' IMPF 7:9'da sürerlik ('-mekte') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'iz' ('O' / '-diğinde') — çakışma değil ('yevme'izin' birleşiğinde işaret, 7:5'te zaman bağlacı)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 6 10 02'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:6, 7:7, 7:8, 7:9 ve 7:10 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:6, 7:7, 7:8, 7:9 ve 7:10 ayet içi karşıt çift yok; ayetler arası: 7:8 / 7:9 ('sequlet' / 'xaffet'); eşleme betikle: ADAY_P",
 "aday 1041: kök كون 7:7 ('kunnâ') ve 7:9 ('kânû'), 7:2 ('yekun') ve 7:5 ('kâne', 'kunnâ') ile bölüm içi; kök وزن 7:8 ('l-veznu', 'mevâzînuhû') ve 7:9 ('mevâzînuhû'); kök ظلم 7:9 ('yazlimûn'), 7:5 ('zâlimîn') ile bölüm içi; kök قلل 7:10 ('qalîlen'), 7:3 ('qalîlen') ile bölüm içi; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 1-2 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 1 ve 2; bölüm kapanışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b02/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 6 10 02'; lem_bozuk.py 02 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 6 10 → AYN_SONUC; sunum/bolum4_kurallar.py 6 10 02 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 6 10 02 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 36)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 2 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('men', 'sequlet' (morph LEM ham biçim), 'mîzân', 'zâ', 'muflih', 'xaffet' (morph LEM ham biçim), 'ellezî', 'xasira', 'nefs'); joker '_' yalnız lemmasız 'hum' öğesinde ('dizi 7 8 4 9'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (6, 10): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_6_10.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b40k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '6', '10'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '6', '10', '02'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '6', '10', '02'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '6', '10', '02', '--tazelik-yok')}
    for _n in range(7, 36): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '6', '10', '02')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35 = [_R['B%d' % _n].splitlines() for _n in range(6, 36)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
