# sûre 6 blok 9 (6:37-41) ARIZA oluşturucu — bölüm 4-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b09/olcum.txt'
os.environ['SAY2'] = '/home/claude/b09/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Elçiye teselli; darlıkta çağrılan'"


def sd(key):
    return sayim.S2[key][1]


def sic(key):
    n, d = sayim.S2[key]
    return 1 + len([x for x in d['basilan'] if x.startswith('6:')]) + d['okunmus_si'] + d['henuz_si']


def taban(key, ay):
    n, d = sayim.S2[key]
    p = [ay] + [x for x in d['basilan'] if x.startswith('6:') and x != ay]
    if d['okunmus_si']: p.append('okunmus_si %d' % d['okunmus_si'])
    if d['henuz_si']: p.append('henuz_si %d' % d['henuz_si'])
    return ' + '.join(p)


R5 = [
 ("6:37", "'qâdir 'alâ en'", 2, 'say 6:37 11-13 --on', "önek kesilmiş 'qâdirun 'alâ en' (11-13. kelime)", None),
 ("6:38", "'summe ilâ rabb'", 3, 'say 6:38 19-21', "harekesiz 'summe ilâ rabbihim' (19-21. kelime)", ('dizi 6 38 19 21', "summe ilâ rabb", '19-21', "biçim farkı (dizi 6 38 19 21): basılmamış eş yazım eş; basılmamış eş zamir eki")),
 ("6:40", "'qâle ra'â in etâ 'azâb allâh'", 2, 'say 6:40 1-6', "harekesiz 'qul era'eytekum in etâkum 'azâbu'llâh' (1-6. kelime)", None),
 ("6:40", "'qâle ra'â in'", 3, 'say 6:40 1-3', "harekesiz 'qul era'eytekum in' (1-3. kelime)", ('dizi 6 40 1 3', "qâle ra'â in", '1-3', "biçim farkı (dizi 6 40 1 3): basılmamış eş fiil çekimi, zamir eki; basılmamış eş yazım eş")),
 ("6:40", "'in kâne sâdiq'", 2, 'say 6:40 13-15', "harekesiz 'in kuntum sâdiqîn' (13-15. kelime)", None),
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

K1 = {k: None for k, (n, d) in sayim.S2.items() if n == 1 and '--medde' not in k}

VF_YAZI = {37: {1: "'ve qâlû'", 16: "'ve lâkinne'"}, 38: {1: "'ve mâ'", 6: "'ve lâ'"}, 39: {1: "'ve'llezîne'", 5: "'ve bukmun'", 12: "'ve men'"}, 40: {}, 41: {4: "'fe-yekşifu'", 10: "'ve tensevne'"}}
sys.path.insert(0, '/home/claude/b09/yap')
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
open('/home/claude/b09/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '09')
BLOKLAR = [str(i) for i in range(1, 10)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '9', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b09/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '37', '41', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b09/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b09/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '37', '41', '09').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_37_41.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:37', '6:38', '6:39', '6:40', '6:41'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_37_41.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(37, 42))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '37', '41', '09')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b09/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 10)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(37, 42))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/bolum8_kurallar.py kural 5 — yazım eşdeğeri iskeletinde 'ilâ' (إِلَى) ve 'illâ' (إِلّا), 'etâ' (أَتَى) ve 'âtâ' (آتَى), 'qâdir' (قادِر) ve 'qadîr' (قَدِير) ayrı lemma, eş iskelet uyarısından çıkarıldı (sûre 6 blok 9); sunum/edat_etiket.py bölüm 15 denetimi kuralı 15 — EDLEM 'iyyâ' (إِيّا) eklendi, es_edat tanınmayan (sûre 6 blok 9); mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 152",
 "kök tablosu: ölçümde '???' 6:37-41 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 37 41 09'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: blokta esmâ yok (ölçüm 6:37-41); esma_el kaydı yok; "
 "lafız 6:37, 6:39 ve 6:40; Rab 6:37 ve 6:38 (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 37 41 09'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:37 '{{1|fâsıla يعلمون → ن, N sınıfı}}', '{{1|simetri \\[3, 1, 8, 1\\]}}', '{{1|harf 74 → harf3 69, isaret 5}}', '{{1|dış düğüm 1}}' ve '{{1|EDİLGEN 1/5 fiil, pas z=0,81}}'; "
 "6:38 '{{2|fâsıla يحشرون → ن, N sınıfı}}', '{{2|simetri \\[3, 1, 19, 1\\]}}', '{{2|harf 85 → harf3 80, isaret 5}}', '{{2|dış düğüm 0}}', '{{2|biçim HASR}}' ve '{{2|EDİLGEN 1/3 fiil, pas z=1,57}}'; "
 "6:39 '{{3|fâsıla مستقيم → م, N sınıfı}}', '{{3|simetri \\[3, 8, 12, 1\\]}}', '{{3|harf 75 → harf3 69, isaret 6}}' ve '{{3|dış düğüm 2}}'; "
 "6:40 '{{4|fâsıla صدقين → ن, N sınıfı}}', '{{4|simetri \\[3, 3, 7, 1\\]}}', '{{4|harf 61 → harf3 61, isaret 0}}', '{{4|dış düğüm 3}}' ve '{{4|İÇ düğüm 1}}'; "
 "6:41 '{{5|fâsıla تشركون → ن, N sınıfı}}', '{{5|simetri \\[3, 1, 7, 1\\]}}', '{{5|harf 46 → harf3 46, isaret 0}}', '{{5|dış düğüm 0}}' ve '{{5|biçim IDRAB}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 37 41 09'): KALAN_P",
 "ölçüm aktör: 6:37-41 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:37 emir — IMPV 1 'qul' (8.), NEG 1 'lâ' (18.); "
 "6:38 haber — NEG 3 'mâ' (1.), 'lâ' (6.), 'mâ' (13.), RES 1 'illâ' (10.); 6:39 şart — COND 2 'men' (8.), 've men' (12.); "
 "6:40 soru, emir, şart — COND 2 'in' (3., 13.), IMPV 1 'qul' (1.), INTG 2 'era'eytekum' (2.), 'e-ğayra' (10.); 6:41 şart — COND 1 'in' (8.); "
 "morph EXH ('levlâ' 6:37 2.), ACC ('inne' 6:37 9.; 'lâkinne' 6:37 16.), SUB ('en' 6:37 13.), REM ('ve' 6:37 1. ve 16.; 6:38 1.; 6:39 1.), RET ('bel' 6:41 1.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:38 ★ (kaynak pas, z=1,57); 6:40 ★★ (kaynak allah, z=2,14); 6:37, 6:39 ve 6:41 yıldız yok",
 "fâsıla: 6:36 ن → 6:37 ن (يعلمون) → 6:38 ن (يحشرون) → 6:39 م (مستقيم) → 6:40 ن (صدقين) → 6:41 ن (تشركون) — N sınıfı sürüyor; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:37 okunmuş 1 ayet; 6:38 yok; 6:39 okunmuş 2 ayet; 6:40 okunmuş 3 ayet ve okunmamış 1 ayet (sûre içi 1); 6:41 yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:37 'qâdir 'alâ en' süzgeç GEÇMEZ; 6:38 'summe ilâ rabb' süzgeç GEÇER; 6:40 'qâle ra'â in etâ 'azâb allâh' ve 'qâle ra'â in' GEÇER, 'in kâne sâdiq' GEÇMEZ; "
 "6:39 ve 6:41 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; edilgen fiilde naib-i faili zamir 'adsız' ile — sûre 6 bölüm 2 denetimi kuralı 5; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8): "
 "6:37 3MP (adsız — gönderge 6:33 11. kelime), 3MS ('nuzzile' edilgen — naib-i faili 'âyetun' 5. kelime; ''aleyhi', 'rabbih' adsız — gönderge elçi; 'yunezzile' adsız — gönderge lafız), muhatap 2MS; "
 "6:38 3MS (adsız — gönderge 'tâ'irin'), muhatap 2MP, konuşan 1P, 3MP (adsız — gönderge 'umemun'; 'yuhşerûn' edilgen — naib-i faili zamir); "
 "6:39 3MP (adsız — gönderge 'llezîne'), konuşan 1P, 3MS ('yeşe'i' 9. kelime — fail 10. kelime; zamirler adsız — gönderge lafız ve 'men'); "
 "6:40 muhatap 2MS, muhatap 2MP, 3MS ('etâkum' 4. kelime — fail 5. kelime), 3FS ('etetkumu' 8. kelime — fail 9. kelime); "
 "6:41 muhatap 2MP, 3MS (adsız — gönderge 6:40 11. kelime) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): "
 "6:37 'qâlû' (1.) ardından söz 2-7. kelime, 'qul' (8.) ardından söz 9-15. kelime — ayet içi kapanışlar; 16-19. kelime ('ve lâkinne', morph REM) söz dışı; 6:40 'qul' (1.) ardından söz 2-15. kelime — ayet içi kapanış; 6:38, 6:39 ve 6:41 söz yok; mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 37 41 09' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 6:37 've qâlû' (1.), 've lâkinne' (16.) REM; 6:38 've mâ' (1.) REM, 've lâ' (6.) CONJ; 6:39 've'llezîne' (1.) REM, 've bukmun' (5.), 've men' (12.) CONJ; 6:41 'fe-yekşifu' (4.), 've tensevne' (10.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:38 ◈K أرض ('l-ardi' 5. kelime — K1); 6:38 ◈B دبب ('dâbbetin' 3. kelime — B1); 6:38 ◈B طير ('tâ'irin' 7. kelime — B1; anlam notu: yerde yürüyen ve uçan canlılar); 6:40 ◈K سوع ('s-sâ'atu' 9. kelime — K2)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 37 41 09'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:37 (13:7); 6:38 (11:6); 6:39, 6:40 ve 6:41 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp yok; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:37 edim geçişi haber → emir; 6:38 edim geçişi emir → haber; 6:39 şart → cevap ('men' 8. kelime / 'yudlilhu' 11. kelime; 'men' 12. kelime / 'yec'alhu' 14. kelime), edim geçişi haber → şart; "
 "6:40 şart → cevap ('in' 3. kelime / 'e-ğayra'llâhi ted'ûn' 10. kelime; 'in' 13. kelime — cevap hazif), şahıs geçişi 3 → 2, edim geçişi şart → soru, emir, şart; 6:41 'in' 8. kelime — cevap hazif, edim geçişi soru, emir, şart → şart, bölüm kapanışı; "
 "şahıs beraberliği yok (sûre 6 bölüm 1 denetimi kuralı 9); ölçüm iltifât 6:37-41 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:37 've qâlû' — istînâf (morph REM); 'levlâ' — tahdîd / istek (morph EXH); 'inne'llâhe qâdirun' — tekit (morph ACC); 've lâkinne' — istînâf ve istidrak (morph REM + ACC); "
 "6:38 've mâ … illâ' — istînâf ve hasr (morph REM + NEG + RES); 'mâ farratnâ' — nefy (morph NEG); 6:39 've'llezîne' — istînâf (morph REM); 'men … ve men' — karşıt şart çifti (morph COND); "
 "6:40 'era'eytekum' — soru (morph INTG); 'in … ev' — şart (morph COND); 'e-ğayra'llâhi' — takdimli soru (morph INTG); 6:41 'bel' — idrâb (morph RET); 'iyyâhu' — takdim (kasr); 'in şâ'e' — şart (morph COND)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:37 'âyetun min rabbih' — 13:7 ile eş (sayım: 'say 6:37 5-7'); 6:37 kök أيي, قول ve نزل ikilemesi; "
 "6:38 'dâbbetin fi'l-ard' — 11:6 ile eş (sayım: 'say 6:38 3-5'); 6:38 kök طير ikilemesi; 6:39 'yudlilhu' / 'yec'alhu 'alâ sırâtin mustaqîm' karşıtlığı; 6:40 kök أتي ikilemesi; 6:41 kök دعو ikilemesi; 6:40 / 6:41 çağırma yönü karşıtlığı",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 09'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'âyetun min rabbih' 6:37 'Rabbinden bir âyet' / 13:7 'Rabbinden bir mucize' (emsal metninde) — çakışma — tam okuma sonu ('âyet' / 'mucize'); "
 "'min rabbih' 6:37 'Rabbinden' / 13:7 'Rabbinden' (emsal metninde) — çakışma değil; "
 "'dâbbetin fi'l-ard' 6:38 'Yeryüzünde hiçbir canlı' / 11:6 'Yeryüzünde hiçbir canlı' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:37 'qâlû' PERF — meal 'Dediler'; 'nuzzile' PERF edilgen (levlâ ile) — meal 'indirilse ya'; 'qul' IMPV — meal 'De'; 'yunezzile' IMPF SUBJ — meal '-meye'; 'ya'lemûn' IMPF IND — meal 'bilmiyorlar'; "
 "6:38 'yetîru' IMPF IND — meal 'uçan'; 'farratnâ' PERF — meal 'etmedik'; 'yuhşerûn' IMPF IND edilgen — meal 'toplanacaklar'; 6:39 'kezzebû' PERF — meal 'yalanlayanlar'; 'yeşe'' IMPF JUS (şart) — meal 'dilerse'; 'yudlil', 'yec'al' IMPF JUS (şart cevabı) — meal geniş zaman; "
 "6:40 'ra'eyte' PERF (soru) — meal 'haber verin'; 'etâ', 'etet' PERF (şart) — meal 'gelse'; 'ted'ûn' IMPF IND — meal 'çağırırsınız'; 'kuntum' PERF (şart) — meal '-seniz'; "
 "6:41 'ted'ûne' IMPF IND — meal 'çağırırsınız' / '-dığınız'; 'yekşifu' IMPF IND — meal 'giderir'; 'şâ'e' PERF (şart) — meal 'dilerse'; 'tensevne', 'tuşrikûn' IMPF IND — meal 'unutursunuz' / '-tuklarınız'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 37 41 09'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:39 tarayıcı adayı (kök ظلم; A_şart) — çıpa değil: 'z-zulumât' sağırlık ve dilsizlik benzetmesi, doğa iddiası yok (olgu=False); 6:37, 6:38, 6:40 ve 6:41 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:37 ('nuzzile' / 'yunezzile'; 'qâdirun' / 'lâ ya'lemûn'); 6:38 ('dâbbetin fi'l-ardi' / 'tâ'irin yetîru'); 6:39 ('yudlilhu' / 'yec'alhu 'alâ sırâtin mustaqîm'; 'z-zulumât' / 'sırâtin mustaqîm'); 6:40 (''azâbu'llâhi' / 's-sâ'atu'); 6:41 ('ted'ûne' / 'tensevne'); "
 "ayetler arası 6:40 'e-ğayra'llâhi ted'ûn' / 6:41 'iyyâhu ted'ûn'; eşleme betikle: ADAY_P",
 "aday 1041: kök دعو 6:40 ('ted'ûn') ve 6:41 ('ted'ûne') — çağırma bağı; kök شيأ 6:38 ('şey'') ve 6:39, 6:41 ('yeşe'', 'şâ'e'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 4-2 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm iki blok (8, 9); bu blok bölümü kapatıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b09/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 37 41 09'; lem_bozuk.py 09 çıktısı): lem_bozuk bayrağı 6:38 8. kelime يَطِيرُ — meal maddelerinde (morph LEM ham biçim) notu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 37 41 → AYN_SONUC; sunum/bolum4_kurallar.py 37 41 09 → KHATA_HEPSI; sunum/bolum5_kurallar.py 37 41 09 → B5_HEPSI; sunum/bolum6_kurallar.py 37 41 09 → B6_HEPSI; sunum/bolum7_kurallar.py 37 41 09 → B7_HEPSI; sunum/bolum8_kurallar.py 37 41 09 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 37 41 09 → B9_HEPSI; sunum/bolum10_kurallar.py 37 41 09 → B10_HEPSI; sunum/bolum11_kurallar.py 37 41 09 → B11_HEPSI; sunum/bolum12_kurallar.py 37 41 09 → B12_HEPSI; sunum/bolum13_kurallar.py 37 41 09 → B13_HEPSI; sunum/bolum14_kurallar.py 37 41 09 → B14_HEPSI; sunum/bolum15_kurallar.py 37 41 09 → B15_HEPSI; sunum/bolum16_kurallar.py 37 41 09 → B16_HEPSI; sunum/bolum17_kurallar.py 37 41 09 → B17_HEPSI; sunum/bolum18_kurallar.py 37 41 09 → B18_HEPSI; sunum/bolum19_kurallar.py 37 41 09 → B19_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 9 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('qâdir', ''alâ', 'en', 'summe', 'ilâ', 'rabb', 'qâle', 'ra'â', 'in', 'etâ', ''azâb', 'allâh', 'kâne', 'sâdiq'); lemmasız öğe joker yok; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (37, 41): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_37_41.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b08.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '37', '41'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '37', '41', '09'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '37', '41', '09'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '37', '41', '09', '--tazelik-yok')}
    for _n in range(7, 20): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '37', '41', '09')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19 = [_R['B%d' % _n].splitlines() for _n in range(6, 20)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
           'MUT_SONUC': (MUT[-1] if MUT else '?'), 'GERI_P': ' / '.join(x.lstrip('# ') for x in GERI), 'B6_ESMA': ('; '.join(l[5:] for l in B6 if 'esmâ kural' in l and l.startswith('HATA')) or 'sapma 0')}
    I_cur = list(I_HAM)
    for k, v in REP.items(): I_cur = I_cur[:len(BEK)] + [x.replace(k, v) for x in I_cur[len(BEK):]]  # bölüm 9 kuralı 9: taşınan denetim maddelerine yer tutucu değişimi uygulanmaz
    I_cur[idx] = ("karşılık çakışması (bölüm 4 kuralı 4, bölüm 5 kuralı 3, bölüm 6 kuralı 2 — komut 'python3 sunum/cakisma.py' + sûre 6'nın okunmuş bütün ARIZA dosyaları; bu bloğun karşılıklarına dokunan gruplar ve son dosyaya dokunan KÖK grupları; grup başına tam bir kapalı karar: 'çakışma değil' ya da 'çakışma — tam okuma sonu'): "
                  + ('; '.join(KARAR.get(l.split(' ←')[0].strip() if not l.startswith('KÖK') else 'KÖK ' + l.split()[1], l + ' — karar yok') for l in CAK_L) if CAK_L else 'bu bloğa dokunan çakışma yok'))
    if I_cur == onceki: break
    onceki = list(I_cur)
yaz(I_cur)
print('yazıldı', len(I_cur), 'tur', tur)
print('\n'.join(CAK_L))
print(GLS)
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
