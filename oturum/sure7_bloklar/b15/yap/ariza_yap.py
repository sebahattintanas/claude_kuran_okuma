# sûre 7 blok 15 (7:52-53) ARIZA oluşturucu — bölüm 5-4
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b15/olcum.txt'
os.environ['SAY2'] = '/home/claude/b15/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = list(ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_7_b14.txt', encoding='utf-8').read() + ']'))
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
 ("7:52", "'hudâ rahme qavm âmene'", 2, 'say 7:52 8-10', "harekesiz 'rahmeten li-qavmin yu'minûn' (8-10. kelime)", ('dizi 7 52 7 10', "hudâ rahme qavm âmene", '7-10', "biçim farkı (dizi 7 52 7 10): basılmamış eş i'râb, önek")),
 ("7:53", "'câ'e rasûl rabb haqq'", 2, 'say 7:53 14-17', "harekesiz 'câ'et rusulu rabbinâ bi'l-haqqi' (14-17. kelime)", ('dizi 7 53 14 17', "câ'e rasûl rabb haqq", '14-17', "biçim farkı (dizi 7 53 14 17): 7:43 yazım eş")),
 ("7:53", "'rabb haqq hel'", 2, 'say 7:53 16-18', "harekesiz 'rabbinâ bi'l-haqqi fe-hel' (16-18. kelime)", ('dizi 7 53 16 18', "rabb haqq hel", '16-18', "biçim farkı (dizi 7 53 16 18): 7:44 i'râb, önek")),
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

