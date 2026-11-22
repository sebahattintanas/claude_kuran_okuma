# sûre 6 blok 28 (6:118-121) ARIZA oluşturucu — bölüm 14-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b28/olcum.txt'
os.environ['SAY2'] = '/home/claude/b28/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Hakem olarak Allah; üzerine Allah'ın adı anılan'"


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
 ("6:118", "'ekele mimmâ zekere ism allâh 'alâ'", 2, 'say 6:118 1-6', "harekesiz 'fe-kulû mimmâ zukira'smu'llâhi 'aleyhi' (1-6. kelime)", ('dizi 6 118 1 6', "ekele mimmâ zekere ism allâh 'alâ", '1-6', 'biçim farkı (dizi 6 118 1 6): 6:119 önek')),
 ("6:118", "'zekere ism allâh 'alâ'", 3, 'say 6:118 3-6', "harekesiz 'zukira'smu'llâhi 'aleyhi' (3-6. kelime); biçim öğesi ''alâ' zamir eki (lemma dizisi sûre içi 4, nakarat3 3)", ('dizi 6 118 3 6', "zekere ism allâh 'alâ", '3-6', 'biçim farkı (dizi 6 118 3 6): 6:119 yazım eş; 6:121 yazım eş; basılmamış eş elif yazımı, fiil çekimi, zamir eki; öneksiz eş koşusu (dizi 6 118 3 6): 6:119 → önek kesilmiş sûre içi 3; 6:121 → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 1')),
 ("6:118", "'zekere ism allâh'", 4, 'say 6:118 3-5', "harekesiz 'zukira'smu'llâh' (3-5. kelime)", ('dizi 6 118 3 5', "zekere ism allâh", '3-5', 'biçim farkı (dizi 6 118 3 5): 6:119 yazım eş; 6:121 yazım eş; basılmamış eş fiil çekimi, zamir eki')),
 ("6:119", "'ekele mimmâ zekere ism allâh 'alâ'", 2, 'say 6:119 4-9', "harekesiz 'te'kulû mimmâ zukira'smu'llâhi 'aleyhi' (4-9. kelime)", ('dizi 6 119 4 9', "ekele mimmâ zekere ism allâh 'alâ", '4-9', 'biçim farkı (dizi 6 119 4 9): 6:118 önek')),
 ("6:119", "'zekere ism allâh 'alâ'", 3, 'say 6:119 6-9', "harekesiz 'zukira'smu'llâhi 'aleyhi' (6-9. kelime); biçim öğesi ''alâ' zamir eki (lemma dizisi sûre içi 4, nakarat3 3)", ('dizi 6 119 6 9', "zekere ism allâh 'alâ", '6-9', 'biçim farkı (dizi 6 119 6 9): 6:118 yazım eş; 6:121 yazım eş; basılmamış eş elif yazımı, fiil çekimi, zamir eki; öneksiz eş koşusu (dizi 6 119 6 9): 6:118 → önek kesilmiş sûre içi 3; 6:121 → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 1')),
 ("6:119", "'inne rabb _ a'lem'", 2, 'say 6:119 26-29', "harekesiz 'inne rabbeke huve a'lemu' (26-29. kelime)", None),
 ("6:119", "'zekere ism allâh'", 4, 'say 6:119 6-8', "harekesiz 'zukira'smu'llâh' (6-8. kelime)", ('dizi 6 119 6 8', "zekere ism allâh", '6-8', 'biçim farkı (dizi 6 119 6 8): 6:118 yazım eş; 6:121 yazım eş; basılmamış eş fiil çekimi, zamir eki')),
 ("6:119", "'ğayr 'ilm inne'", 2, 'say 6:119 24-26', "harekesiz 'bi-ğayri 'ilmin inne' (24-26. kelime)", None),
 ("6:120", "'cezâ bi-mâ kâne'", 2, 'say 6:120 9-11', "harekesiz 'se-yuczevne bi-mâ kânû' (9-11. kelime)", ('dizi 6 120 9 11', 'cezâ mâ kâne', '9-11', 'biçim farkı (dizi 6 120 9 11): basılmamış eş fiil çekimi')),
 ("6:121", "'zekere ism allâh 'alâ'", 3, 'say 6:121 5-8', "harekesiz 'yuzkeri'smu'llâhi 'aleyhi' (5-8. kelime); biçim öğesi ''alâ' zamir eki (lemma dizisi sûre içi 4, nakarat3 3)", ('dizi 6 121 5 8', "zekere ism allâh 'alâ", '5-8', 'biçim farkı (dizi 6 121 5 8): 6:118 yazım eş; 6:119 yazım eş; basılmamış eş elif yazımı, fiil çekimi, zamir eki; öneksiz eş koşusu (dizi 6 121 5 8): 6:118 → önek kesilmiş sûre içi 3; 6:119 → önek kesilmiş sûre içi 3; basılmamış eş → önek kesilmiş sûre içi 1')),
 ("6:121", "'zekere ism allâh'", 4, 'say 6:121 5-7', "harekesiz 'yuzkeri'smu'llâh' (5-7. kelime)", ('dizi 6 121 5 7', "zekere ism allâh", '5-7', 'biçim farkı (dizi 6 121 5 7): 6:118 yazım eş; 6:119 yazım eş; basılmamış eş fiil çekimi, zamir eki')),
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

