# sûre 7 blok 14 (7:48-51) ARIZA oluşturucu — bölüm 5-3
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b14/olcum.txt'
os.environ['SAY2'] = '/home/claude/b14/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Cennet ehli, ateş ehli ve A'râf'takiler'"


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
 ("7:48", "'a'râf ricâl 'arafe'", 2, 'say 7:48 3-5', "harekesiz 'l-a'râfi ricâlen ya'rifûnehum' (3-5. kelime)", ('dizi 7 48 3 5', "a'râf ricâl 'arafe", '3-5', "biçim farkı (dizi 7 48 3 5): 7:46 elif yazımı, zamir eki")),
 ("7:50", "'qâle inne allâh'", 2, 'say 7:50 15-17', "harekesiz 'qâlû inne'llâhe' (15-17. kelime)", ('dizi 7 50 15 17', "qâle inne allâh", '15-17', "biçim farkı (dizi 7 50 15 17): 7:28 fiil çekimi, zamir eki")),
 ("7:50", "'ashâb cenne en'", 2, 'say 7:50 4-6', "harekesiz 'ashâbe'l-cenneti en' (4-6. kelime)", ('dizi 7 50 4 6', "ashâb cenne en", '4-6', "biçim farkı (dizi 7 50 4 6): 7:46 yazım eş")),
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

