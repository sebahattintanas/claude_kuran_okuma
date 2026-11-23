# sûre 6 blok 36 (6:148-150) ARIZA oluşturucu — bölüm 17-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b36/olcum.txt'
os.environ['SAY2'] = '/home/claude/b36/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Haram kılınanlar; şahitlerinizi getirin'"


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
 ("6:148", "'in ittebe illâ zann in'", 2, 'say 6:148 30-34', "harekesiz 'in tettebi'ûne illa'z-zanne ve in' (30-34. kelime)", ('dizi 6 148 30 34', 'in ittebe illâ zann in', '30-34', 'biçim farkı (dizi 6 148 30 34): 6:116 fiil çekimi, zamir eki')),
 ("6:148", "'şâ'e allâh mâ eşrake'", 2, 'say 6:148 5-8', "harekesiz 'şâ'e'llâhu mâ eşraknâ' (5-8. kelime)", ('dizi 6 148 5 8', "şâ'e allâh mâ eşrake", '5-8', 'biçim farkı (dizi 6 148 5 8): 6:107 fiil çekimi, zamir eki')),
 ("6:148", "'in ittebe illâ'", 3, 'say 6:148 30-32', "harekesiz 'in tettebi'ûne illa' (30-32. kelime)", ('dizi 6 148 30 32', 'in ittebe illâ', '30-32', 'biçim farkı (dizi 6 148 30 32): 6:50 fiil çekimi, zamir eki; 6:116 fiil çekimi, zamir eki')),
 ("6:148", "'şâ'e allâh mâ'", 3, 'say 6:148 5-7', "harekesiz 'şâ'e'llâhu mâ' (5-7. kelime)", ('dizi 6 148 5 7', "şâ'e allâh mâ", '5-7', 'biçim farkı (dizi 6 148 5 7): 6:107 yazım eş; 6:137 yazım eş')),
 ("6:148", "'lev şâ'e allâh'", 2, 'say 6:148 4-6', "harekesiz 'lev şâ'e'llâh' (4-6. kelime); biçim öğesi 've' / 'fe' öneki (lemma dizisi sûre içi 4, nakarat3 2)", ('dizi 6 148 4 6', "lev şâ'e allâh", '4-6', 'biçim farkı (dizi 6 148 4 6): 6:35 önek; 6:107 önek; 6:137 önek; öneksiz eş koşusu (dizi 6 148 4 6): 6:35 → önek kesilmiş sûre içi 3; 6:107 → önek kesilmiş sûre içi 3; 6:137 → önek kesilmiş sûre içi 3')),
 ("6:148", "'mâ eşrake lâ'", 2, 'say 6:148 7-9', "harekesiz 'mâ eşraknâ ve lâ' (7-9. kelime)", ('dizi 6 148 7 9', 'mâ eşrake lâ', '7-9', 'biçim farkı (dizi 6 148 7 9): 6:81 fiil çekimi, zamir eki')),
 ("6:150", "'ellezî lâ âmene âxir'", 2, 'say 6:150 21-24', "harekesiz 'llezîne lâ yu'minûne bi'l-âxira' (21-24. kelime)", ('dizi 6 150 21 24', 'ellezî lâ âmene âxir', '21-24', 'biçim farkı (dizi 6 150 21 24): 6:113 önek')),
 ("6:150", "'ellezî lâ âmene'", 3, 'say 6:150 21-23', "harekesiz 'llezîne lâ yu'minûne' (21-23. kelime)", ('dizi 6 150 21 23', 'ellezî lâ âmene', '21-23', 'biçim farkı (dizi 6 150 21 23): 6:113 önek; 6:125 önek')),
 ("6:150", "'ellezî kezzebe âye'", 2, 'say 6:150 18-20', "harekesiz 'llezîne kezzebû bi-âyâtinâ' (18-20. kelime); biçim öğesi 've' öneki (lemma dizisi sûre içi 3, nakarat3 2)", ('dizi 6 150 18 20', 'ellezî kezzebe âye', '18-20', 'biçim farkı (dizi 6 150 18 20): 6:39 önek; 6:49 önek; öneksiz eş koşusu (dizi 6 150 18 20): 6:39 → önek kesilmiş sûre içi 2; 6:49 → önek kesilmiş sûre içi 2')),
 ("6:150", "'lâ ittebe ehvâ''", 2, 'say 6:150 15-17', "harekesiz 've lâ tettebi' ehvâ'e' (15-17. kelime)", ('dizi 6 150 15 17', "lâ ittebe ehvâ'", '15-17', 'biçim farkı (dizi 6 150 15 17): 6:56 fiil çekimi, zamir eki, önek')),
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

