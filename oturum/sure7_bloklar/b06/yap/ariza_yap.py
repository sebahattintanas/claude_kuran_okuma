# sûre 7 blok 6 (7:22-25) ARIZA oluşturucu — bölüm 2-4
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b06/olcum.txt'
os.environ['SAY2'] = '/home/claude/b06/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
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
 ("7:23", "'ğafera _ rahime'", 2, 'say 7:23 7-9', "harekesiz 'teğfir lenâ ve terhamnâ' (7-9. kelime)", ('dizi 7 23 7 9', "ğafera _ rahime", '7-9', "biçim farkı (dizi 7 23 7 9): basılmamış eş fiil çekimi, önek")),
 ("7:23", "'kâne min xâsir'", 2, 'say 7:23 10-12', "harekesiz 'le-nekûnenne mine'l-xâsirîn' (10-12. kelime)", ('dizi 7 23 10 12', "kâne min xâsir", '10-12', "biçim farkı (dizi 7 23 10 12): basılmamış eş yazım eş")),
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

VF_YAZI = {22: {9: "'ve tafiqâ'", 15: "'ve nâdâhumâ'", 22: "'ve aqul'"}, 23: {5: "'ve in'", 9: "'ve terhamnâ'"}, 24: {6: "'ve lekum'", 10: "'ve metâ'un'"}, 25: {4: "'ve fîhâ'", 6: "'ve minhâ'"}}
sys.path.insert(0, '/home/claude/b06/yap')
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
open('/home/claude/b06/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '06')
BLOKLAR = [str(i) for i in range(1, 7)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '6', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b06/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '22', '25', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b06/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b06/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '22', '25', '06').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_22_25.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:22', '7:23', '7:24', '7:25'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_22_25.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(22, 26))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:22 'lemmâ' (3. kelime — morph T, zaman); 7:22 kök سوأ ('sev'âtuhumâ' 8. kelime — çirkin yer): tetik listesinde yok; 7:23 kök نفس ('enfusenâ' 4. kelime — kendi): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '22', '25', '06')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b06/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 7)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(22, 26))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l.replace('**', '') for l in open('/home/claude/b06/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b06/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 21), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
def _esc(t):
    for c in '.()[]|+': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[0]).group(0))