VF_YAZI = {48: {1: "'ve nâdâ'", 12: "'ve mâ'"}, 49: {13: "'ve lâ'"}, 50: {1: "'ve nâdâ'"}, 51: {5: "'ve la'iben'", 6: "'ve ğarrathumu'", 9: "'fe'l-yevme'", 16: "'ve mâ'"}}
sys.path.insert(0, '/home/claude/b14/yap')
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
open('/home/claude/b14/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '14')
BLOKLAR = [str(i) for i in range(1, 15)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '14', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b14/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '48', '51', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b14/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b14/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '48', '51', '14').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_48_51.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:48', '7:49', '7:50', '7:51'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_48_51.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(48, 52))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:48 kök رجل ('ricâlen' 4. kelime — adam): tetik listesinde yok; 7:48 kök جمع ('cem'ukum' 11. kelime — topluluk): tetik listesinde yok; 7:51 kök دنو ('d-dunyâ' 8. kelime — dünya): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '48', '51', '14')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b14/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 15)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(48, 52))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l.replace('**', '') for l in open('/home/claude/b14/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b14/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 47), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK2 = _esc(re.search(r'aktör: adlı .*?rol meful\)', _OL[1]).group(0))
_AK3 = _esc(re.search(r'aktör: adlı .*?rol mecrur\)', _OL[2]).group(0))
for _k, _v in (('_AK2', _AK2), ('_AK3', _AK3)): _MB = _MB.replace('" + %s + "' % _k, _v)
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 432",
 "geriye dönük koşu (sûre 7 bölüm 4 kapanışı, komut 'python3 sunum/geriye_donuk.py b11k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 48 51 14'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:48, 7:49, 7:50 ve 7:51 esmâ yok; 7:49 lafız (6. kelime), 7:50 lafız (14. ve 17. kelime); 7:48 ve 7:51 lafız yok; 7:48, 7:49, 7:50 ve 7:51 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 48 51 14'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (48, 49, 50, 51)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 48 51 14'): KALAN_P",
 "ölçüm aktör: 7:49 '{{2|" + _AK2 + "}}' (A1'de 'l-cennete'); 7:50 '{{3|" + _AK3 + "}}' (A1'de 'l-cenneti'); 7:48 ölçüm adlı aktör yok; 7:51 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:48 haber — NEG 1 'mâ' (8.); 7:49 soru, emir — IMPV 1 'udxulu' (8.), INTG 1 'e-hâ'ulâ'i' (1.; 'e'), NEG 3 'lâ' (4.), 'lâ' (10.), 've lâ' (13.; 'lâ'); ölçüm biçim DIKKAT + QASEM (D2'de yazılmadı); "
 "7:50 emir — IMPV 1 'efîdû' (7.); 7:51 haber — kip yok; ölçüm biçim DIKKAT (D2'de yazılmadı); "
 "morph REL ('ve mâ' 7:48 12., 'llezîne' 7:49 2., 'mimmâ' 7:50 12., 'llezîne' 7:51 1., 've mâ' 7:51 16.), ATT ve DEM ('e-hâ'ulâ'i' 7:49 1., 'hâzâ' 7:51 15.), INT ('en' 7:50 6.), ACC ('inne' 7:50 16.), REM ve T ('fe'l-yevme' 7:51 9.), SUB ('kemâ' 7:51 11.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:48, 7:49, 7:50 ve 7:51 yıldız yok",
 "fâsıla: 7:47 ن → 7:48 ن (" + _F[0] + ") → 7:49 ن (" + _F[1] + ") → 7:50 ن (" + _F[2] + ") → 7:51 ن (" + _F[3] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:48 xref yok; 7:49 xref yok; 7:50 36:47 (emsal olarak basıldı), okunmuş 2 ayet; 7:51 41:28 (emsal olarak basıldı), okunmuş 3 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:48 'a'râf ricâl 'arafe' süzgeç GEÇMEZ; 7:50 'qâle inne allâh' süzgeç GEÇMEZ, 'ashâb cenne en' süzgeç GEÇMEZ; 7:49 ve 7:51 nakarat3 yok; sûre içi eşler 7:46 ve 7:28 (basılmış)",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:48 3MS ('ve nâdâ' — fiil uyumu, fail 2. kelime; 'ağnâ' — söz içi; fiil uyumu, fail 11. kelime), 3MP ('ya'rifûnehum', 'qâlû' — gönderge 'ashâbu' 2. kelime; ekler 'ya'rifûnehum', 'bi-sîmâhum' — gönderge 'ricâlen' 4. kelime), muhatap 2MP ('kuntum', 'testekbirûn' — söz içi; ekler ''ankum', 'cem'ukum' — söz içi); "
 "7:49 muhatap 2MP ('aqsamtum', 'udxulu', 'tahzenûn', 'entum' — söz içi; ek ''aleykum' — söz içi), 3MS ('yenâluhumu' — söz içi; fiil uyumu, fail 6. kelime), 3MP eki ('yenâluhumu' — söz içi; gönderge 'e-hâ'ulâ'i' 1. kelime), aktör adlı 'l-cennete'; "
 "7:50 3MS ('ve nâdâ' — fiil uyumu, fail 2. kelime; 'razaqakumu' — söz içi; fiil uyumu, fail 14. kelime; 'harramehumâ' — söz içi; gönderge 'llâhe' 17. kelime), muhatap 2MP ('efîdû' — söz içi; ek 'razaqakumu' — söz içi), konuşan 1P eki (''aleynâ' — söz içi), 3MP ('qâlû' — gönderge 'ashâbe' 4. kelime), 3D eki ('harramehumâ' — söz içi; tartışmalı; gönderge 'l-mâ'i' 10. kelime), aktör adlı 'l-cenneti'; "
 "7:51 3MP ('ttexazû', 'nesû', 'kânû', 'yechadûn' — gönderge 7:50 20. kelime; ekler 'dînehum', 've ğarrathumu', 'nensâhum', 'yevmihim' — gönderge 7:50 20. kelime), 3FS ('ve ğarrathumu' — fiil uyumu, fail 7. kelime), konuşan 1P ('nensâhum'; ek 'bi-âyâtinâ')",
 "7:48-51 gönderge zinciri: 7:48 'ashâbu'l-a'râfi' (2-3. kelime) seslenen, 'ricâlen' (4. kelime) seslenilen; söz içi muhatap 2MP 'ricâlen'; 7:49 söz sürüyor — 'e-hâ'ulâ'i' (1. kelime) bahçe halkı; 'udxulu' (8. kelime) ve sonrası muhatabı bahçe halkı — muhatap değişimi, tartışmalı (söz sahibi A'râf halkı ya da Allah okunabilir); 7:49 muhatap 2MP 'aqsamtum' (3. kelime) ise 7:48 4. kelimedeki adamlar; "
 "7:50 'ashâbu'n-nâri' (2-3. kelime) seslenen, 'ashâbe'l-cenneti' (4-5. kelime) seslenilen; 'qâlû' (15. kelime) bahçe halkı; 'harramehumâ' 3D eki 'l-mâ'i' (10. kelime) ve 'mimmâ' (12. kelime) — tartışmalı; 7:51 3MP fiil ve ekler 7:50 'l-kâfirîn' (20. kelime) sıfatı; 7:51 konuşan 1P ('nensâhum' 10. kelime, 'bi-âyâtinâ' 18. kelime) söz fiilsiz anlatıda (okuma)",
 "edilgen: 7:48, 7:49, 7:50 ve 7:51 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:48 'qâlû' (7.) ardından söz 8-14. kelime — ayet sonunda kapanmıyor, 7:49 boyunca sürüyor; 7:49 15. kelimede kapanış (söz sahibi tartışmalı) (okuma); "
 "7:50 've nâdâ' (1.) ve 'en' (6.) ardından söz biçimli içerik 7-14. kelime (seslenme fiili, قول kökü değil); 'qâlû' (15.) ardından söz biçimli içerik 16-20. kelime (A3'te seslenme içeriğiyle birlikte biçimli kayıt); 7:51 söz fiili yok, A3 '—'; mealde 'dediler ki:', 'seslendi ki:' ve 'Dediler ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 48 51 14' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:48 've nâdâ' (1.) CONJ, 've mâ' (12.) CONJ; 7:49 've lâ' (13.) CONJ; 7:50 've nâdâ' (1.) CONJ; 7:51 've la'iben' (5.) CONJ, 've ğarrathumu' (6.) CONJ, 've mâ' (16.) CONJ; "
 "'fe' konumu: 7:51 'fe'l-yevme' (9.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:50 ◈K موه ('l-mâ'i' 10. kelime — K1); 7:51 ◈K يوم ('l-yevme' 9. kelime, 'yevmihim' 14. kelime — K2), 7:51 ◈B حيي ('l-hayâtu' 7. kelime — B4); 7:48 ve 7:49 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 48 51 14'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:50 (36:47), 7:51 (41:28); 7:48 ve 7:49 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:48 عرف ×2; 7:50 أله ×2, صحب ×2; 7:51 نسي ×2, يوم ×2; "
 "ayetler arası kalıp 've nâdâ ashâbu' (7:48, 7:50) — sayım 'say 7:48 1-2' / 'say 7:50 1-2' ve lemma dizisi 'dizi 7 48 1 2' / 'dizi 7 50 1 2'; seslenme kalıbı, bağ kurulmadı (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: bloğun emsal dosyasında olmayan basılmış eş (önceki bloklarda basılmış ya da sûre içi), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:48 söz açılır (8. kelime), şahıs geçişi yok, edim geçişi yasak → haber; 7:49 söz kapanır (15. kelime), şahıs geçişi 3 → 2, edim geçişi haber → soru, emir; 7:50 şahıs geçişi 2 → 3, edim geçişi soru, emir → emir; 7:51 şahıs geçişi yok, edim geçişi emir → haber, bölüm kapanışı; ölçüm iltifât 7:48-51 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:48 'mâ ağnâ 'ankum cem'ukum' — olumsuz mâzî, fail sonda (morph NEG + PERF + P + NOM); 7:48 've mâ kuntum testekbirûn' — masdar okunan ilgi adı (morph CONJ + REL + PERF + IMPF); 7:49 'e-hâ'ulâ'i'llezîne aqsamtum' — soru edatlı işaret adı ve ilgi cümlesi (morph INTG + ATT + DEM + REL + PERF); "
 "7:49 'lâ xavfun 'aleykum' — olumsuz isim cümlesi (morph NEG + INDEF); 7:50 'en efîdû' — açıklama edatı ve emir (morph INT + IMPV); 7:51 'llezîne'ttexazû' — 7:50 'l-kâfirîn' sıfatı ilgi cümlesi (morph REL + PERF); 7:51 'kemâ nesû' — benzetme edatı ve masdar edatı (morph P + SUB + PERF)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:50 12-14. kelime — 36:47 ile harekesiz eş (sayım: 'say 7:50 12-14'); 7:51 17-19. kelime — 41:28 ile harekesiz eş (sayım: 'say 7:51 17-19'); "
 "7:51 2-3. kelime — 6:70 ile harekesiz eş (sayım: 'say 7:51 2-3'); 7:48 kök عرف ikilemesi; 7:50 kök أله ve صحب ikilemeleri; 7:51 kök نسي ve يوم ikilemeleri",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 14'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'mimmâ razaqakumu'llâhu' 7:50 'Allah'ın size rızık olarak verdiklerinden' / 36:47 'Allah'ın size verdiği rızıktan' (emsal metninde) — çakışma — tam okuma sonu ('rızık olarak ver-' / 'ver-' ve 'rızık'); 'razaqakumu'llâhu' 7:50 'Allah'ın size rızık olarak verdikleri' / 36:47 'Allah'ın size verdiği rızık' (emsal metninde) — çakışma — tam okuma sonu ('rızık olarak ver-' / 'ver-' ve 'rızık'); "
 "'kânû bi-âyâtinâ yechadûn' 7:51 'âyetlerimizi bile bile inkâr etmekte oldukları' / 41:28 'ayetlerimizi bile bile inkâr edegelmelerine' (emsal metninde) — çakışma — tam okuma sonu ('-mekte oldukları' / '-egelmelerine'); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:48 'nâdâ' PERF — meal 'seslendi'; 'ya'rifûne' IMPF IND — meal 'tanıdıkları'; 'qâlû' PERF — meal 'dediler'; 'ağnâ' PERF ('mâ' ile) — meal 'vermedi'; 'kuntum' PERF — meal 'olduklarınız'; 'testekbirûn' IMPF IND — meal 'büyüklenmekte'; "
 "7:49 'aqsamtum' PERF — meal 'ettikleriniz'; 'yenâlu' IMPF IND ('lâ' ile) — meal 'erişmez'; 'udxulu' IMPV — meal 'girin'; 'tahzenûn' IMPF IND ('lâ' ile) — meal 'üzülmezsiniz'; "
 "7:50 'nâdâ' PERF — meal 'seslendi'; 'efîdû' IMPV — meal 'akıtın'; 'razaqa' PERF — meal 'verdiklerinden'; 'qâlû' PERF — meal 'Dediler'; 'harrame' PERF — meal 'kıldı'; "
 "7:51 'ttexazû' PERF — meal 'edinen'; 'ğarrat' PERF — meal 'aldattığı'; 'nensâ' IMPF IND — meal 'unuturuz'; 'nesû' PERF ('kemâ' ile) — meal 'unuttukları'; 'kânû' PERF — meal 'oldukları'; 'yechadûn' IMPF IND — meal 'etmekte'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle; IMPF IND geniş zaman karşılığı her blokta sapma sayılır — sûre 7 bölüm 3 denetimi kuralı 3): 'ya'rifûne' IMPF 7:48'de geçmiş sıfat-fiil ('-dık') ile; 'kuntum' PERF 7:48'de sıfat-fiil ('-duklarınız') ile; 'yenâlu' IMPF 7:49'da geniş zaman ('-mez') ile; 'tahzenûn' IMPF 7:49'da geniş zaman ('-mezsiniz') ile; "
 "'razaqa' PERF 7:50'de sıfat-fiil ('-dik') ile; 'ttexazû' PERF 7:51'de sıfat-fiil ('-en') ile; 'ğarrat' PERF 7:51'de sıfat-fiil ('-tığı') ile; 'nensâ' IMPF 7:51'de geniş zaman ('-uruz') ile; 'nesû' PERF 7:51'de sıfat-fiil ('-tukları') ile; 'kânû' PERF 7:51'de sıfat-fiil ('-dukları') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): ''an' (yönelme eki / ayrılma eki) — çakışma değil (fiil yönetimi: 'fayda ver-' yönelme); 'bi' ('-le' / 'dolayı' / 'ile' / ayrılma eki / belirtme eki) — çakışma değil (araç, sebep, beraberlik, fiil yönetimi); 'ellezî' (REL: '-en' / '-tikleriniz' / '-an' / '-enler') — çakışma değil (şahıs ve sayı uyumu); 'fe' (REM: 'Artık' / 'Bunun üzerine' / karşılıksız) — çakışma değil (geçiş, sonuç, soru edatı öncesi); 'hum' ('onlara' / 'onları' / 'onlar' / iyelik eki / karşılıksız) — çakışma değil (çekim ve tamlama); 'humâ' ('bunlar' / iyelik eki) — çakışma değil (nesne zamiri, tamlama); 'kum' ('siz' / 'size' / iyelik eki) — çakışma değil (çekim ve tamlama); 'lâ' (NEG: 'yok' / olumsuzluk eki) — çakışma değil (isim cümlesinde yokluk, fiilde olumsuzluk); 'min' ('-dan' / '-den' / karşılıksız) — çakışma değil (ünlü uyumu; beyân); 'mâ' (NEG: olumsuzluk eki / 'değil') — çakışma değil (fiilde olumsuzluk, ek fiilde 'değil'); 'mâ' (REL: '-dikler' / '-dukları' / '-duklarınız' / '-ki' / '-tiğini') — çakışma değil (sıfat-fiil şahıs ve uyum); 'nâ' ('biz' / 'bize' / 'bizi' / iyelik eki) — çakışma değil (çekim ve tamlama); 'ulâ'i' (DEM: 'bunlar' / 'işte onlar') — çakışma değil (tenbih edatlı yakın işaret, hitap ekli uzak işaret)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 48 51 14'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:48, 7:49, 7:50 ve 7:51 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:48, 7:49, 7:50 ve 7:51 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök صحب 7:48 ('ashâbu') ve 7:50 ('ashâbu', 'ashâbe'), 7:42 ('ashâbu'), 7:44 ('ashâbu', 'ashâbe'), 7:46 ('ashâbe') ve 7:47 ('ashâbi') ile bölüm içi; kök جنن 7:49 ('l-cennete') ve 7:50 ('l-cenneti'), 7:42 ('l-cenneti'), 7:43 ('l-cennetu'), 7:44 ('l-cenneti') ve 7:46 ('l-cenneti') ile bölüm içi; kök قول 7:48 ('qâlû') ve 7:50 ('qâlû'), 7:43 ('ve qâlu'), 7:44 ('qâlû') ve 7:47 ('qâlû') ile bölüm içi; kök أله 7:49 ('llâhu') ve 7:50 ('llâhu', 'llâhe'), 7:43 ('li'llâhi', 'llâhu'), 7:44 ('llâhi') ve 7:45 ('llâhi') ile bölüm içi; kök كون 7:48 ('kuntum') ve 7:51 ('kânû'), 7:43 ('kunnâ', 'kuntum') ile bölüm içi; kök ندي 7:48 ('ve nâdâ') ve 7:50 ('ve nâdâ'), 7:43 ('ve nûdû'), 7:44 ('ve nâdâ') ve 7:46 ('ve nâdev') ile bölüm içi; kök نور 7:50 ('n-nâri'), 7:44 ('n-nâri') ve 7:47 ('n-nâri') ile bölüm içi; kök كفر 7:50 ('l-kâfirîn'), 7:45 ('kâfirûn') ile bölüm içi; kök عرف 7:48 ('l-a'râfi', 'ya'rifûnehum'), 7:46 ('l-a'râfi', 'ya'rifûne') ile bölüm içi; kök رجل 7:48 ('ricâlen'), 7:46 ('ricâlun') ile bölüm içi; kök سوم 7:48 ('bi-sîmâhum'), 7:46 ('bi-sîmâhum') ile bölüm içi; kök دخل 7:49 ('udxulu'), 7:46 ('yedxulûhâ') ile bölüm içi; kök لقي 7:51 ('liqâ'e'), 7:47 ('tilqâ'e') ile bölüm içi; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 5-3 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 12, 13 ve 14; bölüm kapanışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b14/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 48 51 14'; lem_bozuk.py 14 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 48 51 → AYN_SONUC; sunum/bolum4_kurallar.py 48 51 14 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 48 51 14 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 40)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 14 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('nâdâ', 'ashâb', 'a'râf', 'ricâl', ''arafe', 'cenne', 'en', 'qâle', 'inne', 'allâh', 'kâne', 'âye', 'cehadu' (morph LEM ham biçim)); joker '_' bu blokta yok; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (48, 51): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_48_51.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_7_b11k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '48', '51'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '48', '51', '14'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '48', '51', '14'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '48', '51', '14', '--tazelik-yok')}
    for _n in range(7, 40): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '48', '51', '14')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39 = [_R['B%d' % _n].splitlines() for _n in range(6, 40)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'B39_HEPSI': (B39[-1] if B39 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
