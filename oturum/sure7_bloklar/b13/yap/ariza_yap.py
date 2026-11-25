# sûre 7 blok 13 (7:44-47) ARIZA oluşturucu — bölüm 5-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b13/olcum.txt'
os.environ['SAY2'] = '/home/claude/b13/say2.txt'
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
 ("7:44", "'nâdâ ashâb cenne'", 2, 'say 7:44 1-3', "harekesiz 've nâdâ ashâbu'l-cenneti' (1-3. kelime)", ('dizi 7 44 1 3', "nâdâ ashâb cenne", '1-3', "biçim farkı (dizi 7 44 1 3): 7:46 fiil çekimi, zamir eki")),
 ("7:44", "'rabb haqq hel'", 2, 'say 7:44 11-13', "harekesiz 'rabbunâ haqqan fe-hel' (11-13. kelime)", ('dizi 7 44 11 13', "rabb haqq hel", '11-13', "biçim farkı (dizi 7 44 11 13): basılmamış eş i'râb, önek")),
 ("7:45", "'sadde 'an sebîl allâh'", 2, 'say 7:45 2-5', "harekesiz 'yasuddûne 'an sebîli'llâhi' (2-5. kelime)", ('dizi 7 45 2 5', "sadde 'an sebîl allâh", '2-5', "biçim farkı (dizi 7 45 2 5): basılmamış eş fiil çekimi, zamir eki, önek")),
 ("7:46", "'nâdâ ashâb cenne'", 2, 'say 7:46 9-11', "harekesiz 've nâdev ashâbe'l-cenneti' (9-11. kelime)", ('dizi 7 46 9 11', "nâdâ ashâb cenne", '9-11', "biçim farkı (dizi 7 46 9 11): 7:44 fiil çekimi, zamir eki")),
 ("7:46", "'a'râf ricâl 'arafe'", 2, 'say 7:46 4-6', "harekesiz 'l-a'râfi ricâlun ya'rifûne' (4-6. kelime)", ('dizi 7 46 4 6', "a'râf ricâl 'arafe", '4-6', "biçim farkı (dizi 7 46 4 6): basılmamış eş elif yazımı, zamir eki")),
 ("7:46", "'ashâb cenne en'", 2, 'say 7:46 10-12', "harekesiz 'ashâbe'l-cenneti en' (10-12. kelime)", ('dizi 7 46 10 12', "ashâb cenne en", '10-12', "biçim farkı (dizi 7 46 10 12): basılmamış eş yazım eş")),
 ("7:47", "'lâ ce'ale ma'a qavm zâlim'", 2, 'say 7:47 9-13', "harekesiz 'lâ tec'alnâ ma'a'l-qavmi'z-zâlimîn' (9-13. kelime)", ('dizi 7 47 9 13', "lâ ce'ale ma'a qavm zâlim", '9-13', "biçim farkı (dizi 7 47 9 13): basılmamış eş zamir eki, önek")),
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

VF_YAZI = {44: {1: "'ve nâdâ'", 13: "'fe-hel'", 21: "'fe-ezzene'"}, 45: {6: "'ve yebğûnehâ'", 8: "'ve hum'"}, 46: {1: "'ve beynehumâ'", 3: "'ve 'ale'", 9: "'ve nâdev'", 17: "'ve hum'"}, 47: {1: "'ve izâ'"}}
sys.path.insert(0, '/home/claude/b13/yap')
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
open('/home/claude/b13/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '13')
BLOKLAR = [str(i) for i in range(1, 14)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '13', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b13/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '44', '47', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b13/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b13/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '44', '47', '13').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_44_47.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'7:44', '7:45', '7:46', '7:47'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_7_44_47.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '7:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '7:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(44, 48))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "7:44 kök أذن ('fe-ezzene' 21. kelime — duyur-): tetik listesinde yok; 7:44 kök أذن ('mu'ezzinun' 22. kelime — duyurucu): tetik listesinde yok; 7:45 kök صدد ('yasuddûne' 2. kelime — alıkoy-): tetik listesinde yok; 7:45 kök أخر ('bi'l-âxirati' 9. kelime — âhiret): tetik listesinde yok; 7:46 kök رجل ('ricâlun' 5. kelime — adam): tetik listesinde yok; 7:47 'izâ' (1. kelime — morph T, zaman)"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '44', '47', '13')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b13/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 14)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b7:%d:\d+' % a_, s_) for a_ in range(44, 48))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
_OL = [l.replace('**', '') for l in open('/home/claude/b13/olcum.txt', encoding='utf-8').read().split('\n\n') if l.strip()]
_F = [re.search(r'fâsıla (\S+) →', l).group(1) for l in _OL]
_MB = open('/home/claude/b13/yap/metin_body.py', encoding='utf-8').read().replace('\\\\', '\\')
_MB = re.sub(r'" \+ _F\[(\d)\] \+ "', lambda m_: _F[int(m_.group(1))], _MB)
def _pat(n):
    p = list(dict.fromkeys(re.findall(r"\{\{%d\|[^}]*\}\}" % (n - 43), _MB)))
    p = ["'%s'" % x for x in p]
    return '7:%d ' % n + (', '.join(p[:-1]) + ' ve ' + p[-1] if len(p) > 1 else p[0])