VF_YAZI = {52: {1: "'ve le-qad'", 8: "'ve rahmeten'"}, 53: {18: "'fe-hel'", 22: "'fe-yeşfe'û'", 26: "'fe-na'mele'", 34: "'ve dalle'"}}
sys.path.insert(0, '/home/claude/b15/yap')
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
open('/home/claude/b15/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '15')
BLOKLAR = [str(i) for i in range(1, 16)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '15', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b15/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '52', '53', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b15/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b15/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '52', '53', '15').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_52_53.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:52', '7:53'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_52_53.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(52, 54))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:53 kök قبل ('qablu' 12. kelime — önce): tetik listesinde yok; 7:53 kök نفس ('enfusehum' 33. kelime — kendi): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '52', '53', '15')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b15/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 16)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(52, 54))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l.replace('**', '') for l in open('/home/claude/b15/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b15/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 51), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta sunum/yasakli.sh IZIN'e ('ariza_7_52_53.txt', 'ilk, evvel') çifti — bölüm 10 denetimi kuralı 10: kök anlamı araç çıktısı aynen (sûre 6 blok emsali); blok 14 sonrası ara denetimde sunum/bolum40_kurallar.py (kural 1-5) eklendi, sunum/geriye_donuk.py ve mutasyon_sina buna göre güncellendi — önceki commit'te, mutasyon sınaması 425 / 425; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 436",
 "geriye dönük koşu (sûre 7 bölüm 5 ara denetimi, komut 'python3 sunum/geriye_donuk.py b14k'): GERI_P",
 "bölüm sınırı düzeltmesi: blok_plani_7.txt'e göre bölüm 5 blokları 12, 13, 14 ve 15; blok 14 kaydında 7:51 A4 'bölüm kapanışı' ve bölüm maddesi 'bölüm kapanışı bu blokta' yanlış yazıldı, bağımsız denetim (bekleyen_ariza_7_b14) bölüm kapanmadan, ara denetim olarak koştu; blok 14 kaydı geriye dönük yeniden yazılmadı — tam okuma sonu; bölüm 5 kapanışı ve kapanış denetimi bu blokta",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 52 53 15'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:52 ve 7:53 esmâ yok; 7:52 ve 7:53 lafız yok; 7:53 Rab (16. kelime); 7:52 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 52 53 15'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (52, 53)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 52 53 15'): KALAN_P",
 "ölçüm aktör: 7:52 ve 7:53 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:52 haber — CERT 1 've le-qad' (1.; 'qad'), EMPH 1 've le-qad' (1.; 'le'); 7:53 soru — CERT 2 'qad' (13.), 'qad' (31.), INTG 2 'hel' (1.), 'fe-hel' (18.; 'hel'), RES 1 'illâ' (3.); ölçüm biçim HASR (D2'de yazılmadı); "
 "morph REM ('ve le-qad' 7:52 1., 'fe-hel' 7:53 18.), REL ('llezîne' 7:53 9., 'llezî' 7:53 28., 'mâ' 7:53 36.), CAUS ('fe-yeşfe'û' 7:53 22., 'fe-na'mele' 7:53 26.), T ('yevme' 7:53 5.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:53 ★★ (kaynak n, z=2,72); 7:52 yıldız yok",
 "fâsıla: 7:51 ن → 7:52 ن (" + _F[0] + ") → 7:53 ن (" + _F[1] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:52 16:64 (emsal olarak basıldı), 12:111 (basılmış), okunmamış 1 ayet (sûre içi 1); 7:53 6:24 (basılmış), 11:21 (basılmış), 35:37 (emsal olarak basıldı), okunmuş 1 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:52 'hudâ rahme qavm âmene' süzgeç GEÇER; 7:53 'câ'e rasûl rabb haqq' süzgeç GEÇER, 'rabb haqq hel' süzgeç GEÇMEZ; sûre içi eşler 7:43 ve 7:44 (basılmış), 7:52 kalıbının sûre içi eşi basılmamış",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:52 konuşan 1P ('ci'nâhum', 'fassalnâhu'), 3MP ('yu'minûn' — gönderge 'li-qavmin' 9. kelime; ek 'ci'nâhum' — gönderge 7:51 1. kelime), 3MS eki ('fassalnâhu' — gönderge 'bi-kitâbin' 3. kelime); "
 "7:53 3MP ('yenzurûne' — gönderge 7:52 2. kelime; 'nesûhu', 'xasirû', 'kânû', 'yefterûn' — gönderge 'llezîne' 9. kelime; 'fe-yeşfe'û' — söz içi; gönderge 'şufe'â'e' 21. kelime; ekler 'enfusehum', ''anhum' — gönderge 'llezîne' 9. kelime), 3MS ('ye'tî' — fiil uyumu, fail 7. kelime; 'yeqûlu' — fiil uyumu, fail 9. kelime; 've dalle' — gönderge 'mâ' 36. kelime; ekler 'te'vîlehu', 'te'vîluhu', 'nesûhu' — gönderge 7:52 3. kelime), "
 "3FS ('câ'et' — söz içi; fiil uyumu, fail 15. kelime), konuşan 1P ('nuraddu' — söz içi; edilgen, naib-i faili zamir; 'fe-na'mele', 'kunnâ', 'na'mel' — söz içi; ekler 'rabbinâ', 'lenâ', 'lenâ', 'kunnâ' — söz içi)",
 "7:52-53 gönderge zinciri: 7:52 konuşan 1P ('ci'nâhum' 2. kelime, 'fassalnâhu' 4. kelime) 7:51 konuşan 1P ('nensâhum') ile eş; 7:52 'ci'nâhum' 3MP eki 7:51 1. kelimedeki ilgi adı; 'fassalnâhu' 3MS eki 'bi-kitâbin' (3. kelime); 7:53 'yenzurûne' (2. kelime) 7:52 'ci'nâhum' göndergesiyle eş; 7:53 'te'vîlehu', 'te'vîluhu', 'nesûhu' 3MS ekleri 7:52 'bi-kitâbin' (3. kelime); "
 "7:53 söz içi konuşan 1P ('rabbinâ' 16. kelime ve sonrası) 'llezîne' (9. kelime) özneleri; 'fe-yeşfe'û' (22. kelime) 'şufe'â'e' (21. kelime) (okuma)",
 "edilgen: 7:53 'nuraddu' (25. kelime; naib-i faili zamir) — ölçüm EDİLGEN 1/14; 7:52 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:53 'yeqûlu' (8.) ardından söz 13-30. kelime (REM sapması 7:53 (18. kelime) — 'fe-hel' söz içinde yeni cümle başı, konuşan 1P sürer) — ayet içi kapanış, 'qad' (31.) anlatıya dönüş (okuma); "
 "7:52 söz fiili yok, A3 '—'; mealde 'derler ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 52 53 15' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:52 've le-qad' (1.) REM, 've rahmeten' (8.) CONJ; 7:53 've dalle' (34.) CONJ; 'fe' konumları: 7:53 'fe-hel' (18.) REM, 'fe-yeşfe'û' (22.) CAUS, 'fe-na'mele' (26.) CAUS",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:53 ◈K يوم ('yevme' 5. kelime — K2); 7:52 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 52 53 15'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 2 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:52 (16:64), 7:53 (35:37); D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:53 أول ×2, شفع ×2, عمل ×2, كون ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: bloğun emsal dosyasında olmayan basılmış eş (önceki bloklarda basılmış ya da sûre içi), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:52 şahıs sayısında beraberlik (1P 4 · 3. şahıs 4 — ölçüm baskın 1), şahıs geçişi 3 → 1, edim geçişi yok; 7:53 söz açılır (13. kelime), söz kapanır (30. kelime, ayet içi), soru → cevap (22. ve 26. kelime, CAUS), şahıs geçişi 1 → 3, edim geçişi haber → soru, bölüm kapanışı; ölçüm iltifât 7:52-53 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:52 've le-qad ci'nâhum bi-kitâbin' — yemin lâmı, tekitli mâzî ve 'bi' ile getirme (morph REM + EMPH + CERT + PERF + P); 7:52 'huden ve rahmeten' — mansub ad, durum bildirir (morph ACC); 7:53 'hel yenzurûne illâ te'vîlehu' — soru edatı ve hasr (morph INTG + IMPF + RES); "
 "7:53 'yevme ye'tî te'vîluhu' — cümleye izafet edilmiş zaman zarfı (morph T + IMPF); 7:53 'fe-yeşfe'û' ve 'fe-na'mele' — sebep edatıyla mansub muzâri (morph CAUS + SUBJ); 7:53 'ev nuraddu' — atıflı edilgen muzâri (morph CONJ + IMPF + PASS)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:52 8-10. kelime — 16:64 ve 12:111 ile harekesiz eş (sayım: 'say 7:52 8-10'); 7:53 14-17. kelime — 7:43 ile harekesiz eş (sayım: 'say 7:53 14-17'); "
 "7:53 27-30. kelime — 35:37 ile harekesiz eş (sayım: 'say 7:53 27-30'); 7:53 33-38. kelime — 6:24 ve 11:21 ile harekesiz eş (sayım: 'say 7:53 33-38'); 7:53 kök أول, شفع, عمل ve كون ikilemeleri",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 15'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'rahmeten li-qavmin yu'minûn' 7:52 'iman eden bir kavim için yol gösterici ve rahmet' / 16:64 'iman eden bir topluluk için yol gösterici ve rahmet' (emsal metninde) — çakışma — tam okuma sonu ('kavim' / 'topluluk'); "
 "'ğayra'llezî kunnâ na'mel' 7:53 'işlemekte olduğumuzdan başkasını' / 35:37 'yaptığımızdan başka salih amel işleyelim' (emsal metninde) — çakışma — tam okuma sonu ('işle-' / 'yap-'; '-mekte olduğumuz' / '-tığımız'); 'llezî kunnâ na'mel' 7:53 'işlemekte olduğumuz' / 35:37 'yaptığımızdan başka salih amel işleyelim' (emsal metninde) — çakışma — tam okuma sonu ('işle-' / 'yap-'); "
 "basılmış sûre içi eş 7:43 ('say 7:53 14-17') kesimi 'Rabbimizin elçileri hak ile geldi' — 7:43 kesimiyle bayt eşit; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:52 'ci'nâ' PERF ('le-qad' ile) — meal 'getirdik'; 'fassalnâ' PERF — meal 'açıkladığımız'; 'yu'minûn' IMPF IND — meal 'eden'; "
 "7:53 'yenzurûne' IMPF IND ('hel' ile) — meal 'bekliyorlar'; 'ye'tî' IMPF IND — meal 'geleceği'; 'yeqûlu' IMPF IND — meal 'derler'; 'nesû' PERF — meal 'unutmuş'; 'câ'et' PERF ('qad' ile) — meal 'geldi'; 'yeşfe'û' IMPF SUBJ ('fe' ile) — meal 'etsinler'; 'nuraddu' IMPF IND edilgen ('ev' ile) — meal 'döndürülsek'; "
 "'na'mele' IMPF SUBJ ('fe' ile) — meal 'işleyelim'; 'kunnâ' PERF — meal 'olduğumuzdan'; 'na'mel' IMPF IND — meal 'işlemekte'; 'xasirû' PERF ('qad' ile) — meal 'uğrattılar'; 'dalle' PERF — meal 'gitti'; 'kânû' PERF — meal 'oldukları'; 'yefterûn' IMPF IND — meal 'uydurmakta'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle; IMPF IND geniş zaman karşılığı her blokta sapma sayılır — sûre 7 bölüm 3 denetimi kuralı 3): 'fassalnâ' PERF 7:52'de sıfat-fiil ('-dığımız') ile; 'yu'minûn' IMPF 7:52'de sıfat-fiil ('-en') ile; 'ye'tî' IMPF 7:53'te gelecek sıfat-fiili ('-eceği') ile; 'yeqûlu' IMPF 7:53'te geniş zaman ('-rler') ile; "
 "'nesû' PERF 7:53'te sıfat-fiil ('-muş olanlar') ile; 'nuraddu' IMPF 7:53'te şart ('-sek') ile; 'kunnâ' PERF ve 'na'mel' IMPF 7:53'te sıfat-fiil ('-mekte olduğumuz') ile; 'kânû' PERF ve 'yefterûn' IMPF 7:53'te sıfat-fiil ('-makta oldukları') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'bi' ('ile' / karşılıksız) — çakışma değil (beraberlik, 'getir-' açılımı); 'fe' (REM: 'Şimdi' / 'Artık' / 'Bunun üzerine' / karşılıksız) — çakışma değil (geçiş); 'fe' (CAUS: 'ki') — çakışma değil (sebep cümlesi); 'hu' ('onun' / 'Onun' / 'onu' / karşılıksız) — çakışma değil (tamlama, belirtme, nitelenen adla karşılama); 'li' ('için' / tamlayan eki / yönelme eki) — çakışma değil (amaç, sahiplik, yön); 'min' (karşılıksız / '-dan' / '-den') — çakışma değil (pekiştirme, 'daha önce' kalıbı); 'nâ' ('biz' / iyelik eki) — çakışma değil (çekim ve tamlama); 'ellezî' (REL: '-anlar' / '-duğumuz') — çakışma değil (şahıs ve sayı uyumu); 'hel' (INTG: 'mı' / 'mu') — çakışma değil (ünlü uyumu); 'illâ' (RES: 'başkasını') — çakışma değil (hasr); 'mâ' (REL: 'şeyler') — çakışma değil (ilgi adı adla karşılandı); ''alâ' ('üzere') — çakışma değil (dayanak bildiren edat); 'hum' ('kendileri' / 'onlara' / iyelik eki) — çakışma değil (dönüşlü kullanım, çekim, tamlama)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 52 53 15'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:52 ve 7:53 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:52 ve 7:53 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök جيأ 7:52 ('ci'nâhum') ve 7:53 ('câ'et'), 7:43 ('câ'et') ile bölüm içi; kök أمن 7:52 ('yu'minûn'), 7:42 ('âmenû') ile bölüm içi; kök هدي 7:52 ('huden'), 7:43 ('hedânâ', 'li-nehtediye', 'hedâna') ile bölüm içi; kök قوم 7:52 ('li-qavmin'), 7:47 ('l-qavmi') ile bölüm içi; kök رحم 7:52 ('rahmeten'), 7:49 ('bi-rahmetin') ile bölüm içi; "
 "kök عمل 7:53 ('fe-na'mele', 'na'mel'), 7:42 (''amilu') ve 7:43 ('ta'melûn') ile bölüm içi; kök نفس 7:53 ('enfusehum'), 7:42 ('nefsen') ile bölüm içi; kök قول 7:53 ('yeqûlu'), 7:43 ('ve qâlu'), 7:44 ('qâlû'), 7:47 ('qâlû'), 7:48 ('qâlû') ve 7:50 ('qâlû') ile bölüm içi; kök كون 7:53 ('kunnâ', 'kânû'), 7:43 ('kunnâ', 'kuntum'), 7:48 ('kuntum') ve 7:51 ('kânû') ile bölüm içi; "
 "kök رسل 7:53 ('rusulu'), 7:43 ('rusulu') ile bölüm içi; kök ربب 7:53 ('rabbinâ'), 7:43 ('rabbinâ'), 7:44 ('rabbunâ', 'rabbukum') ve 7:47 ('rabbenâ') ile bölüm içi; kök حقق 7:53 ('bi'l-haqqi'), 7:43 ('bi'l-haqqi') ve 7:44 ('haqqan', 'haqqan') ile bölüm içi; kök يوم 7:53 ('yevme'), 7:51 ('l-yevme', 'yevmihim') ile bölüm içi; kök نسي 7:53 ('nesûhu'), 7:51 ('nensâhum', 'nesû') ile bölüm içi; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 5-4 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 12, 13, 14 ve 15; bölüm kapanışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b15/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 52 53 15'; lem_bozuk.py 15 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 52 53 → AYN_SONUC; sunum/bolum4_kurallar.py 52 53 15 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 52 53 15 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 41)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 15 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('hudâ', 'rahme', 'qavm', 'âmene', 'câ'e', 'rasûl', 'rabb', 'haqq', 'hel', 'ğayr', 'ellezî', 'kâne', ''amile'); joker '_' bu blokta yok; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (52, 53): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_52_53.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_7_b14k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '52', '53'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '52', '53', '15'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '52', '53', '15'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '52', '53', '15', '--tazelik-yok')}
    for _n in range(7, 41): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '52', '53', '15')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39, B40 = [_R['B%d' % _n].splitlines() for _n in range(6, 41)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'B39_HEPSI': (B39[-1] if B39 else '?'), 'B40_HEPSI': (B40[-1] if B40 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38, B39, B40): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
