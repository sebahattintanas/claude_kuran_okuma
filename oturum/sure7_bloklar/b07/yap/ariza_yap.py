# sûre 7 blok 7 (7:26-27) ARIZA oluşturucu — bölüm 3-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b07/olcum.txt'
os.environ['SAY2'] = '/home/claude/b07/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = list(ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_7_b06.txt', encoding='utf-8').read() + ']'))
VF_YAZI_ESKI = {}
BOL = "'Ey Âdemoğulları: giysi, fitne, ziynet; haram kılınanlar'"


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
 ("7:27", "'min haysu lâ'", 2, 'say 7:27 20-22', "harekesiz 'min haysu lâ' (20-22. kelime)", ('dizi 7 27 20 22', "min haysu lâ", '20-22', "biçim farkı (dizi 7 27 20 22): basılmamış eş yazım eş")),
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

VF_YAZI = {26: {9: "'ve rîşen'", 10: "'ve libâsu'"}, 27: {19: "'ve qabîluhû'"}}
sys.path.insert(0, '/home/claude/b07/yap')
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
open('/home/claude/b07/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '07')
BLOKLAR = [str(i) for i in range(1, 8)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '7', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b07/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '26', '27', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b07/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b07/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '26', '27', '07').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_26_27.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:26', '7:27'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_26_27.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(26, 28))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:26 kök سوأ ('sev'âtikum' 8. kelime — çirkin yer): tetik listesinde yok; 7:27 kök سوأ ('sev'âtihimâ' 15. kelime — çirkin yer): tetik listesinde yok; 7:27 kök قبل ('qabîluhû' 19. kelime — topluluk): tetik listesinde yok; 7:27 kök ولي ('evliyâ'e' 27. kelime — dost): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '26', '27', '07')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b07/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 8)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(26, 28))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l.replace('**', '') for l in open('/home/claude/b07/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b07/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 25), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol mecrur\)', _OL[0]).group(0))
_AK2 = _esc(re.search(r'aktör: adlı .*rol fail\+meful\)', _OL[1]).group(0))
_ES2 = _esc(re.search(r'esmâ \S+ 27\. sırada, ORTA konum, MÜHÜRSÜZ', _OL[1]).group(0))
_HP = _esc(re.search(r'HAPAKS: .*? — hapaks z=3,28', _OL[0]).group(0))
for _k, _v in (('_AK1', _AK1), ('_AK2', _AK2), ('_ES2', _ES2), ('_HP', _HP)): _MB = _MB.replace('" + %s + "' % _k, _v)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; bölüm 2 kapanışında sunum/bolum37_kurallar.py (kural 1-5) eklendi, sunum/geriye_donuk.py ve mutasyon_sina buna göre güncellendi — önceki commit'te, kapanış mutasyon sınaması 395 / 395; yeni kök ريش (7:26 9. kelime 've rîşen'; yamalar/yama_kok_7_26.py → kok_ekle_7.py, kok_turkce 1634; ölçüm yeniden alındı); mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 390",
 "geriye dönük koşu (sûre 7 bölüm 2 kapanışı, komut 'python3 sunum/geriye_donuk.py b06k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 26 27 07'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:27 'innâ ce'alne'ş-şeyâtîne evliyâ'e lillezîne lâ yu'minûn' (24-30. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (inanmayanların dostu kılınan şeytanlar) (yamalar/esma_el_7_26_27.txt); 7:26 esmâ yok; 7:26 lafız (17. kelime); 7:27 lafız yok; 7:26 ve 7:27 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 26 27 07'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 7:27 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı; muhur_el hayır): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (26, 27)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 26 27 07'): KALAN_P",
 "ölçüm aktör: 7:26 '{{1|" + _AK1 + "}}' (A1'de 'âdeme'); 7:27 '{{2|" + _AK2 + "}}' (A1'de 'âdeme', 'ş-şeytânu' — 'yeftinennekumu' faili, 'l-cenneti' ve 'ş-şeyâtîne' — 'ce'alne' mefulü)",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:26 nida — CERT 1 'qad' (3.), VOC 1 'yâ' (1.); 7:27 nida — EMPH 1 'yeftinennekumu' (4.; 'n'), NEG 3 'lâ' (3., 22. ve 29.), VOC 1 'yâ' (1.); "
 "morph REM ('ve libâsu' 7:26 10.), DIST ve ADDR ('zâlike' 7:26 12. ve 14.), ACC ('le'allehum' 7:26 18., 'innehû' 7:27 16., 'innâ' 7:27 24.), SUB ('kemâ' 7:27 6.), PRP ('li-yuriyehumâ' 7:27 14.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:26 ★★★ (kaynak hapaks, z=3,28); 7:27 ★ (kaynak n, z=1,87)",
 "fâsıla: 7:25 ن → 7:26 ن (" + _F[0] + ") → 7:27 ن (" + _F[1] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:26 xref yok; 7:27 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:27 'min haysu lâ' süzgeç GEÇMEZ; 7:26 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:26 konuşan 1P ('enzelnâ'), muhatap 2MP eki (''aleykum', 'sev'âtikum'), 3MS ('yuvârî' — gönderge 'libâsen' 6. kelime), 3MP ('yezzekkerûn' — tartışmalı, gönderge 'benî' 1. kelime; ek 'le'allehum' — tartışmalı, gönderge 'benî' 1. kelime), aktör adlı 'âdeme'; "
 "7:27 3MS ('yeftinennekumu' — fiil uyumu, fail 5. kelime; 'axrace', 'yenzi'u', 'yerâkum', 'huve' — gönderge 'ş-şeytânu' 5. kelime; 'li-yuriyehumâ' — edilgen, naib-i faili zamir; morph PASS etiketi, okuma etken, gönderge 'ş-şeytânu' 5. kelime; ekler 'innehû', 've qabîluhû' — gönderge 'ş-şeytânu' 5. kelime), "
 "muhatap 2MP ('teravnehum'; ekler 'yeftinennekumu', 'ebeveykum', 'yerâkum'), 3D eki (''anhumâ', 'libâsehumâ', 'li-yuriyehumâ', 'sev'âtihimâ' — gönderge 'ebeveykum' 8. kelime), 3MP ('yu'minûn' — gönderge 'lillezîne' 28. kelime; ek 'teravnehum' — gönderge 've qabîluhû' 19. kelime), konuşan 1P ('ce'alne'; ek 'innâ'), "
 "aktör adlı 'âdeme', 'ş-şeytânu', 'l-cenneti' ve 'ş-şeyâtîne'",
 "7:26-27 gönderge zinciri: 7:26 ve 7:27 nida ile muhatap 'benî âdeme' (1-2. kelime); 7:26 'le'allehum' (18. kelime) ve 'yezzekkerûn' (19. kelime) 3MP — muhataptan gıyaba geçiş, gönderge 'benî' 1. kelime tartışmalı (ölçüm iltifât 0); 7:26 konuşan 1P ile 7:27 konuşan 1P eş (7:26 17. kelimede lafız 3. şahısla anılır); "
 "7:27 3MS fiil ve ekler 'ş-şeytânu' (5. kelime); 3D ekleri 'ebeveykum' (8. kelime); 'teravnehum' (23. kelime) 3MP eki 'huve ve qabîluhû' (18-19. kelime) toplamına; 'yu'minûn' (30. kelime) 'lillezîne' (28. kelime) ilgi adına (okuma)",
 "edilgen: 7:27 'li-yuriyehumâ' (14. kelime) morph PASS etiketli — ölçüm EDİLGEN 1/8; okuma IV. bab etken (fail şeytan, naib-i fail yok); 7:26 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:26 ve 7:27 söz fiili yok, A3 '—'; nida 'yâ benî âdeme' (1-2. kelime) doğrudan hitap — A4'te 'nidâ' ile; "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 26 27 07' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:26 've rîşen' (9.) CONJ, 've libâsu' (10.) REM; 7:27 've qabîluhû' (19.) CONJ; 'fe' yok",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:26 ve 7:27 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 26 27 07'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 2 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:26 ve 7:27 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:26 لبس ×2; 7:27 رأي ×3, شطن ×2; ayetler arası kalıp 'yâ benî âdeme' (7:26, 7:27) — sayım 'say 7:26 1-2' ve lemma dizisi 'dizi 7 26 1 2' / 'dizi 7 27 1 2'; nida kalıbı, bağ kurulmadı (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "medde yazımıyla bulunan ek basılmış eşler ('say 7:26 16-17 --on --medde'): 2:61, 3:4, 6:33, 6:157, 40:63 — geniş kalıp, bağ kurulmadı; D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:26 bölüm açılışı, nidâ ('yâ benî âdeme' 1. kelime), şahıs geçişi 2 → 3, edim geçişi haber → nida; 7:27 nidâ ('yâ benî âdeme' 1. kelime), şahıs geçişi yok, edim geçişi yok; "
 "ölçüm iltifât 7:26-27 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:26 'libâsen yuvârî sev'âtikum' — nekre adı niteleyen fiil cümlesi (morph INDEF + IMPF); 7:26 've libâsu't-taqvâ zâlike xayrun' — yeni cümle başlangıcı ve işaret adıyla yinelenen özne (morph REM + DEM); 7:26 'le'allehum yezzekkerûn' — umma edatı ve haberi (morph ACC + IMPF); "
 "7:27 'lâ yeftinennekumu' — tekitli olumsuz muzâri, yasak anlamında (morph NEG + IMPF + EMPH); 7:27 'kemâ axrace' — benzetme edatı ve masdar 'mâ'sı (morph P + SUB + PERF); 7:27 'li-yuriyehumâ' — gerekçe lâmı (morph PRP + SUBJ); 7:27 'innehû yerâkum huve ve qabîluhû' — tekit, ayrı zamirle pekiştirme ve ona bağlanan ad (morph ACC + IMPF + PRON + CONJ)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:26 ve 7:27 'yâ benî âdeme' ile açılıyor (sayım: 'say 7:26 1-2', 'say 7:27 1-2'); 7:26 kök لبس ikilemesi; 7:27 kök رأي ve شطن ikilemeleri; "
 "7:26 'yuvârî' (7. kelime) ile 7:27 'li-yuriyehumâ' (14. kelime) gizleme / gösterme karşıtlığı kurar — ayetler arası, aday 1039 eşlemesine alınmadı; 7:26 9. kelime kökü ريش korpusta 1 (ölçüm HAPAKS)",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 07'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): bu blokta emsal yok; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:26 'enzelnâ' PERF ('qad' ile) — meal 'indirdik'; 'yuvârî' IMPF IND — meal 'gizleyen'; 'yezzekkerûn' IMPF IND ('le'alle' ile) — meal 'düşünürler'; "
 "7:27 'yeftinenne' IMPF IND ('lâ' ve 'n' ile) — meal 'düşürmesin'; 'axrace' PERF ('mâ' ile) — meal 'çıkardığı'; 'yenzi'u' IMPF IND — meal 'alıyordu'; 'yuriye' IMPF SUBJ PASS ('li' ile) — meal 'göstermek'; 'yerâ' IMPF IND — meal 'görür'; 'teravne' IMPF IND ('lâ' ile) — meal 'görmediğiniz'; 'ce'alne' PERF — meal 'kıldık'; 'yu'minûn' IMPF IND ('lâ' ile) — meal 'inanmayanlara'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'yuvârî' IMPF 7:26'da sıfat-fiil ('-en') ile; 'yeftinenne' IMPF IND 7:27'de 'lâ' ve 'n' ile olumsuz emir ('-mesin') ile; 'axrace' PERF 7:27'de 'mâ' ile sıfat-fiil ('-dığı') ile; 'yenzi'u' IMPF 7:27'de geçmişte süren hâl ('-ıyordu') ile; 'yuriye' IMPF SUBJ 7:27'de ad-fiil ('-mek') ile, morph PASS etiketi mealde etken; 'teravne' IMPF 7:27'de sıfat-fiil ('-diğiniz') ile; 'yu'minûn' IMPF 7:27'de sıfat-fiil ('-anlar') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): bölümün açılış bloğu — bölüm içinde önceki blok yok",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 26 27 07'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:26 ve 7:27 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:27 ('yerâkum' / 'lâ teravnehum'); 7:26 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök بني 7:26 ('benî') ve 7:27 ('benî'); kök أدم 7:26 ('âdeme') ve 7:27 ('âdeme'); kök لبس 7:26 ('libâsen', 've libâsu') ve 7:27 ('libâsehumâ'); kök سوأ 7:26 ('sev'âtikum') ve 7:27 ('sev'âtihimâ'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 3-1 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm açılışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b07/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 26 27 07'; lem_bozuk.py 07 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 26 27 → AYN_SONUC; sunum/bolum4_kurallar.py 26 27 07 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 26 27 07 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 38)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 7 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal yok — ölçüm xref alanı 7:26 ve 7:27 için boş; emsal dosyası üretilmedi; önceki basım (sunum/onceki_basim.py): " + ONC + "; say2.txt sayımı basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('bunayy' (morph LEM ham biçim), 'âdem', 'min', 'haysu', 'lâ'); joker '_' kullanılmadı; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (26, 27): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_26_27.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_7_b06k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '26', '27'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '26', '27', '07'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '26', '27', '07'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '26', '27', '07', '--tazelik-yok')}
    for _n in range(7, 38): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '26', '27', '07')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37 = [_R['B%d' % _n].splitlines() for _n in range(6, 38)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