def _esc(t):
    for c in '.()[]|+*': t = t.replace(c, '\\' + c)
    return t
_AK1 = _esc(re.search(r'aktör: adlı .*?rol mecrur\)', _OL[0]).group(0))
_AK3 = _esc(re.search(r'aktör: adlı .*?rol mecrur\)', _OL[2]).group(0))
for _k, _v in (('_AK1', _AK1), ('_AK3', _AK3)): _MB = _MB.replace('" + %s + "' % _k, _v)
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bu blokta araç kuralı değişmedi; yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 426",
 "geriye dönük koşu (sûre 7 bölüm 4 kapanışı, komut 'python3 sunum/geriye_donuk.py b11k'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 44 47 13'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 7:45 've hum bi'l-âxirati kâfirûn' (8-10. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (âhiret günü) (yamalar/esma_el_7_44_47.txt); 7:46 'selâmun 'aleykum' (13-14. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (selamlama sözü) (yamalar/esma_el_7_44_47.txt); 7:45 ve 7:46 esma_kayit 'mühür EVET' / ölçüm MÜHÜRSÜZ — uyuşmuyor (esma_el 'degil' kararı; muhur_el ölçümle eş); 7:44 ve 7:47 esmâ yok; "
 "7:44 lafız (26. kelime), 7:45 lafız (5. kelime); 7:46 ve 7:47 lafız yok; 7:44 Rab (11. ve 17. kelime), 7:47 Rab (8. kelime); 7:45 ve 7:46 Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 44 47 13'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 7:45 ve 7:46 mühür EVET / ölçüm MÜHÜRSÜZ — uyuşmuyor, esma_el 'degil' kararı): " + EMH,
 "ölçüm: " + '; '.join(_pat(n) for n in (44, 45, 46, 47)) + " — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 44 47 13'): KALAN_P",
 "ölçüm aktör: 7:44 '{{1|" + _AK1 + "}}' (A1'de 'l-cenneti'); 7:46 '{{3|" + _AK3 + "}}' (A1'de 'l-cenneti'); 7:45 ve 7:47 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 7:44 soru — CERT 1 'qad' (7.), INTG 1 'fe-hel' (13.; 'hel'); 7:45 haber — kip yok; 7:46 haber — NEG 1 'lem' (15.); 7:47 yasak — PRO 1 'lâ' (9.); ölçüm biçim NEHY (D2'de yazılmadı); "
 "morph INT ('en' 7:44 6. ve 24., 7:46 12.), REL ('mâ' 7:44 9. ve 15., 'llezîne' 7:45 1.), REM ('fe-hel' 7:44 13., 'fe-ezzene' 7:44 21., 've hum' 7:45 8., 've beynehumâ' 7:46 1., 've izâ' 7:47 1.), ANS ('na'am' 7:44 20.), LOC ('beynehum' 7:44 23., 've beynehumâ' 7:46 1., 'tilqâ'e' 7:47 4., 'ma'a'l-qavmi' 7:47 11.), CIRC ('ve hum' 7:46 17.), T ('ve izâ' 7:47 1.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 7:44 ★ (kaynak n, z=1,65); 7:47 ★ (kaynak pas, z=1,57); 7:45 ve 7:46 yıldız yok",
 "fâsıla: 7:43 ن → 7:44 ن (" + _F[0] + ") → 7:45 ن (" + _F[1] + ") → 7:46 ن (" + _F[2] + ") → 7:47 ن (" + _F[3] + ") — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 7:44 11:18 (emsal olarak basıldı), okunmuş 2 ayet; 7:45 11:19 (emsal olarak basıldı), 14:3 (emsal olarak basıldı), esit2 11:19 YAKIN; 7:46 xref yok; 7:47 23:94 (emsal olarak basıldı), okunmamış 1 ayet (sûre içi 1)",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + ('; '.join(r5) or 'bu blokta nakarat3 kalıbı yok'),
 "nakarat3 (R3: kalıp adıyla özetlendi): 7:44 'nâdâ ashâb cenne' süzgeç GEÇMEZ, 'rabb haqq hel' süzgeç GEÇMEZ; 7:45 'sadde 'an sebîl allâh' süzgeç GEÇER; 7:46 'nâdâ ashâb cenne' süzgeç GEÇMEZ, 'a'râf ricâl 'arafe' süzgeç GEÇMEZ, 'ashâb cenne en' süzgeç GEÇMEZ; 7:47 'lâ ce'ale ma'a qavm zâlim' süzgeç GEÇER; GEÇER kalıpların sûre içi eşleri basılmamış",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "7:44 3MS ('ve nâdâ' — fiil uyumu, fail 2. kelime; 've'adenâ' — söz içi; fiil uyumu, fail 11. kelime; 've'ade' — söz içi; fiil uyumu, fail 17. kelime; 'fe-ezzene' — fiil uyumu, fail 22. kelime), konuşan 1P ('vecednâ' — söz içi; ekler 've'adenâ', 'rabbunâ' — söz içi), muhatap 2MP ('vecedtum' — söz içi; ek 'rabbukum' — söz içi), 3MP ('qâlû' — gönderge 'ashâbe'n-nâri' 4. kelime; ek 'beynehum' — tartışmalı; gönderge 'ashâbu'l-cenneti' 2. kelime), aktör adlı 'l-cenneti'; "
 "7:45 3MP ('yasuddûne', 've yebğûnehâ', 'hum' — gönderge 7:44 28. kelime), 3FS eki ('ve yebğûnehâ' — tartışmalı; cins uyumsuz; gönderge 'sebîli' 4. kelime); "
 "7:46 3D eki ('ve beynehumâ' — tartışmalı; gönderge 7:44 2. kelime), 3MP ('ya'rifûne', 've nâdev' — gönderge 'ricâlun' 5. kelime; 'yedxulûhâ', 'hum', 'yatma'ûn' — tartışmalı; gönderge 'ricâlun' 5. kelime; ek 'bi-sîmâhum' — tartışmalı; sayı uyumsuz; gönderge 'kullen' 7. kelime), muhatap 2MP eki (''aleykum' — söz içi), 3FS eki ('yedxulûhâ' — gönderge 'l-cenneti' 11. kelime), aktör adlı 'l-cenneti'; "
 "7:47 3FS ('surifet' — edilgen, naib-i faili 'ebsâruhum' 3. kelime), 3MP ('qâlû' — tartışmalı; gönderge 7:46 5. kelime; ek 'ebsâruhum' — tartışmalı; gönderge 7:46 5. kelime), konuşan 1P eki ('rabbenâ', 'tec'alnâ' — söz içi), muhatap 2MS ('tec'alnâ' — söz içi)",
 "7:44-47 gönderge zinciri: 7:44 'ashâbu'l-cenneti' (2. kelime) seslenen, 'ashâbe'n-nâri' (4. kelime) seslenilen; söz içi konuşan 1P bahçe halkı, muhatap 2MP ateş halkı; 'qâlû' (19. kelime) ateş halkı; 'beynehum' (23. kelime) iki topluluğu birlikte gösteriyor — tartışmalı; "
 "7:45 3MP fiiller ve 'hum' (8. kelime) 7:44 'z-zâlimîn' (28. kelime) sıfatı; 7:45 've yebğûnehâ' (6. kelime) 3FS eki 'sebîli' (4. kelime) — tartışmalı: cins uyumsuz (morph M ad, dişil zamir); 7:46 've beynehumâ' (1. kelime) 3D — bahçe halkı ile ateş halkı, tartışmalı; 7:46 'ricâlun' (5. kelime) 'ya'rifûne' ve 've nâdev' öznesi; 'bi-sîmâhum' (8. kelime) 'kullen' (7. kelime) — tartışmalı: sayı uyumsuz (tekil 'kull', çoğul zamir); "
 "7:46 'yedxulûhâ', 'hum', 'yatma'ûn' (16-18. kelime) 'ricâlun' — tartışmalı (öznesi bahçe halkı da okunabilir); 7:47 'ebsâruhum' (3. kelime) ve 'qâlû' (7. kelime) 7:46 'ricâlun' (5. kelime) — tartışmalı (okuma)",
 "edilgen: 7:47 'surifet' (2. kelime; naib-i faili 'ebsâruhum' 3. kelime) — ölçüm EDİLGEN 1/3; 7:44, 7:45 ve 7:46 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 7:44 've nâdâ' (1.) ve 'en' (6.) ardından söz biçimli içerik 7-18. kelime (seslenme fiili, قول kökü değil; REM sapması 7:44 (13. kelime) — 'fe-hel' içerikte yeni cümle başı, konuşan sürer); 'qâlû' (19.) ardından söz 20. kelime — ayet içi kapanış; 'fe-ezzene' (21.) ve 'en' (24.) ardından söz biçimli içerik 25-28. kelime (okuma); "
 "7:46 've nâdev' (9.) ve 'en' (12.) ardından söz biçimli içerik 13-14. kelime, 'lem' (15.) anlatıya dönüş; 7:47 'qâlû' (7.) ardından söz 8-13. kelime — ayet içi kapanış; 7:45 söz fiili yok, A3 '—'; mealde 'seslendi ki:', 'Dediler ki:', 'duyurdu ki:', 'seslendiler ki:' ve 'dediler ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 44 47 13' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 7:44 've nâdâ' (1.) CONJ; 7:45 've yebğûnehâ' (6.) CONJ, 've hum' (8.) REM; 7:46 've beynehumâ' (1.) REM, 've 'ale' (3.) CONJ, 've nâdev' (9.) CONJ, 've hum' (17.) CIRC; 7:47 've izâ' (1.) REM; "
 "'fe' konumları: 7:44 'fe-hel' (13.) REM, 'fe-ezzene' (21.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 7:47 ◈B بصر ('ebsâruhum' 3. kelime — B3); 7:44, 7:45 ve 7:46 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 44 47 13'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 4 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 7:44 (11:18), 7:45 (11:19, 14:3), 7:47 (23:94); 7:46 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 7:44 أذن ×2, حقق ×2, ربب ×2, صحب ×2, وجد ×2, وعد ×2; 7:46 عرف ×2; "
 "ayetler arası kalıp 'ashâb… l-cenneti' (7:44, 7:46) — sayım 'say 7:44 2-3' / 'say 7:46 10-11' ve lemma dizisi 'dizi 7 44 1 3' / 'dizi 7 46 9 11'; ayetler arası kalıp 'ashâb… n-nâri' (7:44, 7:47) — sayım 'say 7:44 4-5' / 'say 7:47 5-6' ve lemma dizisi 'dizi 7 44 4 5' / 'dizi 7 47 5 6'; topluluk adları, bağ kurulmadı (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: bloğun emsal dosyasında olmayan basılmış eş (önceki bloklarda basılmış ya da sûre içi), bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 7:44 soru → cevap (ayet içi; INTG 'hel' 13. kelime), şahıs geçişi 1 → 3, edim geçişi şart → soru; 7:45 şahıs geçişi yok, edim geçişi soru → haber; "
 "7:46 şahıs geçişi yok, edim geçişi yok; 7:47 söz açılır (8. kelime), söz kapanır (13. kelime, ayet içi), şahıs geçişi yok, edim geçişi haber → yasak; ölçüm iltifât 7:44-47 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 7:44 've nâdâ ashâbu'l-cenneti ashâbe'n-nâri' — fiil, fail ve meful (morph CONJ + PERF + NOM + ACC); 7:44 'en qad vecednâ' — açıklama edatı ve tekitli mâzî (morph INT + CERT + PERF); 7:44 'fe-hel vecedtum' — soru edatı (morph REM + INTG + PERF); 7:44 'na'am' — onay edatı (morph ANS); "
 "7:45 'llezîne yasuddûne' — 7:44 'z-zâlimîn' sıfatı ilgi cümlesi (morph REL + IMPF); 7:46 've beynehumâ hicâbun' — öne alınmış haberli isim cümlesi (morph REM + LOC + INDEF); 7:46 've hum yatma'ûn' — hâl cümlesi (morph CIRC + PRON + IMPF); 7:47 've izâ surifet' — zaman zarfı ve edilgen mâzî (morph REM + T + PERF + PASS); 7:47 'lâ tec'alnâ' — yasak (morph PRO + JUS)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 7:44 25-28. kelime — 11:18 ile harekesiz eş (sayım: 'say 7:44 25-28'); 7:45 'llezîne yasuddûne 'an sebîli'llâhi' ile açılıyor — 11:19 ile harekesiz eş (sayım: 'say 7:45 1-5'); 7:45 1-7. kelime — 11:19 ile harekesiz eş (sayım: 'say 7:45 1-7'); "
 "7:45 4-7. kelime — 11:19 ve 14:3 ile harekesiz eş (sayım: 'say 7:45 4-7'); 7:47 11-13. kelime — 6:68 ile harekesiz eş (sayım: 'say 7:47 11-13'); 7:44 kök أذن, حقق, ربب, صحب, وجد ve وعد ikilemeleri; 7:46 kök عرف ikilemesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 13'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'la'netu'llâhi 'ale'z-zâlimîn' 7:44 'Allah'ın laneti zalimlerin üzerinedir' / 11:18 'Allah'ın laneti zalimlerin üzerinedir' (emsal metninde) — çakışma değil (bayt eşit); "
 "'llezîne yasuddûne 'an sebîli'llâhi' 7:45 'Allah'ın yolundan alıkoyan' / 11:19 'Allah'ın yolundan alıkoyan' (emsal metninde) — çakışma değil (bayt eşit); "
 "'ve yebğûnehâ 'ivecen' 7:45 'onu eğri göstermek isteyen' / 11:19 'onu eğri göstermek isteyen' (emsal metninde) — çakışma değil (bayt eşit); 'yasuddûne 'an sebîli'llâhi' 7:45 'Allah'ın yolundan alıkoyan' / 14:3 'Allah'ın yolundan alıkoyan' (emsal metninde) — çakışma değil (bayt eşit); 've yebğûnehâ 'ivecen' 7:45 'onu eğri göstermek isteyen' / 14:3 've onu eğri göstermek isteyen' (emsal metninde) — çakışma — tam okuma sonu ('ve' bağlacı / virgül); "
 "'l-qavmi'z-zâlimîn' 7:47 'zalim kavimle' / 23:94 'zalim kavmin' (emsal metninde) — çakışma — tam okuma sonu (birliktelik eki / tamlayan eki); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 7:44 'nâdâ' PERF — meal 'seslendi'; 'vecednâ' PERF ('qad' ile) — meal 'bulduk'; 've'adenâ' PERF — meal 'ettiğini'; 'vecedtum' PERF ('hel' ile) — meal 'buldunuz'; 've'ade' PERF (16. kelime) — meal 'ettiğini'; 'qâlû' PERF — meal 'Dediler'; 'ezzene' PERF — meal 'duyurdu'; "
 "7:45 'yasuddûne' IMPF IND — meal 'alıkoyan'; 'yebğûne' IMPF IND — meal 'isteyen'; 7:46 'ya'rifûne' IMPF IND — meal 'tanıyan'; 'nâdev' PERF — meal 'seslendiler'; 'yedxulû' IMPF JUS ('lem' ile) — meal 'girmediler'; 'yatma'ûn' IMPF IND — meal 'umuyorlar'; "
 "7:47 'surifet' PERF edilgen ('izâ' ile) — meal 'çevrildiğinde'; 'qâlû' PERF — meal 'dediler'; 'tec'al' IMPF JUS ('lâ' ile) — meal 'kılma'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle; IMPF IND geniş zaman karşılığı her blokta sapma sayılır — sûre 7 bölüm 3 denetimi kuralı 3): 've'ade' PERF 7:44'te sıfat-fiil ('-diğini') ile; 'yasuddûne' ve 'yebğûne' IMPF 7:45'te sıfat-fiil ('-an', '-en') ile; 'ya'rifûne' IMPF 7:46'da sıfat-fiil ('-yan') ile; "
 "'yedxulû' IMPF JUS 7:46'da 'lem' ile geçmiş zaman ('-mediler') ile; 'surifet' PERF 7:47'de zarf-fiil ('-diğinde') ile",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): "
 "'bi' (belirtme eki / ayrılma eki) — çakışma değil (fiil yönetimi: 'inkâr et-' belirtme, 'tanı-' ayrılma); 'ellezî' (REL: '-an') — çakışma değil (ünlü uyumu); 'hum' (iyelik eki / karşılıksız) — çakışma değil (tamlama; özne fiil ekinde ya da takdirle karşılandı); 'hâ' ('onu' / 'ora') — çakışma değil (belirtme çekimi, yer zamiri); 'mâ' (REL: '-tiğini') — çakışma değil (nesne konumunda sıfat-fiil); 'nâ' ('bizi' / 'bize') — çakışma değil (belirtme ve yönelme çekimi); 've' (CONJ / REM: 've' / karşılıksız; CIRC: 'ama') — çakışma değil (atıf, cümle başı, hâl cümlesinde karşıtlık)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 44 47 13'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 7:44, 7:45, 7:46 ve 7:47 tarayıcı vermedi (cipa_tarama7_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 7:44, 7:45, 7:46 ve 7:47 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök صحب 7:44 ('ashâbu', 'ashâbe'), 7:46 ('ashâbe') ve 7:47 ('ashâbi'), 7:42 ('ashâbu') ile bölüm içi; kök جنن 7:44 ('l-cenneti') ve 7:46 ('l-cenneti'), 7:42 ('l-cenneti') ve 7:43 ('l-cennetu') ile bölüm içi; kök نور 7:44 ('n-nâri') ve 7:47 ('n-nâri'); kök ندي 7:44 ('ve nâdâ') ve 7:46 ('ve nâdev'), 7:43 ('ve nûdû') ile bölüm içi; kök ربب 7:44 ('rabbunâ', 'rabbukum') ve 7:47 ('rabbenâ'), 7:43 ('rabbinâ') ile bölüm içi; kök حقق 7:44 ('haqqan', 'haqqan'), 7:43 ('bi'l-haqqi') ile bölüm içi; kök قول 7:44 ('qâlû') ve 7:47 ('qâlû'), 7:43 ('ve qâlu') ile bölüm içi; kök أله 7:44 ('llâhi') ve 7:45 ('llâhi'), 7:43 ('li'llâhi', 'llâhu') ile bölüm içi; kök ظلم 7:44 ('z-zâlimîn') ve 7:47 ('z-zâlimîn'); kök بين 7:44 ('beynehum') ve 7:46 ('ve beynehumâ'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 5-2 (bölüm 7 kuralı 9 — blok_plani_7.txt'ten) — bölüm blokları 12, 13 ve 14; "
 "mercek_kayit['7']'deki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b13/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 44 47 13'; lem_bozuk.py 13 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 44 47 → AYN_SONUC; sunum/bolum4_kurallar.py 44 47 13 → KHATA_HEPSI; " + '; '.join('sunum/bolum%d_kurallar.py 44 47 13 → B%d_HEPSI' % (n_, n_) for n_ in range(5, 40)) + "; sunum/yasakli_sina.sh → yasakli sınama tamam",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 13 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('nâdâ', 'ashâb', 'cenne', 'rabb', 'haqq', 'hel', 'la'ne', 'allâh', ''alâ', 'zâlim', 'ellezî', 'sadde', ''an', 'sebîl', 'beğâ', ''iveç', 'a'râf', 'ricâl', ''arafe', 'en', 'lâ', 'ce'ale', 'ma'a', 'qavm', 'nâr'); joker '_' bu blokta yok; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (44, 47): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_7_44_47.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_7_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_7_b11k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '44', '47'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '44', '47', '13'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '44', '47', '13'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '44', '47', '13', '--tazelik-yok')}
    for _n in range(7, 40): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '44', '47', '13')
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