VF_YAZI = {148: {9: "'ve lâ'", 11: "'ve lâ'", 34: "'ve in'"}, 149: {}, 150: {15: "'ve lâ'", 21: "'ve'llezîne'", 25: "'ve hum'"}}
sys.path.insert(0, '/home/claude/b36/yap')
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
open('/home/claude/b36/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '36')
BLOKLAR = [str(i) for i in range(1, 37)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '36', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b36/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '148', '150', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b36/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b36/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '148', '150', '36').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_148_150.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:148', '6:149', '6:150'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_148_150.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(148, 151))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:148 kök أبو ('âbâ'unâ' 10. kelime — ata), kök ذوق ('zâqû' 21. kelime — tatma), kök قبل ('qablihim' 19. kelime — önce); 6:149 kök جمع ('ecma'în' 8. kelime — hep); 6:150 kök أخر ('l-âxirati' 24. kelime — ahiret): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '148', '150', '36')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b36/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 37)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(148, 151))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 16 kapanışında sunum/bolum32_kurallar.py eklendi (kural 1-5), sunum/bolum19_kurallar.py KURAL_ATIF bölüm 16, sunum/geriye_donuk.py bolum32 satırı, sunum/mutasyon_sina.py b32 sınamaları (343 / 343); bu blokta araç değişikliği yok; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 322",
 "geriye dönük koşu (bölüm 16 kapanışı, komut 'python3 sunum/geriye_donuk.py b34k yamalar/geriye_donuk_6_b31k.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 148 150 36'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:150 'helumme şuhedâ'akum' (2-3. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (muhatap topluluğun şahitleri) (yamalar/esma_el_6_148_150.txt); 6:150 'yu'minûne bi'l-âxirati' (23-24. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge); "
 "شَهِيد lemmasında 6:150:3 ve 6:144:19 'degil' kayıtlarıyla 6:19:8 'ilahi' kaydı (lafzın haberi) ayrık — esmâ dışı gönderge / çerçeve ayrılığı; آخِر lemmasında önceki 'degil' kayıtlarıyla karar eş; 6:148 ve 6:149 esmâ yok; "
 "6:148 lafız (6. kelime), 6:149 lafız (2. kelime), 6:150 lafız (7. kelime) ve Rab (26. kelime) (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 148 150 36'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 6:150 esma_kayit 'mühür EVET' — ölçüm MÜHÜRSÜZ ile uyuşmuyor, araç tanımı farkı; muhur_el hayır, ölçümle uyuşuyor): " + EMH,
 "ölçüm: 6:148 '{{1|fâsıla تخرصون → ن, N sınıfı}}', '{{1|simetri \\[6, 13, 30, 2\\]}}', '{{1|harf 150 → harf3 143, isaret 7}}', '{{1|dış düğüm 3}}' ve '{{1|İÇ düğüm 1}}'; "
 "6:149 '{{2|fâsıla أجمعين → ن, N sınıfı}}', '{{2|harf 36 → harf3 35, isaret 1}}' ve '{{2|dış düğüm 1}}'; "
 "6:150 '{{3|esmâ شَهِيد 3\\. sırada, ORTA konum, MÜHÜRSÜZ \\| آخِر 24\\. sırada, ORTA konum, MÜHÜRSÜZ}}', '{{3|fâsıla يعدلون → ن, N sınıfı}}', '{{3|simetri \\[6, 4, 10, 2\\]}}', '{{3|harf 123 → harf3 119, isaret 4}}' ve '{{3|dış düğüm 0}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 148 150 36'): KALAN_P",
 "ölçüm aktör: 6:148, 6:149 ve 6:150 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:148 soru, emir, şart — COND 1 'lev' (4.), FUT 1 'se-yeqûlu' (1.), IMPV 1 'qul' (23.), INTG 1 'hel' (24.), NEG 5 'mâ' (7.), 'lâ' (9.), 'lâ' (11.), 'in' (30.), 'in' (34.), RES 1 'illâ' (36.); ölçüm biçim HASR + ISTISNA (D2'de yazılmadı); "
 "6:149 emir, şart — COND 1 'lev' (5.), EMPH 1 'le-hedâkum' (7.), IMPV 1 'qul' (1.); 6:150 emir, yasak, şart — COND 1 'in' (10.), IMPV 2 'qul' (1.), 'helumme' (2.), NEG 1 'lâ' (22.), PRO 2 'lâ' (12.), 'lâ' (15.); ölçüm biçim DIKKAT + NEHY (D2'de yazılmadı); "
 "morph EXP ('illâ' 6:148 32.), CAUS ('fe-tuxricûhu' 6:148 28.), SUP ('fe-lillâhi' 6:149 2.), REM ('fe-lev' 6:149 5., 'fe-in' 6:150 10., 've hum' 6:150 25.), RSLT ('fe-lâ' 6:150 12.), ACC ('enne' 6:150 6.), INC ('hattâ' 6:148 20.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:148 ★★ (kaynak n, z=2,61); 6:149 ★ (kaynak allah, z=1,97); 6:150 ★ (kaynak n, z=1,55)",
 "fâsıla: 6:147 ن → 6:148 ن (تخرصون) → 6:149 ن (أجمعين) → 6:150 ن (يعدلون) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:148 6:116 (basılmış), 10:66 (basılmış), 16:35 (emsal olarak basıldı) ve okunmuş 1 ayet; 6:149 16:9 (emsal olarak basıldı); 6:150 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:148 'in ittebe illâ zann in' süzgeç GEÇER, 'şâ'e allâh mâ eşrake' süzgeç GEÇER, 'in ittebe illâ' süzgeç GEÇER, 'şâ'e allâh mâ' süzgeç GEÇER, 'lev şâ'e allâh' süzgeç GEÇMEZ, 'mâ eşrake lâ' süzgeç GEÇMEZ; 6:149 nakarat3 yok; "
 "6:150 'ellezî lâ âmene âxir' süzgeç GEÇER, 'ellezî lâ âmene' süzgeç GEÇER, 'ellezî kezzebe âye' süzgeç GEÇMEZ, 'lâ ittebe ehvâ'' süzgeç GEÇMEZ",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; edilgen fiil 'naib-i faili'): "
 "6:148 3MS ('se-yeqûlu' — fiil uyumu, fail 2. kelime; 'şâ'e' — söz içi, fiil uyumu, fail 6. kelime; 'kezzebe' — fiil uyumu, fail 17. kelime; 'hu' eki — söz içi, gönderge ''ilmin' 27. kelime), 3MP ('eşrakû', 'qablihim' eki — gönderge 'llezîne' 2. kelime; 'zâqû' — gönderge 'llezîne' 17. kelime), konuşan 1P ('eşraknâ', 'âbâ'unâ', 'harramnâ', 'lenâ' — söz içi; 'be'senâ' eki), muhatap 2MS ('qul'), muhatap 2MP (''indekum', 'tuxricûhu', 'tettebi'ûne', 'entum', 'taxrusûn' — söz içi); "
 "6:149 muhatap 2MS ('qul'), 3MS ('şâ'e', 'le-hedâkum' — söz içi, gönderge 'lillâhi' 2. kelime), muhatap 2MP ('le-hedâkum' eki — söz içi); "
 "6:150 muhatap 2MS ('qul', 'teşhed'; 16. kelime), muhatap 2MP ('helumme', 'şuhedâ'akum' — söz içi), 3MP ('yeşhedûne' — söz içi, 'şehidû', 'ma'ahum' eki — gönderge 'llezîne' 4. kelime; 'kezzebû' — gönderge 'llezîne' 18. kelime; 'yu'minûne', 'hum', 'bi-rabbihim' eki, 'ya'dilûn' — gönderge 'llezîne' 21. kelime), 3MS ('harrame' — söz içi, gönderge 'llâhe' 7. kelime), konuşan 1P ('âyâtinâ' eki)",
 "6:148-150 gönderge zinciri: 6:148 'llezîne eşrakû' (2-3. kelime) söz aktarımının öznesi; 6:149 ve 6:150 'qul' (1. kelime) muhatabı nebi; 6:150 'şehidû' 3MP öznesi 4. kelimedeki şahitlere, 'yu'minûne' ve 'ya'dilûn' öznesi 21. kelimedeki topluluğa bağlanır (okuma)",
 "edilgen: blokta edilgen fiil yok (ölçüm EDİLGEN alanı yok)",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:148 'se-yeqûlu' (1.) ardından söz 4-14. kelime — 'şey'' (14.) ile kapanır, 'kezâlike' (15.) ile anlatı; 'qul' (23.) ardından söz 24-37. kelime — ayet sonuna kadar; 6:149 'qul' (1.) ardından söz 2-8. kelime — ayet sonuna kadar; "
 "6:150 'qul' (1.) ardından söz 2-9. kelime — 'hâzâ' (9.) ile kapanır, 'fe-in' (10.) morph REM ile muhatap 2MS'ye dönüş; mealde 'De ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 148 150 36' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; REM sapması 6:149 (5. kelime) — 'fe-lev' söz içinde istînâf, muhatap 2MP sürer, söz 8. kelimeye dek sürer; "
 "morph 've' konumlarıyla kontrol edildi: 6:148 've lâ' (9.), 've lâ' (11.), 've in' (34.) CONJ; 6:150 've lâ' (15.), 've'llezîne' (21.) CONJ, 've hum' (25.) REM; "
 "'fe' konumları: 6:148 'fe-tuxricûhu' (28.) CAUS; 6:149 'fe-lillâhi' (2.) SUP, 'fe-lev' (5.) REM; 6:150 'fe-in' (10.) REM, 'fe-lâ' (12.) RSLT",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:148-150 ◈K / ◈B tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 148 150 36'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:148 (16:35); 6:149 (16:9); 6:150 bağ yok; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11); medde sayımının basılmış eşi (yazım farkı ile, D3 dışı): 'say 6:148 5-7 --medde' 6:137; 'say 6:148 6-7 --medde' 5:76, 6:71, 6:137, 10:106",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:148 söz açılır (4. kelime), söz kapanır (14. kelime, ayet içi), söz açılır (24. kelime), söz kapanır (37. kelime, ayet içi), şart → cevap (ayet içi; COND 'lev' 4. kelime), muhatap geçişi 2MS → 2MP (ayet içi), şahıs geçişi 3 → 2 (beraberlik), edim geçişi emir, şart → soru, emir, şart; "
 "6:149 söz açılır (2. kelime), söz kapanır (8. kelime, ayet içi), şart → cevap (ayet içi; COND 'lev' 5. kelime), muhatap geçişi 2MS → 2MP (ayet içi), şahıs geçişi 2 → 3 (beraberlik), edim geçişi soru, emir, şart → emir, şart; "
 "6:150 söz açılır (2. kelime), söz kapanır (9. kelime, ayet içi), şart → cevap (ayet içi; COND 'in' 10. kelime), muhatap geçişi 2MP → 2MS (ayet içi), şahıs geçişi yok, edim geçişi emir, şart → emir, yasak, şart; bölüm kapanışı; "
 "ölçüm iltifât 6:148-150 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:148 'lev şâ'e'llâhu mâ eşraknâ' — şart ve cevap (morph COND + NEG); 6:148 'in tettebi'ûne illa'z-zanne' — olumsuzluk ve istisna ile hasr (morph NEG + EXP); 6:148 'hattâ zâqû be'senâ' — gaye edatı (morph INC); "
 "6:149 'le-hedâkum' — cevap lâmı (morph EMPH); 6:150 'fe-in şehidû fe-lâ teşhed' — şart ve cevap bağlacı (morph COND + RSLT)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:148 11-12. kelime — 16:35 ile harekesiz eş (sayım: 'say 6:148 11-12'); 6:149 6-8. kelime — 16:9 ile harekesiz eş (sayım: 'say 6:149 6-8'); "
 "6:150 26-27. kelime — 6:1 ile harekesiz eş (sayım: 'say 6:150 26-27'); 6:148 kök شرك, شيأ, قول ikilemeleri; 6:150 kök شهد ikilemesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 36'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'llezîne eşrakû' 6:148 'Ortak koşanlar' / 16:35 'Ortak koşanlar' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ve lâ harramnâ' 6:148 'haram kılmazdık' / 16:35 'haram kılmazdık' (emsal metninde) — çakışma değil (bayt eşit); "
 "'şâ'e le-hedâkum ecma'în' 6:149 'Dileseydi hepinizi doğru yola iletirdi' / 16:9 'Dileseydi hepinizi doğru yola iletirdi' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:148 'yeqûlu' IMPF IND ('se' ile) — meal 'diyecekler'; 'eşrakû' PERF — meal 'koşanlar'; 'şâ'e' PERF (şart) — meal 'dileseydi'; 'eşraknâ' PERF ('mâ' ile) — meal 'koşardık'; 'harramnâ' PERF ('lâ' ile) — meal 'kılmazdık'; 'kezzebe' PERF — meal 'yalanladılar'; 'zâqû' PERF ('hattâ' ile) — meal 'tadıncaya'; "
 "'qul' IMPV — meal 'De'; 'tuxricû' IMPF SUBJ ('fe' ile) — meal 'çıkaracağınız'; 'tettebi'ûne' IMPF IND — meal 'uyuyorsunuz'; 'taxrusûn' IMPF IND — meal 'bulunuyorsunuz'; "
 "6:149 'qul' IMPV — meal 'De'; 'şâ'e' PERF (şart) — meal 'Dileseydi'; 'hedâ' PERF ('le' ile) — meal 'iletirdi'; "
 "6:150 'qul' IMPV — meal 'De'; 'helumme' IMPV (fiil ismi) — meal 'getirin'; 'yeşhedûne' IMPF IND — meal 'eden'; 'harrame' PERF — meal 'kıldığına'; 'şehidû' PERF (şart) — meal 'ederlerse'; 'teşhed' IMPF JUS ('lâ' ile) — meal 'etme'; 'tettebi'' IMPF JUS ('lâ' ile) — meal 'uyma'; 'kezzebû' PERF — meal 'yalanlayanların'; 'yu'minûne' IMPF IND ('lâ' ile) — meal 'inanmayanların'; 'ya'dilûn' IMPF IND — meal 'tutuyorlar'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'eşrakû', 'kezzebû' PERF 6:148 ve 6:150'de sıfat-fiil ('-anlar', '-anların') ile; 'şâ'e', 'eşraknâ', 'harramnâ' PERF 6:148'de şart / cevap kipi ('-seydi', '-ardık', '-mazdık') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'him' ('Onlardan' / 'onlara') — çakışma değil (ad çekimi); 'illâ' ('ancak' / 'dışında') — çakışma değil (hasr / istisna)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 148 150 36'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:148, 6:149 ve 6:150 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:148 (''ilmin' / 'z-zanne'); 6:149 ve 6:150 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök شيأ 6:148 ('şâ'e') ve 6:149 ('şâ'e'); kök حرم 6:148 ('harramnâ') ve 6:150 ('harrame'); kök كذب 6:148 ('kezzebe') ve 6:150 ('kezzebû'); kök تبع 6:148 ('tettebi'ûne') ve 6:150 ('tettebi''); kök قول 6:148 ('qul'), 6:149 ('qul') ve 6:150 ('qul'); kök أله 6:148 ('llâhu'), 6:149 ('lillâhi') ve 6:150 ('llâhe'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 17-2 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 35 ve 36; bölüm kapanışı bu blokta; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b36/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 148 150 36'; lem_bozuk.py 36 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 148 150 → AYN_SONUC; sunum/bolum4_kurallar.py 148 150 36 → KHATA_HEPSI; sunum/bolum5_kurallar.py 148 150 36 → B5_HEPSI; sunum/bolum6_kurallar.py 148 150 36 → B6_HEPSI; sunum/bolum7_kurallar.py 148 150 36 → B7_HEPSI; sunum/bolum8_kurallar.py 148 150 36 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 148 150 36 → B9_HEPSI; sunum/bolum10_kurallar.py 148 150 36 → B10_HEPSI; sunum/bolum11_kurallar.py 148 150 36 → B11_HEPSI; sunum/bolum12_kurallar.py 148 150 36 → B12_HEPSI; sunum/bolum13_kurallar.py 148 150 36 → B13_HEPSI; sunum/bolum14_kurallar.py 148 150 36 → B14_HEPSI; sunum/bolum15_kurallar.py 148 150 36 → B15_HEPSI; sunum/bolum16_kurallar.py 148 150 36 → B16_HEPSI; sunum/bolum17_kurallar.py 148 150 36 → B17_HEPSI; sunum/bolum18_kurallar.py 148 150 36 → B18_HEPSI; sunum/bolum19_kurallar.py 148 150 36 → B19_HEPSI; sunum/bolum20_kurallar.py 148 150 36 → B20_HEPSI; sunum/bolum21_kurallar.py 148 150 36 → B21_HEPSI; sunum/bolum22_kurallar.py 148 150 36 → B22_HEPSI; sunum/bolum23_kurallar.py 148 150 36 → B23_HEPSI; sunum/bolum24_kurallar.py 148 150 36 → B24_HEPSI; sunum/bolum25_kurallar.py 148 150 36 → B25_HEPSI; sunum/bolum26_kurallar.py 148 150 36 → B26_HEPSI; sunum/bolum27_kurallar.py 148 150 36 → B27_HEPSI; sunum/bolum28_kurallar.py 148 150 36 → B28_HEPSI; sunum/bolum29_kurallar.py 148 150 36 → B29_HEPSI; sunum/bolum30_kurallar.py 148 150 36 → B30_HEPSI; sunum/bolum31_kurallar.py 148 150 36 → B31_HEPSI; sunum/bolum32_kurallar.py 148 150 36 → B32_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 36 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; 6:148 ölçüm xref'teki okunmuş 1 ayet harekesiz sayımla bulunmadı — emsal alınmadı; 6:116 ve 10:66 önceden basılmış; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('qâle', 'ellezî', 'eşrake', 'lev', 'şâ'e', 'allâh', 'mâ', 'lâ', 'âbâ'', 'harrame', 'min', 'in', 'ittebe', 'illâ', 'zann', 'hedâ', 'ecma'', 'âmene', 'âxir', 'kezzebe', 'âye', 'ehvâ''); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (148, 150): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_148_150.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b34k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '148', '150'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '148', '150', '36'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '148', '150', '36'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '148', '150', '36', '--tazelik-yok')}
    for _n in range(7, 33): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '148', '150', '36')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32 = [_R['B%d' % _n].splitlines() for _n in range(6, 33)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
