# sûre 6 blok 29 (6:122-125) ARIZA oluşturucu — bölüm 15-1
import sys, os, ast, subprocess, re, glob
os.environ['OLC'] = '/home/claude/b29/olcum.txt'
os.environ['SAY2'] = '/home/claude/b29/say2.txt'
sys.path.insert(0, '/home/claude/sunum')
from kes import kes
import sayim

BEK = ast.literal_eval('[' + open('/home/claude/yamalar/bekleyen_ariza_6_b28.txt', encoding='utf-8').read() + ']')
VF_YAZI_ESKI = {}
BOL = "'Ölüyken dirilen; cin ve insan toplulukları'"


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
 ("6:122", "'mâ kâne 'amile'", 3, 'say 6:122 22-24', "harekesiz 'mâ kânû ya'melûn' (22-24. kelime); biçim öğesi 'kâne' çekimi (lemma dizisi sûre içi 6, nakarat3 3)", ('dizi 6 122 22 24', "mâ kâne 'amile", '22-24', "biçim farkı (dizi 6 122 22 24): 6:43 yazım eş; 6:60 fiil çekimi, zamir eki, önek; 6:88 yazım eş; 6:108 önek; basılmamış eş önek; öneksiz eş koşusu (dizi 6 122 22 24): 6:43 → önek kesilmiş sûre içi 5; 6:60 → önek kesilmiş sûre içi 1; 6:88 → önek kesilmiş sûre içi 5; 6:108 → önek kesilmiş sûre içi 2; basılmamış eş → önek kesilmiş sûre içi 2")),
 ("6:123", "'illâ nefs mâ yeş'uru'", 2, 'say 6:123 12-15', "harekesiz 'illâ bi-enfusihim ve mâ yeş'urûn' (12-15. kelime)", ('dizi 6 123 12 15', "illâ nefs mâ şa'ara", '12-15', "biçim farkı (dizi 6 123 12 15): 6:26 i'râb, önek")),
 ("6:125", "'ellezî lâ âmene'", 3, 'say 6:125 26-28', "harekesiz 'llezîne lâ yu'minûn' (26-28. kelime)", ('dizi 6 125 26 28', 'ellezî lâ âmene', '26-28', 'biçim farkı (dizi 6 125 26 28): 6:113 yazım eş; basılmamış eş önek')),
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

VF_YAZI = {122: {1: "'e-ve-men'", 5: "'ve ce'alnâ'"}, 123: {1: "'ve kezâlike'", 10: "'ve mâ'", 14: "'ve mâ'"}, 124: {1: "'ve izâ'", 25: "'ve 'azâbun'"}, 125: {9: "'ve men'"}}
sys.path.insert(0, '/home/claude/b29/yap')
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
open('/home/claude/b29/yap/veri.py', 'w', encoding='utf-8').write('MK = %r\n' % MK)


def run(*a):
    return subprocess.run([sys.executable] + list(a), capture_output=True, text=True, cwd='/home/claude').stdout.strip()


ES = run('/home/claude/sunum/es_edat.py', '29')
BLOKLAR = [str(i) for i in range(1, 30)]
ESL = run('/home/claude/sunum/es_lemma.py', *BLOKLAR, '--numarasiz').replace('\n', '; ')
assert not re.search(r'[؀-ۿ]', ESL)
SON = run('/home/claude/sunum/sonradan.py', '--plan', '29', '--numarasiz').replace('\n', '; ')
EMS = open('/home/claude/b29/ems.txt').read().strip()
ONC = run('/home/claude/sunum/onceki_basim.py', '122', '125', EMS)
MED_L = [l for l in run('/home/claude/sunum/medde.py', '/home/claude/b29/say2.txt').splitlines() if l.startswith('MEDDE')]
MED = '%d meddeli kalıp (' % len(MED_L) + ', '.join(re.match(r'MEDDE (\S+ \S+ \S+(?: --on)?)', l).group(1) for l in MED_L) + ')'
sys.path.insert(0, '/home/claude/sunum'); import medde_fark
MEDF = medde_fark.satir('/home/claude/b29/say2.txt')  # bölüm 11 denetimi kuralı 6
GLS = run('/home/claude/sunum/gloss_tara.py', '122', '125', '29').splitlines()

_U = set()
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' not in _k: _U |= set(_d['basilan'])
_BAG = {x for _b in ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_122_125.txt', encoding='utf-8').read() + ']') for x in _b['bag'].split(' → ')}
_ON = {'6:122', '6:123', '6:124', '6:125'}
_UA = {}
for _k, (_n, _d) in sayim.S2.items():
    if '--medde' in _k: continue
    _m = re.match(r'(?:say|lem) \d+:(\d+)|dizi \d+ (\d+)', _k)
    if _m: _UA.setdefault(int(_m.group(1) or _m.group(2)), set()).update(_d['basilan'])
