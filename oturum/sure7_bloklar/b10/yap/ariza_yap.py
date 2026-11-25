# sûre 7 blok 10 (7:35-37) ARIZA oluşturucu — bölüm 4-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b10/olcum.txt'
os.environ['SAY2'] = '/home/claude/b10/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = list(ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_7_b09.txt', encoding='utf-8').read() + ']'))
VF_YAZI_ESKI = {}
BOL = "'Elçiler gelince; yalanlayanların ateşte çekişmesi'"


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
 ("7:36", "'kezzebe âye istekbere 'an'", 2, 'say 7:36 2-5', "harekesiz 'kezzebû bi-âyâtinâ ve'stekberû 'anhâ' (2-5. kelime)", ('dizi 7 36 2 5', "kezzebe âye istekbere 'an", '2-5', "biçim farkı (dizi 7 36 2 5): basılmamış eş yazım eş")),
 ("7:36", "'ellezî kezzebe âye'", 3, 'say 7:36 1-3', "harekesiz 've'llezîne kezzebû bi-âyâtinâ' (1-3. kelime); biçim öğesi 'ellezî' öneki (lemma dizisi sûre içi 8, nakarat3 3)", ('dizi 7 36 1 3', "ellezî kezzebe âye", '1-3', "biçim farkı (dizi 7 36 1 3): basılmamış eş önek; basılmamış eş önek; basılmamış eş önek; basılmamış eş yazım eş; basılmamış eş önek; basılmamış eş önek; basılmamış eş yazım eş")),
 ("7:36", "'_ fî xâlid'", 2, 'say 7:36 9-11', "harekesiz 'hum fîhâ xâlidûn' (9-11. kelime)", ('dizi 7 36 9 11', "_ fî xâlid", '9-11', "biçim farkı (dizi 7 36 9 11): basılmamış eş yazım eş")),
 ("7:37", "'ifterâ 'alâ allâh kezib'", 2, 'say 7:37 4-7', "harekesiz 'fterâ 'ale'llâhi keziben' (4-7. kelime)", ('dizi 7 37 4 7', "ifterâ 'alâ allâh kezib", '4-7', "biçim farkı (dizi 7 37 4 7): basılmamış eş fiil çekimi, zamir eki")),
 ("7:37", "'de'â min dûn allâh'", 2, 'say 7:37 25-28', "harekesiz 'ted'ûne min dûni'llâhi' (25-28. kelime)", ('dizi 7 37 25 28', "de'â min dûn allâh", '25-28', "biçim farkı (dizi 7 37 25 28): basılmamış eş yazım eş")),
 ("7:37", "'min dûn allâh'", 3, 'say 7:37 26-28', "harekesiz 'min dûni'llâhi' (26-28. kelime)", ('dizi 7 37 26 28', "min dûn allâh", '26-28', "biçim farkı (dizi 7 37 26 28): 7:30 yazım eş; basılmamış eş yazım eş")),
 ("7:37", "'de'â min dûn'", 3, 'say 7:37 25-27', "harekesiz 'ted'ûne min dûni' (25-27. kelime)", ('dizi 7 37 25 27', "de'â min dûn", '25-27', "biçim farkı (dizi 7 37 25 27): basılmamış eş yazım eş; basılmamış eş zamir eki")),
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

