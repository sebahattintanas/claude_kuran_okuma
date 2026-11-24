# sûre 6 blok 40 (6:161-165) ARIZA oluşturucu — bölüm 19-2
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b40/olcum.txt'
os.environ['SAY2'] = '/home/claude/b40/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = []
VF_YAZI_ESKI = {}
BOL = "'Bekledikleri; dosdoğru din; yeryüzünün halifeleri'"


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
 ("6:161", "'kâne min muşrik'", 2, 'say 6:161 14-16', "harekesiz 'kâne mine'l-muşrikîn' (14-16. kelime)", ('dizi 6 161 14 16', "kâne min muşrik", '14-16', "biçim farkı (dizi 6 161 14 16): 6:14 fiil çekimi")),
 ("6:161", "'ilâ sırât mustaqîm'", 2, 'say 6:161 5-7', "harekesiz 'ilâ sırâtin mustaqîmin' (5-7. kelime)", ('dizi 6 161 5 7', "ilâ sırât mustaqîm", '5-7', "biçim farkı (dizi 6 161 5 7): 6:87 yazım eş")),
 ("6:162", "'allâh rabb 'âlem'", 2, 'say 6:162 7-9', "harekesiz 'lillâhi rabbi'l-'âlemîn' (7-9. kelime)", ('dizi 6 162 7 9', "allâh rabb 'âlem", '7-9', "biçim farkı (dizi 6 162 7 9): 6:45 yazım eş")),
 ("6:164", "'summe ilâ rabb merci' nebbe'e mâ kâne'", 2, 'say 6:164 21-27', "harekesiz 'summe ilâ rabbikum merci'ukum fe-yunebbi'ukum bimâ kuntum' (21-27. kelime)", ('dizi 6 164 21 27', "summe ilâ rabb merci' nebbe'e mâ kâne", '21-27', "biçim farkı (dizi 6 164 21 27): 6:108 fiil çekimi, zamir eki")),
 ("6:164", "'nebbe'e mâ kâne'", 4, 'say 6:164 25-27', "harekesiz 'fe-yunebbi'ukum bimâ kuntum' (25-27. kelime)", ('dizi 6 164 25 27', "nebbe'e mâ kâne", '25-27', "biçim farkı (dizi 6 164 25 27): 6:60 önek; 6:108 fiil çekimi, zamir eki; 6:159 fiil çekimi, zamir eki, önek")),
 ("6:164", "'summe ilâ rabb'", 3, 'say 6:164 21-23', "harekesiz 'summe ilâ rabbikum' (21-23. kelime)", ('dizi 6 164 21 23', "summe ilâ rabb", '21-23', "biçim farkı (dizi 6 164 21 23): 6:38 zamir eki; 6:108 zamir eki")),
 ("6:164", "'qâle ğayr allâh'", 2, 'say 6:164 1-3', "harekesiz 'qul e-ğayra'llâhi' (1-3. kelime)", ('dizi 6 164 1 3', "qâle ğayr allâh", '1-3', "biçim farkı (dizi 6 164 1 3): 6:14 yazım eş")),
 ("6:164", "'rabb kull şey''", 2, 'say 6:164 7-9', "harekesiz 'rabbu kulli şey'' (7-9. kelime)", ('dizi 6 164 7 9', "rabb kull şey'", '7-9', "biçim farkı (dizi 6 164 7 9): 6:80 zamir eki")),
 ("6:165", "'_ ellezî ce'ale'", 2, 'say 6:165 1-3', "harekesiz 've huve'llezî ce'alekum' (1-3. kelime)", ('dizi 6 165 1 3', "_ ellezî ce'ale", '1-3', "biçim farkı (dizi 6 165 1 3): 6:97 zamir eki")),
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

