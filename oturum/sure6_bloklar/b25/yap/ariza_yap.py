# sûre 6 blok 25 (6:104-108) ARIZA oluşturucu — bölüm 13-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b25/olcum.txt'
os.environ['SAY2'] = '/home/claude/b25/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b24.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {}
BOL = "'Basiretler; yeminleri ve şeytanlar'"


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
 ("6:106", "'rabb lâ ilâh illâ _'", 2, 'say 6:106 6-10', "harekesiz 'rabbike lâ ilâhe illâ huve' (6-10. kelime)", ('dizi 6 106 6 10', 'rabb lâ ilâh illâ _', '6-10', "biçim farkı (dizi 6 106 6 10): 6:102 i'râb, zamir eki")),
 ("6:107", "'lev şâ'e allâh mâ'", 2, 'say 6:107 1-4', "harekesiz 've lev şâ'e'llâhu mâ' (1-4. kelime); biçim öğesi 'lev' öneki (lemma dizisi sûre içi 3, nakarat3 2)", ('dizi 6 107 1 4', "lev şâ'e allâh mâ", '1-4', 'biçim farkı (dizi 6 107 1 4): basılmamış eş yazım eş; basılmamış eş önek; öneksiz eş koşusu (dizi 6 107 1 4): basılmamış eş → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 2')),
 ("6:107", "'şâ'e allâh mâ eşrake'", 2, 'say 6:107 2-5', "harekesiz 'şâ'e'llâhu mâ eşrakû' (2-5. kelime)", ('dizi 6 107 2 5', "şâ'e allâh mâ eşrake", '2-5', 'biçim farkı (dizi 6 107 2 5): basılmamış eş fiil çekimi, zamir eki')),
 ("6:107", "'şâ'e allâh mâ'", 3, 'say 6:107 2-4', "harekesiz 'şâ'e'llâhu mâ' (2-4. kelime)", ('dizi 6 107 2 4', "şâ'e allâh mâ", '2-4', 'biçim farkı (dizi 6 107 2 4): basılmamış eş yazım eş; basılmamış eş yazım eş')),
 ("6:108", "'summe ilâ rabb merci' nebbe'e mâ kâne'", 2, 'say 6:108 18-24', "harekesiz 'summe ilâ rabbihim merci'uhum fe-yunebbi'uhum bi-mâ kânû' (18-24. kelime)", ('dizi 6 108 18 24', "summe ilâ rabb merci' nebbe'e mâ kâne", '18-24', 'biçim farkı (dizi 6 108 18 24): basılmamış eş fiil çekimi, zamir eki')),
 ("6:108", "'ellezî de'â min dûn allâh'", 2, 'say 6:108 3-7', "harekesiz 'llezîne yed'ûne min dûni'llâh' (3-7. kelime)", ('dizi 6 108 3 7', "ellezî de'â min dûn allâh", '3-7', 'biçim farkı (dizi 6 108 3 7): 6:56 fiil çekimi, zamir eki')),
 ("6:108", "'de'â min dûn allâh'", 3, 'say 6:108 4-7', "harekesiz 'yed'ûne min dûni'llâh' (4-7. kelime)", ('dizi 6 108 4 7', "de'â min dûn allâh", '4-7', 'biçim farkı (dizi 6 108 4 7): 6:56 fiil çekimi, zamir eki; 6:71 fiil çekimi, zamir eki, önek')),
 ("6:108", "'nebbe'e mâ kâne 'amile'", 2, 'say 6:108 22-25', "harekesiz 'fe-yunebbi'uhum bi-mâ kânû ya'melûn' (22-25. kelime)", ('dizi 6 108 22 25', "nebbe'e mâ kâne 'amile", '22-25', 'biçim farkı (dizi 6 108 22 25): 6:60 fiil çekimi, zamir eki, önek')),
 ("6:108", "'min dûn allâh'", 4, 'say 6:108 5-7', "harekesiz 'min dûni'llâh' (5-7. kelime)", None),
 ("6:108", "'nebbe'e mâ kâne'", 4, 'say 6:108 22-24', "harekesiz 'fe-yunebbi'uhum bi-mâ kânû' (22-24. kelime)", ('dizi 6 108 22 24', "nebbe'e mâ kâne", '22-24', 'biçim farkı (dizi 6 108 22 24): 6:60 fiil çekimi, zamir eki, önek; basılmamış eş önek; basılmamış eş fiil çekimi, zamir eki')),
 ("6:108", "'summe ilâ rabb'", 3, 'say 6:108 18-20', "harekesiz 'summe ilâ rabbihim' (18-20. kelime)", ('dizi 6 108 18 20', 'summe ilâ rabb', '18-20', 'biçim farkı (dizi 6 108 18 20): 6:38 yazım eş; basılmamış eş zamir eki')),
 ("6:108", "'bi-mâ kâne 'amile'", 3, 'say 6:108 23-25', "harekesiz 'bi-mâ kânû ya'melûn' (23-25. kelime); biçim öğesi 'kâne' çekimi (lemma dizisi sûre içi 6, nakarat3 3)", ('dizi 6 108 23 25', "mâ kâne 'amile", '23-25', 'biçim farkı (dizi 6 108 23 25): 6:43 önek; 6:60 fiil çekimi, zamir eki; 6:88 önek; basılmamış eş önek; basılmamış eş yazım eş; öneksiz eş koşusu (dizi 6 108 23 25): 6:43 → önek kesilmiş sûre içi 5; 6:60 → önek kesilmiş sûre içi 1; 6:88 → önek kesilmiş sûre içi 5; basılmamış eş → önek kesilmiş sûre içi 5; basılmamış eş → önek kesilmiş sûre içi 2')),
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