VF_YAZI = {35: {10: "'fe-meni'", 12: "'ve asleha'", 13: "'fe-lâ'", 16: "'ve lâ'"}, 36: {1: "'ve'llezîne'", 4: "'ve'stekberû'"}, 37: {1: "'fe-men'", 32: "'ve şehidû'"}}
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
ONC = run('/home/claude/sunum/onceki_basim.py', '35', '37', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b10/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b10/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '35', '37', '10').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_35_37.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:35', '7:36', '7:37'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_35_37.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(35, 38))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:37 'izâ' (17. kelime — morph T, zaman); 7:37 kök نفس ('enfusihim' 34. kelime — kendi): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '35', '37', '10')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b10/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 11)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(35, 38))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l.replace('**', '') for l in open('/home/claude/b10/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b10/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 34), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol mecrur\)', _OL[0]).group(0))
for _k, _v in (('_AK1', _AK1),): _MB = _MB.replace('" + %s + "' % _k, _v)
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; bölüm 3 kapanışında sunum/bolum38_kurallar.py (kural 1-5) eklendi, sunum/geriye_donuk.py ve mutasyon_sina buna göre güncellendi — önceki commit'te, kapanış mutasyon sınaması 405 / 405; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 407",
 "geriye dönük koşu (sûre 7 bölüm 3 kapanışı, komut 'python3 sunum/geriye_donuk.py b09k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 35 37 10'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:35, 7:36 ve 7:37 esmâ yok; 7:37 lafız (6. ve 28. kelime); 7:35 ve 7:36 lafız yok; 7:35, 7:36 ve 7:37 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 35 37 10'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (35, 36, 37)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 35 37 10'): KALAN_P",
 "ölçüm aktör: 7:35 '{{1|" + _AK1 + "}}' (A1'de 'âdeme'); 7:36 ve 7:37 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:35 nida, şart — COND 2 'immâ' (3.; 'in'), 'fe-meni' (10.; 'men'), EMPH 1 'ye'tiyennekum' (4.; 'n'), NEG 2 'lâ' (13. ve 16.), VOC 1 'yâ' (1.); 7:36 haber — kip yok; 7:37 soru — INTG 2 'fe-men' (1.; 'men'), 'eyne' (22.); "
 "morph SUP ('immâ' 7:35 3.), RSLT ('fe-meni' 7:35 10., 'fe-lâ' 7:35 13.), REM ('ve'llezîne' 7:36 1., 'fe-men' 7:37 1.), REL ('ve'llezîne' 7:36 1., 'mimmeni' 7:37 3., 'mâ' 7:37 23.), DEM ve ADDR ('ulâ'ike' 7:36 6., 7:37 11.), INC ('hattâ' 7:37 16.), T ('izâ' 7:37 17.), ACC ('ennehum' 7:37 35.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:37 ★★ (kaynak n, z=2,61); 7:35 ve 7:36 yıldız yok",
 "fâsıla: 7:34 ن → 7:35 ن (" + _F[0] + ") → 7:36 ن (" + _F[1] + ") → 7:37 ن (" + _F[2] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:35 6:48 (basılmış), 6:130 (basılmış); 7:36 xref yok; 7:37 6:21 (basılmış), 6:130 (basılmış), 10:17 (basılmış), 40:74 (emsal olarak basıldı), okunmuş 3 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:36 'kezzebe âye istekbere 'an' süzgeç GEÇER, 'ellezî kezzebe âye' süzgeç GEÇER, '_ fî xâlid' süzgeç GEÇMEZ; 7:37 'ifterâ 'alâ allâh kezib' süzgeç GEÇER, 'de'â min dûn allâh' süzgeç GEÇER, 'min dûn allâh' süzgeç GEÇER, 'de'â min dûn' süzgeç GEÇER; 7:35 nakarat3 yok; GEÇER kalıpların sûre içi eşleri basılmamış ya da D3 dışı listesinde",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:35 3MS ('ye'tiyennekum' — fiil uyumu, fail 5. kelime; 'ttaqâ', 've asleha' — gönderge 'fe-meni' 10. kelime), muhatap 2MP eki ('ye'tiyennekum', 'minkum', ''aleykum'), 3MP ('yaqussûne' — gönderge 'rusulun' 5. kelime; 'hum', 'yahzenûn' — tartışmalı; sayı uyumsuz; gönderge 'fe-meni' 10. kelime; ek ''aleyhim' — tartışmalı; sayı uyumsuz; gönderge 'fe-meni' 10. kelime), konuşan 1S eki ('âyâtî'), aktör adlı 'âdeme'; "
 "7:36 3MP ('kezzebû', 've'stekberû', 'hum' — gönderge 've'llezîne' 1. kelime), konuşan 1P eki ('bi-âyâtinâ'), 3FS eki (''anhâ' — gönderge 'bi-âyâtinâ' 3. kelime; 'fîhâ' — gönderge 'n-nâri' 8. kelime); "
 "7:37 3MS ('fterâ', 'kezzebe' — gönderge 'mimmeni' 3. kelime; 'yenâluhum' — fiil uyumu, fail 13. kelime; ek 'bi-âyâtihî' — gönderge 'llâhi' 6. kelime), 3FS ('câ'ethum' — fiil uyumu, fail 19. kelime), 3MP ('yeteveffevnehum', 'qâlû' 21. kelime — gönderge 'rusulunâ' 19. kelime; 'qâlû' 29. kelime, 've şehidû', 'kânû' — gönderge 'ulâ'ike' 11. kelime; 'dallû' — söz içi; gönderge 'mâ' 23. kelime; "
 "ekler 'yenâluhum', 'nasîbuhum', 'câ'ethum', 'yeteveffevnehum', 'enfusihim', 'ennehum' — gönderge 'ulâ'ike' 11. kelime), konuşan 1P eki ('rusulunâ'; ''annâ' — söz içi), muhatap 2MP ('kuntum', 'ted'ûne' — söz içi)",
 "7:35-37 gönderge zinciri: 7:35 nida ile muhatap 'benî âdeme' (1-2. kelime); 7:35 konuşan 1S ('âyâtî' 9. kelime) ile 7:36 ve 7:37 konuşan 1P ('bi-âyâtinâ' 7:36 3. kelime, 'rusulunâ' 7:37 19. kelime) eş — tekilden çoğula geçiş; 7:35 'aleyhim' (15. kelime), 'hum' (17. kelime) ve 'yahzenûn' (18. kelime) 3MP — gönderge 'fe-meni' (10. kelime), tartışmalı: sayı uyumsuz (şart adı tekil fiille, cevap çoğul zamirle); "
 "7:36 3MP fiiller ve 'hum' (9. kelime) 've'llezîne' (1. kelime); 7:37 'ulâ'ike' (11. kelime) 'mimmeni' (3. kelime) ile kurulan yalan uyduran ve yalanlayanlara; 7:37 'qâlû' (21. kelime) 'rusulunâ' (19. kelime), 'qâlû' (29. kelime) 'ulâ'ike' (11. kelime) — konuşan değişimi; 7:37 söz içi muhatap 2MP 'ulâ'ike' topluluğu, söz içi konuşan 1P (''annâ' 31. kelime) yine o topluluk; 'dallû' (30. kelime) 'mâ' (23. kelime) ilgi adına (okuma)",
 "edilgen: 7:35, 7:36 ve 7:37 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:37 'qâlû' (21.) ardından söz 22-28. kelime — ayet içi kapanış; 7:37 'qâlû' (29.) ardından söz 30-31. kelime — ayet içi kapanış, 've şehidû' (32.) anlatıya dönüş (okuma); "
 "7:35 ve 7:36 söz fiili yok, A3 '—'; 7:35 nida 'yâ benî âdeme' (1-2. kelime) — A4'te 'nidâ' ile; mealde 'dediler ki:' ve 'Dediler ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 35 37 10' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:35 've asleha' (12.) CONJ, 've lâ' (16.) CONJ; 7:36 've'llezîne' (1.) REM, 've'stekberû' (4.) CONJ; 7:37 've şehidû' (32.) CONJ; "
 "'fe' konumları: 7:35 'fe-meni' (10.) RSLT, 'fe-lâ' (13.) RSLT; 7:37 'fe-men' (1.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:35, 7:36 ve 7:37 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 35 37 10'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:37 (40:74); 7:35 ve 7:36 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:37 أله ×2, قول ×2, كذب ×2, كون ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: bloğun emsal dosyasında olmayan basılmış eş (önceki bloklarda basılmış ya da sûre içi), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:35 bölüm açılışı, nidâ ('yâ benî âdeme' 1. kelime), şart → cevap (ayet içi; COND 'in' 3. kelime), şart → cevap (ayet içi; COND 'men' 10. kelime), şahıs geçişi yok, edim geçişi haber → nida, şart; 7:36 şahıs geçişi yok, edim geçişi nida, şart → haber; "
 "7:37 söz açılır (22. kelime), söz kapanır (28. kelime, ayet içi), söz açılır (30. kelime), söz kapanır (31. kelime, ayet içi), şahıs geçişi yok, edim geçişi haber → soru; ölçüm iltifât 7:35-37 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:35 'immâ ye'tiyennekum' — zâid edatla pekişen şart ve tekitli muzâri (morph COND + SUP + IMPF + EMPH); 7:35 'fe-meni'ttaqâ' — şart adıyla açılan iç şart (morph RSLT + COND + PERF); 7:35 'fe-lâ xavfun 'aleyhim' — şartın cevabı, olumsuz isim cümlesi (morph RSLT + NEG + INDEF); "
 "7:36 've'llezîne kezzebû' — ilgi adıyla açılan özne (morph REM + REL + PERF); 7:37 'fe-men azlemu' — soru adı ve üstünlük adı (morph REM + INTG + NOM); 7:37 'hattâ izâ câ'ethum' — sınır edatı ve zaman zarfı (morph INC + T + PERF)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:35 'yâ benî âdeme' ile açılıyor (sayım: 'say 7:35 1-2'); 7:35 5-9. kelime — 6:130 ile harekesiz eş (sayım: 'say 7:35 5-9'); 7:35 12-18. kelime — 6:48 ile harekesiz eş (sayım: 'say 7:35 12-18'); "
 "7:36 6-11. kelime okunmuş 4 ayetle harekesiz eş (sayım: 'say 7:36 6-11'); 7:37 1-10. kelime — 10:17 ile harekesiz eş (sayım: 'say 7:37 1-10'); 7:37 2-10. kelime — 6:21 ve 10:17 ile harekesiz eş (sayım: 'say 7:37 2-10'); 7:37 30-31. kelime — 40:74 ile harekesiz eş (sayım: 'say 7:37 30-31'); 7:37 32-37. kelime — 6:130 ile harekesiz eş (sayım: 'say 7:37 32-37'); "
 "7:37 kök أله, قول, كذب ve كون ikilemeleri",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 10'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'min dûni'llâhi' 7:37 'Allah'tan başka' / 40:74 'Allah'ı bırakıp' (emsal metninde) — çakışma — tam okuma sonu ('min dûn' karşılığı 'başka' / 'bırakıp'); "
 "'dallû 'annâ' 7:37 'Bizden kaybolup gittiler' / 40:74 'Bizden kaybolup gittiler' (emsal metninde) — çakışma değil (bayt eşit); en uzun ortak lemma dizisi 'dizi 7 37 26 31' içindeki 'qâlû' (29. kelime) 7:37'de 'Dediler ki', emsalde 'Dediler' — 'ki' takdiri farkı; "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:35 'ye'tiyenne' IMPF IND ('in' ve 'n' ile) — meal 'gelirse'; 'yaqussûne' IMPF IND — meal 'anlatan'; 'ttaqâ' PERF ('men' ile) — meal 'sakınır'; 'asleha' PERF — meal 'düzeltirse'; 'yahzenûn' IMPF IND ('lâ' ile) — meal 'üzülmezler'; "
 "7:36 'kezzebû' PERF — meal 'yalanlayıp'; 'stekberû' PERF — meal 'büyüklenenler'; "
 "7:37 'fterâ' PERF — meal 'uydurandan'; 'kezzebe' PERF — meal 'yalanlayandan'; 'yenâlu' IMPF IND — meal 'erişir'; 'câ'et' PERF ('izâ' ile) — meal 'geldiğinde'; 'yeteveffevne' IMPF IND — meal 'ettirmek'; 'qâlû' PERF (21. kelime) — meal 'dediler'; 'kuntum' PERF — meal 'olduklarınız'; 'ted'ûne' IMPF IND — meal 'etmekte'; "
 "'qâlû' PERF (29. kelime) — meal 'Dediler'; 'dallû' PERF — meal 'gittiler'; 'şehidû' PERF — meal 'ettiler'; 'kânû' PERF — meal 'olduklarına'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle; IMPF IND geniş zaman karşılığı her blokta sapma sayılır — sûre 7 bölüm 3 denetimi kuralı 3): 'ye'tiyenne' IMPF 7:35'te 'in' ile geniş zaman şartı ('-irse') ile; 'yaqussûne' IMPF 7:35'te sıfat-fiil ('-an') ile; 'ttaqâ' ve 'asleha' PERF 7:35'te 'men' ile geniş zaman şartı ('-ır', '-irse') ile; "
 "'yahzenûn' IMPF 7:35'te geniş zaman ('-mezler') ile; 'kezzebû' PERF 7:36'da ulaç ('-yıp') ile; 'stekberû' PERF 7:36'da sıfat-fiil ('-enler') ile; 'fterâ' ve 'kezzebe' PERF 7:37'de sıfat-fiil ('-an') ile; 'yenâlu' IMPF 7:37'de geniş zaman ('-ir') ile; 'câ'et' PERF 7:37'de zarf-fiil ('-diğinde') ile; "
 "'yeteveffevne' IMPF 7:37'de ad-fiil ('-mek') ile; 'kuntum' PERF ve 'ted'ûne' IMPF 7:37'de sıfat-fiil ('-mekte olduklarınız') ile; 'kânû' PERF 7:37'de ad-fiil ('-duklarına') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): bölümün açılış bloğu — bölüm içinde önceki blok yok",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 35 37 10'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:35, 7:36 ve 7:37 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:35, 7:36 ve 7:37 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök أيي 7:35 ('âyâtî'), 7:36 ('bi-âyâtinâ') ve 7:37 ('bi-âyâtihî'); kök رسل 7:35 ('rusulun') ve 7:37 ('rusulunâ'); kök كذب 7:36 ('kezzebû') ve 7:37 ('keziben', 'kezzebe'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 4-1 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm açılışı bu blokta; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b10/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 35 37 10'; lem_bozuk.py 10 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 35 37 → AYN_SONUC; sunum/bolum4_kurallar.py 35 37 10 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 35 37 10 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 39)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 10 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('bunayy' (morph LEM ham biçim), 'âdem', 'rasûl', 'min', 'qassa', ''alâ', 'âye', 'ellezî', 'kezzebe', 'istekbere', ''an', 'fî', 'xâlid', 'ifterâ', 'allâh', 'kezib', 'de'â', 'dûn', 'qâle', 'dalle'); joker '_' yalnız lemmasız öğede ('hum' — 'dizi 7 36 9 11'; ayrı zamir, morph LEM yok); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (35, 37): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_35_37.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_7_b09k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '35', '37'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '35', '37', '10'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '35', '37', '10'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '35', '37', '10', '--tazelik-yok')}
    for _n in range(7, 39): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '35', '37', '10')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38 = [_R['B%d' % _n].splitlines() for _n in range(6, 39)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'B34_HEPSI': (B34[-1] if B34 else '?'), 'B35_HEPSI': (B35[-1] if B35 else '?'), 'B36_HEPSI': (B36[-1] if B36 else '?'), 'B37_HEPSI': (B37[-1] if B37 else '?'), 'B38_HEPSI': (B38[-1] if B38 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34, B35, B36, B37, B38): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