VF_YAZI = {161: {13: "'ve mâ'"}, 162: {4: "'ve nusukî'", 5: "'ve mahyâye'", 6: "'ve memâtî'"}, 163: {4: "'ve bi-zâlike'", 6: "'ve ene'"}, 164: {6: "'ve huve'", 10: "'ve lâ'", 16: "'ve lâ'"}, 165: {1: "'ve huve'", 6: "'ve refe'a'", 19: "'ve innehû'"}}
sys.path.insert(0, '/home/claude/b40/yap')
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
open('/home/claude/b40/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '40')
BLOKLAR = [str(i) for i in range(1, 41)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '40', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b40/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '161', '165', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b40/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b40/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '161', '165', '40').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_161_165.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:161', '6:162', '6:163', '6:164', '6:165'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_161_165.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(161, 166))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:164 kök نفس ('nefsin' 13. kelime — can), kök أخر ('uxrâ' 20. kelime — başka)"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '161', '165', '40')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b40/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 41)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(161, 166))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 18 kapanışında sunum/bolum34_kurallar.py eklendi (kural 1-5); blok 39'da yasaklı tarama aracının Türkçe ikileme listesine 'bölük bölük' eklendi; bu blokta sunum/bolum16_kurallar.py kural 1 fail aramasını morph ACC edatında ('inne') keser (6:165 14. kelime yanlış isabeti), sunum/yasakli.sh IZIN'e ('ariza_6_161_165.txt', 'ilk, evvel') çifti — bölüm 10 denetimi kuralı 10: kök anlamı araç çıktısı aynen (blok 3 ve blok 6 emsali); yeni kök yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 351",
 "geriye dönük koşu (bölüm 18 kapanışı, komut 'python3 sunum/geriye_donuk.py b38k yamalar/geriye_donuk_6_b36k.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 161 165 40'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:163 'evvelu'l-muslimîn' (7-8. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge); 6:165 've innehû le-ğafûrun rahîm' (19-21. kelime) — esma_el 'ilahi', kural ''inne/enne' haberi' (Rab) ve 'rahîm' (21. kelime) için kural ''inne/enne' haberi' (Rab; morph ADJ ile 'ğafûr'un sıfatı) (yamalar/esma_el_6_161_165.txt); غَفُور ve رَحِيم lemmalarında önceki 'ilahi' kayıtlarıyla karar eş; 6:161, 6:162 ve 6:164 esmâ yok; 6:161 Rab (4. kelime), 6:162 lafız (7. kelime) ve Rab (8. kelime), 6:164 lafız (3. kelime) ve Rab (5., 7. ve 23. kelime), 6:165 Rab (16. kelime); 6:163 lafız ve Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 161 165 40'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5; 6:163 muhur EVET / ölçüm esmâ yok — uyuşmuyor, araç tanımı farkı; 6:163 e_oto 1 (أَوَّل) / ölçüm esmâ yok — liste farkı; 6:165 esma_kayit 'mühür EVET (ÇİFT)' — ölçüm MÜHÜR ile uyuşuyor, muhur_el EVET): " + EMH,
 "ölçüm: 6:161 '{{1|aktör: adlı إِبْراهِيم 11\\. sırada \\(kisi, rol mecrur\\)}}', '{{1|fâsıla ٱلمشركين → ن, N sınıfı}}', '{{1|harf 70 → harf3 64, isaret 6}}' ve '{{1|dış düğüm 1}}'; "
 "6:162 '{{2|fâsıla ٱلعلمين → ن, N sınıfı}}', '{{2|harf 38 → harf3 38, isaret 0}}' ve '{{2|dış düğüm 0}}'; "
 "6:163 '{{3|aktör: adlı مُسْلِم 8\\. sırada \\(cins, rol mecrur\\)}}', '{{3|EDİLGEN 1/1 fiil, pas z=5,38}}', '{{3|fâsıla ٱلمسلمين → ن, N sınıfı}}', '{{3|simetri \\[3, 1, 4, 1\\]}}', '{{3|harf 35 → harf3 32, isaret 3}}' ve '{{3|dış düğüm 0}}'; "
 "6:164 '{{4|fâsıla تختلفون → ن, N sınıfı}}', '{{4|simetri \\[3, 6, 10, 1\\]}}', '{{4|harf 110 → harf3 104, isaret 6}}', '{{4|dış düğüm 6}}' ve '{{4|İÇ düğüm 2}}'; "
 "6:165 '{{5|esmâ غَفُور 20\\. sırada, SON konum, MÜHÜR \\| رَحِيم 21\\. sırada, SON konum, MÜHÜR}}', '{{5|fâsıla رحيم → م, N sınıfı}}', '{{5|simetri \\[3, 1, 12, 1\\]}}', '{{5|harf 91 → harf3 85, isaret 6}}' ve '{{5|dış düğüm 3}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi, iki araç 0); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 161 165 40'): KALAN_P",
 "ölçüm aktör: 6:161 adlı إِبْراهِيم 11. sırada ('ibrâhîme'; kisi, rol mecrur); 6:163 adlı مُسْلِم 8. sırada ('l-muslimîn'; cins, rol mecrur); 6:162, 6:164 ve 6:165 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:161 emir — IMPV 1 'qul' (1.), NEG 1 'mâ' (13.); 6:162 emir — IMPV 1 'qul' (1.); 6:163 haber — NEG 1 'lâ' (1.); "
 "6:164 soru, emir — IMPV 1 'qul' (1.), INTG 1 'e-ğayra' (2.), NEG 2 'lâ' (10.), 'lâ' (16.); ölçüm biçim ISTISNA (D2'de yazılmadı); 6:165 haber — EMPH 1 'le-ğafûrun' (20.); "
 "morph ACC ('innenî' 6:161 2., 'inne' 6:162 2., 'inne' 6:165 15., 'innehû' 6:165 19.), CIRC ('ve mâ' 6:161 13.), REM ('ve bi-zâlike' 6:163 4., 've ene' 6:163 6., 've huve' 6:164 6., 'fe-yunebbi'ukum' 6:164 25.), EXP ('illâ' 6:164 14.), PRP ('li-yebluvekum' 6:165 11.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:161 yıldız yok; 6:162 ★★ (kaynak rab, z=2,05; eşiği geçen öbür ölçüler allah z=1,69); 6:163 ★★★ (kaynak pas, z=5,38); 6:164 ★ (kaynak rab, z=1,88; eşiği geçen öbür ölçüler n z=1,76); 6:165 yıldız yok",
 "fâsıla: 6:160 ن → 6:161 ن (ٱلمشركين) → 6:162 ن (ٱلعلمين) → 6:163 ن (ٱلمسلمين) → 6:164 ن (تختلفون) → 6:165 م (رحيم) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:161 okunmuş 1 ayet; 6:162 xref yok; 6:163 xref yok; 6:164 5:48 (emsal olarak basıldı), 6:14 (basılmış), 6:108 (basılmış), 13:42 (emsal olarak basıldı), 39:7 (basılmış), okunmuş 2 ayet ve okunmamış 1 ayet; 6:165 43:32 (emsal olarak basıldı), okunmuş 1 ayet ve okunmamış 1 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:161 'kâne min muşrik' süzgeç GEÇMEZ, 'ilâ sırât mustaqîm' süzgeç GEÇMEZ; 6:162 'allâh rabb 'âlem' süzgeç GEÇMEZ; 6:164 'summe ilâ rabb merci' nebbe'e mâ kâne' süzgeç GEÇER, 'nebbe'e mâ kâne' süzgeç GEÇER, 'summe ilâ rabb' süzgeç GEÇER, 'qâle ğayr allâh' süzgeç GEÇMEZ, 'rabb kull şey'' süzgeç GEÇMEZ; 6:165 '_ ellezî ce'ale' süzgeç GEÇMEZ; 6:163 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; ekler fiillerden ayrı grupta — bölüm 16 ve 17 denetimi A1_EK_AYRIMI): "
 "6:161 muhatap 2MS ('qul'), konuşan 1S eki ('innenî', 'hedânî', 'rabbî' — söz içi), 3MS ('hedânî' — söz içi, fiil uyumu, fail 4. kelime; 'kâne' — söz içi, gönderge 'ibrâhîme' 11. kelime), aktör adlı 'ibrâhîme'; "
 "6:162 muhatap 2MS ('qul'), konuşan 1S eki ('salâtî', 'nusukî', 'mahyâye', 'memâtî' — söz içi); "
 "6:163 3MS ('leh' — söz içi, gönderge 6:162 7. kelime), konuşan 1S ('umirtu' — söz içi, edilgen, naib-i faili konuşan; 'ene' — söz içi), aktör adlı 'l-muslimîn'; "
 "6:164 muhatap 2MS ('qul'), konuşan 1S ('ebğî' — söz içi), 3MS ('huve' — söz içi, gönderge 'llâhi' 3. kelime; 'fe-yunebbi'ukum' — söz içi, gönderge 'rabbikum' 23. kelime; 'fîhi' eki — söz içi, gönderge 'bimâ' 26. kelime), 3FS ('teksibu', 'teziru' — söz içi, fiil uyumu, fail 12. ve 18. kelime; ''aleyhâ' eki — söz içi, gönderge 'nefsin' 13. kelime), "
 "muhatap 2MP ('kuntum', 'taxtelifûn' — söz içi; ekler 'rabbikum', 'merci'ukum', 'fe-yunebbi'ukum' — söz içi); "
 "6:165 3MS ('huve' — gönderge 6:164 23. kelime; 'ce'alekum', 'refe'a', 'li-yebluvekum', 'âtâkum' — gönderge 'llezî' 2. kelime; 'innehû' eki — gönderge 'rabbeke' 16. kelime), muhatap 2MP eki ('ce'alekum', 'ba'dakum', 'li-yebluvekum', 'âtâkum'), muhatap 2MS eki ('rabbeke')",
 "6:161-165 gönderge zinciri: 6:161, 6:162 ve 6:164 'qul' (1. kelime) muhatabı muhatap 2MS (adsız), sözlerde konuşan 1S; 6:162 sözü 6:163 sonuna dek sürer; 6:164 sözünde muhatap 2MP'ye geçiş (23. kelime); 6:165 söz dışı, muhatap 2MP ardından muhatap 2MS (16. kelime) (okuma)",
 "edilgen: 6:163 'umirtu' (5. kelime; naib-i faili konuşan) — ölçüm EDİLGEN 1/1; 6:161, 6:162, 6:164 ve 6:165 edilgen fiil yok",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:161 'qul' (1.) ardından söz 2-16. kelime, ayet sonunda kapanır; 6:162 'qul' (1.) ardından söz 2-9. kelime, ayet sonunda kapanmaz; 6:163 söz 6:162 2. kelimeden sürer ve 8. kelimede kapanır; "
 "6:164 'qul' (1.) ardından söz 2-29. kelime, ayet sonunda kapanır; 6:165 söz yok (okuma); mealde 'De ki:' ardından tırnaksız (blok meal biçimi); "
 "REM sapması 6:163 (4. kelime) — 've bi-zâlike' söz içinde, söz 6:162 2. kelimeden sürüyor ('umirtu' 1S); REM sapması 6:163 (6. kelime) — 've ene' söz içinde, konuşan 1S; REM sapması 6:164 (6. kelime) — 've huve' söz içinde, göndergesi söz içi lafız (3. kelime); REM sapması 6:164 (25. kelime) — 'fe-yunebbi'ukum' söz içinde, muhatap 2MP sözün muhatabı (okuma); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 161 165 40' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:161 've mâ' (13.) CIRC; 6:162 've nusukî' (4.), 've mahyâye' (5.), 've memâtî' (6.) CONJ; 6:163 've bi-zâlike' (4.), 've ene' (6.) REM; 6:164 've huve' (6.) REM, 've lâ' (10.), 've lâ' (16.) CONJ; 6:165 've huve' (1.), 've refe'a' (6.), 've innehû' (19.) CONJ; "
 "'fe' konumları: 6:164 'fe-yunebbi'ukum' (25.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:162 ◈B حيي ('mahyâye' 5. kelime — B4), 6:162 ◈B موت ('memâtî' 6. kelime — B4); 6:165 ◈K أرض ('l-ardi' 5. kelime — K1); 6:161, 6:163 ve 6:164 tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 161 165 40'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:164 (5:48, 13:42); 6:165 (5:48, 43:32); 6:161, 6:162 ve 6:163 bağ yok; D3'te ölçüm kök ikilemeleri (bölüm 17 denetimi D3_KOK_IKILEME): 6:161 قوم ×2; 6:164 ربب ×3, كلل ×2, وزر ×3; 6:165 بعض ×2; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11)",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:161 söz açılır (2. kelime), söz kapanır (16. kelime, ayet içi), şahıs geçişi 3 → 1, edim geçişi şart → emir; 6:162 söz açılır (2. kelime), şahıs geçişi yok, edim geçişi yok; 6:163 söz kapanır (8. kelime), şahıs geçişi yok, edim geçişi emir → haber; "
 "6:164 söz açılır (2. kelime), söz kapanır (29. kelime, ayet içi), muhatap geçişi 2MS → 2MP (ayet içi), şahıs geçişi 1 → 2, edim geçişi haber → soru, emir; 6:165 muhatap geçişi 2MP → 2MS (ayet içi), şahıs geçişi 2 → 3, edim geçişi soru, emir → haber; bölüm kapanışı; sûre kapanışı; "
 "ölçüm iltifât 6:161-165 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:161 'dînen qiyemen' — bedel okuması (morph ACC); 6:161 've mâ kâne mine'l-muşrikîn' — hâl (morph CIRC); 6:164 'e-ğayra'llâhi ebğî rabben' — soru (morph INTG); 6:164 've huve rabbu kulli şey'' — karşıtlık cümlesi (morph REM); "
 "6:164 've lâ teksibu kullu nefsin illâ 'aleyhâ' — olumsuzluk ve istisna (morph CONJ + NEG + EXP); 6:165 'li-yebluvekum' — gerekçe lâmı (morph PRP); 6:165 've innehû le-ğafûrun rahîm' — pekiştirme (morph CONJ + ACC + EMPH)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:164 11-13. kelime — 13:42 ile harekesiz eş (sayım: 'say 6:164 11-13'); 6:164 25-29. kelime — 5:48 ile harekesiz eş (sayım: 'say 6:164 25-29'); "
 "6:165 8-10. kelime — 43:32 ile harekesiz eş (sayım: 'say 6:165 8-10'); 6:165 11-14. kelime — 5:48 ile harekesiz eş (sayım: 'say 6:165 11-14'); 6:161 kök قوم ikilemesi; 6:164 kök ربب, كلل, وزر ikilemeleri; 6:165 kök بعض ikilemesi",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 40'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'teksibu kullu nefsin' 6:164 'Her can kazandığını yalnızca kendi aleyhine kazanır' / 13:42 'Her nefsin ne kazandığını bilir' (emsal metninde) — çakışma — tam okuma sonu ('can' / 'nefis' bağlam karşılığı); "
 "'fe-yunebbi'ukum bimâ kuntum fîhi taxtelifûn' 6:164 'içinde ayrılığa düşmüş olduğunuz şeyi size haber verecek' / 5:48 'içinde ayrılığa düşmüş olduğunuz şeyi size haber verecek' (emsal metninde) — çakışma değil (bayt eşit); "
 "'fe-yunebbi'ukum bimâ kuntum' 6:164 'içinde ayrılığa düşmüş olduğunuz şeyi size haber verecek' / 5:48 'içinde ayrılığa düşmüş olduğunuz şeyi size haber verecek' (emsal metninde) — çakışma değil (bayt eşit); "
 "'fevqa ba'din deracâtin' 6:165 'kiminizi kiminizin üstüne derecelerle yükseltti' / 43:32 'kimini kiminden derecelerle üstün kıldık' (emsal metninde) — çakışma — tam okuma sonu ('üstüne … yükselt-' / 'üstün kıl-' bağlam karşılığı); "
 "'li-yebluvekum fî mâ âtâkum' 6:165 'size verdiğinde sizi sınamak için' / 5:48 'size verdiğinde sizi sınamak için' (emsal metninde) — çakışma değil (bayt eşit); 'fî mâ' 6:165 'size verdiğinde' / 5:48 'size verdiğinde' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil; yinelenen fiil kelime numarasıyla — sûre 6 bölüm 18 denetimi kuralı 4): 6:161 'qul' IMPV — meal 'De'; 'hedâ' PERF — meal 'iletti'; 'kâne' PERF ('mâ' ile) — meal 'değildi'; 6:162 'qul' IMPV — meal 'De'; 6:163 'umirtu' PERF PASS — meal 'emredildi'; "
 "6:164 'qul' IMPV — meal 'De'; 'ebğî' IMPF IND — meal 'arayayım'; 'teksibu' IMPF IND ('lâ' ile) — meal 'kazanır'; 'teziru' IMPF IND ('lâ' ile) — meal 'taşımaz'; 'yunebbi'u' IMPF IND — meal 'verecektir'; 'kuntum' PERF — meal 'olduğunuz'; 'taxtelifûn' IMPF IND — meal 'düşmüş'; "
 "6:165 'ce'ale' PERF — meal 'kılan'; 'refe'a' PERF — meal 'yükseltti'; 'yebluve' IMPF SUBJ ('li' ile) — meal 'sınamak'; 'âtâ' PERF — meal 'verdiğinde'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'ebğî' IMPF IND 6:164'te istek kipi ('-yayım') ile; 'ce'ale', 'âtâ' PERF 6:165'te sıfat-fiil ('-an', '-diği') ile; 'kuntum' PERF 6:164'te sıfat-fiil ('-duğunuz') ile; 'taxtelifûn' IMPF 6:164'te geçmiş ortaç ('-müş') ile ('kuntum' ile birlikte)",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok') + "; bölüm içi eş edat (bölüm 12 denetimi kuralı 3): 'summe' ('Sonra' / 'sonra') — çakışma değil (büyük harf, cümle başı); 'illâ' ('yalnızca' / 'başka') — çakışma değil (olumsuz ve soru hasr açılımı)",
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 161 165 40'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:161-164 tarayıcı vermedi (cipa_tarama6_adaylari.json); 6:165 tarayıcı adayı (kök أرض; B_ta’lîl) çıpa değil — sınama gerekçesi, ölçü / mekanizma yok; L3 / L4 adayı yok",
 "aday 1039: 6:162 ('mahyâye' / 'memâtî'); 6:161, 6:163, 6:164 ve 6:165 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök قول 6:161 ('qul'), 6:162 ('qul') ve 6:164 ('qul'), 6:158 ('quli') ile bölüm içi; kök ربب 6:161 ('rabbî'), 6:162 ('rabbi'), 6:164 ('rabben', 'rabbu', 'rabbikum') ve 6:165 ('rabbeke'), 6:158 ('rabbuke', 'rabbik', 'rabbike') ile bölüm içi; kök شرك 6:161 ('l-muşrikîn') ve 6:163 ('şerîke'); kök أله 6:162 ('lillâhi') ve 6:164 ('llâhi'), 6:159 ('llâhi') ile bölüm içi; "
 "kök كون 6:161 ('kâne') ve 6:164 ('kuntum'), 6:158 ('tekun') ve 6:159 ('kânû', 'kânû') ile bölüm içi; kök خلف 6:164 ('taxtelifûn') ve 6:165 ('xalâ'ife'); kök دين 6:161 ('dînen'), 6:159 ('dînehum') ile bölüm içi; kök أمر 6:163 ('umirtu'), 6:159 ('emruhum') ile bölüm içi; kök نبأ 6:164 ('fe-yunebbi'ukum'), 6:159 ('yunebbi'uhum') ile bölüm içi; "
 "kök كسب 6:164 ('teksibu'), 6:158 ('kesebet') ile bölüm içi; kök نفس 6:164 ('nefsin'), 6:158 ('nefsen') ile bölüm içi; kök أتي 6:165 ('âtâkum'), 6:158 ('te'tiyehumu', 'ye'tiye', 'ye'tiye', 'ye'tî') ile bölüm içi; kök بعض 6:165 ('ba'dakum', 'ba'din'), 6:158 ('ba'du', 'ba'du') ile bölüm içi; kök شيأ 6:164 ('şey''), 6:159 ('şey'') ile bölüm içi; okuma",
 "bölüm: " + BOL + " bölümü, bölüm 19-2 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 39 ve 40; bölüm kapanışı ve sûre kapanışı bu blokta; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b40/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 161 165 40'; lem_bozuk.py 40 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 161 165 → AYN_SONUC; sunum/bolum4_kurallar.py 161 165 40 → KHATA_HEPSI; sunum/bolum5_kurallar.py 161 165 40 → B5_HEPSI; sunum/bolum6_kurallar.py 161 165 40 → B6_HEPSI; sunum/bolum7_kurallar.py 161 165 40 → B7_HEPSI; sunum/bolum8_kurallar.py 161 165 40 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 161 165 40 → B9_HEPSI; sunum/bolum10_kurallar.py 161 165 40 → B10_HEPSI; sunum/bolum11_kurallar.py 161 165 40 → B11_HEPSI; sunum/bolum12_kurallar.py 161 165 40 → B12_HEPSI; sunum/bolum13_kurallar.py 161 165 40 → B13_HEPSI; sunum/bolum14_kurallar.py 161 165 40 → B14_HEPSI; sunum/bolum15_kurallar.py 161 165 40 → B15_HEPSI; sunum/bolum16_kurallar.py 161 165 40 → B16_HEPSI; sunum/bolum17_kurallar.py 161 165 40 → B17_HEPSI; sunum/bolum18_kurallar.py 161 165 40 → B18_HEPSI; sunum/bolum19_kurallar.py 161 165 40 → B19_HEPSI; sunum/bolum20_kurallar.py 161 165 40 → B20_HEPSI; sunum/bolum21_kurallar.py 161 165 40 → B21_HEPSI; sunum/bolum22_kurallar.py 161 165 40 → B22_HEPSI; sunum/bolum23_kurallar.py 161 165 40 → B23_HEPSI; sunum/bolum24_kurallar.py 161 165 40 → B24_HEPSI; sunum/bolum25_kurallar.py 161 165 40 → B25_HEPSI; sunum/bolum26_kurallar.py 161 165 40 → B26_HEPSI; sunum/bolum27_kurallar.py 161 165 40 → B27_HEPSI; sunum/bolum28_kurallar.py 161 165 40 → B28_HEPSI; sunum/bolum29_kurallar.py 161 165 40 → B29_HEPSI; sunum/bolum30_kurallar.py 161 165 40 → B30_HEPSI; sunum/bolum31_kurallar.py 161 165 40 → B31_HEPSI; sunum/bolum32_kurallar.py 161 165 40 → B32_HEPSI; sunum/bolum33_kurallar.py 161 165 40 → B33_HEPSI; sunum/bolum34_kurallar.py 161 165 40 → B34_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta 'ariza_6_161_165.txt' için 'ilk, evvel' eklendi",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 40 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; 6:161, 6:164 ve 6:165 ölçüm xref'lerindeki okunmuş ayetler xref kalıbının harekesiz sayımıyla bulunmadı — emsal alınmadı; 6:14, 6:108 ve 39:7 önceden basılmış; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('ilâ', 'sırât', 'mustaqîm', 'kâne', 'min', 'muşrik', 'allâh', 'rabb', ''âlem', 'qâle', 'ğayr', 'kull', 'şey'', 'kesebe', 'nefs', 'summe', 'merci'', 'nebbe'e', 'mâ', 'fî', 'ixtelefe', 'ellezî', 'ce'ale', 'refe'a', 'ba'd', 'fevq', 'derece', 'belev' (morph LEM ham biçim), 'âtâ'); joker '_' yalnız lemmasız 'huve' öğesinde ('dizi 6 165 1 3'); "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (161, 165): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_161_165.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b38k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '161', '165'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '161', '165', '40'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '161', '165', '40'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '161', '165', '40', '--tazelik-yok')}
    for _n in range(7, 35): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '161', '165', '40')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34 = [_R['B%d' % _n].splitlines() for _n in range(6, 35)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'B32_HEPSI': (B32[-1] if B32 else '?'), 'B33_HEPSI': (B33[-1] if B33 else '?'), 'B34_HEPSI': (B34[-1] if B34 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31, B32, B33, B34): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
