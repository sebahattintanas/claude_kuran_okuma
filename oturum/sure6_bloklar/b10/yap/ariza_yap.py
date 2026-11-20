# sûre 6 blok 10 (6:42-45) ARIZA oluşturucu — bölüm 5-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b10/olcum.txt'
os.environ['SAY2'] = '/home/claude/b10/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b09.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {}
BOL = "'Darlık ve bolluk; kulakları ve gözleri almak'"


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
 ("6:43", "'mâ kâne 'amile'", 3, 'say 6:43 12-14', "harekesiz 'mâ kânû ya'melûn' (12-14. kelime); biçim öğesi 'kâne' çekimi (lemma dizisi sûre içi 6, nakarat3 3)", None),
 ("6:45", "'allâh rabb 'âlem'", 2, 'say 6:45 7-9', "harekesiz 'li'llâhi rabbi'l-'âlemîn' (7-9. kelime)", None),
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

VF_YAZI = {42: {1: "'ve le-qad'", 7: "'fe-exaznâhum'"}, 43: {1: "'fe-levlâ'", 6: "'ve lâkin'", 9: "'ve zeyyene'"}, 44: {1: "'fe-lemmâ'", 18: "'fe-izâ'"}, 45: {1: "'fe-qutı'a'", 6: "'ve'l-hamdu'"}}
sys.path.insert(0, '/home/claude/b10/yap')
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
open('/home/claude/b10/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '10')
BLOKLAR = [str(i) for i in range(1, 11)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '10', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b10/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '42', '45', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b10/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b10/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '42', '45', '10').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_42_45.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:42', '6:43', '6:44', '6:45'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_42_45.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(42, 46))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:42 kök قبل ('qablike' 6. kelime — önce): zaman, tetik listesinde yok; 6:43 'iz' (2. kelime — morph T, zaman); 6:44 'lemmâ' (1. kelime — morph T, zaman); 6:44 'izâ' (12. kelime — morph T, zaman); 6:45 kök قطع ('qutı'a' 1. kelime — kesme): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '42', '45', '10')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b10/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 11)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(42, 46))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: sunum/bolum20_kurallar.py kural 1 — ara geçiş metni '(geçici)' desenden çıkarıldı (öz denetim koşusu ara yamayı okuyor; son kayıt elle taranır — sûre 6 blok 10); mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 158",
 "kök tablosu: ölçümde '???' 6:42-45 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 42 45 10'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: blokta esmâ yok (ölçüm 6:42-45); esma_el kaydı yok; "
 "lafız 6:45; Rab 6:45 (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 42 45 10'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:42 '{{1|fâsıla يتضرعون → ن, N sınıfı}}', '{{1|harf 57 → harf3 56, isaret 1}}' ve '{{1|dış düğüm 2}}'; "
 "6:43 '{{2|fâsıla يعملون → ن, N sınıfı}}', '{{2|harf 64 → harf3 62, isaret 2}}', '{{2|dış düğüm 0}}' ve '{{2|aktör: adlı شَيْطان 11\\. sırada \\(gayb, rol fail\\)}}'; "
 "6:44 '{{3|fâsıla مبلسون → ن, N sınıfı}}', '{{3|simetri \\[3, 1, 5, 1\\]}}', '{{3|harf 83 → harf3 77, isaret 6}}', '{{3|dış düğüm 0}}' ve '{{3|EDİLGEN 2/6 fiil, pas z=1,57}}'; "
 "6:45 '{{4|fâsıla ٱلعلمين → ن, N sınıfı}}', '{{4|harf 43 → harf3 41, isaret 2}}', '{{4|dış düğüm 0}}' ve '{{4|EDİLGEN 1/2 fiil, pas z=2,52}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 42 45 10'): KALAN_P",
 "ölçüm aktör: 6:43 'aktör: adlı شَيْطان 11. sırada (gayb, rol fail)' — 'zeyyene' faili; 6:42, 6:44 ve 6:45 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:42 haber — CERT 1 'qad' (1.), EMPH 1 'le' (1.); "
 "6:43 haber — kip yok; 6:44 haber — kip yok; 6:45 haber — kip yok; "
 "morph EXH ('levlâ' 6:43 1.), ACC ('le'alle' 6:42 10.), AMD ('lâkin' 6:43 6.), T ('iz' 6:43 2.; 'lemmâ' 6:44 1.; 'izâ' 6:44 12.), INC ('hattâ' 6:44 11.), SUR ('izâ' 6:44 18.), "
 "REM ('ve' 6:42 1.; 'fe' 6:43 1.; 've' 6:43 6.; 'fe' 6:44 1. ve 18.; 'fe' 6:45 1.; 've' 6:45 6.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:44 ★ (kaynak pas, z=1,57); 6:45 ★★ (kaynak pas, z=2,52; rab, z=2,05; allah, z=1,69); 6:42 ve 6:43 yıldız yok",
 "fâsıla: 6:41 ن → 6:42 ن (يتضرعون) → 6:43 ن (يعملون) → 6:44 ن (مبلسون) → 6:45 ن (ٱلعلمين) — N sınıfı sürüyor; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:42 16:63 (emsal olarak basıldı) ve okunmamış 1 ayet; 6:43 yok; 6:44 yok; 6:45 yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:43 'mâ kâne 'amile' süzgeç GEÇER; 6:45 'allâh rabb 'âlem' süzgeç GEÇMEZ; "
 "6:42 ve 6:44 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; edilgen fiilde naib-i faili zamir 'adsız' ile — sûre 6 bölüm 2 denetimi kuralı 5; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:42 konuşan 1P, muhatap 2MS, 3MP (adsız — gönderge 'umemin' 4. kelime); "
 "6:43 3MS ('câ'ehum' 3. kelime — fail 4. kelime; 'zeyyene' 9. kelime — fail 11. kelime), konuşan 1P, 3MP (adsız — gönderge 6:42 4. kelime), 3FS ('qaset' 7. kelime — fail 8. kelime); "
 "6:44 3MP (adsız — gönderge 6:42 4. kelime; 'zukkirû' ve 'ûtû' edilgen — naib-i faili zamir), konuşan 1P, 3MS ('bihî' adsız — gönderge 'mâ' 3. kelime); "
 "6:45 3MS ('fe-qutı'a' edilgen — naib-i faili 'dâbiru' 2. kelime), 3MP (adsız — gönderge 'llezîne') — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): "
 "6:42-45 söz yok; mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 42 45 10' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 6:42 've le-qad' (1.) REM, 'fe-exaznâhum' (7.) CONJ; 6:43 'fe-levlâ' (1.), 've lâkin' (6.) REM, 've zeyyene' (9.) CONJ; 6:44 'fe-lemmâ' (1.), 'fe-izâ' (18.) REM; 6:45 'fe-qutı'a' (1.), 've'l-hamdu' (6.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:43 ◈B قلب ('qulûbuhum' 8. kelime — B3; anlam notu: kalplerin katılaşması)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 42 45 10'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:42 (16:63); 6:45 (37:182); 6:43 ve 6:44 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp yok; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:42 şahıs geçişi 2 → 1, edim geçişi şart → haber, şahıs sayısında beraberlik (1P 4 · 3MP 4), bölüm açılışı; 6:43 şahıs geçişi 1 → 3; 6:44 şahıs geçişi yok; 6:45 şahıs geçişi yok; "
 "COND yok; şahıs beraberliği 6:42 (sûre 6 bölüm 1 denetimi kuralı 9); ölçüm iltifât 6:42-45 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:42 've le-qad' — istînâf ve yemin tekidi (morph REM + EMPH + CERT); 'le'allehum' — tereccî (morph ACC); "
 "6:43 'fe-levlâ' — istînâf ve tahdîd (morph REM + EXH); 've lâkin' — istînâf ve istidrak (morph REM + AMD); 6:44 'fe-lemmâ … fetahnâ' — istînâf, zaman zarfı ve cevabı (morph REM + T); "
 "'hattâ izâ … exaznâhum' — gaye ve zaman zarfı (morph INC + T); 'fe-izâ hum' — istînâf ve ani durum (morph REM + SUR); 6:45 'fe-qutı'a' — istînâf (morph REM); 've'l-hamdu' — istînâf (morph REM)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:42 'ilâ umemin min qablik' — 16:63 ile eş (sayım: 'say 6:42 3-6'); "
 "6:45 've'l-hamdu li'llâhi rabbi'l-'âlemîn' — 37:182 ile eş (sayım: 'say 6:45 6-9'); 6:42 'le'allehum yetedarra'ûn' / 6:43 'tedarra'û' — kök ضرع bağı; 6:42 'fe-exaznâhum' / 6:44 'exaznâhum' — kök أخذ bağı",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 10'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'ilâ umemin min qablik' 6:42 'senden önceki ümmetlere' / 16:63 'senden önceki ümmetlere' (emsal metninde) — çakışma değil; "
 "'ve'l-hamdu li'llâhi rabbi'l-'âlemîn' 6:45 'Hamd, âlemlerin Rabbi Allah'adır' / 37:182 'Hamd, âlemlerin Rabbi Allah'adır' (emsal metninde) — çakışma değil; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:42 'erselnâ' PERF — meal 'gönderdik'; 'exaznâ' PERF — meal 'yakaladık'; 'yetedarra'ûn' IMPF IND — meal 'yalvarırlar'; "
 "6:43 'câ'e' PERF — meal 'geldiğinde'; 'tedarra'û' PERF (levlâ ile) — meal 'yalvarsalardı'; 'qaset' PERF — meal 'katılaştı'; 'zeyyene' PERF — meal 'süslü gösterdi'; 'kânû' PERF + 'ya'melûn' IMPF IND — meal 'yapmakta oldukları'; "
 "6:44 'nesû' PERF — meal 'unuttuklarında'; 'zukkirû' PERF edilgen — meal 'hatırlatılan'; 'fetahnâ' PERF — meal 'açtık'; 'ferihû' PERF — meal 'sevindiklerinde'; 'ûtû' PERF edilgen — meal 'verilen'; 'exaznâ' PERF — meal 'yakaladık'; "
 "6:45 'qutı'a' PERF edilgen — meal 'kesildi'; 'zalemû' PERF — meal 'zulmeden'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 42 45 10'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:42, 6:43, 6:44 ve 6:45 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:43 ('tedarra'û' / 'qaset qulûbuhum'); 6:44 ('nesû' / 'zukkirû'; 'ferihû' / 'mublisûn'); 6:45 ('qutı'a dâbiru'l-qavmi' / 've'l-hamdu li'llâh'); 6:42 yok; "
 "ayetler arası çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök ضرع 6:42 ('yetedarra'ûn') ve 6:43 ('tedarra'û'); kök أخذ 6:42 ('fe-exaznâhum') ve 6:44 ('exaznâhum'); kök بأس 6:42 ('l-be'sâ'i') ve 6:43 ('be'sunâ'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 5-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm iki blok (10, 11); "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b10/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 42 45 10'; lem_bozuk.py 10 çıktısı): lem_bozuk bayrağı 6:43 5. kelime تَضَرَّعُ, 6:43 7. kelime قَسَتْ, 6:44 4. kelime ذُكِّرَ, 6:45 1. kelime قُطِعَ — meal maddelerinde (morph LEM ham biçim) notu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 42 45 → AYN_SONUC; sunum/bolum4_kurallar.py 42 45 10 → KHATA_HEPSI; sunum/bolum5_kurallar.py 42 45 10 → B5_HEPSI; sunum/bolum6_kurallar.py 42 45 10 → B6_HEPSI; sunum/bolum7_kurallar.py 42 45 10 → B7_HEPSI; sunum/bolum8_kurallar.py 42 45 10 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 42 45 10 → B9_HEPSI; sunum/bolum10_kurallar.py 42 45 10 → B10_HEPSI; sunum/bolum11_kurallar.py 42 45 10 → B11_HEPSI; sunum/bolum12_kurallar.py 42 45 10 → B12_HEPSI; sunum/bolum13_kurallar.py 42 45 10 → B13_HEPSI; sunum/bolum14_kurallar.py 42 45 10 → B14_HEPSI; sunum/bolum15_kurallar.py 42 45 10 → B15_HEPSI; sunum/bolum16_kurallar.py 42 45 10 → B16_HEPSI; sunum/bolum17_kurallar.py 42 45 10 → B17_HEPSI; sunum/bolum18_kurallar.py 42 45 10 → B18_HEPSI; sunum/bolum19_kurallar.py 42 45 10 → B19_HEPSI; sunum/bolum20_kurallar.py 42 45 10 → B20_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 10 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('mâ', 'kâne', ''amile', 'allâh', 'rabb', ''âlem'); lemmasız öğe joker yok; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (42, 45): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_42_45.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b09.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '42', '45'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '42', '45', '10'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '42', '45', '10'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '42', '45', '10', '--tazelik-yok')}
    for _n in range(7, 21): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '42', '45', '10')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20 = [_R['B%d' % _n].splitlines() for _n in range(6, 21)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
