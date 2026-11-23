# sûre 6 blok 32 (6:136-138) ARIZA oluşturucu — bölüm 16-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b32/olcum.txt'
os.environ['SAY2'] = '/home/claude/b32/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b31.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {}
BOL = "'Ekinlerde ve hayvanlarda pay; sekiz eş'"


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
 ("6:137", "'mâ fe'ale yezere mâ iftarâ'", 2, 'say 6:137 16-20', "harekesiz 'mâ fe'alûh, fe-zerhum ve mâ yefterûn' (16-20. kelime)", None),
 ("6:137", "'lev şâ'e allâh mâ'", 2, 'say 6:137 13-16', "harekesiz 've lev şâ'e'llâhu mâ' (13-16. kelime); biçim öğesi 'lev' öneki (lemma dizisi sûre içi 3, nakarat3 2)", ('dizi 6 137 13 16', "lev şâ'e allâh mâ", '13-16', 'biçim farkı (dizi 6 137 13 16): 6:107 yazım eş; basılmamış eş önek; öneksiz eş koşusu (dizi 6 137 13 16): 6:107 → önek kesilmiş sûre içi 1; basılmamış eş → önek kesilmiş sûre içi 2')),
 ("6:137", "'şâ'e allâh mâ'", 3, 'say 6:137 14-16', "harekesiz 'şâ'e'llâhu mâ' (14-16. kelime)", ('dizi 6 137 14 16', "şâ'e allâh mâ", '14-16', 'biçim farkı (dizi 6 137 14 16): 6:107 yazım eş; basılmamış eş yazım eş; öneksiz eş koşusu (dizi 6 137 14 16): 6:107 → önek kesilmiş sûre içi 2; basılmamış eş → önek kesilmiş sûre içi 2')),
 ("6:138", "'zekere ism allâh'", 4, 'say 6:138 17-19', "harekesiz 'yezkurûne isma'llâh' (17-19. kelime)", ('dizi 6 138 17 19', 'zekere ism allâh', '17-19', 'biçim farkı (dizi 6 138 17 19): 6:118 fiil çekimi, zamir eki; 6:119 fiil çekimi, zamir eki; 6:121 fiil çekimi, zamir eki')),
 ("6:138", "'cezâ bi-mâ kâne'", 2, 'say 6:138 23-25', "harekesiz 'se-yeczîhim bi-mâ kânû' (23-25. kelime)", ('dizi 6 138 23 25', 'cezâ bi-mâ kâne', '23-25', 'biçim farkı (dizi 6 138 23 25): 6:120 fiil çekimi')),
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