VF_YAZI = {104: {9: "'ve men'", 12: "'ve mâ'"}, 105: {1: "'ve kezâlike'", 4: "'ve li-yeqûlû'", 6: "'ve li-nubeyyinehû'"}, 106: {11: "'ve a'rid'"}, 107: {1: "'ve lev'", 6: "'ve mâ'", 10: "'ve mâ'"}, 108: {1: "'ve lâ'"}}
sys.path.insert(0, '/home/claude/b25/yap')
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
open('/home/claude/b25/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '25')
BLOKLAR = [str(i) for i in range(1, 26)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '25', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b25/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '104', '108', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b25/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b25/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '104', '108', '25').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_104_108.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:104', '6:105', '6:106', '6:107', '6:108'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_104_108.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(104, 109))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:104 kök نفس ('fe-li-nefsihî' 8. kelime — can / kendi); 6:106 kök عرض ('ve a'rid' 11. kelime — yüz çevirme): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '104', '108', '25')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b25/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 26)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(104, 109))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 12 kapanışında sunum/bolum28_kurallar.py eklendi (kural 1-5), sunum/bolum19_kurallar.py KURAL_ATIF bölüm 12, sunum/geriye_donuk.py bolum28 satırı, sunum/mutasyon_sina.py b28 sınamaları — bu blokta araç değişikliği yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 249",
 "geriye dönük koşu (bölüm 12 kapanışı, komut 'python3 sunum/geriye_donuk.py b24k yamalar/geriye_donuk_6_b24.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 104 108 25'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:104 've mâ ene 'aleykum bi-hafîz' (12-15. kelime) ve 6:107 've mâ ce'alnâke 'aleyhim hafîz' (6-9. kelime), 've mâ ente 'aleyhim bi-vekîl' (10-13. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge) (yamalar/esma_el_6_104_108.txt); وَكِيل lemmasında 6:66:9 'degil' ve 6:102:16 'ilahi' kayıtlarıyla karar ayrılığı: gönderge ayrılığı (6:66:9 ve 6:107:13 elçi, 6:102:16 Allah); 6:105, 6:106 ve 6:108 esmâ yok; "
 "6:107 lafız (3. kelime), 6:108 lafız (7. ve 9. kelime); 6:104 Rab (5. kelime), 6:106 Rab (6. kelime), 6:108 Rab (20. kelime); 6:105 lafız ve Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 104 108 25'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 6:104 ve 6:107 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı (muhur_el hayır, ölçümle uyuşuyor)): " + EMH,
 "ölçüm: 6:104 '{{1|fâsıla بحفيظ → ظ, ظ sınıfı}}', '{{1|simetri \\[3, 4, 9, 1\\]}}', '{{1|harf 65 → harf3 59, isaret 6}}' ve '{{1|dış düğüm 0}}'; "
 "6:105 '{{2|fâsıla يعلمون → ن, N sınıfı}}', '{{2|harf 47 → harf3 44, isaret 3}}' ve '{{2|dış düğüm 1}}'; "
 "6:106 '{{3|EDİLGEN 1/3 fiil, pas z=1,57}}', '{{3|fâsıla ٱلمشركين → ن, N sınıfı}}', '{{3|simetri \\[4, 2, 7, 1\\]}}', '{{3|harf 46 → harf3 44, isaret 2}}' ve '{{3|dış düğüm 2}}'; "
 "6:107 '{{4|fâsıla بوكيل → ل, ل sınıfı — KAFİYE KIRILMASI}}', '{{4|simetri \\[3, 4, 8, 1\\]}}', '{{4|harf 57 → harf3 52, isaret 5}}' ve '{{4|dış düğüm 0}}'; "
 "6:108 '{{5|fâsıla يعملون → ن, N sınıfı}}', '{{5|harf 109 → harf3 103, isaret 6}}', '{{5|dış düğüm 1}}' ve '{{5|İÇ düğüm 1}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 104 108 25'): KALAN_P",
 "ölçüm aktör: 6:104, 6:105, 6:106, 6:107 ve 6:108 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:104 şart — CERT 1 'qad' (1.), COND 2 'fe-men' (6.), 've men' (9.), NEG 1 've mâ' (12.); 6:105 haber — kip yok; "
 "6:106 emir — IMPV 2 (1., 11.), NEG 1 'lâ' (7.), biçim ISTISNA ('illâ' 9.); 6:107 şart — COND 1 've lev' (1.), NEG 3 (4., 6., 10.); 6:108 yasak — PRO 1 've lâ' (1.), biçim NEHY; "
 "morph RSLT ('fe' 6:104 8., 11.), PRP ('li' 6:105 4., 6.), EXP ('illâ' 6:106 9.), CAUS ('fe' 6:108 8.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:106 ★ (kaynak pas, z=1,57); 6:107 ★ (kaynak allah, z=1,01; kafiye kırığı); 6:104, 6:105 ve 6:108 yıldız yok",
 "fâsıla: 6:103 ر → 6:104 ظ (بحفيظ) → 6:105 ن (يعلمون) → 6:106 ن (ٱلمشركين) → 6:107 ل (بوكيل — KAFİYE KIRILMASI) → 6:108 ن (يعملون) — ظ, N ve ل sınıfları (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:104 xref yok; 6:105 okunmuş 1 ayet; 6:106 33:2 (emsal olarak basıldı) ve okunmamış 1 ayet; 6:107 xref yok; 6:108 39:7 (emsal olarak basıldı) ve okunmamış 1 ayet (sûre içi 1)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:104 ve 6:105 nakarat3 yok; 6:106 'rabb lâ ilâh illâ _' süzgeç GEÇER; 6:107 'lev şâ'e allâh mâ', 'şâ'e allâh mâ eşrake' ve 'şâ'e allâh mâ' süzgeç GEÇER; 6:108 'summe ilâ rabb merci' nebbe'e mâ kâne', 'ellezî de'â min dûn allâh', 'de'â min dûn allâh', 'nebbe'e mâ kâne 'amile', 'min dûn allâh', 'nebbe'e mâ kâne', 'summe ilâ rabb' ve 'bi-mâ kâne 'amile' süzgeç GEÇER",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:104 3MS ('câ'ekum' — fiil uyumu, fail 3. kelime; 'ebsara', 'fe-li-nefsihî' eki — gönderge 'fe-men' 6. kelime; ''amiye' — gönderge 've men' 9. kelime), muhatap 2MP, 3FS (''aleyhâ' — gönderge 'fe-li-nefsihî' 8. kelime), konuşan 1S ('ene'); "
 "6:105 konuşan 1P ('nusarrifu', 've li-nubeyyinehû'), 3MP ('ve li-yeqûlû' — tartışmalı; 'ya'lemûn' — gönderge 'li-qavmin' 7. kelime), muhatap 2MS ('derasta' — söz içi), 3MS ('ve li-nubeyyinehû' eki — gönderge 'l-âyâti' 3. kelime, tartışmalı); "
 "6:106 muhatap 2MS ('ttebi', 'ileyke', 'rabbike', 've a'rid'), 3MS ('ûhiye' — fiil uyumu, edilgen; 'huve' — gönderge 'rabbike' 6. kelime); "
 "6:107 3MS ('şâ'e' — fiil uyumu, fail 3. kelime), 3MP ('eşrakû', ''aleyhim', ''aleyhim' — gönderge 6:106 13. kelime), konuşan 1P, muhatap 2MS ('ente'); "
 "6:108 muhatap 2MP ('tesubbu'), 3MP ('yed'ûne', 'fe-yesubbu' — gönderge 6:107 5. kelime; ''amelehum', 'rabbihim', 'merci'uhum', 'fe-yunebbi'uhum', 'kânû', 'ya'melûn' — gönderge 'ummetin' 16. kelime, tartışmalı), konuşan 1P ('zeyyennâ'), 3MS ('fe-yunebbi'uhum' — gönderge 'rabbihim' 20. kelime) — betik denetimi: KHATA_ADSIZ; "
 "edilgen: 6:106 'ûhiye' (3. kelime; naib-i faili 'mâ' 2. kelime) — ölçüm EDİLGEN 1/3 bu kelimeden",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:105 've li-yeqûlû' (4.) ardından söz 5. kelime ('derasta') — ayet içi kapanış; 6:104, 6:106, 6:107 ve 6:108 söz yok — söz fiili yok (okuma); mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 104 108 25' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:104 've men' (9.) CONJ, 've mâ' (12.) REM; 6:105 've kezâlike' (1.), 've li-yeqûlû' (4.), 've li-nubeyyinehû' (6.) CONJ; 6:106 've a'rid' (11.) CONJ; 6:107 've lev' (1.) REM, 've mâ' (6. ve 10.) CONJ; 6:108 've lâ' (1.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:104 ◈B بصر ('besâ'iru' 3. kelime — B3)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 104 108 25'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:106 (33:2); 6:108 (39:7); 6:104, 6:105 ve 6:107 bağ yok; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:104 şahıs geçişi yok, edim geçişi haber → şart, şart → cevap ('men' 6. ve 9. kelime), bölüm açılışı; 6:105 söz açılır / kapanır (5. kelime), şahıs geçişi yok, edim geçişi şart → haber; 6:106 şahıs geçişi 3 → 2, edim geçişi haber → emir; "
 "6:107 şahıs geçişi 2 → 3, edim geçişi emir → şart, şart → cevap ('lev' 1. kelime); 6:108 şahıs geçişi yok, edim geçişi şart → yasak, nehy → cevap ('fe-yesubbu' 8. kelime); "
 "ölçüm iltifât 6:104-108 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:104 'qad câ'ekum' — tahkik (morph CERT); 'fe-men ebsara fe-li-nefsihî' — şart ve cevap (morph REM + COND, cevapta RSLT); "
 "6:105 've li-yeqûlû derasta' — amaç lâmı ve söz (morph CONJ + PRP); 6:106 'lâ ilâhe illâ huve' — cins nefyi ve istisna (morph NEG + EXP); "
 "6:107 've lev şâ'e'llâhu mâ eşrakû' — 'lev' şartı ve cevabı (morph REM + COND); 6:108 've lâ tesubbu' — nehy (morph REM + PRO); 'fe-yesubbu'llâhe' — sebep / sonuç fâsı (morph CAUS)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:106 1-6. kelime — 33:2 ile lemma dizisi eşi (sayım: 'dizi 6 106 1 6'); "
 "6:108 'summe ilâ rabbihim merci'uhum fe-yunebbi'uhum bi-mâ kânû ya'melûn' — 39:7 ile lemma dizisi eşi (sayım: 'dizi 6 108 18 25'); 6:106 'rabbike lâ ilâhe illâ huve' — 6:102 ile lemma dizisi eşi ('dizi 6 106 6 10'); 6:104 kök بصر ikilemesi; 6:108 kök أله, سبب, عمل ikilemeleri",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 25'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'ileyke min rabbik' 6:106 'Rabbinden sana' / 33:2 'Rabbinden sana' (emsal metninde) — çakışma değil (bayt eşit); 'summe ilâ' 6:108 'Sonra' / 39:7 'Sonra' (emsal metninde) — çakışma değil (bayt eşit); geniş kalıp 33:2 ve 39:7 ile lemma dizisi düzeyinde (fiil çekimi / zamir eki farkı); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:104 'câ'e' PERF — meal 'geldi'; 'ebsara' PERF (şart) — meal 'görürse'; ''amiye' PERF (şart) — meal 'kör olursa'; "
 "6:105 'nusarrifu' IMPF IND — meal 'açıklıyoruz'; 'yeqûlû' IMPF SUBJ — meal 'desinler'; 'derasta' PERF — meal 'ders almışsın'; 'nubeyyine' IMPF SUBJ — meal 'açıklayalım'; 'ya'lemûn' IMPF IND — meal 'bilen'; "
 "6:106 'ttebi' IMPV — meal 'uy'; 'ûhiye' PERF PASS — meal 'vahyolunan'; 'a'rid' IMPV — meal 'yüz çevir'; 6:107 'şâ'e' PERF (şart) — meal 'dileseydi'; 'eşrakû' PERF — meal 'koşmazlardı'; 'ce'alnâ' PERF — meal 'kılmadık'; "
 "6:108 'tesubbu' IMPF JUS ('lâ' ile) — meal 'sövmeyin'; 'yed'ûne' IMPF IND — meal 'dua ettiklerine'; 'yesubbu' IMPF SUBJ — meal 'söverler'; 'zeyyennâ' PERF — meal 'süsledik'; 'yunebbi'u' IMPF IND — meal 'haber verecektir'; 'kânû' PERF — meal 'olduklarını'; 'ya'melûn' IMPF IND — meal 'yapmakta'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 104 108 25'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:104, 6:105, 6:106, 6:107 ve 6:108 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:104 ('ebsara' / ''amiye'); 6:105, 6:106, 6:107 ve 6:108 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök ربب 6:104 ('rabbikum'), 6:106 ('rabbike') ve 6:108 ('rabbihim'); kök حفظ 6:104 ('bi-hafîz') ve 6:107 ('hafîzan'); kök علم 6:105 ('ya'lemûn') ve 6:108 (''ilmin'); kök أله 6:106 ('ilâhe'), 6:107 ('llâhu') ve 6:108 ('llâhi', 'llâhe'); kök شرك 6:106 ('l-muşrikîn') ve 6:107 ('eşrakû'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 13-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 25 ve 26; bu blok bölümü açıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b25/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 104 108 25'; lem_bozuk.py 25 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 104 108 → AYN_SONUC; sunum/bolum4_kurallar.py 104 108 25 → KHATA_HEPSI; sunum/bolum5_kurallar.py 104 108 25 → B5_HEPSI; sunum/bolum6_kurallar.py 104 108 25 → B6_HEPSI; sunum/bolum7_kurallar.py 104 108 25 → B7_HEPSI; sunum/bolum8_kurallar.py 104 108 25 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 104 108 25 → B9_HEPSI; sunum/bolum10_kurallar.py 104 108 25 → B10_HEPSI; sunum/bolum11_kurallar.py 104 108 25 → B11_HEPSI; sunum/bolum12_kurallar.py 104 108 25 → B12_HEPSI; sunum/bolum13_kurallar.py 104 108 25 → B13_HEPSI; sunum/bolum14_kurallar.py 104 108 25 → B14_HEPSI; sunum/bolum15_kurallar.py 104 108 25 → B15_HEPSI; sunum/bolum16_kurallar.py 104 108 25 → B16_HEPSI; sunum/bolum17_kurallar.py 104 108 25 → B17_HEPSI; sunum/bolum18_kurallar.py 104 108 25 → B18_HEPSI; sunum/bolum19_kurallar.py 104 108 25 → B19_HEPSI; sunum/bolum20_kurallar.py 104 108 25 → B20_HEPSI; sunum/bolum21_kurallar.py 104 108 25 → B21_HEPSI; sunum/bolum22_kurallar.py 104 108 25 → B22_HEPSI; sunum/bolum23_kurallar.py 104 108 25 → B23_HEPSI; sunum/bolum24_kurallar.py 104 108 25 → B24_HEPSI; sunum/bolum25_kurallar.py 104 108 25 → B25_HEPSI; sunum/bolum26_kurallar.py 104 108 25 → B26_HEPSI; sunum/bolum27_kurallar.py 104 108 25 → B27_HEPSI; sunum/bolum28_kurallar.py 104 108 25 → B28_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 25 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('ittebe', 'mâ', 'evhâ', 'ilâ', 'min', 'rabb', 'lâ', 'ilâh', 'illâ', 'lev', 'şâ'e', 'allâh', 'eşrake', 'summe', 'merci'', 'nebbe'e', 'kâne', ''amile', 'ellezî', 'de'â', 'dûn'); joker '_' lemmasız öğede ('dizi 6 106 6 10' — 'huve'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (104, 108): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_104_108.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b24k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '104', '108'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '104', '108', '25'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '104', '108', '25'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '104', '108', '25', '--tazelik-yok')}
    for _n in range(7, 29): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '104', '108', '25')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28 = [_R['B%d' % _n].splitlines() for _n in range(6, 29)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