VF_YAZI = {119: {1: "'ve mâ'", 10: "'ve qad'", 20: "'ve inne'"}, 120: {1: "'ve zerû'", 4: "'ve bâtinahû'"}, 121: {1: "'ve lâ'", 9: "'ve innehû'", 11: "'ve inne'", 17: "'ve in'"}}
sys.path.insert(0, '/home/claude/b28/yap')
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
open('/home/claude/b28/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '28')
BLOKLAR = [str(i) for i in range(1, 29)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '28', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b28/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '118', '121', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b28/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b28/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '118', '121', '28').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_118_121.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:118', '6:119', '6:120', '6:121'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_118_121.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(118, 122))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:120 kök ظهر ('zâhira' 2. kelime — açık, esmâ dışı), kök بطن ('ve bâtinahû' 4. kelime — gizli, esmâ dışı); 6:121 kök ولي ('evliyâ'ihim' 15. kelime — dost): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '118', '121', '28')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b28/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 29)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(118, 122))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 13 kapanışında sunum/bolum29_kurallar.py eklendi (kural 1-5), sunum/bolum19_kurallar.py KURAL_ATIF bölüm 13, sunum/geriye_donuk.py bolum29 satırı, sunum/mutasyon_sina.py b29 sınamaları — bu blokta araç değişikliği yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 269",
 "geriye dönük koşu (bölüm 13 kapanışı, komut 'python3 sunum/geriye_donuk.py b26k yamalar/geriye_donuk_6_b24k.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 118 121 28'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:118 'in kuntum bi-âyâtihî mu'minîn' (7-10. kelime) — esma_el 'degil', kural 'çoğul insan göndergeli' (insan topluluğu) (yamalar/esma_el_6_118_121.txt); "
 "6:120 've zerû zâhira'l-ismi ve bâtinahû' (1-4. kelime) ve 6:121 'ilâ evliyâ'ihim' (14-15. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge) (yamalar/esma_el_6_118_121.txt); مُؤْمِن ve وَلِيّ lemmalarında önceki kayıtlarla karar eş ('degil'); 6:119 esmâ yok; "
 "6:118 lafız (5. kelime), 6:119 lafız (8. kelime), 6:121 lafız (7. kelime); 6:119 Rab (27. kelime); 6:120 lafız ve Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 118 121 28'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 6:118, 6:120 ve 6:121 muhur EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, araç tanımı farkı (muhur_el hayır, ölçümle uyuşuyor)): " + EMH,
 "ölçüm: 6:118 '{{1|esmâ مُؤْمِن 10\\. sırada, SON konum, MÜHÜRSÜZ}}', '{{1|EDİLGEN 1/3 fiil, pas z=1,57}}', '{{1|fâsıla مؤمنين → ن, N sınıfı}}', '{{1|harf 42 → harf3 40, isaret 2}}', '{{1|dış düğüm 6}}' ve '{{1|İÇ düğüm 3}}'; "
 "6:119 '{{2|EDİLGEN 2/6 fiil, pas z=1,57}}', '{{2|sayı işareti كَثِير}}', '{{2|fâsıla بٱلمعتدين → ن, N sınıfı}}', '{{2|simetri \\[6, 1, 15, 2\\]}}', '{{2|harf 120 → harf3 116, isaret 4}}', '{{2|dış düğüm 7}}' ve '{{2|İÇ düğüm 3}}'; "
 "6:120 '{{3|esmâ ظاهِر 2\\. sırada, ORTA konum, MÜHÜRSÜZ \\| باطِن 4\\. sırada, ORTA konum, MÜHÜRSÜZ}}', '{{3|EDİLGEN 1/5 fiil, pas z=0,81}}', '{{3|fâsıla يقترفون → ن, N sınıfı}}', '{{3|simetri \\[3, 3, 8, 1\\]}}', '{{3|harf 62 → harf3 58, isaret 4}}' ve '{{3|dış düğüm 0}}'; "
 "6:121 '{{4|esmâ وَلِيّ 15\\. sırada, ORTA konum, MÜHÜRSÜZ}}', '{{4|EDİLGEN 1/5 fiil, pas z=0,81}}', '{{4|fâsıla لمشركون → ن, N sınıfı}}', '{{4|simetri \\[3, 1, 9, 1\\]}}', '{{4|harf 99 → harf3 94, isaret 5}}', '{{4|dış düğüm 5}}' ve '{{4|İÇ düğüm 3}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 118 121 28'): KALAN_P",
 "ölçüm aktör: 6:121 '{{4|aktör: adlı شَيْطان 12\\. sırada \\(gayb, rol meful\\)}}'; 6:118, 6:119 ve 6:120 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:118 emir, şart — COND 1 'in' (7.), IMPV 1 'fe-kulû' (1.); 6:119 soru — CERT 1 'qad' (10.), EMPH 1 'le-yudillûne' (22.), INTG 1 'mâ' (1.), NEG 1 'ellâ' (3.), biçim ISTISNA ('illâ' 16.); "
 "6:120 emir — FUT 1 'se-yuczevne' (9.), IMPV 1 've zerû' (1.); 6:121 yasak, şart — COND 1 'in' (17.), EMPH 3 (10., 13., 20.), NEG 1 'lem' (4.), PRO 1 'lâ' (1.), biçim NEHY; "
 "morph SUB ('en' 6:119 3.), PRP ('li' 6:121 16.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:118 ★ (kaynak pas, z=1,57); 6:119 ★ (kaynak n, z=1,87; eşiği geçen öbür ölçüler pas z=1,57); 6:120 ve 6:121 yıldız yok",
 "fâsıla: 6:117 ن → 6:118 ن (مؤمنين) → 6:119 ن (بٱلمعتدين) → 6:120 ن (يقترفون) → 6:121 ن (لمشركون) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:118 6:119 (basılmış), 6:121 (basılmış) ve okunmuş 6 ayet ve okunmamış 1 ayet (sûre içi 1); 6:119 53:30 (emsal olarak basıldı), 6:118 (basılmış), 6:121 (basılmış) ve okunmuş 6 ayet ve okunmamış 1 ayet (sûre içi 1); 6:120 xref yok; 6:121 6:118 (basılmış), 6:119 (basılmış) ve okunmuş 5 ayet ve okunmamış 1 ayet (sûre içi 1)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:118 'ekele mimmâ zekere ism allâh 'alâ', 'zekere ism allâh 'alâ' ve 'zekere ism allâh' süzgeç GEÇER; 6:119 'ekele mimmâ zekere ism allâh 'alâ', 'zekere ism allâh 'alâ', 'inne rabb _ a'lem' ve 'zekere ism allâh' süzgeç GEÇER, 'ğayr 'ilm inne' süzgeç GEÇMEZ; 6:120 'cezâ bi-mâ kâne' süzgeç GEÇMEZ; 6:121 'zekere ism allâh 'alâ' ve 'zekere ism allâh' süzgeç GEÇER",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:118 muhatap 2MP ('fe-kulû', 'kuntum'), 3MS ('zukira' — fiil uyumu, edilgen; ''aleyhi' eki — gönderge 'mimmâ' 2. kelime; 'bi-âyâtihî' eki — gönderge 'llâhi' 5. kelime); "
 "6:119 muhatap 2MP ('lekum', 'te'kulû', ''aleykum', 'dturirtum' — edilgen), 3MS ('zukira' — fiil uyumu, edilgen; ''aleyhi' — gönderge 'mimmâ' 5. kelime; 'fassale', 'harrame' — gönderge 'llâhi' 8. kelime; 'ileyhi' — gönderge 'mâ' 13. kelime; 'huve' — gönderge 'rabbeke' 27. kelime), 3MP ('le-yudillûne', 'bi-ehvâ'ihim' — gönderge 'kesîran' 21. kelime, tartışmalı), muhatap 2MS ('rabbeke'); "
 "6:120 muhatap 2MP ('ve zerû'), 3MS ('ve bâtinahû' eki — gönderge 'l-ismi' 3. kelime), 3MP ('yeksibûne', 'se-yuczevne', 'kânû', 'yaqterifûn' — gönderge 'llezîne' 6. kelime); "
 "6:121 muhatap 2MP ('te'kulû', 'li-yucâdilûkum', 'eta'tumûhum', 'innekum'), 3MS ('yuzkeri' — fiil uyumu, edilgen; ''aleyhi' — gönderge 'mimmâ' 3. kelime; 've innehû' — gönderge 'mimmâ' 3. kelime, tartışmalı: karşı aday yeme eylemi), 3MP ('le-yûhûne', 'evliyâ'ihim', 'li-yucâdilûkum' — gönderge 'ş-şeyâtîne' 12. kelime; 'eta'tumûhum' eki — tartışmalı) — betik denetimi: KHATA_ADSIZ; "
 "edilgen: 6:118 'zukira' (3. kelime; naib-i faili 'smu' 4. kelime), 6:119 'zukira' (6. kelime; naib-i faili 'smu' 7. kelime) ve 'dturirtum' (18. kelime; naib-i fail 2MP zamir), 6:120 'se-yuczevne' (9. kelime; naib-i fail 3MP zamir), 6:121 'yuzkeri' (5. kelime; naib-i faili 'smu' 6. kelime) — ölçüm EDİLGEN 1/3, 2/6, 1/5, 1/5 bu kelimelerden",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:118, 6:119, 6:120 ve 6:121 söz yok — söz fiili yok (okuma); mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 118 121 28' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:118 'fe-kulû' (1.) 'fe' REM; 6:119 've mâ' (1.) REM, 've qad' (10.), 've inne' (20.) CONJ; 6:120 've zerû' (1.) REM, 've bâtinahû' (4.) CONJ; 6:121 've lâ' (1.), 've innehû' (9.), 've in' (17.) REM, 've inne' (11.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:118, 6:119, 6:120 ve 6:121 ◈K / ◈B tetik yok (سمو kökü 'ism' lemmasında S1 kısıtıyla tetiklemez)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 118 121 28'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:119 (53:30); 6:118, 6:120 ve 6:121 bağ yok; ayetler arası kalıp 'mimmâ zukira'smu'llâhi 'aleyh' (6:118, 6:119) — sayım 'dizi 6 118 1 6', 'dizi 6 119 4 9'; ayetler arası kalıp 'smu'llâhi 'aleyh' (6:118, 6:119, 6:121) — sayım 'dizi 6 118 3 6', 'dizi 6 119 6 9', 'dizi 6 121 5 8'; ayetler arası kalıp 'smu'llâh' (6:118, 6:119, 6:121) — sayım 'dizi 6 118 3 5', 'dizi 6 119 6 8', 'dizi 6 121 5 7'; blok içi tekrar (bölüm 9 kuralı 6), ardışık bağ yerine sayımla kayıt (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:118 şahıs geçişi 3 → 2, edim geçişi haber → emir, şart, şart → cevap ('in' 7. kelime); 6:119 şahıs geçişi yok, şahıs sayısında beraberlik (2. şahıs 8 · 3. şahıs 9), edim geçişi emir, şart → soru; "
 "6:120 şahıs geçişi 2 → 3, edim geçişi soru → emir; 6:121 şahıs geçişi 3 → 2, şahıs sayısında beraberlik (2. şahıs 6 · 3. şahıs 9), edim geçişi emir → yasak, şart, şart → cevap ('in' 17. kelime), bölüm kapanışı; "
 "ölçüm iltifât 6:118-121 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:118 'fe-kulû' — emir (morph REM); 'in kuntum' — şart, cevabı önde (morph COND); 6:119 'mâ lekum ellâ te'kulû' — soru ve olumsuz masdar (morph INTG + SUB, NEG); 'qad fassale' — tahkik (morph CERT); "
 "'illâ ma'dturirtum' — istisna (morph EXP); 'le-yudillûne' — pekiştirme (morph EMPH); 6:120 'se-yuczevne' — gelecek ve edilgen (morph FUT); 6:121 've lâ te'kulû' — nehy (morph REM + PRO); 'li-yucâdilûkum' — amaç lâmı (morph PRP); "
 "'ve in eta'tumûhum innekum le-muşrikûn' — şart ve pekiştirmeli cevap (morph REM + COND, EMPH)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:119 25-29. kelime — 53:30 ile lemma dizisi eşi (sayım: 'dizi 6 119 25 27', 'dizi 6 119 26 29'); "
 "6:118 3-6., 6:119 6-9. ve 6:121 5-8. kelime — blok içi lemma dizisi 'zekere ism allâh 'alâ' (sayım: 'dizi 6 118 3 6'); 6:119 kök علم ikilemesi; 6:120 kök أثم ikilemesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 28'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'inne rabbeke' 6:119 'Rabbin' / 53:30 'Rabbin' (emsal metninde) — çakışma değil (bayt eşit); 'huve a'lemu' 6:119 'en iyi bilendir' / 53:30 'en iyi bilendir' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:118 'fe-kulû' IMPV — meal 'yiyin'; 'zukira' PERF PASS — meal 'anılan'; 'kuntum' PERF (şart) — meal 'inananlarsanız'; "
 "6:119 'te'kulû' IMPF SUBJ ('en lâ' ile) — meal 'yemiyorsunuz'; 'zukira' PERF PASS — meal 'anılan'; 'fassale' PERF — meal 'açıklamıştır'; 'harrame' PERF — meal 'kıldığı'; 'dturirtum' PERF PASS — meal 'zorda kaldığınız'; 'yudillûne' IMPF IND — meal 'saptırıyorlar'; "
 "6:120 've zerû' IMPV — meal 'bırakın'; 'yeksibûne' IMPF IND — meal 'kazananlar'; 'yuczevne' IMPF IND PASS ('se' ile) — meal 'cezalandırılacaklardır'; 'kânû' PERF — meal 'olduklarıyla'; 'yaqterifûn' IMPF IND — meal 'işlemekte'; "
 "6:121 'te'kulû' IMPF JUS ('lâ' ile) — meal 'yemeyin'; 'yuzkeri' IMPF JUS PASS ('lem' ile) — meal 'anılmayan'; 'yûhûne' IMPF IND — meal 'fısıldarlar'; 'yucâdilû' IMPF SUBJ — meal 'tartışsınlar'; 'eta'tumû' PERF (şart) — meal 'itaat ederseniz'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 118 121 28'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:118, 6:119, 6:120 ve 6:121 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:120 ('zâhira' / 've bâtinahû'); 6:118, 6:119 ve 6:121 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök أكل 6:118 ('fe-kulû'), 6:119 ('te'kulû') ve 6:121 ('te'kulû'); kök ذكر 6:118 ('zukira'), 6:119 ('zukira') ve 6:121 ('yuzkeri'); kök سمو 6:118 ('smu'), 6:119 ('smu') ve 6:121 ('smu'); kök أله 6:118 ('llâhi'), 6:119 ('llâhi') ve 6:121 ('llâhi'); kök كون 6:118 ('kuntum') ve 6:120 ('kânû'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 14-2 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 27 ve 28; bu blok bölümü kapatıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b28/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 118 121 28'; lem_bozuk.py 28 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 118 121 → AYN_SONUC; sunum/bolum4_kurallar.py 118 121 28 → KHATA_HEPSI; sunum/bolum5_kurallar.py 118 121 28 → B5_HEPSI; sunum/bolum6_kurallar.py 118 121 28 → B6_HEPSI; sunum/bolum7_kurallar.py 118 121 28 → B7_HEPSI; sunum/bolum8_kurallar.py 118 121 28 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 118 121 28 → B9_HEPSI; sunum/bolum10_kurallar.py 118 121 28 → B10_HEPSI; sunum/bolum11_kurallar.py 118 121 28 → B11_HEPSI; sunum/bolum12_kurallar.py 118 121 28 → B12_HEPSI; sunum/bolum13_kurallar.py 118 121 28 → B13_HEPSI; sunum/bolum14_kurallar.py 118 121 28 → B14_HEPSI; sunum/bolum15_kurallar.py 118 121 28 → B15_HEPSI; sunum/bolum16_kurallar.py 118 121 28 → B16_HEPSI; sunum/bolum17_kurallar.py 118 121 28 → B17_HEPSI; sunum/bolum18_kurallar.py 118 121 28 → B18_HEPSI; sunum/bolum19_kurallar.py 118 121 28 → B19_HEPSI; sunum/bolum20_kurallar.py 118 121 28 → B20_HEPSI; sunum/bolum21_kurallar.py 118 121 28 → B21_HEPSI; sunum/bolum22_kurallar.py 118 121 28 → B22_HEPSI; sunum/bolum23_kurallar.py 118 121 28 → B23_HEPSI; sunum/bolum24_kurallar.py 118 121 28 → B24_HEPSI; sunum/bolum25_kurallar.py 118 121 28 → B25_HEPSI; sunum/bolum26_kurallar.py 118 121 28 → B26_HEPSI; sunum/bolum27_kurallar.py 118 121 28 → B27_HEPSI; sunum/bolum28_kurallar.py 118 121 28 → B28_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 28 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('ekele', 'mimmâ', 'zekere', 'ism', 'allâh', ''alâ', 'inne', 'rabb', 'a'lem', 'ğayr', ''ilm', 'cezâ', 'bi-mâ', 'mâ', 'kâne', 'mu'tedî'); joker '_' lemmasız öğede ('dizi 6 119 26 29' — 'huve'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (118, 121): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_118_121.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b26k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '118', '121'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '118', '121', '28'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '118', '121', '28'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '118', '121', '28', '--tazelik-yok')}
    for _n in range(7, 30): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '118', '121', '28')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29 = [_R['B%d' % _n].splitlines() for _n in range(6, 30)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
