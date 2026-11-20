# sûre 6 blok 12 (6:50-53) ARIZA oluşturucu — bölüm 6-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b12/olcum.txt'
os.environ['SAY2'] = '/home/claude/b12/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b11.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {}
BOL = "'De ki: gaybı bilmem; sabah akşam Rablerine dua edenler'"


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
 ("6:50", "'in ittebe illâ'", 3, 'say 6:50 16-18', "harekesiz 'in ettebi'u illâ' (16-18. kelime)", ('dizi 6 50 16 18', "in ittebe illâ", '16-18', "biçim farkı (dizi 6 50 16 18): basılmamış eş fiil çekimi, zamir eki; basılmamış eş fiil çekimi, zamir eki")),
 ("6:50", "'mâ evhâ ilâ'", 2, 'say 6:50 19-21 --on', "önek kesilmiş 'mâ yûhâ ileyy' (19-21. kelime)", ('dizi 6 50 19 21', "mâ evhâ ilâ", '19-21', "biçim farkı (dizi 6 50 19 21): basılmamış eş zamir eki; basılmamış eş yazım eş; biçim öğesi 'evhâ' çekimi (lemma dizisi sûre içi 3, nakarat3 2); öneksiz eş koşusu (dizi 6 50 19 21): basılmamış eş → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 1")),
 ("6:51", "'veliyy lâ şefî''", 2, 'say 6:51 13-15', "harekesiz 'veliyyun ve lâ şefî'' (13-15. kelime)", None),
 ("6:52", "'min hisâb min şey''", 2, 'say 6:52 12-15', "harekesiz 'min hisâbihim min şey'' (12-15. kelime)", None),
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