_BAGL = ast.literal_eval('[' + open('/home/claude/yamalar/bag_6_122_125.txt', encoding='utf-8').read() + ']')
def _d3(a_):
    ka = {b_['bag'].split(' → ')[0] for b_ in _BAGL if b_['bag'].split(' → ')[1] == '6:%d' % a_}
    x = sorted(_UA.get(a_, set()) - _ON - ka, key=lambda x: tuple(map(int, x.split(':'))))
    return '6:%d: %s' % (a_, ', '.join(x) if x else 'yok')
D3DISI = '; '.join(_d3(a_) for a_ in range(122, 126))  # bölüm 10 denetimi kuralı 11: ayet başına
ANILIS = "6:123 kök نفس ('bi-enfusihim' 13. kelime — kendi), kök شعر ('yeş'urûn' 15. kelime — farkında olma); 6:124 'izâ' (1. kelime — zaman zarfı, morph T); 6:125 kök صدر ('sadrahû' 7. ve 14. kelime — göğüs): tetik listesinde yok"
ARAC = run('/home/claude/sunum/arac_degisim.py')
EMH = run('/home/claude/sunum/esma_muhur.py', '122', '125', '29')
# bölüm 8 kuralı 6: meal karşılık farkı kararları — es_lemma satırları (bloğa dokunan) ve ◈D ayetler arası kalıpları
exec(open('/home/claude/b29/yap/karar_meal.py', encoding='utf-8').read())
_EL = run('/home/claude/sunum/es_lemma.py', *[str(i) for i in range(1, 30)])
_RW = [s_ for s_ in re.split(r'; |\n', _EL) if ' (morph LEM eşit): ' in s_ and any(re.search(r'\b6:%d:\d+' % a_, s_) for a_ in range(122, 126))]
MKK = '; '.join("%s — %s" % (s_.split(' (morph LEM eşit): ')[0], KM.get(s_.split(' (morph LEM eşit): ')[0], 'karar yok')) for s_ in _RW)
MKK += ''.join("; '%s' — %s" % (q_, KM.get("'%s'" % q_, 'karar yok')) for q_ in KQ)
MKK = MKK.lstrip('; ')  # sûre 6 bölüm 2 denetimi kuralı 10: boş alt madde
I = list(BEK) + [
 "araç değişikliği (bölüm 5 kuralı 11, bölüm 7 kuralı 10 — komut 'python3 sunum/arac_degisim.py'): " + ARAC + "; gerekçe: bölüm 14 kapanışında sunum/bolum30_kurallar.py eklendi (kural 1-5), sunum/bolum19_kurallar.py KURAL_ATIF bölüm 14, sunum/geriye_donuk.py bolum30 satırı, sunum/mutasyon_sina.py b30 sınamaları; bu blokta sunum/edat_etiket.py EDLEM sözlüğüne 'ke-enne' (كَأَنَّ, morph ACC) eklendi — bölüm 14 denetimi kuralı 1 (eş edat morph etiketi; es_edat tanınmayan başlık 0); mutasyon_sina — MUT_SONUC; "
 "basilan satır sayısı (blok anı): 274",
 "geriye dönük koşu (bölüm 14 kapanışı, komut 'python3 sunum/geriye_donuk.py b28k yamalar/geriye_donuk_6_b26k.txt'): GERI_P",
 "gloss kapsam taraması (komut 'python3 sunum/gloss_tara.py 122 125 29'; bölüm 7 kuralı 5: TARANMAYAN 0 olmadan teslim yok): " + ' · '.join(GLS) + "; tam okuma sonu",
 "esmâ: 6:122 've ce'alnâ lehû nûran' (5-7. kelime) — esma_el 'degil', kural 'esmâ adı esmâ dışı göndergeyle' (esmâ dışı gönderge) (yamalar/esma_el_6_122_125.txt); نُور lemmasında önceki kayıtlarla karar eş ('degil'); 6:123, 6:124 ve 6:125 esmâ yok; "
 "6:124 lafız (13., 14. ve 24. kelime), 6:125 lafız (3. ve 23. kelime); 6:122 ve 6:123 lafız ve Rab yok; blokta Rab yok (bölüm 6 kuralı 14 — betikle: B6_ESMA); A1'de esmâ anılmadı (bölüm 11 denetimi kuralı 7)",
 "esma_kayit (bölüm 8 kuralı 3 — komut 'python3 sunum/esma_muhur.py 122 125 29'; bölüm 13 denetimi kuralı 2; bölüm 15 denetimi kuralı 5): " + EMH,
 "ölçüm: 6:122 '{{1|esmâ نُور 7\\. sırada, ORTA konum, MÜHÜRSÜZ}}', '{{1|EDİLGEN 1/8 fiil, pas z=0,38}}', '{{1|fâsıla يعملون → ن, N sınıfı}}', '{{1|simetri \\[3, 1, 22, 1\\]}}', '{{1|harf 105 → harf3 97, isaret 8}}' ve '{{1|dış düğüm 1}}'; "
 "6:123 '{{2|fâsıla يشعرون → ن, N sınıfı}}', '{{2|simetri \\[3, 1, 10, 1\\]}}', '{{2|harf 70 → harf3 68, isaret 2}}' ve '{{2|dış düğüm 0}}'; "
 "6:124 '{{3|EDİLGEN 2/10 fiil, pas z=0,81}}', '{{3|fâsıla يمكرون → ن, N sınıfı}}', '{{3|simetri \\[3, 7, 10, 1\\]}}', '{{3|harf 128 → harf3 119, isaret 9}}' ve '{{3|dış düğüm 5}}'; "
 "6:125 '{{4|fâsıla يؤمنون → ن, N sınıfı}}', '{{4|simetri \\[3, 1, 9, 1\\]}}', '{{4|harf 116 → harf3 109, isaret 7}}' ve '{{4|dış düğüm 0}}' — satır aynen (◇'de de; bayt eşitliği satir_aynen araçlarıyla denetlendi); "
 "simetri / İÇ düğüm alanı olmayan ayetler (komut 'python3 sunum/bolum4_kurallar.py 122 125 29'): KALAN_P",
 "ölçüm aktör: 6:123 '{{2|aktör: adsız `karye` 5\\. sırada}}'; 6:125 '{{4|aktör: adlı إِسْلام 8\\. sırada \\(cins, rol mecrur\\)}}'; 6:122 ve 6:124 aktör yok",
 "ölçüm edim / kip (ayet ayet; D2 ölçüm etiketiyle; biçim etiketi D2'de yazılmaz — bölüm 10 denetimi kuralı 7): 6:122 soru — INTG 1 'e-ve-men' (1.); 6:123 haber — NEG 2 'mâ' (10., 14.), RES 1 'illâ' (12.), biçim HASR; "
 "6:124 haber — FUT 1 'se-yusîbu' (19.), NEG 1 'len' (5.); 6:125 şart — COND 2 'fe-men' (1.), 've men' (9.), NEG 1 'lâ' (27.); "
 "morph SUP ('ve' 6:122 1.), PRP ('li' 6:123 8.), SUB ('en' 6:125 4., 11.), ACC + PREV ('ke-ennemâ' 6:125 17.) ölçüm kipinde yok",
 "yıldız (bölüm 6 kuralı 13 — blok_bilanco yıldız kaynağı biçimiyle): 6:124 ★ (kaynak n, z=1,76; eşiği geçen öbür ölçüler allah z=1,54); 6:125 ★ (kaynak n, z=1,65); 6:122 ve 6:123 yıldız yok",
 "fâsıla: 6:121 ن → 6:122 ن (يعملون) → 6:123 ن (يشعرون) → 6:124 ن (يمكرون) → 6:125 ن (يؤمنون) — N sınıfı (ölçüm); aday 1042 için kayıt (test edilmedi)",
 "ölçüm xref (bölüm 10 denetimi kuralı 6, bölüm 13 denetimi kuralı 1, bölüm 15 denetimi kuralı 14): 6:122 okunmuş 1 ayet; 6:123 xref yok; 6:124 28:48 (emsal olarak basıldı) ve okunmuş 4 ayet; 6:125 xref yok",
 "araç tanımı farkları (R5 — nakarat3 'tür' alanı 'ic' sûre içi; sûre içi toplam = bu + basılmış sûre içi + okunmus_si + henuz_si; kalıp adı morph LEM ham adıyla, ◇ lemma dizisi adıyla eş, önceki bloklardaki adla öğe bazında eş (bölüm 12 denetimi kuralı 4), joker '_' yalnız lemmasız öğede; bölüm 6 kuralı 8: gerekçede terimler say2 anahtarıyla, bir ölçüden; bölüm 8 kuralı 1: kapanmayan satırda öneksiz eş koşusu; bölüm 13 denetimi kuralı 6: 'tutmuyor' satırı r5_gerekce çıktısını aynen taşır): " + '; '.join(r5),
 "nakarat3 (R3: kalıp adıyla özetlendi): 6:122 'mâ kâne 'amile' süzgeç GEÇER; 6:123 'illâ nefs mâ yeş'uru' süzgeç GEÇER; 6:124 nakarat3 yok; 6:125 'ellezî lâ âmene' süzgeç GEÇER",
 "aktör / ad (1017, R1; bölüm 3 kuralı 5, bölüm 4 kuralı 9, bölüm 5 kuralları 1 ve 14, bölüm 6 kuralı 15, bölüm 7 kuralı 3, bölüm 8 kuralları 7 ve 14 — ölçüt: zamirlerin hepsi 'adsız', etiketin kendi parantezinde; 2. şahıs 'muhatap', 1. şahıs 'konuşan' ile; alıntı ve kelime numarası ◇ konumuyla eş; "
 "A3 içi 1. / 2. şahıs 'söz içi' — bölüm 13 denetimi kuralı 5; fiilin ardındaki zamirsiz NOM ad 'fiil uyumu; fail' — bölüm 16 denetimi kuralı 1; başka ayete giden gönderge 'S:a N. kelime' — sûre 6 bölüm 2 denetimi kuralı 8; gönderge rol adıyla yazılmaz — sûre 6 bölüm 4 denetimi kuralı 4): "
 "6:122 3MS ('kâne', 'fe-ahyeynâhu' eki, 'lehû', 'yemşî' — gönderge 'e-ve-men' 1. kelime; 'bihî' — gönderge 'nûran' 7. kelime; 'meseluhû', 'leyse' — gönderge 'ke-men' 12. kelime; 'zuyyine' — fiil uyumu, edilgen), konuşan 1P ('fe-ahyeynâhu', 've ce'alnâ'), 3FS ('minhâ' — gönderge 'z-zulumâti' 15. kelime), 3MP ('kânû', 'ya'melûn' — gönderge 'li'l-kâfirîne' 21. kelime); "
 "6:123 konuşan 1P ('ce'alnâ'), 3FS ('mucrimîhâ', 'fîhâ' — gönderge 'qaryetin' 5. kelime), 3MP ('li-yemkurû', 'yemkurûne', 'bi-enfusihim', 'yeş'urûn' — gönderge 'ekâbira' 6. kelime); "
 "6:124 3FS ('câ'ethum' — fiil uyumu, fail 3. kelime), 3MP ('câ'ethum', 'qâlû' — gönderge 6:123 6. kelime; 'ecramû', 'kânû', 'yemkurûn' — gönderge 'llezîne' 20. kelime), konuşan 1P ('nu'mine', 'nu'tâ' — söz içi), 3MS ('ûtiye' — fiil uyumu, edilgen; 'yec'alu', 'risâletehû' — gönderge 'llâhu' 14. kelime; 'se-yusîbu' — fiil uyumu, fail 22. kelime); "
 "6:125 3MS ('yuridi', 'yec'alu' — fiil uyumu; 'yehdiyehû', 'yeşrah', 'yurid', 'yudillehû', 'yec'al' — gönderge 'llâhu' 3. kelime; 'yehdiyehû', 'sadrahû' ekleri — gönderge 'fe-men' 1. kelime; 'yudillehû', 'sadrahû' ekleri, 'yassa'adu' — gönderge 've men' 9. kelime), 3MP ('yu'minûn' — gönderge 'llezîne' 26. kelime) — betik denetimi: KHATA_ADSIZ; "
 "edilgen: 6:122 'zuyyine' (20. kelime; naib-i faili 'mâ' 22. kelime), 6:124 'nu'tâ' (8. kelime; naib-i fail konuşan zamiri) ve 'ûtiye' (11. kelime; naib-i faili 'rusulu' 12. kelime) — ölçüm EDİLGEN 1/8 ve 2/10 bu kelimelerden",
 "söz / tırnak (bölüm 3 kuralı 7, bölüm 4 kuralı 1, bölüm 14 denetimi kuralı 4, bölüm 15 denetimi kuralları 2-4, bölüm 16 denetimi kuralı 2): 6:124 'qâlû' (4.) ardından söz 5-13. kelime ('len nu'mine hattâ nu'tâ misle mâ ûtiye rusulu'llâh') — ayet içi kapanış; 6:122, 6:123 ve 6:125 söz yok — söz fiili yok (okuma); mealde tırnaksız (blok meal biçimi); "
 "REM sapması (komut 'python3 sunum/bolum4_kurallar.py 122 125 29' — A3 aralığında morph REM; bölüm 13 denetimi kuralı 3): KREM_P; "
 "morph 've' konumlarıyla kontrol edildi: 6:122 'e-ve-men' (1.) SUP, 've ce'alnâ' (5.) CONJ, 'fe-ahyeynâhu' (4.) 'fe' REM; 6:123 've kezâlike' (1.), 've mâ' (10., 14.) CONJ; 6:124 've izâ' (1.), 've 'azâbun' (25.) CONJ; 6:125 'fe-men' (1.) 'fe' REM, 've men' (9.) CONJ",
 "◈ tetik (alıntılar önek ve edatsız; alt sınıf kökten — betikle: KHATA_TETIK): 6:122 ◈B أنس ('n-nâsi' 11. kelime — B1); 6:122 ◈B موت ('meyten' 3. kelime — B4); 6:122 ◈B حيي ('ahyeynâhu' 4. kelime — B4; anlam notu: ölünün diriltilmesi, mecaz); 6:125 ◈K سمو ('s-semâ'i' 20. kelime — K1; anlam notu: benzetmedeki gök)",
 "tetik dışı tarama (bölüm 5 kuralı 7, bölüm 6 kuralı 4 — komut 'python3 sunum/bolum5_kurallar.py 122 125 29'): TETIKDISI; anılış: ANILIS_P; oturum_tetik kuru koşu 5 ayet / 0 uyuşmaz, oturum_xy 0 uyuşmaz",
 "◈D D3 / bag (R8): D3 eşleri bag listesiyle birebir — 6:124 (28:48); 6:122, 6:123 ve 6:125 bağ yok; ayetler arası kalıp yok (kontrol.py ile; bag alıntıları ◇ alt dizesi — bölüm 7 kuralı 6; bağ kalıbı say2 listesinde emsali buluyor — bölüm 9 kuralı 3); "
 "D3 dışı bırakılan basılmış sayım eşleri (bölüm 7 kuralı 7, bölüm 10 denetimi kuralı 11 — ayet başına, betikle): D3DISI_P — kalıp başına ölçüt: geniş kalıp ya da sûre içi basılmış eş, bağ kurulmadı (bölüm 3 kuralı 11); medde sayımının basılmış eşi (yazım farkı ile, D3 dışı): 'say 6:124 9-10 --medde' 5:95",
 "◈A A4 (R9 + kapsam; betikle: KHATA_A4): 6:122 şahıs geçişi 2 → 3, edim geçişi yasak, şart → soru, bölüm açılışı; 6:123 şahıs geçişi yok, edim geçişi soru → haber; "
 "6:124 söz açılır (5. kelime) / kapanır (13. kelime), şahıs geçişi yok, edim geçişi yok; 6:125 şahıs geçişi yok, edim geçişi haber → şart, şart → cevap ('men' 1. ve 9. kelime); "
 "ölçüm iltifât 6:122-125 için 0 (sûre 6 bölüm 2 denetimi kuralı 7)",
 "sözdizimi (okuma; morph etiketiyle): 6:122 'e-ve-men kâne meyten' — inkârî soru ve benzetme (morph SUP + INTG); 'leyse bi-xâricin' — 'leyse' haberinde zâid 'bi'; 6:123 've mâ yemkurûne illâ bi-enfusihim' — olumsuzluk ve hasr (morph CONJ + NEG, RES); "
 "6:124 'qâlû len nu'mine' — söz ve 'len' olumsuzluğu (morph NEG); 'se-yusîbu' — gelecek (morph FUT); 6:125 'fe-men yuridi'llâhu' — şart ve cevabı (morph REM + COND); 'ke-ennemâ yassa'adu' — benzetme (morph ACC + PREV)",
 "okuma (gözlem) (iddialar ölçüm ve morph ile; 'ile açılıyor' yalnız 1. kelimeden başlayan aralık için; ikileme iddiaları ölçüm kök ikilemesi alanından): 6:124 9-11. kelime — 28:48 ile harekesiz eş (sayım: 'say 6:124 9-11'); "
 "6:122 kök كون ikilemesi; 6:123 kök مكر ikilemesi; 6:124 kök أتي, أله, رسل ikilemeleri; 6:125 kök أله, جعل, رود, صدر ikilemeleri",
 "meal (okuma, tam okuma sonu): " + '; '.join(MEALS) + "; blok içi eş edat / zamir karşılıkları (komut 'python3 sunum/es_edat.py 29'): " + ES
 + "; eş lemmaya farklı karşılık (komut 'python3 sunum/es_lemma.py " + ' '.join(BLOKLAR) + " --numarasiz'; çıktı aynen — bölüm 10 denetimi kuralı 9): " + (ESL or 'yok')
 + "; emsal meal karşılık farkları (elle; bölüm 9 kuralı 3: yalnız emsalde geçen kalıp; bölüm 12 denetimi kuralı 2: kapalı sözlük; bölüm 13 denetimi kuralı 10: emsal alıntısı bayt eşit; bölüm 15 denetimi kuralı 7; sûre 6 bölüm 1 denetimi kuralları 1-3; sûre 6 bölüm 2 denetimi kuralı 2): "
 "'misle mâ ûtiye' 6:124 'verilenin benzeri' / 28:48 'verilenin benzeri' (emsal metninde) — çakışma değil (bayt eşit); 'misle mâ' 6:124 'benzeri' / 28:48 'benzeri' (emsal metninde) — çakışma değil (bayt eşit); "
 "kip notu (bölüm 15 denetimi kuralı 18, bölüm 16 denetimi kuralı 9; sûre 6 bölüm 2 denetiminden KIP_KAPSAM elle — her fiil): 6:122 'kâne' PERF — meal 'Ölüyken'; 'ahyeynâ' PERF — meal 'dirilttiğimiz'; 'ce'alnâ' PERF — meal 'verdiğimiz'; 'yemşî' IMPF IND — meal 'yürüdüğü'; 'leyse' PERF — meal 'çıkamayan'; 'zuyyine' PERF PASS — meal 'süslü gösterildi'; 'kânû' PERF — meal 'oldukları'; 'ya'melûn' IMPF IND — meal 'yapmakta'; "
 "6:123 'ce'alnâ' PERF — meal 'kıldık'; 'yemkurû' IMPF SUBJ — meal 'kursunlar'; 'yemkurûne' IMPF IND — meal 'kurarlar'; 'yeş'urûn' IMPF IND — meal 'olmazlar'; "
 "6:124 'câ'et' PERF ('izâ' ile) — meal 'geldiğinde'; 'qâlû' PERF — meal 'dediler'; 'nu'mine' IMPF SUBJ ('len' ile) — meal 'inanmayacağız'; 'nu'tâ' IMPF SUBJ PASS — meal 'verilinceye'; 'ûtiye' PERF PASS — meal 'verilenin'; 'yec'alu' IMPF IND — meal 'koyacağını'; 'yusîbu' IMPF IND ('se' ile) — meal 'erişecektir'; 'ecramû' PERF — meal 'işleyenlere'; 'kânû' PERF — meal 'olduklarından'; 'yemkurûn' IMPF IND — meal 'kurmakta'; "
 "6:125 'yuridi' IMPF JUS (şart) — meal 'isterse'; 'yehdiye' IMPF SUBJ — meal 'iletmek'; 'yeşrah' IMPF JUS (cevap) — meal 'açar'; 'yurid' IMPF JUS (şart) — meal 'isterse'; 'yudille' IMPF SUBJ — meal 'saptırmak'; 'yec'al' IMPF JUS (cevap) — meal 'kılar'; 'yassa'adu' IMPF IND — meal 'yükseliyormuş'; 'yec'alu' IMPF IND — meal 'kılar'; 'yu'minûn' IMPF IND — meal 'inanmayanların'",
 "meal karşılık farkı kararları (bölüm 8 kuralı 6, bölüm 10 denetimi kuralı 3, bölüm 11 denetimi kuralı 8 — es_lemma satırları ve ◈D ayetler arası kalıpları, betikle; kapalı sözlük 'çakışma değil' / 'çakışma — tam okuma sonu'): " + (MKK or 'karar gerektiren satır yok'),
 "meal takdirleri (bölüm 5 kuralı 9 — komut 'python3 sunum/bolum5_kurallar.py 122 125 29'): TAKDIR_P",
 "KARSILIK_CAKISMA",
 "çıpa: 6:125 tarayıcı adayı (kök سمو; A_şart) — çıpa değil: göğe yükselme benzetmesi, ölçü / mekanizma yok (olgu=False); 6:122, 6:123 ve 6:124 tarayıcı vermedi (cipa_tarama6_adaylari.json); L3 / L4 adayı yok",
 "aday 1039: 6:122 ('nûran' / 'z-zulumâti'); 6:125 ('yehdiyehû' / 'yudillehû'); 6:123 ve 6:124 karşıt çift yok; ayetler arası karşıt çift yok; eşleme betikle: ADAY_P",
 "aday 1041: kök كون 6:122 ('kâne', 'kânû') ve 6:124 ('kânû'); kök جعل 6:122 ('ce'alnâ'), 6:123 ('ce'alnâ'), 6:124 ('yec'alu') ve 6:125 ('yec'al', 'yec'alu'); kök مثل 6:122 ('meseluhû') ve 6:124 ('misle'); kök جرم 6:123 ('mucrimîhâ') ve 6:124 ('ecramû'); kök مكر 6:123 ('li-yemkurû', 'yemkurûne') ve 6:124 ('yemkurûn'); kök أمن 6:124 ('nu'mine') ve 6:125 ('yu'minûn'); kök أله 6:124 ('llâhi', 'llâhu', 'llâhi') ve 6:125 ('llâhu', 'llâhu'); okuma",
 "bölüm: " + BOL + " bölümü, bölüm 15-1 (bölüm 7 kuralı 9 — blok_plani_6.txt'ten) — bölüm blokları 29, 30 ve 31; bu blok bölümü açıyor; "
 "mercek_kayit['6']'daki eski ◇ notlarından bu bloğun ayetlerine düşenler blok yazılırken arşivlenir; medde taraması (sunum/medde.py b29/say2.txt): " + MED + "; " + MEDF,
 "ham LEM (bölüm 5 kuralı 5, bölüm 6 kuralı 3, bölüm 7 kuralı 11, bölüm 8 kuralı 9, bölüm 11 denetimi kuralı 5 — betikle: komut 'python3 sunum/bolum5_kurallar.py 122 125 29'; lem_bozuk.py 29 çıktısı): HAMLEM_P",
 "öz denetim (ayrı madde): sunum/ayn_kontrol.py 122 125 → AYN_SONUC; sunum/bolum4_kurallar.py 122 125 29 → KHATA_HEPSI; sunum/bolum5_kurallar.py 122 125 29 → B5_HEPSI; sunum/bolum6_kurallar.py 122 125 29 → B6_HEPSI; sunum/bolum7_kurallar.py 122 125 29 → B7_HEPSI; sunum/bolum8_kurallar.py 122 125 29 → B8_HEPSI; "
 "sunum/bolum9_kurallar.py 122 125 29 → B9_HEPSI; sunum/bolum10_kurallar.py 122 125 29 → B10_HEPSI; sunum/bolum11_kurallar.py 122 125 29 → B11_HEPSI; sunum/bolum12_kurallar.py 122 125 29 → B12_HEPSI; sunum/bolum13_kurallar.py 122 125 29 → B13_HEPSI; sunum/bolum14_kurallar.py 122 125 29 → B14_HEPSI; sunum/bolum15_kurallar.py 122 125 29 → B15_HEPSI; sunum/bolum16_kurallar.py 122 125 29 → B16_HEPSI; sunum/bolum17_kurallar.py 122 125 29 → B17_HEPSI; sunum/bolum18_kurallar.py 122 125 29 → B18_HEPSI; sunum/bolum19_kurallar.py 122 125 29 → B19_HEPSI; sunum/bolum20_kurallar.py 122 125 29 → B20_HEPSI; sunum/bolum21_kurallar.py 122 125 29 → B21_HEPSI; sunum/bolum22_kurallar.py 122 125 29 → B22_HEPSI; sunum/bolum23_kurallar.py 122 125 29 → B23_HEPSI; sunum/bolum24_kurallar.py 122 125 29 → B24_HEPSI; sunum/bolum25_kurallar.py 122 125 29 → B25_HEPSI; sunum/bolum26_kurallar.py 122 125 29 → B26_HEPSI; sunum/bolum27_kurallar.py 122 125 29 → B27_HEPSI; sunum/bolum28_kurallar.py 122 125 29 → B28_HEPSI; sunum/yasakli_sina.sh → yasakli sınama tamam; yasakli.sh IZIN listesine bu blokta ekleme yok",
 "sonradan basılan (komut 'python3 sunum/sonradan.py --plan 29 --numarasiz'; çıktı aynen): " + SON + " (geriye dönük düzeltme yok)",
 "korpusta 1 (kayıt; say2'deki tekil sayımlar betikle; öneksiz tekiller '--on' eşiyle — sûre 6 bölüm 1 denetimi kuralı 4): " + ', '.join(K1),
 "bağ: emsal " + ', '.join(EMS.split()) + " — emsal dosyası (AR + meal) teslim edildi; her emsal ayetinin bag'de gerekçesi var; önceki basım (sunum/onceki_basim.py): " + ONC + "; emsal işaretlemesi sayımdan önce yapıldı, say2.txt sayımı işaretlenmiş basılan listesiyle sınıflandı; "
 "lemma adları morph lemmasından ham transliterasyonla ('mâ', 'kâne', ''amile', 'zâ', 'zeyyene', 'illâ', 'nefs', 'şa'ara', 'yeş'uru' (morph LEM ham biçim), 'misl', 'âtâ', 'ellezî', 'lâ', 'âmene'); joker '_' kullanılmadı; "
 "transliterasyon yalnız ة / tanvin / 'l' birleşme yapıntıları; wasl 'va'' taraması 0; A1 alıntıları ◇ alt dizesi",
]

