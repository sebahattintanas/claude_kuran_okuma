# sûre 7 blok 1 (7:1-5) ARIZA oluşturucu — bölüm 1-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b01/olcum.txt'
os.environ['SAY2'] = '/home/claude/b01/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = [l.strip().rstrip(',') for l in open('/home/claude/yamalar/devir_6_165.txt', encoding='utf-8') if l.startswith('  "devir (')]; BEK = [ast.literal_eval(x) for x in BEK]
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
 ("7:5", "'illâ en qâle'", 2, 'say 7:5 7-9', "harekesiz 'illâ en qâlû' (7-9. kelime)", ('dizi 7 5 7 9', "illâ en qâle", '7-9', "biçim farkı (dizi 7 5 7 9): basılmamış eş yazım eş")),
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

VF_YAZI = {1: {}, 2: {12: "'ve zikrâ'"}, 3: {7: "'ve lâ'"}, 4: {1: "'ve kem'"}, 5: {}}
sys.path.insert(0, '/home/claude/b01/yap')
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
open('/home/claude/b01/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '01')
BLOKLAR = [str(i) for i in range(1, 2)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '1', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b01/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '1', '5', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b01/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b01/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '1', '5', '01').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_1_5.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:1', '7:2', '7:3', '7:4', '7:5'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_1_5.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(1, 6))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:2 kök صدر ('sadrike' 7. kelime — göğüs): tetik listesinde yok; 7:3 kök ولي ('evliyâ'' 11. kelime — dost): tetik listesinde yok; 7:4 kök هلك ('ehleknâhâ' 4. kelime — helâk et-): tetik listesinde yok; 7:5 'iz' (4. kelime — morph T, zaman)"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '1', '5', '01')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b01/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 2)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(1, 6))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l for l in open('/home/claude/b01/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b01/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % n, _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta sunum/kelime_kontrol.py (bölüm 10 denetimi kuralı 6) morph INL etiketli kelimede (7:1 harf dizisi) harf adı alıntısını iskelet karşılaştırmasına sokmaz — harf adları ('elif lâm mîm sâd') yazılı biçimin harf iskeletiyle eşlenemiyor; başka araç kuralı değişmedi; bölüm 19 kapanışı (sunum/bolum35_kurallar.py kural 1-5) ve sûre 7 hazırlığı (sunum/sure.py ile sunum/sinifla.py varsayılan sûresi 7; sunum/denetim_7.sh; mutasyon_sina sûre 6 sınamaları sûre 6 blok dizinleriyle) önceki commit'lerde, hazırlık sonu mutasyon sınaması 374 / 374; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 358",
 "geriye dönük koşu (bölüm 19 kapanışı, sûre 6 kayıtlarında, komut 'python3 sunum/geriye_donuk.py b40k yamalar/geriye_donuk_6_b38k.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 1 5 01'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:2 've zikrâ li'l-mu'minîn' (12-13. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (inanan insanlar); 7:3 've lâ tettebi'û min dûnihî evliyâ'' (7-11. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (O'ndan başka edinilen dostlar) (yamalar/esma_el_7_1_5.txt); 7:1, 7:4 ve 7:5 esmâ yok; 7:3 Rab (6. kelime); 7:1, 7:2, 7:4 ve 7:5 lafız ve Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 1 5 01'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 7:2 ve 7:3 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı; muhur_el hayır): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (1, 2, 3, 4, 5)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 1 5 01'): KALAN_P",
 "ölçüm aktör: 7:4 adsız `karye` 3. sırada (A1'de 'qaryetin'); 7:1, 7:2, 7:3 ve 7:5 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:1 haber — kip yok; 7:2 yasak — PRO 1 'lâ' (4.); ölçüm biçim NEHY (D2'de yazılmadı); 7:3 emir, yasak — IMPV 1 'ittebi'û' (1.), PRO 1 'lâ' (7.); ölçüm biçim NEHY (D2'de yazılmadı); "
 "7:4 haber — kip yok; 7:5 haber — NEG 1 'mâ' (1.), RES 1 'illâ' (7.); ölçüm biçim HASR (D2'de yazılmadı); "
 "morph REM ('fe-lâ' 7:2 4., 've kem' 7:4 1.), PRP ('li-tunzire' 7:2 10.), SUP ('mâ' 7:3 13.), SUB ('en' 7:5 8.), ACC ('innâ' 7:5 10.), INL (7:1 1.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:2 ★ (kaynak pas, z=1,57); 7:1, 7:3, 7:4 ve 7:5 yıldız yok",
 "fâsıla: 7:1 ٓ (" + _F[0] + ") → 7:2 ن (" + _F[1] + ") → 7:3 ن (" + _F[2] + ") → 7:4 ن (" + _F[3] + ") → 7:5 ن (" + _F[4] + ") — sûre açılışı ٓ sınıfında (harf dizisi), ardından N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:1 xref yok; 7:2 xref yok; 7:3 xref yok; 7:4 xref yok; 7:5 21:14 (emsal olarak basıldı), 21:46 (emsal olarak basıldı)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:5 'illâ en qâle' süzgeç GEÇMEZ; 7:1, 7:2, 7:3 ve 7:4 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:1 zamir ve fiil yok (harf dizisi); "
 "7:2 3MS ('unzile' — edilgen, naib-i faili 'kitâbun' 1. kelime; 'yekun' — fiil uyumu, fail 8. kelime; 'minhu', 'bihî' eki — gönderge 'kitâbun' 1. kelime), muhatap 2MS ('li-tunzire'; ekler 'ileyke', 'sadrike'); "
 "7:3 muhatap 2MP ('ittebi'û', 'tettebi'û', 'tezekkerûn'; ekler 'ileykum', 'rabbikum'), 3MS ('unzile' — edilgen, naib-i faili 'mâ' 2. kelime; 'dûnihî' eki — gönderge 'rabbikum' 6. kelime); "
 "7:4 konuşan 1P ('ehleknâhâ'; ek 'be'sunâ'), 3FS eki ('ehleknâhâ', 'fe-câ'ehâ' — gönderge 'qaryetin' 3. kelime), 3MS ('fe-câ'ehâ' — fiil uyumu, fail 6. kelime), 3MP ('hum' — tartışmalı, cins uyumsuz, gönderge 'qaryetin' 3. kelime), aktör adsız 'qaryetin'; "
 "7:5 3MS ('kâne' — fiil uyumu, fail 3. kelime; 'câ'ehum' — fiil uyumu, fail 6. kelime), 3MP ('qâlû' — gönderge 7:4 9. kelime; ekler 'da'vâhum', 'câ'ehum' — gönderge 7:4 9. kelime), konuşan 1P eki ('be'sunâ'), konuşan 1P ('kunnâ' — söz içi; ek 'innâ' — söz içi)",
 "7:1-5 gönderge zinciri: 7:2 muhatap 2MS (adsız), 7:3'te muhatap 2MP'ye geçiş (1. kelime); 7:2 'minhu' ve 'bihî' göndergesi 'kitâbun' (1. kelime); 7:3 'dûnihî' göndergesi 'rabbikum' (6. kelime); 7:4 konuşan 1P (adsız) 7:5'te sürer ('be'sunâ' 6. kelime); 7:4 3FS ekleri 'qaryetin' (3. kelime), 'hum' (9. kelime) şehrin halkına geçiş — tartışmalı (cins ve sayı uyumu yok; gönderge A1'de de 'qaryetin' 3. kelime); "
 "7:5 3MP göndergeleri 7:4 9. kelime; 7:5 söz içi konuşan 1P sözü söyleyenler, söz dışı konuşan 1P'den ayrı (okuma)",
 "edilgen: 7:2 'unzile' (2. kelime; naib-i faili 'kitâbun') — ölçüm EDİLGEN 1/3; 7:3 'unzile' (3. kelime; naib-i faili 'mâ') — ölçüm EDİLGEN 1/4; 7:1, 7:4 ve 7:5 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:5 'qâlû' (9.) ardından söz 10-12. kelime, ayet sonunda kapanır; 7:1, 7:2, 7:3 ve 7:4 söz yok (okuma); mealde 'demeleri oldu:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 1 5 01' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:2 've zikrâ' (12.) CONJ; 7:3 've lâ' (7.) CONJ; 7:4 've kem' (1.) REM; "
 "'fe' konumları: 7:2 'fe-lâ' (4.) REM; 7:4 'fe-câ'ehâ' (5.) CONJ; 7:5 'fe-mâ' (1.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:1, 7:2, 7:3, 7:4 ve 7:5 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 1 5 01'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:5 (21:14, 21:46); 7:1, 7:2, 7:3 ve 7:4 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:3 تبع ×2; 7:5 كون ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11); medde sayımının basılmış eşi (yazım farkı ile, D3 dışı): 'say 7:5 4-6 --medde' 6:43",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:1 bölüm açılışı (sûre açılışı); 7:2 şahıs geçişi — → 3 (eksiltili — 7:1 şahıs işareti taşımıyor), edim geçişi haber → yasak; 7:3 şahıs geçişi 3 → 2, edim geçişi yasak → emir, yasak; 7:4 şahıs geçişi 2 → 1, şahıs sayısında toplam farkı (1P 3 · 3. şahıs 4 — ölçüm baskın 1), edim geçişi emir, yasak → haber; "
 "7:5 söz açılır (10. kelime), söz kapanır (12. kelime, ayet içi), şahıs geçişi 1 → 3, edim geçişi yok; "
 "ölçüm iltifât 7:1-5 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:2 'fe-lâ yekun fî sadrike haracun minhu' — ara cümle, yasak (morph REM + PRO); 7:2 'li-tunzire bihî' — gerekçe lâmı (morph PRP); 7:3 'qalîlen mâ tezekkerûn' — zâid 'mâ' ile pekiştirme (morph SUP); "
 "7:4 've kem min qaryetin' — çokluk bildiren 'kem' (morph REM); 7:4 'ev hum qâ'ilûn' — isim cümlesinin atfı (morph CONJ); 7:5 'fe-mâ kâne da'vâhum' ve 'illâ en qâlû' — olumsuzluk ve hasr (morph NEG + RES + SUB)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:1 harf dizisi 'elif lâm mîm sâd' ile açılıyor (sayım: 'say 7:1 1-1'); 7:5 10-12. kelime — 21:14 ve 21:46 ile harekesiz eş (sayım: 'say 7:5 10-12'); 7:3 kök تبع ikilemesi; 7:5 kök كون ikilemesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 01'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'innâ kunnâ zâlimîn' 7:5 'Biz gerçekten zalimmişiz' / 21:14 'Biz gerçekten zalimmişiz' (emsal metninde) — çakışma değil (bayt eşit); "
 "'innâ kunnâ zâlimîn' 7:5 'gerçekten zalimmişiz' / 21:46 'gerçekten zalimmişiz' (emsal metninde) — çakışma değil (bayt eşit); "
 "'kunnâ zâlimîn' 7:5 'zalimmişiz' / 21:14 'zalimmişiz' (emsal metninde) — çakışma değil (bayt eşit); 'kunnâ zâlimîn' 7:5 'zalimmişiz' / 21:46 'zalimmişiz' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:1 fiil yok; 7:2 'unzile' PERF PASS — meal 'indirilen'; 'yekun' IMPF JUS ('lâ' ile) — meal 'olmasın'; 'tunzire' IMPF SUBJ ('li' ile) — meal 'uyarman'; "
 "7:3 'ittebi'û' IMPV — meal 'uyun'; 'unzile' PERF PASS — meal 'indirilene'; 'tettebi'û' IMPF JUS ('lâ' ile) — meal 'uymayın'; 'tezekkerûn' IMPF IND — meal 'düşünüyorsunuz'; "
 "7:4 'ehleknâ' PERF — meal 'ettik'; 'câ'e' PERF — meal 'geldi'; 7:5 'kâne' PERF ('mâ' ile) — meal 'oldu'; 'câ'e' PERF — meal 'geldiğinde'; 'qâlû' PERF ('en' ile) — meal 'demeleri'; 'kunnâ' PERF — meal 'zalimmişiz'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'unzile' PERF 7:2 ve 7:3'te sıfat-fiil ('-en') ile; 'tunzire' IMPF SUBJ 7:2'de ad-fiil ('-man') ile; 'câ'e' PERF 7:5'te zarf-fiil ('-diğinde') ile; 'qâlû' PERF 7:5'te ad-fiil ('-meleri') ile; 'kunnâ' PERF 7:5'te ek fiil ('-mişiz') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): bölümün önceki bloğu yok",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 1 5 01'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:1, 7:2, 7:3, 7:4 ve 7:5 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:1, 7:2, 7:3, 7:4 ve 7:5 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök نزل 7:2 ('unzile') ve 7:3 ('unzile'); kök ذكر 7:2 ('zikrâ') ve 7:3 ('tezekkerûn'); kök جيأ 7:4 ('fe-câ'ehâ') ve 7:5 ('câ'ehum'); kök بأس 7:4 ('be'sunâ') ve 7:5 ('be'sunâ'); kök كون 7:2 ('yekun') ve 7:5 ('kâne', 'kunnâ'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 1-1 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 1 ve 2; bu blok bölümü ve sûreyi açıyor; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b01/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 1 5 01'; lem_bozuk.py 01 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 1 5 → AYN_SONUC; sunum/bolum4_kurallar.py 1 5 01 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 1 5 01 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 36)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 1 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('illâ', 'en', 'qâle', 'inne', 'kâne', 'zâlim'); joker '_' kullanılmadı; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (1, 5): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_1_5.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01',):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b40k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '1', '5'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '1', '5', '01'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '1', '5', '01'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '1', '5', '01', '--tazelik-yok')}
    for _n in range(7, 36): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '1', '5', '01')
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