_ES1 = _esc(re.search(r'esmâ \S+ 28\. sırada, SON konum, MÜHÜRSÜZ', _OL[0]).group(0))
for _k, _v in (('_AK1', _AK1), ('_ES1', _ES1)): _MB = _MB.replace('" + %s + "' % _k, _v)
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; blok 5'te sunum/bolum16_kurallar.py (kural 1), sunum/bolum4_kurallar.py (kural 9), sunum/bolum7_kurallar.py (kural 3) ve sunum/edat_etiket.py düzeltmeleri önceki commit'te; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 388",
 "geriye dönük koşu (sûre 7 bölüm 1 kapanışı, komut 'python3 sunum/geriye_donuk.py b02k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 22 25 06'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:22 'inne'ş-şeytâne lekumâ 'aduvvun mubîn' (24-28. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (şeytanın düşmanlık sıfatı) (yamalar/esma_el_7_22_25.txt); 7:23, 7:24 ve 7:25 esmâ yok; 7:22 Rab (16. kelime); 7:23 Rab (2. kelime); 7:24 ve 7:25 lafız ve Rab yok; 7:22 ve 7:23 lafız yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 22 25 06'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 7:22 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı; muhur_el hayır): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (22, 23, 24, 25)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 22 25 06'): KALAN_P",
 "ölçüm aktör: 7:22 '{{1|" + _AK1 + "}}' (A1'de 'l-cenneti' ve 'ş-şeytâne'); 7:23, 7:24 ve 7:25 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:22 soru — INTG 1 'e-lem' (17.; 'e'), NEG 1 'e-lem' (17.; 'lem'); "
 "7:23 şart — COND 1 'in' (5.), EMPH 2 'le-nekûnenne' (10.; 'le' ve pekiştirme nûnu), NEG 1 'lem' (6.); 7:24 emir — IMPV 1 'hbitû' (2.); 7:25 haber — kip yok; "
 "morph REM ('fe-lemmâ' 7:22 3., 've nâdâhumâ' 7:22 15.), DIST ve ADDR ('tilkume' 7:22 20.), ACC ('inne' 7:22 24.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:22 ★ (kaynak n, z=1,65); 7:23, 7:24 ve 7:25 yıldız yok",
 "fâsıla: 7:21 ن → 7:22 ن (" + _F[0] + ") → 7:23 ن (" + _F[1] + ") → 7:24 ن (" + _F[2] + ") → 7:25 ن (" + _F[3] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:22 20:121 (emsal olarak basıldı); 7:23 okunmuş 3 ayet; 7:24 2:36 (emsal olarak basıldı); 7:25 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:23 'ğafera _ rahime' süzgeç GEÇMEZ, 'kâne min xâsir' süzgeç GEÇMEZ; 7:22, 7:24 ve 7:25 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:22 3MS ('fe-dellâhumâ' — gönderge 7:20 3. kelime; 've nâdâhumâ' — fiil uyumu, fail 16. kelime), 3D eki ('fe-dellâhumâ', 'lehumâ', 'sev'âtuhumâ', 'yaxsifâni', ''aleyhimâ', 've nâdâhumâ', 'rabbuhumâ' — gönderge 7:19 6. kelime), 3MD ('zâqe', 've tafiqâ', 'yaxsifâni' — gönderge 7:19 6. kelime), 3FS ('bedet' — fiil uyumu, fail 8. kelime), "
 "konuşan 1S ('enhekumâ', 've aqul' — söz içi), muhatap 2D eki ('enhekumâ', 'lekumâ', 'lekumâ' — söz içi), aktör adlı 'l-cenneti' ve 'ş-şeytâne'; "
 "7:23 3MD ('qâlâ' — gönderge 7:19 6. kelime), konuşan 1P ('zalemnâ', 'le-nekûnenne' — söz içi; ekler 'rabbenâ', 'enfusenâ', 'lenâ', 've terhamnâ' — söz içi), muhatap 2MS ('teğfir' — söz içi), 3FS ('ve terhamnâ' — söz içi; morph etiketi, okuma muhatap 2MS); "
 "7:24 3MS ('qâle' — gönderge 7:22 16. kelime), muhatap 2MP ('hbitû' — söz içi; ekler 'ba'dukum', 've lekum' — söz içi); "
 "7:25 3MS ('qâle' — gönderge 7:22 16. kelime), 3FS eki ('fîhâ', 've fîhâ', 've minhâ' — söz içi; gönderge 7:24 8. kelime), muhatap 2MP ('tahyevne', 'temûtûne' — söz içi; 'tuxracûn' — söz içi; edilgen, naib-i faili zamir)",
 "7:22-25 gönderge zinciri: 7:22 'fe-dellâhumâ' (1. kelime) fiili 7:20 3. kelimeye (şeytan); 7:22 ve 7:23 ikil 3. şahıs fiil ve ekleri 7:19 6. kelimeye (iki muhatap); 7:22 söz içi konuşan 1S 'rabbuhumâ' (16. kelime), muhatap 2D yine o iki kişi; 7:23 söz içi konuşan 1P o iki kişi, muhatap 2MS 'rabbenâ' (2. kelime); "
 "7:23 've terhamnâ' (9. kelime) morph etiketi 3FS, okuma 7. kelimeyle eş özne; 7:24 ve 7:25 'qâle' fiilleri 7:22 16. kelimeye; 7:24 söz içi muhatap çoğul (2MP) — ikilden çoğula geçiş, kapsamı metinde adsız; 7:25 3FS ekleri 7:24 8. kelimeye ('l-ardi') (okuma)",
 "edilgen: 7:25 'tuxracûn' (7. kelime; naib-i faili zamir) — ölçüm EDİLGEN 1/4; 7:22, 7:23 ve 7:24 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:22 've nâdâhumâ rabbuhumâ' (15-16.) ardından söz biçimli içerik 17-28. kelime — fiil قول kökünden değil; A3'e '(söz biçimli içerik, 17. kelimeden)', A4'te 'söz açılır' / 'söz kapanır' yazılmadı (okuma); "
 "7:22 içteki 've aqul lekumâ' (22-23.) ardından aktarılan söz 24-28. kelime — dış sözle birlikte ayet sonunda kapanır (okuma); 7:23 'qâlâ' (1.) ardından söz 2-12. kelime — ayet içi kapanış; 7:24 'qâle' (1.) ardından söz 2-12. kelime — ayet içi kapanış; 7:25 'qâle' (1.) ardından söz 2-7. kelime — ayet içi kapanış; "
 "mealde 'seslendi:', 'demedim mi:', 'Dediler ki:' ve 'Dedi ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 22 25 06' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:22 've tafiqâ' (9.) CONJ, 've nâdâhumâ' (15.) REM, 've aqul' (22.) CONJ; 7:23 've in' (5.) CONJ, 've terhamnâ' (9.) CONJ; 7:24 've lekum' (6.) CONJ, 've metâ'un' (10.) CONJ; 7:25 've fîhâ' (4.) CONJ, 've minhâ' (6.) CONJ; "
 "'fe' konumları: 7:22 'fe-dellâhumâ' (1.) CONJ, 'fe-lemmâ' (3.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:22 ◈B شجر ('ş-şecerate' 5. kelime, 'ş-şecerati' 21. kelime — B1); 7:24 ◈K أرض ('l-ardi' 8. kelime — K1), 7:24 ◈K حين ('hîn' 12. kelime — K2); 7:25 ◈B حيي ('tahyevne' 3. kelime — B4), 7:25 ◈B موت ('temûtûne' 5. kelime — B4); 7:23 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 22 25 06'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:22 (20:121); 7:24 (2:36); 7:23 ve 7:25 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:22 شجر ×2; 7:24 بعض ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:22 söz biçimli içerik (A4'te söz kaydı yok), şahıs geçişi yok, edim geçişi haber → soru; 7:23 söz açılır (2. kelime), söz kapanır (12. kelime, ayet içi), şart → cevap (ayet içi; COND 'in' 5. kelime), şahıs geçişi 3 → 1, edim geçişi soru → şart; "
 "7:24 söz açılır (2. kelime), söz kapanır (12. kelime, ayet içi), şahıs geçişi 1 → 2, edim geçişi şart → emir; 7:25 söz açılır (2. kelime), söz kapanır (7. kelime, ayet içi), şahıs geçişi yok, edim geçişi emir → haber, bölüm kapanışı; "
 "ölçüm iltifât 7:22-25 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:22 'fe-lemmâ zâqe'ş-şecerate' — zaman bağlacıyla açılan yan cümle (morph REM + T + PERF); 7:22 've tafiqâ yaxsifâni' — başlama fiili ve ardındaki muzâri (morph CONJ + PERF + IMPF); 7:22 'e-lem enhekumâ' — olumsuz soru (morph INTG + NEG + JUS); "
 "7:23 've in lem teğfir lenâ' — olumsuz şart (morph CONJ + COND + NEG + JUS); 7:23 'le-nekûnenne' — tekitli muzâri, şartın cevabı (morph EMPH + IMPF); 7:25 'fîhâ tahyevne' — öne alınmış harfi cerli tümleç (morph P + IMPF)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:22 8-14. kelime — 20:121 ile harekesiz eş (sayım: 'say 7:22 8-14'); 7:24 2-12. kelime — 2:36 ile harekesiz eş (sayım: 'say 7:24 2-12'); 7:24 1. kelimenin çekimi 2:36'dakinden ayrı (sayım: 'dizi 7 24 1 12'); "
 "7:22 kök شجر ikilemesi; 7:24 kök بعض ikilemesi; 7:23 10-12. kelime sûre içinde okunmamış 1 ayetle harekesiz eş (sayım: 'say 7:23 10-12')",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 06'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'lehumâ sev'âtuhumâ' 7:22 'çirkin yerleri kendilerine' / 20:121 'çıplaklıkları kendilerine' (emsal metninde) — çakışma — tam okuma sonu ('sev'e' karşılığı 'çirkin yer' / 'çıplaklık'); "
 "'ve tafiqâ yaxsifâni 'aleyhimâ min varaqi'l-cenneti' 7:22 've bahçe yaprağından üzerlerine yamamaya koyuldular' / 20:121 've cennet yaprağından üzerlerine yamamaya koyuldular' (emsal metninde) — çakışma — tam okuma sonu ('cenne' karşılığı 'bahçe' / 'cennet'); "
 "'sev'âtuhumâ ve tafiqâ yaxsifâni 'aleyhimâ min varaqi'l-cenneti' 7:22 'çirkin yerleri kendilerine göründü ve bahçe yaprağından üzerlerine yamamaya koyuldular' / 20:121 'çıplaklıkları kendilerine göründü ve cennet yaprağından üzerlerine yamamaya koyuldular' (emsal metninde) — çakışma — tam okuma sonu ('sev'e' ve 'cenne' karşılıkları; alıntı 6. ve 7. kelime karşılıklarını da taşıyor); "
 "'ba'dukum li-ba'din 'aduvvun' 7:24 'birbiriniz için düşmansınız' / 2:36 'birbiriniz için düşmansınız' (emsal metninde) — çakışma değil (bayt eşit); "
 "'hbitû ba'dukum li-ba'din 'aduvvun' 7:24 'İnin; birbiriniz için düşmansınız' / 2:36 'İnin; birbiriniz için düşmansınız' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ve lekum fi'l-ardi musteqarrun ve metâ'un ilâ hîn' 7:24 'Yeryüzünde size bir vakte kadar kalacak yer ve geçimlik var' / 2:36 'Yeryüzünde size bir vakte kadar kalacak yer ve geçimlik var' (emsal metninde) — çakışma değil (bayt eşit); "
 "'hbitû ba'dukum li-ba'din 'aduvvun ve lekum fi'l-ardi musteqarrun ve metâ'un ilâ hîn' 7:24 'İnin; birbiriniz için düşmansınız. Yeryüzünde size bir vakte kadar kalacak yer ve geçimlik var' / 2:36 'İnin; birbiriniz için düşmansınız. Yeryüzünde size bir vakte kadar kalacak yer ve geçimlik var' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:22 'dellâ' PERF — meal 'düşürdü'; 'zâqe' PERF ('lemmâ' ile) — meal 'tattıklarında'; 'bedet' PERF — meal 'göründü'; 'tafiqâ' PERF — meal 'koyuldular'; 'yaxsifâni' IMPF — meal 'yamamaya'; "
 "'nâdâ' PERF — meal 'seslendi'; 'enhe' IMPF JUS ('lem' ile) — meal 'yasaklamadım'; 'aqul' IMPF JUS — meal 'demedim'; "
 "7:23 'qâlâ' PERF — meal 'Dediler'; 'zalemnâ' PERF — meal 'zulmettik'; 'teğfir' IMPF JUS ('lem' ile) — meal 'bağışlamaz'; 'terham' IMPF JUS — meal 'etmezsen'; 'nekûnenne' IMPF ('le' ile) — meal 'oluruz'; "
 "7:24 'qâle' PERF — meal 'Dedi'; 'hbitû' IMPV — meal 'İnin'; "
 "7:25 'qâle' PERF — meal 'Dedi'; 'tahyevne' IMPF — meal 'yaşarsınız'; 'temûtûne' IMPF — meal 'ölürsünüz'; 'tuxracûn' IMPF PASS — meal 'çıkarılırsınız'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'zâqe' PERF 7:22'de zarf-fiil ('-tıklarında') ile; 'yaxsifâni' IMPF 7:22'de ad-fiil ('-maya') ile; 'enhe' ve 'aqul' IMPF JUS 7:22'de 'lem' ile olumsuz geçmiş ('-madım', '-medim') ile; 'teğfir' ve 'terham' IMPF JUS 7:23'te 'in' ve 'lem' ile olumsuz geniş zaman ('-maz', '-mezsen') ile; 'nekûnenne' IMPF 7:23'te geniş zaman ('-uruz') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'illâ' ('ancak' / 'hariç') — çakışma değil (hasr edatı morph RES, istisna edatı morph EXP); 'fe' (REM: 'Derken' / 'Hemen' / karşılıksız) — çakışma değil (anlatı geçişi, emir önünde ivedilik, Türkçe sıralama); 'fe' (CONJ: 'Böylece' / karşılıksız) — çakışma değil (sonuç bağı, Türkçe sıralama); 've' (CONJ: 'ama' / 've' / 'ise' / karşılıksız) — çakışma değil (yasak önünde karşıtlık, atıf, Türkçe sıralama); 've' (REM: karşılıksız) — çakışma değil (anlatı geçişi cümle başıyla); 'kumâ' ('size' / 'sizin' / iyelik eki) — çakışma değil (yönelme ve tamlayan çekimi, tamlama)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 22 25 06'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:22, 7:23, 7:24 ve 7:25 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:25 ('tahyevne' / 'temûtûne'); 7:22, 7:23 ve 7:24 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök ربب 7:22 ('rabbuhumâ') ve 7:23 ('rabbenâ'); kök قول 7:22 ('ve aqul'), 7:23 ('qâlâ'), 7:24 ('qâle') ve 7:25 ('qâle'); kök عدو 7:22 (''aduvvun') ve 7:24 (''aduvvun'); kök شجر 7:22 ('ş-şecerate', 'ş-şecerati'), 7:19 ('ş-şecerate') ile bölüm içi; kök نهي 7:22 ('enhekumâ'), 7:20 ('nehâkumâ') ile bölüm içi; kök سوأ 7:22 ('sev'âtuhumâ'), 7:20 ('sev'âtihimâ') ile bölüm içi; "
 "kök شطن 7:22 ('ş-şeytâne'), 7:20 ('ş-şeytânu') ile bölüm içi; kök هبط 7:24 ('hbitû'), 7:13 ('fe'hbit') ile bölüm içi; kök خرج 7:25 ('tuxracûn'), 7:18 ('xruc') ile bölüm içi; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 2-4 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 3, 4, 5 ve 6; bölüm kapanışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b06/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 22 25 06'; lem_bozuk.py 06 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 22 25 → AYN_SONUC; sunum/bolum4_kurallar.py 22 25 06 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 22 25 06 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 37)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 6 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('bedâ', 'sev'e', 'tafiqa', 'yaxsife' (morph LEM ham biçim), ''alâ', 'min', 'varaq', 'cenne', 'ğafera', 'rahime', 'kâne', 'xâsir', 'qâle', 'yehbitu' (morph LEM ham biçim), 'ba'd', ''aduvv', 'fî', 'ard', 'musteqarr', 'metâ'', 'ilâ', 'hîn'); "
 "joker '_' yalnız lemmasız öğelerde ('lehumâ' — 'dizi 7 22 6 14'; 'lenâ' — 'dizi 7 23 7 9'; 've lekum' — 'dizi 7 24 2 12', 'dizi 7 24 1 12'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (22, 25): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_22_25.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_7_b02k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '22', '25'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '22', '25', '06'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '22', '25', '06'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '22', '25', '06', '--tazelik-yok')}
    for _n in range(7, 37): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '22', '25', '06')
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