def yaz(II):
    items = [kes(x) for x in II]
    s = '\n (122, 125): [\n' + '\n'.join('  %r,' % x for x in items) + '\n ],'
    ast.literal_eval('{' + s + '}')
    open('/home/claude/yamalar/ariza_6_122_125.txt', 'w', encoding='utf-8').write(s)


I_HAM = list(I)
idx = I_HAM.index('KARSILIK_CAKISMA')
DOS = sorted(glob.glob('/home/claude/yamalar/ariza_6_*.txt'), key=lambda p: int(p.split('_')[-2]))
KY = {m.group(1) for L in MK.values() for tr, q, its in L for it in its for m in [re.match(r"'([^']+)' '(?:[^']|'(?=[a-zâîûçğışöü']))+' (?:karşılığı|açılımı)", it)] if m}  # bölüm 6 kuralı 2: bolum6_kurallar ile eş süzgeç
KARAR = {}
for nn in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29'):
    if os.path.exists('/home/claude/b%s/yap/karar.py' % nn): exec(open('/home/claude/b%s/yap/karar.py' % nn, encoding='utf-8').read())
MUT = run('/home/claude/sunum/mutasyon_sina.py').splitlines() if 'araç değişmedi' not in ARAC else ['mutasyon sınaması koşulmadı (araç değişmedi)']
GERI = open('/home/claude/yamalar/geriye_donuk_6_b28k.txt', encoding='utf-8').read().splitlines()[:3]
onceki = None
for tur in range(4):  # bölüm 6 kuralı 7: yapıştırılan araç çıktıları kararlı olana dek
    yaz([x if x != 'KARSILIK_CAKISMA' else 'karşılık çakışması (geçici)' for x in (I_cur if tur else I_HAM)])
    CAK = run('/home/claude/sunum/cakisma.py', *DOS)
    CAK_L = [l for l in CAK.splitlines() if ' ←' in l and (l.startswith('KÖK') or l.split(' ←')[0].strip() in KY)]
    from concurrent.futures import ThreadPoolExecutor as _TPE
    _J = {'AYN': ('/home/claude/sunum/ayn_kontrol.py', '122', '125'), 'KUR': ('/home/claude/sunum/bolum4_kurallar.py', '122', '125', '29'),
          'B5': ('/home/claude/sunum/bolum5_kurallar.py', '122', '125', '29'), 'B6': ('/home/claude/sunum/bolum6_kurallar.py', '122', '125', '29', '--tazelik-yok')}
    for _n in range(7, 31): _J['B%d' % _n] = ('/home/claude/sunum/bolum%d_kurallar.py' % _n, '122', '125', '29')
    with _TPE(8) as _ex: _R = {k_: _ex.submit(run, *v_) for k_, v_ in _J.items()}
    _R = {k_: f_.result() for k_, f_ in _R.items()}
    _R['B17'] = run(*_J['B17'])  # sûre 6 blok 16-17: bolum17 kural 14 esma_kayit.py'yi koşuyor — paralel koşuda esma_kayit.json yarışı; sırayla yeniden
    AYN = (_R['AYN'].splitlines() or ['?'])[-1]
    KUR = _R['KUR'].splitlines(); KH = [l for l in KUR if l.startswith('HATA')]
    B5 = _R['B5'].splitlines(); B5H = [l for l in B5 if l.startswith('HATA')]
    B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30 = [_R['B%d' % _n].splitlines() for _n in range(6, 31)]
    REP = {'AYN_SONUC': AYN, 'KREM_P': '; '.join(l[4:] for l in KUR if l.startswith('REM ')), 'KALAN_P': '; '.join(l[10:] for l in KUR if l.startswith('ALAN YOK: ')),
           'KHATA_ADSIZ': ('; '.join(h for h in KH if 'adsız' in h or 'muhatab' in h or 'A1 kapsamı' in h) or 'adsız / söz muhatabı / A1 kapsamı hatası 0 (her zamir etiketi)'), 'KHATA_TETIK': ('; '.join(h for h in KH if h.startswith('HATA ◈')) or '◈ alt sınıf hatası 0'),
           'KHATA_A4': ('; '.join(h for h in KH if 'A4' in h) or 'A4 şart → cevap hatası 0'), 'KHATA_HEPSI': (KUR[-1] if KUR else '?'),
           'TETIKDISI': next((l for l in B5 if l.startswith('tetik dışı')), '?'), 'TAKDIR_P': next((l for l in B5 if l.startswith('meal takdiri')), '?'),
           'ADAY_P': ('; '.join(h for h in B5H if 'aday 1039' in h) or next((l for l in B5 if l.startswith('aday 1039')), '?') + ' — ARIZA ⇔ ◇ bayt eşit'),
           'HAMLEM_P': '; '.join(l for l in B5 if l.startswith('ham LEM')), 'B5_HEPSI': (B5[-1] if B5 else '?'), 'B6_HEPSI': (B6[-1] if B6 else '?'), 'B7_HEPSI': (B7[-1] if B7 else '?'), 'B8_HEPSI': (B8[-1] if B8 else '?'), 'B9_HEPSI': (B9[-1] if B9 else '?'), 'B10_HEPSI': (B10[-1] if B10 else '?'), 'B11_HEPSI': (B11[-1] if B11 else '?'), 'B12_HEPSI': (B12[-1] if B12 else '?'), 'B13_HEPSI': (B13[-1] if B13 else '?'), 'B14_HEPSI': (B14[-1] if B14 else '?'), 'B15_HEPSI': (B15[-1] if B15 else '?'), 'B16_HEPSI': (B16[-1] if B16 else '?'), 'B17_HEPSI': (B17[-1] if B17 else '?'), 'B18_HEPSI': (B18[-1] if B18 else '?'), 'B19_HEPSI': (B19[-1] if B19 else '?'), 'B20_HEPSI': (B20[-1] if B20 else '?'), 'B21_HEPSI': (B21[-1] if B21 else '?'), 'B22_HEPSI': (B22[-1] if B22 else '?'), 'B23_HEPSI': (B23[-1] if B23 else '?'), 'B24_HEPSI': (B24[-1] if B24 else '?'), 'B25_HEPSI': (B25[-1] if B25 else '?'), 'B26_HEPSI': (B26[-1] if B26 else '?'), 'B27_HEPSI': (B27[-1] if B27 else '?'), 'B28_HEPSI': (B28[-1] if B28 else '?'), 'B29_HEPSI': (B29[-1] if B29 else '?'), 'B30_HEPSI': (B30[-1] if B30 else '?'), 'D3DISI_P': D3DISI, 'ANILIS_P': ANILIS,
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
for _x in (KUR, B5, B6, B7, B8, B9, B10, B11, B12, B13, B14, B15, B16, B17, B18, B19, B20, B21, B22, B23, B24, B25, B26, B27, B28, B29, B30): print([l for l in _x if l.startswith('HATA') or 'hata' in l])