VF_YAZI = {50: {8: "'ve lâ'", 11: "'ve lâ'", 26: "'ve'l-basîr'", 27: "'e-fe-lâ'"}, 51: {1: "'ve enzir'", 14: "'ve lâ'"}, 52: {1: "'ve lâ'", 7: "'ve'l-'aşiyyi'", 16: "'ve mâ'", 22: "'fe-tatrudehum'", 23: "'fe-tekûne'"}, 53: {1: "'ve kezâlike'"}}
sys.path.insert(0, '/home/claude/b12/yap')
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
open('/home/claude/b12/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '12')
BLOKLAR = [str(i) for i in range(1, 13)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '12', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b12/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '50', '53', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b12/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b12/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '50', '53', '12').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_50_53.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:50', '6:51', '6:52', '6:53'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_50_53.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(50, 54))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:50 kök عمي ('l-a'mâ' 25. kelime — körlük): tetik listesinde yok; 6:51 kök ولي ('veliyyun' 13. kelime — dost): tetik listesinde yok; 6:52 kök غدو ('l-ğadâti' 6. kelime — sabah), kök عشو ('l-'aşiyyi' 7. kelime — akşam), kök وجه ('vechehû' 9. kelime — yüz): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '50', '53', '12')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b12/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 13)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(50, 54))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: b12/yap/kur.py K1 üretimi — medde farkı olan kalıp 'korpusta 1' listesinden çıkarıldı (sûre 6 bölüm 5 denetimi kuralı 6, TEKIL_MEDDE; sûre 6 blok 12); sunum/edat_etiket.py EDLEM'e ''ulâ'i'' (ذا) — bölüm 15 denetimi kuralı 15: es_edat 6:53 'ulâ'i' başlığını tanısın diye; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 170",
 "kök tablosu: ölçümde '???' 6:50-53 için 0 — yeni kök yok; "
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 50 53 12'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:50 'yestevi'l-a'mâ ve'l-basîr' (24-26. kelime) — esma_el 'degil', kural 'çoğul insan göndergeli' (insan göndergesi; 'l-basîr' cins: gören insan, körün karşıtı; 'ş-şâkirîn' çoğul); 6:51 'min dûnihî veliyyun' (11-13. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge); 6:53 'bi'ş-şâkirîn' (15. kelime) — esma_el 'degil', kural 'çoğul insan göndergeli' (insan göndergesi; 'l-basîr' cins: gören insan, körün karşıtı; 'ş-şâkirîn' çoğul); 6:52 esmâ yok; "
 "lafız 6:50 ve 6:53; Rab 6:51 ve 6:52 (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 50 53 12'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 6:50, 6:51, 6:53 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı): " + EMH,
 "ölçüm: 6:50 '{{1|fâsıla تتفكرون → ن, N sınıfı}}', '{{1|simetri \\[6, 8, 18, 2\\]}}', '{{1|harf 106 → harf3 103, isaret 3}}', '{{1|dış düğüm 5}}', '{{1|biçim HASR}}' ve '{{1|EDİLGEN 1/9 fiil, pas z=0,30}}'; "
 "6:51 '{{2|fâsıla يتقون → ن, N sınıfı}}', '{{2|simetri \\[3, 2, 10, 1\\]}}', '{{2|harf 70 → harf3 65, isaret 5}}', '{{2|dış düğüm 2}}' ve '{{2|EDİLGEN 1/5 fiil, pas z=0,81}}'; "
 "6:52 '{{3|fâsıla ٱلظلمين → ن, N sınıfı}}', '{{3|simetri \\[6, 10, 16, 2\\]}}', '{{3|harf 108 → harf3 104, isaret 4}}', '{{3|dış düğüm 1}}' ve '{{3|biçim NEHY}}'; "
 "6:53 '{{4|fâsıla بٱلشكرين → ن, N sınıfı}}', '{{4|harf 74 → harf3 70, isaret 4}}', '{{4|dış düğüm 2}}' ve '{{4|biçim DIKKAT}}' — satır aynen (◇'de de; iki araçla bayt eşitliği denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 50 53 12'): KALAN_P",
 "ölçüm aktör: 6:50-53 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:50 soru, emir — IMPV 2 'qul' (1., 22.), INTG 2 'hel' (23.), 'e-fe-lâ' (27.), NEG 5 'lâ' (2.), 've lâ' (8., 11.), 'in' (16.), 'e-fe-lâ' (27.), RES 1 'illâ' (18.); "
 "6:51 emir — IMPV 1 've enzir' (1.), NEG 1 've lâ' (14.); 6:52 yasak — NEG 2 'mâ' (10.), 've mâ' (16.), PRO 1 've lâ' (1.); 6:53 soru — INTG 2 'e-hâ'ulâ'i' (6.), 'e-leyse' (12.); "
 "morph ACC ('inne' 6:50 14.; 'le'alle' 6:51 16.), SUB ('en' 6:51 5.), SUP ('fe' 6:50 27.), CAUS ('fe' 6:52 22.), PRP ('li' 6:53 5.), ATT ('hâ' 6:53 6.), REM ('ve' 6:52 1.; 've' 6:53 1.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:50 ★ (kaynak n, z=1,65); 6:53 ★★ (kaynak allah, z=2,14); 6:51 ve 6:52 yıldız yok",
 "fâsıla: 6:49 ن → 6:50 ن (تتفكرون) → 6:51 ن (يتقون) → 6:52 ن (ٱلظلمين) → 6:53 ن (بٱلشكرين) — N sınıfı sürüyor; aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:50 11:31 (emsal olarak basıldı) ve okunmuş 4 ayet; 6:51 okunmuş 2 ayet; 6:52 18:28 (emsal olarak basıldı); 6:53 okunmuş 2 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:50 'in ittebe illâ' süzgeç GEÇER, 'mâ evhâ ilâ' GEÇMEZ; 6:51 'veliyy lâ şefî'' GEÇMEZ; 6:52 'min hisâb min şey'' GEÇER; "
 "6:53 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; edilgen fiilde naib-i faili zamir 'adsız' ile — sûre 6 bölüm 2 denetimi kuralı 5; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:50 muhatap 2MS, konuşan 1S (söz içi), muhatap 2MP (söz içi), 3MS ('yûhâ' edilgen — naib-i faili zamir; 'yestevi' 24. kelime — fail 25. kelime); "
 "6:51 muhatap 2MS, 3MS ('leyse' 9. kelime — fail 13. kelime; zamirler adsız — gönderge 6:50 19. kelime ve 'rabbihim'), 3MP (adsız — gönderge 'llezîne' 3. kelime; 'yuhşerû' edilgen — naib-i faili zamir); "
 "6:52 muhatap 2MS, 3MP (adsız — gönderge 'llezîne' 3. kelime), 3MS (adsız — gönderge 'rabbehum' 5. kelime); "
 "6:53 konuşan 1P (söz içi dahil), 3MP (adsız — gönderge 6:52 3. kelime ve 'hâ'ulâ'i'), 3MS ('menne' 7. kelime — fail 8. kelime; 'e-leyse' 12. kelime — fail 13. kelime) — betik denetimi: KHATA_ADSIZ",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): "
 "6:50 'qul' (1.) ardından söz 2-21. kelime, 'qul' (22.) ardından söz 23-28. kelime — ayet içi kapanışlar; 6:53 'li-yeqûlû' (5.) ardından söz 6-11. kelime — ayet içi kapanış; 6:51 ve 6:52 söz yok; mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 50 53 12' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' / 'fe' konumlarıyla kontrol edildi: 6:50 've lâ' (8., 11.), 've'l-basîr' (26.) CONJ, 'e-fe-lâ' (27.) SUP; 6:51 've enzir' (1.), 've lâ' (14.) CONJ; 6:52 've lâ' (1.) REM, 've'l-'aşiyyi' (7.), 've mâ' (16.), 'fe-tekûne' (23.) CONJ, 'fe-tatrudehum' (22.) CAUS; 6:53 've kezâlike' (1.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:50 ◈B بصر ('l-basîr' 26. kelime — B3; anlam notu: kör ile gören)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 50 53 12'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:50 (11:31); 6:52 (18:28); 6:51 ve 6:53 D3 eşi yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "ayetler arası kalıp yok; "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:50 söz açılır / kapanır (2-21. ve 23-28. kelime), şahıs geçişi 3 → 1, edim geçişi haber → soru, emir, bölüm açılışı; 6:51 şahıs geçişi 1 → 3, edim geçişi soru, emir → emir; 6:52 şahıs geçişi yok, edim geçişi emir → yasak; 6:53 söz açılır / kapanır (6-11. kelime), şahıs geçişi yok, edim geçişi yasak → soru; COND yok; "
 "şahıs beraberliği yok (sûre 6 bölüm 1 denetimi kuralı 9); ölçüm iltifât 6:50-53 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:50 'in ettebi'u illâ' — hasr (morph NEG + RES); 'hel yestevi' — soru (morph INTG); 'e-fe-lâ tetefekkerûn' — 'fe' morph SUP; soru ve nefy (morph INTG + NEG); 6:51 'le'allehum' — tereccî (morph ACC); "
 "6:52 've lâ tatrudi' — istînâf ve yasak (morph REM + PRO); 'fe-tatrudehum' — nefyin cevabı (morph CAUS); "
 "6:53 've kezâlike' — istînâf (morph REM); 'li-yeqûlû' — amaç (morph PRP); 'e-leyse' — takrir sorusu (morph INTG)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:50 ''indî xazâ'inu'llâh' — 11:31 ile eş (sayım: 'say 6:50 5-7'); 6:50 kök قول ikilemesi; "
 "6:52 'llezîne yed'ûne rabbehum bi'l-ğadâti ve'l-'aşiyyi yurîdûne vechehû' — 18:28 ile eş (sayım: 'say 6:52 3-9'); 6:52 kök حسب, شيأ, طرد ikilemesi; 6:53 kök أله, بعض ikilemesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 12'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "''indî xazâ'inu'llâh' 6:50 'Allah'ın hazineleri yanımdadır' / 11:31 'Allah'ın hazineleri yanımdadır' (emsal metninde) — çakışma değil; "
 "'llezîne yed'ûne rabbehum bi'l-ğadâti ve'l-'aşiyyi yurîdûne vechehû' 6:52 'Sabah akşam Rablerine, O'nun yüzünü isteyerek dua edenleri' / 18:28 'Sabah akşam Rablerine, O'nun rızasını dileyerek yalvaranlarla' (emsal metninde) — çakışma — tam okuma sonu ('yüz' / 'rıza'; 'iste-' / 'dile-'; 'dua et-' / 'yalvar-'); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:50 'qul' IMPV — meal 'De'; 'eqûlu' IMPF IND — meal 'demiyorum', 'söylemiyorum'; 'a'lemu' IMPF IND — meal 'bilmem'; 'ettebi'u' IMPF IND — meal 'uyarım'; 'yûhâ' IMPF edilgen — meal 'vahyolunan'; 'yestevi' IMPF IND — meal 'eşit olur'; 'tetefekkerûn' IMPF IND — meal 'düşünmez'; "
 "6:51 've enzir' IMPV — meal 'uyar'; 'yaxâfûne' IMPF IND — meal 'korkan'; 'yuhşerû' IMPF SUBJ edilgen — meal 'toplanmak'; 'leyse' PERF (nefy) — meal 'yoktur'; 'yetteqûn' IMPF IND — meal 'sakınırlar'; "
 "6:52 'tatrudi' IMPF JUS (yasak) — meal 'kovma'; 'yed'ûne' IMPF IND — meal 'dua eden'; 'yurîdûne' IMPF IND — meal 'isteyerek'; 'tatrude', 'tekûne' IMPF SUBJ — meal 'kovasın', 'olasın'; "
 "6:53 'fetennâ' PERF — meal 'sınadık'; 'yeqûlû' IMPF SUBJ — meal 'desinler'; 'menne' PERF — meal 'lütfettiği'; 'leyse' PERF (nefy) — meal 'değil'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 50 53 12'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:50, 6:51, 6:52 ve 6:53 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:50 ('l-a'mâ' / 'l-basîr'); 6:52 ('min hisâbihim' / 'min hisâbike'; 'l-ğadâti' / 'l-'aşiyyi'); 6:51 yok; 6:53 yok; "
 "ayetler arası çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök بصر 6:46 ('ebsârakum') ve 6:50 ('l-basîr'); kök دعو 6:41 ('ted'ûne') ve 6:52 ('yed'ûne'); kök خوف 6:48 ('xavfun') ve 6:51 ('yaxâfûne'); kök حشر 6:38 ('yuhşerûn') ve 6:51 ('yuhşerû'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 6-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm iki blok (12, 13); "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b12/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 50 53 12'; lem_bozuk.py 12 çıktısı): lem_bozuk bayrağı 6:50 28. kelime يَتَفَكَّرُ, 6:53 2. kelime فَتَنُ — meal maddelerinde (morph LEM ham biçim) notu; HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 50 53 → AYN_SONUC; sunum/bolum4_kurallar.py 50 53 12 → KHATA_HEPSI; sunum/bolum5_kurallar.py 50 53 12 → B5_HEPSI; sunum/bolum6_kurallar.py 50 53 12 → B6_HEPSI; sunum/bolum7_kurallar.py 50 53 12 → B7_HEPSI; sunum/bolum8_kurallar.py 50 53 12 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 50 53 12 → B9_HEPSI; sunum/bolum10_kurallar.py 50 53 12 → B10_HEPSI; sunum/bolum11_kurallar.py 50 53 12 → B11_HEPSI; sunum/bolum12_kurallar.py 50 53 12 → B12_HEPSI; sunum/bolum13_kurallar.py 50 53 12 → B13_HEPSI; sunum/bolum14_kurallar.py 50 53 12 → B14_HEPSI; sunum/bolum15_kurallar.py 50 53 12 → B15_HEPSI; sunum/bolum16_kurallar.py 50 53 12 → B16_HEPSI; sunum/bolum17_kurallar.py 50 53 12 → B17_HEPSI; sunum/bolum18_kurallar.py 50 53 12 → B18_HEPSI; sunum/bolum19_kurallar.py 50 53 12 → B19_HEPSI; sunum/bolum20_kurallar.py 50 53 12 → B20_HEPSI; sunum/bolum21_kurallar.py 50 53 12 → B21_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 12 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; sayımlar işaretlemeden sonra sinifla.py ile yeniden sınıflandı (say2.txt); "
 "lemma adları morph lemmasından ham transliterasyonla ('in', 'ittebe', 'illâ', 'mâ', 'evhâ', 'ilâ', 'veliyy', 'lâ', 'şefî'', 'min', 'hisâb', 'şey''); lemmasız öğe joker yok; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (50, 53): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_50_53.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b11.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '50', '53'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '50', '53', '12'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '50', '53', '12'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '50', '53', '12', '--tazelik-yok')}
    for _n in range(7, 22): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '50', '53', '12')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21 = [_R['B%d' % _n].splitlines() for _n in range(6, 22)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