VF_YAZI = {136: {1: "'ve ce'alû'", 7: "'ve'l-en'âmi'", 13: "'ve hâzâ'", 22: "'ve mâ'"}, 137: {1: "'ve kezâlike'", 10: "'ve li-yelbisû'", 13: "'ve lev'", 19: "'ve mâ'"}, 138: {1: "'ve qâlû'", 4: "'ve harsun'", 12: "'ve en'âmun'", 15: "'ve en'âmun'"}}
sys.path.insert(0, '/home/claude/b32/yap')
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
open('/home/claude/b32/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '32')
BLOKLAR = [str(i) for i in range(1, 33)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '32', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b32/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '136', '138', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b32/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b32/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '136', '138', '32').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_136_138.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:136', '6:137', '6:138'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_136_138.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(136, 139))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:136 kök حرث ('l-harsi' 6. kelime — ekin), kök سوأ ('sâ'e' 29. kelime — kötülük); 6:137 kök قتل ('qatle' 6. kelime — öldürme), kök ولد ('evlâdihim' 7. kelime — çocuk); 6:138 kök حرث ('harsun' 4. kelime — ekin), kök طعم ('yat'amuhâ' 7. kelime — yeme), kök ظهر ('zuhûruhâ' 14. kelime — sırt): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '136', '138', '32')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b32/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 33)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(136, 139))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 15 kapanışında sunum/bolum31_kurallar.py eklendi (kural 1-5), sunum/bolum19_kurallar.py KURAL_ATIF bölüm 15, sunum/geriye_donuk.py bolum31 satırı, sunum/mutasyon_sina.py b31 sınamaları; oturum sonunda sunum/yardimci/ (kurulum ve üretim yardımcıları; denetim aracı değil) eklendi; bu blokta araç değişikliği yok; mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 302",
 "geriye dönük koşu (bölüm 15 kapanışı, komut 'python3 sunum/geriye_donuk.py b31k yamalar/geriye_donuk_6_b28k.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 136 138 32'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:136, 6:137 ve 6:138 esmâ yok; 6:136 lafız (2., 11., 21. ve 24. kelime), 6:137 lafız (15. kelime), 6:138 lafız (19. kelime); blokta Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 136 138 32'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:136 '{{1|fâsıla يحكمون → ن, N sınıfı}}', '{{1|simetri \\[7, 13, 20, 2\\]}}', '{{1|harf 133 → harf3 127, isaret 6}}' ve '{{1|dış düğüm 0}}'; "
 "6:137 '{{2|fâsıla يفترون → ن, N sınıfı}}', '{{2|sayı işareti كَثِير}}', '{{2|harf 99 → harf3 95, isaret 4}}' ve '{{2|dış düğüm 0}}'; "
 "6:138 '{{3|EDİLGEN 1/8 fiil, pas z=0,38}}', '{{3|fâsıla يفترون → ن, N sınıfı}}', '{{3|simetri \\[3, 6, 20, 1\\]}}', '{{3|harf 121 → harf3 114, isaret 7}}', '{{3|dış düğüm 5}}' ve '{{3|İÇ düğüm 3}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 136 138 32'): KALAN_P",
 "ölçüm aktör: 6:136, 6:137 ve 6:138 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:136 haber — NEG 1 'fe-lâ' (18.); ölçüm biçim DIKKAT (D2'de yazılmadı); 6:137 emir, şart — COND 1 'lev' (13.), NEG 1 'mâ' (16.), IMPV 1 'fe-zerhum' (18.); "
 "6:138 haber — NEG 2 'lâ' (6.), 'lâ' (16.), RES 1 'illâ' (8.), FUT 1 'se-yeczîhim' (23.); ölçüm biçim DIKKAT + HASR (D2'de yazılmadı); "
 "morph SUP ('fe-lâ' 6:136 18., 'fe-huve' 6:136 25.), REM ('ve ce'alû' 6:136 1., 'fe-mâ' 6:136 15., 've lev' 6:137 13., 'fe-zerhum' 6:137 18.), PRP ('li-yurdûhum' 6:137 9., 've li-yelbisû' 6:137 10.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:136 ★★ (kaynak allah, z=2,05; eşiği geçen öbür ölçüler n z=1,97); 6:137 ve 6:138 yıldız yok",
 "fâsıla: 6:135 ن → 6:136 ن (يحكمون) → 6:137 ن (يفترون) → 6:138 ن (يفترون) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:136 xref yok; 6:137 xref yok; 6:138 22:36 (emsal olarak basıldı), 6:118 (basılmış), 6:119 (basılmış), 6:121 (basılmış) ve okunmuş 4 ayet",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:137 'mâ fe'ale yezere mâ iftarâ' süzgeç GEÇER, 'lev şâ'e allâh mâ' süzgeç GEÇER, 'şâ'e allâh mâ' süzgeç GEÇER; 6:138 'zekere ism allâh' süzgeç GEÇER, 'cezâ bi-mâ kâne' süzgeç GEÇMEZ; 6:136 nakarat3 yok",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4; çoğul zamirin göndergesi bölüm açılışında ayet içinde ad bulmuyor — 'tartışmalı' (sûre 6 bölüm 15 denetiminden GONDERGE_KAPSAM elle)): "
 "6:136 3MP ('ve ce'alû', 'fe-qâlû', 'yahkumûn' — tartışmalı; 'bi-za'mihim', 'li-şurakâ'ihim', 'şurakâ'ihim' ekleri — gönderge 've ce'alû' 1. kelime), konuşan 1P ('li-şurakâ'inâ' — söz içi), 3MS ('zera'e' — gönderge 'li'llâhi' 2. kelime; 'kâne', 'yesilu' — gönderge 'fe-mâ' 15. kelime; 'kâne', 'fe-huve', 'yesilu' — gönderge 've mâ' 22. kelime; 'sâ'e' — gönderge 'mâ' 30. kelime); "
 "6:137 3MS ('zeyyene' — fiil uyumu, fail 8. kelime; 'şâ'e' — fiil uyumu, fail 15. kelime; 'fe'alûh' eki — gönderge 'qatle' 6. kelime), 3MP ('evlâdihim', 'şurakâ'uhum', 'li-yurdûhum', ''aleyhim', 'dînehum', 'fe-zerhum' ekleri ve 'fe'alûh', 'yefterûn' — gönderge 'l-muşrikîne' 5. kelime; 'li-yurdûhum', 've li-yelbisû' — gönderge 'şurakâ'uhum' 8. kelime), muhatap 2MS ('fe-zerhum'); "
 "6:138 3MP ('ve qâlû' — tartışmalı; 'bi-za'mihim' eki — tartışmalı, gönderge 've qâlû' 1. kelime; 'yezkurûne', 'se-yeczîhim' eki, 'kânû', 'yefterûn' — gönderge 've qâlû' 1. kelime), 3MS ('yat'amuhâ' — söz içi, gönderge 'men' 9. kelime; ''aleyh' eki, 'se-yeczîhim' — gönderge 'llâhi' 19. kelime), 3FS ('yat'amuhâ' eki — söz içi, gönderge 'en'âmun' 3. kelime; 'hurrimet' — fiil uyumu, edilgen, naib-i faili 'zuhûruhâ' 14. kelime; 'zuhûruhâ' eki — gönderge 've en'âmun' 12. kelime; ''aleyhâ' eki — gönderge 've en'âmun' 15. kelime), konuşan 1P ('neşâ'u' — söz içi)",
 "6:136-138 gönderge zinciri: 6:136 1. kelimedeki 3MP özne bölüm açılışında ayet içinde ad bulmuyor; 6:137 'l-muşrikîne' (5. kelime) ve 6:138 've qâlû' (1. kelime) 6:136 1. kelimedeki özneyle eş topluluğa bağlanabilir (okuma; tartışmalı)",
 "edilgen: 6:138 'hurrimet' (13. kelime; naib-i faili 'zuhûruhâ' 14. kelime) — ölçüm EDİLGEN 1/8 bu kelimeden",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:136 'fe-qâlû' (9.) ardından söz 10-14. kelime — 'li-şurakâ'inâ' (14.) 1P ile kapanır; 'bi-za'mihim' (12.) 3MP eki taşıyan anlatıcı ara sözü, söz içinde; 15. kelimeden sonra anlatı ('fe-mâ' REM); "
 "6:138 've qâlû' (1.) ardından söz 2-10. kelime — 'neşâ'u' (10.) 1P ile kapanır; 'bi-za'mihim' (11.) anlatıcı ara sözü, söz dışında; 12-20. kelime 'en'âmun' bölümlemesi anlatı ('yezkurûne' 3MP) — söz sürmüyor (okuma); 6:137 söz yok — söz fiili yok (okuma); mealde 'dediler' sona alındı, tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 136 138 32' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:136 've ce'alû' (1.) REM, 've'l-en'âmi' (7.), 've hâzâ' (13.), 've mâ' (22.) CONJ; 6:137 've kezâlike' (1.), 've li-yelbisû' (10.), 've mâ' (19.) CONJ, 've lev' (13.) REM; 6:138 've qâlû' (1.), 've harsun' (4.), 've en'âmun' (12.), 've en'âmun' (15.) CONJ; "
 "'fe' konumları: 6:136 'fe-qâlû' (9.) CONJ, 'fe-mâ' (15.) REM, 'fe-lâ' (18.) ve 'fe-huve' (25.) SUP; 6:137 'fe-zerhum' (18.) REM",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:136 ◈B نعم ('l-en'âmi' 7. kelime — B1); 6:138 ◈B نعم ('en'âmun' 3. kelime — B1); 6:138 ◈B نعم ('en'âmun' 12. kelime — B1); 6:138 ◈B نعم ('en'âmun' 15. kelime — B1); 6:137 ◈K / ◈B tetik yok; 6:136-138 ◈K tetik yok",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 136 138 32'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 3 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:138 (22:36); 6:136 ve 6:137 bağ yok; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3; en uzun ortak lemma dizisi bag kaydında — sûre 6 bölüm 15 denetimi kuralı 5); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11); medde sayımının basılmış eşi (yazım farkı ile, D3 dışı): 'say 6:137 13-16 --medde' 6:107, 'say 6:137 14-16 --medde' 6:107",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:136 söz açılır (10. kelime), söz kapanır (14. kelime, ayet içi), şahıs geçişi 2 → 3, edim geçişi emir, nida → haber; bölüm açılışı; 6:137 şahıs geçişi yok, edim geçişi haber → emir, şart, şart → cevap (ayet içi; COND 'lev' 13. kelime), hitap açılır (ayet içi; 18. kelime muhatap 2MS — sûre 6 bölüm 15 denetiminden MUHATAP_DEGISIMI elle); "
 "6:138 söz açılır (2. kelime), söz kapanır (10. kelime, ayet içi), şahıs geçişi yok, edim geçişi emir, şart → haber; "
 "ölçüm iltifât 6:136-138 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:136 'fe-mâ kâne li-şurakâ'ihim fe-lâ yesilu' — ilgi zamirli özne ve cevap bağlacı (morph REM + SUP + NEG); 6:136 'sâ'e mâ yahkumûn' — yerme fiili ve ilgi zamiri (morph REL); 6:137 'li-yurdûhum' — amaç edatı (morph PRP); 've li-yelbisû' — atıf ve amaç (morph CONJ + PRP); "
 "6:137 'lev şâ'e'llâhu mâ fe'alûh' — 'lev' şartı ve olumsuz cevap (morph COND + NEG); 6:138 'lâ yat'amuhâ illâ men neşâ'u' — olumsuzluk ve istisna (morph NEG + RES); 6:138 ''ftirâ'en' — masdar, gerekçe (mef'ûlun leh) okuması (okuma)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:138 18-20. kelime — 22:36 ile harekesiz eş (sayım: 'say 6:138 18-20'); "
 "6:136 kök أله, شرك, كون, وصل ikilemeleri; 6:137 kök شرك ikilemesi; 6:138 kök فري, نعم ikilemeleri; 6:136 'bi-za'mihim' (12. kelime) ve 6:138 'bi-za'mihim' (11. kelime); kök حرث, نعم 6:136 ve 6:138'de",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 32'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2; sûre 6 bölüm 15 denetimi kuralı 3): "
 "'isma'llâh' 6:138 'Allah'ın adını' / 22:36 'Allah'ın adını' (emsal metninde) — çakışma değil (bayt eşit); 'isma'llâhi 'aleyhâ' 6:138 'üzerine Allah'ın adını' / 22:36 'üzerlerine Allah'ın adını' (emsal metninde) — çakışma — tam okuma sonu (iyelik eki çokluğu); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:136 'ce'alû' PERF — meal 'ayırdılar'; 'zera'e' PERF — meal 'yarattığı'; 'qâlû' PERF — meal 'dediler'; 'kâne' PERF — meal 'olan'; 'yesilu' IMPF IND ('lâ' ile) — meal 'ulaşmaz'; 'kâne' PERF — meal 'olan'; 'yesilu' IMPF IND — meal 'ulaşır'; 'sâ'e' PERF — meal 'ne kötüdür'; 'yahkumûn' IMPF IND — meal 'Hükmettikleri'; "
 "6:137 'zeyyene' PERF — meal 'süslü gösterdi'; 'yurdû' IMPF SUBJ — meal 'helâk etsinler'; 'yelbisû' IMPF SUBJ — meal 'karıştırsınlar'; 'şâ'e' PERF (şart) — meal 'dileseydi'; 'fe'alû' PERF ('mâ' ile) — meal 'yapmazlardı'; 'fe-zerhum' IMPV — meal 'bırak'; 'yefterûn' IMPF IND — meal 'uydurduklarını'; "
 "6:138 'qâlû' PERF — meal 'dediler'; 'yat'amu' IMPF IND ('lâ' ile) — meal 'yiyemez'; 'neşâ'u' IMPF IND — meal 'dilediğimiz'; 'hurrimet' PERF PASS — meal 'haram kılınmış'; 'yezkurûne' IMPF IND ('lâ' ile) — meal 'anmadıkları'; 'yeczî' IMPF IND ('se' ile) — meal 'cezalandıracaktır'; 'kânû' PERF — meal 'olduklarıyla'; 'yefterûn' IMPF IND — meal 'Uydurmakta'; "
 "kip sapma notu (sûre 6 bölüm 15 denetiminden KIP_SAPMA_NOTU elle): 'yefterûn' IMPF 6:137'de '-dukları', 6:138'de '-makta' ile — 'kânû' yardımcı fiili olan kalıpta süreklilik",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 136 138 32'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:136, 6:137 ve 6:138 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:136 ('fe-lâ yesilu ilâ'llâh' / 'fe-huve yesilu ilâ şurakâ'ihim'); 6:137 ve 6:138 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök أله 6:136 ('li'llâhi', 'li'llâhi', 'llâh', 'li'llâhi'), 6:137 ('llâhu') ve 6:138 ('llâhi'); kök حرث 6:136 ('l-harsi') ve 6:138 ('ve harsun'); kök نعم 6:136 ('ve'l-en'âmi') ve 6:138 ('en'âmun', 've en'âmun', 've en'âmun'); kök زعم 6:136 ('bi-za'mihim') ve 6:138 ('bi-za'mihim'); kök شرك 6:136 ('li-şurakâ'inâ', 'li-şurakâ'ihim', 'şurakâ'ihim') ve 6:137 ('l-muşrikîne', 'şurakâ'uhum'); kök قول 6:136 ('fe-qâlû') ve 6:138 ('ve qâlû'); kök كون 6:136 ('kâne', 'kâne') ve 6:138 ('kânû'); kök شيأ 6:137 ('şâ'e') ve 6:138 ('neşâ'u'); kök فري 6:137 ('yefterûn') ve 6:138 (''ftirâ'en', 'yefterûn'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 16-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 32, 33 ve 34; bölüm açılışı bu blokta; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b32/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 136 138 32'; lem_bozuk.py 32 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 136 138 → AYN_SONUC; sunum/bolum4_kurallar.py 136 138 32 → KHATA_HEPSI; sunum/bolum5_kurallar.py 136 138 32 → B5_HEPSI; sunum/bolum6_kurallar.py 136 138 32 → B6_HEPSI; sunum/bolum7_kurallar.py 136 138 32 → B7_HEPSI; sunum/bolum8_kurallar.py 136 138 32 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 136 138 32 → B9_HEPSI; sunum/bolum10_kurallar.py 136 138 32 → B10_HEPSI; sunum/bolum11_kurallar.py 136 138 32 → B11_HEPSI; sunum/bolum12_kurallar.py 136 138 32 → B12_HEPSI; sunum/bolum13_kurallar.py 136 138 32 → B13_HEPSI; sunum/bolum14_kurallar.py 136 138 32 → B14_HEPSI; sunum/bolum15_kurallar.py 136 138 32 → B15_HEPSI; sunum/bolum16_kurallar.py 136 138 32 → B16_HEPSI; sunum/bolum17_kurallar.py 136 138 32 → B17_HEPSI; sunum/bolum18_kurallar.py 136 138 32 → B18_HEPSI; sunum/bolum19_kurallar.py 136 138 32 → B19_HEPSI; sunum/bolum20_kurallar.py 136 138 32 → B20_HEPSI; sunum/bolum21_kurallar.py 136 138 32 → B21_HEPSI; sunum/bolum22_kurallar.py 136 138 32 → B22_HEPSI; sunum/bolum23_kurallar.py 136 138 32 → B23_HEPSI; sunum/bolum24_kurallar.py 136 138 32 → B24_HEPSI; sunum/bolum25_kurallar.py 136 138 32 → B25_HEPSI; sunum/bolum26_kurallar.py 136 138 32 → B26_HEPSI; sunum/bolum27_kurallar.py 136 138 32 → B27_HEPSI; sunum/bolum28_kurallar.py 136 138 32 → B28_HEPSI; sunum/bolum29_kurallar.py 136 138 32 → B29_HEPSI; sunum/bolum30_kurallar.py 136 138 32 → B30_HEPSI; sunum/bolum31_kurallar.py 136 138 32 → B31_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 32 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('mâ', 'fe'ale', 'yezere' (morph LEM ham biçim), 'iftarâ', 'lev', 'şâ'e', 'allâh', 'zekere', 'ism', ''alâ', 'cezâ', 'bi-mâ', 'kâne'); joker '_' kullanılmadı; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (136, 138): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_136_138.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b31k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '136', '138'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '136', '138', '32'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '136', '138', '32'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '136', '138', '32', '--tazelik-yok')}
    for _n in range(7, 32): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '136', '138', '32')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31 = [_R['B%d' % _n].splitlines() for _n in range(6, 32)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'B31_HEPSI': (B31[-1] if B31 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30, B31): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
